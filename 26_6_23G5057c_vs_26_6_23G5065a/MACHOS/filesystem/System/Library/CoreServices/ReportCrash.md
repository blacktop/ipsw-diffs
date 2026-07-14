## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x32668
+  __TEXT.__text: 0x327a0
   __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0x3800
   __TEXT.__objc_methlist: 0xdd0
   __TEXT.__cstring: 0x53b7
   __TEXT.__const: 0x558
   __TEXT.__objc_methname: 0x3ca3
-  __TEXT.__oslogstring: 0x1c82
+  __TEXT.__oslogstring: 0x1cb2
   __TEXT.__objc_classname: 0x2e4
   __TEXT.__objc_methtype: 0xaee
   __TEXT.__gcc_except_tab: 0x3ec

   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x180
   __DATA_CONST.__const: 0xf98
-  __DATA_CONST.__cfstring: 0x7a40
+  __DATA_CONST.__cfstring: 0x7a60
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 699
   Symbols:   622
-  CStrings:  2050
+  CStrings:  2052
 
Functions:
~ sub_1000101b8 : 11396 -> 11708
CStrings:
+ "Stripping thread state (register information)"
+ "mdworker"
```
