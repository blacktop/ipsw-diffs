## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1092.4.10.0.0
-  __TEXT.__text: 0xdf9e8
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x6920
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x13a4
-  __TEXT.__cstring: 0x4168
-  __TEXT.__oslogstring: 0x1e298
+1124.5.8.1.1
+  __TEXT.__text: 0xf7778
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_methlist: 0x6fc8
+  __TEXT.__const: 0xb8
+  __TEXT.__gcc_except_tab: 0x15b0
+  __TEXT.__cstring: 0x4725
+  __TEXT.__oslogstring: 0x20517
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x20cc
-  __TEXT.__objc_classname: 0xbe4
-  __TEXT.__objc_methname: 0x1a4b2
-  __TEXT.__objc_methtype: 0x23a1
-  __TEXT.__objc_stubs: 0x10b00
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x3600
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __TEXT.__unwind_info: 0x22c4
+  __TEXT.__objc_classname: 0xcc5
+  __TEXT.__objc_methname: 0x1bc78
+  __TEXT.__objc_methtype: 0x253a
+  __TEXT.__objc_stubs: 0x117c0
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x3828
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8b50
-  __DATA_CONST.__objc_selrefs: 0x4d60
-  __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__objc_const: 0x27a8
-  __AUTH_CONST.__cfstring: 0x4880
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__objc_intobj: 0xf78
+  __DATA_CONST.__objc_const: 0x9500
+  __DATA_CONST.__objc_selrefs: 0x50c0
+  __DATA_CONST.__objc_classrefs: 0x708
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_arraydata: 0x1f0
+  __AUTH_CONST.__objc_const: 0x2a78
+  __AUTH_CONST.__cfstring: 0x4f80
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__objc_intobj: 0x10f8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x488
-  __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_classrefs: 0x6c8
-  __DATA.__objc_superrefs: 0x200
-  __DATA.__objc_ivar: 0x760
-  __DATA.__data: 0x840
-  __DATA.__bss: 0x2c8
-  __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x60
+  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH.__objc_data: 0x1680
+  __DATA.__objc_ivar: 0x7f8
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0x2b8
+  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3037
-  Symbols:   10552
-  CStrings:  6305
+  Functions: 3210
+  Symbols:   11136
+  CStrings:  6668
 
Symbols:
+ +[HMMTRControllerData logCategory]
+ +[HMMTRFabricData logCategory]
+ +[HMMTRPairingWindowInfoTable logCategory]
+ +[HMMTRUtilities __baseClusterValueForAttributeDeviceListFromReadValue:forIdentify:]
+ +[HMMTRUtilities mtrBaseClusterValueFromMTRClusterReadResultValue:clusterIdentifier:attributeIdentifier:forIdentify:]
+ +[HMMTRVendorMetadataFileStore logCategory]
+ -[HMMTRAccessControl init]
+ -[HMMTRAccessControl privilegeGetter]
+ -[HMMTRAccessControl setPrivilegeGetter:]
+ -[HMMTRAccessoryServer _deregisterDeviceConnectedStateCaptureHandler]
+ -[HMMTRAccessoryServer _deregisterPartsListStateCaptureHandler]
+ -[HMMTRAccessoryServer _deregisterStateCaptureHandlers]
+ -[HMMTRAccessoryServer _queryBridgedAccessoryAndUnreachablePerCacheForCharacteristic:completion:]
+ -[HMMTRAccessoryServer _readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:]
+ -[HMMTRAccessoryServer _registerStateCaptureHandler:stateCaptureInformation:]
+ -[HMMTRAccessoryServer bridgedAccessoryReachabilityReaderTimeoutNSecs]
+ -[HMMTRAccessoryServer createStateData:data:]
+ -[HMMTRAccessoryServer dealloc]
+ -[HMMTRAccessoryServer deviceConnectedStateCaptureInformation]
+ -[HMMTRAccessoryServer deviceConnectedStateHandle]
+ -[HMMTRAccessoryServer dumpState:]
+ -[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]
+ -[HMMTRAccessoryServer hasPreferredLocalLink]
+ -[HMMTRAccessoryServer partsListStateCaptureHandle]
+ -[HMMTRAccessoryServer partsListStateCaptureInformation]
+ -[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]
+ -[HMMTRAccessoryServer reportDistributor]
+ -[HMMTRAccessoryServer residentReachabilityUpdateWaitTimer]
+ -[HMMTRAccessoryServer setBridgedAccessoryReachabilityReaderTimeoutNSecs:]
+ -[HMMTRAccessoryServer setDeviceConnectedStateCaptureInformation:]
+ -[HMMTRAccessoryServer setDeviceConnectedStateHandle:]
+ -[HMMTRAccessoryServer setPartsListStateCaptureHandle:]
+ -[HMMTRAccessoryServer setPartsListStateCaptureInformation:]
+ -[HMMTRAccessoryServer setResidentReachabilityUpdateWaitTimer:]
+ -[HMMTRAccessoryServer setStateCaptureDeviceConnectedTimer:]
+ -[HMMTRAccessoryServer setStateCapturePartsListTimer:]
+ -[HMMTRAccessoryServer stateCaptureDeviceConnectedTimer]
+ -[HMMTRAccessoryServer stateCapturePartsListTimer]
+ -[HMMTRAccessoryServerBrowser _connectPendingFabricConnectionsForFabricID:]
+ -[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]
+ -[HMMTRAccessoryServerBrowser isCurrentDeviceAllowedAccessoryControlDespiteReachableResident]
+ -[HMMTRAccessoryServerBrowser overrideCurrentFabricID:]
+ -[HMMTRAccessoryServerBrowser pairingWindowInfoTable]
+ -[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]
+ -[HMMTRAccessoryServerBrowser registerPairingWindowWithSetupPayload:duration:accessoryServer:]
+ -[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]
+ -[HMMTRAttributeReportDistributor .cxx_destruct]
+ -[HMMTRAttributeReportDistributor deregisterHandlerForAttributePath:registry:]
+ -[HMMTRAttributeReportDistributor distributeAttributeReport:]
+ -[HMMTRAttributeReportDistributor init]
+ -[HMMTRAttributeReportDistributor receivers]
+ -[HMMTRAttributeReportDistributor registerHandlerForAttributePath:queue:handler:]
+ -[HMMTRAttributeReportDistributorRegistry .cxx_destruct]
+ -[HMMTRAttributeReportDistributorRegistry initWithQueue:receiver:]
+ -[HMMTRAttributeReportDistributorRegistry queue]
+ -[HMMTRAttributeReportDistributorRegistry receiver]
+ -[HMMTRClusterDescription attributeID]
+ -[HMMTRClusterDescription clusterID]
+ -[HMMTRClusterDescription setAttributeID:]
+ -[HMMTRClusterDescription setClusterID:]
+ -[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]
+ -[HMMTRControllerData .cxx_destruct]
+ -[HMMTRControllerData attributeDescriptions]
+ -[HMMTRControllerData fabric]
+ -[HMMTRControllerData initWithFabric:]
+ -[HMMTRControllerData logIdentifier]
+ -[HMMTRControllerData nodeID]
+ -[HMMTRControllerData operationalCertificate]
+ -[HMMTRControllerData setFabric:]
+ -[HMMTRControllerData setNodeID:]
+ -[HMMTRControllerData setOperationalCertificate:]
+ -[HMMTRDescriptorClusterManager _fetchStateCaptureInformationForDevice:endpointID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager _fetchStateCaptureInformationForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClientClustersForDevice:endpointID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterAcceptedCommandsForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterAttributesForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterEventListForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterFabricIndexForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterFeatureMapForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterGeneratedCommandsForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchClusterRevisionForDevice:endpointID:clusterID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchDeviceTypesForDevice:endpointID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchPartsListForDevice:endpointID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchServerClustersForDevice:endpointID:callbackQueue:]
+ -[HMMTRDescriptorClusterManager fetchStateCaptureInformationForDevice:nodeId:server:callbackQueue:completionHandler:]
+ -[HMMTRDeviceReader .cxx_destruct]
+ -[HMMTRDeviceReader _readAttributeAfterAttributeListConfirmationWithCompletionHandler:]
+ -[HMMTRDeviceReader attributeID]
+ -[HMMTRDeviceReader clientQueue]
+ -[HMMTRDeviceReader clusterID]
+ -[HMMTRDeviceReader device]
+ -[HMMTRDeviceReader distributor]
+ -[HMMTRDeviceReader endpointID]
+ -[HMMTRDeviceReader initWithClientQueue:distributor:device:endpointID:clusterID:attributeID:]
+ -[HMMTRDeviceReader readAttributeWithCompletion:]
+ -[HMMTRDeviceReader reportTimeoutNSecs]
+ -[HMMTRDeviceReader setReportTimeoutNSecs:]
+ -[HMMTRFabric _createNewFabricData]
+ -[HMMTRFabric _getDataToPersist]
+ -[HMMTRFabric _loadFromDiskWithCompletion:]
+ -[HMMTRFabric _loadFromRemoteWithCompletion:]
+ -[HMMTRFabric _loadFromResidentWithCompletion:]
+ -[HMMTRFabric _loadFromStorageWithCompletion:]
+ -[HMMTRFabric cachedDataValid]
+ -[HMMTRFabric createNewFabricIdentityWithCompletion:]
+ -[HMMTRFabric currentDeviceNodeData]
+ -[HMMTRFabric fabricData]
+ -[HMMTRFabric initWithDelegate:queue:]
+ -[HMMTRFabric invalidateCachedData]
+ -[HMMTRFabric isCachedDataValid]
+ -[HMMTRFabric isValid]
+ -[HMMTRFabric loadFabricAndControllerDataWithCompletion:]
+ -[HMMTRFabric setCachedDataValid:]
+ -[HMMTRFabric setWorkQueue:]
+ -[HMMTRFabric workQueue]
+ -[HMMTRFabricData .cxx_destruct]
+ -[HMMTRFabricData attributeDescriptions]
+ -[HMMTRFabricData fabric]
+ -[HMMTRFabricData initWithFabric:]
+ -[HMMTRFabricData ipk]
+ -[HMMTRFabricData logIdentifier]
+ -[HMMTRFabricData residentNodeID]
+ -[HMMTRFabricData rootCert]
+ -[HMMTRFabricData setFabric:]
+ -[HMMTRFabricData setIpk:]
+ -[HMMTRFabricData setResidentNodeID:]
+ -[HMMTRFabricData setRootCert:]
+ -[HMMTRFirmwareUpdateStatus idleResetTimerQueue]
+ -[HMMTRFirmwareUpdateStatus idleResetTimer]
+ -[HMMTRFirmwareUpdateStatus setIdleResetTimer:]
+ -[HMMTRFirmwareUpdateStatus timerDidFire:]
+ -[HMMTRHAPEnumerator _createHAPServicesFromServiceDescriptions:topology:nodeID:accessoryEndpointID:services:startingServiceInstanceID:primaryAccessory:standaloneServiceLabelIndexMap:]
+ -[HMMTRHAPEnumerator _serviceLabelIndexMapForDescriptions:]
+ -[HMMTRIdentifyDevice _processChildNodesForEndpoint:completionHandler:]
+ -[HMMTRPairingWindowInfoTable .cxx_destruct]
+ -[HMMTRPairingWindowInfoTable _clearExpiredEntriesWithCurrentDate:]
+ -[HMMTRPairingWindowInfoTable init]
+ -[HMMTRPairingWindowInfoTable registerPairingWindowWithSetupPayload:currentDate:duration:accessoryServer:]
+ -[HMMTRPairingWindowInfoTable retrieveAccessoryServerForPairingWindowWithSetupPayload:currentDate:]
+ -[HMMTRPairingWindowInfoTable table]
+ -[HMMTRPairingWindowInfoTableEntry .cxx_destruct]
+ -[HMMTRPairingWindowInfoTableEntry accessoryServer]
+ -[HMMTRPairingWindowInfoTableEntry expirationDate]
+ -[HMMTRPairingWindowInfoTableEntry initWithAccessoryServer:expirationDate:]
+ -[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]
+ -[HMMTRStorage _cachedOperationalCertificateIfValidForFabricID:]
+ -[HMMTRStorage _createTransientOperationalCertificateForFabricID:rootCert:caseAuthenticatedTags:]
+ -[HMMTRStorage _nodeIDFromOperationalX509Certificate:]
+ -[HMMTRStorage fetchCertificatesFromStorageForFabricID:rootCert:operationalCert:residentNodeID:ipk:]
+ -[HMMTRStorage legacyNodeIDForFabricID:]
+ -[HMMTRStorage syncDataSourceDictionary:forFabric:]
+ -[HMMTRStorage(Records) extendedMACAddressForSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) setExtendedMACAddress:forSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) setWEDSupported:forSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) wedSupportedForSystemCommissionerFabricNode:]
+ -[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]
+ -[HMMTRSyncClusterDoorLock addUserAtUserIndex:withUserUniqueID:userType:flow:]
+ -[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]
+ -[HMMTRThreadRadioManager _shouldRetryWEDConnectionToAccessory]
+ -[HMMTRVendorMetadataFileStore .cxx_destruct]
+ -[HMMTRVendorMetadataFileStore _addProductInfoToMetadata:accessories:]
+ -[HMMTRVendorMetadataFileStore _addVendorInfoToMetadata:accessories:]
+ -[HMMTRVendorMetadataFileStore _saveMetadata:]
+ -[HMMTRVendorMetadataFileStore assetAvailablityUpdateForAccessoryID:assetID:]
+ -[HMMTRVendorMetadataFileStore fetchCloudMetadata]
+ -[HMMTRVendorMetadataFileStore fileManager]
+ -[HMMTRVendorMetadataFileStore fileURL]
+ -[HMMTRVendorMetadataFileStore initWithFileURL:]
+ -[HMMTRVendorMetadataFileStore initWithFileURL:uarpController:fileManager:]
+ -[HMMTRVendorMetadataFileStore metadata]
+ -[HMMTRVendorMetadataFileStore sendMessageToAccessory:uarpMsg:error:]
+ -[HMMTRVendorMetadataFileStore staticMetadataFileURL]
+ -[HMMTRVendorMetadataFileStore staticMetadata]
+ -[HMMTRVendorMetadataFileStore supportedAccessories:forProductGroup:]
+ -[HMMTRVendorMetadataFileStore uarpController]
+ GCC_except_table1002
+ GCC_except_table1130
+ GCC_except_table1131
+ GCC_except_table1149
+ GCC_except_table1150
+ GCC_except_table1151
+ GCC_except_table1152
+ GCC_except_table1153
+ GCC_except_table1156
+ GCC_except_table1158
+ GCC_except_table1159
+ GCC_except_table1160
+ GCC_except_table1161
+ GCC_except_table1162
+ GCC_except_table1163
+ GCC_except_table1164
+ GCC_except_table1212
+ GCC_except_table1218
+ GCC_except_table1310
+ GCC_except_table1333
+ GCC_except_table1362
+ GCC_except_table1395
+ GCC_except_table1421
+ GCC_except_table1438
+ GCC_except_table1486
+ GCC_except_table1659
+ GCC_except_table1663
+ GCC_except_table1714
+ GCC_except_table1770
+ GCC_except_table1815
+ GCC_except_table1835
+ GCC_except_table1836
+ GCC_except_table1837
+ GCC_except_table1848
+ GCC_except_table1849
+ GCC_except_table1850
+ GCC_except_table1851
+ GCC_except_table1852
+ GCC_except_table1853
+ GCC_except_table1854
+ GCC_except_table1861
+ GCC_except_table1863
+ GCC_except_table1867
+ GCC_except_table1885
+ GCC_except_table1899
+ GCC_except_table1905
+ GCC_except_table1916
+ GCC_except_table1918
+ GCC_except_table1926
+ GCC_except_table1942
+ GCC_except_table1948
+ GCC_except_table1955
+ GCC_except_table2044
+ GCC_except_table2305
+ GCC_except_table2310
+ GCC_except_table2313
+ GCC_except_table2323
+ GCC_except_table2388
+ GCC_except_table2402
+ GCC_except_table2404
+ GCC_except_table2411
+ GCC_except_table2412
+ GCC_except_table2437
+ GCC_except_table2438
+ GCC_except_table2472
+ GCC_except_table2511
+ GCC_except_table2544
+ GCC_except_table2548
+ GCC_except_table255
+ GCC_except_table2564
+ GCC_except_table2565
+ GCC_except_table2591
+ GCC_except_table2658
+ GCC_except_table2694
+ GCC_except_table2702
+ GCC_except_table2736
+ GCC_except_table2751
+ GCC_except_table2752
+ GCC_except_table2757
+ GCC_except_table2765
+ GCC_except_table2883
+ GCC_except_table2888
+ GCC_except_table2984
+ GCC_except_table2987
+ GCC_except_table3123
+ GCC_except_table3127
+ GCC_except_table3131
+ GCC_except_table3134
+ GCC_except_table3162
+ GCC_except_table3184
+ GCC_except_table447
+ GCC_except_table448
+ GCC_except_table449
+ GCC_except_table480
+ GCC_except_table482
+ GCC_except_table536
+ GCC_except_table540
+ GCC_except_table542
+ GCC_except_table544
+ GCC_except_table546
+ GCC_except_table549
+ GCC_except_table649
+ GCC_except_table707
+ GCC_except_table754
+ GCC_except_table762
+ GCC_except_table788
+ GCC_except_table818
+ _HAPServiceUUID_AccessoryInformation
+ _OBJC_CLASS_$_HMFOSTransaction
+ _OBJC_CLASS_$_HMMTRAttributeReportDistributor
+ _OBJC_CLASS_$_HMMTRAttributeReportDistributorRegistry
+ _OBJC_CLASS_$_HMMTRControllerData
+ _OBJC_CLASS_$_HMMTRDeviceReader
+ _OBJC_CLASS_$_HMMTRFabricData
+ _OBJC_CLASS_$_HMMTRPairingWindowInfoTable
+ _OBJC_CLASS_$_HMMTRPairingWindowInfoTableEntry
+ _OBJC_CLASS_$_HMMTRVendorMetadataFileStore
+ _OBJC_IVAR_$_HMMTRAccessControl._lock
+ _OBJC_IVAR_$_HMMTRAccessControl._privilegeGetter
+ _OBJC_IVAR_$_HMMTRAccessoryServer._bridgedAccessoryReachabilityReaderTimeoutNSecs
+ _OBJC_IVAR_$_HMMTRAccessoryServer._deviceConnectedStateCaptureInformation
+ _OBJC_IVAR_$_HMMTRAccessoryServer._deviceConnectedStateHandle
+ _OBJC_IVAR_$_HMMTRAccessoryServer._partsListStateCaptureHandle
+ _OBJC_IVAR_$_HMMTRAccessoryServer._partsListStateCaptureInformation
+ _OBJC_IVAR_$_HMMTRAccessoryServer._reportDistributor
+ _OBJC_IVAR_$_HMMTRAccessoryServer._residentReachabilityUpdateWaitTimer
+ _OBJC_IVAR_$_HMMTRAccessoryServer._stateCaptureDeviceConnectedTimer
+ _OBJC_IVAR_$_HMMTRAccessoryServer._stateCapturePartsListTimer
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._pairingWindowInfoTable
+ _OBJC_IVAR_$_HMMTRAttributeReportDistributor._receivers
+ _OBJC_IVAR_$_HMMTRAttributeReportDistributorRegistry._queue
+ _OBJC_IVAR_$_HMMTRAttributeReportDistributorRegistry._receiver
+ _OBJC_IVAR_$_HMMTRClusterDescription._attributeID
+ _OBJC_IVAR_$_HMMTRClusterDescription._clusterID
+ _OBJC_IVAR_$_HMMTRControllerData._fabric
+ _OBJC_IVAR_$_HMMTRControllerData._nodeID
+ _OBJC_IVAR_$_HMMTRControllerData._operationalCertificate
+ _OBJC_IVAR_$_HMMTRDeviceReader._attributeID
+ _OBJC_IVAR_$_HMMTRDeviceReader._clientQueue
+ _OBJC_IVAR_$_HMMTRDeviceReader._clusterID
+ _OBJC_IVAR_$_HMMTRDeviceReader._device
+ _OBJC_IVAR_$_HMMTRDeviceReader._distributor
+ _OBJC_IVAR_$_HMMTRDeviceReader._endpointID
+ _OBJC_IVAR_$_HMMTRDeviceReader._reportTimeoutNSecs
+ _OBJC_IVAR_$_HMMTRFabric._cachedDataValid
+ _OBJC_IVAR_$_HMMTRFabric._currentDeviceNodeData
+ _OBJC_IVAR_$_HMMTRFabric._fabricData
+ _OBJC_IVAR_$_HMMTRFabric._workQueue
+ _OBJC_IVAR_$_HMMTRFabricData._fabric
+ _OBJC_IVAR_$_HMMTRFabricData._ipk
+ _OBJC_IVAR_$_HMMTRFabricData._residentNodeID
+ _OBJC_IVAR_$_HMMTRFabricData._rootCert
+ _OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._idleResetTimer
+ _OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._idleResetTimerQueue
+ _OBJC_IVAR_$_HMMTRPairingWindowInfoTable._lock
+ _OBJC_IVAR_$_HMMTRPairingWindowInfoTable._table
+ _OBJC_IVAR_$_HMMTRPairingWindowInfoTableEntry._accessoryServer
+ _OBJC_IVAR_$_HMMTRPairingWindowInfoTableEntry._expirationDate
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._fileManager
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._fileURL
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._lock
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._uarpController
+ _OBJC_METACLASS_$_HMMTRAttributeReportDistributor
+ _OBJC_METACLASS_$_HMMTRAttributeReportDistributorRegistry
+ _OBJC_METACLASS_$_HMMTRControllerData
+ _OBJC_METACLASS_$_HMMTRDeviceReader
+ _OBJC_METACLASS_$_HMMTRFabricData
+ _OBJC_METACLASS_$_HMMTRPairingWindowInfoTable
+ _OBJC_METACLASS_$_HMMTRPairingWindowInfoTableEntry
+ _OBJC_METACLASS_$_HMMTRVendorMetadataFileStore
+ __OBJC_$_CLASS_METHODS_HMMTRControllerData
+ __OBJC_$_CLASS_METHODS_HMMTRFabricData
+ __OBJC_$_CLASS_METHODS_HMMTRPairingWindowInfoTable
+ __OBJC_$_CLASS_METHODS_HMMTRVendorMetadataFileStore
+ __OBJC_$_INSTANCE_METHODS_HMMTRAttributeReportDistributor
+ __OBJC_$_INSTANCE_METHODS_HMMTRAttributeReportDistributorRegistry
+ __OBJC_$_INSTANCE_METHODS_HMMTRControllerData
+ __OBJC_$_INSTANCE_METHODS_HMMTRDeviceReader
+ __OBJC_$_INSTANCE_METHODS_HMMTRFabricData
+ __OBJC_$_INSTANCE_METHODS_HMMTRPairingWindowInfoTable
+ __OBJC_$_INSTANCE_METHODS_HMMTRPairingWindowInfoTableEntry
+ __OBJC_$_INSTANCE_METHODS_HMMTRVendorMetadataFileStore
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAttributeReportDistributor
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAttributeReportDistributorRegistry
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRControllerData
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRDeviceReader
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricData
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRPairingWindowInfoTable
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRPairingWindowInfoTableEntry
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRVendorMetadataFileStore
+ __OBJC_$_PROP_LIST_HMMTRAttributeReportDistributor
+ __OBJC_$_PROP_LIST_HMMTRAttributeReportDistributorRegistry
+ __OBJC_$_PROP_LIST_HMMTRControllerData
+ __OBJC_$_PROP_LIST_HMMTRDeviceReader
+ __OBJC_$_PROP_LIST_HMMTRFabricData
+ __OBJC_$_PROP_LIST_HMMTRPairingWindowInfoTable
+ __OBJC_$_PROP_LIST_HMMTRPairingWindowInfoTableEntry
+ __OBJC_$_PROP_LIST_HMMTRVendorMetadataFileStore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRVendorMetadataStore
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRVendorMetadataStore
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRFirmwareUpdateStatus
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRVendorMetadataFileStore
+ __OBJC_CLASS_RO_$_HMMTRAttributeReportDistributor
+ __OBJC_CLASS_RO_$_HMMTRAttributeReportDistributorRegistry
+ __OBJC_CLASS_RO_$_HMMTRControllerData
+ __OBJC_CLASS_RO_$_HMMTRDeviceReader
+ __OBJC_CLASS_RO_$_HMMTRFabricData
+ __OBJC_CLASS_RO_$_HMMTRPairingWindowInfoTable
+ __OBJC_CLASS_RO_$_HMMTRPairingWindowInfoTableEntry
+ __OBJC_CLASS_RO_$_HMMTRVendorMetadataFileStore
+ __OBJC_LABEL_PROTOCOL_$_HMMTRVendorMetadataStore
+ __OBJC_METACLASS_RO_$_HMMTRAttributeReportDistributor
+ __OBJC_METACLASS_RO_$_HMMTRAttributeReportDistributorRegistry
+ __OBJC_METACLASS_RO_$_HMMTRControllerData
+ __OBJC_METACLASS_RO_$_HMMTRDeviceReader
+ __OBJC_METACLASS_RO_$_HMMTRFabricData
+ __OBJC_METACLASS_RO_$_HMMTRPairingWindowInfoTable
+ __OBJC_METACLASS_RO_$_HMMTRPairingWindowInfoTableEntry
+ __OBJC_METACLASS_RO_$_HMMTRVendorMetadataFileStore
+ __OBJC_PROTOCOL_$_HMMTRVendorMetadataStore
+ ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.634
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.764
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.767
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.692
+ ___105-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]_block_invoke
+ ___105-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]_block_invoke.170
+ ___105-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]_block_invoke.171
+ ___105-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]_block_invoke_2
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.139
+ ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.138
+ ___109-[HMMTRDescriptorClusterManager fetchHAPServicesForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.134
+ ___109-[HMMTRDescriptorClusterManager fetchHAPServicesForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.135
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.141
+ ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke
+ ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke.7
+ ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke.8
+ ___111-[HMMTRColorControl supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:]_block_invoke.9
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.1
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.4
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.5
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.7
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke_2
+ ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.196
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.231
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.232
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.480
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.481
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.482
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.483
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.486
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.484
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.485
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.137
+ ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.235
+ ___131-[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke
+ ___131-[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.106
+ ___131-[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.107
+ ___131-[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.108
+ ___131-[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke.112
+ ___131-[HMMTRProtocolOperationManager registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:]_block_invoke_2
+ ___133-[HMMTRAccessoryServerBrowser fetchCertificatesForSharedUserWithAccessoryNodeID:sharedUserType:publicKey:fabricID:completionHandler:]_block_invoke.187
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.90
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.97
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.98
+ ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.99
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.180
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.181
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.182
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.183
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.184
+ ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.185
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.156
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.167
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.171
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.178
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.182
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.186
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.190
+ ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.194
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.246
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.248
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.247
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.214
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.215
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.221
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.226
+ ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.123
+ ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.195
+ ___30+[HMMTRFabricData logCategory]_block_invoke
+ ___34+[HMMTRControllerData logCategory]_block_invoke
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.590
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.252
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.289
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.291
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.293
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.575
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.579
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.580
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.581
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.582
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.583
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.584
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.585
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.586
+ ___40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.38
+ ___42+[HMMTRPairingWindowInfoTable logCategory]_block_invoke
+ ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.442
+ ___42-[HMMTRStorage prepareStorageForFabricID:]_block_invoke.33
+ ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.102
+ ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.104
+ ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.96
+ ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.105
+ ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_3.110
+ ___43+[HMMTRVendorMetadataFileStore logCategory]_block_invoke
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.281
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.284
+ ___43-[HMMTRFabric _loadFromDiskWithCompletion:]_block_invoke
+ ___43-[HMMTRFabric _loadFromDiskWithCompletion:]_block_invoke_2
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.739
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.646
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.653
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.270
+ ___45-[HMMTRFabric _loadFromRemoteWithCompletion:]_block_invoke
+ ___45-[HMMTRFabric _loadFromRemoteWithCompletion:]_block_invoke.41
+ ___45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.39
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.821
+ ___47-[HMMTRControllerWrapper replaceStartupParams:]_block_invoke.87
+ ___47-[HMMTRFabric _loadFromResidentWithCompletion:]_block_invoke
+ ___47-[HMMTRFabric _loadFromResidentWithCompletion:]_block_invoke_2
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.257
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.258
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke_2.259
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.716
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.720
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.719
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.775
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.776
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.777
+ ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.169
+ ___49-[HMMTRDeviceReader readAttributeWithCompletion:]_block_invoke
+ ___49-[HMMTRDeviceReader readAttributeWithCompletion:]_block_invoke.5
+ ___49-[HMMTRDeviceReader readAttributeWithCompletion:]_block_invoke.7
+ ___49-[HMMTRDeviceReader readAttributeWithCompletion:]_block_invoke_2
+ ___49-[HMMTRDeviceReader readAttributeWithCompletion:]_block_invoke_2.9
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.672
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.676
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.677
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.822
+ ___51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke
+ ___51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke.40
+ ___51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke_2
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.156
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.157
+ ___52-[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]_block_invoke
+ ___52-[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]_block_invoke_2
+ ___52-[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]_block_invoke_3
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.226
+ ___53-[HMMTRFabric createNewFabricIdentityWithCompletion:]_block_invoke
+ ___54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.112
+ ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.670
+ ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.671
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.591
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.596
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.820
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.407
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.408
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.409
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.410
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.411
+ ___56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.36
+ ___57-[HMMTRFabric loadFabricAndControllerDataWithCompletion:]_block_invoke
+ ___57-[HMMTRFabric loadFabricAndControllerDataWithCompletion:]_block_invoke.5
+ ___57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.90
+ ___58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.113
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.417
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.418
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.419
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.420
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.421
+ ___59-[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]_block_invoke.219
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.768
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.770
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.772
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.773
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.412
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.413
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.414
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.415
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.416
+ ___61-[HMMTRAttributeReportDistributor distributeAttributeReport:]_block_invoke
+ ___61-[HMMTRStorage _fetchCertForFabricWithID:isOwner:completion:]_block_invoke.60
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.116
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.459
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.460
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.461
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.462
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.465
+ ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.113
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.426
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.427
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.428
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.429
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.91
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.422
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.423
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.424
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.425
+ ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.300
+ ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.210
+ ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke
+ ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.142
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.448
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.449
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.450
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.451
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.454
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.458
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.399
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.405
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.406
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.118
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.121
+ ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.111
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.254
+ ___71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke
+ ___71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke.166
+ ___71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke.167
+ ___71-[HMMTRIdentifyDevice _processChildNodesForEndpoint:completionHandler:]_block_invoke
+ ___71-[HMMTRIdentifyDevice _processChildNodesForEndpoint:completionHandler:]_block_invoke.57
+ ___71-[HMMTRIdentifyDevice _processChildNodesForEndpoint:completionHandler:]_block_invoke_2
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.387
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.392
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.393
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.430
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.431
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.432
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.434
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.436
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.437
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.438
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.439
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.440
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.441
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.443
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.444
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.445
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.446
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.447
+ ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.81
+ ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.82
+ ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.83
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.666
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.667
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.669
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.668
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.654
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.655
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.662
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.663
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.665
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.656
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.212
+ ___73-[HMMTRThermostat writeAttributePluginActiveWithValue:completionHandler:]_block_invoke.37
+ ___73-[HMMTRThermostat writeAttributePluginActiveWithValue:completionHandler:]_block_invoke.42
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.725
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.726
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.730
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.213
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.214
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.215
+ ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.75
+ ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.76
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.273
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.274
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.275
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.276
+ ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.50
+ ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.53
+ ___77-[HMMTRAccessoryServer _registerStateCaptureHandler:stateCaptureInformation:]_block_invoke
+ ___78-[HMMTRSyncClusterDoorLock addUserAtUserIndex:withUserUniqueID:userType:flow:]_block_invoke
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.785
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.786
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.394
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.395
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.396
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.398
+ ___79-[HMMTRIdentifyDevice _validIdentifyNodeForParentAtEndpoint:completionHandler:]_block_invoke.42
+ ___79-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:]_block_invoke.115
+ ___80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke
+ ___80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.116
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.161
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.102
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.104
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.743
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.744
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.745
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.746
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.751
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.693
+ ___83-[HMMTRThermostat readAttributePluginTargetHeaterCoolerStateWithCompletionHandler:]_block_invoke.48
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.357
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.358
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.360
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.752
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.753
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.754
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.755
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.758
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.759
+ ___84-[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]_block_invoke.17
+ ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.43
+ ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.44
+ ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.45
+ ___86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.153
+ ___87-[HMMTRDeviceReader _readAttributeAfterAttributeListConfirmationWithCompletionHandler:]_block_invoke
+ ___87-[HMMTRDeviceReader _readAttributeAfterAttributeListConfirmationWithCompletionHandler:]_block_invoke_2
+ ___87-[HMMTRDeviceReader _readAttributeAfterAttributeListConfirmationWithCompletionHandler:]_block_invoke_3
+ ___89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.154
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.261
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.262
+ ___92-[HMMTRAccessoryServer _readCharacteristicValueFromCacheWithCharacteristic:responseHandler:]_block_invoke
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.488
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.489
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.490
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.491
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.493
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.492
+ ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.211
+ ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.291
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.691
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.110
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.237
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.238
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.239
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.241
+ ___96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.155
+ ___97-[HMMTRAccessoryServer _queryBridgedAccessoryAndUnreachablePerCacheForCharacteristic:completion:]_block_invoke
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.229
+ ___99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.156
+ ___Block_byref_object_copy_.2084
+ ___Block_byref_object_copy_.2363
+ ___Block_byref_object_copy_.3272
+ ___Block_byref_object_copy_.4182
+ ___Block_byref_object_copy_.4674
+ ___Block_byref_object_copy_.4949
+ ___Block_byref_object_copy_.5308
+ ___Block_byref_object_copy_.5937
+ ___Block_byref_object_copy_.6411
+ ___Block_byref_object_copy_.6873
+ ___Block_byref_object_copy_.7528
+ ___Block_byref_object_copy_.8050
+ ___Block_byref_object_copy_.8731
+ ___Block_byref_object_copy_.8943
+ ___Block_byref_object_dispose_.2085
+ ___Block_byref_object_dispose_.2364
+ ___Block_byref_object_dispose_.3273
+ ___Block_byref_object_dispose_.4183
+ ___Block_byref_object_dispose_.4675
+ ___Block_byref_object_dispose_.4950
+ ___Block_byref_object_dispose_.5309
+ ___Block_byref_object_dispose_.5938
+ ___Block_byref_object_dispose_.6412
+ ___Block_byref_object_dispose_.6874
+ ___Block_byref_object_dispose_.7529
+ ___Block_byref_object_dispose_.8051
+ ___Block_byref_object_dispose_.8732
+ ___Block_byref_object_dispose_.8944
+ ___block_descriptor_32_e18_16?0"NSNumber"8l
+ ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e42_v16?0"HMMTRCachedFabricCertificateData"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e22_v16?0"NSDictionary"8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e37_v24?0"MTRSetupPayload"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e30_v24?0"NSNumber"8"NSError"16lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e18_v16?0"NSString"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e55_{_HMFFutureBlockOutcome=q}16?0"HomeUserSlotResults"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0lw64l8s32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s_e44_{_HMFFutureBlockOutcome=q}16?0"NSNumber"8ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s_e16_"HMFFuture"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s_e16_"HMFFuture"8?0ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56bs64r72r80r88r_e5_v8?0ls32l8r64l8r72l8r80l8s40l8s48l8r88l8s56l8
+ ___block_literal_global.103
+ ___block_literal_global.108
+ ___block_literal_global.114
+ ___block_literal_global.1143
+ ___block_literal_global.120
+ ___block_literal_global.125
+ ___block_literal_global.1365
+ ___block_literal_global.138
+ ___block_literal_global.140
+ ___block_literal_global.149
+ ___block_literal_global.1532
+ ___block_literal_global.162
+ ___block_literal_global.1701
+ ___block_literal_global.1822
+ ___block_literal_global.184
+ ___block_literal_global.2039
+ ___block_literal_global.2104
+ ___block_literal_global.2257
+ ___block_literal_global.230.7616
+ ___block_literal_global.231
+ ___block_literal_global.240
+ ___block_literal_global.2431
+ ___block_literal_global.2582
+ ___block_literal_global.2692
+ ___block_literal_global.295
+ ___block_literal_global.295.5123
+ ___block_literal_global.3325
+ ___block_literal_global.3582
+ ___block_literal_global.3716
+ ___block_literal_global.391
+ ___block_literal_global.3943
+ ___block_literal_global.4315
+ ___block_literal_global.4462
+ ___block_literal_global.4474
+ ___block_literal_global.464
+ ___block_literal_global.4718
+ ___block_literal_global.4829
+ ___block_literal_global.5124
+ ___block_literal_global.5319
+ ___block_literal_global.5680
+ ___block_literal_global.578
+ ___block_literal_global.582
+ ___block_literal_global.5973
+ ___block_literal_global.6194
+ ___block_literal_global.6374
+ ___block_literal_global.645
+ ___block_literal_global.649
+ ___block_literal_global.652
+ ___block_literal_global.658
+ ___block_literal_global.676
+ ___block_literal_global.6787
+ ___block_literal_global.7185
+ ___block_literal_global.75
+ ___block_literal_global.7758
+ ___block_literal_global.7953
+ ___block_literal_global.80
+ ___block_literal_global.8084
+ ___block_literal_global.8227
+ ___block_literal_global.823
+ ___block_literal_global.8333
+ ___block_literal_global.835
+ ___block_literal_global.8809
+ ___block_literal_global.916
+ ___block_literal_global.991
+ ___strlcpy_chk
+ __unnamed_array_storage.100
+ __unnamed_array_storage.111
+ __unnamed_array_storage.119
+ __unnamed_array_storage.1266
+ __unnamed_array_storage.1679
+ __unnamed_array_storage.2245
+ __unnamed_array_storage.5885
+ __unnamed_array_storage.64
+ __unnamed_array_storage.72
+ __unnamed_array_storage.7560
+ __unnamed_array_storage.77
+ _kDumpStateStateKey
+ _logCategory._hmf_once_t1.5679
+ _logCategory._hmf_once_t114
+ _logCategory._hmf_once_t12
+ _logCategory._hmf_once_t125
+ _logCategory._hmf_once_t135
+ _logCategory._hmf_once_t15.8332
+ _logCategory._hmf_once_t2.3715
+ _logCategory._hmf_once_t2.4461
+ _logCategory._hmf_once_t2.6786
+ _logCategory._hmf_once_t24.2486
+ _logCategory._hmf_once_t3.915
+ _logCategory._hmf_once_t3.990
+ _logCategory._hmf_once_t362
+ _logCategory._hmf_once_t4.4828
+ _logCategory._hmf_once_t40
+ _logCategory._hmf_once_t51
+ _logCategory._hmf_once_t51.3324
+ _logCategory._hmf_once_t583
+ _logCategory._hmf_once_t6.2103
+ _logCategory._hmf_once_t68
+ _logCategory._hmf_once_t8.6373
+ _logCategory._hmf_once_t8.7952
+ _logCategory._hmf_once_t89
+ _logCategory._hmf_once_t9.822
+ _logCategory._hmf_once_v10.824
+ _logCategory._hmf_once_v115
+ _logCategory._hmf_once_v126
+ _logCategory._hmf_once_v13
+ _logCategory._hmf_once_v136
+ _logCategory._hmf_once_v16.8334
+ _logCategory._hmf_once_v2.5681
+ _logCategory._hmf_once_v25.2487
+ _logCategory._hmf_once_v3.3717
+ _logCategory._hmf_once_v3.4463
+ _logCategory._hmf_once_v3.6788
+ _logCategory._hmf_once_v363
+ _logCategory._hmf_once_v4.917
+ _logCategory._hmf_once_v4.992
+ _logCategory._hmf_once_v41
+ _logCategory._hmf_once_v5.4830
+ _logCategory._hmf_once_v52
+ _logCategory._hmf_once_v52.3326
+ _logCategory._hmf_once_v584
+ _logCategory._hmf_once_v69
+ _logCategory._hmf_once_v7.2105
+ _logCategory._hmf_once_v9.6375
+ _logCategory._hmf_once_v9.7954
+ _logCategory._hmf_once_v90
+ _malloc_type_calloc
+ _memcpy
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$__baseClusterValueForAttributeDeviceListFromReadValue:forIdentify:
+ _objc_msgSend$_cachedOperationalCertificateIfValidForFabricID:
+ _objc_msgSend$_clearExpiredEntriesWithCurrentDate:
+ _objc_msgSend$_connectPendingFabricConnectionsForFabricID:
+ _objc_msgSend$_createHAPServicesFromServiceDescriptions:topology:nodeID:accessoryEndpointID:services:startingServiceInstanceID:primaryAccessory:standaloneServiceLabelIndexMap:
+ _objc_msgSend$_createNewFabricData
+ _objc_msgSend$_createTransientOperationalCertificateForFabricID:rootCert:caseAuthenticatedTags:
+ _objc_msgSend$_deregisterDeviceConnectedStateCaptureHandler
+ _objc_msgSend$_deregisterPartsListStateCaptureHandler
+ _objc_msgSend$_deregisterStateCaptureHandlers
+ _objc_msgSend$_fetchStateCaptureInformationForDevice:endpointID:callbackQueue:
+ _objc_msgSend$_fetchStateCaptureInformationForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$_getDataToPersist
+ _objc_msgSend$_loadFromDiskWithCompletion:
+ _objc_msgSend$_loadFromRemoteWithCompletion:
+ _objc_msgSend$_loadFromResidentWithCompletion:
+ _objc_msgSend$_loadFromStorageWithCompletion:
+ _objc_msgSend$_nodeIDFromOperationalX509Certificate:
+ _objc_msgSend$_processChildNodesForEndpoint:completionHandler:
+ _objc_msgSend$_queryBridgedAccessoryAndUnreachablePerCacheForCharacteristic:completion:
+ _objc_msgSend$_readAttributeAfterAttributeListConfirmationWithCompletionHandler:
+ _objc_msgSend$_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:
+ _objc_msgSend$_registerStateCaptureHandler:stateCaptureInformation:
+ _objc_msgSend$_serviceLabelIndexMapForDescriptions:
+ _objc_msgSend$_shouldRetryWEDConnectionToAccessory
+ _objc_msgSend$addOperationWithBlock:queuePriority:
+ _objc_msgSend$addUserAtUserIndex:withUserUniqueID:userType:flow:
+ _objc_msgSend$attributeID
+ _objc_msgSend$bridgedAccessoryReachabilityReaderTimeoutNSecs
+ _objc_msgSend$clusterID
+ _objc_msgSend$createNewFabricIdentityWithCompletion:
+ _objc_msgSend$createStateData:data:
+ _objc_msgSend$currentDeviceNodeData
+ _objc_msgSend$dateWithTimeInterval:sinceDate:
+ _objc_msgSend$deregisterHandlerForAttributePath:registry:
+ _objc_msgSend$deviceConnectedStateCaptureInformation
+ _objc_msgSend$deviceConnectedStateHandle
+ _objc_msgSend$distributeAttributeReport:
+ _objc_msgSend$distributor
+ _objc_msgSend$dumpState:
+ _objc_msgSend$endpointID
+ _objc_msgSend$expirationDate
+ _objc_msgSend$extendedMACAddressForSystemCommissionerFabricNode:
+ _objc_msgSend$fabricData
+ _objc_msgSend$fetchCertificatesFromStorageForFabricID:rootCert:operationalCert:residentNodeID:ipk:
+ _objc_msgSend$fetchClientClustersForDevice:endpointID:callbackQueue:
+ _objc_msgSend$fetchClusterAcceptedCommandsForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchClusterAttributesForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchClusterEventListForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchClusterFabricIndexForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchClusterFeatureMapForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchClusterGeneratedCommandsForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchClusterRevisionForDevice:endpointID:clusterID:callbackQueue:
+ _objc_msgSend$fetchDeviceTypesForDevice:endpointID:callbackQueue:
+ _objc_msgSend$fetchPartsListForDevice:endpointID:callbackQueue:
+ _objc_msgSend$fetchServerClustersForDevice:endpointID:callbackQueue:
+ _objc_msgSend$fetchStateCaptureInformationForDevice:nodeId:server:callbackQueue:completionHandler:
+ _objc_msgSend$findOrAddUserWithUniqueID:userType:flow:
+ _objc_msgSend$generateStateCaptureInformationForReason:completionHandler:
+ _objc_msgSend$hasPreferredLocalLink
+ _objc_msgSend$idleResetTimer
+ _objc_msgSend$initWithAccessoryServer:expirationDate:
+ _objc_msgSend$initWithClientQueue:distributor:device:endpointID:clusterID:attributeID:
+ _objc_msgSend$initWithFabric:
+ _objc_msgSend$initWithQueue:receiver:
+ _objc_msgSend$invalidateCachedData
+ _objc_msgSend$isCachedDataValid
+ _objc_msgSend$isCurrentDeviceAllowedAccessoryControlDespiteReachableResident
+ _objc_msgSend$isPairingActive
+ _objc_msgSend$isValid
+ _objc_msgSend$kick
+ _objc_msgSend$legacyNodeIDForFabricID:
+ _objc_msgSend$loadFabricAndControllerDataWithCompletion:
+ _objc_msgSend$longValue
+ _objc_msgSend$mtrBaseClusterValueFromMTRClusterReadResultValue:clusterIdentifier:attributeIdentifier:forIdentify:
+ _objc_msgSend$now
+ _objc_msgSend$pairingWindowInfoTable
+ _objc_msgSend$partsListStateCaptureHandle
+ _objc_msgSend$partsListStateCaptureInformation
+ _objc_msgSend$privilegeGetter
+ _objc_msgSend$queueAccessoryOperation:highPriority:operationQueuePriority:completion:
+ _objc_msgSend$readAttributeClientListWithParams:
+ _objc_msgSend$readAttributeColorTempPhysicalMaxMiredsWithCompletion:
+ _objc_msgSend$readAttributeColorTempPhysicalMinMiredsWithCompletion:
+ _objc_msgSend$readAttributeDeviceTypeListWithParams:
+ _objc_msgSend$readAttributePartsListWithParams:
+ _objc_msgSend$readAttributeWithCompletion:
+ _objc_msgSend$readAttributeWithEndpointID:clusterID:attributeID:params:
+ _objc_msgSend$receiver
+ _objc_msgSend$receivers
+ _objc_msgSend$registerHandlerForAttributePath:queue:handler:
+ _objc_msgSend$registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:
+ _objc_msgSend$registerPairingWindowWithSetupPayload:currentDate:duration:accessoryServer:
+ _objc_msgSend$registerPairingWindowWithSetupPayload:duration:accessoryServer:
+ _objc_msgSend$reportDistributor
+ _objc_msgSend$reportTimeoutNSecs
+ _objc_msgSend$residentNodeID
+ _objc_msgSend$residentReachabilityUpdateWaitTimer
+ _objc_msgSend$retrieveAccessoryServerForPairingWindowWithSetupPayload:currentDate:
+ _objc_msgSend$setAttributeID:
+ _objc_msgSend$setCachedDataValid:
+ _objc_msgSend$setClusterID:
+ _objc_msgSend$setDeviceConnectedStateCaptureInformation:
+ _objc_msgSend$setDeviceConnectedStateHandle:
+ _objc_msgSend$setExtendedMACAddress:forSystemCommissionerFabricNode:
+ _objc_msgSend$setIpk:
+ _objc_msgSend$setOperationalCertificate:
+ _objc_msgSend$setPartsListStateCaptureHandle:
+ _objc_msgSend$setPartsListStateCaptureInformation:
+ _objc_msgSend$setReportTimeoutNSecs:
+ _objc_msgSend$setResidentNodeID:
+ _objc_msgSend$setResidentReachabilityUpdateWaitTimer:
+ _objc_msgSend$setStateCaptureDeviceConnectedTimer:
+ _objc_msgSend$setStateCapturePartsListTimer:
+ _objc_msgSend$setWEDSupported:forSystemCommissionerFabricNode:
+ _objc_msgSend$stateCaptureDeviceConnectedTimer
+ _objc_msgSend$stateCapturePartsListTimer
+ _objc_msgSend$syncDataSourceDictionary:forFabric:
+ _objc_msgSend$table
+ _objc_msgSend$wedSupportedForSystemCommissionerFabricNode:
+ _os_state_add_handler
+ _os_state_remove_handler
+ _os_unfair_lock_lock
- +[HMMTRVendorMetadataStore logCategory]
- -[HMMTRAccessoryServer _isBridgedAccessoryAndUnreachablePerCacheForCharacteristic:]
- -[HMMTRAccessoryServer expiredEventsConsumed]
- -[HMMTRAccessoryServer initWithKeystore:]
- -[HMMTRAccessoryServer setExpiredEventsConsumed:]
- -[HMMTRAccessoryServerBrowser hasOperationalCerts]
- -[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:]
- -[HMMTRAccessoryServerBrowser setHasOperationalCerts:]
- -[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]
- -[HMMTRColorControl supportsColorTemperature:]
- -[HMMTRFabric initSystemCommissionerFabricWithDelegate:]
- -[HMMTRFabric initWithDelegate:]
- -[HMMTRHAPEnumerator _createHAPServicesFromServiceDescriptions:topology:nodeID:accessoryEndpointID:services:startingServiceInstanceID:primaryAccessory:]
- -[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]
- -[HMMTRStorage _createTransientOperationalCertificateForFabricID:]
- -[HMMTRStorage _fetchCert2ForFabricWithID:isOwner:completion:]
- -[HMMTRStorage _fetchOperationalCertificatesFromResidentForFabricID:completion:]
- -[HMMTRStorage _fetchSharedUserCert2ForFabricWithID:reFetch:completion:]
- -[HMMTRStorage fetchSharedUserCertForFabricWithID:reFetch:completion:]
- -[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:forUserIndex:flow:]
- -[HMMTRSyncClusterDoorLock addUserAtUserIndex:withUserUniqueID:isRemote:flow:]
- -[HMMTRSyncClusterDoorLock device]
- -[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:isRemote:flow:]
- -[HMMTRSyncClusterDoorLock setDevice:]
- -[HMMTRVendorMetadataStore .cxx_destruct]
- -[HMMTRVendorMetadataStore _addProductInfoToMetadata:accessories:]
- -[HMMTRVendorMetadataStore _addVendorInfoToMetadata:accessories:]
- -[HMMTRVendorMetadataStore _saveMetadata:]
- -[HMMTRVendorMetadataStore assetAvailablityUpdateForAccessoryID:assetID:]
- -[HMMTRVendorMetadataStore fetchCloudMetadata]
- -[HMMTRVendorMetadataStore fileManager]
- -[HMMTRVendorMetadataStore fileURL]
- -[HMMTRVendorMetadataStore initWithFileURL:]
- -[HMMTRVendorMetadataStore initWithFileURL:uarpController:fileManager:]
- -[HMMTRVendorMetadataStore metadata]
- -[HMMTRVendorMetadataStore sendMessageToAccessory:uarpMsg:error:]
- -[HMMTRVendorMetadataStore staticMetadataFileURL]
- -[HMMTRVendorMetadataStore staticMetadata]
- -[HMMTRVendorMetadataStore supportedAccessories:forProductGroup:]
- -[HMMTRVendorMetadataStore uarpController]
- GCC_except_table1043
- GCC_except_table1044
- GCC_except_table1062
- GCC_except_table1063
- GCC_except_table1064
- GCC_except_table1065
- GCC_except_table1066
- GCC_except_table1069
- GCC_except_table1071
- GCC_except_table1072
- GCC_except_table1073
- GCC_except_table1074
- GCC_except_table1075
- GCC_except_table1076
- GCC_except_table1077
- GCC_except_table1198
- GCC_except_table1247
- GCC_except_table1269
- GCC_except_table1295
- GCC_except_table1312
- GCC_except_table1357
- GCC_except_table1530
- GCC_except_table1534
- GCC_except_table1591
- GCC_except_table1644
- GCC_except_table1686
- GCC_except_table1706
- GCC_except_table1707
- GCC_except_table1718
- GCC_except_table1719
- GCC_except_table1720
- GCC_except_table1721
- GCC_except_table1722
- GCC_except_table1723
- GCC_except_table1724
- GCC_except_table1730
- GCC_except_table1732
- GCC_except_table1736
- GCC_except_table1754
- GCC_except_table1768
- GCC_except_table1774
- GCC_except_table1785
- GCC_except_table1787
- GCC_except_table1795
- GCC_except_table1811
- GCC_except_table1817
- GCC_except_table1824
- GCC_except_table1911
- GCC_except_table2155
- GCC_except_table2160
- GCC_except_table2163
- GCC_except_table2223
- GCC_except_table2237
- GCC_except_table2239
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2272
- GCC_except_table2273
- GCC_except_table2307
- GCC_except_table2347
- GCC_except_table2379
- GCC_except_table2383
- GCC_except_table2399
- GCC_except_table2400
- GCC_except_table2424
- GCC_except_table243
- GCC_except_table2491
- GCC_except_table2527
- GCC_except_table2535
- GCC_except_table2550
- GCC_except_table2569
- GCC_except_table2584
- GCC_except_table2585
- GCC_except_table2590
- GCC_except_table2598
- GCC_except_table2712
- GCC_except_table2811
- GCC_except_table2814
- GCC_except_table2938
- GCC_except_table2957
- GCC_except_table2961
- GCC_except_table2964
- GCC_except_table2989
- GCC_except_table3011
- GCC_except_table430
- GCC_except_table431
- GCC_except_table432
- GCC_except_table463
- GCC_except_table465
- GCC_except_table515
- GCC_except_table519
- GCC_except_table521
- GCC_except_table523
- GCC_except_table525
- GCC_except_table528
- GCC_except_table582
- GCC_except_table648
- GCC_except_table695
- GCC_except_table703
- GCC_except_table729
- GCC_except_table759
- GCC_except_table927
- _OBJC_CLASS_$_HMMTRVendorMetadataStore
- _OBJC_IVAR_$_HMMTRAccessoryServer._expiredEventsConsumed
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._hasOperationalCerts
- _OBJC_IVAR_$_HMMTRSyncClusterDoorLock._device
- _OBJC_IVAR_$_HMMTRVendorMetadataStore._fileManager
- _OBJC_IVAR_$_HMMTRVendorMetadataStore._fileURL
- _OBJC_IVAR_$_HMMTRVendorMetadataStore._lock
- _OBJC_IVAR_$_HMMTRVendorMetadataStore._uarpController
- _OBJC_METACLASS_$_HMMTRVendorMetadataStore
- __OBJC_$_CLASS_METHODS_HMMTRVendorMetadataStore
- __OBJC_$_INSTANCE_METHODS_HMMTRVendorMetadataStore
- __OBJC_$_INSTANCE_VARIABLES_HMMTRVendorMetadataStore
- __OBJC_CLASS_PROTOCOLS_$_HMMTRVendorMetadataStore
- __OBJC_CLASS_RO_$_HMMTRVendorMetadataStore
- __OBJC_METACLASS_RO_$_HMMTRVendorMetadataStore
- ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.611
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.732
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.735
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.669
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.138
- ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.44
- ___109-[HMMTRDescriptorClusterManager fetchHAPServicesForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.40
- ___109-[HMMTRDescriptorClusterManager fetchHAPServicesForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.41
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.140
- ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke
- ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.101
- ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.102
- ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.103
- ___113-[HMMTRProtocolOperationManager registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke_2
- ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.188
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.228
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.229
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.468
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.469
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.470
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.471
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.474
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.472
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.473
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.136
- ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.143
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.87
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.89
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.94
- ___133-[HMMTRProtocolOperationManager handleHueSaturationWriteWithOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:]_block_invoke.96
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.169
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.171
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.173
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.174
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.175
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.177
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.100
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.62
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.73
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.77
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.84
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.88
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.92
- ___163-[HMMTRDescriptorClusterManager _populateAttributeValuesForClusterClassName:clusterClassFeatureMap:endpoint:device:deviceTopology:callbackQueue:completionHandler:]_block_invoke.96
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.154
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.156
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.155
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.120
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.121
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.127
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.132
- ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.122
- ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.101
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.566
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.278
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.280
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.282
- ___39+[HMMTRVendorMetadataStore logCategory]_block_invoke
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.555
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.556
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.557
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.558
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.559
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.560
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.561
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.562
- ___40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.40
- ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.430
- ___42-[HMMTRStorage prepareStorageForFabricID:]_block_invoke.35
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.100
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.92
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.98
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.101
- ___42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_3.106
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.270
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.273
- ___45-[HMMTRAccessoryServer _disconnectWithError:]_block_invoke
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.716
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.623
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.630
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.259
- ___45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.41
- ___46-[HMMTRColorControl supportsColorTemperature:]_block_invoke
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.771
- ___47-[HMMTRControllerWrapper replaceStartupParams:]_block_invoke.86
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.246
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.247
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke_2.248
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.693
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.697
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.696
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.743
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.744
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.745
- ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.167
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.649
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.653
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.654
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.772
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.154
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.155
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.223
- ___54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.108
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.647
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.648
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.567
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.572
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.770
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.394
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.395
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.396
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.397
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.398
- ___56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.38
- ___57-[HMMTRSyncClusterDoorLock _removeUserWithUniqueID:flow:]_block_invoke.86
- ___58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.109
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.404
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.405
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.406
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.407
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.408
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.736
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.738
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.740
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.741
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.399
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.400
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.401
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.402
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.403
- ___60-[HMMTRStorage fetchCertForFabricWithID:isOwner:completion:]_block_invoke_3
- ___61-[HMMTRStorage _fetchCertForFabricWithID:isOwner:completion:]_block_invoke.61
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.115
- ___62-[HMMTRIdentifyDevice identifyWithEndpoint:completionHandler:]_block_invoke.59
- ___62-[HMMTRIdentifyDevice identifyWithEndpoint:completionHandler:]_block_invoke_2.60
- ___62-[HMMTRStorage _fetchCert2ForFabricWithID:isOwner:completion:]_block_invoke
- ___62-[HMMTRStorage _fetchCert2ForFabricWithID:isOwner:completion:]_block_invoke.63
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.447
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.448
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.449
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.450
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.453
- ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.112
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.413
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.414
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.415
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.417
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.90
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.409
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.410
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.411
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.412
- ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.289
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.202
- ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:isRemote:flow:]_block_invoke
- ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:isRemote:flow:]_block_invoke.138
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.436
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.437
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.438
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.439
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.442
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.446
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.386
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.392
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.393
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.116
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.120
- ___69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.107
- ___70-[HMMTRStorage fetchSharedUserCertForFabricWithID:reFetch:completion:]_block_invoke
- ___70-[HMMTRStorage fetchSharedUserCertForFabricWithID:reFetch:completion:]_block_invoke_2
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.243
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.374
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.379
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.380
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.418
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.419
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.420
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.422
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.424
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.425
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.426
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.427
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.428
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.429
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.431
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.432
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.433
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.434
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.435
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.234
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.235
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.236
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.238
- ___72-[HMMTRStorage _fetchSharedUserCert2ForFabricWithID:reFetch:completion:]_block_invoke
- ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.77
- ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.78
- ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke.79
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.643
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.644
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.646
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.645
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.631
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.632
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.639
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.640
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.642
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.633
- ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.206
- ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.207
- ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke_2
- ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke_3
- ___73-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:forUserIndex:flow:]_block_invoke
- ___73-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:forUserIndex:flow:]_block_invoke.112
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.702
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.703
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.707
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.208
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.209
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.210
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.211
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_3
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_4
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke_5
- ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.68
- ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke.71
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.262
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.263
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.264
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.265
- ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.54
- ___76-[HMMTRIdentifyDevice _childNodesWithIdentifyForEndpoint:completionHandler:]_block_invoke.55
- ___78-[HMMTRSyncClusterDoorLock addUserAtUserIndex:withUserUniqueID:isRemote:flow:]_block_invoke
- ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.750
- ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.751
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.381
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.382
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.383
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.385
- ___79-[HMMTRIdentifyDevice _validIdentifyNodeForParentAtEndpoint:completionHandler:]_block_invoke.44
- ___79-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:flow:]_block_invoke.111
- ___80-[HMMTRStorage _fetchOperationalCertificatesFromResidentForFabricID:completion:]_block_invoke
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.159
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.160
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.101
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.103
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.670
- ___83-[HMMTRThermostat readAttributePluginTargetHeaterCoolerStateWithCompletionHandler:]_block_invoke.42
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.344
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.345
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.347
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.720
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.721
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.722
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.723
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.726
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.727
- ___84-[HMMTRColorControl readAttributePluginColorTemperatureMiredsWithCompletionHandler:]_block_invoke.14
- ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.37
- ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.38
- ___84-[HMMTRThermostat readAttributePluginCurrentHeaterCoolerStateWithCompletionHandler:]_block_invoke.39
- ___86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.149
- ___89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.150
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.250
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.251
- ___91-[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]_block_invoke
- ___91-[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]_block_invoke.1
- ___91-[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]_block_invoke.4
- ___91-[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]_block_invoke.5
- ___91-[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]_block_invoke.7
- ___91-[HMMTRAttestationStatus deviceAttestation:completedForDevice:attestationDeviceInfo:error:]_block_invoke_2
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.476
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.477
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.478
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.479
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.481
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.480
- ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.203
- ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.204
- ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.157
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.668
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.109
- ___96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.151
- ___98-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:]_block_invoke
- ___98-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:]_block_invoke.168
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.226
- ___99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.152
- ___Block_byref_object_copy_.1807
- ___Block_byref_object_copy_.2080
- ___Block_byref_object_copy_.2902
- ___Block_byref_object_copy_.4144
- ___Block_byref_object_copy_.4412
- ___Block_byref_object_copy_.4720
- ___Block_byref_object_copy_.5322
- ___Block_byref_object_copy_.5788
- ___Block_byref_object_copy_.6243
- ___Block_byref_object_copy_.6859
- ___Block_byref_object_copy_.7364
- ___Block_byref_object_copy_.8058
- ___Block_byref_object_copy_.8269
- ___Block_byref_object_dispose_.1808
- ___Block_byref_object_dispose_.2081
- ___Block_byref_object_dispose_.2903
- ___Block_byref_object_dispose_.4145
- ___Block_byref_object_dispose_.4413
- ___Block_byref_object_dispose_.4721
- ___Block_byref_object_dispose_.5323
- ___Block_byref_object_dispose_.5789
- ___Block_byref_object_dispose_.6244
- ___Block_byref_object_dispose_.6860
- ___Block_byref_object_dispose_.7365
- ___Block_byref_object_dispose_.8059
- ___Block_byref_object_dispose_.8270
- ___block_descriptor_40_e8_32s_e18_v16?0"NSNumber"8ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e37_v24?0"MTRSetupPayload"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e55_{_HMFFutureBlockOutcome=q}16?0"HomeUserSlotResults"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e42_v16?0"HMMTRCachedFabricCertificateData"8ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e16_"HMFFuture"8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e17_v16?0"NSError"8ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s_e16_"HMFFuture"8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.1092
- ___block_literal_global.117
- ___block_literal_global.134
- ___block_literal_global.136
- ___block_literal_global.136.4437
- ___block_literal_global.1371
- ___block_literal_global.147
- ___block_literal_global.1537
- ___block_literal_global.158
- ___block_literal_global.161
- ___block_literal_global.1655
- ___block_literal_global.1762
- ___block_literal_global.1827
- ___block_literal_global.183
- ___block_literal_global.1974
- ___block_literal_global.198
- ___block_literal_global.2140
- ___block_literal_global.226
- ___block_literal_global.2277
- ___block_literal_global.2384
- ___block_literal_global.256
- ___block_literal_global.2954
- ___block_literal_global.3285
- ___block_literal_global.346
- ___block_literal_global.3513
- ___block_literal_global.3813
- ___block_literal_global.3896
- ___block_literal_global.3957
- ___block_literal_global.4186
- ___block_literal_global.4297
- ___block_literal_global.452
- ___block_literal_global.4538
- ___block_literal_global.4731
- ___block_literal_global.5084
- ___block_literal_global.531
- ___block_literal_global.5357
- ___block_literal_global.5578
- ___block_literal_global.5752
- ___block_literal_global.6153
- ___block_literal_global.622
- ___block_literal_global.626
- ___block_literal_global.626.6265
- ___block_literal_global.629
- ___block_literal_global.635
- ___block_literal_global.6536
- ___block_literal_global.68
- ___block_literal_global.7078
- ___block_literal_global.7270
- ___block_literal_global.73
- ___block_literal_global.7400
- ___block_literal_global.7540
- ___block_literal_global.7643
- ___block_literal_global.771
- ___block_literal_global.785
- ___block_literal_global.8136
- ___block_literal_global.860
- ___block_literal_global.934
- ___block_literal_global.96
- __unnamed_array_storage.104
- __unnamed_array_storage.112
- __unnamed_array_storage.1181
- __unnamed_array_storage.1516
- __unnamed_array_storage.1963
- __unnamed_array_storage.5275
- __unnamed_array_storage.61
- __unnamed_array_storage.66
- __unnamed_array_storage.6894
- __unnamed_array_storage.70
- __unnamed_array_storage.93
- _logCategory._hmf_once_t0.3895
- _logCategory._hmf_once_t123
- _logCategory._hmf_once_t134
- _logCategory._hmf_once_t15.7642
- _logCategory._hmf_once_t17
- _logCategory._hmf_once_t2.6152
- _logCategory._hmf_once_t3.859
- _logCategory._hmf_once_t3.933
- _logCategory._hmf_once_t350
- _logCategory._hmf_once_t4.4296
- _logCategory._hmf_once_t49
- _logCategory._hmf_once_t50
- _logCategory._hmf_once_t563
- _logCategory._hmf_once_t6.1826
- _logCategory._hmf_once_t64
- _logCategory._hmf_once_t8.2139
- _logCategory._hmf_once_t8.5751
- _logCategory._hmf_once_t8.7269
- _logCategory._hmf_once_t84
- _logCategory._hmf_once_t9.4185
- _logCategory._hmf_once_t90
- _logCategory._hmf_once_v1.3897
- _logCategory._hmf_once_v10.4187
- _logCategory._hmf_once_v124
- _logCategory._hmf_once_v135
- _logCategory._hmf_once_v16.7644
- _logCategory._hmf_once_v18
- _logCategory._hmf_once_v3.6154
- _logCategory._hmf_once_v351
- _logCategory._hmf_once_v4.861
- _logCategory._hmf_once_v4.935
- _logCategory._hmf_once_v5.4298
- _logCategory._hmf_once_v50
- _logCategory._hmf_once_v51
- _logCategory._hmf_once_v564
- _logCategory._hmf_once_v65
- _logCategory._hmf_once_v7.1828
- _logCategory._hmf_once_v85
- _logCategory._hmf_once_v9.2141
- _logCategory._hmf_once_v9.5753
- _logCategory._hmf_once_v9.7271
- _logCategory._hmf_once_v91
- _objc_msgSend$_createHAPServicesFromServiceDescriptions:topology:nodeID:accessoryEndpointID:services:startingServiceInstanceID:primaryAccessory:
- _objc_msgSend$_createTransientOperationalCertificateForFabricID:
- _objc_msgSend$_fetchCert2ForFabricWithID:isOwner:completion:
- _objc_msgSend$_fetchOperationalCertificatesFromResidentForFabricID:completion:
- _objc_msgSend$_fetchSharedUserCert2ForFabricWithID:reFetch:completion:
- _objc_msgSend$_isBridgedAccessoryAndUnreachablePerCacheForCharacteristic:
- _objc_msgSend$_removeSharedAdminControllerNodeIDFromACLWithCompletion:
- _objc_msgSend$addUserAtUserIndex:withUserUniqueID:isRemote:flow:
- _objc_msgSend$caseAuthenticatedTag
- _objc_msgSend$expiredEventsConsumed
- _objc_msgSend$fetchSharedUserCertForFabricWithID:reFetch:completion:
- _objc_msgSend$findOrAddUserWithUniqueID:isRemote:flow:
- _objc_msgSend$hasOperationalCerts
- _objc_msgSend$readAttributeReachableWithParams:
- _objc_msgSend$registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:
- _objc_msgSend$setCaseAuthenticatedTag:
- _objc_msgSend$setExpiredEventsConsumed:
- _objc_msgSend$setHasOperationalCerts:
CStrings:
+ "\x02(\x14\x11\x18\x1f"
+ "\x11\x1b"
+ "\x12#"
+ "\x14"
+ " %@ (revision %@), "
+ " WED"
+ " }; }; "
+ "$"
+ "%{public}@Accessory server operations disabled. Aborting generating state capture information."
+ "%{public}@An error occurred while trying to read the control sequence of operation"
+ "%{public}@An error occurred while trying to read the control sequence of operation: %@"
+ "%{public}@Attempting to persist %@"
+ "%{public}@Bad clusterId: %@ defined in protocol map for characteristic %@"
+ "%{public}@Cached data is not valid"
+ "%{public}@Cannot process request without fabric data created for fabric %@, fabricID %@"
+ "%{public}@Cannot process request without fabric data for fabric %@"
+ "%{public}@Cannot read from disk when fabric ID is not valid"
+ "%{public}@Cannot read from storage when fabric ID is not valid"
+ "%{public}@Certificate data is valid"
+ "%{public}@Characteristics Operation Queue: generate state capture information job(%lu) complete."
+ "%{public}@Characteristics Operation Queue: generate state capture information job(%lu) queued."
+ "%{public}@Characteristics Operation Queue: generate state capture information job(%lu) started."
+ "%{public}@Checking currentFirmwareVersionNumber: %@ with downloadedFirmwareVersionNumber: %@ to determine if a software update was installed."
+ "%{public}@Computed service label index map for non-bridged accessory %@ : %@"
+ "%{public}@Connecting pending fabric fabric: %@"
+ "%{public}@Couldn't convert NOC to Matter format"
+ "%{public}@Dictionary element is not a structure type %@"
+ "%{public}@Dropping write request for active characteristic. accessoryUUID: %@"
+ "%{public}@Dumping stack storage for params"
+ "%{public}@Element data data array missing from array type %@"
+ "%{public}@Evicting fabricID: %@"
+ "%{public}@Expired setup payloads: %@"
+ "%{public}@Failed to create fabric data as existing data is already valid"
+ "%{public}@Failed to create fabric data by non-owner user"
+ "%{public}@Failed to create fabric data due to incorrect fabric ID %@"
+ "%{public}@Failed to finish commissioning for System Commissioner with error: %@"
+ "%{public}@Failed to generate IPK"
+ "%{public}@Failed to generate operational certificate with error %@"
+ "%{public}@Failed to generate root certificate with error %@"
+ "%{public}@Failed to load NOC for shared user with error %@"
+ "%{public}@Failed to load certs from resident without operational key"
+ "%{public}@Failed to persist new fabric data"
+ "%{public}@Failed to read color control attribute colorCapabilities with error: %@"
+ "%{public}@Failed to read color control attribute physicalMaxMireds with error: %@"
+ "%{public}@Failed to read color control attribute physicalMinMireds with error: %@"
+ "%{public}@HMMTRAccessoryServer handleEventReportForNotification: Ignoring event report, this is an outdated report. event report=%@"
+ "%{public}@Identify on aggregator failed."
+ "%{public}@Identify on aggregator successful"
+ "%{public}@Idle reset timed out for accessory server [%@]"
+ "%{public}@Invalid handling type %lu. Dropping write request for active characteristic. accessoryUUID: %@"
+ "%{public}@Kicked off timer to stay active while resident updates reachability state"
+ "%{public}@Kicking idle reset timer with delay of %f seconds for accessory server [%@]"
+ "%{public}@Loading certificate data"
+ "%{public}@Loading certificate data from disk"
+ "%{public}@Loading certificate data from remote source"
+ "%{public}@Loading certificate data from resident"
+ "%{public}@Loading certificate data from storage"
+ "%{public}@Loading from resident completed with error %@"
+ "%{public}@Loading from storage completed with error %@"
+ "%{public}@Making room for fabricID: %@"
+ "%{public}@New fabric %@"
+ "%{public}@Newly generated fabric data is invalid"
+ "%{public}@No Matter device controller available to generate state capture information"
+ "%{public}@Not processing connect request to a different WED accessory emac %@ when pairing is active for emac %@"
+ "%{public}@Not setting up MTRDevice for a disabled accessory server"
+ "%{public}@Not starting thread because fabric %@ is empty"
+ "%{public}@Operational certificate fabric ID %@ doesn't match fabric ID of current fabric"
+ "%{public}@Pairing with%s %s accessory %@ via locally opened pairing window"
+ "%{public}@Re-starting operations for fabric: %@"
+ "%{public}@Read cached operational cert data from disk self.rootCert %@, self.operationalCert %@ self.residentNodeID %@ self.ownerIPK %@"
+ "%{public}@Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@] error: %@"
+ "%{public}@Reading disk data for current fabric"
+ "%{public}@Registering pairing window with setup payload: %@, duration: %g, server: %@"
+ "%{public}@Request to generate state capture information"
+ "%{public}@Resident NOC %@ resident node ID %@"
+ "%{public}@Retrieves server with pairing window with setup payload: %@, server: %@"
+ "%{public}@Returning Root Certificate %@, Operational Certificate %@, Resident NodeID %@, and IPK %@ to Shared user Controller"
+ "%{public}@Root certificate fabric ID %@ doesn't match fabric ID of current fabric"
+ "%{public}@Set current user privilege from %@ to %@"
+ "%{public}@Set current user privilege to %@ by getter"
+ "%{public}@Setting active mode On not supported for control sequence of operation value: %@"
+ "%{public}@Starting idle reset timer with delay of %f seconds for accessory server [%@]"
+ "%{public}@State Capture: Information for endpoint %@: %@"
+ "%{public}@State Capture: Information for endpoint 0: %@"
+ "%{public}@State Capture: Information generated for %@, triggered by reason %@ : %@"
+ "%{public}@State Capture: No Endpoints In Use at endpoint 0"
+ "%{public}@State Capture: Setting timer to capture state information due to parts list change for accessory %@, timeout is %@"
+ "%{public}@State Capture: Setting timer to capture state information for %@ due to matter device reachable notification, timeout is %@"
+ "%{public}@State Capture: Timer expired, generate State Capture Information for Device Connected"
+ "%{public}@State Capture: Timer expired, generate State Capture Information for Parts List change"
+ "%{public}@State Capture: completed for server:%@ with Error: %@."
+ "%{public}@Stop idle reset timer for accessory server [%@]"
+ "%{public}@Structure Value does not contain a dictionary %@"
+ "%{public}@Successfully created fabric data for %@"
+ "%{public}@Successfully fetched operational certificates from owner. Root Certificate %@, Operational certificate %@, Owner NodeID %@, fabricID %@"
+ "%{public}@Successfully persisted new fabric with %@ and created new controller with %@"
+ "%{public}@Unable to locate Accessory Information Service on accessory %@, defaulting to service endpoint %@ for characteristic: %@"
+ "%{public}@Unexpected user privilege for user"
+ "%{public}@Unsupported control sequence of operation value: %@"
+ "%{public}@Updating OTA Provider state from %@ to %@ for accessory server [%@]"
+ "%{public}@Updating accessory ACL to include administrative access to %@ and view access to %@"
+ "%{public}@Updating fabric ID to %@ for Shared Home"
+ "%{public}@Using Cached Operational certificate"
+ "%{public}@Using fabric ID as %@ to cache certificates"
+ "%{public}@Waited long enough for resident to update reachability"
+ "%{public}@Wrote to system mode attribute for Active Characteristic, value:%@ (On), system mode:%@"
+ "%{public}@Wrote to system mode attribute for Active Characteristic, value:%@ (On), system mode:%@, error:%@"
+ "%{public}@[Flow: %@] Successfully added pin credential"
+ "%{public}@[Flow: %@] addDeviceCredentialKeyData: %@, credentialType: %ld, tapToUnlockType: %ld, forUserIndex: %ld"
+ "%{public}@[Flow: %@] addIssuerKeyData: %@, isUnifiedAccess: %ld, credentialType: %ld, forUserIndex: %ld"
+ "%{public}@[Flow: %@] addUserAtUserIndex: %ld, withUserUniqueID: %ld, userType: %@"
+ "%{public}@[Flow: %@] findOrAddUserWithUniqueID: %@, userType: %@ if creating new user"
+ "%{public}@_connectPendingFabricConnectionsForFabricID for fabricID - %@"
+ "%{public}@disabled %@, timer running %@ -> local link preferred: %@"
+ "%{public}@fabric %@ not found in either lists"
+ "%{public}@fabric storage is not set %@"
+ "%{public}@fetchClientClustersForDevice: Examining MTRBaseClusterDescriptor clientlist attribute at endpoint %@ to retrieve client clusters."
+ "%{public}@fetchClientClustersForDevice: Retrieved the following client clusters %@"
+ "%{public}@fetchClusterAcceptedCommandsForDevice: Examining MTRBaseClusterDescriptor cluster acceptedCommandList attribute at endpoint %@ to retrieve accepted commands."
+ "%{public}@fetchClusterAcceptedCommandsForDevice: For endpoint %@, cluster %@, retrieved the following accepted command list %@"
+ "%{public}@fetchClusterAttributesForDevice: Examining MTRBaseClusterDescriptor attributelist attribute at endpoint %@ to retrieve cluster attributes."
+ "%{public}@fetchClusterAttributesForDevice: For endpoint %@, cluster %@, retrieved the following attributes %@"
+ "%{public}@fetchClusterEventListForDevice: Examining MTRBaseClusterDescriptor eventlist attribute at endpoint %@ to retrieve events."
+ "%{public}@fetchClusterEventListForDevice: For endpoint %@, cluster %@, retrieved the following events %@"
+ "%{public}@fetchClusterFabricIndexForDevice: Examining MTRBaseClusterDescriptor cluster fabricIndex attribute at endpoint %@ to retrieve fabric index."
+ "%{public}@fetchClusterFabricIndexForDevice: For endpoint %@, cluster %@, retrieved the fabric index info %@"
+ "%{public}@fetchClusterFeatureMapForDevice: Examining MTRBaseClusterDescriptor cluster feature map attribute at endpoint %@ to retrieve feature map."
+ "%{public}@fetchClusterFeatureMapForDevice: For endpoint %@, cluster %@, retrieved the following feature map %@"
+ "%{public}@fetchClusterGeneratedCommandsForDevice: Examining MTRBaseClusterDescriptor cluster geeratedCommandList attribute at endpoint %@ to retrieve accepted commands."
+ "%{public}@fetchClusterGeneratedCommandsForDevice: For endpoint %@, cluster %@, retrieved the following generated command list %@"
+ "%{public}@fetchClusterRevisionForDevice: Examining MTRBaseClusterDescriptor cluster revision attribute at endpoint %@ to cluster revision number."
+ "%{public}@fetchClusterRevisionForDevice: For endpoint %@, cluster %@, retrieved the revison number %@"
+ "%{public}@fetchEndpointsForDevice: At endpoint %@, retrieved the following device types in use %@"
+ "%{public}@fetchEndpointsForDevice: Examining MTRClusterDescriptor cluster parts list at endpoint %@ to retrieve device types."
+ "%{public}@fetchPartsListForDevice: Examining MTRClusterDescriptor cluster parts list at endpoint %@ to retrieve endpoints in use."
+ "%{public}@fetchPartsListForDevice: Failed to read parts list."
+ "%{public}@fetchPartsListForDevice: Retrieved the following parts list in use %@"
+ "%{public}@fetchServerClustersForDevice: Examining MTRBaseClusterDescriptor serverlist attribute at endpoint %@ to retrieve server clusters."
+ "%{public}@fetchServerClustersForDevice: Retrieved the following server clusters %@"
+ "%{public}@tempRootCert %@ && tempOperationalCert %@ && tempResidentNodeID %@ && tempOwnerIPK %@"
+ "( ClusterID:%@ ClusterInfo: %@ ), "
+ "( NodeID: %@; FabricID: %@, "
+ "(AcceptedCommands: %@), "
+ "(AcceptedCommands: ()), "
+ "(Attributes: %@)"
+ "(Attributes: ()), "
+ "(ClientClusters: "
+ "(ClientClusters: ()),"
+ "(ClusterID : %@, ClusterInfo : %@), "
+ "(ClusterRevision: %@), "
+ "(DeviceTypes : ()), "
+ "(DeviceTypes: "
+ "(Events: %@), "
+ "(Events: ()), "
+ "(FabricIds: %@) "
+ "(FabricIds: ()), "
+ "(FeatureMap: %@), "
+ "(GeneratedCommands: %@) "
+ "(GeneratedCommands: ()), "
+ "(PartsList: %@), "
+ "(PartsList: ()), "
+ "(ServerClusters : "
+ "(ServerClusters : () ),"
+ ")"
+ "), "
+ ", "
+ "00000029-0000-1000-8000-0026BB765291"
+ "1&\x12)+#\x1f\f\x17"
+ "@\"<HMMTRVendorMetadataStore>\""
+ "@\"HMMTRAttributeReportDistributor\""
+ "@\"HMMTRControllerData\""
+ "@\"HMMTRFabricData\""
+ "@\"HMMTRPairingWindowInfoTable\""
+ "@\"HMMTRVendorMetadata\"16@0:8"
+ "@\"NSURL\"16@0:8"
+ "@16@?0@\"NSNumber\"8"
+ "@32@0:8@16@?24"
+ "@40@0:8@16@24@?32"
+ "@48@0:8@16q24q32@40"
+ "AcceptedCommands"
+ "AttributeList"
+ "Controller Data"
+ "Controller Node ID"
+ "DeviceConnected"
+ "DeviceList"
+ "EventList"
+ "Fabric Data"
+ "FeatureMap"
+ "GeneratedCommands"
+ "HMD.MTRPlugin.MTS.ExtendedMACAddress."
+ "HMD.MTRPlugin.MTS.WEDSupported."
+ "HMMTRAccessoryServer State for %@/%@(%@)"
+ "HMMTRAttributeReportDistributor"
+ "HMMTRAttributeReportDistributorRegistry"
+ "HMMTRControllerData"
+ "HMMTRDeviceReader"
+ "HMMTRFabricData"
+ "HMMTRPairingWindowInfoTable"
+ "HMMTRPairingWindowInfoTableEntry"
+ "HMMTRVendorMetadataFileStore"
+ "Is Cached Data Valid"
+ "Name: %@, NodeID: %@, FabricID: %@, Category %@, ObjectID: %@, No state capture information available."
+ "Name: %@, NodeID: %@, FabricID: %@, Category: %@, ObjectID: %@, State capture information: %@"
+ "PartsListChange"
+ "Reason: %@, Time: %@, Data: %@"
+ "Resident Node ID"
+ "Revision"
+ "Storage"
+ "T@\"<HMMTRVendorMetadataStore>\",R,N,V_vendorMetadataStore"
+ "T@\"HMFTimer\",&,N,V_idleResetTimer"
+ "T@\"HMFTimer\",&,N,V_residentReachabilityUpdateWaitTimer"
+ "T@\"HMFTimer\",&,N,V_stateCaptureDeviceConnectedTimer"
+ "T@\"HMFTimer\",&,N,V_stateCapturePartsListTimer"
+ "T@\"HMMTRAttributeReportDistributor\",R,N,V_reportDistributor"
+ "T@\"HMMTRAttributeReportDistributor\",R,V_distributor"
+ "T@\"HMMTRControllerData\",R,N,V_currentDeviceNodeData"
+ "T@\"HMMTRFabric\",W,N,V_fabric"
+ "T@\"HMMTRFabricData\",R,N,V_fabricData"
+ "T@\"HMMTRPairingWindowInfoTable\",R,V_pairingWindowInfoTable"
+ "T@\"MTRDevice\",R,V_device"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSData\",&,N,V_ipk"
+ "T@\"NSData\",R,C,V_operationalCertificate"
+ "T@\"NSDate\",R,N,V_expirationDate"
+ "T@\"NSMutableDictionary\",R,N,V_receivers"
+ "T@\"NSMutableDictionary\",R,N,V_table"
+ "T@\"NSNumber\",&,N,V_attributeID"
+ "T@\"NSNumber\",&,N,V_bridgedAccessoryReachabilityReaderTimeoutNSecs"
+ "T@\"NSNumber\",&,N,V_clusterID"
+ "T@\"NSNumber\",&,N,V_residentNodeID"
+ "T@\"NSNumber\",R,V_attributeID"
+ "T@\"NSNumber\",R,V_clusterID"
+ "T@\"NSNumber\",R,V_endpointID"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_idleResetTimerQueue"
+ "T@\"NSString\",&,N,V_deviceConnectedStateCaptureInformation"
+ "T@\"NSString\",&,N,V_partsListStateCaptureInformation"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSURL\",R,C"
+ "T@?,C,V_privilegeGetter"
+ "T@?,R,N,V_receiver"
+ "TB,N,V_cachedDataValid"
+ "TQ,D,N"
+ "TQ,N,V_deviceConnectedStateHandle"
+ "TQ,N,V_partsListStateCaptureHandle"
+ "Tq,N,V_reportTimeoutNSecs"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}32@0:8@16@24"
+ "__baseClusterValueForAttributeDeviceListFromReadValue:forIdentify:"
+ "_attributeID"
+ "_bridgedAccessoryReachabilityReaderTimeoutNSecs"
+ "_cachedDataValid"
+ "_cachedOperationalCertificateIfValidForFabricID:"
+ "_clearExpiredEntriesWithCurrentDate:"
+ "_clusterID"
+ "_connectPendingFabricConnectionsForFabricID:"
+ "_createHAPServicesFromServiceDescriptions:topology:nodeID:accessoryEndpointID:services:startingServiceInstanceID:primaryAccessory:standaloneServiceLabelIndexMap:"
+ "_createNewFabricData"
+ "_createTransientOperationalCertificateForFabricID:rootCert:caseAuthenticatedTags:"
+ "_currentDeviceNodeData"
+ "_deregisterDeviceConnectedStateCaptureHandler"
+ "_deregisterPartsListStateCaptureHandler"
+ "_deregisterStateCaptureHandlers"
+ "_deviceConnectedStateCaptureInformation"
+ "_deviceConnectedStateHandle"
+ "_distributor"
+ "_endpointID"
+ "_expirationDate"
+ "_fabricData"
+ "_fetchStateCaptureInformationForDevice:endpointID:callbackQueue:"
+ "_fetchStateCaptureInformationForDevice:endpointID:clusterID:callbackQueue:"
+ "_getDataToPersist"
+ "_idleResetTimer"
+ "_idleResetTimerQueue"
+ "_loadFromDiskWithCompletion:"
+ "_loadFromRemoteWithCompletion:"
+ "_loadFromResidentWithCompletion:"
+ "_loadFromStorageWithCompletion:"
+ "_nodeIDFromOperationalX509Certificate:"
+ "_operationalCertificate"
+ "_pairingWindowInfoTable"
+ "_partsListStateCaptureHandle"
+ "_partsListStateCaptureInformation"
+ "_privilegeGetter"
+ "_processChildNodesForEndpoint:completionHandler:"
+ "_queryBridgedAccessoryAndUnreachablePerCacheForCharacteristic:completion:"
+ "_readAttributeAfterAttributeListConfirmationWithCompletionHandler:"
+ "_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:"
+ "_receiver"
+ "_receivers"
+ "_registerStateCaptureHandler:stateCaptureInformation:"
+ "_reportDistributor"
+ "_reportTimeoutNSecs"
+ "_residentNodeID"
+ "_residentReachabilityUpdateWaitTimer"
+ "_serviceLabelIndexMapForDescriptions:"
+ "_shouldRetryWEDConnectionToAccessory"
+ "_stateCaptureDeviceConnectedTimer"
+ "_stateCapturePartsListTimer"
+ "_table"
+ "addDeviceCredentialKeyData:ofType:forUserIndex:flow:"
+ "addUserAtUserIndex:withUserUniqueID:userType:flow:"
+ "assetAvailablityUpdateForAccessory:assetID:"
+ "attributeID"
+ "bridgedAccessoryReachabilityReaderTimeoutNSecs"
+ "cachedDataValid"
+ "clusterID"
+ "createNewFabricDataForFabric:completion:"
+ "createNewFabricIdentityWithCompletion:"
+ "createStateData:data:"
+ "currentDeviceNodeData"
+ "dateWithTimeInterval:sinceDate:"
+ "deregisterHandlerForAttributePath:registry:"
+ "deviceConnectedStateCaptureInformation"
+ "deviceConnectedStateHandle"
+ "distributeAttributeReport:"
+ "distributor"
+ "dumpState:"
+ "endpointID"
+ "expirationDate"
+ "extendedMACAddressForSystemCommissionerFabricNode:"
+ "fabricData"
+ "fetchCertificatesFromStorageForFabricID:rootCert:operationalCert:residentNodeID:ipk:"
+ "fetchClientClustersForDevice:endpointID:callbackQueue:"
+ "fetchClusterAcceptedCommandsForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchClusterAttributesForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchClusterEventListForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchClusterFabricIndexForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchClusterFeatureMapForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchClusterGeneratedCommandsForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchClusterRevisionForDevice:endpointID:clusterID:callbackQueue:"
+ "fetchDeviceTypesForDevice:endpointID:callbackQueue:"
+ "fetchPartsListForDevice:endpointID:callbackQueue:"
+ "fetchServerClustersForDevice:endpointID:callbackQueue:"
+ "fetchStateCaptureInformationForDevice:nodeId:server:callbackQueue:completionHandler:"
+ "findOrAddUserWithUniqueID:userType:flow:"
+ "generateStateCaptureInformationForReason:completionHandler:"
+ "hasPreferredLocalLink"
+ "hmmtr.controllerData"
+ "hmmtr.fabricData"
+ "hmmtr.pairinginfotable"
+ "idleResetTimer"
+ "idleResetTimerQueue"
+ "initWithAccessoryServer:expirationDate:"
+ "initWithClientQueue:distributor:device:endpointID:clusterID:attributeID:"
+ "initWithFabric:"
+ "initWithQueue:receiver:"
+ "invalidateCachedData"
+ "isCachedDataValid"
+ "isCurrentDeviceAllowedAccessoryControlDespiteReachableResident"
+ "isValid"
+ "kick"
+ "legacyNodeIDForFabricID:"
+ "loadFabricAndControllerDataWithCompletion:"
+ "longValue"
+ "mtrBaseClusterValueFromMTRClusterReadResultValue:clusterIdentifier:attributeIdentifier:forIdentify:"
+ "non-Thread"
+ "now"
+ "os-state-HMMTRAccessoryServer"
+ "overrideCurrentFabricID:"
+ "pairingWindowInfoTable"
+ "partsListStateCaptureHandle"
+ "partsListStateCaptureInformation"
+ "prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:"
+ "privilegeGetter"
+ "queueAccessoryOperation:highPriority:operationQueuePriority:completion:"
+ "readAttributeClientListWithParams:"
+ "readAttributeColorTempPhysicalMaxMiredsWithCompletion:"
+ "readAttributeColorTempPhysicalMinMiredsWithCompletion:"
+ "readAttributeDeviceTypeListWithParams:"
+ "readAttributePartsListWithParams:"
+ "readAttributeWithCompletion:"
+ "readAttributeWithEndpointID:clusterID:attributeID:params:"
+ "receiver"
+ "receivers"
+ "registerHandlerForAttributePath:queue:handler:"
+ "registerOperation:clientQueue:reportDistributor:operationResponseHandler:updatedAttributesHandler:"
+ "registerPairingWindowWithSetupPayload:currentDate:duration:accessoryServer:"
+ "registerPairingWindowWithSetupPayload:duration:accessoryServer:"
+ "reportDistributor"
+ "reportTimeoutNSecs"
+ "residentNodeID"
+ "residentReachabilityUpdateWaitTimer"
+ "retrieveAccessoryServerForPairingWindowWithSetupPayload:currentDate:"
+ "setAttributeID:"
+ "setBridgedAccessoryReachabilityReaderTimeoutNSecs:"
+ "setCachedDataValid:"
+ "setClusterID:"
+ "setDeviceConnectedStateCaptureInformation:"
+ "setDeviceConnectedStateHandle:"
+ "setExtendedMACAddress:forSystemCommissionerFabricNode:"
+ "setIdleResetTimer:"
+ "setIpk:"
+ "setPartsListStateCaptureHandle:"
+ "setPartsListStateCaptureInformation:"
+ "setPrivilegeGetter:"
+ "setReportTimeoutNSecs:"
+ "setResidentNodeID:"
+ "setResidentReachabilityUpdateWaitTimer:"
+ "setStateCaptureDeviceConnectedTimer:"
+ "setStateCapturePartsListTimer:"
+ "setWEDSupported:forSystemCommissionerFabricNode:"
+ "setWorkQueue:"
+ "stateCaptureDeviceConnectedTimer"
+ "stateCapturePartsListTimer"
+ "supportsColorTemperatureRangeWithMinColorTemperature:maxColorTemperature:completion:queue:"
+ "syncDataSourceDictionary:forFabric:"
+ "table"
+ "v16@?0@\"NSDictionary\"8"
+ "v32@0:8Q16@24"
+ "v40@0:8@16d24@32"
+ "v44@0:8@?16B24q28@?36"
+ "v48@0:8@16@24@?32@40"
+ "v52@0:8@16@24@32B40@?44"
+ "v56@0:8@16@24@32@?40@?48"
+ "v56@0:8@16^@24^@32^@40^@48"
+ "v80@0:8@16@24@32@40o@48N^q56@64@72"
+ "wedSupportedForSystemCommissionerFabricNode:"
+ "{EndpointID: %@, EndpointData: %@}, "
+ "{Endpoints: {EndpointID: %@, EndpointData: %@ }, "
+ "\xc1A"
+ "\xf2\x92\xf0\xf0\xe1"
- "\x028\x14\x11\x18\x1e"
- "\x11\x19"
- "%{public}@#### Failed refetching NOC for shared user with error %@"
- "%{public}@Check validity period of root cert of fabric ID %@"
- "%{public}@Checking currentFirmwareVersionNumber: %@ with downloadedFirmwareVersionNumber: %@"
- "%{public}@Failed to finish commissioning with error: %@"
- "%{public}@Failed to get cached operational cert for fabricID %@ with error %@"
- "%{public}@Getting root certificate for fabric ID %@"
- "%{public}@HMMTRAccessoryServer handleEventReportForNotification: Ignoring initial event report, this is the batch of outdated reports. event report count=%lu"
- "%{public}@No linked characteristics were found for characteristic %@"
- "%{public}@Read cached operational cert data from disk self.rootCert %@, self.operationalCert %@ self.ownerNodeID %@ self.ownerIPK %@"
- "%{public}@Read color control attribute colorCapabilities: %@ error: %@"
- "%{public}@Returning Root Certificate %@, Operational Certificate %@, Owner NodeID %@, and IPK %@ to Shared user Controller"
- "%{public}@Shared User is attempting to get NOC for fabricID %@"
- "%{public}@Successfully fetched operational certificates from owner. Root Certificate %@, Operational certificate %@, Owner NodeID %@"
- "%{public}@Updated Access Control List (Admin 0x%lX (%@), Operate 0x%lX (%@)) on accessory %@"
- "%{public}@Updated storage after refetching shared user certs"
- "%{public}@Updating OTA Provider state: %@"
- "%{public}@Using already cached values self.rootCert %@, self.operationalCert %@ self.ownerNodeID %@ self.ownerIPK %@"
- "%{public}@Write due to active characteristic (sync): Wrote to system mode attribute, value:%@ (Off)"
- "%{public}@[Flow: %@] addDeviceCredentialKeyData: %@, forUserIndex: %ld"
- "%{public}@[Flow: %@] addIssuerKeyData: %@, forUserIndex: %ld"
- "%{public}@[Flow: %@] addUserAtUserIndex: %ld, withUserUniqueID: %ld, isRemote: %@"
- "%{public}@[Flow: %@] findOrAddUserWithUniqueID: %@, isRemote: %@"
- "@\"HMMTRVendorMetadataStore\""
- "@36@0:8@16B24@28"
- "@44@0:8q16q24B32@36"
- "A&9,\x1f\v\x15"
- "T@\"HMMTRVendorMetadataStore\",R,N,V_vendorMetadataStore"
- "T@\"MTRDevice\",&,V_device"
- "T@\"NSArray\",R,C,N"
- "TB,V_expiredEventsConsumed"
- "TB,V_hasOperationalCerts"
- "TQ,V_currentUserPrivilege"
- "_createHAPServicesFromServiceDescriptions:topology:nodeID:accessoryEndpointID:services:startingServiceInstanceID:primaryAccessory:"
- "_createTransientOperationalCertificateForFabricID:"
- "_expiredEventsConsumed"
- "_fetchCert2ForFabricWithID:isOwner:completion:"
- "_fetchOperationalCertificatesFromResidentForFabricID:completion:"
- "_fetchSharedUserCert2ForFabricWithID:reFetch:completion:"
- "_hasOperationalCerts"
- "_isBridgedAccessoryAndUnreachablePerCacheForCharacteristic:"
- "addDeviceCredentialKeyData:forUserIndex:flow:"
- "addUserAtUserIndex:withUserUniqueID:isRemote:flow:"
- "expiredEventsConsumed"
- "fetchSharedUserCertForFabricWithID:reFetch:completion:"
- "findOrAddUserWithUniqueID:isRemote:flow:"
- "hasOperationalCerts"
- "initSystemCommissionerFabricWithDelegate:"
- "initWithDelegate:"
- "prepareForPairingWithSetupPayload:fabricID:owner:completionHandler:"
- "readAttributeReachableWithParams:"
- "registerOperation:clientQueue:operationResponseHandler:updatedAttributesHandler:"
- "setExpiredEventsConsumed:"
- "setHasOperationalCerts:"
- "supportsColorTemperature:"
- "v72@0:8@16@24@32@40o@48N^q56@64"
- "\xd1A"
- "\xe2\x92\xf0\xf0\x91"

```
