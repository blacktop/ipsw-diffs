## remindd

> `/usr/libexec/remindd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
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
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

 3976.0.0.0.0
-  __TEXT.__text: 0x812750
+  __TEXT.__text: 0x812834
   __TEXT.__auth_stubs: 0x87d0
-  __TEXT.__objc_stubs: 0x1b740
+  __TEXT.__objc_stubs: 0x1b760
   __TEXT.__objc_methlist: 0xa8e0
   __TEXT.__const: 0x287f8
-  __TEXT.__objc_methname: 0x279f1
+  __TEXT.__objc_methname: 0x27a01
   __TEXT.__objc_classname: 0x60b6
   __TEXT.__objc_methtype: 0x4267
   __TEXT.__gcc_except_tab: 0x2540
   __TEXT.__cstring: 0x180b7
-  __TEXT.__oslogstring: 0x5e8b0
+  __TEXT.__oslogstring: 0x5e8f0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x14042
   __TEXT.__swift5_fieldmd: 0xa4e8

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA.__objc_const: 0x1d3c0
-  __DATA.__objc_selrefs: 0x7af8
+  __DATA.__objc_selrefs: 0x7b00
   __DATA.__objc_ivar: 0x480
   __DATA.__objc_data: 0x8450
   __DATA.__data: 0x1e630

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 22212
   Symbols:   4184
-  CStrings:  11561
+  CStrings:  11563
 
Functions:
~ sub_100139804 : 404 -> 416
~ sub_100139998 -> sub_1001399a4 : 968 -> 1184
CStrings:
+ "RDFeedbackProvider: Survey is not enabled for non-seed builds."
+ "enableGroceryFeedbackSurvey"
```
