## fontmover

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/Current/Support/fontmover`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-421.0.0.0.0
-  __TEXT.__text: 0x5700
-  __TEXT.__auth_stubs: 0x820
+424.0.0.0.0
+  __TEXT.__text: 0x57a0
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x200
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x5f4
-  __TEXT.__cstring: 0x531
+  __TEXT.__gcc_except_tab: 0x618
+  __TEXT.__cstring: 0x54a
   __TEXT.__oslogstring: 0x3
   __TEXT.__objc_methname: 0x14f
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x298
   __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0xc8
   __DATA.__objc_selrefs: 0x80
   __DATA.__data: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 102
-  Symbols:   161
-  CStrings:  82
+  Symbols:   162
+  CStrings:  83
 
Symbols:
+ _malloc_type_calloc
Functions:
~ sub_1000039fc : 44 -> 48
~ sub_10000466c -> sub_100004670 : 476 -> 500
~ sub_100004900 -> sub_10000491c : 476 -> 500
~ sub_10000592c -> sub_100005960 : 960 -> 984
~ sub_100005f04 -> sub_100005f50 : 320 -> 324
~ sub_100006044 -> sub_100006094 : 372 -> 452
CStrings:
+ "recursion depth exceeded"
```
