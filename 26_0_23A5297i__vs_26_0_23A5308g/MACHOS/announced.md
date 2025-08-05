## announced

> `/usr/libexec/announced`

```diff

-297.0.6.0.0
+297.0.7.0.0
   __TEXT.__text: 0x1108
   __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x52

   __DATA_CONST.__auth_got: 0x198
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x18

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 685DCD57-7574-3833-B705-A78E6635A416
+  UUID: AEB81B7F-3CD8-38DD-8DC9-DB2F1A57CAB9
   Functions: 22
-  Symbols:   94
+  Symbols:   95
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
