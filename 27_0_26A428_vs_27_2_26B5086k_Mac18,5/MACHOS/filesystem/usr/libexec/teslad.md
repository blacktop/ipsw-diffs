## teslad

> `/usr/libexec/teslad`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0xce44
+113.40.17.0.0
+  __TEXT.__text: 0xcefc
   __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_stubs: 0x2120
   __TEXT.__objc_methlist: 0x13bc

   __TEXT.__objc_classname: 0x518
   __TEXT.__objc_methtype: 0xa3e
   __TEXT.__objc_methname: 0x2aae
-  __TEXT.__cstring: 0x12fb
+  __TEXT.__cstring: 0x132b
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__unwind_info: 0x490
-  __DATA_CONST.__const: 0x7e8
-  __DATA_CONST.__cfstring: 0x1cc0
+  __DATA_CONST.__const: 0x808
+  __DATA_CONST.__cfstring: 0x1d40
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 367
   Symbols:   147
-  CStrings:  895
+  CStrings:  899
 
Functions:
~ sub_10000b008 : 4760 -> 4944
CStrings:
+ "OrganizationID"
+ "OrganizationType"
+ "org-id"
+ "org-type"
```
