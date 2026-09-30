## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_bss`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-2027.0.33.0.0
-  __TEXT.__text: 0x29665c
+2027.0.35.0.0
+  __TEXT.__text: 0x296c3c
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0x184c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1359c
-  __TEXT.__const: 0xa020
-  __TEXT.__cstring: 0x30821
+  __TEXT.__const: 0xa030
+  __TEXT.__cstring: 0x3085f
   __TEXT.__oslogstring: 0x2418
   __TEXT.__gcc_except_tab: 0x1634
   __TEXT.__objc_methname: 0x1b911
   __TEXT.__objc_classname: 0x15da
   __TEXT.__objc_methtype: 0xafc9
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x4c68
+  __TEXT.__unwind_info: 0x4c70
   __DATA_CONST.__const: 0x2198
   __DATA_CONST.__cfstring: 0x4980
   __DATA_CONST.__objc_classlist: 0x358

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9823
-  Symbols:   16252
-  CStrings:  9425
+  Functions: 9825
+  Symbols:   16254
+  CStrings:  9426
 
Symbols:
+ _DYTraceDecode_MTLDevice_newSharedEventWithOptions
+ _DYTraceEncode_MTLDevice_newSharedEventWithOptions
Functions:
~ -[CaptureMTLDevice newSharedEventWithOptions:] : 128 -> 316
~ _ResourceTracker_addLibraries : 2480 -> 2492
~ _GTSMMTLSharedEvent_processTraceFuncWithMap : 440 -> 516
~ _GTSMMTLSharedEvent_processTraceFuncWithPool : 440 -> 516
~ _GTTraceFuncToFbuf : 232844 -> 233012
+ _DYTraceEncode_MTLDevice_newSharedEventWithOptions
~ _GTFenum_getConstructorType : 3072 -> 3088
~ _MakeDYMTLAccelerationStructureMotionTriangleGeometryDescriptor : 448 -> 456
~ _MakeDYMTLTensorAuxiliaryPlaneDescriptorMap : 140 -> 168
~ _DecodeDYMTLRasterizationRateMapDescriptor : 368 -> 392
~ _MakeDYMTLAccelerationStructureMotionBoundingBoxGeometryDescriptor : 176 -> 192
~ _MakeDYMTLAccelerationStructureMotionCurveGeometryDescriptor : 492 -> 508
~ _DecodeDYMTLTensorBufferAttachments : 164 -> 188
~ _MakeDYMTL4PrimitiveAccelerationStructureDescriptor : 228 -> 260
~ _MakeDYMTL4StaticLinkingDescriptor : 560 -> 576
~ _MakeDYMTLPrimitiveAccelerationStructureDescriptor : 300 -> 340
+ _DYTraceDecode_MTLDevice_newSharedEventWithOptions
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2613"
+ "Shared events created with certain options cannot be captured"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2612"
```
