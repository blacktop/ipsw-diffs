## com.apple.gpusw.ParavirtualizedGraphicsGPUTask

> `/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/XPCServices/com.apple.gpusw.ParavirtualizedGraphicsGPUTask.xpc/Contents/MacOS/com.apple.gpusw.ParavirtualizedGraphicsGPUTask`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-71.0.8.0.0
-  __TEXT.__text: 0x66bb4
+71.0.12.0.0
+  __TEXT.__text: 0x67688
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x6620
-  __TEXT.__objc_methlist: 0x2420
+  __TEXT.__objc_stubs: 0x66e0
+  __TEXT.__objc_methlist: 0x2460
   __TEXT.__objc_classname: 0x4d1
-  __TEXT.__objc_methname: 0x75c7
-  __TEXT.__objc_methtype: 0x2ac1
-  __TEXT.__cstring: 0x4f22
-  __TEXT.__gcc_except_tab: 0x6a6c
+  __TEXT.__objc_methname: 0x7649
+  __TEXT.__objc_methtype: 0x2c05
+  __TEXT.__cstring: 0x5052
+  __TEXT.__gcc_except_tab: 0x6b5c
   __TEXT.__const: 0x33c8
   __TEXT.__oslogstring: 0x1038
-  __TEXT.__unwind_info: 0x2600
-  __DATA_CONST.__const: 0x850
+  __TEXT.__unwind_info: 0x2610
+  __DATA_CONST.__const: 0x830
   __DATA_CONST.__cfstring: 0x1020
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__auth_got: 0x440
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x3438
-  __DATA.__objc_selrefs: 0x1b60
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_const: 0x3478
+  __DATA.__objc_selrefs: 0x1b90
+  __DATA.__objc_ivar: 0x228
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x5a0
   __DATA.__common: 0x410

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1582
+  Functions: 1587
   Symbols:   426
-  CStrings:  1914
+  CStrings:  1931
 
Symbols:
+ __Z36newRenderPipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectP39PGResourceManagerDeserializationContextNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z37newComputePipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectP39PGResourceManagerDeserializationContextNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
+ __Z40newRenderPipelineStateWithTileDescriptorPU19objcproto9MTLDevice11objc_objectP39PGResourceManagerDeserializationContextNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
- __Z36newRenderPipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
- __Z37newComputePipelineStateWithDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
- __Z40newRenderPipelineStateWithTileDescriptorPU19objcproto9MTLDevice11objc_objectPU36objcproto25MTLDeserializationContext11objc_objectNSt3__110shared_ptrI21PGVirtualMemoryCursorEEP18APVObjectPlacement
CStrings:
+ "Compute pipeline descriptor has nil computeFunction"
+ "Failed to alloc descriptor data"
+ "Function lookup failed during pipeline deserialization: {}"
+ "Render pipeline descriptor has nil vertexFunction"
+ "Tile pipeline descriptor has nil tileFunction"
+ "Unresolvable render pipeline for ref({}): {}"
+ "_firstFailureReason"
+ "_hadFailure"
+ "computeFunction"
+ "firstFailureReason"
+ "function ref {}: {}"
+ "hadLookupFailure"
+ "resetFailureState"
+ "tileFunction"
+ "vertexFunction"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
```
