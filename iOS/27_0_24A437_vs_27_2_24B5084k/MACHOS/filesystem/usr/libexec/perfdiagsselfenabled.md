## perfdiagsselfenabled

> `/usr/libexec/perfdiagsselfenabled`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0xc54c
+430.0.0.0.0
+  __TEXT.__text: 0xc5ac
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0xf40
-  __TEXT.__objc_methlist: 0xae4
-  __TEXT.__const: 0x23c
-  __TEXT.__cstring: 0x14b6
+  __TEXT.__objc_methlist: 0xaf0
+  __TEXT.__const: 0x20c
+  __TEXT.__cstring: 0x14c0
   __TEXT.__oslogstring: 0x2096
   __TEXT.__objc_classname: 0xd2
   __TEXT.__objc_methtype: 0x553
-  __TEXT.__objc_methname: 0x34a7
+  __TEXT.__objc_methname: 0x34bb
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x368
   __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__cfstring: 0x16a0
   __DATA_CONST.__objc_classlist: 0x58

   __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x1bd0
-  __DATA.__objc_selrefs: 0x788
+  __DATA.__objc_selrefs: 0x790
   __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 321
+  Functions: 322
   Symbols:   130
-  CStrings:  842
+  CStrings:  843
 
CStrings:
+ "allTaskingPrefNames"
+ "com.apple.chrono.WidgetRenderer-"
- "WidgetRenderer-Default"
```
