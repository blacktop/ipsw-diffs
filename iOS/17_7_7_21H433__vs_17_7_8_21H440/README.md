# 17.7.7 (21H433) .vs 17.7.8 (21H440)

## IPSWs

- `iPad_64bit_TouchID_ASTC_17.7.7_21H433_Restore.ipsw`
- `iPad_64bit_TouchID_ASTC_17.7.8_21H440_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.7.7 *(21H433)* | 23.6.0 | 10063.142.1.703.7~1 | Thu, 24Apr2025 20:24:42 PDT |
| 17.7.8 *(21H440)* | 23.6.0 | 10063.142.1.703.7~1 | Thu, 24Apr2025 20:24:42 PDT |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### dyld

>  `/usr/lib/dyld`

```diff

   __DATA_DIRTY.__data: 0x5c
   __DATA_DIRTY.__common: 0x1120
   __DATA_DIRTY.__bss: 0x1bc0
-  UUID: 84EB8F8E-0274-3F8C-8C14-C80DDAD40F0F
+  UUID: D85EAED0-C00B-3D42-A351-577BF6A9B430
   Functions: 2887
   Symbols:   3409
   CStrings:  1687
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu May 15 20:29:37 PDT 2025; root:libignition-56~62065/libignition_core/RELEASE_ARM64"
+ "Darwin Ignition Sequence Version 1.0.0: Thu May 15 20:29:37 PDT 2025; root:libignition-56~62065/libignition_core/RELEASE_ARM64"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Apr 24 20:18:56 PDT 2025; root:libignition-56~61869/libignition_core/RELEASE_ARM64"
- "Darwin Ignition Sequence Version 1.0.0: Thu Apr 24 20:18:56 PDT 2025; root:libignition-56~61869/libignition_core/RELEASE_ARM64"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.7.7 *(21H433)* | 618.9.1.10.2 |
| 17.7.8 *(21H440)* | 618.9.1.10.2 |

### Dylibs

#### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### ContainerManagerCommon

>  `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1E9541C2-5252-349C-8E65-2EC6B58094B1
+  UUID: 3A3E10DF-616E-37F4-B4FB-66AF9DB1F593
   Functions: 2393
   Symbols:   9233
   CStrings:  5791
CStrings:
+ "20:38:00"
+ "May 15 2025"
+ "MobileContainerManager-582.140.2~1113"
- "20:33:53"
- "Apr 24 2025"
- "MobileContainerManager-582.140.2~1112"

```

#### dyld

>  `/usr/lib/dyld`

```diff

   __DATA_DIRTY.__data: 0x5c
   __DATA_DIRTY.__common: 0x1120
   __DATA_DIRTY.__bss: 0x1bc0
-  UUID: 84EB8F8E-0274-3F8C-8C14-C80DDAD40F0F
+  UUID: D85EAED0-C00B-3D42-A351-577BF6A9B430
   Functions: 2887
   Symbols:   6317
   CStrings:  1687
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu May 15 20:29:37 PDT 2025; root:libignition-56~62065/libignition_core/RELEASE_ARM64"
+ "Darwin Ignition Sequence Version 1.0.0: Thu May 15 20:29:37 PDT 2025; root:libignition-56~62065/libignition_core/RELEASE_ARM64"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Apr 24 20:18:56 PDT 2025; root:libignition-56~61869/libignition_core/RELEASE_ARM64"
- "Darwin Ignition Sequence Version 1.0.0: Thu Apr 24 20:18:56 PDT 2025; root:libignition-56~61869/libignition_core/RELEASE_ARM64"

```

#### libsandbox.1.dylib

>  `/usr/lib/libsandbox.1.dylib`

```diff

   __DATA.__common: 0x8
   - /usr/lib/libMatch.1.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 0F7CDE60-E01E-3405-9CBB-3D0C855EFEE4
+  UUID: 6B0761CF-9687-3DD8-B70E-29A896217796
   Functions: 47
   Symbols:   95
   CStrings:  19
CStrings:
+ "A29E3E1B-D3C0-45CF-B674-E45AA637FC85"
- "CE1789EF-076A-468B-855C-FCEC33183468"

```


</details>

## EOF
