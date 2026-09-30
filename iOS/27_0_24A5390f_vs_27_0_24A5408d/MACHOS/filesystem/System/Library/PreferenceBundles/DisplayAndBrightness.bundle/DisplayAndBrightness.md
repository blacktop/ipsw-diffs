## DisplayAndBrightness

> `/System/Library/PreferenceBundles/DisplayAndBrightness.bundle/DisplayAndBrightness`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1211.0.0.0.0
+1214.0.0.0.0
   __TEXT.__text: 0x22fc
   __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_stubs: 0x320

   __TEXT.__swift_as_cont: 0x4
   __TEXT.__unwind_info: 0x100
   __TEXT.__eh_frame: 0x98
-  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 47
-  Symbols:   104
+  Symbols:   105
   CStrings:  48
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
```
