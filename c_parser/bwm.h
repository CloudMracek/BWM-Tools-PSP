#pragma once

typedef struct [[gnu::packed]] {
    unsigned int faces_num, vertex_count;
} BWM_Header;

typedef struct [[gnu::packed]] {
    float u,v;
    unsigned int vertex_color;
    float nx,ny,nz;
    float x,y,z;
} BWM_Vertex;

typedef struct [[gnu::packed]] {
    unsigned short v0,v1,v2;
} BWM_VertexIndice;


BWM_Header *bwm_header(void *data);

BWM_Vertex *bwm_vertices(void *data);

BWM_VertexIndice *bwm_vertex_indices(void *data);

