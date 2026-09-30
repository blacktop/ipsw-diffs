## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-153.80.10.0.0
-  __TEXT.__text: 0x2cdfc
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x1500
-  __TEXT.__const: 0x5eb8
-  __TEXT.__cstring: 0x14ca
-  __TEXT.__oslogstring: 0x2062
-  __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__swift5_typeref: 0x98
-  __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__constg_swiftt: 0x38
+176.100.32.0.0
+  __TEXT.__text: 0x3113c
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0x1790
+  __TEXT.__const: 0x5f58
+  __TEXT.__cstring: 0x15c5
+  __TEXT.__oslogstring: 0x2459
+  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__swift5_typeref: 0xdc
+  __TEXT.__swift5_fieldmd: 0x30
+  __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xb68
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x21c
-  __TEXT.__objc_methname: 0x2aea
-  __TEXT.__objc_methtype: 0x5a9
-  __TEXT.__objc_stubs: 0x28e0
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x3cc8
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__objc_classname: 0x2f0
+  __TEXT.__objc_methname: 0x2dd7
+  __TEXT.__objc_methtype: 0x688
+  __TEXT.__objc_stubs: 0x2a80
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x3cf8
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_selrefs: 0xe48
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x2440
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x24d0
-  __AUTH_CONST.__objc_intobj: 0x1158
-  __AUTH_CONST.__objc_arrayobj: 0x318
+  __DATA_CONST.__objc_arraydata: 0x260
+  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH_CONST.__const: 0x2668
+  __AUTH_CONST.__cfstring: 0x1a80
+  __AUTH_CONST.__objc_const: 0x2818
+  __AUTH_CONST.__objc_intobj: 0x11b8
+  __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x740
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x178
-  __DATA.__data: 0xef8
+  __AUTH.__objc_data: 0x7f0
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x1ac
+  __DATA.__data: 0xff0
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 4234A40C-DB5F-3224-9E57-1EBC4291233C
-  Functions: 1154
-  Symbols:   4473
-  CStrings:  1319
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 83D2050F-FDC3-3235-A791-3B15C27B947C
+  Functions: 1284
+  Symbols:   4910
+  CStrings:  1393
 
Symbols:
+ +[MIBUDeviceStatus supportsSecureCoding]
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:error:].cold.21
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:error:].cold.22
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:error:].cold.23
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:error:].cold.24
+ +[MIBUPersonalizationManager requestTatsuTicketForResponse:error:]
+ -[MIBUClient installFactoryAsset:]
+ -[MIBUClient installFactoryAsset:].cold.1
+ -[MIBUClient installFactoryAsset:].cold.2
+ -[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]
+ -[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]
+ -[MIBUClient vendApTicketForTargetOSIfNeeded:outError:].cold.1
+ -[MIBUClient vendApTicketForTargetOSIfNeeded:outError:].cold.2
+ -[MIBUDeviceBase apNonce]
+ -[MIBUDeviceBase boardID]
+ -[MIBUDeviceBase chipID]
+ -[MIBUDeviceBase ecid]
+ -[MIBUDeviceBase entitlement]
+ -[MIBUDeviceBase productionMode]
+ -[MIBUDeviceBase securityDomain]
+ -[MIBUDeviceBase securityMode]
+ -[MIBUDeviceBase sepNonce]
+ -[MIBUDeviceBase setApNonce:]
+ -[MIBUDeviceBase setBoardID:]
+ -[MIBUDeviceBase setChipID:]
+ -[MIBUDeviceBase setEcid:]
+ -[MIBUDeviceBase setEntitlement:]
+ -[MIBUDeviceBase setProductionMode:]
+ -[MIBUDeviceBase setSecurityDomain:]
+ -[MIBUDeviceBase setSecurityMode:]
+ -[MIBUDeviceBase setSepNonce:]
+ -[MIBUDeviceBase setSerialNumber:]
+ -[MIBUDeviceBase setSikaFuse:]
+ -[MIBUDeviceBase setSikaFuseExists:]
+ -[MIBUDeviceBase setSuppressLogging:]
+ -[MIBUDeviceBase setUidMode:]
+ -[MIBUDeviceBase sikaFuseExists]
+ -[MIBUDeviceBase sikaFuse]
+ -[MIBUDeviceBase suppressLogging]
+ -[MIBUDeviceBase uidMode]
+ -[MIBUDeviceNFC setSerialNumber:]
+ -[MIBUDeviceStatus description]
+ -[MIBUDeviceStatus encodeWithCoder:]
+ -[MIBUDeviceStatus initWithCoder:]
+ -[MIBUNFCCommand _deserializeSSUpdate].cold.19
+ -[MIBUNFCCommand _deserializeSSUpdate].cold.20
+ -[MIBUNFCCommand _serializeSSUpdate].cold.29
+ -[MIBUNFCCommand _serializeSSUpdate].cold.30
+ -[MIBUTestPreferences factoryAssetPaths]
+ -[MIBUTestPreferences fakeBootManifestHash]
+ -[MIBUTestPreferences softwareUpdateDownloadPath]
+ -[MIBUTestPreferences useAppleConnectSsoToken]
+ GCC_except_table53
+ GCC_except_table69
+ GCC_except_table78
+ GCC_except_table85
+ _AMAuthInstallSetSigningServerTimeout
+ _AMAuthInstallSsoSetToken
+ _CMSAttributeParseAppleHashAgilityV2
+ _CMSGetCertificateUsingIssuerSerialNumber
+ _CMSParseEncapsulatedContent
+ _CMSParseSignedData
+ _NSStringFromSelector
+ _OBJC_CLASS_$__TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper
+ _OBJC_IVAR_$_MIBUDeviceBase._apNonce
+ _OBJC_IVAR_$_MIBUDeviceBase._boardID
+ _OBJC_IVAR_$_MIBUDeviceBase._chipID
+ _OBJC_IVAR_$_MIBUDeviceBase._ecid
+ _OBJC_IVAR_$_MIBUDeviceBase._entitlement
+ _OBJC_IVAR_$_MIBUDeviceBase._productionMode
+ _OBJC_IVAR_$_MIBUDeviceBase._securityDomain
+ _OBJC_IVAR_$_MIBUDeviceBase._securityMode
+ _OBJC_IVAR_$_MIBUDeviceBase._sepNonce
+ _OBJC_IVAR_$_MIBUDeviceBase._sikaFuse
+ _OBJC_IVAR_$_MIBUDeviceBase._sikaFuseExists
+ _OBJC_IVAR_$_MIBUDeviceBase._suppressLogging
+ _OBJC_IVAR_$_MIBUDeviceBase._uidMode
+ _OBJC_METACLASS_$__TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ __CLASS_METHODS__TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper
+ __DATA__TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper
+ __INSTANCE_METHODS__TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper
+ __METACLASS_DATA__TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper
+ __OBJC_$_CLASS_METHODS_MIBUDeviceStatus
+ __OBJC_$_CLASS_PROP_LIST_MIBUDeviceStatus
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_MIBUDeviceStatus
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.62
+ ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.62.cold.1
+ ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.65
+ ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.65.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke.136
+ ___23-[MIBUClient shutdown:]_block_invoke.136.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke.136.cold.2
+ ___23-[MIBUClient shutdown:]_block_invoke.139
+ ___23-[MIBUClient shutdown:]_block_invoke.139.cold.1
+ ___23-[MIBUClient shutdown:]_block_invoke_2.140
+ ___23-[MIBUClient shutdown:]_block_invoke_2.140.cold.1
+ ___24-[MIBUReaderService run]_block_invoke.35.cold.2
+ ___24-[MIBUReaderService run]_block_invoke.38
+ ___24-[MIBUReaderService run]_block_invoke.38.cold.1
+ ___26-[MIBUDeviceNFC shutdown:]_block_invoke.81
+ ___26-[MIBUDeviceNFC shutdown:]_block_invoke.81.cold.1
+ ___27-[MIBUDeviceNFC endSession]_block_invoke.92
+ ___27-[MIBUDeviceNFC endSession]_block_invoke.92.cold.1
+ ___27-[MIBUDeviceNFC startDiag:]_block_invoke.53
+ ___27-[MIBUDeviceNFC startDiag:]_block_invoke.53.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.95
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.95.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.95.cold.2
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.98
+ ___28-[MIBUClient connectToWiFi:]_block_invoke.98.cold.1
+ ___28-[MIBUClient connectToWiFi:]_block_invoke_2.99
+ ___28-[MIBUClient connectToWiFi:]_block_invoke_2.99.cold.1
+ ___29-[MIBUDeviceNFC startSession]_block_invoke.30
+ ___29-[MIBUDeviceNFC startSession]_block_invoke.30.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.104
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.104.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.104.cold.2
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.107
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.107.cold.1
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.108
+ ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.108.cold.1
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.25
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.25.cold.1
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.25.cold.2
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.25.cold.3
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.25.cold.4
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.25.cold.5
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.31
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.31.cold.1
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.37
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.37.cold.1
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.43
+ ___30-[MIBUNFCReaderSession start:]_block_invoke.43.cold.1
+ ___30-[MIBUReaderService terminate]_block_invoke.30
+ ___30-[MIBUReaderService terminate]_block_invoke.30.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.39
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.39.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.39.cold.2
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.43
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.43.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.48
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.48.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.51
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.51.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.51.cold.2
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.55
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.55.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.44
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.44.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.52
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.52.cold.1
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.56
+ ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.56.cold.1
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.140
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.140.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.113
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.113.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.116
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.116.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.116.cold.2
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.119
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.119.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke_2
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.120
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.120.cold.1
+ ___34-[MIBUClient installFactoryAsset:]_block_invoke_2.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.65
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.65.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.65.cold.2
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.68
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.68.cold.1
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.69
+ ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.69.cold.1
+ ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.64
+ ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.64.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.242
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.242.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.245
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.245.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.253
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.253.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.261
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.261.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.269
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.269.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.277
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.277.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.285
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.285.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.293
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.293.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.301
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.301.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.309
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.309.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.317
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.317.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.325
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.325.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.333
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.333.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.341
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.341.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.349
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.349.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.357
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.357.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.365
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.365.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.373
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.373.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.381
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.381.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.389
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.389.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.397
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.397.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.405
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.405.cold.1
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.214
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.214.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.163
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.163.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.171
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.171.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.460
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.460.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.463
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.463.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.466
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.466.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.469
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.469.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.472
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.472.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.475
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.475.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.478
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.478.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.481
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.481.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.484
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.484.cold.1
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.150
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.150.cold.1
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.453
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.453.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.421
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.421.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.424
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.424.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.427
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.427.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.430
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.430.cold.1
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.102
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.102.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.413
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.413.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.416
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.416.cold.1
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.181
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.181.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.188
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.188.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.196
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.196.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.204
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.204.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.32
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.32.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.35
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.35.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.38
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.38.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.41
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.41.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.44
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.44.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.48
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.48.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.51
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.51.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.54
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.54.cold.1
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.57
+ ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.57.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.435
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.435.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.438
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.438.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.445
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.445.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.448
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.448.cold.1
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.77
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.77.cold.1
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.77.cold.2
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.80
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.81
+ ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.81.cold.1
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.89
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.89.cold.1
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.89.cold.2
+ ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.92
+ ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.20
+ ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.20.cold.1
+ ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.23
+ ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.23.cold.1
+ ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.26
+ ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.26.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.125
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.125.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.125.cold.2
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.128
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.128.cold.1
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.129
+ ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.129.cold.1
+ ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.80
+ ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.80.cold.1
+ ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.86
+ ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.86.cold.1
+ ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.92
+ ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.92.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.154
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.154.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.157
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.157.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.157.cold.2
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.160
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.160.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.161
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.161.cold.1
+ ___55-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke_2.cold.1
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.166
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.166.cold.1
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.cold.1
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke.cold.2
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.167
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.167.cold.1
+ ___62-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke_2.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.109
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.109.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.115
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.115.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.118
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.118.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.124
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.124.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.17
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.17.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.55
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.55.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.58
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.58.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.61
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.61.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.67
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.67.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.70
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.70.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.73
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.73.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.76
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.76.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.82
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.82.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.88
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.88.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.91
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.91.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.97
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.97.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.135
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.135.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.141
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.141.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.147
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.147.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.153
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.153.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.159
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.159.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.165
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.165.cold.1
+ ___block_literal_global.110
+ ___block_literal_global.111
+ ___block_literal_global.122
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.135
+ ___block_literal_global.137
+ ___block_literal_global.142
+ ___block_literal_global.143
+ ___block_literal_global.147
+ ___block_literal_global.148
+ ___block_literal_global.152
+ ___block_literal_global.153
+ ___block_literal_global.154
+ ___block_literal_global.155
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.169
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.190
+ ___block_literal_global.198
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.236
+ ___block_literal_global.244
+ ___block_literal_global.247
+ ___block_literal_global.25
+ ___block_literal_global.255
+ ___block_literal_global.263
+ ___block_literal_global.271
+ ___block_literal_global.279
+ ___block_literal_global.287
+ ___block_literal_global.295
+ ___block_literal_global.303
+ ___block_literal_global.311
+ ___block_literal_global.319
+ ___block_literal_global.327
+ ___block_literal_global.335
+ ___block_literal_global.343
+ ___block_literal_global.351
+ ___block_literal_global.359
+ ___block_literal_global.367
+ ___block_literal_global.375
+ ___block_literal_global.383
+ ___block_literal_global.391
+ ___block_literal_global.399
+ ___block_literal_global.407
+ ___block_literal_global.429
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.437
+ ___block_literal_global.440
+ ___block_literal_global.442
+ ___block_literal_global.444
+ ___block_literal_global.447
+ ___block_literal_global.450
+ ___block_literal_global.452
+ ___block_literal_global.455
+ ___block_literal_global.459
+ ___block_literal_global.462
+ ___block_literal_global.465
+ ___block_literal_global.468
+ ___block_literal_global.471
+ ___block_literal_global.474
+ ___block_literal_global.477
+ ___block_literal_global.480
+ ___block_literal_global.483
+ ___block_literal_global.486
+ ___block_literal_global.50
+ ___block_literal_global.53
+ ___block_literal_global.56
+ ___block_literal_global.60
+ ___block_literal_global.66
+ ___block_literal_global.69
+ ___block_literal_global.74
+ ___block_literal_global.83
+ ___block_literal_global.84
+ ___block_literal_global.90
+ ___block_literal_global.93
+ ___block_literal_global.99
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftAppleArchive_$_MobileInBoxUpdate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_MobileInBoxUpdate
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_MobileInBoxUpdate
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _kMIBUClientLPMOptionDelayStartInMinutes
+ _kMIBUClientLPMOptionScanDelayStart
+ _kMIBUNFCCommandRQFIFileRangesKey
+ _kMIBUNFCCommandRQSUFileRangesKey
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodePropertyListForKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$installFactoryAssetWithReply:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$requestAndVerifyTatsuTicketWithApNonce:reply:
+ _objc_msgSend$startServerWithWebPort:webRoot:waitTillDone:with:
+ _objc_msgSend$stopServer
+ _objc_msgSend$useAppleConnectSsoToken
+ _objc_msgSend$vendApTicketForTargetOS:reply:
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _swift_arrayDestroy
+ _swift_bridgeObjectRetain
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic Say_____G 12AppleArchive0B5FlagsV
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 17MobileInBoxUpdate22MIBUAppleArchiveHelperC
+ _symbolic _____Sg 6System8FilePathV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12AppleArchive0E5FlagsV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- GCC_except_table62
- ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.60
- ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.60.cold.1
- ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.63
- ___109-[MIBUDeserializer _deserializeError:withErrorCodeTag:errorDomainTag:errorDescriptionTag:underlyingErrorTag:]_block_invoke.63.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke.118
- ___23-[MIBUClient shutdown:]_block_invoke.118.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke.118.cold.2
- ___23-[MIBUClient shutdown:]_block_invoke.121
- ___23-[MIBUClient shutdown:]_block_invoke.121.cold.1
- ___23-[MIBUClient shutdown:]_block_invoke_2.122
- ___23-[MIBUClient shutdown:]_block_invoke_2.122.cold.1
- ___24-[MIBUReaderService run]_block_invoke.32
- ___24-[MIBUReaderService run]_block_invoke.32.cold.1
- ___24-[MIBUReaderService run]_block_invoke.32.cold.2
- ___26-[MIBUDeviceNFC shutdown:]_block_invoke.75
- ___26-[MIBUDeviceNFC shutdown:]_block_invoke.75.cold.1
- ___27-[MIBUDeviceNFC endSession]_block_invoke.89
- ___27-[MIBUDeviceNFC endSession]_block_invoke.89.cold.1
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.47
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.47.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke.89
- ___28-[MIBUClient connectToWiFi:]_block_invoke.89.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke.89.cold.2
- ___28-[MIBUClient connectToWiFi:]_block_invoke.92
- ___28-[MIBUClient connectToWiFi:]_block_invoke.92.cold.1
- ___28-[MIBUClient connectToWiFi:]_block_invoke_2.93
- ___28-[MIBUClient connectToWiFi:]_block_invoke_2.93.cold.1
- ___29-[MIBUDeviceNFC startSession]_block_invoke.27
- ___29-[MIBUDeviceNFC startSession]_block_invoke.27.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.101
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.101.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.98
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.98.cold.1
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke.98.cold.2
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.102
- ___30-[MIBUClient stopWiFiMonitor:]_block_invoke_2.102.cold.1
- ___30-[MIBUNFCReaderSession start:]_block_invoke.22
- ___30-[MIBUNFCReaderSession start:]_block_invoke.22.cold.1
- ___30-[MIBUNFCReaderSession start:]_block_invoke.22.cold.2
- ___30-[MIBUNFCReaderSession start:]_block_invoke.22.cold.3
- ___30-[MIBUNFCReaderSession start:]_block_invoke.22.cold.4
- ___30-[MIBUNFCReaderSession start:]_block_invoke.22.cold.5
- ___30-[MIBUNFCReaderSession start:]_block_invoke.28
- ___30-[MIBUNFCReaderSession start:]_block_invoke.28.cold.1
- ___30-[MIBUNFCReaderSession start:]_block_invoke.34
- ___30-[MIBUNFCReaderSession start:]_block_invoke.34.cold.1
- ___30-[MIBUNFCReaderSession start:]_block_invoke.40
- ___30-[MIBUNFCReaderSession start:]_block_invoke.40.cold.1
- ___30-[MIBUReaderService terminate]_block_invoke.27
- ___30-[MIBUReaderService terminate]_block_invoke.27.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.33
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.33.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.33.cold.2
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.37
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.37.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.42
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.42.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.45
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.45.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.45.cold.2
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.49
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke.49.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.38
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.38.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.46
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.46.cold.1
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.50
- ___32-[MIBUClient isInBoxUpdateMode:]_block_invoke_2.50.cold.1
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.104
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.104.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.56
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.56.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.59
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.59.cold.1
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke.59.cold.2
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.63
- ___35-[MIBUClient isInPalletUpdateMode:]_block_invoke_2.63.cold.1
- ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.61
- ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.61.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.218
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.218.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.247
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.247.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.255
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.255.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.263
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.263.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.271
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.271.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.279
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.279.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.287
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.287.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.295
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.295.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.303
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.303.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.311
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.311.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.319
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.319.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.327
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.327.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.335
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.335.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.343
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.343.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.351
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.351.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.359
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.359.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.367
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.367.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.375
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.375.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.383
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.383.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.391
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.391.cold.1
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.211
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.211.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.160
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.160.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.168
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.168.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.446
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.446.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.449
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.449.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.452
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.452.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.455
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.455.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.458
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.458.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.461
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.461.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.464
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.464.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.467
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.467.cold.1
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.147
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.147.cold.1
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.439
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.439.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.407
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.407.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.410
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.410.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.413
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.413.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.416
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.416.cold.1
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.99
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.99.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.399
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.399.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.402
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.402.cold.1
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.178
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.178.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.185
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.185.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.193
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.193.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.201
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.201.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.30
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.30.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.33
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.33.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.36
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.36.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.39
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.39.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.42
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.42.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.46
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.46.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.49
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.49.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.52
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.52.cold.1
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.55
- ___42-[MIBUDeserializer _valueForTag:withData:]_block_invoke.55.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.421
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.421.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.424
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.424.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.431
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.431.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.434
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.434.cold.1
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.71
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.71.cold.1
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.71.cold.2
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke.74
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.75
- ___45-[MIBUClient eapConfigurationWithCompletion:]_block_invoke_2.75.cold.1
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.83
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.83.cold.1
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.83.cold.2
- ___49-[MIBUClient terminateInBoxUpdateWithCompletion:]_block_invoke.86
- ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.18
- ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.18.cold.1
- ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.21
- ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.21.cold.1
- ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.24
- ___49-[MIBUDeserializer _deserializeNextTag:withData:]_block_invoke.24.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.107
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.107.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.107.cold.2
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.110
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke.110.cold.1
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.111
- ___52-[MIBUClient setLowPowerModeWithOptions:completion:]_block_invoke_2.111.cold.1
- ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.77
- ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.77.cold.1
- ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.83
- ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.83.cold.1
- ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.89
- ___52-[MIBUNFCReaderSession readerSession:didDetectTags:]_block_invoke.89.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.101
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.101.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.107
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.107.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.15
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.15.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.53
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.53.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.56
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.56.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.59
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.59.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.65
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.65.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.68
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.68.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.71
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.71.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.74
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.74.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.80
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.80.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.92
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.92.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.98
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.98.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.118
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.118.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.124
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.124.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.130
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.130.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.136
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.136.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.142
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.142.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.148
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.148.cold.1
- ___block_literal_global.100
- ___block_literal_global.113
- ___block_literal_global.132
- ___block_literal_global.14
- ___block_literal_global.141
- ___block_literal_global.150
- ___block_literal_global.151
- ___block_literal_global.162
- ___block_literal_global.17
- ___block_literal_global.170
- ___block_literal_global.171
- ___block_literal_global.172
- ___block_literal_global.180
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.20
- ___block_literal_global.203
- ___block_literal_global.205
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.23
- ___block_literal_global.249
- ___block_literal_global.257
- ___block_literal_global.26
- ___block_literal_global.265
- ___block_literal_global.273
- ___block_literal_global.281
- ___block_literal_global.289
- ___block_literal_global.297
- ___block_literal_global.305
- ___block_literal_global.313
- ___block_literal_global.321
- ___block_literal_global.329
- ___block_literal_global.337
- ___block_literal_global.345
- ___block_literal_global.35
- ___block_literal_global.353
- ___block_literal_global.361
- ___block_literal_global.369
- ___block_literal_global.377
- ___block_literal_global.385
- ___block_literal_global.393
- ___block_literal_global.395
- ___block_literal_global.398
- ___block_literal_global.401
- ___block_literal_global.404
- ___block_literal_global.406
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.44
- ___block_literal_global.441
- ___block_literal_global.443
- ___block_literal_global.445
- ___block_literal_global.448
- ___block_literal_global.451
- ___block_literal_global.454
- ___block_literal_global.460
- ___block_literal_global.463
- ___block_literal_global.466
- ___block_literal_global.469
- ___block_literal_global.51
- ___block_literal_global.62
- ___block_literal_global.77
- ___block_literal_global.85
- ___block_literal_global.95
- _kMIBUNFCCommandInterfaceNameKey
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
CStrings:
+ "%s: Device woke up from LPMSU = %{bool}d"
+ "%s: entered."
+ "%{public}@: Failed to load AC SSO token from file: %{public}@"
+ "%{public}@: Failed to set AC SSO token, status: %d"
+ "%{public}@: Loading AC SSO token: %{public}@"
+ "%{public}@: Sending Tatsu personalization request with timeout: %f..."
+ "-[MIBUClient installFactoryAsset:]_block_invoke"
+ "-[MIBUClient requestAndVerifyTatsuTicketWithApNonce:outError:]_block_invoke"
+ "-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]"
+ "-[MIBUClient vendApTicketForTargetOSIfNeeded:outError:]_block_invoke"
+ "<MIBUDeviceStatus: State=%lu Op=%lu>"
+ "@24@0:8@\"NSCoder\"16"
+ "AppleArchiveHelper"
+ "Creating Apple Archive from contents of folder: %s to: %s"
+ "Device is NOT booted from LPMSU and not in InBoxUpdate mode"
+ "Done creating Apple Archive. Total time taken: %lld secs"
+ "Done extracting Apple Archive. Total time taken: %lld secs"
+ "Extracting contents of Apple Archive from: %s to: %s"
+ "FactoryAssetPaths"
+ "Failed to archive directory contents: %@"
+ "Failed to create compress stream."
+ "Failed to create decode stream."
+ "Failed to create decompress stream."
+ "Failed to create directory: %@"
+ "Failed to create encode stream."
+ "Failed to create extract stream."
+ "Failed to create read file stream."
+ "Failed to create write file stream."
+ "Failed to deserialize factory install file ranges from command"
+ "Failed to deserialize software update file ranges from command"
+ "Failed to load AC SSO token from file"
+ "Failed to set AC SSO token, status: %d"
+ "Failed to unarchive directory contents: %@"
+ "FakeBootManifestHash"
+ "LPMDelayStartInMinutes"
+ "LPMScanDelayStart"
+ "NSCoding"
+ "NSSecureCoding"
+ "RQFIFileRanges"
+ "RQSUFileRanges"
+ "SoftwareUpdateDownloadPath"
+ "TB,R"
+ "Tq,N,V_entitlement"
+ "UseAppleConnectSsoToken"
+ "_TtC17MobileInBoxUpdate22MIBUAppleArchiveHelper"
+ "createArchiveFrom:to:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithContentsOfFile:options:error:"
+ "decodeObjectOfClass:forKey:"
+ "decodePropertyListForKey:"
+ "enableDarkWakeWithReply is NOT supported on iOS"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "extractArchiveFrom:to:"
+ "factoryAssetPaths"
+ "fakeBootManifestHash"
+ "initWithCoder:"
+ "installFactoryAsset:"
+ "installFactoryAssetWithReply:"
+ "localizedDescription"
+ "requestAndVerifyTatsuTicketWithApNonce:outError:"
+ "requestAndVerifyTatsuTicketWithApNonce:reply:"
+ "requestTatsuTicketForResponse:error:"
+ "softwareUpdateDownloadPath"
+ "supportsSecureCoding"
+ "useAppleConnectSsoToken"
+ "v24@0:8@\"NSCoder\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "vendApTicketForTargetOS:reply:"
+ "vendApTicketForTargetOSIfNeeded:outError:"
- "%s acquireDarkWakeAssertionIfNeeded"
- "%{public}@: Sending Tatsu personalization request..."
- "Failed to deserialize interface name from command"
- "InterfaceName"
- "T@\"NSString\",R,N,V_serialNumber"

```
