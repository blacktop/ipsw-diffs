## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

```diff

-970.6.0.0.0
-  __TEXT.__text: 0xfff80
+1005.0.0.0.0
+  __TEXT.__text: 0x104e70
   __TEXT.__auth_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xb3f4
-  __TEXT.__const: 0x6ec
-  __TEXT.__cstring: 0xfd39
-  __TEXT.__gcc_except_tab: 0x327c
+  __TEXT.__objc_methlist: 0xba4c
+  __TEXT.__const: 0x73c
+  __TEXT.__cstring: 0xff49
+  __TEXT.__gcc_except_tab: 0x3408
   __TEXT.__ustring: 0x2b4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x3b30
-  __TEXT.__objc_classname: 0x1151
-  __TEXT.__objc_methname: 0x1e765
-  __TEXT.__objc_methtype: 0x84e1
-  __TEXT.__objc_stubs: 0x14340
-  __DATA_CONST.__got: 0x8e0
-  __DATA_CONST.__const: 0x8f10
-  __DATA_CONST.__objc_classlist: 0x450
+  __TEXT.__unwind_info: 0x3c20
+  __TEXT.__objc_classname: 0x1291
+  __TEXT.__objc_methname: 0x1fc06
+  __TEXT.__objc_methtype: 0x86fa
+  __TEXT.__objc_stubs: 0x14a80
+  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__const: 0x9038
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6500
+  __DATA_CONST.__objc_selrefs: 0x6848
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x400
+  __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x12f0
-  __AUTH_CONST.__const: 0x1228
-  __AUTH_CONST.__cfstring: 0xc700
-  __AUTH_CONST.__objc_const: 0x119f0
+  __AUTH_CONST.__const: 0x1268
+  __AUTH_CONST.__cfstring: 0xc900
+  __AUTH_CONST.__objc_const: 0x12758
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1180
-  __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x11fc
-  __DATA.__data: 0xe20
+  __AUTH.__objc_data: 0x1298
+  __AUTH.__data: 0xb0
+  __DATA.__objc_ivar: 0x12e4
+  __DATA.__data: 0xed8
   __DATA.__bss: 0x818
-  __DATA_DIRTY.__objc_data: 0x19a0
-  __DATA_DIRTY.__data: 0xd1
-  __DATA_DIRTY.__bss: 0x9a0
+  __DATA_DIRTY.__objc_data: 0x1a18
+  __DATA_DIRTY.__data: 0xe8
+  __DATA_DIRTY.__bss: 0x9c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AF827AD-7C15-3216-B6AD-9788252CBC9A
-  Functions: 5103
-  Symbols:   17417
-  CStrings:  10346
+  UUID: FD090560-0C1A-32EE-9F20-713C74A4D7E1
+  Functions: 5249
+  Symbols:   17887
+  CStrings:  10590
 
Symbols:
+ +[NSCountableTextLocation initialize]
+ +[NSCountableTextRange initialize]
+ +[NSTextAttachmentViewProvider acceptsViewProviderForContext:]
+ +[NSTextContentManager defaultBaseWritingDirectionResolutionStrategy]
+ +[NSTextContentManager defaultBaseWritingDirectionResolutionStrategy].cold.1
+ +[NSTextLayoutManager _fallbackBaseWritingDirectionForApplicationFrameworkContext:]
+ +[NSTextListElement _validatedMarkerAttributesForAttributes:]
+ +[NSTextPhraseAnimationTimingFunction cubicBezierTimingFunctionWithSamplingFrequency:duration:initialValue:finalValue:point1:point2:]
+ +[UIFontDescriptor _preferredFontDescriptorWithTextStyle:addingSymbolicTraits:compatibleWithTraitCollection:]
+ +[_NSParagraphBidiLevelsProducer resolvedBaseWritingDirectionForTextContentManager:AttributedString:paragraphRange:baseWritingDirection:fallbackBaseWritingDirection:bidiLevels:]
+ -[NSCoreTypesetter _fallbackWritingDirection]
+ -[NSCoreTypesetter _overridingFallbackWritingDirection]
+ -[NSCoreTypesetter _updateBidiLevelsAndBaseWritingDirectionForAttributedString:paragraphRange:]
+ -[NSCoreTypesetter fallbackBaseWritingDirection]
+ -[NSCoreTypesetter resolvesNaturalAlignmentWithBaseWritingDirection]
+ -[NSCoreTypesetter setFallbackBaseWritingDirection:]
+ -[NSCoreTypesetter setResolvesNaturalAlignmentWithBaseWritingDirection:]
+ -[NSMutableParagraphStyle setBaselineInterval:]
+ -[NSMutableParagraphStyle setBaselineIntervalType:]
+ -[NSParagraphStyle baselineIntervalType]
+ -[NSParagraphStyle baselineInterval]
+ -[NSStringDrawingContext fallbackBaseWritingDirection]
+ -[NSStringDrawingContext setFallbackBaseWritingDirection:]
+ -[NSTextContainer setExclusionPaths:temporarily:]
+ -[NSTextContainer(UIFoundation_UIKitAdditions) _appendTemporaryExclusionPathsForRects_iOS:]
+ -[NSTextContentManager _hasAnchoredTextAttachments]
+ -[NSTextContentManager baseWritingDirectionResolutionStrategy]
+ -[NSTextContentManager supportsAnchoredTextAttachments]
+ -[NSTextContentStorage _hasAnchoredTextAttachments]
+ -[NSTextContentStorage baseWritingDirectionResolutionStrategy]
+ -[NSTextContentStorage setBaseWritingDirectionResolutionStrategy:]
+ -[NSTextContentStorage setSupportsAnchoredTextAttachments:]
+ -[NSTextContentStorage set_hasAnchoredTextAttachments:]
+ -[NSTextContentStorage supportsAnchoredTextAttachments]
+ -[NSTextLayoutFragment _bidiLevelsAndResolvedBaseWritingDirectionPointer:]
+ -[NSTextLayoutFragment _boundingRectForAnchoredAttachments]
+ -[NSTextLayoutFragment _configureForTextAnimationContext:]
+ -[NSTextLayoutFragment _notifyTextLayoutManagerAboutTextAttachmentInvalidation]
+ -[NSTextLayoutFragment coreTypesetter:baseWritingDirectionForRange:bidiLevelsPointer:]
+ -[NSTextLayoutFragment set_boundingRectForAnchoredAttachments:]
+ -[NSTextLayoutFragment(NSTextLayoutFragment_OldAPI) anchoredTextAttachments]
+ -[NSTextLayoutFragment(NSTextLayoutFragment_OldAPI) boundsForTextParagraphAnchoredAttachment:]
+ -[NSTextLayoutFragment(NSTextLayoutFragment_OldAPI) drawTextParagraphAnchoredAttachment:bounds:context:]
+ -[NSTextLayoutFragment(NSTextLayoutFragment_OldAPI) textAttachmentViewProviderForTextParagraphAnchoredAttachment:]
+ -[NSTextLayoutManager _hasTextAnimationContextsSnapshotting]
+ -[NSTextLayoutManager canSendViewProviderInvalidationNotification]
+ -[NSTextLayoutManager fallbackBaseWritingDirection]
+ -[NSTextLayoutManager resolvesNaturalAlignmentWithBaseWritingDirection]
+ -[NSTextLayoutManager setFallbackBaseWritingDirection:]
+ -[NSTextLayoutManager setResolvesNaturalAlignmentWithBaseWritingDirection:]
+ -[NSTextLayoutManager set_hasTextAnimationContextsSnapshotting:]
+ -[NSTextLayoutManager willInvalidateTextAttachmentViewProvider:forTextAttachment:]
+ -[NSTextParagraph _bidiLevelsForFallbackWritingDirection:resolvedBaseWritingDirectionPointer:]
+ -[NSTextParagraph anchoredTextAttachments]
+ -[NSTextParagraphAnchoredAttachment .cxx_destruct]
+ -[NSTextParagraphAnchoredAttachment _updateLayoutFrame:]
+ -[NSTextParagraphAnchoredAttachment excludesText]
+ -[NSTextParagraphAnchoredAttachment frame]
+ -[NSTextParagraphAnchoredAttachment initWithTextAttachment:position:]
+ -[NSTextParagraphAnchoredAttachment position]
+ -[NSTextParagraphAnchoredAttachment setExcludesText:]
+ -[NSTextParagraphAnchoredAttachment setFrame:]
+ -[NSTextParagraphAnchoredAttachment setPosition:]
+ -[NSTextParagraphAnchoredAttachment setTextAttachment:]
+ -[NSTextParagraphAnchoredAttachment setVerticalPosition:]
+ -[NSTextParagraphAnchoredAttachment textAttachment]
+ -[NSTextParagraphAnchoredAttachment verticalPosition]
+ -[NSTextPhraseAnimationController .cxx_destruct]
+ -[NSTextPhraseAnimationController _drawCurrentFrame:]
+ -[NSTextPhraseAnimationController _initWithAttributedStringPhrases:animationType:completionHandler:]
+ -[NSTextPhraseAnimationController animatingAttributedStringPhrases]
+ -[NSTextPhraseAnimationController animationDisplayLink]
+ -[NSTextPhraseAnimationController animationState]
+ -[NSTextPhraseAnimationController attributesProvider]
+ -[NSTextPhraseAnimationController completionHandler]
+ -[NSTextPhraseAnimationController defaultAttributes]
+ -[NSTextPhraseAnimationController drawCurrentFrame]
+ -[NSTextPhraseAnimationController frameRate]
+ -[NSTextPhraseAnimationController frameRequestCount]
+ -[NSTextPhraseAnimationController initWithAttributedStringPhrases:animationType:completionHandler:]
+ -[NSTextPhraseAnimationController initWithDefaultPhrase:animatedPhrases:animationType:defaultAttributes:]
+ -[NSTextPhraseAnimationController initWithStringPhrases:animationType:defaultAttributes:completionHandler:]
+ -[NSTextPhraseAnimationController invalidate]
+ -[NSTextPhraseAnimationController lastFrameTime]
+ -[NSTextPhraseAnimationController renderNextFrameUsingHandler:]
+ -[NSTextPhraseAnimationController setAnimationDisplayLink:]
+ -[NSTextPhraseAnimationController setAnimationState:]
+ -[NSTextPhraseAnimationController setAttributesProvider:]
+ -[NSTextPhraseAnimationController setCompletionHandler:]
+ -[NSTextPhraseAnimationController setDefaultAttributes:]
+ -[NSTextPhraseAnimationController setFrameRequestCount:]
+ -[NSTextPhraseAnimationController setLastFrameTime:]
+ -[NSTextPhraseAnimationController setStartTime:]
+ -[NSTextPhraseAnimationController startTime]
+ -[NSTextPhraseAnimationController start]
+ -[NSTextPhraseAnimationController version]
+ -[NSTextPhraseAnimationTimingFunction .cxx_destruct]
+ -[NSTextPhraseAnimationTimingFunction calcTimingFunction]
+ -[NSTextPhraseAnimationTimingFunction duration]
+ -[NSTextPhraseAnimationTimingFunction finalValue]
+ -[NSTextPhraseAnimationTimingFunction frequency]
+ -[NSTextPhraseAnimationTimingFunction initWithSamplingFrequency:duration:initialValue:finalValue:]
+ -[NSTextPhraseAnimationTimingFunction initialValue]
+ -[NSTextPhraseAnimationTimingFunction populateValues]
+ -[NSTextPhraseAnimationTimingFunction sampleAtIndex:]
+ -[NSTextPhraseAnimationTimingFunction sampledValues]
+ -[NSTextPhraseAnimationTimingFunction setCalcTimingFunction:]
+ -[NSTextPhraseAnimationTimingFunction setDuration:]
+ -[NSTextPhraseAnimationTimingFunction setFinalValue:]
+ -[NSTextPhraseAnimationTimingFunction setFrequency:]
+ -[NSTextPhraseAnimationTimingFunction setInitialValue:]
+ -[NSTextPhraseAnimationTimingFunction setSampledValues:]
+ -[NSTextPhraseAttributesProvider_RippleFade .cxx_destruct]
+ -[NSTextPhraseAttributesProvider_RippleFade animationElapsedTimeIndex]
+ -[NSTextPhraseAttributesProvider_RippleFade attributedStringForPhraseIndex:atPhraseTimeIndex:]
+ -[NSTextPhraseAttributesProvider_RippleFade cycleCount]
+ -[NSTextPhraseAttributesProvider_RippleFade cycleTimeIndex]
+ -[NSTextPhraseAttributesProvider_RippleFade generateDelayValues]
+ -[NSTextPhraseAttributesProvider_RippleFade generateFactorArrayValues]
+ -[NSTextPhraseAttributesProvider_RippleFade initWithController:]
+ -[NSTextPhraseAttributesProvider_RippleFade invalidate]
+ -[NSTextPhraseAttributesProvider_RippleFade isSecondaryPhraseAvailable]
+ -[NSTextPhraseAttributesProvider_RippleFade opacityFactorForGlyphIndex:phraseIndex:atTimeIndex:]
+ -[NSTextPhraseAttributesProvider_RippleFade phraseCount]
+ -[NSTextPhraseAttributesProvider_RippleFade primaryPhraseIndex]
+ -[NSTextPhraseAttributesProvider_RippleFade renderFrameForTime:usingHandler:]
+ -[NSTextPhraseAttributesProvider_RippleFade scaleFactorForGlyphIndex:phraseIndex:atTimeIndex:]
+ -[NSTextPhraseAttributesProvider_RippleFade secondaryPhraseIndex]
+ -[NSTextPhraseAttributesProvider_RippleFade startAtTime:]
+ -[NSTextPhraseAttributesProvider_RippleFade totalElapsedTimeIndex]
+ -[NSTextPhraseAttributesProvider_RippleFade totalElapsedTime]
+ -[_NSTextAttachmentLayoutContext .cxx_destruct]
+ -[_NSTextAttachmentLayoutContext notifyTextLayoutManagerAboutTextAttachmentInvalidation]
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table210
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table226
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table248
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table68
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table94
+ GCC_except_table97
+ _CFAbsoluteTimeGetCurrent
+ _CFAttributedStringGetStatisticalWritingDirections
+ _CGRectIntersectsRect
+ _CTEnumerateKnownUrduSequencesInString
+ _CTFontCreateCopyForKnownUrduSequences
+ _CTIsLanguageIdentifierSuitableForKnownUrduSequences
+ _NSParagraphAttachmentAttributeName
+ _NSTextParagraphAnchoredAttachmentAttributeName
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_NSTextParagraphAnchoredAttachment
+ _OBJC_CLASS_$_NSTextPhraseAnimationController
+ _OBJC_CLASS_$_NSTextPhraseAnimationTimingFunction
+ _OBJC_CLASS_$_NSTextPhraseAttributesProvider_RippleFade
+ _OBJC_CLASS_$__NSParagraphBidiLevelsProducer
+ _OBJC_IVAR_$_NSCoreTypesetter._bidiLevels
+ _OBJC_IVAR_$_NSCoreTypesetter._delegateSupportsBidi
+ _OBJC_IVAR_$_NSCoreTypesetter._delegateSupportsTruncationToken
+ _OBJC_IVAR_$_NSCoreTypesetter._fallbackBaseWritingDirection
+ _OBJC_IVAR_$_NSCoreTypesetter._resolvedBaseWritingDirection
+ _OBJC_IVAR_$_NSCoreTypesetter._resolvesNaturalAlignmentWithBaseWritingDirection
+ _OBJC_IVAR_$_NSParagraphStyleExtraData._baselineInterval
+ _OBJC_IVAR_$_NSParagraphStyleExtraData._baselineIntervalType
+ _OBJC_IVAR_$_NSStringDrawingContext._fallbackBaseWritingDirection
+ _OBJC_IVAR_$_NSTextContentStorage.__hasAnchoredTextAttachments
+ _OBJC_IVAR_$_NSTextContentStorage._baseWritingDirectionResolutionStrategy
+ _OBJC_IVAR_$_NSTextContentStorage._supportsAnchoredTextAttachments
+ _OBJC_IVAR_$_NSTextLayoutFragment._anchoredAttacmentViewProviews
+ _OBJC_IVAR_$_NSTextLayoutFragment._boundingRectForAnchoredAttachments
+ _OBJC_IVAR_$_NSTextLayoutFragment._textContainerForAnchoredAttacmentViewProviewCache
+ _OBJC_IVAR_$_NSTextLayoutManager._delegateWithCachedViewProviderForTextAttachment
+ _OBJC_IVAR_$_NSTextLayoutManager._delegateWithViewProviderInvalidationNotification
+ _OBJC_IVAR_$_NSTextLayoutManager._fallbackBaseWritingDirection
+ _OBJC_IVAR_$_NSTextLayoutManager._hasTextAnimationContextsSnapshotting
+ _OBJC_IVAR_$_NSTextLayoutManager._resolvesNaturalAlignmentWithBaseWritingDirection
+ _OBJC_IVAR_$_NSTextLayoutManager._viewProviderCreated
+ _OBJC_IVAR_$_NSTextParagraph._bidiLevels
+ _OBJC_IVAR_$_NSTextParagraphAnchoredAttachment._excludesText
+ _OBJC_IVAR_$_NSTextParagraphAnchoredAttachment._frame
+ _OBJC_IVAR_$_NSTextParagraphAnchoredAttachment._position
+ _OBJC_IVAR_$_NSTextParagraphAnchoredAttachment._textAttachment
+ _OBJC_IVAR_$_NSTextParagraphAnchoredAttachment._verticalPosition
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._animatingAttributedStringPhrases
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._animationDisplayLink
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._animationState
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._attributesProvider
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._completionHandler
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._defaultAttributes
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._frameRequestCount
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._lastFrameTime
+ _OBJC_IVAR_$_NSTextPhraseAnimationController._startTime
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._calcTimingFunction
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._duration
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._finalValue
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._frequency
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._indexCount
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._initialValue
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._populatedSamples
+ _OBJC_IVAR_$_NSTextPhraseAnimationTimingFunction._sampledValues
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._animatingAttributedStringPhrases
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._animationElapsedTimeIndex
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._controller
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._currentTime
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._cycleCount
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._cycleTimeIndex
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._delayArrays
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._opacityFactorArray
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._phraseCount
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._primaryPhraseIndex
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._scaleFactorArray
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._secondaryPhraseIndex
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._startTime
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._totalElapsedTime
+ _OBJC_IVAR_$_NSTextPhraseAttributesProvider_RippleFade._totalElapsedTimeIndex
+ _OBJC_METACLASS_$_NSTextParagraphAnchoredAttachment
+ _OBJC_METACLASS_$_NSTextPhraseAnimationController
+ _OBJC_METACLASS_$_NSTextPhraseAnimationTimingFunction
+ _OBJC_METACLASS_$_NSTextPhraseAttributesProvider_RippleFade
+ _OBJC_METACLASS_$__NSParagraphBidiLevelsProducer
+ _OUTLINED_FUNCTION_75
+ _UIBezierPathFunction
+ __OBJC_$_CLASS_METHODS_NSTextAttachmentViewProvider
+ __OBJC_$_INSTANCE_METHODS_NSTextParagraphAnchoredAttachment
+ __OBJC_$_INSTANCE_METHODS_NSTextPhraseAnimationController
+ __OBJC_$_INSTANCE_METHODS_NSTextPhraseAnimationTimingFunction
+ __OBJC_$_INSTANCE_METHODS_NSTextPhraseAttributesProvider_RippleFade
+ __OBJC_$_INSTANCE_VARIABLES_NSTextParagraphAnchoredAttachment
+ __OBJC_$_INSTANCE_VARIABLES_NSTextPhraseAnimationController
+ __OBJC_$_INSTANCE_VARIABLES_NSTextPhraseAnimationTimingFunction
+ __OBJC_$_INSTANCE_VARIABLES_NSTextPhraseAttributesProvider_RippleFade
+ __OBJC_$_PROP_LIST_NSTextParagraphAnchoredAttachment
+ __OBJC_$_PROP_LIST_NSTextPhraseAnimationController
+ __OBJC_$_PROP_LIST_NSTextPhraseAnimationTimingFunction
+ __OBJC_$_PROP_LIST_NSTextPhraseAttributesProvider_RippleFade
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSTextPhraseAttributesProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSTextPhraseAttributesProvider
+ __OBJC_$_PROTOCOL_REFS_NSTextPhraseAttributesProvider
+ __OBJC_$_PROTOCOL_REFS_NSTextViewportRenderingSurfaceKey
+ __OBJC_CLASS_PROTOCOLS_$_NSTextParagraphAnchoredAttachment
+ __OBJC_CLASS_PROTOCOLS_$_NSTextPhraseAttributesProvider_RippleFade
+ __OBJC_CLASS_RO_$_NSTextParagraphAnchoredAttachment
+ __OBJC_CLASS_RO_$_NSTextPhraseAnimationController
+ __OBJC_CLASS_RO_$_NSTextPhraseAnimationTimingFunction
+ __OBJC_CLASS_RO_$_NSTextPhraseAttributesProvider_RippleFade
+ __OBJC_CLASS_RO_$__NSParagraphBidiLevelsProducer
+ __OBJC_LABEL_PROTOCOL_$_NSTextPhraseAttributesProvider
+ __OBJC_LABEL_PROTOCOL_$_NSTextViewportRenderingSurfaceKey
+ __OBJC_METACLASS_RO_$_NSTextParagraphAnchoredAttachment
+ __OBJC_METACLASS_RO_$_NSTextPhraseAnimationController
+ __OBJC_METACLASS_RO_$_NSTextPhraseAnimationTimingFunction
+ __OBJC_METACLASS_RO_$_NSTextPhraseAttributesProvider_RippleFade
+ __OBJC_METACLASS_RO_$__NSParagraphBidiLevelsProducer
+ __OBJC_PROTOCOL_$_NSTextPhraseAttributesProvider
+ __OBJC_PROTOCOL_$_NSTextViewportRenderingSurfaceKey
+ ___105-[NSTextPhraseAnimationController initWithDefaultPhrase:animatedPhrases:animationType:defaultAttributes:]_block_invoke
+ ___107-[NSTextPhraseAnimationController initWithStringPhrases:animationType:defaultAttributes:completionHandler:]_block_invoke
+ ___133+[NSTextPhraseAnimationTimingFunction cubicBezierTimingFunctionWithSamplingFrequency:duration:initialValue:finalValue:point1:point2:]_block_invoke
+ ___31-[NSTextLayoutFragment _layout]_block_invoke_5
+ ___31-[NSTextLayoutFragment _layout]_block_invoke_6
+ ___42-[NSTextParagraph anchoredTextAttachments]_block_invoke
+ ___53-[NSTextPhraseAnimationController _drawCurrentFrame:]_block_invoke
+ ___64-[NSTextPhraseAttributesProvider_RippleFade generateDelayValues]_block_invoke
+ ___69+[NSTextContentManager defaultBaseWritingDirectionResolutionStrategy]_block_invoke
+ ___88-[_NSTextAttachmentLayoutContext notifyTextLayoutManagerAboutTextAttachmentInvalidation]_block_invoke
+ ___98-[NSTextContentStorage processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:]_block_invoke_2
+ ___NSCountableTextLocationClass
+ ___NSCountableTextLocationTable
+ ___NSCountableTextRangeClass
+ ___NSCountableTextRangeTable
+ ___NSJustifyLine
+ ___NSStringDrawingEngine.onceToken.359
+ ___NSTextContentStorageGetRangeForIndexRange
+ ___NSTextHighlightShapeProviderHasTypingAttributesOverride
+ _____NSCoreTypesetterCreateBaseLineFromAttributedString_block_invoke_2
+ _____NSStringDrawingEngine_block_invoke.376
+ _____NSStringDrawingEngine_block_invoke_2.377
+ _____NSTextLayoutManagerRemoveTextLayoutFragmentsInTextRange_block_invoke_3
+ ___block_descriptor_102_e8_32o40o48b56r64r72r_e34_v24?0"NSTextLayoutFragment"8^B16ls32l8s40l8s48l8r56l8r64l8r72l8
+ ___block_descriptor_224_e8_32o40o48o56b64r72r80r_e55_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8"NSTextRange"40ls32l8s40l8r64l8r72l8s56l8r80l8s48l8
+ ___block_descriptor_40_e8_32o_e45_v32?0"NSTextAttachmentViewProvider"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e88_v64?0q8"NSAttributedString"16"NSAttributedString"24{CGRect={CGPoint=dd}{CGSize=dd}}32ls32l8
+ ___block_descriptor_48_e18_r*32?0{?=qq}8^c24l
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSAttributedString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e78_B64?0"NSTextRange"8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"NSTextContainer"56ls32l8s40l8
+ ___block_descriptor_56_e8_32o40r48r_e24_v32?0"NSValue"8Q16^B24lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_d16?0d8l
+ ___block_descriptor_65_e8_32s40s48bs56r_e78_B64?0"NSTextRange"8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"NSTextContainer"56ls32l8s40l8s48l8r56l8
+ ___block_descriptor_73_e8_32o40r48r56r_e30_B16?0"NSTextLayoutFragment"8ls32l8r40l8r48l8r56l8
+ ___block_literal_global.139
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.161
+ ___block_literal_global.169
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.191
+ ___block_literal_global.194
+ ___block_literal_global.213
+ ___block_literal_global.217
+ ___block_literal_global.218
+ ___block_literal_global.231
+ ___block_literal_global.234
+ ___block_literal_global.299
+ ___block_literal_global.337
+ ___block_literal_global.342
+ ___block_literal_global.350
+ ___block_literal_global.353
+ ___block_literal_global.361
+ ___block_literal_global.380
+ ___block_literal_global.462
+ ___block_literal_global.472
+ ___block_literal_global.57
+ ___block_literal_global.609
+ ___block_literal_global.611
+ ___block_literal_global.76
+ _classUIBezierPath
+ _defaultBaseWritingDirectionResolutionStrategy.defaultStrategy
+ _defaultBaseWritingDirectionResolutionStrategy.onceToken
+ _getUIBezierPathClass
+ _initUIBezierPath
+ _initUIBezierPath.cold.1
+ _kCTTypesetterOptionBidiLevelsProvider
+ _objc_msgSend$_bidiLevelsAndResolvedBaseWritingDirectionPointer:
+ _objc_msgSend$_bidiLevelsForFallbackWritingDirection:resolvedBaseWritingDirectionPointer:
+ _objc_msgSend$_configureForTextAnimationContext:
+ _objc_msgSend$_drawCurrentFrame:
+ _objc_msgSend$_fallbackBaseWritingDirectionForApplicationFrameworkContext:
+ _objc_msgSend$_hasAnchoredTextAttachments
+ _objc_msgSend$_hasTextAnimationContextsSnapshotting
+ _objc_msgSend$_initWithAttributedStringPhrases:animationType:completionHandler:
+ _objc_msgSend$_notifyTextLayoutManagerAboutTextAttachmentInvalidation
+ _objc_msgSend$_updateBidiLevelsAndBaseWritingDirectionForAttributedString:paragraphRange:
+ _objc_msgSend$_updateLayoutFrame:
+ _objc_msgSend$_validatedMarkerAttributesForAttributes:
+ _objc_msgSend$acceptsViewProviderForContext:
+ _objc_msgSend$anchoredTextAttachments
+ _objc_msgSend$animatingAttributedStringPhrases
+ _objc_msgSend$animationElapsedTimeIndex
+ _objc_msgSend$animationState
+ _objc_msgSend$attributedStringForPhraseIndex:atPhraseTimeIndex:
+ _objc_msgSend$baseWritingDirectionResolutionStrategy
+ _objc_msgSend$baselineInterval
+ _objc_msgSend$baselineIntervalType
+ _objc_msgSend$bezierPathWithRect:
+ _objc_msgSend$canSendViewProviderInvalidationNotification
+ _objc_msgSend$coreTypesetter:baseWritingDirectionForRange:bidiLevelsPointer:
+ _objc_msgSend$cycleCount
+ _objc_msgSend$cycleTimeIndex
+ _objc_msgSend$defaultBaseWritingDirectionResolutionStrategy
+ _objc_msgSend$displayLinkWithTarget:selector:
+ _objc_msgSend$excludesText
+ _objc_msgSend$fallbackBaseWritingDirection
+ _objc_msgSend$generateDelayValues
+ _objc_msgSend$generateFactorArrayValues
+ _objc_msgSend$initWithController:
+ _objc_msgSend$initWithSamplingFrequency:duration:initialValue:finalValue:
+ _objc_msgSend$isSecondaryPhraseAvailable
+ _objc_msgSend$notifyTextLayoutManagerAboutTextAttachmentInvalidation
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$opacityFactorForGlyphIndex:phraseIndex:atTimeIndex:
+ _objc_msgSend$phraseCount
+ _objc_msgSend$populateValues
+ _objc_msgSend$position
+ _objc_msgSend$primaryPhraseIndex
+ _objc_msgSend$renderFrameForTime:usingHandler:
+ _objc_msgSend$secondaryPhraseIndex
+ _objc_msgSend$setCalcTimingFunction:
+ _objc_msgSend$setExclusionPaths:temporarily:
+ _objc_msgSend$setFallbackBaseWritingDirection:
+ _objc_msgSend$setResolvesNaturalAlignmentWithBaseWritingDirection:
+ _objc_msgSend$set_hasTextAnimationContextsSnapshotting:
+ _objc_msgSend$startAtTime:
+ _objc_msgSend$textAttachmentViewProviderForTextParagraphAnchoredAttachment:
+ _objc_msgSend$textLayoutManager:cachedTextAttachmentViewProviderForTextAttachment:
+ _objc_msgSend$textLayoutManager:willInvalidateTextAttachmentViewProvider:forTextAttachment:
+ _objc_msgSend$textViewportLayoutController:cacheRenderingSurface:forCacheableObjectsInKey:
+ _objc_msgSend$textViewportLayoutController:cachedRenderingSurfaceForCacheableObjectsInKey:
+ _objc_msgSend$totalElapsedTime
+ _objc_msgSend$totalElapsedTimeIndex
+ _objc_msgSend$weakObjectsHashTable
+ _objc_msgSend$willInvalidateTextAttachmentViewProvider:forTextAttachment:
- +[NSEmojiImageTextAttachment _isEmojiImageTextAttachmentData:UTI:]
- -[NSATSLineFragment _invalidate]
- -[NSATSTypesetter endParagraph].cold.1
- -[NSStringDrawingContext actualTrackingAdjustment]
- -[NSStringDrawingContext setActualTrackingAdjustment:]
- GCC_except_table135
- GCC_except_table146
- GCC_except_table15
- GCC_except_table152
- GCC_except_table167
- GCC_except_table170
- GCC_except_table172
- GCC_except_table174
- GCC_except_table176
- GCC_except_table189
- GCC_except_table193
- GCC_except_table200
- GCC_except_table202
- GCC_except_table209
- GCC_except_table212
- GCC_except_table216
- GCC_except_table225
- GCC_except_table236
- GCC_except_table237
- GCC_except_table238
- GCC_except_table245
- GCC_except_table251
- GCC_except_table252
- GCC_except_table253
- GCC_except_table38
- GCC_except_table42
- GCC_except_table50
- GCC_except_table77
- GCC_except_table93
- _CGImageRelease
- _CGImageSourceCopyPropertiesAtIndex
- _CGImageSourceCreateImageAtIndex
- _CGImageSourceCreateWithData
- _CGImageSourceGetCount
- _ISEnumerateKnownUrduSequencesInString
- _NSEmojiImagePropertyKeyOrigin
- _NSEmojiImageSourceCopyImageStrikes
- _NSEmojiImageSourceCreateWithData
- _NSEmojiImageSourceGetImageIndex
- _OBJC_IVAR_$_NSCoreTypesetter._delegatesSupportsTruncationToken
- ___GetNextUrduSequenceFromString_block_invoke_2
- ___NSStringDrawingEngine.onceToken.357
- ___NSTextContentStorageUpdateCachedRange
- _____NSStringDrawingEngine_block_invoke.374
- _____NSStringDrawingEngine_block_invoke_2.375
- ___block_descriptor_224_e8_32o40o48o56b64r72r80r_e55_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8"NSTextRange"40ls32l8r64l8r72l8s56l8s40l8r80l8s48l8
- ___block_descriptor_40_e8_32s_e78_B64?0"NSTextRange"8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"NSTextContainer"56ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e78_B64?0"NSTextRange"8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"NSTextContainer"56ls32l8s40l8r48l8
- ___block_descriptor_57_e8_32o40r48r_e30_B16?0"NSTextLayoutFragment"8lr40l8s32l8r48l8
- ___block_descriptor_94_e8_32o40o48b56r64r_e34_v24?0"NSTextLayoutFragment"8^B16ls32l8s40l8s48l8r56l8r64l8
- ___block_literal_global.132
- ___block_literal_global.143
- ___block_literal_global.145
- ___block_literal_global.15
- ___block_literal_global.159
- ___block_literal_global.162
- ___block_literal_global.164
- ___block_literal_global.170
- ___block_literal_global.183
- ___block_literal_global.186
- ___block_literal_global.195
- ___block_literal_global.205
- ___block_literal_global.210
- ___block_literal_global.223
- ___block_literal_global.271
- ___block_literal_global.319
- ___block_literal_global.335
- ___block_literal_global.348
- ___block_literal_global.359
- ___block_literal_global.378
- ___block_literal_global.447
- ___block_literal_global.457
- ___block_literal_global.54
- ___block_literal_global.579
- ___block_literal_global.66
- ___block_literal_global.73
- _kCGImagePropertyPixelHeight
- _kCGImagePropertyPixelWidth
- _kCGImagePropertyTIFFDictionary
- _kCGImagePropertyTIFFDocumentName
- _kCGImagePropertyTIFFImageDescription
- _kCGImagePropertyTIFFXPosition
- _kCGImagePropertyTIFFYPosition
- _objc_msgSend$_deviceLanguage
- _objc_msgSend$initWithImage:alignmentInset:
CStrings:
+ "\n]"
+ "%.2f "
+ "%lu "
+ ", BaselineInterval %@ %g"
+ ": ["
+ "@\"<NSTextPhraseAttributesProvider>\""
+ "@\"CADisplayLink\""
+ "@\"NSTextPhraseAnimationController\""
+ "@24@0:8@\"NSTextPhraseAnimationController\"16"
+ "@32@0:8Q16q24"
+ "@36@0:8@16I24@28"
+ "@48@0:8@16q24@32@?40"
+ "@48@0:8Q16d24d32d40"
+ "Alignment %@%@, LineSpacing %g, ParagraphSpacing %g, ParagraphSpacingBefore %g, HeadIndent %g, TailIndent %g, FirstLineHeadIndent %g, LineHeight %g/%g, LineHeightMultiple %g%@ LineBreakMode %@%@, Tabs %@, DefaultTabInterval %g, Blocks %@, Lists %@, BaseWritingDirection %@, HyphenationFactor %g, TighteningForTruncation %@, HeaderLevel %ld LineBreakStrategy %lu%@ PresentationIntents %@ ListIntentOrdinal %ld CodeBlockIntentLanguageHint '%@'"
+ "B24@0:8^{CGContext=}16"
+ "Exact"
+ "LanguageAwareString"
+ "Leading"
+ "Multiple"
+ "NS.resolvesNaturalAlignmentWithBaseWritingDirection"
+ "NSBaselineInterval"
+ "NSBaselineIntervalType"
+ "NSTextListIncludesMarkerStrings"
+ "NSTextParagraphAnchoredAttachment"
+ "NSTextPhraseAnimationController"
+ "NSTextPhraseAnimationTimingFunction"
+ "NSTextPhraseAttributesProvider"
+ "NSTextPhraseAttributesProvider_RippleFade"
+ "NSTextViewportRenderingSurfaceKey"
+ "T@\"<NSTextPhraseAttributesProvider>\",&,V_attributesProvider"
+ "T@\"CADisplayLink\",&,V_animationDisplayLink"
+ "T@\"NSArray\",R,C,V_animatingAttributedStringPhrases"
+ "T@\"NSDictionary\",C,V_defaultAttributes"
+ "T@\"NSMutableArray\",&,N,V_sampledValues"
+ "T@\"NSTextAttachment\",&,V_textAttachment"
+ "T@?,C,N,V_calcTimingFunction"
+ "TB,V__hasAnchoredTextAttachments"
+ "TB,V_excludesText"
+ "TB,V_hasTextAnimationContextsSnapshotting"
+ "TB,V_resolvesNaturalAlignmentWithBaseWritingDirection"
+ "TB,V_supportsAnchoredTextAttachments"
+ "TPT_RF: "
+ "TPT_RF: _opacityFactorArray: ["
+ "TPT_RF: phrase%02d cycleIndex:%03d "
+ "TQ,N,V_frequency"
+ "TQ,V_baseWritingDirectionResolutionStrategy"
+ "TQ,V_frameRequestCount"
+ "TQ,V_position"
+ "TQ,V_verticalPosition"
+ "Td,N,V_duration"
+ "Td,N,V_finalValue"
+ "Td,N,V_initialValue"
+ "Td,V_lastFrameTime"
+ "Td,V_startTime"
+ "Tq,V_animationState"
+ "Tq,V_fallbackBaseWritingDirection"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},V_boundingRectForAnchoredAttachments"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},V_frame"
+ "UIBezierPath"
+ "UIFoundation"
+ "[255d]"
+ "]"
+ "]\n"
+ "_NSParagraphBidiLevelsProducer"
+ "_NSTextBaseWritingDirectionResolutionStrategyStatistical"
+ "__hasAnchoredTextAttachments"
+ "_anchoredAttacmentViewProviews"
+ "_animatingAttributedStringPhrases"
+ "_animationDisplayLink"
+ "_animationElapsedTimeIndex"
+ "_animationState"
+ "_appendTemporaryExclusionPathsForRects_iOS:"
+ "_appendTemporaryExclusionPathsForRects_macOS:"
+ "_attributesProvider"
+ "_baseWritingDirectionResolutionStrategy"
+ "_baselineInterval"
+ "_baselineIntervalType"
+ "_bidiLevelsAndResolvedBaseWritingDirectionPointer:"
+ "_bidiLevelsForFallbackWritingDirection:resolvedBaseWritingDirectionPointer:"
+ "_boundingRectForAnchoredAttachments"
+ "_calcTimingFunction"
+ "_configureForTextAnimationContext:"
+ "_controller"
+ "_currentTime"
+ "_cycleCount"
+ "_cycleTimeIndex"
+ "_defaultAttributes"
+ "_delayArrays"
+ "_delegateSupportsBidi"
+ "_delegateSupportsTruncationToken"
+ "_delegateWithCachedViewProviderForTextAttachment"
+ "_delegateWithViewProviderInvalidationNotification"
+ "_drawCurrentFrame:"
+ "_excludesText"
+ "_fallbackBaseWritingDirection"
+ "_fallbackBaseWritingDirectionForApplicationFrameworkContext:"
+ "_finalValue"
+ "_frame"
+ "_frameRequestCount"
+ "_frequency"
+ "_hasAnchoredTextAttachments"
+ "_hasTextAnimationContextsSnapshotting"
+ "_indexCount"
+ "_initWithAttributedStringPhrases:animationType:completionHandler:"
+ "_initialValue"
+ "_lastFrameTime"
+ "_notifyTextLayoutManagerAboutTextAttachmentInvalidation"
+ "_opacityFactorArray"
+ "_overridingFallbackWritingDirection"
+ "_phraseCount"
+ "_populatedSamples"
+ "_position"
+ "_preferredFontDescriptorWithTextStyle:addingSymbolicTraits:compatibleWithTraitCollection:"
+ "_primaryPhraseIndex"
+ "_resolvedBaseWritingDirection"
+ "_resolvesNaturalAlignmentWithBaseWritingDirection"
+ "_sampledValues"
+ "_scaleFactorArray"
+ "_secondaryPhraseIndex"
+ "_startTime"
+ "_supportsAnchoredTextAttachments"
+ "_textContainerForAnchoredAttacmentViewProviewCache"
+ "_totalElapsedTime"
+ "_totalElapsedTimeIndex"
+ "_updateBidiLevelsAndBaseWritingDirectionForAttributedString:paragraphRange:"
+ "_updateLayoutFrame:"
+ "_validatedMarkerAttributesForAttributes:"
+ "_verticalPosition"
+ "_viewProviderCreated"
+ "acceptsViewProviderForContext:"
+ "anchoredTextAttachments"
+ "animatingAttributedStringPhrases"
+ "animationDisplayLink"
+ "animationElapsedTimeIndex"
+ "animationState"
+ "attributedStringForPhraseIndex:atPhraseTimeIndex:"
+ "attributesProvider"
+ "baseWritingDirectionResolutionStrategy"
+ "baselineInterval"
+ "baselineIntervalType"
+ "bezierPathWithRect:"
+ "boundsForTextParagraphAnchoredAttachment:"
+ "calcTimingFunction"
+ "canSendViewProviderInvalidationNotification"
+ "classUIBezierPath"
+ "coreTypesetter:baseWritingDirectionForRange:bidiLevelsPointer:"
+ "cycleCount"
+ "cycleTimeIndex"
+ "d16@?0d8"
+ "d40@0:8q16q24q32"
+ "defaultAttributes"
+ "defaultBaseWritingDirectionResolutionStrategy"
+ "displayLinkWithTarget:selector:"
+ "drawCurrentFrame"
+ "drawTextParagraphAnchoredAttachment:bounds:context:"
+ "excludesText"
+ "fallbackBaseWritingDirection"
+ "finalValue"
+ "frameRate"
+ "frameRequestCount"
+ "frequency"
+ "generateDelayValues"
+ "generateFactorArrayValues"
+ "initUIBezierPath"
+ "initWithAttributedStringPhrases:animationType:completionHandler:"
+ "initWithController:"
+ "initWithDefaultPhrase:animatedPhrases:animationType:defaultAttributes:"
+ "initWithSamplingFrequency:duration:initialValue:finalValue:"
+ "initWithStringPhrases:animationType:defaultAttributes:completionHandler:"
+ "initWithTextAttachment:position:"
+ "initialValue"
+ "isSecondaryPhraseAvailable"
+ "lastFrameTime"
+ "notifyTextLayoutManagerAboutTextAttachmentInvalidation"
+ "numberWithFloat:"
+ "numberWithInt:"
+ "opacity: ["
+ "opacityFactorForGlyphIndex:phraseIndex:atTimeIndex:"
+ "phraseCount"
+ "populateValues"
+ "position"
+ "primaryPhraseIndex"
+ "q48@0:8@\"NSCoreTypesetter\"16{_NSRange=QQ}24or^*40"
+ "q48@0:8@16{_NSRange=QQ}24or^*40"
+ "r*"
+ "r*24@0:8o^q16"
+ "r*32@0:8q16o^q24"
+ "r*32@?0{?=qq}8^c24"
+ "renderFrameForTime:usingHandler:"
+ "renderNextFrameUsingHandler:"
+ "resolvesNaturalAlignmentWithBaseWritingDirection"
+ "sampledValues"
+ "scale: ["
+ "scaleFactorForGlyphIndex:phraseIndex:atTimeIndex:"
+ "secondaryPhraseIndex"
+ "setAnimationDisplayLink:"
+ "setAnimationState:"
+ "setAttributesProvider:"
+ "setBaseWritingDirectionResolutionStrategy:"
+ "setBaselineInterval:"
+ "setBaselineIntervalType:"
+ "setCalcTimingFunction:"
+ "setDefaultAttributes:"
+ "setDuration:"
+ "setExcludesText:"
+ "setExclusionPaths:temporarily:"
+ "setFallbackBaseWritingDirection:"
+ "setFinalValue:"
+ "setFrameRequestCount:"
+ "setFrequency:"
+ "setInitialValue:"
+ "setLastFrameTime:"
+ "setPosition:"
+ "setResolvesNaturalAlignmentWithBaseWritingDirection:"
+ "setSampledValues:"
+ "setStartTime:"
+ "setSupportsAnchoredTextAttachments:"
+ "setVerticalPosition:"
+ "set_boundingRectForAnchoredAttachments:"
+ "set_hasAnchoredTextAttachments:"
+ "set_hasTextAnimationContextsSnapshotting:"
+ "startAtTime:"
+ "startTime"
+ "supportsAnchoredTextAttachments"
+ "textAttachmentViewProviderForTextParagraphAnchoredAttachment:"
+ "textLayoutManager:cachedTextAttachmentViewProviderForTextAttachment:"
+ "textLayoutManager:willInvalidateTextAttachmentViewProvider:forTextAttachment:"
+ "textViewportLayoutController:cacheRenderingSurface:forCacheableObjectsInKey:"
+ "textViewportLayoutController:cachedRenderingSurfaceForCacheableObjectsInKey:"
+ "totalElapsedTime"
+ "totalElapsedTimeIndex"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?q@\"NSAttributedString\"@\"NSAttributedString\"{CGRect={CGPoint=dd}{CGSize=dd}}>24"
+ "v32@?0@\"NSAttributedString\"8Q16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v32@?0@\"NSTextAttachmentViewProvider\"8Q16^B24"
+ "v64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24^{CGContext=}56"
+ "v64@?0q8@\"NSAttributedString\"16@\"NSAttributedString\"24{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "verticalPosition"
+ "weakObjectsHashTable"
+ "willInvalidateTextAttachmentViewProvider:forTextAttachment:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"
+ "\x81"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb1"
- ".DecoTypeNastaleeqUrduUI-Bold"
- ".DecoTypeNastaleeqUrduUI-Regular"
- "Alignment %@%@, LineSpacing %g, ParagraphSpacing %g, ParagraphSpacingBefore %g, HeadIndent %g, TailIndent %g, FirstLineHeadIndent %g, LineHeight %g/%g, LineHeightMultiple %g, LineBreakMode %@%@, Tabs %@, DefaultTabInterval %g, Blocks %@, Lists %@, BaseWritingDirection %@, HyphenationFactor %g, TighteningForTruncation %@, HeaderLevel %ld LineBreakStrategy %lu%@ PresentationIntents %@ ListIntentOrdinal %ld CodeBlockIntentLanguageHint '%@'"
- "AlwaysUseDecoTypeNastaliq"
- "CoreText"
- "InternationalSupport"
- "KnownUrduSequencesAltUIFont"
- "NSEmojiImagePropertyKeyOrigin"
- "T@\"NSTextLayoutFragment\",V_textLayoutFragment"
- "Td,N,V_actualTrackingAdjustment"
- "_delegatesSupportsTruncationToken"
- "_deviceLanguage"
- "_isEmojiImageTextAttachmentData:UTI:"
- "ar"
- "initWithImage:alignmentInset:"
- "setActualTrackingAdjustment:"
- "ur"
- "{CGPoint=dd}"

```
