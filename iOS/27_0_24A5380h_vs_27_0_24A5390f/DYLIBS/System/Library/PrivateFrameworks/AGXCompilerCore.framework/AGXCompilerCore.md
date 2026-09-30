## AGXCompilerCore

> `/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__AUTH.__thread_vars`

```diff

-360.31.1.0.0
-  __TEXT.__text: 0x268ae8
-  __TEXT.__const: 0x3a408
-  __TEXT.__cstring: 0x1c4c2
+360.32.0.0.0
+  __TEXT.__text: 0x268f04
+  __TEXT.__const: 0x3a418
+  __TEXT.__cstring: 0x1c6e2
   __TEXT.__oslogstring: 0x5fc
-  __TEXT.__unwind_info: 0x4758
+  __TEXT.__unwind_info: 0x47a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x7b98
+  __DATA_CONST.__const: 0x7bb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x77988
+  __AUTH_CONST.__const: 0x78040
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__weak_auth_got: 0xe8
-  __AUTH_CONST.__auth_got: 0x13a0
+  __AUTH_CONST.__auth_got: 0x13d0
   __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30
   __DATA.__data: 0x80
-  __DATA.__bss: 0x4540
+  __DATA.__bss: 0x5098
   __DATA_DIRTY.__bss: 0xc00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8169
-  Symbols:   11061
-  CStrings:  4668
+  Functions: 8182
+  Symbols:   11081
+  CStrings:  4686
 
Symbols:
+ __ZGVZN28AGCPerThreadPerTargetContext13createLLVMCtxERK19AGCLLVMTargetConfigRK19AGCCompilerFeaturesE21agx_extra_llvm_attrib
+ __ZL11loadRuntimeRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPKcPN4llvm6ModuleE
+ __ZN10AGCLLVMCtxC1ERK19AGCLLVMTargetConfigN4llvm3AGX11AGXCompilerERK19AGCCompilerFeatures3ApiRKNSt3__112basic_stringIcNSA_11char_traitsIcEENSA_9allocatorIcEEEESI_
+ __ZN19AGCLLVMTargetConfigD2Ev
+ __ZN23AGCLLVMG14TargetLowererC2ERN4llvm11LLVMContextERK19AGCLLVMTargetConfig
+ __ZN23AGCLLVMG14XTargetConfigC2E13AGCTargetArch
+ __ZN28AGCPerThreadPerTargetContext13getAGCLLVMCtxERK19AGCLLVMTargetConfigRK19AGCCompilerFeatures
+ __ZN4llvm11StringErrorC1ERKNS_5TwineENSt3__110error_codeE
+ __ZN4llvm11raw_ostreamlsERKNS_18format_object_baseE
+ __ZN4llvm18format_object_base4homeEv
+ __ZN4llvm22inconvertibleErrorCodeEv
+ __ZN4llvm3sys4path6appendERNS_15SmallVectorImplIcEERKNS_5TwineES7_S7_S7_
+ __ZNK19AGCLLVMTargetConfig13getGpeRuntimeEv
+ __ZNK19AGCLLVMTargetConfig13getVftRuntimeEv
+ __ZNK19AGCLLVMTargetConfig16getTensorRuntimeEv
+ __ZNK19AGCLLVMTargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK19AGCLLVMTargetConfig19getTexAtomicRuntimeEv
+ __ZNK19AGCLLVMTargetConfig20getRaytracingRuntimeEv
+ __ZNK19AGCLLVMTargetConfig21getDefaultMathRuntimeEv
+ __ZNK19AGCLLVMTargetConfig21getPreciseMathRuntimeEv
+ __ZNK19AGCLLVMTargetConfig24getDoraRaytracingRuntimeEv
+ __ZNK19AGCLLVMTargetConfig25getDisableFP64MathRuntimeEv
+ __ZNK19AGCLLVMTargetConfig26getMeshTessellationRuntimeEv
+ __ZNK19AGCLLVMTargetConfig30getDisableSubnormalMathRuntimeEv
+ __ZNK21AGCLLVMDynamicLibrary19isYieldAPISupportedEv
+ __ZNK22AGCLLVMG13TargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK22AGCLLVMG14TargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK23AGCLLVMG14XTargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK25AGCLLVMG15GA0TargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK25AGCLLVMG15GB0TargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK25AGCLLVMG15GC0TargetConfig17getMetalEiRuntimeENSt3__18optionalI11AGCTargetOSEE
+ __ZNK4llvm11Instruction16mayWriteToMemoryEv
+ __ZNK4llvm11Instruction17mayReadFromMemoryEv
+ __ZNK4llvm13format_objectIJPKcS2_EE7snprintEPcj
+ __ZNK4llvm4Loop15isLoopInvariantEPKNS_5ValueE
+ __ZNSt3__110unique_ptrI10AGCLLVMCtxNS_14default_deleteIS1_EEED1B9fqn220106Ev
+ __ZTVN4llvm13format_objectIJPKcS2_EEE
+ __ZTv0_n104_N25AGCLLVMUserDynamicLibrary22finalizeDriverBindingsEPN4llvm8FunctionE
+ __ZTv0_n128_N25AGCLLVMUserDynamicLibrary14constructReplyEv
+ __ZTv0_n136_NK25AGCLLVMUserDynamicLibrary18disableGin1122SWWAEv
+ __ZTv0_n168_NK21AGCLLVMDynamicLibrary19isYieldAPISupportedEv
+ __ZZN10AGCLLVMCtx16loadMetalRuntimeEP13AGCLLVMObjectPN4llvm6ModuleENS_14RuntimeLibraryENSt3__18optionalINS2_6TripleEEEENK3$_0clENS2_8ExpectedIS4_EE
+ __ZZN16InsertYieldsPass3runERN4llvm8FunctionERNS0_15AnalysisManagerIS1_JEEEENK3$_2clEPNS0_11InstructionEPNS0_4LoopE
+ __ZZN28AGCPerThreadPerTargetContext13createLLVMCtxERK19AGCLLVMTargetConfigRK19AGCCompilerFeaturesE21agx_extra_llvm_attrib
- __Z28AGCLLVMCreateG14TargetConfig13AGCTargetArch
- __ZGVZN28AGCPerThreadPerTargetContext13createLLVMCtxE13AGCTargetArchE21agx_extra_llvm_attrib
- __ZL11loadRuntimePKcPN4llvm6ModuleE
- __ZN10AGCLLVMCtxC1ERK19AGCLLVMTargetConfigN4llvm3AGX11AGXCompilerEb3ApiRKNSt3__112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEESF_
- __ZN26AGCLLVMG15PB0TargetLowerer15maxImageDimLog2Ev
- __ZN26AGCLLVMG15PB0TargetLowerer16getF16FormatInfoEtPN4llvm4TypeEbbb
- __ZN26AGCLLVMG15PB0TargetLowerer25buildImageMipCountExtractEN14AGCLLVMBuilder11InsertPointEPN4llvm5ValueES4_
- __ZN26AGCLLVMG15PB0TargetLowerer26buildImageBaseLevelExtractEN14AGCLLVMBuilder11InsertPointEPN4llvm5ValueES4_
- __ZN26AGCLLVMG15PB0TargetLowerer27buildImageDimensionsExtractEN14AGCLLVMBuilder11InsertPointEPN4llvm5ValueES4_
- __ZN26AGCLLVMG15PB0TargetLowerer27buildImagePackFormatExtractEN14AGCLLVMBuilder11InsertPointEPN4llvm5ValueES4_
- __ZN26AGCLLVMG15PB0TargetLowerer28buildImageSampleCountExtractEN14AGCLLVMBuilder11InsertPointEPN4llvm5ValueES4_
- __ZNK26AGCLLVMG15PB0TargetLowerer16createGPUVAMasksEPKN16AGCCodeGenerator12CompileReplyEb
- __ZNK26AGCLLVMG15PB0TargetLowerer19supportsMeshShadingEv
- __ZNK26AGCLLVMG15PB0TargetLowerer19supportsPrimitiveIDEv
- __ZNK26AGCLLVMG15PB0TargetLowerer21needsShaderDepthClampEv
- __ZNK26AGCLLVMG15PB0TargetLowerer25supportsBarycentricCoordsEv
- __ZNK26AGCLLVMG15PB0TargetLowerer34getPBEStateWordDimFromEmitStateDimEN13_AGCEmitState9DimensionE
- __ZNSt3__110unique_ptrI10AGCLLVMCtxNS_14default_deleteIS1_EEE5resetB9fqn220106EPS1_
- __ZNSt3__110unique_ptrI25AGCCompilationResultCacheNS_14default_deleteIS1_EEE5resetB9fqn220106EPS1_
- __ZTv0_n120_N25AGCLLVMUserDynamicLibrary14constructReplyEv
- __ZTv0_n128_NK25AGCLLVMUserDynamicLibrary18disableGin1122SWWAEv
- __ZTv0_n96_N25AGCLLVMUserDynamicLibrary22finalizeDriverBindingsEPN4llvm8FunctionE
- __ZZN28AGCPerThreadPerTargetContext13createLLVMCtxE13AGCTargetArchE21agx_extra_llvm_attrib
- _os_parse_boot_arg_int
CStrings:
+ "-f32denorm"
+ "ei_rt_g13.metallib"
+ "ei_rt_g13x.metallib"
+ "ei_rt_g14.metallib"
+ "ei_rt_g14d.metallib"
+ "ei_rt_g14sc.metallib"
+ "ei_rt_g15g_a0.metallib"
+ "ei_rt_g15g_b0.metallib"
+ "ei_rt_g15g_c0.metallib"
+ "ei_rt_g16p_a0.metallib"
+ "ei_rt_g16p_b0.metallib"
+ "ei_rt_hal200.metallib"
+ "ei_rt_hal300.metallib"
+ "failed to load runtime file %s in search directory %s"
+ "gpe_rt.metallib"
+ "ms_tessellation.metallib"
+ "raytracing_runtime_dora_ria2.metallib"
+ "raytracing_runtime_dora_ria3.metallib"
+ "raytracing_runtime_emulation.metallib"
+ "raytracing_runtime_ria1.metallib"
+ "raytracing_runtime_ria2.metallib"
+ "raytracing_runtime_ria3.metallib"
+ "runtime.gen10.metallib"
+ "runtime.gen12.metallib"
+ "runtime.gen15.metallib"
+ "tensor.metallib"
+ "tex_atomic_emu_g13.metallib"
+ "tex_atomic_emu_g14.metallib"
+ "tex_atomic_emu_g15.metallib"
+ "tex_atomic_emu_g16.metallib"
+ "tex_atomic_emu_g17.metallib"
+ "vft_rt_gen1.metallib"
+ "vft_rt_gen1_agx3.metallib"
- "-gin-1087"
- ".metallib"
- "/gpe_rt.metallib"
- "/metal_rt.metallib"
- "/metal_rt_precise.metallib"
- "/ms_tessellation.metallib"
- "/raytracing_rt"
- "/tensor.metallib"
- "/tex_atomic_emu.metallib"
- "/vft_rt.metallib"
- "_dora"
- "agx-disable-gin1087-swwa"
- "ei_rt.metallib"
- "unable to load helper runtime files"
- "unable to load math metal runtime files"
```
