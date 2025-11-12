## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

 1335.0.0.0.0
-  __TEXT.__text: 0x53628
+  __TEXT.__text: 0x53668
   __TEXT.__const: 0x1bb39
   __TEXT.__cstring: 0xcfc2
   __TEXT.__unwind_info: 0x7e0

   __DATA.__common: 0x4c0
   __DATA.__bss: 0xb5fa0
   __DATA_DIRTY.__all_image_info: 0x170
-  UUID: 75D3AADB-D7A2-3EF6-987D-8466789AF5C6
+  UUID: 829D6338-3412-3B03-8E85-24383D5D8467
   Functions: 2365
   Symbols:   2596
   CStrings:  1344
Functions:
~ _write_float : 112 -> 120
~ ___vsnprintf_chk : 96 -> 108
~ __liblibc_seed_insecure_rand : 88 -> 96
~ ___memcpy_chk : 88 -> 100
~ _decimalLength9 : 220 -> 224
~ _multipleOfPowerOf2 : 68 -> 72
~ _ZN3lsl9Allocator18AllocationMetadata11setPoolHintEPNS0_4PoolE.cold.1 : 52 -> 68
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBS9ugAvIbyfkEdTcNxLrj1p5jBC_mCZmVJLeD4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.2.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CAo3ugBp3ovfsOqi1Rhz_-Hzaj0wSchq_yNrDnk/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.2.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"

```
