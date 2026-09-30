## ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/Versions/Current/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-645.1.401.0.0
+649.0.0.0.0
   __TEXT.__text: 0x46e8
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_stubs: 0x860

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__unwind_info: 0x1e8
   __TEXT.__eh_frame: 0xe8
-  __DATA_CONST.__const: 0x420
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 116
-  Symbols:   110
+  Symbols:   111
   CStrings:  185
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
```
