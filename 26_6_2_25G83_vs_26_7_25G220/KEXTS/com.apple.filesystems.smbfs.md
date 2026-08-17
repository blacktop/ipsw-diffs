## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

```diff

-538.161.2.0.0
+538.161.2.700.3
   __TEXT.__const: 0xc25
-  __TEXT.__cstring: 0x489f
-  __TEXT.__os_log: 0x16091
-  __TEXT_EXEC.__text: 0x7c8f8
+  __TEXT.__cstring: 0x48f3
+  __TEXT.__os_log: 0x164c1
+  __TEXT_EXEC.__text: 0x7d050
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdf8
   __DATA.__common: 0x24f0

   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x78
-  __DATA_CONST.__kalloc_type: 0x4d80
+  __DATA_CONST.__kalloc_type: 0x4dc0
   __DATA_CONST.__kalloc_var: 0x460
-  Functions: 765
-  Symbols:   2100
-  CStrings:  2507
+  Functions: 766
+  Symbols:   2102
+  CStrings:  2529
 
Symbols:
+ _smb_iod_lease_dequeue
+ nsmb_dev_load.kalloc_type_view_1862
+ smb1fs_smb_findclose.kalloc_type_view_5682
+ smb2_mc_add_new_interface_info_to_list.kalloc_type_view_1503
+ smb2_mc_parse_client_interface_array.kalloc_type_view_741
+ smb2_mc_query_info_response_event.kalloc_type_view_807
+ smb2_mc_query_info_response_event.kalloc_type_view_883
+ smb2_mc_release_connection_list.kalloc_type_view_1835
+ smb2_mc_release_interface.kalloc_type_view_1849
+ smb2_mc_release_interface.kalloc_type_view_1864
+ smb2_mc_remove_nic_if_unused.kalloc_type_view_995
+ smb2_mc_update_con_list.kalloc_type_view_1672
+ smb2_mc_update_info_with_ip.kalloc_type_view_2011
+ smb2_mc_update_info_with_ip.kalloc_type_view_2019
+ smb2_smb_lease_break_ack_queue.kalloc_type_view_3170
+ smb2_smb_read_uio.kalloc_type_view_9021
+ smb2_smb_read_uio.kalloc_type_view_9038
+ smb2_smb_read_write_async.kalloc_type_view_9190
+ smb2_smb_read_write_async.kalloc_type_view_9256
+ smb2_smb_read_write_async.kalloc_type_view_9584
+ smb2_smb_read_write_async.kalloc_type_view_9653
+ smb2_smb_write_uio.kalloc_type_view_10813
+ smb2_smb_write_uio.kalloc_type_view_10866
+ smb_iod_create.kalloc_type_view_4252
+ smb_iod_create.kalloc_type_view_4270
+ smb_iod_create.kalloc_type_view_4298
+ smb_iod_destroy.kalloc_type_view_4368
+ smb_iod_destroy.kalloc_type_view_4372
+ smb_iod_destroy.kalloc_type_view_4406
+ smb_iod_lease_dequeue.kalloc_type_view_4882
+ smb_iod_lease_enqueue.kalloc_type_view_4138
+ smb_rw_cleanup.kalloc_type_view_415
+ smb_rw_init.kalloc_type_view_276
+ smb_rw_thread.kalloc_type_view_208
+ smb_rw_thread.kalloc_type_view_226
+ smb_session_create.kalloc_type_view_577
+ smb_session_free.kalloc_type_view_484
+ smb_session_free.kalloc_type_view_510
+ smb_session_lease_thread.kalloc_type_view_2237
+ smb_share_create.kalloc_type_view_1499
+ smb_share_create.kalloc_type_view_1505
+ smb_share_free.kalloc_type_view_1460
+ smbfs_smb_findopen.kalloc_type_view_5945
+ smbfs_smb_reopen_file.kalloc_type_view_5032
+ smbfs_smb_reopen_file.kalloc_type_view_5108
- nsmb_dev_load.kalloc_type_view_1846
- smb1fs_smb_findclose.kalloc_type_view_5621
- smb2_mc_add_new_interface_info_to_list.kalloc_type_view_1483
- smb2_mc_parse_client_interface_array.kalloc_type_view_721
- smb2_mc_query_info_response_event.kalloc_type_view_787
- smb2_mc_query_info_response_event.kalloc_type_view_863
- smb2_mc_release_connection_list.kalloc_type_view_1815
- smb2_mc_release_interface.kalloc_type_view_1829
- smb2_mc_release_interface.kalloc_type_view_1844
- smb2_mc_remove_nic_if_unused.kalloc_type_view_975
- smb2_mc_update_con_list.kalloc_type_view_1652
- smb2_mc_update_info_with_ip.kalloc_type_view_1991
- smb2_mc_update_info_with_ip.kalloc_type_view_1999
- smb2_smb_lease_break_ack_queue.kalloc_type_view_3160
- smb2_smb_read_uio.kalloc_type_view_8913
- smb2_smb_read_uio.kalloc_type_view_8930
- smb2_smb_read_write_async.kalloc_type_view_9082
- smb2_smb_read_write_async.kalloc_type_view_9148
- smb2_smb_read_write_async.kalloc_type_view_9476
- smb2_smb_read_write_async.kalloc_type_view_9545
- smb2_smb_write_uio.kalloc_type_view_10705
- smb2_smb_write_uio.kalloc_type_view_10758
- smb_iod_create.kalloc_type_view_4230
- smb_iod_create.kalloc_type_view_4248
- smb_iod_create.kalloc_type_view_4276
- smb_iod_destroy.kalloc_type_view_4346
- smb_iod_destroy.kalloc_type_view_4350
- smb_iod_destroy.kalloc_type_view_4384
- smb_iod_lease_dequeue.kalloc_type_view_4836
- smb_iod_lease_enqueue.kalloc_type_view_4126
- smb_rw_init.kalloc_type_view_269
- smb_rw_thread.kalloc_type_view_201
- smb_rw_thread.kalloc_type_view_219
- smb_session_create.kalloc_type_view_575
- smb_session_free.kalloc_type_view_482
- smb_session_free.kalloc_type_view_508
- smb_session_lease_thread.kalloc_type_view_2228
- smb_share_create.kalloc_type_view_1497
- smb_share_create.kalloc_type_view_1503
- smb_share_free.kalloc_type_view_1458
- smbfs_smb_findopen.kalloc_type_view_5884
- smbfs_smb_reopen_file.kalloc_type_view_4971
- smbfs_smb_reopen_file.kalloc_type_view_5047
CStrings:
+ "%s: Bad output buf offset: %u\n"
+ "%s: Bad output buffer offset: %u\n"
+ "%s: CreateContextsOffset too small: %u\n"
+ "%s: NegotiateContextOffset too small: %u\n"
+ "%s: Odd FileNameLength %u not allowed in SMB2 FILE_ALL_INFORMATION\n"
+ "%s: Odd PathNameLength %u not allowed in unicode SMB_QFILEINFO_ALL_INFO\n"
+ "%s: OutputOffset too small: %u\n"
+ "%s: Read DataOffset too small: %u\n"
+ "%s: SecurityBufferOffset too small: %u\n"
+ "%s: UNIX_LINK nmlen=%zu would overflow target_allocsize\n"
+ "%s: UNIX_LINK reply too short for UTF-16 trim: nmlen=%zu\n"
+ "%s: Unsupported sa_family %u in client NIC entry\n"
+ "%s: WHOAMI invalid fields: reserved=%u cnt_gid=%d sids_cnt=%d\n"
+ "%s: WHOAMI kalloc_data of %zu bytes for ntwrk_gids failed\n"
+ "%s: WHOAMI total_bytes=%zu exceeds session_txmax=%u\n"
+ "%s: WHOAMI truncated gid list at index %u of %u (err=%d)\n"
+ "%s: id %u (main) (rqlist empty %d) (ref_cnt %u) \n"
+ "%s: sa_len %u too small for sa_family %u (min %u)\n"
+ "%s: unexpected leftover lease rqp — ref leak"
+ "smb_iod_lease_dequeue"
+ "smb_iod_lease_enqueue"
+ "smb_rw_cleanup"
+ "smb_session_lease_thread"
- "%s: id %u rqlist is not empty (ref_cnt %u) \n"
```
