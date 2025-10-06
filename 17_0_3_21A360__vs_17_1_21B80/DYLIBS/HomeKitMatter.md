## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1054.1.7.1.4
-  __TEXT.__text: 0xb70f0
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x52f0
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x15c0
-  __TEXT.__cstring: 0x3adc
-  __TEXT.__oslogstring: 0x16eff
-  __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x1acc
-  __TEXT.__objc_classname: 0x9da
-  __TEXT.__objc_methname: 0x15bec
-  __TEXT.__objc_methtype: 0x1eae
-  __TEXT.__objc_stubs: 0xe0a0
+1076.2.8.1.1
+  __TEXT.__text: 0xc3178
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x5bd0
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0x1004
+  __TEXT.__cstring: 0x3e5c
+  __TEXT.__oslogstring: 0x18a71
+  __TEXT.__ustring: 0x68
+  __TEXT.__unwind_info: 0x1c00
+  __TEXT.__objc_classname: 0xa9c
+  __TEXT.__objc_methname: 0x177be
+  __TEXT.__objc_methtype: 0x21a0
+  __TEXT.__objc_stubs: 0xefe0
   __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x3270
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__const: 0x33c8
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7068
-  __DATA_CONST.__objc_selrefs: 0x40f0
+  __DATA_CONST.__objc_const: 0x7b98
+  __DATA_CONST.__objc_selrefs: 0x45c8
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x1f80
-  __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__objc_intobj: 0xcc0
+  __AUTH_CONST.__cfstring: 0x44a0
+  __AUTH_CONST.__objc_const: 0x2250
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH.__objc_data: 0x1090
-  __DATA.__objc_classrefs: 0x638
-  __DATA.__objc_superrefs: 0x198
-  __DATA.__objc_ivar: 0x594
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH.__objc_data: 0x1270
+  __DATA.__objc_classrefs: 0x680
+  __DATA.__objc_superrefs: 0x1d8
+  __DATA.__objc_ivar: 0x65c
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0x1d0
+  __DATA.__bss: 0x250
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F7D5B84-ACEF-3C25-ADCC-CA108EF6F1A3
-  Functions: 2417
-  Symbols:   8634
-  CStrings:  5684
+  UUID: 12F5E985-4507-38C6-B6B6-FECD8C7E529B
+  Functions: 2641
+  Symbols:   9302
+  CStrings:  6174
 
Symbols:
+ +[HMMTRAttributeTimer logCategory]
+ +[HMMTRControllerFactory factoryParamsWithNoStorage]
+ +[HMMTRControllerFactory logCategory]
+ +[HMMTRControllerWrapper logCategory]
+ +[HMMTRControllerWrapper shortDescription]
+ +[HMMTRFabricControllerStore logCategory]
+ +[HMMTRFabricControllerStore startupParams:isEquivalentTo:]
+ +[HMMTRSystemCommissionerControllerParams logCategory]
+ +[HMMTRTLVParser keyPairDataFromTLV:]
+ +[HMMTRTLVParser logCategory]
+ +[HMMTRUtilities mtrAuthModeAsString:]
+ +[HMMTRUtilities mtrPrivilegeAsString:]
+ +[HMMTRUtilities printAccessControlList:]
+ +[HMMTRUtilities sanitizeHAPName:]
+ -[HMMTRAccessoryServer _restoreCommissioneeInfoBeforeNextPairingAttempt]
+ -[HMMTRAccessoryServer _updateAttributeTimer:report:timeout:server:]
+ -[HMMTRAccessoryServer attributeTimers]
+ -[HMMTRAccessoryServer colorControlCluster]
+ -[HMMTRAccessoryServer controllerRevokeHandlerRegistered]
+ -[HMMTRAccessoryServer controllerWrapper]
+ -[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]
+ -[HMMTRAccessoryServer fetchColorControlCluster:]
+ -[HMMTRAccessoryServer initialMTRDeviceStateTimeoutId]
+ -[HMMTRAccessoryServer isPairedInStorage]
+ -[HMMTRAccessoryServer originalPairingAttemptOperationalCert]
+ -[HMMTRAccessoryServer originalPairingAttemptRootCert]
+ -[HMMTRAccessoryServer processAttributeReport:]
+ -[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]
+ -[HMMTRAccessoryServer setAttributeTimers:]
+ -[HMMTRAccessoryServer setColorControlCluster:]
+ -[HMMTRAccessoryServer setControllerRevokeHandlerRegistered:]
+ -[HMMTRAccessoryServer setControllerWrapper:]
+ -[HMMTRAccessoryServer setInitialMTRDeviceStateTimeoutId:]
+ -[HMMTRAccessoryServer setOriginalPairingAttemptOperationalCert:]
+ -[HMMTRAccessoryServer setOriginalPairingAttemptRootCert:]
+ -[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]
+ -[HMMTRAccessoryServerBrowser _accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:]
+ -[HMMTRAccessoryServerBrowser _currentHomeFabricDeviceControllerStartupParams]
+ -[HMMTRAccessoryServerBrowser _currentHomeFabricDeviceController]
+ -[HMMTRAccessoryServerBrowser _isDeviceIDPaired:nodeID:fabricID:]
+ -[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]
+ -[HMMTRAccessoryServerBrowser _setupAndPersistStorageStateForHomeFabricID:completion:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateAfterCertFetchForHomeFabricID:completion:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForHomeFabricID:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricID:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:]
+ -[HMMTRAccessoryServerBrowser _setupStorageStateIfNotFabricID:rediscoverAccessories:]
+ -[HMMTRAccessoryServerBrowser accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:]
+ -[HMMTRAccessoryServerBrowser configure]
+ -[HMMTRAccessoryServerBrowser controllerFactoryEnablePerPrimaryResidentConfirmationToken]
+ -[HMMTRAccessoryServerBrowser controllerFactory]
+ -[HMMTRAccessoryServerBrowser currentHomeFabricDeviceControllerWrapper]
+ -[HMMTRAccessoryServerBrowser dealloc]
+ -[HMMTRAccessoryServerBrowser fetchCertificatesForSharedUserWithAccessoryNodeID:sharedUserType:publicKey:fabricID:completionHandler:]
+ -[HMMTRAccessoryServerBrowser fetchSystemCommissionerRootCertificateWithCompletion:]
+ -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricID:]
+ -[HMMTRAccessoryServerBrowser hasOperationalCerts]
+ -[HMMTRAccessoryServerBrowser homeFabricControllers]
+ -[HMMTRAccessoryServerBrowser homeKeychainReadyNotificationToken]
+ -[HMMTRAccessoryServerBrowser isOwnerForHomeWithFabricID:]
+ -[HMMTRAccessoryServerBrowser mtsKeychainReadyNotificationToken]
+ -[HMMTRAccessoryServerBrowser setControllerFactoryEnablePerPrimaryResidentConfirmationToken:]
+ -[HMMTRAccessoryServerBrowser setHasOperationalCerts:]
+ -[HMMTRAccessoryServerBrowser setHomeKeychainReadyNotificationToken:]
+ -[HMMTRAccessoryServerBrowser setMtsKeychainReadyNotificationToken:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateAfterCertFetchForHomeFabricID:completion:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricID:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricID:]
+ -[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricID:]
+ -[HMMTRAccessoryServerBrowser systemCommissionerControllerParams]
+ -[HMMTRAccessoryServerBrowser systemCommissionerControllerWrapper]
+ -[HMMTRAttributeTimer .cxx_destruct]
+ -[HMMTRAttributeTimer attributeTimer]
+ -[HMMTRAttributeTimer initWithServer:report:timeout:queue:server:]
+ -[HMMTRAttributeTimer path]
+ -[HMMTRAttributeTimer report]
+ -[HMMTRAttributeTimer server]
+ -[HMMTRAttributeTimer setAttributeTimer:]
+ -[HMMTRAttributeTimer setReport:]
+ -[HMMTRAttributeTimer start]
+ -[HMMTRAttributeTimer stop]
+ -[HMMTRAttributeTimer timerDidFire:]
+ -[HMMTRAttributeTimer updateReport:]
+ -[HMMTRColorControl initWithDevice:endpointID:queue:]
+ -[HMMTRColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]
+ -[HMMTRColorControl(Test) initWithQueue:]
+ -[HMMTRControllerFactory .cxx_destruct]
+ -[HMMTRControllerFactory _createControllerForGetter:]
+ -[HMMTRControllerFactory _createControllerWithStartupParams:]
+ -[HMMTRControllerFactory _removeGetter:]
+ -[HMMTRControllerFactory _restartMatterControllerFactory]
+ -[HMMTRControllerFactory _revokeAvailable:]
+ -[HMMTRControllerFactory _setEnabled:]
+ -[HMMTRControllerFactory controllerWrappers]
+ -[HMMTRControllerFactory disableNormalOperation]
+ -[HMMTRControllerFactory disablingTokens]
+ -[HMMTRControllerFactory enableNormalOperationWithToken:]
+ -[HMMTRControllerFactory enabled]
+ -[HMMTRControllerFactory factoryOperationEnabled]
+ -[HMMTRControllerFactory factoryParams]
+ -[HMMTRControllerFactory initWithWorkQueue:factoryParams:]
+ -[HMMTRControllerFactory matterFactoryRunning]
+ -[HMMTRControllerFactory setFactoryOperationEnabled:]
+ -[HMMTRControllerFactory setMatterFactoryRunning:]
+ -[HMMTRControllerFactory sharedDeviceControllerFactory]
+ -[HMMTRControllerFactory stackStorageWithStartupParams:operationalKeyPairTLV:]
+ -[HMMTRControllerFactory storage]
+ -[HMMTRControllerFactory workQueue]
+ -[HMMTRControllerFactory wrapperWithName:startupParams:]
+ -[HMMTRControllerFactoryStorage .cxx_destruct]
+ -[HMMTRControllerFactoryStorage clear]
+ -[HMMTRControllerFactoryStorage dictionaryCopy]
+ -[HMMTRControllerFactoryStorage init]
+ -[HMMTRControllerFactoryStorage mtrControllerFactoryKeyValueStore]
+ -[HMMTRControllerFactoryStorage removeStorageDataForKey:]
+ -[HMMTRControllerFactoryStorage setStorageData:forKey:]
+ -[HMMTRControllerFactoryStorage storageDataForKey:]
+ -[HMMTRControllerFactoryStorage workQueue]
+ -[HMMTRControllerWrapper .cxx_destruct]
+ -[HMMTRControllerWrapper _revokeAvailable:]
+ -[HMMTRControllerWrapper attributeDescriptions]
+ -[HMMTRControllerWrapper cachedDeviceController]
+ -[HMMTRControllerWrapper controller]
+ -[HMMTRControllerWrapper factory]
+ -[HMMTRControllerWrapper initWithWorkQueue:factory:startupParams:name:]
+ -[HMMTRControllerWrapper logIdentifier]
+ -[HMMTRControllerWrapper name]
+ -[HMMTRControllerWrapper privateDescription]
+ -[HMMTRControllerWrapper registerRevokeHandlerWithQueue:handler:]
+ -[HMMTRControllerWrapper remove]
+ -[HMMTRControllerWrapper replaceStartupParams:]
+ -[HMMTRControllerWrapper revokeHandlers]
+ -[HMMTRControllerWrapper setCachedDeviceController:]
+ -[HMMTRControllerWrapper setFactory:]
+ -[HMMTRControllerWrapper shutdown]
+ -[HMMTRControllerWrapper startupParams]
+ -[HMMTRControllerWrapper workQueue]
+ -[HMMTRControllerWrapperRevokeHandlerInfo .cxx_destruct]
+ -[HMMTRControllerWrapperRevokeHandlerInfo handler]
+ -[HMMTRControllerWrapperRevokeHandlerInfo initWithHandler:queue:]
+ -[HMMTRControllerWrapperRevokeHandlerInfo queue]
+ -[HMMTRDescriptorClusterManager _querySupportedAttributesFromClusterAtCHIPEndpoint:device:callbackQueue:clusterClassName:completionHandler:]
+ -[HMMTRDescriptorClusterManager _verifyHAPOptionalCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForAttributes:hapServicesToCheckForOptionalMatterAttribute:clusterAttributesSupported:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]
+ -[HMMTRDescriptorClusterManager hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:server:]
+ -[HMMTRFabricControllerStore .cxx_destruct]
+ -[HMMTRFabricControllerStore _auditControllerWrappersWithAllFabricIDs:]
+ -[HMMTRFabricControllerStore controllerFactory]
+ -[HMMTRFabricControllerStore controllerWrappers]
+ -[HMMTRFabricControllerStore initWithQueue:controllerFactory:]
+ -[HMMTRFabricControllerStore removeAllGetters]
+ -[HMMTRFabricControllerStore workQueue]
+ -[HMMTRFabricControllerStore wrapperWithFabricID:startupParams:allFabricIDs:]
+ -[HMMTRFirmwareUpdateStatus otaProviderState]
+ -[HMMTRMatterKeypair _reloadWithDictionary:]
+ -[HMMTRMatterKeypair archiveV1KeyItemValue]
+ -[HMMTRMatterKeypair createPrivateKeyWithData:]
+ -[HMMTRMatterKeypair initUnassociated]
+ -[HMMTRMatterKeypair initWithPrivateKey:]
+ -[HMMTRMatterKeypair initWithTLVData:]
+ -[HMMTRMatterKeypair initWithV0Account:]
+ -[HMMTRMatterKeypair initWithV0Account:privateKey:]
+ -[HMMTRMatterKeypair initWithV1Account:]
+ -[HMMTRMatterKeypair initWithV1Account:privateKey:operationalKey:rootCert:operationalCert:ipk:]
+ -[HMMTRMatterKeypair initializeAllowingNew:]
+ -[HMMTRMatterKeypair ipk]
+ -[HMMTRMatterKeypair keyRepr]
+ -[HMMTRMatterKeypair opKeyRepr]
+ -[HMMTRMatterKeypair operationalCert]
+ -[HMMTRMatterKeypair operationalKey]
+ -[HMMTRMatterKeypair rootCert]
+ -[HMMTRMatterKeypair setKeyRepr:]
+ -[HMMTRMatterKeypair setOpKeyRepr:]
+ -[HMMTRMatterKeypair setOperationalKey:]
+ -[HMMTRMatterKeypair unarchiveV1KeyItemValue:]
+ -[HMMTRMatterKeypair version]
+ -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:]
+ -[HMMTRProtocolMap isRequiresOptionalMatterAttributeForCharacteristic:]
+ -[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]
+ -[HMMTRProtocolOperationManager handleSpecialCaseCharacteristicWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]
+ -[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]
+ -[HMMTRStorage fetchSharedUserCertForFabricWithID:completion:]
+ -[HMMTRStorage(Records) removeRecordsForNode:systemCommissionerFabric:]
+ -[HMMTRStorage(Records) removeRecordsForNodeIDs:systemCommissionerFabric:]
+ -[HMMTRSystemCommissionerControllerParams .cxx_destruct]
+ -[HMMTRSystemCommissionerControllerParams _buildV1KeyFromScratch]
+ -[HMMTRSystemCommissionerControllerParams _buildV1KeyFromV0KeyAllowingNew:]
+ -[HMMTRSystemCommissionerControllerParams _buildV1KeyWithPrivateKey:operationalKey:ipk:rootCert:operationalCert:updatingMTSKeyValueStore:]
+ -[HMMTRSystemCommissionerControllerParams _buildV1KeyWithV0KeyPair:]
+ -[HMMTRSystemCommissionerControllerParams _findFabricRecordInMTSKeyValueStoreMatchingKeyPair:ipk:rootCert:operationalKey:operationalCert:]
+ -[HMMTRSystemCommissionerControllerParams _handleKeychainDataChanged]
+ -[HMMTRSystemCommissionerControllerParams _obtainControllerWrapperWithV1KeyPair:startupParams:]
+ -[HMMTRSystemCommissionerControllerParams _startWithV1Keypair:]
+ -[HMMTRSystemCommissionerControllerParams _updateMTSKeyValueStore:]
+ -[HMMTRSystemCommissionerControllerParams adminNodeID]
+ -[HMMTRSystemCommissionerControllerParams commissioneeNodeID]
+ -[HMMTRSystemCommissionerControllerParams commissioningFabricID]
+ -[HMMTRSystemCommissionerControllerParams controllerFactory]
+ -[HMMTRSystemCommissionerControllerParams controllerWrapper]
+ -[HMMTRSystemCommissionerControllerParams fetchControllerParamsAllowingNew:nocSigner:controllerWrapper:]
+ -[HMMTRSystemCommissionerControllerParams generatingKeyPair]
+ -[HMMTRSystemCommissionerControllerParams handleKeyPairDataChanged]
+ -[HMMTRSystemCommissionerControllerParams initWithQueue:controllerFactory:]
+ -[HMMTRSystemCommissionerControllerParams issueOperationalCertificateForRequest:attestationInfo:controller:completion:]
+ -[HMMTRSystemCommissionerControllerParams mtsKeyValueStore]
+ -[HMMTRSystemCommissionerControllerParams setAdminNodeID:]
+ -[HMMTRSystemCommissionerControllerParams setCommissioneeNodeID:]
+ -[HMMTRSystemCommissionerControllerParams setCommissioningFabricID:]
+ -[HMMTRSystemCommissionerControllerParams setControllerWrapper:]
+ -[HMMTRSystemCommissionerControllerParams setGeneratingKeyPair:]
+ -[HMMTRSystemCommissionerControllerParams setV1keypair:]
+ -[HMMTRSystemCommissionerControllerParams shouldSkipAttestationCertificateValidation]
+ -[HMMTRSystemCommissionerControllerParams storeV0MatterKeypairWithPrivateKey:]
+ -[HMMTRSystemCommissionerControllerParams storeV0MatterKeypair]
+ -[HMMTRSystemCommissionerControllerParams storeV1MatterKeypairWithPrivateKey:operationalKey:rootCert:operationalCert:ipk:]
+ -[HMMTRSystemCommissionerControllerParams v0MatterKeypairFromKeychain]
+ -[HMMTRSystemCommissionerControllerParams v1KeypairIsEquivalentTo:]
+ -[HMMTRSystemCommissionerControllerParams v1MatterKeypairFromKeychain]
+ -[HMMTRSystemCommissionerControllerParams v1keypair]
+ -[HMMTRSystemCommissionerControllerParams workQueue]
+ GCC_except_table1026
+ GCC_except_table1048
+ GCC_except_table1074
+ GCC_except_table1091
+ GCC_except_table1135
+ GCC_except_table1295
+ GCC_except_table1299
+ GCC_except_table1322
+ GCC_except_table1405
+ GCC_except_table1429
+ GCC_except_table1431
+ GCC_except_table1435
+ GCC_except_table1453
+ GCC_except_table1467
+ GCC_except_table1473
+ GCC_except_table1482
+ GCC_except_table1484
+ GCC_except_table1491
+ GCC_except_table1507
+ GCC_except_table1513
+ GCC_except_table1520
+ GCC_except_table1832
+ GCC_except_table1837
+ GCC_except_table1840
+ GCC_except_table1895
+ GCC_except_table1911
+ GCC_except_table1919
+ GCC_except_table1933
+ GCC_except_table1934
+ GCC_except_table1965
+ GCC_except_table2003
+ GCC_except_table2035
+ GCC_except_table2039
+ GCC_except_table2055
+ GCC_except_table2056
+ GCC_except_table2080
+ GCC_except_table2128
+ GCC_except_table2164
+ GCC_except_table2172
+ GCC_except_table2187
+ GCC_except_table2206
+ GCC_except_table2221
+ GCC_except_table2222
+ GCC_except_table2227
+ GCC_except_table2235
+ GCC_except_table2343
+ GCC_except_table2348
+ GCC_except_table2442
+ GCC_except_table2445
+ GCC_except_table2564
+ GCC_except_table2568
+ GCC_except_table2571
+ GCC_except_table2594
+ GCC_except_table2615
+ GCC_except_table418
+ GCC_except_table420
+ GCC_except_table469
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table534
+ GCC_except_table565
+ GCC_except_table581
+ GCC_except_table626
+ GCC_except_table634
+ GCC_except_table659
+ GCC_except_table689
+ _OBJC_CLASS_$_HMMTRAttributeTimer
+ _OBJC_CLASS_$_HMMTRControllerFactory
+ _OBJC_CLASS_$_HMMTRControllerFactoryStorage
+ _OBJC_CLASS_$_HMMTRControllerWrapper
+ _OBJC_CLASS_$_HMMTRControllerWrapperRevokeHandlerInfo
+ _OBJC_CLASS_$_HMMTRFabricControllerStore
+ _OBJC_CLASS_$_HMMTRSystemCommissionerControllerParams
+ _OBJC_CLASS_$_MTRDeviceControllerFactory
+ _OBJC_CLASS_$_MTRDeviceControllerFactoryParams
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_IVAR_$_HMMTRAccessoryServer._attributeTimers
+ _OBJC_IVAR_$_HMMTRAccessoryServer._colorControlCluster
+ _OBJC_IVAR_$_HMMTRAccessoryServer._controllerRevokeHandlerRegistered
+ _OBJC_IVAR_$_HMMTRAccessoryServer._controllerWrapper
+ _OBJC_IVAR_$_HMMTRAccessoryServer._initialMTRDeviceStateTimeoutId
+ _OBJC_IVAR_$_HMMTRAccessoryServer._originalPairingAttemptOperationalCert
+ _OBJC_IVAR_$_HMMTRAccessoryServer._originalPairingAttemptRootCert
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._controllerFactory
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._controllerFactoryEnablePerPrimaryResidentConfirmationToken
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._hasOperationalCerts
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._homeFabricControllers
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._homeKeychainReadyNotificationToken
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._mtsKeychainReadyNotificationToken
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._systemCommissionerControllerParams
+ _OBJC_IVAR_$_HMMTRAttributeTimer._attributeTimer
+ _OBJC_IVAR_$_HMMTRAttributeTimer._path
+ _OBJC_IVAR_$_HMMTRAttributeTimer._report
+ _OBJC_IVAR_$_HMMTRAttributeTimer._server
+ _OBJC_IVAR_$_HMMTRControllerFactory._controllerWrappers
+ _OBJC_IVAR_$_HMMTRControllerFactory._disablingTokens
+ _OBJC_IVAR_$_HMMTRControllerFactory._enabled
+ _OBJC_IVAR_$_HMMTRControllerFactory._factoryOperationEnabled
+ _OBJC_IVAR_$_HMMTRControllerFactory._factoryParams
+ _OBJC_IVAR_$_HMMTRControllerFactory._matterFactoryRunning
+ _OBJC_IVAR_$_HMMTRControllerFactory._storage
+ _OBJC_IVAR_$_HMMTRControllerFactory._workQueue
+ _OBJC_IVAR_$_HMMTRControllerFactoryStorage._mtrControllerFactoryKeyValueStore
+ _OBJC_IVAR_$_HMMTRControllerFactoryStorage._workQueue
+ _OBJC_IVAR_$_HMMTRControllerWrapper._cachedDeviceController
+ _OBJC_IVAR_$_HMMTRControllerWrapper._factory
+ _OBJC_IVAR_$_HMMTRControllerWrapper._name
+ _OBJC_IVAR_$_HMMTRControllerWrapper._revokeHandlers
+ _OBJC_IVAR_$_HMMTRControllerWrapper._startupParams
+ _OBJC_IVAR_$_HMMTRControllerWrapper._workQueue
+ _OBJC_IVAR_$_HMMTRControllerWrapperRevokeHandlerInfo._handler
+ _OBJC_IVAR_$_HMMTRControllerWrapperRevokeHandlerInfo._queue
+ _OBJC_IVAR_$_HMMTRFabricControllerStore._controllerFactory
+ _OBJC_IVAR_$_HMMTRFabricControllerStore._controllerWrappers
+ _OBJC_IVAR_$_HMMTRFabricControllerStore._workQueue
+ _OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._otaProviderState
+ _OBJC_IVAR_$_HMMTRMatterKeypair._ipk
+ _OBJC_IVAR_$_HMMTRMatterKeypair._keyRepr
+ _OBJC_IVAR_$_HMMTRMatterKeypair._opKeyRepr
+ _OBJC_IVAR_$_HMMTRMatterKeypair._operationalCert
+ _OBJC_IVAR_$_HMMTRMatterKeypair._operationalKey
+ _OBJC_IVAR_$_HMMTRMatterKeypair._rootCert
+ _OBJC_IVAR_$_HMMTRMatterKeypair._version
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._adminNodeID
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._commissioneeNodeID
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._commissioningFabricID
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._controllerFactory
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._controllerWrapper
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._generatingKeyPair
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._v1keypair
+ _OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._workQueue
+ _OBJC_METACLASS_$_HMMTRAttributeTimer
+ _OBJC_METACLASS_$_HMMTRControllerFactory
+ _OBJC_METACLASS_$_HMMTRControllerFactoryStorage
+ _OBJC_METACLASS_$_HMMTRControllerWrapper
+ _OBJC_METACLASS_$_HMMTRControllerWrapperRevokeHandlerInfo
+ _OBJC_METACLASS_$_HMMTRFabricControllerStore
+ _OBJC_METACLASS_$_HMMTRSystemCommissionerControllerParams
+ _ReadIntegerWithContextSpecificTag
+ _ReadOctetStringWithContextSpecificTag
+ __OBJC_$_CLASS_METHODS_HMMTRAttributeTimer
+ __OBJC_$_CLASS_METHODS_HMMTRColorControl(Test)
+ __OBJC_$_CLASS_METHODS_HMMTRControllerFactory
+ __OBJC_$_CLASS_METHODS_HMMTRControllerWrapper
+ __OBJC_$_CLASS_METHODS_HMMTRFabricControllerStore
+ __OBJC_$_CLASS_METHODS_HMMTRSystemCommissionerControllerParams
+ __OBJC_$_INSTANCE_METHODS_HMMTRAttributeTimer
+ __OBJC_$_INSTANCE_METHODS_HMMTRColorControl(Test)
+ __OBJC_$_INSTANCE_METHODS_HMMTRControllerFactory
+ __OBJC_$_INSTANCE_METHODS_HMMTRControllerFactoryStorage
+ __OBJC_$_INSTANCE_METHODS_HMMTRControllerWrapper
+ __OBJC_$_INSTANCE_METHODS_HMMTRControllerWrapperRevokeHandlerInfo
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricControllerStore
+ __OBJC_$_INSTANCE_METHODS_HMMTRSystemCommissionerControllerParams
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAttributeTimer
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRControllerFactory
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRControllerFactoryStorage
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRControllerWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRControllerWrapperRevokeHandlerInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricControllerStore
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRSystemCommissionerControllerParams
+ __OBJC_$_PROP_LIST_HMMTRAttributeTimer
+ __OBJC_$_PROP_LIST_HMMTRControllerFactory
+ __OBJC_$_PROP_LIST_HMMTRControllerFactoryStorage
+ __OBJC_$_PROP_LIST_HMMTRControllerWrapper
+ __OBJC_$_PROP_LIST_HMMTRControllerWrapperRevokeHandlerInfo
+ __OBJC_$_PROP_LIST_HMMTRFabricControllerStore
+ __OBJC_$_PROP_LIST_HMMTRSystemCommissionerControllerParams
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRAttributeTimer
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRControllerFactoryStorage
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSystemCommissionerControllerParams
+ __OBJC_CLASS_RO_$_HMMTRAttributeTimer
+ __OBJC_CLASS_RO_$_HMMTRControllerFactory
+ __OBJC_CLASS_RO_$_HMMTRControllerFactoryStorage
+ __OBJC_CLASS_RO_$_HMMTRControllerWrapper
+ __OBJC_CLASS_RO_$_HMMTRControllerWrapperRevokeHandlerInfo
+ __OBJC_CLASS_RO_$_HMMTRFabricControllerStore
+ __OBJC_CLASS_RO_$_HMMTRSystemCommissionerControllerParams
+ __OBJC_METACLASS_RO_$_HMMTRAttributeTimer
+ __OBJC_METACLASS_RO_$_HMMTRControllerFactory
+ __OBJC_METACLASS_RO_$_HMMTRControllerFactoryStorage
+ __OBJC_METACLASS_RO_$_HMMTRControllerWrapper
+ __OBJC_METACLASS_RO_$_HMMTRControllerWrapperRevokeHandlerInfo
+ __OBJC_METACLASS_RO_$_HMMTRFabricControllerStore
+ __OBJC_METACLASS_RO_$_HMMTRSystemCommissionerControllerParams
+ ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.573
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.689
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.692
+ ___102-[HMMTRAccessoryServerBrowser accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke
+ ___103-[HMMTRAccessoryServerBrowser _accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke
+ ___104-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:endpoint:callbackQueue:completionHandler:]_block_invoke.340
+ ___104-[HMMTRSystemCommissionerControllerParams fetchControllerParamsAllowingNew:nocSigner:controllerWrapper:]_block_invoke
+ ___107-[HMMTRAccessoryServer _writeCharacteristicValues:device:responseTuples:completionQueue:completionHandler:]_block_invoke_4
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.128
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke_2
+ ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke
+ ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.100
+ ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.101
+ ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.102
+ ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke_2
+ ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.173
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.227
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.425
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.426
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.427
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.428
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.431
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.429
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.430
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.126
+ ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.143
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.86
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.88
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.91
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.93
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.94
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.95
+ ___140-[HMMTRDescriptorClusterManager _querySupportedAttributesFromClusterAtCHIPEndpoint:device:callbackQueue:clusterClassName:completionHandler:]_block_invoke
+ ___146-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
+ ___146-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.154
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.155
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.157
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.160
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.162
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.100
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.62
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.73
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.77
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.84
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.88
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.92
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.96
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.154
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.156
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.155
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.120
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.127
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.132
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke_2
+ ___263-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.112
+ ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.101
+ ___29+[HMMTRTLVParser logCategory]_block_invoke
+ ___32-[HMMTRControllerWrapper remove]_block_invoke
+ ___328-[HMMTRDescriptorClusterManager _verifyHAPOptionalCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForAttributes:hapServicesToCheckForOptionalMatterAttribute:clusterAttributesSupported:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke
+ ___33-[HMMTRControllerFactory enabled]_block_invoke
+ ___34+[HMMTRAttributeTimer logCategory]_block_invoke
+ ___34-[HMMTRControllerWrapper shutdown]_block_invoke
+ ___36-[HMMTRControllerWrapper controller]_block_invoke
+ ___37+[HMMTRControllerFactory logCategory]_block_invoke
+ ___37+[HMMTRControllerWrapper logCategory]_block_invoke
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.269
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.273
+ ___38-[HMMTRControllerFactoryStorage clear]_block_invoke
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.518
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.519
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.520
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.521
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.522
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.523
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.524
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.525
+ ___41+[HMMTRFabricControllerStore logCategory]_block_invoke
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.261
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.264
+ ___43-[HMMTRControllerWrapper _revokeAvailable:]_block_invoke
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.673
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.585
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.592
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke_2
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke_3
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.250
+ ___46-[HMMTRFabricControllerStore removeAllGetters]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.729
+ ___47-[HMMTRControllerFactoryStorage dictionaryCopy]_block_invoke
+ ___47-[HMMTRControllerWrapper replaceStartupParams:]_block_invoke
+ ___47-[HMMTRControllerWrapper replaceStartupParams:]_block_invoke.86
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.239
+ ___48-[HMMTRControllerFactory disableNormalOperation]_block_invoke
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.650
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.654
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.653
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.700
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.701
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.702
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.705
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke_2
+ ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.152
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.610
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.613
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.614
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.730
+ ___51-[HMMTRControllerFactoryStorage storageDataForKey:]_block_invoke
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.140
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.141
+ ___54+[HMMTRSystemCommissionerControllerParams logCategory]_block_invoke
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.529
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.534
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.728
+ ___55-[HMMTRControllerFactoryStorage setStorageData:forKey:]_block_invoke
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.368
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.369
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.370
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.371
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.372
+ ___56-[HMMTRControllerFactory wrapperWithName:startupParams:]_block_invoke
+ ___57-[HMMTRControllerFactory enableNormalOperationWithToken:]_block_invoke
+ ___57-[HMMTRControllerFactoryStorage removeStorageDataForKey:]_block_invoke
+ ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.250
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.378
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.379
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.380
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.381
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.382
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.693
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.695
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.697
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.698
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.373
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.374
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.375
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.376
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.377
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.106
+ ___62-[HMMTRStorage fetchSharedUserCertForFabricWithID:completion:]_block_invoke
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.404
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.405
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.406
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.407
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.410
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.387
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.388
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.389
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.391
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.82
+ ___64-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricID:]_block_invoke
+ ___65-[HMMTRAccessoryServerBrowser _isDeviceIDPaired:nodeID:fabricID:]_block_invoke
+ ___65-[HMMTRControllerWrapper registerRevokeHandlerWithQueue:handler:]_block_invoke
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.383
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.384
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.385
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.386
+ ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.280
+ ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.187
+ ___67-[HMMTRSystemCommissionerControllerParams handleKeyPairDataChanged]_block_invoke
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.360
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.366
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.367
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.107
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.110
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.235
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.348
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.353
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.354
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.392
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.393
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.394
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.396
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.398
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.399
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.400
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.401
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.402
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.403
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.605
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.606
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.608
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.607
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.593
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.594
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.601
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.602
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.604
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.595
+ ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.149
+ ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.150
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.659
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.660
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.664
+ ___74-[HMMTRStorage(Records) removeRecordsForNodeIDs:systemCommissionerFabric:]_block_invoke
+ ___75-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricID:]_block_invoke
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.253
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.254
+ ___77-[HMMTRFabricControllerStore wrapperWithFabricID:startupParams:allFabricIDs:]_block_invoke
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.355
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.356
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.357
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.359
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.145
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.147
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.148
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.93
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.95
+ ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.228
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.318
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.320
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.677
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.678
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.679
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.680
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.683
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.684
+ ___84-[HMMTRAccessoryServerBrowser fetchSystemCommissionerRootCertificateWithCompletion:]_block_invoke
+ ___88-[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricID:]_block_invoke
+ ___88-[HMMTRColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]_block_invoke
+ ___89-[HMMTRAccessoryServerBrowser setupStorageStateAfterCertFetchForHomeFabricID:completion:]_block_invoke
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.241
+ ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.343
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.433
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.434
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.435
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.436
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.438
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.437
+ ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.157
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.628
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.101
+ ___95-[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricID:]_block_invoke
+ ___98-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:]_block_invoke.153
+ ___99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke_3
+ ___Block_byref_object_copy_.1458
+ ___Block_byref_object_copy_.1720
+ ___Block_byref_object_copy_.3477
+ ___Block_byref_object_copy_.3778
+ ___Block_byref_object_copy_.4380
+ ___Block_byref_object_copy_.5180
+ ___Block_byref_object_copy_.5710
+ ___Block_byref_object_copy_.6205
+ ___Block_byref_object_copy_.6743
+ ___Block_byref_object_copy_.6933
+ ___Block_byref_object_dispose_.1459
+ ___Block_byref_object_dispose_.1721
+ ___Block_byref_object_dispose_.3478
+ ___Block_byref_object_dispose_.3779
+ ___Block_byref_object_dispose_.4381
+ ___Block_byref_object_dispose_.5181
+ ___Block_byref_object_dispose_.5711
+ ___Block_byref_object_dispose_.6206
+ ___Block_byref_object_dispose_.6744
+ ___Block_byref_object_dispose_.6934
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
+ ___block_descriptor_162_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s152l8s128l8s136l8s144l8
+ ___block_descriptor_32_e28_"NSNumber"16?0"NSString"8l
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32s_e30_v16?0"HMMTRAccessoryServer"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32bs40w_e35_v20?0"HMMTRControllerWrapper"8B16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e18_v16?0"NSNumber"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e48_v24?0"MTRCommissioningParameters"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e35_v24?0"MTRBaseDevice"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?08"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v24?0"MTRBaseDevice"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e60_{_HMFFutureBlockOutcome=q}16?0"HMMTRSyncClusterDoorLock"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r_e40_B16?0"<HMMTRFabricStorageDataSource>"8ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.104.258
+ ___block_literal_global.112
+ ___block_literal_global.1130
+ ___block_literal_global.1274
+ ___block_literal_global.136.3502
+ ___block_literal_global.1375
+ ___block_literal_global.1477
+ ___block_literal_global.161
+ ___block_literal_global.1621
+ ___block_literal_global.1782
+ ___block_literal_global.183
+ ___block_literal_global.1917
+ ___block_literal_global.200
+ ___block_literal_global.2024
+ ___block_literal_global.230
+ ___block_literal_global.264
+ ___block_literal_global.2692
+ ___block_literal_global.2994
+ ___block_literal_global.3075
+ ___block_literal_global.3258
+ ___block_literal_global.3367
+ ___block_literal_global.3604
+ ___block_literal_global.3789
+ ___block_literal_global.404
+ ___block_literal_global.409
+ ___block_literal_global.4106
+ ___block_literal_global.442
+ ___block_literal_global.4420
+ ___block_literal_global.4626
+ ___block_literal_global.5098
+ ___block_literal_global.536
+ ___block_literal_global.5412
+ ___block_literal_global.584
+ ___block_literal_global.588
+ ___block_literal_global.591
+ ___block_literal_global.5920
+ ___block_literal_global.597
+ ___block_literal_global.60
+ ___block_literal_global.6112
+ ___block_literal_global.6238
+ ___block_literal_global.6378
+ ___block_literal_global.639
+ ___block_literal_global.6691
+ ___block_literal_global.743
+ ___block_literal_global.864
+ __unnamed_array_storage.1256
+ __unnamed_array_storage.1610
+ __unnamed_array_storage.335
+ __unnamed_array_storage.4323
+ __unnamed_array_storage.5744
+ _logCategory._hmf_once_t134
+ _logCategory._hmf_once_t2.5097
+ _logCategory._hmf_once_t24
+ _logCategory._hmf_once_t263
+ _logCategory._hmf_once_t3.3257
+ _logCategory._hmf_once_t3.638
+ _logCategory._hmf_once_t38
+ _logCategory._hmf_once_t4.3366
+ _logCategory._hmf_once_t45
+ _logCategory._hmf_once_t501
+ _logCategory._hmf_once_t57
+ _logCategory._hmf_once_t6
+ _logCategory._hmf_once_t78
+ _logCategory._hmf_once_t8.1781
+ _logCategory._hmf_once_t8.6111
+ _logCategory._hmf_once_t90
+ _logCategory._hmf_once_v135
+ _logCategory._hmf_once_v25
+ _logCategory._hmf_once_v264
+ _logCategory._hmf_once_v3.5099
+ _logCategory._hmf_once_v39
+ _logCategory._hmf_once_v4.3259
+ _logCategory._hmf_once_v4.640
+ _logCategory._hmf_once_v46
+ _logCategory._hmf_once_v5.3368
+ _logCategory._hmf_once_v502
+ _logCategory._hmf_once_v58
+ _logCategory._hmf_once_v7
+ _logCategory._hmf_once_v79
+ _logCategory._hmf_once_v9.1783
+ _logCategory._hmf_once_v9.6113
+ _logCategory._hmf_once_v91
+ _notify_cancel
+ _objc_msgSend$OTAProviderState
+ _objc_msgSend$_accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:
+ _objc_msgSend$_auditControllerWrappersWithAllFabricIDs:
+ _objc_msgSend$_buildV1KeyFromScratch
+ _objc_msgSend$_buildV1KeyFromV0KeyAllowingNew:
+ _objc_msgSend$_buildV1KeyWithPrivateKey:operationalKey:ipk:rootCert:operationalCert:updatingMTSKeyValueStore:
+ _objc_msgSend$_buildV1KeyWithV0KeyPair:
+ _objc_msgSend$_createControllerForGetter:
+ _objc_msgSend$_createControllerWithStartupParams:
+ _objc_msgSend$_currentHomeFabricDeviceController
+ _objc_msgSend$_currentHomeFabricDeviceControllerStartupParams
+ _objc_msgSend$_findFabricRecordInMTSKeyValueStoreMatchingKeyPair:ipk:rootCert:operationalKey:operationalCert:
+ _objc_msgSend$_handleKeychainDataChanged
+ _objc_msgSend$_obtainControllerWrapperWithV1KeyPair:startupParams:
+ _objc_msgSend$_prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:
+ _objc_msgSend$_querySupportedAttributesFromClusterAtCHIPEndpoint:device:callbackQueue:clusterClassName:completionHandler:
+ _objc_msgSend$_reloadWithDictionary:
+ _objc_msgSend$_removeGetter:
+ _objc_msgSend$_restartMatterControllerFactory
+ _objc_msgSend$_restoreCommissioneeInfoBeforeNextPairingAttempt
+ _objc_msgSend$_revokeAvailable:
+ _objc_msgSend$_setEnabled:
+ _objc_msgSend$_setupAndPersistStorageStateForHomeFabricID:completion:
+ _objc_msgSend$_setupStorageStateAfterCertFetchForHomeFabricID:completion:
+ _objc_msgSend$_setupStorageStateForHomeFabricID:
+ _objc_msgSend$_setupStorageStateForUpdatedHomeFabricID:
+ _objc_msgSend$_setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:
+ _objc_msgSend$_startWithV1Keypair:
+ _objc_msgSend$_updateAttributeTimer:report:timeout:server:
+ _objc_msgSend$_updateMTSKeyValueStore:
+ _objc_msgSend$_verifyHAPOptionalCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForAttributes:hapServicesToCheckForOptionalMatterAttribute:clusterAttributesSupported:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:
+ _objc_msgSend$accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$adminNodeID
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$archiveV1KeyItemValue
+ _objc_msgSend$attributePathWithEndpointID:clusterID:attributeID:
+ _objc_msgSend$attributeTimer
+ _objc_msgSend$attributeTimers
+ _objc_msgSend$authMode
+ _objc_msgSend$cachedDeviceController
+ _objc_msgSend$certificationDeclarationCertificates
+ _objc_msgSend$clear
+ _objc_msgSend$colorControlCluster
+ _objc_msgSend$colorTemperatureMireds
+ _objc_msgSend$commissioneeNodeID
+ _objc_msgSend$commissioningFabricID
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$controller
+ _objc_msgSend$controllerFactory
+ _objc_msgSend$controllerFactoryEnablePerPrimaryResidentConfirmationToken
+ _objc_msgSend$controllerRevokeHandlerRegistered
+ _objc_msgSend$controllerWrapper
+ _objc_msgSend$controllerWrappers
+ _objc_msgSend$createControllerOnExistingFabric:error:
+ _objc_msgSend$createControllerOnNewFabric:error:
+ _objc_msgSend$createPrivateKeyWithData:
+ _objc_msgSend$currentHomeFabricDeviceControllerWrapper
+ _objc_msgSend$deserialize:
+ _objc_msgSend$device:receivedAttributeReport:
+ _objc_msgSend$disableNormalOperation
+ _objc_msgSend$disablingTokens
+ _objc_msgSend$enableNormalOperationWithToken:
+ _objc_msgSend$factory
+ _objc_msgSend$factoryParams
+ _objc_msgSend$factoryParamsWithNoStorage
+ _objc_msgSend$fetchControllerParamsAllowingNew:nocSigner:controllerWrapper:
+ _objc_msgSend$fetchSystemCommissionerRootCertificateWithCompletion:
+ _objc_msgSend$forAllStorageDataSourcesDo:
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$generatingKeyPair
+ _objc_msgSend$getCHIPAttributesForCharacteristic:
+ _objc_msgSend$handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:
+ _objc_msgSend$handleKeyPairDataChanged
+ _objc_msgSend$handleSpecialCaseCharacteristicWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:
+ _objc_msgSend$handler
+ _objc_msgSend$hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:server:
+ _objc_msgSend$homeFabricControllers
+ _objc_msgSend$initUnassociated
+ _objc_msgSend$initWithHandler:queue:
+ _objc_msgSend$initWithPrivateKey:
+ _objc_msgSend$initWithQueue:controllerFactory:
+ _objc_msgSend$initWithServer:report:timeout:queue:server:
+ _objc_msgSend$initWithTLVData:
+ _objc_msgSend$initWithV0Account:
+ _objc_msgSend$initWithV0Account:privateKey:
+ _objc_msgSend$initWithV1Account:
+ _objc_msgSend$initWithV1Account:privateKey:operationalKey:rootCert:operationalCert:ipk:
+ _objc_msgSend$initWithWorkQueue:factory:startupParams:name:
+ _objc_msgSend$initWithWorkQueue:factoryParams:
+ _objc_msgSend$initialMTRDeviceStateTimeoutId
+ _objc_msgSend$initializeAllowingNew:
+ _objc_msgSend$intermediateCertificate
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isCertificate:equalTo:
+ _objc_msgSend$isOwnerForHomeWithFabricID:
+ _objc_msgSend$isPairedInStorage
+ _objc_msgSend$isRequiresOptionalMatterAttributeForCharacteristic:
+ _objc_msgSend$keyPairDataFromTLV:
+ _objc_msgSend$matterFactoryRunning
+ _objc_msgSend$moveToColorTemperatureWithParams:completion:
+ _objc_msgSend$mtrAuthModeAsString:
+ _objc_msgSend$mtrControllerFactoryKeyValueStore
+ _objc_msgSend$mtrPrivilegeAsString:
+ _objc_msgSend$mtsKeyValueStore
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$operationalCertificateIssuer
+ _objc_msgSend$operationalCertificateIssuerQueue
+ _objc_msgSend$operationalKey
+ _objc_msgSend$operationalKeypair
+ _objc_msgSend$originalPairingAttemptOperationalCert
+ _objc_msgSend$originalPairingAttemptRootCert
+ _objc_msgSend$port
+ _objc_msgSend$printAccessControlList:
+ _objc_msgSend$privateKey
+ _objc_msgSend$privilege
+ _objc_msgSend$processAttributeReport:
+ _objc_msgSend$productAttestationAuthorityCertificates
+ _objc_msgSend$queueAccessoryOperation:highPriority:completion:
+ _objc_msgSend$readAttributeAttributeListWithCompletionHandler:
+ _objc_msgSend$registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:
+ _objc_msgSend$registerRevokeHandlerWithQueue:handler:
+ _objc_msgSend$remove
+ _objc_msgSend$removeAllGetters
+ _objc_msgSend$removeRecordsForNode:systemCommissionerFabric:
+ _objc_msgSend$removeRecordsForNodeIDs:systemCommissionerFabric:
+ _objc_msgSend$replaceStartupParams:
+ _objc_msgSend$revokeHandlers
+ _objc_msgSend$sanitizeHAPName:
+ _objc_msgSend$setAdminNodeID:
+ _objc_msgSend$setCachedDeviceController:
+ _objc_msgSend$setCertificationDeclarationCertificates:
+ _objc_msgSend$setColorControlCluster:
+ _objc_msgSend$setColorTemperatureMireds:
+ _objc_msgSend$setCommissioneeNodeID:
+ _objc_msgSend$setCommissioningFabricID:
+ _objc_msgSend$setControllerFactoryEnablePerPrimaryResidentConfirmationToken:
+ _objc_msgSend$setControllerRevokeHandlerRegistered:
+ _objc_msgSend$setControllerWrapper:
+ _objc_msgSend$setFactory:
+ _objc_msgSend$setGeneratingKeyPair:
+ _objc_msgSend$setInitialMTRDeviceStateTimeoutId:
+ _objc_msgSend$setMatterFactoryRunning:
+ _objc_msgSend$setOriginalPairingAttemptOperationalCert:
+ _objc_msgSend$setOriginalPairingAttemptRootCert:
+ _objc_msgSend$setPort:
+ _objc_msgSend$setProductAttestationAuthorityCertificates:
+ _objc_msgSend$setShouldStartServer:
+ _objc_msgSend$setV1keypair:
+ _objc_msgSend$setupStorageStateAfterCertFetchForHomeFabricID:completion:
+ _objc_msgSend$setupStorageStateForHomeFabricID:
+ _objc_msgSend$sharedDeviceControllerFactory
+ _objc_msgSend$shouldStartServer
+ _objc_msgSend$stackStorageWithStartupParams:operationalKeyPairTLV:
+ _objc_msgSend$startControllerFactory:error:
+ _objc_msgSend$startupParams
+ _objc_msgSend$startupParams:isEquivalentTo:
+ _objc_msgSend$stopControllerFactory
+ _objc_msgSend$storeV0MatterKeypair
+ _objc_msgSend$storeV1MatterKeypairWithPrivateKey:operationalKey:rootCert:operationalCert:ipk:
+ _objc_msgSend$subjects
+ _objc_msgSend$systemCommissionerControllerParams
+ _objc_msgSend$systemCommissionerControllerWrapper
+ _objc_msgSend$unarchiveV1KeyItemValue:
+ _objc_msgSend$unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:
+ _objc_msgSend$updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:
+ _objc_msgSend$updateReport:
+ _objc_msgSend$v0MatterKeypairFromKeychain
+ _objc_msgSend$v1KeypairIsEquivalentTo:
+ _objc_msgSend$v1MatterKeypairFromKeychain
+ _objc_msgSend$v1keypair
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$wrapperWithFabricID:startupParams:allFabricIDs:
+ _objc_msgSend$wrapperWithName:startupParams:
+ _objc_retainAutoreleasedReturnValue
- +[HMMTRSyncClusterColorControl logCategory]
- -[HMMTRAccessoryServer createDoorLockClusterObject]
- -[HMMTRAccessoryServer readPairingWindowStatusAfterStackReadyWithCompletionHandler:]
- -[HMMTRAccessoryServer restrictAccessToNodeIDs:completion:]
- -[HMMTRAccessoryServer setDeviceController:]
- -[HMMTRAccessoryServerBrowser _accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]
- -[HMMTRAccessoryServerBrowser _callMatterStackRestartHandlers]
- -[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]
- -[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:hasPriorSuccessfulPairing:category:completionHandler:]
- -[HMMTRAccessoryServerBrowser _restartMatterStackWithFabricID:]
- -[HMMTRAccessoryServerBrowser _startChipStackWithFabricID:]
- -[HMMTRAccessoryServerBrowser _updateSystemCommissionerFabricIDAndGetIndex]
- -[HMMTRAccessoryServerBrowser accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]
- -[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForSharedAdminWithDeviceNodeID:sharedUserIdentifier:publicKey:fabricID:completionHandler:]
- -[HMMTRAccessoryServerBrowser fetchOrCreateSystemCommissionerRootCertificateWithCompletion:]
- -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:]
- -[HMMTRAccessoryServerBrowser matterStackRestartHandlers]
- -[HMMTRAccessoryServerBrowser restartMatterStackForSystemCommissionerFabricWithCompletionHandler:]
- -[HMMTRAccessoryServerBrowser restartMatterStackWithFabricID:]
- -[HMMTRAccessoryServerBrowser restartMatterStackWithFabricID:completion:]
- -[HMMTRAccessoryServerBrowser setSystemCommissionerFabricID:]
- -[HMMTRAccessoryServerBrowser setSystemCommissionerNocSigner:]
- -[HMMTRAccessoryServerBrowser stopMatterStackWithCompletion:]
- -[HMMTRAccessoryServerBrowser timerDidFire:]
- -[HMMTRColorControl moveToCustomHueAndSaturationWithParams:completionHandler:]
- -[HMMTRColorControl moveToCustomHueWithParams:completionHandler:]
- -[HMMTRColorControl moveToCustomSaturationWithParams:completionHandler:]
- -[HMMTRDescriptorClusterManager hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:server:]
- -[HMMTRMatterKeypair initialize]
- -[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]
- -[HMMTRProtocolOperationManager handleSpecialCaseCharacteristicWithOperation:clientQueue:operationResponseHandler:]
- -[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:]
- -[HMMTRStorage(Records) removeRecordsForNode:]
- -[HMMTRStorage(Records) removeRecordsForNodeIDs:]
- -[HMMTRSyncClusterColorControl moveToCustomColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:]
- -[HMMTRSyncClusterColorControl moveToCustomHueAndSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:]
- -[HMMTRSyncClusterColorControl moveToCustomHueWithParams:expectedValues:expectedValueInterval:completionHandler:]
- -[HMMTRSyncClusterColorControl moveToCustomSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:]
- GCC_except_table1118
- GCC_except_table1122
- GCC_except_table1145
- GCC_except_table1195
- GCC_except_table1198
- GCC_except_table1200
- GCC_except_table1202
- GCC_except_table1241
- GCC_except_table1243
- GCC_except_table1247
- GCC_except_table1265
- GCC_except_table1276
- GCC_except_table1284
- GCC_except_table1293
- GCC_except_table1302
- GCC_except_table1304
- GCC_except_table1311
- GCC_except_table1327
- GCC_except_table1333
- GCC_except_table1340
- GCC_except_table1639
- GCC_except_table1644
- GCC_except_table1651
- GCC_except_table1682
- GCC_except_table1691
- GCC_except_table1692
- GCC_except_table1695
- GCC_except_table1697
- GCC_except_table1705
- GCC_except_table1707
- GCC_except_table1714
- GCC_except_table1715
- GCC_except_table1727
- GCC_except_table1728
- GCC_except_table1729
- GCC_except_table1730
- GCC_except_table1733
- GCC_except_table1739
- GCC_except_table1745
- GCC_except_table1759
- GCC_except_table1761
- GCC_except_table1778
- GCC_except_table1783
- GCC_except_table1786
- GCC_except_table1790
- GCC_except_table1799
- GCC_except_table1830
- GCC_except_table1834
- GCC_except_table1848
- GCC_except_table1849
- GCC_except_table1869
- GCC_except_table1872
- GCC_except_table1879
- GCC_except_table1887
- GCC_except_table1894
- GCC_except_table1901
- GCC_except_table1915
- GCC_except_table1925
- GCC_except_table1932
- GCC_except_table1938
- GCC_except_table1945
- GCC_except_table1948
- GCC_except_table1955
- GCC_except_table1986
- GCC_except_table2000
- GCC_except_table2001
- GCC_except_table2002
- GCC_except_table2008
- GCC_except_table2016
- GCC_except_table2027
- GCC_except_table2038
- GCC_except_table2050
- GCC_except_table2059
- GCC_except_table2062
- GCC_except_table2121
- GCC_except_table2126
- GCC_except_table2220
- GCC_except_table2223
- GCC_except_table2340
- GCC_except_table2344
- GCC_except_table2347
- GCC_except_table2370
- GCC_except_table2391
- GCC_except_table432
- GCC_except_table434
- GCC_except_table486
- GCC_except_table488
- GCC_except_table490
- GCC_except_table492
- GCC_except_table495
- GCC_except_table526
- GCC_except_table556
- GCC_except_table901
- GCC_except_table923
- GCC_except_table946
- GCC_except_table961
- _OBJC_CLASS_$_HMMTRSyncClusterColorControl
- _OBJC_CLASS_$_MTRClusterColorControl
- _OBJC_CLASS_$_MTRControllerFactory
- _OBJC_CLASS_$_MTRControllerFactoryParams
- _OBJC_IVAR_$_HMMTRAccessoryServer._deviceController
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._deviceController
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._matterStackRestartHandlers
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._systemCommissionerFabricID
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._systemCommissionerNocSigner
- _OBJC_METACLASS_$_HMMTRSyncClusterColorControl
- _OBJC_METACLASS_$_MTRClusterColorControl
- __OBJC_$_CLASS_METHODS_HMMTRColorControl
- __OBJC_$_CLASS_METHODS_HMMTRSyncClusterColorControl
- __OBJC_$_INSTANCE_METHODS_HMMTRColorControl
- __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterColorControl
- __OBJC_$_PROP_LIST_HMMTRSyncClusterColorControl
- __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterColorControl
- __OBJC_CLASS_RO_$_HMMTRSyncClusterColorControl
- __OBJC_METACLASS_RO_$_HMMTRSyncClusterColorControl
- ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.527
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.631
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.634
- ___104-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:endpoint:callbackQueue:completionHandler:]_block_invoke.337
- ___108-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]_block_invoke
- ___108-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]_block_invoke.76
- ___108-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]_block_invoke.79
- ___108-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]_block_invoke.81
- ___108-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]_block_invoke.82
- ___108-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:]_block_invoke.83
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.129
- ___113-[HMMTRSyncClusterColorControl moveToCustomHueWithParams:expectedValues:expectedValueInterval:completionHandler:]_block_invoke
- ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.177
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.229
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.404
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.405
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.406
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.407
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.408
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.409
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.123
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.125
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke_2.124
- ___120-[HMMTRSyncClusterColorControl moveToCustomSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:]_block_invoke
- ___126-[HMMTRSyncClusterColorControl moveToCustomColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:]_block_invoke
- ___126-[HMMTRSyncClusterColorControl moveToCustomHueAndSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:]_block_invoke
- ___128-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
- ___128-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.157
- ___128-[HMMTRAccessoryServerBrowser accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]_block_invoke
- ___129-[HMMTRAccessoryServerBrowser _accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]_block_invoke
- ___129-[HMMTRAccessoryServerBrowser _accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]_block_invoke_2
- ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.137
- ___133-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]_block_invoke
- ___133-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]_block_invoke.127
- ___133-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:]_block_invoke_2
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.158
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.165
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.166
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.167
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.168
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.60
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.68
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.72
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.79
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.83
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.87
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.91
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.95
- ___174-[HMMTRAccessoryServer _handleAddNocCompletionDuringSystemCommissionerFabricCommissioningWithDispatchGroup:fabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:error:]_block_invoke.526
- ___174-[HMMTRAccessoryServer _handleAddNocCompletionDuringSystemCommissionerFabricCommissioningWithDispatchGroup:fabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:error:]_block_invoke_2
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.148
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.150
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.149
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.114
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.115
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.126
- ___263-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.104
- ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.96
- ___37-[HMMTRAccessoryServer _retryPairing]_block_invoke
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.496
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.497
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.498
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.499
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.500
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.501
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.502
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.503
- ___43+[HMMTRSyncClusterColorControl logCategory]_block_invoke
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.262
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.265
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.617
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.539
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.540
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.251
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.252
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke_2
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.240
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.594
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.598
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.597
- ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.156
- ___49-[HMMTRStorage(Records) removeRecordsForNodeIDs:]_block_invoke
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.557
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.560
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.561
- ___51-[HMMTRAccessoryServer createDoorLockClusterObject]_block_invoke
- ___51-[HMMTRAccessoryServer createDoorLockClusterObject]_block_invoke.638
- ___51-[HMMTRAccessoryServer createDoorLockClusterObject]_block_invoke.639
- ___51-[HMMTRAccessoryServer createDoorLockClusterObject]_block_invoke_2
- ___51-[HMMTRAccessoryServer createDoorLockClusterObject]_block_invoke_3
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.658
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.135
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.136
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.555
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke_2
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.507
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.512
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.657
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.362
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.363
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.364
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke_4
- ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.247
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.369
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.370
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.371
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke_4
- ___59-[HMMTRAccessoryServer restrictAccessToNodeIDs:completion:]_block_invoke
- ___59-[HMMTRAccessoryServer restrictAccessToNodeIDs:completion:]_block_invoke.572
- ___59-[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]_block_invoke.200
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.365
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.366
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.367
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.368
- ___61-[HMMTRAccessoryServerBrowser stopMatterStackWithCompletion:]_block_invoke
- ___62-[HMMTRAccessoryServerBrowser restartMatterStackWithFabricID:]_block_invoke
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.98
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.385
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.386
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.387
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke_6
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.374
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.375
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke_4
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.73
- ___65-[HMMTRColorControl moveToCustomHueWithParams:completionHandler:]_block_invoke
- ___65-[HMMTRColorControl moveToCustomHueWithParams:completionHandler:]_block_invoke.1
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.372
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.373
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke_4
- ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.277
- ___66-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:]_block_invoke
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.198
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.102
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.99
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.236
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.345
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.350
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.377
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.378
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.379
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke_4
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.382
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.383
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.384
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke_4
- ___72-[HMMTRColorControl moveToCustomSaturationWithParams:completionHandler:]_block_invoke
- ___72-[HMMTRColorControl moveToCustomSaturationWithParams:completionHandler:]_block_invoke.5
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.552
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.553
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.554
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.541
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.542
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.549
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.550
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.543
- ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.143
- ___73-[HMMTRAccessoryServerBrowser restartMatterStackWithFabricID:completion:]_block_invoke
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.603
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.604
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.608
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.257
- ___78-[HMMTRColorControl moveToCustomColorTemperatureWithParams:completionHandler:]_block_invoke.9
- ___78-[HMMTRColorControl moveToCustomHueAndSaturationWithParams:completionHandler:]_block_invoke
- ___78-[HMMTRColorControl moveToCustomHueAndSaturationWithParams:completionHandler:]_block_invoke.7
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.351
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.352
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.353
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.138
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.140
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.141
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.84
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.86
- ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.225
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.314
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.315
- ___84-[HMMTRAccessoryServer readPairingWindowStatusAfterStackReadyWithCompletionHandler:]_block_invoke
- ___84-[HMMTRAccessoryServer readPairingWindowStatusAfterStackReadyWithCompletionHandler:]_block_invoke.355
- ___84-[HMMTRAccessoryServer readPairingWindowStatusAfterStackReadyWithCompletionHandler:]_block_invoke.361
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.621
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.622
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.623
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.626
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke_4
- ___88-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:]_block_invoke
- ___88-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:]_block_invoke.88
- ___88-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:]_block_invoke.89
- ___88-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:]_block_invoke.90
- ___88-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:]_block_invoke_2
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.243
- ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.340
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.411
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.412
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.413
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.414
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.415
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_3.416
- ___92-[HMMTRAccessoryServerBrowser fetchOrCreateSystemCommissionerRootCertificateWithCompletion:]_block_invoke
- ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.151
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.92
- ___98-[HMMTRAccessoryServerBrowser restartMatterStackForSystemCommissionerFabricWithCompletionHandler:]_block_invoke
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.226
- ___99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke.113
- ___99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke.115
- ___99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke_2.114
- ___99-[HMMTRAccessoryServerBrowser removeSystemCommissionerFabricAccessoryWithNodeID:completionHandler:]_block_invoke_2.116
- ___Block_byref_object_copy_.3006
- ___Block_byref_object_copy_.3663
- ___Block_byref_object_copy_.4495
- ___Block_byref_object_copy_.5006
- ___Block_byref_object_copy_.5494
- ___Block_byref_object_copy_.6015
- ___Block_byref_object_copy_.6198
- ___Block_byref_object_dispose_.3007
- ___Block_byref_object_dispose_.3664
- ___Block_byref_object_dispose_.4496
- ___Block_byref_object_dispose_.5007
- ___Block_byref_object_dispose_.5495
- ___Block_byref_object_dispose_.6016
- ___Block_byref_object_dispose_.6199
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32s_e48_v24?0"MTRCommissioningParameters"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e60_{_HMFFutureBlockOutcome=q}16?0"HMMTRSyncClusterDoorLock"8ls32l8
- ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?08"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56bs64bs_e20_v20?0B8"NSError"12ls48l8s32l8s56l8s40l8s64l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e20_v20?0B8"NSError"12ls32l8s56l8s40l8s48l8r64l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48bs56bs64bs72r_e20_v20?0B8"NSError"12ls32l8s48l8s56l8r72l8s40l8s64l8
- ___block_descriptor_80_e8_32s40s48bs56bs64bs72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8
- ___block_literal_global.100
- ___block_literal_global.104.257
- ___block_literal_global.1145
- ___block_literal_global.1291
- ___block_literal_global.130
- ___block_literal_global.1379
- ___block_literal_global.155
- ___block_literal_global.1569
- ___block_literal_global.1678
- ___block_literal_global.212
- ___block_literal_global.227
- ___block_literal_global.2315
- ___block_literal_global.2612
- ___block_literal_global.263
- ___block_literal_global.2693
- ___block_literal_global.2900
- ___block_literal_global.3114
- ___block_literal_global.3422
- ___block_literal_global.3703
- ___block_literal_global.373
- ___block_literal_global.389
- ___block_literal_global.3916
- ___block_literal_global.392
- ___block_literal_global.4328
- ___block_literal_global.4724
- ___block_literal_global.512
- ___block_literal_global.5211
- ___block_literal_global.538
- ___block_literal_global.5403
- ___block_literal_global.545
- ___block_literal_global.5527
- ___block_literal_global.5665
- ___block_literal_global.606
- ___block_literal_global.6081
- ___block_literal_global.671
- ___block_literal_global.785
- ___block_literal_global.932
- __unnamed_array_storage.1274
- __unnamed_array_storage.1558
- __unnamed_array_storage.332
- __unnamed_array_storage.3609
- __unnamed_array_storage.5035
- _logCategory._hmf_once_t13
- _logCategory._hmf_once_t133
- _logCategory._hmf_once_t20.5664
- _logCategory._hmf_once_t293
- _logCategory._hmf_once_t3.784
- _logCategory._hmf_once_t44
- _logCategory._hmf_once_t492
- _logCategory._hmf_once_t7.1378
- _logCategory._hmf_once_t76
- _logCategory._hmf_once_t81
- _logCategory._hmf_once_t9
- _logCategory._hmf_once_v10
- _logCategory._hmf_once_v134
- _logCategory._hmf_once_v14
- _logCategory._hmf_once_v21.5666
- _logCategory._hmf_once_v294
- _logCategory._hmf_once_v4.786
- _logCategory._hmf_once_v45
- _logCategory._hmf_once_v493
- _logCategory._hmf_once_v77
- _logCategory._hmf_once_v8.1380
- _logCategory._hmf_once_v82
- _objc_msgSend$_accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:
- _objc_msgSend$_callMatterStackRestartHandlers
- _objc_msgSend$_fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:
- _objc_msgSend$_getSystemCommissionerFabricRootCertificateWithIndex:ipk:controllerNodeID:
- _objc_msgSend$_prepareForPairingWithSetupPayload:fabricID:hasPriorSuccessfulPairing:category:completionHandler:
- _objc_msgSend$_restartMatterStackWithFabricID:
- _objc_msgSend$_startChipStackWithFabricID:
- _objc_msgSend$_stopMatterStack
- _objc_msgSend$_updateSystemCommissionerFabricIDAndGetIndex
- _objc_msgSend$accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:
- _objc_msgSend$addOperationWithBlock:queuePriority:
- _objc_msgSend$attestationDataStore
- _objc_msgSend$fabricIDForSystemCommissioner
- _objc_msgSend$fetchOrCreateSystemCommissionerRootCertificateWithCompletion:
- _objc_msgSend$handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:
- _objc_msgSend$handleSpecialCaseCharacteristicWithOperation:clientQueue:operationResponseHandler:
- _objc_msgSend$hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:server:
- _objc_msgSend$hue
- _objc_msgSend$initWithSigningKeypair:fabricId:ipk:
- _objc_msgSend$initialize
- _objc_msgSend$ipkForCurrentFabricID
- _objc_msgSend$knownFabricWithID:
- _objc_msgSend$matterStackRestartHandlers
- _objc_msgSend$moveToColorTemperatureWithParams:completionHandler:
- _objc_msgSend$moveToColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:
- _objc_msgSend$moveToCustomHueAndSaturationWithParams:completionHandler:
- _objc_msgSend$moveToCustomHueAndSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:
- _objc_msgSend$moveToCustomHueWithParams:completionHandler:
- _objc_msgSend$moveToCustomHueWithParams:expectedValues:expectedValueInterval:completionHandler:
- _objc_msgSend$moveToCustomSaturationWithParams:completionHandler:
- _objc_msgSend$moveToCustomSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:
- _objc_msgSend$optionsOverride
- _objc_msgSend$readAttributeOptionsWithCompletion:
- _objc_msgSend$readAttributeOptionsWithParams:
- _objc_msgSend$readPairingWindowStatusAfterStackReadyWithCompletionHandler:
- _objc_msgSend$registerOperation:clientQueue:operationResponseHandler:
- _objc_msgSend$removeRecordsForNode:
- _objc_msgSend$removeRecordsForNodeIDs:
- _objc_msgSend$restartMatterStackForSystemCommissionerFabricWithCompletionHandler:
- _objc_msgSend$restartMatterStackWithFabricID:
- _objc_msgSend$restartMatterStackWithFabricID:completion:
- _objc_msgSend$restrictAccessToNodeIDs:completion:
- _objc_msgSend$saturation
- _objc_msgSend$setCdCerts:
- _objc_msgSend$setColorTemperature:
- _objc_msgSend$setDeviceController:
- _objc_msgSend$setPaaCerts:
- _objc_msgSend$setStartServer:
- _objc_msgSend$setSystemCommissionerFabricID:
- _objc_msgSend$startControllerOnExistingFabric:
- _objc_msgSend$startControllerOnNewFabric:
- _objc_msgSend$startup:
- _objc_release_x10
CStrings:
+ "\x02\x11"
+ "\x03\x12"
+ "\x15"
+ "\x17"
+ "%@/%p"
+ "%{public}@    %@ (0x%016X)"
+ "%{public}@    Subjects:"
+ "%{public}@Accessory is not position aware, setting target tilt step size to maximum value."
+ "%{public}@Accessory with node ID %@ was added to home with fabricID %@"
+ "%{public}@Adding controller NodeID %@ (0x%lX)"
+ "%{public}@Adding owner NodeID %@ (0x%lX)"
+ "%{public}@All nodes to add when storage became available: %@"
+ "%{public}@All parameters are not available"
+ "%{public}@Attribute timer NOT found for path %@ - Create timer with report %@"
+ "%{public}@Attribute timer found for %@ - reset timer and update report with %@"
+ "%{public}@Attribute timer triggered for path %@ with report %@"
+ "%{public}@Attributes %@ for characteristic %@ not found in supported attribute list %@ for endpoint %@"
+ "%{public}@AuthMode: %@"
+ "%{public}@Bad NOC in V1 key"
+ "%{public}@Bad op key passed to initializer"
+ "%{public}@Bad op key passed to operationalKey"
+ "%{public}@Bad params: %@"
+ "%{public}@Bad private key passed to initializer"
+ "%{public}@Bad startup parameter"
+ "%{public}@Bad startup parameter from V1 keypair"
+ "%{public}@Building V1 key from V0 key"
+ "%{public}@Building new fabric certs with fabricID: %@"
+ "%{public}@CHIP Stack is not running. Aborting pairing."
+ "%{public}@Characteristics Operation Queue: Read characteristics(%@) job(%lu) queued."
+ "%{public}@Characteristics Operation Queue: Write characteristics(%@) job(%lu) queued%s."
+ "%{public}@Characteristics Operation Queue: fetch color control cluster job(%lu) completed."
+ "%{public}@Characteristics Operation Queue: fetch color control cluster job(%lu) started."
+ "%{public}@Characteristics Operation Queue: fetching color control cluster job(%lu) queued."
+ "%{public}@Cluster classes to query for attributes : %@"
+ "%{public}@Constructed Service Label service at endpoint %@"
+ "%{public}@Could not build V1 key. System commissioner won't be functional."
+ "%{public}@Could not build operational key pair from V1 Key. System commissioner won't be functional."
+ "%{public}@Could not fetch color control cluster because no device paired: %@ job(%lu)"
+ "%{public}@Could not obtain fabric ID for pairing from root cert %@"
+ "%{public}@Could not remove key '%@' from MTSKeyValueStore"
+ "%{public}@Could not retrieve MTSKeyValueStore to update"
+ "%{public}@Could not serialize operational key pair"
+ "%{public}@Could not store key '%@' into MTSKeyValueStore"
+ "%{public}@Creating controller for %@ in enabled state: %@"
+ "%{public}@Creating controller for fabric ID: %@"
+ "%{public}@Currently generating key pair. Will ignore the keypair data change."
+ "%{public}@Device controller unavailable to custom-handle the Attribute Report for characteristic %@"
+ "%{public}@Device controller wrapper is disabled."
+ "%{public}@Device controller wrapper is revoked and back online. Setting up MTRDevice again."
+ "%{public}@Disable controller factory operation while not a primary resident"
+ "%{public}@Disabled normal operation with token %@"
+ "%{public}@Disabling normal operation with token %@"
+ "%{public}@Dumping stack storage for params: %@"
+ "%{public}@Dumping storage content to MTSKeyValueStore for backward compatibility"
+ "%{public}@Enabling normal operation with token %@"
+ "%{public}@FATAL Error: Failed to generate ooperational cert for fabric ID %@. error: %@"
+ "%{public}@FATAL Error: Failed to generate root cert for fabric ID %@. error: %@"
+ "%{public}@Failed in getting keypair data from private key"
+ "%{public}@Failed to create controller: %@"
+ "%{public}@Failed to fetch root certificate: %@"
+ "%{public}@Failed to generate operational key"
+ "%{public}@Failed to get controller wrapper for the fabric ID %@"
+ "%{public}@Failed to get device attribute list for cluster class name %@ at endpoint %@. Error: %@"
+ "%{public}@Failed to get key data from operational key"
+ "%{public}@Failed to get key data from private key"
+ "%{public}@Failed to read ACL. No device found"
+ "%{public}@Failed to serialize combo keypair cert data: %@"
+ "%{public}@Failed to serialize operational key pair for new fabric. Aborting pairing prep."
+ "%{public}@Failed to setup storage for new fabric. Aborting pairing prep."
+ "%{public}@Failed to start system commissioner controller for fabric ID: %@"
+ "%{public}@Failed to start: %@"
+ "%{public}@Failed to update Access Control List on the accessory with error %@"
+ "%{public}@Failed unarchive V1 key data: %@"
+ "%{public}@Faking a color temperature attribute report (50) on endpoint %@ upon hue/sat command invocation"
+ "%{public}@Fetch fabric parameters from storage"
+ "%{public}@Fetching color control cluster for job: %lu"
+ "%{public}@Fetching system commissioner certs for fabric ID %@ and controller node ID %@"
+ "%{public}@Found color control cluster at endpoint: %@ job(%lu)"
+ "%{public}@Hitting maximum number of getters. Removing unused and restarting factory. Currently used: %@"
+ "%{public}@Key value could not be deserialized: %@"
+ "%{public}@Keypair data changed"
+ "%{public}@Matter device controller is unexpectedly inactive when storage is updated"
+ "%{public}@New controller wrapper %@ for fabric ID %@"
+ "%{public}@No Matter device available to open pairing window"
+ "%{public}@No Matter device controller available to announce OTA provider"
+ "%{public}@No Matter device controller available to commission"
+ "%{public}@No Matter device controller available to commission with system commissioner fabric"
+ "%{public}@No Matter device controller available to fetch color control cluster for job(%lu)"
+ "%{public}@No Matter device controller available to fetch current pairing"
+ "%{public}@No Matter device controller available to fetch pairings"
+ "%{public}@No Matter device controller available to fetch serial number"
+ "%{public}@No Matter device controller available to fetch software version number"
+ "%{public}@No Matter device controller available to fetch software version string"
+ "%{public}@No Matter device controller available to get endpoint for OTA requester"
+ "%{public}@No Matter device controller available to handle commissioning completion"
+ "%{public}@No Matter device controller available to remove all pairings"
+ "%{public}@No Matter device controller available to remove pairing"
+ "%{public}@No Matter device controller available to update default OTA provider"
+ "%{public}@No Matter device controller available to write characteristics"
+ "%{public}@No Matter device controller to update fabric label job"
+ "%{public}@No V0 keypair present"
+ "%{public}@No V0 keypair present. Building new V1 keypair."
+ "%{public}@No V1 keypair present"
+ "%{public}@No active Matter device controller to read characteristic values"
+ "%{public}@No commissionee node ID assigned yet. Not issuing NOC."
+ "%{public}@No device controller to get transport type"
+ "%{public}@No f/%x/o in storage"
+ "%{public}@No fabric records present in MTS storage for matching V0 key pair"
+ "%{public}@No new fabric created. Returning previous controller wrapper."
+ "%{public}@No supported attributes read from accessory for cluster class %@ on endpoint %@, Error: %@"
+ "%{public}@Obtained controller wrapper %@ for fabric ID %@"
+ "%{public}@Obtained device controller: %p"
+ "%{public}@Obtaining device controller"
+ "%{public}@Optional characteristic %@ on endpoint %@ requires an additional Optional Matter attribute check"
+ "%{public}@Pairing accessory requires retrieving controller wrapper with fabric ID: %@"
+ "%{public}@Persisting HomeKitMatter Data for Accessory: %@, shared admin: %@, system commissioner mode: %@"
+ "%{public}@Picked fabric index %@ with fabric ID %@"
+ "%{public}@Pre-warming system commissioning device controller"
+ "%{public}@Private key not found"
+ "%{public}@Privilege: %@"
+ "%{public}@Processing Attribute Report: %@"
+ "%{public}@Propagating V1 key from V0 key and creating new fabric certs"
+ "%{public}@Propagating V1 key from V0 key and storage certs"
+ "%{public}@Querying device cluster %@ at endpoint %@ for supported attributes"
+ "%{public}@Received supported attributes list from accessory for cluster class %@ on endpoint %@. Attributes: %@"
+ "%{public}@Registered controller revoke handler"
+ "%{public}@Removed"
+ "%{public}@Removing"
+ "%{public}@Removing %@ from factory"
+ "%{public}@Removing all controller wrappers"
+ "%{public}@Removing controller wrapper: %@"
+ "%{public}@Replaced startup params"
+ "%{public}@Replacing startup params"
+ "%{public}@Restarting controller factory"
+ "%{public}@Retrieving controller wrapper for the first time for %@"
+ "%{public}@SecKeyCreateWithData failed"
+ "%{public}@Setting root and operational cert in start up params %@ %@ for current home controller"
+ "%{public}@Setting up MTRDevice"
+ "%{public}@Setting up controller for Home fabric %@ in order to pre-warm commissioning session"
+ "%{public}@Setting up controller wrapper for Home FabricID = %@, currentFabricID = %@"
+ "%{public}@Setting up storage state after cert fetch for Home Fabric ID = %@"
+ "%{public}@Setting up storage state for Home Fabric ID = %@"
+ "%{public}@Setting up storage state to persist for Home Fabric ID = %@"
+ "%{public}@Shutdown"
+ "%{public}@Shutting down"
+ "%{public}@Skip handling of report: %@"
+ "%{public}@Staging is no longer supported when system commissioner feature is disabled"
+ "%{public}@Starting attribute timer with delay of %f for path %@"
+ "%{public}@Startup parameter changed for %@. Replaced controller wrapper params."
+ "%{public}@Startup parameter remains the same for %@. Returning the previous controller wrapper."
+ "%{public}@Stopping attribute timer for path %@"
+ "%{public}@Storage is already configured. Prewarming Matter device controller."
+ "%{public}@Storage state cannot be setup without fabric ID"
+ "%{public}@Storing the initial Matter storage to remote"
+ "%{public}@Successfully updated ACL to"
+ "%{public}@Supported attributes selector not found for cluster: %@"
+ "%{public}@System commissioner controller is not ready to start. Aborting staging."
+ "%{public}@System commissioner controller parameters are not available. No certs are fetched."
+ "%{public}@System commissioner controller parameters could not be fetched. No certs are fetched."
+ "%{public}@System commissioner operational cert missing controller node ID. No certs are fetched."
+ "%{public}@TLV parsing failed"
+ "%{public}@Unable to get controller wrapper for fabric ID: %@"
+ "%{public}@Unable to reconstruct operational key %@"
+ "%{public}@Unable to reconstruct private key"
+ "%{public}@Unable to reconstruct private key from TLV"
+ "%{public}@Unable to recover public key from TLV"
+ "%{public}@Unexpected key pair data version: %@"
+ "%{public}@Unexpected non-UTF8 SSID was skipped: %@"
+ "%{public}@Unexpected storage fabric ID %@ after generating cert for fabric ID %@"
+ "%{public}@Unknown field in the key pair TLV struct"
+ "%{public}@Update report for path %@ with report %@ and reset timer"
+ "%{public}@Updated Access Control List on accessory %@"
+ "%{public}@Updating accessory ACL to"
+ "%{public}@Updating accessory ACL to restrict administrative access to %@ and view access to %@"
+ "%{public}@Using fabric ID %@ for pairing from retrieved cert"
+ "%{public}@Using new key pair for system commissioner: %@"
+ "%{public}@V1 keypair disappeared from keychain"
+ "%{public}@V1 keypair remains the same"
+ "%{public}@Voted normal operation with token %@"
+ "%{public}@Voting to enable controller factory when setting up paired devices"
+ "%{public}@Will construct service with characteristics %@ for nodeID %@"
+ "%{public}@[Flow: %@] Created door lock cluster object: %@"
+ "%{public}@[Flow: %@] Creation is already in progress"
+ "%{public}@[Flow: %@] Did not find endpoint for door lock with error: %@"
+ "%{public}@[Flow: %@] Failed to create door lock cluster object. Removing door lock cluster future from accessory server: %p"
+ "%{public}@[Flow: %@] Failed to get base device. matter device: %@, base device: %@, getBaseDeviceError: %@"
+ "%{public}@[Flow: %@] Found base device: %@. matterDevice: %@"
+ "%{public}@[Flow: %@] Found existing door lock cluster object"
+ "%{public}@[Flow: %@] Getting base device with nodeID: %@"
+ "%{public}@[Flow: %@] Getting door lock cluster object"
+ "%{public}@[Flow: %@] Looking up endpoint for clusterID: %@, device: %@, "
+ "%{public}@[Flow: %@] No Matter device controller available"
+ "%{public}@[Flow: %@] Returning doorLockCluster: %@"
+ "%{public}@[Flow: %@] findOrAddUserWithUniqueID: %@"
+ "%{public}@[Flow: %@] findOrAddUserWithUniqueID: %@, isRemote: %@"
+ "%{public}@disabling"
+ "%{public}@enabled: %@ -> %@"
+ "%{public}@f/%x/n doesn't match f/%x/o"
+ "%{public}@f/%x/o format mismatch"
+ "%{public}@moveToColorTemperatureWithParams completed with colorTemperature %@, optionsMask %@, error %@"
+ "%{public}@moveToColorTemperatureWithParams with colorTemperature %@, transitionTime: %@, optionsMask %@"
+ "%{public}@vendorID = %@, productID = %@, category = %@, configNumber = %@, nodeID = %@"
+ "(\x13\x11\x18\x1c"
+ "."
+ "000000C2-0000-1000-8000-0026BB765291"
+ "1&8+\x1f\n\x15"
+ "3#"
+ "?"
+ "@\"HMMTRColorControl\""
+ "@\"HMMTRControllerFactory\""
+ "@\"HMMTRControllerFactoryStorage\""
+ "@\"HMMTRControllerWrapper\""
+ "@\"HMMTRFabricControllerStore\""
+ "@\"HMMTRSystemCommissionerControllerParams\""
+ "@\"MTRAttributePath\""
+ "@\"MTRDeviceControllerFactoryParams\""
+ "@\"MTRDeviceControllerStartupParams\""
+ "@\"NSNumber\"16@?0@\"NSString\"8"
+ "@24@0:8^{__SecKey=}16"
+ "@32@0:8@16^{__SecKey=}24"
+ "@32@0:8@?16@24"
+ "@56@0:8@16@24d32@40@48"
+ "@56@0:8^{__SecKey=}16^{__SecKey=}24@32@40@48"
+ "@64@0:8@16^{__SecKey=}24^{__SecKey=}32@40@48@56"
+ "Administrator"
+ "B16@?0@\"<HMMTRFabricStorageDataSource>\"8"
+ "B20@0:8B16"
+ "B36@0:8B16^@20^@28"
+ "B40@0:8@16^@24^@32"
+ "B48@0:8@16@24@?32@?40"
+ "B56@0:8@16^@24^@32^@40^@48"
+ "CASE"
+ "CHIPPlugin.systemCommissioner.nodeopcerts.CA:1"
+ "ColorControl"
+ "Controller"
+ "Group"
+ "HMMTRAttributeTimer"
+ "HMMTRControllerFactory"
+ "HMMTRControllerFactory queue"
+ "HMMTRControllerFactoryStorage"
+ "HMMTRControllerWrapper"
+ "HMMTRControllerWrapperRevokeHandlerInfo"
+ "HMMTRFabricControllerStore"
+ "HMMTRFabricControllerStore queue"
+ "HMMTRSystemCommissionerControllerParams"
+ "HMMTRSystemCommissionerControllerParams queue"
+ "MTRBaseClusterWindowCovering"
+ "Manage"
+ "OTAProviderState"
+ "Operate"
+ "PASE"
+ "PerFabricID:%@"
+ "ProxyView"
+ "RequiresOptionalMatterAttribute"
+ "System Commissioner Controller"
+ "T@\"HMFTimer\",&,N,V_attributeTimer"
+ "T@\"HMMTRColorControl\",&,V_colorControlCluster"
+ "T@\"HMMTRControllerFactory\",R,N,V_controllerFactory"
+ "T@\"HMMTRControllerFactory\",W,N,V_factory"
+ "T@\"HMMTRControllerFactoryStorage\",R,N,V_storage"
+ "T@\"HMMTRControllerWrapper\",&,N,V_controllerWrapper"
+ "T@\"HMMTRControllerWrapper\",&,V_controllerWrapper"
+ "T@\"HMMTRControllerWrapper\",R,D,N"
+ "T@\"HMMTRFabricControllerStore\",R,V_homeFabricControllers"
+ "T@\"HMMTRMatterKeypair\",&,N,V_v1keypair"
+ "T@\"HMMTRMatterKeypair\",R,D,N"
+ "T@\"HMMTRSystemCommissionerControllerParams\",R,N,V_systemCommissionerControllerParams"
+ "T@\"MTRAttributePath\",R,N,V_path"
+ "T@\"MTRDeviceController\",&,N,V_cachedDeviceController"
+ "T@\"MTRDeviceController\",R"
+ "T@\"MTRDeviceController\",R,D"
+ "T@\"MTRDeviceController\",R,D,N"
+ "T@\"MTRDeviceControllerFactoryParams\",R,C,N,V_factoryParams"
+ "T@\"MTRDeviceControllerStartupParams\",R,D,N"
+ "T@\"NSData\",&,N,V_originalPairingAttemptOperationalCert"
+ "T@\"NSData\",&,N,V_originalPairingAttemptRootCert"
+ "T@\"NSData\",&,V_keyRepr"
+ "T@\"NSData\",&,V_opKeyRepr"
+ "T@\"NSData\",R,C,V_ipk"
+ "T@\"NSData\",R,C,V_operationalCert"
+ "T@\"NSData\",R,C,V_rootCert"
+ "T@\"NSMutableArray\",R,N,V_controllerWrappers"
+ "T@\"NSMutableArray\",R,N,V_revokeHandlers"
+ "T@\"NSMutableDictionary\",&,N,V_attributeTimers"
+ "T@\"NSMutableDictionary\",&,N,V_report"
+ "T@\"NSMutableDictionary\",R,N,V_controllerWrappers"
+ "T@\"NSMutableDictionary\",R,N,V_mtrControllerFactoryKeyValueStore"
+ "T@\"NSMutableSet\",R,N,V_disablingTokens"
+ "T@\"NSNumber\",&,N,V_adminNodeID"
+ "T@\"NSNumber\",&,N,V_commissioningFabricID"
+ "T@\"NSNumber\",&,V_commissioneeNodeID"
+ "T@\"NSNumber\",R,D,N"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_workQueue"
+ "T@\"NSUUID\",&,V_initialMTRDeviceStateTimeoutId"
+ "T@,&,N,V_controllerFactoryEnablePerPrimaryResidentConfirmationToken"
+ "T@?,R,N,V_handler"
+ "TB,N,V_controllerRevokeHandlerRegistered"
+ "TB,N,V_generatingKeyPair"
+ "TB,N,V_matterFactoryRunning"
+ "TB,R,D"
+ "TB,V_factoryOperationEnabled"
+ "TB,V_hasOperationalCerts"
+ "TQ,R,V_version"
+ "T^{__SecKey=},D"
+ "Test"
+ "Ti,V_homeKeychainReadyNotificationToken"
+ "Ti,V_mtsKeychainReadyNotificationToken"
+ "Tq,R,N,V_otaProviderState"
+ "View"
+ "^{__SecKey=}24@0:8@16"
+ "_accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:"
+ "_adminNodeID"
+ "_attributeTimer"
+ "_attributeTimers"
+ "_auditControllerWrappersWithAllFabricIDs:"
+ "_buildV1KeyFromScratch"
+ "_buildV1KeyFromV0KeyAllowingNew:"
+ "_buildV1KeyWithPrivateKey:operationalKey:ipk:rootCert:operationalCert:updatingMTSKeyValueStore:"
+ "_buildV1KeyWithV0KeyPair:"
+ "_cachedDeviceController"
+ "_colorControlCluster"
+ "_commissioneeNodeID"
+ "_commissioningFabricID"
+ "_controllerFactory"
+ "_controllerFactoryEnablePerPrimaryResidentConfirmationToken"
+ "_controllerRevokeHandlerRegistered"
+ "_controllerWrapper"
+ "_controllerWrappers"
+ "_createControllerForGetter:"
+ "_createControllerWithStartupParams:"
+ "_currentHomeFabricDeviceController"
+ "_currentHomeFabricDeviceControllerStartupParams"
+ "_disablingTokens"
+ "_enabled"
+ "_factory"
+ "_factoryOperationEnabled"
+ "_factoryParams"
+ "_findFabricRecordInMTSKeyValueStoreMatchingKeyPair:ipk:rootCert:operationalKey:operationalCert:"
+ "_generatingKeyPair"
+ "_handleKeychainDataChanged"
+ "_handler"
+ "_hasOperationalCerts"
+ "_homeFabricControllers"
+ "_homeKeychainReadyNotificationToken"
+ "_initialMTRDeviceStateTimeoutId"
+ "_ipk"
+ "_isDeviceIDPaired:nodeID:fabricID:"
+ "_keyRepr"
+ "_matterFactoryRunning"
+ "_mtrControllerFactoryKeyValueStore"
+ "_mtsKeychainReadyNotificationToken"
+ "_obtainControllerWrapperWithV1KeyPair:startupParams:"
+ "_opKeyRepr"
+ "_operationalKey"
+ "_originalPairingAttemptOperationalCert"
+ "_originalPairingAttemptRootCert"
+ "_otaProviderState"
+ "_path"
+ "_prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:"
+ "_querySupportedAttributesFromClusterAtCHIPEndpoint:device:callbackQueue:clusterClassName:completionHandler:"
+ "_reloadWithDictionary:"
+ "_removeGetter:"
+ "_report"
+ "_restartMatterControllerFactory"
+ "_restoreCommissioneeInfoBeforeNextPairingAttempt"
+ "_revokeAvailable:"
+ "_revokeHandlers"
+ "_setEnabled:"
+ "_setupAndPersistStorageStateForHomeFabricID:completion:"
+ "_setupStorageStateAfterCertFetchForHomeFabricID:completion:"
+ "_setupStorageStateForHomeFabricID:"
+ "_setupStorageStateForUpdatedHomeFabricID:"
+ "_setupStorageStateForUpdatedHomeFabricID:rediscoverAccessories:"
+ "_setupStorageStateIfNotFabricID:rediscoverAccessories:"
+ "_startWithV1Keypair:"
+ "_startupParams"
+ "_systemCommissionerControllerParams"
+ "_updateAttributeTimer:report:timeout:server:"
+ "_updateMTSKeyValueStore:"
+ "_v1keypair"
+ "_verifyHAPOptionalCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForAttributes:hapServicesToCheckForOptionalMatterAttribute:clusterAttributesSupported:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:"
+ "accessoryServerForSystemCommissionerDeviceWithNodeID:completionHandler:"
+ "addCharactersInString:"
+ "adminNodeID"
+ "alphanumericCharacterSet"
+ "archiveV1KeyItemValue"
+ "attributePathWithEndpointID:clusterID:attributeID:"
+ "attributeTimer"
+ "attributeTimers"
+ "authMode"
+ "cachedDeviceController"
+ "certificationDeclarationCertificates"
+ "clear"
+ "colorControlCluster"
+ "colorTemperatureMireds"
+ "commissioneeNodeID"
+ "commissioningFabricID"
+ "componentsSeparatedByCharactersInSet:"
+ "configure"
+ "controller"
+ "controllerFactory"
+ "controllerFactoryEnablePerPrimaryResidentConfirmationToken"
+ "controllerRevokeHandlerRegistered"
+ "controllerWrapper"
+ "controllerWrappers"
+ "createControllerOnExistingFabric:error:"
+ "createControllerOnNewFabric:error:"
+ "createDoorLockClusterObjectWithFlow:"
+ "createPrivateKeyWithData:"
+ "currentHomeFabricDeviceControllerWrapper"
+ "dictionaryCopy"
+ "disableNormalOperation"
+ "disablingTokens"
+ "enableNormalOperationWithToken:"
+ "enabled"
+ "f/1/m"
+ "f/1/n"
+ "f/1/o"
+ "f/1/r"
+ "factory"
+ "factoryOperationEnabled"
+ "factoryParams"
+ "factoryParamsWithNoStorage"
+ "fetchCertificatesForSharedUserWithAccessoryNodeID:sharedUserType:publicKey:fabricID:completionHandler:"
+ "fetchColorControlCluster:"
+ "fetchControllerParamsAllowingNew:nocSigner:controllerWrapper:"
+ "fetchSharedUserCertForFabricWithID:completion:"
+ "fetchSystemCommissionerRootCertificateWithCompletion:"
+ "forAllStorageDataSourcesDo:"
+ "formUnionWithCharacterSet:"
+ "generatingKeyPair"
+ "getCHIPAttributesForCharacteristic:"
+ "handleHomeAddedAccessoryWithNodeID:fabricID:"
+ "handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:"
+ "handleKeyPairDataChanged"
+ "handleSpecialCaseCharacteristicWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:"
+ "handler"
+ "hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassesToQuery:hapServicesToCheckForFeatureMap:hapServicesToCheckForOptionalMatterAttribute:server:"
+ "hasOperationalCerts"
+ "hmmtr.attribute.timer"
+ "hmmtr.controllerfactory"
+ "hmmtr.controllerfactory.getter"
+ "hmmtr.ctrlpfabric"
+ "hmmtr.syscm.ctrparams"
+ "hmmtr.util.tlvparser"
+ "homeFabricControllers"
+ "homeKeychainReadyNotificationToken"
+ "initUnassociated"
+ "initWithHandler:queue:"
+ "initWithPrivateKey:"
+ "initWithQueue:controllerFactory:"
+ "initWithServer:report:timeout:queue:server:"
+ "initWithTLVData:"
+ "initWithV0Account:"
+ "initWithV0Account:privateKey:"
+ "initWithV1Account:"
+ "initWithV1Account:privateKey:operationalKey:rootCert:operationalCert:ipk:"
+ "initWithWorkQueue:factory:startupParams:name:"
+ "initWithWorkQueue:factoryParams:"
+ "initialMTRDeviceStateTimeoutId"
+ "initializeAllowingNew:"
+ "intermediateCertificate"
+ "invertedSet"
+ "isCertificate:equalTo:"
+ "isOwnerForHomeWithFabricID:"
+ "isPairedInStorage"
+ "isRequiresOptionalMatterAttributeForCharacteristic:"
+ "keyPairDataFromTLV:"
+ "keyRepr"
+ "matterFactoryRunning"
+ "moveToColorTemperatureWithParams:completion:"
+ "moveToCustomColorTemperatureValue:transitionTime:completionHandler:"
+ "mtrAuthModeAsString:"
+ "mtrControllerFactoryKeyValueStore"
+ "mtrPrivilegeAsString:"
+ "mtsKeyValueStore"
+ "mtsKeychainReadyNotificationToken"
+ "numberWithUnsignedLong:"
+ "opKeyRepr"
+ "opcert"
+ "operationalCertificateIssuer"
+ "operationalCertificateIssuerQueue"
+ "operationalKey"
+ "operationalKeypair"
+ "opkey"
+ "originalPairingAttemptOperationalCert"
+ "originalPairingAttemptRootCert"
+ "otaProviderState"
+ "path"
+ "port"
+ "printAccessControlList:"
+ "privilege"
+ "privkey"
+ "processAttributeReport:"
+ "productAttestationAuthorityCertificates"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "queueAccessoryOperation:highPriority:completion:"
+ "readAttributeAttributeListWithCompletionHandler:"
+ "registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:"
+ "registerRevokeHandlerWithQueue:handler:"
+ "removeAllGetters"
+ "removeRecordsForNode:systemCommissionerFabric:"
+ "removeRecordsForNodeIDs:systemCommissionerFabric:"
+ "replaceStartupParams:"
+ "report"
+ "revokeHandlers"
+ "rootcert"
+ "sanitizeHAPName:"
+ "self.version != V1"
+ "self.version == V1"
+ "setAdminNodeID:"
+ "setAttributeTimer:"
+ "setAttributeTimers:"
+ "setCachedDeviceController:"
+ "setCertificationDeclarationCertificates:"
+ "setColorControlCluster:"
+ "setColorTemperatureMireds:"
+ "setCommissioneeNodeID:"
+ "setCommissioningFabricID:"
+ "setControllerFactoryEnablePerPrimaryResidentConfirmationToken:"
+ "setControllerRevokeHandlerRegistered:"
+ "setControllerWrapper:"
+ "setFactory:"
+ "setFactoryOperationEnabled:"
+ "setGeneratingKeyPair:"
+ "setHasOperationalCerts:"
+ "setHomeKeychainReadyNotificationToken:"
+ "setInitialMTRDeviceStateTimeoutId:"
+ "setKeyRepr:"
+ "setMatterFactoryRunning:"
+ "setMtsKeychainReadyNotificationToken:"
+ "setOpKeyRepr:"
+ "setOperationalKey:"
+ "setOriginalPairingAttemptOperationalCert:"
+ "setOriginalPairingAttemptRootCert:"
+ "setPort:"
+ "setProductAttestationAuthorityCertificates:"
+ "setReport:"
+ "setShouldStartServer:"
+ "setV1keypair:"
+ "setupStorageStateAfterCertFetchForHomeFabricID:completion:"
+ "setupStorageStateAndRediscoverAccessoriesForHomeFabricID:"
+ "setupStorageStateForHomeFabricID:"
+ "setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricID:"
+ "sharedDeviceControllerFactory"
+ "shouldStartServer"
+ "stackStorageWithStartupParams:operationalKeyPairTLV:"
+ "startControllerFactory:error:"
+ "startupParams"
+ "startupParams:isEquivalentTo:"
+ "stopControllerFactory"
+ "storeV0MatterKeypair"
+ "storeV0MatterKeypairWithPrivateKey:"
+ "storeV1MatterKeypairWithPrivateKey:operationalKey:rootCert:operationalCert:ipk:"
+ "subjects"
+ "systemCommissionerControllerParams"
+ "systemCommissionerControllerWrapper"
+ "unarchiveV1KeyItemValue:"
+ "unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:"
+ "updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:"
+ "updateReport:"
+ "v0MatterKeypairFromKeychain"
+ "v120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@?112"
+ "v16@?0@\"HMMTRAccessoryServer\"8"
+ "v1KeypairIsEquivalentTo:"
+ "v1MatterKeypairFromKeychain"
+ "v1keypair"
+ "v20@0:8i16"
+ "v20@?0@\"HMMTRControllerWrapper\"8B16"
+ "v24@0:8^{__SecKey=}16"
+ "v32@?0@\"NSString\"8@\"NSArray\"16@\"NSError\"24"
+ "v36@0:8@?16B24@?28"
+ "v48@0:8@16@24@?32@?40"
+ "v48@0:8@16@24d32@40"
+ "v52@0:8@16B24@28@36@?44"
+ "v60@0:8@16@24@32B40@44@?52"
+ "v60@0:8^{__SecKey=}16^{__SecKey=}24@32@40@48B56"
+ "whitespaceCharacterSet"
+ "wrapperWithFabricID:startupParams:allFabricIDs:"
+ "wrapperWithName:startupParams:"
+ "\xa11"
+ "҂\xf0\xf0q"
- "\x18\x13\x11\x1a\x1a"
- "%{public}@Accessory with node ID %@ was added to home"
- "%{public}@An error occurred while trying to read the Color Control Options attribute"
- "%{public}@An error occurred while trying to read the Color Control Options attribute: %@"
- "%{public}@CHIP Stack is not running, starting it up now before staging accessory"
- "%{public}@Characteristics Operation Queue: Read characteristics job(%lu) queued."
- "%{public}@Characteristics Operation Queue: Write characteristics job(%lu) queued%s."
- "%{public}@Creating a new fabric for fabric ID: %@"
- "%{public}@Deferring pairing setup to a later point when all parameters are available"
- "%{public}@Did not find endpoint for door lock with error: %@"
- "%{public}@Explicitly writing fabric operational Key %@ to storage as current value doesn't match"
- "%{public}@Failed to generate root certificate: %@"
- "%{public}@Failed to read ACL. Node device found"
- "%{public}@Failed to remove accessory with node %@ as HMMTRAccessoryServer disappeared"
- "%{public}@Failed to restart Matter stack for System Commissioner Fabric with %@"
- "%{public}@Failed to restart matter stack for System Commissioner Storage Fabric"
- "%{public}@Failed to start matter stack for fabric with index: %@"
- "%{public}@Failed to update system commissioner fabric ID in MatterSupport storage: %@"
- "%{public}@Fatal error while starting the MTRControllerFactory, Matter stack cannot be started up..."
- "%{public}@Fetching system commissioner info through fabric ID %@"
- "%{public}@Gave up prewarming upon Matter stack restart failure: %@"
- "%{public}@HMMTRAccessoryServerBrowser is gone. Unwrapping pairing without restarting stack."
- "%{public}@HomeKitMatter Keypair doesn't support Deserialize"
- "%{public}@Matter SDK already running for System Commissioner Fabric"
- "%{public}@Matter stack already started for commissioning session pre-warming for fabric ID %@"
- "%{public}@Matter stack is already running. Prewarming Matter device controller."
- "%{public}@Matter stack restarted"
- "%{public}@Pairing accessory requires restart of stack with fabric ID: %@"
- "%{public}@Pairing prep already running system commissioner fabric"
- "%{public}@Pairing timed out already when matter stack restarted. Aborting pairing retry."
- "%{public}@Pairing timed out already when matter stack restarted. Discarding open commissioning window completion."
- "%{public}@Persisting HomeKitMatter Data for Accessory: %@"
- "%{public}@Removing door lock cluster future from accessory server: %p"
- "%{public}@Restarting Matter stack for Home fabric %@ in order to pre-warm commissioning session"
- "%{public}@Restarting Matter stack for system commissioner in order to pre-warm commissioning session"
- "%{public}@Restarting Matter stack to clear state after aborting pairing"
- "%{public}@Restarting stack to clear the stack state after failed pairing."
- "%{public}@Restarting the CHIP Stack to pick up storage changes before pairing"
- "%{public}@Restarting the stack for FabricID = %@, currentFabricID = %@"
- "%{public}@Root keypair for System Commissioner fabric has changed."
- "%{public}@Selecting System Commissioner Fabric ID as = %@"
- "%{public}@Setting NOC issuer and queue for it in start up params"
- "%{public}@Setting controller node ID as %@"
- "%{public}@Setting root and operational cert in start up params %@ %@"
- "%{public}@Skipping starting matter stack as IPK is not available"
- "%{public}@Starting up the stack for Fabric ID = %@"
- "%{public}@Starting up the stack for System Commissioner FabricID = %@"
- "%{public}@Storing System Commissioner Fabric ID as = %@"
- "%{public}@Successfully updated ACL to restrict access to Node IDs %@"
- "%{public}@System commissioner fabric ID changed from %@ to %@"
- "%{public}@System commissioner fabric ID set to %@"
- "%{public}@System commissioner mode was cleared upon restarting Matter stack with non-system commissioner fabric: %@"
- "%{public}@Updated Access control List on accessory %@ to restrict access to resident only"
- "%{public}@Updating accessory ACL to restrict access to Node IDs %@"
- "%{public}@Updating system commissioner fabric ID from %@ to %@ with fabric index 0x%x."
- "%{public}@Using current system commissioner fabric ID %@ with index 0x%x"
- "%{public}@Will construct service with characteristics %@"
- "%{public}@Will not reset system commissioner mode upon remove device pairing completion."
- "%{public}@Will not reset system commissioner mode upon remove system commissioner fabric accessory completion."
- "%{public}@[Flow: %@] findOrAddHomeUser"
- "%{public}@matter device: %@, base device: %@, getBaseDeviceError: %@"
- "%{public}@moveToColorTemperatureWithParams colorTemperature %@, optionsMask %@, error %@"
- "%{public}@moveToCustomColorTemperatureWithParams colorTemperature %@, optionsMask %@, error %@"
- "%{public}@moveToCustomHueAndSaturationWithParams: params %@"
- "%{public}@moveToCustomHueAndSaturationWithParams: params %@, newParams %@, expectedDataValueDictionaries %@, expectedValueIntervalMs %@"
- "%{public}@moveToHueAndSaturationWithParams hue %@, saturation %@, optionsMask %@"
- "%{public}@moveToHueAndSaturationWithParams hue %@, saturation %@, optionsMask %@, error %@"
- "%{public}@moveToHueWithParams hue %@, optionsMask %@, err %@"
- "%{public}@moveToHueWithParams hue %@, optionsMask %@, error %@"
- "%{public}@moveToSaturationWithParams saturation %@, optionsMask %@, error %@"
- "%{public}@vendorID = %@, productID = %@, category = %@, configNumber = %@"
- "1&6)\x1f\b\x16"
- "B40@0:8@16@24@?32"
- "HMMTRSyncClusterColorControl"
- "T@\"MTRDeviceController\",&,N,V_deviceController"
- "T@\"MTRDeviceController\",R,V_deviceController"
- "T@\"NSMutableArray\",R,N,V_matterStackRestartHandlers"
- "T@\"NSNumber\",&,N,V_systemCommissionerFabricID"
- "_accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:"
- "_callMatterStackRestartHandlers"
- "_deviceController"
- "_fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:"
- "_matterStackRestartHandlers"
- "_prepareForPairingWithSetupPayload:fabricID:hasPriorSuccessfulPairing:category:completionHandler:"
- "_restartMatterStackWithFabricID:"
- "_startChipStackWithFabricID:"
- "_systemCommissionerFabricID"
- "_updateSystemCommissionerFabricIDAndGetIndex"
- "accessoryServerForSystemCommissionerDeviceWithNodeID:matterStackRestartHandler:completionHandler:"
- "createDoorLockClusterObject"
- "fetchCommissioningCertificatesForSharedAdminWithDeviceNodeID:sharedUserIdentifier:publicKey:fabricID:completionHandler:"
- "fetchOrCreateSystemCommissionerRootCertificateWithCompletion:"
- "handleHomeAddedAccessoryWithNodeID:"
- "handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:"
- "handleSpecialCaseCharacteristicWithOperation:clientQueue:operationResponseHandler:"
- "hapServiceDescriptionForServiceType:clustersInUse:endpoint:name:hapToCHIPClusterMappingArray:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:server:"
- "hue"
- "initWithSigningKeypair:fabricId:ipk:"
- "initialize"
- "matterStackRestartHandlers"
- "moveToColorTemperatureWithParams:completionHandler:"
- "moveToColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "moveToCustomColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "moveToCustomHueAndSaturationWithParams:completionHandler:"
- "moveToCustomHueAndSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "moveToCustomHueWithParams:completionHandler:"
- "moveToCustomHueWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "moveToCustomSaturationWithParams:completionHandler:"
- "moveToCustomSaturationWithParams:expectedValues:expectedValueInterval:completionHandler:"
- "optionsOverride"
- "readAttributeOptionsWithCompletion:"
- "readAttributeOptionsWithParams:"
- "readPairingWindowStatusAfterStackReadyWithCompletionHandler:"
- "registerOperation:clientQueue:operationResponseHandler:"
- "removeRecordsForNode:"
- "removeRecordsForNodeIDs:"
- "restartMatterStackForSystemCommissionerFabricWithCompletionHandler:"
- "restartMatterStackWithFabricID:"
- "restartMatterStackWithFabricID:completion:"
- "restrictAccessToNodeIDs:completion:"
- "saturation"
- "setCdCerts:"
- "setColorTemperature:"
- "setDeviceController:"
- "setPaaCerts:"
- "setStartServer:"
- "startControllerOnExistingFabric:"
- "startControllerOnNewFabric:"
- "startup:"
- "stopMatterStackWithCompletion:"
- "v40@0:8@16@?24@?32"
- "v52@0:8@16@24B32@36@?44"
- "\x911"
- "\xd2b\xf0\xf01"

```
