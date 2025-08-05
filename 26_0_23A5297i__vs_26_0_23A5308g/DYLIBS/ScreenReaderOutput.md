## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-419.0.0.0.0
-  __TEXT.__text: 0x6f6d0
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0x6bd4
-  __TEXT.__gcc_except_tab: 0x18b8
+421.0.0.0.0
+  __TEXT.__text: 0x6f390
+  __TEXT.__auth_stubs: 0x1930
+  __TEXT.__objc_methlist: 0x6c94
+  __TEXT.__gcc_except_tab: 0x186c
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0x56a8
-  __TEXT.__oslogstring: 0x1fab
-  __TEXT.__ustring: 0x9a
+  __TEXT.__cstring: 0x57a8
+  __TEXT.__oslogstring: 0x1f3b
+  __TEXT.__ustring: 0x96
   __TEXT.__swift5_typeref: 0x39a
   __TEXT.__constg_swiftt: 0x414
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e30
+  __TEXT.__unwind_info: 0x1e68
   __TEXT.__eh_frame: 0x678
-  __TEXT.__objc_classname: 0xa9c
-  __TEXT.__objc_methname: 0xf4d3
-  __TEXT.__objc_methtype: 0x224e
-  __TEXT.__objc_stubs: 0xd240
-  __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0xc28
+  __TEXT.__objc_classname: 0xa9a
+  __TEXT.__objc_methname: 0xf4cc
+  __TEXT.__objc_methtype: 0x2242
+  __TEXT.__objc_stubs: 0xd1c0
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0xc58
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d30
+  __DATA_CONST.__objc_selrefs: 0x3d40
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x380
-  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH_CONST.__auth_got: 0xca8
   __AUTH_CONST.__const: 0x1790
-  __AUTH_CONST.__cfstring: 0x4f00
-  __AUTH_CONST.__objc_const: 0xec60
-  __AUTH_CONST.__objc_intobj: 0x9a8
+  __AUTH_CONST.__cfstring: 0x50a0
+  __AUTH_CONST.__objc_const: 0xecd8
+  __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xbd0
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0x820
+  __DATA.__objc_ivar: 0x828
   __DATA.__data: 0x1020
   __DATA.__common: 0x28
   __DATA.__bss: 0x7b8

   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation
   - /System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 75E4E265-7D53-36C5-B54C-65CFB10560E6
-  Functions: 2795
-  Symbols:   8989
-  CStrings:  4641
+  UUID: 29EBFBB2-190A-3A77-AC49-C9209E7E7E5C
+  Functions: 2811
+  Symbols:   9024
+  CStrings:  4674
 
Symbols:
+ +[SCROBrailleUIApp isHidingViews]
+ +[SCROBrailleUIApp showViews]
+ -[SCROBrailleDisplay _forwardToScreenReader:routerIndex:token:BeginLocation:endLocation:appToken:didPerform:]
+ -[SCROBrailleDisplay doubleRouterClickTimeout]
+ -[SCROBrailleDisplay routerClicks]
+ -[SCROBrailleDisplay setRouterClicks:]
+ -[SCROBrailleKey isRouterKey]
+ -[SCROBrailleKey setIsRouterKey:]
+ -[SCROBrailleLine _selectBrailleRange:selectionBegin:selectionEnd:]
+ -[SCROBrailleLine selectContiguousBrailleRange:selectionBegin:selectionEnd:]
+ -[SCROBrailleLine selectEntireLine:selectionEnd:]
+ -[SCROBrailleLine selectUpToRouterIndex:selectionBegin:selectionEnd:]
+ -[SCROBrailleUIApp _requestRefreshBraille]
+ -[SCROBrailleUIBrailleAreaView initialSelectionLength]
+ -[SCROBrailleUIBrailleAreaView setInitialSelectionLength:]
+ -[SCROBrailleUIDisplayManager _commitDisplayedBrailleToTopMostView]
+ -[SCROBrailleUIDisplayManager _speakFocusedListItem]
+ -[SCROBrailleUIDisplayManager _updateIsHidingViews]
+ -[SCROBrailleUIDisplayManager hideViews]
+ -[SCROBrailleUIDisplayManager isHidingViews]
+ -[SCROBrailleUIDisplayManager showViews]
+ -[SCROBrailleUIMainApp _sendAnalytics]
+ -[SCROBrailleUISettingsManager shouldReopenViewsWhenRestart]
+ GCC_except_table16
+ GCC_except_table203
+ GCC_except_table254
+ _AnalyticsSendEventLazy
+ _OBJC_IVAR_$_SCROBrailleDisplay._routerClicks
+ _OBJC_IVAR_$_SCROBrailleKey._isRouterKey
+ _OBJC_IVAR_$_SCROBrailleUIBrailleAreaView._initialSelectionLength
+ _OBJC_IVAR_$_SCROBrailleUIDisplayManager._isHidingViews
+ __OBJC_$_PROP_LIST_SCROBrailleKey
+ ___117-[SCROBrailleTranslationManager printBrailleForText:language:mode:textPositionsRange:locations:textFormattingRanges:]_block_invoke.35
+ ___38-[SCROBrailleUIMainApp _sendAnalytics]_block_invoke
+ ___56-[SCROBrailleDisplayManager _eventQueue_startBrailleUI:]_block_invoke.189
+ ___77-[SCROBrailleTranslationManager textForPrintBraille:language:mode:locations:]_block_invoke.37
+ ____appendBrailleKeysToArray_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_literal_global.136
+ ___block_literal_global.140
+ ___block_literal_global.20
+ ___block_literal_global.22
+ ___block_literal_global.25
+ ___block_literal_global.309
+ ___block_literal_global.312
+ ___block_literal_global.315
+ ___block_literal_global.318
+ ___block_literal_global.321
+ ___block_literal_global.335
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_ScreenReaderOutput
+ _objc_msgSend$_commitDisplayedBrailleToTopMostView
+ _objc_msgSend$_forwardToScreenReader:routerIndex:token:BeginLocation:endLocation:appToken:didPerform:
+ _objc_msgSend$_requestRefreshBraille
+ _objc_msgSend$_selectBrailleRange:selectionBegin:selectionEnd:
+ _objc_msgSend$_sendAnalytics
+ _objc_msgSend$_speakFocusedListItem
+ _objc_msgSend$_updateIsHidingViews
+ _objc_msgSend$doubleRouterClickTimeout
+ _objc_msgSend$hideViews
+ _objc_msgSend$initialSelectionLength
+ _objc_msgSend$isHidingViews
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$routerClicks
+ _objc_msgSend$selectContiguousBrailleRange:selectionBegin:selectionEnd:
+ _objc_msgSend$selectEntireLine:selectionEnd:
+ _objc_msgSend$selectUpToRouterIndex:selectionBegin:selectionEnd:
+ _objc_msgSend$setInitialSelectionLength:
+ _objc_msgSend$setRouterClicks:
+ _objc_msgSend$shouldReopenViewsWhenRestart
+ _objc_msgSend$showViews
+ _objc_msgSend$voiceOverTouchBrailleUIShouldReopenViewsWhenRestart
- -[SCROBrailleDisplay _forwardToScreenReader:Key:routerIndex:token:BeginLocation:endLocation:appToken:didPerform:]
- -[SCROBrailleDisplay routerMultiplicity]
- -[SCROBrailleDisplay setRouterMultiplicity:]
- -[SCROBrailleLine _selectBrailleRange:forwardToScreenReader:updateSelectionBegin:selectionEnd:]
- -[SCROBrailleLine selectContiguousBrailleRange:forwardToScreenReader:updateSelectionBegin:selectionEnd:]
- -[SCROBrailleLine selectEntireLineWithForwardToScreenReader:updateSelectionBegin:selectionEnd:]
- -[SCROBrailleLine selectUpToRouterIndex:forwardToScreenReader:updateSelectionBegin:selectionEnd:]
- GCC_except_table201
- GCC_except_table253
- OBJC_IVAR_$_SCROBrailleKey._hasRouterInfo
- _OBJC_IVAR_$_SCROBrailleDisplay._routerMultiplicity
- _SCROCustomBrailleEnabled
- ___117-[SCROBrailleTranslationManager printBrailleForText:language:mode:textPositionsRange:locations:textFormattingRanges:]_block_invoke.36
- ___56-[SCROBrailleDisplayManager _eventQueue_startBrailleUI:]_block_invoke.188
- ___77-[SCROBrailleTranslationManager textForPrintBraille:language:mode:locations:]_block_invoke.38
- ____appendBrailleKeysToArray_block_invoke.909
- ___block_literal_global.21
- ___block_literal_global.23
- ___block_literal_global.26
- ___block_literal_global.262
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.271
- ___block_literal_global.274
- ___block_literal_global.331
- ___block_literal_global.90
- ___block_literal_global.94
- _kBTDuxburyServiceIdentifier
- _objc_msgSend$_forwardToScreenReader:Key:routerIndex:token:BeginLocation:endLocation:appToken:didPerform:
- _objc_msgSend$_pauseInput
- _objc_msgSend$_selectBrailleRange:forwardToScreenReader:updateSelectionBegin:selectionEnd:
- _objc_msgSend$bits
- _objc_msgSend$brailleBuffer
- _objc_msgSend$brailleDisplayString
- _objc_msgSend$brailleFocus
- _objc_msgSend$brailleSelection
- _objc_msgSend$brailleString
- _objc_msgSend$brailleSuggestion
- _objc_msgSend$deleteBrailleChar
- _objc_msgSend$deleteBrailleCharSilently
- _objc_msgSend$initWithPendingBraille:modifiers:
- _objc_msgSend$insertBrailleChar:modifiers:silently:
- _objc_msgSend$primaryTableSupportsContractedBraille
- _objc_msgSend$primaryTableSupportsEightDotBraille
- _objc_msgSend$routerMultiplicity
- _objc_msgSend$scriptRangeForBrailleRange:
- _objc_msgSend$selectContiguousBrailleRange:forwardToScreenReader:updateSelectionBegin:selectionEnd:
- _objc_msgSend$selectEntireLineWithForwardToScreenReader:updateSelectionBegin:selectionEnd:
- _objc_msgSend$selectUpToRouterIndex:forwardToScreenReader:updateSelectionBegin:selectionEnd:
- _objc_msgSend$setBrailleSelection:
- _objc_msgSend$setBrailleSelection:needsForwardToScreenReader:newScriptLocation:
- _objc_msgSend$setRouterMultiplicity:
- _objc_msgSend$tokenRanges
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "B32@0:8o^q16o^q24"
+ "B40@0:8Q16o^q24o^q32"
+ "B48@0:8{_NSRange=QQ}16o^q32o^q40"
+ "Nemeth"
+ "TB,N,V_isRouterKey"
+ "TB,R,N,V_isHidingViews"
+ "TQ,N,V_routerClicks"
+ "Tq,N,V_initialSelectionLength"
+ "UEB"
+ "_commitDisplayedBrailleToTopMostView"
+ "_forwardToScreenReader:routerIndex:token:BeginLocation:endLocation:appToken:didPerform:"
+ "_initialSelectionLength"
+ "_isHidingViews"
+ "_isRouterKey"
+ "_requestRefreshBraille"
+ "_routerClicks"
+ "_selectBrailleRange:selectionBegin:selectionEnd:"
+ "_sendAnalytics"
+ "_speakFocusedListItem"
+ "_updateIsHidingViews"
+ "aqui OBrailleDisplay.handleCommandRouterKeyEvent: selectionBegin %d selectionEnd %d"
+ "brailleNotes"
+ "brfFiles"
+ "calculator"
+ "chooseItem"
+ "com.apple.accessibility.braille.access.enabled"
+ "doubleRouterClickTimeout"
+ "firstApp"
+ "hideViews"
+ "initialSelectionLength"
+ "isHidingViews"
+ "isRouterKey"
+ "launchApp"
+ "liveCaptions"
+ "locale"
+ "localeIdentifier"
+ "mathCode"
+ "none"
+ "routerClicks"
+ "selectContiguousBrailleRange:selectionBegin:selectionEnd:"
+ "selectEntireLine:selectionEnd:"
+ "selectUpToRouterIndex:selectionBegin:selectionEnd:"
+ "setInitialSelectionLength:"
+ "setIsRouterKey:"
+ "setRouterClicks:"
+ "shouldReopenViewsWhenRestart"
+ "showViews"
+ "showVisualCount"
+ "v68@0:8@16q24q32q40q48@56B64"
+ "voiceOverTouchBrailleUIShouldReopenViewsWhenRestart"
- "0("
- "B40@0:8o^B16^q24^q32"
- "B48@0:8Q16o^B24^q32^q40"
- "B56@0:8{_NSRange=QQ}16o^B32^q40^q48"
- "CustomBraille"
- "Starting Latin character input in Japanese Braille"
- "Stopping Latin character input in Japanese Braille"
- "TQ,N,V_routerMultiplicity"
- "_forwardToScreenReader:Key:routerIndex:token:BeginLocation:endLocation:appToken:didPerform:"
- "_hasRouterInfo"
- "_routerMultiplicity"
- "_selectBrailleRange:forwardToScreenReader:updateSelectionBegin:selectionEnd:"
- "bits"
- "brailleBuffer"
- "brailleDisplayString"
- "brailleFocus"
- "brailleSelection"
- "brailleString"
- "brailleSuggestion"
- "deleteBrailleChar"
- "deleteBrailleCharSilently"
- "eng-xueb"
- "insertBrailleChar:modifiers:silently:"
- "routerMultiplicity"
- "scriptRangeForBrailleRange:"
- "selectContiguousBrailleRange:forwardToScreenReader:updateSelectionBegin:selectionEnd:"
- "selectEntireLineWithForwardToScreenReader:updateSelectionBegin:selectionEnd:"
- "selectUpToRouterIndex:forwardToScreenReader:updateSelectionBegin:selectionEnd:"
- "setBrailleSelection:"
- "setBrailleSelection:needsForwardToScreenReader:newScriptLocation:"
- "setRouterMultiplicity:"
- "tokenRanges"
- "v72@0:8B16@20q28q36q44q52@60B68"

```
