## com.apple.filesystems.afpfs

> `com.apple.filesystems.afpfs`

```diff

-693.0.0.0.0
-  __TEXT.__cstring: 0xc36a
-  __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x39514
+695.0.0.0.0
+  __TEXT.__cstring: 0xc339
+  __TEXT.__const: 0x410
+  __TEXT_EXEC.__text: 0x39bf4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2e90
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x138
   __DATA_CONST.__kalloc_type: 0x1fc0
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: FDF3F078-F4CD-38E5-8229-19D561E0FAD0
-  Functions: 821
-  Symbols:   1348
-  CStrings:  1206
+  UUID: 1EFAF7F2-45B5-3322-AB8F-2609A9B96046
+  Functions: 765
+  Symbols:   1316
+  CStrings:  1205
 
Symbols:
- DisconnectOldSessions.cold.3
- DoRecon1Reconnect.cold.4
- ERR_add_error_data.cold.3
- ERR_add_error_data.cold.4
- GetExtendedAttributes.cold.2
- LogInClearText.cold.4
- OpenSession.cold.2
- RefreshCredential.cold.3
- RefreshCredential.cold.4
- RefreshCredential.cold.5
- RemoveExtendedAttribute.cold.3
- SetExtendedAttributes.cold.3
- SetExtendedAttributes.cold.4
- SetFileDirParms.cold.3
- afpfs_CatalogCopyFile.cold.3
- afpfs_CatalogCopyFile.cold.4
- afpfs_CreateCatalogNode.cold.3
- afpfs_DeleteCatalogNode.cold.2
- afpfs_ExchangeFileIDs.cold.3
- afpfs_ExchangeFileIDs.cold.4
- afpfs_LookupCatalogNode.cold.2
- afpfs_MoveRenameCatalogNode.cold.3
- afpfs_MoveRenameCatalogNode.cold.4
- afpfs_SRPLogin.cold.2
- afpfs_UpdateCatalogNode.cold.3
- afpfs_makenode.cold.2
- afpfs_sysctl.cold.3
- lh_delete.cold.2
- lh_insert.cold.3
- sk_dup.cold.2
- sk_dup.cold.3
- sk_insert.cold.2
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/LogMessage.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bio.subproj/bio_lib.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_add.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_blind.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_div.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp2.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_gcd.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_lib.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mont.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mpi.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_print.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_rand.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_recp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/buffer.subproj/buffer.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/cryptlib.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/err.subproj/err.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/ex_data.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/lhash.subproj/lhash.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/rand.subproj/md_rand.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/stack.subproj/stack.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_catalog.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_encodings.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_reconnect.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_request.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_search.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsutils.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vhash.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vnops.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_xattr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/encrypt_random.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/recon1.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/LogMessage.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bio.subproj/bio_lib.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_add.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_blind.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_div.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp2.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_gcd.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_lib.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mont.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mpi.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_print.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_rand.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_recp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/buffer.subproj/buffer.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/cryptlib.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/err.subproj/err.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/ex_data.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/lhash.subproj/lhash.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/rand.subproj/md_rand.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/OpenSSL/stack.subproj/stack.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_catalog.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_encodings.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_reconnect.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_request.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_search.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vhash.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_vnops.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/afpfs_xattr.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/encrypt_random.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/afpfs/Sources/recon1.c"
- "afpfs_MountAFPVolume:  unknown try attempt 0x%x\n"

```
