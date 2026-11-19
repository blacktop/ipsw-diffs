## ScreenReader

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader`

```diff

-1048.3.0.0.0
-  __TEXT.__text: 0x2d8e30
-  __TEXT.__objc_methlist: 0x25ac8
+1050.3.5.0.0
+  __TEXT.__text: 0x2ddd84
+  __TEXT.__objc_methlist: 0x25e18
   __TEXT.__dlopen_cstrs: 0x6c9
   __TEXT.__const: 0x1470
   __TEXT.__swift5_typeref: 0x664

   __TEXT.__swift5_reflstr: 0x1d4
   __TEXT.__swift5_fieldmd: 0x258
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__cstring: 0x1e15c
-  __TEXT.__oslogstring: 0x1441
+  __TEXT.__cstring: 0x1e6ee
+  __TEXT.__oslogstring: 0x1475
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x90

   __TEXT.__ustring: 0x48
   __TEXT.__dof_SCRMapEle: 0x47e
   __TEXT.__dof_SCRSpeech: 0x21a
-  __TEXT.__unwind_info: 0x8b30
-  __TEXT.__eh_frame: 0x1098
+  __TEXT.__unwind_info: 0x8bf0
+  __TEXT.__eh_frame: 0x1110
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f80
-  __DATA_CONST.__objc_classlist: 0xd18
+  __DATA_CONST.__const: 0x1fc0
+  __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d18
+  __DATA_CONST.__objc_selrefs: 0x13f40
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x9a8
-  __DATA_CONST.__objc_arraydata: 0x8b0
-  __DATA_CONST.__got: 0x2130
-  __AUTH_CONST.__const: 0x49b8
-  __AUTH_CONST.__cfstring: 0x23640
-  __AUTH_CONST.__objc_const: 0x25358
-  __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH_CONST.__objc_intobj: 0x1590
+  __DATA_CONST.__objc_superrefs: 0x9b0
+  __DATA_CONST.__objc_arraydata: 0x8e8
+  __DATA_CONST.__got: 0x2148
+  __AUTH_CONST.__const: 0x4a08
+  __AUTH_CONST.__cfstring: 0x23ae0
+  __AUTH_CONST.__objc_const: 0x25578
+  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__objc_intobj: 0x15d8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1f60
+  __AUTH_CONST.__auth_got: 0x1fd8
   __AUTH_CONST.__auth_ptr: 0x288
-  __AUTH.__objc_data: 0x8650
+  __AUTH.__objc_data: 0x86a0
   __AUTH.__data: 0x560
-  __DATA.__objc_ivar: 0x1a80
-  __DATA.__data: 0x2270
-  __DATA.__bss: 0x1318
+  __DATA.__objc_ivar: 0x1aa4
+  __DATA.__data: 0x2290
+  __DATA.__bss: 0x1328
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13721
-  Symbols:   29183
-  CStrings:  5088
+  Functions: 13797
+  Symbols:   29342
+  CStrings:  5134
 
Symbols:
+ +[SCRBrailleManager _relativeIndexBasedRangeFor:textProvider:]
+ +[SCRBrailleManager _textLineRangeForTextAreaStartLineIndex:endLineIndex:currentLineIndex:]
+ +[SCRBrailleUtilities brailleLineIsEmptyContentPlaceholder:]
+ +[SCRBrailleUtilities refreshSelectionOnCurrentBrailleTextLineKeepingWindow:]
+ +[SCRElement(SCRElementEventHandling) isScreenRecordingInProgress]
+ -[AXFUIElement(SCRExtensions) isHostedViewSceneWindow]
+ -[SCRApplication echoPassThroughValueForElement:]
+ -[SCRApplication navigationSelectionAwaitingEcho]
+ -[SCRApplication setNavigationSelectionAwaitingEcho:]
+ -[SCRBrailleManager refreshSelectionOnCurrentTextLineKeepingWindow:]
+ -[SCRCell _rowSpeaksExpandedStatus]
+ -[SCRCell mouseHotSpot]
+ -[SCRCell traitsSortingDescendantDescription]
+ -[SCRElement axDescriptionOrTitle]
+ -[SCRElement hasAXDescriptionOrTitle]
+ -[SCRElement(SCRElementDescription) _processDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:perEntry:]
+ -[SCRElement(SCRElementDescription) _spokenStringValueForRawStringValue:role:subrole:traits:]
+ -[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:defaultCategory:]
+ -[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:updatingMutableVariants:]
+ -[SCRElement(SCRElementEventHandling) _bringUpSiriDispatchHandler:]
+ -[SCRElement(SCRElementEventHandling) _intelligenceOptionsDispatchHandler:]
+ -[SCRElement(SCRElementEventHandling) _speakCurrentSearchDispatchHandler:]
+ -[SCRElement(SCRElementEventHandling) _startScreenRecording:]
+ -[SCRElement(SCRElementEventHandling) _stopScreenRecording:]
+ -[SCRElement(SCRElementInteraction) _applicationsBrowsableByRotor]
+ -[SCRElement(SCRElementInteraction) handleApplicationsMovement:request:]
+ -[SCRElement(SCRElementInteraction) handleBoundaryReachedWithEvent:request:forward:discardEscapeSpeech:]
+ -[SCRElement(SCRElementInteraction) intelligenceOptionsGuide]
+ -[SCRElement(SCRElementInteraction) isAtBoundaryInDirection:]
+ -[SCRElement(SCRElementInteraction) performBringUpSiriWithRequest:]
+ -[SCRElement(SCRElementInteraction) presentIntelligenceOptionsForRequest:]
+ -[SCRElement(SCRElementInteraction) shouldAutoDrillOutAtBoundary]
+ -[SCRElement(SCRElementInteraction) shouldEchoValueDuringPassThroughDrag]
+ -[SCRElementRotorManager pendingApplicationSelection]
+ -[SCRElementRotorManager setPendingApplicationSelection:]
+ -[SCREventFactory(Gesture) _processPreCommand:]
+ -[SCREventFactory(Gesture) _processPressEventWithGestureString:factory:failSilently:modifierMask:ignoreHelp:]
+ -[SCRIncrementor _echoValueChangeFrom:toRequest:]
+ -[SCRIncrementor _echoesValueThroughTextFieldParent]
+ -[SCRList setFocusedChild:]
+ -[SCRLiveActivity _appendContentDescriptionsOfElement:toArray:hostPid:depth:]
+ -[SCRLiveActivity _owningApplicationTitle]
+ -[SCRLiveActivity _remoteDescendantPidOfElement:hostPid:depth:]
+ -[SCRLiveActivity roleDescription]
+ -[SCRLiveActivity valueDescription]
+ -[SCRMailCell traitsSortingDescendantDescription]
+ -[SCRMailWebArea setSuppressesValueDescriptionForReadToEnd:]
+ -[SCRMailWebArea suppressesValueDescriptionForReadToEnd]
+ -[SCROutputBrailleComponent handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROutputBrailleComponent handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROutputBrailleComponent handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROutputBrailleComponent handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
+ -[SCROutputManager _configureMaximumFramesPerSlice]
+ -[SCRPDFGroup _isTransparentWrapper]
+ -[SCRPassThroughManager lastEchoedValue]
+ -[SCRPassThroughManager lastNotificationEchoTime]
+ -[SCRPassThroughManager lastPollTime]
+ -[SCRPassThroughManager setLastEchoedValue:]
+ -[SCRPassThroughManager setLastNotificationEchoTime:]
+ -[SCRPassThroughManager setLastPollTime:]
+ -[SCRSearchManager speakCurrentSearchWithRequest:]
+ -[SCRSlider shouldEchoValueDuringPassThroughDrag]
+ -[SCRSystemUIServerApplication _expandedOverflowIndicatorFromMenuExtras:]
+ -[SCRSystemUIServerApplication _overflowIndicatorFromMenuExtras:]
+ -[SCRSystemUIServerApplication classForChildUIElement:parent:]
+ -[SCRSystemUIServerApplication isMenuExtraFrame:inMenubarFrame:]
+ -[SCRTextArea _isShownOnBrailleLine:]
+ -[SCRTextArea _refreshBrailleLineIfValueChangedWithoutDetails:uiElement:]
+ -[SCRTextArea _refreshSelectionOnCurrentBrailleTextLineKeepingWindow:]
+ -[SCRTextArea navigationSelectionAwaitingEcho]
+ -[SCRTextArea setNavigationSelectionAwaitingEcho:]
+ -[SCRWindow _siriUIAffordanceBoundsChanged:]
+ -[SCRWindow isWritingToolsPanelWindow]
+ -[SCRWindowManagerApplication isShowingDesktop]
+ -[SCRWorkspace createBrailleManagerForTesting]
+ -[SCRWritingToolsManager _focusIntoPanel:fromElement:request:event:]
+ -[SCRWritingToolsManager lastPanelFocusedUIElement]
+ -[SCRWritingToolsManager panelVisible]
+ -[SCRWritingToolsManager panel]
+ -[SCRWritingToolsManager setLastPanelFocusedUIElement:]
+ -[SCRWritingToolsManager setPanel:]
+ -[SCRXcodeTextElement _addCodingAnnouncementsToRequest:forEchoedRange:]
+ -[SCRXcodeTextElement _announceLineNumberForLine:moveType:request:]
+ -[SCRXcodeTextElement _beginLineGranularityReadAtPosition:]
+ -[SCRXcodeTextElement _currentLineNumberForVOCursor]
+ -[SCRXcodeTextElement _endLineGranularityRead]
+ -[SCRXcodeTextElement echoCharacterAttributedString:variants:request:]
+ -[SCRXcodeTextElement echoDataInRange:request:showOnScreen:braille:]
+ -[SCRXcodeTextElement readNextLine:]
+ -[SCRXcodeTextElement readPreviousLine:]
+ GCC_except_table10394
+ GCC_except_table10398
+ GCC_except_table10402
+ GCC_except_table10543
+ GCC_except_table10548
+ GCC_except_table11172
+ GCC_except_table11195
+ GCC_except_table11481
+ GCC_except_table11485
+ GCC_except_table11588
+ GCC_except_table1160
+ GCC_except_table1173
+ GCC_except_table11810
+ GCC_except_table12044
+ GCC_except_table1207
+ GCC_except_table12091
+ GCC_except_table1215
+ GCC_except_table12160
+ GCC_except_table12162
+ GCC_except_table12289
+ GCC_except_table12366
+ GCC_except_table12455
+ GCC_except_table12459
+ GCC_except_table12460
+ GCC_except_table12467
+ GCC_except_table1251
+ GCC_except_table1255
+ GCC_except_table1258
+ GCC_except_table12686
+ GCC_except_table12775
+ GCC_except_table1472
+ GCC_except_table1656
+ GCC_except_table1843
+ GCC_except_table1883
+ GCC_except_table1921
+ GCC_except_table2035
+ GCC_except_table2190
+ GCC_except_table2192
+ GCC_except_table2254
+ GCC_except_table2366
+ GCC_except_table2585
+ GCC_except_table2602
+ GCC_except_table2659
+ GCC_except_table2863
+ GCC_except_table3120
+ GCC_except_table3122
+ GCC_except_table3198
+ GCC_except_table3274
+ GCC_except_table3404
+ GCC_except_table3408
+ GCC_except_table3492
+ GCC_except_table3596
+ GCC_except_table3674
+ GCC_except_table3697
+ GCC_except_table3816
+ GCC_except_table3907
+ GCC_except_table3910
+ GCC_except_table3934
+ GCC_except_table3939
+ GCC_except_table3953
+ GCC_except_table4057
+ GCC_except_table4101
+ GCC_except_table4503
+ GCC_except_table4512
+ GCC_except_table4515
+ GCC_except_table4640
+ GCC_except_table4678
+ GCC_except_table4682
+ GCC_except_table4686
+ GCC_except_table4688
+ GCC_except_table4692
+ GCC_except_table4696
+ GCC_except_table4766
+ GCC_except_table4780
+ GCC_except_table4829
+ GCC_except_table4855
+ GCC_except_table4861
+ GCC_except_table5696
+ GCC_except_table5732
+ GCC_except_table5835
+ GCC_except_table6110
+ GCC_except_table6116
+ GCC_except_table6285
+ GCC_except_table6335
+ GCC_except_table6372
+ GCC_except_table6467
+ GCC_except_table6654
+ GCC_except_table6740
+ GCC_except_table6755
+ GCC_except_table6765
+ GCC_except_table6787
+ GCC_except_table6793
+ GCC_except_table6797
+ GCC_except_table6906
+ GCC_except_table6909
+ GCC_except_table6914
+ GCC_except_table6940
+ GCC_except_table6947
+ GCC_except_table6978
+ GCC_except_table6981
+ GCC_except_table7015
+ GCC_except_table7016
+ GCC_except_table7135
+ GCC_except_table7141
+ GCC_except_table7162
+ GCC_except_table7163
+ GCC_except_table7230
+ GCC_except_table7256
+ GCC_except_table7258
+ GCC_except_table7372
+ GCC_except_table7410
+ GCC_except_table7412
+ GCC_except_table7429
+ GCC_except_table7430
+ GCC_except_table7443
+ GCC_except_table7457
+ GCC_except_table7458
+ GCC_except_table7536
+ GCC_except_table7543
+ GCC_except_table7544
+ GCC_except_table7687
+ GCC_except_table7980
+ GCC_except_table8002
+ GCC_except_table8178
+ GCC_except_table8267
+ GCC_except_table8273
+ GCC_except_table8274
+ GCC_except_table8275
+ GCC_except_table8276
+ GCC_except_table8280
+ GCC_except_table8281
+ GCC_except_table8402
+ GCC_except_table8413
+ GCC_except_table8417
+ GCC_except_table8445
+ GCC_except_table8549
+ GCC_except_table8695
+ GCC_except_table8701
+ GCC_except_table8796
+ GCC_except_table8870
+ GCC_except_table8952
+ GCC_except_table9026
+ GCC_except_table9027
+ GCC_except_table9044
+ GCC_except_table9054
+ GCC_except_table9064
+ GCC_except_table9065
+ GCC_except_table9072
+ GCC_except_table9075
+ GCC_except_table9076
+ GCC_except_table9231
+ GCC_except_table9609
+ GCC_except_table9614
+ GCC_except_table9948
+ GCC_except_table9952
+ GCC_except_table9957
+ OBJC_IVAR_$_SCRApplication._navigationSelectionAwaitingEcho
+ OBJC_IVAR_$_SCRElementRotorManager._pendingApplicationSelection
+ OBJC_IVAR_$_SCRMailWebArea._suppressesValueDescriptionForReadToEnd
+ OBJC_IVAR_$_SCRPassThroughManager._lastEchoedValue
+ OBJC_IVAR_$_SCRPassThroughManager._lastNotificationEchoTime
+ OBJC_IVAR_$_SCRPassThroughManager._lastPollTime
+ OBJC_IVAR_$_SCRWritingToolsManager._lastPanelFocusedUIElement
+ OBJC_IVAR_$_SCRWritingToolsManager._panel
+ OBJC_IVAR_$_SCRXcodeTextElement._isLineGranularityRead
+ OBJC_IVAR_$_SCRXcodeTextElement._lineGranularityReadPosition
+ OBJC_IVAR_$_SCRXcodeTextElement._lineGranularityReadStartLine
+ _OBJC_CLASS_$_NSTask
+ _OBJC_CLASS_$_SCRLiveActivity
+ _OBJC_METACLASS_$_SCRLiveActivity
+ _SCRSpokenGestureTitle
+ __OBJC_$_INSTANCE_METHODS_SCRLiveActivity
+ __OBJC_CLASS_RO_$_SCRLiveActivity
+ __OBJC_METACLASS_RO_$_SCRLiveActivity
+ __SCRProcessExecutableIsWithinBundle
+ __ScreenRecordingTask
+ ___131-[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:defaultCategory:]_block_invoke
+ ___139-[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:updatingMutableVariants:]_block_invoke
+ ___61-[SCRElement(SCRElementEventHandling) _startScreenRecording:]_block_invoke
+ ___61-[SCRElement(SCRElementInteraction) intelligenceOptionsGuide]_block_invoke
+ ___66-[SCRElement(SCRElementInteraction) _applicationsBrowsableByRotor]_block_invoke
+ ___block_descriptor_32_e16_v16?0"NSTask"8l
+ ___block_descriptor_32_e43_q24?0"SCRApplication"8"SCRApplication"16l
+ ___block_descriptor_33_e39_q24?0"AXFUIElement"8"AXFUIElement"16l
+ ___block_descriptor_48_e8_32s40s_e69_v48?0"NSAttributedString"8"NSString"16Q24"NSString"32"NSArray"40l
+ ___block_descriptor_64_e8_32s40s48s56s_e69_v48?0"NSAttributedString"8"NSString"16Q24"NSString"32"NSArray"40l
+ __kLSAuditTokenKey
+ _objc_msgSend$_addCodingAnnouncementsToRequest:forEchoedRange:
+ _objc_msgSend$_announceLineNumberForLine:moveType:request:
+ _objc_msgSend$_appendContentDescriptionsOfElement:toArray:hostPid:depth:
+ _objc_msgSend$_applicationsBrowsableByRotor
+ _objc_msgSend$_beginLineGranularityReadAtPosition:
+ _objc_msgSend$_configureMaximumFramesPerSlice
+ _objc_msgSend$_currentLineNumberForVOCursor
+ _objc_msgSend$_echoValueChangeFrom:toRequest:
+ _objc_msgSend$_echoesValueThroughTextFieldParent
+ _objc_msgSend$_endLineGranularityRead
+ _objc_msgSend$_expandedOverflowIndicatorFromMenuExtras:
+ _objc_msgSend$_focusIntoPanel:fromElement:request:event:
+ _objc_msgSend$_isShownOnBrailleLine:
+ _objc_msgSend$_isTransparentWrapper
+ _objc_msgSend$_overflowIndicatorFromMenuExtras:
+ _objc_msgSend$_owningApplicationTitle
+ _objc_msgSend$_processDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:perEntry:
+ _objc_msgSend$_processPreCommand:
+ _objc_msgSend$_processPressEventWithGestureString:factory:failSilently:modifierMask:ignoreHelp:
+ _objc_msgSend$_refreshBrailleLineIfValueChangedWithoutDetails:uiElement:
+ _objc_msgSend$_refreshSelectionOnCurrentBrailleTextLineKeepingWindow:
+ _objc_msgSend$_relativeIndexBasedRangeFor:textProvider:
+ _objc_msgSend$_remoteDescendantPidOfElement:hostPid:depth:
+ _objc_msgSend$_rowSpeaksExpandedStatus
+ _objc_msgSend$_spokenStringValueForRawStringValue:role:subrole:traits:
+ _objc_msgSend$_supportsAccessibilityRelativeIndexForTextMarker
+ _objc_msgSend$_textLineRangeForTextAreaStartLineIndex:endLineIndex:currentLineIndex:
+ _objc_msgSend$accessibilityLabelOrTitle
+ _objc_msgSend$axDescriptionOrTitle
+ _objc_msgSend$brailleLineIsEmptyContentPlaceholder:
+ _objc_msgSend$descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:defaultCategory:
+ _objc_msgSend$descriptionFromDescendantEntriesIncludingCaption:excludingRoles:sortingTraits:updatingMutableVariants:
+ _objc_msgSend$echoPassThroughValueForElement:
+ _objc_msgSend$elementToken
+ _objc_msgSend$handleApplicationsMovement:request:
+ _objc_msgSend$handleBoundaryReachedWithEvent:request:forward:discardEscapeSpeech:
+ _objc_msgSend$hasAXDescriptionOrTitle
+ _objc_msgSend$hasAccessibilityLabelOrTitle
+ _objc_msgSend$intelligenceOptionsGuide
+ _objc_msgSend$interrupt
+ _objc_msgSend$isAtBoundaryInDirection:
+ _objc_msgSend$isHostedViewSceneWindow
+ _objc_msgSend$isMenuExtraFrame:inMenubarFrame:
+ _objc_msgSend$isScreenRecordingInProgress
+ _objc_msgSend$isTextLine
+ _objc_msgSend$isWritingToolsPanelWindow
+ _objc_msgSend$lastEchoedValue
+ _objc_msgSend$lastNotificationEchoTime
+ _objc_msgSend$lastPollTime
+ _objc_msgSend$launchAndReturnError:
+ _objc_msgSend$navigationSelectionAwaitingEcho
+ _objc_msgSend$panel
+ _objc_msgSend$panelVisible
+ _objc_msgSend$pendingApplicationSelection
+ _objc_msgSend$performBringUpSiriWithRequest:
+ _objc_msgSend$planarPanDisplayLeft:
+ _objc_msgSend$planarPanDisplayRight:
+ _objc_msgSend$presentIntelligenceOptionsForRequest:
+ _objc_msgSend$refreshSelectionOnCurrentBrailleTextLineKeepingWindow:
+ _objc_msgSend$refreshSelectionOnCurrentTextLineKeepingWindow:
+ _objc_msgSend$setArguments:
+ _objc_msgSend$setLastEchoedValue:
+ _objc_msgSend$setLastNotificationEchoTime:
+ _objc_msgSend$setLastPanelFocusedUIElement:
+ _objc_msgSend$setLastPollTime:
+ _objc_msgSend$setLaunchPath:
+ _objc_msgSend$setNavigationSelectionAwaitingEcho:
+ _objc_msgSend$setPanel:
+ _objc_msgSend$setPendingApplicationSelection:
+ _objc_msgSend$setPlaceholderValue:
+ _objc_msgSend$setSuppressesValueDescriptionForReadToEnd:
+ _objc_msgSend$setTerminationHandler:
+ _objc_msgSend$shouldAutoDrillOutAtBoundary
+ _objc_msgSend$shouldEchoValueDuringPassThroughDrag
+ _objc_msgSend$speakCurrentSearchWithRequest:
+ _objc_msgSend$suppressesValueDescriptionForReadToEnd
+ _objc_msgSend$traitsSortingDescendantDescription
+ _proc_pidpath
- -[SCRApplication _lastGlobalValueChangedOutputTime]
- -[SCRApplication set_lastGlobalValueChangedOutputTime:]
- -[SCRCell _identifiersExcludedFromDescendantDescription]
- -[SCRElement(SCRElementDescription) descriptionFromDescendantEntriesIncludingCaption:excludingIdentifiers:updatingMutableVariants:]
- -[SCRElement(SCRElementEventHandling) _showRecognitionOptionsDispatchHandler:]
- -[SCRElement(SCRElementInteraction) presentRecognitionOptionsForRequest:]
- -[SCRElement(SCRElementInteraction) recognitionOptionsGuide]
- -[SCREventFactory(Gesture) _processPreCommand]
- -[SCREventFactory(Gesture) _processPressEventWithGestureString:failSilently:modifierMask:ignoreHelp:]
- -[SCRMenuBarAgentApplication handleLayoutChangeWithInfo:]
- -[SCROutputBrailleComponent handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROutputBrailleComponent handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCRPDFContentList shouldAutoFocusOnChildren]
- -[SCRSiriUIManager _performSettleForWindow:]
- -[SCRSiriUIManager _settleAppearance]
- -[SCRSiriUIManager affordanceSummonedByAction]
- -[SCRSiriUIManager setAffordanceSummonedByAction:]
- -[SCRSiriUIManager wasAffordanceSummonedByAction]
- -[SCRSystemUIServerApplication _focusIntoLiveActivity]
- -[SCRSystemUIServerApplication _menuExtraIndexForLiveActivity]
- -[SCRSystemUIServerApplication dispatchFocusIntoLiveActivity]
- GCC_except_table10340
- GCC_except_table10344
- GCC_except_table10348
- GCC_except_table10490
- GCC_except_table10495
- GCC_except_table11119
- GCC_except_table11142
- GCC_except_table11428
- GCC_except_table11432
- GCC_except_table11534
- GCC_except_table1158
- GCC_except_table1171
- GCC_except_table11756
- GCC_except_table11988
- GCC_except_table12035
- GCC_except_table1205
- GCC_except_table12104
- GCC_except_table12106
- GCC_except_table1213
- GCC_except_table12232
- GCC_except_table12309
- GCC_except_table12398
- GCC_except_table12402
- GCC_except_table12403
- GCC_except_table12410
- GCC_except_table1249
- GCC_except_table1253
- GCC_except_table1256
- GCC_except_table12623
- GCC_except_table12703
- GCC_except_table1470
- GCC_except_table1653
- GCC_except_table1840
- GCC_except_table1879
- GCC_except_table1913
- GCC_except_table2031
- GCC_except_table2172
- GCC_except_table2178
- GCC_except_table2250
- GCC_except_table2358
- GCC_except_table2581
- GCC_except_table2598
- GCC_except_table2655
- GCC_except_table2859
- GCC_except_table3114
- GCC_except_table3116
- GCC_except_table3192
- GCC_except_table3268
- GCC_except_table3392
- GCC_except_table3396
- GCC_except_table3476
- GCC_except_table3579
- GCC_except_table3657
- GCC_except_table3679
- GCC_except_table3793
- GCC_except_table3883
- GCC_except_table3886
- GCC_except_table3909
- GCC_except_table3914
- GCC_except_table3928
- GCC_except_table4029
- GCC_except_table4073
- GCC_except_table4473
- GCC_except_table4482
- GCC_except_table4485
- GCC_except_table4610
- GCC_except_table4648
- GCC_except_table4652
- GCC_except_table4656
- GCC_except_table4658
- GCC_except_table4662
- GCC_except_table4666
- GCC_except_table4736
- GCC_except_table4750
- GCC_except_table4795
- GCC_except_table4799
- GCC_except_table4831
- GCC_except_table5305
- GCC_except_table5662
- GCC_except_table5698
- GCC_except_table5801
- GCC_except_table6071
- GCC_except_table6077
- GCC_except_table6246
- GCC_except_table6296
- GCC_except_table6332
- GCC_except_table6426
- GCC_except_table6613
- GCC_except_table6699
- GCC_except_table6714
- GCC_except_table6724
- GCC_except_table6744
- GCC_except_table6750
- GCC_except_table6754
- GCC_except_table6863
- GCC_except_table6866
- GCC_except_table6871
- GCC_except_table6897
- GCC_except_table6904
- GCC_except_table6935
- GCC_except_table6938
- GCC_except_table6972
- GCC_except_table6973
- GCC_except_table7091
- GCC_except_table7097
- GCC_except_table7118
- GCC_except_table7119
- GCC_except_table7186
- GCC_except_table7212
- GCC_except_table7214
- GCC_except_table7328
- GCC_except_table7366
- GCC_except_table7368
- GCC_except_table7370
- GCC_except_table7385
- GCC_except_table7386
- GCC_except_table7399
- GCC_except_table7413
- GCC_except_table7492
- GCC_except_table7499
- GCC_except_table7500
- GCC_except_table7643
- GCC_except_table7935
- GCC_except_table7957
- GCC_except_table8133
- GCC_except_table8222
- GCC_except_table8228
- GCC_except_table8229
- GCC_except_table8230
- GCC_except_table8231
- GCC_except_table8235
- GCC_except_table8236
- GCC_except_table8357
- GCC_except_table8368
- GCC_except_table8372
- GCC_except_table8399
- GCC_except_table8503
- GCC_except_table8648
- GCC_except_table8654
- GCC_except_table8749
- GCC_except_table8823
- GCC_except_table8905
- GCC_except_table8979
- GCC_except_table8980
- GCC_except_table8997
- GCC_except_table9007
- GCC_except_table9017
- GCC_except_table9018
- GCC_except_table9025
- GCC_except_table9028
- GCC_except_table9029
- GCC_except_table9183
- GCC_except_table9513
- GCC_except_table9556
- GCC_except_table9894
- GCC_except_table9898
- GCC_except_table9903
- OBJC_IVAR_$_SCRApplication.__lastGlobalValueChangedOutputTime
- OBJC_IVAR_$_SCRSiriUIManager._affordanceSummonedByAction
- ___60-[SCRElement(SCRElementInteraction) recognitionOptionsGuide]_block_invoke
- ___60-[SCRList _moveInDirection:event:request:allowFullWrapping:]_block_invoke
- ___block_descriptor_32_e39_q24?0"AXFUIElement"8"AXFUIElement"16l
- ___block_descriptor_40_e8_32r_e22_B16?0"AXFUIElement"8l
- _objc_msgSend$_identifiersExcludedFromDescendantDescription
- _objc_msgSend$_menuExtraIndexForLiveActivity
- _objc_msgSend$_processPreCommand
- _objc_msgSend$_processPressEventWithGestureString:failSilently:modifierMask:ignoreHelp:
- _objc_msgSend$accessibilityIndexOfChild:
- _objc_msgSend$descriptionFromDescendantEntriesIncludingCaption:excludingIdentifiers:updatingMutableVariants:
- _objc_msgSend$dispatchFocusIntoLiveActivity
- _objc_msgSend$getRange:ofAttribute:
- _objc_msgSend$presentRecognitionOptionsForRequest:
- _objc_msgSend$recognitionOptionsGuide
- _objc_msgSend$setFocusedChildAtIndex:
- _objc_msgSend$wasAffordanceSummonedByAction
CStrings:
+ "-A"
+ "-u"
+ "-v"
+ "/usr/sbin/screencapture"
+ "3!"
+ "AXHostedViewSceneWindow"
+ "AXResized"
+ "AXWritingToolsPanel"
+ "Braille: dropped description value \"%@\"; text-line element %lu already holds its line"
+ "ERROR: -- ERROR SETTING UP AUDIO -- CAN'T SET MIXER MAX FRAMES PER SLICE - result code: %ld"
+ "ERROR: -- ERROR SETTING UP AUDIO -- CAN'T SET SOUND UNIT MAX FRAMES PER SLICE - result code: %ld"
+ "Failed to launch screencapture for screen recording: %@"
+ "Global.bringUpSiri"
+ "Global.bringUpSiri.title"
+ "Global.findTextSpeakCurrentSearch"
+ "Global.intelligenceOptions"
+ "Global.intelligenceOptions.title"
+ "Global.startScreenRecording"
+ "Global.startedScreenRecording.failure"
+ "Global.startingScreenRecording.message"
+ "Global.stopScreenRecording"
+ "Global.stoppedScreenRecording.failure"
+ "IEAskAboutImage"
+ "IEFetchAndSpeakDescription"
+ "Navigation echo rejected: %@ marker could not be placed"
+ "No valid PID for application %@"
+ "ReadLine"
+ "ReadWord"
+ "SCRBraille.panPageDown"
+ "SCRBraille.panPageUp"
+ "SCRElement.bringUpSiri"
+ "SCRElement.intelligenceOptions"
+ "SCRElementRotorTypeApplications"
+ "SCRWorkspace.rotor.applications"
+ "Sync'd selection change: navigation echo = %@"
+ "Warning: braille element %lu got a second value (\"%@\" after \"%@\"); a producer is emitting more than one consolidated action for one element. Appending both."
+ "[Error] Interval already ended"
+ "arrived"
+ "awaited"
+ "granularity=line"
+ "granularity=word"
+ "liveActivity"
+ "menu-bar-overflow-indicator-expanded"
+ "no, following the cursor"
+ "q24@?0@\"SCRApplication\"8@\"SCRApplication\"16"
+ "role"
+ "subrole"
+ "v16@?0@\"NSTask\"8"
+ "v48@?0@\"NSAttributedString\"8@\"NSString\"16Q24@\"NSString\"32@\"NSArray\"40"
+ "yes, keeping the window"
- "!q"
- "Global.showRecognitionOptions"
- "Global.showRecognitionOptions.title"
- "SCRElement.showRecognitionOptions"
```
