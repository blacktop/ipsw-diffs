## dyld

> `/usr/lib/dyld`

```diff

-1321.0.0.0.0
-  __TEXT.__text: 0x89a90
-  __TEXT.__const: 0x22f0
-  __TEXT.__cstring: 0xfd93
-  __TEXT.__unwind_info: 0x508
+1322.3.0.0.0
+  __TEXT.__text: 0x8a368
+  __TEXT.__const: 0x2300
+  __TEXT.__cstring: 0xfe43
+  __TEXT.__unwind_info: 0x4f8
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x6f00
+  __DATA_CONST.__const: 0x6e08
   __DATA.__data: 0x2f0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0x70
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 8955619B-E236-3D86-9DB1-2E4141BF277A
-  Functions: 2873
-  Symbols:   7264
-  CStrings:  1973
+  UUID: 4E9F3B1E-8F53-3E3B-849C-950CA957C64B
+  Functions: 2881
+  Symbols:   7274
+  CStrings:  1981
 
Symbols:
+ __ZN11Diagnostics11appendErrorEPKcz.cold.1
+ __ZN11Diagnostics11appendErrorEPKcz.cold.2
+ __ZN11Diagnostics11appendErrorEPKcz.cold.3
+ __ZN11Diagnostics11appendErrorEPKcz.cold.4
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.1
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.2
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.3
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.4
+ __ZN11DiagnosticsC1EOS_
+ __ZN11DiagnosticsC1Ev
+ __ZN3lsl13MemoryManagerC2EPPKcS3_Pvb
+ __ZN3lsl9Allocator4PoolC1EPS0_PS1_NS_13MemoryManager6BufferES5_bb
+ __ZN3lsl9Allocator4PoolC2EPS0_PS1_NS_13MemoryManager6BufferES5_bb
+ __ZN3lsl9Allocator4PoolC2EPS0_PS1_NS_13MemoryManager6BufferES5_bb.cold.1
+ __ZN5dyld44APIs36_dyld_call_with_writable_tpro_memoryEPFvPvES1_
+ ___Block_byref_object_copy_.93
+ ___Block_byref_object_dispose_.94
+ ____ZN3lsl13MemoryManager26withWritableMemoryInternalIZN5dyld44APIs36_dyld_call_with_writable_tpro_memoryEPFvPvES4_E3$_0EEvT__block_invoke
+ ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke.101
+ ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke_2.102
+ ____ZN5dyld4L19getObjCPatchClassesEPKN5dyld313MachOAnalyzerERNS0_3MapIPKvbNS_11HashPointerENS_12EqualPointerEEE_block_invoke_2
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.217
+ ___block_descriptor_tmp.225
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.243
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.89
+ __simple_vsnprintf
+ __simple_vsnprintf.cold.1
+ __snprintf_out_of_space
- __ZN11DiagnosticsC1Eb
- __ZN3lsl13MemoryManagerC2EPPKcS3_Pv
- __ZN3lsl9Allocator4PoolC1EPS0_PS1_NS_13MemoryManager6BufferES5_b
- __ZN3lsl9Allocator4PoolC2EPS0_PS1_NS_13MemoryManager6BufferES5_b
- __ZN3lsl9Allocator4PoolC2EPS0_PS1_NS_13MemoryManager6BufferES5_b.cold.1
- __ZNK11Diagnostics13assertNoErrorEv.cold.1
- __ZNK11Diagnostics16errorMessageCStrEv
- __ZNK15DyldSharedCache17forEachTPRORegionEU13block_pointerFvPKvyyRbE
- __ZNK6mach_o12PlatformInfo14versionForYearEtb
- __ZNK6mach_o18PlatformInfo_macOS14versionForYearEtb
- __ZNK6mach_o18PlatformInfo_sepOS14versionForYearEtb
- __ZNK6mach_o21PlatformInfo_firmware14versionForYearEtb
- ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke.103
- ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke_2.104
- ____ZN5dyld413ProcessConfig9DyldCacheC2ERNS0_7ProcessERKNS0_8SecurityERKNS0_7LoggingERNS_15SyscallDelegateERN3lsl9AllocatorERKS0__block_invoke
- ____ZN5dyld4L19getObjCPatchClassesEPKN5dyld313MachOAnalyzerERNS0_3MapIPKvbNS_11HashPointerENS_12EqualPointerEEE_block_invoke.95
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.206
- ___block_descriptor_tmp.213
- ___block_descriptor_tmp.224
- ___block_descriptor_tmp.226
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.241
- ___block_descriptor_tmp.91
- ___copy_helper_block_8_40
- ___destroy_helper_block_8_40c17_ZTS11Diagnostics
- __simple_sresize
CStrings:
+ "(actualSize + 1) == expectedSize"
+ "1322.3"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jun 30 21:48:11 PDT 2025; root:libignition-58~7356/libignition_core/RELEASE_ARM64E"
+ "BUG IN LIBPLATFORM: Overflow in _simple_snprintf"
+ "DYLD_OVERLAY_PATH"
+ "Darwin Ignition Sequence Version 1.0.0: Mon Jun 30 21:48:11 PDT 2025; root:libignition-58~7356/libignition_core/RELEASE_ARM64E"
+ "Diagnostics.cpp"
+ "Illegal TPRO memory access"
+ "actualSize >= 0"
+ "appendError"
+ "error"
+ "expectedSize >= 0"
- "1321"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Jun 14 07:57:28 PDT 2025; root:libignition-58~5924/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sat Jun 14 07:57:28 PDT 2025; root:libignition-58~5924/libignition_core/RELEASE_ARM64E"
- "v40@?0r^v8Q16Q24^B32"

```
