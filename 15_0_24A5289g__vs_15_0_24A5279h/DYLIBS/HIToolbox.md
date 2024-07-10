## HIToolbox

> `/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox`

```diff

-1215.0.0.0.0
-  __TEXT.__text: 0x2a0f34
-  __TEXT.__auth_stubs: 0x6240
-  __TEXT.__objc_methlist: 0x3240
-  __TEXT.__gcc_except_tab: 0x6f78
-  __TEXT.__const: 0xaa44
-  __TEXT.__cstring: 0x2df20
+1213.0.0.0.0
+  __TEXT.__text: 0x2648b0
+  __TEXT.__auth_stubs: 0x61f0
+  __TEXT.__objc_methlist: 0x1f90
+  __TEXT.__gcc_except_tab: 0x64b8
+  __TEXT.__const: 0xaa24
+  __TEXT.__cstring: 0x2dbff
   __TEXT.__ustring: 0x9e
   __TEXT.__oslogstring: 0x22f
-  __TEXT.__unwind_info: 0xa638
+  __TEXT.__unwind_info: 0x9d00
   __TEXT.__eh_frame: 0x350
-  __TEXT.__objc_classname: 0x53a
-  __TEXT.__objc_methname: 0x78ad
-  __TEXT.__objc_methtype: 0x22e4
-  __TEXT.__objc_stubs: 0x6dc0
-  __DATA_CONST.__got: 0xcb8
+  __TEXT.__objc_classname: 0x450
+  __TEXT.__objc_methname: 0x747e
+  __TEXT.__objc_methtype: 0x226b
+  __TEXT.__objc_stubs: 0x6c80
+  __DATA_CONST.__got: 0xcb0
   __DATA_CONST.__const: 0x79d0
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f88
+  __DATA_CONST.__objc_selrefs: 0x1f38
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0x3140
+  __AUTH_CONST.__auth_got: 0x3118
   __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__const: 0x150f8
-  __AUTH_CONST.__cfstring: 0x1bdc0
-  __AUTH_CONST.__objc_const: 0x5d88
+  __AUTH_CONST.__const: 0x14ef8
+  __AUTH_CONST.__cfstring: 0x1bb60
+  __AUTH_CONST.__objc_const: 0x4568
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xb40
+  __AUTH.__objc_data: 0x8c0
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0x498
-  __DATA.__data: 0xd38
+  __DATA.__objc_ivar: 0x284
+  __DATA.__data: 0xd30
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x378
-  __DATA.__bss: 0x3d98
+  __DATA.__bss: 0x3c60
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 12274
-  Symbols:   18992
-  CStrings:  5581
+  Functions: 11594
+  Symbols:   18000
+  CStrings:  5552
 
Symbols:
+ +[IMKClient(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]
+ +[IMKClient(IMKClient_Main_Thread_Tracking) IMKRunLoopUpdateMain]
+ +[IMKClient(IMKClient_Main_Thread_Tracking) IMK_Catch_Log_Stalled_PerformBlocks_DispatchTime:withSelector:]
+ +[IMKClientInvocationSentinel sentinel]
+ +[IMKClientXPCInvocation invocationWithTimeout:selector:]
+ +[IMKInputSessionInvocationSentinel sentinel]
+ +[IMKInputSessionXPCInvocation invocationWithSession:selector:]
+ +[IPMDFontRange valueWithFont:range:]
+ -[IMKClient _addActionFrom:toDictionary:forCarbonMenu:base:]
+ -[IMKClient _buildSelectorDictionaryFromMenuDict:settingCommandID:]
+ -[IMKClient _bumpTimeout]
+ -[IMKClient _bundle]
+ -[IMKClient _cancelGetServerRetry]
+ -[IMKClient _checkSetTISCompletionBlock]
+ -[IMKClient _createAndInstallMenuSetSelectorDictFromMenuDict:]
+ -[IMKClient _defaultTimeout]
+ -[IMKClient _eventHandlerRef]
+ -[IMKClient _getServerRetry]
+ -[IMKClient _haveSafeServerProxy:]
+ -[IMKClient _inputMethodInfoDictionary]
+ -[IMKClient _isNonLaunchOption]
+ -[IMKClient _isPalette]
+ -[IMKClient _isServerRetryPending]
+ -[IMKClient _launch:fromBundle:throughPort:usingSBExtension:]
+ -[IMKClient _mapKeyCodeToInputSource:modifiers:]
+ -[IMKClient _mapKeyCodeToInputSource:modifiers:completionHandler:]
+ -[IMKClient _modeMenuKeysWithCompletionHandler:]
+ -[IMKClient _modeMenuKeys]
+ -[IMKClient _requestGetServerRetryNotifyingTarget:withSelector:]
+ -[IMKClient _selectorDictionary]
+ -[IMKClient _senderIsInvalid:]
+ -[IMKClient _setBundleIdentifier:]
+ -[IMKClient _setEventHandlerRef:]
+ -[IMKClient _setSelectorDictionary:]
+ -[IMKClient _setTargetForServerRetry:]
+ -[IMKClient _startServer_AllowingSandboxExtension:]
+ -[IMKClient _targetForServerRetry]
+ -[IMKClient _timeout]
+ -[IMKClient _untargetFromServerRetry:]
+ -[IMKClient bundleIdentifier]
+ -[IMKClient completionBlock]
+ -[IMKClient currentSession]
+ -[IMKClient dealloc]
+ -[IMKClient fulfillServerDependentWork]
+ -[IMKClient haveTISSelectCompletionBlock]
+ -[IMKClient imageFileForName:]
+ -[IMKClient initWithBundleIdentifier:isIMKExtension:]
+ -[IMKClient invalidateServerConnection]
+ -[IMKClient isClientServerTracing]
+ -[IMKClient isClientServerXPCTracing]
+ -[IMKClient isConnectionTracing]
+ -[IMKClient isDataTracingOn]
+ -[IMKClient isGeneralDebuggingOn]
+ -[IMKClient localizedStringForKey:]
+ -[IMKClient menuWithCompletionBlock:]
+ -[IMKClient menuWithCompletionHandler:]
+ -[IMKClient menu]
+ -[IMKClient modesWithCompletionHandler:]
+ -[IMKClient modes]
+ -[IMKClient serverWillTerminate]
+ -[IMKClient setCompletionBlock:]
+ -[IMKClient setCurrentSession:]
+ -[IMKClient setTISSelectCompletionBlock:]
+ -[IMKClient shouldUseXPC]
+ -[IMKClient switchedInputMode:]
+ -[IMKClient switchedInputMode:completionHandler:]
+ -[IMKClient tisSelectCompletionBlock]
+ -[IMKClientInvocationSentinel dealloc]
+ -[IMKClientInvocationSentinel init]
+ -[IMKClientInvocationSentinel isMarkedDone]
+ -[IMKClientInvocationSentinel markDone]
+ -[IMKClientXPCInvocation dealloc]
+ -[IMKClientXPCInvocation handleReplyTimerDidFire:]
+ -[IMKClientXPCInvocation handleRunLoopAwaitedMarkedDoneUntilTimeout]
+ -[IMKClientXPCInvocation handleRunLoopMarkedDone]
+ -[IMKClientXPCInvocation initWithTimeout:selector:]
+ -[IMKClientXPCInvocation invocationAwaitXPCReply]
+ -[IMKClientXPCInvocation invocationInterruptXPCReply]
+ -[IMKClientXPCInvocation isMarkedDone]
+ -[IMKClientXPCInvocation markDone]
+ -[IMKClientXPCInvocation performRunRunLoopEndedWithOther:]
+ -[IMKClientXPCInvocation performRunRunLoopEndedWithStopOrFinish:]
+ -[IMKClientXPCInvocation performRunRunloopWithTimeLimit:]
+ -[IMKClientXPCInvocation restoreRegularRunloop]
+ -[IMKClientXPCInvocation runRunLoopUntilMarkedDoneWithTimeLimit:]
+ -[IMKClientXPCInvocation sentinel]
+ -[IMKClientXPCInvocation timedOut]
+ -[IMKClientXPCInvocation timeout]
+ -[IMKInputSession _TIPropertyValueIsValid:]
+ -[IMKInputSession _addLineInformationFromCarbonEvent:toDictionary:]
+ -[IMKInputSession _addString:toEventRef:]
+ -[IMKInputSession _adjustAttachmentAttributes_forInsertText:]
+ -[IMKInputSession _adjustChromaticIMKAttributes_forSetMarkedText:]
+ -[IMKInputSession _adjustIronwoodAttributes_forInsertText:]
+ -[IMKInputSession _adjustIronwoodAttributes_forSetMarkedText:]
+ -[IMKInputSession _adjustServerStringAttributes_forInsertText:]
+ -[IMKInputSession _adjustServerStringAttributes_forSetMarkedText:]
+ -[IMKInputSession _attributesFromRangeViaGetSelectedText:completionHandler:]
+ -[IMKInputSession _attributesToHighlightStyle:fallback:isChromaticMarkedText:]
+ -[IMKInputSession _blankEvent:kind:]
+ -[IMKInputSession _closeInputPalette_withCompletionHandler:]
+ -[IMKInputSession _commitOnMouseDown:completionHandler:]
+ -[IMKInputSession _copyPaletteInputSource]
+ -[IMKInputSession _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]
+ -[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]
+ -[IMKInputSession _createAndSendOffsetToPointEvent:completionHandler:]
+ -[IMKInputSession _eventIsOn:completionHandler:]
+ -[IMKInputSession _glyphAttributesFromEventRef:forString:]
+ -[IMKInputSession _glyphInfoData:]
+ -[IMKInputSession _heightFromFontData:]
+ -[IMKInputSession _postEvent:completionHandler:]
+ -[IMKInputSession _showHideInputWindow:completionHandler:]
+ -[IMKInputSession _supportsDocumentAccess]
+ -[IMKInputSession _unicodeTextEventFromString:]
+ -[IMKInputSession _unmarkEventFromString:]
+ -[IMKInputSession _unmarkIMKMarkedRange]
+ -[IMKInputSession _updateEventFromAttributedString:pinRange:replacementRange:resultShouldUnmark:resultLength:]
+ -[IMKInputSession _updateIMKMarkedRange:markedLength:completionHandler:]
+ -[IMKInputSession activateAfterServerConnection]
+ -[IMKInputSession activate]
+ -[IMKInputSession addPendingEvent:withUniqueSeqNum:]
+ -[IMKInputSession attributedSubstringFromRange:]
+ -[IMKInputSession attributedSubstringFromRange:completionHandler:]
+ -[IMKInputSession attributesForCharacterIndex:]
+ -[IMKInputSession attributesForCharacterIndex:completionHandler:]
+ -[IMKInputSession attributesForCharacterIndex:lineHeightRectangle:]
+ -[IMKInputSession attributesForCharacterIndex_andLineRect:completionHandler:]
+ -[IMKInputSession bundleIdentifier]
+ -[IMKInputSession characterIndexForPoint:tracking:completionHandler:]
+ -[IMKInputSession characterIndexForPoint:tracking:inMarkedRange:]
+ -[IMKInputSession client]
+ -[IMKInputSession commitComposition]
+ -[IMKInputSession commitPendingInlineSession]
+ -[IMKInputSession currentInputSourceBundleID]
+ -[IMKInputSession deactivate]
+ -[IMKInputSession deadKeyState]
+ -[IMKInputSession dealloc]
+ -[IMKInputSession didCommandBySelector:]
+ -[IMKInputSession didCommandBySelector:completionHandler:]
+ -[IMKInputSession dismissFunctionRowItemTextInputView]
+ -[IMKInputSession doCommandBySelector:commandDictionary:]
+ -[IMKInputSession do_coreAttributesFromRange_postEventLoopWithContext:initBlockEach:postEventCompletionEach:whileConditionBlock:finalCompletion:]
+ -[IMKInputSession enqueueDeferredActivateInputSessionAction:timestamp:withInfo:]
+ -[IMKInputSession enqueueEventForDeferredActivate:]
+ -[IMKInputSession fetchViewServiceEndpointWithCompletionHandler:]
+ -[IMKInputSession finishSession]
+ -[IMKInputSession firstRectForCharacterRange:actualRange:]
+ -[IMKInputSession firstRectForCharacterRange:completionHandler:]
+ -[IMKInputSession handleEvent:completionHandler:]
+ -[IMKInputSession hidePalettesAtInsertionPoint]
+ -[IMKInputSession hidePalettes]
+ -[IMKInputSession imkxpc_attributedSubstringFromRange:reply:]
+ -[IMKInputSession imkxpc_attributesForCharacterIndex:reply:]
+ -[IMKInputSession imkxpc_bundleIdentifierWithReply:]
+ -[IMKInputSession imkxpc_characterIndexForPoint:tracking:reply:]
+ -[IMKInputSession imkxpc_commitPendingInlineSessionWithReply:]
+ -[IMKInputSession imkxpc_currentInputSourceBundleIDWithReply:]
+ -[IMKInputSession imkxpc_deadKeyStateWithReply:]
+ -[IMKInputSession imkxpc_dismissFunctionRowItemTextInputViewWithReply:]
+ -[IMKInputSession imkxpc_firstRectForCharacterRange:reply:]
+ -[IMKInputSession imkxpc_getApplicationProperty:reply:]
+ -[IMKInputSession imkxpc_hidePalettesAtInsertionPointWithReply:]
+ -[IMKInputSession imkxpc_incrementalSearchClientGeometryWithReply:]
+ -[IMKInputSession imkxpc_inputSessionDoneSleepWithReply:]
+ -[IMKInputSession imkxpc_insertText:replacementRange:validFlags:reply:]
+ -[IMKInputSession imkxpc_insertText:reply:]
+ -[IMKInputSession imkxpc_isAutomaticCapitalizationEnabledWithReply:]
+ -[IMKInputSession imkxpc_isAutomaticDashSubstitutionEnabledWithReply:]
+ -[IMKInputSession imkxpc_isAutomaticPeriodSubstitutionEnabledWithReply:]
+ -[IMKInputSession imkxpc_isAutomaticQuoteSubstitutionEnabledWithReply:]
+ -[IMKInputSession imkxpc_isAutomaticSpellingCorrectionEnabledWithReply:]
+ -[IMKInputSession imkxpc_isAutomaticTextCompletionEnabledWithReply:]
+ -[IMKInputSession imkxpc_isAutomaticTextReplacementEnabledWithReply:]
+ -[IMKInputSession imkxpc_isBottomLineInputContextWithReply:]
+ -[IMKInputSession imkxpc_isContinuousSpellCheckingEnabledWithReply:]
+ -[IMKInputSession imkxpc_isDictationHiliteCapableInputContextWithReply:]
+ -[IMKInputSession imkxpc_isGrammarCheckingEnabledWithReply:]
+ -[IMKInputSession imkxpc_isIncrementalSearchInputContextWithReply:]
+ -[IMKInputSession imkxpc_isPaletteTerminated:reply:]
+ -[IMKInputSession imkxpc_isSmartInsertDeleteEnabledWithReply:]
+ -[IMKInputSession imkxpc_isTextPlaceholderAwareInputContextWithReply:]
+ -[IMKInputSession imkxpc_lengthWithReply:]
+ -[IMKInputSession imkxpc_markedRangeValueWithReply:]
+ -[IMKInputSession imkxpc_overrideKeyboardWithKeyboardNamed:reply:]
+ -[IMKInputSession imkxpc_passSanityCheckAsyncClient:]
+ -[IMKInputSession imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]
+ -[IMKInputSession imkxpc_selectInputMode:reply:]
+ -[IMKInputSession imkxpc_selectedRangeWithReply:]
+ -[IMKInputSession imkxpc_setApplicationProperty:value:]
+ -[IMKInputSession imkxpc_setApplicationProperty:value:reply:]
+ -[IMKInputSession imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]
+ -[IMKInputSession imkxpc_stringFromRange:reply:]
+ -[IMKInputSession imkxpc_supportsChromaticMarkedTextWithReply:]
+ -[IMKInputSession imkxpc_supportsProperty:reply:]
+ -[IMKInputSession imkxpc_supportsTextAttachmentInsertionWithReply:]
+ -[IMKInputSession imkxpc_supportsUnicodeWithReply:]
+ -[IMKInputSession imkxpc_terminatePalette:reply:]
+ -[IMKInputSession imkxpc_uniqueClientIdentifierStringWithReply:]
+ -[IMKInputSession imkxpc_updateMenusDictionary:]
+ -[IMKInputSession imkxpc_validAttributesForMarkedTextWithReply:]
+ -[IMKInputSession imkxpc_viewEffectiveAppearanceNameWithReply:]
+ -[IMKInputSession imkxpc_viewEffectiveAppearanceWithReply:]
+ -[IMKInputSession imkxpc_windowEffectiveAppearanceNameWithReply:]
+ -[IMKInputSession imkxpc_windowEffectiveAppearanceWithReply:]
+ -[IMKInputSession imkxpc_windowLevelWithReply:]
+ -[IMKInputSession imkxpc_wouldHandleEvent:reply:]
+ -[IMKInputSession incrementalSearchClientGeometry]
+ -[IMKInputSession initWithClient:document:]
+ -[IMKInputSession inputSessionDoneSleep]
+ -[IMKInputSession insertPlaceholderCachedWeakRef:forKey:]
+ -[IMKInputSession insertText:]
+ -[IMKInputSession insertText:completionHandler:]
+ -[IMKInputSession insertText:replacementRange:]
+ -[IMKInputSession insertText:replacementRange:completionHandler:]
+ -[IMKInputSession insertText:replacementRange:validFlags:]
+ -[IMKInputSession insertText:replacementRange:validFlags:completionHandler:]
+ -[IMKInputSession invalidateAllPendingEvents]
+ -[IMKInputSession invalidateClientGeometry]
+ -[IMKInputSession ironwoodInputSessionPlaceholderWasInvalidated:]
+ -[IMKInputSession ironwoodInputSessionTextWasCorrected:]
+ -[IMKInputSession isAutomaticCapitalizationEnabled_WithAvailability:]
+ -[IMKInputSession isAutomaticDashSubstitutionEnabled_WithAvailability:]
+ -[IMKInputSession isAutomaticPeriodSubstitutionEnabled_WithAvailability:]
+ -[IMKInputSession isAutomaticQuoteSubstitutionEnabled_WithAvailability:]
+ -[IMKInputSession isAutomaticSpellingCorrectionEnabled_WithAvailability:]
+ -[IMKInputSession isAutomaticTextCompletionEnabled_WithAvailability:]
+ -[IMKInputSession isAutomaticTextReplacementEnabled_WithAvailability:]
+ -[IMKInputSession isBottomLineInputContext]
+ -[IMKInputSession isContinuousSpellCheckingEnabled_WithAvailability:]
+ -[IMKInputSession isDictationHiliteCapableInputContext]
+ -[IMKInputSession isFixTSMIsFromDiscardMarkedText]
+ -[IMKInputSession isGrammarCheckingEnabled_WithAvailability:]
+ -[IMKInputSession isIncrementalSearchInputContext]
+ -[IMKInputSession isPaletteTerminated:]
+ -[IMKInputSession isSmartInsertDeleteEnabled_WithAvailability:]
+ -[IMKInputSession isTextPlaceholderAwareInputContext]
+ -[IMKInputSession length]
+ -[IMKInputSession length_withCompletionHandler:]
+ -[IMKInputSession lookupPlaceholderCachedWeakRef:]
+ -[IMKInputSession markedRangeValue]
+ -[IMKInputSession markedRange]
+ -[IMKInputSession overrideKeyboardWithKeyboardNamed:]
+ -[IMKInputSession presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:]
+ -[IMKInputSession presentFunctionRowItemTextInputView]
+ -[IMKInputSession removePlaceholderCachedWeakRef:]
+ -[IMKInputSession replyWaitCount_decrementWithLocking]
+ -[IMKInputSession replyWaitCount_incrementWithLocking]
+ -[IMKInputSession replyWaitCount_lockDecrement]
+ -[IMKInputSession replyWaitCount_lockIncrement]
+ -[IMKInputSession replyWaitCount_testWithLocking]
+ -[IMKInputSession replyWaitCount_unlock]
+ -[IMKInputSession resetDeferredActivateInputSessionQueuedActions]
+ -[IMKInputSession resetDeferredActivateQueuedEvents]
+ -[IMKInputSession selectInputMode:]
+ -[IMKInputSession selectedRange]
+ -[IMKInputSession selectedRange_withCompletionHandler:]
+ -[IMKInputSession sendInputSessionSessAction:timestamp:withInfo:]
+ -[IMKInputSession sessionConnectionIsInvalid:]
+ -[IMKInputSession setInputMethodProperty:value:]
+ -[IMKInputSession setMarkedText:selectionRange:replacementRange:]
+ -[IMKInputSession setMarkedText:selectionRange:replacementRange:completionHandler:]
+ -[IMKInputSession setMarkedText:selectionRange:replacementRange:validFlags:]
+ -[IMKInputSession setMarkedText:selectionRange:replacementRange:validFlags:completionHandler:]
+ -[IMKInputSession setValue:forTag:]
+ -[IMKInputSession stringFromRange:actualRange:]
+ -[IMKInputSession stringFromRange:completionHandler:]
+ -[IMKInputSession supportsChromaticMarkedText]
+ -[IMKInputSession supportsProperty:]
+ -[IMKInputSession supportsTextAttachmentInsertion]
+ -[IMKInputSession supportsUnicode]
+ -[IMKInputSession terminatePalette:]
+ -[IMKInputSession textInputContext]
+ -[IMKInputSession tryCoreAttributesFromRange_CheckForSurrogateCharacter_CopyUniCharsForRangeAdjusted_wTest:context:initialBlock:continuationBlock:]
+ -[IMKInputSession tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]
+ -[IMKInputSession tryHandleEventSwitchedInputMode:eventWasHandled:continuationHandler:]
+ -[IMKInputSession tryHandleEvent_GetOffsetAndLocationForMouseEvent__withDispatchCondition:initialization:dispatchWork:postEventCompletion:continuationHandler:]
+ -[IMKInputSession tryHandleEvent_commitOnMouseDown_withDispatchCondition:dispatchWork:continuation:]
+ -[IMKInputSession tryUpdateIMKMarkedRange_withDispatchCondition:dispatchWork:continuation:]
+ -[IMKInputSession uniqueClientIdentifierString]
+ -[IMKInputSession unmarkTextInClient]
+ -[IMKInputSession validAttributesForMarkedText]
+ -[IMKInputSession valueForTag:]
+ -[IMKInputSession valueForTag:completionHandler:]
+ -[IMKInputSession viewEffectiveAppearance]
+ -[IMKInputSession windowEffectiveAppearance]
+ -[IMKInputSession windowLevel]
+ -[IMKInputSession wouldHandleEvent:completionHandler:]
+ -[IMKInputSessionInvocationSentinel dealloc]
+ -[IMKInputSessionInvocationSentinel init]
+ -[IMKInputSessionInvocationSentinel isMarkedDone]
+ -[IMKInputSessionInvocationSentinel markDone]
+ -[IMKInputSessionXPCInvocation addReplyTimerToRunloop]
+ -[IMKInputSessionXPCInvocation configureObservers]
+ -[IMKInputSessionXPCInvocation configureReplyTimerWithTimeout:]
+ -[IMKInputSessionXPCInvocation dealloc]
+ -[IMKInputSessionXPCInvocation handleInvocationAwaitXPCReplyDidTimeout]
+ -[IMKInputSessionXPCInvocation handlePrivateRunloopRunResult:]
+ -[IMKInputSessionXPCInvocation handlePrivateRunloopRunResult:].cold.1
+ -[IMKInputSessionXPCInvocation handleRunloopObservationWithObserver:activity:]
+ -[IMKInputSessionXPCInvocation initWithSession:selector:]
+ -[IMKInputSessionXPCInvocation invocationAwaitXPCReply]
+ -[IMKInputSessionXPCInvocation invocationInterruptXPCReply]
+ -[IMKInputSessionXPCInvocation isMarkedDone]
+ -[IMKInputSessionXPCInvocation markDone]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_0_innerRunLoop0:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_0_innerRunLoop1:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_0_innerRunLoop2:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_0_innerRunLoop3:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_1_innerRunLoop0:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_1_innerRunLoop1:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_1_innerRunLoop2:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_1_innerRunLoop3:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_2_innerRunLoop0:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_2_innerRunLoop1:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_2_innerRunLoop2:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_2_innerRunLoop3:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_3_innerRunLoop0:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_3_innerRunLoop1:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_3_innerRunLoop2:]
+ -[IMKInputSessionXPCInvocation runPrivateRunloopWithTimeLimit_3_innerRunLoop3:]
+ -[IMKInputSessionXPCInvocation runloopObservedActivityEntry]
+ -[IMKInputSessionXPCInvocation runloopObservedActivityExit]
+ -[IMKInputSessionXPCInvocation sentinel]
+ -[IMKInputSessionXPCInvocation teardownInvocationAwaitXPCReply]
+ -[IMKInputSessionXPCInvocation test_surpriseInnerRunloop]
+ -[IMKInputSessionXPCInvocation timedOut]
+ -[IMKInputSessionXPCInvocation verbose_runPrivateRunLoopWithTimeLimit:waitIteration:]
+ -[IMKQueuedEventRef dealloc]
+ -[IMKQueuedEventRef eventRef]
+ -[IMKQueuedEventRef initWithEventRef:]
+ -[IPMDFontRange dealloc]
+ -[IPMDFontRange font]
+ -[IPMDFontRange rangeValue]
+ OBJC_IVAR_$_IMKClientInvocationSentinel._int
+ OBJC_IVAR_$_IMKClientXPCInvocation._callerSelector
+ OBJC_IVAR_$_IMKClientXPCInvocation._replyTimer
+ OBJC_IVAR_$_IMKClientXPCInvocation._request_reply_done
+ OBJC_IVAR_$_IMKClientXPCInvocation._sentinel
+ OBJC_IVAR_$_IMKClientXPCInvocation._timedOut
+ OBJC_IVAR_$_IMKClientXPCInvocation._timeout
+ OBJC_IVAR_$_IMKInputSessionInvocationSentinel._int
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._callerSelector
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._imkInputSession
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._innerRunLoopCount
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._invocationInterruptAttempted
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._otherInnerRunLoopDetected
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._replyObserver
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._replyTimer
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._request_reply_done
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._sentinel
+ OBJC_IVAR_$_IMKInputSessionXPCInvocation._timedOut
+ OBJC_IVAR_$_IMKQueuedEventRef._eventRef
+ OBJC_IVAR_$_IPMDFontRange._font
+ OBJC_IVAR_$_IPMDFontRange._range
+ _OBJC_CLASS_$_IMKClientInvocationSentinel
+ _OBJC_CLASS_$_IMKClientXPCInvocation
+ _OBJC_CLASS_$_IMKInputSessionInvocationSentinel
+ _OBJC_CLASS_$_IMKInputSessionXPCInvocation
+ _OBJC_CLASS_$_IMKQueuedEventRef
+ _OBJC_CLASS_$_IPMDFontRange
+ _OBJC_METACLASS_$_IMKClientInvocationSentinel
+ _OBJC_METACLASS_$_IMKClientXPCInvocation
+ _OBJC_METACLASS_$_IMKInputSessionInvocationSentinel
+ _OBJC_METACLASS_$_IMKInputSessionXPCInvocation
+ _OBJC_METACLASS_$_IMKQueuedEventRef
+ _OBJC_METACLASS_$_IPMDFontRange
+ __17-[IMKClient menu]_block_invoke.134
+ __27-[IMKInputSession activate]_block_invoke.343
+ __39-[IMKClient menuWithCompletionHandler:]_block_invoke.185
+ __39-[IMKClient menuWithCompletionHandler:]_block_invoke.196
+ __39-[IMKClient menuWithCompletionHandler:]_block_invoke_2.189
+ __39-[IMKClient menuWithCompletionHandler:]_block_invoke_2.197
+ __40-[IMKClient modesWithCompletionHandler:]_block_invoke.236
+ __40-[IMKClient modesWithCompletionHandler:]_block_invoke_2.237
+ __48-[IMKInputSession _eventIsOn:completionHandler:]_block_invoke.862
+ __48-[IMKInputSession _eventIsOn:completionHandler:]_block_invoke.878
+ __48-[IMKInputSession _eventIsOn:completionHandler:]_block_invoke_2.866
+ __48-[IMKInputSession _eventIsOn:completionHandler:]_block_invoke_2.879
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke.479
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke.501
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke.514
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke.526
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke.527
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_2.480
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_2.503
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_2.518
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_3.495
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_3.507
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_4.497
+ __49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_4.511
+ __49-[IMKInputSession valueForTag:completionHandler:]_block_invoke.671
+ __49-[IMKInputSession valueForTag:completionHandler:]_block_invoke.684
+ __49-[IMKInputSession valueForTag:completionHandler:]_block_invoke_2.675
+ __49-[IMKInputSession valueForTag:completionHandler:]_block_invoke_2.685
+ __53-[IMKInputSession stringFromRange:completionHandler:]_block_invoke.1531
+ __58-[IMKInputSession didCommandBySelector:completionHandler:]_block_invoke.759
+ __58-[IMKInputSession didCommandBySelector:completionHandler:]_block_invoke_2.760
+ __60+[IMKClient(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke.168
+ __60+[IMKClient(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke.172
+ __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke.143
+ __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke.151
+ __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2.147
+ __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2.155
+ __67-[IMKClient(IMKClientConnection_XPC) _getServerXPCProxyForSession:]_block_invoke.452
+ __72-[IMKInputSession _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.896
+ __72-[IMKInputSession _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.902
+ __Block_byref_object_copy_.1387
+ __Block_byref_object_copy_.1459
+ __Block_byref_object_dispose_.1388
+ __Block_byref_object_dispose_.1460
+ __OBJC_$_CLASS_METHODS_IMKClient(IMKClientConnection_DO|IMKClient_XPCReplyWaitCount_Locking|IMKClient_Main_Thread_Tracking|IMKClientConnection_XPC)
+ __OBJC_$_CLASS_METHODS_IMKClientInvocationSentinel
+ __OBJC_$_CLASS_METHODS_IMKClientXPCInvocation
+ __OBJC_$_CLASS_METHODS_IMKInputSessionInvocationSentinel
+ __OBJC_$_CLASS_METHODS_IMKInputSessionXPCInvocation
+ __OBJC_$_CLASS_METHODS_IPMDFontRange
+ __OBJC_$_INSTANCE_METHODS_IMKClient(IMKClientConnection_DO|IMKClient_XPCReplyWaitCount_Locking|IMKClient_Main_Thread_Tracking|IMKClientConnection_XPC)
+ __OBJC_$_INSTANCE_METHODS_IMKClientInvocationSentinel
+ __OBJC_$_INSTANCE_METHODS_IMKClientXPCInvocation
+ __OBJC_$_INSTANCE_METHODS_IMKInputSessionInvocationSentinel
+ __OBJC_$_INSTANCE_METHODS_IMKInputSessionXPCInvocation
+ __OBJC_$_INSTANCE_METHODS_IMKQueuedEventRef
+ __OBJC_$_INSTANCE_METHODS_IPMDFontRange
+ __OBJC_$_INSTANCE_VARIABLES_IMKClientInvocationSentinel
+ __OBJC_$_INSTANCE_VARIABLES_IMKClientXPCInvocation
+ __OBJC_$_INSTANCE_VARIABLES_IMKInputSessionInvocationSentinel
+ __OBJC_$_INSTANCE_VARIABLES_IMKInputSessionXPCInvocation
+ __OBJC_$_INSTANCE_VARIABLES_IMKQueuedEventRef
+ __OBJC_$_INSTANCE_VARIABLES_IPMDFontRange
+ __OBJC_CLASS_RO_$_IMKClientInvocationSentinel
+ __OBJC_CLASS_RO_$_IMKClientXPCInvocation
+ __OBJC_CLASS_RO_$_IMKInputSessionInvocationSentinel
+ __OBJC_CLASS_RO_$_IMKInputSessionXPCInvocation
+ __OBJC_CLASS_RO_$_IMKQueuedEventRef
+ __OBJC_CLASS_RO_$_IPMDFontRange
+ __OBJC_METACLASS_RO_$_IMKClientInvocationSentinel
+ __OBJC_METACLASS_RO_$_IMKClientXPCInvocation
+ __OBJC_METACLASS_RO_$_IMKInputSessionInvocationSentinel
+ __OBJC_METACLASS_RO_$_IMKInputSessionXPCInvocation
+ __OBJC_METACLASS_RO_$_IMKQueuedEventRef
+ __OBJC_METACLASS_RO_$_IPMDFontRange
+ __ZZ28-[IMKClient _defaultTimeout]E16sDefaultsChecked
+ __ZZ36+[IMKInputSession IMKCFRunLoopSetup]E9onceToken
+ __ZZ47-[IMKInputSession validAttributesForMarkedText]E8theArray
+ __ZZ53-[IMKClient initWithBundleIdentifier:isIMKExtension:]E16sDefaultsChecked
+ __ZZ62+[IMKClient(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]E4once
+ ___100-[IMKInputSession tryHandleEvent_commitOnMouseDown_withDispatchCondition:dispatchWork:continuation:]_block_invoke
+ ___145-[IMKInputSession do_coreAttributesFromRange_postEventLoopWithContext:initBlockEach:postEventCompletionEach:whileConditionBlock:finalCompletion:]_block_invoke
+ ___147-[IMKInputSession tryCoreAttributesFromRange_CheckForSurrogateCharacter_CopyUniCharsForRangeAdjusted_wTest:context:initialBlock:continuationBlock:]_block_invoke
+ ___159-[IMKInputSession tryHandleEvent_GetOffsetAndLocationForMouseEvent__withDispatchCondition:initialization:dispatchWork:postEventCompletion:continuationHandler:]_block_invoke
+ ___17-[IMKClient menu]_block_invoke
+ ___177-[IMKInputSession tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]_block_invoke
+ ___177-[IMKInputSession tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]_block_invoke_2
+ ___18-[IMKClient modes]_block_invoke
+ ___18-[IMKClient modes]_block_invoke_2
+ ___25-[IMKInputSession length]_block_invoke
+ ___27-[IMKInputSession activate]_block_invoke
+ ___29-[IMKInputSession deactivate]_block_invoke
+ ___29-[IMKInputSession deactivate]_block_invoke_2
+ ___30-[IMKInputSession insertText:]_block_invoke
+ ___32-[IMKInputSession selectedRange]_block_invoke
+ ___35-[IMKInputSession setValue:forTag:]_block_invoke
+ ___35-[IMKInputSession setValue:forTag:]_block_invoke_2
+ ___36+[IMKInputSession IMKCFRunLoopSetup]_block_invoke
+ ___36-[IMKInputSession commitComposition]_block_invoke
+ ___36-[IMKInputSession commitComposition]_block_invoke_2
+ ___37-[IMKInputSession unmarkTextInClient]_block_invoke
+ ___39-[IMKClient invalidateServerConnection]_block_invoke
+ ___39-[IMKClient menuWithCompletionHandler:]_block_invoke
+ ___39-[IMKClient menuWithCompletionHandler:]_block_invoke_2
+ ___40-[IMKClient modesWithCompletionHandler:]_block_invoke
+ ___40-[IMKClient modesWithCompletionHandler:]_block_invoke_2
+ ___40-[IMKClient modesWithCompletionHandler:]_block_invoke_3
+ ___40-[IMKClient modesWithCompletionHandler:]_block_invoke_4
+ ___42-[IMKInputSession imkxpc_lengthWithReply:]_block_invoke
+ ___42-[IMKInputSession imkxpc_lengthWithReply:]_block_invoke_2
+ ___43-[IMKInputSession imkxpc_insertText:reply:]_block_invoke
+ ___43-[IMKInputSession imkxpc_insertText:reply:]_block_invoke_2
+ ___47-[IMKInputSession attributesForCharacterIndex:]_block_invoke
+ ___47-[IMKInputSession imkxpc_windowLevelWithReply:]_block_invoke
+ ___47-[IMKInputSession insertText:replacementRange:]_block_invoke
+ ___47-[IMKInputSession stringFromRange:actualRange:]_block_invoke
+ ___48-[IMKClient _modeMenuKeysWithCompletionHandler:]_block_invoke
+ ___48-[IMKInputSession _eventIsOn:completionHandler:]_block_invoke
+ ___48-[IMKInputSession _eventIsOn:completionHandler:]_block_invoke_2
+ ___48-[IMKInputSession _postEvent:completionHandler:]_block_invoke
+ ___48-[IMKInputSession activateAfterServerConnection]_block_invoke
+ ___48-[IMKInputSession activateAfterServerConnection]_block_invoke_2
+ ___48-[IMKInputSession attributedSubstringFromRange:]_block_invoke
+ ___48-[IMKInputSession imkxpc_deadKeyStateWithReply:]_block_invoke
+ ___48-[IMKInputSession imkxpc_selectInputMode:reply:]_block_invoke
+ ___48-[IMKInputSession imkxpc_stringFromRange:reply:]_block_invoke
+ ___48-[IMKInputSession imkxpc_stringFromRange:reply:]_block_invoke_2
+ ___48-[IMKInputSession imkxpc_updateMenusDictionary:]_block_invoke
+ ___48-[IMKInputSession insertText:completionHandler:]_block_invoke
+ ___48-[IMKInputSession length_withCompletionHandler:]_block_invoke
+ ___49-[IMKClient switchedInputMode:completionHandler:]_block_invoke
+ ___49-[IMKClientXPCInvocation invocationAwaitXPCReply]_block_invoke
+ ___49-[IMKInputSession handleEvent:completionHandler:]_block_invoke
+ ___49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_2
+ ___49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_3
+ ___49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_4
+ ___49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_5
+ ___49-[IMKInputSession handleEvent:completionHandler:]_block_invoke_6
+ ___49-[IMKInputSession imkxpc_selectedRangeWithReply:]_block_invoke
+ ___49-[IMKInputSession imkxpc_selectedRangeWithReply:]_block_invoke_2
+ ___49-[IMKInputSession imkxpc_supportsProperty:reply:]_block_invoke
+ ___49-[IMKInputSession imkxpc_terminatePalette:reply:]_block_invoke
+ ___49-[IMKInputSession imkxpc_wouldHandleEvent:reply:]_block_invoke
+ ___49-[IMKInputSession imkxpc_wouldHandleEvent:reply:]_block_invoke_2
+ ___49-[IMKInputSession valueForTag:completionHandler:]_block_invoke
+ ___49-[IMKInputSession valueForTag:completionHandler:]_block_invoke_2
+ ___50-[IMKInputSessionXPCInvocation configureObservers]_block_invoke
+ ___51-[IMKInputSession imkxpc_supportsUnicodeWithReply:]_block_invoke
+ ___52-[IMKInputSession imkxpc_bundleIdentifierWithReply:]_block_invoke
+ ___52-[IMKInputSession imkxpc_isPaletteTerminated:reply:]_block_invoke
+ ___52-[IMKInputSession imkxpc_markedRangeValueWithReply:]_block_invoke
+ ___53-[IMKClientXPCInvocation invocationInterruptXPCReply]_block_invoke
+ ___53-[IMKInputSession stringFromRange:completionHandler:]_block_invoke
+ ___54-[IMKInputSession wouldHandleEvent:completionHandler:]_block_invoke
+ ___54-[IMKInputSessionXPCInvocation addReplyTimerToRunloop]_block_invoke
+ ___55-[IMKInputSession imkxpc_getApplicationProperty:reply:]_block_invoke
+ ___55-[IMKInputSession selectedRange_withCompletionHandler:]_block_invoke
+ ___56-[IMKInputSession _commitOnMouseDown:completionHandler:]_block_invoke
+ ___57-[IMKInputSession doCommandBySelector:commandDictionary:]_block_invoke
+ ___57-[IMKInputSession doCommandBySelector:commandDictionary:]_block_invoke_2
+ ___57-[IMKInputSession imkxpc_inputSessionDoneSleepWithReply:]_block_invoke
+ ___58-[IMKInputSession _showHideInputWindow:completionHandler:]_block_invoke
+ ___58-[IMKInputSession didCommandBySelector:completionHandler:]_block_invoke
+ ___58-[IMKInputSession didCommandBySelector:completionHandler:]_block_invoke_2
+ ___58-[IMKInputSession didCommandBySelector:completionHandler:]_block_invoke_3
+ ___58-[IMKInputSession didCommandBySelector:completionHandler:]_block_invoke_4
+ ___58-[IMKInputSession firstRectForCharacterRange:actualRange:]_block_invoke
+ ___58-[IMKInputSession insertText:replacementRange:validFlags:]_block_invoke
+ ___59-[IMKInputSession imkxpc_firstRectForCharacterRange:reply:]_block_invoke
+ ___59-[IMKInputSession imkxpc_firstRectForCharacterRange:reply:]_block_invoke_2
+ ___59-[IMKInputSession imkxpc_viewEffectiveAppearanceWithReply:]_block_invoke
+ ___59-[IMKInputSessionXPCInvocation invocationInterruptXPCReply]_block_invoke
+ ___60-[IMKInputSession _closeInputPalette_withCompletionHandler:]_block_invoke
+ ___60-[IMKInputSession imkxpc_attributesForCharacterIndex:reply:]_block_invoke
+ ___60-[IMKInputSession imkxpc_attributesForCharacterIndex:reply:]_block_invoke_2
+ ___60-[IMKInputSession imkxpc_isBottomLineInputContextWithReply:]_block_invoke
+ ___60-[IMKInputSession imkxpc_isGrammarCheckingEnabledWithReply:]_block_invoke
+ ___61-[IMKInputSession imkxpc_attributedSubstringFromRange:reply:]_block_invoke
+ ___61-[IMKInputSession imkxpc_attributedSubstringFromRange:reply:]_block_invoke_2
+ ___61-[IMKInputSession imkxpc_setApplicationProperty:value:reply:]_block_invoke
+ ___61-[IMKInputSession imkxpc_windowEffectiveAppearanceWithReply:]_block_invoke
+ ___62+[IMKClient(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]_block_invoke
+ ___62-[IMKInputSession imkxpc_commitPendingInlineSessionWithReply:]_block_invoke
+ ___62-[IMKInputSession imkxpc_currentInputSourceBundleIDWithReply:]_block_invoke
+ ___62-[IMKInputSession imkxpc_isSmartInsertDeleteEnabledWithReply:]_block_invoke
+ ___63-[IMKInputSession imkxpc_supportsChromaticMarkedTextWithReply:]_block_invoke
+ ___63-[IMKInputSession imkxpc_viewEffectiveAppearanceNameWithReply:]_block_invoke
+ ___63-[IMKInputSessionXPCInvocation configureReplyTimerWithTimeout:]_block_invoke
+ ___64-[IMKInputSession firstRectForCharacterRange:completionHandler:]_block_invoke
+ ___64-[IMKInputSession imkxpc_characterIndexForPoint:tracking:reply:]_block_invoke
+ ___64-[IMKInputSession imkxpc_characterIndexForPoint:tracking:reply:]_block_invoke_2
+ ___64-[IMKInputSession imkxpc_hidePalettesAtInsertionPointWithReply:]_block_invoke
+ ___64-[IMKInputSession imkxpc_uniqueClientIdentifierStringWithReply:]_block_invoke
+ ___64-[IMKInputSession imkxpc_validAttributesForMarkedTextWithReply:]_block_invoke
+ ___65-[IMKInputSession attributesForCharacterIndex:completionHandler:]_block_invoke
+ ___65-[IMKInputSession characterIndexForPoint:tracking:inMarkedRange:]_block_invoke
+ ___65-[IMKInputSession fetchViewServiceEndpointWithCompletionHandler:]_block_invoke
+ ___65-[IMKInputSession fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_2
+ ___65-[IMKInputSession fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_3
+ ___65-[IMKInputSession fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_4
+ ___65-[IMKInputSession imkxpc_windowEffectiveAppearanceNameWithReply:]_block_invoke
+ ___65-[IMKInputSession insertText:replacementRange:completionHandler:]_block_invoke
+ ___65-[IMKInputSession insertText:replacementRange:completionHandler:]_block_invoke_2
+ ___65-[IMKInputSession setMarkedText:selectionRange:replacementRange:]_block_invoke
+ ___66-[IMKClient _mapKeyCodeToInputSource:modifiers:completionHandler:]_block_invoke
+ ___66-[IMKInputSession attributedSubstringFromRange:completionHandler:]_block_invoke
+ ___66-[IMKInputSession attributedSubstringFromRange:completionHandler:]_block_invoke_2
+ ___66-[IMKInputSession imkxpc_overrideKeyboardWithKeyboardNamed:reply:]_block_invoke
+ ___67-[IMKInputSession attributesForCharacterIndex:lineHeightRectangle:]_block_invoke
+ ___67-[IMKInputSession imkxpc_incrementalSearchClientGeometryWithReply:]_block_invoke
+ ___67-[IMKInputSession imkxpc_isIncrementalSearchInputContextWithReply:]_block_invoke
+ ___67-[IMKInputSession imkxpc_supportsTextAttachmentInsertionWithReply:]_block_invoke
+ ___68-[IMKInputSession imkxpc_isAutomaticCapitalizationEnabledWithReply:]_block_invoke
+ ___68-[IMKInputSession imkxpc_isAutomaticTextCompletionEnabledWithReply:]_block_invoke
+ ___68-[IMKInputSession imkxpc_isContinuousSpellCheckingEnabledWithReply:]_block_invoke
+ ___69-[IMKInputSession characterIndexForPoint:tracking:completionHandler:]_block_invoke
+ ___69-[IMKInputSession imkxpc_isAutomaticTextReplacementEnabledWithReply:]_block_invoke
+ ___70-[IMKInputSession _createAndSendOffsetToPointEvent:completionHandler:]_block_invoke
+ ___70-[IMKInputSession imkxpc_isAutomaticDashSubstitutionEnabledWithReply:]_block_invoke
+ ___70-[IMKInputSession imkxpc_isTextPlaceholderAwareInputContextWithReply:]_block_invoke
+ ___71-[IMKInputSession imkxpc_dismissFunctionRowItemTextInputViewWithReply:]_block_invoke
+ ___71-[IMKInputSession imkxpc_insertText:replacementRange:validFlags:reply:]_block_invoke
+ ___71-[IMKInputSession imkxpc_insertText:replacementRange:validFlags:reply:]_block_invoke_2
+ ___71-[IMKInputSession imkxpc_isAutomaticQuoteSubstitutionEnabledWithReply:]_block_invoke
+ ___72-[IMKInputSession _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke
+ ___72-[IMKInputSession _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke_2
+ ___72-[IMKInputSession imkxpc_isAutomaticPeriodSubstitutionEnabledWithReply:]_block_invoke
+ ___72-[IMKInputSession imkxpc_isAutomaticSpellingCorrectionEnabledWithReply:]_block_invoke
+ ___72-[IMKInputSession imkxpc_isDictationHiliteCapableInputContextWithReply:]_block_invoke
+ ___76-[IMKInputSession _attributesFromRangeViaGetSelectedText:completionHandler:]_block_invoke
+ ___76-[IMKInputSession insertText:replacementRange:validFlags:completionHandler:]_block_invoke
+ ___76-[IMKInputSession setMarkedText:selectionRange:replacementRange:validFlags:]_block_invoke
+ ___77-[IMKInputSession attributesForCharacterIndex_andLineRect:completionHandler:]_block_invoke
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_10
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_11
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_12
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_13
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_14
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_2
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_3
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_4
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_5
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_6
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_7
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_8
+ ___78-[IMKInputSession _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_9
+ ___79-[IMKInputSession _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]_block_invoke
+ ___80-[IMKInputSession imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]_block_invoke
+ ___80-[IMKInputSession imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]_block_invoke_2
+ ___83-[IMKInputSession setMarkedText:selectionRange:replacementRange:completionHandler:]_block_invoke
+ ___83-[IMKInputSession setMarkedText:selectionRange:replacementRange:completionHandler:]_block_invoke_2
+ ___85-[IMKInputSession presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:]_block_invoke
+ ___87+[IMKInputSession IMKXPCPerformBlockOnMainThreadInMode:performHow:callerCmd:workBlock:]_block_invoke
+ ___87-[IMKInputSession tryHandleEventSwitchedInputMode:eventWasHandled:continuationHandler:]_block_invoke
+ ___89-[IMKInputSession imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]_block_invoke
+ ___89-[IMKInputSession imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]_block_invoke_2
+ ___91-[IMKInputSession tryUpdateIMKMarkedRange_withDispatchCondition:dispatchWork:continuation:]_block_invoke
+ ___94-[IMKInputSession setMarkedText:selectionRange:replacementRange:validFlags:completionHandler:]_block_invoke
+ __block_literal_global.1368
+ __block_literal_global.1375
+ __block_literal_global.1380
+ __block_literal_global.1385
+ __block_literal_global.166
+ __block_literal_global.189
+ __block_literal_global.2053
+ __block_literal_global.302
+ __block_literal_global.581
+ __block_literal_global.842
- +[IMKClient IMKRunLoopGetMain]
- +[IMKClient IMKRunLoopUpdateMain]
- +[IMKClient IMK_Catch_Log_Stalled_PerformBlocks_DispatchTime:withSelector:]
- +[IMKClient allocWithZone:]
- +[IMKClient imExtensionBundlePaths]
- +[IMKClient privateRunLoopMode]
- +[IMKClient replyWaitCount_decrementWithLocking]
- +[IMKClient replyWaitCount_incrementWithLocking]
- +[IMKClient replyWaitCount_lockDecrement]
- +[IMKClient replyWaitCount_lockIncrement]
- +[IMKClient replyWaitCount_testWithLocking]
- +[IMKClient replyWaitCount_unlock]
- +[IMKClient subclass]
- +[IMKClientInvocationSentinel_Legacy sentinel]
- +[IMKClientXPCInvocation_Legacy invocationWithTimeout:selector:]
- +[IMKClientXPCInvocation_Modern invocationWithTimeout:selector:]
- +[IMKClient_Legacy clientServerXPCBlockStallLogging]
- +[IMKClient_Legacy isClientServerTracing]
- +[IMKClient_Legacy isClientServerXPCTracing]
- +[IMKClient_Legacy isConnectionTracing]
- +[IMKClient_Legacy isDataTracingOn]
- +[IMKClient_Legacy isGeneralDebuggingOn]
- +[IMKClient_Legacy setTemporaryClientServerXPCTracing:]
- +[IMKClient_Legacy(IMKClientConnection_XPC) imExtensionBundlePaths]
- +[IMKClient_Legacy(IMKClientConnection_XPC) privateRunLoopMode]
- +[IMKClient_Legacy(IMKClientConnection_XPC) xpcSetupForMessaging]
- +[IMKClient_Legacy(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]
- +[IMKClient_Legacy(IMKClient_Main_Thread_Tracking) IMKRunLoopUpdateMain]
- +[IMKClient_Legacy(IMKClient_Main_Thread_Tracking) IMK_Catch_Log_Stalled_PerformBlocks_DispatchTime:withSelector:]
- +[IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking) replyWaitCount_decrementWithLocking]
- +[IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking) replyWaitCount_incrementWithLocking]
- +[IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking) replyWaitCount_lockDecrement]
- +[IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking) replyWaitCount_lockIncrement]
- +[IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking) replyWaitCount_testWithLocking]
- +[IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking) replyWaitCount_unlock]
- +[IMKClient_Modern clientServerXPCBlockStallLogging]
- +[IMKClient_Modern isClientServerTracing]
- +[IMKClient_Modern isClientServerXPCTracing]
- +[IMKClient_Modern isConnectionTracing]
- +[IMKClient_Modern isDataTracingOn]
- +[IMKClient_Modern isGeneralDebuggingOn]
- +[IMKClient_Modern setTemporaryClientServerXPCTracing:]
- +[IMKClient_Modern(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]
- +[IMKClient_Modern(IMKClient_Main_Thread_Tracking) IMKRunLoopUpdateMain]
- +[IMKClient_Modern(IMKClient_Main_Thread_Tracking) IMK_Catch_Log_Stalled_PerformBlocks_DispatchTime:withSelector:]
- +[IMKInputSession allocWithZone:]
- +[IMKInputSession subclass]
- +[IMKInputSessionInvocationSentinel_Legacy sentinel]
- +[IMKInputSessionXPCInvocation_Legacy invocationWithSession:selector:]
- +[IMKInputSessionXPCInvocation_Modern invocationWithSession:selector:]
- +[IMKInputSession_Legacy IMKCFRunLoopSetup]
- +[IMKInputSession_Legacy IMKXPCPerformBlockOnMainThreadInMode:performHow:callerCmd:workBlock:]
- +[IMKInputSession_Legacy inputSessionWithClient:document:]
- +[IMKInputSession_Modern IMKCFRunLoopSetup]
- +[IMKInputSession_Modern IMKXPCPerformBlockOnMainThreadInMode:performHow:callerCmd:workBlock:]
- +[IMKInputSession_Modern inputSessionWithClient:document:]
- +[IMKInputSession_Modern whileAwaitingReplyFromProcess:performActions:]
- +[IMKInputSession_Modern withActivity:performActions:]
- +[IPMDFontRange_Legacy valueWithFont:range:]
- +[IPMDFontRange_Modern valueWithFont:range:]
- -[IMKClientInvocationSentinel_Legacy dealloc]
- -[IMKClientInvocationSentinel_Legacy init]
- -[IMKClientInvocationSentinel_Legacy isMarkedDone]
- -[IMKClientInvocationSentinel_Legacy markDone]
- -[IMKClientXPCInvocation_Legacy dealloc]
- -[IMKClientXPCInvocation_Legacy handleReplyTimerDidFire:]
- -[IMKClientXPCInvocation_Legacy handleRunLoopAwaitedMarkedDoneUntilTimeout]
- -[IMKClientXPCInvocation_Legacy handleRunLoopMarkedDone]
- -[IMKClientXPCInvocation_Legacy initWithTimeout:selector:]
- -[IMKClientXPCInvocation_Legacy invocationAwaitXPCReply]
- -[IMKClientXPCInvocation_Legacy invocationInterruptXPCReply]
- -[IMKClientXPCInvocation_Legacy isMarkedDone]
- -[IMKClientXPCInvocation_Legacy markDone]
- -[IMKClientXPCInvocation_Legacy performRunRunLoopEndedWithOther:]
- -[IMKClientXPCInvocation_Legacy performRunRunLoopEndedWithStopOrFinish:]
- -[IMKClientXPCInvocation_Legacy performRunRunloopWithTimeLimit:]
- -[IMKClientXPCInvocation_Legacy restoreRegularRunloop]
- -[IMKClientXPCInvocation_Legacy runRunLoopUntilMarkedDoneWithTimeLimit:]
- -[IMKClientXPCInvocation_Legacy sentinel]
- -[IMKClientXPCInvocation_Legacy timedOut]
- -[IMKClientXPCInvocation_Legacy timeout]
- -[IMKClientXPCInvocation_Modern initWithTimeout:selector:]
- -[IMKClientXPCInvocation_Modern invocationAwaitXPCReplyFromProcessIdentifier:]
- -[IMKClientXPCInvocation_Modern timeout]
- -[IMKClient_Legacy _addActionFrom:toDictionary:forCarbonMenu:base:]
- -[IMKClient_Legacy _buildSelectorDictionaryFromMenuDict:settingCommandID:]
- -[IMKClient_Legacy _bumpTimeout]
- -[IMKClient_Legacy _bundle]
- -[IMKClient_Legacy _cancelGetServerRetry]
- -[IMKClient_Legacy _checkSetTISCompletionBlock]
- -[IMKClient_Legacy _createAndInstallMenuSetSelectorDictFromMenuDict:]
- -[IMKClient_Legacy _defaultTimeout]
- -[IMKClient_Legacy _eventHandlerRef]
- -[IMKClient_Legacy _getServerRetry]
- -[IMKClient_Legacy _haveSafeServerProxy:]
- -[IMKClient_Legacy _inputMethodInfoDictionary]
- -[IMKClient_Legacy _isNonLaunchOption]
- -[IMKClient_Legacy _isPalette]
- -[IMKClient_Legacy _isServerRetryPending]
- -[IMKClient_Legacy _launch:fromBundle:throughPort:usingSBExtension:]
- -[IMKClient_Legacy _mapKeyCodeToInputSource:modifiers:]
- -[IMKClient_Legacy _mapKeyCodeToInputSource:modifiers:completionHandler:]
- -[IMKClient_Legacy _modeMenuKeysWithCompletionHandler:]
- -[IMKClient_Legacy _modeMenuKeys]
- -[IMKClient_Legacy _requestGetServerRetryNotifyingTarget:withSelector:]
- -[IMKClient_Legacy _selectorDictionary]
- -[IMKClient_Legacy _senderIsInvalid:]
- -[IMKClient_Legacy _setBundleIdentifier:]
- -[IMKClient_Legacy _setEventHandlerRef:]
- -[IMKClient_Legacy _setSelectorDictionary:]
- -[IMKClient_Legacy _setTargetForServerRetry:]
- -[IMKClient_Legacy _startServer_AllowingSandboxExtension:]
- -[IMKClient_Legacy _targetForServerRetry]
- -[IMKClient_Legacy _timeout]
- -[IMKClient_Legacy _untargetFromServerRetry:]
- -[IMKClient_Legacy _waitingForMenu]
- -[IMKClient_Legacy bundleIdentifier]
- -[IMKClient_Legacy cleanTermination]
- -[IMKClient_Legacy completionBlock]
- -[IMKClient_Legacy currentSession]
- -[IMKClient_Legacy dealloc]
- -[IMKClient_Legacy fulfillServerDependentWork]
- -[IMKClient_Legacy haveTISSelectCompletionBlock]
- -[IMKClient_Legacy imageFileForName:]
- -[IMKClient_Legacy initWithBundleIdentifier:isIMKExtension:]
- -[IMKClient_Legacy invalidateServerConnection]
- -[IMKClient_Legacy isClientServerTracing]
- -[IMKClient_Legacy isClientServerXPCTracing]
- -[IMKClient_Legacy isConnectionTracing]
- -[IMKClient_Legacy isDataTracingOn]
- -[IMKClient_Legacy isGeneralDebuggingOn]
- -[IMKClient_Legacy isIMKExtension]
- -[IMKClient_Legacy localizedStringForKey:]
- -[IMKClient_Legacy menuWithCompletionBlock:]
- -[IMKClient_Legacy menuWithCompletionHandler:]
- -[IMKClient_Legacy menu]
- -[IMKClient_Legacy modesWithCompletionHandler:]
- -[IMKClient_Legacy modes]
- -[IMKClient_Legacy serverDiedBadly]
- -[IMKClient_Legacy serverWillTerminate]
- -[IMKClient_Legacy setCleanTermination:]
- -[IMKClient_Legacy setCompletionBlock:]
- -[IMKClient_Legacy setCurrentSession:]
- -[IMKClient_Legacy setServerDiedBadly:]
- -[IMKClient_Legacy setTISSelectCompletionBlock:]
- -[IMKClient_Legacy set_waitingForMenu:]
- -[IMKClient_Legacy shouldUseXPC]
- -[IMKClient_Legacy switchedInputMode:]
- -[IMKClient_Legacy switchedInputMode:completionHandler:]
- -[IMKClient_Legacy tisSelectCompletionBlock]
- -[IMKClient_Legacy(IMKClientConnection_XPC) _getServerXPCProxyForSession:]
- -[IMKClient_Legacy(IMKClientConnection_XPC) _invalidateXPCConnectionEndpoint]
- -[IMKClient_Legacy(IMKClientConnection_XPC) _receiveXPCConnectionEndpoint:]
- -[IMKClient_Legacy(IMKClientConnection_XPC) inputMethodXPCEndpoint]
- -[IMKClient_Legacy(IMKClientConnection_XPC) invalidateIMKXPCEndpointForBundleIdentifier:]
- -[IMKClient_Legacy(IMKClientConnection_XPC) remoteXPCProxyForSession:fromCaller:]
- -[IMKClient_Legacy(IMKClientConnection_XPC) setIMKXPCEndpoint:forBundleIdentifier:]
- -[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]
- -[IMKClient_Modern _addActionFrom:toDictionary:forCarbonMenu:base:]
- -[IMKClient_Modern _buildSelectorDictionaryFromMenuDict:settingCommandID:]
- -[IMKClient_Modern _bumpTimeout]
- -[IMKClient_Modern _bundle]
- -[IMKClient_Modern _cancelGetServerRetry]
- -[IMKClient_Modern _checkSetTISCompletionBlock]
- -[IMKClient_Modern _createAndInstallMenuSetSelectorDictFromMenuDict:]
- -[IMKClient_Modern _defaultTimeout]
- -[IMKClient_Modern _eventHandlerRef]
- -[IMKClient_Modern _getServerRetry]
- -[IMKClient_Modern _haveSafeServerProxy:]
- -[IMKClient_Modern _inputMethodInfoDictionary]
- -[IMKClient_Modern _isNonLaunchOption]
- -[IMKClient_Modern _isPalette]
- -[IMKClient_Modern _isServerRetryPending]
- -[IMKClient_Modern _launch:fromBundle:throughPort:usingSBExtension:]
- -[IMKClient_Modern _mapKeyCodeToInputSource:modifiers:]
- -[IMKClient_Modern _mapKeyCodeToInputSource:modifiers:completionHandler:]
- -[IMKClient_Modern _modeMenuKeysWithCompletionHandler:]
- -[IMKClient_Modern _modeMenuKeys]
- -[IMKClient_Modern _requestGetServerRetryNotifyingTarget:withSelector:]
- -[IMKClient_Modern _selectorDictionary]
- -[IMKClient_Modern _senderIsInvalid:]
- -[IMKClient_Modern _setBundleIdentifier:]
- -[IMKClient_Modern _setEventHandlerRef:]
- -[IMKClient_Modern _setSelectorDictionary:]
- -[IMKClient_Modern _setTargetForServerRetry:]
- -[IMKClient_Modern _startServer_AllowingSandboxExtension:]
- -[IMKClient_Modern _targetForServerRetry]
- -[IMKClient_Modern _timeout]
- -[IMKClient_Modern _untargetFromServerRetry:]
- -[IMKClient_Modern _waitingForMenu]
- -[IMKClient_Modern bundleIdentifier]
- -[IMKClient_Modern cleanTermination]
- -[IMKClient_Modern completionBlock]
- -[IMKClient_Modern currentSession]
- -[IMKClient_Modern dealloc]
- -[IMKClient_Modern fulfillServerDependentWork]
- -[IMKClient_Modern haveTISSelectCompletionBlock]
- -[IMKClient_Modern imageFileForName:]
- -[IMKClient_Modern initWithBundleIdentifier:isIMKExtension:]
- -[IMKClient_Modern invalidateServerConnection]
- -[IMKClient_Modern isClientServerTracing]
- -[IMKClient_Modern isClientServerXPCTracing]
- -[IMKClient_Modern isConnectionTracing]
- -[IMKClient_Modern isDataTracingOn]
- -[IMKClient_Modern isGeneralDebuggingOn]
- -[IMKClient_Modern isIMKExtension]
- -[IMKClient_Modern localizedStringForKey:]
- -[IMKClient_Modern menuWithCompletionBlock:]
- -[IMKClient_Modern menuWithCompletionHandler:]
- -[IMKClient_Modern menu]
- -[IMKClient_Modern modesWithCompletionHandler:]
- -[IMKClient_Modern modes]
- -[IMKClient_Modern serverDiedBadly]
- -[IMKClient_Modern serverWillTerminate]
- -[IMKClient_Modern setCleanTermination:]
- -[IMKClient_Modern setCompletionBlock:]
- -[IMKClient_Modern setCurrentSession:]
- -[IMKClient_Modern setServerDiedBadly:]
- -[IMKClient_Modern setTISSelectCompletionBlock:]
- -[IMKClient_Modern set_waitingForMenu:]
- -[IMKClient_Modern shouldUseXPC]
- -[IMKClient_Modern switchedInputMode:]
- -[IMKClient_Modern switchedInputMode:completionHandler:]
- -[IMKClient_Modern tisSelectCompletionBlock]
- -[IMKInputSessionInvocationSentinel_Legacy dealloc]
- -[IMKInputSessionInvocationSentinel_Legacy init]
- -[IMKInputSessionInvocationSentinel_Legacy isMarkedDone]
- -[IMKInputSessionInvocationSentinel_Legacy markDone]
- -[IMKInputSessionXPCInvocation_Legacy addReplyTimerToRunloop]
- -[IMKInputSessionXPCInvocation_Legacy configureObservers]
- -[IMKInputSessionXPCInvocation_Legacy configureReplyTimerWithTimeout:]
- -[IMKInputSessionXPCInvocation_Legacy dealloc]
- -[IMKInputSessionXPCInvocation_Legacy handleInvocationAwaitXPCReplyDidTimeout]
- -[IMKInputSessionXPCInvocation_Legacy handlePrivateRunloopRunResult:]
- -[IMKInputSessionXPCInvocation_Legacy handlePrivateRunloopRunResult:].cold.1
- -[IMKInputSessionXPCInvocation_Legacy handleRunloopObservationWithObserver:activity:]
- -[IMKInputSessionXPCInvocation_Legacy initWithSession:selector:]
- -[IMKInputSessionXPCInvocation_Legacy invocationAwaitXPCReply]
- -[IMKInputSessionXPCInvocation_Legacy invocationInterruptXPCReply]
- -[IMKInputSessionXPCInvocation_Legacy isMarkedDone]
- -[IMKInputSessionXPCInvocation_Legacy markDone]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_0_innerRunLoop0:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_0_innerRunLoop1:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_0_innerRunLoop2:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_0_innerRunLoop3:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_1_innerRunLoop0:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_1_innerRunLoop1:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_1_innerRunLoop2:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_1_innerRunLoop3:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_2_innerRunLoop0:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_2_innerRunLoop1:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_2_innerRunLoop2:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_2_innerRunLoop3:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_3_innerRunLoop0:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_3_innerRunLoop1:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_3_innerRunLoop2:]
- -[IMKInputSessionXPCInvocation_Legacy runPrivateRunloopWithTimeLimit_3_innerRunLoop3:]
- -[IMKInputSessionXPCInvocation_Legacy runloopObservedActivityEntry]
- -[IMKInputSessionXPCInvocation_Legacy runloopObservedActivityExit]
- -[IMKInputSessionXPCInvocation_Legacy sentinel]
- -[IMKInputSessionXPCInvocation_Legacy teardownInvocationAwaitXPCReply]
- -[IMKInputSessionXPCInvocation_Legacy test_surpriseInnerRunloop]
- -[IMKInputSessionXPCInvocation_Legacy timedOut]
- -[IMKInputSessionXPCInvocation_Legacy verbose_runPrivateRunLoopWithTimeLimit:waitIteration:]
- -[IMKInputSessionXPCInvocation_Modern dealloc]
- -[IMKInputSessionXPCInvocation_Modern initWithSession:selector:]
- -[IMKInputSessionXPCInvocation_Modern invocationAwaitXPCReply]
- -[IMKInputSessionXPCInvocation_Modern invocationInterruptXPCReply]
- -[IMKInputSessionXPCInvocation_Modern timedOut]
- -[IMKInputSession_Legacy _TIPropertyValueIsValid:]
- -[IMKInputSession_Legacy _addLineInformationFromCarbonEvent:toDictionary:]
- -[IMKInputSession_Legacy _addString:toEventRef:]
- -[IMKInputSession_Legacy _adjustAttachmentAttributes_forInsertText:]
- -[IMKInputSession_Legacy _adjustChromaticIMKAttributes_forSetMarkedText:]
- -[IMKInputSession_Legacy _adjustIronwoodAttributes_forInsertText:]
- -[IMKInputSession_Legacy _adjustIronwoodAttributes_forSetMarkedText:]
- -[IMKInputSession_Legacy _adjustServerStringAttributes_forInsertText:]
- -[IMKInputSession_Legacy _adjustServerStringAttributes_forSetMarkedText:]
- -[IMKInputSession_Legacy _allowRetryOnInvalidPortException]
- -[IMKInputSession_Legacy _attributesFromRangeViaGetSelectedText:completionHandler:]
- -[IMKInputSession_Legacy _attributesToHighlightStyle:fallback:isChromaticMarkedText:]
- -[IMKInputSession_Legacy _blankEvent:kind:]
- -[IMKInputSession_Legacy _closeInputPalette_withCompletionHandler:]
- -[IMKInputSession_Legacy _commitOnMouseDown:completionHandler:]
- -[IMKInputSession_Legacy _copyPaletteInputSource]
- -[IMKInputSession_Legacy _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]
- -[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]
- -[IMKInputSession_Legacy _createAndSendOffsetToPointEvent:completionHandler:]
- -[IMKInputSession_Legacy _eventIsOn:completionHandler:]
- -[IMKInputSession_Legacy _glyphAttributesFromEventRef:forString:]
- -[IMKInputSession_Legacy _glyphInfoData:]
- -[IMKInputSession_Legacy _heightFromFontData:]
- -[IMKInputSession_Legacy _postEvent:completionHandler:]
- -[IMKInputSession_Legacy _showHideInputWindow:completionHandler:]
- -[IMKInputSession_Legacy _supportsDocumentAccess]
- -[IMKInputSession_Legacy _unicodeTextEventFromString:]
- -[IMKInputSession_Legacy _unmarkEventFromString:]
- -[IMKInputSession_Legacy _unmarkIMKMarkedRange]
- -[IMKInputSession_Legacy _updateEventFromAttributedString:pinRange:replacementRange:resultShouldUnmark:resultLength:]
- -[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]
- -[IMKInputSession_Legacy activateAfterServerConnection]
- -[IMKInputSession_Legacy activatePending]
- -[IMKInputSession_Legacy activate]
- -[IMKInputSession_Legacy addPendingEvent:withUniqueSeqNum:]
- -[IMKInputSession_Legacy attributedSubstringFromRange:]
- -[IMKInputSession_Legacy attributedSubstringFromRange:completionHandler:]
- -[IMKInputSession_Legacy attributesForCharacterIndex:]
- -[IMKInputSession_Legacy attributesForCharacterIndex:completionHandler:]
- -[IMKInputSession_Legacy attributesForCharacterIndex:lineHeightRectangle:]
- -[IMKInputSession_Legacy attributesForCharacterIndex_andLineRect:completionHandler:]
- -[IMKInputSession_Legacy bundleIdentifier]
- -[IMKInputSession_Legacy characterIndexForPoint:tracking:completionHandler:]
- -[IMKInputSession_Legacy characterIndexForPoint:tracking:inMarkedRange:]
- -[IMKInputSession_Legacy client]
- -[IMKInputSession_Legacy commitComposition]
- -[IMKInputSession_Legacy commitPendingInlineSession]
- -[IMKInputSession_Legacy currentInputSourceBundleID]
- -[IMKInputSession_Legacy deactivate]
- -[IMKInputSession_Legacy deadKeyState]
- -[IMKInputSession_Legacy dealloc]
- -[IMKInputSession_Legacy deferredActivateHaveEventsQueued]
- -[IMKInputSession_Legacy deferredActivateHaveInputSessionActionsQueued]
- -[IMKInputSession_Legacy deferredActivateInputMode]
- -[IMKInputSession_Legacy deferredActivatePending]
- -[IMKInputSession_Legacy didActivate]
- -[IMKInputSession_Legacy didCommandBySelector:]
- -[IMKInputSession_Legacy didCommandBySelector:completionHandler:]
- -[IMKInputSession_Legacy dismissFunctionRowItemTextInputView]
- -[IMKInputSession_Legacy doCommandBySelector:commandDictionary:]
- -[IMKInputSession_Legacy do_coreAttributesFromRange_postEventLoopWithContext:initBlockEach:postEventCompletionEach:whileConditionBlock:finalCompletion:]
- -[IMKInputSession_Legacy enqueueDeferredActivateInputSessionAction:timestamp:withInfo:]
- -[IMKInputSession_Legacy enqueueEventForDeferredActivate:]
- -[IMKInputSession_Legacy fetchViewServiceEndpointWithCompletionHandler:]
- -[IMKInputSession_Legacy finishSession]
- -[IMKInputSession_Legacy firstRectForCharacterRange:actualRange:]
- -[IMKInputSession_Legacy firstRectForCharacterRange:completionHandler:]
- -[IMKInputSession_Legacy handleEvent:completionHandler:]
- -[IMKInputSession_Legacy hidePalettesAtInsertionPoint]
- -[IMKInputSession_Legacy hidePalettes]
- -[IMKInputSession_Legacy imkxpc_attributedSubstringFromRange:reply:]
- -[IMKInputSession_Legacy imkxpc_attributesForCharacterIndex:reply:]
- -[IMKInputSession_Legacy imkxpc_bundleIdentifierWithReply:]
- -[IMKInputSession_Legacy imkxpc_characterIndexForPoint:tracking:reply:]
- -[IMKInputSession_Legacy imkxpc_commitPendingInlineSessionWithReply:]
- -[IMKInputSession_Legacy imkxpc_currentInputSourceBundleIDWithReply:]
- -[IMKInputSession_Legacy imkxpc_deadKeyStateWithReply:]
- -[IMKInputSession_Legacy imkxpc_dismissFunctionRowItemTextInputViewWithReply:]
- -[IMKInputSession_Legacy imkxpc_firstRectForCharacterRange:reply:]
- -[IMKInputSession_Legacy imkxpc_getApplicationProperty:reply:]
- -[IMKInputSession_Legacy imkxpc_hidePalettesAtInsertionPointWithReply:]
- -[IMKInputSession_Legacy imkxpc_incrementalSearchClientGeometryWithReply:]
- -[IMKInputSession_Legacy imkxpc_inputSessionDoneSleepWithReply:]
- -[IMKInputSession_Legacy imkxpc_insertText:replacementRange:validFlags:reply:]
- -[IMKInputSession_Legacy imkxpc_insertText:reply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticCapitalizationEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticDashSubstitutionEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticPeriodSubstitutionEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticQuoteSubstitutionEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticSpellingCorrectionEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticTextCompletionEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isAutomaticTextReplacementEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isBottomLineInputContextWithReply:]
- -[IMKInputSession_Legacy imkxpc_isContinuousSpellCheckingEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isDictationHiliteCapableInputContextWithReply:]
- -[IMKInputSession_Legacy imkxpc_isGrammarCheckingEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isIncrementalSearchInputContextWithReply:]
- -[IMKInputSession_Legacy imkxpc_isPaletteTerminated:reply:]
- -[IMKInputSession_Legacy imkxpc_isSmartInsertDeleteEnabledWithReply:]
- -[IMKInputSession_Legacy imkxpc_isTextPlaceholderAwareInputContextWithReply:]
- -[IMKInputSession_Legacy imkxpc_lengthWithReply:]
- -[IMKInputSession_Legacy imkxpc_markedRangeValueWithReply:]
- -[IMKInputSession_Legacy imkxpc_overrideKeyboardWithKeyboardNamed:reply:]
- -[IMKInputSession_Legacy imkxpc_passSanityCheckAsyncClient:]
- -[IMKInputSession_Legacy imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]
- -[IMKInputSession_Legacy imkxpc_selectInputMode:reply:]
- -[IMKInputSession_Legacy imkxpc_selectedRangeWithReply:]
- -[IMKInputSession_Legacy imkxpc_setApplicationProperty:value:]
- -[IMKInputSession_Legacy imkxpc_setApplicationProperty:value:reply:]
- -[IMKInputSession_Legacy imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]
- -[IMKInputSession_Legacy imkxpc_stringFromRange:reply:]
- -[IMKInputSession_Legacy imkxpc_supportsChromaticMarkedTextWithReply:]
- -[IMKInputSession_Legacy imkxpc_supportsProperty:reply:]
- -[IMKInputSession_Legacy imkxpc_supportsTextAttachmentInsertionWithReply:]
- -[IMKInputSession_Legacy imkxpc_supportsUnicodeWithReply:]
- -[IMKInputSession_Legacy imkxpc_terminatePalette:reply:]
- -[IMKInputSession_Legacy imkxpc_uniqueClientIdentifierStringWithReply:]
- -[IMKInputSession_Legacy imkxpc_updateMenusDictionary:]
- -[IMKInputSession_Legacy imkxpc_validAttributesForMarkedTextWithReply:]
- -[IMKInputSession_Legacy imkxpc_viewEffectiveAppearanceNameWithReply:]
- -[IMKInputSession_Legacy imkxpc_viewEffectiveAppearanceWithReply:]
- -[IMKInputSession_Legacy imkxpc_windowEffectiveAppearanceNameWithReply:]
- -[IMKInputSession_Legacy imkxpc_windowEffectiveAppearanceWithReply:]
- -[IMKInputSession_Legacy imkxpc_windowLevelWithReply:]
- -[IMKInputSession_Legacy imkxpc_wouldHandleEvent:reply:]
- -[IMKInputSession_Legacy incrementalSearchClientGeometry]
- -[IMKInputSession_Legacy initWithClient:document:]
- -[IMKInputSession_Legacy inputMethodXPCConnection]
- -[IMKInputSession_Legacy inputSessionDoneSleep]
- -[IMKInputSession_Legacy insertPlaceholderCachedWeakRef:forKey:]
- -[IMKInputSession_Legacy insertText:]
- -[IMKInputSession_Legacy insertText:completionHandler:]
- -[IMKInputSession_Legacy insertText:replacementRange:]
- -[IMKInputSession_Legacy insertText:replacementRange:completionHandler:]
- -[IMKInputSession_Legacy insertText:replacementRange:validFlags:]
- -[IMKInputSession_Legacy insertText:replacementRange:validFlags:completionHandler:]
- -[IMKInputSession_Legacy invalidateAllPendingEvents]
- -[IMKInputSession_Legacy invalidateClientGeometry]
- -[IMKInputSession_Legacy ironwoodInputSessionPlaceholderWasInvalidated:]
- -[IMKInputSession_Legacy ironwoodInputSessionTextWasCorrected:]
- -[IMKInputSession_Legacy isAutomaticCapitalizationEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isAutomaticDashSubstitutionEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isAutomaticPeriodSubstitutionEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isAutomaticQuoteSubstitutionEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isAutomaticSpellingCorrectionEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isAutomaticTextCompletionEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isAutomaticTextReplacementEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isBottomLineInputContext]
- -[IMKInputSession_Legacy isContinuousSpellCheckingEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isDictationHiliteCapableInputContext]
- -[IMKInputSession_Legacy isFixTSMIsFromDiscardMarkedText]
- -[IMKInputSession_Legacy isGrammarCheckingEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isIncrementalSearchInputContext]
- -[IMKInputSession_Legacy isPaletteTerminated:]
- -[IMKInputSession_Legacy isSmartInsertDeleteEnabled_WithAvailability:]
- -[IMKInputSession_Legacy isTextPlaceholderAwareInputContext]
- -[IMKInputSession_Legacy length]
- -[IMKInputSession_Legacy length_withCompletionHandler:]
- -[IMKInputSession_Legacy lookupPlaceholderCachedWeakRef:]
- -[IMKInputSession_Legacy markedRangeValue]
- -[IMKInputSession_Legacy markedRange]
- -[IMKInputSession_Legacy overrideKeyboardWithKeyboardNamed:]
- -[IMKInputSession_Legacy presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:]
- -[IMKInputSession_Legacy presentFunctionRowItemTextInputView]
- -[IMKInputSession_Legacy queuedDeferredEvents]
- -[IMKInputSession_Legacy queuedInputSessionActions]
- -[IMKInputSession_Legacy removePlaceholderCachedWeakRef:]
- -[IMKInputSession_Legacy replyWaitCount_decrementWithLocking]
- -[IMKInputSession_Legacy replyWaitCount_incrementWithLocking]
- -[IMKInputSession_Legacy replyWaitCount_lockDecrement]
- -[IMKInputSession_Legacy replyWaitCount_lockIncrement]
- -[IMKInputSession_Legacy replyWaitCount_testWithLocking]
- -[IMKInputSession_Legacy replyWaitCount_unlock]
- -[IMKInputSession_Legacy resetDeferredActivateInputSessionQueuedActions]
- -[IMKInputSession_Legacy resetDeferredActivateQueuedEvents]
- -[IMKInputSession_Legacy selectInputMode:]
- -[IMKInputSession_Legacy selectedRange]
- -[IMKInputSession_Legacy selectedRange_withCompletionHandler:]
- -[IMKInputSession_Legacy sendInputSessionSessAction:timestamp:withInfo:]
- -[IMKInputSession_Legacy sessionConnectionIsInvalid:]
- -[IMKInputSession_Legacy setActivatePending:]
- -[IMKInputSession_Legacy setDeferredActivateHaveEventsQueued:]
- -[IMKInputSession_Legacy setDeferredActivateHaveInputSessionActionsQueued:]
- -[IMKInputSession_Legacy setDeferredActivateInputMode:]
- -[IMKInputSession_Legacy setDeferredActivatePending:]
- -[IMKInputSession_Legacy setDidActivate:]
- -[IMKInputSession_Legacy setInputMethodProperty:value:]
- -[IMKInputSession_Legacy setInputMethodXPCConnection:]
- -[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:]
- -[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:completionHandler:]
- -[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:validFlags:]
- -[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:validFlags:completionHandler:]
- -[IMKInputSession_Legacy setQueuedDeferredEvents:]
- -[IMKInputSession_Legacy setQueuedInputSessionActions:]
- -[IMKInputSession_Legacy setTouchBarViewController:]
- -[IMKInputSession_Legacy setValue:forTag:]
- -[IMKInputSession_Legacy set_allowRetryOnInvalidPortException:]
- -[IMKInputSession_Legacy stringFromRange:actualRange:]
- -[IMKInputSession_Legacy stringFromRange:completionHandler:]
- -[IMKInputSession_Legacy supportsChromaticMarkedText]
- -[IMKInputSession_Legacy supportsProperty:]
- -[IMKInputSession_Legacy supportsTextAttachmentInsertion]
- -[IMKInputSession_Legacy supportsUnicode]
- -[IMKInputSession_Legacy terminatePalette:]
- -[IMKInputSession_Legacy textInputContext]
- -[IMKInputSession_Legacy touchBarViewController]
- -[IMKInputSession_Legacy tryCoreAttributesFromRange_CheckForSurrogateCharacter_CopyUniCharsForRangeAdjusted_wTest:context:initialBlock:continuationBlock:]
- -[IMKInputSession_Legacy tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]
- -[IMKInputSession_Legacy tryHandleEventSwitchedInputMode:eventWasHandled:continuationHandler:]
- -[IMKInputSession_Legacy tryHandleEvent_GetOffsetAndLocationForMouseEvent__withDispatchCondition:initialization:dispatchWork:postEventCompletion:continuationHandler:]
- -[IMKInputSession_Legacy tryHandleEvent_commitOnMouseDown_withDispatchCondition:dispatchWork:continuation:]
- -[IMKInputSession_Legacy tryUpdateIMKMarkedRange_withDispatchCondition:dispatchWork:continuation:]
- -[IMKInputSession_Legacy uniqueClientIdentifierString]
- -[IMKInputSession_Legacy unmarkTextInClient]
- -[IMKInputSession_Legacy validAttributesForMarkedText]
- -[IMKInputSession_Legacy valueForTag:]
- -[IMKInputSession_Legacy valueForTag:completionHandler:]
- -[IMKInputSession_Legacy viewEffectiveAppearance]
- -[IMKInputSession_Legacy windowEffectiveAppearance]
- -[IMKInputSession_Legacy windowLevel]
- -[IMKInputSession_Legacy wouldHandleEvent:completionHandler:]
- -[IMKInputSession_Modern _TIPropertyValueIsValid:]
- -[IMKInputSession_Modern _addLineInformationFromCarbonEvent:toDictionary:]
- -[IMKInputSession_Modern _addString:toEventRef:]
- -[IMKInputSession_Modern _adjustAttachmentAttributes_forInsertText:]
- -[IMKInputSession_Modern _adjustChromaticIMKAttributes_forSetMarkedText:]
- -[IMKInputSession_Modern _adjustIronwoodAttributes_forInsertText:]
- -[IMKInputSession_Modern _adjustIronwoodAttributes_forSetMarkedText:]
- -[IMKInputSession_Modern _adjustServerStringAttributes_forInsertText:]
- -[IMKInputSession_Modern _adjustServerStringAttributes_forSetMarkedText:]
- -[IMKInputSession_Modern _allowRetryOnInvalidPortException]
- -[IMKInputSession_Modern _attributesFromRangeViaGetSelectedText:completionHandler:]
- -[IMKInputSession_Modern _attributesToHighlightStyle:fallback:isChromaticMarkedText:]
- -[IMKInputSession_Modern _blankEvent:kind:]
- -[IMKInputSession_Modern _closeInputPalette_withCompletionHandler:]
- -[IMKInputSession_Modern _commitOnMouseDown:completionHandler:]
- -[IMKInputSession_Modern _copyPaletteInputSource]
- -[IMKInputSession_Modern _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]
- -[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]
- -[IMKInputSession_Modern _createAndSendOffsetToPointEvent:completionHandler:]
- -[IMKInputSession_Modern _eventIsOn:completionHandler:]
- -[IMKInputSession_Modern _glyphAttributesFromEventRef:forString:]
- -[IMKInputSession_Modern _glyphInfoData:]
- -[IMKInputSession_Modern _heightFromFontData:]
- -[IMKInputSession_Modern _postEvent:completionHandler:]
- -[IMKInputSession_Modern _showHideInputWindow:completionHandler:]
- -[IMKInputSession_Modern _supportsDocumentAccess]
- -[IMKInputSession_Modern _unicodeTextEventFromString:]
- -[IMKInputSession_Modern _unmarkEventFromString:]
- -[IMKInputSession_Modern _unmarkIMKMarkedRange]
- -[IMKInputSession_Modern _updateEventFromAttributedString:pinRange:replacementRange:resultShouldUnmark:resultLength:]
- -[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]
- -[IMKInputSession_Modern activateAfterServerConnection]
- -[IMKInputSession_Modern activatePending]
- -[IMKInputSession_Modern activate]
- -[IMKInputSession_Modern addPendingEvent:withUniqueSeqNum:]
- -[IMKInputSession_Modern attributedSubstringFromRange:]
- -[IMKInputSession_Modern attributedSubstringFromRange:completionHandler:]
- -[IMKInputSession_Modern attributesForCharacterIndex:]
- -[IMKInputSession_Modern attributesForCharacterIndex:completionHandler:]
- -[IMKInputSession_Modern attributesForCharacterIndex:lineHeightRectangle:]
- -[IMKInputSession_Modern attributesForCharacterIndex_andLineRect:completionHandler:]
- -[IMKInputSession_Modern bundleIdentifier]
- -[IMKInputSession_Modern characterIndexForPoint:tracking:completionHandler:]
- -[IMKInputSession_Modern characterIndexForPoint:tracking:inMarkedRange:]
- -[IMKInputSession_Modern client]
- -[IMKInputSession_Modern commitComposition]
- -[IMKInputSession_Modern commitPendingInlineSession]
- -[IMKInputSession_Modern currentInputSourceBundleID]
- -[IMKInputSession_Modern deactivate]
- -[IMKInputSession_Modern deadKeyState]
- -[IMKInputSession_Modern dealloc]
- -[IMKInputSession_Modern deferredActivateHaveEventsQueued]
- -[IMKInputSession_Modern deferredActivateHaveInputSessionActionsQueued]
- -[IMKInputSession_Modern deferredActivateInputMode]
- -[IMKInputSession_Modern deferredActivatePending]
- -[IMKInputSession_Modern didActivate]
- -[IMKInputSession_Modern didCommandBySelector:]
- -[IMKInputSession_Modern didCommandBySelector:completionHandler:]
- -[IMKInputSession_Modern dismissFunctionRowItemTextInputView]
- -[IMKInputSession_Modern doCommandBySelector:commandDictionary:]
- -[IMKInputSession_Modern do_coreAttributesFromRange_postEventLoopWithContext:initBlockEach:postEventCompletionEach:whileConditionBlock:finalCompletion:]
- -[IMKInputSession_Modern enqueueDeferredActivateInputSessionAction:timestamp:withInfo:]
- -[IMKInputSession_Modern enqueueEventForDeferredActivate:]
- -[IMKInputSession_Modern fetchViewServiceEndpointWithCompletionHandler:]
- -[IMKInputSession_Modern finishSession]
- -[IMKInputSession_Modern firstRectForCharacterRange:actualRange:]
- -[IMKInputSession_Modern firstRectForCharacterRange:completionHandler:]
- -[IMKInputSession_Modern handleEvent:completionHandler:]
- -[IMKInputSession_Modern hidePalettesAtInsertionPoint]
- -[IMKInputSession_Modern hidePalettes]
- -[IMKInputSession_Modern imkxpc_attributedSubstringFromRange:reply:]
- -[IMKInputSession_Modern imkxpc_attributesForCharacterIndex:reply:]
- -[IMKInputSession_Modern imkxpc_bundleIdentifierWithReply:]
- -[IMKInputSession_Modern imkxpc_characterIndexForPoint:tracking:reply:]
- -[IMKInputSession_Modern imkxpc_commitPendingInlineSessionWithReply:]
- -[IMKInputSession_Modern imkxpc_currentInputSourceBundleIDWithReply:]
- -[IMKInputSession_Modern imkxpc_deadKeyStateWithReply:]
- -[IMKInputSession_Modern imkxpc_dismissFunctionRowItemTextInputViewWithReply:]
- -[IMKInputSession_Modern imkxpc_firstRectForCharacterRange:reply:]
- -[IMKInputSession_Modern imkxpc_getApplicationProperty:reply:]
- -[IMKInputSession_Modern imkxpc_hidePalettesAtInsertionPointWithReply:]
- -[IMKInputSession_Modern imkxpc_incrementalSearchClientGeometryWithReply:]
- -[IMKInputSession_Modern imkxpc_inputSessionDoneSleepWithReply:]
- -[IMKInputSession_Modern imkxpc_insertText:replacementRange:validFlags:reply:]
- -[IMKInputSession_Modern imkxpc_insertText:reply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticCapitalizationEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticDashSubstitutionEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticPeriodSubstitutionEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticQuoteSubstitutionEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticSpellingCorrectionEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticTextCompletionEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isAutomaticTextReplacementEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isBottomLineInputContextWithReply:]
- -[IMKInputSession_Modern imkxpc_isContinuousSpellCheckingEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isDictationHiliteCapableInputContextWithReply:]
- -[IMKInputSession_Modern imkxpc_isGrammarCheckingEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isIncrementalSearchInputContextWithReply:]
- -[IMKInputSession_Modern imkxpc_isPaletteTerminated:reply:]
- -[IMKInputSession_Modern imkxpc_isSmartInsertDeleteEnabledWithReply:]
- -[IMKInputSession_Modern imkxpc_isTextPlaceholderAwareInputContextWithReply:]
- -[IMKInputSession_Modern imkxpc_lengthWithReply:]
- -[IMKInputSession_Modern imkxpc_markedRangeValueWithReply:]
- -[IMKInputSession_Modern imkxpc_overrideKeyboardWithKeyboardNamed:reply:]
- -[IMKInputSession_Modern imkxpc_passSanityCheckAsyncClient:]
- -[IMKInputSession_Modern imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]
- -[IMKInputSession_Modern imkxpc_selectInputMode:reply:]
- -[IMKInputSession_Modern imkxpc_selectedRangeWithReply:]
- -[IMKInputSession_Modern imkxpc_setApplicationProperty:value:]
- -[IMKInputSession_Modern imkxpc_setApplicationProperty:value:reply:]
- -[IMKInputSession_Modern imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]
- -[IMKInputSession_Modern imkxpc_stringFromRange:reply:]
- -[IMKInputSession_Modern imkxpc_supportsChromaticMarkedTextWithReply:]
- -[IMKInputSession_Modern imkxpc_supportsProperty:reply:]
- -[IMKInputSession_Modern imkxpc_supportsTextAttachmentInsertionWithReply:]
- -[IMKInputSession_Modern imkxpc_supportsUnicodeWithReply:]
- -[IMKInputSession_Modern imkxpc_terminatePalette:reply:]
- -[IMKInputSession_Modern imkxpc_uniqueClientIdentifierStringWithReply:]
- -[IMKInputSession_Modern imkxpc_updateMenusDictionary:]
- -[IMKInputSession_Modern imkxpc_validAttributesForMarkedTextWithReply:]
- -[IMKInputSession_Modern imkxpc_viewEffectiveAppearanceNameWithReply:]
- -[IMKInputSession_Modern imkxpc_viewEffectiveAppearanceWithReply:]
- -[IMKInputSession_Modern imkxpc_windowEffectiveAppearanceNameWithReply:]
- -[IMKInputSession_Modern imkxpc_windowEffectiveAppearanceWithReply:]
- -[IMKInputSession_Modern imkxpc_windowLevelWithReply:]
- -[IMKInputSession_Modern imkxpc_wouldHandleEvent:reply:]
- -[IMKInputSession_Modern incrementalSearchClientGeometry]
- -[IMKInputSession_Modern initWithClient:document:]
- -[IMKInputSession_Modern inputMethodXPCConnection]
- -[IMKInputSession_Modern inputSessionDoneSleep]
- -[IMKInputSession_Modern insertPlaceholderCachedWeakRef:forKey:]
- -[IMKInputSession_Modern insertText:]
- -[IMKInputSession_Modern insertText:completionHandler:]
- -[IMKInputSession_Modern insertText:replacementRange:]
- -[IMKInputSession_Modern insertText:replacementRange:completionHandler:]
- -[IMKInputSession_Modern insertText:replacementRange:validFlags:]
- -[IMKInputSession_Modern insertText:replacementRange:validFlags:completionHandler:]
- -[IMKInputSession_Modern invalidateAllPendingEvents]
- -[IMKInputSession_Modern invalidateClientGeometry]
- -[IMKInputSession_Modern ironwoodInputSessionPlaceholderWasInvalidated:]
- -[IMKInputSession_Modern ironwoodInputSessionTextWasCorrected:]
- -[IMKInputSession_Modern isAutomaticCapitalizationEnabled_WithAvailability:]
- -[IMKInputSession_Modern isAutomaticDashSubstitutionEnabled_WithAvailability:]
- -[IMKInputSession_Modern isAutomaticPeriodSubstitutionEnabled_WithAvailability:]
- -[IMKInputSession_Modern isAutomaticQuoteSubstitutionEnabled_WithAvailability:]
- -[IMKInputSession_Modern isAutomaticSpellingCorrectionEnabled_WithAvailability:]
- -[IMKInputSession_Modern isAutomaticTextCompletionEnabled_WithAvailability:]
- -[IMKInputSession_Modern isAutomaticTextReplacementEnabled_WithAvailability:]
- -[IMKInputSession_Modern isBottomLineInputContext]
- -[IMKInputSession_Modern isContinuousSpellCheckingEnabled_WithAvailability:]
- -[IMKInputSession_Modern isDictationHiliteCapableInputContext]
- -[IMKInputSession_Modern isFixTSMIsFromDiscardMarkedText]
- -[IMKInputSession_Modern isGrammarCheckingEnabled_WithAvailability:]
- -[IMKInputSession_Modern isIncrementalSearchInputContext]
- -[IMKInputSession_Modern isPaletteTerminated:]
- -[IMKInputSession_Modern isSmartInsertDeleteEnabled_WithAvailability:]
- -[IMKInputSession_Modern isTextPlaceholderAwareInputContext]
- -[IMKInputSession_Modern length]
- -[IMKInputSession_Modern length_withCompletionHandler:]
- -[IMKInputSession_Modern lookupPlaceholderCachedWeakRef:]
- -[IMKInputSession_Modern markedRangeValue]
- -[IMKInputSession_Modern markedRange]
- -[IMKInputSession_Modern overrideKeyboardWithKeyboardNamed:]
- -[IMKInputSession_Modern presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:]
- -[IMKInputSession_Modern presentFunctionRowItemTextInputView]
- -[IMKInputSession_Modern queuedDeferredEvents]
- -[IMKInputSession_Modern queuedInputSessionActions]
- -[IMKInputSession_Modern removePlaceholderCachedWeakRef:]
- -[IMKInputSession_Modern replyWaitCount_decrementWithLocking]
- -[IMKInputSession_Modern replyWaitCount_incrementWithLocking]
- -[IMKInputSession_Modern replyWaitCount_lockDecrement]
- -[IMKInputSession_Modern replyWaitCount_lockIncrement]
- -[IMKInputSession_Modern replyWaitCount_testWithLocking]
- -[IMKInputSession_Modern replyWaitCount_unlock]
- -[IMKInputSession_Modern resetDeferredActivateInputSessionQueuedActions]
- -[IMKInputSession_Modern resetDeferredActivateQueuedEvents]
- -[IMKInputSession_Modern selectInputMode:]
- -[IMKInputSession_Modern selectedRange]
- -[IMKInputSession_Modern selectedRange_withCompletionHandler:]
- -[IMKInputSession_Modern sendInputSessionSessAction:timestamp:withInfo:]
- -[IMKInputSession_Modern sessionConnectionIsInvalid:]
- -[IMKInputSession_Modern setActivatePending:]
- -[IMKInputSession_Modern setDeferredActivateHaveEventsQueued:]
- -[IMKInputSession_Modern setDeferredActivateHaveInputSessionActionsQueued:]
- -[IMKInputSession_Modern setDeferredActivateInputMode:]
- -[IMKInputSession_Modern setDeferredActivatePending:]
- -[IMKInputSession_Modern setDidActivate:]
- -[IMKInputSession_Modern setInputMethodProperty:value:]
- -[IMKInputSession_Modern setInputMethodXPCConnection:]
- -[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:]
- -[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:completionHandler:]
- -[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:validFlags:]
- -[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:validFlags:completionHandler:]
- -[IMKInputSession_Modern setQueuedDeferredEvents:]
- -[IMKInputSession_Modern setQueuedInputSessionActions:]
- -[IMKInputSession_Modern setTouchBarViewController:]
- -[IMKInputSession_Modern setValue:forTag:]
- -[IMKInputSession_Modern set_allowRetryOnInvalidPortException:]
- -[IMKInputSession_Modern stringFromRange:actualRange:]
- -[IMKInputSession_Modern stringFromRange:completionHandler:]
- -[IMKInputSession_Modern supportsChromaticMarkedText]
- -[IMKInputSession_Modern supportsProperty:]
- -[IMKInputSession_Modern supportsTextAttachmentInsertion]
- -[IMKInputSession_Modern supportsUnicode]
- -[IMKInputSession_Modern terminatePalette:]
- -[IMKInputSession_Modern textInputContext]
- -[IMKInputSession_Modern touchBarViewController]
- -[IMKInputSession_Modern tryCoreAttributesFromRange_CheckForSurrogateCharacter_CopyUniCharsForRangeAdjusted_wTest:context:initialBlock:continuationBlock:]
- -[IMKInputSession_Modern tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]
- -[IMKInputSession_Modern tryHandleEventSwitchedInputMode:eventWasHandled:continuationHandler:]
- -[IMKInputSession_Modern tryHandleEvent_GetOffsetAndLocationForMouseEvent__withDispatchCondition:initialization:dispatchWork:postEventCompletion:continuationHandler:]
- -[IMKInputSession_Modern tryHandleEvent_commitOnMouseDown_withDispatchCondition:dispatchWork:continuation:]
- -[IMKInputSession_Modern tryUpdateIMKMarkedRange_withDispatchCondition:dispatchWork:continuation:]
- -[IMKInputSession_Modern uniqueClientIdentifierString]
- -[IMKInputSession_Modern unmarkTextInClient]
- -[IMKInputSession_Modern validAttributesForMarkedText]
- -[IMKInputSession_Modern valueForTag:]
- -[IMKInputSession_Modern valueForTag:completionHandler:]
- -[IMKInputSession_Modern viewEffectiveAppearance]
- -[IMKInputSession_Modern whileAwaitingReplyPerformActions:]
- -[IMKInputSession_Modern windowEffectiveAppearance]
- -[IMKInputSession_Modern windowLevel]
- -[IMKInputSession_Modern wouldHandleEvent:completionHandler:]
- -[IMKQueuedEventRef_Legacy dealloc]
- -[IMKQueuedEventRef_Legacy eventRef]
- -[IMKQueuedEventRef_Legacy initWithEventRef:]
- -[IMKQueuedEventRef_Modern dealloc]
- -[IMKQueuedEventRef_Modern eventRef]
- -[IMKQueuedEventRef_Modern initWithEventRef:]
- -[IPMDFontRange_Legacy dealloc]
- -[IPMDFontRange_Legacy font]
- -[IPMDFontRange_Legacy rangeValue]
- -[IPMDFontRange_Modern dealloc]
- -[IPMDFontRange_Modern font]
- -[IPMDFontRange_Modern rangeValue]
- GCC_except_table112
- GCC_except_table114
- GCC_except_table129
- GCC_except_table142
- GCC_except_table147
- GCC_except_table156
- GCC_except_table332
- GCC_except_table373
- GCC_except_table378
- GCC_except_table382
- GCC_except_table390
- GCC_except_table396
- GCC_except_table415
- GCC_except_table420
- GCC_except_table479
- GCC_except_table480
- GCC_except_table69
- OBJC_IVAR_$_IMKClient.__waitingForMenu
- OBJC_IVAR_$_IMKClientInvocationSentinel_Legacy._int
- OBJC_IVAR_$_IMKClientXPCInvocation_Legacy._callerSelector
- OBJC_IVAR_$_IMKClientXPCInvocation_Legacy._replyTimer
- OBJC_IVAR_$_IMKClientXPCInvocation_Legacy._request_reply_done
- OBJC_IVAR_$_IMKClientXPCInvocation_Legacy._sentinel
- OBJC_IVAR_$_IMKClientXPCInvocation_Legacy._timedOut
- OBJC_IVAR_$_IMKClientXPCInvocation_Legacy._timeout
- OBJC_IVAR_$_IMKClientXPCInvocation_Modern._callerSelector
- OBJC_IVAR_$_IMKClientXPCInvocation_Modern._timeOutStatus
- OBJC_IVAR_$_IMKClientXPCInvocation_Modern._timeout
- OBJC_IVAR_$_IMKClient_Legacy._bundle
- OBJC_IVAR_$_IMKClient_Legacy._bundleIdentifier
- OBJC_IVAR_$_IMKClient_Legacy._cleanTermination
- OBJC_IVAR_$_IMKClient_Legacy._clientHasDied
- OBJC_IVAR_$_IMKClient_Legacy._connection
- OBJC_IVAR_$_IMKClient_Legacy._currentSession
- OBJC_IVAR_$_IMKClient_Legacy._eventHandlerRef
- OBJC_IVAR_$_IMKClient_Legacy._exceptionTimeoutBumpCount
- OBJC_IVAR_$_IMKClient_Legacy._getServerGetMenuWasCalledDuringRetry
- OBJC_IVAR_$_IMKClient_Legacy._getServerRetryCount
- OBJC_IVAR_$_IMKClient_Legacy._getServerRetryNotificationSel
- OBJC_IVAR_$_IMKClient_Legacy._getServerRetryNotificationTarget
- OBJC_IVAR_$_IMKClient_Legacy._getServerRetryPending
- OBJC_IVAR_$_IMKClient_Legacy._inputMethodInfoDictionary
- OBJC_IVAR_$_IMKClient_Legacy._inputMethodXPCEndpoint
- OBJC_IVAR_$_IMKClient_Legacy._isIMKExtension
- OBJC_IVAR_$_IMKClient_Legacy._isServerStarted
- OBJC_IVAR_$_IMKClient_Legacy._launchPort
- OBJC_IVAR_$_IMKClient_Legacy._launcherXPCConnection
- OBJC_IVAR_$_IMKClient_Legacy._lookedForMenuKeys
- OBJC_IVAR_$_IMKClient_Legacy._modeMenuKeys
- OBJC_IVAR_$_IMKClient_Legacy._modes
- OBJC_IVAR_$_IMKClient_Legacy._remoteProxyLock
- OBJC_IVAR_$_IMKClient_Legacy._selectorDictionary
- OBJC_IVAR_$_IMKClient_Legacy._serverConnection
- OBJC_IVAR_$_IMKClient_Legacy._serverDOProxy
- OBJC_IVAR_$_IMKClient_Legacy._serverDiedBadly
- OBJC_IVAR_$_IMKClient_Legacy._serverName
- OBJC_IVAR_$_IMKClient_Legacy._timeout
- OBJC_IVAR_$_IMKClient_Legacy._tisSelectInputSourceCompletionBlock
- OBJC_IVAR_$_IMKClient_Legacy._waitingForMenu
- OBJC_IVAR_$_IMKClient_Legacy.completionBlock
- OBJC_IVAR_$_IMKClient_Legacy.localizedStrings
- OBJC_IVAR_$_IMKClient_Modern._bundle
- OBJC_IVAR_$_IMKClient_Modern._bundleIdentifier
- OBJC_IVAR_$_IMKClient_Modern._cleanTermination
- OBJC_IVAR_$_IMKClient_Modern._clientHasDied
- OBJC_IVAR_$_IMKClient_Modern._connection
- OBJC_IVAR_$_IMKClient_Modern._currentSession
- OBJC_IVAR_$_IMKClient_Modern._eventHandlerRef
- OBJC_IVAR_$_IMKClient_Modern._exceptionTimeoutBumpCount
- OBJC_IVAR_$_IMKClient_Modern._getServerGetMenuWasCalledDuringRetry
- OBJC_IVAR_$_IMKClient_Modern._getServerRetryCount
- OBJC_IVAR_$_IMKClient_Modern._getServerRetryNotificationSel
- OBJC_IVAR_$_IMKClient_Modern._getServerRetryNotificationTarget
- OBJC_IVAR_$_IMKClient_Modern._getServerRetryPending
- OBJC_IVAR_$_IMKClient_Modern._inputMethodInfoDictionary
- OBJC_IVAR_$_IMKClient_Modern._inputMethodXPCEndpoint
- OBJC_IVAR_$_IMKClient_Modern._isIMKExtension
- OBJC_IVAR_$_IMKClient_Modern._isServerStarted
- OBJC_IVAR_$_IMKClient_Modern._launchPort
- OBJC_IVAR_$_IMKClient_Modern._launcherXPCConnection
- OBJC_IVAR_$_IMKClient_Modern._lookedForMenuKeys
- OBJC_IVAR_$_IMKClient_Modern._modeMenuKeys
- OBJC_IVAR_$_IMKClient_Modern._modes
- OBJC_IVAR_$_IMKClient_Modern._remoteProxyLock
- OBJC_IVAR_$_IMKClient_Modern._selectorDictionary
- OBJC_IVAR_$_IMKClient_Modern._serverConnection
- OBJC_IVAR_$_IMKClient_Modern._serverDOProxy
- OBJC_IVAR_$_IMKClient_Modern._serverDiedBadly
- OBJC_IVAR_$_IMKClient_Modern._serverName
- OBJC_IVAR_$_IMKClient_Modern._timeout
- OBJC_IVAR_$_IMKClient_Modern._tisSelectInputSourceCompletionBlock
- OBJC_IVAR_$_IMKClient_Modern._waitingForMenu
- OBJC_IVAR_$_IMKClient_Modern.completionBlock
- OBJC_IVAR_$_IMKClient_Modern.localizedStrings
- OBJC_IVAR_$_IMKInputSession.__allowRetryOnInvalidPortException
- OBJC_IVAR_$_IMKInputSession._activatePending
- OBJC_IVAR_$_IMKInputSession._deferredActivateHaveEventsQueued
- OBJC_IVAR_$_IMKInputSession._deferredActivateHaveInputSessionActionsQueued
- OBJC_IVAR_$_IMKInputSession._deferredActivateInputMode
- OBJC_IVAR_$_IMKInputSession._deferredActivatePending
- OBJC_IVAR_$_IMKInputSession._didActivate
- OBJC_IVAR_$_IMKInputSession._inputMethodXPCConnection
- OBJC_IVAR_$_IMKInputSession._queuedDeferredEvents
- OBJC_IVAR_$_IMKInputSession._queuedInputSessionActions
- OBJC_IVAR_$_IMKInputSession._touchBarViewController
- OBJC_IVAR_$_IMKInputSessionInvocationSentinel_Legacy._int
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._callerSelector
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._imkInputSession
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._innerRunLoopCount
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._invocationInterruptAttempted
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._otherInnerRunLoopDetected
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._replyObserver
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._replyTimer
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._request_reply_done
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._sentinel
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Legacy._timedOut
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Modern._callerSelector
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Modern._imkInputSession
- OBJC_IVAR_$_IMKInputSessionXPCInvocation_Modern._timeoutStatus
- OBJC_IVAR_$_IMKInputSession_Legacy._allowRetryOnInvalidPortException
- OBJC_IVAR_$_IMKInputSession_Legacy._charactersEntered
- OBJC_IVAR_$_IMKInputSession_Legacy._client
- OBJC_IVAR_$_IMKInputSession_Legacy._commiting
- OBJC_IVAR_$_IMKInputSession_Legacy._eventPending
- OBJC_IVAR_$_IMKInputSession_Legacy._eventStatus
- OBJC_IVAR_$_IMKInputSession_Legacy._markedRange
- OBJC_IVAR_$_IMKInputSession_Legacy._pendingEvents
- OBJC_IVAR_$_IMKInputSession_Legacy._sessionFinishedPreviously
- OBJC_IVAR_$_IMKInputSession_Legacy._supportedEvents
- OBJC_IVAR_$_IMKInputSession_Legacy._supportsDocumentAccess
- OBJC_IVAR_$_IMKInputSession_Legacy._tsmDocument
- OBJC_IVAR_$_IMKInputSession_Legacy.activatePending
- OBJC_IVAR_$_IMKInputSession_Legacy.deferredActivateHaveEventsQueued
- OBJC_IVAR_$_IMKInputSession_Legacy.deferredActivateHaveInputSessionActionsQueued
- OBJC_IVAR_$_IMKInputSession_Legacy.deferredActivateInputMode
- OBJC_IVAR_$_IMKInputSession_Legacy.deferredActivatePending
- OBJC_IVAR_$_IMKInputSession_Legacy.didActivate
- OBJC_IVAR_$_IMKInputSession_Legacy.inputMethodXPCConnection
- OBJC_IVAR_$_IMKInputSession_Legacy.placeholdersCachedWeakRef
- OBJC_IVAR_$_IMKInputSession_Legacy.queuedDeferredEvents
- OBJC_IVAR_$_IMKInputSession_Legacy.queuedInputSessionActions
- OBJC_IVAR_$_IMKInputSession_Legacy.touchBarViewController
- OBJC_IVAR_$_IMKInputSession_Modern._allowRetryOnInvalidPortException
- OBJC_IVAR_$_IMKInputSession_Modern._charactersEntered
- OBJC_IVAR_$_IMKInputSession_Modern._client
- OBJC_IVAR_$_IMKInputSession_Modern._commiting
- OBJC_IVAR_$_IMKInputSession_Modern._eventPending
- OBJC_IVAR_$_IMKInputSession_Modern._eventStatus
- OBJC_IVAR_$_IMKInputSession_Modern._markedRange
- OBJC_IVAR_$_IMKInputSession_Modern._pendingEvents
- OBJC_IVAR_$_IMKInputSession_Modern._sessionFinishedPreviously
- OBJC_IVAR_$_IMKInputSession_Modern._supportedEvents
- OBJC_IVAR_$_IMKInputSession_Modern._supportsDocumentAccess
- OBJC_IVAR_$_IMKInputSession_Modern._tsmDocument
- OBJC_IVAR_$_IMKInputSession_Modern.activatePending
- OBJC_IVAR_$_IMKInputSession_Modern.deferredActivateHaveEventsQueued
- OBJC_IVAR_$_IMKInputSession_Modern.deferredActivateHaveInputSessionActionsQueued
- OBJC_IVAR_$_IMKInputSession_Modern.deferredActivateInputMode
- OBJC_IVAR_$_IMKInputSession_Modern.deferredActivatePending
- OBJC_IVAR_$_IMKInputSession_Modern.didActivate
- OBJC_IVAR_$_IMKInputSession_Modern.inputMethodXPCConnection
- OBJC_IVAR_$_IMKInputSession_Modern.placeholdersCachedWeakRef
- OBJC_IVAR_$_IMKInputSession_Modern.queuedDeferredEvents
- OBJC_IVAR_$_IMKInputSession_Modern.queuedInputSessionActions
- OBJC_IVAR_$_IMKInputSession_Modern.touchBarViewController
- OBJC_IVAR_$_IMKQueuedEventRef_Legacy._eventRef
- OBJC_IVAR_$_IMKQueuedEventRef_Modern._eventRef
- OBJC_IVAR_$_IPMDFontRange_Legacy._font
- OBJC_IVAR_$_IPMDFontRange_Legacy._range
- OBJC_IVAR_$_IPMDFontRange_Modern._font
- OBJC_IVAR_$_IPMDFontRange_Modern._range
- _IMKInitializeNSRemoteView_Legacy
- _IMKInitializeNSRemoteView_Modern
- _IMServerDiedAbnormally_Legacy
- _IMServerDiedAbnormally_Modern
- _IsNSTextInputContextCompletionHandling_Legacy
- _IsNSTextInputContextCompletionHandling_Modern
- _OBJC_CLASS_$_HIRunLoopSemaphore
- _OBJC_CLASS_$_HIRunLoopUtilities
- _OBJC_CLASS_$_IMKClientInvocationSentinel_Legacy
- _OBJC_CLASS_$_IMKClientXPCInvocation_Legacy
- _OBJC_CLASS_$_IMKClientXPCInvocation_Modern
- _OBJC_CLASS_$_IMKClient_Legacy
- _OBJC_CLASS_$_IMKClient_Modern
- _OBJC_CLASS_$_IMKInputSessionInvocationSentinel_Legacy
- _OBJC_CLASS_$_IMKInputSessionXPCInvocation_Legacy
- _OBJC_CLASS_$_IMKInputSessionXPCInvocation_Modern
- _OBJC_CLASS_$_IMKInputSession_Legacy
- _OBJC_CLASS_$_IMKInputSession_Modern
- _OBJC_CLASS_$_IMKQueuedEventRef_Legacy
- _OBJC_CLASS_$_IMKQueuedEventRef_Modern
- _OBJC_CLASS_$_IPMDFontRange_Legacy
- _OBJC_CLASS_$_IPMDFontRange_Modern
- _OBJC_METACLASS_$_HIRunLoopSemaphore
- _OBJC_METACLASS_$_IMKClientInvocationSentinel_Legacy
- _OBJC_METACLASS_$_IMKClientXPCInvocation_Legacy
- _OBJC_METACLASS_$_IMKClientXPCInvocation_Modern
- _OBJC_METACLASS_$_IMKClient_Legacy
- _OBJC_METACLASS_$_IMKClient_Modern
- _OBJC_METACLASS_$_IMKInputSessionInvocationSentinel_Legacy
- _OBJC_METACLASS_$_IMKInputSessionXPCInvocation_Legacy
- _OBJC_METACLASS_$_IMKInputSessionXPCInvocation_Modern
- _OBJC_METACLASS_$_IMKInputSession_Legacy
- _OBJC_METACLASS_$_IMKInputSession_Modern
- _OBJC_METACLASS_$_IMKQueuedEventRef_Legacy
- _OBJC_METACLASS_$_IMKQueuedEventRef_Modern
- _OBJC_METACLASS_$_IPMDFontRange_Legacy
- _OBJC_METACLASS_$_IPMDFontRange_Modern
- __24-[IMKClient_Legacy menu]_block_invoke.131
- __24-[IMKClient_Modern menu]_block_invoke.109
- __34-[IMKInputSession_Legacy activate]_block_invoke.295
- __34-[IMKInputSession_Modern activate]_block_invoke.168
- __46-[IMKClient_Legacy menuWithCompletionHandler:]_block_invoke.182
- __46-[IMKClient_Legacy menuWithCompletionHandler:]_block_invoke.193
- __46-[IMKClient_Legacy menuWithCompletionHandler:]_block_invoke_2.186
- __46-[IMKClient_Legacy menuWithCompletionHandler:]_block_invoke_2.194
- __46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke.158
- __46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke.169
- __46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke_2.162
- __46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke_2.170
- __47-[IMKClient_Legacy modesWithCompletionHandler:]_block_invoke.233
- __47-[IMKClient_Legacy modesWithCompletionHandler:]_block_invoke_2.234
- __47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke.209
- __47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke_2.210
- __47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke_3.211
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke.814
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke.830
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2.818
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2.831
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke.661
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke.677
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2.665
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2.678
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.431
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.453
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.466
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.478
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.479
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.432
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.455
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.470
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3.447
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3.459
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4.449
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4.463
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke.623
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke.636
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2.627
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2.637
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.295
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.316
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.321
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.331
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.343
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.344
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.296
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.317
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.323
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.335
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.345
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_3.311
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_3.324
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_4.313
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_4.328
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke.482
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke.495
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2.486
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2.496
- __60+[IMKClient(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke.79
- __60+[IMKClient(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke.83
- __60+[IMKClient(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke_2.85
- __60-[IMKInputSession_Legacy stringFromRange:completionHandler:]_block_invoke.1483
- __60-[IMKInputSession_Modern stringFromRange:completionHandler:]_block_invoke.1334
- __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke.56
- __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke.64
- __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2.60
- __65-[IMKClient(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2.68
- __65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke.711
- __65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke_2.712
- __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke.563
- __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_2.564
- __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_3.565
- __67+[IMKClient_Legacy(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke.162
- __67+[IMKClient_Legacy(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke.166
- __67-[IMKClient(IMKClientConnection_XPC) _getServerXPCProxyForSession:]_block_invoke.364
- __72-[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke.137
- __72-[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke.145
- __72-[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2.141
- __72-[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2.149
- __74-[IMKClient_Legacy(IMKClientConnection_XPC) _getServerXPCProxyForSession:]_block_invoke.446
- __79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.848
- __79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.854
- __79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.697
- __79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.703
- __Block_byref_object_copy_.1190
- __Block_byref_object_copy_.1262
- __Block_byref_object_copy_.1339
- __Block_byref_object_copy_.1411
- __Block_byref_object_dispose_.1191
- __Block_byref_object_dispose_.1263
- __Block_byref_object_dispose_.1340
- __Block_byref_object_dispose_.1412
- __HIRLU_AddRunLoopModeForDeferredActions
- __IMKClientCopyMenuItems_Legacy
- __IMKClientCopyMenuItems_Modern
- __OBJC_$_CLASS_METHODS_IMKClient(IMKClientConnection_DO|IMKClient_XPCReplyWaitCount_Locking|IMKClientConnection_XPC)
- __OBJC_$_CLASS_METHODS_IMKClientInvocationSentinel_Legacy
- __OBJC_$_CLASS_METHODS_IMKClientXPCInvocation_Legacy
- __OBJC_$_CLASS_METHODS_IMKClientXPCInvocation_Modern
- __OBJC_$_CLASS_METHODS_IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking|IMKClient_Main_Thread_Tracking|IMKClientConnection_XPC)
- __OBJC_$_CLASS_METHODS_IMKClient_Modern(IMKClient_Main_Thread_Tracking)
- __OBJC_$_CLASS_METHODS_IMKInputSessionInvocationSentinel_Legacy
- __OBJC_$_CLASS_METHODS_IMKInputSessionXPCInvocation_Legacy
- __OBJC_$_CLASS_METHODS_IMKInputSessionXPCInvocation_Modern
- __OBJC_$_CLASS_METHODS_IMKInputSession_Legacy
- __OBJC_$_CLASS_METHODS_IMKInputSession_Modern
- __OBJC_$_CLASS_METHODS_IPMDFontRange_Legacy
- __OBJC_$_CLASS_METHODS_IPMDFontRange_Modern
- __OBJC_$_INSTANCE_METHODS_IMKClient(IMKClientConnection_DO|IMKClient_XPCReplyWaitCount_Locking|IMKClientConnection_XPC)
- __OBJC_$_INSTANCE_METHODS_IMKClientInvocationSentinel_Legacy
- __OBJC_$_INSTANCE_METHODS_IMKClientXPCInvocation_Legacy
- __OBJC_$_INSTANCE_METHODS_IMKClientXPCInvocation_Modern
- __OBJC_$_INSTANCE_METHODS_IMKClient_Legacy(IMKClient_XPCReplyWaitCount_Locking|IMKClient_Main_Thread_Tracking|IMKClientConnection_XPC)
- __OBJC_$_INSTANCE_METHODS_IMKClient_Modern
- __OBJC_$_INSTANCE_METHODS_IMKInputSessionInvocationSentinel_Legacy
- __OBJC_$_INSTANCE_METHODS_IMKInputSessionXPCInvocation_Legacy
- __OBJC_$_INSTANCE_METHODS_IMKInputSessionXPCInvocation_Modern
- __OBJC_$_INSTANCE_METHODS_IMKInputSession_Legacy
- __OBJC_$_INSTANCE_METHODS_IMKInputSession_Modern
- __OBJC_$_INSTANCE_METHODS_IMKQueuedEventRef_Legacy
- __OBJC_$_INSTANCE_METHODS_IMKQueuedEventRef_Modern
- __OBJC_$_INSTANCE_METHODS_IPMDFontRange_Legacy
- __OBJC_$_INSTANCE_METHODS_IPMDFontRange_Modern
- __OBJC_$_INSTANCE_VARIABLES_IMKClientInvocationSentinel_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKClientXPCInvocation_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKClientXPCInvocation_Modern
- __OBJC_$_INSTANCE_VARIABLES_IMKClient_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKClient_Modern
- __OBJC_$_INSTANCE_VARIABLES_IMKInputSessionInvocationSentinel_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKInputSessionXPCInvocation_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKInputSessionXPCInvocation_Modern
- __OBJC_$_INSTANCE_VARIABLES_IMKInputSession_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKInputSession_Modern
- __OBJC_$_INSTANCE_VARIABLES_IMKQueuedEventRef_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IMKQueuedEventRef_Modern
- __OBJC_$_INSTANCE_VARIABLES_IPMDFontRange_Legacy
- __OBJC_$_INSTANCE_VARIABLES_IPMDFontRange_Modern
- __OBJC_$_PROP_LIST_IMKClient_Legacy
- __OBJC_$_PROP_LIST_IMKClient_Modern
- __OBJC_$_PROP_LIST_IMKInputSession_Legacy
- __OBJC_$_PROP_LIST_IMKInputSession_Modern
- __OBJC_CLASS_PROTOCOLS_$_IMKClient_Legacy
- __OBJC_CLASS_PROTOCOLS_$_IMKClient_Modern
- __OBJC_CLASS_PROTOCOLS_$_IMKInputSession_Legacy
- __OBJC_CLASS_PROTOCOLS_$_IMKInputSession_Modern
- __OBJC_CLASS_RO_$_IMKClientInvocationSentinel_Legacy
- __OBJC_CLASS_RO_$_IMKClientXPCInvocation_Legacy
- __OBJC_CLASS_RO_$_IMKClientXPCInvocation_Modern
- __OBJC_CLASS_RO_$_IMKClient_Legacy
- __OBJC_CLASS_RO_$_IMKClient_Modern
- __OBJC_CLASS_RO_$_IMKInputSessionInvocationSentinel_Legacy
- __OBJC_CLASS_RO_$_IMKInputSessionXPCInvocation_Legacy
- __OBJC_CLASS_RO_$_IMKInputSessionXPCInvocation_Modern
- __OBJC_CLASS_RO_$_IMKInputSession_Legacy
- __OBJC_CLASS_RO_$_IMKInputSession_Modern
- __OBJC_CLASS_RO_$_IMKQueuedEventRef_Legacy
- __OBJC_CLASS_RO_$_IMKQueuedEventRef_Modern
- __OBJC_CLASS_RO_$_IPMDFontRange_Legacy
- __OBJC_CLASS_RO_$_IPMDFontRange_Modern
- __OBJC_METACLASS_RO_$_IMKClientInvocationSentinel_Legacy
- __OBJC_METACLASS_RO_$_IMKClientXPCInvocation_Legacy
- __OBJC_METACLASS_RO_$_IMKClientXPCInvocation_Modern
- __OBJC_METACLASS_RO_$_IMKClient_Legacy
- __OBJC_METACLASS_RO_$_IMKClient_Modern
- __OBJC_METACLASS_RO_$_IMKInputSessionInvocationSentinel_Legacy
- __OBJC_METACLASS_RO_$_IMKInputSessionXPCInvocation_Legacy
- __OBJC_METACLASS_RO_$_IMKInputSessionXPCInvocation_Modern
- __OBJC_METACLASS_RO_$_IMKInputSession_Legacy
- __OBJC_METACLASS_RO_$_IMKInputSession_Modern
- __OBJC_METACLASS_RO_$_IMKQueuedEventRef_Legacy
- __OBJC_METACLASS_RO_$_IMKQueuedEventRef_Modern
- __OBJC_METACLASS_RO_$_IPMDFontRange_Legacy
- __OBJC_METACLASS_RO_$_IPMDFontRange_Modern
- __Z34IMKCopyExtensionBundlePaths_Legacyv
- __Z34IMKCopyExtensionBundlePaths_Modernv
- __ZL16_swapYCoordinatel
- __ZL19_generalDebuggingOn
- __ZL19_menuCommandHandlerP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv
- __ZZ21+[IMKClient subclass]E4once
- __ZZ21+[IMKClient subclass]E6result
- __ZZ27+[IMKClient allocWithZone:]E10allocating
- __ZZ27+[IMKInputSession subclass]E4once
- __ZZ27+[IMKInputSession subclass]E6result
- __ZZ33+[IMKInputSession allocWithZone:]E10allocating
- __ZZ35-[IMKClient_Legacy _defaultTimeout]E16sDefaultsChecked
- __ZZ35-[IMKClient_Modern _defaultTimeout]E16sDefaultsChecked
- __ZZ43+[IMKInputSession_Legacy IMKCFRunLoopSetup]E9onceToken
- __ZZ43+[IMKInputSession_Modern IMKCFRunLoopSetup]E9onceToken
- __ZZ54-[IMKInputSession_Legacy validAttributesForMarkedText]E8theArray
- __ZZ54-[IMKInputSession_Modern validAttributesForMarkedText]E8theArray
- __ZZ60-[IMKClient_Legacy initWithBundleIdentifier:isIMKExtension:]E16sDefaultsChecked
- __ZZ60-[IMKClient_Modern initWithBundleIdentifier:isIMKExtension:]E16sDefaultsChecked
- __ZZ63+[IMKClient_Legacy(IMKClientConnection_XPC) privateRunLoopMode]E11runLoopMode
- __ZZ63+[IMKClient_Legacy(IMKClientConnection_XPC) privateRunLoopMode]E4once
- __ZZ69+[IMKClient_Legacy(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]E4once
- __ZZL22IMKClientRunLoopModernvE4once
- __ZZL22IMKClientRunLoopModernvE6result
- ___101-[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:validFlags:completionHandler:]_block_invoke
- ___101-[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:validFlags:completionHandler:]_block_invoke
- ___107-[IMKInputSession_Legacy tryHandleEvent_commitOnMouseDown_withDispatchCondition:dispatchWork:continuation:]_block_invoke
- ___107-[IMKInputSession_Modern tryHandleEvent_commitOnMouseDown_withDispatchCondition:dispatchWork:continuation:]_block_invoke
- ___152-[IMKInputSession_Legacy do_coreAttributesFromRange_postEventLoopWithContext:initBlockEach:postEventCompletionEach:whileConditionBlock:finalCompletion:]_block_invoke
- ___152-[IMKInputSession_Modern do_coreAttributesFromRange_postEventLoopWithContext:initBlockEach:postEventCompletionEach:whileConditionBlock:finalCompletion:]_block_invoke
- ___154-[IMKInputSession_Legacy tryCoreAttributesFromRange_CheckForSurrogateCharacter_CopyUniCharsForRangeAdjusted_wTest:context:initialBlock:continuationBlock:]_block_invoke
- ___154-[IMKInputSession_Modern tryCoreAttributesFromRange_CheckForSurrogateCharacter_CopyUniCharsForRangeAdjusted_wTest:context:initialBlock:continuationBlock:]_block_invoke
- ___166-[IMKInputSession_Legacy tryHandleEvent_GetOffsetAndLocationForMouseEvent__withDispatchCondition:initialization:dispatchWork:postEventCompletion:continuationHandler:]_block_invoke
- ___166-[IMKInputSession_Modern tryHandleEvent_GetOffsetAndLocationForMouseEvent__withDispatchCondition:initialization:dispatchWork:postEventCompletion:continuationHandler:]_block_invoke
- ___184-[IMKInputSession_Legacy tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]_block_invoke
- ___184-[IMKInputSession_Legacy tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]_block_invoke_2
- ___184-[IMKInputSession_Modern tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]_block_invoke
- ___184-[IMKInputSession_Modern tryCoreAttributesFromRange_CheckForSurrogateCharacter_GetDocLength_CopyUniCharsForRangeAdjusted_wTest:context:nextDispatchTest:initialBlock:continuationBlock:]_block_invoke_2
- ___21+[IMKClient subclass]_block_invoke
- ___24-[IMKClient_Legacy menu]_block_invoke
- ___24-[IMKClient_Modern menu]_block_invoke
- ___24-[IMKClient_Modern menu]_block_invoke_2
- ___25-[IMKClient_Legacy modes]_block_invoke
- ___25-[IMKClient_Legacy modes]_block_invoke_2
- ___25-[IMKClient_Modern modes]_block_invoke
- ___25-[IMKClient_Modern modes]_block_invoke_2
- ___25-[IMKClient_Modern modes]_block_invoke_3
- ___27+[IMKInputSession subclass]_block_invoke
- ___32-[IMKInputSession_Legacy length]_block_invoke
- ___32-[IMKInputSession_Modern length]_block_invoke
- ___34-[IMKInputSession_Legacy activate]_block_invoke
- ___34-[IMKInputSession_Modern activate]_block_invoke
- ___34-[IMKInputSession_Modern activate]_block_invoke_2
- ___36-[IMKInputSession_Legacy deactivate]_block_invoke
- ___36-[IMKInputSession_Legacy deactivate]_block_invoke_2
- ___36-[IMKInputSession_Modern deactivate]_block_invoke
- ___36-[IMKInputSession_Modern deactivate]_block_invoke_2
- ___36-[IMKInputSession_Modern deactivate]_block_invoke_3
- ___37-[IMKInputSession_Legacy insertText:]_block_invoke
- ___37-[IMKInputSession_Modern insertText:]_block_invoke
- ___39-[IMKInputSession_Legacy selectedRange]_block_invoke
- ___39-[IMKInputSession_Modern selectedRange]_block_invoke
- ___42-[IMKInputSession_Legacy setValue:forTag:]_block_invoke
- ___42-[IMKInputSession_Legacy setValue:forTag:]_block_invoke_2
- ___42-[IMKInputSession_Modern setValue:forTag:]_block_invoke
- ___42-[IMKInputSession_Modern setValue:forTag:]_block_invoke_2
- ___42-[IMKInputSession_Modern setValue:forTag:]_block_invoke_3
- ___43+[IMKInputSession_Legacy IMKCFRunLoopSetup]_block_invoke
- ___43+[IMKInputSession_Modern IMKCFRunLoopSetup]_block_invoke
- ___43-[IMKInputSession_Legacy commitComposition]_block_invoke
- ___43-[IMKInputSession_Legacy commitComposition]_block_invoke_2
- ___43-[IMKInputSession_Modern commitComposition]_block_invoke
- ___43-[IMKInputSession_Modern commitComposition]_block_invoke_2
- ___43-[IMKInputSession_Modern commitComposition]_block_invoke_3
- ___44-[IMKInputSession_Legacy unmarkTextInClient]_block_invoke
- ___44-[IMKInputSession_Modern unmarkTextInClient]_block_invoke
- ___46-[IMKClient_Legacy invalidateServerConnection]_block_invoke
- ___46-[IMKClient_Legacy menuWithCompletionHandler:]_block_invoke
- ___46-[IMKClient_Legacy menuWithCompletionHandler:]_block_invoke_2
- ___46-[IMKClient_Modern invalidateServerConnection]_block_invoke
- ___46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke
- ___46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke_2
- ___46-[IMKClient_Modern menuWithCompletionHandler:]_block_invoke_3
- ___47-[IMKClient_Legacy modesWithCompletionHandler:]_block_invoke
- ___47-[IMKClient_Legacy modesWithCompletionHandler:]_block_invoke_2
- ___47-[IMKClient_Legacy modesWithCompletionHandler:]_block_invoke_3
- ___47-[IMKClient_Legacy modesWithCompletionHandler:]_block_invoke_4
- ___47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke
- ___47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke_2
- ___47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke_3
- ___47-[IMKClient_Modern modesWithCompletionHandler:]_block_invoke_4
- ___49-[IMKInputSession_Legacy imkxpc_lengthWithReply:]_block_invoke
- ___49-[IMKInputSession_Legacy imkxpc_lengthWithReply:]_block_invoke_2
- ___49-[IMKInputSession_Modern imkxpc_lengthWithReply:]_block_invoke
- ___49-[IMKInputSession_Modern imkxpc_lengthWithReply:]_block_invoke_2
- ___50-[IMKInputSession_Legacy imkxpc_insertText:reply:]_block_invoke
- ___50-[IMKInputSession_Legacy imkxpc_insertText:reply:]_block_invoke_2
- ___50-[IMKInputSession_Modern imkxpc_insertText:reply:]_block_invoke
- ___50-[IMKInputSession_Modern imkxpc_insertText:reply:]_block_invoke_2
- ___54-[IMKInputSession_Legacy attributesForCharacterIndex:]_block_invoke
- ___54-[IMKInputSession_Legacy imkxpc_windowLevelWithReply:]_block_invoke
- ___54-[IMKInputSession_Legacy insertText:replacementRange:]_block_invoke
- ___54-[IMKInputSession_Legacy stringFromRange:actualRange:]_block_invoke
- ___54-[IMKInputSession_Modern attributesForCharacterIndex:]_block_invoke
- ___54-[IMKInputSession_Modern imkxpc_windowLevelWithReply:]_block_invoke
- ___54-[IMKInputSession_Modern insertText:replacementRange:]_block_invoke
- ___54-[IMKInputSession_Modern stringFromRange:actualRange:]_block_invoke
- ___55-[IMKClient_Legacy _modeMenuKeysWithCompletionHandler:]_block_invoke
- ___55-[IMKClient_Modern _modeMenuKeysWithCompletionHandler:]_block_invoke
- ___55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke
- ___55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2
- ___55-[IMKInputSession_Legacy _postEvent:completionHandler:]_block_invoke
- ___55-[IMKInputSession_Legacy activateAfterServerConnection]_block_invoke
- ___55-[IMKInputSession_Legacy activateAfterServerConnection]_block_invoke_2
- ___55-[IMKInputSession_Legacy attributedSubstringFromRange:]_block_invoke
- ___55-[IMKInputSession_Legacy imkxpc_deadKeyStateWithReply:]_block_invoke
- ___55-[IMKInputSession_Legacy imkxpc_selectInputMode:reply:]_block_invoke
- ___55-[IMKInputSession_Legacy imkxpc_stringFromRange:reply:]_block_invoke
- ___55-[IMKInputSession_Legacy imkxpc_stringFromRange:reply:]_block_invoke_2
- ___55-[IMKInputSession_Legacy imkxpc_updateMenusDictionary:]_block_invoke
- ___55-[IMKInputSession_Legacy insertText:completionHandler:]_block_invoke
- ___55-[IMKInputSession_Legacy length_withCompletionHandler:]_block_invoke
- ___55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke
- ___55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2
- ___55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_3
- ___55-[IMKInputSession_Modern _postEvent:completionHandler:]_block_invoke
- ___55-[IMKInputSession_Modern activateAfterServerConnection]_block_invoke
- ___55-[IMKInputSession_Modern activateAfterServerConnection]_block_invoke_2
- ___55-[IMKInputSession_Modern attributedSubstringFromRange:]_block_invoke
- ___55-[IMKInputSession_Modern imkxpc_deadKeyStateWithReply:]_block_invoke
- ___55-[IMKInputSession_Modern imkxpc_selectInputMode:reply:]_block_invoke
- ___55-[IMKInputSession_Modern imkxpc_stringFromRange:reply:]_block_invoke
- ___55-[IMKInputSession_Modern imkxpc_stringFromRange:reply:]_block_invoke_2
- ___55-[IMKInputSession_Modern imkxpc_updateMenusDictionary:]_block_invoke
- ___55-[IMKInputSession_Modern insertText:completionHandler:]_block_invoke
- ___55-[IMKInputSession_Modern length_withCompletionHandler:]_block_invoke
- ___56-[IMKClientXPCInvocation_Legacy invocationAwaitXPCReply]_block_invoke
- ___56-[IMKClient_Legacy switchedInputMode:completionHandler:]_block_invoke
- ___56-[IMKClient_Modern switchedInputMode:completionHandler:]_block_invoke
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_5
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_6
- ___56-[IMKInputSession_Legacy imkxpc_selectedRangeWithReply:]_block_invoke
- ___56-[IMKInputSession_Legacy imkxpc_selectedRangeWithReply:]_block_invoke_2
- ___56-[IMKInputSession_Legacy imkxpc_supportsProperty:reply:]_block_invoke
- ___56-[IMKInputSession_Legacy imkxpc_terminatePalette:reply:]_block_invoke
- ___56-[IMKInputSession_Legacy imkxpc_wouldHandleEvent:reply:]_block_invoke
- ___56-[IMKInputSession_Legacy imkxpc_wouldHandleEvent:reply:]_block_invoke_2
- ___56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke
- ___56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2
- ___56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke
- ___56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2
- ___56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_3
- ___56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_4
- ___56-[IMKInputSession_Modern imkxpc_selectedRangeWithReply:]_block_invoke
- ___56-[IMKInputSession_Modern imkxpc_selectedRangeWithReply:]_block_invoke_2
- ___56-[IMKInputSession_Modern imkxpc_supportsProperty:reply:]_block_invoke
- ___56-[IMKInputSession_Modern imkxpc_terminatePalette:reply:]_block_invoke
- ___56-[IMKInputSession_Modern imkxpc_wouldHandleEvent:reply:]_block_invoke
- ___56-[IMKInputSession_Modern imkxpc_wouldHandleEvent:reply:]_block_invoke_2
- ___56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke
- ___56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2
- ___56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_3
- ___57-[IMKInputSessionXPCInvocation_Legacy configureObservers]_block_invoke
- ___58-[IMKInputSession_Legacy imkxpc_supportsUnicodeWithReply:]_block_invoke
- ___58-[IMKInputSession_Modern imkxpc_supportsUnicodeWithReply:]_block_invoke
- ___59-[IMKInputSession_Legacy imkxpc_bundleIdentifierWithReply:]_block_invoke
- ___59-[IMKInputSession_Legacy imkxpc_isPaletteTerminated:reply:]_block_invoke
- ___59-[IMKInputSession_Legacy imkxpc_markedRangeValueWithReply:]_block_invoke
- ___59-[IMKInputSession_Modern imkxpc_bundleIdentifierWithReply:]_block_invoke
- ___59-[IMKInputSession_Modern imkxpc_isPaletteTerminated:reply:]_block_invoke
- ___59-[IMKInputSession_Modern imkxpc_markedRangeValueWithReply:]_block_invoke
- ___60-[IMKClientXPCInvocation_Legacy invocationInterruptXPCReply]_block_invoke
- ___60-[IMKInputSession_Legacy stringFromRange:completionHandler:]_block_invoke
- ___60-[IMKInputSession_Modern stringFromRange:completionHandler:]_block_invoke
- ___61-[IMKInputSessionXPCInvocation_Legacy addReplyTimerToRunloop]_block_invoke
- ___61-[IMKInputSession_Legacy wouldHandleEvent:completionHandler:]_block_invoke
- ___61-[IMKInputSession_Modern wouldHandleEvent:completionHandler:]_block_invoke
- ___62-[IMKInputSessionXPCInvocation_Modern invocationAwaitXPCReply]_block_invoke
- ___62-[IMKInputSession_Legacy imkxpc_getApplicationProperty:reply:]_block_invoke
- ___62-[IMKInputSession_Legacy selectedRange_withCompletionHandler:]_block_invoke
- ___62-[IMKInputSession_Modern imkxpc_getApplicationProperty:reply:]_block_invoke
- ___62-[IMKInputSession_Modern selectedRange_withCompletionHandler:]_block_invoke
- ___63+[IMKClient_Legacy(IMKClientConnection_XPC) privateRunLoopMode]_block_invoke
- ___63-[IMKInputSession_Legacy _commitOnMouseDown:completionHandler:]_block_invoke
- ___63-[IMKInputSession_Modern _commitOnMouseDown:completionHandler:]_block_invoke
- ___64-[IMKInputSession_Legacy doCommandBySelector:commandDictionary:]_block_invoke
- ___64-[IMKInputSession_Legacy doCommandBySelector:commandDictionary:]_block_invoke_2
- ___64-[IMKInputSession_Legacy imkxpc_inputSessionDoneSleepWithReply:]_block_invoke
- ___64-[IMKInputSession_Modern doCommandBySelector:commandDictionary:]_block_invoke
- ___64-[IMKInputSession_Modern doCommandBySelector:commandDictionary:]_block_invoke_2
- ___64-[IMKInputSession_Modern doCommandBySelector:commandDictionary:]_block_invoke_3
- ___64-[IMKInputSession_Modern imkxpc_inputSessionDoneSleepWithReply:]_block_invoke
- ___65-[IMKInputSession_Legacy _showHideInputWindow:completionHandler:]_block_invoke
- ___65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke
- ___65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke_2
- ___65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke_3
- ___65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke_4
- ___65-[IMKInputSession_Legacy firstRectForCharacterRange:actualRange:]_block_invoke
- ___65-[IMKInputSession_Legacy insertText:replacementRange:validFlags:]_block_invoke
- ___65-[IMKInputSession_Modern _showHideInputWindow:completionHandler:]_block_invoke
- ___65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke
- ___65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_2
- ___65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_3
- ___65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_4
- ___65-[IMKInputSession_Modern firstRectForCharacterRange:actualRange:]_block_invoke
- ___65-[IMKInputSession_Modern insertText:replacementRange:validFlags:]_block_invoke
- ___66-[IMKInputSessionXPCInvocation_Legacy invocationInterruptXPCReply]_block_invoke
- ___66-[IMKInputSession_Legacy imkxpc_firstRectForCharacterRange:reply:]_block_invoke
- ___66-[IMKInputSession_Legacy imkxpc_firstRectForCharacterRange:reply:]_block_invoke_2
- ___66-[IMKInputSession_Legacy imkxpc_viewEffectiveAppearanceWithReply:]_block_invoke
- ___66-[IMKInputSession_Modern imkxpc_firstRectForCharacterRange:reply:]_block_invoke
- ___66-[IMKInputSession_Modern imkxpc_firstRectForCharacterRange:reply:]_block_invoke_2
- ___66-[IMKInputSession_Modern imkxpc_viewEffectiveAppearanceWithReply:]_block_invoke
- ___67+[IMKClient_Legacy(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke
- ___67+[IMKClient_Legacy(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke_2
- ___67-[IMKInputSession_Legacy _closeInputPalette_withCompletionHandler:]_block_invoke
- ___67-[IMKInputSession_Legacy imkxpc_attributesForCharacterIndex:reply:]_block_invoke
- ___67-[IMKInputSession_Legacy imkxpc_attributesForCharacterIndex:reply:]_block_invoke_2
- ___67-[IMKInputSession_Legacy imkxpc_isBottomLineInputContextWithReply:]_block_invoke
- ___67-[IMKInputSession_Legacy imkxpc_isGrammarCheckingEnabledWithReply:]_block_invoke
- ___67-[IMKInputSession_Modern _closeInputPalette_withCompletionHandler:]_block_invoke
- ___67-[IMKInputSession_Modern imkxpc_attributesForCharacterIndex:reply:]_block_invoke
- ___67-[IMKInputSession_Modern imkxpc_attributesForCharacterIndex:reply:]_block_invoke_2
- ___67-[IMKInputSession_Modern imkxpc_isBottomLineInputContextWithReply:]_block_invoke
- ___67-[IMKInputSession_Modern imkxpc_isGrammarCheckingEnabledWithReply:]_block_invoke
- ___68-[IMKInputSession_Legacy imkxpc_attributedSubstringFromRange:reply:]_block_invoke
- ___68-[IMKInputSession_Legacy imkxpc_attributedSubstringFromRange:reply:]_block_invoke_2
- ___68-[IMKInputSession_Legacy imkxpc_setApplicationProperty:value:reply:]_block_invoke
- ___68-[IMKInputSession_Legacy imkxpc_windowEffectiveAppearanceWithReply:]_block_invoke
- ___68-[IMKInputSession_Modern imkxpc_attributedSubstringFromRange:reply:]_block_invoke
- ___68-[IMKInputSession_Modern imkxpc_attributedSubstringFromRange:reply:]_block_invoke_2
- ___68-[IMKInputSession_Modern imkxpc_setApplicationProperty:value:reply:]_block_invoke
- ___68-[IMKInputSession_Modern imkxpc_windowEffectiveAppearanceWithReply:]_block_invoke
- ___69+[IMKClient_Legacy(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain]_block_invoke
- ___69-[IMKInputSession_Legacy imkxpc_commitPendingInlineSessionWithReply:]_block_invoke
- ___69-[IMKInputSession_Legacy imkxpc_currentInputSourceBundleIDWithReply:]_block_invoke
- ___69-[IMKInputSession_Legacy imkxpc_isSmartInsertDeleteEnabledWithReply:]_block_invoke
- ___69-[IMKInputSession_Modern imkxpc_commitPendingInlineSessionWithReply:]_block_invoke
- ___69-[IMKInputSession_Modern imkxpc_currentInputSourceBundleIDWithReply:]_block_invoke
- ___69-[IMKInputSession_Modern imkxpc_isSmartInsertDeleteEnabledWithReply:]_block_invoke
- ___70-[IMKInputSessionXPCInvocation_Legacy configureReplyTimerWithTimeout:]_block_invoke
- ___70-[IMKInputSession_Legacy imkxpc_supportsChromaticMarkedTextWithReply:]_block_invoke
- ___70-[IMKInputSession_Legacy imkxpc_viewEffectiveAppearanceNameWithReply:]_block_invoke
- ___70-[IMKInputSession_Modern imkxpc_supportsChromaticMarkedTextWithReply:]_block_invoke
- ___70-[IMKInputSession_Modern imkxpc_viewEffectiveAppearanceNameWithReply:]_block_invoke
- ___71-[IMKInputSession_Legacy firstRectForCharacterRange:completionHandler:]_block_invoke
- ___71-[IMKInputSession_Legacy imkxpc_characterIndexForPoint:tracking:reply:]_block_invoke
- ___71-[IMKInputSession_Legacy imkxpc_characterIndexForPoint:tracking:reply:]_block_invoke_2
- ___71-[IMKInputSession_Legacy imkxpc_hidePalettesAtInsertionPointWithReply:]_block_invoke
- ___71-[IMKInputSession_Legacy imkxpc_uniqueClientIdentifierStringWithReply:]_block_invoke
- ___71-[IMKInputSession_Legacy imkxpc_validAttributesForMarkedTextWithReply:]_block_invoke
- ___71-[IMKInputSession_Modern firstRectForCharacterRange:completionHandler:]_block_invoke
- ___71-[IMKInputSession_Modern imkxpc_characterIndexForPoint:tracking:reply:]_block_invoke
- ___71-[IMKInputSession_Modern imkxpc_characterIndexForPoint:tracking:reply:]_block_invoke_2
- ___71-[IMKInputSession_Modern imkxpc_hidePalettesAtInsertionPointWithReply:]_block_invoke
- ___71-[IMKInputSession_Modern imkxpc_uniqueClientIdentifierStringWithReply:]_block_invoke
- ___71-[IMKInputSession_Modern imkxpc_validAttributesForMarkedTextWithReply:]_block_invoke
- ___72-[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke
- ___72-[IMKClient_Legacy(IMKClientConnection_XPC) startServerSetupForEndpoint]_block_invoke_2
- ___72-[IMKInputSession_Legacy attributesForCharacterIndex:completionHandler:]_block_invoke
- ___72-[IMKInputSession_Legacy characterIndexForPoint:tracking:inMarkedRange:]_block_invoke
- ___72-[IMKInputSession_Legacy fetchViewServiceEndpointWithCompletionHandler:]_block_invoke
- ___72-[IMKInputSession_Legacy fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_2
- ___72-[IMKInputSession_Legacy fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_3
- ___72-[IMKInputSession_Legacy fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_4
- ___72-[IMKInputSession_Legacy imkxpc_windowEffectiveAppearanceNameWithReply:]_block_invoke
- ___72-[IMKInputSession_Legacy insertText:replacementRange:completionHandler:]_block_invoke
- ___72-[IMKInputSession_Legacy insertText:replacementRange:completionHandler:]_block_invoke_2
- ___72-[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:]_block_invoke
- ___72-[IMKInputSession_Modern attributesForCharacterIndex:completionHandler:]_block_invoke
- ___72-[IMKInputSession_Modern characterIndexForPoint:tracking:inMarkedRange:]_block_invoke
- ___72-[IMKInputSession_Modern fetchViewServiceEndpointWithCompletionHandler:]_block_invoke
- ___72-[IMKInputSession_Modern fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_2
- ___72-[IMKInputSession_Modern fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_3
- ___72-[IMKInputSession_Modern fetchViewServiceEndpointWithCompletionHandler:]_block_invoke_4
- ___72-[IMKInputSession_Modern imkxpc_windowEffectiveAppearanceNameWithReply:]_block_invoke
- ___72-[IMKInputSession_Modern insertText:replacementRange:completionHandler:]_block_invoke
- ___72-[IMKInputSession_Modern insertText:replacementRange:completionHandler:]_block_invoke_2
- ___72-[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:]_block_invoke
- ___73-[IMKClient_Legacy _mapKeyCodeToInputSource:modifiers:completionHandler:]_block_invoke
- ___73-[IMKClient_Modern _mapKeyCodeToInputSource:modifiers:completionHandler:]_block_invoke
- ___73-[IMKInputSession_Legacy attributedSubstringFromRange:completionHandler:]_block_invoke
- ___73-[IMKInputSession_Legacy attributedSubstringFromRange:completionHandler:]_block_invoke_2
- ___73-[IMKInputSession_Legacy imkxpc_overrideKeyboardWithKeyboardNamed:reply:]_block_invoke
- ___73-[IMKInputSession_Modern attributedSubstringFromRange:completionHandler:]_block_invoke
- ___73-[IMKInputSession_Modern attributedSubstringFromRange:completionHandler:]_block_invoke_2
- ___73-[IMKInputSession_Modern imkxpc_overrideKeyboardWithKeyboardNamed:reply:]_block_invoke
- ___74-[IMKClient_Legacy(IMKClientConnection_XPC) _getServerXPCProxyForSession:]_block_invoke
- ___74-[IMKClient_Legacy(IMKClientConnection_XPC) _getServerXPCProxyForSession:]_block_invoke_2
- ___74-[IMKInputSession_Legacy attributesForCharacterIndex:lineHeightRectangle:]_block_invoke
- ___74-[IMKInputSession_Legacy imkxpc_incrementalSearchClientGeometryWithReply:]_block_invoke
- ___74-[IMKInputSession_Legacy imkxpc_isIncrementalSearchInputContextWithReply:]_block_invoke
- ___74-[IMKInputSession_Legacy imkxpc_supportsTextAttachmentInsertionWithReply:]_block_invoke
- ___74-[IMKInputSession_Modern attributesForCharacterIndex:lineHeightRectangle:]_block_invoke
- ___74-[IMKInputSession_Modern imkxpc_incrementalSearchClientGeometryWithReply:]_block_invoke
- ___74-[IMKInputSession_Modern imkxpc_isIncrementalSearchInputContextWithReply:]_block_invoke
- ___74-[IMKInputSession_Modern imkxpc_supportsTextAttachmentInsertionWithReply:]_block_invoke
- ___75-[IMKClient_Legacy(IMKClientConnection_XPC) _receiveXPCConnectionEndpoint:]_block_invoke
- ___75-[IMKInputSession_Legacy imkxpc_isAutomaticCapitalizationEnabledWithReply:]_block_invoke
- ___75-[IMKInputSession_Legacy imkxpc_isAutomaticTextCompletionEnabledWithReply:]_block_invoke
- ___75-[IMKInputSession_Legacy imkxpc_isContinuousSpellCheckingEnabledWithReply:]_block_invoke
- ___75-[IMKInputSession_Modern imkxpc_isAutomaticCapitalizationEnabledWithReply:]_block_invoke
- ___75-[IMKInputSession_Modern imkxpc_isAutomaticTextCompletionEnabledWithReply:]_block_invoke
- ___75-[IMKInputSession_Modern imkxpc_isContinuousSpellCheckingEnabledWithReply:]_block_invoke
- ___76-[IMKInputSession_Legacy characterIndexForPoint:tracking:completionHandler:]_block_invoke
- ___76-[IMKInputSession_Legacy imkxpc_isAutomaticTextReplacementEnabledWithReply:]_block_invoke
- ___76-[IMKInputSession_Modern characterIndexForPoint:tracking:completionHandler:]_block_invoke
- ___76-[IMKInputSession_Modern imkxpc_isAutomaticTextReplacementEnabledWithReply:]_block_invoke
- ___77-[IMKInputSession_Legacy _createAndSendOffsetToPointEvent:completionHandler:]_block_invoke
- ___77-[IMKInputSession_Legacy imkxpc_isAutomaticDashSubstitutionEnabledWithReply:]_block_invoke
- ___77-[IMKInputSession_Legacy imkxpc_isTextPlaceholderAwareInputContextWithReply:]_block_invoke
- ___77-[IMKInputSession_Modern _createAndSendOffsetToPointEvent:completionHandler:]_block_invoke
- ___77-[IMKInputSession_Modern imkxpc_isAutomaticDashSubstitutionEnabledWithReply:]_block_invoke
- ___77-[IMKInputSession_Modern imkxpc_isTextPlaceholderAwareInputContextWithReply:]_block_invoke
- ___78-[IMKClientXPCInvocation_Modern invocationAwaitXPCReplyFromProcessIdentifier:]_block_invoke
- ___78-[IMKInputSession_Legacy imkxpc_dismissFunctionRowItemTextInputViewWithReply:]_block_invoke
- ___78-[IMKInputSession_Legacy imkxpc_insertText:replacementRange:validFlags:reply:]_block_invoke
- ___78-[IMKInputSession_Legacy imkxpc_insertText:replacementRange:validFlags:reply:]_block_invoke_2
- ___78-[IMKInputSession_Legacy imkxpc_isAutomaticQuoteSubstitutionEnabledWithReply:]_block_invoke
- ___78-[IMKInputSession_Modern imkxpc_dismissFunctionRowItemTextInputViewWithReply:]_block_invoke
- ___78-[IMKInputSession_Modern imkxpc_insertText:replacementRange:validFlags:reply:]_block_invoke
- ___78-[IMKInputSession_Modern imkxpc_insertText:replacementRange:validFlags:reply:]_block_invoke_2
- ___78-[IMKInputSession_Modern imkxpc_isAutomaticQuoteSubstitutionEnabledWithReply:]_block_invoke
- ___79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke
- ___79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke_2
- ___79-[IMKInputSession_Legacy imkxpc_isAutomaticPeriodSubstitutionEnabledWithReply:]_block_invoke
- ___79-[IMKInputSession_Legacy imkxpc_isAutomaticSpellingCorrectionEnabledWithReply:]_block_invoke
- ___79-[IMKInputSession_Legacy imkxpc_isDictationHiliteCapableInputContextWithReply:]_block_invoke
- ___79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke
- ___79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke_2
- ___79-[IMKInputSession_Modern imkxpc_isAutomaticPeriodSubstitutionEnabledWithReply:]_block_invoke
- ___79-[IMKInputSession_Modern imkxpc_isAutomaticSpellingCorrectionEnabledWithReply:]_block_invoke
- ___79-[IMKInputSession_Modern imkxpc_isDictationHiliteCapableInputContextWithReply:]_block_invoke
- ___81-[IMKClient_Legacy(IMKClientConnection_XPC) remoteXPCProxyForSession:fromCaller:]_block_invoke
- ___83-[IMKClient_Legacy(IMKClientConnection_XPC) setIMKXPCEndpoint:forBundleIdentifier:]_block_invoke
- ___83-[IMKInputSession_Legacy _attributesFromRangeViaGetSelectedText:completionHandler:]_block_invoke
- ___83-[IMKInputSession_Legacy insertText:replacementRange:validFlags:completionHandler:]_block_invoke
- ___83-[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:validFlags:]_block_invoke
- ___83-[IMKInputSession_Modern _attributesFromRangeViaGetSelectedText:completionHandler:]_block_invoke
- ___83-[IMKInputSession_Modern insertText:replacementRange:validFlags:completionHandler:]_block_invoke
- ___83-[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:validFlags:]_block_invoke
- ___84-[IMKInputSession_Legacy attributesForCharacterIndex_andLineRect:completionHandler:]_block_invoke
- ___84-[IMKInputSession_Modern attributesForCharacterIndex_andLineRect:completionHandler:]_block_invoke
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_10
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_11
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_12
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_13
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_14
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_2
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_3
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_4
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_5
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_6
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_7
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_8
- ___85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_9
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_10
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_11
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_12
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_13
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_14
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_2
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_3
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_4
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_5
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_6
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_7
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_8
- ___85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_9
- ___86-[IMKInputSession_Legacy _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]_block_invoke
- ___86-[IMKInputSession_Modern _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]_block_invoke
- ___87-[IMKInputSession_Legacy imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]_block_invoke
- ___87-[IMKInputSession_Legacy imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]_block_invoke_2
- ___87-[IMKInputSession_Modern imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]_block_invoke
- ___87-[IMKInputSession_Modern imkxpc_presentFunctionRowItemTextInputViewWithEndpoint:reply:]_block_invoke_2
- ___89-[IMKClient_Legacy(IMKClientConnection_XPC) invalidateIMKXPCEndpointForBundleIdentifier:]_block_invoke
- ___90-[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:completionHandler:]_block_invoke
- ___90-[IMKInputSession_Legacy setMarkedText:selectionRange:replacementRange:completionHandler:]_block_invoke_2
- ___90-[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:completionHandler:]_block_invoke
- ___90-[IMKInputSession_Modern setMarkedText:selectionRange:replacementRange:completionHandler:]_block_invoke_2
- ___92-[IMKInputSession_Legacy presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:]_block_invoke
- ___92-[IMKInputSession_Modern presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:]_block_invoke
- ___94+[IMKInputSession_Legacy IMKXPCPerformBlockOnMainThreadInMode:performHow:callerCmd:workBlock:]_block_invoke
- ___94-[IMKInputSession_Legacy tryHandleEventSwitchedInputMode:eventWasHandled:continuationHandler:]_block_invoke
- ___94-[IMKInputSession_Modern tryHandleEventSwitchedInputMode:eventWasHandled:continuationHandler:]_block_invoke
- ___96-[IMKInputSession_Legacy imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]_block_invoke
- ___96-[IMKInputSession_Legacy imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]_block_invoke_2
- ___96-[IMKInputSession_Modern imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]_block_invoke
- ___96-[IMKInputSession_Modern imkxpc_setMarkedText:selectionRange:replacementRange:validFlags:reply:]_block_invoke_2
- ___98-[IMKInputSession_Legacy tryUpdateIMKMarkedRange_withDispatchCondition:dispatchWork:continuation:]_block_invoke
- ___98-[IMKInputSession_Modern tryUpdateIMKMarkedRange_withDispatchCondition:dispatchWork:continuation:]_block_invoke
- ____ZL22IMKClientRunLoopModernv_block_invoke
- ___block_descriptor_57_e8_32o40r_e5_v8?0l
- ___block_descriptor_64_e8_32o40o48r_e5_v8?0l
- ___block_descriptor_64_e8_32o40r_e5_v8?0l
- ___block_descriptor_65_e8_32o40o48r_e5_v8?0l
- __block_literal_global.1169
- __block_literal_global.1176
- __block_literal_global.1183
- __block_literal_global.1188
- __block_literal_global.1320
- __block_literal_global.1327
- __block_literal_global.1332
- __block_literal_global.1337
- __block_literal_global.160
- __block_literal_global.2005
- __block_literal_global.254
- __block_literal_global.392
- __block_literal_global.533
- __block_literal_global.641
- __block_literal_global.794
- __block_literal_global.99
- _class_setSuperclass
- _objc_exception_rethrow
- _objc_msgSend$deferActions:
- _objc_msgSend$getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- _objc_msgSend$isGeneralDebuggingOn
- _objc_msgSend$signal
- _objc_msgSend$subclass
- _objc_msgSend$wait:
- _objc_msgSend$whileAwaitingReplyFromProcess:performActions:
- _objc_msgSend$whileAwaitingReplyPerformActions:
- _objc_msgSend$withActivity:performActions:
- _pthread_getname_np
- _pthread_setname_np
CStrings:
- "%!s(MISSING): chose %!@(MISSING)"
- "(awaiting reply from input method with PID %!d(MISSING))"
- "(input method %!u(MISSING) %!@(MISSING))"
- "+[IMKClient subclass]"
- "+[IMKInputSession subclass]"
- "-[IMKClient_Legacy(IMKClientConnection_XPC) _getServerXPCProxyForSession:]"
- "./IMKClient/Sources/IMKClientLegacyModern.m"
- "./IMKClient/Sources/IMKInputSession_Modern.m"
- "ClientRunLoopModern"
- "IMKClientRunLoopModern"
- "IMKClient_Legacy"
- "IMKClient_Modern"
- "IMKInputSession_Legacy"
- "IMKInputSession_Modern"
- "InputMethodKit"
- "Invalid parameter not satisfying: %!s(MISSING)"
- "actions"
- "activity.length > 0"
- "bool IMKClientRunLoopModern()_block_invoke"
- "failed to get bytes"
- "insufficiently boolish"
- "pthread_getname_np failed"
- "pthread_setname_np (new) failed"
- "pthread_setname_np (old) failed"
- "unable to format string"
- "unable to instantiate"
- "unable to obtain class"
- "unable to obtain standard user defaults"
- "unexpected thread"

```
