## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation`

```diff

-969.5.0.0.0
-  __TEXT.__text: 0x13ddd4
-  __TEXT.__auth_stubs: 0x27c0
-  __TEXT.__objc_methlist: 0xc14c
-  __TEXT.__const: 0x11ec
-  __TEXT.__cstring: 0x16f4f
+970.5.0.0.0
+  __TEXT.__text: 0x13d92c
+  __TEXT.__auth_stubs: 0x27d0
+  __TEXT.__objc_methlist: 0xc868
+  __TEXT.__const: 0x120c
+  __TEXT.__cstring: 0x16f7f
   __TEXT.__ustring: 0x31a
-  __TEXT.__gcc_except_tab: 0x34a0
+  __TEXT.__gcc_except_tab: 0x34c4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x43c8
-  __TEXT.__objc_classname: 0x134f
-  __TEXT.__objc_methname: 0x21fca
-  __TEXT.__objc_methtype: 0x918f
-  __TEXT.__objc_stubs: 0x173e0
+  __TEXT.__unwind_info: 0x44d0
+  __TEXT.__objc_classname: 0x12a8
+  __TEXT.__objc_methname: 0x21c9a
+  __TEXT.__objc_methtype: 0x9133
+  __TEXT.__objc_stubs: 0x172c0
   __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__const: 0x7080
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7370
+  __DATA_CONST.__objc_selrefs: 0x7390
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x13f0
-  __AUTH_CONST.__const: 0x43b8
-  __AUTH_CONST.__cfstring: 0x10380
-  __AUTH_CONST.__objc_const: 0x15518
+  __AUTH_CONST.__auth_got: 0x13f8
+  __AUTH_CONST.__const: 0x4418
+  __AUTH_CONST.__cfstring: 0x10340
+  __AUTH_CONST.__objc_const: 0x14240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xb40
-  __AUTH.__data: 0x48
-  __DATA.__objc_ivar: 0x1580
-  __DATA.__data: 0x1360
-  __DATA.__bss: 0x1048
+  __AUTH.__objc_data: 0xaa0
+  __AUTH.__data: 0x68
+  __DATA.__objc_ivar: 0x1560
+  __DATA.__data: 0x12f0
+  __DATA.__bss: 0x1060
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2440
-  __DATA_DIRTY.__data: 0x678
-  __DATA_DIRTY.__bss: 0x5d8
+  __DATA_DIRTY.__data: 0x660
+  __DATA_DIRTY.__bss: 0x5b8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
+  - /System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: EE3427E1-5CCA-3C01-99AF-BD5D17303540
-  Functions: 5651
-  Symbols:   13872
-  CStrings:  12325
+  UUID: B58C5D0B-E098-3C9C-91C7-AF5C8E906AD0
+  Functions: 5896
+  Symbols:   14205
+  CStrings:  12282
 
Symbols:
+ +[NSAttributedString(NSAttributedStringAttachmentConveniences) attributedStringWithAttachment:].cold.1
+ +[NSAttributedString(NSAttributedStringUIFoundationAdditions) _documentTypeForFileType:].cold.1
+ +[NSAttributedString(NSAttributedStringUIFoundationAdditions) allowedSecureCodingClasses].cold.1
+ +[NSCoreTypesetter _allowsFontOverridingTextAttachmentVerticalMetricsForStringDrawing].cold.1
+ +[NSCountableTextLocation endOfDocumentLocation].cold.1
+ +[NSCountableTextRange documentRange].cold.1
+ +[NSEmojiImageTextAttachment _UTIForEmojiImage].cold.1
+ +[NSEmojiImageTextAttachment _readsEmojiImageTextAttachmentFromDocumentFormats].cold.1
+ +[NSEmojiImageTextAttachment setEmojiImageTextAttachment:forContentIdentifier:].cold.1
+ +[NSFont _allowsDefaultFontSubstitution].cold.1
+ +[NSFont availableMembersOfFontFamily:].cold.1
+ +[NSFont initialize].cold.1
+ +[NSGlyphGenerator defaultGlyphGenerator].cold.1
+ +[NSHTMLReader _usesLibXML2ForOptions:].cold.1
+ +[NSHTMLReader allowsAttributedStringAgentForOptions:].cold.1
+ +[NSLayoutManager(NSPrivate) _defaultLinkAttributesForLabel].cold.1
+ +[NSLayoutManager(NSPrivate) _defaultLinkAttributes].cold.1
+ +[NSOpenDocumentReader _gregorianCalendar].cold.1
+ +[NSParagraphArbitrator _hyphenatesAsLastResort].cold.1
+ +[NSParagraphArbitrator _languageCategoryForLanguageCode:].cold.1
+ +[NSParagraphArbitrator _lineBreakStyleForFont:].cold.1
+ +[NSParagraphArbitrator initialize].cold.1
+ +[NSParagraphStyle defaultParagraphStyle].cold.1
+ +[NSParagraphStyle initialize].cold.1
+ +[NSRTFWriter cocoaVersion].cold.1
+ +[NSTextAttachment imageCache].cold.1
+ +[NSTextContentStorage __isNotesTextContentStorageClass].cold.1
+ +[NSTextContentStorage _includesTextListMarkers].cold.1
+ +[NSTextContentStorage _usesTextListElements].cold.1
+ +[NSTextElement _searchElements:forLocation:].cold.1
+ +[NSTextElement _searchElements:forLocation:].cold.2
+ +[NSTextElement _searchElements:forLocation:].cold.3
+ +[NSTextGraphicsContextProvider textGraphicsContextProviderClass].cold.1
+ +[NSTextLayoutFragment _validCoreTextRenderingAttributes].cold.1
+ +[NSTextLayoutFragment coordinateSystemCompatibilityFor2022AndEarlierSDKEnabled].cold.1
+ +[NSTextLayoutFragment layoutFragmentQueue].cold.1
+ +[NSTextLayoutManager _textHighlightBackgroundColorPercentage].cold.1
+ +[NSTextLayoutManager _usesOutlinedHighlightByDefault].cold.1
+ +[NSTextLayoutManager linkRenderingAttributesForLabels].cold.1
+ +[NSTextLayoutManager linkRenderingAttributes].cold.1
+ +[NSTextLayoutManager maximumNumberOfCachedTextLayoutFragments].cold.1
+ +[NSTextLayoutManager shouldBeUsedForNSTextView].cold.1
+ +[NSTextLayoutManager usesHyphenation].cold.1
+ +[NSTextLayoutManager validRenderingAttributes].cold.1
+ +[NSTextLayoutManager(UIFoundation_AppKitAdditions) textHighlightAttributes_macOS].cold.1
+ +[NSTextLayoutManager(UIFoundation_UIKitAdditions) textHighlightAttributes_iOS].cold.1
+ +[NSTextLineFragment _hiddenContentRenderingAttributes].cold.1
+ +[NSTextList includesTextListMarkers].cold.1
+ +[NSTextSelectionNavigation _setupCharacterSets].cold.1
+ +[NSTextViewportLayoutController flushesCachedViewportElements].cold.1
+ +[NSWordMLReader _gregorianCalendar].cold.1
+ +[UIFont _sharedFontCache].cold.1
+ +[UIFont _sharedZeroPointFont].cold.1
+ +[UIFont _supportedDynamicFontStyles].cold.1
+ -[NSATSGlyphStorage release].cold.1
+ -[NSATSTypesetter _baseWritingDirection].cold.1
+ -[NSATSTypesetter _baselineRenderingMode].cold.1
+ -[NSATSTypesetter _bidiLevels].cold.1
+ -[NSATSTypesetter _ctTypesetter].cold.1
+ -[NSATSTypesetter _ctTypesetter].cold.2
+ -[NSATSTypesetter _doBidiProcessing].cold.1
+ -[NSATSTypesetter _flushCachedObjects].cold.1
+ -[NSATSTypesetter _forceWordWrapping].cold.1
+ -[NSATSTypesetter _getATSTypesetterGuts].cold.1
+ -[NSATSTypesetter _isBusy].cold.1
+ -[NSATSTypesetter _layoutLineFragmentStartingWithGlyphAtIndex:characterIndex:atPoint:renderingContext:].cold.1
+ -[NSATSTypesetter _layoutLineFragmentStartingWithGlyphAtIndex:characterIndex:atPoint:renderingContext:].cold.2
+ -[NSATSTypesetter _layoutLineFragmentStartingWithGlyphAtIndex:characterIndex:atPoint:renderingContext:].cold.3
+ -[NSATSTypesetter _layoutLineFragmentStartingWithGlyphAtIndex:characterIndex:atPoint:renderingContext:].cold.4
+ -[NSATSTypesetter _lineFragmentRectForProposedRectArgs].cold.1
+ -[NSATSTypesetter _setBaselineRenderingMode:].cold.1
+ -[NSATSTypesetter _setBusy:].cold.1
+ -[NSATSTypesetter _setForceWordWrapping:].cold.1
+ -[NSATSTypesetter beginLineWithGlyphAtIndex:].cold.1
+ -[NSATSTypesetter beginParagraph].cold.1
+ -[NSATSTypesetter defaultTighteningFactor].cold.1
+ -[NSATSTypesetter endLineWithGlyphRange:].cold.1
+ -[NSATSTypesetter endParagraph].cold.1
+ -[NSATSTypesetter init].cold.1
+ -[NSATSTypesetter limitsLayoutForSuspiciousContents].cold.1
+ -[NSATSTypesetter lineBreakStrategy].cold.1
+ -[NSATSTypesetter lineFragmentRectForProposedRect:remainingRect:].cold.1
+ -[NSATSTypesetter setDefaultTighteningFactor:].cold.1
+ -[NSATSTypesetter setLimitsLayoutForSuspiciousContents:].cold.1
+ -[NSATSTypesetter setLineBreakStrategy:].cold.1
+ -[NSAttributedString(NSAttributedStringUIFoundationAdditions) containsAttachmentsInRange:].cold.1
+ -[NSAttributedString(NSAttributedStringUIFoundationAdditions) lineBreakByHyphenatingBeforeIndex:withinRange:].cold.1
+ -[NSAttributedString(NSExtendedStringDrawing) boundingRectWithSize:options:context:].cold.1
+ -[NSConcreteTextStorage _initLocks].cold.1
+ -[NSCoreTypesetter _shouldShowLineBadges].cold.1
+ -[NSCoreTypesetter isSimpleRectangularTextContainerForStartingCharacterAtIndex:].cold.1
+ -[NSDataAsset initWithName:bundle:].cold.1
+ -[NSEmojiImageTextAttachment initWithData:].cold.1
+ -[NSFont _isUIFontWithUIKitBehavior].cold.1
+ -[NSFont initWithCoder:].cold.1
+ -[NSFont setInContext:].cold.1
+ -[NSFontDescriptor _NSAffineTransform].cold.1
+ -[NSFontDescriptor _fontDescriptorWithMatrix:].cold.1
+ -[NSFontDescriptor _matrix].cold.1
+ -[NSFontDescriptor initWithCoder:].cold.1
+ -[NSGlyphGenerator generateGlyphsForGlyphStorage:desiredNumberOfCharacters:glyphIndex:characterIndex:].cold.1
+ -[NSHTMLReader _addAttachmentForElement:URL:needsParagraph:usePlaceholder:].cold.1
+ -[NSHTMLWebDelegate webView:decidePolicyForNavigationAction:request:frame:decisionListener:].cold.1
+ -[NSLayoutManager _commonInit].cold.1
+ -[NSLayoutManager _hyphenationFactor].cold.1
+ -[NSLayoutManager _setHyphenationFactor:].cold.1
+ -[NSLayoutManager(NSLayoutManager_Debugging) _stringForLoggingLineFragmentForGlyphAtIndex:].cold.1
+ -[NSLayoutManager(NSPrivate) _drawGlyphsForGlyphRange:atPoint:].cold.1
+ -[NSLayoutManager(NSPrivate) beginScrollingForView:textContainer:].cold.1
+ -[NSLayoutManager(NSPrivate) prepareLayoutForBoundingRect:textContainer:].cold.1
+ -[NSLayoutManager(NSPrivate) showAttachment:inRect:textContainer:characterIndex:].cold.1
+ -[NSLayoutManager(OtherSupport) _drawLineForGlyphRange:type:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:isStrikethrough:].cold.1
+ -[NSLayoutManager(OtherSupport) drawSpellingUnderlineForGlyphRange:spellingState:inGlyphRange:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:].cold.1
+ -[NSLineFragmentRenderingContext drawAtPoint:inContext:].cold.1
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) applyFontTraits:range:].cold.1
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.1
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.10
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.11
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.12
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.13
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.14
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.15
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.16
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.17
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.18
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.19
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.2
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.3
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.4
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.5
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.6
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.7
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.8
+ -[NSMutableAttributedString(NSMutableAttributedStringKitAdditions) fixFontAttributeInRange:].cold.9
+ -[NSMutableParagraphStyle _mutateTabStops].cold.1
+ -[NSMutableParagraphStyle setTabStops:].cold.1
+ -[NSParagraphArbitrator _firstFitLineBreakContextBeforeIndex:lineFragmentWidth:range:].cold.1
+ -[NSParagraphArbitrator _lineBreakStyleForLastResortHyphenation:].cold.1
+ -[NSParagraphArbitrator _preferredLanguageForCharacterAtIndex:].cold.1
+ -[NSParagraphArbitrator _shouldUseCFStringTokenizerForLineBreaks].cold.1
+ -[NSParagraphArbitrator _shouldUseOptimalLayout].cold.1
+ -[NSParagraphArbitrator adjustedLineBreakIndexForProposedIndex:].cold.1
+ -[NSParagraphArbitrator prepareTokenizerForPreferredLanguage:].cold.1
+ -[NSParagraphStyle _allocExtraData].cold.1
+ -[NSParagraphStyle tabStops].cold.1
+ -[NSRTFReader _currentTableCellIsPlaceholder].cold.1
+ -[NSRTFReader _setTableNestingLevel:].cold.1
+ -[NSRTFReader _setTableNestingLevel:].cold.2
+ -[NSShadow initWithCoder:].cold.1
+ -[NSSingleLineTypesetter createRenderingContextForCharacterRange:typesetterBehavior:usesScreenFonts:hasStrongRight:syncDirection:mirrorsTextAlignment:maximumWidth:].cold.1
+ -[NSSingleLineTypesetter createRenderingContextForCharacterRange:typesetterBehavior:usesScreenFonts:hasStrongRight:syncDirection:mirrorsTextAlignment:maximumWidth:].cold.2
+ -[NSString(UIFontPrivate) stringByStrippingLeadingAndTrailingWhitespaceAndQuotes].cold.1
+ -[NSSubstituteWebResource _webResourceClass].cold.1
+ -[NSTextAttachment _textAttachmentCell].cold.1
+ -[NSTextAttachment initWithCoder:].cold.1
+ -[NSTextBlock borderColorForEdge:].cold.1
+ -[NSTextBlock borderColorForEdge:].cold.2
+ -[NSTextBlock initWithCoder:].cold.1
+ -[NSTextBlock initWithCoder:].cold.2
+ -[NSTextBlock initWithCoder:].cold.3
+ -[NSTextBlock initWithCoder:].cold.4
+ -[NSTextLayoutFragment _textAttributesAffectingLayout].cold.1
+ -[NSTextLayoutFragment rangeInElement].cold.1
+ -[NSTextLayoutManager _validateTextContainerEntries].cold.1
+ -[NSTextLayoutManager _validateTextContainerEntries].cold.2
+ -[NSTextLayoutManager _validateTextContainerEntries].cold.3
+ -[NSTextLayoutManager documentRange].cold.1
+ -[NSTextLineFragment _drawTextCorrectionMarker:characterRange:atOrigin:graphicsContext:].cold.1
+ -[NSTextLineFragment _getCaretPositionsForCharactersInRange:positionsCache:positionsCacheSize:block:].cold.1
+ -[NSTextLineFragment characterIndexForPoint:fractionOfDistanceThroughGlyph:].cold.1
+ -[NSTextListElement initWithParentElement:textList:contents:markerAttributes:childElements:].cold.1
+ -[NSTextRange initWithLocation:endLocation:].cold.1
+ -[NSTextRange textRangeByIntersectingWithTextRange:].cold.1
+ -[NSTextSelectionNavigation _usesVisualBidiSelection].cold.1
+ -[NSTextStorage setDelegate:].cold.1
+ -[NSTextTab initWithType:location:].cold.1
+ -[NSTextTab tabStopType].cold.1
+ -[NSTypesetter _getRemainingNominalParagraphRange:andParagraphSeparatorRange:charactarIndex:layoutManager:string:].cold.1
+ -[NSWritingToolsContextState .cxx_destruct]
+ -[NSWritingToolsContextState initWithContextString:contextLocation:proposedRange:].cold.1
+ -[NSWritingToolsEditTracker .cxx_destruct]
+ -[NSWritingToolsEditTracker _adjustLocation:].cold.1
+ -[NSWritingToolsEditTracker adjustRange:].cold.1
+ -[NSWritingToolsProofreadingController identifier]
+ -[NSWritingToolsProofreadingController setIdentifier:]
+ -[NSWritingToolsProofreadingSuggestion .cxx_destruct]
+ -[UIFont _scaledValueForValue:useLanguageAwareScaling:].cold.1
+ -[UIFont encodeWithCoder:].cold.1
+ -[UIFontDescriptor initWithCoder:].cold.1
+ -[UINibEncoder encodeConditionalObject:forKey:].cold.1
+ -[UINibEncoder encodeObject:forKey:].cold.1
+ -[_NSLineBreakerNodeDictionary setNode:forClass:].cold.2
+ -[_NSLineMetrics _finalAdvanceForCharacterAtIndex:range:].cold.3
+ -[_NSLineMetrics _hasShaping].cold.1
+ -[_NSLineMetrics _initialAdvanceForCharacterAtIndex:range:].cold.2
+ -[_NSOptimalLineBreaker _addLineBreakWithRange:flags:].cold.3
+ -[_NSOptimalLineBreaker _bestNode:dominatesNode:].cold.5
+ -[_NSOptimalLineBreaker _estimatedExpansionRatioForLineWithNaturalWidth:].cold.2
+ -[_NSOptimalLineBreaker _mustExceedLineCount:].cold.3
+ -[_NSTextHighlightCluster registerMaxYOfRun:].cold.1
+ -[_NSTextHighlightCluster registerMinYOfRun:].cold.1
+ -[_NSTextHighlightRun initWithTextRange:withCluster:].cold.1
+ -[__NSFontTypefaceInfo _familyName].cold.1
+ -[__NSWritingToolsEdit .cxx_destruct]
+ -[__NSWritingToolsEdit initWithRange:delta:identifier:]
+ -[__NSWritingToolsEdit range]
+ GCC_except_table101
+ NSDefaultFont.cold.1
+ NSTextContentStorageBreakOnEnumerateWhileEditing.cold.1
+ NSTextLayoutManagerBreakOnNilContentManager.cold.1
+ OBJC_IVAR_$_NSWritingToolsEditTracker._uuidToEdit
+ OBJC_IVAR_$_NSWritingToolsProofreadingController._identifier
+ OBJC_IVAR_$___NSWritingToolsEdit._delta
+ OBJC_IVAR_$___NSWritingToolsEdit._identifier
+ OBJC_IVAR_$___NSWritingToolsEdit._range
+ _GetNextUrduSequenceFromInlineBuffer
+ _ISEnumerateKnownUrduSequencesInString
+ _MergedGlobals.485
+ _NSAttachmentCharacterSet.cold.1
+ _NSBidiControlCharacterSet.cold.1
+ _NSBidiEmbeddingAndOverrideCharSet.cold.1
+ _NSCopyBreakIterator.cold.2
+ _NSFontAttributeNames.cold.1
+ _NSGetAppKitVersionNumber.cold.1
+ _NSGetUIFoundationVersionNumber.cold.1
+ _NSNonAttachmentCharacterSet.cold.1
+ _NSReadAttributedStringFromHTMLData.cold.1
+ _NSReadAttributedStringFromHTMLData.cold.2
+ _OBJC_CLASS_$___NSWritingToolsEdit
+ _OBJC_METACLASS_$___NSWritingToolsEdit
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _UIFoundationAssert.cold.1
+ __103-[NSTextLineFragment drawMarkedTextIndicatorAtPoint:graphicsContext:backgroundOnly:adjustmentCallback:]_block_invoke.cold.1
+ __24+[UIFont _readableWidth]_block_invoke_2.cold.1
+ __43+[NSConcreteTextStorage _writerCountTSDKey]_block_invoke.cold.1
+ __58-[NSTextLayoutManager _invalidateLayoutForTextRange:hard:]_block_invoke_2.cold.1
+ __94-[NSWritingToolsProofreadingController addSuggestionWithUUID:originalRange:replacementString:]_block_invoke.81
+ __CTFontGetExtraData.cold.1
+ __GetNextUrduSequenceFromInlineBuffer_block_invoke.64
+ __MergedGlobals
+ __NSGetFrameworkReference.cold.1
+ __NSGetMetaFontInstanceWithType.cold.1
+ __NSGetNSAppearanceClass.cold.1
+ __NSGetSystemFontVariants.cold.1
+ __NSGetSystemFontVariants.cold.2
+ __NSStringDrawingEngine.cold.1
+ __NSStringDrawingEngine.cold.2
+ __NSStringDrawingEngine.cold.3
+ __NSStringDrawingEngine.cold.4
+ __NSTokenizerLanguageSet.cold.1
+ __NSUltraFastLineBreakFinder.cold.1
+ __NSValidateCoreTextAttributes.cold.1
+ __OBJC_$_INSTANCE_METHODS___NSWritingToolsEdit
+ __OBJC_$_INSTANCE_VARIABLES___NSWritingToolsEdit
+ __OBJC_CLASS_RO_$___NSWritingToolsEdit
+ __OBJC_METACLASS_RO_$___NSWritingToolsEdit
+ ___GetNextUrduSequenceFromInlineBuffer_block_invoke
+ ___NSGetAppKitVersionNumber_block_invoke.cold.1
+ ____NSTextContentStorageCacheElementIndexRange_block_invoke.cold.1
+ ____NSTextContentStorageCacheElementIndexRange_block_invoke_2.cold.1
+ ____NSTextContentStorageGetTextElementAtIndex_block_invoke.cold.1
+ ___block_descriptor_40_e8_32bs_e42_v28?0"NSUUID"8"NSAttributedString"16B24l
+ ___block_descriptor_40_e8_32r_e17_v32?0{?=qq}8^B24l
+ ___block_descriptor_40_e8_32s_e18_"NSString"16?08l
+ ___block_descriptor_48_e8_32s_e18_"NSString"16?08l
+ ___block_descriptor_64_e8_32s40bs48w_e42_v28?0"NSUUID"8"NSAttributedString"16B24l
+ ___block_descriptor_97_e8_32s40bs48w_e42_v28?0"NSUUID"8"NSAttributedString"16B24l
+ ___copy_helper_block_e8_32s40b48w
+ ___destroy_helper_block_e8_32s40s48w
+ __block_literal_global.84
+ __block_literal_global.86
+ __block_literal_global.89
+ __fastRunStorageElementAtIndex
+ _fontNameForFont.cold.1
+ _objc_msgSend$_deviceLanguage
+ _rtfBlackColor.cold.1
+ _rtfWhiteColor.cold.1
+ charIsNormalWhitespace.cold.1
+ defaultBreakLanguage.cold.1
+ fixFontAttributeInRange:.useDecoTypeFontForUrdu
+ getColor.cold.1
+ getColor.cold.2
+ processColor.cold.1
+ processColor.cold.2
- -[NSCoreTypesetter _NSFastDrawString:length:attributes:paragraphStyle:typesetterBehavior:lineBreakMode:rect:padding:graphicsContext:baselineRendering:usesFontLeading:usesScreenFont:scrollable:syncAlignment:mirrored:boundingRectPointer:baselineOffsetPointer:drawingContext:].cold.1
- -[NSCoreTypesetter _NSFastDrawString:length:attributes:paragraphStyle:typesetterBehavior:lineBreakMode:rect:padding:graphicsContext:baselineRendering:usesFontLeading:usesScreenFont:scrollable:syncAlignment:mirrored:boundingRectPointer:baselineOffsetPointer:drawingContext:].cold.2
- -[NSWritingToolsAnimationParameters .cxx_destruct]
- -[NSWritingToolsAnimationParameters alongsideAnimation]
- -[NSWritingToolsAnimationParameters alongsideCompletion]
- -[NSWritingToolsAnimationParameters delay]
- -[NSWritingToolsAnimationParameters duration]
- -[NSWritingToolsAnimationParameters initWithDelay:duration:]
- -[NSWritingToolsAnimationParameters setAlongsideAnimation:]
- -[NSWritingToolsAnimationParameters setAlongsideCompletion:]
- -[NSWritingToolsContext .cxx_destruct]
- -[NSWritingToolsContext _setEvaluatedRange:]
- -[NSWritingToolsContext attributedString]
- -[NSWritingToolsContext description]
- -[NSWritingToolsContext evaluatedRange]
- -[NSWritingToolsContext identifier]
- -[NSWritingToolsContext initWithAttributedString:range:]
- -[NSWritingToolsContext range]
- -[NSWritingToolsContext(NSWritingToolsContext_APITransition) attributedText]
- -[NSWritingToolsContext(NSWritingToolsContext_APITransition) initWithAttributedText:range:]
- -[NSWritingToolsContext(NSWritingToolsContext_APITransition) uuid]
- -[NSWritingToolsContextState dealloc]
- -[NSWritingToolsEditTracker dealloc]
- -[NSWritingToolsProofreadingController finished]
- -[NSWritingToolsProofreadingController setContextString:]
- -[NSWritingToolsProofreadingController setDelegate:]
- -[NSWritingToolsProofreadingController setEditTracker:]
- -[NSWritingToolsProofreadingController setFinished:]
- -[NSWritingToolsProofreadingController setSuggestionsByRange:]
- -[NSWritingToolsProofreadingController setSuggestionsByUUID:]
- -[NSWritingToolsProofreadingSuggestion dealloc]
- -[NSWritingToolsSelection .cxx_destruct]
- -[NSWritingToolsSelection contextIdentifier]
- -[NSWritingToolsSelection description]
- -[NSWritingToolsSelection initWithRange:contextIdentifier:]
- -[NSWritingToolsSelection range]
- -[NSWritingToolsSelection(NSWritingToolsSelection_APITransition) initWithSelectionRange:selectionContextID:]
- -[NSWritingToolsSelection(NSWritingToolsSelection_APITransition) selectionContextID]
- -[NSWritingToolsSelection(NSWritingToolsSelection_APITransition) selectionRange]
- GCC_except_table32
- OBJC_IVAR_$_NSWritingToolsAnimationParameters._alongsideAnimation
- OBJC_IVAR_$_NSWritingToolsAnimationParameters._alongsideCompletion
- OBJC_IVAR_$_NSWritingToolsAnimationParameters._delay
- OBJC_IVAR_$_NSWritingToolsAnimationParameters._duration
- OBJC_IVAR_$_NSWritingToolsContext._attributedString
- OBJC_IVAR_$_NSWritingToolsContext._evaluatedRange
- OBJC_IVAR_$_NSWritingToolsContext._identifier
- OBJC_IVAR_$_NSWritingToolsContext._range
- OBJC_IVAR_$_NSWritingToolsEditTracker._capacity
- OBJC_IVAR_$_NSWritingToolsEditTracker._count
- OBJC_IVAR_$_NSWritingToolsEditTracker._uuidToIndex
- OBJC_IVAR_$_NSWritingToolsSelection._contextIdentifier
- OBJC_IVAR_$_NSWritingToolsSelection._range
- _NSFastDrawString:length:attributes:paragraphStyle:typesetterBehavior:lineBreakMode:rect:padding:graphicsContext:baselineRendering:usesFontLeading:usesScreenFont:scrollable:syncAlignment:mirrored:boundingRectPointer:baselineOffsetPointer:drawingContext:.once
- _NSFastDrawString:length:attributes:paragraphStyle:typesetterBehavior:lineBreakMode:rect:padding:graphicsContext:baselineRendering:usesFontLeading:usesScreenFont:scrollable:syncAlignment:mirrored:boundingRectPointer:baselineOffsetPointer:drawingContext:.whitespaceCharacterSet
- _OBJC_CLASS_$_NSWritingToolsAnimationParameters
- _OBJC_CLASS_$_NSWritingToolsContext
- _OBJC_CLASS_$_NSWritingToolsSelection
- _OBJC_METACLASS_$_NSWritingToolsAnimationParameters
- _OBJC_METACLASS_$_NSWritingToolsContext
- _OBJC_METACLASS_$_NSWritingToolsSelection
- __94-[NSWritingToolsProofreadingController addSuggestionWithUUID:originalRange:replacementString:]_block_invoke.70
- __OBJC_$_INSTANCE_METHODS_NSWritingToolsAnimationParameters
- __OBJC_$_INSTANCE_METHODS_NSWritingToolsContext(NSWritingToolsContext_APITransition)
- __OBJC_$_INSTANCE_METHODS_NSWritingToolsSelection(NSWritingToolsSelection_APITransition)
- __OBJC_$_INSTANCE_VARIABLES_NSWritingToolsAnimationParameters
- __OBJC_$_INSTANCE_VARIABLES_NSWritingToolsContext
- __OBJC_$_INSTANCE_VARIABLES_NSWritingToolsSelection
- __OBJC_$_PROP_LIST_NSWritingToolsAnimationParameters
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__NSWritingToolsContextKitAdditions
- __OBJC_$_PROTOCOL_METHOD_TYPES__NSWritingToolsContextKitAdditions
- __OBJC_$_PROTOCOL_REFS__NSWritingToolsContextKitAdditions
- __OBJC_CLASS_PROTOCOLS_$_NSWritingToolsContext
- __OBJC_CLASS_RO_$_NSWritingToolsAnimationParameters
- __OBJC_CLASS_RO_$_NSWritingToolsContext
- __OBJC_CLASS_RO_$_NSWritingToolsSelection
- __OBJC_LABEL_PROTOCOL_$__NSWritingToolsContextKitAdditions
- __OBJC_METACLASS_RO_$_NSWritingToolsAnimationParameters
- __OBJC_METACLASS_RO_$_NSWritingToolsContext
- __OBJC_METACLASS_RO_$_NSWritingToolsSelection
- __OBJC_PROTOCOL_$__NSWritingToolsContextKitAdditions
- ___CFArrayTypeID
- ___NSATSGlyphStorageCache
- ___NSATSGlyphStorageCacheNextIndex
- ___NSATSGlyphStorageLock
- ___NSATSTypesetterClass
- ___NSAllowsScreenFontKerning
- ___NSLineFragmentRectIMP
- ___block_descriptor_105_e8_32o40o48b56w_e42_v28?0"NSUUID"8"NSAttributedString"16B24l
- ___block_descriptor_40_e8_32b_e42_v28?0"NSUUID"8"NSAttributedString"16B24l
- ___block_descriptor_40_e8_32o_e18_"NSString"16?08l
- ___block_descriptor_64_e8_32o40b48w_e42_v28?0"NSUUID"8"NSAttributedString"16B24l
- ___copy_helper_block_e8_32o40b48w
- ___copy_helper_block_e8_32o40o48b56w
- ___destroy_helper_block_e8_32o40b48w
- ___destroy_helper_block_e8_32o40o48b56w
- __block_literal_global.61
- __block_literal_global.73
- _enumerateNonBreakingSpacesWithBlock:.nbspCharacterSet
- _enumerateNonBreakingSpacesWithBlock:.once
- _generateOpenStepCompatible
- _objc_msgSend$_uuidForNewWritingToolsContextFromRange:attributedText:
- _objc_msgSend$attributedText
- _objc_msgSend$contextIdentifier
- _objc_msgSend$finished
- _objc_msgSend$initWithRange:contextIdentifier:
- _objc_msgSend$setEditTracker:
- _objc_msgSend$setFinished:
- _objc_msgSend$setSuggestionsByRange:
- _objc_msgSend$setSuggestionsByUUID:
- _objc_msgSend$stringByAppendingFormat:
- _plainFontNameForFont:.fontToPlainNameTable
- _plainFontNameForFont:.tigerCompatibility
- _rtfWritingLock
- _shouldAvoidBreakingAfterWord:.maxShortWordLength
- _shouldAvoidBreakingAfterWord:.once
- _shouldAvoidBreakingAfterWord:.wordSets
- createCTTypesetter.numWarnings
- getMetricsForTextSize:cornerRadius:cornerOutset:.onceToken
- getMetricsForTextSize:cornerRadius:cornerOutset:.outsetIncrement
- rtfFontFamilyForFontFamily.fontMapTable
- rtfFontFamilyForFontFamily.loadedExternalFile
CStrings:
+ ".DecoTypeNastaleeqUrduUI-Bold"
+ ".DecoTypeNastaleeqUrduUI-Regular"
+ "AlwaysUseDecoTypeNastaliq"
+ "CoreText"
+ "InternationalSupport"
+ "KnownUrduSequencesAltUIFont"
+ "T@\"<NSWritingToolsProofreadingControllerDelegate>\",R,W,V_delegate"
+ "T@\"NSAttributedString\",R,C,V_contextString"
+ "T@\"NSAttributedString\",R,C,V_replacementString"
+ "T@\"NSMutableArray\",R,V_suggestionsByRange"
+ "T@\"NSMutableDictionary\",R,V_suggestionsByUUID"
+ "T@\"NSUUID\",&,V_identifier"
+ "T@\"NSUUID\",R,V_uuid"
+ "T@\"NSWritingToolsEditTracker\",R,V_editTracker"
+ "TB,V_acceptOpenSuggestionsInFinish"
+ "Tq,R,V_lengthDelta"
+ "Tq,V_state"
+ "T{_NSRange=QQ},R,V_currentContextRange"
+ "T{_NSRange=QQ},R,V_originalRange"
+ "__NSWritingToolsEdit"
+ "_delta"
+ "_deviceLanguage"
+ "_uuidToEdit"
+ "ar"
+ "setIdentifier:"
+ "ur"
+ "v32@?0{?=qq}8^B24"
- " evaluatedRange={%lu,%lu}"
- " no evaluated range,"
- " range={%lu, %lu} contextID=%@"
- " range={%lu,%lu}"
- " text=%@"
- "@\"NSUUID\"40@0:8{_NSRange=QQ}16@\"NSAttributedString\"32"
- "NSWritingToolsAnimationParameters"
- "NSWritingToolsContext"
- "NSWritingToolsContext_APITransition"
- "NSWritingToolsSelection"
- "NSWritingToolsSelection_APITransition"
- "T@\"<NSWritingToolsProofreadingControllerDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",R,C,N"
- "T@\"NSAttributedString\",R,C"
- "T@\"NSAttributedString\",R,C,N,V_replacementString"
- "T@\"NSAttributedString\",R,C,V_attributedString"
- "T@\"NSMutableArray\",&,N,V_suggestionsByRange"
- "T@\"NSMutableDictionary\",&,N,V_suggestionsByUUID"
- "T@\"NSUUID\",R"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"NSUUID\",R,V_contextIdentifier"
- "T@\"NSUUID\",R,V_identifier"
- "T@\"NSWritingToolsEditTracker\",&,N,V_editTracker"
- "T@?,C,V_alongsideAnimation"
- "T@?,C,V_alongsideCompletion"
- "TB,N,V_acceptOpenSuggestionsInFinish"
- "TB,N,V_finished"
- "Td,R,V_delay"
- "Td,R,V_duration"
- "Tq,N,V_state"
- "Tq,R,N,V_lengthDelta"
- "T{_NSRange=QQ},R,N"
- "T{_NSRange=QQ},R,N,V_currentContextRange"
- "T{_NSRange=QQ},R,N,V_originalRange"
- "T{_NSRange=QQ},R,V_evaluatedRange"
- "^{NSWritingToolsEdit={_NSRange=QQ}q@}"
- "_NSWritingToolsContextKitAdditions"
- "_alongsideAnimation"
- "_alongsideCompletion"
- "_contextIdentifier"
- "_delay"
- "_evaluatedRange"
- "_setEvaluatedRange:"
- "_uuidForNewWritingToolsContextFromRange:attributedText:"
- "_uuidToIndex"
- "alongsideAnimation"
- "alongsideCompletion"
- "attributedText"
- "contextIdentifier"
- "delay"
- "evaluatedRange"
- "finished"
- "index out of range"
- "initWithAttributedText:range:"
- "initWithDelay:duration:"
- "initWithRange:contextIdentifier:"
- "initWithSelectionRange:selectionContextID:"
- "selectionContextID"
- "selectionRange"
- "setAlongsideAnimation:"
- "setAlongsideCompletion:"
- "setEditTracker:"
- "setFinished:"
- "setSuggestionsByRange:"
- "setSuggestionsByUUID:"
- "stringByAppendingFormat:"

```
