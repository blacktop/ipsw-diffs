## PaymentsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/PaymentsFlowDelegatePlugin.bundle/PaymentsFlowDelegatePlugin`

```diff

-3401.4.1.0.0
+3401.6.1.0.0
   __TEXT.__text: 0xe40
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__const: 0xae

   __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 33
-  Symbols:   436
+  Symbols:   439
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_PaymentsFlowDelegatePlugin

```
