## MobileDevice

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__dof_MobileDev`
- `__TEXT.__dof_afc`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__objc_classrefs`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1860.0.0.0.0
-  __TEXT.__text: 0x2b7b38
+1860.0.1.0.0
+  __TEXT.__text: 0x2b7f98
   __TEXT.__objc_methlist: 0x3fbc
-  __TEXT.__const: 0x10c0a8
-  __TEXT.__cstring: 0x7aa8b
-  __TEXT.__gcc_except_tab: 0x52b0
+  __TEXT.__const: 0x10c108
+  __TEXT.__cstring: 0x7aa9b
+  __TEXT.__gcc_except_tab: 0x5330
   __TEXT.__oslogstring: 0xf37
   __TEXT.__ustring: 0xb0
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__dof_MobileDev: 0x1ac1
   __TEXT.__dof_afc: 0x6d7
-  __TEXT.__unwind_info: 0x6ef0
+  __TEXT.__unwind_info: 0x6f18
   __TEXT.__eh_frame: 0x66c
   __TEXT.__objc_stubs: 0x5e00
-  __TEXT.__auth_stubs: 0x4190
+  __TEXT.__auth_stubs: 0x41a0
   __TEXT.__objc_classname: 0xe2f
   __TEXT.__objc_methname: 0x7711
   __TEXT.__objc_methtype: 0x2782

   __AUTH_CONST.__cfstring: 0x40320
   __AUTH_CONST.__objc_const: 0x74e0
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x20c0
+  __AUTH_CONST.__auth_got: 0x20c8
   __AUTH.__objc_data: 0x1a40
   __AUTH.__data: 0x338
   __AUTH.__thread_vars: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libssl.35.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10384
-  Symbols:   14643
+  Functions: 10383
+  Symbols:   14645
   CStrings:  16932
 
Symbols:
+ _AMAuthInstallErrorFromAMSupportError
+ __ZN11ACFULogging14getUpdaterNameEv
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
- _ZN9ACFUError10getCFErrorEv
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2nm7JH/Sources/MobileInstallation_host/patch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4LGXc9/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C3MUkH/Sources/PurpleReverseProxy_host/Common/RPSocket.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C3MUkH/Sources/PurpleReverseProxy_host/Common/Utilities.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C3MUkH/Sources/PurpleReverseProxy_host/ReverseProxyHost/ReverseProxyHost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.C3MUkH/Sources/PurpleReverseProxy_host/Socks5/Socks5Server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JWgBRS/Sources/MobileDevice/Source/AMDevicePowerAssertion.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XZue6L/Sources/VeridianDylibs/T200RestoreInfo/T200RestoreInfo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XZue6L/Sources/VeridianDylibs/T200Updater/T200UpdaterPrivateHelper.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mYwtL7/Sources/AppleFileConduit/afc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mYwtL7/Sources/AppleFileConduit/client-async.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mYwtL7/Sources/AppleFileConduit/client-sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mYwtL7/Sources/AppleFileConduit/connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mYwtL7/Sources/AppleFileConduit/platform.c"
+ "1860.0.1"
+ "Helsinki_Restore_Host-58.0.44"
+ "copying+removing %s -> %s"
+ "libauthinstall-1155.0.4"
+ "removefile() failed: %d"
+ "restore library built Jul 16 2026 at 00:01:24"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CN4oW8/Sources/VeridianDylibs/T200RestoreInfo/T200RestoreInfo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CN4oW8/Sources/VeridianDylibs/T200Updater/T200UpdaterPrivateHelper.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KCqARo/Sources/MobileInstallation_host/patch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/Common/RPSocket.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/Common/Utilities.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/ReverseProxyHost/ReverseProxyHost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/Socks5/Socks5Server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGGYNh/Sources/MobileDevice/Source/AMDevicePowerAssertion.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/afc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/client-async.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/client-sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/platform.c"
- "1860"
- "Helsinki_Restore_Host-58.0.42"
- "libauthinstall-1155.0.3"
- "rename() failed: %d"
- "renaming %s -> %s"
- "restore library built Jun 26 2026 at 19:26:41"
```
