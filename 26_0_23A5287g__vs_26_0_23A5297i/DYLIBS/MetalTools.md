## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-370.56.0.0.0
-  __TEXT.__text: 0x12c1d8
+370.57.0.0.0
+  __TEXT.__text: 0x12c5c4
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x18cb4
+  __TEXT.__objc_methlist: 0x18d0c
   __TEXT.__cstring: 0x3160a
   __TEXT.__const: 0x2f8
   __TEXT.__gcc_except_tab: 0x2b68
   __TEXT.__oslogstring: 0x282e
-  __TEXT.__unwind_info: 0x50a8
+  __TEXT.__unwind_info: 0x50b0
   __TEXT.__objc_classname: 0x2520
   __TEXT.__objc_methname: 0x1e210
   __TEXT.__objc_methtype: 0x179cd
-  __TEXT.__objc_stubs: 0x165e0
-  __DATA_CONST.__got: 0xae8
+  __TEXT.__objc_stubs: 0x16600
+  __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__const: 0x1b28
   __DATA_CONST.__objc_classlist: 0x748
   __DATA_CONST.__objc_protolist: 0x4c8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 549B4C3F-4B8A-3156-ADBF-072A9FEA5606
-  Functions: 7660
-  Symbols:   24307
+  UUID: AC582AD7-CD00-399C-901C-6F79D6E2CEF0
+  Functions: 7667
+  Symbols:   24322
   CStrings:  10876
 
Symbols:
+ -[MTLDebugBuffer newTensorWithDescriptor:offset:error:]
+ -[MTLDebugDevice newTensorWithDescriptor:error:]
+ -[MTLDebugTensor newTensorViewWithReshapedDescriptor:error:]
+ -[MTLDebugTensor newTensorViewWithSlice:error:]
+ -[MTLGPUDebugDevice supportsBinaryArchives]
+ -[MTLToolsBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:]
+ -[MTLToolsCommandEncoder insertSplit]
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table200
+ GCC_except_table205
+ GCC_except_table209
+ GCC_except_table229
+ GCC_except_table239
+ _objc_msgSend$insertSplit
- GCC_except_table177
- GCC_except_table204
- GCC_except_table208
- GCC_except_table228
- GCC_except_table238

```
