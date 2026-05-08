# 26.5 (23F75) .vs 26.5 (23F77)

## Inputs

- `iPhone18,1_26.5_23F75_Restore.ipsw`
- `iPhone18,1_26.5_23F77_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.5 *(23F75)* | 25.5.0 | 12377.122.4~1 | Thu, 23Apr2026 20:42:24 PDT |
| 26.5 *(23F77)* | 25.5.0 | 12377.122.4~1 | Thu, 23Apr2026 20:42:24 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### warlock.metallib

>  `/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/warlock.metallib`

```diff

 
   __TEXT.__reflection: 0x1d30
-  __TEXT.__compute: 0x7030
+  __TEXT.__compute: 0x7020
   __TEXT.__descriptor: 0x4e0
   __TEXT.__metallib: 0x21b20
-  UUID: 92EF8E5E-29DE-3787-9D90-7475F3D9D816
+  UUID: 2C3A897F-05D2-3C59-8D0C-1BC28576E438
   Functions: 0
   Symbols:   0
   CStrings:  0

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F75)* | mBoot-18000.120.36 |
| 26.5 *(23F77)* | mBoot-18000.120.36 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F75)* | 624.2.5.10.4 |
| 26.5 *(23F77)* | 624.2.5.10.4 |

### Dylibs

#### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### NanoTimeKitCompanion

>  `/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion`

```diff

-2483.340.80.0.0
+2483.340.80.1.0
   __TEXT.__text: 0x0
-  __TEXT.__cstring: 0x24
+  __TEXT.__cstring: 0x26
   __DATA.__data: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 5E30ADAD-9ED9-32EA-BF7E-8FB966E00B2B
+  UUID: AED5BA0E-FF00-3D72-ABD2-9A129A78934E
   Functions: 0
   Symbols:   1
   CStrings:  1
CStrings:
+ "description=NanoTimeKit-2483.340.80.1"
- "description=NanoTimeKit-2483.340.80"

```

#### UserNotificationsCore

>  `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-640.5.32.103.0
-  __TEXT.__text: 0x205cdc
-  __TEXT.__auth_stubs: 0x3b20
+640.5.32.104.0
+  __TEXT.__text: 0x206b80
+  __TEXT.__auth_stubs: 0x3b50
   __TEXT.__objc_methlist: 0x7ba4
   __TEXT.__cstring: 0xa2e3
-  __TEXT.__const: 0x10568
+  __TEXT.__const: 0x10748
   __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__oslogstring: 0x10437
+  __TEXT.__oslogstring: 0x10507
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__constg_swiftt: 0x6958
-  __TEXT.__swift5_typeref: 0x625e
+  __TEXT.__constg_swiftt: 0x6984
+  __TEXT.__swift5_typeref: 0x6298
   __TEXT.__swift5_reflstr: 0x3b33
-  __TEXT.__swift5_fieldmd: 0x4598
-  __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_assocty: 0x4b0
+  __TEXT.__swift5_fieldmd: 0x45b4
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_assocty: 0x4e0
   __TEXT.__swift5_protos: 0x128
-  __TEXT.__swift5_proto: 0xb28
-  __TEXT.__swift5_types: 0x528
+  __TEXT.__swift5_proto: 0xb40
+  __TEXT.__swift5_types: 0x52c
   __TEXT.__swift_as_entry: 0x1ac
   __TEXT.__swift5_capture: 0x19a0
   __TEXT.__swift_as_ret: 0x1ec
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x5fc8
+  __TEXT.__unwind_info: 0x5fd0
   __TEXT.__eh_frame: 0x7910
   __TEXT.__objc_classname: 0x3796
   __TEXT.__objc_methname: 0x19295
   __TEXT.__objc_methtype: 0x39ff
   __TEXT.__objc_stubs: 0xfb80
-  __DATA_CONST.__got: 0x15f8
+  __DATA_CONST.__got: 0x1600
   __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x80

   __DATA_CONST.__objc_selrefs: 0x49a8
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x200
-  __AUTH_CONST.__auth_got: 0x1da0
-  __AUTH_CONST.__const: 0xb318
+  __AUTH_CONST.__auth_got: 0x1db8
+  __AUTH_CONST.__const: 0xb340
   __AUTH_CONST.__cfstring: 0x64e0
   __AUTH_CONST.__objc_const: 0x24990
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x1120
   __AUTH.__data: 0x2e28
   __DATA.__objc_ivar: 0x880
-  __DATA.__data: 0x3d88
-  __DATA.__bss: 0xe2b0
+  __DATA.__data: 0x3de8
+  __DATA.__bss: 0xe5b0
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0x2bd0
-  __DATA_DIRTY.__data: 0x6070
+  __DATA_DIRTY.__data: 0x6090
   __DATA_DIRTY.__bss: 0x5580
   __DATA_DIRTY.__common: 0x380
   - /System/Library/Frameworks/AccessoryLiveActivities.framework/AccessoryLiveActivities

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50E79734-83FE-3B3A-8C72-27258EF90696
-  Functions: 9147
-  Symbols:   13303
-  CStrings:  7400
+  UUID: 27058F3E-3A18-37BC-B618-004F5E29FE88
+  Functions: 9153
+  Symbols:   13311
+  CStrings:  7403
 
Symbols:
+ _BPSBulletinDistributorBBSectionsDidChangeNotification
+ _NSURLFileProtectionKey
+ _associated conformance So16NSURLResourceKeyaSHSCSQ
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _symbolic _____ So16NSURLResourceKeya
+ _symbolic _____y_____G s11_SetStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16NSURLResourceKeya
CStrings:
+ "%s -- No device found for pairing ID: %s"
+ "Failed to update data protection class for watch forwarding configuration: %@"
+ "Updating data protection class for watch forwarding configuration"

```

#### WatchFacesWallpaperSupport

>  `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport`

```diff

-2483.340.80.0.0
-  __TEXT.__text: 0x4042c
-  __TEXT.__auth_stubs: 0x14f0
+2483.340.80.1.0
+  __TEXT.__text: 0x3f8e4
+  __TEXT.__auth_stubs: 0x14b0
   __TEXT.__objc_methlist: 0xdc4
-  __TEXT.__const: 0x416a
-  __TEXT.__swift5_typeref: 0x1210
+  __TEXT.__const: 0x41ca
+  __TEXT.__swift5_typeref: 0x11c0
   __TEXT.__cstring: 0xab3
-  __TEXT.__swift5_capture: 0x18c
-  __TEXT.__oslogstring: 0x157c
-  __TEXT.__constg_swiftt: 0x167c
+  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__oslogstring: 0x16bc
+  __TEXT.__constg_swiftt: 0x1658
   __TEXT.__swift5_reflstr: 0xf50
   __TEXT.__swift5_fieldmd: 0x1504
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x2c8
-  __TEXT.__swift5_types: 0x188
+  __TEXT.__swift5_proto: 0x2d4
+  __TEXT.__swift5_types: 0x184
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__unwind_info: 0xe48
   __TEXT.__eh_frame: 0xc08
-  __TEXT.__objc_classname: 0x4d2
-  __TEXT.__objc_methname: 0x3a0b
-  __TEXT.__objc_methtype: 0x1d75
-  __TEXT.__objc_stubs: 0x13c0
-  __DATA_CONST.__got: 0x330
+  __TEXT.__objc_classname: 0x4e2
+  __TEXT.__objc_methname: 0x3a3b
+  __TEXT.__objc_methtype: 0x1d25
+  __TEXT.__objc_stubs: 0x13e0
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc98
+  __DATA_CONST.__objc_selrefs: 0xca0
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x2e58
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__const: 0x2d60
   __AUTH_CONST.__objc_const: 0x2288
   __AUTH.__objc_data: 0x108
   __AUTH.__data: 0x630
-  __DATA.__data: 0xda0
-  __DATA.__bss: 0x5280
+  __DATA.__data: 0xd70
+  __DATA.__bss: 0x5400
   __DATA_DIRTY.__objc_data: 0x210
   __DATA_DIRTY.__data: 0xc38
   __DATA_DIRTY.__bss: 0x500

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0EFEF32C-8BDB-33E7-99DF-D295451F8D13
-  Functions: 1654
-  Symbols:   1090
-  CStrings:  887
+  UUID: 96096B07-3A5C-36F4-8640-2210DDB0768B
+  Functions: 1645
+  Symbols:   1075
+  CStrings:  891
 
Symbols:
+ _associated conformance So10CGImageRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So10CGImageRefaSHSCSQ
+ _objc_msgSend$error
+ _swift_unknownObjectRelease_n
- _block_copy_helper.74
- _block_descriptor.76
- _block_destroy_helper.75
- _swift_projectBox
- _symbolic SDy___________pG So22UIInterfaceOrientationV So9MTLBufferP
- _symbolic SaySiG
- _symbolic Siz_Xx
- _symbolic _____ So15CGColorSpaceRefa
- _symbolic _____SgXwz_Xx 26WatchFacesWallpaperSupport0C17MetalCoordinationO18EditingCoordinatorC
- _symbolic _____XDXMT 26WatchFacesWallpaperSupport0C17MetalCoordinationO18EditingCoordinatorC
- _symbolic _____y___________pG s18_DictionaryStorageC So22UIInterfaceOrientationV So9MTLBufferP
- _symbolic _____z_Xx 10Foundation8IndexSetV
CStrings:
+ "Exit generateLookSnapshotsIfNeeded (reason: cache hit, %ld look(s))"
+ "Exit generateLookSnapshotsIfNeeded (reason: not .paged)"
+ "GPU completed “%{public}s” with status %lu"
+ "committing snapshot render for “%{public}s” (%ld/%ld)"
+ "couldn’t create data provider for “%{public}s”"
+ "couldn’t create image from data for “%{public}s”"
+ "couldn’t make buffer for look snapshot “%{public}s”"
+ "couldn’t make command buffer for look snapshotting “%{public}s”"
+ "encoding render for “%{public}s” (%ld/%ld)"
+ "error"
+ "lastGeneratedSnapshotState"
+ "look-snapshotting command buffer did not complete successfully for “%{public}s” (status %lu, error: %{public}s)"
+ "not applying snapshot for “%{public}s” (final orientation %{public}s, this is %{public}s)"
+ "snapshotted look “%{public}s” (%{public}s)"
- "couldn’t create data provider"
- "couldn’t create image from data"
- "couldn’t make buffer for look snapshots"
- "couldn’t make command buffer for look snapshotting"
- "latestSnapshotBuffers"
- "look-snapshotting command buffer did not complete successfully"
- "missing snapshot for “%{public}s” in orientation %{public}s — clearing contents"
- "not applying snapshots (final orientation %{public}s, these are %{public}s)"
- "snapshot rendering finished for %{public}s"
- "snapshotted look “%{public}s”"

```


</details>

## EOF
