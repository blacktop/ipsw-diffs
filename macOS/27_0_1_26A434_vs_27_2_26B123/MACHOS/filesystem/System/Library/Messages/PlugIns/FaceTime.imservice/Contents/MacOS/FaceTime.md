## FaceTime

> `/System/Library/Messages/PlugIns/FaceTime.imservice/Contents/MacOS/FaceTime`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1491.100.1.1.13
-  __TEXT.__text: 0x1fae0
-  __TEXT.__auth_stubs: 0x470
+1491.200.101.1.3
+  __TEXT.__text: 0x1fb08
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x25e0
   __TEXT.__objc_methlist: 0x1154
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x1844
   __TEXT.__cstring: 0x1bf1
-  __TEXT.__oslogstring: 0x2a51
+  __TEXT.__oslogstring: 0x2a79
   __TEXT.__objc_methname: 0x29ce
   __TEXT.__objc_classname: 0x127
   __TEXT.__objc_methtype: 0xb15

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x2a8
   __DATA.__objc_const: 0x2088
   __DATA.__objc_selrefs: 0xb00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 392
-  Symbols:   164
-  CStrings:  933
+  Symbols:   166
+  CStrings:  934
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
Functions:
~ sub_158b8 : 848 -> 860
~ sub_15d7c -> sub_15d88 : 128 -> 156
CStrings:
+ "Failed type check! {key: %@, class: %@}"
```
