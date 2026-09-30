## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
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

-1056.0.12.0.0
-  __TEXT.__text: 0x50928
+1056.0.17.0.0
+  __TEXT.__text: 0x50a7c
   __TEXT.__auth_stubs: 0x22e0
   __TEXT.__objc_stubs: 0x4380
   __TEXT.__objc_methlist: 0x10c0
-  __TEXT.__cstring: 0x5b7b
+  __TEXT.__cstring: 0x5b8b
   __TEXT.__const: 0x10f8
   __TEXT.__objc_methname: 0x4bad
-  __TEXT.__oslogstring: 0x2e41
+  __TEXT.__oslogstring: 0x2e71
   __TEXT.__objc_classname: 0x2b4
   __TEXT.__objc_methtype: 0xa9e
   __TEXT.__gcc_except_tab: 0x4f4

   __TEXT.__unwind_info: 0xc28
   __TEXT.__eh_frame: 0x638
   __DATA_CONST.__const: 0x1a88
-  __DATA_CONST.__cfstring: 0x7c40
+  __DATA_CONST.__cfstring: 0x7c60
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1129
   Symbols:   848
-  CStrings:  2345
+  CStrings:  2347
 
Functions:
~ sub_10001c774 : 11384 -> 11724
CStrings:
+ "Stripping thread state (register information)"
+ "mdworker"
```
