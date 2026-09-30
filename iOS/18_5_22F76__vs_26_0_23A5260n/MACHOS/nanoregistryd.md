## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-989.21.0.0.0
-  __TEXT.__text: 0xfd7ac
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x10d00
-  __TEXT.__objc_methlist: 0xd704
-  __TEXT.__const: 0x678
-  __TEXT.__gcc_except_tab: 0x2638
-  __TEXT.__objc_methname: 0x1bd23
-  __TEXT.__cstring: 0xd7c2
-  __TEXT.__oslogstring: 0x14a14
-  __TEXT.__objc_classname: 0x21a5
-  __TEXT.__objc_methtype: 0x492e
+1027.4.0.0.0
+  __TEXT.__text: 0x103d38
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_stubs: 0x10d80
+  __TEXT.__objc_methlist: 0xd8c4
+  __TEXT.__const: 0x688
+  __TEXT.__gcc_except_tab: 0x2658
+  __TEXT.__objc_methname: 0x1c0fd
+  __TEXT.__cstring: 0xda55
+  __TEXT.__oslogstring: 0x15626
+  __TEXT.__objc_classname: 0x225b
+  __TEXT.__objc_methtype: 0x49be
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x39e0
-  __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0xc78
+  __TEXT.__unwind_info: 0x3a40
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4b50
-  __DATA_CONST.__cfstring: 0xbb40
-  __DATA_CONST.__objc_classlist: 0x7a8
+  __DATA_CONST.__const: 0x49d8
+  __DATA_CONST.__cfstring: 0xbc20
+  __DATA_CONST.__objc_classlist: 0x7c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x3d0
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_intobj: 0xde0
   __DATA_CONST.__objc_doubleobj: 0xb0
   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x19840
-  __DATA.__objc_selrefs: 0x5d30
-  __DATA.__objc_ivar: 0x1174
-  __DATA.__objc_data: 0x4c90
+  __DATA.__objc_const: 0x19f30
+  __DATA.__objc_selrefs: 0x5dc8
+  __DATA.__objc_ivar: 0x11c4
+  __DATA.__objc_data: 0x4dd0
   __DATA.__data: 0x19d8
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x488
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: E4568193-B8A7-3AA8-98EF-7A47C412A178
-  Functions: 5694
-  Symbols:   689
-  CStrings:  10039
+  UUID: 692FB18F-57E1-36AD-9FA7-595DFE12449A
+  Functions: 5750
+  Symbols:   696
+  CStrings:  10146
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFDataGetTypeID
+ _NRDevicePropertyIsStagedForTransfer
+ _NRDevicePropertyRunnableArchNames
+ _NRDevicePropertyTransferType
+ _OBJC_CLASS_$_NRMutableDeviceProperty
+ _OBJC_CLASS_$_NRRegistryProxy
+ _SecCopyErrorMessageString
+ _kSecMatchLimitAll
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ "\nPairing Manager (migration): %@"
+ "%s No more migration candidates to scan for"
+ "%s calling watchTransferManager unstageDevice:completion:"
+ "%s identifier: requested nrUUID = %{public}@; got newly paired BTUUID = %{public}@ error:%{public}@"
+ "%s no EPSagaOperandNewlyPairedNetworkRelayIDKey"
+ "%s: _migrationScanIdentifiers = %@"
+ "-[EPSagaTransactionUnstageFromWatchTransferManager beginTransactionWithRoutingSlipEntry:serviceRegistry:]"
+ "-[EPSagaTransactionUnstageFromWatchTransferManager beginTransactionWithRoutingSlipEntry:serviceRegistry:]_block_invoke"
+ "-[NRPairingDaemon xpcListWatchStagedForTransferWithCompletion:]"
+ "-[NRPairingDaemon xpcStageWatchForGraduationWithDeviceID:completion:]"
+ "-[NRPairingDaemon xpcStageWatchForTransferWithDeviceID:completion:]"
+ "-[NetworkRelayAgent addMigrationScanCandidates:]"
+ "-[NetworkRelayAgent removeMigrationScanCandidates:]"
+ "-[NetworkRelayAgent startScanningForMigrationCandidates]"
+ "-[WatchTransferManager _createLocalNRDevicesForStagedWatches:]"
+ "-[WatchTransferManager _retrieveWatchesStagedForTransferFromKeychain]"
+ "-[WatchTransferManager retrieveWatchesStagedForTransfer]"
+ "-[WatchTransferManager unstageDevice:completion:]"
+ "27EC88C0-A142-4C22-BCEB-4B6A90B5184F"
+ "32"
+ "38627122-E97A-4089-861C-81704B480D2E"
+ "Adding EPSagaTransactionSendGraduateMessage to EPDTC"
+ "Adding properties for a staged device:- regular transfer of a family Watch"
+ "Checking if device with pairing ID %{public}@ (alternate account: %{BOOL}d) can be staged for transfer"
+ "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
+ "Device %{public}@ is staged for transfer, ignoring."
+ "Device with identifier %{public}@ is not fully paired yet"
+ "Device with identifier %{public}@ not found"
+ "DeviceSupportsContextualVolume"
+ "Dump timestamp: %.6f"
+ "EPKeychain: Failed to retrieve a list of watch transfer data, result = %ld"
+ "EPKeychain: Failed to store watch transfer data, result = %ld"
+ "EPKeychain: added data %@"
+ "EPKeychain: dataRef isn't CFData???"
+ "EPKeychain: failed to remove transfer data, result = %ld"
+ "EPKeychain: failed to remove transfer data, result = %{public}@"
+ "EPKeychain: no watch transfer data in account"
+ "EPKeychain: stored watch transfer data with length %ld"
+ "EPKeychain: successfully removed transfer data"
+ "EPKeychain: transfer data is NOT an array!"
+ "EPKeychain: transfer data is an array!"
+ "EPKeychain: watch transfer data not present"
+ "EPMigrationAutoTrigger: Ignorable Error: %@"
+ "EPMigrationAutoTrigger: locked=%{BOOL}d, _hasSwitchAssertion=%{BOOL}d, needsSync=%{BOOL}d"
+ "EPMigrationAutoTrigger: no more migratable candidates"
+ "EPMigrationAutoTrigger: unlocked=%{BOOL}d, becameUnlocked=%{BOOL}d"
+ "EPSagaTransactionSendGraduateMessage"
+ "EPSagaTransactionSendGraduateMessageTransaction"
+ "EPSagaTransactionUnstageFromWatchTransferManager"
+ "EPSagaTransactionUnstageWatch"
+ "Failed to init NRPBWatchTransferStagingRequest from data!"
+ "Failed to register for NanoRegistry View Hint notification: %ld"
+ "Failed to store Watch Transfer Staging Request for a Watch with advertised name %@, Phone side info: nrUUID=%@"
+ "Generated new pairing ID for staged Watch %@ as %@"
+ "Graduate request to BT UUID %@ success = %{BOOL}d"
+ "NRPBGraduationRequest"
+ "NRPBWatchTransferStagingRequest"
+ "NanoRegistry-1027.4"
+ "NetworkRelayPairing is in progress but no more candidates, stop scanning"
+ "NetworkRelayPairing migration discovery in progress and actively migrating"
+ "NetworkRelayPairing migration discovery in progress but not actively migrating (StatusCode %lu), stopping"
+ "Now %f, last version broadcast %@, diff %f vs. %f"
+ "Pairing Manager: %@"
+ "Phone Side Information for Watch transfer"
+ "Phone Side Information for Watch transfer sent"
+ "Request to start scanning with different set of migration candidates, resetting. current %@, new %@"
+ "Request to start scanning with identical set of migration candidates, no need to reset manager. current %@"
+ "Requesting to start scanning with an empty set of candidate identifiers!"
+ "RestoringDiff = %@"
+ "Reuse existing NRDevicePairingManager to scan for candidates"
+ "Sending Phone side information for Watch staging to %@"
+ "Setting properties for a staged device:- graduation transfer"
+ "Setting properties for a staged device:- regular transfer"
+ "Skip broadcasting system versions to inactive watches"
+ "Skip checking duplicate for staged device %{public}@"
+ "Staged Watch %@ was already in the registry, ignored"
+ "Staging alternate account device with pairing ID %{public}@, altAccountIdentifier %{public}@"
+ "Staging device with pairing ID %{public}@ (serial number %@)"
+ "Staging request does not have BuddyStage set, assuming all completed."
+ "Starting migration discovery (new manager)"
+ "Successfully stored Watch Transfer Staging Request for a Watch with advertised name %@, Phone side info: nrUUID=%@"
+ "T@\"NSString\",R,N,V_serialNumber"
+ "TB,R,N,V_watchTransfer"
+ "Telling Watch to Graduate! BT UUID %@"
+ "There's some changes to NanoRegistry View Hint!"
+ "Timeout NetworkRelay migration"
+ "Unable to set properties for graduation transfer, required properties not present"
+ "Unable to set properties for unrecognized transfer type: %u"
+ "Unable to unstage device with pairing ID %{public}@ (can't find serial)"
+ "Unstaging device with pairing ID %{public}@ (serial %{private}@)"
+ "Watch graduation request"
+ "WatchTransferManager"
+ "_activeMigrationScanIdentifiers"
+ "_altAccountIdentifier"
+ "_isAltAccount"
+ "_keychainViewHintToken"
+ "_migrationIDSCloudIdentifier"
+ "_phoneName"
+ "_phoneSerialNumber"
+ "_requestedMigrationScanIdentifiers"
+ "_retrieveWatchesStagedForTransferFromKeychain"
+ "_serialNumber"
+ "_setError"
+ "_shouldBroadcastVersion"
+ "_transferType"
+ "_watchBuddyStage"
+ "_watchNetworkRelayIdentifierOnPhone"
+ "_watchTransfer"
+ "addMigrationScanCandidates:"
+ "addTellWatchToGraduateTransaction"
+ "altAccountIdentifier"
+ "centralManager:didUpdateSynchronizationEventForPeripheral:results:"
+ "com.apple.security.view-change.DevicePairing"
+ "deprecateIRN1"
+ "deviceInfoDidChange:deviceInfo:"
+ "fullDescription"
+ "getBytes:range:"
+ "initWithObjects:"
+ "lastVersionBroadcastTimestamp"
+ "migrationIDSCloudIdentifier"
+ "networkRelayUnpairingCompletedWithError called with error %{public}@"
+ "networkRelayUnpairingCompletedWithError:"
+ "phoneName"
+ "phoneSerialNumber"
+ "position"
+ "receivedWatchTransferStagingRequestWithData: %@"
+ "remoteObject:receivedWatchTransferStagingRequestWithData:"
+ "removeMigrationScanCandidates:"
+ "removeWatchTransferDataForWatchWithIdentifier:"
+ "resetStashVariables"
+ "retrieveWatchTransferData"
+ "retrieveWatchesStagedForTransfer"
+ "sendGraduationRequestToIDSBTUUID:withResponseBlock:"
+ "sendWatchTransferRequestToDestination:withWatchTransferStagingRequest:withSentBlock:"
+ "sentBlock called"
+ "serialNumber"
+ "setPosition:"
+ "stageDeviceToTransferForTransferWithType:device:completion:"
+ "startScanningForMigrationCandidates"
+ "storeWatchTransferData:watchIdentifier:"
+ "tellWatchToGraduate"
+ "transferType"
+ "unsetProperties"
+ "unstageDevice:completion:"
+ "unstageWatch"
+ "unstageWatchFromTransferManager"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NRDeviceInfo\"24"
+ "v32@0:8@\"NRRemoteObjectTinker\"16@\"NSData\"24"
+ "v32@?0@\"NRPBWatchTransferStagingRequest\"8Q16^B24"
+ "v32@?0@\"NSData\"8Q16^B24"
+ "v36@0:8I16@20@?28"
+ "watchBuddyStage"
+ "watchNetworkRelayIdentifierOnPhone"
+ "watchTransfer"
+ "watch_transfer"
+ "watchtransfer"
+ "xpcListWatchStagedForTransferWithCompletion:"
+ "xpcStageWatchForGraduationWithDeviceID:completion:"
+ "xpcStageWatchForTransferWithDeviceID:completion:"
+ "{?=\"watchBuddyStage\"b1\"isAltAccount\"b1}"
- "%s identifier: %{public}@ error:%{public}@"
- "-[NetworkRelayAgent startScanningForMigrationCandidatesWithNetworkRelayIdentifiers:]"
- "526"
- "Cached state dump is %s:- cached history index %lu; current history index %lu"
- "Dump timestamp: %@ (%.6f)"
- "Ignorable Error: %@"
- "Internal functionality not available in customer builds"
- "NRPBSwitchRecord"
- "NRPBSwitchRecordCollection"
- "NRRegistryProxy"
- "NanoRegistry-989.21"
- "NetworkRelayPairing is enabled, stop scanning for migratable Watches using NetworkRelay"
- "Received a request to start scanning for different set of migration candidates, resetting the current scanning manager"
- "Received a request to start scanning for same set of migration candidates, no-op"
- "ResumeReminder"
- "Reuse existing NRDevicePairingManager to scan for candiates"
- "Starting migration discovery"
- "_dateTimeInterval"
- "_deviceIDBytes"
- "_hasInternalEntitlement"
- "_migrationScanIdentifiers"
- "_records"
- "_switchIndex"
- "client %{public}@ is missing the %@ entitlement"
- "clientRemoteObjectInterface"
- "com.apple.bluetoothregistry"
- "com.apple.nano.nanoregistry"
- "com.apple.nano.nanoregistry.applydiff"
- "com.apple.nano.nanoregistry.generalaccess"
- "com.apple.nano.nanoregistry.ids.plugin"
- "com.apple.nano.nanoregistry.internal"
- "com.apple.nano.nanoregistry.paireddeviceregistry"
- "com.apple.nano.nanoregistry.pairunpairobliterate"
- "com.apple.nano.nanoregistry.submitrtcpairingmetric"
- "com.apple.nano.nanoregistry.unpairwithbrick"
- "com.apple.nanoregistry.BDE85C67-0FDD-4A95-A9B9-3CB5DD0C06A2"
- "connection"
- "dateTimeInterval"
- "deviceIDBytes"
- "enclosedClassTypes"
- "entitlement required"
- "fresh"
- "hasEntitlement:"
- "hasEntitlements"
- "launchedBy=%@"
- "loudHasEntitlement:"
- "networkRelayPairingCompletedWithError called with error %{public}@"
- "records"
- "resetStashVaribles"
- "runCompletionBlock:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "stale"
- "startScanningForMigrationCandidatesWithNetworkRelayIdentifiers:"
- "v12@?0I8"
- "v16@?0@\"NRDeviceCollectionHistory\"8"
- "v16@?0@\"NSDictionary\"8"
- "v16@?0B8B12"
- "v20@?0B8q12"
- "v24@?0@\"NSUUID\"8@\"NSDate\"16"
- "v36@?0@\"NRDeviceCollectionDiff\"8@\"NSDictionary\"16B24Q28"
- "v36@?0@\"NRMutableDeviceCollection\"8@\"NRSecureDevicePropertyStore\"16Q24B32"
- "{?=\"dateTimeInterval\"b1\"switchIndex\"b1}"

```
