## PlatterKit

> `/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit`

```diff

-311.5.0.0.0
-  __TEXT.__text: 0x277e8
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x3088
-  __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__cstring: 0xc02
+311.8.0.0.0
+  __TEXT.__text: 0x23c04
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_methlist: 0x2b30
+  __TEXT.__const: 0x1b8
+  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__cstring: 0xbd4
   __TEXT.__oslogstring: 0x512
-  __TEXT.__objc_const_ax: 0x358
-  __TEXT.__unwind_info: 0xda0
-  __TEXT.__objc_classname: 0x8a1
-  __TEXT.__objc_methname: 0xb7b5
-  __TEXT.__objc_methtype: 0x2454
-  __TEXT.__objc_stubs: 0x8000
+  __TEXT.__objc_const_ax: 0x34c
+  __TEXT.__unwind_info: 0xc74
+  __TEXT.__objc_classname: 0x85d
+  __TEXT.__objc_methname: 0xabfb
+  __TEXT.__objc_methtype: 0x2327
+  __TEXT.__objc_stubs: 0x7740
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x7e8
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc558
-  __DATA_CONST.__objc_selrefs: 0x25e0
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_const: 0xb590
+  __DATA_CONST.__objc_selrefs: 0x2358
+  __DATA_CONST.__objc_arraydata: 0x40
+  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__objc_const: 0xed0
-  __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH.__objc_data: 0x780
+  __AUTH_CONST.__objc_const: 0xe40
+  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH.__objc_data: 0x6e0
   __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x340
-  __DATA.__objc_superrefs: 0x100
-  __DATA.__objc_ivar: 0x39c
+  __DATA.__objc_classrefs: 0x330
+  __DATA.__objc_superrefs: 0xf0
+  __DATA.__objc_ivar: 0x360
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0xb58
+  __DATA.__data: 0xaf8
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x28

   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1193
-  Symbols:   4753
-  CStrings:  2118
+  Functions: 1080
+  Symbols:   4392
+  CStrings:  2003
 
Symbols:
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ ___65-[PLPillView initWithLeadingAccessoryView:trailingAccessoryView:]_block_invoke
+ ___68-[PLPillControl initWithLeadingAccessoryView:trailingAccessoryView:]_block_invoke
+ ___block_descriptor_40_e8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_retain_x28
- -[PLPillControl traitCollectionDidChange:]
- -[PLPillView traitCollectionDidChange:]
- -[PLSummaryContentView .cxx_destruct]
- -[PLSummaryContentView _cachedNumberOfMeasuredLinesForText:withFont:forWidth:]
- -[PLSummaryContentView _clearCacheForFont:]
- -[PLSummaryContentView _configureTextSupportingView:]
- -[PLSummaryContentView _contentInsetsForLongLook]
- -[PLSummaryContentView _contentInsetsForShortLook]
- -[PLSummaryContentView _contentInsets]
- -[PLSummaryContentView _fontProvider]
- -[PLSummaryContentView _frameForThumbnailInRect:]
- -[PLSummaryContentView _invalidateNumberOfLinesCache]
- -[PLSummaryContentView _lazyPrimaryLabel]
- -[PLSummaryContentView _lazyPrimarySubtitleLabel]
- -[PLSummaryContentView _lazySecondaryLabel]
- -[PLSummaryContentView _lazySecondaryTextSupportingView]
- -[PLSummaryContentView _lazySummaryLabel]
- -[PLSummaryContentView _lazyThumbnailImageView]
- -[PLSummaryContentView _newPrimaryLabel]
- -[PLSummaryContentView _newSecondaryLabel]
- -[PLSummaryContentView _newSummaryLabel]
- -[PLSummaryContentView _numberOfMeasuredLinesForText:withFont:forSize:]
- -[PLSummaryContentView _primaryLabelBoundsForSize:withContentInsets:andNumberOfLines:]
- -[PLSummaryContentView _primaryLabel]
- -[PLSummaryContentView _primarySubtitleLabelBoundsForSize:withContentInsets:andNumberOfLines:]
- -[PLSummaryContentView _primarySubtitleLabel]
- -[PLSummaryContentView _primarySubtitleTextBaselineOffsetForCurrentStyle]
- -[PLSummaryContentView _primarySubtitleTextMeasuredNumberOfLinesForWidth:]
- -[PLSummaryContentView _primarySubtitleTextNumberOfLinesWithMeasuredNumberOfLines:]
- -[PLSummaryContentView _primaryTextBaselineOffsetWithBaseValue:]
- -[PLSummaryContentView _primaryTextMeasuredNumberOfLinesForWidth:]
- -[PLSummaryContentView _primaryTextNumberOfLinesWithMeasuredNumberOfLines:]
- -[PLSummaryContentView _secondaryLabel]
- -[PLSummaryContentView _secondaryTextBaselineOffsetForCurrentStyle]
- -[PLSummaryContentView _secondaryTextBaselineOffsetFromBottomWithBaseValue:]
- -[PLSummaryContentView _secondaryTextBaselineOffsetWithBaseValue:]
- -[PLSummaryContentView _secondaryTextMeasuredNumberOfLinesForWidth:]
- -[PLSummaryContentView _secondaryTextNumberOfLinesWithMeasuredNumberOfLines:]
- -[PLSummaryContentView _secondaryTextNumberOfLines]
- -[PLSummaryContentView _secondaryTextSupportingView]
- -[PLSummaryContentView _secondaryTextViewBoundsForSize:withContentInsets:andNumberOfLines:]
- -[PLSummaryContentView _setPrimaryLabel:]
- -[PLSummaryContentView _setPrimarySubtitleLabel:]
- -[PLSummaryContentView _setSecondaryTextNumberOfLines:]
- -[PLSummaryContentView _setSummaryLabel:]
- -[PLSummaryContentView _sizeThatFits:withContentInsets:]
- -[PLSummaryContentView _summaryLabelBoundsForSize:withContentInsets:andNumberOfLines:]
- -[PLSummaryContentView _summaryLabel]
- -[PLSummaryContentView _summaryTextBaselineOffsetForCurrentStyle]
- -[PLSummaryContentView _summaryTextBaselineOffsetWithBaseValue:]
- -[PLSummaryContentView _summaryTextMeasuredNumberOfLinesForWidth:]
- -[PLSummaryContentView _summaryTextNumberOfLinesWithMeasuredNumberOfLines:]
- -[PLSummaryContentView _updateFontForSecondaryTextSupportingView:]
- -[PLSummaryContentView _updateStyleForPrimaryLabel:]
- -[PLSummaryContentView _updateStyleForSecondaryTextSupportingView:]
- -[PLSummaryContentView _updateStyleForSummaryLabel:]
- -[PLSummaryContentView _updateTextAttributesForLabel:]
- -[PLSummaryContentView _updateTextAttributesForPrimaryLabel:]
- -[PLSummaryContentView _updateTextAttributesForSummaryLabel:]
- -[PLSummaryContentView accessoryView]
- -[PLSummaryContentView adjustForContentSizeCategoryChange]
- -[PLSummaryContentView adjustsFontForContentSizeCategory]
- -[PLSummaryContentView debugDescription]
- -[PLSummaryContentView descriptionBuilderWithMultilinePrefix:]
- -[PLSummaryContentView descriptionWithMultilinePrefix:]
- -[PLSummaryContentView fontProvider]
- -[PLSummaryContentView init]
- -[PLSummaryContentView layoutSubviews]
- -[PLSummaryContentView messageNumberOfLines]
- -[PLSummaryContentView preferredContentSizeCategory]
- -[PLSummaryContentView primarySubtitleText]
- -[PLSummaryContentView primaryText]
- -[PLSummaryContentView requiredVisualStyleCategories]
- -[PLSummaryContentView secondaryText]
- -[PLSummaryContentView setAccessoryView:]
- -[PLSummaryContentView setAdjustsFontForContentSizeCategory:]
- -[PLSummaryContentView setFontProvider:]
- -[PLSummaryContentView setMessageNumberOfLines:]
- -[PLSummaryContentView setPreferredContentSizeCategory:]
- -[PLSummaryContentView setPrimarySubtitleText:]
- -[PLSummaryContentView setPrimaryText:]
- -[PLSummaryContentView setSecondaryText:]
- -[PLSummaryContentView setSummaryText:]
- -[PLSummaryContentView setThumbnail:]
- -[PLSummaryContentView setVisualStylingProvider:forCategory:]
- -[PLSummaryContentView sizeThatFits:]
- -[PLSummaryContentView summaryText]
- -[PLSummaryContentView thumbnail]
- -[PLSummaryContentView traitCollectionDidChange:]
- -[PLSummaryContentView visualStylingProviderForCategory:]
- -[PLTitledSummaryPlatterView .cxx_destruct]
- -[PLTitledSummaryPlatterView _configureSummaryContentViewIfNecessary]
- -[PLTitledSummaryPlatterView _layoutSummaryContentView]
- -[PLTitledSummaryPlatterView accessoryView]
- -[PLTitledSummaryPlatterView adjustForContentSizeCategoryChange]
- -[PLTitledSummaryPlatterView adjustsFontForContentSizeCategory]
- -[PLTitledSummaryPlatterView layoutSubviews]
- -[PLTitledSummaryPlatterView messageNumberOfLines]
- -[PLTitledSummaryPlatterView primarySubtitleText]
- -[PLTitledSummaryPlatterView primaryText]
- -[PLTitledSummaryPlatterView secondaryText]
- -[PLTitledSummaryPlatterView setAccessoryView:]
- -[PLTitledSummaryPlatterView setAdjustsFontForContentSizeCategory:]
- -[PLTitledSummaryPlatterView setBackgroundView:]
- -[PLTitledSummaryPlatterView setMessageNumberOfLines:]
- -[PLTitledSummaryPlatterView setPrimarySubtitleText:]
- -[PLTitledSummaryPlatterView setPrimaryText:]
- -[PLTitledSummaryPlatterView setSecondaryText:]
- -[PLTitledSummaryPlatterView setSummaryText:]
- -[PLTitledSummaryPlatterView setThumbnail:]
- -[PLTitledSummaryPlatterView sizeThatFits:]
- -[PLTitledSummaryPlatterView sizeThatFitsContentWithSize:]
- -[PLTitledSummaryPlatterView summaryText]
- -[PLTitledSummaryPlatterView thumbnail]
- _OBJC_CLASS_$_BSUIEmojiLabelView
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_PLSummaryContentView
- _OBJC_CLASS_$_PLTitledSummaryPlatterView
- _OBJC_IVAR_$_PLSummaryContentView._accessoryView
- _OBJC_IVAR_$_PLSummaryContentView._adjustsFontForContentSizeCategory
- _OBJC_IVAR_$_PLSummaryContentView._contentInsets
- _OBJC_IVAR_$_PLSummaryContentView._contentView
- _OBJC_IVAR_$_PLSummaryContentView._drawingContext
- _OBJC_IVAR_$_PLSummaryContentView._fontProvider
- _OBJC_IVAR_$_PLSummaryContentView._preferredContentSizeCategory
- _OBJC_IVAR_$_PLSummaryContentView._primaryLabel
- _OBJC_IVAR_$_PLSummaryContentView._primarySubtitleLabel
- _OBJC_IVAR_$_PLSummaryContentView._secondaryLabel
- _OBJC_IVAR_$_PLSummaryContentView._summaryLabel
- _OBJC_IVAR_$_PLSummaryContentView._thumbnailImageView
- _OBJC_IVAR_$_PLSummaryContentView._visualStylingProvider
- _OBJC_IVAR_$_PLSummaryContentView._widthToFontToStringToMeasuredNumLines
- _OBJC_IVAR_$_PLTitledSummaryPlatterView._summaryContentView
- _OBJC_METACLASS_$_PLSummaryContentView
- _OBJC_METACLASS_$_PLTitledSummaryPlatterView
- _UIRectCenteredYInRectScale
- _UIRoundToViewScale
- __OBJC_$_INSTANCE_METHODS_PLSummaryContentView
- __OBJC_$_INSTANCE_METHODS_PLTitledSummaryPlatterView
- __OBJC_$_INSTANCE_VARIABLES_PLSummaryContentView
- __OBJC_$_INSTANCE_VARIABLES_PLTitledSummaryPlatterView
- __OBJC_$_PROP_LIST_PLSummaryContentView
- __OBJC_$_PROP_LIST_PLSummaryPlatter
- __OBJC_$_PROP_LIST_PLTitledSummaryPlatterView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLSummaryPlatter
- __OBJC_$_PROTOCOL_METHOD_TYPES_PLSummaryPlatter
- __OBJC_$_PROTOCOL_REFS_PLSummaryPlatter
- __OBJC_CLASS_PROTOCOLS_$_PLSummaryContentView
- __OBJC_CLASS_PROTOCOLS_$_PLTitledSummaryPlatterView
- __OBJC_CLASS_RO_$_PLSummaryContentView
- __OBJC_CLASS_RO_$_PLTitledSummaryPlatterView
- __OBJC_LABEL_PROTOCOL_$_PLSummaryPlatter
- __OBJC_METACLASS_RO_$_PLSummaryContentView
- __OBJC_METACLASS_RO_$_PLTitledSummaryPlatterView
- __OBJC_PROTOCOL_$_PLSummaryPlatter
- ___62-[PLSummaryContentView descriptionBuilderWithMultilinePrefix:]_block_invoke
- _objc_msgSend$_cachedNumberOfMeasuredLinesForText:withFont:forWidth:
- _objc_msgSend$_clearCacheForFont:
- _objc_msgSend$_configureSummaryContentViewIfNecessary
- _objc_msgSend$_configureTextSupportingView:
- _objc_msgSend$_contentInsetsForShortLook
- _objc_msgSend$_frameForThumbnailInRect:
- _objc_msgSend$_invalidateNumberOfLinesCache
- _objc_msgSend$_layoutSummaryContentView
- _objc_msgSend$_lazyPrimaryLabel
- _objc_msgSend$_lazyPrimarySubtitleLabel
- _objc_msgSend$_lazySecondaryLabel
- _objc_msgSend$_lazySecondaryTextSupportingView
- _objc_msgSend$_lazySummaryLabel
- _objc_msgSend$_lazyThumbnailImageView
- _objc_msgSend$_newPrimaryLabel
- _objc_msgSend$_newSecondaryLabel
- _objc_msgSend$_newSummaryLabel
- _objc_msgSend$_numberOfMeasuredLinesForText:withFont:forSize:
- _objc_msgSend$_primaryLabelBoundsForSize:withContentInsets:andNumberOfLines:
- _objc_msgSend$_primarySubtitleLabelBoundsForSize:withContentInsets:andNumberOfLines:
- _objc_msgSend$_primarySubtitleTextBaselineOffsetForCurrentStyle
- _objc_msgSend$_primarySubtitleTextMeasuredNumberOfLinesForWidth:
- _objc_msgSend$_primarySubtitleTextNumberOfLinesWithMeasuredNumberOfLines:
- _objc_msgSend$_primaryTextBaselineOffsetWithBaseValue:
- _objc_msgSend$_primaryTextMeasuredNumberOfLinesForWidth:
- _objc_msgSend$_primaryTextNumberOfLinesWithMeasuredNumberOfLines:
- _objc_msgSend$_secondaryTextBaselineOffsetForCurrentStyle
- _objc_msgSend$_secondaryTextBaselineOffsetFromBottomWithBaseValue:
- _objc_msgSend$_secondaryTextBaselineOffsetWithBaseValue:
- _objc_msgSend$_secondaryTextMeasuredNumberOfLinesForWidth:
- _objc_msgSend$_secondaryTextNumberOfLines
- _objc_msgSend$_secondaryTextNumberOfLinesWithMeasuredNumberOfLines:
- _objc_msgSend$_secondaryTextSupportingView
- _objc_msgSend$_secondaryTextViewBoundsForSize:withContentInsets:andNumberOfLines:
- _objc_msgSend$_setSecondaryTextNumberOfLines:
- _objc_msgSend$_setTextAlignmentFollowsWritingDirection:
- _objc_msgSend$_sizeThatFits:withContentInsets:
- _objc_msgSend$_summaryLabelBoundsForSize:withContentInsets:andNumberOfLines:
- _objc_msgSend$_summaryTextBaselineOffsetForCurrentStyle
- _objc_msgSend$_summaryTextBaselineOffsetWithBaseValue:
- _objc_msgSend$_summaryTextMeasuredNumberOfLinesForWidth:
- _objc_msgSend$_summaryTextNumberOfLinesWithMeasuredNumberOfLines:
- _objc_msgSend$_updateFontForSecondaryTextSupportingView:
- _objc_msgSend$_updateStyleForPrimaryLabel:
- _objc_msgSend$_updateStyleForSecondaryTextSupportingView:
- _objc_msgSend$_updateStyleForSummaryLabel:
- _objc_msgSend$_updateTextAttributesForLabel:
- _objc_msgSend$_updateTextAttributesForPrimaryLabel:
- _objc_msgSend$_updateTextAttributesForSummaryLabel:
- _objc_msgSend$allKeys
- _objc_msgSend$boundingRectWithSize:options:attributes:context:
- _objc_msgSend$centerXAnchor
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$messageNumberOfLines
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$primarySubtitleText
- _objc_msgSend$primaryText
- _objc_msgSend$removeAllObjects
- _objc_msgSend$secondaryText
- _objc_msgSend$setAccessoryView:
- _objc_msgSend$setFontProvider:
- _objc_msgSend$setMessageNumberOfLines:
- _objc_msgSend$setNeedsDisplay
- _objc_msgSend$setPrimarySubtitleText:
- _objc_msgSend$setPrimaryText:
- _objc_msgSend$setSecondaryText:
- _objc_msgSend$setSummaryText:
- _objc_msgSend$setThumbnail:
- _objc_msgSend$summaryText
- _objc_msgSend$thumbnail
CStrings:
+ "registerForTraitChanges:withHandler:"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
- "@\"BSUIEmojiLabelView\""
- "@\"PLSummaryContentView\""
- "@\"UIImage\"16@0:8"
- "E\x17"
- "PLSummaryContentView"
- "PLSummaryPlatter"
- "PLTitledSummaryPlatterView"
- "Q40@0:8@16@24d32"
- "Q48@0:8@16@24{CGSize=dd}32"
- "T@\"BSUIEmojiLabelView\",&,N,G_summaryLabel,S_setSummaryLabel:,V_summaryLabel"
- "T@\"BSUIFontProvider\",&,N,V_fontProvider"
- "T@\"NSString\",&,N"
- "T@\"UIImage\",&,N"
- "T@\"UILabel\",&,N,G_primaryLabel,S_setPrimaryLabel:,V_primaryLabel"
- "T@\"UILabel\",&,N,G_primarySubtitleLabel,S_setPrimarySubtitleLabel:,V_primarySubtitleLabel"
- "T@\"UILabel\",R,N,G_secondaryLabel,V_secondaryLabel"
- "T@\"UIView\",&,N,V_accessoryView"
- "TQ,N"
- "UILabel"
- "_cachedNumberOfMeasuredLinesForText:withFont:forWidth:"
- "_clearCacheForFont:"
- "_configureSummaryContentViewIfNecessary"
- "_configureTextSupportingView:"
- "_contentInsets"
- "_contentInsetsForLongLook"
- "_contentInsetsForShortLook"
- "_frameForThumbnailInRect:"
- "_invalidateNumberOfLinesCache"
- "_layoutSummaryContentView"
- "_lazyPrimaryLabel"
- "_lazyPrimarySubtitleLabel"
- "_lazySecondaryLabel"
- "_lazySecondaryTextSupportingView"
- "_lazySummaryLabel"
- "_lazyThumbnailImageView"
- "_newPrimaryLabel"
- "_newSecondaryLabel"
- "_newSummaryLabel"
- "_numberOfMeasuredLinesForText:withFont:forSize:"
- "_primaryLabel"
- "_primaryLabelBoundsForSize:withContentInsets:andNumberOfLines:"
- "_primarySubtitleLabel"
- "_primarySubtitleLabelBoundsForSize:withContentInsets:andNumberOfLines:"
- "_primarySubtitleTextBaselineOffsetForCurrentStyle"
- "_primarySubtitleTextMeasuredNumberOfLinesForWidth:"
- "_primarySubtitleTextNumberOfLinesWithMeasuredNumberOfLines:"
- "_primaryTextBaselineOffsetWithBaseValue:"
- "_primaryTextMeasuredNumberOfLinesForWidth:"
- "_primaryTextNumberOfLinesWithMeasuredNumberOfLines:"
- "_secondaryLabel"
- "_secondaryTextBaselineOffsetForCurrentStyle"
- "_secondaryTextBaselineOffsetFromBottomWithBaseValue:"
- "_secondaryTextBaselineOffsetWithBaseValue:"
- "_secondaryTextMeasuredNumberOfLinesForWidth:"
- "_secondaryTextNumberOfLines"
- "_secondaryTextNumberOfLinesWithMeasuredNumberOfLines:"
- "_secondaryTextSupportingView"
- "_secondaryTextViewBoundsForSize:withContentInsets:andNumberOfLines:"
- "_setPrimaryLabel:"
- "_setPrimarySubtitleLabel:"
- "_setSecondaryTextNumberOfLines:"
- "_setSummaryLabel:"
- "_setTextAlignmentFollowsWritingDirection:"
- "_sizeThatFits:withContentInsets:"
- "_summaryContentView"
- "_summaryLabel"
- "_summaryLabelBoundsForSize:withContentInsets:andNumberOfLines:"
- "_summaryTextBaselineOffsetForCurrentStyle"
- "_summaryTextBaselineOffsetWithBaseValue:"
- "_summaryTextMeasuredNumberOfLinesForWidth:"
- "_summaryTextNumberOfLinesWithMeasuredNumberOfLines:"
- "_thumbnailImageView"
- "_updateFontForSecondaryTextSupportingView:"
- "_updateStyleForPrimaryLabel:"
- "_updateStyleForSecondaryTextSupportingView:"
- "_updateStyleForSummaryLabel:"
- "_updateTextAttributesForLabel:"
- "_updateTextAttributesForPrimaryLabel:"
- "_updateTextAttributesForSummaryLabel:"
- "_widthToFontToStringToMeasuredNumLines"
- "allKeys"
- "boundingRectWithSize:options:attributes:context:"
- "centerXAnchor"
- "dictionaryWithObjects:forKeys:count:"
- "messageNumberOfLines"
- "numberWithDouble:"
- "numberWithUnsignedInteger:"
- "primaryLabel"
- "primarySubtitleLabel"
- "primarySubtitleText"
- "primaryText"
- "removeAllObjects"
- "secondaryLabel"
- "secondaryText"
- "setAccessoryView:"
- "setFontProvider:"
- "setMessageNumberOfLines:"
- "setNeedsDisplay"
- "setPrimarySubtitleText:"
- "setPrimaryText:"
- "setSecondaryText:"
- "setSummaryText:"
- "setThumbnail:"
- "summary-label"
- "summaryLabel"
- "summaryText"
- "thumbnail"
- "traitCollectionDidChange:"
- "v24@0:8@\"UIImage\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}72@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32Q64"
- "{CGSize=dd}64@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"

```
