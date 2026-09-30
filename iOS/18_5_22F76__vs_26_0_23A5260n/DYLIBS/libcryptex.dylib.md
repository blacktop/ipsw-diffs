## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-493.122.1.0.0
-  __TEXT.__text: 0x2515c
-  __TEXT.__auth_stubs: 0x1360
+589.0.1.0.0
+  __TEXT.__text: 0x2570c
+  __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_methlist: 0x490
   __TEXT.__const: 0x7c0
-  __TEXT.__gcc_except_tab: 0xf78
-  __TEXT.__oslogstring: 0x3f36
-  __TEXT.__cstring: 0x1ba0
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__gcc_except_tab: 0xf58
+  __TEXT.__oslogstring: 0x3fc9
+  __TEXT.__cstring: 0x1bcc
+  __TEXT.__unwind_info: 0x5a8
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x9da
   __TEXT.__objc_methtype: 0x360

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x9c0
+  __AUTH_CONST.__auth_got: 0x9c8
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xe18

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
+  - /System/Library/PrivateFrameworks/StorageKit.framework/StorageKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
+  - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib
   - /usr/lib/libcryptex_interface.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AFB6300-FBE2-301C-AC4B-6A85E51F2160
-  Functions: 480
-  Symbols:   1739
-  CStrings:  841
+  UUID: 06ADEB78-4283-388D-BDC1-BB2D9EFDA8C5
+  Functions: 482
+  Symbols:   1727
+  CStrings:  848
 
Symbols:
+ ___block_descriptor_tmp.48
+ _cryptex_attr_set_auth_token
+ _cryptex_attr_set_read_write
+ _cryptex_fcopy_info_plist
+ _cryptex_scrivener_set_auth_token
- ___block_descriptor_tmp.47
- __cryptex_set_actor
Functions:
~ __cryptex_install_core : 1540 -> 1548
~ __cryptex_copy_list : 2160 -> 2168
~ _cryptex_signing_service_trust : 1600 -> 1652
- __cryptex_set_actor
~ __cryptex_populate_cryptex1_properties : 1872 -> 1752
~ _collation_copy_mount_point_for_cryptex_bundle_id : 132 -> 148
~ _cryptex_install2 : 3848 -> 3888
~ _cryptex_personalize2 : 4848 -> 4868
~ _cryptex_fcopy_personalized_manifest2 : 1492 -> 1496
+ _cryptex_fcopy_info_plist
~ __cryptex_attr_dealloc : 60 -> 68
+ _cryptex_attr_set_auth_token
+ _cryptex_attr_set_read_write
CStrings:
+ "%{public}s: Cryptex does not have an info plist. %{darwin.errno}d"
+ "%{public}s: Invalid info plist fd. %{darwin.errno}d"
+ "%{public}s: empty auth token"
+ "%{public}s: failed to alloc buffer"
+ "%{public}s: setting auth token"
+ "589.0.1"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Fri May 23 06:18:00 PDT 2025; root:libcryptex-589.0.1~224/libcryptex/RELEASE_ARM64E"
+ "Ap,SikaFuse"
+ "Darwin Cryptex Interface Version 2.0.0: Fri May 23 06:18:00 PDT 2025; root:libcryptex-589.0.1~224/libcryptex/RELEASE_ARM64E"
+ "UID_MODE"
+ "cryptex_fcopy_info_plist"
- "%{public}s: Performing nonce domain workaround, 0x8 mapped to 0x3"
- "493.122.1"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Sat Apr 19 07:20:34 PDT 2025; root:libcryptex-493.122.1~1/libcryptex/RELEASE_ARM64E"
- "Darwin Cryptex Interface Version 2.0.0: Sat Apr 19 07:20:34 PDT 2025; root:libcryptex-493.122.1~1/libcryptex/RELEASE_ARM64E"

```
