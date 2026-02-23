## dyld

> `/usr/lib/dyld`

```diff

-1376.3.0.0.0
-  __TEXT.__text: 0x90fec
+1376.6.0.0.0
+  __TEXT.__text: 0x9146c
   __TEXT.__const: 0x2038
   __TEXT.__cstring: 0xffdd
   __TEXT.__unwind_info: 0x4f0
-  __DATA_CONST.__const: 0x4be8
+  __DATA_CONST.__const: 0x4c08
   __AUTH_CONST.__const: 0x24a0
   __DATA.__data: 0x1b0
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 504F6008-70BC-3F1E-B6B8-9D0B429ED3B9
-  Functions: 2989
-  Symbols:   7542
+  UUID: 7108E40C-BAF1-31C6-9F63-EE14FF0D01B3
+  Functions: 2990
+  Symbols:   7545
   CStrings:  2000
 
Symbols:
+ ____ZN3lsl13MemoryManager26withWritableMemoryInternalIZZZN5dyld44APIs15_dyld_lazy_loadEPjPK11mach_headerEUb2_EUb3_E4$_11EEvT__block_invoke
+ ___block_descriptor_tmp.272
Functions:
~ __ZN5dyld412RuntimeLocksC1Ev : 16 -> 20
~ _dyld_parse_boot_arg_int : 428 -> 456
~ ____ZN5dyld44APIs15_dyld_lazy_loadEPjPK11mach_header_block_invoke : 316 -> 420
~ ____ZN5dyld44APIs15_dyld_lazy_loadEPjPK11mach_header_block_invoke_2 : 520 -> 1272
~ __ZZN5dyld412RuntimeLocks37withLoadersWriteLockAndProtectedStackIZZNS_4APIs11dlopen_fromEPKciPvENK3$_0clEvEUlvE0_EEvT_ENKUlvE_clEv : 292 -> 340
~ ____ZN3lsl13MemoryManager18withProtectedStackIZZN5dyld412RuntimeLocks37withLoadersWriteLockAndProtectedStackIZZNS2_4APIs11dlopen_fromEPKciPvENK3$_0clEvEUlvE0_EEvT_ENKUlvE_clEvEUlvE_EEvSB__block_invoke : 40 -> 120
+ ____ZN3lsl13MemoryManager26withWritableMemoryInternalIZZZN5dyld44APIs15_dyld_lazy_loadEPjPK11mach_headerEUb2_EUb3_E4$_11EEvT__block_invoke
~ __ZN5dyld412RuntimeLocks18takeLockBeforeForkEv : 280 -> 320
~ __ZN5dyld412RuntimeLocks23releaseLockInForkParentEv : 264 -> 300
~ __ZN5dyld412RuntimeLocks20resetLockInForkChildEv : 152 -> 156
~ ____ZN5dyld412RuntimeState12notifyUnloadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEE_block_invoke : 408 -> 412
~ __ZZZN5dyld412RuntimeState10notifyLoadERKNSt3__14spanIPKNS_6LoaderELm18446744073709551615EEEEUb_ENK3$_8clEv : 1224 -> 1256
CStrings:
+ "/Library/Caches/com.apple.xbs/F0FFD1D7-CAB1-4A5A-8240-A251B11CAB4A/TemporaryDirectory.U9jDxc/Binaries/libignition/install/Symbols/ignition_core"
+ "1376.6"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Feb 15 20:56:12 PST 2026; root:libignition-58~36169/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sun Feb 15 20:56:12 PST 2026; root:libignition-58~36169/libignition_core/RELEASE_ARM64E"
- "/Library/Caches/com.apple.xbs/C3F7015A-71D3-4436-82F7-3C1FE69E5CAD/TemporaryDirectory.Tahj7C/Binaries/libignition/install/Symbols/ignition_core"
- "1376.3"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Feb  4 22:52:00 PST 2026; root:libignition-58~35779/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Wed Feb  4 22:52:00 PST 2026; root:libignition-58~35779/libignition_core/RELEASE_ARM64E"

```
