## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

 1331.0.0.0.0
-  __TEXT.__text: 0x53528
+  __TEXT.__text: 0x53628
   __TEXT.__const: 0x1bb39
-  __TEXT.__cstring: 0xcfb7
+  __TEXT.__cstring: 0xcfc2
   __TEXT.__unwind_info: 0x7e0
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x46e8
+  __DATA_CONST.__const: 0x4718
   __DATA.__data: 0x15a8
   __DATA.__ENDPOINTS: 0x62a
   __DATA.__thread_vars: 0x0

   __DATA.__common: 0x4c0
   __DATA.__bss: 0xb5fa0
   __DATA_DIRTY.__all_image_info: 0x170
-  UUID: 51588157-3DCE-3968-B5A7-2B54B89D6991
-  Functions: 2366
-  Symbols:   2597
-  CStrings:  1343
+  UUID: E70FFB27-4073-3B91-B5F3-B6AC793A5E14
+  Functions: 2365
+  Symbols:   2596
+  CStrings:  1344
 
Symbols:
- __lock_fastpath
Functions:
~ __liblibc_plat_mtx_lock : 44 -> 20
~ _xrt__log_write_prefixed_lines : 248 -> 256
~ _xrt_sync_mutex_lock : 8 -> 164
~ __mutex_lock : 396 -> 384
~ _xrt_sync_mutex_try_lock : 40 -> 156
- __lock_fastpath
~ _xrt__thread_context_create : 1536 -> 1724
~ _ZN3lsl9Allocator18AllocationMetadata11setPoolHintEPNS0_4PoolE.cold.1 : 60 -> 52
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B-3qugAfrhoh5BcaprhpeA5kxsJ9V0kV-qfFVlA/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.1.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
+ "PAC object"
- "/AppleInternal/Library/BuildRoots/4~B9I_ugCDJB_JKcye6CED-2U6jux-RczqHP4qE4c/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.1.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"

```
