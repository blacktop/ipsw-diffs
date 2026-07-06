## accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

-  __TEXT.__text: 0x183af0
-  __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0x9180
-  __TEXT.__objc_methlist: 0x6b84
-  __TEXT.__const: 0x20e0
-  __TEXT.__gcc_except_tab: 0x1bb4
-  __TEXT.__objc_classname: 0xf93
-  __TEXT.__objc_methname: 0xf3d0
-  __TEXT.__objc_methtype: 0x2f90
-  __TEXT.__cstring: 0xd52c
-  __TEXT.__oslogstring: 0x37447
+  __TEXT.__text: 0x199608
+  __TEXT.__auth_stubs: 0x1890
+  __TEXT.__objc_stubs: 0x95c0
+  __TEXT.__objc_methlist: 0x6e8c
+  __TEXT.__const: 0x2110
+  __TEXT.__gcc_except_tab: 0x20e0
+  __TEXT.__objc_classname: 0xfd3
+  __TEXT.__objc_methname: 0xfeab
+  __TEXT.__objc_methtype: 0x321c
+  __TEXT.__cstring: 0xe275
+  __TEXT.__oslogstring: 0x37924
   __TEXT.__ustring: 0x232
-  __TEXT.__unwind_info: 0x4180
-  __DATA_CONST.__const: 0x8760
-  __DATA_CONST.__cfstring: 0x6b00
-  __DATA_CONST.__objc_classlist: 0x300
+  __TEXT.__unwind_info: 0x4758
+  __DATA_CONST.__const: 0x99a0
+  __DATA_CONST.__cfstring: 0x7340
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x2e0
+  __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA_CONST.__auth_got: 0xc70
-  __DATA_CONST.__got: 0xdd8
-  __DATA_CONST.__auth_ptr: 0xc0
-  __DATA.__objc_const: 0xa708
-  __DATA.__objc_selrefs: 0x3240
-  __DATA.__objc_ivar: 0x700
-  __DATA.__objc_data: 0x1e00
-  __DATA.__data: 0x1a78
-  __DATA.__bss: 0x1678
+  __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__auth_got: 0xc58
+  __DATA_CONST.__got: 0xec8
+  __DATA_CONST.__auth_ptr: 0x98
+  __DATA.__objc_const: 0xb078
+  __DATA.__objc_selrefs: 0x33b8
+  __DATA.__objc_ivar: 0x7a0
+  __DATA.__objc_data: 0x1ef0
+  __DATA.__data: 0x1940
+  __DATA.__bss: 0x1618
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 8002
-  Symbols:   51708
-  CStrings:  9259
+  Functions: 8569
+  Symbols:   55126
+  CStrings:  9569
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
Symbols:
+ -[ACCConnectionSnapshotInfo .cxx_destruct]
+ -[ACCConnectionSnapshotInfo accInfo]
+ -[ACCConnectionSnapshotInfo adapterPID]
+ -[ACCConnectionSnapshotInfo adapterVID]
+ -[ACCConnectionSnapshotInfo authInfo]
+ -[ACCConnectionSnapshotInfo connectionType]
+ -[ACCConnectionSnapshotInfo connectionUUID]
+ -[ACCConnectionSnapshotInfo createTimestampMs]
+ -[ACCConnectionSnapshotInfo endpoints]
+ -[ACCConnectionSnapshotInfo identifier]
+ -[ACCConnectionSnapshotInfo initWithDictionary:]
+ -[ACCConnectionSnapshotInfo isConnectedThroughAdapter]
+ -[ACCConnectionSnapshotInfo properties]
+ -[ACCEndpointSnapshotInfo .cxx_destruct]
+ -[ACCEndpointSnapshotInfo accInfo]
+ -[ACCEndpointSnapshotInfo adapterPID]
+ -[ACCEndpointSnapshotInfo adapterVID]
+ -[ACCEndpointSnapshotInfo appMatchProtocols]
+ -[ACCEndpointSnapshotInfo appMatchTeamIDs]
+ -[ACCEndpointSnapshotInfo authInfo]
+ -[ACCEndpointSnapshotInfo carPlayCapable]
+ -[ACCEndpointSnapshotInfo certData]
+ -[ACCEndpointSnapshotInfo certSerial]
+ -[ACCEndpointSnapshotInfo connectionType]
+ -[ACCEndpointSnapshotInfo connectionUUID]
+ -[ACCEndpointSnapshotInfo createTimestampMs]
+ -[ACCEndpointSnapshotInfo eaProtocols]
+ -[ACCEndpointSnapshotInfo endpointUUID]
+ -[ACCEndpointSnapshotInfo featuresBitMask]
+ -[ACCEndpointSnapshotInfo identifier]
+ -[ACCEndpointSnapshotInfo initWithDictionary:]
+ -[ACCEndpointSnapshotInfo isConnectedThroughAdapter]
+ -[ACCEndpointSnapshotInfo isWireless]
+ -[ACCEndpointSnapshotInfo multipleEASessionsCapable]
+ -[ACCEndpointSnapshotInfo parentConnection]
+ -[ACCEndpointSnapshotInfo preferredApp]
+ -[ACCEndpointSnapshotInfo properties]
+ -[ACCEndpointSnapshotInfo protocolType]
+ -[ACCEndpointSnapshotInfo themeAssetsCapable]
+ -[ACCEndpointSnapshotInfo transportType]
+ -[ACCEndpointSnapshotInfo usbCarPlayCapable]
+ -[ACCEndpointSnapshotInfo vehicleInfo]
+ -[ACCEndpointSnapshotInfo wirelessCarPlayCapable]
+ -[ACCExternalAccessory _addAccessoryInfoFromSnapshot:connectionSnapshot:]
+ -[ACCExternalAccessory _addEAProtocolPrimaryEndpointInfoFromSnapshot:connectionSnapshot:]
+ -[ACCExternalAccessory _addEAProtocolsForEAEndpointsFromSnapshots:connectionUUID:]
+ -[ACCExternalAccessory _addGenericMFiEAProtocolsFromSnapshot:connectionUUID:]
+ -[ACCExternalAccessory _addiAP2AuthInfoFromSnapshot:]
+ -[ACCExternalAccessory _addiAP2EAProtocolsFromSnapshot:connectionUUID:]
+ -[ACCExternalAccessory _addiAP2IdentificationInfoFromSnapshot:]
+ -[ACCExternalAccessory _addiAP2VehicleInfoFromSnapshot:]
+ -[ACCExternalAccessory _nativeUSBEndpointUUIDForProtocolIdentifierFromSnapshot:connectionUUID:]
+ -[ACCPlatformPowerInfo initWithEndpointUID:andModelNumber:andBitmask:andOldBitmask:]
+ -[ACCPlatformPowerInfo isModelNumberConnected:]
+ -[ACCPlatformPowerInfo modelNumber]
+ -[ACCPlatformPowerInfo setModelNumber:]
+ -[ACCPlatformPowerManager addAccessoryForEndpointUID:andModelNumber:andBitmask:andOldBitmask:]
+ -[ACCPlatformSleepAssertionManager _addSleepAssertionForUUID:withConnectionType:]
+ -[ACCPlatformSleepAssertionManager addSleepAssertionForUUID:withConnectionType:]
+ -[PlatformIAPDBridge _generateIAPDPortTypeForDictionary:withConnectionType:transportType:]
+ -[PlatformIAPDBridge iapdAccessoryArrivedWithSnapshotInfo:endpointUUID:protocol:transportType:connectionType:]
+ -[PlatformIAPDBridge iapdAccessoryProcessIncomingDataWithSnapshotInfo:transportType:protocol:incomingData:]
+ -[_ACConnection pConnection]
+ -[_ACConnection setPConnection:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ACCConnectionSnapshotInfo.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ACCEndpointSnapshotInfo.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_connection2.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_connectionEndpoint_snapshotInfoKeys.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_endpoint2.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager2.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager2_connection.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager2_cta.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager2_endpoint.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager2_featureHandler.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager2_helper.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_platform_analytics2.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccm-decrypt-ceb7cce1b63de9f6bb9cea53aa843b31.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccm-encrypt-739dafc2d601adca866a48cb0dba9abe.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_add-3c836ac7d4f46e74b1e60bd32a0cbcd0.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_add-bdf79ea9f2ea12cfdc27d22fd37ae247.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_cmp-7758bbea61e26b5f0285768cea064611.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_mul-535c9d4517ef5c98d978f30f82c7d245.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_mul-e3b444859026a761ebf36ed973d0932e.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_n-b1ce3e3f2d9715cdda21f821bedd93e7.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_set-85eb7a76bbc72081f499a675dfcddacd.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_shift_right-00ecf205ef375a5f1ab915652aa3051c.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_shift_right-c8ff3a6d528ff465e68c5c7c32da8818.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_sub-efb7ab9a919f7ef2823f2f8eca5a5c52.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_sub-f9e2c095270ba12768878c94b1a10f8f.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_sub1-77f6ce147eb936f02051f67c9c69f7a5.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(mfi4Auth_connectionInfo_feature_handlers.o)
+ ACCConnectionSnapshotInfo.m
+ ACCEndpointSnapshotInfo.m
+ GCC_except_table101
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table11
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table152
+ GCC_except_table219
+ GCC_except_table22
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table24
+ GCC_except_table247
+ GCC_except_table28
+ GCC_except_table52
+ GCC_except_table62
+ GCC_except_table89
+ GCC_except_table94
+ GCC_except_table98
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._accInfo
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._adapterPID
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._adapterVID
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._authInfo
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._connectionType
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._connectionUUID
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._createTimestampMs
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._endpoints
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._identifier
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._isConnectedThroughAdapter
+ OBJC_IVAR_$_ACCConnectionSnapshotInfo._properties
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._accInfo
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._adapterPID
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._adapterVID
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._appMatchProtocols
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._appMatchTeamIDs
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._authInfo
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._carPlayCapable
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._certData
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._certSerial
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._connectionType
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._connectionUUID
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._createTimestampMs
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._eaProtocols
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._endpointUUID
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._featuresBitMask
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._identifier
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._isConnectedThroughAdapter
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._multipleEASessionsCapable
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._parentConnection
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._preferredApp
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._properties
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._protocolType
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._themeAssetsCapable
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._transportType
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._usbCarPlayCapable
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._vehicleInfo
+ OBJC_IVAR_$_ACCEndpointSnapshotInfo._wirelessCarPlayCapable
+ OBJC_IVAR_$_ACCPlatformPowerInfo._modelNumber
+ OBJC_IVAR_$__ACConnection._pConnection
+ _CFAllocatorGetDefault
+ _CFAutorelease
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_ACCConnectionSnapshotInfo
+ _OBJC_CLASS_$_ACCEndpointSnapshotInfo
+ _OBJC_CLASS_$__ACConnection
+ _OBJC_METACLASS_$_ACCConnectionSnapshotInfo
+ _OBJC_METACLASS_$_ACCEndpointSnapshotInfo
+ _OBJC_METACLASS_$__ACConnection
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ __81-[ACCPlatformSleepAssertionManager _addSleepAssertionForUUID:withConnectionType:]_block_invoke
+ __Block_byref_object_copy_
+ __Block_byref_object_dispose_
+ __OBJC_$_INSTANCE_METHODS_ACCConnectionSnapshotInfo
+ __OBJC_$_INSTANCE_METHODS_ACCEndpointSnapshotInfo
+ __OBJC_$_INSTANCE_METHODS__ACConnection
+ __OBJC_$_INSTANCE_VARIABLES_ACCConnectionSnapshotInfo
+ __OBJC_$_INSTANCE_VARIABLES_ACCEndpointSnapshotInfo
+ __OBJC_$_INSTANCE_VARIABLES__ACConnection
+ __OBJC_$_PROP_LIST_ACCConnectionSnapshotInfo
+ __OBJC_$_PROP_LIST_ACCEndpointSnapshotInfo
+ __OBJC_$_PROP_LIST__ACConnection
+ __OBJC_CLASS_RO_$_ACCConnectionSnapshotInfo
+ __OBJC_CLASS_RO_$_ACCEndpointSnapshotInfo
+ __OBJC_CLASS_RO_$__ACConnection
+ __OBJC_METACLASS_RO_$_ACCConnectionSnapshotInfo
+ __OBJC_METACLASS_RO_$_ACCEndpointSnapshotInfo
+ __OBJC_METACLASS_RO_$__ACConnection
+ ___110-[PlatformIAPDBridge iapdAccessoryArrivedWithSnapshotInfo:endpointUUID:protocol:transportType:connectionType:]_block_invoke
+ ___48-[ACCConnectionSnapshotInfo initWithDictionary:]_block_invoke
+ ___54-[ACCExternalAccessory _addEAProtocolsForEAEndpoints:]_block_invoke
+ ___80-[ACCPlatformSleepAssertionManager addSleepAssertionForUUID:withConnectionType:]_block_invoke
+ ___81-[ACCExternalAccessory _nativeUSBEndpointUUIDForProtocolIdentifier:iAP2Endpoint:]_block_invoke
+ ___81-[ACCPlatformSleepAssertionManager _addSleepAssertionForUUID:withConnectionType:]_block_invoke
+ _____MsgSentOutCB_block_invoke
+ _____findWirelessCTAReceiverCapableConnection_block_invoke
+ ____accAuthProtocol_endpoint_authReadyChanged_block_invoke
+ ____accAuthProtocol_endpoint_connectionInfo_handleInterceptData_block_invoke
+ ____acc_connection2_analytics_connectionWillBeDestroyed_withSnapshotInfo_block_invoke
+ ____acc_connection2_analytics_connectionWillBePublished_block_invoke
+ ____acc_connection2_connectionInfo_accessoryConnectionAttached_block_invoke
+ ____acc_connection2_connectionInfo_accessoryConnectionDetached_withSnapshotInfo_block_invoke
+ ____acc_connection2_connectionInfo_accessoryConnectionInfoPropertyChanged_block_invoke
+ ____acc_connection2_externalAccessory_addEAAccessoryForEAEndpoints_block_invoke
+ ____acc_connection2_externalAccessory_removeEAAccessoryForPrimaryEndpoints_block_invoke
+ ____acc_connection2_invokeFeatureHandlerWithResult_asyncImpl_block_invoke
+ ____acc_connection2_notifications_propertiesDidChangeForConnection_block_invoke
+ ____acc_endpoint2_analytics_endpointAccessoryInfoDidChange_block_invoke
+ ____acc_endpoint2_analytics_endpointProtocolDidChange_block_invoke
+ ____acc_endpoint2_analytics_endpointWillBeDestroyed_withSnapshotInfo_block_invoke
+ ____acc_endpoint2_analytics_endpointWillBePublished_block_invoke
+ ____acc_endpoint2_connectionInfo_accessoryEndpointAttached_block_invoke
+ ____acc_endpoint2_connectionInfo_accessoryEndpointDetached_block_invoke
+ ____acc_endpoint2_connectionInfo_accessoryEndpointInfoPropertyChanged_block_invoke
+ ____acc_endpoint2_connectionInfo_accessoryEndpointProtocolUpdate_block_invoke
+ ____acc_endpoint2_notifications_authenticationStatusDidChangeForConnectionUUID_block_invoke
+ ____acc_endpoint2_notifications_propertiesDidChangeForEndpointUUID_block_invoke
+ ____acc_manager2_checkForInductiveCTA_checkMatch_block_invoke
+ ____acc_manager2_checkForWirelessCTA_checkMatch_block_invoke
+ ____acc_manager2_copyAdapterForConnection_internal_block_invoke
+ ____acc_manager2_copyConnectionsThroughAdapter_internal_block_invoke
+ ____acc_manager2_createSnapshotInfoAsync_block_invoke
+ ____acc_manager2_createSnapshotInfoAsync_block_invoke_2
+ ____acc_manager2_invokeFeatureHandlerForAllConnectionEndpoint_internal_block_invoke
+ ____acc_manager2_invokeFeatureHandlerForConnectionEndpoint_internal_block_invoke
+ ____acc_manager2_invokeFeatureHandlerWithResultForConnectionEndpoint_internal_block_invoke
+ ____addConnection_block_invoke
+ ____analytics_nfcEndpointWillBePublished_block_invoke
+ ____analytics_nfcEndpointWillBePublished_block_invoke_2
+ ____audioProductCerts_endpoint_handlePropertiesDidChange_block_invoke_2
+ ____audioProductCerts_endpoint_handlePropertiesDidChange_block_invoke_3
+ ____authAndIDComplete_block_invoke
+ ____configStream_endpoint_connectionInfo_categoryListReady_block_invoke
+ ____configStream_endpoint_connectionInfo_propertyResponse_block_invoke
+ ____configStream_endpoint_processCategoryListReady_block_invoke
+ ____configureAndUnlockUSBHostInterfaces_block_invoke
+ ____destroyFeature_block_invoke
+ ____destroyFeature_block_invoke_2
+ ____genericMFi_appLaunch_RequestUserForAppLaunch_block_invoke_3
+ ____genericMFi_endpoint_handleAuthStatusDidChange_block_invoke
+ ____genericMFi_endpoint_handleAuthStatusDidChange_block_invoke_2
+ ____genericMFi_endpoint_handlePropertiesDidChange_block_invoke_2
+ ____genericMFi_endpoint_handlePropertiesDidChange_block_invoke_3
+ ____iAP2MediaLibraryMsgCleanupCB_block_invoke
+ ____initReferenceDate_block_invoke
+ ____mfi4Auth_endpoint_firstUnlockHandler_block_invoke
+ ____mfi4Auth_endpoint_firstUnlockHandler_block_invoke_2
+ ____mfi4Auth_featureHandler_beginUserKeyErase_block_invoke
+ ____mfi4Auth_featureHandler_beginVendorKeyErase_block_invoke
+ ____mfi4Auth_featureHandler_cancelUserKeyErase_block_invoke
+ ____mfi4Auth_featureHandler_cancelVendorKeyErase_block_invoke
+ ____mfi4Auth_featureHandler_continueUserKeyErase_block_invoke
+ ____mfi4Auth_featureHandler_continueVendorKeyErase_block_invoke
+ ____mfi4Auth_featureHandler_copyUserPrivateKey_block_invoke
+ ____mfi4Auth_featureHandler_getAccessoryUserName_block_invoke
+ ____mfi4Auth_featureHandler_getPrivateNvmKeyValues_block_invoke
+ ____mfi4Auth_featureHandler_getPublicNvmKeyValues_block_invoke
+ ____mfi4Auth_featureHandler_provisionPairing_block_invoke
+ ____mfi4Auth_featureHandler_resetPairing_block_invoke
+ ____mfi4Auth_featureHandler_setAccessoryUserName_block_invoke
+ ____mfi4Auth_featureHandler_setPrivateNvmKeyValues_block_invoke
+ ____mfi4Auth_featureHandler_setPublicNvmKeyValues_block_invoke
+ ____oobPairing_endpoint_handlePairingInfo_block_invoke
+ ____parseUSBHostHIDComponentIdentificationParams_block_invoke
+ ____platform_externalAccessory_EASessionOpened_manager2_block_invoke
+ ____processAccessoryInfoOverrides_block_invoke
+ ____processAccessoryPowerUpdate_block_invoke
+ ____processPowerSourceUpdate_block_invoke
+ ____processPowerSourceUpdate_block_invoke_2
+ ____processPowerUpdates_block_invoke
+ ____recalcWindowSize_block_invoke
+ ____requestAppLaunchHandler_block_invoke_2
+ ____requestAuthorization_block_invoke_2
+ ____requestAuthorization_block_invoke_3
+ ____startFeatureFromDevice_block_invoke
+ ____startFeatureFromDevice_block_invoke_2
+ ___accAuthProtocol_endpoint_authReadyChanged_block_invoke
+ ___accAuthProtocol_endpoint_destroy_block_invoke_2
+ ___acc_connection2_addToDictionaryPropertyForEndpoint_block_invoke
+ ___acc_connection2_addToDictionaryPropertyForEndpoint_block_invoke_2
+ ___acc_connection2_addToDictionaryProperty_block_invoke
+ ___acc_connection2_analytics_connectionAuthUnsuccessfulForProtocol_block_invoke
+ ___acc_connection2_analytics_connectionAuthUnsuccessfulForProtocol_block_invoke_2
+ ___acc_connection2_analytics_connectionAuthUnsuccessful_block_invoke
+ ___acc_connection2_analytics_connectionAuthUnsuccessful_block_invoke_2
+ ___acc_connection2_analytics_connectionPassedAuthForProtocol_block_invoke
+ ___acc_connection2_analytics_connectionPassedAuthForProtocol_block_invoke_2
+ ___acc_connection2_analytics_connectionPassedAuth_block_invoke
+ ___acc_connection2_analytics_connectionPassedAuth_block_invoke_2
+ ___acc_connection2_analytics_iap2_featuresSupportedDidChange_block_invoke
+ ___acc_connection2_analytics_iap2_featuresSupportedDidChange_block_invoke_2
+ ___acc_connection2_appendToArrayPropertyForEndpoint_block_invoke
+ ___acc_connection2_appendToArrayPropertyForEndpoint_block_invoke_2
+ ___acc_connection2_appendToArrayProperty_block_invoke
+ ___acc_connection2_copyAccessoryInfoDictionary_block_invoke
+ ___acc_connection2_copyDescription_block_invoke
+ ___acc_connection2_copyEndpointSnapshotInfo_block_invoke
+ ___acc_connection2_copyEndpointSnapshotInfo_block_invoke_2
+ ___acc_connection2_copyEndpointUUIDs_block_invoke
+ ___acc_connection2_copyIdentifierForEndpoint_block_invoke
+ ___acc_connection2_copyIdentifier_block_invoke
+ ___acc_connection2_copyPropertiesForEndpoint_block_invoke
+ ___acc_connection2_copyPropertiesForEndpoint_block_invoke_2
+ ___acc_connection2_copyProperties_block_invoke
+ ___acc_connection2_copyProperty_block_invoke
+ ___acc_connection2_copyProperty_block_invoke_2
+ ___acc_connection2_copySnapshotInfo_block_invoke
+ ___acc_connection2_copyUUID_block_invoke
+ ___acc_connection2_createEndpoint_block_invoke
+ ___acc_connection2_createSnapshotInfoAsync_block_invoke
+ ___acc_connection2_createSnapshotInfo_block_invoke
+ ___acc_connection2_destroyEndpoint_block_invoke
+ ___acc_connection2_destroyEndpoint_block_invoke_2
+ ___acc_connection2_destroyEndpoint_block_invoke_3
+ ___acc_connection2_destroy_block_invoke
+ ___acc_connection2_endpointIterateForConnection_block_invoke
+ ___acc_connection2_getAuthInfo_block_invoke
+ ___acc_connection2_getAuthStatus_block_invoke
+ ___acc_connection2_getEndpointStruct_block_invoke
+ ___acc_connection2_getEndpointStruct_block_invoke_2
+ ___acc_connection2_getProtocolForEndpoint_block_invoke
+ ___acc_connection2_getTransportTypeForEndpoint_block_invoke
+ ___acc_connection2_getType_block_invoke
+ ___acc_connection2_invokeFeatureHandlerWithResult_asyncImpl_block_invoke
+ ___acc_connection2_invokeFeatureHandler_asyncWithAssert_block_invoke
+ ___acc_connection2_invokeFeatureHandler_asyncWithAssert_block_invoke_2
+ ___acc_connection2_invokeFeatureHandler_asyncWithAssert_block_invoke_3
+ ___acc_connection2_invokeFeatureHandler_asyncWithAssert_block_invoke_4
+ ___acc_connection2_invokeFeatureHandler_asyncWithAssert_block_invoke_5
+ ___acc_connection2_invokeFeatureHandler_asyncWithAssert_block_invoke_6
+ ___acc_connection2_invokeFeatureHandler_block_invoke
+ ___acc_connection2_invokeFeatureHandler_block_invoke_2
+ ___acc_connection2_invokeFeatureHandler_block_invoke_3
+ ___acc_connection2_invokeFeatureHandler_block_invoke_4
+ ___acc_connection2_invokeFeatureHandler_block_invoke_5
+ ___acc_connection2_invokeFeatureHandler_block_invoke_6
+ ___acc_connection2_isAuthenticatedForAppMatchLaunch_block_invoke
+ ___acc_connection2_isAuthenticatedForInductivePowerIn_block_invoke
+ ___acc_connection2_isAuthenticated_block_invoke
+ ___acc_connection2_mapAccessoryInfo_block_invoke
+ ___acc_connection2_mapAccessoryInfo_internal_block_invoke
+ ___acc_connection2_mapAccessoryInfo_internal_block_invoke_2
+ ___acc_connection2_performAsyncWithCleanup_block_invoke
+ ___acc_connection2_performBlockForConnection_block_invoke
+ ___acc_connection2_performBlockForEndpoint_asyncWithCleanup_block_invoke
+ ___acc_connection2_performBlockForEndpoint_block_invoke
+ ___acc_connection2_performSyncWithCleanup_block_invoke
+ ___acc_connection2_processIncomingDataForEndpoint_block_invoke
+ ___acc_connection2_processIncomingDataForEndpoint_block_invoke_2
+ ___acc_connection2_publish_block_invoke
+ ___acc_connection2_publish_internal_block_invoke
+ ___acc_connection2_removePropertyForEndpoint_block_invoke
+ ___acc_connection2_removePropertyForEndpoint_block_invoke_2
+ ___acc_connection2_removeProperty_block_invoke
+ ___acc_connection2_sendDataOut_internal_block_invoke
+ ___acc_connection2_setAccessoryInfoForEndpoint_block_invoke
+ ___acc_connection2_setAccessoryInfoForEndpoint_block_invoke_2
+ ___acc_connection2_setAccessoryInfoOverridesWithDictionaryForEndpoint_block_invoke
+ ___acc_connection2_setAccessoryInfoOverridesWithDictionaryForEndpoint_block_invoke_2
+ ___acc_connection2_setAuthCertData_block_invoke
+ ___acc_connection2_setAuthCertData_block_invoke_2
+ ___acc_connection2_setAuthStatus_block_invoke
+ ___acc_connection2_setAuthStatus_internal_block_invoke
+ ___acc_connection2_setPropertiesForEndpoint_block_invoke
+ ___acc_connection2_setPropertiesForEndpoint_block_invoke_2
+ ___acc_connection2_setProperties_block_invoke
+ ___acc_connection2_setProperty_block_invoke
+ ___acc_connection2_setProperty_block_invoke_2
+ ___acc_connection2_setProperty_internal_block_invoke
+ ___acc_connection2_setSupervisedTransportsRestricted_block_invoke
+ ___acc_endpoint2_externalAccessory_addEAAccessoryForPrimaryEndpoint_block_invoke
+ ___acc_endpoint2_externalAccessory_handleIncomingEADataFromAccessoryForEndpointUUID_block_invoke
+ ___acc_endpoint2_externalAccessory_removeEAAccessoryForPrimaryEndpoint_block_invoke
+ ___acc_endpoint2_externalAccessory_updateEAAccessoryInfoForEndpointWithUUID_block_invoke
+ ___acc_endpoint2_invokeFeatureHandlerWithResult_block_invoke
+ ___acc_endpoint2_invokeFeatureHandler_block_invoke
+ ___acc_endpoint2_invokeFeatureHandler_block_invoke_2
+ ___acc_endpoint2_invokeFeatureHandler_block_invoke_3
+ ___acc_endpoint2_sendOutgoingData_block_invoke
+ ___acc_endpoint2_supervisedTransportsRestrictedDidChange_block_invoke
+ ___acc_manager2_addToDictionaryPropertyForConnection_block_invoke
+ ___acc_manager2_addToDictionaryPropertyForEndpoint_block_invoke
+ ___acc_manager2_appendToArrayPropertyForConnection_block_invoke
+ ___acc_manager2_appendToArrayPropertyForEndpoint_block_invoke
+ ___acc_manager2_checkForInductiveCTA_block_invoke
+ ___acc_manager2_checkForInductiveCTA_block_invoke_2
+ ___acc_manager2_checkForInductiveCTA_block_invoke_3
+ ___acc_manager2_checkForWirelessCTA_block_invoke
+ ___acc_manager2_checkForWirelessCTA_block_invoke_2
+ ___acc_manager2_checkForWirelessCTA_block_invoke_3
+ ___acc_manager2_copyAccessoryInfoDictionaryForConnection_block_invoke
+ ___acc_manager2_copyAllConnectionUUIDs_block_invoke
+ ___acc_manager2_copyAuthCertDataForConnection_block_invoke
+ ___acc_manager2_copyCertCapabilitiesForConnection_block_invoke
+ ___acc_manager2_copyCertSerialForConnection_block_invoke
+ ___acc_manager2_copyCertSerialStringForConnection_block_invoke
+ ___acc_manager2_copyConnectionSnapshotInfo_block_invoke
+ ___acc_manager2_copyEndpointIdentifier_block_invoke
+ ___acc_manager2_copyEndpointSnapshotInfo_block_invoke
+ ___acc_manager2_copyEndpointUUIDsForConnection_block_invoke
+ ___acc_manager2_copyIdentifierForConnection_block_invoke
+ ___acc_manager2_copyPropertiesForConnection_block_invoke
+ ___acc_manager2_copyPropertiesForEndpoint_block_invoke
+ ___acc_manager2_createAllSnapshotInfoAsync_block_invoke
+ ___acc_manager2_createEndpointForConnection_block_invoke
+ ___acc_manager2_createSnapshotInfoAsync_block_invoke
+ ___acc_manager2_getAuthStatusForConnection_block_invoke
+ ___acc_manager2_getConnectionType_block_invoke
+ ___acc_manager2_getEndpointProtocol_block_invoke
+ ___acc_manager2_getEndpointTransportType_block_invoke
+ ___acc_manager2_invokeFeatureHandlerWithResultForConnectionEndpoint_internal_block_invoke
+ ___acc_manager2_invokeFeatureHandlerWithResult_block_invoke
+ ___acc_manager2_invokeFeatureHandler_block_invoke
+ ___acc_manager2_invokeFeatureHandler_block_invoke_2
+ ___acc_manager2_isConnectionAuthenticatedForAppMatchLaunch_block_invoke
+ ___acc_manager2_isConnectionAuthenticated_block_invoke
+ ___acc_manager2_performAsync_block_invoke
+ ___acc_manager2_performBlockForConnectionEndpoint_asyncWithCleanup_block_invoke
+ ___acc_manager2_performBlockForConnectionEndpoint_block_invoke
+ ___acc_manager2_performBlockForConnection_block_invoke
+ ___acc_manager2_performBlockForConnection_internal_block_invoke
+ ___acc_manager2_performPlatformWorkAsync_block_invoke
+ ___acc_manager2_performPlatformWorkForConnectionEndpointAsync_block_invoke
+ ___acc_manager2_performSync_block_invoke
+ ___acc_manager2_processIncomingDataForConnectionEndpoint_block_invoke
+ ___acc_manager2_publishConnection_block_invoke
+ ___acc_manager2_removeConnectionEndpoint_block_invoke
+ ___acc_manager2_removeConnection_block_invoke
+ ___acc_manager2_removePropertyForConnection_block_invoke
+ ___acc_manager2_removePropertyForEndpoint_block_invoke
+ ___acc_manager2_sendOutgoingDataForConnectionEndpoint_block_invoke
+ ___acc_manager2_setAccessoryInfoForEndpoint_block_invoke
+ ___acc_manager2_setAccessoryInfoOverridesWithDictionaryForEndpoint_block_invoke
+ ___acc_manager2_setAdapterPropertiesOnConnectionsAsync_block_invoke
+ ___acc_manager2_setAuthCertDataForConnection_block_invoke
+ ___acc_manager2_setAuthStatusForConnection_block_invoke
+ ___acc_manager2_setAuthStatusWithCertDataForConnection_block_invoke
+ ___acc_manager2_setAuthStatusWithCertDataForConnection_block_invoke_2
+ ___acc_manager2_setAuthStatusWithCertDataForConnection_block_invoke_3
+ ___acc_manager2_setPropertiesForConnection_block_invoke
+ ___acc_manager2_setPropertiesForEndpoint_block_invoke
+ ___acc_manager2_setPropertiesOnConnectionsThroughAdapterConnectionAsync_block_invoke
+ ___acc_manager2_setPropertyForConnection_block_invoke
+ ___acc_manager2_setSupervisedTransportsRestricted_block_invoke
+ ___acc_manager2_sharedManager_block_invoke
+ ___acc_protocolRouter_destroyProtocolLayer_block_invoke
+ ___acc_protocolRouter_initProtocolLayer_block_invoke
+ ___acc_protocolRouter_routeIncomingData_block_invoke
+ ___addConnection_block_invoke
+ ___audioProductCerts_endpoint_destroy_block_invoke_2
+ ___block_descriptor_32_e231_B32?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}24l
+ ___block_descriptor_32_e37_v24?0^{__CFString=}8^{__CFString=}16l
+ ___block_descriptor_36_e231_B32?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}24l
+ ___block_descriptor_40_e8_32bs_e25_B24?0^{__CFString=}8^v16ls32l8
+ ___block_descriptor_40_e8_32bs_e35_v24?0^{__CFArray=}8^{__CFError=}16ls32l8
+ ___block_descriptor_40_e8_32bs_e41_B32?0^{__CFString=}8^{__CFString=}16^v24ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e188_B24?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB}16lr32l8
+ ___block_descriptor_40_e8_32r_e231_B32?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}24lr32l8
+ ___block_descriptor_40_e8_32r_e41_B32?0^{__CFString=}8^{__CFString=}16^v24lr32l8
+ ___block_descriptor_40_e8_32s_e35_v24?0^{__CFString=}8^{__CFData=}16ls32l8
+ ___block_descriptor_40_e8_32s_e37_v24?0^{__CFString=}8^{__CFString=}16ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e51_B32?0^{__CFString=}8^{__CFString=}16^{__CFData=}24lw32l8
+ ___block_descriptor_42_e5_v8?0l
+ ___block_descriptor_44_e188_B24?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB}16l
+ ___block_descriptor_44_e41_B32?0^{__CFString=}8^{__CFString=}16^v24l
+ ___block_descriptor_44_e8_32r_e51_v24?0^{__CFString=}8"ACCConnectionSnapshotInfo"16lr32l8
+ ___block_descriptor_44_e8_32s_e37_v24?0^{__CFString=}8^{__CFString=}16ls32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_45_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_46_e37_v24?0^{__CFString=}8^{__CFString=}16l
+ ___block_descriptor_46_e5_v8?0l
+ ___block_descriptor_48_e188_B24?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB}16l
+ ___block_descriptor_48_e37_v24?0^{__CFString=}8^{__CFString=}16l
+ ___block_descriptor_48_e8_32bs40r_e41_B32?0^{__CFString=}8^{__CFString=}16^v24lr40l8s32l8
+ ___block_descriptor_48_e8_32bs_e51_v24?0^{__CFString=}8"ACCConnectionSnapshotInfo"16ls32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r_e231_B32?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}24lr32l8
+ ___block_descriptor_48_e8_32s40r_e188_B24?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB}16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e37_v24?0^{__CFString=}8^{__CFString=}16ls32l8
+ ___block_descriptor_49_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_50_e8_32s40r_e231_B32?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}24ls32l8r40l8
+ ___block_descriptor_52_e37_v24?0^{__CFString=}8^{__CFString=}16l
+ ___block_descriptor_52_e5_v8?0l
+ ___block_descriptor_52_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_52_e8_32s_e188_B24?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB}16ls32l8
+ ___block_descriptor_56_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32r40r48r_e231_B32?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}24lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_57_e5_v8?0l
+ ___block_descriptor_60_e5_v8?0l
+ ___block_descriptor_64_e5_v8?0l
+ ___block_descriptor_64_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_64_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_68_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_68_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_72_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_76_e8_32s40bs_e188_B24?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB}16ls32l8s40l8
+ ___configStream_endpoint_processCategoryListReady_block_invoke
+ ___configureAndUnlockUSBHostInterfaces_block_invoke
+ ___destructor_8_s0_s8
+ ___genericMFi_appLaunch_RequestUserForAppLaunch_block_invoke
+ ___genericMFi_endpoint_destroy_block_invoke_2
+ ___genericMFi_endpoint_handleAuthStatusDidChange_block_invoke
+ ___genericMFi_endpoint_handleAuthStatusDidChange_block_invoke_2
+ ___iap2_hid_AccessoryHIDGetReportResponseHandler_block_invoke
+ ___iap2_hid_AccessoryHIDReportHandler_block_invoke
+ ___iap2_hid_StartHIDMsgHandler_block_invoke
+ ___iap2_mediaLibrary_startMediaLibraryInformationHandler_block_invoke
+ ___iap2_mediaLibrary_updateHandler_block_invoke
+ ___iap2_oobBtPairing2_accessoryInfoHandler_block_invoke
+ ___iap2_oobBtPairing2_statusHandler_block_invoke
+ ___iap2_oobBtPairing_accessoryInfoHandler_block_invoke
+ ___iap2_oobBtPairing_completionInfoHandler_block_invoke
+ ___iap2_power_registerForSleepNotification_block_invoke
+ ___iap2_power_sendPowerUpdate_block_invoke
+ ___iap2_power_stopPowerUpdatesHandler_block_invoke
+ ___iap2_sessionControl_cleanup_block_invoke
+ ___iap2_sessionControl_cleanup_block_invoke_2
+ ___iap2_sessionLog_sendOutgoingMessage_block_invoke
+ ___iap2_wifisharing_AccessoryWiFiConfigurationInformation_block_invoke
+ ___iap2_wifisharing_RequestWiFiInformation_block_invoke
+ ___mfi4Auth_endpoint_destroy_block_invoke_2
+ ___mfi4Auth_endpoint_firstUnlockHandler_block_invoke_2
+ ___oobPairing_endpoint_create_block_invoke
+ ___oobPairing_endpoint_destroy_block_invoke
+ ___oobPairing_endpoint_destroy_block_invoke_2
+ ___oobPairing_endpoint_processIncomingData_block_invoke
+ ___oobPairing_endpoint_processIncomingData_block_invoke_2
+ ___oobPairing_endpoint_publish_block_invoke_2
+ ___parseUSBHostHIDComponentIdentificationParams_block_invoke
+ ___platform_analytics2_connectionPassedAuthForProtocol_block_invoke
+ ___platform_analytics2_endpointAccessoryInfoDidChange_block_invoke
+ ___platform_analytics2_endpointWillBeDestroyed_block_invoke
+ ___platform_connectionInfo_beginUserKeyErase_block_invoke
+ ___platform_connectionInfo_beginVendorKeyErase_block_invoke
+ ___platform_connectionInfo_cancelUserKeyErase_block_invoke
+ ___platform_connectionInfo_cancelVendorKeyErase_block_invoke
+ ___platform_connectionInfo_checkConfigStreamCategoryListReady_block_invoke
+ ___platform_connectionInfo_continueUserKeyErase_block_invoke
+ ___platform_connectionInfo_continueVendorKeyErase_block_invoke
+ ___platform_connectionInfo_copyUserPrivateKey_block_invoke
+ ___platform_connectionInfo_getAccessoryUserName_block_invoke
+ ___platform_connectionInfo_getInterceptCountForEndpoint_block_invoke
+ ___platform_connectionInfo_getPairingStatus_block_invoke
+ ___platform_connectionInfo_getPrivateNvmKeyValues_block_invoke
+ ___platform_connectionInfo_getPublicNvmKeyValues_block_invoke
+ ___platform_connectionInfo_provisionPairing_block_invoke
+ ___platform_connectionInfo_resetPairing_block_invoke
+ ___platform_connectionInfo_sendDataForEndpoint_block_invoke
+ ___platform_connectionInfo_setAccessoryUserName_block_invoke
+ ___platform_connectionInfo_setPrivateNvmKeyValues_block_invoke
+ ___platform_connectionInfo_setPublicNvmKeyValues_block_invoke
+ ___platform_connectionInfo_setupInterceptForEndpoint_block_invoke
+ ___platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID_withSnapshotInfo_block_invoke
+ ___processPowerSourceUpdate_block_invoke
+ ___qiAuth_endpoint_destroy_block_invoke_2
+ ___requestAuthorization_block_invoke_3
+ ___startFeatureFromDevice_block_invoke_2
+ ___t56_endpoint_destroy_block_invoke
+ ___t56_endpoint_destroy_block_invoke_2
+ __acc_connection2_addToDictionaryProperty_block_invoke
+ __acc_connection2_appendToArrayProperty_block_invoke
+ __acc_connection2_connectionInfo_accessoryConnectionInfoPropertyChanged
+ __acc_connection2_destroy_block_invoke
+ __acc_connection2_getDurationMS_internal
+ __acc_connection2_invokeFeatureHandlerWithResult_asyncImpl
+ __acc_connection2_mapAccessoryInfo_internal_block_invoke
+ __acc_connection2_notifications_propertiesDidChangeForConnection
+ __acc_connection2_performBlockForEndpoint_internal
+ __acc_connection2_performSyncWithCleanup_block_invoke
+ __acc_connection2_removeAllEndpoints_internal
+ __acc_connection2_removeProperty_block_invoke
+ __acc_connection2_setAuthStatus_internal_block_invoke
+ __acc_connection2_setDataOutHandler_internal
+ __acc_connection2_setProperties_block_invoke
+ __acc_connection2_setSupervisedTransportsRestricted_block_invoke
+ __acc_endpoint2_analytics_endpointAccessoryInfoDidChange
+ __acc_endpoint2_connectionInfo_accessoryEndpointInfoPropertyChanged
+ __acc_endpoint2_notifications_propertiesDidChangeForEndpointUUID
+ __acc_manager2_checkForInductiveCTA_block_invoke
+ __acc_manager2_checkForWirelessCTA_block_invoke
+ __acc_manager2_checkForWirelessCTA_block_invoke_3
+ __acc_manager2_copyAdapterForConnection_internal
+ __acc_manager2_copyAllConnectionUUIDs_block_invoke
+ __acc_manager2_copyConnectionsThroughAdapter_internal
+ __acc_manager2_createAllSnapshotInfoAsync_block_invoke
+ __acc_manager2_createSnapshotInfoAsync
+ __acc_manager2_getConnectionEndpointStruct_internal
+ __acc_manager2_performBlockForConnectionEndpoint_asyncWithCleanup_block_invoke
+ __acc_manager2_performBlockForConnectionEndpoint_block_invoke
+ __acc_manager2_removeConnection_block_invoke
+ __acc_manager2_sharedManager_block_invoke
+ __configStream_endpoint_cleanupSession
+ __createConfigStreamParamsArray
+ __dumpHex
+ __emitLogString
+ __emitLogWithData
+ __gDeviceUUID
+ __genericMFi_endpoint_processPropertiesDidChange
+ __getAuthInfoFromSnapshotAuthInfo
+ __getBestEndpointInfoForAuthEvent
+ __getDurationMSFromTimestamp
+ __getEndpointProtocol_manager2
+ __handleEAPowerSourceChange_manager2
+ __iap2_hid_StartHIDMsgHandler_block_invoke
+ __mfi4Auth_featureHandler_beginUserKeyErase
+ __mfi4Auth_featureHandler_beginVendorKeyErase
+ __mfi4Auth_featureHandler_cancelUserKeyErase
+ __mfi4Auth_featureHandler_cancelVendorKeyErase
+ __mfi4Auth_featureHandler_continueUserKeyErase
+ __mfi4Auth_featureHandler_continueVendorKeyErase
+ __mfi4Auth_featureHandler_copyUserPrivateKey
+ __mfi4Auth_featureHandler_getAccessoryUserName
+ __mfi4Auth_featureHandler_getPairingStatus
+ __mfi4Auth_featureHandler_getPrivateNvmKeyValues
+ __mfi4Auth_featureHandler_getPublicNvmKeyValues
+ __mfi4Auth_featureHandler_provisionPairing
+ __mfi4Auth_featureHandler_resetPairing
+ __mfi4Auth_featureHandler_setAccessoryUserName
+ __mfi4Auth_featureHandler_setPrivateNvmKeyValues
+ __mfi4Auth_featureHandler_setPublicNvmKeyValues
+ __platform_analytics2_connectionPassedAuthForProtocol_block_invoke
+ __platform_analytics2_endpointAccessoryInfoDidChange_block_invoke
+ __platform_analytics2_endpointWillBeDestroyed_block_invoke
+ __platform_connectionInfo_addAuthInfoFromSnapshot
+ __platform_connectionInfo_checkConfigStreamCategoryListReady_block_invoke
+ __platform_connectionInfo_sendDataForEndpoint_block_invoke
+ __platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID_withSnapshotInfo_block_invoke
+ __processAccessoryPowerUpdate
+ __processPowerUpdates
+ __qiAuth_endpoint_cancelPublishDelayTimer
+ __safePercentEncode
+ __t56_endpoint_cancelPublishDelayTimer
+ _acc_authInfo_copyAuthInfoDictionary
+ _acc_connection2_addEndpoint_internal
+ _acc_connection2_addToDictionaryProperty
+ _acc_connection2_addToDictionaryPropertyForEndpoint
+ _acc_connection2_analytics_connectionAuthUnsuccessfulForProtocol
+ _acc_connection2_analytics_connectionPassedAuth
+ _acc_connection2_analytics_connectionPassedAuthForProtocol
+ _acc_connection2_analytics_iap2_featuresSupportedDidChange
+ _acc_connection2_appendToArrayProperty
+ _acc_connection2_appendToArrayPropertyForEndpoint
+ _acc_connection2_containsEndpoint_internal
+ _acc_connection2_copyAccessoryInfoDictionary
+ _acc_connection2_copyAccessoryInfoDictionary_internal
+ _acc_connection2_copyAllEndpointsSnapshotInfo_internal
+ _acc_connection2_copyDescription
+ _acc_connection2_copyDescription_internal
+ _acc_connection2_copyEndpointSnapshotInfo
+ _acc_connection2_copyEndpointSnapshotInfo_internal
+ _acc_connection2_copyEndpointUUIDs
+ _acc_connection2_copyIdentifier
+ _acc_connection2_copyIdentifierForEndpoint
+ _acc_connection2_copyIdentifierForEndpoint_internal
+ _acc_connection2_copyProperties
+ _acc_connection2_copyPropertiesForEndpoint
+ _acc_connection2_copyProperty
+ _acc_connection2_copyProperty_internal
+ _acc_connection2_copySnapshotInfo
+ _acc_connection2_copySnapshotInfo_internal
+ _acc_connection2_copyUUID
+ _acc_connection2_create
+ _acc_connection2_createEndpoint
+ _acc_connection2_createEndpointSnapshotInfo_internal
+ _acc_connection2_createEndpoint_internal
+ _acc_connection2_createSnapshotInfo
+ _acc_connection2_createSnapshotInfoAsync
+ _acc_connection2_createSnapshotInfo_internal
+ _acc_connection2_createWithUUID
+ _acc_connection2_destroy
+ _acc_connection2_destroyEndpoint
+ _acc_connection2_endpointIterateForConnection
+ _acc_connection2_endpointIterateForConnection_internal
+ _acc_connection2_getAccessoryInfo_internal
+ _acc_connection2_getAdapterPID_internal
+ _acc_connection2_getAdapterVID_internal
+ _acc_connection2_getAuthInfo
+ _acc_connection2_getAuthInfo_internal
+ _acc_connection2_getAuthStatus
+ _acc_connection2_getAuthStatus_internal
+ _acc_connection2_getEndpointStruct
+ _acc_connection2_getEndpointStruct_internal
+ _acc_connection2_getNumEndpoints_internal
+ _acc_connection2_getPairingStatus
+ _acc_connection2_getProtocolForEndpoint
+ _acc_connection2_getProtocolForEndpoint_internal
+ _acc_connection2_getSupervisedTransportsRestricted_internal
+ _acc_connection2_getTransportTypeForEndpoint
+ _acc_connection2_getTransportTypeForEndpoint_internal
+ _acc_connection2_getType
+ _acc_connection2_getTypeStringFromType
+ _acc_connection2_getType_internal
+ _acc_connection2_invokeFeatureHandler
+ _acc_connection2_invokeFeatureHandlerWithResult_asyncImpl
+ _acc_connection2_invokeFeatureHandlerWithResult_asyncWithAssert
+ _acc_connection2_invokeFeatureHandler_asyncWithAssert
+ _acc_connection2_isAuthenticated
+ _acc_connection2_isAuthenticatedForAppMatchLaunch
+ _acc_connection2_isAuthenticatedForAppMatchLaunch_internal
+ _acc_connection2_isAuthenticatedForInductivePowerIn
+ _acc_connection2_isAuthenticated_internal
+ _acc_connection2_isConnectedThroughAdapter_internal
+ _acc_connection2_isPublished_internal
+ _acc_connection2_mapAccessoryInfo
+ _acc_connection2_mapAccessoryInfo_internal
+ _acc_connection2_performAsync
+ _acc_connection2_performAsyncWithCleanup
+ _acc_connection2_performBlockForConnection
+ _acc_connection2_performBlockForEndpoint
+ _acc_connection2_performBlockForEndpoint_asyncWithCleanup
+ _acc_connection2_performSyncWithCleanup
+ _acc_connection2_processIncomingDataForEndpoint
+ _acc_connection2_processIncomingDataForEndpoint_internal
+ _acc_connection2_processOutgoingSecureTunnelDataForEndpointClient_internal
+ _acc_connection2_publish
+ _acc_connection2_publish_internal
+ _acc_connection2_removeEndpoint_internal
+ _acc_connection2_removeProperty
+ _acc_connection2_removePropertyForEndpoint
+ _acc_connection2_sendDataOut_internal
+ _acc_connection2_setAccessoryInfoForEndpoint
+ _acc_connection2_setAccessoryInfoOverridesWithDictionaryForEndpoint
+ _acc_connection2_setAuthCertData
+ _acc_connection2_setAuthCertData_internal
+ _acc_connection2_setAuthStatus
+ _acc_connection2_setAuthStatus_internal
+ _acc_connection2_setPairingStatus
+ _acc_connection2_setProperties
+ _acc_connection2_setPropertiesForEndpoint
+ _acc_connection2_setProperty
+ _acc_connection2_setProperty_internal
+ _acc_connection2_setSupervisedTransportsRestricted
+ _acc_connection2_updateAcccessoryInfoIfNeeded
+ _acc_endpoint2_addToDictionaryProperty
+ _acc_endpoint2_appendToArrayProperty
+ _acc_endpoint2_clearAccessoryInfo
+ _acc_endpoint2_copyDescription
+ _acc_endpoint2_copyIdentifier
+ _acc_endpoint2_copyParentEndpointUUID
+ _acc_endpoint2_copyProperties
+ _acc_endpoint2_copyProperty
+ _acc_endpoint2_copySnapshotInfo
+ _acc_endpoint2_createSnapshotInfo
+ _acc_endpoint2_createWithUUID
+ _acc_endpoint2_destroy
+ _acc_endpoint2_externalAccessory_addEAAccessoryForPrimaryEndpoint
+ _acc_endpoint2_externalAccessory_handleIncomingEADataFromAccessoryForEndpointUUID
+ _acc_endpoint2_externalAccessory_removeEAAccessoryForPrimaryEndpoint
+ _acc_endpoint2_externalAccessory_updateEAAccessoryInfoForEndpointWithUUID
+ _acc_endpoint2_getAccessoryInfo
+ _acc_endpoint2_getParentConnection
+ _acc_endpoint2_getProtocol
+ _acc_endpoint2_getProtocolTypeStringWithProtocol
+ _acc_endpoint2_getTransportType
+ _acc_endpoint2_getTransportTypeString
+ _acc_endpoint2_getTransportTypeStringWithTransportType
+ _acc_endpoint2_invokeFeatureHandler
+ _acc_endpoint2_invokeFeatureHandlerWithResult
+ _acc_endpoint2_isPublished
+ _acc_endpoint2_isTransportRestricted
+ _acc_endpoint2_isWireless
+ _acc_endpoint2_processIncomingData
+ _acc_endpoint2_processOutgoingSecureTunnelDataForClient
+ _acc_endpoint2_publish
+ _acc_endpoint2_removeProperty
+ _acc_endpoint2_sendOutgoingData
+ _acc_endpoint2_setAccessoryInfo
+ _acc_endpoint2_setAccessoryInfoOverridesWithDictionary
+ _acc_endpoint2_setAccessoryInfoWithDictionary
+ _acc_endpoint2_setEndpointSecureTunnelDataReceiveTypeHandler
+ _acc_endpoint2_setParentEndpointUUID
+ _acc_endpoint2_setProperties
+ _acc_endpoint2_setProperty
+ _acc_endpoint2_supervisedTransportsRestrictedDidChange
+ _acc_manager2_addToDictionaryPropertyForConnection
+ _acc_manager2_addToDictionaryPropertyForEndpoint
+ _acc_manager2_appendToArrayPropertyForConnection
+ _acc_manager2_appendToArrayPropertyForEndpoint
+ _acc_manager2_checkForInductiveCTA
+ _acc_manager2_checkForWirelessCTA
+ _acc_manager2_copyAccessoryInfoDictionaryForConnection
+ _acc_manager2_copyAdapterForConnection_internal
+ _acc_manager2_copyAllConnectionUUIDs
+ _acc_manager2_copyAuthCertDataForConnection
+ _acc_manager2_copyCertCapabilitiesForConnection
+ _acc_manager2_copyCertSerialForConnection
+ _acc_manager2_copyCertSerialStringForConnection
+ _acc_manager2_copyConnectionSnapshotInfo
+ _acc_manager2_copyConnectionUUIDFromEndpointUUID
+ _acc_manager2_copyConnectionsThroughAdapter_internal
+ _acc_manager2_copyEndpointIdentifier
+ _acc_manager2_copyEndpointSnapshotInfo
+ _acc_manager2_copyEndpointUUIDsForConnection
+ _acc_manager2_copyIdentifierForConnection
+ _acc_manager2_copyPropertiesForConnection
+ _acc_manager2_copyPropertiesForEndpoint
+ _acc_manager2_createAllSnapshotInfoAsync
+ _acc_manager2_createConnection
+ _acc_manager2_createConnectionSnapshotInfo
+ _acc_manager2_createEndpointForConnection
+ _acc_manager2_createEndpointSnapshotInfo
+ _acc_manager2_createSnapshotInfoAsync
+ _acc_manager2_getAuthStatusForConnection
+ _acc_manager2_getConnectionStruct_internal
+ _acc_manager2_getConnectionType
+ _acc_manager2_getConnectionTypeStringFromType
+ _acc_manager2_getEndpointProtocol
+ _acc_manager2_getEndpointTransportType
+ _acc_manager2_getFeatureHandlerWithResult_internal
+ _acc_manager2_getFeatureHandler_internal
+ _acc_manager2_getProtocolStringFromProtocol
+ _acc_manager2_getTransportTypeStringFromTransportType
+ _acc_manager2_invokeFeatureHandler
+ _acc_manager2_invokeFeatureHandlerWithResult
+ _acc_manager2_isConnectionAuthenticated
+ _acc_manager2_isConnectionAuthenticatedForAppMatchLaunch
+ _acc_manager2_isWirelessFromEndpointSnapshotInfo
+ _acc_manager2_iterateAllConnections_internal
+ _acc_manager2_performAsync
+ _acc_manager2_performBlockForConnection
+ _acc_manager2_performBlockForConnectionEndpoint
+ _acc_manager2_performBlockForConnectionEndpoint_asyncWithCleanup
+ _acc_manager2_performBlockForConnection_internal
+ _acc_manager2_performPlatformWorkAsync
+ _acc_manager2_performPlatformWorkForConnectionEndpointAsync
+ _acc_manager2_performSync
+ _acc_manager2_processIncomingDataForConnectionEndpoint
+ _acc_manager2_publishConnection
+ _acc_manager2_removeConnection
+ _acc_manager2_removeConnectionEndpoint
+ _acc_manager2_removePropertyForConnection
+ _acc_manager2_removePropertyForEndpoint
+ _acc_manager2_sendOutgoingDataForConnectionEndpoint
+ _acc_manager2_setAccessoryInfoForEndpoint
+ _acc_manager2_setAccessoryInfoOverridesWithDictionaryForEndpoint
+ _acc_manager2_setAdapterPropertiesOnConnectionsAsync
+ _acc_manager2_setAuthCertDataForConnection
+ _acc_manager2_setAuthStatusForConnection
+ _acc_manager2_setAuthStatusWithCertDataForConnection
+ _acc_manager2_setPropertiesForConnection
+ _acc_manager2_setPropertiesForEndpoint
+ _acc_manager2_setPropertiesOnConnectionsThroughAdapterConnectionAsync
+ _acc_manager2_setPropertyForConnection
+ _acc_manager2_setSupervisedTransportsRestricted
+ _acc_manager2_sharedManager
+ _acc_manager2_sharedManagerPlatformWorkQueue
+ _acc_manager2_sharedManagerQueue
+ _acc_platform_packetLogging_logAccAuthProtocolMsgForEndpoint
+ _acc_platform_packetLogging_logDataForEndpoint
+ _acc_platform_packetLogging_logEADataForEndpoint
+ _acc_platform_packetLogging_logEventForEndpoint
+ _acc_platform_packetLogging_logEventVAForEndpoint
+ _acc_platform_packetLogging_logGenericMFiTLVForEndpoint
+ _acc_platform_packetLogging_logMFi4AuthProtocolMsgForEndpoint
+ _acc_platform_packetLogging_logParsedDataForEndpoint
+ _acc_platform_packetLogging_logQiAuthMsgForEndpoint
+ _acc_platform_packetLogging_logSNTPTimeSyncMsgForEndpoint
+ _acc_platform_packetLogging_logT56MsgForEndpoint
+ _acc_platform_packetLogging_logiAP2PacketForEndpoint
+ _acc_protocolEndpoint_performAsync
+ _acc_protocolEndpoint_performSync
+ _configStream_endpoint_cleanupSession
+ _eACCAuthInfo_AuthVersion
+ _eACCAuthInfo_CTAAllowed
+ _eACCAuthInfo_CertCapabilities
+ _eACCAuthInfo_CertData
+ _eACCAuthInfo_CertSerial
+ _eACCAuthInfo_CertSerialString
+ _eACCAuthInfo_Status
+ _eACCAuthInfo_V2CertClass
+ _emitLogString
+ _emitLogWithData
+ _genericMFi_endpoint_processPropertiesDidChange
+ _getBestEndpointInfoForAuthEvent
+ _initReferenceDate.onceToken
+ _isPowerDuringSleepForApplePencil
+ _kCFACCUserDefaultsKey_OverrideMPPAuthSupported
+ _kCFAllocatorMalloc
+ _kCFConnectionEndpoint_SnapshotInfo_AccInfo
+ _kCFConnectionEndpoint_SnapshotInfo_AdapterPID
+ _kCFConnectionEndpoint_SnapshotInfo_AdapterVID
+ _kCFConnectionEndpoint_SnapshotInfo_AppMatchProtocols
+ _kCFConnectionEndpoint_SnapshotInfo_AppMatchTeamIDs
+ _kCFConnectionEndpoint_SnapshotInfo_AuthInfo
+ _kCFConnectionEndpoint_SnapshotInfo_CarPlayCapable
+ _kCFConnectionEndpoint_SnapshotInfo_CertData
+ _kCFConnectionEndpoint_SnapshotInfo_CertSerial
+ _kCFConnectionEndpoint_SnapshotInfo_ConnectionType
+ _kCFConnectionEndpoint_SnapshotInfo_ConnectionUUID
+ _kCFConnectionEndpoint_SnapshotInfo_CreateTimestampMs
+ _kCFConnectionEndpoint_SnapshotInfo_EAProtocols
+ _kCFConnectionEndpoint_SnapshotInfo_EndpointUUID
+ _kCFConnectionEndpoint_SnapshotInfo_Endpoints
+ _kCFConnectionEndpoint_SnapshotInfo_FeaturesBitMask
+ _kCFConnectionEndpoint_SnapshotInfo_Identifier
+ _kCFConnectionEndpoint_SnapshotInfo_IsConnectedThroughAdapter
+ _kCFConnectionEndpoint_SnapshotInfo_MultipleEASessionsCapable
+ _kCFConnectionEndpoint_SnapshotInfo_ParentConnection
+ _kCFConnectionEndpoint_SnapshotInfo_PreferredApp
+ _kCFConnectionEndpoint_SnapshotInfo_Properties
+ _kCFConnectionEndpoint_SnapshotInfo_ProtocolType
+ _kCFConnectionEndpoint_SnapshotInfo_ThemeAssetsCapable
+ _kCFConnectionEndpoint_SnapshotInfo_TransportType
+ _kCFConnectionEndpoint_SnapshotInfo_USBCarPlayCapable
+ _kCFConnectionEndpoint_SnapshotInfo_VehicleInfo
+ _kCFConnectionEndpoint_SnapshotInfo_WirelessCarPlayCapable
+ _kCFWirelessCTAConnectionUUID2
+ _kCFWirelessCTAIdentifier2
+ _kCFWirelessCTAOOBPairingData2
+ _kConnectionEndpoint_SnapshotInfo_AccInfo
+ _kConnectionEndpoint_SnapshotInfo_AdapterPID
+ _kConnectionEndpoint_SnapshotInfo_AdapterVID
+ _kConnectionEndpoint_SnapshotInfo_AppMatchProtocols
+ _kConnectionEndpoint_SnapshotInfo_AppMatchTeamIDs
+ _kConnectionEndpoint_SnapshotInfo_AuthInfo
+ _kConnectionEndpoint_SnapshotInfo_CarPlayCapable
+ _kConnectionEndpoint_SnapshotInfo_CertData
+ _kConnectionEndpoint_SnapshotInfo_CertSerial
+ _kConnectionEndpoint_SnapshotInfo_ConnectionType
+ _kConnectionEndpoint_SnapshotInfo_ConnectionUUID
+ _kConnectionEndpoint_SnapshotInfo_CreateTimestampMs
+ _kConnectionEndpoint_SnapshotInfo_EAProtocols
+ _kConnectionEndpoint_SnapshotInfo_EndpointUUID
+ _kConnectionEndpoint_SnapshotInfo_Endpoints
+ _kConnectionEndpoint_SnapshotInfo_FeaturesBitMask
+ _kConnectionEndpoint_SnapshotInfo_Identifier
+ _kConnectionEndpoint_SnapshotInfo_IsConnectedThroughAdapter
+ _kConnectionEndpoint_SnapshotInfo_MultipleEASessionsCapable
+ _kConnectionEndpoint_SnapshotInfo_ParentConnection
+ _kConnectionEndpoint_SnapshotInfo_PreferredApp
+ _kConnectionEndpoint_SnapshotInfo_Properties
+ _kConnectionEndpoint_SnapshotInfo_ProtocolType
+ _kConnectionEndpoint_SnapshotInfo_ThemeAssetsCapable
+ _kConnectionEndpoint_SnapshotInfo_TransportType
+ _kConnectionEndpoint_SnapshotInfo_USBCarPlayCapable
+ _kConnectionEndpoint_SnapshotInfo_VehicleInfo
+ _kConnectionEndpoint_SnapshotInfo_WirelessCarPlayCapable
+ _kMFi4AuthConnectionInfoFeatureHandlerWithResultCount
+ _kMFi4AuthConnectionInfoFeatureHandlerWithResultEntries
+ _mfi4Auth_protocol_initMessage_RequestNVMAuthFinish
+ _objc_msgSend$URLQueryAllowedCharacterSet
+ _objc_msgSend$_addAccessoryInfoFromSnapshot:connectionSnapshot:
+ _objc_msgSend$_addEAProtocolPrimaryEndpointInfoFromSnapshot:connectionSnapshot:
+ _objc_msgSend$_addEAProtocolsForEAEndpointsFromSnapshots:connectionUUID:
+ _objc_msgSend$_addGenericMFiEAProtocolsFromSnapshot:connectionUUID:
+ _objc_msgSend$_addSleepAssertionForUUID:withConnectionType:
+ _objc_msgSend$_addiAP2AuthInfoFromSnapshot:
+ _objc_msgSend$_addiAP2EAProtocolsFromSnapshot:connectionUUID:
+ _objc_msgSend$_addiAP2IdentificationInfoFromSnapshot:
+ _objc_msgSend$_addiAP2VehicleInfoFromSnapshot:
+ _objc_msgSend$_generateIAPDPortTypeForDictionary:withConnectionType:transportType:
+ _objc_msgSend$_nativeUSBEndpointUUIDForProtocolIdentifierFromSnapshot:connectionUUID:
+ _objc_msgSend$accInfo
+ _objc_msgSend$adapterPID
+ _objc_msgSend$adapterVID
+ _objc_msgSend$addAccessoryForEndpointUID:andModelNumber:andBitmask:andOldBitmask:
+ _objc_msgSend$addSleepAssertionForUUID:withConnectionType:
+ _objc_msgSend$appMatchProtocols
+ _objc_msgSend$appMatchTeamIDs
+ _objc_msgSend$authInfo
+ _objc_msgSend$carPlayCapable
+ _objc_msgSend$certData
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$connectionType
+ _objc_msgSend$connectionUUID
+ _objc_msgSend$createTimestampMs
+ _objc_msgSend$distantPast
+ _objc_msgSend$eaProtocols
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$featuresBitMask
+ _objc_msgSend$iapdAccessoryArrivedWithSnapshotInfo:endpointUUID:protocol:transportType:connectionType:
+ _objc_msgSend$iapdAccessoryProcessIncomingDataWithSnapshotInfo:transportType:protocol:incomingData:
+ _objc_msgSend$initWithEndpointUID:andModelNumber:andBitmask:andOldBitmask:
+ _objc_msgSend$isConnectedThroughAdapter
+ _objc_msgSend$isModelNumberConnected:
+ _objc_msgSend$multipleEASessionsCapable
+ _objc_msgSend$pConnection
+ _objc_msgSend$preferredApp
+ _objc_msgSend$properties
+ _objc_msgSend$removeCharactersInString:
+ _objc_msgSend$setModelNumber:
+ _objc_msgSend$setPConnection:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$themeAssetsCapable
+ _objc_msgSend$transportType
+ _objc_msgSend$unionSet:
+ _objc_msgSend$usbCarPlayCapable
+ _objc_msgSend$vehicleInfo
+ _objc_msgSend$wirelessCarPlayCapable
+ _objc_retain_x7
+ _parseRoadSignParameter
+ _platform_analytics2_connectionAuthUnsuccessful
+ _platform_analytics2_connectionAuthUnsuccessfulForProtocol
+ _platform_analytics2_connectionPassedAuth
+ _platform_analytics2_connectionPassedAuthForProtocol
+ _platform_analytics2_connectionWillBeDestroyed
+ _platform_analytics2_connectionWillBePublished
+ _platform_analytics2_endpointAccessoryInfoDidChange
+ _platform_analytics2_endpointProtocolDidChange
+ _platform_analytics2_endpointWillBeDestroyed
+ _platform_analytics2_endpointWillBePublished
+ _platform_analytics2_iap2_featuresSupportedDidChange
+ _platform_analytics_availableCurrentNegotiated_withSnapshotInfo
+ _platform_connectionInfo_accessoryConnectionAttachedWithSnapshotInfo
+ _platform_connectionInfo_accessoryConnectionInfoPropertyChangedWithSnapshotInfo
+ _platform_connectionInfo_accessoryEndpointAttachedWithSnapshotInfo
+ _platform_connectionInfo_accessoryEndpointInfoPropertyChangedWithSnapshotInfo
+ _platform_connectionInfo_accessoryEndpointProtocolUpdateWithSnapshotInfo
+ _platform_externalAccessory_EASessionOpened_manager2.onceToken
+ _platform_externalAccessory_copyMutableEADataFromAppForSessionUUID
+ _platform_iapd_bridge_accessory_connected_withInfo
+ _platform_iapd_bridge_accessory_processIncomingData_withInfo
+ _platform_nowPlaying_playbackQueueListChanged
+ _platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID_withSnapshotInfo
+ _platform_power_setAvailableCurrent_withSnapshotInfo
+ _platform_sleepAssertion_create_withInfo
+ _platform_systemInfo_copyDeviceUUID
+ _platform_systemInfo_resetDeviceUUID
+ _platform_wifisharing_accessory_wifi_configuration_information_withSnapshotInfo
+ _qiAuth_endpoint_sendOutgoingDataCF
+ accFeatureHandlers_invokeHandler
+ acc_connection2.m
+ acc_connection2_getPairingStatus
+ acc_connection2_mapAccessoryInfo_internal
+ acc_connection2_performAsyncWithCleanup
+ acc_connection2_performSyncWithCleanup
+ acc_connection2_publish_internal
+ acc_connection2_setAuthStatus_internal
+ acc_connection2_setPairingStatus
+ acc_connectionEndpoint_snapshotInfoKeys.m
+ acc_endpoint2.m
+ acc_endpoint2_invokeFeatureHandlerWithResult
+ acc_endpoint2_sendOutgoingData
+ acc_manager2.m
+ acc_manager2_connection.m
+ acc_manager2_copyAccessoryInfoDictionaryForConnection
+ acc_manager2_copyAuthCertDataForConnection
+ acc_manager2_copyCertCapabilitiesForConnection
+ acc_manager2_copyCertSerialForConnection
+ acc_manager2_copyCertSerialStringForConnection
+ acc_manager2_copyConnectionSnapshotInfo
+ acc_manager2_copyConnectionUUIDFromEndpointUUID
+ acc_manager2_copyEndpointIdentifier
+ acc_manager2_copyEndpointSnapshotInfo
+ acc_manager2_copyEndpointUUIDsForConnection
+ acc_manager2_copyIdentifierForConnection
+ acc_manager2_copyPropertiesForConnection
+ acc_manager2_copyPropertiesForEndpoint
+ acc_manager2_createConnection
+ acc_manager2_createEndpointForConnection
+ acc_manager2_cta.m
+ acc_manager2_endpoint.m
+ acc_manager2_featureHandler.m
+ acc_manager2_getAuthStatusForConnection
+ acc_manager2_getConnectionType
+ acc_manager2_getConnectionTypeStringFromType
+ acc_manager2_getEndpointProtocol
+ acc_manager2_getEndpointTransportType
+ acc_manager2_getProtocolStringFromProtocol
+ acc_manager2_getTransportTypeStringFromTransportType
+ acc_manager2_helper.m
+ acc_manager2_invokeFeatureHandler
+ acc_manager2_invokeFeatureHandlerWithResult
+ acc_manager2_isConnectionAuthenticated
+ acc_manager2_isConnectionAuthenticatedForAppMatchLaunch
+ acc_manager2_iterateAllConnections_internal
+ acc_manager2_performBlockForConnection
+ acc_manager2_performBlockForConnectionEndpoint
+ acc_manager2_performBlockForConnectionEndpoint_asyncWithCleanup
+ acc_manager2_performBlockForConnection_internal
+ acc_manager2_removeConnectionEndpoint
+ acc_manager2_setPropertiesForConnection
+ acc_manager2_setPropertiesForEndpoint
+ acc_manager2_setPropertyForConnection
+ acc_manager2_setSupervisedTransportsRestricted
+ acc_manager2_sharedManager
+ acc_manager2_sharedManagerPlatformWorkQueue
+ acc_manager2_sharedManagerQueue
+ acc_platform_analytics2.m
+ acc_platform_packetLogging_logAccAuthProtocolMsgForEndpoint
+ acc_platform_packetLogging_logDataForEndpoint
+ acc_platform_packetLogging_logEADataForEndpoint
+ acc_platform_packetLogging_logEventVAForEndpoint
+ acc_platform_packetLogging_logGenericMFiTLVForEndpoint
+ acc_platform_packetLogging_logMFi4AuthProtocolMsgForEndpoint
+ acc_platform_packetLogging_logParsedDataForEndpoint
+ acc_platform_packetLogging_logQiAuthMsgForEndpoint
+ acc_platform_packetLogging_logSNTPTimeSyncMsgForEndpoint
+ acc_platform_packetLogging_logT56MsgForEndpoint
+ acc_platform_packetLogging_logiAP2PacketForEndpoint
+ acc_protocolEndpoint_performAsync
+ acc_protocolEndpoint_performSync
+ genericMFi_util_SetOrRemoveProperty
+ mfi4Auth_connectionInfo_feature_handlers.m
+ openLogFileWriter
+ platform_connectionInfo_checkConfigStreamCategoryListReady
+ platform_connectionInfo_getPairingStatus
+ platform_connectionInfo_sendDataForEndpoint
+ platform_externalAccessory_sendOutgoingEADataFromClient
+ platform_iapd_bridge_accessory_connected_withInfo
+ platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID_withSnapshotInfo
+ platform_power_sendEAPowerUpdate
+ platform_sleepAssertion_create_withInfo
+ platform_wifisharing_accessory_wifi_configuration_information_withSnapshotInfo
+ qiAuth_endpoint_sendOutgoingDataCF
- -[ACCPlatformPowerInfo initWithEndpointUID:andBitmask:andOldBitmask:]
- -[ACCPlatformPowerManager addAccessoryForEndpointUID:andBitmask:andOldBitmask:]
- -[ACCPlatformSleepAssertionManager _addSleepAssertionForUUID:]
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_connection.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_endpoint.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_manager_objc.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_platform_analytics.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccm-decrypt-4a9991a1dabff1ec88b854bba177ca59.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccm-encrypt-926c7c8eed6aa774dde7a87eca6ef6b8.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_add-b88bd8b451a6ac10f5ed15c8dcf643a1.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_add-e2d4021dab97e90b3ab60b61d36c2778.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_cmp-4cb81a2fc48f025948b06c14bfe09041.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_mul-5f62a3c49b088d908991494029c23e4d.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_mul-e7d5da0e673878f664a0dc0c6140339d.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_n-4817c88bfc24ac4e87840a930f1f9082.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_set-fcc48202b11d62f2295ba8aca4a58bbf.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_shift_right-7c249877612c728b0d30fb85acc9ed74.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_shift_right-ed78de4767bd3f6b493403088186a497.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_sub-45c1f96350c7c7a6a494edcfd1d2faf1.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_sub-d5b043df232bae2ad26bed790cc691f2.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(ccn_sub1-e0ae5cc4d90af5a3630370c3cd0f60c2.o)
- GCC_except_table14
- GCC_except_table19
- GCC_except_table35
- _CFDictionaryApplierFunction_addKeyToMutableSet
- _CFDictionaryGetKeys
- _CFSetApplierFunction_removeValueFromMutableDictionary
- _CFSetCreateCopy
- _MGGetStringAnswer
- __102-[ACCTransportPluginManager setAuthenticationStatus:andCertificateData:authCTA:forConnectionWithUUID:]_block_invoke
- __61-[ACCTransportServerRemote setConnectionAuthenticated:state:]_block_invoke
- __62-[ACCPlatformSleepAssertionManager _addSleepAssertionForUUID:]_block_invoke
- __63-[ACCTransportPluginManager setProperties:forEndpointWithUUID:]_block_invoke
- __65-[ACCTransportPluginManager setProperties:forConnectionWithUUID:]_block_invoke
- __66-[ACCTransportPluginManager setAccessoryInfo:forEndpointWithUUID:]_block_invoke
- __68-[ACCTransportServerRemote identifierForEndpointWithUUID:withReply:]_block_invoke
- __68-[ACCTransportServerRemote propertiesForEndpointWithUUID:withReply:]_block_invoke
- __68-[PlatformIAPDBridge _handleAuthenticationState:forPortID:certData:]_block_invoke_2
- __70-[ACCTransportServerRemote identifierForConnectionWithUUID:withReply:]_block_invoke
- __70-[ACCTransportServerRemote propertiesForConnectionWithUUID:withReply:]_block_invoke
- __71-[ACCTransportServerRemote isConnectionAuthenticatedForUUID:withReply:]_block_invoke
- __72-[ACCTransportServerRemote setProperties:forEndpointWithUUID:withReply:]_block_invoke
- __73-[ACCTransportServerRemote accessoryInfoForConnectionWithUUID:withReply:]_block_invoke
- __73-[ACCTransportServerRemote removeProperty:forEndpointWithUUID:withReply:]_block_invoke
- __74-[ACCTransportServerRemote setProperties:forConnectionWithUUID:withReply:]_block_invoke
- __75-[ACCTransportServerRemote removeProperty:forConnectionWithUUID:withReply:]_block_invoke
- __75-[ACCTransportServerRemote setAccessoryInfo:forEndpointWithUUID:withReply:]_block_invoke
- __79-[ACCTransportServerRemote authStatusForConnectionWithUUID:authType:withReply:]_block_invoke
- __85-[ACCTransportPluginManager setSupervisedTransportsRestricted:forConnectionWithUUID:]_block_invoke
- __87-[ACCTransportServerRemote appendToArrayProperty:values:forEndpointWithUUID:withReply:]_block_invoke
- __89-[ACCTransportServerRemote addToDictionaryProperty:values:forEndpointWithUUID:withReply:]_block_invoke
- __89-[ACCTransportServerRemote appendToArrayProperty:values:forConnectionWithUUID:withReply:]_block_invoke
- __91-[ACCTransportServerRemote addToDictionaryProperty:values:forConnectionWithUUID:withReply:]_block_invoke
- __CFDictionaryApplierFunction_countEAServiceEndpoints
- __CFDictionaryApplierFunction_findEAServiceEndpoint
- __CFDictionaryApplierFunction_findInductiveAuthEndpoint
- __CFDictionaryApplierFunction_findInternalInfoEndpoint
- __CFDictionaryApplierFunction_findiAP2Endpoint
- __CFDictionaryApplierFunction_findiAPEndpoint
- ___102-[ACCTransportPluginManager setAuthenticationStatus:andCertificateData:authCTA:forConnectionWithUUID:]_block_invoke
- ___57-[ACCTransportPluginManager protocolForEndpointWithUUID:]_block_invoke
- ___59-[ACCTransportPluginManager identifierForEndpointWithUUID:]_block_invoke
- ___59-[ACCTransportPluginManager propertiesForEndpointWithUUID:]_block_invoke
- ___61-[ACCPlatformSleepAssertionManager addSleepAssertionForUUID:]_block_invoke
- ___61-[ACCTransportPluginManager identifierForConnectionWithUUID:]_block_invoke
- ___61-[ACCTransportPluginManager propertiesForConnectionWithUUID:]_block_invoke
- ___61-[ACCTransportServerRemote setConnectionAuthenticated:state:]_block_invoke
- ___62-[ACCPlatformSleepAssertionManager _addSleepAssertionForUUID:]_block_invoke
- ___62-[ACCTransportPluginManager transportTypeForEndpointWithUUID:]_block_invoke
- ___63-[ACCTransportPluginManager connectionUUIDForEndpointWithUUID:]_block_invoke
- ___63-[ACCTransportPluginManager setProperties:forEndpointWithUUID:]_block_invoke
- ___65-[ACCTransportPluginManager connectionTypeForConnectionWithUUID:]_block_invoke
- ___65-[ACCTransportPluginManager setProperties:forConnectionWithUUID:]_block_invoke
- ___66-[ACCTransportPluginManager certificateDataForConnectionWithUUID:]_block_invoke
- ___66-[ACCTransportPluginManager setAccessoryInfo:forEndpointWithUUID:]_block_invoke
- ___68-[ACCTransportPluginManager certificateSerialForConnectionWithUUID:]_block_invoke
- ___68-[ACCTransportServerRemote propertiesForEndpointWithUUID:withReply:]_block_invoke
- ___68-[PlatformIAPDBridge _handleAuthenticationState:forPortID:certData:]_block_invoke_2
- ___70-[ACCTransportPluginManager authStatusForConnectionWithUUID:authType:]_block_invoke
- ___70-[ACCTransportServerRemote identifierForConnectionWithUUID:withReply:]_block_invoke
- ___70-[ACCTransportServerRemote propertiesForConnectionWithUUID:withReply:]_block_invoke
- ___71-[ACCTransportServerRemote isConnectionAuthenticatedForUUID:withReply:]_block_invoke
- ___72-[ACCTransportServerRemote connectionUUIDForEndpointWithUUID:withReply:]_block_invoke
- ___72-[ACCTransportServerRemote setProperties:forEndpointWithUUID:withReply:]_block_invoke
- ___73-[ACCTransportServerRemote accessoryInfoForConnectionWithUUID:withReply:]_block_invoke
- ___73-[ACCTransportServerRemote removeProperty:forEndpointWithUUID:withReply:]_block_invoke
- ___74-[ACCTransportPluginManager certificateCapabilitiesForConnectionWithUUID:]_block_invoke
- ___74-[ACCTransportPluginManager certificateSerialStringForConnectionWithUUID:]_block_invoke
- ___74-[ACCTransportServerRemote setProperties:forConnectionWithUUID:withReply:]_block_invoke
- ___75-[ACCTransportServerRemote removeProperty:forConnectionWithUUID:withReply:]_block_invoke
- ___75-[ACCTransportServerRemote setAccessoryInfo:forEndpointWithUUID:withReply:]_block_invoke
- ___79-[ACCTransportServerRemote authStatusForConnectionWithUUID:authType:withReply:]_block_invoke
- ___85-[ACCTransportPluginManager setSupervisedTransportsRestricted:forConnectionWithUUID:]_block_invoke
- ___87-[ACCTransportServerRemote appendToArrayProperty:values:forEndpointWithUUID:withReply:]_block_invoke
- ___89-[ACCTransportServerRemote addToDictionaryProperty:values:forEndpointWithUUID:withReply:]_block_invoke
- ___89-[ACCTransportServerRemote appendToArrayProperty:values:forConnectionWithUUID:withReply:]_block_invoke
- ___91-[ACCTransportServerRemote addToDictionaryProperty:values:forConnectionWithUUID:withReply:]_block_invoke
- ____AccManagerCTAProcessingQueue_block_invoke
- ____iap2_session_control_endpointCallback_block_invoke
- ____initSharedManager_block_invoke
- ____invokeFeatureHandler_block_invoke
- ____invokeFeatureHandler_block_invoke_2
- ____invokeFeatureHandler_block_invoke_3
- ____logAuthPassedEvent_block_invoke
- ____platform_connectionInfo_sendDataForAuthProtocolEndpoint_block_invoke
- ____platform_connectionInfo_sendDataForiAP2Endpoint_block_invoke
- ____platform_externalAccessory_EASessionOpened_block_invoke
- ___acc_endpoint_sendOutgoingData_block_invoke
- ___acc_endpoint_setupPassthroughMode
- ___acc_endpoint_setupPassthroughPair
- ___acc_manager_checkForInductiveCTA_block_invoke
- ___acc_manager_checkForWirelessCTA_block_invoke
- ___block_descriptor_32_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16l
- ___block_descriptor_36_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16l
- ___block_descriptor_40_e35_v24?0^{__CFString=}8^{__CFData=}16l
- ___block_descriptor_40_e8_32r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- ___block_descriptor_40_e8_32r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- ___block_descriptor_40_e8_32s_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8
- ___block_descriptor_41_e8_32s_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8
- ___block_descriptor_44_e8_32r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- ___block_descriptor_44_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- ___block_descriptor_48_e8_32s40r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_49_e8_32s40r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_49_e8_32s40s_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8
- ___block_descriptor_50_e8_32s40r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_52_e8_32s40r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
- ___block_descriptor_61_e8_32s40s48r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
- ___block_descriptor_64_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16l
- ___block_descriptor_64_e8_32s40r48r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e269_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8s48l8r56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e201_B24?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^??BB{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r64l8s40l8s48l8s56l8
- ___findInductiveCTADonorCapableConnection
- ___findInductiveCTAReceiverCapableConnection
- ___findWirelessCTADonorCapableConnection
- ___findWirelessCTAReceiverCapableConnection
- ___genericMFi_endpoint_handlePropertiesDidChange_block_invoke
- ___genericMFi_util_SetOrRemoveProperty_block_invoke
- ___initSharedManager_block_invoke
- ___logAuthPassedEvent_block_invoke
- ___platform_analytics_connectionPassedAuthForProtocol_block_invoke
- ___platform_analytics_endpointAccessoryInfoDidChange_block_invoke
- ___platform_analytics_endpointWillBeDestroyed_block_invoke
- ___platform_connectionInfo_accessoryInfoForConnection_block_invoke
- ___platform_connectionInfo_accessoryPropertiesForConnection_block_invoke
- ___platform_connectionInfo_accessoryPropertiesForEndpoint_block_invoke
- ___platform_externalAccessory_closeExternalAccessorySession_block_invoke
- ___platform_externalAccessory_openExternalAccessorySession_block_invoke
- ___platform_externalAccessory_openExternalAccessorySession_block_invoke_2
- ___platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID_block_invoke
- ___qiAuth_endpoint_publish_block_invoke
- ___t56_endpoint_publish_block_invoke
- __acc_endpoint_setupPassthroughMode
- __acc_endpoint_setupPassthroughPair
- __acc_manager_checkForInductiveCTA_checkMatch
- __acc_manager_checkForWirelessCTA_checkMatch
- __acc_manager_getEndpointWithUUID_unsafe
- __acc_manager_processIncomingDataForEndpointWithUUID
- __analyticsQueue
- __configStream_endpoint_destroy_block_invoke
- __connectionContainsInductiveEndpoint
- __findAdapterForConnection
- __findConnectionsThroughAdapter
- __findiAP2EndpointForConnection
- __gAccConnectionLock
- __gAccManagerLock
- __genericMFi_util_SetOrRemoveProperty_block_invoke
- __getEndpointAndAccInfoForAuthPassedEvent
- __handleConnectionCallback
- __handleEAPowerSourceChange
- __handleEndpointCallback
- __iap2_session_control_endpointCallback
- __invokeFeatureHandler
- __invokeFeatureHandlerIterator
- __isModelNumberConnected
- __platform_analytics_connectionPassedAuthForProtocol_block_invoke
- __platform_analytics_endpointAccessoryInfoDidChange_block_invoke
- __platform_analytics_endpointWillBeDestroyed_block_invoke
- __platform_connectionInfo_addAuthInfo
- __platform_externalAccessory_closeExternalAccessorySession_block_invoke
- __platform_externalAccessory_openExternalAccessorySession_block_invoke_2
- __platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID_block_invoke
- __qiAuth_endpoint_publish_block_invoke
- __sendEAPowerSourceUpdate
- __setTransportLockoutHandler
- __t56_endpoint_publish_block_invoke
- __tryWRLock
- _acc_connection_addEndpoint
- _acc_connection_addToDictionaryProperty
- _acc_connection_appendToArrayProperty
- _acc_connection_containsEndpointUUID
- _acc_connection_copyDescription
- _acc_connection_copyEndpointUUIDs
- _acc_connection_copyIdentifier
- _acc_connection_copyProperties
- _acc_connection_copyProperty
- _acc_connection_copyUUID
- _acc_connection_create
- _acc_connection_destroy
- _acc_connection_endpointIterateForConnection
- _acc_connection_getAccessoryInfo
- _acc_connection_getAdapterPID
- _acc_connection_getAdapterVID
- _acc_connection_getAuthInfo
- _acc_connection_getAuthStatus
- _acc_connection_getDurationMS
- _acc_connection_getNumEndpoints
- _acc_connection_getPairingStatus
- _acc_connection_getSupervisedTransportsRestricted
- _acc_connection_getType
- _acc_connection_getTypeString
- _acc_connection_getUUID
- _acc_connection_isAuthenticated
- _acc_connection_isAuthenticatedForAppMatchLaunch
- _acc_connection_isAuthenticatedForInductivePowerIn
- _acc_connection_isConnectedThroughAdapter
- _acc_connection_isPublished
- _acc_connection_mapAccessoryInfo
- _acc_connection_publish
- _acc_connection_removeAllEndpoints
- _acc_connection_removeEndpointUUID
- _acc_connection_removeProperty
- _acc_connection_sendDataOut
- _acc_connection_setAuthCTAAAllowed
- _acc_connection_setAuthCertData
- _acc_connection_setAuthStatus
- _acc_connection_setDataOutHandler
- _acc_connection_setPairingStatus
- _acc_connection_setProperties
- _acc_connection_setProperty
- _acc_connection_setSupervisedTransportsRestricted
- _acc_connection_updateAcccessoryInfoIfNeeded
- _acc_endpoint_addToDictionaryProperty
- _acc_endpoint_appendToArrayProperty
- _acc_endpoint_clearAccessoryInfo
- _acc_endpoint_copyDescription
- _acc_endpoint_copyIdentifier
- _acc_endpoint_copyParentEndpointUUID
- _acc_endpoint_copyProperties
- _acc_endpoint_copyProperty
- _acc_endpoint_create
- _acc_endpoint_destroy
- _acc_endpoint_getAccessoryInfo
- _acc_endpoint_getCreationTimestampMS
- _acc_endpoint_getDurationMS
- _acc_endpoint_getParentConnection
- _acc_endpoint_getProtocol
- _acc_endpoint_getProtocolString
- _acc_endpoint_getTransportType
- _acc_endpoint_getTransportTypeString
- _acc_endpoint_isPublished
- _acc_endpoint_isTransportRestricted
- _acc_endpoint_isWireless
- _acc_endpoint_processIncomingData
- _acc_endpoint_processOutgoingSecureTunnelDataForClient
- _acc_endpoint_publish
- _acc_endpoint_removeProperty
- _acc_endpoint_sendOutgoingData
- _acc_endpoint_setAccessoryInfo
- _acc_endpoint_setAccessoryInfoOverridesWithDictionary
- _acc_endpoint_setAccessoryInfoWithDictionary
- _acc_endpoint_setEndpointSecureTunnelDataReceiveTypeHandler
- _acc_endpoint_setParentEndpointUUID
- _acc_endpoint_setProperties
- _acc_endpoint_setProperty
- _acc_endpoint_supervisedTransportsRestrictedDidChange
- _acc_manager_callbackForConnection
- _acc_manager_callbackForEndpoint
- _acc_manager_checkForInductiveCTA
- _acc_manager_checkForWirelessCTA
- _acc_manager_copyAdapterConnectionUUIDForConnection
- _acc_manager_copyAllConnections
- _acc_manager_copyAllEndpoints
- _acc_manager_copyConnectionUUIDForEndpointUUID
- _acc_manager_copyConnectionsThroughAdapter
- _acc_manager_copyDeviceUUID
- _acc_manager_copyEndpointUUIDsForConnection
- _acc_manager_disableLockoutForAllTransportTypes
- _acc_manager_disableLockoutForTransportType
- _acc_manager_enableLockoutForTransportType
- _acc_manager_getConnectionWithUUID
- _acc_manager_getEndpointWithUUID
- _acc_manager_isLockoutActiveForTransportType
- _acc_manager_iterateAllConnections
- _acc_manager_iterateAllEndpoints
- _acc_manager_newConnection
- _acc_manager_newEndpointForConnection
- _acc_manager_newEndpointForConnectionWithUUID
- _acc_manager_processIncomingDataForEndpointWithUUID
- _acc_manager_protectedConnectionCall
- _acc_manager_protectedEndpointCall
- _acc_manager_publishConnectionWithUUID
- _acc_manager_removeConnectionWithUUID
- _acc_manager_removeEndpointWithUUID
- _acc_platform_packetLogging_logAccAuthProtocolMsg
- _acc_platform_packetLogging_logEAData
- _acc_platform_packetLogging_logEventVA
- _acc_platform_packetLogging_logGenericMFiTLV
- _acc_platform_packetLogging_logParsedData
- _acc_platform_packetLogging_logQiAuthMsg
- _acc_platform_packetLogging_logSNTPTimeSyncMsg
- _acc_platform_packetLogging_logT56Msg
- _acc_platform_packetLogging_logiAP2Packet
- _analyticsQueue
- _analyticsQueue.analyticsQueue
- _analyticsQueue.onceToken
- _configStream_endpoint_publish
- _findiAP2EndpointForConnection
- _invokeFeatureHandlerIterator
- _kCFACCUserDefaultsKey_PretendWirelessCTAMatch
- _kCFWirelessCTAConnectionUUID
- _kCFWirelessCTAIdentifier
- _kCFWirelessCTAOOBPairingData
- _logAuthPassedEvent
- _objc_msgSend$_addAccessoryInfo:
- _objc_msgSend$_addEAProtocolPrimaryEndpointInfo:
- _objc_msgSend$_addEAProtocolsForEAEndpoints:
- _objc_msgSend$_addGenericMFiEAProtocols:
- _objc_msgSend$_addSleepAssertionForUUID:
- _objc_msgSend$_addiAP2AuthInfo:
- _objc_msgSend$_addiAP2EAProtocols:
- _objc_msgSend$_addiAP2IdentificationInfo:
- _objc_msgSend$_shouldProcessAuthenticationFailState:
- _objc_msgSend$addAccessoryForEndpointUID:andBitmask:andOldBitmask:
- _objc_msgSend$addSleepAssertionForUUID:
- _objc_msgSend$iapdAccessory:dataArrivedFromAccessory:
- _objc_msgSend$iapdAccessoryArrived:
- _objc_msgSend$initWithEndpointUID:andBitmask:andOldBitmask:
- _objc_msgSend$initWithInt:
- _platform_analytics_availableCurrentNegotiated
- _platform_analytics_connectionAuthUnsuccessful
- _platform_analytics_connectionAuthUnsuccessfulForProtocol
- _platform_analytics_connectionPassedAuth
- _platform_analytics_connectionPassedAuthForProtocol
- _platform_analytics_connectionWillBeDestroyed
- _platform_analytics_connectionWillBePublished
- _platform_analytics_endpointAccessoryInfoDidChange
- _platform_analytics_endpointProtocolDidChange
- _platform_analytics_endpointWillBeDestroyed
- _platform_analytics_endpointWillBePublished
- _platform_analytics_iap1_lingoesSupportedDidChange
- _platform_analytics_iap2_featuresSupportedDidChange
- _platform_blePairing_deleteParams
- _platform_btConnectionStatus_deleteParams
- _platform_configStream_deleteParams
- _platform_connectionInfo_accessoryConnectionAttached
- _platform_connectionInfo_accessoryConnectionInfoPropertyChanged
- _platform_connectionInfo_accessoryEndpointAttached
- _platform_connectionInfo_accessoryEndpointInfoPropertyChanged
- _platform_connectionInfo_accessoryEndpointProtocolUpdate
- _platform_externalAccessory_EASessionOpened.onceToken
- _platform_externalAccessory_retrieveMutableEADataFromAppForSessionUUID
- _platform_iapd_bridge_accessory_connected
- _platform_iapd_bridge_accessory_processIncomingData
- _platform_mediaLibrary_deleteParams
- _platform_navigation_deleteParams
- _platform_oobBtPairing2_deleteParams
- _platform_sleepAssertion_create
- _platform_voiceOver_deleteParams
- _pthread_rwlock_rdlock
- _pthread_rwlock_trywrlock
- _pthread_rwlock_unlock
- _pthread_rwlock_wrlock
- _startListUpdatesHandler
- _tryWRLock
- accSNTPTimeSync_endpoint_getAccessoryTime
- accSNTPTimeSync_endpoint_sendAccessoryTime
- acc_connection.c
- acc_connection_getPairingStatus
- acc_connection_setPairingStatus
- acc_endpoint.c
- acc_endpoint_sendOutgoingData
- acc_manager.c
- acc_manager_copyAdapterConnectionUUIDForConnection
- acc_manager_copyAllConnections
- acc_manager_copyAllEndpoints
- acc_manager_copyConnectionsThroughAdapter
- acc_manager_disableLockoutForAllTransportTypes
- acc_manager_disableLockoutForTransportType
- acc_manager_enableLockoutForTransportType
- acc_manager_isLockoutActiveForTransportType
- acc_manager_objc.m
- acc_platform_analytics.m
- acc_platform_packetLogging_logAccAuthProtocolMsg
- acc_platform_packetLogging_logData
- acc_platform_packetLogging_logEAData
- acc_platform_packetLogging_logEventVA
- acc_platform_packetLogging_logGenericMFiTLV
- acc_platform_packetLogging_logMFi4AuthProtocolMsg
- acc_platform_packetLogging_logParsedData
- acc_platform_packetLogging_logQiAuthMsg
- acc_platform_packetLogging_logSNTPTimeSyncMsg
- acc_platform_packetLogging_logT56Msg
- acc_platform_packetLogging_logiAP2Packet
- platform_analytics_connectionPassedAuthForProtocol
- platform_connectionInfo_beginUserKeyErase
- platform_connectionInfo_beginVendorKeyErase
- platform_connectionInfo_cancelUserKeyErase
- platform_connectionInfo_cancelVendorKeyErase
- platform_connectionInfo_configStreamPropertySetValue
- platform_connectionInfo_continueUserKeyErase
- platform_connectionInfo_continueVendorKeyErase
- platform_connectionInfo_copyUserPrivateKey
- platform_connectionInfo_getAccessoryUserName
- platform_connectionInfo_getPrivateNvmKeyValues
- platform_connectionInfo_provisionPairing
- platform_connectionInfo_setPrivateNvmKeyValues
- platform_connectionInfo_setPublicNvmKeyValues
- platform_iapd_bridge_accessory_connected
- platform_oobBtPairing_requestLegacyConnectionIDForAccessoryUID
- platform_sleepAssertion_create
- platform_wifisharing_accessory_wifi_configuration_information
- t56_endpoint_create
CStrings:
+ " (inductive)"
+ "%s (manager2): no endpoint for endpoint %@ !!"
+ "%s (manager2): no protocol endpoint for endpoint %@ !!"
+ "%s (manager2): protocol_authSetupStart failed"
+ "%s (manager2): unable to find endpoint for %@"
+ "%s (manager2): wrong protocol (%d) for endpoint %@ !!"
+ "%s: !dhPublicKey"
+ "%s: (manager2) parentEndpoint NULL, dataOut %@"
+ "%s: (manager2) parentEndpointUUID %@, dataOut %@"
+ "%s: Failed to get tokens for endpointUUID %@"
+ "%s: Found GenericMFi endpointUUID %@, dispatch authStatusChanged to endpoint queue, authStatus %{coreacc:ACCAuthInfo_Status_t}d"
+ "%s: Found only 1 token for endpointUUID %@"
+ "%s: Invalid parameter! block(%d), pConnection(%d), queue(%d), destroying(%d)"
+ "%s: Missing ACCEndpoint2_t"
+ "%s: Skip adding AppMatch EA protocols for accessory (manager2)!!! authenticatedForAppMatchLaunch %d, ignoreCertCaps %d, %@"
+ "%s: connection %@ not found"
+ "%s: connection %@, endpoint %@, handlerType %d, arg1 %d"
+ "%s: connection %@, endpoint %@, handlerType %d, arg1 present: %s"
+ "%s: connection destroyed, invoking resultHandler with error for endpoint %@"
+ "%s: connectionUUID %@ not owned by this client"
+ "%s: destroyConnection true! drop calling block(%d), pConnection(%d)"
+ "%s: endpoint %@ disappeared before async dispatch"
+ "%s: endpoint %@ not found for connection %@"
+ "%s: endpoint %@. handlerType %d"
+ "%s: endpoint %@. protocol %{coreacc:ACCEndpoint_Protocol_t}d, handlerType %d"
+ "%s: handler returned false for handlerType %d (endpoint %@) — invoking resultHandler with error"
+ "%s: invalid parameter — connectionUUID(%d), endpointUUID(%d), resultHandler(%d)"
+ "%s: isEqual %d, new %@, old %@"
+ "%s: more than 2 tokens found for endpointUUID %@, continue to assume first is connectionUUID"
+ "%s: pairingDataMatch %d, bdAddrMatch %d"
+ "%s:%d  connectionType %{coreacc:ACCConnection_Type_t}d"
+ "%s:%d  connectionUUID %@"
+ "%s:%d  connectionUUID %@, authType %{coreacc:ACCAuthInfo_Type_t}d, authStatus %{coreacc:ACCAuthInfo_Status_t}d"
+ "%s:%d  connectionUUID %@, authType %{coreacc:ACCAuthInfo_Type_t}d, authStatus %{coreacc:ACCAuthInfo_Status_t}d, certData %@, bCTAAllowed %d"
+ "%s:%d  connectionUUID %@, certData %@"
+ "%s:%d  connectionUUID %@, endpointUUID %@"
+ "%s:%d  connectionUUID %@, endpointUUID %@, accessoryInfoOverrides %@"
+ "%s:%d  connectionUUID %@, endpointUUID %@, dataIn %@"
+ "%s:%d  connectionUUID %@, endpointUUID %@, key %@"
+ "%s:%d  connectionUUID %@, endpointUUID %@, key %@, values %@"
+ "%s:%d  connectionUUID %@, endpointUUID %@, properties %@"
+ "%s:%d  connectionUUID %@, isAuthenticated %d"
+ "%s:%d  connectionUUID %@, key %@"
+ "%s:%d  connectionUUID %@, key %@, value %@"
+ "%s:%d  connectionUUID %@, key %@, values %@"
+ "%s:%d  connectionUUID %@, properties %@"
+ "%s:%d  connectionUUID %@, supervisedTransportsRestricted %d"
+ "%s:%d  protocol %{coreacc:ACCEndpoint_Protocol_t}d"
+ "%s:%d  transportType %{coreacc:ACCEndpoint_TransportType_t}d"
+ "%s:%d [%ld / %ld], call iterator %@ for endpoint %@ - %@ "
+ "%s:%d [%ld / %ld], call iteratorCB, %@"
+ "%s:%d adapterConnection %@, adapterVID %@, adapterPID %@"
+ "%s:%d call callback %@ for connection %@"
+ "%s:%d call connectionCB, connection %@ "
+ "%s:%d call handler %@ for endpoint %@ - %@ "
+ "%s:%d connection %@"
+ "%s:%d connection %@, connectionCB %d"
+ "%s:%d connectionUUID %@, deprecated, should use acc_manager2_performBlockForConnection"
+ "%s:%d connectionUUID %@, endpointUUID %@, deprecated, should use acc_manager2_callbackForEndpoint"
+ "%s:%d endpoint %@, endpointCB %d"
+ "&=+?"
+ "-[ACCExternalAccessory _addGenericMFiEAProtocolsFromSnapshot:connectionUUID:]"
+ "-[ACCTransportPluginManager destroyEndpointWithUUID:]"
+ "-[ACCTransportServerRemote createEndpointWithTransportType:andProtocol:andIdentifier:forConnectionWithUUID:withReply:]"
+ "-[ACCTransportServerRemote destroyConnectionWithUUID:withReply:]"
+ "-[ACCTransportServerRemote destroyEndpointWithUUID:withReply:]"
+ "-[ACCTransportServerRemote processIncomingData:forEndpointWithUUID:withReply:]"
+ "-[ACCTransportServerRemote publishConnectionWithUUID:withReply:]"
+ "0x%02x, "
+ "5#"
+ "<ACCConnection2_t: %@; connectionType: [%s]; identifier: %@; dataOutHandler: %s; creationTimestampMS: %llu; durationMS: %llu; numEndpoints: %ld; authenticated: %s; accessoryInfo: %s; numProperties: %ld; published: %s>"
+ "<ACCEndpoint2_t: %@; parentConnectionUUID: %@; transportType: [%s]; protocol: [%s]; identifier: %@; creationTimestampMS: %llu; durationMS: %llu; protocolEndpoint: %s; accessoryInfo: %s; numAccessoryInfoOverrides: %ld; numProperties: %ld, published: %s>"
+ "@32@0:8@16^{?=^{ACCEndpoint2_s}^{__CFString}^{__CFString}@BB^{iAP2LinkRunLoop_st}{iAP2PacketSYNData_st=CCCCSSSCCS[5C][5C]C[5C][5{?=CCCB}]}iB^{iAP2Packet_st}^{iAP2MsgParser_st}{iAP2Msg_t_st=*III**^?^vB^?}*[29^v]^vB^vd}24"
+ "@48@0:8@16@24Q32Q40"
+ "ACCConnectionSnapshotInfo"
+ "ACCEndpointSnapshotInfo"
+ "Adding accessory info (manager2): name %@, model %@, manufacturer %@, serial %@, firmware revision (active) %@, firmware revision (pending) %@, hardware revision %@, ppid %@, regionCode %@, hideFromUI: %s"
+ "Adding iAP2 identification info (manager2)..."
+ "AuthState: !pEndpoint2"
+ "AuthState: AUTH FAILED"
+ "AuthState: AUTH PASSED"
+ "AuthState: AUTH TIMEOUT"
+ "Authorized but endpoint %@ destroyed, skip completion"
+ "B24@0:8^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}16"
+ "B24@?0^{__CFString=}8^v16"
+ "B24@?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB@}16"
+ "B24@?0^{__CFString=}8^{ACCConnection2_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB^{dispatch_queue_s}}16"
+ "B32@0:8^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}16@24"
+ "B32@?0^{__CFString=}8^{__CFString=}16^v24"
+ "B32@?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}24"
+ "B32@?0^{__CFString=}8^{__CFString=}16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?^{dispatch_queue_s}@?BB{_opaque_pthread_mutex_t=q[56c]}}24"
+ "B40@0:8^{__CFString=}16i24i28@32"
+ "Check for InductiveCTA: finisehd in %lu ms."
+ "Check for WirelessCTA: Found match! donor %@, receiver %@"
+ "Check for WirelessCTA: finisehd in %lu ms."
+ "Closing EA session for endpoint %@ (manager2)..."
+ "Connection Management2"
+ "Connection destroyed"
+ "Connection not found"
+ "Connection2"
+ "Created endpoint (internal) %@ for connection %@."
+ "Creating endpoint (internal) %@ for connection %@ - connection published = %s..."
+ "Didn't find native EA endpoint UUID, using primary endpoint UUID (manager2)"
+ "Endpoint %@ added to endpoint list for connection %@, new count %ld"
+ "Endpoint %@ already in connection endpoint list!"
+ "Endpoint no longer available"
+ "Endpoint not found"
+ "Endpoint2"
+ "Error setting AccessoryPowerMode for endpoint: %@ (manager2)"
+ "Failed to create endpoint (internal) %@ for connection %@."
+ "Failed to get pConnection for %@!"
+ "Failed to init protocol layer for endpoint %@ (protocol %{coreacc:ACCEndpoint_Protocol_t}d) - destroying endpoint"
+ "Failed to register HID interface! (endpointUUID: %@, componentID: %d)"
+ "Failed to unregister HID interface! (endpointUUID: %@, componentID: %d)"
+ "Feature handler failed"
+ "Feature handler not found"
+ "Finished updating EADictionary (manager2)... (new: %@)"
+ "Found EANative endpointUUID %@, identifier %@ (manager2)"
+ "Found native EA USB endpoint %@ protocol for string %@ (manager2)"
+ "Get SnapshotInfo for all connections..."
+ "Get SnapshotInfo for connection: %@ : %@"
+ "Get SnapshotInfo for connection: %@..."
+ "Get SnapshotInfo for endpoint: %@ - %@ : %@"
+ "Get SnapshotInfo for endpoint: %@ - %@..."
+ "Have %ld endpoints to parse (manager2)"
+ "Have first EA session requiring sleep assertion (manager2)"
+ "InfoProperties_AccInfo"
+ "InfoProperties_AppMatchProtocols"
+ "InfoProperties_AppMatchTeamIDs"
+ "InfoProperties_AuthInfo"
+ "InfoProperties_CarPlayCapable"
+ "InfoProperties_CertData"
+ "InfoProperties_CertSerial"
+ "InfoProperties_ConnectionType"
+ "InfoProperties_ConnectionUUID"
+ "InfoProperties_CreateTimestampMs"
+ "InfoProperties_EAProtocols"
+ "InfoProperties_EndpointUUID"
+ "InfoProperties_Endpoints"
+ "InfoProperties_FeaturesBitMask"
+ "InfoProperties_Identifier"
+ "InfoProperties_IsConnectedThroughAdapter"
+ "InfoProperties_MultipleEASessionsCapable"
+ "InfoProperties_ParentConnection"
+ "InfoProperties_PreferredApp"
+ "InfoProperties_Properties"
+ "InfoProperties_ProtocolType"
+ "InfoProperties_ThemeAssetsCapable"
+ "InfoProperties_TransportType"
+ "InfoProperties_USBCarPlayCapable"
+ "InfoProperties_VehicleInfo"
+ "InfoProperties_WirelessCarPlayCapable"
+ "Invalid parameter to invokeFeatureHandlerWithResult"
+ "LOG; %.6f; %@; %s; %@; %s; data(len=%d)="
+ "LOG; %.6f; %@; %s; %@; SNTP BD Cmd %#04x; packetLen %#04x; data(len=%d)="
+ "LOG; %.6f; %@; %s; %@; len=0x%04x; control=0x%02x; seq=0x%02x; ack=0x%02x; session=0x%02x; hdrChk=0x%04x; payload(len=%d chk=0x%04x)="
+ "LOG; %.6f; %@; %s; %@; sessionID %u; %s; data(len=%d)="
+ "LOG; %.6f; %@; %s; %@; sessionID %u; msgID %#04x; ctl0 %#04x; ctl1 %#04x; payloadLen %d; data(len=%d)="
+ "LOG; %.6f; %@; %s; %@; sessionUUID %@; data(len=%d)="
+ "Missing connectionUUID, endpointUUID, or pConnection for wireless CarPlay bridge connect"
+ "Missing required key erase parameters"
+ "NVMReadResponse: paramID %d exceeds maximum expected value"
+ "No DataOutHandler or ConnectionUUID!!! - Unable to send %ld bytes of outgoing data for connectionUUID %@ endpointUUID %@"
+ "No iAP2 endpoint found! (manager2)"
+ "No native USB endpoints found! (manager2)"
+ "No queue found for handlerType %d (withResult) for %{coreacc:ACCEndpoint_Protocol_t}d! (endpoint %@)"
+ "Opening EA session for endpoint %@ (manager2)..."
+ "OverrideMPPAuthSupported"
+ "Protocol endpoint not available"
+ "Protocol endpoint queue not available"
+ "QiAuth publish: transportType %{coreacc:ACCEndpoint2_transportType_t}d"
+ "QiAuth publish: transportType %{coreacc:ACCEndpoint2_transportType_t}d, start protocol!!!"
+ "Removing connection endpoint: %@ - %@..."
+ "RequestNVMAuthFinish"
+ "Sending outgoing EA data to endpointUUID %@ (manager2)"
+ "Skipping handlerType %d for destroying endpoint %@"
+ "Skipping handlerType %d for uninitialized iAP2 endpoint %@"
+ "T@\"<ACCPowerSiphoningControlDelegate>\",R,W,N,V_delegate"
+ "T@\"NSArray\",R,N,V_appMatchProtocols"
+ "T@\"NSArray\",R,N,V_appMatchTeamIDs"
+ "T@\"NSArray\",R,N,V_eaProtocols"
+ "T@\"NSData\",R,N,V_certData"
+ "T@\"NSData\",R,N,V_certSerial"
+ "T@\"NSDictionary\",R,N,V_accInfo"
+ "T@\"NSDictionary\",R,N,V_authInfo"
+ "T@\"NSDictionary\",R,N,V_endpoints"
+ "T@\"NSDictionary\",R,N,V_properties"
+ "T@\"NSDictionary\",R,N,V_vehicleInfo"
+ "T@\"NSString\",C,N,V_modelNumber"
+ "T@\"NSString\",R,N,V_connectionUUID"
+ "T@\"NSString\",R,N,V_endpointUUID"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@\"NSString\",R,N,V_parentConnection"
+ "T@\"NSString\",R,N,V_preferredApp"
+ "TB,R,N,V_carPlayCapable"
+ "TB,R,N,V_isConnectedThroughAdapter"
+ "TB,R,N,V_multipleEASessionsCapable"
+ "TB,R,N,V_themeAssetsCapable"
+ "TB,R,N,V_usbCarPlayCapable"
+ "TB,R,N,V_wirelessCarPlayCapable"
+ "TQ,R,N,V_createTimestampMs"
+ "TQ,R,N,V_featuresBitMask"
+ "TS,R,N,V_adapterPID"
+ "TS,R,N,V_adapterVID"
+ "T^{ACCConnection2_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB@},V_pConnection"
+ "Ti,R,N,V_connectionType"
+ "Ti,R,N,V_transportType"
+ "URLQueryAllowedCharacterSet"
+ "Unnamed"
+ "Updating EADictionary (manager2)... (old: %@)"
+ "UserPublicKey %@"
+ "[#BT Connection Status] btConnectionStatus updateHandler (manager2): invokeHandler failed for %@"
+ "[#EventLogger] %s: didn't find accInfo for connection %@"
+ "[#EventLogger] %s: retry for connection %@ failed -- connection no longer exists"
+ "[#EventLogger] Calling auth passed via retry data%s"
+ "[#EventLogger] Filtered FeaturesMask: 0x%016llx"
+ "[#EventLogger] Performing retry in %llu seconds%s"
+ "[#EventLogger] True FeaturesMask: 0x%016llx"
+ "[#Power] addAccessoryForEndpointUID: endpointUID %@, modelNumber %@, updateTypesBitMask %llx, oldUpdateTypesBitmask %llx"
+ "[#SleepAssertions] Creating sleep assertion for UUID %@ with connectionType %d..."
+ "[#iapd Bridge] Can't find dictionary for accessory info"
+ "[#iapd Bridge] Can't find endpoint for accessory info"
+ "[#iapd Bridge] Dropping iAP1 bytes over %{coreacc:ACCEndpoint_TransportType_t}d! (manager2)"
+ "[#iapd Bridge] Got endpoint type of %d, must not handle failed auth state (manager2)"
+ "[#iapd Bridge] Ignoring failed auth state for endpoint type %{coreacc:ACCEndpoint_TransportType_t}d (manager2)"
+ "[#iapd Bridge] an iAP1 dock accessory connected (manager2) with transport type %{coreacc:ACCEndpoint_TransportType_t}d"
+ "[#iapd Bridge] enabling authentication passed? %d for USB Host (manager2)"
+ "[#iapd Bridge] found endpointUUID %@ for portID %llu, port lockout behavior has been removed for manager flow, No-Op"
+ "[#iapd Bridge] iAP1 lingoes supported (manager2): endpointUUID %@, lingoes 0x%08x"
+ "[#iapd Bridge] iapd accessory arrived (manager2), connectionUUID %@, generated portID %llu, acc. info %@"
+ "[#iapd Bridge] iapd accessory arrived (manager2), connectionUUID %@, generated portID %llu, coreAccToIAPDAccDict %@"
+ "[#iapd Bridge] ignoring authenticated flag for iAP1 bridge (manager2)"
+ "[manager2] %s: connectionUUID %@ not owned by this client"
+ "[manager2] %s: connectionUUID %@, bAuthCTAAllowed %d, authStatus %{coreacc:ACCAuthInfo_Status_t}d, certData %@"
+ "[manager2] %s: connectionUUID %@, properties %@"
+ "[manager2] %s: connectionUUID %@, supervisedTransportsRestricted %d"
+ "[manager2] %s: connectionUUID is nil"
+ "[manager2] %s: didn't find endpointUUID %@"
+ "[manager2] Attempt to modify accessoryInfo on connection not created by client, ignore! connectionUUID %@"
+ "[manager2] Attempt to modify properties on endpoint not created by client, ignore! endpointUUID %@"
+ "[manager2] Attempt to modify properties on endpoint of connection not created by client, ignore! endpointUUID %@, connectionUUID %@"
+ "[manager2] SecureTunnelHandler endpoint: %@, data:%@"
+ "[manager2] createConnectionWithType: %{coreacc:ACCConnection_Type_t}d andIdentifier: %@ withReply: , connectionUUID = %@, connectionUUIDs = %@"
+ "[manager2] createConnectionWithType: %{coreacc:ACCConnection_Type_t}d andIdentifier: %@, connectionUUID = %@"
+ "[manager2] createEndpointWithTransportType: %{coreacc:ACCEndpoint_TransportType_t}d andProtocol: %{coreacc:ACCEndpoint_Protocol_t}d andIdentifier: %@ forConnectionWithUUID: %@ withReply: , endpointUUID = %@, connectionUUIDs = %@"
+ "[manager2] createEndpointWithTransportType: %{coreacc:ACCEndpoint_TransportType_t}d forConnectionWithUUID: %@, endpointUUID = %@"
+ "[manager2] destroyConnectionWithUUID: %@"
+ "[manager2] destroyEndpointWithUUID: %@, connectionUUID: %@"
+ "[manager2] processIncomingData: didn't find endpointUUID %@"
+ "[manager2] publishConnectionWithUUID: %@"
+ "[manager2] setAccessoryInfo, endpointUUID %@, accInfo %@"
+ "[manager2] setConnectionAuthenticated: %@ state: %d, status %{coreacc:ACCAuthInfo_Status_t}d for type %{coreacc:ACCAuthInfo_Type_t}d"
+ "[manager2] setProperties, endpointUUID %@, properties %@"
+ "^{ACCConnection2_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB@}"
+ "^{ACCConnection2_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB@}16@0:8"
+ "_"
+ "_ACConnection"
+ "_acc_connection2_invokeFeatureHandlerWithResult_asyncImpl"
+ "_acc_connection2_invokeFeatureHandlerWithResult_asyncImpl_block_invoke"
+ "_acc_connection2_performBlockForConnection_internal"
+ "_acc_connection2_performBlockForEndpoint_internal"
+ "_acc_manager2_checkForInductiveCTA_checkMatch"
+ "_acc_manager2_checkForWirelessCTA_checkMatch"
+ "_acc_manager2_copyAdapterForConnection_internal"
+ "_acc_manager2_copyConnectionsThroughAdapter_internal"
+ "_acc_manager2_getConnectionEndpointStruct_internal"
+ "_acc_manager2_invokeFeatureHandlerWithResultForConnectionEndpoint_internal_block_invoke"
+ "_acc_manager2_setAdapterPropertiesOnConnections_internal"
+ "_adapterPID"
+ "_adapterVID"
+ "_addAccessoryInfoFromSnapshot:connectionSnapshot:"
+ "_addEAProtocolPrimaryEndpointInfoFromSnapshot:connectionSnapshot:"
+ "_addEAProtocolsForEAEndpointsFromSnapshots:connectionUUID:"
+ "_addGenericMFiEAProtocolsFromSnapshot:connectionUUID:"
+ "_addSleepAssertionForUUID:withConnectionType:"
+ "_addiAP2AuthInfoFromSnapshot:"
+ "_addiAP2EAProtocolsFromSnapshot:connectionUUID:"
+ "_addiAP2IdentificationInfoFromSnapshot:"
+ "_addiAP2VehicleInfoFromSnapshot:"
+ "_appMatchProtocols"
+ "_appMatchTeamIDs"
+ "_authInfo"
+ "_carPlayCapable"
+ "_certData"
+ "_checkForAdapterInfo_internal"
+ "_connectionType"
+ "_connectionUUID"
+ "_createTimestampMs"
+ "_eaProtocols"
+ "_featuresBitMask"
+ "_generateIAPDPortTypeForDictionary:withConnectionType:transportType:"
+ "_genericMFi_endpoint_handleAuthStatusDidChange_block_invoke_2"
+ "_genericMFi_endpoint_processPropertiesDidChange"
+ "_isConnectedThroughAdapter"
+ "_kConnectionEndpoint_SnapshotInfo_AdapterPID"
+ "_kConnectionEndpoint_SnapshotInfo_AdapterVID"
+ "_mfi4Auth_endpoint_firstUnlockHandler endpoint Found (manager2): %@"
+ "_mfi4Auth_endpoint_handlePropertiesDidChange (manager2): sendAuthSetupStart"
+ "_modelNumber"
+ "_multipleEASessionsCapable"
+ "_nativeUSBEndpointUUIDForProtocolIdentifierFromSnapshot:connectionUUID:"
+ "_pConnection"
+ "_parentConnection"
+ "_preferredApp"
+ "_properties"
+ "_replyGetNVMKey: !dictionary"
+ "_themeAssetsCapable"
+ "_transportType"
+ "_usbCarPlayCapable"
+ "_vehicleInfo"
+ "_wirelessCarPlayCapable"
+ "accAuthProtocol sendAuthSetupStart (manager2): endpoint not found for endpointUUID %@ !!"
+ "accAuthProtocol: (manager2) endpoint is ACCAuthProtocol"
+ "accFeatureHandlers_invokeHandler"
+ "acc_connection2_destroy: call acc_manager2_checkForInductiveCTA"
+ "acc_connection2_destroy: call acc_manager2_checkForWirelessCTA"
+ "acc_connection2_endpointIterateForConnection_internal"
+ "acc_connection2_getPairingStatus"
+ "acc_connection2_getPairingStatus: %d"
+ "acc_connection2_invokeFeatureHandler"
+ "acc_connection2_invokeFeatureHandlerWithResult_asyncWithAssert"
+ "acc_connection2_invokeFeatureHandler_asyncWithAssert"
+ "acc_connection2_isAuthenticatedForAppMatchLaunch_internal"
+ "acc_connection2_isAuthenticatedForInductivePowerIn_block_invoke"
+ "acc_connection2_performAsyncWithCleanup"
+ "acc_connection2_performSyncWithCleanup"
+ "acc_connection2_performSyncWithCleanup_block_invoke"
+ "acc_connection2_setAuthStatus: %@, authType %{coreacc:ACCAuthInfo_Type_t}d, authStatus %{coreacc:ACCAuthInfo_Status_t}d"
+ "acc_connection2_setAuthStatus: auth passed for BT connection, call acc_manager2_checkForWirelessCTA"
+ "acc_connection2_setAuthStatus: auth passed for NFC connection, call acc_manager2_checkForInductiveCTA"
+ "acc_connection2_setPairingStatus"
+ "acc_connection2_setProperties: call acc_manager2_checkForInductiveCTA"
+ "acc_connection2_setProperties: call acc_manager2_checkForWirelessCTA"
+ "acc_connection2_setProperty: call acc_manager2_checkForInductiveCTA"
+ "acc_connection2_setProperty: call acc_manager2_checkForWirelessCTA"
+ "acc_endpoint2_addToDictionaryProperty"
+ "acc_endpoint2_appendToArrayProperty"
+ "acc_endpoint2_invokeFeatureHandler"
+ "acc_endpoint2_invokeFeatureHandlerWithResult"
+ "acc_endpoint2_publish"
+ "acc_endpoint2_removeProperty"
+ "acc_endpoint2_setProperties"
+ "acc_endpoint2_setProperty"
+ "acc_manager2_addToDictionaryPropertyForConnection"
+ "acc_manager2_addToDictionaryPropertyForEndpoint"
+ "acc_manager2_appendToArrayPropertyForConnection"
+ "acc_manager2_appendToArrayPropertyForEndpoint"
+ "acc_manager2_copyAccessoryInfoDictionaryForConnection"
+ "acc_manager2_copyAuthCertDataForConnection"
+ "acc_manager2_copyCertCapabilitiesForConnection"
+ "acc_manager2_copyCertSerialForConnection"
+ "acc_manager2_copyCertSerialStringForConnection"
+ "acc_manager2_copyConnectionUUIDFromEndpointUUID"
+ "acc_manager2_copyEndpointIdentifier"
+ "acc_manager2_copyEndpointUUIDsForConnection"
+ "acc_manager2_copyIdentifierForConnection"
+ "acc_manager2_copyPropertiesForConnection"
+ "acc_manager2_copyPropertiesForEndpoint"
+ "acc_manager2_createEndpointForConnection"
+ "acc_manager2_getAuthStatusForConnection"
+ "acc_manager2_getConnectionType"
+ "acc_manager2_getConnectionTypeStringFromType"
+ "acc_manager2_getEndpointProtocol"
+ "acc_manager2_getEndpointTransportType"
+ "acc_manager2_getProtocolStringFromProtocol"
+ "acc_manager2_getTransportTypeStringFromTransportType"
+ "acc_manager2_invokeFeatureHandler"
+ "acc_manager2_invokeFeatureHandlerWithResult"
+ "acc_manager2_isConnectionAuthenticated"
+ "acc_manager2_isConnectionAuthenticatedForAppMatchLaunch"
+ "acc_manager2_iterateAllConnections_internal"
+ "acc_manager2_performBlockForConnection"
+ "acc_manager2_performBlockForConnectionEndpoint"
+ "acc_manager2_performBlockForConnectionEndpoint_asyncWithCleanup"
+ "acc_manager2_performBlockForConnection_internal"
+ "acc_manager2_processIncomingDataForConnectionEndpoint"
+ "acc_manager2_removePropertyForConnection"
+ "acc_manager2_removePropertyForEndpoint"
+ "acc_manager2_setAccessoryInfoForEndpoint"
+ "acc_manager2_setAccessoryInfoOverridesWithDictionaryForEndpoint"
+ "acc_manager2_setAdapterPropertiesOnConnectionsAsync"
+ "acc_manager2_setAuthCertDataForConnection"
+ "acc_manager2_setAuthStatusForConnection"
+ "acc_manager2_setAuthStatusWithCertDataForConnection"
+ "acc_manager2_setPropertiesForConnection"
+ "acc_manager2_setPropertiesForEndpoint"
+ "acc_manager2_setPropertiesOnConnectionsThroughAdapterConnectionAsync"
+ "acc_manager2_setPropertyForConnection"
+ "acc_manager2_setSupervisedTransportsRestricted"
+ "accessory doesn't support public iAP (manager2)"
+ "accessory supports public iAP (manager2)"
+ "accessoryNonce"
+ "adapterPID"
+ "adapterVID"
+ "addAccessoryForEndpointUID:andModelNumber:andBitmask:andOldBitmask:"
+ "addSleepAssertionForUUID:withConnectionType:"
+ "after open EA session, gWiredEASessionUUIDs count = %lu (manager2)"
+ "appMatchProtocols"
+ "appMatchTeamIDs"
+ "authInfo"
+ "authInfoCTAAllowed"
+ "authInfoCertCapabilities"
+ "authInfoCertData"
+ "authInfoCertSerial"
+ "authInfoCertSerialString"
+ "authInfoStatus"
+ "authInfoV2CertClass"
+ "authInfoVersion"
+ "certData"
+ "com.apple.acc.connection.queue.%@"
+ "com.apple.acc.manager.queue"
+ "com.apple.acc.platformWorkQ"
+ "componentsSeparatedByString:"
+ "connectionInfo accessoryConnectionAttachedWithSnapshotInfo: %@ type=%{coreacc:ACCConnection_Type_t}d"
+ "connectionInfo accessoryConnectionInfoPropertyChangedWithSnapshotInfo: %@"
+ "connectionInfo accessoryEndpointAttachedWithSnapshotInfo: %@ - %@ transport=%{coreacc:ACCEndpoint_TransportType_t}d protocol=%{coreacc:ACCEndpoint_Protocol_t}d"
+ "connectionInfo accessoryEndpointInfoPropertyChangedWithSnapshotInfo: %@ - %@"
+ "connectionInfo accessoryEndpointProtocolUpdateWithSnapshotInfo: %@ - %@ protocol=%{coreacc:ACCEndpoint_Protocol_t}d"
+ "connectionInfo sendDataForEndpoint (manager2): %@ - %@, %ld bytes Failed! "
+ "connectionInfo sendDataForEndpoint: data length %ld exceeds uint16_t max"
+ "connectionSupportsEA = %s (manager2)"
+ "connectionUUID is NULL — handler will not be called"
+ "createTimestampMs"
+ "cursorInformationHandler %@, cursorInfoRequestedMask=%xh, (validMask=%xh label=%@ value=%@ hint=%@ traitsMask=%llxh)"
+ "cursorInformationHandler %@, failed to get hint from cursorHint (%@)"
+ "cursorInformationHandler %@, failed to get label from cursorLabel (%@)"
+ "cursorInformationHandler %@, failed to get value from cursorValue (%@)"
+ "distantPast"
+ "eaProtocols"
+ "endpoint_requestNvmErasePublicKey: (manager2) no endpoint for endpoint!!"
+ "engineTypes"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "featuresBitMask"
+ "gWiredConnectionSessionCountDict: %@ (manager2)"
+ "getPairingStatus should not be routed through feature handler"
+ "handle_NVMAuthFinish: paramID %d exceeds maximum expected value"
+ "handle_NVMAuthStart: !serialNumberString"
+ "handle_NVMAuthStart: !userKey"
+ "handle_NVMAuthStart: !userPublicKey"
+ "handle_NVMAuthStart: U_c0: %@"
+ "handle_NVMAuthStart: U_sig: %@"
+ "handle_NVMAuthStart: ccsigma_seal error"
+ "handle_NVMAuthStart: ccsigma_sign: error"
+ "handle_NVMAuthStart: initMessage_RequestNVMAuthFinish error"
+ "handle_NVMAuthStart: paramID %d exceeds maximum expected value"
+ "handle_NVMEraseResponse: paramID %d exceeds maximum expected value"
+ "handle_NVMOperationResponse: paramID %d exceeds maximum expected value"
+ "handle_NVMPublicKeyChallenge: paramID %d exceeds maximum expected value"
+ "handlerType %d (withResult) not found for %{coreacc:ACCEndpoint_Protocol_t}d! (endpoint %@)"
+ "iAP2 vehicle info (manager2) is %@"
+ "iapdAccessoryArrivedWithSnapshotInfo:endpointUUID:protocol:transportType:connectionType:"
+ "iapdAccessoryProcessIncomingDataWithSnapshotInfo:transportType:protocol:incomingData:"
+ "informationHandler %@, infoRequestedMask=%xh, (validMask=%xh volume=%f rate=%f enabled=%d)"
+ "initSigmaContextNvm: !userKey"
+ "initSigmaContextNvm: ccsigma_export_key_share: error"
+ "initSigmaContextNvm: ccsigma_set_signing_function"
+ "initSigmaContextNvm: key_share_size != 33"
+ "initWithEndpointUID:andModelNumber:andBitmask:andOldBitmask:"
+ "isConnectedThroughAdapter"
+ "isModelNumberConnected:"
+ "isWireless"
+ "mapsDisplayName"
+ "matchAction"
+ "mfi4Auth_protocol_handleAuthSessionClose: Keep session open for %llds"
+ "mfi4Auth_protocol_initMessage_RequestNVMAuthFinish"
+ "modelNumber"
+ "multipleEASessionsCapable"
+ "nvmDhPublicKeyX %@"
+ "nvmDhPublicKeyY %@"
+ "oobPairing_endpoint_processIncomingData: call acc_manager2_checkForWirelessCTA"
+ "pConnection"
+ "pConnection2 = NULL"
+ "parentConnection"
+ "performAsync: block is NULL"
+ "performAsync: queue is NULL (ownsQueue=true)"
+ "performSync: block is NULL"
+ "performSync: queue is NULL (ownsQueue=true)"
+ "platform_analytics2_connectionPassedAuthForProtocol"
+ "platform_analytics2_connectionPassedAuthForProtocol_block_invoke"
+ "powerForConnectorTypeCCS1"
+ "powerForConnectorTypeCCS2"
+ "powerForConnectorTypeCHAdeMO"
+ "powerForConnectorTypeGBT_AC"
+ "powerForConnectorTypeGBT_DC"
+ "powerForConnectorTypeJ1772"
+ "powerForConnectorTypeMennekes"
+ "powerForConnectorTypeNACS_AC"
+ "powerForConnectorTypeNACS_DC"
+ "powerForConnectorTypeTesla"
+ "preferredApp"
+ "properties"
+ "removeCharactersInString:"
+ "setModelNumber:"
+ "setPConnection:"
+ "signature"
+ "substringToIndex:"
+ "supportedChargingConnectors"
+ "themeAssetsCapable"
+ "unionSet:"
+ "usbCarPlayCapable"
+ "v24@0:8^{?=^{ACCEndpoint2_s}^{__CFString}^{__CFString}@BB^{iAP2LinkRunLoop_st}{iAP2PacketSYNData_st=CCCCSSSCCS[5C][5C]C[5C][5{?=CCCB}]}iB^{iAP2Packet_st}^{iAP2MsgParser_st}{iAP2Msg_t_st=*III**^?^vB^?}*[29^v]^vB^vd}16"
+ "v24@0:8^{?=^{ACCEndpoint2_s}^{__CFString}^{__CFString}B@BBi^{__CFArray}^{__CFData}^{__CFArray}^{__CFArray}^{__CFDictionary}C@[3^v]}16"
+ "v24@0:8^{ACCConnection2_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSAB@}16"
+ "v24@0:8^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}16"
+ "v24@?0^{__CFArray=}8^{__CFError=}16"
+ "v24@?0^{__CFString=}8@\"ACCConnectionSnapshotInfo\"16"
+ "v24@?0^{__CFString=}8^{__CFString=}16"
+ "v32@0:8@16^{ACCEndpoint2_s=^{ACCConnection2_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}24"
+ "v32@0:8@16i24i28"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v44@0:8^{__CFString=}16^{__CFString=}24i32i36i40"
+ "v48@0:8@16@24Q32Q40"
+ "vehicleColorHexCode"
+ "vehicleInfo"
+ "vendorNonce"
+ "wirelessCarPlayCapable"
+ "\x91"
- "%s: %@ state: %d, status %{coreacc:ACCAuthInfo_Status_t}d for type %{coreacc:ACCAuthInfo_Type_t}d"
- "%s: %s:%d tryCount %d, err %d "
- "%s: Found GenericMFi endpointUUID %@, call genericMFi_endpoint_authStatusChanged, authStatus %{coreacc:ACCAuthInfo_Status_t}d"
- "%s: Have %ld endpoints to parse"
- "%s: Missing ACCEndpoint_t"
- "%s: [%u / %ld] endpointUUID %@"
- "%s: _isEqual %d, new %@, old %@"
- "%s: connectionUUID %@"
- "%s: connectionUUID %@, authType %{coreacc:ACCAuthInfo_Type_t}d"
- "%s: connectionUUID %@, bAuthCTAAllowed %d, authStatus %{coreacc:ACCAuthInfo_Status_t}d, certData %@"
- "%s: connectionUUID %@, key %@"
- "%s: connectionUUID %@, key %@, values %@"
- "%s: connectionUUID %@, properties %@"
- "%s: connectionUUID %@, supervisedTransportsRestricted %d"
- "%s: didn't find connectionUUID %@"
- "%s: didn't find endpointUUID %@"
- "%s: endpointUUID %@"
- "%s: no endpoint for endpoint %@ !!"
- "%s: no protocol endpoint for endpoint %@ !!"
- "%s: pairingDataMatch %d, bdAddrMatch %d, override %d"
- "%s: parentEndpoint %@, dataOut %@"
- "%s: parentEndpoint NULL, dataOut %@"
- "%s: protocol_authSetupStart failed"
- "%s: unable to find endpoint for %@"
- "%s: wrong protocol for endpoint %@ !!"
- "%s:%d ERROR: Endpoint not found!!!!"
- "%s:%d [%ld / %ld], call iteratorCB, %@, context %d "
- "%s:%d call iteratorCB, connection %@, context %d "
- "%s:%d call iteratorCB, endpoint %@, context %d "
- "%s:%d connection %@, iteratorCB %d, context %d, forWrite %d "
- "%s:%d connectionUUID %@, deprecated, should use acc_manager_callbackForConnection"
- "%s:%d endpoint %@, iteratorCB %d, context %d, forWrite %d "
- "%s:%d endpointUUID %@, deprecated, should use acc_manager_callbackForEndpoint"
- "%s:%d iteratorCB %d, context %d, forWrite %d "
- "%s:%d iteratorCalled %d "
- "-> accessoryInfoOverrides: %@"
- "-[ACCTransportPluginManager setAuthenticationStatus:andCertificateData:authCTA:forConnectionWithUUID:]_block_invoke"
- "-[ACCTransportPluginManager setProperties:forConnectionWithUUID:]_block_invoke"
- "-[ACCTransportPluginManager setSupervisedTransportsRestricted:forConnectionWithUUID:]_block_invoke"
- "-[ACCTransportServerRemote accessoryInfoForConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote accessoryInfoForConnectionWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote addToDictionaryProperty:values:forConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote addToDictionaryProperty:values:forConnectionWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote appendToArrayProperty:values:forConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote appendToArrayProperty:values:forConnectionWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote authStatusForConnectionWithUUID:authType:withReply:]"
- "-[ACCTransportServerRemote authStatusForConnectionWithUUID:authType:withReply:]_block_invoke"
- "-[ACCTransportServerRemote identifierForConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote identifierForConnectionWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote identifierForEndpointWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote isConnectionAuthenticatedForUUID:withReply:]"
- "-[ACCTransportServerRemote isConnectionAuthenticatedForUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote propertiesForConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote propertiesForConnectionWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote propertiesForEndpointWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote removeProperty:forConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote removeProperty:forConnectionWithUUID:withReply:]_block_invoke"
- "-[ACCTransportServerRemote setConnectionAuthenticated:state:]"
- "-[ACCTransportServerRemote setConnectionAuthenticated:state:]_block_invoke"
- "-[ACCTransportServerRemote setProperties:forConnectionWithUUID:withReply:]"
- "-[ACCTransportServerRemote setProperties:forConnectionWithUUID:withReply:]_block_invoke"
- "-[PlatformIAPDBridge _handleAuthenticationState:forPortID:certData:]"
- "4#"
- "<ACCConnection_t: %@; connectionType: [%s]; identifier: %@; dataOutHandler: %s; creationTimestampMS: %llu; durationMS: %llu; numEndpoints: %ld; authenticated: %s; accessoryInfo: %s; numProperties: %ld; published: %s>"
- "<ACCEndpoint_t: %@; parentConnectionUUID: %@; transportType: [%s]; protocol: [%s]; identifier: %@; creationTimestampMS: %llu; durationMS: %llu; protocolEndpoint: %s; accessoryInfo: %s; numAccessoryInfoOverrides: %ld; numProperties: %ld, published: %s>"
- "@32@0:8@16^{?=^{ACCEndpoint_s}^{__CFString}^{__CFString}@^{iAP2LinkRunLoop_st}{iAP2PacketSYNData_st=CCCCSSSCCS[5C][5C]C[5C][5{?=CCCB}]}iB^{iAP2Packet_st}^{iAP2MsgParser_st}{iAP2Msg_t_st=*III**^?^vB^?}*[29^v]^vB^vd}24"
- "Added connection endpoint: %@"
- "Attempt to modify accessoryInfo on connection not created by client, ignore! connectionUUID %@"
- "Attempt to modify properties on endpoint not created by client, ignore! endpointUUID %@"
- "Attempt to modify properties on endpoint of connection but cannot get connection for endpointUUID %@"
- "Attempt to modify properties on endpoint of connection not created by client, ignore! endpointUUID %@, connectionUUID %@"
- "B24@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}16"
- "B24@?0^{ACCConnection_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16"
- "B24@?0^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}8^v16"
- "B32@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}16@24"
- "Check for WirelessCTA: Found match! donor %@, receiver %@, override %d"
- "Closing EA session for endpoint %@..."
- "Closing EA session for iAP2 endpoint %@..."
- "Connection %@ already published, publish endpoint of protocol %{coreacc:ACCEndpoint_Protocol_t}d /  %{coreacc:ACCEndpoint_Protocol_t}d."
- "Create new endpoint for connection %@, transport %{coreacc:ACCEndpoint_TransportType_t}d, protocol %{coreacc:ACCEndpoint_Protocol_t}d."
- "Disabled lockout for all transport types!"
- "Disabled lockout for transport type: %{coreacc:ACCEndpoint_TransportType_t}d!"
- "ERROR: Found more than one passthroughAccessory endpoint (%@) for passthroughDevice endpoint %@ !"
- "ERROR: Found more than one passthroughDevice endpoint (%@) for passthroughAccessory endpoint %@ !"
- "Enabled lockout for transport type: %{coreacc:ACCEndpoint_TransportType_t}d for %d seconds!"
- "Endpoint %@ isPassThrough(passthroughMode=%d)"
- "Endpoint %@ passthroughMode(0=NO,1=Acc,2=Dev) %d -> %d"
- "Endpoint destroyed during logging"
- "Error setting AccessoryPowerMode for endpoint: %@"
- "Failed to register HID interface! (connectionUUID: %@, endpointUUID: %@, componentID: %d)"
- "Failed to unregister HID interface! (connectionUUID: %@, endpointUUID: %@, componentID: %d)"
- "Finished updating EADictionary... (new: %@)"
- "Found passthroughAccessory endpoint %@ for passthroughDevice endpoint %@"
- "Found passthroughDevice endpoint %@ for passthroughAccessory endpoint %@"
- "Have %ld endpoints to parse"
- "Have first EA session requiring sleep assertion"
- "Invalid endpointUUID! %@ - %@"
- "Invalid transport type: %{coreacc:ACCEndpoint_TransportType_t}d or timeout value: %u!"
- "Invalid transport type: %{coreacc:ACCEndpoint_TransportType_t}d!"
- "LOG; %.6f; %@; %s; %@%@; %s; data(len=%d)="
- "LOG; %.6f; %@; %s; %@%@; SNTP BD Cmd %#04x; packetLen %#04x; data(len=%d)="
- "LOG; %.6f; %@; %s; %@%@; len=0x%04x; control=0x%02x; seq=0x%02x; ack=0x%02x; session=0x%02x; hdrChk=0x%04x; payload(len=%d chk=0x%04x)="
- "LOG; %.6f; %@; %s; %@%@; sessionID %u; %s; data(len=%d)="
- "LOG; %.6f; %@; %s; %@%@; sessionID %u; msgID %#04x; ctl0 %#04x; ctl1 %#04x; payloadLen %d; data(len=%d)="
- "LOG; %.6f; %@; %s; %@%@; sessionUUID %@; data(len=%d)="
- "Lockout for transport type: %{coreacc:ACCEndpoint_TransportType_t}d was extended to %d seconds!"
- "No DataOutHandler!!! - Unable to send %ld bytes of outgoing data for connectionUUID %@ endpointUUID %@"
- "No Passthrough pair, ignore %ld bytes of data for endpoint %@"
- "No endpoint for %@!"
- "No iAP2 endpoint found!"
- "Opening EA session for endpoint %@..."
- "Passthrough %ld bytes of data for endpoint %@ to %@"
- "PretendWirelessCTAMatch"
- "QiAuth publish: transportType %{coreacc:ACCEndpoint_TransportType_t}d"
- "QiAuth publish: transportType %{coreacc:ACCEndpoint_TransportType_t}d, start protocol!!!"
- "Received Set Transport Lockout message (0x%04X)!"
- "Removing %ld endpoint(s) for connection %@..."
- "Removing connection endpoint: %@..."
- "Reset device UUID: %@"
- "SecureTunnelHandler endpoint: %@, data:%@"
- "Sending outgoing EA data to endpointUUID %@"
- "Skip sending outgoingEADataFromClientAvailable to endpointUUID %@, iAP2_Initialized=%s"
- "Skipping invokeHandler (handlerType: %d) for %{coreacc:ACCEndpoint_Protocol_t}d endpoint %@ != %@ !!!"
- "Skipping invokeHandler (handlerType: %d) for %{coreacc:ACCEndpoint_Protocol_t}d endpoint %@!"
- "T56 publish: transportType %{coreacc:ACCEndpoint_TransportType_t}d, parentEndpointUUID %@, after delay, call t56_protocol_start"
- "T@\"<ACCPowerSiphoningControlDelegate>\",R,N,V_delegate"
- "There are now %ld endpoint(s)."
- "Transport %{coreacc:ACCEndpoint_TransportType_t}d is locked out for %u more second(s), dropping %ld bytes of incoming data for endpoint %@!"
- "Transport %{coreacc:ACCEndpoint_TransportType_t}d is locked out for %u more second(s), dropping %ld bytes of outgoing data for endpoint %@!"
- "Trying to close EA session for uninitialized iAP2 endpoint"
- "Updating EADictionary... (old: %@)"
- "[#EventLogger] %s: didn't find connectionUUID %@, or accInfo for connection"
- "[#EventLogger] Calling auth passed for inductive via retry data"
- "[#EventLogger] Calling auth passed via retry data"
- "[#EventLogger] Filtered FeaturesMask: 0x%08x"
- "[#EventLogger] Performing retry in 30 seconds"
- "[#EventLogger] Performing retry in 5 seconds"
- "[#EventLogger] True FeaturesMask: 0x%08x"
- "[#EventLogger] Unable to create %@ analytic. No connection found"
- "[#EventLogger] iAP1 lingoes reported for endpoint: %@ (connection %@)"
- "[#Power] Not sending EA Power Update: iap2initialized = %s, protocol = %{coreacc:ACCEndpoint_Protocol_t}d"
- "[#Power] addAccessoryForEndpointUID: endpointUID %@, updateTypesBitMask %llx, oldUpdateTypesBitmask %llx"
- "[#SleepAssertions] Creating sleep assertion for UUID %@..."
- "[#iapd Bridge] %s: didn't find endpointUUID %@"
- "[#iapd Bridge] Dropping iAP1 bytes over %{coreacc:ACCEndpoint_TransportType_t}d!"
- "[#iapd Bridge] Ignoring failed auth state for endpoint type %{coreacc:ACCEndpoint_TransportType_t}d, matching iaptransportd behavior"
- "[#iapd Bridge] enabling authentication passed? %d for USB Host"
- "[#iapd Bridge] found endpointUUID %@ for portID %llu, handle port lockout"
- "[#iapd Bridge] ignoring authenticated flag for iAP1 bridge"
- "[FindMy] platform_connectionInfo_provisionPairing"
- "__PASSTHROUGH_ACCESSORY__"
- "__PASSTHROUGH_DEVICE__"
- "_acc_manager_checkForInductiveCTA_checkMatch"
- "_acc_manager_checkForWirelessCTA_checkMatch"
- "_acc_manager_getEndpointWithUUID_unsafe"
- "_addConnection"
- "_addEndpoint"
- "_addSleepAssertionForUUID:"
- "_checkForAdapterInfo"
- "_convertNVMReadResponse: Unsupported read response ID: %d"
- "_genericMFi_endpoint_handlePropertiesDidChange_block_invoke"
- "_mfi4Auth_endpoint_firstUnlockHandler endpoint Found: %@"
- "_mfi4Auth_endpoint_handlePropertiesDidChange: sendAuthSetupStart"
- "_tryWRLock"
- "accAuthProtocol sendAuthSetupStart: no endpoint(%d) or wrong protocol(%d) or no protocolEndpoint(%d) for endpointUUID %@ !!"
- "accAuthProtocol: endpoint is ACCAuthProtocol"
- "acc_connection_destroy: call acc_manager_checkForInductiveCTA"
- "acc_connection_destroy: call acc_manager_checkForWirelessCTA"
- "acc_connection_getPairingStatus"
- "acc_connection_getPairingStatus: %d"
- "acc_connection_isAuthenticatedForAppMatchLaunch"
- "acc_connection_isAuthenticatedForInductivePowerIn"
- "acc_connection_setAuthStatus: %@, authType %{coreacc:ACCAuthInfo_Type_t}d, authStatus %{coreacc:ACCAuthInfo_Status_t}d"
- "acc_connection_setAuthStatus: auth passed for BT connection, call acc_manager_checkForWirelessCTA"
- "acc_connection_setAuthStatus: auth passed for NFC connection, call acc_manager_checkForInductiveCTA"
- "acc_connection_setPairingStatus"
- "acc_connection_setProperties: call acc_manager_checkForInductiveCTA"
- "acc_connection_setProperties: call acc_manager_checkForWirelessCTA"
- "acc_connection_setProperty: call acc_manager_checkForInductiveCTA"
- "acc_connection_setProperty: call acc_manager_checkForWirelessCTA"
- "acc_endpoint_addToDictionaryProperty"
- "acc_endpoint_appendToArrayProperty"
- "acc_endpoint_publish"
- "acc_endpoint_removeProperty"
- "acc_endpoint_setProperties"
- "acc_endpoint_setProperty"
- "acc_manager_callbackForConnection"
- "acc_manager_callbackForEndpoint"
- "acc_manager_copyAdapterConnectionUUIDForConnection"
- "acc_manager_copyConnectionsThroughAdapter"
- "acc_manager_copyEndpointUUIDsForConnection"
- "acc_manager_disableLockoutForAllTransportTypes"
- "acc_manager_disableLockoutForTransportType"
- "acc_manager_enableLockoutForTransportType"
- "acc_manager_getConnectionWithUUID"
- "acc_manager_getEndpointWithUUID"
- "acc_manager_iterateAllConnections"
- "acc_manager_iterateAllEndpoints"
- "acc_manager_removeConnectionWithUUID"
- "acc_manager_removeEndpointWithUUID"
- "addAccessoryForEndpointUID:andBitmask:andOldBitmask:"
- "after open EA session, gWiredEASessionUUIDs count = %lu"
- "blePairing resolvedAccessoryBTAddress: malloc failed for %@"
- "com.apple.acc.manager.asyncQ"
- "com.apple.accessories.endpoint.iap1.lingoesSupported"
- "configStream publish: transportType %{coreacc:ACCEndpoint_TransportType_t}d"
- "configStream publish: wasPublished = %d, accInfoDict = %@ "
- "connectionEndpoints = null!"
- "connectionInfo accessoryConnectionAttached: %@ type=%{coreacc:ACCConnection_Type_t}d"
- "connectionInfo accessoryConnectionInfoPropertyChanged: %@"
- "connectionInfo accessoryEndpointAttached: %@ - %@ transport=%{coreacc:ACCEndpoint_TransportType_t}d protocol=%{coreacc:ACCEndpoint_Protocol_t}d"
- "connectionInfo accessoryEndpointInfoPropertyChanged: %@ - %@"
- "connectionInfo accessoryEndpointProtocolUpdate: %@ - %@ protocol=%{coreacc:ACCEndpoint_Protocol_t}d"
- "connectionInfo sendDataForEndpoint: %@ - %@, %ld bytes Failed! "
- "connectionSupportsEA = %s"
- "createConnectionWithType: %{coreacc:ACCConnection_Type_t}d andIdentifier: %@ withReply: , connectionUUID = %@, connectionUUIDs = %@"
- "createEndpointWithTransportType:  %{coreacc:ACCEndpoint_TransportType_t}d andProtocol: %{coreacc:ACCEndpoint_Protocol_t}d andIdentifier: %@ forConnectionWithUUID: %@ withReply: , endpointUUID = %@, connectionUUIDs = %@"
- "cursorInformationHandler %@, failed to get hint from p->hint (%@)"
- "cursorInformationHandler %@, failed to get label from p->label (%@)"
- "cursorInformationHandler %@, failed to get value from p->value (%@)"
- "endpoint %@ is not a passthrough endpoint"
- "endpoint_requestNvmErasePublicKey: no endpoint for endpoint!!"
- "findWirelessCTAReceiverCapableConnection: prefer %@ over %@ (cached pairing populated on candidate; prior empty candidate should have been cleaned up)"
- "genericMFi_util_SetOrRemoveProperty_block_invoke"
- "handleAuthSessionClose: Keep session open for %llds"
- "informationHandler %@, cursorInfoRequestedMask=%xh, p (validMask=%xh label=%@ value=%@ hint=%@ traitsMask=%llxh)"
- "informationHandler %@, infoRequestedMask=%xh, p (validMask=%xh volume=%f rate=%f enabled=%d)"
- "informationHandler %@, parm type=%d"
- "initWithEndpointUID:andBitmask:andOldBitmask:"
- "initWithInt:"
- "invokeHandler returned false (handlerType: %d) for %{coreacc:ACCEndpoint_Protocol_t}d endpoint %@!"
- "lingoesBitmask"
- "oobPairing_endpoint_processIncomingData: call acc_manager_checkForWirelessCTA"
- "platform_analytics_connectionPassedAuthForProtocol"
- "platform_connectionInfo_beginUserKeyErase"
- "platform_connectionInfo_beginUserKeyErase: unexpected protocol: %s"
- "platform_connectionInfo_beginVendorKeyErase"
- "platform_connectionInfo_beginVendorKeyErase: unexpected protocol: %s"
- "platform_connectionInfo_cancelUserKeyErase"
- "platform_connectionInfo_cancelUserKeyErase: unexpected protocol: %s"
- "platform_connectionInfo_cancelVendorKeyErase"
- "platform_connectionInfo_cancelVendorKeyErase: unexpected protocol: %s"
- "platform_connectionInfo_continueUserKeyErase"
- "platform_connectionInfo_continueUserKeyErase: unexpected protocol: %s"
- "platform_connectionInfo_continueVendorKeyErase"
- "platform_connectionInfo_continueVendorKeyErase: unexpected protocol: %s"
- "platform_connectionInfo_copyUserPrivateKey"
- "platform_connectionInfo_copyUserPrivateKey: unexpected protocol: %s"
- "platform_connectionInfo_getAccessoryUserName"
- "platform_connectionInfo_getAccessoryUserName: unexpected protocol: %s"
- "platform_connectionInfo_getPairingStatus: unexpected protocol: %s"
- "platform_connectionInfo_getPrivateNvmKeyValues"
- "platform_connectionInfo_getPrivateNvmKeyValues: unexpected protocol: %s"
- "platform_connectionInfo_getPublicNvmKeyValues: !pEndpoint"
- "platform_connectionInfo_getPublicNvmKeyValues: unexpected protocol: %s"
- "platform_connectionInfo_provisionPairing: unexpected protocol: %s"
- "platform_connectionInfo_resetPairing: !pEndpoint"
- "platform_connectionInfo_resetPairing: destroyingEndpoint"
- "platform_connectionInfo_resetPairing: mfi4Auth_endpoint_erasePairing"
- "platform_connectionInfo_resetPairing: unexpected protocol: %s"
- "platform_connectionInfo_setAccessoryUserName"
- "platform_connectionInfo_setAccessoryUserName: unexpected protocol: %s"
- "platform_connectionInfo_setPrivateNvmKeyValues"
- "platform_connectionInfo_setPrivateNvmKeyValues: unexpected protocol: %s"
- "platform_connectionInfo_setPublicNvmKeyValues"
- "platform_connectionInfo_setPublicNvmKeyValues: unexpected protocol: %s"
- "qiID"
- "setAccessoryInfo, endpointUUID %@, accInfo %@"
- "setProperties, endpointUUID %@, properties %@"
- "setupPassthroughPair (Accessory) for endpoint %@, endpointCount=%ld"
- "setupPassthroughPair (Accessory) for endpoint %@, index= %d / %ld, %@ passthroughMode=%d"
- "setupPassthroughPair (Device) for endpoint %@, endpointCount=%ld"
- "setupPassthroughPair (Device) for endpoint %@, index= %d / %ld, %@ passthroughMode=%d"
- "setupPassthroughPair for endpoint %@, validPassthroughPair=%d passthroughMode=%d"
- "v24@0:8^{?=^{ACCEndpoint_s}^{__CFString}^{__CFString}@^{iAP2LinkRunLoop_st}{iAP2PacketSYNData_st=CCCCSSSCCS[5C][5C]C[5C][5{?=CCCB}]}iB^{iAP2Packet_st}^{iAP2MsgParser_st}{iAP2Msg_t_st=*III**^?^vB^?}*[29^v]^vB^vd}16"
- "v24@0:8^{?=^{ACCEndpoint_s}^{__CFString}^{__CFString}B@i^{__CFArray}^{__CFData}^{__CFArray}^{__CFArray}^{__CFDictionary}C@[3^v]}16"
- "v24@0:8^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}16"
- "v32@0:8@16^{ACCEndpoint_s=^{ACCConnection_s}^{__CFString}^{__CFString}ii^{__CFString}Q^{?}^v^{?}^{__CFDictionary}^{__CFDictionary}BBiB^{__CFString}^{__CFString}^?@@?BB{_opaque_pthread_mutex_t=q[56c]}}24"
- "v40@0:8@16Q24Q32"
- "wpcPolicyExt"

```
