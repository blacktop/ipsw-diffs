## VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

-561.10.3.0.0
+561.10.5.0.0
   __TEXT.__text: 0x5b68
   __TEXT.__auth_stubs: 0x700
   __TEXT.__const: 0x72a

   __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x408
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x50
   __DATA.__data: 0x298

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 153
-  Symbols:   88
+  Symbols:   89
   CStrings:  41
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
