## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-304.5.4.102.0
-  __TEXT.__text: 0x1be6c
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x1bf4
-  __TEXT.__const: 0x330
-  __TEXT.__cstring: 0xf2a
-  __TEXT.__oslogstring: 0xf13
-  __TEXT.__gcc_except_tab: 0x70c
-  __TEXT.__unwind_info: 0x918
-  __TEXT.__objc_classname: 0x4fb
-  __TEXT.__objc_methname: 0x4a0a
-  __TEXT.__objc_methtype: 0xd84
-  __TEXT.__objc_stubs: 0x39c0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x8a0
-  __DATA_CONST.__objc_classlist: 0x100
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x70
+341.0.3.0.0
+  __TEXT.__text: 0x232ec
+  __TEXT.__objc_methlist: 0x25c0
+  __TEXT.__const: 0x340
+  __TEXT.__cstring: 0x12ab
+  __TEXT.__oslogstring: 0x11f5
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__unwind_info: 0xb80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x968
+  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1218
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x690
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0x4f98
+  __DATA_CONST.__objc_selrefs: 0x18c0
+  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__got: 0x4a0
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x16a0
+  __AUTH_CONST.__objc_const: 0x6398
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x224
-  __DATA.__data: 0x540
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x334
+  __DATA.__data: 0x600
   __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit
+  - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76089E4D-26B5-3DB7-BC79-C6374CDFC794
-  Functions: 690
-  Symbols:   2865
-  CStrings:  1390
+  UUID: FB090CF5-E359-3DC9-996A-A64344299187
+  Functions: 905
+  Symbols:   3699
+  CStrings:  480
 
Symbols:
+ +[PLKImageRenderer contextWithFormat:].cold.1
+ +[PLKImageRenderer contextWithFormat:].cold.2
+ +[PLKLabel defaultLayerGroup]
+ +[PLKLabel defaultLayerGroup].cold.1
+ +[PLKLabelContent _measureSizeWithFramesetter:forAttributedString:withConstraints:numberOfLines:]
+ +[PLKLabelContent _measureSizeWithFramesetter:forAttributedString:withConstraints:numberOfLines:].cold.1
+ +[PLKLabelContent _measureSizeWithFramesetter:forAttributedString:withConstraints:numberOfLines:].cold.2
+ +[PLKLabelContent differencesBetween:and:]
+ +[PLKLabelContent supportsSecureCoding]
+ +[PLKLegibilityContent contentWithImage:]
+ +[PLKLegibilityContent defaultSynchronousLegibilityImageGenerator]
+ +[PLKLegibilityDescriptor legibilityDescriptorForSettings:strength:options:]
+ +[UIColor(RenderBox) plk_colorWithRBColor:]
+ -[PLKCachedImageGenerator _drainPendingPrewarm]
+ -[PLKLabel .cxx_destruct]
+ -[PLKLabel HDRMode]
+ -[PLKLabel _applyContentModeTransform:toBounds:inDisplayList:]
+ -[PLKLabel _commonInit]
+ -[PLKLabel _contentSizeCategoryDidChange:]
+ -[PLKLabel _dynamicRangeDidChange]
+ -[PLKLabel _effectiveDisplayScale]
+ -[PLKLabel _initializeLabel]
+ -[PLKLabel _invalidateGlyphCache]
+ -[PLKLabel _invalidateShadowCache]
+ -[PLKLabel _labelContentDidChange]
+ -[PLKLabel _labelContentHasUniformColor:outUniformColor:]
+ -[PLKLabel _layoutSubviews]
+ -[PLKLabel _performScheduledDisplay]
+ -[PLKLabel _rebuildCachedShadowContents]
+ -[PLKLabel _rebuildCachedShadowContents].cold.1
+ -[PLKLabel _rebuildCachedTextContents]
+ -[PLKLabel _registerForTraitChanges]
+ -[PLKLabel _renderAllLayers]
+ -[PLKLabel _renderPendingLayers]
+ -[PLKLabel _resetLabelContent]
+ -[PLKLabel _scheduleDisplay]
+ -[PLKLabel _setNeedsShadowLayerDisplay]
+ -[PLKLabel _setNeedsTextLayerDisplay]
+ -[PLKLabel _shouldBeBackdropAware]
+ -[PLKLabel _updateAccessibilityProperties]
+ -[PLKLabel _updateDisplayScale]
+ -[PLKLabel _updateForTraitCollection]
+ -[PLKLabel _updateShadowLayerFilter]
+ -[PLKLabel _updateTextLayerColorMode]
+ -[PLKLabel _updateTextLayerFilter]
+ -[PLKLabel _updateTraitBasedBackdropAwareness]
+ -[PLKLabel _updateUserInterfaceStyle]
+ -[PLKLabel adjustsFontForContentSizeCategory]
+ -[PLKLabel adjustsFontSizeToFitWidth]
+ -[PLKLabel allowsDefaultTighteningForTruncation]
+ -[PLKLabel attributedText]
+ -[PLKLabel clearColor]
+ -[PLKLabel clearsBackground]
+ -[PLKLabel colorMode]
+ -[PLKLabel dealloc]
+ -[PLKLabel didMoveToSuperview]
+ -[PLKLabel didMoveToWindow]
+ -[PLKLabel displayHeadroomLimit]
+ -[PLKLabel firstBaselineOffsetFromTop]
+ -[PLKLabel font]
+ -[PLKLabel forceDisplayIfNeeded]
+ -[PLKLabel hitTest:withEvent:]
+ -[PLKLabel initWithCoder:]
+ -[PLKLabel initWithFrame:]
+ -[PLKLabel init]
+ -[PLKLabel intrinsicContentSize]
+ -[PLKLabel isBackdropAware]
+ -[PLKLabel isDrawableAvailable]
+ -[PLKLabel isTraitBasedBackdropAwarenessEnabled]
+ -[PLKLabel labelContent]
+ -[PLKLabel lastBaselineOffsetFromBottom]
+ -[PLKLabel layoutSubviews]
+ -[PLKLabel legibilityDescriptor]
+ -[PLKLabel lineBreakMode]
+ -[PLKLabel lineBreakStrategy]
+ -[PLKLabel minimumScaleFactor]
+ -[PLKLabel noteBackdropAwarenessTraitDidUpdate]
+ -[PLKLabel numberOfLines]
+ -[PLKLabel prepareForReuse]
+ -[PLKLabel rendersAsynchronously]
+ -[PLKLabel setAdjustsFontForContentSizeCategory:]
+ -[PLKLabel setAdjustsFontSizeToFitWidth:]
+ -[PLKLabel setAllowsDefaultTighteningForTruncation:]
+ -[PLKLabel setAttributedText:]
+ -[PLKLabel setBackdropAware:]
+ -[PLKLabel setBounds:]
+ -[PLKLabel setClearColor:]
+ -[PLKLabel setClearsBackground:]
+ -[PLKLabel setColorMode:]
+ -[PLKLabel setContentMode:]
+ -[PLKLabel setDisplayHeadroomLimit:]
+ -[PLKLabel setFont:]
+ -[PLKLabel setFrame:]
+ -[PLKLabel setHDRMode:]
+ -[PLKLabel setLabelContent:]
+ -[PLKLabel setLegibilityDescriptor:]
+ -[PLKLabel setLineBreakMode:]
+ -[PLKLabel setLineBreakStrategy:]
+ -[PLKLabel setMinimumScaleFactor:]
+ -[PLKLabel setNeedsAsyncDisplay]
+ -[PLKLabel setNeedsDisplay]
+ -[PLKLabel setNumberOfLines:]
+ -[PLKLabel setOpaque:]
+ -[PLKLabel setRendersAsynchronously:]
+ -[PLKLabel setText:]
+ -[PLKLabel setTextAlignment:]
+ -[PLKLabel setTextColor:]
+ -[PLKLabel setTraitBasedBackdropAwarenessEnabled:]
+ -[PLKLabel sizeThatFits:]
+ -[PLKLabel sizeToFit]
+ -[PLKLabel textAlignment]
+ -[PLKLabel textColor]
+ -[PLKLabel textRectForBounds:limitedToNumberOfLines:]
+ -[PLKLabel text]
+ -[PLKLabel waitUntilAsyncRenderingCompleted]
+ -[PLKLabelContent .cxx_destruct]
+ -[PLKLabelContent _calculateAndCacheBaselinesWithFramesetter:intrinsicSize:]
+ -[PLKLabelContent _calculateAndCacheBaselinesWithFramesetter:intrinsicSize:].cold.1
+ -[PLKLabelContent _calculateInkBoundsForCTFrame:]
+ -[PLKLabelContent _calculatePropertiesHash]
+ -[PLKLabelContent _effectiveConstraintWidthForBounds:]
+ -[PLKLabelContent _ensureLayoutCacheIsValid]
+ -[PLKLabelContent _ensureLayoutCacheIsValid].cold.1
+ -[PLKLabelContent _ensureLayoutCacheIsValid].cold.2
+ -[PLKLabelContent _hasCustomFrameBounds]
+ -[PLKLabelContent _hasCustomTextRect]
+ -[PLKLabelContent _initializeWithDefaults]
+ -[PLKLabelContent _intrinsicSizeForAttributedString:]
+ -[PLKLabelContent _intrinsicSizeForAttributedString:].cold.1
+ -[PLKLabelContent _invalidateAndRecalculateHash]
+ -[PLKLabelContent _isConstrainedLayout]
+ -[PLKLabelContent _resolvedLayoutByFittingString:toWidth:]
+ -[PLKLabelContent _resolvedLayoutByFittingString:toWidth:].cold.1
+ -[PLKLabelContent _resolvedLayoutByFittingString:toWidth:].cold.2
+ -[PLKLabelContent _resolvedLayoutForBounds:frameBounds:textRect:]
+ -[PLKLabelContent _resolvedLayoutForBounds:frameBounds:textRect:].cold.1
+ -[PLKLabelContent adjustsFontSizeToFitWidth]
+ -[PLKLabelContent allowsDefaultTighteningForTruncation]
+ -[PLKLabelContent attributedText]
+ -[PLKLabelContent boundingRect]
+ -[PLKLabelContent copyWithZone:]
+ -[PLKLabelContent description]
+ -[PLKLabelContent drawInDisplayList:bounds:blendMode:alpha:]
+ -[PLKLabelContent drawInRect:inContext:blendMode:alpha:]
+ -[PLKLabelContent effectiveAttributedText]
+ -[PLKLabelContent effectiveAttributedText].cold.1
+ -[PLKLabelContent encodeWithCoder:]
+ -[PLKLabelContent firstBaselineOffsetFromTop]
+ -[PLKLabelContent font]
+ -[PLKLabelContent frameBounds]
+ -[PLKLabelContent hash]
+ -[PLKLabelContent initWithAttributedText:]
+ -[PLKLabelContent initWithAttributedText:frameBounds:textRect:]
+ -[PLKLabelContent initWithAttributedText:frameBounds:textRect:].cold.1
+ -[PLKLabelContent initWithCoder:]
+ -[PLKLabelContent initWithText:]
+ -[PLKLabelContent init]
+ -[PLKLabelContent isEmpty]
+ -[PLKLabelContent isEqual:]
+ -[PLKLabelContent isEqualToLabelContent:]
+ -[PLKLabelContent lastBaselineOffsetFromBottom]
+ -[PLKLabelContent lineBreakMode]
+ -[PLKLabelContent lineBreakStrategy]
+ -[PLKLabelContent minimumScaleFactor]
+ -[PLKLabelContent mutableCopyWithZone:]
+ -[PLKLabelContent numberOfLines]
+ -[PLKLabelContent overflowEdgeInsets]
+ -[PLKLabelContent sizeThatFits:]
+ -[PLKLabelContent sizeThatFits:].cold.1
+ -[PLKLabelContent textAlignment]
+ -[PLKLabelContent textColor]
+ -[PLKLabelContent textRectForBounds:limitedToNumberOfLines:]
+ -[PLKLabelContent textRect]
+ -[PLKLabelContent text]
+ -[PLKLegibilityBackgroundContentDescriptor shadowRenderScale]
+ -[PLKLegibilityDescriptor(RenderBox) applyShadowStylesToDisplayList:renderScale:shadowRenderScale:textColor:]
+ -[PLKLegibilityDescriptor(RenderBox) drawShadowsInDisplayList:renderScale:shadowRenderScale:textColor:drawingBlock:]
+ -[PLKLegibilityView hitTest:withEvent:]
+ -[PLKMutableLabelContent _updateFont:forTraitCollection:]
+ -[PLKMutableLabelContent copyWithZone:]
+ -[PLKMutableLabelContent setAdjustsFontSizeToFitWidth:]
+ -[PLKMutableLabelContent setAllowsDefaultTighteningForTruncation:]
+ -[PLKMutableLabelContent setAttributedText:]
+ -[PLKMutableLabelContent setFont:]
+ -[PLKMutableLabelContent setLineBreakMode:]
+ -[PLKMutableLabelContent setLineBreakStrategy:]
+ -[PLKMutableLabelContent setMinimumScaleFactor:]
+ -[PLKMutableLabelContent setNumberOfLines:]
+ -[PLKMutableLabelContent setOverflowEdgeInsets:]
+ -[PLKMutableLabelContent setText:]
+ -[PLKMutableLabelContent setTextAlignment:]
+ -[PLKMutableLabelContent setTextColor:]
+ -[PLKMutableLabelContent updateForTraitCollection:]
+ -[PLKMutableLabelContent updateForTraitCollection:].cold.1
+ -[RBDisplayList(CoreText) _defaultTextFill]
+ -[RBDisplayList(CoreText) _drawColorGlyphRun:origin:alpha:]
+ -[RBDisplayList(CoreText) _drawGlyphRun:origin:alpha:blendMode:]
+ -[RBDisplayList(CoreText) drawAttributedString:inPath:alpha:blendMode:]
+ -[RBDisplayList(CoreText) drawAttributedString:inRect:]
+ -[RBDisplayList(CoreText) drawAttributedString:inRect:alpha:blendMode:]
+ -[RBDisplayList(CoreText) drawCTFrame:]
+ -[RBDisplayList(CoreText) drawCTFrame:alpha:blendMode:]
+ -[RBDisplayList(CoreText) drawCTLine:origin:]
+ -[RBDisplayList(CoreText) drawCTLine:origin:alpha:blendMode:]
+ -[RBDisplayList(CoreText) drawCTRun:origin:]
+ -[RBDisplayList(CoreText) drawCTRun:origin:alpha:blendMode:]
+ -[UIColor(RenderBox) plk_rbColorWithAlpha:]
+ -[UIColor(RenderBox) plk_rbColor]
+ -[_PLKLegibilityContainerView init]
+ -[_PLKNSAttributedLabelContentsProvider plk_boundingRectForObject:maxSize:]
+ -[_PLKResolvedLayout .cxx_destruct]
+ -[_PLKResolvedLayout dealloc]
+ -[_PLKStringLayoutMetrics .cxx_destruct]
+ -[_PLKStringLayoutMetrics copyWithZone:]
+ -[_PLKStringLayoutMetrics dealloc]
+ -[_PLKStringLayoutMetrics init]
+ -[_PLKStringLayoutMetrics invalidate]
+ GCC_except_table10
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table44
+ GCC_except_table72
+ GCC_except_table9
+ OBJC_IVAR_$_PLKLabelContent._adjustsFontSizeToFitWidth
+ OBJC_IVAR_$_PLKLabelContent._allowsDefaultTighteningForTruncation
+ OBJC_IVAR_$_PLKLabelContent._attributedText
+ OBJC_IVAR_$_PLKLabelContent._effectiveAttributedText
+ OBJC_IVAR_$_PLKLabelContent._font
+ OBJC_IVAR_$_PLKLabelContent._frameBounds
+ OBJC_IVAR_$_PLKLabelContent._layoutMetrics
+ OBJC_IVAR_$_PLKLabelContent._lineBreakMode
+ OBJC_IVAR_$_PLKLabelContent._lineBreakStrategy
+ OBJC_IVAR_$_PLKLabelContent._minimumScaleFactor
+ OBJC_IVAR_$_PLKLabelContent._numberOfLines
+ OBJC_IVAR_$_PLKLabelContent._overflowEdgeInsets
+ OBJC_IVAR_$_PLKLabelContent._propertiesHash
+ OBJC_IVAR_$_PLKLabelContent._text
+ OBJC_IVAR_$_PLKLabelContent._textAlignment
+ OBJC_IVAR_$_PLKLabelContent._textColor
+ OBJC_IVAR_$_PLKLabelContent._textRect
+ OBJC_IVAR_$__PLKResolvedLayout._cachedFrame
+ OBJC_IVAR_$__PLKResolvedLayout._cachedTextSize
+ OBJC_IVAR_$__PLKResolvedLayout._frameBounds
+ OBJC_IVAR_$__PLKResolvedLayout._framesetter
+ OBJC_IVAR_$__PLKResolvedLayout._framesetterIsOwnedBySelf
+ OBJC_IVAR_$__PLKResolvedLayout._isConstrained
+ OBJC_IVAR_$__PLKResolvedLayout._isPositioned
+ OBJC_IVAR_$__PLKResolvedLayout._requestedBounds
+ OBJC_IVAR_$__PLKResolvedLayout._string
+ OBJC_IVAR_$__PLKResolvedLayout._textDrawingRect
+ OBJC_IVAR_$__PLKResolvedLayout._textRect
+ OBJC_IVAR_$__PLKStringLayoutMetrics._adjustedFramesetterCache
+ OBJC_IVAR_$__PLKStringLayoutMetrics._attributedTextHash
+ OBJC_IVAR_$__PLKStringLayoutMetrics._firstBaselineOffset
+ OBJC_IVAR_$__PLKStringLayoutMetrics._framesetter
+ OBJC_IVAR_$__PLKStringLayoutMetrics._intrinsicSize
+ OBJC_IVAR_$__PLKStringLayoutMetrics._isValid
+ OBJC_IVAR_$__PLKStringLayoutMetrics._lastBaselineOffset
+ OBJC_IVAR_$__PLKStringLayoutMetrics._layoutCache
+ OBJC_IVAR_$__PLKStringLayoutMetrics._overflowEdgeInsets
+ OBJC_IVAR_$__PLKStringLayoutMetrics._sizeCache
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFRetain
+ _CGAffineTransformIsIdentity
+ _CGAffineTransformMakeTranslation
+ _CGColorCreateCopyByMatchingToColorSpace
+ _CGColorGetComponents
+ _CGColorGetNumberOfComponents
+ _CGContextSetAlpha
+ _CGContextSetBlendMode
+ _CGContextSetTextMatrix
+ _CGContextSetTextPosition
+ _CGPathAddRect
+ _CGPathCreateMutable
+ _CGPathCreateWithRect
+ _CGPathGetBoundingBox
+ _CGPathRelease
+ _CGRectContainsRect
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _CGRectInset
+ _CGRectIsInfinite
+ _CGRectIsNull
+ _CGRectNull
+ _CGRectOffset
+ _CGRectUnion
+ _CTFontCopyGraphicsFont
+ _CTFontGetSize
+ _CTFontGetSymbolicTraits
+ _CTFrameDraw
+ _CTFrameGetLineOrigins
+ _CTFrameGetLines
+ _CTFrameGetPath
+ _CTFramesetterCreateFrame
+ _CTFramesetterCreateWithAttributedString
+ _CTFramesetterSuggestFrameSizeWithConstraints
+ _CTLineGetBoundsWithOptions
+ _CTLineGetGlyphRuns
+ _CTLineGetTypographicBounds
+ _CTRunDraw
+ _CTRunGetAttributes
+ _CTRunGetGlyphCount
+ _CTRunGetGlyphs
+ _CTRunGetImageBounds
+ _CTRunGetPositions
+ _NSAttachmentAttributeName
+ _NSFontAttributeName
+ _NSForegroundColorAttributeName
+ _NSParagraphStyleAttributeName
+ _NSShadowAttributeName
+ _OBJC_CLASS_$_CATransaction
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSMutableParagraphStyle
+ _OBJC_CLASS_$_NSShadow
+ _OBJC_CLASS_$_PLKLabel
+ _OBJC_CLASS_$_PLKLabelContent
+ _OBJC_CLASS_$_PLKMutableLabelContent
+ _OBJC_CLASS_$_RBDisplayList
+ _OBJC_CLASS_$_RBFill
+ _OBJC_CLASS_$_RBLayer
+ _OBJC_CLASS_$_RBLayerGroup
+ _OBJC_CLASS_$_RBShape
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UIFontMetrics
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UITraitDisplayScale
+ _OBJC_CLASS_$_UITraitImageDynamicRange
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$__PLKNSAttributedLabelContentsProvider
+ _OBJC_CLASS_$__PLKResolvedLayout
+ _OBJC_CLASS_$__PLKStringLayoutMetrics
+ _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmCoalesceLock
+ _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmCoalesceLock_activeDrainFuture
+ _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmCoalesceLock_pendingPrewarmNilContextObjects
+ _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmCoalesceLock_pendingPrewarmObjectsByContext
+ _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmScheduledFlag
+ _OBJC_IVAR_$_PLKLabel._HDRMode
+ _OBJC_IVAR_$_PLKLabel._adjustsFontForContentSizeCategory
+ _OBJC_IVAR_$_PLKLabel._backdropAwarenessTraitRegistration
+ _OBJC_IVAR_$_PLKLabel._cachedShadowContents
+ _OBJC_IVAR_$_PLKLabel._cachedShadowContentsScale
+ _OBJC_IVAR_$_PLKLabel._cachedTextBounds
+ _OBJC_IVAR_$_PLKLabel._cachedTextContents
+ _OBJC_IVAR_$_PLKLabel._clearColor
+ _OBJC_IVAR_$_PLKLabel._clearsBackground
+ _OBJC_IVAR_$_PLKLabel._colorMode
+ _OBJC_IVAR_$_PLKLabel._displayHeadroomLimit
+ _OBJC_IVAR_$_PLKLabel._drawableAvailable
+ _OBJC_IVAR_$_PLKLabel._hasRegisteredCommitHandler
+ _OBJC_IVAR_$_PLKLabel._hasUniformColor
+ _OBJC_IVAR_$_PLKLabel._isBackdropAware
+ _OBJC_IVAR_$_PLKLabel._isInDisplay
+ _OBJC_IVAR_$_PLKLabel._isTraitBasedBackdropAwarenessEnabled
+ _OBJC_IVAR_$_PLKLabel._labelContent
+ _OBJC_IVAR_$_PLKLabel._legibilityDescriptor
+ _OBJC_IVAR_$_PLKLabel._rendersAsynchronously
+ _OBJC_IVAR_$_PLKLabel._shadowLayer
+ _OBJC_IVAR_$_PLKLabel._shadowLayerNeedsDisplay
+ _OBJC_IVAR_$_PLKLabel._textLayer
+ _OBJC_IVAR_$_PLKLabel._textLayerNeedsDisplay
+ _OBJC_IVAR_$_PLKLabel._uniformColor
+ _OBJC_IVAR_$_PLKLabelContent._boundingRect
+ _OBJC_METACLASS_$_PLKLabel
+ _OBJC_METACLASS_$_PLKLabelContent
+ _OBJC_METACLASS_$_PLKMutableLabelContent
+ _OBJC_METACLASS_$__PLKNSAttributedLabelContentsProvider
+ _OBJC_METACLASS_$__PLKResolvedLayout
+ _OBJC_METACLASS_$__PLKStringLayoutMetrics
+ _RBColorBlack
+ _RBColorWhite
+ _UIAccessibilityTraitStaticText
+ _UIFloorToScale
+ _UIFontDescriptorTextStyleAttribute
+ _UIViewNoIntrinsicMetric
+ __OBJC_$_CATEGORY_CLASS_METHODS_UIColor_$_RenderBox
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_RBDisplayList_$_CoreText
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIColor_$_RenderBox
+ __OBJC_$_CATEGORY_RBDisplayList_$_CoreText
+ __OBJC_$_CATEGORY_UIColor_$_RenderBox
+ __OBJC_$_CLASS_METHODS_PLKLabel
+ __OBJC_$_CLASS_METHODS_PLKLabelContent
+ __OBJC_$_CLASS_PROP_LIST_PLKLabelContent
+ __OBJC_$_INSTANCE_METHODS_PLKLabel
+ __OBJC_$_INSTANCE_METHODS_PLKLabelContent
+ __OBJC_$_INSTANCE_METHODS_PLKLegibilityDescriptor(RenderBox)
+ __OBJC_$_INSTANCE_METHODS_PLKMutableLabelContent
+ __OBJC_$_INSTANCE_METHODS__PLKNSAttributedLabelContentsProvider
+ __OBJC_$_INSTANCE_METHODS__PLKResolvedLayout
+ __OBJC_$_INSTANCE_METHODS__PLKStringLayoutMetrics
+ __OBJC_$_INSTANCE_VARIABLES_PLKLabel
+ __OBJC_$_INSTANCE_VARIABLES_PLKLabelContent
+ __OBJC_$_INSTANCE_VARIABLES__PLKResolvedLayout
+ __OBJC_$_INSTANCE_VARIABLES__PLKStringLayoutMetrics
+ __OBJC_$_PROP_LIST_PLKLabel
+ __OBJC_$_PROP_LIST_PLKLabelContent
+ __OBJC_$_PROP_LIST_PLKMutableLabelContent
+ __OBJC_$_PROP_LIST_UIContentSizeCategoryAdjusting
+ __OBJC_$_PROP_LIST__PLKNSAttributedLabelContentsProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSMutableCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIContentSizeCategoryAdjusting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSMutableCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIContentSizeCategoryAdjusting
+ __OBJC_$_PROTOCOL_REFS_UIContentSizeCategoryAdjusting
+ __OBJC_CLASS_PROTOCOLS_$_PLKLabel
+ __OBJC_CLASS_PROTOCOLS_$_PLKLabelContent
+ __OBJC_CLASS_PROTOCOLS_$__PLKNSAttributedLabelContentsProvider
+ __OBJC_CLASS_PROTOCOLS_$__PLKStringLayoutMetrics
+ __OBJC_CLASS_RO_$_PLKLabel
+ __OBJC_CLASS_RO_$_PLKLabelContent
+ __OBJC_CLASS_RO_$_PLKMutableLabelContent
+ __OBJC_CLASS_RO_$__PLKNSAttributedLabelContentsProvider
+ __OBJC_CLASS_RO_$__PLKResolvedLayout
+ __OBJC_CLASS_RO_$__PLKStringLayoutMetrics
+ __OBJC_LABEL_PROTOCOL_$_NSMutableCopying
+ __OBJC_LABEL_PROTOCOL_$_UIContentSizeCategoryAdjusting
+ __OBJC_METACLASS_RO_$_PLKLabel
+ __OBJC_METACLASS_RO_$_PLKLabelContent
+ __OBJC_METACLASS_RO_$_PLKMutableLabelContent
+ __OBJC_METACLASS_RO_$__PLKNSAttributedLabelContentsProvider
+ __OBJC_METACLASS_RO_$__PLKResolvedLayout
+ __OBJC_METACLASS_RO_$__PLKStringLayoutMetrics
+ __OBJC_PROTOCOL_$_NSMutableCopying
+ __OBJC_PROTOCOL_$_UIContentSizeCategoryAdjusting
+ __PLKDefaultTextAttributes
+ __PLKDefaultTextAttributes.cold.1
+ __PLKDefaultTextAttributes.fallbackDefaults
+ __PLKDefaultTextAttributes.onceToken
+ ___120+[PLKCachedLegibilityContentDataSource attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:]_block_invoke.110
+ ___28-[PLKLabel _scheduleDisplay]_block_invoke
+ ___29+[PLKLabel defaultLayerGroup]_block_invoke
+ ___32-[PLKLabel _renderPendingLayers]_block_invoke
+ ___32-[PLKLabel _renderPendingLayers]_block_invoke.26
+ ___36-[PLKLabel _performScheduledDisplay]_block_invoke
+ ___42-[PLKLabelContent effectiveAttributedText]_block_invoke
+ ___47-[PLKCachedImageGenerator _drainPendingPrewarm]_block_invoke
+ ___47-[PLKCachedImageGenerator _drainPendingPrewarm]_block_invoke.45
+ ___47-[PLKCachedImageGenerator _drainPendingPrewarm]_block_invoke_2
+ ___47-[PLKCachedImageGenerator _drainPendingPrewarm]_block_invoke_2.46
+ ___47-[PLKCachedImageGenerator _drainPendingPrewarm]_block_invoke_3
+ ___47-[PLKCachedImageGenerator _drainPendingPrewarm]_block_invoke_4
+ ___51-[PLKMutableLabelContent updateForTraitCollection:]_block_invoke
+ ___57-[PLKLabel _labelContentHasUniformColor:outUniformColor:]_block_invoke
+ ___66+[PLKLegibilityContent defaultSynchronousLegibilityImageGenerator]_block_invoke
+ ___88+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:]_block_invoke.20
+ ____PLKDefaultTextAttributes_block_invoke
+ ___block_descriptor_104_e8_32s_e23_v16?0"RBDisplayList"8ls32l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72r_e27_"UIImage"16?0"NSString"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e28_"<PFTFuture>"16?0"NSSet"8l
+ ___block_descriptor_40_e8_32r_e27_v40?08{_NSRange=QQ}16^B32lr32l8
+ ___block_descriptor_40_e8_32s_e28_"<PFTFuture>"16?0"NSSet"8ls32l8
+ ___block_descriptor_40_e8_32w_e9_16?0^8lw32l8
+ ___block_descriptor_48_e8_32r40r_e36_v40?0"UIColor"8{_NSRange=QQ}16^B32lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e9_16?0^8ls32l8w48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e35_v40?0"UIFont"8{_NSRange=QQ}16^B32ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e32_v24?0"NSMapTable"8"NSError"16ls32l8s40l8w64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e18_v24?0"NSSet"816lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s_e27_"UIImage"16?0"NSString"8ls32l8
+ ___block_literal_global.149
+ ___block_literal_global.39
+ ___block_literal_global.43
+ ___block_literal_global.56
+ ___block_literal_global.97
+ ___gxx_personality_v0
+ _defaultLayerGroup.counter
+ _defaultLayerGroup.onceToken
+ _defaultLayerGroup.textLayerGroups
+ _defaultSynchronousLegibilityImageGenerator.defaultSynchronousLegibilityImageGenerator
+ _defaultSynchronousLegibilityImageGenerator.onceToken
+ _kCTFontAttributeName
+ _kCTForegroundColorAttributeName
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_calculateAndCacheBaselinesWithFramesetter:intrinsicSize:
+ _objc_msgSend$_calculateInkBoundsForCTFrame:
+ _objc_msgSend$_calculatePropertiesHash
+ _objc_msgSend$_containsEmoji
+ _objc_msgSend$_defaultAttributes
+ _objc_msgSend$_defaultTextFill
+ _objc_msgSend$_drainPendingPrewarm
+ _objc_msgSend$_drawColorGlyphRun:origin:alpha:
+ _objc_msgSend$_drawGlyphRun:origin:alpha:blendMode:
+ _objc_msgSend$_effectiveConstraintWidthForBounds:
+ _objc_msgSend$_effectiveDisplayScale
+ _objc_msgSend$_ensureLayoutCacheIsValid
+ _objc_msgSend$_hasCustomFrameBounds
+ _objc_msgSend$_hasCustomTextRect
+ _objc_msgSend$_initializeLabel
+ _objc_msgSend$_initializeWithDefaults
+ _objc_msgSend$_intrinsicSizeForAttributedString:
+ _objc_msgSend$_invalidateAndRecalculateHash
+ _objc_msgSend$_invalidateGlyphCache
+ _objc_msgSend$_invalidateShadowCache
+ _objc_msgSend$_isConstrainedLayout
+ _objc_msgSend$_labelContentDidChange
+ _objc_msgSend$_labelContentHasUniformColor:outUniformColor:
+ _objc_msgSend$_layoutSubviews
+ _objc_msgSend$_measureSizeWithFramesetter:forAttributedString:withConstraints:numberOfLines:
+ _objc_msgSend$_performScheduledDisplay
+ _objc_msgSend$_rebuildCachedShadowContents
+ _objc_msgSend$_rebuildCachedTextContents
+ _objc_msgSend$_registerForTraitChanges
+ _objc_msgSend$_renderAllLayers
+ _objc_msgSend$_renderPendingLayers
+ _objc_msgSend$_resetLabelContent
+ _objc_msgSend$_resolvedLayoutByFittingString:toWidth:
+ _objc_msgSend$_resolvedLayoutForBounds:frameBounds:textRect:
+ _objc_msgSend$_scheduleDisplay
+ _objc_msgSend$_setNeedsShadowLayerDisplay
+ _objc_msgSend$_updateAccessibilityProperties
+ _objc_msgSend$_updateFont:forTraitCollection:
+ _objc_msgSend$_updateForTraitCollection
+ _objc_msgSend$_updateShadowLayerFilter
+ _objc_msgSend$_updateTextLayerColorMode
+ _objc_msgSend$_updateTextLayerFilter
+ _objc_msgSend$addAttribute:value:range:
+ _objc_msgSend$addCommitHandler:forPhase:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addShadowStyleWithRadius:offset:color:colorSpace:blendMode:flags:
+ _objc_msgSend$addSublayer:
+ _objc_msgSend$allowsDefaultTighteningForTruncation
+ _objc_msgSend$appendBool:withName:ifEqualTo:
+ _objc_msgSend$appendDouble:
+ _objc_msgSend$appendInteger:
+ _objc_msgSend$appendString:
+ _objc_msgSend$applyShadowStylesToDisplayList:renderScale:shadowRenderScale:textColor:
+ _objc_msgSend$array
+ _objc_msgSend$attribute:atIndex:effectiveRange:
+ _objc_msgSend$beginCGContextWithAlpha:
+ _objc_msgSend$beginLayerWithFlags:
+ _objc_msgSend$clearHasBeenCommitted
+ _objc_msgSend$colorMode
+ _objc_msgSend$colorWithCGColor:
+ _objc_msgSend$concat:
+ _objc_msgSend$contentMode
+ _objc_msgSend$contentsScale
+ _objc_msgSend$countLimit
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeCGRectForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultColorSpace
+ _objc_msgSend$defaultLayerGroup
+ _objc_msgSend$defaultMetrics
+ _objc_msgSend$differencesBetween:and:
+ _objc_msgSend$displayWithBounds:callback:
+ _objc_msgSend$drawAttributedString:inPath:alpha:blendMode:
+ _objc_msgSend$drawAttributedString:inRect:alpha:blendMode:
+ _objc_msgSend$drawCTFrame:alpha:blendMode:
+ _objc_msgSend$drawCTLine:origin:alpha:blendMode:
+ _objc_msgSend$drawCTRun:origin:alpha:blendMode:
+ _objc_msgSend$drawDisplayList:
+ _objc_msgSend$drawInDisplayList:bounds:blendMode:alpha:
+ _objc_msgSend$drawLayerWithAlpha:blendMode:
+ _objc_msgSend$drawShape:fill:alpha:blendMode:
+ _objc_msgSend$effectiveAttributedText
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeCGRect:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endCGContext
+ _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
+ _objc_msgSend$enumerateAttributesInRange:options:usingBlock:
+ _objc_msgSend$firstBaselineOffsetFromTop
+ _objc_msgSend$fontAttributes
+ _objc_msgSend$fontDescriptor
+ _objc_msgSend$fontDescriptorWithSymbolicTraits:
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$fontWithSize:
+ _objc_msgSend$frame
+ _objc_msgSend$getWhite:alpha:
+ _objc_msgSend$imageDynamicRange
+ _objc_msgSend$imageFutureForObject:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$initWithText:
+ _objc_msgSend$isDrawableAvailable
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEqualToAttributedString:
+ _objc_msgSend$isEqualToLabelContent:
+ _objc_msgSend$labelColor
+ _objc_msgSend$labelFontSize
+ _objc_msgSend$lastBaselineOffsetFromBottom
+ _objc_msgSend$legibilityDescriptorForSettings:strength:options:
+ _objc_msgSend$moveContents
+ _objc_msgSend$needsDisplay
+ _objc_msgSend$needsSynchronousUpdate
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$overflowEdgeInsets
+ _objc_msgSend$plk_rbColorWithAlpha:
+ _objc_msgSend$pointSize
+ _objc_msgSend$preferredFontForTextStyle:compatibleWithTraitCollection:
+ _objc_msgSend$registerForTraitChanges:withAction:
+ _objc_msgSend$restore
+ _objc_msgSend$save
+ _objc_msgSend$scaleByX:Y:
+ _objc_msgSend$scaledFontForFont:compatibleWithTraitCollection:
+ _objc_msgSend$screen
+ _objc_msgSend$setAccessibilityAttributedLabel:
+ _objc_msgSend$setAccessibilityLabel:
+ _objc_msgSend$setAccessibilityTraits:
+ _objc_msgSend$setAdjustsFontSizeToFitWidth:
+ _objc_msgSend$setAlignment:
+ _objc_msgSend$setAllowsDefaultTighteningForTruncation:
+ _objc_msgSend$setAllowsHitTesting:
+ _objc_msgSend$setAllowsPackedDrawable:
+ _objc_msgSend$setAsynchronousGroup:
+ _objc_msgSend$setAttributedText:
+ _objc_msgSend$setAttributes:range:
+ _objc_msgSend$setClearColor:
+ _objc_msgSend$setClearsBackground:
+ _objc_msgSend$setClipsToBounds:
+ _objc_msgSend$setColor:colorSpace:
+ _objc_msgSend$setColorMode:
+ _objc_msgSend$setContents:
+ _objc_msgSend$setContentsScale:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$setDisplayHeadroomLimit:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setGlyphs:positions:count:font:renderingStyle:
+ _objc_msgSend$setHDRMode:
+ _objc_msgSend$setIsAccessibilityElement:
+ _objc_msgSend$setLineBreakMode:
+ _objc_msgSend$setLineBreakStrategy:
+ _objc_msgSend$setMaxDrawableCount:
+ _objc_msgSend$setMinimumScaleFactor:
+ _objc_msgSend$setNeedsAsyncDisplay
+ _objc_msgSend$setNeedsDisplay
+ _objc_msgSend$setNumberOfLines:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOpaque:
+ _objc_msgSend$setOverflowEdgeInsets:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setProfile:
+ _objc_msgSend$setPromotesFramebuffer:
+ _objc_msgSend$setRendersAsynchronously:
+ _objc_msgSend$setShadowBlurRadius:
+ _objc_msgSend$setShadowColor:
+ _objc_msgSend$setShadowOffset:
+ _objc_msgSend$setText:
+ _objc_msgSend$setTextAlignment:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$setUserInteractionEnabled:
+ _objc_msgSend$setValue:forAttribute:
+ _objc_msgSend$sizeThatFits:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$superview
+ _objc_msgSend$symbolicTraits
+ _objc_msgSend$systemFontOfSize:
+ _objc_msgSend$systemFontSize
+ _objc_msgSend$textColor
+ _objc_msgSend$textRectForBounds:limitedToNumberOfLines:
+ _objc_msgSend$translateByX:Y:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$updateForTraitCollection:
+ _objc_msgSend$waitUntilAsyncRenderingCompleted
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_msgSend$window
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- +[PLKLegibilityDescriptor legibilityDescriptorForUILegibilitySettings:strength:]
- +[PLKShadowDescriptor classicDrawShadows:renderScale:color:context:]
- -[PLKCachedImageGenerator prewarmObjects:context:].cold.1
- -[PLKCachedImageGenerator removeImagesForCacheKeys:].cold.1
- -[PLKLegibilityBackgroundContentDescriptor renderScale]
- -[_PLKNSAttributedStringMetricsProvider plk_boundingRectForObject:maxSize:]
- GCC_except_table12
- GCC_except_table15
- GCC_except_table24
- GCC_except_table26
- GCC_except_table40
- GCC_except_table42
- GCC_except_table48
- _CGBitmapContextGetBytesPerRow
- _CGBitmapContextGetHeight
- _CGBitmapContextGetWidth
- _CGContextSetFillColorWithColor
- _NSLog
- _OBJC_CLASS_$__PLKNSAttributedStringMetricsProvider
- _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmInProgressFlag
- _OBJC_METACLASS_$__PLKNSAttributedStringMetricsProvider
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- __OBJC_$_INSTANCE_METHODS_PLKLegibilityDescriptor
- __OBJC_$_INSTANCE_METHODS__PLKNSAttributedStringMetricsProvider
- __OBJC_$_PROP_LIST__PLKNSAttributedStringMetricsProvider
- __OBJC_CLASS_PROTOCOLS_$__PLKNSAttributedStringMetricsProvider
- __OBJC_CLASS_RO_$__PLKNSAttributedStringMetricsProvider
- __OBJC_METACLASS_RO_$__PLKNSAttributedStringMetricsProvider
- ___120+[PLKCachedLegibilityContentDataSource attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:]_block_invoke.111
- ___50-[PLKCachedImageGenerator prewarmObjects:context:]_block_invoke.41
- ___50-[PLKCachedImageGenerator prewarmObjects:context:]_block_invoke.45
- ___52-[PLKCachedImageGenerator removeImagesForCacheKeys:]_block_invoke
- ___52-[PLKCachedImageGenerator removeImagesForCacheKeys:]_block_invoke.48
- ___52-[PLKCachedImageGenerator removeImagesForCacheKeys:]_block_invoke_2
- ___68+[PLKShadowDescriptor classicDrawShadows:renderScale:color:context:]_block_invoke
- ___68+[PLKShadowDescriptor classicDrawShadows:renderScale:color:context:]_block_invoke.8
- ___68+[PLKShadowDescriptor classicDrawShadows:renderScale:color:context:]_block_invoke_2
- ____prewarmContinuationScheduler_block_invoke
- ____removeContinuationScheduler_block_invoke
- ___block_descriptor_120_e8_32s40s48s56s64s72r_e27_"UIImage"16?0"NSString"8lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_140_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_48_e8_32s40w_e21_"<PFTFuture>"16?08ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48s_e18_16?0"NSString"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56w_e27_v24?0"NSSet"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e33_"<PFTFuture>"16?0"NSMapTable"8ls32l8s40l8w72l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s_e27_"UIImage"16?0"NSString"8ls32l8
- ___block_descriptor_84_e5_v8?0l
- ___block_literal_global.14
- ___block_literal_global.145
- ___block_literal_global.150
- ___block_literal_global.3
- ___block_literal_global.8
- ___block_literal_global.98
- __prewarmContinuationScheduler
- __prewarmContinuationScheduler.cold.1
- __prewarmContinuationScheduler.onceToken
- __prewarmContinuationScheduler.scheduler
- __removeContinuationScheduler.onceToken
- __removeContinuationScheduler.scheduler
- _objc_msgSend$_flatImageWithColor:
- _objc_msgSend$allObjects
- _objc_msgSend$bs_array
- _objc_msgSend$finishWithResult:
- _objc_msgSend$imageForObject:
- _objc_msgSend$initWithLegibilitySettings:strength:
- _objc_msgSend$keyEnumerator
- _objc_msgSend$plk_compatibleWithDescriptor:
- _vImageTentConvolve_ARGB8888
- _vImageTentConvolve_Planar8
CStrings:
+ "-[PLKCachedImageGenerator removeImagesForPredicate:]"
+ "@\"<PFTFuture>\"16@?0@\"NSSet\"8"
+ "Cannot adjust font size: attributed string has no font attribute."
+ "Cannot calculate size, failed to resolve layout."
+ "Could not retrieve UILabel default attributes. Using provided attributed string as-is."
+ "Failed to create CTFramesetter."
+ "Failed to create final framesetter for adjusted string."
+ "Failed to create temporary frame for baseline calculation."
+ "Failed to create temporary framesetter for intrinsic sizing."
+ "HasExtendedColorDisplay"
+ "Invalid configuration: textRect must fit within frameBounds. frameBounds: %@, textRect: %@"
+ "Layout cache is invalid, recalculating."
+ "Line height calculation: topY=%.2f, bottomY=%.2f, calculatedHeight=%.2f, originalHeight=%.2f"
+ "Line measurement: lineCount=%ld, lineLimit=%ld"
+ "Line-limited measurement: limit=%ld, final size=%.2fx%.2f"
+ "No line limiting needed: lineCount=%ld <= lineLimit=%ld"
+ "PLKLabel _rebuildCachedShadowContents: SKIPPED - no cachedTextContents"
+ "PLKLabel _rebuildCachedTextContents: SKIPPED - labelContent=%{public}@ bounds=%{public}@"
+ "PLKLabel _renderPendingLayers: RENDERING TEXT WITH NO CONTENTS - viewBounds=%{public}@ text='%{public}@'"
+ "PLKLabelContent zero height bug: typographicSize=%@, constrainedTextSize=%@, numberOfLines=%ld, string length=%lu"
+ "Updated fonts for trait collection changes"
+ "Using effective constraint width %.1f instead of bounds width %.1f for font adjustment"
+ "_allowsDefaultTighteningForTruncation"
+ "_frameBounds"
+ "_textAlignment"
+ "_textColor"
+ "_textRect"
+ "adjustsFontSizeToFitWidth: %d vs %d"
+ "allowsDefaultTighteningForTruncation"
+ "allowsDefaultTighteningForTruncation: %d vs %d"
+ "attributedText: '%@' vs '%@'"
+ "com.apple.PLKLabelContent.AdjustedCache.%p"
+ "com.apple.PLKLabelContent.LayoutCache.%p"
+ "com.apple.PLKLabelContent.SizeCache.%p"
+ "font: %@ vs %@"
+ "frameBounds: %@ vs %@"
+ "hash: %lu vs %lu"
+ "lhs is nil"
+ "lineBreakMode: %ld vs %ld"
+ "lineBreakStrategy: %lu vs %lu"
+ "minimumScaleFactor: %.4f vs %.4f"
+ "numberOfLines: %ld vs %ld"
+ "overflowEdgeInsets: %@ vs %@"
+ "rhs is nil"
+ "text: '%@' vs '%@'"
+ "textAlignment: %ld vs %ld"
+ "textColor"
+ "textColor: %@ vs %@"
+ "textRect: %@ vs %@"
+ "v16@?0@\"RBDisplayList\"8"
+ "v24@?0@\"NSMapTable\"8@\"NSError\"16"
+ "v24@?0@\"NSSet\"8@16"
+ "v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32"
+ "v40@?0@\"UIColor\"8{_NSRange=QQ}16^B32"
+ "v40@?0@\"UIFont\"8{_NSRange=QQ}16^B32"
+ "v40@?0@8{_NSRange=QQ}16^B32"
- "#16@0:8"
- "-[PLKCachedImageGenerator(%@%p) prewarmObjects: bailing, prewarm already in progress]"
- "-[PLKCachedImageGenerator(%@%p) prewarmed %@]"
- "-[PLKCachedImageGenerator(%@%p) prewarming %@]"
- "-[PLKCachedImageGenerator(%@%p) prewarming key]"
- "-[PLKCachedImageGenerator(%p) Setting up with cache %{public}@"
- ".cxx_destruct"
- "<%{public}@:%p initWithContentGenerator:legibilityGenerator:>"
- "<%{public}@:%p prewarmContentForObjects:%@ legibilityDescriptors:%{public}@>"
- "<%{public}@:%p removeAllObjects>"
- "<%{public}@:%p removeContentForObjects:%lu legibilityDescriptors:%{public}@>"
- "<PLKImageRenderer:%p imageWithActions>"
- "<PLKImageRenderer:%p imageWithRenderable:%@>"
- "@"
- "@\"<BSPathProviding>\""
- "@\"<NSObject>\""
- "@\"<NSObject>\"16@0:8"
- "@\"<PFTFuture>\"16@?0@\"NSMapTable\"8"
- "@\"<PFTFuture>\"16@?0@8"
- "@\"<PFTScheduler>\""
- "@\"<UITraitChangeRegistration>\""
- "@\"BSAtomicFlag\""
- "@\"BSAtomicSignal\""
- "@\"BSMutableOrderedDictionary\""
- "@\"BSUIMappedImageCache\""
- "@\"BSUIMappedImageCache\"16@0:8"
- "@\"CPMemoryPool\""
- "@\"NSArray\""
- "@\"NSAttributedString\""
- "@\"NSDateInterval\""
- "@\"NSDictionary\""
- "@\"NSMapTable\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSOperationQueue\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\"16@0:8"
- "@\"NSValue\""
- "@\"PFTFuture\""
- "@\"PLKColorBoxes\""
- "@\"PLKImageGenerator\""
- "@\"PLKLRUCache\""
- "@\"PLKLegibilityBackgroundContentDescriptor\""
- "@\"PLKLegibilityContent\""
- "@\"PLKLegibilityContentDataSource\""
- "@\"PLKLegibilityDescriptor\""
- "@\"PLKLegibilityForegroundContentDescriptor\""
- "@\"UIColor\""
- "@\"UIColor\"16@0:8"
- "@\"UIColor\"48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@\"UIFont\""
- "@\"UIImage\""
- "@\"_PFTImageView\""
- "@\"_PLKLegibilityContainerView\""
- "@\"_UILegibilitySettings\""
- "@\"_UILegibilitySettings\"16@0:8"
- "@104@0:8{CAColorMatrix=ffffffffffffffffffff}16@96"
- "@104@0:8{CAColorMatrix=ffffffffffffffffffff}16q96"
- "@112@0:8{CAColorMatrix=ffffffffffffffffffff}16@96d104"
- "@16@0:8"
- "@16@?0@\"NSString\"8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8o^@16"
- "@24@0:8o^d16"
- "@24@0:8q16"
- "@28@0:8Q16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8@16d24"
- "@32@0:8Q16Q24"
- "@32@0:8d16@24"
- "@32@0:8q16d24"
- "@32@0:8q16q24"
- "@32@0:8{CGSize=dd}16"
- "@36@0:8{CGSize=dd}16B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24d32"
- "@40@0:8@16@?24@?32"
- "@40@0:8@16d24@32"
- "@40@0:8@16d24d32"
- "@40@0:8@16d24q32"
- "@40@0:8Q16@24@32"
- "@40@0:8d16q24@32"
- "@40@0:8d16{CGSize=dd}24"
- "@40@0:8q16d24@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24Q32@40"
- "@48@0:8@16Q24@32@40"
- "@48@0:8@16Q24d32@40"
- "@48@0:8@16d24d32@40"
- "@48@0:8d16{CGSize=dd}24d40"
- "@48@0:8{?={CGSize=dd}dq}16"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@48@0:8{CGSize=dd}16d32@40"
- "@48@0:8{CGSize=dd}16d32q40"
- "@56@0:8d16{CGSize=dd}24d40d48"
- "@56@0:8{CGSize=dd}16d32@40@48"
- "@56@0:8{CGSize=dd}16d32q40@48"
- "@64@0:8@16Q24@32d40d48@56"
- "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48"
- "@64@0:8{CGSize=dd}16d32q40@48@?56"
- "@68@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48B64"
- "@72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48B64B68"
- "@80@0:8@16Q24@32d40d48@56@64@72"
- "@96@0:8{CAColorMatrix=ffffffffffffffffffff}16"
- "@?"
- "@?16@0:8"
- "Aixt/MEN2O2B7f+8m4TxUA"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B40@0:8@16d24@32"
- "B48@0:8@16d24d32@40"
- "B48@0:8{?={CGSize=dd}dq}16"
- "BSCancellable"
- "BSDescriptionStreamable"
- "BSInvalidatable"
- "BSPathProviding"
- "C"
- "CAColorMatrixValue"
- "CGColor"
- "CGImage"
- "CGRectValue"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSObjectOverride"
- "NSSecureCoding"
- "PLK view alignment offset: insets=%@, offset=(%.2f, %.2f)"
- "PLKAdditions"
- "PLKBackdropAwareTrait"
- "PLKCacheProvider"
- "PLKCacheProviding"
- "PLKCachedImageGenerator-prewarm-continuation"
- "PLKCachedImageGenerator-remove-continuation"
- "PLKCachedLegibilityContentDataSource"
- "PLKColorBoxes"
- "PLKImageGenerator"
- "PLKImageRenderable"
- "PLKImageRenderableAdditions"
- "PLKImageRenderer"
- "PLKImageRendererContext"
- "PLKImageRendererFormat"
- "PLKLRUCache"
- "PLKLegibilityAdditions"
- "PLKLegibilityBackgroundContentDescriptor"
- "PLKLegibilityContent"
- "PLKLegibilityContentDataSource"
- "PLKLegibilityContentDescriptor"
- "PLKLegibilityContext"
- "PLKLegibilityDescriptor"
- "PLKLegibilityEnvironment"
- "PLKLegibilityEnvironmentBuilder"
- "PLKLegibilityEnvironmentContext"
- "PLKLegibilityEnvironmentVariantContext"
- "PLKLegibilityForegroundContentDescriptor"
- "PLKLegibilityImageRenderer"
- "PLKLegibilityLabelView"
- "PLKLegibilityView"
- "PLKMetricsProviding"
- "PLKShadowDescriptor"
- "PLKUILegibilitySettingsBackgroundContentDescriptor"
- "PLKUtilities"
- "PosterLegibilityKitAdditions"
- "Q16@0:8"
- "SBHAdditions"
- "T#,R"
- "T@\"<BSPathProviding>\",R,N,V_mappedImageCachePathProvider"
- "T@\"<NSObject>\",&,N,V_compositingFilter"
- "T@\"<NSObject>\",&,N,V_content"
- "T@\"<NSObject>\",R,N"
- "T@\"<PFTScheduler>\",&,V_keyScheduler"
- "T@\"<PFTScheduler>\",&,V_workScheduler"
- "T@\"BSUIMappedImageCache\",?,R,N"
- "T@\"BSUIMappedImageCache\",?,R,N,V_contentCache"
- "T@\"BSUIMappedImageCache\",?,R,N,V_legibilityCache"
- "T@\"BSUIMappedImageCache\",R,N,V_cache"
- "T@\"CPMemoryPool\",R,N,V_memoryPool"
- "T@\"NSArray\",R,N,V_shadows"
- "T@\"NSAttributedString\",R,C,N,V_attributedText"
- "T@\"NSDateInterval\",R,N,V_generationInterval"
- "T@\"NSDictionary\",C,N,V_userInfo"
- "T@\"NSDictionary\",R,C,N,V_userInfo"
- "T@\"NSDictionary\",R,C,N,V_variantToContextProvider"
- "T@\"NSNumber\",C,V_defaultPersistenceOptions"
- "T@\"NSNumber\",R,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,N"
- "T@\"NSString\",C,V_label"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_cacheIdentifier"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_contentCacheIdentifier"
- "T@\"NSString\",R,N,V_legibilityCacheIdentifier"
- "T@\"NSString\",R,N,V_variant"
- "T@\"NSURL\",R,N"
- "T@\"PFTFuture\",R,N,V_contentImageFuture"
- "T@\"PFTFuture\",R,N,V_legibilityImageFuture"
- "T@\"PLKCachedImageGenerator\",&,D,N"
- "T@\"PLKImageGenerator\",&,N,V_contentGenerator"
- "T@\"PLKImageGenerator\",&,N,V_legibilityGenerator"
- "T@\"PLKImageRendererFormat\",R,D,N"
- "T@\"PLKLegibilityBackgroundContentDescriptor\",R,N,V_background"
- "T@\"PLKLegibilityContent\",&,N,V_content"
- "T@\"PLKLegibilityContent\",R,N"
- "T@\"PLKLegibilityContentDataSource\",W,N,V_dataSource"
- "T@\"PLKLegibilityContext\",R,N"
- "T@\"PLKLegibilityDescriptor\",R,N,V_legibilityDescriptor"
- "T@\"PLKLegibilityForegroundContentDescriptor\",R,N,V_foreground"
- "T@\"UIColor\",R,D,N"
- "T@\"UIColor\",R,N"
- "T@\"UIColor\",R,N,V_averageColor"
- "T@\"UIColor\",R,N,V_backgroundColor"
- "T@\"UIColor\",R,N,V_contentColor"
- "T@\"UIColor\",R,N,V_primaryColor"
- "T@\"UIColor\",R,N,V_secondaryColor"
- "T@\"UIImage\",&,N,V_overrideCurrentImage"
- "T@\"UIImage\",R,N"
- "T@\"UIView\",R,N,V_contentView"
- "T@\"UIView\",R,N,V_shadowView"
- "T@\"_UILegibilitySettings\",R,N"
- "T@\"_UILegibilitySettings\",R,N,V_legibilitySettings"
- "T@,R,N,V_context"
- "T@,R,N,V_object"
- "T@?,R,C,N,V_imageGenerator"
- "T@?,R,C,N,V_keyGenerator"
- "TB,?,R,N"
- "TB,D,N"
- "TB,N,SsetBackdropAware:,V_isBackdropAware"
- "TB,N,SsetTraitBasedBackdropAwarenessEnabled:,V_isTraitBasedBackdropAwarenessEnabled"
- "TB,N,V_hideForegroundContent"
- "TB,N,V_usesContentAlignmentRectInsets"
- "TB,R"
- "TB,R,N"
- "TB,V_collectStatistics"
- "TQ,N,V_alignmentMode"
- "TQ,N,V_capacity"
- "TQ,R"
- "TQ,R,D,N"
- "TQ,R,N"
- "TQ,R,N,V_numberOfBytes"
- "TQ,R,N,V_preferredCacheCapacity"
- "TQ,R,N,V_style"
- "T^{CGColorSpace=},R,N,V_colorSpace"
- "Td,R,N"
- "Td,R,N,V_alpha"
- "Td,R,N,V_contrast"
- "Td,R,N,V_displayScale"
- "Td,R,N,V_luma"
- "Td,R,N,V_radius"
- "Td,R,N,V_saturation"
- "Td,R,N,V_shadowRenderScale"
- "Td,R,N,V_strength"
- "Tq,R,N,V_contextType"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentRect"
- "T{CGSize=dd},R,N,V_offset"
- "T{UIEdgeInsets=dddd},N,V_shadowAlignmentInsets"
- "UIObjectTraitDefinition"
- "UITraitDefinition"
- "UTF8String"
- "Vv16@0:8"
- "^{?=CCCCC}"
- "^{CGColorSpace=}"
- "^{CGColorSpace=}16@0:8"
- "^{CGContext=}24@0:8@16"
- "^{_NSZone=}16@0:8"
- "_LRUCache"
- "_PFTImageView"
- "_PLKDontAllowGroupOpacityOrGroupBlendingLayer"
- "_PLKImageGenerationContext"
- "_PLKLegibilityContainerView"
- "_PLKNSAttributedStringMetricsProvider"
- "_PLKUILabelCacheKey"
- "_UILegibilitySettings"
- "__PLKLRUCacheKeyTuple"
- "_activeContentImageFuture"
- "_activeLegibilityImageFuture"
- "_alignment"
- "_alignmentMode"
- "_asyncUpdateCounter"
- "_attrString"
- "_averageColor"
- "_backdropAwarenessTraitRegistration"
- "_background"
- "_backgroundColor"
- "_cache"
- "_cacheHash"
- "_cacheIdentifier"
- "_cacheKey"
- "_cacheKeyFutureLRUCache"
- "_cacheKeyFutureLock"
- "_cachedHash"
- "_cachedMaxShadowRadius"
- "_cachedMaxXOffset"
- "_cachedMaxYOffset"
- "_cachedMinXOffset"
- "_cachedMinYOffset"
- "_capacity"
- "_collectStatistics"
- "_colorBoxes"
- "_colorBoxesRowMajor"
- "_colorSpace"
- "_columnCount"
- "_commonInit"
- "_compositingFilter"
- "_containerView"
- "_content"
- "_contentCache"
- "_contentCacheIdentifier"
- "_contentGenerator"
- "_contentImageFuture"
- "_contentRect"
- "_contentView"
- "_context"
- "_contextType"
- "_contrast"
- "_currentOptions"
- "_dataSource"
- "_defaultPathProvider"
- "_defaultPersistenceOptions"
- "_displayScale"
- "_downsampledBoxSize"
- "_drawImageForLegibilitySettings:strength:size:alphaOnly:"
- "_effectiveDownsampleFactor"
- "_flatImageWithColor:"
- "_foreground"
- "_generateLegibilityDescriptor"
- "_generationInterval"
- "_hash"
- "_hideForegroundContent"
- "_imageFutureLRUCache"
- "_imageFutureLock"
- "_imageGenerator"
- "_imageSize"
- "_initWithIOSurface:scale:orientation:"
- "_invalidationSignal"
- "_isBackdropAware"
- "_isSimilarToColor:withinPercentage:"
- "_isTraitBasedBackdropAwarenessEnabled"
- "_keyGenerator"
- "_keyScheduler"
- "_knownMappedImageCacheKeys"
- "_label"
- "_labelBounds"
- "_legibilityCache"
- "_legibilityCacheIdentifier"
- "_legibilityDescriptor"
- "_legibilityGenerator"
- "_legibilityImageFuture"
- "_legibilityImageSizeForSize:style:"
- "_legibilitySettings"
- "_luma"
- "_luminance"
- "_luminanceWithRed:green:blue:"
- "_mappedImageCache"
- "_mappedImageCachePathProvider"
- "_memoryPool"
- "_memoryWarningDidFire:"
- "_numberOfBytes"
- "_object"
- "_overrideCurrentImage"
- "_pixelHeight"
- "_pixelWidth"
- "_poolBackedImage:pool:scale:"
- "_preferredCacheCapacity"
- "_prewarmInProgressFlag"
- "_prewarmLock"
- "_prewarmScheduler"
- "_prewarmScheduler_perwarmingCacheKeys"
- "_primaryColor"
- "_propertyLock"
- "_registerCreatedImage:startDate:numberOfBytes:userInfo:"
- "_rowCount"
- "_saturation"
- "_saturationCalculated"
- "_setLegibilityNeedsUpdate:"
- "_shadowAlignmentInsets"
- "_shadowRenderScale"
- "_shadowView"
- "_shadows"
- "_shouldAnimatePropertyWithKey:"
- "_shouldBeBackdropAware"
- "_size"
- "_statisticScheduler"
- "_statisticsMapTable"
- "_statisticsOperationQueue"
- "_storage"
- "_stringKey"
- "_style"
- "_totalContrast8"
- "_totalSaturation8"
- "_updateContentViewForLegibilityChanges"
- "_updateShadowViewForLegibilityChanges"
- "_updateTraitBasedBackdropAwareness"
- "_updateWithColorBoxes:"
- "_userInfo"
- "_usesContentAlignmentRectInsets"
- "_variant"
- "_variantToContextDictionary"
- "_variantToContextProvider"
- "_version"
- "_workScheduler"
- "accumulateChangesToContentColor:contrast:"
- "activityWrapping:"
- "addCompletionBlock:"
- "addCompletionBlock:scheduler:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addOperations:waitUntilFinished:"
- "addSubview:"
- "addSuccessBlock:"
- "affectsColorAppearance"
- "alignmentMode"
- "alignmentRectInsets"
- "allKeys"
- "allObjects"
- "allocWithZone:"
- "allocationSize"
- "allowsImageOutput"
- "alpha"
- "anchorPoint"
- "appendBool:"
- "appendBool:withName:"
- "appendCGFloat:"
- "appendCGRect:"
- "appendDescriptionToFormatter:"
- "appendFloat:"
- "appendFloat:withName:"
- "appendFormat:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPointer:withName:"
- "appendProem:block:"
- "appendString:withName:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUnsignedInteger:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attributedStringContentDataSource"
- "attributedStringContentDataSourceForMaxSize:scale:cacheProvider:"
- "attributedStringContentDataSourceForMaxSize:scale:cacheProvider:metricsProvider:"
- "attributedStringContentDataSourceForScale:metricsProvider:"
- "autorelease"
- "averageColorInRect:"
- "backgroundView"
- "baseAddress"
- "blackColor"
- "blockOperationWithBlock:"
- "boolForKey:"
- "boolValue"
- "boundingRectWithSize:options:context:"
- "bounds"
- "bs_array"
- "bs_filter:"
- "bs_mapNoNulls:"
- "bs_safeAddObject:"
- "bs_setSafeObject:forKey:"
- "build"
- "buildLegibilityImageGenerator"
- "buildWithError:"
- "builder"
- "builderWithObject:"
- "bytes"
- "bytesPerRow"
- "cache"
- "cacheIdentifier"
- "cacheKeyForLabel:"
- "cacheKeyFutureForObject:context:"
- "cachesPath"
- "cancel"
- "cancelledFuture"
- "capacity"
- "center"
- "class"
- "classicDrawShadows: memoryPool incompatible for shadow %{public}@ @%.0fx"
- "classicDrawShadows:renderScale:color:context:"
- "clearColor"
- "clearContentColorAccumulator"
- "collectStatistics"
- "colorBoxesForAverageColor:"
- "colorBoxesForAverageColor:contrast:"
- "colorBoxesForImage:"
- "colorSpace"
- "colorWithAlphaComponent:"
- "colorWithRed:green:blue:alpha:"
- "componentsJoinedByString:"
- "configureCALayer:forContentRenderedWithContextType:options:"
- "conformsToProtocol:"
- "containsObject:"
- "containsValueForKey:"
- "content"
- "contentColor"
- "contentDescriptorForColor:"
- "contentDescriptorForColor:shadows:"
- "contentDescriptorForColor:shadows:renderScale:"
- "contentDescriptorForPrimaryColor:secondaryColor:"
- "contentDescriptorForVibrantColorMatrix:shadows:"
- "contentDescriptorForVibrantColorMatrix:shadows:renderScale:"
- "contentImageIfFinished"
- "contentRect"
- "context"
- "contextForVariant"
- "contextType"
- "contextWithFormat:"
- "contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:"
- "contextWithStartDate:endDate:numberOfBytes:userInfo:"
- "contrastInRect:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentImage"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "dataSource"
- "dataUsingEncoding:"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decodeBytesForKey:returnedLength:"
- "decodeCGSizeForKey:"
- "decodeFloatForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decrementUseCount"
- "defaultCenter"
- "defaultContentDescriptor"
- "defaultContext"
- "defaultLegibilityDescriptor"
- "defaultLegibilityDescriptorForStyle:"
- "defaultLegibilityImageGenerator"
- "defaultPath"
- "defaultPersistenceOptions"
- "defaultValue"
- "defaultWorkScheduler"
- "defaultsToTraitBasedBackdropAwarenessEnabled"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "dictionaryWithObjects:forKeys:count:"
- "displayScale"
- "doesNotRecognizeSelector:"
- "doubleForKey:"
- "doubleValue"
- "drawAtPoint:"
- "drawInRect:"
- "drawInRect:blendMode:alpha:"
- "drawShadows:forImage:contentRect:renderScale:color:"
- "drawShadows:renderScale:color:context:"
- "drawTextInRect:"
- "duration"
- "effectiveUILegibilitySettings:"
- "encodeBytes:length:forKey:"
- "encodeCGSize:forKey:"
- "encodeFloat:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "filterUsingPredicate:"
- "filterWithType:"
- "filtersForContextType:options:"
- "finishWithResult:"
- "firstObject"
- "flatMap:"
- "flatMap:continuationScheduler:"
- "foregroundView"
- "format"
- "formatForContextType:"
- "formatForContextType:scale:"
- "formatForContextType:scale:memoryPool:"
- "futureWithBlock:"
- "futureWithBlock:scheduler:"
- "futureWithResult:"
- "generationInterval"
- "getRed:green:blue:alpha:"
- "hasBeenSignalled"
- "hash"
- "height"
- "hideForegroundContent"
- "identifier"
- "image"
- "imageForCacheKey:"
- "imageForKey:"
- "imageForKey:generatingIfNecessaryWithBlock:"
- "imageForKey:generatingIfNil:"
- "imageForObject:"
- "imageForObject:context:"
- "imageFutureForCacheKey:"
- "imageFutureForObject:"
- "imageFutureForObject:context:"
- "imageFutureForObject:persistenceOptions:context:"
- "imageGenerator"
- "imageOrientation"
- "imageWithActions:"
- "imageWithCGImage:scale:orientation:"
- "imageWithRenderable:"
- "incrementUseCount"
- "init"
- "initWithCGImage:scale:orientation:"
- "initWithCache:keyGenerator:imageGenerator:"
- "initWithCacheIdentifier:preferredCacheCapacity:displayScale:cacheProvider:"
- "initWithCapacity:"
- "initWithCapacity:keyOrderingStrategy:"
- "initWithCoder:"
- "initWithContentCache:legibilityCache:"
- "initWithContentCacheIdentifier:legibilityCacheIdentifier:"
- "initWithContentCacheIdentifier:legibilityCacheIdentifier:pathProvider:"
- "initWithContentColor:"
- "initWithContentGenerator:"
- "initWithContentGenerator:legibilityGenerator:"
- "initWithContentImage:legibilityDescriptor:"
- "initWithContentImage:legibilityDescriptor:renderer:"
- "initWithContentImageFuture:legibilityDescriptor:"
- "initWithContentImageFuture:legibilityDescriptor:renderer:"
- "initWithContentImageFuture:legibilityImageFuture:legibilityDescriptor:"
- "initWithDictionary:copyItems:"
- "initWithDictionary:userInfo:"
- "initWithEnvironment:"
- "initWithFlag:"
- "initWithForegroundContentDescriptor:backgroundContentDescriptor:"
- "initWithFrame:"
- "initWithImageGenerator:"
- "initWithLabel:slotLength:"
- "initWithLegibilitySettings:strength:"
- "initWithObject:context:"
- "initWithPrimaryColor:secondaryColor:"
- "initWithRadius:offset:alpha:strength:"
- "initWithScale:contextType:memoryPool:"
- "initWithSize:format:"
- "initWithStartDate:endDate:"
- "initWithStyle:"
- "initWithStyle:foregroundContentDescriptor:backgroundContentDescriptor:"
- "initWithStyle:primaryColor:secondaryColor:shadowColor:"
- "initWithUniqueIdentifier:options:"
- "initWithVariant:colorBoxes:"
- "initWithVariant:image:"
- "initWithVariant:style:averageColor:contrast:saturation:legibilitySettings:"
- "initWithVariant:style:averageColor:contrast:saturation:primaryColor:secondaryColor:backgroundColor:"
- "initWithVariant:style:colorBoxes:legibilitySettings:"
- "inlineScheduler"
- "intrinsicContentSize"
- "invalidate"
- "invalidateIntrinsicContentSize"
- "ioSurface"
- "isBackdropAware"
- "isEqual:"
- "isEqualToColorBoxes:"
- "isEqualToLegibilityContent:"
- "isEqualToLegibilityDescriptor:"
- "isEqualToShadow:"
- "isEqualToString:"
- "isFinished"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTraitBasedBackdropAwarenessEnabled"
- "isValidCacheKeyForObject:context:"
- "join:"
- "keyEnumerator"
- "keyGenerator"
- "keyScheduler"
- "label"
- "labelLegibilityImageGenerator"
- "layer"
- "layerClass"
- "layoutIfNeeded"
- "layoutSubviews"
- "legibilityContentForAttributedString:legibilityDescriptor:"
- "legibilityContentForImage:legibilityDescriptor:"
- "legibilityContentForImage:legibilityDescriptor:renderer:"
- "legibilityContentForLabel:legibilityDescriptor:"
- "legibilityContentForLabel:legibilityDescriptor:context:"
- "legibilityContentForLabel:legibilityDescriptor:context:renderer:"
- "legibilityContentForObject:legibilityDescriptor:"
- "legibilityContextForVariant:"
- "legibilityDescriptorForEnvironmentContext:"
- "legibilityDescriptorForSettings:strength:"
- "legibilityDescriptorForUILegibilitySettings:strength:"
- "legibilityDescriptorForVariant:"
- "legibilityEnvironmentContextForVariant:"
- "legibilityEnvironmentForAverageColor:contrast:"
- "legibilityEnvironmentForAverageColor:contrast:saturation:"
- "legibilityEnvironmentForAverageColor:contrast:saturation:variants:"
- "legibilityEnvironmentForAverageColor:contrast:variants:"
- "legibilityEnvironmentForImage:"
- "legibilityEnvironmentForImage:variants:"
- "legibilityEnvironmentForUILegibilitySettings:"
- "legibilityEnvironmentForUILegibilitySettings:variant:"
- "legibilityEnvironmentWithDictionary:userInfo:"
- "legibilityGenerator"
- "legibilityImageFuture"
- "length"
- "libraryPath"
- "lockWithOptions:seed:"
- "luma"
- "lumaInRect:"
- "magentaColor"
- "mainConfiguration"
- "mainScreen"
- "mainThreadScheduler"
- "mappedImageCachePathProvider"
- "memoryPool"
- "mutableCopy"
- "name"
- "needsDisplayForKey:"
- "new"
- "nextSlotWithBytes:length:"
- "noContent"
- "noteBackdropAwarenessTraitDidUpdate"
- "numberOfBytes"
- "numberOfBytesGenerated"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKey:ifNil:"
- "objectForKeyedSubscript:"
- "objectForTrait:"
- "offMainThreadSchedulerWithBackgroundScheduler:"
- "offset"
- "opaque"
- "operationQueueSchedulerWithMaxConcurrentOperationCount:qualityOfService:name:"
- "operationQueueSchedulerWithOperationQueue:qualityOfService:"
- "optionsWithContainerPathProvider:"
- "overrideCurrentImage"
- "pathProviderForCurrentContainer"
- "performBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performanceLegibilityDescriptorForStyle:"
- "performanceLegibilityDescriptorForStyle:options:"
- "pixelFormat"
- "plk_CGImageBackedImage"
- "plk_CGImageBackedImageWithMaximumBitsPerComponent:"
- "plk_CGImageBackedImageWithMaximumBitsPerComponent:skipCIF10FitsInSRGBCheck:"
- "plk_alphaMaskImage"
- "plk_boundingRectForObject:maxSize:"
- "plk_colorSpace"
- "plk_compatibleWithDescriptor:"
- "plk_contentCache"
- "plk_contentCacheIdentifier"
- "plk_cropImageWithRect:outputSize:"
- "plk_cropImageWithRect:outputSize:canUseIOSurface:"
- "plk_cropImageWithRect:outputSize:preservingAspectRatio:"
- "plk_cropImageWithRect:outputSize:preservingAspectRatio:canUseIOSurface:"
- "plk_imageFromContextWithSize:scale:type:pool:drawing:"
- "plk_imageWithIOSurface:scale:orientation:"
- "plk_isAlphaMask"
- "plk_isPLKImageRendererFormat"
- "plk_legibilityCache"
- "plk_legibilityCacheIdentifier"
- "plk_multiplyColor:"
- "plk_renderWithContext:"
- "plk_resizeImageToSize:"
- "plk_resizeImageToSize:preservingAspectRatio:"
- "plk_setBoundsAndPositionFromFrame:"
- "plk_sha256Hash"
- "plk_sha256Hash:"
- "plk_sha256HashForObject:error:"
- "plk_sharedMemoryPoolForDescriptor:"
- "plk_sharedMemoryPoolForMaxSize:scale:contextType:"
- "plk_shouldBeBackdropAware"
- "plk_stringFromCAColorMatrix:"
- "plk_traitCollectionNotingShouldBeBackdropAware:"
- "plk_vibrantColorMatrixFilterWithVibrantColorMatrix:options:"
- "plk_wrappedIOSurface"
- "pointScale"
- "predicateWithValue:"
- "preferredCacheCapacity"
- "preferredFormat"
- "prepareCGContext:withRendererContext:"
- "prewarmContentForObjects:legibilityDescriptors:"
- "prewarmObjects:context:"
- "q"
- "q16@0:8"
- "radius"
- "registerForTraitChanges:withTarget:action:"
- "release"
- "removeAllImagesWithCompletion:"
- "removeAllObjects"
- "removeAllObjectsWithCompletion:"
- "removeContentForObjects:legibilityDescriptors:"
- "removeImageForKey:withCompletion:"
- "removeImagesForCacheKeys:"
- "removeImagesForPredicate:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeVariant:"
- "renderLegibilityImageDecoratingImage:actions:"
- "renderLegibilityImageForImage:legibilityDescriptor:"
- "rendererContextClass"
- "respondsToSelector:"
- "result:"
- "retain"
- "retainCount"
- "runUntilDate:"
- "saturationInRect:"
- "scale"
- "self"
- "serialDispatchQueueSchedulerWithName:"
- "set"
- "setAlignmentMode:"
- "setAllowsGroupBlending:"
- "setAllowsGroupOpacity:"
- "setAttachment:forKey:"
- "setAttributedText:legibilityDescriptor:"
- "setAutoresizingMask:"
- "setBackdropAware:"
- "setBounds:"
- "setCapacity:"
- "setCenter:"
- "setCollectStatistics:"
- "setCompositingFilter:"
- "setContent:"
- "setContentGenerator:"
- "setContentRect:"
- "setCountStyle:"
- "setDataSource:"
- "setDefaultPersistenceOptions:"
- "setFill"
- "setFilters:"
- "setFlag:"
- "setFrame:"
- "setHidden:"
- "setHideForegroundContent:"
- "setImage:"
- "setImage:forKey:"
- "setKeyScheduler:"
- "setLabel:"
- "setLegibilityGenerator:"
- "setMaxConcurrentOperationCount:"
- "setName:"
- "setNeedsLayout"
- "setObject:forKey:"
- "setObject:forTrait:"
- "setOverrideCurrentImage:"
- "setScale:"
- "setShadowAlignmentInsets:"
- "setShadowImage:"
- "setShouldRasterize:"
- "setTraitBasedBackdropAwarenessEnabled:"
- "setUserInfo:"
- "setUsesContentAlignmentRectInsets:"
- "setValue:forKey:"
- "setWithArray:"
- "setWithObject:"
- "setWorkScheduler:"
- "settings"
- "shadowAlignmentInsets"
- "shadowAlpha"
- "shadowColor"
- "shadowImage"
- "shadowRadius"
- "shadowWithRadius:"
- "shadowWithRadius:offset:"
- "shadowWithRadius:offset:alpha:"
- "shadowWithRadius:offset:alpha:strength:"
- "sharedFormatForLegibilityWithMaximumSize:scale:contentType:legibilityDescriptor:"
- "sharedInstanceForStyle:"
- "signal"
- "sizeForContentSize:"
- "sizeToFit"
- "slotLength"
- "sortByInsertionOrder"
- "standardUserDefaults"
- "string"
- "stringByAppendingString:"
- "stringFromByteCount:"
- "stringKey"
- "stringWithCapacity:"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "strongToWeakObjectsMapTable"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "supportsSecureCoding"
- "synchonrouslyRemoveAllObjects"
- "systemGrayColor"
- "systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:"
- "track"
- "trackWithActivity:"
- "traitCollection"
- "traitCollectionWithTraits:"
- "unlockWithOptions:seed:"
- "unregisterForTraitChanges:"
- "unsignedIntValue"
- "updateWithAverageColor:contrast:saturation:variants:"
- "updateWithAverageColor:contrast:variants:"
- "updateWithContext:"
- "updateWithContext:variants:"
- "updateWithLegibilitySettings:contrast:saturation:variants:"
- "updateWithLegibilitySettings:variants:"
- "userCanceledError"
- "userInfo"
- "usesContentAlignmentRectInsets"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<BSDescriptionFormatting>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"PLKImageRendererContext\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@?0@\"NSSet\"8@\"NSError\"16"
- "v32@0:8@16@24"
- "v32@0:8^{CGContext=}16@24"
- "v40@0:8@16q24q32"
- "v48@0:8@16@24^Q32@40"
- "v48@0:8@16d24@32@40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v80@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32d64@72"
- "valueForKey:"
- "valueWithCAColorMatrix:"
- "valueWithCGRect:"
- "variant"
- "variants"
- "weakObjectsHashTable"
- "weakToStrongObjectsMapTable"
- "whiteColor"
- "width"
- "workScheduler"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@\"NSAttributedString\"16{CGSize=dd}24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@16{CGSize=dd}24"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{CGSize=dd}40@0:8{CGSize=dd}16f32f36"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
