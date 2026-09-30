## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x3b38
+2171.100.125.0.3
+  __TEXT.__text: 0x3c14
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0x420
-  __TEXT.__cstring: 0x27bb
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__cstring: 0x2980
   __TEXT.__const: 0x444
-  __TEXT.__objc_methname: 0x2e8
+  __TEXT.__objc_methname: 0x31d
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x10
   __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_selrefs: 0x108
+  __DATA.__objc_selrefs: 0x118
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /usr/lib/libMobileGestalt.dylib
+  - /usr/lib/libSecureMAHelper.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 22
-  Symbols:   300
-  CStrings:  291
+  Functions: 24
+  Symbols:   318
+  CStrings:  300
 
Symbols:
+ /AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ _OBJC_CLASS_$_SecureMAHelper
+ _graftSecureAssets
+ _logString
+ _logfunctionv
+ _objc_msgSend$graftSecureAssetsFromLastBootSession
+ _objc_msgSend$initWithLogger:
+ _objc_retain_x25
- /AppleInternal/Library/BuildRoots/b7b4deac-d976-11ef-a629-6a83e84fab3b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- _objc_retain_x24
CStrings:
+ "%s: Failed to graft SMA's from previous boot attempt"
+ "=========================MSUEarlyBootTask: Running on first boot after update==========================\n"
+ "=========================MSUEarlyBootTask: Running on reboot==========================\n"
+ "Failed to graft"
+ "MSUEarlyBootTask: %s secure assets from previous boot session\n"
+ "MSUEarlyBootTask: Attempting to determine secure assets grafted during previous boot\n"
+ "MSUEarlyBootTask: Failed to allocate secureAssetHelper to graft SMA's\n"
+ "Successfully grafted"
+ "graftSecureAssetsFromLastBootSession"
+ "initWithLogger:"
- "MSUEarlyBootTask: I have nothing to do. Goodbye!!"

```
