## dyld

> `/usr/lib/dyld`

```diff

 1323.3.0.0.0
-  __TEXT.__text: 0x8a6a8
+  __TEXT.__text: 0x8af68
   __TEXT.__const: 0x2300
-  __TEXT.__cstring: 0xfe5f
+  __TEXT.__cstring: 0xfe73
   __TEXT.__unwind_info: 0x4f8
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x6e20
+  __DATA_CONST.__const: 0x6e40
   __DATA.__data: 0x2f0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__all_image_info: 0x170
   __DATA_DIRTY.__bss: 0x1bb8
   __DATA_DIRTY.__common: 0x1120
-  __TPRO_CONST.__data: 0x70
+  __TPRO_CONST.__data: 0x71
   __TPRO_CONST.__allocator: 0x20000
-  UUID: DAE7163E-38FD-3195-8642-F958AE7766EC
-  Functions: 2882
-  Symbols:   7276
-  CStrings:  1983
+  UUID: 211A824B-618C-3DAF-A790-499FCAC0D702
+  Functions: 2887
+  Symbols:   7290
+  CStrings:  1984
 
Symbols:
+ __ZN3lsl9Allocator4PoolC1EPS0_PS1_yb.cold.2
+ __ZNK3lsl9Allocator18AllocationMetadata12firstAddressEv
+ __ZNK3lsl9Allocator18AllocationMetadata12firstAddressEv.cold.1
+ __ZZN5dyld45startEPNS_10KernelArgsEPvS2_ENK3$_1clEv
+ ___Block_byref_object_copy_.11
+ ___Block_byref_object_copy_.34
+ ___Block_byref_object_dispose_.12
+ ___Block_byref_object_dispose_.35
+ ____ZN3lsl13MemoryManager26withWritableMemoryInternalIZN5dyld45startEPNS2_10KernelArgsEPvS5_E3$_1EEvT__block_invoke
+ ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke.102
+ ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke_2.103
+ ___block_descriptor_tmp.14
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.28
+ ___block_descriptor_tmp.29
+ __gUseInstrumentedStringRoutines
+ __platform_strcmp$VARIANT$MTE
+ __platform_strcmp_noMTE
- __ZZN5dyld45startEPNS_10KernelArgsEPvS2_ENK3$_0clEv
- ___Block_byref_object_copy_.10
- ___Block_byref_object_copy_.32
- ___Block_byref_object_dispose_.11
- ___Block_byref_object_dispose_.33
- ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke.101
- ____ZN5dyld413ProcessConfig13PathOverrides21processVersionedPathsERKNS0_7ProcessERNS_15SyscallDelegateERKNS0_9DyldCacheEN6mach_o8PlatformERKNSA_19GradedArchitecturesERN3lsl9AllocatorE_block_invoke_2.102
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.26
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Aug 26 20:17:33 PDT 2025; root:libignition-58~15009/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Aug 26 20:17:33 PDT 2025; root:libignition-58~15009/libignition_core/RELEASE_ARM64E"
+ "has_sec_transition"
+ "v16@?0r^{Pool=^{Allocator}^{Pool}^{Pool}^{AllocationMetadata}{Buffer=^vQ}^vBBB}8"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Aug 14 23:45:41 PDT 2025; root:libignition-58~13230/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Aug 14 23:45:41 PDT 2025; root:libignition-58~13230/libignition_core/RELEASE_ARM64E"
- "v16@?0r^{Pool=^{Allocator}^{Pool}^{Pool}^{AllocationMetadata}{Buffer=^vQ}^vBB}8"

```
