## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-579.0.5.0.0
+579.0.10.0.0
   __TEXT.__const: 0xc35
   __TEXT.__cstring: 0x5196
-  __TEXT.__os_log: 0x17fea
-  __TEXT_EXEC.__text: 0x8401c
+  __TEXT.__os_log: 0x1801a
+  __TEXT_EXEC.__text: 0x84048
   __TEXT_EXEC.__auth_stubs: 0x1580
   __DATA.__data: 0x12d8
   __DATA.__bss: 0x107c

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 797
   Symbols:   2335
-  CStrings:  2656
+  CStrings:  2657
 
Symbols:
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6276
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6314
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6325
+ dequeue_notify_change_request.kalloc_type_view_1200
+ dequeue_notify_svrmsg_request.kalloc_type_view_1242
+ enqueue_notify_change_request.kalloc_type_view_1109
+ enqueue_notify_svrmsg_request.kalloc_type_view_1154
+ smb2fs_smb_markfordelete.kalloc_type_view_8908
+ smb2fs_smb_markfordelete.kalloc_type_view_8935
+ smb2fs_smb_ntcreatex.kalloc_type_view_9002
+ smb2fs_smb_ntcreatex.kalloc_type_view_9119
+ smb2fs_smb_qpathinfo.kalloc_type_view_9640
+ smb2fs_smb_qpathinfo.kalloc_type_view_9682
+ smb2fs_smb_qstreaminfo.kalloc_type_view_9765
+ smb2fs_smb_qstreaminfo.kalloc_type_view_9836
+ smb2fs_smb_query_network_interface_info.kalloc_type_view_11067
+ smb2fs_smb_query_network_interface_info.kalloc_type_view_11118
+ smb2fs_smb_rename.kalloc_type_view_10015
+ smb2fs_smb_rename.kalloc_type_view_9974
+ smb2fs_smb_request_resume_key.kalloc_type_view_10071
+ smb2fs_smb_request_resume_key.kalloc_type_view_10104
+ smb2fs_smb_security_set.kalloc_type_view_10198
+ smb2fs_smb_security_set.kalloc_type_view_10229
+ smb2fs_smb_set_allocation.kalloc_type_view_10322
+ smb2fs_smb_set_allocation.kalloc_type_view_10349
+ smb2fs_smb_set_eof.kalloc_type_view_10384
+ smb2fs_smb_set_eof.kalloc_type_view_10414
+ smb2fs_smb_set_file_basic_info.kalloc_type_view_10449
+ smb2fs_smb_setfattrNT.kalloc_type_view_10503
+ smb2fs_smb_setfattrNT.kalloc_type_view_10533
+ smb2fs_smb_setfattrNT.kalloc_type_view_10537
+ smb2fs_smb_setpattrNT.kalloc_type_view_10633
+ smb2fs_smb_validate_neg_info.kalloc_type_view_10837
+ smb2fs_smb_validate_neg_info.kalloc_type_view_11033
+ smb_iod_create.kalloc_type_view_4364
+ smb_iod_create.kalloc_type_view_4382
+ smb_iod_create.kalloc_type_view_4410
+ smb_iod_destroy.kalloc_type_view_4480
+ smb_iod_destroy.kalloc_type_view_4484
+ smb_iod_destroy.kalloc_type_view_4518
+ smb_iod_lease_dequeue.kalloc_type_view_4994
+ smb_iod_lease_enqueue.kalloc_type_view_4252
+ smb_iod_main.kalloc_type_view_4042
+ smb_iod_thread.kalloc_type_view_4146
+ smb_session_lease_thread.kalloc_type_view_2259
+ smbfs_clear_lockEntries.kalloc_type_view_6687
+ smbfs_clear_lockEntries.kalloc_type_view_6717
+ smbfs_free_locks_on_close.kalloc_type_view_6875
+ smbfs_get_lockEntry.kalloc_type_view_7082
+ smbfs_get_lockEntry.kalloc_type_view_7171
+ smbfs_lease_hash_add.kalloc_type_view_6128
+ smbfs_lease_hash_remove.kalloc_type_view_6228
+ smbfs_notify_change_create_thread.kalloc_type_view_1040
+ smbfs_notify_change_create_thread.kalloc_type_view_1054
+ smbfs_notify_change_destroy_thread.kalloc_type_view_1095
+ smbfs_smb_query_info.kalloc_type_view_9905
+ smbfs_smb_query_info.kalloc_type_view_9952
- AddRemoveByteRangeLockEntry.kalloc_type_view_6268
- AddRemoveByteRangeLockEntry.kalloc_type_view_6306
- AddRemoveByteRangeLockEntry.kalloc_type_view_6317
- dequeue_notify_change_request.kalloc_type_view_1174
- dequeue_notify_svrmsg_request.kalloc_type_view_1216
- enqueue_notify_change_request.kalloc_type_view_1083
- enqueue_notify_svrmsg_request.kalloc_type_view_1128
- smb2fs_smb_markfordelete.kalloc_type_view_8898
- smb2fs_smb_markfordelete.kalloc_type_view_8925
- smb2fs_smb_ntcreatex.kalloc_type_view_8992
- smb2fs_smb_ntcreatex.kalloc_type_view_9109
- smb2fs_smb_qpathinfo.kalloc_type_view_9641
- smb2fs_smb_qpathinfo.kalloc_type_view_9683
- smb2fs_smb_qstreaminfo.kalloc_type_view_9766
- smb2fs_smb_qstreaminfo.kalloc_type_view_9837
- smb2fs_smb_query_network_interface_info.kalloc_type_view_11068
- smb2fs_smb_query_network_interface_info.kalloc_type_view_11119
- smb2fs_smb_rename.kalloc_type_view_10016
- smb2fs_smb_rename.kalloc_type_view_9975
- smb2fs_smb_request_resume_key.kalloc_type_view_10072
- smb2fs_smb_request_resume_key.kalloc_type_view_10105
- smb2fs_smb_security_set.kalloc_type_view_10199
- smb2fs_smb_security_set.kalloc_type_view_10230
- smb2fs_smb_set_allocation.kalloc_type_view_10323
- smb2fs_smb_set_allocation.kalloc_type_view_10350
- smb2fs_smb_set_eof.kalloc_type_view_10385
- smb2fs_smb_set_eof.kalloc_type_view_10415
- smb2fs_smb_set_file_basic_info.kalloc_type_view_10450
- smb2fs_smb_setfattrNT.kalloc_type_view_10504
- smb2fs_smb_setfattrNT.kalloc_type_view_10534
- smb2fs_smb_setfattrNT.kalloc_type_view_10538
- smb2fs_smb_setpattrNT.kalloc_type_view_10634
- smb2fs_smb_validate_neg_info.kalloc_type_view_10838
- smb2fs_smb_validate_neg_info.kalloc_type_view_11034
- smb_iod_create.kalloc_type_view_4358
- smb_iod_create.kalloc_type_view_4376
- smb_iod_create.kalloc_type_view_4404
- smb_iod_destroy.kalloc_type_view_4474
- smb_iod_destroy.kalloc_type_view_4478
- smb_iod_destroy.kalloc_type_view_4505
- smb_iod_lease_dequeue.kalloc_type_view_4981
- smb_iod_lease_enqueue.kalloc_type_view_4244
- smb_iod_main.kalloc_type_view_4034
- smb_iod_thread.kalloc_type_view_4138
- smb_session_lease_thread.kalloc_type_view_2253
- smbfs_clear_lockEntries.kalloc_type_view_6679
- smbfs_clear_lockEntries.kalloc_type_view_6709
- smbfs_free_locks_on_close.kalloc_type_view_6867
- smbfs_get_lockEntry.kalloc_type_view_7074
- smbfs_get_lockEntry.kalloc_type_view_7163
- smbfs_lease_hash_add.kalloc_type_view_6120
- smbfs_lease_hash_remove.kalloc_type_view_6220
- smbfs_notify_change_create_thread.kalloc_type_view_1014
- smbfs_notify_change_create_thread.kalloc_type_view_1028
- smbfs_notify_change_destroy_thread.kalloc_type_view_1069
- smbfs_smb_query_info.kalloc_type_view_9906
- smbfs_smb_query_info.kalloc_type_view_9953
Functions:
~ _smb_session_lease_thread : 432 -> 440
~ _smb_iod_waitrq : 860 -> 872
~ _smb_iod_lease_enqueue : 212 -> 204
~ _smb2fs_smb_parse_ntcreatex : 552 -> 500
~ _smb2fs_smb_copyfile : 2488 -> 2572
CStrings:
+ "%s: xattr list grew past allocation: %zu > %zu\n"
```
