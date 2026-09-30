## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.406.0.0.0
-  __TEXT.__text: 0x435598
-  __TEXT.__auth_stubs: 0x4d30
+32023.619.0.0.0
+  __TEXT.__text: 0x40a700
+  __TEXT.__auth_stubs: 0x4d40
   __TEXT.__init_offsets: 0x48
-  __TEXT.__const: 0x1b0610
-  __TEXT.__cstring: 0x324468
+  __TEXT.__const: 0x1b4db0
+  __TEXT.__cstring: 0x32436c
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x4da0
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0xb2aa8
-  __AUTH_CONST.__auth_got: 0x2698
+  __TEXT.__unwind_info: 0x48d0
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xb2a68
+  __AUTH_CONST.__auth_got: 0x26a0
   __AUTH_CONST.__const: 0x8c68
   __AUTH.__thread_vars: 0x30
-  __AUTH.__thread_bss: 0x11
+  __AUTH.__thread_bss: 0x18
   __DATA.__data: 0x68
-  __DATA.__bss: 0x1cb8
+  __DATA.__bss: 0x1cd8
   __DATA.__common: 0x80
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x410

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6E12A315-FAF3-3634-B393-86B0122FB613
-  Functions: 8002
-  Symbols:   3074
-  CStrings:  17575
+  UUID: F417FA01-D1BE-3C97-800F-20BC60C34032
+  Functions: 7559
+  Symbols:   3076
+  CStrings:  17569
 
Symbols:
+ __ZN10llvm_utils22PackedMachObjectWriter8ZeroHashE
+ __ZN4llvm3air12MachOBuilder16buildModuleTableERKNS_11SmallVectorIN10llvm_utils22PackedMachObjectWriter8MetalLibELj4EEE
+ __ZN4llvm5airnt10Translator13emitHashTableEPN10llvm_utils16PackedMCStreamerEPNS0_16TranslatorPluginERKNSt3__13mapINS_9StringRefENS7_10shared_ptrINS_3air12NativeScriptEEENS7_4lessIS9_EENS7_9allocatorINS7_4pairIKS9_SD_EEEEEERKNS8_IS9_NS_8ArrayRefIhEESF_NSG_INSH_ISI_SP_EEEEEESU_
+ __ZNK4llvm5airnt12OpaquePlugin19getFunctionHashImplENS_8ArrayRefIPKNS_6ModuleEEE
+ __ZNK4llvm5airnt12OpaquePlugin26getBuiltinFunctionHashImplEv
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
- __ZN4llvm3air12MachOBuilder16buildModuleTableERKNSt3__16vectorIN10llvm_utils22PackedMachObjectWriter8MetalLibENS2_9allocatorIS6_EEEE
- __ZN4llvm5airnt10Translator13emitHashTableEPN10llvm_utils16PackedMCStreamerEPNS0_16TranslatorPluginERKNSt3__13mapINS_9StringRefENS7_10shared_ptrINS_3air12NativeScriptEEENS7_4lessIS9_EENS7_9allocatorINS7_4pairIKS9_SD_EEEEEERKNS8_IS9_NS_8ArrayRefIhEESF_NSG_INSH_ISI_SP_EEEEEERKNS8_IS9_NS7_5arrayIhLm32EEESF_NSG_INSH_ISI_SW_EEEEEE
- __ZNK4llvm5airnt12OpaquePlugin15getFunctionHashENS_8ArrayRefIPKNS_6ModuleEEE
- __ZNK4llvm5airnt12OpaquePlugin22getBuiltinFunctionHashEv
CStrings:
+ "32023.619"
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "g15d_a0"
- "32023.406"
- "air.simdgroup_matrix_8x8_load.device_coherent"
- "air.simdgroup_matrix_8x8_load.system_coherent"
- "air.simdgroup_matrix_8x8_load_bf16.device_coherent"
- "air.simdgroup_matrix_8x8_load_bf16.system_coherent"
- "air.simdgroup_matrix_8x8_store.device_coherent"
- "air.simdgroup_matrix_8x8_store.system_coherent"
- "air.simdgroup_matrix_8x8_store_bf16.device_coherent"
- "air.simdgroup_matrix_8x8_store_bf16.system_coherent"

```
