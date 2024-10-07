## ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

-6.1.13.0.0
+6.1.20.2.1
   __TEXT.__text: 0x277c
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__const: 0x262

   __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x108

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 93
-  Symbols:   82
+  Symbols:   83
   CStrings:  3
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
