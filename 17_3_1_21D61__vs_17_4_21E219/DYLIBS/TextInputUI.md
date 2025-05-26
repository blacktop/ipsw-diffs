## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-7302.0.0.0.0
-  __TEXT.__text: 0x63528
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0x73a8
-  __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x185d
+7439.0.0.0.0
+  __TEXT.__text: 0x69fa8
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x7ae8
+  __TEXT.__const: 0x518
+  __TEXT.__cstring: 0x1e15
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__oslogstring: 0x86
-  __TEXT.__unwind_info: 0x1618
-  __TEXT.__objc_classname: 0xec3
-  __TEXT.__objc_methname: 0x16cc4
-  __TEXT.__objc_methtype: 0x34db
-  __TEXT.__objc_stubs: 0x11f60
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xb50
-  __DATA_CONST.__objc_classlist: 0x330
+  __TEXT.__unwind_info: 0x17a8
+  __TEXT.__objc_classname: 0xf94
+  __TEXT.__objc_methname: 0x17658
+  __TEXT.__objc_methtype: 0x3516
+  __TEXT.__objc_stubs: 0x12ac0
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0xb90
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10ac8
-  __DATA_CONST.__objc_selrefs: 0x5488
-  __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__cfstring: 0x23a0
-  __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__objc_const: 0x2a40
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_const: 0x10e40
+  __DATA_CONST.__objc_selrefs: 0x5770
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x678
+  __DATA_CONST.__objc_superrefs: 0x2a0
+  __DATA_CONST.__objc_arraydata: 0x178
+  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_const: 0x2de8
+  __AUTH_CONST.__cfstring: 0x2ac0
+  __AUTH_CONST.__objc_doubleobj: 0xb0
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__objc_floatobj: 0xe0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x6e0
-  __AUTH.__objc_data: 0x1090
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x638
-  __DATA.__objc_superrefs: 0x268
-  __DATA.__objc_ivar: 0xa4c
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH.__objc_data: 0x1360
+  __DATA.__objc_ivar: 0xa68
   __DATA.__data: 0xca8
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0xf50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2520
-  Symbols:   9686
-  CStrings:  4893
+  Functions: 2679
+  Symbols:   10176
+  CStrings:  5071
 
Symbols:
+ +[TUIKey layoutTypeForKey:]
+ +[TUIKeyPopupView hitTestingMode]
+ +[TUIKeyplane defaultEffectsType]
+ +[TUIKeyplaneView selectorViewClassForKey:]
+ +[TUISeparatedFlickSelectorView hitTestingMode]
+ +[TUISeparatedVariantSelectorView hitTestingMode]
+ +[TUISeparatedVariantSelectorView minCellDimension]
+ +[TUIVariantSelectorView minCellDimension]
+ -[TUICandidateCell setHighlighted:]
+ -[TUICandidateGrid updateGradientLayerToCollectionView]
+ -[TUIFlickSelectorView addVariantsForKey:toView:isNonVariantPaddle:]
+ -[TUIFlickSelectorView alignmentConstraintsForKey:]
+ -[TUIFlickSelectorView backgroundBezierPath]
+ -[TUIFlickSelectorView backgroundPathForFlick]
+ -[TUIFlickSelectorView backgroundPathForLongPress]
+ -[TUIFlickSelectorView cellViewsInSubtreeOrder]
+ -[TUIFlickSelectorView cellViewsInTopDownLTROrder]
+ -[TUIFlickSelectorView countNonNullVariantEntriesForKey:]
+ -[TUIFlickSelectorView flickDirection]
+ -[TUIFlickSelectorView flickPopupOffset]
+ -[TUIFlickSelectorView initWithKey:renderTraits:]
+ -[TUIFlickSelectorView maxVariantsPerRowForKey:]
+ -[TUIFlickSelectorView orderedVariantIndicesForKey]
+ -[TUIFlickSelectorView setFlickDirection:]
+ -[TUIFlickSelectorView setTopRowHasTrailingAlignment:]
+ -[TUIFlickSelectorView setTotalVariants:]
+ -[TUIFlickSelectorView stackLayoutMargins]
+ -[TUIFlickSelectorView topRowHasTrailingAlignment]
+ -[TUIFlickSelectorView totalVariants]
+ -[TUIFlickSelectorView updateVariantViewPropertiesForKey:isNonVariantPaddle:]
+ -[TUIFlickSelectorView updateVariantsIfNeededForKey:]
+ -[TUIFlickSelectorView variantCellWithString:]
+ -[TUIFlickSelectorView variantRowLimitForLayout]
+ -[TUIFlickSelectorView variantViewAlignment]
+ -[TUIFlickVariantCell backgroundCornerRadius]
+ -[TUIFlickVariantCell backgroundInsets]
+ -[TUIFlickVariantCell backgroundMaskedCorners]
+ -[TUIFlickVariantCell cornerMaskForBackground]
+ -[TUIFlickVariantCell curvedCorners]
+ -[TUIFlickVariantCell setCornerMaskForBackground:]
+ -[TUIFlickVariantCell setCurvedCorners:]
+ -[TUIKBKeyView shapeWhenMergedWithKey:insets:]
+ -[TUIKBKeyView updateStateFrom:to:]
+ -[TUIKey frame]
+ -[TUIKey keyShape]
+ -[TUIKey setFrame:]
+ -[TUIKey setKeyShape:]
+ -[TUIKeyPopupView .cxx_destruct]
+ -[TUIKeyPopupView _addShadows]
+ -[TUIKeyPopupView addVariantsForKey:toView:isNonVariantPaddle:]
+ -[TUIKeyPopupView alignmentConstraintsForKey:]
+ -[TUIKeyPopupView arrangedVariantCells]
+ -[TUIKeyPopupView arrangedVariantRows]
+ -[TUIKeyPopupView associatedTree]
+ -[TUIKeyPopupView backdropView]
+ -[TUIKeyPopupView backgroundBezierPath]
+ -[TUIKeyPopupView backgroundMaskView]
+ -[TUIKeyPopupView backingTree]
+ -[TUIKeyPopupView baseKeyLayoutGuide]
+ -[TUIKeyPopupView borderView]
+ -[TUIKeyPopupView cellViewsInSubtreeOrder]
+ -[TUIKeyPopupView constraintsToMatchInnerView:toOuterView:withInsets:]
+ -[TUIKeyPopupView constraintsToMatchView:toLayoutGuide:withInsets:]
+ -[TUIKeyPopupView decorateVariantView]
+ -[TUIKeyPopupView deepShadowView]
+ -[TUIKeyPopupView drawsBackground]
+ -[TUIKeyPopupView drawsShadows]
+ -[TUIKeyPopupView finishVariantSelection]
+ -[TUIKeyPopupView hasConstrainedBackground]
+ -[TUIKeyPopupView highlightCellAtLocation:]
+ -[TUIKeyPopupView hitTest:withEvent:]
+ -[TUIKeyPopupView indexOfHighlightedVariant]
+ -[TUIKeyPopupView initWithKey:renderTraits:]
+ -[TUIKeyPopupView itemSpacing]
+ -[TUIKeyPopupView keyShadowView]
+ -[TUIKeyPopupView layoutStyle]
+ -[TUIKeyPopupView layoutSubviews]
+ -[TUIKeyPopupView maxRows]
+ -[TUIKeyPopupView maxVariantsPerRowForKey:]
+ -[TUIKeyPopupView needsPopup]
+ -[TUIKeyPopupView pointInside:withEvent:]
+ -[TUIKeyPopupView popupConstructorForKey:]
+ -[TUIKeyPopupView popupDelegate]
+ -[TUIKeyPopupView renderTraits]
+ -[TUIKeyPopupView selectedVariant]
+ -[TUIKeyPopupView setArrangedVariantCells:]
+ -[TUIKeyPopupView setArrangedVariantRows:]
+ -[TUIKeyPopupView setBackdropView:]
+ -[TUIKeyPopupView setBackgroundMaskView:]
+ -[TUIKeyPopupView setBackingTree:]
+ -[TUIKeyPopupView setBorderView:]
+ -[TUIKeyPopupView setDeepShadowView:]
+ -[TUIKeyPopupView setHasConstrainedBackground:]
+ -[TUIKeyPopupView setInitialHighlight]
+ -[TUIKeyPopupView setKeyShadowView:]
+ -[TUIKeyPopupView setLayoutStyle:]
+ -[TUIKeyPopupView setNeedsPopup:]
+ -[TUIKeyPopupView setPopupDelegate:]
+ -[TUIKeyPopupView setRenderTraits:]
+ -[TUIKeyPopupView setSubclassAdditionalConstraints:]
+ -[TUIKeyPopupView setTouchesForwardingView:]
+ -[TUIKeyPopupView setVariantView:]
+ -[TUIKeyPopupView setVariantViewRows:]
+ -[TUIKeyPopupView shouldProvideDefaultSelection]
+ -[TUIKeyPopupView stackLayoutMargins]
+ -[TUIKeyPopupView subclassAdditionalConstraints]
+ -[TUIKeyPopupView touchesForwardingView]
+ -[TUIKeyPopupView unhighlightAllViews]
+ -[TUIKeyPopupView updateConstraints]
+ -[TUIKeyPopupView updateRenderTraits:forState:]
+ -[TUIKeyPopupView updateSelectorForPoint:]
+ -[TUIKeyPopupView updateSelectorForTouch:event:]
+ -[TUIKeyPopupView updateVariantViewPropertiesForKey:isNonVariantPaddle:]
+ -[TUIKeyPopupView updateVariantsIfNeededForKey:]
+ -[TUIKeyPopupView variantCellAtLocation:]
+ -[TUIKeyPopupView variantRowLimitForLayout]
+ -[TUIKeyPopupView variantViewAlignment]
+ -[TUIKeyPopupView variantViewBottomSpacing]
+ -[TUIKeyPopupView variantViewRows]
+ -[TUIKeyPopupView variantView]
+ -[TUIKeyPopupView wantsUserInteractionEnabled]
+ -[TUIKeyboardContentView _userInteractionStateDeterminesLayerHitTestState]
+ -[TUIKeyplane createPreparedKeyFromTree:withMultiplier:type:shape:]
+ -[TUIKeyplane doubleHeightKeys]
+ -[TUIKeyplane effectsType]
+ -[TUIKeyplane findRowSpanningDuplicatesForKeyplane:]
+ -[TUIKeyplane keysForName:]
+ -[TUIKeyplane setDoubleHeightKeys:]
+ -[TUIKeyplane setEffectsType:]
+ -[TUIKeyplaneRow _userInteractionStateDeterminesLayerHitTestState]
+ -[TUIKeyplaneRow removeFromSuperview]
+ -[TUIKeyplaneView _userInteractionStateDeterminesLayerHitTestState]
+ -[TUIKeyplaneView changingSelectedVariantForKey:atPoint:isDragging:]
+ -[TUIKeyplaneView hitTestVariantKeyAtPoint:]
+ -[TUIKeyplaneView idealKeySizeforLayoutType:]
+ -[TUIKeyplaneView preferredKeyViewClass]
+ -[TUIKeyplaneView rowInsets]
+ -[TUIKeyplaneView rowsVerticalSpacing]
+ -[TUIKeyplaneView(Internal) _shouldUseUnifiedKeyView:]
+ -[TUISeparatedFlickSelectorView decorateVariantView]
+ -[TUISeparatedFlickSelectorView drawsBackground]
+ -[TUISeparatedFlickSelectorView drawsShadows]
+ -[TUISeparatedFlickSelectorView flickPopupOffset]
+ -[TUISeparatedFlickSelectorView itemSpacing]
+ -[TUISeparatedFlickSelectorView layoutSubviews]
+ -[TUISeparatedFlickSelectorView setInitialHighlight]
+ -[TUISeparatedFlickSelectorView shouldProvideDefaultSelection]
+ -[TUISeparatedFlickSelectorView stackLayoutMargins]
+ -[TUISeparatedFlickSelectorView variantCellWithString:]
+ -[TUISeparatedFlickSelectorView wantsUserInteractionEnabled]
+ -[TUISeparatedFlickVariantCell .cxx_destruct]
+ -[TUISeparatedFlickVariantCell backgroundCornerRadius]
+ -[TUISeparatedFlickVariantCell backgroundInsets]
+ -[TUISeparatedFlickVariantCell cornerMaskForBackground]
+ -[TUISeparatedFlickVariantCell highlightColor]
+ -[TUISeparatedFlickVariantCell hitTest:withEvent:]
+ -[TUISeparatedFlickVariantCell initWithFrame:string:traits:]
+ -[TUISeparatedFlickVariantCell labelInsets]
+ -[TUISeparatedFlickVariantCell setTouchesForwardingView:]
+ -[TUISeparatedFlickVariantCell touchesForwardingView]
+ -[TUISeparatedFlickVariantCell transitionToHighlighted:]
+ -[TUISeparatedKBKeyView _addGlassEffect]
+ -[TUISeparatedKBKeyView _addHoverEffect]
+ -[TUISeparatedKBKeyView _addShadowEffect]
+ -[TUISeparatedKBKeyView _pressRingLayer]
+ -[TUISeparatedKBKeyView _startStateTransitionAnimationsFrom:to:]
+ -[TUISeparatedKBKeyView _updateHoverToEnabled:]
+ -[TUISeparatedKBKeyView initWithKey:]
+ -[TUISeparatedKBKeyView updateStateFrom:to:]
+ -[TUISeparatedVariantCell .cxx_destruct]
+ -[TUISeparatedVariantCell backgroundCornerRadius]
+ -[TUISeparatedVariantCell backgroundInsets]
+ -[TUISeparatedVariantCell highlightColor]
+ -[TUISeparatedVariantCell hitTest:withEvent:]
+ -[TUISeparatedVariantCell initWithFrame:string:traits:]
+ -[TUISeparatedVariantCell labelInsets]
+ -[TUISeparatedVariantCell setTouchesForwardingView:]
+ -[TUISeparatedVariantCell touchesForwardingView]
+ -[TUISeparatedVariantCell transitionToHighlighted:]
+ -[TUISeparatedVariantSelectorView decorateVariantView]
+ -[TUISeparatedVariantSelectorView drawsBackground]
+ -[TUISeparatedVariantSelectorView drawsShadows]
+ -[TUISeparatedVariantSelectorView itemSpacing]
+ -[TUISeparatedVariantSelectorView layoutSubviews]
+ -[TUISeparatedVariantSelectorView maxRows]
+ -[TUISeparatedVariantSelectorView pointInside:withEvent:]
+ -[TUISeparatedVariantSelectorView shouldProvideDefaultSelection]
+ -[TUISeparatedVariantSelectorView stackLayoutMargins]
+ -[TUISeparatedVariantSelectorView variantCellWithString:]
+ -[TUISeparatedVariantSelectorView variantRowLimitForLayout]
+ -[TUISeparatedVariantSelectorView variantViewAlignment]
+ -[TUISeparatedVariantSelectorView variantViewBottomSpacing]
+ -[TUISeparatedVariantSelectorView wantsUserInteractionEnabled]
+ -[TUISeparatedVariantSelectorView widthConstraintForVariantCell:previousCell:]
+ -[TUIVariantCell backgroundCornerRadius]
+ -[TUIVariantCell backgroundInsets]
+ -[TUIVariantCell backgroundMaskedCorners]
+ -[TUIVariantCell highlightColor]
+ -[TUIVariantCell labelInsets]
+ -[TUIVariantCell layoutSubviews]
+ -[TUIVariantCell traitsForCell]
+ -[TUIVariantCell transitionToHighlighted:]
+ -[TUIVariantSelectorView alignmentConstraintsForKey:]
+ -[TUIVariantSelectorView backgroundBezierPath]
+ -[TUIVariantSelectorView variantCellWithString:]
+ -[TUIVariantSelectorView widthConstraintForVariantCell:previousCell:]
+ _CATransform3DMakeTranslation
+ _CATransform3DTranslate
+ _OBJC_CLASS_$_CAGradientLayer
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_TUIFlickSelectorView
+ _OBJC_CLASS_$_TUIFlickVariantCell
+ _OBJC_CLASS_$_TUIKeyPopupView
+ _OBJC_CLASS_$_TUIKeyboardContentView
+ _OBJC_CLASS_$_TUISeparatedFlickSelectorView
+ _OBJC_CLASS_$_TUISeparatedFlickVariantCell
+ _OBJC_CLASS_$_TUISeparatedKBKeyView
+ _OBJC_CLASS_$_TUISeparatedVariantCell
+ _OBJC_CLASS_$_TUISeparatedVariantSelectorView
+ _OBJC_IVAR_$_TUIFlickSelectorView._flickDirection
+ _OBJC_IVAR_$_TUIFlickSelectorView._topRowHasTrailingAlignment
+ _OBJC_IVAR_$_TUIFlickSelectorView._totalVariants
+ _OBJC_IVAR_$_TUIFlickVariantCell._cornerMaskForBackground
+ _OBJC_IVAR_$_TUIFlickVariantCell._curvedCorners
+ _OBJC_IVAR_$_TUIKeyPopupView._arrangedVariantCells
+ _OBJC_IVAR_$_TUIKeyPopupView._arrangedVariantRows
+ _OBJC_IVAR_$_TUIKeyPopupView._backdropView
+ _OBJC_IVAR_$_TUIKeyPopupView._backgroundMaskView
+ _OBJC_IVAR_$_TUIKeyPopupView._backingTree
+ _OBJC_IVAR_$_TUIKeyPopupView._baseKeyLayoutGuide
+ _OBJC_IVAR_$_TUIKeyPopupView._borderView
+ _OBJC_IVAR_$_TUIKeyPopupView._deepShadowView
+ _OBJC_IVAR_$_TUIKeyPopupView._hasConstrainedBackground
+ _OBJC_IVAR_$_TUIKeyPopupView._keyShadowView
+ _OBJC_IVAR_$_TUIKeyPopupView._layoutStyle
+ _OBJC_IVAR_$_TUIKeyPopupView._needsPopup
+ _OBJC_IVAR_$_TUIKeyPopupView._popupDelegate
+ _OBJC_IVAR_$_TUIKeyPopupView._renderTraits
+ _OBJC_IVAR_$_TUIKeyPopupView._selectedVariant
+ _OBJC_IVAR_$_TUIKeyPopupView._subclassAdditionalConstraints
+ _OBJC_IVAR_$_TUIKeyPopupView._touchesForwardingView
+ _OBJC_IVAR_$_TUIKeyPopupView._variantView
+ _OBJC_IVAR_$_TUIKeyPopupView._variantViewRows
+ _OBJC_IVAR_$_TUIKeyplane._doubleHeightKeys
+ _OBJC_IVAR_$_TUIKeyplane._effectsType
+ _OBJC_IVAR_$_TUISeparatedFlickVariantCell._touchesForwardingView
+ _OBJC_IVAR_$_TUISeparatedVariantCell._touchesForwardingView
+ _OBJC_METACLASS_$_TUIFlickSelectorView
+ _OBJC_METACLASS_$_TUIFlickVariantCell
+ _OBJC_METACLASS_$_TUIKeyPopupView
+ _OBJC_METACLASS_$_TUIKeyboardContentView
+ _OBJC_METACLASS_$_TUISeparatedFlickSelectorView
+ _OBJC_METACLASS_$_TUISeparatedFlickVariantCell
+ _OBJC_METACLASS_$_TUISeparatedKBKeyView
+ _OBJC_METACLASS_$_TUISeparatedVariantCell
+ _OBJC_METACLASS_$_TUISeparatedVariantSelectorView
+ _TUIPPMFloatValue
+ _TUIPPMScaledFloatValue
+ _UIDistanceBetweenPoints
+ _UIKeyboardOrderInOutAnimatedDuration
+ __OBJC_$_CLASS_METHODS_TUIKeyPopupView
+ __OBJC_$_CLASS_METHODS_TUISeparatedFlickSelectorView
+ __OBJC_$_CLASS_METHODS_TUISeparatedVariantSelectorView
+ __OBJC_$_CLASS_METHODS_TUIVariantSelectorView
+ __OBJC_$_CLASS_PROP_LIST_TUIKeyPopupView
+ __OBJC_$_CLASS_PROP_LIST_TUIVariantSelectorView
+ __OBJC_$_INSTANCE_METHODS_TUIFlickSelectorView
+ __OBJC_$_INSTANCE_METHODS_TUIFlickVariantCell
+ __OBJC_$_INSTANCE_METHODS_TUIKeyPopupView
+ __OBJC_$_INSTANCE_METHODS_TUIKeyboardContentView
+ __OBJC_$_INSTANCE_METHODS_TUISeparatedFlickSelectorView
+ __OBJC_$_INSTANCE_METHODS_TUISeparatedFlickVariantCell
+ __OBJC_$_INSTANCE_METHODS_TUISeparatedKBKeyView
+ __OBJC_$_INSTANCE_METHODS_TUISeparatedVariantCell
+ __OBJC_$_INSTANCE_METHODS_TUISeparatedVariantSelectorView
+ __OBJC_$_INSTANCE_VARIABLES_TUIFlickSelectorView
+ __OBJC_$_INSTANCE_VARIABLES_TUIFlickVariantCell
+ __OBJC_$_INSTANCE_VARIABLES_TUIKeyPopupView
+ __OBJC_$_INSTANCE_VARIABLES_TUISeparatedFlickVariantCell
+ __OBJC_$_INSTANCE_VARIABLES_TUISeparatedVariantCell
+ __OBJC_$_PROP_LIST_NSObject.1879
+ __OBJC_$_PROP_LIST_NSObject.2405
+ __OBJC_$_PROP_LIST_NSObject.2558
+ __OBJC_$_PROP_LIST_NSObject.2709
+ __OBJC_$_PROP_LIST_NSObject.2889
+ __OBJC_$_PROP_LIST_NSObject.3084
+ __OBJC_$_PROP_LIST_NSObject.3269
+ __OBJC_$_PROP_LIST_NSObject.375
+ __OBJC_$_PROP_LIST_NSObject.4142
+ __OBJC_$_PROP_LIST_NSObject.4476
+ __OBJC_$_PROP_LIST_NSObject.4593
+ __OBJC_$_PROP_LIST_NSObject.5075
+ __OBJC_$_PROP_LIST_NSObject.5471
+ __OBJC_$_PROP_LIST_NSObject.5802
+ __OBJC_$_PROP_LIST_NSObject.6087
+ __OBJC_$_PROP_LIST_NSObject.6392
+ __OBJC_$_PROP_LIST_NSObject.6697
+ __OBJC_$_PROP_LIST_NSObject.727
+ __OBJC_$_PROP_LIST_NSObject.7467
+ __OBJC_$_PROP_LIST_NSObject.7736
+ __OBJC_$_PROP_LIST_NSObject.979
+ __OBJC_$_PROP_LIST_TUIFlickSelectorView
+ __OBJC_$_PROP_LIST_TUIFlickVariantCell
+ __OBJC_$_PROP_LIST_TUIKeyPopupView
+ __OBJC_$_PROP_LIST_TUISeparatedFlickVariantCell
+ __OBJC_$_PROP_LIST_TUISeparatedVariantCell
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1880
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2406
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2559
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2710
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2890
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3085
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3270
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.376
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4143
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4477
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4594
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5076
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5472
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5803
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6088
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6393
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6698
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.728
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7468
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7737
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.980
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1881
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2407
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2560
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2711
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2891
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3086
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3271
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.377
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4144
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4478
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4595
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5077
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5473
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5804
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6089
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6394
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6699
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.729
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7469
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7738
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.981
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TUIInputAccessoryViewTraits.5078
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UICollectionViewDataSource.4479
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UICollectionViewDelegate.4145
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UICollectionViewDelegate.4480
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.4146
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.4481
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.5474
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.730
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.7739
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUIKeyPopupDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UICollectionViewDataSource.4482
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1882
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2408
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2561
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2712
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2892
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3087
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3272
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.378
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4147
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4483
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4596
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5079
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5475
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5805
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6090
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6395
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6700
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.731
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7470
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7740
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.982
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUIInputAccessoryViewTraits.5080
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUIKeyPopupDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UICollectionViewDataSource.4484
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UICollectionViewDelegate.4148
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UICollectionViewDelegate.4485
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.4149
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.4486
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.5476
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.732
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.7741
+ __OBJC_$_PROTOCOL_REFS_TUIInputAccessoryViewTraits.5081
+ __OBJC_$_PROTOCOL_REFS_TUIKeyPopupDelegate
+ __OBJC_$_PROTOCOL_REFS_UICollectionViewDataSource.4487
+ __OBJC_$_PROTOCOL_REFS_UICollectionViewDelegate.4150
+ __OBJC_$_PROTOCOL_REFS_UICollectionViewDelegate.4488
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.4151
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.4489
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.5477
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.733
+ __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.7742
+ __OBJC_CLASS_RO_$_TUIFlickSelectorView
+ __OBJC_CLASS_RO_$_TUIFlickVariantCell
+ __OBJC_CLASS_RO_$_TUIKeyPopupView
+ __OBJC_CLASS_RO_$_TUIKeyboardContentView
+ __OBJC_CLASS_RO_$_TUISeparatedFlickSelectorView
+ __OBJC_CLASS_RO_$_TUISeparatedFlickVariantCell
+ __OBJC_CLASS_RO_$_TUISeparatedKBKeyView
+ __OBJC_CLASS_RO_$_TUISeparatedVariantCell
+ __OBJC_CLASS_RO_$_TUISeparatedVariantSelectorView
+ __OBJC_LABEL_PROTOCOL_$_TUIKeyPopupDelegate
+ __OBJC_METACLASS_RO_$_TUIFlickSelectorView
+ __OBJC_METACLASS_RO_$_TUIFlickVariantCell
+ __OBJC_METACLASS_RO_$_TUIKeyPopupView
+ __OBJC_METACLASS_RO_$_TUIKeyboardContentView
+ __OBJC_METACLASS_RO_$_TUISeparatedFlickSelectorView
+ __OBJC_METACLASS_RO_$_TUISeparatedFlickVariantCell
+ __OBJC_METACLASS_RO_$_TUISeparatedKBKeyView
+ __OBJC_METACLASS_RO_$_TUISeparatedVariantCell
+ __OBJC_METACLASS_RO_$_TUISeparatedVariantSelectorView
+ __OBJC_PROTOCOL_$_TUIKeyPopupDelegate
+ ___30-[TUIKeyPopupView _addShadows]_block_invoke
+ ___35-[TUICandidateCell setHighlighted:]_block_invoke
+ ___35-[TUICandidateCell setHighlighted:]_block_invoke_2
+ ___40-[TUISeparatedKBKeyView _pressRingLayer]_block_invoke
+ ___46-[TUIVariantSelectorView backgroundBezierPath]_block_invoke
+ ___46-[TUIVariantSelectorView backgroundBezierPath]_block_invoke_2
+ ___50-[TUIFlickSelectorView backgroundPathForLongPress]_block_invoke
+ ___51-[TUISeparatedVariantCell transitionToHighlighted:]_block_invoke
+ ___51-[TUISeparatedVariantCell transitionToHighlighted:]_block_invoke_2
+ ___51-[TUISeparatedVariantCell transitionToHighlighted:]_block_invoke_3
+ ___51-[TUISeparatedVariantCell transitionToHighlighted:]_block_invoke_4
+ ___56-[TUISeparatedFlickVariantCell transitionToHighlighted:]_block_invoke
+ ___56-[TUISeparatedFlickVariantCell transitionToHighlighted:]_block_invoke_2
+ ___Block_byref_object_copy_.1811
+ ___Block_byref_object_copy_.2039
+ ___Block_byref_object_copy_.6873
+ ___Block_byref_object_dispose_.1812
+ ___Block_byref_object_dispose_.2040
+ ___Block_byref_object_dispose_.6874
+ ___block_descriptor_40_8_32r_e24_v32?0"CALayer"8Q16^B24lr32l8
+ ___block_descriptor_72_8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_literal_global.1110
+ ___block_literal_global.1383
+ ___block_literal_global.1488
+ ___block_literal_global.149
+ ___block_literal_global.1673
+ ___block_literal_global.1819
+ ___block_literal_global.2159
+ ___block_literal_global.240
+ ___block_literal_global.2592
+ ___block_literal_global.2668
+ ___block_literal_global.2852
+ ___block_literal_global.310
+ ___block_literal_global.3105
+ ___block_literal_global.33
+ ___block_literal_global.334
+ ___block_literal_global.3465
+ ___block_literal_global.36
+ ___block_literal_global.4004
+ ___block_literal_global.41
+ ___block_literal_global.4349
+ ___block_literal_global.4532
+ ___block_literal_global.4642
+ ___block_literal_global.47
+ ___block_literal_global.4943
+ ___block_literal_global.5382
+ ___block_literal_global.5532
+ ___block_literal_global.5713
+ ___block_literal_global.6152
+ ___block_literal_global.6345
+ ___block_literal_global.653
+ ___block_literal_global.6883
+ ___block_literal_global.7407
+ ___block_literal_global.98
+ __unnamed_array_storage.1399
+ __unnamed_array_storage.16
+ __unnamed_array_storage.1641
+ __unnamed_array_storage.342
+ __unnamed_array_storage.3840
+ __unnamed_array_storage.4333
+ __unnamed_array_storage.6164
+ _kCACornerCurveCircular
+ _kCAGradientLayerRadial
+ _kCAMediaTimingFunctionEaseOut
+ _kCAShadowScale
+ _kShadowOffset
+ _kShadowOpacity
+ _kShadowPadding
+ _kShadowRadius
+ _objc_msgSend$_addGlassEffect
+ _objc_msgSend$_addHoverEffect
+ _objc_msgSend$_addShadowEffect
+ _objc_msgSend$_addShadows
+ _objc_msgSend$_pressRingLayer
+ _objc_msgSend$_shouldUseUnifiedKeyView:
+ _objc_msgSend$_startStateTransitionAnimationsFrom:to:
+ _objc_msgSend$_updateHoverToEnabled:
+ _objc_msgSend$addQuadCurveToPoint:controlPoint:
+ _objc_msgSend$alignmentConstraintsForKey:
+ _objc_msgSend$alternativeTextLeftSpacing
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$arrowButtonConfig
+ _objc_msgSend$arrowButtonHighlightBackgroundHidden
+ _objc_msgSend$backgroundBezierPath
+ _objc_msgSend$backgroundCornerRadius
+ _objc_msgSend$backgroundInsets
+ _objc_msgSend$backgroundMaskedCorners
+ _objc_msgSend$backgroundPathForFlick
+ _objc_msgSend$backgroundPathForLongPress
+ _objc_msgSend$bezierPathWithRect:
+ _objc_msgSend$cellViewsInTopDownLTROrder
+ _objc_msgSend$center
+ _objc_msgSend$changingSelectedVariantForKey:atPoint:isDragging:
+ _objc_msgSend$constraintEqualToAnchor:multiplier:constant:
+ _objc_msgSend$cornerMaskForBackground
+ _objc_msgSend$countNonNullVariantEntriesForKey:
+ _objc_msgSend$countryCode
+ _objc_msgSend$createPreparedKeyFromTree:withMultiplier:type:shape:
+ _objc_msgSend$decorateVariantView
+ _objc_msgSend$defaultEffectsType
+ _objc_msgSend$doubleHeightKeys
+ _objc_msgSend$drawsBackground
+ _objc_msgSend$drawsShadows
+ _objc_msgSend$effectsType
+ _objc_msgSend$findRowSpanningDuplicatesForKeyplane:
+ _objc_msgSend$flickDirection
+ _objc_msgSend$flickPopupOffset
+ _objc_msgSend$groupHeaderPadding
+ _objc_msgSend$hasConstrainedBackground
+ _objc_msgSend$hideLinesOnDisambiguationGridEdges
+ _objc_msgSend$hitTestingMode
+ _objc_msgSend$idealKeySizeforLayoutType:
+ _objc_msgSend$keysForName:
+ _objc_msgSend$labelInsets
+ _objc_msgSend$layoutTypeForKey:
+ _objc_msgSend$localizedStringForCountryCode:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$maxRows
+ _objc_msgSend$minCellDimension
+ _objc_msgSend$needsPopup
+ _objc_msgSend$null
+ _objc_msgSend$orderedVariantIndicesForKey
+ _objc_msgSend$performScalingAnimationOnCellHighlight
+ _objc_msgSend$popupDelegate
+ _objc_msgSend$preferredKeyViewClass
+ _objc_msgSend$rowInsets
+ _objc_msgSend$rowsVerticalSpacing
+ _objc_msgSend$selectorViewClassForKey:
+ _objc_msgSend$setColors:
+ _objc_msgSend$setConcaveCorner:
+ _objc_msgSend$setConcaveCornerOffset:
+ _objc_msgSend$setCornerMaskForBackground:
+ _objc_msgSend$setCurvedCorners:
+ _objc_msgSend$setDoubleHeightKeys:
+ _objc_msgSend$setEffectsType:
+ _objc_msgSend$setEndPoint:
+ _objc_msgSend$setFlickDirection:
+ _objc_msgSend$setLocations:
+ _objc_msgSend$setNeedsPopup:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setPopupDelegate:
+ _objc_msgSend$setShadowPathIsBounds:
+ _objc_msgSend$setSpacing:
+ _objc_msgSend$setStartPoint:
+ _objc_msgSend$setSubclassAdditionalConstraints:
+ _objc_msgSend$setTotalVariants:
+ _objc_msgSend$setTransform3D:
+ _objc_msgSend$setType:
+ _objc_msgSend$setVariantViewRows:
+ _objc_msgSend$shapeWhenMergedWithKey:insets:
+ _objc_msgSend$shouldProvideDefaultSelection
+ _objc_msgSend$showCellBorderForSpaceConfirmationCandidate
+ _objc_msgSend$spaceConfirmationCandidateCellBackgroundColor
+ _objc_msgSend$stackLayoutMargins
+ _objc_msgSend$subclassAdditionalConstraints
+ _objc_msgSend$sublayers
+ _objc_msgSend$systemWhiteColor
+ _objc_msgSend$totalVariants
+ _objc_msgSend$traitsForCell
+ _objc_msgSend$transform3D
+ _objc_msgSend$transitionToHighlighted:
+ _objc_msgSend$updateGradientLayerToCollectionView
+ _objc_msgSend$updateStateFrom:to:
+ _objc_msgSend$updateVariantViewPropertiesForKey:isNonVariantPaddle:
+ _objc_msgSend$variantCellWithString:
+ _objc_msgSend$variantType
+ _objc_msgSend$variantViewAlignment
+ _objc_msgSend$variantViewBottomSpacing
+ _objc_msgSend$variantViewRows
+ _objc_msgSend$wantsUserInteractionEnabled
+ _objc_msgSend$widthConstraintForVariantCell:previousCell:
+ _objc_msgSend$widthOfGridGradient
+ _sharedInstance.__instance.5533
+ _sharedInstance.onceToken.4941
+ _sharedInstance.onceToken.5531
- -[TUICursorAccessory preferredAnimationStyle]
- -[TUICursorAccessory setPreferredAnimationStyle:]
- -[TUIDictationAccessory animationStyle]
- -[TUIDictationAccessory initWithLanguages:animationStyle:actionHandler:]
- -[TUIDictationAccessory preferredAnimationStyle]
- -[TUIDictationAccessory setAnimationStyle:]
- -[TUIDictationAccessory setPreferredAnimationStyle:]
- -[TUIKBKeyView updateState:]
- -[TUIKeyplane createPreparedKeyFromTree:withMultiplier:type:]
- -[TUIKeyplane layoutTypeFromDisplayType:]
- -[TUIVariantSelectorView .cxx_destruct]
- -[TUIVariantSelectorView arrangedVariantCells]
- -[TUIVariantSelectorView arrangedVariantRows]
- -[TUIVariantSelectorView associatedTree]
- -[TUIVariantSelectorView backdropView]
- -[TUIVariantSelectorView backgroundMaskView]
- -[TUIVariantSelectorView backingTree]
- -[TUIVariantSelectorView baseKeyLayoutGuide]
- -[TUIVariantSelectorView borderView]
- -[TUIVariantSelectorView constraintsToMatchInnerView:toOuterView:withInsets:]
- -[TUIVariantSelectorView constraintsToMatchView:toLayoutGuide:withInsets:]
- -[TUIVariantSelectorView deepShadowView]
- -[TUIVariantSelectorView finishVariantSelection]
- -[TUIVariantSelectorView highlightCellAtLocation:]
- -[TUIVariantSelectorView indexOfHighlightedVariant]
- -[TUIVariantSelectorView keyShadowView]
- -[TUIVariantSelectorView layoutStyle]
- -[TUIVariantSelectorView layoutSubviews]
- -[TUIVariantSelectorView maxVariantsPerRowForKey:]
- -[TUIVariantSelectorView needsPopup]
- -[TUIVariantSelectorView paddleBezierPath]
- -[TUIVariantSelectorView popupConstructorForKey:]
- -[TUIVariantSelectorView renderTraits]
- -[TUIVariantSelectorView selectedVariant]
- -[TUIVariantSelectorView selectorDelegate]
- -[TUIVariantSelectorView setArrangedVariantCells:]
- -[TUIVariantSelectorView setArrangedVariantRows:]
- -[TUIVariantSelectorView setBackdropView:]
- -[TUIVariantSelectorView setBackgroundMaskView:]
- -[TUIVariantSelectorView setBackingTree:]
- -[TUIVariantSelectorView setBorderView:]
- -[TUIVariantSelectorView setDeepShadowView:]
- -[TUIVariantSelectorView setInitialHighlight]
- -[TUIVariantSelectorView setKeyShadowView:]
- -[TUIVariantSelectorView setLayoutStyle:]
- -[TUIVariantSelectorView setNeedsPopup:]
- -[TUIVariantSelectorView setRenderTraits:]
- -[TUIVariantSelectorView setSelectorDelegate:]
- -[TUIVariantSelectorView setTouchesForwardingView:]
- -[TUIVariantSelectorView setVariantLayoutGuide:]
- -[TUIVariantSelectorView setVariantView:]
- -[TUIVariantSelectorView setVariantViewRows:]
- -[TUIVariantSelectorView touchesForwardingView]
- -[TUIVariantSelectorView unhighlightAllViews]
- -[TUIVariantSelectorView updateConstraints]
- -[TUIVariantSelectorView updateRenderTraits:forState:]
- -[TUIVariantSelectorView updateSelectorForPoint:]
- -[TUIVariantSelectorView updateSelectorForTouch:event:]
- -[TUIVariantSelectorView updateVariantRowsForKey:isNonVariantPaddle:]
- -[TUIVariantSelectorView variantCellAtLocation:]
- -[TUIVariantSelectorView variantLayoutGuide]
- -[TUIVariantSelectorView variantRowLimitForLayout]
- -[TUIVariantSelectorView variantViewRows]
- -[TUIVariantSelectorView variantView]
- _OBJC_IVAR_$_TUICursorAccessory._preferredAnimationStyle
- _OBJC_IVAR_$_TUIDictationAccessory._animationStyle
- _OBJC_IVAR_$_TUIDictationAccessory.preferredAnimationStyle
- _OBJC_IVAR_$_TUIVariantSelectorView._arrangedVariantCells
- _OBJC_IVAR_$_TUIVariantSelectorView._arrangedVariantRows
- _OBJC_IVAR_$_TUIVariantSelectorView._backdropView
- _OBJC_IVAR_$_TUIVariantSelectorView._backgroundMaskView
- _OBJC_IVAR_$_TUIVariantSelectorView._backingTree
- _OBJC_IVAR_$_TUIVariantSelectorView._baseKeyLayoutGuide
- _OBJC_IVAR_$_TUIVariantSelectorView._borderView
- _OBJC_IVAR_$_TUIVariantSelectorView._deepShadowView
- _OBJC_IVAR_$_TUIVariantSelectorView._keyShadowView
- _OBJC_IVAR_$_TUIVariantSelectorView._layoutStyle
- _OBJC_IVAR_$_TUIVariantSelectorView._needsPopup
- _OBJC_IVAR_$_TUIVariantSelectorView._renderTraits
- _OBJC_IVAR_$_TUIVariantSelectorView._selectedVariant
- _OBJC_IVAR_$_TUIVariantSelectorView._selectorDelegate
- _OBJC_IVAR_$_TUIVariantSelectorView._touchesForwardingView
- _OBJC_IVAR_$_TUIVariantSelectorView._variantLayoutGuide
- _OBJC_IVAR_$_TUIVariantSelectorView._variantView
- _OBJC_IVAR_$_TUIVariantSelectorView._variantViewRows
- __OBJC_$_PROP_LIST_NSObject.1728
- __OBJC_$_PROP_LIST_NSObject.2252
- __OBJC_$_PROP_LIST_NSObject.2406
- __OBJC_$_PROP_LIST_NSObject.2557
- __OBJC_$_PROP_LIST_NSObject.2726
- __OBJC_$_PROP_LIST_NSObject.2929
- __OBJC_$_PROP_LIST_NSObject.3116
- __OBJC_$_PROP_LIST_NSObject.317
- __OBJC_$_PROP_LIST_NSObject.3910
- __OBJC_$_PROP_LIST_NSObject.4226
- __OBJC_$_PROP_LIST_NSObject.4347
- __OBJC_$_PROP_LIST_NSObject.4825
- __OBJC_$_PROP_LIST_NSObject.5227
- __OBJC_$_PROP_LIST_NSObject.5557
- __OBJC_$_PROP_LIST_NSObject.5839
- __OBJC_$_PROP_LIST_NSObject.6144
- __OBJC_$_PROP_LIST_NSObject.6445
- __OBJC_$_PROP_LIST_NSObject.658
- __OBJC_$_PROP_LIST_NSObject.7169
- __OBJC_$_PROP_LIST_NSObject.7436
- __OBJC_$_PROP_LIST_NSObject.890
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1729
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2253
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2407
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2558
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2727
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2930
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.318
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3911
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4227
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4348
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4826
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5228
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5558
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5840
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6145
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6446
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.659
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7170
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7437
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.891
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1730
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2254
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2408
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2559
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2728
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2931
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3118
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.319
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3912
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4228
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4349
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4827
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5229
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5559
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5841
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6146
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6447
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.660
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7171
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7438
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.892
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TUIInputAccessoryViewTraits.4828
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UICollectionViewDataSource.4229
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UICollectionViewDelegate.3913
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UICollectionViewDelegate.4230
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.3914
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.4231
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.5230
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.661
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIScrollViewDelegate.7439
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUIVariantSelectorDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UICollectionViewDataSource.4232
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1731
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2255
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2409
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2560
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2729
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2932
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3119
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.320
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3915
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4233
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4350
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4829
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5231
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5560
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5842
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6147
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6448
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.662
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7172
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7440
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.893
- __OBJC_$_PROTOCOL_METHOD_TYPES_TUIInputAccessoryViewTraits.4830
- __OBJC_$_PROTOCOL_METHOD_TYPES_TUIVariantSelectorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UICollectionViewDataSource.4234
- __OBJC_$_PROTOCOL_METHOD_TYPES_UICollectionViewDelegate.3916
- __OBJC_$_PROTOCOL_METHOD_TYPES_UICollectionViewDelegate.4235
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.3917
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.4236
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.5232
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.663
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIScrollViewDelegate.7441
- __OBJC_$_PROTOCOL_REFS_TUIInputAccessoryViewTraits.4831
- __OBJC_$_PROTOCOL_REFS_TUIVariantSelectorDelegate
- __OBJC_$_PROTOCOL_REFS_UICollectionViewDataSource.4237
- __OBJC_$_PROTOCOL_REFS_UICollectionViewDelegate.3918
- __OBJC_$_PROTOCOL_REFS_UICollectionViewDelegate.4238
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.3919
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.4239
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.5233
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.664
- __OBJC_$_PROTOCOL_REFS_UIScrollViewDelegate.7442
- __OBJC_LABEL_PROTOCOL_$_TUIVariantSelectorDelegate
- __OBJC_PROTOCOL_$_TUIVariantSelectorDelegate
- __ReducedLanguageIdentifierForKeyboardLanguage
- ___42-[TUIVariantSelectorView paddleBezierPath]_block_invoke
- ___42-[TUIVariantSelectorView paddleBezierPath]_block_invoke_2
- ___51-[TUIVariantSelectorView initWithKey:renderTraits:]_block_invoke
- ___Block_byref_object_copy_.1662
- ___Block_byref_object_copy_.6621
- ___Block_byref_object_dispose_.1663
- ___Block_byref_object_dispose_.6622
- ___block_descriptor_80_8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_literal_global.1021
- ___block_literal_global.1252
- ___block_literal_global.1350
- ___block_literal_global.148
- ___block_literal_global.1528
- ___block_literal_global.1670
- ___block_literal_global.177
- ___block_literal_global.2440
- ___block_literal_global.2517
- ___block_literal_global.2689
- ___block_literal_global.2950
- ___block_literal_global.309
- ___block_literal_global.34
- ___block_literal_global.3639
- ___block_literal_global.3770
- ___block_literal_global.39
- ___block_literal_global.4094
- ___block_literal_global.4282
- ___block_literal_global.43
- ___block_literal_global.4396
- ___block_literal_global.4694
- ___block_literal_global.5138
- ___block_literal_global.5288
- ___block_literal_global.5468
- ___block_literal_global.588
- ___block_literal_global.5905
- ___block_literal_global.6096
- ___block_literal_global.6631
- ___block_literal_global.7108
- ___block_literal_global.94
- __unnamed_array_storage.1507
- __unnamed_array_storage.3413
- __unnamed_array_storage.5917
- _objc_msgSend$constraintLessThanOrEqualToAnchor:multiplier:
- _objc_msgSend$createPreparedKeyFromTree:withMultiplier:type:
- _objc_msgSend$initWithLanguages:animationStyle:actionHandler:
- _objc_msgSend$layoutTypeFromDisplayType:
- _objc_msgSend$paddleBezierPath
- _objc_msgSend$preferredAnimationStyle
- _objc_msgSend$selectorDelegate
- _objc_msgSend$setPreferredAnimationStyle:
- _objc_msgSend$setSelectorDelegate:
- _objc_msgSend$unhighlightAllViews
- _objc_msgSend$updateState:
- _objc_msgSend$updateVariantRowsForKey:isNonVariantPaddle:
- _sharedInstance.__instance.5289
- _sharedInstance.onceToken.4692
- _sharedInstance.onceToken.5287
CStrings:
+ "\x11!"
+ "\"9\x11"
+ "#24@0:8@16"
+ "%"
+ "@\"<TUIKeyPopupDelegate>\""
+ "@48@0:8@16d24q32q40"
+ "@56@0:8@16{UIEdgeInsets=dddd}24"
+ "AZERTY"
+ "AZERTY-French"
+ "AZERTY-Pinyin-Simplified"
+ "Cangjie"
+ "Cangjie-QWERTY"
+ "Double height"
+ "F"
+ "Kana"
+ "Kana-Flick"
+ "KeyPressEffectHighlightLayerName"
+ "Keyplane-Switch-Key"
+ "Korean"
+ "Numbers-And-Punctuation"
+ "Pinyin-Simplified"
+ "Pinyin-Traditional"
+ "Pinyin10-Simplified"
+ "QWERTY-Accents"
+ "QWERTY-Japanese"
+ "QWERTZ"
+ "QWERTZ-German"
+ "Return-Key"
+ "Sami-Julev-Norway"
+ "Shuangpin-with-Semicolon-Simplified"
+ "Sucheng"
+ "Sucheng-QWERTY"
+ "T@\"<TUIKeyPopupDelegate>\",W,N,V_popupDelegate"
+ "T@\"NSArray\",&,N,V_subclassAdditionalConstraints"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSMutableDictionary\",&,N,V_doubleHeightKeys"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIImageSymbolConfiguration\",?,R,N"
+ "T@\"UIKBShape\",&,N"
+ "TB,N,V_hasConstrainedBackground"
+ "TB,N,V_topRowHasTrailingAlignment"
+ "TQ,N,V_cornerMaskForBackground"
+ "TQ,N,V_curvedCorners"
+ "TQ,N,V_totalVariants"
+ "TUIFlickSelectorView"
+ "TUIFlickVariantCell"
+ "TUIKeyPopupDelegate"
+ "TUIKeyPopupView"
+ "TUIKeyboardContentView"
+ "TUISeparatedFlickSelectorView"
+ "TUISeparatedFlickVariantCell"
+ "TUISeparatedKBKeyView"
+ "TUISeparatedVariantCell"
+ "TUISeparatedVariantSelectorView"
+ "TenKey-AdaptiveKey-Facemark-Voiced"
+ "Tq,N,V_effectsType"
+ "Tq,N,V_flickDirection"
+ "Wubihua-Simplified"
+ "Wubihua-Traditional"
+ "_addGlassEffect"
+ "_addHoverEffect"
+ "_addShadowEffect"
+ "_addShadows"
+ "_cornerMaskForBackground"
+ "_curvedCorners"
+ "_doubleHeightKeys"
+ "_effectsType"
+ "_flickDirection"
+ "_hasConstrainedBackground"
+ "_popupDelegate"
+ "_pressRingLayer"
+ "_shouldUseUnifiedKeyView:"
+ "_startStateTransitionAnimationsFrom:to:"
+ "_subclassAdditionalConstraints"
+ "_topRowHasTrailingAlignment"
+ "_totalVariants"
+ "_updateHoverToEnabled:"
+ "_userInteractionStateDeterminesLayerHitTestState"
+ "addQuadCurveToPoint:controlPoint:"
+ "alignmentConstraintsForKey:"
+ "alternativeTextLeftSpacing"
+ "arrayWithObjects:"
+ "arrowButtonConfig"
+ "arrowButtonHighlightBackgroundHidden"
+ "backgroundBezierPath"
+ "backgroundCornerRadius"
+ "backgroundInsets"
+ "backgroundMaskedCorners"
+ "backgroundPathForFlick"
+ "backgroundPathForLongPress"
+ "bezierPathWithRect:"
+ "cellViewsInTopDownLTROrder"
+ "center"
+ "changingSelectedVariantForKey:atPoint:isDragging:"
+ "constraintEqualToAnchor:multiplier:constant:"
+ "cornerMaskForBackground"
+ "countNonNullVariantEntriesForKey:"
+ "countryCode"
+ "createPreparedKeyFromTree:withMultiplier:type:shape:"
+ "curvedCorners"
+ "decorateVariantView"
+ "defaultEffectsType"
+ "doubleHeightKeys"
+ "drawsBackground"
+ "drawsShadows"
+ "effectsType"
+ "findRowSpanningDuplicatesForKeyplane:"
+ "flickDirection"
+ "flickPopupOffset"
+ "groupHeaderPadding"
+ "hasConstrainedBackground"
+ "hideLinesOnDisambiguationGridEdges"
+ "hitTestVariantKeyAtPoint:"
+ "hitTestingMode"
+ "idealKeySizeforLayoutType:"
+ "keyShape"
+ "keysForName:"
+ "labelInsets"
+ "layoutTypeForKey:"
+ "localizedStringForCountryCode:"
+ "localizedStringWithFormat:"
+ "maxRows"
+ "maximizeSortControlWidthWithPadding"
+ "minCellDimension"
+ "null"
+ "opacity"
+ "orderedVariantIndicesForKey"
+ "performScalingAnimationOnCellHighlight"
+ "popupDelegate"
+ "preferredKeyViewClass"
+ "rowInsets"
+ "rowsVerticalSpacing"
+ "selectorViewClassForKey:"
+ "separatedOptions.acceptsUpstreamHitTesting"
+ "separatedOptions.geometry.backBevel"
+ "separatedOptions.geometry.flatDepth"
+ "separatedOptions.geometry.frontBevel"
+ "separatedOptions.platter.enabled"
+ "separatedOptions.platter.fakeFresnelFalloff"
+ "separatedOptions.platter.fakeFresnelMaxDist"
+ "separatedOptions.platter.fakeFresnelStrength"
+ "separatedOptions.platter.fillSpecularExponent"
+ "separatedOptions.platter.fillSpecularStrength"
+ "separatedOptions.platter.frontDepthForNormals"
+ "separatedOptions.platter.mainSpecularExponent"
+ "separatedOptions.platter.mainSpecularStrength"
+ "separatedOptions.separatedThickness"
+ "separatedOptions.shadows.expansionOpacity"
+ "separatedOptions.shadows.expansionRadius"
+ "separatedOptions.shadows.expansionSize"
+ "separatedOptions.shadows.expansionTargetZ"
+ "separatedOptions.shadows.maxDynamicOffset"
+ "setColors:"
+ "setConcaveCorner:"
+ "setConcaveCornerOffset:"
+ "setCornerMaskForBackground:"
+ "setCurvedCorners:"
+ "setDoubleHeightKeys:"
+ "setEffectsType:"
+ "setEndPoint:"
+ "setFlickDirection:"
+ "setHasConstrainedBackground:"
+ "setKeyShape:"
+ "setLocations:"
+ "setOpacity:"
+ "setPopupDelegate:"
+ "setShadowPathIsBounds:"
+ "setSpacing:"
+ "setStartPoint:"
+ "setSubclassAdditionalConstraints:"
+ "setTopRowHasTrailingAlignment:"
+ "setTotalVariants:"
+ "setTransform3D:"
+ "setType:"
+ "shapeWhenMergedWithKey:insets:"
+ "shouldProvideDefaultSelection"
+ "showCellBorderForSpaceConfirmationCandidate"
+ "spaceConfirmationCandidateCellBackgroundColor"
+ "stackLayoutMargins"
+ "subclassAdditionalConstraints"
+ "sublayers"
+ "systemWhiteColor"
+ "topRowHasTrailingAlignment"
+ "totalVariants"
+ "touch down scale"
+ "touch down scale X"
+ "touch down scale Y"
+ "touch down z translation"
+ "touch down z translation reverse"
+ "touch up opacity"
+ "touch up scale"
+ "touch up z translation"
+ "touch up z translation reverse"
+ "traitsForCell"
+ "transform.scale"
+ "transform.scale.x"
+ "transform.scale.y"
+ "transform.translation.z"
+ "transform3D"
+ "transitionToHighlighted:"
+ "updateGradientLayerToCollectionView"
+ "updateStateFrom:to:"
+ "updateVariantViewPropertiesForKey:isNonVariantPaddle:"
+ "v24@0:8i16i20"
+ "v32@?0@\"CALayer\"8Q16^B24"
+ "v44@0:8@16{CGPoint=dd}24B40"
+ "variantCellWithString:"
+ "variantType"
+ "variantViewAlignment"
+ "variantViewBottomSpacing"
+ "wantsUserInteractionEnabled"
+ "widthConstraintForVariantCell:previousCell:"
+ "widthOfGridGradient"
- "\x11\x11"
- "\x14\x11"
- "!\x1a!"
- "5"
- "@\"<TUIVariantSelectorDelegate>\""
- "@40@0:8@16d24q32"
- "T@\"<TUIVariantSelectorDelegate>\",W,N,V_selectorDelegate"
- "T@\"UILayoutGuide\",&,N,V_variantLayoutGuide"
- "TUIAnimationStyleCodingKey"
- "TUIVariantSelectorDelegate"
- "TUIVariantSelectorVariantContainerGuide"
- "Tq,N,V_animationStyle"
- "Tq,N,V_preferredAnimationStyle"
- "_animationStyle"
- "_preferredAnimationStyle"
- "_selectorDelegate"
- "_variantLayoutGuide"
- "animationStyle"
- "animationStyle = %ld"
- "constraintLessThanOrEqualToAnchor:multiplier:"
- "createPreparedKeyFromTree:withMultiplier:type:"
- "initWithLanguages:animationStyle:actionHandler:"
- "layoutTypeFromDisplayType:"
- "paddleBezierPath"
- "preferredAnimationStyle"
- "q20@0:8i16"
- "selectorDelegate"
- "setAnimationStyle:"
- "setPreferredAnimationStyle:"
- "setSelectorDelegate:"
- "setVariantLayoutGuide:"
- "updateState:"
- "updateVariantRowsForKey:isNonVariantPaddle:"
- "v20@0:8i16"
- "variantLayoutGuide"

```
