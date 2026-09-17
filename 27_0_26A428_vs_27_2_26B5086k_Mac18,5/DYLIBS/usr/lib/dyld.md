## dyld

> `/usr/lib/dyld`

```diff

-27062.0.0.0.0
-  __TEXT.__text: 0xa0ec8
-  __TEXT.__const: 0x1a38
-  __TEXT.__cstring: 0x13886
-  __TEXT.__unwind_info: 0x3578
+27102.0.0.0.0
+  __TEXT.__text: 0xa1138
+  __TEXT.__const: 0x1a68
+  __TEXT.__cstring: 0x1389a
+  __TEXT.__unwind_info: 0x3580
   __DATA_CONST.__const: 0x2bd0
-  __AUTH_CONST.__const: 0x6310
+  __AUTH_CONST.__const: 0x6348
   __DATA.__data: 0x1c8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__bss: 0x48
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 3369
-  Symbols:   3762
-  CStrings:  2376
+  Functions: 3372
+  Symbols:   3766
+  CStrings:  2377
 
Symbols:
+ __ZN5dyld44APIs28_dyld_with_active_atlas_PRIVEPvPFvS1_PKvmE
+ __ZNK6mach_o5Image19maxAuthRebaseOffsetEv
+ __ZNK6mach_o6Policy34enforceAuthRebasesPointWithinImageEv
+ ____ZNK6mach_o5Image19maxAuthRebaseOffsetEv_block_invoke
CStrings:
+ "27102"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri Sep  4 22:55:32 PDT 2026; root:libignition-64~25449/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Fri Sep  4 22:55:32 PDT 2026; root:libignition-64~25449/libignition_core/RELEASE_ARM64E"
+ "rebase out of range"
- "27062"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Aug 11 20:40:24 PDT 2026; root:libignition-64~19252/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Tue Aug 11 20:40:24 PDT 2026; root:libignition-64~19252/libignition_core/RELEASE_ARM64E"
```
