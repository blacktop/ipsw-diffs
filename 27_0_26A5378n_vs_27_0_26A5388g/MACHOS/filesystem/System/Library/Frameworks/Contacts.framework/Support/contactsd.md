## contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3837.100.1.0.0
+3839.100.3.0.0
   __TEXT.__text: 0x2f640
   __TEXT.__auth_stubs: 0x1510
   __TEXT.__objc_stubs: 0x4120

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__unwind_info: 0xa80
   __TEXT.__eh_frame: 0x610
-  __DATA_CONST.__const: 0x1328
+  __DATA_CONST.__const: 0x1330
   __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 992
-  Symbols:   606
+  Symbols:   607
   CStrings:  1376
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
```
