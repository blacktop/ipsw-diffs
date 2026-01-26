## dyld

> `/usr/lib/dyld`

```diff

-1335.0.0.0.0
-  __TEXT.__text: 0x8af68
+1340.0.0.0.0
+  __TEXT.__text: 0x8b740
   __TEXT.__const: 0x23e0
   __TEXT.__cstring: 0xfe42
   __TEXT.__unwind_info: 0x4f8
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x6e40
+  __DATA_CONST.__const: 0x6e80
   __DATA.__data: 0x2f0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8f0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0x71
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 62D430F6-9826-3A6C-82EA-C6565959B632
-  Functions: 2886
-  Symbols:   7288
+  UUID: 0FFC14EA-C2DF-3725-B7AF-44004B8DC998
+  Functions: 2893
+  Symbols:   7306
   CStrings:  1982
 
Symbols:
+ __ZN3lsl6VectorINSt3__14pairIPKN5dyld46LoaderEPKcEEEC2IPS9_EET_SD_RNS_9AllocatorE
+ __ZN3lsl9Allocator10makeUniqueINS_6VectorIPKN5dyld46LoaderEEEJPS6_S8_RS0_EEENS_9UniquePtrIT_EEDpOT0_
+ __ZN3lsl9UniquePtrINS_6VectorINSt3__14pairIPKN5dyld46LoaderEPKcEEEEED2Ev
+ __ZN3lsl9UniquePtrINS_6VectorIPKN5dyld46LoaderEEEED2Ev
+ __ZNK5dyld46Loader23runInitializersBottomUpERNS_12RuntimeStateERN3lsl6VectorIPKS0_EES8_
+ __ZZN5dyld412RuntimeLocks37withLoadersWriteLockAndProtectedStackIZZNS_4APIs11dlopen_fromEPKciPvENK3$_0clEvEUlvE0_EEvT_ENKUlvE_clEv
+ __ZZN5dyld412RuntimeLocks37withLoadersWriteLockAndProtectedStackIZZNS_4APIs11dlopen_fromEPKciPvENK3$_0clEvEUlvE0_EEvT_ENKUlvE_clEv.cold.1
+ ____ZN3lsl13MemoryManager18withProtectedStackIZZN5dyld412RuntimeLocks37withLoadersWriteLockAndProtectedStackIZZNS2_4APIs11dlopen_fromEPKciPvENK3$_0clEvEUlvE0_EEvT_ENKUlvE_clEvEUlvE_EEvSB__block_invoke
+ ____ZN3lsl13MemoryManager26withWritableMemoryInternalIZN5dyld412RuntimeLocks37withLoadersWriteLockAndProtectedStackIZZNS2_4APIs11dlopen_fromEPKciPvENK3$_0clEvEUlvE0_EEvT_EUlvE_EEvSB__block_invoke
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.256
- __ZNK5dyld46Loader23runInitializersBottomUpERNS_12RuntimeStateERN5dyld35ArrayIPKS0_EES8_
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.243
- ___block_descriptor_tmp.249
CStrings:
+ "1340"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Jan 22 20:34:02 PST 2026; root:libignition-58~35304/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Jan 22 20:34:02 PST 2026; root:libignition-58~35304/libignition_core/RELEASE_ARM64E"
- "1335"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jan  5 20:05:28 PST 2026; root:libignition-58~34371/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Jan  5 20:05:28 PST 2026; root:libignition-58~34371/libignition_core/RELEASE_ARM64E"

```
