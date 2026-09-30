## ScreenReader

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/ScreenReader`

```diff

-964.9.2.0.0
-  __TEXT.__text: 0x297b44
-  __TEXT.__auth_stubs: 0x2b70
-  __TEXT.__objc_methlist: 0x2290c
+964.12.7.1.0
+  __TEXT.__text: 0x296ddc
+  __TEXT.__auth_stubs: 0x2b60
+  __TEXT.__objc_methlist: 0x23bdc
   __TEXT.__const: 0xdaa
-  __TEXT.__gcc_except_tab: 0x2f78
-  __TEXT.__cstring: 0x1f92e
+  __TEXT.__gcc_except_tab: 0x320c
+  __TEXT.__cstring: 0x1f98e
   __TEXT.__dlopen_cstrs: 0x66b
   __TEXT.__oslogstring: 0x339
   __TEXT.__ustring: 0x48

   __TEXT.__swift5_types: 0x4
   __TEXT.__dof_SCRMapEle: 0x47e
   __TEXT.__dof_SCRSpeech: 0x21a
-  __TEXT.__unwind_info: 0x7f08
-  __TEXT.__objc_classname: 0x322c
-  __TEXT.__objc_methname: 0x52341
-  __TEXT.__objc_methtype: 0x7e22
-  __TEXT.__objc_stubs: 0x3eb60
-  __DATA_CONST.__got: 0x1aa0
-  __DATA_CONST.__const: 0x2068
-  __DATA_CONST.__objc_classlist: 0xce8
+  __TEXT.__unwind_info: 0x7f40
+  __TEXT.__objc_classname: 0x324c
+  __TEXT.__objc_methname: 0x52444
+  __TEXT.__objc_methtype: 0x7e17
+  __TEXT.__objc_stubs: 0x3ebe0
+  __DATA_CONST.__got: 0x1a98
+  __DATA_CONST.__const: 0x2110
+  __DATA_CONST.__objc_classlist: 0xcf0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12660
+  __DATA_CONST.__objc_selrefs: 0x129f0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x9a0
   __DATA_CONST.__objc_arraydata: 0x7d8
-  __AUTH_CONST.__auth_got: 0x15c8
-  __AUTH_CONST.__const: 0x39e0
+  __AUTH_CONST.__auth_got: 0x15c0
+  __AUTH_CONST.__const: 0x3a00
   __AUTH_CONST.__cfstring: 0x24160
-  __AUTH_CONST.__objc_const: 0x310b8
+  __AUTH_CONST.__objc_const: 0x2efd8
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_intobj: 0x1428
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x8190
+  __AUTH.__objc_data: 0x81e0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x18f4
+  __DATA.__objc_ivar: 0x18f8
   __DATA.__data: 0x1be8
-  __DATA.__bss: 0xbf0
+  __DATA.__bss: 0xc00
   __DATA.__common: 0x108
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A6225583-54B9-35CA-AAA1-B6A61B93244A
-  Functions: 12598
-  Symbols:   28545
-  CStrings:  23149
+  UUID: 69E4927A-DF5B-3CDE-ACD4-C4C88BA32170
+  Functions: 12629
+  Symbols:   28646
+  CStrings:  23158
 
Symbols:
+ +[SCRApplication(ContentChooser) contentChooserSerialQueue].cold.1
+ +[SCRBrailleUtilities _eligibileRequestCategories].cold.1
+ +[SCRBrailleUtilities _ineligibileRequestCategories].cold.1
+ +[SCRBrailleUtilities _isRequestActionEligibleForBrailleAlert:].cold.1
+ +[SCRElement(SCRElementDescription) urlLookupQueue].cold.1
+ +[SCREvent _tagTitleMap].cold.1
+ +[SCRInputMethodManager shared].cold.1
+ +[SCRObserverManager sharedManager].cold.1
+ +[SCROutputManager(SCROutputManagerConfiguration) _getCachedSupportedSynthesizerCharactersForVoice:].cold.1
+ +[SCRPositionUtilities sharedMeasurementFormatter].cold.1
+ +[SCRPositionUtilities sharedNumberFormatter].cold.1
+ +[SCRSitePattern sitePatternStringFromURLString:].cold.1
+ +[SCRSpeechSettings sharedInstance].cold.1
+ +[SCRTextCheckerEngine defaultIssueKindFilter].cold.1
+ +[SCRTextElement _localeName].cold.1
+ +[SCRVisualsRemoteDelegate voiceOverBuiltInFeatureIdentifiers].cold.1
+ +[SCRWorkspace shared].cold.1
+ +[SCRWritingToolsManager shared].cold.1
+ -[SCRApplication _applicationActivated:].cold.1
+ -[SCRApplication _exclusionQueueIDsForKeyboardFocusChange].cold.1
+ -[SCRArgumentParser _checkAndRunSplash].cold.1
+ -[SCRArgumentParser _tearDownMachServicesWithReturnValue:].cold.1
+ -[SCRArgumentParser run].cold.3
+ -[SCRCaptionsProvider _overrideActions].cold.1
+ -[SCRElement handleDragToElement:hint:]
+ -[SCRElement(SCRElementDescription) addInteractableSoundIfNeededToRequest:].cold.1
+ -[SCRElement(SCRElementDescription) addInteractableSoundIfNeededToRequest:].cold.2
+ -[SCRElement(SCRElementNavigation) _navigableElementWithinCriteriaBlock:].cold.1
+ -[SCRElement(SCRWebElementUtilities) webAreaClassForChildUIElement:parent:].cold.1
+ -[SCRElement(SCRWebElementUtilities) webChildInAXOrderForward:visibleOnly:wrapped:didHitBoundary:startElement:].cold.1
+ -[SCRElementRotorManager searchKeyToWebRotorLookup].cold.1
+ -[SCREvent isNavigationEvent].cold.1
+ -[SCREventFactory _lastQuickNavArrowKeyDownEventTime]
+ -[SCREventFactory set_lastQuickNavArrowKeyDownEventTime:]
+ -[SCRFocusMovementNavigationEventInfo description].cold.1
+ -[SCRGroup classForChildUIElement:parent:].cold.1
+ -[SCRGuideItem addDisplayTitleToRequest:].cold.1
+ -[SCRKeyboardKey(SCRKeyboardAdditions) modifiersAsSFSymbols].cold.1
+ -[SCRKeyboardKey(SCRKeyboardAdditions) modifiersSpelledOut].cold.1
+ -[SCRMailTable classForChildUIElement:parent:].cold.1
+ -[SCRNotificationCenterScrollArea shouldAutoFocusOnChildren]
+ -[SCROutputBrailleComponent _showExpandedStatusForStatusCellIndex:].cold.1
+ -[SCROutputBrailleComponent _showExpandedStatusForStatusCellIndex:].cold.2
+ -[SCROutputBrailleComponent _showExpandedStatusForStatusCellIndex:].cold.3
+ -[SCROutputBrailleComponent _showExpandedStatusForStatusCellIndex:].cold.4
+ -[SCROutputBrailleComponent handleBrailleModifierCommand:modifier:persistent:].cold.1
+ -[SCROutputManager localizedNameOfColor:isExactMatch:].cold.1
+ -[SCROutputRequest addAttributedString:category:variants:].cold.1
+ -[SCROutputRequest shouldAddCommaAndPause:].cold.1
+ -[SCROutputUserSubstitutionsManager makeRegexSubstitutionsInAction:componentName:component:].cold.1
+ -[SCRRemoteGuide supportedSearchKeyRotorMapping].cold.1
+ -[SCRRemoteWebGuide supportedSearchKeyRotorMapping].cold.1
+ -[SCRSafariApplication classForChildUIElement:parent:].cold.1
+ -[SCRSortButton handleDragToElement:hint:]
+ -[SCRSortButton tableColumnUIElement]
+ -[SCRSpeechSynthesizer initWithVoice:].cold.1
+ -[SCRTable _columnHeaderDescriptionForCellElement:headerIndex:]
+ -[SCRTable _coordinatesInfoForCell:usedShortCoordinatesStyle:].cold.1
+ -[SCRTable _headerDescriptionForIndex:orientation:]
+ -[SCRTable _headerInfoForIndex:headerUIElement:orientation:]
+ -[SCRTable columnHeaderInfoWithIndex:]
+ -[SCRTable rowHeaderInfoWithIndex:]
+ -[SCRTextArea _attachmentCharacterAttributedString].cold.1
+ -[SCRTextArea _lineFeedCharacterAttributedString].cold.1
+ -[SCRWebArea chainEvent:request:].cold.1
+ -[SCRWebArea(LiveRegions) _liveRegionQueue].cold.1
+ -[SCRWebStitchedText _updateInitializedAttributedContentForUIElement:stitchedContent:content:attributedContent:attributedValue:].cold.1
+ -[SCRWorkspace tutorialSetRecognizedGesture:forActivatorOrGuideEvents:].cold.2
+ -[_SCRLayoutChangedNotificationInfo initWithNotificationInfoDictionary:application:].cold.1
+ GCC_except_table232
+ GCC_except_table243
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table452
+ OBJC_IVAR_$_SCREventFactory.__lastQuickNavArrowKeyDownEventTime
+ SCRBrailleCommandFamilies.cold.1
+ SCRCustomCommandKeys.cold.1
+ SCRIsAppleSilicon.cold.1
+ SCRIsAppleSilicon.isAppleSilicon
+ SCRIsAppleSilicon.onceToken
+ SCRIsCustomAction.cold.1
+ SCRIsDeleteKeyboardKey.cold.1
+ SCRIsSpaceKeyboardKey.cold.1
+ SCRKeyboardLoadInputSourceCommandMappings.cold.1
+ SCRVirtualKeyboardKeyForCommand.cold.1
+ _CGEventGetTimestamp
+ _OBJC_CLASS_$_SCRNotificationCenterScrollArea
+ _OBJC_METACLASS_$_SCRNotificationCenterScrollArea
+ _SCRIsAppleSilicon
+ _SCRLogFVUnlock.cold.1
+ _SCRLogReleaseContext.cold.1
+ _SCRSiteSchemeTypeFromSchemeString.cold.1
+ __47-[SCRWebArea _interestingAncestorForUIElement:]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_SCRNotificationCenterScrollArea
+ __OBJC_CLASS_RO_$_SCRNotificationCenterScrollArea
+ __OBJC_METACLASS_RO_$_SCRNotificationCenterScrollArea
+ ___SCRIsAppleSilicon_block_invoke
+ __block_literal_global.31
+ __block_literal_global.437
+ __block_literal_global.607
+ _keypath_getTm
+ _objc_msgSend$_columnHeaderDescriptionForCellElement:headerIndex:
+ _objc_msgSend$_headerDescriptionForIndex:orientation:
+ _objc_msgSend$_headerInfoForIndex:headerUIElement:orientation:
+ _objc_msgSend$columnHeaderInfoWithIndex:
+ _objc_msgSend$handleDragToElement:hint:
+ _objc_msgSend$hasPlaceholderCharPrefix
+ _objc_msgSend$isMusicApplication
+ _objc_msgSend$rowHeaderInfoWithIndex:
+ _objc_msgSend$setAXAttribute:withNumber:
+ _objc_msgSend$tableColumnUIElement
+ _voMathTypeForSubrole.cold.1
+ setPreventSystemSleep.cold.1
- -[SCRTable _columnHeaderDescriptionForCellElement:cell:]
- -[SCRTable _headerInfoForIndex:ofOrientation:usedHeader:]
- -[SCRTable columnHeaderInfoWithIndex:usedHeader:]
- -[SCRTable rowHeaderInfoWithIndex:usedHeader:]
- -[SCRWritingToolsManager _announceAffordance]
- GCC_except_table242
- GCC_except_table451
- __block_literal_global.25
- __block_literal_global.431
- __block_literal_global.604
- _fmod
- _objc_msgSend$_columnHeaderDescriptionForCellElement:cell:
- _objc_msgSend$_headerInfoForIndex:ofOrientation:usedHeader:
- _objc_msgSend$columnHeaderInfoWithIndex:usedHeader:
- _objc_msgSend$includeColumnIndices
- _objc_msgSend$includeRowIndices
- _objc_msgSend$rowHeaderInfoWithIndex:usedHeader:
- _swift_arrayDestroy
CStrings:
+ "/System/AppleInternal/Library/Frameworks/AccessibilityPerformance.framework/AccessibilityPerformance"
+ "@40@0:8Q16@24q32"
+ "AXIndex"
+ "SCRNotificationCenterScrollArea"
+ "TQ,N,V__lastQuickNavArrowKeyDownEventTime"
+ "__lastQuickNavArrowKeyDownEventTime"
+ "_columnHeaderDescriptionForCellElement:headerIndex:"
+ "_headerDescriptionForIndex:orientation:"
+ "_headerInfoForIndex:headerUIElement:orientation:"
+ "_lastQuickNavArrowKeyDownEventTime"
+ "columnHeaderInfoWithIndex:"
+ "handleDragToElement:hint:"
+ "hasPlaceholderCharPrefix"
+ "init()"
+ "rowHeaderInfoWithIndex:"
+ "setAXAttribute:withNumber:"
+ "set_lastQuickNavArrowKeyDownEventTime:"
+ "tableColumnUIElement"
+ "{?=\"controlOnly\"b1\"eventCaptureEnabled\"b1\"fastSearchEnabled\"b1\"invalid\"b1\"kbCommanderEnabled\"b1\"kbCommanderTracking\"b1\"keyboardPassthruEnabled\"b1\"inKeyboardCaptureDialog\"b1\"modalSessionEnabled\"b1\"numPadCommanderEnabled\"b1\"quickNavOverridesSelectionEvents\"b1\"speakAfterTextInsertionEnabled\"b1\"vocFollowsKeyWindow\"b1\"arrowKeyQuickNavEnabled\"b1\"singleKeyQuickNavEnabled\"b1\"arrowKeyQuickNavTemporarilyDisabled\"b1\"singleKeyQuickNavTemporarilyDisabled\"b1\"leftRightQuickNavDoesSomething\"b1\"exploreAllElementsEnabled\"b1}"
+ "\xf0\xf0\xf0\xf0\xf0A"
- "@32@0:8Q16^B24"
- "@40@0:8@16{SCRDataCell=QQ}24"
- "@40@0:8Q16q24^B32"
- "SCRTextElement.writingToolsAvailable"
- "_announceAffordance"
- "_columnHeaderDescriptionForCellElement:cell:"
- "_headerInfoForIndex:ofOrientation:usedHeader:"
- "columnHeaderInfoWithIndex:usedHeader:"
- "rowHeaderInfoWithIndex:usedHeader:"
- "{?=\"controlOnly\"b1\"eventCaptureEnabled\"b1\"fastSearchEnabled\"b1\"invalid\"b1\"kbCommanderEnabled\"b1\"kbCommanderTracking\"b1\"keyboardPassthruEnabled\"b1\"inKeyboardCaptureDialog\"b1\"modalSessionEnabled\"b1\"numPadCommanderEnabled\"b1\"quickNavOverridesSelectionEvents\"b1\"speakAfterTextInsertionEnabled\"b1\"vocFollowsKeyWindow\"b1\"arrowKeyQuickNavEnabled\"b1\"singleKeyQuickNavEnabled\"b1\"arrowKeyQuickNavTemporarilyDisabled\"b1\"singleKeyQuickNavTemporarilyDisabled\"b1\"exploreAllElementsEnabled\"b1}"
- "\xf0\xf0\xf0\xf0\xf01"

```
