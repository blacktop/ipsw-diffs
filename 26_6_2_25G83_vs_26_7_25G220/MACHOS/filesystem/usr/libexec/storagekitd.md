## storagekitd

> `usr/libexec/storagekitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1037.160.3.0.0
-  __TEXT.__text: 0x194c0c
-  __TEXT.__auth_stubs: 0x2ec0
+1037.160.3.700.2
+  __TEXT.__text: 0x194d2c
+  __TEXT.__auth_stubs: 0x2ed0
   __TEXT.__objc_stubs: 0xef00
   __TEXT.__objc_methlist: 0x80f4
   __TEXT.__const: 0xc98

   __TEXT.__objc_classname: 0xd84
   __TEXT.__objc_methtype: 0x631b
   __TEXT.__gcc_except_tab: 0x2718
-  __TEXT.__cstring: 0x680c4
-  __TEXT.__unwind_info: 0x2af8
+  __TEXT.__cstring: 0x68196
+  __TEXT.__unwind_info: 0x2b00
   __TEXT.__eh_frame: 0x168
-  __DATA_CONST.__auth_got: 0x1770
+  __DATA_CONST.__auth_got: 0x1778
   __DATA_CONST.__got: 0xb48
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA_CONST.__const: 0x2b80
-  __DATA_CONST.__cfstring: 0x3f7a0
+  __DATA_CONST.__cfstring: 0x3f7e0
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3622
-  Symbols:   1120
-  CStrings:  14568
+  Functions: 3623
+  Symbols:   1121
+  CStrings:  14573
 
Symbols:
+ _memcmp
Functions:
~ sub_1000fe2e8 : 55868 -> 55852
+ sub_10010bd14
CStrings:
+ ". picture file outside allowed dirs: canonical=%s"
+ ". picture file realpath failed: path=%@ errno=%d"
+ "/Library/User Pictures/"
+ "/System/Library/Templates/Data/Library/User Pictures/"
+ "_DMOpenUserPictureFileForPreboot"
```
