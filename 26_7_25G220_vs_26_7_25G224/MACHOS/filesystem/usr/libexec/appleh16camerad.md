## appleh16camerad

> `usr/libexec/appleh16camerad`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 5.605.0.0.0
-  __TEXT.__text: 0x7eee0
+  __TEXT.__text: 0x7eab0
   __TEXT.__auth_stubs: 0x1710
   __TEXT.__objc_stubs: 0x9c0
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x63bf
+  __TEXT.__cstring: 0x6320
   __TEXT.__const: 0x17970
-  __TEXT.__gcc_except_tab: 0x1ed0
+  __TEXT.__gcc_except_tab: 0x1ec0
   __TEXT.__oslogstring: 0x435d
   __TEXT.__objc_methname: 0x9f4
   __TEXT.__objc_classname: 0xaa

   __DATA_CONST.__got: 0x1258
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0xa3a8
-  __DATA_CONST.__cfstring: 0x23c0
+  __DATA_CONST.__cfstring: 0x2320
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libz.1.dylib
   Functions: 1340
   Symbols:   977
-  CStrings:  1486
+  CStrings:  1481
 
Functions:
~ sub_10003ac68 : 10132 -> 10096
~ sub_100049b10 -> sub_100049aec : 24944 -> 24624
~ sub_10004fd9c -> sub_10004fc38 : 140720 -> 140004
CStrings:
- "TimewarpActualFrameRate_Private"
- "TimewarpDecimationLevel_Private"
- "TimewarpDecimationTag_Private"
- "TimewarpDesiredFrameRate_Private"
- "TimewarpShouldSkipFrame_Private"
```
