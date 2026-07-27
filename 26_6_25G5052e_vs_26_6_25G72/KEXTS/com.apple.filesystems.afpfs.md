## com.apple.filesystems.afpfs

> `com.apple.filesystems.afpfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-703.0.0.0.0
-  __TEXT.__cstring: 0xc6b0
+705.0.0.0.0
+  __TEXT.__cstring: 0xc734
   __TEXT.__const: 0x3f0
-  __TEXT_EXEC.__text: 0x380c8
+  __TEXT_EXEC.__text: 0x3811c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2e90
   __DATA.__common: 0xe8

   __DATA_CONST.__kalloc_var: 0x460
   Functions: 781
   Symbols:   1229
-  CStrings:  1203
+  CStrings:  1205
 
Symbols:
+ afpfs_vnop_ioctl.kalloc_type_view_5731
+ afpfs_vnop_ioctl.kalloc_type_view_5746
- afpfs_vnop_ioctl.kalloc_type_view_5719
- afpfs_vnop_ioctl.kalloc_type_view_5734
Functions:
~ _afpfs_vnop_ioctl : 6576 -> 6660
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/LogMessage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bio.subproj/bio_lib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_add.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_blind.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_div.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp2.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_gcd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_lib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mont.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mpi.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_print.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_rand.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_recp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/buffer.subproj/buffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/cryptlib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/err.subproj/err.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/ex_data.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/lhash.subproj/lhash.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/rand.subproj/md_rand.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/OpenSSL/stack.subproj/stack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_catalog.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_encodings.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_reconnect.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_request.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_search.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_vfsutils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_vhash.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/afpfs_vnops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/encrypt_random.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kzkIqt/Sources/afpfs/Sources/recon1.c"
+ "afpfs_ioctl:  cmdBufferLength %u exceeds maximum %zu, clamping.\n"
+ "afpfs_ioctl:  replyBufferLength %u exceeds maximum %zu, clamping.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/LogMessage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bio.subproj/bio_lib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_add.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_blind.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_div.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_exp2.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_gcd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_lib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mont.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_mpi.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_print.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_rand.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/bn.subproj/bn_recp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/buffer.subproj/buffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/cryptlib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/err.subproj/err.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/ex_data.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/lhash.subproj/lhash.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/rand.subproj/md_rand.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/OpenSSL/stack.subproj/stack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_catalog.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_encodings.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_reconnect.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_request.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_search.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_vhash.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/afpfs_vnops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/encrypt_random.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8LdIwd/Sources/afpfs/Sources/recon1.c"
```
