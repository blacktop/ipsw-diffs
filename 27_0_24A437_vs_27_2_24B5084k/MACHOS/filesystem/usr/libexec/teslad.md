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

-113.2.5.0.0
-  __TEXT.__text: 0xe2f4
+113.40.17.0.0
+  __TEXT.__text: 0xe3b0
   __TEXT.__auth_stubs: 0x560
   __TEXT.__objc_stubs: 0x26e0
   __TEXT.__objc_methlist: 0x1744
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x54
   __TEXT.__oslogstring: 0xd2e
-  __TEXT.__cstring: 0x13ba
+  __TEXT.__cstring: 0x13ea
   __TEXT.__objc_classname: 0x694
   __TEXT.__objc_methtype: 0xbd4
   __TEXT.__dlopen_cstrs: 0xaa
   __TEXT.__objc_methname: 0x2f04
   __TEXT.__unwind_info: 0x518
-  __DATA_CONST.__const: 0x840
-  __DATA_CONST.__cfstring: 0x1e00
+  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__cfstring: 0x1e80
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 425
   Symbols:   191
-  CStrings:  971
+  CStrings:  975
 
Functions:
~ sub_10000c4c0 : 4820 -> 5008
CStrings:
+ "OrganizationID"
+ "OrganizationType"
+ "org-id"
+ "org-type"
```
