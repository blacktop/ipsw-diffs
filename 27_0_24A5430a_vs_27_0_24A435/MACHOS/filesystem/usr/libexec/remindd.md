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
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 4046.11.0.0.0
-  __TEXT.__text: 0x80f6c8
-  __TEXT.__auth_stubs: 0x8c50
-  __TEXT.__objc_stubs: 0x1bc40
+  __TEXT.__text: 0x80f7d0
+  __TEXT.__auth_stubs: 0x8c60
+  __TEXT.__objc_stubs: 0x1bc60
   __TEXT.__objc_methlist: 0xab90
   __TEXT.__const: 0x292b8
-  __TEXT.__objc_methname: 0x284b1
+  __TEXT.__objc_methname: 0x284c1
   __TEXT.__objc_classname: 0x6396
   __TEXT.__cstring: 0x18c47
   __TEXT.__objc_methtype: 0x43d7
   __TEXT.__gcc_except_tab: 0x20f0
-  __TEXT.__oslogstring: 0x618b0
+  __TEXT.__oslogstring: 0x618f0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x143ce
   __TEXT.__swift5_fieldmd: 0xa7e4

   __TEXT.__swift_as_ret: 0x204
   __TEXT.__swift_as_cont: 0x410
   __TEXT.__swift5_mpenum: 0xe0
-  __TEXT.__unwind_info: 0x10348
+  __TEXT.__unwind_info: 0x10340
   __TEXT.__eh_frame: 0x1f588
   __DATA_CONST.__const: 0x26068
   __DATA_CONST.__cfstring: 0x51a0

   __DATA_CONST.__objc_arrayobj: 0x390
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA_CONST.__auth_got: 0x4638
+  __DATA_CONST.__auth_got: 0x4640
   __DATA_CONST.__got: 0x3530
   __DATA_CONST.__auth_ptr: 0x28a0
   __DATA.__objc_const: 0x1de08
-  __DATA.__objc_selrefs: 0x7cd8
+  __DATA.__objc_selrefs: 0x7ce0
   __DATA.__objc_ivar: 0x48c
   __DATA.__objc_data: 0x8708
   __DATA.__data: 0x1f330

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 22663
-  Symbols:   4278
-  CStrings:  11815
+  Symbols:   4279
+  CStrings:  11817
 
Symbols:
+ _swift_release_x11
CStrings:
+ "RDFeedbackProvider: Survey is not enabled for non-seed builds."
+ "enableGroceryFeedbackSurvey"
```
