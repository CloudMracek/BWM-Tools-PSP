# A simple obj converter for the BWM model format

import argparse
import struct
from os.path import exists
import os

def pack_int_number(num):
    int_to_four_bytes = struct.Struct('<i').pack
    return int_to_four_bytes(num)

def pack_uint_number(num):
    int_to_four_bytes = struct.Struct('<I').pack
    return int_to_four_bytes(num)

def pack_float_number(num):
    float_to_four_bytes = struct.Struct('<f').pack
    return float_to_four_bytes(num)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input OBJ file")
    parser.add_argument("output_file", help="Output BWM file")
    args = parser.parse_args()
    
    try:
        obj_file = open(args.input_file, "r")
    except:
        print("Failed to open the input file:", args.input_file)
        exit()
    try:
        if not args.output_file.endswith(".bwm"):
            args.output_file = args.output_file + ".bwm"
        if exists(args.output_file):
            print("The output file already exists. Would you like to overwrite it? [Y/n]")
            reply = input().lower().strip()
            if reply == "y" or len(reply) == 0:
                os.remove(args.output_file)
            else:
                exit()
        bwm_file = open(args.output_file, "wb")
    except Exception as e:
        obj_file.close()
        print("Failed to open the output file:", args.output_file)
        print(e)
        exit()

    vertices = []
    vertex_indices = []

    uvs = []
    uv_indices = []

    normals = []
    normal_indices = []

    num_faces = 0
    
    for line in obj_file:
        data = line.split(" ")
        operation = data[0]

        if operation == "v":
            x = float(data[1])
            y = float(data[2])
            z = float(data[3])
            
            vertices.append([x,y,z])
        
        elif operation == "vt":
            u = float(data[1])
            v = float(data[2])

            if(u < 0):
                u = 0
            if(v < 0):
                v = 0
            
            uvs.append([u,v])
        
        elif operation == "vn":
            x = float(data[1])
            y = float(data[2])
            z = float(data[3])
            
            normals.append([x,y,z])
        elif operation == "f":
            v0 = data[1].split("/")
            v1 = data[2].split("/")
            v2 = data[3].split("/")

            vi_0 = int(v0[0])
            vi_1 = int(v1[0])
            vi_2 = int(v2[0])
            
            
            ui_0 = int(v0[1])
            ui_1 = int(v1[1])
            ui_2 = int(v2[1])
            
            ni_0 = int(v0[2])
            ni_1 = int(v1[2])
            ni_2 = int(v2[2])

            uv_indices.append([ui_0-1, ui_1-1, ui_2-1])
            vertex_indices.append([vi_0-1, vi_1-1, vi_2-1])
            normal_indices.append([ni_0-1, ni_1-1, ni_2-1])
            num_faces += 1
    
    bwm_file.write(pack_uint_number(num_faces))
    bwm_file.write(pack_uint_number(len(vertices)))
    bwm_file.write(pack_uint_number(len(uvs)))
    bwm_file.write(pack_uint_number(len(normals)))

    for vertex in vertices:
        bwm_file.write(pack_uint_number(0xFFFFFFFF))
        for coord in vertex:
            bwm_file.write(pack_float_number(coord))

    for face in vertex_indices:
        for indice in face:
            bwm_file.write(pack_uint_number(indice))

    for uv in uvs:
        for coord in uv:
            bwm_file.write(pack_float_number(coord))
    
    for face in uv_indices:
        for indice in face:
            bwm_file.write(pack_uint_number(indice))
    
    for normal in normals:
        for coord in normal:
            bwm_file.write(pack_float_number(coord))

    for face in normal_indices:
        for indice in face:
            bwm_file.write(pack_uint_number(indice))

    bwm_file.close()

    print("The file:",args.output_file, "was successfully written")
    print("Vertex count:", len(vertices))
    print("Vertex indices count:", len(vertex_indices))
    print("UV count:", len(uvs))
    print("UV indices count:", len(uv_indices))
    print("Normal count:", len(normals))
    print("Normal indices count:", len(normal_indices))

