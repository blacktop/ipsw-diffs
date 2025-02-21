## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x17dec
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1094
+166.12.0.1.0
+  __TEXT.__text: 0x1b0f0
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x159c
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x518
-  __TEXT.__cstring: 0x8b2
-  __TEXT.__oslogstring: 0x30b4
+  __TEXT.__gcc_except_tab: 0x610
+  __TEXT.__cstring: 0xc47
+  __TEXT.__oslogstring: 0x3627
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x690
-  __TEXT.__objc_classname: 0x452
-  __TEXT.__objc_methname: 0x43c7
-  __TEXT.__objc_methtype: 0xfe2
-  __TEXT.__objc_stubs: 0x3940
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x8b8
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x740
+  __TEXT.__objc_classname: 0x46b
+  __TEXT.__objc_methname: 0x48ec
+  __TEXT.__objc_methtype: 0x1098
+  __TEXT.__objc_stubs: 0x3d20
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_selrefs: 0x1190
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x378
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0xb0
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x31e0
+  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__objc_const: 0x3010
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x21c
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x240
   __DATA.__data: 0x720
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 553
-  Symbols:   782
-  CStrings:  1211
+  Functions: 616
+  Symbols:   856
+  CStrings:  1316
 
Symbols:
+ _OBJC_CLASS_$_CCDatabaseDeviceMapping
+ _OBJC_CLASS_$_CCDeviceSite
+ _OBJC_CLASS_$_CCSetChangeXPCListener
+ _OBJC_CLASS_$_NSConstantArray
+ _RPOptionSenderModelID
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _BMSetsResource
- _BMUseCaseWriter
- _CCPersistedKeyValueKeyLocalDeviceIdentifier
- _OBJC_CLASS_$_CCDevice
- _OBJC_CLASS_$_NSNull
- _objc_retain_x10
- _objc_retain_x6
CStrings:
+ "\x02\x12"
+ "\x03\x13"
+ "\x04\x11\x17"
+ "\x11#\x11"
+ "\x13\x11"
+ " and removed %u item(s)"
+ "\""
+ "%@ initialized with update type: %@"
+ "%@ sets root directory: %@"
+ ", client added or updated %u item(s)"
+ "-[CCDifferentialUpdater _tombstoneSet]"
+ "-[CCDifferentialUpdater addItemsWithContents:metaContents:]"
+ "-[CCDifferentialUpdater mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]"
+ "-[CCDifferentialUpdater removeSourceItemIdentifier:]"
+ "@\"CCDeviceSite\""
+ "@\"CCSetChangeXPCListener\""
+ "@32@0:8@16C24S28"
+ "@40@0:8Q16Q24d32"
+ "@60@0:8@16@24@32@40Q48S56"
+ "@64@0:8@16@24@32@40@48@?56"
+ "@64@0:8@16@24@32@40Q48@56"
+ "@64@0:8@16Q24@32@40@48@?56"
+ "@84@0:8@16@24S32@36@44Q52@60Q68@76"
+ "App.InstalledApp"
+ "App.IntentVocabulary.CustomContactGroupName"
+ "App.IntentVocabulary.CustomContactName"
+ "App.IntentVocabulary.CustomMediaPlaylistTitle"
+ "App.IntentVocabulary.CustomVoiceCommandName"
+ "App.Shortcut.Entity"
+ "App.Shortcut.Phrase"
+ "B24@0:8^@16"
+ "B40@0:8@16@24@32"
+ "BMOPACKCodable"
+ "C"
+ "C16@0:8"
+ "CCRapportSyncEngine%@: discovered %@ sets with device %@"
+ "CCRapportSyncEngine%@: discovered synable set %@ for platform %@"
+ "CCRapportSyncEngine%@: failed to enumerate sets with error %@"
+ "CCRapportSyncEngine%@: parent fetch all deltas operation cancelled, cancelling all operations on device operation queue"
+ "CCRapportSyncEngine%@: received fetch mergeable deltas request %@ %@"
+ "CCRapportSyncEngine%@: received set discovery request %@ %@"
+ "CCRapportSyncEngine: item completion handler invoked for url %@ with error %@"
+ "CCRapportSyncEngine: received response from set discovery %@ with error %@"
+ "CCSetDiscoveryRequest"
+ "CCSetDiscoveryResponse"
+ "Cannot construct mergeable deltas without device mapping: %@"
+ "Cannot resolve local device site without device mapping: %@"
+ "Committed update: %@ producing %@ changes%@"
+ "Committing update: %@%@%@"
+ "Completed merge of atom batch for set %@ from device site %@"
+ "Contacts.Contact"
+ "Done syncing in response to set changes with site identifiers %@"
+ "Evaluated set change requiring immmediate sync %@"
+ "Failed access database while handling fetch mergeable deltas request for set: %@ error: %@"
+ "Failed access database while handling file transfer for set: %@ error: %@"
+ "Failed to decode deviceSite from opack encoding %@"
+ "Failed to decode set from opack encoded set %@"
+ "Failed to discover remote sets, cannot proceed to sync with device %@"
+ "Failed to obtain access for maintenance at resource: %@, error: %@"
+ "Failed to obtain access to remove sets root directory with resource: %@, error: %@"
+ "Failed to register peer device site: %@"
+ "Failed to register relayed device site: %@"
+ "Failed to remove"
+ "FullSetDonation"
+ "IncrementalSetDonation"
+ "Local source updating set: %@ with stored local item instance count: %@"
+ "No sets requiring immediate sync, returning from notification handler"
+ "Notified of changes to sets, evaluating policy %@"
+ "R\x11\x11"
+ "Rejecting request %@ with unexpected update type: %@"
+ "Relaying changes not yet supported, dropping atoms for site: %@"
+ "Skipping related device site resolution after device mapping failed: %@"
+ "Skipping relayed device site (%@) matching local device (%@)"
+ "Skipping relayed device site (%@) matching peer device (%@)"
+ "Skipping state vector construction after device mapping failed: %@"
+ "Successfully removed"
+ "Syncing in response to set changes with site identifiers %@ encountered errors %@"
+ "T@\"CCDeviceSite\",&,N,V_deviceSite"
+ "T@\"NSArray\",&,N,V_discoveredSets"
+ "T@\"NSArray\",&,N,V_relayedDeviceSites"
+ "T@\"NSArray\",&,N,V_resolvedSetsToSync"
+ "T@\"NSArray\",&,N,V_setUUIDsSupportingSync"
+ "T@\"NSArray\",&,N,V_setUUIDsToDiscover"
+ "T@\"NSString\",R,N,V_sourceValidity"
+ "TB,R,N,V_isXPC"
+ "TC,R,N,V_updateType"
+ "TQ,N,V_syncReason"
+ "TQ,R,N,V_options"
+ "TQ,R,N,V_sourceVersion"
+ "TQ,R,N,V_syncReason"
+ "TS,N,V_requestOptions"
+ "Triggering immediate sync due to set change for sets %@"
+ "Unknown (%u)"
+ "Unsupported method: %s for update type: %@"
+ "Updater cannot tombstone donations with added or modified items, aborting"
+ "Vv32@0:8@\"BMResourceSpecifier\"16@?<v@?S>24"
+ "Vv32@0:8@16@?24"
+ "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?SqQ>52"
+ "Vv60@0:8S16@20Q28@36Q44@?52"
+ "_cancelled"
+ "_deltaProduced"
+ "_deviceSite"
+ "_discoveredSets"
+ "_isXPC"
+ "_loadCachedDeviceMapping:"
+ "_lock"
+ "_options"
+ "_relayedDeviceSites"
+ "_requestOptions"
+ "_resolvedSetsToSync"
+ "_setChangeListener"
+ "_setUUIDsSupportingSync"
+ "_setUUIDsToDiscover"
+ "_setupAdminConnection"
+ "_shouldCommit"
+ "_sourceValidity"
+ "_sourceVersion"
+ "_syncReason"
+ "_updateType"
+ "allActiveDeviceSites"
+ "allowsAccessToAllSetsWithMode:"
+ "beginSetDonationWithItemType:encodedDescriptors:sourceVersion:sourceValidity:options:completion:"
+ "buildBasePeerToPeerMessage"
+ "buildMergeableDeltasRequestForSet:"
+ "buildVersionedMergeableForSet:readAccess:"
+ "cancel"
+ "com.apple.biomesyncd.cascade.setDiscoveryRequest"
+ "com.apple.biomesyncd.cascadeSetChange"
+ "complete"
+ "constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:"
+ "copyWithExpirationDate:"
+ "databaseReadAccessForSet:error:"
+ "dateWithTimeIntervalSinceNow:"
+ "descriptionForSiteIdentifier:"
+ "deviceSite"
+ "deviceUUID"
+ "discoveredSets"
+ "enumerateAllSets:withOptions:usingBlock:"
+ "fetchDeltasRequestOptions"
+ "fetchMergableDeltasRequestFromPeerToPeerMessage:deviceSite:set:stateVector:atomBatchVersion:requestOptions:"
+ "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:deviceSite:peerPublicKey:"
+ "handleSetChanges:"
+ "initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:sourceVersion:sourceValidity:options:accessAssertion:"
+ "initWithConnection:writeAccess:"
+ "initWithDatabaseAccess:siteIdentifierFormat:"
+ "initWithDeviceRecords:siteIdentifierFormat:error:"
+ "initWithIdentifier:batchHandlerBlock:queue:useCase:"
+ "initWithSet:request:setWriter:database:changeNotifier:completion:"
+ "initWithSyncReason:protocolVersion:wallTime:"
+ "initWithUUID:reason:activity:setUUIDsSupportingSync:queue:completionHandler:"
+ "isRemoteSync"
+ "localDeviceRecord"
+ "localDeviceSite"
+ "lookupSetConfigurationForSet:"
+ "mergeDelta:fromDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:fromDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
+ "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:completion:"
+ "mergeableDeltaAfterStateVector:atomBatchVersion:options:"
+ "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:deviceSite:set:mergeableDeltaMetadataVectors:fileFormatVersion:relayedDeviceSites:"
+ "options"
+ "pathForResource:inContainer:"
+ "performMaintenanceOnAllSets:completion:"
+ "priorLocalSourceValidityHash"
+ "priorLocalSourceVersion"
+ "registerRemoteDeviceSite:isAttestation:returningRowId:"
+ "relayedDeviceSites"
+ "relayedDeviceSitesNotIncludingRequestingDeviceSite:"
+ "remoteCRDTSetDonation"
+ "remoteCRDTSetDonationWithItemType:descriptors:serviceProvider:completion:"
+ "removeAllSets:completion:"
+ "requestOptions"
+ "resolvedSetsToSync"
+ "selectAllDeviceRecords"
+ "sendSetDiscoveryRequest:toDevice:completionHandler:"
+ "senderRapportWorkaroundIdentifier"
+ "setDeviceSite:"
+ "setDiscoveredSets:"
+ "setDiscoveryMessageFromPeerToPeerMessage:setUUIDsToDiscover:"
+ "setDiscoveryRequestHandler"
+ "setDiscoveryResponseFromPeerToPeerMessage:discoveredSets:"
+ "setIdentifiersToDiscover"
+ "setRelayedDeviceSites:"
+ "setRequestOptions:"
+ "setResolvedSetsToSync:"
+ "setSetUUIDsSupportingSync:"
+ "setSetUUIDsToDiscover:"
+ "setSyncReason:"
+ "setUUID"
+ "setUUIDsSupportingSync"
+ "setUUIDsToDiscover"
+ "sourceValidity"
+ "sourceVersion"
+ "supportsTransport:direction:fromPlatform:"
+ "syncReason"
+ "unsignedIntValue"
+ "unsignedLongLongValue"
+ "updateType"
+ "updatedLocalSourceValidityHash"
+ "updatedLocalSourceVersion"
+ "updaterForDonateRequest:toDatabase:"
+ "v16@?0@\"CCSet\"8"
+ "v16@?0@\"NSSet\"8"
+ "v20@0:8S16"
+ "v24@?0@\"CCSetDiscoveryResponse\"8@\"NSError\"16"
+ "v24@?0@?<B@?>8@?<v@?>16"
+ "v48@0:8@\"CKMergeableDelta\"16@\"CCDeviceSite\"24@\"NSArray\"32@?<v@?S>40"
+ "waitForCommit:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\x01\x11"
- "\x01!"
- "\x01#\x11"
- "\x02\x11"
- "\x04\x14"
- "\x04\x17"
- "\t"
- "\x12"
- "@\"CCDevice\""
- "@28@0:8@16C24"
- "@48@0:8@16@24@32Q40"
- "@48@0:8@16Q24d32@40"
- "@56@0:8@16@24@32@40@?48"
- "@56@0:8@16@24@32Q40@48"
- "@72@0:8@16@24@32@40@48@56@?64"
- "@84@0:8@16@24S32@36@44Q52@60@68@76"
- "B24@0:8^B16"
- "CCPeerToPeerMessageOPACKCodable"
- "CCRapportSyncEngine%@: all sets %@"
- "CCRapportSyncEngine%@: no set found on device, but set is registered for sync, initiating day zero request for item type %@"
- "CCRapportSyncEngine%@: received request %@ %@"
- "CCRapportSyncEngine: item completion handler invoked with error %@"
- "Committed dataset update producing %@ changes%@"
- "Committing full set update. Client registered %u item(s)"
- "Committing incremental set update. Client added or updated %u item(s) and removed %u item(s)"
- "Completed merge of atom batch for set %@ from device %@"
- "Could not resolve access assertion for specifier: %@, error: %@"
- "Failed to find local device identifier for set: %@, request: %@, error: %@"
- "Failed to resolve device mapping: %@"
- "R\x13"
- "Relaying changes not yet supported, dropping atoms for site identifier %@"
- "Removed sets root directory URL: %@ success: %@"
- "T@\"CCDevice\",R,N,V_device"
- "T@\"CCDevice\",R,N,V_remoteDevice"
- "T@\"NSArray\",&,N,V_itemTypesSupportingSync"
- "T@\"NSString\",R,N,V_validity"
- "TQ,R,N,V_version"
- "Updater can not tombstone donations with added or modified items, aborting"
- "Updater can not tombstone incremental donations, aborting"
- "Updating set: %@ stored local item instance count: %@"
- "Vv24@0:8@?<v@?S>16"
- "Vv60@0:8S16@\"CCDevice\"20@\"NSString\"28Q36@\"NSString\"44@?<v@?SQ>52"
- "Vv60@0:8S16@20@28Q36@44@?52"
- "YES"
- "_isIncremental"
- "_itemTypesSupportingSync"
- "_localDevice"
- "_localDeviceIdentifier"
- "_remoteDevice"
- "_setupAdminService"
- "_shouldCommit:"
- "_validity"
- "_version"
- "allSetsWithOptions:error:"
- "allowsAccessToSetsWithMode:"
- "beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:"
- "buildMergeableDeltasRequestForSet:device:"
- "buildVersionedMergeableForSet:"
- "constructStateVectorsFromDatabaseOutContent:outMetaContent:outDeviceMapping:error:"
- "databaseReadAccessForSet:"
- "date"
- "deviceIdentifier"
- "encodedStringFromDescriptors:error:"
- "fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:"
- "fileTransferSessionInitiatedResponseFromPeerToPeerMessage:peerPublicKey:"
- "initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:version:validity:remoteDevice:accessAssertion:"
- "initWithConnection:writeAccess:accessAssertion:"
- "initWithData:encoding:"
- "initWithDatabase:device:request:startTimeMicros:"
- "initWithDatabaseAccess:"
- "initWithDevice:protocolVersion:wallTime:peerPublicKey:"
- "initWithIdentifier:options:"
- "initWithItemType:personaIdentifier:descriptors:options:error:"
- "initWithItemType:personaIdentifier:encodedDescriptors:options:error:"
- "initWithSet:device:request:setWriter:database:changeNotifier:completion:"
- "initWithType:name:"
- "initWithUUID:activity:itemTypesSupportingSync:queue:completionHandler:"
- "integerValue"
- "isAsynchronous"
- "isIncremental"
- "itemTypesSupportingSync"
- "legacySetsRootDirectoryURL"
- "localDeviceIdForSet:"
- "mergeDelta:"
- "mergeDelta:completion:"
- "mergeDelta:fromDevice:"
- "mergeableDeltaAfterStateVector:atomBatchVersion:"
- "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:peerPublicKey:"
- "null"
- "persistedKeyValueForKey:database:error:"
- "priorValidityHash"
- "remoteCRDTSetDonationWithItemType:forAccount:fromDevice:descriptors:serviceProvider:completion:"
- "remoteDevice"
- "removeSetsRootDirectory:"
- "senderIdsIdentifier"
- "setItemTypesSupportingSync:"
- "setsWithItemType:"
- "startMaintenanceActivity:"
- "stringValue"
- "syncPolicyForSet:"
- "timeIntervalSince1970"
- "unsignedShortValue"
- "updateValidityHash"
- "updateVersion"
- "v16@?0@?<v@?>8"
- "v32@0:8@\"CKMergeableDelta\"16@?<v@?S>24"
- "validity"
- "version"

```
