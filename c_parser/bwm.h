#pragma once

typedef struct {
    unsigned int faces_num, vertex_count, uv_count, normal_count;
} BWM_Header;

typedef struct {
    unsigned int vertex_color;
    float x,y,z;
} BWM_Vertex;

typedef struct {
    unsigned int v0,v1,v2;
} BWM_VertexIndice;

typedef struct {
    float u,v;
} BWM_UV;

typedef struct {
    unsigned int v0,v1,v2;
} BWM_UVIndice;

typedef struct {
    float x,y,z;
} BWM_Normal;

typedef struct {
    unsigned int v0,v1,v2;
} BWM_NormalIndice;

BWM_Header *bwm_header(void *data);

BWM_Vertex *bwm_vertices(void *data);

BWM_VertexIndice *bwm_vertex_indices(void *data);

BWM_UV *bwm_uvs(void *data);

BWM_UVIndice *bwm_uv_indices(void *data);

BWM_Normal *bwm_normals(void *data);

BWM_NormalIndice *bwm_normal_indices(void *data);
