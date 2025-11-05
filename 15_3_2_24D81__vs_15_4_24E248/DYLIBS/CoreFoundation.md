## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation`

```diff

-3302.1.400.0.0
-  __TEXT.__text: 0x1f05a4
-  __TEXT.__auth_stubs: 0x3360
+3423.0.0.0.0
+  __TEXT.__text: 0x1fc0f8
+  __TEXT.__auth_stubs: 0x33b0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x7e3c
-  __TEXT.__const: 0x18c474
-  __TEXT.__oslogstring: 0x9275
-  __TEXT.__cstring: 0xba6a7
-  __TEXT.__gcc_except_tab: 0x4a1c
-  __TEXT.__ustring: 0x14b6
+  __TEXT.__objc_methlist: 0x7f1c
+  __TEXT.__const: 0x19b7b4
+  __TEXT.__oslogstring: 0xa97f
+  __TEXT.__cstring: 0xbb177
+  __TEXT.__gcc_except_tab: 0x50b0
+  __TEXT.__ustring: 0x1440
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__dof_NSAppNap: 0x4cf
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x6a44
+  __TEXT.__unwind_info: 0x6f48
   __TEXT.__eh_frame: 0x684
   __TEXT.__objc_classname: 0xbfa
-  __TEXT.__objc_methname: 0x93ae
-  __TEXT.__objc_methtype: 0x88b44
-  __TEXT.__objc_stubs: 0x6f60
-  __DATA_CONST.__const: 0x2a15f0
+  __TEXT.__objc_methname: 0x9a2a
+  __TEXT.__objc_methtype: 0xb4223
+  __TEXT.__objc_stubs: 0x74a0
+  __DATA_CONST.__const: 0x361128
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x71f0
-  __DATA_CONST.__objc_selrefs: 0x2aa8
+  __DATA_CONST.__objc_const: 0x7380
+  __DATA_CONST.__objc_selrefs: 0x2be8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x2f0
+  __DATA_CONST.__objc_classrefs: 0x310
   __DATA_CONST.__objc_superrefs: 0x328
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__objc_arraydata: 0x1570
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__objc_arraydata: 0x15a0
   __AUTH_CONST.__const_cfobj2: 0x40
-  __AUTH_CONST.__const: 0x8978
-  __AUTH_CONST.__cfstring: 0xd5180
+  __AUTH_CONST.__const: 0x8ef8
+  __AUTH_CONST.__cfstring: 0xd5540
   __AUTH_CONST.__objc_const: 0x3e78
-  __AUTH_CONST.__objc_dictobj: 0x7f8
+  __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x19c8
+  __AUTH_CONST.__auth_got: 0x19f0
   __AUTH.__objc_data: 0xd70
-  __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0xf85
+  __AUTH.__data: 0x130
+  __DATA.__objc_ivar: 0x614
+  __DATA.__data: 0xf25
   __DATA.__thread_vars: 0x18
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x40
   __DATA.__thread_data: 0x4
-  __DATA.__bss: 0xa50
+  __DATA.__bss: 0xbe0
   __DATA.__common: 0x408
-  __DATA_DIRTY.__const: 0x6570
+  __DATA_DIRTY.__const: 0x6690
   __DATA_DIRTY.__objc_data: 0x21c0
   __DATA_DIRTY.__data: 0x100
-  __DATA_DIRTY.__bss: 0xc48
+  __DATA_DIRTY.__bss: 0xc20
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/liboah.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 190E6A36-FCAA-3EA3-94BB-7009C44653DA
-  Functions: 8557
-  Symbols:   15343
-  CStrings:  71126
+  UUID: 39E0F63A-3AB8-39E9-97F8-333CDE9A7BA4
+  Functions: 9123
+  Symbols:   16337
+  CStrings:  74414
 
Symbols:
+ +[NSInvocation _invocationWithMethodSignature:frame:].cold.2
+ +[NSObject(NSObject) load].cold.1
+ +[NSURL __unurl].cold.1
+ +[_CFPasteboardStore pasteboardStoreWithName:createIfNecessary:].cold.1
+ +[_CFPrefsSynchronizer sharedInstance].cold.1
+ +[_CFXPreferences copyDefaultPreferences].cold.1
+ +[__NSPlaceholderDate initialize].cold.1
+ -[CFPDCloudSource initWithDomain:userName:storeName:configurationPath:containerPath:shmemIndex:daemon:].cold.1
+ -[CFPDSource acceptMessage:].cold.8
+ -[CFPDSource beginHandlingRequest].cold.3
+ -[CFPDSource createDiskWrite].cold.2
+ -[CFPDSource processEndOfMessageIntendingToRemoveSource:replacingWithTombstone:].cold.1
+ -[CFPDSource processEndOfMessageIntendingToRemoveSource:replacingWithTombstone:].cold.2
+ -[CFPDSource processEndOfMessageIntendingToRemoveSource:replacingWithTombstone:].cold.3
+ -[CFPDSource setDirty:].cold.1
+ -[CFPrefsDaemon handleMessage:fromPeer:replyHandler:].cold.2
+ -[CFPrefsDaemon handleMultiMessage:replyHandler:].cold.2
+ -[CFPrefsDaemon handleMultiMessage:replyHandler:].cold.3
+ -[CFPrefsDaemon handleSourceMessage:replyHandler:].cold.2
+ -[CFPrefsDaemon initWithRole:testMode:].cold.2
+ -[CFPrefsDaemon withAgentDictionaryIfApplicable:].cold.2
+ -[CFPrefsPlistSource handleErrorReply:toMessage:settingKeys:toValues:count:retryCount:retryContinuation:].cold.11
+ -[CFPrefsPlistSource handleErrorReply:toMessage:settingKeys:toValues:count:retryCount:retryContinuation:].cold.12
+ -[CFPrefsPlistSource sendRequestNewDataMessage:toConnection:retryCount:error:].cold.1
+ -[CFPrefsPlistSource setDomainIdentifier:].cold.2
+ -[CFPrefsSearchListSource _getPendingNotifications].cold.2
+ -[CFPrefsSearchListSource alreadylocked_copyValueForKey:].cold.2
+ -[CFPrefsSearchListSource alreadylocked_copyValueForKey:].cold.3
+ -[CFPrefsSearchListSource alreadylocked_copyValueForKey:].cold.4
+ -[CFPrefsSearchListSource copyCloudConfigurationWithURL:outConfigFileSource:outStoreName:].cold.3
+ -[CFPrefsSearchListSource copyCloudConfigurationWithURL:outConfigFileSource:outStoreName:].cold.4
+ -[CFPrefsSearchListSource generationCount].cold.1
+ -[CFPrefsSearchListSource replaceSource:withSource:].cold.2
+ -[NSInvocation _initWithMethodSignature:frame:buffer:size:].cold.2
+ -[NSInvocation copyWithZone:].cold.4
+ -[NSInvocation invokeSuper].cold.3
+ -[NSInvocation invokeUsingIMP:].cold.3
+ -[NSInvocation invoke].cold.3
+ -[NSInvocation retainArguments].cold.4
+ -[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]
+ -[_CFGeneralPasteboardStore _ensureCSUIAIsRunning].cold.1
+ -[_CFGeneralPasteboardStore _ensureCSUIAIsRunning].cold.2
+ -[_CFGeneralPasteboardStore _ensureCSUIAIsRunning].cold.3
+ -[_CFGeneralPasteboardStore _ensureCSUIAIsRunning].cold.4
+ -[_CFGeneralPasteboardStore _onDialogQueue_sendShowInAppApprovalDialogIPC]
+ -[_CFGeneralPasteboardStore _onDialogQueue_sendShowIndirectApprovalDialogIPCForCLIProcess:]
+ -[_CFGeneralPasteboardStore _onqueue_isManagedPromiseDragWithCache:forGeneration:itemIdentifier:]
+ -[_CFGeneralPasteboardStore _onqueue_isPasteLocationRelatedEntryAllowedForMessage:]
+ -[_CFGeneralPasteboardStore _onqueue_postflightNewEntries:forMessage:withPreflightData:]
+ -[_CFGeneralPasteboardStore _onqueue_postflightNewEntries:forMessage:withPreflightData:].cold.1
+ -[_CFGeneralPasteboardStore _onqueue_preflightNewEntries:forMessage:]
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:]
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.1
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.2
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.3
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.4
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.5
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.6
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.7
+ -[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:].cold.8
+ -[_CFGeneralPasteboardStore _showCurrentApprovalDialogAndWaitForReply]
+ -[_CFGeneralPasteboardStore getUserApproval:inApp:withCompletion:]
+ -[_CFGeneralPasteboardStore onqueue_handleDeadClient:withUUID:].cold.2
+ -[_CFPasteboardCache lastPboardError]
+ -[_CFPasteboardCache setLastPboardError:]
+ -[_CFPasteboardClientInstanceID auditToken]
+ -[_CFPasteboardClientInstanceID isCSUIA]
+ -[_CFPasteboardEntry _setRemotePromiseState:]
+ -[_CFPasteboardEntry didLeakExtension]
+ -[_CFPasteboardEntry requestDataForPasteboard:generation:immediatelyAvailableResult:].cold.1
+ -[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:]
+ -[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:].cold.1
+ -[_CFPasteboardEntry setDidLeakExtension:]
+ -[_CFPasteboardStore _handleDetectionOfType:withMessage:]
+ -[_CFPasteboardStore _onqueue_beginGenerationWithNewOwner:].cold.1
+ -[_CFPasteboardStore _onqueue_beginGenerationWithNewOwner:].cold.2
+ -[_CFPasteboardStore _onqueue_handleNewRegularEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:]
+ -[_CFPasteboardStore _onqueue_handleNewRegularEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:].cold.1
+ -[_CFPasteboardStore _onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:]
+ -[_CFPasteboardStore _onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:].cold.1
+ -[_CFPasteboardStore _onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:].cold.2
+ -[_CFPasteboardStore _onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:].cold.3
+ -[_CFPasteboardStore _onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:].cold.4
+ -[_CFPasteboardStore _onqueue_isManagedPromiseDragWithCache:forGeneration:itemIdentifier:]
+ -[_CFPasteboardStore _onqueue_isPasteLocationRelatedEntryAllowedForMessage:]
+ -[_CFPasteboardStore _onqueue_postflightNewEntries:forMessage:withPreflightData:]
+ -[_CFPasteboardStore _onqueue_preflightNewEntries:forMessage:]
+ -[_CFPasteboardStore getUserApproval:inApp:withCompletion:]
+ -[_CFPasteboardStore handleDetectMetadata:]
+ -[_CFPasteboardStore handleDetectPatterns:]
+ -[_CFPasteboardStore handleDetectValues:]
+ -[_CFPasteboardStore onqueue_analyzeSandboxExtensionEntry:destinedForClient:]
+ -[_CFPasteboardStore onqueue_filterDataFromEntry:inResponseToMessage:error:]
+ -[_CFPasteboardStore onqueue_filterDataFromEntry:inResponseToMessage:error:].cold.1
+ -[_CFPasteboardStore onqueue_filterDataFromEntry:inResponseToMessage:error:].cold.2
+ -[_CFPasteboardStore onqueue_reissueSandboxExtensionFromEntry:toClient:error:]
+ -[_CFRemotePasteboardCache prepareDataForItemIdentifier:flavor:].cold.1
+ -[_CFRemotePasteboardCache prepareMetadata].cold.1
+ -[_CFXPreferences canLookUpAgents].cold.1
+ -[_CFXPreferences ingestVolatileStateFromPreferences:].cold.2
+ -[_CFXPreferences setAccessRestricted:forAppIdentifier:].cold.2
+ -[_CFXPreferences withSourceForIdentifier:user:byHost:container:cloud:perform:].cold.2
+ -[__NSFastEnumerationEnumerator initWithObject:].cold.1
+ -[__NSPlaceholderOrderedSet initWithObjects:count:].cold.1
+ CFArrayCreate.cold.1
+ CFArrayCreateCopy.cold.1
+ CFArrayCreateMutable.cold.1
+ CFArrayCreateMutableCopy.cold.1
+ CFBasicHashGetPtrIndex.cold.1
+ CFBundleAllowMixedLocalizations.cold.1
+ CFBundleCloseBundleResourceMap.cold.1
+ CFBundleGetMainBundle.cold.2
+ CFBundleOpenBundleResourceMap.cold.1
+ CFCharacterSetAddCharactersInString.cold.2
+ CFCharacterSetInvert.cold.2
+ CFCharacterSetRemoveCharactersInString.cold.2
+ CFDataReplaceBytes.cold.13
+ CFDateGetTypeID.cold.1
+ CFFileDescriptorCreateRunLoopSource.cold.1
+ CFFileDescriptorDisableCallBacks.cold.1
+ CFFileDescriptorEnableCallBacks.cold.1
+ CFFileDescriptorGetContext.cold.1
+ CFFileDescriptorGetNativeDescriptor.cold.1
+ CFFileDescriptorGetTypeID.cold.1
+ CFFileDescriptorInvalidate.cold.1
+ CFFileDescriptorIsValid.cold.1
+ CFGetSystemUptime.cold.1
+ CFMessagePortSetDispatchQueue.cold.1
+ CFNotificationCenterGetDarwinNotifyCenter.cold.1
+ CFNotificationCenterGetDistributedCenter.cold.1
+ CFNotificationCenterGetLocalCenter.cold.1
+ CFNumberCreate.cold.1
+ CFNumberGetTypeID.cold.1
+ CFPasteboardCopyData.cold.2
+ CFPasteboardCreate.cold.2
+ CFPasteboardDetectMetadataForTypes.cold.1
+ CFPasteboardDetectPatternsForPatterns.cold.1
+ CFPasteboardDetectValuesForPatterns.cold.1
+ CFPasteboardIsPrivacyDeveloperPreviewEnabled.cold.1
+ CFPasteboardIsPrivacyDeveloperPreviewEnabled.onceToken
+ CFPasteboardIsPrivacyDeveloperPreviewEnabled.sIsDevPreviewEnabled
+ CFPasteboardSetPasteboardValidationCallbacks.cold.1
+ CFPlugInAddInstanceForFactory.cold.3
+ CFPlugInAddInstanceForFactory.cold.4
+ CFPlugInFindFactoriesForPlugInType.cold.2
+ CFPlugInFindFactoriesForPlugInTypeInPlugIn.cold.1
+ CFPlugInInstanceCreate.cold.5
+ CFPlugInInstanceCreate.cold.6
+ CFPlugInInstanceCreate.cold.7
+ CFPlugInInstanceCreate.cold.8
+ CFPlugInInstanceCreate.cold.9
+ CFPlugInRemoveInstanceForFactory.cold.3
+ CFPlugInRemoveInstanceForFactory.cold.4
+ CFPlugInUnregisterFactory.cold.2
+ CFPlugInUnregisterPlugInType.cold.2
+ CFPreferencesAppSynchronize.cold.1
+ CFPreferencesAppValueIsForced.cold.1
+ CFRunLoopAddCommonMode.cold.1
+ CFRunLoopAddObserver.cold.1
+ CFRunLoopAddSource.cold.1
+ CFRunLoopAddTimer.cold.1
+ CFRunLoopContainsObserver.cold.1
+ CFRunLoopContainsSource.cold.1
+ CFRunLoopContainsTimer.cold.1
+ CFRunLoopGetMain.cold.1
+ CFRunLoopGetNextTimerFireDate.cold.1
+ CFRunLoopIsWaiting.cold.1
+ CFRunLoopPerformBlock.cold.1
+ CFRunLoopRemoveObserver.cold.1
+ CFRunLoopRemoveSource.cold.1
+ CFRunLoopRemoveTimer.cold.1
+ CFRunLoopRunSpecific.cold.3
+ CFRunLoopStop.cold.1
+ CFRunLoopTimerCreate.cold.2
+ CFRunLoopTimerSetNextFireDate.cold.1
+ CFRunLoopWakeUp.cold.2
+ CFServiceControllerPerformService.cold.1
+ CFServiceControllerRegisterProvider.cold.1
+ CFSocketConnectToAddress.cold.1
+ CFSocketCopyAddress.cold.1
+ CFSocketCopyPeerAddress.cold.1
+ CFSocketCreateRunLoopSource.cold.1
+ CFSocketCreateWithNative.cold.1
+ CFSocketDisableCallBacks.cold.1
+ CFSocketEnableCallBacks.cold.1
+ CFSocketGetContext.cold.1
+ CFSocketGetNative.cold.1
+ CFSocketGetSocketFlags.cold.1
+ CFSocketGetTypeID.cold.1
+ CFSocketInvalidate.cold.1
+ CFSocketIsValid.cold.1
+ CFSocketSendData.cold.1
+ CFSocketSetAddress.cold.1
+ CFSocketSetSocketFlags.cold.1
+ CFStringConvertEncodingToIANACharSetName.cold.1
+ CFStringConvertIANACharSetNameToEncoding.cold.1
+ CFStringConvertIANACharSetNameToEncoding.cold.2
+ CFStringConvertIANACharSetNameToEncoding.cold.3
+ CFStringConvertIANACharSetNameToEncoding.cold.4
+ CFStringGetMostCompatibleMacStringEncoding.cold.1
+ CFStringGetNameOfEncoding.cold.1
+ CFStringTokenizerCopyBestStringLanguage.cold.1
+ CFStringTokenizerCopyBestStringLanguageWithHints.cold.1
+ CFStringTokenizerCreate.cold.1
+ CFURLCopyParameterString.cold.2
+ CFURLCreateAbsoluteURLWithBytes.cold.1
+ CFURLCreateDataAndPropertiesFromResource.cold.1
+ CFURLCreateFromFSRef.cold.1
+ CFURLDestroyResource.cold.1
+ CFURLGetByteRangeForComponent.cold.1
+ CFURLWriteDataAndPropertiesToResource.cold.1
+ CF_IS_OBJC_CHECKING_CONSTANT_STRING.cold.1
+ CanonicalFileURLStringToFileSystemRepresentation.cold.1
+ CreateStringFromFileSystemRepresentationByAddingPercentEscapes.cold.1
+ DataDetectorsCoreLibrary.frameworkLibrary
+ GCC_except_table106
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table132
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table183
+ GCC_except_table192
+ GCC_except_table199
+ GCC_except_table208
+ GCC_except_table228
+ GCC_except_table26
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table307
+ GCC_except_table83
+ GCC_except_table86
+ ImageIOLibrary.frameworkLibrary
+ OBJC_IVAR_$__CFGeneralPasteboardStore._coreServicesUIAgentClientInstance
+ OBJC_IVAR_$__CFPasteboardCache.didHandleCreate
+ OBJC_IVAR_$__CFPasteboardCache.lastPboardError
+ OBJC_IVAR_$__CFPasteboardClientInstanceID._auditToken
+ OBJC_IVAR_$__CFPasteboardClientInstanceID._hasCheckedPath
+ OBJC_IVAR_$__CFPasteboardClientInstanceID._isCSUIA
+ OBJC_IVAR_$__CFPasteboardEntry._didLeakExtension
+ OBJC_IVAR_$__CFPasteboardEntry._localPromiseState
+ OBJC_IVAR_$__CFPasteboardEntry._localPromisor
+ OBJC_IVAR_$__CFPasteboardEntry._remotePromiseState
+ OBJC_IVAR_$__CFPasteboardEntry._remotePromisor
+ OBJC_IVAR_$__CFPasteboardStore._destinationProcessID
+ OBJC_IVAR_$__CFPasteboardStore._detectionLastDialogGeneration
+ OBJC_IVAR_$__CFPasteboardStore._detectionLastDialogRequestTime
+ OBJC_IVAR_$__CFPasteboardStore._detectionLastDialogResponse
+ OBJC_IVAR_$__CFPasteboardStore._patternDetectionQueue
+ SafariSharedLibrary.frameworkLibrary
+ UniformTypeIdentifiersLibrary.frameworkLibrary
+ WindowsPathToURLPath.cold.1
+ _CFAccentuatedStringCreate.cold.1
+ _CFAppSleepMonitorSystemAudioVolumeChanges.cold.1
+ _CFAppSleepSetupAppSleepDebug.cold.1
+ _CFAppVersionCheck.cold.1
+ _CFAppVersionCheckLessThan.cold.3
+ _CFAppVersionLessThan.cold.1
+ _CFAuditTokenForSelf.cold.1
+ _CFBundleAddToTablesLocked.cold.2
+ _CFBundleAddToTablesLocked.cold.3
+ _CFBundleCopyBundleLocalizations.cold.1
+ _CFBundleCopyLocalizedStringForLocalizationTableURLAndMarkdownOption.cold.1
+ _CFBundleCopyLocalizedStringForLocalizationTableURLAndMarkdownOption.cold.2
+ _CFBundleCopyLocalizedStringForLocalizations
+ _CFBundleCopyPreferredLanguagesInList.cold.1
+ _CFBundleCopyPreferredLanguagesInList.cold.2
+ _CFBundleCopyPreferredLanguagesInList.cold.3
+ _CFBundleCopyXPCBootstrapMainBundleLanguages.cold.1
+ _CFBundleCreate.cold.10
+ _CFBundleCreate.cold.6
+ _CFBundleCreate.cold.7
+ _CFBundleCreate.cold.8
+ _CFBundleCreate.cold.9
+ _CFBundleDeallocatePlugIn.cold.2
+ _CFBundleEnsureBundleExistsForImagePath.cold.3
+ _CFBundleEnsureBundleExistsForImagePath.cold.4
+ _CFBundleForksCouldBeResourceFile.cold.1
+ _CFBundleGetProductNameSuffix.cold.1
+ _CFBundleInitPlugIn.cold.2
+ _CFBundleLoadExecutableAndReturnError.cold.4
+ _CFBundleLoadExecutableAndReturnError.cold.5
+ _CFBundleLoadExecutableAndReturnError.cold.6
+ _CFBundleLoadingLogger.cold.1
+ _CFBundleLocalizedStringLogger.cold.1
+ _CFBundleResourceLogger.cold.1
+ _CFCopyResolvedFormatStringWithConfiguration.cold.1
+ _CFCopyResolvedFormatStringWithConfiguration.cold.2
+ _CFCopyServerVersionDictionary.cold.1
+ _CFCopySupplementalVersionDictionary.cold.1
+ _CFCopySystemVersionDictionary.cold.1
+ _CFCopySystemVersionPlatformDictionary.cold.1
+ _CFCreateURLFromFSSpec.cold.1
+ _CFErrorOSStatusCallBack.cold.1
+ _CFErrorOSStatusCallBack.cold.2
+ _CFErrorSetCallStackReturnAddresses.cold.1
+ _CFFoundationRuntimeIssuesLog.cold.1
+ _CFGetCachedUnsandboxedHomeDirectoryForCurrentUser.cold.1
+ _CFGetProductName.cold.1
+ _CFHyphenationGetLinguisticDataPath.cold.1
+ _CFICULog.cold.1
+ _CFLookupDiskArbitrationFunction.cold.1
+ _CFMachPortCreateWithPort4.cold.4
+ _CFMethodSignatureROMLog.cold.1
+ _CFOSLog.cold.1
+ _CFOperatingSystemVersionGetCurrent.cold.1
+ _CFOperatingSystemVersionIsAtLeastVersion.cold.1
+ _CFPFactoryCommonCreateLocked.cold.2
+ _CFPFactoryDeallocate.cold.2
+ _CFPFactoryDisableLocked.cold.2
+ _CFPFactoryRemoveInstanceLocked.cold.2
+ _CFPFactoryRemoveTypeLocked.cold.2
+ _CFPasteboardAllowedMetadataClasses.onceToken
+ _CFPasteboardAllowedMetadataClasses.sClasses
+ _CFPasteboardAttachSecurityScopeFromDataToURL.cold.1
+ _CFPasteboardCheckSandboxAccessToPath.cold.1
+ _CFPasteboardCheckSandboxAccessToPath.cold.2
+ _CFPasteboardCheckSandboxAccessToPath.cold.3
+ _CFPasteboardCheckSandboxAccessToPath.cold.4
+ _CFPasteboardDetectMetadataForTypes
+ _CFPasteboardDetectPatternsForPatterns
+ _CFPasteboardDetectValuesForPatterns
+ _CFPasteboardDetectionsDetectValuesForPatterns.cold.1
+ _CFPasteboardHandleCancelIndirectApprovalDialogMessage.cold.1
+ _CFPasteboardHandleCancelIndirectApprovalDialogMessage.cold.2
+ _CFPasteboardHandleCancelIndirectApprovalDialogMessage.cold.3
+ _CFPasteboardHandleCancelIndirectApprovalDialogMessage.cold.4
+ _CFPasteboardHandleCancelIndirectApprovalDialogMessage.cold.5
+ _CFPasteboardHandleCancelIndirectApprovalDialogMessage.cold.6
+ _CFPasteboardHandleShowInAppApprovalDialogMessage.cold.1
+ _CFPasteboardHandleShowInAppApprovalDialogMessage.cold.2
+ _CFPasteboardHandleShowInAppApprovalDialogMessage.cold.3
+ _CFPasteboardHandleShowInAppApprovalDialogMessage.cold.4
+ _CFPasteboardHandleShowIndirectApprovalDialogMessage.cold.1
+ _CFPasteboardHandleShowIndirectApprovalDialogMessage.cold.2
+ _CFPasteboardHandleShowIndirectApprovalDialogMessage.cold.3
+ _CFPasteboardHandleShowIndirectApprovalDialogMessage.cold.4
+ _CFPasteboardHandleShowIndirectApprovalDialogMessage.cold.5
+ _CFPasteboardHandleShowIndirectApprovalDialogMessage.cold.6
+ _CFPasteboardIsPrivacyDeveloperPreviewEnabled
+ _CFPasteboardMustCheckSandboxAccessForProcess.cold.1
+ _CFPasteboardProcessHasEntitlement.cold.1
+ _CFPasteboardProcessHasEntitlement.cold.2
+ _CFPasteboardProcessHasEntitlement.onceToken
+ _CFPasteboardProcessHasEntitlement.sHaveSecurityFunctions
+ _CFPasteboardPromiseDataUsingAsyncBlock
+ _CFPasteboardSetPasteboardValidationCallbacks
+ _CFPasteboardTestingAccessConsumedSandboxExtensions.array
+ _CFPasteboardTestingAccessConsumedSandboxExtensions.lock
+ _CFPasteboardWantSandboxExtensionForFlavor.cold.1
+ _CFPlugInRegisterPlugInTypeLocked.cold.3
+ _CFPlugInRegisterPlugInTypeLocked.cold.4
+ _CFPlugInUnloadScheduledPlugIns.cold.1
+ _CFPlugInUnscheduleForUnloading.cold.2
+ _CFPreferencesAddSuitePreferencesToAppWithContainer.cold.1
+ _CFPreferencesAppSynchronizeWithContainer.cold.1
+ _CFPreferencesCopyAppValueWithContainerAndConfiguration.cold.1
+ _CFPreferencesCopyKeyListWithContainer.cold.1
+ _CFPreferencesCopyMultipleManaged.cold.1
+ _CFPreferencesCopyMultipleWithContainer.cold.1
+ _CFPreferencesCopyValueWithContainer.cold.1
+ _CFPreferencesGetFileProtectionClass.cold.1
+ _CFPreferencesHasAppCloudValue.cold.1
+ _CFPreferencesHasAppValue.cold.1
+ _CFPreferencesRegisterStandardUserDefaultsExists.cold.1
+ _CFPreferencesRemoveSuitePreferencesFromAppWithContainer.cold.1
+ _CFPreferencesSetAccessRestricted.cold.1
+ _CFPreferencesSetAppValueWithContainerAndConfiguration.cold.1
+ _CFPreferencesSetDaemonCacheEnabled.cold.1
+ _CFPreferencesSetFileProtectionClass.cold.1
+ _CFPreferencesSynchronizeWithContainer.cold.1
+ _CFPrefsClientLog.cold.1
+ _CFPrefsCopyAppDictionaryWithContainer.cold.1
+ _CFPrefsCopyDirectModeConnection.cold.1
+ _CFPrefsDaemonLog.cold.1
+ _CFPrefsDeliverPendingKVONotificationsGuts.cold.1
+ _CFPrefsDirectMode.cold.1
+ _CFPrefsDirectMode.cold.2
+ _CFPrefsDirectModeEnabledForDomain.cold.1
+ _CFPrefsExtractQuadrupleFromPathIfPossible.cold.4
+ _CFPrefsGetEntitlementForMessageWithLockedContext.cold.4
+ _CFPrefsGetFixedUpDomainForMessage.cold.2
+ _CFPrefsGetPathForManagedBundleID.cold.2
+ _CFPrefsGetPathForManagedBundleID.cold.3
+ _CFPrefsRegisterUserDefaultsInstanceWithCloudConfigurationURL.cold.1
+ _CFPrefsResetPreferences.cold.1
+ _CFPrefsSynchronizeForProcessTermination.cold.1
+ _CFPrefsTemporaryFDToWriteTo.cold.7
+ _CFPrefsUnregisterUserDefaultsInstance.cold.1
+ _CFRelease.cold.4
+ _CFRelease.cold.5
+ _CFRetain.cold.3
+ _CFRuntimeIssuesLog.cold.1
+ _CFStreamSetDispatchQueue.cold.1
+ _CFStringCreateByAddingPercentEncodingWithAllowedCharacters.cold.1
+ _CFStringCreateByAddingPercentEncodingWithAllowedCharacters.cold.2
+ _CFStringCreateByAddingPercentEncodingWithAllowedCharacters.cold.3
+ _CFStringCreateWithMarkdownAndConfiguration.cold.1
+ _CFStringObjCFormatRequiresInflection.cold.1
+ _CFStringTokenizerCopyPossibleStringLanguages.cold.1
+ _CFURLComponentsGetURLFragmentAllowedCharacterSet.cold.1
+ _CFURLComponentsGetURLHostAllowedCharacterSet.cold.1
+ _CFURLComponentsGetURLPasswordAllowedCharacterSet.cold.1
+ _CFURLComponentsGetURLPathAllowedCharacterSet.cold.1
+ _CFURLComponentsGetURLPortAllowedCharacterSet.cold.1
+ _CFURLComponentsGetURLQueryAllowedCharacterSet.cold.1
+ _CFURLComponentsGetURLUserAllowedCharacterSet.cold.1
+ _CFURLCopyExtendedPropertyListPrimitive.cold.1
+ _CFURLCopyExtendedPropertyListRepresentation.cold.1
+ _CFURLCopyExtendedPropertyListRepresentation.cold.2
+ _CFURLCreateResolvedDirectoryWithString.cold.2
+ _CFURLCreateWithFileSystemPath.cold.1
+ _CFURLCreateWithFileSystemPath.cold.2
+ _CFURLCreateWithFileSystemPath.cold.3
+ _CFURLCreateWithFileSystemPath.cold.4
+ _CFURLCreateWithFileSystemRepresentation.cold.1
+ _CFURLCreateWithFileSystemRepresentation.cold.2
+ _CFURLNoteSecurityScopedResourceMoved.cold.1
+ _CFVolumeObserverGetTypeID.cold.1
+ _CFXNotificationGetTaskCenter.cold.1
+ _CFXNotificationRegisterObserver.cold.1
+ _CFXPreferencesCopyDictionaryForNamedVolatileSource.cold.1
+ _CFXPreferencesCopyDictionaryForSourceWithBundleID.cold.1
+ _CFXPreferencesCopyVolatileSourceNames.cold.1
+ _CFXPreferencesGetByHostIdentifierString.cold.1
+ _CFXPreferencesRegisterDefaultValues.cold.1
+ _CF_IS_OBJC_CHECKING_CONSTANT_STRING
+ _DDBinderEmailKeyFunction
+ _DDBinderFlightInformationKeyFunction
+ _DDBinderTrackingNumberKeyFunction
+ _DDScannerServiceConfigurationFunction
+ _DDScannerServiceFunction
+ _DDScannerSmallTimeoutFunction
+ _MergedGlobals.58
+ _NSCFCalendarLogger.cold.1
+ _NSClassFromString
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSValue
+ _OUTLINED_FUNCTION_16
+ _SANDBOX_CHECK_POSIX_READABLE
+ _SANDBOX_EXTENSION_CANONICAL
+ _UTTypeFunction
+ __107-[_CFPasteboardStore requestDataForGeneration:itemIdentifier:flavor:inResponseToMessage:completionHandler:]_block_invoke.86
+ __107-[_CFPasteboardStore requestDataForGeneration:itemIdentifier:flavor:inResponseToMessage:completionHandler:]_block_invoke.87
+ __108-[_CFXPreferences(SearchListAdditions) withSearchListForIdentifier:container:cloudConfigurationURL:perform:]_block_invoke.152.cold.1
+ __108-[_CFXPreferences(SearchListAdditions) withSearchListForIdentifier:container:cloudConfigurationURL:perform:]_block_invoke.152.cold.2
+ __118-[_CFPasteboardStore _onqueue_handleNewRegularEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:]_block_invoke.74
+ __197-[CFPrefsDaemon(SourceSupport) withSourceForDomain:inContainer:user:byHost:managed:managedUsesContainer:cloudStoreEntitlement:cloudConfigurationPath:performWithSourceLock:afterReleasingSourceLock:]_block_invoke_2.cold.1
+ __29-[CFPDSource createDiskWrite]_block_invoke.cold.1
+ __33+[__NSPlaceholderDate initialize]_block_invoke.cold.1
+ __40-[_CFPasteboardStore handleRequestData:]_block_invoke.94
+ __40-[_CFPasteboardStore handleRequestData:]_block_invoke.97
+ __41-[_CFPasteboardStore handleSetDataFlags:]_block_invoke.81
+ __44-[_CFPasteboardStore handleResolvePromises:]_block_invoke.98
+ __46-[_CFPasteboardStore handleSetExpirationDate:]_block_invoke.34
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.1
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.2
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.3
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.4
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.5
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.6
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.7
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.8
+ __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.399.cold.9
+ __50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke.349
+ __50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke.349.cold.1
+ __50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke.349.cold.2
+ __50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke.349.cold.3
+ __50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke.349.cold.4
+ __50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke.349.cold.5
+ __55-[_CFPasteboardEntry initFromXPCObject:fromConnection:]_block_invoke.cold.1
+ __55-[_CFPasteboardEntry initFromXPCObject:fromConnection:]_block_invoke.cold.2
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.43
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.44
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.46
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.53
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.63
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.63.cold.1
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.63.cold.2
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.63.cold.3
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.cold.1
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.cold.2
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.cold.3
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.cold.4
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.cold.5
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke.cold.6
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke_2.54
+ __57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke_2.67
+ __59-[_CFGeneralPasteboardStore handleVerificationTokenCreate:]_block_invoke.261
+ __62-[CFPrefsPlistSource createRequestNewContentMessageForDaemon:]_block_invoke.cold.1
+ __64-[_CFRemotePasteboardCache prepareDataForItemIdentifier:flavor:]_block_invoke.423
+ __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.268
+ __65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.cold.1
+ __66-[_CFGeneralPasteboardStore getUserApproval:inApp:withCompletion:]_block_invoke.336
+ __66-[_CFGeneralPasteboardStore getUserApproval:inApp:withCompletion:]_block_invoke_2.337
+ __67-[_CFGeneralPasteboardStore notifyRemoteGenerationBecameAvailable:]_block_invoke.284
+ __69-[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:]_block_invoke.274
+ __70-[_CFGeneralPasteboardStore _showCurrentApprovalDialogAndWaitForReply]_block_invoke.340
+ __79-[_CFPasteboardEntry(CFRemotePasteboardSupport) promiseDataWithFetchOperation:]_block_invoke.443
+ __79-[_CFPasteboardEntry(CFRemotePasteboardSupport) promiseDataWithFetchOperation:]_block_invoke.cold.1
+ __79-[_CFPasteboardEntry(CFRemotePasteboardSupport) promiseDataWithFetchOperation:]_block_invoke.cold.2
+ __88-[_CFPasteboardStore flushOwnerChangesIfNecessaryInResponseToMessage:completionHandler:]_block_invoke.116
+ __88-[_CFPasteboardStore flushOwnerChangesIfNecessaryInResponseToMessage:completionHandler:]_block_invoke.119
+ __94-[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:]_block_invoke.311
+ __94-[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:]_block_invoke_2.313
+ __Block_byref_object_copy_.627
+ __Block_byref_object_dispose_.628
+ __CFAllocateObject.cold.1
+ __CFCarbonCore_ConvertFromTextToUnicodeNoInit.cold.1
+ __CFCarbonCore_ConvertFromUnicodeToTextNoInit.cold.1
+ __CFCarbonCore_CreateTextToUnicodeInfoNoInit.cold.1
+ __CFCarbonCore_DisposeTextToUnicodeInfoNoInit.cold.1
+ __CFCarbonCore_DisposeUnicodeToTextInfoNoInit.cold.1
+ __CFCarbonCore_FSGetCatalogInfo.cold.1
+ __CFCarbonCore_FSGetResourceForkName.cold.1
+ __CFCarbonCore_FSGetVolumeInfo.cold.1
+ __CFCarbonCore_FSOpenResourceFile.cold.1
+ __CFCarbonCore_FSOpenResourceFileMapped.cold.1
+ __CFCarbonCore_FSPathMakeRef.cold.1
+ __CFCarbonCore_FSRefMakePath.cold.1
+ __CFCarbonCore_RMCloseResourceFile.cold.1
+ __CFCarbonCore_RMGetResource.cold.1
+ __CFCarbonCore_RMOpenResourceFileRef.cold.1
+ __CFCharacterSetInitialize.cold.1
+ __CFDateFormatterCreateForcedString.cold.1
+ __CFDescribeCFMachPortPerformCallout.cold.1
+ __CFDiskArbitration_DADiskCopyDescription.cold.1
+ __CFDiskArbitration_DASessionSetDispatchQueue.cold.1
+ __CFErrorCopyCallStackReturnAddresses
+ __CFErrorSetCallStackReturnAddresses
+ __CFFileDescriptorCreate_block_invoke.cold.1
+ __CFGetDYLDImageSuffix.cold.1
+ __CFGetDYLDImageSuffix.onceToken
+ __CFGetDYLDImageSuffix.suffix
+ __CFGetUGIDs.cold.1
+ __CFLookupCFNetworkFunction.cold.1
+ __CFLookupCarbonCoreFunction.cold.1
+ __CFPBStart.cold.1
+ __CFPasteboardAddPrivatePrefixToPathIfNecessary
+ __CFPasteboardCheckSandboxAccessToPath
+ __CFPasteboardClearEntitlementCacheForDeadProcess
+ __CFPasteboardConsumeSandboxExtensionDataFinalize
+ __CFPasteboardCopyData_block_invoke.102
+ __CFPasteboardCopyData_block_invoke.99
+ __CFPasteboardCreateCanonicalPath
+ __CFPasteboardCreateUniquePromiseFileURL_block_invoke_2.cold.2
+ __CFPasteboardDetectionDetectProbableWebData.cold.1
+ __CFPasteboardDetectionsDetectValuesForPatterns
+ __CFPasteboardGeneratePasteVerificationToken_block_invoke.242
+ __CFPasteboardGeneratePasteVerificationToken_block_invoke.242.cold.1
+ __CFPasteboardGeneratePasteVerificationToken_block_invoke.244
+ __CFPasteboardGeneratePasteVerificationToken_block_invoke.249
+ __CFPasteboardHandleCancelIndirectApprovalDialogMessage
+ __CFPasteboardHandleMessageFromDaemon.cold.4
+ __CFPasteboardHandleShowInAppApprovalDialogMessage
+ __CFPasteboardHandleShowIndirectApprovalDialogMessage
+ __CFPasteboardIsImageFlavor
+ __CFPasteboardIsPasteLocationRelatedFlavor
+ __CFPasteboardIsSecurityScopeFlavor
+ __CFPasteboardIsStringFlavor
+ __CFPasteboardIsURLFlavor
+ __CFPasteboardMustCheckSandboxAccessForProcess
+ __CFPasteboardProcessHasEntitlement
+ __CFPasteboardPromiseDataUsingAsyncBlock_block_invoke.207
+ __CFPasteboardPromiseDataUsingAsyncBlock_block_invoke.209
+ __CFPasteboardPromiseDataUsingBlock_block_invoke.cold.1
+ __CFPasteboardReleasePreviouslyConsumedSandboxExtensions
+ __CFPasteboardResolvePromisedData_block_invoke.213
+ __CFPasteboardStartInProcessServer.cold.1
+ __CFPasteboardStartServicingConnection.cold.1
+ __CFPasteboardTestingAccessConsumedSandboxExtensions
+ __CFPasteboardWantSandboxExtensionForFlavor
+ __CFRunLoopDoTimer.cold.2
+ __CFRunLoopDoTimers.cold.1
+ __CFRunLoopSetOptionsReason.cold.1
+ __CFRunLoopTimerCopyDescription.cold.1
+ __CFStringCreateImmutableFunnel3.cold.2
+ __CFStringDecodeByteStream3.cold.1
+ __CFStringEncodingCreateListOfAvailablePlatformConverters.cold.1
+ __CFStringEncodingCreateListOfAvailablePlatformConverters.cold.2
+ __CFStringEncodingCreateListOfAvailablePlatformConverters.cold.3
+ __CFStringEncodingPlatformUnicodeToBytes.cold.1
+ __CFTSDInitialize.cold.1
+ __CFTSRToTimeInterval.cold.1
+ __CFTimeIntervalToTSR.cold.1
+ __CFTimeIntervalUntilTSR.cold.1
+ __CFTimeIntervalUntilTSR.cold.2
+ __CFTimeIntervalUntilTSR.cold.3
+ __CFURLGetQueryResolveFlags
+ __CFXPreferencesCopyCurrentApplicationStateWithDeadlockAvoidance.cold.1
+ __InitializeURLAllowedCharacterSets_block_invoke.cold.1
+ __MergedGlobals
+ __NSCFDictionaryCreate.cold.1
+ __NSCFDictionaryCreateMutable.cold.1
+ __NSCFDictionaryCreateTransfer.cold.1
+ __NSCacheValueRelease.cold.1
+ __NSCollectionsShouldCopy.cold.1
+ __NSPasteboardDetectionPatternCalendarEvent
+ __NSPasteboardDetectionPatternDataDetectorsPrefix
+ __NSPasteboardDetectionPatternEmailAddress
+ __NSPasteboardDetectionPatternFlightNumber
+ __NSPasteboardDetectionPatternLink
+ __NSPasteboardDetectionPatternMoneyAmount
+ __NSPasteboardDetectionPatternNumber
+ __NSPasteboardDetectionPatternPhoneNumber
+ __NSPasteboardDetectionPatternPostalAddress
+ __NSPasteboardDetectionPatternPrefix
+ __NSPasteboardDetectionPatternProbableWebSearch
+ __NSPasteboardDetectionPatternProbableWebURL
+ __NSPasteboardDetectionPatternShipmentTrackingNumber
+ __NSPasteboardMetadataTypeContentType
+ __NSPasteboardMetadataTypeImageProperties
+ ___118-[_CFPasteboardStore _onqueue_handleNewRegularEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:]_block_invoke
+ ___124-[_CFPasteboardStore _onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:]_block_invoke
+ ___50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke
+ ___50-[_CFGeneralPasteboardStore _ensureCSUIAIsRunning]_block_invoke_2
+ ___57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke
+ ___57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke_2
+ ___57-[_CFPasteboardStore _handleDetectionOfType:withMessage:]_block_invoke_3
+ ___66-[_CFGeneralPasteboardStore getUserApproval:inApp:withCompletion:]_block_invoke
+ ___66-[_CFGeneralPasteboardStore getUserApproval:inApp:withCompletion:]_block_invoke_2
+ ___69-[_CFGeneralPasteboardStore _onqueue_validateToken:forRequestingApp:]_block_invoke
+ ___70-[_CFGeneralPasteboardStore _showCurrentApprovalDialogAndWaitForReply]_block_invoke
+ ___94-[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:]_block_invoke
+ ___94-[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:]_block_invoke_2
+ ___CFBundleCreateFilteredInfoPlistWithData_block_invoke_2.cold.1
+ ___CFBundleGetProductNameSuffix_block_invoke.cold.1
+ ___CFBundleInfoPlistProcessInfoDictionary_block_invoke.cold.1
+ ___CFBundleInfoPlistProcessInfoDictionary_block_invoke.cold.2
+ ___CFBundleInfoPlistProcessInfoDictionary_block_invoke.cold.3
+ ___CFBundleInfoPlistProcessInfoDictionary_block_invoke.cold.4
+ ___CFGetDYLDImageSuffix
+ ___CFNotificationCenterInitializeDependentNotificationIfNecessary_block_invoke.cold.1
+ ___CFNullHash
+ ___CFPASTEBOARDDAEMON_IS_WAITING_FOR_AN_APPROVAL_DIALOG__
+ ___CFPASTEBOARD_IS_SHOWING_AN_INDIRECT_APPROVAL_DIALOG__
+ ___CFPasteboardClientToDaemonQueue
+ ___CFPasteboardCreateSecurityScopeDataForPaths
+ ___CFPasteboardCreateSecurityScopeDataForURL
+ ___CFPasteboardDaemonIsInProcessForTesting
+ ___CFPasteboardDetectMetadataForTypes_block_invoke
+ ___CFPasteboardDetectPatternsForPatterns_block_invoke
+ ___CFPasteboardDetectValuesForPatterns_block_invoke
+ ___CFPasteboardDetect_block_invoke.557
+ ___CFPasteboardDetect_block_invoke.557.cold.1
+ ___CFPasteboardDetect_block_invoke.561
+ ___CFPasteboardDetect_block_invoke.561.cold.1
+ ___CFPasteboardDetect_block_invoke.cold.1
+ ___CFPasteboardDetect_block_invoke.cold.2
+ ___CFPasteboardDetect_block_invoke_2.cold.1
+ ___CFPasteboardDetect_block_invoke_2.cold.2
+ ___CFPasteboardDetect_block_invoke_2.cold.3
+ ___CFPasteboardDetect_block_invoke_2.cold.4
+ ___CFPasteboardDetectionDetectProbableWebData
+ ___CFPasteboardDetectionsDetectMetadataForImageSource
+ ___CFPasteboardFRTPOnceToken
+ ___CFPasteboardFRTPasteboards
+ ___CFPasteboardHandleFlushMessage_block_invoke.607
+ ___CFPasteboardHandleFlushMessage_block_invoke.610
+ ___CFPasteboardHandleFlushMessage_block_invoke.610.cold.1
+ ___CFPasteboardHandleFlushMessage_block_invoke.611
+ ___CFPasteboardHandleFlushMessage_block_invoke.611.cold.1
+ ___CFPasteboardHandleFulfillMessage_block_invoke.629
+ ___CFPasteboardHandleInvalidatedDaemonConnection_block_invoke.599
+ ___CFPasteboardIsPrivacyDeveloperPreviewEnabled_block_invoke
+ ___CFPasteboardIsTesting
+ ___CFPasteboardProcessHasEntitlement_block_invoke.cold.1
+ ___CFPasteboardPromiseDataUsingAsyncBlock_block_invoke
+ ____CFICUGetEnumStringForUCalendarDaysOfWeek
+ ____CFICUGetEnumStringForUCalendarLimitType
+ ____CFICUGetEnumStringForUNumberFormatTextAttribute
+ ____CFICUGetEnumStringForURelativeDateTimeUnit
+ ____CFPasteboardAllowedMetadataClasses_block_invoke
+ ____CFPasteboardClearEntitlementCacheForDeadProcess_block_invoke
+ ____CFPasteboardClearEntitlementCacheForDeadProcess_block_invoke_2
+ ____CFPasteboardConsumeSandboxExtensionDataFinalize_block_invoke
+ ____CFPasteboardDetect_block_invoke
+ ____CFPasteboardDetect_block_invoke_2
+ ____CFPasteboardFileReferenceTransportingPasteboards_block_invoke
+ ____CFPasteboardHandleCancelIndirectApprovalDialogMessage_block_invoke
+ ____CFPasteboardHandleFulfillMessage_block_invoke_3
+ ____CFPasteboardHandleShowApprovalDialogMessage_block_invoke.646
+ ____CFPasteboardHandleShowApprovalDialogMessage_block_invoke.647
+ ____CFPasteboardHandleShowApprovalDialogMessage_block_invoke.647.cold.1
+ ____CFPasteboardHandleShowApprovalDialogMessage_block_invoke.647.cold.2
+ ____CFPasteboardHandleShowApprovalDialogMessage_block_invoke.cold.1
+ ____CFPasteboardHandleShowApprovalDialogMessage_block_invoke.cold.2
+ ____CFPasteboardProcessHasEntitlement_block_invoke
+ ____CFPasteboardReleasePreviouslyConsumedSandboxExtensions_block_invoke
+ ____CFPasteboardReleaseSandboxExtensionHandles_block_invoke.cold.1
+ ____CFPasteboardScheduleInvalidationAheadOfNextWorkload_block_invoke
+ ____CFPasteboardScheduleInvalidationAheadOfNextWorkload_block_invoke_2
+ ____CFPasteboardStartInProcessServer_block_invoke.cold.1
+ ____CFPasteboardStartServicingConnection_block_invoke.cold.1
+ _____CFGetDYLDImageSuffix_block_invoke
+ _____CFPasteboardCreateSecurityScopeDataForPaths_block_invoke
+ _____CFPasteboardDetectionsDetectMetadataForImageSource_block_invoke
+ _____CFPasteboardHandleShowApprovalDialogMessage_block_invoke
+ _____CFPasteboardPerformOnQueue_block_invoke
+ _____CFPasteboardReleaseSandboxExtensionHandles_block_invoke
+ ____haveDataDetectors_block_invoke
+ ____haveImageIO_block_invoke
+ ____haveSafariShared_block_invoke
+ ____haveUTTypes_block_invoke
+ ____onqueue_CFPasteboardShowApprovalDialogIfNecessaryForPasteboard_block_invoke
+ ____onqueue_CFPasteboardShowApprovalDialogIfNecessaryForPasteboard_block_invoke_2
+ ____onqueue_CFPasteboardShowIndirectApprovalDialogIfNecessaryForPasteboard_block_invoke
+ ____onqueue_CFPasteboardShowIndirectApprovalDialogIfNecessaryForPasteboard_block_invoke_2
+ ___block_descriptor_104_e8_32o40o48o56o_e5_v8?0l
+ ___block_descriptor_104_e8_32o40o48o56r64r72r80r88r96r_e5_v8?0l
+ ___block_descriptor_112_e8_32r40r48r56r64r_e5_v8?0l
+ ___block_descriptor_136_e8_32o40o48o56b64b72b80r88r96r104r112r120r_e5_v8?0l
+ ___block_descriptor_32_e20_v16?0^{__CFArray=}8l
+ ___block_descriptor_40_e18_v32?0r^v8r^v16*24l
+ ___block_descriptor_40_e8_32b_e204_v52?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}CAQCCCC^{__CFData}^{__CFDictionary}????d{?=[8I]}}8q16q24^{__CFString=}32C40?<v?C>44l
+ ___block_descriptor_40_e8_32b_e61_v36?0^{__CFSet=}8^{__CFDictionary=}16^{__CFDictionary=}24i32l
+ ___block_descriptor_40_e8_32o_e13_v24?0r^v8*16l
+ ___block_descriptor_40_e8_32o_e18_v32?0r^v8r^v16*24l
+ ___block_descriptor_48_e191_C40?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}CAQCCCC^{__CFData}^{__CFDictionary}????d{?=[8I]}}8q16q24^{__CFString=}32l
+ ___block_descriptor_48_e20_v16?0^{__CFArray=}8l
+ ___block_descriptor_48_e8_32o40o_e18_v20?0C8?<v?C>12l
+ ___block_descriptor_48_e8_32o40o_e8_v12?0C8l
+ ___block_descriptor_48_e8_32o_e19_v16?0^{__CFData=}8l
+ ___block_descriptor_49_e8_32o40b_e8_v12?0C8l
+ ___block_descriptor_52_e8_32o40w_e18_v20?0C8?<v?C>12l
+ ___block_descriptor_56_e8_32o40b48r_e8_v12?0C8l
+ ___block_descriptor_56_e8_32o40b_e31_v20?0"_CFPasteboardEntry"8i16l
+ ___block_descriptor_56_e8_32o40o48b_e18_v16?0^{__CFSet=}8l
+ ___block_descriptor_56_e8_32o40o48b_e25_v16?0^{__CFDictionary=}8l
+ ___block_descriptor_56_e8_32o40o48b_e8_v12?0i8l
+ ___block_descriptor_56_e8_32o40o48r_e8_v12?0C8l
+ ___block_descriptor_56_e8_32r_e35_v24?0^{__CFString=}8^{__CFData=}16l
+ ___block_descriptor_65_e8_32o40b48r56r_e5_v8?0l
+ ___block_descriptor_65_e8_32o40o48b56r_e5_v8?0l
+ ___block_descriptor_68_e8_32o40b_e18_v20?0C8?<v?C>12l
+ ___block_descriptor_72_e8_32b_e5_v8?0l
+ ___block_descriptor_72_e8_32o40b48b56r_e8_v12?0B8l
+ ___block_descriptor_72_e8_32o40b_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_72_e8_32o40r48r_e8_v12?0C8l
+ ___block_descriptor_72_e8_32r_e18_v32?0r^v8r^v16*24l
+ ___block_descriptor_73_e8_32o40o48b56r64r_e8_v12?0C8l
+ ___block_descriptor_80_e8_32o40o48b56b64r_e5_v8?0l
+ ___block_descriptor_80_e8_32o40o48b_e8_v12?0C8l
+ ___block_descriptor_80_e8_32o40r_e5_v8?0l
+ ___block_descriptor_88_e8_32o40o48o56b_e8_v12?0C8l
+ ___block_descriptor_88_e8_32o40r48r_e5_v8?0l
+ ___block_descriptor_88_e8_32o40r48r_e8_v16?0Q8l
+ ___block_descriptor_89_e8_32b40r_e5_v8?0l
+ ___block_descriptor_96_e8_32o40o48o56o64o72r_e8_v12?0C8l
+ ___block_descriptor_96_e8_32o40r48r56r64r_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_96_e8_32r40r48r56r64r_e5_v8?0l
+ ___copy_helper_block_e8_32o40b48b56r
+ ___copy_helper_block_e8_32o40o48b56b64r
+ ___copy_helper_block_e8_32o40o48o56b64b72b80r88r96r104r112r120r
+ ___copy_helper_block_e8_32o40o48o56o64o72r
+ ___copy_helper_block_e8_32o40o48o56r64r72r80r88r96r
+ ___destroy_helper_block_e8_32o40b48b56r
+ ___destroy_helper_block_e8_32o40o48b56b64r
+ ___destroy_helper_block_e8_32o40o48o56b64b72b80r88r96r104r112r120r
+ ___destroy_helper_block_e8_32o40o48o56o64o72r
+ ___destroy_helper_block_e8_32o40o48o56r64r72r80r88r96r
+ ___forwarding___.cold.7
+ ___getRemotePasteboardClass_block_invoke.cold.2
+ ___handle_barrier_block_invoke_2
+ ___onqueue_CFPasteboardFlushLocalEntriesIfNecessary_block_invoke.545
+ ___onqueue_CFPasteboardMarkLocalChange_block_invoke.549
+ ___onqueue_CFPasteboardRequestDataFromDaemon_block_invoke.676
+ ___onqueue_CFPasteboardRequestDataFromDaemon_block_invoke.676.cold.1
+ ___onqueue_CFPasteboardRequestDataFromDaemon_block_invoke.676.cold.2
+ ___onqueue_CFPasteboardShowApprovalDialogIfNecessaryForPasteboard_block_invoke_2.cold.1
+ ___onqueue_CFPasteboardShowIndirectApprovalDialogIfNecessaryForPasteboard_block_invoke_2.cold.1
+ __block_literal_global.112
+ __block_literal_global.113
+ __block_literal_global.134
+ __block_literal_global.190
+ __block_literal_global.223
+ __block_literal_global.227
+ __block_literal_global.229
+ __block_literal_global.234
+ __block_literal_global.237
+ __block_literal_global.247
+ __block_literal_global.259
+ __block_literal_global.269
+ __block_literal_global.276
+ __block_literal_global.287
+ __block_literal_global.290
+ __block_literal_global.488
+ __block_literal_global.502
+ __block_literal_global.515
+ __block_literal_global.517
+ __block_literal_global.528
+ __block_literal_global.531
+ __block_literal_global.544
+ __block_literal_global.573
+ __block_literal_global.580
+ __block_literal_global.581
+ __block_literal_global.584
+ __block_literal_global.602
+ __block_literal_global.604
+ __block_literal_global.606
+ __block_literal_global.609
+ __block_literal_global.620
+ __block_literal_global.622
+ __block_literal_global.624
+ __block_literal_global.639
+ __block_literal_global.643
+ __block_literal_global.661
+ __block_literal_global.662
+ __block_literal_global.665
+ __cficu_ucal_add.cold.1
+ __cficu_ucal_add.cold.2
+ __cficu_ucal_add.cold.3
+ __cficu_ucal_clear.cold.2
+ __cficu_ucal_clear.cold.3
+ __cficu_ucal_clear.cold.4
+ __cficu_ucal_clone.cold.1
+ __cficu_ucal_clone.cold.2
+ __cficu_ucal_clone.cold.3
+ __cficu_ucal_close.cold.2
+ __cficu_ucal_close.cold.3
+ __cficu_ucal_close.cold.4
+ __cficu_ucal_close.cold.5
+ __cficu_ucal_get.cold.1
+ __cficu_ucal_get.cold.2
+ __cficu_ucal_get.cold.3
+ __cficu_ucal_getAttribute.cold.1
+ __cficu_ucal_getAttribute.cold.2
+ __cficu_ucal_getAttribute.cold.3
+ __cficu_ucal_getDayOfWeekType.cold.1
+ __cficu_ucal_getDayOfWeekType.cold.2
+ __cficu_ucal_getDayOfWeekType.cold.3
+ __cficu_ucal_getFieldDifference.cold.1
+ __cficu_ucal_getFieldDifference.cold.2
+ __cficu_ucal_getFieldDifference.cold.3
+ __cficu_ucal_getGregorianChange.cold.1
+ __cficu_ucal_getGregorianChange.cold.2
+ __cficu_ucal_getGregorianChange.cold.3
+ __cficu_ucal_getLimit.cold.1
+ __cficu_ucal_getLimit.cold.2
+ __cficu_ucal_getLimit.cold.3
+ __cficu_ucal_getMillis.cold.1
+ __cficu_ucal_getMillis.cold.2
+ __cficu_ucal_getMillis.cold.3
+ __cficu_ucal_getNow.cold.2
+ __cficu_ucal_getWeekendTransition.cold.1
+ __cficu_ucal_getWeekendTransition.cold.2
+ __cficu_ucal_getWeekendTransition.cold.3
+ __cficu_ucal_isWeekend.cold.1
+ __cficu_ucal_isWeekend.cold.2
+ __cficu_ucal_isWeekend.cold.3
+ __cficu_ucal_open.cold.1
+ __cficu_ucal_open.cold.2
+ __cficu_ucal_open.cold.3
+ __cficu_ucal_roll.cold.1
+ __cficu_ucal_roll.cold.2
+ __cficu_ucal_roll.cold.3
+ __cficu_ucal_set.cold.1
+ __cficu_ucal_set.cold.2
+ __cficu_ucal_set.cold.3
+ __cficu_ucal_setAttribute.cold.1
+ __cficu_ucal_setAttribute.cold.2
+ __cficu_ucal_setAttribute.cold.3
+ __cficu_ucal_setGregorianChange.cold.1
+ __cficu_ucal_setGregorianChange.cold.2
+ __cficu_ucal_setGregorianChange.cold.3
+ __cficu_ucal_setMillis.cold.1
+ __cficu_ucal_setMillis.cold.2
+ __cficu_ucal_setMillis.cold.3
+ __cficu_ucal_setTimeZone.cold.1
+ __cficu_ucal_setTimeZone.cold.2
+ __cficu_ucal_setTimeZone.cold.3
+ __cficu_ucurr_getDefaultFractionDigits.cold.1
+ __cficu_ucurr_getRoundingIncrement.cold.1
+ __cficu_udat_applyPattern.cold.1
+ __cficu_udat_applyPatternRelative.cold.1
+ __cficu_udat_clone.cold.1
+ __cficu_udat_close.cold.1
+ __cficu_udat_countSymbols.cold.1
+ __cficu_udat_format.cold.1
+ __cficu_udat_formatForFields.cold.1
+ __cficu_udat_get2DigitYearStart.cold.1
+ __cficu_udat_getCalendar.cold.1
+ __cficu_udat_getContext.cold.1
+ __cficu_udat_getSymbols.cold.1
+ __cficu_udat_isLenient.cold.1
+ __cficu_udat_open.cold.1
+ __cficu_udat_parseCalendar.cold.1
+ __cficu_udat_set2DigitYearStart.cold.1
+ __cficu_udat_setCalendar.cold.1
+ __cficu_udat_setContext.cold.1
+ __cficu_udat_setLenient.cold.1
+ __cficu_udat_setSymbols.cold.1
+ __cficu_udat_toPattern.cold.1
+ __cficu_udat_toPatternRelativeDate.cold.1
+ __cficu_udat_toPatternRelativeTime.cold.1
+ __cficu_udatpg_close.cold.1
+ __cficu_udatpg_getBestPattern.cold.1
+ __cficu_udatpg_getSkeleton.cold.1
+ __cficu_udatpg_open.cold.1
+ __cficu_ulistfmt_close.cold.1
+ __cficu_ulistfmt_format.cold.1
+ __cficu_ulistfmt_open.cold.1
+ __cficu_unum_applyPattern.cold.1
+ __cficu_unum_close.cold.1
+ __cficu_unum_formatDecimal.cold.1
+ __cficu_unum_formatDouble.cold.1
+ __cficu_unum_getAttribute.cold.1
+ __cficu_unum_getContext.cold.1
+ __cficu_unum_getDoubleAttribute.cold.1
+ __cficu_unum_getSymbol.cold.1
+ __cficu_unum_getTextAttribute.cold.1
+ __cficu_unum_open.cold.1
+ __cficu_unum_parse.cold.1
+ __cficu_unum_parseDecimal.cold.1
+ __cficu_unum_setAttribute.cold.1
+ __cficu_unum_setContext.cold.1
+ __cficu_unum_setDoubleAttribute.cold.1
+ __cficu_unum_setSymbol.cold.1
+ __cficu_unum_setTextAttribute.cold.1
+ __cficu_unum_toPattern.cold.1
+ __cficu_ureldatefmt_close.cold.1
+ __cficu_ureldatefmt_format.cold.1
+ __cficu_ureldatefmt_formatNumeric.cold.1
+ __cficu_ureldatefmt_open.cold.1
+ __handle_barrier_block_invoke_2.cold.1
+ __initDayChangedNotification.cold.1
+ __onqueue_CFPasteboardShowApprovalDialogIfNecessaryForPasteboard
+ _addBackstopValuesForIdentifierAndSource.cold.1
+ _addBackstopValuesForIdentifierAndSource.cold.2
+ _canDup.cold.1
+ _cfmp_record_deallocation.cold.1
+ _cfmp_record_intent_to_invalidate.cold.2
+ _cfmp_record_nsmachport_deallocation.cold.1
+ _cfmp_record_nsmachport_is_interested.cold.1
+ _cfmp_source_invalidated.cold.1
+ _cfmp_source_record_deadness.cold.1
+ _classDDScannerService
+ _classDDScannerServiceConfiguration
+ _classUTType
+ _constantDDBinderEmailKey
+ _constantDDBinderFlightInformationKey
+ _constantDDBinderTrackingNumberKey
+ _constantDDScannerSmallTimeout
+ _constantkCGImagePropertyDPIHeight
+ _constantkCGImagePropertyDPIWidth
+ _constantkCGImagePropertyDepth
+ _constantkCGImagePropertyHasAlpha
+ _constantkCGImagePropertyOrientation
+ _constantkCGImagePropertyPixelHeight
+ _constantkCGImagePropertyPixelWidth
+ _getDDBinderEmailKey
+ _getDDBinderFlightInformationKey
+ _getDDBinderTrackingNumberKey
+ _getDDScannerServiceClass
+ _getDDScannerServiceConfigurationClass
+ _getDDScannerSmallTimeout
+ _getUTTypeClass
+ _getkCGImagePropertyDPIHeight
+ _getkCGImagePropertyDPIWidth
+ _getkCGImagePropertyDepth
+ _getkCGImagePropertyHasAlpha
+ _getkCGImagePropertyOrientation
+ _getkCGImagePropertyPixelHeight
+ _getkCGImagePropertyPixelWidth
+ _handleExternalNotification.cold.1
+ _handle_allow_extension_for_process
+ _handle_begin_generation
+ _handle_detect_metadata
+ _handle_detect_patterns
+ _handle_detect_values
+ _handle_make_generation_local
+ _handle_notify_has_entries
+ _handle_refresh_cache
+ _handle_register_entries
+ _handle_release
+ _handle_request_data
+ _handle_resolve_all_pboard_promises
+ _handle_resolve_pboard_promises
+ _handle_restrict_extension
+ _handle_set_data_flags
+ _handle_set_expiration_date
+ _handle_unique_promise_file
+ _handle_verification_token_create
+ _haveDataDetectors.onceToken
+ _haveDataDetectors.sHaveDataDetectors
+ _haveImageIO.onceToken
+ _haveImageIO.sHaveImageIO
+ _haveSafariShared.onceToken
+ _haveSafariShared.sHaveSafariShared
+ _haveUTTypes.onceToken
+ _haveUTTypes.sHaveUTTypes
+ _initCGImageSourceCopyPropertiesAtIndex
+ _initCGImageSourceCreateWithData
+ _initCGImageSourceCreateWithURL
+ _initCGImageSourceGetCount
+ _initDDBinderEmailKey
+ _initDDBinderFlightInformationKey
+ _initDDBinderTrackingNumberKey
+ _initDDResultGetCategory
+ _initDDResultHasType
+ _initDDScannerService
+ _initDDScannerServiceConfiguration
+ _initDDScannerSmallTimeout
+ _initUTType
+ _initWBSUnifiedFieldInputTypeForString
+ _initkCGImagePropertyDPIHeight
+ _initkCGImagePropertyDPIWidth
+ _initkCGImagePropertyDepth
+ _initkCGImagePropertyHasAlpha
+ _initkCGImagePropertyOrientation
+ _initkCGImagePropertyPixelHeight
+ _initkCGImagePropertyPixelWidth
+ _kCGImagePropertyDPIHeightFunction
+ _kCGImagePropertyDPIWidthFunction
+ _kCGImagePropertyDepthFunction
+ _kCGImagePropertyHasAlphaFunction
+ _kCGImagePropertyOrientationFunction
+ _kCGImagePropertyPixelHeightFunction
+ _kCGImagePropertyPixelWidthFunction
+ _objc_copyStruct
+ _objc_getAssociatedObject
+ _objc_msgSend$URLWithDataRepresentation:relativeToURL:
+ _objc_msgSend$_ensureCSUIAIsRunning
+ _objc_msgSend$_handleDetectionOfType:withMessage:
+ _objc_msgSend$_onDialogQueue_sendShowInAppApprovalDialogIPC
+ _objc_msgSend$_onDialogQueue_sendShowIndirectApprovalDialogIPCForCLIProcess:
+ _objc_msgSend$_onqueue_handleNewRegularEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:
+ _objc_msgSend$_onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:
+ _objc_msgSend$_onqueue_isManagedPromiseDragWithCache:forGeneration:itemIdentifier:
+ _objc_msgSend$_onqueue_isPasteLocationRelatedEntryAllowedForMessage:
+ _objc_msgSend$_onqueue_postflightNewEntries:forMessage:withPreflightData:
+ _objc_msgSend$_onqueue_preflightNewEntries:forMessage:
+ _objc_msgSend$_onqueue_validateToken:forRequestingApp:
+ _objc_msgSend$_setRemotePromiseState:
+ _objc_msgSend$_showCurrentApprovalDialogAndWaitForReply
+ _objc_msgSend$auditToken
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$checkResourceIsReachableAndReturnError:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$coreResult
+ _objc_msgSend$dictionary
+ _objc_msgSend$didLeakExtension
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$firstObject
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$getUserApproval:inApp:withCompletion:
+ _objc_msgSend$groupingSeparator
+ _objc_msgSend$handleDetectMetadata:
+ _objc_msgSend$handleDetectPatterns:
+ _objc_msgSend$handleDetectValues:
+ _objc_msgSend$initWithScannerType:passiveIntent:
+ _objc_msgSend$isCSUIA
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$lastPboardError
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$onqueue_analyzeSandboxExtensionEntry:destinedForClient:
+ _objc_msgSend$onqueue_filterDataFromEntry:inResponseToMessage:error:
+ _objc_msgSend$onqueue_reissueSandboxExtensionFromEntry:toClient:error:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:
+ _objc_msgSend$scanDouble:
+ _objc_msgSend$scanString:range:configuration:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$setDidLeakExtension:
+ _objc_msgSend$setLastPboardError:
+ _objc_msgSend$setRemoteScannerEnabled:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$stringByStandardizingPath
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$typeWithFilenameExtension:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_removeAssociatedObjects
+ _onqueue_CFPasteboardSetData.cold.1
+ _onqueue_CFPasteboardSetData.cold.2
+ _onqueue_CFPasteboardSetData.cold.3
+ _onqueue_CFPasteboardSetData.cold.4
+ _onqueue_CFPasteboardSetData.cold.5
+ _onqueue_CFPasteboardSetData.cold.6
+ _onqueue_CFPasteboardShowApprovalDialogIfNecessaryForPasteboard.cold.1
+ _onqueue_validateToken:forRequestingApp:.onceToken
+ _onqueue_validateToken:forRequestingApp:.sTimeScale
+ _parseComponents.cold.1
+ _parseComponents.cold.2
+ _proc_pidpath_audittoken
+ _registerFactoryLocked.cold.1
+ _registerTypeLocked.cold.2
+ _registerTypeLocked.cold.3
+ _sClientInstanceForCurrentApprovalDialog
+ _sCurrentApprovalDialogIsIndirect
+ _sEntitlementCache
+ _sEntitlementCacheLock
+ _softLinkCGImageSourceCopyPropertiesAtIndex
+ _softLinkCGImageSourceCreateWithData
+ _softLinkCGImageSourceCreateWithURL
+ _softLinkCGImageSourceGetCount
+ _softLinkDDResultGetCategory
+ _softLinkDDResultHasType
+ _softLinkWBSUnifiedFieldInputTypeForString
+ _unescapedQueryString.cold.2
+ _unnamed_array_storage.659
+ _unnamed_array_storage.679
+ _unnamed_array_storage.680
+ cfprefsdEuid.cold.1
+ decomposeToRFC1808.cold.1
+ getAtomTarget.cold.1
+ isDate:equalToDate:toUnitGranularity:.__count__.24
+ isDate:inSameDayAsDate:.__count__.28
+ log_paste_telemetry.cold.2
+ log_paste_telemetry.cold.3
+ log_paste_telemetry.cold.4
+ makeAtom.cold.1
+ notifyFunc.cold.1
+ parseFrameArgumentInfo.cold.1
+ parseFrameArgumentInfo.cold.10
+ parseFrameArgumentInfo.cold.11
+ parseFrameArgumentInfo.cold.12
+ parseFrameArgumentInfo.cold.13
+ parseFrameArgumentInfo.cold.14
+ parseFrameArgumentInfo.cold.15
+ parseFrameArgumentInfo.cold.16
+ parseFrameArgumentInfo.cold.17
+ parseFrameArgumentInfo.cold.2
+ parseFrameArgumentInfo.cold.3
+ parseFrameArgumentInfo.cold.4
+ parseFrameArgumentInfo.cold.5
+ parseFrameArgumentInfo.cold.6
+ parseFrameArgumentInfo.cold.7
+ parseFrameArgumentInfo.cold.8
+ parseFrameArgumentInfo.cold.9
+ setAndAdvance.cold.1
+ softLink_LSCopyFrontApplication_block_invoke.onceToken
- -[CFPDMirroredSource acceptMessage:].cold.1
- -[CFPDSource cleanUpIfNecessaryAfterCreatingPlist].cold.1
- -[CFPDSource cleanUpIfNecessaryAfterCreatingPlist].cold.2
- -[CFPDSource shouldStayDirtyAfterOpenForWritingFailureWithErrno:].cold.1
- -[CFPrefsDaemon _initializeShmemPage:].cold.1
- -[CFPrefsDaemon handleAgentCheckInMessage:].cold.1
- -[CFPrefsDaemon handleAgentCheckInMessage:].cold.2
- -[CFPrefsPlistSource handlePossibleOversizedMessage:forWritingKeys:values:count:].cold.1
- -[CFPrefsPlistSource handlePossibleOversizedMessage:forWritingKeys:values:count:].cold.2
- -[CFPrefsPlistSource setUserIdentifier:].cold.1
- -[_CFDragPasteboardStore _isManagedPromiseDragForGeneration:itemIdentifier:]
- -[_CFDragPasteboardStore _onqueue_handleNewEntries:forMessage:shouldInvalidateClientMetadata:]
- -[_CFDragPasteboardStore requestDataForGeneration:itemIdentifier:flavor:inResponseToMessage:completionHandler:]
- -[_CFGeneralPasteboardStore _onqueue_handleNewEntries:forMessage:shouldInvalidateClientMetadata:]
- -[_CFGeneralPasteboardStore getUserApproval:withCompletion:]
- -[_CFGeneralPasteboardStore getUserApproval:withCompletion:].cold.1
- -[_CFPasteboardEntry extensionConsumed]
- -[_CFPasteboardEntry resolveClientPromisedDataWithQueue:completionHandler:]
- -[_CFPasteboardEntry resolveLocalPromisedData]
- -[_CFPasteboardEntry setExtensionConsumed:]
- -[_CFPasteboardStore _onqueue_handleNewEntries:forMessage:shouldInvalidateClientMetadata:]
- -[_CFPasteboardStore analyzeSandboxExtensionEntry:destinedForClient:]
- -[_CFPasteboardStore filterDataFromEntry:inResponseToMessage:error:]
- -[_CFPasteboardStore reissueSandboxExtensionFromEntry:toClient:error:]
- -[_CFXPreferences _copyDaemonConnectionSettingUpIfNecessaryForRole:andUserIdentifier:].cold.1
- CFPasteboardSetPrevalidationCallbacks.cold.1
- CF_RUNLOOP_ASSERTIONS.onceToken
- GCC_except_table143
- GCC_except_table162
- GCC_except_table182
- GCC_except_table247
- GCC_except_table93
- GCC_except_table95
- OBJC_IVAR_$__CFDragPasteboardStore._sourceProcessID
- OBJC_IVAR_$__CFPasteboardEntry._asyncPromisor
- OBJC_IVAR_$__CFPasteboardEntry._extensionConsumed
- OBJC_IVAR_$__CFPasteboardEntry._promiseState
- OBJC_IVAR_$__CFPasteboardEntry._promisor
- _CFPasteboardGetPasteVerificationToken
- _CFPasteboardIssueSandboxExtensionForPath.cold.1
- _CFPasteboardSetPrevalidationCallbacks
- _CFPrefsCopyDefaultPreferences.defaultPrefs
- _CFPrefsCopyDefaultPreferences.onceToken
- _CFVolumeObserverGetTypeID.onceToken
- _InitializeDiskArbitrationKeys.onceToken
- _InitializeDiskArbitrationKeys.result
- __107-[_CFPasteboardStore requestDataForGeneration:itemIdentifier:flavor:inResponseToMessage:completionHandler:]_block_invoke.51
- __40-[_CFPasteboardStore handleRequestData:]_block_invoke.57
- __41-[_CFPasteboardStore handleSetDataFlags:]_block_invoke.47
- __44-[_CFPasteboardStore handleResolvePromises:]_block_invoke.58
- __46-[_CFPasteboardStore handleSetExpirationDate:]_block_invoke.33
- __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.355
- __50-[_CFDragPasteboardStore handleUniquePromiseFile:]_block_invoke.355.cold.1
- __59-[_CFGeneralPasteboardStore handleVerificationTokenCreate:]_block_invoke.197
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke.283
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke.283.cold.1
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke.283.cold.2
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke.283.cold.3
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_2.287
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_2.cold.1
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_3.cold.1
- __60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_3.cold.2
- __64-[_CFRemotePasteboardCache prepareDataForItemIdentifier:flavor:]_block_invoke.383
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.209
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.210
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.214
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.cold.1
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.cold.2
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.cold.3
- __65-[_CFGeneralPasteboardStore validatePasteRequest:withCompletion:]_block_invoke.cold.4
- __67-[_CFGeneralPasteboardStore notifyRemoteGenerationBecameAvailable:]_block_invoke.225
- __75-[_CFPasteboardEntry resolveClientPromisedDataWithQueue:completionHandler:]_block_invoke.192
- __79-[_CFPasteboardEntry(CFRemotePasteboardSupport) promiseDataWithFetchOperation:]_block_invoke.400
- __88-[_CFPasteboardStore flushOwnerChangesIfNecessaryInResponseToMessage:completionHandler:]_block_invoke.76
- __88-[_CFPasteboardStore flushOwnerChangesIfNecessaryInResponseToMessage:completionHandler:]_block_invoke.77
- __Block_byref_object_copy_.461
- __Block_byref_object_dispose_.462
- __CFDiskArbitration_DARegisterDiskAppearedCallback.dyfunc
- __CFDiskArbitration_DARegisterDiskAppearedCallback.onceToken
- __CFDiskArbitration_DARegisterDiskDescriptionChangedCallback.dyfunc
- __CFDiskArbitration_DARegisterDiskDescriptionChangedCallback.onceToken
- __CFDiskArbitration_DARegisterDiskDisappearedCallback.dyfunc
- __CFDiskArbitration_DARegisterDiskDisappearedCallback.onceToken
- __CFDiskArbitration_DARegisterDiskUnmountApprovalCallback.dyfunc
- __CFDiskArbitration_DARegisterDiskUnmountApprovalCallback.onceToken
- __CFDiskArbitration_DARegisterIdleCallback.dyfunc
- __CFDiskArbitration_DARegisterIdleCallback.onceToken
- __CFDiskArbitration_DASessionCreate.dyfunc
- __CFDiskArbitration_DASessionCreate.onceToken
- __CFErrorCreateCallStackReturnAddresses
- __CFHandleFinishedEnumerating.oIsOldPages
- __CFHandleFinishedEnumerating.oIsOldSoundtrackLoopUtility
- __CFHandleFinishedEnumerating.oIsOldiWeb
- __CFHandleFinishedEnumerating.onceToken
- __CFPasteboardGeneratePasteVerificationToken_block_invoke.132
- __CFPasteboardGeneratePasteVerificationToken_block_invoke.132.cold.1
- __CFPasteboardGeneratePasteVerificationToken_block_invoke.134
- __CFPasteboardGeneratePasteVerificationToken_block_invoke.137
- __CFPasteboardPromiseDataUsingBlock_block_invoke.101
- __CFPasteboardPromiseDataUsingBlock_block_invoke.99
- __CFPasteboardResolvePromisedData_block_invoke.105
- __CFPrefsDaemonLock
- ___111-[_CFDragPasteboardStore requestDataForGeneration:itemIdentifier:flavor:inResponseToMessage:completionHandler:]_block_invoke
- ___60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke
- ___60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_2
- ___60-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_3
- ___70-[_CFPasteboardStore reissueSandboxExtensionFromEntry:toClient:error:]_block_invoke
- ___75-[_CFPasteboardEntry resolveClientPromisedDataWithQueue:completionHandler:]_block_invoke
- ___75-[_CFPasteboardEntry resolveClientPromisedDataWithQueue:completionHandler:]_block_invoke_2
- ___CFMidnightNoteCount
- ___CFPASTEBOARDDAEMON_IS_SHOWING_AN_APPROVAL_DIALOG__
- ___CFPasteboardHandleFlushMessage_block_invoke.441
- ___CFPasteboardHandleFlushMessage_block_invoke.444
- ___CFPasteboardHandleFlushMessage_block_invoke.444.cold.1
- ___CFPasteboardHandleFlushMessage_block_invoke.445
- ___CFPasteboardHandleFlushMessage_block_invoke.445.cold.1
- ___CFPasteboardHandleFulfillMessage_block_invoke.463
- ___CFPasteboardHandleInvalidatedDaemonConnection_block_invoke.431
- ___CFRunLoopMain
- ____CFPasteboardCreateSecurityScopeDataForPaths_block_invoke
- ____CFPasteboardSetSandboxExtensionData_block_invoke
- ____cfNotificationCancelIfNecessary_block_invoke
- ____haveSecurityFunctions_block_invoke
- ____onqueue_CFPasteboardPrecheckTokenAndShowApprovalDialogIfNecessaryForPasteboard_block_invoke
- ____onqueue_CFPasteboardPrecheckTokenAndShowApprovalDialogIfNecessaryForPasteboard_block_invoke_2
- ____onqueue_CFPasteboardPromiseSandboxExtensionDataIfNecessary_block_invoke
- ___block_descriptor_41_e8_32b_e5_v8?0l
- ___block_descriptor_48_e147_C40?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}^{__CFUUID}^{__CFArray}CAQCCCC^{__CFData}^{__CFDictionary}??d}8q16q24^{__CFString=}32l
- ___block_descriptor_48_e35_v24?0^{__CFString=}8^{__CFData=}16l
- ___block_descriptor_48_e8_32o40o_e15_v16?0?<v?C>8l
- ___block_descriptor_48_e8_32o40r_e8_v12?0C8l
- ___block_descriptor_52_e8_32o40w_e15_v16?0?<v?C>8l
- ___block_descriptor_56_e8_32o_e8_v16?0Q8l
- ___block_descriptor_57_e8_32o40b48b_e5_v8?0l
- ___block_descriptor_57_e8_32o_e147_C40?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}^{__CFUUID}^{__CFArray}CAQCCCC^{__CFData}^{__CFDictionary}??d}8q16q24^{__CFString=}32l
- ___block_descriptor_64_e8_32o40o48b56b_e8_v12?0C8l
- ___block_descriptor_64_e8_32o40r_e5_v8?0l
- ___block_descriptor_68_e8_32o40b_e5_C8?0l
- ___block_descriptor_72_e8_32o40o48o56o_e5_v8?0l
- ___block_descriptor_73_e8_32r_e5_v8?0l
- ___block_descriptor_80_e8_32o40o48b_e5_v8?0l
- ___block_descriptor_80_e8_32o40o48o56b_e8_v12?0C8l
- ___block_descriptor_88_e8_32o40o48o56o64b_e8_v12?0C8l
- ___block_descriptor_88_e8_32o40r48r56r64r_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_89_e8_32r40r48r_e5_v8?0l
- ___copy_helper_block_e8_32o40b48b
- ___copy_helper_block_e8_32o40o48b56b
- ___copy_helper_block_e8_32o40o48o56o64b
- ___destroy_helper_block_e8_32o40b48b
- ___destroy_helper_block_e8_32o40o48b56b
- ___destroy_helper_block_e8_32o40o48o56o64b
- ___noteCount
- ___onqueue_CFPasteboardFlushLocalEntriesIfNecessary_block_invoke.405
- ___onqueue_CFPasteboardMarkLocalChange_block_invoke.409
- ___onqueue_CFPasteboardPrecheckTokenAndShowApprovalDialogIfNecessaryForPasteboard_block_invoke_2.cold.1
- ___onqueue_CFPasteboardPromiseSandboxExtensionDataIfNecessary_block_invoke.412
- ___onqueue_CFPasteboardRequestDataFromDaemon_block_invoke.480
- ___onqueue_CFPasteboardRequestDataFromDaemon_block_invoke.480.cold.1
- ___onqueue_CFPasteboardRequestDataFromDaemon_block_invoke.480.cold.2
- __agentShmem
- __block_literal_global.114
- __block_literal_global.117
- __block_literal_global.119
- __block_literal_global.184
- __block_literal_global.225
- __block_literal_global.228
- __block_literal_global.241
- __block_literal_global.263
- __block_literal_global.266
- __block_literal_global.275
- __block_literal_global.289
- __block_literal_global.375
- __block_literal_global.388
- __block_literal_global.390
- __block_literal_global.404
- __block_literal_global.416
- __block_literal_global.429
- __block_literal_global.436
- __block_literal_global.438
- __block_literal_global.514
- __block_literal_global.521
- __block_literal_global.526
- __block_literal_global.530
- __block_literal_global.547
- __block_literal_global.552
- __block_literal_global.563
- __block_literal_global.565
- __cfNotificationCallback
- __daemonShmem
- __handle_barrier_block_invoke.512
- __handle_barrier_block_invoke.512.cold.1
- __onqueue_CFPasteboardCreateSandboxExtensionData
- __onqueue_CFPasteboardPromiseSandboxExtensionDataIfNecessary
- __shmemLock
- _block_invoke.sTimeScale
- _block_invoke_2.onceToken
- _cfNotificationCallback.cold.1
- _haveSecurityFunctions.onceToken
- _haveSecurityFunctions.sHaveSecurityFunctions
- _objc_msgSend$_URLByInsertingResolveFlags:
- _objc_msgSend$_isManagedPromiseDragForGeneration:itemIdentifier:
- _objc_msgSend$_onqueue_handleNewEntries:forMessage:shouldInvalidateClientMetadata:
- _objc_msgSend$_resolveFlags
- _objc_msgSend$analyzeSandboxExtensionEntry:destinedForClient:
- _objc_msgSend$extensionConsumed
- _objc_msgSend$filterDataFromEntry:inResponseToMessage:error:
- _objc_msgSend$getUserApproval:withCompletion:
- _objc_msgSend$reissueSandboxExtensionFromEntry:toClient:error:
- _objc_msgSend$resolveClientPromisedDataWithQueue:completionHandler:
- _objc_msgSend$resolveLocalPromisedData
- _objc_msgSend$setExtensionConsumed:
- _onqueue_CFPasteboardCreateSandboxExtensionData.cold.1
- _onqueue_CFPasteboardCreateSandboxExtensionData.cold.2
- _onqueue_CFPasteboardPromiseSandboxExtensionDataIfNecessary.cold.1
- _sAppConnectionForCurrentNotification
- _sApprovalDialogSemaphore
- _sCFNotificationCompletionBlock
- _sCurrentNotification
- directCFPrefsD.daemon
- directCFPrefsD.onceToken
- initWithRole:testMode:.onceToken
- initWithRole:testMode:.runningInSystemContext
- isDate:equalToDate:toUnitGranularity:.__count__.23
- isDate:inSameDayAsDate:.__count__.27
- registerForChangeNotifications.cloudSources
- registerForChangeNotifications.cloudSourcesLock
- shmemForRole:name:.cannotAccessAgentShmem
- shmemForRole:name:.cannotAccessDaemonShmem
- shmemForRole:name:.onceToken
- softLink_LSCopyFrontApplication_block_invoke_3.onceToken
CStrings:
+ "#24@0:8@16"
+ "%ld bytes"
+ "%u;%u;%u;%u;%u;%u;%u;%u;"
+ "%u;%u;%u;%u;%u;%u;%u;%u;%@;%@"
+ "%{public}@ has new generation %d"
+ "%{public}@ has new generation %d with owner %{public}@"
+ "-[_CFPasteboardEntry initFromXPCObject:fromConnection:]_block_invoke"
+ "-[_CFPasteboardEntry resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:]"
+ "-[_CFPasteboardEntry(CFRemotePasteboardSupport) promiseDataWithFetchOperation:]_block_invoke"
+ "/.nofollow"
+ "/.nofollow/"
+ "/System/Library/CoreServices/CoreServicesUIAgent.app/Contents/MacOS/CoreServicesUIAgent"
+ "/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers"
+ "/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared"
+ "/etc"
+ "/tmp"
+ "/var"
+ "<nil>"
+ "<same as key>"
+ "<same as value>"
+ "@\"<CSAttendingServiceDelegate>\"16@0:8"
+ "@\"<FBSceneClientProcess>\"16@0:8"
+ "@\"ATXCustomIntentDescription\"32@?0@\"CLPlacemark\"8@\"NSString\"16@\"NSString\"24"
+ "@\"ATXCustomIntentDescription\"8@?0"
+ "@\"BKSProximityDetectionMaskChangeEvent\"24@0:8@\"NSNumber\"16"
+ "@\"BSSettings\"16@0:8"
+ "@\"CHSWidgetMetrics\"24@0:8@\"CHSWidget\"16"
+ "@\"CHSWidgetMetrics\"32@0:8@\"CHSWidget\"16@\"NSString\"24"
+ "@\"CHSWidgetMetricsSpecification\"24@0:8@\"NSString\"16"
+ "@\"CHSWidgetMetricsSpecification\"40@0:8@\"UISDeviceContext\"16@\"UISDisplayContext\"24@\"NSString\"32"
+ "@\"FBSSceneUpdate\"16@0:8"
+ "@\"JSAPackage\"8@?0"
+ "@\"NSArray\"16@?0@\"CNContact\"8"
+ "@\"NSArray<__BKSHIDKeyboardDeviceProperties__>\"24@0:8@\"NSNumber\"16"
+ "@\"NSArray<__NSString__>\"16@0:8"
+ "@\"NSArray<__UNCNotificationCategoryRecord__>\"24@0:8@\"NSString\"16"
+ "@\"NSArray<__UNSNotificationRecord__>\"24@0:8@\"NSString\"16"
+ "@\"NSData\"32@0:8@\"NSData\"16^@24"
+ "@\"NSDictionary\"16@?0@\"NSArray\"8"
+ "@\"NSDictionary\"24@0:8@\"NSNumber\"16"
+ "@\"NSDictionary\"24@?0d8d16"
+ "@\"NSDictionary\"40@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32"
+ "@\"NSDictionary<__NSString__><__CHSWidgetMetricsSpecification__>\"24@0:8@\"NSString\"16"
+ "@\"NSDictionary<__NSString__><__CHSWidgetMetricsSpecification__>\"40@0:8@\"UISDeviceContext\"16@\"UISDisplayContext\"24@\"NSString\"32"
+ "@\"NSError\"16@0:8"
+ "@\"NSNumber\"24@0:8@\"NSUUID\"16"
+ "@\"NSNumber\"24@0:8@\"XCTINanoRegistryDevice\"16"
+ "@\"NSNumber\"24@?0@\"JSValue\"8@\"JSValue\"16"
+ "@\"NSNumber\"32@0:8@\"NSUUID\"16@\"NSString\"24"
+ "@\"NSNumber\"32@0:8@\"NSUUID\"16@\"NSUUID\"24"
+ "@\"NSNumber\"32@0:8@\"NSUUID\"16@\"SEPosterUpdate\"24"
+ "@\"NSNumber\"32@0:8@\"PRSPosterConfiguration\"16@\"PRSPosterUpdate\"24"
+ "@\"NSNumber\"40@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32"
+ "@\"NSNumber\"48@0:8@\"NSNumber\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40"
+ "@\"NSNumber\"64@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48@\"NSNumber\"56"
+ "@\"NSProgress\"28@0:8B16@?<v@?@\"NSError\">20"
+ "@\"NSProgress\"32@0:8@\"<SKEraserProtocol>\"16@?<v@?@\"NSArray\">24"
+ "@\"NSProgress\"32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "@\"NSProgress\"32@0:8@\"NSUUID\"16@?<v@?>24"
+ "@\"NSProgress\"32@0:8@\"PRUISAnalysisServiceRequest\"16@?<v@?@\"PRUISAnalysisServiceResponse\"@\"NSError\">24"
+ "@\"NSProgress\"32@0:8Q16@?<v@?@\"NSError\">24"
+ "@\"NSProgress\"40@0:8@\"NSArray\"16Q24@?<v@?@\"NSError\">32"
+ "@\"NSProgress\"40@0:8@\"NSDictionary\"16Q24@?<v@?@\"NSError\">32"
+ "@\"NSProgress\"48@0:8@\"NSSet\"16@\"NSSecurityScopedURLWrapper\"24@\"PLInterLibraryTransferOptions\"32@?<v@?@\"NSError\">40"
+ "@\"NSProgress\"48@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">40"
+ "@\"NSProgress\"48@0:8@\"NSURL\"16B24@\"NSString\"28I36@?<v@?@\"NSError\">40"
+ "@\"NSProgress\"48@0:8Q16@\"NSArray\"24Q32@?<v@?B@\"NSError\">40"
+ "@\"NSProgress\"56@0:8@\"FPItemID\"16@\"NSFileProviderItemVersion\"24Q32@\"NSFileProviderRequest\"40@?<v@?@\"FPExtensionResponse\"@\"NSError\">48"
+ "@\"NSProgress\"68@0:8@\"FPItem\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSFileProviderRequest\"48B56@?<v@?@\"FPItem\"QB@\"FPExtensionResponse\"@\"NSError\">60"
+ "@\"NSProgress\"72@0:8@\"FPItem\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSFileProviderRequest\"56@?<v@?@\"FPItem\"QB@\"FPExtensionResponse\"@\"NSError\">64"
+ "@\"NSSet<__BKSHIDEventPolicyObservation__>\"24@0:8@\"NSNumber\"16"
+ "@\"NSString\"24@0:8@\"NSDictionary\"16"
+ "@\"NSString\"24@0:8@\"_BKSHIDEventDeferringRuleIdentity\"16"
+ "@\"NSURL\"24@0:8@\"NSUUID\"16"
+ "@\"NSUUID\"24@0:8@\"PRSPosterConfiguration\"16"
+ "@\"NSUUID\"40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
+ "@\"PPSMetricCollection\"16@0:8"
+ "@\"PRSActivePosterConfiguration\"24@0:8@\"NSString\"16"
+ "@\"PRSActivePosterConfiguration\"32@0:8@\"NSString\"16o^@24"
+ "@\"PRSPosterConfiguration\"24@0:8@\"NSString\"16"
+ "@\"PRSWidget\"56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40@\"INIntent\"48"
+ "@\"PRUISAnalysisServiceResponse\"32@0:8@\"PRUISAnalysisServiceRequest\"16o^@24"
+ "@\"SBSDebugActiveWidgetInfo\"16@0:8"
+ "@\"SBSHomeScreenIconStyleConfiguration\"16@0:8"
+ "@\"SBSHomeScreenServiceArrayOfNumbers\"16@0:8"
+ "@\"SBSHomeScreenServiceArrayOfStrings\"16@0:8"
+ "@\"SBSHomeScreenServiceArrayOfStrings\"24@0:8@\"NSString\"16"
+ "@\"SEPosterConfiguration\"24@0:8@\"NSString\"16"
+ "@\"SEPosterDescriptors\"24@0:8@\"NSString\"16"
+ "@\"THThreadNetworkCredentialsStoreLocalClient\"16@0:8"
+ "@\"UIColor\"16@0:8"
+ "@\"UITraitCollection\"16@0:8"
+ "@\"UNCNotificationCategoryRecord\"32@0:8@\"NSString\"16@\"NSString\"24"
+ "@\"UNSNotificationRecord\"32@0:8@\"NSString\"16@\"NSString\"24"
+ "@\"XCTINanoRegistryDevice\"16@0:8"
+ "@\"_BKSCATransform3DContainer\"40@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32"
+ "@\"_TtC18ReplicatorServices36MigrationXPCServerResponseGetRecords\"24@0:8^@16"
+ "@\"_TtC18ReplicatorServices38ReplicationXPCServerResponseGetRecords\"32@0:8@\"NSData\"16^@24"
+ "@\"_UISheetPresentationControllerClientConfiguration\"16@0:8"
+ "@\"_UISheetPresentationControllerConfiguration\"16@0:8"
+ "@24@0:8#16"
+ "@24@0:8@\"<QLPreviewItem>\"16"
+ "@24@0:8@\"NSData\"16"
+ "@24@0:8B16B20"
+ "@24@0:8^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}16"
+ "@28@0:8d16B24"
+ "@32@0:8@16^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}24"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16@24^@32"
+ "@40@0:8d16@24@32"
+ "@44@0:8@16@24@32B40"
+ "@?40@0:8^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}16q24^{?=iq^{__CFData}Q}32"
+ "@@:@:"
+ "Actually registered %ld entries for generation %llu of pasteboard '%{public}@'"
+ "An error occurred in CoreServicesUIAgent. Status: %lld"
+ "An error occurred while attempting to get a unique promise file URL. Error: Did not receive a valid URL."
+ "An error occurred while launching CSUIA. Unable to build message."
+ "An error occurred while launching CSUIA. Unable to create connection."
+ "An error occurred while launching CSUIA. Unable to find client after launch."
+ "An error occurred while showing approval dialog for '%{public}@ via client '%{public}@'. Error: %d"
+ "An error occurred while showing indirect approval dialog for '%{public}@ via CSUIA '%{public}@'. Error: %d"
+ "Attach Security Scope - canonical path: %{private}@"
+ "Attach Security Scope - data: %{public}@"
+ "Attach Security Scope - path: %{private}@"
+ "Attempted to use stale generation %ld (current generation: %ld) while trying to look up sandbox extension entry for item %ld flavor: %{public}@"
+ "B24@0:8^v16"
+ "B24@0:8^{?=iddff(?={?={?=fff}{?=fff}}{?=B[282c]})}16"
+ "B24@0:8^{?=i{?=dd}ddddddddidi{?=dd}diIiiidB}16"
+ "B24@0:8^{CLGnssControlPlaneStatusReport=ddddddiiI}16"
+ "B24@0:8^{ThinShellIonosphereParameters=BB{CNTimeSpan=qd}ddd{TAITime={CNTimeSpan=qd}}dddddddddddddd}16"
+ "B24@0:8r^v16"
+ "B28@0:8^v16B24"
+ "B32@0:8@\"NSData\"16^@24"
+ "B32@0:8@\"_TtC18ReplicatorServices40ReplicationXPCServerParametersAddRecords\"16^@24"
+ "B32@0:8B16B20^v24"
+ "B32@0:8Q16^@24"
+ "B32@0:8^v16@24"
+ "B32@0:8q16d24"
+ "B32@0:8r^i16^v24"
+ "B40@0:8@\"CNContact\"16@\"NSString\"24@\"NSString\"32"
+ "B40@0:8@\"_DASActivity\"16@\"_DASActivityGroup\"24^@32"
+ "B40@0:8@16Q24Q32"
+ "B40@0:8^v16@24@32"
+ "B40@0:8^v16^i24^d32"
+ "B44@0:8@16@24@32B40"
+ "B44@0:8@16B24@28^@36"
+ "B44@0:8^v16^i24^d32B40"
+ "B48@0:8^v16d24d32^v40"
+ "B48@0:8c16B20B24B28r*32r^v40"
+ "B48@0:8r^{?=i{?=dd}ddddddddidi{?=dd}diIiiidB}16f24^v28^v36B44"
+ "B56@0:8^{__CFData=}16{?=[8I]}24"
+ "Bad data for security scope entry corresponding to file reference entry."
+ "Bundle: %{private}@, key: %@, value: %@, table: %{public}@, localizationNames: %{public}@, result: %{public}@"
+ "C40@?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}8q16q24^{__CFString=}32"
+ "CFErrorCallStacks"
+ "CFPasteboard couldn't load a Security symbol."
+ "CFPasteboard received indirect approval dialog reply: %{public}@"
+ "CFPasteboard skipping rapidly repeated requests for indirect approval dialog."
+ "CFPasteboard: calling approval dialog requestor block"
+ "CFPasteboard: calling indirect approval dialog cancellation block"
+ "CFPasteboard: calling indirect approval dialog requestor block"
+ "CFPasteboard: dequeued %{public}@ presentation"
+ "CFPasteboard: did not find pasteboard UUID for %{public}@"
+ "CFPasteboard: did not find pasteboard UUID for indirect approval dialog cancellation"
+ "CFPasteboard: did not find pasteboard for %{public}@"
+ "CFPasteboard: did not find pasteboard for indirect approval dialog cancellation"
+ "CFPasteboard: enqueuing %{public}@ presentation"
+ "CFPasteboard: invalid audit token for %{public}@"
+ "CFPasteboard: invalid audit token for indirect approval dialog cancellation"
+ "CFPasteboard: no approval dialog callback"
+ "CFPasteboard: no audit token for %{public}@"
+ "CFPasteboard: no audit token for indirect approval dialog cancellation"
+ "CFPasteboard: no indirect approval cancellation callback"
+ "CFPasteboard: no indirect approval dialog callback"
+ "CFPasteboard: pasteboard for %{public}@ was not the general pasteboard"
+ "CFPasteboard: pasteboard for indirect approval dialog cancellation was not the general pasteboard"
+ "CFPasteboardDetect async"
+ "CFPasteboardPromiseDataUsingBlock_block_invoke"
+ "CFPasteboardSetPasteboardValidationCallbacks('%{public}@' (%{public}@), ...)"
+ "CFPasteboardSetPasteboardValidationCallbacks() can only be used with kCFPasteboardGeneral. Pasteboard was: '%{public}@' (%{public}@) "
+ "CFPasteboardSetPasteboardValidationCallbacks(NULL, ...)"
+ "CGImageSourceCopyPropertiesAtIndex"
+ "CGImageSourceCreateWithData"
+ "CGImageSourceCreateWithURL"
+ "CGImageSourceGetCount"
+ "CSUIAgent Launched successfully."
+ "CSUIAgent wasn't running. Launching it now."
+ "Caller didn't provide a proposed filename, required to create unique promise drag destination"
+ "Client died. Will cancel approval dialog."
+ "CoreServicesUIAgent could not be found (configuration error). Error: %{public}s"
+ "CoreServicesUIAgent encountered an unexpected error. Error: %{public}s"
+ "CoreServicesUIAgent exited unexpectedly. Retrying. Error: %{public}s"
+ "CoreServicesUIAgent exited unexpectedly. Retrying. Error: %{public}s\nInvalidation reason: %{public}s"
+ "CoreServicesUIAgent is exiting unexpectedly. Error: %{public}s"
+ "Could not obtain entitlement %{private}@ for process with pid %ld. Error: %{private}@"
+ "CreateSandboxExtensionData failed: fileNamesData: %p length: %ld (-1 means null)"
+ "CreateSandboxExtensionData failed: filenames null"
+ "DDBinderEmailKey"
+ "DDBinderFlightInformationKey"
+ "DDBinderTrackingNumberKey"
+ "DDResultGetCategory"
+ "DDResultHasType"
+ "DDScannerResult"
+ "DDScannerService"
+ "DDScannerServiceConfiguration"
+ "DDScannerSmallTimeout"
+ "Destination URL entry and sandbox extension entry missing, required to create unique promise drag destination"
+ "Destination URL entry missing, required to create unique promise drag destination"
+ "EnablePasteboardPrivacyDeveloperPreview"
+ "Entry failed validation: [%d, %{public}@]"
+ "Error detecting on pasteboard: %{public}@ (error: %{private}@)"
+ "Error detecting on pasteboard: %{public}@ result: %lld"
+ "Extension entry lacks data."
+ "Extension entry was not a dictionary."
+ "Extension entry was not a plist."
+ "Extension for entry has already been permanently applied to process. Skipping."
+ "Failed sandbox check for invalid path."
+ "Failed sandbox check for path."
+ "Failed sandbox check for path. [%d]"
+ "Failed to consume sandbox extension from pasteboard with error: %{darwin.errno}d  path: [%{private}@]"
+ "Failed to consume sandbox extension, required to create unique promise drag destination"
+ "Failed to decode pattern or type: %{public}@"
+ "Failed to get a sandbox extension (%d)"
+ "Failed to get destination URL, required to create unique promise drag destination"
+ "Failed to get destination sandbox extension, required to create unique promise drag destination"
+ "Failed to issue sandbox extension for path: [%{private}@]"
+ "Failed to release sandbox extension"
+ "Failed to send %{public}s message to daemon. Error: %{public}s"
+ "Failed to show approval dialog for '%{public}@ via client '%{public}@'. Error: %{public}s"
+ "Failed to show indirect approval dialog for '%{public}@ via CSUIA '%{public}@'. Error: %{public}s"
+ "Failure to flush owner changes."
+ "Failure to get flavors for item."
+ "Filenames entry: data invalid"
+ "Filenames entry: invalid array item"
+ "Filenames entry: not an array"
+ "Filenames entry: unable to create canonical path"
+ "Filenames entry: zero file names"
+ "Generation mismatch."
+ "Ignoring plist data for type public.url. Only URL data is allowed for this type."
+ "Incorrect input parameters."
+ "Informing %ld clients about outdated cached info for %ld modified entries for generation %llu of pasteboard '%{public}@'"
+ "Informing %ld clients about outdated cached info for generation %llu of pasteboard '%{public}@'"
+ "Invalid dictionary entry."
+ "Message lacked patterns or types."
+ "Metadata detection: image source contains no images."
+ "Metadata detection: no properties for image."
+ "No corresponding sandbox entry for file reference entry: [%d, %{public}@]"
+ "No data for file reference entry that supposedly hasData."
+ "No data for security scope entry corresponding to file reference entry."
+ "No extraction type determined."
+ "No flavors found on item."
+ "No pasteboard contents applicable to detection."
+ "No sandbox extension entry in cache when one was expected for item %ld flavor: %{public}@ (error: %d)"
+ "Not allowing process impersonation by process %{public}s (%{public}d) due to missing com.apple.private.defaults-impersonate entitlement."
+ "Paste location extension update not allowed"
+ "Paste location update not allowed"
+ "Path is not absolute"
+ "Process is not entitled to check in apps for paste verification."
+ "Process with pid %d was denied access to sandbox extension by owner"
+ "Process with pid %ld is not entitled for %{private}@ / %{private}@."
+ "Promise fulfilled - %lu bytes for '%{public}@' gen: %ld of flavor: '%{public}@'"
+ "RVv48@0:8@\"FBSSceneIdentity\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
+ "Received security scope entry that was a promise. This is unexpected."
+ "Received security scope entry that was invalid. This is unexpected."
+ "Reissued extension for process with pid %d"
+ "Replaced incorrect cache entry!"
+ "Replaced security scope entry that was a promise. This is unexpected."
+ "Sandbox extension creation failed: client lacks entitlements? for path: [%{private}@] [%{private}s] [%d]"
+ "Sandbox extension data required immediately for flavor %{public}@, but failed to obtain. (%d)"
+ "Sandbox extension entry missing, required to create unique promise drag destination"
+ "Security scope entry failed validation: [%d, %{public}@]"
+ "Sending reply to %{public}@ message"
+ "Some new entries were rejected! (%ld > %ld)"
+ "Something went wrong with the '%{public}s' connection: %{public}s"
+ "Something went wrong with the '%{public}s' connection: %{public}s\nInvalidation reason: %{public}s"
+ "Successfully consumed sandbox extension for path %{private}@"
+ "Successfully created sandbox extension for path: [%{private}@] [%{private}s] [%d]"
+ "Successfully released sandbox extension"
+ "TC,V_didLeakExtension"
+ "T^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}},R,V_pboard"
+ "Ti,VlastPboardError"
+ "T{?=[8I]},R,V_auditToken"
+ "URL [%{private}@] is not a file URL."
+ "URL entry: data invalid"
+ "URL entry: no path"
+ "URL entry: not a file URL"
+ "URL entry: unable to convert to file path URL"
+ "URL entry: unable to create canonical path"
+ "URLWithDataRepresentation:relativeToURL:"
+ "UTType"
+ "Unable to get file system representation"
+ "Unable to identify path(s) to check for file reference entry: [%d, %{public}@]"
+ "Unexpected reply from CoreServicesUIAgent."
+ "VB32@0:8@\"NSString\"16@\"NSString\"24"
+ "Vv104@0:8@\"<SEProxyInterface>\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSData\"80@\"NSNumber\"88@?<v@?@\"NSError\">96"
+ "Vv104@0:8@16@24@32@40@48@56@64@72@80@88@?96"
+ "Vv116@0:8@\"<SEProxyInterface>\"16C24@\"NSString\"28@\"NSData\"36@\"NSData\"44@\"NSData\"52@\"NSData\"60@\"NSData\"68@\"NSData\"76S84S88@\"NSData\"92@\"NSData\"100@?<v@?@\"SEEndPointAuthorizeResponse\"@\"NSError\">108"
+ "Vv116@0:8@16C24@28@36@44@52@60@68@76S84S88@92@100@?108"
+ "Vv136@0:8@\"<SEProxyInterface>\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"SEEndPointConfiguration\"48@\"NSData\"56@\"NSData\"64@\"NSString\"72@\"NSData\"80@\"NSData\"88@\"NSData\"96@\"NSArray\"104@\"NSNumber\"112@\"NSNumber\"120@?<v@?@\"SEEndPoint\"@\"NSError\">128"
+ "Vv136@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@?128"
+ "Vv24@0:8@\"BKSHIDEventDeferringPredicate\"16"
+ "Vv24@0:8@\"BKSHIDEventDeliveryRuleChangeTransaction\"16"
+ "Vv24@0:8@\"BKSProximityDetectionMaskChangeEvent\"16"
+ "Vv24@0:8@\"CESRModelProperties\"16"
+ "Vv24@0:8@\"CHSTimelineEntryRelevanceBox\"16"
+ "Vv24@0:8@\"CHSWidgetRelevanceServiceEvent\"16"
+ "Vv24@0:8@\"DNDBehaviorSettings\"16"
+ "Vv24@0:8@\"DNDBypassSettings\"16"
+ "Vv24@0:8@\"DNDScheduleSettings\"16"
+ "Vv24@0:8@\"DNDStateUpdate\"16"
+ "Vv24@0:8@\"FMDBluetoothDiscoveryXPCAdapterDevice\"16"
+ "Vv24@0:8@\"LBLocalSpeechRecognitionSettings\"16"
+ "Vv24@0:8@\"NFApplet\"16"
+ "Vv24@0:8@\"NSArray<__BKSHIDEventDeliveryChain__>\"16"
+ "Vv24@0:8@\"NSArray<__DNDMode__>\"16"
+ "Vv24@0:8@\"NSArray<__NSValue__>\"16"
+ "Vv24@0:8@\"NSArray<__PRSPosterRoleCollectionObserverUpdate__>\"16"
+ "Vv24@0:8@\"NSArray<__PRSRoleActivePosterObserverUpdate__>\"16"
+ "Vv24@0:8@\"NSArray<__PRSWallpaperObserverPathUpdate__>\"16"
+ "Vv24@0:8@\"NSArray<__PRSWallpaperObserverSnapshotUpdate__>\"16"
+ "Vv24@0:8@\"NSSet<__BKSHIDEventPolicyObservation__>\"16"
+ "Vv24@0:8@\"NSXPCListenerEndpoint\"16"
+ "Vv24@0:8@\"PRUISExternallyHostedPosterEntryPointWrapper\"16"
+ "Vv24@0:8@\"PRUISModalEntryPointResponse\"16"
+ "Vv24@0:8@\"SASLockStateTransport\"16"
+ "Vv24@0:8@\"SASPreheatOptions\"16"
+ "Vv24@0:8@\"SASPresentationState\"16"
+ "Vv24@0:8@\"SBSHomeScreenIconStyleConfiguration\"16"
+ "Vv24@0:8@\"SFRequestParameters\"16"
+ "Vv24@0:8@\"SFSpeechRecognitionResult\"16"
+ "Vv24@0:8@\"SUIBRequestProgress\"16"
+ "Vv24@0:8@\"SUIBSiriResponse\"16"
+ "Vv24@0:8@\"SiriDirectActionContext\"16"
+ "Vv24@0:8@\"SiriRemotePresentationBringUpContext\"16"
+ "Vv24@0:8@\"SiriTostadaContext\"16"
+ "Vv24@0:8@\"SiriVocalShortcutContext\"16"
+ "Vv24@0:8@\"TUNearbyDeviceHandle\"16"
+ "Vv24@0:8@\"WFWorkflowRunViewSource\"16"
+ "Vv24@0:8@\"WFWorkflowRunningContext\"16"
+ "Vv24@0:8@\"_DUIPresentationUpdate\"16"
+ "Vv24@0:8@?<v@?@\"<TUScreenShareAttributes>\">16"
+ "Vv24@0:8@?<v@?@\"AFAudioSessionCoordinationSnapshot\">16"
+ "Vv24@0:8@?<v@?@\"AFHomeAccessoryInfo\">16"
+ "Vv24@0:8@?<v@?@\"AFPeerInfo\"@\"NSArray\">16"
+ "Vv24@0:8@?<v@?@\"ATXFaceGalleryConfiguration\"@\"NSDate\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"CHSControlConfigurationHostsBox\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"CHSWidgetConfigurationHostsBox\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NFAssertionInternal\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NSArray\"@\"NSArray\"B>16"
+ "Vv24@0:8@?<v@?@\"NSArray<__NSString__>\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NSMutableArray\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NSString\"@\"NSArray\">16"
+ "Vv24@0:8@?<v@?@\"ODDSiriSchemaODDSiriClientEvent\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"TUCallProvider\">16"
+ "Vv24@0:8@?<v@?@\"TUConversationLink\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"TUConversationNotice\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?B@\"NSDictionary\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?BBI@\"NSError\">16"
+ "Vv24@0:8@?<v@?Bq@\"NSError\">16"
+ "Vv24@0:8@?<v@?Q@\"NSData\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?Q@\"NSData\"CII@\"NSError\">16"
+ "Vv24@0:8@?<v@?QQQ@\"NSError\">16"
+ "Vv24@0:8@?<v@?d>16"
+ "Vv24@0:8@?<v@?i>16"
+ "Vv28@0:8@\"<TUScreenShareAttributes>\"16B24"
+ "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB>20"
+ "Vv28@0:8B16@?<v@?@\"NSSet\"@\"NSError\">20"
+ "Vv28@0:8B16@?<v@?@\"NSString\">20"
+ "Vv28@0:8C16@?<v@?QI@\"NSError\">20"
+ "Vv28@0:8I16@?20"
+ "Vv28@0:8I16@?<v@?qB@\"NSDictionary\"@\"NSArray\">20"
+ "Vv32@0:8@\"AFMyriadAdvertisementContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "Vv32@0:8@\"AFSetAudioSessionActiveContext\"16@?<v@?@\"AFSetAudioSessionActiveResult\">24"
+ "Vv32@0:8@\"AFSpeechPackage\"16@\"AFDictationNLUResult\"24"
+ "Vv32@0:8@\"AFSpeechPackage\"16@\"AFSpeechInfoPackage\"24"
+ "Vv32@0:8@\"AKAttestationAnalyticsInfo\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"ATXFaceGalleryConfiguration\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"BKSAnimationFenceHandle\"16@\"BSAnimationSettings\"24"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
+ "Vv32@0:8@\"CESRSpeechParameters\"16@?<v@?@\"CESRModelProperties\"@\"NSError\">24"
+ "Vv32@0:8@\"CESRSpeechParameters\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "Vv32@0:8@\"CHSControlIdentity\"16@?<v@?@\"CHSControlDescriptor\"@\"NSError\">24"
+ "Vv32@0:8@\"CHSControlIdentity\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"CHSWidgetConfiguration\"16@\"NSString\"24"
+ "Vv32@0:8@\"CLSAdminRequestor\"16@?<v@?@@\"NSError\">24"
+ "Vv32@0:8@\"CLSSurvey\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "Vv32@0:8@\"FMDRepairDeviceContext\"16@?<v@?@\"FMDRepairDeviceResult\"@\"NSError\">24"
+ "Vv32@0:8@\"GKGameSettingsInternal\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"HUDConfiguration\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"MonitoredStates\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NFAssertionInternal\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NFECommercePaymentRequest\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSArray\"16@\"AFSpeechInfoPackage\"24"
+ "Vv32@0:8@\"NSArray\"16@\"NSDictionary\"24"
+ "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSError\"@\"NSArray\">24"
+ "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSSet\"@\"NSError\">24"
+ "Vv32@0:8@\"NSArray\"16@?<v@?B@\"_DUITargetLayerDescriptor\">24"
+ "Vv32@0:8@\"NSArray<__BKSHIDKeyboardDeviceProperties__>\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSArray<__BKSTouchDeliveryUpdate__>\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSArray<__CHSDescriptorEnablementChangeRequest__>\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSArray<__NSString__>\"16@\"NSString\"24"
+ "Vv32@0:8@\"NSArray<__NSUUID__>\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSArray<__UNCNotificationCategoryRecord__>\"16@\"NSString\"24"
+ "Vv32@0:8@\"NSArray<__UNCNotificationRecordUpdate__>\"16@\"NSString\"24"
+ "Vv32@0:8@\"NSArray<__UNSNotificationRecord__>\"16@\"NSString\"24"
+ "Vv32@0:8@\"NSData\"16@\"NSData\"24"
+ "Vv32@0:8@\"NSData\"16@?<v@?@\"NSDictionary\">24"
+ "Vv32@0:8@\"NSData\"16@?<v@?@\"PFServerPosterPath\"@\"NSError\">24"
+ "Vv32@0:8@\"NSData\"16@?<v@?B>24"
+ "Vv32@0:8@\"NSDate\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSDate\"16q24"
+ "Vv32@0:8@\"NSDictionary\"16@\"TUConversation\"24"
+ "Vv32@0:8@\"NSDictionary<__NSString__><__HTHangHUDInfo__>\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSDictionary<__NSString__><__HTProcessLaunchExitRecord__>\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSNumber\"16@\"NSData\"24"
+ "Vv32@0:8@\"NSNumber\"16@?<v@?@\"NSValue\"@\"NSError\">24"
+ "Vv32@0:8@\"NSObject<NFCFieldDetectSessionCallbacks>\"16@?<v@?@\"NSObject<NFCFieldDetectSessionInterface>\"@\"NSError\">24"
+ "Vv32@0:8@\"NSPredicate\"16@?<v@?B@\"NSError\">24"
+ "Vv32@0:8@\"NSSet\"16@\"NSString\"24"
+ "Vv32@0:8@\"NSSet\"16Q24"
+ "Vv32@0:8@\"NSString\"16@\"AFDictationOptions\"24"
+ "Vv32@0:8@\"NSString\"16@\"AFSpeechPackage\"24"
+ "Vv32@0:8@\"NSString\"16@\"AFSpeechRecognition\"24"
+ "Vv32@0:8@\"NSString\"16@\"NSURL\"24"
+ "Vv32@0:8@\"NSString\"16@\"NSURLPromisePair\"24"
+ "Vv32@0:8@\"NSString\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"NSString\"16@\"TUCallScreenShareAttributes\"24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"AFExperiment\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"GKGameActivityInternal\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"GKGameSettingsInternal\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"GKPlayerInternalOnboarding\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\"BB>24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"PFServerPosterPath\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"PFServerPosterPath\"@\"PFServerPosterPath\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"TUConversationProvider\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?i>24"
+ "Vv32@0:8@\"NSString\"16q24"
+ "Vv32@0:8@\"NSURL\"16@\"NSString\"24"
+ "Vv32@0:8@\"NSURL\"16@?<v@?@@\"NSError\">24"
+ "Vv32@0:8@\"NSURL\"16@?<v@?q@\"NSString\"@\"CKRecordID\"@\"NSError\">24"
+ "Vv32@0:8@\"NSUUID\"16@\"CXCallDTMFUpdate\"24"
+ "Vv32@0:8@\"NSUUID\"16@\"TUConversationHandoffContext\"24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"IXDataPromiseSeed\"@\"NSDictionary\"@\"NSError\">24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"PFServerPosterPath\"@\"NSError\">24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"TUConversationLink\"@\"NSError\">24"
+ "Vv32@0:8@\"PFServerPosterPath\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
+ "Vv32@0:8@\"PKBannerHandleState\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"PRSPosterSnapshotRequest\"16@?<v@?@\"PRSPosterSnapshotResponse\"@\"NSError\">24"
+ "Vv32@0:8@\"PRUISExternallyHostedPosterEntryPointWrapper\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"SFEntitledAssetConfig\"16@?<v@?@\"CESRModelProperties\"@\"NSError\">24"
+ "Vv32@0:8@\"SFTranscription\"16@\"SFTranscription\"24"
+ "Vv32@0:8@\"SiriAnalyticsXPCLargeMessageEnvelope\"16@?<v@?B@\"NSError\">24"
+ "Vv32@0:8@\"SiriDirectActionContext\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "Vv32@0:8@\"SiriPresentationIdentifierTransport\"16@\"SASPresentationState\"24"
+ "Vv32@0:8@\"TUCallDTMFUpdate\"16@\"NSString\"24"
+ "Vv32@0:8@\"TUCallRecordingRequest\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"TUCollaborationInitiator\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"TUConversation\"16@\"NSSet\"24"
+ "Vv32@0:8@\"TUConversation\"16@\"TUConversationActivityEvent\"24"
+ "Vv32@0:8@\"TUConversation\"16@\"TUConversationActivitySession\"24"
+ "Vv32@0:8@\"TUConversation\"16@\"TUConversationMember\"24"
+ "Vv32@0:8@\"TUConversation\"16@\"TUConversationParticipant\"24"
+ "Vv32@0:8@\"TUConversationActivity\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"TUConversationActivitySession\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"TUConversationLink\"16@?<v@?B@\"NSDate\"@\"NSError\">24"
+ "Vv32@0:8@\"TUConversationLink\"16@?<v@?B@\"NSError\">24"
+ "Vv32@0:8@\"TUConversationMember\"16@\"TUConversationLink\"24"
+ "Vv32@0:8@\"TUConversationParticipant\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"TUConversationProvider\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"TUScreenSharingRequest\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"WFAnyToolKitVariableContent\"16@?<v@?@\"WFAnyPropertyListObject\"@\"NSError\">24"
+ "Vv32@0:8@\"WFToolKitIndexingRequest\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"WFWorkflowRunViewSource\"16@?<v@?@\"WFWorkflowRunViewSource\"@\"NSError\">24"
+ "Vv32@0:8I16B20@?<v@?@\"NSError\">24"
+ "Vv32@0:8Q16@\"NSUUID\"24"
+ "Vv32@0:8Q16@24"
+ "Vv32@0:8Q16@?<v@?@\"NFAssertionInternal\"@\"NSError\">24"
+ "Vv32@0:8Q16@?<v@?@\"NSArray\">24"
+ "Vv32@0:8Q16@?<v@?B@\"NSError\">24"
+ "Vv32@0:8Q16@?<v@?S>24"
+ "Vv32@0:8q16@\"NSError\"24"
+ "Vv32@0:8q16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "Vv32@0:8q16@?<v@?@\"NSDate\">24"
+ "Vv36@0:8@\"GKPlayerInternal\"16i24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "Vv36@0:8@\"NSArray\"16B24@?<v@?@\"NSDictionary\"@\"NSError\">28"
+ "Vv36@0:8@\"NSArray\"16B24@?<v@?@\"NSError\">28"
+ "Vv36@0:8@\"NSData\"16B24@?<v@?@\"NSError\">28"
+ "Vv36@0:8@\"NSDictionary\"16@\"NSUUID\"24B32"
+ "Vv36@0:8@\"NSString\"16B24@?<v@?@\"GKLeaderboardChallengeInternal\"@\"NSError\">28"
+ "Vv36@0:8@\"NSString\"16B24@?<v@?@\"NSArray\">28"
+ "Vv36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
+ "Vv36@0:8@\"NSString\"16i24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "Vv36@0:8@\"NSURL\"16@\"NSString\"24i32"
+ "Vv36@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24B32"
+ "Vv36@0:8@16B24@28"
+ "Vv36@0:8B16@\"GKPlayerInternal\"20@?<v@?@\"NSError\">28"
+ "Vv36@0:8B16@\"TUCallScreenShareAttributes\"20@\"NSString\"28"
+ "Vv36@0:8B16@\"TUConversationActivitySession\"20@\"NSUUID\"28"
+ "Vv36@0:8B16@\"TUScreenShareAttributes\"20@\"NSUUID\"28"
+ "Vv36@0:8B16Q20@?<v@?@\"NSDictionary\"@\"NSError\">28"
+ "Vv36@0:8C16@\"NSData\"20@?<v@?Q@\"NSData\"I@\"NSError\">28"
+ "Vv36@0:8C16@\"NSData\"20@?<v@?QI@\"NSError\">28"
+ "Vv36@0:8C16@\"NSString\"20@?<v@?@\"NSError\">28"
+ "Vv36@0:8i16@\"GKPlayerInternal\"20@?<v@?@\"<GKAccountService>\"@\"<GKProfileService>\"@\"<GKFriendService>\"@\"<GKGameService>\"@\"<GKGameStatService>\"@\"<GKChallengeService>\"@\"<GKMultiplayerService>\"@\"<GKTurnBasedService>\"@\"<GKUtilityService>\"@\"<GKBulletinService>\">28"
+ "Vv36@0:8i16@\"GKPlayerInternal\"20@?<v@?@\"NSError\"@\"<GKAccountServicePrivate>\"@\"<GKProfileServicePrivate>\"@\"<GKFriendServicePrivate>\"@\"<GKGameServicePrivate>\"@\"<GKGameStatServicePrivate>\"@\"<GKChallengeServicePrivate>\"@\"<GKMultiplayerServicePrivate>\"@\"<GKTurnBasedServicePrivate>\"@\"<GKUtilityServicePrivate>\"@\"<GKBulletinServicePrivate>\">28"
+ "Vv36@0:8q16B24@?28"
+ "Vv36@0:8q16i24@?<v@?@\"NSError\">28"
+ "Vv40@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "Vv40@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"<SEProxyInterface>\"16@\"NSDictionary\"24@?<v@?@\"SEEndPoint\"@\"NSError\">32"
+ "Vv40@0:8@\"<SEProxyInterface>\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"<SEProxyInterface>\"16@\"NSString\"24@?<v@?@\"SEEndPointBindingAttestationRequestItems\"@\"NSError\">32"
+ "Vv40@0:8@\"AFSpeechPackage\"16@\"AFDictationNLUResult\"24@\"NSString\"32"
+ "Vv40@0:8@\"CHSExtensionIdentity\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"CHSWidget\"16@\"CHSWidgetMetrics\"24@?<v@?@\"BSAction\"@\"NSError\">32"
+ "Vv40@0:8@\"CLSOrganization\"16@\"NSArray\"24@?<v@?@@\"NSError\">32"
+ "Vv40@0:8@\"DNDModeAssertion\"16@\"DNDModeAssertionInvalidation\"24@\"NSArray<__NSString__>\"32"
+ "Vv40@0:8@\"DNDModeAssertion\"16@\"DNDStateUpdate\"24@\"NSArray<__NSString__>\"32"
+ "Vv40@0:8@\"FMFHandle\"16@\"FMFHandle\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "Vv40@0:8@\"NSArray\"16@\"<SEProxyInterface>\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "Vv40@0:8@\"NSArray\"16@\"AFDictationNLUResult\"24@\"NSString\"32"
+ "Vv40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8@\"NSArray\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"PFPosterPathsAssertion\"@\"NSError\">32"
+ "Vv40@0:8@\"NSArray<__PRSWallpaperObserverPathUpdate__>\"16@\"NSArray<__PRSRoleActivePosterObserverUpdate__>\"24@\"PRSPosterRoleCollectionObserverUpdate\"32"
+ "Vv40@0:8@\"NSArray<__WFContextualActionFile__>\"16@\"NSArray<__WFFinderImageResizeDescriptor__>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "Vv40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "Vv40@0:8@\"NSData\"16@\"NSNumber\"24@\"NSNumber\"32"
+ "Vv40@0:8@\"NSData\"16@\"WFWorkflowRunningContext\"24@?<v@?@\"WFWorkflowRunResult\"@\"NSError\">32"
+ "Vv40@0:8@\"NSDate\"16@\"NSString\"24q32"
+ "Vv40@0:8@\"NSDictionary\"16@\"NSData\"24@?<v@?@\"NFApplet\"@\"NSSet\"@\"NSError\">32"
+ "Vv40@0:8@\"NSNumber\"16@\"NSString\"24@\"SASTimeIntervalTransport\"32"
+ "Vv40@0:8@\"NSNumber\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSNumber\"16@\"PRSMigrationDescriptor\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSNumber\"16q24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFCCardSessionCallbackInterface>\"16@\"NFCardSessionConfig\"24@?<v@?@\"NSObject<NFCCardSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFContactlessPaymentSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFContactlessPaymentSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFContactlessSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFContactlessSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFCredentialSessionCallbackInterface>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFCredentialSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFECommercePaymentSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFECommercePaymentSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFFieldDetectSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFFieldDetectSessionInterface>\"@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFHostEmulationSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFHostEmulationSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFPeerPaymentSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFPeerPaymentSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFReaderSessionCallbacks>\"16@\"NFReaderSessionConfig\"24@?<v@?@\"NSObject<NFReaderSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFReaderSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFReaderSessionInternalInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSecureElementAndHostCardEmulationSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSecureElementAndHostCardEmulationSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSecureElementLoggingSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSecureElementLoggingSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSecureElementManagerSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSecureElementManagerSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSecureTransactionServicesHandoverHybridSessionCallbacksInterface>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSecureTransactionServicesHandoverHybridSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSecureTransactionServicesHandoverSessionCallbacksInterface>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSecureTransactionServicesHandoverSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSeshatSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSeshatSessionInterface>\"@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFTrustSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFTrustSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSSet\"16@\"NSSet\"24@\"NSUUID\"32"
+ "Vv40@0:8@\"NSSet\"16@\"TUConversationLink\"24@?<v@?@\"TUConversationLink\"@\"NSError\">32"
+ "Vv40@0:8@\"NSSet\"16Q24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8@\"NSSet\"16q24@?<v@?@\"TUConversationLink\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"CHSControlConfiguration\"24@\"NSNumber\"32"
+ "Vv40@0:8@\"NSString\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"LNActionMetadata\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"LNEntityMetadata\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"LNEnumMetadata\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"LNQueryMetadata\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"NSSet\"24@\"NSURLPromisePair\"32"
+ "Vv40@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32"
+ "Vv40@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32"
+ "Vv40@0:8@\"NSString\"16@\"PRSDataStoreArchiveConfiguration\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16@\"TUConversationLink\"24@?<v@?@\"TUConversationLink\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16Q24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16d24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSString\"16q24@?<v@?@\"NSDate\">32"
+ "Vv40@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32"
+ "Vv40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSURL\"@\"NSURL\">32"
+ "Vv40@0:8@\"NSURL\"16d24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSUUID\"16@\"NSArray<__PRSPosterUpdate__>\"24@?<v@?@\"PFServerPosterPath\"@\"NSArray<__PRSPosterUpdateResult__>\"@\"NSError\">32"
+ "Vv40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"NSUUID\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"PFServerPosterPath\"@\"NSError\">32"
+ "Vv40@0:8@\"NSUUID\"16B24B28@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"PFPosterPath\"16@\"PRSPosterUpdateSessionInfo\"24@?<v@?@\"PFPosterPathsAssertion\"@\"NSError\">32"
+ "Vv40@0:8@\"PKBannerHandleRequest\"16@\"PKBannerHandleState\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"PRSHostConfiguration\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"PRSPosterConfiguration\"16@\"NSArray<__PRSPosterUpdate__>\"24@?<v@?@\"PFServerPosterPath\"@\"NSArray<__PRSPosterUpdateResult__>\"@\"NSError\">32"
+ "Vv40@0:8@\"PRSPosterConfiguration\"16@\"NSNumber\"24@?<v@?@\"NSArray<__NSValue__>\"@\"NSError\">32"
+ "Vv40@0:8@\"PRSPosterConfiguration\"16@\"NSNumber\"24@?<v@?@\"NSValue\"@\"NSError\">32"
+ "Vv40@0:8@\"PRSPosterSnapshotCollection\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"SABaseCommand\"16@\"AFCommandExecutionInfo\"24@?<v@?@\"SABaseCommand\"@\"NSError\">32"
+ "Vv40@0:8@\"SASButtonIdentifierTransport\"16@\"SASTimeIntervalTransport\"24@\"SiriLongPressButtonContext\"32"
+ "Vv40@0:8@\"SEFidoKeySearchParameters\"16@\"<SEProxyInterface>\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24@\"NSURL\"32"
+ "Vv40@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24@?<v@?@\"NSString\">32"
+ "Vv40@0:8@\"TUCollaborationInitiator\"16@\"NSUUID\"24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8@\"TUConversation\"16@\"NSDate\"24Q32"
+ "Vv40@0:8@\"TUConversation\"16@\"TUConversationParticipant\"24@\"NSString\"32"
+ "Vv40@0:8@\"TUConversation\"16@\"TUConversationParticipant\"24@\"TUConversationNotice\"32"
+ "Vv40@0:8@\"TUConversation\"16Q24@\"TUConversationActivitySession\"32"
+ "Vv40@0:8@\"TUConversation\"16q24@\"NSString\"32"
+ "Vv40@0:8@\"TUConversationLink\"16q24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8@\"TUConversationParticipant\"16@\"TUConversation\"24@\"NSString\"32"
+ "Vv40@0:8@\"TUHandle\"16@\"TUConversationProvider\"24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8@\"UNSNotificationRecord\"16@\"NSString\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "Vv40@0:8@\"WFWorkflowDescriptor\"16@\"NSNumber\"24@\"WFDialogAttribution\"32"
+ "Vv40@0:8@\"WFWorkflowRunningContext\"16@\"WFWorkflowRunRequest\"24@?<v@?@\"WFWorkflowRunResult\"@\"NSError\">32"
+ "Vv40@0:8B16C20@\"NSData\"24@?<v@?QI@\"NSError\">32"
+ "Vv40@0:8B16Q20B28@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "Vv40@0:8C16C20@\"NSData\"24@?<v@?Q@\"NSData\"I@\"NSError\">32"
+ "Vv40@0:8Q16@\"CDPContext\"24@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">32"
+ "Vv40@0:8Q16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8q16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv44@0:8@\"<SEProxyInterface>\"16@\"NSString\"24B32@?<v@?@\"NSError\">36"
+ "Vv44@0:8@\"NSSet\"16@\"NSString\"24B32@?<v@?@\"NSArray\">36"
+ "Vv44@0:8@\"NSString\"16@\"NSString\"24B32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "Vv44@0:8@\"SFEntitledAssetConfig\"16B24@\"NSString\"28@?<v@?@\"NSError\">36"
+ "Vv48@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"SEEndPoint\"@\"NSError\">40"
+ "Vv48@0:8@\"FBSSceneIdentity\"16@\"FBSSceneParameters\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"FBSSceneIdentity\"16@\"FBSSceneSettingsDiff\"24@\"FBSSceneTransitionContext\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"NSArray\"16@\"CLSAdminRequestor\"24@\"NSArray\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "Vv48@0:8@\"NSData\"16@\"NSNumber\"24@\"NSData\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"NSDictionary\"16@\"NSString\"24q32@\"NSError\"40"
+ "Vv48@0:8@\"NSNumber\"16@\"NSNumber\"24@\"BKSAnimationFenceHandle\"32@\"BSAnimationSettings\"40"
+ "Vv48@0:8@\"NSObject<NFNdefTagSessionCallbacks>\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"NSObject<NFNdefTagSessionInterface>\"B@\"NSError\">40"
+ "Vv48@0:8@\"NSString\"16@\"NSError\"24@\"WFAnyPropertyListObject\"32@\"WFStepwiseExecutionResultMetadata\"40"
+ "Vv48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "Vv48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32@?<v@?@\"NSArray<__CHSControlDescriptor__>\"@\"NSError\">40"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSUUID\"40"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?>40"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"PFServerPosterPath\"@\"NSError\">40"
+ "Vv48@0:8@\"NSString\"16Q24@\"AFSpeechPackage\"32d40"
+ "Vv48@0:8@\"NSString\"16Q24B32B36@\"NSArray\"40"
+ "Vv48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"NSURL\"16d24@32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"SASButtonIdentifierTransport\"16@\"NSString\"24@\"SASTimeIntervalTransport\"32@\"SiriLongPressButtonContext\"40"
+ "Vv48@0:8@\"TUConversationLink\"16@\"NSDate\"24Q32@?<v@?B@\"NSError\">40"
+ "Vv48@0:8@\"TUConversationProvider\"16d24@\"NSString\"32@?<v@?@\"TUHandle\"@\"NSDate\"@\"NSError\">40"
+ "Vv48@0:8@\"TUHandle\"16@\"TUConversationProvider\"24@\"NSDate\"32@?<v@?B@\"NSDate\"@\"NSError\">40"
+ "Vv48@0:8@\"UNNotificationRequest\"16@\"NSNumber\"24@\"NSDate\"32@\"NSString\"40"
+ "Vv48@0:8@\"WRWidgetRendererSessionKey\"16@\"NSNumber\"24@\"LNAction\"32@?<v@?@\"NSError\">40"
+ "Vv48@0:8@\"_SFLanguageDetectorOptions\"16@\"_SFAnalyzerClientInfo\"24@\"_SFAnalysisOptions\"32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">40"
+ "Vv52@0:8@\"TUConversationParticipant\"16@\"TUConversation\"24@\"NSString\"32@\"NSString\"40B48"
+ "Vv52@0:8@16@24@32B40@?44"
+ "Vv56@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "Vv56@0:8@\"<SEProxyInterface>\"16@\"NSString\"24@\"NSData\"32@\"NSArray\"40@?<v@?@\"SESLegacyKeyCreateResponse\"@\"NSError\">48"
+ "Vv56@0:8@\"CHSWidget\"16@\"CHSWidgetMetrics\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"BSAction\"@\"NSArray<__ATXInfoTimelineEntry__>\"@\"NSError\">48"
+ "Vv56@0:8@\"NSLocale\"16@\"NSString\"24q32q40@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">48"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSUUID\"40@?<v@?q@\"NSError\">48"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"AFCommandExecutionInfo\"40@?<v@?@\"NSDictionary\"@\"NSArray\"@\"NSError\">48"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSArray\"40@?<v@?@\"NSError\">48"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSURLPromisePair\"32@\"NSString\"40@\"NSString\"48"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24q32q40@?<v@?@\"NSError\">48"
+ "Vv56@0:8@\"NSString\"16{CGSize=dd}24B40B44@?<v@?@\"NSError\">48"
+ "Vv56@0:8@\"NSString\"16{CGSize=dd}24B40B44@?<v@?@\"NSError\"BB>48"
+ "Vv56@0:8@\"UNSNotificationRecord\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSString\"40@?<v@?@\"NSNumber\"@\"NSError\">48"
+ "Vv56@0:8@\"WFWorkflowRunDescriptor\"16@\"WFWorkflowRunRequest\"24@\"NSNumber\"32@\"WFWorkflowRunningContext\"40@?<v@?@\"WFWorkflowRunResult\"@\"NSError\">48"
+ "Vv60@0:8@\"NSLocale\"16@\"NSString\"24@\"NSString\"32@\"NSURL\"40B48@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">52"
+ "Vv60@0:8q16{CGSize=dd}24@\"NSString\"40B48@?<v@?B@\"NSError\">52"
+ "Vv60@0:8q16{CGSize=dd}24@40B48@?52"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48@?<v@?@\"NSData\"@\"NSError\">56"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSData\"32@\"NSUUID\"40@\"NSNumber\"48@?<v@?@\"SEEndPoint\"@\"NSError\">56"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSString\"32@\"NSData\"40@\"NSArray\"48@?<v@?@\"NSData\"@\"NSError\">56"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSNumber\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@?<v@?@\"SESLegacyKeySignResponse\"@\"NSError\">56"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSNumber\"24@\"NSData\"32@\"NSData\"40@\"NSNumber\"48@?<v@?@\"SESLegacyKeySignResponse\"@\"NSError\">56"
+ "Vv64@0:8@\"<SEProxyInterface>\"16@\"NSString\"24B32@\"NSString\"36B44@\"NSString\"48@?<v@?@\"NSError\">56"
+ "Vv64@0:8@\"NSArray\"16@\"NFApplet\"24@\"NSArray\"32@\"NSData\"40Q48@?<v@?@\"NSError\">56"
+ "Vv64@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSData\"40@\"<SEProxyInterface>\"48@?<v@?@\"NSArray\"@\"NSError\">56"
+ "Vv64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSURL\"40@\"NSString\"48@?<v@?@\"NSURL\"@\"NSURL\">56"
+ "Vv64@0:8@\"NSString\"16@\"NSArray\"24q32@\"NSString\"40q48@?<v@?@\"NSError\">56"
+ "Vv64@0:8@\"NSString\"16{CGSize=dd}24B40B44@\"NSXPCListenerEndpoint\"48@?<v@?@\"NSError\">56"
+ "Vv64@0:8@\"NSString\"16{CGSize=dd}24B40B44@\"NSXPCListenerEndpoint\"48@?<v@?@\"NSError\"BB>56"
+ "Vv64@0:8@16@24B32@36B44@48@?56"
+ "Vv72@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32Q40B48B52@\"NSSet\"56@?<v@?@\"NSDictionary\"@\"NSError\">64"
+ "Vv72@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSArray\"48@\"NSString\"56@?<v@?@\"GKLeaderboardChallengeInternal\"@\"NSError\">64"
+ "Vv72@0:8q16q24d32@\"NSArray\"40d48q56d64"
+ "Vv76@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32@\"NSArray\"40@\"NSString\"48@\"NSString\"56B64@?<v@?@\"NSDictionary\"@\"NSError\">68"
+ "Vv76@0:8q16Q24@\"NSArray\"32@\"GKPlayerInternal\"40B48@\"NSArray\"52@\"GKGameDescriptor\"60@?<v@?@\"NSError\">68"
+ "Vv80@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"AFDictationNLUResult\"48@\"NSString\"56@\"NSDictionary\"64@\"AFSpeechAudioAnalytics\"72"
+ "Vv80@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72"
+ "Vv88@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80"
+ "WBSUnifiedFieldInputTypeForString"
+ "Will attempt to register %ld entries for generation %llu of pasteboard '%{public}@'"
+ "Zero patterns or types extracted."
+ "^{FBNewCaptureCoordinatorConfiguration={FBCaptureCoordinatorConfiguration={FBCameraConfiguration=BBqq@BBBCBBBBBBqBBff{FBBracketedCaptureConfiguration=@^?BBQ}dBBBB@?{CGSize=dd}BBBBBBB@@@BII{FBCaptureAutoExposureConfiguration=BBBBBB}{FBCapturePOIDetectorConfiguration=qddB}B@BB{CGSize=dd}{FBPhotoCaptureConfiguration=BBBBBBQ}BBB{FBCameraSimulationConfiguration=@?@?BBB}BBB{FBRecordingConfiguration=@?@?B{?=qiIq}B}BBiB@BiB}{FBRendererConfiguration=BBBBBBBBBiBBBBBB}{FBPreviewConfiguration=B@{CGRect={CGPoint=dd}{CGSize=dd}}BBB}{FBGestureConfiguration=B}QQdBBBBB{CGSize=dd}BB}{FBPostCaptureCoordinatorConfiguration={FBRendererConfiguration=BBBBBBBBBiBBBBBB}B@}}16@0:8"
+ "^{__CFData=}48@0:8{?=[8I]}16"
+ "^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}"
+ "^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}16@0:8"
+ "_CFPasteboardDetect"
+ "_CFPasteboardDetect_block_invoke"
+ "_CFPasteboardHandleFulfillMessage"
+ "_auditToken"
+ "_coreServicesUIAgentClientInstance"
+ "_destinationProcessID"
+ "_detectionLastDialogGeneration"
+ "_detectionLastDialogRequestTime"
+ "_detectionLastDialogResponse"
+ "_didLeakExtension"
+ "_ensureCSUIAIsRunning"
+ "_handleDetectionOfType:withMessage:"
+ "_hasCheckedPath"
+ "_isCSUIA"
+ "_localPromiseState"
+ "_localPromisor"
+ "_onDialogQueue_sendShowInAppApprovalDialogIPC"
+ "_onDialogQueue_sendShowIndirectApprovalDialogIPCForCLIProcess:"
+ "_onqueue_CFPasteboardRequestLocalPromiseData_block_invoke"
+ "_onqueue_CFPasteboardShowApprovalDialogIfNecessaryForPasteboard_block_invoke_2"
+ "_onqueue_CFPasteboardShowIndirectApprovalDialogIfNecessaryForPasteboard_block_invoke_2"
+ "_onqueue_handleNewRegularEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:"
+ "_onqueue_handleNewSecurityScopeEntries:forMessage:withSourceAuditToken:shouldInvalidateClientMetadata:"
+ "_onqueue_isManagedPromiseDragWithCache:forGeneration:itemIdentifier:"
+ "_onqueue_isPasteLocationRelatedEntryAllowedForMessage:"
+ "_onqueue_postflightNewEntries:forMessage:withPreflightData:"
+ "_onqueue_preflightNewEntries:forMessage:"
+ "_onqueue_validateToken:forRequestingApp:"
+ "_patternDetectionQueue"
+ "_remotePromiseState"
+ "_remotePromisor"
+ "_setRemotePromiseState:"
+ "_showCurrentApprovalDialogAndWaitForReply"
+ "approval dialog"
+ "auditToken"
+ "bool"
+ "boolForKey:"
+ "checkResourceIsReachableAndReturnError:"
+ "cmd"
+ "com.apple.CFPasteboard.pattern-detection"
+ "com.apple.appkit.pasteboard-detection-pattern."
+ "com.apple.appkit.pasteboard-detection-pattern.dd."
+ "com.apple.appkit.pasteboard-detection-pattern.dd.address"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.email"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.event"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.flight"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.link"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.money"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.phone"
+ "com.apple.appkit.pasteboard-detection-pattern.dd.shipment"
+ "com.apple.appkit.pasteboard-detection-pattern.number"
+ "com.apple.appkit.pasteboard-detection-pattern.probable-web-search"
+ "com.apple.appkit.pasteboard-detection-pattern.probable-web-url"
+ "com.apple.appkit.pasteboard-metadata-type.contenttype"
+ "com.apple.appkit.pasteboard-metadata-type.imageproperties"
+ "com.apple.coreservices.quarantine-resolver"
+ "com.apple.coreservices.uiagent.status"
+ "com.apple.pboard.cancel-indirect-approval-dialog"
+ "com.apple.pboard.detect-metadata"
+ "com.apple.pboard.detect-patterns"
+ "com.apple.pboard.detect-values"
+ "com.apple.pboard.pattern-array"
+ "com.apple.pboard.pattern-dictionary"
+ "com.apple.pboard.show-approval-dialog"
+ "com.apple.pboard.show-indirect-approval-dialog"
+ "completionHandler != nil"
+ "completionQueue != nil"
+ "completionWasCalled == YES"
+ "componentsSeparatedByCharactersInSet:"
+ "coreResult"
+ "d24@?0d8q16"
+ "d32@0:8d16@24"
+ "d40@0:8@16@24q32"
+ "d48@0:8@16@24@32d40"
+ "d@:"
+ "didHandleCreate"
+ "didLeakExtension"
+ "fileURLWithPath:"
+ "fulfillAsync == true"
+ "getUserApproval:inApp:withCompletion:"
+ "handleDetectMetadata:"
+ "handleDetectPatterns:"
+ "handleDetectValues:"
+ "i200@0:8{CLStepCountEntry=dddIddddIIdddi^{__CFString}BB{CLAccelerometerPace=ddd}IICII(FalseStepDetectorStateUnion={FalseStepDetectorState=b1b1b1b1b1b1b1b1}C)CCi}16^v192"
+ "i20@?0@\"JSValue\"8i16"
+ "i28@0:8r^v16B24"
+ "i32@0:8^{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}16r^v24"
+ "i32@0:8^{CLExerciseMinuteData=id^{__CFString}}16^v24"
+ "i32@0:8^{CLNatalieData=i^{__CFString}diBBddqqd[16C]}16^v24"
+ "i32@0:8r^{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}16r^v24"
+ "i40@0:8r^v16B24B28r^{CLNetworkLocationRequestConfig=i}32"
+ "i64@0:8@16@24@32@40@48@56"
+ "indirect approval dialog"
+ "initWithScannerType:passiveIntent:"
+ "invalid timebase"
+ "isCSUIA"
+ "isLocal == YES"
+ "kCGImagePropertyDPIHeight"
+ "kCGImagePropertyDPIWidth"
+ "kCGImagePropertyDepth"
+ "kCGImagePropertyHasAlpha"
+ "kCGImagePropertyOrientation"
+ "kCGImagePropertyPixelHeight"
+ "kCGImagePropertyPixelWidth"
+ "kCGImageSourceForceUseServer"
+ "kCGImageSourceShouldMemoryMap"
+ "kTCCServiceSystemPolicyAllFiles"
+ "lastPathComponent"
+ "lastPboardError"
+ "no useable token"
+ "numberWithDouble:"
+ "onqueue_analyzeSandboxExtensionEntry:destinedForClient:"
+ "onqueue_filterDataFromEntry:inResponseToMessage:error:"
+ "onqueue_reissueSandboxExtensionFromEntry:toClient:error:"
+ "pathExtension"
+ "promisorCompletion != nil"
+ "q36@0:8q16I24@28"
+ "r^{__CFArray=}32@0:8^{__CFArray=}16@24"
+ "resolvePromisedDataWithCompletionQueue:isLocalPromise:completionHandler:"
+ "scanDouble:"
+ "scanString:range:configuration:"
+ "scannerWithString:"
+ "setDidLeakExtension:"
+ "setLastPboardError:"
+ "setRemoteScannerEnabled:"
+ "stringByAppendingPathComponent:"
+ "stringByDeletingLastPathComponent"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringByResolvingSymlinksInPath"
+ "stringByStandardizingPath"
+ "stringWithCString:encoding:"
+ "token is valid"
+ "typeWithFilenameExtension:"
+ "v104@0:8@\"CPLResource\"16Q24@\"NSDictionary\"32{?={?=qiIq}{?=qiIq}}40@\"NSString\"88@?<v@?@\"NSURL\"@\"NSData\"@\"NSDate\"@\"NSString\"@\"NSError\">96"
+ "v108@0:8@16B24@28@36@44@52@60@68@76@84@92@?100"
+ "v112@0:8@\"NSData\"16@\"NSData\"24@\"NSDictionary\"32@\"NSArray\"40@\"NSData\"48@\"NSData\"56Q64Q72@\"NSData\"80@\"NSData\"88@\"NSString\"96@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"I@\"NSError\">104"
+ "v112@0:8@16@24@32@40@48@56Q64Q72@80@88@96@?104"
+ "v1136@0:8{Result={CLBodyMetrics=iiffffffffifBfBBB}BBBiidddddddBBIIB{Result=dd{Features=dddd}{Result=iiiidd{FusionLikelihoods=dd}I}{Features=ddddddddddddddddddd}{Result=iiiidd{FusionLikelihoods=dd}I}{Features=dddddddddd}{Result=iiiidd{FusionLikelihoods=dd}I}{Features=dddd}{Result=iiiidd{FusionLikelihoods=dd}I}{Features=dddddddddddddddddddddddddddddd}B}{Features=dddddd}{Features=ddd}{EventResult=BBBdddBBB{SteadinessEvent=ddi}ddd}iB{DailyHealthKitStats=iidd}}16"
+ "v116@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48@\"NSString\"56i64@\"NSString\"68{?=[8I]}76@?<v@?@\"NSError\">108"
+ "v120@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96@\"NSDate\"104@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">112"
+ "v120@0:8{DirectionOfTravelAssistance=dddddddddBBBBBidd}16"
+ "v128@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48B56@\"NSString\"60@\"NSString\"68@\"NSString\"76B84@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSNumber\"112@?<v@?B@\"NSError\">120"
+ "v136@0:8{VO2MaxInput=Q[16C]fdffdidBBiqddB}16@?128"
+ "v144@0:8{CATransform3D=dddddddddddddddd}16"
+ "v16@?0@\"<CGRemotePDFDocumentProtocol>\"8"
+ "v16@?0@\"<CGRemotePDFPageProtocol>\"8"
+ "v16@?0@\"<CKXPCLogicalDeviceScopedClient>\"8"
+ "v16@?0@\"<CKXPCProcessScopedClient>\"8"
+ "v16@?0@\"<CKXPCProcessScopedDaemon>\"8"
+ "v16@?0@\"<TUScreenShareAttributes>\"8"
+ "v16@?0@\"AAAttributionResult\"8"
+ "v16@?0@\"AFSetAudioSessionActiveResult\"8"
+ "v16@?0@\"CTSignalStrengthMeasurements\"8"
+ "v16@?0@\"DiagnosticDevice\"8"
+ "v16@?0@\"INIntent\"8"
+ "v16@?0@\"ISGenerationResponse\"8"
+ "v16@?0@\"ISIconCacheConfiguration\"8"
+ "v16@?0@\"LSExtensionPointRecord\"8"
+ "v16@?0@\"MRAVRoutingDiscoverySessionConfiguration\"8"
+ "v16@?0@\"NDODeviceInfo\"8"
+ "v16@?0@\"NEVirtualInterfaceParameters\"8"
+ "v16@?0@\"NSDate\"8"
+ "v16@?0@\"OSLogEntry\"8"
+ "v16@?0@\"PKAccountEnhancedMerchantBehavior\"8"
+ "v16@?0@\"PKExpressPassConfiguration\"8"
+ "v16@?0@\"PKGroupsControllerSnapshot\"8"
+ "v16@?0@\"PKPaymentOfferCatalog\"8"
+ "v16@?0@\"PKPaymentRewardsRedemption\"8"
+ "v16@?0@\"PKPeerPaymentPreferences\"8"
+ "v16@?0@\"PLCPLSettings\"8"
+ "v16@?0@\"PRChipInfo\"8"
+ "v16@?0@\"PVAppIdentityDigest\"8"
+ "v16@?0@\"SFCredentialProviderExtensionState\"8"
+ "v16@?0@\"SPBeaconSharingLimits\"8"
+ "v16@?0@\"STCallingStatusDomainCallDescriptor\"8"
+ "v16@?0@\"TUCallProvider\"8"
+ "v16@?0@\"TUConversationProvider\"8"
+ "v16@?0@\"TribecaStatus\"8"
+ "v16@?0@\"UARPAssetID\"8"
+ "v16@?0@\"UISSlotRemoteContent\"8"
+ "v16@?0@\"WFWorkflowReference\"8"
+ "v16@?0@\"_LTLocaleModalities\"8"
+ "v16@?0@\"_OSInactivityPredictorMetadata\"8"
+ "v16@?0@\"_TtC7Empower29GWMPreLoginBulletinsViewModel\"8"
+ "v16@?0@?<{ScanResult=d{vector<CLWifiService_Type::AccessPoint, std::allocator<CLWifiService_Type::AccessPoint>>=^{AccessPoint}^{AccessPoint}{__compressed_pair<CLWifiService_Type::AccessPoint *, std::allocator<CLWifiService_Type::AccessPoint>>=^{AccessPoint}}}}@?>8"
+ "v16@?0^{__CFArray=}8"
+ "v16@?0^{__CFData=}8"
+ "v16@?0i8I12"
+ "v172@0:8{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}16"
+ "v180@0:8{?=i{?=dd}ddddddddidi{?=dd}diIiiidB}16@?172"
+ "v184@0:8{WorkoutSettings=[16C][16C][16C]qq(WorkoutAttrib={SwimAttrib=qd}Q){FitnessPlusInfo=B[64c]q}Q}16"
+ "v188@0:8{WorkoutSettings=[16C][16C][16C]qq(WorkoutAttrib={SwimAttrib=qd}Q){FitnessPlusInfo=B[64c]q}Q}16B184"
+ "v18@0:8{?=BB}16"
+ "v196@0:8{WorkoutSettings=[16C][16C][16C]qq(WorkoutAttrib={SwimAttrib=qd}Q){FitnessPlusInfo=B[64c]q}Q}16@?184B192"
+ "v20@0:8S16"
+ "v20@?0@\"NSSet\"8B16"
+ "v20@?0C8@?<v@?C>12"
+ "v20@?0i8@\"CADSequenceToken\"12"
+ "v240@0:8{BoutMetrics=iddIiIIdCidddddddddddffffffIIIIIIIIIIfBfB}16"
+ "v24@0:8@\"<APMetricProtocol>\"16"
+ "v24@0:8@\"<CSAttendingServiceDelegate>\"16"
+ "v24@0:8@\"<FBSceneClientProcess>\"16"
+ "v24@0:8@\"<NDDownloadConsumer>\"16"
+ "v24@0:8@\"<TUCallHistoryControllerXPCClient>\"16"
+ "v24@0:8@\"<TUConversationProviderManagerXPCClient>\"16"
+ "v24@0:8@\"<TUNeighborhoodActivityConduitXPCClient>\"16"
+ "v24@0:8@\"AAAudioSessionControl\"16"
+ "v24@0:8@\"AFSpeechSynthesisRecord\"16"
+ "v24@0:8@\"AMSEngagementPushEvent\"16"
+ "v24@0:8@\"ASDSupportedDialogHandlers\"16"
+ "v24@0:8@\"ATXFaceGalleryConfiguration\"16"
+ "v24@0:8@\"ATXUserEducationSuggestionEvent\"16"
+ "v24@0:8@\"ATXUserEducationSuggestionFeedback\"16"
+ "v24@0:8@\"AUNotificationRequest\"16"
+ "v24@0:8@\"AWDLTrafficRegistrationConfiguration\"16"
+ "v24@0:8@\"AudioAccessoryDevice\"16"
+ "v24@0:8@\"BMComputeXPCSubscription\"16"
+ "v24@0:8@\"BSAction\"16"
+ "v24@0:8@\"BSSettings\"16"
+ "v24@0:8@\"CHRemotePowerLoggingRequest\"16"
+ "v24@0:8@\"CKProcessScopedMetadata\"16"
+ "v24@0:8@\"CKRecordZone\"16"
+ "v24@0:8@\"CKThrottle\"16"
+ "v24@0:8@\"CLVisionNotification\"16"
+ "v24@0:8@\"CSAttendingTriggerInfo\"16"
+ "v24@0:8@\"CTQoSLinkCharacteristics\"16"
+ "v24@0:8@\"DOCItemBookmark\"16"
+ "v24@0:8@\"DOCUIPBrowserState\"16"
+ "v24@0:8@\"FBSSceneUpdate\"16"
+ "v24@0:8@\"FSTaskDescription\"16"
+ "v24@0:8@\"GEOComposedRoute\"16"
+ "v24@0:8@\"GEOComposedRouteTraffic\"16"
+ "v24@0:8@\"HKCloudSyncRequest\"16"
+ "v24@0:8@\"HKDatabaseAccessibilityAssertion\"16"
+ "v24@0:8@\"HKMCExperienceModel\"16"
+ "v24@0:8@\"HKMobilityWalkingSteadinessNotificationStatus\"16"
+ "v24@0:8@\"HKMobilityWalkingSteadinessOnboardingStatus\"16"
+ "v24@0:8@\"HKSPSleepEvent\"16"
+ "v24@0:8@\"HKSPSleepModeObject\"16"
+ "v24@0:8@\"HKSPSleepScheduleStateObject\"16"
+ "v24@0:8@\"HMDeviceDiagnosticRecord\"16"
+ "v24@0:8@\"HMDeviceRecord\"16"
+ "v24@0:8@\"IAXPCObject\"16"
+ "v24@0:8@\"IDSCertifiedDeliveryContext\"16"
+ "v24@0:8@\"MNUserOptions\"16"
+ "v24@0:8@\"MRGroupSessionInfo\"16"
+ "v24@0:8@\"NDDownloadLimits\"16"
+ "v24@0:8@\"NEVirtualInterfaceParameters\"16"
+ "v24@0:8@\"NFNdefMessageInternal\"16"
+ "v24@0:8@\"NIAcwgM3Msg\"16"
+ "v24@0:8@\"NINearbyObject\"16"
+ "v24@0:8@\"NISystemState\"16"
+ "v24@0:8@\"NSArray<__BKSEventDeferringChainIdentity__>\"16"
+ "v24@0:8@\"NTKFaceInstanceDescriptor\"16"
+ "v24@0:8@\"PBCodable\"16"
+ "v24@0:8@\"PCDisambiguationContext\"16"
+ "v24@0:8@\"PCHomeKitIdentifier\"16"
+ "v24@0:8@\"PCLockscreenControlsDevice\"16"
+ "v24@0:8@\"PCLockscreenControlsObserver\"16"
+ "v24@0:8@\"PCMediaRemoteIdentifier\"16"
+ "v24@0:8@\"PCMediaTransferContext\"16"
+ "v24@0:8@\"PHPickerUpdateConfiguration\"16"
+ "v24@0:8@\"PKDiscoveryItem\"16"
+ "v24@0:8@\"PKPaymentRequestCouponCodeUpdate\"16"
+ "v24@0:8@\"PRUISAnalysisServiceRequest\"16"
+ "v24@0:8@\"RTIDocumentTraits\"16"
+ "v24@0:8@\"RVQuery\"16"
+ "v24@0:8@\"SAUIDelayedActionCommand\"16"
+ "v24@0:8@\"SBSHomeScreenIconStyleConfiguration\"16"
+ "v24@0:8@\"SBSHomeScreenServiceArrayOfStrings\"16"
+ "v24@0:8@\"SECFUserNotification\"16"
+ "v24@0:8@\"SFB389NFCPromptConfiguration\"16"
+ "v24@0:8@\"SFPunchout\"16"
+ "v24@0:8@\"SFSafariCredential\"16"
+ "v24@0:8@\"SOSButtonPressState\"16"
+ "v24@0:8@\"SOSStatus\"16"
+ "v24@0:8@\"SPDelegatedLocationResult\"16"
+ "v24@0:8@\"SPDeviceEventFetchResult\"16"
+ "v24@0:8@\"SRUIFLatencyInformation\"16"
+ "v24@0:8@\"SRUIFSiriSessionInfo\"16"
+ "v24@0:8@\"STUserNotificationContext\"16"
+ "v24@0:8@\"SUAnalyticsEvent\"16"
+ "v24@0:8@\"SUCoreDDMDeclaration\"16"
+ "v24@0:8@\"SUCoreDDMDeclarationGlobalSettings\"16"
+ "v24@0:8@\"SURollbackDescriptor\"16"
+ "v24@0:8@\"SUScanResults\"16"
+ "v24@0:8@\"TRISQLiteCKDatabaseFailureInjectionDelegate\"16"
+ "v24@0:8@\"UARPConsent\"16"
+ "v24@0:8@\"UARPServiceUpdaterDASMatchingRule\"16"
+ "v24@0:8@\"UARPServiceUpdaterMatchedEARule\"16"
+ "v24@0:8@\"UIKeyCommand\"16"
+ "v24@0:8@\"UISClickAttribution\"16"
+ "v24@0:8@\"UITraitCollection\"16"
+ "v24@0:8@\"ULCustomLoiConfiguration\"16"
+ "v24@0:8@\"ULFingerprintMetaInfo\"16"
+ "v24@0:8@\"ULPrediction\"16"
+ "v24@0:8@\"ULServiceStatus\"16"
+ "v24@0:8@\"UNNotificationContent\"16"
+ "v24@0:8@\"W5PeerDiscoveryEvent\"16"
+ "v24@0:8@\"WBSSavedAccount\"16"
+ "v24@0:8@\"WFWorkflowReference\"16"
+ "v24@0:8@\"_LTInstallRequest\"16"
+ "v24@0:8@\"_LTSELFLoggingTranslationLIDData\"16"
+ "v24@0:8@\"_PSCNAutocompleteFeedback\"16"
+ "v24@0:8@\"_TtC14NearbySessions19NearbyAdvertisement\"16"
+ "v24@0:8@\"_TtC14NearbySessions22InvitationJoinResponse\"16"
+ "v24@0:8@\"_TtC14NearbySessions29IncomingInvitationJoinRequest\"16"
+ "v24@0:8@\"_TtC8Feedback18FBKSubmissionError\"16"
+ "v24@0:8@\"_UIDismissInteractionUpdate\"16"
+ "v24@0:8@\"_UISheetPresentationControllerClientConfiguration\"16"
+ "v24@0:8@?<v@?@\"<AMSDPaymentConfirmationInterface>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<AMSFraudReportServiceInterface>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<AMSPaymentValidationServiceInterface>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<ASCLockupFetcherService>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<ASCMetricsService>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<ASCUtilityService>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<ASDAppMetricsServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<ASDAppStoreServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<ASDRestoreServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<CKXPCProcessScopedClient>\">16"
+ "v24@0:8@?<v@?@\"<CKXPCProcessScopedDaemon>\">16"
+ "v24@0:8@?<v@?@\"<EMDiagnosticInfoGathererInterface>\">16"
+ "v24@0:8@?<v@?@\"<IDSXPCEventReporting>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<IDSXPCOffGridMessenger>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<IDSXPCOffGridStateManager>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<IDSXPCPinnedIdentity>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<IDSXPCServerMessaging>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<PLAssetsdNonBindingDebugServiceProtocol>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"AAURLConfiguration\"@\"NSHTTPURLResponse\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"APClientState\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"APPerAppManagedProtectability\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"ASPasskeyCredentialRequestParameters\">16"
+ "v24@0:8@?<v@?@\"ATXFaceGalleryConfiguration\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"ATXSportsResponse\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"BDSCloudSyncDiagnosticInfo\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"BDSReadingGoalsStateInfo\"B>16"
+ "v24@0:8@?<v@?@\"BDSReadingHistoryServiceStatusInfo\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"BDSReadingHistoryStateInfo\"B>16"
+ "v24@0:8@?<v@?@\"BSAction\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CHSTimelineEntryRelevanceBox\"@\"BSAction\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CHSynthesisStyleInventoryStatus\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CKAccountInfo\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CKRecordID\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CLLocation\">16"
+ "v24@0:8@?<v@?@\"CNChangeHistoryAnchor\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CPLScopeChange\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CTQoSLinkCharacteristics\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CTRadioFrequencyFrontEndScanData\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"CTSatelliteMessagingProvisioning\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"DCCredentialAuthACL\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"DCCredentialNonce\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"FMDActivationLockInfo\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKFeatureAvailabilityRequirementSet\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKFeatureOnboardingRecord\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKMCCachedPregnancyModel\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKMCExperienceModel\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKMobilityWalkingSteadinessNotificationStatus\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKMobilityWalkingSteadinessOnboardingStatus\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKPairedFeatureAttributes\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"HKSPSleepScheduleModel\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"IDSPinnedIdentity\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"ISIconCacheConfiguration\">16"
+ "v24@0:8@?<v@?@\"LACDTORatchetStateComposite\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"LSExtensionPointRecord\">16"
+ "v24@0:8@?<v@?@\"MRAVRoutingDiscoverySessionConfiguration\">16"
+ "v24@0:8@?<v@?@\"MSPSharedTripSharingIdentity\"@\"NSArray\"@\"NSDictionary\"@\"NSArray\"Q>16"
+ "v24@0:8@?<v@?@\"MTAlarm\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NDODevice\">16"
+ "v24@0:8@?<v@?@\"NRMutableDeviceCollection\"@\"NRSecureDevicePropertyStore\"QB>16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSDate\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSDictionary\">16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\"Qd@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\"q@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\">16"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"I@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDate\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSDictionary\"q>16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"SUIAutomationServiceError\">16"
+ "v24@0:8@?<v@?@\"NSError\"@\"<NSSecureCoding>\"I>16"
+ "v24@0:8@?<v@?@\"NSError\"@\"AUParameterTree\">16"
+ "v24@0:8@?<v@?@\"NSError\"@\"NSData\"@\"NSString\">16"
+ "v24@0:8@?<v@?@\"NSError\"@\"NSString\">16"
+ "v24@0:8@?<v@?@\"NSError\"@\"SDMDMConfiguration\">16"
+ "v24@0:8@?<v@?@\"NSError\"Q>16"
+ "v24@0:8@?<v@?@\"NSError\"d>16"
+ "v24@0:8@?<v@?@\"NSError\"q>16"
+ "v24@0:8@?<v@?@\"NSNumber\"q>16"
+ "v24@0:8@?<v@?@\"NSObject<OS_xpc_object>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSPersonNameComponents\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSPersonNameComponents\"@\"NSString\"@\"NSString\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSPersonNameComponents\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSSet\"@\"MRGroupSessionInfo\">16"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSSecurityScopedURLWrapper\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSString\"q@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSUUID\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"OSLogEntry\">16"
+ "v24@0:8@?<v@?@\"PKPaymentOfferCatalog\">16"
+ "v24@0:8@?<v@?@\"PKPaymentOfferCatalog\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"PKTrustedDeviceEnrollmentInfo\"@\"PKTrustedDeviceEnrollmentInfo\">16"
+ "v24@0:8@?<v@?@\"PLCPLSettings\">16"
+ "v24@0:8@?<v@?@\"RTPeopleDensity\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SDDevice\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SFAutoUnlockNotificationModel\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SMCurrentWorkoutSnapshot\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SMLocalSessionState\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SPPublishResult\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"STCommunicationConfiguration\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"STIDSTransportPrimitiveDestinationReachabilityMap\">16"
+ "v24@0:8@?<v@?@\"STScreenTimeConfiguration\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SUAutoInstallForecast\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SUCoreDDMDeclaration\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SUCoreDDMDeclarationGlobalSettings\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"SUIAutomationServiceError\">16"
+ "v24@0:8@?<v@?@\"SUScanResults\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"TUNearbyDeviceHandle\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"WFWorkflowDescriptor\"@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"WiFiAwareDeviceCapabilities\">16"
+ "v24@0:8@?<v@?@\"_LTLocaleModalities\">16"
+ "v24@0:8@?<v@?@\"_OSInactivityPredictorMetadata\">16"
+ "v24@0:8@?<v@?@\"_OSInactivityPredictorOutput\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"_TtC12ModelCatalog28SiriResourceAvailabilityInfo\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">16"
+ "v24@0:8@?<v@?@\"_TtC9SEService16DeviceCapability\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"_TtC9SEService16ReservationState\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"CDPLocalSecret\">16"
+ "v24@0:8@?<v@?B@\"NSError\"@\"NSDictionary\">16"
+ "v24@0:8@?<v@?B@\"SURollbackDescriptor\"@\"NSError\">16"
+ "v24@0:8@?<v@?BB@\"NSError\"@\"NSError\">16"
+ "v24@0:8@?<v@?BB@\"NSString\"@\"NSError\">16"
+ "v24@0:8@?<v@?B^@>16"
+ "v24@0:8@?<v@?BqB>16"
+ "v24@0:8@?<v@?Bqq@\"SOSButtonPressState\">16"
+ "v24@0:8@?<v@?II>16"
+ "v24@0:8@?<v@?q@\"NSUUID\">16"
+ "v24@0:8@?<v@?{?=III{?=C{?=I[32C]}}}@\"NSError\">16"
+ "v24@0:8f16B20"
+ "v24@0:8i16C20"
+ "v24@?0@\"<AMSFraudReportServiceInterface><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v24@?0@\"<ASDUpdatesServiceProtocol><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v24@?0@\"<CKXPCContainerScopedDaemon>\"8@\"NSError\"16"
+ "v24@?0@\"<FPIndexingAssertion>\"8@\"NSError\"16"
+ "v24@?0@\"<GCAdaptiveTriggersXPCProxyServiceRemoteServerInterface>\"8@\"NSError\"16"
+ "v24@?0@\"<GCGameIntentXPCProxyServiceRemoteServerInterface>\"8@\"NSError\"16"
+ "v24@?0@\"<_TtP19PrivateCloudCompute28TC2XPCTrustedRequestProtocol_>\"8@\"NSData\"16"
+ "v24@?0@\"AKAttestationData\"8@\"NSError\"16"
+ "v24@?0@\"AKDeviceListResponse\"8@\"NSError\"16"
+ "v24@?0@\"AKTrustedContactsSyncResult\"8@\"NSError\"16"
+ "v24@?0@\"AMSFraudReportResponse\"8@\"NSError\"16"
+ "v24@?0@\"APClientState\"8@\"NSError\"16"
+ "v24@?0@\"APPerAppManagedProtectability\"8@\"NSError\"16"
+ "v24@?0@\"ATXFaceGalleryConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"ATXSettingsActionsClientResponse\"8@\"NSError\"16"
+ "v24@?0@\"ATXSportsResponse\"8@\"NSError\"16"
+ "v24@?0@\"BCSBusinessLogo\"8@\"NSError\"16"
+ "v24@?0@\"CBControllerInfo\"8@\"NSError\"16"
+ "v24@?0@\"CDPCombinedWalrusStatus\"8@\"NSError\"16"
+ "v24@?0@\"CERuleConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"CEServerRecommendations\"8@\"NSError\"16"
+ "v24@?0@\"CGBitmapFormat\"8@\"NSData\"16"
+ "v24@?0@\"CHSynthesisStyleInventoryStatus\"8@\"NSError\"16"
+ "v24@?0@\"CLLocation\"8@\"NSError\"16"
+ "v24@?0@\"CTActivationPolicyState\"8@\"NSError\"16"
+ "v24@?0@\"CTPrivateNetworkCapabilities\"8@\"NSError\"16"
+ "v24@?0@\"CTPrivateNetworkSimInfo\"8@\"NSError\"16"
+ "v24@?0@\"CTSatelliteMessagingProvisioning\"8@\"NSError\"16"
+ "v24@?0@\"CTTrafficDescriptorsContainer\"8@\"NSError\"16"
+ "v24@?0@\"CTTransportKeysUpdate\"8@\"NSError\"16"
+ "v24@?0@\"CTXPCResponseMessage\"8@\"NSError\"16"
+ "v24@?0@\"CloudFeature\"8@\"NSError\"16"
+ "v24@?0@\"DCCredentialCryptoKey\"8@\"NSError\"16"
+ "v24@?0@\"DCCredentialProperties\"8@\"NSError\"16"
+ "v24@?0@\"DIDeviceHandle\"8@\"NSError\"16"
+ "v24@?0@\"DUPersonalIDResult\"8@\"NSError\"16"
+ "v24@?0@\"FHFeaturesResponse\"8@\"NSError\"16"
+ "v24@?0@\"FMDActivationLockInfo\"8@\"NSError\"16"
+ "v24@?0@\"GDEntityResolutionResult\"8@\"NSError\"16"
+ "v24@?0@\"GDKnosisResult\"8@\"NSError\"16"
+ "v24@?0@\"HAHDPinnedContentState\"8@\"NSError\"16"
+ "v24@?0@\"HKDatabaseAccessibilityAssertion\"8@\"NSError\"16"
+ "v24@?0@\"HKFeatureAvailabilityOnboardingEligibility\"8@\"NSError\"16"
+ "v24@?0@\"HKFeatureAvailabilityRequirementSet\"8@\"NSError\"16"
+ "v24@?0@\"HKFeatureOnboardingRecord\"8@\"NSError\"16"
+ "v24@?0@\"HKMobilityWalkingSteadinessNotificationStatus\"8@\"NSError\"16"
+ "v24@?0@\"HKMobilityWalkingSteadinessOnboardingStatus\"8@\"NSError\"16"
+ "v24@?0@\"HKQuantity\"8@\"NSError\"16"
+ "v24@?0@\"HKRegionAvailability\"8@\"NSError\"16"
+ "v24@?0@\"HKSPSleepScheduleModel\"8@\"NSError\"16"
+ "v24@?0@\"IDSPinnedIdentity\"8@\"NSError\"16"
+ "v24@?0@\"INAppIntent\"8@\"NSError\"16"
+ "v24@?0@\"INIntent\"8@\"NSError\"16"
+ "v24@?0@\"KTOptInState\"8@\"NSError\"16"
+ "v24@?0@\"LACDTORatchetState\"8@\"NSError\"16"
+ "v24@?0@\"LACEnvironmentState\"8@\"NSError\"16"
+ "v24@?0@\"LNAction\"8@\"NSError\"16"
+ "v24@?0@\"LNActionMetadata\"8@\"NSError\"16"
+ "v24@?0@\"LNDynamicOption\"8@\"NSError\"16"
+ "v24@?0@\"LNDynamicOptionsResult\"8@\"NSError\"16"
+ "v24@?0@\"LNEntityMetadata\"8@\"NSError\"16"
+ "v24@?0@\"LNEnumMetadata\"8@\"NSError\"16"
+ "v24@?0@\"LNQueryOutput\"8@\"NSError\"16"
+ "v24@?0@\"LNSuccessResult\"8@\"NSError\"16"
+ "v24@?0@\"LPLinkMetadata\"8@\"NSError\"16"
+ "v24@?0@\"MCResourceStatus\"8@\"NSError\"16"
+ "v24@?0@\"MLRTaskResult\"8@\"NSError\"16"
+ "v24@?0@\"NFAssertionInternal\"8@\"NSError\"16"
+ "v24@?0@\"NFTrustPaymentSignResponse\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"WBSPasskeyAutoFillFromNearbyDeviceOptions\"16"
+ "v24@?0@\"NSArray\"8q16"
+ "v24@?0@\"NSData\"8@\"NSData\"16"
+ "v24@?0@\"NSDateComponents\"8@\"NSError\"16"
+ "v24@?0@\"NSError\"8@\"AUParameterTree\"16"
+ "v24@?0@\"NSError\"8@\"NSDate\"16"
+ "v24@?0@\"NSError\"8@\"NSXPCListenerEndpoint\"16"
+ "v24@?0@\"NSSet\"8@\"MRGroupSessionInfo\"16"
+ "v24@?0@\"ODDSiriSchemaODDSiriClientEvent\"8@\"NSError\"16"
+ "v24@?0@\"OTCurrentSecureElementIdentities\"8@\"NSError\"16"
+ "v24@?0@\"PBSaveResponse\"8@\"NSError\"16"
+ "v24@?0@\"PFPosterPathsAssertion\"8@\"NSError\"16"
+ "v24@?0@\"PKPaymentOfferCatalog\"8@\"NSError\"16"
+ "v24@?0@\"PPSocialAttribution\"8@\"NSError\"16"
+ "v24@?0@\"PRUISAnalysisServiceResponse\"8@\"NSError\"16"
+ "v24@?0@\"QLThumbnailReply\"8@\"NSError\"16"
+ "v24@?0@\"RMSubscriberStore\"8@\"NSError\"16"
+ "v24@?0@\"RTAuthorizedLocationStatus\"8@\"NSError\"16"
+ "v24@?0@\"RTPeopleDensity\"8@\"NSError\"16"
+ "v24@?0@\"SDBetaProgram\"8@\"NSError\"16"
+ "v24@?0@\"SDDevice\"8@\"NSError\"16"
+ "v24@?0@\"SKHandleInvitability\"8@\"NSError\"16"
+ "v24@?0@\"SKStatusSubscriptionMetadata\"8@\"NSError\"16"
+ "v24@?0@\"SOAuthorizationCredentialCore\"8@\"NSError\"16"
+ "v24@?0@\"SPLocationFetchResult\"8@\"NSError\"16"
+ "v24@?0@\"SPSecureLocation\"8@\"NSError\"16"
+ "v24@?0@\"SPSecureLocationsStewiePublishResult\"8@\"NSError\"16"
+ "v24@?0@\"SPSecureLocationsSubscriptionResult\"8@\"NSError\"16"
+ "v24@?0@\"SUCoreDDMDeclaration\"8@\"NSError\"16"
+ "v24@?0@\"SUCoreDDMDeclarationGlobalSettings\"8@\"NSError\"16"
+ "v24@?0@\"SURollbackDescriptor\"8@\"NSError\"16"
+ "v24@?0@\"SUScanResults\"8@\"NSError\"16"
+ "v24@?0@\"SWTransparencyExpiringVerificationResult\"8@\"NSError\"16"
+ "v24@?0@\"SiriTTSSynthesisVoice\"8@\"NSError\"16"
+ "v24@?0@\"TCSmartRepliesResponse\"8@\"NSError\"16"
+ "v24@?0@\"TCTextCompositionOutput\"8@\"NSError\"16"
+ "v24@?0@\"TCTextCompositionReviewOutput\"8@\"NSError\"16"
+ "v24@?0@\"THThreadNetworkCredentialsActiveDataSetRecord\"8@\"NSError\"16"
+ "v24@?0@\"TUNearbyDeviceHandle\"8@\"NSError\"16"
+ "v24@?0@\"TrustedPeersHelperCustodianRecoveryKey\"8@\"NSError\"16"
+ "v24@?0@\"TrustedPeersHelperHealthCheckResult\"8@\"NSError\"16"
+ "v24@?0@\"UAFAssetStatus\"8@\"NSError\"16"
+ "v24@?0@\"UISSlotRemoteContent\"8@\"NSError\"16"
+ "v24@?0@\"VMVoicemailGreeting\"8@\"NSError\"16"
+ "v24@?0@\"WFWorkflowRunResult\"8@\"NSError\"16"
+ "v24@?0@\"WiFi3BarsResponse\"8@\"NSError\"16"
+ "v24@?0@\"_EXQueryResult\"8@\"NSError\"16"
+ "v24@?0@\"_EXSceneSessionConnectionResponse\"8@\"NSError\"16"
+ "v24@?0@\"_OSChargingPredictorOutput\"8@\"NSError\"16"
+ "v24@?0@\"_TtC12ModelCatalog17ResourceContainer\"8@\"NSError\"16"
+ "v24@?0@\"_TtC12ModelCatalog23ResourceBundleContainer\"8@\"NSError\"16"
+ "v24@?0@\"_TtC12ModelCatalog28SiriResourceAvailabilityInfo\"8@\"NSError\"16"
+ "v24@?0@\"_TtC13SiriAnalytics13StagingReport\"8@\"NSError\"16"
+ "v24@?0@\"_TtC14CopresenceCore29PresenceSessionConnectionInfo\"8@\"NSError\"16"
+ "v24@?0@\"_TtC19EnergyKitFoundation12EKEnergySite\"8@\"NSError\"16"
+ "v24@?0@\"_TtC4Sage22SummarizationXPCResult\"8@\"NSError\"16"
+ "v24@?0@\"_TtC9SEService16DeviceCapability\"8@\"NSError\"16"
+ "v24@?0@\"_TtC9SEService16ReservationState\"8@\"NSError\"16"
+ "v24@?0B8I12B16I20"
+ "v24@?0B8q12B20"
+ "v264@0:8{IGRequestQueueLoggerEvent=qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqB}16"
+ "v264@0:8{WorkoutEvent=ddqd{CLWorkoutSessionDetails=idqQ}{WorkoutSettings=[16C][16C][16C]qq(WorkoutAttrib={SwimAttrib=qd}Q){FitnessPlusInfo=B[64c]q}Q}}16@?248@?256"
+ "v28@0:8@\"<HKFeatureAvailabilityRequirement>\"16B24"
+ "v28@0:8@\"ATXInfoSuggestion\"16B24"
+ "v28@0:8@\"CTServiceDescriptor\"16B24"
+ "v28@0:8@\"CTTetheringStatus\"16i24"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
+ "v28@0:8@\"GCDeviceAdaptiveTriggersPayload\"16i24"
+ "v28@0:8@\"RPRemoteDisplayPerson\"16B24"
+ "v28@0:8@\"SUDescriptor\"16B24"
+ "v28@0:8@\"SUDownload\"16B24"
+ "v28@0:8@?16B24"
+ "v28@0:8@?<v@?@\"CTTetheringStatus\"@\"NSError\">16i24"
+ "v28@0:8B16@\"NSArray\"20"
+ "v28@0:8B16@\"NSUUID\"20"
+ "v28@0:8B16@?<v@?@\"<FPIndexingAssertion>\"@\"NSError\">20"
+ "v28@0:8B16@?<v@?@\"HKSharedSummaryTransaction\"@\"NSError\">20"
+ "v28@0:8B16@?<v@?@\"NSDictionary\">20"
+ "v28@0:8B16@?<v@?@\"NSSet\"@\"NSError\">20"
+ "v28@0:8B16@?<v@?@\"NSString\">20"
+ "v28@0:8B16@?<v@?@\"PKPaymentWebServiceContext\">20"
+ "v28@0:8B16@?<v@?@\"PKPeerPaymentWebServiceContext\">20"
+ "v28@0:8B16@?<v@?@\"PRChipInfo\">20"
+ "v28@0:8B16@?<v@?@\"SUScanResults\"@\"NSError\">20"
+ "v28@0:8B16@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">20"
+ "v28@0:8B16@?<v@?i@\"CADObjectID\">20"
+ "v28@0:8B16@?<v@?q>20"
+ "v28@0:8C16@?20"
+ "v28@0:8C16@?<v@?@\"NSArray\"@\"NSError\">20"
+ "v28@0:8I16@\"NSUUID\"20"
+ "v28@0:8I16q20"
+ "v28@0:8f16@?<v@?@\"NSError\">20"
+ "v28@0:8f16@?<v@?ff>20"
+ "v28@0:8i16@\"NSError\"20"
+ "v28@0:8i16@?<v@?i@\"NSString\">20"
+ "v28@0:8i16@?<v@?{CGRect={CGPoint=dd}{CGSize=dd}}>20"
+ "v28@0:8{OverrideClient=CBBBBBBB}16B24"
+ "v28@?0@\"<CNEncodedFetchResponse>\"8B16@\"NSError\"20"
+ "v28@?0@\"CLLocation\"8B16@\"NSData\"20"
+ "v28@?0@\"NSObject<NFSessionInterface><NSXPCProxyCreating>\"8B16@\"NSError\"20"
+ "v28@?0@\"SMSessionManagerState\"8B16@\"NSError\"20"
+ "v28@?0B8@\"INIntent\"12@\"NSDictionary\"20"
+ "v28@?0B8@\"NSArray\"12@\"NSError\"20"
+ "v28@?0B8@\"SURollbackDescriptor\"12@\"NSError\"20"
+ "v28@?0B8^{ScalarArgsArray=[16Q]I}12@\"NSError\"20"
+ "v28@?0Q8I16@\"NSError\"20"
+ "v32@0:8@\"<ASCAppOfferStateDelegate>\"16@?<v@?@\"<ASCAppOfferStateService>\"@\"NSError\">24"
+ "v32@0:8@\"<ASCOffer>\"16@\"NSString\"24"
+ "v32@0:8@\"<BDSSecureEngagementData>\"16@?<v@?BB@\"NSError\">24"
+ "v32@0:8@\"<BRItemNotificationReceiving>\"16@?<v@?@\"<BRItemNotificationSending><NSXPCProxyCreating>\"@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"<EMDiagnosticInfoProvidingXPC>\"16@?<v@?@\"<EFCancelable>\">24"
+ "v32@0:8@\"<FPProgressProtocol>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"<GCAdaptiveTriggersXPCProxyRemoteClientEndpointInterface>\"16@?<v@?@\"<GCAdaptiveTriggersXPCProxyRemoteServerEndpointInterface>\"@\"NSError\">24"
+ "v32@0:8@\"<GCAdaptiveTriggersXPCProxyServiceRemoteClientInterface>\"16@?<v@?@\"<GCAdaptiveTriggersXPCProxyServiceRemoteServerInterface>\"@\"NSError\">24"
+ "v32@0:8@\"<GCGameIntentXPCProxyRemoteClientEndpointInterface>\"16@?<v@?@\"<GCGameIntentXPCProxyRemoteServerEndpointInterface>\"@\"NSError\">24"
+ "v32@0:8@\"<GCGameIntentXPCProxyServiceRemoteClientInterface>\"16@?<v@?@\"<GCGameIntentXPCProxyServiceRemoteServerInterface>\"@\"NSError\">24"
+ "v32@0:8@\"<MNNavigationServiceProxy>\"16@\"MNTransitAlert\"24"
+ "v32@0:8@\"<NSObject>\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"<SFAuthenticationStateChangesObserverProtocol>\"16@\"NSUUID\"24"
+ "v32@0:8@\"<SFUnlockClientProtocol>\"16Q24"
+ "v32@0:8@\"<SRRequestRecording>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"<WBSHistoryExporterProtocol>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AAAudioSessionControl\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AACloudServicesClient\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AADeviceManager\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AAProxCardsInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ACAccount\"16@?<v@?@\"AALoginAccountResponse\"@\"NSError\">24"
+ "v32@0:8@\"AFBulletin\"16@?<v@?Q>24"
+ "v32@0:8@\"AFSiriResponse\"16Q24"
+ "v32@0:8@\"AKAttestationRequestData\"16@?<v@?@\"AKAttestationData\"@\"NSError\">24"
+ "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"AKCustodianSetupResult\"@\"NSError\">24"
+ "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"AKTrustedContactsSyncResult\"@\"NSError\">24"
+ "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"AKCustodianContext\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"AKInheritanceContext\"16@?<v@?@\"AKBeneficiaryManifest\"@\"NSError\">24"
+ "v32@0:8@\"AKInheritanceContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AKSignInWithAppleRequestContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"AKSignInWithAppleRequestContext\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"AMSAccountIdentity\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"AMSBiometricsSignatureRequest\"16@?<v@?@\"AMSBiometricsSignatureResult\"@\"NSError\">24"
+ "v32@0:8@\"AMSFraudReportOptions\"16@?<v@?@\"AMSFraudReportResponse\"@\"NSError\">24"
+ "v32@0:8@\"ANAnnouncementContext\"16@\"NSString\"24"
+ "v32@0:8@\"ASCAdamID\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ASCCollectionRequest\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"ASCCredentialRequestContext\"16@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">24"
+ "v32@0:8@\"ASCLockupBatchRequest\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"ASCLockupRequest\"16@?<v@?@\"ASCLockup\"@\"NSError\">24"
+ "v32@0:8@\"ASCSignpostPredicate\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ASDAlertPresentationRequest\"16@?<v@?@\"ASDAlertPresentationResult\"@\"NSError\">24"
+ "v32@0:8@\"ASDImpressionParamsConfig\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ASPasswordCredential\"16@\"ASCredentialServiceIdentifier\"24"
+ "v32@0:8@\"ATXFaceGalleryItem\"16@?<v@?@\"ATXComplicationSet\"@\"NSError\">24"
+ "v32@0:8@\"ATXFaceGalleryItem\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"ATXFaceGalleryItem\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"ATXFaceSuggestionFocusMode\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"ATXMailContextRequest\"16@?<v@?@\"ATXMailContextResponse\"@\"NSError\">24"
+ "v32@0:8@\"ATXMessageContextRequest\"16@?<v@?@\"ATXMessageContextResponse\"@\"NSError\">24"
+ "v32@0:8@\"ATXNotificationContextRequest\"16@?<v@?@\"ATXNotificationContextResponse\"@\"NSError\">24"
+ "v32@0:8@\"ATXNotificationRankingRequest\"16@?<v@?@\"ATXNotificationRankingResult\"@\"NSError\">24"
+ "v32@0:8@\"ATXPosterEdit\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ATXPosterSwitch\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ATXProactiveSuggestion\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ATXSettingsActionsClientRequest\"16@?<v@?@\"ATXSettingsActionsClientResponse\"@\"NSError\">24"
+ "v32@0:8@\"ATXSuggestionRequest\"16@?<v@?@\"<ATXUICacheProtocol>\">24"
+ "v32@0:8@\"ATXUserNotification\"16@?<v@?@\"ATXNotificationCategorizationFeatureCollectionSet\"@\"NSError\">24"
+ "v32@0:8@\"ATXUserNotification\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"AUAudioUnitPreset\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AUAudioUnitPreset\"16@?<v@?@\"NSError\"@\"NSDictionary\">24"
+ "v32@0:8@\"AUAudioUnitViewConfiguration\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AVSpeechSynthesisProviderRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AWDLServiceDiscoveryConfiguration\"16@?<v@?q>24"
+ "v32@0:8@\"BDSDistributedPriceTrackingConfig\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"BMResourceSpecifier\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"CADDatabaseInitializationOptions\"16@?<v@?ii>24"
+ "v32@0:8@\"CADObjectID\"16@?<v@?i@\"NSArray\"@\"NSArray\">24"
+ "v32@0:8@\"CARConnectionEvent\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"CCSIconElementRequest\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"CCSIconElementRequest\"16@?<v@?Q@\"NSError\">24"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"AKInheritanceAccessKey\"@\"NSError\">24"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"CDPContext\"16@?<v@?BB@\"NSError\">24"
+ "v32@0:8@\"CDPCustodianRecoveryInfo\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"CHRemoteInventoryRequest\"16@?<v@?@\"CHSynthesisStyleInventoryStatus\"@\"NSError\">24"
+ "v32@0:8@\"CHRemoteLineWrappingRequest\"16@?<v@?@\"CHLineWrappingResult\"@\"NSError\">24"
+ "v32@0:8@\"CHRemoteRecognitionRequest\"16@?<v@?@\"CHTokenizedResult\"@\"NSError\">24"
+ "v32@0:8@\"CHRemoteRecognitionSketchRequest\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"CHRemoteSynthesisRequest\"16@?<v@?@\"CHSynthesisResult\"@\"NSError\">24"
+ "v32@0:8@\"CHSTimelineReloadRequest\"16^@24"
+ "v32@0:8@\"CHSWidgetExtensionProviderOptions\"16@?<v@?@\"CHSWidgetExtensionsBox\"@\"BSAction\"@\"NSError\">24"
+ "v32@0:8@\"CKAcceptSharesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKAggregateZonePCSOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKArchiveRecordsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKCheckSupportedDeviceCapabilitiesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKCodeFunctionInvokeOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKCompleteParticipantVettingOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKDatabaseOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKDeclineSharesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKDeserializeRecordModificationsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKDiscoverUserIdentitiesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchArchivedRecordsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchDatabaseChangesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchMergeableDeltaMetadataOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchMergeableDeltasOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchRecordVersionsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchRecordZoneChangesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchRecordZonesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchRecordsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchShareMetadataOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchShareParticipantKeyOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchShareParticipantsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchSubscriptionsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKFetchWebAuthTokenOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKInitiateParticipantVettingOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKMapShareURLsToInstalledBundleIDsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKMarkAssetBrokenOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKMergeableDelta\"16@?<v@?S>24"
+ "v32@0:8@\"CKModifyRecordAccessOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKModifyRecordZonesOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKModifyRecordsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKModifySubscriptionsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKModifyWebSharingOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKMovePhotosOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKPublishAssetsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKQueryOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKRecordID\"16q24"
+ "v32@0:8@\"CKRepairAssetsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKReplaceMergeableDeltasOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKSerializeRecordModificationsOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKShare\"16@?<v@?@\"CKShare\"@\"NSError\">24"
+ "v32@0:8@\"CKShareAccessRequestOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CKUploadMergeableDeltasOperationInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CNContact\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"CPBackgroundSessionCreationRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CPPresenceSessionCreationRequest\"16@?<v@?@\"_TtC14CopresenceCore29PresenceSessionConnectionInfo\"@\"NSError\">24"
+ "v32@0:8@\"CSAttendingOptions\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"CTDataUsagePoliciesWrapper\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CTDedicatedBearerRequest\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"CTGeofenceProfile\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CTSatelliteMessagingProvisioningReceipt\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTPlmnInfo\"24"
+ "v32@0:8@\"CTXPCRequestMessage\"16@?<v@?@\"CTXPCResponseMessage\"@\"NSError\">24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestinationUpdate\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliMessageDispositionStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliMessageID\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliOperationResult\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliSystemConfiguration\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSimDeactivationInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@?<v@?@\"CTPrivateNetworkSimInfo\"@\"NSError\">24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@?<v@?Q@\"NSError\">24"
+ "v32@0:8@\"CWFRequestParameters\"16@?<v@?@\"NSError\"@\"CWFBackgroundScanConfiguration\">24"
+ "v32@0:8@\"Core_Audio_XPC_Raw_Transporter\"16@?<v@?i>24"
+ "v32@0:8@\"DCCredentialAuthorizationToken\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"DDScannerResult\"16@\"NSDictionary\"24"
+ "v32@0:8@\"DIAttachParams\"16@?<v@?@\"DIDeviceHandle\"@\"NSError\">24"
+ "v32@0:8@\"DIAttachParams\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"DIConvertParams\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"DIDeviceHandle\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"DIEncryptionFrontend\"16@?<v@?@\"DIEncryptionFrontend\"@\"NSError\">24"
+ "v32@0:8@\"DIEncryptionUnlocker\"16@?<v@?@\"DIEncryptionUnlocker\"@\"NSError\">24"
+ "v32@0:8@\"DIStatsParams\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"DIUserDataParams\"16@?<v@?@\"DIUserDataParams\"@\"NSError\">24"
+ "v32@0:8@\"DIUserDataParams\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"DIVerifyParams\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"DNDRequestDetails\"16@?<v@?@\"NSArray<__DNDModeConfiguration__>\"@\"NSError\">24"
+ "v32@0:8@\"DNDRequestDetails\"16@?<v@?@\"NSArray<__DNDMode__>\"@\"NSError\">24"
+ "v32@0:8@\"DNDRequestDetails\"16@?<v@?@\"NSNumber\"@\"DNDModeAssertion\"@\"NSError\">24"
+ "v32@0:8@\"DNDRequestDetails\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"DNDRequestDetails\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"DiagnosticDevice\"16@?<v@?@\"DiagnosticDevice\">24"
+ "v32@0:8@\"EMMailboxObjectID\"16@?<v@?q>24"
+ "v32@0:8@\"EMQuery\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FBSSceneIdentityToken\"16@\"MOSuggestionSheetOptions\"24"
+ "v32@0:8@\"FHTransaction\"16@?<v@?@\"PKPaymentTransaction\">24"
+ "v32@0:8@\"FMDLocalFindableAccessory\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FMDSecureLocationContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FPItemID\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"FPItemID\"16@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"<DOCServiceTransitionProtocol>\">24"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"DOCAnimatableInfo\">24"
+ "v32@0:8@\"GDEntityResolutionRequest\"16@?<v@?@\"GDEntityResolutionCollectionResult\"@\"NSError\">24"
+ "v32@0:8@\"GDEntityResolutionRequest\"16@?<v@?@\"GDEntityResolutionResult\"@\"NSError\">24"
+ "v32@0:8@\"GDKnosisRequest\"16@?<v@?@\"GDKnosisResult\"@\"NSError\">24"
+ "v32@0:8@\"GEOLogMsgEventPeriodicSettingsSummary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"HKCharacteristicType\"16@?<v@?@\"NSDate\"@\"NSError\">24"
+ "v32@0:8@\"HKClinicalProviderSearchQueryDescription\"16@?<v@?@\"HKClinicalProviderSearchResultsPage\"@\"NSError\">24"
+ "v32@0:8@\"HKConceptIdentifier\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"HKDataCollectorState\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HKMCPregnancyModeSetupCompletionRecord\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HKMCPregnancyModel\"16@\"NSUUID\"24"
+ "v32@0:8@\"HKMHValenceSummary\"16@\"NSUUID\"24"
+ "v32@0:8@\"HKProfileIdentifier\"16@?<v@?@\"NSDate\"@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"HKRecalibrateEstimatesRequestRecord\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HKSignedClinicalDataRecord\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HKSignedClinicalDataRecord\"16@?<v@?Bq@\"NSError\">24"
+ "v32@0:8@\"HKSignedClinicalDataSource\"16@?<v@?@\"HKSignedClinicalDataParsingResult\"@\"NSError\">24"
+ "v32@0:8@\"HKWorkoutCluster\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"HMDeviceCloudRecordInfo\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"HMServiceClient\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"IDSOffGridEncryptedMessage\"16@?<v@?>24"
+ "v32@0:8@\"IDSOffGridEncryptedMessage\"16@?<v@?@\"IDSOffGridMessage\"@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"IDSOffGridMessage\"16@?<v@?@\"IDSOffGridEncryptedMessage\"@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"IDSOffGridSummaryMessage\"16@?<v@?>24"
+ "v32@0:8@\"IDSReportClientEvent\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"IDSURI\"16@?<v@?B>24"
+ "v32@0:8@\"IMServiceReachabilityRequest\"16@\"<IMServiceReachabilityResponseHandler>\"24"
+ "v32@0:8@\"IMServiceReachabilityRequest\"16@\"IMServiceReachabilityResult\"24"
+ "v32@0:8@\"INIntent\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"INIntent\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"INIntent\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"IREvent\"16@\"IRCandidate\"24"
+ "v32@0:8@\"ISGenerationRequest\"16@?<v@?@\"ISGenerationResponse\">24"
+ "v32@0:8@\"LAContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"LNAsyncIteratorReference\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"LNAsyncSequenceReference\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"LNConfigurableQueryRequest\"16@?<v@?@\"LNQueryOutput\"@\"NSError\">24"
+ "v32@0:8@\"LNConnectionContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"LNEntity\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"LNOpenURLRequest\"16@?<v@?@\"LNOpenURLResponse\"@\"NSError\">24"
+ "v32@0:8@\"LNStaticDeferredLocalizedString\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"LNTranscriptActionRecord\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"LNTranscriptMatchingPredicate\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"MCCCategoryContext\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"MCCSecretAgentContext\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSSet\"@\"NSError\">24"
+ "v32@0:8@\"MLRTask\"16@?<v@?@\"MLRTaskResult\"@\"NSError\">24"
+ "v32@0:8@\"MOContextFeedback\"16@?<v@?Q@\"NSError\">24"
+ "v32@0:8@\"MOContextFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"MOXPCContext\"16@\"<MODatabaseUpgradeCompletionDelegateProtocol>\"24"
+ "v32@0:8@\"MOXPCContext\"16@?<v@?@\"NSDateComponents\"@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"MOXPCContext\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"ManageSubscriptionsRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NDDownloadRequest\"16@\"FCContentArchive\"24"
+ "v32@0:8@\"NDDownloadRequest\"16@\"NSError\"24"
+ "v32@0:8@\"NDDownloadRequest\"16d24"
+ "v32@0:8@\"NEConfiguration\"16@?<v@?B@\"NSArray\">24"
+ "v32@0:8@\"NEVirtualInterfaceParameters\"16@?<v@?@\"NEVirtualInterfaceParameters\">24"
+ "v32@0:8@\"NIAcwgM1Msg\"16q24"
+ "v32@0:8@\"NIAcwgM2Msg\"16@\"NSError\"24"
+ "v32@0:8@\"NIAcwgM4Msg\"16@\"NSError\"24"
+ "v32@0:8@\"NIAcwgRangingSessionResumeResponseMsg\"16@\"NSError\"24"
+ "v32@0:8@\"NIConfiguration\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NIDiscoveryToken\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@\"AVSpeechSynthesisProviderRequest\"24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"CKContextResponse\"@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\"@\"NSIndexSet\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSMutableDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?Bqq@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?Q@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?q>24"
+ "v32@0:8@\"NSArray<__NSNumber__>\"16@\"NSNumber\"24"
+ "v32@0:8@\"NSData\"16@\"NINearbyObject\"24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"<CGRemotePDFDocumentProtocol>\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"FPSandboxingURLWrapper\"@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"_TtC10FinanceKit13StorableColor\"@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?Q>24"
+ "v32@0:8@\"NSData\"16@?<v@?i>24"
+ "v32@0:8@\"NSDate\"16@?<v@?B>24"
+ "v32@0:8@\"NSDictionary\"16@\"NSURL\"24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"FACircleStateResponse\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"W5DiagnosticsMode\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSData\"@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16Q24"
+ "v32@0:8@\"NSFileProviderDomain\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@\"MOSuggestion\"24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"CNApplicationProxy\"@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"CNLimitedAccessSyncData\"@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"LACEnvironmentState\"@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\"@\"NSData\">24"
+ "v32@0:8@\"NSNumber\"16o^@24"
+ "v32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSPredicate\"16@\"NSString\"24"
+ "v32@0:8@\"NSPredicate\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?i>24"
+ "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?ii>24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"CTDataUsagePoliciesWrapper\"@\"NSError\">24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"<IDSXPCBAASigner>\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"AAProxCardsInfo\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"BDSMutableSecureEngagementData\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"CNApplicationProxy\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"DCCredentialCryptoKey\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"DCCredentialProperties\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ExternalPurchaseLinkResponse\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"FSModuleIdentity\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"GDMentionGenerationResult\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HAHDPinnedContentState\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HKDatabaseAccessibilityAssertion\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HKFeatureAvailabilityOnboardingEligibility\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HKSignedClinicalDataRegistryPublicKeyFetchResult\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"HMDeviceCloudRecordInfo\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"LNConnectionListenerEndpoint\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"LPLinkMetadata\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MCCSigningAndEncryptionMessagesStatus\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MCResourceInformation\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MCResourceStatus\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"@\"NSXPCListenerEndpoint\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"@>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"C>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\"@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSObject\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"B>24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSString\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKAccountDailyCashDestinationsSummary\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKAccountEnhancedMerchantBehavior\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKAccountPromotionBehavior\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKAppleBalanceInStoreTopUpToken\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKAppleBalancePromotionConfiguration\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKExpressPassConfiguration\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKPayLaterCardMagnitudes\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKPayLaterFinancingPlan\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKPaymentPass\"@\"PKPaymentTransaction\"@\"NSString\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKPaymentRewardsBalance\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKPaymentRewardsRedemption\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKPeerPaymentCounterpartImageData\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKSharedAccountCloudStore\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PKSharedAccountCloudStore\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"PPSocialAttribution\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"RMDeclarationManifest\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"RMObserverStore\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"RMProviderStore\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"RMSubscriberStore\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"SKStatusSubscriptionMetadata\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"SOAuthorizationCredential\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"STCallingStatusDomainCallDescriptor\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"TRIClientNamespaceMetadata\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"WFWorkflowCollection\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"WFWorkflowReference\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"WiFi3BarsResponse\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC12ModelCatalog17ResourceContainer\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC12ModelCatalog23ResourceBundleContainer\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC25CloudSubscriptionFeatures12TicketStatus\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC25CloudSubscriptionFeatures14WaitlistResult\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC25CloudSubscriptionFeatures6Ticket\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?BB>24"
+ "v32@0:8@\"NSString\"16@?<v@?Bq>24"
+ "v32@0:8@\"NSString\"16@?<v@?i@\"NSData\">24"
+ "v32@0:8@\"NSString\"16@?<v@?q@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16o^@24"
+ "v32@0:8@\"NSURL\"16@\"DOCItemBookmark\"24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"ASDBetaAppDisplayNames\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"ASDBetaAppFeedbackMetadata\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"ASDBetaAppLaunchInfo\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSData\"@\"NSDate\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSDate\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSURL\"@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"PLPhotoLibraryIdentifier\"@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@\"NSSet\"24"
+ "v32@0:8@\"NSUUID\"16@\"SFAuthenticationApproveInfo\"24"
+ "v32@0:8@\"NSUUID\"16@\"SPPeripheralConnectionMaterial\"24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"HKWorkoutCluster\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\"@\"CLLocation\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\"@\"NSDictionary\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSURL\"@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"FSTaskDescription\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"SPPeripheralConnectionMaterial\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"_TtC9SEService11Reservation\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?Q>24"
+ "v32@0:8@\"NSUUID\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?i>24"
+ "v32@0:8@\"NTKArgonKeyDescriptor\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NTKFaceInstanceDescriptor\"16@\"NSUUID\"24"
+ "v32@0:8@\"PARSmartSearchV1Parameters\"16@\"PARSmartSearchV2Parameters\"24"
+ "v32@0:8@\"PBCodable\"16Q24"
+ "v32@0:8@\"PCLockscreenControlsObserver\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"PCMediaTransferObserver\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"PCRemoteActivityClient\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"PHPickerConfiguration\"16@?<v@?B>24"
+ "v32@0:8@\"PKAccount\"16@?<v@?B>24"
+ "v32@0:8@\"PKAppleBalanceInStoreTopUpToken\"16@\"NSString\"24"
+ "v32@0:8@\"PKAppleBalancePromotionConfiguration\"16@\"NSString\"24"
+ "v32@0:8@\"PKDeviceSharingCapabilities\"16@\"NSString\"24"
+ "v32@0:8@\"PKExpressPassConfiguration\"16@?<v@?@\"NSSet\">24"
+ "v32@0:8@\"PKGroupsControllerSnapshotFetchOptions\"16@?<v@?@\"PKGroupsControllerSnapshot\">24"
+ "v32@0:8@\"PKPayLaterCardMagnitudes\"16@\"NSString\"24"
+ "v32@0:8@\"PKPayLaterFinancingPlan\"16@\"NSString\"24"
+ "v32@0:8@\"PKPaymentAvailableProductsRequest\"16@?<v@?@\"PKPaymentAvailableProductsResponse\"@\"NSError\">24"
+ "v32@0:8@\"PKPaymentRequest\"16@?<v@?B>24"
+ "v32@0:8@\"PKPaymentShareableCredential\"16@?<v@?B@\"PKPaymentPass\"@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"PKPaymentTransactionRequest\"16@?<v@?@\"PKCurrencyAmount\">24"
+ "v32@0:8@\"PKPeerPaymentFailureDiagnostic\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"PLPhotoLibraryOptions\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"PLPhotoLibrarySearchCriteria\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"PPFuzzyContactQuery\"16Q24"
+ "v32@0:8@\"PPSDataRequest\"16@?<v@?@@\"NSError\">24"
+ "v32@0:8@\"PPSource\"16Q24"
+ "v32@0:8@\"PRUISSnapshotServiceRequest\"16@?<v@?@\"PRUISSnapshotServiceResponse\"@\"NSError\">24"
+ "v32@0:8@\"QLFileThumbnailRequest\"16@?<v@?@\"QLThumbnailReply\"@\"NSError\">24"
+ "v32@0:8@\"RCWebRule\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"RMStoreDeclarationKey\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"RTBackgroundInertialOdometrySampleEnumerationOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"RTPlaceInferenceOptions\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"ResourceHint\"16@?<v@?@\"NSUUID\">24"
+ "v32@0:8@\"ResourceHint\"16@?<v@?B>24"
+ "v32@0:8@\"SAUIPaginateList\"16@?<v@?@\"AceObject<SAAceCommand>\">24"
+ "v32@0:8@\"SAUIShowRequestHandlingStatus\"16@?<v@?@\"AceObject<SAAceCommand>\">24"
+ "v32@0:8@\"SAUIStartGenAIEnablementFlow\"16@?<v@?@\"AceObject<SAAceCommand>\">24"
+ "v32@0:8@\"SAUIStartImmersiveExperience\"16@?<v@?@\"AceObject<SAAceCommand>\">24"
+ "v32@0:8@\"SBSRemoteContentAlert\"16@?<v@?@\"SBSRemoteContentAlertAction\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?@\"SDBetaProgram\"@\"NSError\">24"
+ "v32@0:8@\"SDDevice\"16@?<v@?B>24"
+ "v32@0:8@\"SDDevice\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SFB389NFCPromptConfiguration\"16@?<v@?@\"NSError\"dQ>24"
+ "v32@0:8@\"SGMailHeaders\"16@?<v@?@\"SGXPCResponse1\">24"
+ "v32@0:8@\"SGSocialProfile\"16@?<v@?@\"SGXPCResponse1\">24"
+ "v32@0:8@\"SKStatusSubscriptionMetadata\"16@?<v@?>24"
+ "v32@0:8@\"SMConversation\"16@?<v@?@\"NSDictionary\"qq@\"NSError\">24"
+ "v32@0:8@\"SMConversation\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"SMLikelyReceiverOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"SMLocalSessionState\"16@\"NSError\"24"
+ "v32@0:8@\"SPAccessoryDiscoveryPairingStatusRequest\"16@?<v@?@\"SPAccessoryDiscoveryPairingStatusResult\"@\"NSError\">24"
+ "v32@0:8@\"SPBeaconLocationShareContext\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"SPBeaconLocationShareContext\"16@?<v@?B>24"
+ "v32@0:8@\"SPBeaconLocationShareContext\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SPDelegatedLocationContext\"16@?<v@?@\"SPDelegatedLocationResult\"@\"NSError\">24"
+ "v32@0:8@\"STSetupConfiguration\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"STUserID\"16@?<v@?@\"STSetupConfiguration\"@\"NSError\">24"
+ "v32@0:8@\"SUCoreDDMDeclaration\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SUCoreDDMDeclarationGlobalSettings\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SUDescriptor\"16@\"SURollbackSuggestionInfo\"24"
+ "v32@0:8@\"SUDescriptor\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SUIAQuickActionConfigurationRequest\"16@?<v@?@\"SUIAutomationServiceError\">24"
+ "v32@0:8@\"SUIAStageManagerLayoutRequest\"16@?<v@?@\"SUIAutomationServiceError\">24"
+ "v32@0:8@\"SUKeybagOptions\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SUPurgeOptions\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SURollbackDescriptor\"16@\"NSError\"24"
+ "v32@0:8@\"SURollbackDescriptor\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SURollbackOptions\"16@?<v@?@\"SURollbackDescriptor\"@\"NSError\">24"
+ "v32@0:8@\"SURollbackOptions\"16@?<v@?B@\"SURollbackDescriptor\"@\"NSError\">24"
+ "v32@0:8@\"SURollbackSuggestionInfo\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"SUScanOptions\"16@?<v@?@\"SUScanResults\"@\"NSError\">24"
+ "v32@0:8@\"SYDStoreID\"16@\"NSDictionary\"24"
+ "v32@0:8@\"SecureBackup\"16@?<v@?@\"CSStingrayAccountStatus\"@\"NSError\">24"
+ "v32@0:8@\"TCTextCompositionInput\"16@\"NSArray\"24"
+ "v32@0:8@\"TCTextCompositionInput\"16@?<v@?@\"TCTextCompositionReviewOutput\"@\"NSError\">24"
+ "v32@0:8@\"THThreadNetworkBorderAgent\"16@?<v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">24"
+ "v32@0:8@\"TISupplementalLexicon\"16@?<v@?>24"
+ "v32@0:8@\"TPSpecificUser\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"TUNearbyDeviceHandle\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"UARPAccessoryID\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@\"UARPAccessoryID\"16@?<v@?@\"UARPAssetID\">24"
+ "v32@0:8@\"UARPAssetID\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@\"UARPConsent\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"UIColor\"16@\"UIColor\"24"
+ "v32@0:8@\"UISUIActivityExtensionItemDataRequest\"16@?<v@?@\"NSArray\"@\"UISDActivityItemData\"@\"NSError\">24"
+ "v32@0:8@\"ULUpdateConfiguration\"16@\"NSUUID\"24"
+ "v32@0:8@\"UNNotificationResponse\"16@?<v@?Q>24"
+ "v32@0:8@\"W5Event\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"W5Peer\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"W5Peer\"16@?<v@?@\"NSError\"@\"NSArray\">24"
+ "v32@0:8@\"WFDialogRequest\"16@?<v@?@\"WFDialogResponse\">24"
+ "v32@0:8@\"WFOnScreenContentServiceOptions\"16@?<v@?@\"WFOnScreenContent\"@\"NSError\">24"
+ "v32@0:8@\"WFOnScreenContentServiceOptions\"16@?<v@?@\"WFOnScreenContentNode\"@\"NSError\">24"
+ "v32@0:8@\"WFSiriActionRequest\"16@?<v@?@\"WFSiriActionResponse\">24"
+ "v32@0:8@\"WFSpringBoardWebClipMetadata\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"WFWorkflowCollection\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"WFWorkflowReference\"16@?<v@?@\"WFWorkflowCollection\"@\"NSError\">24"
+ "v32@0:8@\"WallpaperDeepLinksTemplate\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"WiFiAwareDatapathConfiguration\"16@?<v@?q>24"
+ "v32@0:8@\"WiFiAwarePublishConfiguration\"16@?<v@?q>24"
+ "v32@0:8@\"WiFiAwareSubscribeConfiguration\"16@?<v@?q>24"
+ "v32@0:8@\"WiFiMACAddress\"16@?<v@?i>24"
+ "v32@0:8@\"XPCThumbnailConfiguration\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"_DPDediscoDonation\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"_EXQuery\"16@?<v@?@\"_EXQueryResult\"@\"NSError\">24"
+ "v32@0:8@\"_EXSceneSessionConnectionRequest\"16@?<v@?@\"_EXSceneSessionConnectionResponse\"@\"NSError\">24"
+ "v32@0:8@\"_HKFilter\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"_HKObjectTypeAnchor\"16@\"NSUUID\"24"
+ "v32@0:8@\"_LTSELFLoggingEventData\"16@\"_LTSELFLoggingEventData\"24"
+ "v32@0:8@\"_OSInactivityPredictorOutput\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@\"_TtC12ModelCatalog17ResourceContainer\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"_TtC12ModelCatalog23ResourceBundleContainer\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"_TtC14NearbySessions19NearbyAdvertisement\"16@\"NSData\"24"
+ "v32@0:8@\"_TtC14NearbySessions25InvitationApprovalRequest\"16@?<v@?@\"_TtC14NearbySessions22InvitationJoinResponse\"@\"NSError\">24"
+ "v32@0:8@\"_TtC14NearbySessions26NearbyGroupCreationRequest\"16@?<v@?@\"_TtC14NearbySessions25NearbyGroupConnectionInfo\"@\"NSError\">24"
+ "v32@0:8@\"_TtC14NearbySessions26NearbyInvitationParameters\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"_TtC14NearbySessions29IncomingInvitationJoinRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"_TtC14NearbySessions35NearbyInvitationJoinRequestMetadata\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"_TtC19EnergyKitFoundation12EKEnergySite\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"_TtC20FaceTimeMessageStore10XPCWrapper\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"_TtC20FaceTimeMessageStore10XPCWrapper\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"_TtC4Sage22SummarizationXPCResult\"16@\"NSString\"24"
+ "v32@0:8@\"_TtC4Sage23SummarizationXPCRequest\"16@\"<SummarizationStreamingDelegate>\"24"
+ "v32@0:8@\"_TtC4Sage23SummarizationXPCRequest\"16@?<v@?@\"_TtC4Sage22SummarizationXPCResult\"@\"NSError\">24"
+ "v32@0:8@\"_TtC8Feedback15FBKFeedbackForm\"16@?<v@?@\"NSNumber\">24"
+ "v32@0:8@\"_TtC9WidgetKit22WidgetRelevanceRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"_TtC9WidgetKit25ModifyControlStateRequest\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"_TtC9WidgetKit33ControlsConfigurationXPCContainer\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@?<v@?@@\"NSError\">24"
+ "v32@0:8B16B20@\"NSString\"24"
+ "v32@0:8B16B20@?<v@?@\"NSError\"B>24"
+ "v32@0:8B16B20@?<v@?B@\"NSError\">24"
+ "v32@0:8C16C20@?<v@?@\"NSError\"@\"MIDICIProfileState\">24"
+ "v32@0:8I16B20@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8I16I20@?<v@?i>24"
+ "v32@0:8I16I20^{ScalarArgsArray=[16Q]I}24"
+ "v32@0:8I16i20@?<v@?@\"NSError\"@\"NSString\">24"
+ "v32@0:8Q16@\"<STStatusDomainData><STStatusDomainDataDifferencing>\"24"
+ "v32@0:8Q16@\"BSAnimationSettings\"24"
+ "v32@0:8Q16@\"CDPLocalSecret\"24"
+ "v32@0:8Q16@\"NSArray\"24"
+ "v32@0:8Q16@?<v@?@\"<WBSHistoryImporterDelegate>\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"DOCItemBookmark\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"LSDefaultApplicationQueryResult\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NDODeviceInfo\">24"
+ "v32@0:8Q16@?<v@?@\"NSArray\"@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSArray\"q>24"
+ "v32@0:8Q16@?<v@?@\"NSError\"QQQ@\"NSData\"BI>24"
+ "v32@0:8Q16@?<v@?@\"NSFileProviderKnownFolderLocations\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"PKPaymentHardwareStatus\">24"
+ "v32@0:8Q16@?<v@?q@\"NSError\">24"
+ "v32@0:8R@16@24"
+ "v32@0:8^{SpecSendRequestQuery=@}16@?24"
+ "v32@0:8d16@\"CSEndpointerMetrics\"24"
+ "v32@0:8d16@?<v@?@\"NSData\">24"
+ "v32@0:8d16@?<v@?B>24"
+ "v32@0:8d16@?<v@?B@\"NSArray\">24"
+ "v32@0:8q16@\"ATXUserNotification\"24"
+ "v32@0:8q16@?<v@?@\"<CGRemotePDFPageProtocol>\">24"
+ "v32@0:8q16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8q16@?<v@?@\"NSError\"@\"NSArray\">24"
+ "v32@0:8q16@?<v@?@\"NSError\"BI>24"
+ "v32@0:8q16@?<v@?@\"_OSInactivityPredictorOutput\"@\"NSError\">24"
+ "v32@0:8q16@?<v@?@\"_TtC14NearbySessions35NearbyInvitationJoinRequestMetadata\"@\"NSError\">24"
+ "v32@0:8q16@?<v@?B@\"NSString\">24"
+ "v32@0:8q16@?<v@?B^@>24"
+ "v32@0:8q16@?<v@?Q@\"NSError\">24"
+ "v32@0:8r^i16r^v24"
+ "v32@0:8{?=ii}16@?24"
+ "v32@0:8{?=ii}16@?<v@?@\"NSError\">24"
+ "v32@0:8{UIOffset=dd}16"
+ "v32@?0@\"<LAContextXPC>\"8@\"NSString\"16@\"NSError\"24"
+ "v32@?0@\"AAURLConfiguration\"8@\"NSHTTPURLResponse\"16@\"NSError\"24"
+ "v32@?0@\"NSArray\"8@\"NSDate\"16@\"NSError\"24"
+ "v32@?0@\"NSArray\"8@\"NSError\"16@\"NSDate\"24"
+ "v32@?0@\"NSData\"8@\"NFSignatureInfo\"16@\"NSError\"24"
+ "v32@?0@\"NSData\"8q16@\"NSError\"24"
+ "v32@?0@\"NSSet\"8@\"NSSecurityScopedURLWrapper\"16@\"NSError\"24"
+ "v32@?0@\"NSSet\"8@\"NSSet\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"NSURL\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"TPSyncingPolicy\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8q16@\"NSError\"24"
+ "v32@?0@\"NSURL\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0B8B12@\"NSError\"16@\"NSError\"24"
+ "v32@?0Q8Q16@\"NSError\"24"
+ "v32@?0q8@\"NSString\"16q24"
+ "v36@0:8@\"AAAudioRoutingControl\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"AUAudioUnitProperty\"16B24@?<v@?@\"NSError\"@>28"
+ "v36@0:8@\"AWDLTrafficRegistrationConfiguration\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"CKEventMetricInfo\"16B24@?<v@?>28"
+ "v36@0:8@\"CPLDropDerivativesRecipe\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"CTGeofenceProfile\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"DUPersonalIDDocument\"16i24@?<v@?@\"DUPersonalIDResult\"@\"NSError\">28"
+ "v36@0:8@\"FHTransaction\"16B24@?<v@?@\"FHFeaturesResponse\"@\"NSError\">28"
+ "v36@0:8@\"FPItemID\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"FPItemID\"16I24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"DOCItemBookmark\"@\"NSError\">28"
+ "v36@0:8@\"HKClinicalEphemeralAccount\"16B24@?<v@?@\"HKClinicalAccount\"@\"NSError\">28"
+ "v36@0:8@\"HKCloudSyncRequest\"16B24@\"NSError\"28"
+ "v36@0:8@\"HKConceptIdentifier\"16B24@?<v@?@\"HKConcept\"@\"NSError\">28"
+ "v36@0:8@\"NSArray\"16B24@?<v@?>28"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">28"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSMutableArray\">28"
+ "v36@0:8@\"NSArray\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8@\"NSData\"16B24@?<v@?@\"NSData\">28"
+ "v36@0:8@\"NSData\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8@\"NSData\"16I24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"NSDate\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@\"NSDictionary\"16B24@?<v@?B>28"
+ "v36@0:8@\"NSDictionary\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28"
+ "v36@0:8@\"NSSet\"16C24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16@\"NSNumber\"24B32"
+ "v36@0:8@\"NSString\"16B24@?<v@?>28"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"CKKSExternalKey\"@\"NSArray\"@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSDictionary\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSSet\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"PKAccountUserInfo\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"UTTypeRecord\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"VGVehicle\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">28"
+ "v36@0:8@\"NSString\"16B24@?<v@?BB>28"
+ "v36@0:8@\"NSString\"16C24@\"NSString\"28"
+ "v36@0:8@\"NSString\"16C24@?<v@?B@\"NSError\">28"
+ "v36@0:8@\"NSString\"16f24@\"NSString\"28"
+ "v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\"@\"NSString\">28"
+ "v36@0:8@\"NSString\"16i24@?<v@?i@\"NSError\">28"
+ "v36@0:8@\"NSURL\"16B24@\"NSError\"28"
+ "v36@0:8@\"NSURL\"16B24@?<v@?@\"FPItem\"@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@\"NSURL\"16B24@?<v@?B@\"NSURL\"@\"NSData\"@\"NSError\">28"
+ "v36@0:8@\"SFContactInfo\"16B24@?<v@?@\"SFContactInfo\"@\"NSError\">28"
+ "v36@0:8@\"SFFormAutoFillFrameHandle\"16@\"NSString\"24B32"
+ "v36@0:8@\"STStatusDomainDataChangeRecord\"16B24@?<v@?>28"
+ "v36@0:8@16B24B28I32"
+ "v36@0:8@16B24d28"
+ "v36@0:8@16I24R@28"
+ "v36@0:8@16R@24B32"
+ "v36@0:8@16R@24f32"
+ "v36@0:8@16q24B32"
+ "v36@0:8@?16B24B28i32"
+ "v36@0:8@?16R@24B32"
+ "v36@0:8B16@\"<BLUIHostServiceProtocol>\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@\"<PKPushablePassConfigurationProvider>\"20@?<v@?@\"<PKPushablePassConfigurationProvider>\"@\"NSError\">28"
+ "v36@0:8B16@\"NSArray\"20@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8B16@\"NSArray\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@\"NSArray\"20@?<v@?@\"NSMapTable\"@\"NSError\">28"
+ "v36@0:8B16@\"NSArray\"20@?<v@?q>28"
+ "v36@0:8B16@\"NSNumber\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@\"NSSet\"20@?<v@?B>28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"BDSMutableSecureEngagementData\"@\"NSError\">28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"GDViewAccessToken\"@\"NSError\">28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSArray\">28"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSArray\"@\"NSData\"@\"NSError\">28"
+ "v36@0:8B16@\"PKAddSecureElementPassConfiguration\"20@?<v@?B@\"NSError\">28"
+ "v36@0:8B16@\"PKFileDescriptorXPCContainer\"20@?<v@?B>28"
+ "v36@0:8B16@\"PKGroupsControllerSnapshotFetchOptions\"20@?<v@?@\"PKGroupsControllerSnapshot\">28"
+ "v36@0:8B16@\"PKPassesXPCContainer\"20@?<v@?q>28"
+ "v36@0:8B16@\"PKPaymentWebServiceContext\"20@?<v@?>28"
+ "v36@0:8B16@\"PKPeerPaymentWebServiceContext\"20@?<v@?>28"
+ "v36@0:8B16@\"WBSSavedAccountContext\"20@?<v@?B>28"
+ "v36@0:8B16@20d28"
+ "v36@0:8B16@?20@?28"
+ "v36@0:8B16Q20@?<v@?@\"NSURL\"@\"NSDate\"@\"NSError\">28"
+ "v36@0:8C16@\"NSString\"20@?<v@?@\"SGXPCResponse\">28"
+ "v36@0:8C16@20@?28"
+ "v36@0:8C16C20@\"MIDICIProfile\"24B32"
+ "v36@0:8I16@\"NSData\"20@?<v@?i>28"
+ "v36@0:8I16@20R@28"
+ "v36@0:8I16Q20@?<v@?iQ>28"
+ "v36@0:8Q16B24@\"NSArray\"28"
+ "v36@0:8Q16B24@?<v@?@\"NSArray\">28"
+ "v36@0:8Q16B24@?<v@?@\"PKPeerPaymentEncryptionCertificate\"@\"NSError\">28"
+ "v36@0:8Q16B24@?<v@?q@\"NSError\">28"
+ "v36@0:8Q16I24@?<v@?@\"NSError\"@\"NSArray\">28"
+ "v36@0:8Q16I24@?<v@?@\"NSError\"f>28"
+ "v36@0:8Q16I24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">28"
+ "v36@0:8Q16I24@?<v@?I@\"NSError\">28"
+ "v36@0:8Q16i24@?<v@?@\"PKMerchant\">28"
+ "v36@0:8S16@20@28"
+ "v36@0:8i16@\"NSArray\"20@?<v@?i>28"
+ "v36@0:8i16@\"NSURL\"20@?<v@?@\"NSError\">28"
+ "v36@0:8i16@20q28"
+ "v36@0:8i16d20Q28"
+ "v36@0:8i16q20@?<v@?Bdd>28"
+ "v36@0:8q16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8q16B24@?<v@?@\"NSUUID\"@\"NSError\">28"
+ "v36@0:8q16B24@?<v@?B@\"NSError\">28"
+ "v36@?0@\"NRMutableDeviceCollection\"8@\"NRSecureDevicePropertyStore\"16Q24B32"
+ "v36@?0@\"NSArray<NSFileProviderItem>\"8Q16B24@\"NSError\"28"
+ "v36@?0B8q12q20@\"SOSButtonPressState\"28"
+ "v36@?0Q8@\"NSData\"16I24@\"NSError\"28"
+ "v36@?0^{__CFSet=}8^{__CFDictionary=}16^{__CFDictionary=}24i32"
+ "v40@0:8@\"<IDSXPCOffGridMessengerClient>\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"<IDSXPCOffGridStateManagerClient>\"16@\"NSString\"24@?<v@?qq@\"NSError\">32"
+ "v40@0:8@\"AADeviceConfig\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"AALoginAccountResponse\"16@\"ACAccount\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"ACAccount\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"AFSiriRequest\"16@\"NSError\"24Q32"
+ "v40@0:8@\"AKAuthorization\"16@\"AKCredentialRequestContext\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"AKCustodianContext\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"AKPersistRecoveryKeyContext\"16@\"AKAppleIDAuthenticationContext\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"AKSignInWithAppleRequestContext\"16@\"AKSignInWithAppleAccountShareInfo\"24@?<v@?@\"AKSignInWithAppleAccount\"@\"NSError\">32"
+ "v40@0:8@\"AKSignInWithAppleRequestContext\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"AMSPurchaseSIWA\"16@\"<PaymentSheetDelegate>\"24@?<v@?@\"AMSPurchaseSIWAResult\"@\"NSError\">32"
+ "v40@0:8@\"ANPlaybackCommand\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"ASCAppOffer\"16@\"ASCMetricsActivity\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"ASDBetaAppFeedback\"16@\"NSURL\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"ATXHomeScreenEvent\"16Q24@\"NSArray\"32"
+ "v40@0:8@\"AUAudioUnitPreset\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"AUAudioUnitProperty\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"BCSBusinessEmailIdentifier\"16@\"NSString\"24@?<v@?@\"BCSBusinessEmailItem\"@\"NSError\">32"
+ "v40@0:8@\"BCSBusinessLogoIdentifier\"16@\"NSString\"24@?<v@?@\"BCSBusinessLogo\"@\"NSError\">32"
+ "v40@0:8@\"BDSCRDTModelSyncVersionInfo\"16@\"BDSReadingHistoryUpdateInfo\"24@?<v@?B>32"
+ "v40@0:8@\"BLDownloadManifestRequest\"16@\"<BLUIHostServiceProtocol>\"24@?<v@?@\"BLDownloadManifestResponse\"@\"NSError\">32"
+ "v40@0:8@\"BMResourceSpecifier\"16Q24@?<v@?@\"BMResourceContainer\"@\"NSString\"@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"CADObjectID\"16@\"CADObjectID\"24@?<v@?i@\"CADObjectID\">32"
+ "v40@0:8@\"CADObjectID\"16@\"NSString\"24@?<v@?i@\"NSSecurityScopedURLWrapper\">32"
+ "v40@0:8@\"CADObjectID\"16Q24@?<v@?i@\"NSData\">32"
+ "v40@0:8@\"CDPContext\"16@\"<CDPRemoteDeviceSecretValidatorProtocolInternal>\"24@?<v@?>32"
+ "v40@0:8@\"CDPContext\"16@\"<CDPStateUIProviderInternal>\"24@?<v@?Q@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"CDPContext\"16@\"NSError\"24@?<v@?Q@\"NSError\">32"
+ "v40@0:8@\"CHTokenizedTextResult\"16@\"CHRemoteRecognitionTextRequest\"24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"CKContainerSetupInfo\"16@\"<CKXPCContainerScopedClient>\"24@?<v@?@\"<CKXPCContainerScopedDaemon>\"@\"NSError\">32"
+ "v40@0:8@\"CKRecordID\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CKRecordZoneID\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CKShare\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CNContact\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"CPLResource\"16@\"NSString\"24@?<v@?@\"NSString\">32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestination\"24@\"CTLazuliCapabilitiesInformation\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestination\"24@\"CTLazuliMessageID\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestination\"24@\"CTLazuliOperationResult\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatIcon\"24@\"CTLazuliOperationResult\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24@\"CTLazuliGroupChatParticipant\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24@\"CTLazuliOperationResult\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatSubject\"24@\"CTLazuliOperationResult\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatUri\"24@\"CTLazuliGroupChatParticipant\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliMessageID\"24@\"CTLazuliMessageRevokeResult\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliMessageID\"24@\"CTLazuliMessageTypeInformation\"32"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliMessageID\"24@\"CTLazuliOperationError\"32"
+ "v40@0:8@\"CWFAutoJoinParameters\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CWFBackgroundScanConfiguration\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CWFHostAPConfiguration\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CWFNearbyDeviceDiscoveryParameter\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CWFNetworkProfile\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\"@\"NSNumber\">32"
+ "v40@0:8@\"DIEncryptionCreator\"16@\"NSString\"24@?<v@?@\"DIEncryptionCreator\"@\"NSError\">32"
+ "v40@0:8@\"DNDBehaviorSettings\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"DNDContactHandle\"16@\"DNDRequestDetails\"24@?<v@?@\"NSArray<__NSString__>\"@\"NSError\">32"
+ "v40@0:8@\"DNDContactHandle\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"DNDModeAssertionDetails\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"DNDModeConfiguration\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"DNDScheduleSettings\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"EMMessage\"16@\"EMMessageObjectID\"24q32"
+ "v40@0:8@\"EMMessageObjectID\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"FPItemID\"16@\"NSFileProviderRequest\"24@?<v@?@\"FPItem\"@\"FPExtensionResponse\"@\"NSError\">32"
+ "v40@0:8@\"FPSandboxingURLWrapper\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"FPSandboxingURLWrapper\"16Q24@?<v@?@\"DOCItemBookmark\"@\"NSError\">32"
+ "v40@0:8@\"FPSandboxingURLWrapper\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"NSString\"24@?<v@?@\"FSProbeResult\"@\"NSError\">32"
+ "v40@0:8@\"HDExtractionRequest\"16@\"HKPIIRedactor\"24@?<v@?@\"HDClinicalDataCollectionExtractionResult\"@\"NSError\">32"
+ "v40@0:8@\"HDOriginalFHIRResourceObject\"16Q24@?<v@?@\"HDHRSSignedClinicalDataProcessingContextCollection\"@\"NSError\">32"
+ "v40@0:8@\"HKClinicalBrand\"16@\"NSNumber\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"HKMCPregnancyModeSetupCompletionRecord\"16@\"NSUUID\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"HKMedicalRecord\"16Q24@?<v@?@\"HKSignedClinicalDataGroup\"@\"NSError\">32"
+ "v40@0:8@\"HKSampleType\"16@\"NSDate\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"HKSignedClinicalDataSource\"16Q24@?<v@?@\"HDHRSSignedClinicalDataProcessingContextCollection\"@\"NSError\">32"
+ "v40@0:8@\"HMDeviceConfigurations\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"IDSOffGridEncryptedMessage\"16@\"IDSOffGridDeliveryOptions\"24@?<v@?@\"IDSOffGridEncryptedMessage\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"IXApplicationIdentity\"16Q24@?<v@?Q@\"NSError\">32"
+ "v40@0:8@\"LNAsyncSequenceReference\"16@\"LNAsyncIteratorOptions\"24@?<v@?@\"LNAsyncIteratorReference\"@\"NSError\">32"
+ "v40@0:8@\"LPLinkMetadata\"16@\"NSArray\"24@?<v@?@\"NSError\"@\"NSArray\">32"
+ "v40@0:8@\"MCCSecretAgentContext\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"MIDICIProfile\"16C24C28@?<v@?@\"NSError\">32"
+ "v40@0:8@\"MOEventBundleFetchOptions\"16@\"MOXPCContext\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"MOEventFetchOptions\"16@\"MOXPCContext\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"MOSuggestion\"16@\"MOSuggestionAssetTypeOptions\"24@?<v@?@\"MOSuggestionAssetsArrayTransport\"@\"NSError\">32"
+ "v40@0:8@\"MOSuggestion\"16@\"MOSuggestionAssetTypeOptions\"24@?<v@?@\"MOSuggestionAssetsBundle\"@\"NSError\">32"
+ "v40@0:8@\"MOXPCContext\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"MTIDScheme\"16@\"NSDictionary\"24@?<v@?@\"MTIDSecret\"@\"NSError\">32"
+ "v40@0:8@\"NINearbyObject\"16@\"NIRegionPredicate\"24@\"NIRegionPredicate\"32"
+ "v40@0:8@\"NSArray\"16@\"CMLClientConfig\"24@?<v@?q@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"FPItemID\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSArray\"16@\"LNExportedContentConfiguration\"24@?<v@?@\"LNValue\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"LNQueryRequest\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"MOXPCContext\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSDateInterval\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"ASDPurchaseResponse\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@\"NSDate\"32"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"HAHDPinnedContentState\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSSet\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16q24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSArray<__NSString__>\"16@\"DNDRequestDetails\"24@?<v@?@\"NSArray<__DNDAppInfo__>\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"CNApplicationProxy\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSData\">32"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"SWTransparencyExpiringVerificationResult\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSError\"24@\"NSUUID\"32"
+ "v40@0:8@\"NSData\"16@\"NSNumber\"24@?<v@?>32"
+ "v40@0:8@\"NSData\"16@\"NSNumber\"24@?<v@?@\"NSDictionary\"@\"NSError\"@\"IDSBAASignerContext\">32"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@\"IDSServerMessagingIncomingContext\"32"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"DCCredentialTrust\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSURL\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSData\"@\"PKSecureElementSignatureInfo\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSData\"16d24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16q24@?<v@?@\"DUFoundInEventClientAbstractResult\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16q24@?<v@?@\"NSArray\"@\"NSArray\"B@\"NSData\"@\"FPExtensionResponse\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16q24@?<v@?@\"NSArray\"@\"NSData\"@\"NSData\"@\"FPExtensionResponse\"@\"NSError\">32"
+ "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSDate\"16@\"RTEstimatedLocationOptions\"24@?<v@?@\"CLLocation\"@\"NSError\">32"
+ "v40@0:8@\"NSDate\"16B24B28@?<v@?i@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSDate\">32"
+ "v40@0:8@\"NSDate\"16Q24@?<v@?@\"AAAttributionResult\">32"
+ "v40@0:8@\"NSDate\"16q24@?<v@?B>32"
+ "v40@0:8@\"NSDateInterval\"16@\"NSData\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSDateInterval\"16@\"NSData\"24@?<v@?@\"NSDictionary\">32"
+ "v40@0:8@\"NSDictionary\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"CWFRequestParameters\"24@?<v@?@\"NSError\"@\"NSDictionary\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSArray\"24@\"NSArray\"32"
+ "v40@0:8@\"NSDictionary\"16@\"NSData\"24@?<v@?@\"NSURL\"@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32"
+ "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"ASDPurchaseResponse\"@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"NSDictionary\"16@\"NSUUID\"24@?<v@?@\"NSError\"@\"NSArray\"@\"NSURL\">32"
+ "v40@0:8@\"NSDictionary\"16@\"REMObjectID\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16I24S28q32"
+ "v40@0:8@\"NSDictionary\"16Q24@\"NSString\"32"
+ "v40@0:8@\"NSDictionary\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSError\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSFileHandle\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSFileProviderDomain\"16Q24@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">32"
+ "v40@0:8@\"NSIndexSet\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSDictionary\"32"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSString\"32"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSString\"24o^@32"
+ "v40@0:8@\"NSNumber\"16Q24@?<v@?B>32"
+ "v40@0:8@\"NSPredicate\"16@\"_CDContextualKeyPath\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSPredicate\"16q24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSPredicate\"16q24@?<v@?Q@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"HKQuerySubscriptionAnchor\"24@\"NSUUID\"32"
+ "v40@0:8@\"NSSet\"16@\"IDSURI\"24@?<v@?@\"NSSet\"@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSSet\"24@\"PKAccount\"32"
+ "v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?B>32"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSSet\"@\"NSError\">32"
+ "v40@0:8@\"NSSet\"16Q24@?<v@?@\"NSSet\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"CLLocation\"24@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"DCCredentialOptions\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"DNDRequestDetails\"24@?<v@?@\"DNDAppInfo\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"DNDRequestDetails\"24@?<v@?@\"DNDModeConfiguration\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"IMItem\"24@\"NSArray\"32"
+ "v40@0:8@\"NSString\"16@\"LNAction\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSData\"@\"LNAction\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"LNEntity\"24@?<v@?@\"LNValue\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"MRCodableGroupSessionParticipant\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSArray\"B@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSDate\"@\"NSDate\">32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"INIntent\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"PKPaymentTransaction\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?@\"_TtC9SEService11Reservation\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?Q@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?i>32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSData\">32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?B@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSSet\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"BCSBusinessEmailItem\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"BCSLinkItemModel\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"GDViewAccessInfo\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"HAHDPinnedContentState\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\"@\"NSFileHandle\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSUUID\"@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"PKAccountPaymentFundingSource\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"PKAccountStatementMetadata\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"RMModelDeclarationBase\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?i@\"CADObjectID\">32"
+ "v40@0:8@\"NSString\"16@\"PKPaymentBalanceReminder\"24@\"PKPaymentBalance\"32"
+ "v40@0:8@\"NSString\"16@\"RTPeopleDiscoveryServiceConfiguration\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"SDDevice\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"SKPresenceOptions\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"SKPresencePayload\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"SMConversation\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"SOAuthorizationCredential\"24@\"NSError\"32"
+ "v40@0:8@\"NSString\"16@\"UARPAssetID\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@24@?<v@?B>32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NDODeviceInfo\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\"f>32"
+ "v40@0:8@\"NSString\"16d24@?<v@?>32"
+ "v40@0:8@\"NSString\"16d24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"NSError\"@\"NSString\">32"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"SGXPCResponse1\">32"
+ "v40@0:8@\"NSString\"16r^{?=[8I]}24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16{CGSize=dd}24"
+ "v40@0:8@\"NSString\"16{_NSRange=QQ}24"
+ "v40@0:8@\"NSString<TRIFactorPackId>\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"ASWebAuthenticationSessionCallback\"24@\"NSArray\"32"
+ "v40@0:8@\"NSURL\"16@\"NSData\"24@?<v@?@\"PVAppIdentityDigest\">32"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"_TtC13SiriAnalytics13StagingReport\"@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16Q24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16Q24@?<v@?@\"SAVolumeSizeInfo\"@\"NSError\">32"
+ "v40@0:8@\"NSURL\"16d24d32"
+ "v40@0:8@\"NSURL\"16q24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSURLRequest\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"DNDRequestDetails\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSData\"24@?<v@?@\"_TtC9SEService11Reservation\"@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSDate\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSDictionary\"24@\"NSNumber\"32"
+ "v40@0:8@\"NSUUID\"16@\"NSError\"24@?<v@?>32"
+ "v40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"HKProfileIdentifier\"@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSUUID\"32"
+ "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16q24@?<v@?q>32"
+ "v40@0:8@\"NTKArgonKeyDescriptor\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NTKFaceInstanceDescriptor\"16@\"NSDictionary\"24@?<v@?@\"UIImage\">32"
+ "v40@0:8@\"NTKFaceInstanceDescriptor\"16@\"NSDictionary\"24@?<v@?B@\"UIImage\">32"
+ "v40@0:8@\"NTKFaceInstanceDescriptor\"16@\"NSUUID\"24@\"NSNumber\"32"
+ "v40@0:8@\"PAAccess\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"PKAccountEnhancedMerchant\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"PKAccountPromotion\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"PKAppleBalanceInStoreTopUpToken\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"PKExpressPassConfiguration\"16@\"NSData\"24@?<v@?B@\"NSSet\">32"
+ "v40@0:8@\"PKExpressPassConfiguration\"16@\"NSSet\"24@?<v@?@\"NSSet\">32"
+ "v40@0:8@\"PKPayLaterFinancingPlan\"16@\"PKPayLaterFinancingPlan\"24@\"NSString\"32"
+ "v40@0:8@\"PKPaymentRewardsRedemption\"16@\"NSString\"24@?<v@?>32"
+ "v40@0:8@\"PKPeerPaymentRecurringPaymentMemo\"16@\"NSString\"24@?<v@?@\"PKPeerPaymentRecurringPayment\">32"
+ "v40@0:8@\"REMObjectID\"16@\"NSData\"24@?<v@?@\"CKShare\"@\"NSError\">32"
+ "v40@0:8@\"REMObjectID\"16B24B28@?<v@?@\"REMMigrationResult\"@\"NSError\">32"
+ "v40@0:8@\"REMObjectID\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"REMStoreContainerToken\"16@\"NSString\"24@?<v@?@\"<REMXPCDebugPerformer>\"@\"NSError\">32"
+ "v40@0:8@\"RMModelDeclarationBase\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"RMStoreUnresolvedAsset\"16@\"NSString\"24@?<v@?@\"RMStoreResolvedAsset\"@\"NSError\">32"
+ "v40@0:8@\"SDDevice\"16@\"SDBetaProgram\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"SKHandle\"16@\"NSString\"24@?<v@?@\"SKStatusSubscriptionMetadata\"@\"NSError\">32"
+ "v40@0:8@\"SKStatusPublishRequest\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"SMMessage\"16@\"SMConversation\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"SOAuthorizationCredential\"16@\"NSError\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"SUDownloadOptions\"16@\"SUDownloadOptions\"24@?<v@?BB@\"NSError\"@\"NSError\">32"
+ "v40@0:8@\"SURollbackDescriptor\"16@\"SURollbackOptions\"24@?<v@?B@\"SURollbackDescriptor\"@\"NSError\">32"
+ "v40@0:8@\"SUScanOptions\"16@\"SUScanResults\"24@\"NSError\"32"
+ "v40@0:8@\"TCTextCompositionCalendarEventGenerationInput\"16@\"NSDictionary\"24@?<v@?@\"TCTextCompositionCalendarEventGenerationOutput\"@\"NSError\">32"
+ "v40@0:8@\"TCTextCompositionInput\"16@\"NSString\"24@?<v@?@\"TCTextCompositionOutput\"@\"NSError\">32"
+ "v40@0:8@\"TPSpecificUser\"16@\"NSArray\"24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"TUNearbyDeviceHandle\"16@\"NSUUID\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24@\"UARPUpdateFirmwareAnalyticsEventFrameworkParams\"32"
+ "v40@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24Q32"
+ "v40@0:8@\"UARPConsent\"16Q24Q32"
+ "v40@0:8@\"W5Peer\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"W5Peer\"16@\"NSDictionary\"24@?<v@?@\"NSError\"@\"NSArray\">32"
+ "v40@0:8@\"W5Peer\"16@\"NSFetchRequest\"24@?<v@?@\"NSError\"@\"NSArray\">32"
+ "v40@0:8@\"W5Peer\"16@\"NSURL\"24@?<v@?@\"NSError\"@\"NSArray\">32"
+ "v40@0:8@\"W5Peer\"16@\"NSURL\"24@?<v@?@\"NSError\"@\"NSURL\">32"
+ "v40@0:8@\"W5PeerDiscoveryConfiguration\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"WFDatabaseObjectDescriptor\"16@\"NSString\"24@?<v@?@\"WFDatabaseObjectDescriptor\"@\"NSError\">32"
+ "v40@0:8@\"WFItemProviderRequestMetadata\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"WFWorkflowReference\"16@\"NSString\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"_DASActivity\"16@\"_DASActivityGroup\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"_EXQuery\"16@\"NSXPCListenerEndpoint\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"_TtC14NearbySessions19NearbyAdvertisement\"16@\"_TtC14NearbySessions35NearbyInvitationJoinRequestMetadata\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"_TtC14NearbySessions19NearbyAdvertisement\"16@\"_TtC14NearbySessions35NearbyInvitationJoinRequestMetadata\"24@?<v@?@\"_TtC14NearbySessions14InvitationBlob\"@\"NSError\">32"
+ "v40@0:8@\"_TtC14NearbySessions26NearbyAdvertisementRequest\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"_TtC14NearbySessions26NearbyInvitationParameters\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"_TtC14NearbySessions29IncomingInvitationJoinRequest\"16@\"_TtC14NearbySessions22InvitationJoinResponse\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@\"NSString\"24@?<v@?@\"NSError\"@\"NSArray\">32"
+ "v40@0:8@16I24C28@32"
+ "v40@0:8@16I24S28q32"
+ "v40@0:8@16Q24@?<v@?>32"
+ "v40@0:8@16R@24f32B36"
+ "v40@0:8@16q24B32B36"
+ "v40@0:8@16q24Q32"
+ "v40@0:8@16r*24r*32"
+ "v40@0:8@16{CGSize=dd}24"
+ "v40@0:8@?16^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}24q32"
+ "v40@0:8C16C20@24@32"
+ "v40@0:8C16S20@\"NSString\"24@\"NSString\"32"
+ "v40@0:8I16B20@\"NSArray\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8I16B20@24@?32"
+ "v40@0:8I16I20@\"AVAudioFormat\"24@?<v@?@\"NSError\"@\"NSArray\">32"
+ "v40@0:8I16I20@24R@32"
+ "v40@0:8Q16@\"ICClientInfo\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8Q16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8Q16@\"NSDate\"24@?<v@?@\"NSURL\"@\"NSError\">32"
+ "v40@0:8Q16@\"NSDictionary\"24@?<v@?>32"
+ "v40@0:8Q16@\"NSDictionary\"24@?<v@?B>32"
+ "v40@0:8Q16@\"NSString\"24@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSError\">32"
+ "v40@0:8Q16@\"NSString\"24@?<v@?@\"PKPeerPaymentRecurringPayment\">32"
+ "v40@0:8Q16@\"NSString\"24@?<v@?@\"PKPeerPaymentRecurringPayment\"@\"NSError\">32"
+ "v40@0:8Q16@\"NSString\"24@?<v@?@\"PKPhysicalCard\">32"
+ "v40@0:8Q16@\"NSURL\"24@?<v@?@\"NSError\">32"
+ "v40@0:8Q16@24@?<v@?B>32"
+ "v40@0:8Q16Q24@?<v@?@\"NSDictionary\">32"
+ "v40@0:8Q16q24@?<v@?@\"NSError\">32"
+ "v40@0:8Q16q24@?<v@?Q@\"NSError\">32"
+ "v40@0:8R@16@24Q32"
+ "v40@0:8R@16{CLBarometerCalibrationElevationThreshold=dd}24"
+ "v40@0:8^{__CFArray=}16@24r^{__CFArray=}32"
+ "v40@0:8d16d24@?32"
+ "v40@0:8d16d24@?<v@?@\"NSError\">32"
+ "v40@0:8d16d24d32"
+ "v40@0:8f16B20Q24@?<v@?@\"NSError\"@\"NSString\">32"
+ "v40@0:8i16@\"NSURL\"20B28@?<v@?@\"NSError\">32"
+ "v40@0:8q16@\"ATXUserNotification\"24Q32"
+ "v40@0:8q16@\"IDSOffGridModeOptions\"24@?<v@?qq@\"NSError\">32"
+ "v40@0:8q16@\"NSArray\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8q16@\"NSDictionary\"24@?<v@?q>32"
+ "v40@0:8q16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8q16@\"NSString\"24@\"_TtC8Feedback15FBKFeedbackForm\"32"
+ "v40@0:8q16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8q16@\"NSURL\"24@?<v@?q@\"NSError\">32"
+ "v40@0:8q16@\"NSUUID\"24@\"NSDate\"32"
+ "v40@0:8q16@?24@?32"
+ "v40@0:8q16q24@\"NSError\"32"
+ "v40@0:8q16q24@32"
+ "v40@0:8{CGSize=dd}16@?32"
+ "v40@0:8{CGSize=dd}16@?<v@?B@\"NSError\">32"
+ "v40@0:8{CLLocationCoordinate2D=dd}16@?<v@?@\"NSArray\">32"
+ "v40@0:8{PASessionTestingSettings=qQ}16@?<v@?@\"NSError\">32"
+ "v40@0:8{SBSystemApertureContainerRenderingConfiguration=qqB}16"
+ "v40@0:8{VehicleStateData=QQQ}16"
+ "v40@?0@\"BMResourceContainer\"8@\"NSString\"16@\"NSData\"24@\"NSError\"32"
+ "v40@?0@\"CKKSExternalKey\"8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
+ "v40@?0@\"NSArray\"8Q16d24@\"NSError\"32"
+ "v40@?0@\"NSData\"8@\"PBSecurityScopedURLWrapper\"16@\"PBResponseMetadata\"24@\"NSError\"32"
+ "v40@?0@\"NSNumber\"8@\"NSArray\"16@\"NSDate\"24@\"NSError\"32"
+ "v40@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
+ "v40@?0{CGRect={CGPoint=dd}{CGSize=dd}}8"
+ "v44@0:8@\"BRFileObjectID\"16S24@\"NSFileProviderRequest\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"CKRecordZoneID\"16q24B32@?<v@?@\"CKDPCSData\"@\"NSError\">36"
+ "v44@0:8@\"GKPlayerInternal\"16Q24i32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@\"IMMessageItem\"16B24Q28@\"NSString\"36"
+ "v44@0:8@\"MOXPCContext\"16Q24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSArray\"16@\"NSArray\"24i32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@\"NSArray\"16@\"NSString\"24B32@?<v@?B@\"NSError\">36"
+ "v44@0:8@\"NSArray\"16@\"NSString\"24i32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@\"NSArray\"16@\"NSURL\"24i32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@\"NSArray\"16B24@\"HKQueryAnchor\"28@\"NSUUID\"36"
+ "v44@0:8@\"NSArray\"16B24Q28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSArray\"16C24@\"NSArray\"28@?<v@?@\"NSDate\">36"
+ "v44@0:8@\"NSData\"16@\"NSString\"24B32@?<v@?B>36"
+ "v44@0:8@\"NSData\"16@\"RMStoreDeclarationKey\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40"
+ "v44@0:8@\"NSData\"16q24i32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@\"NSDate\"16@\"NSDate\"24B32@?<v@?@\"NSSet\"@\"NSError\">36"
+ "v44@0:8@\"NSDate\"16@\"NSString\"24B32@?<v@?B@\"NSError\">36"
+ "v44@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32B40"
+ "v44@0:8@\"NSDictionary\"16B24Q28@?<v@?i>36"
+ "v44@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24B32@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">36"
+ "v44@0:8@\"NSString\"16@\"NSArray\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSString\"16@\"NSData\"24I32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSString\"16@\"NSDictionary\"24B32@?<v@?B@\"NSError\">36"
+ "v44@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24B32@?<v@?i>36"
+ "v44@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24B32@?<v@?ii>36"
+ "v44@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32B40"
+ "v44@0:8@\"NSString\"16@\"NSString\"24B32@?<v@?@\"NSData\">36"
+ "v44@0:8@\"NSString\"16@\"NSString\"24i32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSString\"16@\"UARPAssetID\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSString\"16B24@\"NSString\"28@?<v@?@\"GDViewAccessToken\"@\"NSError\">36"
+ "v44@0:8@\"NSString\"16B24Q28@?<v@?@\"NSArray\"@\"NSError\"@\"NSDate\">36"
+ "v44@0:8@\"NSString\"16I24@\"LAContext\"28@?<v@?@\"NSData\"@\"NSError\">36"
+ "v44@0:8@\"NSString\"16I24@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSString\"16i24@\"NSString\"28@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@\"NSString\"16i24@\"NSString\"28@?<v@?@\"TRIClientRolloutArtifact\"@\"NSError\">36"
+ "v44@0:8@\"NSString\"16q24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSURL\"16@\"NSError\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"NSURL\"16@\"NSString\"24B32@?<v@?@\"SGXPCResponse1\">36"
+ "v44@0:8@\"NSURL\"16@\"NSString\"24B32@?<v@?B>36"
+ "v44@0:8@\"NSURL\"16B24@\"NSString\"28@?<v@?@\"BCSLinkItemModel\"@\"NSError\">36"
+ "v44@0:8@\"NSURL\"16B24@\"NSString\"28@?<v@?B@\"NSString\"@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@\"NSUUID\"16@\"SPBeaconIndex\"24C32@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8@\"NSUUID\"16I24@\"NSUUID\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"OTControlArguments\"16B24@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"OTControlArguments\"16q24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"RMModelDeclarationBase\"16B24@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"TPSpecificUser\"16B24B28B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"WFItemProviderRequestMetadata\"16@\"NSString\"24B32@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSError\">36"
+ "v44@0:8@16@\"AUAudioUnitProperty\"24B32@?<v@?@\"NSError\"@\"NSArray\">36"
+ "v44@0:8@16@24i32@36"
+ "v44@0:8@16I24@28@?36"
+ "v44@0:8@16Q24B32@36"
+ "v44@0:8@16Q24I32R@36"
+ "v44@0:8@16Q24Q32B40"
+ "v44@0:8@16R@24*32S40"
+ "v44@0:8@16R@24d32B40"
+ "v44@0:8@16S24@28@36"
+ "v44@0:8@16S24@28@?36"
+ "v44@0:8@16d24B32d36"
+ "v44@0:8@16q24@32B40"
+ "v44@0:8@16q24i32@?36"
+ "v44@0:8B16@\"CWFNetworkProfile\"20@\"CWFRequestParameters\"28@?<v@?@\"NSError\">36"
+ "v44@0:8B16@\"NSData\"20@\"NSData\"28@?<v@?@\"NSString\"@\"NSString\"@\"NSString\"@\"NSData\"@\"NSError\">36"
+ "v44@0:8B16@\"NSMapTable\"20q28@?<v@?@\"NSError\">36"
+ "v44@0:8B16@\"NSString\"20@\"NSData\"28@?<v@?@\"PKPaymentTransaction\"@\"NSError\">36"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?@\"NSString\">36"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?@\"PKAppletSubcredential\"@\"NSError\">36"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B>36"
+ "v44@0:8B16@\"NSString\"20B28B32@?<v@?@\"NSError\">36"
+ "v44@0:8B16@\"NSString\"20q28@?<v@?@\"NSArray\">36"
+ "v44@0:8B16@\"WFWorkflowReference\"20@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8B16@20@28@?36"
+ "v44@0:8B16@20q28@?36"
+ "v44@0:8B16q20@\"NSPredicate\"28@?<v@?Q@\"NSError\">36"
+ "v44@0:8I16Q20Q28@?<v@?i>36"
+ "v44@0:8I16q20Q28@?<v@?i>36"
+ "v44@0:8Q16@\"NSDictionary\"24B32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8d16B24{CGPoint=dd}28"
+ "v44@0:8i16@\"NSString\"20@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8i16@\"NSURL\"20@\"NSArray\"28@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8i16@\"NSURL\"20@\"NSURL\"28@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8i16@20@28q36"
+ "v44@0:8q16@24B32@?36"
+ "v44@0:8q16B24q28@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">36"
+ "v44@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@?36"
+ "v44@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@?<v@?C>36"
+ "v44@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@?<v@?iC>36"
+ "v44@?0Q8@\"NSData\"16C24I28I32@\"NSError\"36"
+ "v48@0:8@\"<ASCOffer>\"16@\"NSString\"24@\"ASCOfferMetadata\"32q40"
+ "v48@0:8@\"<DOCHostDocumentBrowserViewControllerInterface>\"16@\"DOCConfiguration\"24@\"DOCUIPBrowserState\"32@?<v@?@\"<DOCServiceDocumentBrowserViewControllerInterface>\">40"
+ "v48@0:8@\"<FigCameraViewfinderSessionRemoteObject>\"16q24@\"NSData\"32B40B44"
+ "v48@0:8@\"<IDSXPCServerMessagingClient>\"16@\"NSString\"24@\"NSString\"32@\"NSSet\"40"
+ "v48@0:8@\"<SFUnlockClientProtocol>\"16Q24@\"NSString\"32@\"NSUUID\"40"
+ "v48@0:8@\"<SFUnlockClientProtocol>\"16Q24@\"NSUUID\"32@\"SFAuthenticationOptions\"40"
+ "v48@0:8@\"ACAccount\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"AKBeneficiaryManifest\"16@\"<AAInheritanceContactInfo>\"24@\"NSString\"32@?<v@?@\"AABeneficiary\"@\"NSError\">40"
+ "v48@0:8@\"ASCMetricsData\"16@\"NSDictionary\"24@\"ASCMetricsActivity\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestination\"24@\"CTLazuliCapabilitiesInformation\"32@\"CTLazuliOperationResult\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestination\"24@\"CTLazuliChatBotRenderInformationData\"32@\"CTLazuliOperationResult\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliDestination\"24@\"CTLazuliMessageID\"32@\"CTLazuliMessageComposingIndicator\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24@\"CTLazuliGroupChatIcon\"32@\"CTLazuliGroupChatParticipant\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24@\"CTLazuliGroupChatParticipantList\"32@\"CTLazuliGroupChatParticipant\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24@\"CTLazuliGroupChatSubject\"32@\"CTLazuliGroupChatParticipant\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatParticipantList\"24@\"CTLazuliGroupChatParticipantList\"32@\"CTLazuliOperationResult\"40"
+ "v48@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24@\"CTBundleMatchingInfo\"32@?<v@?@\"NSObject\"@\"NSError\">40"
+ "v48@0:8@\"CWFNetworkProfile\"16Q24@\"CWFRequestParameters\"32@?<v@?@\"NSError\"@\"NSArray\">40"
+ "v48@0:8@\"CalGrantedDelegate\"16q24@\"CADObjectID\"32@?<v@?i>40"
+ "v48@0:8@\"DCCredentialNonce\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"DCCredentialAuthorizationToken\"@\"NSError\">40"
+ "v48@0:8@\"DNDModeAssertionInvalidationDetails\"16@\"NSNumber\"24@\"DNDRequestDetails\"32@?<v@?@\"DNDModeAssertionInvalidation\"@\"NSError\">40"
+ "v48@0:8@\"FPSandboxingURLWrapper\"16@\"FPSandboxingURLWrapper\"24Q32@?<v@?@\"DOCItemBookmark\"@\"NSError\">40"
+ "v48@0:8@\"FSResource\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"FSResource\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"FSVolumeIdentifier\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"FSVolumeIdentifier\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"CPLRecordComputeStateValidator\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"MOXPCContext\"24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24Q32@?<v@?q>40"
+ "v48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSFileHandle\"24q32@?<v@?q>40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSString\">40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32Q40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSURL\"24@\"MADEmbeddingSearchOptions\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"SKHandle\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16Q24@\"NSDateInterval\"32@\"NSDictionary\"40"
+ "v48@0:8@\"NSArray\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16Q24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16q24@\"EMObjectID\"32@?<v@?@\"NSArray\">40"
+ "v48@0:8@\"NSArray\"16q24@\"SYDTestConfiguration\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@?<v@?B>40"
+ "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"NSFileHandle\"24Q32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"VCVoiceShortcut\"@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSUUID\"32@?<v@?B>40"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"WFWorkflowReference\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"NSString\"24Q32@?<v@?@\"WFWorkflowReference\"@\"NSError\">40"
+ "v48@0:8@\"NSData\"16C24S28@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@\"NSDate\"16@\"NSArray\"24Q32@?<v@?@\"REMChangeSet\"@\"NSError\">40"
+ "v48@0:8@\"NSDate\"16@\"NSDate\"24@\"<ECEmailAddressConvertible>\"32@\"NSNumber\"40"
+ "v48@0:8@\"NSDate\"16@\"NSDate\"24@\"NSDate\"32@?<v@?@\"BDSReadingHistoryStateInfo\"B>40"
+ "v48@0:8@\"NSDate\"16d24q32@?<v@?@\"_OSInactivityPredictorOutput\"@\"NSError\">40"
+ "v48@0:8@\"NSDate\"16q24@\"NSPredicate\"32@?<v@?Q@\"NSError\">40"
+ "v48@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B>40"
+ "v48@0:8@\"NSDictionary\"16q24@\"NSDictionary\"32@?<v@?@@\"NSError\">40"
+ "v48@0:8@\"NSFileHandle\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSFileHandle\"16@\"NSURL\"24@\"NSData\"32@?<v@?@\"UASharedPasteboardInfo\"@\"NSError\">40"
+ "v48@0:8@\"NSFileHandle\"16@\"NSUUID\"24Q32@?<v@?@\"HKClinicalIngestionOutcome\"@\"NSError\">40"
+ "v48@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40"
+ "v48@0:8@\"NSNumber\"16@\"RPRemoteDisplayDevice\"24@\"NSNumber\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSPredicate\"16Q24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16@\"HKQuerySubscriptionAnchor\"24@\"NSNumber\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16@\"IDSURI\"24@\"IDSOffGridDeliveryHandlesDonationOptions\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16@\"IDSURI\"24@\"NSDictionary\"32@?<v@?@\"NSSet\"@\"IDSURI\"@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16@\"NSDate\"24@\"NSData\"32@?<v@?@\"NSDictionary\">40"
+ "v48@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32@?<v@?@\"NSDictionary\">40"
+ "v48@0:8@\"NSSet\"16@\"NSSet\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16@\"NSSet\"24@\"NSUUID\"32@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16@\"NSString\"24q32@?<v@?q>40"
+ "v48@0:8@\"NSSet\"16@\"NSURL\"24@\"MADEmbeddingFetchOptions\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSSet\"16q24@\"NSPredicate\"32@?<v@?Q@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"CERuleConfiguration\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"CKDiscretionaryOptions\"24@\"CKOperationCallbackProxyEndpoint\"32@?<v@?>40"
+ "v48@0:8@\"NSString\"16@\"FSTaskOptionsBundle\"24@\"FSMessageConnection\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSArray\"24@\"NSArray\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSObject\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSString\"@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSDate\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSDictionary\"24d32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"<BRFileProviderExtensionBackChannel>\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"ASCLockup\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"FPCTLTermDumper\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?>40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"TCSmartRepliesResponse\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSError\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@?<v@?@\"HAHDPinnedContentState\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDate\"40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"ASPasskeyCredentialRequest\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"PKPeerPaymentProfileAppearanceData\"32@?<v@?B>40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24B32B36@?<v@?@\"NSError\"@\"NSData\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@\"NSString\"16Q24@\"ICClientInfo\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16Q24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16Q24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSString\"16d24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16q24@\"NSNumber\"32@?<v@?@@\"NSError\">40"
+ "v48@0:8@\"NSString\"16q24@\"NSPredicate\"32@?<v@?Q@\"NSError\">40"
+ "v48@0:8@\"NSString\"16q24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16q24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSString\"16q24q32@?<v@?>40"
+ "v48@0:8@\"NSString\"16q24q32@?<v@?@\"CPLLibraryShareScopeChange\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16q24q32@?<v@?@\"NSArray\">40"
+ "v48@0:8@\"NSString\"16r^{?=[8I]}24q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16{CGSize=dd}24@?<v@?@\"AKIconContext\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16{CGSize=dd}24@?<v@?B>40"
+ "v48@0:8@\"NSString<TRIFactorPackId>\"16@\"NSString\"24@\"TRIRolloutDeployment\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSData\"32@?<v@?Q>40"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">40"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">40"
+ "v48@0:8@\"NSURL\"16@\"PRSDataStoreArchiveConfiguration\"24@\"NSData\"32o^@40"
+ "v48@0:8@\"NSUUID\"16@\"NSDate\"24@\"NSDate\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSDate\"24Q32@?<v@?@\"HKCodableLocationCoordinateSeries\"@\"NSError\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSDateInterval\"24Q32@?<v@?@\"HKCodableLocationCoordinateSeries\"@\"NSError\">40"
+ "v48@0:8@\"NSUUID\"16@\"W5Peer\"24q32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"OTControlArguments\"16@\"NSUUID\"24@\"OTInheritanceKey\"32@?<v@?@\"OTInheritanceKey\"@\"NSError\">40"
+ "v48@0:8@\"PCHomeKitIdentifier\"16@\"PCMediaRemoteIdentifier\"24@\"NSOrderedSet\"32@\"PCDisambiguationContext\"40"
+ "v48@0:8@\"PKAccountAction\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"PKAccount\"@\"NSError\">40"
+ "v48@0:8@\"PKAccountUserNotificationSettings\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"PKAccountUser\"@\"NSError\">40"
+ "v48@0:8@\"PKAccountUserPreferences\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"PKAccountUser\"@\"NSError\">40"
+ "v48@0:8@\"PKBarcodePaymentEvent\"16@\"NSString\"24@\"NSData\"32@?<v@?>40"
+ "v48@0:8@\"PKCurrencyAmount\"16@\"PKCurrencyAmount\"24@\"NSString\"32@?<v@?@\"PKPeerPaymentRecurringPayment\">40"
+ "v48@0:8@\"PKEncryptedDataObject\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"PKPaymentTransaction\"@\"NSError\">40"
+ "v48@0:8@\"PKPartialShareInvitation\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"PKSharingMessage\"@\"PKPassShare\"@\"NSError\">40"
+ "v48@0:8@\"PKVirtualCard\"16@\"NSData\"24q32@?<v@?@\"PKVirtualCardCredentials\"@\"NSError\">40"
+ "v48@0:8@\"REMChangeToken\"16@\"NSArray\"24Q32@?<v@?@\"REMChangeSet\"@\"NSError\">40"
+ "v48@0:8@\"SKHandle\"16@\"SKHandle\"24@\"NSString\"32@?<v@?@\"SKHandleInvitability\"@\"NSError\">40"
+ "v48@0:8@\"SKHandle\"16@\"SKHandle\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"TCSmartRepliesResponse\"@\"NSError\">40"
+ "v48@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"UARPAssetTag\"16@\"NSArray\"24@\"NSXPCListenerEndpoint\"32@?<v@?B>40"
+ "v48@0:8@\"UARPAssetTag\"16@\"NSString\"24@\"NSXPCListenerEndpoint\"32@?<v@?B>40"
+ "v48@0:8@\"WBSGlobalFrameIdentifier\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"ASPasskeyCredentialRequest\">40"
+ "v48@0:8@\"_HKFilter\"16@\"HKQueryAnchor\"24Q32@?<v@?@\"NSArray\"@\"HKQueryAnchor\"@\"NSError\">40"
+ "v48@0:8@\"_HKFilter\"16Q24@\"NSArray\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16@24B32B36@40"
+ "v48@0:8@16@24B32i36@40"
+ "v48@0:8@16@24^{SpecConnectOptions=@}32d40"
+ "v48@0:8@16B24@28@36B44"
+ "v48@0:8@16Q24@32@\"NSError\"40"
+ "v48@0:8@16Q24Q32q40"
+ "v48@0:8@16S24Q28Q36S44"
+ "v48@0:8@16q24@32B40B44"
+ "v48@0:8@16{_UIUpdateTiming=QQQ}24"
+ "v48@0:8@?16B24B28@?32@?40"
+ "v48@0:8B16@\"NSString\"20@\"NSNumber\"28B36@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">40"
+ "v48@0:8B16@20@28B36@?40"
+ "v48@0:8I16@\"NSDictionary\"20B28Q32@?<v@?i>40"
+ "v48@0:8I16I20i24B28@\"NSString\"32@?<v@?i>40"
+ "v48@0:8Q16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSData\">40"
+ "v48@0:8Q16@\"NSString\"24@\"NSArray\"32@?<v@?@\"HKClinicalIngestionOutcome\"@\"NSError\">40"
+ "v48@0:8Q16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSString\"Q@\"NSData\"@\"NSError\">40"
+ "v48@0:8Q16@\"NSString\"24@\"NSString\"32@?<v@?@\"PKAccountEvent\"@\"NSError\">40"
+ "v48@0:8Q16@\"NSString\"24@\"NSString\"32Q40"
+ "v48@0:8Q16@\"NSString\"24@\"UARPAccessoryID\"32@?<v@?@\"NSError\">40"
+ "v48@0:8Q16@\"UISSlotStyle\"24@\"PBPasteButtonTag\"32@?<v@?@\"UISSlotRemoteContent\"@\"NSError\">40"
+ "v48@0:8Q16@24@32@40"
+ "v48@0:8Q16@24@32Q40"
+ "v48@0:8Q16@24C32i36@?40"
+ "v48@0:8Q16B24B28@\"NSString\"32@?<v@?@\"NSArray\"BB@\"NSError\">40"
+ "v48@0:8Q16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8Q16Q24@\"NSString\"32@?<v@?@>40"
+ "v48@0:8Q16Q24@32@?40"
+ "v48@0:8Q16f24Q28Q36I44"
+ "v48@0:8d16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
+ "v48@0:8d16Q24@32@?40"
+ "v48@0:8i16@20q28i36@40"
+ "v48@0:8q16@\"ATXUserNotification\"24Q32Q40"
+ "v48@0:8q16@\"CWFNetworkProfile\"24@\"CWFRequestParameters\"32@?<v@?@\"NSError\">40"
+ "v48@0:8q16@\"NSDictionary\"24@\"<LACContextUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8q16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8q16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
+ "v48@0:8q16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v48@0:8q16@\"NSXPCListenerEndpoint\"24@\"NSDictionary\"32@?<v@?q>40"
+ "v48@0:8q16@24@?32@?40"
+ "v48@0:8q16@24Q32Q40"
+ "v48@0:8q16B24B28@\"NSDictionary\"32@?<v@?@\"RMProviderStore\"@\"NSError\">40"
+ "v48@0:8q16Q24Q32@?<v@?@\"NIBluetoothHostTimeSyncResponse\"@\"NSError\">40"
+ "v48@0:8q16q24@\"NSUUID\"32@\"NSDate\"40"
+ "v48@0:8q16q24@32@40"
+ "v48@0:8q16q24q32@?<v@?B@\"NSError\">40"
+ "v48@0:8q16q24q32q40"
+ "v48@0:8{CGPoint=dd}16{CGPoint=dd}32"
+ "v48@0:8{CGSize=dd}16{CGSize=dd}32"
+ "v48@0:8{RNCSafeAreaViewEdges=qqqq}16"
+ "v48@?0@\"MSPSharedTripSharingIdentity\"8@\"NSArray\"16@\"NSDictionary\"24@\"NSArray\"32Q40"
+ "v48@?0@\"NSArray\"8@\"NSData\"16@\"NSData\"24@\"FPExtensionResponse\"32@\"NSError\"40"
+ "v52@0:8@\"BiometricKitIdentity\"16@\"NSDictionary\"24B32Q36@?<v@?i>44"
+ "v52@0:8@\"CKDPResponseOperationResult\"16@\"NSString\"24@32i40@?<v@?@\"NSError\">44"
+ "v52@0:8@\"NSArray\"16Q24B32@\"NSString\"36@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@\"NSData\"16@\"NSData\"24B32@\"NSSet\"36@?<v@?@\"NSError\">44"
+ "v52@0:8@\"NSData\"16@\"NSString\"24d32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@\"NSDate\"16@\"NSDate\"24Q32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@\"NSDateInterval\"16@\"NSArray\"24C32@\"NSArray\"36@?<v@?@\"IMMessageHistoryDateRangeSummary\">44"
+ "v52@0:8@\"NSDictionary\"16@\"DiagnosticDevice\"24@\"NSString\"32B40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@\"NSDictionary\"16@\"NSData\"24Q32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@\"NSDictionary\"16@\"NSDictionary\"24B32Q36@?<v@?i>44"
+ "v52@0:8@\"NSDictionary\"16I24i28B32@\"NSString\"36@?<v@?iI>44"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"FPItem\"@\"NSError\">44"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?B@\"NSError\">44"
+ "v52@0:8@\"NSString\"16@\"NSString\"24i32@\"NSError\"36@?<v@?@\"NSError\"@\"NSString\">44"
+ "v52@0:8@\"NSString\"16@\"NSString\"24q32B40@?<v@?B>44"
+ "v52@0:8@\"NSString\"16@\"NSUUID\"24@\"HKQueryServerConfiguration\"32B40@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">44"
+ "v52@0:8@\"NSString\"16B24B28B32q36@\"NSDictionary\"44"
+ "v52@0:8@\"NSString\"16I24@\"NSURL\"28@\"NSDictionary\"36@?<v@?B@\"NSError\">44"
+ "v52@0:8@\"NSString\"16Q24@\"NSString\"32i40@\"NSDictionary\"44"
+ "v52@0:8@\"NSString\"16i24q28@\"NSDictionary\"36@?<v@?q>44"
+ "v52@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32B40@?<v@?B@\"NSError\">44"
+ "v52@0:8@\"SecureBackup\"16B24@\"NSString\"28@\"SecureBackupEscrowReason\"36@?<v@?@\"SecureBackupBeginPasscodeRequestResults\"@\"NSError\">44"
+ "v52@0:8@\"THThreadNetworkBorderAgent\"16@\"THThreadNetwork\"24@\"THThreadNetworkCredentialsDataSet\"32B40@?<v@?@\"NSUUID\"@\"NSError\">44"
+ "v52@0:8@\"_ANEModel\"16@\"NSDictionary\"24@\"_ANEModelInstanceParameters\"32I40@?<v@?B@\"NSDictionary\"QQc@\"NSString\"@\"NSError\">44"
+ "v52@0:8@16@24@32i40@?44"
+ "v52@0:8@16@24B32@?36@?44"
+ "v52@0:8@16@24B32B36B40@44"
+ "v52@0:8@16@24B32Q36@?44"
+ "v52@0:8@16@24C32@36@?44"
+ "v52@0:8@16@24d32B40@?44"
+ "v52@0:8@16@24i32i36i40@?44"
+ "v52@0:8@16@24i32q36q44"
+ "v52@0:8@16@24q32B40@?44"
+ "v52@0:8@16B24@?28@?36@?44"
+ "v52@0:8@16B24B28B32q36@44"
+ "v52@0:8@16Q24@32B40@?44"
+ "v52@0:8@16Q24B32@36@44"
+ "v52@0:8B16@\"NSString\"20@\"NSString\"28@\"NSData\"36@?<v@?B>44"
+ "v52@0:8B16@\"NSString\"20@\"NSString\"28@\"NSString\"36@?<v@?@\"NSError\">44"
+ "v52@0:8B16@20@28@36@44"
+ "v52@0:8B16{CGRect={CGPoint=dd}{CGSize=dd}}20"
+ "v52@0:8C16S20@\"NSString\"24@\"NSString\"32@\"NSData\"40B48"
+ "v52@0:8I16I20^{ScalarArgsArray=[16Q]I}24@\"NSData\"32I40@?<v@?B^{ScalarArgsArray=[16Q]I}@\"NSError\">44"
+ "v52@0:8I16I20^{ScalarArgsArray=[16Q]I}24@32I40@?44"
+ "v52@0:8I16Q20@\"HALDeviceInfo\"28Q36@?<v@?@\"NSError\">44"
+ "v52@0:8I16Q20@\"NSNumber\"28Q36@?<v@?@\"NSError\">44"
+ "v52@0:8I16Q20@28Q36@?44"
+ "v52@0:8Q16@\"NSArray\"24@\"NSURL\"32i40@?<v@?@\"NSError\">44"
+ "v52@0:8Q16@24@32i40@?44"
+ "v52@0:8i16@\"NSData\"20I28I32@\"NSObject<OS_xpc_object>\"36@?<v@?@\"NSError\"I>44"
+ "v52@0:8i16@\"NSString\"20@\"NSString\"28@\"NSUUID\"36@?<v@?@\"NSUUID\"@\"NSError\">44"
+ "v52@0:8i16@\"NSURL\"20@\"NSURL\"28@\"NSURL\"36@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8i16I20@\"NSDictionary\"24B32Q36@?<v@?i>44"
+ "v52@0:8q16@\"NSString\"24@\"NSString\"32B40@?<v@?B@\"NSError\">44"
+ "v52@0:8q16Q24@\"<QLPreviewItemProvider>\"32@\"<QLPreviewControllerStateProtocol>\"40B48"
+ "v52@0:8q16Q24@32@40B48"
+ "v52@0:8{AudioComponentDescription=IIIII}16@\"NSUUID\"36@?<v@?@\"NSError\"BB@\"NSArray\"@\"NSArray\"BBiQQ>44"
+ "v52@0:8{AudioComponentDescription=IIIII}16@36@?44"
+ "v52@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@\"NSData\"36@?<v@?iI>44"
+ "v52@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@36@?44"
+ "v52@?0@\"NSArray\"8@\"NSArray\"16B24@\"NSData\"28@\"FPExtensionResponse\"36@\"NSError\"44"
+ "v52@?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFArray}{os_unfair_lock_s=I}^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?@?@?d{?=[8I]}}8q16q24^{__CFString=}32C40@?<v@?C>44"
+ "v56@0:8@\"<FPOperationClient>\"16@\"NSArray\"24{CGSize=dd}32@?<v@?>48"
+ "v56@0:8@\"<SFUnlockClientProtocol>\"16Q24@\"NSString\"32@\"NSString\"40@\"NSUUID\"48"
+ "v56@0:8@\"BCSBusinessEmailItem\"16@\"BCSBusinessEmailIdentifier\"24@\"NSUUID\"32@\"NSError\"40@?<v@?B>48"
+ "v56@0:8@\"BNPresentableIdentification\"16@\"NSNumber\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"NSArray<__BNPresentableIdentification__>\"@\"NSError\">48"
+ "v56@0:8@\"CPLResource\"16@\"NSString\"24@\"CPLResourceTransferTaskOptions\"32@\"NSString\"40@?<v@?@\"NSString\">48"
+ "v56@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTLazuliGroupChatInformation\"24@\"CTLazuliGroupChatParticipant\"32@\"CTLazuliMessageID\"40@\"CTLazuliMessageComposingIndicator\"48"
+ "v56@0:8@\"EMQuery\"16@\"<EMMessageListItemQueryResultsObserver>\"24@\"EMObjectID\"32@\"<EMMessageQueryHelperObserver_xpc>\"40@?<v@?@\"<EFCancelable>\">48"
+ "v56@0:8@\"FSResource\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32@\"FSMessageConnection\"40@?<v@?@\"NSUUID\"@\"NSError\">48"
+ "v56@0:8@\"HKQuantitySample\"16@\"HKWorkout\"24@\"HKWorkoutActivity\"32@\"NSArray\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSArray\"16@\"<HKAssociatableObject>\"24@\"<HKAssociatableObject>\"32Q40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSArray\"16@\"IOSurface\"24I32@\"NSString\"36i44@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@\"NSArray\"16@\"NSArray\"24d32@\"WFRemoteImageDrawingContext\"40@?<v@?>48"
+ "v56@0:8@\"NSArray\"16@\"NSString\"24q32q40@?<v@?@\"CPLLibraryShareScopeChange\"@\"NSError\">48"
+ "v56@0:8@\"NSArray\"16@\"SKHandle\"24@\"SKInvitationPayload\"32@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSArray\"16d24@\"W5Peer\"32@\"NSUUID\"40@?<v@?@\"NSError\"@\"NSArray\">48"
+ "v56@0:8@\"NSArray\"16d24@\"W5Peer\"32@\"NSUUID\"40@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\"@\"NSUUID\">48"
+ "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"CMLClientConfig\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSUUID\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSData\"16@\"NSDictionary\"24@\"NSSet\"32@\"NSString\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@\"NSData\"16@\"NSString\"24@\"IDSServerMessagingOptions\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSData\"16@\"NSUUID\"24@\"NSData\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSData\"16q24@\"NSString\"32@\"IDSSigningOptions\"40@\"NSString\"48"
+ "v56@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32Q40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8@\"NSDictionary\"16@\"NSUUID\"24@?<v@?q@\"CXParticipant\">32B40B44q48"
+ "v56@0:8@\"NSDictionary\"16I24@\"NSDictionary\"28B36Q40@?<v@?i>48"
+ "v56@0:8@\"NSFileHandle\"16Q24B32B36@\"NSData\"40@?<v@?i@\"NSError\">48"
+ "v56@0:8@\"NSSet\"16@\"IDSURI\"24@\"NSString\"32@\"IDSOffGridDeliveryQueryOptions\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8@\"NSSet\"16@\"NSSet\"24q32@\"NSDictionary\"40@\"NSString\"48"
+ "v56@0:8@\"NSSet\"16@\"NSString\"24@\"NSDate\"32@\"NSDate\"40@?<v@?@\"PKAccountRewardsTierSummary\">48"
+ "v56@0:8@\"NSSet\"16q24@\"NSDate\"32@\"NSDate\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"CKKSExternalKey\"24@\"CKKSExternalKey\"32@\"NSArray\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSArray\"24@\"NSObject\"32@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSDate\"24@\"NSDate\"32Q40@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSDateComponents\"24@\"NSURL\"32@\"MOXPCContext\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSDecimalNumber\"24@\"NSString\"32@\"NSString\"40@?<v@?B>48"
+ "v56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@?<v@?>48"
+ "v56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"IDSURI\"32@\"IDSURI\"40@\"NSDictionary\"48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"ASCLockup\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B>48"
+ "v56@0:8@\"NSString\"16Q24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16Q24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSString\"16Q24@\"NSString\"32@\"NSURLPromisePair\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16Q24Q32B40B44@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16Q24d32Q40@?<v@?@\"FHTransactionStatistics\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16q24@\"NSDate\"32@\"HKFeatureSettings\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8@\"NSString\"16q24B32B36q40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16r^{?=[8I]}24q32@\"NSUUID\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSString\"16{_NSRange=QQ}24@\"NSDictionary\"40@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@\"NSTextCheckingResult\"16q24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"HKSource\"@\"NSError\">48"
+ "v56@0:8@\"NSUUID\"16@\"NSString\"24B32B36q40@?<v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\">48"
+ "v56@0:8@\"NSXPCListenerEndpoint\"16@\"NSURL\"24@\"NSString\"32i40B44@?<v@?i>48"
+ "v56@0:8@\"OTControlArguments\"16@\"NSUUID\"24@\"NSData\"32@\"NSData\"40@?<v@?@\"OTInheritanceKey\"@\"NSError\">48"
+ "v56@0:8@\"PKPhysicalCardOrder\"16@\"NSString\"24@\"NSString\"32@\"PKPaymentDeviceMetadata\"40@?<v@?@\"PKApplePayTrustSignatureRequest\"@\"PKAccountWebServiceRequestPhysicalCardRequest\"@\"PKPhysicalCard\"@\"PKAccount\"@\"NSError\">48"
+ "v56@0:8@\"PKShareablePassMetadata\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"SMMessage\"16@\"NSString\"24@\"SMConversation\"32@\"NSString\"40@?<v@?@\"NSString\"B@\"NSError\">48"
+ "v56@0:8@\"TCInputContextHistory\"16@\"NSArray\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"TCSmartRepliesResponse\"@\"NSError\">48"
+ "v56@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"TCSmartReplyBaseResponseAndUserQuestionnaire\"@\"NSError\">48"
+ "v56@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"TCSmartReplyUserQuestionnaire\"@\"NSError\">48"
+ "v56@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@\"W5Peer\"16@\"NSArray\"24@\"NSDictionary\"32@\"NSUUID\"40@?<v@?@\"NSError\"@\"NSArray\">48"
+ "v56@0:8@\"_SWCServiceSpecifier\"16@\"NSURL\"24Q32@\"NSValue\"40@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@16@\"NSNumber\"24q32d40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40R@48"
+ "v56@0:8@16@24@32d40Q48"
+ "v56@0:8@16@24@32i40B44@?48"
+ "v56@0:8@16@24I32@36i44@?48"
+ "v56@0:8@16@24^B32@?40@?48"
+ "v56@0:8@16@24d32@?40@?48"
+ "v56@0:8@16@24q32@40@48"
+ "v56@0:8@16B24@28@36B44@?48"
+ "v56@0:8@16Q24B32B36@40@?48"
+ "v56@0:8@16Q24{_NSRange=QQ}32q48"
+ "v56@0:8@16q24@32@40@48"
+ "v56@0:8@16q24@32q40q48"
+ "v56@0:8@16q24d32@40@48"
+ "v56@0:8@16{UIEdgeInsets=dddd}24"
+ "v56@0:8@16{_NSRange=QQ}24@40d48"
+ "v56@0:8Q16@\"NSString\"24@\"NSDictionary\"32@\"NSDictionary\"40@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8Q16Q24Q32@40@?48"
+ "v56@0:8d16Q24@32@40@?48"
+ "v56@0:8d16Q24Q32@40@?48"
+ "v56@0:8q16@\"NSDate\"24@\"NSString\"32q40@?<v@?B@\"NSError\">48"
+ "v56@0:8q16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"PKVirtualCard\"@\"NSError\">48"
+ "v56@0:8{?=[8I]}16@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8{?=[8I]}16@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8{AudioStreamBasicDescription=dIIIIIIII}16"
+ "v56@0:8{CGPoint=dd}16{CGPoint=dd}32B48B52"
+ "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@\"<NSSecureCoding>\"48"
+ "v56@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@\"NSData\"36I44@?<v@?i@\"NSData\">48"
+ "v56@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@36I44@?48"
+ "v56@0:8{TAData=IIIIIdBB}16"
+ "v60@0:8@\"IMMessageItem\"16@\"IMMessageItem\"24@\"NSIndexSet\"32@\"NSString\"40C48@\"NSString\"52"
+ "v60@0:8@\"NSArray\"16@\"IMMessageItem\"24@\"NSString\"32@\"NSString\"40C48@\"NSString\"52"
+ "v60@0:8@\"NSArray\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40i48@?<v@?@\"NSArray\"@\"NSError\">52"
+ "v60@0:8@\"NSData\"16B24@\"NSString\"28@\"CMLPIRConfig\"36@\"CMLClientConfig\"44@?<v@?@\"NSData\"@\"NSError\">52"
+ "v60@0:8@\"NSSet\"16@\"NSArray\"24@\"NSNumber\"32@\"NSNumber\"40B48@?<v@?@\"REMGrocerySuggestions\"@\"NSError\">52"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@\"RMConfigurationUIDetails\"44@?<v@?@\"NSError\">52"
+ "v60@0:8@\"NSString\"16@\"NSString\"24B32q36@\"NSDictionary\"44@?<v@?@\"NSDictionary\">52"
+ "v60@0:8@\"NSString\"16@\"NSString\"24I32@\"NSFileHandle\"36Q44@?<v@?@\"NSError\">52"
+ "v60@0:8@\"NSString\"16@\"NSURL\"24q32@\"NSString\"40B48@?<v@?@\"NSData\"@\"NSError\">52"
+ "v60@0:8@\"NSString\"16B24B28B32q36q44@?<v@?@\"NSError\">52"
+ "v60@0:8@\"NSString\"16Q24@\"NSString\"32@\"NSString\"40B48@?<v@?@\"NDODeviceInfo\">52"
+ "v60@0:8@\"NSString\"16i24i28i32@\"NSString\"36@\"NSString\"44@?<v@?@\"NSError\">52"
+ "v60@0:8@\"NSString\"16{?=[8I]}24B56"
+ "v60@0:8@\"RVQuery\"16B24B28B32q36d44B52B56"
+ "v60@0:8@16@24@32B40@44@52"
+ "v60@0:8@16@24B32q36@44@?52"
+ "v60@0:8@16@24q32@40B48@?52"
+ "v60@0:8@16@24q32B40@44@?52"
+ "v60@0:8@16@24{_NSRange=QQ}32@48B56"
+ "v60@0:8@16B24B28B32q36d44B52B56"
+ "v60@0:8@16C24C28C32C36S40@44R@52"
+ "v60@0:8@16Q24@32@40B48@?52"
+ "v60@0:8@16Q24@32B40@44@52"
+ "v60@0:8@16q24q32q40B48q52"
+ "v60@0:8@?16@24@32i40i44B48@52"
+ "v60@0:8B16@\"NSString\"20@\"NSUUID\"28@\"PKUnifiedAccessHomeAuxiliaryCapabilityDescriptor\"36@\"PKAliroHomeAuxiliaryCapabilityDescriptor\"44@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">52"
+ "v60@0:8B16@20q28@36@44@?52"
+ "v60@0:8I16I20d24I32@\"Core_Audio_XPC_Raw_Transporter\"36@\"Core_Audio_XPC_Raw_Transporter\"44@?<v@?i>52"
+ "v60@0:8Q16@\"NSString\"24@\"AFSpeechPackage\"32@\"NSString\"40B48@?<v@?BB@\"NSArray\">52"
+ "v60@0:8i16@20@28Q36@44@?52"
+ "v60@0:8i16{?=[8I]}20@\"NSString\"52"
+ "v60@0:8i16{CGSize=dd}20@36@\"NSDictionary\"44@?<v@?@\"CGBitmapFormat\"@\"NSData\">52"
+ "v60@0:8i16{CGSize=dd}20@36@44@?52"
+ "v60@0:8{?=[8I]}16I48@?52"
+ "v60@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48@?52"
+ "v60@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48@?<v@?@\"NSArray\">52"
+ "v60@0:8{CLLocationCoordinate2D=dd}16d32i40B44B48@?<v@?@\"NSArray\">52"
+ "v60@0:8{Driver_Property_Identity=Ii{AudioObjectPropertyAddress=III}}16@\"NSData\"36@\"NSData\"44@?<v@?i>52"
+ "v64@0:8@\"BMDSL\"16@\"NSString\"24@\"NSString\"32Q40@\"NSArray\"48@?<v@?B@\"NSError\">56"
+ "v64@0:8@\"BMDSL\"16@\"NSString\"24@\"NSString\"32Q40q48@?<v@?B@\"NSError\">56"
+ "v64@0:8@\"NSArray\"16@\"IOSurface\"24I32@\"NSString\"36@\"NSURL\"44i52@?<v@?@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48@?<v@?@\"NSData\"@\"NSError\">56"
+ "v64@0:8@\"NSArray\"16@\"UISSlotStyle\"24d32Q40Q48@?<v@?@\"UISSlotRemoteContent\">56"
+ "v64@0:8@\"NSArray\"16Q24Q32@\"CMLPECConfig\"40@\"CMLClientConfig\"48@?<v@?@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"IDSURI\"40@\"IDSURI\"48@\"NSDictionary\"56"
+ "v64@0:8@\"NSDate\"16@\"NSDate\"24@\"NSSet\"32@\"NSString\"40C48I52@?<v@?@\"SGXPCResponse1\">56"
+ "v64@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32@\"IDSURI\"40@\"IDSURI\"48@\"NSDictionary\"56"
+ "v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36B44i48B52@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSDictionary\"16i24@\"NSFileHandle\"28Q36i44@\"NSData\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSURL\"32@\"NSString\"40Q48@?<v@?C>56"
+ "v64@0:8@\"NSPredicate\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSURL\"40@\"NSNumber\"48@?<v@?@\"NSURL\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSDate\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSDictionary\">56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSUUID\"48@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSUUID\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24d32d40@\"NSArray\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"<_TtP18SiriSuggestionsAPI15XPCClientBridge_>\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSDate\"32@\"NSDate\"40@\"NSTimeZone\"48@?<v@?@\"PKAccountExportedTransactionInfo\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@\"NSNumber\"48@?<v@?@\"NSNumber\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSDictionary\"@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24Q32Q40@48@?<v@?@\"NSArray\"@@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24Q32q40@\"WBSTrialSearchParameters\"48@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"UISSlotStyle\"24d32Q40Q48@?<v@?@\"UISSlotRemoteContent\">56"
+ "v64@0:8@\"NSString\"16Q24Q32Q40@\"NSString\"48@?<v@?B>56"
+ "v64@0:8@\"NSString\"16Q24d32q40d48@?<v@?QQ@\"NSError\">56"
+ "v64@0:8@\"NSString\"16{_NSRange=QQ}24@\"NSString\"40@\"NSDictionary\"48@?<v@?@\"NSString\"@\"NSError\">56"
+ "v64@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSURL\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?B>56"
+ "v64@0:8@\"PKPhysicalCardAction\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"PKPaymentDeviceMetadata\"48@?<v@?@\"PKApplePayTrustSignatureRequest\"@\"PKAccountWebServicePhysicalCardActionRequest\"@\"NSSet\"@\"PKAccount\"@\"NSError\">56"
+ "v64@0:8@\"PKShareablePassMetadata\"16@\"NSString\"24@\"NSString\"32@\"PKIdentityProvisioningAttestations\"40@\"NSData\"48@?<v@?@\"PKSecureElementPass\"@\"NSError\">56"
+ "v64@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48@?<v@?@\"TCSmartReplyUserQuestionnaire\"@\"NSError\">56"
+ "v64@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSString\"32@\"TCSmartReplyUserQuestionnaire\"40@\"NSDictionary\"48@?<v@?@\"TCSmartRepliesResponse\"@\"NSError\">56"
+ "v64@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">56"
+ "v64@0:8@\"_UISticker\"16{CGRect={CGPoint=dd}{CGSize=dd}}24@?<v@?@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@16@24@32@40@?48@?56"
+ "v64@0:8@16@24@32@40B48B52@?56"
+ "v64@0:8@16@24@32@40C48I52@?56"
+ "v64@0:8@16@24@32d40@?48@?56"
+ "v64@0:8@16@24d32Q40Q48@?56"
+ "v64@0:8@16B24B28@32@40@48@?56"
+ "v64@0:8@16Q24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@@\"NSError\">56"
+ "v64@0:8@16Q24Q32Q40@48@?56"
+ "v64@0:8@16q24@32@40@48@56"
+ "v64@0:8q16@\"NSString\"24@\"NSDictionary\"32q40@\"NSDictionary\"48@?<v@?B@\"NSError\">56"
+ "v65@?0{?=III{?=C{?=I[32C]}}}8@\"NSError\"57"
+ "v68@0:8@\"IMMessageItem\"16@\"IMMessageItem\"24q32Q40@\"NSString\"48C56@\"NSString\"60"
+ "v68@0:8@\"NSFileHandle\"16Q24@\"NSFileHandle\"32Q40@\"NSData\"48I56@?<v@?@\"NSError\">60"
+ "v68@0:8@\"NSString\"16@\"NSNumber\"24Q32@\"NSData\"40I48@\"BMAccount\"52@\"NSString\"60"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSError\"40@\"NSString\"48i56@?<v@?@\"NSError\">60"
+ "v68@0:8@16@24B32B36@40B48q52@60"
+ "v68@0:8@16@24B32Q36@44@52@?60"
+ "v68@0:8@16@24Q32@40I48@52@60"
+ "v68@0:8@16B24B28@32@40B48B52@56B64"
+ "v68@0:8@16Q24@\"NSNumber\"32@\"NSNumber\"40@\"NSDictionary\"48B56@?<v@?@\"NSError\">60"
+ "v68@0:8B16@20{?=[8I]}28B60B64"
+ "v68@0:8{?=[8I]}16@\"NSString\"48B56@?<v@?@\"NSError\">60"
+ "v68@?0@\"NSError\"8B16B20@\"NSArray\"24@\"NSArray\"32B40B44i48Q52Q60"
+ "v72@0:8@\"<NSFilePresenterXPCInterface>\"16@\"NSString\"24@\"NSURL\"32@\"NSNumber\"40@\"NSSet\"48Q56Q64"
+ "v72@0:8@\"<NSFileProviderXPCInterface>\"16@\"NSString\"24@\"NSUUID\"32@\"NSURL\"40Q48@\"NSXPCListenerEndpoint\"56@?<v@?B>64"
+ "v72@0:8@\"FSResource\"16@\"NSString\"24{?=[8I]}32@?<v@?@\"FSProbeResult\"@\"NSError\">64"
+ "v72@0:8@\"NSArray\"16@\"HKDevice\"24@\"NSDictionary\"32Q40@\"NSUUID\"48@\"NSUUID\"56@?<v@?B@\"NSError\">64"
+ "v72@0:8@\"NSArray\"16@\"NSArray\"24{CGRect={CGPoint=dd}{CGSize=dd}}32@?<v@?i>64"
+ "v72@0:8@\"NSArray\"16@\"NSString\"24{?=[8I]}32@?<v@?B@\"NSError\">64"
+ "v72@0:8@\"NSData\"16@\"NSData\"24q32@\"NSString\"40@\"IDSURI\"48@\"IDSSigningOptions\"56@\"NSString\"64"
+ "v72@0:8@\"NSData\"16@\"NSString\"24@\"NSSet\"32@\"NSDictionary\"40@\"NSData\"48@\"NSString\"56@?<v@?@\"NSData\"@\"NSError\">64"
+ "v72@0:8@\"NSData\"16@\"NSUUID\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSUUID\"56@?<v@?@\"<_TtP19PrivateCloudCompute28TC2XPCTrustedRequestProtocol_>\"@\"NSData\">64"
+ "v72@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSURI\"48@\"IDSURI\"56@\"NSDictionary\"64"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSArray\"48@\"NSArray\"56@\"NSArray\"64"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@?<v@?@\"NSDictionary\"@\"NSArray\"@\"NSError\">64"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40Q48@\"WFWorkflowReference\"56@?<v@?@\"WFDeletionAuthorizationState\"@\"NSError\">64"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@\"NSString\"48q56@?<v@?B@\"NSError\">64"
+ "v72@0:8@\"NSString\"16d24@\"NSString\"32B40B44@\"NSString\"48d56Q64"
+ "v72@0:8@\"NSURL\"16@\"NSURL\"24@\"NSURL\"32@\"NSString\"40@\"NSString\"48Q56@?<v@?@\"NSError\"@\"NSDictionary\"QQQQQ@\"NSString\"@\"NSString\"@\"NSString\"@\"NSURL\">64"
+ "v72@0:8@\"NSUUID\"16@\"NSDate\"24@\"NSDate\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSString\"56@?<v@?B@\"NSError\">64"
+ "v72@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSUUID\"32@\"NSUUID\"40@\"NSArray\"48@\"NSArray\"56@?<v@?B@\"NSError\">64"
+ "v72@0:8@\"OTControlArguments\"16q24@\"NSString\"32@\"NSString\"40B48@\"OTAccountSettings\"52B60@?<v@?@\"NSError\">64"
+ "v72@0:8@\"SMMessage\"16@\"NSString\"24@\"NSString\"32@\"NSDate\"40@\"SMConversation\"48@\"NSString\"56@?<v@?@\"NSString\"B@\"NSError\">64"
+ "v72@0:8@\"TCInputContextHistory\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"TCSmartReplyUserQuestionnaire\"48@\"NSDictionary\"56@?<v@?@\"TCSmartRepliesResponse\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48Q56@?64"
+ "v72@0:8@16@24@32@40Q48Q56@?64"
+ "v72@0:8@16@24@32@40d48@?56@?64"
+ "v72@0:8@16@24@32Q40@48@56@?64"
+ "v72@0:8@16@24@32q40q48q56d64"
+ "v72@0:8@16@24B32@36@44B52@56@64"
+ "v72@0:8@16@24d32d40i48i52d56@?64"
+ "v72@0:8@16@24q32@40@48@56@64"
+ "v72@0:8@16Q24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSDictionary\"56@?<v@?@@\"NSError\">64"
+ "v72@0:8^{__CFArray=}16@24{?=[8I]}32^B64"
+ "v72@0:8q16@\"NSDate\"24@\"NSArray\"32@\"NSString\"40@\"NSString\"48@\"NSData\"56@?<v@?B@\"NSError\">64"
+ "v72@0:8q16q24d32@\"NSArray\"40d48q56d64"
+ "v72@0:8q16q24d32@40d48q56d64"
+ "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSError\"40@\"NSString\"48i56@\"NSString\"60@?<v@?@\"NSError\">68"
+ "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48B56@\"NSArray\"60@?<v@?@\"NSError\">68"
+ "v76@0:8@\"NSString\"16@\"NSUUID\"24@\"BKSHIDEventAuthenticationMessage\"32Q40@\"NSSet\"48B56q60@?<v@?@\"NSDictionary\"@\"NSError\">68"
+ "v76@0:8@16@24@32Q40@48B56q60@?68"
+ "v76@0:8B16@\"NSString\"20@\"NSString\"28@\"NSData\"36@\"NSData\"44@\"NSString\"52@\"NSData\"60@?<v@?@\"NSData\"@\"NSError\">68"
+ "v800@?0{CLVehicleConnection=dd[256c][256c][256c]d}8"
+ "v80@0:8@\"FSResource\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32{?=[8I]}40@?<v@?@\"NSArray\"@\"NSError\">72"
+ "v80@0:8@\"FSResource\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32{?=[8I]}40@?<v@?@\"NSError\">72"
+ "v80@0:8@\"FSVolumeIdentifier\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32{?=[8I]}40@?<v@?@\"NSError\">72"
+ "v80@0:8@\"FSVolumeIdentifier\"16@\"NSString\"24Q32{?=[8I]}40@?<v@?@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"FSTaskOptionsBundle\"24{?=[8I]}32@\"FSMessageConnection\"64@?<v@?@\"NSUUID\"@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"NSArray\"24@\"UISSlotStyle\"32@\"SLDImageSymbolConfiguration\"40d48q56Q64@?<v@?@\"UISSlotRemoteContent\">72"
+ "v80@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSString\"56@\"NSString\"64@?<v@?@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDate\"40@\"NSDate\"48@\"NSTimeZone\"56@\"NSString\"64@?<v@?@\"NSDictionary\"@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDate\"48@\"NSString\"56@\"NSString\"64@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56Q64@?<v@?C@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40d48d56d64@?<v@?>72"
+ "v80@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@\"NSArray\"68B76"
+ "v80@0:8@\"NSString\"16d24d32d40i48i52@\"NSString\"56@\"NSString\"64@?<v@?@\"NSError\">72"
+ "v80@0:8@\"NSString\"16i24i28@\"NSString\"32@\"NSString\"40d48d56@\"NSArray\"64@?<v@?@\"NSNumber\">72"
+ "v80@0:8@\"NSString\"16i24i28@\"NSString\"32@\"NSString\"40d48d56@\"NSArray\"64@?<v@?@\"NSNumber\"BBB>72"
+ "v80@0:8@\"PKPeerPaymentAccount\"16@\"PKCurrencyAmount\"24Q32@\"NSString\"40@\"NSNumber\"48@\"NSString\"56@\"NSString\"64@?<v@?B>72"
+ "v80@0:8@\"TPSpecificUser\"16q24@\"NSString\"32@\"NSString\"40B48B52B56B60q64@?<v@?@\"NSError\">72"
+ "v80@0:8@16@24@32@40@48@56@?64@?72"
+ "v80@0:8@16@24@32Q40@48q56@64@?72"
+ "v80@0:8@16@24C32@36@44@52@60@68B76"
+ "v80@0:8@16@24q32@40@48@56@64@72"
+ "v80@0:8@16Q24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@56@\"NSNumber\"64@?<v@?@@\"NSError\">72"
+ "v80@0:8@16d24@32d40@48d56@?64@?72"
+ "v80@0:8Q16@24@32{?=[8I]}40@?72"
+ "v80@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40@\"NSString\"48d56d64@\"ATXCustomIntentDescription\"72"
+ "v84@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48@\"NSString\"56i64@\"NSString\"68@?<v@?@\"NSError\">76"
+ "v84@0:8q16q24d32@\"NSArray\"40d48@\"NSString\"56q64d72B80"
+ "v88@0:8@\"FSResource\"16@\"NSString\"24@\"FSTaskOptionsBundle\"32{?=[8I]}40@\"FSMessageConnection\"72@?<v@?@\"NSUUID\"@\"NSError\">80"
+ "v88@0:8@\"NSString\"16@\"NSDate\"24@\"NSDate\"32@\"NSString\"40@\"NSString\"48@\"NSTimeZone\"56q64@\"NSString\"72@?<v@?@\"NSDictionary\">80"
+ "v88@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSArray\"32@\"NSArray\"40I48B52@\"NSDictionary\"56Q64Q72@\"NSString\"80"
+ "v88@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDate\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@?<v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\">80"
+ "v88@0:8@\"NSString\"16d24@\"NSString\"32B40B44@\"NSString\"48d56@\"NSString\"64d72Q80"
+ "v88@0:8@\"NSUUID\"16@\"NSArray\"24@\"NSData\"32{CGRect={CGPoint=dd}{CGSize=dd}}40i72q76B84"
+ "v88@0:8@\"OTControlArguments\"16@\"OTJoiningConfiguration\"24@\"NSString\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSData\"64@\"NSString\"72@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">80"
+ "v88@0:8@\"PKPaymentRequest\"16B24@\"NSString\"28@\"NSString\"36@\"NSString\"44@\"NSNumber\"52B60@\"NSString\"64@\"NSData\"72@?<v@?B@\"NSError\">80"
+ "v88@0:8@16@24@32@40@48@56B64@68@76B84"
+ "v88@0:8@16@24@32@40I48B52@56Q64Q72@80"
+ "v88@0:8@16@24@32{CGRect={CGPoint=dd}{CGSize=dd}}40i72q76B84"
+ "v88@0:8@16B24@28@36@44@52B60@64@72@?80"
+ "v88@0:8@16Q24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSDictionary\"72@?<v@?>80"
+ "v88@0:8Q16{?=[8I]}24I56@\"NSString\"60@\"NSString\"68I76@?<v@?@\"NSError\"I@\"NSObject<OS_xpc_object>\"II>80"
+ "v88@0:8Q16{?=[8I]}24I56@60@68I76@?80"
+ "v88@0:8q16@\"NSDate\"24@\"NSString\"32q40@\"NSArray\"48@\"NSString\"56@\"NSString\"64@\"NSData\"72@?<v@?B@\"NSError\">80"
+ "v88@?0@\"<GKAccountService>\"8@\"<GKProfileService>\"16@\"<GKFriendService>\"24@\"<GKGameService>\"32@\"<GKGameStatService>\"40@\"<GKChallengeService>\"48@\"<GKMultiplayerService>\"56@\"<GKTurnBasedService>\"64@\"<GKUtilityService>\"72@\"<GKBulletinService>\"80"
+ "v92@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40q44q52@\"NSString\"60B68q72B80@?<v@?B@\"NSError\">84"
+ "v96@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40Q48@\"NSArray\"56@\"NSString\"64@\"NSString\"72@\"NSArray\"80@?<v@?@\"NSArray\"@\"NSError\">88"
+ "v96@0:8{AltitudeUpdateData=ddddiBB{BaroBiasEstimate=ddddd}}16"
+ "v96@?0@\"NSError\"8@\"<GKAccountServicePrivate>\"16@\"<GKProfileServicePrivate>\"24@\"<GKFriendServicePrivate>\"32@\"<GKGameServicePrivate>\"40@\"<GKGameStatServicePrivate>\"48@\"<GKChallengeServicePrivate>\"56@\"<GKMultiplayerServicePrivate>\"64@\"<GKTurnBasedServicePrivate>\"72@\"<GKUtilityServicePrivate>\"80@\"<GKBulletinServicePrivate>\"88"
+ "v96@?0@\"NSError\"8@\"NSDictionary\"16Q24Q32Q40Q48Q56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSURL\"88"
+ "v@?@\"<AMSDPaymentConfirmationInterface>\"@\"NSError\""
+ "v@?@\"<AMSFraudReportServiceInterface>\"@\"NSError\""
+ "v@?@\"<AMSPaymentValidationServiceInterface>\"@\"NSError\""
+ "v@?@\"<ASCAppOfferStateService>\"@\"NSError\""
+ "v@?@\"<ASCCredentialProtocol>\"@\"NSError\""
+ "v@?@\"<ASCLockupFetcherService>\"@\"NSError\""
+ "v@?@\"<ASCMetricsService>\"@\"NSError\""
+ "v@?@\"<ASCUtilityService>\"@\"NSError\""
+ "v@?@\"<ASDAppMetricsServiceProtocol><NSXPCProxyCreating>\"@\"NSError\""
+ "v@?@\"<ASDAppStoreServiceProtocol><NSXPCProxyCreating>\"@\"NSError\""
+ "v@?@\"<ASDRestoreServiceProtocol><NSXPCProxyCreating>\"@\"NSError\""
+ "v@?@\"<ATXUICacheProtocol>\""
+ "v@?@\"<BRItemNotificationSending><NSXPCProxyCreating>\"@\"NSDictionary\"@\"NSError\""
+ "v@?@\"<CGRemotePDFDocumentProtocol>\""
+ "v@?@\"<CGRemotePDFPageProtocol>\""
+ "v@?@\"<CKXPCContainerScopedDaemon>\"@\"NSError\""
+ "v@?@\"<CKXPCLogicalDeviceScopedClient>\""
+ "v@?@\"<CKXPCLogicalDeviceScopedDaemon>\""
+ "v@?@\"<CKXPCProcessScopedClient>\""
+ "v@?@\"<CKXPCProcessScopedDaemon>\""
+ "v@?@\"<EMDiagnosticInfoGathererInterface>\""
+ "v@?@\"<FPIndexingAssertion>\"@\"NSError\""
+ "v@?@\"<GCAdaptiveTriggersXPCProxyRemoteServerEndpointInterface>\"@\"NSError\""
+ "v@?@\"<GCAdaptiveTriggersXPCProxyServiceRemoteServerInterface>\"@\"NSError\""
+ "v@?@\"<GCGameIntentXPCProxyRemoteServerEndpointInterface>\"@\"NSError\""
+ "v@?@\"<GCGameIntentXPCProxyServiceRemoteServerInterface>\"@\"NSError\""
+ "v@?@\"<GKAccountService>\"@\"<GKProfileService>\"@\"<GKFriendService>\"@\"<GKGameService>\"@\"<GKGameStatService>\"@\"<GKChallengeService>\"@\"<GKMultiplayerService>\"@\"<GKTurnBasedService>\"@\"<GKUtilityService>\"@\"<GKBulletinService>\""
+ "v@?@\"<IDSXPCBAASigner>\"@\"NSError\""
+ "v@?@\"<IDSXPCEventReporting>\"@\"NSError\""
+ "v@?@\"<IDSXPCOffGridMessenger>\"@\"NSError\""
+ "v@?@\"<IDSXPCOffGridStateManager>\"@\"NSError\""
+ "v@?@\"<IDSXPCPinnedIdentity>\"@\"NSError\""
+ "v@?@\"<IDSXPCServerMessaging>\"@\"NSError\""
+ "v@?@\"<PKPushablePassConfigurationProvider>\"@\"NSError\""
+ "v@?@\"<PLAssetsdNonBindingDebugServiceProtocol>\"@\"NSError\""
+ "v@?@\"<TUScreenShareAttributes>\""
+ "v@?@\"<WBSHistoryImporterDelegate>\"@\"NSError\""
+ "v@?@\"<_TtP19PrivateCloudCompute28TC2XPCTrustedRequestProtocol_>\"@\"NSData\""
+ "v@?@\"AAAttributionResult\""
+ "v@?@\"AAURLConfiguration\"@\"NSHTTPURLResponse\"@\"NSError\""
+ "v@?@\"AFHomeAccessoryInfo\""
+ "v@?@\"AFPeerInfo\"@\"NSArray\""
+ "v@?@\"AFSetAudioSessionActiveResult\""
+ "v@?@\"AKBeneficiaryManifest\"@\"NSError\""
+ "v@?@\"AKCustodianSetupResult\"@\"NSError\""
+ "v@?@\"AKIconContext\"@\"NSError\""
+ "v@?@\"AKInheritanceAccessKey\"@\"NSError\""
+ "v@?@\"AKSignInWithAppleAccount\"@\"NSError\""
+ "v@?@\"AKTrustedContactsSyncResult\"@\"NSError\""
+ "v@?@\"AMSBiometricsSignatureResult\"@\"NSError\""
+ "v@?@\"AMSFraudReportResponse\"@\"NSError\""
+ "v@?@\"APClientState\"@\"NSError\""
+ "v@?@\"APPerAppManagedProtectability\"@\"NSError\""
+ "v@?@\"ASCLockup\"@\"NSError\""
+ "v@?@\"ATXFaceGalleryConfiguration\"@\"NSDate\"@\"NSError\""
+ "v@?@\"ATXFaceGalleryConfiguration\"@\"NSError\""
+ "v@?@\"ATXMailContextResponse\"@\"NSError\""
+ "v@?@\"ATXMessageContextResponse\"@\"NSError\""
+ "v@?@\"ATXNotificationCategorizationFeatureCollectionSet\"@\"NSError\""
+ "v@?@\"ATXNotificationContextResponse\"@\"NSError\""
+ "v@?@\"ATXNotificationRankingResult\"@\"NSError\""
+ "v@?@\"ATXSettingsActionsClientResponse\"@\"NSError\""
+ "v@?@\"ATXSportsResponse\"@\"NSError\""
+ "v@?@\"BCSBusinessLogo\"@\"NSError\""
+ "v@?@\"BMResourceContainer\"@\"NSString\"@\"NSData\"@\"NSError\""
+ "v@?@\"BSAction\"@\"NSArray<__ATXInfoTimelineEntry__>\"@\"NSError\""
+ "v@?@\"BSAction\"@\"NSError\""
+ "v@?@\"CERuleConfiguration\"@\"NSError\""
+ "v@?@\"CESRModelProperties\"@\"NSError\""
+ "v@?@\"CEServerRecommendations\"@\"NSError\""
+ "v@?@\"CGBitmapFormat\"@\"NSData\""
+ "v@?@\"CHSControlConfigurationHostsBox\"@\"NSError\""
+ "v@?@\"CHSControlDescriptor\"@\"NSError\""
+ "v@?@\"CHSTimelineEntryRelevanceBox\"@\"BSAction\"@\"NSError\""
+ "v@?@\"CHSWidgetConfigurationHostsBox\"@\"NSError\""
+ "v@?@\"CHSynthesisResult\"@\"NSError\""
+ "v@?@\"CHSynthesisStyleInventoryStatus\"@\"NSError\""
+ "v@?@\"CKContextResponse\"@\"NSError\""
+ "v@?@\"CKKSExternalKey\"@\"NSArray\"@\"NSArray\"@\"NSError\""
+ "v@?@\"CLLocation\""
+ "v@?@\"CLLocation\"@\"NSError\""
+ "v@?@\"CNApplicationProxy\"@\"NSError\""
+ "v@?@\"CNChangeHistoryAnchor\"@\"NSError\""
+ "v@?@\"CNLimitedAccessSyncData\"@\"NSError\""
+ "v@?@\"CPLLibraryShareScopeChange\"@\"NSError\""
+ "v@?@\"CTPrivateNetworkCapabilities\"@\"NSError\""
+ "v@?@\"CTPrivateNetworkSimInfo\"@\"NSError\""
+ "v@?@\"CTSatelliteMessagingProvisioning\"@\"NSError\""
+ "v@?@\"CTTrafficDescriptorsContainer\"@\"NSError\""
+ "v@?@\"CTTransportKeysUpdate\"@\"NSError\""
+ "v@?@\"CTXPCResponseMessage\"@\"NSError\""
+ "v@?@\"CloudFeature\"@\"NSError\""
+ "v@?@\"DCCredentialCryptoKey\"@\"NSError\""
+ "v@?@\"DCCredentialProperties\"@\"NSError\""
+ "v@?@\"DIDeviceHandle\"@\"NSError\""
+ "v@?@\"DNDAppInfo\"@\"NSError\""
+ "v@?@\"DNDModeConfiguration\"@\"NSError\""
+ "v@?@\"DUPersonalIDResult\"@\"NSError\""
+ "v@?@\"DiagnosticDevice\""
+ "v@?@\"FHFeaturesResponse\"@\"NSError\""
+ "v@?@\"FHTransactionStatistics\"@\"NSError\""
+ "v@?@\"FMDActivationLockInfo\"@\"NSError\""
+ "v@?@\"FPItem\"@\"NSArray\"@\"NSError\""
+ "v@?@\"FPSandboxingURLWrapper\"@\"NSData\"@\"NSError\""
+ "v@?@\"GDEntityResolutionResult\"@\"NSError\""
+ "v@?@\"GDKnosisResult\"@\"NSError\""
+ "v@?@\"GKGameActivityInternal\""
+ "v@?@\"GKGameSettingsInternal\"@\"NSError\""
+ "v@?@\"HAHDPinnedContentState\"@\"NSError\""
+ "v@?@\"HDHRSSignedClinicalDataProcessingContextCollection\"@\"NSError\""
+ "v@?@\"HKClinicalIngestionOutcome\"@\"NSError\""
+ "v@?@\"HKDatabaseAccessibilityAssertion\"@\"NSError\""
+ "v@?@\"HKFeatureAvailabilityOnboardingEligibility\"@\"NSError\""
+ "v@?@\"HKFeatureAvailabilityRequirementSet\"@\"NSError\""
+ "v@?@\"HKFeatureOnboardingRecord\"@\"NSError\""
+ "v@?@\"HKMCExperienceModel\"@\"NSError\""
+ "v@?@\"HKMobilityWalkingSteadinessNotificationStatus\"@\"NSError\""
+ "v@?@\"HKMobilityWalkingSteadinessOnboardingStatus\"@\"NSError\""
+ "v@?@\"HKQuantity\"@\"NSError\""
+ "v@?@\"HKRegionAvailability\"@\"NSError\""
+ "v@?@\"HKSPSleepScheduleModel\"@\"NSError\""
+ "v@?@\"HKSharedSummaryTransaction\"@\"NSError\""
+ "v@?@\"IDSOffGridEncryptedMessage\"@\"NSString\"@\"NSError\""
+ "v@?@\"IDSOffGridMessage\"@\"NSString\"@\"NSError\""
+ "v@?@\"IDSPinnedIdentity\"@\"NSError\""
+ "v@?@\"INIntent\"@\"NSError\""
+ "v@?@\"ISGenerationResponse\""
+ "v@?@\"ISIconCacheConfiguration\""
+ "v@?@\"LACDTORatchetState\"@\"NSError\""
+ "v@?@\"LACEnvironmentState\"@\"NSError\""
+ "v@?@\"LNActionMetadata\"@\"NSError\""
+ "v@?@\"LNAsyncIteratorReference\"@\"NSError\""
+ "v@?@\"LNConnectionListenerEndpoint\"@\"NSError\""
+ "v@?@\"LNEntityMetadata\"@\"NSError\""
+ "v@?@\"LNEnumMetadata\"@\"NSError\""
+ "v@?@\"LNOpenURLResponse\"@\"NSError\""
+ "v@?@\"LNQueryMetadata\"@\"NSError\""
+ "v@?@\"LPLinkMetadata\"@\"NSError\""
+ "v@?@\"LSDefaultApplicationQueryResult\"@\"NSError\""
+ "v@?@\"LSExtensionPointRecord\""
+ "v@?@\"MCCSigningAndEncryptionMessagesStatus\"@\"NSError\""
+ "v@?@\"MCResourceStatus\"@\"NSError\""
+ "v@?@\"MLRTaskResult\"@\"NSError\""
+ "v@?@\"MOSuggestionAssetsArrayTransport\"@\"NSError\""
+ "v@?@\"MOSuggestionAssetsBundle\"@\"NSError\""
+ "v@?@\"MRAVRoutingDiscoverySessionConfiguration\""
+ "v@?@\"MSPSharedTripSharingIdentity\"@\"NSArray\"@\"NSDictionary\"@\"NSArray\"Q"
+ "v@?@\"MTAlarm\"@\"NSError\""
+ "v@?@\"NDODevice\""
+ "v@?@\"NDODeviceInfo\""
+ "v@?@\"NEVirtualInterfaceParameters\""
+ "v@?@\"NFAssertionInternal\"@\"NSError\""
+ "v@?@\"NIBluetoothHostTimeSyncResponse\"@\"NSError\""
+ "v@?@\"NRMutableDeviceCollection\"@\"NRSecureDevicePropertyStore\"QB"
+ "v@?@\"NSArray\"@\"HKQueryAnchor\"@\"NSError\""
+ "v@?@\"NSArray\"@\"NSArray\"B@\"NSData\"@\"FPExtensionResponse\"@\"NSError\""
+ "v@?@\"NSArray\"@\"NSData\"@\"NSData\"@\"FPExtensionResponse\"@\"NSError\""
+ "v@?@\"NSArray\"@\"NSDate\"@\"NSError\""
+ "v@?@\"NSArray\"@\"NSError\"@\"NSDate\""
+ "v@?@\"NSArray\"@\"NSString\""
+ "v@?@\"NSArray\"@\"TrustedPeersHelperCustodianRecoveryKey\"@\"NSError\""
+ "v@?@\"NSArray\"@\"UISDActivityItemData\"@\"NSError\""
+ "v@?@\"NSArray\"@@\"NSError\""
+ "v@?@\"NSArray\"Qd@\"NSError\""
+ "v@?@\"NSArray\"q"
+ "v@?@\"NSArray<__BNPresentableIdentification__>\"@\"NSError\""
+ "v@?@\"NSArray<__CHSControlDescriptor__>\"@\"NSError\""
+ "v@?@\"NSArray<__DNDAppInfo__>\"@\"NSError\""
+ "v@?@\"NSArray<__DNDModeConfiguration__>\"@\"NSError\""
+ "v@?@\"NSArray<__DNDMode__>\"@\"NSError\""
+ "v@?@\"NSArray<__NSString__>\"@\"NSError\""
+ "v@?@\"NSArray<__NSValue__>\"@\"NSError\""
+ "v@?@\"NSArray<__PFServerPosterPath__>\"@\"NSError\""
+ "v@?@\"NSData\"@\"NSData\""
+ "v@?@\"NSData\"@\"PKSecureElementSignatureInfo\"@\"NSError\""
+ "v@?@\"NSDictionary\"@\"NSError\"@\"IDSBAASignerContext\""
+ "v@?@\"NSDictionary\"@\"SUIAutomationServiceError\""
+ "v@?@\"NSDictionary\"qq@\"NSError\""
+ "v@?@\"NSError\"@\"<GKAccountServicePrivate>\"@\"<GKProfileServicePrivate>\"@\"<GKFriendServicePrivate>\"@\"<GKGameServicePrivate>\"@\"<GKGameStatServicePrivate>\"@\"<GKChallengeServicePrivate>\"@\"<GKMultiplayerServicePrivate>\"@\"<GKTurnBasedServicePrivate>\"@\"<GKUtilityServicePrivate>\"@\"<GKBulletinServicePrivate>\""
+ "v@?@\"NSError\"@\"AUParameterTree\""
+ "v@?@\"NSError\"@\"MIDICIProfileState\""
+ "v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\"@\"NSUUID\""
+ "v@?@\"NSError\"@\"NSDictionary\"QQQQQ@\"NSString\"@\"NSString\"@\"NSString\"@\"NSURL\""
+ "v@?@\"NSError\"@\"NSIndexSet\""
+ "v@?@\"NSError\"@\"NSXPCListenerEndpoint\""
+ "v@?@\"NSError\"@\"SDMDMConfiguration\""
+ "v@?@\"NSError\"BB@\"NSArray\"@\"NSArray\"BBiQQ"
+ "v@?@\"NSMapTable\"@\"NSError\""
+ "v@?@\"NSMutableArray\"@\"NSError\""
+ "v@?@\"NSNumber\"@\"DNDModeAssertion\"@\"NSError\""
+ "v@?@\"NSNumber\"@\"NSNumber\"@\"NSError\""
+ "v@?@\"NSObject<NFCCardSessionInterface>\"B@\"NSError\""
+ "v@?@\"NSObject<NFCFieldDetectSessionInterface>\"@\"NSError\""
+ "v@?@\"NSObject<NFCredentialSessionInterface>\"B@\"NSError\""
+ "v@?@\"NSObject<NFReaderSessionInterface>\"B@\"NSError\""
+ "v@?@\"NSObject<NFSecureElementLoggingSessionInterface>\"B@\"NSError\""
+ "v@?@\"NSObject<NFSecureTransactionServicesHandoverHybridSessionInterface>\"B@\"NSError\""
+ "v@?@\"NSObject<NFSecureTransactionServicesHandoverSessionInterface>\"B@\"NSError\""
+ "v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"B@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB"
+ "v@?@\"NSSet\"@\"IDSURI\"@\"NSDictionary\"@\"NSError\""
+ "v@?@\"NSSet\"@\"MRGroupSessionInfo\""
+ "v@?@\"NSSet\"@\"NSSecurityScopedURLWrapper\"@\"NSError\""
+ "v@?@\"NSSet\"B"
+ "v@?@\"NSString\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"TPSyncingPolicy\"@\"NSString\"@\"NSArray\"@\"NSError\""
+ "v@?@\"NSString\"@\"NSURL\"@\"NSError\""
+ "v@?@\"NSString\"q@\"NSError\""
+ "v@?@\"NSURL\"@\"NSData\"@\"NSError\""
+ "v@?@\"NSURL\"@\"NSURL\""
+ "v@?@\"NSUUID\"@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\""
+ "v@?@\"NSXPCListenerEndpoint\"@\"NSData\"@\"LNAction\"@\"NSError\""
+ "v@?@\"ODDSiriSchemaODDSiriClientEvent\"@\"NSError\""
+ "v@?@\"OSLogEntry\""
+ "v@?@\"OTCurrentSecureElementIdentities\"@\"NSError\""
+ "v@?@\"OTCustodianRecoveryKey\"@\"NSError\""
+ "v@?@\"OTInheritanceKey\"@\"NSError\""
+ "v@?@\"PFPosterPathsAssertion\"@\"NSError\""
+ "v@?@\"PFServerPosterPath\"@\"NSArray<__PRSPosterUpdateResult__>\"@\"NSError\""
+ "v@?@\"PFServerPosterPath\"@\"NSError\""
+ "v@?@\"PFServerPosterPath\"@\"PFServerPosterPath\"@\"NSError\""
+ "v@?@\"PKAccountDailyCashDestinationsSummary\"@\"NSError\""
+ "v@?@\"PKAccountEnhancedMerchantBehavior\""
+ "v@?@\"PKAccountPaymentFundingSource\""
+ "v@?@\"PKAccountPromotionBehavior\""
+ "v@?@\"PKAccountRewardsTierSummary\""
+ "v@?@\"PKAccountStatementMetadata\"@\"NSError\""
+ "v@?@\"PKAccountUserInfo\"@\"NSError\""
+ "v@?@\"PKAppletSubcredential\"@\"NSError\""
+ "v@?@\"PKExpressPassConfiguration\""
+ "v@?@\"PKGroupsControllerSnapshot\""
+ "v@?@\"PKPayLaterCardMagnitudes\""
+ "v@?@\"PKPaymentOfferCatalog\""
+ "v@?@\"PKPaymentOfferCatalog\"@\"NSError\""
+ "v@?@\"PKPaymentRewardsRedemption\""
+ "v@?@\"PKPeerPaymentRecurringPayment\""
+ "v@?@\"PKPeerPaymentRecurringPayment\"@\"NSError\""
+ "v@?@\"PLCPLSettings\""
+ "v@?@\"PPSocialAttribution\"@\"NSError\""
+ "v@?@\"PRSPosterSnapshotResponse\"@\"NSError\""
+ "v@?@\"PRUISAnalysisServiceResponse\"@\"NSError\""
+ "v@?@\"PRUISSnapshotServiceResponse\"@\"NSError\""
+ "v@?@\"PVAppIdentityDigest\""
+ "v@?@\"QLThumbnailReply\"@\"NSError\""
+ "v@?@\"RMDeclarationManifest\"@\"NSError\""
+ "v@?@\"RMSubscriberStore\"@\"NSError\""
+ "v@?@\"RTPeopleDensity\"@\"NSError\""
+ "v@?@\"SDBetaProgram\"@\"NSError\""
+ "v@?@\"SDDevice\"@\"NSError\""
+ "v@?@\"SEFidoKey\"@\"NSError\""
+ "v@?@\"SESLegacyKeyCreateResponse\"@\"NSError\""
+ "v@?@\"SESLegacyKeySignResponse\"@\"NSError\""
+ "v@?@\"SFAutoUnlockNotificationModel\"@\"NSError\""
+ "v@?@\"SKHandleInvitability\"@\"NSError\""
+ "v@?@\"SKStatusSubscriptionMetadata\"@\"NSError\""
+ "v@?@\"SMLocalSessionState\"@\"NSError\""
+ "v@?@\"SMSessionManagerState\"B@\"NSError\""
+ "v@?@\"SPBeaconSharingLimits\""
+ "v@?@\"SPLocationFetchResult\"@\"NSError\""
+ "v@?@\"SPSecureLocation\"@\"NSError\""
+ "v@?@\"SPSecureLocationsStewiePublishResult\"@\"NSError\""
+ "v@?@\"SPSecureLocationsSubscriptionResult\"@\"NSError\""
+ "v@?@\"STCallingStatusDomainCallDescriptor\""
+ "v@?@\"STCommunicationConfiguration\"@\"NSError\""
+ "v@?@\"SUCoreDDMDeclaration\"@\"NSError\""
+ "v@?@\"SUCoreDDMDeclarationGlobalSettings\"@\"NSError\""
+ "v@?@\"SUIAutomationServiceError\""
+ "v@?@\"SURollbackDescriptor\"@\"NSError\""
+ "v@?@\"SUScanResults\"@\"NSError\""
+ "v@?@\"SWTransparencyExpiringVerificationResult\"@\"NSError\""
+ "v@?@\"TCSmartRepliesResponse\"@\"NSError\""
+ "v@?@\"TCTextCompositionOutput\"@\"NSError\""
+ "v@?@\"TCTextCompositionReviewOutput\"@\"NSError\""
+ "v@?@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\""
+ "v@?@\"TUCallProvider\""
+ "v@?@\"TUConversationLink\"@\"NSError\""
+ "v@?@\"TUConversationNotice\"@\"NSError\""
+ "v@?@\"TUConversationProvider\""
+ "v@?@\"TUNearbyDeviceHandle\"@\"NSError\""
+ "v@?@\"TribecaStatus\""
+ "v@?@\"UARPAssetID\""
+ "v@?@\"UISSlotRemoteContent\""
+ "v@?@\"UISSlotRemoteContent\"@\"NSError\""
+ "v@?@\"W5DiagnosticsMode\"@\"NSError\""
+ "v@?@\"WFDatabaseObjectDescriptor\"@\"NSError\""
+ "v@?@\"WFDeletionAuthorizationState\"@\"NSError\""
+ "v@?@\"WFDialogResponse\""
+ "v@?@\"WFOnScreenContent\"@\"NSError\""
+ "v@?@\"WFOnScreenContentNode\"@\"NSError\""
+ "v@?@\"WFSiriActionResponse\""
+ "v@?@\"WFSmartPromptApprovalResult\"@\"NSError\""
+ "v@?@\"WFWorkflowCollection\"@\"NSError\""
+ "v@?@\"WFWorkflowDescriptor\"@\"NSNumber\"@\"NSError\""
+ "v@?@\"WFWorkflowReference\""
+ "v@?@\"WFWorkflowRunResult\"@\"NSError\""
+ "v@?@\"WiFi3BarsResponse\"@\"NSError\""
+ "v@?@\"_EXQueryResult\"@\"NSError\""
+ "v@?@\"_EXSceneSessionConnectionResponse\"@\"NSError\""
+ "v@?@\"_LTLocaleModalities\""
+ "v@?@\"_OSChargingPredictorOutput\"@\"NSError\""
+ "v@?@\"_OSInactivityPredictorMetadata\""
+ "v@?@\"_TtC12ModelCatalog17ResourceContainer\"@\"NSError\""
+ "v@?@\"_TtC12ModelCatalog23ResourceBundleContainer\"@\"NSError\""
+ "v@?@\"_TtC12ModelCatalog28SiriResourceAvailabilityInfo\"@\"NSError\""
+ "v@?@\"_TtC13SiriAnalytics13StagingReport\"@\"NSError\""
+ "v@?@\"_TtC14CopresenceCore29PresenceSessionConnectionInfo\"@\"NSError\""
+ "v@?@\"_TtC14NearbySessions14InvitationBlob\"@\"NSError\""
+ "v@?@\"_TtC14NearbySessions22InvitationJoinResponse\"@\"NSError\""
+ "v@?@\"_TtC14NearbySessions35NearbyInvitationJoinRequestMetadata\"@\"NSError\""
+ "v@?@\"_TtC19EnergyKitFoundation12EKEnergySite\"@\"NSError\""
+ "v@?@\"_TtC31TextToSpeechVoiceBankingSupport15TTSVBBoxedError\""
+ "v@?@\"_TtC4Sage22SummarizationXPCResult\"@\"NSError\""
+ "v@?@\"_TtC9SEService11Reservation\"@\"NSError\""
+ "v@?@\"_TtC9SEService16DeviceCapability\"@\"NSError\""
+ "v@?@\"_TtC9SEService16ReservationState\"@\"NSError\""
+ "v@?B@\"PCSMTT\"@\"NSError\""
+ "v@?B@\"PKPaymentPass\"@\"NSArray\"@\"NSError\""
+ "v@?B@\"SURollbackDescriptor\"@\"NSError\""
+ "v@?B@\"_DUITargetLayerDescriptor\""
+ "v@?BB@\"NSError\"@\"NSError\""
+ "v@?B^{ScalarArgsArray=[16Q]I}@\"NSError\""
+ "v@?BqB"
+ "v@?Bqq@\"SOSButtonPressState\""
+ "v@?Q@\"NSData\"CII@\"NSError\""
+ "v@?Q@\"NSData\"I@\"NSError\""
+ "v@?QI@\"NSError\""
+ "v@?QQ@\"NSArray\"@\"NSError\""
+ "v@?iI"
+ "v@?q@\"NSArray\""
+ "v@?q@\"NSString\"@\"CKRecordID\"@\"NSError\""
+ "v@?{?=III{?=C{?=I[32C]}}}@\"NSError\""
+ "{?=[8I]}16@0:8"
+ "{?=dddddffBBB}88@0:8{?=dddddffBBB}16@72@80"
+ "{CATransform3D=dddddddddddddddd}16@0:8"
+ "{CATransform3D=dddddddddddddddd}24@0:8@16"
+ "{CGPoint=dd}48@0:8@16{CGPoint=dd}24q40"
+ "{CGSize=dd}40@0:8@16@24q32"
+ "{CLStepDistance=idddiidi}32@0:8^d16^d24"
+ "{RNCSafeAreaViewEdges=qqqq}16@0:8"
+ "{RNCSafeAreaViewEdges=qqqq}24@0:8@16"
+ "{SBSystemApertureContainerRenderingConfiguration=qqB}16@0:8"
- "!sAppConnectionForCurrentNotification"
- "!sCFNotificationCompletionBlock"
- "!sCurrentNotification"
- "%2F"
- "-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]"
- "-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke"
- "-[_CFGeneralPasteboardStore getUserApproval:withCompletion:]_block_invoke_2"
- "@24@0:8^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}16"
- "@32@0:8@16^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}24"
- "@?40@0:8^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}16q24^{?=iq^{__CFData}Q}32"
- "Allow Paste"
- "Allowing process impersonation by process %{public}s (%{public}d) despite not having the com.apple.private.defaults-impersonate entitlement due to it not being sandboxed. Please add com.apple.private.defaults-impersonate instead, this will stop working in the future."
- "Bundle: %{private}@, key: %{public}@, value: %{public}@, table: %{public}@, localizationNames: %{public}@, result: %{public}@"
- "C40@?0^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}8q16q24^{__CFString=}32"
- "C8@?0"
- "CFPasteboardSetPrevalidationCallbacks('%{public}@' (%{public}@), ...)"
- "CFPasteboardSetPrevalidationCallbacks() can only be used with kCFPasteboardGeneral. Pasteboard was: '%{public}@' (%{public}@) "
- "CFPasteboardSetPrevalidationCallbacks(NULL, ...)"
- "CFUserNotification callback wasn't for the current notification. Ignoring."
- "Caller didn't provide a proposed filename required to unique promise drag destination"
- "Canceling CFUserNotification."
- "Client died. Will cancel CFUserNotification."
- "Could not obtain paste verification entitlement for process with pid %ld. Error: %@"
- "Failed to consume destination URL sandbox extension required to unique promise drag destination"
- "Failed to consume sandbox extension from pasteboard with path: '%{private}@'"
- "Failed to creae  url: [%{private}@]"
- "Failed to get a sandbox extension"
- "Failed to get destination URL required to unique promise drag destination"
- "Failed to issue sandbox extension"
- "NSCallStackReturnAddresses"
- "No extension string for url: [%{private}@]"
- "No sandbox extension entry in cache when one was expected for item %ld flavor: %{public}@"
- "Process with pid %d denied access to sandbox extension by owner"
- "Process with pid %ld is not entitled to check in apps for paste verification."
- "Promise fufilled - %lu bytes for '%{public}@' gen: %ld of flavor: '%{public}@'"
- "Received CFUserNotification reply: shouldAllowPaste = %d"
- "Sandbox extension creation failed: client lacks entitlements? for path: [%{private}@] [%{private}s]"
- "Sandbox extension data required immediately for flavor %{public}@, but failed to obtain."
- "Showing CFUserNotification"
- "Something went wrong with the '%s' connection: %{public}s"
- "Something went wrong with the '%s' connection: %{public}s\nInvalidation reason: %{public}s"
- "Successfully promised sandbox extension data"
- "Successfully registered entries (%ld)"
- "Successfuly consumed sandbox extension"
- "TC,V_extensionConsumed"
- "T^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d},R,V_pboard"
- "Unable to get timebase info."
- "Waiting for CFUserNotification reply"
- "^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}"
- "^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}16@0:8"
- "_CFPasteboardStore couldn't load a Security symbol."
- "_asyncPromisor"
- "_cfNotificationCallback"
- "_extensionConsumed"
- "_isManagedPromiseDragForGeneration:itemIdentifier:"
- "_kCFPasteboardVerificationAlertRunLoopMode"
- "_onqueue_CFPasteboardPrecheckTokenAndShowApprovalDialogIfNecessaryForPasteboard_block_invoke_2"
- "_onqueue_handleNewEntries:forMessage:shouldInvalidateClientMetadata:"
- "_promiseState"
- "_promisor"
- "_sourceProcessID"
- "analyzeSandboxExtensionEntry:destinedForClient:"
- "extensionConsumed"
- "failed to create CFRunLoopSource"
- "failed to create a CFUserNotification: %ld"
- "filterDataFromEntry:inResponseToMessage:error:"
- "getUserApproval:withCompletion:"
- "kCFTimeZoneSystemTimeZoneDidChangeNotification-2"
- "kCFTimeZoneSystemTimeZoneDidChangeNotification-4"
- "reissueSandboxExtensionFromEntry:toClient:error:"
- "resolveClientPromisedDataWithQueue:completionHandler:"
- "resolveLocalPromisedData"
- "sApprovalDialogSemaphore"
- "sCFNotificationCompletionBlock"
- "setExtensionConsumed:"
- "v16@?0@?<v@?C>8"
- "v40@0:8@?16^{__CFPasteboard={__CFRuntimeBase=QAQ}^{__CFString}@^{__CFUUID}^{__CFArray}C@@AQCCCC^{__CFData}^{__CFDictionary}@?@?d}24q32"
- "v40@0:8^{__CFArray=}16@24^B32"
- "yyyyMMdd"
- "~{"

```
