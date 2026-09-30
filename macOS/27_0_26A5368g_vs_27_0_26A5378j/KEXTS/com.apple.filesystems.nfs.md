## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

```diff

   __TEXT.__cstring: 0x9c08
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9df48
+  __TEXT_EXEC.__text: 0x9df5c
   __TEXT_EXEC.__auth_stubs: 0x1530
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ _nfs4_id2guid : 1240 -> 1228
~ _nfs4_guid2id : 1204 -> 1216
~ _nfsstat_update_nfserror : 264 -> 288
~ _nfs_dir_buf_search : 744 -> 752
~ _nfs_locks_init : 252 -> 264
~ _nfs_vfs_mount : 4752 -> 4772
~ _nfs_get_volname : 372 -> 360
~ _nfs4_mount_update_path_with_symlink : 3580 -> 3576
~ _nfs_mirror_mount_domount : 8932 -> 8904

```
