## remindd

> `/usr/libexec/remindd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__objc_stublist`

```diff

 4080.0.0.0.0
-  __TEXT.__text: 0x7f9940
+  __TEXT.__text: 0x7f9a24
   __TEXT.__auth_stubs: 0x8d10
-  __TEXT.__objc_stubs: 0x1bf40
+  __TEXT.__objc_stubs: 0x1bf60
   __TEXT.__objc_methlist: 0xac90
   __TEXT.__const: 0x29588
-  __TEXT.__objc_methname: 0x28891
+  __TEXT.__objc_methname: 0x288a1
   __TEXT.__objc_classname: 0x63f6
   __TEXT.__cstring: 0x18e47
   __TEXT.__objc_methtype: 0x4347
   __TEXT.__gcc_except_tab: 0x213c
-  __TEXT.__oslogstring: 0x62830
+  __TEXT.__oslogstring: 0x62870
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x1446a
   __TEXT.__swift5_fieldmd: 0xa8a4

   __DATA_CONST.__got: 0x35b0
   __DATA_CONST.__auth_ptr: 0x28e8
   __DATA.__objc_const: 0x1dfd0
-  __DATA.__objc_selrefs: 0x7db8
+  __DATA.__objc_selrefs: 0x7dc0
   __DATA.__objc_ivar: 0x490
   __DATA.__objc_data: 0x87e8
   __DATA.__data: 0x1f560

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 22874
   Symbols:   4305
-  CStrings:  11910
+  CStrings:  11912
 
Functions:
~ sub_10010cd34 : 352 -> 364
~ sub_10010ce94 -> sub_10010cea0 : 1124 -> 1340
CStrings:
+ "RDFeedbackProvider: Survey is not enabled for non-seed builds."
+ "enableGroceryFeedbackSurvey"
```
