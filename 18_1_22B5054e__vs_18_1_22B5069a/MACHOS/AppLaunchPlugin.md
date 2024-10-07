## AppLaunchPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin`

```diff

-3401.3.1.0.0
+3401.4.1.0.0
   __TEXT.__text: 0x2160
   __TEXT.__auth_stubs: 0x440
   __TEXT.__const: 0x9a

   __DATA_CONST.__auth_got: 0x220
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 47
-  Symbols:   74
+  Symbols:   75
   CStrings:  28
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
