## libGSFont.dylib

> `/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x800c
-  __TEXT.__auth_stubs: 0xae0
+137.0.0.0.0
+  __TEXT.__text: 0x82c0
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x8f2
+  __TEXT.__cstring: 0x92c
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__oslogstring: 0x15d
   __TEXT.__unwind_info: 0x218
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x6a8
-  __TEXT.__objc_stubs: 0x980
+  __TEXT.__objc_methname: 0x6b7
+  __TEXT.__objc_stubs: 0x9a0
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__cfstring: 0xb60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__bss: 0xa8
-  __DATA_DIRTY.__bss: 0x98
+  __DATA.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/FontServices.framework/FontServices
+  - /System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib
   - /System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 137
-  Symbols:   361
-  CStrings:  90
+  Functions: 138
+  Symbols:   363
+  CStrings:  58
 
Symbols:
+ _CGFontGetParserFont
+ _FPFontCopyMetadata
+ _GSFontFileDescriptorForPath
- _OSAtomicCompareAndSwapPtrBarrier
CStrings:
+ "__fetchAllAccessTokens:"
+ "_childCountInDatabaseForFolderFetchInCollection:skipCountingInDatabaseBookmarksThatAreDeletedInMemory:"
+ "_childrenExcludingExcessNodes:excludingReactors:"
+ "_discardAllCachedButtonSizes"
+ "_errorForwardingProxyForServiceProxy:proxyReplyError:interface:proxyPromise:"
+ "_loadImageIsDylib:"
+ "_logVoiceTriggerInfo:withMHUUID:"
+ "_needToGenerateModelWithType:ignoreLastGenerationTime:withExtendTimeout:"
+ "_persistContacts:"
+ "_rangeForAutocorrectionText:"
+ "_remainsActionable"
+ "_removeHubbleRequestedTransfer:"
+ "_removeRegionPredicate:"
+ "_resourceLoadStatisticsDebugMode"
+ "_sharedStreamsExplicitlyDisabled"
+ "_shouldQueryDropActionForIndexPath:"
+ "_startListenerWithName:"
+ "_transferEnabledToFig"
+ "_updateTimerFired"
+ "accessTokenKnownOrigins"
+ "accessWithAccessor:fromBroadcaster:"
+ "advBuffersToRead"
+ "animateDisplayingStateHUD"
+ "assistantTextFormatting"
+ "canonicalLanguageIdentifierFromString:"
+ "clearTextAttachmentForTextAttachment:"
+ "continueStartingAutoBugCapture"
+ "createServiceConnectionWithServiceName:invalidationHandler:terminationHandler:peerEventHandler:peerQueue:"
+ "defaultTextureWriteRoundingMode"
+ "descriptorForRequiredKeysWithOptions:description:"
+ "dragInitiationGestureStateChanged:"
+ "edTopics:"
+ "extensionsByIdentifier"
+ "flushSnapshotsForSceneID:"
+ "hasMigratedToDriving"
+ "homeScreenWallpaperConfigurationIncludingValuesForTypes:"
+ "initWithApplication:uniqueIdentifier:sceneHandleProvider:displayIdentity:"
+ "initWithName:columns:primaryKeyColumns:conflictResolution:"
+ "insert:"
+ "isAggregateForEntryKey:"
+ "keyPathForNFCTagIdentifiers"
+ "layoutsForSpacerItem:"
+ "mainScreenSizePixels"
+ "nonSubscriberUpsellArticleID"
+ "promoteNodeWithDictionaryKey:"
+ "pruneDataOlderThan:exceptFor:inWorkspace:"
+ "releaseInputManager"
+ "sendStatusKitInvitationsForContacts:forceAvailabilityPublish:completionHandler:"
+ "setCloudCallingDevices:"
+ "setDepthPixelBufferYReplication:"
+ "setDestinationGlyphRange:"
+ "setDigitBaseline:"
+ "setHasProcessUserIdentifier:"
+ "setSystemApertureCoverSheetAssertion:"
+ "set_resultQueue_identitiesInProximity:"
+ "showPerformanceGroup:"
+ "updateQuerySuggestionsFromResponse:"
+ "zoom:withPoint:completionHandler:"
- "T@\"INFERENCESchemaINFERENCEDisambiguationPromptContext\",&,N,V_disambiguationPromptContext"
- "T@\"INFERENCESchemaINFERENCEEuclidScoreStatistics\",&,N,V_euclidScoreStatistics"
- "T@\"INFERENCESchemaINFERENCEEuclidTrialParameters\",&,N,V_euclidTrialParameters"
- "T@\"INFERENCESchemaINFERENCEMusicAppSelectionGroundTruthGenerated\",&,N,V_musicAppSelectionGroundTruthGenerated"
- "T@\"INFERENCESchemaINFERENCENotebookAppSelectionGroundTruthGenerated\",&,N,V_notebookAppSelectionGroundTruthGenerated"
- "T@\"INFERENCESchemaINFERENCEPervasiveEntityResolutionCommonSignals\",&,N,V_commonSignals"
- "T@\"INFERENCESchemaINFERENCEPotentialRetryContactInteractionContext\",&,N,V_interactionContext"
- "T@\"INFERENCESchemaINFERENCEPrivatizedHistoryStats\",&,N,V_historyStatsInSameDomain"
- "T@\"INFERENCESchemaINFERENCEPromptContext\",&,N,V_forcePrompt"
- "T@\"INFERENCESchemaINFERENCERequestMatchSignalSet\",&,N,V_requestMatchSignalSet"
- "T@\"INFERENCESchemaINFERENCEResolutionRequestContext\",&,N,V_resolutionRequestContext"
- "T@\"INFERENCESchemaINFERENCEResolutionRequestFailed\",&,N,V_failed"
- "T@\"INFERENCESchemaINFERENCESimpleTaskInfoGenerated\",&,N,V_simpleTaskInfoGenerated"
- "T@\"INFERENCESchemaINFERENCESpeechAlternativeRanks\",&,N,V_speechAlternativeRanks"
- "T@\"INFERENCESchemaINFERENCETrialEnrollment\",&,N,V_trialEnrollment"
- "T@\"INFERENCESchemaINFERENCEVideoPlayOnThirdPartyAppGroundTruthGenerated\",&,N,V_videoPlayOnThirdPartyAppGroundTruthGenerated"
- "T@\"INFERENCESchemaINFERENCEVideoSmartAppSelectionDisambiguationIndependentSignals\",&,N,V_independentSignal"
- "T@\"INFERENCESchemaINFERENCEWorkoutsAppSelectionGroundTruthGenerated\",&,N,V_workoutsAppSelectionGroundTruthGenerated"
- "T@\"JRSchemaJRAction\",&,N,V_action"
- "T@\"JRSchemaJRAnonymizedHistoryAndContext\",&,N,V_jrAnonymizedHistoryAndContext"
- "T@\"JRSchemaJRExperimentTriggered\",&,N,V_jrExperimentTriggered"
- "T@\"JRSchemaJRInferenceEnded\",&,N,V_ended"
- "T@\"JRSchemaJRModelInputShapes\",&,N,V_modelInputShapes"
- "T@\"JRSchemaRanking\",&,N,V_ranking"
- "T@\"JRSchemaRiskProfile\",&,N,V_riskProfile"
- "T@\"LCServiceLoggingConfiguration\",&,N,V_configuration"
- "T@\"LCServiceLoggingParameters\",&,N,V_categoryParameters"
- "T@\"MHSchemaMHASRAudioConfigureStarted\",&,N,V_asrAudioConfigureStarted"
- "T@\"MHSchemaMHAcousticFalseTriggerMitigationScoreGenerated\",&,N,V_aftmScore"
- "T@\"MHSchemaMHAcousticFalseTriggerMitigationStarted\",&,N,V_startedOrChanged"
- "T@\"MHSchemaMHAdMatchingFailed\",&,N,V_failed"
- "T@\"MHSchemaMHApplicationPlaybackAttempted\",&,N,V_applicationPlaybackAttempted"
- "T@\"MHSchemaMHAssistantDaemonAudioConfigureContext\",&,N,V_assistantDaemonAudioConfigureContext"
- "T@\"MHSchemaMHAssistantDaemonAudioConfigureStarted\",&,N,V_startedOrChanged"
- "T@\"MHSchemaMHAssistantDaemonAudioFetchRouteEnded\",&,N,V_ended"
- "T@\"MHSchemaMHAssistantDaemonAudioInitContext\",&,N,V_assistantDaemonAudioInitContext"
- "T@\"MHSchemaMHAssistantDaemonAudioInitStarted\",&,N,V_startedOrChanged"
- "T@\"MHSchemaMHAssistantDaemonAudioPrepareContext\",&,N,V_assistantDaemonAudioPrepareContext"
- "T@\"MHSchemaMHAssistantDaemonAudioPrepareStarted\",&,N,V_startedOrChanged"
- "T@\"MHSchemaMHAssistantDaemonAudioPrewarmEnded\",&,N,V_ended"
- "T@\"MHSchemaMHAssistantDaemonAudioRecordinFirstBufferReceipt\",&,N,V_ended"
- "T@\"MHSchemaMHAssistantDaemonAudioRecordingEnded\",&,N,V_ended"
- "T@\"MHSchemaMHAssistantDaemonAudioRecordingFailureInsufficientPriority\",&,N,V_assistantDaemonAudioRecordingFailureInsufficientPriority"
- "T@\"MHSchemaMHAssistantDaemonAudioRecordingFirstBufferStart\",&,N,V_startedOrChanged"
- "T@\"MHSchemaMHAssistantDaemonAudioRecordingInterruptionEnded\",&,N,V_ended"
- "_hasIfSessionId"
- "_hasInputLocale"
- "_hasIntentEagerExecutionContext"
- "_hasIntentTier1"
- "_hasIsSettingOn"
- "_hasKey"
- "_hasLastMediaUserFollowupAction"
- "_hasMeReference"
- "_hasMediaSignal"
- "_hasModelOutput"
- "_hasMultistepSubSearchExecution"
- "_hasNlv4SampleEvaluationContext"
- "_hasOriginAppId"
- "_hasOriginatingPrewarmRequestId"
- "_hasParameterId"
- "_hasPlanEventId"
- "_hasProductType"
- "_hasResolveTool"
- "_hasResponseFromMultipleDevices"
- "_hasResponseSafetyInferenceTime"
- "_hasRiskProfile"
- "_hasSay"
- "_hasSetUndoArgs"
- "_hasSiriSetupId"
- "_hasSortedScore"
- "_hasSsuBackgroundRequestContext"
- "_hasStartToContextRetrievedTime"
- "_heySiriEnabled"
- "_identityScores"
- "_integerPayload"
- "_intercomTarget"
- "_isAppInstalled"
- "_isAudioPlaying"
- "_isAutoshortcut"
- "_isClientAction"
- "_isDeviceLocked"
- "_isExactMatchPriorSiriContactId"
- "_isFirstPartyAppUsedForFollowup"
- "_isHlsKeysReady"
- "_isPhoneNumberContactResolvable"
- "_isRequestedApp"
- "_isSelf"
- "lValue"
- "resolverConfig"
- "sspeechTranslationEvent"

```
