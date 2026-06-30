## acfs.util

> `/System/Library/Filesystems/acfs.fs/Contents/Resources/acfs.util`

```diff

 804.100.3.0.0
   __TEXT.__text: 0x1da80 sha256:cee1fba442bed2140f14a385eb01a9c6d7ebdc39e466961d3c63bacb37c69558
   __TEXT.__auth_stubs: 0x8e0 sha256:5af1f5cbe7288090089cf4f61ff15f9a14d7a74d1018ff5f9784e6adf8fddc76
-  __TEXT.__cstring: 0x6691 sha256:76bd66761029fec774fe0f17d6cc23253feef637ccecd9d13b67971feb809690
+  __TEXT.__cstring: 0x6691 sha256:b172558f7147398a692ed61bea38b0ae0d69496a18502123dd2c36ff4c89ca03
   __TEXT.__const: 0x305c sha256:0fab021b239305a7688e03c8e8c1e99bc83b82f22682c1de023b855b35d7f74f
   __TEXT.__unwind_info: 0x568 sha256:05153e3d3031f712768f2f67074cdf2513a8fa20dc366784c3f3a46f7b51e1fd
   __DATA_CONST.__auth_got: 0x470 sha256:86de2f0b4d923ccc137a61e69f4abe4dca197d00c25c735748607d25f9461317

   __DATA_CONST.__auth_ptr: 0x10 sha256:466d00c6308a17f586604c2cfa68b7ac66793b0dbcdcf422545248428bdc7529
   __DATA_CONST.__cfstring: 0x460 sha256:3f34e4997aa852350a5cd43f87329e589ab851cc925242926abd78e1373f8d30
   __DATA.__data: 0x2a78 sha256:820cf89130205969572dd5017ad6f8b33066a55914b0eeebfae6fe7f21394d45
-  __DATA.__common: 0x10310 sha256:e3d0cd3a750e31dd7caa4a8043b45a6af14ad0f24fec388a463dbac0fc1caec4
-  __DATA.__bss: 0x7265 sha256:792089ab0142d5c62b28c138679cd707a3375807cdc498cf8473bc1d643b8037
+  __DATA.__common: 0x10310 sha256:80c6f634300b2f931307229402e64ad9a13c85803c093bce071f0e57b93d0611
+  __DATA.__bss: 0x7265 sha256:993e364edce58dc3aec397e98503f1a7a21ae9ed7e509626a9aedbf15d25ccf0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: F829C4E6-58DC-351E-97BD-DE3D4FF54A79
+  UUID: 395188C9-D55A-3F1E-B87F-D5F37C6955A1
   Functions: 444
   Symbols:   2891
   CStrings:  953
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(auth_connection.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(auth_globals.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(md5.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(utilities.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../extapi/libcvextapi.a(cvapi.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(disks.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(dk_nomad.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(do_sum.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(efi_gpt.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(efi_util.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(snfs_cverr.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libglobals-static.a(globals.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(altpmap.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(fsmcomm.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(pxsubr.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(rerecv.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libcrc32-static.a(crc32.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(alloc.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(brandcfg.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(cvras.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(dopanic.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(fmt_syserror.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(fsports.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(getroot.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(list.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(logger.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(pollutil.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(rawip.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(resolvshim.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(sn_fsname.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(snprintf.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(sock46.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(subr2.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(timer.c.o)
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/CMakeFiles/acfs.util.dir/acfsutil.c.o
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/authlib/
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/client/util/nomad/acfs.util/
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/extapi/
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/fsmlib/
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/include/common/
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libfsmcomm/
+ /AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libutil/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(auth_connection.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(auth_globals.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(md5.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../authlib/libcvfsauth.a(utilities.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../extapi/libcvextapi.a(cvapi.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(disks.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(dk_nomad.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(do_sum.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(efi_gpt.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(efi_util.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libfsmlib-static.a(snfs_cverr.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../fsmlib/libglobals-static.a(globals.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(altpmap.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(fsmcomm.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(pxsubr.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libfsmcomm/libfsmcomm-static.a(rerecv.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libcrc32-static.a(crc32.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(alloc.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(brandcfg.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(cvras.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(dopanic.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(fmt_syserror.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(fsports.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(getroot.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(list.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(logger.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(pollutil.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(rawip.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(resolvshim.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(sn_fsname.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(snprintf.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(sock46.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(subr2.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/../../../../libutil/libsnutil-static.a(timer.c.o)
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Binaries/XsanFS/install/TempContent/Objects/snfs/client/util/nomad/acfs.util/CMakeFiles/acfs.util.dir/acfsutil.c.o
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/authlib/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/client/util/nomad/acfs.util/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/extapi/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/fsmlib/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/include/common/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libfsmcomm/
- /AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libutil/
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/fsmlib/disks.c"
+ "/AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libfsmcomm/fsmcomm.c"
+ "/AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libutil/alloc.c"
+ "/AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libutil/cvras.c"
+ "/AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libutil/pollutil.c"
+ "/AppleInternal/Library/BuildRoots/4~CSESugCUJPzMi_niV4vww7ibB8sK2e-K30Sp2Dg/Library/Caches/com.apple.xbs/TemporaryDirectory.RZsLdn/Sources/XsanFS/snfs/libutil/sock46.c"
- "/AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/fsmlib/disks.c"
- "/AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libfsmcomm/fsmcomm.c"
- "/AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libutil/alloc.c"
- "/AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libutil/cvras.c"
- "/AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libutil/pollutil.c"
- "/AppleInternal/Library/BuildRoots/4~CRehugArstVfuCKng82HZGYnclZNjzZZyzAQZrs/Library/Caches/com.apple.xbs/TemporaryDirectory.FJuDpI/Sources/XsanFS/snfs/libutil/sock46.c"

```
