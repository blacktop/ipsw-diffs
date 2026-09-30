## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-9127.0.75.1.101
-  __TEXT.__text: 0x12d03c
-  __TEXT.__objc_methlist: 0xf7f4
-  __TEXT.__dlopen_cstrs: 0x315
-  __TEXT.__const: 0x3620
+9127.0.79.0.0
+  __TEXT.__text: 0x130278
+  __TEXT.__objc_methlist: 0xfb6c
+  __TEXT.__dlopen_cstrs: 0x406
+  __TEXT.__const: 0x3630
   __TEXT.__swift5_typeref: 0x1964
   __TEXT.__swift5_capture: 0x4f8
-  __TEXT.__cstring: 0xdabf
-  __TEXT.__constg_swiftt: 0x17b8
+  __TEXT.__cstring: 0xdc7c
+  __TEXT.__constg_swiftt: 0x17c0
   __TEXT.__swift5_reflstr: 0xca5
   __TEXT.__swift5_assocty: 0x2f0
   __TEXT.__swift5_fieldmd: 0xcd4
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__oslogstring: 0x5b1f
+  __TEXT.__oslogstring: 0x5cb4
   __TEXT.__swift5_proto: 0x150
   __TEXT.__swift5_types: 0x128
   __TEXT.__swift_as_entry: 0x60

   __TEXT.__swift_as_cont: 0x134
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__ustring: 0x254
-  __TEXT.__unwind_info: 0x40c0
+  __TEXT.__ustring: 0x258
+  __TEXT.__unwind_info: 0x4160
   __TEXT.__eh_frame: 0x1884
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7930
-  __DATA_CONST.__objc_classlist: 0x6e8
+  __DATA_CONST.__const: 0x7a18
+  __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e68
+  __DATA_CONST.__objc_selrefs: 0xa0d0
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x450
-  __DATA_CONST.__objc_arraydata: 0x9b0
-  __DATA_CONST.__got: 0x14b0
-  __AUTH_CONST.__const: 0x2ac8
-  __AUTH_CONST.__cfstring: 0xe560
-  __AUTH_CONST.__objc_const: 0x18d48
-  __AUTH_CONST.__objc_intobj: 0x3c0
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_arraydata: 0xa08
+  __DATA_CONST.__got: 0x14b8
+  __AUTH_CONST.__const: 0x2b68
+  __AUTH_CONST.__cfstring: 0xe700
+  __AUTH_CONST.__objc_const: 0x19260
+  __AUTH_CONST.__objc_intobj: 0x3f0
+  __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH_CONST.__auth_got: 0x1b98
-  __AUTH.__objc_data: 0x3888
+  __AUTH_CONST.__auth_got: 0x1bb0
+  __AUTH.__objc_data: 0x3930
   __AUTH.__data: 0x990
-  __DATA.__objc_ivar: 0x117c
-  __DATA.__data: 0x27e8
-  __DATA.__bss: 0x2d50
+  __DATA.__objc_ivar: 0x11c8
+  __DATA.__data: 0x2848
+  __DATA.__bss: 0x2dc0
   __DATA.__common: 0x288
   __DATA_DIRTY.__objc_data: 0x20c0
   __DATA_DIRTY.__data: 0x2d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6698
-  Symbols:   14750
-  CStrings:  2674
+  Functions: 6781
+  Symbols:   14961
+  CStrings:  2704
 
Symbols:
+ +[TUITestSupport sharedInstance]
+ -[TUIFlickVariantCell initWithFrame:string:annotation:traits:]
+ -[TUIInputSession localizedAppName]
+ -[TUIInputSessionManager localizedNameForHostAuditToken:]
+ -[TUIKeyboardHitDebugOverlay .cxx_destruct]
+ -[TUIKeyboardHitDebugOverlay buildLayers]
+ -[TUIKeyboardHitDebugOverlay chargeToken]
+ -[TUIKeyboardHitDebugOverlay dealloc]
+ -[TUIKeyboardHitDebugOverlay decisionToken]
+ -[TUIKeyboardHitDebugOverlay drawKeyFramesAndCentersFromSource:]
+ -[TUIKeyboardHitDebugOverlay drawTapDecisionFromSource:]
+ -[TUIKeyboardHitDebugOverlay effectiveHitCenterLayer]
+ -[TUIKeyboardHitDebugOverlay effectiveHitCenterOffset]
+ -[TUIKeyboardHitDebugOverlay effectiveHitRadius]
+ -[TUIKeyboardHitDebugOverlay engineOverrodeTappedKey]
+ -[TUIKeyboardHitDebugOverlay geometrySource]
+ -[TUIKeyboardHitDebugOverlay hasEffectiveHitCenter]
+ -[TUIKeyboardHitDebugOverlay hasTapDecision]
+ -[TUIKeyboardHitDebugOverlay hitKeyReason]
+ -[TUIKeyboardHitDebugOverlay initWithFrame:]
+ -[TUIKeyboardHitDebugOverlay isHitTestCorrection]
+ -[TUIKeyboardHitDebugOverlay mostLikelyKeyCode]
+ -[TUIKeyboardHitDebugOverlay mostLikelyKeyLayer]
+ -[TUIKeyboardHitDebugOverlay physicallyTappedKeyCode]
+ -[TUIKeyboardHitDebugOverlay physicallyTappedKeyLayer]
+ -[TUIKeyboardHitDebugOverlay refresh]
+ -[TUIKeyboardHitDebugOverlay setChargeToken:]
+ -[TUIKeyboardHitDebugOverlay setDecisionToken:]
+ -[TUIKeyboardHitDebugOverlay setEffectiveHitCenterLayer:]
+ -[TUIKeyboardHitDebugOverlay setEffectiveHitCenterOffset:]
+ -[TUIKeyboardHitDebugOverlay setEffectiveHitRadius:]
+ -[TUIKeyboardHitDebugOverlay setEngineOverrodeTappedKey:]
+ -[TUIKeyboardHitDebugOverlay setGeometrySource:]
+ -[TUIKeyboardHitDebugOverlay setHasEffectiveHitCenter:]
+ -[TUIKeyboardHitDebugOverlay setHasTapDecision:]
+ -[TUIKeyboardHitDebugOverlay setHitKeyReason:]
+ -[TUIKeyboardHitDebugOverlay setIsHitTestCorrection:]
+ -[TUIKeyboardHitDebugOverlay setMostLikelyKeyCode:]
+ -[TUIKeyboardHitDebugOverlay setMostLikelyKeyLayer:]
+ -[TUIKeyboardHitDebugOverlay setPhysicallyTappedKeyCode:]
+ -[TUIKeyboardHitDebugOverlay setPhysicallyTappedKeyLayer:]
+ -[TUIKeyboardHitDebugOverlay setVisibleKeyFramesLayer:]
+ -[TUIKeyboardHitDebugOverlay startObservingEngineChannels]
+ -[TUIKeyboardHitDebugOverlay stopObservingEngineChannels]
+ -[TUIKeyboardHitDebugOverlay visibleKeyFramesLayer]
+ -[TUIKeyplaneRow _needsFlexibleControlKeyPriorities]
+ -[TUIKeyplaneRow constraintsForCoreKeys:inRowGuide:matchingSizingGuide:splitIndex:]
+ -[TUIKeyplaneView _engineHitFrameForKeyView:]
+ -[TUIKeyplaneView _maximumHandwritingResizeOffset]
+ -[TUIKeyplaneView _updateHitDebugOverlay]
+ -[TUIKeyplaneView debugOverlayBounds]
+ -[TUIKeyplaneView debugOverlayHitFrameForKeyCode:]
+ -[TUIKeyplaneView debugOverlayIsAcceptOnHitKeyForKeyCode:]
+ -[TUIKeyplaneView debugOverlayKeyHitFrames]
+ -[TUIKeyplaneView hitDebugOverlay]
+ -[TUIKeyplaneView setHitDebugOverlay:]
+ -[TUIPasteboardItem linkPresentationThumbnailWithCompletion:]
+ -[TUIPasteboardItem thumbnailFromLinkPresentationData:completion:]
+ -[TUIPasteboardItem webURLFallbackThumbnailImage]
+ -[TUIRecentPasteCandidate initWithPasteboardName:pasteboardChangeCount:contentTitle:thumbnailImage:sourceApp:contentIdentifier:]
+ -[TUIRecentPasteCandidate pasteboardChangeCount]
+ -[TUIRecentPasteCandidate pasteboardName]
+ -[TUIRecentPasteCandidate setPasteboardChangeCount:]
+ -[TUIRecentPasteCandidate setPasteboardName:]
+ -[TUIRecentPasteGenerator quickCheckShouldGenerateCandidateForContext:]
+ -[TUIRecentPasteGenerator responderCanPerformPasteForContext:]
+ -[TUISmartActionGLPSearchCandidate _maskedValueForResult:]
+ -[TUISmartActionGLPSearchCandidate localizedAuthenticationReason]
+ -[TUITestSupport init]
+ -[TUITestSupport setTestApplicationType:]
+ -[TUITestSupport testApplicationType]
+ -[TUIVariantCell attributedKeycapStringForString:]
+ _LinkPresentationLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_TUIKeyboardHitDebugOverlay
+ _OBJC_CLASS_$_TUITestSupport
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._chargeToken
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._decisionToken
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._effectiveHitCenterLayer
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._effectiveHitCenterOffset
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._effectiveHitRadius
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._engineOverrodeTappedKey
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._geometrySource
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._hasEffectiveHitCenter
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._hasTapDecision
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._hitKeyReason
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._isHitTestCorrection
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._mostLikelyKeyCode
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._mostLikelyKeyLayer
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._physicallyTappedKeyCode
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._physicallyTappedKeyLayer
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._visibleKeyFramesLayer
+ _OBJC_IVAR_$_TUIKeyplaneView._hitDebugOverlay
+ _OBJC_IVAR_$_TUIRecentPasteCandidate._pasteboardChangeCount
+ _OBJC_IVAR_$_TUIRecentPasteCandidate._pasteboardName
+ _OBJC_IVAR_$_TUITestSupport._testConversationType
+ _OBJC_METACLASS_$_TUIKeyboardHitDebugOverlay
+ _OBJC_METACLASS_$_TUITestSupport
+ _TIGetShowAllKeysDebugHitAreaValue.onceToken
+ _TIGetSplitHWRKeyboardEnabledValue.onceToken
+ _TUITestSupportLog
+ _TUITestSupportLog.log
+ _TUITestSupportLog.onceToken
+ __OBJC_$_CLASS_METHODS_TUITestSupport
+ __OBJC_$_INSTANCE_METHODS_TUIKeyboardHitDebugOverlay
+ __OBJC_$_INSTANCE_METHODS_TUITestSupport
+ __OBJC_$_INSTANCE_VARIABLES_TUIKeyboardHitDebugOverlay
+ __OBJC_$_INSTANCE_VARIABLES_TUITestSupport
+ __OBJC_$_PROP_LIST_TUIKeyboardHitDebugOverlay
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUIKeyboardHitDebugGeometrySource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUIKeyboardHitDebugGeometrySource
+ __OBJC_$_PROTOCOL_REFS_TUIKeyboardHitDebugGeometrySource
+ __OBJC_CLASS_RO_$_TUIKeyboardHitDebugOverlay
+ __OBJC_CLASS_RO_$_TUITestSupport
+ __OBJC_LABEL_PROTOCOL_$_TUIKeyboardHitDebugGeometrySource
+ __OBJC_METACLASS_RO_$_TUIKeyboardHitDebugOverlay
+ __OBJC_METACLASS_RO_$_TUITestSupport
+ __OBJC_PROTOCOL_$_TUIKeyboardHitDebugGeometrySource
+ ___32+[TUITestSupport sharedInstance]_block_invoke
+ ___49-[TUIPasteboardItem webURLFallbackThumbnailImage]_block_invoke
+ ___58-[TUIKeyboardHitDebugOverlay startObservingEngineChannels]_block_invoke
+ ___58-[TUIKeyboardHitDebugOverlay startObservingEngineChannels]_block_invoke_2
+ ___58-[TUISmartActionGLPSearchCandidate _maskedValueForResult:]_block_invoke
+ ___61-[TUIPasteboardItem linkPresentationThumbnailWithCompletion:]_block_invoke
+ ___66-[TUIPasteboardItem thumbnailFromLinkPresentationData:completion:]_block_invoke
+ ___LinkPresentationLibraryCore_block_invoke
+ ___TIGetShowAllKeysDebugHitAreaValue_block_invoke
+ ___TIGetSplitHWRKeyboardEnabledValue_block_invoke
+ ___TUITestSupportLog_block_invoke
+ ___block_descriptor_40_8_32bs_e45_v24?0"<NSItemProviderReading>"8"NSError"16ls32l8
+ ___block_descriptor_40_8_32s_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8
+ ___block_descriptor_40_8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_8_32s40bs_e17_v16?0"UIImage"8ls40l8s32l8
+ ___getLPLinkMetadataClass_block_invoke
+ ___getSTKGenerativeModelsAvailabilityClass_block_invoke
+ ___swift_closure_destructor.35Tm
+ _audit_stringLinkPresentation
+ _getLPLinkMetadataClass.softClass
+ _getSTKGenerativeModelsAvailabilityClass.softClass
+ _notify_cancel
+ _notify_get_state
+ _notify_register_dispatch
+ _objc_msgSend$_engineHitFrameForKeyView:
+ _objc_msgSend$_maskedValueForResult:
+ _objc_msgSend$_maximumHandwritingResizeOffset
+ _objc_msgSend$_needsFlexibleControlKeyPriorities
+ _objc_msgSend$_updateHitDebugOverlay
+ _objc_msgSend$attributedKeycapStringForString:
+ _objc_msgSend$baseKeyTraits
+ _objc_msgSend$buildLayers
+ _objc_msgSend$canLoadObjectOfClass:
+ _objc_msgSend$chargeToken
+ _objc_msgSend$constraintsForCoreKeys:inRowGuide:matchingSizingGuide:splitIndex:
+ _objc_msgSend$convertPoint:fromCoordinateSpace:
+ _objc_msgSend$cyanColor
+ _objc_msgSend$debugOverlayBounds
+ _objc_msgSend$debugOverlayHitFrameForKeyCode:
+ _objc_msgSend$debugOverlayIsAcceptOnHitKeyForKeyCode:
+ _objc_msgSend$debugOverlayKeyHitFrames
+ _objc_msgSend$decisionToken
+ _objc_msgSend$drawKeyFramesAndCentersFromSource:
+ _objc_msgSend$drawTapDecisionFromSource:
+ _objc_msgSend$effectiveHitCenterLayer
+ _objc_msgSend$effectiveHitCenterOffset
+ _objc_msgSend$effectiveHitRadius
+ _objc_msgSend$engineOverrodeTappedKey
+ _objc_msgSend$enumerateSubstringsInRange:options:usingBlock:
+ _objc_msgSend$geometrySource
+ _objc_msgSend$hasEffectiveHitCenter
+ _objc_msgSend$hasTapDecision
+ _objc_msgSend$hitDebugOverlay
+ _objc_msgSend$hitKeyReason
+ _objc_msgSend$iconProvider
+ _objc_msgSend$imageProvider
+ _objc_msgSend$initWithPasteboardName:pasteboardChangeCount:contentTitle:thumbnailImage:sourceApp:contentIdentifier:
+ _objc_msgSend$isHitTestCorrection
+ _objc_msgSend$linkPresentationThumbnailWithCompletion:
+ _objc_msgSend$loadObjectOfClass:completionHandler:
+ _objc_msgSend$localizedAppName
+ _objc_msgSend$localizedAuthenticationReason
+ _objc_msgSend$localizedNameForHostAuditToken:
+ _objc_msgSend$magentaColor
+ _objc_msgSend$mostLikelyKeyCode
+ _objc_msgSend$mostLikelyKeyLayer
+ _objc_msgSend$orangeColor
+ _objc_msgSend$pasteboardChangeCount
+ _objc_msgSend$pasteboardName
+ _objc_msgSend$physicallyTappedKeyCode
+ _objc_msgSend$physicallyTappedKeyLayer
+ _objc_msgSend$quickCheckShouldGenerateCandidateForContext:
+ _objc_msgSend$reachableKeyboardDefinedWidth
+ _objc_msgSend$redColor
+ _objc_msgSend$refresh
+ _objc_msgSend$responderCanPerformPasteForContext:
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$setChargeToken:
+ _objc_msgSend$setDecisionToken:
+ _objc_msgSend$setEffectiveHitCenterLayer:
+ _objc_msgSend$setEffectiveHitCenterOffset:
+ _objc_msgSend$setEffectiveHitRadius:
+ _objc_msgSend$setEngineOverrodeTappedKey:
+ _objc_msgSend$setGeometrySource:
+ _objc_msgSend$setHasEffectiveHitCenter:
+ _objc_msgSend$setHasTapDecision:
+ _objc_msgSend$setHitDebugOverlay:
+ _objc_msgSend$setHitKeyReason:
+ _objc_msgSend$setIsHitTestCorrection:
+ _objc_msgSend$setLineDashPattern:
+ _objc_msgSend$setMostLikelyKeyCode:
+ _objc_msgSend$setMostLikelyKeyLayer:
+ _objc_msgSend$setOptionCallerName:
+ _objc_msgSend$setPhysicallyTappedKeyCode:
+ _objc_msgSend$setPhysicallyTappedKeyLayer:
+ _objc_msgSend$setVisibleKeyFramesLayer:
+ _objc_msgSend$startObservingEngineChannels
+ _objc_msgSend$stopObservingEngineChannels
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$systemGreenColor
+ _objc_msgSend$systemIndigoColor
+ _objc_msgSend$testApplicationType
+ _objc_msgSend$thumbnailFromLinkPresentationData:completion:
+ _objc_msgSend$visibleKeyFramesLayer
+ _objc_msgSend$webURLFallbackThumbnailImage
+ _objc_msgSend$yellowColor
+ _sharedInstance.instance
+ _webURLFallbackThumbnailImage.fallbackImage
+ _webURLFallbackThumbnailImage.onceToken
- -[TUIKeyplaneRow constraintsForStringKeys:inRowGuide:matchingSizingGuide:splitIndex:]
- -[TUIRecentPasteCandidate initWithPasteboard:contentTitle:thumbnailImage:sourceApp:contentIdentifier:]
- -[TUIRecentPasteGenerator responderCanPerformPaste]
- -[TUISmartActionGLPSearchCandidate searchResults]
- -[TUIVariantCell attributedKeycapStringForString:withSymbolStyle:]
- _OBJC_IVAR_$_TUIRecentPasteCandidate._pasteboard
- _UIFontSystemFontDesignDefault
- ___swift_closure_destructor.34Tm
- _objc_msgSend$attributedKeycapStringForString:withSymbolStyle:
- _objc_msgSend$constraintsForStringKeys:inRowGuide:matchingSizingGuide:splitIndex:
- _objc_msgSend$initWithPasteboard:contentTitle:thumbnailImage:sourceApp:contentIdentifier:
- _objc_msgSend$isChina
- _objc_msgSend$responderCanPerformPaste
- _objc_msgSend$setAdjustsFontForContentSizeCategory:
- _objc_msgSend$usesControlKeyAppearance
CStrings:
+ "4"
+ "Authenticate to Add"
+ "Belarusian"
+ "Dhivehi-QWERTY"
+ "Failed to decode LinkPresentation metadata: %{public}@"
+ "Failed to load LinkPresentation preview image: %{public}@"
+ "Jawi"
+ "Kurdish-Sorani"
+ "LPLinkMetadata"
+ "No session found for versionedPID: %@ (%@); cannot resolve localized name"
+ "Pashto"
+ "Persian"
+ "STKGenerativeModelsAvailability"
+ "Serbian-Cyrillic"
+ "ShowAllKeysDebugHitArea"
+ "Sindhi"
+ "SplitHWRKeyboardEnabled"
+ "TestSupport"
+ "Uzbek-Arabic"
+ "Web URL thumbnail: no preview image; using safari.fill fallback glyph"
+ "Web URL thumbnail: returning rich-link preview image"
+ "canInsertGenmoji"
+ "com.apple.keyboard.debugCharge"
+ "com.apple.keyboard.debugDecision"
+ "com.apple.linkpresentation.metadata"
+ "safari.fill"
+ "setTestApplicationType: called from non-InputUI process — ignoring"
+ "softlink:r:path:/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation"
+ "supportsGenmojiCreation"
+ "testApplicationType = %ld"
+ "v24@?0@\"<NSItemProviderReading>\"8@\"NSError\"16"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
+ "•"
- "AUTOFILL_FROM_APP_NAME"
- "Authenticate to view suggestion"
- "value"
```
