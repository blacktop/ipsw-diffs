## SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

-3401.11.1.0.0
+3401.14.1.0.0
   __TEXT.__text: 0x1df0
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__swift5_typeref: 0xd7

   __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x98
   __DATA.__bss: 0x280

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 82
-  Symbols:   788
+  Symbols:   791
   CStrings:  22
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_SearchToolExtension

```
