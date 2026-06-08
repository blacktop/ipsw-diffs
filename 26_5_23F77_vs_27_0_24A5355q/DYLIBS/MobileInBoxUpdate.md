## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-176.122.1.0.0
-  __TEXT.__text: 0x32480
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x17d0
-  __TEXT.__const: 0x5f58
-  __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__cstring: 0x1665
-  __TEXT.__oslogstring: 0x24b9
+253.0.0.0.0
+  __TEXT.__text: 0x32264
+  __TEXT.__objc_methlist: 0x1868
+  __TEXT.__const: 0xbda3
+  __TEXT.__cstring: 0x17c1
+  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__oslogstring: 0x2669
   __TEXT.__swift5_typeref: 0xdc
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__unwind_info: 0xa98
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x2f0
-  __TEXT.__objc_methname: 0x2e7b
-  __TEXT.__objc_methtype: 0x6a8
-  __TEXT.__objc_stubs: 0x2ae0
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x3d40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x43b8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe78
+  __DATA_CONST.__objc_selrefs: 0xee8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH_CONST.__const: 0x2788
-  __AUTH_CONST.__cfstring: 0x1b60
-  __AUTH_CONST.__objc_const: 0x2818
+  __DATA_CONST.__objc_arraydata: 0x360
+  __DATA_CONST.__got: 0x2c0
+  __AUTH_CONST.__const: 0x2988
+  __AUTH_CONST.__cfstring: 0x1c80
+  __AUTH_CONST.__objc_const: 0x2828
   __AUTH_CONST.__objc_intobj: 0x1278
   __AUTH_CONST.__objc_arrayobj: 0x390
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH.__objc_data: 0x7f0
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0xff0
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 55C1E0BC-C59A-32D9-A82B-205F53CC1964
-  Functions: 1315
-  Symbols:   5014
-  CStrings:  1417
+  UUID: D3555549-EAAA-381F-8832-19DAB335450D
+  Functions: 1374
+  Symbols:   5223
+  CStrings:  710
 
Symbols:
+ +[MIBUPMUHelper _checkPMUForProperties:outError:]
+ +[MIBUPMUHelper _checkPMUForProperties:outError:].cold.1
+ +[MIBUPMUHelper _configurePMUWithProperties:]
+ +[MIBUPMUHelper _configurePMUWithProperties:].cold.1
+ +[MIBUPMUHelper _configurePMUWithProperties:].cold.2
+ +[MIBUPMUHelper _configurePMUWithProperties:].cold.3
+ +[MIBUPMUHelper _configurePMUWithProperties:].cold.4
+ +[MIBUPMUHelper _configurePMUWithProperties:].cold.5
+ +[MIBUPMUHelper _findServicePmuPrimary].cold.7
+ +[MIBUPMUHelper enableLPMFlagForBT]
+ +[MIBUPMUHelper enableLPMFlagForRTCAlarm]
+ +[MIBUPMUHelper isRTCAlarmWakeScheduled:]
+ +[MIBUPMUHelper readLPMFlagForBT:]
+ +[MIBUPMUHelper readLPMFlagForRTCAlarm:]
+ +[MIBUPMUHelper scheduleRTCAlarmWakeOnDate:]
+ +[MIBUPMUHelper scheduleRTCAlarmWakeOnDate:].cold.1
+ +[MIBUPMUHelper scheduleRTCAlarmWakeOnDate:].cold.2
+ +[MIBUPMUHelper wakedUpByRTCAlarm]
+ +[MIBUPMUHelper wakedUpByRTCAlarm].cold.1
+ +[MIBUPMUHelper wakedUpByRTCAlarm].cold.2
+ +[MIBUPMUHelper wakedUpByRTCAlarm].cold.3
+ +[MIBUPMUHelper wakedUpByRTCAlarm].cold.4
+ +[MIBUPMUHelper wakedUpByRTCAlarm].cold.5
+ +[MIBUPMUHelper wakedUpByRTCAlarm].cold.6
+ -[MIBUClient invalidate].cold.2
+ -[MIBUClient isInPalletUpdateMode:].cold.3
+ -[MIBUClient isInPalletUpdateMode:].cold.4
+ -[MIBUClient isRTCAlarmSetWithCompletion:]
+ -[MIBUClient personalizationInfoWithError:]
+ -[MIBUClient personalizationInfoWithError:].cold.1
+ -[MIBUNFCCommand _serializeHeartbeat].cold.4
+ -[MIBUStatusResponse _deserialize:].cold.15
+ -[MIBUStatusResponse _deserialize:].cold.16
+ -[MIBUStatusResponse _deserialize:].cold.17
+ -[MIBUStatusResponse _deserialize:].cold.18
+ -[MIBUTestPreferences collectTCPDumpForWiFi]
+ -[MIBUTestPreferences skipPersonalizationDeletion]
+ -[MIBUTestPreferences wakedByRTCAlarm]
+ GCC_except_table32
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table74
+ GCC_except_table83
+ GCC_except_table90
+ GCC_except_table96
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1PublicKey
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1SKID
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1SPKI
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_public_key
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_skid
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_spki
+ _CFArrayGetTypeID
+ _CTEvaluateKeyTransparency
+ _CTEvaluateVLTileSigning
+ _CTGetAKIDFromCertificate
+ _CTGetSKIDFromCertificate
+ _CTOidAppleAAICA
+ _CTOidAppleKeyTransparencyLeaf
+ _CTOidAppleVLTilesSigning
+ _IOPMCopyScheduledPowerEvents
+ _IOPMSchedulePowerEvent
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1PublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1SKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1SPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWPublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWSKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWSPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_spki
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13PublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13SKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13SPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_spki
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_spki
+ _X509ExtensionParseKeyTransparencyLeaf
+ _X509PolicyVLTile
+ ___23-[MIBUClient shutdown:]_block_invoke.152
+ ___23-[MIBUClient shutdown:]_block_invoke.152.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke.152.cold.2
+ ___23-[MIBUClient shutdown:]_block_invoke.155
+ ___23-[MIBUClient shutdown:]_block_invoke.155.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke_2.156
+ ___23-[MIBUClient shutdown:]_block_invoke_2.156.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.109
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.109.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.109.cold.2
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.112
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.112.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke_2.113
+ ___28-[MIBUClient connectToWiFi:]_block_invoke_2.113.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.118
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.118.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.118.cold.2
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.121
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.121.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.122
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.122.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.47
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.47.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.47.cold.2
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.56
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.56.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.59
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.59.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.59.cold.2
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.63
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.63.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.60
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.60.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.64
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.64.cold.1
+ ___34+[MIBUPMUHelper wakedUpByRTCAlarm]_block_invoke
+ ___34+[MIBUPMUHelper wakedUpByRTCAlarm]_block_invoke.44
+ ___34+[MIBUPMUHelper wakedUpByRTCAlarm]_block_invoke.44.cold.1
+ ___34+[MIBUPMUHelper wakedUpByRTCAlarm]_block_invoke.47
+ ___34+[MIBUPMUHelper wakedUpByRTCAlarm]_block_invoke.47.cold.1
+ ___34+[MIBUPMUHelper wakedUpByRTCAlarm]_block_invoke.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.127
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.127.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.130
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.130.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.130.cold.2
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.133
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.133.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.134
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.134.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.70
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.70.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.73
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.73.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.76
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.76.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.76.cold.2
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.79
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.79.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.83
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.83.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.80
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.80.cold.1
+ ___35-[MIBUStatusResponse _deserialize:]_block_invoke.34
+ ___35-[MIBUStatusResponse _deserialize:]_block_invoke.34.cold.1
+ ___35-[MIBUStatusResponse _deserialize:]_block_invoke.40
+ ___35-[MIBUStatusResponse _deserialize:]_block_invoke.40.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.170
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.170.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.102
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.102.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.105
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.105.cold.1
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.108
+ ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.108.cold.1
+ ___39-[MIBUDeviceInfoResponse _deserialize:]_block_invoke.56
+ ___39-[MIBUDeviceInfoResponse _deserialize:]_block_invoke.56.cold.1
+ ___42-[MIBUClient isRTCAlarmSetWithCompletion:]_block_invoke
+ ___42-[MIBUClient isRTCAlarmSetWithCompletion:]_block_invoke.cold.1
+ ___42-[MIBUClient isRTCAlarmSetWithCompletion:]_block_invoke.cold.2
+ ___42-[MIBUClient isRTCAlarmSetWithCompletion:]_block_invoke_2
+ ___42-[MIBUClient isRTCAlarmSetWithCompletion:]_block_invoke_2.cold.1
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke.182
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke.182.cold.1
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke.182.cold.2
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke.185
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke.185.cold.1
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke.cold.1
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke_2
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke_2.186
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke_2.186.cold.1
+ ___43-[MIBUClient personalizationInfoWithError:]_block_invoke_2.cold.1
+ ___44+[MIBUPMUHelper scheduleRTCAlarmWakeOnDate:]_block_invoke
+ ___44+[MIBUPMUHelper scheduleRTCAlarmWakeOnDate:]_block_invoke.cold.1
+ ___45+[MIBUPMUHelper _configurePMUWithProperties:]_block_invoke
+ ___45+[MIBUPMUHelper _configurePMUWithProperties:]_block_invoke.113
+ ___45+[MIBUPMUHelper _configurePMUWithProperties:]_block_invoke.113.cold.1
+ ___45+[MIBUPMUHelper _configurePMUWithProperties:]_block_invoke.116
+ ___45+[MIBUPMUHelper _configurePMUWithProperties:]_block_invoke.116.cold.1
+ ___45+[MIBUPMUHelper _configurePMUWithProperties:]_block_invoke.cold.1
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.91
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.91.cold.1
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.91.cold.2
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.94
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.95
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.95.cold.1
+ ___49+[MIBUPMUHelper _checkPMUForProperties:outError:]_block_invoke
+ ___49+[MIBUPMUHelper _checkPMUForProperties:outError:]_block_invoke.cold.1
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.103
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.103.cold.1
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.103.cold.2
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.106
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.139
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.139.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.139.cold.2
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.142
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.142.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.143
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.143.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.170
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.170.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.173
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.173.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.173.cold.2
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.176
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.176.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.177
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.177.cold.1
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.192
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.192.cold.1
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.193
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.193.cold.1
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
+ ___block_literal_global.102
+ ___block_literal_global.107
+ ___block_literal_global.108
+ ___block_literal_global.111
+ ___block_literal_global.117
+ ___block_literal_global.120
+ ___block_literal_global.126
+ ___block_literal_global.129
+ ___block_literal_global.132
+ ___block_literal_global.141
+ ___block_literal_global.147
+ ___block_literal_global.149
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.175
+ ___block_literal_global.179
+ ___block_literal_global.184
+ ___block_literal_global.191
+ ___block_literal_global.195
+ ___block_literal_global.265
+ ___block_literal_global.87
+ ___block_literal_global.93
+ ___kCFBooleanTrue
+ ___swift__destructor
+ _algorithmIsPQCComposite
+ _cchybridsig_import_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_verify_prehashed_with_context
+ _isInPalletUpdateMode:.answerCached
+ _kMIBUClientLPMOptionRTCAlarmWakeDate
+ _kMIBUClientLPMOptionScanStartDate
+ _kMIBUClientPersonalizationNameKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_checkPMUForProperties:outError:
+ _objc_msgSend$_configurePMUWithProperties:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$enableLPMFlagForRTCAlarm
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isRTCAlarmSetWithReply:
+ _objc_msgSend$vendPersonalizationDataIfAvailableWithReply:
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _pqcCompositeAlgs
+ _sha512WithMLDSA87_RSA3072_draft13
+ _sha512WithMLDSA87_RSA3072_draft7
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x24
+ _validateSignaturePQCComposite
- +[MIBUPMUHelper enableLPMFlag]
- +[MIBUPMUHelper enableLPMFlag].cold.1
- +[MIBUPMUHelper enableLPMFlag].cold.2
- +[MIBUPMUHelper enableLPMFlag].cold.3
- +[MIBUPMUHelper enableLPMFlag].cold.4
- +[MIBUPMUHelper readLPMFlag:]
- -[MIBUTestPreferences usePythonLoopbackServer]
- GCC_except_table30
- GCC_except_table41
- GCC_except_table47
- GCC_except_table53
- GCC_except_table69
- GCC_except_table78
- GCC_except_table85
- _CFStringCreateWithCString
- _OUTLINED_FUNCTION_16
- _X509ExtensionParseMFIAuthv3Leaf
- ___23-[MIBUClient shutdown:]_block_invoke.136
- ___23-[MIBUClient shutdown:]_block_invoke.136.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke.136.cold.2
- ___23-[MIBUClient shutdown:]_block_invoke.139
- ___23-[MIBUClient shutdown:]_block_invoke.139.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke_2.140
- ___23-[MIBUClient shutdown:]_block_invoke_2.140.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke.95
- ___28-[MIBUClient connectToWiFi:]_block_invoke.95.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke.95.cold.2
- ___28-[MIBUClient connectToWiFi:]_block_invoke.98
- ___28-[MIBUClient connectToWiFi:]_block_invoke.98.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke_2.99
- ___28-[MIBUClient connectToWiFi:]_block_invoke_2.99.cold.1
- ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke
- ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke.38
- ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke.38.cold.1
- ___30+[MIBUPMUHelper enableLPMFlag]_block_invoke.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.104
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.104.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.104.cold.2
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.107
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.107.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.108
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.108.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.39
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.39.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.39.cold.2
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.43
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.43.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.48
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.48.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.51.cold.2
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.55
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.55.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.44
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.44.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.56
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.56.cold.1
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.113
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.113.cold.1
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.116
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.116.cold.1
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.116.cold.2
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.119
- ___34-[MIBUClient installFactoryAsset:]_block_invoke.119.cold.1
- ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.120
- ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.120.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.62
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.62.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.65
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.65.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.65.cold.2
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.68
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.68.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.69
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.69.cold.1
- ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.73
- ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.73.cold.1
- ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.76
- ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.76.cold.1
- ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.79
- ___39+[MIBUPMUHelper _findServicePmuPrimary]_block_invoke.79.cold.1
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.77
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.77.cold.1
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.77.cold.2
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.80
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.81
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.81.cold.1
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.89
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.89.cold.1
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.89.cold.2
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.92
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.125
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.125.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.125.cold.2
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.128
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.128.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.129
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.129.cold.1
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.154
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.154.cold.1
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.157
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.157.cold.1
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.157.cold.2
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.160
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.160.cold.1
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.161
- ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.161.cold.1
- ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.166
- ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.166.cold.1
- ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.167
- ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.167.cold.1
- ___block_literal_global.103
- ___block_literal_global.106
- ___block_literal_global.135
- ___block_literal_global.153
- ___block_literal_global.156
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.236
- ___block_literal_global.41
- ___block_literal_global.79
- ___block_literal_global.81
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "%s: Caching isInPalletUpdateMode = NO for this client!"
+ "%s: personalizationData = %{public}@; error = %{public}@"
+ "-[MIBUClient isInPalletUpdateMode:]"
+ "-[MIBUClient personalizationInfoWithError:]"
+ "-[MIBUClient personalizationInfoWithError:]_block_invoke"
+ "Cannot find IO registry entry property for IOPMUBootOff2WakeSource"
+ "Checking PMU for properties: %{public}@"
+ "CollectTCPDumpForWiFi"
+ "Configuring PMU with properties: %{public}@"
+ "Failed to deserialize build version"
+ "Failed to deserialize sep nonce"
+ "Failed to schedule RTC alarm wake event: 0x%x"
+ "IOPMUBootOff2WakeSource"
+ "LPMRTCAlarmWakeDate"
+ "LPMScanStartDate"
+ "PersonalizationName"
+ "Repair UCRT"
+ "SkipPersonalizationDeletion"
+ "Unexpected data type found for IOPMUBootOff2WakeSource"
+ "WakedByRTCAlarm"
+ "eventtype"
+ "poweron"
+ "rtc_alarm_wakeup"
+ "scheduledby"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<MIBUReaderServiceDelegate>\""
- "@\"MIBUDeviceNFC\""
- "@\"MIBUDeviceStatus\""
- "@\"MIBUNFCReaderSession\""
- "@\"MIBUNetworkInfo\""
- "@\"NFReaderSession\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<NFSession>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSOperationQueue\""
- "@\"NSRunLoop\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16Q24^@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8q16"
- "B32@0:8@16@24"
- "B32@0:8Q16^@24"
- "B32@0:8^@16^@24"
- "B40@0:8@16@24@32"
- "B40@0:8S16@20B28^@32"
- "B56@0:8@16@24@32@40@48"
- "B56@0:8^@16@24@32@40@48"
- "BSSID"
- "C"
- "C16@0:8"
- "I16@0:8"
- "IPv4Addresses"
- "IPv6Addresses"
- "JSONObjectWithData:options:error:"
- "MACAddress"
- "MCSIndex"
- "MIBUCertHelper"
- "MIBUChallengeResponse"
- "MIBUClient"
- "MIBUDefaultPreferences"
- "MIBUDeserializer"
- "MIBUDeviceBase"
- "MIBUDeviceInfoResponse"
- "MIBUDeviceNFC"
- "MIBUDeviceStatus"
- "MIBUEAPConfiguartion"
- "MIBUExtension"
- "MIBUNFCCommand"
- "MIBUNFCReaderSession"
- "MIBUNFCResponse"
- "MIBUNetworkInfo"
- "MIBUNetworkInfoResponse"
- "MIBUPMUHelper"
- "MIBUPersonalizationManager"
- "MIBUReaderService"
- "MIBUSelectResponse"
- "MIBUSerializationUtil"
- "MIBUSerializer"
- "MIBUStatusResponse"
- "MIBUTestPreferences"
- "MIBUXPCProtocol"
- "NFHardwareEventListener"
- "NFReaderSessionDelegate"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "PHYMode"
- "Q"
- "Q16@0:8"
- "RSSI"
- "S24@0:8@16"
- "SUCertPresent"
- "T#,R"
- "T#,R,GgetResponseClass"
- "T@\"<MIBUReaderServiceDelegate>\",&,N,V_delegate"
- "T@\"MIBUDeviceNFC\",&,N,V_device"
- "T@\"MIBUDeviceStatus\",&,N,V_status"
- "T@\"MIBUNFCReaderSession\",&,N,V_mibureaderSession"
- "T@\"MIBUNetworkInfo\",&,N,V_networkInfo"
- "T@\"NFReaderSession\",&,N,V_readerSession"
- "T@\"NSArray\",&,N,V_tags"
- "T@\"NSArray\",C,N,V_tlsCertificateChain"
- "T@\"NSData\",&,N,V_apNonce"
- "T@\"NSData\",&,N,V_certChainBlob"
- "T@\"NSData\",&,N,V_data"
- "T@\"NSData\",&,N,V_sepNonce"
- "T@\"NSData\",&,N,V_signatureBlob"
- "T@\"NSData\",R,N,V_apdu"
- "T@\"NSData\",R,N,V_serializedPayload"
- "T@\"NSDictionary\",&,N,V_batteryDetails"
- "T@\"NSDictionary\",&,N,V_operationDetails"
- "T@\"NSDictionary\",&,N,V_tagValDict"
- "T@\"NSDictionary\",&,N,V_thermalDetails"
- "T@\"NSDictionary\",&,N,V_updateSummary"
- "T@\"NSDictionary\",R,N"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSError\",&,N,V_operationError"
- "T@\"NSMutableData\",&,N,V_data"
- "T@\"NSMutableDictionary\",&,N,V_mutablePayload"
- "T@\"NSNumber\",&,N,V_batteryLevel"
- "T@\"NSNumber\",&,N,V_boardID"
- "T@\"NSNumber\",&,N,V_chipID"
- "T@\"NSNumber\",&,N,V_ecid"
- "T@\"NSNumber\",&,N,V_protocolVersion"
- "T@\"NSNumber\",&,N,V_sikaFuse"
- "T@\"NSNumber\",N,V_securityDomain"
- "T@\"NSNumber\",R,N,V_protocolVersion"
- "T@\"NSObject<NFSession>\",&,N,V_nfSession"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_deviceQueue"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_connectSem"
- "T@\"NSOperationQueue\",&,N,V_serviceQueue"
- "T@\"NSRunLoop\",&,N,V_runLoop"
- "T@\"NSString\",&,N,V_BSSID"
- "T@\"NSString\",&,N,V_MACAddress"
- "T@\"NSString\",&,N,V_buildVersion"
- "T@\"NSString\",&,N,V_iPV4Address"
- "T@\"NSString\",&,N,V_iPV6Address"
- "T@\"NSString\",&,N,V_networkName"
- "T@\"NSString\",&,N,V_osVersion"
- "T@\"NSString\",&,N,V_serialNumber"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_buildVersion"
- "T@\"NSString\",R,N,V_osVersion"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"_TtC17MobileInBoxUpdate24MIBULoopbackServerClient\",N,R"
- "TB,N,V_productionMode"
- "TB,N,V_rejected"
- "TB,N,V_securityMode"
- "TB,N,V_sikaFuseExists"
- "TB,N,V_suppressLogging"
- "TB,N,V_uidMode"
- "TB,R"
- "TB,R,N,V_protocolSupported"
- "TC,R,N,V_cla"
- "TC,R,N,V_ins"
- "TC,R,N,V_p1"
- "TC,R,N,V_p2"
- "TQ,N,V_MCSIndex"
- "TQ,N,V_PHYMode"
- "TQ,N,V_channelBand"
- "TQ,N,V_channelWidth"
- "TQ,N,V_numberOfSpatialStreams"
- "TQ,N,V_operation"
- "TQ,N,V_pos"
- "TQ,N,V_state"
- "TQ,R"
- "T^{__SecKey=},R,N,V_tlsKey"
- "Tq,N,V_RSSI"
- "Tq,N,V_channel"
- "Tq,N,V_entitlement"
- "Tq,N,V_noise"
- "Tq,R,N,V_code"
- "URLWithString:"
- "UTF8String"
- "Unexpected data type found for lpm3 key"
- "UsePythonLoopbackServer"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__AMAuthInstall=}32@0:8@16^@24"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}36@0:8@16B24^@28"
- "^{__SecKey=}"
- "^{__SecKey=}16@0:8"
- "_BSSID"
- "_MACAddress"
- "_MCSIndex"
- "_PHYMode"
- "_RSSI"
- "_TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper"
- "_TtC17MobileInBoxUpdate24MIBULoopbackServerClient"
- "_TtP17MobileInBoxUpdate32MIBULoopbackServerHelperProtocol_"
- "_apNonce"
- "_apdu"
- "_batteryDetails"
- "_batteryLevel"
- "_boardID"
- "_buildVersion"
- "_certChainBlob"
- "_channel"
- "_channelBand"
- "_channelWidth"
- "_chipID"
- "_cla"
- "_code"
- "_connectSem"
- "_connection"
- "_createBaseAMAIObjectForDevice:error:"
- "_data"
- "_delegate"
- "_deserialize:"
- "_deserializeAuthenticate"
- "_deserializeBatteryDetailsFromDict:"
- "_deserializeChallenge"
- "_deserializeConfigureNFC"
- "_deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:"
- "_deserializeFromTagDict:withKeyToTagMapping:"
- "_deserializeHeartbeat"
- "_deserializeNextTag:withData:"
- "_deserializeOperationDetailsFromDict:"
- "_deserializeRetryAfter"
- "_deserializeSSUpdate"
- "_deserializeShutdown"
- "_deserializeStartDiag"
- "_deserializeStartUpdate"
- "_deserializeTatsuPayload"
- "_deserializeThermalDetailsFromDict:"
- "_device"
- "_deviceQueue"
- "_ecid"
- "_entitlement"
- "_error"
- "_findServicePmuPrimary"
- "_getCertDataFromPath:error:"
- "_getInnermostNSError:"
- "_iPV4Address"
- "_iPV6Address"
- "_initWithAPDU:"
- "_initWithCommandCode:"
- "_ins"
- "_isActivated:"
- "_isIPad"
- "_isMac"
- "_isOnLockScreen"
- "_mibureaderSession"
- "_mutablePayload"
- "_networkInfo"
- "_networkName"
- "_nfSession"
- "_noise"
- "_numberOfSpatialStreams"
- "_operation"
- "_operationDetails"
- "_operationError"
- "_osVersion"
- "_p1"
- "_p2"
- "_pandoraCertificates:"
- "_parseDERCertificates:error:"
- "_pos"
- "_productionMode"
- "_protocolSupported"
- "_protocolVersion"
- "_readerSession"
- "_rejected"
- "_reverseDict:"
- "_runLoop"
- "_securityDomain"
- "_securityMode"
- "_sepNonce"
- "_serialNumber"
- "_serializeAuthenticate"
- "_serializeBatteryDetailsWithSerializer:"
- "_serializeChallenge"
- "_serializeConfigureNFC"
- "_serializeDict:fromKeyToTagMapping:withSerializer:"
- "_serializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:"
- "_serializeHeartbeat"
- "_serializeOperationDetailsWithSerializer:"
- "_serializeRetryAfter"
- "_serializeSSUpdate"
- "_serializeShutdown"
- "_serializeStartDiag"
- "_serializeStartUpdate"
- "_serializeTatsuPayload:"
- "_serializeThermalDetailsWithSerializer:"
- "_serializeValue:forTag:"
- "_serializedPayload"
- "_serviceQueue"
- "_setupConnection"
- "_signatureBlob"
- "_sikaFuse"
- "_sikaFuseExists"
- "_startDiagWithEntitlement:error:"
- "_state"
- "_status"
- "_suppressLogging"
- "_tagValDict"
- "_tags"
- "_thermalDetails"
- "_tlsCertificateChain"
- "_tlsKey"
- "_toJsonData:"
- "_uidMode"
- "_updateSummary"
- "_valueForTag:withData:"
- "acquireDarkWakeAssertionIfNeeded:"
- "activate"
- "addObject:"
- "addObjectsFromArray:"
- "addOperation:"
- "adjustData:toLength:"
- "apNonce"
- "apdu"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "arrayWithObjects:count:"
- "assetPath"
- "autorelease"
- "band"
- "batteryDetails"
- "batteryLevel"
- "blockOperationWithBlock:"
- "boardID"
- "boolValue"
- "buildVersion"
- "bytes"
- "certChainBlob"
- "certificatesFromData:error:"
- "channel"
- "channelBand"
- "channelWidth"
- "charValue"
- "chipID"
- "cla"
- "class"
- "code"
- "configureNFC:error:"
- "conformsToProtocol:"
- "connectSem"
- "connectTag:error:"
- "connectToWiFi:"
- "connectToWiFiWithReply:"
- "connection"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createArchiveFrom:to:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentRunLoop"
- "data"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithCapacity:"
- "dataWithContentsOfFile:options:error:"
- "dataWithHexString:"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodePropertyListForKey:"
- "defaultManager"
- "delegate"
- "deleteSUCert:"
- "description"
- "deserialize"
- "deserializeOperationError:"
- "deserializeResponseError:"
- "deviceDidConnect:"
- "deviceDidNotConnect"
- "deviceQueue"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeRadioState:"
- "didReceiveFatalCommunicationError"
- "disableNarrativeAuthentication"
- "disconnectTag:"
- "disconnectTagWithError:"
- "domain"
- "doubleValue"
- "eapConfigurationWithCompletion:"
- "eapConfigurationWithReply:"
- "ecid"
- "enableLPMFlag"
- "enablePipelineMode"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "end"
- "endSession"
- "enterLPMAfterUpdateComplete"
- "entitlement"
- "enumerateObjectsUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "expectedAPDULength:"
- "extractArchiveFrom:to:"
- "factoryAssetPaths"
- "factorySUCertExist"
- "factorySUCertPath"
- "factorySUKeyIsSEP"
- "factorySUKeyPath"
- "fakeBootManifestHash"
- "fakeTatsuPayloadPath"
- "fileExistsAtPath:"
- "firstObject"
- "generateRandomBytesOfSize:"
- "getBytes:length:"
- "getBytes:range:"
- "getDeviceInfo:"
- "getResponseClass"
- "getValueFromTestPreferencesForKey:"
- "hardwareStateDidChange"
- "hash"
- "hexStringRepresentation"
- "iPV4Address"
- "iPV6Address"
- "inBoxUpdateMode"
- "increaseLengthBy:"
- "init"
- "initWithAPDU:"
- "initWithBytes:length:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCoder:"
- "initWithCommandCode:andPayload:"
- "initWithContentsOfFile:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithFormat:arguments:"
- "initWithLength:"
- "initWithMachServiceName:options:"
- "initWithResponsePayload:"
- "initWithServiceName:"
- "initialBuddySetupComplete"
- "ins"
- "installFactoryAsset:"
- "installFactoryAssetWithReply:"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isActivated"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isInBoxUpdateMode:"
- "isInBoxUpdateModeWithReply:"
- "isInDiagnosticModeWithReply:"
- "isInPalletUpdateMode:"
- "isInPalletUpdateModeWithReply:"
- "isKindOfClass:"
- "isLPMSetWithReply:"
- "isLowPowerModeSetWithCompletion:"
- "isMemberOfClass:"
- "isOnLockScreen"
- "isProxy"
- "isValidJSONObject:"
- "iseTrustCertName"
- "iseTrustCertPaths"
- "length"
- "localizedDescription"
- "longLongValue"
- "longValue"
- "loopbackServerURL:"
- "maxLengthForTag:"
- "mibureaderSession"
- "mutableBytes"
- "mutableCopy"
- "mutablePayload"
- "networkInfo"
- "networkName"
- "nfSession"
- "nfcIdleTime"
- "noise"
- "numberOfSpatialStreams"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithShort:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operation"
- "operationCount"
- "operationDetails"
- "operationError"
- "osVersion"
- "p1"
- "p2"
- "pandoraCertsData:"
- "pandoraKeyServerURL"
- "payload"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pos"
- "productionMode"
- "protocolSupported"
- "protocolVersion"
- "q16@0:8"
- "queryNetworkInfo"
- "readBTFWOKFlag:"
- "readLPMFlag:"
- "readSUIdentityWithCompletion:"
- "readerSession"
- "readerSession:didDetectTags:"
- "readerSession:externalReaderFieldNotification:"
- "readerSessionDidEndUnexpectedly:"
- "readerSessionDidEndUnexpectedly:reason:"
- "rejected"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeItemAtPath:error:"
- "removeObjectForKey:"
- "requestAndVerifyTatsuTicketWithApNonce:outError:"
- "requestAndVerifyTatsuTicketWithApNonce:reply:"
- "requestTatsuTicketForDevice:error:"
- "requestTatsuTicketForDevice:withTimeout:error:"
- "requestTatsuTicketForResponse:error:"
- "respondsToSelector:"
- "responseClass"
- "resume"
- "retain"
- "retainCount"
- "run"
- "runLoop"
- "secureElement:didChangeRestrictedMode:"
- "securityDomain"
- "securityMode"
- "self"
- "sendCommand:withError:"
- "sepNonce"
- "serialNumber"
- "serialize"
- "serialize:withValue:"
- "serializeOperationError:"
- "serializeResponseError:"
- "serializedData"
- "serializedPayload"
- "serviceQueue"
- "setApNonce:"
- "setBSSID:"
- "setBatteryDetails:"
- "setBatteryLevel:"
- "setBoardID:"
- "setBuildVersion:"
- "setCertChainBlob:"
- "setChannel:"
- "setChannelBand:"
- "setChannelWidth:"
- "setChipID:"
- "setConnectSem:"
- "setConnection:"
- "setData:"
- "setDelegate:"
- "setDevice:"
- "setDeviceQueue:"
- "setEcid:"
- "setEntitlement:"
- "setError:"
- "setIPV4Address:"
- "setIPV6Address:"
- "setLowPowerModeWithOptions:completion:"
- "setMACAddress:"
- "setMCSIndex:"
- "setMaxConcurrentOperationCount:"
- "setMibureaderSession:"
- "setMutablePayload:"
- "setName:"
- "setNetworkInfo:"
- "setNetworkName:"
- "setNfSession:"
- "setNoise:"
- "setNumberOfSpatialStreams:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOperation:"
- "setOperationDetails:"
- "setOperationError:"
- "setOsVersion:"
- "setPHYMode:"
- "setPos:"
- "setProductionMode:"
- "setProtocolVersion:"
- "setRSSI:"
- "setReaderSession:"
- "setRejected:"
- "setRemoteObjectInterface:"
- "setRunLoop:"
- "setSecurityDomain:"
- "setSecurityMode:"
- "setSepNonce:"
- "setSerialNumber:"
- "setServiceQueue:"
- "setSignatureBlob:"
- "setSikaFuse:"
- "setSikaFuseExists:"
- "setState:"
- "setStatus:"
- "setSuppressLogging:"
- "setTLSKey:"
- "setTagValDict:"
- "setTags:"
- "setThermalDetails:"
- "setTlsCertificateChain:"
- "setToLPMWithOptions:reply:"
- "setUidMode:"
- "setUpdateSummary:"
- "sharedHardwareManagerWithNoUI"
- "sharedInstance"
- "shortValue"
- "shutdown:"
- "shutdownWithReply:"
- "signatureBlob"
- "sikaFuse"
- "sikaFuseExists"
- "skipCertDeletion"
- "skipDaemonDisable"
- "skipDeviceIdentityVerification"
- "skipWiFiAssociation"
- "softwareUpdateAssetPath"
- "softwareUpdateBrainAssetPath"
- "softwareUpdateBrainXMLPath"
- "softwareUpdateDownloadPath"
- "softwareUpdateXMLPath"
- "standardUserDefaults"
- "standbyIdleTimeout"
- "start"
- "start:"
- "startDiag:"
- "startDiagnostics:"
- "startPollingWithError:"
- "startReaderSession:"
- "startServerWithWebPort:webRoot:waitTillDone:error:"
- "startServerWithWebPort:webRoot:waitTillDone:with:"
- "startSession"
- "state"
- "status"
- "statusServerHostAddress"
- "statusServerPortNumber"
- "stopServer"
- "stopServerAndReturnError:"
- "stopWiFiMonitor:"
- "stopWiFiMonitorWithReply:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithString:"
- "suCertKeyFromData:isSEPKey:error:"
- "superclass"
- "supportsSecureCoding"
- "suppressLogging"
- "synchronize"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tagLengthMapping"
- "tagTypeMapping"
- "tagValDict"
- "tags"
- "tcpUnicastAddress"
- "tcpUnicastPort"
- "temperatureChanged:"
- "terminate"
- "terminateInBoxUpdateWithCompletion:"
- "terminateInBoxUpdateWithReply:"
- "thermalDetails"
- "tlsCertificateChain"
- "tlsKey"
- "transceive:error:"
- "trustCertificatesWithCompletion:"
- "typeForTag:"
- "typeLengthMapping"
- "uidMode"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "updateDeviceStatus:"
- "updateSummary"
- "useAppleConnect"
- "useAppleConnectSsoToken"
- "useLiveTatsu"
- "usePandoraNonProdCerts"
- "usePlistForDeviceIKM"
- "usePythonLoopbackServer"
- "useScriptForDeviceKey"
- "useSrNmForDeviceKey"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NFReaderSession\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSData\"B@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8^@16"
- "v24@0:8^{__SecKey=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"NFSecureElement\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"NFReaderSession\"16@\"NFFieldNotification\"24"
- "v32@0:8@\"NFReaderSession\"16@\"NSArray\"24"
- "v32@0:8@\"NFReaderSession\"16@\"NSError\"24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16^@24"
- "v40@0:8S16@\"NSString\"20B28@?<v@?>32"
- "v40@0:8S16@20B28@?32"
- "vendApTicketForTargetOS:reply:"
- "vendApTicketForTargetOSIfNeeded:outError:"
- "waitUntilAllOperationsAreFinished"
- "wakedFromLPMSU"
- "wakedUpFromLPMSU"
- "width"
- "wifiPassword"
- "wifiSSID"
- "zone"

```
