## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-343.160.2.0.0
-  __TEXT.__cstring: 0x9c08
+343.160.4.0.0
+  __TEXT.__cstring: 0x9c42
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9d26c
+  __TEXT_EXEC.__text: 0x9d2a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4

   __DATA_CONST.__kalloc_var: 0x320
   Functions: 1002
   Symbols:   1760
-  CStrings:  1155
+  CStrings:  1156
 
Symbols:
+ mountnfs.kalloc_type_view_2989
+ mountnfs.kalloc_type_view_2998
+ mountnfs.kalloc_type_view_3007
+ mountnfs.kalloc_type_view_3017
+ mountnfs.kalloc_type_view_3040
+ nfs3_vnop_create.kalloc_type_view_4516
+ nfs3_vnop_create.kalloc_type_view_4644
+ nfs3_vnop_mkdir.kalloc_type_view_5624
+ nfs3_vnop_mkdir.kalloc_type_view_5738
+ nfs3_vnop_rmdir.kalloc_type_view_5795
+ nfs3_vnop_rmdir.kalloc_type_view_5871
+ nfs3_vnop_symlink.kalloc_type_view_5435
+ nfs3_vnop_symlink.kalloc_type_view_5555
+ nfs4_init_clientid.kalloc_type_view_124
+ nfs4_init_clientid.kalloc_type_view_138
+ nfs4_parsefattr.kalloc_type_view_1929
+ nfs4_parsefattr.kalloc_type_view_2249
+ nfs4_parsefattr.kalloc_type_view_2259
+ nfs4_parsefattr.kalloc_type_view_2271
+ nfs4_parsefattr.kalloc_type_view_2279
+ nfs4_parsefattr.kalloc_type_view_2300
+ nfs4_parsefattr.kalloc_type_view_2755
+ nfs4_remove_clientid.kalloc_type_view_441
+ nfs_fs_locations_cleanup.kalloc_type_view_4712
+ nfs_fs_locations_cleanup.kalloc_type_view_4715
+ nfs_fs_locations_cleanup.kalloc_type_view_4717
+ nfs_fs_locations_cleanup.kalloc_type_view_4720
+ nfs_fs_locations_cleanup.kalloc_type_view_4722
+ nfs_mount_cleanup.kalloc_type_view_5023
+ nfs_sillyrename.kalloc_type_view_7058
+ nfs_sillyrename.kalloc_type_view_7117
+ nfs_vnop_inactive.kalloc_type_view_692
+ nfs_vnop_inactive.kalloc_type_view_967
+ nfs_vnop_inactive.kalloc_type_view_969
+ nfs_vnop_reclaim.kalloc_type_view_1155
+ nfs_vnop_remove.kalloc_type_view_4701
+ nfs_vnop_remove.kalloc_type_view_4897
+ nfs_vnop_setattr.kalloc_type_view_2429
+ nfs_vnop_setattr.kalloc_type_view_2473
- mountnfs.kalloc_type_view_2988
- mountnfs.kalloc_type_view_2997
- mountnfs.kalloc_type_view_3006
- mountnfs.kalloc_type_view_3016
- mountnfs.kalloc_type_view_3039
- nfs3_vnop_create.kalloc_type_view_4513
- nfs3_vnop_create.kalloc_type_view_4641
- nfs3_vnop_mkdir.kalloc_type_view_5621
- nfs3_vnop_mkdir.kalloc_type_view_5735
- nfs3_vnop_rmdir.kalloc_type_view_5792
- nfs3_vnop_rmdir.kalloc_type_view_5868
- nfs3_vnop_symlink.kalloc_type_view_5432
- nfs3_vnop_symlink.kalloc_type_view_5552
- nfs4_init_clientid.kalloc_type_view_123
- nfs4_init_clientid.kalloc_type_view_137
- nfs4_parsefattr.kalloc_type_view_1918
- nfs4_parsefattr.kalloc_type_view_2238
- nfs4_parsefattr.kalloc_type_view_2248
- nfs4_parsefattr.kalloc_type_view_2260
- nfs4_parsefattr.kalloc_type_view_2268
- nfs4_parsefattr.kalloc_type_view_2289
- nfs4_parsefattr.kalloc_type_view_2744
- nfs4_remove_clientid.kalloc_type_view_440
- nfs_fs_locations_cleanup.kalloc_type_view_4711
- nfs_fs_locations_cleanup.kalloc_type_view_4714
- nfs_fs_locations_cleanup.kalloc_type_view_4716
- nfs_fs_locations_cleanup.kalloc_type_view_4719
- nfs_fs_locations_cleanup.kalloc_type_view_4721
- nfs_mount_cleanup.kalloc_type_view_5022
- nfs_sillyrename.kalloc_type_view_7055
- nfs_sillyrename.kalloc_type_view_7114
- nfs_vnop_inactive.kalloc_type_view_666
- nfs_vnop_inactive.kalloc_type_view_941
- nfs_vnop_inactive.kalloc_type_view_943
- nfs_vnop_reclaim.kalloc_type_view_1129
- nfs_vnop_remove.kalloc_type_view_4698
- nfs_vnop_remove.kalloc_type_view_4894
- nfs_vnop_setattr.kalloc_type_view_2426
- nfs_vnop_setattr.kalloc_type_view_2470
Functions:
~ _nfs4_mount : 13228 -> 13280
CStrings:
+ "nfs: warning: 'namedattr' not supported by server for %s\n"
```
