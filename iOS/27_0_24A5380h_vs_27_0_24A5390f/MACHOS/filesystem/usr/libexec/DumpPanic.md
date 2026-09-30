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
-  __TEXT.__text: 0x2aee4
+37.0.0.0.0
+  __TEXT.__text: 0x2b194
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_stubs: 0x25a0
-  __TEXT.__objc_methlist: 0x85c
-  __TEXT.__cstring: 0x2b9b
-  __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methtype: 0x531
-  __TEXT.__objc_methname: 0x1f55
+  __TEXT.__objc_stubs: 0x2640
+  __TEXT.__objc_methlist: 0x8bc
+  __TEXT.__cstring: 0x2b8b
+  __TEXT.__objc_classname: 0x12c
+  __TEXT.__objc_methtype: 0x546
+  __TEXT.__objc_methname: 0x1fc4
   __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0xb78
-  __TEXT.__oslogstring: 0x48e8
+  __TEXT.__gcc_except_tab: 0xbb8
+  __TEXT.__oslogstring: 0x48d8
   __TEXT.__ustring: 0x1c6
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__unwind_info: 0x8d0
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__cfstring: 0x2400
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   __DATA_CONST.__auth_got: 0x8d8
   __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA.__objc_const: 0xfb0
-  __DATA.__objc_selrefs: 0xac8
-  __DATA.__objc_ivar: 0x94
-  __DATA.__objc_data: 0x4d8
+  __DATA.__objc_const: 0x10e0
+  __DATA.__objc_selrefs: 0xb00
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_data: 0x528
   __DATA.__data: 0x3b8
   __DATA.__common: 0x28
   __DATA.__bss: 0xab8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 853
+  Functions: 863
   Symbols:   400
-  CStrings:  1317
+  CStrings:  1334
 
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
