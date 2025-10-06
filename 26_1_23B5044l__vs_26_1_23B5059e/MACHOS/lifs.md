## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-737.40.5.0.0
-  __TEXT.__os_log: 0x13b7
-  __TEXT.__cstring: 0x2220
+737.40.13.0.0
+  __TEXT.__os_log: 0x13e3
+  __TEXT.__cstring: 0x2226
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1ba50
-  __TEXT_EXEC.__auth_stubs: 0xfd0
+  __TEXT_EXEC.__text: 0x1bad0
+  __TEXT_EXEC.__auth_stubs: 0xff0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7e8
+  __DATA_CONST.__auth_got: 0x7f8
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18

   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 59DB1B21-2C6B-3F23-AFF0-6A021A77D104
+  UUID: F04893FC-E8F8-32DF-87DA-8F32CD933341
   Functions: 406
-  Symbols:   3082
-  CStrings:  402
+  Symbols:   3086
+  CStrings:  403
 
Symbols:
+ ___strncpy_chk
+ _memchr
+ add_sillyrename_entry.kalloc_type_view_1954
+ add_sillyrename_entry.kalloc_type_view_1977
+ cleanup_sillyrename_entries.kalloc_type_view_2067
+ lifs_fsync_internal.kalloc_type_view_3796
+ lifs_koio_done.kalloc_type_view_2096
+ lifs_pack_attrlist_entry._os_log_fmt.29
+ lifs_reclaim_done.kalloc_type_view_4708
+ lifs_setfsattr_done.kalloc_type_view_3724
+ lifs_submit_io.kalloc_type_view_2077
+ lifs_submit_koio.kalloc_type_view_2118
+ lifs_vnop_readdir.kalloc_type_view_2912
+ lifs_vnop_readdir.kalloc_type_view_2914
+ lifs_vnop_readdir.kalloc_type_view_3009
+ lifs_vnop_readdir.kalloc_type_view_3011
+ lifs_vnop_reclaim.kalloc_type_view_4752
+ lifs_vnop_reclaim.kalloc_type_view_4806
+ lifs_vnop_strategy.kalloc_type_view_2175
+ lifs_vnop_strategy_done.kalloc_type_view_1942
+ move_sillyrename_entries.kalloc_type_view_2041
- add_sillyrename_entry.kalloc_type_view_1944
- add_sillyrename_entry.kalloc_type_view_1967
- cleanup_sillyrename_entries.kalloc_type_view_2057
- lifs_fsync_internal.kalloc_type_view_3788
- lifs_koio_done.kalloc_type_view_2088
- lifs_reclaim_done.kalloc_type_view_4700
- lifs_setfsattr_done.kalloc_type_view_3716
- lifs_submit_io.kalloc_type_view_2069
- lifs_submit_koio.kalloc_type_view_2110
- lifs_vnop_readdir.kalloc_type_view_2904
- lifs_vnop_readdir.kalloc_type_view_2906
- lifs_vnop_readdir.kalloc_type_view_3001
- lifs_vnop_readdir.kalloc_type_view_3003
- lifs_vnop_reclaim.kalloc_type_view_4744
- lifs_vnop_reclaim.kalloc_type_view_4798
- lifs_vnop_strategy.kalloc_type_view_2167
- lifs_vnop_strategy_done.kalloc_type_view_1947
- move_sillyrename_entries.kalloc_type_view_2031
Functions:
~ _lifs_submit_io : 744 -> 776
~ _lifs_vnop_strategy_done : 704 -> 680
~ _lifs_pack_attrlist_entry : 492 -> 612
CStrings:
+ "\"%s: lnode %p vp %p async_io_inflights (%d) < 0\" @%s:%d"
+ "Skipping directory entry contains '/': %.*s"
- "\"%s: lnode %p async_io_inflights (%d) < 0\" @%s:%d"

```
