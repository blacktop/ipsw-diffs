## DumpPanicRecoveryOS

> `/usr/libexec/DumpPanicRecoveryOS`

### Sections with Same Size but Changed Content

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
-  __TEXT.__text: 0x280a0
+37.0.0.0.0
+  __TEXT.__text: 0x28390
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_stubs: 0x2000
-  __TEXT.__objc_methlist: 0x70c
+  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_methlist: 0x76c
   __TEXT.__const: 0x250
-  __TEXT.__objc_methname: 0x1b04
-  __TEXT.__cstring: 0x26d2
-  __TEXT.__oslogstring: 0x4a7b
-  __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methtype: 0x52b
-  __TEXT.__gcc_except_tab: 0xad4
-  __TEXT.__unwind_info: 0x830
+  __TEXT.__objc_methname: 0x1b83
+  __TEXT.__cstring: 0x26cf
+  __TEXT.__oslogstring: 0x4a67
+  __TEXT.__objc_classname: 0xe9
+  __TEXT.__objc_methtype: 0x540
+  __TEXT.__gcc_except_tab: 0xb14
+  __TEXT.__unwind_info: 0x840
   __DATA_CONST.__const: 0x690
   __DATA_CONST.__cfstring: 0x2140
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   __DATA_CONST.__auth_got: 0x5f0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0xca8
-  __DATA.__objc_selrefs: 0x958
-  __DATA.__objc_ivar: 0x74
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0xdd8
+  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x228
   __DATA.__common: 0x30
   __DATA.__bss: 0xa88

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 818
+  Functions: 828
   Symbols:   266
-  CStrings:  1226
+  CStrings:  1243
 
CStrings:
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
+ "TC,N,V_agentId"
+ "TC,N,V_type"
+ "Warning: Failed to set AWL platform data from platformSocdBuffer in plane metadata"
+ "_agentId"
+ "_data"
+ "_type"
+ "agentId"
+ "firstObject"
+ "plane_node"
+ "setAgentId:"
+ "setData:"
+ "setPlaneMetadata:"
+ "setType:"
+ "v20@0:8C16"
- "Failed to allocate memory for report data, size: %zu"
- "Failed to get SOCD container size, report record ID: %d, error: %d"
- "Failed to open SOCD container size, report record ID: %d, error: %d"
- "Failed to read SOCD container report data, report record ID: %d, error: %d"
- "Warning: Failed to set AWL platform data from platformSocdBuffer in ensemble metadata"
- "ensemble_node"
- "setEnsembleMetadata:"
```
