## fmflocatord

> `/usr/libexec/fmflocatord`

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
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-103.30.6.7.10
+103.31.7.12.2
   __TEXT.__text: 0x36d90
   __TEXT.__auth_stubs: 0x1700
   __TEXT.__objc_stubs: 0x70e0

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__unwind_info: 0x1368
   __TEXT.__eh_frame: 0x7c8
-  __DATA_CONST.__const: 0x20c1
+  __DATA_CONST.__const: 0x20c9
   __DATA_CONST.__cfstring: 0x3f60
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x28

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1561
-  Symbols:   597
+  Symbols:   598
   CStrings:  2611
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftIntents
```
