# 17.6.1 (21G93) .vs 17.6.1 (21G101)

## IPSWs

- `iPhone16,2_17.6.1_21G93_Restore.ipsw`
- `iPhone16,2_17.6.1_21G101_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.6.1 *(21G93)* | 23.6.0 | 10063.142.1~1 | Fri, 05Jul2024 18:04:28 PDT |
| 17.6.1 *(21G101)* | 23.6.0 | 10063.142.1~1 | Fri, 05Jul2024 18:04:28 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### lockdownd

>  `/usr/libexec/lockdownd`

```diff

   __TEXT.__auth_stubs: 0x2ab0
   __TEXT.__objc_stubs: 0x4120
   __TEXT.__objc_methlist: 0x31ec
-  __TEXT.__cstring: 0x487f0
+  __TEXT.__cstring: 0x487f1
   __TEXT.__const: 0x18130
   __TEXT.__oslogstring: 0x6bc
   __TEXT.__gcc_except_tab: 0x34bc
CStrings:
+ "VinylRestore-50~247"
- "VinylRestore-50~99"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.6.1 *(21G93)* | 618.3.11.10.5 |
| 17.6.1 *(21G101)* | 618.3.11.10.5 |

### Dylibs

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### libimage4.dylib

>  `/usr/lib/libimage4.dylib`

```diff

   __TEXT.__text: 0x26090
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__const: 0x8850
-  __TEXT.__cstring: 0x54c6
+  __TEXT.__cstring: 0x54c8
   __TEXT.__oslogstring: 0x7e
   __TEXT.__unwind_info: 0x9f8
   __DATA_CONST.__got: 0x28
CStrings:
+ "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Fri Aug 16 18:29:47 PDT 2024; root:AppleImage4_libraries-257.140.2~1081/libimage4/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 6.3.0: Fri Aug 16 18:29:47 PDT 2024; root:AppleImage4_libraries-257.140.2~1081/libimage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Sun Jun 30 11:37:43 PDT 2024; root:AppleImage4_libraries-257.140.2~615/libimage4/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 6.3.0: Sun Jun 30 11:37:43 PDT 2024; root:AppleImage4_libraries-257.140.2~615/libimage4/RELEASE_ARM64E"

```

#### libVinylUpdater.dylib

>  `/usr/lib/updaters/libVinylUpdater.dylib`

```diff

   __TEXT.__auth_stubs: 0x13a0
   __TEXT.__init_offsets: 0x34
   __TEXT.__gcc_except_tab: 0x20c8
-  __TEXT.__cstring: 0x5de0
+  __TEXT.__cstring: 0x5de1
   __TEXT.__const: 0xdc0
   __TEXT.__unwind_info: 0xf28
   __TEXT.__eh_frame: 0x178
CStrings:
+ "/AppleInternal/Library/BuildRoots/57b12f66-5b5c-11ef-9f8f-0a3c3d30a6d7/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "VinylRestore-50~247"
- "/AppleInternal/Library/BuildRoots/ce4161a3-3a02-11ef-92ee-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "VinylRestore-50~99"

```

#### CallHistory

>  `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

   __TEXT.__objc_methlist: 0x2890
   __TEXT.__const: 0x210
   __TEXT.__gcc_except_tab: 0x5ac
-  __TEXT.__cstring: 0x1e4a
+  __TEXT.__cstring: 0x1e4b
   __TEXT.__oslogstring: 0x34f2
   __TEXT.__dlopen_cstrs: 0x95
   __TEXT.__unwind_info: 0xd94
CStrings:
+ "1222.700.81~398"
- "1222.700.81~27"

```

#### SeymourServices

>  `/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices`

```diff

-843.44.0.0.0
-  __TEXT.__text: 0x7c9a10
-  __TEXT.__auth_stubs: 0xafc0
+843.46.0.0.0
+  __TEXT.__text: 0x7c91f8
+  __TEXT.__auth_stubs: 0xafd0
   __TEXT.__objc_methlist: 0x1094
-  __TEXT.__const: 0x17c70
-  __TEXT.__cstring: 0x2b248
-  __TEXT.__constg_swiftt: 0xc388
+  __TEXT.__const: 0x17cc0
+  __TEXT.__cstring: 0x2b338
+  __TEXT.__constg_swiftt: 0xc390
   __TEXT.__swift5_typeref: 0x13344
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_reflstr: 0xbe8e

   __TEXT.__swift5_assocty: 0x1cc0
   __TEXT.__swift5_proto: 0xfbc
   __TEXT.__swift5_types: 0x94c
-  __TEXT.__swift5_capture: 0x15bd0
+  __TEXT.__swift5_capture: 0x15be0
   __TEXT.__swift5_protos: 0x2e8
   __TEXT.__swift5_mpenum: 0x120
-  __TEXT.__unwind_info: 0x17adc
-  __TEXT.__eh_frame: 0x3cde4
+  __TEXT.__unwind_info: 0x17b0c
+  __TEXT.__eh_frame: 0x3ce1c
   __TEXT.__objc_classname: 0x24a
-  __TEXT.__objc_methname: 0x6127
+  __TEXT.__objc_methname: 0x611d
   __TEXT.__objc_methtype: 0x18a5
   __TEXT.__objc_stubs: 0x1c0
   __DATA_CONST.__got: 0x43e0

   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x162d0
-  __DATA_CONST.__objc_selrefs: 0x1db0
+  __DATA_CONST.__objc_selrefs: 0x1da8
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_classrefs: 0x448
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x420
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__const: 0x461c8
+  __AUTH_CONST.__const: 0x461f8
   __AUTH_CONST.__auth_ptr: 0xc68
-  __AUTH_CONST.__auth_got: 0x57e8
+  __AUTH_CONST.__auth_got: 0x57f0
   __AUTH.__objc_data: 0x2aa8
   __AUTH.__data: 0x6f80
   __DATA.__objc_ivar: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 32423
-  Symbols:   1692
-  CStrings:  4964
+  Functions: 32430
+  Symbols:   1693
+  CStrings:  4966
 
Symbols:
+ _swift_deallocUninitializedObject
CStrings:
+ "Couldn't find a step for fallback version %{public}s."
+ "Found invalid version %{public}s. Attempting recovery by forcing data version %{public}s"
+ "Found newer data version than expected %{public}s. Expected: %{public}s"
- "hasChanges"

```

#### libauthinstall.dylib

>  `/usr/lib/libauthinstall.dylib`

```diff

   __TEXT.__text: 0x968ec
   __TEXT.__auth_stubs: 0x1820
   __TEXT.__objc_methlist: 0x26d4
-  __TEXT.__cstring: 0x1c912
+  __TEXT.__cstring: 0x1c913
   __TEXT.__const: 0xab60
   __TEXT.__oslogstring: 0x48b
   __TEXT.__gcc_except_tab: 0x2b94
CStrings:
+ "VinylRestore-50~247"
- "VinylRestore-50~99"

```


</details>

## EOF
