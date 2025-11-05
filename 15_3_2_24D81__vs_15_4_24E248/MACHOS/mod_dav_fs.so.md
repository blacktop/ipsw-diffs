## mod_dav_fs.so

> `/usr/libexec/apache2/mod_dav_fs.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x9678
+880.0.0.0.0
+  __TEXT.__text: 0x8908
   __TEXT.__auth_stubs: 0x680
   __TEXT.__cstring: 0x1447
   __TEXT.__const: 0xd9
-  __TEXT.__unwind_info: 0xa4
+  __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x310

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: EDDCBE5E-08C8-3AC6-9DB7-05A51E39CF31
+  UUID: CA9D0368-D3CC-3DB7-A20E-7FFFD7F46E57
   Functions: 102
   Symbols:   207
   CStrings:  117
Functions:
~ _dav_fs_merge_server_config : 160 -> 144
~ _dav_fs_cmd_davlockdb : 184 -> 176
~ _dav_dbm_get_statefiles : 100 -> 92
~ _dav_fs_ensure_state_dir : 96 -> 92
~ _dav_dbm_open_direct : 288 -> 248
~ _dav_fs_dbm_error : 504 -> 452
~ _dav_dbm_fetch : 144 -> 136
~ _dav_dbm_store : 100 -> 96
~ _dav_dbm_delete : 84 -> 80
~ _dav_propdb_open : 788 -> 728
~ _dav_propdb_close : 424 -> 384
~ _dav_propdb_define_namespaces : 252 -> 232
~ _dav_propdb_output_value : 244 -> 224
~ _dav_propdb_map_namespaces : 524 -> 500
~ _dav_propdb_first_name : 188 -> 164
~ _dav_propdb_next_name : 236 -> 204
~ _dav_propdb_get_rollback : 312 -> 292
~ _dav_propdb_apply_rollback : 160 -> 144
~ _dav_dbm_open : 240 -> 224
~ _dav_build_key : 468 -> 440
~ _dav_append_prop : 808 -> 776
~ _dav_dbm_firstkey : 76 -> 72
~ _dav_set_name : 272 -> 248
~ _dav_get_ns_table_uri : 120 -> 108
~ _dav_dbm_nextkey : 76 -> 72
~ _dav_fs_load_locknull_list : 748 -> 704
~ _dav_fs_parse_locktoken : 240 -> 228
~ _dav_fs_format_locktoken : 148 -> 144
~ _dav_fs_open_lockdb : 308 -> 292
~ _dav_fs_close_lockdb : 80 -> 72
~ _dav_fs_remove_locknull_state : 160 -> 140
~ _dav_fs_create_lock : 156 -> 152
~ _dav_fs_get_locks : 812 -> 744
~ _dav_fs_find_lock : 864 -> 792
~ _dav_fs_has_locks : 220 -> 200
~ _dav_fs_append_locks : 884 -> 804
~ _dav_fs_remove_lock : 752 -> 620
~ _dav_fs_refresh_locks : 972 -> 872
~ _dav_fs_really_open_lockdb : 216 -> 200
~ _dav_fs_remove_locknull_member : 548 -> 480
~ _dav_fs_save_locknull_list : 696 -> 632
~ _dav_fs_build_key : 204 -> 196
~ _dav_fs_alloc_lock : 204 -> 196
~ _dav_fs_load_lock_record : 1776 -> 1640
~ _dav_fs_resolve : 328 -> 292
~ _dav_fs_lock_expired : 96 -> 88
~ _dav_fs_save_lock_record : 1328 -> 1208
~ _dav_fs_add_locknull_state : 300 -> 272
~ _dav_fs_do_refresh : 160 -> 140
~ _dav_fs_dir_file_name : 564 -> 476
~ _dav_fs_find_liveprop : 120 -> 116
~ _dav_fs_insert_all_liveprops : 212 -> 200
~ _dav_fs_insert_prop : 944 -> 868
~ _dav_fs_get_resource : 888 -> 816
~ _dav_fs_get_parent_resource : 872 -> 792
~ _dav_fs_is_same_resource : 272 -> 228
~ _dav_fs_is_parent_resource : 280 -> 252
~ _dav_fs_open_stream : 1260 -> 1136
~ _dav_fs_close_stream : 408 -> 360
~ _dav_fs_write_stream : 228 -> 212
~ _dav_fs_seek_stream : 132 -> 124
~ _dav_fs_create_collection : 320 -> 296
~ _dav_fs_copy_resource : 220 -> 204
~ _dav_fs_move_resource : 660 -> 604
~ _dav_fs_remove_resource : 440 -> 392
~ _dav_fs_getetag : 208 -> 188
~ _dav_fs_mktemp : 312 -> 292
~ _tmpfile_cleanup : 96 -> 84
~ _dav_fs_copymove_resource : 596 -> 532
~ _dav_fs_copymove_walker : 596 -> 520
~ _dav_fs_internal_walk : 720 -> 684
~ _dav_fs_copymove_file : 1492 -> 1312
~ _dav_fs_copymoveset : 504 -> 448
~ _dav_fs_walker : 2684 -> 2344
~ _dav_fs_copymove_state : 824 -> 764
~ _dav_fs_delete_walker : 276 -> 236
~ _dav_fs_deleteset : 420 -> 388
~ _dav_fs_is_writable : 136 -> 124
~ _dav_fs_patch_validate : 624 -> 560
~ _dav_fs_patch_exec : 332 -> 300
~ _dav_fs_patch_rollback : 244 -> 216
~ _dav_format_time : 336 -> 324
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/fs/dbm.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/fs/mod_dav_fs.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/fs/repos.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/fs/dbm.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/fs/mod_dav_fs.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/dav/fs/repos.c"

```
