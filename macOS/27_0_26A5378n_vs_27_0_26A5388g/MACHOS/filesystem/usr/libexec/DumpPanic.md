## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x2dd8c
+37.0.0.0.0
+  __TEXT.__text: 0x2e07c
   __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_stubs: 0x2540
-  __TEXT.__objc_methlist: 0x894
-  __TEXT.__cstring: 0x2bab
-  __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methtype: 0x556
-  __TEXT.__objc_methname: 0x1fd4
+  __TEXT.__objc_stubs: 0x25e0
+  __TEXT.__objc_methlist: 0x8f4
+  __TEXT.__cstring: 0x2b9b
+  __TEXT.__objc_classname: 0x12c
+  __TEXT.__objc_methtype: 0x56b
+  __TEXT.__objc_methname: 0x2043
   __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0xc14
-  __TEXT.__oslogstring: 0x5018
+  __TEXT.__gcc_except_tab: 0xc54
+  __TEXT.__oslogstring: 0x5008
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__unwind_info: 0x8f8
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__cfstring: 0x22c0
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__objc_const: 0xfe0
-  __DATA.__objc_selrefs: 0xab8
-  __DATA.__objc_ivar: 0x98
-  __DATA.__objc_data: 0x4d8
+  __DATA.__objc_const: 0x1110
+  __DATA.__objc_selrefs: 0xaf0
+  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_data: 0x528
   __DATA.__data: 0x3d8
   __DATA.__common: 0x28
   __DATA.__bss: 0xaa8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 894
+  Functions: 904
   Symbols:   370
-  CStrings:  1352
+  CStrings:  1369
 
CStrings:
+ "  -e, --plane FILE\n              use plane panic test input JSON file with multiple nodes\n\n"
+ "C"
+ "C16@0:8"
+ "Failed to allocate %zu bytes for report %d"
+ "Failed to create SOCD handle: %d"
+ "Failed to get SOCD v2 container agent ID: %d, num_agents: %zu"
+ "Failed to load SOCD container: %d"
+ "Failed to open report %d: %d"
+ "Failed to read report data for report %d: %d"
+ "SOCDReportInfo"
+ "T@\"NSData\",&,N,V_data"
+ "T@\"NSURL\",&,V_plane_json"
+ "TC,N,V_agentId"
+ "TC,N,V_type"
+ "Warning: Failed to set AWL platform data from platformSocdBuffer in plane metadata"
+ "_agentId"
+ "_data"
+ "_plane_json"
+ "_type"
+ "agentId"
+ "firstObject"
+ "plane"
+ "plane_json"
+ "plane_node"
+ "setAgentId:"
+ "setData:"
+ "setPlaneMetadata:"
+ "setPlane_json:"
+ "setType:"
+ "v20@0:8C16"
- "  -e, --ensemble FILE\n              use ensemble panic test input JSON file with multiple nodes\n\n"
- "Failed to allocate memory for report data, size: %zu"
- "Failed to get SOCD container size, report record ID: %d, error: %d"
- "Failed to open SOCD container size, report record ID: %d, error: %d"
- "Failed to read SOCD container report data, report record ID: %d, error: %d"
- "T@\"NSURL\",&,V_ensemble_json"
- "Warning: Failed to set AWL platform data from platformSocdBuffer in ensemble metadata"
- "_ensemble_json"
- "ensemble"
- "ensemble_json"
- "ensemble_node"
- "setEnsembleMetadata:"
- "setEnsemble_json:"
```
