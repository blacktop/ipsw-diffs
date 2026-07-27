## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-538.160.8.0.0
+538.161.2.0.0
   __TEXT.__const: 0xc25
   __TEXT.__cstring: 0x489f
-  __TEXT.__os_log: 0x16061
-  __TEXT_EXEC.__text: 0x7c878
+  __TEXT.__os_log: 0x16091
+  __TEXT_EXEC.__text: 0x7c89c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdf8
   __DATA.__bss: 0x106c

   __DATA_CONST.__kalloc_var: 0x460
   Functions: 765
   Symbols:   2100
-  CStrings:  2506
+  CStrings:  2507
 
Symbols:
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6280
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6318
+ AddRemoveByteRangeLockEntry.kalloc_type_view_6329
+ dequeue_notify_change_request.kalloc_type_view_1200
+ dequeue_notify_svrmsg_request.kalloc_type_view_1242
+ enqueue_notify_change_request.kalloc_type_view_1109
+ enqueue_notify_svrmsg_request.kalloc_type_view_1154
+ smb2fs_smb_markfordelete.kalloc_type_view_8859
+ smb2fs_smb_markfordelete.kalloc_type_view_8886
+ smb2fs_smb_ntcreatex.kalloc_type_view_8953
+ smb2fs_smb_ntcreatex.kalloc_type_view_9070
+ smb2fs_smb_qpathinfo.kalloc_type_view_9590
+ smb2fs_smb_qpathinfo.kalloc_type_view_9632
+ smb2fs_smb_qstreaminfo.kalloc_type_view_9715
+ smb2fs_smb_qstreaminfo.kalloc_type_view_9786
+ smb2fs_smb_query_network_interface_info.kalloc_type_view_11022
+ smb2fs_smb_query_network_interface_info.kalloc_type_view_11073
+ smb2fs_smb_rename.kalloc_type_view_9924
+ smb2fs_smb_rename.kalloc_type_view_9965
+ smb2fs_smb_request_resume_key.kalloc_type_view_10021
+ smb2fs_smb_request_resume_key.kalloc_type_view_10054
+ smb2fs_smb_security_set.kalloc_type_view_10148
+ smb2fs_smb_security_set.kalloc_type_view_10179
+ smb2fs_smb_set_allocation.kalloc_type_view_10272
+ smb2fs_smb_set_allocation.kalloc_type_view_10299
+ smb2fs_smb_set_eof.kalloc_type_view_10334
+ smb2fs_smb_set_eof.kalloc_type_view_10364
+ smb2fs_smb_set_file_basic_info.kalloc_type_view_10399
+ smb2fs_smb_setfattrNT.kalloc_type_view_10453
+ smb2fs_smb_setfattrNT.kalloc_type_view_10483
+ smb2fs_smb_setfattrNT.kalloc_type_view_10487
+ smb2fs_smb_setpattrNT.kalloc_type_view_10583
+ smb2fs_smb_validate_neg_info.kalloc_type_view_10786
+ smb2fs_smb_validate_neg_info.kalloc_type_view_10988
+ smb_iod_destroy.kalloc_type_view_4384
+ smb_iod_lease_dequeue.kalloc_type_view_4836
+ smbfs_clear_lockEntries.kalloc_type_view_6691
+ smbfs_clear_lockEntries.kalloc_type_view_6721
+ smbfs_free_locks_on_close.kalloc_type_view_6879
+ smbfs_get_lockEntry.kalloc_type_view_7086
+ smbfs_get_lockEntry.kalloc_type_view_7175
+ smbfs_lease_hash_add.kalloc_type_view_6132
+ smbfs_lease_hash_remove.kalloc_type_view_6232
+ smbfs_notify_change_create_thread.kalloc_type_view_1040
+ smbfs_notify_change_create_thread.kalloc_type_view_1054
+ smbfs_notify_change_destroy_thread.kalloc_type_view_1095
+ smbfs_smb_query_info.kalloc_type_view_9855
+ smbfs_smb_query_info.kalloc_type_view_9902
- AddRemoveByteRangeLockEntry.kalloc_type_view_6272
- AddRemoveByteRangeLockEntry.kalloc_type_view_6310
- AddRemoveByteRangeLockEntry.kalloc_type_view_6321
- dequeue_notify_change_request.kalloc_type_view_1174
- dequeue_notify_svrmsg_request.kalloc_type_view_1216
- enqueue_notify_change_request.kalloc_type_view_1083
- enqueue_notify_svrmsg_request.kalloc_type_view_1128
- smb2fs_smb_markfordelete.kalloc_type_view_8849
- smb2fs_smb_markfordelete.kalloc_type_view_8876
- smb2fs_smb_ntcreatex.kalloc_type_view_8943
- smb2fs_smb_ntcreatex.kalloc_type_view_9060
- smb2fs_smb_qpathinfo.kalloc_type_view_9585
- smb2fs_smb_qpathinfo.kalloc_type_view_9627
- smb2fs_smb_qstreaminfo.kalloc_type_view_9710
- smb2fs_smb_qstreaminfo.kalloc_type_view_9781
- smb2fs_smb_query_network_interface_info.kalloc_type_view_11017
- smb2fs_smb_query_network_interface_info.kalloc_type_view_11068
- smb2fs_smb_rename.kalloc_type_view_9919
- smb2fs_smb_rename.kalloc_type_view_9960
- smb2fs_smb_request_resume_key.kalloc_type_view_10016
- smb2fs_smb_request_resume_key.kalloc_type_view_10049
- smb2fs_smb_security_set.kalloc_type_view_10143
- smb2fs_smb_security_set.kalloc_type_view_10174
- smb2fs_smb_set_allocation.kalloc_type_view_10267
- smb2fs_smb_set_allocation.kalloc_type_view_10294
- smb2fs_smb_set_eof.kalloc_type_view_10329
- smb2fs_smb_set_eof.kalloc_type_view_10359
- smb2fs_smb_set_file_basic_info.kalloc_type_view_10394
- smb2fs_smb_setfattrNT.kalloc_type_view_10448
- smb2fs_smb_setfattrNT.kalloc_type_view_10478
- smb2fs_smb_setfattrNT.kalloc_type_view_10482
- smb2fs_smb_setpattrNT.kalloc_type_view_10578
- smb2fs_smb_validate_neg_info.kalloc_type_view_10781
- smb2fs_smb_validate_neg_info.kalloc_type_view_10983
- smb_iod_destroy.kalloc_type_view_4377
- smb_iod_lease_dequeue.kalloc_type_view_4829
- smbfs_clear_lockEntries.kalloc_type_view_6683
- smbfs_clear_lockEntries.kalloc_type_view_6713
- smbfs_free_locks_on_close.kalloc_type_view_6871
- smbfs_get_lockEntry.kalloc_type_view_7078
- smbfs_get_lockEntry.kalloc_type_view_7167
- smbfs_lease_hash_add.kalloc_type_view_6124
- smbfs_lease_hash_remove.kalloc_type_view_6224
- smbfs_notify_change_create_thread.kalloc_type_view_1014
- smbfs_notify_change_create_thread.kalloc_type_view_1028
- smbfs_notify_change_destroy_thread.kalloc_type_view_1069
- smbfs_smb_query_info.kalloc_type_view_9850
- smbfs_smb_query_info.kalloc_type_view_9897
Functions:
~ _smb2fs_smb_parse_ntcreatex : 536 -> 500
~ _smb2fs_smb_copyfile : 2356 -> 2428
CStrings:
+ "%s: xattr list grew past allocation: %zu > %zu\n"
```
