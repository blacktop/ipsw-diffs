# 18.3 (22D63) .vs 18.3 (22D64)

## IPSWs

- `iPhone12,1_18.3_22D63_Restore.ipsw`
- `iPhone12,1_18.3_22D64_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.3 *(22D63)* | 24.3.0 | 11215.82.4~20 | Thu, 16Jan2025 02:59:55 PST |
| 18.3 *(22D64)* | 24.3.0 | 11215.82.4~20 | Thu, 16Jan2025 02:59:55 PST |

## MachO

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### powerd

>  `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1740.80.3.0.0
-  __TEXT.__text: 0x67f34
+1740.82.1.0.0
+  __TEXT.__text: 0x67ecc
   __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0x4920
   __TEXT.__objc_methlist: 0x2278
   __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0x640f
+  __TEXT.__cstring: 0x6401
   __TEXT.__objc_methname: 0x6035
-  __TEXT.__oslogstring: 0xb78b
+  __TEXT.__oslogstring: 0xb78c
   __TEXT.__objc_classname: 0x2fe
   __TEXT.__objc_methtype: 0x81e
   __TEXT.__gcc_except_tab: 0x498

   __TEXT.__unwind_info: 0x11a8
   __DATA_CONST.__auth_got: 0xdd8
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__cfstring: 0x6d60
+  __DATA_CONST.__const: 0x23d8
+  __DATA_CONST.__cfstring: 0x6d40
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xa0c
   __DATA.__common: 0x1138
-  __DATA.__bss: 0xb60
+  __DATA.__bss: 0xb50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2175
+  Functions: 2173
   Symbols:   562
-  CStrings:  3584
+  CStrings:  3583
 
CStrings:
+ "calib0: device not relevant"
- "InternalBuild"
- "calib: device not relevant"

```

#### SafetyMonitorMessages

>  `/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages`

```diff

 986.0.1.0.0
-  __TEXT.__text: 0x12474
+  __TEXT.__text: 0x124c8
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__swift5_typeref: 0x1b6

```

#### applekeystored

>  `/usr/libexec/applekeystored`

```diff

   __TEXT.__eh_frame: 0x21e8
   __DATA_CONST.__auth_got: 0xbe8
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__auth_ptr: 0x758
+  __DATA_CONST.__auth_ptr: 0x718
   __DATA_CONST.__const: 0x7a50
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.3 *(22D63)* | 620.2.4.10.7 |
| 18.3 *(22D64)* | 620.2.4.10.7 |

### Dylibs

#### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### _MapKit_SwiftUI

>  `/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI`

```diff

   __DATA_CONST.__objc_selrefs: 0x6f0
   __DATA_CONST.__objc_protorefs: 0x48
   __AUTH_CONST.__auth_got: 0x10c8
-  __AUTH_CONST.__auth_ptr: 0x1040
+  __AUTH_CONST.__auth_ptr: 0x1068
   __AUTH_CONST.__const: 0x7270
   __AUTH_CONST.__objc_const: 0x2158
   __AUTH.__objc_data: 0x7a0

```

#### SafetyMonitorUI

>  `/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI`

```diff

   __DATA_CONST.__objc_selrefs: 0xdc8
   __DATA_CONST.__objc_protorefs: 0x50
   __AUTH_CONST.__auth_got: 0x1788
-  __AUTH_CONST.__auth_ptr: 0x1460
+  __AUTH_CONST.__auth_ptr: 0x1458
   __AUTH_CONST.__const: 0x69e8
   __AUTH_CONST.__objc_const: 0x3438
   __AUTH.__objc_data: 0x2220

```


</details>

## EOF
