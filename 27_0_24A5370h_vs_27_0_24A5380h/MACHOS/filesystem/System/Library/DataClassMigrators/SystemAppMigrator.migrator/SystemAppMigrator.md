## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-  __TEXT.__text: 0x7d0c
-  __TEXT.__auth_stubs: 0x580
+  __TEXT.__text: 0x7d38
+  __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x62c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c64
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x2cb1
   __TEXT.__gcc_except_tab: 0x1b8
   __TEXT.__objc_methname: 0x1ec0
   __TEXT.__objc_classname: 0xa6

   __TEXT.__oslogstring: 0x142
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0x1640
+  __DATA_CONST.__cfstring: 0x1660
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x1a0
   __DATA.__objc_const: 0x880
   __DATA.__objc_selrefs: 0x750

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 129
-  Symbols:   180
-  CStrings:  722
+  Symbols:   182
+  CStrings:  724
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _os_eligibility_bring_up_daemon_4_migration
+ _os_eligibility_get_error_description
Functions:
~ sub_37e8 : 296 -> 340
CStrings:
+ "MISystemAppMigrator: Failed to bring up eligibility daemon for migration: %s"

```
