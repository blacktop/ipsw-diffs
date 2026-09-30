## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-356.0.3.0.0
-  __TEXT.__cstring: 0x9c08
+356.0.5.0.0
+  __TEXT.__cstring: 0x9c42
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9df5c
+  __TEXT_EXEC.__text: 0x9df90
   __TEXT_EXEC.__auth_stubs: 0x1530
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 1003
   Symbols:   1762
-  CStrings:  1155
+  CStrings:  1156
 
Symbols:
+ mountnfs.kalloc_type_view_3001
+ mountnfs.kalloc_type_view_3010
+ mountnfs.kalloc_type_view_3019
+ mountnfs.kalloc_type_view_3029
+ mountnfs.kalloc_type_view_3052
+ nfs3_vnop_create.kalloc_type_view_4528
+ nfs3_vnop_create.kalloc_type_view_4656
+ nfs3_vnop_mkdir.kalloc_type_view_5636
+ nfs3_vnop_mkdir.kalloc_type_view_5750
+ nfs3_vnop_rmdir.kalloc_type_view_5807
+ nfs3_vnop_rmdir.kalloc_type_view_5883
+ nfs3_vnop_symlink.kalloc_type_view_5447
+ nfs3_vnop_symlink.kalloc_type_view_5567
+ nfs4_init_clientid.kalloc_type_view_124
+ nfs4_init_clientid.kalloc_type_view_138
+ nfs4_parsefattr.kalloc_type_view_1929
+ nfs4_parsefattr.kalloc_type_view_2249
+ nfs4_parsefattr.kalloc_type_view_2259
+ nfs4_parsefattr.kalloc_type_view_2271
+ nfs4_parsefattr.kalloc_type_view_2279
+ nfs4_parsefattr.kalloc_type_view_2300
+ nfs4_parsefattr.kalloc_type_view_2756
+ nfs4_remove_clientid.kalloc_type_view_441
+ nfs_fs_locations_cleanup.kalloc_type_view_4724
+ nfs_fs_locations_cleanup.kalloc_type_view_4727
+ nfs_fs_locations_cleanup.kalloc_type_view_4729
+ nfs_fs_locations_cleanup.kalloc_type_view_4732
+ nfs_fs_locations_cleanup.kalloc_type_view_4734
+ nfs_mount_cleanup.kalloc_type_view_5035
+ nfs_sillyrename.kalloc_type_view_7070
+ nfs_sillyrename.kalloc_type_view_7129
+ nfs_vnop_inactive.kalloc_type_view_701
+ nfs_vnop_inactive.kalloc_type_view_976
+ nfs_vnop_inactive.kalloc_type_view_978
+ nfs_vnop_reclaim.kalloc_type_view_1164
+ nfs_vnop_remove.kalloc_type_view_4713
+ nfs_vnop_remove.kalloc_type_view_4909
+ nfs_vnop_setattr.kalloc_type_view_2435
+ nfs_vnop_setattr.kalloc_type_view_2479
- mountnfs.kalloc_type_view_3000
- mountnfs.kalloc_type_view_3009
- mountnfs.kalloc_type_view_3018
- mountnfs.kalloc_type_view_3028
- mountnfs.kalloc_type_view_3051
- nfs3_vnop_create.kalloc_type_view_4525
- nfs3_vnop_create.kalloc_type_view_4653
- nfs3_vnop_mkdir.kalloc_type_view_5633
- nfs3_vnop_mkdir.kalloc_type_view_5747
- nfs3_vnop_rmdir.kalloc_type_view_5804
- nfs3_vnop_rmdir.kalloc_type_view_5880
- nfs3_vnop_symlink.kalloc_type_view_5444
- nfs3_vnop_symlink.kalloc_type_view_5564
- nfs4_init_clientid.kalloc_type_view_123
- nfs4_init_clientid.kalloc_type_view_137
- nfs4_parsefattr.kalloc_type_view_1918
- nfs4_parsefattr.kalloc_type_view_2238
- nfs4_parsefattr.kalloc_type_view_2248
- nfs4_parsefattr.kalloc_type_view_2260
- nfs4_parsefattr.kalloc_type_view_2268
- nfs4_parsefattr.kalloc_type_view_2289
- nfs4_parsefattr.kalloc_type_view_2745
- nfs4_remove_clientid.kalloc_type_view_440
- nfs_fs_locations_cleanup.kalloc_type_view_4723
- nfs_fs_locations_cleanup.kalloc_type_view_4726
- nfs_fs_locations_cleanup.kalloc_type_view_4728
- nfs_fs_locations_cleanup.kalloc_type_view_4731
- nfs_fs_locations_cleanup.kalloc_type_view_4733
- nfs_mount_cleanup.kalloc_type_view_5034
- nfs_sillyrename.kalloc_type_view_7067
- nfs_sillyrename.kalloc_type_view_7126
- nfs_vnop_inactive.kalloc_type_view_675
- nfs_vnop_inactive.kalloc_type_view_950
- nfs_vnop_inactive.kalloc_type_view_952
- nfs_vnop_reclaim.kalloc_type_view_1138
- nfs_vnop_remove.kalloc_type_view_4710
- nfs_vnop_remove.kalloc_type_view_4906
- nfs_vnop_setattr.kalloc_type_view_2432
- nfs_vnop_setattr.kalloc_type_view_2476
Functions:
~ _nfs4_mount : 13336 -> 13388
CStrings:
+ "nfs: warning: 'namedattr' not supported by server for %s\n"
```
