## PassbookStubAppIntentsExtension

> `filesystem/System/Library/ExtensionKit/Extensions/PassbookStubAppIntentsExtension.appex/PassbookStubAppIntentsExtension`

```diff

-1642.6.1.0.0
+1642.6.3.0.0
   __TEXT.__text: 0x1bc
   __TEXT.__auth_stubs: 0x70
   __TEXT.__swift5_typeref: 0x46

   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x100

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5BABAB35-23C1-3A71-A820-7F53CE7D5D8B
+  UUID: 5A17A419-C495-3661-91C4-810AE223EB98
   Functions: 9
-  Symbols:   40
+  Symbols:   41
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
