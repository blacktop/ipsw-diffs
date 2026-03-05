# 26.4 (23E5223f) .vs 26.4 (23E5223k)

## IPSWs

- `iPhone18,1_26.4_23E5223f_Restore.ipsw`
- `iPhone18,1_26.4_23E5223k_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.4 *(23E5223f)* | 25.4.0 | 12377.100.630.502.1~1 | Thu, 26Feb2026 23:19:49 PST |
| 26.4 *(23E5223k)* | 25.4.0 | 12377.100.630.502.1~1 | Thu, 26Feb2026 23:19:49 PST |

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.4 *(23E5223f)* | mBoot-18000.100.13 |
| 26.4 *(23E5223k)* | mBoot-18000.100.13 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.4 *(23E5223f)* | 624.1.14.10.4 |
| 26.4 *(23E5223k)* | 624.1.14.10.4 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### libIPTelephony.dylib

>  `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2652.0.0.0.0
-  __TEXT.__text: 0x50aa7c
+2652.1.0.0.0
+  __TEXT.__text: 0x50aa60
   __TEXT.__auth_stubs: 0x2d80
   __TEXT.__init_offsets: 0x158
   __TEXT.__objc_methlist: 0x748
   __TEXT.__const: 0x2001b
-  __TEXT.__gcc_except_tab: 0x4e78c
+  __TEXT.__gcc_except_tab: 0x4e784
   __TEXT.__cstring: 0x37b87
   __TEXT.__oslogstring: 0xf5e1
   __TEXT.__unwind_info: 0x18e30

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 2A89E16D-123B-3421-B09F-C6B312F04476
+  UUID: 246DF7F6-AAAD-3A4B-8239-2C807D38376C
   Functions: 17031
   Symbols:   51066
   CStrings:  9989
Functions:
~ __ZN15AVCAudioSession16setConfigurationENSt3__18weak_ptrI10SDPSessionEE : 7468 -> 7460
~ __ZN23SDPMediaFormatEVSParamsC2Et : 148 -> 152
~ __ZN23SDPMediaFormatEVSParamsC2ERKS_ : 212 -> 220
~ __ZN19SDPMediaEVSSettingsneERKS_ : 344 -> 340
~ __ZN19SDPMediaEVSSettingsC2EPK23SDPMediaFormatEVSParamsS2_bRK8ImsPrefs : 1100 -> 1104
~ __ZN10IBISession28generateSessionConfigurationENSt3__18weak_ptrI10SDPSessionEE : 8336 -> 8324
~ ____ZN13QMIRTPSession16setConfigurationENSt3__18weak_ptrI10SDPSessionEE_block_invoke.45 : 356 -> 348
~ __ZN9SDPParser22parseEVSHeaderFullOnlyEP23SDPMediaFormatEVSParamsNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 76 -> 68
~ __ZNK23SDPMediaFormatEVSParams16formatParametersEv : 2508 -> 2504
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKRcugBsBAV5HxTehUqARD5QP_Xvm3qQgtT4SDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/4~CKRcugBsBAV5HxTehUqARD5QP_Xvm3qQgtT4SDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~CJ7-ugA0ii0xD6Ydjm1lswSulU90BHQ_vfxXgyw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~CJ7-ugA0ii0xD6Ydjm1lswSulU90BHQ_vfxXgyw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"

```


</details>

## EOF
