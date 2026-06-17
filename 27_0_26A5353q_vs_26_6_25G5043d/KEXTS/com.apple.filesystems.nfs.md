## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

```diff

-356.0.0.0.0
+343.160.2.0.0
   __TEXT.__cstring: 0x9c08 sha256:e73ef3da3ced65b5797ba897bf180ae1e5b4560c94699e2d8c01c24ee7234d39
   __TEXT.__const: 0x39c sha256:fab49046e42bd797e8443daf729b8310cda528415f11ff2e9dee7321ab663a0c
-  __TEXT_EXEC.__text: 0x9d4e8 sha256:56fa7ae00403d142d85ed529b5f83b2c7ec837f7f1b3082122fbe52069f25d4b
+  __TEXT_EXEC.__text: 0x9d26c sha256:8fa8f4e5a2d7e3124f2e1e2bc4049a885653954d990dfb0e4e3d80213b97ecee
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xf00 sha256:d82f41ef9abf8d91157241c722d57bce8a2fc947417addd2f50c77ca6a2edd19
+  __DATA.__data: 0xf00 sha256:4cfdb3b413df59a7b2976bcd8a694986fd95455d9aeacb1456add6dde72fde31
   __DATA.__common: 0xee4 sha256:cc7eec1a25c8146b755306b97d56d9331eb3e3894dad122b8737969bfcc883c5
   __DATA.__bss: 0xb0 sha256:86d2cf5b090f43ee54d8f7c1dcf746a853951191457ff6dac96269a9d24860b9
-  __DATA_CONST.__mod_init_func: 0x8 sha256:3c0c8e63f53a9d5f9a189bd1afeed26ffe95469c5b5fd55d3c849ea738e1bed9
-  __DATA_CONST.__mod_term_func: 0x8 sha256:3907d346405651ea9aa04035fe55e5ece3c71152f0fd0784caa44c6ee81dc2a5
-  __DATA_CONST.__const: 0x1e58 sha256:de11d01b9ede512fc28c7c6c970a4c20409c270d07125120e9b8bfbc29141b07
-  __DATA_CONST.__kalloc_type: 0x1000 sha256:c28e3aad5705f8bfe95e467d370fa856b91b08b7213f9b2642615068198beb1c
-  __DATA_CONST.__kalloc_var: 0x320 sha256:7ca59460b88147012e1bd6d9290ecd30224b79306450f97f8fff4243595363f9
-  __DATA_CONST.__auth_got: 0xa98 sha256:85c8f91cc51d0370fb155e44e43fb4be32590a06f1fc28ecd890caf914c9e70b
-  __DATA_CONST.__got: 0xa8 sha256:60ef2fbda91fe9b379172648f08e3856a7fc523f5b582f2eec3967be05c077dc
-  __DATA_CONST.__auth_ptr: 0x8 sha256:3c2ede708c5837723d08eb66a1bde0785f3f7743308e331909f3d0594415b976
-  UUID: D27882AF-DA40-3AD3-AE8D-48266CE76B49
-  Functions: 1003
-  Symbols:   2020
+  __DATA_CONST.__auth_got: 0xa88 sha256:5d1bb9cc0d83a745606e7adc959f99d98e72ec942c9c18dc413250ce70065722
+  __DATA_CONST.__got: 0xa8 sha256:1e7ec22c7b241efe54d823a769717e29db6529836a9d56999923a0fcd1c9e328
+  __DATA_CONST.__auth_ptr: 0x8 sha256:68e0e529e940db22554e9c491076fd02667b81de55c486ab6ba87f7a2b4c36db
+  __DATA_CONST.__mod_init_func: 0x8 sha256:e6ad532ec29d1a0be5a251b9aa3a2ad88765f8b47fea100e50bc5a22a9f10d45
+  __DATA_CONST.__mod_term_func: 0x8 sha256:fb27b99c0cfd6dc802d3f60439408f127dc94ebce100c3682ef2a53273e631e0
+  __DATA_CONST.__const: 0x1e58 sha256:2771dad2b63238b64be60b8948c56aba305cb2bfac0d4bf69b982350088e2166
+  __DATA_CONST.__kalloc_type: 0x1000 sha256:643367dc370374a169c631f5e7eb81cf542033c50b1401afc84e2ae860147c62
+  __DATA_CONST.__kalloc_var: 0x320 sha256:3833ae88f88ee16b9308ec0670af0e66023574e006005823f72805b57012a013
+  UUID: C9DE2A84-7A00-3910-82C2-737731D3FD4B
+  Functions: 1002
+  Symbols:   2018
   CStrings:  1155
 
Symbols:
+ mountnfs.kalloc_type_view_2988
+ mountnfs.kalloc_type_view_2997
+ mountnfs.kalloc_type_view_3006
+ mountnfs.kalloc_type_view_3016
+ mountnfs.kalloc_type_view_3039
+ nfs3_vnop_create.kalloc_type_view_4513
+ nfs3_vnop_create.kalloc_type_view_4641
+ nfs3_vnop_mkdir.kalloc_type_view_5621
+ nfs3_vnop_mkdir.kalloc_type_view_5735
+ nfs3_vnop_rmdir.kalloc_type_view_5792
+ nfs3_vnop_rmdir.kalloc_type_view_5868
+ nfs3_vnop_symlink.kalloc_type_view_5432
+ nfs3_vnop_symlink.kalloc_type_view_5552
+ nfs4_callback_timer.kalloc_type_view_2750
+ nfs4_cb_accept.kalloc_type_view_2784
+ nfs4_cb_accept.kalloc_type_view_2794
+ nfs4_create_rpc.kalloc_type_view_7710
+ nfs4_create_rpc.kalloc_type_view_7841
+ nfs4_mount_callback_shutdown.kalloc_type_view_2717
+ nfs4_open_rpc_internal.kalloc_type_view_5692
+ nfs4_open_rpc_internal.kalloc_type_view_6051
+ nfs4_parsefattr.kalloc_type_view_2744
+ nfs4_vnop_rmdir.kalloc_type_view_8170
+ nfs4_vnop_rmdir.kalloc_type_view_8207
+ nfs_file_lock_alloc.kalloc_type_view_3842
+ nfs_file_lock_destroy.kalloc_type_view_3860
+ nfs_fs_locations_cleanup.kalloc_type_view_4711
+ nfs_fs_locations_cleanup.kalloc_type_view_4714
+ nfs_fs_locations_cleanup.kalloc_type_view_4716
+ nfs_fs_locations_cleanup.kalloc_type_view_4719
+ nfs_fs_locations_cleanup.kalloc_type_view_4721
+ nfs_lock_owner_destroy.kalloc_type_view_3695
+ nfs_lock_owner_find.kalloc_type_view_3655
+ nfs_mount_cleanup.kalloc_type_view_5022
+ nfs_open_file_destroy.kalloc_type_view_2449
+ nfs_open_file_find_internal.kalloc_type_view_2392
+ nfs_open_owner_destroy.kalloc_type_view_2189
+ nfs_open_owner_find.kalloc_type_view_2148
+ nfs_request_destroy.kalloc_type_view_4517
+ nfs_sillyrename.kalloc_type_view_7055
+ nfs_sillyrename.kalloc_type_view_7114
+ nfs_socket_create.kalloc_type_view_638
+ nfs_socket_destroy.kalloc_type_view_739
+ nfs_vnop_inactive.kalloc_type_view_666
+ nfs_vnop_inactive.kalloc_type_view_941
+ nfs_vnop_inactive.kalloc_type_view_943
+ nfs_vnop_reclaim.kalloc_type_view_1129
+ nfs_vnop_remove.kalloc_type_view_4698
+ nfs_vnop_remove.kalloc_type_view_4894
+ nfs_vnop_setattr.kalloc_type_view_2426
+ nfs_vnop_setattr.kalloc_type_view_2470
- _lck_rw_unlock_exclusive
- _lck_rw_unlock_shared
- mountnfs.kalloc_type_view_2994
- mountnfs.kalloc_type_view_3003
- mountnfs.kalloc_type_view_3012
- mountnfs.kalloc_type_view_3022
- mountnfs.kalloc_type_view_3045
- nfs3_vnop_create.kalloc_type_view_4525
- nfs3_vnop_create.kalloc_type_view_4653
- nfs3_vnop_mkdir.kalloc_type_view_5633
- nfs3_vnop_mkdir.kalloc_type_view_5747
- nfs3_vnop_rmdir.kalloc_type_view_5804
- nfs3_vnop_rmdir.kalloc_type_view_5880
- nfs3_vnop_symlink.kalloc_type_view_5444
- nfs3_vnop_symlink.kalloc_type_view_5564
- nfs4_callback_timer.kalloc_type_view_2771
- nfs4_cb_accept.kalloc_type_view_2805
- nfs4_cb_accept.kalloc_type_view_2815
- nfs4_create_rpc.kalloc_type_view_7722
- nfs4_create_rpc.kalloc_type_view_7853
- nfs4_mount_callback_shutdown.kalloc_type_view_2738
- nfs4_open_rpc_internal.kalloc_type_view_5704
- nfs4_open_rpc_internal.kalloc_type_view_6063
- nfs4_parsefattr.kalloc_type_view_2745
- nfs4_vnop_rmdir.kalloc_type_view_8182
- nfs4_vnop_rmdir.kalloc_type_view_8219
- nfs_file_lock_alloc.kalloc_type_view_3854
- nfs_file_lock_destroy.kalloc_type_view_3872
- nfs_fs_locations_cleanup.kalloc_type_view_4717
- nfs_fs_locations_cleanup.kalloc_type_view_4720
- nfs_fs_locations_cleanup.kalloc_type_view_4722
- nfs_fs_locations_cleanup.kalloc_type_view_4725
- nfs_fs_locations_cleanup.kalloc_type_view_4727
- nfs_lock_owner_destroy.kalloc_type_view_3707
- nfs_lock_owner_find.kalloc_type_view_3667
- nfs_mount_cleanup.kalloc_type_view_5028
- nfs_open_file_destroy.kalloc_type_view_2461
- nfs_open_file_find_internal.kalloc_type_view_2404
- nfs_open_owner_destroy.kalloc_type_view_2201
- nfs_open_owner_find.kalloc_type_view_2160
- nfs_request_destroy.kalloc_type_view_4538
- nfs_sillyrename.kalloc_type_view_7067
- nfs_sillyrename.kalloc_type_view_7126
- nfs_socket_create.kalloc_type_view_659
- nfs_socket_destroy.kalloc_type_view_760
- nfs_vnop_inactive.kalloc_type_view_675
- nfs_vnop_inactive.kalloc_type_view_950
- nfs_vnop_inactive.kalloc_type_view_952
- nfs_vnop_reclaim.kalloc_type_view_1138
- nfs_vnop_remove.kalloc_type_view_4710
- nfs_vnop_remove.kalloc_type_view_4906
- nfs_vnop_setattr.kalloc_type_view_2432
- nfs_vnop_setattr.kalloc_type_view_2476

```
