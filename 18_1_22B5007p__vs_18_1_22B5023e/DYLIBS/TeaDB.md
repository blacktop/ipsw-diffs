## TeaDB

> `/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB`

```diff

-1048.0.0.0.0
-  __TEXT.__text: 0x44138
+1056.0.0.0.0
+  __TEXT.__text: 0x440ac
   __TEXT.__auth_stubs: 0x1510
-  __TEXT.__const: 0x2cdc
+  __TEXT.__const: 0x2ccc
   __TEXT.__cstring: 0xf59
   __TEXT.__swift5_typeref: 0x929
   __TEXT.__swift5_capture: 0x47c

   __TEXT.__swift5_types: 0x134
   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__oslogstring: 0x1e9
-  __TEXT.__unwind_info: 0x1878
+  __TEXT.__unwind_info: 0x1880
   __TEXT.__eh_frame: 0x2a14
   __TEXT.__objc_classname: 0x57
   __TEXT.__objc_methname: 0x1e7
   __TEXT.__objc_methtype: 0xad
   __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_ptr: 0x460
   __AUTH_CONST.__const: 0x34c8
   __AUTH_CONST.__objc_const: 0xcd8
-  __AUTH.__data: 0x28
-  __DATA.__data: 0x9d8
+  __DATA.__data: 0x948
   __DATA.__bss: 0x2f00
-  __DATA_DIRTY.__data: 0x1700
+  __DATA_DIRTY.__data: 0x17f0
   __DATA_DIRTY.__bss: 0x1600
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2275
-  Symbols:   513
-  CStrings:  171
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2273
+  Symbols:   520
+  CStrings:  124
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Context"
+ "DatesAreInDateInterval:ascending:error:usingBlock:"
+ "ctivityTypeObjectField:activityTypeField:confidenceField:allNameField:allDateField:allStartLocationField:allEndLocationField:allActivityTypeObjectField:allActivityTypeField:allConfidenceField:"
+ "enumerateEntriesForActivityEventsWhoseStartDatesAreIn:ascending:error:block:"
+ "enumerateEntriesForActivityEventsWhoseStartDatesAreInDateInterval:ascending:error:usingBlock:"
+ "enumerateEntriesForActivityEventsWithAscending:error:block:"
+ "enumerateEntriesForFutureActivityEventsInAscendingOrder:error:usingBlock:"
+ "enumerateEntriesForFutureActivityEventsWithAscending:error:block:"
+ "enumerateEntriesForSongEventsThatOverlapWith:ascending:error:block:"
+ "enumerateEntriesForSongEventsThatOverlapWithDateInterval:ascending:error:usingBlock:"
+ "enumerateEntriesForSongEventsWhoseEndDatesAreIn:ascending:error:block:"
+ "enumerateEntriesForSongEventsWhoseEndDatesAreInDateInterval:ascending:error:usingBlock:"
+ "enumerateEntriesForSongEventsWhoseStartDatesAreIn:ascending:error:block:"
+ "enumerateEntriesForSongEventsWhoseStartDatesAreInDateInterval:ascending:error:usingBlock:"
+ "enumerateEntriesForSongEventsWithAscending:error:block:"
+ "enumerateFutureActivityEventsWithAscending:error:block:"
+ "enumerateIdentifiersWithBlock:"
+ "enumerateIdentifiersWithQuery:block:"
+ "enumerateObjectsWithQuery:block:"
+ "enumeratePeopleMatchingName:block:"
+ "enumeratePeopleWithBlock:"
+ "enumerateSongEventsInAscendingOrder:error:usingBlock:"
+ "enumerateSongEventsThatOverlapWith:ascending:error:block:"
+ "enumerateSongEventsThatOverlapWithDateInterval:ascending:error:usingBlock:"
+ "enumerateSongEventsWhoseEndDatesAreIn:ascending:error:block:"
+ "enumerateSongEventsWhoseEndDatesAreInDateInterval:ascending:error:usingBlock:"
+ "enumerateSongEventsWhoseStartDatesAreIn:ascending:error:block:"
+ "enumerateSongEventsWhoseStartDatesAreInDateInterval:ascending:error:usingBlock:"
+ "enumerateSongEventsWithAscending:error:block:"
+ "enumerateTopicsWithBlock:"
+ "enumerateTriples:"
+ "er"
+ "eventParticipationType"
+ "eventTypes"
+ "execSteps"
+ "executeIntent:completionHandler:"
+ "executeIntent:completionHandlerWithGraphObjectContext:"
+ "executeIntent:error:"
+ "executeIntent:withCompletion:"
+ "executeIntentsWithGraphObjectContextWithRequest:"
+ "executeIntentsWithRequest:"
+ "executeKGQ:completionHandler:"
+ "executeKGQ:completionHandlerWithGraphObjectContext:"
+ "executeKGQ:error:"
+ "executeKGQ:withCompletion:"
+ "executeKGQWithGraphObjectContextWithRequest:"
+ "executeKGQWithRequest:"
+ "expectedDurationInSecondsNoTraffic"
+ "expectedFeatureKeysWithError:"
+ "extremeActivityEventWithEntityIdentifierType:ascending:outStartDate:outEndDate:error:"
+ "extremeFutureActivityEventWithEntityIdentifierType:ascending:outStartDate:outEndDate:error:"
+ "faceprintRevision"
+ "facetimePopularityGivenCoarseGeoHash"
+ "facetimePopularityGivenCoarseTimeOfDay"
+ "facetimePopularityGivenDayOfWeek"
+ "facetimePopularityGivenFocusMode"
+ "facetimePopularityGivenLOI"
+ "facetimePopularityGivenLargeGeoHash"
+ "facetimePopularityGivenMicroLocation"
+ "facetimePopularityGivenMotionState"
+ "facetimePopularityGivenSpecificGeoHash"
+ "facetimePopularityGivenTimeOfDay"
+ "facetimePopularityGivenWiFi"
+ "facetimeWithEntityGivenCoarseGeoHash"
+ "facetimeWithEntityGivenCoarseTimeOfDay"
+ "facetimeWithEntityGivenDayOfWeek"
+ "facetimeWithEntityGivenFocusMode"
+ "facetimeWithEntityGivenLOI"
+ "facetimeWithEntityGivenLargeGeoHash"
+ "facetimeWithEntityGivenMicroLocation"
+ "facetimeWithEntityGivenMotionState"
+ "facetimeWithEntityGivenSpecificGeoHash"
+ "facetimeWithEntityGivenTimeOfDay"
+ "facetimeWithEntityGivenWiFi"
+ "factId"
+ "featureForKey:error:"
+ "featureKeys:"
+ "featureKeysWithError:"
+ "featureViewWithAccessAssertion:database:error:"
+ "featureViewWithError:"
+ "fieldsTokens"
+ "firstPartyLongTermTopicViewAndReturnError:"
+ "firstPartyLongTermTopicViewWithAccessAssertion:database:error:"
+ "firstPartyLongTermTopicViewWithError:"
+ "firstPartyMsgSixMonths"
+ "firstPartyMsgThreeMonths"
+ "firstPartyShortTermTopicViewAndReturnError:"
+ "firstPartyShortTermTopicViewWithError:"
+ "focusModeGivenCallWithEntity"
+ "focusModeGivenFacetimeWithEntity"
+ "ftsTokenize:"
+ "fullNames"
+ "gdFeatureViewAndReturnError:"
+ "gdSwiftContext"
+ "gdSwiftSubgraphViewContextWithName:tableName:error:"
+ "gdTag"
+ "gdTagTypeWithName:"
+ "generateActivityCentricLifeEventsFromStartDate:toEndDate:completion:"
+ "pe:sourceIdentifier:completion:"
+ "softwareId"
+ "softwareLinks"
+ "songId"
+ "sourceDuplicates"
+ "sourceIDs"
+ "sourceUpdatedWithSourceType:sourceIdentifier:error:"
+ "specificGeoHashGivenCallWithEntity"
+ "specificGeoHashGivenFacetimeWithEntity"
+ "specificGeoHashGivenMessageWithEntity"
+ "statsWithCompletion:"
+ "statusWithError:"
+ "stopPipelineWithCompletion:"
+ "stopPipelineWithError:"
+ "streamUpdatedWithStreamName:isDelete:completion:"
+ "streamUpdatedWithStreamName:isDelete:error:"
+ "streamsChangedWithUpdated:deletes:completion:"
+ "streamsChangedWithUpdated:deletes:error:"
+ "subentity"
+ "subgraphViewContextWithViewName:tableName:error:"
+ "subidentifierName"
+ "subjectAlias"
+ "subjectId"
+ "subjectIsa"
+ "subjectPopularity"
+ "subjects"
- "\",R,C,N,V_ecdsaCertificate"
- "DEREncodeData:singleByteTag:"
- "DERParseSEFWSequence:info:"
- "T@\"<ORProvisionDelegate>\",W,V_delegate"
- "T@\"<SPRReadDelegate>\",R,V_base"
- "T@\"NSArray\",R,C,N,V_kernelsInstalled"
- "T@\"NSArray\",R,C,N,V_vasResponses"
- "T@\"NSData\",C,V_details"
- "T@\"NSData\",R,C,N,V_cardHolderData"
- "T@\"NSData\",R,C,N,V_cvmResult"
- "T@\"NSData\",R,C,N,V_interfaceDeviceSerial"
- "T@\"NSData\",R,C,N,V_merchantCategoryCode"
- "T@\"NSData\",R,N,V_confirmationBlobHash"
- "T@\"NSMutableArray\",&,N,V_delayWork"
- "T@\"NSObject<NFSession>\",&,N,V_initiatingSession"
- "T@\"NSObject<STSXPCClientNotificationListenerDelegate>\",R,W,N,V_delegate"
- "T@\"NSString\",&,N,V_publicTransactionHash"
- "T@\"NSString\",&,N,V_readerIdentifier"
- "T@\"NSString\",&,N,V_readerMerchantId"
- "T@\"NSString\",R,C,N,V_configId"
- "T@\"NSString\",R,C,N,V_transactionId"
- "T@\"NSString\",R,N,V_organizationUnit"
- "T@\"NSString\",R,N,V_secondaryIdentifier"
- "T@\"NSString\",R,N,V_secondarySubIdentifier"
- "T@\"NSString\",R,N,V_signupUrl"
- "T@\"NSString\",R,N,V_subIdentifier"
- "T@\"NSXPCListener\",&,N,V_xpc"
- "T@\"ORReader\",&,V_reader"
- "T@\"SPAssetCacheClientCache\",&,N,V_transientCache"
- "T@\"SPProtoAudioFilePlayerAsset\",&,N,V_asset"
- "T@\"SPProtoAudioFilePlayerItem\",&,N,V_playerItem"
- "T@\"SPProtoAudioFilePlayerMessage\",&,N,V_audioFilePlayerMessage"
- "T@\"SPProtoAudioFilePlayerUpdateContainedIdentifier\",&,N,V_appendItem"
- "T@\"SPProtoAudioFilePlayerUpdateContainedIdentifier\",&,N,V_replaceCurrentItem"
- "T@\"STS18013ReaderAnalyticsData\",R,N,V_readerAnalyticsData"
- "T@\"STSAuxiliaryCredential\",R,N,V_credential"
- "T@\"STSCASessionStats\",&,N,V_caSessionStats"
- "T@\"STSCredential\",&,N,V_credential"
- "T@\"STSCredential\",R,N,V_activeSTSCredential"
- "T@\"STSHandler\",&,N,V_handler"
- "T@\"STSHardwareManagerWrapper\",&,N,V_nfHwManager"
- "T@\"STSHelperLibrary\",&,N,V_stsHelper"
- "T@\"STSMerchantPaymentRequest\",&,N,V_topUpRequest"
- "T@\"STSPeerPaymentTransferRequest\",&,N,V_transferRequest"
- "T@\"STSSession\",R,W,N,V_parent"
- "T@\"STSSigningSession\",R,W,N,V_parent"
- "T@\"STSTimer\",&,N,V_responseTimeout"
- "T@\"STSXPCClientNotificationListener\",&,N,V_stsNotificationListener"
- "T@?,C,N,V_sessionStartCompletion"
- "T@?,C,N,V_theStartCallback"
- "T@?,C,N,V_tnepStatusHandler"
- "TB,N,V_alternativeCarrierConnected"
- "TB,N,V_monotonic"
- "TB,N,V_queuePaused"
- "TB,N,V_readerAuthenticated"
- "TB,N,V_resolvedHwManagerState"
- "TI,R,V_nfcTechnology"
- "TQ,N,V_engagementConfiguration"
- "TQ,N,V_popTimeInSeconds"
- "TQ,R,N,V_dataRetrievalType"
- "TQ,R,N,V_deviceEngagementType"
- "TQ,R,V_ecpVersion"
- "TQ,R,V_fieldType"
- "TS,N,V_retention"
- "TS,N,V_transactionMode"
- "TS,R,V_systemCode"
- "Tq,N,V_merchantCapabilities"
- "Tq,N,V_totalSuccessfulTransactionsInSession"
- "Tq,N,V_totalTransactionsInSession"
- "Tq,N,V_transmissionState"
- "Tq,R,N,V_provisionReadTimeout"
- "Tq,R,N,V_terminalMode"
- "T{?=b8b4b1b1b18[8S]},R,N,V_amount"
- "T{os_unfair_lock_s=I},N,V_xpcUpdateLock"
- "_activateInvalidationHandler:"
- "_activateOnConnectCompletion"
- "_activateSendRequestCompletion:sessionTerminationRequested:error:"
- "_activateSendRequestCompletion:terminationRequested:error:"
- "_activateSessionStartCompletion:"
- "_activateTnepStatusHandler:"
- "_activeCredential"
- "_activeSTSCredential"
- "_activeSTSCredentials"
- "_alternativeCarrierConnected"
- "_asynchronousRemoteProxyWithErrorHandler:"
- "_cardHolderData"
- "_configId"
- "_controlSessionSem"
- "_controlSessionSuspended"
- "_createHandlerForMerchantPaymentSign"
- "_createHandlerForPeerPaymentSign"
- "_dataRetrievalType"
- "_delayWork"
- "_deviceEngagementType"
- "_ecpVersion"
- "_engagementConfiguration"
- "_executeWhenXPCAvailable:"
- "_generateFromCredRequest:"
- "_handoverSession"
- "_handoverSessionMutex"
- "_hasStartedWithDelegate"
- "_initiatingSession"
- "_lastField"
- "_masterSESession"
- "_mobileToken"
- "_nearFieldFdSession"
- "_nfECommerceSession"
- "_nfHwManager"
- "_nfPeerPaymentSession"
- "_nfcTechnology"
- "_notificationTesterDelegate"
- "_postReaderSessionEvent:"
- "_postReaderTransactionEvent:prepOnly:"
- "_provisionDataBlob"
- "_provisionReadTimeout"
- "_proxyReaderSESession"
- "_queuePaused"
- "_readerAnalyticsData"
- "_readerAuthenticated"
- "_readerMerchantId"
- "_releasedCredential"
- "_requestByNamespace"
- "_resolvedHwManagerState"
- "_retention"
- "_seProxyCleanup:"
- "_seSession"
- "_secondarySubIdentifier"
- "_sepCerts"
- "_sessionStartCompletion"
- "_sessionTranscriptBytes"
- "_sessionUpdateLock"
- "_start18013TransactionWithToken:"
- "_startHandoverSession"
- "_startTransactionOption"
- "_startedNFSession"
- "_stsHandoverNotificationListenerCallbackProtocol"
- "_stsHandoverNotificationListenerProtocol"
- "_stsHelper"
- "_stsNotificationListener"
- "_subIdentifier"
- "_supportedPNOs"
- "_synchronousRemoteProxyWithErrorHandler:"
- "_tcis"
- "_tearDownOnQueue:completion:"
- "_theStartCallback"
- "_timeoutReadVas"
- "_tnepStatusHandler"
- "_totalSuccessfulTransactionsInSession"
- "_totalTransactionsInSession"
- "_transactionMode"
- "_translateFromCarrierConnectionStatus:"
- "_translateNfcdXPCHelperError:"
- "_translateSTSXPCHelperError:"
- "_translateXPCClientNotificationStatus:"
- "ableNumber"
- "boolStringValue"
- "capturePINWithParameters:error:"
- "criptSequence:info:"
- "cvmType"
- "generatePINBlockAndReturnError:"
- "initWithMode:vasPasses:urls:amount:currencyCode:transactionType:merchantCategoryCode:kernelToken:timeoutReadPay:timeoutReadVas:"
- "lock:"
- "makeConfiguratorAndReturnError:"
- "ontrollers:"
- "setAlternativeCarrierConnected:"
- "setMobileToken:"
- "setODARequired:"
- "setRequestHandoverConfirmation:"
- "startRemoteInterfaceWithBundle:"
- "terminateSockPuppetAppForCompanionAppWithIdentifier:completion:"
- "waitForControlSessionToBeReady:"

```
