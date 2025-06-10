## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-683.120.3.0.0
+704.0.0.0.0
   __TEXT.__const: 0x1b18
   __TEXT.__cstring: 0xa072
-  __TEXT_EXEC.__text: 0x51cc4
+  __TEXT_EXEC.__text: 0x52ad4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__const: 0xf50
   __DATA_CONST.__kalloc_type: 0x3340
   __DATA_CONST.__kalloc_var: 0x690
-  UUID: 3B885E39-8E9C-3546-AE91-80A12171935D
+  UUID: E058EE4E-1120-3215-A3D7-06AF20EFC4BB
   Functions: 531
   Symbols:   0
   CStrings:  865
Functions:
~ _hfs_extendfs : 2468 -> 2472
~ _hfs_vnop_readdir : 3076 -> 3180
~ sub_fffffff009efed38 -> sub_fffffff00a2aa7e4 : 172 -> 196
~ sub_fffffff009efede4 -> sub_fffffff00a2aa8a8 : 1064 -> 1080
~ sub_fffffff009eff730 -> sub_fffffff00a2ab204 : 2576 -> 2604
~ _hfs_vnop_renamex : 5268 -> 5248
~ sub_fffffff009f04c3c -> sub_fffffff00a2b0718 : 2536 -> 2544
~ sub_fffffff009f05bc0 -> sub_fffffff00a2b16a4 : 1008 -> 1004
~ _SetBTreeBlockSize : 196 -> 192
~ sub_fffffff009f07cd0 -> sub_fffffff00a2b37ac : 424 -> 488
~ sub_fffffff009f07e78 -> sub_fffffff00a2b3994 : 300 -> 412
~ sub_fffffff009f08058 -> sub_fffffff00a2b3be4 : 136 -> 168
~ sub_fffffff009f084f4 -> sub_fffffff00a2b40a0 : 824 -> 856
~ _BTIterateRecord : 1784 -> 1816
~ _BTIterateRecords : 1916 -> 1948
~ sub_fffffff009f09d78 -> sub_fffffff00a2b5984 : 848 -> 880
~ _do_journal_io : 732 -> 748
~ _size_up_tbuffer : 360 -> 356
~ _replay_journal : 4632 -> 4840
~ _insert_block : 616 -> 708
~ _end_transaction : 1852 -> 1868
~ _finish_end_transaction : 2404 -> 2432
~ _journal_modify_block_start : 1600 -> 1632
~ _journal_modify_block_end : 1816 -> 1836
~ _trim_remove_extent : 416 -> 540
~ sub_fffffff009f12ac0 -> sub_fffffff00a2be900 : 132 -> 156
~ sub_fffffff009f12ba8 -> sub_fffffff00a2bea00 : 72 -> 92
~ sub_fffffff009f12d48 -> sub_fffffff00a2bebb4 : 180 -> 200
~ _hfs_chash_getvnode : 312 -> 336
~ sub_fffffff009f12f98 -> sub_fffffff00a2bee30 : 200 -> 224
~ sub_fffffff009f130cc -> sub_fffffff00a2bef7c : 384 -> 424
~ _xattr_fext_alloc : 200 -> 220
~ _hfs_setxattr_internal : 2392 -> 2412
~ sub_fffffff009f16820 -> sub_fffffff00a2c2720 : 468 -> 460
~ sub_fffffff009f16e68 -> sub_fffffff00a2c2d60 : 788 -> 784
~ sub_fffffff009f1742c -> sub_fffffff00a2c3320 : 648 -> 644
~ sub_fffffff009f176b4 -> sub_fffffff00a2c35a4 : 4576 -> 4568
~ _hfs_flush_invalid_ranges : 1020 -> 1004
~ sub_fffffff009f18db8 -> sub_fffffff00a2c4c90 : 152 -> 148
~ _MoveExtents : 1140 -> 1132
~ sub_fffffff009f19b60 -> sub_fffffff00a2c5a2c : 360 -> 388
~ sub_fffffff009f19e00 -> sub_fffffff00a2c5ce8 : 3464 -> 3716
~ sub_fffffff009f1ace4 -> sub_fffffff00a2c6cc8 : 712 -> 752
~ _hfs_swap_BTNode : 4884 -> 5092
~ sub_fffffff009f1c3c0 -> sub_fffffff00a2c849c : 184 -> 180
~ sub_fffffff009f1c478 -> sub_fffffff00a2c8550 : 556 -> 552
~ sub_fffffff009f1cf74 -> sub_fffffff00a2c9048 : 376 -> 372
~ sub_fffffff009f1ecbc -> sub_fffffff00a2cad8c : 2168 -> 2224
~ _hfs_zero_eof_page : 324 -> 320
~ _hfs_ubc_setsize : 224 -> 220
~ _hfs_vnop_ioctl : 11616 -> 12068
~ sub_fffffff009f22ff8 -> sub_fffffff00a2cf2bc : 132 -> 180
~ _hfs_vnop_blockmap : 1812 -> 1836
~ sub_fffffff009f23ed8 -> sub_fffffff00a2d01e4 : 856 -> 852
~ _hfs_flush_invalid_ranges -> sub_fffffff00a2d223c : 700 -> 696
~ _ReplaceBTreeRecord : 376 -> 372
~ sub_fffffff009f26774 -> sub_fffffff00a2d2a74 : 536 -> 560
~ _catrec_update : 1240 -> 1184
~ sub_fffffff009f294d8 -> sub_fffffff00a2d57b8 : 500 -> 524
~ sub_fffffff009f29da4 -> sub_fffffff00a2d609c : 584 -> 600
~ sub_fffffff009f2a08c -> sub_fffffff00a2d6394 : 1688 -> 1752
~ _hfc_btree_create : 1436 -> 1532
~ _hfs_setup_default_cf_hotfiles : 532 -> 548
~ _hfs_vnop_lookup : 2004 -> 2012
~ _hfs_flushvolumeheader : 2820 -> 2808
~ sub_fffffff009f2eeb4 -> sub_fffffff00a2db268 : 140 -> 164
~ _hfs_sync : 7332 -> 7340
~ _hfs_unmount : 1252 -> 1272
~ _hfs_mount : 3568 -> 3604
~ sub_fffffff009f34c58 -> sub_fffffff00a2e1064 : 568 -> 592
~ sub_fffffff009f34e90 -> sub_fffffff00a2e12b4 : 464 -> 496
~ sub_fffffff009f35194 -> sub_fffffff00a2e15d8 : 1104 -> 1120
~ _remove_free_extent_list : 132 -> 176
~ sub_fffffff009f358e0 -> sub_fffffff00a2e1d60 : 228 -> 292
~ _ScanUnmapBlocks : 1208 -> 1228
~ sub_fffffff009f36054 -> sub_fffffff00a2e2528 : 92 -> 140
~ _process_reservations : 744 -> 740
~ _hfs_release_reserved : 420 -> 440
~ _BlockAllocate : 3444 -> 3440
~ _BlockFindContiguous : 1948 -> 1944
~ sub_fffffff009f37f18 -> sub_fffffff00a2e4424 : 776 -> 816
~ _BlockMarkAllocatedInternal : 2448 -> 2468
~ sub_fffffff009f390b0 -> sub_fffffff00a2e55f8 : 432 -> 428
~ _BlockMarkFreeInternal : 2920 -> 3048
~ _get_more_bits : 540 -> 536
~ _hfs_unlock_truncate : 332 -> 328
~ _hfs_getnewvnode : 3160 -> 3204
~ sub_fffffff009f3d1a8 -> sub_fffffff00a2e9790 : 584 -> 600
~ sub_fffffff009f3dde0 -> sub_fffffff00a2ea3d8 : 788 -> 884
~ sub_fffffff009f3f6dc -> sub_fffffff00a2ebd34 : 380 -> 428
~ _MapFileBlockC : 376 -> 396
~ sub_fffffff009f3ff20 -> sub_fffffff00a2ec5bc : 408 -> 480
~ sub_fffffff009f40560 -> sub_fffffff00a2ecc44 : 1852 -> 1940
~ sub_fffffff009f40c9c -> sub_fffffff00a2ed3d8 : 720 -> 796
~ sub_fffffff009f41748 -> sub_fffffff00a2eded0 : 600 -> 620
~ _hfs_MountHFSPlusVolume : 4520 -> 4536
~ _hfs_end_transaction : 292 -> 288
~ _GetLogicalBlockSize : 304 -> 300
~ sub_fffffff009f45d78 -> sub_fffffff00a2f251c : 76 -> 96
~ sub_fffffff009f45eb4 -> sub_fffffff00a2f266c : 88 -> 108
~ _hfs_readdirattr_internal : 7680 -> 7688
~ sub_fffffff009f48ca8 -> sub_fffffff00a2f547c : 100 -> 116
~ sub_fffffff009f49380 -> sub_fffffff00a2f5b64 : 444 -> 488
~ sub_fffffff009f4b19c -> sub_fffffff00a2f79ac : 940 -> 1004

```
