## SettingsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin`

```diff

-3401.18.1.0.0
+3401.19.1.0.0
   __TEXT.__text: 0x2354
   __TEXT.__auth_stubs: 0x600
   __TEXT.__const: 0x1e6

   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0xa8
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1d8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 75
-  Symbols:   154
+  Symbols:   156
   CStrings:  40
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_SettingsFlowDelegatePlugin

```
