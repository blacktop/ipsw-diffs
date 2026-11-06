## aidearlyboot

> `/usr/libexec/aidearlyboot`

### Sections with Same Size but Changed Content

- `__TEXT.__info_plist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10400.41.0.0.0
-  __TEXT.__text: 0xa524
+10410.3.0.0.0
+  __TEXT.__text: 0xa614
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0xee5
-  __TEXT.__const: 0xd668
-  __TEXT.__objc_methname: 0xab8
+  __TEXT.__objc_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x344
+  __TEXT.__cstring: 0xefc
+  __TEXT.__const: 0xd672
+  __TEXT.__objc_methname: 0xad4
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methtype: 0x220
+  __TEXT.__objc_methtype: 0x22b
   __TEXT.__info_plist: 0x3cb
   __TEXT.__unwind_info: 0x480
-  __DATA_CONST.__const: 0x1850
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__const: 0x1860
+  __DATA_CONST.__cfstring: 0xc00
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x500
-  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_selrefs: 0x390
   __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xe8

   - /usr/lib/libobjc.A.dylib
   Functions: 295
   Symbols:   116
-  CStrings:  295
+  CStrings:  298
 
Symbols:
+ _MGIsDeviceOneOfType
- _MGGetProductType
CStrings:
+ "earlyBootOptionsForService:"
+ "hid-early-boot-options"
+ "i20@0:8I16"
```
