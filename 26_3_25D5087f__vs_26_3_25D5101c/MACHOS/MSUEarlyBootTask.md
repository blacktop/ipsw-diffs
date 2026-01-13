## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-2422.80.7.0.0
+2422.80.7.0.1
   __TEXT.__text: 0x848
   __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0x160

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/MobileSoftwareUpdate
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: D2B2E1D2-2D39-3245-A9E3-63B2A80531F4
+  UUID: 8CE33566-F9AA-33D8-A9A6-17A636D56F0C
   Functions: 9
   Symbols:   110
   CStrings:  45
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CGHuugAdMg-sAV-g-f91vRHyl7Bp1X7Za1sXA1k/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
+ /AppleInternal/Library/BuildRoots/4~CGHuugAdMg-sAV-g-f91vRHyl7Bp1X7Za1sXA1k/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/
- /AppleInternal/Library/BuildRoots/4~CDy1ugCzYXGGLN7Vsbr8AMqVsIkCHPExYZVaiH8/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/MSUEarlyBootTask.build/Objects-normal/arm64e/MSUEarlyBootTask.o
- /AppleInternal/Library/BuildRoots/4~CDy1ugCzYXGGLN7Vsbr8AMqVsIkCHPExYZVaiH8/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUEarlyBootTask/

```
