## ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/Contents/MacOS/ScreenTimeDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-645.1.401.0.0
+649.0.0.0.0
   __TEXT.__text: 0x1fcc
   __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0xc2
+  __TEXT.__const: 0xb2
   __TEXT.__cstring: 0x63
   __TEXT.__oslogstring: 0x1b3
   __TEXT.__objc_classname: 0x5b

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xf8
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 40
-  Symbols:   73
+  Symbols:   74
   CStrings:  41
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
```
