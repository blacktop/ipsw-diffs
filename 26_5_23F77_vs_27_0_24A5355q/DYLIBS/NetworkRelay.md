## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-676.120.2.0.0
-  __TEXT.__text: 0x6d648
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x1aec
-  __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x8b0
-  __TEXT.__cstring: 0xe379
-  __TEXT.__oslogstring: 0x121e
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__objc_classname: 0x362
-  __TEXT.__objc_methname: 0x49c6
-  __TEXT.__objc_methtype: 0x797
-  __TEXT.__objc_stubs: 0x2b40
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0xe20
-  __DATA_CONST.__objc_classlist: 0x108
+890.0.0.0.7
+  __TEXT.__text: 0x77f2c
+  __TEXT.__objc_methlist: 0x1ea4
+  __TEXT.__const: 0x240
+  __TEXT.__gcc_except_tab: 0xb3c
+  __TEXT.__cstring: 0xfdb4
+  __TEXT.__oslogstring: 0x13a9
+  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xce0
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeb8
-  __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x778
-  __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__cfstring: 0x4be0
-  __AUTH_CONST.__objc_const: 0x4870
-  __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __DATA_CONST.__objc_selrefs: 0x1070
+  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_arraydata: 0x1f8
+  __DATA_CONST.__got: 0x270
+  __AUTH_CONST.__const: 0x630
+  __AUTH_CONST.__cfstring: 0x4f80
+  __AUTH_CONST.__objc_const: 0x5068
+  __AUTH_CONST.__objc_intobj: 0x2d0
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x4dc
-  __DATA.__data: 0x218
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x540
+  __DATA.__data: 0x208
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x278
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA.__bss: 0x260
+  __DATA_DIRTY.__objc_data: 0xb90
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9BAA26D1-6AC3-39A1-B4F2-80C88182DF61
-  Functions: 903
-  Symbols:   3281
-  CStrings:  3389
+  UUID: E53561FE-4102-38CE-B34F-76000BAE50BC
+  Functions: 1030
+  Symbols:   3651
+  CStrings:  2580
 
Symbols:
+ +[NRDeviceMeshParticipantInfo supportsSecureCoding]
+ +[NRDeviceOperationalProperties copyPropertiesForMeshDevice]
+ +[NRDeviceOperationalProperties copyPropertiesForVisionPairedCompanion]
+ +[NRDeviceOperationalProperties copyPropertiesForVisionPairedDevice]
+ +[NRMeshInfo supportsSecureCoding]
+ -[NRDeviceInfo meshParticipantInfo]
+ -[NRDeviceInfo setMeshParticipantInfo:]
+ -[NRDeviceManager registerMesh:operationalProperties:queue:completionBlock:]
+ -[NRDeviceManager unregisterMesh:]
+ -[NRDeviceManager(Internal) setRouterConfidence:queue:completionBlock:]
+ -[NRDeviceManager(Internal) setWiFiScore:queue:completionBlock:]
+ -[NRDeviceMeshParticipantInfo .cxx_destruct]
+ -[NRDeviceMeshParticipantInfo applicationIdentifier]
+ -[NRDeviceMeshParticipantInfo copyWithZone:]
+ -[NRDeviceMeshParticipantInfo description]
+ -[NRDeviceMeshParticipantInfo encodeWithCoder:]
+ -[NRDeviceMeshParticipantInfo initWithCoder:]
+ -[NRDeviceMeshParticipantInfo isPrimaryAssistCapable]
+ -[NRDeviceMeshParticipantInfo isSelectedAsPrimaryAssist]
+ -[NRDeviceMeshParticipantInfo setApplicationIdentifier:]
+ -[NRDeviceMeshParticipantInfo setIsPrimaryAssistCapable:]
+ -[NRDeviceMeshParticipantInfo setIsSelectedAsPrimaryAssist:]
+ -[NRDeviceOperationalProperties applicationIdentifier]
+ -[NRDeviceOperationalProperties isMesh]
+ -[NRDeviceOperationalProperties meshEnableBabelOverP2PWiFi]
+ -[NRDeviceOperationalProperties setApplicationIdentifier:]
+ -[NRDeviceOperationalProperties setIsMesh:]
+ -[NRDeviceOperationalProperties setMeshEnableBabelOverP2PWiFi:]
+ -[NRDeviceOperationalProperties setUseRPKForASQUIC:]
+ -[NRDeviceOperationalProperties setUsesMultiplexedASForNWSC:]
+ -[NRDeviceOperationalProperties useRPKForASQUIC]
+ -[NRDeviceOperationalProperties usesLPN]
+ -[NRDeviceOperationalProperties usesMultiplexedASForNWSC]
+ -[NRDeviceOperationalProperties usesULPN]
+ -[NRDevicePairingManager authRequestWithCandidateHandler]
+ -[NRDevicePairingManager cancelAdvertising]
+ -[NRDevicePairingManager setAuthRequestWithCandidateHandler:]
+ -[NRDevicePairingManager startAdvertisingWithCompletion:]
+ -[NRDevicePairingManagerMux startAdvertisingForPairingManager:withCompletion:]
+ -[NRDevicePairingManagerMux stopAdvertisingForPairingManager:withCompletion:]
+ -[NRMeshIdentifier .cxx_destruct]
+ -[NRMeshIdentifier identifier]
+ -[NRMeshIdentifier initWithIdentifier:]
+ -[NRMeshInfo .cxx_destruct]
+ -[NRMeshInfo copyWithZone:]
+ -[NRMeshInfo description]
+ -[NRMeshInfo devices]
+ -[NRMeshInfo encodeWithCoder:]
+ -[NRMeshInfo initWithCoder:]
+ -[NRMeshInfo interfaceIndex]
+ -[NRMeshInfo interfaceName]
+ -[NRMeshInfo isEqual:]
+ -[NRMeshInfo isRegistered]
+ -[NRMeshInfo primaryAssistFeatureEnabled]
+ -[NRMeshInfo roomDistributorFeatureEnabled]
+ -[NRMeshInfo setDevices:]
+ -[NRMeshInfo setInterfaceIndex:]
+ -[NRMeshInfo setInterfaceName:]
+ -[NRMeshInfo setIsRegistered:]
+ -[NRMeshInfo setPrimaryAssistFeatureEnabled:]
+ -[NRMeshInfo setRoomDistributorFeatureEnabled:]
+ -[NRMeshMonitor .cxx_destruct]
+ -[NRMeshMonitor activateWithCompletionBlock:]
+ -[NRMeshMonitor cancel]
+ -[NRMeshMonitor checkMeshStatusWithRetryCount:]
+ -[NRMeshMonitor dealloc]
+ -[NRMeshMonitor initWithIdentifier:delegate:queue:]
+ -[NRMeshMonitor meshIdentifier]
+ -[NRMeshMonitor meshInfo]
+ -[NRMeshMonitor updateMeshStateFromResponse:]
+ -[NRMeshPreferences .cxx_destruct]
+ -[NRMeshPreferences addPeers:]
+ -[NRMeshPreferences cancelConnectionLocked]
+ -[NRMeshPreferences cancel]
+ -[NRMeshPreferences dealloc]
+ -[NRMeshPreferences description]
+ -[NRMeshPreferences initWithMulticastAddress:]
+ -[NRMeshPreferences removePeers:]
+ -[NRMeshPreferences restartConnectionLocked]
+ -[NRMeshPreferences sendMeshPreferencesLocked]
+ GCC_except_table123
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table272
+ GCC_except_table327
+ GCC_except_table352
+ GCC_except_table443
+ GCC_except_table454
+ GCC_except_table690
+ GCC_except_table698
+ GCC_except_table70
+ GCC_except_table703
+ GCC_except_table707
+ GCC_except_table711
+ GCC_except_table721
+ GCC_except_table725
+ GCC_except_table752
+ GCC_except_table755
+ GCC_except_table759
+ GCC_except_table764
+ GCC_except_table766
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table772
+ GCC_except_table775
+ GCC_except_table777
+ GCC_except_table81
+ GCC_except_table828
+ GCC_except_table830
+ GCC_except_table845
+ _NRIsValidMulticastGroupAddress
+ _NRLaunchClientForApplicationService
+ _NRPacketFindIPNextHeader
+ _NRPacketGetMulticastDestinationGroup
+ _NRPacketIsMLDv2
+ _NRPacketProcessMLDReport
+ _OBJC_CLASS_$_NRDeviceMeshParticipantInfo
+ _OBJC_CLASS_$_NRMeshIdentifier
+ _OBJC_CLASS_$_NRMeshInfo
+ _OBJC_CLASS_$_NRMeshMonitor
+ _OBJC_CLASS_$_NRMeshPreferences
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_NRDeviceInfo._meshParticipantInfo
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._applicationIdentifier
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._isPrimaryAssistCapable
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._isSelectedAsPrimaryAssist
+ _OBJC_IVAR_$_NRDeviceOperationalProperties._applicationIdentifier
+ _OBJC_IVAR_$_NRDeviceOperationalProperties._meshEnableBabelOverP2PWiFi
+ _OBJC_IVAR_$_NRDevicePairingManager._authRequestWithCandidateHandler
+ _OBJC_IVAR_$_NRMeshIdentifier._identifier
+ _OBJC_IVAR_$_NRMeshInfo._devices
+ _OBJC_IVAR_$_NRMeshInfo._interfaceIndex
+ _OBJC_IVAR_$_NRMeshInfo._interfaceName
+ _OBJC_IVAR_$_NRMeshInfo._isRegistered
+ _OBJC_IVAR_$_NRMeshInfo._primaryAssistFeatureEnabled
+ _OBJC_IVAR_$_NRMeshInfo._roomDistributorFeatureEnabled
+ _OBJC_IVAR_$_NRMeshMonitor._connection
+ _OBJC_IVAR_$_NRMeshMonitor._delegate
+ _OBJC_IVAR_$_NRMeshMonitor._delegateQueue
+ _OBJC_IVAR_$_NRMeshMonitor._didIssueFirstUpdate
+ _OBJC_IVAR_$_NRMeshMonitor._internalMeshIdentifier
+ _OBJC_IVAR_$_NRMeshMonitor._internalMeshInfo
+ _OBJC_IVAR_$_NRMeshMonitor._lock
+ _OBJC_IVAR_$_NRMeshPreferences._connection
+ _OBJC_IVAR_$_NRMeshPreferences._lock
+ _OBJC_IVAR_$_NRMeshPreferences._multicastAddress
+ _OBJC_IVAR_$_NRMeshPreferences._peerSet
+ _OBJC_METACLASS_$_NRDeviceMeshParticipantInfo
+ _OBJC_METACLASS_$_NRMeshIdentifier
+ _OBJC_METACLASS_$_NRMeshInfo
+ _OBJC_METACLASS_$_NRMeshMonitor
+ _OBJC_METACLASS_$_NRMeshPreferences
+ __NRCopyDateAndTimeStringForDate
+ __NRCopyDateAndTimeStringForDate.onceToken
+ __OBJC_$_CLASS_METHODS_NRDeviceMeshParticipantInfo
+ __OBJC_$_CLASS_METHODS_NRMeshInfo
+ __OBJC_$_CLASS_PROP_LIST_NRDeviceMeshParticipantInfo
+ __OBJC_$_CLASS_PROP_LIST_NRMeshInfo
+ __OBJC_$_INSTANCE_METHODS_NRDeviceMeshParticipantInfo
+ __OBJC_$_INSTANCE_METHODS_NRMeshIdentifier
+ __OBJC_$_INSTANCE_METHODS_NRMeshInfo
+ __OBJC_$_INSTANCE_METHODS_NRMeshMonitor
+ __OBJC_$_INSTANCE_METHODS_NRMeshPreferences
+ __OBJC_$_INSTANCE_VARIABLES_NRDeviceMeshParticipantInfo
+ __OBJC_$_INSTANCE_VARIABLES_NRMeshIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_NRMeshInfo
+ __OBJC_$_INSTANCE_VARIABLES_NRMeshMonitor
+ __OBJC_$_INSTANCE_VARIABLES_NRMeshPreferences
+ __OBJC_$_PROP_LIST_NRDeviceMeshParticipantInfo
+ __OBJC_$_PROP_LIST_NRMeshIdentifier
+ __OBJC_$_PROP_LIST_NRMeshInfo
+ __OBJC_$_PROP_LIST_NRMeshMonitor
+ __OBJC_CLASS_PROTOCOLS_$_NRDeviceMeshParticipantInfo
+ __OBJC_CLASS_PROTOCOLS_$_NRMeshInfo
+ __OBJC_CLASS_RO_$_NRDeviceMeshParticipantInfo
+ __OBJC_CLASS_RO_$_NRMeshIdentifier
+ __OBJC_CLASS_RO_$_NRMeshInfo
+ __OBJC_CLASS_RO_$_NRMeshMonitor
+ __OBJC_CLASS_RO_$_NRMeshPreferences
+ __OBJC_METACLASS_RO_$_NRDeviceMeshParticipantInfo
+ __OBJC_METACLASS_RO_$_NRMeshIdentifier
+ __OBJC_METACLASS_RO_$_NRMeshInfo
+ __OBJC_METACLASS_RO_$_NRMeshMonitor
+ __OBJC_METACLASS_RO_$_NRMeshPreferences
+ ___22-[NRMeshMonitor start]_block_invoke
+ ___43-[NRDevicePairingManager cancelAdvertising]_block_invoke
+ ___43-[NRDevicePairingManager cancelAdvertising]_block_invoke_2
+ ___43-[NRDevicePairingManager cancelAdvertising]_block_invoke_3
+ ___45-[NRMeshMonitor activateWithCompletionBlock:]_block_invoke
+ ___45-[NRMeshMonitor activateWithCompletionBlock:]_block_invoke_2
+ ___45-[NRMeshMonitor activateWithCompletionBlock:]_block_invoke_3
+ ___45-[NRMeshMonitor updateMeshStateFromResponse:]_block_invoke
+ ___46-[NRMeshPreferences sendMeshPreferencesLocked]_block_invoke
+ ___46-[NRMeshPreferences sendMeshPreferencesLocked]_block_invoke_2
+ ___47-[NRMeshMonitor checkMeshStatusWithRetryCount:]_block_invoke
+ ___57-[NRDevicePairingManager startAdvertisingWithCompletion:]_block_invoke
+ ___57-[NRDevicePairingManager startAdvertisingWithCompletion:]_block_invoke_2
+ ___57-[NRDevicePairingManager startAdvertisingWithCompletion:]_block_invoke_3
+ ___62-[NRDevicePairingManager getDataForAuthMethod:withCompletion:]_block_invoke_5
+ ___64-[NRDeviceManager(Internal) setWiFiScore:queue:completionBlock:]_block_invoke
+ ___71-[NRDeviceManager(Internal) setRouterConfidence:queue:completionBlock:]_block_invoke
+ ___77-[NRDevicePairingManagerMux stopAdvertisingForPairingManager:withCompletion:]_block_invoke
+ ___78-[NRDevicePairingManagerMux startAdvertisingForPairingManager:withCompletion:]_block_invoke
+ ___81-[NRDevicePairingManager receivedRequestForAuthMethod:authData:requestingDevice:]_block_invoke
+ ___81-[NRDevicePairingManager receivedRequestForAuthMethod:authData:requestingDevice:]_block_invoke_2
+ ___Block_byref_object_copy_.1154
+ ___Block_byref_object_copy_.2017
+ ___Block_byref_object_copy_.3070
+ ___Block_byref_object_dispose_.1155
+ ___Block_byref_object_dispose_.2018
+ ___Block_byref_object_dispose_.3071
+ ___NRLaunchClientForApplicationService_block_invoke
+ ____NRCopyDateAndTimeStringForDate_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1066
+ ___block_literal_global.110
+ ___block_literal_global.1137
+ ___block_literal_global.1242
+ ___block_literal_global.1539
+ ___block_literal_global.1752
+ ___block_literal_global.1983
+ ___block_literal_global.2034
+ ___block_literal_global.2082
+ ___block_literal_global.2176
+ ___block_literal_global.2248
+ ___block_literal_global.235
+ ___block_literal_global.2351
+ ___block_literal_global.2377
+ ___block_literal_global.26
+ ___block_literal_global.3050
+ ___block_literal_global.3249
+ ___block_literal_global.354
+ ___block_literal_global.408
+ ___block_literal_global.42
+ ___block_literal_global.444
+ ___block_literal_global.454
+ ___block_literal_global.47
+ ___block_literal_global.485
+ ___block_literal_global.54
+ ___block_literal_global.558
+ ___block_literal_global.567
+ ___block_literal_global.572
+ ___block_literal_global.607
+ ___block_literal_global.62
+ ___block_literal_global.67.1149
+ ___block_literal_global.69
+ ___block_literal_global.695
+ ___block_literal_global.708
+ ___block_literal_global.72
+ ___block_literal_global.77
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___block_literal_global.839
+ ___block_literal_global.95
+ ___block_literal_global.963
+ ___nrCopyLogObj_block_invoke.1073
+ ___nrCopyLogObj_block_invoke.1146
+ ___nrCopyLogObj_block_invoke.12
+ ___nrCopyLogObj_block_invoke.1233
+ ___nrCopyLogObj_block_invoke.1543
+ ___nrCopyLogObj_block_invoke.159
+ ___nrCopyLogObj_block_invoke.1757
+ ___nrCopyLogObj_block_invoke.1931
+ ___nrCopyLogObj_block_invoke.2043
+ ___nrCopyLogObj_block_invoke.2088
+ ___nrCopyLogObj_block_invoke.2201
+ ___nrCopyLogObj_block_invoke.2252
+ ___nrCopyLogObj_block_invoke.2355
+ ___nrCopyLogObj_block_invoke.2388
+ ___nrCopyLogObj_block_invoke.243
+ ___nrCopyLogObj_block_invoke.3061
+ ___nrCopyLogObj_block_invoke.3230
+ ___nrCopyLogObj_block_invoke.358
+ ___nrCopyLogObj_block_invoke.419
+ ___nrCopyLogObj_block_invoke.489
+ ___nrCopyLogObj_block_invoke.591
+ ___nrCopyLogObj_block_invoke.712
+ ___nrCopyLogObj_block_invoke.77
+ ___nrCopyLogObj_block_invoke.847
+ ___nrCopyLogObj_block_invoke.967
+ _copyPacketDestinationIPAddress
+ _createIPv4AddrString
+ _createIPv4AddrStringFromData
+ _createStringFromNRDeviceType
+ _getNRLDMLinkType
+ _getNRLinkSubtype
+ _getNRLinkType
+ _isPacketValidIPv4
+ _nrCopyLogObj.1085
+ _nrCopyLogObj.113
+ _nrCopyLogObj.1156
+ _nrCopyLogObj.1226
+ _nrCopyLogObj.1533
+ _nrCopyLogObj.1740
+ _nrCopyLogObj.19
+ _nrCopyLogObj.1924
+ _nrCopyLogObj.2046
+ _nrCopyLogObj.2090
+ _nrCopyLogObj.2171
+ _nrCopyLogObj.2238
+ _nrCopyLogObj.2323
+ _nrCopyLogObj.245
+ _nrCopyLogObj.2642
+ _nrCopyLogObj.3052
+ _nrCopyLogObj.3223
+ _nrCopyLogObj.342
+ _nrCopyLogObj.416
+ _nrCopyLogObj.479
+ _nrCopyLogObj.585
+ _nrCopyLogObj.67
+ _nrCopyLogObj.704
+ _nrCopyLogObj.851
+ _nrCopyLogObj.958
+ _nrCopyLogObj.onceToken.1065
+ _nrCopyLogObj.onceToken.109
+ _nrCopyLogObj.onceToken.1136
+ _nrCopyLogObj.onceToken.1230
+ _nrCopyLogObj.onceToken.1538
+ _nrCopyLogObj.onceToken.1751
+ _nrCopyLogObj.onceToken.1927
+ _nrCopyLogObj.onceToken.2033
+ _nrCopyLogObj.onceToken.2081
+ _nrCopyLogObj.onceToken.2175
+ _nrCopyLogObj.onceToken.2247
+ _nrCopyLogObj.onceToken.234
+ _nrCopyLogObj.onceToken.2350
+ _nrCopyLogObj.onceToken.2376
+ _nrCopyLogObj.onceToken.3058
+ _nrCopyLogObj.onceToken.3227
+ _nrCopyLogObj.onceToken.353
+ _nrCopyLogObj.onceToken.413
+ _nrCopyLogObj.onceToken.484
+ _nrCopyLogObj.onceToken.588
+ _nrCopyLogObj.onceToken.707
+ _nrCopyLogObj.onceToken.74
+ _nrCopyLogObj.onceToken.8
+ _nrCopyLogObj.onceToken.838
+ _nrCopyLogObj.onceToken.962
+ _nrCopyLogObj.sNRLogObj.1067
+ _nrCopyLogObj.sNRLogObj.111
+ _nrCopyLogObj.sNRLogObj.1138
+ _nrCopyLogObj.sNRLogObj.1231
+ _nrCopyLogObj.sNRLogObj.1540
+ _nrCopyLogObj.sNRLogObj.1753
+ _nrCopyLogObj.sNRLogObj.1928
+ _nrCopyLogObj.sNRLogObj.2035
+ _nrCopyLogObj.sNRLogObj.2083
+ _nrCopyLogObj.sNRLogObj.2177
+ _nrCopyLogObj.sNRLogObj.2249
+ _nrCopyLogObj.sNRLogObj.2352
+ _nrCopyLogObj.sNRLogObj.236
+ _nrCopyLogObj.sNRLogObj.2378
+ _nrCopyLogObj.sNRLogObj.3059
+ _nrCopyLogObj.sNRLogObj.3228
+ _nrCopyLogObj.sNRLogObj.355
+ _nrCopyLogObj.sNRLogObj.414
+ _nrCopyLogObj.sNRLogObj.486
+ _nrCopyLogObj.sNRLogObj.589
+ _nrCopyLogObj.sNRLogObj.709
+ _nrCopyLogObj.sNRLogObj.75
+ _nrCopyLogObj.sNRLogObj.840
+ _nrCopyLogObj.sNRLogObj.9
+ _nrCopyLogObj.sNRLogObj.964
+ _nrXPCCompanionSetSkipAPLABOverrides
+ _nrXPCEntitlementMeshMonitor
+ _nrXPCEntitlementMeshMonitor_block_invoke.sNRXPCConnection
+ _nrXPCEntitlementMeshRead
+ _nrXPCEntitlementMeshWrite
+ _nrXPCKeyAppSvcName
+ _nrXPCKeyBabelRouteDumpLevel
+ _nrXPCKeyBabelRouterConfidence
+ _nrXPCKeyBabelWiFiScore
+ _nrXPCKeyMeshIdentifier
+ _nrXPCKeyMeshInfo
+ _nrXPCKeyMeshPreferencesMulticastAddress
+ _nrXPCKeyMeshPreferencesPeerList
+ _nrXPCKeyPersistentMesh
+ _nrXPCKeySkipAPLABOverrides
+ _nrXPCLaunchAppSvcClient
+ _nrXPCSetPersistentMesh
+ _nrXPCSetRouterConfidence
+ _nrXPCSetWiFiScore
+ _nrXPCWiFiAwareAutoPairWithNRUUID
+ _nw_parameters_set_custom_options
+ _nw_quic_stream_copy_shared_connection_options
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$applicationIdentifier
+ _objc_msgSend$authRequestWithCandidateHandler
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$devices
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$hostname
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$interfaceIndex
+ _objc_msgSend$interfaceName
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isMesh
+ _objc_msgSend$isPrimaryAssistCapable
+ _objc_msgSend$isSelectedAsPrimaryAssist
+ _objc_msgSend$meshInfoDidChange:meshMonitor:
+ _objc_msgSend$meshParticipantInfo
+ _objc_msgSend$primaryAssistFeatureEnabled
+ _objc_msgSend$roomDistributorFeatureEnabled
+ _objc_msgSend$setApplicationIdentifier:
+ _objc_msgSend$setDevices:
+ _objc_msgSend$setInterfaceIndex:
+ _objc_msgSend$setInterfaceName:
+ _objc_msgSend$setIsMesh:
+ _objc_msgSend$setIsPrimaryAssistCapable:
+ _objc_msgSend$setIsRegistered:
+ _objc_msgSend$setIsSelectedAsPrimaryAssist:
+ _objc_msgSend$setMeshParticipantInfo:
+ _objc_msgSend$setPrimaryAssistFeatureEnabled:
+ _objc_msgSend$setRoomDistributorFeatureEnabled:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
+ _xpc_data_create
- GCC_except_table117
- GCC_except_table130
- GCC_except_table132
- GCC_except_table270
- GCC_except_table325
- GCC_except_table350
- GCC_except_table427
- GCC_except_table438
- GCC_except_table657
- GCC_except_table662
- GCC_except_table669
- GCC_except_table67
- GCC_except_table676
- GCC_except_table680
- GCC_except_table684
- GCC_except_table688
- GCC_except_table710
- GCC_except_table713
- GCC_except_table722
- GCC_except_table724
- GCC_except_table726
- GCC_except_table731
- GCC_except_table78
- _OBJC_CLASS_$_NSCountedSet
- __NRAddEligibleNRUUIDForLogObject
- __NRRemoveEligibleNRUUIDForLogObject
- __NRUpdateNRUUIDsEligibleForLogObjects
- ___62-[NRDevicePairingManager getDataForAuthMethod:withCompletion:]_block_invoke
- ___64-[NRDevicePairingManager receivedRequestForAuthMethod:authData:]_block_invoke
- ___Block_byref_object_copy_.1176
- ___Block_byref_object_copy_.1983
- ___Block_byref_object_copy_.2689
- ___Block_byref_object_dispose_.1177
- ___Block_byref_object_dispose_.1984
- ___Block_byref_object_dispose_.2690
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.1004
- ___block_literal_global.1087
- ___block_literal_global.114
- ___block_literal_global.1161
- ___block_literal_global.1263
- ___block_literal_global.1569
- ___block_literal_global.1754
- ___block_literal_global.1961
- ___block_literal_global.2002
- ___block_literal_global.2022
- ___block_literal_global.242
- ___block_literal_global.2668
- ___block_literal_global.2849
- ___block_literal_global.29
- ___block_literal_global.360
- ___block_literal_global.415
- ___block_literal_global.445
- ___block_literal_global.452
- ___block_literal_global.48
- ___block_literal_global.491
- ___block_literal_global.498
- ___block_literal_global.519
- ___block_literal_global.523
- ___block_literal_global.528
- ___block_literal_global.55
- ___block_literal_global.64
- ___block_literal_global.65
- ___block_literal_global.68
- ___block_literal_global.688
- ___block_literal_global.701
- ___block_literal_global.78
- ___block_literal_global.84
- ___block_literal_global.842
- ___block_literal_global.92
- ___block_literal_global.97
- ___block_literal_global.99
- ___nrCopyLogObj_block_invoke.1008
- ___nrCopyLogObj_block_invoke.1094
- ___nrCopyLogObj_block_invoke.11
- ___nrCopyLogObj_block_invoke.1169
- ___nrCopyLogObj_block_invoke.1255
- ___nrCopyLogObj_block_invoke.1573
- ___nrCopyLogObj_block_invoke.166
- ___nrCopyLogObj_block_invoke.1759
- ___nrCopyLogObj_block_invoke.1917
- ___nrCopyLogObj_block_invoke.2011
- ___nrCopyLogObj_block_invoke.2033
- ___nrCopyLogObj_block_invoke.250
- ___nrCopyLogObj_block_invoke.2679
- ___nrCopyLogObj_block_invoke.2829
- ___nrCopyLogObj_block_invoke.364
- ___nrCopyLogObj_block_invoke.420
- ___nrCopyLogObj_block_invoke.495
- ___nrCopyLogObj_block_invoke.589
- ___nrCopyLogObj_block_invoke.705
- ___nrCopyLogObj_block_invoke.78
- ___nrCopyLogObj_block_invoke.850
- _createStringFromNRDeviceEndpointType
- _nrCopyLogObj.1107
- _nrCopyLogObj.117
- _nrCopyLogObj.1178
- _nrCopyLogObj.1248
- _nrCopyLogObj.1564
- _nrCopyLogObj.1742
- _nrCopyLogObj.1908
- _nrCopyLogObj.2014
- _nrCopyLogObj.22
- _nrCopyLogObj.2233
- _nrCopyLogObj.252
- _nrCopyLogObj.2670
- _nrCopyLogObj.2822
- _nrCopyLogObj.350
- _nrCopyLogObj.425
- _nrCopyLogObj.485
- _nrCopyLogObj.583
- _nrCopyLogObj.68
- _nrCopyLogObj.697
- _nrCopyLogObj.855
- _nrCopyLogObj.998
- _nrCopyLogObj.onceToken.1003
- _nrCopyLogObj.onceToken.1086
- _nrCopyLogObj.onceToken.113
- _nrCopyLogObj.onceToken.1160
- _nrCopyLogObj.onceToken.1252
- _nrCopyLogObj.onceToken.1568
- _nrCopyLogObj.onceToken.1753
- _nrCopyLogObj.onceToken.1912
- _nrCopyLogObj.onceToken.2001
- _nrCopyLogObj.onceToken.2021
- _nrCopyLogObj.onceToken.241
- _nrCopyLogObj.onceToken.2676
- _nrCopyLogObj.onceToken.2826
- _nrCopyLogObj.onceToken.359
- _nrCopyLogObj.onceToken.417
- _nrCopyLogObj.onceToken.490
- _nrCopyLogObj.onceToken.586
- _nrCopyLogObj.onceToken.7
- _nrCopyLogObj.onceToken.700
- _nrCopyLogObj.onceToken.75
- _nrCopyLogObj.onceToken.841
- _nrCopyLogObj.sNRLogObj.1005
- _nrCopyLogObj.sNRLogObj.1088
- _nrCopyLogObj.sNRLogObj.115
- _nrCopyLogObj.sNRLogObj.1162
- _nrCopyLogObj.sNRLogObj.1253
- _nrCopyLogObj.sNRLogObj.1570
- _nrCopyLogObj.sNRLogObj.1755
- _nrCopyLogObj.sNRLogObj.1913
- _nrCopyLogObj.sNRLogObj.2003
- _nrCopyLogObj.sNRLogObj.2023
- _nrCopyLogObj.sNRLogObj.243
- _nrCopyLogObj.sNRLogObj.2677
- _nrCopyLogObj.sNRLogObj.2827
- _nrCopyLogObj.sNRLogObj.361
- _nrCopyLogObj.sNRLogObj.418
- _nrCopyLogObj.sNRLogObj.492
- _nrCopyLogObj.sNRLogObj.587
- _nrCopyLogObj.sNRLogObj.702
- _nrCopyLogObj.sNRLogObj.76
- _nrCopyLogObj.sNRLogObj.8
- _nrCopyLogObj.sNRLogObj.843
- _nrXPCEntitlementIdentityProxy_block_invoke.sNRXPCConnection
- _nw_parameters_set_account_id
- _objc_msgSend$allKeys
- _objc_release_x12
- _sNRUUIDsEligibleForLogObject
- _xpc_data_get_bytes_ptr
- _xpc_data_get_length
CStrings:
+ "%F %T"
+ "%s called with null [devicesArray isKindOfClass:[NSArray class]]"
+ "%s called with null [obj isKindOfClass:[NRDeviceInfo class]]"
+ "%s called with null asName"
+ "%s%.30s:%-4d %@ added %lu peers, total %lu"
+ "%s%.30s:%-4d %@ cancelling connection"
+ "%s%.30s:%-4d %@ cancelling connection because multicastAddress list is empty"
+ "%s%.30s:%-4d %@ failed to send mesh preferences: %@"
+ "%s%.30s:%-4d %@ interrupted, resubmitting mesh preferences"
+ "%s%.30s:%-4d %@ removed %lu peers, %lu remaining"
+ "%s%.30s:%-4d %@ restarting connection"
+ "%s%.30s:%-4d %@ sending mesh preferences"
+ "%s%.30s:%-4d %@ sent mesh preferences"
+ "%s%.30s:%-4d %@: Starting pairing advertising failed: %@"
+ "%s%.30s:%-4d %@: State changed while starting pairing advertising"
+ "%s%.30s:%-4d %@: State changed while stopping pairing advertising"
+ "%s%.30s:%-4d %@: Stopping pairing advertising failed: %@"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL identifier"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL meshID"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL multicastAddress"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL operationalProperties"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL peers"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL routerConfidenceStr"
+ "%s%.30s:%-4d Already activated %@, issuing meshInfoDidChange"
+ "%s%.30s:%-4d Cancel: %@"
+ "%s%.30s:%-4d Canceling %@"
+ "%s%.30s:%-4d Failed to start %@"
+ "%s%.30s:%-4d Informing client that mesh info changed"
+ "%s%.30s:%-4d Mesh checkin could not deliver message %@, error %@, retrying"
+ "%s%.30s:%-4d Mesh checkin received XPC dict: %@"
+ "%s%.30s:%-4d Mesh checkin received unexpected XPC object: %@"
+ "%s%.30s:%-4d Mesh state changed, firstIssue %@, old mesh info %@, new mesh info %@"
+ "%s%.30s:%-4d No mesh delegate found"
+ "%s%.30s:%-4d Parsed MLD record: %s group %@"
+ "%s%.30s:%-4d Received auth method request from device: %@"
+ "%s%.30s:%-4d Received mesh XPC error: %@, retrying"
+ "%s%.30s:%-4d Received mesh status XPC dict: %@"
+ "%s%.30s:%-4d Received unexpected mesh XPC object: %@"
+ "%s%.30s:%-4d Registering mesh %@ with operational properties %@"
+ "%s%.30s:%-4d Requesting launch of client for application service: %@"
+ "%s%.30s:%-4d Sent advertising start message: %@"
+ "%s%.30s:%-4d Sent advertising stop message: %@"
+ "%s%.30s:%-4d Setting WiFi score to %lu Mbps"
+ "%s%.30s:%-4d Setting babel router confidence to %@"
+ "%s%.30s:%-4d Start advertising could not deliver message %@, error %@"
+ "%s%.30s:%-4d Start advertising received XPC dict: %@"
+ "%s%.30s:%-4d Start advertising received unexpected XPC object: %@"
+ "%s%.30s:%-4d Start advertising request with no XPC connection"
+ "%s%.30s:%-4d Started %@"
+ "%s%.30s:%-4d Stop advertising could not deliver message %@, error %@"
+ "%s%.30s:%-4d Stop advertising received XPC dict: %@"
+ "%s%.30s:%-4d Stop advertising received unexpected XPC object: %@"
+ "%s%.30s:%-4d Stop advertising request with no XPC connection"
+ "%s%.30s:%-4d Unregistering mesh %@"
+ "%s%.30s:%-4d launch requesting for application service completed: %@ (error %@)"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with NULL identifier"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with NULL meshID"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with NULL multicastAddress"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with NULL operationalProperties"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with NULL peers"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with NULL routerConfidenceStr"
+ "(none)"
+ "(null)"
+ ", appID:%@"
+ ", mesh"
+ "-[NRDeviceManager registerMesh:operationalProperties:queue:completionBlock:]"
+ "-[NRDeviceManager unregisterMesh:]"
+ "-[NRDeviceManager(Internal) setRouterConfidence:queue:completionBlock:]"
+ "-[NRDeviceManager(Internal) setWiFiScore:queue:completionBlock:]"
+ "-[NRDeviceMeshParticipantInfo initWithCoder:]"
+ "-[NRDevicePairingManager cancelAdvertising]_block_invoke_2"
+ "-[NRDevicePairingManager startAdvertisingWithCompletion:]"
+ "-[NRDevicePairingManager startAdvertisingWithCompletion:]_block_invoke_2"
+ "-[NRDevicePairingManagerMux startAdvertisingForPairingManager:withCompletion:]"
+ "-[NRDevicePairingManagerMux startAdvertisingForPairingManager:withCompletion:]_block_invoke"
+ "-[NRDevicePairingManagerMux stopAdvertisingForPairingManager:withCompletion:]"
+ "-[NRDevicePairingManagerMux stopAdvertisingForPairingManager:withCompletion:]_block_invoke"
+ "-[NRMeshIdentifier initWithIdentifier:]"
+ "-[NRMeshInfo initWithCoder:]"
+ "-[NRMeshMonitor activateWithCompletionBlock:]"
+ "-[NRMeshMonitor cancel]"
+ "-[NRMeshMonitor checkMeshStatusWithRetryCount:]_block_invoke"
+ "-[NRMeshMonitor dealloc]"
+ "-[NRMeshMonitor initWithIdentifier:delegate:queue:]"
+ "-[NRMeshMonitor start]_block_invoke"
+ "-[NRMeshMonitor updateMeshStateFromResponse:]"
+ "-[NRMeshMonitor updateMeshStateFromResponse:]_block_invoke"
+ "-[NRMeshPreferences addPeers:]"
+ "-[NRMeshPreferences cancelConnectionLocked]"
+ "-[NRMeshPreferences cancel]"
+ "-[NRMeshPreferences dealloc]"
+ "-[NRMeshPreferences initWithMulticastAddress:]"
+ "-[NRMeshPreferences removePeers:]"
+ "-[NRMeshPreferences restartConnectionLocked]"
+ "-[NRMeshPreferences sendMeshPreferencesLocked]"
+ "-[NRMeshPreferences sendMeshPreferencesLocked]_block_invoke"
+ "-[NRMeshPreferences sendMeshPreferencesLocked]_block_invoke_2"
+ "1\"!"
+ "<NRMeshInfo: %p> interfaceName: %@, interfaceIndex: %u, isRegistered: %@, devices: %lu, primaryAssistEnabled: %@, roomDistributorEnabled: %@"
+ "Advertising"
+ "AppSvcName"
+ "BabelRouteDumpLevel"
+ "BabelRouterConfidence"
+ "BabelWiFiScore"
+ "Cannot auto-pair with nil nrUUID"
+ "Could not check mesh status as no connection found"
+ "Failed to checkin NRMeshMonitor after retries"
+ "Failed to create NRMeshMonitor XPC connection"
+ "Failed to get requesting device candidate from message"
+ "Failed to set WiFi score"
+ "Failed to set router confidence"
+ "Failed to start mesh monitor"
+ "Joining"
+ "LaunchAppSvcClient"
+ "Leaving"
+ "Mesh checkin received unexpected XPC object"
+ "MeshIdentifier"
+ "MeshInfo"
+ "MeshMonitorStatus"
+ "MeshPreferences"
+ "MeshPreferencesMulticastAddress"
+ "MeshPreferencesPeerList"
+ "MeshPrefs[%@]"
+ "MeshPrefs[idle]"
+ "NRLaunchClientForApplicationService"
+ "NRLaunchClientForApplicationService_block_invoke"
+ "NRMeshMonitorErrorDomain"
+ "NRMeshParticipantInfo[appID=%@ primaryAssistCapable=%@ selectedAsPrimaryAssist=%@]"
+ "NRPacketProcessMLDReport"
+ "PersistentMesh"
+ "Received unexpected mesh XPC object"
+ "SetPersistentMesh"
+ "SetSkipAPLABOverrides"
+ "SkipAPLABOverrides"
+ "Start advertising received invalid result type"
+ "Start advertising received response without result code"
+ "Start advertising received unexpected XPC object"
+ "StartingAdvertising"
+ "Stop advertising received invalid result type"
+ "Stop advertising received response without result code"
+ "Stop advertising received unexpected XPC object"
+ "StoppingAdvertising"
+ "WiFiAwareAutoPairWithNRUUID"
+ "WiFiP2PLPNAN"
+ "applicationIdentifier"
+ "com.apple.networkrelay.mesh.read"
+ "com.apple.networkrelay.mesh.write"
+ "com.apple.networkrelay.meshMonitor"
+ "devices"
+ "interfaceIndex"
+ "interfaceName"
+ "isPacketValidIPv4"
+ "isPrimaryAssistCapable"
+ "isSelectedAsPrimaryAssist"
+ "lp-N"
+ "meshParticipantInfo"
+ "no"
+ "nrXPCCompanionSetSkipAPLABOverrides"
+ "nrXPCLaunchAppSvcClient"
+ "nrXPCSetPersistentMesh"
+ "nrXPCSetRouterConfidence"
+ "nrXPCSetWiFiScore"
+ "nrXPCWiFiAwareAutoPairWithNRUUID"
+ "nr_dispatch_queue_create_with_qos2"
+ "primaryAssistFeatureEnabled"
+ "roomDistributorFeatureEnabled"
+ "yes"
- "#16@0:8"
- "."
- ".cxx_destruct"
- "1\""
- "@\"<NRDeviceMonitorDelegate>\""
- "@\"CWFInterface\""
- "@\"NRBluetoothLinkPreferences\""
- "@\"NRCompanionLinkPreferences\""
- "@\"NRDeviceIdentifier\""
- "@\"NRDeviceInfo\""
- "@\"NRDeviceOperationalProperties\""
- "@\"NRDevicePairingCandidate\""
- "@\"NRDevicePairingCriteria\""
- "@\"NRDevicePairingManager\""
- "@\"NRDevicePairingManagerInfo\""
- "@\"NRDevicePairingManagerMux\""
- "@\"NRDevicePairingProperties\""
- "@\"NRDevicePairingTarget\""
- "@\"NRDevicePreferencesQuickRelay\""
- "@\"NRDeviceProxyInfo\""
- "@\"NRDeviceProxyProviderCriteria\""
- "@\"NRXPCComm\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_nw_parameters>\""
- "@\"NSObject<OS_nw_path>\""
- "@\"NSObject<OS_nw_path_evaluator>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NWAddressEndpoint\""
- "@\"SecKeyProxy\""
- "@16@0:8"
- "@20@0:8C16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8C16B20"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@28@0:8C16B20B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8@16@24C32"
- "@36@0:8@16C24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@44@0:8@16@24C32@36"
- "@48@0:8@16@24@32@40"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "C16@0:8"
- "C20@0:8C16"
- "Internal"
- "NENexusDelegate"
- "NRBluetoothLinkPreferences"
- "NRBluetoothPacketParser"
- "NRBluetoothPacketParserManager"
- "NRCompanionLinkPreferences"
- "NRDeviceIdentifier"
- "NRDeviceInfo"
- "NRDeviceManager"
- "NRDeviceMonitor"
- "NRDeviceOperationalProperties"
- "NRDevicePairingCandidate"
- "NRDevicePairingCriteria"
- "NRDevicePairingManager"
- "NRDevicePairingManagerInfo"
- "NRDevicePairingManagerMux"
- "NRDevicePairingManagerMuxEntry"
- "NRDevicePairingProperties"
- "NRDevicePairingTarget"
- "NRDevicePreferences"
- "NRDevicePreferencesQuickRelay"
- "NRDeviceProperties"
- "NRDeviceProxyInfo"
- "NRDeviceProxyProviderCriteria"
- "NRDeviceProxyProviderFlowMatchRule"
- "NREndpoint"
- "NRIdentityProxyClient"
- "NRLinkPreferences"
- "NRPairedDevice"
- "NRParameters"
- "NRParametersPhoneCallRelay"
- "NRParametersServiceConnection"
- "NRPreferWiFi"
- "NRXPCComm"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Received request for auth method with no auth data"
- "S"
- "S16@0:8"
- "T#,R"
- "T@\"NRBluetoothLinkPreferences\",&,N"
- "T@\"NRCompanionLinkPreferences\",&,N"
- "T@\"NRDeviceIdentifier\",&,N,V_deviceIdentifier"
- "T@\"NRDeviceIdentifier\",&,N,V_nrDeviceIdentifier"
- "T@\"NRDeviceIdentifier\",C,N,V_nrDeviceIdentifier"
- "T@\"NRDeviceIdentifier\",R,N"
- "T@\"NRDeviceIdentifier\",R,N,V_nrDeviceIdentifier"
- "T@\"NRDeviceInfo\",R,N"
- "T@\"NRDeviceOperationalProperties\",C,N,V_operationalProperties"
- "T@\"NRDevicePairingCandidate\",&,N,V_candidate"
- "T@\"NRDevicePairingCriteria\",&,N,V_pairingCriteria"
- "T@\"NRDevicePairingProperties\",C,N,V_properties"
- "T@\"NRDevicePairingTarget\",&,N,V_device"
- "T@\"NRDeviceProxyInfo\",&,N,V_proxyInfo"
- "T@\"NRDeviceProxyProviderCriteria\",&,N,V_proxyProviderCriteria"
- "T@\"NSArray\",&,N,V_allowedLinkSubtypes"
- "T@\"NSArray\",&,N,V_allowedLinkTypes"
- "T@\"NSArray\",&,N,V_httpConnectURLs"
- "T@\"NSArray\",&,N,V_nrDeviceIdentifiers"
- "T@\"NSArray\",&,N,V_proxyUsageRules"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_bluetoothMACAddress"
- "T@\"NSData\",&,N,V_httpConnectPSK"
- "T@\"NSData\",&,N,V_httpConnectPSKIdentity"
- "T@\"NSData\",&,N,V_identifier"
- "T@\"NSData\",&,N,V_metadata"
- "T@\"NSData\",&,N,V_outOfBandKey"
- "T@\"NSData\",C,N,V_authData"
- "T@\"NSData\",C,N,V_identifier"
- "T@\"NSData\",C,N,V_metadata"
- "T@\"NSDictionary\",&,N,V_entitlements"
- "T@\"NSDictionary\",&,N,V_peerEndpointDictionary"
- "T@\"NSNumber\",&,N,V_inputBytesPerSecond"
- "T@\"NSNumber\",&,N,V_outputBytesPerSecond"
- "T@\"NSNumber\",&,N,V_packetsPerSecond"
- "T@\"NSNumber\",&,N,V_rssi"
- "T@\"NSSet\",&,N"
- "T@\"NSString\",&,N,V_candidateService"
- "T@\"NSString\",&,N,V_connectedInterfaceName"
- "T@\"NSString\",&,N,V_domain"
- "T@\"NSString\",&,N,V_httpConnectPassword"
- "T@\"NSString\",&,N,V_httpConnectUserName"
- "T@\"NSString\",&,N,V_matchResultAccountID"
- "T@\"NSString\",&,N,V_matchResultBundleID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSUUID\",&,N,V_bluetoothUUID"
- "T@\"NSUUID\",&,N,V_serviceUUID"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSUUID\",C,N,V_cbUUID"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"NWAddressEndpoint\",&,N,V_localEndpoint"
- "T@\"NWAddressEndpoint\",&,N,V_remoteEndpoint"
- "T@?,C,N,V_authRequestHandler"
- "T@?,C,N,V_candidateDiscoveredHandler"
- "T@?,C,N,V_candidateLostHandler"
- "T@?,C,N,V_invalidationHandler"
- "TB,N"
- "TB,N,V_allowsDeadPeerDetection"
- "TB,N,V_allowsDeviceDiscovery"
- "TB,N,V_allowsDirectToCloud"
- "TB,N,V_allowsPermittedClientsOnly"
- "TB,N,V_controlOnly"
- "TB,N,V_datagramMode"
- "TB,N,V_direct"
- "TB,N,V_handlesLinkRecommendations"
- "TB,N,V_isAltAccountPairing"
- "TB,N,V_isExternalPairing"
- "TB,N,V_isNRDTestServer"
- "TB,N,V_isNotEncapsulated"
- "TB,N,V_isReachableOverWiFi"
- "TB,N,V_migrationPairing"
- "TB,N,V_pairWithSPPLink"
- "TB,N,V_providesPhoneCallRelaySupport"
- "TB,N,V_proxyProviderRequiresWiFi"
- "TB,N,V_reportedToABC"
- "TB,N,V_requiresReachability"
- "TB,N,V_uses6LoWPAN"
- "TB,N,V_usesTLS"
- "TB,N,V_wasInitiallySetupUsingIDSPairing"
- "TB,R"
- "TB,R,N"
- "TC,N,V_allowedPeerDeviceType"
- "TC,N,V_connectedLinkSubtype"
- "TC,N,V_connectedLinkType"
- "TC,N,V_pairingTransport"
- "TC,N,V_serviceClass"
- "TC,N,V_transportProtocol"
- "TC,R,N"
- "TC,R,N,V_linkType"
- "TQ,N,V_activeOperationalScope"
- "TQ,N,V_authMethod"
- "TQ,N,V_bluetoothEndpointType"
- "TQ,N,V_bluetoothRole"
- "TQ,N,V_deviceType"
- "TQ,N,V_flags"
- "TQ,N,V_managerState"
- "TQ,N,V_operationalScope"
- "TQ,N,V_pairingProtocolVersion"
- "TQ,N,V_proxyCapability"
- "TQ,N,V_proxyProviderAuthMode"
- "TQ,N,V_proxyProviderType"
- "TQ,N,V_startTime"
- "TQ,R"
- "TS,N,V_peerNetworkRelayVersion"
- "TS,N,V_psm"
- "TS,N,V_trafficClass"
- "TS,N,V_version"
- "Ti,R,N"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{?=^v^?^?^?^v}"
- "^{?=^v^?^?^?^v}36@0:8C16^?20^v28"
- "^{?=^v^?^?^v}"
- "^{?=^v^?^?^v}36@0:8C16^?20^v28"
- "^{_NSZone=}16@0:8"
- "^{__SCDynamicStore=}"
- "^{channel=}"
- "^{channel_ring_desc=}"
- "_activeOperationalScope"
- "_activePairingCandidates"
- "_activityMask"
- "_advancedWithoutRXSync"
- "_agentUUID"
- "_allowedLinkSubtypes"
- "_allowedLinkTypes"
- "_allowedPeerDeviceType"
- "_allowsDeadPeerDetection"
- "_allowsDeviceDiscovery"
- "_allowsDirectToCloud"
- "_allowsPermittedClientsOnly"
- "_assertCount"
- "_authData"
- "_authMethod"
- "_authRequestHandler"
- "_bluetoothEndpointType"
- "_bluetoothMACAddress"
- "_bluetoothRole"
- "_bluetoothUUID"
- "_bytesFromLink"
- "_bytesToLink"
- "_callbackQueue"
- "_cancelled"
- "_candidate"
- "_candidateDiscoveredHandler"
- "_candidateLostHandler"
- "_candidateService"
- "_cbUUID"
- "_certificateData"
- "_checkedIn"
- "_cmpnLnkPrefsEvaluator"
- "_connectedInterfaceName"
- "_connectedLinkSubtype"
- "_connectedLinkType"
- "_connection"
- "_controlOnly"
- "_coreWiFiHandle"
- "_counterForDataStallCheck"
- "_counterForDataStallRemediation"
- "_dNexusBEInputSource"
- "_dNexusBEOutputSource"
- "_dNexusBKInputSource"
- "_dNexusBKOutputSource"
- "_dNexusVIInputSource"
- "_dNexusVIOutputSource"
- "_dNexusVOInputSource"
- "_dNexusVOOutputSource"
- "_dataProtectionClass"
- "_datagramBytesFromLink"
- "_datagramBytesToLink"
- "_datagramMode"
- "_delegate"
- "_delegateQueue"
- "_device"
- "_deviceIdentifier"
- "_deviceType"
- "_didIssueFirstUpdate"
- "_direct"
- "_domain"
- "_entitlements"
- "_ephemeral"
- "_evaluator"
- "_excludedBundleIdentifiers"
- "_flags"
- "_forceWakePacketForTesting"
- "_handlesLinkRecommendations"
- "_hasCmpnLnkPrefsForBT"
- "_hasCmpnLnkPrefsForIsoch"
- "_hasCmpnLnkPrefsForThroughput"
- "_hasCmpnLnkPrefsForThroughputP2P"
- "_hasCmpnLnkPrefsForThroughputP2PImmediate"
- "_highThroughput"
- "_httpConnectPSK"
- "_httpConnectPSKIdentity"
- "_httpConnectPassword"
- "_httpConnectURLs"
- "_httpConnectUserName"
- "_identifier"
- "_includeP2P"
- "_inputBytesPerSecond"
- "_internalBluetoothLinkPreferences"
- "_internalCompanionLinkPreferences"
- "_internalDeviceIdentifier"
- "_internalDeviceInfo"
- "_internalDeviceSetupCompleted"
- "_internalDeviceSetupStarted"
- "_internalEphemeralBluetoothUUID"
- "_internalHasUnpairedBluetooth"
- "_internalIsAsleep"
- "_internalIsClassCConnected"
- "_internalIsCloudConnected"
- "_internalIsConnected"
- "_internalIsEnabled"
- "_internalIsNearby"
- "_internalIsRegistered"
- "_internalLinkSubtype"
- "_internalLinkType"
- "_internalManagerState"
- "_internalPluggedIn"
- "_internalPolicyTrafficClassifiers"
- "_internalProxySvcIntfName"
- "_internalThermalPressureLevel"
- "_internalUsesAPL"
- "_invalidationHandler"
- "_ipHeaderOffset"
- "_isAltAccountPairing"
- "_isCertificateReference"
- "_isExternalPairing"
- "_isIdentityReference"
- "_isNRDTestServer"
- "_isNotEncapsulated"
- "_isP2P"
- "_isReachableOverWiFi"
- "_keyProxy"
- "_lastPacketDataArrivalTime"
- "_lastReadBytesFromDatagramLink"
- "_lastReadBytesFromLink"
- "_lastReadBytesFromUrgentLink"
- "_lastReadBytesToDatagramLink"
- "_lastReadBytesToLink"
- "_lastReadBytesToUrgentLink"
- "_lastReadPacketsFromNexusBE"
- "_lastReadPacketsFromNexusBK"
- "_lastReadPacketsFromNexusVI"
- "_lastReadPacketsFromNexusVO"
- "_lastReadPacketsToNexusBE"
- "_lastReadPacketsToNexusBK"
- "_lastReadPacketsToNexusVI"
- "_lastReadPacketsToNexusVO"
- "_lastReadWriteActivityCounterForHigh"
- "_lastReadWriteActivityCounterForIsochronous"
- "_lastReadWriteActivityCounterForMedium"
- "_launchFlags"
- "_linkActivationMap"
- "_linkStatTimerSource"
- "_linkType"
- "_localAddrClassD"
- "_localEndpoint"
- "_lock"
- "_managerInfo"
- "_managerState"
- "_matchResultAccountID"
- "_matchResultBundleID"
- "_matchTokens"
- "_metadata"
- "_migrationPairing"
- "_muxEntries"
- "_needsReassert"
- "_newZeroingDataWithBytes:length:"
- "_nexusBEChannel"
- "_nexusBEChannelUsedSinceLastPurge"
- "_nexusBEGroup"
- "_nexusBEInputRing"
- "_nexusBEOutputRing"
- "_nexusBKChannel"
- "_nexusBKChannelUsedSinceLastPurge"
- "_nexusBKGroup"
- "_nexusBKInputRing"
- "_nexusBKOutputRing"
- "_nexusInstances"
- "_nexusSetupComplete"
- "_nexusVIChannel"
- "_nexusVIChannelUsedSinceLastPurge"
- "_nexusVIGroup"
- "_nexusVIInputRing"
- "_nexusVIOutputRing"
- "_nexusVOChannel"
- "_nexusVOChannelUsedSinceLastPurge"
- "_nexusVOGroup"
- "_nexusVOInputRing"
- "_nexusVOOutputRing"
- "_notificationBlock"
- "_notificationQueue"
- "_notifyToken"
- "_nrDeviceIdentifier"
- "_nrDeviceIdentifiers"
- "_nrUUID"
- "_operationQueue"
- "_operationalProperties"
- "_operationalScope"
- "_options"
- "_outOfBandKey"
- "_outputBytesPerSecond"
- "_p2pNeededImmediately"
- "_packetDataIntervalAverage"
- "_packetsFromNexusBE"
- "_packetsFromNexusBK"
- "_packetsFromNexusVI"
- "_packetsFromNexusVO"
- "_packetsPerSecond"
- "_packetsToNexusBE"
- "_packetsToNexusBK"
- "_packetsToNexusVI"
- "_packetsToNexusVO"
- "_pairWithSPPLink"
- "_pairingCriteria"
- "_pairingManager"
- "_pairingManagerMux"
- "_pairingProtocolVersion"
- "_pairingResultBlock"
- "_pairingTransport"
- "_parameters"
- "_parserDictionary"
- "_path"
- "_pathEvaluator"
- "_peerEndpointDictionary"
- "_peerNetworkRelayVersion"
- "_pendingAuthRequestCompletionBlocks"
- "_pendingPairingResultCompletionBlock"
- "_pendingRegistrationCompletionBlock"
- "_persistentReference"
- "_poolPurgeTimer"
- "_portString"
- "_preferWiFiRequestCount"
- "_processingNexusInput"
- "_profileChangedEventCount"
- "_properties"
- "_providesPhoneCallRelaySupport"
- "_proxyCapability"
- "_proxyInfo"
- "_proxyProviderAuthMode"
- "_proxyProviderCriteria"
- "_proxyProviderRequiresWiFi"
- "_proxyProviderType"
- "_proxyUsageRules"
- "_psm"
- "_queue"
- "_quickRelayPreference"
- "_quickRelayRequestCount"
- "_readContextForHigh"
- "_readContextForIsochronous"
- "_readContextForMedium"
- "_references"
- "_remoteAddrClassD"
- "_remoteEndpoint"
- "_reportedToABC"
- "_requiresReachability"
- "_ringIdxToStart"
- "_ringIdxToStartForMedium"
- "_rssi"
- "_scdKeyIR"
- "_scdRef"
- "_sentCheckInMessage"
- "_service"
- "_serviceClass"
- "_serviceUUID"
- "_simulateWakePacketForTesting"
- "_startRequested"
- "_startTime"
- "_started"
- "_state"
- "_timer"
- "_totalContextCount"
- "_trafficClass"
- "_transportProtocol"
- "_urgentBytesFromLink"
- "_urgentBytesToLink"
- "_uses6LoWPAN"
- "_usesASQUIC"
- "_usesTLS"
- "_uuid"
- "_version"
- "_wasInitiallySetupUsingIDSPairing"
- "_writeActivityCounterForHigh"
- "_writeActivityCounterForIsochronous"
- "_writeActivityCounterForMedium"
- "_writeContextForHigh"
- "_writeContextForIsochronous"
- "_writeContextForMedium"
- "_xpcComm"
- "_xpcCommDictionaryCallback"
- "acceptNewFlow:fromNexus:completionHandler:"
- "activate"
- "activateWithCompletion:"
- "activeOperationalScope"
- "addMatchRuleForClientsWithEntitlement:entitlementValue:"
- "addMatchToken:"
- "addObject:"
- "addObjectsFromArray:"
- "addPreferWiFiRequest"
- "addQuickRelayRequest"
- "addressData"
- "allKeys"
- "allKeysForObject:"
- "allObjects"
- "allocWithZone:"
- "allowsApplicationServiceConnections"
- "allowsDemuxForwarding"
- "allowsListenerClients"
- "anyObject"
- "appendBytes:length:"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "authRequestHandler"
- "autorelease"
- "awdlAddressData"
- "base64EncodedStringWithOptions:"
- "bluetoothLinkPreferences"
- "bluetoothUUID"
- "boolValue"
- "bytes"
- "c"
- "cancel"
- "cancelDiscovery"
- "cancelPairing"
- "candidateDiscoveredHandler"
- "candidateLostHandler"
- "class"
- "com.apple.networkrelay.encoded"
- "combinePreferences:"
- "companionLinkPreferences"
- "compare:"
- "components:fromDate:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "containsObject:"
- "controlOnly"
- "copy"
- "copyBestTestingDeviceIdentifier"
- "copyCEndpoint"
- "copyCParameters"
- "copyCertificateData"
- "copyCriteriaForCellularSlicing"
- "copyDeviceIdentifierWithIDSDeviceID:"
- "copyDeviceListString"
- "copyEncodedXPCDict"
- "copyEndpoint"
- "copyExcludedBundleIdentifiers"
- "copyIDSDeviceID"
- "copyLongDescription"
- "copyMatchRulesForCellularSlicing"
- "copyMatchTokens"
- "copyNWEndpoint"
- "copyParameters"
- "copyPropertiesForDefaultPairedPhone"
- "copyPropertiesForDefaultPairedWatch"
- "copySecKeyProxy"
- "copySendData"
- "copySharedDeviceManager"
- "copySharedMonitor"
- "copyShortDescription"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createFromEncodedXPCDict:"
- "createReadContextForPriority:readAvailableCallback:readAvailableContext:"
- "createWriteContextForPriority:writeOutputCallback:writeOutputContext:"
- "currentCalendar"
- "currentKnownNetworkProfile"
- "dataProtectionClass"
- "dataUsingEncoding:"
- "dataWithPropertyList:format:options:error:"
- "datagramMode"
- "date"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultManager"
- "description"
- "deviceHasUnpairedBluetooth:"
- "deviceIdentifier"
- "deviceInfo"
- "deviceInfoDidChange:deviceInfo:"
- "deviceIsAsleepDidChange:isAsleep:"
- "deviceIsClassCConnectedDidChange:isClassCConnected:"
- "deviceIsCloudConnectedDidChange:isCloudConnected:"
- "deviceIsConnectedDidChange:isConnected:"
- "deviceIsEnabledDidChange:isEnabled:"
- "deviceIsNearbyDidChange:isNearby:"
- "deviceIsRegisteredDidChange:isRegistered:"
- "deviceLinkTypeDidChange:linkType:"
- "deviceLinkTypeDidChange:linkType:linkSubtype:"
- "devicePluggedInStateDidChange:pluggedIn:"
- "deviceProxyServiceInterfaceNameDidChange:interfaceName:"
- "deviceSetupCompleted"
- "deviceSetupStarted"
- "deviceThermalPressureLevelDidChange:thermalPressureLevel:"
- "deviceUsesAPLDidChange:usesAPL:"
- "dictionaryWithObjects:forKeys:count:"
- "direct"
- "disableDevice:"
- "disableDevice:queue:completionBlock:"
- "enableDevice:"
- "enableDevice:queue:completionBlock:"
- "encodeBool:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpoint"
- "endpointWithAddress:"
- "endpointWithCEndpoint:"
- "endpointWithHostname:port:"
- "excludeBundleIdentifier:"
- "excludeClientApplication"
- "excludeLegacyClients"
- "excludeNonMatchingLegacyClients"
- "excludeVPNClients"
- "fileExistsAtPath:isDirectory:"
- "firstObject"
- "forwardNonMatchingTraffic"
- "fullDescription"
- "getBytes:length:"
- "getDataForAuthMethod:withCompletion:"
- "getDefaultLinkSubtypeForLinkType:"
- "getNetworkRelayVersion"
- "getUUIDBytes:"
- "handleRequestToActivateNexus:fromFlow:"
- "hasCompanionDatapath"
- "hasMatchRulesExcludingEntitlements"
- "hasMatchRulesWithTokens"
- "hasPoliciesForProxyCriteria"
- "hasPreferWiFiRequest"
- "hasProxyCriteriaAssigningTokens"
- "hasQuickRelayRequest"
- "hasValidProxyCriteria"
- "hash"
- "highThroughput"
- "hour"
- "i16@0:8"
- "includeP2P"
- "init"
- "initForHighThroughputWithServiceClass:includeP2P:"
- "initInternal"
- "initInternalWithServiceClass:highThroughout:includeP2P:"
- "initInternalWithUUID:"
- "initWithArray:"
- "initWithBluetoothUUID:queue:"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCapacity:"
- "initWithCertificateReference:options:"
- "initWithCoder:"
- "initWithDeviceIdentifier:"
- "initWithDeviceIdentifier:dataProtectionClass:options:"
- "initWithDeviceIdentifier:delegate:queue:"
- "initWithDeviceIdentifier:notificationQueue:notificationBlock:"
- "initWithDeviceIdentifier:portString:dataProtectionClass:"
- "initWithDeviceIdentifier:portString:dataProtectionClass:service:"
- "initWithDeviceIdentifier:queue:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithIdentifier:pairingCriteria:metadata:queue:"
- "initWithIdentity:"
- "initWithIdentityReference:options:"
- "initWithLinkType:"
- "initWithLocalPort:"
- "initWithNRUUID:"
- "initWithParameters:"
- "initWithReceivedData:"
- "initWithServiceClass:"
- "initWithSet:copyItems:"
- "initWithString:"
- "initWithUTF8String:"
- "initWithUUID:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "inputBytesPerSecond"
- "intValue"
- "integerValue"
- "invalidate"
- "invalidationHandler"
- "isAsleep"
- "isClassCConnected"
- "isCloudConnected"
- "isConnected"
- "isEnabled"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNRDTestServer"
- "isNearby"
- "isNotEmpty"
- "isNotEncapsulated"
- "isPersonalHotspot"
- "isProxy"
- "l"
- "length"
- "linkSubtype"
- "linkType"
- "managerState"
- "mergeProperties:"
- "minute"
- "mutableCopy"
- "newDeviceIdentifierWithBluetoothUUID:"
- "newDeviceIdentifierWithIDSDeviceID:"
- "newDeviceIdentifierWithIDSDeviceID:shouldCreate:"
- "newEphemeralDeviceIdentifier"
- "nr_dispatch_queue_create_with_qos"
- "numberWithInt:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "outputBytesPerSecond"
- "packetsPerSecond"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluggedIn"
- "policyTrafficClassifiers"
- "portString"
- "propertyListWithData:options:format:error:"
- "proxyServiceInterfaceName"
- "r"
- "registerDevice:properties:operationalproperties:queue:completionBlock:"
- "registerDevice:properties:queue:completionBlock:"
- "release"
- "removeAllObjects"
- "removeAllQuickRelayRequests"
- "removeObject:"
- "removePreferWiFiRequest"
- "removeQuickRelayRequest"
- "removing event log object for %@"
- "removing log object for %@"
- "reportedToABC"
- "requestAuthMethodForDevice:authMethod:withCompletion:"
- "requireNetworkAgentWithDomain:type:"
- "resetContextForPriority:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scrubAllDevicesWithQueue:completionBlock:"
- "scrubDevice:queue:completionBlock:"
- "second"
- "self"
- "sendXPCCommDictionary:"
- "service"
- "serviceClass"
- "setAccount:"
- "setActiveOperationalScope:"
- "setAllowedLinkSubtypes:"
- "setAllowedLinkTypes:"
- "setAllowedPeerDeviceType:"
- "setAllowsApplicationServiceConnections:"
- "setAllowsDeadPeerDetection:"
- "setAllowsDeviceDiscovery:"
- "setAllowsDirectToCloud:"
- "setAllowsPermittedClientsOnly:"
- "setAuthData:"
- "setAuthMethod:"
- "setAuthRequestHandler:"
- "setAwdlAddressData:"
- "setBluetoothEndpointType:"
- "setBluetoothLinkPreferences:"
- "setBluetoothMACAddress:"
- "setBluetoothRole:"
- "setBluetoothUUID:"
- "setCandidate:"
- "setCandidateDiscoveredHandler:"
- "setCandidateLostHandler:"
- "setCandidateService:"
- "setCbUUID:"
- "setCompanionLinkPreferences:"
- "setConnectedInterfaceName:"
- "setConnectedLinkSubtype:"
- "setConnectedLinkType:"
- "setControlOnly:"
- "setDatagramMode:"
- "setDevice:"
- "setDeviceIdentifier:"
- "setDeviceType:"
- "setDirect:"
- "setDomain:"
- "setEntitlements:"
- "setEventHandler:"
- "setFlags:"
- "setForwardNonMatchingTraffic:"
- "setHandlesLinkRecommendations:"
- "setHttpConnectPSK:"
- "setHttpConnectPSKIdentity:"
- "setHttpConnectPassword:"
- "setHttpConnectURLs:"
- "setHttpConnectUserName:"
- "setIdentifier:"
- "setInputBytesPerSecond:"
- "setInvalidationHandler:"
- "setIsAltAccountPairing:"
- "setIsExternalPairing:"
- "setIsNRDTestServer:"
- "setIsNotEncapsulated:"
- "setIsReachableOverWiFi:"
- "setLocalEndpoint:"
- "setManagerState:"
- "setMatchResultAccountID:"
- "setMatchResultBundleID:"
- "setMetadata:"
- "setMigrationPairing:"
- "setNrDeviceIdentifier:"
- "setNrDeviceIdentifiers:"
- "setObject:forKeyedSubscript:"
- "setOperationalProperties:"
- "setOperationalScope:"
- "setOutOfBandKey:"
- "setOutputBytesPerSecond:"
- "setPacketsPerSecond:"
- "setPairWithSPPLink:"
- "setPairingCriteria:"
- "setPairingProtocolVersion:"
- "setPairingTransport:"
- "setPeerEndpointDictionary:"
- "setPeerNetworkRelayVersion:"
- "setPolicyTrafficClassifiers:"
- "setProperties:"
- "setProvidesPhoneCallRelaySupport:"
- "setProxyCapability:"
- "setProxyInfo:"
- "setProxyProviderAuthMode:"
- "setProxyProviderCriteria:"
- "setProxyProviderRequiresWiFi:"
- "setProxyProviderType:"
- "setProxyUsageRules:"
- "setPsm:"
- "setReceiveXPCCommDictionaryHandler:"
- "setRemoteEndpoint:"
- "setReportedToABC:"
- "setRequiresReachability:"
- "setRssi:"
- "setServiceClass:"
- "setServiceUUID:"
- "setStartTime:"
- "setTrafficClass:"
- "setTransportProtocol:"
- "setUseP2P:"
- "setUses6LoWPAN:"
- "setUsesTLS:"
- "setUuid:"
- "setVersion:"
- "setWasInitiallySetupUsingIDSPairing:"
- "sortedArrayUsingSelector:"
- "start"
- "startBrowse:fromNexus:"
- "startDiscoveryWithCompletion:"
- "startMonitoringEventType:error:"
- "startPairingDevice:withCompletion:resultBlock:"
- "startTime"
- "stopBrowse:fromNexus:"
- "string"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringToIndex:"
- "superclass"
- "supportsSecureCoding"
- "thermalPressureLevel"
- "timeIntervalSinceReferenceDate"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unpairDevice:queue:withCompletion:"
- "unpairDevice:withCompletion:"
- "unregisterAllDevicesWithQueue:completionBlock:"
- "unregisterDevice:"
- "unregisterDevice:queue:completionBlock:"
- "unsignedCharValue"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "unsignedShortValue"
- "uses6LoWPAN"
- "usesASQUIC"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8S16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@\"NENexus\"16@\"NENexusFlow\"24"
- "v32@0:8@\"NENexusBrowse\"16@\"NENexus\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v40@0:8@\"NENexusFlow\"16@\"NENexus\"24@?<v@?@\"NENexusFlowAssignedProperties\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16Q24@?32"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "zone"
- "{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
