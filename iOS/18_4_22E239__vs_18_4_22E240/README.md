# 18.4 (22E239) .vs 18.4 (22E240)

## IPSWs

- `iPhone17,1_18.4_22E239_Restore.ipsw`
- `iPhone17,1_18.4_22E240_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.4 *(22E239)* | 24.4.0 | 11417.102.9~20 | Sat, 15Mar2025 18:26:55 PDT |
| 18.4 *(22E240)* | 24.4.0 | 11417.102.9~20 | Sat, 15Mar2025 18:26:55 PDT |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.4 *(22E239)* | 621.1.15.10.7 |
| 18.4 *(22E240)* | 621.1.15.10.7 |

### Dylibs

#### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### _MapKit_SwiftUI

>  `/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI`

```diff

   __DATA_CONST.__objc_selrefs: 0x9f0
   __DATA_CONST.__objc_protorefs: 0x48
   __AUTH_CONST.__auth_got: 0x10b0
-  __AUTH_CONST.__auth_ptr: 0x1070
+  __AUTH_CONST.__auth_ptr: 0x10c8
   __AUTH_CONST.__const: 0x6fe0
   __AUTH_CONST.__objc_const: 0x14e0
   __AUTH.__objc_data: 0x7a0

```

#### HomeKitCore

>  `/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore`

```diff

-1278.5.13.1.4
+1278.5.13.1.5
   __TEXT.__text: 0x91da0
   __TEXT.__auth_stubs: 0x1da0
   __TEXT.__objc_methlist: 0x374

   __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_protorefs: 0x38
   __AUTH_CONST.__auth_got: 0xed0
-  __AUTH_CONST.__auth_ptr: 0xae8
+  __AUTH_CONST.__auth_ptr: 0x9a8
   __AUTH_CONST.__const: 0x3fe8
   __AUTH_CONST.__objc_const: 0x1648
   __AUTH.__objc_data: 0x900

```

#### HomeKitDaemon

>  `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon`

```diff

-1278.5.13.1.4
-  __TEXT.__text: 0xdbbf80
+1278.5.13.1.5
+  __TEXT.__text: 0xdbbf88
   __TEXT.__auth_stubs: 0x5ba0
-  __TEXT.__objc_methlist: 0x8ebcc
+  __TEXT.__objc_methlist: 0x8ebd4
   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__const: 0xa314
   __TEXT.__cstring: 0x6b77a

   __DATA_CONST.__objc_superrefs: 0x33e8
   __DATA_CONST.__objc_arraydata: 0x32a8
   __AUTH_CONST.__auth_got: 0x2de8
-  __AUTH_CONST.__auth_ptr: 0x11a0
+  __AUTH_CONST.__auth_ptr: 0x1148
   __AUTH_CONST.__const: 0x18730
   __AUTH_CONST.__cfstring: 0x5aca0
   __AUTH_CONST.__objc_const: 0x110798

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 56721
-  Symbols:   54100
+  Functions: 56722
+  Symbols:   54101
   CStrings:  82180
 

```

#### HomeKitDaemonFoundation

>  `/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation`

```diff

-1278.5.13.1.4
+1278.5.13.1.5
   __TEXT.__text: 0x5ef3c
   __TEXT.__auth_stubs: 0x13a0
   __TEXT.__swift5_typeref: 0x134a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __AUTH_CONST.__auth_got: 0x9d0
-  __AUTH_CONST.__auth_ptr: 0xaa0
+  __AUTH_CONST.__auth_ptr: 0xa90
   __AUTH_CONST.__const: 0x2f40
   __AUTH_CONST.__objc_const: 0x5a8
   __AUTH.__data: 0x710

```

#### HomeKitDaemonLegacy

>  `/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy`

```diff

-1278.5.13.1.4
+1278.5.13.1.5
   __TEXT.__text: 0xa60c54
   __TEXT.__auth_stubs: 0x4390
   __TEXT.__objc_methlist: 0x7169c

   __DATA_CONST.__objc_superrefs: 0x2ae8
   __DATA_CONST.__objc_arraydata: 0x27f8
   __AUTH_CONST.__auth_got: 0x21e0
-  __AUTH_CONST.__auth_ptr: 0x4c0
+  __AUTH_CONST.__auth_ptr: 0x4f0
   __AUTH_CONST.__const: 0xd5e8
   __AUTH_CONST.__cfstring: 0x4cba0
   __AUTH_CONST.__objc_const: 0xcddb0

```

#### HomeKitEvents

>  `/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents`

```diff

-1278.5.13.1.4
+1278.5.13.1.5
   __TEXT.__text: 0x79ad0
   __TEXT.__auth_stubs: 0x1c70
   __TEXT.__objc_methlist: 0x45c

   __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_protorefs: 0x70
   __AUTH_CONST.__auth_got: 0xe40
-  __AUTH_CONST.__auth_ptr: 0x840
+  __AUTH_CONST.__auth_ptr: 0x7c0
   __AUTH_CONST.__const: 0x45d0
   __AUTH_CONST.__objc_const: 0x1520
   __AUTH.__objc_data: 0x960

```

#### HomeKitMetrics

>  `/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics`

```diff

-1278.5.13.1.4
+1278.5.13.1.5
   __TEXT.__text: 0x3ab98
   __TEXT.__auth_stubs: 0xeb0
   __TEXT.__objc_methlist: 0x1764

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__auth_ptr: 0x270
+  __AUTH_CONST.__auth_ptr: 0x308
   __AUTH_CONST.__const: 0xc18
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x3f08

```


</details>

## EOF
