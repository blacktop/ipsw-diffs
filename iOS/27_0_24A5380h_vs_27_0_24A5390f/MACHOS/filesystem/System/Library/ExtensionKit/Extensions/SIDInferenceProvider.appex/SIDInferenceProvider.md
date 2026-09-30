## SIDInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SIDInferenceProvider.appex/SIDInferenceProvider`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
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

-1.65.0.0.0
+1.69.0.0.0
   __TEXT.__text: 0x14764
   __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0x320

   __TEXT.__swift_as_cont: 0x68
   __TEXT.__unwind_info: 0x448
   __TEXT.__eh_frame: 0xab8
-  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 227
-  Symbols:   199
+  Symbols:   200
   CStrings:  134
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
```
