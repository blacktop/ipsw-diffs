## com.apple.filesystems.cd9660

> `com.apple.filesystems.cd9660`

```diff

-46.0.0.0.0
-  __TEXT.__cstring: 0x42a
+47.40.1.0.0
+  __TEXT.__cstring: 0x490
   __TEXT.__const: 0x1016
-  __TEXT_EXEC.__text: 0x53dc
+  __TEXT_EXEC.__text: 0x5498
   __TEXT_EXEC.__auth_stubs: 0x5c0
   __DATA.__data: 0xd10
   __DATA.__common: 0x50

   __DATA_CONST.__got: 0x20
   Functions: 90
   Symbols:   295
-  CStrings:  35
+  CStrings:  37
 
Symbols:
+ cd9660_vget_internal.kalloc_type_view_1478
- cd9660_vget_internal.kalloc_type_view_1456
Functions:
~ _cd9660_rrip_getname : 152 -> 156
~ _cd9660_rrip_defname : 152 -> 192
~ _isofntrans : 136 -> 160
~ _cd9660_vget_internal : 1908 -> 2024
~ _cd9660_readdir : 1152 -> 1156
CStrings:
+ "cd9660: bad relocated record len %d for name_len %d\n"
+ "cd9660: record len %d too small for name_len %d\n"
```
