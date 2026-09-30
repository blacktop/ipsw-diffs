## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-153.10.0.0.0
-  __TEXT.__text: 0x15158
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0xfc4
-  __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x4e4
-  __TEXT.__cstring: 0x895
-  __TEXT.__oslogstring: 0x27c4
+165.2.0.2.0
+  __TEXT.__text: 0x17b50
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x1094
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x518
+  __TEXT.__cstring: 0x8b2
+  __TEXT.__oslogstring: 0x2f05
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x648
-  __TEXT.__objc_classname: 0x412
-  __TEXT.__objc_methname: 0x3e71
-  __TEXT.__objc_methtype: 0xfa9
-  __TEXT.__objc_stubs: 0x3480
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0x6a8
+  __TEXT.__objc_classname: 0x452
+  __TEXT.__objc_methname: 0x43a3
+  __TEXT.__objc_methtype: 0xfe2
+  __TEXT.__objc_stubs: 0x3940
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x8b8
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf10
+  __DATA_CONST.__objc_selrefs: 0x1020
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x388
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_arraydata: 0x70
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2fe8
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_const: 0x31e0
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x204
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x21c
   __DATA.__data: 0x720
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 518
-  Symbols:   737
-  CStrings:  1133
+  Functions: 551
+  Symbols:   780
+  CStrings:  1205
 
Symbols:
+ _BMSetsMergeableDeltasResource
+ _NSFileCreationDate
+ _OBJC_CLASS_$_BMPaths
+ _OBJC_CLASS_$_BMPersonaUtilities
+ _OBJC_CLASS_$_CCPersonaSyncManager
+ _OBJC_CLASS_$_CCSetConfiguration
+ _OBJC_METACLASS_$_CCPersonaSyncManager
- _CCSetsRootDirectoryURL
- _OBJC_CLASS_$_NSConstantArray
- _objc_retain_x5
CStrings:
+ "\x01\x11"
+ "\x01!"
+ "\x01#\x11"
+ "\x04"
+ "\x06"
+ "\x11\x17\x11"
+ "%!@(MISSING) could not resolve set identifier for item type %!h(MISSING)u'"
+ "%!@(MISSING) is not entitled to access the set store update service for set: %!@(MISSING)"
+ "%!@(MISSING)-%!@(MISSING).batch"
+ "@\"CCRapportSyncEngine\""
+ "@48@0:8@16@24@32@40"
+ "@48@0:8@16@24@32Q40"
+ "@48@0:8@16Q24d32@40"
+ "@48@0:8^@16@24Q32^@40"
+ "@56@0:8@16@24@32Q40@48"
+ "@84@0:8@16@24S32@36@44Q52@60@68@76"
+ "B20@0:8S16"
+ "CCPersonaSyncManager"
+ "CCRapportDevice[%!@(MISSING)]: tearing down client"
+ "CCRapportFileTransferManager could not get access to sync directory %!@(MISSING)"
+ "CCRapportFileTransferManager: failed to create file transfer directory %!@(MISSING) with error %!@(MISSING)"
+ "CCRapportFileTransferManager: initializing file transfer diretory with url %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): attempting to tear down sync engine but a request is still in progress %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): could not find device to reciprocate with RPOptionSenderIDSDeviceID %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): could not find device to reciprocate with fallback identifier %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): creating operations for syncing sets with device %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): done fetching all deltas from device, signalling remote device we are done fetching %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): evaluating whether device is supported for messaging %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): expecting reciprocal request from device %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): found syncable set %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): no set found on device, but set is registered for sync, initiating day zero request for item type %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): no syncable sets"
+ "CCRapportSyncEngine%!@(MISSING): other device is already syncing so will not reciprocate with us, complete the request %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): received done fetching mergeable deltas message %!@(MISSING) %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): reciprocal request completed with %!@(MISSING) %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): request timed out because no devices are nearby or messages in flight to devices failed to respond in time"
+ "CCRapportSyncEngine%!@(MISSING): signalled remote device we are done fetching %!@(MISSING) with error %!@(MISSING)"
+ "CCRapportSyncEngine%!@(MISSING): syncing to platform %!@(MISSING) is not supported from this device"
+ "CCRapportSyncEngine: received response from signalling end of fetching %!@(MISSING) with error %!@(MISSING)"
+ "CCSignalDoneFetchingMergeableDeltas"
+ "Failed to delete file %!@(MISSING) from file\u00a0transfer directory with error %!@(MISSING)"
+ "Failed to delete mergeable delta at URL %!@(MISSING) with error %!@(MISSING)"
+ "Failed to enumerate contents of file transfer directory %!@(MISSING)"
+ "Failed to fetch attributes of file at path: %!@(MISSING)"
+ "Failed to obtain read only access for mergeable deltas resource %!@(MISSING)"
+ "Failed to obtain write access for resource: %!@(MISSING), error: %!@(MISSING)"
+ "Failed to remove item at url %!@(MISSING) with error %!@(MISSING)"
+ "Failed to resolve set: %!@(MISSING)"
+ "Invalid descriptors: %!@(MISSING)"
+ "Invalid itemType: %!@(MISSING)"
+ "R\x13"
+ "Skipping pruning of temporary file with creation date: %!@(MISSING), not old enough"
+ "T@\"CCDevice\",R,N,V_remoteDevice"
+ "T@\"CCSet\",&,N,V_set"
+ "T@\"NSString\",&,N,V_rapportIdentifier"
+ "T@\"NSString\",R,N,V_personaIdentifier"
+ "T@\"NSURL\",R,N,V_directoryURL"
+ "URLByAppendingPathComponent:"
+ "UUID"
+ "UUIDString"
+ "Unexpected state {completion: %!@(MISSING), request: %!@(MISSING), set: %!@(MISSING)}"
+ "_adminConnection"
+ "_directoryURL"
+ "_mergeableDeltasFileURL"
+ "_personaIdentifier"
+ "_remoteDevice"
+ "_setupDonateConnectionWithItemType:"
+ "_syncEngine"
+ "addBarrierBlock:"
+ "addOperationsToFetchMergeableDeltasFromDevice:isReciprocal:"
+ "allSetsWithOptions:error:"
+ "attributesOfItemAtPath:error:"
+ "beginSetDonationWithItemType:remoteDevice:encodedDescriptors:version:validity:completion:"
+ "buildDoneFetchingMergeableDeltasMessageToDevice:withIsReciprocal:"
+ "buildMergeableDeltasRequestForSet:device:"
+ "com.apple.biomesyncd.cascade.doneFetchingMergeableDeltas"
+ "currentPersonaIdentifier"
+ "currentPersonaIdentifierLoggingDescription"
+ "deleteDanglingFilesFromFileTransferDirectory"
+ "descriptionForTypeIdentifier:"
+ "descriptorsFromEncodedString:error:"
+ "directoryURL"
+ "doneFetchingMergeableDeltasMessageFromPeerToPeerMessage:isReciprocal:rapportIdentifier:"
+ "doneFetchingMergeableDeltasRequestHandler"
+ "enumeratorAtPath:"
+ "fetchMergableDeltasRequestFromPeerToPeerMessage:set:stateVector:atomBatchVersion:"
+ "fetchMergeableDeltasResponseFromPeerToPeerMessage:"
+ "fetchMergeableDeltasWithReason persona is %!@(MISSING)"
+ "fetchMergeableDeltasWithReason:activity:completionHandler:"
+ "fetchReciprocalMergeableDeltasFromDevice:completionHandler:"
+ "fileURLWithPath:"
+ "initWithConnection:manager:itemType:encodedDescriptors:personaIdentifier:version:validity:remoteDevice:accessAssertion:"
+ "initWithDevice:protocolVersion:wallTime:peerPublicKey:"
+ "initWithDirectoryURL:accessAssertion:"
+ "initWithItemType:personaIdentifier:descriptors:options:error:"
+ "initWithItemType:personaIdentifier:encodedDescriptors:options:error:"
+ "initWithRequestManager:xpcConnection:"
+ "initWithSet:readAccess:donateServiceProvider:mergeableDeltasFileURL:"
+ "initWithType:name:descriptors:options:"
+ "initWriterWithMergeableValueID:metadata:formatVersion:fileURL:error:"
+ "legacySetsRootDirectoryURL"
+ "mergeDelta:"
+ "mergeDelta:completion:"
+ "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:set:mergeableDeltaMetadataVectors:fileFormatVersion:peerPublicKey:"
+ "personaIdentifier"
+ "remoteDevice"
+ "removeItemAtURL:error:"
+ "requestAccess:forResource:withMode:error:"
+ "runAsPersonaIdentifier:block:"
+ "sendDoneFetchingMergeableDeltasRequest:toDevice:completionHandler:"
+ "senderIdsIdentifier"
+ "setConfigurationForItemType:"
+ "setFromResourceSpecifier:inContainer:error:"
+ "setIdentifier"
+ "setRapportIdentifier:"
+ "setSet:"
+ "setupSyncEngineToHandleIncomingRequestsForPersona:completionHandler:"
+ "startServerWithCompletion:"
+ "statusFlags"
+ "stringByAppendingPathComponent:"
+ "supportsSyncingWithPlatform:overTransport:inDirection:"
+ "supportsSyncingWithPlatform:overTransport:inDirection:fromPlatform:"
+ "supportsTransport:direction:"
+ "syncAllPersonasNowWithReason:activity:completionHandler:"
+ "syncEngineForCurrentPersona"
+ "syncPolicy"
+ "syncPolicyForSet:"
+ "syncableSetConfigurations"
+ "teardown"
+ "timeIntervalSinceDate:"
+ "v24@?0@\"NSArray\"8@\"NSArray\"16"
+ "v28@0:8@16B24"
+ "v32@0:8@\"CKMergeableDelta\"16@?<v@?S>24"
- "\x01\"\x12"
- "\x02!"
- "\x11\x16\x11"
- "@44@0:8@16@24Q32B40"
- "@48@0:8@16@24Q32@40"
- "@56@0:8@16@24Q32d40@48"
- "@76@0:8@16@24S32@36Q44@52@60@68"
- "B28@0:8S16@20"
- "CCRapportSyncEngine%!@(MISSING): creating operations for syncing sets %!@(MISSING) with device %!@(MISSING)"
- "CCRapportSyncEngine%!@(MISSING): done fetching all deltas from device %!@(MISSING)"
- "CCRapportSyncEngine%!@(MISSING): sets: %!@(MISSING)"
- "CCRapportSyncEngine: holding onto mergeableDelta %!@(MISSING)"
- "CCSetDonationServerExported - %!@(MISSING) could not resolve set identifier for item type %!h(MISSING)u'"
- "CCSetDonationServerExported - %!@(MISSING) is not entitled to access the set store update service for'%!@(MISSING)'"
- "CCSetDonationServerExported could not initialize CCSet with error: %!@(MISSING)"
- "Failed to initialize CKMergeableDeltaMetadata from incoming data %!@(MISSING), %!@(MISSING)"
- "Failed to resolve valid set from request: %!@(MISSING) error: %!@(MISSING)"
- "Q\x13"
- "T@\"<BMAccessAssertion>\",&,N,V_accessAssertion"
- "T@\"CCSet\",R,N,V_set"
- "T@\"NSData\",&,N,V_mergeableDelta"
- "T@\"NSURL\",R,N,V_temporaryDirectoryURL"
- "Unexpected state {completion: %!@(MISSING), request: %!@(MISSING)"
- "_adminService"
- "_isEntitledXPC"
- "_mergeableDelta"
- "_temporaryDirectoryURL"
- "addObjectsFromArray:"
- "addOperationsToFetchMergeableDeltasFromDevice:"
- "allSets:"
- "beginSetDonationWithItemType:fromDevice:encodedDescriptors:version:validity:completion:"
- "buildMergeableDeltasRequestForSet:withIsReciprocal:device:"
- "com.apple.CascadeSets.donate.internal"
- "com.apple.siri.koa.donate.internal"
- "dataWithError:"
- "fetchMergableDeltasRequestFromPeerToPeerMessage:stateVector:atomBatchVersion:isReciprocalRequest:"
- "fetchMergeableDeltasIsReciprocal:reason:activity:completionHandler:"
- "fetchMergeableDeltasResponseFromPeerToPeerMessage:mergeableDelta:mergeableDeltaMetadataVectors:"
- "initWithConnection:manager:itemType:encodedDescriptors:version:validity:device:accessAssertion:"
- "initWithData:metadata:"
- "initWithItemType:encodedDescriptors:error:"
- "initWithRequestManager:xpcConnection:accessAssertion:"
- "initWithSet:"
- "initWithSet:device:protocolVersion:wallTime:peerPublicKey:"
- "initWithSet:readAccess:donateServiceProvider:"
- "initWithType:name:descriptors:"
- "makeXPCConnection:accessAssertion:"
- "mergeDelta:withDeltaMetadata:"
- "mergeDelta:withDeltaMetadata:completion:"
- "mergeableDelta"
- "mergeableDeltaFileTransferMessageMetadataFromPeerToPeerMessage:mergeableDeltaMetadataVectors:fileFormatVersion:peerPublicKey:"
- "setAccessAssertion:"
- "setMergeableDelta:"
- "setupDonateConnectionForSetWithItemType:encodedDescriptors:"
- "startServer"
- "temporaryDirectoryURL"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?S>32"
- "v44@0:8B16Q20@28@?36"
- "valueForEntitlement:"

```
