## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-1513.2.1.0.0
-  __TEXT.__text: 0x78d4
+1513.40.8.0.0
+  __TEXT.__text: 0x7904
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1600
+  __TEXT.__objc_stubs: 0x1620
   __TEXT.__objc_methlist: 0x5fc
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x80
   __TEXT.__cstring: 0x2b08
   __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__objc_methname: 0x1deb
+  __TEXT.__objc_methname: 0x1e03
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methtype: 0x3cf
   __TEXT.__oslogstring: 0x142

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x850
-  __DATA.__objc_selrefs: 0x728
+  __DATA.__objc_selrefs: 0x730
   __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37C4D8E6-82C1-336F-AD1D-A45F136389C4
+  UUID: 309635BA-0935-32E7-8B57-54CDDE01A72C
   Functions: 123
   Symbols:   177
-  CStrings:  705
+  CStrings:  706
 
Functions:
~ sub_58e0 : 1160 -> 1208
CStrings:
+ "initWithName:client:transferPath:diskSpaceNeeded:location:error:"
+ "location"
- "initWithName:client:transferPath:diskSpaceNeeded:"

```
