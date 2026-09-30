## AppLaunchIntentExtension

> `/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension`

```diff

-3401.3.1.0.0
+3401.4.1.0.0
   __TEXT.__text: 0xf84
   __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x2c

   __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 27
-  Symbols:   79
+  Symbols:   80
   CStrings:  30
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
