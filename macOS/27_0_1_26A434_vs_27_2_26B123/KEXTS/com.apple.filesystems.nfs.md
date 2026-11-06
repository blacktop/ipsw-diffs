## com.apple.filesystems.nfs

> `com.apple.filesystems.nfs`

```diff

-356.0.6.0.0
-  __TEXT.__cstring: 0x9c42
+356.40.6.0.0
+  __TEXT.__cstring: 0x9c53
   __TEXT.__const: 0x39c
-  __TEXT_EXEC.__text: 0x9e860
+  __TEXT_EXEC.__text: 0x9e9f0
   __TEXT_EXEC.__auth_stubs: 0x1530
   __DATA.__data: 0xf00
   __DATA.__common: 0xee4

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 1003
   Symbols:   1762
-  CStrings:  1156
+  CStrings:  1157
 
Symbols:
+ gss_krb5_destroy_context.kalloc_type_view_2799
+ gss_krb5_make_context.kalloc_type_view_2778
+ gss_krb5_make_context.kalloc_type_view_2781
+ nfs3_vnop_create.kalloc_type_view_4538
+ nfs3_vnop_create.kalloc_type_view_4666
+ nfs3_vnop_mkdir.kalloc_type_view_5646
+ nfs3_vnop_mkdir.kalloc_type_view_5760
+ nfs3_vnop_rmdir.kalloc_type_view_5817
+ nfs3_vnop_rmdir.kalloc_type_view_5893
+ nfs3_vnop_symlink.kalloc_type_view_5457
+ nfs3_vnop_symlink.kalloc_type_view_5577
+ nfs_request_destroy.kalloc_type_view_4551
+ nfs_sillyrename.kalloc_type_view_7084
+ nfs_sillyrename.kalloc_type_view_7143
+ nfs_vnop_reclaim.kalloc_type_view_1181
+ nfs_vnop_remove.kalloc_type_view_4723
+ nfs_vnop_remove.kalloc_type_view_4919
+ nfs_vnop_setattr.kalloc_type_view_2445
+ nfs_vnop_setattr.kalloc_type_view_2489
- gss_krb5_destroy_context.kalloc_type_view_2795
- gss_krb5_make_context.kalloc_type_view_2774
- gss_krb5_make_context.kalloc_type_view_2777
- nfs3_vnop_create.kalloc_type_view_4528
- nfs3_vnop_create.kalloc_type_view_4656
- nfs3_vnop_mkdir.kalloc_type_view_5636
- nfs3_vnop_mkdir.kalloc_type_view_5750
- nfs3_vnop_rmdir.kalloc_type_view_5807
- nfs3_vnop_rmdir.kalloc_type_view_5883
- nfs3_vnop_symlink.kalloc_type_view_5447
- nfs3_vnop_symlink.kalloc_type_view_5567
- nfs_request_destroy.kalloc_type_view_4538
- nfs_sillyrename.kalloc_type_view_7070
- nfs_sillyrename.kalloc_type_view_7129
- nfs_vnop_reclaim.kalloc_type_view_1164
- nfs_vnop_remove.kalloc_type_view_4713
- nfs_vnop_remove.kalloc_type_view_4909
- nfs_vnop_setattr.kalloc_type_view_2435
- nfs_vnop_setattr.kalloc_type_view_2479
Functions:
~ _nfs_recover : 3476 -> 3524
~ _nfs_request_match_reply : 1324 -> 1392
~ _nfs_wait_reply -> _nfs_request_ref : 568 -> 124
~ _nfs_noremotehang -> _nfs_wait_reply : 52 -> 568
~ _nfs_request_create -> _nfs_noremotehang : 892 -> 52
~ _nfs_request_destroy -> _nfs_request_create : 968 -> 892
~ _nfs_request_ref -> _nfs_request_destroy : 124 -> 968
~ _nfs_request_finish : 2944 -> 2948
~ _nfs_vnop_reclaim : 3468 -> 3604
~ _nfs_refresh_fh : 1316 -> 1328
~ _nfs_dir_buf_freespace : 52 -> 64
~ _nfs3_readdir_rpc : 4764 -> 4848
~ _nfs_vnop_pageout : 4820 -> 4840
~ _mbuf_walk : 608 -> 624
CStrings:
+ "nfswaitdelegscan"
```
