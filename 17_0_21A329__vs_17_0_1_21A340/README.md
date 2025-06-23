# 17.0 (21A329) .vs 17.0.1 (21A340)

## IPSWs

- `iPhone15,2_17.0_21A329_Restore.ipsw`
- `iPhone15,2_17.0.1_21A340_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.0 *(21A329)* | 23.0.0 | 10002.2.11~1 | Thu, 24Aug2023 20:19:01 PDT |
| 17.0.1 *(21A340)* | 23.0.0 | 10002.2.12~1 | Fri, 15Sep2023 13:43:33 PDT |

### Kexts

#### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.kernel`

```diff

-10002.2.11.0.0
+10002.2.12.0.0
   __TEXT.__const: 0x34970
   __TEXT.__copyio_vectors: 0xf0
   __TEXT.__cstring: 0x61d15

   __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc88
-  __TEXT_EXEC.__text: 0x736cac
+  __TEXT_EXEC.__text: 0x736ca4
   __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
   __KLD.__text: 0x1630
   __LASTDATA_CONST.__mod_init_func: 0x8

```

>  `com.apple.kext.CoreTrust`

```diff

-135.0.0.0.0
+135.2.1.0.0
   __TEXT.__const: 0xe80
   __TEXT.__cstring: 0x52
-  __TEXT_EXEC.__text: 0x7eb4
+  __TEXT_EXEC.__text: 0x7f24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x10

```

</details>

## MachO

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### imagent

>  `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1261.100.4.2.30
+1261.100.4.2.33
   __TEXT.__text: 0x7ed50
   __TEXT.__auth_stubs: 0x1670
   __TEXT.__objc_stubs: 0x7480
   __TEXT.__objc_methlist: 0x27e8
   __TEXT.__const: 0xdd4
   __TEXT.__gcc_except_tab: 0x6b3c
-  __TEXT.__cstring: 0x8021
+  __TEXT.__cstring: 0x8011
   __TEXT.__oslogstring: 0x6a54
   __TEXT.__objc_methname: 0xe684
   __TEXT.__objc_classname: 0x8cb

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1374
   Symbols:   574
-  CStrings:  3412
+  CStrings:  3411
 
CStrings:
+ "14:35:38"
+ "Sep 15 2023"
- "20:59:54"
- "20:59:55"
- "Aug 23 2023"

```

#### Maps

>  `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0xc1131c
+  __TEXT.__text: 0xc11170
   __TEXT.__auth_stubs: 0x6c10
-  __TEXT.__objc_stubs: 0xed360
-  __TEXT.__objc_methlist: 0xa33c4
+  __TEXT.__objc_stubs: 0xed340
+  __TEXT.__objc_methlist: 0xa33bc
   __TEXT.__const: 0xd348
-  __TEXT.__objc_methname: 0x164c18
+  __TEXT.__objc_methname: 0x164bfb
   __TEXT.__swift5_typeref: 0x116ca
   __TEXT.__cstring: 0x866ba
   __TEXT.__constg_swiftt: 0x57a8

   __TEXT.__swift5_proto: 0x424
   __TEXT.__swift5_types: 0x498
   __TEXT.__objc_classname: 0x1cd09
-  __TEXT.__objc_methtype: 0x37f86
+  __TEXT.__objc_methtype: 0x37f92
   __TEXT.__swift5_mpenum: 0x68
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__oslogstring: 0x50b64
+  __TEXT.__oslogstring: 0x50b5d
   __TEXT.__gcc_except_tab: 0x14290
   __TEXT.__ustring: 0x156c
   __TEXT.__dlopen_cstrs: 0x13b
-  __TEXT.__unwind_info: 0x2e010
+  __TEXT.__unwind_info: 0x2dff8
   __DATA_CONST.__auth_got: 0x3618
   __DATA_CONST.__got: 0x25a0
   __DATA_CONST.__auth_ptr: 0x280

   __DATA_CONST.__objc_dictobj: 0x730
   __DATA_CONST.__objc_doubleobj: 0x5b0
   __DATA_CONST.__objc_floatobj: 0x150
-  __DATA.__objc_const: 0x171f10
-  __DATA.__objc_selrefs: 0x45668
+  __DATA.__objc_const: 0x171ef0
+  __DATA.__objc_selrefs: 0x45660
   __DATA.__objc_protorefs: 0x988
   __DATA.__objc_classrefs: 0x7740
   __DATA.__objc_superrefs: 0x47f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 70021
+  Functions: 70019
   Symbols:   4532
-  CStrings:  86756
+  CStrings:  86754
 
CStrings:
+ "navigationListener:didUpdateManeuvers:laneGuidances:"
+ "navigationListener:didUpdateManeuvers:laneGuidances: maneuver count: %lu laneGuidance count: %lu"
+ "v40@0:8@\"CarMetadataNavigationListener\"16@\"NSArray\"24@\"NSArray\"32"
- "navigationListener:didUpdateLaneGuidances:"
- "navigationListener:didUpdateLaneGuidances: count: %lu"
- "navigationListener:didUpdateManeuvers:"
- "navigationListener:didUpdateManeuvers: count: %lu"
- "v32@0:8@\"CarMetadataNavigationListener\"16@\"NSArray\"24"

```

#### cryptexd

>  `/usr/libexec/cryptexd`

```diff

   __TEXT.__objc_methname: 0x15ae
   __TEXT.__objc_classname: 0xf8
   __TEXT.__objc_methtype: 0x3ae
-  __TEXT.__cstring: 0x2202
+  __TEXT.__cstring: 0x2204
   __TEXT.__oslogstring: 0x724b
   __TEXT.__unwind_info: 0x910
   __DATA_CONST.__auth_got: 0xe08
CStrings:
+ "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Fri Sep 15 13:46:17 PDT 2023; root:libcryptex_executables-369.0.11~121/cryptexd/RELEASE_ARM64E"
+ "Darwin Cryptex Manager Version 2.0.0: Fri Sep 15 13:46:17 PDT 2023; root:libcryptex_executables-369.0.11~121/cryptexd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Cryptex Manager Version 2.0.0: Wed Aug  9 06:18:22 PDT 2023; root:libcryptex_executables-369.0.11~48/cryptexd/RELEASE_ARM64E"
- "Darwin Cryptex Manager Version 2.0.0: Wed Aug  9 06:18:22 PDT 2023; root:libcryptex_executables-369.0.11~48/cryptexd/RELEASE_ARM64E"

```

#### inboxupdaterd

>  `/usr/libexec/inboxupdaterd`

```diff

 42.0.0.0.0
-  __TEXT.__text: 0x42414
+  __TEXT.__text: 0x4246c
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_stubs: 0x4220
   __TEXT.__objc_methlist: 0x192c

```

#### mobileactivationd

>  `/usr/libexec/mobileactivationd`

```diff

 898.0.10.0.0
-  __TEXT.__text: 0x1e85f4
+  __TEXT.__text: 0x1e864c
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_stubs: 0x2d20
   __TEXT.__objc_methlist: 0x9f4
Symbols:
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/4a252cd4-3693-11ee-95db-7a03568b17ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
CStrings:
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-898.0.10 built on Sep 15 2023 at 13:58:32)"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-898.0.10 built on Aug  9 2023 at 06:32:25)"

```


</details>

## Firmware

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

   __TEXT.__chain_starts: 0x38
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x65c0
-  __TEXT_EXEC.__text: 0x375e4
+  __TEXT_EXEC.__text: 0x37650
   __TEXT_BOOT_EXEC.__text: 0x4084
   __TEXT_BOOT_EXEC.__bootcode: 0x20
   __DATA.__data: 0x38

```

#### txm.iphoneos.research.im4p

>  `txm.iphoneos.research.im4p`

```diff

   __TEXT.__chain_starts: 0x38
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x65c0
-  __TEXT_EXEC.__text: 0x37504
+  __TEXT_EXEC.__text: 0x37570
   __TEXT_BOOT_EXEC.__text: 0x4084
   __TEXT_BOOT_EXEC.__bootcode: 0x20
   __DATA.__data: 0x38

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.0 *(21A329)* | 616.1.27.10.13 |
| 17.0.1 *(21A340)* | 616.1.27.10.15 |

### Dylibs

#### ⬆️ Updated (17)

<details>
  <summary><i>View Updated</i></summary>

#### libvDSP.dylib

>  `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib`

```diff

 1041.0.0.0.0
   __TEXT.__text: 0xe742c
-  __TEXT.__stubs: 0xa8
   __TEXT.__auth_stubs: 0x260
+  __TEXT.__stubs: 0xa8
   __TEXT.__resolver_help: 0x578
   __TEXT.__const: 0x47e0
   __TEXT.__unwind_info: 0x10e8

```

#### JavaScriptCore

>  `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-616.1.27.10.13
-  __TEXT.__text: 0x15bfbd8
+616.1.27.10.15
+  __TEXT.__text: 0x15c12f8
   __TEXT.__auth_stubs: 0x2bd0
   __TEXT.__objc_methlist: 0x950
   __TEXT.__const: 0x7d128
CStrings:
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__utility/unreachable.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/array"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/optional"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/string"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__utility/unreachable.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/array"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/optional"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/string"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/2a6f8d19-40df-11ee-90b0-aead88ae2785/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"

```

#### SafariServices

>  `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-616.1.27.10.13
-  __TEXT.__text: 0x184d94
+616.1.27.10.15
+  __TEXT.__text: 0x1850bc
   __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0x15138
+  __TEXT.__objc_methlist: 0x15150
   __TEXT.__const: 0x3ee8
-  __TEXT.__cstring: 0x101a0
+  __TEXT.__cstring: 0x101b3
   __TEXT.__gcc_except_tab: 0xc894
-  __TEXT.__oslogstring: 0x85ca
+  __TEXT.__oslogstring: 0x8628
   __TEXT.__ustring: 0x33d4
   __TEXT.__dlopen_cstrs: 0x795
-  __TEXT.__unwind_info: 0x8a54
+  __TEXT.__unwind_info: 0x8a50
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x4e6a
-  __TEXT.__objc_methname: 0x58ead
+  __TEXT.__objc_methname: 0x58f65
   __TEXT.__objc_methtype: 0x11fd3
-  __TEXT.__objc_stubs: 0x36660
+  __TEXT.__objc_stubs: 0x366c0
   __DATA_CONST.__got: 0xc90
-  __DATA_CONST.__const: 0x6af0
+  __DATA_CONST.__const: 0x6b18
   __DATA_CONST.__objc_classlist: 0xae8
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x848
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x31158
-  __DATA_CONST.__objc_selrefs: 0x102f0
+  __DATA_CONST.__objc_const: 0x31198
+  __DATA_CONST.__objc_selrefs: 0x10308
   __DATA_CONST.__objc_arraydata: 0x760
   __AUTH_CONST.__cfstring: 0xe1e0
   __AUTH_CONST.__const: 0x18d8

   __DATA.__objc_protorefs: 0xe8
   __DATA.__objc_classrefs: 0x1958
   __DATA.__objc_superrefs: 0x980
-  __DATA.__objc_ivar: 0x21cc
+  __DATA.__objc_ivar: 0x21d4
   __DATA.__data: 0x6420
   __DATA.__bss: 0x840
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 9261
-  Symbols:   35647
-  CStrings:  16856
+  Functions: 9265
+  Symbols:   35661
+  CStrings:  16863
 
Symbols:
+ -[SFSharedAccountsGroupMemberPickerViewController _cachedIsRecipientEligible:]
+ -[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipient:completionHandler:]
+ -[SFSharedAccountsGroupMemberPickerViewController _hasEligibilityCachedForRecipient:]
+ -[SFSharedAccountsGroupMemberPickerViewController _updatePreferredHandleForRecipientIfNecessary:]
+ _OBJC_IVAR_$_SFSharedAccountsGroupMemberPickerViewController._addressesCurrentlyBeingCheckedForAvailability
+ _OBJC_IVAR_$_SFSharedAccountsGroupMemberPickerViewController._addressesThatHaveBeenFetched
+ ___78-[SFSharedAccountsGroupMemberPickerViewController _cachedIsRecipientEligible:]_block_invoke
+ ___85-[SFSharedAccountsGroupMemberPickerViewController _hasEligibilityCachedForRecipient:]_block_invoke
+ ___97-[SFSharedAccountsGroupMemberPickerViewController _updatePreferredHandleForRecipientIfNecessary:]_block_invoke
+ ___99-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipient:completionHandler:]_block_invoke
+ ___99-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipient:completionHandler:]_block_invoke.34
+ ___99-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipient:completionHandler:]_block_invoke_2
+ ___99-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipient:completionHandler:]_block_invoke_2.35
+ ___99-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipient:completionHandler:]_block_invoke_2.35.cold.1
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
+ _objc_msgSend$_cachedIsRecipientEligible:
+ _objc_msgSend$_fetchEligibilityForRecipient:completionHandler:
+ _objc_msgSend$_hasEligibilityCachedForRecipient:
+ _objc_msgSend$_updatePreferredHandleForRecipientIfNecessary:
+ _objc_msgSend$setPreferredRecipient:forRecipient:
- -[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipients:completionHandler:]
- -[SFSharedAccountsGroupMemberPickerViewController _hasEligibilityCachedForAllRecipients:]
- ___100-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipients:completionHandler:]_block_invoke
- ___100-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipients:completionHandler:]_block_invoke_2
- ___100-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipients:completionHandler:]_block_invoke_3
- ___100-[SFSharedAccountsGroupMemberPickerViewController _fetchEligibilityForRecipients:completionHandler:]_block_invoke_3.cold.1
- ___89-[SFSharedAccountsGroupMemberPickerViewController _hasEligibilityCachedForAllRecipients:]_block_invoke
- ___91-[SFSharedAccountsGroupMemberPickerViewController consumeAutocompleteSearchResults:taskID:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- _objc_msgSend$_fetchEligibilityForRecipients:completionHandler:
- _objc_msgSend$_hasEligibilityCachedForAllRecipients:
CStrings:
+ "B16@?0@\"NSString\"8"
+ "SFSharedAccountsGroupMemberPickerViewController has tried to fetch %lu unique handles so far."
+ "_addressesCurrentlyBeingCheckedForAvailability"
+ "_addressesThatHaveBeenFetched"
+ "_cachedIsRecipientEligible:"
+ "_fetchEligibilityForRecipient:completionHandler:"
+ "_hasEligibilityCachedForRecipient:"
+ "_updatePreferredHandleForRecipientIfNecessary:"
+ "setPreferredRecipient:forRecipient:"
- "_fetchEligibilityForRecipients:completionHandler:"
- "_hasEligibilityCachedForAllRecipients:"

```

#### Security

>  `/System/Library/Frameworks/Security.framework/Security`

```diff

 61040.2.2.0.0
-  __TEXT.__text: 0x153f70
+  __TEXT.__text: 0x153fd4
   __TEXT.__auth_stubs: 0x3a80
   __TEXT.__objc_methlist: 0x42e4
   __TEXT.__const: 0x85b2

```

#### SMS

>  `/System/Library/Messages/PlugIns/SMS.imservice/SMS`

```diff

-1261.100.4.2.30
-  __TEXT.__text: 0x641c8
+1261.100.4.2.33
+  __TEXT.__text: 0x641bc
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_methlist: 0x125c
   __TEXT.__const: 0xa0

```

#### AppleKeyStore

>  `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

 1555.2.2.0.0
-  __TEXT.__text: 0x297b0
+  __TEXT.__text: 0x29808
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__const: 0x27b0
   __TEXT.__cstring: 0x21c0

```

#### AuthKit

>  `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

 458.1.1.7.0
-  __TEXT.__text: 0xab7b0
+  __TEXT.__text: 0xab808
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x9540
   __TEXT.__const: 0x1760

```

#### CoreRepairCore

>  `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

 376.0.3.0.0
-  __TEXT.__text: 0x4d3c0
+  __TEXT.__text: 0x4d3e0
   __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_methlist: 0x1e44
   __TEXT.__const: 0x1178

```

#### IntelligencePlatformCore

>  `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

 75.0.3.2.0
-  __TEXT.__text: 0xaa27c8
+  __TEXT.__text: 0xaa3810
   __TEXT.__auth_stubs: 0x8fa0
   __TEXT.__objc_methlist: 0x1524
-  __TEXT.__const: 0x58d89
+  __TEXT.__const: 0x58d99
   __TEXT.__swift5_typeref: 0x1958e
-  __TEXT.__cstring: 0x540c2
+  __TEXT.__cstring: 0x540d2
   __TEXT.__constg_swiftt: 0x1e0b4
   __TEXT.__swift5_reflstr: 0x2310c
   __TEXT.__swift5_fieldmd: 0x1e1d4

   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__oslogstring: 0x385
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__unwind_info: 0x28d20
-  __TEXT.__eh_frame: 0x54924
+  __TEXT.__unwind_info: 0x28d1c
+  __TEXT.__eh_frame: 0x54964
   __TEXT.__objc_classname: 0x470
   __TEXT.__objc_methname: 0x8958
   __TEXT.__objc_methtype: 0x1f4d

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 69897
+  Functions: 69900
   Symbols:   755
   CStrings:  8629
 

```

#### MFAAuthentication

>  `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

 898.2.3.0.0
-  __TEXT.__text: 0x3d5b8
+  __TEXT.__text: 0x3d610
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x5e000

```

#### MobileInBoxUpdate

>  `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

 42.0.0.0.0
-  __TEXT.__text: 0x1008c
+  __TEXT.__text: 0x100e4
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0x12e0

```

#### PhotosGraph

>  `/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph`

```diff

 608.1.119.0.0
-  __TEXT.__text: 0x5f3740
-  __TEXT.__auth_stubs: 0x3960
+  __TEXT.__text: 0x5f39bc
+  __TEXT.__auth_stubs: 0x39d0
   __TEXT.__objc_methlist: 0x2bff4
   __TEXT.__const: 0x151b6
   __TEXT.__swift5_typeref: 0x6464

   __TEXT.__oslogstring: 0x1d51a
   __TEXT.__ustring: 0x822
   __TEXT.__dlopen_cstrs: 0x4d
-  __TEXT.__unwind_info: 0x139c0
+  __TEXT.__unwind_info: 0x139b0
   __TEXT.__eh_frame: 0xfe68
   __TEXT.__objc_classname: 0x8ca8
   __TEXT.__objc_methname: 0x80ebb

   __AUTH_CONST.__objc_doubleobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1cc8
+  __AUTH_CONST.__auth_got: 0x1d00
   __AUTH.__objc_data: 0x96b8
   __AUTH.__const_weak: 0x70
   __AUTH.__data: 0xb538

   __DATA.__objc_classrefs: 0x28c8
   __DATA.__objc_superrefs: 0x15b8
   __DATA.__objc_ivar: 0x34cc
-  __DATA.__data: 0x8708
+  __DATA.__data: 0x8718
   __DATA.__bss: 0x18f78
   __DATA.__common: 0x228
   __DATA_DIRTY.__objc_data: 0xfab0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 30035
+  Functions: 30034
   Symbols:   59240
   CStrings:  27360
 

```

#### libcryptex.dylib

>  `/usr/lib/libcryptex.dylib`

```diff

   __TEXT.__const: 0x6cd
   __TEXT.__gcc_except_tab: 0x5e0
   __TEXT.__oslogstring: 0x36c2
-  __TEXT.__cstring: 0x179d
+  __TEXT.__cstring: 0x179f
   __TEXT.__unwind_info: 0x538
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x999
CStrings:
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Fri Sep 15 13:46:19 PDT 2023; root:libcryptex-369.0.11~124/libcryptex/RELEASE_ARM64E"
+ "Darwin Cryptex Interface Version 2.0.0: Fri Sep 15 13:46:19 PDT 2023; root:libcryptex-369.0.11~124/libcryptex/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Wed Aug  9 06:19:06 PDT 2023; root:libcryptex-369.0.11~50/libcryptex/RELEASE_ARM64E"
- "Darwin Cryptex Interface Version 2.0.0: Wed Aug  9 06:19:06 PDT 2023; root:libcryptex-369.0.11~50/libcryptex/RELEASE_ARM64E"

```

#### libcryptex_core.dylib

>  `/usr/lib/libcryptex_core.dylib`

```diff

   __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x153d
+  __TEXT.__cstring: 0x153f
   __TEXT.__oslogstring: 0x1fcd
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__unwind_info: 0x420
CStrings:
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Fri Sep 15 13:46:06 PDT 2023; root:libcryptex-369.0.11~124/libcryptex_core/RELEASE_ARM64E"
+ "Darwin Cryptex Core Interface Version 2.0.0: Fri Sep 15 13:46:06 PDT 2023; root:libcryptex-369.0.11~124/libcryptex_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Wed Aug  9 06:18:54 PDT 2023; root:libcryptex-369.0.11~50/libcryptex_core/RELEASE_ARM64E"
- "Darwin Cryptex Core Interface Version 2.0.0: Wed Aug  9 06:18:54 PDT 2023; root:libcryptex-369.0.11~50/libcryptex_core/RELEASE_ARM64E"

```

#### libcryptex_interface.dylib

>  `/usr/lib/libcryptex_interface.dylib`

```diff

   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x110
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x81a
+  __TEXT.__cstring: 0x81c
   __TEXT.__oslogstring: 0x93e
   __TEXT.__gcc_except_tab: 0x160
   __TEXT.__unwind_info: 0x23c
CStrings:
+ "@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Fri Sep 15 13:45:54 PDT 2023; root:libcryptex-369.0.11~124/libcryptex_interface/RELEASE_ARM64E"
+ "Cryptex IPC Interface Version 2.0.0: Fri Sep 15 13:45:54 PDT 2023; root:libcryptex-369.0.11~124/libcryptex_interface/RELEASE_ARM64E"
- "@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Wed Aug  9 06:18:41 PDT 2023; root:libcryptex-369.0.11~50/libcryptex_interface/RELEASE_ARM64E"
- "Cryptex IPC Interface Version 2.0.0: Wed Aug  9 06:18:41 PDT 2023; root:libcryptex-369.0.11~50/libcryptex_interface/RELEASE_ARM64E"

```

#### libcryptex_trampoline.dylib

>  `/usr/lib/libcryptex_trampoline.dylib`

```diff

   __TEXT.__text: 0x788
   __TEXT.__auth_stubs: 0x110
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1dd
+  __TEXT.__cstring: 0x1df
   __TEXT.__oslogstring: 0x104
   __TEXT.__unwind_info: 0x74
   __DATA_CONST.__got: 0x10
CStrings:
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Fri Sep 15 13:46:04 PDT 2023; root:libcryptex-369.0.11~124/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Fri Sep 15 13:46:04 PDT 2023; root:libcryptex-369.0.11~124/libcryptex_trampoline/RELEASE_ARM64E"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Wed Aug  9 06:18:52 PDT 2023; root:libcryptex-369.0.11~50/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Wed Aug  9 06:18:52 PDT 2023; root:libcryptex-369.0.11~50/libcryptex_trampoline/RELEASE_ARM64E"

```

#### libimg4.dylib

>  `/usr/lib/libimg4.dylib`

```diff

 245.0.0.0.0
-  __TEXT.__text: 0x21a7c
+  __TEXT.__text: 0x21ae4
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__const: 0x84b8
   __TEXT.__cstring: 0x336e
   __TEXT.__oslogstring: 0x819
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x744
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3ad0
   __DATA_CONST.__img4_rt: 0x18
CStrings:
+ "@(#)VERSION:Darwin Image4 Validator Version 5.0.0: Fri Sep 15 13:43:48 PDT 2023; root:AppleImage4_libraries-245~1911/libimg4/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 5.0.0: Fri Sep 15 13:43:48 PDT 2023; root:AppleImage4_libraries-245~1911/libimg4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Validator Version 5.0.0: Mon Aug  7 21:45:33 PDT 2023; root:AppleImage4_libraries-245~1766/libimg4/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 5.0.0: Mon Aug  7 21:45:33 PDT 2023; root:AppleImage4_libraries-245~1766/libimg4/RELEASE_ARM64E"

```


</details>

## EOF
