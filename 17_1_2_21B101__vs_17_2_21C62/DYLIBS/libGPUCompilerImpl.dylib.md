## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.47.0.0.0
-  __TEXT.__text: 0x3d623c
-  __TEXT.__auth_stubs: 0x48c0
+32023.98.0.0.0
+  __TEXT.__text: 0x3a98dc
+  __TEXT.__auth_stubs: 0x48f0
   __TEXT.__init_offsets: 0x48
-  __TEXT.__const: 0x167680
-  __TEXT.__cstring: 0x28c4e9
-  __TEXT.__unwind_info: 0x4a7c
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x9bdb0
-  __AUTH_CONST.__const: 0x79c8
+  __TEXT.__const: 0x167174
+  __TEXT.__cstring: 0x28c906
+  __TEXT.__unwind_info: 0x5aa4
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x9bd78
+  __AUTH_CONST.__const: 0x8bc8
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__auth_got: 0x2448
+  __AUTH_CONST.__auth_got: 0x2460
   __AUTH.__const_weak: 0x858
   __AUTH.__got_weak: 0x18
   __DATA.__got_weak: 0x838
   __DATA.__data: 0x1c
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x11
-  __DATA.__common: 0x11
-  __DATA.__bss: 0x19
+  __DATA.__common: 0x22
+  __DATA.__bss: 0x6e9
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__common: 0x380
-  __DATA_DIRTY.__bss: 0x2110
+  __DATA_DIRTY.__common: 0x608
+  __DATA_DIRTY.__bss: 0x1768
   - /usr/lib/libLLVM.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libllvm-lmdb.dylib
-  Functions: 7581
-  Symbols:   2748
-  CStrings:  14695
+  Functions: 9246
+  Symbols:   2766
+  CStrings:  14757
 
Symbols:
+ __ZN10llvm_utils23decodeExternalReferenceEN4llvm9StringRefE
+ __ZN10llvm_utils23encodeExternalReferenceERKNS_17ExternalReferenceE
+ __ZN4llvm34ShouldNotRunFunctionPassesAnalysis3KeyE
+ __ZN4llvm3air14getAISignatureEPKNS_6ModuleE
+ __ZN4llvm3air15AISignatureNode7classofEPKNS_8MetadataE
+ __ZN4llvm3air15AISignatureNode7classofEPKNS_8MetadataENS_9StringRefE
+ __ZN4llvm3air16AILinkedConstant7classofEPKNS_8MetadataE
+ __ZN4llvm3air16AILinkedConstant7getImplERNS_11LLVMContextEPNS_8ConstantENS_9StringRefEjNS_8Metadata11StorageTypeEb
+ __ZN4llvm3air16dropAIRSignatureERNS_6ModuleE
+ __ZN4llvm3air17AIModuleSignature7getImplERNS_11LLVMContextENS_9StringRefENS_8Metadata11StorageTypeEb
+ __ZN4llvm3air26AILinkedConstantsSignature7getImplERNS_11LLVMContextEPNS0_15AISignatureNodeENS_8ArrayRefIPNS0_16AILinkedConstantEEENS_8Metadata11StorageTypeEb
+ __ZN4llvm3air34AIRenameQualifiedFunctionSignature7getImplERNS_11LLVMContextEPNS0_15AISignatureNodeENS_9StringRefENS_8Metadata11StorageTypeEb
+ __ZN4llvm3air9bc_common24removeAlignmentAttributeERNS_6ModuleE
+ __ZN4llvm3air9bc_common30removeAssumeWithOperandBundlesERNS_6ModuleE
+ __ZN7metalfe11GPUCompiler18specializeFunctionERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefENSA_IhEERNS1_11raw_ostreamE
+ __ZN7metalfe11GPUCompiler24specializeDynamicLibraryERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefENSA_IhEERNS1_11raw_ostreamE
+ __ZN7metalfe11GPUCompiler24specializeFunctionToFileERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefENSA_IhEERNS1_11raw_ostreamERNS1_17raw_pwrite_streamE
+ __ZN7metalfe11GPUCompiler26specializeFunctionToBufferERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefENSA_IhEERNS1_11raw_ostreamE
+ __ZN7metalfe11GPUCompiler30specializeDynamicLibraryToFileERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefENSA_IhEERNS1_11raw_ostreamERNS1_17raw_pwrite_streamE
+ __ZN7metalfe11GPUCompiler32specializeDynamicLibraryToBufferERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefENSA_IhEERNS1_11raw_ostreamE
+ __ZNK4llvm4Type18isSizedDerivedTypeEPNS_15SmallPtrSetImplIPS0_EE
+ __ZNK4llvm8Argument13getParamAlignEv
+ __ZNK4llvm8Argument29hasPassPointeeByValueCopyAttrEv
+ __ZNK4llvm9StringRef16find_last_not_ofEcm
+ __ZTVN4llvm10CallbackVHE
- __ZN7metalfe11GPUCompiler18specializeFunctionERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefERNS1_11raw_ostreamE
- __ZN7metalfe11GPUCompiler24specializeDynamicLibraryERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefERNS1_11raw_ostreamE
- __ZN7metalfe11GPUCompiler24specializeFunctionToFileERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefERNS1_11raw_ostreamERNS1_17raw_pwrite_streamE
- __ZN7metalfe11GPUCompiler26specializeFunctionToBufferERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefERNS1_11raw_ostreamE
- __ZN7metalfe11GPUCompiler30specializeDynamicLibraryToFileERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefERNS1_11raw_ostreamERNS1_17raw_pwrite_streamE
- __ZN7metalfe11GPUCompiler32specializeDynamicLibraryToBufferERN4llvm11LLVMContextENSt3__110unique_ptrINS1_6ModuleENS4_14default_deleteIS6_EEEENS1_8ArrayRefINS1_3air4BindEEENS1_9StringRefERNS1_11raw_ostreamE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
CStrings:
+ "', "
+ "(root)"
+ ".aira"
+ ".aird"
+ ".airf"
+ ".airo"
+ ".airp"
+ ".btnf"
+ ".dylib"
+ ".mtlp"
+ ".rtlib"
+ "32023.98"
+ "AILinkedConstant"
+ "AILinkedConstantsSignature"
+ "AIModuleSignature"
+ "AIRenameQualifiedFunctionSignature"
+ "AISignatureNode"
+ "APPLE_1_"
+ "MH_CORE"
+ "MH_DSYM"
+ "MH_DYLIB"
+ "MacOS"
+ "StringRef llvm::getTypeName() [DesiredTypeName = llvm::InvalidateAnalysisPass<llvm::ShouldNotRunFunctionPassesAnalysis>]"
+ "StringRef llvm::getTypeName() [DesiredTypeName = llvm::ShouldNotRunFunctionPassesAnalysis]"
+ "T"
+ "TvOS"
+ "WatchOS"
+ "XrOS"
+ "_ios"
+ "_iosmac"
+ "_iossim"
+ "_osx"
+ "_read"
+ "_sample"
+ "_tvos"
+ "_tvossim"
+ "_watchos"
+ "_write"
+ "_xros"
+ "_xrossim"
+ "air-lld"
+ "air-nt"
+ "air-pack"
+ "air.linked_constants_signature"
+ "air.module_signature"
+ "air.rename_qualified_function_signature"
+ "air.signature"
+ "airr"
+ "cpp_type"
+ "depth2d"
+ "g11g_a0"
+ "g11m_a0"
+ "g11p_a0"
+ "g12p_a0"
+ "g15g_a0"
+ "g15g_b0"
+ "g15s_a0"
+ "g15s_b0"
+ "hash"
+ "iOS"
+ "key"
+ "ld"
+ "llong"
+ "long"
+ "mesh<"
+ "metal"
+ "or '"
+ "private"
+ "swift"
+ "ullong"
- "32023.47"
- "?#"
- "MTLComputePipelineDescriptor"
- "MTLFeatureSet"
- "MTLFunction"
- "MTLLibrary"
- "MTLRenderPipelineDescriptor"
- "specialized"

```
