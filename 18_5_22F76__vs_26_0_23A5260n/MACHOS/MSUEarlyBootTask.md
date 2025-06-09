## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-2171.120.44.0.1
-  __TEXT.__text: 0x3c14
+2422.0.15.0.2
+  __TEXT.__text: 0x3bc0
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0x460
-  __TEXT.__cstring: 0x2980
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__cstring: 0x27f2
   __TEXT.__const: 0x444
-  __TEXT.__objc_methname: 0x31d
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__objc_methname: 0x2e8
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x118
+  __DATA.__objc_selrefs: 0x108
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /usr/lib/libMobileGestalt.dylib
-  - /usr/lib/libSecureMAHelper.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DFD2362-B208-3026-9358-EE35E6C98309
-  Functions: 24
-  Symbols:   318
-  CStrings:  328
+  - /usr/lib/libpartition2_dynamic.dylib
+  UUID: CA307B38-8E3E-3A38-A521-9BAEB462592F
+  Functions: 23
+  Symbols:   310
+  CStrings:  319
 
Symbols:
+ /AppleInternal/Library/BuildRoots/4~B2JtugCE-2OzM46J-igsKLkeEMnvxtqFUIF7OJA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- _OBJC_CLASS_$_SecureMAHelper
- _graftSecureAssets
- _objc_msgSend$graftSecureAssetsFromLastBootSession
- _objc_msgSend$initWithLogger:
Functions:
~ _main : 8332 -> 8416
- _graftSecureAssets
CStrings:
- "%s: Failed to graft SMA's from previous boot attempt"
- "=========================MSUEarlyBootTask: Running on reboot==========================\n"
- "Failed to graft"
- "MSUEarlyBootTask: %s secure assets from previous boot session\n"
- "MSUEarlyBootTask: Attempting to determine secure assets grafted during previous boot\n"
- "MSUEarlyBootTask: Failed to allocate secureAssetHelper to graft SMA's\n"
- "Successfully grafted"
- "graftSecureAssetsFromLastBootSession"
- "initWithLogger:"

```
