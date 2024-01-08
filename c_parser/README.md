# Simple BWM parser

## Example usage:

```c
BWM_Header* header = bwm_header(cube);
BWM_Vertex* vertices = bwm_vertices(cube);
BWM_VertexIndice* vertex_indices = bwm_vertex_indices(cube);
BWM_UV* uvs = bwm_uvs(cube);
BWM_UVIndice* uv_indices = bwm_uv_indices(cube);
BWM_Normal* normals = bwm_normals(cube);
BWM_NormalIndice* normal_indices = bwm_normal_indices(cube);

printf("Vertices:\n");
for(int i = 0; i < header->vertex_count; i++) {
	printf("color: %x, POS:%f,%f,%f\n", vertices[i].vertex_color, vertices[i].x, vertices[i].y, vertices[i].z);
}
printf("----------------------------:\n");
printf("Vertex indices:\n");
for(int i = 0; i < header->faces_num; i++) {
	printf("%d,%d,%d\n", vertex_indices[i].v0, vertex_indices[i].v1, vertex_indices[i].v2);
}
printf("----------------------------:\n");
printf("UVs:\n");
for(int i = 0; i < header->uv_count; i++) {
	printf("%f,%f\n", uvs[i].u, uvs[i].v);
}
printf("----------------------------:\n");
printf("UV indices:\n");
for(int i = 0; i < header->faces_num; i++) {
	printf("%d,%d,%d\n", uv_indices[i].v0, uv_indices[i].v1, uv_indices[i].v2);
}
printf("----------------------------:\n");
printf("Normals:\n");
for(int i = 0; i < header->normal_count; i++) {
	printf("%f,%f,%f\n", normals[i].x, normals[i].y, normals[i].z);
}
printf("----------------------------:\n");
printf("Normal indices:\n");
for(int i = 0; i < header->faces_num; i++) {
	printf("%d,%d,%d\n", normal_indices[i].v0, normal_indices[i].v1, normal_indices[i].v2);
}
```
