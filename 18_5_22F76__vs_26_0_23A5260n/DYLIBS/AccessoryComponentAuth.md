## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

```diff

-1043.120.6.0.0
-  __TEXT.__text: 0x10aec
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x260
-  __TEXT.__const: 0x6940
-  __TEXT.__cstring: 0x1298
-  __TEXT.__oslogstring: 0xf77
-  __TEXT.__unwind_info: 0x3d8
+1110.0.0.0.1
+  __TEXT.__text: 0x11180
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x280
+  __TEXT.__const: 0x75e0
+  __TEXT.__cstring: 0x131a
+  __TEXT.__oslogstring: 0x1000
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methname: 0x87a
-  __TEXT.__objc_methtype: 0x206
-  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methname: 0x8dd
+  __TEXT.__objc_methtype: 0x215
+  __TEXT.__objc_stubs: 0x940
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x13e8
+  __DATA_CONST.__const: 0x1430
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x6a8
-  __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0x388
-  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_selrefs: 0x288
+  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__const: 0x830
+  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__objc_const: 0x3b8
+  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_ivar: 0x24
   __DATA.__data: 0xf0
   __DATA.__bss: 0xf0
   __DATA.__common: 0x1c

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE47071B-461C-3762-9479-94C71D423A79
-  Functions: 374
-  Symbols:   1678
-  CStrings:  583
+  UUID: 405ED127-1837-354F-BBFA-3447E67A1ED5
+  Functions: 388
+  Symbols:   1725
+  CStrings:  601
 
Symbols:
+ -[ACCHWComponentAuthService _verifyBatteryMatch:outputBatteryCode:]
+ -[ACCHWComponentAuthService _verifyBatteryMatch:outputBatteryCode:].cold.1
+ -[ACCHWComponentAuthService signVeridianChallenge:completionHandler:].cold.5
+ -[ACCHWComponentAuthServiceParams batteryCode]
+ -[ACCHWComponentAuthServiceParams setBatteryCode:]
+ _ACCUserDefaultsAccessorydDomain
+ _ACCUserDefaultsKey_DisableAuthFailureTTRForXR
+ _ACCUserDefaultsKey_DisableInductiveAuthTTR
+ _ACCUserDefaultsKey_SysdiagnoseOnInductiveCTAFailure
+ _AVPSecureBootG2Rsa4kSha384IM4C
+ _AVPSecureBootG2Rsa4kSha384IM4C_len
+ _CryptexG1Rsa4kSha384IM4C
+ _CryptexG1Rsa4kSha384IM4C_len
+ _CryptexGlobalG1Rsa4kSha384IM4C
+ _CryptexGlobalG1Rsa4kSha384IM4C_len
+ _DERParseInteger64Signed
+ _DERParseIntegerSigned
+ _Img4DecodeAVPSecureBootG2Rsa4kSha384IM4C
+ _Img4DecodeCryptexG1Rsa4kSha384IM4C
+ _Img4DecodeCryptexGlobalG1Rsa4kSha384IM4C
+ _Img4DecodeLocalPolicyTatsuG8Rsa4kSha384IM4C
+ _Img4DecodeRepairG1Rsa4kSha384IM4C
+ _Img4DecodeSecureBootG7Rsa4kSha384IM4C
+ _Img4DecodeSecureBootGlobalG1Rsa4kSha384IM4C
+ _LocalPolicyTatsuG8Rsa4kSha384IM4C
+ _LocalPolicyTatsuG8Rsa4kSha384IM4C_len
+ _LocalRsa4kSha384IM4C
+ _LocalRsa4kSha384IM4C_len
+ _OBJC_IVAR_$_ACCHWComponentAuthServiceParams._batteryCode
+ _RepairG1Rsa4kSha384IM4C
+ _RepairG1Rsa4kSha384IM4C_len
+ _SecureBootG7Rsa4kSha384IM4C
+ _SecureBootG7Rsa4kSha384IM4C_len
+ _SecureBootGlobalG1Rsa4kSha384IM4C
+ _SecureBootGlobalG1Rsa4kSha384IM4C_len
+ _ShamRsa4kSha384IM4C
+ _ShamRsa4kSha384IM4C_len
+ ___block_literal_global.108
+ ___block_literal_global.111
+ ___block_literal_global.114
+ ___block_literal_global.286
+ ___block_literal_global.288
+ _cpSetBatteryCode
+ _kCFACCUserDefaultsAccessorydDomain
+ _kCFACCUserDefaultsKey_DisableAuthFailureTTRForXR
+ _kCFACCUserDefaultsKey_DisableInductiveAuthTTR
+ _kCFACCUserDefaultsKey_SysdiagnoseOnInductiveCTAFailure
+ _kImg4DecodeAVPSecureBootG2Rsa4kSha384IM4C
+ _kImg4DecodeCryptexG1Rsa4kSha384IM4C
+ _kImg4DecodeCryptexGlobalG1Rsa4kSha384IM4C
+ _kImg4DecodeLocalPolicyTatsuG8Rsa4kSha384IM4C
+ _kImg4DecodeRepairG1Rsa4kSha384IM4C
+ _kImg4DecodeSecureBootG7Rsa4kSha384IM4C
+ _kImg4DecodeSecureBootGlobalG1Rsa4kSha384IM4C
+ _objc_msgSend$_verifyBatteryMatch:outputBatteryCode:
+ _objc_msgSend$setBatteryCode:
+ _objc_retain_x27
+ _sleep
- -[ACCHWComponentAuthService _verifyBatteryMatch:].cold.1
- _Local_root_rsa4k_pub
- _SecureBoot_root_rsa4k_pub
- _SecureBoot_root_rsa4k_pub_len
- _Sham_root_rsa4k_pub
- ___block_literal_global.103
- ___block_literal_global.106
- ___block_literal_global.109
- ___block_literal_global.274
- ___block_literal_global.276
CStrings:
+ "(moduleType=%d) sleeping for %d seconds before retrying auth"
+ "Could not cpGetDeviceIDSN: %s\n"
+ "DisableAuthFailureTTRForXR"
+ "DisableInductiveAuthTTR"
+ "IOTimeoutDeviceBusyError"
+ "Sleeping for %d seconds before retrying auth"
+ "SysdiagnoseOnInductiveCTAFailure"
+ "TI,N,V_batteryCode"
+ "_batteryCode"
+ "_verifyBatteryMatch:outputBatteryCode:"
+ "batteryCode"
+ "com.apple.accessoryd"
+ "i32@0:8@16^S24"
+ "setBatteryCode:"

```
