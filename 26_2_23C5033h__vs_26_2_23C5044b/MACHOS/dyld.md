## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x4c0
-  __DATA.__bss: 0xb5fa0
+  __DATA.__bss: 0xb5fb0
   __DATA_DIRTY.__all_image_info: 0x170
-  UUID: 829D6338-3412-3B03-8E85-24383D5D8467
+  UUID: 629F1CF8-6A9A-3BD2-89BB-1522B68AAFD1
   Functions: 2365
   Symbols:   2596
   CStrings:  1344
Functions:
~ _vas__easm_setup_ek : 1504 -> 1500
~ _xrt__vtable_kernel_object_get : 36 -> 32
~ _ZN3lsl9Allocator18AllocationMetadata11setPoolHintEPNS0_4PoolE.cold.1 : 68 -> 76
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CCGQugCzvatom1VUenAngiiAxfa8nJuUooTQdjg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.2.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CBS9ugAvIbyfkEdTcNxLrj1p5jBC_mCZmVJLeD4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.2.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"

```
