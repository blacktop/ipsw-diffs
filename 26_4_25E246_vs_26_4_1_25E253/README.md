# 26.4 (25E246) .vs 26.4.1 (25E253)

## Inputs

- `UniversalMac_26.4_25E246_Restore.ipsw`
- `UniversalMac_26.4.1_25E253_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.4 *(25E246)* | 25.4.0 | 12377.101.15~1 | Thu, 19Mar2026 19:32:36 PDT |
| 26.4.1 *(25E253)* | 25.4.0 | 12377.101.15~1 | Thu, 19Mar2026 19:32:36 PDT |

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.4 *(25E246)* | mBoot-18000.101.7 |
| 26.4.1 *(25E253)* | mBoot-18000.101.7 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.4 *(25E246)* | 624.1.16.11.4 |
| 26.4.1 *(25E253)* | 624.1.16.11.4 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### WiFiAnalytics

>  `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics`

```diff

   __TEXT.__objc_methlist: 0xfe18
   __TEXT.__const: 0x390
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x13800
+  __TEXT.__cstring: 0x137d6
   __TEXT.__oslogstring: 0x104ad
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x145

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E925F73A-9929-31E8-BBAF-C36A628967AC
+  UUID: DD37E52E-87FF-3506-91D2-E162C762E804
   Functions: 5937
   Symbols:   10602
-  CStrings:  12550
+  CStrings:  12549
 
CStrings:
+ "WiFiAnalytics-800.15 Apr  5 2026 21:38:33"
- "WiFiAnalytics-800.15 Feb 24 2026 22:26:36"
- "WiFiAnalytics-800.15 Feb 24 2026 22:26:37"

```


</details>

## Files

### 🆕 New

#### IPSW (6)

- `Firmware/022-18976-362.dmg.aea.x86.trustcache`
- `Firmware/043-03455-370.dmg.x86.trustcache`
- `Firmware/043-03487-351.dmg.aea.x86.mtree`
- `Firmware/043-03487-351.dmg.aea.x86.root_hash`
- `Firmware/043-03487-351.dmg.aea.x86.trustcache`
- `Firmware/043-03568-369.dmg.x86.trustcache`

### ❌ Removed

#### IPSW (6)

- `Firmware/022-18976-358.dmg.aea.x86.trustcache`
- `Firmware/043-03455-366.dmg.x86.trustcache`
- `Firmware/043-03487-347.dmg.aea.x86.mtree`
- `Firmware/043-03487-347.dmg.aea.x86.root_hash`
- `Firmware/043-03487-347.dmg.aea.x86.trustcache`
- `Firmware/043-03568-365.dmg.x86.trustcache`

## EOF
