## VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

-593.0.2.0.0
+593.10.1.0.0
   __TEXT.__text: 0x5690
   __TEXT.__auth_stubs: 0x730
   __TEXT.__const: 0x7e2

   __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x48
   __DATA.__data: 0x238

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3E7D4E0-7976-3580-9706-D2D008C65C52
+  UUID: 94F9B868-0ABB-37B1-8FA2-3BC1A1A722C7
   Functions: 161
-  Symbols:   84
+  Symbols:   85
   CStrings:  34
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage

```
