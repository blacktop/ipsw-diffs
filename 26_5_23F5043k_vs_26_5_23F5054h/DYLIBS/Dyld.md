## dyld

> `/usr/lib/dyld`

```diff

-1377.1.0.0.0
-  __TEXT.__text: 0x915cc
-  __TEXT.__const: 0x2088
-  __TEXT.__cstring: 0xffdd
+1377.2.1.0.0
+  __TEXT.__text: 0x9173c
+  __TEXT.__const: 0x2098
+  __TEXT.__cstring: 0xffdf
   __TEXT.__unwind_info: 0x4f0
   __DATA_CONST.__const: 0x4c08
   __AUTH_CONST.__const: 0x24a0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  UUID: CEE97364-1653-31C5-BCEA-B6989815BC72
-  Functions: 2990
-  Symbols:   7549
+  UUID: 4F1B9181-F514-3C23-9C5D-0A61AFB7D71D
+  Functions: 2991
+  Symbols:   7551
   CStrings:  2000
 
Symbols:
+ __ZN5dyld412RuntimeLocks15couldDlopenLockEv
Functions:
~ __ZN5dyld44APIs11dlopen_fromEPKciPv : 1228 -> 1240
~ ____ZN5dyld412RuntimeState15PermanentRanges4makeERS0_RKN5dyld35ArrayIPKNS_6LoaderEEE_block_invoke : 220 -> 208
~ ____ZN5dyld46Loader9getLoaderER11DiagnosticsRNS_12RuntimeStateEPKcRKNS0_11LoadOptionsE_block_invoke : 3172 -> 3340
~ __ZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEv : 3344 -> 3404
~ __ZN3lsl14ProtectedStack18withProtectedStackEU13block_pointerFvvE : 564 -> 560
~ __ZZZN5dyld44APIs11dlopen_fromEPKciPvENK3$_0clEvENKUlvE_clEv : 3356 -> 3376
~ __ZNK5dyld416JustInTimeLoader15runInitializersERNS_12RuntimeStateE : 204 -> 216
~ __ZN5dyld4L7prepareERNS_4APIsEPKN6mach_o12UnsafeHeaderE : 5144 -> 5148
+ __ZN5dyld412RuntimeLocks15couldDlopenLockEv
~ _ccsha384_vng_arm_hw_compress : 16 -> 8
CStrings:
+ "1377.2.1"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Apr  5 21:35:24 PDT 2026; root:libignition-58~37472/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sun Apr  5 21:35:24 PDT 2026; root:libignition-58~37472/libignition_core/RELEASE_ARM64E"
- "1377.1"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Mar 23 20:56:16 PDT 2026; root:libignition-58~37217/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Mar 23 20:56:16 PDT 2026; root:libignition-58~37217/libignition_core/RELEASE_ARM64E"

```
