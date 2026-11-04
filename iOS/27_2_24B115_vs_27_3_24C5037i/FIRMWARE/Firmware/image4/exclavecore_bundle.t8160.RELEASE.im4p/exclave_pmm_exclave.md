## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_pmm_exclave`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_fixups`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`

```diff

-1490.40.28.0.0
-  __TEXT.__text: 0x4d538
+1490.60.7.0.0
+  __TEXT.__text: 0x4d678
   __TEXT.__const: 0x1d140
-  __TEXT.__cstring: 0x120f8
+  __TEXT.__cstring: 0x12182
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x60
   __TEXT.__eh_frame: 0x50
-  __DATA.__const: 0x14a0
+  __DATA.__const: 0x14d8
   __DATA.__data: 0x2421
-  __DATA.__auth_ptr: 0x30
+  __DATA.__auth_ptr: 0x28
   __DATA.__ENDPOINTS: 0x93f
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x18

   __PDATA.__shared_cache: 0x0
   Functions: 14
   Symbols:   4
-  CStrings:  1529
+  CStrings:  1536
 
Functions:
~ sub_8036908 -> sub_8036a38 : 256 -> 272
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.3.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "bundle_size_kib"
+ "carveout_permanent_kib"
+ "carveout_reclaimable_kib"
+ "carveout_total_kib"
+ "cl4_allocations_kib"
+ "ipmm_usage_kib"
+ "unknown_global_stat"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
```
