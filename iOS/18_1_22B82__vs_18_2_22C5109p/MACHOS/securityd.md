## securityd

> `/usr/libexec/securityd`

```diff

-61439.42.2.0.0
-  __TEXT.__text: 0x22f5f0
+61439.60.91.502.1
+  __TEXT.__text: 0x22fcec
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a540
-  __TEXT.__objc_methlist: 0x12974
-  __TEXT.__const: 0x8cd
-  __TEXT.__cstring: 0x203f2
-  __TEXT.__oslogstring: 0x28d78
-  __TEXT.__gcc_except_tab: 0xac5c
-  __TEXT.__objc_classname: 0x22ba
-  __TEXT.__objc_methname: 0x2937c
-  __TEXT.__objc_methtype: 0x9927
-  __TEXT.__dlopen_cstrs: 0x2c4
+  __TEXT.__objc_stubs: 0x1a460
+  __TEXT.__objc_methlist: 0x128c4
+  __TEXT.__const: 0x8d5
+  __TEXT.__cstring: 0x1f896
+  __TEXT.__oslogstring: 0x28ee9
+  __TEXT.__gcc_except_tab: 0xac90
+  __TEXT.__objc_classname: 0x2283
+  __TEXT.__objc_methname: 0x291e5
+  __TEXT.__objc_methtype: 0x995f
+  __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6288
+  __TEXT.__unwind_info: 0x6200
   __DATA_CONST.__auth_got: 0x1c70
-  __DATA_CONST.__got: 0xdd0
+  __DATA_CONST.__got: 0x1040
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x131a0
-  __DATA_CONST.__cfstring: 0x1af80
-  __DATA_CONST.__objc_classlist: 0x880
+  __DATA_CONST.__const: 0x13080
+  __DATA_CONST.__cfstring: 0x1a580
+  __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x7e0
-  __DATA_CONST.__objc_intobj: 0x1308
+  __DATA_CONST.__objc_superrefs: 0x7d8
+  __DATA_CONST.__objc_intobj: 0x12d8
   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23698
-  __DATA.__objc_selrefs: 0x87a0
-  __DATA.__objc_ivar: 0x186c
-  __DATA.__objc_data: 0x5500
+  __DATA.__objc_const: 0x234a8
+  __DATA.__objc_selrefs: 0x8738
+  __DATA.__objc_ivar: 0x1854
+  __DATA.__objc_data: 0x5460
   __DATA.__data: 0x20b8
   __DATA.__thread_vars: 0xd8
   __DATA.__thread_bss: 0x1e
-  __DATA.__bss: 0xa48
+  __DATA.__bss: 0x9d0
   __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
+  - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9096
-  Symbols:   1373
-  CStrings:  15248
+  Functions: 9062
+  Symbols:   1451
+  CStrings:  15132
 
Symbols:
+ _OBJC_CLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
+ _kSecurityRTCEventCategoryAccountDataAccessRecovery
+ _kSecurityRTCEventNameAcceptorFetchesInitialSyncData
+ _kSecurityRTCEventNameCKAccountLogin
+ _kSecurityRTCEventNameCKKSTlkFetch
+ _kSecurityRTCEventNameCloudKitAccountAvailability
+ _kSecurityRTCEventNameContentSyncFinish
+ _kSecurityRTCEventNameCreateMissingTLKShares
+ _kSecurityRTCEventNameCreateSOSCircleBlob
+ _kSecurityRTCEventNameCreatesSOSApplication
+ _kSecurityRTCEventNameFetchMachineID
+ _kSecurityRTCEventNameFirstManateeKeyFetch
+ _kSecurityRTCEventNameFixMismatchedViewItems
+ _kSecurityRTCEventNameFlush
+ _kSecurityRTCEventNameHealBrokenRecords
+ _kSecurityRTCEventNameHealKeyHierarchy
+ _kSecurityRTCEventNameHealTLKShares
+ _kSecurityRTCEventNameInitiatorJoinsSOS
+ _kSecurityRTCEventNameKVSSyncAndWait
+ _kSecurityRTCEventNameLaunchStart
+ _kSecurityRTCEventNameLoadAndProcessIQEs
+ _kSecurityRTCEventNameLocalReset
+ _kSecurityRTCEventNameLocalSyncFinish
+ _kSecurityRTCEventNameOnboardMissingItems
+ _kSecurityRTCEventNamePreApprovedJoin
+ _kSecurityRTCEventNamePrepareIdentityInTPH
+ _kSecurityRTCEventNameProcessIncomingQueue
+ _kSecurityRTCEventNameProcessOutgoingQueue
+ _kSecurityRTCEventNameProcessReceivedKeys
+ _kSecurityRTCEventNameQuerySyncableItems
+ _kSecurityRTCEventNameSaveCKMirrorEntries
+ _kSecurityRTCEventNameScanLocalItems
+ _kSecurityRTCEventNameSyncingPolicySet
+ _kSecurityRTCEventNameTrustGain
+ _kSecurityRTCEventNameTrustLoss
+ _kSecurityRTCEventNameTrustedDeviceListFailure
+ _kSecurityRTCEventNameUpdateTDL
+ _kSecurityRTCEventNameUploadHealedTLKShares
+ _kSecurityRTCEventNameUploadMissingTLKShares
+ _kSecurityRTCEventNameUploadOQEsToCK
+ _kSecurityRTCEventNameValidatedStashedAccountCredential
+ _kSecurityRTCEventNameVerifySOSApplication
+ _kSecurityRTCEventNameZoneChangeFetch
+ _kSecurityRTCEventNameZoneCreation
+ _kSecurityRTCFieldAvgCKRecords
+ _kSecurityRTCFieldAvgErrorItemsProcessed
+ _kSecurityRTCFieldAvgRemoteKeys
+ _kSecurityRTCFieldAvgSuccessfulItemsProcessed
+ _kSecurityRTCFieldErrorItemsProcessed
+ _kSecurityRTCFieldFullFetch
+ _kSecurityRTCFieldFullRefetchNeeded
+ _kSecurityRTCFieldIsFullUpload
+ _kSecurityRTCFieldIsLocked
+ _kSecurityRTCFieldIsPrioritized
+ _kSecurityRTCFieldItemsScanned
+ _kSecurityRTCFieldItemsToAdd
+ _kSecurityRTCFieldItemsToDelete
+ _kSecurityRTCFieldItemsToModify
+ _kSecurityRTCFieldMissingKey
+ _kSecurityRTCFieldNeedsReencryption
+ _kSecurityRTCFieldNewItemsScanned
+ _kSecurityRTCFieldNewTLKShares
+ _kSecurityRTCFieldNumKeychainItems
+ _kSecurityRTCFieldNumMismatchedItems
+ _kSecurityRTCFieldNumViews
+ _kSecurityRTCFieldNumViewsWithNewEntries
+ _kSecurityRTCFieldNumberOfBluetoothMigrationItemsFetched
+ _kSecurityRTCFieldNumberOfKeychainItemsCollected
+ _kSecurityRTCFieldNumberOfPCSItemsFetched
+ _kSecurityRTCFieldNumberOfTLKsFetched
+ _kSecurityRTCFieldPendingClassA
+ _kSecurityRTCFieldPolicyFreshness
+ _kSecurityRTCFieldSuccessfulItemsProcessed
+ _kSecurityRTCFieldSyncingPolicy
+ _kSecurityRTCFieldTotalCKRecords
+ _kSecurityRTCFieldTotalRemoteKeys
+ _kSecurityRTCFieldTrustStatus
CStrings:
+ "-[CuttlefishXPCWrapper octagonPeerIDGivenBottleIDWithSpecificUser:bottleID:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper trustedDeviceNamesByPeerIDWithSpecificUser:reply:]_block_invoke"
+ "<CuttlefishCurrentItem(%!@(MISSING))>"
+ "<CuttlefishCurrentItemSpecifier(%!@(MISSING)): %!@(MISSING)>"
+ "<CuttlefishPCSIdentity(%!@(MISSING))>"
+ "<CuttlefishPCSServiceIdentifier(%!@(MISSING)): %!@(MISSING)>"
+ "Could not find key material in keychain: %!@(MISSING)"
+ "Errored fetching TLK shares, unable to decrypt identities: %!@(MISSING)"
+ "Errored fetching TLK shares: %!@(MISSING)"
+ "Errored fetching parent key: %!@(MISSING)"
+ "Errored saving synckey to keychain: %!@(MISSING)"
+ "Errored unwrapping TLK %!@(MISSING): %!@(MISSING)"
+ "Errored unwrapping TLK Shares, quitting: %!@(MISSING)"
+ "Errored unwrapping sync keys, quitting: %!@(MISSING)"
+ "Have items needing re-encryption, but device is locked"
+ "Octagon peerID not trusted for record %!@(MISSING): %!@(MISSING)"
+ "Successfully retrieved current items: %!@(MISSING)"
+ "Successfully retrieved identities: %!@(MISSING)"
+ "Unable to decrypt synckey %!@(MISSING): %!@(MISSING)"
+ "Unable to fetch names by peerID: %!@(MISSING)"
+ "Unable to find bottleID: %!@(MISSING)"
+ "ckks-oob"
+ "decryptCurrentItems:cache:complete:"
+ "decryptPCSIdentities:cache:complete:"
+ "ensureKeyLoadedForContextID:cache:error:"
+ "error fetching tlk shares: %!@(MISSING)"
+ "fetchRecoverableTLKShares:peerID:contextID:reply:"
+ "fetchTrustedDeviceNamesByPeerID:"
+ "octagonPeerIDGivenBottleIDWithSpecificUser:bottleID:reply:"
+ "populateWithRecords:contextID:"
+ "trustedDeviceNamesByPeerIDWithSpecificUser:reply:"
+ "unwrapKeysAndSaveToCache:syncKeys:error:"
+ "unwrapTLKAndSaveToCache:tlks:tlkShares:error:"
+ "unwrapViaKeyHierarchy:error:"
+ "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v48@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "@\"AAFAnalyticsEvent\""
- "@56@0:8@16@24@32B40@44B52"
- "@72@0:8@16@24@32@40@48B56B60@64"
- "AAFAnalyticsEvent"
- "AAFAnalyticsEvent+Security.m"
- "AAFAnalyticsEventSecurity"
- "AAFAnalyticsReporter"
- "AAFAnalyticsTransportRTC"
- "AKAccountManager"
- "Class getAAFAnalyticsEventClass(void)_block_invoke"
- "Class getAAFAnalyticsReporterClass(void)_block_invoke"
- "Class getAAFAnalyticsTransportRTCClass(void)_block_invoke"
- "Class getAKAccountManagerClass(void)_block_invoke"
- "NSString *getkAAFDeviceSessionId(void)"
- "NSString *getkAAFFlowId(void)"
- "Octagon peerID not trusted for record %!@(MISSING)"
- "SecurityAnalyticsReporterRTC"
- "SecurityAnalyticsReporterRTC.m"
- "T@\"AAFAnalyticsEvent\",&,V_event"
- "TB,V_areTestsEnabled"
- "TB,V_canSendMetrics"
- "TB,V_isAAAFoundationAvailable"
- "TB,V_isAuthKitAvailable"
- "_areTestsEnabled"
- "_canSendMetrics"
- "_event"
- "_isAAAFoundationAvailable"
- "_isAuthKitAvailable"
- "aafanalyticsevent-security: failed to softlink AAAFoundation"
- "aafanalyticsevent-security: failed to softlink AuthKit"
- "accountAccessTelemetryOptInForAccount:"
- "analyticsReporterWithTransport:"
- "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
- "areTestsEnabled"
- "authKitAccountWithAltDSID returned error: %!@(MISSING)"
- "avgCKRecords"
- "avgErrorItemsProcessed"
- "avgRemoteKeys"
- "avgSuccessfulItemsProcessed"
- "bottles"
- "canSendMetrics"
- "com.apple.aaa.dnu"
- "com.apple.security.aafanalyticsevent.queue"
- "com.apple.security.acceptorFetchesInitialSyncData"
- "com.apple.security.cKKSTLKFetch"
- "com.apple.security.ckks.CKAccountLogin"
- "com.apple.security.ckks.contentSyncFinish"
- "com.apple.security.ckks.firstManateeKeyFetch"
- "com.apple.security.ckks.healKeyHierarchy"
- "com.apple.security.ckks.healKeyHierarchy.healBrokenRecords"
- "com.apple.security.ckks.healKeyHierarchy.uploadHealedTLKShares"
- "com.apple.security.ckks.healTLKShares"
- "com.apple.security.ckks.healTLKShares.createMissingTLKShares"
- "com.apple.security.ckks.healTLKShares.uploadMissingTLKShares"
- "com.apple.security.ckks.launchStart"
- "com.apple.security.ckks.localReset"
- "com.apple.security.ckks.localSyncFinish"
- "com.apple.security.ckks.processIncomingQueue"
- "com.apple.security.ckks.processIncomingQueue.fixMismatchedViewItems"
- "com.apple.security.ckks.processIncomingQueue.loadAndProcessIQEs"
- "com.apple.security.ckks.processOutgoingQueue"
- "com.apple.security.ckks.processOutgoingQueue.saveCKMirrorEntries"
- "com.apple.security.ckks.processOutgoingQueue.uploadOQEstoCK"
- "com.apple.security.ckks.processReceivedKeys"
- "com.apple.security.ckks.scanLocalItems"
- "com.apple.security.ckks.scanLocalItems.onboardMissingItems"
- "com.apple.security.ckks.scanLocalItems.querySyncableItems"
- "com.apple.security.ckks.syncingPolicySet"
- "com.apple.security.ckks.trustGain"
- "com.apple.security.ckks.trustLoss"
- "com.apple.security.ckks.zoneChangeFetch"
- "com.apple.security.ckks.zoneCreation"
- "com.apple.security.cloudKitAccountAvailability"
- "com.apple.security.createSOSApplication"
- "com.apple.security.createSOSCircleBlob"
- "com.apple.security.fetchMachineID"
- "com.apple.security.flush"
- "com.apple.security.initiatorJoinSOS"
- "com.apple.security.kVSSyncAndWait"
- "com.apple.security.preApprovedJoin"
- "com.apple.security.prepareIdentityInTPH"
- "com.apple.security.trustedDeviceListFailure"
- "com.apple.security.updateTDL"
- "com.apple.security.validatedStashedAccountCredential"
- "com.apple.security.verifySOSApplication"
- "device_name"
- "didSucceed"
- "dynamicInfo"
- "ensureKeyLoadedForContextID:error:"
- "event"
- "fullFetch"
- "fullRefetchNeeded"
- "getEvent"
- "included"
- "initWithEventName:eventCategory:initData:"
- "initWithKeychainCircleMetrics:altDSID:eventName:category:"
- "isAAAFoundationAvailable"
- "isAuthKitAvailable"
- "isFullUpload"
- "isPrioritized"
- "itemsScanned"
- "itemsToAdd"
- "itemsToModify"
- "kAAFDeviceSessionId"
- "kAAFFlowId"
- "needsReencryption"
- "newItemsScanned"
- "newTLKShares"
- "numKeychainItems"
- "numMismatchedItems"
- "numViews"
- "numViewsWithNewEntries"
- "numberOfBluetoothMigrationItemsFetched"
- "numberOfKeychainItemsCollected"
- "numberOfPCSItemsFetched"
- "numberOfTLKsFetched"
- "octagon: have a trusted peer ID without peer information: %!@(MISSING)"
- "peers"
- "policyFreshness"
- "primaryAuthKitAccount"
- "rpcFetchDeviceNamesByPeerID:"
- "rpcFetchPeerAttributes:includeSelf:reply:"
- "rpcFetchPeerIDByBottleID:"
- "rtcAnalyticsReporter"
- "sendEvent:"
- "setAreTestsEnabled:"
- "setCanSendMetrics:"
- "setEvent:"
- "setIsAAAFoundationAvailable:"
- "setIsAuthKitAvailable:"
- "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
- "softlink:o:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
- "telemetryDeviceSessionIDForAccount:"
- "totalCKRecords"
- "totalRemoteKeys"
- "v16@?0@\"NSString\"8"
- "v32@?0@\"CKRecord\"8Q16^B24"
- "v32@?0@\"CuttlefishCurrentItem\"8Q16^B24"
- "v32@?0@\"CuttlefishPCSIdentity\"8Q16^B24"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "v36@0:8@16B24@28"
- "void *AAAFoundationLibrary(void)"
- "void *AuthKitLibrary(void)"

```
