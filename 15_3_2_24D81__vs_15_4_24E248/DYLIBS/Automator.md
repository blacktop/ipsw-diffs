## Automator

> `/System/Library/Frameworks/Automator.framework/Versions/A/Automator`

```diff

-527.0.0.0.0
-  __TEXT.__text: 0x17bf00
+528.0.0.0.0
+  __TEXT.__text: 0x180b74
   __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x1d48c
-  __TEXT.__gcc_except_tab: 0x177c
+  __TEXT.__objc_methlist: 0x1e868
+  __TEXT.__gcc_except_tab: 0x1768
   __TEXT.__const: 0x218
   __TEXT.__cstring: 0x1887f
   __TEXT.__oslogstring: 0x1a10
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x6350
+  __TEXT.__unwind_info: 0x6580
   __TEXT.__objc_classname: 0x42e7
-  __TEXT.__objc_methname: 0x2ddcb
+  __TEXT.__objc_methname: 0x2dda2
   __TEXT.__objc_methtype: 0x45c0
-  __TEXT.__objc_stubs: 0x21040
-  __DATA_CONST.__got: 0x1028
+  __TEXT.__objc_stubs: 0x21020
+  __DATA_CONST.__got: 0x1038
   __DATA_CONST.__const: 0x9478
   __DATA_CONST.__objc_classlist: 0x1358
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc668
+  __DATA_CONST.__objc_selrefs: 0xcba8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x6d0

   __AUTH_CONST.__auth_got: 0x850
   __AUTH_CONST.__const: 0x28a0
   __AUTH_CONST.__cfstring: 0x1b6e0
-  __AUTH_CONST.__objc_const: 0x348b0
+  __AUTH_CONST.__objc_const: 0x32340
   __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4176A50-AF4C-3736-85F2-5BA0B43110BF
-  Functions: 10163
-  Symbols:   21264
-  CStrings:  17070
+  UUID: 6E9CAD54-24DA-3F5A-87D9-FB5D458D8632
+  Functions: 10552
+  Symbols:   21720
+  CStrings:  17069
 
Symbols:
+ +[AMActionLoader coreTypesBundle].cold.1
+ +[AMActionLoader displayNameAtPathWithCaching:].cold.1
+ +[AMActionRegistry sharedActionRegistry].cold.1
+ +[AMActionSecAssess actionIsThirdPartyWithURL:].cold.1
+ +[AMAddressBookSoftLinking ABAddressBook].cold.1
+ +[AMAddressBookSoftLinking ABGroup].cold.1
+ +[AMAddressBookSoftLinking ABPerson].cold.1
+ +[AMAddressBookSoftLinking ABSearchElement].cold.1
+ +[AMAddressBookSoftLinking framework].cold.1
+ +[AMAppleScriptKitSoftLinking ASKDebuggerSupport].cold.1
+ +[AMAppleScriptKitSoftLinking ASKNibObjectInfoManager].cold.1
+ +[AMAppleScriptKitSoftLinking ASKScriptCache].cold.1
+ +[AMAppleScriptKitSoftLinking ASKScript].cold.1
+ +[AMAppleScriptKitSoftLinking framework].cold.1
+ +[AMAppleScriptKitSoftLinking framework].cold.2
+ +[AMApplicationRegistry sharedApplicationRegistry].cold.1
+ +[AMConverter _cachedChildIdentifiersForType:].cold.1
+ +[AMConverter _cachedParentIdentifiersForType:].cold.1
+ +[AMDescriptionLineItemView labelsForKeys].cold.1
+ +[AMDictationServicesSoftLinking framework].cold.1
+ +[AMDotMacSyncSoftLinking DMCPrefsCenter].cold.1
+ +[AMDotMacSyncSoftLinking framework].cold.1
+ +[AMEventKitCalendarItemXPCToken eventStoreForConversionForEntityType:].cold.1
+ +[AMEventKitSoftLinking EKAlarm].cold.1
+ +[AMEventKitSoftLinking EKCalendarItem].cold.1
+ +[AMEventKitSoftLinking EKCalendar].cold.1
+ +[AMEventKitSoftLinking EKEventStore].cold.1
+ +[AMEventKitSoftLinking EKEvent].cold.1
+ +[AMEventKitSoftLinking EKReminder].cold.1
+ +[AMEventKitSoftLinking framework].cold.1
+ +[AMFFeedContent plainTextStringFromHTMLString:error:].cold.1
+ +[AMFFeedEntry dateFromAtomDateString:].cold.1
+ +[AMFFeedEntry dateFromRSSDateString:].cold.1
+ +[AMFFeedEntry dateFromRSSDateString:].cold.2
+ +[AMFFeedEntry feedEntryWithAtomFeedElement:baseURL:].cold.1
+ +[AMFFeedEntry feedEntryWithRSSFeedElement:baseURL:].cold.1
+ +[AMFFeedFinder _interestingLinkStrings].cold.1
+ +[AMFFeedFinder _parseResultsFromHeadElement:sourceURL:error:].cold.1
+ +[AMFFeedParser parseFeedAsynchronouslyWithData:url:completionHandler:].cold.1
+ +[AMFolderActionsKitSoftLinking FAFolderAction].cold.1
+ +[AMFolderActionsKitSoftLinking FAScript].cold.1
+ +[AMFolderActionsKitSoftLinking FolderActionsDispatcher].cold.1
+ +[AMFolderActionsKitSoftLinking framework].cold.1
+ +[AMGenericActionLoader sharedGenericActionLoader].cold.1
+ +[AMILMediaBrowserSoftLinking ILPluginManager].cold.1
+ +[AMILMediaBrowserSoftLinking framework].cold.1
+ +[AMImageRegistry sharedImageRegistry].cold.1
+ +[AMInputOutputWorkflowMetadata _legacyServiceKeyMapping].cold.1
+ +[AMLibraryViewController _variableIdentifiersToChildIdentifiers].cold.1
+ +[AMLocalRunnerController localRunnerControllerWithWorkflow:error:].cold.1
+ +[AMPluginInstallerController urlForExistingPluginNamed:atLibrarySubPath:].cold.1
+ +[AMRemoteActionController sharedRemoteActionController].cold.1
+ +[AMRemoteRunnerController remoteRunnerControllerWithPropertyList:workflowURL:workingDirectoryURL:error:].cold.1
+ +[AMRemoteRunnerController remoteRunnerControllerWithWorkflow:workingDirectoryURL:error:].cold.1
+ +[AMRemoteRunnerController remoteRunnerControllerWithWorkflowURL:workingDirectoryURL:error:].cold.1
+ +[AMServicePluginHeaderViewController _imageNames].cold.1
+ +[AMServicesController sharedServicesController].cold.1
+ +[AMTemplateChooserItem templateChooserItems].cold.1
+ +[AMTextDetector sharedTextDetector].cold.1
+ +[AMTypeRegistry sharedTypeRegistry].cold.1
+ +[AMVariable _variableIdentifiersToTemplateIdentifiers].cold.1
+ +[AMVariable _variableIdentifiersToTypes].cold.1
+ +[AMVariable _variableSpecificIdentifiersToIdentifiers].cold.1
+ +[AMWebKitSoftLinking WebArchive].cold.1
+ +[AMWebKitSoftLinking framework].cold.1
+ +[AMWorkflow(AMWorkflowLoading) workflowAtURL:forRunning:remotely:error:].cold.1
+ +[AMWorkflow(AMWorkflowLoading) workflowAtURL:forRunning:remotely:variablesDictionary:error:].cold.1
+ +[AMWorkflow(AMWorkflowLoading) workflowWithPropertyList:url:forRunning:remotely:error:].cold.1
+ +[AMWorkflowRunner _operationKeysToObserve].cold.1
+ +[NSDate(AMDateFormatting) am_dateWithNaturalLanguageString:].cold.1
+ +[NSDate(AMExampleDate) am_exampleDate].cold.1
+ +[NSFileManager(AMNSFileManagerExtensions) am_cachedNumberFormatter].cold.1
+ +[_AMPredicateUtilities typeForPredicate:].cold.1
+ -[AMActionInWorkflowXPCToken initWithUUID:].cold.1
+ -[AMActionLoader _appleSignedBundleRequiresOutOfProcessLoaderForNonLoaderProcess:].cold.1
+ -[AMActionLoader bundleForActionWithPropertyList:].cold.1
+ -[AMActionMetadataStore initWithCacheFileURL:].cold.1
+ -[AMActionMetadataStore writeUpdatedStoreFileIfNeeded].cold.2
+ -[AMActionPropertyListXPCToken initWithPropertyList:].cold.1
+ -[AMActionRegistry _loadAllActionsForActionType:].cold.1
+ -[AMActionSecAssess isActionCodeSignedByApple:].cold.1
+ -[AMActionShowWhenRunOverlayView viewDidMoveToSuperview].cold.1
+ -[AMActionView mouseDragged:].cold.1
+ -[AMApplicationRegistry _systemLibraryURL].cold.1
+ -[AMApplicationStub loadWorkflowAtPath:error:].cold.1
+ -[AMApplicationStub runWorkflowAtPath:withInput:error:].cold.1
+ -[AMApplicationStubController runWorkflowAtURL:withInput:error:].cold.1
+ -[AMApplicationStubController validateWorkflowAtURL:error:].cold.1
+ -[AMCache _cacheFileDataForCacheLocationEntries:error:].cold.1
+ -[AMCache _cacheFileDataForCacheLocationEntries:error:].cold.2
+ -[AMCache _cacheFileDataForCacheLocationEntries:error:].cold.3
+ -[AMCache _cacheLocationEntriesFromCacheFileURL:expectedActionLocationURLs:shouldDirtyCache:].cold.1
+ -[AMCache _cacheLocationEntryURLsFromCacheFileData:error:].cold.1
+ -[AMCache _validCacheLocationEntriesFromCacheFileURL:expectedActionLocationURLs:shouldDirtyCache:].cold.3
+ -[AMCache _writeCacheFileForLocationEntries:toURL:error:].cold.1
+ -[AMCache actionWithBundleIdentifier:].cold.1
+ -[AMCache actionsForActionType:].cold.1
+ -[AMCache initWithCacheFileURL:actionLocations:].cold.1
+ -[AMCache initWithCacheFileURL:actionLocations:].cold.2
+ -[AMCacheLocationEntry _addAction:actionType:].cold.2
+ -[AMCacheLocationEntry actionsForActionType:].cold.1
+ -[AMCacheLocationEntry initWithURL:].cold.1
+ -[AMCacheLocationEntry loadAllActionsIfNeededForActionType:].cold.1
+ -[AMConvertEventKitObject sharedEventStore].cold.1
+ -[AMDictationCommandWorkflowPersonality canSaveWorkflow:atURL:forInstallation:error:].cold.1
+ -[AMDiskBasedCacheLocationEntry _generateActionForURLFromDisk:].cold.2
+ -[AMEventKitCalendarItemXPCToken initWithCalendarItem:].cold.1
+ -[AMFFeed initWithURL:metadata:].cold.1
+ -[AMFFeed initWithURL:metadata:].cold.2
+ -[AMFFeedController _feedParsedAtURL:metadata:entries:completionHandler:].cold.1
+ -[AMFFeedController _parseFeedAtURL:data:completionHandler:].cold.1
+ -[AMFFeedController _refreshFeedAtURL:completionHandler:].cold.1
+ -[AMFFeedController _refreshFeedAtURL:completionHandler:].cold.2
+ -[AMFFeedController _refreshFeedAtURL:completionHandler:].cold.3
+ -[AMFFeedController existingFeedAtURL:].cold.1
+ -[AMFFeedController feedAtURL:refreshRequired:completionHandler:].cold.1
+ -[AMFFeedController feedAtURL:refreshRequired:completionHandler:].cold.2
+ -[AMFFeedController feedAtURL:refreshRequired:completionHandler:].cold.3
+ -[AMFFeedController refreshFeed:completionHandler:].cold.1
+ -[AMFFeedController refreshFeed:completionHandler:].cold.2
+ -[AMFFeedController reset].cold.1
+ -[AMFFeedElement childWithName:].cold.1
+ -[AMFFeedEnclosure initWithURL:type:length:].cold.1
+ -[AMFFeedFinder _finishWithError:].cold.1
+ -[AMFFeedFinder _startFindingUsingFeedController].cold.1
+ -[AMFFeedFinder _startFindingUsingFeedController].cold.2
+ -[AMFFeedFinder _startFindingUsingWebView].cold.1
+ -[AMFFeedFinder _startFindingUsingWebView].cold.2
+ -[AMFFeedFinder initWithURL:feedController:].cold.1
+ -[AMFFeedFinder startFinding].cold.1
+ -[AMFFeedFinder startFinding].cold.2
+ -[AMFFeedParser parser:didEndElement:namespaceURI:qualifiedName:].cold.1
+ -[AMFFeedParser parser:didEndElement:namespaceURI:qualifiedName:].cold.2
+ -[AMFFeedParser parser:foundCDATA:].cold.1
+ -[AMFFeedParser parser:foundCharacters:].cold.1
+ -[AMFolderActionWorkflowPersonality canSaveWorkflow:atURL:forInstallation:error:].cold.1
+ -[AMFolderActionWorkflowPersonality finishSavingWorkflow:forOperation:atURL:error:].cold.1
+ -[AMFolderActionWorkflowPersonality infoStringForCompleteInstallationWithMetaData:].cold.1
+ -[AMGroup insertAsset:atIndex:].cold.1
+ -[AMGroup insertChildGroup:atIndex:].cold.1
+ -[AMImageRegistry _staticBundleIdentifierForApplicationNamed:].cold.1
+ -[AMImageRegistry iconForApplicationName:size:].cold.1
+ -[AMImageRegistry iconForApplicationWithIdentifier:size:].cold.1
+ -[AMImageRegistry iconForFileType:size:].cold.1
+ -[AMImageRegistry imageForURL:size:].cold.1
+ -[AMImageRegistry imageFromSystemNamed:size:].cold.1
+ -[AMInputOutputPluginHeaderViewController _inputOutputWorkflowMetaData].cold.1
+ -[AMLibraryViewController predicateForSearchString:].cold.1
+ -[AMLocalRunnerController initWithWorkflow:].cold.1
+ -[AMLocalRunnerController isIdle].cold.1
+ -[AMLocalRunnerController isPaused].cold.1
+ -[AMLocalRunnerController isRunning].cold.1
+ -[AMLocalRunnerController isStopping].cold.1
+ -[AMLocalRunnerController pause].cold.1
+ -[AMLocalRunnerController pause].cold.2
+ -[AMLocalRunnerController resume].cold.1
+ -[AMLocalRunnerController resume].cold.2
+ -[AMLocalRunnerController runWithInput:steppingInitially:completionHandler:].cold.1
+ -[AMLocalRunnerController step].cold.1
+ -[AMLocalRunnerController stopWithError:].cold.1
+ -[AMLocalRunnerController workflowRunner:didError:].cold.1
+ -[AMLocalRunnerController workflowRunner:didLogMessage:ofType:fromAction:].cold.1
+ -[AMLocalRunnerController workflowRunner:didResumeWithAction:].cold.1
+ -[AMLocalRunnerController workflowRunner:didRunAction:].cold.1
+ -[AMLocalRunnerController workflowRunner:didRunConversion:].cold.1
+ -[AMLocalRunnerController workflowRunner:progressDidChange:forAction:].cold.1
+ -[AMLocalRunnerController workflowRunner:willRunAction:].cold.1
+ -[AMLocalRunnerController workflowRunner:willRunConversion:].cold.1
+ -[AMLocalRunnerController workflowRunnerDidFinish:].cold.1
+ -[AMLocalRunnerController workflowRunnerDidPause:].cold.1
+ -[AMLocalRunnerController workflowRunnerDidRun:].cold.1
+ -[AMLocalRunnerController workflowRunnerDidStop:].cold.1
+ -[AMLocalRunnerController workflowRunnerWillPause:].cold.1
+ -[AMLocalRunnerController workflowRunnerWillRun:].cold.1
+ -[AMLocalRunnerController workflowRunnerWillStop:].cold.1
+ -[AMProxyAction initWithCacheLocationEntry:bundleID:].cold.1
+ -[AMProxyAction initWithCacheLocationEntry:bundleID:].cold.2
+ -[AMProxyAction initWithDictionary:].cold.1
+ -[AMRemoteAction _executeXPC:synchronous:errorHandler:].cold.1
+ -[AMRemoteAction _invalidateUserInterface].cold.1
+ -[AMRemoteAction _invalidate].cold.1
+ -[AMRemoteAction _prepareForRunningOnMainThread].cold.2
+ -[AMRemoteAction _supportsPauseResume].cold.1
+ -[AMRemoteAction _supportsPauseResume].cold.2
+ -[AMRemoteAction initWithDefinition:fromArchive:].cold.1
+ -[AMRemoteAction retryXPCConnectionWithCompletionHandler:].cold.1
+ -[AMRemoteAction runAsynchronouslyWithInput:].cold.1
+ -[AMRemoteActionController _dummyHostViewControllerForRemoteAction:completionHandler:].cold.1
+ -[AMRemoteActionController _dummyHostViewControllerForRemoteAction:completionHandler:].cold.2
+ -[AMRemoteActionController _dummyHostViewControllerForRemoteAction:completionHandler:].cold.3
+ -[AMRemoteActionController _dummyHostViewControllerForRemoteAction:completionHandler:].cold.4
+ -[AMRemoteActionController _dummyHostViewControllerForRemoteAction:completionHandler:].cold.5
+ -[AMRemoteActionController _invalidateRemoteActionWithLock:fromXPCError:].cold.1
+ -[AMRemoteActionController _remoteActionsForConnection:].cold.1
+ -[AMRemoteActionController _setNameForConnection:remoteAction:].cold.1
+ -[AMRemoteActionController _xpcConnectionForRemoteActionWithLock:].cold.1
+ -[AMRemoteActionController _xpcConnectionForRemoteActionWithLock:].cold.2
+ -[AMRemoteActionController _xpcProxyForRemoteAction:workflowUUID:synchronous:proxyCreationError:errorHandler:].cold.3
+ -[AMRemoteActionController _xpcServiceProxyForRemoteActionWithLock:errorHandler:].cold.2
+ -[AMRemoteActionController configureDummyViewControllerForRemoteAction:completionHandler:].cold.1
+ -[AMRemoteActionController configureDummyViewControllerForRemoteAction:completionHandler:].cold.2
+ -[AMRemoteActionController configureDummyViewControllerForRemoteAction:completionHandler:].cold.3
+ -[AMRemoteActionController hostViewControllerForRemoteAction:completionHandler:].cold.1
+ -[AMRemoteActionController hostViewControllerForRemoteAction:completionHandler:].cold.2
+ -[AMRemoteActionController hostViewControllerForRemoteAction:completionHandler:].cold.3
+ -[AMRemoteActionController hostViewControllerForRemoteAction:completionHandler:].cold.4
+ -[AMRemoteActionController hostViewControllerForRemoteAction:completionHandler:].cold.5
+ -[AMRemoteActionController invalidateRemoteAction:].cold.1
+ -[AMRemoteActionDelegate initWithRemoteAction:].cold.1
+ -[AMRemoteActionVariableDelegate _localVariableForXPCVariable:].cold.1
+ -[AMRemoteActionVariableDelegate initWithLocalVariablesController:remoteAction:].cold.1
+ -[AMRemoteActionVariableDelegate remoteActionAddVariable:newVariableUUID:].cold.1
+ -[AMRemoteActionVariableDelegate remoteActionEditVariable:clickedPoint:controlFrame:isTokenField:].cold.1
+ -[AMRemoteActionVariableDelegate remoteActionRenameVariable:name:].cold.1
+ -[AMRemoteActionVariableDelegate remoteActionRenameVariable:name:].cold.2
+ -[AMRemoteActionVariableDelegate remoteActionUpdateValue:ofVariable:].cold.1
+ -[AMRemoteActionViewController initWithRemoteAction:viewInfo:].cold.1
+ -[AMRemoteActionViewController initWithRemoteAction:viewInfo:].cold.2
+ -[AMRemoteActionViewController invalidateXPC].cold.1
+ -[AMRemoteRunnerController initWithPropertyList:workflowURL:workingDirectoryURL:].cold.1
+ -[AMRemoteRunnerController initWithWorkflow:propertyList:workingDirectoryURL:].cold.1
+ -[AMRemoteRunnerController initWithWorkflow:propertyList:workingDirectoryURL:].cold.2
+ -[AMRemoteRunnerController initWithWorkflow:workingDirectoryURL:].cold.1
+ -[AMRemoteRunnerController runWithInput:steppingInitially:completionHandler:].cold.1
+ -[AMRemoteRunnerController setDelegate:].cold.1
+ -[AMRemoteRunnerXPCDelegate handleCommunicationsError:].cold.1
+ -[AMResultsViewController awakeFromNib].cold.1
+ -[AMServicePluginHeaderViewController _chooseCustomImageCompleteWithImageData:pathExtension:].cold.1
+ -[AMServicePluginHeaderViewController _serviceWorkflowMetaData].cold.1
+ -[AMServiceWorkflowPersonality _infoPlistForServiceWorkflowWithMetadata:].cold.1
+ -[AMServiceWorkflowPersonality updateFileWrapper:forWorkflowMetaData:documentType:error:].cold.1
+ -[AMServiceWorkflowPersonality updateFileWrapper:forWorkflowMetaData:documentType:error:].cold.2
+ -[AMServicesController _activateServiceAction:error:].cold.1
+ -[AMServicesController _clearServiceActivationStateAtURL:].cold.1
+ -[AMServicesController _serviceFoundForServicesMonitor:url:].cold.1
+ -[AMServicesController activateServiceAtURL:completionHandler:].cold.1
+ -[AMSplitView engageBreadthConstraintForSubview:].cold.1
+ -[AMType initWithApplicationBundleID:customUTI:].cold.1
+ -[AMTypeRegistry orderedCategoryIdentifiers].cold.1
+ -[AMUnknownXPCToken initWithObject:].cold.1
+ -[AMValidatedCacheLocationEntry _actionBundleIDListForActionType:].cold.1
+ -[AMValidatedCacheLocationEntry _dateFromPropertyListData:forKey:].cold.2
+ -[AMValidatedCacheLocationEntry _generateActionsForActionType:].cold.1
+ -[AMValidatedCacheLocationEntry initWithURL:propertyListData:].cold.1
+ -[AMValidatedCacheLocationEntry valueForKey:forActionWithBundleIdentifier:].cold.1
+ -[AMValidatedCacheLocationEntry valueForKey:forActionWithBundleIdentifier:].cold.2
+ -[AMValidatedCacheLocationEntry valueForKey:forActionWithBundleIdentifier:].cold.3
+ -[AMWorkflow _clearLoadingErrorsForAction:].cold.1
+ -[AMWorkflow _configureForWorkflowPersonality:templateWorkflowMetaData:].cold.1
+ -[AMWorkflow _insertActionWithoutNotifying:atIndex:].cold.1
+ -[AMWorkflow _insertActionWithoutNotifying:atIndex:].cold.2
+ -[AMWorkflow _insertActionWithoutNotifying:atIndex:].cold.3
+ -[AMWorkflow _reloadActionWithoutNotifying:].cold.1
+ -[AMWorkflow fileWrapperForWritingReturningSavedPropertyList:documentType:originalContentsFileWrapper:error:].cold.1
+ -[AMWorkflow insertAction:atIndex:].cold.1
+ -[AMWorkflow insertAction:atIndex:].cold.2
+ -[AMWorkflow insertAction:atIndex:].cold.3
+ -[AMWorkflow insertActions:atIndex:].cold.1
+ -[AMWorkflow insertActions:atIndex:].cold.2
+ -[AMWorkflow insertActions:atIndex:].cold.3
+ -[AMWorkflow readFromFileWrapper:variablesDictionary:error:].cold.1
+ -[AMWorkflow readFromPropertyList:variablesDictionary:error:].cold.1
+ -[AMWorkflow readFromURL:variablesDictionary:error:].cold.1
+ -[AMWorkflow removeActions:].cold.1
+ -[AMWorkflowCompletionResults encodeWithCoder:].cold.1
+ -[AMWorkflowCompletionResults initWithCoder:].cold.1
+ -[AMWorkflowController _displayWarningsForActions:toInsertAtIndex:].cold.1
+ -[AMWorkflowController _displayWarningsForActions:toInsertAtIndex:].cold.2
+ -[AMWorkflowController _displayWarningsForActions:toInsertAtIndex:].cold.3
+ -[AMWorkflowController _insertActions:atIndex:displayWarnings:refuseDeprecatedActions:].cold.1
+ -[AMWorkflowController _shouldDisplayWarningForAction:givenPreviousAction:].cold.1
+ -[AMWorkflowController _showDeprecatedSheetForAction:].cold.1
+ -[AMWorkflowController _showDeprecatedSheetForAction:].cold.2
+ -[AMWorkflowController _warningAlertDidEnd:returnCode:contextInfo:].cold.1
+ -[AMWorkflowController run:].cold.1
+ -[AMWorkflowController(WorkflowPasteboard) addActionWithBundleID:atIndex:withParameters:].cold.1
+ -[AMWorkflowController(WorkflowPasteboard) addActionWithBundleID:atIndex:withParameters:].cold.2
+ -[AMWorkflowController(WorkflowPasteboard) addActionWithBundleID:atIndex:withParameters:].cold.3
+ -[AMWorkflowController(WorkflowPasteboard) addSpecifiedItemsActionWithBundleID:atIndex:withItems:].cold.1
+ -[AMWorkflowController(WorkflowPasteboard) addSpecifiedItemsActionWithBundleID:atIndex:withItemsFromPasteboard:].cold.1
+ -[AMWorkflowController(WorkflowPasteboard) itemsFromPasteboard:withSpecifiedItemsActionWithBundleID:].cold.1
+ -[AMWorkflowController(WorkflowPasteboard) itemsFromPasteboard:withSpecifiedItemsActionWithBundleID:].cold.2
+ -[AMWorkflowPersonality disableWarningDefaultsKey].cold.1
+ -[AMWorkflowPersonalityInstallerController attemptRecoveryFromError:optionIndex:delegate:didRecoverSelector:contextInfo:].cold.1
+ -[AMWorkflowServiceRunner getInputFromPasteBoard:serviceMetaData:error:].cold.1
+ -[AMWorkflowServiceRunner initWithWorkflowURL:pasteboardName:].cold.1
+ -[AMWorkflowServiceRunner initWithWorkflowURL:pasteboardName:].cold.2
+ -[AMWorkflowServiceRunner runWorkflowWithCompletionBlock:completionQueue:].cold.1
+ -[AMWorkflowView addActionWithBundleID:atIndex:withParameters:].cold.1
+ -[AMWorkflowView addActionWithBundleID:atIndex:withParameters:].cold.2
+ -[AMWorkflowView addActionWithBundleID:atIndex:withParameters:].cold.3
+ -[AMWorkflowView pasteWithPasteboard:].cold.1
+ -[AMWorkspace _performOnExcecutionRunLoop:].cold.1
+ -[AMWorkspace runWorkflowAtPath:withInput:error:].cold.1
+ -[NSArray(AMCocoaExtensions) am_indexSetOfObjects:].cold.1
+ -[NSFileWrapper(AMCocoaExtensions) _am_removeFileWrapperIfPresentNamed:].cold.1
+ -[NSFileWrapper(AMCocoaExtensions) _am_replaceOrAddFileWrapper:].cold.1
+ -[NSMutableDictionary(AMCocoaExtensions) am_overwriteEntriesFromDictionary:].cold.1
+ -[NSURL(AMURLExtensions) am_isImageURL].cold.1
+ -[_AMAddressBookItemsRowTemplateFactory _convertGroupEvaluationPredicateToSearchElement:].cold.1
+ -[_AMAddressBookItemsRowTemplateFactory _convertPersonEvaluationPredicateToSearchElement:].cold.1
+ -[_AMAddressBookItemsRowTemplateFactory _convertPersonEvaluationPredicateToSearchElement:].cold.2
+ -[_AMAddressBookItemsRowTemplateFactory _convertPersonEvaluationPredicateToSearchElement:].cold.3
+ -[_AMAddressBookItemsRowTemplateFactory _convertPersonEvaluationPredicateToSearchElement:].cold.4
+ -[_AMAddressBookItemsRowTemplateFactory _convertPersonUIPredicateToSearchElement:].cold.1
+ -[_AMAddressBookItemsRowTemplateFactory _nameSearchElementForComparisonPredicate:].cold.1
+ -[_AMBoolRowTemplate initTemplateWithName:andKeyPath:andValueName:andValue:].cold.1
+ -[_AMBoolRowTemplate initTemplateWithName:andKeyPath:andValueName:andValue:].cold.2
+ -[_AMBoolRowTemplate initTemplateWithName:andKeyPath:andValueName:andValue:].cold.3
+ -[_AMBoolRowTemplate setPredicate:].cold.1
+ -[_AMDateRelativeToCalendarUnitsRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMDateRelativeToCalendarUnitsRowTemplate initWithName:withKeyPath:isForPast:].cold.1
+ -[_AMDateRelativeToCalendarUnitsRowTemplate initWithName:withKeyPath:isForPast:].cold.2
+ -[_AMDateRelativeToCalendarUnitsRowTemplate setPredicate:].cold.1
+ -[_AMDaysRelativeToCalendarUnitsRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMDaysRelativeToCalendarUnitsRowTemplate initWithName:withKeyPath:isForPast:].cold.1
+ -[_AMDaysRelativeToCalendarUnitsRowTemplate initWithName:withKeyPath:isForPast:].cold.2
+ -[_AMDaysRelativeToCalendarUnitsRowTemplate setPredicate:].cold.1
+ -[_AMDaysRelativeToSpecificDateRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMDaysRelativeToSpecificDateRowTemplate initWithName:withKeyPath:].cold.1
+ -[_AMDaysRelativeToSpecificDateRowTemplate initWithName:withKeyPath:].cold.2
+ -[_AMDaysRelativeToSpecificDateRowTemplate setPredicate:].cold.1
+ -[_AMFileLabelRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMFileLabelRowTemplate initWithName:withKeyPath:].cold.1
+ -[_AMFileLabelRowTemplate initWithName:withKeyPath:].cold.2
+ -[_AMFileLabelRowTemplate setPredicate:].cold.1
+ -[_AMFileSizeRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMFileSizeRowTemplate initWithName:withKeyPath:].cold.1
+ -[_AMFileSizeRowTemplate initWithName:withKeyPath:].cold.2
+ -[_AMFileSizeRowTemplate setPredicate:].cold.1
+ -[_AMFinderItemsRowTemplateFactory finderItemsKindEvaluationPredicateForUIPredicate:].cold.1
+ -[_AMFinderItemsRowTemplateFactory finderItemsKindEvaluationPredicateForUIPredicate:].cold.2
+ -[_AMFinderItemsRowTemplateFactory finderItemsKindRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMFinderItemsRowTemplateFactory rowTemplatesWithLeftPopupName:leftKeyPath:operators:rightPopupNames:rightPopupValues:].cold.1
+ -[_AMFinderItemsRowTemplateFactory rowTemplatesWithLeftPopupName:leftKeyPath:operators:rightPopupNames:rightPopupValues:].cold.2
+ -[_AMFinderItemsRowTemplateFactory rowTemplatesWithLeftPopupName:leftKeyPath:operators:rightPopupNames:rightPopupValues:].cold.3
+ -[_AMPredicateEditorAction setUpUIForItemType:withPredicate:].cold.1
+ -[_AMPredicateEditorAction setUpUIForItemType:withPredicate:].cold.2
+ -[_AMRatingRowTemplate initWithName:withKeyPath:].cold.1
+ -[_AMRatingRowTemplate initWithName:withKeyPath:].cold.2
+ -[_AMRatingRowTemplate setPredicate:].cold.1
+ -[_AMRowTemplateFactory convertToEvaluationPredicateFromComparisonUIPredicate:withItemType:].cold.1
+ -[_AMRowTemplateFactory convertToEvaluationPredicateFromCompoundUIPredicate:withItemType:].cold.1
+ -[_AMRowTemplateFactory integerRowTemplateWithName:andKeyPath:withMinimum:].cold.1
+ -[_AMRowTemplateFactory integerRowTemplateWithName:andKeyPath:withMinimum:].cold.2
+ -[_AMRowTemplateFactory longStringRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMRowTemplateFactory rowTemplateBestMatchingPredicate:withItemType:].cold.1
+ -[_AMRowTemplateFactory rowTemplatesForRowTemplateFactoryTypes:].cold.1
+ -[_AMRowTemplateFactory rowTemplatesForRowTemplateFactoryTypes:].cold.2
+ -[_AMRowTemplateFactory stringRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMSpecificDateRangeRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMSpecificDateRangeRowTemplate initWithName:withKeyPath:].cold.1
+ -[_AMSpecificDateRangeRowTemplate initWithName:withKeyPath:].cold.2
+ -[_AMSpecificDateRangeRowTemplate setPredicate:].cold.1
+ -[_AMSuffixLabeledRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMTimeIntervalRowTemplate convertToEvaluationPredicateFromUIPredicate:].cold.1
+ -[_AMTimeIntervalRowTemplate initWithName:withKeyPath:].cold.1
+ -[_AMTimeIntervalRowTemplate initWithName:withKeyPath:].cold.2
+ -[_AMTimeIntervalRowTemplate setPredicate:].cold.1
+ -[_AMiPhotoItemsRowTemplateFactory _spotlightIPhotoPhotoPredicateForPersistentPredicate:].cold.1
+ -[_AMiPhotoItemsRowTemplateFactory apertureRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMiPhotoItemsRowTemplateFactory apertureRowTemplatesWithName:andKeyPath:].cold.2
+ -[_AMiPhotoItemsRowTemplateFactory pixelRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMiPhotoItemsRowTemplateFactory pixelRowTemplatesWithName:andKeyPath:].cold.2
+ -[_AMiPhotoItemsRowTemplateFactory shutterSpeedRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMiPhotoItemsRowTemplateFactory shutterSpeedRowTemplatesWithName:andKeyPath:].cold.2
+ -[_AMiPhotoItemsRowTemplateFactory stringRowTemplatesForAnyItemInCollectionWithName:andKeyPath:].cold.1
+ -[_AMiTunesItemsRowTemplateFactory bitRateRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMiTunesItemsRowTemplateFactory bitRateRowTemplatesWithName:andKeyPath:].cold.2
+ -[_AMiTunesItemsRowTemplateFactory sampleRateRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMiTunesItemsRowTemplateFactory sampleRateRowTemplatesWithName:andKeyPath:].cold.2
+ -[_AMiTunesItemsRowTemplateFactory specificYearRowTemplatesWithName:andKeyPath:].cold.1
+ -[_AMiTunesItemsRowTemplateFactory specificYearRowTemplatesWithName:andKeyPath:].cold.2
+ -[_AMiTunesItemsRowTemplateFactory specificYearRowTemplatesWithName:andKeyPath:].cold.3
+ AMSecAssessIsURLSignedByApple.cold.3
+ AutomatorSecurityHelperHostInterface.cold.1
+ AutomatorSecurityHelperServiceInterface.cold.1
+ GCC_except_table61
+ _AMAuditTokenForCurrentProcess.cold.2
+ _AMAutomatorApplicationStubBundle.cold.1
+ _AMAutomatorFrameworkBundle.cold.1
+ _AMBundleIdentifiersOfAutomatorComponents.cold.1
+ _AMIsAppleInternal.cold.1
+ _AMRunningInAutomatorApp.cold.1
+ _AMRunningInsideActionLoaderService.cold.1
+ _AMRunningInsideAppleSignedApplicationWithBundleIdentifier.cold.1
+ _AMRunningInsideRunner.cold.1
+ _AMVariableBuiltInIdentifiers.cold.1
+ _AMVariableChildIdentifiers.cold.1
+ _AMVariableEditableIdentifiers.cold.1
+ _AMVariableTemplateIdentifiers.cold.1
+ __35-[AMLibraryViewController loadView]_block_invoke.cold.1
+ __45-[AMFFeedElement childrenWithName:namespace:]_block_invoke.cold.1
+ __54-[AMSecurityHelperWindowController _connectViewBridge]_block_invoke.cold.1
+ __54-[AMSecurityHelperWindowController _connectViewBridge]_block_invoke.cold.2
+ __59-[_AMiCalPredicateEditorAction runAsynchronouslyWithInput:]_block_invoke.cold.1
+ __66+[AMWorkflowPersonality _instantiateWorkflowPersonalitiesIfNeeded]_block_invoke.cold.1
+ __84-[AMRemoteAction remoteActionFinishedRunningAsynchronouslyWithOutput:stopped:error:]_block_invoke.cold.1
+ _fixUpBundleIdentifer.cold.1
+ workflow_service_runner_xpc_main.cold.1
- GCC_except_table50
- _NSURLVolumeURLKey
- _objc_msgSend$runningApplicationsWithBundleIdentifier:
CStrings:
- "runningApplicationsWithBundleIdentifier:"

```
