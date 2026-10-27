## SiriAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/SiriAutoEvalPlugin.appex/Contents/MacOS/SiriAutoEvalPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-42.0.0.0.0
+47.0.0.0.0
   __TEXT.__text: 0xa058
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_stubs: 0x80

   __TEXT.__swift5_capture: 0x14
   __TEXT.__unwind_info: 0x400
   __TEXT.__eh_frame: 0x708
-  __DATA_CONST.__const: 0x541
+  __DATA_CONST.__const: 0x549
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x578

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMediaIO.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIOKit.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 215
-  Symbols:   108
+  Symbols:   109
   CStrings:  35
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMediaIO
```
