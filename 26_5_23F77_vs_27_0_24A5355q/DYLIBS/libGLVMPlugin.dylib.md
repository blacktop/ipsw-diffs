## libGLVMPlugin.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib`

```diff

-23.1.1.0.0
-  __TEXT.__text: 0x468f0
-  __TEXT.__auth_stubs: 0xb20
+24.0.1.0.0
+  __TEXT.__text: 0x4702c
   __TEXT.__cstring: 0x33a5
   __TEXT.__const: 0x930
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x610
-  __DATA_CONST.__got: 0x18
+  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1248
-  __AUTH_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x150
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH.__data: 0xe00
   __DATA.__data: 0xcc
   __DATA.__bss: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /usr/lib/libLLVM.dylib
+  - /System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5092AA70-5265-3E39-99A5-FF33B9129E06
-  Functions: 630
-  Symbols:   1435
+  UUID: C1810F85-F658-3032-87AB-E2F478A76025
+  Functions: 631
+  Symbols:   1437
   CStrings:  857
 
Symbols:
+ __ZNSt3__110unique_ptrIN4llvm6ModuleENS_14default_deleteIS2_EEED1B9fqn220100Ev
+ __ZNSt3__119__allocate_at_leastB9fqn220100INS_9allocatorIPN4llvm6MDNodeEEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__16vectorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS0_IS7_NS_9allocatorIS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEENS8_ISG_EEE16__destroy_vectorclB9fqn220100Ev
+ __ZNSt3__16vectorIPN4llvm6MDNodeENS_9allocatorIS3_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIPN4llvm6MDNodeENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__19allocatorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS_6vectorIS7_NS0_IS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEEE7destroyB9fqn220100EPSG_
+ __ZSt28__throw_bad_array_new_lengthB9fqn220100v
- __ZNSt3__110unique_ptrIN4llvm6ModuleENS_14default_deleteIS2_EEED1B9nqn210106Ev
- __ZNSt3__119__allocate_at_leastB9nqn210106INS_9allocatorIPN4llvm6MDNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__16vectorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS0_IS7_NS_9allocatorIS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEENS8_ISG_EEE16__destroy_vectorclB9nqn210106Ev
- __ZNSt3__16vectorIPN4llvm6MDNodeENS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__19allocatorINS_4pairIPN4llvm6MDNodeENS2_9SetVectorIPNS2_8MetadataENS_6vectorIS7_NS0_IS7_EEEENS2_8DenseSetIS7_NS2_12DenseMapInfoIS7_vEEEEEEEEE7destroyB9nqn210106EPSG_
- __ZSt28__throw_bad_array_new_lengthB9nqn210106v
Functions:
~ _PPParserMacroCreateFromMacro : 220 -> 224
~ _PPParserMacroFree : 124 -> 128
~ _PPParserPreprocessString : 2552 -> 2620
~ _PPParserLabelsFree : 92 -> 96
~ _llvmir_PPStreamAddAttribBinding : 148 -> 152
~ _llvmir_PPStreamAddOutputBinding : 124 -> 128
~ _llvmir_PPStreamAddConstant : 128 -> 124
~ _PPParserGetPart : 440 -> 444
~ _PPParserParseParamBinding : 6584 -> 6708
~ _PPParserParse : 3164 -> 3168
~ _glpARBProgram_AttribToFunction : 328 -> 332
~ _glpARBProgram_GenerateMetadata : 336 -> 340
~ _GLDAttribBindingsAddAttribBinding : 132 -> 128
~ _PPParserOutputBindingsAddOutputBinding : 116 -> 112
~ _PPParserLabelsAddLabel : 140 -> 136
~ _glpFragProgram_GenerateMetadata : 1892 -> 1900
~ _glpVertProgram_GenerateMetadata : 1888 -> 1900
~ __glpPointerHashRealPut : 132 -> 108
~ _glpABIGetTypeAlign : 32 -> 36
~ _glpABIGetMinimumStructAlignment : 24 -> 28
~ _glpABIGetMinimumBufferBytesForType : 80 -> 84
~ _glpLLVMBuildSubroutinesTypeClasses : 1132 -> 1136
~ _glpLLVMCleanUpASTObjects : 420 -> 424
~ _glpLLVMCGFindSamplersAndBuffers : 1164 -> 1168
~ _glpLLVMCreateAttributeDescription : 696 -> 700
~ _glpLLVMVertexMetaData : 276 -> 284
~ _glpLLVMFragmentMetaData : 676 -> 684
~ _glpLLVMCGPPStreamOpNode : 10288 -> 10316
~ _glpLLVMCGCommaExpr : 408 -> 412
~ _glpLLVMCGFunctionPrototype : 10140 -> 10228
~ _glpLLVMCGFunctionDefinition : 2460 -> 2468
~ _glpLLVMCGInterfaceBlock : 96 -> 100
~ _glpLLVMCGBlock : 924 -> 920
~ _glpLLVMWriteOutput : 696 -> 724
~ _glpLLVMPrimitiveConstant : 584 -> 588
~ _glpLLVMCreateConstantVectors : 468 -> 472
~ _glpLLVMCGSamplerNode : 1304 -> 1320
~ _glpBuildConstantIntVector : 300 -> 304
~ _glpLLVMBuildLength : 760 -> 768
~ _glpLLVMBuildCross : 456 -> 484
~ _glpBuildTextureOperation : 5376 -> 5404
~ _glpBuildTextureSizeOperation : 1224 -> 1232
~ _glpBuildGetLODOperation : 580 -> 596
~ _glpCGSwizzle : 1384 -> 1396
~ _glpProcessComponentWiseVectorAssignment : 2076 -> 2112
~ _glpTypeToLLVMTypeWithUnderlying : 720 -> 724
~ _glpLLVMBuildFunctionType : 1612 -> 1624
~ _glpLLVMVertexGeometryMetadata : 1380 -> 1420
~ _glpLLVMSharedRawCall : 548 -> 556
~ _glpLLVMCGWriteVertexOutput : 460 -> 464
~ _glpMangleTypeName : 796 -> 800
~ _glpLLVMCreateBuilderInContext : 108 -> 112
~ _glpLLVMConstInt : 492 -> 532
~ _glpLLVMConstUint64 : 120 -> 124
~ _glpLLVMStructTypeInContext : 612 -> 644
~ _glpLLVMBuildInsertValue : 544 -> 576
~ _glpLLVMBuildExtractValue : 528 -> 560
~ _glpLLVMSetCurrentLineStub : 444 -> 476
~ _glpGenerateLLVMIRModule : 692 -> 696
~ _glpDeserializeLLVMType : 408 -> 444
~ _glpDeserializeuint32 : 404 -> 436
~ _glpDeserializeArraySize : 404 -> 436
~ _glpDeserializeLLVMValue : 408 -> 444
~ _glpDeserializeLLVMBlock : 408 -> 444
~ _glpLinkedProgramGetSubroutineUniformLocationCount : 136 -> 140
~ _deserialize_double : 60 -> 64
~ _glpTypeGetSamplerCount : 240 -> 244
~ _glpStructTypeGetSizesAndAlignments : 424 -> 432
~ __ZN19GLPDebugInfoContext14createFunctionEPKcPN4llvm8FunctionE : 416 -> 320
~ _glpLLVMGetDebugLocation : 92 -> 104
+ __ZNSt3__16vectorIPN4llvm6MDNodeENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
~ _gleLLVMBeginMain : 912 -> 916
~ _gleLLVMFinishMain : 720 -> 728
~ _gleLLVMCreateVaryingsMetaData : 600 -> 604
~ _gleLLVMAddTexture : 340 -> 344
~ _gleLLVMCreateConstantVec4 : 188 -> 196
~ _gleLLVMClampColor : 404 -> 408
~ _gleStateProgram_BuildOperation : 700 -> 708
~ _gleLLVMAddOperation : 11620 -> 11664
~ _readTempValue : 196 -> 204
~ _gleStateProgram_BuildTextureOperation : 2452 -> 2464
~ _TestCC_XYZW : 288 -> 292
~ _gleLLVMApplyDestMaskAndCC : 1288 -> 1308
~ _readAddressValue : 196 -> 204
~ _gleLLVMVectorExtend : 480 -> 484
~ _glpVertexStateToLLVMIR : 1684 -> 1688
~ _gleVStateProgram_Core : 15416 -> 15584
~ _gleVStateProgram_GenerateMetadata : 2000 -> 2008
~ _gleVStateProgram_LightingStage : 37976 -> 38392
~ _gleFragmentStateToModule : 1904 -> 1920
~ _glpFragmentStateToLLVMIR : 1352 -> 1356
~ _gleFStateProgram_Core : 12456 -> 12460
~ _gleFStateProgram_GenerateMetadata : 1804 -> 1812
~ __glpSetCrashLogMessage.cold.1 : 128 -> 84

```
