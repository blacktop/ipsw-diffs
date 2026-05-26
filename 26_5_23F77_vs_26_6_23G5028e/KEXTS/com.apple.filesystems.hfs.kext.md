## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-715.120.4.0.0
+715.160.6.0.0
   __TEXT.__const: 0x1b50
   __TEXT.__cstring: 0xa4a4
-  __TEXT_EXEC.__text: 0x52170
+  __TEXT_EXEC.__text: 0x52258
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__const: 0xf50
   __DATA_CONST.__kalloc_type: 0x3340
   __DATA_CONST.__kalloc_var: 0x690
-  UUID: C84AAD0A-4ED8-321A-A38B-3791E55F042A
+  UUID: E24CD6BA-1188-3BD0-A4EC-FCFF7BB7815C
   Functions: 532
   Symbols:   0
   CStrings:  869
Functions:
~ sub_fffffe00099a5e64 -> sub_fffffe0009a465a4 : 944 -> 1016
~ _BTIterateRecord : 1808 -> 1828
~ _BTIterateRecords : 1936 -> 1952
~ _hfs_getxattr_internal : 1524 -> 1580
~ _hfs_setxattr_internal : 2408 -> 2420
~ _remove_attribute_records : 688 -> 736
~ sub_fffffe00099b4334 -> sub_fffffe0009a54b54 : 344 -> 352

```
