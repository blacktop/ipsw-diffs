## livefiles_ntfs.dylib

> `/System/Library/Filesystems/ntfs.fs/Contents/Resources/livefiles_ntfs.dylib`

```diff

-  __TEXT.__text: 0x41da0
+  __TEXT.__text: 0x41d60
   __TEXT.__const: 0xdd0
   __TEXT.__cstring: 0x13963
   __TEXT.__oslogstring: 0x108c
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _ntfs_read_compressed : 3576 -> 3544
~ _ntfs_rl_find_vcn_nolock : 124 -> 108
~ _ntfs_get_size_for_mapping_pairs : 792 -> 772
~ _ntfs_mapping_pairs_build : 1140 -> 1116
~ _ntfs_rl_truncate_nolock : 564 -> 556
~ _ntfs_rl_punch_nolock : 1116 -> 1160
~ _ntfs_attr_find_vcn_nolock : 372 -> 368
~ _ntfs_attr_find_in_attrdef : 120 -> 100
~ _ntfs_attr_extend_initialized : 2236 -> 2212
~ _ntfs_cluster_free_from_rl_nolock : 604 -> 608
~ _ntfs_extent_mft_record_free : 732 -> 740
~ _ntfs_mst_fixup_post_read : 164 -> 160
~ _vfs_fsadd : 1692 -> 1716
~ _ntfs_inode_reclaim : 1032 -> 1040

```
