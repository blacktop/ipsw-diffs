## ControlsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/ControlsFlowDelegatePlugin.bundle/ControlsFlowDelegatePlugin`

```diff

-3401.11.1.0.0
+3401.14.1.0.0
   __TEXT.__text: 0x280
   __TEXT.__auth_stubs: 0xc0
   __TEXT.__cstring: 0x3d

   __TEXT.__unwind_info: 0x90
   __DATA_CONST.__auth_got: 0x60
   __DATA_CONST.__auth_ptr: 0x58
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
   Functions: 15
-  Symbols:   45
+  Symbols:   46
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
