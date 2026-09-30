## modelcatalogdump

> `/usr/bin/modelcatalogdump`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-302.6.0.3.0
-  __TEXT.__text: 0x19cbc
-  __TEXT.__auth_stubs: 0x1250
+308.7.0.1.0
+  __TEXT.__text: 0x19c78
+  __TEXT.__auth_stubs: 0x1260
   __TEXT.__objc_stubs: 0x120
   __TEXT.__const: 0x5e4
   __TEXT.__swift5_entry: 0x8

   __TEXT.__objc_methname: 0x9e
   __TEXT.__unwind_info: 0x630
   __TEXT.__eh_frame: 0x10a8
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x930
+  __DATA_CONST.__auth_got: 0x938
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x228
   __DATA.__objc_selrefs: 0x48

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 543
-  Symbols:   124
+  Functions: 542
+  Symbols:   126
   CStrings:  54
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ _setvbuf
```
