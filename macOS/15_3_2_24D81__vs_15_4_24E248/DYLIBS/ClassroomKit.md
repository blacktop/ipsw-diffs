## ClassroomKit

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/Versions/A/ClassroomKit`

```diff

-112.2.4.0.0
-  __TEXT.__text: 0xc1014
+112.4.4.0.0
+  __TEXT.__text: 0xc4bfc
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x1082c
+  __TEXT.__objc_methlist: 0x129cc
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x88ec
+  __TEXT.__cstring: 0x88d1
   __TEXT.__oslogstring: 0x43b6
-  __TEXT.__gcc_except_tab: 0x6e0
+  __TEXT.__gcc_except_tab: 0x6e8
   __TEXT.__ustring: 0x37e
-  __TEXT.__unwind_info: 0x3660
+  __TEXT.__unwind_info: 0x38e8
   __TEXT.__objc_classname: 0x439a
-  __TEXT.__objc_methname: 0x2313d
+  __TEXT.__objc_methname: 0x230e0
   __TEXT.__objc_methtype: 0x5bb0
   __TEXT.__objc_stubs: 0x15c20
   __DATA_CONST.__got: 0x1228

   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x448
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6aa8
+  __DATA_CONST.__objc_selrefs: 0x6e38
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xbd0
   __DATA_CONST.__objc_arraydata: 0x2a0
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x36d0
   __AUTH_CONST.__cfstring: 0x8e60
-  __AUTH_CONST.__objc_const: 0x29fe8
+  __AUTH_CONST.__objc_const: 0x263f0
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B2433E2-61F7-3170-8311-634AD8281AD3
-  Functions: 5912
-  Symbols:   15704
-  CStrings:  9481
+  UUID: A7F8BBC5-2526-3871-8A21-39EED613C371
+  Functions: 6285
+  Symbols:   16131
+  CStrings:  9477
 
Symbols:
+ +[CATOperationQueue(CRKAdditions) crk_backgroundQueue].cold.1
+ +[CRKASMCertificateUserIdentifierExtractor pickIdentifierFromIdentifiers:].cold.2
+ +[CRKASMCollidingCourseFilter coursesByFilteringCollidingCoursesFromArray:].cold.2
+ +[CRKASMConcreteNameComponents sharedFormatter].cold.1
+ +[CRKChunkedFile assertFileDescriptorIsValid:].cold.1
+ +[CRKClassKitColorAndMascotUtility classThemeColors].cold.1
+ +[CRKClassSessionBeaconBrowser invitationUUID].cold.1
+ +[CRKClassroomInstallation installationWithClassroomBundleIdentifier:bundleHasContentsFolder:instructordBundleIdentifier:].cold.2
+ +[CRKConcreteStudentConnection connectionWithStudentDaemonProxy:invalidationHandler:].cold.1
+ +[CRKCourseEnrollmentController sharedEnrollmentController].cold.1
+ +[CRKDevice(Translations) keyTranslations].cold.1
+ +[CRKEmptySubscription errorSubscriptionWithReason:].cold.2
+ +[CRKFeatureDataStoreHeuristics_MCX overrideFeaturesByFeature].cold.1
+ +[CRKFeatureDataStoreHeuristics_MCX overrideIsForcedByFeature].cold.1
+ +[CRKFeatures allClassroomCRKFeatures].cold.1
+ +[CRKFeatures allClassroomTopLevelRestrictions].cold.1
+ +[CRKIDSMessageNotificationInfo instanceWithDictionary:].cold.1
+ +[CRKIDSMessageNotificationInfo instanceWithDictionary:].cold.2
+ +[CRKIDSMessageNotificationInfo instanceWithDictionary:].cold.3
+ +[CRKInstructorExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[CRKInstructorExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[CRKInstructorExtensionProxy sharedExtensionProxy].cold.1
+ +[CRKInstructorHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[CRKInstructorHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[CRKJSONConverter JSONArrayForArray:].cold.1
+ +[CRKJSONConverter JSONDictionaryForDictionary:].cold.1
+ +[CRKJSONConverter bestEffortJSONObjectForObject:].cold.1
+ +[CRKJSONConverter bestEffortJSONObjectForObject:].cold.2
+ +[CRKJSONConverter bestEffortJSONObjectForObject:].cold.3
+ +[CRKJSONConverter stringForObject:].cold.1
+ +[CRKJSONConverter stringForObject:].cold.2
+ +[CRKLocalDeviceIPAddresses makeIPAddresses].cold.2
+ +[CRKNetworkPowerAssertion sharedInstance].cold.1
+ +[CRKPlatformClassroomLockScreenMonitor sharedMonitor].cold.1
+ +[CRKPlatformFeatureDataStore sharedDataStore].cold.1
+ +[CRKPlatformInternetDateProvider sharedProvider].cold.1
+ +[CRKShareTarget sandboxExtensionForPath:].cold.1
+ +[CRKSystemInfo sharedSystemInfo].cold.1
+ +[CRKTransportInvalidator invalidateTransportOperationDidFinish:].cold.2
+ +[NSDate(CRKAdditions) crk_sharedDateFormatter].cold.1
+ -[CRKASMAtomicRosterProvider createCourseWithProperties:completion:].cold.1
+ -[CRKASMAtomicRosterProvider evaluateConstraintForUnderlyingCompletion:error:].cold.1
+ -[CRKASMAtomicRosterProvider evalutateConstraintsForRosterUpdate].cold.1
+ -[CRKASMAtomicRosterProvider pushCompletion:withRosterEvaluator:].cold.1
+ -[CRKASMAtomicRosterProvider removeCourseWithIdentifier:completion:].cold.1
+ -[CRKASMAtomicRosterProvider updateCourseWithIdentifier:properties:completion:].cold.1
+ -[CRKASMConcreteUserDirectoryIterator queryDidFinishExecutingWithResults:error:].cold.1
+ -[CRKASMConcreteUserDirectoryIterator queryDidFinishExecutingWithResults:error:].cold.2
+ -[CRKASMConcreteUserDirectoryIterator serviceQueryQueue].cold.1
+ -[CRKASMCredentialStore addCertificate:entry:].cold.1
+ -[CRKASMCredentialStore addCertificate:entry:].cold.2
+ -[CRKASMCredentialStore addCertificate:forUserIdentifier:].cold.1
+ -[CRKASMCredentialStore addCertificate:forUserIdentifier:].cold.2
+ -[CRKASMCredentialStore addCertificates:forUserIdentifier:].cold.1
+ -[CRKASMCredentialStore addIdentity:entry:].cold.1
+ -[CRKASMCredentialStore addIdentity:entry:].cold.2
+ -[CRKASMCredentialStore addIdentity:forUserIdentifier:].cold.1
+ -[CRKASMCredentialStore addIdentity:forUserIdentifier:].cold.2
+ -[CRKASMRosterUpdater objectIDForCourseWithIdentifier:inRoster:error:].cold.1
+ -[CRKASMTimeoutRosterProvider createCourseWithProperties:completion:].cold.1
+ -[CRKASMTimeoutRosterProvider dealloc].cold.1
+ -[CRKASMTimeoutRosterProvider operationDidFinishWithTimer:error:].cold.1
+ -[CRKASMTimeoutRosterProvider removeCourseWithIdentifier:completion:].cold.1
+ -[CRKASMTimeoutRosterProvider updateCourseWithIdentifier:properties:completion:].cold.1
+ -[CRKASMUserFactory isUser:suitableForPerson:].cold.1
+ -[CRKAnnotatedCredentialStore storedManifest].cold.2
+ -[CRKApplicationInfo isEqual:].cold.1
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.1
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.2
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.3
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.4
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.5
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.6
+ -[CRKArrayDifferenceEngine updateWithNewArray:].cold.7
+ -[CRKBoundedGrowthFunction initWithGrowthFunction:lowerBound:upperBound:].cold.1
+ -[CRKBoundedGrowthFunction initWithGrowthFunction:lowerBound:upperBound:].cold.2
+ -[CRKCancelableServer decrementClientCount].cold.1
+ -[CRKCancelableServer decrementClientCount].cold.2
+ -[CRKCancelableServer makeCountedCancelable].cold.1
+ -[CRKCertificatesRequestResult isEqual:].cold.1
+ -[CRKChunkedFile readNextChunkIntoBuffer:error:].cold.1
+ -[CRKClassKitAccountStateProvider accountStoreDidChange:].cold.1
+ -[CRKClassKitChangeNotifier dataChanged].cold.1
+ -[CRKClassKitClassPropertyApplicator addTrustedUser:toClass:].cold.1
+ -[CRKClassKitClassPropertyApplicator addUser:toClass:].cold.1
+ -[CRKClassKitClassPropertyApplicator removeTrustedUser:fromClass:].cold.1
+ -[CRKClassKitClassPropertyApplicator removeUser:fromClass:].cold.1
+ -[CRKClassKitPersonaAdopter currentUserChanged].cold.1
+ -[CRKClassKitPersonaAdopter performBlockWithClassKitPersona:].cold.1
+ -[CRKClassSession foundBeaconWithFlags:].cold.1
+ -[CRKClassSession initWithIdentifier:].cold.1
+ -[CRKClassSession lostBeacon].cold.1
+ -[CRKClassSessionBeaconBrowser increaseScanFrequencyForDuration:].cold.1
+ -[CRKClassSessionBeaconBrowser setAllowInvitationSessions:].cold.1
+ -[CRKClassSessionBeaconBrowser setOrganizationUUIDs:].cold.1
+ -[CRKClassSessionBeaconBrowser startBrowsing].cold.1
+ -[CRKClassSessionBeaconBrowser stopBrowsing].cold.1
+ -[CRKClassSessionBrowser acquireConnectWithoutBeaconAssertionForInvitationSessionWithEndpoint:].cold.1
+ -[CRKClassSessionBrowser acquireConnectWithoutBeaconAssertionForSessionIdentifier:].cold.1
+ -[CRKClassSessionBrowser beaconBrowser:didFindBeaconForClassSession:flags:].cold.1
+ -[CRKClassSessionBrowser beaconBrowser:didFindBeaconForInvitationSessionWithEndpoint:].cold.1
+ -[CRKClassSessionBrowser classSessionInvalidated:].cold.1
+ -[CRKClassSessionBrowser classSessionRejected:].cold.1
+ -[CRKClassSessionBrowser delegateNeedsTrustedAnchorCertificatesForGroup:].cold.1
+ -[CRKClassSessionBrowser hasConnectionToClassWithIdentifier:].cold.1
+ -[CRKClassSessionBrowser hasConnectionToClassWithIdentifier:].cold.2
+ -[CRKClassSessionBrowser init].cold.1
+ -[CRKClassSessionBrowser invitationSessionWithEndpointInvalidated:].cold.1
+ -[CRKClassSessionBrowser lostConnectionToClassSession:].cold.1
+ -[CRKClassSessionBrowser lostConnectionToInvitationSessionWithEndpoint:].cold.1
+ -[CRKClassSessionBrowser releaseConnectWithoutBeaconAssertionForInvitationSessionWithEndpoint:].cold.1
+ -[CRKClassSessionBrowser releaseConnectWithoutBeaconAssertionForSessionIdentifier:].cold.1
+ -[CRKClassSessionBrowser setAllowInvitationSessions:].cold.1
+ -[CRKClassSessionBrowser setAllowUnenrolledSessions:].cold.1
+ -[CRKClassSessionBrowser setEnrolledControlGroupIdentifiers:].cold.1
+ -[CRKClassSessionBrowser setOrganizationUUIDs:].cold.1
+ -[CRKConcreteCertificate keySizeInBits].cold.2
+ -[CRKConcreteClassKitFacade addPerson:withRole:toClass:].cold.1
+ -[CRKConcreteClassKitFacade addPerson:withRole:toClass:].cold.2
+ -[CRKConcreteClassKitFacade executeQuery:].cold.1
+ -[CRKConcreteClassKitFacade objectIDsOfMembersInClass:withRole:].cold.1
+ -[CRKConcreteClassKitFacade removePerson:withRole:fromClass:].cold.1
+ -[CRKConcreteClassKitFacade removePerson:withRole:fromClass:].cold.2
+ -[CRKConcreteClassKitRosterRequirements callGeneralObserversWithReason:].cold.1
+ -[CRKConcreteFileDescriptor close].cold.2
+ -[CRKConcreteFileDescriptor rawValue].cold.1
+ -[CRKConcreteIDSAccount account:isActiveChanged:].cold.1
+ -[CRKConcreteIDSFirewall addAllowedAppleIDs:completion:].cold.1
+ -[CRKConcreteIDSFirewall fetchAllowedAppleIDsWithCompletion:].cold.1
+ -[CRKConcreteIDSFirewall removeAllowedAppleIDs:completion:].cold.1
+ -[CRKConcreteIDSMessageDidReceiveSubscription cancel].cold.1
+ -[CRKConcreteIDSMessageDidReceiveSubscription receiveMessage:senderAppleID:senderAddress:].cold.1
+ -[CRKConcreteIDSMessageDidReceiveSubscription resume].cold.1
+ -[CRKConcreteIDSMessageDidSendSubscription cancel].cold.1
+ -[CRKConcreteIDSMessageDidSendSubscription receiveMessageIdentifier:didSucceed:error:].cold.1
+ -[CRKConcreteIDSMessageDidSendSubscription resume].cold.1
+ -[CRKConcreteMCXPrimitives_macOS isKeyUserModifiable:].cold.1
+ -[CRKCourse initWithIdentifier:type:].cold.1
+ -[CRKCourseEnrollmentController disconnectOperationDidFinish:].cold.2
+ -[CRKCourseEnrollmentController fetchConfigurationTypeOperationDidFinish:].cold.2
+ -[CRKCourseEnrollmentController initWithStudentDaemonProxy:].cold.1
+ -[CRKDataSeparationBlockingClassKitFacade nextAccountState].cold.2
+ -[CRKDevice(Private) initWithIdentifier:].cold.1
+ -[CRKDeviceDisplay isEqual:].cold.1
+ -[CRKDictionaryRowTableEntries initWithDictionaryObjects:keys:].cold.1
+ -[CRKDictionaryRowTableEntries initWithDictionaryObjects:keys:].cold.2
+ -[CRKDownloadResourcesOperation URLSession:task:didReceiveChallenge:completionHandler:].cold.1
+ -[CRKDownloadResourcesOperation cancelIfNeeded].cold.1
+ -[CRKDynamicDataObserverClassKitFacade addDataObserver:].cold.1
+ -[CRKDynamicDataObserverClassKitFacade removeDataObserver:].cold.1
+ -[CRKEDUPayload parseDictionary:isStub:outError:].cold.2
+ -[CRKEventLog initWithStartDate:endDate:].cold.1
+ -[CRKEventLog initWithStartDate:endDate:].cold.2
+ -[CRKEventLog initWithStartDate:endDate:eventDatas:].cold.1
+ -[CRKEventLog initWithStartDate:endDate:events:].cold.1
+ -[CRKExecutionTimer start].cold.1
+ -[CRKExecutionTimer stop].cold.1
+ -[CRKExpiredCourseAlertText initWithCourse:].cold.1
+ -[CRKExpiredCoursesInteraction initWithStudentDaemonProxy:delegate:courses:].cold.1
+ -[CRKExpiredCoursesInteraction initWithStudentDaemonProxy:delegate:courses:].cold.2
+ -[CRKExpiredCoursesInteraction initWithStudentDaemonProxy:delegate:courses:].cold.3
+ -[CRKExpiredCoursesInteraction leaveControlGroupsOperationDidFinish:].cold.2
+ -[CRKExpiredCoursesInteraction leaveControlGroupsOperationDidFinish:].cold.3
+ -[CRKExpiredCoursesInteraction removeCourses:].cold.1
+ -[CRKFTSEntry initWithFTSEntry:error:].cold.1
+ -[CRKFTSEnumeration closeFTS:].cold.2
+ -[CRKFTSEnumeration initWithDirectoryPath:options:].cold.1
+ -[CRKFetchObservingInstructorsByCourseOperation compileResultsWithFetchCoursesResult:fetchScreenObserversResult:].cold.1
+ -[CRKFetchObservingInstructorsByCourseOperation operationsDidComplete:].cold.1
+ -[CRKFetchObservingInstructorsByCourseOperation operationsDidComplete:].cold.2
+ -[CRKFileBackedMarker initWithFileURL:].cold.1
+ -[CRKFileBasedKeyedDataStore URLForKey:].cold.1
+ -[CRKFileBasedKeyedDataStore initWithDirectoryURL:directoryResourceValuesByKey:].cold.1
+ -[CRKFileBasedKeyedDataStore updateExistingDirectoryResourceValues].cold.2
+ -[CRKHostResourcesOperation initWithConfiguration:].cold.1
+ -[CRKHostResourcesOperation zipDirectoryAtURL:completion:].cold.1
+ -[CRKHostResourcesOperation zipDirectoryAtURL:completion:].cold.2
+ -[CRKIDSAccountsEvaluator knownAccountsDidChange].cold.1
+ -[CRKIDSAccountsEvaluator observedAccountDidChange:].cold.1
+ -[CRKIDSFirewallUpdatingRosterProvider rosterDidChange].cold.1
+ -[CRKIDSFirewallUpdatingRosterProvider synchronizeFirewallOperationDidFail:].cold.2
+ -[CRKInstructorExtensionProxy beginExtensionRequestWithCompletionBlock:].cold.1
+ -[CRKInstructorExtensionProxy configureInstructorExtensionAfterFetchError:completionBlock:].cold.1
+ -[CRKInstructorExtensionProxy fetchListenerEndpointForExtensionBundleIdentifier:fromClassroomBundleWithURL:completionBlock:].cold.1
+ -[CRKInterfaceOrientationMonitor interfaceOrientationWithCompletion:].cold.1
+ -[CRKInterfaceOrientationMonitor interfaceOrientationWithCompletion:].cold.2
+ -[CRKInternetDateProvider callAndRemoveCompletionHandlerWithDate:error:task:].cold.1
+ -[CRKLeaveControlGroupsRequest encodeWithCoder:].cold.1
+ -[CRKLeaveControlGroupsRequest initWithCoder:].cold.1
+ -[CRKListTableEntries initWithArray:].cold.1
+ -[CRKLogEvent initWithName:date:userInfo:].cold.1
+ -[CRKLogEvent initWithName:date:userInfo:].cold.2
+ -[CRKMonitorExpiredCoursesInteraction beginInteractionWithExpiredCourses:].cold.1
+ -[CRKMonitorExpiredCoursesInteraction expiredCoursesInteractionDidFinish:].cold.2
+ -[CRKMonitorExpiredCoursesInteraction expiredCoursesInteractionDidFinish:].cold.3
+ -[CRKMonitorExpiredCoursesInteraction initWithStudentDaemonProxy:enrollmentController:expiredCoursesInteractionDelegate:].cold.1
+ -[CRKMonitorExpiredCoursesInteraction initWithStudentDaemonProxy:enrollmentController:expiredCoursesInteractionDelegate:].cold.2
+ -[CRKMonitorExpiredCoursesInteraction initWithStudentDaemonProxy:enrollmentController:expiredCoursesInteractionDelegate:].cold.3
+ -[CRKMonitorExpiredCoursesInteraction updateWithCourses:].cold.1
+ -[CRKNonCatalystStudentDaemonProxy setOfActiveRestrictionUUIDs:].cold.2
+ -[CRKOperationBackedIDSMessageSubscription taskOperation:didPostNotificationWithName:userInfo:].cold.1
+ -[CRKOrderedOneToManyKVOAccumulator _integrateChange:toArray:].cold.1
+ -[CRKOrderedOneToManyKVOAccumulator _prestateIndexForImmediateIndex:].cold.1
+ -[CRKOrderedOneToManyKVOAccumulator observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[CRKPersonaMatchEnforcingClassKitFacade isPersonaEligible].cold.1
+ -[CRKPlatformInternetDateProvider fetchInternetDateWithCompletion:].cold.1
+ -[CRKPrimitiveBackedCertificateConduit operationToFetchCertificateForDestinationAppleID:sourceAppleID:destinationDeviceIdentifier:controlGroupIdentifier:sourceRole:destinationRole:requesterCertificate:timeout:].cold.1
+ -[CRKPrivateIdentity encodeWithCoder:].cold.1
+ -[CRKPrivateIdentity initWithCoder:].cold.1
+ -[CRKPrivateIdentity initWithDictionary:].cold.1
+ -[CRKPrivateIdentity initWithIdentityPersistentId:stagedIdentityPersistentId:commonNamePrefix:].cold.1
+ -[CRKPrivateIdentity initWithIdentityPersistentId:stagedIdentityPersistentId:commonNamePrefix:].cold.2
+ -[CRKResource initWithHostedURL:isZippedBundle:].cold.1
+ -[CRKRightPaddingTableEntry initWithObject:].cold.1
+ -[CRKScreenObservationMonitor didEstablishStudentConnection:].cold.1
+ -[CRKScreenObservationMonitor didLoseStudentConnection].cold.1
+ -[CRKSession backoffDidFinish].cold.1
+ -[CRKSession connect].cold.1
+ -[CRKSession didConnect].cold.1
+ -[CRKSession failedToConnect].cold.1
+ -[CRKSession foundBeacon].cold.1
+ -[CRKSession initWithEndpoint:].cold.1
+ -[CRKSession initWithEndpoint:].cold.2
+ -[CRKSession invalidate].cold.1
+ -[CRKSession localWiFiBecameAvailable].cold.1
+ -[CRKSession localWiFiBecameUnavailable].cold.1
+ -[CRKSession lostBeacon].cold.1
+ -[CRKSession lostConnection].cold.1
+ -[CRKSession rejected].cold.1
+ -[CRKSession setRequiresBeacon:].cold.1
+ -[CRKSession startPreflightingTransport:].cold.1
+ -[CRKShareTarget initWithDictionary:].cold.1
+ -[CRKShareTargetBrowser connectToInstructord].cold.1
+ -[CRKShareTargetBrowser connectToStudentd].cold.1
+ -[CRKShareTargetBrowser initWithDelegate:queue:].cold.1
+ -[CRKShareTargetBrowser initWithDelegate:queue:].cold.2
+ -[CRKShareTargetBrowser resume].cold.1
+ -[CRKShowOpenDialogOperation cleanupHiddenTransferItemsIfNeeded].cold.2
+ -[CRKShowOpenDialogOperation failWithError:].cold.2
+ -[CRKShowOpenDialogOperation failWithError:].cold.3
+ -[CRKShowOpenDialogOperation initWithFileURLs:keepOriginalFiles:previewImageData:senderName:autoAccept:sourceBundleIdentifier:filesDescription:cleanupDelay:sharingPrimitives:fileSystemPrimitives:].cold.1
+ -[CRKShowOpenDialogOperation startTransfer].cold.2
+ -[CRKShowOpenDialogOperation succeedIfNeeded].cold.1
+ -[CRKShowOpenDialogOperation transferDidFinishWithSuccess:destinationPath:error:].cold.1
+ -[CRKShowOpenDialogOperation transferDidProgressWithSuccess:destinationPath:error:].cold.1
+ -[CRKShowOpenDialogOperation transferDidStartWithSuccess:destinationPath:error:].cold.1
+ -[CRKShowOpenDialogOperation transferWithIdentifierWasAccepted:].cold.1
+ -[CRKShowOpenDialogOperation transferWithIdentifierWasDeclined:error:].cold.1
+ -[CRKSingleConnectionAttemptStudentDaemonProxy failWithError:].cold.1
+ -[CRKSingleConnectionAttemptStudentDaemonProxy operationForRequest:].cold.1
+ -[CRKStudentDaemonProxy addObserver:].cold.1
+ -[CRKStudentDaemonProxy client:didInterruptWithError:].cold.2
+ -[CRKStudentDaemonProxy connect].cold.1
+ -[CRKStudentDaemonProxy disconnect].cold.1
+ -[CRKStudentDaemonProxy enqueueOperation:].cold.1
+ -[CRKStudentDaemonProxy enqueueOperation:].cold.2
+ -[CRKStudentDaemonProxy enqueuedOperationForRequest:].cold.1
+ -[CRKStudentDaemonProxy enqueuedOperationForRequest:].cold.2
+ -[CRKStudentDaemonProxy operationForRequest:].cold.1
+ -[CRKStudentDaemonProxy operationForRequest:].cold.2
+ -[CRKStudentDaemonProxy removeObserver:].cold.1
+ -[CRKSynchronizeIDSFirewallOperation addAllowedAppleIDs].cold.1
+ -[CRKSynchronizeIDSFirewallOperation computeChanges].cold.1
+ -[CRKSynchronizeIDSFirewallOperation computeChanges].cold.2
+ -[CRKSynchronizeIDSFirewallOperation finishWithError:].cold.1
+ -[CRKSynchronizeIDSFirewallOperation operationToFetchAppleIDsDidFinish:].cold.1
+ -[CRKSynchronizeIDSFirewallOperation removeAllowedAppleIDs].cold.1
+ -[CRKSynchronizeIDSFirewallOperation run].cold.1
+ -[CRKTable initWithEntries:].cold.1
+ -[CRKTable stringValue].cold.1
+ -[CRKTableEntriesWithAddedColumn initWithOrigin:index:entries:].cold.1
+ -[CRKTableEntriesWithAddedColumn initWithOrigin:index:entries:].cold.2
+ -[CRKTableEntriesWithAddedColumn initWithOrigin:index:entries:].cold.3
+ -[CRKTableEntriesWithAddedColumn initWithOrigin:index:entries:].cold.4
+ -[CRKTableEntriesWithAddedRow initWithOrigin:index:entries:].cold.1
+ -[CRKTableEntriesWithAddedRow initWithOrigin:index:entries:].cold.2
+ -[CRKTableEntriesWithAddedRow initWithOrigin:index:entries:].cold.3
+ -[CRKTableEntriesWithAddedRow initWithOrigin:index:entries:].cold.4
+ -[CRKTableEntriesWithColumnSpacer initWithOrigin:index:spacerEntry:].cold.1
+ -[CRKTableEntriesWithColumnSpacer initWithOrigin:index:spacerEntry:].cold.2
+ -[CRKTableEntriesWithRowSpacer initWithOrigin:index:spacerEntry:].cold.1
+ -[CRKTableEntriesWithRowSpacer initWithOrigin:index:spacerEntry:].cold.2
+ -[CRKTimeoutHarnessOperation run].cold.1
+ -[CRKToolCommand connectToTaskClientWithCompletionBlock:].cold.1
+ -[CRKTransportPreflightResultObject dealloc].cold.1
+ -[CRKUnzipOperation initWithZipFileURL:destinationDirectoryURL:].cold.1
+ -[CRKUnzipOperation initWithZipFileURL:destinationDirectoryURL:].cold.2
+ -[CRKUser encodeWithCoder:].cold.1
+ -[CRKUser initWithCoder:].cold.1
+ -[CRKUser isEqualToUser:].cold.1
+ -[CRKValidXPCConnectionProvider connectionDied:].cold.2
+ -[CRKZipOperation initWithDirectoryURL:destinationZipName:].cold.1
+ -[CRKZipOperation initWithDirectoryURL:destinationZipURL:].cold.1
+ -[CRKZipOperation initWithDirectoryURL:destinationZipURL:].cold.2
+ -[NSArray(CRKGenericAdditions) crk_sortedArrayForRange:usingComparator:].cold.1
+ -[NSArray(CRKGenericAdditions) crk_sortedSubarrayWithRange:comparator:].cold.1
+ -[NSDictionary(CRKGenericAdditions) crk_mapUsingBlock:].cold.1
+ -[NSFileManager(CRKAdditions) crk_collisionAvoidingURLForURL:].cold.2
+ -[NSFileManager(CRKAdditions) crk_deepContentsOfDirectoryAtPath:options:error:].cold.1
+ -[NSSet(CRKAdditions) crk_mapUsingBlock:].cold.1
+ -[NSURL(CRKAdditions) crk_isBundle].cold.2
+ CRKErrorWithCodeAndUserInfo.cold.1
+ CRKFoundationClasses.cold.1
+ JSONStringRepresentation.cold.2
+ _CRKLogASM.cold.1
+ _CRKLogBluetooth.cold.1
+ _CRKLogGeneral.cold.1
+ _CRKLogOperation.cold.1
+ _CRKLogSession.cold.1
+ _CRKLogSettings.cold.1
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __21-[CRKEventLog events]_block_invoke.cold.2
+ __44-[CRKShowOpenDialogOperation failWithError:]_block_invoke.cold.1
+ __51-[CRKClassKitCurrentUserProvider updateCurrentUser]_block_invoke.cold.1
+ __63+[CRKClassKitColorAndMascotUtility colorTypesByColorIdentifier]_block_invoke.cold.1
+ __65+[CRKClassKitColorAndMascotUtility mascotTypesByMascotIdentifier]_block_invoke.cold.1
+ __73-[CRKASMRosterUpdater errorWrappingCompletionForCompletion:selectorName:]_block_invoke.cold.2
+ __86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_4.cold.1
+ __88-[CRKTransportPreflightOperation transport:encounteredTrustDecisionWhileTryingToSecure:]_block_invoke.cold.1
+ __block_literal_global.332
- -[CRKConcreteFeatureFlags isRenderPDFThumbnailsEnabled]
- __block_literal_global.329
CStrings:
- "RenderPDFThumbnailsEnabled"
- "TB,R,N,GisRenderPDFThumbnailsEnabled"
- "isRenderPDFThumbnailsEnabled"
- "renderPDFThumbnailsEnabled"

```
