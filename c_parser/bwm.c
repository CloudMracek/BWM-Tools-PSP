#include "bwm.h"

BWM_Header* bwm_header(void *data) {
	return (BWM_Header*) data;
}

BWM_Vertex* bwm_vertices(void *data) {
	return (BWM_Vertex*) (data+sizeof(BWM_Header));
}

BWM_VertexIndice* bwm_vertex_indices(void *data) {
	BWM_Header* header = data;
	return (BWM_VertexIndice*) (data
		+sizeof(BWM_Header)
		+(sizeof(BWM_Vertex)*header->vertex_count));
}

BWM_UV* bwm_uvs(void *data) {
	BWM_Header* header = data;
	return (BWM_UV*) (data
		+sizeof(BWM_Header)
		+(sizeof(BWM_Vertex)*header->vertex_count)
		+(sizeof(BWM_VertexIndice)*header->faces_num));
}

BWM_UVIndice* bwm_uv_indices(void *data) {
	BWM_Header* header = data;
	return (BWM_UVIndice*) (data
		+sizeof(BWM_Header)
		+(sizeof(BWM_Vertex)*header->vertex_count)
		+(sizeof(BWM_VertexIndice)*header->faces_num)
		+(sizeof(BWM_UV)*header->uv_count));
}

BWM_Normal* bwm_normals(void *data) {
	BWM_Header* header = data;
	return (BWM_Normal*) (data
		+sizeof(BWM_Header)
		+(sizeof(BWM_Vertex)*header->vertex_count)
		+(sizeof(BWM_VertexIndice)*header->faces_num)
		+(sizeof(BWM_UV)*header->uv_count)
		+(sizeof(BWM_NormalIndice)*header->faces_num));
}

BWM_NormalIndice* bwm_normal_indices(void *data) {
	BWM_Header* header = data;
	return (BWM_NormalIndice*) (data
		+sizeof(BWM_Header)
		+(sizeof(BWM_Vertex)*header->vertex_count)
		+(sizeof(BWM_VertexIndice)*header->faces_num)
		+(sizeof(BWM_UV)*header->uv_count)
		+(sizeof(BWM_NormalIndice)*header->faces_num)
		+(sizeof(BWM_Normal)*header->normal_count));
}

