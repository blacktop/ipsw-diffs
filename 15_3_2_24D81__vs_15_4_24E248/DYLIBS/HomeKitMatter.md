## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x13f65c
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x88bc
-  __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x27dc
-  __TEXT.__cstring: 0x5b8f
-  __TEXT.__oslogstring: 0x22cfa
-  __TEXT.__ustring: 0x68
+1278.5.13.4.2
+  __TEXT.__text: 0x14c63c
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x9acc
+  __TEXT.__const: 0x150
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x2ab0
-  __TEXT.__objc_classname: 0xfba
-  __TEXT.__objc_methname: 0x2169f
-  __TEXT.__objc_methtype: 0x35f0
-  __TEXT.__objc_stubs: 0x14220
-  __DATA_CONST.__got: 0x8f8
-  __DATA_CONST.__const: 0xa58
-  __DATA_CONST.__objc_classlist: 0x368
+  __TEXT.__gcc_except_tab: 0x2aa0
+  __TEXT.__cstring: 0x5fbb
+  __TEXT.__oslogstring: 0x236b8
+  __TEXT.__ustring: 0x68
+  __TEXT.__unwind_info: 0x2c88
+  __TEXT.__objc_classname: 0x1338
+  __TEXT.__objc_methname: 0x23078
+  __TEXT.__objc_methtype: 0x377b
+  __TEXT.__objc_stubs: 0x148c0
+  __DATA_CONST.__got: 0x920
+  __DATA_CONST.__const: 0xb10
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e48
+  __DATA_CONST.__objc_selrefs: 0x64a0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x400
-  __AUTH_CONST.__const: 0x4c70
-  __AUTH_CONST.__cfstring: 0x6220
-  __AUTH_CONST.__objc_const: 0xeb10
-  __AUTH_CONST.__objc_intobj: 0x1290
+  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__const: 0x4fc0
+  __AUTH_CONST.__cfstring: 0x6580
+  __AUTH_CONST.__objc_const: 0xe9e0
+  __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x2210
-  __DATA.__objc_ivar: 0x9f4
-  __DATA.__data: 0xc00
-  __DATA.__bss: 0x3c0
+  __AUTH.__objc_data: 0x2710
+  __DATA.__objc_ivar: 0xa58
+  __DATA.__data: 0xd80
+  __DATA.__bss: 0x498
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi
   - /System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation
+  - /System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit
   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/Versions/A/HomeKitFeatures
   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/Versions/A/HomeKitMetrics
   - /System/Library/PrivateFrameworks/MatterPlugin.framework/Versions/A/MatterPlugin
+  - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/Versions/A/NetAppsUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 008E436A-6129-3A74-AE21-A75A0BDDDF08
-  Functions: 3978
-  Symbols:   9409
-  CStrings:  8542
+  UUID: 40716A52-897E-34F6-8101-4E8624ACA9BE
+  Functions: 4116
+  Symbols:   9865
+  CStrings:  8799
 
Symbols:
+ +[HMMTRAccessoryServer propagateCharactersticValuesToAccessory:]
+ +[HMMTRAccessoryServerBuilder updateAccessory:withServices:]
+ +[HMMTRDoorLockClusterAPIRouter aliroClearCredentialParamsFromParams:flow:]
+ +[HMMTRDoorLockClusterAPIRouter arrayOfDataFromRead:]
+ +[HMMTRFabricDataCreator fabricDataForRootKeyPair:opKeyPair:fabricID:residentNodeID:overridingRCAC:ipk:]
+ +[HMMTRFabricDataCreator logCategory]
+ +[HMMTRFabricRandomV0KeyStore logCategory]
+ +[HMMTRFabricV0KeyStore logCategory]
+ +[HMMTRFabricVoidV0DataStore logCategory]
+ +[HMMTRFeatures disableFeatureMatterRVCForTests]
+ +[HMMTRFeatures enableFeatureMatterRVCForTests]
+ +[HMMTRFeatures unsetFeatureMatterRVCForTests]
+ +[HMMTRHAPServiceDescription descriptionsDictionaryFromAccessoryInfo:]
+ +[HMMTRMultiFabricDataStoreQuery logCategory]
+ +[HMMTRMultiFabricDataStoreUpdate logCategory]
+ +[HMMTROperationalCertificateIssuer logCategory]
+ +[HMMTRProtocolMap mapCarbonMonoxideDetected:]
+ +[HMMTRProtocolMap mapSmokeDetected:]
+ +[HMMTRStorage knownFabricInStorage:fabricID:keyPair:controllerNodeID:rootCertificate:]
+ +[HMMTRSyncClusterCarbonDioxideConcentrationMeasurement logCategory]
+ +[HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement logCategory]
+ +[HMMTRSyncClusterDoorLock dataOfReadValue:]
+ +[HMMTRSyncClusterDoorLock sortedArrayOfData:]
+ +[HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement logCategory]
+ +[HMMTRSyncClusterOzoneConcentrationMeasurement logCategory]
+ +[HMMTRSyncClusterPM10ConcentrationMeasurement logCategory]
+ +[HMMTRSyncClusterPM25ConcentrationMeasurement logCategory]
+ +[HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement logCategory]
+ +[HMMTRUtilities supportedLinkLayerTypesContainsEthernet:]
+ +[HMMTRUtilities supportedLinkLayerTypesContainsThread:]
+ +[HMMTRUtilities supportedLinkLayerTypesContainsWiFi:]
+ +[MTRCertificates(HMMTRAdditions) certificate:isCompatibleWithAnotherControllerCertificate:]
+ +[MTRCertificates(HMMTRAdditions) publicKeyDataFromCertificate:]
+ -[HMMCredentialKey .cxx_destruct]
+ -[HMMCredentialKey copyWithZone:]
+ -[HMMCredentialKey credentialIndex]
+ -[HMMCredentialKey credentialStruct]
+ -[HMMCredentialKey credentialType]
+ -[HMMCredentialKey hash]
+ -[HMMCredentialKey initWithCredentialParams:]
+ -[HMMCredentialKey initWithCredentialType:andCredentialIndex:]
+ -[HMMCredentialKey isEqual:]
+ -[HMMCredentialKey setCredentialIndex:]
+ -[HMMCredentialKey setCredentialType:]
+ -[HMMTRAccessoryConnectionRequest fabricUUID]
+ -[HMMTRAccessoryServer _deviceInternalStateChanged:]
+ -[HMMTRAccessoryServer _handleEventReport:]
+ -[HMMTRAccessoryServer _legacyHMDHAPAccessoryDelegateShouldHandleEvent:]
+ -[HMMTRAccessoryServer addReportObserver:]
+ -[HMMTRAccessoryServer configureDefaultRequiresThreadRouter]
+ -[HMMTRAccessoryServer endpointToDeviceTypesMap]
+ -[HMMTRAccessoryServer fabricUUID]
+ -[HMMTRAccessoryServer handleRemoveFromBrowser]
+ -[HMMTRAccessoryServer markAsSubscribed]
+ -[HMMTRAccessoryServer markForResubscription]
+ -[HMMTRAccessoryServer mtrBaseDeviceWithNodeID:controller:]
+ -[HMMTRAccessoryServer removeReportObserver:]
+ -[HMMTRAccessoryServer reportObservers]
+ -[HMMTRAccessoryServer setEndpointToDeviceTypesMap:]
+ -[HMMTRAccessoryServer setFabricUUID:]
+ -[HMMTRAccessoryServer setShouldReestablishSubscription:]
+ -[HMMTRAccessoryServer shouldReestablishSubscription]
+ -[HMMTRAccessoryServer(DiagnosticsInternal) _getThreadHardwareAddressFromReadValue:]
+ -[HMMTRAccessoryServerBrowser _abortAllOperationsForFabricUUID:reason:]
+ -[HMMTRAccessoryServerBrowser _connectPendingFabricConnectionsForTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _handleClientsRemovedWithFabricUUID:updateConnectionIdleTimeout:reason:]
+ -[HMMTRAccessoryServerBrowser _handleDeviceActivityStateChange:reason:]
+ -[HMMTRAccessoryServerBrowser _handleKeybagLockStateNotification]
+ -[HMMTRAccessoryServerBrowser _handleLogoutNotification]
+ -[HMMTRAccessoryServerBrowser _isDeviceIDPaired:nodeID:targetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _isNodeIDPaired:targetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:targetFabricUUID:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]
+ -[HMMTRAccessoryServerBrowser _removeOrSuspendAllActiveClientsWithCurrentFabricUUID:reason:]
+ -[HMMTRAccessoryServerBrowser _resumeSuspendedActiveClients]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateIfNotFabricUUID:rediscoverAccessories:]
+ -[HMMTRAccessoryServerBrowser _stopSystemCommissionerFabricWithReason:]
+ -[HMMTRAccessoryServerBrowser _suspendOperationsForTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser addFabricWithActiveClientForTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser addSuspendedActiveSecondaryClientFabricUUIDs:]
+ -[HMMTRAccessoryServerBrowser appleHomeFabricWithTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser clearOperationalFabricDataForTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser clearSuspendedActiveSecondaryClientFabricUUIDs]
+ -[HMMTRAccessoryServerBrowser currentFabricUUID]
+ -[HMMTRAccessoryServerBrowser fabricDataForPairingTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricData:adminCAT:opCAT:completionHandler:]
+ -[HMMTRAccessoryServerBrowser getNumberOfAccessoryServersForFabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser handlePairingCompletionForAccessoryWithNodeID:targetFabricUUID:fabricID:vendorID:productID:configNumber:category:topology:]
+ -[HMMTRAccessoryServerBrowser handlePairingForThreadAccessoryWithTargetFabricUUID:nodeID:]
+ -[HMMTRAccessoryServerBrowser lockStateKBNotificationRegistered]
+ -[HMMTRAccessoryServerBrowser lockStateKBNotificationRegistrationToken]
+ -[HMMTRAccessoryServerBrowser logoutNotificationRegistered]
+ -[HMMTRAccessoryServerBrowser logoutNotificationRegistrationToken]
+ -[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:targetFabricUUID:completionHandler:]
+ -[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]
+ -[HMMTRAccessoryServerBrowser removeActiveClientWithFabricUUID:updateConnectionIdleTimeout:reason:]
+ -[HMMTRAccessoryServerBrowser removeActiveSecondaryClientWithFabricUUID:updateConnectionIdleTimeout:reason:]
+ -[HMMTRAccessoryServerBrowser runAfterCommissioningToTargetFabricUUID:controllerSetUpBlock:]
+ -[HMMTRAccessoryServerBrowser setCurrentFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setLockStateKBNotificationRegistered:]
+ -[HMMTRAccessoryServerBrowser setLockStateKBNotificationRegistrationToken:]
+ -[HMMTRAccessoryServerBrowser setLogoutNotificationRegistered:]
+ -[HMMTRAccessoryServerBrowser setLogoutNotificationRegistrationToken:]
+ -[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:forTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setPairingTargetFabricData:targetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setSuspendedActiveClientFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser suspendedActiveClientFabricUUID]
+ -[HMMTRAccessoryServerBrowser suspendedActiveSecondaryClientFabricUUIDs]
+ -[HMMTRAccessoryServerBrowser systemCommissionerFabricUUID]
+ -[HMMTRAccessoryServerBrowser updateAccessoryACLForFabric:]
+ -[HMMTRAliroVersion .cxx_destruct]
+ -[HMMTRAliroVersion bleAdvertisingVersion]
+ -[HMMTRAliroVersion bleUWBSupportedVersions]
+ -[HMMTRAliroVersion expeditedTransactionSupportedVersions]
+ -[HMMTRAliroVersion setBleAdvertisingVersion:]
+ -[HMMTRAliroVersion setBleUWBSupportedVersions:]
+ -[HMMTRAliroVersion setExpeditedTransactionSupportedVersions:]
+ -[HMMTRControllerFactory _disableNormalOperation:]
+ -[HMMTRControllerFactory mtrPluginDeviceControllerRegistry]
+ -[HMMTRControllerFactory mtrPluginSharedInstance]
+ -[HMMTRControllerFactory restartNormalOperation]
+ -[HMMTRControllerParameters rootPublicKey]
+ -[HMMTRControllerParameters setRootPublicKey:]
+ -[HMMTRControllerWrapper deregisterRevokeHandlersWithQueue:]
+ -[HMMTRControllerWrapper didSendRevokeAvailableOnResume]
+ -[HMMTRControllerWrapper setDidSendRevokeAvailableOnResume:]
+ -[HMMTRDescriptorClusterManager _queryAttributeValueFromClusterAtCHIPEndpoint:device:attributeValuesToCheckDict:attributeValuesSupportedDict:attributeValuesRetrievedDict:callbackQueue:clusterClassName:completionHandler:]
+ -[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint:device:callbackQueue:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:attributeValuesSupportedDict:attributeValuesRetrievedDict:deviceTopology:server:lastError:completionHandler:]
+ -[HMMTRDescriptorClusterManager hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:]
+ -[HMMTRDeviceTopology storeForNodeId:server:]
+ -[HMMTRDoorLockClusterAPIRouter appendAliroCredentialsToUser:aliroCredentials:]
+ -[HMMTRDoorLockClusterAPIRouter clearCredentialWithParams:flow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter device]
+ -[HMMTRDoorLockClusterAPIRouter doorLock]
+ -[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:startingAtIndex:credentials:flow:]
+ -[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter initWithDoorLock:device:queue:]
+ -[HMMTRDoorLockClusterAPIRouter numberOfAliroDeviceKeyCredentialsSupportedWithFlow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter numberOfAliroIssuerKeyCredentialsSupportedWithFlow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter readAttributeAliroBLEAdvertisingVersionWithFlow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter readAttributeAliroExpeditedTransactionSupportedProtocolVersionsWithFlow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter readAttributeAliroSupportedBLEUWBProtocolVersionsWithFlow:completion:]
+ -[HMMTRFabricConnectionRequest fabricUUID]
+ -[HMMTRFabricConnectionRequest initWithQueue:browser:fabricUUID:systemCommissionerFabric:]
+ -[HMMTRFabricControllerStore cachedWrapperWithTargetFabricUUID:]
+ -[HMMTRFabricControllerStore removeTargetFabricUUID:]
+ -[HMMTRFabricControllerStore updateAllTargetFabricUUIDs:]
+ -[HMMTRFabricDataCreator .cxx_destruct]
+ -[HMMTRFabricDataCreator chipStorageDelegate]
+ -[HMMTRFabricDataCreator generateIPK]
+ -[HMMTRFabricDataCreator initWithCHIPStorageDelegate:keychainDelegate:]
+ -[HMMTRFabricDataCreator keychainDelegate]
+ -[HMMTRFabricDataCreator logIdentifier]
+ -[HMMTRFabricDataCreator newFabricData]
+ -[HMMTRFabricDataCreator setChipStorageDelegate:]
+ -[HMMTRFabricDataCreator setKeychainDelegate:]
+ -[HMMTRFabricDataSnapshot initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:residentOperationalKeyPair:residentOperationalCert:]
+ -[HMMTRFabricDataSnapshot residentOperationalCert]
+ -[HMMTRFabricDataSnapshot residentOperationalKeyPair]
+ -[HMMTRFabricRandomV0KeyStore .cxx_destruct]
+ -[HMMTRFabricRandomV0KeyStore init]
+ -[HMMTRFabricRandomV0KeyStore nocSigner]
+ -[HMMTRFabricRandomV0KeyStore ownerSharedOperationalKeyPair]
+ -[HMMTRFabricRandomV0KeyStore updateNocSigner:ownerSharedOperationalKeyPair:]
+ -[HMMTRFabricV0KeyStore forceUpdateNocSigner:ownerSharedOperationalKeyPair:]
+ -[HMMTRFabricV0KeyStore nocSigner]
+ -[HMMTRFabricV0KeyStore ownerSharedOperationalKeyPair]
+ -[HMMTRFabricV0KeyStore updateNocSigner:ownerSharedOperationalKeyPair:]
+ -[HMMTRFabricVoidV0DataStore fabricID]
+ -[HMMTRFabricVoidV0DataStore identifier]
+ -[HMMTRFabricVoidV0DataStore keyValueStore]
+ -[HMMTRFabricVoidV0DataStore updateKeyValueStoreWithEntries:]
+ -[HMMTRIdentifyDevice bridgeIdentifyEndpointWithAggregatorEndpoint:]
+ -[HMMTRIdentifyDevice identifyBridgeWithAggregatorEndpoint:completionHandler:]
+ -[HMMTRIdentifyDevice logIdentifier]
+ -[HMMTRMatterKeypair copyPublicKey]
+ -[HMMTRMatterKeypair dealloc]
+ -[HMMTRMatterKeypair initWithPrivateKeyExternalRepresentation:]
+ -[HMMTRMatterKeypair updateStorageWithPrivateKeyData:]
+ -[HMMTRMultiFabricDataStoreQuery .cxx_destruct]
+ -[HMMTRMultiFabricDataStoreQuery chipStorageDelegate]
+ -[HMMTRMultiFabricDataStoreQuery fabricDataFromV2FabricDataItem:]
+ -[HMMTRMultiFabricDataStoreQuery initWithCHIPStorageDelegate:keychainDelegate:v2FabricDataStoreDelegate:]
+ -[HMMTRMultiFabricDataStoreQuery keychainDelegate]
+ -[HMMTRMultiFabricDataStoreQuery locallyStoredFabricDataWithDataPresentInV2FabricDataStore:error:]
+ -[HMMTRMultiFabricDataStoreQuery logIdentifier]
+ -[HMMTRMultiFabricDataStoreQuery setChipStorageDelegate:]
+ -[HMMTRMultiFabricDataStoreQuery setKeychainDelegate:]
+ -[HMMTRMultiFabricDataStoreQuery setV2FabricDataStoreDelegate:]
+ -[HMMTRMultiFabricDataStoreQuery v2FabricDataStoreDelegate]
+ -[HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore fabricDataItems]
+ -[HMMTRMultiFabricDataStoreUpdate .cxx_destruct]
+ -[HMMTRMultiFabricDataStoreUpdate chipStorageContentFromFabricData:]
+ -[HMMTRMultiFabricDataStoreUpdate chipStorageDelegate]
+ -[HMMTRMultiFabricDataStoreUpdate commit]
+ -[HMMTRMultiFabricDataStoreUpdate fabricData]
+ -[HMMTRMultiFabricDataStoreUpdate initWithFabricData:chipStorageDelegate:keychainDelegate:v2FabricDataStoreDelegate:]
+ -[HMMTRMultiFabricDataStoreUpdate keychainDelegate]
+ -[HMMTRMultiFabricDataStoreUpdate logIdentifier]
+ -[HMMTRMultiFabricDataStoreUpdate v2FabricDataStoreDelegate]
+ -[HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore storeFabricData:]
+ -[HMMTROperationalCertificateIssuer commissioneeNodeID]
+ -[HMMTROperationalCertificateIssuer fabricID]
+ -[HMMTROperationalCertificateIssuer initWithRemoteDelegate:fabricID:]
+ -[HMMTROperationalCertificateIssuer initWithRootKeyPair:rootCertificate:fabricID:]
+ -[HMMTROperationalCertificateIssuer logIdentifier]
+ -[HMMTROperationalCertificateIssuer remoteDelegate]
+ -[HMMTROperationalCertificateIssuer rootKeyPair]
+ -[HMMTROperationalCertificateIssuer setCommissioneeNodeID:]
+ -[HMMTROperationalCertificateIssuer(Test) publicKeyFromCSRInfo:error:]
+ -[HMMTROperationalFabricData .cxx_destruct]
+ -[HMMTROperationalFabricData attributeDescriptions]
+ -[HMMTROperationalFabricData fabricID]
+ -[HMMTROperationalFabricData initWithRootCert:ipk:residentNodeID:operationalCert:operationalKeyPair:]
+ -[HMMTROperationalFabricData ipk]
+ -[HMMTROperationalFabricData operationalCert]
+ -[HMMTROperationalFabricData operationalKeyPair]
+ -[HMMTROperationalFabricData operationalNodeID]
+ -[HMMTROperationalFabricData residentNodeID]
+ -[HMMTROperationalFabricData rootCert]
+ -[HMMTRPerControllerStorage fabricID]
+ -[HMMTRPerControllerStorage initWithQueue:privateDataSource:]
+ -[HMMTRProtocolMap getRequiredAttributesForCharacteristic:]
+ -[HMMTRProtocolMap nativeMatterDeviceTypes]
+ -[HMMTRProtocolMap retrieveHAPCharacteristicsToCheckForRequiredAttributeValues]
+ -[HMMTRStorage fabricUUID]
+ -[HMMTRStorage ipkForTargetFabricUUID:forPairing:]
+ -[HMMTRStorage legacyNodeIDForTargetFabricUUID:]
+ -[HMMTRStorage prepareStorageForTargetFabricUUID:]
+ -[HMMTRStorage prepareStorageForTargetFabricUUID:forInitialSetup:]
+ -[HMMTRStorage setFabricUUID:]
+ -[HMMTRSyncClusterCarbonDioxideConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterCarbonDioxideConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement readAttributePluginPeakMeasuredValueWithParams:]
+ -[HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement updatedValuePluginPeakMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterDoorLock __getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:]
+ -[HMMTRSyncClusterDoorLock _addIssuerKeyData:forUserIndex:credentialType:flow:]
+ -[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]
+ -[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUserIndex:flow:]
+ -[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUserUniqueID:flow:]
+ -[HMMTRSyncClusterDoorLock _getUserAtIndex:flow:]
+ -[HMMTRSyncClusterDoorLock _readReaderConfigWithFlow:]
+ -[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:]
+ -[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]
+ -[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:]
+ -[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserIndex:flow:]
+ -[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]
+ -[HMMTRSyncClusterDoorLock cacheUserResponse:]
+ -[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]
+ -[HMMTRSyncClusterDoorLock findAllOccupiedCredentialSlotsForCredentialType:startingAtSlot:assumingTotalNumberOfSlots:occupiedSlots:flow:]
+ -[HMMTRSyncClusterDoorLock findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]
+ -[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:]
+ -[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withFlow:]
+ -[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]
+ -[HMMTRSyncClusterDoorLock getMaxPINCodeLength]
+ -[HMMTRSyncClusterDoorLock getMinPINCodeLength]
+ -[HMMTRSyncClusterDoorLock initWithDevice:endpoint:queue:accessoryServer:]
+ -[HMMTRSyncClusterDoorLock issuerCredentialForUser:flow:]
+ -[HMMTRSyncClusterDoorLock numberOfCredentialsSupportedPerUserWithFlow:]
+ -[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]
+ -[HMMTRSyncClusterDoorLock setUserUniqueIdentifierToUser:]
+ -[HMMTRSyncClusterDoorLock updateUserUniqueIDForUserIndex:userUniqueID:flow:]
+ -[HMMTRSyncClusterDoorLock userUniqueIdentifierToUser]
+ -[HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterOzoneConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterOzoneConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterPM10ConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterPM10ConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterPM25ConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterPM25ConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement readAttributePluginMeasuredValueWithParams:]
+ -[HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement updatedValuePluginMeasuredValueForAttributeReport:responseHandler:]
+ -[HMMTRThreadRadioManager _notifyThreadRadioStateChanged:nodeType:fabricUUID:]
+ -[HMMTRThreadRadioManager _startThreadRadioForSystemCommissionerFabricUUID:]
+ -[HMMTRThreadRadioManager _startThreadRadioForTargetFabricUUID:preventDisconnect:]
+ -[HMMTRThreadRadioManager _stopThreadRadioForSystemCommissionerFabricUUID:]
+ -[HMMTRThreadRadioManager _stopThreadRadioForTargetFabricUUID:]
+ -[HMMTRThreadRadioManager _updateFabricUUIDOfActiveThreadNetwork:isFabricUUIDOfSystemCommissioner:]
+ -[HMMTRThreadRadioManager fabricUUIDOfActiveThreadNetwork]
+ -[HMMTRThreadRadioManager fabricUUIDOfPendingStartPairingBlock]
+ -[HMMTRThreadRadioManager hasMatterThreadAccessoryInHomeWithFabricUUID:]
+ -[HMMTRThreadRadioManager notifyThreadRadioStateChanged:nodeType:fabricUUID:]
+ -[HMMTRThreadRadioManager overrideLocationCheckForPairingForFabricUUID:]
+ -[HMMTRThreadRadioManager setFabricUUIDOfActiveThreadNetwork:]
+ -[HMMTRThreadRadioManager setFabricUUIDOfPendingStartPairingBlock:]
+ -[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricUUID:]
+ -[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricUUID:preventDisconnect:]
+ -[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricUUID:]
+ -[HMMTRThreadRadioManager stopThreadOnUserLogout]
+ -[HMMTRThreadRadioManager stopThreadRadioForHomeWithFabricUUID:]
+ -[HMMTRThreadRadioManager stopThreadRadioForSystemCommissionerFabricUUID:]
+ -[HMMTRThreadSoftwareUpdateController isFirmwareUpdateInProgressForFabricUUID:]
+ -[HMMTRThreadSoftwareUpdateController suspendOperationsForFabricUUID:]
+ -[HMMTRVendorMetadataProduct initWithIdentifier:categoryNumber:isInvalid:]
+ -[HMMTRVendorMetadataProduct isInvalid]
+ GCC_except_table1066
+ GCC_except_table1113
+ GCC_except_table1117
+ GCC_except_table1124
+ GCC_except_table1158
+ GCC_except_table1184
+ GCC_except_table1192
+ GCC_except_table1229
+ GCC_except_table1266
+ GCC_except_table1485
+ GCC_except_table1526
+ GCC_except_table1676
+ GCC_except_table1677
+ GCC_except_table1679
+ GCC_except_table1698
+ GCC_except_table1699
+ GCC_except_table1700
+ GCC_except_table1701
+ GCC_except_table1702
+ GCC_except_table1705
+ GCC_except_table1708
+ GCC_except_table1709
+ GCC_except_table1710
+ GCC_except_table1711
+ GCC_except_table1712
+ GCC_except_table1713
+ GCC_except_table1714
+ GCC_except_table1773
+ GCC_except_table1781
+ GCC_except_table1981
+ GCC_except_table2008
+ GCC_except_table2041
+ GCC_except_table2051
+ GCC_except_table2053
+ GCC_except_table2102
+ GCC_except_table2151
+ GCC_except_table2219
+ GCC_except_table2469
+ GCC_except_table2475
+ GCC_except_table2533
+ GCC_except_table2566
+ GCC_except_table2606
+ GCC_except_table2629
+ GCC_except_table2630
+ GCC_except_table2631
+ GCC_except_table2649
+ GCC_except_table2650
+ GCC_except_table2651
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table2654
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table2668
+ GCC_except_table2670
+ GCC_except_table2689
+ GCC_except_table2704
+ GCC_except_table2710
+ GCC_except_table2723
+ GCC_except_table2726
+ GCC_except_table2730
+ GCC_except_table2742
+ GCC_except_table2746
+ GCC_except_table2748
+ GCC_except_table2765
+ GCC_except_table2771
+ GCC_except_table2778
+ GCC_except_table2791
+ GCC_except_table2844
+ GCC_except_table2845
+ GCC_except_table3202
+ GCC_except_table3203
+ GCC_except_table3206
+ GCC_except_table3212
+ GCC_except_table3215
+ GCC_except_table3229
+ GCC_except_table3245
+ GCC_except_table3304
+ GCC_except_table3305
+ GCC_except_table3330
+ GCC_except_table3331
+ GCC_except_table3367
+ GCC_except_table3375
+ GCC_except_table3394
+ GCC_except_table3397
+ GCC_except_table3435
+ GCC_except_table3439
+ GCC_except_table3455
+ GCC_except_table3457
+ GCC_except_table3480
+ GCC_except_table3540
+ GCC_except_table3584
+ GCC_except_table3601
+ GCC_except_table3627
+ GCC_except_table3633
+ GCC_except_table3648
+ GCC_except_table3649
+ GCC_except_table3654
+ GCC_except_table3661
+ GCC_except_table3700
+ GCC_except_table3720
+ GCC_except_table3773
+ GCC_except_table3778
+ GCC_except_table3781
+ GCC_except_table3916
+ GCC_except_table3919
+ GCC_except_table4033
+ GCC_except_table4038
+ GCC_except_table4044
+ GCC_except_table4048
+ GCC_except_table4072
+ GCC_except_table4095
+ GCC_except_table480
+ GCC_except_table647
+ GCC_except_table650
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table712
+ GCC_except_table752
+ GCC_except_table813
+ GCC_except_table819
+ GCC_except_table821
+ GCC_except_table823
+ GCC_except_table825
+ GCC_except_table829
+ GCC_except_table833
+ GCC_except_table838
+ GCC_except_table881
+ GCC_except_table887
+ GCC_except_table889
+ GCC_except_table995
+ OBJC_IVAR_$_HMMCredentialKey._credentialIndex
+ OBJC_IVAR_$_HMMCredentialKey._credentialType
+ OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._fabricUUID
+ OBJC_IVAR_$_HMMTRAccessoryServer._endpointToDeviceTypesMap
+ OBJC_IVAR_$_HMMTRAccessoryServer._fabricUUID
+ OBJC_IVAR_$_HMMTRAccessoryServer._reportObservers
+ OBJC_IVAR_$_HMMTRAccessoryServer._shouldReestablishSubscription
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._commissioneeAccessoryServerLock
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._controllerSetUpBlockToRunAfterCommissioning
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._currentFabricUUID
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._fabricDataPerPairingTargetFabricUUID
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._lockStateKBNotificationRegistered
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._lockStateKBNotificationRegistrationToken
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._logoutNotificationRegistered
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._logoutNotificationRegistrationToken
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._pairingTargetFabricDataLock
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._suspendedActiveClientFabricUUID
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._suspendedActiveSecondaryClientFabricUUIDs
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._systemCommissionerFabricUUID
+ OBJC_IVAR_$_HMMTRAliroVersion._bleAdvertisingVersion
+ OBJC_IVAR_$_HMMTRAliroVersion._bleUWBSupportedVersions
+ OBJC_IVAR_$_HMMTRAliroVersion._expeditedTransactionSupportedVersions
+ OBJC_IVAR_$_HMMTRControllerParameters._rootPublicKey
+ OBJC_IVAR_$_HMMTRControllerWrapper._didSendRevokeAvailableOnResume
+ OBJC_IVAR_$_HMMTRDoorLockClusterAPIRouter._device
+ OBJC_IVAR_$_HMMTRDoorLockClusterAPIRouter._doorLock
+ OBJC_IVAR_$_HMMTRFabricConnectionRequest._fabricUUID
+ OBJC_IVAR_$_HMMTRFabricDataCreator._chipStorageDelegate
+ OBJC_IVAR_$_HMMTRFabricDataCreator._keychainDelegate
+ OBJC_IVAR_$_HMMTRFabricDataSnapshot._residentOperationalCert
+ OBJC_IVAR_$_HMMTRFabricDataSnapshot._residentOperationalKeyPair
+ OBJC_IVAR_$_HMMTRFabricRandomV0KeyStore._nocSigner
+ OBJC_IVAR_$_HMMTRFabricRandomV0KeyStore._nodSigner
+ OBJC_IVAR_$_HMMTRFabricRandomV0KeyStore._ownerSharedOperationalKeyPair
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreQuery._chipStorageDelegate
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreQuery._keychainDelegate
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreQuery._v2FabricDataStoreDelegate
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreUpdate._chipStorageDelegate
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreUpdate._fabricData
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreUpdate._keychainDelegate
+ OBJC_IVAR_$_HMMTRMultiFabricDataStoreUpdate._v2FabricDataStoreDelegate
+ OBJC_IVAR_$_HMMTROperationalCertificateIssuer._commissioneeNodeID
+ OBJC_IVAR_$_HMMTROperationalCertificateIssuer._fabricID
+ OBJC_IVAR_$_HMMTROperationalCertificateIssuer._remoteDelegate
+ OBJC_IVAR_$_HMMTROperationalCertificateIssuer._rootKeyPair
+ OBJC_IVAR_$_HMMTROperationalFabricData._fabricID
+ OBJC_IVAR_$_HMMTROperationalFabricData._ipk
+ OBJC_IVAR_$_HMMTROperationalFabricData._operationalCert
+ OBJC_IVAR_$_HMMTROperationalFabricData._operationalKeyPair
+ OBJC_IVAR_$_HMMTROperationalFabricData._operationalNodeID
+ OBJC_IVAR_$_HMMTROperationalFabricData._residentNodeID
+ OBJC_IVAR_$_HMMTROperationalFabricData._rootCert
+ OBJC_IVAR_$_HMMTRPerControllerStorage._fabricID
+ OBJC_IVAR_$_HMMTRProtocolMap._nativeMatterDeviceTypes
+ OBJC_IVAR_$_HMMTRStorage._fabricUUID
+ OBJC_IVAR_$_HMMTRSyncClusterDoorLock._userUniqueIdentifierToUser
+ OBJC_IVAR_$_HMMTRThreadRadioManager._fabricUUIDOfActiveThreadNetwork
+ OBJC_IVAR_$_HMMTRThreadRadioManager._fabricUUIDOfPendingStartPairingBlock
+ _CFRelease
+ _CFRetain
+ _HMMTRUserFabricKeyUpdatedNotification
+ _OBJC_CLASS_$_HMFSoftwareVersion
+ _OBJC_CLASS_$_HMMCredentialKey
+ _OBJC_CLASS_$_HMMTRAliroVersion
+ _OBJC_CLASS_$_HMMTRFabricDataCreator
+ _OBJC_CLASS_$_HMMTRFabricRandomV0KeyStore
+ _OBJC_CLASS_$_HMMTRFabricV0KeyStore
+ _OBJC_CLASS_$_HMMTRFabricVoidV0DataStore
+ _OBJC_CLASS_$_HMMTRMultiFabricDataStoreQuery
+ _OBJC_CLASS_$_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ _OBJC_CLASS_$_HMMTRMultiFabricDataStoreUpdate
+ _OBJC_CLASS_$_HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore
+ _OBJC_CLASS_$_HMMTROperationalFabricData
+ _OBJC_CLASS_$_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ _OBJC_CLASS_$_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ _OBJC_CLASS_$_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ _OBJC_CLASS_$_HMMTRSyncClusterOzoneConcentrationMeasurement
+ _OBJC_CLASS_$_HMMTRSyncClusterPM10ConcentrationMeasurement
+ _OBJC_CLASS_$_HMMTRSyncClusterPM25ConcentrationMeasurement
+ _OBJC_CLASS_$_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterCarbonDioxideConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterCarbonMonoxideConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterNitrogenDioxideConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterOzoneConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterPM10ConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterPM25ConcentrationMeasurement
+ _OBJC_CLASS_$_MTRClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ _OBJC_CLASS_$_MTRDoorLockClusterAppleClearAliroCredentialParams
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_METACLASS_$_HMMCredentialKey
+ _OBJC_METACLASS_$_HMMTRAliroVersion
+ _OBJC_METACLASS_$_HMMTRFabricDataCreator
+ _OBJC_METACLASS_$_HMMTRFabricRandomV0KeyStore
+ _OBJC_METACLASS_$_HMMTRFabricV0KeyStore
+ _OBJC_METACLASS_$_HMMTRFabricVoidV0DataStore
+ _OBJC_METACLASS_$_HMMTRMultiFabricDataStoreQuery
+ _OBJC_METACLASS_$_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ _OBJC_METACLASS_$_HMMTRMultiFabricDataStoreUpdate
+ _OBJC_METACLASS_$_HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore
+ _OBJC_METACLASS_$_HMMTROperationalFabricData
+ _OBJC_METACLASS_$_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ _OBJC_METACLASS_$_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ _OBJC_METACLASS_$_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ _OBJC_METACLASS_$_HMMTRSyncClusterOzoneConcentrationMeasurement
+ _OBJC_METACLASS_$_HMMTRSyncClusterPM10ConcentrationMeasurement
+ _OBJC_METACLASS_$_HMMTRSyncClusterPM25ConcentrationMeasurement
+ _OBJC_METACLASS_$_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterCarbonDioxideConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterCarbonMonoxideConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterNitrogenDioxideConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterOzoneConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterPM10ConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterPM25ConcentrationMeasurement
+ _OBJC_METACLASS_$_MTRClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __100-[HMMTRAccessoryServer _writeCharacteristicValues:responseTuples:completionQueue:completionHandler:]_block_invoke.575
+ __100-[HMMTRAccessoryServer _writeCharacteristicValues:responseTuples:completionQueue:completionHandler:]_block_invoke_2.576
+ __101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.934
+ __101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.937
+ __101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.875
+ __102-[HMMTRSyncClusterDoorLock updateSchedulesForUserIndex:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.379
+ __105-[HMMTRSyncClusterDoorLock updateSchedulesOfScheduleType:withRequestedSchedules:forUserAtUserIndex:flow:]_block_invoke.455
+ __107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.230
+ __107-[HMMTRSyncClusterDoorLock setScheduleOfScheduleType:withSchedule:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.508
+ __109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.143
+ __109-[HMMTRDescriptorClusterManager fetchHAPCategoryWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.148
+ __109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.139
+ __109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.140
+ __110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.236
+ __111-[HMMTRDescriptorClusterManager _updateOTARequestorEndpointsInTopology:device:callbackQueue:completionHandler:]_block_invoke.318
+ __113-[HMMTRSyncClusterDoorLock findOperationOrderForModifyingWeekDaySchedules:andYearDaySchedules:forUserIndex:flow:]_block_invoke.451
+ __114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.415
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.553
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.554
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.555
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.556
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.557
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.561
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.563
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.558
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.562
+ __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.564
+ __119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.222
+ __123-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]_block_invoke.51
+ __123-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]_block_invoke.60
+ __123-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]_block_invoke.64
+ __124-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:]_block_invoke.422
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.366
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.367
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.371
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.374
+ __131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.307
+ __131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.310
+ __133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.105
+ __133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.110
+ __134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.311
+ __134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.312
+ __140-[HMMTRDescriptorClusterManager _runBlockForAllEndpointsWithClusterID:endpoints:device:callbackQueue:finishedRunningAllBlocksPromise:block:]_block_invoke.400
+ __147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.116
+ __147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.117
+ __147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.124
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.372
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.373
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.375
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.376
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.377
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.378
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.379
+ __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.380
+ __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.326
+ __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.328
+ __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.335
+ __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.329
+ __242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.282
+ __254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.202
+ __280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.258
+ __37-[HMMTRAccessoryServer finishPairing]_block_invoke.794
+ __37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.274
+ __39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke.360
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.679
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.680
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.683
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.684
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.688
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.689
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.692
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.693
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.685
+ __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.694
+ __40-[HMMTRAccessoryServerBrowser configure]_block_invoke.129
+ __40-[HMMTRAccessoryServerBrowser configure]_block_invoke.131
+ __40-[HMMTRAccessoryServerBrowser configure]_block_invoke.133
+ __40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.18
+ __42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.330
+ __42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.334
+ __42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.501
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.256
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.264
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.268
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.278
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.271
+ __43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.313
+ __43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.318
+ __43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.326
+ __45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.289
+ __45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.19
+ __45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.22
+ __47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.1016
+ __47-[HMMTRControllerWrapper replaceStartupParams:]_block_invoke.90
+ __47-[HMMTRStorage handleUpdatedCurrentFabricIndex]_block_invoke.7
+ __49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.419
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.847
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.851
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.855
+ __51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.1017
+ __51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke.24
+ __52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.677
+ __52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.350
+ __54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.295
+ __55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.1013
+ __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.449
+ __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.450
+ __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.451
+ __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.454
+ __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.455
+ __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.456
+ __56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.15
+ __57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.239
+ __58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.292
+ __58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.315
+ __58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke.162
+ __58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke_2.163
+ __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.471
+ __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.472
+ __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.473
+ __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.477
+ __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.478
+ __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.479
+ __59-[HMMTRSyncClusterDoorLock readSchedulesForUserIndex:flow:]_block_invoke.380
+ __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.938
+ __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.942
+ __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.946
+ __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.457
+ __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.458
+ __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.459
+ __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.460
+ __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.465
+ __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.470
+ __62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.180
+ __62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.383
+ __62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.384
+ __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.845
+ __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.846
+ __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.527
+ __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.528
+ __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.529
+ __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.530
+ __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.535
+ __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.536
+ __63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.175
+ __63-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withFlow:]_block_invoke.208
+ __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.491
+ __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.492
+ __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.493
+ __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.496
+ __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.497
+ __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.966
+ __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.967
+ __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.968
+ __64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.140
+ __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.486
+ __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.487
+ __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.488
+ __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.489
+ __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.490
+ __66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.395
+ __66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.396
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.331
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.337
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.340
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.346
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke_2.341
+ __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.480
+ __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.481
+ __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.482
+ __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.485
+ __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.430
+ __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.432
+ __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.516
+ __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.517
+ __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.518
+ __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.521
+ __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.525
+ __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.526
+ __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.436
+ __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.441
+ __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.445
+ __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.446
+ __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.181
+ __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.184
+ __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.190
+ __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.192
+ __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.191
+ __69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.284
+ __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.411
+ __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.417
+ __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.420
+ __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.423
+ __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.504
+ __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.505
+ __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.506
+ __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.510
+ __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.514
+ __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.515
+ __72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.255
+ __72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.260
+ __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.200
+ __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.201
+ __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.202
+ __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.203
+ __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.204
+ __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.205
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.838
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.839
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.843
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.844
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.820
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.821
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.831
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.832
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.836
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.837
+ __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.353
+ __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.354
+ __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.355
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.171
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.172
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.176
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.177
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.178
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.185
+ __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.192
+ __75+[HMMTRSyncClusterDoorLock validateFutureResults:ofClass:areNullable:flow:]_block_invoke.413
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.296
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.297
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.298
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.302
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.305
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.306
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.309
+ __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.299
+ __76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.195
+ __78-[HMMTRIdentifyDevice identifyBridgeWithAggregatorEndpoint:completionHandler:]_block_invoke.82
+ __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.425
+ __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.427
+ __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.428
+ __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.434
+ __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.435
+ __79-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumeration:]_block_invoke.819
+ __79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.366
+ __79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke.309
+ __79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_2.310
+ __80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.326
+ __81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.360
+ __81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.363
+ __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.952
+ __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.954
+ __82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke.214
+ __82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.154
+ __82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.156
+ __82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.266
+ __82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.267
+ __82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.268
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.904
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.905
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.906
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.918
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.919
+ __83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.878
+ __83-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:]_block_invoke.321
+ __84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.391
+ __84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.393
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.920
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.921
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.922
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.923
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.929
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.930
+ __84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke.212
+ __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.969
+ __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.970
+ __86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.487
+ __88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.402
+ __88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.403
+ __88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.404
+ __89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.488
+ __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.420
+ __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.421
+ __91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.418
+ __92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.809
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.579
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.580
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.581
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.582
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.585
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.588
+ __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.589
+ __93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.383
+ __94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.872
+ __94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.163
+ __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.517
+ __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke_2.522
+ __96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.387
+ __96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.420
+ __96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.491
+ __96-[HMMTRSyncClusterDoorLock clearScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.507
+ __97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.337
+ __99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke.214
+ __99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.496
+ __Block_byref_object_copy_.10413
+ __Block_byref_object_copy_.11088
+ __Block_byref_object_copy_.11753
+ __Block_byref_object_copy_.11944
+ __Block_byref_object_copy_.2826
+ __Block_byref_object_copy_.2968
+ __Block_byref_object_copy_.3131
+ __Block_byref_object_copy_.4116
+ __Block_byref_object_copy_.5280
+ __Block_byref_object_copy_.6927
+ __Block_byref_object_copy_.7249
+ __Block_byref_object_copy_.7632
+ __Block_byref_object_copy_.8710
+ __Block_byref_object_copy_.9694
+ __Block_byref_object_dispose_.10414
+ __Block_byref_object_dispose_.11089
+ __Block_byref_object_dispose_.11754
+ __Block_byref_object_dispose_.11945
+ __Block_byref_object_dispose_.2827
+ __Block_byref_object_dispose_.2969
+ __Block_byref_object_dispose_.3132
+ __Block_byref_object_dispose_.4117
+ __Block_byref_object_dispose_.5281
+ __Block_byref_object_dispose_.6928
+ __Block_byref_object_dispose_.7250
+ __Block_byref_object_dispose_.7633
+ __Block_byref_object_dispose_.8711
+ __Block_byref_object_dispose_.9695
+ __OBJC_$_CLASS_METHODS_HMMTRAccessoryServerBuilder
+ __OBJC_$_CLASS_METHODS_HMMTRFabricDataCreator
+ __OBJC_$_CLASS_METHODS_HMMTRFabricRandomV0KeyStore
+ __OBJC_$_CLASS_METHODS_HMMTRFabricV0KeyStore
+ __OBJC_$_CLASS_METHODS_HMMTRFabricVoidV0DataStore
+ __OBJC_$_CLASS_METHODS_HMMTRHAPServiceDescription
+ __OBJC_$_CLASS_METHODS_HMMTRMultiFabricDataStoreQuery
+ __OBJC_$_CLASS_METHODS_HMMTRMultiFabricDataStoreUpdate
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterOzoneConcentrationMeasurement
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterPM10ConcentrationMeasurement
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterPM25ConcentrationMeasurement
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMCredentialKey
+ __OBJC_$_INSTANCE_METHODS_HMMTRAliroVersion
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricDataCreator
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricRandomV0KeyStore
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricV0KeyStore
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricVoidV0DataStore
+ __OBJC_$_INSTANCE_METHODS_HMMTRMultiFabricDataStoreQuery
+ __OBJC_$_INSTANCE_METHODS_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ __OBJC_$_INSTANCE_METHODS_HMMTRMultiFabricDataStoreUpdate
+ __OBJC_$_INSTANCE_METHODS_HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore
+ __OBJC_$_INSTANCE_METHODS_HMMTROperationalCertificateIssuer(Test)
+ __OBJC_$_INSTANCE_METHODS_HMMTROperationalFabricData
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterOzoneConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterPM10ConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterPM25ConcentrationMeasurement
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __OBJC_$_INSTANCE_VARIABLES_HMMCredentialKey
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAliroVersion
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricDataCreator
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricRandomV0KeyStore
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRMultiFabricDataStoreQuery
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRMultiFabricDataStoreUpdate
+ __OBJC_$_INSTANCE_VARIABLES_HMMTROperationalFabricData
+ __OBJC_$_PROP_LIST_HMMCredentialKey
+ __OBJC_$_PROP_LIST_HMMTRAliroVersion
+ __OBJC_$_PROP_LIST_HMMTRFabricDataCreator
+ __OBJC_$_PROP_LIST_HMMTRFabricRandomV0KeyStore
+ __OBJC_$_PROP_LIST_HMMTRFabricV0KeyStore
+ __OBJC_$_PROP_LIST_HMMTRFabricVoidV0DataStore
+ __OBJC_$_PROP_LIST_HMMTRMultiFabricDataStoreQuery
+ __OBJC_$_PROP_LIST_HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate
+ __OBJC_$_PROP_LIST_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ __OBJC_$_PROP_LIST_HMMTRMultiFabricDataStoreQueryKeychainDelegate
+ __OBJC_$_PROP_LIST_HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate
+ __OBJC_$_PROP_LIST_HMMTRMultiFabricDataStoreUpdate
+ __OBJC_$_PROP_LIST_HMMTROperationalFabricData
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterOzoneConcentrationMeasurement
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterPM10ConcentrationMeasurement
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterPM25ConcentrationMeasurement
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRMultiFabricDataStoreQueryKeychainDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRMultiFabricDataStoreUpdateKeychainDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRMultiFabricDataStoreQueryKeychainDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRMultiFabricDataStoreUpdateKeychainDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMMCredentialKey
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRFabricRandomV0KeyStore
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRFabricV0KeyStore
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRFabricVoidV0DataStore
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterOzoneConcentrationMeasurement
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterPM10ConcentrationMeasurement
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterPM25ConcentrationMeasurement
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMCredentialKey
+ __OBJC_CLASS_RO_$_HMMTRAliroVersion
+ __OBJC_CLASS_RO_$_HMMTRFabricDataCreator
+ __OBJC_CLASS_RO_$_HMMTRFabricRandomV0KeyStore
+ __OBJC_CLASS_RO_$_HMMTRFabricV0KeyStore
+ __OBJC_CLASS_RO_$_HMMTRFabricVoidV0DataStore
+ __OBJC_CLASS_RO_$_HMMTRMultiFabricDataStoreQuery
+ __OBJC_CLASS_RO_$_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ __OBJC_CLASS_RO_$_HMMTRMultiFabricDataStoreUpdate
+ __OBJC_CLASS_RO_$_HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore
+ __OBJC_CLASS_RO_$_HMMTROperationalFabricData
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterOzoneConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterPM10ConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterPM25ConcentrationMeasurement
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __OBJC_LABEL_PROTOCOL_$_HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRMultiFabricDataStoreQueryKeychainDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRMultiFabricDataStoreUpdateKeychainDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate
+ __OBJC_METACLASS_RO_$_HMMCredentialKey
+ __OBJC_METACLASS_RO_$_HMMTRAliroVersion
+ __OBJC_METACLASS_RO_$_HMMTRFabricDataCreator
+ __OBJC_METACLASS_RO_$_HMMTRFabricRandomV0KeyStore
+ __OBJC_METACLASS_RO_$_HMMTRFabricV0KeyStore
+ __OBJC_METACLASS_RO_$_HMMTRFabricVoidV0DataStore
+ __OBJC_METACLASS_RO_$_HMMTRMultiFabricDataStoreQuery
+ __OBJC_METACLASS_RO_$_HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore
+ __OBJC_METACLASS_RO_$_HMMTRMultiFabricDataStoreUpdate
+ __OBJC_METACLASS_RO_$_HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore
+ __OBJC_METACLASS_RO_$_HMMTROperationalFabricData
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterCarbonDioxideConcentrationMeasurement
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterOzoneConcentrationMeasurement
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterPM10ConcentrationMeasurement
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterPM25ConcentrationMeasurement
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement
+ __OBJC_PROTOCOL_$_HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate
+ __OBJC_PROTOCOL_$_HMMTRMultiFabricDataStoreQueryKeychainDelegate
+ __OBJC_PROTOCOL_$_HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate
+ __OBJC_PROTOCOL_$_HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate
+ __OBJC_PROTOCOL_$_HMMTRMultiFabricDataStoreUpdateKeychainDelegate
+ __OBJC_PROTOCOL_$_HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate
+ ___100-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:targetFabricUUID:completionHandler:]_block_invoke
+ ___102-[HMMTRAccessoryServerBrowser _handleClientsRemovedWithFabricUUID:updateConnectionIdleTimeout:reason:]_block_invoke
+ ___102-[HMMTRDoorLockClusterAPIRouter readAttributeAliroSupportedBLEUWBProtocolVersionsWithFlow:completion:]_block_invoke
+ ___106-[HMMTRSyncClusterDoorLock __getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:]_block_invoke
+ ___106-[HMMTRSyncClusterDoorLock __getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:]_block_invoke_2
+ ___109-[HMMTRDescriptorClusterManager fetchHAPServicesWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke_2
+ ___109-[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:startingAtIndex:credentials:flow:]_block_invoke
+ ___116-[HMMTRDoorLockClusterAPIRouter readAttributeAliroExpeditedTransactionSupportedProtocolVersionsWithFlow:completion:]_block_invoke
+ ___123-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]_block_invoke
+ ___124-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:]_block_invoke
+ ___125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke
+ ___137-[HMMTRSyncClusterDoorLock findAllOccupiedCredentialSlotsForCredentialType:startingAtSlot:assumingTotalNumberOfSlots:occupiedSlots:flow:]_block_invoke
+ ___153-[HMMTRAccessoryServerBrowser handlePairingCompletionForAccessoryWithNodeID:targetFabricUUID:fabricID:vendorID:productID:configNumber:category:topology:]_block_invoke
+ ___153-[HMMTRSyncClusterDoorLock findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]_block_invoke
+ ___154-[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:forTargetFabricUUID:]_block_invoke
+ ___163-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:targetFabricUUID:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
+ ___166-[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricData:adminCAT:opCAT:completionHandler:]_block_invoke
+ ___171-[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:]_block_invoke
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke_3
+ ___332-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint:device:callbackQueue:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:attributeValuesSupportedDict:attributeValuesRetrievedDict:deviceTopology:server:lastError:completionHandler:]_block_invoke
+ ___36+[HMMTRFabricV0KeyStore logCategory]_block_invoke
+ ___37+[HMMTRFabricDataCreator logCategory]_block_invoke
+ ___41+[HMMTRFabricVoidV0DataStore logCategory]_block_invoke
+ ___42+[HMMTRFabricRandomV0KeyStore logCategory]_block_invoke
+ ___45+[HMMTRMultiFabricDataStoreQuery logCategory]_block_invoke
+ ___46+[HMMTRMultiFabricDataStoreUpdate logCategory]_block_invoke
+ ___46+[HMMTRSyncClusterDoorLock sortedArrayOfData:]_block_invoke
+ ___47-[HMMTRAccessoryServer handleRemoveFromBrowser]_block_invoke
+ ___47-[HMMTRSyncClusterDoorLock getMaxPINCodeLength]_block_invoke
+ ___47-[HMMTRSyncClusterDoorLock getMinPINCodeLength]_block_invoke
+ ___48+[HMMTROperationalCertificateIssuer logCategory]_block_invoke
+ ___49-[HMMTRThreadRadioManager stopThreadOnUserLogout]_block_invoke
+ ___50-[HMMTRControllerFactory _disableNormalOperation:]_block_invoke
+ ___53+[HMMTRDoorLockClusterAPIRouter arrayOfDataFromRead:]_block_invoke
+ ___53-[HMMTRFabricControllerStore removeTargetFabricUUID:]_block_invoke
+ ___54-[HMMTRSyncClusterDoorLock _readReaderConfigWithFlow:]_block_invoke
+ ___54-[HMMTRSyncClusterDoorLock _readReaderConfigWithFlow:]_block_invoke_2
+ ___55-[HMMTRSyncClusterDoorLock deriveHomePinFromUUID:flow:]_block_invoke
+ ___55-[HMMTRSyncClusterDoorLock setOrReadReaderConfig:flow:]_block_invoke_3
+ ___57-[HMMTRFabricControllerStore updateAllTargetFabricUUIDs:]_block_invoke
+ ___57-[HMMTRSyncClusterDoorLock issuerCredentialForUser:flow:]_block_invoke
+ ___59+[HMMTRSyncClusterPM10ConcentrationMeasurement logCategory]_block_invoke
+ ___59+[HMMTRSyncClusterPM25ConcentrationMeasurement logCategory]_block_invoke
+ ___59-[HMMTRAccessoryServerBrowser updateAccessoryACLForFabric:]_block_invoke
+ ___60+[HMMTRSyncClusterOzoneConcentrationMeasurement logCategory]_block_invoke
+ ___60-[HMMTRControllerWrapper deregisterRevokeHandlersWithQueue:]_block_invoke
+ ___60-[HMMTRControllerWrapper deregisterRevokeHandlersWithQueue:]_block_invoke_2
+ ___61-[HMMTRAccessoryServer triggerEstablishingMatterSubscription]_block_invoke
+ ___62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke
+ ___63-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withFlow:]_block_invoke
+ ___63-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withFlow:]_block_invoke_2
+ ___64-[HMMTRAccessoryServerBrowser _isNodeIDPaired:targetFabricUUID:]_block_invoke
+ ___64-[HMMTRFabricControllerStore cachedWrapperWithTargetFabricUUID:]_block_invoke
+ ___64-[HMMTRThreadRadioManager stopThreadRadioForHomeWithFabricUUID:]_block_invoke
+ ___65-[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricUUID:]_block_invoke
+ ___66-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:]_block_invoke
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke
+ ___67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke_2
+ ___68+[HMMTRSyncClusterCarbonDioxideConcentrationMeasurement logCategory]_block_invoke
+ ___69+[HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement logCategory]_block_invoke
+ ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke_2
+ ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke_3
+ ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke_4
+ ___70+[HMMTRHAPServiceDescription descriptionsDictionaryFromAccessoryInfo:]_block_invoke
+ ___70+[HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement logCategory]_block_invoke
+ ___70-[HMMTRSyncClusterDoorLock fetchAccessorySupportsAliroBLEUWBWithFlow:]_block_invoke_3
+ ___71-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserIndex:flow:]_block_invoke
+ ___72-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUserIndex:flow:]_block_invoke
+ ___72-[HMMTRSyncClusterDoorLock numberOfCredentialsSupportedPerUserWithFlow:]_block_invoke
+ ___72-[HMMTRThreadRadioManager overrideLocationCheckForPairingForFabricUUID:]_block_invoke
+ ___73-[HMMTRAccessoryServerBrowser _isDeviceIDPaired:nodeID:targetFabricUUID:]_block_invoke
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke
+ ___74-[HMMTRThreadRadioManager stopThreadRadioForSystemCommissionerFabricUUID:]_block_invoke
+ ___75-[HMMTRDoorLockClusterAPIRouter clearCredentialWithParams:flow:completion:]_block_invoke
+ ___75-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke
+ ___75-[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricUUID:]_block_invoke
+ ___76-[HMMTRAccessoryServerBrowser addFabricWithActiveClientForTargetFabricUUID:]_block_invoke
+ ___76-[HMMTRSyncClusterDoorLock fetchAccessorySupportsAliroProvisioningWithFlow:]_block_invoke_3
+ ___77-[HMMTRAccessoryServerBrowser clearOperationalFabricDataForTargetFabricUUID:]_block_invoke
+ ___77-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:completion:]_block_invoke
+ ___77-[HMMTRSyncClusterDoorLock updateUserUniqueIDForUserIndex:userUniqueID:flow:]_block_invoke
+ ___77-[HMMTRSyncClusterDoorLock updateUserUniqueIDForUserIndex:userUniqueID:flow:]_block_invoke_2
+ ___77-[HMMTRThreadRadioManager notifyThreadRadioStateChanged:nodeType:fabricUUID:]_block_invoke
+ ___78-[HMMTRIdentifyDevice identifyBridgeWithAggregatorEndpoint:completionHandler:]_block_invoke
+ ___78-[HMMTRIdentifyDevice identifyBridgeWithAggregatorEndpoint:completionHandler:]_block_invoke_2
+ ___78-[HMMTRThreadRadioManager _notifyThreadRadioStateChanged:nodeType:fabricUUID:]_block_invoke
+ ___79-[HMMTRDoorLockClusterAPIRouter appendAliroCredentialsToUser:aliroCredentials:]_block_invoke
+ ___79-[HMMTRSyncClusterDoorLock _addIssuerKeyData:forUserIndex:credentialType:flow:]_block_invoke
+ ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke
+ ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_2
+ ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_3
+ ___79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_4
+ ___83-[HMMTRAccessoryServerBrowser getNumberOfAccessoryServersForFabricUUID:completion:]_block_invoke
+ ___83-[HMMTRAccessoryServerBrowser getNumberOfAccessoryServersForFabricUUID:completion:]_block_invoke_2
+ ___83-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:]_block_invoke
+ ___83-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:]_block_invoke_2
+ ___83-[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricUUID:preventDisconnect:]_block_invoke
+ ___84+[HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement logCategory]_block_invoke
+ ___90-[HMMTRAccessoryServerBrowser handlePairingForThreadAccessoryWithTargetFabricUUID:nodeID:]_block_invoke
+ ___90-[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:]_block_invoke
+ ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke
+ ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_2
+ ___92-[HMMTRDoorLockClusterAPIRouter readAttributeAliroBLEAdvertisingVersionWithFlow:completion:]_block_invoke
+ ___95-[HMMTRDoorLockClusterAPIRouter numberOfAliroDeviceKeyCredentialsSupportedWithFlow:completion:]_block_invoke
+ ___95-[HMMTRDoorLockClusterAPIRouter numberOfAliroIssuerKeyCredentialsSupportedWithFlow:completion:]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricUUID:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e83_v44?0"HMMTRHAPAccessoryInfo"8B16"NSNumber"20"HMMTRDeviceTopology"28"NSError"36l
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs96r104r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e56_v40?0"NSString"8"NSNumber"16"NSNumber"24"NSError"32l
+ ___block_descriptor_194_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184bs_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e27_q24?0"NSData"8"NSData"16l
+ ___block_descriptor_32_e40_B16?0"<HMMTRFabricStorageDataSource>"8l
+ ___block_descriptor_32_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8l
+ ___block_descriptor_32_e51_B32?0"MTRDoorLockClusterCredentialStruct"8Q16^B24l
+ ___block_descriptor_40_e20_B16?0"HAPService"8l
+ ___block_descriptor_40_e8_32bs_e83_v44?0"HMMTRHAPAccessoryInfo"8B16"NSNumber"20"HMMTRDeviceTopology"28"NSError"36l
+ ___block_descriptor_40_e8_32s_e30_B16?0"HMMTRAccessoryServer"8l
+ ___block_descriptor_40_e8_32s_e56_B32?0"HMMTRControllerWrapperRevokeHandlerInfo"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e60_{_HMFFutureBlockOutcome=q}16?0"FindOrAddHomeUserResults"8l
+ ___block_descriptor_40_e8_32s_e81_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterSetCredentialResponseParams"8l
+ ___block_descriptor_40_e8_32s_e8_v16?0Q8l
+ ___block_descriptor_48_e8_32s40bs_e133_v60?0"HMMTRHAPAccessoryInfo"8B16"NSNumber"20"HMMTRDeviceTopology"28"HMMTRHAPAccessoryInfo"36"HMMTRDeviceTopology"44"NSError"52l
+ ___block_descriptor_48_e8_32s40bs_e47_v32?0"NSNumber"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e83_v44?0"HMMTRHAPAccessoryInfo"8B16"NSNumber"20"HMMTRDeviceTopology"28"NSError"36l
+ ___block_descriptor_48_e8_32s40s_e49_16?0"MTRDoorLockClusterGetUserResponseParams"8l
+ ___block_descriptor_56_e8_32s40s48bs_e43_{_HMFFutureBlockOutcome=q}16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48bs_e44_{_HMFFutureBlockOutcome=q}16?0"NSString"8l
+ ___block_descriptor_56_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48s_e30_v24?0"NSNumber"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48s_e43_{_HMFFutureBlockOutcome=q}16?0"NSArray"8l
+ ___block_descriptor_56_e8_32s40s48s_e82_v24?0"HMMCredentialKey"8"MTRDoorLockClusterGetCredentialStatusResponseParams"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56s_e16_"HMFFuture"8?0l
+ ___block_descriptor_64_e8_32s40s48s56s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8l
+ ___block_descriptor_64_e8_32s40s48s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8l
+ ___block_descriptor_65_e8_32s40s48s_e16_"HMFFuture"8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
+ ___block_descriptor_72_e8_32s40s48s56s_e81_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterSetCredentialResponseParams"8l
+ ___block_descriptor_72_e8_32s40s48s_e71_"NAFuture"16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56s64s_e16_"HMFFuture"8?0l
+ ___block_descriptor_73_e8_32s40s48s56s64s_e60_{_HMFFutureBlockOutcome=q}16?0"FindOrAddHomeUserResults"8l
+ ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e16_"HMFFuture"8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e81_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterSetCredentialResponseParams"8l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8l
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e83_v44?0"HMMTRHAPAccessoryInfo"8B16"NSNumber"20"HMMTRDeviceTopology"28"NSError"36l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e18_v16?0"NSNumber"8l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8l
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96r104r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184b
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r104r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s
+ __block_literal_global.10152
+ __block_literal_global.1025
+ __block_literal_global.1058
+ __block_literal_global.10683
+ __block_literal_global.10908
+ __block_literal_global.11133
+ __block_literal_global.11276
+ __block_literal_global.1135
+ __block_literal_global.11390
+ __block_literal_global.11797
+ __block_literal_global.133
+ __block_literal_global.1336
+ __block_literal_global.156
+ __block_literal_global.1596
+ __block_literal_global.1648
+ __block_literal_global.1695
+ __block_literal_global.17
+ __block_literal_global.1783
+ __block_literal_global.197
+ __block_literal_global.2132
+ __block_literal_global.215
+ __block_literal_global.2276
+ __block_literal_global.2580
+ __block_literal_global.270
+ __block_literal_global.270.10518
+ __block_literal_global.2730
+ __block_literal_global.274
+ __block_literal_global.2759
+ __block_literal_global.2854
+ __block_literal_global.287
+ __block_literal_global.288
+ __block_literal_global.301
+ __block_literal_global.3028
+ __block_literal_global.312
+ __block_literal_global.316
+ __block_literal_global.3217
+ __block_literal_global.333
+ __block_literal_global.3349
+ __block_literal_global.339
+ __block_literal_global.343
+ __block_literal_global.345
+ __block_literal_global.3460
+ __block_literal_global.348
+ __block_literal_global.357
+ __block_literal_global.362
+ __block_literal_global.382
+ __block_literal_global.396
+ __block_literal_global.398
+ __block_literal_global.406
+ __block_literal_global.410
+ __block_literal_global.417
+ __block_literal_global.419
+ __block_literal_global.4212
+ __block_literal_global.428
+ __block_literal_global.4500
+ __block_literal_global.46.9494
+ __block_literal_global.460
+ __block_literal_global.4635
+ __block_literal_global.464
+ __block_literal_global.4737
+ __block_literal_global.490
+ __block_literal_global.4995
+ __block_literal_global.512
+ __block_literal_global.5169
+ __block_literal_global.520
+ __block_literal_global.524
+ __block_literal_global.527
+ __block_literal_global.532
+ __block_literal_global.532.9857
+ __block_literal_global.5409
+ __block_literal_global.5538
+ __block_literal_global.5773
+ __block_literal_global.5807
+ __block_literal_global.5829
+ __block_literal_global.6086
+ __block_literal_global.6098
+ __block_literal_global.6192
+ __block_literal_global.6288
+ __block_literal_global.6383
+ __block_literal_global.6491
+ __block_literal_global.6586
+ __block_literal_global.6682
+ __block_literal_global.6827
+ __block_literal_global.686
+ __block_literal_global.6975
+ __block_literal_global.7082
+ __block_literal_global.7161
+ __block_literal_global.7455
+ __block_literal_global.7644
+ __block_literal_global.782
+ __block_literal_global.7972
+ __block_literal_global.8100
+ __block_literal_global.816
+ __block_literal_global.82.9495
+ __block_literal_global.8734
+ __block_literal_global.9170
+ __block_literal_global.9493
+ __block_literal_global.9571
+ __block_literal_global.966
+ __block_literal_global.99
+ _isFeatureMatterRVCEnabled
+ _isFeatureMatterRVCEnabledForTests
+ _kCHIPKeychainDescription
+ _kCHIPKeychainLabel
+ _kSecUseDataProtectionKeychain
+ _memcmp
+ _objc_msgSend$__getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:
+ _objc_msgSend$_abortAllOperationsForFabricUUID:reason:
+ _objc_msgSend$_addIssuerKeyData:forUserIndex:credentialType:flow:
+ _objc_msgSend$_addOrUpdateIssuerKeyData:forUser:flow:
+ _objc_msgSend$_addOrUpdateIssuerKeyData:forUserIndex:flow:
+ _objc_msgSend$_addOrUpdateIssuerKeyData:forUserUniqueID:flow:
+ _objc_msgSend$_connectPendingFabricConnectionsForTargetFabricUUID:
+ _objc_msgSend$_deviceHasActiveSubscription
+ _objc_msgSend$_deviceMayBeReachable
+ _objc_msgSend$_disableNormalOperation:
+ _objc_msgSend$_getThreadHardwareAddressFromReadValue:
+ _objc_msgSend$_getUserAtIndex:flow:
+ _objc_msgSend$_handleClientsRemovedWithFabricUUID:updateConnectionIdleTimeout:reason:
+ _objc_msgSend$_handleDeviceActivityStateChange:reason:
+ _objc_msgSend$_handleEventReport:
+ _objc_msgSend$_handleKeybagLockStateNotification
+ _objc_msgSend$_handleLogoutNotification
+ _objc_msgSend$_isDeviceIDPaired:nodeID:targetFabricUUID:
+ _objc_msgSend$_isNodeIDPaired:targetFabricUUID:
+ _objc_msgSend$_legacyHMDHAPAccessoryDelegateShouldHandleEvent:
+ _objc_msgSend$_notifyThreadRadioStateChanged:nodeType:fabricUUID:
+ _objc_msgSend$_prepareForPairingWithSetupPayload:targetFabricUUID:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:
+ _objc_msgSend$_queryAttributeValueFromClusterAtCHIPEndpoint:device:attributeValuesToCheckDict:attributeValuesSupportedDict:attributeValuesRetrievedDict:callbackQueue:clusterClassName:completionHandler:
+ _objc_msgSend$_readReaderConfigWithFlow:
+ _objc_msgSend$_removeOrSuspendAllActiveClientsWithCurrentFabricUUID:reason:
+ _objc_msgSend$_resumeSuspendedActiveClients
+ _objc_msgSend$_setupStorageStateForHomeFabricUUID:
+ _objc_msgSend$_setupStorageStateForUpdatedHomeFabricUUID:
+ _objc_msgSend$_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:
+ _objc_msgSend$_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:
+ _objc_msgSend$_setupStorageStateIfNotFabricUUID:rediscoverAccessories:
+ _objc_msgSend$_startThreadRadioForSystemCommissionerFabricUUID:
+ _objc_msgSend$_startThreadRadioForTargetFabricUUID:preventDisconnect:
+ _objc_msgSend$_stopSystemCommissionerFabricWithReason:
+ _objc_msgSend$_stopThreadRadioForSystemCommissionerFabricUUID:
+ _objc_msgSend$_stopThreadRadioForTargetFabricUUID:
+ _objc_msgSend$_suspendOperationsForTargetFabricUUID:
+ _objc_msgSend$_updateFabricUUIDOfActiveThreadNetwork:isFabricUUIDOfSystemCommissioner:
+ _objc_msgSend$_verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint:device:callbackQueue:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:attributeValuesSupportedDict:attributeValuesRetrievedDict:deviceTopology:server:lastError:completionHandler:
+ _objc_msgSend$addFabricWithActiveClientForTargetFabricUUID:
+ _objc_msgSend$addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:
+ _objc_msgSend$addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:
+ _objc_msgSend$addSuspendedActiveSecondaryClientFabricUUIDs:
+ _objc_msgSend$aliroClearCredentialParamsFromParams:flow:
+ _objc_msgSend$appendAliroCredentialsToUser:aliroCredentials:
+ _objc_msgSend$appleClearAliroCredentialWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$appleGetAliroCredentialStatusWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$appleHomeFabricWithTargetFabricUUID:
+ _objc_msgSend$appleSetAliroCredentialWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$appleSetAliroReaderConfigWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$arrayOfDataFromRead:
+ _objc_msgSend$bridgeIdentifyEndpointWithAggregatorEndpoint:
+ _objc_msgSend$cacheUserResponse:
+ _objc_msgSend$cachedWrapperWithTargetFabricUUID:
+ _objc_msgSend$cancel
+ _objc_msgSend$chipStorageContentFromFabricData:
+ _objc_msgSend$clearCredentialWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$clearCredentialWithParams:flow:completion:
+ _objc_msgSend$clearSuspendedActiveSecondaryClientFabricUUIDs
+ _objc_msgSend$combineAllFutures:
+ _objc_msgSend$commissioneeNodeID
+ _objc_msgSend$configureDefaultRequiresThreadRouter
+ _objc_msgSend$connectToAccessoryWithExtendedMACAddress:withFabricUUID:completion:
+ _objc_msgSend$creationTime
+ _objc_msgSend$credentialStruct
+ _objc_msgSend$currentFabricUUID
+ _objc_msgSend$deleteKeychainItem:error:
+ _objc_msgSend$deregisterRevokeHandlersWithQueue:
+ _objc_msgSend$descriptionsDictionaryFromAccessoryInfo:
+ _objc_msgSend$didSendRevokeAvailableOnResume
+ _objc_msgSend$doorLock
+ _objc_msgSend$fabricDataForPairingTargetFabricUUID:
+ _objc_msgSend$fabricDataForRootKeyPair:opKeyPair:fabricID:residentNodeID:overridingRCAC:ipk:
+ _objc_msgSend$fabricDataFromV2FabricDataItem:
+ _objc_msgSend$fabricDataItems
+ _objc_msgSend$fabricIDFromFabricUUID:
+ _objc_msgSend$fabricUUID
+ _objc_msgSend$fabricUUIDOfActiveThreadNetwork
+ _objc_msgSend$fabricUUIDOfPendingStartPairingBlock
+ _objc_msgSend$findAllOccupiedCredentialSlotsForCredentialType:startingAtSlot:assumingTotalNumberOfSlots:occupiedSlots:flow:
+ _objc_msgSend$findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:
+ _objc_msgSend$findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:
+ _objc_msgSend$findOrAddUserWithUniqueID:flow:
+ _objc_msgSend$finishWithError:
+ _objc_msgSend$finishWithResult:
+ _objc_msgSend$getAppleAliroCredentialsWithCredentialType:startingAtIndex:credentials:flow:
+ _objc_msgSend$getCredentialStatusWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$getNumberOfAccessoryServersForFabricUUID:completion:
+ _objc_msgSend$getThreadNetworkConnectionStateWithFabricUUID:
+ _objc_msgSend$getThreadNetworkNodeTypeWithFabricUUID:
+ _objc_msgSend$getUserWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:
+ _objc_msgSend$handleRemoveFromBrowser
+ _objc_msgSend$hapErrorWithCode:marker:
+ _objc_msgSend$hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:
+ _objc_msgSend$hasMatterThreadAccessoryInHomeWithFabricUUID:
+ _objc_msgSend$identifyBridgeWithAggregatorEndpoint:completionHandler:
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initWithCredentialType:andCredentialIndex:
+ _objc_msgSend$initWithDevice:endpoint:queue:accessoryServer:
+ _objc_msgSend$initWithDoorLock:device:queue:
+ _objc_msgSend$initWithIdentifier:categoryNumber:isInvalid:
+ _objc_msgSend$initWithMajorVersion:minorVersion:updateVersion:
+ _objc_msgSend$initWithQueue:browser:fabricUUID:systemCommissionerFabric:
+ _objc_msgSend$initWithQueue:privateDataSource:
+ _objc_msgSend$initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:residentOperationalKeyPair:residentOperationalCert:
+ _objc_msgSend$ipkForTargetFabricUUID:forPairing:
+ _objc_msgSend$isFirmwareUpdateInProgressForFabricUUID:
+ _objc_msgSend$isInvalid
+ _objc_msgSend$issuerCredentialForUser:flow:
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$legacyNodeIDForTargetFabricUUID:
+ _objc_msgSend$mapCarbonMonoxideDetected:
+ _objc_msgSend$mapSmokeDetected:
+ _objc_msgSend$markAsSubscribed
+ _objc_msgSend$markForResubscription
+ _objc_msgSend$mtrBaseDeviceWithNodeID:controller:
+ _objc_msgSend$mtrPluginDeviceControllerRegistry
+ _objc_msgSend$mtrPluginSharedInstance
+ _objc_msgSend$na_firstObjectPassingTest:
+ _objc_msgSend$numberOfAliroIssuerKeyCredentialsSupportedWithFlow:completion:
+ _objc_msgSend$numberOfCredentialsSupportedPerUserWithFlow:
+ _objc_msgSend$operationalNodeID
+ _objc_msgSend$overrideLocationCheckForPairingForFabricUUID:
+ _objc_msgSend$pairingRequest
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$prepareStorageForTargetFabricUUID:
+ _objc_msgSend$prepareStorageForTargetFabricUUID:forInitialSetup:
+ _objc_msgSend$propagateCharactersticValuesToAccessory:
+ _objc_msgSend$publicKeyData
+ _objc_msgSend$publicKeyDataFromCertificate:
+ _objc_msgSend$publicKeyFromCSRInfo:error:
+ _objc_msgSend$rcac
+ _objc_msgSend$readAttributeAliroBLEAdvertisingVersionWithFlow:completion:
+ _objc_msgSend$readAttributeAliroBLEAdvertisingVersionWithParams:
+ _objc_msgSend$readAttributeAliroExpeditedTransactionSupportedProtocolVersionsWithFlow:completion:
+ _objc_msgSend$readAttributeAliroExpeditedTransactionSupportedProtocolVersionsWithParams:
+ _objc_msgSend$readAttributeAliroGroupResolvingKeyWithParams:
+ _objc_msgSend$readAttributeAliroReaderGroupIdentifierWithParams:
+ _objc_msgSend$readAttributeAliroReaderVerificationKeyWithParams:
+ _objc_msgSend$readAttributeAliroSupportedBLEUWBProtocolVersionsWithFlow:completion:
+ _objc_msgSend$readAttributeAliroSupportedBLEUWBProtocolVersionsWithParams:
+ _objc_msgSend$readAttributeAppleAliroBLEAdvertisingVersionWithParams:
+ _objc_msgSend$readAttributeAppleAliroExpeditedTransactionSupportedProtocolVersionsWithParams:
+ _objc_msgSend$readAttributeAppleAliroGroupResolvingKeyWithParams:
+ _objc_msgSend$readAttributeAppleAliroReaderGroupIdentifierWithParams:
+ _objc_msgSend$readAttributeAppleAliroReaderGroupSubIdentifierWithParams:
+ _objc_msgSend$readAttributeAppleAliroReaderVerificationKeyWithParams:
+ _objc_msgSend$readAttributeAppleAliroSupportedBLEUWBProtocolVersionsWithParams:
+ _objc_msgSend$readAttributeAppleNumberOfAliroCredentialIssuerKeysSupportedWithParams:
+ _objc_msgSend$readAttributeAppleNumberOfAliroEndpointKeysSupportedWithParams:
+ _objc_msgSend$readAttributeMaxCoolSetpointLimitWithParams:
+ _objc_msgSend$readAttributeMaxHeatSetpointLimitWithParams:
+ _objc_msgSend$readAttributeMeasuredValueWithParams:
+ _objc_msgSend$readAttributeMeasurementUnitWithParams:
+ _objc_msgSend$readAttributeMinCoolSetpointLimitWithParams:
+ _objc_msgSend$readAttributeMinHeatSetpointLimitWithParams:
+ _objc_msgSend$readAttributeMinPINCodeLengthWithParams:
+ _objc_msgSend$readAttributeNumberOfAliroCredentialIssuerKeysSupportedWithParams:
+ _objc_msgSend$readAttributeNumberOfAliroEndpointKeysSupportedWithParams:
+ _objc_msgSend$readAttributeNumberOfCredentialsSupportedPerUserWithParams:
+ _objc_msgSend$readAttributePeakMeasuredValueWithParams:
+ _objc_msgSend$reloadOperationalFabricData
+ _objc_msgSend$remoteDelegate
+ _objc_msgSend$removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:
+ _objc_msgSend$removeActiveClientWithFabricUUID:updateConnectionIdleTimeout:reason:
+ _objc_msgSend$removeActiveSecondaryClientWithFabricUUID:updateConnectionIdleTimeout:reason:
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$removeTargetFabricUUID:
+ _objc_msgSend$reportObservers
+ _objc_msgSend$requiresRemoteFabricDataUpdateThroughPairingCompletionMessage
+ _objc_msgSend$residentOpKeyPair
+ _objc_msgSend$residentOperationalCert
+ _objc_msgSend$residentOperationalKeyPair
+ _objc_msgSend$restartNormalOperation
+ _objc_msgSend$retrieveHAPCharacteristicsToCheckForRequiredAttributeValues
+ _objc_msgSend$retrieveOperationalCertificatesForFabricID:commissioneeNodeID:publicKey:completion:
+ _objc_msgSend$rootKeyPair
+ _objc_msgSend$runAfterCommissioningToTargetFabricUUID:controllerSetUpBlock:
+ _objc_msgSend$setAliroReaderConfigWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$setBleAdvertisingVersion:
+ _objc_msgSend$setBleUWBSupportedVersions:
+ _objc_msgSend$setCredentialWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$setCurrentFabricUUID:
+ _objc_msgSend$setDidSendRevokeAvailableOnResume:
+ _objc_msgSend$setEndpointToDeviceTypesMap:
+ _objc_msgSend$setExpeditedTransactionSupportedVersions:
+ _objc_msgSend$setFabricUUID:
+ _objc_msgSend$setFabricUUIDOfActiveThreadNetwork:
+ _objc_msgSend$setFabricUUIDOfPendingStartPairingBlock:
+ _objc_msgSend$setFirmwareVersion:
+ _objc_msgSend$setLockStateKBNotificationRegistered:
+ _objc_msgSend$setLockStateKBNotificationRegistrationToken:
+ _objc_msgSend$setLogoutNotificationRegistered:
+ _objc_msgSend$setLogoutNotificationRegistrationToken:
+ _objc_msgSend$setPairingRequest:
+ _objc_msgSend$setPairingTargetFabricData:targetFabricUUID:
+ _objc_msgSend$setShouldReestablishSubscription:
+ _objc_msgSend$setSuspendedActiveClientFabricUUID:
+ _objc_msgSend$setUserUniqueID:
+ _objc_msgSend$setUserWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:
+ _objc_msgSend$setupStorageStateForHomeFabricUUID:
+ _objc_msgSend$shouldReestablishSubscription
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$sortedArrayOfData:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$startAccessoryFirmwareUpdateWithExtendedMACAddress:fabricUUID:isWedDevice:completion:
+ _objc_msgSend$startAccessoryPairingWithExtendedMACAddress:fabricUUID:isWedDevice:completion:
+ _objc_msgSend$startThreadRadioForHomeWithFabricUUID:
+ _objc_msgSend$startThreadRadioForHomeWithFabricUUID:preventDisconnect:
+ _objc_msgSend$startThreadRadioForSystemCommissionerFabricUUID:
+ _objc_msgSend$stopAccessoryFirmwareUpdateWithFabricUUID:completion:
+ _objc_msgSend$stopAccessoryPairingWithFabricUUID:completion:
+ _objc_msgSend$stopThreadOnUserLogout
+ _objc_msgSend$stopThreadRadioForHomeWithFabricUUID:
+ _objc_msgSend$stopThreadRadioForSystemCommissionerFabricUUID:
+ _objc_msgSend$storageDataSourceForFabricUUID:
+ _objc_msgSend$storeFabricData:
+ _objc_msgSend$supportedLinkLayerTypesContainsEthernet:
+ _objc_msgSend$supportedLinkLayerTypesContainsThread:
+ _objc_msgSend$supportedLinkLayerTypesContainsWiFi:
+ _objc_msgSend$suspendOperationsForFabricUUID:
+ _objc_msgSend$suspendedActiveClientFabricUUID
+ _objc_msgSend$suspendedActiveSecondaryClientFabricUUIDs
+ _objc_msgSend$systemCommissionerFabricUUID
+ _objc_msgSend$updateAllTargetFabricUUIDs:
+ _objc_msgSend$updateKeyValueStoreWithEntries:
+ _objc_msgSend$updateNocSigner:ownerSharedOperationalKeyPair:
+ _objc_msgSend$updateStorageWithPrivateKeyData:
+ _objc_msgSend$updateUserUniqueIDForUserIndex:userUniqueID:flow:
+ _objc_msgSend$userUniqueIdentifierToUser
+ _objc_msgSend$v2FabricDataStoreDelegate
+ _objc_msgSend$versionString
+ _objc_msgSend$weakObjectsHashTable
+ _objc_sync_enter
+ _objc_sync_exit
+ logCategory._hmf_once_t0.1647
+ logCategory._hmf_once_t0.2729
+ logCategory._hmf_once_t0.5168
+ logCategory._hmf_once_t0.5806
+ logCategory._hmf_once_t1.4634
+ logCategory._hmf_once_t10.6974
+ logCategory._hmf_once_t13
+ logCategory._hmf_once_t13.2853
+ logCategory._hmf_once_t13.3216
+ logCategory._hmf_once_t193
+ logCategory._hmf_once_t2.4736
+ logCategory._hmf_once_t2.5772
+ logCategory._hmf_once_t2.6826
+ logCategory._hmf_once_t2.9570
+ logCategory._hmf_once_t20.11275
+ logCategory._hmf_once_t21
+ logCategory._hmf_once_t22.6191
+ logCategory._hmf_once_t22.6287
+ logCategory._hmf_once_t22.6585
+ logCategory._hmf_once_t22.6681
+ logCategory._hmf_once_t22.7971
+ logCategory._hmf_once_t265
+ logCategory._hmf_once_t3.1057
+ logCategory._hmf_once_t31
+ logCategory._hmf_once_t34
+ logCategory._hmf_once_t346
+ logCategory._hmf_once_t36
+ logCategory._hmf_once_t4.3348
+ logCategory._hmf_once_t4.7081
+ logCategory._hmf_once_t40
+ logCategory._hmf_once_t40.7643
+ logCategory._hmf_once_t43
+ logCategory._hmf_once_t560
+ logCategory._hmf_once_t59
+ logCategory._hmf_once_t6.1694
+ logCategory._hmf_once_t6.1782
+ logCategory._hmf_once_t65
+ logCategory._hmf_once_t8.10907
+ logCategory._hmf_once_t81
+ logCategory._hmf_once_t87
+ logCategory._hmf_once_t9.5537
+ logCategory._hmf_once_t93
+ logCategory._hmf_once_v1.1649
+ logCategory._hmf_once_v1.2731
+ logCategory._hmf_once_v1.5170
+ logCategory._hmf_once_v1.5808
+ logCategory._hmf_once_v10.5539
+ logCategory._hmf_once_v11.6976
+ logCategory._hmf_once_v14
+ logCategory._hmf_once_v14.2855
+ logCategory._hmf_once_v14.3218
+ logCategory._hmf_once_v194
+ logCategory._hmf_once_v2.4636
+ logCategory._hmf_once_v21.11277
+ logCategory._hmf_once_v22
+ logCategory._hmf_once_v23.6193
+ logCategory._hmf_once_v23.6289
+ logCategory._hmf_once_v23.6587
+ logCategory._hmf_once_v23.6683
+ logCategory._hmf_once_v23.7973
+ logCategory._hmf_once_v266
+ logCategory._hmf_once_v3.4738
+ logCategory._hmf_once_v3.5774
+ logCategory._hmf_once_v3.6828
+ logCategory._hmf_once_v3.9572
+ logCategory._hmf_once_v32
+ logCategory._hmf_once_v347
+ logCategory._hmf_once_v35
+ logCategory._hmf_once_v37
+ logCategory._hmf_once_v4.1059
+ logCategory._hmf_once_v41
+ logCategory._hmf_once_v41.7645
+ logCategory._hmf_once_v44
+ logCategory._hmf_once_v5.3350
+ logCategory._hmf_once_v5.7083
+ logCategory._hmf_once_v561
+ logCategory._hmf_once_v60
+ logCategory._hmf_once_v66
+ logCategory._hmf_once_v7.1696
+ logCategory._hmf_once_v7.1784
+ logCategory._hmf_once_v82
+ logCategory._hmf_once_v88
+ logCategory._hmf_once_v9.10909
+ logCategory._hmf_once_v94
- +[HMMTRFabricDataFetcher logCategory]
- +[HMMTRSyncClusterDoorLock colorFromAttributeResponse:]
- +[HMMTRSyncClusterDoorLock productFinishFromAttributeResponse:]
- -[HMMTRAccessoryConnectionRequest fabricID]
- -[HMMTRAccessoryServer handleEventReportForNotification:]
- -[HMMTRAccessoryServer pairingTargetHomeUUID]
- -[HMMTRAccessoryServer setPairingTargetHomeUUID:]
- -[HMMTRAccessoryServerBrowser _abortAllOperationsForFabricID:reason:]
- -[HMMTRAccessoryServerBrowser _connectPendingFabricConnectionsForFabricID:]
- -[HMMTRAccessoryServerBrowser _createFabricKeyPairsIfAbsent]
- -[HMMTRAccessoryServerBrowser _createOperationalKeyPairIfAbsent]
- -[HMMTRAccessoryServerBrowser _currentHomeFabricDeviceControllerStartupParams1]
- -[HMMTRAccessoryServerBrowser _currentHomeFabricDeviceControllerStartupParams2]
- -[HMMTRAccessoryServerBrowser _currentHomeFabricDeviceControllerStartupParams]
- -[HMMTRAccessoryServerBrowser _handleClientsRemovedWithFabricID:updateConnectionIdleTimeout:reason:]
- -[HMMTRAccessoryServerBrowser _isDeviceIDPaired:nodeID:fabricID:]
- -[HMMTRAccessoryServerBrowser _isNodeIDPaired:fabricID:]
- -[HMMTRAccessoryServerBrowser _loadFabricKeyPairs]
- -[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]
- -[HMMTRAccessoryServerBrowser _setupAndPersistStorageStateForHomeFabricID:completion:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateAfterCertFetchForHomeFabricID:completion:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForHomeFabricID:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricID:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:overrideAccessoryControlAllowed:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateIfNotFabricID:rediscoverAccessories:]
- -[HMMTRAccessoryServerBrowser _stopSystemCommissionerFabricID:reason:]
- -[HMMTRAccessoryServerBrowser _suspendOperationsForFabricID:]
- -[HMMTRAccessoryServerBrowser addFabricWithActiveClientForFabricID:]
- -[HMMTRAccessoryServerBrowser appleHomeFabricRootPublicKey]
- -[HMMTRAccessoryServerBrowser appleHomeFabricWithID:]
- -[HMMTRAccessoryServerBrowser appleHomeFabricWithUUID:]
- -[HMMTRAccessoryServerBrowser cacheOperationalCertificate:fabricID:]
- -[HMMTRAccessoryServerBrowser clearPreWarmTarget]
- -[HMMTRAccessoryServerBrowser configureControllerForFabric:]
- -[HMMTRAccessoryServerBrowser configuredPreWarmTargetFabricID]
- -[HMMTRAccessoryServerBrowser createMatterOperationalKeyPairIfAbsentWithCompletion:]
- -[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]
- -[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]
- -[HMMTRAccessoryServerBrowser createNewFabricIDWithCompletion:]
- -[HMMTRAccessoryServerBrowser currentFabricID]
- -[HMMTRAccessoryServerBrowser fetchCachedOperationalCertificateForFabricID:completionHandler:]
- -[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:]
- -[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:rootCertificate:completionHandler:]
- -[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForSharedAdminWithDeviceNodeID:forOwner:publicKey:fabricID:completionHandler:]
- -[HMMTRAccessoryServerBrowser getNOCFromResidentForSharedUserForFabric:]
- -[HMMTRAccessoryServerBrowser handlePairingCompletionForAccessoryWithNodeID:fabricID:vendorID:productID:configNumber:category:topology:]
- -[HMMTRAccessoryServerBrowser handlePairingForThreadAccessoryWithFabricID:nodeID:]
- -[HMMTRAccessoryServerBrowser isCurrentDeviceMobileAndResidentReachableAndThreadCapableForFabric:]
- -[HMMTRAccessoryServerBrowser nocSigner]
- -[HMMTRAccessoryServerBrowser nodeIDForFabricID:deviceIdentifier:]
- -[HMMTRAccessoryServerBrowser overrideCurrentFabricID:]
- -[HMMTRAccessoryServerBrowser ownerLocalOperationalKeyPair]
- -[HMMTRAccessoryServerBrowser preWarmTargetIsSystemCommissionerFabric]
- -[HMMTRAccessoryServerBrowser preWarmedFabricID]
- -[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]
- -[HMMTRAccessoryServerBrowser removeActiveClientWithFabricID:updateConnectionIdleTimeout:reason:]
- -[HMMTRAccessoryServerBrowser removeActiveSecondaryClientWithFabricID:updateConnectionIdleTimeout:reason:]
- -[HMMTRAccessoryServerBrowser setConfiguredPreWarmTargetFabricID:]
- -[HMMTRAccessoryServerBrowser setCurrentFabricID:]
- -[HMMTRAccessoryServerBrowser setNocSigner:]
- -[HMMTRAccessoryServerBrowser setOwnerLocalOperationalKeyPair:]
- -[HMMTRAccessoryServerBrowser setPreWarmTargetIsSystemCommissionerFabric:]
- -[HMMTRAccessoryServerBrowser setPreWarmTargetToFabricWithID:isOwner:]
- -[HMMTRAccessoryServerBrowser setPreWarmTargetToSystemCommissionerFabric]
- -[HMMTRAccessoryServerBrowser setPreWarmedFabricID:]
- -[HMMTRAccessoryServerBrowser setUserOwnsConfiguredPreWarmTargetFabric:]
- -[HMMTRAccessoryServerBrowser setupStorageStateAfterCertFetchForHomeFabricID:completion:]
- -[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricID:]
- -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricID:]
- -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricID:completion:]
- -[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricID:]
- -[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]
- -[HMMTRAccessoryServerBrowser userOwnsConfiguredPreWarmTargetFabric]
- -[HMMTRCachedFabricCertificateData .cxx_destruct]
- -[HMMTRCachedFabricCertificateData fabricID]
- -[HMMTRCachedFabricCertificateData initWithFabricID:rootCert:operationalCert:ownerNode:ipk:]
- -[HMMTRCachedFabricCertificateData ipk]
- -[HMMTRCachedFabricCertificateData operationalCert]
- -[HMMTRCachedFabricCertificateData ownerNode]
- -[HMMTRCachedFabricCertificateData rootCert]
- -[HMMTRControllerData operationalCertificate]
- -[HMMTRControllerData setOperationalCertificate:]
- -[HMMTRControllerParameters setStartSuspended:]
- -[HMMTRControllerParameters startSuspended]
- -[HMMTRControllerWrapper cachedDeviceControllerShouldResume]
- -[HMMTRControllerWrapper isRVCEnabled]
- -[HMMTRControllerWrapper setCachedDeviceControllerShouldResume:]
- -[HMMTRDescriptorClusterManager hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:server:]
- -[HMMTRDoorLockClusterAPIRouter baseDevice]
- -[HMMTRDoorLockClusterAPIRouter baseDoorLock]
- -[HMMTRDoorLockClusterAPIRouter getAllAppleAliroCredentialsForUser:flow:]
- -[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsForUser:withCredentialType:startingAtIndex:credentials:flow:]
- -[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:flow:completion:]
- -[HMMTRDoorLockClusterAPIRouter initWithBaseDoorLock:baseDevice:queue:]
- -[HMMTRFabric _clearNewFabricData]
- -[HMMTRFabric _createNewFabricData]
- -[HMMTRFabric _getDataToPersist]
- -[HMMTRFabric _loadForPairingWithFetchFromResident:completion:]
- -[HMMTRFabric _loadFromDiskWithCompletion:]
- -[HMMTRFabric _loadFromRemoteWithCompletion:]
- -[HMMTRFabric _loadFromResidentWithCompletion:]
- -[HMMTRFabric _loadFromStorageWithCompletion:]
- -[HMMTRFabric createNewFabricIdentityWithCompletion:]
- -[HMMTRFabric isValid]
- -[HMMTRFabric loadFabricAndControllerDataForPairing:fetchFromResident:completion:]
- -[HMMTRFabric setStorage:]
- -[HMMTRFabric storage]
- -[HMMTRFabricConnectionRequest fabricID]
- -[HMMTRFabricConnectionRequest initWithQueue:browser:fabricID:systemCommissionerFabric:]
- -[HMMTRFabricDataFetcher .cxx_destruct]
- -[HMMTRFabricDataFetcher chipStorageDelegate]
- -[HMMTRFabricDataFetcher initWithCHIPStorageDelegate:keychainDelegate:]
- -[HMMTRFabricDataFetcher keychainDelegate]
- -[HMMTRFabricDataFetcher locallyStoredFabricDataWithError:]
- -[HMMTRFabricDataFetcher logIdentifier]
- -[HMMTRFabricDataFetcher setChipStorageDelegate:]
- -[HMMTRFabricDataFetcher setKeychainDelegate:]
- -[HMMTRFabricDataSnapshot initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:]
- -[HMMTRMatterKeypair reload]
- -[HMMTRMutableDeviceTopology storeForNodeId:server:]
- -[HMMTROperationalCertificateIssuer initWithQueue:rootCertificate:browser:]
- -[HMMTRPerControllerStorage fabric]
- -[HMMTRPerControllerStorage setFabric:]
- -[HMMTRPerControllerStorage setPrivateDataSource:]
- -[HMMTRPerControllerStorage setQueue:]
- -[HMMTRStorage _cachedOperationalCertificateIfValidForFabricID:]
- -[HMMTRStorage _cachedRootCertificateIfValidForFabricID:]
- -[HMMTRStorage _createOperationalCertificateForFabricID:rootCert:caseAuthenticatedTags:controllerNodeID:]
- -[HMMTRStorage _fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:]
- -[HMMTRStorage _operationalCertificateFromSdkCertificatesForFabricID:]
- -[HMMTRStorage _rootCertificateFromSdkCertificatesForFabricID:]
- -[HMMTRStorage areCachedCertificatesValidForFabricID:]
- -[HMMTRStorage caseAuthenticatedTagsUpdated]
- -[HMMTRStorage certificateIssuerID]
- -[HMMTRStorage fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:]
- -[HMMTRStorage fetchCertificatesFromStorageForFabricID:controllerNodeID:rootCert:operationalCert:residentNodeID:ipk:]
- -[HMMTRStorage ipkForFabricID:forPairing:]
- -[HMMTRStorage knownFabricInStorage:fabricID:keyPair:controllerNodeID:rootCertificate:]
- -[HMMTRStorage knownFabricWithID:]
- -[HMMTRStorage legacyNodeIDForFabricID:]
- -[HMMTRStorage nocSigner]
- -[HMMTRStorage operationalCertForCurrentFabric]
- -[HMMTRStorage operationalKeyPair]
- -[HMMTRStorage persistLegacyControllerNodeWithDictionary:]
- -[HMMTRStorage prepareStorageForFabricID:]
- -[HMMTRStorage prepareStorageForFabricID:forInitialSetup:]
- -[HMMTRStorage setCaseAuthenticatedTagsUpdated:]
- -[HMMTRStorage setCertificateIssuerID:]
- -[HMMTRStorage setNocSigner:]
- -[HMMTRStorage setOperationalKeyPair:]
- -[HMMTRStorage(Records) nodeIDForFabricID:deviceIdentifier:]
- -[HMMTRSyncClusterDoorLock _getUserAtIndex:includeAliroCredentials:flow:]
- -[HMMTRSyncClusterDoorLock baseDevice]
- -[HMMTRSyncClusterDoorLock baseDoorLock]
- -[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:]
- -[HMMTRSyncClusterDoorLock initWithDevice:baseDevice:endpoint:queue:accessoryServer:]
- -[HMMTRSyncClusterDoorLock readAttributeWithEndpointIDAndCompletion:clusterID:attributeID:completion:]
- -[HMMTRSyncClusterDoorLock setBaseDevice:]
- -[HMMTRSyncClusterDoorLock setBaseDoorLock:]
- -[HMMTRThreadRadioManager _notifyThreadRadioStateChanged:nodeType:fabricID:]
- -[HMMTRThreadRadioManager _startThreadRadioForHomeWithFabricID:preventDisconnect:]
- -[HMMTRThreadRadioManager _startThreadRadioForSystemCommissionerFabricID:]
- -[HMMTRThreadRadioManager _stopThreadRadioForHomeWithFabricID:]
- -[HMMTRThreadRadioManager _stopThreadRadioForSystemCommissionerFabricID:]
- -[HMMTRThreadRadioManager _updateFabricIDOfActiveThreadNetwork:isFabricIDOfSystemCommissioner:]
- -[HMMTRThreadRadioManager fabricIDOfActiveThreadNetwork]
- -[HMMTRThreadRadioManager fabricIDOfPendingStartPairingBlock]
- -[HMMTRThreadRadioManager hasMatterThreadAccessoryInHomeWithFabricID:]
- -[HMMTRThreadRadioManager notifyThreadRadioStateChanged:nodeType:fabricID:]
- -[HMMTRThreadRadioManager overrideLocationCheckForPairingForFabricID:]
- -[HMMTRThreadRadioManager setFabricIDOfActiveThreadNetwork:]
- -[HMMTRThreadRadioManager setFabricIDOfPendingStartPairingBlock:]
- -[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricID:]
- -[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricID:preventDisconnect:]
- -[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricID:]
- -[HMMTRThreadRadioManager stopThreadRadioForHomeWithFabricID:]
- -[HMMTRThreadRadioManager stopThreadRadioForSystemCommissionerFabricID:]
- -[HMMTRThreadSoftwareUpdateController isFirmwareUpdateInProgressForFabricID:]
- -[HMMTRThreadSoftwareUpdateController suspendOperationsForFabricID:]
- -[HMMTRVendorMetadataProduct initWithIdentifier:categoryNumber:]
- -[HMMTRVendorMetadataProduct invalid]
- -[HMMTRVendorMetadataProduct setInvalid:]
- GCC_except_table1027
- GCC_except_table1032
- GCC_except_table1063
- GCC_except_table1089
- GCC_except_table1097
- GCC_except_table1132
- GCC_except_table1165
- GCC_except_table1384
- GCC_except_table1425
- GCC_except_table1573
- GCC_except_table1574
- GCC_except_table1576
- GCC_except_table1595
- GCC_except_table1596
- GCC_except_table1597
- GCC_except_table1598
- GCC_except_table1599
- GCC_except_table1602
- GCC_except_table1605
- GCC_except_table1606
- GCC_except_table1607
- GCC_except_table1608
- GCC_except_table1609
- GCC_except_table1610
- GCC_except_table1611
- GCC_except_table1663
- GCC_except_table1671
- GCC_except_table1749
- GCC_except_table1831
- GCC_except_table1891
- GCC_except_table1901
- GCC_except_table1903
- GCC_except_table1951
- GCC_except_table1994
- GCC_except_table2056
- GCC_except_table2296
- GCC_except_table2302
- GCC_except_table2360
- GCC_except_table2418
- GCC_except_table2468
- GCC_except_table2470
- GCC_except_table2497
- GCC_except_table2498
- GCC_except_table2499
- GCC_except_table2517
- GCC_except_table2518
- GCC_except_table2519
- GCC_except_table2520
- GCC_except_table2521
- GCC_except_table2522
- GCC_except_table2537
- GCC_except_table2539
- GCC_except_table2545
- GCC_except_table2563
- GCC_except_table2576
- GCC_except_table2582
- GCC_except_table2595
- GCC_except_table2598
- GCC_except_table2618
- GCC_except_table2634
- GCC_except_table2640
- GCC_except_table2647
- GCC_except_table2666
- GCC_except_table3041
- GCC_except_table3046
- GCC_except_table3049
- GCC_except_table3062
- GCC_except_table3078
- GCC_except_table3140
- GCC_except_table3141
- GCC_except_table3166
- GCC_except_table3167
- GCC_except_table3210
- GCC_except_table3228
- GCC_except_table3231
- GCC_except_table3269
- GCC_except_table3273
- GCC_except_table3289
- GCC_except_table3291
- GCC_except_table3318
- GCC_except_table3378
- GCC_except_table3424
- GCC_except_table3438
- GCC_except_table3465
- GCC_except_table3469
- GCC_except_table3484
- GCC_except_table3485
- GCC_except_table3490
- GCC_except_table3497
- GCC_except_table3545
- GCC_except_table3565
- GCC_except_table3615
- GCC_except_table3620
- GCC_except_table3623
- GCC_except_table3748
- GCC_except_table3751
- GCC_except_table3886
- GCC_except_table3891
- GCC_except_table3897
- GCC_except_table3901
- GCC_except_table3929
- GCC_except_table3951
- GCC_except_table404
- GCC_except_table571
- GCC_except_table574
- GCC_except_table634
- GCC_except_table635
- GCC_except_table636
- GCC_except_table676
- GCC_except_table737
- GCC_except_table743
- GCC_except_table745
- GCC_except_table747
- GCC_except_table749
- GCC_except_table753
- GCC_except_table757
- GCC_except_table765
- GCC_except_table789
- GCC_except_table795
- GCC_except_table797
- GCC_except_table899
- GCC_except_table960
- OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._fabricID
- OBJC_IVAR_$_HMMTRAccessoryServer._pairingTargetHomeUUID
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._configuredPreWarmTargetFabricID
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._currentFabricID
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._nocSigner
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._ownerLocalOperationalKeyPair
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._preWarmTargetIsSystemCommissionerFabric
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._preWarmedFabricID
- OBJC_IVAR_$_HMMTRAccessoryServerBrowser._userOwnsConfiguredPreWarmTargetFabric
- OBJC_IVAR_$_HMMTRCachedFabricCertificateData._fabricID
- OBJC_IVAR_$_HMMTRCachedFabricCertificateData._ipk
- OBJC_IVAR_$_HMMTRCachedFabricCertificateData._operationalCert
- OBJC_IVAR_$_HMMTRCachedFabricCertificateData._ownerNode
- OBJC_IVAR_$_HMMTRCachedFabricCertificateData._rootCert
- OBJC_IVAR_$_HMMTRControllerData._operationalCertificate
- OBJC_IVAR_$_HMMTRControllerParameters._startSuspended
- OBJC_IVAR_$_HMMTRControllerWrapper._cachedDeviceControllerShouldResume
- OBJC_IVAR_$_HMMTRDoorLockClusterAPIRouter._baseDevice
- OBJC_IVAR_$_HMMTRDoorLockClusterAPIRouter._baseDoorLock
- OBJC_IVAR_$_HMMTRFabric._storage
- OBJC_IVAR_$_HMMTRFabric._targetFabricUUID
- OBJC_IVAR_$_HMMTRFabricConnectionRequest._fabricID
- OBJC_IVAR_$_HMMTRFabricDataFetcher._chipStorageDelegate
- OBJC_IVAR_$_HMMTRFabricDataFetcher._keychainDelegate
- OBJC_IVAR_$_HMMTRPerControllerStorage._fabric
- OBJC_IVAR_$_HMMTRStorage._caseAuthenticatedTagsUpdated
- OBJC_IVAR_$_HMMTRStorage._certificateIssuerID
- OBJC_IVAR_$_HMMTRStorage._nocSigner
- OBJC_IVAR_$_HMMTRStorage._operationalKeyPair
- OBJC_IVAR_$_HMMTRSyncClusterDoorLock._baseDevice
- OBJC_IVAR_$_HMMTRSyncClusterDoorLock._baseDoorLock
- OBJC_IVAR_$_HMMTRThreadRadioManager._fabricIDOfActiveThreadNetwork
- OBJC_IVAR_$_HMMTRThreadRadioManager._fabricIDOfPendingStartPairingBlock
- _OBJC_CLASS_$_HMMTRCachedFabricCertificateData
- _OBJC_CLASS_$_HMMTRFabricDataFetcher
- _OBJC_CLASS_$_MTRBaseClusterDoorLock
- _OBJC_CLASS_$_MTRDoorLockClusterDlCredential
- _OBJC_METACLASS_$_HMMTRCachedFabricCertificateData
- _OBJC_METACLASS_$_HMMTRFabricDataFetcher
- __100-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.285
- __100-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.289
- __100-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.292
- __101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.939
- __101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.942
- __101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.880
- __102-[HMMTRSyncClusterDoorLock updateSchedulesForUserIndex:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.297
- __105-[HMMTRSyncClusterDoorLock updateSchedulesOfScheduleType:withRequestedSchedules:forUserAtUserIndex:flow:]_block_invoke.358
- __107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.223
- __107-[HMMTRSyncClusterDoorLock setScheduleOfScheduleType:withSchedule:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.410
- __109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.142
- __109-[HMMTRDescriptorClusterManager fetchHAPCategoryWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.147
- __110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.229
- __111-[HMMTRDescriptorClusterManager _updateOTARequestorEndpointsInTopology:device:callbackQueue:completionHandler:]_block_invoke.282
- __113-[HMMTRSyncClusterDoorLock findOperationOrderForModifyingWeekDaySchedules:andYearDaySchedules:forUserIndex:flow:]_block_invoke.354
- __114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.396
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.570
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.571
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.573
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.577
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.579
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.585
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.588
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.574
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.578
- __119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.580
- __119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.215
- __131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.272
- __131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.275
- __132-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:rootCertificate:completionHandler:]_block_invoke.438
- __133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.109
- __133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.112
- __134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.276
- __140-[HMMTRDescriptorClusterManager _runBlockForAllEndpointsWithClusterID:endpoints:device:callbackQueue:finishedRunningAllBlocksPromise:block:]_block_invoke.360
- __146-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]_block_invoke.382
- __146-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]_block_invoke.388
- __146-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]_block_invoke.389
- __146-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]_block_invoke_2.390
- __147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.122
- __147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.123
- __147-[HMMTRProtocolOperationManager registerOperation:accessoryServer:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.127
- __149-[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:]_block_invoke.414
- __149-[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:]_block_invoke.420
- __149-[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:]_block_invoke.421
- __149-[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:]_block_invoke.422
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.397
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.399
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.401
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.402
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.403
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.404
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.405
- __155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.406
- __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.293
- __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.295
- __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.301
- __198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.296
- __242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.248
- __254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.196
- __280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.227
- __37-[HMMTRAccessoryServer finishPairing]_block_invoke.805
- __37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.273
- __39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke.279
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.690
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.691
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.694
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.695
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.699
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.700
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.703
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.704
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.696
- __40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.705
- __40-[HMMTRAccessoryServerBrowser configure]_block_invoke.124
- __40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.32
- __42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.348
- __42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.352
- __42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.517
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.224
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.232
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.236
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.246
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.239
- __43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.329
- __43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.334
- __43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_3.335
- __43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.344
- __45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.305
- __45-[HMMTRFabric _loadFromRemoteWithCompletion:]_block_invoke.47
- __45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.33
- __45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.36
- __47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.1025
- __47-[HMMTRControllerWrapper replaceStartupParams:]_block_invoke.91
- __49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.381
- __49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.469
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.858
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.861
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.862
- __51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.1026
- __51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke.38
- __52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.688
- __52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.357
- __52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.358
- __52-[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]_block_invoke.9
- __53-[HMMTRSyncClusterDoorLock fetchAccessoryColor_flow:]_block_invoke.218
- __54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.252
- __55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.1022
- __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.465
- __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.466
- __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.467
- __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.470
- __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.471
- __56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.472
- __56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.30
- __57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.201
- __58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.279
- __58-[HMMTRStorage prepareStorageForFabricID:forInitialSetup:]_block_invoke.27
- __58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.265
- __58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke.142
- __58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke_2.143
- __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.485
- __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.486
- __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.487
- __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.491
- __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.494
- __59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.495
- __59-[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]_block_invoke.466
- __59-[HMMTRSyncClusterDoorLock readSchedulesForUserIndex:flow:]_block_invoke.300
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.943
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.947
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.952
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.959
- __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.473
- __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.474
- __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.475
- __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.476
- __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.479
- __60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.484
- __60-[HMMTRAccessoryServerBrowser configureControllerForFabric:]_block_invoke.126
- __62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.168
- __62-[HMMTRIdentifyDevice identifyWithEndpoint:completionHandler:]_block_invoke.80
- __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.852
- __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.853
- __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.543
- __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.544
- __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.545
- __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.546
- __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.551
- __63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.552
- __63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.163
- __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.507
- __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.508
- __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.509
- __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.512
- __64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.513
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.974
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.975
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.976
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.977
- __64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.138
- __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.502
- __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.503
- __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.504
- __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.505
- __66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.506
- __66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.447
- __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.496
- __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.497
- __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.498
- __68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.501
- __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.333
- __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.532
- __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.533
- __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.534
- __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.537
- __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.541
- __69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.542
- __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.454
- __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.460
- __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.461
- __69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.462
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.169
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.172
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.178
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.180
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.182
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.179
- __69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.181
- __69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.249
- __71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke.378
- __71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke.379
- __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.429
- __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.435
- __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.438
- __72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.441
- __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.520
- __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.521
- __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.522
- __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.526
- __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.530
- __72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.531
- __72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.252
- __72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.259
- __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.173
- __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.174
- __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.175
- __72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.176
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.845
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.846
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.850
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.851
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.847
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.828
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.829
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.838
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.839
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.843
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.844
- __73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.376
- __73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.377
- __73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.449
- __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.151
- __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.152
- __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.156
- __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.157
- __74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.164
- __75+[HMMTRSyncClusterDoorLock validateFutureResults:ofClass:areNullable:flow:]_block_invoke.321
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.312
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.313
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.314
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.318
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.321
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.322
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.325
- __76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.315
- __76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.185
- __76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.190
- __76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke_2.191
- __77-[HMMTRDoorLockClusterAPIRouter isCustomClusterAvailableWithFlow:completion:]_block_invoke.3
- __78-[HMMTRDoorLockClusterAPIRouter fetchAppleClusterFeaturesWithFlow:completion:]_block_invoke.12
- __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.443
- __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.445
- __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.446
- __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.452
- __79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.453
- __79-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumeration:]_block_invoke.826
- __79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.375
- __79-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:]_block_invoke.269
- __80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.274
- __81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.369
- __81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.372
- __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.960
- __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.962
- __82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke.212
- __82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.151
- __82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.153
- __82-[HMMTRFabric loadFabricAndControllerDataForPairing:fetchFromResident:completion:]_block_invoke.6
- __82-[HMMTRFabric loadFabricAndControllerDataForPairing:fetchFromResident:completion:]_block_invoke.8
- __82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.252
- __82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.253
- __82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.254
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.910
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.911
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.914
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.923
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.924
- __83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.883
- __84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.409
- __84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.411
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.925
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.926
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.927
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.928
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.934
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.935
- __84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke.210
- __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.980
- __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.981
- __86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.394
- __88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.450
- __88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.451
- __88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.452
- __89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.395
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.278
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.281
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.283
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.288
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke_2.282
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke_2.284
- __90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke_2.289
- __91-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:flow:completion:]_block_invoke.17
- __91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.399
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.591
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.592
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.593
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.594
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.597
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.600
- __92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.601
- __93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.448
- __93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.349
- __94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.877
- __94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.160
- __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.419
- __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke_2.424
- __95-[HMMTRStorage _fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:]_block_invoke.60
- __96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.351
- __96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.401
- __96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.399
- __96-[HMMTRSyncClusterDoorLock clearScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.409
- __99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke.207
- __99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.402
- __Block_byref_object_copy_.10620
- __Block_byref_object_copy_.10806
- __Block_byref_object_copy_.2726
- __Block_byref_object_copy_.2873
- __Block_byref_object_copy_.3029
- __Block_byref_object_copy_.3986
- __Block_byref_object_copy_.5103
- __Block_byref_object_copy_.6005
- __Block_byref_object_copy_.6350
- __Block_byref_object_copy_.6718
- __Block_byref_object_copy_.7594
- __Block_byref_object_copy_.8499
- __Block_byref_object_copy_.9267
- __Block_byref_object_copy_.9880
- __Block_byref_object_dispose_.10621
- __Block_byref_object_dispose_.10807
- __Block_byref_object_dispose_.2727
- __Block_byref_object_dispose_.2874
- __Block_byref_object_dispose_.3030
- __Block_byref_object_dispose_.3987
- __Block_byref_object_dispose_.5104
- __Block_byref_object_dispose_.6006
- __Block_byref_object_dispose_.6351
- __Block_byref_object_dispose_.6719
- __Block_byref_object_dispose_.7595
- __Block_byref_object_dispose_.8500
- __Block_byref_object_dispose_.9268
- __Block_byref_object_dispose_.9881
- __OBJC_$_CLASS_METHODS_HMMTRFabricDataFetcher
- __OBJC_$_INSTANCE_METHODS_HMMTRCachedFabricCertificateData
- __OBJC_$_INSTANCE_METHODS_HMMTRFabricDataFetcher
- __OBJC_$_INSTANCE_METHODS_HMMTROperationalCertificateIssuer
- __OBJC_$_INSTANCE_VARIABLES_HMMTRCachedFabricCertificateData
- __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricDataFetcher
- __OBJC_$_PROP_LIST_HMMTRCachedFabricCertificateData
- __OBJC_$_PROP_LIST_HMMTRFabricDataFetcher
- __OBJC_$_PROP_LIST_HMMTRFabricDataFetcherKeychainDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRFabricDataFetcherKeychainDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTRKeypair
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRFabricDataFetcherKeychainDelegate
- __OBJC_$_PROTOCOL_REFS_MTRPersistentStorageDelegate
- __OBJC_CLASS_RO_$_HMMTRCachedFabricCertificateData
- __OBJC_CLASS_RO_$_HMMTRFabricDataFetcher
- __OBJC_LABEL_PROTOCOL_$_HMMTRFabricDataFetcherKeychainDelegate
- __OBJC_LABEL_PROTOCOL_$_MTRPersistentStorageDelegate
- __OBJC_METACLASS_RO_$_HMMTRCachedFabricCertificateData
- __OBJC_METACLASS_RO_$_HMMTRFabricDataFetcher
- __OBJC_PROTOCOL_$_HMMTRFabricDataFetcherKeychainDelegate
- __OBJC_PROTOCOL_$_MTRPersistentStorageDelegate
- ___100-[HMMTRAccessoryServer _writeCharacteristicValues:responseTuples:completionQueue:completionHandler:]_block_invoke_3
- ___100-[HMMTRAccessoryServer _writeCharacteristicValues:responseTuples:completionQueue:completionHandler:]_block_invoke_4
- ___100-[HMMTRAccessoryServerBrowser _handleClientsRemovedWithFabricID:updateConnectionIdleTimeout:reason:]_block_invoke
- ___100-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke
- ___100-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke_2
- ___117-[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsForUser:withCredentialType:startingAtIndex:credentials:flow:]_block_invoke
- ___121-[HMMTRSyncClusterDoorLock findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:flow:]_block_invoke
- ___132-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:rootCertificate:completionHandler:]_block_invoke
- ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke_2
- ___136-[HMMTRAccessoryServerBrowser handlePairingCompletionForAccessoryWithNodeID:fabricID:vendorID:productID:configNumber:category:topology:]_block_invoke
- ___138-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForSharedAdminWithDeviceNodeID:forOwner:publicKey:fabricID:completionHandler:]_block_invoke
- ___139-[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:flow:]_block_invoke
- ___146-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
- ___146-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]_block_invoke
- ___146-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:]_block_invoke_2
- ___149-[HMMTRAccessoryServerBrowser fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:]_block_invoke
- ___37+[HMMTRFabricDataFetcher logCategory]_block_invoke
- ___43-[HMMTRFabric _loadFromDiskWithCompletion:]_block_invoke
- ___43-[HMMTRFabric _loadFromDiskWithCompletion:]_block_invoke_2
- ___45-[HMMTRFabric _loadFromRemoteWithCompletion:]_block_invoke
- ___48-[HMMTRControllerFactory disableNormalOperation]_block_invoke
- ___49-[HMMTRAccessoryServerBrowser clearPreWarmTarget]_block_invoke
- ___52-[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]_block_invoke_2
- ___53-[HMMTRFabric createNewFabricIdentityWithCompletion:]_block_invoke
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke_3
- ___56-[HMMTRAccessoryServerBrowser _isNodeIDPaired:fabricID:]_block_invoke
- ___57-[HMMTRSyncClusterDoorLock fetchReaderGroupSubIdentifier]_block_invoke_2
- ___58-[HMMTRStorage prepareStorageForFabricID:forInitialSetup:]_block_invoke
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke_3
- ___59-[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]_block_invoke
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke_2
- ___60-[HMMTRAccessoryServerBrowser configureControllerForFabric:]_block_invoke
- ___60-[HMMTRAccessoryServerBrowser configureControllerForFabric:]_block_invoke_2
- ___61-[HMMTRSyncClusterDoorLock fetchAccessorySupportsTapToUnlock]_block_invoke_2
- ___62-[HMMTRThreadRadioManager stopThreadRadioForHomeWithFabricID:]_block_invoke
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke_5
- ___63-[HMMTRAccessoryServerBrowser createNewFabricIDWithCompletion:]_block_invoke
- ___63-[HMMTRFabric _loadForPairingWithFetchFromResident:completion:]_block_invoke
- ___63-[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricID:]_block_invoke
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke_3
- ___64-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricID:]_block_invoke
- ___65-[HMMTRAccessoryServerBrowser _isDeviceIDPaired:nodeID:fabricID:]_block_invoke
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke_3
- ___66-[HMMTRAccessoryServerBrowser nodeIDForFabricID:deviceIdentifier:]_block_invoke
- ___68-[HMMTRAccessoryServerBrowser addFabricWithActiveClientForFabricID:]_block_invoke
- ___68-[HMMTRAccessoryServerBrowser cacheOperationalCertificate:fabricID:]_block_invoke
- ___69-[HMMTRAccessoryServer(DiagnosticsInternal) _handleDiagnosticsEvent:]_block_invoke
- ___70-[HMMTRAccessoryServerBrowser setPreWarmTargetToFabricWithID:isOwner:]_block_invoke
- ___70-[HMMTRThreadRadioManager overrideLocationCheckForPairingForFabricID:]_block_invoke
- ___71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke
- ___72-[HMMTRAccessoryServerBrowser getNOCFromResidentForSharedUserForFabric:]_block_invoke
- ___72-[HMMTRThreadRadioManager stopThreadRadioForSystemCommissionerFabricID:]_block_invoke
- ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke
- ___73-[HMMTRAccessoryServerBrowser setPreWarmTargetToSystemCommissionerFabric]_block_invoke
- ___73-[HMMTRDoorLockClusterAPIRouter getAllAppleAliroCredentialsForUser:flow:]_block_invoke
- ___73-[HMMTRDoorLockClusterAPIRouter getAllAppleAliroCredentialsForUser:flow:]_block_invoke_2
- ___73-[HMMTRSyncClusterDoorLock _getUserAtIndex:includeAliroCredentials:flow:]_block_invoke
- ___73-[HMMTRSyncClusterDoorLock _getUserAtIndex:includeAliroCredentials:flow:]_block_invoke_2
- ___73-[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricID:]_block_invoke
- ___75-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricID:completion:]_block_invoke
- ___75-[HMMTRThreadRadioManager notifyThreadRadioStateChanged:nodeType:fabricID:]_block_invoke
- ___76-[HMMTRThreadRadioManager _notifyThreadRadioStateChanged:nodeType:fabricID:]_block_invoke
- ___78-[HMMTRAccessoryServer(Diagnostics) _readPastEventsFromAccessory:forClusters:]_block_invoke_2
- ___81-[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricID:preventDisconnect:]_block_invoke
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke_2
- ___82-[HMMTRAccessoryServerBrowser handlePairingForThreadAccessoryWithFabricID:nodeID:]_block_invoke
- ___82-[HMMTRFabric loadFabricAndControllerDataForPairing:fetchFromResident:completion:]_block_invoke
- ___82-[HMMTRFabric loadFabricAndControllerDataForPairing:fetchFromResident:completion:]_block_invoke_2
- ___84-[HMMTRAccessoryServerBrowser createMatterOperationalKeyPairIfAbsentWithCompletion:]_block_invoke
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke_2
- ___88-[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricID:]_block_invoke
- ___89-[HMMTRAccessoryServerBrowser setupStorageStateAfterCertFetchForHomeFabricID:completion:]_block_invoke
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke_2
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke_3
- ___91-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:flow:completion:]_block_invoke
- ___91-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:flow:completion:]_block_invoke_2
- ___91-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:flow:completion:]_block_invoke_3
- ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke
- ___94-[HMMTRAccessoryServerBrowser fetchCachedOperationalCertificateForFabricID:completionHandler:]_block_invoke
- ___94-[HMMTRStorage fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:]_block_invoke
- ___94-[HMMTRStorage fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:]_block_invoke_2
- ___95-[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricID:]_block_invoke
- ___95-[HMMTRStorage _fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88r96r_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s_e5_v8?0l
- ___block_descriptor_32_e47_B32?0"MTRDoorLockClusterDlCredential"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e42_v16?0"HMMTRCachedFabricCertificateData"8l
- ___block_descriptor_40_e8_32bs_e51_v40?0"NSData"8"NSData"16"NSNumber"24"NSData"32l
- ___block_descriptor_40_e8_32s_e27_"NAFuture"16?0"NSArray"8l
- ___block_descriptor_40_e8_32s_e42_{_HMFFutureBlockOutcome=q}16?0"NSData"8l
- ___block_descriptor_40_e8_32s_e48_{_HMFFutureBlockOutcome=q}16?0"NSDictionary"8l
- ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32s40bs_e18_v16?0"NSNumber"8l
- ___block_descriptor_48_e8_32s40bs_e31_{_HMFFutureBlockOutcome=q}8?0l
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e35_v24?0"MTRBaseDevice"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e42_v16?0"HMMTRCachedFabricCertificateData"8l
- ___block_descriptor_48_e8_32s40bs_e51_v40?0"NSData"8"NSData"16"NSNumber"24"NSData"32l
- ___block_descriptor_48_e8_32s40bs_e59_v36?0"HMMTRHAPAccessoryInfo"8B16"NSNumber"20"NSError"28l
- ___block_descriptor_48_e8_32s40s_e35_v24?0"MTRBaseDevice"8"NSError"16l
- ___block_descriptor_48_e8_32s40s_e48_{_HMFFutureBlockOutcome=q}16?0"NSDictionary"8l
- ___block_descriptor_49_e8_32s_e5_v8?0l
- ___block_descriptor_50_e8_32s40bs_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8l
- ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"MTRBaseDevice"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48s_e27_"NAFuture"16?0"NSArray"8l
- ___block_descriptor_56_e8_32s40s48s_e35_v24?0"MTRBaseDevice"8"NSError"16l
- ___block_descriptor_57_e8_32s40s_e16_"HMFFuture"8?0l
- ___block_descriptor_58_e8_32s40s48s_e17_v16?0"NSError"8l
- ___block_descriptor_59_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s56s_e30_v24?0"NSNumber"8"NSError"16l
- ___block_descriptor_65_e8_32s40s48s56bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_72_e8_32s40s48bs56r64r_e35_v24?0"MTRBaseDevice"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e33_v28?0"NSNumber"8B16"NSError"20l
- ___block_descriptor_72_e8_32s40s48s56s64s_e16_"HMFFuture"8?0l
- ___block_descriptor_72_e8_32s40s48s56s64s_e60_{_HMFFutureBlockOutcome=q}16?0"FindOrAddHomeUserResults"8l
- ___block_descriptor_73_e8_32s40s48s56s_e16_"HMFFuture"8?0l
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8l
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e35_v24?0"MTRBaseDevice"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56s_e71_"NAFuture"16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
- ___block_descriptor_80_e8_32s40s48s56s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8l
- ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0l
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0l
- ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s_e18_v16?0"NSNumber"8l
- ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
- ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0l
- __block_literal_global.10077
- __block_literal_global.10191
- __block_literal_global.1043
- __block_literal_global.10679
- __block_literal_global.1084
- __block_literal_global.1161
- __block_literal_global.127.5451
- __block_literal_global.136
- __block_literal_global.1360
- __block_literal_global.1615
- __block_literal_global.1699
- __block_literal_global.182
- __block_literal_global.183
- __block_literal_global.2050
- __block_literal_global.214
- __block_literal_global.2211
- __block_literal_global.238
- __block_literal_global.242
- __block_literal_global.2445
- __block_literal_global.256
- __block_literal_global.258
- __block_literal_global.267
- __block_literal_global.2682
- __block_literal_global.2756
- __block_literal_global.2932
- __block_literal_global.308
- __block_literal_global.3116
- __block_literal_global.318
- __block_literal_global.3235
- __block_literal_global.329
- __block_literal_global.331
- __block_literal_global.332
- __block_literal_global.3343
- __block_literal_global.344
- __block_literal_global.366
- __block_literal_global.368
- __block_literal_global.378
- __block_literal_global.4081
- __block_literal_global.414
- __block_literal_global.422
- __block_literal_global.426
- __block_literal_global.434
- __block_literal_global.4368
- __block_literal_global.4502
- __block_literal_global.46.8301
- __block_literal_global.4603
- __block_literal_global.471
- __block_literal_global.477
- __block_literal_global.480
- __block_literal_global.4855
- __block_literal_global.5232
- __block_literal_global.5361
- __block_literal_global.548
- __block_literal_global.5593
- __block_literal_global.5605
- __block_literal_global.5843
- __block_literal_global.5905
- __block_literal_global.6052
- __block_literal_global.6162
- __block_literal_global.6241
- __block_literal_global.6544
- __block_literal_global.6729
- __block_literal_global.7057
- __block_literal_global.715
- __block_literal_global.7625
- __block_literal_global.808
- __block_literal_global.82.8302
- __block_literal_global.8300
- __block_literal_global.831
- __block_literal_global.8382
- __block_literal_global.9006
- __block_literal_global.9512
- __block_literal_global.9739
- __block_literal_global.992
- __block_literal_global.9935
- _getLowestError
- _objc_msgSend$_abortAllOperationsForFabricID:reason:
- _objc_msgSend$_cachedOperationalCertificateIfValidForFabricID:
- _objc_msgSend$_cachedRootCertificateIfValidForFabricID:
- _objc_msgSend$_clearNewFabricData
- _objc_msgSend$_connectPendingFabricConnectionsForFabricID:
- _objc_msgSend$_createFabricKeyPairsIfAbsent
- _objc_msgSend$_createNewFabricData
- _objc_msgSend$_createOperationalCertificateForFabricID:rootCert:caseAuthenticatedTags:controllerNodeID:
- _objc_msgSend$_createOperationalKeyPairIfAbsent
- _objc_msgSend$_currentHomeFabricDeviceControllerStartupParams
- _objc_msgSend$_currentHomeFabricDeviceControllerStartupParams1
- _objc_msgSend$_currentHomeFabricDeviceControllerStartupParams2
- _objc_msgSend$_fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:
- _objc_msgSend$_getDataToPersist
- _objc_msgSend$_getRandomFabricId
- _objc_msgSend$_getUserAtIndex:includeAliroCredentials:flow:
- _objc_msgSend$_handleClientsRemovedWithFabricID:updateConnectionIdleTimeout:reason:
- _objc_msgSend$_isDeviceIDPaired:nodeID:fabricID:
- _objc_msgSend$_isNodeIDPaired:fabricID:
- _objc_msgSend$_loadFabricKeyPairs
- _objc_msgSend$_loadForPairingWithFetchFromResident:completion:
- _objc_msgSend$_loadFromDiskWithCompletion:
- _objc_msgSend$_loadFromRemoteWithCompletion:
- _objc_msgSend$_loadFromResidentWithCompletion:
- _objc_msgSend$_loadFromStorageWithCompletion:
- _objc_msgSend$_notifyThreadRadioStateChanged:nodeType:fabricID:
- _objc_msgSend$_operationalCertificateFromSdkCertificatesForFabricID:
- _objc_msgSend$_prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:
- _objc_msgSend$_rootCertificateFromSdkCertificatesForFabricID:
- _objc_msgSend$_setupAndPersistStorageStateForHomeFabricID:completion:
- _objc_msgSend$_setupStorageStateAfterCertFetchForHomeFabricID:completion:
- _objc_msgSend$_setupStorageStateForHomeFabricID:
- _objc_msgSend$_setupStorageStateForUpdatedHomeFabricID:
- _objc_msgSend$_setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:
- _objc_msgSend$_setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:overrideAccessoryControlAllowed:
- _objc_msgSend$_setupStorageStateIfNotFabricID:rediscoverAccessories:
- _objc_msgSend$_startThreadRadioForHomeWithFabricID:preventDisconnect:
- _objc_msgSend$_startThreadRadioForSystemCommissionerFabricID:
- _objc_msgSend$_stopSystemCommissionerFabricID:reason:
- _objc_msgSend$_stopThreadRadioForHomeWithFabricID:
- _objc_msgSend$_stopThreadRadioForSystemCommissionerFabricID:
- _objc_msgSend$_suspendOperationsForFabricID:
- _objc_msgSend$_updateFabricIDOfActiveThreadNetwork:isFabricIDOfSystemCommissioner:
- _objc_msgSend$accessoryServerBrowser:cacheOperationalCertData:forFabricID:
- _objc_msgSend$accessoryServerBrowser:getCachedOperationalCertificateDataForFabricID:completion:
- _objc_msgSend$addFabricWithActiveClientForFabricID:
- _objc_msgSend$appleGetAliroCredentialStatusWithParams:completion:
- _objc_msgSend$appleHomeFabricRootPublicKey
- _objc_msgSend$appleHomeFabricWithID:
- _objc_msgSend$appleHomeFabricWithUUID:
- _objc_msgSend$appleSetAliroCredentialWithParams:completion:
- _objc_msgSend$appleSetAliroReaderConfigWithParams:completion:
- _objc_msgSend$areCachedCertificatesValidForFabricID:
- _objc_msgSend$baseDevice
- _objc_msgSend$baseDoorLock
- _objc_msgSend$cacheOperationalCertificate:fabricID:
- _objc_msgSend$cachedDeviceControllerShouldResume
- _objc_msgSend$caseAuthenticatedTagsUpdated
- _objc_msgSend$certificateIssuerID
- _objc_msgSend$clearCredentialWithParams:expectedValues:expectedValueInterval:completionHandler:
- _objc_msgSend$colorFromAttributeResponse:
- _objc_msgSend$configuredPreWarmTargetFabricID
- _objc_msgSend$connectToAccessoryWithExtendedMACAddress:withFabricID:completion:
- _objc_msgSend$controllerEntityIdentifier
- _objc_msgSend$createMatterOperationalKeyPairIfAbsentWithCompletion:
- _objc_msgSend$createNewFabricIdentityWithCompletion:
- _objc_msgSend$currentDeviceControllerNodeID
- _objc_msgSend$currentFabricID
- _objc_msgSend$deRegisterFromSleepWake:
- _objc_msgSend$fabricIDOfActiveThreadNetwork
- _objc_msgSend$fabricIDOfPendingStartPairingBlock
- _objc_msgSend$fetchCachedOperationalCertificateForFabricID:completionHandler:
- _objc_msgSend$fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:
- _objc_msgSend$fetchCertificatesFromStorageForFabricID:controllerNodeID:rootCert:operationalCert:residentNodeID:ipk:
- _objc_msgSend$fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:rootCertificate:completionHandler:
- _objc_msgSend$fetchCommissioningCertificatesForSharedAdminWithDeviceNodeID:forOwner:publicKey:fabricID:completionHandler:
- _objc_msgSend$fetchCommissioningCertificatesFromOwnerForPublicKey:fabricID:completionHandler:
- _objc_msgSend$fetchOperationalCertificatesForNewFabricWithFabricID:publicKey:fetchFromResident:completion:
- _objc_msgSend$getAllAppleAliroCredentialsForUser:flow:
- _objc_msgSend$getAppleAliroCredentialsForUser:withCredentialType:startingAtIndex:credentials:flow:
- _objc_msgSend$getBaseDevice:queue:completionHandler:
- _objc_msgSend$getCredentialStatusWithParams:completion:
- _objc_msgSend$getNOCFromResidentForSharedUserForFabric:
- _objc_msgSend$getThreadNetworkConnectionStateWithFabricID:
- _objc_msgSend$getThreadNetworkNodeTypeWithFabricID:
- _objc_msgSend$getUserWithParams:completion:
- _objc_msgSend$getUserWithParams:includeAliroCredentials:flow:completion:
- _objc_msgSend$handleEventReportForNotification:
- _objc_msgSend$handleStartUpWithEventNumber:
- _objc_msgSend$hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:server:
- _objc_msgSend$hasMatterThreadAccessoryInHomeWithFabricID:
- _objc_msgSend$initAsDeviceLocal
- _objc_msgSend$initWithBaseDoorLock:baseDevice:queue:
- _objc_msgSend$initWithDevice:baseDevice:endpoint:queue:accessoryServer:
- _objc_msgSend$initWithFabricID:rootCert:operationalCert:ownerNode:ipk:
- _objc_msgSend$initWithIdentifier:categoryNumber:
- _objc_msgSend$initWithQueue:browser:fabricID:systemCommissionerFabric:
- _objc_msgSend$initWithQueue:fabric:
- _objc_msgSend$initWithQueue:rootCertificate:browser:
- _objc_msgSend$initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:
- _objc_msgSend$invalidateCachedData
- _objc_msgSend$ipkForCurrentFabric
- _objc_msgSend$ipkForFabricID:forPairing:
- _objc_msgSend$isCurrentDeviceMobileAndResidentReachable
- _objc_msgSend$isCurrentDeviceMobileAndResidentReachableAndThreadCapableForFabric:
- _objc_msgSend$isFirmwareUpdateInProgressForFabricID:
- _objc_msgSend$isHAPError
- _objc_msgSend$isOwnerForHomeWithFabric:
- _objc_msgSend$isPrimaryResidentNodeReachableAndThreadCapable
- _objc_msgSend$isRVCEnabled
- _objc_msgSend$isSuspended
- _objc_msgSend$isValid
- _objc_msgSend$legacyNodeIDForFabricID:
- _objc_msgSend$loadFabricAndControllerDataForPairing:fetchFromResident:completion:
- _objc_msgSend$nodeIDForFabricID:deviceIdentifier:
- _objc_msgSend$operationalCertForCurrentFabric
- _objc_msgSend$overrideLocationCheckForPairingForFabricID:
- _objc_msgSend$ownerLocalOperationalKeyPair
- _objc_msgSend$ownerNode
- _objc_msgSend$ownerNodeID
- _objc_msgSend$pairingTargetHomeUUID
- _objc_msgSend$persistLegacyControllerNodeWithDictionary:
- _objc_msgSend$preWarmTargetIsSystemCommissionerFabric
- _objc_msgSend$preWarmedFabricID
- _objc_msgSend$prepareStorageForFabricID:
- _objc_msgSend$prepareStorageForFabricID:forInitialSetup:
- _objc_msgSend$productFinishFromAttributeResponse:
- _objc_msgSend$readAttributeAliroGroupResolvingKeyWithCompletion:
- _objc_msgSend$readAttributeAliroReaderGroupIdentifierWithCompletion:
- _objc_msgSend$readAttributeAliroReaderGroupSubIdentifierWithCompletion:
- _objc_msgSend$readAttributeAliroReaderVerificationKeyWithCompletion:
- _objc_msgSend$readAttributeAppleAliroGroupResolvingKeyWithCompletion:
- _objc_msgSend$readAttributeAppleAliroReaderGroupIdentifierWithCompletion:
- _objc_msgSend$readAttributeAppleAliroReaderVerificationKeyWithCompletion:
- _objc_msgSend$readAttributeWithEndpointIDAndCompletion:clusterID:attributeID:completion:
- _objc_msgSend$readReaderConfigWithFlow:
- _objc_msgSend$reload
- _objc_msgSend$removeActiveClientWithFabricID:updateConnectionIdleTimeout:reason:
- _objc_msgSend$removeActiveSecondaryClientWithFabricID:updateConnectionIdleTimeout:reason:
- _objc_msgSend$rootCertForCurrentFabric
- _objc_msgSend$setAliroReaderConfigWithParams:completion:
- _objc_msgSend$setCachedDeviceControllerShouldResume:
- _objc_msgSend$setCaseAuthenticatedTagsUpdated:
- _objc_msgSend$setCertificateIssuerID:
- _objc_msgSend$setConfiguredPreWarmTargetFabricID:
- _objc_msgSend$setControllerNodeID:
- _objc_msgSend$setCredentialWithParams:completion:
- _objc_msgSend$setCurrentFabricID:
- _objc_msgSend$setFabricCreationInProgress:
- _objc_msgSend$setFabricIDOfActiveThreadNetwork:
- _objc_msgSend$setFabricIDOfPendingStartPairingBlock:
- _objc_msgSend$setIpk:
- _objc_msgSend$setNocSigner:
- _objc_msgSend$setOperationalCertificate:
- _objc_msgSend$setOperationalKeyPair:
- _objc_msgSend$setOwnerSharedOperationalKeyPair:
- _objc_msgSend$setPreWarmTargetIsSystemCommissionerFabric:
- _objc_msgSend$setPreWarmedFabricID:
- _objc_msgSend$setResidentNodeID:
- _objc_msgSend$setStartSuspended:
- _objc_msgSend$setStorageData:forKey:
- _objc_msgSend$setUserOwnsConfiguredPreWarmTargetFabric:
- _objc_msgSend$setUserWithParams:completion:
- _objc_msgSend$setUserWithParams:expectedValues:expectedValueInterval:completionHandler:
- _objc_msgSend$setupStorageStateAfterCertFetchForHomeFabricID:completion:
- _objc_msgSend$setupStorageStateAndRediscoverAccessoriesForHomeFabricID:
- _objc_msgSend$setupStorageStateForHomeFabricID:
- _objc_msgSend$setupStorageStateForHomeFabricID:completion:
- _objc_msgSend$startAccessoryFirmwareUpdateWithExtendedMACAddress:fabricID:isWedDevice:completion:
- _objc_msgSend$startAccessoryPairingWithExtendedMACAddress:fabricID:isWedDevice:completion:
- _objc_msgSend$startSuspended
- _objc_msgSend$startThreadRadioForHomeWithFabricID:
- _objc_msgSend$startThreadRadioForHomeWithFabricID:preventDisconnect:
- _objc_msgSend$startThreadRadioForSystemCommissionerFabricID:
- _objc_msgSend$stopAccessoryFirmwareUpdateWithFabricID:completion:
- _objc_msgSend$stopAccessoryPairingWithFabricID:completion:
- _objc_msgSend$stopThreadRadioForHomeWithFabricID:
- _objc_msgSend$stopThreadRadioForSystemCommissionerFabricID:
- _objc_msgSend$storageDataForKey:
- _objc_msgSend$storageDataSourceForFabricWithID:
- _objc_msgSend$suspendOperationsForFabricID:
- _objc_msgSend$syncDataSourceDictionary:forFabric:
- _objc_msgSend$userOwnsConfiguredPreWarmTargetFabric
- logCategory._hmf_once_t1.1614
- logCategory._hmf_once_t1.4501
- logCategory._hmf_once_t10.6051
- logCategory._hmf_once_t11.2755
- logCategory._hmf_once_t12
- logCategory._hmf_once_t173
- logCategory._hmf_once_t2.4602
- logCategory._hmf_once_t2.5592
- logCategory._hmf_once_t2.5904
- logCategory._hmf_once_t2.8381
- logCategory._hmf_once_t206
- logCategory._hmf_once_t26.9934
- logCategory._hmf_once_t3.1083
- logCategory._hmf_once_t33
- logCategory._hmf_once_t38
- logCategory._hmf_once_t39
- logCategory._hmf_once_t4.5842
- logCategory._hmf_once_t4.6161
- logCategory._hmf_once_t400
- logCategory._hmf_once_t42
- logCategory._hmf_once_t44
- logCategory._hmf_once_t540
- logCategory._hmf_once_t6.1698
- logCategory._hmf_once_t64
- logCategory._hmf_once_t86
- logCategory._hmf_once_t9.5360
- logCategory._hmf_once_t90
- logCategory._hmf_once_t91
- logCategory._hmf_once_t98
- logCategory._hmf_once_v10.5362
- logCategory._hmf_once_v11.6053
- logCategory._hmf_once_v12.2757
- logCategory._hmf_once_v13
- logCategory._hmf_once_v174
- logCategory._hmf_once_v2.1616
- logCategory._hmf_once_v2.4503
- logCategory._hmf_once_v207
- logCategory._hmf_once_v27.9936
- logCategory._hmf_once_v3.4604
- logCategory._hmf_once_v3.5594
- logCategory._hmf_once_v3.5906
- logCategory._hmf_once_v3.8383
- logCategory._hmf_once_v34
- logCategory._hmf_once_v39
- logCategory._hmf_once_v4.1085
- logCategory._hmf_once_v40
- logCategory._hmf_once_v401
- logCategory._hmf_once_v43
- logCategory._hmf_once_v45
- logCategory._hmf_once_v5.5844
- logCategory._hmf_once_v5.6163
- logCategory._hmf_once_v541
- logCategory._hmf_once_v65
- logCategory._hmf_once_v7.1700
- logCategory._hmf_once_v87
- logCategory._hmf_once_v91
- logCategory._hmf_once_v92
- logCategory._hmf_once_v99
CStrings:
+ "%{public}@AbsMaxCoolSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@AbsMaxHeatSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@AbsMinCoolSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@AbsMinHeatSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@Accessory marked as subscribed"
+ "%{public}@Accessory marked for resubscription"
+ "%{public}@Accessory services dictionary: %@"
+ "%{public}@Accessory services: %@"
+ "%{public}@Added active client for pairing into fabric %@, currently active clients: %@"
+ "%{public}@Allowing thread stop for fabric %@"
+ "%{public}@An error occurred while getting all the device types for each endpoint of node %@. %@. DeviceTypes: %@"
+ "%{public}@An error occurred while getting all the endpoints for the aggregate node (bridge) endpoint of node %@: %@"
+ "%{public}@An error occurred while trying to read Measured Value attribute"
+ "%{public}@An error occurred while trying to read Measurement Unit attribute"
+ "%{public}@An error occurred while trying to read Measurement Unit attribute. Cannot handle Measured Value attribute."
+ "%{public}@An error occurred while trying to read Peak Measured Value attribute"
+ "%{public}@Attempting to resume active client fabric UUID: %@"
+ "%{public}@Attempting to resume secondary clients fabric UUIDs: %@"
+ "%{public}@Attribute node label absent from cache of node %@"
+ "%{public}@Attribute selector not found for cluster: %@"
+ "%{public}@AttributeList attribute for cluster class %@ on endpoint %@ absent from cache of node %@"
+ "%{public}@Attributes %@ for characteristic %@ not found in supported attribute list %@ for endpoint %@ of node %@"
+ "%{public}@Bad aggregator parts list: %@"
+ "%{public}@Bad root key"
+ "%{public}@Bad root parts list: %@"
+ "%{public}@Bridge node native services dictionary: %@"
+ "%{public}@Bridge node native topology: %@"
+ "%{public}@Bridge node services updated with native Matter functionalities: %@"
+ "%{public}@Bridge services dictionary: %@"
+ "%{public}@CHIP Stack is not running. Controller wrapper: %@"
+ "%{public}@Cached wrapper required for pairing prep was not found for %@"
+ "%{public}@Calling MTRDevice _deviceMayBeReachable"
+ "%{public}@Calling fetch Device Types completion block for node %@, error: %@, endpointDeviceTypes %@"
+ "%{public}@Cannot convert %@ measured value read from %@ measurement unit to PPM."
+ "%{public}@Cannot convert %@ measured value read from %@ measurement unit to UGM3."
+ "%{public}@Cannot generate new fabric data reusing previous keys - Trying with a new set of keys"
+ "%{public}@Cannot issue NOC because commissionee node ID was not set"
+ "%{public}@Cannot obtain device controller after wrapper is removed"
+ "%{public}@Characteristic: (%@), selector: %@, endpoint: %@, numberOfArguments = %@"
+ "%{public}@Clearing fabric data for target fabric UUID %@"
+ "%{public}@Cluster ID %@ not found at any endpoints of node %@"
+ "%{public}@Cluster class name not found for mandatory characteristic %@ in use at endpoint %@ of node %@"
+ "%{public}@Cluster class name not found for optional characteristic %@ in use at endpoint %@ of node %@"
+ "%{public}@Cluster classes to query for attributes of node %@: %@"
+ "%{public}@Cluster classes to query for feature map of node %@: %@"
+ "%{public}@ColorTempPhysicalMaxMireds attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@ColorTempPhysicalMinMireds attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@Comparing device feature map %u with characteristic %@ required feature map %u of node %@"
+ "%{public}@Computed service label index map for non-bridged accessory %@ of node %@: %@"
+ "%{public}@Connection has become idle but there are still active clients, keeping matter stack active for fabric %@. Fabrics with active clients: %@, secondary clients: %@"
+ "%{public}@Connection has become idle, but FW update is active, keeping matter stack active for fabric %@. Fabrics with active clients: %@, secondary clients: %@"
+ "%{public}@Connection has become idle, shutting down matter stack for fabric %@. Fabrics with active clients: %@"
+ "%{public}@Constructed HAP service description for HAP Characteristic %@, CHIP clusterID %@, endpoint %@ of node %@"
+ "%{public}@Constructed HAP service description for optional HAP Characteristic %@, CHIP clusterID %@, endpoint %@ of node %@"
+ "%{public}@Constructed bridge accessory %@"
+ "%{public}@Constructed new service to add %@ at endpoint %@ of node %@"
+ "%{public}@Could not construct any of the services of node %@"
+ "%{public}@Could not fetch current pairing because of no device"
+ "%{public}@Could not fetch pairings because of no device"
+ "%{public}@Could not fetch serial number because of no device"
+ "%{public}@Could not remove pairing %@ because of no device"
+ "%{public}@Could not retrieve hap category because of no device"
+ "%{public}@Could not update fabric label to %@ because of no device"
+ "%{public}@Current Matter stack is running for fabric %@ and therefore request to handle pairing on fabric %@ cannot be processed"
+ "%{public}@Current target fabric changed from %@/%@ to %@/%@"
+ "%{public}@Device Type Enumeration : Got at endpoint %@ of node %@, following device types in use %@"
+ "%{public}@Device Type Enumeration Endpoint: %@ of node %@ Failed to get the device types %@. Not fatal, continuing with enumeration..."
+ "%{public}@Device Type Enumeration Endpoint: %@ of node %@. The List of device types %@"
+ "%{public}@Device Type Enumeration for node %@. The List of device types @%@"
+ "%{public}@Device controller is not set up yet to fake discover node ID %@"
+ "%{public}@DeviceList is incomplete, proceeding anyway. Only partial enumeration is possible for node %@"
+ "%{public}@Disable controller factory operation ignored"
+ "%{public}@Dropping existing service %@ of node %@ to replace"
+ "%{public}@Dropping notification as the fabricID does not match that of the active network, activeNetworkFabricUUID: %@, fabricUUID: %@"
+ "%{public}@Endpoints In Use for the bridge of node %@: %@. Error: %@"
+ "%{public}@Error: Cannot get signature for %@ from %@ cluster"
+ "%{public}@Error: Failed to read attribute from cluster class %@ on endpoint %@"
+ "%{public}@Error: Failed to read attribute value from cluster class %@ on endpoint %@"
+ "%{public}@Error: nil read for Measurement Unit attribute"
+ "%{public}@Error: nil read for Measurement Unit attribute. Cannot handle Measured Value attribute."
+ "%{public}@Error: nil read for Measurement Unit attribute. Cannot handle Peak Measured Value attribute."
+ "%{public}@Error: nil read for Measurement Value attribute, returning 0"
+ "%{public}@Error: nil read for Peak Measurement Value attribute"
+ "%{public}@Error: nil recieved for Measured Value attribute, returning 0."
+ "%{public}@Evicting fabric: %@"
+ "%{public}@Examining MTRClusterDescriptor cluster parts list at endpoint %@ of node %@ to retrieve endpoints in use."
+ "%{public}@Examining MTRClusterDescriptor device list at endpoint %@ of node %@"
+ "%{public}@FATAL Error: Failed to generate IPK for fabric %@"
+ "%{public}@Fabric %@ has become idle, but current fabric is %@, not stopping current matter stack. fabrics with active clients:%@"
+ "%{public}@Fabric data source not available; failed to get ipk for fabric %@"
+ "%{public}@Fabric data source not available; failed to get legacy node ID for fabric %@"
+ "%{public}@Fabric key pairs or root cert are missing. Declining to fetch certificates."
+ "%{public}@Failed to derive fabric data from combined data item: %@"
+ "%{public}@Failed to fetch clusters in use at endpoint %@ of node %@"
+ "%{public}@Failed to find HAP characteristic ID for characteristic %@ on endpoint %@ of node %@, aborting"
+ "%{public}@Failed to find HAP to CHIP cluster mapping for characteristic %@ on endpoint %@ of node %@, aborting"
+ "%{public}@Failed to generate new fabric data"
+ "%{public}@Failed to get HAP Services at Endpoint:%@ of node %@. Error:%@. Error is not fatal, continuing with enumeration"
+ "%{public}@Failed to get HAP Services from plist for endpoint:%@ of node %@. Error:%@"
+ "%{public}@Failed to get device attribute list for cluster class name %@ at endpoint %@ of node %@. Error: %@"
+ "%{public}@Failed to get device feature map value for characteristic %@ with cluster class name %@ at endpoint %@ of node %@"
+ "%{public}@Failed to get device feature map value for cluster class name %@ at endpoint %@ of node %@. Ignoring feature map errors"
+ "%{public}@Failed to get device for unpairing. The device will not be notified of removal"
+ "%{public}@Failed to get endpoints for node %@: %@"
+ "%{public}@Failed to read aggregator %@ parts list"
+ "%{public}@Failed to read root parts list"
+ "%{public}@Failed to register a handler for keybagd.lock_status notification with status: %u"
+ "%{public}@Failed to register a handler for loginwindow.logoutNoReturn notification with status: %u"
+ "%{public}@Failed to remove V0 key %@"
+ "%{public}@Failed to replace current NOC signer key in storage"
+ "%{public}@Failed to replace current operational key in storage"
+ "%{public}@Failed to retrieve operational certificate from remote delegate: %@"
+ "%{public}@Failed to start matter stack for target fabric UUID: %@"
+ "%{public}@Failed to store NOC signer"
+ "%{public}@Failed to store Shared Operational Key"
+ "%{public}@Failed to store fabric data into combined data store"
+ "%{public}@Failed to store fabric keys to common key store - it is expected in some cases. Not updating CHIP storage"
+ "%{public}@Failed to store fabric parameters to CHIP storage"
+ "%{public}@Failed to store operational Key"
+ "%{public}@Failed to update V0 key: %@"
+ "%{public}@Feature map information not available for mandatory characteristic %@ on endpoint %@ of node %@"
+ "%{public}@Feature map information not available for optional characteristic %@ on endpoint %@ of node %@"
+ "%{public}@Feature map not in cache for cluster class %@ of node %@"
+ "%{public}@Feature map selector not found for cluster: %@ of node %@"
+ "%{public}@Fetching server list from descriptor cluster at endpoint %@, bridgeAggregateNodeEndpoint %@, isComposedDevice %d of node %@"
+ "%{public}@Finding endpoint for clusterID %@ from node %@"
+ "%{public}@Force updating V0 keys"
+ "%{public}@Found required feature map %@ for mandatory characteristic %@ on endpoint %@ of node %@"
+ "%{public}@Found required feature map %@ for optional characteristic %@ on endpoint %@ of node %@"
+ "%{public}@Generating new IPK for fabric %@"
+ "%{public}@HAP characteristics support verification for node %@ failed with error : %@"
+ "%{public}@HMMTRSyncClusterDoorLock initWithDevice called with device: %@ and endpoint: %@"
+ "%{public}@Handling pairing completion for Accessory with Node ID %@, Fabric ID %@, Vendor ID %@, Product ID %@, Config Number %@, Category %@, fabric UUID %@"
+ "%{public}@Handling remove from browser"
+ "%{public}@Hitting maximum number of wrappers. Removing unused and restarting factory. Currently used: %@"
+ "%{public}@IPK generation failed"
+ "%{public}@IPK missing for fabric %@"
+ "%{public}@Identify on aggregator %@ failed"
+ "%{public}@Identify on aggregator %@ successful"
+ "%{public}@Identify on endpoint %@ for bridge failed"
+ "%{public}@Identify on endpoint %@ for bridge successful"
+ "%{public}@Ignoring thread start for fabric %@, network is locked to fabric %@"
+ "%{public}@Ignoring wake, device is still locked"
+ "%{public}@In-memory fabric ID %@ is used while KVS hasn't stored fabric ID yet"
+ "%{public}@Installed NOC signer key into storage"
+ "%{public}@Installed operational key into storage"
+ "%{public}@Invalid fabric UUID, ignoring thread radio stop"
+ "%{public}@Invalid fabricUUID, ignoring thread radio start"
+ "%{public}@Invalid target fabric UUID, ignoring thread radio start"
+ "%{public}@Keybag Lock state changed: %@"
+ "%{public}@Looking for optional HAP Characteristic %@ as its matching CHIP clusterID %@ on endpoint %@ of node %@"
+ "%{public}@Looking for required HAP Characteristic %@ as its matching CHIP clusterID %@ on endpoint %@ of node %@"
+ "%{public}@MTRDevice is ready to read from. Triggering pending MTRDevice read-ready handlers"
+ "%{public}@Making room for target fabric UUID: %@"
+ "%{public}@Mandatory characteristic %@ cannot be found in clusters in use at endpoint %@ of node %@"
+ "%{public}@MaxCoolSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@MaxHeatSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@MinCoolSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@MinHeatSetpointLimit attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@NOC issuer was initialized incorrectly"
+ "%{public}@NOC signer already exists - failed to store new NOC signer"
+ "%{public}@Native Matter functionalities shall be ignored for fetching HAP services for bridge native Matter functionalities failed for node %@ with error %@"
+ "%{public}@No Endpoints In Use at endpoint 0 of node %@: %@"
+ "%{public}@No IPK"
+ "%{public}@No clusters in use at endpoint %@ of node %@"
+ "%{public}@No endpoint found to identify bridge"
+ "%{public}@No endpoints of node %@ contain clusters, not storing topology. Enumeration will re-run next time."
+ "%{public}@No fabric ID"
+ "%{public}@No fabric root key pair"
+ "%{public}@No legacy resident node ID retrieved from stored operational cert"
+ "%{public}@No operational cert"
+ "%{public}@No operational key pair"
+ "%{public}@No resident reachable for target fabric UUID %@ and there are active clients, start local stack"
+ "%{public}@No root cert"
+ "%{public}@Not reading because fabricID is not yet defined for target fabric %@"
+ "%{public}@Not shutting down stack for fabric %@ because there is an active client"
+ "%{public}@Not shutting down stack for fabric %@ because there is an active connection"
+ "%{public}@Not shutting down stack for fabric %@ because there is an active secondary client"
+ "%{public}@Not starting local discovery for target fabric UUID %@, resident available"
+ "%{public}@Operational fabric data was set successfully for %@"
+ "%{public}@Operational fabric data wasn't set for %@"
+ "%{public}@Operational key doesn't match operational cert"
+ "%{public}@Optional characteristic %@ cannot be found in clusters in use at endpoint %@ of node %@"
+ "%{public}@Optional characteristic %@ on endpoint %@ of node %@ requires an additional Optional Matter attribute check"
+ "%{public}@Order attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@Overriding linkLayerType unknown -> thread for nodeID %@"
+ "%{public}@Parts list of endpoint %@ of node %@ absent from cache"
+ "%{public}@Power state state changed - state = %lu, goingToSleep: %@"
+ "%{public}@Pre-warming device controller factory"
+ "%{public}@Prepare pairing with setup payload: %@, targetfabricUUID: %@"
+ "%{public}@Preventing thread stop for fabric %@ because preventDisconnect is true and locked to fabric %@"
+ "%{public}@Preventing thread stop for system commissioner fabricID %@ because preventDisconnect is true and locked to fabric %@"
+ "%{public}@Querying device cluster %@ at endpoint %@ of node %@ for feature map value"
+ "%{public}@Querying device cluster %@ at endpoint %@ of node %@ for supported attributes"
+ "%{public}@Re-enabling fabric with active client: %@"
+ "%{public}@Re-enabling keep-alive for fabrics with secondary clients: %@"
+ "%{public}@Read Measurement Unit value = %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint (sync): Current System Mode was read with unexpected class type %@"
+ "%{public}@Received feature map from accessory for cluster class %@ of node %@. Value: %@"
+ "%{public}@Received supported attributes list from accessory for cluster class %@ on endpoint %@ of node %@. Attributes: %@"
+ "%{public}@Received supportedAttribute value from accessory for cluster class %@ on endpoint %@. Value: %@"
+ "%{public}@Received suspendOperations, but no active fw updates in progress for fabric %@"
+ "%{public}@Received thread radio state changed notification, connectionState: %ld, nodeType: %ld, fabric:%@, last known connectionState: %ld"
+ "%{public}@Redundant native bridge Matter functionalities shall be ignored for node %@"
+ "%{public}@Registered keybagd.lock_status notification handler"
+ "%{public}@Registered loginwindow.logoutNoReturn notification handler"
+ "%{public}@Registering %@ to receive attribute and event reports"
+ "%{public}@Remote storage is not yet available for fabric %@"
+ "%{public}@Removed unsupported characteristic %@ for endpoint %@ due to attribute value %@ not matching supported attribute mask %@."
+ "%{public}@Removed unsupported characteristic %@ for endpoint %@ of node %@"
+ "%{public}@Removing active clients fabricUUIDs: %@"
+ "%{public}@Removing fabrics with secondary clients fabricUUIDs: %@"
+ "%{public}@Removing from discovered accessory server list: %@ for reason: %@, context: %@"
+ "%{public}@Replaced NOC signer key in storage"
+ "%{public}@Replaced operational key in storage"
+ "%{public}@Resident Operational Cert generation failed: %@"
+ "%{public}@Resident reachability changed for non-current target fabric UUID %@, ignoring"
+ "%{public}@Retrieved at endpoint %@ of node %@, following HAP categories in use %@"
+ "%{public}@Retrieved at endpoint %@ of node %@, following clusters in use %@"
+ "%{public}@Retrieved controller %@ for fabric UUID %@ upon setting the startup parameters"
+ "%{public}@Retrieved service description @%@ at composed endpoint %@"
+ "%{public}@Retrieved the following endpoints of endpoint %@ of node %@ in use %@"
+ "%{public}@Root cert generation failed: %@"
+ "%{public}@Root key doesn't match root cert"
+ "%{public}@Running block on all endpoints of node %@ with clusterID %@"
+ "%{public}@Saving AbsMaxCoolSetpointLimit attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
+ "%{public}@Saving AbsMinCoolSetpointLimit attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
+ "%{public}@Saving AbsMinHeatSetpointLimit attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
+ "%{public}@Saving defaultAbsMaxHeatSetpointLimit attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
+ "%{public}@Server %@ already removed from discovered server list"
+ "%{public}@ServerList at endpoint %@ of node %@ absent from cache"
+ "%{public}@ServerList attribute at endpoint %@ of node %@ absent from cache"
+ "%{public}@Service label index enumerated to %@ for endpoint %@ of node %@"
+ "%{public}@Setting controller parameters for target fabric UUID %@ was deferred during pairing"
+ "%{public}@Setting deferred controller parameters after pairing is complete"
+ "%{public}@Setting root and operational cert in start up params %@ %@ for target fabric UUID %@ with UUID %@ using operational key %@"
+ "%{public}@Setting up controller wrapper for Target Fabric UUID = %@, currentFabricUUID = %@"
+ "%{public}@Setting up storage state for Target Fabric UUID = %@"
+ "%{public}@Shared operational key already exists - failed to store new shared operational key"
+ "%{public}@Shutting down stack for fabric %@ because there are no active clients"
+ "%{public}@Skipping calling _deviceMayBeReachable, no change in networking state since last successful subscription"
+ "%{public}@Sources attribute from the %@ cluster endpoint:%@ absent from cache of node %@"
+ "%{public}@Start thread for fabric %@, preventDisconnect = %@, last known connectionState: %ld"
+ "%{public}@Start thread for system commissioner fabric %@"
+ "%{public}@Started Matter controller '%@' with Node ID %@ on fabric ID %@, entity id %@"
+ "%{public}@Starting discovery for target fabric UUID %@ because there are active clients"
+ "%{public}@Starting discovery stack for target fabric UUID %@ because there are active clients"
+ "%{public}@Starting locally discovered accessory pairing for targetFabricUUID %@"
+ "%{public}@Starting pairing with %@, server fabricUUID %@"
+ "%{public}@Starting stack for target fabric UUID %@ because there are active clients and local stack is unconfigured"
+ "%{public}@Starting thread for target fabric UUID %@ because it became the current fabric"
+ "%{public}@State Capture: No Endpoints In Use at endpoint 0 of node %@"
+ "%{public}@Stop thread for fabric %@"
+ "%{public}@Stop thread for system commissioner fabric %@"
+ "%{public}@Stopping operation with system commissioner fabric"
+ "%{public}@Stopping the matter stack for target fabric UUID %@"
+ "%{public}@Stopping thread due to user logout"
+ "%{public}@Storage state cannot be setup without target fabric UUID"
+ "%{public}@Successfully stored new fabric data"
+ "%{public}@Successfully updated V0 key in storage"
+ "%{public}@Supported attributes selector not found for cluster: %@ of node %@"
+ "%{public}@System commissioner NOC: %@"
+ "%{public}@System commissioner root certificate: %@"
+ "%{public}@The accessory contains no valid HAP services in endpoint hierarchy"
+ "%{public}@Thread network connection state: %@ for fabric: %@, calling start pairing block now"
+ "%{public}@Thread network connection state: %@ for fabric: %@, calling start pairing block now. ActiveThreadNetworkFabricID: %@"
+ "%{public}@Thread network connection state: %@ for fabric: %@, deferring call to start pairing block. ActiveThreadNetworkFabricUUID: %@"
+ "%{public}@Thread network is already running for fabric %@. Not starting Thread."
+ "%{public}@Thread start already pending, ignoring startThread request for fabric %@"
+ "%{public}@Thread start called for new fabric %@, will be disconnecting from thread network for fabric %@"
+ "%{public}@Total endpoints In Use at endpoint 0 of node %@: %@. Error: %@"
+ "%{public}@Tracking fabric with secondary clients for resumption with fabricUUID: %@"
+ "%{public}@Tracking frabic with active clients for resumption for fabricUUID: %@"
+ "%{public}@Unable to get additional thread information from accessory after firmware update for nodeID %@ because of no device"
+ "%{public}@Unexpected state, fabricUUIDOfActiveThreadNetwork = %@, preventDisconnect = %@"
+ "%{public}@UpdateNotifications received for target fabric UUID:%@ enabled:%@ keepAliveOnly:%@. currentFabricUUID %@, browserState = %lu, fabricsWithActiveClients = %@, fabricWithActiveSecondaryClients = %@"
+ "%{public}@UpdateNotifications received nil target fabric UUID for fabric: %@. Ignoring request"
+ "%{public}@Updated OTA requestor endpoints of node %@ in topology"
+ "%{public}@Updating CATs (admin %@, user %@) for FabricID (browser's fabric %@, server's %@, storage's %@"
+ "%{public}@Updating V0 key in storage"
+ "%{public}@User logging out"
+ "%{public}@[Flow: %@] Adding issuerKey: %@ to userUniqueID: %@ toCredentialSlot: %ld"
+ "%{public}@[Flow: %@] Begin process to re-add AliroCredentialsToUser: %@"
+ "%{public}@[Flow: %@] Cached user has aliro credential index mapped as %ld."
+ "%{public}@[Flow: %@] Cached user indeed has aliro credential at %ld on the lock"
+ "%{public}@[Flow: %@] Cached user is stale on the lock: %@"
+ "%{public}@[Flow: %@] Cached user matches identifiers with the lock's current user on index %ld."
+ "%{public}@[Flow: %@] Clear abandoned user: %@ since it belongs to a deleted fabric"
+ "%{public}@[Flow: %@] Corresponding issuer key index: %ld in our cache was stale for userIndex: %ld."
+ "%{public}@[Flow: %@] Could not determine number of credentials supported per user, assuming %@ by default"
+ "%{public}@[Flow: %@] Could not determine total number of aliro device credentials supported, assuming 50 by default"
+ "%{public}@[Flow: %@] Could not determine total number of aliro issuer credentials supported, assuming 50 by default"
+ "%{public}@[Flow: %@] Could not find corresponding issuer key index in our cache for userIndex: %ld."
+ "%{public}@[Flow: %@] Could not find user at userIndex: %ld"
+ "%{public}@[Flow: %@] Could not find user with uniqueID: %@ in cache, need to perform full user search"
+ "%{public}@[Flow: %@] Could not find user with userUniqueID: %ld"
+ "%{public}@[Flow: %@] Creating door lock cluster object"
+ "%{public}@[Flow: %@] Credential slot resources have been exhausted"
+ "%{public}@[Flow: %@] Credentials per user limit reached, and no evictable endpoints to remove"
+ "%{public}@[Flow: %@] Did not find existing issuer key credential on user index: %ld"
+ "%{public}@[Flow: %@] Door lock became nil"
+ "%{public}@[Flow: %@] Error while reading number of aliro issuer key credentials supported: %@"
+ "%{public}@[Flow: %@] Existing guest with schedule already exists on the lock, just return the user response"
+ "%{public}@[Flow: %@] Existing issuer key credential index: %ld"
+ "%{public}@[Flow: %@] Existing issuer key: %@, does not match requested issuer key: %@"
+ "%{public}@[Flow: %@] Failed to derive home PIN"
+ "%{public}@[Flow: %@] Failed to read BLE advertising version with error: %@"
+ "%{public}@[Flow: %@] Failed to read aliro BLE protocol versions with error: %@"
+ "%{public}@[Flow: %@] Failed to read aliro expedited transaction supported protocol versions with error: %@"
+ "%{public}@[Flow: %@] Failed to read max pin code length constraint from accessory"
+ "%{public}@[Flow: %@] Failed to read min pin code length constraint from accessory"
+ "%{public}@[Flow: %@] Failed to update credential with error: %@"
+ "%{public}@[Flow: %@] Failed to update credential with status: %@"
+ "%{public}@[Flow: %@] Failure to remove all abandonded users with error: %@"
+ "%{public}@[Flow: %@] Found cached user: %@"
+ "%{public}@[Flow: %@] Found evictable endpoint at credential index: %ld"
+ "%{public}@[Flow: %@] Found user on index verify userUniqueID %@"
+ "%{public}@[Flow: %@] Issuer key matches: %@, no updates required"
+ "%{public}@[Flow: %@] No matter device available"
+ "%{public}@[Flow: %@] Successfully removed %lu abandoned users"
+ "%{public}@[Flow: %@] Unexpected that userUniqueID and issuerKey arrays are not the same length"
+ "%{public}@[Flow: %@] _addIssuerKeyData: %@, credentialType: %@, forUserIndex: %ld"
+ "%{public}@[Flow: %@] _addOrUpdateIssuerKeyData: %@ forUser: %@"
+ "%{public}@[Flow: %@] _addOrUpdateIssuerKeyData: %@ forUserIndex: %ld"
+ "%{public}@[Flow: %@] _addOrUpdateIssuerKeyData: %@ forUserUniqueID: %ld"
+ "%{public}@[Flow: %@] addCredentialData: %@ forCredentialType: %@, atIndex: %ld forUserAtUserIndex: %@"
+ "%{public}@[Flow: %@] addNewUsersWithUserUniqueIDs: userUniqueIDs: %@ withCorrespondingIssuerKeys: %@"
+ "%{public}@[Flow: %@] addOrUpdateIssuerKeyData: %@ forUserIndex: %ld"
+ "%{public}@[Flow: %@] addOrUpdateIssuerKeyData: %@ forUserUniqueID: %ld"
+ "%{public}@[Flow: %@] clearAllUsersWithDeletedCreatorFabricIndexWithFlow"
+ "%{public}@[Flow: %@] issuerCredentialForUser: %@"
+ "%{public}@[Flow: %@] updateUserUniqueIDForUserIndex: %ld, userUniqueID: %@"
+ "%{public}@[Flow: %@] userIndex is nil when trying to add credential to new user. Possible firmware issue."
+ "%{public}@[NewFlow: %@] getMaxPINCodeLength"
+ "%{public}@[NewFlow: %@] getMinPINCodeLength"
+ "%{public}@_connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
+ "%{public}@_handleThreadRadioStateChanged - requiresThreadRouter = %@ (isWED = %@, isControllerInSleepyRouterState = %@)"
+ "%{public}@_handleThreadRadioStateChanged - thread went offline - marking accessory for resubscription"
+ "%{public}@abortAllOperations for fabric: %@"
+ "%{public}@configureDefaultRequiresThreadRouter - accessory requires thread router = %@ (isAccessoryServerThreadCapable = %@, isDeviceThreadCapable = %@, isWEDDevice = %@"
+ "%{public}@deviceActivityState change - goOffline=%@, reason=%ld, current active fabric %@"
+ "%{public}@discoverAccessoryServerWithNodeId %@"
+ "%{public}@fabricUUID %@ didn't retrieve any fabric parameter"
+ "%{public}@fabricUUID %@ retrieved fabricID %@ while pairingRequest had fabricID %@"
+ "%{public}@fabricUUID was not set before starting pairing"
+ "%{public}@fetchClientClustersForDevice of endpoint %@ of node %@: Retrieved the following client clusters %@"
+ "%{public}@fetchClientClustersForDevice: Examining MTRBaseClusterDescriptor clientlist attribute at endpoint %@ of node %@ to retrieve client clusters."
+ "%{public}@fetchClusterAcceptedCommandsForDevice: Examining MTRBaseClusterDescriptor cluster acceptedCommandList attribute at endpoint %@ of node %@ to retrieve accepted commands."
+ "%{public}@fetchClusterAcceptedCommandsForDevice: For endpoint %@ of node %@, cluster %@, retrieved the following accepted command list %@"
+ "%{public}@fetchClusterAttributesForDevice: Examining MTRBaseClusterDescriptor attributelist attribute at endpoint %@ of node %@ to retrieve cluster attributes."
+ "%{public}@fetchClusterAttributesForDevice: For endpoint %@ of node %@, cluster %@, retrieved the following attributes %@"
+ "%{public}@fetchClusterEventListForDevice: Examining MTRBaseClusterDescriptor eventlist attribute at endpoint %@ of node %@ to retrieve events."
+ "%{public}@fetchClusterEventListForDevice: For endpoint %@ of node %@, cluster %@, retrieved the following events %@"
+ "%{public}@fetchClusterFeatureMapForDevice: Examining MTRBaseClusterDescriptor cluster feature map attribute at endpoint %@ of node %@ to retrieve feature map."
+ "%{public}@fetchClusterFeatureMapForDevice: For endpoint %@ of node %@, cluster %@, retrieved the following feature map %@"
+ "%{public}@fetchClusterGeneratedCommandsForDevice: Examining MTRBaseClusterDescriptor cluster generated command list attribute at endpoint %@ of node %@ to retrieve accepted commands."
+ "%{public}@fetchClusterGeneratedCommandsForDevice: For endpoint %@ of node %@, cluster %@, retrieved the following generated command list %@"
+ "%{public}@fetchClusterRevisionForDevice: Examining MTRBaseClusterDescriptor cluster revision attribute at endpoint %@ of node %@ to cluster revision number."
+ "%{public}@fetchClusterRevisionForDevice: For endpoint %@ of node %@, cluster %@, retrieved the revison number %@"
+ "%{public}@fetchDeviceTypesWithMTRDevice: At endpoint %@ of node %@, retrieved the following device types in use %@"
+ "%{public}@fetchDeviceTypesWithMTRDevice: Examining MTRClusterDescriptor cluster parts list at endpoint %@ of node %@ to retrieve device types."
+ "%{public}@fetchPartsListForDevice for endpoint %@ of node %@: Failed to read parts list."
+ "%{public}@fetchPartsListForDevice for endpoint %@ of node %@: Retrieved the following parts list in use %@"
+ "%{public}@fetchPartsListForDevice: Examining MTRClusterDescriptor cluster parts list at endpoint %@ of node %@ to retrieve endpoints in use."
+ "%{public}@fetchServerClustersForDevice for endpoint %@ of node %@: Retrieved the following server clusters %@"
+ "%{public}@fetchServerClustersForDevice: Examining MTRBaseClusterDescriptor serverlist attribute at endpoint %@ of node %@ to retrieve server clusters."
+ "%{public}@handleThreadDirectConnectionSleepyTypeChange - requiresThreadRouter = %@ for accessory with nodeID %@ (isWED = %@, isSleepyLink = %@)"
+ "%{public}@isReadyToEstablishWEDConnection - Thread is not active"
+ "%{public}@isReadyToTransitionToFullRouterModeForFirmwareUpdate - Thread is not active"
+ "%{public}@isThreadNetworkConnected - Thread is not active"
+ "%{public}@no target fabric UUID was provided, restarting with fabric with active client: %@"
+ "%{public}@stopping thread even though preventDisconnect is true due to logout"
+ "%{public}@updateAllConnectionIdleTimeoutsToMinimum for fabric: %@"
+ "00000069-0000-1000-8000-0026BB765291"
+ "00000076-0000-1000-8000-0026BB765291"
+ "?3"
+ "@\"<HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate>\""
+ "@\"<HMMTRMultiFabricDataStoreQueryKeychainDelegate>\""
+ "@\"<HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate>\""
+ "@\"<HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate>\""
+ "@\"<HMMTRMultiFabricDataStoreUpdateKeychainDelegate>\""
+ "@\"<HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate>\""
+ "@\"<HMMTROperationalCertificateIssuerRemoteDelegate>\""
+ "@\"<HMMTRReportObserver>\""
+ "@\"HMMTRFabricDataSnapshot\""
+ "@\"MTRClusterDoorLock\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSHashTable\""
+ "@\"NSSet\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "@32@0:8^B16^@24"
+ "@44@0:8@16S24@28@36"
+ "@44@0:8q16B24@28@36"
+ "@48@0:8@16q24@32@40"
+ "@52@0:8@16@24@32B40@44"
+ "@56@0:8@16@24q32@40@48"
+ "@72@0:8@16q24q32@40@48@56@64"
+ "B16@?0@\"HAPService\"8"
+ "B16@?0@\"HMMTRAccessoryServer\"8"
+ "B24@0:8@\"HMMTRFabricDataSnapshot\"16"
+ "B24@0:8@\"NSDictionary\"16"
+ "B32@0:8@\"HMMTRMatterKeypair\"16@\"HMMTRMatterKeypair\"24"
+ "B32@?0@\"HMMTRControllerWrapperRevokeHandlerInfo\"8Q16^B24"
+ "B32@?0@\"MTRDoorLockClusterCredentialStruct\"8Q16^B24"
+ "FabricUUID"
+ "HMMCredentialKey"
+ "HMMTRAliroVersion"
+ "HMMTRFabricDataCreator"
+ "HMMTRFabricRandomV0KeyStore"
+ "HMMTRFabricV0KeyStore"
+ "HMMTRFabricVoidV0DataStore"
+ "HMMTRMultiFabricDataStoreQuery"
+ "HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate"
+ "HMMTRMultiFabricDataStoreQueryEmptyV2FabricDataStore"
+ "HMMTRMultiFabricDataStoreQueryKeychainDelegate"
+ "HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate"
+ "HMMTRMultiFabricDataStoreUpdate"
+ "HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate"
+ "HMMTRMultiFabricDataStoreUpdateKeychainDelegate"
+ "HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate"
+ "HMMTRMultiFabricDataStoreUpdateVoidV2FabricDataStore"
+ "HMMTROperationalFabricData"
+ "HMMTRSyncClusterCarbonDioxideConcentrationMeasurement"
+ "HMMTRSyncClusterCarbonMonoxideConcentrationMeasurement"
+ "HMMTRSyncClusterNitrogenDioxideConcentrationMeasurement"
+ "HMMTRSyncClusterOzoneConcentrationMeasurement"
+ "HMMTRSyncClusterPM10ConcentrationMeasurement"
+ "HMMTRSyncClusterPM25ConcentrationMeasurement"
+ "HMMTRSyncClusterTotalVolatileOrganicCompoundsConcentrationMeasurement"
+ "HMMTRUserFabricKeyUpdatedNotification"
+ "MatteriPhoneOnlyPairingForiPad"
+ "NativeMatterDeviceTypes"
+ "ObjID"
+ "Op Cert"
+ "Op Key Pair"
+ "Op Node ID"
+ "RequiredAttributes"
+ "Root Cert"
+ "SupportedAttributeBitmap"
+ "SystemCommissioner"
+ "T@\"<HMMTRDeviceControllerStorageDataSource>\",R,N,V_privateDataSource"
+ "T@\"<HMMTRMultiFabricDataStoreQueryCHIPStorageDelegate>\",W,N,V_chipStorageDelegate"
+ "T@\"<HMMTRMultiFabricDataStoreQueryKeychainDelegate>\",W,N,V_keychainDelegate"
+ "T@\"<HMMTRMultiFabricDataStoreQueryV2FabricDataStoreDelegate>\",W,N,V_v2FabricDataStoreDelegate"
+ "T@\"<HMMTRMultiFabricDataStoreUpdateCHIPStorageDelegate>\",R,W,N,V_chipStorageDelegate"
+ "T@\"<HMMTRMultiFabricDataStoreUpdateKeychainDelegate>\",R,W,N,V_keychainDelegate"
+ "T@\"<HMMTRMultiFabricDataStoreUpdateV2FabricDataStoreDelegate>\",R,W,N,V_v2FabricDataStoreDelegate"
+ "T@\"<HMMTROperationalCertificateIssuerRemoteDelegate>\",R,V_remoteDelegate"
+ "T@\"<HMMTRReportObserver>\",W,N,V_hmdHAPAccessoryDelegate"
+ "T@\"HMMTRAccessoryServer\",&,D,N"
+ "T@\"HMMTRFabricDataSnapshot\",R,N,V_fabricData"
+ "T@\"HMMTRMatterKeypair\",R,N,V_nocSigner"
+ "T@\"HMMTRMatterKeypair\",R,N,V_operationalKeyPair"
+ "T@\"HMMTRMatterKeypair\",R,N,V_ownerSharedOperationalKeyPair"
+ "T@\"HMMTRMatterKeypair\",R,N,V_residentOperationalKeyPair"
+ "T@\"HMMTRMatterKeypair\",R,V_rootKeyPair"
+ "T@\"MTRClusterDoorLock\",R,W,V_doorLock"
+ "T@\"NSArray\",&,V_bleUWBSupportedVersions"
+ "T@\"NSArray\",&,V_expeditedTransactionSupportedVersions"
+ "T@\"NSArray\",C,D,N"
+ "T@\"NSArray\",C,N"
+ "T@\"NSCache\",&,V_userUniqueIdentifierToUser"
+ "T@\"NSData\",C,N,V_rootPublicKey"
+ "T@\"NSData\",R,N,V_operationalCert"
+ "T@\"NSData\",R,N,V_residentOperationalCert"
+ "T@\"NSDictionary\",&,N,V_endpointToDeviceTypesMap"
+ "T@\"NSDictionary\",R,C,N"
+ "T@\"NSHashTable\",R,C,N,V_reportObservers"
+ "T@\"NSNumber\",&,N,V_credentialIndex"
+ "T@\"NSNumber\",&,N,V_credentialType"
+ "T@\"NSNumber\",&,V_bleAdvertisingVersion"
+ "T@\"NSNumber\",R,C,N"
+ "T@\"NSNumber\",R,N,V_operationalNodeID"
+ "T@\"NSSet\",R,N,V_nativeMatterDeviceTypes"
+ "T@\"NSUUID\",&,N,V_currentFabricUUID"
+ "T@\"NSUUID\",&,N,V_fabricUUIDOfActiveThreadNetwork"
+ "T@\"NSUUID\",&,N,V_fabricUUIDOfPendingStartPairingBlock"
+ "T@\"NSUUID\",&,V_fabricUUID"
+ "T@\"NSUUID\",R,D"
+ "T@\"NSUUID\",R,N,V_fabricUUID"
+ "T@\"NSUUID\",R,V_systemCommissionerFabricUUID"
+ "TB,N,V_didSendRevokeAvailableOnResume"
+ "TB,N,V_shouldReestablishSubscription"
+ "TB,R,GisInvalid,V_invalid"
+ "TB,V_lockStateKBNotificationRegistered"
+ "TB,V_logoutNotificationRegistered"
+ "Ti,V_lockStateKBNotificationRegistrationToken"
+ "Ti,V_logoutNotificationRegistrationToken"
+ "VoidV0DataStore"
+ "__getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:"
+ "_abortAllOperationsForFabricUUID:reason:"
+ "_addIssuerKeyData:forUserIndex:credentialType:flow:"
+ "_addOrUpdateIssuerKeyData:forUser:flow:"
+ "_addOrUpdateIssuerKeyData:forUserIndex:flow:"
+ "_addOrUpdateIssuerKeyData:forUserUniqueID:flow:"
+ "_bleAdvertisingVersion"
+ "_bleUWBSupportedVersions"
+ "_commissioneeAccessoryServerLock"
+ "_connectPendingFabricConnectionsForTargetFabricUUID:"
+ "_controllerSetUpBlockToRunAfterCommissioning"
+ "_credentialIndex"
+ "_credentialType"
+ "_currentFabricUUID"
+ "_deviceHasActiveSubscription"
+ "_deviceInternalStateChanged:"
+ "_deviceMayBeReachable"
+ "_didSendRevokeAvailableOnResume"
+ "_disableNormalOperation:"
+ "_doorLock"
+ "_endpointToDeviceTypesMap"
+ "_expeditedTransactionSupportedVersions"
+ "_fabricDataPerPairingTargetFabricUUID"
+ "_fabricUUID"
+ "_fabricUUIDOfActiveThreadNetwork"
+ "_fabricUUIDOfPendingStartPairingBlock"
+ "_getThreadHardwareAddressFromReadValue:"
+ "_getUserAtIndex:flow:"
+ "_handleClientsRemovedWithFabricUUID:updateConnectionIdleTimeout:reason:"
+ "_handleDeviceActivityStateChange:reason:"
+ "_handleEventReport:"
+ "_handleKeybagLockStateNotification"
+ "_handleLogoutNotification"
+ "_isDeviceIDPaired:nodeID:targetFabricUUID:"
+ "_isNodeIDPaired:targetFabricUUID:"
+ "_legacyHMDHAPAccessoryDelegateShouldHandleEvent:"
+ "_lockStateKBNotificationRegistered"
+ "_lockStateKBNotificationRegistrationToken"
+ "_logoutNotificationRegistered"
+ "_logoutNotificationRegistrationToken"
+ "_nativeMatterDeviceTypes"
+ "_nodSigner"
+ "_notifyThreadRadioStateChanged:nodeType:fabricUUID:"
+ "_operationalNodeID"
+ "_pairingTargetFabricDataLock"
+ "_prepareForPairingWithSetupPayload:targetFabricUUID:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:"
+ "_queryAttributeValueFromClusterAtCHIPEndpoint:device:attributeValuesToCheckDict:attributeValuesSupportedDict:attributeValuesRetrievedDict:callbackQueue:clusterClassName:completionHandler:"
+ "_readReaderConfigWithFlow:"
+ "_remoteDelegate"
+ "_removeOrSuspendAllActiveClientsWithCurrentFabricUUID:reason:"
+ "_reportObservers"
+ "_residentOperationalCert"
+ "_residentOperationalKeyPair"
+ "_resumeSuspendedActiveClients"
+ "_setupStorageStateForHomeFabricUUID:"
+ "_setupStorageStateForUpdatedHomeFabricUUID:"
+ "_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:"
+ "_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:"
+ "_setupStorageStateIfNotFabricUUID:rediscoverAccessories:"
+ "_shouldReestablishSubscription"
+ "_startThreadRadioForSystemCommissionerFabricUUID:"
+ "_startThreadRadioForTargetFabricUUID:preventDisconnect:"
+ "_stopSystemCommissionerFabricWithReason:"
+ "_stopThreadRadioForSystemCommissionerFabricUUID:"
+ "_stopThreadRadioForTargetFabricUUID:"
+ "_suspendOperationsForTargetFabricUUID:"
+ "_suspendedActiveClientFabricUUID"
+ "_suspendedActiveSecondaryClientFabricUUIDs"
+ "_systemCommissionerFabricUUID"
+ "_updateFabricUUIDOfActiveThreadNetwork:isFabricUUIDOfSystemCommissioner:"
+ "_userUniqueIdentifierToUser"
+ "_v2FabricDataStoreDelegate"
+ "_verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint:device:callbackQueue:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:attributeValuesSupportedDict:attributeValuesRetrievedDict:deviceTopology:server:lastError:completionHandler:"
+ "addFabricWithActiveClientForTargetFabricUUID:"
+ "addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:"
+ "addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:"
+ "addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:"
+ "addOrUpdateIssuerKeyData:forUserIndex:flow:"
+ "addOrUpdateIssuerKeyData:forUserUniqueID:flow:"
+ "addReportObserver:"
+ "addSuspendedActiveSecondaryClientFabricUUIDs:"
+ "aliroClearCredentialParamsFromParams:flow:"
+ "aliroCredentials"
+ "appendAliroCredentialsToUser:aliroCredentials:"
+ "appleClearAliroCredentialWithParams:expectedValues:expectedValueInterval:completion:"
+ "appleGetAliroCredentialStatusWithParams:expectedValues:expectedValueInterval:completion:"
+ "appleHomeFabricWithTargetFabricUUID:"
+ "appleSetAliroCredentialWithParams:expectedValues:expectedValueInterval:completion:"
+ "appleSetAliroReaderConfigWithParams:expectedValues:expectedValueInterval:completion:"
+ "arrayOfDataFromRead:"
+ "attributeValue"
+ "bleAdvertisingVersion"
+ "bleUWBSupportedVersions"
+ "bridgeIdentifyEndpointWithAggregatorEndpoint:"
+ "cacheUserResponse:"
+ "cachedWrapperWithTargetFabricUUID:"
+ "cancel"
+ "certificate:isCompatibleWithAnotherControllerCertificate:"
+ "chipStorageContentFromFabricData:"
+ "clearAllUsersWithDeletedCreatorFabricIndexWithFlow:"
+ "clearCredentialWithParams:expectedValues:expectedValueInterval:completion:"
+ "clearCredentialWithParams:flow:completion:"
+ "clearOperationalFabricDataForTargetFabricUUID:"
+ "clearSuspendedActiveSecondaryClientFabricUUIDs"
+ "com.apple.loginwindow.logoutNoReturn"
+ "com.apple.mobile.keybagd.lock_status"
+ "combineAllFutures:"
+ "commit"
+ "configureDefaultRequiresThreadRouter"
+ "connectToAccessoryWithExtendedMACAddress:withFabricUUID:completion:"
+ "controller:readCommissioneeInfo:"
+ "copyPublicKey"
+ "creationTime"
+ "credentialStruct"
+ "currentFabricUUID"
+ "deleteKeychainItem:error:"
+ "deregisterRevokeHandlersWithQueue:"
+ "descriptionsDictionaryFromAccessoryInfo:"
+ "devicesChangedForController:"
+ "didSendRevokeAvailableOnResume"
+ "disableFeatureMatterRVCForTests"
+ "doorLock"
+ "enableFeatureMatterRVCForTests"
+ "endpointToDeviceTypesMap"
+ "expeditedTransactionSupportedVersions"
+ "fabricDataForPairingTargetFabricUUID:"
+ "fabricDataForRootKeyPair:opKeyPair:fabricID:residentNodeID:overridingRCAC:ipk:"
+ "fabricDataFromV2FabricDataItem:"
+ "fabricDataItems"
+ "fabricIDFromFabricUUID:"
+ "fabricUUID"
+ "fabricUUIDOfActiveThreadNetwork"
+ "fabricUUIDOfPendingStartPairingBlock"
+ "fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricData:adminCAT:opCAT:completionHandler:"
+ "findAllOccupiedCredentialSlotsForCredentialType:startingAtSlot:assumingTotalNumberOfSlots:occupiedSlots:flow:"
+ "findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:"
+ "findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:"
+ "findOrAddUserWithUniqueID:withFlow:"
+ "findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:"
+ "finishWithError:"
+ "finishWithResult:"
+ "forceUpdateNocSigner:ownerSharedOperationalKeyPair:"
+ "getAppleAliroCredentialsWithCredentialType:startingAtIndex:credentials:flow:"
+ "getCredentialStatusWithParams:expectedValues:expectedValueInterval:completion:"
+ "getMaxPINCodeLength"
+ "getMinPINCodeLength"
+ "getNumberOfAccessoryServersForFabricUUID:completion:"
+ "getRequiredAttributesForCharacteristic:"
+ "getThreadNetworkConnectionStateWithFabricUUID:"
+ "getThreadNetworkNodeTypeWithFabricUUID:"
+ "getUserWithParams:expectedValues:expectedValueInterval:completion:"
+ "getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:"
+ "handlePairingCompletionForAccessoryWithNodeID:targetFabricUUID:fabricID:vendorID:productID:configNumber:category:topology:"
+ "handlePairingForThreadAccessoryWithTargetFabricUUID:nodeID:"
+ "handleRemoveFromBrowser"
+ "hapErrorWithCode:marker:"
+ "hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:hapServicesToCheckForRequiredAttributeValues:hapCharacteristicsToCheckForRequiredAttributeValues:server:"
+ "hasMatterThreadAccessoryInHomeWithFabricUUID:"
+ "hmmtr.CarbonDioxideConcentrationMeasurement"
+ "hmmtr.CarbonMonoxideConcentrationMeasurement"
+ "hmmtr.NitrogenDioxideConcentrationMeasurement"
+ "hmmtr.OzoneConcentrationMeasurement"
+ "hmmtr.PM10ConcentrationMeasurement"
+ "hmmtr.PM25ConcentrationMeasurement"
+ "hmmtr.TotalVolatileOrganicCompoundsConcentrationMeasurement"
+ "hmmtr.fabric.datacreator"
+ "hmmtr.fabric.datastorer"
+ "hmmtr.fabric.random.v0keystore"
+ "hmmtr.fabric.v0keystore"
+ "hmmtr.fabric.void.v0datastore"
+ "hmmtr.op.cert.issuer"
+ "identifyBridgeWithAggregatorEndpoint:completionHandler:"
+ "indexesOfObjectsPassingTest:"
+ "initWithCHIPStorageDelegate:keychainDelegate:v2FabricDataStoreDelegate:"
+ "initWithCredentialParams:"
+ "initWithCredentialType:andCredentialIndex:"
+ "initWithDevice:endpoint:queue:accessoryServer:"
+ "initWithDoorLock:device:queue:"
+ "initWithFabricData:chipStorageDelegate:keychainDelegate:v2FabricDataStoreDelegate:"
+ "initWithIdentifier:categoryNumber:isInvalid:"
+ "initWithMajorVersion:minorVersion:updateVersion:"
+ "initWithPrivateKeyExternalRepresentation:"
+ "initWithQueue:browser:fabricUUID:systemCommissionerFabric:"
+ "initWithQueue:privateDataSource:"
+ "initWithRemoteDelegate:fabricID:"
+ "initWithRootCert:ipk:residentNodeID:operationalCert:operationalKeyPair:"
+ "initWithRootKeyPair:rootCertificate:fabricID:"
+ "initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:residentOperationalKeyPair:residentOperationalCert:"
+ "ipkForTargetFabricUUID:forPairing:"
+ "isFirmwareUpdateInProgressForFabricUUID:"
+ "isInvalid"
+ "issuerCredentialForUser:flow:"
+ "keyEnumerator"
+ "legacyNodeIDForTargetFabricUUID:"
+ "locallyStoredFabricDataWithDataPresentInV2FabricDataStore:error:"
+ "lockStateKBNotificationRegistered"
+ "lockStateKBNotificationRegistrationToken"
+ "logoutNotificationRegistered"
+ "logoutNotificationRegistrationToken"
+ "mapCarbonMonoxideDetected:"
+ "mapSmokeDetected:"
+ "markAsSubscribed"
+ "markForResubscription"
+ "maxCoolSetpointLimit"
+ "maxHeatSetpointLimit"
+ "minCoolSetpointLimit"
+ "minHeatSetpointLimit"
+ "mtrBaseDeviceWithNodeID:controller:"
+ "mtrPluginDeviceControllerRegistry"
+ "mtrPluginSharedInstance"
+ "na_firstObjectPassingTest:"
+ "nativeMatterDeviceTypes"
+ "newFabricData"
+ "notifyThreadRadioStateChanged:nodeType:fabricUUID:"
+ "numberOfAliroDeviceKeyCredentialsSupportedWithFlow:completion:"
+ "numberOfAliroIssuerKeyCredentialsSupportedWithFlow:completion:"
+ "numberOfCredentialsSupportedPerUserWithFlow:"
+ "operationalNodeID"
+ "overrideLocationCheckForPairingForFabricUUID:"
+ "pairingRequest"
+ "postNotificationName:object:"
+ "prepareForPairingWithSetupPayload:targetFabricUUID:completionHandler:"
+ "prepareStorageForTargetFabricUUID:"
+ "prepareStorageForTargetFabricUUID:forInitialSetup:"
+ "propagateCharactersticValuesToAccessory:"
+ "publicKeyData"
+ "publicKeyDataFromCertificate:"
+ "publicKeyFromCSRInfo:error:"
+ "q24@?0@\"NSData\"8@\"NSData\"16"
+ "rcac"
+ "readAliroSupportedVersionWithFlow:"
+ "readAttributeAliroBLEAdvertisingVersionWithFlow:completion:"
+ "readAttributeAliroBLEAdvertisingVersionWithParams:"
+ "readAttributeAliroExpeditedTransactionSupportedProtocolVersionsWithFlow:completion:"
+ "readAttributeAliroExpeditedTransactionSupportedProtocolVersionsWithParams:"
+ "readAttributeAliroGroupResolvingKeyWithParams:"
+ "readAttributeAliroReaderGroupIdentifierWithParams:"
+ "readAttributeAliroReaderVerificationKeyWithParams:"
+ "readAttributeAliroSupportedBLEUWBProtocolVersionsWithFlow:completion:"
+ "readAttributeAliroSupportedBLEUWBProtocolVersionsWithParams:"
+ "readAttributeAppleAliroBLEAdvertisingVersionWithParams:"
+ "readAttributeAppleAliroExpeditedTransactionSupportedProtocolVersionsWithParams:"
+ "readAttributeAppleAliroGroupResolvingKeyWithParams:"
+ "readAttributeAppleAliroReaderGroupIdentifierWithParams:"
+ "readAttributeAppleAliroReaderGroupSubIdentifierWithParams:"
+ "readAttributeAppleAliroReaderVerificationKeyWithParams:"
+ "readAttributeAppleAliroSupportedBLEUWBProtocolVersionsWithParams:"
+ "readAttributeAppleNumberOfAliroCredentialIssuerKeysSupportedWithParams:"
+ "readAttributeAppleNumberOfAliroEndpointKeysSupportedWithParams:"
+ "readAttributeMaxCoolSetpointLimitWithParams:"
+ "readAttributeMaxHeatSetpointLimitWithParams:"
+ "readAttributeMeasuredValueWithParams:"
+ "readAttributeMeasurementUnitWithParams:"
+ "readAttributeMinCoolSetpointLimitWithParams:"
+ "readAttributeMinHeatSetpointLimitWithParams:"
+ "readAttributeMinPINCodeLengthWithParams:"
+ "readAttributeNumberOfAliroCredentialIssuerKeysSupportedWithParams:"
+ "readAttributeNumberOfAliroEndpointKeysSupportedWithParams:"
+ "readAttributeNumberOfCredentialsSupportedPerUserWithParams:"
+ "readAttributePeakMeasuredValueWithParams:"
+ "readAttributePluginMeasuredValueWithParams:"
+ "readAttributePluginPeakMeasuredValueWithParams:"
+ "reloadOperationalFabricData"
+ "remoteDelegate"
+ "removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:"
+ "removeActiveClientWithFabricUUID:updateConnectionIdleTimeout:reason:"
+ "removeActiveSecondaryClientWithFabricUUID:updateConnectionIdleTimeout:reason:"
+ "removeObjectsAtIndexes:"
+ "removeObjectsInArray:"
+ "removeReportObserver:"
+ "removeTargetFabricUUID:"
+ "reportObservers"
+ "requiresRemoteFabricDataUpdateThroughPairingCompletionMessage"
+ "residentOpKeyPair"
+ "residentOperationalCert"
+ "residentOperationalKeyPair"
+ "restartNormalOperation"
+ "retrieveHAPCharacteristicsToCheckForRequiredAttributeValues"
+ "retrieveOperationalCertificatesForFabricID:commissioneeNodeID:publicKey:completion:"
+ "runAfterCommissioningToTargetFabricUUID:controllerSetUpBlock:"
+ "self.fabricID"
+ "self.rootCertificate"
+ "setAliroReaderConfigWithParams:expectedValues:expectedValueInterval:completion:"
+ "setBleAdvertisingVersion:"
+ "setBleUWBSupportedVersions:"
+ "setCredentialWithParams:expectedValues:expectedValueInterval:completion:"
+ "setCurrentFabricUUID:"
+ "setDidSendRevokeAvailableOnResume:"
+ "setEndpointToDeviceTypesMap:"
+ "setExpeditedTransactionSupportedVersions:"
+ "setFabricDataItems:"
+ "setFabricUUID:"
+ "setFabricUUIDOfActiveThreadNetwork:"
+ "setFabricUUIDOfPendingStartPairingBlock:"
+ "setFirmwareVersion:"
+ "setLockStateKBNotificationRegistered:"
+ "setLockStateKBNotificationRegistrationToken:"
+ "setLogoutNotificationRegistered:"
+ "setLogoutNotificationRegistrationToken:"
+ "setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:forTargetFabricUUID:"
+ "setPairingRequest:"
+ "setPairingTargetFabricData:targetFabricUUID:"
+ "setRootPublicKey:"
+ "setShouldReestablishSubscription:"
+ "setSuspendedActiveClientFabricUUID:"
+ "setUserUniqueID:"
+ "setUserUniqueIdentifierToUser:"
+ "setUserWithParams:expectedValues:expectedValueInterval:completion:"
+ "setV2FabricDataStoreDelegate:"
+ "setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:"
+ "setupStorageStateForHomeFabricUUID:"
+ "setupStorageStateForHomeFabricUUID:completion:"
+ "setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricUUID:"
+ "shouldReestablishSubscription"
+ "sortUsingSelector:"
+ "sortedArrayOfData:"
+ "sortedArrayUsingComparator:"
+ "startAccessoryFirmwareUpdateWithExtendedMACAddress:fabricUUID:isWedDevice:completion:"
+ "startAccessoryPairingWithExtendedMACAddress:fabricUUID:isWedDevice:completion:"
+ "startThreadRadioForHomeWithFabricUUID:"
+ "startThreadRadioForHomeWithFabricUUID:preventDisconnect:"
+ "startThreadRadioForSystemCommissionerFabricUUID:"
+ "stopAccessoryFirmwareUpdateWithFabricUUID:completion:"
+ "stopAccessoryPairingWithFabricUUID:completion:"
+ "stopThreadOnUserLogout"
+ "stopThreadRadioForHomeWithFabricUUID:"
+ "stopThreadRadioForSystemCommissionerFabricUUID:"
+ "storageDataSource"
+ "storageDataSourceForFabricUUID:"
+ "storeFabricData:"
+ "supportedLinkLayerTypesContainsEthernet:"
+ "supportedLinkLayerTypesContainsThread:"
+ "supportedLinkLayerTypesContainsWiFi:"
+ "suspendOperationsForFabricUUID:"
+ "suspendedActiveClientFabricUUID"
+ "suspendedActiveSecondaryClientFabricUUIDs"
+ "systemCommissionerFabricUUID"
+ "unsetFeatureMatterRVCForTests"
+ "updateAccessory:withServices:"
+ "updateAccessoryACLForFabric:"
+ "updateAllTargetFabricUUIDs:"
+ "updateKeyValueStoreWithEntries:"
+ "updateNocSigner:ownerSharedOperationalKeyPair:"
+ "updateStorageWithPrivateKeyData:"
+ "updateUserUniqueIDForUserIndex:userUniqueID:flow:"
+ "updatedValuePluginMeasuredValueForAttributeReport:responseHandler:"
+ "updatedValuePluginPeakMeasuredValueForAttributeReport:responseHandler:"
+ "userUniqueIdentifierToUser"
+ "v104@0:8@16@24@32@40@48@56@64@72@80@88@?96"
+ "v16@?0Q8"
+ "v24@0:8@\"MTRDeviceController\"16"
+ "v24@0:8@\"NSArray\"16"
+ "v24@?0@\"HMMCredentialKey\"8@\"MTRDoorLockClusterGetCredentialStatusResponseParams\"16"
+ "v28@0:8B16q20"
+ "v2FabricDataStoreDelegate"
+ "v32@0:8@\"MTRDeviceController\"16@\"MTRCommissioneeInfo\"24"
+ "v32@0:8@\"NSUUID\"16@?<v@?Q>24"
+ "v32@?0@\"NSNumber\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v40@?0@\"NSString\"8@\"NSNumber\"16@\"NSNumber\"24@\"NSError\"32"
+ "v44@?0@\"HMMTRHAPAccessoryInfo\"8B16@\"NSNumber\"20@\"HMMTRDeviceTopology\"28@\"NSError\"36"
+ "v60@?0@\"HMMTRHAPAccessoryInfo\"8B16@\"NSNumber\"20@\"HMMTRDeviceTopology\"28@\"HMMTRHAPAccessoryInfo\"36@\"HMMTRDeviceTopology\"44@\"NSError\"52"
+ "v64@0:8@16@24@32@40@48@56"
+ "v68@0:8@16@24@32@40B48@52@?60"
+ "v76@0:8@16@24B32@36@44@52@60@?68"
+ "v80@0:8@16@24@32@40@48@56@64@72"
+ "v80@0:8@16@24@32@40@48@56@64@?72"
+ "versionString"
+ "weakObjectsHashTable"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"NSString\"8"
+ "\xf0\x82\xc1\xf0\xf1\xc1"
- "%{public}@!!! NOC Signer keypair failed to load, browser may not be operational !!!"
- "%{public}@!!!Failed to reload keypair!!! Keypair is useless now. "
- "%{public}@#### Failed fetching NOC for shared user with error %@"
- "%{public}@%@ [Event no. %@, UpTime %@] Startup Event %@, delegated: %@"
- "%{public}@AbsMaxCoolSetpointLimit attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@AbsMaxHeatSetpointLimit attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@AbsMinCoolSetpointLimit attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@AbsMinHeatSetpointLimit attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@Allowing thread stop for fabricID %@"
- "%{public}@An error occurred while getting all the device types for each endpoint. %@. DeviceTypes: %@"
- "%{public}@An error occurred while getting all the endpoints for the aggregate node (bridge) endpoint: %@"
- "%{public}@Apple Home fabrics root key pair is loaded"
- "%{public}@Apple Home fabrics root keypair has changed."
- "%{public}@Attempting to persist %@"
- "%{public}@Attribute node label absent from cache"
- "%{public}@AttributeList attribute for cluster class %@ on endpoint %@ absent from cache"
- "%{public}@Attributes %@ for characteristic %@ not found in supported attribute list %@ for endpoint %@"
- "%{public}@Bad params: %@"
- "%{public}@CHIP Stack is not running"
- "%{public}@Cached Root certificate not found"
- "%{public}@Cached Root certificate uses unexpected operational key pair"
- "%{public}@Cached Root/Operational certificates are not found in storage"
- "%{public}@Cached Root/Operational certificates are valid"
- "%{public}@Cached data is not valid"
- "%{public}@Cached root certificate: %@, matches: %@"
- "%{public}@Cached root/NOC in storage has invalid fabric ID %@ vs expected %@"
- "%{public}@Cannot process request without fabric data created for fabric %@, fabricID %@"
- "%{public}@Cannot process request without fabric data for fabric %@"
- "%{public}@Cannot read from disk when fabric ID is not valid"
- "%{public}@Cannot read from storage when fabric ID is not valid"
- "%{public}@Cannot retrieve current home fabric device controller because of missing target fabric for fabric ID %@"
- "%{public}@Cannot retrieve current home fabric device controller wrapper because of missing target fabric for fabric ID %@"
- "%{public}@Certificate data is valid"
- "%{public}@Characteristic (%@), Added completion handler at index %@"
- "%{public}@Characteristic (%@), Added default argument %@ at index %@"
- "%{public}@Characteristic (%@), Added primary argument %@ at index %@"
- "%{public}@Characteristic (%@), numberOfArguments = %@"
- "%{public}@Check validity period of the Matter SDK stored root cert of fabric ID %@"
- "%{public}@Check validity period of the root cert of fabric ID %@"
- "%{public}@Cluster class name not found for mandatory characteristic %@ in use at endpoint %@"
- "%{public}@Cluster class name not found for optional characteristic %@ in use at endpoint %@"
- "%{public}@Cluster classes to query for attributes : %@"
- "%{public}@Cluster classes to query for feature map : %@"
- "%{public}@ColorTempPhysicalMaxMireds attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@ColorTempPhysicalMinMireds attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@Commissioning session was already pre-warmed"
- "%{public}@Comparing device feature map %u with characteristic %@ required feature map %u"
- "%{public}@Computed service label index map for non-bridged accessory %@ : %@"
- "%{public}@Connection has become idle but there are still active clients, keeping matter stack active for fabricID %@. Fabrics with active clients: %@, secondary clients: %@"
- "%{public}@Connection has become idle, but FW update is active, keeping matter stack active for fabricID %@. Fabrics with active clients: %@, secondary clients: %@"
- "%{public}@Connection has become idle, shutting down matter stack for fabricID %@. Fabrics with active clients: %@"
- "%{public}@Constructed HAP service description for HAP Characteristic %@, CHIP clusterID %@, endpoint %@"
- "%{public}@Constructed HAP service description for optional HAP Characteristic %@, CHIP clusterID %@, endpoint %@"
- "%{public}@Constructed bridge accessory @%@"
- "%{public}@Constructed new service to add %@ at endpoint %@"
- "%{public}@Constructing arguments for invocation for characteristic: %@, selector: %@, endpoint: %@"
- "%{public}@Could not construct any of the services."
- "%{public}@Could not fetch current pairing because no device paired: %@"
- "%{public}@Could not fetch pairings because no device paired: %@"
- "%{public}@Could not fetch serial number because no device paired: %@"
- "%{public}@Could not obtain fabric ID for pairing from root cert %@"
- "%{public}@Could not pre-warm commissioning session when fabric was never created"
- "%{public}@Could not pre-warm due to failure to fetch root cert for fabricID %@"
- "%{public}@Could not remove pairing %@ because no device paired: %@"
- "%{public}@Could not retrieve hap category: %@"
- "%{public}@Could not update fabric label to %@ because no device paired %@"
- "%{public}@Couldn't convert NOC to Matter format"
- "%{public}@Creating new fabric data for fabric ID: %@"
- "%{public}@Creating operational certificate for controller node ID %@ CAT %@ root cert %@, fabric ID %@"
- "%{public}@Current Matter stack is running for fabric Index %@ and therefore request to handle pairing on fabric ID %@ cannot be processed"
- "%{public}@Current fabric ID changed from %@ to %@"
- "%{public}@Device Type Enumeration : Got at endpoint %@ following device types in use %@"
- "%{public}@Device Type Enumeration The List of device types @%@"
- "%{public}@DeviceList is incomplete, proceeding anyway. Only partial enumeration is possible"
- "%{public}@Dropping existing service %@"
- "%{public}@Dropping notification as the fabricID does not match that of the active network, activeNetworkFabricID: %@, fabricID: %@"
- "%{public}@Dumping stack storage for params"
- "%{public}@Endpoints In Use for the bridge: %@. Error: %@"
- "%{public}@Error in protocol map plist. Required value for priority order not found"
- "%{public}@Error: %@. Failed to establish a connection to the device for unpairing. The device will not be notified of removal"
- "%{public}@Evicting fabricID: %@"
- "%{public}@Examining MTRClusterDescriptor cluster parts list at endpoint %@ to retrieve endpoints in use."
- "%{public}@Examining MTRClusterDescriptor device list at endpoint %@"
- "%{public}@FATAL Error: Failed to generate IPK for fabric ID %@"
- "%{public}@Fabric %@ has become idle, but current FabricID is %@, not stopping current matter stack. fabrics with active clients:%@"
- "%{public}@Fabric data source not available; failed to get ipk for fabric ID %@"
- "%{public}@Fabric data source not available; failed to get legacy node ID for fabric ID %@"
- "%{public}@Fabric key pairs are missing. Declining to fetch certificates."
- "%{public}@Fabric storage for fabric ID %@ does not include paired node IDs"
- "%{public}@FabricID from cached Root (%@) doesn't match expected value (%@)"
- "%{public}@Failed to Get Root/Operational Certificate for accessory from Owner with error %@"
- "%{public}@Failed to convert public key to NSData for transmission with error %@"
- "%{public}@Failed to create Matter Key Pairs for pairing"
- "%{public}@Failed to create fabric data as existing data is already valid"
- "%{public}@Failed to create fabric data by non-owner user"
- "%{public}@Failed to create fabric data due to incorrect fabric ID %@"
- "%{public}@Failed to create operational certificate for controller node ID %@ CAT %@ with error %@"
- "%{public}@Failed to create operational certificates from owner with error %@"
- "%{public}@Failed to fetch Apple Home fabric public key"
- "%{public}@Failed to fetch Apple Home fabric public key; Key-pair doesn't exist"
- "%{public}@Failed to fetch Certificates OR Owner Node ID required for pairing"
- "%{public}@Failed to fetch Fabric object for target fabric ID %@ or Home UUID %@"
- "%{public}@Failed to fetch IPK for fabric ID: %@"
- "%{public}@Failed to fetch Root / Operational Certificate for accessory getting paired with error %@"
- "%{public}@Failed to fetch cert for fabric ID: %@, error: %@"
- "%{public}@Failed to fetch certificates for owner"
- "%{public}@Failed to fetch certificates required for pairing on fabricID %@ with error %@ and underlying error %@"
- "%{public}@Failed to fetch certificates required for pairing with error %@"
- "%{public}@Failed to fetch clusters in use at endpoint %@"
- "%{public}@Failed to fetch commissioning certificates for fabric ID %@ with error %@"
- "%{public}@Failed to find HAP characteristic ID for characteristic %@ on endpoint %@, aborting"
- "%{public}@Failed to find HAP to CHIP cluster mapping for characteristic %@ on endpoint %@, aborting"
- "%{public}@Failed to find accessory getting paired"
- "%{public}@Failed to find nodeID matching device identifier %@ in fabric ID %@"
- "%{public}@Failed to generate IPK"
- "%{public}@Failed to generate Operational Certificate with error %@"
- "%{public}@Failed to generate operational certificate with error %@"
- "%{public}@Failed to generate root certificate with error %@"
- "%{public}@Failed to get HAP Services at Endpoint:%@. Error:%@. Error is not fatal, continuing with enumeration"
- "%{public}@Failed to get HAP Services from plist for endpoint:%@. Error:%@"
- "%{public}@Failed to get controller wrapper for the fabric ID %@"
- "%{public}@Failed to get device attribute list for cluster class name %@ at endpoint %@. Error: %@"
- "%{public}@Failed to get device feature map value for characteristic %@ with cluster class name %@ at endpoint %@"
- "%{public}@Failed to get device feature map value for cluster class name %@ at endpoint %@. Ignoring feature map errors"
- "%{public}@Failed to load NOC for shared user with error %@"
- "%{public}@Failed to load NodeID set for fabric ID %@ with error: %@"
- "%{public}@Failed to load certificates for fabric ID %@ with error %@"
- "%{public}@Failed to load certs from resident without operational key"
- "%{public}@Failed to persist legacy node with error %@"
- "%{public}@Failed to persist new fabric data"
- "%{public}@Failed to serialize operational key pair for new fabric. Aborting pairing prep."
- "%{public}@Failed to setup storage for new fabric. Aborting pairing prep."
- "%{public}@Failed to start matter stack for fabric ID: %@"
- "%{public}@Faking a color temperature attribute report %@ on endpoint %@ upon hue/sat command invocation, updatedAttributesHandler %@"
- "%{public}@Feature map information not available for mandatory characteristic %@ on endpoint %@"
- "%{public}@Feature map information not available for optional characteristic %@ on endpoint %@"
- "%{public}@Feature map not in cache for cluster class %@"
- "%{public}@Fetching server list from descriptor cluster at endpoint %@, bridgeAggregateNodeEndpoint %@, isComposedDevice %d"
- "%{public}@Found required feature map %@ for mandatory characteristic %@ on endpoint %@"
- "%{public}@Found required feature map %@ for optional characteristic %@ on endpoint %@"
- "%{public}@Generated new fabric ID: %@"
- "%{public}@Generating NOC for Owner %@"
- "%{public}@Generating a OP cert for %s Controller with nocSigner %@, rootCert = %@, pubKeyAsSecKey %@, fabricID %@, nodeID %@"
- "%{public}@Generating a random Node ID %@ for Owner"
- "%{public}@Generating new IPK for fabric ID %@"
- "%{public}@Generating new NOC using node ID = %@"
- "%{public}@Generating root certificate using issuer ID %@"
- "%{public}@HAP characteristics support verification failed with error : %@"
- "%{public}@HMMTRAccessoryServer handleEventReportForNotification: Ignoring event report, this is an outdated report. event report=%@"
- "%{public}@HMMTRSyncClusterDoorLock initWithDevice called with device: %@, baseDevice: %@ and endpoint: %@"
- "%{public}@Handling pairing completion for Accessory with Node ID %@, Fabric ID %@, Vendor ID %@, Product ID %@, Config Number %@, Category %@"
- "%{public}@Handling special case lock target state write"
- "%{public}@Hitting maximum number of getters. Removing unused and restarting factory. Currently used: %@"
- "%{public}@IPK missing for fabric ID %@"
- "%{public}@Identify on aggregator failed."
- "%{public}@Identify on aggregator successful"
- "%{public}@Ignoring thread start for fabric %@, network is locked to fabricID %@"
- "%{public}@Invalid fabricID, ignoring thread radio start"
- "%{public}@Key pair creation failed. Cannot move on with pairing preparation."
- "%{public}@Key pairs are not present. Cannot move forward."
- "%{public}@Key value could not be deserialized: %@"
- "%{public}@Keypair data was not changed not reloading"
- "%{public}@Loading certificate data for pairing from %s"
- "%{public}@Loading certificate data from disk"
- "%{public}@Loading certificate data from remote source"
- "%{public}@Loading certificate data from storage"
- "%{public}@Loading certificate data, pairing: %@, resident fetch: %@"
- "%{public}@Loading from resident completed with error %@"
- "%{public}@Loading from storage completed with error %@"
- "%{public}@Looking for optional HAP Characteristic %@ as its matching CHIP clusterID %@ on endpoint %@"
- "%{public}@Looking for required HAP Characteristic %@ as its matching CHIP clusterID %@ on endpoint %@"
- "%{public}@Making room for fabricID: %@"
- "%{public}@Mandatory characteristic %@ cannot be found in clusters in use at endpoint %@."
- "%{public}@NOC for accessory:"
- "%{public}@New fabric %@"
- "%{public}@New operation privilege CAT %@ missing from current NOC: %@, fetching a new NOC."
- "%{public}@Newly generated fabric data is invalid"
- "%{public}@No Endpoints In Use at endpoint 0: %@"
- "%{public}@No Information for Characteristic %@"
- "%{public}@No accessory server browser to move on with pairing"
- "%{public}@No clusters in use at endpoint %@"
- "%{public}@No endpoints contain clusters, not storing topology. Enumeration will re-run next time."
- "%{public}@No fabric parameters for fabric ID %@ - no controller configured"
- "%{public}@No need to fetch NOC again for updated operate privilege CAT: %@ as current NOC contains %@"
- "%{public}@No operational key created yet. Aborting fabric cert loading."
- "%{public}@No paired NodeIDs set for fabric ID %@"
- "%{public}@No resident reachable for fabricID %@ and there are active clients, start local stack"
- "%{public}@NodeID %@ returned for fabric ID %@ and device identifier %@"
- "%{public}@Not shutting down stack for fabricID %@ because there is an active client"
- "%{public}@Not shutting down stack for fabricID %@ because there is an active connection"
- "%{public}@Not shutting down stack for fabricID %@ because there is an active secondary client"
- "%{public}@Not starting local discovery for fabricID %@, resident available"
- "%{public}@Operational Keypair of the cached NOC doesn't match current keypair"
- "%{public}@Operational certificate fabric ID %@ doesn't match fabric ID of current fabric"
- "%{public}@Operational key pair for Apple Home fabrics is loaded."
- "%{public}@Operational keypair for Apple Home fabrics has changed."
- "%{public}@Optional characteristic %@ cannot be found in clusters in use at endpoint %@."
- "%{public}@Optional characteristic %@ on endpoint %@ requires an additional Optional Matter attribute check"
- "%{public}@Order attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@Owner user - No need to request NOC"
- "%{public}@Pairing accessory requires retrieving controller wrapper with fabric ID: %@"
- "%{public}@Parts list absent from cache"
- "%{public}@Per controller storage API enabled = %@ (pref value %@)"
- "%{public}@Per-controller storage is not enabled to configure controller for fabric ID %@ upfront"
- "%{public}@Pre-warming system commissioning device controller"
- "%{public}@Prepare pairing with setup payload: %@, fabric ID: %@, owner: %@, ownerCertFetchSupported: %@"
- "%{public}@Preventing thread stop for fabricID %@ because preventDisconnect is true and locked to fabricID %@"
- "%{public}@Preventing thread stop for system commissioner fabricID %@ because preventDisconnect is true and locked to fabricID %@"
- "%{public}@Prewarming Matter device controller"
- "%{public}@Querying device cluster %@ at endpoint %@ for feature map value"
- "%{public}@Querying device cluster %@ at endpoint %@ for supported attributes"
- "%{public}@Read cached operational cert data from disk self.rootCert %@, self.operationalCert %@ self.residentNodeID %@ self.ownerIPK %@"
- "%{public}@Reading disk data for current fabric"
- "%{public}@Received Root Certificate %@, Operational Certificate %@, Owner Node ID %@, and IPK %@ from Resident"
- "%{public}@Received feature map from accessory for cluster class %@. Value: %@"
- "%{public}@Received supported attributes list from accessory for cluster class %@ on endpoint %@. Attributes: %@"
- "%{public}@Received suspendOperations, but no active fw updates in progress for fabricID %@"
- "%{public}@Received thread radio state changed notification, connectionState: %ld, nodeType: %ld, fabricID:%@, last known connectionState: %ld"
- "%{public}@Remote storage is not yet available for fabric index = %@"
- "%{public}@Removed unsupported characteristic %@ for endpoint %@"
- "%{public}@Removing fabricID %@ from active clients and aborting operations"
- "%{public}@Request for nodeID failed to find storage for matching fabric ID: %@"
- "%{public}@Requesting certificates required for commissioning from Resident device"
- "%{public}@Requesting signed operational certificate from Resident device for commissionee with node ID %@"
- "%{public}@Resident NOC %@ resident node ID %@"
- "%{public}@Resident is not yet reachable to get NOC"
- "%{public}@Resident reachability changed for non-current fabricID %@, ignoring"
- "%{public}@Retrieved at endpoint %@ following HAP categories in use %@"
- "%{public}@Retrieved at endpoint %@ following clusters in use %@"
- "%{public}@Returning Root Certificate %@, Operational Certificate %@, Owner NodeID %@, and IPK %@ to %s Controller"
- "%{public}@Returning certificates fetched from disk: Root Certificate %@, Operational Certificate %@, Resident NodeID %@, and IPK %@"
- "%{public}@Root Certificate not found in storage; generating a new one using issuer ID %@"
- "%{public}@Root certificate fabric ID %@ doesn't match fabric ID of current fabric"
- "%{public}@Root certificate:"
- "%{public}@ServerList at endpoint %@ absent from cache"
- "%{public}@ServerList attribute at endpoint %@ absent from cache"
- "%{public}@Service label index enumerated to %@ for endpoint %@"
- "%{public}@Setting root and operational cert in start up params %@ %@ for current home controller using %s operational key and %s NOC issuer"
- "%{public}@Setting root and operational cert in start up params %@ %@ for current home controller with UUID %@ using %s operational key and %s NOC issuer"
- "%{public}@Setting up controller for Home fabric %@ in order to pre-warm commissioning session"
- "%{public}@Setting up controller wrapper for Home FabricID = %@, currentFabricID = %@"
- "%{public}@Setting up storage state after cert fetch for Home Fabric ID = %@"
- "%{public}@Setting up storage state for Home Fabric ID = %@"
- "%{public}@Setting up storage state to persist for Home Fabric ID = %@"
- "%{public}@Shared Admin is attempting to pair"
- "%{public}@Shutting down stack for fabricID %@ because there are no active clients"
- "%{public}@Sources attribute from the %@ cluster endpoint:%@ absent from cache"
- "%{public}@Start thread for fabricID %@, preventDisconnect = %@, last known connectionState: %ld"
- "%{public}@Start thread for system commissioner fabric ID %@"
- "%{public}@Started Matter controller '%@' with Node ID %@ on fabric ID %@"
- "%{public}@Starting discovery for fabricID %@ because there are active clients"
- "%{public}@Starting discovery stack for fabricID %@ because there are active clients"
- "%{public}@Starting pairing"
- "%{public}@Starting stack for fabricID %@ because there are active clients and local stack is unconfigured"
- "%{public}@Starting thread for fabricID %@ because it became the current fabric"
- "%{public}@State Capture: No Endpoints In Use at endpoint 0"
- "%{public}@Stop thread for fabricID %@"
- "%{public}@Stop thread for system commissioner fabric ID %@"
- "%{public}@Stopping operation with system commissioner fabric ID %@"
- "%{public}@Stopping the matter stack for FabricID = %@"
- "%{public}@Storage doesn't have f/%x/n"
- "%{public}@Storage is already configured. Prewarming Matter device controller."
- "%{public}@Storage state cannot be setup without fabric ID"
- "%{public}@Storing the initial Matter storage to remote %@"
- "%{public}@Successfully created fabric data for %@"
- "%{public}@Successfully created operational certificates from owner for fabric ID %@. Root Certificate %@, Operational certificate %@, Owner NodeID %@"
- "%{public}@Successfully fetched Owner NOC from storage"
- "%{public}@Successfully fetched Owner Node ID from storage"
- "%{public}@Successfully fetched Root %@ and Operational Certificate %@ for accessory getting paired"
- "%{public}@Successfully fetched Root certificate from storage"
- "%{public}@Successfully fetched commissioning certificates for fabric ID %@"
- "%{public}@Successfully generated Operational Certificate using Root Certificate from storage"
- "%{public}@Successfully generated Operational Certificate using SDK Root Certificate and Node ID from storage"
- "%{public}@Successfully generated Operational Certificate using newly generated Root Certificate"
- "%{public}@Successfully persisted legacy node to Apple Home storage with %lu keys"
- "%{public}@Successfully persisted new fabric with %@ and created new controller with %@"
- "%{public}@Successfully received signed Operational Certificate %@ for Accessory with node ID %@ from Owner"
- "%{public}@Supported attributes selector not found for cluster: %@"
- "%{public}@This resident is not configured for any fabric as fabricID is nil"
- "%{public}@Thread is not active"
- "%{public}@Thread network connection state: %@ for fabricID: %@, calling start pairing block now"
- "%{public}@Thread network connection state: %@ for fabricID: %@, calling start pairing block now. ActiveThreadNetworkFabricID: %@"
- "%{public}@Thread network connection state: %@ for fabricID: %@, deferring call to start pairing block. ActiveThreadNetworkFabricID: %@"
- "%{public}@Thread network is already running for fabric ID %@. Not starting Thread."
- "%{public}@Thread start already pending, ignoring startThread request for fabricID %@"
- "%{public}@Thread start called for new fabricID %@, will be disconnecting from thread network for fabricID %@"
- "%{public}@Total endpoints In Use at endpoint 0: %@. Error: %@"
- "%{public}@Trying to reload keypair from keychain"
- "%{public}@Unable to get additional thread information from accessory after firmware update for nodeID %@, error: %@"
- "%{public}@Unable to get controller wrapper for fabric ID: %@"
- "%{public}@Unexpected nested aggregate type %@"
- "%{public}@Unexpected state, fabricIDOfActiveThreadNetwork = %@, preventDisconnect = %@"
- "%{public}@Unexpected storage fabric ID %@ after generating cert for fabric ID %@"
- "%{public}@Unexpected user privilege for user"
- "%{public}@UpdateNotifications received for fabricID:%@ enabled:%@ keepAliveOnly:%@. currentFabricID %@, browserState = %lu, fabricsWithActiveClients = %@, fabricWithActiveSecondaryClients = %@"
- "%{public}@UpdateNotifications received nil fabricID for fabric: %@. Ignoring request"
- "%{public}@Updated OTA requestor endpoints in topology"
- "%{public}@Updating CATs (admin %@, user %@) for FabricID (browser's %@, server's %@, storage's %@"
- "%{public}@Updating fabric ID to %@ for Shared Home"
- "%{public}@Using Cached Operational certificate"
- "%{public}@Using Cached Root certificate"
- "%{public}@Using Cached Root/Operational certificates"
- "%{public}@Using fabric ID %@ for pairing from retrieved cert"
- "%{public}@Using fabricID = %lld for pairing. Root Certificate %@"
- "%{public}@Write Occupied Heating/Cooling Setpoint (sync): An error occurred while trying to read the min/max cool setpoints"
- "%{public}@Write Occupied Heating/Cooling Setpoint (sync): An error occurred while trying to read the min/max heat setpoints"
- "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target cool temperature out of supported max setpoint limit. Setting it to %@"
- "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target cool temperature out of supported min setpoint limit. Setting it to %@"
- "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target heat temperature out of supported max setpoint limit. Setting it to %@"
- "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target heat temperature out of supported min setpoint limit. Setting it to %@"
- "%{public}@[Flow: %@] Failed to get base device. matter device: %@, base device: %@, getBaseDeviceError: %@"
- "%{public}@[Flow: %@] Found base device: %@. matterDevice: %@"
- "%{public}@[Flow: %@] Getting base device with nodeID: %@"
- "%{public}@[Flow: %@] addCredentialData: %@ forCredentialType: %@, atIndex: %ld forUserAtUserIndex: %ld"
- "%{public}@[Flow: %@] addIssuerKeyData: %@, isUnifiedAccess: %ld, credentialType: %@, forUserIndex: %ld"
- "%{public}@_connectPendingFabricConnectionsForFabricID for fabricID - %@"
- "%{public}@_handleThreadRadioStateChanged - requiresThreadRouter = %@ (isWED = %@, isControllerInSleepyRouterState = %@, primaryReachableAndThreadCapable = %@)"
- "%{public}@abortAllOperations for fabricID: %@"
- "%{public}@configuring controller for fabric ID %@"
- "%{public}@discoverAccessoryServerWithNideId %@"
- "%{public}@f/%x/n doesn't match "
- "%{public}@fabric storage is not set %@"
- "%{public}@fetchClientClustersForDevice: Examining MTRBaseClusterDescriptor clientlist attribute at endpoint %@ to retrieve client clusters."
- "%{public}@fetchClientClustersForDevice: Retrieved the following client clusters %@"
- "%{public}@fetchClusterAcceptedCommandsForDevice: Examining MTRBaseClusterDescriptor cluster acceptedCommandList attribute at endpoint %@ to retrieve accepted commands."
- "%{public}@fetchClusterAcceptedCommandsForDevice: For endpoint %@, cluster %@, retrieved the following accepted command list %@"
- "%{public}@fetchClusterAttributesForDevice: Examining MTRBaseClusterDescriptor attributelist attribute at endpoint %@ to retrieve cluster attributes."
- "%{public}@fetchClusterAttributesForDevice: For endpoint %@, cluster %@, retrieved the following attributes %@"
- "%{public}@fetchClusterEventListForDevice: Examining MTRBaseClusterDescriptor eventlist attribute at endpoint %@ to retrieve events."
- "%{public}@fetchClusterEventListForDevice: For endpoint %@, cluster %@, retrieved the following events %@"
- "%{public}@fetchClusterFeatureMapForDevice: Examining MTRBaseClusterDescriptor cluster feature map attribute at endpoint %@ to retrieve feature map."
- "%{public}@fetchClusterFeatureMapForDevice: For endpoint %@, cluster %@, retrieved the following feature map %@"
- "%{public}@fetchClusterGeneratedCommandsForDevice: Examining MTRBaseClusterDescriptor cluster generated command list attribute at endpoint %@ to retrieve accepted commands."
- "%{public}@fetchClusterGeneratedCommandsForDevice: For endpoint %@, cluster %@, retrieved the following generated command list %@"
- "%{public}@fetchClusterRevisionForDevice: Examining MTRBaseClusterDescriptor cluster revision attribute at endpoint %@ to cluster revision number."
- "%{public}@fetchClusterRevisionForDevice: For endpoint %@, cluster %@, retrieved the revison number %@"
- "%{public}@fetchDeviceTypesWithMTRDevice: At endpoint %@, retrieved the following device types in use %@"
- "%{public}@fetchDeviceTypesWithMTRDevice: Examining MTRClusterDescriptor cluster parts list at endpoint %@ to retrieve device types."
- "%{public}@fetchPartsListForDevice: Examining MTRClusterDescriptor cluster parts list at endpoint %@ to retrieve endpoints in use."
- "%{public}@fetchPartsListForDevice: Failed to read parts list."
- "%{public}@fetchPartsListForDevice: Retrieved the following parts list in use %@"
- "%{public}@fetchServerClustersForDevice: Examining MTRBaseClusterDescriptor serverlist attribute at endpoint %@ to retrieve server clusters."
- "%{public}@fetchServerClustersForDevice: Retrieved the following server clusters %@"
- "%{public}@handleThreadDirectConnectionSleepyTypeChange - requiresThreadRouter = %@ for accessory with nodeID %@ (isWED = %@, isSleepyLink = %@, primaryReachableAndThreadCapable = %@)"
- "%{public}@keypair was deleted, not reloading..."
- "%{public}@no fabricID was provided, restarting with fabric with active client: %@"
- "%{public}@tempRootCert %@ && tempOperationalCert %@ && tempResidentNodeID %@ && tempOwnerIPK %@"
- "%{public}@updateAllConnectionIdleTimeoutsToMinimum for fabricID: %@"
- "@\"<HMMTRFabricDataFetcherCHIPStorageDelegate>\""
- "@\"<HMMTRFabricDataFetcherKeychainDelegate>\""
- "@\"<HMMTRHMDHAPAccessoryDelegate>\""
- "@\"MTRBaseClusterDoorLock\""
- "@\"MTRBaseDevice\""
- "@\"NAFuture\"16@?0@\"NSArray\"8"
- "@24@0:8^@16"
- "@36@0:8q16B24@28"
- "@52@0:8@16@24S32@36@44"
- "B32@?0@\"MTRDoorLockClusterDlCredential\"8Q16^B24"
- "HMMTRCachedFabricCertificateData"
- "HMMTRFabricDataFetcher"
- "HMMTRFabricDataFetcherKeychainDelegate"
- "I24@0:8@16"
- "MTRPersistentStorageDelegate"
- "MatterPincodes"
- "MatterTTU"
- "No"
- "Shared Admin"
- "Storage"
- "T@\"<HMMTRDeviceControllerStorageDataSource>\",&,N,V_privateDataSource"
- "T@\"<HMMTRFabricDataFetcherCHIPStorageDelegate>\",W,N,V_chipStorageDelegate"
- "T@\"<HMMTRFabricDataFetcherKeychainDelegate>\",W,N,V_keychainDelegate"
- "T@\"<HMMTRHMDHAPAccessoryDelegate>\",W,N,V_hmdHAPAccessoryDelegate"
- "T@\"HMMTRAccessoryServer\",&,N,V_commissioneeAccessoryServer"
- "T@\"HMMTRMatterKeypair\",&,N,V_nocSigner"
- "T@\"HMMTRMatterKeypair\",&,N,V_operationalKeyPair"
- "T@\"HMMTRMatterKeypair\",&,N,V_ownerLocalOperationalKeyPair"
- "T@\"MTRBaseClusterDoorLock\",&,V_baseDoorLock"
- "T@\"MTRBaseClusterDoorLock\",R,V_baseDoorLock"
- "T@\"MTRBaseDevice\",&,V_baseDevice"
- "T@\"MTRBaseDevice\",R,V_baseDevice"
- "T@\"NSData\",R,C,V_operationalCertificate"
- "T@\"NSNumber\",&,N,V_certificateIssuerID"
- "T@\"NSNumber\",&,N,V_configuredPreWarmTargetFabricID"
- "T@\"NSNumber\",&,N,V_currentFabricID"
- "T@\"NSNumber\",&,N,V_fabricIDOfActiveThreadNetwork"
- "T@\"NSNumber\",&,N,V_fabricIDOfPendingStartPairingBlock"
- "T@\"NSNumber\",&,N,V_preWarmedFabricID"
- "T@\"NSNumber\",R,C,V_fabricID"
- "T@\"NSNumber\",R,C,V_ownerNode"
- "T@\"NSUUID\",&,V_pairingTargetHomeUUID"
- "T@\"NSUUID\",R,V_targetFabricUUID"
- "TB,N,V_cachedDeviceControllerShouldResume"
- "TB,N,V_caseAuthenticatedTagsUpdated"
- "TB,N,V_startSuspended"
- "TB,V_preWarmTargetIsSystemCommissionerFabric"
- "TB,V_userOwnsConfiguredPreWarmTargetFabric"
- "Yes"
- "_abortAllOperationsForFabricID:reason:"
- "_baseDevice"
- "_baseDoorLock"
- "_cachedDeviceControllerShouldResume"
- "_cachedOperationalCertificateIfValidForFabricID:"
- "_cachedRootCertificateIfValidForFabricID:"
- "_caseAuthenticatedTagsUpdated"
- "_certificateIssuerID"
- "_clearNewFabricData"
- "_configuredPreWarmTargetFabricID"
- "_connectPendingFabricConnectionsForFabricID:"
- "_createFabricKeyPairsIfAbsent"
- "_createNewFabricData"
- "_createOperationalCertificateForFabricID:rootCert:caseAuthenticatedTags:controllerNodeID:"
- "_createOperationalKeyPairIfAbsent"
- "_currentFabricID"
- "_currentHomeFabricDeviceControllerStartupParams"
- "_currentHomeFabricDeviceControllerStartupParams1"
- "_currentHomeFabricDeviceControllerStartupParams2"
- "_fabricIDOfActiveThreadNetwork"
- "_fabricIDOfPendingStartPairingBlock"
- "_fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:"
- "_getDataToPersist"
- "_getUserAtIndex:includeAliroCredentials:flow:"
- "_handleClientsRemovedWithFabricID:updateConnectionIdleTimeout:reason:"
- "_isDeviceIDPaired:nodeID:fabricID:"
- "_isNodeIDPaired:fabricID:"
- "_loadFabricKeyPairs"
- "_loadForPairingWithFetchFromResident:completion:"
- "_loadFromDiskWithCompletion:"
- "_loadFromRemoteWithCompletion:"
- "_loadFromResidentWithCompletion:"
- "_loadFromStorageWithCompletion:"
- "_notifyThreadRadioStateChanged:nodeType:fabricID:"
- "_operationalCertificateFromSdkCertificatesForFabricID:"
- "_ownerLocalOperationalKeyPair"
- "_ownerNode"
- "_pairingTargetHomeUUID"
- "_preWarmTargetIsSystemCommissionerFabric"
- "_preWarmedFabricID"
- "_prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:"
- "_rootCertificateFromSdkCertificatesForFabricID:"
- "_setupAndPersistStorageStateForHomeFabricID:completion:"
- "_setupStorageStateAfterCertFetchForHomeFabricID:completion:"
- "_setupStorageStateForHomeFabricID:"
- "_setupStorageStateForUpdatedHomeFabricID:"
- "_setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:"
- "_setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:overrideAccessoryControlAllowed:"
- "_setupStorageStateIfNotFabricID:rediscoverAccessories:"
- "_startSuspended"
- "_startThreadRadioForHomeWithFabricID:preventDisconnect:"
- "_startThreadRadioForSystemCommissionerFabricID:"
- "_stopSystemCommissionerFabricID:reason:"
- "_stopThreadRadioForHomeWithFabricID:"
- "_stopThreadRadioForSystemCommissionerFabricID:"
- "_suspendOperationsForFabricID:"
- "_targetFabricUUID"
- "_updateFabricIDOfActiveThreadNetwork:isFabricIDOfSystemCommissioner:"
- "_userOwnsConfiguredPreWarmTargetFabric"
- "accessoryServerBrowser:cacheOperationalCertData:forFabricID:"
- "accessoryServerBrowser:getCachedOperationalCertificateDataForFabricID:completion:"
- "addFabricWithActiveClientForFabricID:"
- "appleGetAliroCredentialStatusWithParams:completion:"
- "appleHomeFabricRootPublicKey"
- "appleHomeFabricWithID:"
- "appleHomeFabricWithUUID:"
- "appleSetAliroCredentialWithParams:completion:"
- "appleSetAliroReaderConfigWithParams:completion:"
- "areCachedCertificatesValidForFabricID:"
- "baseDevice"
- "baseDoorLock"
- "cacheOperationalCertificate:fabricID:"
- "cachedDeviceControllerShouldResume"
- "caseAuthenticatedTagsUpdated"
- "certificateIssuerID"
- "clearCredentialWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "clearPreWarmTarget"
- "colorFromAttributeResponse:"
- "configureControllerForFabric:"
- "configuredPreWarmTargetFabricID"
- "connectToAccessoryWithExtendedMACAddress:withFabricID:completion:"
- "createMatterOperationalKeyPairIfAbsentWithCompletion:"
- "createNewFabricDataForFabric:completion:"
- "createNewFabricDataForFabricID:completion:"
- "createNewFabricIDWithCompletion:"
- "createNewFabricIdentityWithCompletion:"
- "current device"
- "currentDeviceControllerNodeID"
- "currentFabricID"
- "deRegisterFromSleepWake:"
- "fabricIDOfActiveThreadNetwork"
- "fabricIDOfPendingStartPairingBlock"
- "fetchCachedOperationalCertificateForFabricID:completionHandler:"
- "fetchCertForFabricWithID:isOwner:forPairing:forceFetchFromResident:completion:"
- "fetchCertificatesForMatterNodeWithCommissionerNodeID:commissioneeNodeID:forOwner:publicKey:fabricID:completionHandler:"
- "fetchCertificatesFromStorageForFabricID:controllerNodeID:rootCert:operationalCert:residentNodeID:ipk:"
- "fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:rootCertificate:completionHandler:"
- "fetchCommissioningCertificatesForSharedAdminWithDeviceNodeID:forOwner:publicKey:fabricID:completionHandler:"
- "fetchOperationalCertificatesForNewFabricWithFabricID:publicKey:fetchFromResident:completion:"
- "findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:"
- "getAllAppleAliroCredentialsForUser:flow:"
- "getAppleAliroCredentialsForUser:withCredentialType:startingAtIndex:credentials:flow:"
- "getBaseDevice:queue:completionHandler:"
- "getCredentialStatusWithParams:completion:"
- "getNOCFromResidentForSharedUserForFabric:"
- "getThreadNetworkConnectionStateWithFabricID:"
- "getThreadNetworkNodeTypeWithFabricID:"
- "getUserWithParams:completion:"
- "getUserWithParams:includeAliroCredentials:flow:completion:"
- "handleEventReportForNotification:"
- "handlePairingCompletionForAccessoryWithNodeID:fabricID:vendorID:productID:configNumber:category:topology:"
- "handlePairingForThreadAccessoryWithFabricID:nodeID:"
- "handleStartUpWithEventNumber:"
- "hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:server:"
- "hasMatterThreadAccessoryInHomeWithFabricID:"
- "hmmtr.feature.PerControllerStorageAPIEnabled"
- "initWithBaseDoorLock:baseDevice:queue:"
- "initWithDevice:baseDevice:endpoint:queue:accessoryServer:"
- "initWithFabricID:rootCert:operationalCert:ownerNode:ipk:"
- "initWithIdentifier:categoryNumber:"
- "initWithQueue:browser:fabricID:systemCommissionerFabric:"
- "initWithQueue:rootCertificate:browser:"
- "initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:"
- "ipkForFabricID:forPairing:"
- "isCurrentDeviceMobileAndResidentReachableAndThreadCapableForFabric:"
- "isFirmwareUpdateInProgressForFabricID:"
- "isHAPError"
- "isPrimaryResidentNodeReachableAndThreadCapable"
- "isRVCEnabled"
- "isSuspended"
- "isValid"
- "knownFabricWithID:"
- "legacyNodeIDForFabricID:"
- "loadFabricAndControllerDataForPairing:fetchFromResident:completion:"
- "locallyStoredFabricDataWithError:"
- "maxCoolSetpointNumber"
- "maxHeatSetpointNumber"
- "minCoolSetpointNumber"
- "minHeatSetpointNumber"
- "nodeIDForFabricID:deviceIdentifier:"
- "notifyThreadRadioStateChanged:nodeType:fabricID:"
- "operationalCertForCurrentFabric"
- "overrideCurrentFabricID:"
- "overrideLocationCheckForPairingForFabricID:"
- "ownerLocalOperationalKeyPair"
- "ownerNode"
- "pairingTargetHomeUUID"
- "persistLegacyControllerNodeWithDictionary:"
- "preWarmTargetIsSystemCommissionerFabric"
- "preWarmedFabricID"
- "prepareForPairingWithSetupPayload:fabric:targetFabricUUID:fabricID:owner:ownerCertFetchSupported:completionHandler:"
- "prepareStorageForFabricID:"
- "prepareStorageForFabricID:forInitialSetup:"
- "productFinishFromAttributeResponse:"
- "readAttributeAliroGroupResolvingKeyWithCompletion:"
- "readAttributeAliroReaderGroupIdentifierWithCompletion:"
- "readAttributeAliroReaderGroupSubIdentifierWithCompletion:"
- "readAttributeAliroReaderVerificationKeyWithCompletion:"
- "readAttributeAppleAliroGroupResolvingKeyWithCompletion:"
- "readAttributeAppleAliroReaderGroupIdentifierWithCompletion:"
- "readAttributeAppleAliroReaderVerificationKeyWithCompletion:"
- "readAttributeWithEndpointIDAndCompletion:clusterID:attributeID:completion:"
- "reload"
- "removeActiveClientWithFabricID:updateConnectionIdleTimeout:reason:"
- "removeActiveSecondaryClientWithFabricID:updateConnectionIdleTimeout:reason:"
- "resident"
- "setAliroReaderConfigWithParams:completion:"
- "setBaseDevice:"
- "setBaseDoorLock:"
- "setCachedDeviceControllerShouldResume:"
- "setCaseAuthenticatedTagsUpdated:"
- "setCertificateIssuerID:"
- "setConfiguredPreWarmTargetFabricID:"
- "setCredentialWithParams:completion:"
- "setCurrentFabricID:"
- "setFabricIDOfActiveThreadNetwork:"
- "setFabricIDOfPendingStartPairingBlock:"
- "setNocSigner:"
- "setOperationalKeyPair:"
- "setOwnerLocalOperationalKeyPair:"
- "setPairingTargetHomeUUID:"
- "setPreWarmTargetIsSystemCommissionerFabric:"
- "setPreWarmTargetToFabricWithID:isOwner:"
- "setPreWarmTargetToSystemCommissionerFabric"
- "setPreWarmedFabricID:"
- "setStartSuspended:"
- "setUserOwnsConfiguredPreWarmTargetFabric:"
- "setUserWithParams:completion:"
- "setUserWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "setupStorageStateAfterCertFetchForHomeFabricID:completion:"
- "setupStorageStateAndRediscoverAccessoriesForHomeFabricID:"
- "setupStorageStateForHomeFabricID:"
- "setupStorageStateForHomeFabricID:completion:"
- "setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricID:"
- "shared"
- "startAccessoryFirmwareUpdateWithExtendedMACAddress:fabricID:isWedDevice:completion:"
- "startAccessoryPairingWithExtendedMACAddress:fabricID:isWedDevice:completion:"
- "startSuspended"
- "startThreadRadioForHomeWithFabricID:"
- "startThreadRadioForHomeWithFabricID:preventDisconnect:"
- "startThreadRadioForSystemCommissionerFabricID:"
- "stopAccessoryFirmwareUpdateWithFabricID:completion:"
- "stopAccessoryPairingWithFabricID:completion:"
- "stopThreadRadioForHomeWithFabricID:"
- "stopThreadRadioForSystemCommissionerFabricID:"
- "storageDataSourceForFabricWithID:"
- "suspendOperationsForFabricID:"
- "updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:"
- "userOwnsConfiguredPreWarmTargetFabric"
- "v16@?0@\"HMMTRCachedFabricCertificateData\"8"
- "v24@?0@\"MTRBaseDevice\"8@\"NSError\"16"
- "v28@?0@\"NSNumber\"8B16@\"NSError\"20"
- "v32@0:8@\"HMMTRCachedFabricCertificateData\"16@\"NSNumber\"24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"HMMTRCachedFabricCertificateData\">24"
- "v32@0:8B16B20@?24"
- "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"HMMTRCachedFabricCertificateData\"24@\"NSNumber\"32"
- "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"NSNumber\"24@?<v@?@\"HMMTRCachedFabricCertificateData\">32"
- "v40@?0@\"NSData\"8@\"NSData\"16@\"NSNumber\"24@\"NSData\"32"
- "v44@0:8@16B24B28B32@?36"
- "v60@0:8@16@24@32B40@44@?52"
- "v60@0:8@16@24B32@36@44@?52"
- "v64@0:8@16@24@32@40B48B52@?56"
- "v64@0:8@16@24@32^{__SecKey=}40@48@56"
- "v64@0:8@16@24^@32^@40^@48^@56"
- "v80@0:8@16@24@32@40^{__SecKey=}48@56@64@72"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"NSData\"8"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"NSDictionary\"8"
- "\xf01a"
- "\xf0b\xc2\xf0\xf0\xc1"

```
