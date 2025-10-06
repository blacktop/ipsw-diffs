## accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

-898.80.3.0.0
-  __TEXT.__text: 0x1e220c
-  __TEXT.__auth_stubs: 0x1790
+919.100.33.0.0
+  __TEXT.__text: 0x1eb5c0
+  __TEXT.__auth_stubs: 0x17c0
   __TEXT.__objc_stubs: 0x88e0
-  __TEXT.__objc_methlist: 0x5734
-  __TEXT.__cstring: 0xb294
-  __TEXT.__oslogstring: 0x324ee
-  __TEXT.__const: 0x1e18
+  __TEXT.__objc_methlist: 0x5744
+  __TEXT.__cstring: 0xb68d
+  __TEXT.__oslogstring: 0x3313a
+  __TEXT.__const: 0x1e28
   __TEXT.__gcc_except_tab: 0x101c
-  __TEXT.__objc_methname: 0xee9e
+  __TEXT.__objc_methname: 0xef1c
   __TEXT.__objc_classname: 0x1025
-  __TEXT.__objc_methtype: 0x2e9d
+  __TEXT.__objc_methtype: 0x2f4e
   __TEXT.__ustring: 0x232
-  __TEXT.__unwind_info: 0x3960
-  __DATA_CONST.__auth_got: 0xbd8
-  __DATA_CONST.__got: 0x970
+  __TEXT.__unwind_info: 0x3994
+  __DATA_CONST.__auth_got: 0xbf0
+  __DATA_CONST.__got: 0x9f0
   __DATA_CONST.__auth_ptr: 0xb8
-  __DATA_CONST.__const: 0x6380
-  __DATA_CONST.__cfstring: 0x6440
+  __DATA_CONST.__const: 0x6410
+  __DATA_CONST.__cfstring: 0x65c0
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_classrefs: 0x468
+  __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0xcfa8
-  __DATA.__objc_selrefs: 0x2fc8
-  __DATA.__objc_protorefs: 0x150
-  __DATA.__objc_classrefs: 0x468
-  __DATA.__objc_superrefs: 0x300
+  __DATA.__objc_const: 0xcfc8
+  __DATA.__objc_selrefs: 0x2fd0
   __DATA.__objc_ivar: 0x710
   __DATA.__objc_data: 0x1e50
   __DATA.__data: 0x1a80

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B821EAAF-1895-36CD-BC09-CD24181B5A68
-  Functions: 9881
-  Symbols:   55465
-  CStrings:  8533
+  UUID: 30DF7584-2AC1-32F3-90FE-5ADB6E839D43
+  Functions: 10056
+  Symbols:   56376
+  CStrings:  8639
 
Symbols:
+ -[ACCExternalAccessoryServerRemote sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:]
+ -[ACCExternalAccessoryServerRemote sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:].cold.1
+ /AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTCompress.o)
+ /AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessoryd.build/Objects-normal/arm64e/mfi4Auth_relay.o
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessoryd.build/Objects-normal/arm64e/mfi4Auth_relay_device.o
+ _ACCBLEPairingAccPlatformID
+ _CFDictionaryApplierFunction_findWirelessCTADonorCapableConnection.cold.4
+ _CFDictionaryApplierFunction_findWirelessCTADonorCapableConnection.cold.5
+ _CFNumberCompare
+ _MFAADeviceIdentityCertsExist
+ _X509ExtensionParseCertifiedChipIntermediate
+ __115-[ACCExternalAccessoryServer handleIncomingExternalAccessoryData:forEASessionIdentifier:toExternalAccessoryClient:]_block_invoke.128
+ __115-[ACCExternalAccessoryServer handleIncomingExternalAccessoryData:forEASessionIdentifier:toExternalAccessoryClient:]_block_invoke.128.cold.1
+ __115-[ACCExternalAccessoryServer handleIncomingExternalAccessoryData:forEASessionIdentifier:toExternalAccessoryClient:]_block_invoke.128.cold.2
+ __51-[ACCHIDServer listener:shouldAcceptNewConnection:]_block_invoke.71
+ __51-[ACCHIDServer listener:shouldAcceptNewConnection:]_block_invoke.71.cold.1
+ __51-[ACCHIDServer listener:shouldAcceptNewConnection:]_block_invoke.71.cold.2
+ __52-[ACCExternalAccessoryServer externalAccessoryLeft:]_block_invoke.118
+ __52-[ACCExternalAccessoryServer externalAccessoryLeft:]_block_invoke.118.cold.1
+ __52-[ACCExternalAccessoryServer externalAccessoryLeft:]_block_invoke.118.cold.2
+ __52-[ACCNowPlayingServer triggerMediaItemArtworkUpdate]_block_invoke.85
+ __52-[ACCNowPlayingServer triggerMediaItemArtworkUpdate]_block_invoke.85.cold.1
+ __53-[ACCAudioServer listener:shouldAcceptNewConnection:]_block_invoke.59
+ __53-[ACCAudioServer listener:shouldAcceptNewConnection:]_block_invoke.59.cold.1
+ __53-[ACCAudioServer listener:shouldAcceptNewConnection:]_block_invoke.59.cold.2
+ __54-[ACCNowPlayingServer triggerPlaybackAttributesUpdate]_block_invoke.90
+ __54-[ACCNowPlayingServer triggerPlaybackAttributesUpdate]_block_invoke.90.cold.1
+ __55-[ACCExternalAccessoryServer externalAccessoryArrived:]_block_invoke.112.cold.1
+ __55-[ACCExternalAccessoryServer externalAccessoryArrived:]_block_invoke.112.cold.2
+ __55-[ACCExternalAccessoryServer externalAccessoryArrived:]_block_invoke.116
+ __55-[ACCNowPlayingServer triggerMediaItemAttributesUpdate]_block_invoke.80
+ __55-[ACCNowPlayingServer triggerMediaItemAttributesUpdate]_block_invoke.80.cold.1
+ __57-[ACCTransportServer listener:shouldAcceptNewConnection:]_block_invoke.113
+ __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.123
+ __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.123.cold.1
+ __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.123.cold.2
+ __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.125
+ __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.125.cold.1
+ __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.164
+ __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.168
+ __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.168.cold.1
+ __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.168.cold.2
+ __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.170.cold.1
+ __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.171
+ __58-[ACCExternalAccessoryServer updateExternalAccessoryInfo:]_block_invoke.121
+ __58-[ACCExternalAccessoryServer updateExternalAccessoryInfo:]_block_invoke.121.cold.1
+ __58-[ACCExternalAccessoryServer updateExternalAccessoryInfo:]_block_invoke.121.cold.2
+ __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.146
+ __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.146.cold.1
+ __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.146.cold.2
+ __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.149
+ __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.149.cold.1
+ __58-[ACCNowPlayingServer listener:shouldAcceptNewConnection:]_block_invoke.73
+ __58-[ACCNowPlayingServer listener:shouldAcceptNewConnection:]_block_invoke.73.cold.1
+ __58-[ACCNowPlayingServer listener:shouldAcceptNewConnection:]_block_invoke.73.cold.2
+ __60-[ACCCommunicationsServer invokeBlockOnClients:synchronous:]_block_invoke.86
+ __60-[ACCCommunicationsServer invokeBlockOnClients:synchronous:]_block_invoke.86.cold.1
+ __60-[ACCCommunicationsServer invokeBlockOnClients:synchronous:]_block_invoke.86.cold.2
+ __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.172
+ __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.172.cold.1
+ __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.172.cold.2
+ __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.174
+ __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.129
+ __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.129.cold.1
+ __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.129.cold.2
+ __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.131
+ __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.131.cold.1
+ __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.112
+ __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.112.cold.1
+ __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.112.cold.2
+ __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.114
+ __62-[ACCCommunicationsServer listener:shouldAcceptNewConnection:]_block_invoke.82
+ __62-[ACCCommunicationsServer listener:shouldAcceptNewConnection:]_block_invoke.82.cold.1
+ __62-[ACCCommunicationsServer listener:shouldAcceptNewConnection:]_block_invoke.82.cold.2
+ __62-[ACCConnectionInfoServer listener:shouldAcceptNewConnection:]_block_invoke.190
+ __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.108
+ __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.108.cold.1
+ __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.108.cold.2
+ __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.108.cold.3
+ __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.108.cold.4
+ __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.109
+ __65-[ACCExternalAccessoryServer notifyClientOfConnectedAccessories:]_block_invoke.133
+ __65-[ACCExternalAccessoryServer notifyClientOfConnectedAccessories:]_block_invoke.133.cold.1
+ __65-[ACCExternalAccessoryServer notifyClientOfConnectedAccessories:]_block_invoke.133.cold.2
+ __67-[ACCExternalAccessoryServer notifyClientOfConnectedVehicleStatus:]_block_invoke.138
+ __67-[ACCExternalAccessoryServer notifyClientOfConnectedVehicleStatus:]_block_invoke.138.cold.1
+ __67-[ACCExternalAccessoryServer notifyClientOfConnectedVehicleStatus:]_block_invoke.138.cold.2
+ __79-[ACCExternalAccessoryServer sendNMEASentence:forAccessoryUUID:withTimestamps:]_block_invoke.130
+ __79-[ACCExternalAccessoryServer sendNMEASentence:forAccessoryUUID:withTimestamps:]_block_invoke.130.cold.1
+ __79-[ACCExternalAccessoryServer sendNMEASentence:forAccessoryUUID:withTimestamps:]_block_invoke.130.cold.2
+ __83-[ACCTransportServer sendOutgoingData:forEndpointWithUUID:connectionUUID:toClient:]_block_invoke.117
+ __83-[ACCTransportServer sendOutgoingData:forEndpointWithUUID:connectionUUID:toClient:]_block_invoke.117.cold.1
+ __83-[ACCTransportServer sendOutgoingData:forEndpointWithUUID:connectionUUID:toClient:]_block_invoke.117.cold.2
+ ____mfi4Auth_endpoint_isEndpointSupportsMutualAuth_block_invoke
+ ___block_descriptor_32_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16l
+ ___block_descriptor_40_e8_32r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
+ ___block_descriptor_40_e8_32s_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8
+ ___block_descriptor_48_e8_32r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
+ ___block_descriptor_48_e8_32s40r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
+ ___block_descriptor_50_e8_32s40r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e196_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r56l8s40l8s48l8
+ ___mfi4Auth_endpoint_isEndpointSupportsMutualAuth_block_invoke.cold.1
+ ___mfi4Auth_endpoint_isEndpointSupportsMutualAuth_block_invoke.cold.2
+ ___presentShareWiFiCredentialsNotification_block_invoke.103
+ __audioProductCerts_endpoint_generateAuthChallenge
+ __audioProductCerts_endpoint_handleAuthResponseWithMissingCert
+ __audioProductCerts_endpoint_handleMissingCertList
+ __audioProductCerts_endpoint_handlePrimaryBudMismatch
+ __audioProductCerts_endpoint_validateChallenge
+ __block_descriptor_tmp.18
+ __block_literal_global.124
+ __block_literal_global.126
+ __block_literal_global.132
+ __block_literal_global.135
+ __block_literal_global.137
+ __block_literal_global.142
+ __block_literal_global.144
+ __block_literal_global.152
+ __block_literal_global.154
+ __block_literal_global.195
+ __block_literal_global.197
+ __block_literal_global.199
+ __block_literal_global.201
+ __block_literal_global.203
+ __block_literal_global.205
+ __block_literal_global.207
+ __block_literal_global.209
+ __block_literal_global.211
+ __block_literal_global.216
+ __block_literal_global.229
+ __block_literal_global.231
+ __block_literal_global.60
+ __block_literal_global.64
+ __block_literal_global.68
+ __block_literal_global.72
+ __block_literal_global.75
+ __block_literal_global.80
+ __block_literal_global.82
+ __block_literal_global.85
+ __block_literal_global.89
+ __block_literal_global.92
+ __block_literal_global.94
+ __block_literal_global.96
+ __block_literal_global.98
+ __main_block_invoke.106
+ __main_block_invoke.106.cold.1
+ __main_block_invoke.106.cold.2
+ __main_block_invoke.56
+ __main_block_invoke.62
+ __main_block_invoke.62.cold.1
+ __main_block_invoke.66
+ __main_block_invoke.66.cold.1
+ __main_block_invoke.70
+ __main_block_invoke.70.cold.1
+ _acc_endpoint_setEndpointSecureTunnelDataReceiveTypeHandler
+ _acc_platform_packetLogging_logEventVA
+ _acc_protocolRouter_setSecureTunnelDataTypeHandler
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.1
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.2
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.3
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.4
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.5
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.6
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.7
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.8
+ _audioProductCerts_endpoint_generateAuthChallenge.cold.9
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.1
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.10
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.11
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.12
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.13
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.2
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.3
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.4
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.5
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.6
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.7
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.8
+ _audioProductCerts_endpoint_handleAuthResponseWithMissingCert.cold.9
+ _audioProductCerts_endpoint_handleMissingCertList.cold.1
+ _audioProductCerts_endpoint_handleMissingCertList.cold.10
+ _audioProductCerts_endpoint_handleMissingCertList.cold.11
+ _audioProductCerts_endpoint_handleMissingCertList.cold.12
+ _audioProductCerts_endpoint_handleMissingCertList.cold.13
+ _audioProductCerts_endpoint_handleMissingCertList.cold.14
+ _audioProductCerts_endpoint_handleMissingCertList.cold.15
+ _audioProductCerts_endpoint_handleMissingCertList.cold.16
+ _audioProductCerts_endpoint_handleMissingCertList.cold.2
+ _audioProductCerts_endpoint_handleMissingCertList.cold.3
+ _audioProductCerts_endpoint_handleMissingCertList.cold.4
+ _audioProductCerts_endpoint_handleMissingCertList.cold.5
+ _audioProductCerts_endpoint_handleMissingCertList.cold.6
+ _audioProductCerts_endpoint_handleMissingCertList.cold.7
+ _audioProductCerts_endpoint_handleMissingCertList.cold.8
+ _audioProductCerts_endpoint_handleMissingCertList.cold.9
+ _audioProductCerts_endpoint_handlePrimaryBudMismatch.cold.1
+ _audioProductCerts_endpoint_handlePrimaryBudMismatch.cold.2
+ _audioProductCerts_endpoint_handlePrimaryBudMismatch.cold.3
+ _audioProductCerts_endpoint_handlePrimaryBudMismatch.cold.4
+ _audioProductCerts_endpoint_validateChallenge.cold.1
+ _audioProductCerts_endpoint_validateChallenge.cold.10
+ _audioProductCerts_endpoint_validateChallenge.cold.11
+ _audioProductCerts_endpoint_validateChallenge.cold.12
+ _audioProductCerts_endpoint_validateChallenge.cold.13
+ _audioProductCerts_endpoint_validateChallenge.cold.14
+ _audioProductCerts_endpoint_validateChallenge.cold.15
+ _audioProductCerts_endpoint_validateChallenge.cold.16
+ _audioProductCerts_endpoint_validateChallenge.cold.17
+ _audioProductCerts_endpoint_validateChallenge.cold.18
+ _audioProductCerts_endpoint_validateChallenge.cold.19
+ _audioProductCerts_endpoint_validateChallenge.cold.2
+ _audioProductCerts_endpoint_validateChallenge.cold.20
+ _audioProductCerts_endpoint_validateChallenge.cold.3
+ _audioProductCerts_endpoint_validateChallenge.cold.4
+ _audioProductCerts_endpoint_validateChallenge.cold.5
+ _audioProductCerts_endpoint_validateChallenge.cold.6
+ _audioProductCerts_endpoint_validateChallenge.cold.7
+ _audioProductCerts_endpoint_validateChallenge.cold.8
+ _audioProductCerts_endpoint_validateChallenge.cold.9
+ _ccec_add_normalized_ws
+ _ccec_map_to_homogeneous_ws
+ _convertNVMEraseResponse.cold.3
+ _convertNVMReadResponse.cold.5
+ _convertNVMWriteResponse.cold.3
+ _handleNvmReadAccessoryInfo.cold.16
+ _iap2_identification_isIdentifiedForThemeAssets
+ _kACCInfo_AccessoryPlatformID
+ _kACCVehicleInfoPowerForConnectorTypeNACS_ACKey
+ _kACCVehicleInfoPowerForConnectorTypeNACS_DCKey
+ _kCFACCInfo_AccessoryPlatformID
+ _kCFACCProperties_Endpoint_DigitalCarKey_CCCBrand
+ _kCFACCProperties_Endpoint_DigitalCarKey_CCCManufacturer
+ _kCFACCProperties_Endpoint_DigitalCarKey_Group
+ _kCFACCProperties_Endpoint_DigitalCarKey_OnlineServicesActivated
+ _kCFACCProperties_Endpoint_DigitalCarKey_OwnerKeyPairingAvailable
+ _kCFACCProperties_Endpoint_DigitalCarKey_ProductPlanUID
+ _kCFACCProperties_Endpoint_DigitalCarKey_ProofOfOwnershipPresent
+ _kCFACCProperties_Endpoint_DigitalCarKey_ProvisioningTemplate
+ _kCFACCProperties_Endpoint_DigitalCarKey_SupportedRadioTechnologies
+ _kCFACCProperties_Endpoint_DigitalCarKey_VehicleIdentifier
+ _kCFACCProperties_Endpoint_MFi4Auth_OneWayOnly
+ _kCFACCProperties_Endpoint_NFC_TagId
+ _kCFACCUserDefaultsKey_IgnoreAuthReset
+ _kCFACCUserDefaultsKey_MFi4ECDSADisallow
+ _kCFACCUserDefaultsKey_MFi4ECDSAOnly
+ _kCFACCUserDefaultsKey_MFi4SigmaIRequired
+ _kCFACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _malloc
+ _mfi4Auth_endpoint_handlePropertiesDidChange.cold.1
+ _mfi4Auth_endpoint_initSession.cold.2
+ _mfi4Auth_endpoint_initSession.cold.3
+ _mfi4Auth_endpoint_initSession.cold.4
+ _mfi4Auth_endpoint_initSession.cold.5
+ _mfi4Auth_endpoint_initSession.cold.6
+ _mfi4Auth_endpoint_initSession.cold.7
+ _mfi4Auth_endpoint_setEndpointSecureTunnelDataReceiveTypeHandler
+ _mfi4Auth_protocol_cleanupNVMContext
+ _mfi4Auth_protocol_initIdentityCerts
+ _mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler
+ _mfi4Auth_protocol_processIncomingMessageRelay
+ _mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler
+ _mfi4Auth_protocol_supportsRelay
+ _mfi4Auth_relay_cleanup
+ _mfi4Auth_relay_handle_iAP2RelayFailed
+ _mfi4Auth_relay_handle_iAP2RelayRemote
+ _mfi4Auth_relay_handle_iAP2RelaySucceeded
+ _mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote
+ _mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_TypeData
+ _mfi4Auth_relay_initMessage_RequestiAP2RelayRead
+ _mfi4Auth_util_packIntoTunnelDataiAP2Msg
+ _mfi4Auth_util_packetLoggingEncryptedData
+ _mfi4Auth_util_packetLogging_logData
+ _mfi4Auth_util_unpackFromTunnelDataiAP2Msg
+ _oobPairing_endpoint_copyCachedOOBPairingInfo
+ _parseIdentificationParams.cold.10
+ _parseIdentificationParams.cold.11
+ _parseIdentificationParams.cold.12
+ _parseIdentificationParams.cold.13
+ _parseIdentificationParams.cold.14
+ _parseIdentificationParams.cold.15
+ _parseIdentificationParams.cold.16
+ _parseIdentificationParams.cold.17
+ _parseIdentificationParams.cold.18
+ _parseIdentificationParams.cold.19
+ _parseIdentificationParams.cold.20
+ _parseIdentificationParams.cold.21
+ _parseIdentificationParams.cold.22
+ _parseIdentificationParams.cold.23
+ _parseIdentificationParams.cold.24
+ _parseIdentificationParams.cold.25
+ _parseIdentificationParams.cold.26
+ _parseIdentificationParams.cold.27
+ _parseIdentificationParams.cold.28
+ _parseIdentificationParams.cold.29
+ _parseIdentificationParams.cold.30
+ _parseIdentificationParams.cold.31
+ _parseIdentificationParams.cold.32
+ _parseIdentificationParams.cold.33
+ _parseIdentificationParams.cold.34
+ _parseIdentificationParams.cold.35
+ _parseIdentificationParams.cold.36
+ _parseIdentificationParams.cold.37
+ _parseIdentificationParams.cold.7
+ _parseIdentificationParams.cold.8
+ _parseIdentificationParams.cold.9
+ acc_endpoint_processIncomingData.cold.13
+ acc_manager_checkForWirelessCTA.cold.6
+ acc_platform_packetLogging_logEventVA.cold.1
+ acc_platform_packetLogging_logEventVA.cold.2
+ acc_platform_packetLogging_logEventVA.cold.3
+ acc_platform_packetLogging_logEventVA.cold.4
+ acc_platform_packetLogging_logEventVA.cold.5
+ acc_platform_packetLogging_logEventVA.cold.6
+ acc_protocolRouter_setSecureTunnelDataTypeHandler.cold.1
+ acc_protocolRouter_setSecureTunnelDataTypeHandler.cold.2
+ acc_protocolRouter_setSecureTunnelDataTypeHandler.cold.3
+ iap2_CarPlayStartSession.cold.13
+ iap2_CarPlayStartSession.cold.14
+ iap2_CarPlayStartSession.cold.15
+ iap2_CarPlayStartSession.cold.16
+ mfi4Auth_endpoint_setEndpointSecureTunnelDataReceiveTypeHandler.cold.1
+ mfi4Auth_endpoint_setEndpointSecureTunnelDataReceiveTypeHandler.cold.2
+ mfi4Auth_protocol_handleAuthSessionClose.cold.7
+ mfi4Auth_protocol_handle_AuthState.cold.3
+ mfi4Auth_protocol_handle_AuthState.cold.4
+ mfi4Auth_protocol_handle_AuthenticationReset.cold.4
+ mfi4Auth_protocol_initIdentityCerts.cold.1
+ mfi4Auth_protocol_initIdentityCerts.cold.2
+ mfi4Auth_protocol_initIdentityCerts.cold.3
+ mfi4Auth_protocol_messageHandler_handleOutgoingSecureTunnelDataForClient.cold.10
+ mfi4Auth_protocol_messageHandler_handleOutgoingSecureTunnelDataForClient.cold.11
+ mfi4Auth_protocol_messageHandler_handleOutgoingSecureTunnelDataForClient.cold.9
+ mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler.cold.1
+ mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler.cold.2
+ mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler.cold.3
+ mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler.cold.4
+ mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler.cold.5
+ mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveTypeHandler.cold.6
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.1
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.10
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.11
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.12
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.13
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.14
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.15
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.16
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.17
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.18
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.19
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.2
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.20
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.21
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.3
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.4
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.5
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.6
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.7
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.8
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.9
+ mfi4Auth_protocol_processOutgoingSecureTunnelDataForClient.cold.11
+ mfi4Auth_protocol_processOutgoingSecureTunnelDataForClient.cold.12
+ mfi4Auth_protocol_processOutgoingSecureTunnelDataForClient.cold.13
+ mfi4Auth_protocol_processOutgoingSecureTunnelDataForClient.cold.14
+ mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler.cold.1
+ mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler.cold.2
+ mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler.cold.3
+ mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler.cold.4
+ mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler.cold.5
+ mfi4Auth_protocol_setSecureTunnelDataReceiveTypeHandler.cold.6
+ mfi4Auth_relay.c
+ mfi4Auth_relay_device.m
+ mfi4Auth_relay_handle_iAP2RelayFailed.cold.1
+ mfi4Auth_relay_handle_iAP2RelayFailed.cold.2
+ mfi4Auth_relay_handle_iAP2RelayFailed.cold.3
+ mfi4Auth_relay_handle_iAP2RelayFailed.cold.4
+ mfi4Auth_relay_handle_iAP2RelayFailed.cold.5
+ mfi4Auth_relay_handle_iAP2RelayFailed.cold.6
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.1
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.10
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.11
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.12
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.13
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.14
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.15
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.16
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.17
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.18
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.19
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.2
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.3
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.4
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.5
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.6
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.7
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.8
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.9
+ mfi4Auth_relay_handle_iAP2RelaySucceeded.cold.1
+ mfi4Auth_relay_handle_iAP2RelaySucceeded.cold.2
+ mfi4Auth_relay_handle_iAP2RelaySucceeded.cold.3
+ mfi4Auth_relay_handle_iAP2RelaySucceeded.cold.4
+ mfi4Auth_relay_handle_iAP2RelaySucceeded.cold.5
+ mfi4Auth_relay_handle_iAP2RelaySucceeded.cold.6
+ mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_TypeData.cold.1
+ mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_TypeData.cold.2
+ mfi4Auth_util_packIntoTunnelDataiAP2Msg.cold.1
+ mfi4Auth_util_packIntoTunnelDataiAP2Msg.cold.2
+ mfi4Auth_util_packIntoTunnelDataiAP2Msg.cold.3
+ mfi4Auth_util_packIntoTunnelDataiAP2Msg.cold.4
+ mfi4Auth_util_packIntoTunnelDataiAP2Msg.cold.5
+ mfi4Auth_util_packIntoTunnelDataiAP2Msg.cold.6
+ mfi4Auth_util_unpackFromTunnelDataiAP2Msg.cold.1
+ mfi4Auth_util_unpackFromTunnelDataiAP2Msg.cold.2
+ mfi4Auth_util_unpackFromTunnelDataiAP2Msg.cold.3
+ mfi4Auth_util_unpackFromTunnelDataiAP2Msg.cold.4
- /AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTCompress.o)
- /AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- _CFArrayApplierFunction_handleCertList.cold.17
- _CFArrayApplierFunction_handleSerialList.cold.13
- __115-[ACCExternalAccessoryServer handleIncomingExternalAccessoryData:forEASessionIdentifier:toExternalAccessoryClient:]_block_invoke.124
- __115-[ACCExternalAccessoryServer handleIncomingExternalAccessoryData:forEASessionIdentifier:toExternalAccessoryClient:]_block_invoke.124.cold.1
- __115-[ACCExternalAccessoryServer handleIncomingExternalAccessoryData:forEASessionIdentifier:toExternalAccessoryClient:]_block_invoke.124.cold.2
- __51-[ACCHIDServer listener:shouldAcceptNewConnection:]_block_invoke.70
- __51-[ACCHIDServer listener:shouldAcceptNewConnection:]_block_invoke.70.cold.1
- __51-[ACCHIDServer listener:shouldAcceptNewConnection:]_block_invoke.70.cold.2
- __52-[ACCExternalAccessoryServer externalAccessoryLeft:]_block_invoke.114
- __52-[ACCExternalAccessoryServer externalAccessoryLeft:]_block_invoke.114.cold.1
- __52-[ACCExternalAccessoryServer externalAccessoryLeft:]_block_invoke.114.cold.2
- __52-[ACCNowPlayingServer triggerMediaItemArtworkUpdate]_block_invoke.84
- __52-[ACCNowPlayingServer triggerMediaItemArtworkUpdate]_block_invoke.84.cold.1
- __53-[ACCAudioServer listener:shouldAcceptNewConnection:]_block_invoke.58
- __53-[ACCAudioServer listener:shouldAcceptNewConnection:]_block_invoke.58.cold.1
- __53-[ACCAudioServer listener:shouldAcceptNewConnection:]_block_invoke.58.cold.2
- __54-[ACCNowPlayingServer triggerPlaybackAttributesUpdate]_block_invoke.89
- __54-[ACCNowPlayingServer triggerPlaybackAttributesUpdate]_block_invoke.89.cold.1
- __55-[ACCExternalAccessoryServer externalAccessoryArrived:]_block_invoke.108
- __55-[ACCExternalAccessoryServer externalAccessoryArrived:]_block_invoke.108.cold.1
- __55-[ACCExternalAccessoryServer externalAccessoryArrived:]_block_invoke.108.cold.2
- __55-[ACCNowPlayingServer triggerMediaItemAttributesUpdate]_block_invoke.79
- __55-[ACCNowPlayingServer triggerMediaItemAttributesUpdate]_block_invoke.79.cold.1
- __57-[ACCTransportServer listener:shouldAcceptNewConnection:]_block_invoke.112
- __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.122
- __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.122.cold.1
- __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.122.cold.2
- __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.124
- __57-[ACCVoiceOverServer listener:shouldAcceptNewConnection:]_block_invoke.124.cold.1
- __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.163
- __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.167
- __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.167.cold.1
- __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.167.cold.2
- __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.169
- __58-[ACCBLEPairingServer listener:shouldAcceptNewConnection:]_block_invoke.169.cold.1
- __58-[ACCExternalAccessoryServer updateExternalAccessoryInfo:]_block_invoke.117
- __58-[ACCExternalAccessoryServer updateExternalAccessoryInfo:]_block_invoke.117.cold.1
- __58-[ACCExternalAccessoryServer updateExternalAccessoryInfo:]_block_invoke.117.cold.2
- __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.145
- __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.145.cold.1
- __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.145.cold.2
- __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.147
- __58-[ACCNavigationServer listener:shouldAcceptNewConnection:]_block_invoke.147.cold.1
- __58-[ACCNowPlayingServer listener:shouldAcceptNewConnection:]_block_invoke.72
- __58-[ACCNowPlayingServer listener:shouldAcceptNewConnection:]_block_invoke.72.cold.1
- __58-[ACCNowPlayingServer listener:shouldAcceptNewConnection:]_block_invoke.72.cold.2
- __60-[ACCCommunicationsServer invokeBlockOnClients:synchronous:]_block_invoke.85
- __60-[ACCCommunicationsServer invokeBlockOnClients:synchronous:]_block_invoke.85.cold.1
- __60-[ACCCommunicationsServer invokeBlockOnClients:synchronous:]_block_invoke.85.cold.2
- __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.171
- __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.171.cold.1
- __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.171.cold.2
- __60-[ACCMediaLibraryServer listener:shouldAcceptNewConnection:]_block_invoke.173
- __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.128
- __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.128.cold.1
- __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.128.cold.2
- __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.130
- __60-[ACCOOBBTPairingServer listener:shouldAcceptNewConnection:]_block_invoke.130.cold.1
- __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.111
- __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.111.cold.1
- __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.111.cold.2
- __62-[ACCAssistiveTouchServer listener:shouldAcceptNewConnection:]_block_invoke.113
- __62-[ACCCommunicationsServer listener:shouldAcceptNewConnection:]_block_invoke.81
- __62-[ACCCommunicationsServer listener:shouldAcceptNewConnection:]_block_invoke.81.cold.1
- __62-[ACCCommunicationsServer listener:shouldAcceptNewConnection:]_block_invoke.81.cold.2
- __62-[ACCConnectionInfoServer listener:shouldAcceptNewConnection:]_block_invoke.189
- __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.104
- __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.104.cold.1
- __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.104.cold.2
- __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.104.cold.3
- __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.104.cold.4
- __65-[ACCExternalAccessoryServer listener:shouldAcceptNewConnection:]_block_invoke.105
- __65-[ACCExternalAccessoryServer notifyClientOfConnectedAccessories:]_block_invoke.129
- __65-[ACCExternalAccessoryServer notifyClientOfConnectedAccessories:]_block_invoke.129.cold.1
- __65-[ACCExternalAccessoryServer notifyClientOfConnectedAccessories:]_block_invoke.129.cold.2
- __67-[ACCExternalAccessoryServer notifyClientOfConnectedVehicleStatus:]_block_invoke.134
- __67-[ACCExternalAccessoryServer notifyClientOfConnectedVehicleStatus:]_block_invoke.134.cold.1
- __67-[ACCExternalAccessoryServer notifyClientOfConnectedVehicleStatus:]_block_invoke.134.cold.2
- __79-[ACCExternalAccessoryServer sendNMEASentence:forAccessoryUUID:withTimestamps:]_block_invoke.126
- __79-[ACCExternalAccessoryServer sendNMEASentence:forAccessoryUUID:withTimestamps:]_block_invoke.126.cold.1
- __79-[ACCExternalAccessoryServer sendNMEASentence:forAccessoryUUID:withTimestamps:]_block_invoke.126.cold.2
- __83-[ACCTransportServer sendOutgoingData:forEndpointWithUUID:connectionUUID:toClient:]_block_invoke.116
- __83-[ACCTransportServer sendOutgoingData:forEndpointWithUUID:connectionUUID:toClient:]_block_invoke.116.cold.1
- __83-[ACCTransportServer sendOutgoingData:forEndpointWithUUID:connectionUUID:toClient:]_block_invoke.116.cold.2
- ___block_descriptor_32_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16l
- ___block_descriptor_40_e8_32r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- ___block_descriptor_40_e8_32s_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8
- ___block_descriptor_48_e8_32r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- ___block_descriptor_48_e8_32s40r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_49_e8_32s40r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40r48r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e183_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r56l8s40l8s48l8
- ___presentShareWiFiCredentialsNotification_block_invoke.102
- __block_descriptor_tmp.15
- __block_literal_global.113
- __block_literal_global.116
- __block_literal_global.119
- __block_literal_global.121
- __block_literal_global.131
- __block_literal_global.133
- __block_literal_global.136
- __block_literal_global.138
- __block_literal_global.148
- __block_literal_global.150
- __block_literal_global.194
- __block_literal_global.196
- __block_literal_global.198
- __block_literal_global.200
- __block_literal_global.202
- __block_literal_global.204
- __block_literal_global.206
- __block_literal_global.208
- __block_literal_global.210
- __block_literal_global.215
- __block_literal_global.59
- __block_literal_global.63
- __block_literal_global.67
- __block_literal_global.71
- __block_literal_global.76
- __block_literal_global.81
- __block_literal_global.83
- __block_literal_global.86
- __block_literal_global.90
- __block_literal_global.93
- __block_literal_global.95
- __block_literal_global.97
- __main_block_invoke.55
- __main_block_invoke.61
- __main_block_invoke.61.cold.1
- __main_block_invoke.65
- __main_block_invoke.65.cold.1
- __main_block_invoke.69
- __main_block_invoke.69.cold.1
- __mfi4Auth_endpoint_sessionOpened
- __setProtocol
- _acc_endpoint_setEndpointSecureTunnelDataReceiveHandler
- _acc_protocolRouter_routeSecureTunnelDataHandler
- _audioProductCerts_endpoint_handleAuthCertList.cold.10
- _audioProductCerts_endpoint_handleAuthCertList.cold.11
- _audioProductCerts_endpoint_handleAuthCertList.cold.12
- _audioProductCerts_endpoint_handleAuthCertList.cold.13
- _audioProductCerts_endpoint_handleAuthCertList.cold.5
- _audioProductCerts_endpoint_handleAuthCertList.cold.6
- _audioProductCerts_endpoint_handleAuthCertList.cold.7
- _audioProductCerts_endpoint_handleAuthCertList.cold.8
- _audioProductCerts_endpoint_handleAuthCertList.cold.9
- _audioProductCerts_endpoint_handleAuthResponseList.cold.10
- _audioProductCerts_endpoint_handleAuthResponseList.cold.11
- _audioProductCerts_endpoint_handleAuthResponseList.cold.12
- _audioProductCerts_endpoint_handleAuthResponseList.cold.13
- _audioProductCerts_endpoint_handleAuthResponseList.cold.14
- _audioProductCerts_endpoint_handleAuthResponseList.cold.15
- _audioProductCerts_endpoint_handleAuthResponseList.cold.16
- _audioProductCerts_endpoint_handleAuthResponseList.cold.17
- _audioProductCerts_endpoint_handleAuthResponseList.cold.18
- _audioProductCerts_endpoint_handleAuthResponseList.cold.19
- _audioProductCerts_endpoint_handleAuthResponseList.cold.5
- _audioProductCerts_endpoint_handleAuthResponseList.cold.6
- _audioProductCerts_endpoint_handleAuthResponseList.cold.7
- _audioProductCerts_endpoint_handleAuthResponseList.cold.8
- _audioProductCerts_endpoint_handleAuthResponseList.cold.9
- _ccec_add_ws
- _mfi4Auth_endpoint_sessionOpened.cold.1
- _mfi4Auth_endpoint_setEndpointSecureTunnelDataReceiveHandler
- _mfi4Auth_protocol_handle_iAP2RelayFailed
- _mfi4Auth_protocol_handle_iAP2RelayRemote
- _mfi4Auth_protocol_handle_iAP2RelaySucceeded
- _mfi4Auth_protocol_initMessage_RequestiAP2RelayRead
- _mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler
- _mfi4Auth_protocol_setSecureTunnelDataReceiveHandler
- _mfi4Auth_util_packIntoiAP2Msg
- _mfi4Auth_util_unpackFromiAP2Msg
- _setProtocol.cold.1
- acc_accInfo_setAccessoryInfo.cold.2
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.10
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.11
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.12
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.13
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.5
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.6
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.7
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.8
- acc_endpoint_processOutgoingSecureTunnelDataForClient.cold.9
- acc_platform_packetLogging_logEvent.cold.1
- acc_platform_packetLogging_logEvent.cold.2
- acc_platform_packetLogging_logEvent.cold.3
- acc_platform_packetLogging_logEvent.cold.4
- acc_protocolRouter_routeSecureTunnelDataHandler.cold.1
- acc_protocolRouter_routeSecureTunnelDataHandler.cold.2
- acc_protocolRouter_routeSecureTunnelDataHandler.cold.3
- mfi4Auth_endpoint_setEndpointSecureTunnelDataReceiveHandler.cold.1
- mfi4Auth_endpoint_setEndpointSecureTunnelDataReceiveHandler.cold.2
- mfi4Auth_protocol_handle_iAP2RelayFailed.cold.1
- mfi4Auth_protocol_handle_iAP2RelayFailed.cold.2
- mfi4Auth_protocol_handle_iAP2RelayFailed.cold.3
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.1
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.2
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.3
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.4
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.5
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.6
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.7
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.8
- mfi4Auth_protocol_handle_iAP2RelayRemote.cold.9
- mfi4Auth_protocol_handle_iAP2RelaySucceeded.cold.1
- mfi4Auth_protocol_handle_iAP2RelaySucceeded.cold.2
- mfi4Auth_protocol_handle_iAP2RelaySucceeded.cold.3
- mfi4Auth_protocol_initMessage_RequestiAP2RelayRead.cold.1
- mfi4Auth_protocol_initMessage_RequestiAP2RelayRead.cold.2
- mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler.cold.1
- mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler.cold.2
- mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler.cold.3
- mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler.cold.4
- mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler.cold.5
- mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler.cold.6
- mfi4Auth_protocol_processIncomingMessageExtra.cold.10
- mfi4Auth_protocol_processIncomingMessageExtra.cold.11
- mfi4Auth_protocol_setSecureTunnelDataReceiveHandler.cold.1
- mfi4Auth_protocol_setSecureTunnelDataReceiveHandler.cold.2
- mfi4Auth_protocol_setSecureTunnelDataReceiveHandler.cold.3
- mfi4Auth_util_packIntoiAP2Msg.cold.1
- mfi4Auth_util_packIntoiAP2Msg.cold.2
- mfi4Auth_util_packIntoiAP2Msg.cold.3
- mfi4Auth_util_packIntoiAP2Msg.cold.4
- mfi4Auth_util_packIntoiAP2Msg.cold.5
- mfi4Auth_util_packIntoiAP2Msg.cold.6
- mfi4Auth_util_unpackFromiAP2Msg.cold.1
- mfi4Auth_util_unpackFromiAP2Msg.cold.2
- mfi4Auth_util_unpackFromiAP2Msg.cold.3
CStrings:
+ "%02x:%02x:%02x:%02x:%02x:%02x"
+ "%s: %@, No pending auth certificates"
+ "%s: %@, Unable to generate auth challenge! %@ : %@"
+ "%s: %d"
+ "%s: Cert info contained no type"
+ "%s: Challenge validation failed"
+ "%s: Given key not string"
+ "%s: Given value not array"
+ "%s: Missing ACCEndpoint_t"
+ "%s: Missing connection"
+ "%s: Missing key"
+ "%s: Missing protocol endpoint"
+ "%s: Missing value"
+ "%s: No auth responses!"
+ "%s: No cert info found"
+ "%s: allowSigmaI %d, allowOneWay %d, (endpointSupportsMutualAuth %d, mfi4SigmaIRequired %d, mfi4ECDSAOnly %d, mfi4ECDSADisallow %d)"
+ "%s: authSession(%d), keepOpen %d"
+ "%s: authSession(%d), secureTunnelType %d, dataOut %@"
+ "%s: deviceIdentityCertsExist %d, trigger re-init for next time."
+ "%s: endpointUUID %@, EndpointSupportsMutualAuth %d, (bOneWayOnly %d, deviceIdentityCertsExist %d)"
+ "%s: endpointUUID %@, endpointSupportsMutualAuth %d"
+ "%s: initIdentityCerts ... "
+ "%s: initIdentityCerts ... errNo %d"
+ "%s: pairingDataMatch %d, bdAddrMatch %d"
+ "%s: supportedAuthTypes [%d %d %d], supportedCapabilities [%d %d %d]"
+ "%s:%d identifier %@, isBdAddrFormat %d"
+ "%s:%d negotiatedVersion %d, force %d, commandID 0x%04x -> 0x%04x"
+ "<ACCAccessoryInfo_t: name: %@; manufacturer: %@; model: %@; serialNumber: %@; hardwareVersion: %@; firmwareVersionActive: %@; firmwareVersionPending: %@; ppid: %@, regionCode: %@; deviceUID: %@>; deviceCompatibility: %@; vid/pid: %@/%@, accessoryPlatformID: %@"
+ "ACCEndpoint == NULL"
+ "AuthState: Unknown authStatus! %d"
+ "AuthenticationReset: Ignored"
+ "B24@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}16"
+ "B24@?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16"
+ "B32@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}16@24"
+ "Check for WirelessCTA: Found donor %@, receiver %@, but data/info doesn't match or doesn't exist! donor %@ / %@, receiver %@ / %@"
+ "Couldn't find an endpoint to update accessory info with! Try mapAccessoryInfo"
+ "Endpoint destroyed during logging"
+ "IAPAppBTPairingAccPlatformID"
+ "IgnoreAuthReset"
+ "IncomingOOBPairingInfo/Data: messageID %d, pairingType %d, supports2way %d, supportedTypes[%d %d], dataIn %@"
+ "MFi30Leaf-Certificate"
+ "MFi40Leaf-Certificate"
+ "MFi40Leaf-Intermediate"
+ "MFi4Auth"
+ "MFi4Auth NFC session closed"
+ "MFi4Auth NFC session opened"
+ "MFi4Auth accessory authentication Failed!"
+ "MFi4Auth accessory authentication Passed!"
+ "MFi4Auth accessory authentication Timed Out!"
+ "MFi4ECDSADisallow"
+ "MFi4ECDSAOnly"
+ "MFi4SigmaIRequired"
+ "Missing required subparams in Param ID: %d for Msg ID: 0x%04X - ignoring message"
+ "NFC Session Closed"
+ "NFC Session Opened"
+ "PacketLoggingPlainTextOnly"
+ "Received unhandled message with ID: 0x%04x"
+ "SDKVersion"
+ "T@\"NSString\",?,R,C"
+ "Too many subparams SubparamID: %d in Param ID: %d for Msg ID: 0x%04X - ignoring message"
+ "Unrecognized asset group paramID:0x%04X"
+ "VehicleDigitalCarKeyInfo group: identifier: %@, manufacturer: %@, brand: %@, ppid: %@, supportedTechnologies: %@, provisioningTemplate: %@, pairingAvailable: %@, onlineActivated: %@, ownershipPresent: %@"
+ "[#Accessory Info] %s:%d Set accessory info: name: %@, manufacturer: %@, model: %@, serialNumber: %@, hardwareVersion: %@, firmwareVersionActive: %@, firmwareVersionPending: %@, ppid: %@ regionCode: %@, deviceUID: %@, deviceCompatibility: %@, vid/pid: %@/%@, accessoryPlatformID: %@"
+ "[#CarPlay] Received CarPlayAvailability for accessory UUID %@, wiredAvailable %@, usbIdentifier %@, wirelessAvailable %@, bluetoothIdentifier %@ themeAssetsAvailable %@"
+ "[#CarPlay] platform_CarPlay_startSession: usbIP %@, wifiIP %@, ssid %@, pass %@, securityType %@, channel %@, port %@, deviceID %@, pubKey %@, srcVer %@, sdkVer %@, assetID %@, assetVer %@, mutualAuth %@"
+ "_IsBdAddrFormatString"
+ "_audioProductCerts_endpoint_generateAuthChallenge"
+ "_audioProductCerts_endpoint_handleAuthResponseWithMissingCert"
+ "_audioProductCerts_endpoint_handleMissingCertList"
+ "_audioProductCerts_endpoint_handlePrimaryBudMismatch"
+ "_audioProductCerts_endpoint_validateChallenge"
+ "_mfi4Auth_endpoint_isEndpointSupportsMutualAuth"
+ "_mfi4Auth_endpoint_isEndpointSupportsMutualAuth_block_invoke"
+ "acc_manager_checkForWirelessCTA"
+ "clusterAssetIdentifer"
+ "clusterAssetVersion"
+ "could not create DigitalCarKeyInfo feature"
+ "findWirelessCTADonorCapableConnection: %@ type %{coreacc:ACCConnection_Type_t}d, isAuthenticated %d, ident: %@"
+ "findWirelessCTADonorCapableConnection: %@ type %{coreacc:ACCConnection_Type_t}d, isAuthenticated %d, isBdAddrFormatString %d, found oobPairingData %@ / identifier %@"
+ "iap2_CarPlayAvailability: %@, wiredAvailable %@, usbIdentifier %@, wirelessAvailable %@, bluetoothIdentifier %@, themeAssetsAvailable %@"
+ "iap2_CarPlayStartSession: call platform_CarPlay_startSession, usbIP %@, wifiIP %@, ssid %@, pass %@, securityType %@, channel %@, port %@, deviceID %@, pubKey %@, srcVer %@, sdkVer %@, assetID %@, assetVer %@, mutualAuth %@"
+ "initIdentityCerts: !authSession"
+ "initIdentityCerts: authSession shutting down"
+ "invalide secureTunnelType (%d)"
+ "main_block_invoke"
+ "mfi4Auth_endpoint_getPublicNvmKeyValues: [%d / %d] 0x%x"
+ "mfi4Auth_protocol_cleanupSessionCommon"
+ "mfi4Auth_protocol_handleAuthSessionClose"
+ "mfi4Auth_protocol_handle_iAP2RelayRemote: invalid unpacket message size(%zu) !!!"
+ "mfi4Auth_protocol_handle_iAP2RelayRemote: unable to unpack nested message!!!"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: Unknown UserMessage 0x%x"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: invalid packageDataType!!!"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: msgID 0x%04x, len %zu"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: no secureTunnelHandler for type %d !!!"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: type %d, data %@"
+ "mfi4Auth_util_packIntoTunnelDataiAP2Msg: invalid data passed in"
+ "mfi4Auth_util_packIntoTunnelDataiAP2Msg: unable to allocate outMsg buffer!"
+ "mfi4Auth_util_packIntoTunnelDataiAP2Msg: unable to allocate outMsg!"
+ "mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, length %d"
+ "mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, type %d, Already have unpackedMessage %ld bytes !!!, release and create new one"
+ "mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, type %d, unpackedMessage %ld bytes"
+ "missing auth session"
+ "missing data handler"
+ "not a kiAP2ParamIdentificationInfo_VehicleDigitalCarKeyInfo parameter passed in!"
+ "pGroup == NULL"
+ "pMsg == NULL"
+ "processIncomingMessageRelay: !authSession"
+ "processIncomingMessageRelay: !inMessage"
+ "processIncomingMessageRelay: !msgId"
+ "processIncomingMessageRelay: action %d"
+ "processIncomingMessageRelay: cmd:0x%x  rsp:0x%x"
+ "processIncomingMessageRelay: error"
+ "processIncomingMessageRelay: supportedSecureTunnelCapabilitiesMask 0x%llx, processed 0x%llx"
+ "processOutgoingSecureTunnelDataForClient: !authSession"
+ "processOutgoingSecureTunnelDataForClient: !dataOut"
+ "processOutgoingSecureTunnelDataForClient: authSession shuttingDown"
+ "processOutgoingSecureTunnelDataForClient: sessionID %x, type %d, dataOut %@"
+ "receiveIncomingData: outMessage:(%d)"
+ "sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:"
+ "supportedSecureTunnelCapabilitiesMask: 0x%llx -> 0x%llx"
+ "supportsMutualAuth"
+ "themeAssetsAvailable"
+ "v24@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}16"
+ "v32@0:8@16^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}24"
+ "v32@0:8^{?=^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFArray}^{__CFNumber}^{__CFNumber}^{__CFNumber}{_opaque_pthread_mutex_t=q[56c]}}16Q24"
+ "v44@0:8@\"NSData\"16@\"NSString\"24S32@?<v@?B>36"
+ "v44@0:8@16@24S32@?36"
+ "v64@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@\"NSString\"40@\"NSNumber\"48@\"NSString\"56"
+ "v64@0:8@16@24@32@40@48@56"
+ "wrong type (%d)"
- "%s: %@, No pending auth certificates, %@ : %@"
- "<ACCAccessoryInfo_t: name: %@; manufacturer: %@; model: %@; serialNumber: %@; hardwareVersion: %@; firmwareVersionActive: %@; firmwareVersionPending: %@; ppid: %@, regionCode: %@; deviceUID: %@>; deviceCompatibility: %@, vendorID: %@, productID: %@"
- "B24@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}16"
- "B24@?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}8^v16"
- "B32@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}16@24"
- "Check for WirelessCTA: Found donor %@, receiver %@, but data doesn't match or doesn't exist! donorData %@, receiverData %@"
- "Couldn't find an endpoint to uppate accessory info with! Try mapAccessoryInfo"
- "IncomingOOBPairingInfo: messageID %d, pairingType %d, supports2way %d, supportedTypes[%d %d], dataIn %@"
- "Received unhandled message with ID: %d"
- "RequestiAP2RelayRead: !outMessage"
- "RequestiAP2RelayRead: authSession shutting down"
- "[#Accessory Info] %s:%d Set accessory info: name: %@, manufacturer: %@, model: %@, serialNumber: %@, hardwareVersion: %@, firmwareVersionActive: %@, firmwareVersionPending: %@, ppid: %@ regionCode: %@, deviceUID: %@, deviceCompatibility: %@, vendorID: %@, productID: %@"
- "[#CarPlay] platform_CarPlay_startSession: usbIP %@, wifiIP %@, ssid %@, pass %@, securityType %@, channel %@, port %@, deviceID %@, pubKey %@, srcVer %@"
- "findWirelessCTADonorCapableConnection: %@ type %{coreacc:ACCConnection_Type_t}d, isAuthenticated %d"
- "findWirelessCTADonorCapableConnection: %@ type %{coreacc:ACCConnection_Type_t}d, isAuthenticated %d, found oobPairingData %@"
- "iap2_CarPlayAvailability: %@, wiredAvailable %@, usbIdentifier %@, wirelessAvailable %@, bluetoothIdentifier %@"
- "iap2_CarPlayStartSession: call platform_CarPlay_startSession, usbIP %@, wifiIP %@, ssid %@, pass %@, securityType %@, channel %@, port %@, deviceID %@, pubKey %@, srcVer %@"
- "mfi4Auth_endpoint_getPublicNvmKeyValues: 0x%x"
- "mfi4Auth_protocol_handle_iAP2RelayRemote: type %d, data %@"
- "mfi4Auth_protocol_handle_iAP2RelayRemote: unable to unpack nested message"
- "mfi4Auth_protocol_messageHandler_setEndpointSecureTunnelDataReceiveHandler"
- "mfi4Auth_util_packageIntoiAP2Msg: invalid data passed in"
- "mfi4Auth_util_packageIntoiAP2Msg: unable to allocate outMsg buffer!"
- "mfi4Auth_util_packageIntoiAP2Msg: unable to allocate outMsg!"
- "mfi4Auth_util_unpackFromiAP2Msg: message 0x%04X, length %d"
- "mfi4Auth_util_unpackFromiAP2Msg: message 0x%04X, type %d, unpackedMessage %ld bytes"
- "receiveIncomingData: outMessage:%p"
- "setSecureTunnelDataReceiveHandler: !authSession"
- "setSecureTunnelDataReceiveHandler: !dataHandler"
- "setSecureTunnelDataReceiveHandler: !dataOut"
- "setSecureTunnelDataReceiveHandler: authSession shuttingDown"
- "v24@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}16"
- "v32@0:8@16^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}BB{_opaque_pthread_mutex_t=q[56c]}}24"
- "v32@0:8^{?=^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFArray}^{__CFNumber}^{__CFNumber}{_opaque_pthread_mutex_t=q[56c]}}16Q24"
- "v44@0:8@\"NSData\"16@\"NSString\"24C32@?<v@?B>36"
- "v44@0:8@16@24C32@?36"

```
