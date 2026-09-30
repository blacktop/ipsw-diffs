## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-715.120.1.0.0
+715.120.4.0.0
   __TEXT.__const: 0x1b50
-  __TEXT.__cstring: 0xa3e4
-  __TEXT_EXEC.__text: 0x52114
+  __TEXT.__cstring: 0xa4a4
+  __TEXT_EXEC.__text: 0x52170
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__const: 0xf50
   __DATA_CONST.__kalloc_type: 0x3340
   __DATA_CONST.__kalloc_var: 0x690
-  UUID: 5F2F021F-B606-3910-AB7F-41009F9E6561
+  UUID: 97B7A84D-281B-30A8-94A8-CB603175D1D1
   Functions: 532
   Symbols:   0
-  CStrings:  865
+  CStrings:  869
 
Functions:
~ _replay_journal : 4644 -> 4628
~ _hfs_getxattr_internal : 1504 -> 1524
~ _hfs_setxattr_internal : 2328 -> 2408
~ _remove_attribute_records : 704 -> 688
~ sub_fffffe0009a67058 -> sub_fffffe00099cc49c : 384 -> 408
CStrings:
+ "hfs_getxattr: %s has a malformed attr extent\n"
+ "hfs_getxattr: %s has a malformed overflow extent\n"
+ "hfs_setxattr: %s has a malformed attr extent\n"
+ "hfs_setxattr: %s has a malformed overflow extent\n"

```
