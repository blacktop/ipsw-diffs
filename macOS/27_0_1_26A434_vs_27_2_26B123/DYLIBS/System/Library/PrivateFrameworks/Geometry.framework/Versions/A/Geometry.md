## Geometry

> `/System/Library/PrivateFrameworks/Geometry.framework/Versions/A/Geometry`

```diff

-67.0.5.0.0
-  __TEXT.__text: 0x1ac174
+67.40.1.0.0
+  __TEXT.__text: 0x1ac318
   __TEXT.__objc_methlist: 0x12d0
   __TEXT.__const: 0x161d8
-  __TEXT.__cstring: 0x16fc
-  __TEXT.__gcc_except_tab: 0x1604
+  __TEXT.__cstring: 0x172c
+  __TEXT.__gcc_except_tab: 0x1614
   __TEXT.__oslogstring: 0x256
   __TEXT.__constg_swiftt: 0x2028
   __TEXT.__swift5_typeref: 0x2c9c

   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__auth_ptr: 0x498
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x2560
-  __DATA.__data: 0x1878
+  __DATA.__data: 0x17b0
   __DATA.__bss: 0x62f0
-  __DATA_DIRTY.__objc_data: 0x1a90
+  __DATA_DIRTY.__objc_data: 0x1ae0
+  __DATA_DIRTY.__data: 0x2628
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 9606
   Symbols:   10313
-  CStrings:  190
+  CStrings:  191
 
Functions:
~ __ZN4geom2mp44add_vertex_face_adjacency_attributes_to_meshERNS0_4meshE : 528 -> 552
~ __ZN4geom2mp49remapVerticesOnVertexFaceAdjacencyTableAttributesERNS0_4meshERKS1_RKNS0_9index_mapE : 704 -> 744
~ __ZN4geom2mp25makeConditionedMeshForGPUERKNS0_4meshERS1_RNS0_9index_mapES6_RKNS0_24gpu_conditioning_optionsE : 2780 -> 3108
~ __ZN4geom2mp32compute_vertex_face_connectivityERKNS0_4meshERNSt3__16vectorIjNS4_9allocatorIjEEEES9_ : 516 -> 544
CStrings:
+ "Vertex-face adjacency table overflowed. "
```
