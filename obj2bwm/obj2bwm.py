# A simple obj converter for the BWM model format

import argparse
import struct
from os.path import exists
import os

def pack_short_number(num):
    int_to_four_bytes = struct.Struct('<H').pack
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
            
            uvs.append([round(u,2),round(v,2)])
        
        elif operation == "vn":
            x = float(data[1])
            y = float(data[2])
            z = float(data[3])
            
            normals.append([x,y,z])
        elif operation == "f":
            v0 = data[1].split("/")
            v1 = data[2].split("/")
            v2 = data[3].split("/")

            vi_2 = int(v0[0])
            vi_1 = int(v1[0])
            vi_0 = int(v2[0])
            
            
            ui_2 = int(v0[1])
            ui_1 = int(v1[1])
            ui_0 = int(v2[1])
            
            ni_2 = int(v0[2])
            ni_1 = int(v1[2])
            ni_0 = int(v2[2])

            uv_indices.append(ui_0-1)
            uv_indices.append(ui_1-1)
            uv_indices.append(ui_2-1)

            vertex_indices.append(vi_0-1)
            vertex_indices.append(vi_1-1)
            vertex_indices.append(vi_2-1)
            
            normal_indices.append(ni_0-1)
            normal_indices.append(ni_1-1)
            normal_indices.append(ni_2-1)
            num_faces += 1
    

    combined_data = []
    unique_data_map = {}
    new_indices = []

    # Combine vertices and uvs into a single array
    for vertex_index, uv_index, normal_index in zip(vertex_indices, uv_indices, normal_indices):
        vertex_uv_pair = tuple(uvs[uv_index] + [0xffffffff] + normals[normal_index] + vertices[vertex_index]) 
        if vertex_uv_pair not in unique_data_map:
            unique_data_map[vertex_uv_pair] = len(unique_data_map)
            combined_data.extend(vertex_uv_pair)

        new_indices.append(unique_data_map[vertex_uv_pair])
    formatted_combined_data = [tuple(combined_data[i:i+9]) for i in range(0, len(combined_data), 9)]
    for data in formatted_combined_data:
        print(f"U: {data[0]}, V: {data[1]}, 0xffffffff, NX: {data[3]}, NY: {data[4]}, NZ: {data[5]}, X: {data[6]}, Y: {data[7]}, Z: {data[8]}")
        


    bwm_file.write(pack_uint_number(num_faces))
    bwm_file.write(pack_uint_number(len(formatted_combined_data)))

    for vertex in formatted_combined_data:
        for byte in vertex:
            if not isinstance(byte, float):
                bwm_file.write(pack_uint_number(byte))
            else:
                bwm_file.write(pack_float_number(byte))
    
    for byte in new_indices:
        bwm_file.write(pack_short_number(byte))
    
    bwm_file.close()

    print("The file:",args.output_file, "was successfully written")
    print("Vertex count:", len(formatted_combined_data))
    print("Vertex indices count:", len(new_indices))
    print("Face cout:" , num_faces)


