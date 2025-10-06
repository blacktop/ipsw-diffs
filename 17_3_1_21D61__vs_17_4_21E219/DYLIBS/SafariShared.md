## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-617.2.4.10.8
-  __TEXT.__text: 0x1636d0
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0xefc0
-  __TEXT.__gcc_except_tab: 0x191ec
-  __TEXT.__cstring: 0x18769
-  __TEXT.__const: 0x54dc8
-  __TEXT.__oslogstring: 0xeaea
-  __TEXT.__ustring: 0xd9b6
+618.1.15.10.11
+  __TEXT.__text: 0x16ffc0
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0xf9f8
+  __TEXT.__const: 0x56690
+  __TEXT.__gcc_except_tab: 0x196c8
+  __TEXT.__cstring: 0x19fc8
+  __TEXT.__ustring: 0xd374
+  __TEXT.__oslogstring: 0xf1bd
   __TEXT.__dlopen_cstrs: 0x1b3
-  __TEXT.__unwind_info: 0xa420
+  __TEXT.__unwind_info: 0xa798
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x2d04
-  __TEXT.__objc_methname: 0x2e510
-  __TEXT.__objc_methtype: 0xb7f3
-  __TEXT.__objc_stubs: 0x19540
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x13598
-  __DATA_CONST.__objc_classlist: 0xa00
+  __TEXT.__objc_classname: 0x2ed9
+  __TEXT.__objc_methname: 0x3010a
+  __TEXT.__objc_methtype: 0xbb48
+  __TEXT.__objc_stubs: 0x1a3c0
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x13ac0
+  __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17da8
-  __DATA_CONST.__objc_selrefs: 0x8a78
-  __DATA_CONST.__objc_arraydata: 0xdd8
-  __AUTH_CONST.__const: 0x2910
-  __AUTH_CONST.__objc_const: 0x7cf0
-  __AUTH_CONST.__cfstring: 0x16380
-  __AUTH_CONST.__objc_arrayobj: 0x3a8
-  __AUTH_CONST.__objc_intobj: 0x4c8
-  __AUTH_CONST.__objc_doubleobj: 0xa0
+  __DATA_CONST.__objc_const: 0x190d0
+  __DATA_CONST.__objc_selrefs: 0x9010
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_classrefs: 0xc48
+  __DATA_CONST.__objc_superrefs: 0x870
+  __DATA_CONST.__objc_arraydata: 0xc18
+  __AUTH_CONST.__cfstring: 0x17140
+  __AUTH_CONST.__const: 0x2a48
+  __AUTH_CONST.__objc_const: 0x82d8
+  __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0xd90
-  __AUTH.__objc_data: 0x32f0
-  __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0xc00
-  __DATA.__objc_superrefs: 0x800
-  __DATA.__objc_ivar: 0x1298
-  __DATA.__data: 0x2c20
-  __DATA.__bss: 0x720
+  __AUTH_CONST.__objc_intobj: 0x468
+  __AUTH_CONST.__objc_doubleobj: 0xa0
+  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH.__objc_data: 0x37a0
+  __DATA.__got_weak: 0x8
+  __DATA.__objc_ivar: 0x1370
+  __DATA.__data: 0x2da8
+  __DATA.__bss: 0x7f0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x5b8
+  __DATA_DIRTY.__bss: 0x5a0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: EDDCFDED-2498-3911-B7D2-605FAFFB54A9
-  Functions: 8479
-  Symbols:   29023
-  CStrings:  14452
+  UUID: C7C618AD-BD2C-3A3E-AFAA-8A862A2BF453
+  Functions: 8792
+  Symbols:   30014
+  CStrings:  15044
 
Symbols:
+ +[NSBundle(SafariSharedExtras) safari_bundlesFromDirectory:bundleType:]
+ +[NSString(SafariSharedExtras) safari_detailStringWithTitleString:prompt:]
+ +[WBSAutoFillInternalFeedbackController informativeText]
+ +[WBSAutoFillInternalFeedbackController placeholderForFeedbackDetailType:]
+ +[WBSAutoFillInternalFeedbackController titleForAttachmentsType:]
+ +[WBSAutoFillInternalFeedbackController titleForFeedbackCategory:]
+ +[WBSAutoFillInternalFeedbackController titleForFeedbackDetailType:]
+ +[WBSAutoFillInternalFeedbackController titleText]
+ +[WBSDispatchSourceTimer timerWithInterval:repeats:queue:handler:]
+ +[WBSFifoTestResults createFifoAtFileURL:error:]
+ +[WBSFifoTestResults readReportFromFifoHandle:error:]
+ +[WBSFormTelemetryDataMonitor formFieldTypeForFormControlMetadata:formMetadata:]
+ +[WBSInternalFeedbackRadarComponent passwordManagerIOS]
+ +[WBSInternalFeedbackRadarComponent safariAutoFill]
+ +[WBSInternalFeedbackRadarComponent safariIOS]
+ +[WBSInternalFeedbackRadarComponent safariNewBugs]
+ +[WBSInternalFeedbackRadarComponent safariStartPageIOS]
+ +[WBSInternalFeedbackRadarComponent safariStartPageMacOS]
+ +[WBSSingleCreditCardData stringForSingleCreditCardDataType:]
+ +[WBSSiriIntelligenceDonor _historyItemIdentifierForURLString:profileIdentifier:]
+ +[WBSSiriIntelligenceDonor historyItemIdentifierForURL:profileIdentifier:]
+ +[WBSTestResultsReport reportForActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:]
+ +[WBSTestResultsReport reportForError:forStage:forTest:inBundle:]
+ +[WBSTestResultsReport reportForPerformance:forStage:forTest:inBundle:]
+ -[NSURL(SafariSharedExtras) safari_isMarketplaceKitURL]
+ -[WBSAutoFillInternalFeedbackController .cxx_destruct]
+ -[WBSAutoFillInternalFeedbackController _radarTitleComponentForDetails]
+ -[WBSAutoFillInternalFeedbackController attachmentDetailsText]
+ -[WBSAutoFillInternalFeedbackController canContinueInTapToRadar]
+ -[WBSAutoFillInternalFeedbackController continueInTapToRadarURL]
+ -[WBSAutoFillInternalFeedbackController detailTypesForSelectedFeedbackCategory]
+ -[WBSAutoFillInternalFeedbackController diagnosticsData]
+ -[WBSAutoFillInternalFeedbackController initWithDiagnosticsData:]
+ -[WBSAutoFillInternalFeedbackController responseForDetailType:]
+ -[WBSAutoFillInternalFeedbackController selectedAttachmentsType]
+ -[WBSAutoFillInternalFeedbackController selectedFeedbackCategory]
+ -[WBSAutoFillInternalFeedbackController setResponse:forDetailType:]
+ -[WBSAutoFillInternalFeedbackController setSelectedAttachmentsType:]
+ -[WBSAutoFillInternalFeedbackController setSelectedFeedbackCategory:]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData .cxx_destruct]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData creationDateString]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData formMetadata]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData init]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData setFormMetadata:]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData setUrl:]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData url]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData writeTemporaryFileWithFormMetadata]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData writeTemporaryFileWithFormMetadata].cold.1
+ -[WBSAutoFillTestController bundleType]
+ -[WBSAutoFillTestController cleanSuiteWithCompletionHandler:]
+ -[WBSAutoFillTestController expectedResultsPathExtension]
+ -[WBSAutoFillTestController pageTestType]
+ -[WBSAutoFillTestController prepareSuiteWithCompletionHandler:]
+ -[WBSAutoFillTestController runTest:bundle:storeResultsIn:completionHandler:]
+ -[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]
+ -[WBSAutoplayQuirkWhitelistSnapshot initWithSnapshotData:error:]
+ -[WBSAutoplayQuirkWhitelistSnapshot snapshotData]
+ -[WBSBiomeDonationManager _windowProxyStream]
+ -[WBSBrowserTabCompletionMatch initWithTabInfo:userTypedString:alternativeDisplayTextForURL:forQueryID:]
+ -[WBSBundleTestResults .cxx_destruct]
+ -[WBSBundleTestResults beginTest:inBundle:]
+ -[WBSBundleTestResults endTest:inBundle:]
+ -[WBSBundleTestResults fileURL]
+ -[WBSBundleTestResults flushWithCompletionHandler:]
+ -[WBSBundleTestResults initWithFileURL:error:]
+ -[WBSBundleTestResults reportActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:]
+ -[WBSBundleTestResults reportError:forStage:forTest:inBundle:]
+ -[WBSBundleTestResults reportPerformance:forStage:forTest:inBundle:]
+ -[WBSCompletionListVendorForHistoryService .cxx_destruct]
+ -[WBSCompletionListVendorForHistoryService _connect]
+ -[WBSCompletionListVendorForHistoryService _setExportedInterfaceAndObjectForConnection:]
+ -[WBSCompletionListVendorForHistoryService dataSource]
+ -[WBSCompletionListVendorForHistoryService initWithDataSource:]
+ -[WBSCompletionListVendorForHistoryService listener:shouldAcceptNewConnection:]
+ -[WBSCompletionListVendorForHistoryService listener:shouldAcceptNewConnection:].cold.1
+ -[WBSCompletionQuery canonicalQueryString]
+ -[WBSCreditCardData balance]
+ -[WBSCreditCardData isCardBalanceZeroOrNegative]
+ -[WBSCreditCardData test_setBalance:]
+ -[WBSCreditCardData test_setLastUsedDate:]
+ -[WBSCreditCardDataController isVirtualCard:previouslyFilledVirtualCardNumbers:completion:]
+ -[WBSCreditCardDataController sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledVirtualCardData:]
+ -[WBSCreditCardDataController tellWalletThatExistingCardWasFilledInForm:previouslyFilledVirtualCardNumbers:]
+ -[WBSDispatchSourceTimer initWithStartDelay:interval:repeats:queue:handler:]
+ -[WBSDispatchSourceTimer queue]
+ -[WBSDomainAllowListSnapshot initWithSnapshotData:error:]
+ -[WBSDomainAllowListSnapshot snapshotData]
+ -[WBSFifoTestResults .cxx_destruct]
+ -[WBSFifoTestResults _writeReportToFifo:]
+ -[WBSFifoTestResults _writeReportToFifo:].cold.1
+ -[WBSFifoTestResults _writeReportToFifo:].cold.2
+ -[WBSFifoTestResults beginTest:inBundle:]
+ -[WBSFifoTestResults endTest:inBundle:]
+ -[WBSFifoTestResults fifoHandle]
+ -[WBSFifoTestResults fifoURL]
+ -[WBSFifoTestResults flushWithCompletionHandler:]
+ -[WBSFifoTestResults initWithFifoURL:error:]
+ -[WBSFifoTestResults reportActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:]
+ -[WBSFifoTestResults reportError:forStage:forTest:inBundle:]
+ -[WBSFifoTestResults reportPerformance:forStage:forTest:inBundle:]
+ -[WBSFormControlMetadata classification]
+ -[WBSFormControlMetadata continuationID]
+ -[WBSFormControlMetadata continuationIndex]
+ -[WBSFormControlMetadata dictionaryRepresentationRedactingSensitiveValues:]
+ -[WBSFormControlMetadata isVerticalWritingMode]
+ -[WBSFormControlMetadata looksLikeEIDField]
+ -[WBSFormControlMetadata looksLikeIMEIField]
+ -[WBSFormMetadata dictionaryRepresentationRedactingSensitiveValues:]
+ -[WBSFormMetadataController autoFilledField:inForm:inFrame:]
+ -[WBSFormMetadataController autoFilledField:inFrame:]
+ -[WBSFormTelemetryData .cxx_destruct]
+ -[WBSFormTelemetryData fieldIDToSingleFieldData]
+ -[WBSFormTelemetryData formID]
+ -[WBSFormTelemetryData formType]
+ -[WBSFormTelemetryData initWithFormType:formID:]
+ -[WBSFormTelemetryData setFieldIDToSingleFieldData:]
+ -[WBSFormTelemetryDataMonitor .cxx_destruct]
+ -[WBSFormTelemetryDataMonitor _elementTypeForFormControlMetadata:]
+ -[WBSFormTelemetryDataMonitor _isMonitoringTextFieldWithID:forFormID:]
+ -[WBSFormTelemetryDataMonitor _sendModificationTelemetryEventsPerFormField]
+ -[WBSFormTelemetryDataMonitor _sendModificationTelemetryEventsPerForm]
+ -[WBSFormTelemetryDataMonitor _sendUsageTelemetryEventsPerForm]
+ -[WBSFormTelemetryDataMonitor _updateAutoFillOfferedType:forTextFieldWithID:forFormID:]
+ -[WBSFormTelemetryDataMonitor _updateMonitorDataWithFormMetadata:]
+ -[WBSFormTelemetryDataMonitor _updateMonitorDataWithTextFieldMetadata:textFieldValueLength:forFormID:]
+ -[WBSFormTelemetryDataMonitor _updateTelemetryFieldData:withTextFieldMetadata:textFieldValueLength:]
+ -[WBSFormTelemetryDataMonitor _wasAutoFillUsedForModificationType:]
+ -[WBSFormTelemetryDataMonitor initWithWebpageLocale:]
+ -[WBSFormTelemetryDataMonitor sendTelemetryEventsOnFormSubmission]
+ -[WBSFormTelemetryDataMonitor updateAutoFillOfferedType:forTextFieldWithID:forFormMetadata:]
+ -[WBSFormTelemetryDataMonitor updateFormTelemetryWithFormMetadata:textFieldMetadata:textFieldValueLength:]
+ -[WBSFormTelemetryDataMonitor webpageLocale]
+ -[WBSHistoryServiceURLCompletion recordVisit:sourceVisit:title:loadSuccessful:origin:increaseVisitCount:score:statusCode:]
+ -[WBSInternalFeedbackRadar .cxx_destruct]
+ -[WBSInternalFeedbackRadar attachmentPaths]
+ -[WBSInternalFeedbackRadar classification]
+ -[WBSInternalFeedbackRadar component]
+ -[WBSInternalFeedbackRadar continueInTapToRadarURL]
+ -[WBSInternalFeedbackRadar descriptionTemplate]
+ -[WBSInternalFeedbackRadar initWithComponent:title:descriptionTemplate:]
+ -[WBSInternalFeedbackRadar keywords]
+ -[WBSInternalFeedbackRadar reproducibility]
+ -[WBSInternalFeedbackRadar setAttachmentPaths:]
+ -[WBSInternalFeedbackRadar setClassification:]
+ -[WBSInternalFeedbackRadar setComponent:]
+ -[WBSInternalFeedbackRadar setDescriptionTemplate:]
+ -[WBSInternalFeedbackRadar setKeywords:]
+ -[WBSInternalFeedbackRadar setReproducibility:]
+ -[WBSInternalFeedbackRadar setTitle:]
+ -[WBSInternalFeedbackRadar title]
+ -[WBSInternalFeedbackRadarComponent .cxx_destruct]
+ -[WBSInternalFeedbackRadarComponent copyWithZone:]
+ -[WBSInternalFeedbackRadarComponent identifier]
+ -[WBSInternalFeedbackRadarComponent initWithIdentifier:name:version:]
+ -[WBSInternalFeedbackRadarComponent name]
+ -[WBSInternalFeedbackRadarComponent version]
+ -[WBSMutableFormControlMetadata setClassification:]
+ -[WBSMutableFormControlMetadata setContinuationID:]
+ -[WBSMutableFormControlMetadata setContinuationIndex:]
+ -[WBSMutableFormControlMetadata setLooksLikeEIDField:]
+ -[WBSMutableFormControlMetadata setLooksLikeIMEIField:]
+ -[WBSMutableFormControlMetadata setVerticalWritingMode:]
+ -[WBSOfflineSearchRemoteDisablementSnapshot initWithSnapshotData:error:]
+ -[WBSOfflineSearchRemoteDisablementSnapshot initWithSnapshotData:error:].cold.1
+ -[WBSOfflineSearchRemoteDisablementSnapshot snapshotData]
+ -[WBSPageTest .cxx_destruct]
+ -[WBSPageTest expectedResultsURL]
+ -[WBSPageTest identifier]
+ -[WBSPageTest initWithIdentifier:pageURL:expectedResultsURL:dictionary:]
+ -[WBSPageTest pageURL]
+ -[WBSPageTest viewportSize]
+ -[WBSPageTestBundle .cxx_destruct]
+ -[WBSPageTestBundle allTests]
+ -[WBSPageTestBundle identifier]
+ -[WBSPageTestBundle initWithIdentifier:tests:]
+ -[WBSPageTestController .cxx_destruct]
+ -[WBSPageTestController bundleFromNSBundle:]
+ -[WBSPageTestController delegate]
+ -[WBSPageTestController expectedResultsPathExtension]
+ -[WBSPageTestController pageTestType]
+ -[WBSPageTestController setDelegate:]
+ -[WBSPageTestEvaluator iOS]
+ -[WBSPageTestEvaluator iPad]
+ -[WBSPageTestEvaluator iPhone]
+ -[WBSPageTestEvaluator macCatalyst]
+ -[WBSPageTestEvaluator macOS]
+ -[WBSPageZoomPreferenceManager _getZoomStepForDomain:usingBlock:].cold.1
+ -[WBSPageZoomPreferenceManager _getZoomStepForDomain:usingBlock:].cold.2
+ -[WBSPasswordBreachConfigurationBag initWithSnapshotData:error:]
+ -[WBSPasswordBreachConfigurationBag initWithSnapshotData:error:].cold.1
+ -[WBSPasswordBreachConfigurationBag snapshotData]
+ -[WBSSearchParameters isDuckDuckGoABEnabledForSearchEnginePreferenceObserver:]
+ -[WBSSearchParameters isGoogleABEnabledForSearchEnginePreferenceObserver:]
+ -[WBSSearchParameters isLabelPreviousSearchesInCompletionListEnabledForTrial]
+ -[WBSSearchParameters isLabelPreviousSearchesInCompletionListEnabled]
+ -[WBSSearchParameters isStreamlinedCompletionListEnabledForTrial]
+ -[WBSSearchParameters setIsLabelPreviousSearchesInCompletionListEnabledForTrial:]
+ -[WBSSearchParameters setIsStreamlinedCompletionListEnabledForTrial:]
+ -[WBSSingleFieldTelemetryData .cxx_destruct]
+ -[WBSSingleFieldTelemetryData autoFillOfferedType]
+ -[WBSSingleFieldTelemetryData elementType]
+ -[WBSSingleFieldTelemetryData fieldID]
+ -[WBSSingleFieldTelemetryData fieldType]
+ -[WBSSingleFieldTelemetryData initWithFieldType:fieldID:elementType:]
+ -[WBSSingleFieldTelemetryData isAutoFilled]
+ -[WBSSingleFieldTelemetryData isManuallyFilledByUser]
+ -[WBSSingleFieldTelemetryData modificationType]
+ -[WBSSingleFieldTelemetryData setAutoFillOfferedType:]
+ -[WBSSingleFieldTelemetryData setFieldType:]
+ -[WBSSingleFieldTelemetryData setIsAutoFilled:]
+ -[WBSSingleFieldTelemetryData setIsManuallyFilledByUser:]
+ -[WBSSingleFieldTelemetryData setModificationType:]
+ -[WBSSingleFieldTelemetryData wasPreviouslyAutoFilled]
+ -[WBSSiriIntelligenceDonor _indexedIDsForSearchQueryString:outError:]
+ -[WBSSiriIntelligenceDonor processRemovedHistoryItems:forProfileWithIdentifier:]
+ -[WBSTestController .cxx_destruct]
+ -[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]
+ -[WBSTestController bundleFromNSBundle:]
+ -[WBSTestController bundleType]
+ -[WBSTestController bundles]
+ -[WBSTestController cleanBundle:completionHandler:]
+ -[WBSTestController cleanSuiteWithCompletionHandler:]
+ -[WBSTestController cleanTest:bundle:completionHandler:]
+ -[WBSTestController initWithSuiteURL:bundleNames:]
+ -[WBSTestController isRunning]
+ -[WBSTestController prepareBundle:completionHandler:]
+ -[WBSTestController prepareSuiteWithCompletionHandler:]
+ -[WBSTestController prepareTest:bundle:completionHandler:]
+ -[WBSTestController runTest:bundle:storeResultsIn:completionHandler:]
+ -[WBSTestController runTestsAndStoreResultsIn:completionHandler:]
+ -[WBSTestController suiteURL]
+ -[WBSTestResultsReport .cxx_destruct]
+ -[WBSTestResultsReport bundleIdentifier]
+ -[WBSTestResultsReport dictionaryRepresentation]
+ -[WBSTestResultsReport errorCode]
+ -[WBSTestResultsReport errorDomain]
+ -[WBSTestResultsReport errorMessage]
+ -[WBSTestResultsReport initWithDictionaryRepresentation:]
+ -[WBSTestResultsReport performanceValues]
+ -[WBSTestResultsReport reportType]
+ -[WBSTestResultsReport resultsActual]
+ -[WBSTestResultsReport resultsExpectedName]
+ -[WBSTestResultsReport resultsExpected]
+ -[WBSTestResultsReport resultsUniformTypeIdentifier]
+ -[WBSTestResultsReport testIdentifier]
+ -[WBSTestResultsReport testStage]
+ -[WBSTrialManager _weightedRandomIdentifier]
+ -[WBSTrialManager performDelayedLaunchOperations]
+ -[WBSTrialManager trialABGroupIdentifier]
+ -[WBSURLCompletionMatch alternativeDisplayTextForURL]
+ -[WBSURLCompletionMatch setAlternativeDisplayTextForURL:]
+ -[WBSUserAgentQuirksSnapshot initWithSnapshotData:error:]
+ -[WBSUserAgentQuirksSnapshot snapshotData]
+ GCC_except_table180
+ GCC_except_table189
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table292
+ GCC_except_table337
+ OBJC_IVAR_$_WBSBiomeDonationManager._streamAccessQueue
+ _BMSafariWindowProxyIdentifier
+ _CFBundleCopyBundleURL
+ _CFBundleCreateBundlesFromDirectory
+ _NSURLErrorFailingURLErrorKey
+ _OBJC_CLASS_$_NSDecimalNumber
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_CLASS_$_WBSAutoFillInternalFeedbackController
+ _OBJC_CLASS_$_WBSAutoFillInternalFeedbackDiagnosticsData
+ _OBJC_CLASS_$_WBSAutoFillTestController
+ _OBJC_CLASS_$_WBSBundleTestResults
+ _OBJC_CLASS_$_WBSCompletionListVendorForHistoryService
+ _OBJC_CLASS_$_WBSDevice
+ _OBJC_CLASS_$_WBSFifoTestResults
+ _OBJC_CLASS_$_WBSFormTelemetryData
+ _OBJC_CLASS_$_WBSFormTelemetryDataMonitor
+ _OBJC_CLASS_$_WBSInternalFeedbackRadar
+ _OBJC_CLASS_$_WBSInternalFeedbackRadarComponent
+ _OBJC_CLASS_$_WBSPageTest
+ _OBJC_CLASS_$_WBSPageTestBundle
+ _OBJC_CLASS_$_WBSPageTestController
+ _OBJC_CLASS_$_WBSPageTestEvaluator
+ _OBJC_CLASS_$_WBSRemotelyUpdatableDataController
+ _OBJC_CLASS_$_WBSSingleFieldTelemetryData
+ _OBJC_CLASS_$_WBSTestController
+ _OBJC_CLASS_$_WBSTestResultsReport
+ _OBJC_EHTYPE_id
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackController._detailResponses
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackController._diagnosticsData
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackController._selectedAttachmentsType
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackController._selectedFeedbackCategory
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackDiagnosticsData._creationDateString
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackDiagnosticsData._formMetadata
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackDiagnosticsData._url
+ _OBJC_IVAR_$_WBSAutoplayQuirkWhitelistManager._remotelyUpdatableDataController
+ _OBJC_IVAR_$_WBSBiomeDonationManager._windowProxyStream
+ _OBJC_IVAR_$_WBSBundleTestResults._fileURL
+ _OBJC_IVAR_$_WBSBundleTestResults._internalQueue
+ _OBJC_IVAR_$_WBSBundleTestResults._pendingReports
+ _OBJC_IVAR_$_WBSCalculationResultProvider._calculateRequestLock
+ _OBJC_IVAR_$_WBSCalculationResultProvider._currentCalculateRequest
+ _OBJC_IVAR_$_WBSCompletionListVendorForHistoryService._completionListItemsCallback
+ _OBJC_IVAR_$_WBSCompletionListVendorForHistoryService._dataSource
+ _OBJC_IVAR_$_WBSCompletionListVendorForHistoryService._historyProxy
+ _OBJC_IVAR_$_WBSCompletionListVendorForHistoryService._xpcListener
+ _OBJC_IVAR_$_WBSCreditCardData._balance
+ _OBJC_IVAR_$_WBSDispatchSourceTimer._lock
+ _OBJC_IVAR_$_WBSDispatchSourceTimer._queue
+ _OBJC_IVAR_$_WBSDomainAllowListManager._remotelyUpdatableDataController
+ _OBJC_IVAR_$_WBSFifoTestResults._fifoHandle
+ _OBJC_IVAR_$_WBSFifoTestResults._fifoURL
+ _OBJC_IVAR_$_WBSFifoTestResults._internalQueue
+ _OBJC_IVAR_$_WBSFormControlMetadata._classification
+ _OBJC_IVAR_$_WBSFormControlMetadata._continuationID
+ _OBJC_IVAR_$_WBSFormControlMetadata._continuationIndex
+ _OBJC_IVAR_$_WBSFormTelemetryData._fieldIDToSingleFieldData
+ _OBJC_IVAR_$_WBSFormTelemetryData._formID
+ _OBJC_IVAR_$_WBSFormTelemetryData._formType
+ _OBJC_IVAR_$_WBSFormTelemetryDataMonitor._formIDToFormData
+ _OBJC_IVAR_$_WBSFormTelemetryDataMonitor._webpageLocale
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._attachmentPaths
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._classification
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._component
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._descriptionTemplate
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._keywords
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._reproducibility
+ _OBJC_IVAR_$_WBSInternalFeedbackRadar._title
+ _OBJC_IVAR_$_WBSInternalFeedbackRadarComponent._identifier
+ _OBJC_IVAR_$_WBSInternalFeedbackRadarComponent._name
+ _OBJC_IVAR_$_WBSInternalFeedbackRadarComponent._version
+ _OBJC_IVAR_$_WBSOfflineSearchRemoteDisablementManager._remotelyUpdatableDataController
+ _OBJC_IVAR_$_WBSPageTest._expectedResultsURL
+ _OBJC_IVAR_$_WBSPageTest._identifier
+ _OBJC_IVAR_$_WBSPageTest._pageURL
+ _OBJC_IVAR_$_WBSPageTest._viewportSize
+ _OBJC_IVAR_$_WBSPageTestBundle._allTests
+ _OBJC_IVAR_$_WBSPageTestBundle._identifier
+ _OBJC_IVAR_$_WBSPageTestController._delegate
+ _OBJC_IVAR_$_WBSPasswordBreachConfigurationBagLoader._remotelyUpdatableDataController
+ _OBJC_IVAR_$_WBSSearchParameters._isLabelPreviousSearchesInCompletionListEnabledForTrial
+ _OBJC_IVAR_$_WBSSearchParameters._isProvider1Enabled
+ _OBJC_IVAR_$_WBSSearchParameters._isProvider2Enabled
+ _OBJC_IVAR_$_WBSSearchParameters._isStreamlinedCompletionListEnabledForTrial
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._autoFillOfferedType
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._elementType
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._fieldID
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._fieldType
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._isAutoFilled
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._isManuallyFilledByUser
+ _OBJC_IVAR_$_WBSSingleFieldTelemetryData._modificationType
+ _OBJC_IVAR_$_WBSTestController._internalQueue
+ _OBJC_IVAR_$_WBSTestController._running
+ _OBJC_IVAR_$_WBSTestController._suiteURL
+ _OBJC_IVAR_$_WBSTestController._testBundles
+ _OBJC_IVAR_$_WBSTestResultsReport._dictionaryRepresentation
+ _OBJC_IVAR_$_WBSURLCompletionMatch._alternativeDisplayTextForURL
+ _OBJC_IVAR_$_WBSUserAgentQuirksManager._remotelyUpdatableDataController
+ _OBJC_METACLASS_$_WBSAutoFillInternalFeedbackController
+ _OBJC_METACLASS_$_WBSAutoFillInternalFeedbackDiagnosticsData
+ _OBJC_METACLASS_$_WBSAutoFillTestController
+ _OBJC_METACLASS_$_WBSBundleTestResults
+ _OBJC_METACLASS_$_WBSCompletionListVendorForHistoryService
+ _OBJC_METACLASS_$_WBSFifoTestResults
+ _OBJC_METACLASS_$_WBSFormTelemetryData
+ _OBJC_METACLASS_$_WBSFormTelemetryDataMonitor
+ _OBJC_METACLASS_$_WBSInternalFeedbackRadar
+ _OBJC_METACLASS_$_WBSInternalFeedbackRadarComponent
+ _OBJC_METACLASS_$_WBSPageTest
+ _OBJC_METACLASS_$_WBSPageTestBundle
+ _OBJC_METACLASS_$_WBSPageTestController
+ _OBJC_METACLASS_$_WBSPageTestEvaluator
+ _OBJC_METACLASS_$_WBSSingleFieldTelemetryData
+ _OBJC_METACLASS_$_WBSTestController
+ _OBJC_METACLASS_$_WBSTestResultsReport
+ _TRIAL_enableLabelPreviousSearchesInCompletionList
+ _TRIAL_enableProvider1
+ _TRIAL_enableProvider2
+ _UTTypePlainText
+ _WBSAllowUnsignedExtensionsTimeoutNotification
+ _WBSAuditTokenHasEntitlement
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectDataExpectedFilledData
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectDataIncorrectFields
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectFormatExpectedFormat
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectFormatIncorrectFields
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillFillingFailedUnfilledFieldsExpectingFilling
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillIncorrectlyOfferedFormPurpose
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillIncorrectlyOfferedUnexpectedAutoFillInformationTypes
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillMultipleIssues
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillNotOfferedExpectedAutoFillInformationTypes
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillNotOfferedFormPurpose
+ _WBSAutoFillInternalFeedbackDetailTypeAutoFillOtherIssue
+ _WBSBookmarksDonationDelay
+ _WBSFormMetadataControlClassificationKey
+ _WBSFormMetadataControlContinuationIDKey
+ _WBSFormMetadataControlContinuationIndexKey
+ _WBSFormMetadataControlIsVerticalWritingModeKey
+ _WBSFormMetadataControlLooksLikeEIDFieldKey
+ _WBSFormMetadataControlLooksLikeIMEIFieldKey
+ _WBSIOSDefaultBrowserSelectionStateKey
+ _WBSInitialBookmarksDonationDelay
+ _WBSMinimumLogicalWidthToShowManualAutoFillButton
+ _WBSPageTestErrorDomain
+ _WBSReadExactAmountOfBytesFromFileDescriptor
+ _WBSReadExactAmountOfBytesFromFileDescriptorAsNSData
+ _WBSReaderConfigurationFontFamilyForLanguageTagKey
+ _WBSReaderConfigurationThemeKey
+ _WBSStringFromAutoFillFormType
+ _WBSTimestampForBiomeEventDonation
+ _WBSTrialGroupManagerDidChangeGroupIdentifierNotification
+ _WBSWriteExactAmountOfBytesToFileDescriptor
+ _WBS_LOG_CHANNEL_PREFIXTest
+ _WBS_LOG_CHANNEL_PREFIXTest.log
+ _WBS_LOG_CHANNEL_PREFIXTest.onceToken
+ __OBJC_$_CATEGORY_CKRecord_$_SafariSharedExtras
+ __OBJC_$_CATEGORY_NSString_$_SafariSharedExtras
+ __OBJC_$_CLASS_METHODS_CKRecord(SafariSharedExtras|CloudSettingsExtras)
+ __OBJC_$_CLASS_METHODS_NSString(SafariSharedExtras|ParsecExtras)
+ __OBJC_$_CLASS_METHODS_WBSAutoFillInternalFeedbackController
+ __OBJC_$_CLASS_METHODS_WBSFifoTestResults
+ __OBJC_$_CLASS_METHODS_WBSFormTelemetryDataMonitor
+ __OBJC_$_CLASS_METHODS_WBSInternalFeedbackRadarComponent
+ __OBJC_$_CLASS_METHODS_WBSTestResultsReport
+ __OBJC_$_CLASS_PROP_LIST_WBSAutoFillInternalFeedbackController
+ __OBJC_$_CLASS_PROP_LIST_WBSInternalFeedbackRadarComponent
+ __OBJC_$_INSTANCE_METHODS_CKRecord(SafariSharedExtras|CloudSettingsExtras)
+ __OBJC_$_INSTANCE_METHODS_NSString(SafariSharedExtras|ParsecExtras)
+ __OBJC_$_INSTANCE_METHODS_WBSAutoFillInternalFeedbackController
+ __OBJC_$_INSTANCE_METHODS_WBSAutoFillInternalFeedbackDiagnosticsData
+ __OBJC_$_INSTANCE_METHODS_WBSAutoFillTestController
+ __OBJC_$_INSTANCE_METHODS_WBSBundleTestResults
+ __OBJC_$_INSTANCE_METHODS_WBSCompletionListVendorForHistoryService
+ __OBJC_$_INSTANCE_METHODS_WBSFifoTestResults
+ __OBJC_$_INSTANCE_METHODS_WBSFormTelemetryData
+ __OBJC_$_INSTANCE_METHODS_WBSFormTelemetryDataMonitor
+ __OBJC_$_INSTANCE_METHODS_WBSInternalFeedbackRadar
+ __OBJC_$_INSTANCE_METHODS_WBSInternalFeedbackRadarComponent
+ __OBJC_$_INSTANCE_METHODS_WBSPageTest
+ __OBJC_$_INSTANCE_METHODS_WBSPageTestBundle
+ __OBJC_$_INSTANCE_METHODS_WBSPageTestController
+ __OBJC_$_INSTANCE_METHODS_WBSPageTestEvaluator
+ __OBJC_$_INSTANCE_METHODS_WBSSingleFieldTelemetryData
+ __OBJC_$_INSTANCE_METHODS_WBSTestController
+ __OBJC_$_INSTANCE_METHODS_WBSTestResultsReport
+ __OBJC_$_INSTANCE_VARIABLES_WBSAutoFillInternalFeedbackController
+ __OBJC_$_INSTANCE_VARIABLES_WBSAutoFillInternalFeedbackDiagnosticsData
+ __OBJC_$_INSTANCE_VARIABLES_WBSBundleTestResults
+ __OBJC_$_INSTANCE_VARIABLES_WBSCompletionListVendorForHistoryService
+ __OBJC_$_INSTANCE_VARIABLES_WBSFifoTestResults
+ __OBJC_$_INSTANCE_VARIABLES_WBSFormTelemetryData
+ __OBJC_$_INSTANCE_VARIABLES_WBSFormTelemetryDataMonitor
+ __OBJC_$_INSTANCE_VARIABLES_WBSInternalFeedbackRadar
+ __OBJC_$_INSTANCE_VARIABLES_WBSInternalFeedbackRadarComponent
+ __OBJC_$_INSTANCE_VARIABLES_WBSPageTest
+ __OBJC_$_INSTANCE_VARIABLES_WBSPageTestBundle
+ __OBJC_$_INSTANCE_VARIABLES_WBSPageTestController
+ __OBJC_$_INSTANCE_VARIABLES_WBSSingleFieldTelemetryData
+ __OBJC_$_INSTANCE_VARIABLES_WBSTestController
+ __OBJC_$_INSTANCE_VARIABLES_WBSTestResultsReport
+ __OBJC_$_PROP_LIST_WBSAutoFillInternalFeedbackController
+ __OBJC_$_PROP_LIST_WBSAutoFillInternalFeedbackDiagnosticsData
+ __OBJC_$_PROP_LIST_WBSBiomeDonationManager
+ __OBJC_$_PROP_LIST_WBSBundleTestResults
+ __OBJC_$_PROP_LIST_WBSCompletionListVendorForHistoryService
+ __OBJC_$_PROP_LIST_WBSFifoTestResults
+ __OBJC_$_PROP_LIST_WBSFormTelemetryData
+ __OBJC_$_PROP_LIST_WBSFormTelemetryDataMonitor
+ __OBJC_$_PROP_LIST_WBSInternalFeedbackRadar
+ __OBJC_$_PROP_LIST_WBSInternalFeedbackRadarComponent
+ __OBJC_$_PROP_LIST_WBSPageTest
+ __OBJC_$_PROP_LIST_WBSPageTestBundle
+ __OBJC_$_PROP_LIST_WBSPageTestController
+ __OBJC_$_PROP_LIST_WBSPageTestEvaluator
+ __OBJC_$_PROP_LIST_WBSPerSitePreferenceManager.141
+ __OBJC_$_PROP_LIST_WBSSingleFieldTelemetryData
+ __OBJC_$_PROP_LIST_WBSTest
+ __OBJC_$_PROP_LIST_WBSTestBundle
+ __OBJC_$_PROP_LIST_WBSTestController
+ __OBJC_$_PROP_LIST_WBSTestResultsReport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WBSSearchEnginePreferenceObserverDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSTest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSTestBundle
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSTestResults
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSSearchEnginePreferenceObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSTest
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSTestBundle
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSTestResults
+ __OBJC_$_PROTOCOL_REFS_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_$_PROTOCOL_REFS_WBSSearchEnginePreferenceObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_WBSTest
+ __OBJC_$_PROTOCOL_REFS_WBSTestBundle
+ __OBJC_CLASS_PROTOCOLS_$_WBSBundleTestResults
+ __OBJC_CLASS_PROTOCOLS_$_WBSCompletionListVendorForHistoryService
+ __OBJC_CLASS_PROTOCOLS_$_WBSFifoTestResults
+ __OBJC_CLASS_PROTOCOLS_$_WBSInternalFeedbackRadarComponent
+ __OBJC_CLASS_PROTOCOLS_$_WBSPageTest
+ __OBJC_CLASS_PROTOCOLS_$_WBSPageTestBundle
+ __OBJC_CLASS_RO_$_WBSAutoFillInternalFeedbackController
+ __OBJC_CLASS_RO_$_WBSAutoFillInternalFeedbackDiagnosticsData
+ __OBJC_CLASS_RO_$_WBSAutoFillTestController
+ __OBJC_CLASS_RO_$_WBSBundleTestResults
+ __OBJC_CLASS_RO_$_WBSCompletionListVendorForHistoryService
+ __OBJC_CLASS_RO_$_WBSFifoTestResults
+ __OBJC_CLASS_RO_$_WBSFormTelemetryData
+ __OBJC_CLASS_RO_$_WBSFormTelemetryDataMonitor
+ __OBJC_CLASS_RO_$_WBSInternalFeedbackRadar
+ __OBJC_CLASS_RO_$_WBSInternalFeedbackRadarComponent
+ __OBJC_CLASS_RO_$_WBSPageTest
+ __OBJC_CLASS_RO_$_WBSPageTestBundle
+ __OBJC_CLASS_RO_$_WBSPageTestController
+ __OBJC_CLASS_RO_$_WBSPageTestEvaluator
+ __OBJC_CLASS_RO_$_WBSSingleFieldTelemetryData
+ __OBJC_CLASS_RO_$_WBSTestController
+ __OBJC_CLASS_RO_$_WBSTestResultsReport
+ __OBJC_LABEL_PROTOCOL_$_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_LABEL_PROTOCOL_$_WBSSearchEnginePreferenceObserverDelegate
+ __OBJC_LABEL_PROTOCOL_$_WBSTest
+ __OBJC_LABEL_PROTOCOL_$_WBSTestBundle
+ __OBJC_LABEL_PROTOCOL_$_WBSTestResults
+ __OBJC_METACLASS_RO_$_WBSAutoFillInternalFeedbackController
+ __OBJC_METACLASS_RO_$_WBSAutoFillInternalFeedbackDiagnosticsData
+ __OBJC_METACLASS_RO_$_WBSAutoFillTestController
+ __OBJC_METACLASS_RO_$_WBSBundleTestResults
+ __OBJC_METACLASS_RO_$_WBSCompletionListVendorForHistoryService
+ __OBJC_METACLASS_RO_$_WBSFifoTestResults
+ __OBJC_METACLASS_RO_$_WBSFormTelemetryData
+ __OBJC_METACLASS_RO_$_WBSFormTelemetryDataMonitor
+ __OBJC_METACLASS_RO_$_WBSInternalFeedbackRadar
+ __OBJC_METACLASS_RO_$_WBSInternalFeedbackRadarComponent
+ __OBJC_METACLASS_RO_$_WBSPageTest
+ __OBJC_METACLASS_RO_$_WBSPageTestBundle
+ __OBJC_METACLASS_RO_$_WBSPageTestController
+ __OBJC_METACLASS_RO_$_WBSPageTestEvaluator
+ __OBJC_METACLASS_RO_$_WBSSingleFieldTelemetryData
+ __OBJC_METACLASS_RO_$_WBSTestController
+ __OBJC_METACLASS_RO_$_WBSTestResultsReport
+ __OBJC_PROTOCOL_$_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_PROTOCOL_$_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_PROTOCOL_$_WBSSearchEnginePreferenceObserverDelegate
+ __OBJC_PROTOCOL_$_WBSTest
+ __OBJC_PROTOCOL_$_WBSTestBundle
+ __OBJC_PROTOCOL_$_WBSTestResults
+ __ZGVZN12SafariShared13FrameMetadataC1EPU31objcproto20WBSFormAutoFillFrame11objc_objectP25WBSFormMetadataControllerE20frameMetadataScripts
+ __ZL25canonicalizedDateTemplateP8NSString
+ __ZL26recordTypeForFieldIfFilledP12NSDictionaryP19NSMutableDictionaryIP8NSStringP8NSNumberES3_27WBSSingleCreditCardDataType
+ __ZL33localeForCreditCardExpirationDatev
+ __ZN12SafariShared11JSUtilities21logExceptionInChannelEPU19objcproto9OS_os_log8NSObjectPK15OpaqueJSContextPK13OpaqueJSValue
+ __ZN12SafariShared21URLCompletionEntryMap11recordVisitEP8NSStringS2_db21WBSHistoryVisitOriginbib
+ __ZN12SafariSharedL51jsSpecifierForAutocompleteTokensAndAddressBookLabelEPK15OpaqueJSContextP13OpaqueJSValueS4_mPKPKS3_PS6_
+ __ZN3WTF6VectorItLm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14expandCapacityILNS_13FailureActionE0EEEPtmS6_
+ __ZN3WTF6VectorItLm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE0EEEbm
+ __ZN3WTF6VectorItLm256ENS_15CrashOnOverflowELm16ENS_10FastMallocEE8growImplILNS_13FailureActionE0EEEbm
+ __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8sn170006IP29_WBSSearchSuggestionCandidateNS_16__deque_iteratorIS4_S5_RS4_PS5_lLl170EEELi0EEENS_4pairIT_T0_EESB_SB_SC_
+ __ZNKSt3__114default_deleteIN12SafariShared18URLCompletionEntryEEclB8sn170006EPS2_
+ __ZNKSt3__114default_deleteIN12SafariShared28ReaderAvailabilityController30AvailabilityDetectionSchedulerEEclB8sn170006EPS3_
+ __ZNKSt3__114default_deleteIN12SafariShared33BookmarkAndHistoryCompletionMatchEEclB8sn170006EPS2_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8sn170006IS4_EENS_12basic_stringIcS2_T_EERKS8_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8sn170006Ev
+ __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8sn170006IP29_WBSSearchSuggestionCandidateNS_16__deque_iteratorIS4_S5_RS4_PS5_lLl170EEELi0EEENS_4pairIT_T0_EESB_SB_SC_
+ __ZNSt3__110__pop_heapB8sn170006INS_17_ClassicAlgPolicyEPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SG_RT0_NS_15iterator_traitsISG_E15difference_typeE
+ __ZNSt3__110__pop_heapB8sn170006INS_17_ClassicAlgPolicyEPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SG_RT0_NS_15iterator_traitsISG_E15difference_typeE.cold.1
+ __ZNSt3__110__pop_heapB8sn170006INS_17_ClassicAlgPolicyEU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZNSt3__110unique_ptrIN12SafariShared25SuddenTerminationDisablerENS_14default_deleteIS2_EEE5resetB8sn170006EPS2_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringNS0_IN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB8sn170006EPSD_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringS5_EEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8sn170006EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU6__weakP15WBSHistoryVisitEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8sn170006EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP14WBSHistoryItemEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8sn170006EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP15WBSHistoryVisitEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8sn170006EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP18WBSHistoryTopicTagEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8sn170006EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8sn170006EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeIU8__strongP8NSStringPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEE5resetB8sn170006EPS6_
+ __ZNSt3__110unique_ptrINS_6vectorIN3WTF6RefPtrIN12SafariShared24HistoryURLCompletionItemENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEENS_9allocatorISA_EEEENS_14default_deleteISD_EEE5resetB8sn170006EPSD_
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_Lb0EEEvT1_SH_T0_NS_15iterator_traitsISH_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_Lb0EEEvT1_SA_T0_NS_15iterator_traitsISA_E15difference_typeEb
+ __ZNSt3__111__sift_downB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_OT0_NS_15iterator_traitsISH_E15difference_typeESH_
+ __ZNSt3__111__sift_downB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_OT0_NS_15iterator_traitsISH_E15difference_typeESH_.cold.1
+ __ZNSt3__111__sift_downB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
+ __ZNSt3__112__destroy_atB8sn170006I29_WBSSearchSuggestionCandidateLi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIKxU6__weakP15WBSHistoryVisitEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIKxU8__strongP14WBSHistoryItemEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIKxU8__strongP15WBSHistoryVisitEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIKxU8__strongP18WBSHistoryTopicTagEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIKxU8__strongP8NSStringEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIU8__strongKP8NSStringNS_10unique_ptrIN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006INS_4pairIU8__strongKP8NSStringU8__strongS3_EELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8sn170006IU8__strongP8NSStringLi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8sn170006Emc
+ __ZNSt3__112construct_atB8sn170006I29_WBSSearchSuggestionCandidateJRKS1_EPS1_EEPT_S6_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIKxU6__weakP15WBSHistoryVisitEEJNS1_IxU8__strongS4_EEEPS6_EEPT_SB_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIKxU6__weakP15WBSHistoryVisitEEJRKNS_21piecewise_construct_tENS_5tupleIJRS2_EEENSA_IJEEEEPS6_EEPT_SG_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIKxU8__strongP14WBSHistoryItemEEJNS1_IxS5_EEEPS6_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIKxU8__strongP15WBSHistoryVisitEEJNS1_IxS5_EEEPS6_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIKxU8__strongP8NSStringEEJNS1_IxS5_EEEPS6_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIKxU8__strongP8NSStringEEJRxRS5_EPS6_EEPT_SB_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIU8__strongKP8NSStringNS_10unique_ptrIN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEEJRKNS_21piecewise_construct_tENS_5tupleIJRS4_EEENSF_IJEEEEPSB_EEPT_SL_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIU8__strongKP8NSStringNS_10unique_ptrIN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEEJRU8__strongS3_SA_EPSB_EEPT_SG_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIU8__strongKP8NSStringU8__strongS3_EEJRS4_RS5_EPS6_EEPT_SB_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIU8__strongKP8NSStringU8__strongS3_EEJRS4_S7_EPS6_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB8sn170006INS_4pairIU8__strongKP8NSStringU8__strongS3_EEJS5_S5_EPS6_EEPT_S9_DpOT0_
+ __ZNSt3__112construct_atB8sn170006IU8__strongP40WBSHistoryServiceURLCompletionMatchEntryJRU8__strongKS2_EPS3_EEPT_S8_DpOT0_
+ __ZNSt3__112construct_atB8sn170006IU8__strongP8NSStringJRU8__strongKS2_EPS3_EEPT_S8_DpOT0_
+ __ZNSt3__113__equal_rangeB8sn170006INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPdS5_dNS_10__identityEEENS_4pairIT1_S8_EES8_T2_RKT3_OT0_OT4_
+ __ZNSt3__114__split_bufferIP29_WBSSearchSuggestionCandidateNS_9allocatorIS2_EEE9push_backB8sn170006ERKS2_
+ __ZNSt3__114__split_bufferIP29_WBSSearchSuggestionCandidateRNS_9allocatorIS2_EEE28__construct_at_end_with_sizeINS_13move_iteratorIPS2_EEEEvT_m
+ __ZNSt3__114__split_bufferIP29_WBSSearchSuggestionCandidateRNS_9allocatorIS2_EEE9push_backB8sn170006ERKS2_
+ __ZNSt3__114__split_bufferIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryRNS_9allocatorIS3_EEE28__construct_at_end_with_sizeINS_13move_iteratorIPS3_EEEEvT_m
+ __ZNSt3__114__split_bufferIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryRNS_9allocatorIS3_EEE9push_backB8sn170006ERU8__strongKS2_
+ __ZNSt3__116__deque_iteratorI29_WBSSearchSuggestionCandidatePKS1_RS2_PKS3_lLl170EEpLB8sn170006El
+ __ZNSt3__116__deque_iteratorI29_WBSSearchSuggestionCandidatePS1_RS1_PS2_lLl170EEpLB8sn170006El
+ __ZNSt3__116__insertion_sortB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_
+ __ZNSt3__116__insertion_sortB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_.cold.1
+ __ZNSt3__116__insertion_sortB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_T0_
+ __ZNSt3__116__pad_and_outputB8sn170006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__117__floyd_sift_downB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EET1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE
+ __ZNSt3__117__floyd_sift_downB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8sn170006Ev
+ __ZNSt3__119__allocate_at_leastB8sn170006INS_9allocatorI29_WBSSearchSuggestionCandidateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8sn170006INS_9allocatorIP29_WBSSearchSuggestionCandidateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8sn170006INS_9allocatorIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8sn170006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__partial_sort_implB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_SG_EET1_SH_SH_T2_OT0_
+ __ZNSt3__119__partial_sort_implB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_S9_EET1_SA_SA_T2_OT0_
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__121__unwrap_and_dispatchB8sn170006INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEP29_WBSSearchSuggestionCandidateS8_S8_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
+ __ZNSt3__121__unwrap_and_dispatchB8sn170006INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP40WBSHistoryServiceURLCompletionMatchEntrySA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
+ __ZNSt3__121__unwrap_and_dispatchB8sn170006INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEP29_WBSSearchSuggestionCandidateS8_S8_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
+ __ZNSt3__121__unwrap_and_dispatchB8sn170006INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEPU8__strongP40WBSHistoryServiceURLCompletionMatchEntrySA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
+ __ZNSt3__124__put_character_sequenceB8sn170006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__126__insertion_sort_unguardedB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_
+ __ZNSt3__126__insertion_sort_unguardedB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEbT1_SH_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEbT1_SH_T0_.cold.1
+ __ZNSt3__127__insertion_sort_incompleteB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEbT1_SA_T0_
+ __ZNSt3__131__partition_with_equals_on_leftB8sn170006INS_17_ClassicAlgPolicyEP9SortEntryRU8__strongU13block_pointerFbRKS2_S5_EEET0_SA_SA_T1_
+ __ZNSt3__131__partition_with_equals_on_leftB8sn170006INS_17_ClassicAlgPolicyEPN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEERPFbRKSA_SD_EEET0_SH_SH_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8sn170006INS_17_ClassicAlgPolicyEP9SortEntryRU8__strongU13block_pointerFbRKS2_S5_EEENS_4pairIT0_bEESB_SB_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8sn170006INS_17_ClassicAlgPolicyEPN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEERPFbRKSA_SD_EEENS_4pairIT0_bEESI_SI_T1_
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8sn170006INS_9allocatorIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE18__append_with_sizeB8sn170006INS_16__deque_iteratorIS1_PKS1_RS7_PKS8_lLl170EEEEEvT_m
+ __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE25__maybe_remove_back_spareB8sn170006Eb
+ __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE26__maybe_remove_front_spareB8sn170006Eb
+ __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE8__appendINS_16__deque_iteratorIS1_PKS1_RS7_PKS8_lLl170EEEEEvT_SD_PNS_9enable_ifIXsr31__has_forward_iterator_categoryISD_EE5valueEvE4typeE
+ __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEED2B8sn170006Ev
+ __ZNSt3__16vectorI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE16__destroy_vectorclB8sn170006Ev
+ __ZNSt3__16vectorIN3WTF6RefPtrIN12SafariShared24HistoryURLCompletionItemENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEENS_9allocatorIS9_EEE16__destroy_vectorclB8sn170006Ev
+ __ZNSt3__16vectorIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryNS_9allocatorIS3_EEE16__destroy_vectorclB8sn170006Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8sn170006Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8sn170006IPdS5_EEvT_T0_m
+ __ZNSt3__17__sort3B8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEjT1_SH_SH_T0_
+ __ZNSt3__17__sort3B8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEjT1_SA_SA_T0_
+ __ZNSt3__17__sort4B8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_SH_SH_T0_
+ __ZNSt3__17__sort4B8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort5B8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_SH_SH_SH_T0_
+ __ZNSt3__17__sort5B8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8sn170006IRP9SortEntryS5_EEvOT_OT0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8sn170006IRP9SortEntryS6_EEvOT_OT0_
+ __ZNSt3__19__sift_upB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE
+ __ZNSt3__19__sift_upB8sn170006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE.cold.1
+ __ZNSt3__19__sift_upB8sn170006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8sn170006v
+ __ZZL26updateCachedArraysIfNeededvE14haveLoadedData
+ __ZZL33localeForCreditCardExpirationDatevE33localeForCreditCardExpirationDate
+ __ZZL33localeForCreditCardExpirationDatevE4once
+ __ZZN12SafariShared13FrameMetadataC1EPU31objcproto20WBSFormAutoFillFrame11objc_objectP25WBSFormMetadataControllerE20frameMetadataScripts
+ ___106-[WBSCloudHistory _updateHistoryAfterSuccessfulPersistedLongLivedSaveOperationWithGenerations:completion:]_block_invoke.200
+ ___106-[WBSCloudHistory _updateHistoryAfterSuccessfulPersistedLongLivedSaveOperationWithGenerations:completion:]_block_invoke.200.cold.1
+ ___108-[WBSCreditCardDataController sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledVirtualCardData:]_block_invoke
+ ___108-[WBSCreditCardDataController sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledVirtualCardData:]_block_invoke.cold.1
+ ___108-[WBSCreditCardDataController tellWalletThatExistingCardWasFilledInForm:previouslyFilledVirtualCardNumbers:]_block_invoke
+ ___110-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.133
+ ___110-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.133.cold.1
+ ___122-[WBSHistoryServiceURLCompletion recordVisit:sourceVisit:title:loadSuccessful:origin:increaseVisitCount:score:statusCode:]_block_invoke
+ ___126-[WBSFifoTestResults reportActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:]_block_invoke
+ ___128-[WBSBundleTestResults reportActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:]_block_invoke
+ ___133-[WBSSiriIntelligenceDonor _donateHistoryItemsToCoreSpotlightCreatedAfterDate:beforeDate:historiesForProfiles:withCompletionHandler:]_block_invoke.141
+ ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.135
+ ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.135.cold.1
+ ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.136
+ ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.136.cold.1
+ ___179-[WBSFormDataController _matchesForControl:inDomain:matchingPartialString:autoFillDataType:preferredLabel:contact:allowingIdentifiedAddressBookLabelToOverridePreferredIdentifier:]_block_invoke
+ ___28-[WBSTestController bundles]_block_invoke
+ ___41-[WBSBundleTestResults endTest:inBundle:]_block_invoke
+ ___41-[WBSBundleTestResults endTest:inBundle:]_block_invoke.cold.1
+ ___41-[WBSBundleTestResults endTest:inBundle:]_block_invoke.cold.2
+ ___41-[WBSBundleTestResults endTest:inBundle:]_block_invoke_2
+ ___43-[WBSTrialManager fetchFactorsInNamespace:]_block_invoke
+ ___44-[WBSFifoTestResults initWithFifoURL:error:]_block_invoke
+ ___44-[WBSFifoTestResults initWithFifoURL:error:]_block_invoke.cold.1
+ ___46+[WBSInternalFeedbackRadarComponent safariIOS]_block_invoke
+ ___50+[WBSInternalFeedbackRadarComponent safariNewBugs]_block_invoke
+ ___50-[WBSTestController initWithSuiteURL:bundleNames:]_block_invoke
+ ___50-[WBSTestController initWithSuiteURL:bundleNames:]_block_invoke_2
+ ___50-[WBSTestController initWithSuiteURL:bundleNames:]_block_invoke_3
+ ___50-[WBSTestController initWithSuiteURL:bundleNames:]_block_invoke_4
+ ___51+[WBSInternalFeedbackRadarComponent safariAutoFill]_block_invoke
+ ___52-[WBSCompletionListVendorForHistoryService _connect]_block_invoke
+ ___52-[WBSCompletionListVendorForHistoryService _connect]_block_invoke.cold.1
+ ___53-[WBSCloudHistory _deleteAllCloudHistoryAndSaveAgain]_block_invoke.180
+ ___53-[WBSCloudHistory _deleteAllCloudHistoryAndSaveAgain]_block_invoke_2.181
+ ___53-[WBSCloudHistory _deleteAllCloudHistoryAndSaveAgain]_block_invoke_3.182
+ ___53-[WBSCloudHistory _initializePushNotificationSupport]_block_invoke.206
+ ___53-[WBSCloudHistory _pcsIdentitiesChangedNotification:]_block_invoke.163
+ ___54-[WBSCloudHistory _fetchAddedProfileLocalIdentifiers:]_block_invoke.221
+ ___54-[WBSCloudHistory _fetchAddedProfileLocalIdentifiers:]_block_invoke_2.223
+ ___55+[WBSInternalFeedbackRadarComponent passwordManagerIOS]_block_invoke
+ ___55+[WBSInternalFeedbackRadarComponent safariStartPageIOS]_block_invoke
+ ___55-[WBSSearchParameters initWithTrial:forPrefs:forTrial:]_block_invoke
+ ___56-[WBSBiomeDonationManager _clearEventsDonatedSinceDate:]_block_invoke_6
+ ___57+[WBSInternalFeedbackRadarComponent safariStartPageMacOS]_block_invoke
+ ___57-[WBSUserAgentQuirksSnapshot initWithSnapshotData:error:]_block_invoke
+ ___60-[WBSFifoTestResults reportError:forStage:forTest:inBundle:]_block_invoke
+ ___62-[WBSBundleTestResults reportError:forStage:forTest:inBundle:]_block_invoke
+ ___63-[WBSFormTelemetryDataMonitor _sendUsageTelemetryEventsPerForm]_block_invoke
+ ___63-[WBSFormTelemetryDataMonitor _sendUsageTelemetryEventsPerForm]_block_invoke_2
+ ___64-[WBSAutoFillInternalFeedbackController canContinueInTapToRadar]_block_invoke
+ ___64-[WBSAutoFillInternalFeedbackController continueInTapToRadarURL]_block_invoke
+ ___64-[WBSAutoplayQuirkWhitelistSnapshot initWithSnapshotData:error:]_block_invoke
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_10
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_11
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_12
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_2
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_3
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_4
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_5
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_6
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_7
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_8
+ ___64-[WBSTestController _runTestsAndStoreResultsIn:completionBlock:]_block_invoke_9
+ ___65-[WBSTestController runTestsAndStoreResultsIn:completionHandler:]_block_invoke
+ ___65-[WBSTestController runTestsAndStoreResultsIn:completionHandler:]_block_invoke.10
+ ___65-[WBSTestController runTestsAndStoreResultsIn:completionHandler:]_block_invoke.cold.1
+ ___65-[WBSTestController runTestsAndStoreResultsIn:completionHandler:]_block_invoke_2
+ ___66-[WBSFifoTestResults reportPerformance:forStage:forTest:inBundle:]_block_invoke
+ ___68-[WBSBundleTestResults reportPerformance:forStage:forTest:inBundle:]_block_invoke
+ ___68-[WBSCloudHistory _replayPersistedLongLivedSaveOperationIfNecessary]_block_invoke.199
+ ___68-[WBSFormMetadata dictionaryRepresentationRedactingSensitiveValues:]_block_invoke
+ ___69-[WBSSiriIntelligenceDonor _indexedIDsForSearchQueryString:outError:]_block_invoke
+ ___69-[WBSSiriIntelligenceDonor _indexedIDsForSearchQueryString:outError:]_block_invoke_2
+ ___69-[WBSSiriIntelligenceDonor _indexedIDsForSearchQueryString:outError:]_block_invoke_3
+ ___70-[WBSFormTelemetryDataMonitor _sendModificationTelemetryEventsPerForm]_block_invoke
+ ___70-[WBSFormTelemetryDataMonitor _sendModificationTelemetryEventsPerForm]_block_invoke_2
+ ___70-[WBSPageZoomPreferenceManager resetZoomLevelOnURL:completionHandler:]_block_invoke_2.cold.1
+ ___70-[WBSPageZoomPreferenceManager resetZoomLevelOnURL:completionHandler:]_block_invoke_2.cold.2
+ ___70-[WBSSiriIntelligenceDonor _indexCoreSpotlightData:completionHandler:]_block_invoke.147
+ ___72+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]_block_invoke.52
+ ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke.175
+ ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke.177
+ ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke.177.cold.1
+ ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke_2.176
+ ___75-[WBSFormTelemetryDataMonitor _sendModificationTelemetryEventsPerFormField]_block_invoke
+ ___75-[WBSFormTelemetryDataMonitor _sendModificationTelemetryEventsPerFormField]_block_invoke_2
+ ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke.153
+ ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke.156
+ ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke_2.155
+ ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke_2.157
+ ___77-[WBSHistory addTagWithIdentifier:title:toItemAtURL:level:completionHandler:]_block_invoke.66
+ ___77-[WBSHistory addTagWithIdentifier:title:toItemAtURL:level:completionHandler:]_block_invoke.66.cold.1
+ ___77-[WBSHistory addTagWithIdentifier:title:toItemAtURL:level:completionHandler:]_block_invoke.66.cold.2
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.183
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.186
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.189
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.189.cold.1
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.191
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_2.184
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_2.187
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_3.185
+ ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_3.188
+ ___80-[WBSAutoFillInternalFeedbackDiagnosticsData writeTemporaryFileWithFormMetadata]_block_invoke
+ ___83-[WBSCloudHistory getVisitsAndTombstonesNeedingSyncWithVisitSyncWindow:completion:]_block_invoke.147
+ ___83-[WBSCloudHistory getVisitsAndTombstonesNeedingSyncWithVisitSyncWindow:completion:]_block_invoke.147.cold.1
+ ___85-[WBSPerSitePreferenceManager getValueOfPreference:forDomain:withTimeout:usingBlock:]_block_invoke.23
+ ___85-[WBSPerSitePreferenceManager getValueOfPreference:forDomain:withTimeout:usingBlock:]_block_invoke_2.cold.1
+ ___85-[WBSPerSitePreferenceManager getValueOfPreference:forDomain:withTimeout:usingBlock:]_block_invoke_2.cold.2
+ ___85-[WBSPerSitePreferenceManager getValueOfPreference:forDomain:withTimeout:usingBlock:]_block_invoke_2.cold.3
+ ___86-[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]_block_invoke
+ ___86-[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]_block_invoke.11
+ ___86-[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]_block_invoke.7
+ ___86-[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]_block_invoke_2
+ ___86-[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]_block_invoke_2.cold.1
+ ___86-[WBSAutoFillTestController runTest:bundle:storeResultsIn:tryCount:completionHandler:]_block_invoke_2.cold.2
+ ___86-[WBSPageZoomPreferenceManager _incrementOrDecreaseZoomStep:forURL:completionHandler:]_block_invoke_4.cold.1
+ ___87-[WBSCloudHistory _determineNumberOfDevicesInSyncCircleForOperation:completionHandler:]_block_invoke.213
+ ___91-[WBSCreditCardDataController isVirtualCard:previouslyFilledVirtualCardNumbers:completion:]_block_invoke
+ ___WBS_LOG_CHANNEL_PREFIXTest_block_invoke
+ ____ZL33localeForCreditCardExpirationDatev_block_invoke
+ ____ZN12SafariShared21URLCompletionEntryMap11recordVisitEP8NSStringS2_db21WBSHistoryVisitOriginbib_block_invoke
+ ___block_descriptor_128_e8_32s40r48r56r64r72r80r88r96r104r112r120r_e54_v32?0"NSString"8"WBSSingleFieldTelemetryData"16^B24lr40l8s32l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8
+ ___block_descriptor_32_e31_q24?0"NSBundle"8"NSBundle"16l
+ ___block_descriptor_32_e35_"NSNumber"32?0"NSObject"8Q16^B24l
+ ___block_descriptor_32_e44_"NSDictionary"16?0"WBSTestResultsReport"8l
+ ___block_descriptor_32_e46_"NSMutableDictionary"16?0"WBSFormMetadata"8l
+ ___block_descriptor_33_e46_"NSDictionary"16?0"WBSFormControlMetadata"8l
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e28_"NSBundle"16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e35_"<WBSTestBundle>"16?0"NSBundle"8ls32l8
+ ___block_descriptor_40_e8_32s_e47_v32?0"NSNumber"8"WBSFormTelemetryData"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e23_v32?0q8q16"NSError"24ls32l8
+ ___block_descriptor_40_ea8_32s_e36_v16?0"WBSSavedAccountMatchResult"8ls32l8
+ ___block_descriptor_40_ea8_32w_e11_v24?0q8q16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e8_v16?0q8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e38_v32?0"<WBSTestBundle>"8Q16?<v?B>24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e49_v24?0"WBSSiriIntelligenceDonorHistoryData"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e53_v32?0"WBSSiriIntelligenceDonorBookmarkData"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e54_v32?0"NSString"8"WBSSingleFieldTelemetryData"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e56_"WBSStartPageSectionDescriptor"32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e32_v32?0"<WBSTest>"8Q16?<v?B>24ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e17_v16?0"NSError"8lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e17_v16?0"NSError"8lr72l8s32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_86_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32r40r48r56r64r72r80r_e54_v32?0"NSString"8"WBSSingleFieldTelemetryData"16^B24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e48_v24?0"<WBSFormsMetadataProvider>"8"NSError"16ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.103
+ ___block_literal_global.111
+ ___block_literal_global.132
+ ___block_literal_global.139
+ ___block_literal_global.149
+ ___block_literal_global.162
+ ___block_literal_global.186
+ ___block_literal_global.189
+ ___block_literal_global.195
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.216
+ ___block_literal_global.219
+ ___block_literal_global.225
+ ___block_literal_global.229
+ ___block_literal_global.44
+ ___block_literal_global.455
+ ___block_literal_global.478
+ ___block_literal_global.481
+ ___block_literal_global.483
+ ___block_literal_global.485
+ ___block_literal_global.487
+ ___block_literal_global.492
+ ___block_literal_global.71
+ __unnamed_array_storage.111
+ __unnamed_array_storage.219
+ __unnamed_array_storage.256
+ __unnamed_array_storage.268
+ __unnamed_array_storage.285
+ __unnamed_array_storage.342
+ __unnamed_array_storage.366
+ __unnamed_array_storage.441
+ __unnamed_array_storage.477
+ _appendToQueryItems
+ _coreSpotlightBookmarksDonationIdentifier
+ _formMetadataClassificationSource
+ _formMetadataClassificationSourceLength
+ _mkfifo
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLByDeletingPathExtension
+ _objc_msgSend$URLWithString:relativeToURL:
+ _objc_msgSend$_connect
+ _objc_msgSend$_elementTypeForFormControlMetadata:
+ _objc_msgSend$_historyItemIdentifierForURLString:profileIdentifier:
+ _objc_msgSend$_indexedIDsForSearchQueryString:outError:
+ _objc_msgSend$_isMonitoringTextFieldWithID:forFormID:
+ _objc_msgSend$_radarTitleComponentForDetails
+ _objc_msgSend$_runTestsAndStoreResultsIn:completionBlock:
+ _objc_msgSend$_sendModificationTelemetryEventsPerForm
+ _objc_msgSend$_sendModificationTelemetryEventsPerFormField
+ _objc_msgSend$_sendUsageTelemetryEventsPerForm
+ _objc_msgSend$_setExportedInterfaceAndObjectForConnection:
+ _objc_msgSend$_updateAutoFillOfferedType:forTextFieldWithID:forFormID:
+ _objc_msgSend$_updateMonitorDataWithFormMetadata:
+ _objc_msgSend$_updateMonitorDataWithTextFieldMetadata:textFieldValueLength:forFormID:
+ _objc_msgSend$_updateTelemetryFieldData:withTextFieldMetadata:textFieldValueLength:
+ _objc_msgSend$_wasAutoFillUsedForModificationType:
+ _objc_msgSend$_weightedRandomIdentifier
+ _objc_msgSend$_windowProxyStream
+ _objc_msgSend$_writeReportToFifo:
+ _objc_msgSend$allTests
+ _objc_msgSend$amount
+ _objc_msgSend$auditToken
+ _objc_msgSend$autoFillOfferedType
+ _objc_msgSend$autoFilledField:inForm:inFrame:
+ _objc_msgSend$autoFilledField:inFrame:
+ _objc_msgSend$balance
+ _objc_msgSend$beginTest:inBundle:
+ _objc_msgSend$browserTabCompletionProvider:alternativeDisplayTextForURLForExtensionURL:
+ _objc_msgSend$browserTabCompletionProvider:doesURLRepresentNativeContent:
+ _objc_msgSend$browserTabCompletionProvider:shouldExtensionURLAppearAsSwitchToTabItem:
+ _objc_msgSend$bundleFromNSBundle:
+ _objc_msgSend$bundleType
+ _objc_msgSend$bundleURL
+ _objc_msgSend$cleanBundle:completionHandler:
+ _objc_msgSend$cleanSuiteWithCompletionHandler:
+ _objc_msgSend$cleanTest:bundle:completionHandler:
+ _objc_msgSend$continueInTapToRadarURL
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$creationDateString
+ _objc_msgSend$credentialTypes
+ _objc_msgSend$currentDevice
+ _objc_msgSend$defaultSearchEngineMatchesExperiment
+ _objc_msgSend$detailTypesForSelectedFeedbackCategory
+ _objc_msgSend$determineAccountStateWithCompletion:
+ _objc_msgSend$deviceClass
+ _objc_msgSend$diagnosticsData
+ _objc_msgSend$dictionaryRepresentationRedactingSensitiveValues:
+ _objc_msgSend$didSubmitFormOfType:withFieldType:elementType:isAutoFilled:isManuallyFilledByUser:modificationType:autoFillOfferedType:webpageLocale:
+ _objc_msgSend$didSubmitFormOfType:withPerFormModificationsDictionary:webpageLocale:
+ _objc_msgSend$didSubmitFormOfType:withPerFormUsageDictionary:webpageLocale:
+ _objc_msgSend$displayablePANSuffix
+ _objc_msgSend$elementType
+ _objc_msgSend$endTest:inBundle:
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$expectedResultsPathExtension
+ _objc_msgSend$expectedResultsURL
+ _objc_msgSend$fieldIDToSingleFieldData
+ _objc_msgSend$fieldType
+ _objc_msgSend$fileHandleForWritingToURL:error:
+ _objc_msgSend$formFieldTypeForFormControlMetadata:formMetadata:
+ _objc_msgSend$formMetadata
+ _objc_msgSend$formType
+ _objc_msgSend$initWithComponent:title:descriptionTemplate:
+ _objc_msgSend$initWithContentsOfURL:options:error:
+ _objc_msgSend$initWithDataFormat:builtInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:
+ _objc_msgSend$initWithFieldType:fieldID:elementType:
+ _objc_msgSend$initWithFormType:formID:
+ _objc_msgSend$initWithIdentifier:name:version:
+ _objc_msgSend$initWithIdentifier:pageURL:expectedResultsURL:dictionary:
+ _objc_msgSend$initWithIdentifier:tests:
+ _objc_msgSend$initWithSnapshotData:error:
+ _objc_msgSend$initWithStartDelay:interval:repeats:queue:handler:
+ _objc_msgSend$initWithTabInfo:userTypedString:alternativeDisplayTextForURL:forQueryID:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$isAutoFilled
+ _objc_msgSend$isCardBalanceZeroOrNegative
+ _objc_msgSend$isFieldUnidentified:
+ _objc_msgSend$isLabelPreviousSearchesInCompletionListEnabled
+ _objc_msgSend$isManuallyFilledByUser
+ _objc_msgSend$isVerticalWritingMode
+ _objc_msgSend$isVirtualCard:previouslyFilledVirtualCardNumbers:completion:
+ _objc_msgSend$matchesForPasswordAutoFill
+ _objc_msgSend$modificationType
+ _objc_msgSend$pageTestController:navigateAndCaptureFormsMetadataForURL:completionHandler:
+ _objc_msgSend$pageTestController:resizeViewport:completionHandler:
+ _objc_msgSend$pageTestControllerInitializeApp:completionHandler:
+ _objc_msgSend$pageTestControllerTerminateApp:
+ _objc_msgSend$prepareBundle:completionHandler:
+ _objc_msgSend$prepareSuiteWithCompletionHandler:
+ _objc_msgSend$prepareTest:bundle:completionHandler:
+ _objc_msgSend$recordVisit:sourceVisit:title:loadSuccessful:origin:increaseVisitCount:score:statusCode:
+ _objc_msgSend$removeAllCoreSpotlightHistoryDataDonatedBySafariForProfileWithIdentifier:
+ _objc_msgSend$reportActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:
+ _objc_msgSend$reportError:forStage:forTest:inBundle:
+ _objc_msgSend$reportForActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:
+ _objc_msgSend$reportForError:forStage:forTest:inBundle:
+ _objc_msgSend$reportForPerformance:forStage:forTest:inBundle:
+ _objc_msgSend$reportPerformance:forStage:forTest:inBundle:
+ _objc_msgSend$runTest:bundle:storeResultsIn:completionHandler:
+ _objc_msgSend$runTest:bundle:storeResultsIn:tryCount:completionHandler:
+ _objc_msgSend$safariAutoFill
+ _objc_msgSend$safariStartPageIOS
+ _objc_msgSend$safari_allObjectsPassTest:
+ _objc_msgSend$safari_bundlesFromDirectory:bundleType:
+ _objc_msgSend$safari_filenameFormattedString
+ _objc_msgSend$safari_isSafariExtensionURL
+ _objc_msgSend$safari_looksLikeEmailAddress
+ _objc_msgSend$savedAccount
+ _objc_msgSend$setAlternativeDisplayTextForURL:
+ _objc_msgSend$setAttachmentPaths:
+ _objc_msgSend$setAutoFillOfferedType:
+ _objc_msgSend$setClassification:
+ _objc_msgSend$setFieldIDToSingleFieldData:
+ _objc_msgSend$setFieldType:
+ _objc_msgSend$setIsAutoFilled:
+ _objc_msgSend$setIsManuallyFilledByUser:
+ _objc_msgSend$setKeywords:
+ _objc_msgSend$setModificationType:
+ _objc_msgSend$setReproducibility:
+ _objc_msgSend$setZoneID:
+ _objc_msgSend$stringRepresentationFromMetadataProvider:
+ _objc_msgSend$textFieldLooksLikeCreditCardFormField:inForm:
+ _objc_msgSend$timerWithInterval:repeats:queue:handler:
+ _objc_msgSend$userInterfaceIdiom
+ _objc_msgSend$version
+ _objc_msgSend$viewportSize
+ _objc_msgSend$wasPreviouslyAutoFilled
+ _objc_msgSend$writeTemporaryFileWithFormMetadata
+ _objc_msgSend$writeToURL:options:error:
+ _objc_msgSend$zero
+ _os_unfair_lock_assert_owner
+ _passwordManagerIOS.component
+ _passwordManagerIOS.onceToken
+ _random
+ _safariAutoFill.component
+ _safariAutoFill.onceToken
+ _safariIOS.component
+ _safariIOS.onceToken
+ _safariNewBugs.component
+ _safariNewBugs.onceToken
+ _safariStartPageIOS.component
+ _safariStartPageIOS.onceToken
+ _safariStartPageMacOS.component
+ _safariStartPageMacOS.onceToken
+ _titleForFeedbackDetailType
- +[WBSSiriIntelligenceDonor _historyItemIdentifierForURLString:]
- +[WBSSiriIntelligenceDonor historyItemIdentifierForURL:]
- -[WBSAutoplayQuirkWhitelistSnapshot initWithPlistData:error:]
- -[WBSAutoplayQuirkWhitelistSnapshot plistDataWithFormat:]
- -[WBSBrowserTabCompletionMatch initWithTabInfo:userTypedString:forQueryID:]
- -[WBSCreditCardDataController isVirtualCard:lastFilledCardData:completion:]
- -[WBSCreditCardDataController sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledCardData:]
- -[WBSCreditCardDataController tellWalletThatExistingCardWasFilledInForm:lastFilledCardData:]
- -[WBSCyclerTabsTestSuite _relativeProbabilitiesForOperationsWithNoMovableTabs]
- -[WBSDispatchSourceTimer _initWithStartDelay:interval:repeats:handler:]
- -[WBSDomainAllowListSnapshot initWithPlistData:error:]
- -[WBSDomainAllowListSnapshot plistDataWithFormat:]
- -[WBSGeolocationPreferenceManager setDefaultGeolocationSetting:]
- -[WBSHistoryServiceURLCompletion recordVisit:sourceVisit:title:loadSuccessful:visitWasFromThisDevice:increaseVisitCount:score:statusCode:]
- -[WBSOfflineSearchRemoteDisablementSnapshot initWithPlistData:error:]
- -[WBSOfflineSearchRemoteDisablementSnapshot initWithPlistData:error:].cold.1
- -[WBSOfflineSearchRemoteDisablementSnapshot plistDataWithFormat:]
- -[WBSPasswordBreachConfigurationBag initWithPlistData:error:]
- -[WBSPasswordBreachConfigurationBag initWithPlistData:error:].cold.1
- -[WBSPasswordBreachConfigurationBag plistDataWithFormat:]
- -[WBSRadarNewProblemURLBuilder .cxx_destruct]
- -[WBSRadarNewProblemURLBuilder attachmentURLs]
- -[WBSRadarNewProblemURLBuilder classification]
- -[WBSRadarNewProblemURLBuilder componentName]
- -[WBSRadarNewProblemURLBuilder componentVersion]
- -[WBSRadarNewProblemURLBuilder descriptionText]
- -[WBSRadarNewProblemURLBuilder setAttachmentURLs:]
- -[WBSRadarNewProblemURLBuilder setClassification:]
- -[WBSRadarNewProblemURLBuilder setComponentName:]
- -[WBSRadarNewProblemURLBuilder setComponentVersion:]
- -[WBSRadarNewProblemURLBuilder setDescriptionText:]
- -[WBSRadarNewProblemURLBuilder setTitle:]
- -[WBSRadarNewProblemURLBuilder title]
- -[WBSRadarNewProblemURLBuilder url]
- -[WBSSearchParameters isMoreSearchProviderSuggestionsEnabled]
- -[WBSSearchParameters isReflectUserIntentInSearchEnabled]
- -[WBSSearchParameters isResponsiveCompletionListEnabled]
- -[WBSSearchParameters setIsMoreSearchProviderSuggestionsEnabled:]
- -[WBSSearchParameters setIsReflectUserIntentInSearchEnabled:]
- -[WBSSearchParameters setIsResponsiveCompletionListEnabled:]
- -[WBSSearchParameters setIsStreamlinedCompletionListEnabled:]
- -[WBSSiriIntelligenceDonor _contentDescriptionForURL:]
- -[WBSSiriIntelligenceDonor processRemovedHistoryItems:]
- -[WBSSiriIntelligenceDonorHistoryData setVisitCount:]
- -[WBSSiriIntelligenceDonorHistoryData visitCount]
- -[WBSUserAgentQuirksSnapshot initWithPlistData:error:]
- -[WBSUserAgentQuirksSnapshot plistDataWithFormat:]
- GCC_except_table173
- GCC_except_table289
- _MGGetSInt32Answer
- _NSFileProtectionCompleteUntilFirstUserAuthentication
- _OBJC_CLASS_$_CSCustomAttributeKey
- _OBJC_CLASS_$_WBSRadarNewProblemURLBuilder
- _OBJC_CLASS_$_WBSRecentlyBreachedSavedPasswordProvider
- _OBJC_CLASS_$_WBSRemotePlistController
- _OBJC_IVAR_$_WBSAutoplayQuirkWhitelistManager._remotePlistController
- _OBJC_IVAR_$_WBSBiomeDonationManager._streamAccessQueue
- _OBJC_IVAR_$_WBSDomainAllowListManager._remotePlistController
- _OBJC_IVAR_$_WBSOfflineSearchRemoteDisablementManager._remotePlistController
- _OBJC_IVAR_$_WBSPasswordBreachConfigurationBagLoader._remotePlistController
- _OBJC_IVAR_$_WBSRadarNewProblemURLBuilder._attachmentURLs
- _OBJC_IVAR_$_WBSRadarNewProblemURLBuilder._classification
- _OBJC_IVAR_$_WBSRadarNewProblemURLBuilder._componentName
- _OBJC_IVAR_$_WBSRadarNewProblemURLBuilder._componentVersion
- _OBJC_IVAR_$_WBSRadarNewProblemURLBuilder._descriptionText
- _OBJC_IVAR_$_WBSRadarNewProblemURLBuilder._title
- _OBJC_IVAR_$_WBSSearchParameters._isMoreSearchProviderSuggestionsEnabled
- _OBJC_IVAR_$_WBSSearchParameters._isReflectUserIntentInSearchEnabled
- _OBJC_IVAR_$_WBSSearchParameters._isResponsiveCompletionListEnabled
- _OBJC_IVAR_$_WBSSearchParameters._isStreamlinedCompletionListEnabled
- _OBJC_IVAR_$_WBSSiriIntelligenceDonorHistoryData._visitCount
- _OBJC_IVAR_$_WBSUserAgentQuirksManager._remotePlistController
- _OBJC_METACLASS_$_WBSRadarNewProblemURLBuilder
- _OBJC_METACLASS_$_WBSRecentlyBreachedSavedPasswordProvider
- _WBSDeviceUDID
- _WBSDeviceUDID.deviceUDID
- _WBSDeviceUDID.onceToken
- _WBSMinimumWidthToShowManualAutoFillButton
- __OBJC_$_CATEGORY_CKRecord_$_CloudSettingsExtras
- __OBJC_$_CATEGORY_NSString_$_ParsecExtras
- __OBJC_$_CLASS_METHODS_CKRecord(CloudSettingsExtras|SafariSharedExtras)
- __OBJC_$_CLASS_METHODS_NSString(ParsecExtras|SafariSharedExtras)
- __OBJC_$_INSTANCE_METHODS_CKRecord(CloudSettingsExtras|SafariSharedExtras)
- __OBJC_$_INSTANCE_METHODS_NSString(ParsecExtras|SafariSharedExtras)
- __OBJC_$_INSTANCE_METHODS_WBSRadarNewProblemURLBuilder
- __OBJC_$_INSTANCE_VARIABLES_WBSRadarNewProblemURLBuilder
- __OBJC_$_PROP_LIST_WBSPerSitePreferenceManager.139
- __OBJC_$_PROP_LIST_WBSRadarNewProblemURLBuilder
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WBSRemotePlistControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSRemotePlistSnapshot
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotePlistControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotePlistSnapshot
- __OBJC_$_PROTOCOL_REFS_WBSRemotePlistControllerDelegate
- __OBJC_$_PROTOCOL_REFS_WBSRemotePlistSnapshot
- __OBJC_CLASS_RO_$_WBSRadarNewProblemURLBuilder
- __OBJC_CLASS_RO_$_WBSRecentlyBreachedSavedPasswordProvider
- __OBJC_LABEL_PROTOCOL_$_WBSRemotePlistControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_WBSRemotePlistSnapshot
- __OBJC_METACLASS_RO_$_WBSRadarNewProblemURLBuilder
- __OBJC_METACLASS_RO_$_WBSRecentlyBreachedSavedPasswordProvider
- __OBJC_PROTOCOL_$_WBSRemotePlistControllerDelegate
- __OBJC_PROTOCOL_$_WBSRemotePlistSnapshot
- __ZGVZ41+[WBSReaderResources readerHTMLSourceURL]E19readerSourcePathURL
- __ZGVZ47+[WBSReaderResources sharedUIScriptForContext:]E14sharedUIScript
- __ZL39writeExactAmountOfBytesToFileDescriptoriPKvm
- __ZL39writeExactAmountOfBytesToFileDescriptoriPKvm.cold.1
- __ZL40readExactAmountOfBytesFromFileDescriptoriPvm
- __ZN12SafariShared21URLCompletionEntryMap11recordVisitEP8NSStringS2_dbbbib
- __ZN3WTF6VectorItLm256ENS_15CrashOnOverflowELm16ENS_10FastMallocEE4growEm
- __ZNKSt3__114default_deleteIN12SafariShared18URLCompletionEntryEEclB7v160006EPS2_
- __ZNKSt3__114default_deleteIN12SafariShared28ReaderAvailabilityController30AvailabilityDetectionSchedulerEEclB7v160006EPS3_
- __ZNKSt3__114default_deleteIN12SafariShared33BookmarkAndHistoryCompletionMatchEEclB7v160006EPS2_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__110__pop_heapB7v160006INS_17_ClassicAlgPolicyEPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SG_RT0_NS_15iterator_traitsISG_E15difference_typeE
- __ZNSt3__110__pop_heapB7v160006INS_17_ClassicAlgPolicyEPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SG_RT0_NS_15iterator_traitsISG_E15difference_typeE.cold.1
- __ZNSt3__110__pop_heapB7v160006INS_17_ClassicAlgPolicyEU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZNSt3__110unique_ptrIN12SafariShared25SuddenTerminationDisablerENS_14default_deleteIS2_EEE5resetB7v160006EPS2_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringNS0_IN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB7v160006EPSD_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringS5_EEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU6__weakP15WBSHistoryVisitEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP14WBSHistoryItemEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP15WBSHistoryVisitEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP18WBSHistoryTopicTagEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB7v160006EPS8_
- __ZNSt3__110unique_ptrINS_11__hash_nodeIU8__strongP8NSStringPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEE5resetB7v160006EPS6_
- __ZNSt3__110unique_ptrINS_6vectorIN3WTF6RefPtrIN12SafariShared24HistoryURLCompletionItemENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEENS_9allocatorISA_EEEENS_14default_deleteISD_EEE5resetB7v160006EPSD_
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_NS_15iterator_traitsISH_E15difference_typeE
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_T0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB7v160006IP29_WBSSearchSuggestionCandidateNS_16__deque_iteratorIS4_S5_RS4_PS5_lLl170EEELi0EEENS_4pairIT_T0_EESB_SB_SC_
- __ZNSt3__111__sift_downB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_OT0_NS_15iterator_traitsISH_E15difference_typeESH_
- __ZNSt3__111__sift_downB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_OT0_NS_15iterator_traitsISH_E15difference_typeESH_.cold.1
- __ZNSt3__111__sift_downB7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
- __ZNSt3__112__destroy_atB7v160006I29_WBSSearchSuggestionCandidateLi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKxU6__weakP15WBSHistoryVisitEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKxU8__strongP14WBSHistoryItemEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKxU8__strongP15WBSHistoryVisitEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKxU8__strongP18WBSHistoryTopicTagEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIKxU8__strongP8NSStringEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIU8__strongKP8NSStringNS_10unique_ptrIN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006INS_4pairIU8__strongKP8NSStringU8__strongS3_EELi0EEEvPT_
- __ZNSt3__112__destroy_atB7v160006IU8__strongP8NSStringLi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006Emc
- __ZNSt3__112construct_atB7v160006I29_WBSSearchSuggestionCandidateJRKS1_EPS1_EEPT_S6_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIKxU6__weakP15WBSHistoryVisitEEJNS1_IxU8__strongS4_EEEPS6_EEPT_SB_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIKxU6__weakP15WBSHistoryVisitEEJRKNS_21piecewise_construct_tENS_5tupleIJRS2_EEENSA_IJEEEEPS6_EEPT_SG_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIKxU8__strongP14WBSHistoryItemEEJNS1_IxS5_EEEPS6_EEPT_SA_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIKxU8__strongP15WBSHistoryVisitEEJNS1_IxS5_EEEPS6_EEPT_SA_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIKxU8__strongP8NSStringEEJNS1_IxS5_EEEPS6_EEPT_SA_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIKxU8__strongP8NSStringEEJRxRS5_EPS6_EEPT_SB_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIU8__strongKP8NSStringNS_10unique_ptrIN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEEJRKNS_21piecewise_construct_tENS_5tupleIJRS4_EEENSF_IJEEEEPSB_EEPT_SL_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIU8__strongKP8NSStringNS_10unique_ptrIN12SafariShared24URLCompletionEntryExtrasENS_14default_deleteIS7_EEEEEEJRU8__strongS3_SA_EPSB_EEPT_SG_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIU8__strongKP8NSStringU8__strongS3_EEJRS4_RS5_EPS6_EEPT_SB_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIU8__strongKP8NSStringU8__strongS3_EEJRS4_S7_EPS6_EEPT_SA_DpOT0_
- __ZNSt3__112construct_atB7v160006INS_4pairIU8__strongKP8NSStringU8__strongS3_EEJS5_S5_EPS6_EEPT_S9_DpOT0_
- __ZNSt3__112construct_atB7v160006IU8__strongP40WBSHistoryServiceURLCompletionMatchEntryJRU8__strongKS2_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__112construct_atB7v160006IU8__strongP8NSStringJRU8__strongKS2_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__113__equal_rangeB7v160006INS_17_ClassicAlgPolicyERNS_6__lessIddEEPdS5_dNS_10__identityEEENS_4pairIT1_S8_EES8_T2_RKT3_OT0_OT4_
- __ZNSt3__114__split_bufferIP29_WBSSearchSuggestionCandidateNS_9allocatorIS2_EEE9push_backB7v160006ERKS2_
- __ZNSt3__114__split_bufferIP29_WBSSearchSuggestionCandidateRNS_9allocatorIS2_EEE18__construct_at_endINS_13move_iteratorIPS2_EEEENS_9enable_ifIXsr27__is_cpp17_forward_iteratorIT_EE5valueEvE4typeESC_SC_
- __ZNSt3__114__split_bufferIP29_WBSSearchSuggestionCandidateRNS_9allocatorIS2_EEE9push_backB7v160006ERKS2_
- __ZNSt3__114__split_bufferIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryRNS_9allocatorIS3_EEE18__construct_at_endINS_13move_iteratorIPS3_EEEENS_9enable_ifIXsr27__is_cpp17_forward_iteratorIT_EE5valueEvE4typeESD_SD_
- __ZNSt3__114__split_bufferIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryRNS_9allocatorIS3_EEE9push_backB7v160006ERU8__strongKS2_
- __ZNSt3__116__deque_iteratorI29_WBSSearchSuggestionCandidatePKS1_RS2_PKS3_lLl170EEpLB7v160006El
- __ZNSt3__116__deque_iteratorI29_WBSSearchSuggestionCandidatePS1_RS1_PS2_lLl170EEpLB7v160006El
- __ZNSt3__116__pad_and_outputB7v160006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__117__floyd_sift_downB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EET1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE
- __ZNSt3__117__floyd_sift_downB7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__118__insertion_sort_3B7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_
- __ZNSt3__118__insertion_sort_3B7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_T0_.cold.1
- __ZNSt3__118__insertion_sort_3B7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_T0_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI29_WBSSearchSuggestionCandidateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP29_WBSSearchSuggestionCandidateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__partial_sort_implB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_SG_EET1_SH_SH_T2_OT0_
- __ZNSt3__119__partial_sort_implB7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_S9_EET1_SA_SA_T2_OT0_
- __ZNSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB7v160006IP29_WBSSearchSuggestionCandidateNS_16__deque_iteratorIS4_S5_RS4_PS5_lLl170EEELi0EEENS_4pairIT_T0_EESB_SB_SC_
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEP29_WBSSearchSuggestionCandidateS8_S8_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP40WBSHistoryServiceURLCompletionMatchEntrySA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEP29_WBSSearchSuggestionCandidateS8_S8_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEPU8__strongP40WBSHistoryServiceURLCompletionMatchEntrySA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__124__put_character_sequenceB7v160006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__insertion_sort_incompleteIRPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESB_EPS9_EEbT0_SG_T_
- __ZNSt3__127__insertion_sort_incompleteIRPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESB_EPS9_EEbT0_SG_T_.cold.1
- __ZNSt3__127__insertion_sort_incompleteIRU8__strongU13block_pointerFbRK9SortEntryS3_EPS1_EEbT0_S9_T_
- __ZNSt3__130__uninitialized_allocator_copyB7v160006INS_9allocatorIdEEPdS3_S3_EET2_RT_T0_T1_S4_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE25__maybe_remove_back_spareB7v160006Eb
- __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE26__maybe_remove_front_spareB7v160006Eb
- __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE8__appendINS_16__deque_iteratorIS1_PKS1_RS7_PKS8_lLl170EEEEEvT_SD_PNS_9enable_ifIXsr27__is_cpp17_forward_iteratorISD_EE5valueEvE4typeE
- __ZNSt3__15dequeI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEED2B7v160006Ev
- __ZNSt3__16vectorI29_WBSSearchSuggestionCandidateNS_9allocatorIS1_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIN3WTF6RefPtrIN12SafariShared24HistoryURLCompletionItemENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEENS_9allocatorIS9_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIU8__strongP40WBSHistoryServiceURLCompletionMatchEntryNS_9allocatorIS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2ERKS3_
- __ZNSt3__17__sort3B7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEjT1_SH_SH_T0_
- __ZNSt3__17__sort3B7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEjT1_SA_SA_T0_
- __ZNSt3__17__sort4B7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEjT1_SH_SH_SH_T0_
- __ZNSt3__17__sort4B7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEjT1_SA_SA_SA_T0_
- __ZNSt3__17__sort5IRPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS1_12RawPtrTraitsIS4_EENS1_21DefaultRefDerefTraitsIS4_EEEESB_EPS9_EEjT0_SG_SG_SG_SG_T_
- __ZNSt3__17__sort5IRU8__strongU13block_pointerFbRK9SortEntryS3_EPS1_EEjT0_S9_S9_S9_S9_T_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB7v160006IRP9SortEntryS6_EEvOT_OT0_
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyERPFbRKN3WTF6RefPtrIN12SafariShared33BookmarkAndHistoryCompletionMatchENS2_12RawPtrTraitsIS5_EENS2_21DefaultRefDerefTraitsIS5_EEEESC_EPSA_EEvT1_SH_OT0_NS_15iterator_traitsISH_E15difference_typeE.cold.1
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyERU8__strongU13block_pointerFbRK9SortEntryS4_EPS2_EEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__1L19piecewise_constructE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- __ZZL26updateCachedArraysIfNeededvE14haveReadPlists
- __ZZN12SafariShared13FrameMetadataC1EPU31objcproto20WBSFormAutoFillFrame11objc_objectP25WBSFormMetadataControllerE14autoFillScript
- __ZZN12SafariShared13FrameMetadataC1EPU31objcproto20WBSFormAutoFillFrame11objc_objectP25WBSFormMetadataControllerE24automaticPasswordsScript
- ___101-[WBSCreditCardDataController sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledCardData:]_block_invoke
- ___101-[WBSCreditCardDataController sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledCardData:]_block_invoke.cold.1
- ___106-[WBSCloudHistory _updateHistoryAfterSuccessfulPersistedLongLivedSaveOperationWithGenerations:completion:]_block_invoke.202
- ___106-[WBSCloudHistory _updateHistoryAfterSuccessfulPersistedLongLivedSaveOperationWithGenerations:completion:]_block_invoke.202.cold.1
- ___110-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.139
- ___110-[WBSSiriIntelligenceDonor reindexAllBookmarkAndHistoryItems:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.139.cold.1
- ___133-[WBSSiriIntelligenceDonor _donateHistoryItemsToCoreSpotlightCreatedAfterDate:beforeDate:historiesForProfiles:withCompletionHandler:]_block_invoke.147
- ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.141
- ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.141.cold.1
- ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.142
- ___135-[WBSSiriIntelligenceDonor reindexBookmarkAndHistoryItemsWithIdentifiers:allBookmarks:historiesForProfiles:withAcknowledgementHandler:]_block_invoke.142.cold.1
- ___138-[WBSHistoryServiceURLCompletion recordVisit:sourceVisit:title:loadSuccessful:visitWasFromThisDevice:increaseVisitCount:score:statusCode:]_block_invoke
- ___35-[WBSRadarNewProblemURLBuilder url]_block_invoke
- ___43-[WBSFormMetadata dictionaryRepresentation]_block_invoke
- ___49-[WBSSiriIntelligenceDonor _indexedBookmarksIDs:]_block_invoke
- ___49-[WBSSiriIntelligenceDonor _indexedBookmarksIDs:]_block_invoke_2
- ___49-[WBSSiriIntelligenceDonor _indexedBookmarksIDs:]_block_invoke_3
- ___53-[WBSCloudHistory _deleteAllCloudHistoryAndSaveAgain]_block_invoke.181
- ___53-[WBSCloudHistory _deleteAllCloudHistoryAndSaveAgain]_block_invoke_2.182
- ___53-[WBSCloudHistory _deleteAllCloudHistoryAndSaveAgain]_block_invoke_3.183
- ___53-[WBSCloudHistory _initializePushNotificationSupport]_block_invoke.207
- ___53-[WBSCloudHistory _pcsIdentitiesChangedNotification:]_block_invoke.164
- ___54-[WBSCloudHistory _fetchAddedProfileLocalIdentifiers:]_block_invoke.222
- ___54-[WBSCloudHistory _fetchAddedProfileLocalIdentifiers:]_block_invoke_2.224
- ___54-[WBSUserAgentQuirksSnapshot initWithPlistData:error:]_block_invoke
- ___61-[WBSAutoplayQuirkWhitelistSnapshot initWithPlistData:error:]_block_invoke
- ___68-[WBSCloudHistory _replayPersistedLongLivedSaveOperationIfNecessary]_block_invoke.200
- ___70-[WBSSiriIntelligenceDonor _indexCoreSpotlightData:completionHandler:]_block_invoke.154
- ___72+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]_block_invoke.25
- ___72-[WBSProfileDataManager didRemoveProfileWithServerID:profileIdentifier:]_block_invoke
- ___72-[WBSProfileDataManager didRemoveProfileWithServerID:profileIdentifier:]_block_invoke.cold.1
- ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke.176
- ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke.178.cold.1
- ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke.179
- ___73-[WBSCloudHistory _transitionCloudHistoryStoreToManateeState:completion:]_block_invoke_2.177
- ___75-[WBSCreditCardDataController isVirtualCard:lastFilledCardData:completion:]_block_invoke
- ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke.155
- ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke.157
- ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke_2.156
- ___76-[WBSCloudHistory fetchAndMergeChangesBypassingThrottler:completionHandler:]_block_invoke_2.158
- ___77-[WBSHistory addTagWithIdentifier:title:toItemAtURL:level:completionHandler:]_block_invoke.67
- ___77-[WBSHistory addTagWithIdentifier:title:toItemAtURL:level:completionHandler:]_block_invoke.67.cold.1
- ___77-[WBSHistory addTagWithIdentifier:title:toItemAtURL:level:completionHandler:]_block_invoke.67.cold.2
- ___78-[WBSCyclerTabsTestSuite _relativeProbabilitiesForOperationsWithNoMovableTabs]_block_invoke
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.184
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.187
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.190
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.190.cold.1
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke.192
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_2.185
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_2.188
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_3.186
- ___79-[WBSCloudHistory _fetchAndMergeChangesWithServerChangeTokenData:withPriority:]_block_invoke_3.189
- ___83-[WBSCloudHistory getVisitsAndTombstonesNeedingSyncWithVisitSyncWindow:completion:]_block_invoke.148
- ___83-[WBSCloudHistory getVisitsAndTombstonesNeedingSyncWithVisitSyncWindow:completion:]_block_invoke.148.cold.1
- ___85-[WBSPerSitePreferenceManager getValueOfPreference:forDomain:withTimeout:usingBlock:]_block_invoke_3
- ___87-[WBSCloudHistory _determineNumberOfDevicesInSyncCircleForOperation:completionHandler:]_block_invoke.214
- ___92-[WBSCreditCardDataController tellWalletThatExistingCardWasFilledInForm:lastFilledCardData:]_block_invoke
- ___WBSDeviceUDID_block_invoke
- ____ZN12SafariShared21URLCompletionEntryMap11recordVisitEP8NSStringS2_dbbbib_block_invoke
- ___block_descriptor_32_e31_"NSNumber"24?0"NSObject"8Q16l
- ___block_descriptor_32_e46_"NSDictionary"16?0"WBSFormControlMetadata"8l
- ___block_descriptor_40_e8_32s_e53_v32?0"WBSSiriIntelligenceDonorBookmarkData"8Q16^B24ls32l8
- ___block_descriptor_40_ea8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_descriptor_40_ea8_32w_e8_v16?0q8lw32l8
- ___block_descriptor_48_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_48_e8_32s40s_e52_"WBSStartPageSectionDescriptor"24?0"NSString"8Q16ls32l8s40l8
- ___block_descriptor_56_e8_32bs40w_e8_v12?0B8ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48s_e49_v24?0"WBSSiriIntelligenceDonorHistoryData"8^B16ls32l8s40l8s48l8
- ___block_descriptor_79_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.106
- ___block_literal_global.119
- ___block_literal_global.127
- ___block_literal_global.137
- ___block_literal_global.138
- ___block_literal_global.157
- ___block_literal_global.163
- ___block_literal_global.185
- ___block_literal_global.188
- ___block_literal_global.196
- ___block_literal_global.204
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.230
- ___block_literal_global.233
- ___block_literal_global.419
- ___block_literal_global.441
- ___block_literal_global.444
- ___block_literal_global.446
- ___block_literal_global.448
- ___block_literal_global.450
- ___block_literal_global.5
- ___block_literal_global.52
- ___block_literal_global.69
- __relativeProbabilitiesForOperationsWithNoMovableTabs.onceToken
- __relativeProbabilitiesForOperationsWithNoMovableTabs.relativeProbabilitiesForOperations
- __unnamed_array_storage.101
- __unnamed_array_storage.189
- __unnamed_array_storage.225
- __unnamed_array_storage.236
- __unnamed_array_storage.246
- __unnamed_array_storage.248
- __unnamed_array_storage.267
- __unnamed_array_storage.28
- __unnamed_array_storage.297
- __unnamed_array_storage.333
- __unnamed_array_storage.577
- __unnamed_array_storage.604
- _coreSpotlightPageVisitCountKey
- _objc_msgSend$FPANSuffix
- _objc_msgSend$_contentDescriptionForURL:
- _objc_msgSend$_historyItemIdentifierForURLString:
- _objc_msgSend$_initWithStartDelay:interval:repeats:handler:
- _objc_msgSend$_relativeProbabilitiesForOperationsWithNoMovableTabs
- _objc_msgSend$deleteSearchableItemsWithDomainIdentifiers:protectionClass:forBundleID:options:completionHandler:
- _objc_msgSend$determineManateeStateWithCompletion:
- _objc_msgSend$initWithBuiltInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:
- _objc_msgSend$initWithKeyName:searchable:searchableByDefault:unique:multiValued:
- _objc_msgSend$initWithPlistData:error:
- _objc_msgSend$initWithTabInfo:userTypedString:forQueryID:
- _objc_msgSend$isVirtualCard:lastFilledCardData:completion:
- _objc_msgSend$recordVisit:sourceVisit:title:loadSuccessful:visitWasFromThisDevice:increaseVisitCount:score:statusCode:
- _objc_msgSend$setComponentName:
- _objc_msgSend$setComponentVersion:
- _objc_msgSend$setDescriptionText:
- _objc_msgSend$setValue:forCustomKey:
- _read
- _write
CStrings:
+ "\t"
+ "\tg\xb9R\x1fgP\x96"
+ "\x0f\x04"
+ "\x11\x13"
+ "\x112"
+ "\x18"
+ "\x1c\x0e9\x0eI\x0e\x16\x0e7\x0e-\x0e\x1a\x0e1\x0e\x15\x0e#\x0e"
+ " * %@"
+ "#\x0e+\x0e1\x0e*\x0e#\x0e1\x0e\x01\x0e)\x0e2\x0e\x04\x0e'\x0e2\x0e!\x0e\x1b\x0e%\x0e-\x0e\x14\x0e \x0e1\x0e\"\x0e\x1a\x0e1\x0e\x15\x0e#\x0e"
+ "%@\n"
+ "%@ %@"
+ "%@_%@.plist"
+ "%s:%d: assertion %s failed: %s\n"
+ "'\x0e1\x0e\x19\x0e+\x0e!\x0e\x14\x0e-\x0e2\x0e\"\x0e8\x0e"
+ "(?=\"flags\"{?=\"disallowsAutocomplete\"b1\"claimsToBeCurrentPasswordViaAutocompleteAttribute\"b1\"claimsToBeNewPasswordViaAutocompleteAttribute\"b1\"claimsToBeUsernameViaAutocompleteAttribute\"b1\"looksLikeCreditCardCardholderField\"b1\"looksLikeCreditCardCompositeExpirationDateField\"b1\"looksLikeCreditCardNumberField\"b1\"looksLikeCreditCardSecurityCodeField\"b1\"looksLikeCreditCardTypeField\"b1\"looksLikeEIDField\"b1\"looksLikeIMEIField\"b1\"looksLikeDayField\"b1\"looksLikeMonthField\"b1\"looksLikeYearField\"b1\"looksLikeIgnoredDataTypeField\"b1\"looksLikePasswordCredentialField\"b1\"looksLikeOneTimeCodeField\"b1\"oneTimeCodeIsEligibleForAutomaticLogin\"b1\"visible\"b1\"active\"b1\"disabled\"b1\"readOnly\"b1\"textField\"b1\"secureTextField\"b1\"autoFilledTextField\"b1\"userEditedTextField\"b1\"labeledUsernameField\"b1\"verticalWritingMode\"b1}\"asInteger\"q)"
+ "(New Bugs)"
+ "(__end - __begin) >= 0"
+ "+\x0e!\x0e2\x0e\"\x0e@\x0e%\x0e\x02\x0e\x1a\x0e1\x0e\x15\x0e#\x0e@\x0e\x04\x0e#\x0e\x14\x0e4\x0e\x15\x0e"
+ "-expected"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__hash_table"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/deque"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/string_view"
+ "/AppleInternal/Library/BuildRoots/b96130be-d2c4-11ee-8194-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/vector"
+ "1118801"
+ "1175764"
+ "144485"
+ "1549076"
+ "1723108"
+ "1723110"
+ "1723112"
+ "1723114"
+ "1723116"
+ "1723118"
+ "1723120"
+ "224849"
+ "4"
+ "5"
+ "567407"
+ "6"
+ "=\x04>\x04<\x045\x04@\x04 "
+ "@\"<WBSCompletionListVendorForHistoryServiceDataSource>\""
+ "@\"<WBSPageTestDelegate>\""
+ "@\"<WBSTestBundle>\"16@?0@\"NSBundle\"8"
+ "@\"CalculateRequest\""
+ "@\"NSBundle\"16@?0@\"NSString\"8"
+ "@\"NSData\"16@0:8"
+ "@\"NSDictionary\"16@?0@\"WBSTestResultsReport\"8"
+ "@\"NSMutableDictionary\"16@?0@\"WBSFormMetadata\"8"
+ "@\"NSNumber\"32@?0@\"NSObject\"8Q16^B24"
+ "@\"PKCurrencyAmount\""
+ "@\"WBSAutoFillInternalFeedbackDiagnosticsData\""
+ "@\"WBSInternalFeedbackRadarComponent\""
+ "@\"WBSRemotelyUpdatableDataController\""
+ "@\"WBSStartPageSectionDescriptor\"32@?0@\"NSString\"8Q16^B24"
+ "@32@0:8Q16q24"
+ "@40@0:8q16@24Q32"
+ "@44@0:8d16B24@28@?36"
+ "@52@0:8d16d24B32@36@?44"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "A\x04@\x04>\x04:\x04 "
+ "AllowUnsignedExtensionsTimeoutNotification"
+ "Apple will store and use this feedback including the URL and optionally the contents of this webpage, to improve AutoFill."
+ "Attachments"
+ "AutoFill failed to fill fields"
+ "AutoFill failed to fill fields (e.g. missing credit card expiration date)"
+ "AutoFill filled the wrong format of data"
+ "AutoFill filled the wrong format of data (e.g. filled a data as MM/DD instead of DD-MM)"
+ "AutoFill filled the wrong type of data"
+ "AutoFill filled the wrong type of data (e.g. zip code in a phone number field)"
+ "AutoFill was unexpectedly offered"
+ "AutoFill wasn't offered"
+ "AutomaticPassword.js"
+ "B24@0:8@\"WBSRemotelyUpdatableDataController\"16"
+ "B24@0:8@\"WBSSearchEnginePreferenceObserver\"16"
+ "B32@0:8@16^@24"
+ "B32@0:8@16q24"
+ "Can't open fifo %{public}@: %{public}@"
+ "CardType"
+ "Checking page zoom per site preference from storage"
+ "Checking page zoom per site preference from storage for domain '%{private}@'"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Condition"
+ "ControlClassification"
+ "ControlContinuationID"
+ "ControlContinuationIndex"
+ "ControlIsVerticalWritingMode"
+ "ControlLooksLikeEIDField"
+ "ControlLooksLikeIMEIField"
+ "Description"
+ "Diagnostics collection was triggered at %@"
+ "Encountered error generating JSON data with form metadata: %{public}@"
+ "Encountered error writing temporary file with form metadata: %{public}@"
+ "Error has been detected for test %{public}@/%{public}@. Retrying."
+ "Error sending completion list endpoint to history service: %{public}@"
+ "Excluding duplicate match with same title and host"
+ "Excluding duplicate top hit"
+ "Excluding unlikely match due to client or server error"
+ "Excluding unlikely match due to nil match value"
+ "Expectations"
+ "Expected a string for addressBookLabel."
+ "Expected an array of autocomplete tokens."
+ "Expected autocomplete token to be a string."
+ "Expected two arguments, autocompleteTokens and addressBookLabel."
+ "Expected: %@"
+ "ExpectedResults"
+ "FIFO is not connected"
+ "Failed to create script %{public}s: line %i: %{public}@"
+ "Failed to fetch per site preference with identifier '%{public}@' from SQLiteStore"
+ "Failed to parse predicate '%{public}@': %{public}@"
+ "Failed to serialize report"
+ "Failed to serialize reports: %{private}@"
+ "Failed to update SQLiteStore for page zoom per site preferences due to database not open or statement not done"
+ "Failed to write reports: %{private}@"
+ "Fields: %@"
+ "Form metadata attached."
+ "FormMetadata.js"
+ "FormMetadataClassification.js"
+ "FormMetadataClassificationJS"
+ "Invalid Modification Type"
+ "JavaScript Exception: %@\n(%@:%d)\n%@"
+ "Keywords"
+ "Loading website with page zoom factor: %f"
+ "Multiple issues"
+ "No issue"
+ "Not Applicable"
+ "OneTimeCodeFieldLabels"
+ "Other issue"
+ "Page Contents (Report AutoFill Issue, Internal Only)"
+ "Password Manager"
+ "Please describe each issue you had, including what AutoFill did and how that differed from the expected result."
+ "Report AutoFill Issue [Internal Only] (Report AutoFill Issue, Internal Only)"
+ "Reproducibility"
+ "SQLiteStore deletion failed for page zoom per site preferences"
+ "SQLiteStore deletion failed for page zoom per site preferences for domain %{private}@"
+ "Safari AutoFill"
+ "Safari AutoFill [in-app feedback]: %@ on %@ (%@)"
+ "Safari was unable to attach form metadata for this issue."
+ "SecurityCode"
+ "Serious Bug"
+ "Skipping bundle '%{public}@' because they contained no runnable tests for current device"
+ "Skipping expectation '%{public}@' because the current device didn't meet the condition '%{public}@'"
+ "Successfully sent completion list endpoint to history service."
+ "T@\"<WBSCompletionListVendorForHistoryServiceDataSource>\",R,W,N,V_dataSource"
+ "T@\"<WBSPageTestDelegate>\",W,V_delegate"
+ "T@\"NSArray\",C,N,V_attachmentPaths"
+ "T@\"NSArray\",C,N,V_formMetadata"
+ "T@\"NSArray\",C,N,V_keywords"
+ "T@\"NSArray\",R,N,V_allTests"
+ "T@\"NSDictionary\",C,N,V_fieldIDToSingleFieldData"
+ "T@\"NSDictionary\",R,C,N,V_dictionaryRepresentation"
+ "T@\"NSFileHandle\",R,N,V_fifoHandle"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSOrderedSet\",R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,C,N,V_uuidString"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSString\",C,N,V_alternativeDisplayTextForURL"
+ "T@\"NSString\",C,N,V_classification"
+ "T@\"NSString\",C,N,V_descriptionTemplate"
+ "T@\"NSString\",C,N,V_reproducibility"
+ "T@\"NSString\",R,C,N,V_classification"
+ "T@\"NSString\",R,C,N,V_creationDateString"
+ "T@\"NSString\",R,C,N,V_version"
+ "T@\"NSString\",R,C,N,V_webpageLocale"
+ "T@\"NSURL\",R,N,V_expectedResultsURL"
+ "T@\"NSURL\",R,N,V_fifoURL"
+ "T@\"NSURL\",R,N,V_fileURL"
+ "T@\"NSURL\",R,N,V_pageURL"
+ "T@\"NSURL\",R,N,V_suiteURL"
+ "T@\"PKCurrencyAmount\",R,N,V_balance"
+ "T@\"WBSAutoFillInternalFeedbackDiagnosticsData\",R,C,N,V_diagnosticsData"
+ "T@\"WBSCyclerIterationCounter\",?,&,N"
+ "T@\"WBSCyclerIterationCounter\",?,&,N,V_iterationCounter"
+ "T@\"WBSInternalFeedbackRadarComponent\",C,N,V_component"
+ "T@\"WBSInternalFeedbackRadarComponent\",R,C,N"
+ "T@\"WBSQuerySuggestion\",?,&,N"
+ "T@\"_WBSBiomeStream\",R,N"
+ "TB,?,R,N"
+ "TB,?,R,N,GisFinished"
+ "TB,?,R,N,GisFinished,V_finished"
+ "TB,D,N,GisVerticalWritingMode"
+ "TB,N,V_isAutoFilled"
+ "TB,N,V_isLabelPreviousSearchesInCompletionListEnabledForTrial"
+ "TB,N,V_isManuallyFilledByUser"
+ "TB,N,V_isStreamlinedCompletionListEnabledForTrial"
+ "TB,R,N,GisVerticalWritingMode"
+ "TEXTAREA"
+ "TQ,N,V_autoFillOfferedType"
+ "TQ,N,V_modificationType"
+ "TQ,N,V_selectedAttachmentsType"
+ "TQ,N,V_selectedFeedbackCategory"
+ "TQ,R,N,V_elementType"
+ "TQ,R,N,V_formType"
+ "Test"
+ "Test %{public}@/%{public}@ expected and actual results differed. Retrying."
+ "Test %{public}@/%{public}@ reported error: %{public}@"
+ "Test for '%{public}@' is required to specify an expected result files"
+ "Test for '%{public}@' is required to specify identifiers"
+ "Test suite is already running"
+ "TestPages"
+ "The URL (%@) will be included in the report. When selected, the contents of the page may contain sensitive information like your username, but does not include information filled into form fields by you or Safari."
+ "The completion list vendor has rejected an incoming connection due to missing entitlements."
+ "Timed out fetching per site preference with identifier '%{public}@' from SQLiteStore"
+ "Too many consecutive errors for test %{public}@/%{public}@. Failing."
+ "Tq,?,R,N"
+ "Tq,N,V_fieldType"
+ "Tq,R,N,V_formID"
+ "T{CGSize=dd},R,N,V_viewportSize"
+ "UIDevice"
+ "URL only (Report AutoFill Issue, Internal Only)"
+ "URLByAppendingPathExtension:"
+ "URLByDeletingPathExtension"
+ "URLWithString:relativeToURL:"
+ "Unable to recognize value from the tag. Deleting preference value for this domain from memory"
+ "Unexpected: %@"
+ "Updating website with page zoom factor: %f"
+ "ViewportHeight"
+ "ViewportWidth"
+ "WBSAutoFillFormTypeAutoFillableLogin"
+ "WBSAutoFillFormTypeAutoFillableStandard"
+ "WBSAutoFillFormTypeChangePassword"
+ "WBSAutoFillFormTypeNewAccount"
+ "WBSAutoFillFormTypeNonAutoFillable"
+ "WBSAutoFillFormTypeUndetermined"
+ "WBSAutoFillInternalFeedbackController"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectDataExpectedFilledData"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectDataIncorrectFields"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectFormatExpectedFormat"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillFilledIncorrectFormatIncorrectFields"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillFillingFailedUnfilledFieldsExpectingFilling"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillIncorrectlyOfferedFormPurpose"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillIncorrectlyOfferedUnexpectedAutoFillInformationTypes"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillMultipleIssues"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillNotOfferedExpectedAutoFillInformationTypes"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillNotOfferedFormPurpose"
+ "WBSAutoFillInternalFeedbackDetailTypeAutoFillOtherIssue"
+ "WBSAutoFillInternalFeedbackDiagnosticsData"
+ "WBSAutoFillTestController"
+ "WBSBundleTestResults"
+ "WBSCompletionListVendorForHistoryService"
+ "WBSFifoTestResults"
+ "WBSFormTelemetryData"
+ "WBSFormTelemetryDataMonitor"
+ "WBSInternalFeedbackRadar"
+ "WBSInternalFeedbackRadarComponent"
+ "WBSPageTest"
+ "WBSPageTestBundle"
+ "WBSPageTestController"
+ "WBSPageTestErrorDomain"
+ "WBSPageTestEvaluator"
+ "WBSRemotelyUpdatableDataControllerDelegate"
+ "WBSRemotelyUpdatableDataSnapshot"
+ "WBSSearchEnginePreferenceObserverDelegate"
+ "WBSSingleFieldTelemetryData"
+ "WBSTest"
+ "WBSTestBundle"
+ "WBSTestController"
+ "WBSTestResults"
+ "WBSTestResultsReport"
+ "WeakOneTimeCodeFieldLabels"
+ "WebArchiveFileName"
+ "What format was the form expecting, and what format was filled?"
+ "What happened and how did that differ from the expected result?"
+ "What is the purpose of the form where AutoFill was incorrectly offered?"
+ "What type of information was filled and what type of information did you expect to be filled?"
+ "What type(s) of information did you expect to be available for AutoFill in the form?"
+ "What type(s) of information were offered to be filled and why is this unexpected?"
+ "Which fields did you expect to be filled that were not?"
+ "Which fields had data incorrectly formatted?"
+ "Which fields had incorrect information filled?"
+ "Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?"
+ "__first != __end"
+ "__k != __leftmost"
+ "__last != __begin"
+ "__last - __first >= difference_type(3)"
+ "__s2 < __s1 || __s2 >= __s1 + __n"
+ "_allTests"
+ "_alternativeDisplayTextForURL"
+ "_attachmentPaths"
+ "_autoFillOfferedType"
+ "_balance"
+ "_calculateRequestLock"
+ "_completionListItemsCallback"
+ "_component"
+ "_connect"
+ "_continuationID"
+ "_continuationIndex"
+ "_creationDateString"
+ "_currentCalculateRequest"
+ "_descriptionTemplate"
+ "_detailResponses"
+ "_diagnosticsData"
+ "_elementType"
+ "_elementTypeForFormControlMetadata:"
+ "_expectedResultsURL"
+ "_fieldIDToSingleFieldData"
+ "_fieldType"
+ "_fifoHandle"
+ "_fifoURL"
+ "_fileURL"
+ "_formID"
+ "_formIDToFormData"
+ "_formType"
+ "_historyItemIdentifierForURLString:profileIdentifier:"
+ "_historyProxy"
+ "_indexedIDsForSearchQueryString:outError:"
+ "_isAutoFilled"
+ "_isLabelPreviousSearchesInCompletionListEnabledForTrial"
+ "_isManuallyFilledByUser"
+ "_isMonitoringTextFieldWithID:forFormID:"
+ "_isProvider1Enabled"
+ "_isProvider2Enabled"
+ "_isStreamlinedCompletionListEnabledForTrial"
+ "_keywords"
+ "_modificationType"
+ "_pendingReports"
+ "_radarTitleComponentForDetails"
+ "_remotelyUpdatableDataController"
+ "_reproducibility"
+ "_runTestsAndStoreResultsIn:completionBlock:"
+ "_selectedAttachmentsType"
+ "_selectedFeedbackCategory"
+ "_sendModificationTelemetryEventsPerForm"
+ "_sendModificationTelemetryEventsPerFormField"
+ "_sendUsageTelemetryEventsPerForm"
+ "_setExportedInterfaceAndObjectForConnection:"
+ "_suiteURL"
+ "_testBundles"
+ "_updateAutoFillOfferedType:forTextFieldWithID:forFormID:"
+ "_updateMonitorDataWithFormMetadata:"
+ "_updateMonitorDataWithTextFieldMetadata:textFieldValueLength:forFormID:"
+ "_updateTelemetryFieldData:withTextFieldMetadata:textFieldValueLength:"
+ "_version"
+ "_viewportSize"
+ "_wasAutoFillUsedForModificationType:"
+ "_webpageLocale"
+ "_weightedRandomIdentifier"
+ "_windowProxyStream"
+ "_writeReportToFifo:"
+ "actualResults"
+ "allTests"
+ "alternativeDisplayTextForURL"
+ "amount"
+ "app-distribution"
+ "attachmentDetailsText"
+ "attachmentPaths"
+ "autoFillOfferedType"
+ "autoFilledField:inForm:inFrame:"
+ "autoFilledField:inFrame:"
+ "autofilltest"
+ "balance"
+ "beginTest:inBundle:"
+ "browserTabCompletionProvider:alternativeDisplayTextForURLForExtensionURL:"
+ "browserTabCompletionProvider:doesURLRepresentNativeContent:"
+ "browserTabCompletionProvider:shouldExtensionURLAppearAsSwitchToTabItem:"
+ "bundleFromNSBundle:"
+ "bundleType"
+ "bundleURL"
+ "bundles"
+ "caduca"
+ "caducidad"
+ "canContinueInTapToRadar"
+ "canonicalQueryString"
+ "char_traits::copy overlapped range"
+ "cleanBundle:completionHandler:"
+ "cleanSuiteWithCompletionHandler:"
+ "cleanTest:bundle:completionHandler:"
+ "codice di sicurezza"
+ "com.apple.SafariShared.WBSFifoTestResults.%@.%p.internalQueue"
+ "com.apple.SafariShared.WBSFileTestsResults.%@.%p.internalQueue"
+ "com.apple.SafariShared.WBSTestController.%@.%p.internalQueue"
+ "continuationID"
+ "continuationIndex"
+ "continueInTapToRadarURL"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createFifoAtFileURL:error:"
+ "creationDateString"
+ "credentialTypes"
+ "currentDevice"
+ "data de validade"
+ "date d'expiration"
+ "defaultSearchEngineMatchesExperiment"
+ "descriptionTemplate"
+ "detailTypesForSelectedFeedbackCategory"
+ "determineAccountStateWithCompletion:"
+ "deviceClass"
+ "diagnosticsData"
+ "dictionaryRepresentationRedactingSensitiveValues:"
+ "didDownloadDataForRemotelyUpdatableDataController:"
+ "didSubmitFormOfType:withFieldType:elementType:isAutoFilled:isManuallyFilledByUser:modificationType:autoFillOfferedType:webpageLocale:"
+ "didSubmitFormOfType:withPerFormModificationsDictionary:webpageLocale:"
+ "didSubmitFormOfType:withPerFormUsageDictionary:webpageLocale:"
+ "displayablePANSuffix"
+ "e.g. Billing ZIP code"
+ "e.g. Billing information"
+ "e.g. Birth date"
+ "e.g. Expected address and credit card AutoFill prompts"
+ "e.g. Failed to fill credit card security code"
+ "e.g. Filled credit card security code"
+ "e.g. Filled date as MM-DD-YYYY, but expected DD/MM"
+ "e.g. Safari offered to fill ZIP code"
+ "e.g. Search field"
+ "elementType"
+ "email"
+ "enableLabelPreviousSearchesInCompletionList"
+ "enableProvider1"
+ "enableProvider2"
+ "endTest:inBundle:"
+ "errorMessage"
+ "evaluateWithObject:"
+ "expectedResults"
+ "expectedResultsName"
+ "expectedResultsPathExtension"
+ "expectedResultsURL"
+ "expira"
+ "fieldIDToSingleFieldData"
+ "fieldType"
+ "fifoHandle"
+ "fifoURL"
+ "fileHandleForWritingToURL:error:"
+ "fileURL"
+ "form-metadata-%@-%@.json"
+ "formFieldTypeForFormControlMetadata:formMetadata:"
+ "formID"
+ "formType"
+ "historyItemIdentifierForURL:profileIdentifier:"
+ "iOSDefaultBrowserSelectionState"
+ "informativeText"
+ "initWithComponent:title:descriptionTemplate:"
+ "initWithContentsOfURL:options:error:"
+ "initWithDataFormat:builtInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:"
+ "initWithDataSource:"
+ "initWithDiagnosticsData:"
+ "initWithFieldType:fieldID:elementType:"
+ "initWithFifoURL:error:"
+ "initWithFileURL:error:"
+ "initWithFormType:formID:"
+ "initWithIdentifier:name:version:"
+ "initWithIdentifier:pageURL:expectedResultsURL:dictionary:"
+ "initWithIdentifier:tests:"
+ "initWithSnapshotData:error:"
+ "initWithStartDelay:interval:repeats:queue:handler:"
+ "initWithSuiteURL:bundleNames:"
+ "initWithTabInfo:userTypedString:alternativeDisplayTextForURL:forQueryID:"
+ "initWithWebpageLocale:"
+ "isAutoFilled"
+ "isCardBalanceZeroOrNegative"
+ "isDuckDuckGoABEnabledForSearchEnginePreferenceObserver:"
+ "isGoogleABEnabledForSearchEnginePreferenceObserver:"
+ "isLabelPreviousSearchesInCompletionListEnabled"
+ "isLabelPreviousSearchesInCompletionListEnabledForTrial"
+ "isManuallyFilledByUser"
+ "isProvider1Enabled"
+ "isProvider2Enabled"
+ "isStreamlinedCompletionListEnabledForTrial"
+ "isVerticalWritingMode"
+ "isVirtualCard:previouslyFilledVirtualCardNumbers:completion:"
+ "json"
+ "kreditkartennummer"
+ "line"
+ "looksLikeEIDField"
+ "looksLikeIMEIField"
+ "macCatalyst"
+ "macOS"
+ "marketplace-kit"
+ "matchesForPasswordAutoFill"
+ "modificationType"
+ "new"
+ "nom du titulaire de la carte"
+ "nombre en la tarjeta"
+ "nome sulla carta"
+ "numero carta di credito"
+ "numero della carta di credito"
+ "overall"
+ "pageTestController:navigateAndCaptureFormsMetadataForURL:completionHandler:"
+ "pageTestController:resizeViewport:completionHandler:"
+ "pageTestControllerInitializeApp:completionHandler:"
+ "pageTestControllerTerminateApp:"
+ "pageTestType"
+ "passwordManagerIOS"
+ "percentageOfBlankFields"
+ "percentageOfFieldsAutoFilled"
+ "percentageOfFieldsAutoFilledThenCleared"
+ "percentageOfFieldsAutofilledThenModified"
+ "percentageOfFieldsManuallyFilledByUser"
+ "percentageOfFieldsManuallyFilledByWebsite"
+ "percentageOfFieldsWhereAutoFillWasUsedOverOffered"
+ "percentageOfFieldsWhereContactAutoFillWasUsedOverOffered"
+ "percentageOfFieldsWhereCreditCardAutoFillWasUsedOverOffered"
+ "percentageOfFieldsWhereOneTimeCodeAutoFillWasUsedOverOffered"
+ "percentageOfFieldsWherePasswordAutoFillWasUsedOverOffered"
+ "performance"
+ "performanceValues"
+ "placeholderForFeedbackDetailType:"
+ "prepareBundle:completionHandler:"
+ "prepareSuiteWithCompletionHandler:"
+ "prepareTest:bundle:completionHandler:"
+ "processRemovedHistoryItems:forProfileWithIdentifier:"
+ "q24@?0@\"NSBundle\"8@\"NSBundle\"16"
+ "readReportFromFifoHandle:error:"
+ "recordVisit:sourceVisit:title:loadSuccessful:origin:increaseVisitCount:score:statusCode:"
+ "reportActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:"
+ "reportError:forStage:forTest:inBundle:"
+ "reportForActualResults:expectedResults:expectedResultsName:uniformTypeIdentifier:forStage:forTest:inBundle:"
+ "reportForError:forStage:forTest:inBundle:"
+ "reportForPerformance:forStage:forTest:inBundle:"
+ "reportPerformance:forStage:forTest:inBundle:"
+ "reportType"
+ "reproducibility"
+ "responseForDetailType:"
+ "resultsActual"
+ "resultsExpected"
+ "resultsExpectedName"
+ "resultsUniformTypeIdentifier"
+ "runTest:bundle:storeResultsIn:completionHandler:"
+ "runTest:bundle:storeResultsIn:tryCount:completionHandler:"
+ "runTestsAndStoreResultsIn:completionHandler:"
+ "safariAutoFill"
+ "safariIOS"
+ "safariNewBugs"
+ "safariStartPageIOS"
+ "safariStartPageMacOS"
+ "safari_allObjectsPassTest:"
+ "safari_bundlesFromDirectory:bundleType:"
+ "safari_detailStringWithTitleString:prompt:"
+ "safari_filenameFormattedString"
+ "safari_isMarketplaceKitURL"
+ "safari_looksLikeEmailAddress"
+ "saved passkey"
+ "saved password"
+ "savedAccount"
+ "scadenza"
+ "selectedAttachmentsType"
+ "selectedFeedbackCategory"
+ "sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledVirtualCardData:"
+ "sendTelemetryEventsOnFormSubmission"
+ "setAlternativeDisplayTextForURL:"
+ "setAttachmentPaths:"
+ "setAutoFillOfferedType:"
+ "setComponent:"
+ "setContinuationID:"
+ "setContinuationIndex:"
+ "setDescriptionTemplate:"
+ "setFieldIDToSingleFieldData:"
+ "setFieldType:"
+ "setFormMetadata:"
+ "setIsAutoFilled:"
+ "setIsLabelPreviousSearchesInCompletionListEnabledForTrial:"
+ "setIsManuallyFilledByUser:"
+ "setIsStreamlinedCompletionListEnabledForTrial:"
+ "setKeywords:"
+ "setLooksLikeEIDField:"
+ "setLooksLikeIMEIField:"
+ "setModificationType:"
+ "setReproducibility:"
+ "setResponse:forDetailType:"
+ "setSelectedAttachmentsType:"
+ "setSelectedFeedbackCategory:"
+ "setVerticalWritingMode:"
+ "setZoneID:"
+ "shouldRemotelyUpdatableDataControllerUpdateOnSchedule:"
+ "sicherheitscode"
+ "snapshotData"
+ "sourceURL"
+ "specifierForAutocompleteTokensAndAddressBookLabel"
+ "stack"
+ "stage"
+ "std::string_view::string_view(iterator, sentinel) received invalid range"
+ "stringForSingleCreditCardDataType:"
+ "suiteURL"
+ "tap-to-radar"
+ "tellWalletThatExistingCardWasFilledInForm:previouslyFilledVirtualCardNumbers:"
+ "testBundle"
+ "testIdentifier"
+ "testStage"
+ "test_setBalance:"
+ "test_setLastUsedDate:"
+ "timerWithInterval:repeats:queue:handler:"
+ "titleForAttachmentsType:"
+ "titleForFeedbackCategory:"
+ "titleForFeedbackDetailType:"
+ "titleText"
+ "titolare carta"
+ "titolare della carta"
+ "titolare della carta di credito"
+ "titular de la tarjeta"
+ "totalNumberOfFields"
+ "totalNumberOfFieldsWhereAutoFillWasOffered"
+ "trialABGroupIdentifier"
+ "txt"
+ "unknown detail type placeholder"
+ "unknown detail type title"
+ "unordered container::erase(iterator) called with a non-dereferenceable iterator"
+ "updateAutoFillOfferedType:forTextFieldWithID:forFormMetadata:"
+ "updateFormTelemetryWithFormMetadata:textFieldMetadata:textFieldValueLength:"
+ "userInterfaceIdiom"
+ "uti"
+ "v24@0:8@\"WBSRemotelyUpdatableDataController\"16"
+ "v24@?0@\"<WBSFormsMetadataProvider>\"8@\"NSError\"16"
+ "v24@?0q8q16"
+ "v32@0:8@\"<WBSTest>\"16@\"<WBSTestBundle>\"24"
+ "v32@?0@\"<WBSTest>\"8Q16@?<v@?B>24"
+ "v32@?0@\"<WBSTestBundle>\"8Q16@?<v@?B>24"
+ "v32@?0@\"NSNumber\"8@\"WBSFormTelemetryData\"16^B24"
+ "v32@?0@\"NSString\"8@\"WBSSingleFieldTelemetryData\"16^B24"
+ "v40@0:8@16@24Q32"
+ "v40@0:8@16Q24q32"
+ "v40@0:8Q16@24@32"
+ "v40@0:8Q16@24q32"
+ "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"<WBSTest>\"32@\"<WBSTestBundle>\"40"
+ "v48@0:8@\"NSError\"16@\"NSString\"24@\"<WBSTest>\"32@\"<WBSTestBundle>\"40"
+ "v68@0:8@16@24@32B40q44B52i56q60"
+ "v72@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"<WBSTest>\"56@\"<WBSTestBundle>\"64"
+ "values"
+ "verticalWritingMode"
+ "viewportSize"
+ "wasPreviouslyAutoFilled"
+ "webpageLocale"
+ "writeTemporaryFileWithFormMetadata"
+ "writeToURL:options:error:"
+ "yy"
+ "zero"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"
+ "\xab0\xfc0\xc90\rT\xa9\x7f\xbaN"
+ "\xab0\xfc0\xc90ju\xf7S"
+ "\xaf0\xec0\xb80\xc30\xc80\xab0\xfc0\xc90\rT\xa9\x7f\xbaN"
+ "\xbb0\xad0\xe50\xea0\xc60\xa30\xb30\xfc0\xc90"
+ "̸̹ "
+ "̸̹|\xc7"
+ "\xf4\xbcH\xc5 "
- "\x011"
- "\x06\x13"
- "\x0f\x03"
- "\x1a\x04>\x044\x04 "
- "!h\x8c\x9a\x01x"
- "#\x0e+\x0e1\x0e*\x0e\x01\x0e2\x0e#\x0e\x15\x0e#\x0e'\x0e\b\x0e*\x0e-\x0e\x1a\x0e\"\x0e7\x0e\x19\x0e\"\x0e1\x0e\x19\x0e"
- "#\x0e+\x0e1\x0e*\x0e\x01\x0e2\x0e#\x0e\"\x0e7\x0e\x19\x0e\"\x0e1\x0e\x19\x0e"
- "#\x0e+\x0e1\x0e*\x0e\x04\x0e'\x0e2\x0e!\x0e\x1b\x0e%\x0e-\x0e\x14\x0e \x0e1\x0e\"\x0e"
- "#\x0e+\x0e1\x0e*\x0e\"\x0e7\x0e\x19\x0e\"\x0e1\x0e\x19\x0e"
- "#\x0e+\x0e1\x0e*\x0eO"
- "%s:%d: assertion %s failed: %s"
- "(?=\"flags\"{?=\"disallowsAutocomplete\"b1\"claimsToBeCurrentPasswordViaAutocompleteAttribute\"b1\"claimsToBeNewPasswordViaAutocompleteAttribute\"b1\"claimsToBeUsernameViaAutocompleteAttribute\"b1\"looksLikeCreditCardCardholderField\"b1\"looksLikeCreditCardCompositeExpirationDateField\"b1\"looksLikeCreditCardNumberField\"b1\"looksLikeCreditCardSecurityCodeField\"b1\"looksLikeCreditCardTypeField\"b1\"looksLikeDayField\"b1\"looksLikeMonthField\"b1\"looksLikeYearField\"b1\"looksLikeIgnoredDataTypeField\"b1\"looksLikePasswordCredentialField\"b1\"looksLikeOneTimeCodeField\"b1\"oneTimeCodeIsEligibleForAutomaticLogin\"b1\"visible\"b1\"active\"b1\"disabled\"b1\"readOnly\"b1\"textField\"b1\"secureTextField\"b1\"autoFilledTextField\"b1\"userEditedTextField\"b1\"labeledUsernameField\"b1}\"asInteger\"q)"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/__hash_table"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/deque"
- "/AppleInternal/Library/BuildRoots/7df5dd62-b1e4-11ee-ad34-d64f9dd5e0b3/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/include/c++/v1/vector"
- "2fa"
- "6-digit authentication code"
- "8\t$\tM\t/\t>\t*\t(\t "
- ":\x04>\x044\x04"
- ":\x04>\x044\x04 "
- "@\"NSData\"24@0:8Q16"
- "@\"NSNumber\"24@?0@\"NSObject\"8Q16"
- "@\"WBSRemotePlistController\""
- "@\"WBSStartPageSectionDescriptor\"24@?0@\"NSString\"8Q16"
- "@44@0:8d16d24B32@?36"
- "Aktivierungscode"
- "Authorisierungscode"
- "B24@0:8@\"WBSRemotePlistController\"16"
- "Bestatigungscode"
- "Codice attivazione"
- "Codice di sicurezza"
- "Codul de confirmare"
- "DeviceClassNumber"
- "FPANSuffix"
- "Failed to clear history from CoreSpotlight for profile with identifier %{private}@"
- "Failed to write bytes to file descriptor %d: %{errno}i"
- "Finished clearing history from CoreSpotlight for profile with %{private}@"
- "Interrupted while writing to file descriptor %d; trying again"
- "Kod autoryzacyjny"
- "Kod pengesahan"
- "Kod weryfikacyjny"
- "Kode keamanan"
- "Kode konfirmasi"
- "Kode verifikasi"
- "MFA code"
- "Masukkan Kod"
- "PIN"
- "SMS"
- "Sicherheitscode"
- "Some of your passwords have appeared in a data leak, putting those accounts at high risk of compromise. iPod can help you re-secure your accounts."
- "SpotlightSuggestionsEnabled"
- "T@\"NSArray\",C,N,V_attachmentURLs"
- "T@\"NSString\",C,N,V_componentName"
- "T@\"NSString\",C,N,V_componentVersion"
- "T@\"NSString\",C,N,V_descriptionText"
- "T@\"NSString\",R,C,N,V_uuidString"
- "T@\"WBSCyclerIterationCounter\",&,N"
- "T@\"WBSCyclerIterationCounter\",&,N,V_iterationCounter"
- "T@\"WBSQuerySuggestion\",&,N"
- "TB,N,V_isMoreSearchProviderSuggestionsEnabled"
- "TB,N,V_isReflectUserIntentInSearchEnabled"
- "TB,N,V_isResponsiveCompletionListEnabled"
- "TB,N,V_isStreamlinedCompletionListEnabled"
- "TB,R,N,GisFinished"
- "TQ,N,V_visitCount"
- "Task"
- "The password for one of your accounts has appeared in a data leak, putting it at high risk of compromise. iPod can help you re-secure your account."
- "Tq,N,V_classification"
- "T\xcfܴ"
- "UniqueDeviceID"
- "U\xd6x\xc7T\xcfܴ"
- "Verifizierungscode"
- "WBSRadarNewProblemURLBuilder"
- "WBSRecentlyBreachedSavedPasswordProvider"
- "WBSRemotePlistControllerDelegate"
- "WBSRemotePlistSnapshot"
- "W\x9a<\x8a\xbcx"
- "W\x9aI\x8b\xbcx"
- "_attachmentURLs"
- "_componentName"
- "_componentVersion"
- "_contentDescriptionForURL:"
- "_descriptionText"
- "_historyItemIdentifierForURLString:"
- "_initWithStartDelay:interval:repeats:handler:"
- "_isMoreSearchProviderSuggestionsEnabled"
- "_isReflectUserIntentInSearchEnabled"
- "_isResponsiveCompletionListEnabled"
- "_isStreamlinedCompletionListEnabled"
- "_relativeProbabilitiesForOperationsWithNoMovableTabs"
- "_remotePlistController"
- "access code"
- "activation code"
- "attachmentURLs"
- "attachments"
- "code d'authentification"
- "code d'autorisation"
- "code d'identification"
- "code de confirmation"
- "code de validation"
- "codice di attivazione"
- "codice di conferma"
- "codice di verifica"
- "componentName"
- "componentVersion"
- "confirmation code"
- "deleteSearchableItemsWithDomainIdentifiers:protectionClass:forBundleID:options:completionHandler:"
- "descriptionText"
- "determineManateeStateWithCompletion:"
- "didDownloadPlistForRemotePlistController:"
- "digit code"
- "digite o codigo"
- "dogrulama kodu"
- "enter code"
- "enter the code"
- "historyItemIdentifierForURL:"
- "identification code"
- "identificationCode"
- "initWithBuiltInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:"
- "initWithKeyName:searchable:searchableByDefault:unique:multiValued:"
- "initWithPlistData:error:"
- "initWithTabInfo:userTypedString:forQueryID:"
- "isMoreSearchProviderSuggestionsEnabled"
- "isResponsiveCompletionListEnabled"
- "isVirtualCard:lastFilledCardData:completion:"
- "login code"
- "new credit card"
- "one time passcode"
- "one time password"
- "onetimecode"
- "onetimepasscode"
- "pageVisitCount"
- "passcode"
- "plistDataWithFormat:"
- "processRemovedHistoryItems:"
- "rdar://new/problem"
- "rdar://new/problem/"
- "recordVisit:sourceVisit:title:loadSuccessful:visitWasFromThisDevice:increaseVisitCount:score:statusCode:"
- "sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledCardData:"
- "setAttachmentURLs:"
- "setComponentName:"
- "setComponentVersion:"
- "setDefaultGeolocationSetting:"
- "setDescriptionText:"
- "setIsMoreSearchProviderSuggestionsEnabled:"
- "setIsReflectUserIntentInSearchEnabled:"
- "setIsResponsiveCompletionListEnabled:"
- "setIsStreamlinedCompletionListEnabled:"
- "setValue:forCustomKey:"
- "shouldRemotePlistControllerUpdateOnSchedule:"
- "sign-in code"
- "tellWalletThatExistingCardWasFilledInForm:lastFilledCardData:"
- "token"
- "two factor"
- "two step sign in"
- "two-factor"
- "two-step sign in"
- "twofactor"
- "unordered container erase(iterator) called with a non-dereferenceable iterator"
- "v24@0:8@\"WBSRemotePlistController\"16"
- "v64@0:8@16@24@32B40B44B48i52q56"
- "verification code"
- "verificationCode"
- "xǝɈ\xbc8\xd6"
- "\x8c\x9a\xc1\x8b\x01x"
- "\x8d\x8a<\x8a\xb30\xfc0\xc90"
- "\x8d\x8aI\x8b\xbcx"
- "\xb30\xfc0\xc90"
- "\xbax\x8d\x8a\xb30\xfc0\xc90"
- "\xbax\x8d\x8a\xbcx"
- "\xdc"

```
