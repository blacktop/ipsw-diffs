## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x4c0
-  __DATA.__bss: 0xb5fa0
+  __DATA.__bss: 0xb5fb0
   __DATA_DIRTY.__all_image_info: 0x170
-  UUID: 50A57B5F-C696-3B8B-BF01-C48CACAF59A3
+  UUID: E6F47634-70EA-3648-8915-8C25D14019B1
   Functions: 2365
   Symbols:   2596
   CStrings:  1344
Functions:
~ _vas__easm_setup_ek : 1504 -> 1500
~ _xrt__vtable_kernel_object_get : 36 -> 32
~ _ZN3lsl9Allocator18AllocationMetadata11setPoolHintEPNS0_4PoolE.cold.1 : 52 -> 60
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B_x3ugCTMmCMufX5byhi94SSe9Rsk8vVBK8Wy1k/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.1.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B_YgugAzVvar5Fl0K-Xs1Sc6MQAwkidCZyCVkts/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.1.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"

```
