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
-  __TEXT.__text: 0x4def4
+1056.0.17.0.0
+  __TEXT.__text: 0x4e048
   __TEXT.__auth_stubs: 0x2530
   __TEXT.__objc_stubs: 0x4020
   __TEXT.__objc_methlist: 0xfb8
-  __TEXT.__cstring: 0x5beb
+  __TEXT.__cstring: 0x5bfb
   __TEXT.__const: 0x1100
   __TEXT.__objc_methname: 0x4710
-  __TEXT.__oslogstring: 0x2d11
+  __TEXT.__oslogstring: 0x2d31
   __TEXT.__objc_classname: 0x2b4
   __TEXT.__objc_methtype: 0xb7e
   __TEXT.__gcc_except_tab: 0x3e4

   __TEXT.__unwind_info: 0xc50
   __TEXT.__eh_frame: 0x638
   __DATA_CONST.__const: 0x1950
-  __DATA_CONST.__cfstring: 0x7da0
+  __DATA_CONST.__cfstring: 0x7dc0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1078
   Symbols:   869
-  CStrings:  2284
+  CStrings:  2286
 
Functions:
~ sub_100010d80 : 10892 -> 11232
CStrings:
+ "Stripping thread state (register information)"
+ "mdworker"
```
