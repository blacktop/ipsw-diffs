## KeychainSyncAccountNotification

> `/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification`

```diff

-61040.42.1.0.0
-  __TEXT.__text: 0xedc
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xb9
-  __TEXT.__oslogstring: 0x377
-  __TEXT.__unwind_info: 0x58
-  __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x3d2
-  __TEXT.__objc_methtype: 0x1f3
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x58
-  __DATA_CONST.__objc_classlist: 0x8
+61040.62.1.0.0
+  __TEXT.__text: 0x2004
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_methlist: 0x138
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x1c
+  __TEXT.__oslogstring: 0x3eb
+  __TEXT.__dlopen_cstrs: 0xfc
+  __TEXT.__cstring: 0xe3e
+  __TEXT.__unwind_info: 0xbc
+  __TEXT.__objc_classname: 0x80
+  __TEXT.__objc_methname: 0x7ea
+  __TEXT.__objc_methtype: 0x2a0
+  __TEXT.__objc_stubs: 0x560
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4a0
-  __DATA_CONST.__objc_selrefs: 0xb0
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x110
-  __DATA.__objc_classrefs: 0x20
+  __DATA_CONST.__objc_const: 0x5e8
+  __DATA_CONST.__objc_selrefs: 0x1a0
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__objc_const: 0x120
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_classrefs: 0x40
+  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_ivar: 0x14
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5
-  Symbols:   51
-  CStrings:  108
+  Functions: 38
+  Symbols:   186
+  CStrings:  276
 
Symbols:
+ _OBJC_CLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_SecurityAnalyticsReporterRTC
+ _OBJC_METACLASS_$_AAFAnalyticsEventSecurity
+ _OBJC_METACLASS_$_SecurityAnalyticsReporterRTC
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ __Unwind_Resume
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ ___objc_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _dispatch_async
+ _dispatch_once
+ _dispatch_sync
+ _free
+ _kSecurityRTCClientBundleIdentifier
+ _kSecurityRTCClientName
+ _kSecurityRTCClientNameDNU
+ _kSecurityRTCClientType
+ _kSecurityRTCEventCategoryAccountDataAccessRecovery
+ _kSecurityRTCEventNameAcceptorCreatesPacket2
+ _kSecurityRTCEventNameAcceptorCreatesPacket4
+ _kSecurityRTCEventNameAcceptorCreatesPacket5
+ _kSecurityRTCEventNameAcceptorCreatesVoucher
+ _kSecurityRTCEventNameAcceptorFetchesInitialSyncData
+ _kSecurityRTCEventNameCKAccountLogin
+ _kSecurityRTCEventNameCKKSTlkFetch
+ _kSecurityRTCEventNameCloudKitAccountAvailability
+ _kSecurityRTCEventNameContentSyncFinish
+ _kSecurityRTCEventNameCreateMissingTLKShares
+ _kSecurityRTCEventNameCreateSOSCircleBlob
+ _kSecurityRTCEventNameCreatesSOSApplication
+ _kSecurityRTCEventNameDeviceLocked
+ _kSecurityRTCEventNameDeviceUnlocked
+ _kSecurityRTCEventNameFetchAndPersistChanges
+ _kSecurityRTCEventNameFetchMachineID
+ _kSecurityRTCEventNameFetchPolicyDocument
+ _kSecurityRTCEventNameFirstManateeKeyFetch
+ _kSecurityRTCEventNameFixMismatchedViewItems
+ _kSecurityRTCEventNameFlush
+ _kSecurityRTCEventNameHealBrokenRecords
+ _kSecurityRTCEventNameHealKeyHierarchy
+ _kSecurityRTCEventNameHealTLKShares
+ _kSecurityRTCEventNameIdMSSecurityLevel
+ _kSecurityRTCEventNameInitiatorCreatesPacket1
+ _kSecurityRTCEventNameInitiatorCreatesPacket3
+ _kSecurityRTCEventNameInitiatorImportsInitialSyncData
+ _kSecurityRTCEventNameInitiatorJoinsSOS
+ _kSecurityRTCEventNameInitiatorJoinsTrustSystems
+ _kSecurityRTCEventNameInitiatorWaitsForUpgrade
+ _kSecurityRTCEventNameJoin
+ _kSecurityRTCEventNameKVSSyncAndWait
+ _kSecurityRTCEventNameLaunchStart
+ _kSecurityRTCEventNameLoadAndProcessIQEs
+ _kSecurityRTCEventNameLocalReset
+ _kSecurityRTCEventNameLocalSyncFinish
+ _kSecurityRTCEventNameNumberOfTrustedOctagonPeers
+ _kSecurityRTCEventNameOnboardMissingItems
+ _kSecurityRTCEventNamePreApprovedJoin
+ _kSecurityRTCEventNamePrepareIdentityInTPH
+ _kSecurityRTCEventNamePrimaryAccountAdded
+ _kSecurityRTCEventNameProcessIncomingQueue
+ _kSecurityRTCEventNameProcessOutgoingQueue
+ _kSecurityRTCEventNameProcessReceivedKeys
+ _kSecurityRTCEventNameQuerySyncableItems
+ _kSecurityRTCEventNameSaveCKMirrorEntries
+ _kSecurityRTCEventNameScanLocalItems
+ _kSecurityRTCEventNameSyncingPolicySet
+ _kSecurityRTCEventNameTrustGain
+ _kSecurityRTCEventNameTrustLoss
+ _kSecurityRTCEventNameTrustedDeviceListRefresh
+ _kSecurityRTCEventNameUpdateTDL
+ _kSecurityRTCEventNameUpdateTrust
+ _kSecurityRTCEventNameUploadHealedTLKShares
+ _kSecurityRTCEventNameUploadMissingTLKShares
+ _kSecurityRTCEventNameUploadOQEsToCK
+ _kSecurityRTCEventNameValidatedStashedAccountCredential
+ _kSecurityRTCEventNameVerifySOSApplication
+ _kSecurityRTCEventNameZoneChangeFetch
+ _kSecurityRTCEventNameZoneCreation
+ _kSecurityRTCFieldAccountAvailability
+ _kSecurityRTCFieldDidSucceed
+ _kSecurityRTCFieldErrorItemsProcessed
+ _kSecurityRTCFieldEventName
+ _kSecurityRTCFieldFetchReasons
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
+ _kSecurityRTCFieldNumCKRecords
+ _kSecurityRTCFieldNumKeychainItems
+ _kSecurityRTCFieldNumLocalRecords
+ _kSecurityRTCFieldNumMismatchedItems
+ _kSecurityRTCFieldNumRemoteKeys
+ _kSecurityRTCFieldNumViews
+ _kSecurityRTCFieldNumViewsWithNewEntries
+ _kSecurityRTCFieldNumberOfBluetoothMigrationItemsFetched
+ _kSecurityRTCFieldNumberOfKeychainItemsAdded
+ _kSecurityRTCFieldNumberOfKeychainItemsCollected
+ _kSecurityRTCFieldNumberOfPCSItemsFetched
+ _kSecurityRTCFieldNumberOfTLKsFetched
+ _kSecurityRTCFieldNumberOfTrustedPeers
+ _kSecurityRTCFieldOctagonSignInResult
+ _kSecurityRTCFieldPartialFailure
+ _kSecurityRTCFieldPendingClassA
+ _kSecurityRTCFieldPolicyFreshness
+ _kSecurityRTCFieldRetryAttemptCount
+ _kSecurityRTCFieldSecurityLevel
+ _kSecurityRTCFieldSuccessfulItemsProcessed
+ _kSecurityRTCFieldSupportedTrustSystem
+ _kSecurityRTCFieldSyncingPolicy
+ _kSecurityRTCFieldTotalRetryDuration
+ _kSecurityRTCFieldTrustStatus
+ _objc_enumerationMutation
+ _objc_getClass
+ _objc_getProperty
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x27
+ _objc_setProperty_atomic
+ _objc_storeStrong
- _objc_retain_x22
- _objc_retain_x26
CStrings:
+ "\x12"
+ "%s"
+ ".cxx_destruct"
+ "@\"AAFAnalyticsEvent\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@48@0:8@16@24@32@40"
+ "@52@0:8@16@24@32B40@44"
+ "@68@0:8@16@24@32@40@48B56@60"
+ "AAFAnalyticsEventSecurity"
+ "AAFAnalyticsReporter"
+ "AAFAnalyticsTransportRTC"
+ "B"
+ "SecurityAnalyticsReporterRTC"
+ "T@\"AAFAnalyticsEvent\",&,V_event"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "TB,V_areTestsEnabled"
+ "TB,V_isAAAFoundationAvailable"
+ "TB,V_isAuthKitAvailable"
+ "Unable to find class %s"
+ "_areTestsEnabled"
+ "_event"
+ "_isAAAFoundationAvailable"
+ "_isAuthKitAvailable"
+ "_queue"
+ "aafanalyticsevent-security: failed to softlink AAAFoundation"
+ "aafanalyticsevent-security: failed to softlink AuthKit"
+ "accountAvailability"
+ "addMetrics:"
+ "allKeys"
+ "analyticsReporterWithTransport:"
+ "analyticsTransportRTCWithClientType:clientBundleId:clientName:"
+ "areTestsEnabled"
+ "com.apple.aaa"
+ "com.apple.aaa.dnu"
+ "com.apple.security.acceptorCreatesPacket2"
+ "com.apple.security.acceptorCreatesPacket4"
+ "com.apple.security.acceptorCreatesPacket5"
+ "com.apple.security.acceptorCreatesVoucher"
+ "com.apple.security.acceptorFetchesInitialSyncData"
+ "com.apple.security.cKKSTLKFetch"
+ "com.apple.security.ckks.CKAccountLogin"
+ "com.apple.security.ckks.contentSyncFinish"
+ "com.apple.security.ckks.deviceLocked"
+ "com.apple.security.ckks.deviceUnlocked"
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
+ "com.apple.security.fetchAndPersistChanges"
+ "com.apple.security.fetchMachineID"
+ "com.apple.security.fetchPolicyDocument"
+ "com.apple.security.flush"
+ "com.apple.security.idMSSecurityLevel"
+ "com.apple.security.initiatorCreatesPacket1"
+ "com.apple.security.initiatorCreatesPacket3"
+ "com.apple.security.initiatorImportsInitialSyncData"
+ "com.apple.security.initiatorJoinSOS"
+ "com.apple.security.initiatorJoinsTrustSystems"
+ "com.apple.security.initiatorWaitsForUpgrade"
+ "com.apple.security.joinWithVoucher"
+ "com.apple.security.kVSSyncAndWait"
+ "com.apple.security.numberOfTrustedOctagonPeers"
+ "com.apple.security.preApprovedJoin"
+ "com.apple.security.prepareIdentityInTPH"
+ "com.apple.security.primaryAccountAdded"
+ "com.apple.security.trustedDeviceListRefresh"
+ "com.apple.security.updateTDL"
+ "com.apple.security.updateTrust"
+ "com.apple.security.validatedStashedAccountCredential"
+ "com.apple.security.verifySOSApplication"
+ "com.apple.securityd"
+ "countByEnumeratingWithState:objects:count:"
+ "dictionaryWithObjects:forKeys:count:"
+ "didSucceed"
+ "errorItemsProcessed"
+ "event"
+ "eventName"
+ "fetchReasons"
+ "fullFetch"
+ "fullRefetchNeeded"
+ "getEvent"
+ "i"
+ "init"
+ "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:"
+ "initWithKeychainCircleMetrics:altDSID:eventName:category:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:"
+ "isAAAFoundationAvailable"
+ "isAuthKitAvailable"
+ "isFullUpload"
+ "isLocked"
+ "isPrioritized"
+ "itemsScanned"
+ "itemsToAdd"
+ "itemsToDelete"
+ "itemsToModify"
+ "missingKey"
+ "needsReencryption"
+ "newItemsScanned"
+ "newTLKShares"
+ "numCKRecords"
+ "numKeychainItems"
+ "numLocalRecords"
+ "numMismatchedItems"
+ "numRemoteKeys"
+ "numViews"
+ "numViewsWithNewEntries"
+ "numberOfBluetoothMigrationItemsFetched"
+ "numberOfKeychainItemsAdded"
+ "numberOfKeychainItemsCollected"
+ "numberOfPCSItemsFetched"
+ "numberOfTLKsFetched"
+ "numberOfTrustedPeers"
+ "numberWithBool:"
+ "numberWithUnsignedInteger:"
+ "objectForKeyedSubscript:"
+ "octagonSignInResult"
+ "partialFailure"
+ "pendingClassAEntries"
+ "policyFreshness"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "queue"
+ "retryAttemptCount"
+ "rtcAnalyticsReporter"
+ "securityLevel"
+ "sendEvent:"
+ "sendMetricWithEvent:success:error:"
+ "setAreTestsEnabled:"
+ "setEvent:"
+ "setIsAAAFoundationAvailable:"
+ "setIsAuthKitAvailable:"
+ "setObject:forKeyedSubscript:"
+ "setQueue:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
+ "successfulItemsProcessed"
+ "supportedTrustSystem"
+ "syncingPolicy"
+ "totalRetryDuration"
+ "trustStatus"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@16"
+ "v36@0:8@16B24@28"
+ "v8@?0"

```
