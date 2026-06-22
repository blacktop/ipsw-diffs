## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

```diff

-578.0.0.0.0
+579.0.1.0.0
   __TEXT.__const: 0xc35 sha256:2e22cf8dfe2123cf0773dd06af27dd4647b0c8f5f2c6d70cecd5f54ebbb5715b
-  __TEXT.__cstring: 0x5142 sha256:5ddaa5cbe9e5e00506435e88b3472b96014b44cc7614b43c02da3c240745e48a
-  __TEXT.__os_log: 0x17ca3 sha256:fb7adc8f9c5effcb0db7dd73a08a2844c03bb259fb4f13349137f83fcd4e3192
-  __TEXT_EXEC.__text: 0x8360c sha256:fe71aea81f176b001a02de55d94a9a3a6f5035396bddda71d93a3b323f7ba0c0
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x12d8 sha256:5f1fecfb237c5de4af4ed4a00e817d2d606af7850de4fa372fc37fac0f342103
+  __TEXT.__cstring: 0x5196 sha256:aeae9fe8e5f6de6583dc04546d1d153a6dda08cb4458622c30280fa499afb393
+  __TEXT.__os_log: 0x17e36 sha256:a0312672dc32b888996b4e590d24ccd81250715f581aead229fe51675cc6127c
+  __TEXT_EXEC.__text: 0x83e38 sha256:506ec250b7e72cd5e43aa41886869b95bab013a7eff2e12e39a667b206f46c53
+  __TEXT_EXEC.__auth_stubs: 0x1580 sha256:7ffd8c64946cada83a4e53abbf6947b9993262db01a585d9f07b8955ab60f77b
+  __DATA.__data: 0x12d8 sha256:381b26cc98126ca8a7edc57f73daafb141b99e6aaa17485dcff6fd1eef494bd0
   __DATA.__bss: 0x107c sha256:f54e116b2ac6ca925ac8b5fad18420a77c3f2ba7174258dac775b054a3c8c799
   __DATA.__common: 0x2278 sha256:b3e05266fc0a39ee10337d8636bb59b8eb1734c612083f4f9f5fbfc1308498ca
-  __DATA_CONST.__const: 0x78 sha256:b0a3b373697268ba8f2b5b918eb47580dbc318a050bbe4ae4064c8641c157c7a
-  __DATA_CONST.__kalloc_type: 0x4e80 sha256:947e85e8c59956a779da040ddafe635d9f2f40846c41243a7bad6cbd7b8fa57f
-  __DATA_CONST.__kalloc_var: 0x640 sha256:5f427cad127954d1dcb8507bf211b68794466e4c115910f7500affbf6f29be86
-  __DATA_CONST.__auth_got: 0xac0 sha256:72e0b60b2a81a3dc089d17f06acb30d2990cbab6a1874602a83e1c70780797ed
-  __DATA_CONST.__got: 0x50 sha256:5464bd914c45e52a371620f5556cd79d7661e37468113b51c44a6ef6c6578633
-  __DATA_CONST.__auth_ptr: 0x8 sha256:862b908ab75481e86d3cd1c20b95ce20b1268c53a48070cc9f50fd2a3af9a5aa
-  UUID: 7BDA2F91-62D0-38C5-9E7F-449D019EA912
-  Functions: 796
-  Symbols:   3991
-  CStrings:  2638
+  __DATA_CONST.__const: 0x78 sha256:b3fbd68e4112948d6c497f0f570171c27504d625ae9f9b665b820fdfe38b88f0
+  __DATA_CONST.__kalloc_type: 0x4ec0 sha256:12dc998c1f3f2cd0ad8f97338168d15042fcc8adb58568b11c7b32be8d9dbaa7
+  __DATA_CONST.__kalloc_var: 0x640 sha256:238f5ea9a2e88b790b1dc57a722ffb1d6b96f6883b2023cde72d7de0e127be69
+  __DATA_CONST.__auth_got: 0xac0 sha256:ea83ffd01cc4b574955a1f2ebee1b13a3c581f84b4ad72eb9b9aacecdf38d013
+  __DATA_CONST.__got: 0x50 sha256:5b14176b41c10c947ca2e5c18b21f337d55fa85e6ba76d141c925a895a854c92
+  __DATA_CONST.__auth_ptr: 0x8 sha256:91d75f79896d310ee08788f6bbf23d1a2aeb1802a80055b457e609d832720be6
+  UUID: 4EA7E2DA-A76C-3D07-9018-351242EEDF3F
+  Functions: 797
+  Symbols:   4000
+  CStrings:  2649
 
Symbols:
+ _smb_iod_lease_dequeue
+ nsmb_dev_load.kalloc_type_view_1854
+ nsmb_dev_load.kalloc_type_view_1862
+ smb1fs_qfsattr._os_log_fmt.21
+ smb1fs_qfsattr._os_log_fmt.29
+ smb1fs_smb_findclose.kalloc_type_view_5639
+ smb1fs_smb_findnext._os_log_fmt.54
+ smb1fs_smb_ntcreatex._os_log_fmt.38
+ smb1fs_smb_ntcreatex._os_log_fmt.39
+ smb1fs_smb_qpathinfo._os_log_fmt.6
+ smb2_mc_add_new_interface_info_to_list._os_log_fmt.48
+ smb2_mc_add_new_interface_info_to_list.kalloc_type_view_1503
+ smb2_mc_count_connection_stats._os_log_fmt.32
+ smb2_mc_count_connection_stats._os_log_fmt.33
+ smb2_mc_init._os_log_fmt.21
+ smb2_mc_init._os_log_fmt.22
+ smb2_mc_parse_client_interface_array._os_log_fmt.10
+ smb2_mc_parse_client_interface_array._os_log_fmt.11
+ smb2_mc_parse_client_interface_array._os_log_fmt.14
+ smb2_mc_parse_client_interface_array.kalloc_type_view_741
+ smb2_mc_query_info_response_event._os_log_fmt.16
+ smb2_mc_query_info_response_event._os_log_fmt.17
+ smb2_mc_query_info_response_event.kalloc_type_view_807
+ smb2_mc_query_info_response_event.kalloc_type_view_883
+ smb2_mc_release_connection_list.kalloc_type_view_1835
+ smb2_mc_release_interface.kalloc_type_view_1849
+ smb2_mc_release_interface.kalloc_type_view_1864
+ smb2_mc_remove_nic_if_unused._os_log_fmt.43
+ smb2_mc_remove_nic_if_unused.kalloc_type_view_995
+ smb2_mc_report_connection_trial_results._os_log_fmt.25
+ smb2_mc_sockaddr_cmp._os_log_fmt.50
+ smb2_mc_update_con_list._os_log_fmt.49
+ smb2_mc_update_con_list.kalloc_type_view_1672
+ smb2_mc_update_info_with_ip._os_log_fmt.41
+ smb2_mc_update_info_with_ip._os_log_fmt.42
+ smb2_mc_update_info_with_ip.kalloc_type_view_2011
+ smb2_mc_update_info_with_ip.kalloc_type_view_2019
+ smb2_mc_update_main_channel._os_log_fmt.23
+ smb2_mc_update_main_channel._os_log_fmt.24
+ smb2_mc_update_new_connection._os_log_fmt.51
+ smb2_mc_update_new_connection._os_log_fmt.52
+ smb2_mc_update_nic_list_from_notifier._os_log_fmt.20
+ smb2_session_maxread._os_log_fmt.169
+ smb2_session_maxwrite._os_log_fmt.173
+ smb2_smb_add_create_contexts._os_log_fmt.179
+ smb2_smb_add_negotiate_contexts._os_log_fmt.183
+ smb2_smb_get_alloc_size._os_log_fmt.247
+ smb2_smb_get_quantum_sizes._os_log_fmt.283
+ smb2_smb_logoff._os_log_fmt.181
+ smb2_smb_parse_create_contexts._os_log_fmt.216
+ smb2_smb_parse_create_str._os_log_fmt.259
+ smb2_smb_parse_create_str._os_log_fmt.260
+ smb2_smb_parse_file_all_info._os_log_fmt.256
+ smb2_smb_parse_file_all_info._os_log_fmt.257
+ smb2_smb_parse_ioctl._os_log_fmt.87
+ smb2_smb_parse_lease_break._os_log_fmt.88
+ smb2_smb_parse_negotiate._os_log_fmt.229
+ smb2_smb_parse_negotiate_contexts._os_log_fmt.246
+ smb2_smb_parse_query_dir._os_log_fmt.94
+ smb2_smb_parse_query_dir_both_dir_info._os_log_fmt.122
+ smb2_smb_parse_query_info._os_log_fmt.124
+ smb2_smb_parse_read_one._os_log_fmt.126
+ smb2_smb_parse_security._os_log_fmt.127
+ smb2_smb_parse_svrmsg_notify._os_log_fmt.128
+ smb2_smb_parse_svrmsg_notify._os_log_fmt.130
+ smb2_smb_query_dir._os_log_fmt.133
+ smb2_smb_query_info._os_log_fmt.138
+ smb2_smb_read._os_log_fmt.140
+ smb2_smb_read_one._os_log_fmt.144
+ smb2_smb_read_uio.kalloc_type_view_9173
+ smb2_smb_read_uio.kalloc_type_view_9190
+ smb2_smb_read_write_async._os_log_fmt.263
+ smb2_smb_read_write_async._os_log_fmt.264
+ smb2_smb_read_write_async._os_log_fmt.269
+ smb2_smb_read_write_async._os_log_fmt.278
+ smb2_smb_read_write_async._os_log_fmt.281
+ smb2_smb_read_write_async._os_log_fmt.282
+ smb2_smb_read_write_async.kalloc_type_view_9342
+ smb2_smb_read_write_async.kalloc_type_view_9408
+ smb2_smb_read_write_async.kalloc_type_view_9736
+ smb2_smb_read_write_async.kalloc_type_view_9805
+ smb2_smb_read_write_fill._os_log_fmt.284
+ smb2_smb_set_info._os_log_fmt.147
+ smb2_smb_tree_connect._os_log_fmt.149
+ smb2_smb_tree_connect._os_log_fmt.156
+ smb2_smb_tree_connect._os_log_fmt.162
+ smb2_smb_tree_connect_bad_cluster_dialect._os_log_fmt.286
+ smb2_smb_tree_connect_bad_cluster_dialect._os_log_fmt.287
+ smb2_smb_tree_disconnect._os_log_fmt.288
+ smb2_smb_tree_disconnect._os_log_fmt.289
+ smb2_smb_write._os_log_fmt.163
+ smb2_smb_write_one._os_log_fmt.165
+ smb2_smb_write_uio._os_log_fmt.290
+ smb2_smb_write_uio.kalloc_type_view_10965
+ smb2_smb_write_uio.kalloc_type_view_11018
+ smb_iod_create.kalloc_type_view_4358
+ smb_iod_create.kalloc_type_view_4376
+ smb_iod_create.kalloc_type_view_4404
+ smb_iod_destroy.kalloc_type_view_4474
+ smb_iod_destroy.kalloc_type_view_4478
+ smb_iod_destroy.kalloc_type_view_4505
+ smb_iod_lease_dequeue.kalloc_type_view_4981
+ smb_iod_lease_enqueue.kalloc_type_view_4244
+ smb_rw_cleanup.kalloc_type_view_415
+ smb_rw_init.kalloc_type_view_276
+ smb_rw_proxy._os_log_fmt.5
+ smb_rw_start._os_log_fmt.8
+ smb_rw_thread.kalloc_type_view_208
+ smb_rw_thread.kalloc_type_view_226
+ smb_session_create.kalloc_type_view_583
+ smb_session_free._os_log_fmt.73
+ smb_session_free.kalloc_type_view_484
+ smb_session_free.kalloc_type_view_510
+ smb_session_lease_thread.kalloc_type_view_2253
+ smb_share_create.kalloc_type_view_1513
+ smb_share_create.kalloc_type_view_1519
+ smb_share_free.kalloc_type_view_1470
+ smbfs_lookup._os_log_fmt.56
+ smbfs_lookup._os_log_fmt.57
+ smbfs_remove_dir_lease._os_log_fmt.59
+ smbfs_smb_findopen.kalloc_type_view_5902
+ smbfs_smb_fsync._os_log_fmt.35
+ smbfs_smb_fsync._os_log_fmt.36
+ smbfs_smb_getsec_int._os_log_fmt.64
+ smbfs_smb_getsec_int._os_log_fmt.65
+ smbfs_smb_reopen_file._os_log_fmt.50
+ smbfs_smb_reopen_file._os_log_fmt.51
+ smbfs_smb_reopen_file.kalloc_type_view_4989
+ smbfs_smb_reopen_file.kalloc_type_view_5065
+ smbfs_smb_t2rename._os_log_fmt.30
+ smbfs_smb_trans2find2._os_log_fmt.62
+ smbfs_smb_trans2find2._os_log_fmt.63
+ smbfs_smb_unix_read_symlink._os_log_fmt.11
+ smbfs_smb_unix_read_symlink._os_log_fmt.12
+ smbfs_smb_windows_read_symlink._os_log_fmt.10
+ smbfs_tmpclose._os_log_fmt.46
+ smbfs_tmpclose._os_log_fmt.47
+ smbfs_tmpopen._os_log_fmt.43
+ smbfs_tmpopen._os_log_fmt.44
+ smbfs_unix_qfsattr._os_log_fmt.20
+ smbfs_unix_whoami._os_log_fmt.19
- nsmb_dev_load.kalloc_type_view_1852
- nsmb_dev_load.kalloc_type_view_1860
- smb1fs_qfsattr._os_log_fmt.19
- smb1fs_qfsattr._os_log_fmt.27
- smb1fs_smb_findclose.kalloc_type_view_5622
- smb1fs_smb_findnext._os_log_fmt.52
- smb1fs_smb_ntcreatex._os_log_fmt.35
- smb1fs_smb_ntcreatex._os_log_fmt.36
- smb2_mc_add_new_interface_info_to_list._os_log_fmt.46
- smb2_mc_add_new_interface_info_to_list.kalloc_type_view_1483
- smb2_mc_count_connection_stats._os_log_fmt.29
- smb2_mc_count_connection_stats._os_log_fmt.30
- smb2_mc_init._os_log_fmt.19
- smb2_mc_init._os_log_fmt.20
- smb2_mc_parse_client_interface_array._os_log_fmt.12
- smb2_mc_parse_client_interface_array.kalloc_type_view_721
- smb2_mc_query_info_response_event._os_log_fmt.13
- smb2_mc_query_info_response_event._os_log_fmt.14
- smb2_mc_query_info_response_event.kalloc_type_view_787
- smb2_mc_query_info_response_event.kalloc_type_view_863
- smb2_mc_release_connection_list.kalloc_type_view_1815
- smb2_mc_release_interface.kalloc_type_view_1829
- smb2_mc_release_interface.kalloc_type_view_1844
- smb2_mc_remove_nic_if_unused._os_log_fmt.41
- smb2_mc_remove_nic_if_unused.kalloc_type_view_975
- smb2_mc_report_connection_trial_results._os_log_fmt.23
- smb2_mc_sockaddr_cmp._os_log_fmt.48
- smb2_mc_update_con_list._os_log_fmt.47
- smb2_mc_update_con_list.kalloc_type_view_1652
- smb2_mc_update_info_with_ip._os_log_fmt.39
- smb2_mc_update_info_with_ip._os_log_fmt.40
- smb2_mc_update_info_with_ip.kalloc_type_view_1991
- smb2_mc_update_info_with_ip.kalloc_type_view_1999
- smb2_mc_update_main_channel._os_log_fmt.21
- smb2_mc_update_main_channel._os_log_fmt.22
- smb2_mc_update_new_connection._os_log_fmt.49
- smb2_mc_update_new_connection._os_log_fmt.50
- smb2_mc_update_nic_list_from_notifier._os_log_fmt.18
- smb2_session_maxread._os_log_fmt.165
- smb2_session_maxwrite._os_log_fmt.169
- smb2_smb_add_create_contexts._os_log_fmt.173
- smb2_smb_add_negotiate_contexts._os_log_fmt.181
- smb2_smb_get_alloc_size._os_log_fmt.246
- smb2_smb_get_quantum_sizes._os_log_fmt.281
- smb2_smb_logoff._os_log_fmt.179
- smb2_smb_parse_create_contexts._os_log_fmt.183
- smb2_smb_parse_create_str._os_log_fmt.256
- smb2_smb_parse_create_str._os_log_fmt.257
- smb2_smb_parse_file_all_info._os_log_fmt.253
- smb2_smb_parse_lease_break._os_log_fmt.87
- smb2_smb_parse_negotiate._os_log_fmt.216
- smb2_smb_parse_negotiate_contexts._os_log_fmt.229
- smb2_smb_parse_query_dir._os_log_fmt.88
- smb2_smb_parse_query_dir_both_dir_info._os_log_fmt.94
- smb2_smb_parse_query_info._os_log_fmt.122
- smb2_smb_parse_read_one._os_log_fmt.124
- smb2_smb_parse_security._os_log_fmt.126
- smb2_smb_parse_svrmsg_notify._os_log_fmt.127
- smb2_smb_parse_svrmsg_notify._os_log_fmt.129
- smb2_smb_query_dir._os_log_fmt.130
- smb2_smb_query_info._os_log_fmt.133
- smb2_smb_read._os_log_fmt.138
- smb2_smb_read_one._os_log_fmt.140
- smb2_smb_read_uio.kalloc_type_view_9149
- smb2_smb_read_uio.kalloc_type_view_9166
- smb2_smb_read_write_async._os_log_fmt.259
- smb2_smb_read_write_async._os_log_fmt.260
- smb2_smb_read_write_async._os_log_fmt.265
- smb2_smb_read_write_async._os_log_fmt.266
- smb2_smb_read_write_async._os_log_fmt.271
- smb2_smb_read_write_async._os_log_fmt.280
- smb2_smb_read_write_async.kalloc_type_view_9318
- smb2_smb_read_write_async.kalloc_type_view_9384
- smb2_smb_read_write_async.kalloc_type_view_9712
- smb2_smb_read_write_async.kalloc_type_view_9781
- smb2_smb_read_write_fill._os_log_fmt.282
- smb2_smb_set_info._os_log_fmt.144
- smb2_smb_tree_connect._os_log_fmt.148
- smb2_smb_tree_connect._os_log_fmt.150
- smb2_smb_tree_connect._os_log_fmt.157
- smb2_smb_tree_connect_bad_cluster_dialect._os_log_fmt.283
- smb2_smb_tree_connect_bad_cluster_dialect._os_log_fmt.284
- smb2_smb_tree_disconnect._os_log_fmt.286
- smb2_smb_tree_disconnect._os_log_fmt.287
- smb2_smb_write._os_log_fmt.162
- smb2_smb_write_one._os_log_fmt.163
- smb2_smb_write_uio._os_log_fmt.288
- smb2_smb_write_uio.kalloc_type_view_10941
- smb2_smb_write_uio.kalloc_type_view_10994
- smb_iod_create.kalloc_type_view_4336
- smb_iod_create.kalloc_type_view_4354
- smb_iod_create.kalloc_type_view_4382
- smb_iod_destroy.kalloc_type_view_4452
- smb_iod_destroy.kalloc_type_view_4456
- smb_iod_destroy.kalloc_type_view_4483
- smb_iod_lease_dequeue.kalloc_type_view_4935
- smb_iod_lease_enqueue.kalloc_type_view_4232
- smb_rw_init.kalloc_type_view_269
- smb_rw_proxy._os_log_fmt.3
- smb_rw_start._os_log_fmt.6
- smb_rw_thread.kalloc_type_view_201
- smb_rw_thread.kalloc_type_view_219
- smb_session_create.kalloc_type_view_581
- smb_session_free.kalloc_type_view_482
- smb_session_free.kalloc_type_view_508
- smb_session_lease_thread.kalloc_type_view_2244
- smb_share_create.kalloc_type_view_1511
- smb_share_create.kalloc_type_view_1517
- smb_share_free.kalloc_type_view_1468
- smbfs_lookup._os_log_fmt.53
- smbfs_lookup._os_log_fmt.54
- smbfs_remove_dir_lease._os_log_fmt.57
- smbfs_smb_findopen.kalloc_type_view_5885
- smbfs_smb_fsync._os_log_fmt.32
- smbfs_smb_fsync._os_log_fmt.33
- smbfs_smb_getsec_int._os_log_fmt.62
- smbfs_smb_getsec_int._os_log_fmt.63
- smbfs_smb_reopen_file._os_log_fmt.48
- smbfs_smb_reopen_file._os_log_fmt.49
- smbfs_smb_reopen_file.kalloc_type_view_4972
- smbfs_smb_reopen_file.kalloc_type_view_5048
- smbfs_smb_t2rename._os_log_fmt.28
- smbfs_smb_trans2find2._os_log_fmt.60
- smbfs_smb_trans2find2._os_log_fmt.61
- smbfs_smb_unix_read_symlink._os_log_fmt.10
- smbfs_smb_windows_read_symlink._os_log_fmt.7
- smbfs_tmpclose._os_log_fmt.43
- smbfs_tmpclose._os_log_fmt.44
- smbfs_tmpopen._os_log_fmt.38
- smbfs_tmpopen._os_log_fmt.39
- smbfs_unix_qfsattr._os_log_fmt.18
- smbfs_unix_whoami._os_log_fmt.17
CStrings:
+ "%s: CtlCode mismatch: request 0x%x, response 0x%x\n"
+ "%s: Odd FileNameLength %u not allowed in SMB2 FILE_ALL_INFORMATION\n"
+ "%s: Odd PathNameLength %u not allowed in unicode SMB_QFILEINFO_ALL_INFO\n"
+ "%s: UNIX_LINK reply too short for UTF-16 trim: nmlen=%zu\n"
+ "%s: Unsupported sa_family %u in client NIC entry\n"
+ "%s: id %u (main) (rqlist empty %d) (ref_cnt %u) \n"
+ "%s: sa_len %u too small for sa_family %u (min %u)\n"
+ "%s: unexpected leftover lease rqp — ref leak"
+ "smb_iod_lease_dequeue"
+ "smb_iod_lease_enqueue"
+ "smb_rw_cleanup"
+ "smb_session_lease_thread"
- "%s: id %u rqlist is not empty (ref_cnt %u) \n"

```
