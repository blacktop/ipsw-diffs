## dyld

> `/usr/lib/dyld`

```diff

-27062.0.0.0.0
-  __TEXT.__text: 0x9a3c4
-  __TEXT.__const: 0x1978
-  __TEXT.__cstring: 0x12573
-  __TEXT.__unwind_info: 0x3648
-  __DATA_CONST.__const: 0x55f0
-  __AUTH_CONST.__const: 0x2758
+27102.0.0.0.0
+  __TEXT.__text: 0x9a61c
+  __TEXT.__const: 0x1998
+  __TEXT.__cstring: 0x12587
+  __TEXT.__unwind_info: 0x3650
+  __DATA_CONST.__const: 0x5618
+  __AUTH_CONST.__const: 0x2760
   __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__bss: 0x1bc0
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3422
-  Symbols:   3273
-  CStrings:  2255
+  Functions: 3425
+  Symbols:   3277
+  CStrings:  2256
 
Symbols:
+ __ZN5dyld44APIs28_dyld_with_active_atlas_PRIVEPvPFvS1_PKvmE
+ __ZNK6mach_o5Image19maxAuthRebaseOffsetEv
+ __ZNK6mach_o6Policy34enforceAuthRebasesPointWithinImageEv
+ ____ZNK6mach_o5Image19maxAuthRebaseOffsetEv_block_invoke
CStrings:
+ "27102"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri Sep  4 23:05:44 PDT 2026; root:libignition-64~25453/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Fri Sep  4 23:05:44 PDT 2026; root:libignition-64~25453/libignition_core/RELEASE_ARM64E"
+ "rebase out of range"
- "27062"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 21:26:15 PDT 2026; root:libignition-64~19679/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 21:26:15 PDT 2026; root:libignition-64~19679/libignition_core/RELEASE_ARM64E"
```
