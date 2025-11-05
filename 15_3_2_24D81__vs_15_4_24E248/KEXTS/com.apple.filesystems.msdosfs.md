## com.apple.filesystems.msdosfs

> `com.apple.filesystems.msdosfs`

```diff

-720.80.2.0.0
-  __TEXT.__const: 0x308
+747.100.27.0.0
+  __TEXT.__const: 0x318
   __TEXT.__cstring: 0xe40
-  __TEXT_EXEC.__text: 0xc3e0
+  __TEXT_EXEC.__text: 0xc61c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x600
   __DATA.__common: 0x28

   __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 27723DEC-3E51-36F3-8F53-70B2FFB4FD81
+  UUID: 270CA111-91B4-3278-8A56-45A4625EEF5A
   Functions: 138
   Symbols:   357
   CStrings:  79
Functions:
~ _msdosfs_dos2unixtime : 240 -> 244
~ _msdosfs_unicode2dos : 324 -> 328
~ _msdosfs_dos2unicodefn : 288 -> 324
~ _msdosfs_unicode_to_dos_name : 936 -> 964
~ _msdosfs_apply_generation_to_short_name : 192 -> 204
~ _msdosfs_unicode2winfn : 224 -> 240
~ _msdosfs_winChkName : 472 -> 516
~ _msdosfs_getunicodefn : 312 -> 288
~ _msdosfs_hash_get : 376 -> 368
~ _msdosfs_hash_remove : 32 -> 24
~ _msdosfs_hash_insert : 76 -> 96
~ _msdosfs_deget : 1400 -> 1444
~ _msdosfs_deupdat : 656 -> 660
~ _msdosfs_hash_reinsert : 156 -> 168
~ _msdosfs_vnop_reclaim : 284 -> 276
~ _msdosfs_fat_cache_flush : 460 -> 464
~ _msdosfs_fat_init_vol : 560 -> 556
~ _msdosfs_count_free_clusters : 448 -> 468
~ _msdosfs_update_fsinfo : 368 -> 372
~ _msdosfs_fatchain : 464 -> 492
~ _msdosfs_chainlength : 412 -> 436
~ _msdosfs_find_next_free : 480 -> 504
~ _msdosfs_insert_free_extent : 232 -> 252
~ _msdosfs_find_free_extents : 420 -> 428
~ _msdosfs_extendfile : 1340 -> 1364
~ _msdosfs_unicode_to_dos_lookup : 388 -> 400
~ _msdosfs_lookup_name : 1020 -> 988
~ _msdosfs_createde : 1140 -> 1192
~ _msdosfs_doscheckpath : 368 -> 364
~ _msdosfs_readep : 496 -> 500
~ _msdosfs_dir_flush : 228 -> 236
~ _msdosfs_vfs_mount : 580 -> 572
~ _msdosfs_vfs_unmount : 400 -> 404
~ _msdosfs_scan_root_dir : 1000 -> 1016
~ _msdosfs_vfs_getattr : 468 -> 472
~ _msdosfs_vfs_setattr : 816 -> 920
~ _msdosfs_flush_thread : 184 -> 216
~ _msdosfs_sort_denodes : 116 -> 108
~ _msdosfs_lock_four : 132 -> 136
~ _msdosfs_unlock_four : 132 -> 136
~ _msdosfs_vnop_create : 900 -> 920
~ _msdosfs_vnop_getattr : 664 -> 660
~ _msdosfs_vnop_getxattr : 180 -> 184
~ _msdosfs_vnop_listxattr : 140 -> 144
~ _msdosfs_vnop_read : 764 -> 768
~ _msdosfs_vnop_write : 932 -> 892
~ _msdosfs_vnop_rename : 1624 -> 1620
~ _msdosfs_vnop_mkdir : 1204 -> 1212
~ _msdosfs_vnop_readdir : 1764 -> 1780
~ _msdosfs_vnop_blktooff : 204 -> 212
~ _msdosfs_vnop_offtoblk : 204 -> 212
~ _msdosfs_md5_digest : 216 -> 220
~ _msdosfs_check_link : 508 -> 512
~ _msdosfs_vnop_symlink : 1316 -> 1332
~ _msdosfs_vnop_ioctl : 260 -> 264

```
