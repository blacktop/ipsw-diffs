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
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-934.160.3.0.0
-  __TEXT.__text: 0x353bc
+934.160.4.0.0
+  __TEXT.__text: 0x35480
   __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_stubs: 0x3c80
   __TEXT.__objc_methlist: 0xed0
-  __TEXT.__cstring: 0x52e7
+  __TEXT.__cstring: 0x52f7
   __TEXT.__const: 0x568
   __TEXT.__objc_methname: 0x40ef
-  __TEXT.__oslogstring: 0x1f02
+  __TEXT.__oslogstring: 0x1f32
   __TEXT.__objc_classname: 0x2f4
   __TEXT.__objc_methtype: 0xa0e
   __TEXT.__gcc_except_tab: 0x4bc

   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x188
   __DATA_CONST.__const: 0x1140
-  __DATA_CONST.__cfstring: 0x7860
+  __DATA_CONST.__cfstring: 0x7880
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 755
   Symbols:   634
-  CStrings:  2111
+  CStrings:  2113
 
Functions:
~ sub_10001b600 : 12016 -> 12212
CStrings:
+ "Stripping thread state (register information)"
+ "mdworker"
```
