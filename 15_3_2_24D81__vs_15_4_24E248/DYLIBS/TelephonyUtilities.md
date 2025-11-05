## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities`

```diff

-1525.400.141.0.0
-  __TEXT.__text: 0x13f93c
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x14100
-  __TEXT.__cstring: 0xf140
+1525.500.181.0.0
+  __TEXT.__text: 0x13ecf8
+  __TEXT.__auth_stubs: 0x1180
+  __TEXT.__objc_methlist: 0x175e0
+  __TEXT.__cstring: 0xeec3
   __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0xeb26
-  __TEXT.__gcc_except_tab: 0x12d4
+  __TEXT.__oslogstring: 0xea26
+  __TEXT.__gcc_except_tab: 0x12a4
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x504
   __TEXT.__swift5_typeref: 0x59

   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x48c0
-  __TEXT.__objc_classname: 0x2402
-  __TEXT.__objc_methname: 0x35de6
-  __TEXT.__objc_methtype: 0x790b
-  __TEXT.__objc_stubs: 0x1d760
-  __DATA_CONST.__got: 0xa80
-  __DATA_CONST.__const: 0x15c0
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __TEXT.__unwind_info: 0x4988
+  __TEXT.__objc_classname: 0x23a4
+  __TEXT.__objc_methname: 0x35f72
+  __TEXT.__objc_methtype: 0x78a9
+  __TEXT.__objc_stubs: 0x1d820
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x3e8
+  __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9bd8
-  __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_arraydata: 0x3b8
-  __AUTH_CONST.__auth_got: 0x8f0
-  __AUTH_CONST.__const: 0x3a90
+  __DATA_CONST.__objc_selrefs: 0x9d60
+  __DATA_CONST.__objc_protorefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x5e8
+  __DATA_CONST.__objc_arraydata: 0x3f8
+  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH_CONST.__const: 0x3a00
   __AUTH_CONST.__cfstring: 0xfa20
-  __AUTH_CONST.__objc_const: 0x298a8
+  __AUTH_CONST.__objc_const: 0x233d0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x2210
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x156c
-  __DATA.__data: 0x2ec0
-  __DATA.__bss: 0x680
+  __DATA.__objc_ivar: 0x1570
+  __DATA.__data: 0x2e00
+  __DATA.__bss: 0x670
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0x2350
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__objc_data: 0x2300
+  __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/CallKit.framework/Versions/A/CallKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2125383F-6073-31FA-B645-34053C415620
-  Functions: 8213
-  Symbols:   17785
-  CStrings:  14395
+  UUID: DC732295-37A2-344E-86BD-9824AA67DFDB
+  Functions: 8308
+  Symbols:   17871
+  CStrings:  14390
 
Symbols:
+ +[CNContact(TUSearchUtilities) keysToFetchForFaceTime].cold.1
+ +[FTCaptionsMachine machTimeScale].cold.1
+ +[NSURL(FaceTime_PinExchange) _faceTimePinExchangeURLWithParameters:].cold.1
+ +[NSURL(TUSanitizedCopying) tu_defaultAllowedSchemes].cold.1
+ +[NSURL(Telephony) TUDialRequestSchemeDefaultAppPrompt]
+ +[NSURL(Telephony) TUDialRequestSchemeDefaultApp]
+ +[NSURL(Telephony) TUDialRequestSchemeForceTelephonyPrompt]
+ +[NSURL(Telephony) TUDialRequestSchemeForceTelephony]
+ +[NSURL(Telephony) isDefaultAppScheme:]
+ +[NSURL(Telephony) isDefaultCallingAppScheme:]
+ +[NSURL(Telephony) isForceTelephonyScheme:]
+ +[NSUserDefaults(TelephonyUtilities) sb_defaults].cold.1
+ +[NSUserDefaults(TelephonyUtilities) tu_defaults].cold.1
+ +[NSXPCConnection(TUCallServicesAdditions) callServicesClientXPCInterface].cold.1
+ +[NSXPCConnection(TUCallServicesAdditions) callServicesServerXPCInterface].cold.1
+ +[NSXPCInterface(TUUIXPCClientSupport) clientInterface].cold.1
+ +[NSXPCInterface(TUUIXPCClientSupport) hostInterface].cold.1
+ +[TUAudioSystemController sharedAudioSystemController].cold.1
+ +[TUCallCapabilities client].cold.1
+ +[TUCallCapabilitiesXPCClient callCapabilitiesClientXPCInterface].cold.1
+ +[TUCallCapabilitiesXPCClient callCapabilitiesServerXPCInterface].cold.1
+ +[TUCallCenter sharedContactStore].cold.1
+ +[TUCallHistoryController sharedController].cold.1
+ +[TUCallHistoryControllerXPCClient callHistoryControllerClientXPCInterface].cold.1
+ +[TUCallHistoryManagerXPCClient callHistoryManagerClientXPCInterface].cold.1
+ +[TUContactsDataProvider defaultContactKeyDescriptors].cold.1
+ +[TUContactsDataProvider familyNameFirstLocaleCountryCodes].cold.1
+ +[TUContactsDataProvider numberFormatter].cold.1
+ +[TUContactsDataProvider unsupportedLocalesForPrefixHint].cold.1
+ +[TUConversation mergedRemoteMemberHandlesFromRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:]
+ +[TUConversation mergedRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:]
+ +[TUConversation numberFormatter].cold.1
+ +[TUConversationActivityContext mediaContextIdentifiers].cold.1
+ +[TUConversationLink featureFlags].cold.1
+ +[TUConversationLink userConfiguration].cold.1
+ +[TUConversationLinkDescriptorXPCClientDataSource clientXPCInterface].cold.1
+ +[TUConversationLinkDescriptorXPCClientDataSource serverXPCInterface].cold.1
+ +[TUConversationManager allowsVideo].cold.1
+ +[TUConversationProvider expanseProvider].cold.1
+ +[TUConversationProvider faceTimeProvider].cold.1
+ +[TUConversationProvider unknownProvider].cold.1
+ +[TUCoreTelephonyClient(TTY) RTTSettingsClass].cold.1
+ +[TUCoreTelephonyClient(TTY) RTTTelephonyUtilitiesClass].cold.1
+ +[TUDialAssist sharedInstance].cold.1
+ +[TUDiscoverabilitySignal isSeniorUser].cold.1
+ +[TUMomentsController faceTimePhotosEnabledDeterminer].cold.1
+ +[TUMomentsController sharedInstance].cold.1
+ +[TUMomentsControllerXPCClient momentsControllerClientXPCInterface].cold.1
+ +[TUMomentsControllerXPCClient momentsControllerServerXPCInterface].cold.1
+ +[TUNeighborhoodActivityConduitXPCClient neighborhoodActivityClientXPCInterface].cold.1
+ +[TUNeighborhoodActivityConduitXPCClient neighborhoodActivityServerXPCInterface].cold.1
+ +[TUPrivacyManager sharedPrivacyManager].cold.1
+ +[TUSearchController sharedInstance].cold.1
+ +[TUSearchModuleManager recentsModuleClasses].cold.1
+ +[TUSearchModuleManager searchModuleClasses].cold.1
+ +[TUSimulatedConversationControllerXPCClient simulatedConversationControllerClientXPCInterface].cold.1
+ +[TUSuggestionsMetadataCacheDataProvider sharedService].cold.1
+ +[TUUserConfiguration registeredDefaults].cold.1
+ +[TUUserNotificationProviderXPCClient userNotificationProviderServerXPCInterface].cold.1
+ -[CNContactStore(TUSearchUtilities) contactForDestinationId:].cold.1
+ -[CNContactStore(TUSearchUtilities) contactForIdentifier:].cold.1
+ -[NSString(TelephonyUtilities) IDSFormattedDestinationID].cold.1
+ -[NSString(TelephonyUtilities) IDSFormattedDestinationID].cold.2
+ -[NSString(TelephonyUtilities) IDSFormattedDestinationID].cold.3
+ -[NSString(TelephonyUtilities) IDSFormattedDestinationID].cold.4
+ -[NSURL(Telephony) hasTelephonyOrDefaultAppScheme]
+ -[NSURL(Telephony) isDefaultCallingAppPromptURL]
+ -[NSURL(Telephony) isDefaultCallingAppURL]
+ -[NSURL(Telephony) isForceTelephonyPromptURL]
+ -[NSURL(Telephony) isForceTelephonyURL]
+ -[TUCall hasEverUnsuppressedRingtone]
+ -[TUCall remoteVideoContentRect].cold.1
+ -[TUCall setHasEverUnsuppressedRingtone:]
+ -[TUCallCenter disconnectCurrentCall]
+ -[TUCallCenter getCurrentCallsToDisconnect]
+ -[TUCallGroup initWithCall:].cold.1
+ -[TUCallGroup initWithCalls:].cold.1
+ -[TUCallNotificationManager deferNotificationsUntilAfterPerformingBlock:].cold.1
+ -[TUCallNotificationManager postNotificationsForCall:usingComparisonCall:afterUpdatesInBlock:].cold.1
+ -[TUCallProviderManagerXPCClient currentProcessCanAccessInitialState].cold.1
+ -[TUCallServicesInterface dialWithRequest:completion:].cold.1
+ -[TUCallServicesInterface disconnectCurrentCall]
+ -[TUContactsDataProvider processBatchFetchRequests:].cold.1
+ -[TUContactsDataProviderFetchRequest initWithCall:].cold.1
+ -[TUContactsDataProviderFetchRequest initWithHandle:].cold.1
+ -[TUContactsDataProviderFetchRequest initWithHandles:].cold.1
+ -[TUContactsDataProviderFetchRequest initWithHandles:isConversation:].cold.1
+ -[TUContinuityCallInfo initWithCallIdentifier:callerIdSubstring:displayName:isBranded:isEmergency:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:]
+ -[TUContinuityCallInfo isEmergency]
+ -[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:recentCallsInfos:callBlockedStates:]
+ -[TUConversationLink fetchedResults].cold.1
+ -[TUConversationLink initWithPseudonym:publicKey:groupUUID:originatorHandle:creationDate:deletionDate:expirationDate:invitedMemberHandles:locallyCreated:linkName:linkLifetimeScope:deleteReason:].cold.1
+ -[TUConversationLink initWithPseudonym:publicKey:groupUUID:originatorHandle:creationDate:deletionDate:expirationDate:invitedMemberHandles:locallyCreated:linkName:linkLifetimeScope:deleteReason:].cold.2
+ -[TUConversationManager currentProcessCanAccessCollaborations].cold.1
+ -[TUDialRequest initWithProvider:].cold.1
+ -[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:contactsDataSource:cacheOnly:].cold.2
+ -[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:contactsDataSource:cacheOnly:].cold.3
+ -[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:contactsDataSource:cacheOnly:].cold.4
+ -[TUDynamicCallDisplayContext initWithDisplayContext:call:serialQueue:cacheOnly:].cold.1
+ -[TUDynamicCallDisplayContext initWithDisplayContext:call:serialQueue:cacheOnly:].cold.2
+ -[TUDynamicCallDisplayContext initWithDisplayContext:call:serialQueue:cacheOnly:].cold.3
+ -[TUFeatureFlags automaticCallActivationDisabled]
+ -[TUFeatureFlags callConnectHapticsEnabled]
+ -[TUFeatureFlags continuityEmergencyMultiDeviceDiscoveryEnabled]
+ -[TUFeatureFlags mooseEnabled]
+ -[TUJoinConversationRequest localMemberAssociation]
+ -[TUJoinConversationRequest mergedRemoteMembers]
+ -[TUJoinConversationRequest setLocalMemberAssociation:]
+ -[TUMomentsController endRequestWithTransactionID:completion:].cold.1
+ -[TUMomentsController registerProvider:completion:].cold.1
+ -[TUMomentsController startRequestWithMediaType:forProvider:requesteeID:completion:].cold.1
+ -[TUMomentsController unregisterProvider:completion:].cold.1
+ -[TUNeighborhoodActivityConduit _osStateDictionary].cold.1
+ -[TUNeighborhoodActivityConduit addDelegate:].cold.1
+ -[TUNeighborhoodActivityConduit splitSessionUpdated]
+ -[TUNeighborhoodActivityConduitXPCClient splitSessionUpdated]
+ -[TUProxyCall localAspectRatioForOrientation:].cold.1
+ -[TUProxyRecentCall mostRecentCallWasMissed].cold.1
+ -[TUSenderIdentityCapabilities isThumperCallingAllowedOnDefaultPairedSecondaryDevice].cold.1
+ -[TUSenderIdentityCapabilities isThumperCallingAllowedOnSecondaryDeviceWithID:].cold.1
+ -[TUSenderIdentityCapabilities setThumperCallingAllowed:onSecondaryDeviceWithID:].cold.1
+ -[TUSenderIdentityCapabilities setThumperCallingAllowedOnDefaultPairedSecondaryDevice:].cold.1
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table170
+ GCC_except_table211
+ GCC_except_table236
+ GCC_except_table243
+ OBJC_IVAR_$_TUCall._hasEverUnsuppressedRingtone
+ OBJC_IVAR_$_TUContinuityCallInfo._isEmergency
+ OBJC_IVAR_$_TUJoinConversationRequest._localMemberAssociation
+ TUCTServerConnection.cold.1
+ TUConduitLog.cold.1
+ TUDefaultLog.cold.1
+ TUDispatchMainIfNecessaryAndWait.cold.1
+ TUGreenTeaLog.cold.1
+ TUISOCountryCodeForMCC.cold.2
+ TUIsEmergencyNumber.cold.2
+ TUIsEmergencyNumberOrIsWhiteListed.cold.2
+ TUIsStoreDemoModeEnabled.cold.1
+ TULockdownModeEnabled.cold.1
+ TUMapItemForPhoneNumberRefSync.cold.1
+ TUOversizedLog.cold.1
+ TUOversizedLogQueue.cold.1
+ TUPreferredFaceTimeBundleIdentifier.cold.1
+ TUThumperCarrierName.cold.2
+ _OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.407
+ _OBJC_$_PROP_LIST_TUFeatureFlags.413
+ _TUCTGASRAvailableLocales
+ _TUCallHapticsEnabled
+ _TUCallTranscriptionAvailability
+ __25-[TUDTMFSoundPlayer init]_block_invoke.cold.1
+ __28-[TUSoundPlayer stopPlaying]_block_invoke.cold.1
+ __32-[TUPrivacyManager privacyRules]_block_invoke.cold.1
+ __52-[TUNeighborhoodActivityConduit splitSessionUpdated]_block_invoke.cold.1
+ __65-[TUContactsAutocompleteSearchModule searchForString:completion:]_block_invoke.cold.1
+ __80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_2.cold.1
+ __80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_2.cold.2
+ __CUTWeakCGSizeZero.cold.1
+ __TUAddTelephonyCenterObserver_block_invoke.cold.1
+ __TUCTServerConnection_block_invoke.cold.1
+ __TURemoveEveryTelephonyCenterObserver_block_invoke.cold.1
+ __TURemoveTelephonyCenterObserver_block_invoke.cold.1
+ ___120+[TUConversation mergedRemoteMemberHandlesFromRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:]_block_invoke
+ ___37-[TUCallCenter disconnectCurrentCall]_block_invoke
+ ___52-[TUNeighborhoodActivityConduit splitSessionUpdated]_block_invoke
+ ___61-[TUNeighborhoodActivityConduitXPCClient splitSessionUpdated]_block_invoke
+ ___97+[TUConversation mergedRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:]_block_invoke
+ ___block_descriptor_40_e8_32s_e42_v24?0"TUNearbyDeviceHandle"8"NSError"16l
+ __block_literal_global.1660
+ __block_literal_global.1666
+ __block_literal_global.199
+ __block_literal_global.291
+ __swiftImmortalRefCount
+ _objc_msgSend$automaticCallActivationDisabled
+ _objc_msgSend$callConnectHapticsEnabled
+ _objc_msgSend$disconnectCurrentCall
+ _objc_msgSend$getCurrentCallsToDisconnect
+ _objc_msgSend$hasEverUnsuppressedRingtone
+ _objc_msgSend$hasTelephonyOrDefaultAppScheme
+ _objc_msgSend$initWithCallIdentifier:callerIdSubstring:displayName:isBranded:isEmergency:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:
+ _objc_msgSend$initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:recentCallsInfos:callBlockedStates:
+ _objc_msgSend$isDefaultCallingAppScheme:
+ _objc_msgSend$isForceTelephonyPromptURL
+ _objc_msgSend$localMemberAssociation
+ _objc_msgSend$mergedRemoteMemberHandlesFromRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:
+ _objc_msgSend$mergedRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:
+ _objc_msgSend$oneToOneFaceTimeMyselfEnabled
+ _objc_msgSend$setLocalMemberAssociation:
+ _objc_msgSend$splitSessionUpdated
+ legacySchemeIfEnabled.cold.1
- +[NSURL(FaceTime) TUDialRequestSchemeDefaultAppPrompt]
- +[NSURL(FaceTime) TUDialRequestSchemeDefaultApp]
- +[NSURL(FaceTime) TUDialRequestSchemeForceTelephonyPrompt]
- +[NSURL(FaceTime) TUDialRequestSchemeForceTelephony]
- +[NSURL(FaceTime) isDefaultAppScheme:]
- +[TUConversation mergedRemoteMemberHandlesFromRemoteMembers:withLocalMember:removingLocallyAssociatedMember:]
- +[TUConversation mergedRemoteMembers:withLocalMember:removingLocallyAssociatedMember:]
- +[TUDialRequest urlSchemeMatchesDefaultProvider:provider:]
- +[TUDiscoverabilitySignal logAnalyticsEventSpeakerphone]
- +[TUReportingControllerXPCClient asynchronousServer]
- +[TUReportingControllerXPCClient reportingControllerServerXPCInterface]
- +[TUReportingControllerXPCClient setAsynchronousServer:]
- +[TUReportingControllerXPCClient setSynchronousServer:]
- +[TUReportingControllerXPCClient synchronousServer]
- -[TUContinuityCallInfo initWithCallIdentifier:callerIdSubstring:displayName:isBranded:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:]
- -[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:recentCallsInfos:]
- -[TUNeighborhoodActivityConduitXPCClient splitSessionUpdated:]
- -[TUReportingControllerXPCClient .cxx_destruct]
- -[TUReportingControllerXPCClient dealloc]
- -[TUReportingControllerXPCClient didCleanUpForStream:reply:]
- -[TUReportingControllerXPCClient didReceiveResultsForStream:withTransactionID:reply:]
- -[TUReportingControllerXPCClient didStartRequestForStream:withTransactionID:reply:]
- -[TUReportingControllerXPCClient init]
- -[TUReportingControllerXPCClient queue]
- -[TUReportingControllerXPCClient registeredStream:withAvailability:reply:]
- -[TUReportingControllerXPCClient serverWithErrorHandler:]
- -[TUReportingControllerXPCClient setXpcConnection:]
- -[TUReportingControllerXPCClient synchronousServerWithErrorHandler:]
- -[TUReportingControllerXPCClient xpcConnection]
- GCC_except_table142
- GCC_except_table148
- GCC_except_table151
- GCC_except_table157
- GCC_except_table160
- GCC_except_table163
- GCC_except_table167
- GCC_except_table208
- GCC_except_table233
- GCC_except_table240
- OBJC_IVAR_$_TUReportingControllerXPCClient._queue
- OBJC_IVAR_$_TUReportingControllerXPCClient._xpcConnection
- _OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.395
- _OBJC_$_PROP_LIST_TUFeatureFlags.401
- _OBJC_CLASS_$_TUReportingControllerXPCClient
- _OBJC_METACLASS_$_TUReportingControllerXPCClient
- _OUTLINED_FUNCTION_5
- _TUAnalyticsEventSpeakerphone
- _TUTipsEventSpeakerProximity
- _TUTipsEventSpeakerUsed
- __47-[TUReportingControllerXPCClient xpcConnection]_block_invoke.15
- __47-[TUReportingControllerXPCClient xpcConnection]_block_invoke_2.16
- __60-[TUReportingControllerXPCClient didCleanUpForStream:reply:]_block_invoke_2.cold.1
- __74-[TUReportingControllerXPCClient registeredStream:withAvailability:reply:]_block_invoke_2.cold.1
- __83-[TUReportingControllerXPCClient didStartRequestForStream:withTransactionID:reply:]_block_invoke_2.cold.1
- __85-[TUReportingControllerXPCClient didReceiveResultsForStream:withTransactionID:reply:]_block_invoke_2.cold.1
- __OBJC_$_CLASS_METHODS_TUReportingControllerXPCClient
- __OBJC_$_CLASS_PROP_LIST_TUReportingControllerXPCClient
- __OBJC_$_INSTANCE_METHODS_TUReportingControllerXPCClient
- __OBJC_$_INSTANCE_VARIABLES_TUReportingControllerXPCClient
- __OBJC_$_PROP_LIST_TUReportingControllerXPCClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUReportingControllerDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUReportingControllerXPCServer
- __OBJC_$_PROTOCOL_METHOD_TYPES_TUReportingControllerDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_TUReportingControllerXPCServer
- __OBJC_$_PROTOCOL_REFS_TUReportingControllerDataSource
- __OBJC_$_PROTOCOL_REFS_TUReportingControllerXPCServer
- __OBJC_CLASS_PROTOCOLS_$_TUReportingControllerXPCClient
- __OBJC_CLASS_RO_$_TUReportingControllerXPCClient
- __OBJC_LABEL_PROTOCOL_$_TUReportingControllerDataSource
- __OBJC_LABEL_PROTOCOL_$_TUReportingControllerXPCServer
- __OBJC_METACLASS_RO_$_TUReportingControllerXPCClient
- __OBJC_PROTOCOL_$_TUReportingControllerDataSource
- __OBJC_PROTOCOL_$_TUReportingControllerXPCServer
- __OBJC_PROTOCOL_REFERENCE_$_TUReportingControllerXPCServer
- ___109+[TUConversation mergedRemoteMemberHandlesFromRemoteMembers:withLocalMember:removingLocallyAssociatedMember:]_block_invoke
- ___47-[TUReportingControllerXPCClient xpcConnection]_block_invoke
- ___47-[TUReportingControllerXPCClient xpcConnection]_block_invoke_2
- ___60-[TUReportingControllerXPCClient didCleanUpForStream:reply:]_block_invoke
- ___60-[TUReportingControllerXPCClient didCleanUpForStream:reply:]_block_invoke_2
- ___62-[TUNeighborhoodActivityConduitXPCClient splitSessionUpdated:]_block_invoke
- ___71+[TUReportingControllerXPCClient reportingControllerServerXPCInterface]_block_invoke
- ___74-[TUReportingControllerXPCClient registeredStream:withAvailability:reply:]_block_invoke
- ___74-[TUReportingControllerXPCClient registeredStream:withAvailability:reply:]_block_invoke_2
- ___83-[TUReportingControllerXPCClient didStartRequestForStream:withTransactionID:reply:]_block_invoke
- ___83-[TUReportingControllerXPCClient didStartRequestForStream:withTransactionID:reply:]_block_invoke_2
- ___85-[TUReportingControllerXPCClient didReceiveResultsForStream:withTransactionID:reply:]_block_invoke
- ___85-[TUReportingControllerXPCClient didReceiveResultsForStream:withTransactionID:reply:]_block_invoke_2
- ___86+[TUConversation mergedRemoteMembers:withLocalMember:removingLocallyAssociatedMember:]_block_invoke
- ___block_descriptor_60_e8_32s40bs_e5_v8?0l
- __block_literal_global.1652
- __block_literal_global.1658
- __block_literal_global.285
- __block_literal_global.99
- _objc_msgSend$didCleanUpForStream:reply:
- _objc_msgSend$didReceiveResultsForStream:withTransactionID:reply:
- _objc_msgSend$didStartRequestForStream:withTransactionID:reply:
- _objc_msgSend$initWithCallIdentifier:callerIdSubstring:displayName:isBranded:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:
- _objc_msgSend$initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:recentCallsInfos:
- _objc_msgSend$isDefaultAppScheme:
- _objc_msgSend$mergedRemoteMemberHandlesFromRemoteMembers:withLocalMember:removingLocallyAssociatedMember:
- _objc_msgSend$mergedRemoteMembers:withLocalMember:removingLocallyAssociatedMember:
- _objc_msgSend$registeredStream:withAvailability:reply:
- _objc_msgSend$reportingControllerServerXPCInterface
- reportingControllerServerXPCInterface.onceToken
- reportingControllerServerXPCInterface.reportingControllerServerXPCInterface
CStrings:
+ " isEmergency=%@"
+ ":$"
+ "@80@0:8@16@24@32B40B44@48@56@64@72"
+ "@84@0:8@16@24@32@40@48B56@60@68@76"
+ "AutomaticCallActivationDisabled"
+ "ContinuityEmergencyMultiDeviceDiscovery"
+ "Failed to update split session due to %@"
+ "Moose"
+ "Proxying disconnectCurrentCall through CSD"
+ "T@\"TUConversationMemberAssociation\",C,N,V_localMemberAssociation"
+ "TB,N,V_hasEverUnsuppressedRingtone"
+ "TB,R,N,V_isEmergency"
+ "_hasEverUnsuppressedRingtone"
+ "_isEmergency"
+ "_localMemberAssociation"
+ "automaticCallActivationDisabled"
+ "callConnectHaptics"
+ "callConnectHapticsEnabled"
+ "com.apple.preferences.sounds"
+ "continuityEmergencyMultiDeviceDiscoveryEnabled"
+ "disconnectCurrentCall"
+ "effects-haptic"
+ "getCurrentCallsToDisconnect"
+ "hasEverUnsuppressedRingtone"
+ "hasTelephonyOrDefaultAppScheme"
+ "initWithCallIdentifier:callerIdSubstring:displayName:isBranded:isEmergency:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:"
+ "initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:recentCallsInfos:callBlockedStates:"
+ "isDefaultCallingAppPromptURL"
+ "isDefaultCallingAppScheme:"
+ "isDefaultCallingAppURL"
+ "isForceTelephonyPromptURL"
+ "isForceTelephonyScheme:"
+ "isForceTelephonyURL"
+ "isOneToOneFaceTimeMyself: activeRemoteParticipants.count: %lu, remoteMembers.count: %lu, isOneToOneModeEnabled: %d, localHandle: %@, initiator: %@, state: %ld"
+ "localMemberAssociation"
+ "mergedRemoteMemberHandlesFromRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:"
+ "mergedRemoteMembers:withLocalMemberAssociation:removingLocallyAssociatedMember:"
+ "mooseEnabled"
+ "remoteMembers: %@"
+ "setHasEverUnsuppressedRingtone:"
+ "setLocalMemberAssociation:"
+ "splitSessionUpdated"
+ "v24@?0@\"TUNearbyDeviceHandle\"8@\"NSError\"16"
- ":#"
- "@76@0:8@16@24@32@40@48B56@60@68"
- "@76@0:8@16@24@32B40@44@52@60@68"
- "Error reporting captured stream token: %@"
- "Error reporting moments stream token: %@"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"<TUReportingControllerXPCServer>\",&,N"
- "TUReportingControllerDataSource"
- "TUReportingControllerXPCClient"
- "TUReportingControllerXPCServer"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Vv36@0:8q16i24@?28"
- "Vv36@0:8q16i24@?<v@?@\"NSError\">28"
- "com.apple.InCallService.speaker-used"
- "com.apple.mobilephone.talking-with-phone-away-from-face-without-speaker"
- "com.apple.telephonyutilities.callservicesdaemon.reportingcontroller"
- "com.apple.telephonyutilities.reportingcontrollerxpcclient"
- "com.apple.tips.phone_speakerphone"
- "didCleanUpForStream: %ld"
- "didCleanUpForStream:reply:"
- "didReceiveResultsForStream: %ld transactionID: %@"
- "didReceiveResultsForStream:withTransactionID:reply:"
- "didStartRequestForStream: %ld transactionID: %@"
- "didStartRequestForStream:withTransactionID:reply:"
- "initWithCallIdentifier:callerIdSubstring:displayName:isBranded:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:"
- "initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:recentCallsInfos:"
- "invalid Collection: less than 'count' elements in collection"
- "isOneToOneFaceTimeMyself: activeRemoteParticipants.count: %lu, remoteMembers.count: %lu, isOneToOneModeEnabled: %d, localHandle: %@"
- "logAnalyticsEventSpeakerphone"
- "mergedRemoteMemberHandlesFromRemoteMembers:withLocalMember:removingLocallyAssociatedMember:"
- "mergedRemoteMembers:withLocalMember:removingLocallyAssociatedMember:"
- "registeredStream: %ld withAvailability: %ld"
- "registeredStream:withAvailability:reply:"
- "reporting controller provider XPC connection interrupted (client side)"
- "reporting controller xpc connection invalidated (client side)"
- "reportingControllerServerXPCInterface"
- "urlSchemeMatchesDefaultProvider:provider:"
- "v36@0:8q16i24@?28"
- "v36@0:8q16i24@?<v@?@\"NSError\">28"

```
