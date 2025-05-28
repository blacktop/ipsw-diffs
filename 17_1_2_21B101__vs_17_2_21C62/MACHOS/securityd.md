## securityd

> `/usr/libexec/securityd`

```diff

-61040.42.1.0.0
-  __TEXT.__text: 0x223d28
-  __TEXT.__auth_stubs: 0x38b0
-  __TEXT.__objc_stubs: 0x1a580
-  __TEXT.__objc_methlist: 0x1295c
+61040.62.1.0.0
+  __TEXT.__text: 0x22a708
+  __TEXT.__auth_stubs: 0x38c0
+  __TEXT.__objc_stubs: 0x1a880
+  __TEXT.__objc_methlist: 0x12b6c
   __TEXT.__const: 0x62d
-  __TEXT.__cstring: 0x1edd7
-  __TEXT.__oslogstring: 0x27fef
-  __TEXT.__gcc_except_tab: 0x6a5c
-  __TEXT.__objc_classname: 0x224a
-  __TEXT.__objc_methname: 0x29031
-  __TEXT.__objc_methtype: 0x9268
-  __TEXT.__dlopen_cstrs: 0x114
+  __TEXT.__cstring: 0x1f9f7
+  __TEXT.__oslogstring: 0x28208
+  __TEXT.__gcc_except_tab: 0x6c00
+  __TEXT.__objc_classname: 0x2281
+  __TEXT.__objc_methname: 0x29786
+  __TEXT.__objc_methtype: 0x94f6
+  __TEXT.__dlopen_cstrs: 0x26a
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x623c
-  __DATA_CONST.__auth_got: 0x1c68
+  __TEXT.__unwind_info: 0x62d4
+  __DATA_CONST.__auth_got: 0x1c70
   __DATA_CONST.__got: 0x8f0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x13380
-  __DATA_CONST.__cfstring: 0x1a120
-  __DATA_CONST.__objc_classlist: 0x880
+  __DATA_CONST.__const: 0x135c8
+  __DATA_CONST.__cfstring: 0x1ab20
+  __DATA_CONST.__objc_classlist: 0x890
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0xf60
-  __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__objc_arrayobj: 0x3f0
+  __DATA_CONST.__objc_intobj: 0x13e0
+  __DATA_CONST.__objc_arraydata: 0x468
+  __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x232f0
-  __DATA.__objc_selrefs: 0x8780
+  __DATA.__objc_const: 0x23710
+  __DATA.__objc_selrefs: 0x8870
   __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0xce8
-  __DATA.__objc_superrefs: 0x7e0
-  __DATA.__objc_ivar: 0x184c
-  __DATA.__objc_data: 0x5500
+  __DATA.__objc_classrefs: 0xcf8
+  __DATA.__objc_superrefs: 0x7e8
+  __DATA.__objc_ivar: 0x1888
+  __DATA.__objc_data: 0x55a0
   __DATA.__data: 0x1fe8
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x1a
-  __DATA.__bss: 0x9f8
+  __DATA.__bss: 0xa60
   __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9090
-  Symbols:   1366
-  CStrings:  15014
+  Functions: 9146
+  Symbols:   1367
+  CStrings:  15176
 
Symbols:
+ _objc_retain_x7
CStrings:
+ "\x01\x15\x12\x1b\""
+ "\x03\x12\x11\x11\x1f\x0f\v"
+ "\n"
+ "\f\x11\""
+ "\f\x15"
+ "\x0e"
+ "\x1f\x03"
+ "-[CuttlefishXPCWrapper joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper resetAccountCDPContentsWithSpecificUser:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:reply:]_block_invoke"
+ "<OctagonStateTransitionPath: %@ %@"
+ "@\"AAFAnalyticsEvent\""
+ "@\"AAFAnalyticsEventSecurity\""
+ "@\"NSString\"48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32^@40"
+ "@160@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120#128#136@144@152"
+ "@40@0:8@16Q24^@32"
+ "@48@0:8@16#24@32@40"
+ "@52@0:8@16@24@32B40@44"
+ "@76@0:8@16#24@32@40@48B56@60@68"
+ "AAFAnalyticsEventSecurity"
+ "AAFAnalyticsReporter"
+ "AAFAnalyticsTransportRTC"
+ "Accepting invite for %{public}@: %{private}@"
+ "B48@0:8@16@24@32^^{__CFError}40"
+ "Canceled any pending invitations for participants removed from %{public}@"
+ "Canceled pending invitations for now-deleted group %{public}@"
+ "Class getAAFAnalyticsReporterClass(void)_block_invoke"
+ "Class getAAFAnalyticsTransportRTCClass(void)_block_invoke"
+ "Could not find handle for lookupinfo %{private}@"
+ "Declining invite for group: %{public}@, %{private}@"
+ "Device not in SOS circle"
+ "Did not obtain group object for now-deleted group %{public}@, can't cancel pending invitations"
+ "Expected share metadata not found for group invite %{public}@"
+ "Expected share metadata not found for invite for %@"
+ "Failed to accept shares for invite for group %{public}@: %{public}@"
+ "Failed to cancel (some) pending invitations for now-deleted group %{public}@: %{public}@"
+ "Failed to cancel (some) pending invitations for participants removed from %{public}@: %{public}@"
+ "Failed to decline shares for group invite %{public}@: %{public}@"
+ "Failed to fetch metadata for invites: %{private}@: %{public}@"
+ "Failed to fetch share metadata for group invite %{private}@ for group %{public}@: %{public}@"
+ "Failed to find local share for groupID %{public}@ (%{public}@)"
+ "Failed to stage outgoing share %{private}@ for group %{public}@: %{public}@"
+ "Failed to update mirror with saved record %@ with error=%@"
+ "Fetched %{public}ld groups (%{public}ld of which pending): %{private}@"
+ "Fetched share metadata for group invites: %{private}@"
+ "Fetching and updating participants for %{public}@, %{private}@\n%{private}@"
+ "Metadata fetch error means the share for %{public}@ is no longer accessible to us, will attempt async to decline invitation"
+ "MetricsOverrideTestsAreEnabled"
+ "Participant handle %{private}@ appears to be neither an email or phone number, not looking it up in CloudKit"
+ "ProtectedCloudStorage"
+ "Rejected group update request for non-owned group: %{public}@, %{private}@"
+ "Rejecting updateOctagon for arguments (%@): %@"
+ "SOS not enabled on this platform"
+ "SecurityAnalyticsReporterRTC"
+ "SecurityAnalyticsReporterRTC.m"
+ "Share metadata fetch for invites %{private}@ partly failed (%ld/%ld): %{public}@"
+ "Skipping fetch because a recent fetch was performed"
+ "Skipping participant without handle. This is a bug! %{private}@"
+ "Successfully created/updated and staged CKShare for group create/update request %{public}@"
+ "T@\"AAFAnalyticsEvent\",&,V_event"
+ "T@\"AAFAnalyticsEventSecurity\",&,N,V_eventS"
+ "T@\"NSDictionary\",&,V_stateNumberMap"
+ "T@\"NSDictionary\",R,V_stateNumberMap"
+ "T@\"NSString\",&,N,V_deviceSessionID"
+ "T@\"NSString\",&,N,V_flowID"
+ "T@\"NSString\",&,V_altDSID"
+ "T@\"NSString\",&,V_deviceSessionID"
+ "T@\"NSString\",&,V_flowID"
+ "T@\"NSString\",&,V_unexpectedStateErrorDomain"
+ "T@\"NSString\",R,V_unexpectedStateErrorDomain"
+ "TB,V_areTestsEnabled"
+ "TB,V_firstManateeKeyFetched"
+ "TB,V_isAAAFoundationAvailable"
+ "TB,V_isAuthKitAvailable"
+ "Unable to perform health check on this account type"
+ "Unable to retrieve view state, using ProtectedCloudStorage: %@"
+ "Unknown item error for invite %{public}@, will consider decline a success"
+ "Will return successfully saved group %{private}@"
+ "Zone is inactive; cancelling fetch"
+ "_areTestsEnabled"
+ "_deviceSessionID"
+ "_event"
+ "_eventS"
+ "_firstManateeKeyFetched"
+ "_flowID"
+ "_isAAAFoundationAvailable"
+ "_isAuthKitAvailable"
+ "_stateNumberMap"
+ "_unexpectedStateErrorDomain"
+ "aafanalyticsevent-security: failed to softlink AAAFoundation"
+ "aafanalyticsevent-security: failed to softlink AuthKit"
+ "accountAvailability"
+ "addMetrics:"
+ "analyticsReporterWithTransport:"
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "areTestsEnabled"
+ "availability results: %{private}@"
+ "bool soft_MetricsOverrideTestsAreEnabled(void)"
+ "circleJoiningBlob:flowID:deviceSessionID:applicant:complete:"
+ "com.apple.aaa.dnu"
+ "com.apple.security.acceptorFetchesInitialSyncData"
+ "com.apple.security.cKKSTLKFetch"
+ "com.apple.security.ckks.CKAccountLogin"
+ "com.apple.security.ckks.contentSyncFinish"
+ "com.apple.security.ckks.firstManateeKeyFetch"
+ "com.apple.security.ckks.healKeyHierarchy"
+ "com.apple.security.ckks.healKeyHierarchy.healBrokenRecords"
+ "com.apple.security.ckks.healKeyHierarchy.uploadHealedTLKShares"
+ "com.apple.security.ckks.healTLKShares"
+ "com.apple.security.ckks.healTLKShares.createMissingTLKShares"
+ "com.apple.security.ckks.healTLKShares.uploadMissingTLKShares"
+ "com.apple.security.ckks.launchStart"
+ "com.apple.security.ckks.localReset"
+ "com.apple.security.ckks.localSyncFinish"
+ "com.apple.security.ckks.processIncomingQueue"
+ "com.apple.security.ckks.processIncomingQueue.fixMismatchedViewItems"
+ "com.apple.security.ckks.processIncomingQueue.loadAndProcessIQEs"
+ "com.apple.security.ckks.processOutgoingQueue"
+ "com.apple.security.ckks.processOutgoingQueue.saveCKMirrorEntries"
+ "com.apple.security.ckks.processOutgoingQueue.uploadOQEstoCK"
+ "com.apple.security.ckks.processReceivedKeys"
+ "com.apple.security.ckks.scanLocalItems"
+ "com.apple.security.ckks.scanLocalItems.onboardMissingItems"
+ "com.apple.security.ckks.scanLocalItems.querySyncableItems"
+ "com.apple.security.ckks.syncingPolicySet"
+ "com.apple.security.ckks.trustGain"
+ "com.apple.security.ckks.trustLoss"
+ "com.apple.security.ckks.zoneChangeFetch"
+ "com.apple.security.ckks.zoneCreation"
+ "com.apple.security.cloudKitAccountAvailability"
+ "com.apple.security.createSOSApplication"
+ "com.apple.security.createSOSCircleBlob"
+ "com.apple.security.escrowrequest.state"
+ "com.apple.security.fetchMachineID"
+ "com.apple.security.flush"
+ "com.apple.security.initiatorJoinSOS"
+ "com.apple.security.kVSSyncAndWait"
+ "com.apple.security.keychainitemupgrade.state"
+ "com.apple.security.octagon.state"
+ "com.apple.security.preApprovedJoin"
+ "com.apple.security.prepareIdentityInTPH"
+ "com.apple.security.sosaccount.state"
+ "com.apple.security.updateTDL"
+ "com.apple.security.validatedStashedAccountCredential"
+ "com.apple.security.verifySOSApplication"
+ "com.appple.ckks.state"
+ "could not find CKShareParticipant or KCSharingParticipant for lookupinfo %{private}@ handle %{private}@"
+ "deviceSessionID"
+ "didSucceed"
+ "event"
+ "eventS"
+ "fetch result for lookupInfo %{private}@: participant %{private}@ error %{public}@"
+ "firstManateeKeyFetched"
+ "flowID"
+ "fullFetch"
+ "fullRefetchNeeded"
+ "getEvent"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:"
+ "initNamed:stateMachine:path:initialRequest:"
+ "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:"
+ "initWithContainer:fetchClass:clientMap:fetchReasons:apnsPushes:forceResync:ckoperationGroup:altDSID:"
+ "initWithContainer:fetchClass:reachabilityTracker:altDSID:"
+ "initWithKeychainCircleMetrics:altDSID:eventName:category:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:"
+ "initWithName:states:flags:initialState:queue:stateEngine:unexpectedStateErrorDomain:lockStateTracker:reachabilityTracker:"
+ "initialSyncCredentials:altDSID:flowID:deviceSessionID:complete:"
+ "isAAAFoundationAvailable"
+ "isAuthKitAvailable"
+ "isFullUpload"
+ "isPrioritized"
+ "itemsScanned"
+ "itemsToAdd"
+ "itemsToModify"
+ "joinCircleWithBlob:altDSID:flowID:deviceSessionID:version:complete:"
+ "joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:reply:"
+ "machineID:flowID:deviceSessionID:error:"
+ "myPeerInfo:flowID:deviceSessionID:complete:"
+ "needsReencryption"
+ "newItemsScanned"
+ "newTLKShares"
+ "notifying container of change (simulated)"
+ "numCKRecords"
+ "numKeychainItems"
+ "numMismatchedItems"
+ "numRemoteKeys"
+ "numViews"
+ "numViewsWithNewEntries"
+ "numberOfBluetoothMigrationItemsFetched"
+ "numberOfKeychainItemsCollected"
+ "numberOfPCSItemsFetched"
+ "numberOfTLKsFetched"
+ "octagon-push"
+ "policyDependentViewStateForName:timeout:error:"
+ "policyFreshness"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "resetAccountCDPContentsWithSpecificUser:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:reply:"
+ "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:reply:"
+ "restartOctagonContext:"
+ "rtcAnalyticsReporter"
+ "sendEvent:"
+ "sendMetricForFirstManateeAccess"
+ "sendMetricWithEvent:success:error:"
+ "setAreTestsEnabled:"
+ "setDeviceSessionID:"
+ "setEvent:"
+ "setEventS:"
+ "setFirstManateeKeyFetched:"
+ "setFlowID:"
+ "setIsAAAFoundationAvailable:"
+ "setIsAuthKitAvailable:"
+ "setStateNumberMap:"
+ "setUnexpectedStateErrorDomain:"
+ "simulateReceivePush:reply:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
+ "softlink:o:path:/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle"
+ "stashAccountCredential:altDSID:flowID:deviceSessionID:complete:"
+ "stateNumberMap"
+ "syncWaitAndFlush:flowID:deviceSessionID:error:"
+ "testDropPolicy"
+ "unexpected state '%@'"
+ "unexpectedStateErrorDomain"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v52@0:8I16@\"NSString\"20@\"NSString\"28@\"NSString\"36@?<v@?@\"NSArray\"@\"NSError\">44"
+ "v52@0:8I16@20@28@36@?44"
+ "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v60@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40i48@?<v@?B@\"NSError\">52"
+ "v60@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32B40B44B48@?<v@?@\"NSError\">52"
+ "v60@0:8@16@24@32@40i48@?52"
+ "v60@0:8@16@24@32B40B44B48@?52"
+ "v68@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48B52B56@?<v@?@\"NSError\">60"
+ "v68@0:8@16q24@32@40B48B52B56@?60"
+ "v88@0:8@\"TPSpecificUser\"16@\"NSData\"24@\"NSData\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSString\"64@\"NSString\"72@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">80"
+ "v88@0:8@16@24@32@40@48@56@64@72@?80"
+ "v96@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSArray\"64@\"NSString\"72@\"NSString\"80@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">88"
+ "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
+ "validatedStashedAccountCredential:flowID:deviceSessionID:complete:"
+ "void *AAAFoundationLibrary(void)"
+ "void *KeychainCircleLibrary(void)"
+ "vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:reply:"
+ "zoneIDForViewHint:pcsShortcut:error:"
+ "\xa1"
- "\x01\x12\x12\x1c\""
- "\x03\x12\x11\x11\x1f\x0f\t"
- "\f\x13"
- "\f2"
- "\x0f\x01"
- "\x18"
- "\x1f\x02"
- "-[CuttlefishXPCWrapper joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper resetAccountCDPContentsWithSpecificUser:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:reply:]_block_invoke"
- "@\"NSString\"24@0:8^@16"
- "@144@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120#128#136"
- "@40@0:8@16#24@32"
- "@68@0:8@16#24@32@40@48B56@60"
- "Accepting group invite: %@"
- "CDPCapableHealthCheck"
- "Canceled any pending invitations for participants removed from %@"
- "Canceled pending invitations for now-deleted group %@"
- "Could not find handle for lookupinfo %@"
- "Created TTR with error: %{public}@"
- "Declining group invite: %@"
- "Did not obtain group object for now-deleted group %@, can't cancel pending invitations"
- "Expected share metadata not found for group invite %@"
- "Failed to accept shares for group invite %@: %{public}@"
- "Failed to cancel (some) pending invitations for now-deleted group %@: %@"
- "Failed to cancel (some) pending invitations for participants removed from %@: %@"
- "Failed to decline shares for group invite %@: %{public}@"
- "Failed to fetch metadata for invites: %{public}@: %{public}@"
- "Failed to fetch share metadata for group invite %{public}@ for group %{public}@: %{public}@"
- "Failed to find local share for groupID %@ (%@)"
- "Failed to stage outgoing share %@ for group %{public}@: %{public}@"
- "Failed to update mirror with saved record with error=%@"
- "Fetched %ld groups (%ld of which pending): %@"
- "Fetched share metadata for group invites: %@"
- "Fetching and updating participants for %{public}@\n%{public}@"
- "Groups out of sync, but TTR service not available"
- "Groups out of sync, posting TTR"
- "Metadata fetch error means the share is no longer accessible to us, will attempt async to decline invitation"
- "Participant handle %@ appears to be neither an email or phone number, not looking it up in CloudKit"
- "Rejected group update request for non-owned group: %{public}@, %@"
- "Share metadata fetch for invites %{public}@ partly failed (%ld/%ld): %{public}@"
- "Shared Groups out of sync"
- "Skipping participant without handle. This is a bug! %{public}@"
- "Skipping rpcFetchAndProcessChanges because a recent fetch was performed"
- "StartCompanionPairing"
- "Successfully created/updated and staged CKShare for group create/update request %@"
- "T@\"TPSyncingPolicy\",&,V_policy"
- "Unknown item error for invite %@, will consider decline a success"
- "Will return successfully saved group %{public}@"
- "_policy"
- "availability results: %@"
- "circleJoiningBlob:complete:"
- "could not find CKShareParticipant or KCSharingParticipant for lookupinfo %@ handle %@"
- "defaultConfiguration"
- "fetch result for lookupInfo %@: participant %@ error %@"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:"
- "initNamed:serialQueue:path:initialRequest:"
- "initWithContainer:fetchClass:clientMap:fetchReasons:apnsPushes:forceResync:ckoperationGroup:"
- "initWithContainer:fetchClass:reachabilityTracker:"
- "initWithName:states:flags:initialState:queue:stateEngine:lockStateTracker:reachabilityTracker:"
- "initialSyncCredentials:complete:"
- "it detected a Shared Groups sync issue"
- "joinCircleWithBlob:version:complete:"
- "joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:reply:"
- "machineID:"
- "myPeerInfo:"
- "postGroupsOutOfSyncTTR"
- "resetAccountCDPContentsWithSpecificUser:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:reply:"
- "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:reply:"
- "restartCKKSAccountSyncWithoutSettingPolicyForContext:"
- "setAutoDiagnostics:"
- "setKeywords:"
- "setPolicy:"
- "stashAccountCredential:complete:"
- "syncWaitAndFlush:"
- "v28@0:8I16@?<v@?@\"NSArray\"@\"NSError\">20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v36@0:8@\"NSData\"16i24@?<v@?B@\"NSError\">28"
- "v36@0:8@16i24@?28"
- "v52@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSError\">44"
- "v60@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48@?<v@?@\"NSError\">52"
- "v60@0:8@16q24@32@40B48@?52"
- "v72@0:8@\"TPSpecificUser\"16@\"NSData\"24@\"NSData\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">64"
- "v80@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSArray\"64@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">72"
- "validatedStashedAccountCredential:"
- "vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:reply:"

```
