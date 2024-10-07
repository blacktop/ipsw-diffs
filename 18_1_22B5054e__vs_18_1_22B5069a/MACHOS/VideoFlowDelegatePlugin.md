## VideoFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/VideoFlowDelegatePlugin.bundle/VideoFlowDelegatePlugin`

```diff

-3401.10.1.0.0
+3401.13.2.0.0
   __TEXT.__text: 0x1674
   __TEXT.__auth_stubs: 0x380
   __TEXT.__cstring: 0x138

   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x60
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
   Functions: 37
-  Symbols:   62
+  Symbols:   63
   CStrings:  14
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
