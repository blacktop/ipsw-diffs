## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1076.2.8.1.1
-  __TEXT.__text: 0xc3178
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x5bd0
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x1004
-  __TEXT.__cstring: 0x3e5c
-  __TEXT.__oslogstring: 0x18a71
+1092.3.10.1.2
+  __TEXT.__text: 0xdfa40
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_methlist: 0x6938
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x13b4
+  __TEXT.__cstring: 0x4508
+  __TEXT.__oslogstring: 0x1e19c
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x1c00
-  __TEXT.__objc_classname: 0xa9c
-  __TEXT.__objc_methname: 0x177be
-  __TEXT.__objc_methtype: 0x21a0
-  __TEXT.__objc_stubs: 0xefe0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x33c8
-  __DATA_CONST.__objc_classlist: 0x278
+  __TEXT.__unwind_info: 0x20c8
+  __TEXT.__objc_classname: 0xbe4
+  __TEXT.__objc_methname: 0x1a51c
+  __TEXT.__objc_methtype: 0x23a1
+  __TEXT.__objc_stubs: 0x10b40
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x3600
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7b98
-  __DATA_CONST.__objc_selrefs: 0x45c8
-  __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__cfstring: 0x44a0
-  __AUTH_CONST.__objc_const: 0x2250
-  __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__objc_intobj: 0xdb0
-  __AUTH_CONST.__objc_arrayobj: 0x138
+  __DATA_CONST.__objc_const: 0x8b80
+  __DATA_CONST.__objc_selrefs: 0x4d70
+  __DATA_CONST.__objc_arraydata: 0x1d0
+  __AUTH_CONST.__objc_const: 0x27a8
+  __AUTH_CONST.__cfstring: 0x4880
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__objc_intobj: 0xf78
+  __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x468
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_classrefs: 0x680
-  __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x65c
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0x250
+  __AUTH_CONST.__auth_got: 0x488
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_classrefs: 0x6c8
+  __DATA.__objc_superrefs: 0x200
+  __DATA.__objc_ivar: 0x764
+  __DATA.__data: 0x840
+  __DATA.__bss: 0x2c8
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2641
-  Symbols:   9302
-  CStrings:  5625
+  Functions: 3039
+  Symbols:   10558
+  CStrings:  6315
 
Symbols:
+ +[HMMTRAccessControl logCategory]
+ +[HMMTRAccessoryConnectionRequest logCategory]
+ +[HMMTRAccessoryConnectionRequest shortDescription]
+ +[HMMTRFabric logCategory]
+ +[HMMTRFabricConnectionRequest logCategory]
+ +[HMMTRFabricConnectionRequest shortDescription]
+ +[HMMTRFanControl logCategory]
+ +[HMMTRFeatures disableFeatureiPhoneOnlyPairingControlForTests]
+ +[HMMTRFeatures enableFeatureiPhoneOnlyPairingControlForTests]
+ +[HMMTRFeatures unsetFeatureiPhoneOnlyPairingControlForTests]
+ +[HMMTRStorage checkAndUpdateExpiryOfCertificate:keyPair:newCertificate:]
+ +[HMMTRSyncClusterColorControl logCategory]
+ +[HMMTRSyncClusterFanControl logCategory]
+ +[HMMTRThreadRadioManager logCategory]
+ +[HMMTRUtilities isValidCATSubject:]
+ -[HMMTRAccessControl .cxx_destruct]
+ -[HMMTRAccessControl attributeDescriptions]
+ -[HMMTRAccessControl currentUserPrivilege]
+ -[HMMTRAccessControl fabric]
+ -[HMMTRAccessControl handleRegularUserAdded]
+ -[HMMTRAccessControl handleSharedAdminAdded]
+ -[HMMTRAccessControl logIdentifier]
+ -[HMMTRAccessControl setCurrentUserPrivilege:]
+ -[HMMTRAccessControl setFabric:]
+ -[HMMTRAccessoryConnectionRequest .cxx_destruct]
+ -[HMMTRAccessoryConnectionRequest _getAllPendingOperations]
+ -[HMMTRAccessoryConnectionRequest _kickIdleTimer]
+ -[HMMTRAccessoryConnectionRequest _numPendingOperations]
+ -[HMMTRAccessoryConnectionRequest _restartConnectionIdleTimer:]
+ -[HMMTRAccessoryConnectionRequest abortAllPendingOperations:]
+ -[HMMTRAccessoryConnectionRequest attributeDescriptions]
+ -[HMMTRAccessoryConnectionRequest connectionIdleTime]
+ -[HMMTRAccessoryConnectionRequest connectionPriority]
+ -[HMMTRAccessoryConnectionRequest executeAllPendingOperations]
+ -[HMMTRAccessoryConnectionRequest fabricID]
+ -[HMMTRAccessoryConnectionRequest hasPendingHighPriorityConnectionRequest]
+ -[HMMTRAccessoryConnectionRequest hash]
+ -[HMMTRAccessoryConnectionRequest idleTimer]
+ -[HMMTRAccessoryConnectionRequest initWithQueue:server:highPriority:completion:]
+ -[HMMTRAccessoryConnectionRequest isEqual:]
+ -[HMMTRAccessoryConnectionRequest logIdentifier]
+ -[HMMTRAccessoryConnectionRequest mergeAccessoryConnectionRequest:]
+ -[HMMTRAccessoryConnectionRequest nodeID]
+ -[HMMTRAccessoryConnectionRequest parentFabricRequest]
+ -[HMMTRAccessoryConnectionRequest privateDescription]
+ -[HMMTRAccessoryConnectionRequest server]
+ -[HMMTRAccessoryConnectionRequest setConnectionIdleTime:]
+ -[HMMTRAccessoryConnectionRequest setConnectionPriority:]
+ -[HMMTRAccessoryConnectionRequest setParentFabricRequest:]
+ -[HMMTRAccessoryConnectionRequest setServer:]
+ -[HMMTRAccessoryConnectionRequest timerDidFire:]
+ -[HMMTRAccessoryConnectionRequest updateConnectionIdleTime:]
+ -[HMMTRAccessoryConnectionRequest workQueue]
+ -[HMMTRAccessoryServer _continueNetworkProvisioning]
+ -[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]
+ -[HMMTRAccessoryServer _removeSharedAdminControllerNodeIDFromACLWithCompletion:]
+ -[HMMTRAccessoryServer characteristicsOperationDispatchQueue]
+ -[HMMTRAccessoryServer delayDiscovery]
+ -[HMMTRAccessoryServer eMACAddress]
+ -[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]
+ -[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]
+ -[HMMTRAccessoryServer isWEDDevice]
+ -[HMMTRAccessoryServer mergeExistingAclEntries:withAdminNodes:regularUserNodes:]
+ -[HMMTRAccessoryServer mergeExistingAclEntries:withNewNodes:withPrivilege:]
+ -[HMMTRAccessoryServer objectID]
+ -[HMMTRAccessoryServer removeNode:withPrivilge:fromExistingAclEntries:]
+ -[HMMTRAccessoryServer setDelayDiscovery:]
+ -[HMMTRAccessoryServer setEMACAddress:]
+ -[HMMTRAccessoryServer setWedDevice:]
+ -[HMMTRAccessoryServer setupThreadPairing]
+ -[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]
+ -[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]
+ -[HMMTRAccessoryServer(DiagnosticsInternal) _getOperationalHardwareAddressFromReadValue:]
+ -[HMMTRAccessoryServer(DiagnosticsInternal) _getOperationalNetworkAddressForAccessory:]
+ -[HMMTRAccessoryServerBrowser _abortAllOperationsForFabricID:]
+ -[HMMTRAccessoryServerBrowser _addToActiveFabrics:]
+ -[HMMTRAccessoryServerBrowser _addToPendingFabrics:]
+ -[HMMTRAccessoryServerBrowser _connectPendingFabricConnections]
+ -[HMMTRAccessoryServerBrowser _disconnectFromIdleFabric:]
+ -[HMMTRAccessoryServerBrowser _establishConnectionWhenAllowedWithAccessoryConnectionRequest:]
+ -[HMMTRAccessoryServerBrowser _establishConnectionWhenAllowedWithFabricConnectionRequest:]
+ -[HMMTRAccessoryServerBrowser _removeFromActiveFabrics:]
+ -[HMMTRAccessoryServerBrowser _removeFromPendingFabrics:]
+ -[HMMTRAccessoryServerBrowser _restartDiscovery]
+ -[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]
+ -[HMMTRAccessoryServerBrowser _stopSystemCommissionerFabricID:]
+ -[HMMTRAccessoryServerBrowser _suspendOperationsForFabricID:]
+ -[HMMTRAccessoryServerBrowser _tryAddAccessoryConnectionRequestToExistingFabric:]
+ -[HMMTRAccessoryServerBrowser _updateACLOnPairedAccessories]
+ -[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]
+ -[HMMTRAccessoryServerBrowser abortOperationsForAccessoryServer:]
+ -[HMMTRAccessoryServerBrowser addFabricWithActiveClientForFabricID:]
+ -[HMMTRAccessoryServerBrowser appleHomeFabricWithID:]
+ -[HMMTRAccessoryServerBrowser connectToAccessoryWhenAllowed:highPriority:completion:]
+ -[HMMTRAccessoryServerBrowser currentFabric]
+ -[HMMTRAccessoryServerBrowser didFinishPairingAccessoryServer:operationDisabled:]
+ -[HMMTRAccessoryServerBrowser fabricsWithActiveClients]
+ -[HMMTRAccessoryServerBrowser fabricsWithActiveConnections]
+ -[HMMTRAccessoryServerBrowser fabricsWithPendingConnections]
+ -[HMMTRAccessoryServerBrowser fetchCachedOperationalCertificateForFabricID:completionHandler:]
+ -[HMMTRAccessoryServerBrowser fetchOperationalCertificatesFromResidentForPublicKey:fabricID:completionHandler:]
+ -[HMMTRAccessoryServerBrowser getNOCFromResidentForSharedUserForFabric:]
+ -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabric:]
+ -[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabric:]
+ -[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]
+ -[HMMTRAccessoryServerBrowser handleThreadRadioStateChanged]
+ -[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]
+ -[HMMTRAccessoryServerBrowser isCurrentDeviceAllowedAccessoryControlDespiteReachableResidentForFabric:]
+ -[HMMTRAccessoryServerBrowser isCurrentDeviceMobileAndAllowedAccessoryControl]
+ -[HMMTRAccessoryServerBrowser isCurrentDeviceMobileAndResidentReachable]
+ -[HMMTRAccessoryServerBrowser isOwnerForHomeWithFabric:]
+ -[HMMTRAccessoryServerBrowser nodesWithPendingACLOverwrite]
+ -[HMMTRAccessoryServerBrowser operationsCompletedForFabricConnectionRequest:]
+ -[HMMTRAccessoryServerBrowser operationsStartedForFabricConnectionRequest:]
+ -[HMMTRAccessoryServerBrowser preventThreadStopDuringStackRestart]
+ -[HMMTRAccessoryServerBrowser restartDiscovery]
+ -[HMMTRAccessoryServerBrowser setFabricsWithActiveClients:]
+ -[HMMTRAccessoryServerBrowser setNodesWithPendingACLOverwrite:]
+ -[HMMTRAccessoryServerBrowser setPreventThreadStopDuringStackRestart:]
+ -[HMMTRAccessoryServerBrowser threadRadioManager]
+ -[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]
+ -[HMMTRCachedFabricCertificateData .cxx_destruct]
+ -[HMMTRCachedFabricCertificateData fabricID]
+ -[HMMTRCachedFabricCertificateData initWithFabricID:rootCert:operationalCert:ownerNode:ipk:]
+ -[HMMTRCachedFabricCertificateData ipk]
+ -[HMMTRCachedFabricCertificateData operationalCert]
+ -[HMMTRCachedFabricCertificateData ownerNode]
+ -[HMMTRCachedFabricCertificateData rootCert]
+ -[HMMTRColorControl moveToCustomColorTemperatureValue:fromColorTemperature:transitionTime:completionHandler:]
+ -[HMMTRColorControl moveToPluginColorTemperatureWithParams:completionHandler:]
+ -[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]
+ -[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]
+ -[HMMTRColorControl readStartUpColorTemperatureWithCompletion:]
+ -[HMMTRColorControl stopMoveToColorTemperatureCommandWithCompletion:]
+ -[HMMTRColorControl subscribeAttributeReportForColorModeWithCompletion:]
+ -[HMMTRColorControl supportsColorTemperature:]
+ -[HMMTRColorControl writeStartUpColorTemperature:completion:]
+ -[HMMTRColorControlColorTemperatureAttributes .cxx_destruct]
+ -[HMMTRColorControlColorTemperatureAttributes colorMode]
+ -[HMMTRColorControlColorTemperatureAttributes colorTemperatureMireds]
+ -[HMMTRColorControlColorTemperatureAttributes remainingTime]
+ -[HMMTRColorControlColorTemperatureAttributes setColorMode:]
+ -[HMMTRColorControlColorTemperatureAttributes setColorTemperatureMireds:]
+ -[HMMTRColorControlColorTemperatureAttributes setRemainingTime:]
+ -[HMMTRColorControlColorTemperatureAttributes shortDescription]
+ -[HMMTRFabric .cxx_destruct]
+ -[HMMTRFabric accessControl]
+ -[HMMTRFabric attributeDescriptions]
+ -[HMMTRFabric delegate]
+ -[HMMTRFabric fabricID]
+ -[HMMTRFabric initSystemCommissionerFabricWithDelegate:]
+ -[HMMTRFabric initWithDelegate:]
+ -[HMMTRFabric isSystemCommissionerFabric]
+ -[HMMTRFabric logIdentifier]
+ -[HMMTRFabric setAccessControl:]
+ -[HMMTRFabric setFabricID:]
+ -[HMMTRFabric setStorage:]
+ -[HMMTRFabric storage]
+ -[HMMTRFabricConnectionRequest .cxx_destruct]
+ -[HMMTRFabricConnectionRequest _addToActiveIPConnections:]
+ -[HMMTRFabricConnectionRequest _addToActiveThreadConnections:]
+ -[HMMTRFabricConnectionRequest _addToActiveThreadWEDConnections:]
+ -[HMMTRFabricConnectionRequest _addToPendingConnections:]
+ -[HMMTRFabricConnectionRequest _calculateFabricIdleTime]
+ -[HMMTRFabricConnectionRequest _connectPendingConnections]
+ -[HMMTRFabricConnectionRequest _hasActiveAccessoryConnections]
+ -[HMMTRFabricConnectionRequest _kickIdleTimer]
+ -[HMMTRFabricConnectionRequest _removeFromActiveIPConnections:]
+ -[HMMTRFabricConnectionRequest _removeFromActiveThreadConnections:]
+ -[HMMTRFabricConnectionRequest _removeFromActiveThreadWEDConnections:]
+ -[HMMTRFabricConnectionRequest _removeFromPendingConnections:]
+ -[HMMTRFabricConnectionRequest _restartConnectionIdleTimer:]
+ -[HMMTRFabricConnectionRequest _tryMergeIntoExistingConnection:]
+ -[HMMTRFabricConnectionRequest _updateActiveThreadWEDConnectionsIdleTime:]
+ -[HMMTRFabricConnectionRequest _updateConnectionIdleTime:]
+ -[HMMTRFabricConnectionRequest abortAllOperations]
+ -[HMMTRFabricConnectionRequest abortOperationsForConnectionRequest:]
+ -[HMMTRFabricConnectionRequest activeIPConnectionRequests]
+ -[HMMTRFabricConnectionRequest activeThreadConnectionRequests]
+ -[HMMTRFabricConnectionRequest activeThreadWEDConnectionRequests]
+ -[HMMTRFabricConnectionRequest active]
+ -[HMMTRFabricConnectionRequest attributeDescriptions]
+ -[HMMTRFabricConnectionRequest browser]
+ -[HMMTRFabricConnectionRequest connectToAccessoryWhenAllowed:]
+ -[HMMTRFabricConnectionRequest fabricID]
+ -[HMMTRFabricConnectionRequest fabricIdleTime]
+ -[HMMTRFabricConnectionRequest hasPendingHighPriorityConnectionRequest]
+ -[HMMTRFabricConnectionRequest hash]
+ -[HMMTRFabricConnectionRequest idleTimer]
+ -[HMMTRFabricConnectionRequest initWithQueue:browser:fabricID:systemCommissionerFabric:]
+ -[HMMTRFabricConnectionRequest isEqual:]
+ -[HMMTRFabricConnectionRequest logIdentifier]
+ -[HMMTRFabricConnectionRequest operationsCompletedForAccessoryConnectionRequest:]
+ -[HMMTRFabricConnectionRequest pendingConnectionRequests]
+ -[HMMTRFabricConnectionRequest privateDescription]
+ -[HMMTRFabricConnectionRequest retryOperations]
+ -[HMMTRFabricConnectionRequest setActive:]
+ -[HMMTRFabricConnectionRequest setFabricIdleTime:]
+ -[HMMTRFabricConnectionRequest startOperations]
+ -[HMMTRFabricConnectionRequest stopOperations]
+ -[HMMTRFabricConnectionRequest suspendOperations]
+ -[HMMTRFabricConnectionRequest systemCommissionerFabric]
+ -[HMMTRFabricConnectionRequest timerDidFire:]
+ -[HMMTRFabricConnectionRequest workQueue]
+ -[HMMTRFanControl readAttributePluginRockSettingWithCompletionHandler:]
+ -[HMMTRFanControl updatedValuePluginRockSettingForAttributeReport:responseHandler:]
+ -[HMMTRFanControl writeAttributePluginRockSettingWithValue:completionHandler:]
+ -[HMMTRProtocolOperationManager _queryColorModeFromClusterAtCHIPEndpoint:device:callbackQueue:completionHandler:]
+ -[HMMTRResidentStateManager delegate]
+ -[HMMTRResidentStateManager handleResidentReachabilityChangeForFabric:]
+ -[HMMTRResidentStateManager handleUpdateNotificationsEnabled:forFabric:]
+ -[HMMTRResidentStateManager setDelegate:]
+ -[HMMTRStorage _cachedRootCertificateIfValidForFabricID:]
+ -[HMMTRStorage _createTransientOperationalCertificateForFabricID:]
+ -[HMMTRStorage _fetchCert2ForFabricWithID:isOwner:completion:]
+ -[HMMTRStorage _fetchOperationalCertificatesFromResidentForFabricID:completion:]
+ -[HMMTRStorage _fetchSharedUserCert2ForFabricWithID:reFetch:completion:]
+ -[HMMTRStorage _operationalCertificateFromSdkCertificatesForFabricID:]
+ -[HMMTRStorage _rootCertificateFromSdkCertificatesForFabricID:]
+ -[HMMTRStorage caseAuthenticatedTag]
+ -[HMMTRStorage caseAuthenticatedTagsUpdated]
+ -[HMMTRStorage fetchSharedUserCertForFabricWithID:reFetch:completion:]
+ -[HMMTRStorage isFabricCreationInProgress]
+ -[HMMTRStorage legacyNodeIDForCurrentFabric]
+ -[HMMTRStorage persistLegacyControllerNodeWithDictionary:]
+ -[HMMTRStorage setCaseAuthenticatedTag:]
+ -[HMMTRStorage setCaseAuthenticatedTagsUpdated:]
+ -[HMMTRStorage setFabricCreationInProgress:]
+ -[HMMTRSyncClusterColorControl moveToPluginColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:]
+ -[HMMTRSyncClusterColorControl readAttributePluginColorTemperatureMiredsWithParams:]
+ -[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:]
+ -[HMMTRSyncClusterDoorLock baseDoorLock]
+ -[HMMTRSyncClusterDoorLock setBaseDoorLock:]
+ -[HMMTRSyncClusterFanControl readAttributePluginRockSettingWithParams:]
+ -[HMMTRSyncClusterFanControl updatedValuePluginRockSettingForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterFanControl writeAttributePluginRockSettingWithValue:expectedValueInterval:]
+ -[HMMTRSystemCommissionerControllerParams _checkAndUpdateValidityPeriodOfV1Keypair:newKeyPair:]
+ -[HMMTRThreadRadioManager .cxx_destruct]
+ -[HMMTRThreadRadioManager _retryWEDConnectionToAccessory]
+ -[HMMTRThreadRadioManager _updateFabricIDOfActiveThreadNetwork:isFabricIDOfSystemCommissioner:]
+ -[HMMTRThreadRadioManager allowDisconnect]
+ -[HMMTRThreadRadioManager browser]
+ -[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:completion:]
+ -[HMMTRThreadRadioManager delegate]
+ -[HMMTRThreadRadioManager deviceSupportsThreadService]
+ -[HMMTRThreadRadioManager eMACAddressOfWEDAccessory]
+ -[HMMTRThreadRadioManager fabricIDOfActiveThreadNetwork]
+ -[HMMTRThreadRadioManager initWithBrowser:]
+ -[HMMTRThreadRadioManager isPairingActive]
+ -[HMMTRThreadRadioManager isReadyToEstablishWEDConnection]
+ -[HMMTRThreadRadioManager isThreadNetworkConnected]
+ -[HMMTRThreadRadioManager isWEDConnectionRetryActive]
+ -[HMMTRThreadRadioManager lastKnownThreadNetworkConnectionState]
+ -[HMMTRThreadRadioManager notifyThreadRadioStateChanged:nodeType:]
+ -[HMMTRThreadRadioManager notifyWakeOnDeviceConnectionChanged:eMACAddress:]
+ -[HMMTRThreadRadioManager pendingThreadStart]
+ -[HMMTRThreadRadioManager preventDisconnect]
+ -[HMMTRThreadRadioManager retryConnectionQueue]
+ -[HMMTRThreadRadioManager setBrowser:]
+ -[HMMTRThreadRadioManager setDelegate:]
+ -[HMMTRThreadRadioManager setDeviceSupportsThreadService:]
+ -[HMMTRThreadRadioManager setEMACAddressOfWEDAccessory:]
+ -[HMMTRThreadRadioManager setFabricIDOfActiveThreadNetwork:]
+ -[HMMTRThreadRadioManager setIsPairingActive:]
+ -[HMMTRThreadRadioManager setIsWEDConnectionRetryActive:]
+ -[HMMTRThreadRadioManager setLastKnownThreadNetworkConnectionState:]
+ -[HMMTRThreadRadioManager setPendingThreadStart:]
+ -[HMMTRThreadRadioManager setPreventDisconnect:]
+ -[HMMTRThreadRadioManager setRetryConnectionQueue:]
+ -[HMMTRThreadRadioManager setThreadNetworkActivatedForSystemCommissionerFabric:]
+ -[HMMTRThreadRadioManager startAccessoryPairingWithExtendedMACAddress:isWedDevice:completion:]
+ -[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricID:]
+ -[HMMTRThreadRadioManager startThreadRadioForHomeWithFabricID:preventDisconnect:]
+ -[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricID:]
+ -[HMMTRThreadRadioManager stopAccessoryPairingWithCompletion:]
+ -[HMMTRThreadRadioManager stopThreadRadioForHomeWithFabricID:]
+ -[HMMTRThreadRadioManager stopThreadRadioForSystemCommissionerFabricID:]
+ -[HMMTRThreadRadioManager threadNetworkActivatedForSystemCommissionerFabric]
+ GCC_except_table1043
+ GCC_except_table1044
+ GCC_except_table1062
+ GCC_except_table1063
+ GCC_except_table1064
+ GCC_except_table1065
+ GCC_except_table1066
+ GCC_except_table1069
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1075
+ GCC_except_table1076
+ GCC_except_table1077
+ GCC_except_table1198
+ GCC_except_table1247
+ GCC_except_table1269
+ GCC_except_table1312
+ GCC_except_table1357
+ GCC_except_table1530
+ GCC_except_table1534
+ GCC_except_table1591
+ GCC_except_table1644
+ GCC_except_table1686
+ GCC_except_table1706
+ GCC_except_table1707
+ GCC_except_table1718
+ GCC_except_table1719
+ GCC_except_table1720
+ GCC_except_table1721
+ GCC_except_table1722
+ GCC_except_table1723
+ GCC_except_table1724
+ GCC_except_table1730
+ GCC_except_table1732
+ GCC_except_table1736
+ GCC_except_table1754
+ GCC_except_table1768
+ GCC_except_table1774
+ GCC_except_table1785
+ GCC_except_table1787
+ GCC_except_table1795
+ GCC_except_table1811
+ GCC_except_table1817
+ GCC_except_table1824
+ GCC_except_table2157
+ GCC_except_table2162
+ GCC_except_table2165
+ GCC_except_table2225
+ GCC_except_table2239
+ GCC_except_table2241
+ GCC_except_table2248
+ GCC_except_table2249
+ GCC_except_table2274
+ GCC_except_table2275
+ GCC_except_table2309
+ GCC_except_table2349
+ GCC_except_table2381
+ GCC_except_table2385
+ GCC_except_table2401
+ GCC_except_table2402
+ GCC_except_table2426
+ GCC_except_table243
+ GCC_except_table2493
+ GCC_except_table2529
+ GCC_except_table2537
+ GCC_except_table2552
+ GCC_except_table2586
+ GCC_except_table2587
+ GCC_except_table2592
+ GCC_except_table2600
+ GCC_except_table2714
+ GCC_except_table2719
+ GCC_except_table2813
+ GCC_except_table2816
+ GCC_except_table2940
+ GCC_except_table2959
+ GCC_except_table2963
+ GCC_except_table2966
+ GCC_except_table2991
+ GCC_except_table3013
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table515
+ GCC_except_table519
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table582
+ GCC_except_table615
+ GCC_except_table648
+ GCC_except_table695
+ GCC_except_table703
+ GCC_except_table729
+ GCC_except_table759
+ GCC_except_table927
+ OBJC_IVAR_$_HAPAccessoryServerBrowser._lock
+ _HMFDispatchQueueName
+ _HMMTRUserPrivilegeAsString
+ _OBJC_CLASS_$_HMMTRAccessControl
+ _OBJC_CLASS_$_HMMTRAccessoryConnectionRequest
+ _OBJC_CLASS_$_HMMTRCachedFabricCertificateData
+ _OBJC_CLASS_$_HMMTRColorControlColorTemperatureAttributes
+ _OBJC_CLASS_$_HMMTRFabric
+ _OBJC_CLASS_$_HMMTRFabricConnectionRequest
+ _OBJC_CLASS_$_HMMTRFanControl
+ _OBJC_CLASS_$_HMMTRFeatures
+ _OBJC_CLASS_$_HMMTRSyncClusterColorControl
+ _OBJC_CLASS_$_HMMTRSyncClusterFanControl
+ _OBJC_CLASS_$_HMMTRThreadRadioManager
+ _OBJC_CLASS_$_MTRBaseClusterFanControl
+ _OBJC_CLASS_$_MTRClusterColorControl
+ _OBJC_CLASS_$_MTRClusterFanControl
+ _OBJC_CLASS_$_MTRColorControlClusterStopMoveStepParams
+ _OBJC_CLASS_$_MTRSubscribeParams
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_IVAR_$_HMMTRAccessControl._currentUserPrivilege
+ _OBJC_IVAR_$_HMMTRAccessControl._fabric
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._connectionIdleTime
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._connectionPriority
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._fabricID
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._idleTimer
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._lock
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._nodeID
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._parentFabricRequest
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._pendingOperations
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._server
+ _OBJC_IVAR_$_HMMTRAccessoryConnectionRequest._workQueue
+ _OBJC_IVAR_$_HMMTRAccessoryServer._characteristicsOperationDispatchQueue
+ _OBJC_IVAR_$_HMMTRAccessoryServer._delayDiscovery
+ _OBJC_IVAR_$_HMMTRAccessoryServer._eMACAddress
+ _OBJC_IVAR_$_HMMTRAccessoryServer._objectID
+ _OBJC_IVAR_$_HMMTRAccessoryServer._wedDevice
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._fabricsWithActiveClients
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._fabricsWithActiveConnections
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._fabricsWithPendingConnections
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._nodesWithPendingACLOverwrite
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._preventThreadStopDuringStackRestart
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._threadRadioManager
+ _OBJC_IVAR_$_HMMTRCachedFabricCertificateData._fabricID
+ _OBJC_IVAR_$_HMMTRCachedFabricCertificateData._ipk
+ _OBJC_IVAR_$_HMMTRCachedFabricCertificateData._operationalCert
+ _OBJC_IVAR_$_HMMTRCachedFabricCertificateData._ownerNode
+ _OBJC_IVAR_$_HMMTRCachedFabricCertificateData._rootCert
+ _OBJC_IVAR_$_HMMTRColorControlColorTemperatureAttributes._colorMode
+ _OBJC_IVAR_$_HMMTRColorControlColorTemperatureAttributes._colorTemperatureMireds
+ _OBJC_IVAR_$_HMMTRColorControlColorTemperatureAttributes._remainingTime
+ _OBJC_IVAR_$_HMMTRFabric._accessControl
+ _OBJC_IVAR_$_HMMTRFabric._delegate
+ _OBJC_IVAR_$_HMMTRFabric._fabricID
+ _OBJC_IVAR_$_HMMTRFabric._storage
+ _OBJC_IVAR_$_HMMTRFabric._systemCommissionerFabric
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._active
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._activeIPConnectionRequests
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._activeThreadConnectionRequests
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._activeThreadWEDConnectionRequests
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._browser
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._fabricID
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._fabricIdleTime
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._idleTimer
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._lock
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._pendingConnectionRequests
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._systemCommissionerFabric
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._workQueue
+ _OBJC_IVAR_$_HMMTRResidentStateManager._delegate
+ _OBJC_IVAR_$_HMMTRStorage._caseAuthenticatedTag
+ _OBJC_IVAR_$_HMMTRStorage._caseAuthenticatedTagsUpdated
+ _OBJC_IVAR_$_HMMTRStorage._fabricCreationInProgress
+ _OBJC_IVAR_$_HMMTRSyncClusterDoorLock._baseDoorLock
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._browser
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._delegate
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._deviceSupportsThreadService
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._eMACAddressOfWEDAccessory
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._fabricIDOfActiveThreadNetwork
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._isPairingActive
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._isWEDConnectionRetryActive
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._lastKnownThreadNetworkConnectionState
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._lock
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._pendingThreadStart
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._preventDisconnect
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._retryConnectionQueue
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._threadNetworkActivatedForSystemCommissionerFabric
+ _OBJC_METACLASS_$_HMMTRAccessControl
+ _OBJC_METACLASS_$_HMMTRAccessoryConnectionRequest
+ _OBJC_METACLASS_$_HMMTRCachedFabricCertificateData
+ _OBJC_METACLASS_$_HMMTRColorControlColorTemperatureAttributes
+ _OBJC_METACLASS_$_HMMTRFabric
+ _OBJC_METACLASS_$_HMMTRFabricConnectionRequest
+ _OBJC_METACLASS_$_HMMTRFanControl
+ _OBJC_METACLASS_$_HMMTRFeatures
+ _OBJC_METACLASS_$_HMMTRSyncClusterColorControl
+ _OBJC_METACLASS_$_HMMTRSyncClusterFanControl
+ _OBJC_METACLASS_$_HMMTRThreadRadioManager
+ _OBJC_METACLASS_$_MTRBaseClusterFanControl
+ _OBJC_METACLASS_$_MTRClusterColorControl
+ _OBJC_METACLASS_$_MTRClusterFanControl
+ __OBJC_$_CLASS_METHODS_HMMTRAccessControl
+ __OBJC_$_CLASS_METHODS_HMMTRAccessoryConnectionRequest
+ __OBJC_$_CLASS_METHODS_HMMTRFabric
+ __OBJC_$_CLASS_METHODS_HMMTRFabricConnectionRequest
+ __OBJC_$_CLASS_METHODS_HMMTRFanControl
+ __OBJC_$_CLASS_METHODS_HMMTRFeatures
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterColorControl
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterFanControl
+ __OBJC_$_CLASS_METHODS_HMMTRThreadRadioManager
+ __OBJC_$_INSTANCE_METHODS_HMMTRAccessControl
+ __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryConnectionRequest
+ __OBJC_$_INSTANCE_METHODS_HMMTRCachedFabricCertificateData
+ __OBJC_$_INSTANCE_METHODS_HMMTRColorControlColorTemperatureAttributes
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabric
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricConnectionRequest
+ __OBJC_$_INSTANCE_METHODS_HMMTRFanControl
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterColorControl
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterFanControl
+ __OBJC_$_INSTANCE_METHODS_HMMTRThreadRadioManager
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAccessControl
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAccessoryConnectionRequest
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRCachedFabricCertificateData
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRColorControlColorTemperatureAttributes
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRFabric
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricConnectionRequest
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRThreadRadioManager
+ __OBJC_$_PROP_LIST_HMMTRAccessControl
+ __OBJC_$_PROP_LIST_HMMTRAccessoryConnectionRequest
+ __OBJC_$_PROP_LIST_HMMTRCachedFabricCertificateData
+ __OBJC_$_PROP_LIST_HMMTRColorControlColorTemperatureAttributes
+ __OBJC_$_PROP_LIST_HMMTRFabric
+ __OBJC_$_PROP_LIST_HMMTRFabricConnectionRequest
+ __OBJC_$_PROP_LIST_HMMTRFanControl
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterColorControl
+ __OBJC_$_PROP_LIST_HMMTRSyncClusterFanControl
+ __OBJC_$_PROP_LIST_HMMTRThreadRadioManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRResidentStateManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRResidentStateManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMTRResidentStateManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRAccessoryConnectionRequest
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRFabricConnectionRequest
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRFanControl
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterColorControl
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRSyncClusterFanControl
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRThreadRadioManager
+ __OBJC_CLASS_RO_$_HMMTRAccessControl
+ __OBJC_CLASS_RO_$_HMMTRAccessoryConnectionRequest
+ __OBJC_CLASS_RO_$_HMMTRCachedFabricCertificateData
+ __OBJC_CLASS_RO_$_HMMTRColorControlColorTemperatureAttributes
+ __OBJC_CLASS_RO_$_HMMTRFabric
+ __OBJC_CLASS_RO_$_HMMTRFabricConnectionRequest
+ __OBJC_CLASS_RO_$_HMMTRFanControl
+ __OBJC_CLASS_RO_$_HMMTRFeatures
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterColorControl
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterFanControl
+ __OBJC_CLASS_RO_$_HMMTRThreadRadioManager
+ __OBJC_LABEL_PROTOCOL_$_HMMTRResidentStateManagerDelegate
+ __OBJC_METACLASS_RO_$_HMMTRAccessControl
+ __OBJC_METACLASS_RO_$_HMMTRAccessoryConnectionRequest
+ __OBJC_METACLASS_RO_$_HMMTRCachedFabricCertificateData
+ __OBJC_METACLASS_RO_$_HMMTRColorControlColorTemperatureAttributes
+ __OBJC_METACLASS_RO_$_HMMTRFabric
+ __OBJC_METACLASS_RO_$_HMMTRFabricConnectionRequest
+ __OBJC_METACLASS_RO_$_HMMTRFanControl
+ __OBJC_METACLASS_RO_$_HMMTRFeatures
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterColorControl
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterFanControl
+ __OBJC_METACLASS_RO_$_HMMTRThreadRadioManager
+ __OBJC_PROTOCOL_$_HMMTRResidentStateManagerDelegate
+ ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.611
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.732
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.735
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.669
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.138
+ ___107-[HMMTROTAProviderDelegate handleBDXQueryForNodeID:controller:blockSize:blockIndex:bytesToSkip:completion:]_block_invoke
+ ___107-[HMMTROTAProviderDelegate handleBDXQueryForNodeID:controller:blockSize:blockIndex:bytesToSkip:completion:]_block_invoke.32
+ ___109-[HMMTRColorControl moveToCustomColorTemperatureValue:fromColorTemperature:transitionTime:completionHandler:]_block_invoke
+ ___109-[HMMTRColorControl moveToCustomColorTemperatureValue:fromColorTemperature:transitionTime:completionHandler:]_block_invoke.5
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.140
+ ___111-[HMMTRAccessoryServerBrowser fetchOperationalCertificatesFromResidentForPublicKey:fabricID:completionHandler:]_block_invoke
+ ___111-[HMMTRAccessoryServerBrowser fetchOperationalCertificatesFromResidentForPublicKey:fabricID:completionHandler:]_block_invoke_2
+ ___113-[HMMTRProtocolOperationManager _queryColorModeFromClusterAtCHIPEndpoint:device:callbackQueue:completionHandler:]_block_invoke
+ ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.103
+ ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.188
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.229
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.468
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.469
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.470
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.471
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.474
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.472
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.473
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.136
+ ___121-[HMMTRAccessoryServerBrowser stageAccessoryServerWithSetupPayload:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
+ ___126-[HMMTRSyncClusterColorControl moveToPluginColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:]_block_invoke
+ ___133-[HMMTRAccessoryServerBrowser fetchCertificatesForSharedUserWithAccessoryNodeID:sharedUserType:publicKey:fabricID:completionHandler:]_block_invoke
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.87
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.89
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.92
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.96
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.169
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.171
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.173
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.174
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.175
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.176
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.177
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.178
+ ___227-[HMMTRAccessoryServerBrowser stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completionHandler:]_block_invoke
+ ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
+ ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.122
+ ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke_2
+ ___26+[HMMTRFabric logCategory]_block_invoke
+ ___30+[HMMTRFanControl logCategory]_block_invoke
+ ___33+[HMMTRAccessControl logCategory]_block_invoke
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.566
+ ___38+[HMMTRThreadRadioManager logCategory]_block_invoke
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.278
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.280
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.282
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.555
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.556
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.557
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.558
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.559
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.560
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.561
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.562
+ ___40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.40
+ ___41+[HMMTRSyncClusterFanControl logCategory]_block_invoke
+ ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke
+ ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.430
+ ___42-[HMMTRStorage prepareStorageForFabricID:]_block_invoke.35
+ ___43+[HMMTRFabricConnectionRequest logCategory]_block_invoke
+ ___43+[HMMTRSyncClusterColorControl logCategory]_block_invoke
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.270
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.273
+ ___43-[HMMTRControllerWrapper _revokeAvailable:]_block_invoke_2
+ ___45-[HMMTRAccessoryServer _disconnectWithError:]_block_invoke
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.716
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.623
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.630
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.259
+ ___45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.41
+ ___46+[HMMTRAccessoryConnectionRequest logCategory]_block_invoke
+ ___46-[HMMTRColorControl supportsColorTemperature:]_block_invoke
+ ___46-[HMMTRFabricConnectionRequest stopOperations]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.771
+ ___47-[HMMTRAccessoryServerBrowser restartDiscovery]_block_invoke
+ ___47-[HMMTRFabricConnectionRequest retryOperations]_block_invoke
+ ___47-[HMMTRFabricConnectionRequest startOperations]_block_invoke
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.246
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.247
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke_2.248
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.693
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.697
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.696
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.743
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.744
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.745
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke_3
+ ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.167
+ ___49-[HMMTRFabricConnectionRequest suspendOperations]_block_invoke
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.649
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.653
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.654
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke_2
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.772
+ ___52-[HMMTRAccessoryServer _continueNetworkProvisioning]_block_invoke
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.154
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.155
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.223
+ ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.647
+ ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.648
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.567
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.572
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.770
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.394
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.395
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.396
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.397
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.398
+ ___56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.38
+ ___57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.86
+ ___57-[HMMTRThreadRadioManager _retryWEDConnectionToAccessory]_block_invoke
+ ___57-[HMMTRThreadRadioManager _retryWEDConnectionToAccessory]_block_invoke.3
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.404
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.405
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.406
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.407
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.408
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.736
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.738
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.740
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.741
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.399
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.400
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.401
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.402
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.403
+ ___60-[HMMTRAccessoryServerBrowser _updateACLOnPairedAccessories]_block_invoke
+ ___60-[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabric:]_block_invoke
+ ___60-[HMMTRStorage fetchCertForFabricWithID:isOwner:completion:]_block_invoke_3
+ ___61-[HMMTRColorControl writeStartUpColorTemperature:completion:]_block_invoke
+ ___61-[HMMTRStorage _fetchCertForFabricWithID:isOwner:completion:]_block_invoke.61
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.115
+ ___62-[HMMTRFabricConnectionRequest connectToAccessoryWhenAllowed:]_block_invoke
+ ___62-[HMMTRStorage _fetchCert2ForFabricWithID:isOwner:completion:]_block_invoke
+ ___62-[HMMTRStorage _fetchCert2ForFabricWithID:isOwner:completion:]_block_invoke.63
+ ___62-[HMMTRThreadRadioManager stopAccessoryPairingWithCompletion:]_block_invoke
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.447
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.448
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.449
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.450
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.453
+ ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.112
+ ___63-[HMMTRColorControl readStartUpColorTemperatureWithCompletion:]_block_invoke
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.413
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.414
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.415
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.417
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.90
+ ___65-[HMMTRAccessoryServerBrowser abortOperationsForAccessoryServer:]_block_invoke
+ ___65-[HMMTRAccessoryServerBrowser abortOperationsForAccessoryServer:]_block_invoke_2
+ ___65-[HMMTRFabricConnectionRequest _addToActiveThreadWEDConnections:]_block_invoke
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.409
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.410
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.411
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.412
+ ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.289
+ ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.202
+ ___66-[HMMTRThreadRadioManager notifyThreadRadioStateChanged:nodeType:]_block_invoke
+ ___68-[HMMTRAccessoryServerBrowser addFabricWithActiveClientForFabricID:]_block_invoke
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.436
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.437
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.438
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.439
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.442
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.446
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.386
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.392
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.393
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.116
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.117
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.120
+ ___69-[HMMTRColorControl stopMoveToColorTemperatureCommandWithCompletion:]_block_invoke
+ ___70-[HMMTRFabricConnectionRequest _removeFromActiveThreadWEDConnections:]_block_invoke
+ ___70-[HMMTRStorage fetchSharedUserCertForFabricWithID:reFetch:completion:]_block_invoke
+ ___70-[HMMTRStorage fetchSharedUserCertForFabricWithID:reFetch:completion:]_block_invoke_2
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.243
+ ___71-[HMMTRFanControl readAttributePluginRockSettingWithCompletionHandler:]_block_invoke
+ ___71-[HMMTRFanControl readAttributePluginRockSettingWithCompletionHandler:]_block_invoke.1
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.374
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.379
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.380
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.418
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.419
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.420
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.422
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.424
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.425
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.426
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.427
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.428
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.429
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.431
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.432
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.433
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.434
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.435
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke_2
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.234
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.235
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.236
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.238
+ ___72-[HMMTRAccessoryServerBrowser getNOCFromResidentForSharedUserForFabric:]_block_invoke
+ ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke
+ ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke_2
+ ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke_3
+ ___72-[HMMTRColorControl readColorTemperatureAttributesWithCompletion:queue:]_block_invoke_4
+ ___72-[HMMTRColorControl subscribeAttributeReportForColorModeWithCompletion:]_block_invoke
+ ___72-[HMMTRStorage _fetchSharedUserCert2ForFabricWithID:reFetch:completion:]_block_invoke
+ ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.79
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.643
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.644
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.646
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.645
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.631
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.632
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.639
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.640
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.642
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.633
+ ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.164
+ ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.165
+ ___73-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabric:]_block_invoke
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.206
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.207
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke_2
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke_3
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.702
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.703
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.707
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.208
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.209
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.210
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.211
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_2
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_3
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_4
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_5
+ ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.68
+ ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.72
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.262
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.263
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.264
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.265
+ ___78-[HMMTRColorControl moveToPluginColorTemperatureWithParams:completionHandler:]_block_invoke
+ ___78-[HMMTRFanControl writeAttributePluginRockSettingWithValue:completionHandler:]_block_invoke
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.750
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.751
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.381
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.382
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.383
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.385
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.163
+ ___79-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:]_block_invoke
+ ___79-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:]_block_invoke.111
+ ___79-[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:completion:]_block_invoke
+ ___80-[HMMTRAccessoryServer _removeSharedAdminControllerNodeIDFromACLWithCompletion:]_block_invoke
+ ___80-[HMMTRStorage _fetchOperationalCertificatesFromResidentForFabricID:completion:]_block_invoke
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.159
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.160
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.162
+ ___81-[HMMTRAccessoryServerBrowser didFinishPairingAccessoryServer:operationDisabled:]_block_invoke
+ ___81-[HMMTRFabricConnectionRequest operationsCompletedForAccessoryConnectionRequest:]_block_invoke
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.101
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.103
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.670
+ ___83-[HMMTRFanControl updatedValuePluginRockSettingForAttributeReport:responseHandler:]_block_invoke
+ ___83-[HMMTRThermostat readAttributePluginTargetHeaterCoolerStateWithCompletionHandler:]_block_invoke.42
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.344
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.345
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.347
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.720
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.721
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.722
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.723
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.726
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.727
+ ___84-[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]_block_invoke
+ ___84-[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]_block_invoke.14
+ ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.37
+ ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.38
+ ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.39
+ ___85-[HMMTRAccessoryServerBrowser connectToAccessoryWhenAllowed:highPriority:completion:]_block_invoke
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.250
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.251
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.476
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.477
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.478
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.479
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.481
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.480
+ ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke
+ ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.203
+ ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.204
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.668
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.109
+ ___94-[HMMTRAccessoryServerBrowser fetchCachedOperationalCertificateForFabricID:completionHandler:]_block_invoke
+ ___94-[HMMTRThreadRadioManager startAccessoryPairingWithExtendedMACAddress:isWedDevice:completion:]_block_invoke
+ ___98-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:]_block_invoke.168
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.226
+ ___Block_byref_object_copy_.1811
+ ___Block_byref_object_copy_.2084
+ ___Block_byref_object_copy_.2906
+ ___Block_byref_object_copy_.4147
+ ___Block_byref_object_copy_.4413
+ ___Block_byref_object_copy_.4721
+ ___Block_byref_object_copy_.5323
+ ___Block_byref_object_copy_.5789
+ ___Block_byref_object_copy_.6244
+ ___Block_byref_object_copy_.6860
+ ___Block_byref_object_copy_.7365
+ ___Block_byref_object_copy_.8059
+ ___Block_byref_object_copy_.8270
+ ___Block_byref_object_dispose_.1812
+ ___Block_byref_object_dispose_.2085
+ ___Block_byref_object_dispose_.2907
+ ___Block_byref_object_dispose_.4148
+ ___Block_byref_object_dispose_.4414
+ ___Block_byref_object_dispose_.4722
+ ___Block_byref_object_dispose_.5324
+ ___Block_byref_object_dispose_.5790
+ ___Block_byref_object_dispose_.6245
+ ___Block_byref_object_dispose_.6861
+ ___Block_byref_object_dispose_.7366
+ ___Block_byref_object_dispose_.8060
+ ___Block_byref_object_dispose_.8271
+ ___block_descriptor_40_e8_32bs_e42_v16?0"HMMTRCachedFabricCertificateData"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSNumber"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e35_B20?0"HMMTRControllerWrapper"8B16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e30_v24?0"NSNumber"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e63_v48?0"NSData"8"NSData"16"NSNumber"24"NSData"32"NSError"40ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e30_v24?0"NSNumber"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_57_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s56l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e30_v24?0"NSNumber"8"NSError"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e42_v16?0"HMMTRCachedFabricCertificateData"8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e17_v16?0"NSError"8ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e16_"HMFFuture"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e44_{_HMFFutureBlockOutcome=q}16?0"NSNumber"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_97_e8_32s40s48bs56bs64bs72bs80bs88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.107
+ ___block_literal_global.1094
+ ___block_literal_global.117
+ ___block_literal_global.136.4438
+ ___block_literal_global.1373
+ ___block_literal_global.147
+ ___block_literal_global.1539
+ ___block_literal_global.1658
+ ___block_literal_global.1766
+ ___block_literal_global.1831
+ ___block_literal_global.1978
+ ___block_literal_global.198
+ ___block_literal_global.2144
+ ___block_literal_global.226
+ ___block_literal_global.2281
+ ___block_literal_global.2388
+ ___block_literal_global.256
+ ___block_literal_global.2958
+ ___block_literal_global.3289
+ ___block_literal_global.346
+ ___block_literal_global.3515
+ ___block_literal_global.3816
+ ___block_literal_global.3899
+ ___block_literal_global.3960
+ ___block_literal_global.4188
+ ___block_literal_global.4298
+ ___block_literal_global.452
+ ___block_literal_global.4539
+ ___block_literal_global.4732
+ ___block_literal_global.5085
+ ___block_literal_global.531
+ ___block_literal_global.5358
+ ___block_literal_global.5579
+ ___block_literal_global.5753
+ ___block_literal_global.6154
+ ___block_literal_global.622
+ ___block_literal_global.626
+ ___block_literal_global.626.6266
+ ___block_literal_global.629
+ ___block_literal_global.635
+ ___block_literal_global.6538
+ ___block_literal_global.68
+ ___block_literal_global.7079
+ ___block_literal_global.7271
+ ___block_literal_global.73
+ ___block_literal_global.7401
+ ___block_literal_global.7541
+ ___block_literal_global.7644
+ ___block_literal_global.773
+ ___block_literal_global.785
+ ___block_literal_global.8137
+ ___block_literal_global.862
+ ___block_literal_global.936
+ ___block_literal_global.96
+ __unnamed_array_storage.104
+ __unnamed_array_storage.112
+ __unnamed_array_storage.1183
+ __unnamed_array_storage.1518
+ __unnamed_array_storage.1967
+ __unnamed_array_storage.5276
+ __unnamed_array_storage.6895
+ __unnamed_array_storage.70
+ __unnamed_array_storage.93
+ _dispatch_get_global_queue
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create_with_target$V2
+ _isFeatureMatteriPhoneOnlyPairingControlEnabled
+ _isFeatureMatteriPhoneOnlyPairingControlEnabledForTests
+ _isFeatureMatteriPhoneOnlyPairingControlForIPEnabled
+ _isFeatureMatteriPhoneOnlyPairingControlForThreadEnabled
+ _logCategory._hmf_once_t0
+ _logCategory._hmf_once_t0.3898
+ _logCategory._hmf_once_t11
+ _logCategory._hmf_once_t11.1657
+ _logCategory._hmf_once_t123
+ _logCategory._hmf_once_t15.7643
+ _logCategory._hmf_once_t2.6153
+ _logCategory._hmf_once_t3.861
+ _logCategory._hmf_once_t3.935
+ _logCategory._hmf_once_t350
+ _logCategory._hmf_once_t4.4297
+ _logCategory._hmf_once_t47
+ _logCategory._hmf_once_t49
+ _logCategory._hmf_once_t49.3514
+ _logCategory._hmf_once_t50
+ _logCategory._hmf_once_t562
+ _logCategory._hmf_once_t59
+ _logCategory._hmf_once_t6.1830
+ _logCategory._hmf_once_t64
+ _logCategory._hmf_once_t8.2143
+ _logCategory._hmf_once_t8.5752
+ _logCategory._hmf_once_t8.7270
+ _logCategory._hmf_once_t84
+ _logCategory._hmf_once_t9
+ _logCategory._hmf_once_v1
+ _logCategory._hmf_once_v1.3900
+ _logCategory._hmf_once_v10
+ _logCategory._hmf_once_v12
+ _logCategory._hmf_once_v12.1659
+ _logCategory._hmf_once_v124
+ _logCategory._hmf_once_v16.7645
+ _logCategory._hmf_once_v3.6155
+ _logCategory._hmf_once_v351
+ _logCategory._hmf_once_v4.863
+ _logCategory._hmf_once_v4.937
+ _logCategory._hmf_once_v48
+ _logCategory._hmf_once_v5.4299
+ _logCategory._hmf_once_v50
+ _logCategory._hmf_once_v50.3516
+ _logCategory._hmf_once_v51
+ _logCategory._hmf_once_v563
+ _logCategory._hmf_once_v60
+ _logCategory._hmf_once_v65
+ _logCategory._hmf_once_v7.1832
+ _logCategory._hmf_once_v85
+ _logCategory._hmf_once_v9.2145
+ _logCategory._hmf_once_v9.5754
+ _logCategory._hmf_once_v9.7272
+ _objc_msgSend$_abortAllOperationsForFabricID:
+ _objc_msgSend$_addToActiveFabrics:
+ _objc_msgSend$_addToActiveIPConnections:
+ _objc_msgSend$_addToActiveThreadConnections:
+ _objc_msgSend$_addToActiveThreadWEDConnections:
+ _objc_msgSend$_addToPendingConnections:
+ _objc_msgSend$_addToPendingFabrics:
+ _objc_msgSend$_cachedRootCertificateIfValidForFabricID:
+ _objc_msgSend$_calculateFabricIdleTime
+ _objc_msgSend$_checkAndUpdateValidityPeriodOfV1Keypair:newKeyPair:
+ _objc_msgSend$_connectPendingConnections
+ _objc_msgSend$_connectPendingFabricConnections
+ _objc_msgSend$_continueNetworkProvisioning
+ _objc_msgSend$_createTransientOperationalCertificateForFabricID:
+ _objc_msgSend$_disconnectFromIdleFabric:
+ _objc_msgSend$_establishConnectionWhenAllowedWithAccessoryConnectionRequest:
+ _objc_msgSend$_establishConnectionWhenAllowedWithFabricConnectionRequest:
+ _objc_msgSend$_fetchAdditionalThreadNetworkInformationWithCompletion:
+ _objc_msgSend$_fetchCert2ForFabricWithID:isOwner:completion:
+ _objc_msgSend$_fetchOperationalCertificatesFromResidentForFabricID:completion:
+ _objc_msgSend$_fetchSharedUserCert2ForFabricWithID:reFetch:completion:
+ _objc_msgSend$_getAllPendingOperations
+ _objc_msgSend$_getOperationalHardwareAddressFromReadValue:
+ _objc_msgSend$_getOperationalNetworkAddressForAccessory:
+ _objc_msgSend$_hasActiveAccessoryConnections
+ _objc_msgSend$_isDeviceIDPaired:nodeID:fabricID:
+ _objc_msgSend$_kickIdleTimer
+ _objc_msgSend$_operationalCertificateFromSdkCertificatesForFabricID:
+ _objc_msgSend$_removeFromActiveFabrics:
+ _objc_msgSend$_removeFromActiveIPConnections:
+ _objc_msgSend$_removeFromActiveThreadConnections:
+ _objc_msgSend$_removeFromActiveThreadWEDConnections:
+ _objc_msgSend$_removeFromPendingConnections:
+ _objc_msgSend$_removeFromPendingFabrics:
+ _objc_msgSend$_removeSharedAdminControllerNodeIDFromACLWithCompletion:
+ _objc_msgSend$_restartConnectionIdleTimer:
+ _objc_msgSend$_restartDiscovery
+ _objc_msgSend$_retryWEDConnectionToAccessory
+ _objc_msgSend$_rootCertificateFromSdkCertificatesForFabricID:
+ _objc_msgSend$_setupStorageStateIfNotFabricID:rediscoverAccessories:
+ _objc_msgSend$_stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:
+ _objc_msgSend$_stopMatterStack
+ _objc_msgSend$_stopSystemCommissionerFabricID:
+ _objc_msgSend$_suspendOperationsForFabricID:
+ _objc_msgSend$_tryAddAccessoryConnectionRequestToExistingFabric:
+ _objc_msgSend$_tryMergeIntoExistingConnection:
+ _objc_msgSend$_updateACLOnPairedAccessories
+ _objc_msgSend$_updateAccessoryControlListForServer:completion:
+ _objc_msgSend$_updateActiveThreadWEDConnectionsIdleTime:
+ _objc_msgSend$_updateConnectionIdleTime:
+ _objc_msgSend$_updateFabricIDOfActiveThreadNetwork:isFabricIDOfSystemCommissioner:
+ _objc_msgSend$abortAllOperations
+ _objc_msgSend$abortAllPendingOperations:
+ _objc_msgSend$abortOperationsForAccessoryServer:
+ _objc_msgSend$abortOperationsForConnectionRequest:
+ _objc_msgSend$accessControl
+ _objc_msgSend$accessoryAdministerPrivilegeCATID:
+ _objc_msgSend$accessoryOperatePrivilegeCATID:
+ _objc_msgSend$accessoryServerBrowser:cacheOperationalCertData:forFabricID:
+ _objc_msgSend$accessoryServerBrowser:getCachedOperationalCertificateDataForFabricID:completion:
+ _objc_msgSend$accessoryServerBrowser:getOperationalCertificatesForFabricID:publicKey:completion:
+ _objc_msgSend$active
+ _objc_msgSend$activeIPConnectionRequests
+ _objc_msgSend$activeThreadConnectionRequests
+ _objc_msgSend$activeThreadWEDConnectionRequests
+ _objc_msgSend$addFabricWithActiveClientForFabricID:
+ _objc_msgSend$allowDisconnect
+ _objc_msgSend$anyObject
+ _objc_msgSend$appleHomeFabricWithID:
+ _objc_msgSend$browserState
+ _objc_msgSend$caseAuthenticatedTag
+ _objc_msgSend$caseAuthenticatedTagsUpdated
+ _objc_msgSend$characteristicsOperationDispatchQueue
+ _objc_msgSend$checkAndUpdateExpiryOfCertificate:keyPair:newCertificate:
+ _objc_msgSend$colorMode
+ _objc_msgSend$connectToAccessoryWhenAllowed:
+ _objc_msgSend$connectToAccessoryWhenAllowed:highPriority:completion:
+ _objc_msgSend$connectToAccessoryWithExtendedMACAddress:completion:
+ _objc_msgSend$connectToAccessoryWithExtendedMACAddress:withFabricID:completion:
+ _objc_msgSend$connectionIdleTime
+ _objc_msgSend$connectionPriority
+ _objc_msgSend$createNewFabricDataForFabricID:completion:
+ _objc_msgSend$currentFabric
+ _objc_msgSend$currentUserPrivilege
+ _objc_msgSend$delayDiscovery
+ _objc_msgSend$deviceSupportsThreadService
+ _objc_msgSend$didFinishPairingAccessoryServer:operationDisabled:
+ _objc_msgSend$eMACAddress
+ _objc_msgSend$eMACAddressOfWEDAccessory
+ _objc_msgSend$executeAllPendingOperations
+ _objc_msgSend$extendedMACAddress
+ _objc_msgSend$fabric
+ _objc_msgSend$fabricIDOfActiveThreadNetwork
+ _objc_msgSend$fabricIdleTime
+ _objc_msgSend$fabricsWithActiveClients
+ _objc_msgSend$fabricsWithActiveConnections
+ _objc_msgSend$fabricsWithPendingConnections
+ _objc_msgSend$fetchCachedOperationalCertificateForFabricID:completionHandler:
+ _objc_msgSend$fetchExtendedMACAddressFromDevice:completion:
+ _objc_msgSend$fetchOperationalCertificatesFromResidentForPublicKey:fabricID:completionHandler:
+ _objc_msgSend$fetchSharedUserCertForFabricWithID:reFetch:completion:
+ _objc_msgSend$fetchWEDSupportInformationFromDevice:completion:
+ _objc_msgSend$fire
+ _objc_msgSend$getNOCFromResidentForSharedUserForFabric:
+ _objc_msgSend$getThreadNetworkConnectionStateWithFabricID:
+ _objc_msgSend$getThreadNetworkNodeTypeWithFabricID:
+ _objc_msgSend$handleResidentReachabilityChangeForFabric:
+ _objc_msgSend$handleThreadRadioStateChanged
+ _objc_msgSend$handleUpdateNotificationsEnabled:forFabric:
+ _objc_msgSend$hasOperationalCerts
+ _objc_msgSend$hasPendingHighPriorityConnectionRequest
+ _objc_msgSend$idleTimer
+ _objc_msgSend$initWithBrowser:
+ _objc_msgSend$initWithFabricID:rootCert:operationalCert:ownerNode:ipk:
+ _objc_msgSend$initWithMinInterval:maxInterval:
+ _objc_msgSend$initWithQueue:browser:fabricID:systemCommissionerFabric:
+ _objc_msgSend$initWithQueue:server:highPriority:completion:
+ _objc_msgSend$isCurrentDeviceAllowedAccessoryControlDespiteReachableResidentForFabric:
+ _objc_msgSend$isCurrentDeviceMobileAndAllowedAccessoryControl
+ _objc_msgSend$isCurrentDeviceMobileAndResidentReachable
+ _objc_msgSend$isCurrentUserOwner
+ _objc_msgSend$isFabricCreationInProgress
+ _objc_msgSend$isOwnerForHomeWithFabric:
+ _objc_msgSend$isPrimaryResidentNodeReachable
+ _objc_msgSend$isPrimaryResidentNodeReachableAndThreadCapable
+ _objc_msgSend$isReadyToEstablishWEDConnection
+ _objc_msgSend$isThreadNetworkConnected
+ _objc_msgSend$isValidCATSubject:
+ _objc_msgSend$isWEDConnectionRetryActive
+ _objc_msgSend$isWEDDevice
+ _objc_msgSend$lastKnownThreadNetworkConnectionState
+ _objc_msgSend$legacyNodeIDForCurrentFabric
+ _objc_msgSend$mergeAccessoryConnectionRequest:
+ _objc_msgSend$mergeExistingAclEntries:withAdminNodes:regularUserNodes:
+ _objc_msgSend$mergeExistingAclEntries:withNewNodes:withPrivilege:
+ _objc_msgSend$moveToColorTemperatureWithParams:completionHandler:
+ _objc_msgSend$moveToColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:
+ _objc_msgSend$moveToCustomColorTemperatureValue:fromColorTemperature:transitionTime:completionHandler:
+ _objc_msgSend$nodesWithPendingACLOverwrite
+ _objc_msgSend$objectID
+ _objc_msgSend$operationsCompletedForAccessoryConnectionRequest:
+ _objc_msgSend$operationsCompletedForFabricConnectionRequest:
+ _objc_msgSend$operationsStartedForFabricConnectionRequest:
+ _objc_msgSend$orderedSet
+ _objc_msgSend$otaProviderState
+ _objc_msgSend$ownerNode
+ _objc_msgSend$parentFabricRequest
+ _objc_msgSend$parseCaseAuthenticatedTag:identifier:version:
+ _objc_msgSend$pendingConnectionRequests
+ _objc_msgSend$pendingThreadStart
+ _objc_msgSend$persistLegacyControllerNodeWithDictionary:
+ _objc_msgSend$preventDisconnect
+ _objc_msgSend$preventThreadStopDuringStackRestart
+ _objc_msgSend$readAttributeColorCapabilitiesWithCompletion:
+ _objc_msgSend$readAttributeColorModeWithCompletion:
+ _objc_msgSend$readAttributeColorModeWithCompletionHandler:
+ _objc_msgSend$readAttributeColorModeWithParams:
+ _objc_msgSend$readAttributeColorTemperatureMiredsWithCompletion:
+ _objc_msgSend$readAttributeColorTemperatureMiredsWithParams:
+ _objc_msgSend$readAttributeRemainingTimeWithCompletion:
+ _objc_msgSend$readAttributeRockSettingWithCompletion:
+ _objc_msgSend$readAttributeRockSettingWithParams:
+ _objc_msgSend$readAttributeRockSupportWithCompletion:
+ _objc_msgSend$readAttributeRockSupportWithParams:
+ _objc_msgSend$readAttributeStartUpColorTemperatureMiredsWithCompletion:
+ _objc_msgSend$remainingTime
+ _objc_msgSend$removeNode:withPrivilge:fromExistingAclEntries:
+ _objc_msgSend$restartDiscovery
+ _objc_msgSend$retryConnectionQueue
+ _objc_msgSend$retryOperations
+ _objc_msgSend$setActive:
+ _objc_msgSend$setCaseAuthenticatedTag:
+ _objc_msgSend$setCaseAuthenticatedTagsUpdated:
+ _objc_msgSend$setColorMode:
+ _objc_msgSend$setColorTemperature:
+ _objc_msgSend$setConnectionIdleTime:
+ _objc_msgSend$setConnectionPriority:
+ _objc_msgSend$setDelayDiscovery:
+ _objc_msgSend$setEMACAddress:
+ _objc_msgSend$setEMACAddressOfWEDAccessory:
+ _objc_msgSend$setFabric:
+ _objc_msgSend$setFabricCreationInProgress:
+ _objc_msgSend$setFabricIDOfActiveThreadNetwork:
+ _objc_msgSend$setFabricIdleTime:
+ _objc_msgSend$setHasOperationalCerts:
+ _objc_msgSend$setIsPairingActive:
+ _objc_msgSend$setIsWEDConnectionRetryActive:
+ _objc_msgSend$setLastKnownThreadNetworkConnectionState:
+ _objc_msgSend$setParentFabricRequest:
+ _objc_msgSend$setPendingThreadStart:
+ _objc_msgSend$setPreventDisconnect:
+ _objc_msgSend$setPreventThreadStopDuringStackRestart:
+ _objc_msgSend$setRemainingTime:
+ _objc_msgSend$setThreadNetworkActivatedForSystemCommissionerFabric:
+ _objc_msgSend$setWedDevice:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$setupStorageStateAndRediscoverAccessoriesForHomeFabricID:
+ _objc_msgSend$setupThreadPairing
+ _objc_msgSend$startAccessoryPairingWithExtendedMACAddress:fabricID:isWedDevice:completion:
+ _objc_msgSend$startAccessoryPairingWithExtendedMACAddress:isWedDevice:completion:
+ _objc_msgSend$startOperations
+ _objc_msgSend$startThreadRadioForHomeWithFabricID:
+ _objc_msgSend$startThreadRadioForHomeWithFabricID:preventDisconnect:
+ _objc_msgSend$startThreadRadioForSystemCommissionerFabricID:
+ _objc_msgSend$startThreadRadioForUserPreferredNetwork
+ _objc_msgSend$stopAccessoryPairingWithCompletion:
+ _objc_msgSend$stopAccessoryPairingWithFabricID:completion:
+ _objc_msgSend$stopMoveStepWithParams:completion:
+ _objc_msgSend$stopOperations
+ _objc_msgSend$stopThreadRadioForHomeWithFabricID:
+ _objc_msgSend$stopThreadRadioForSystemCommissionerFabricID:
+ _objc_msgSend$stopThreadRadioForUserPreferredNetwork
+ _objc_msgSend$subscribeAttributeColorModeWithParams:subscriptionEstablished:reportHandler:
+ _objc_msgSend$suspendOperations
+ _objc_msgSend$systemCommissionerFabric
+ _objc_msgSend$targets
+ _objc_msgSend$threadNetworkActivatedForSystemCommissionerFabric
+ _objc_msgSend$threadRadioManager
+ _objc_msgSend$updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:
+ _objc_msgSend$updateAccessoryControlToRemoveAdministratorNode:completion:
+ _objc_msgSend$updateConnectionIdleTime:
+ _objc_msgSend$wedSupport
+ _objc_msgSend$writeAttributeRockSettingWithValue:completionHandler:
+ _objc_msgSend$writeAttributeRockSettingWithValue:expectedValueInterval:
+ _objc_msgSend$writeAttributeStartUpColorTemperatureMiredsWithValue:completion:
- -[HMMTRAccessoryServer(Diagnostics) getOperationalHardwareAddressFromReadValue:]
- -[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]
- -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricID:]
- -[HMMTRAccessoryServerBrowser isOwnerForHomeWithFabricID:]
- -[HMMTRColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]
- -[HMMTRStorage fetchSharedUserCertForFabricWithID:completion:]
- -[HMMTRStorage ipkForCurrentFabricID]
- -[HMMTRStorage updateCertificateExpiryInStorage:keyPair:]
- -[HMMTRStorage(Records) isStorageCorruptForKeyValueStore:]
- -[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:flow:]
- GCC_except_table1026
- GCC_except_table1048
- GCC_except_table1091
- GCC_except_table1135
- GCC_except_table1299
- GCC_except_table1322
- GCC_except_table1405
- GCC_except_table1429
- GCC_except_table1431
- GCC_except_table1435
- GCC_except_table1453
- GCC_except_table1467
- GCC_except_table1473
- GCC_except_table1482
- GCC_except_table1484
- GCC_except_table1491
- GCC_except_table1507
- GCC_except_table1513
- GCC_except_table1520
- GCC_except_table1832
- GCC_except_table1837
- GCC_except_table1840
- GCC_except_table1895
- GCC_except_table1909
- GCC_except_table1918
- GCC_except_table1919
- GCC_except_table1933
- GCC_except_table1934
- GCC_except_table1965
- GCC_except_table2003
- GCC_except_table2035
- GCC_except_table2039
- GCC_except_table2055
- GCC_except_table2056
- GCC_except_table2080
- GCC_except_table2128
- GCC_except_table2164
- GCC_except_table2172
- GCC_except_table2187
- GCC_except_table2206
- GCC_except_table2221
- GCC_except_table2222
- GCC_except_table2227
- GCC_except_table2235
- GCC_except_table229
- GCC_except_table2343
- GCC_except_table2348
- GCC_except_table2442
- GCC_except_table2445
- GCC_except_table2564
- GCC_except_table2568
- GCC_except_table2594
- GCC_except_table2615
- GCC_except_table418
- GCC_except_table420
- GCC_except_table469
- GCC_except_table473
- GCC_except_table475
- GCC_except_table477
- GCC_except_table479
- GCC_except_table482
- GCC_except_table534
- GCC_except_table565
- GCC_except_table581
- GCC_except_table626
- GCC_except_table634
- GCC_except_table659
- GCC_except_table689
- ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.573
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.689
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.692
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.128
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.130
- ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.100
- ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.173
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.227
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.425
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.426
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.427
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.428
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.431
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.429
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.430
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.126
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.86
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.88
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.91
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.93
- ___146-[HMMTRAccessoryServerBrowser _prepareForPairingWithSetupPayload:fabricID:controllerWrapper:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.154
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.155
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.157
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.159
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.160
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.161
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.162
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.163
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.164
- ___263-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
- ___263-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.112
- ___263-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke_2
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.269
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.271
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.273
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.518
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.519
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.520
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.521
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.522
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.523
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.524
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.525
- ___40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.23
- ___42-[HMMTRAccessoryServer onPairingComplete:]_block_invoke
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.261
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.264
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.673
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.585
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.592
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.250
- ___45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.24
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.729
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.239
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.650
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.654
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.653
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.700
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.701
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.702
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.705
- ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.152
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.610
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.613
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.614
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.730
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.140
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.141
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.222
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.529
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.534
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.728
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.368
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.369
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.370
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.371
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.372
- ___56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.21
- ___57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.85
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.378
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.379
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.380
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.381
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.382
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.693
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.695
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.697
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.698
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.373
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.374
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.375
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.376
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.377
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.106
- ___62-[HMMTRStorage fetchSharedUserCertForFabricWithID:completion:]_block_invoke
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.404
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.405
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.406
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.407
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.410
- ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke_3
- ___63-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:flow:]_block_invoke
- ___63-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:flow:]_block_invoke.111
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.387
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.388
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.389
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.391
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.82
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.383
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.384
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.385
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.386
- ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.280
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.187
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.360
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.366
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.367
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.107
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.110
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.235
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.348
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.353
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.354
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.392
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.393
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.394
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.396
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.398
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.399
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.400
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.401
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.402
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.403
- ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.76
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.605
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.606
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.608
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.607
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.593
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.594
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.601
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.602
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.604
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.595
- ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.149
- ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.150
- ___73-[HMMTRThermostat writeAttributePluginActiveWithValue:completionHandler:]_block_invoke.41
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.659
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.660
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.664
- ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.67
- ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.70
- ___75-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricID:]_block_invoke
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.253
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.254
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.255
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.256
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.355
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.356
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.357
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.359
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.145
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.147
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.148
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.93
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.95
- ___83-[HMMTRThermostat readAttributePluginTargetHeaterCoolerStateWithCompletionHandler:]_block_invoke.47
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.317
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.318
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.320
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.677
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.678
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.679
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.680
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.683
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.684
- ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.42
- ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.43
- ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.44
- ___88-[HMMTRColorControl moveToCustomColorTemperatureValue:transitionTime:completionHandler:]_block_invoke
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.241
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.242
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.433
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.434
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.435
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.436
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.438
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.437
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.628
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.101
- ___98-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:]_block_invoke.153
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.225
- ___Block_byref_object_copy_.1458
- ___Block_byref_object_copy_.1720
- ___Block_byref_object_copy_.3477
- ___Block_byref_object_copy_.3778
- ___Block_byref_object_copy_.4380
- ___Block_byref_object_copy_.5180
- ___Block_byref_object_copy_.5710
- ___Block_byref_object_copy_.6205
- ___Block_byref_object_copy_.6743
- ___Block_byref_object_copy_.6933
- ___Block_byref_object_dispose_.1459
- ___Block_byref_object_dispose_.1721
- ___Block_byref_object_dispose_.3478
- ___Block_byref_object_dispose_.3779
- ___Block_byref_object_dispose_.4381
- ___Block_byref_object_dispose_.5181
- ___Block_byref_object_dispose_.5711
- ___Block_byref_object_dispose_.6206
- ___Block_byref_object_dispose_.6744
- ___Block_byref_object_dispose_.6934
- ___block_descriptor_48_e8_32bs40w_e35_v20?0"HMMTRControllerWrapper"8B16lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e30_v24?0"NSNumber"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.104.258
- ___block_literal_global.112
- ___block_literal_global.1130
- ___block_literal_global.1274
- ___block_literal_global.136.3502
- ___block_literal_global.1375
- ___block_literal_global.1477
- ___block_literal_global.1621
- ___block_literal_global.170
- ___block_literal_global.1782
- ___block_literal_global.1917
- ___block_literal_global.200
- ___block_literal_global.2024
- ___block_literal_global.264
- ___block_literal_global.2692
- ___block_literal_global.2994
- ___block_literal_global.3075
- ___block_literal_global.3258
- ___block_literal_global.3367
- ___block_literal_global.3604
- ___block_literal_global.3789
- ___block_literal_global.409
- ___block_literal_global.4106
- ___block_literal_global.442
- ___block_literal_global.4420
- ___block_literal_global.4626
- ___block_literal_global.5098
- ___block_literal_global.536
- ___block_literal_global.5412
- ___block_literal_global.584
- ___block_literal_global.588
- ___block_literal_global.591
- ___block_literal_global.5920
- ___block_literal_global.597
- ___block_literal_global.60
- ___block_literal_global.6112
- ___block_literal_global.6238
- ___block_literal_global.6378
- ___block_literal_global.639
- ___block_literal_global.65
- ___block_literal_global.6691
- ___block_literal_global.70
- ___block_literal_global.711
- ___block_literal_global.743
- ___block_literal_global.864
- ___block_literal_global.93
- __unnamed_array_storage.101
- __unnamed_array_storage.109
- __unnamed_array_storage.1256
- __unnamed_array_storage.1610
- __unnamed_array_storage.4323
- __unnamed_array_storage.5744
- __unnamed_array_storage.67
- __unnamed_array_storage.90
- _logCategory._hmf_once_t2.5097
- _logCategory._hmf_once_t263
- _logCategory._hmf_once_t3.3257
- _logCategory._hmf_once_t3.638
- _logCategory._hmf_once_t3.710
- _logCategory._hmf_once_t4.3366
- _logCategory._hmf_once_t45
- _logCategory._hmf_once_t46
- _logCategory._hmf_once_t501
- _logCategory._hmf_once_t57
- _logCategory._hmf_once_t66
- _logCategory._hmf_once_t7
- _logCategory._hmf_once_t8.1781
- _logCategory._hmf_once_t8.6111
- _logCategory._hmf_once_t87
- _logCategory._hmf_once_t99
- _logCategory._hmf_once_v100
- _logCategory._hmf_once_v264
- _logCategory._hmf_once_v3.5099
- _logCategory._hmf_once_v4.3259
- _logCategory._hmf_once_v4.640
- _logCategory._hmf_once_v4.712
- _logCategory._hmf_once_v46
- _logCategory._hmf_once_v47
- _logCategory._hmf_once_v5.3368
- _logCategory._hmf_once_v502
- _logCategory._hmf_once_v58
- _logCategory._hmf_once_v67
- _logCategory._hmf_once_v8
- _logCategory._hmf_once_v88
- _logCategory._hmf_once_v9.1783
- _logCategory._hmf_once_v9.6113
- _objc_msgSend$_stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:
- _objc_msgSend$getOperationalHardwareAddressFromReadValue:
- _objc_msgSend$isOwnerForHomeWithFabricID:
- _objc_msgSend$isStorageCorruptForKeyValueStore:
- _objc_msgSend$setOperationalCertificate:
- _objc_msgSend$updateCertificateExpiryInStorage:keyPair:
CStrings:
+ "\x028\x14\x11\x18\x1e"
+ "\x114"
+ "\x14\x13"
+ "!\x11"
+ "%@ %@ [%@]"
+ "%@/%@(%@)"
+ "%{public}@#### Failed fetching NOC for shared user with error %@"
+ "%{public}@#### Failed refetching NOC for shared user with error %@"
+ "%{public}@%s - %@"
+ "%{public}@%s - accessoryConnectionRequest = %@ on %@"
+ "%{public}@Aborting operations for fabric: %@"
+ "%{public}@Accessory returned WED support information as %@"
+ "%{public}@Accessory returned eMAC address as %@"
+ "%{public}@Accessory returned values as %@"
+ "%{public}@Accessory server disabled by the time operation is executed"
+ "%{public}@Accessory server disappeared, aborting all requests for %@"
+ "%{public}@Accessory server is disabled, aborting all requests for %@"
+ "%{public}@Accessory server operations disabled. Aborting fetching WED support information."
+ "%{public}@Accessory server operations disabled. Aborting fetching eMAC address."
+ "%{public}@Accessory with node ID %@ was added to home with fabric %@"
+ "%{public}@Active WED session, add thread request to pending queue"
+ "%{public}@Added active client for pairing into fabric ID %@, currently active clients: %@"
+ "%{public}@Adding active IP connection for request: %@"
+ "%{public}@Adding active connection for fabric: %@"
+ "%{public}@Adding active thread WED connection for request: %@"
+ "%{public}@Adding active thread connection for request: %@"
+ "%{public}@Allowing server creation for non-owner with NodeID %@"
+ "%{public}@Allowing thread stop for fabricID %@"
+ "%{public}@An accessory operation is complete"
+ "%{public}@An error occurred while trying to read RockSetting attribute"
+ "%{public}@An error occurred while trying to read RockSupport attribute"
+ "%{public}@An error occurred while trying to read RockSupport attribute. Cannot write RockSetting attribute."
+ "%{public}@An error occurred while trying to read color mode"
+ "%{public}@An error occurred while trying to read color temperature"
+ "%{public}@Attempting to retry WED connection to eMACAddress: %@"
+ "%{public}@Cached Root certificate not found"
+ "%{public}@Cannot write RockSetting attribute. Unexpected swing value %@"
+ "%{public}@Certificate doesn't match key pair %@"
+ "%{public}@Certificate expires in distant future. No update needed %@ vs %@"
+ "%{public}@Characteristics Operation Queue: fetch WED support information job(%lu) complete."
+ "%{public}@Characteristics Operation Queue: fetch WED support information job(%lu) queued."
+ "%{public}@Characteristics Operation Queue: fetch WED support information job(%lu) started."
+ "%{public}@Characteristics Operation Queue: fetch eMAC address job(%lu) complete."
+ "%{public}@Characteristics Operation Queue: fetch eMAC address job(%lu) queued."
+ "%{public}@Characteristics Operation Queue: fetch eMAC address job(%lu) started."
+ "%{public}@Check if MTS stored cert has correct validity period"
+ "%{public}@Check validity period of root cert of fabric ID %@"
+ "%{public}@Check validity period of the Matter SDK stored root cert of fabric ID %@"
+ "%{public}@Check validity period of the root cert of fabric ID %@"
+ "%{public}@Color mode selector not found for cluster: %@"
+ "%{public}@Connected to an accessory for an operation with error: %@"
+ "%{public}@Connecting pending connections for fabric %@"
+ "%{public}@Connecting to WED accessory: %@"
+ "%{public}@Connecting to an accessory for an operation"
+ "%{public}@Connection has become idle but there are still active clients, keeping matter stack active for fabricID %@. Fabrics with active clients: %@"
+ "%{public}@Connection has become idle, shutting down matter stack for fabricID %@. Fabrics with active clients: %@"
+ "%{public}@Connection request for accessory %@. Current active fabric count: %tu, Pending: %tu"
+ "%{public}@Connection request for fabric %@, Current active fabric count: %tu, Pending: %tu"
+ "%{public}@Could not create a new fabric data: %@. Aborting pairing"
+ "%{public}@Could not create server for local try: %@"
+ "%{public}@Couldn't extract certificate info"
+ "%{public}@Couldn't get a strong ref to browser"
+ "%{public}@Creating operational certificate for transient node ID %@ CAT %@ root cert %@, fabric ID %@"
+ "%{public}@Current device cannot be an OTA provider"
+ "%{public}@Current implementation doesn't support removal of CAT IDs"
+ "%{public}@Current implementation is restricted to removal of admin nodes only"
+ "%{public}@Current pending connections: %@, Connected/Connecting: %@"
+ "%{public}@Disconnect from WED accessory %@ with emac %@ completed, error %@"
+ "%{public}@Disconnecting from WED accessory %@"
+ "%{public}@Error reading color mode on endpoint %@, Error: %@"
+ "%{public}@Executing an operation without connecting to the accessory"
+ "%{public}@Fabric %@ does not have active clients, fabricsWithActiveClients - %@"
+ "%{public}@Fabric %@ has become idle, but current FabricID is %@, not stopping current matter stack. fabrics with active clients:%@"
+ "%{public}@Fabric data source not available; failed to get legacy node ID for fabric ID %@"
+ "%{public}@Fabric is currently inactive, do not connect any pending connections: %@"
+ "%{public}@Fabric not provided and no active clients, not configuring any controller wrapper"
+ "%{public}@Failed to connect to accessory with emac %@, error %@"
+ "%{public}@Failed to create operational certificate for transient node ID %@ CAT %@ with error %@"
+ "%{public}@Failed to disconnect from WED accessory %@, error %@"
+ "%{public}@Failed to establish WED connection to accessory %@ with emac %@, error %@"
+ "%{public}@Failed to fetch certificates required for pairing on fabricID %@ with error %@"
+ "%{public}@Failed to fetch eMAC address of CHIP Accessory with error %@"
+ "%{public}@Failed to fetch operational certificates from owner with error %@"
+ "%{public}@Failed to get cached operational cert for fabricID %@ with error %@"
+ "%{public}@Failed to get color mode. Error: %@"
+ "%{public}@Failed to inform thread SW of start pairing with emac %@, error %@"
+ "%{public}@Failed to inform thread SW of stop pairing"
+ "%{public}@Failed to persist legacy node with error %@"
+ "%{public}@Failed to re-create certificate with new validity %@ due to error %@"
+ "%{public}@Failed to retrieve WED support information: %@"
+ "%{public}@Failed to retrieve eMAC address: %@"
+ "%{public}@Failed to update ACL on accessory with error %@"
+ "%{public}@Faking a color temperature attribute report %@ on endpoint %@ upon hue/sat command invocation, updatedAttributesHandler %@"
+ "%{public}@Fetching WED support information"
+ "%{public}@Fetching eMAC address"
+ "%{public}@Found existing server for nodeID %llu in unpaired state, but discovery is delayed for server %@"
+ "%{public}@Found existing server for nodeID %llu in unpaired state, using it instead of new server = %@ "
+ "%{public}@Generating a OP cert for Shared user (isAdmin %@) with nocSigner %@, rootCert = %@, pubKeyAsSecKey %@, fabricID %@, nodeID %@ CATs = %@"
+ "%{public}@Generating a Random Node ID for Shared user Controller as %@"
+ "%{public}@Getting root certificate for fabric ID %@"
+ "%{public}@Handling Attribute report linked to Active Char (sync) - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to Active Char - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to current heater cooler state (sync) - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to current heater cooler state - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to current heating/cooling state (sync) - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to current heating/cooling state - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to target heater cooler state (sync) - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Handling Attribute report linked to target heater cooler state - endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@Home with fabric %@ has been deleted, cleaning up state"
+ "%{public}@Ignoring announcement request for automatic software updates"
+ "%{public}@Ignoring spurious fabric index update notification for fabric ID %@"
+ "%{public}@Ignoring thread start for fabric %@, network is locked to fabricID %@"
+ "%{public}@Ignoring updated fabric index notification until fabric creation is successful"
+ "%{public}@Informed thread SW of start pairing with emac %@"
+ "%{public}@Informed thread SW of stop pairing"
+ "%{public}@Invalid fabricID, ignoring thread radio start"
+ "%{public}@Invalid fabricID, ignoring thread radio stop"
+ "%{public}@Invalid state, expecting to be active for retryOperations for %@"
+ "%{public}@Keeping CHIP link alive for accessory:%@ since resident is not available."
+ "%{public}@Marking operation complete for accessory request: %@"
+ "%{public}@Marking operation complete for fabric: %@"
+ "%{public}@Matter device doesn't have general diagnostic cluster"
+ "%{public}@Matter device is nil"
+ "%{public}@Matter topology is nil"
+ "%{public}@New ACL entries %@"
+ "%{public}@No ACL nodes to update on accessory"
+ "%{public}@No Matter device controller available to fetch WED support information"
+ "%{public}@No Matter device controller available to fetch eMAC address"
+ "%{public}@No active fabric, no action taken on thread state change"
+ "%{public}@No active thread network configured, dropping request to connect to accessory with eMAC %@"
+ "%{public}@No active thread network configured, dropping request to inform thread SW of start pairing with eMAC %@"
+ "%{public}@No active thread network configured, dropping request to inform thread SW of stop pairing"
+ "%{public}@No activity for accessory %@, releasing connection"
+ "%{public}@No activity on fabric %@, releasing connection"
+ "%{public}@No fabric to connect"
+ "%{public}@No more pending connections"
+ "%{public}@No more pending fabric connection requests"
+ "%{public}@No resident reachable for fabricID %@ and there are active clients, start local stack"
+ "%{public}@Not owner for home with fabric %@ - Not updating ACLs and blocking invalidation"
+ "%{public}@Not ready to establish a WED session, add to pending queue"
+ "%{public}@Not retrying thread connection. eMACAddress: %@, allowedAccessoryControl: %@, connection retry: %@, isReadyToEstablishWEDConnection: %@"
+ "%{public}@Not shutting down stack for fabricID %@ because there is an active connection"
+ "%{public}@Not starting local discovery for fabricID %@, resident available"
+ "%{public}@Overwriting ACL on accessory to remove node ID of shared Admin controller"
+ "%{public}@Owner user - No need to request NOC"
+ "%{public}@Paired device %@ with node ID %@ fakes discovery for local fallback"
+ "%{public}@Pending connection to accessory: %@"
+ "%{public}@Pending connection to fabric: %@"
+ "%{public}@Preventing thread stop for fabricID %@ because preventDisconnect is true and locked to fabricID %@"
+ "%{public}@Querying endpoint %@ for color mode"
+ "%{public}@RETRY: Connected to WED accessory with emac: %@"
+ "%{public}@RETRY: Failed to establish WED connection to accessory with emac %@, error %@"
+ "%{public}@Read Active Char (sync): An error occurred while trying to read the system mode"
+ "%{public}@Read Active Characteristic: An error occurred while trying to read the system mode: %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint (sync): An error occurred while trying to read the current System Mode"
+ "%{public}@Read Occupied Heating/Cooling Setpoint (sync): OccupiedCoolingSetpoint is %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint (sync): OccupiedHeatingSetpoint is %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint (sync): Read local temperature %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint (sync): Thermostat Setpoint should not be read in unexpected system mode: %ld"
+ "%{public}@Read Occupied Heating/Cooling Setpoint: An error occurred while trying to read the System Mode: %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint: OccupiedCoolingSetpoint is %@, error: %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint: OccupiedHeatingSetpoint is %@, error: %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint: Read local temperature %@, error: %@"
+ "%{public}@Read Occupied Heating/Cooling Setpoint: Thermostat Setpoint should not be read in unexpected system mode: %ld"
+ "%{public}@Read attribute RockSetting completed with value %@, error %@"
+ "%{public}@Read attribute RockSupport completed with value %@, error %@"
+ "%{public}@Read cached operational cert data from disk self.rootCert %@, self.operationalCert %@ self.ownerNodeID %@ self.ownerIPK %@"
+ "%{public}@Read color control attribute colorCapabilities: %@ error: %@"
+ "%{public}@Read color mode on endpoint %@. Color mode: %@"
+ "%{public}@Read current heater cooler state (sync): An error occurred while trying to read the local temperature"
+ "%{public}@Read current heater cooler state (sync): An error occurred while trying to read the occupied cooling point"
+ "%{public}@Read current heater cooler state (sync): An error occurred while trying to read the occupied heating point"
+ "%{public}@Read current heater cooler state (sync): An error occurred while trying to read the system mode"
+ "%{public}@Read current heater cooler state (sync): Got coolPointValue value: %ld"
+ "%{public}@Read current heater cooler state (sync): Got heatPointValue value: %ld"
+ "%{public}@Read current heater cooler state (sync): Got systemModeValue value: %ld"
+ "%{public}@Read current heater cooler state (sync): Got temperatureValue value: %ld"
+ "%{public}@Read current heater cooler state (sync): Unsupported system mode: %ld"
+ "%{public}@Read current heater cooler state: An error occurred while trying to read the local temperature: %@"
+ "%{public}@Read current heater cooler state: An error occurred while trying to read the occupied cooling point: %@"
+ "%{public}@Read current heater cooler state: An error occurred while trying to read the occupied heating point: %@"
+ "%{public}@Read current heater cooler state: An error occurred while trying to read the system mode: %@"
+ "%{public}@Read current heater cooler state: Got coolPointValue value: %@"
+ "%{public}@Read current heater cooler state: Got heatPointValue value: %@"
+ "%{public}@Read current heater cooler state: Got systemModeValue value: %@"
+ "%{public}@Read current heater cooler state: Got temperatureValue value: %@"
+ "%{public}@Read current heater cooler state: Unsupported system mode: %@"
+ "%{public}@Read current heating/cooling state (sync): An error occurred while trying to read the local temperature"
+ "%{public}@Read current heating/cooling state (sync): An error occurred while trying to read the occupied cooling point"
+ "%{public}@Read current heating/cooling state (sync): An error occurred while trying to read the occupied heating point"
+ "%{public}@Read current heating/cooling state (sync): An error occurred while trying to read the system mode"
+ "%{public}@Read current heating/cooling state (sync): Couldn't get thermostat running mode from device. Ignoring error"
+ "%{public}@Read current heating/cooling state (sync): Got coolPointValue value: %ld"
+ "%{public}@Read current heating/cooling state (sync): Got heatPointValue value: %ld"
+ "%{public}@Read current heating/cooling state (sync): Got runningModeValue value: %ld"
+ "%{public}@Read current heating/cooling state (sync): Got systemModeValue value: %ld"
+ "%{public}@Read current heating/cooling state (sync): Got temperatureValue value: %ld"
+ "%{public}@Read current heating/cooling state (sync): Unsupported system mode: %ld"
+ "%{public}@Read current heating/cooling state: An error occurred while trying to read the local temperature: %@"
+ "%{public}@Read current heating/cooling state: An error occurred while trying to read the occupied cooling point: %@"
+ "%{public}@Read current heating/cooling state: An error occurred while trying to read the occupied heating point: %@"
+ "%{public}@Read current heating/cooling state: An error occurred while trying to read the system mode: %@"
+ "%{public}@Read current heating/cooling state: Couldn't get thermostat running mode from device. Ignoring error: %@"
+ "%{public}@Read current heating/cooling state: Got coolPointValue value: %@"
+ "%{public}@Read current heating/cooling state: Got heatPointValue value: %@"
+ "%{public}@Read current heating/cooling state: Got runningModeValue value: %@"
+ "%{public}@Read current heating/cooling state: Got systemModeValue value: %@"
+ "%{public}@Read current heating/cooling state: Got temperatureValue value: %@"
+ "%{public}@Read current heating/cooling state: Unsupported system mode: %@"
+ "%{public}@Read target heater cooler state (sync): An error occurred while trying to read the control sequence of operation"
+ "%{public}@Read target heater cooler state (sync): An error occurred while trying to read the system mode"
+ "%{public}@Read target heater cooler state (sync): Unsupported control sequence of operation value: %@"
+ "%{public}@Read target heater cooler state: An error occurred while trying to read the control sequence of operation: %@"
+ "%{public}@Read target heater cooler state: An error occurred while trying to read the system mode: %@"
+ "%{public}@Read target heater cooler state: Unsupported control sequence of operation value: %@"
+ "%{public}@Receive update notification enabled:%@ for fabricID:%@"
+ "%{public}@Received %@ as fabricID, ignoring ResidentReachabilityChange"
+ "%{public}@Received %@ as fabricID, ignoring updateNotifications"
+ "%{public}@Received attribute report for color mode value: %@ error: %@"
+ "%{public}@Received request from Shared user controller to generate Operational Certificate for Node ID %@"
+ "%{public}@Received request from Shared user controller to generate Operational certificate for itself"
+ "%{public}@Received thread WED connection changed notification for eMACAddress: %@ with state: %ld, eMACAddress of last connection: %@"
+ "%{public}@Received thread radio state changed notification, connectionState: %ld, nodeType: %ld, last known connectionState: %ld"
+ "%{public}@Removed active IP connection for accessory %@"
+ "%{public}@Removed active connection for fabric: %{public}@"
+ "%{public}@Removed active thread WED connection for accessory %@"
+ "%{public}@Removed active thread connection for accessory %@"
+ "%{public}@Removed pending connection for fabric: %@"
+ "%{public}@Removed pending connection to accessory: %@"
+ "%{public}@Removing shared admin controller device's node ID from ACL"
+ "%{public}@Requesting certificates required for shared user direct control from Resident device"
+ "%{public}@Resetting storage state after pairing error"
+ "%{public}@Resetting storage state after pairing failure"
+ "%{public}@Resident is not yet reachable to get NOC"
+ "%{public}@Resident reachability changed for non-current fabricID %@, ignoring"
+ "%{public}@Resident state change for fabricID:%@"
+ "%{public}@Retrying WED connection"
+ "%{public}@Return %@ for color temp due to ColorMode is currently %@"
+ "%{public}@Returning Root Certificate %@, Operational Certificate %@ to Shared user Controller"
+ "%{public}@Returning Root Certificate %@, Operational Certificate %@, Owner NodeID %@, and IPK %@ to Shared user Controller"
+ "%{public}@Set eMACAddress of WED accessory to :%@"
+ "%{public}@Setting WED support to %@"
+ "%{public}@Shared User is attempting to get NOC for fabricID %@"
+ "%{public}@Shutting down stack for fabricID %@ because there are no active clients"
+ "%{public}@Start thread for fabricID %@, preventDisconnect = %@, last known connectionState: %ld"
+ "%{public}@Start thread for system commissioner fabric ID %@"
+ "%{public}@Starting discovery for fabric %@"
+ "%{public}@Starting discovery for fabricID %@ because there are active clients"
+ "%{public}@Starting discovery stack for fabricID %@ because there are active clients"
+ "%{public}@Starting operations for fabric: %@"
+ "%{public}@Starting stack for fabricID %@ because there are active clients and local stack is unconfigured"
+ "%{public}@Starting thread for fabricID %@ because it became the current fabric"
+ "%{public}@Stop thread for fabricID %@"
+ "%{public}@Stop thread for system commissioner fabric ID %@"
+ "%{public}@Stopping operaiton with system commissioner fabric ID %@"
+ "%{public}@Storage doesn't have f/%x/n"
+ "%{public}@Storing the initial Matter storage to remote %@"
+ "%{public}@Successfully fetched operational certificates from owner. Root Certificate %@, Operational certificate %@, Owner NodeID %@"
+ "%{public}@Successfully persisted legacy node to Apple Home storage with %lu keys"
+ "%{public}@Successfully re-created certificate with new validity %@"
+ "%{public}@Suspending operations for fabric: %@"
+ "%{public}@Thread StopAccessoryPairing completed, error: %@"
+ "%{public}@Thread is not active"
+ "%{public}@Thread network is already running for fabric ID %@. Not starting Thread."
+ "%{public}@Thread network is already running for this fabric, calling threadStart and setting preventDisconnect to %@"
+ "%{public}@Thread network is running for another fabric ID %@. Not stopping Thread."
+ "%{public}@Thread radio feature is not enabled"
+ "%{public}@Thread start already pending, ignoring startThread request for fabricID %@"
+ "%{public}@Thread start called for new fabricID %@, will be disconnecting from thread network for fabricID %@"
+ "%{public}@ThreadService feature is disabled"
+ "%{public}@ThreadService feature is enabled"
+ "%{public}@ThreadService feature is enabled through profile"
+ "%{public}@Too many active WED session, add to pending queue"
+ "%{public}@Unexpected ACL remove operation"
+ "%{public}@Unexpected state, fabricIDOfActiveThreadNetwork = %@, preventDisconnect = %@"
+ "%{public}@Unexpected, color temperature characteristic not found on endpoint %@"
+ "%{public}@Unexpected, target temperature characteristic not found on endpoint %@"
+ "%{public}@Unexpected, thread radio went offline. Restarting thread radio for fabric ID: %@, is system commissioner: %@, preventDisconnect = %@"
+ "%{public}@Unsupported linkLayerType: %ld for request %@"
+ "%{public}@UpdateNotifications received for fabricID:%@ enabled:%@. currentFabricID %@, browserState = %lu, fabricsWithActiveClients = %@"
+ "%{public}@UpdateValueForAttributeReport (sync): An error occurred while trying to read the current System Mode"
+ "%{public}@UpdateValueForAttributeReport (sync): Handling Attribute report endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@UpdateValueForAttributeReport (sync): Report OccupiedCoolingSetpoint %@"
+ "%{public}@UpdateValueForAttributeReport (sync): Report OccupiedHeatingSetpoint %@"
+ "%{public}@UpdateValueForAttributeReport: An error occurred while trying to read the current System Mode: %@"
+ "%{public}@UpdateValueForAttributeReport: Handling Attribute report endpoint:%@ cluster:%@ attribute:%@ value:%@"
+ "%{public}@UpdateValueForAttributeReport: Report OccupiedCoolingSetpoint %@"
+ "%{public}@UpdateValueForAttributeReport: Report OccupiedHeatingSetpoint %@"
+ "%{public}@Updated ACL after user CAT update on server %@"
+ "%{public}@Updated Access Control List (Admin 0x%lX (%@), Operate 0x%lX (%@)) on accessory %@"
+ "%{public}@Updated additional characteristic %@ \nbased on characteristic \n%@"
+ "%{public}@Updated storage after refetching shared user certs"
+ "%{public}@Updating AccessoryConnectionRequest Idle time to: %f"
+ "%{public}@Updating CATs (admin %@, user %@) for FabricID (browser's %@, server's %@, storage's %@"
+ "%{public}@Updating FabricConnectionRequest Idle time to: %f"
+ "%{public}@Updating accessory ACL to remove administrative access to %@"
+ "%{public}@Using Cached Root certificate"
+ "%{public}@Using already cached values self.rootCert %@, self.operationalCert %@ self.ownerNodeID %@ self.ownerIPK %@"
+ "%{public}@V1 key pair root cert is updated. This will disrupt already paired accessories."
+ "%{public}@V1 key will be updated using new root cert. This will disrupt all paired accessories"
+ "%{public}@WED support %@ and eMAC Address %@"
+ "%{public}@Waiting for active thread operations to complete, add to pending queue"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): An error occurred while trying to read the current System Mode"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): An error occurred while trying to read the min/max cool setpoints"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): An error occurred while trying to read the min/max heat setpoints"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target cool temperature out of supported max setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target cool temperature out of supported min setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target heat temperature out of supported max setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target heat temperature out of supported min setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Thermostat Setpoint cannot be set in unexpected system mode: %ld"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Thermostat Setpoint cannot be set when system is off"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: An error occurred while trying to read the System Mode: %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: An error occurred while trying to read the max cool setpoint: %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: An error occurred while trying to read the max heat setpoint: %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: An error occurred while trying to read the min cool setpoint: %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: An error occurred while trying to read the min heat setpoint: %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Target cool temperature out of supported max setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Target cool temperature out of supported min setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Target heat temperature out of supported max setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Target heat temperature out of supported min setpoint limit. Setting it to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Thermostat Setpoint cannot be set in unexpected system mode: %ld"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Thermostat Setpoint cannot be set when system is off"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Wrote to OccupiedCoolingSetpoint cluster value %@, error: %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint: Wrote to OccupiedHeatingSetpoint cluster value %@, error: %@"
+ "%{public}@Write attribute RockSetting %@"
+ "%{public}@Write attribute RockSetting 0"
+ "%{public}@Write completion contains tuple for characteristic %@ with value:%@ Error: %@"
+ "%{public}@Write due to active characteristic (sync): Wrote to system mode attribute, value:%@ (Off)"
+ "%{public}@Write due to target heater cooler state (sync): Wrote to system mode attribute, value:%@ (%@)"
+ "%{public}@Wrote to system mode attribute for Active Characteristic, value:%@ (Off), error:%@"
+ "%{public}@Wrote to system mode attribute for Target Heater Cooler State Characteristic, value:%@ (%@), error:%@"
+ "%{public}@f/%x/n doesn't match "
+ "%{public}@handleBDXQueryForNodeID command {nodeID = %@, blockSize: %@, blockIndex: %@}. Error: %@"
+ "%{public}@iPhoneOnly Pairing and Control feature is disabled"
+ "%{public}@iPhoneOnly Pairing and Control feature is enabled"
+ "%{public}@iPhoneOnly Pairing and Control feature is enabled through profile"
+ "%{public}@merged into existing connection"
+ "%{public}@moveToColorTemperatureWithParams colorTemperature %@, optionsMask %@, error %@"
+ "%{public}@moveToColorTemperatureWithParams completed with colorTemperature %@, transitionTime: %@, optionsMask %@, error %@"
+ "%{public}@moveToPluginColorTemperatureWithParams colorTemperature %@, optionsMask %@, error %@"
+ "%{public}@no fabricID was provided, restarting with fabric with active client: %@"
+ "%{public}@not reading thread network prerequisites"
+ "%{public}@startAccessoryPairingWithExtendedMACAddress completed, error: %@"
+ "%{public}@startDiscoveringAccessoryServers platform is iOS and resident is down - allowing discovery"
+ "%{public}@stopAccessoryPairingWithCompletion completed, error: %@"
+ "-[HMMTRAccessoryConnectionRequest _getAllPendingOperations]"
+ "-[HMMTRAccessoryConnectionRequest _kickIdleTimer]"
+ "-[HMMTRAccessoryConnectionRequest _numPendingOperations]"
+ "-[HMMTRAccessoryConnectionRequest abortAllPendingOperations:]"
+ "-[HMMTRAccessoryConnectionRequest executeAllPendingOperations]"
+ "-[HMMTRAccessoryConnectionRequest mergeAccessoryConnectionRequest:]"
+ "-[HMMTRAccessoryServer finishPairing]_block_invoke"
+ "-[HMMTRFabricConnectionRequest _addToActiveIPConnections:]"
+ "-[HMMTRFabricConnectionRequest _connectPendingConnections]"
+ "-[HMMTRFabricConnectionRequest _kickIdleTimer]"
+ "-[HMMTRFabricConnectionRequest connectToAccessoryWhenAllowed:]_block_invoke"
+ "-[HMMTRFabricConnectionRequest operationsCompletedForAccessoryConnectionRequest:]"
+ "-[HMMTRFabricConnectionRequest retryOperations]_block_invoke"
+ "-[HMMTRFabricConnectionRequest startOperations]_block_invoke"
+ "-[HMMTRFabricConnectionRequest stopOperations]_block_invoke"
+ "-[HMMTRFabricConnectionRequest suspendOperations]_block_invoke"
+ "/ system commissioner"
+ "1\x12"
+ "2"
+ "5\x1d"
+ "@\"<HMMTRFabricDelegate>\""
+ "@\"<HMMTRResidentStateManagerDelegate>\""
+ "@\"<HMMTRThreadRadioControllerDelegate>\""
+ "@\"HMMTRAccessControl\""
+ "@\"HMMTRFabric\""
+ "@\"HMMTRFabricConnectionRequest\""
+ "@\"HMMTRThreadRadioManager\""
+ "@\"MTRBaseClusterDoorLock\""
+ "@\"NSMutableOrderedSet\""
+ "@36@0:8@16@24C32"
+ "@36@0:8@16C24@28"
+ "@44@0:8@16@24B32@?36"
+ "@44@0:8@16q24B32@36"
+ "A&9,\x1f\v\x15"
+ "Access Control"
+ "ActiveIPRequests:"
+ "ActiveThreadRequests:"
+ "ActiveThreadWEDRequests:"
+ "B20@?0@\"HMMTRControllerWrapper\"8B16"
+ "B32@0:8@16^@24"
+ "C16@0:8"
+ "Cool"
+ "Current User Privilege"
+ "FabricID"
+ "HMMTRAccessControl"
+ "HMMTRAccessoryConnectionRequest"
+ "HMMTRCachedFabricCertificateData"
+ "HMMTRColorControlColorTemperatureAttributes"
+ "HMMTRFabric"
+ "HMMTRFabricConnectionRequest"
+ "HMMTRFanControl"
+ "HMMTRFeatures"
+ "HMMTRResidentStateManagerDelegate"
+ "HMMTRSyncClusterColorControl"
+ "HMMTRSyncClusterFanControl"
+ "HMMTRThreadRadioManager"
+ "Heat"
+ "MatteriPhoneOnlyPairing"
+ "MatteriPhoneOnlyPairingEnabled"
+ "MatteriPhoneOnlyPairingForIP"
+ "MatteriPhoneOnlyPairingForIPEnabled"
+ "None"
+ "Owner"
+ "PendingRequests:"
+ "Regular User"
+ "System Commissioner"
+ "SystemCommissionerFabric"
+ "T@\"<HMMTRFabricDelegate>\",R,W,N,V_delegate"
+ "T@\"<HMMTRResidentStateManagerDelegate>\",W,V_delegate"
+ "T@\"<HMMTRThreadRadioControllerDelegate>\",W,V_delegate"
+ "T@\"HMFTimer\",R,N,V_idleTimer"
+ "T@\"HMMTRAccessControl\",&,N,V_accessControl"
+ "T@\"HMMTRAccessoryServer\",W,N,V_server"
+ "T@\"HMMTRFabric\",W,V_fabric"
+ "T@\"HMMTRFabricConnectionRequest\",W,N,V_parentFabricRequest"
+ "T@\"HMMTRThreadRadioManager\",R,N,V_threadRadioManager"
+ "T@\"MTRBaseClusterDoorLock\",&,V_baseDoorLock"
+ "T@\"NSMutableSet\",&,V_fabricsWithActiveClients"
+ "T@\"NSMutableSet\",&,V_nodesWithPendingACLOverwrite"
+ "T@\"NSNumber\",&,N,V_caseAuthenticatedTag"
+ "T@\"NSNumber\",&,N,V_fabricIDOfActiveThreadNetwork"
+ "T@\"NSNumber\",C,N,V_colorMode"
+ "T@\"NSNumber\",C,N,V_colorTemperatureMireds"
+ "T@\"NSNumber\",C,N,V_remainingTime"
+ "T@\"NSNumber\",C,V_fabricID"
+ "T@\"NSNumber\",R,C,V_fabricID"
+ "T@\"NSNumber\",R,C,V_ownerNode"
+ "T@\"NSNumber\",R,N,V_fabricID"
+ "T@\"NSNumber\",R,N,V_nodeID"
+ "T@\"NSNumber\",R,N,V_objectID"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_retryConnectionQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_characteristicsOperationDispatchQueue"
+ "T@\"NSString\",&,N,V_eMACAddress"
+ "T@\"NSString\",&,N,V_eMACAddressOfWEDAccessory"
+ "TB,GisFabricCreationInProgress,V_fabricCreationInProgress"
+ "TB,N,GisWEDDevice,V_wedDevice"
+ "TB,N,V_active"
+ "TB,N,V_caseAuthenticatedTagsUpdated"
+ "TB,N,V_delayDiscovery"
+ "TB,N,V_deviceSupportsThreadService"
+ "TB,N,V_isPairingActive"
+ "TB,N,V_isWEDConnectionRetryActive"
+ "TB,N,V_pendingThreadStart"
+ "TB,N,V_preventDisconnect"
+ "TB,N,V_threadNetworkActivatedForSystemCommissionerFabric"
+ "TB,R,GisSystemCommissionerFabric,V_systemCommissionerFabric"
+ "TB,R,N,V_systemCommissionerFabric"
+ "TB,V_preventThreadStopDuringStackRestart"
+ "TC,N,V_connectionIdleTime"
+ "TC,N,V_fabricIdleTime"
+ "TQ,N,V_connectionPriority"
+ "TQ,V_currentUserPrivilege"
+ "ThreadService"
+ "ThreadServiceEnabled"
+ "Tq,N,V_lastKnownThreadNetworkConnectionState"
+ "_abortAllOperationsForFabricID:"
+ "_accessControl"
+ "_active"
+ "_activeIPConnectionRequests"
+ "_activeThreadConnectionRequests"
+ "_activeThreadWEDConnectionRequests"
+ "_addToActiveFabrics:"
+ "_addToActiveIPConnections:"
+ "_addToActiveThreadConnections:"
+ "_addToActiveThreadWEDConnections:"
+ "_addToPendingConnections:"
+ "_addToPendingFabrics:"
+ "_baseDoorLock"
+ "_cachedRootCertificateIfValidForFabricID:"
+ "_calculateFabricIdleTime"
+ "_caseAuthenticatedTag"
+ "_caseAuthenticatedTagsUpdated"
+ "_characteristicsOperationDispatchQueue"
+ "_checkAndUpdateValidityPeriodOfV1Keypair:newKeyPair:"
+ "_colorMode"
+ "_colorTemperatureMireds"
+ "_connectPendingConnections"
+ "_connectPendingFabricConnections"
+ "_connectionIdleTime"
+ "_connectionPriority"
+ "_continueNetworkProvisioning"
+ "_createTransientOperationalCertificateForFabricID:"
+ "_currentUserPrivilege"
+ "_delayDiscovery"
+ "_deviceSupportsThreadService"
+ "_disconnectFromIdleFabric:"
+ "_eMACAddress"
+ "_eMACAddressOfWEDAccessory"
+ "_establishConnectionWhenAllowedWithAccessoryConnectionRequest:"
+ "_establishConnectionWhenAllowedWithFabricConnectionRequest:"
+ "_fabric"
+ "_fabricCreationInProgress"
+ "_fabricIDOfActiveThreadNetwork"
+ "_fabricIdleTime"
+ "_fabricsWithActiveClients"
+ "_fabricsWithActiveConnections"
+ "_fabricsWithPendingConnections"
+ "_fetchAdditionalThreadNetworkInformationWithCompletion:"
+ "_fetchCert2ForFabricWithID:isOwner:completion:"
+ "_fetchOperationalCertificatesFromResidentForFabricID:completion:"
+ "_fetchSharedUserCert2ForFabricWithID:reFetch:completion:"
+ "_getAllPendingOperations"
+ "_getOperationalHardwareAddressFromReadValue:"
+ "_getOperationalNetworkAddressForAccessory:"
+ "_hasActiveAccessoryConnections"
+ "_idleTimer"
+ "_isPairingActive"
+ "_isWEDConnectionRetryActive"
+ "_kickIdleTimer"
+ "_lastKnownThreadNetworkConnectionState"
+ "_nodesWithPendingACLOverwrite"
+ "_numPendingOperations"
+ "_objectID"
+ "_operationalCertificateFromSdkCertificatesForFabricID:"
+ "_ownerNode"
+ "_parentFabricRequest"
+ "_pendingConnectionRequests"
+ "_pendingOperations"
+ "_pendingThreadStart"
+ "_preventDisconnect"
+ "_preventThreadStopDuringStackRestart"
+ "_queryColorModeFromClusterAtCHIPEndpoint:device:callbackQueue:completionHandler:"
+ "_remainingTime"
+ "_removeFromActiveFabrics:"
+ "_removeFromActiveIPConnections:"
+ "_removeFromActiveThreadConnections:"
+ "_removeFromActiveThreadWEDConnections:"
+ "_removeFromPendingConnections:"
+ "_removeFromPendingFabrics:"
+ "_removeSharedAdminControllerNodeIDFromACLWithCompletion:"
+ "_restartConnectionIdleTimer:"
+ "_restartDiscovery"
+ "_retryConnectionQueue"
+ "_retryWEDConnectionToAccessory"
+ "_rootCertificateFromSdkCertificatesForFabricID:"
+ "_stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:"
+ "_stopSystemCommissionerFabricID:"
+ "_suspendOperationsForFabricID:"
+ "_threadNetworkActivatedForSystemCommissionerFabric"
+ "_threadRadioManager"
+ "_tryAddAccessoryConnectionRequestToExistingFabric:"
+ "_tryMergeIntoExistingConnection:"
+ "_updateACLOnPairedAccessories"
+ "_updateAccessoryControlListForServer:completion:"
+ "_updateActiveThreadWEDConnectionsIdleTime:"
+ "_updateConnectionIdleTime:"
+ "_updateFabricIDOfActiveThreadNetwork:isFabricIDOfSystemCommissioner:"
+ "_wedDevice"
+ "abortAllOperations"
+ "abortAllPendingOperations:"
+ "abortOperationsForAccessoryServer:"
+ "abortOperationsForConnectionRequest:"
+ "accessControl"
+ "accessoryAdministerPrivilegeCATID:"
+ "accessoryOperatePrivilegeCATID:"
+ "accessoryServerBrowser:cacheOperationalCertData:forFabricID:"
+ "accessoryServerBrowser:getCachedOperationalCertificateDataForFabricID:completion:"
+ "accessoryServerBrowser:getOperationalCertificatesForFabricID:publicKey:completion:"
+ "active"
+ "activeIPConnectionRequests"
+ "activeThreadConnectionRequests"
+ "activeThreadWEDConnectionRequests"
+ "addFabricWithActiveClientForFabricID:"
+ "addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:"
+ "allowDisconnect"
+ "anyObject"
+ "appleHomeFabricWithID:"
+ "baseDoorLock"
+ "caseAuthenticatedTag"
+ "caseAuthenticatedTagsUpdated"
+ "characteristicsOperationDispatchQueue"
+ "checkAndUpdateExpiryOfCertificate:keyPair:newCertificate:"
+ "colorMode"
+ "colorMode: %@ remainingTime: %@ colorTemperatureMireds: %@"
+ "com.apple.homed"
+ "connectToAccessoryWhenAllowed:"
+ "connectToAccessoryWhenAllowed:highPriority:completion:"
+ "connectToAccessoryWithExtendedMACAddress:completion:"
+ "connectToAccessoryWithExtendedMACAddress:withFabricID:completion:"
+ "connectionIdleTime"
+ "connectionPriority"
+ "currentFabric"
+ "currentUserPrivilege"
+ "delayDiscovery"
+ "deviceSupportsThreadService"
+ "didFinishPairingAccessoryServer:operationDisabled:"
+ "disableFeatureiPhoneOnlyPairingControlForTests"
+ "eMACAddress"
+ "eMACAddressOfWEDAccessory"
+ "enableFeatureiPhoneOnlyPairingControlForTests"
+ "executeAllPendingOperations"
+ "extendedMACAddress"
+ "fabric"
+ "fabricCreationInProgress"
+ "fabricIDOfActiveThreadNetwork"
+ "fabricIdleTime"
+ "fabricsWithActiveClients"
+ "fabricsWithActiveConnections"
+ "fabricsWithPendingConnections"
+ "fetchCachedOperationalCertificateForFabricID:completionHandler:"
+ "fetchExtendedMACAddressFromDevice:completion:"
+ "fetchOperationalCertificatesFromResidentForPublicKey:fabricID:completionHandler:"
+ "fetchSharedUserCertForFabricWithID:reFetch:completion:"
+ "fetchWEDSupportInformationFromDevice:completion:"
+ "fire"
+ "getNOCFromResidentForSharedUserForFabric:"
+ "getThreadNetworkConnectionStateWithFabricID:"
+ "getThreadNetworkNodeTypeWithFabricID:"
+ "handleHomeAddedAccessoryWithNodeID:fabric:"
+ "handleHomeDeletionWithFabric:"
+ "handleRegularUserAdded"
+ "handleResidentReachabilityChangeForFabric:"
+ "handleSharedAdminAdded"
+ "handleThreadRadioStateChanged"
+ "handleUpdateNotificationsEnabled:forFabric:"
+ "hasPendingHighPriorityConnectionRequest"
+ "hmmtr.accessControl"
+ "hmmtr.accessory.server.chrop"
+ "hmmtr.browser.connectionRequest"
+ "hmmtr.browser.fabricConnectionRequest"
+ "hmmtr.fabric"
+ "hmmtr.fancontrol"
+ "hmmtr.thread.manager"
+ "idleTimer"
+ "initSystemCommissionerFabricWithDelegate:"
+ "initWithBrowser:"
+ "initWithDelegate:"
+ "initWithFabricID:rootCert:operationalCert:ownerNode:ipk:"
+ "initWithMinInterval:maxInterval:"
+ "initWithQueue:browser:fabricID:systemCommissionerFabric:"
+ "initWithQueue:server:highPriority:completion:"
+ "isCurrentDeviceAllowedAccessoryControlDespiteReachableResidentForFabric:"
+ "isCurrentDeviceMobileAndAllowedAccessoryControl"
+ "isCurrentDeviceMobileAndResidentReachable"
+ "isCurrentUserOwner"
+ "isFabricCreationInProgress"
+ "isHH2Enabled"
+ "isOwnerForHomeWithFabric:"
+ "isPairingActive"
+ "isPrimaryResidentNodeReachable"
+ "isPrimaryResidentNodeReachableAndThreadCapable"
+ "isReadyToEstablishWEDConnection"
+ "isThreadNetworkConnected"
+ "isValidCATSubject:"
+ "isWEDConnectionRetryActive"
+ "isWEDDevice"
+ "lastKnownThreadNetworkConnectionState"
+ "legacyNodeIDForCurrentFabric"
+ "mergeAccessoryConnectionRequest:"
+ "mergeExistingAclEntries:withAdminNodes:regularUserNodes:"
+ "mergeExistingAclEntries:withNewNodes:withPrivilege:"
+ "moveToColorTemperatureWithParams:completionHandler:"
+ "moveToColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:"
+ "moveToCustomColorTemperatureValue:fromColorTemperature:transitionTime:completionHandler:"
+ "moveToPluginColorTemperatureWithParams:completionHandler:"
+ "moveToPluginColorTemperatureWithParams:expectedValues:expectedValueInterval:completionHandler:"
+ "nodesWithPendingACLOverwrite"
+ "notifyThreadRadioStateChanged:nodeType:"
+ "notifyWakeOnDeviceConnectionChanged:eMACAddress:"
+ "objectID"
+ "operationsCompletedForAccessoryConnectionRequest:"
+ "operationsCompletedForFabricConnectionRequest:"
+ "operationsStartedForFabricConnectionRequest:"
+ "orderedSet"
+ "ownerNode"
+ "parentFabricRequest"
+ "pendingConnectionRequests"
+ "pendingThreadStart"
+ "persistLegacyControllerNodeWithDictionary:"
+ "preventDisconnect"
+ "preventThreadStopDuringStackRestart"
+ "readAttributeColorCapabilitiesWithCompletion:"
+ "readAttributeColorModeWithCompletion:"
+ "readAttributeColorModeWithCompletionHandler:"
+ "readAttributeColorModeWithParams:"
+ "readAttributeColorTemperatureMiredsWithCompletion:"
+ "readAttributeColorTemperatureMiredsWithParams:"
+ "readAttributePluginColorTemperatureMiredsWithCompletionHandler:"
+ "readAttributePluginColorTemperatureMiredsWithParams:"
+ "readAttributePluginRockSettingWithCompletionHandler:"
+ "readAttributePluginRockSettingWithParams:"
+ "readAttributeRemainingTimeWithCompletion:"
+ "readAttributeRockSettingWithCompletion:"
+ "readAttributeRockSettingWithParams:"
+ "readAttributeRockSupportWithCompletion:"
+ "readAttributeRockSupportWithParams:"
+ "readAttributeStartUpColorTemperatureMiredsWithCompletion:"
+ "readColorTemperatureAttributesWithCompletion:queue:"
+ "readStartUpColorTemperatureWithCompletion:"
+ "remainingTime"
+ "removeNode:withPrivilge:fromExistingAclEntries:"
+ "restartDiscovery"
+ "retryConnectionQueue"
+ "retryOperations"
+ "rockSettingValue"
+ "rockSupportValue"
+ "setAccessControl:"
+ "setActive:"
+ "setBaseDoorLock:"
+ "setCaseAuthenticatedTag:"
+ "setCaseAuthenticatedTagsUpdated:"
+ "setColorMode:"
+ "setColorTemperature:"
+ "setConnectionIdleTime:"
+ "setConnectionPriority:"
+ "setCurrentUserPrivilege:"
+ "setDelayDiscovery:"
+ "setDeviceSupportsThreadService:"
+ "setEMACAddress:"
+ "setEMACAddressOfWEDAccessory:"
+ "setFabric:"
+ "setFabricCreationInProgress:"
+ "setFabricIDOfActiveThreadNetwork:"
+ "setFabricIdleTime:"
+ "setFabricsWithActiveClients:"
+ "setIsPairingActive:"
+ "setIsWEDConnectionRetryActive:"
+ "setLastKnownThreadNetworkConnectionState:"
+ "setNodesWithPendingACLOverwrite:"
+ "setParentFabricRequest:"
+ "setPendingThreadStart:"
+ "setPreventDisconnect:"
+ "setPreventThreadStopDuringStackRestart:"
+ "setRemainingTime:"
+ "setRetryConnectionQueue:"
+ "setServer:"
+ "setThreadNetworkActivatedForSystemCommissionerFabric:"
+ "setWedDevice:"
+ "setWithObject:"
+ "setupThreadPairing"
+ "startAccessoryPairingWithExtendedMACAddress:fabricID:isWedDevice:completion:"
+ "startAccessoryPairingWithExtendedMACAddress:isWedDevice:completion:"
+ "startOperations"
+ "startThreadRadioForHomeWithFabricID:"
+ "startThreadRadioForHomeWithFabricID:preventDisconnect:"
+ "startThreadRadioForSystemCommissionerFabricID:"
+ "startThreadRadioForUserPreferredNetwork"
+ "stopAccessoryPairingWithCompletion:"
+ "stopAccessoryPairingWithFabricID:completion:"
+ "stopMoveStepWithParams:completion:"
+ "stopMoveToColorTemperatureCommandWithCompletion:"
+ "stopOperations"
+ "stopThreadRadioForHomeWithFabricID:"
+ "stopThreadRadioForSystemCommissionerFabricID:"
+ "stopThreadRadioForUserPreferredNetwork"
+ "subscribeAttributeColorModeWithParams:subscriptionEstablished:reportHandler:"
+ "subscribeAttributeReportForColorModeWithCompletion:"
+ "supportsColorTemperature:"
+ "suspendOperations"
+ "swingValue"
+ "targets"
+ "threadNetworkActivatedForSystemCommissionerFabric"
+ "threadRadioManager"
+ "unsetFeatureiPhoneOnlyPairingControlForTests"
+ "updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:"
+ "updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:"
+ "updateAccessoryControlToRemoveAdministratorNode:completion:"
+ "updateConnectionIdleTime:"
+ "updatedValuePluginRockSettingForAttributeReport:responseHandler:"
+ "v16@?0@\"HMMTRCachedFabricCertificateData\"8"
+ "v20@0:8C16"
+ "v24@0:8@\"HMMTRFabric\"16"
+ "v24@0:8d16"
+ "v28@0:8B16@\"HMMTRFabric\"20"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"HMMTRCachedFabricCertificateData\">24"
+ "v32@0:8@?16@24"
+ "v32@0:8q16q24"
+ "v88@0:8@16@?24@?32@?40@?48@?56B64B68@72@?80"
+ "wedDevice"
+ "wedSupport"
+ "writeAttributePluginRockSettingWithValue:completionHandler:"
+ "writeAttributePluginRockSettingWithValue:expectedValueInterval:"
+ "writeAttributeRockSettingWithValue:completionHandler:"
+ "writeAttributeRockSettingWithValue:expectedValueInterval:"
+ "writeAttributeStartUpColorTemperatureMiredsWithValue:completion:"
+ "writeStartUpColorTemperature:completion:"
+ "\x91"
+ "\xd1A"
+ "\xe2\x92\xf0\xf0\x91"
- "\x14"
- "%{public}@Accessory with node ID %@ was added to home with fabricID %@"
- "%{public}@An error occurred while trying to read the System Mode: %@"
- "%{public}@An error occurred while trying to read the control sequence of operation"
- "%{public}@An error occurred while trying to read the control sequence of operation: %@"
- "%{public}@An error occurred while trying to read the current System Mode"
- "%{public}@An error occurred while trying to read the current System Mode: %@"
- "%{public}@An error occurred while trying to read the local temperature"
- "%{public}@An error occurred while trying to read the local temperature: %@"
- "%{public}@An error occurred while trying to read the max cool setpoint: %@"
- "%{public}@An error occurred while trying to read the max heat setpoint: %@"
- "%{public}@An error occurred while trying to read the min cool setpoint: %@"
- "%{public}@An error occurred while trying to read the min heat setpoint: %@"
- "%{public}@An error occurred while trying to read the min/max cool setpoints"
- "%{public}@An error occurred while trying to read the min/max heat setpoints"
- "%{public}@An error occurred while trying to read the occupied cooling point"
- "%{public}@An error occurred while trying to read the occupied cooling point: %@"
- "%{public}@An error occurred while trying to read the occupied heating point"
- "%{public}@An error occurred while trying to read the occupied heating point: %@"
- "%{public}@An error occurred while trying to read the system mode"
- "%{public}@An error occurred while trying to read the system mode: %@"
- "%{public}@Attempting to sync to remote storage when storageSyncPending = %@"
- "%{public}@Compute Active characteristic, handling Attribute report endpoint:%@ cluster:%@ attribute:%@ value:%@"
- "%{public}@Compute current heater cooler state, handling Attribute report endpoint:%@ cluster:%@ attribute:%@ value:%@"
- "%{public}@Compute current heating cooling state, handling Attribute report endpoint:%@ cluster:%@ attribute:%@ value:%@"
- "%{public}@Compute target heater cooler state, handling Attribute report endpoint:%@ cluster:%@ attribute:%@ value:%@"
- "%{public}@Controller Node ID from cached NOC (%@) doesn't match expected value (%@)"
- "%{public}@Corrupted key value store contains %@"
- "%{public}@Couldn't extract certificate info for f/%x/r"
- "%{public}@Couldn't get thermostat running mode from device. Ignoring error"
- "%{public}@Couldn't get thermostat running mode from device. Ignoring error: %@"
- "%{public}@Failed to re-create certificate cached root certificate with new validity %@ due to error %@"
- "%{public}@Failed to re-create certificate f/%x/r with new validity %@ due to error %@"
- "%{public}@Faking a color temperature attribute report (50) on endpoint %@ upon hue/sat command invocation"
- "%{public}@Fetch fabric parameters from storage"
- "%{public}@Got coolPointValue value: %@"
- "%{public}@Got coolPointValue value: %ld"
- "%{public}@Got heatPointValue value: %@"
- "%{public}@Got heatPointValue value: %ld"
- "%{public}@Got runningModeValue value: %@"
- "%{public}@Got runningModeValue value: %ld"
- "%{public}@Got systemModeValue value: %@"
- "%{public}@Got systemModeValue value: %ld"
- "%{public}@Got temperatureValue value: %@"
- "%{public}@Got temperatureValue value: %ld"
- "%{public}@IssuerID from cached Root (%@) doesn't match issuerID of the SDK root certificate (%@)"
- "%{public}@Read OccupiedCoolingSetpoint %@"
- "%{public}@Read OccupiedCoolingSetpoint %@, error: %@"
- "%{public}@Read OccupiedHeatingSetpoint %@"
- "%{public}@Read OccupiedHeatingSetpoint %@, error: %@"
- "%{public}@Read local temperature %@"
- "%{public}@Read local temperature %@, error: %@"
- "%{public}@Report OccupiedCoolingSetpoint %@"
- "%{public}@Report OccupiedHeatingSetpoint %@"
- "%{public}@Storage seems to be corrupt, resetting it"
- "%{public}@Storing the initial Matter storage to remote"
- "%{public}@Successfully re-created cached root certificate with new validity %@"
- "%{public}@Successfully re-created certificate f/%x/r with new validity %@"
- "%{public}@Target cool temperature out of supported max setpoint limit. Setting it to %@"
- "%{public}@Target cool temperature out of supported min setpoint limit. Setting it to %@"
- "%{public}@Target heat temperature out of supported max setpoint limit. Setting it to %@"
- "%{public}@Target heat temperature out of supported min setpoint limit. Setting it to %@"
- "%{public}@Thermostat Setpoint cannot be set in unexpected system mode: %ld"
- "%{public}@Thermostat Setpoint cannot be set when system is off"
- "%{public}@Thermostat Setpoint should not be read in unexpected system mode: %ld"
- "%{public}@Unexpected, target temperature characteristic not found"
- "%{public}@Unsupported control sequence of operation value: %@"
- "%{public}@Unsupported system mode: %@"
- "%{public}@Unsupported system mode: %ld"
- "%{public}@Updated Apple Home certificates %@ to have no expiration"
- "%{public}@Updated system commissioner certificate %@ with error %@"
- "%{public}@Write completion contains tuple with value:%@ error: %@"
- "%{public}@Wrote to OccupiedCoolingSetpoint cluster value %@, error: %@"
- "%{public}@Wrote to OccupiedHeatingSetpoint cluster value %@, error: %@"
- "%{public}@Wrote to system mode attribute, value:%@"
- "%{public}@Wrote to system mode attribute, value:%@, error:%@"
- "%{public}@f/%x/r expires in distant future. No update needed %@ vs %@"
- "(\x13\x11\x18\x1c"
- "1&8+\x1f\n\x15"
- "5\x1c"
- "_stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:"
- "addIssuerKeyData:forUserIndex:flow:"
- "fetchSharedUserCertForFabricWithID:completion:"
- "getOperationalHardwareAddressFromReadValue:"
- "handleHomeAddedAccessoryWithNodeID:fabricID:"
- "ipkForCurrentFabricID"
- "isOwnerForHomeWithFabricID:"
- "isStorageCorruptForKeyValueStore:"
- "moveToCustomColorTemperatureValue:transitionTime:completionHandler:"
- "targetActivationNumber"
- "updateCertificateExpiryInStorage:keyPair:"
- "v20@?0@\"HMMTRControllerWrapper\"8B16"
- "v96@0:8@16@24@?32@?40@?48@?56@?64B72B76@80@?88"
- "\xa11"
- "҂\xf0\xf0q"

```
