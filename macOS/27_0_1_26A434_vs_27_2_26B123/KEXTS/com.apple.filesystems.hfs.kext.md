## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-751.0.0.0.0
+753.41.1.0.0
   __TEXT.__const: 0x1ab0
-  __TEXT.__cstring: 0xaba4
-  __TEXT_EXEC.__text: 0x4f038
+  __TEXT.__cstring: 0xac58
+  __TEXT_EXEC.__text: 0x4f3bc
   __TEXT_EXEC.__auth_stubs: 0x1850
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 510
   Symbols:   1569
-  CStrings:  869
+  CStrings:  872
 
Symbols:
+ file_attribute_exist.kalloc_type_view_1744
+ file_attribute_exist.kalloc_type_view_1770
+ hfs_mountfs.kalloc_type_view_1283
+ hfs_mountfs.kalloc_type_view_1894
+ hfs_removeallattr.kalloc_type_view_2128
+ hfs_removeallattr.kalloc_type_view_2169
+ hfs_set_volxattr.kalloc_type_view_2228
+ hfs_set_volxattr.kalloc_type_view_2289
+ hfs_setxattr_internal.kalloc_type_view_1152
+ hfs_setxattr_internal.kalloc_type_view_1419
+ hfs_unmount.kalloc_type_view_2111
+ hfs_vnop_listxattr.kalloc_type_view_1975
+ hfs_vnop_listxattr.kalloc_type_view_2029
+ hfs_vnop_removexattr.kalloc_type_view_1608
+ hfs_vnop_removexattr.kalloc_type_view_1658
- file_attribute_exist.kalloc_type_view_1688
- file_attribute_exist.kalloc_type_view_1714
- hfs_mountfs.kalloc_type_view_1272
- hfs_mountfs.kalloc_type_view_1883
- hfs_removeallattr.kalloc_type_view_2072
- hfs_removeallattr.kalloc_type_view_2113
- hfs_set_volxattr.kalloc_type_view_2172
- hfs_set_volxattr.kalloc_type_view_2233
- hfs_setxattr_internal.kalloc_type_view_1151
- hfs_setxattr_internal.kalloc_type_view_1363
- hfs_unmount.kalloc_type_view_2100
- hfs_vnop_listxattr.kalloc_type_view_1919
- hfs_vnop_listxattr.kalloc_type_view_1973
- hfs_vnop_removexattr.kalloc_type_view_1552
- hfs_vnop_removexattr.kalloc_type_view_1602
Functions:
~ _DeleteRecord : 400 -> 420
~ _hfs_setxattr_internal : 2476 -> 3024
~ _hfs_swap_BTNode : 5376 -> 5648
~ _hfs_vnop_ioctl : 9776 -> 9800
~ _hfs_mount : 3604 -> 3620
~ _RotateLeft : 888 -> 896
~ _VerifyHeader : 216 -> 228
CStrings:
+ "\"hfs_UNswap_BTNode: initial record at bad offset (0x%04X)\\n\" @%s:%d"
+ "hfs_setxattr: orphan overflow attr record vol=%s %d,%s\n"
+ "hfs_swap_BTNode: initial record at bad offset (0x%04X)\n"
```
