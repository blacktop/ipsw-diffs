# 18.5 (22F75) .vs 18.5 (22F76)

## IPSWs

- `iPhone17,1_18.5_22F75_Restore.ipsw`
- `iPhone17,1_18.5_22F76_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.5 *(22F75)* | 24.5.0 | 11417.122.4~1 | Tue, 22Apr2025 20:38:09 PDT |
| 18.5 *(22F76)* | 24.5.0 | 11417.122.4~1 | Tue, 22Apr2025 20:38:09 PDT |

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F75)* | iBoot-11881.122.1 |
| 18.5 *(22F76)* | iBoot-11881.122.1 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F75)* | 621.2.5.10.10 |
| 18.5 *(22F76)* | 621.2.5.10.10 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### MediaControls

>  `/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls`

```diff

-2963.10.30.0.0
-  __TEXT.__text: 0x87ec
+2963.10.30.1.0
+  __TEXT.__text: 0x8844
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0xfc4
-  __TEXT.__cstring: 0x1cc6
+  __TEXT.__cstring: 0x1cde
   __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x4b
   __TEXT.__gcc_except_tab: 0x150

   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2900
+  __AUTH_CONST.__cfstring: 0x2940
   __AUTH_CONST.__objc_const: 0x2c70
   __AUTH.__objc_data: 0xa0
   __DATA.__bss: 0x20

   - /usr/lib/libobjc.A.dylib
   Functions: 310
   Symbols:   1295
-  CStrings:  620
+  CStrings:  622
 
CStrings:
+ "MRUCAPackageAsset"
+ "asset"

```


</details>

## EOF
