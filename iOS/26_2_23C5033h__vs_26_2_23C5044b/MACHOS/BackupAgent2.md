## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2899.60.1.0.1
-  __TEXT.__text: 0x9f4c4
-  __TEXT.__auth_stubs: 0x1a30
-  __TEXT.__objc_stubs: 0xd980
+2899.60.7.0.0
+  __TEXT.__text: 0x9f528
+  __TEXT.__auth_stubs: 0x1a40
+  __TEXT.__objc_stubs: 0xd9a0
   __TEXT.__objc_methlist: 0x6be0
   __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x1bb5d
+  __TEXT.__cstring: 0x1bb72
   __TEXT.__oslogstring: 0xe828
-  __TEXT.__objc_methname: 0xfd52
+  __TEXT.__objc_methname: 0xfd72
   __TEXT.__objc_classname: 0xaeb
   __TEXT.__objc_methtype: 0x2176
   __TEXT.__gcc_except_tab: 0x2730
   __TEXT.__unwind_info: 0x1bc8
-  __DATA_CONST.__auth_got: 0xd28
+  __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x540
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1640

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0xaad0
-  __DATA.__objc_selrefs: 0x4370
+  __DATA.__objc_selrefs: 0x4378
   __DATA.__objc_ivar: 0x638
   __DATA.__objc_data: 0x2580
   __DATA.__data: 0x8d8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 269FC1A9-D53B-3E81-BBAB-9BECAAB9290C
+  UUID: 55FE3D9E-F7B6-3CC6-A214-D14994091121
   Functions: 2713
-  Symbols:   602
-  CStrings:  8939
+  Symbols:   603
+  CStrings:  8940
 
Symbols:
+ _strerror
Functions:
~ sub_10007ac70 : 932 -> 1024
~ sub_10007b080 -> sub_10007b0dc : 612 -> 620
CStrings:
+ "fsctl(APFSIOC_MAKE_OBJECT_DATALESS) error (%d) %s"
+ "internalIgnoreSetDatalessErrors"
- "set_dataless_attribute error"

```
