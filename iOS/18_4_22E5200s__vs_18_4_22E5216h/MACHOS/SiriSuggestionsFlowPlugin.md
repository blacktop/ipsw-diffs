## SiriSuggestionsFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin`

```diff

-3404.70.4.0.0
+3404.77.1.0.0
   __TEXT.__text: 0xd038
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__const: 0x37a

   __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x1a0
-  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x3e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 303
-  Symbols:   102
+  Symbols:   104
   CStrings:  55
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
