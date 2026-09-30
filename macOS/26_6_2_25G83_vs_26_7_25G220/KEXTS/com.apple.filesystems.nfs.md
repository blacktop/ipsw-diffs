## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

```diff

-343.160.4.0.0
+343.160.4.701.3
   __TEXT.__cstring: 0x9c42
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9d218
+  __TEXT_EXEC.__text: 0x9d294
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4
Symbols:
+ gss_krb5_destroy_context.kalloc_type_view_2795
+ gss_krb5_make_context.kalloc_type_view_2774
+ gss_krb5_make_context.kalloc_type_view_2777
+ nfs3_vnop_create.kalloc_type_view_4522
+ nfs3_vnop_create.kalloc_type_view_4650
+ nfs3_vnop_mkdir.kalloc_type_view_5630
+ nfs3_vnop_mkdir.kalloc_type_view_5744
+ nfs3_vnop_rmdir.kalloc_type_view_5801
+ nfs3_vnop_rmdir.kalloc_type_view_5877
+ nfs3_vnop_symlink.kalloc_type_view_5441
+ nfs3_vnop_symlink.kalloc_type_view_5561
+ nfs4_create_rpc.kalloc_type_view_7716
+ nfs4_create_rpc.kalloc_type_view_7847
+ nfs4_open_rpc_internal.kalloc_type_view_5696
+ nfs4_open_rpc_internal.kalloc_type_view_6055
+ nfs4_vnop_rmdir.kalloc_type_view_8176
+ nfs4_vnop_rmdir.kalloc_type_view_8213
+ nfs_file_lock_alloc.kalloc_type_view_3846
+ nfs_file_lock_destroy.kalloc_type_view_3864
+ nfs_gss_clnt_ctx_copy.kalloc_type_view_2368
+ nfs_gss_clnt_ctx_copy.kalloc_type_view_2372
+ nfs_gss_clnt_ctx_destroy.kalloc_type_view_2429
+ nfs_gss_clnt_rpcdone.kalloc_type_view_2145
+ nfs_lock_owner_destroy.kalloc_type_view_3699
+ nfs_lock_owner_find.kalloc_type_view_3659
+ nfs_open_file_destroy.kalloc_type_view_2453
+ nfs_open_file_find_internal.kalloc_type_view_2396
+ nfs_open_owner_destroy.kalloc_type_view_2193
+ nfs_open_owner_find.kalloc_type_view_2152
+ nfs_sillyrename.kalloc_type_view_7064
+ nfs_sillyrename.kalloc_type_view_7123
+ nfs_vnop_remove.kalloc_type_view_4707
+ nfs_vnop_remove.kalloc_type_view_4903
- gss_krb5_destroy_context.kalloc_type_view_2791
- gss_krb5_make_context.kalloc_type_view_2770
- gss_krb5_make_context.kalloc_type_view_2773
- nfs3_vnop_create.kalloc_type_view_4516
- nfs3_vnop_create.kalloc_type_view_4644
- nfs3_vnop_mkdir.kalloc_type_view_5624
- nfs3_vnop_mkdir.kalloc_type_view_5738
- nfs3_vnop_rmdir.kalloc_type_view_5795
- nfs3_vnop_rmdir.kalloc_type_view_5871
- nfs3_vnop_symlink.kalloc_type_view_5435
- nfs3_vnop_symlink.kalloc_type_view_5555
- nfs4_create_rpc.kalloc_type_view_7710
- nfs4_create_rpc.kalloc_type_view_7841
- nfs4_open_rpc_internal.kalloc_type_view_5692
- nfs4_open_rpc_internal.kalloc_type_view_6051
- nfs4_vnop_rmdir.kalloc_type_view_8170
- nfs4_vnop_rmdir.kalloc_type_view_8207
- nfs_file_lock_alloc.kalloc_type_view_3842
- nfs_file_lock_destroy.kalloc_type_view_3860
- nfs_gss_clnt_ctx_copy.kalloc_type_view_2362
- nfs_gss_clnt_ctx_copy.kalloc_type_view_2366
- nfs_gss_clnt_ctx_destroy.kalloc_type_view_2423
- nfs_gss_clnt_rpcdone.kalloc_type_view_2139
- nfs_lock_owner_destroy.kalloc_type_view_3695
- nfs_lock_owner_find.kalloc_type_view_3655
- nfs_open_file_destroy.kalloc_type_view_2449
- nfs_open_file_find_internal.kalloc_type_view_2392
- nfs_open_owner_destroy.kalloc_type_view_2189
- nfs_open_owner_find.kalloc_type_view_2148
- nfs_sillyrename.kalloc_type_view_7058
- nfs_sillyrename.kalloc_type_view_7117
- nfs_vnop_remove.kalloc_type_view_4701
- nfs_vnop_remove.kalloc_type_view_4897
Functions:
~ _nfs_gss_clnt_ctx_init_retry : 5572 -> 5600
~ _nfs4_write_rpc_async_finish : 1984 -> 1996
~ _nfs4_claim_delegated_open_rpc : 9684 -> 9736
~ _nfs_write_rpc : 1604 -> 1608
~ _nfs3_write_rpc_async_finish : 1148 -> 1144
~ _krb5_crypt_mbuf : 792 -> 824
```
