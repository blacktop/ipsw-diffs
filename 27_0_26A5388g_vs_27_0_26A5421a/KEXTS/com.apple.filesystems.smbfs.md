## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-579.0.10.0.0
+579.0.11.0.0
   __TEXT.__const: 0xc35
   __TEXT.__cstring: 0x5196
   __TEXT.__os_log: 0x1801a
-  __TEXT_EXEC.__text: 0x84048
+  __TEXT_EXEC.__text: 0x840c4
   __TEXT_EXEC.__auth_stubs: 0x1580
   __DATA.__data: 0x12d8
   __DATA.__bss: 0x107c
Symbols:
+ smbfs_do_strategy.kalloc_type_view_6773
+ smbfs_do_strategy.kalloc_type_view_6920
+ smbfs_vnop_advlock.kalloc_type_view_11050
+ smbfs_vnop_advlock.kalloc_type_view_11139
+ smbfs_vnop_getxattr.kalloc_type_view_12832
+ smbfs_vnop_getxattr.kalloc_type_view_12849
+ smbfs_vnop_rename.kalloc_type_view_9208
+ smbfs_vnop_strategy.kalloc_type_view_6966
- smbfs_do_strategy.kalloc_type_view_6762
- smbfs_do_strategy.kalloc_type_view_6909
- smbfs_vnop_advlock.kalloc_type_view_11039
- smbfs_vnop_advlock.kalloc_type_view_11128
- smbfs_vnop_getxattr.kalloc_type_view_12821
- smbfs_vnop_getxattr.kalloc_type_view_12838
- smbfs_vnop_rename.kalloc_type_view_9197
- smbfs_vnop_strategy.kalloc_type_view_6955
Functions:
~ _smbfs_set_data_size : 1228 -> 1260
~ _smb3_msg_decrypt : 1852 -> 1848
~ _smb_iod_destroy : 616 -> 640
~ _notify_main : 3048 -> 3120
CStrings:
+ "21122221111111222222221111222222222222222222222112221212222222222222222222222222222222222222222222222211122222222222222221222222222222222222221112222222222222222112112212221121122112222222222222222222222222222222222222222222"
+ "22222221221121221122222221111221212212212122122222221222222121222222222222222222222221212222221222212"
- "2112222111111122222222111122222222222222222222211222121222222222222222222222222222222222222222222222221112222222222222222122222222222222222122221112222222222222222112112212221121122112222222222222222222222222222222222222222222"
- "222222212211212211222222211112212122122121221222222212222221212222222222222222222222212122222212222"
```
