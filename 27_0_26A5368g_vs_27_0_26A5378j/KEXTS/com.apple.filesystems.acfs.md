## com.apple.filesystems.acfs

> `com.apple.filesystems.acfs`

```diff

-  __TEXT.__cstring: 0x37882
+  __TEXT.__cstring: 0x37eb7
   __TEXT.__const: 0x3672
-  __TEXT_EXEC.__text: 0xcf470
-  __TEXT_EXEC.__auth_stubs: 0x1040
+  __TEXT_EXEC.__text: 0xcf048
+  __TEXT_EXEC.__auth_stubs: 0x1030
   __DATA.__data: 0x12498
-  __DATA.__common: 0x613c
+  __DATA.__common: 0x60e4
   __DATA.__bss: 0x10934
-  __DATA_CONST.__const: 0x290
-  __DATA_CONST.__kalloc_type: 0x2c0
-  __DATA_CONST.__auth_got: 0x820
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__kalloc_type: 0x780
+  __DATA_CONST.__auth_got: 0x818
   __DATA_CONST.__got: 0x40
-  Functions: 4089
-  Symbols:   4828
-  CStrings:  5143
+  Functions: 4088
+  Symbols:   4835
+  CStrings:  5164
 
Sections:
~ __TEXT.__const : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _cvfs_ktv_DmigReq
+ _cvfs_ktv_FsmReq
+ _cvfs_ktv_ReqData
+ _cvfs_ktv_ReqNoData
+ _cvfs_ktv_brl
+ _cvfs_ktv_brlra
+ _cvfs_ktv_buf
+ _cvfs_ktv_cvnode
+ _cvfs_ktv_dircache
+ _cvfs_ktv_dircachehash
+ _cvfs_ktv_dirchnk
+ _cvfs_ktv_dirdup
+ _cvfs_ktv_dmigmsgh
+ _cvfs_ktv_dmigsess
+ _cvfs_ktv_dmon
+ _cvfs_ktv_extent
+ _cvfs_ktv_misc
+ _cvfs_ktv_spotlightL
+ _cvfs_ktv_spotlightS
+ _cvfs_zone_ktv
+ _kalloc_data
+ _kalloc_type_impl
+ _kfree_data
+ _kfree_type_impl
- _MdOsTagToUse
- _OSFree
- _OSMalloc
- _OSMalloc_Tagalloc
- _OSMalloc_Tagfree
- _OSMalloc_noblock
- _cvfs_RawZone_1024_Malloc_Tag
- _cvfs_RawZone_128_Malloc_Tag
- _cvfs_RawZone_16_Malloc_Tag
- _cvfs_RawZone_2048_Malloc_Tag
- _cvfs_RawZone_256_Malloc_Tag
- _cvfs_RawZone_32_Malloc_Tag
- _cvfs_RawZone_4096_Malloc_Tag
- _cvfs_RawZone_512_Malloc_Tag
- _cvfs_RawZone_64_Malloc_Tag
- _cvfs_RawZone_fat_Malloc_Tag
- _cvfs_chunk_Malloc_Tag
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/dmiglib/dmig_attributes.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/dmiglib/dmig_events.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/dmiglib/dmig_handles.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/dmiglib/dmig_io.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/dmiglib/dmig_session.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/dmiglib/dmigfs.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/misclib/dmon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/misclib/lock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/misclib/memalloc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/misclib/nomad/md_dmon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/misclib/slidingbucket.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/misclib/utf8.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/cvportmap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/cvproxy_clnt.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/cvproxy_con.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/cvproxy_srv.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/cvproxy_subr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsm_brlops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsm_proxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsm_rtqos.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsm_token.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsm_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsm_vnops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/fsmcom.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/nomad/md_cvproxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/nomad/md_cvsock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/nomad/md_fsmcom.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/recon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/sockinput.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/net/socksubr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/clntrtqos.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/cvdir.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/cvdisk.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/cvnc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/cvpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/cvsock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/cvsubr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/debuglog.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/extapi.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/extent.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/iodesc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_acl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_cvdir.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_debuglog.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_rw.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_rwbuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_rwproxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_subr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/md_vnops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/xsanfs_bulkaccess.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/nomad/xsanfs_spotproxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/quotas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/rtio.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/rw.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/rwproxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/shared/sh_vnops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/vnops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/client/vfs/xattr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/darwinSupport/include/../../qustat/libqustat/libqustat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/include/common/list.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/include/common/rbtree.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f7JD4j/Sources/XsanFS/snfs/include/common/splay.c"
+ "111112221111"
+ "11112111211211222222222222222222222222222222222211111111"
+ "11222121111111111111122"
+ "11222222222222222222222222222222222222222"
+ "11222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "11222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "12111111111111"
+ "133131111"
+ "21112112112111211111111"
+ "21212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121211"
+ "212221111112221"
+ "22111111"
+ "221112112112111211211121112112112212222222222222222222222222222222222122122221121112211122211111111111111111111111121111222111122211111112211111212211212112222222"
+ "2221112112112212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212111"
+ "22222112111211211111111111111111111111111111112122212"
+ "222222221112211"
+ "22222231111"
+ "site.CvNode_t"
+ "site.DmigReq_t"
+ "site.FsmRequest_t"
+ "site.ReqData_t"
+ "site.ReqNoData_t"
+ "site.cl_brl_t"
+ "site.cvExtent_t"
+ "site.cvFsmDirBlock_t"
+ "site.cvbrl_range_t"
+ "site.cvfsBC_t"
+ "site.dd_chunk_t"
+ "site.dir_cache_hash_t"
+ "site.dir_dups_t"
+ "site.dmig_sess_t"
+ "site.dmigfs_msgh_t"
+ "site.dmonReq_t"
+ "site.fseLargeR_t"
+ "site.fseSmallR_t"
+ "site.miscZone_t"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/dmiglib/dmig_attributes.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/dmiglib/dmig_events.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/dmiglib/dmig_handles.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/dmiglib/dmig_io.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/dmiglib/dmig_session.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/dmiglib/dmigfs.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/dmon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/lock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/memalloc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/nomad/md_dmon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/nomad/md_memalloc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/slidingbucket.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/misclib/utf8.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/cvportmap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/cvproxy_clnt.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/cvproxy_con.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/cvproxy_srv.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/cvproxy_subr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsm_brlops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsm_proxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsm_rtqos.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsm_token.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsm_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsm_vnops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/fsmcom.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/nomad/md_cvproxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/nomad/md_cvsock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/nomad/md_fsmcom.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/recon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/sockinput.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/net/socksubr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/clntrtqos.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/cvdir.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/cvdisk.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/cvnc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/cvpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/cvsock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/cvsubr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/debuglog.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/extapi.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/extent.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/iodesc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_acl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_cvdir.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_debuglog.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_rw.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_rwbuf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_rwproxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_subr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/md_vnops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/xsanfs_bulkaccess.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/nomad/xsanfs_spotproxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/quotas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/rtio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/rw.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/rwproxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/shared/sh_vnops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/vnops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/vfs/xattr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/darwinSupport/include/../../qustat/libqustat/libqustat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/include/common/list.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/include/common/rbtree.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/include/common/splay.c"
- "MdOsAlloc: failed alloc for general area."
- "MdOsZoneAlloc: failed alloc for general area."
- "MdOsZoneInit: Cannot create zone <%s>."
- "cvfs_RawZone_1024"
- "cvfs_RawZone_128"
- "cvfs_RawZone_16"
- "cvfs_RawZone_2048"
- "cvfs_RawZone_256"
- "cvfs_RawZone_32"
- "cvfs_RawZone_4096"
- "cvfs_RawZone_512"
- "cvfs_RawZone_64"
- "cvfs_RawZone_Fat"
- "cvfs_chunk"

```
