## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 2027.0.37.0.0
-  __TEXT.__text: 0x297cbc
+  __TEXT.__text: 0x297fc0
   __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_stubs: 0x18520
+  __TEXT.__objc_stubs: 0x18640
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x135a4
-  __TEXT.__const: 0xa080
-  __TEXT.__cstring: 0x3085f
+  __TEXT.__objc_methlist: 0x13634
+  __TEXT.__const: 0xa090
+  __TEXT.__cstring: 0x308b8
   __TEXT.__oslogstring: 0x2418
   __TEXT.__gcc_except_tab: 0x1634
-  __TEXT.__objc_methname: 0x1b95c
+  __TEXT.__objc_methname: 0x1baf0
   __TEXT.__objc_classname: 0x15da
   __TEXT.__objc_methtype: 0xafc9
   __TEXT.__ustring: 0x20a

   __DATA_CONST.__got: 0x868
   __DATA_CONST.__auth_ptr: 0x48
   __AUTH_CONST.__interpose: 0x50
-  __DATA.__objc_const: 0x1b4b0
-  __DATA.__objc_selrefs: 0x7058
+  __DATA.__objc_const: 0x1b5f8
+  __DATA.__objc_selrefs: 0x70d0
   __DATA.__objc_ivar: 0xba4
   __DATA.__objc_data: 0x2170
   __DATA.__data: 0x3530

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9836
-  Symbols:   16268
-  CStrings:  9429
+  Functions: 9839
+  Symbols:   16280
+  CStrings:  9444
 
Symbols:
+ -[CaptureMTLComputePipelineState forwardProgressUsage]
+ -[CaptureMTLComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:]
+ -[CaptureMTLTexture minLOD]
+ GCC_except_table3064
+ GCC_except_table3072
+ GCC_except_table3208
+ GCC_except_table3359
+ GCC_except_table3366
+ GCC_except_table3375
+ GCC_except_table3475
+ GCC_except_table3603
+ GCC_except_table4229
+ GCC_except_table4407
+ GCC_except_table4419
+ GCC_except_table4420
+ GCC_except_table4595
+ GCC_except_table4596
+ GCC_except_table4867
+ _objc_msgSend$contentionRelief
+ _objc_msgSend$forwardProgressUsage
+ _objc_msgSend$minLOD
+ _objc_msgSend$optimizeForPersistentKernel
+ _objc_msgSend$recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:
+ _objc_msgSend$setContentionRelief:
+ _objc_msgSend$setForwardProgressUsage:
+ _objc_msgSend$setMinLOD:
+ _objc_msgSend$setOptimizeForPersistentKernel:
- GCC_except_table3062
- GCC_except_table3070
- GCC_except_table3206
- GCC_except_table3357
- GCC_except_table3364
- GCC_except_table3373
- GCC_except_table3473
- GCC_except_table3601
- GCC_except_table4227
- GCC_except_table4402
- GCC_except_table4403
- GCC_except_table4415
- GCC_except_table4589
- GCC_except_table4590
- GCC_except_table4865
Functions:
~ _TranslateGTMTLStructType : 720 -> 732
~ _TranslateGTMTLPipelineLibraryInfo : 1256 -> 1260
~ _GTTraceStoreDebugDescription : 4804 -> 4800
~ -[SparseTexturePageTable fillArrayWithCopyOps:fromPageTable:apiOpCount:gpuOps:] : 2128 -> 2140
~ _SaveMTLTextureInfo : 188 -> 192
~ _SaveMTLTextureMipmapInfo : 208 -> 220
~ _TextureAccess : 228 -> 240
+ -[CaptureMTLComputePipelineState reflection]
+ -[CaptureMTLComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:]
~ -[GTMTLCaptureSparsePageTables dumpBufferMappingsWithCallback:buffer:] : 648 -> 652
+ -[CaptureMTLTexture responsibleProcess]
~ _GTBitSet_popcount : 128 -> 120
~ _apr_table_get : 248 -> 252
~ _apr_table_merge : 368 -> 372
~ _apr_table_mergen : 336 -> 340
~ _TranslateGTMTLComputePipelineDescriptorAuto : 1072 -> 1168
~ _MakeMTLComputePipelineDescriptorWithoutResourceIndex : 944 -> 1048
~ _TranslateGTMTLTileRenderPipelineDescriptor : 828 -> 908
~ _MakeMTLTileRenderPipelineDescriptor : 708 -> 760
~ _TranslateNestedGTMTL4ComputePipelineDescriptor : 272 -> 376
~ _MakeMTL4ComputePipelineDescriptor : 280 -> 384
~ _TranslateGTMTLTextureViewDescriptorDirectly : 124 -> 144
~ _MakeMTLTextureViewDescriptor : 132 -> 164
~ _GTSMMTLIntersectionFunctionTableStateful_processTraceFuncWithMap : 1332 -> 1336
~ _GTSMMTLIntersectionFunctionTableStateful_processTraceFuncWithPool : 1332 -> 1336
~ _WriteGTMTLIntersectionFunctionTable : 1328 -> 1336
~ _UpdateAccess : 152 -> 156
~ _DecodeDYMTLRenderPipelineReflection : 2780 -> 2776
~ _DecodeDYMTLStructType : 1400 -> 1444
~ _DecodeDYMTLTextureMipmapInfo : 184 -> 188
~ _GTCaptureArchive_open : 1360 -> 1344
CStrings:
+ "contentionRelief"
+ "forwardProgressUsage"
+ "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
+ "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
+ "minLOD"
+ "optimizeForPersistentKernel"
+ "recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:"
+ "setContentionRelief:"
+ "setForwardProgressUsage:"
+ "setMinLOD:"
+ "setOptimizeForPersistentKernel:"
+ "supportsAtomicWaitNotify"
+ "supportsMXUNarrowTileSizes"
+ "supportsPackUnpackSmallInteger"
+ "supportsRGBTextureBuffers"
+ "supportsSIMDGroupParallelForwardProgress"
+ "supportsTextureViewMinLOD"
- "0xffffc0e9"
- "0xffffc0ea"
```
