## Geometry

> `/System/Library/PrivateFrameworks/Geometry.framework/Geometry`

```diff

-67.0.5.0.0
-  __TEXT.__text: 0x1bd7e0
+67.40.1.0.0
+  __TEXT.__text: 0x1bd96c
   __TEXT.__objc_methlist: 0x12d0
   __TEXT.__const: 0x161c8
-  __TEXT.__cstring: 0x16fc
-  __TEXT.__gcc_except_tab: 0x1660
+  __TEXT.__cstring: 0x172c
+  __TEXT.__gcc_except_tab: 0x1670
   __TEXT.__oslogstring: 0x256
   __TEXT.__constg_swiftt: 0x2028
   __TEXT.__swift5_typeref: 0x2c9c

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 9648
   Symbols:   10358
-  CStrings:  190
+  CStrings:  191
 
Functions:
~ __ZN4geom2mp44add_vertex_face_adjacency_attributes_to_meshERNS0_4meshE : 548 -> 572
~ __ZN4geom2mp49remapVerticesOnVertexFaceAdjacencyTableAttributesERNS0_4meshERKS1_RKNS0_9index_mapE : 740 -> 780
~ __ZN4geom2mp25makeConditionedMeshForGPUERKNS0_4meshERS1_RNS0_9index_mapES6_RKNS0_24gpu_conditioning_optionsE : 2812 -> 3140
~ __ZN4geom2mp32compute_vertex_face_connectivityERKNS0_4meshERNSt3__16vectorIjNS4_9allocatorIjEEEES9_ : 672 -> 676
CStrings:
+ "Vertex-face adjacency table overflowed. "
```
