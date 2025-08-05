## Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

-238.0.0.0.0
+240.1.0.0.0
   __TEXT.__text: 0x175c
   __TEXT.__auth_stubs: 0x460
   __TEXT.__const: 0x204

   __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0xd0
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 32397552-C3F4-376F-9A53-ED9E59B4FD2A
+  UUID: 871AAB34-E392-367D-AB76-91D0FF214AC8
   Functions: 35
-  Symbols:   149
+  Symbols:   150
   CStrings:  9
 
Symbols:
+ _$s15AXCoreUtilities5AXLogO10magdefault2os6LoggerVvgZ
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
- _$s16MagnifierSupport3LogV7default2os6LoggerVvgZ

```
