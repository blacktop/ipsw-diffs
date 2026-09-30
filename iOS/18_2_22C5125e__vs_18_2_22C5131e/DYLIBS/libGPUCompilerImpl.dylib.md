## libGPUCompilerImpl.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib`

```diff

-32023.406.0.0.0
-  __TEXT.__text: 0x435208
+32023.408.0.0.0
+  __TEXT.__text: 0x4376e4
   __TEXT.__auth_stubs: 0x4d40
   __TEXT.__init_offsets: 0x48
-  __TEXT.__const: 0x1b0610
-  __TEXT.__cstring: 0x32449d
+  __TEXT.__const: 0x1b0480
+  __TEXT.__cstring: 0x324315
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x4da0
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0xb2aa8
+  __TEXT.__unwind_info: 0x4e00
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xb2a68
   __AUTH_CONST.__auth_got: 0x26a0
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x8c68
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x11
   __DATA.__data: 0x24
-  __DATA.__bss: 0x5a9
+  __DATA.__bss: 0x59
   __DATA.__common: 0x11
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x1b10
+  __DATA_DIRTY.__bss: 0x2080
   __DATA_DIRTY.__common: 0x380
   - /usr/lib/libLLVM.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libllvm-lmdb.dylib
-  Functions: 8003
-  Symbols:   3075
-  CStrings:  17576
+  Functions: 8012
+  Symbols:   3076
+  CStrings:  17568
 
Symbols:
+ __ZN10llvm_utils22PackedMachObjectWriter8ZeroHashE
+ __ZN4llvm3air12MachOBuilder16buildModuleTableERKNS_11SmallVectorIN10llvm_utils22PackedMachObjectWriter8MetalLibELj4EEE
+ __ZN4llvm5airnt10Translator13emitHashTableEPN10llvm_utils16PackedMCStreamerEPNS0_16TranslatorPluginERKNSt3__13mapINS_9StringRefENS7_10shared_ptrINS_3air12NativeScriptEEENS7_4lessIS9_EENS7_9allocatorINS7_4pairIKS9_SD_EEEEEERKNS8_IS9_NS_8ArrayRefIhEESF_NSG_INSH_ISI_SP_EEEEEESU_
+ __ZNK4llvm5airnt12OpaquePlugin19getFunctionHashImplENS_8ArrayRefIPKNS_6ModuleEEE
+ __ZNK4llvm5airnt12OpaquePlugin26getBuiltinFunctionHashImplEv
- __ZN4llvm3air12MachOBuilder16buildModuleTableERKNSt3__16vectorIN10llvm_utils22PackedMachObjectWriter8MetalLibENS2_9allocatorIS6_EEEE
- __ZN4llvm5airnt10Translator13emitHashTableEPN10llvm_utils16PackedMCStreamerEPNS0_16TranslatorPluginERKNSt3__13mapINS_9StringRefENS7_10shared_ptrINS_3air12NativeScriptEEENS7_4lessIS9_EENS7_9allocatorINS7_4pairIKS9_SD_EEEEEERKNS8_IS9_NS_8ArrayRefIhEESF_NSG_INSH_ISI_SP_EEEEEERKNS8_IS9_NS7_5arrayIhLm32EEESF_NSG_INSH_ISI_SW_EEEEEE
- __ZNK4llvm5airnt12OpaquePlugin15getFunctionHashENS_8ArrayRefIPKNS_6ModuleEEE
- __ZNK4llvm5airnt12OpaquePlugin22getBuiltinFunctionHashEv
CStrings:
+ "32023.408"
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
