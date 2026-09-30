## TextInputUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/TextInputUI.framework/Versions/A/TextInputUI`

```diff

-9127.0.79.0.0
-  __TEXT.__text: 0x10c774
-  __TEXT.__objc_methlist: 0xf07c
-  __TEXT.__const: 0x2dd0
-  __TEXT.__dlopen_cstrs: 0x1eb
-  __TEXT.__swift5_typeref: 0x168e
-  __TEXT.__constg_swiftt: 0x13cc
+9127.0.84.0.0
+  __TEXT.__text: 0x110ddc
+  __TEXT.__objc_methlist: 0xf384
+  __TEXT.__const: 0x2e1e
+  __TEXT.__dlopen_cstrs: 0x22c
+  __TEXT.__swift5_typeref: 0x1694
+  __TEXT.__constg_swiftt: 0x13e4
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_reflstr: 0x7e5
   __TEXT.__swift5_fieldmd: 0x9cc
   __TEXT.__swift5_assocty: 0x270
-  __TEXT.__cstring: 0xcd18
+  __TEXT.__cstring: 0xc8a3
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0xf8
-  __TEXT.__oslogstring: 0x48ac
-  __TEXT.__swift5_capture: 0x448
+  __TEXT.__swift5_capture: 0x434
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__oslogstring: 0x4c00
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0xcc
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__swift5_protos: 0xc
   __TEXT.__ustring: 0x258
-  __TEXT.__unwind_info: 0x3718
+  __TEXT.__unwind_info: 0x37f8
   __TEXT.__eh_frame: 0x11b4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76c8
-  __DATA_CONST.__objc_classlist: 0x680
+  __DATA_CONST.__const: 0x76e0
+  __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x270
+  __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9968
+  __DATA_CONST.__objc_selrefs: 0x9b78
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x428
-  __DATA_CONST.__objc_arraydata: 0x948
-  __DATA_CONST.__got: 0x1270
-  __AUTH_CONST.__const: 0x2548
-  __AUTH_CONST.__cfstring: 0xde80
-  __AUTH_CONST.__objc_const: 0x18008
-  __AUTH_CONST.__objc_intobj: 0x378
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __DATA_CONST.__objc_superrefs: 0x430
+  __DATA_CONST.__objc_arraydata: 0xa10
+  __DATA_CONST.__got: 0x1280
+  __AUTH_CONST.__const: 0x25a0
+  __AUTH_CONST.__cfstring: 0xe240
+  __AUTH_CONST.__objc_const: 0x18540
+  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH_CONST.__auth_got: 0x1608
-  __AUTH.__objc_data: 0x3040
+  __AUTH_CONST.__auth_got: 0x1620
+  __AUTH.__objc_data: 0x30f0
   __AUTH.__data: 0x758
-  __DATA.__objc_ivar: 0x1144
-  __DATA.__data: 0x23c8
-  __DATA.__bss: 0x2350
+  __DATA.__objc_ivar: 0x118c
+  __DATA.__data: 0x2478
+  __DATA.__bss: 0x23a8
   __DATA.__common: 0x168
-  __DATA_DIRTY.__objc_data: 0x20c8
+  __DATA_DIRTY.__objc_data: 0x20d0
   __DATA_DIRTY.__data: 0x3c0
   __DATA_DIRTY.__bss: 0x588
   __DATA_DIRTY.__common: 0x68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6156
-  Symbols:   14161
-  CStrings:  2472
+  Functions: 6234
+  Symbols:   14331
+  CStrings:  2494
 
Symbols:
+ +[TUIEmojiRemoteKeyViewProvider isDynamicEmojiLayoutEnabled]
+ +[TUIEmojiRemoteKeyViewProvider sharedProvider]
+ +[TUIGenmojiCandidateCell reuseIdentifier]
+ +[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]
+ +[TUIKeyplane dynamicEmojiReservedAssistantBarHeightForLayoutClass:]
+ +[TUIKeyplane isRegularWidthLayoutClass:]
+ +[TUIKeyplane layoutHasNumberRow:]
+ +[TUIKeyplaneView constrainedGridSkipsKeyplaneInsetCorrectionForLayoutClass:hostIsEmojiPoster:]
+ +[TUIKeyplaneView emojiGridBaseOffsetsForSurface:layoutClass:minorEdgeWidth:nextToKeyplane:constrainedToHost:]
+ +[TUIKeyplaneView hostProcessIsEmojiPoster]
+ -[TUICandidateGeneratorInstallContext .cxx_destruct]
+ -[TUICandidateGeneratorInstallContext setTextComposerWrapper:]
+ -[TUICandidateGeneratorInstallContext textComposerWrapper]
+ -[TUICandidateThrottler _queueOnly_updateWithAutocorrectionList:]
+ -[TUIEmojiRemoteKeyViewProvider _remoteViewClassForDisplayType:]
+ -[TUIEmojiRemoteKeyViewProvider remoteViewForKey:inKeyplane:screenTraits:]
+ -[TUIGenmojiCandidateCell .cxx_destruct]
+ -[TUIGenmojiCandidateCell bottomPaddingConstraint]
+ -[TUIGenmojiCandidateCell commonInit]
+ -[TUIGenmojiCandidateCell genmojiContentView]
+ -[TUIGenmojiCandidateCell initWithCoder:]
+ -[TUIGenmojiCandidateCell initWithFrame:]
+ -[TUIGenmojiCandidateCell layoutSubviews]
+ -[TUIGenmojiCandidateCell leftPaddingConstraint]
+ -[TUIGenmojiCandidateCell rightPaddingConstraint]
+ -[TUIGenmojiCandidateCell setBottomPaddingConstraint:]
+ -[TUIGenmojiCandidateCell setCandidate:]
+ -[TUIGenmojiCandidateCell setGenmojiContentView:]
+ -[TUIGenmojiCandidateCell setLeftPaddingConstraint:]
+ -[TUIGenmojiCandidateCell setRightPaddingConstraint:]
+ -[TUIGenmojiCandidateCell setStyle:]
+ -[TUIGenmojiCandidateCell setTopPaddingConstraint:]
+ -[TUIGenmojiCandidateCell topPaddingConstraint]
+ -[TUIGenmojiCandidateCell updateLayout]
+ -[TUIInputSession forwardInvocation:]
+ -[TUIInputSession methodSignatureForSelector:]
+ -[TUIInputSession respondsToSelector:]
+ -[TUIInputSessionManager inputSessionForHostAuditToken:]
+ -[TUIKBKeyView installedRemoteContentView]
+ -[TUIKBKeyView setInstalledRemoteContentView:]
+ -[TUIKBKeyView(RemoteContent) installRemoteContentView:inContainerView:leadingExtent:trailingExtent:verticalExtent:bottomOffset:topOffset:]
+ -[TUIKey isLastKeyBeforeSplit]
+ -[TUIKey pairedSplitKey]
+ -[TUIKey setLastKeyBeforeSplit:]
+ -[TUIKey setPairedSplitKey:]
+ -[TUIKey setSplitRowMultiplier:]
+ -[TUIKey shouldSplitAfter]
+ -[TUIKey splitCopyOfKey]
+ -[TUIKey splitRowMultiplier]
+ -[TUIKeyplane checkForCachedSplitKeys]
+ -[TUIKeyplane duplicateKeyForSplitMode:]
+ -[TUIKeyplane duplicateKeyList]
+ -[TUIKeyplane handleSplitDuplicationForKey:inRow:keyRow:multiplier:layoutType:layoutShape:outSubtreesCopy:]
+ -[TUIKeyplane isCoreKey:]
+ -[TUIKeyplane isEmojiLayout]
+ -[TUIKeyplane moveControlKey:toRowAtIndex:inRowSet:]
+ -[TUIKeyplane numberOfCachedKeys]
+ -[TUIKeyplane setDuplicateKeyList:]
+ -[TUIKeyplane setNumberOfCachedKeys:]
+ -[TUIKeyplane setStackedControlColumnSwitchKey:spanningFromRow:toRow:inRowSet:]
+ -[TUIKeyplane stackedControlColumnSwitchKeyInRowSet:]
+ -[TUIKeyplane unduplicateDoubleHeightKey:fromRow:]
+ -[TUIKeyplane updateStackedControlColumnForRowSet:]
+ -[TUIKeyplane usesStackedControlColumn]
+ -[TUIKeyplaneRowInfo hasMiddlePadding]
+ -[TUIKeyplaneRowInfo setHasMiddlePadding:]
+ -[TUIKeyplaneTransitionRow description]
+ -[TUIKeyplaneTransitionRow stringForKeyArray:]
+ -[TUIKeyplaneView _installRemoteViewForKeyIfAvailable:]
+ -[TUIKeyplaneView _updateHandwritingLayoutWithOffset:isFinished:]
+ -[TUIKeyplaneView _walkKeyplaneAndInstallRemoteViewsIfNeeded]
+ -[TUIKeyplaneView _walkSubtreeForRemoteViews:]
+ -[TUIKeyplaneView currentEmojiGridSurface]
+ -[TUIKeyplaneView emojiGridContainmentView]
+ -[TUIKeyplaneView emojiGridOffsetsConstrainedToHost:]
+ -[TUIKeyplaneView installedRemoteViews]
+ -[TUIKeyplaneView remoteContentViewForKey:]
+ -[TUIKeyplaneView remoteKeyViewProvider]
+ -[TUIKeyplaneView setEmojiGridContainmentView:]
+ -[TUIKeyplaneView setInstalledRemoteViews:]
+ -[TUIKeyplaneView setOverrideScreenTraits:currentKeyboardMode:]
+ -[TUIKeyplaneView setRemoteKeyViewProvider:]
+ -[TUIKeyplaneView setShouldForceResetLayoutForNextKeyplane:]
+ -[TUIKeyplaneView setTraitChangeRegistration:]
+ -[TUIKeyplaneView setTransitionBottomRowSizingConstraint:]
+ -[TUIKeyplaneView shouldForceResetLayoutForNextKeyplane]
+ -[TUIKeyplaneView traitChangeRegistration]
+ -[TUIKeyplaneView transitionBottomRowSizingConstraint]
+ -[TUIKeyplaneView updateBottomRowSpacingForSplitProgress:]
+ OBJC_IVAR_$_TUICandidateGeneratorInstallContext._textComposerWrapper
+ OBJC_IVAR_$_TUICandidateThrottler._timerGeneration
+ OBJC_IVAR_$_TUIGenmojiCandidateCell._bottomPaddingConstraint
+ OBJC_IVAR_$_TUIGenmojiCandidateCell._genmojiContentView
+ OBJC_IVAR_$_TUIGenmojiCandidateCell._leftPaddingConstraint
+ OBJC_IVAR_$_TUIGenmojiCandidateCell._rightPaddingConstraint
+ OBJC_IVAR_$_TUIGenmojiCandidateCell._topPaddingConstraint
+ OBJC_IVAR_$_TUIKBKeyView._installedRemoteContentView
+ OBJC_IVAR_$_TUIKey._lastKeyBeforeSplit
+ OBJC_IVAR_$_TUIKey._pairedSplitKey
+ OBJC_IVAR_$_TUIKey._splitRowMultiplier
+ OBJC_IVAR_$_TUIKeyplane._duplicateKeyList
+ OBJC_IVAR_$_TUIKeyplane._numberOfCachedKeys
+ OBJC_IVAR_$_TUIKeyplaneRowInfo._hasMiddlePadding
+ OBJC_IVAR_$_TUIKeyplaneView._emojiGridContainmentView
+ OBJC_IVAR_$_TUIKeyplaneView._installedRemoteViews
+ OBJC_IVAR_$_TUIKeyplaneView._remoteKeyViewProvider
+ OBJC_IVAR_$_TUIKeyplaneView._shouldForceResetLayoutForNextKeyplane
+ OBJC_IVAR_$_TUIKeyplaneView._traitChangeRegistration
+ OBJC_IVAR_$_TUIKeyplaneView._transitionBottomRowSizingConstraint
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_TUIEmojiRemoteKeyViewProvider
+ _OBJC_CLASS_$_TUIGenmojiCandidateCell
+ _OBJC_METACLASS_$_TUIEmojiRemoteKeyViewProvider
+ _OBJC_METACLASS_$_TUIGenmojiCandidateCell
+ _TUIEmojiRemoteKeyViewProviderLogger.log
+ _TUIEmojiRemoteKeyViewProviderLogger.onceToken
+ __OBJC_$_CLASS_METHODS_TUIEmojiRemoteKeyViewProvider
+ __OBJC_$_CLASS_METHODS_TUIGenmojiCandidateCell
+ __OBJC_$_CLASS_METHODS_TUIInputSession
+ __OBJC_$_INSTANCE_METHODS_TUIEmojiRemoteKeyViewProvider
+ __OBJC_$_INSTANCE_METHODS_TUIGenmojiCandidateCell
+ __OBJC_$_INSTANCE_METHODS_TUIKBKeyView(RemoteContent)
+ __OBJC_$_INSTANCE_VARIABLES_TUICandidateGeneratorInstallContext
+ __OBJC_$_INSTANCE_VARIABLES_TUIGenmojiCandidateCell
+ __OBJC_$_PROP_LIST_TUICandidateGeneratorInstallContext
+ __OBJC_$_PROP_LIST_TUIEmojiRemoteKeyViewProvider
+ __OBJC_$_PROP_LIST_TUIGenmojiCandidateCell
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUIRemoteKeyViewProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUIRemoteKeyViewProviding
+ __OBJC_$_PROTOCOL_REFS_TUIRemoteKeyViewProviding
+ __OBJC_CLASS_PROTOCOLS_$_TUIEmojiRemoteKeyViewProvider
+ __OBJC_CLASS_RO_$_TUIEmojiRemoteKeyViewProvider
+ __OBJC_CLASS_RO_$_TUIGenmojiCandidateCell
+ __OBJC_LABEL_PROTOCOL_$_TUIRemoteKeyViewProviding
+ __OBJC_METACLASS_RO_$_TUIEmojiRemoteKeyViewProvider
+ __OBJC_METACLASS_RO_$_TUIGenmojiCandidateCell
+ __OBJC_PROTOCOL_$_TUIRemoteKeyViewProviding
+ ___107-[TUIKeyplane handleSplitDuplicationForKey:inRow:keyRow:multiplier:layoutType:layoutShape:outSubtreesCopy:]_block_invoke
+ ___34+[TUIKeyplane layoutHasNumberRow:]_block_invoke
+ ___43+[TUIKeyplaneView hostProcessIsEmojiPoster]_block_invoke
+ ___47+[TUIEmojiRemoteKeyViewProvider sharedProvider]_block_invoke
+ ___65-[TUICandidateThrottler _queueOnly_updateWithAutocorrectionList:]_block_invoke
+ ___92+[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke
+ ___92+[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke_2
+ ____TUIEmojiRemoteKeyViewProviderLogger_block_invoke
+ ___block_descriptor_40_8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
+ ___block_descriptor_48_8_32s40s_e15_B32?08Q16^B24ls32l8s40l8
+ ___block_descriptor_48_8_32w_e5_v8?0lw32l8
+ ___getUIRemoteCategoryKeyViewClass_block_invoke
+ ___getUIRemoteEmojiAndStickerInputViewClass_block_invoke
+ _objc_msgSend$_installRemoteViewForKeyIfAvailable:
+ _objc_msgSend$_queueOnly_updateWithAutocorrectionList:
+ _objc_msgSend$_remoteViewClassForDisplayType:
+ _objc_msgSend$_updateHandwritingLayoutWithOffset:isFinished:
+ _objc_msgSend$_walkKeyplaneAndInstallRemoteViewsIfNeeded
+ _objc_msgSend$_walkSubtreeForRemoteViews:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$cacheKey:
+ _objc_msgSend$checkForCachedSplitKeys
+ _objc_msgSend$configureForGenerativeFlow:
+ _objc_msgSend$constrainedGridSkipsKeyplaneInsetCorrectionForLayoutClass:hostIsEmojiPoster:
+ _objc_msgSend$currentEmojiGridSurface
+ _objc_msgSend$currentHeight
+ _objc_msgSend$duplicateKeyForSplitMode:
+ _objc_msgSend$duplicateKeyList
+ _objc_msgSend$dynamicEmojiReservedAssistantBarHeightForLayoutClass:
+ _objc_msgSend$emojiGridBaseOffsetsForSurface:layoutClass:minorEdgeWidth:nextToKeyplane:constrainedToHost:
+ _objc_msgSend$emojiGridContainmentView
+ _objc_msgSend$emojiGridOffsetsConstrainedToHost:
+ _objc_msgSend$genmojiContentView
+ _objc_msgSend$handleSplitDuplicationForKey:inRow:keyRow:multiplier:layoutType:layoutShape:outSubtreesCopy:
+ _objc_msgSend$hasMiddlePadding
+ _objc_msgSend$hideInputCandidateView
+ _objc_msgSend$hostProcessIsEmojiPoster
+ _objc_msgSend$inputSessionForHostAuditToken:
+ _objc_msgSend$installRemoteContentView:inContainerView:leadingExtent:trailingExtent:verticalExtent:bottomOffset:topOffset:
+ _objc_msgSend$installedRemoteContentView
+ _objc_msgSend$installedRemoteViews
+ _objc_msgSend$isCoreKey:
+ _objc_msgSend$isDynamicEmojiLayoutEnabled
+ _objc_msgSend$isEmojiLayout
+ _objc_msgSend$isHandwritingResizing
+ _objc_msgSend$isLastKeyBeforeSplit
+ _objc_msgSend$isRegularWidthLayoutClass:
+ _objc_msgSend$layoutHasNumberRow:
+ _objc_msgSend$lock
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$moveControlKey:toRowAtIndex:inRowSet:
+ _objc_msgSend$numberOfCachedKeys
+ _objc_msgSend$pairedSplitKey
+ _objc_msgSend$remoteKeyViewProvider
+ _objc_msgSend$remoteViewForKey:inKeyplane:screenTraits:
+ _objc_msgSend$removeLastObject
+ _objc_msgSend$setCurrentHeight:
+ _objc_msgSend$setHasMiddlePadding:
+ _objc_msgSend$setInstalledRemoteContentView:
+ _objc_msgSend$setLastKeyBeforeSplit:
+ _objc_msgSend$setNumberOfCachedKeys:
+ _objc_msgSend$setOverrideScreenTraits:currentKeyboardMode:
+ _objc_msgSend$setPairedSplitKey:
+ _objc_msgSend$setShouldForceResetLayoutForNextKeyplane:
+ _objc_msgSend$setSplitRowMultiplier:
+ _objc_msgSend$setStackedControlColumnSwitchKey:spanningFromRow:toRow:inRowSet:
+ _objc_msgSend$setTextComposerWrapper:
+ _objc_msgSend$setTraitChangeRegistration:
+ _objc_msgSend$setTransitionBottomRowSizingConstraint:
+ _objc_msgSend$shouldForceResetLayoutForNextKeyplane
+ _objc_msgSend$shouldShowRecents
+ _objc_msgSend$splitCopyOfKey
+ _objc_msgSend$splitRowMultiplier
+ _objc_msgSend$stackedControlColumnSwitchKeyInRowSet:
+ _objc_msgSend$stringForKeyArray:
+ _objc_msgSend$textComposerWrapper
+ _objc_msgSend$traitChangeRegistration
+ _objc_msgSend$transitionBottomRowSizingConstraint
+ _objc_msgSend$unduplicateDoubleHeightKey:fromRow:
+ _objc_msgSend$unlock
+ _objc_msgSend$unregisterForTraitChanges:
+ _objc_msgSend$updateBottomRowSpacingForSplitProgress:
+ _objc_msgSend$updateStackedControlColumnForRowSet:
+ _objc_msgSend$usesStackedControlColumn
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV
+ _symbolic _____Sg______t 16GenerativeModels0aB12AvailabilityV s6UInt64V
+ _symbolic _____ySS_____G s18_DictionaryStorageC 16GenerativeModels0cD12AvailabilityV
+ getUIRemoteCategoryKeyViewClass.softClass
+ getUIRemoteEmojiAndStickerInputViewClass.softClass
+ hostProcessIsEmojiPoster.isEmojiPoster
+ hostProcessIsEmojiPoster.onceToken
+ layoutHasNumberRow:.__layouts
+ layoutHasNumberRow:.onceToken
+ sharedProvider.onceToken
+ sharedProvider.sharedInstance
- -[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]
- -[TUIInputSession acceptingCandidateWithTrigger:]
- -[TUIInputSession addSupplementalLexicon:completionHandler:]
- -[TUIInputSession adjustPhraseBoundaryInForwardDirection:granularity:keyboardState:completionHandler:]
- -[TUIInputSession adjustPhraseBoundaryInForwardDirection:keyboardState:completionHandler:]
- -[TUIInputSession candidateRejected:]
- -[TUIInputSession changingContextWithTrigger:]
- -[TUIInputSession generateInlineCompletions:withPrefix:]
- -[TUIInputSession generateRefinementsForCandidate:keyboardState:completionHandler:]
- -[TUIInputSession generateReplacementsForString:keyLayout:continuation:]
- -[TUIInputSession handleAcceptedCandidate:keyboardState:completionHandler:]
- -[TUIInputSession handleKeyboardInput:keyboardState:completionHandler:]
- -[TUIInputSession lastAcceptedCandidateCorrected]
- -[TUIInputSession logDiscoverabilityEvent:userInfo:]
- -[TUIInputSession performHitTestForTouchEvent:keyboardState:continuation:]
- -[TUIInputSession performHitTestForTouchEvents:keyboardState:continuation:]
- -[TUIInputSession predominantLanguageInContextWithCompletionHandler:]
- -[TUIInputSession registerLearning:fullCandidate:keyboardState:mode:]
- -[TUIInputSession registerLearningForCompletion:fullCompletion:context:prefix:mode:]
- -[TUIInputSession removeSupplementalLexiconWithIdentifier:]
- -[TUIInputSession setOriginalInput:]
- -[TUIInputSession skipHitTestForTouchEvent:keyboardState:]
- -[TUIInputSession skipHitTestForTouchEvents:keyboardState:]
- -[TUIInputSession smartSelectionForTextInDocument:inRange:language:tokenizedRanges:options:completion:]
- -[TUIInputSession stickerWithIdentifier:stickerRoles:completionHandler:]
- -[TUIInputSession textAccepted:]
- -[TUIInputSession textAccepted:completionHandler:]
- -[TUIInputSession writeTypologyLogWithCompletionHandler:]
- -[TUIKey isDuplicatedSplitKey]
- -[TUIKey setIsDuplicatedSplitKey:]
- -[TUIKeyboardCandidateMultiplexer internalSharedClientWrapper]
- -[TUIKeyboardCandidateMultiplexer setInternalSharedClientWrapper:]
- -[TUIKeyplane unduplicateDoubleHeightKey:]
- -[TUIKeyplaneView _updateHandwritingLayoutWithOffset:]
- -[TUISmartReplyGenerator createLocalTextComposerClientIfNeeded]
- OBJC_IVAR_$_TUIKey._isDuplicatedSplitKey
- OBJC_IVAR_$_TUIKeyboardCandidateMultiplexer._internalSharedClientWrapper
- __113-[TUIKeyboardCandidateMultiplexer _queueOnly_resultAccumulatorForContext:type:enabledCandidateSources:isDelayed:]_block_invoke
- __113-[TUIKeyboardCandidateMultiplexer _queueOnly_resultAccumulatorForContext:type:enabledCandidateSources:isDelayed:]_block_invoke_2
- __OBJC_$_INSTANCE_METHODS_TUIKBKeyView
- ___92-[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke
- ___92-[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke_2
- ___block_descriptor_40_8_32s_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16ls32l8
- ___block_descriptor_52_8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_52_8_32s40w_e5_v8?0lw40l8s32l8
- _objc_msgSend$_updateHandwritingLayoutWithOffset:
- _objc_msgSend$adjustPhraseBoundaryInForwardDirection:keyboardState:completionHandler:
- _objc_msgSend$createLocalTextComposerClientIfNeeded
- _objc_msgSend$generateInlineCompletions:withPrefix:
- _objc_msgSend$generateRefinementsForCandidate:keyboardState:completionHandler:
- _objc_msgSend$internalSharedClientWrapper
- _objc_msgSend$listWithCorrections:
- _objc_msgSend$performHitTestForTouchEvent:keyboardState:continuation:
- _objc_msgSend$predominantLanguageInContextWithCompletionHandler:
- _objc_msgSend$registerLearning:fullCandidate:keyboardState:mode:
- _objc_msgSend$registerLearningForCompletion:fullCompletion:context:prefix:mode:
- _objc_msgSend$setIsDuplicatedSplitKey:
- _objc_msgSend$setOnContainerUpdate:
- _objc_msgSend$setWithCandidates:proactiveTriggers:
- _objc_msgSend$skipHitTestForTouchEvent:keyboardState:
- _objc_msgSend$subtreesWithProperty:value:
- _objc_msgSend$textAccepted:
- _objc_msgSend$unduplicateDoubleHeightKey:
- _symbolic So28TIKeyboardCandidateResultSetC
CStrings:
+ "#e"
+ "%@|"
+ "6"
+ "<%@: %p; left full = %@; left small = %@; core keys = %@; right small = %@; right full = %@>"
+ "<%@: %p; name = %@; preferredSize = %@; currentKeyplane = %@; frame = %@"
+ "Armenian"
+ "Assamese"
+ "B32@?0@8Q16^B24"
+ "Cached key mismatch but no split support; expected %li vs %li"
+ "Cancelled smart reply generation due to text composer client being nil."
+ "Devanagari-Hindi"
+ "Devanagari-Marathi"
+ "EmojiRemoteKeyViewProvider"
+ "Fula-Adlam-QWERTY"
+ "GenerativeModelsAvailability changed; cleared cached eligibility"
+ "Genmoji Generation Prompt"
+ "Gujarati"
+ "Kannada"
+ "Kazakh-Cyrillic"
+ "Keyplane transition core keys: %@"
+ "Keyplane transition full row\nLeft: %@\nRight: %@"
+ "Keyplane transition small row\nLeft: %@\nRight: %@"
+ "Khmer"
+ "Korean10Key-Small-Wide"
+ "Kurdish-Sorani-QWERTY"
+ "Malayalam"
+ "Mongolian-Cyrillic"
+ "No view controller is set to receive autocorrections"
+ "Now resetting layout for updated keyplane."
+ "Oriya"
+ "Provider returned nil for key %{public}@ displayType=%d"
+ "Punjabi"
+ "Punjabi-Phonetic"
+ "QWERTY-Kurdish-Kurmanji"
+ "QWERTY-Numbers"
+ "QWERTY-VIQR"
+ "R"
+ "Remote view class %{public}@ does not respond to expected init"
+ "Santali-OlChiki-QWERTY"
+ "Screen traits changed split support. Force a reset on the next keyplane change."
+ "Sinhala"
+ "Stale timer handler fired (gen %lu, current %lu) - ignoring"
+ "Suppressing GLP search candidate: cannot evaluate authentication"
+ "TUIGenmojiCandidateCell"
+ "Tajik-Cyrillic"
+ "Tamil"
+ "Telugu"
+ "UIRemoteCategoryKeyView"
+ "UIRemoteEmojiAndStickerInputView"
+ "Uzbek-Cyrillic"
+ "W!!"
+ "[%@:%@] forwarding invocation: [%@], target: %@, identifier: [%@]"
+ "[install-HOIST] key=%{public}@ hoisting grid into containment=%p so its variant selector draws above the search bar"
+ "[install-HOST-MISS] key=%{public}@ — no host TUIKBKeyView in storedKeyViews; falling back to sibling install"
+ "[install-HOST] key=%{public}@ host=%p hostFrame=%@"
+ "[install-WINDOW-MISS] key=%{public}@ host has no window yet — API fell back to host bounds; will retry on next walk"
+ "com.apple.EmojiPoster"
+ "dynamic_emoji_layout"
+ "|"
+ "\x8a"
- "#T"
- "-[TUIInputSession acceptingCandidateWithTrigger:]"
- "-[TUIInputSession addSupplementalLexicon:completionHandler:]"
- "-[TUIInputSession adjustPhraseBoundaryInForwardDirection:granularity:keyboardState:completionHandler:]"
- "-[TUIInputSession adjustPhraseBoundaryInForwardDirection:keyboardState:completionHandler:]"
- "-[TUIInputSession candidateRejected:]"
- "-[TUIInputSession changingContextWithTrigger:]"
- "-[TUIInputSession generateInlineCompletions:withPrefix:]"
- "-[TUIInputSession generateRefinementsForCandidate:keyboardState:completionHandler:]"
- "-[TUIInputSession generateReplacementsForString:keyLayout:continuation:]"
- "-[TUIInputSession handleAcceptedCandidate:keyboardState:completionHandler:]"
- "-[TUIInputSession handleKeyboardInput:keyboardState:completionHandler:]"
- "-[TUIInputSession lastAcceptedCandidateCorrected]"
- "-[TUIInputSession logDiscoverabilityEvent:userInfo:]"
- "-[TUIInputSession performHitTestForTouchEvent:keyboardState:continuation:]"
- "-[TUIInputSession performHitTestForTouchEvents:keyboardState:continuation:]"
- "-[TUIInputSession predominantLanguageInContextWithCompletionHandler:]"
- "-[TUIInputSession registerLearning:fullCandidate:keyboardState:mode:]"
- "-[TUIInputSession registerLearningForCompletion:fullCompletion:context:prefix:mode:]"
- "-[TUIInputSession removeSupplementalLexiconWithIdentifier:]"
- "-[TUIInputSession setOriginalInput:]"
- "-[TUIInputSession skipHitTestForTouchEvent:keyboardState:]"
- "-[TUIInputSession skipHitTestForTouchEvents:keyboardState:]"
- "-[TUIInputSession smartSelectionForTextInDocument:inRange:language:tokenizedRanges:options:completion:]"
- "-[TUIInputSession stickerWithIdentifier:stickerRoles:completionHandler:]"
- "-[TUIInputSession textAccepted:]"
- "-[TUIInputSession textAccepted:completionHandler:]"
- "-[TUIInputSession writeTypologyLogWithCompletionHandler:]"
- "7"
- "<%@: %p> name = %@; preferredSize = %@; currentKeyplane = %@"
- "Autocorrection list contains candidates to be redacted.  Unsupported selector `redactedList`.  Sending empty autocorrection list instead."
- "Candidate result set contains candidates to be redacted.  Unsupported selector `redactedSet`.  Sending empty result set instead."
- "Floating transition core keys: %@"
- "Floating transition floating row\nLeft: %@\nRight: %@"
- "Floating transition full row\nLeft: %@\nRight: %@"
- "One Key"
- "W!"
- "z"
```
