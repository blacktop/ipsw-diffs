## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

-1043.120.6.0.0
-  __TEXT.__text: 0x1031c
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x960
-  __TEXT.__objc_methlist: 0x394
-  __TEXT.__const: 0x68f8
-  __TEXT.__cstring: 0x124b
+1110.0.0.0.1
+  __TEXT.__text: 0x109b0
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x3b4
+  __TEXT.__const: 0x7598
+  __TEXT.__cstring: 0x12cd
   __TEXT.__objc_classname: 0x9e
-  __TEXT.__objc_methname: 0xa41
-  __TEXT.__objc_methtype: 0x2df
-  __TEXT.__oslogstring: 0xe8d
-  __TEXT.__unwind_info: 0x3c0
-  __DATA_CONST.__auth_got: 0x3c8
+  __TEXT.__objc_methname: 0xaa4
+  __TEXT.__objc_methtype: 0x2ee
+  __TEXT.__oslogstring: 0xf16
+  __TEXT.__unwind_info: 0x3d0
+  __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x19f8
-  __DATA_CONST.__cfstring: 0x12a0
+  __DATA_CONST.__const: 0x1bc8
+  __DATA_CONST.__cfstring: 0x1320
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x648
-  __DATA.__objc_selrefs: 0x348
-  __DATA.__objc_ivar: 0x20
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x678
+  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b0
   __DATA.__bss: 0xd9

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D42C0C2E-94B8-314A-BF4D-0F6D6E383732
-  Functions: 367
-  Symbols:   2335
-  CStrings:  623
+  UUID: 3317FDEE-637F-3552-8E9A-832595A0337F
+  Functions: 381
+  Symbols:   2406
+  CStrings:  641
 
Symbols:
+ -[ACCHWComponentAuthService _verifyBatteryMatch:outputBatteryCode:]
+ -[ACCHWComponentAuthService _verifyBatteryMatch:outputBatteryCode:].cold.1
+ -[ACCHWComponentAuthService signVeridianChallenge:completionHandler:].cold.5
+ -[ACCHWComponentAuthServiceParams batteryCode]
+ -[ACCHWComponentAuthServiceParams setBatteryCode:]
+ OBJC_IVAR_$_ACCHWComponentAuthServiceParams._batteryCode
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
+ _RepairG1Rsa4kSha384IM4C
+ _RepairG1Rsa4kSha384IM4C_len
+ _SecureBootG7Rsa4kSha384IM4C
+ _SecureBootG7Rsa4kSha384IM4C_len
+ _SecureBootGlobalG1Rsa4kSha384IM4C
+ _SecureBootGlobalG1Rsa4kSha384IM4C_len
+ _ShamRsa4kSha384IM4C
+ _ShamRsa4kSha384IM4C_len
+ __block_literal_global.108
+ __block_literal_global.111
+ __block_literal_global.114
+ __block_literal_global.286
+ __block_literal_global.288
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
- __block_literal_global.103
- __block_literal_global.106
- __block_literal_global.109
- __block_literal_global.274
- __block_literal_global.276
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
