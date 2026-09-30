## PosterKit

> `/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit`

```diff

-280.101.0.0.0
-  __TEXT.__text: 0x12b384
-  __TEXT.__auth_stubs: 0x2010
-  __TEXT.__objc_methlist: 0x17b2c
-  __TEXT.__const: 0x1e74
-  __TEXT.__cstring: 0x9698
-  __TEXT.__oslogstring: 0x4b29
+283.101.0.0.0
+  __TEXT.__text: 0x12cd58
+  __TEXT.__auth_stubs: 0x2040
+  __TEXT.__objc_methlist: 0x17d54
+  __TEXT.__const: 0x1e54
+  __TEXT.__cstring: 0x9748
+  __TEXT.__oslogstring: 0x4d79
   __TEXT.__gcc_except_tab: 0x265c
   __TEXT.__ustring: 0x1c
   __TEXT.__constg_swiftt: 0x844

   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x118
-  __TEXT.__unwind_info: 0x4c60
+  __TEXT.__unwind_info: 0x4d40
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x3b15
-  __TEXT.__objc_methname: 0x3c3f8
-  __TEXT.__objc_methtype: 0xb948
-  __TEXT.__objc_stubs: 0x20260
-  __DATA_CONST.__got: 0x1840
-  __DATA_CONST.__const: 0x3340
-  __DATA_CONST.__objc_classlist: 0x9e8
+  __TEXT.__objc_classname: 0x3b39
+  __TEXT.__objc_methname: 0x3c7bd
+  __TEXT.__objc_methtype: 0xb99e
+  __TEXT.__objc_stubs: 0x204c0
+  __DATA_CONST.__got: 0x1850
+  __DATA_CONST.__const: 0x3388
+  __DATA_CONST.__objc_classlist: 0x9f0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x588
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb2d8
+  __DATA_CONST.__objc_selrefs: 0xb378
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x810
-  __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x1018
-  __AUTH_CONST.__const: 0x1cd0
-  __AUTH_CONST.__cfstring: 0x91e0
-  __AUTH_CONST.__objc_const: 0x4d3c8
-  __AUTH_CONST.__objc_intobj: 0x618
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __DATA_CONST.__objc_superrefs: 0x818
+  __DATA_CONST.__objc_arraydata: 0x180
+  __AUTH_CONST.__auth_got: 0x1030
+  __AUTH_CONST.__const: 0x1cf0
+  __AUTH_CONST.__cfstring: 0x92a0
+  __AUTH_CONST.__objc_const: 0x4d7e0
+  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x38e0
+  __AUTH.__objc_data: 0x3930
   __AUTH.__data: 0x408
-  __DATA.__objc_ivar: 0x1800
+  __DATA.__objc_ivar: 0x1814
   __DATA.__data: 0x4788
-  __DATA.__bss: 0x1380
+  __DATA.__bss: 0x1390
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0x2bb0
   __DATA_DIRTY.__data: 0x2b0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 40EE0EC2-4930-3440-9393-85AE8BCBD6D2
-  Functions: 8249
-  Symbols:   27535
-  CStrings:  12782
+  UUID: F274CA13-8502-31F3-B042-E73D504CE201
+  Functions: 8300
+  Symbols:   27683
+  CStrings:  12833
 
Symbols:
+ +[PRComplicationGalleryIconProvider loadIconImageForApplicationBundleIdentifier:atWidth:completion:].cold.1
+ +[PRPosterDescriptorGalleryOptions galleryOptionsWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:]
+ +[PRPosterDescriptorGalleryTitleStyle supportsSecureCoding]
+ +[PRPosterScriptStatement statementWithSignificantEvent:significantEventsCounter:duration:]
+ +[UIFont(PRTimeFont) pr_fontWithName:forRole:includingFallbackFonts:attributes:]
+ -[FBSMutableSceneClientSettings(PREditingScene) pr_setComplicationRowMode:]
+ -[FBSMutableSceneClientSettings(PREditingScene) pr_setShouldShowEditingReticles:]
+ -[FBSSceneClientSettings(PREditingScene) pr_complicationRowMode]
+ -[FBSSceneClientSettings(PREditingScene) pr_shouldShowEditingReticles]
+ -[FBSSceneClientSettingsDiff(PREditingScene) pr_complicationRowModeDidChange]
+ -[FBSSceneClientSettingsDiff(PREditingScene) pr_shouldShowEditingReticlesDidChange]
+ -[PRComplicationContainerViewController scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
+ -[PRComplicationContainerViewController setShowsEditingReticles:]
+ -[PREditingSceneViewController setComplicationRowMode:]
+ -[PREditor setShowsEditingReticles:]
+ -[PREditorContentStylePalette withPreferredMaterialType:]
+ -[PRPosterContentCustomStyle copyWithPreferredMaterial:]
+ -[PRPosterContentDiscreteColorsStyle copyWithPreferredMaterial:]
+ -[PRPosterContentGlassMaterialStyle copyWithPreferredMaterial:]
+ -[PRPosterContentGradientStyle copyWithPreferredMaterial:]
+ -[PRPosterContentLUTStyle copyWithPreferredMaterial:]
+ -[PRPosterContentVibrantMaterialStyle copyWithPreferredMaterial:]
+ -[PRPosterContentVibrantMonochromeStyle copyWithPreferredMaterial:]
+ -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:]
+ -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:].cold.1
+ -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:].cold.2
+ -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:].cold.3
+ -[PRPosterDescriptorGalleryOptions preferredTitleStyle]
+ -[PRPosterDescriptorGalleryTitleStyle copyWithZone:]
+ -[PRPosterDescriptorGalleryTitleStyle encodeWithCoder:]
+ -[PRPosterDescriptorGalleryTitleStyle initWithCoder:]
+ -[PRPosterDescriptorGalleryTitleStyle initWithPreferredTimeMaxYPortrait:preferredTimeMaxYLandscape:]
+ -[PRPosterDescriptorGalleryTitleStyle preferredTimeMaxYLandscape]
+ -[PRPosterDescriptorGalleryTitleStyle preferredTimeMaxYPortrait]
+ -[PRPosterDescriptorGalleryTitleStyle setPreferredTimeMaxYLandscape:]
+ -[PRPosterDescriptorGalleryTitleStyle setPreferredTimeMaxYPortrait:]
+ -[PRPosterHomeScreenCustomizationConfiguration _defaultVariantsForStyleTypeOptions]
+ -[PRPosterPreferencesImpl complicationRowMode]
+ -[PRPosterPreferencesImpl setComplicationRowMode:]
+ -[PRPosterRootViewController didMoveToParentViewController:]
+ -[PRPosterRootViewController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[PRRenderer _configureProminentDisplay:]
+ -[PRRenderer _updateDepthEffectIfNeededFrom:to:animationSettings:]
+ -[PRRenderer _updateHeaderAndComplicationsFrom:to:animationSettings:]
+ -[PRRenderer _updateOrientationIfNeededFrom:to:animationSettings:]
+ -[PRRenderer _updateProminentViewSizingAndTransforms:]
+ -[PRRenderer _updateViewsIfNeededFrom:to:animationSettings:]
+ -[PRRenderingServiceMotionEvent isEqual:]
+ -[PRRenderingServiceServer dealloc]
+ -[PRWidgetGridViewController complicationsDidEndDisplaying]
+ -[PRWidgetGridViewController complicationsWillDisplay]
+ -[PRWidgetGridViewController isComplicationUserInteractionEnabled]
+ -[PRWidgetGridViewController setComplicationUserInteractionEnabled:]
+ -[PRWidgetGridViewController updatePresentationMode:]
+ -[UIFont(PRTimeFont) pr_fontWithAttributes:options:]
+ -[_PREditingPosterContentVibrantMonochromeStyleCoordinatorImpl _preferredMaterialType]
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table162
+ GCC_except_table174
+ GCC_except_table180
+ GCC_except_table311
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table341
+ GCC_except_table365
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table447
+ GCC_except_table64
+ GCC_except_table78
+ _CTFontCreateWithFontDescriptorAndOptions
+ _CTFontDescriptorCreateCopyWithAttributes
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_PRPosterDescriptorGalleryTitleStyle
+ _OBJC_IVAR_$_PREditingSceneViewController._complicationRowMode
+ _OBJC_IVAR_$_PRPosterDescriptorGalleryOptions._preferredTitleStyle
+ _OBJC_IVAR_$_PRPosterDescriptorGalleryTitleStyle._preferredTimeMaxYLandscape
+ _OBJC_IVAR_$_PRPosterDescriptorGalleryTitleStyle._preferredTimeMaxYPortrait
+ _OBJC_IVAR_$_PRPosterPreferencesImpl._complicationRowMode
+ _OBJC_IVAR_$_PRRenderer._adaptiveTimeHeight
+ _OBJC_METACLASS_$_PRPosterDescriptorGalleryTitleStyle
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _PRFontAttributesForTimeFontIdentifier
+ _PUICGRectIsValidSalientContentRectangle
+ __OBJC_$_CATEGORY_FBSSceneClientSettingsDiff_$_PREditingScene
+ __OBJC_$_CLASS_METHODS_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_$_CLASS_PROP_LIST_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_$_INSTANCE_METHODS_FBSSceneClientSettingsDiff(PREditingScene|PRRenderingScene|PRScene)
+ __OBJC_$_INSTANCE_METHODS_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_$_INSTANCE_VARIABLES_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_$_PROP_LIST_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_CLASS_PROTOCOLS_$_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_CLASS_RO_$_PRPosterDescriptorGalleryTitleStyle
+ __OBJC_METACLASS_RO_$_PRPosterDescriptorGalleryTitleStyle
+ __ZL22SPRotation3DMakeLookAt9SPPoint3DS_10SPVector3D
+ ___100+[PRComplicationGalleryIconProvider loadIconImageForApplicationBundleIdentifier:atWidth:completion:]_block_invoke_3
+ ___100+[PRComplicationGalleryIconProvider loadIconImageForApplicationBundleIdentifier:atWidth:completion:]_block_invoke_4
+ ___100+[PRComplicationGalleryIconProvider loadIconImageForApplicationBundleIdentifier:atWidth:completion:]_block_invoke_5
+ ___122-[PREditor _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.399
+ ___122-[PREditor _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.403
+ ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.109
+ ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.117
+ ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke_2.118
+ ___36-[PREditor setShowsEditingReticles:]_block_invoke
+ ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.82
+ ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.82.cold.1
+ ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.82.cold.2
+ ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.89
+ ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.90
+ ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.91
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.198
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.199
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.203
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.204
+ ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.205
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.363
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.376
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.376.cold.1
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.381
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.375
+ ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.375.cold.1
+ ___53-[PRWidgetGridViewController updatePresentationMode:]_block_invoke
+ ___54-[PRRenderer _updateProminentViewSizingAndTransforms:]_block_invoke
+ ___54-[PRRenderer _updateProminentViewSizingAndTransforms:]_block_invoke_2
+ ___59-[PRInlineComplicationGalleryViewController _buildSnapshot]_block_invoke.54
+ ___62-[PRRenderer _updateBacklightLuminanceFrom:to:animateChanges:]_block_invoke.126
+ ___66-[PRRenderer _updateOrientationIfNeededFrom:to:animationSettings:]_block_invoke
+ ___66-[PRRenderer _updateOrientationIfNeededFrom:to:animationSettings:]_block_invoke_2
+ ___70-[PRRenderingServiceServer listener:didReceiveConnection:withContext:]_block_invoke.61
+ ___75-[PRInlineComplicationGalleryViewController _makeSectionHeaderRegistration]_block_invoke.109
+ ___81-[PRPosterRootViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_2
+ ___block_descriptor_32_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s_e64_d16?0"<UISheetPresentationControllerDetentResolutionContext>"8ls32l8
+ ___block_literal_global.1059
+ ___block_literal_global.1139
+ ___block_literal_global.1725
+ ___block_literal_global.1727
+ ___block_literal_global.175
+ ___block_literal_global.176
+ ___block_literal_global.215
+ ___block_literal_global.252
+ ___block_literal_global.312
+ ___block_literal_global.336
+ ___block_literal_global.359
+ ___block_literal_global.366
+ ___block_literal_global.378
+ ___block_literal_global.405
+ ___block_literal_global.410
+ ___block_literal_global.425
+ ___block_literal_global.458
+ ___block_literal_global.49
+ ___block_literal_global.67
+ ___block_literal_global.69
+ ___block_literal_global.78
+ ___block_literal_global.92
+ _kCTFontTrackAttribute
+ _loadIconImageForApplicationBundleIdentifier:atWidth:completion:.cache
+ _loadIconImageForApplicationBundleIdentifier:atWidth:completion:.onceToken
+ _objc_msgSend$_animateWithAnimationSettings:animations:completion:
+ _objc_msgSend$_defaultVariantsForStyleTypeOptions
+ _objc_msgSend$adaptiveTimeTextHeight
+ _objc_msgSend$complicationRowMode
+ _objc_msgSend$copyWithPreferredMaterial:
+ _objc_msgSend$decodeBytesForKey:returnedLength:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$encodeBytes:length:forKey:
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:
+ _objc_msgSend$initWithPreferredTimeMaxYPortrait:preferredTimeMaxYLandscape:
+ _objc_msgSend$layoutFrame
+ _objc_msgSend$pr_complicationRowMode
+ _objc_msgSend$pr_complicationRowModeDidChange
+ _objc_msgSend$pr_fontWithAttributes:options:
+ _objc_msgSend$pr_fontWithName:forRole:includingFallbackFonts:attributes:
+ _objc_msgSend$pr_setComplicationRowMode:
+ _objc_msgSend$pr_setShouldShowEditingReticles:
+ _objc_msgSend$pr_shouldShowEditingReticles
+ _objc_msgSend$pr_shouldShowEditingReticlesDidChange
+ _objc_msgSend$pui_safelySendActions:outError:
+ _objc_msgSend$setComplicationRowMode:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$setHidesSharedBackground:
+ _objc_msgSend$setPrefersGrabberVisible:
+ _objc_msgSend$setShowsEditingReticles:
+ _objc_msgSend$statementWithDuration:
+ _objc_msgSend$statementWithSignificantEvent:significantEventsCounter:duration:
+ _objc_msgSend$updatePresentationMode:
+ _objc_msgSend$withPreferredMaterialType:
+ _pow
- +[PRPosterScriptStatement statementWithSignificantEvent:significantEventCounter:duration:]
- -[PRComplicationGalleryViewController _closeButtonTapped:]
- -[PRIncomingCallTextViewAdapterWrapper maxTextWidth]
- -[PRIncomingCallTextViewAdapterWrapper setMaxTextWidth:]
- -[PRInlineComplicationGalleryViewController _closeButtonTapped:]
- -[PRInlineComplicationGalleryViewController scrollViewDidScroll:]
- -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:]
- -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:].cold.1
- -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:].cold.2
- -[PRPosterDescriptorGalleryOptions initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:].cold.3
- -[PRRenderer _configureProminentDisplay]
- -[PRRenderer _updateDepthEffectIfNeededFrom:to:animateChanges:]
- -[PRRenderer _updateHeaderAndComplicationsFrom:to:animateChanges:]
- -[PRRenderer _updateOrientationIfNeededFrom:to:animateChanges:]
- -[PRRenderer _updateProminentViewSizingAndTransforms]
- -[PRRenderer _updateViewsIfNeededFrom:to:animateChanges:]
- GCC_except_table141
- GCC_except_table143
- GCC_except_table144
- GCC_except_table15
- GCC_except_table160
- GCC_except_table172
- GCC_except_table179
- GCC_except_table309
- GCC_except_table312
- GCC_except_table315
- GCC_except_table339
- GCC_except_table35
- GCC_except_table363
- GCC_except_table37
- GCC_except_table445
- GCC_except_table62
- GCC_except_table77
- _OBJC_CLASS_$_UINavigationBarAppearance
- _OBJC_IVAR_$_PRIncomingCallTextViewAdapterWrapper._maxTextWidth
- _UIAccessibilityIsReduceTransparencyEnabled
- __OBJC_$_CATEGORY_FBSSceneClientSettingsDiff_$_PRRenderingScene
- __OBJC_$_INSTANCE_METHODS_FBSSceneClientSettingsDiff(PRRenderingScene|PRScene)
- ___122-[PREditor _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.397
- ___122-[PREditor _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.401
- ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.103
- ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke.111
- ___124-[PRRenderer _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]_block_invoke_2.112
- ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.76
- ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.76.cold.1
- ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.76.cold.2
- ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.83
- ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.84
- ___37-[PRRenderer _issueSceneInvalidated:]_block_invoke.85
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.195
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.196
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.200
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.201
- ___40-[PRRenderer _updateRenderingExtensions]_block_invoke.202
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.365
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.378
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.378.cold.1
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke.383
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.377
- ___51-[PREditingSceneViewController _dismissWithAction:]_block_invoke_2.377.cold.1
- ___59-[PRInlineComplicationGalleryViewController _buildSnapshot]_block_invoke.57
- ___62-[PREditingContentStylePickerComponentViewController loadView]_block_invoke_2
- ___62-[PRRenderer _updateBacklightLuminanceFrom:to:animateChanges:]_block_invoke.120
- ___63-[PRRenderer _updateOrientationIfNeededFrom:to:animateChanges:]_block_invoke
- ___63-[PRRenderer _updateOrientationIfNeededFrom:to:animateChanges:]_block_invoke_2
- ___70-[PRRenderingServiceServer listener:didReceiveConnection:withContext:]_block_invoke.59
- ___75-[PRInlineComplicationGalleryViewController _makeSectionHeaderRegistration]_block_invoke.112
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.1056
- ___block_literal_global.1136
- ___block_literal_global.1722
- ___block_literal_global.1724
- ___block_literal_global.173
- ___block_literal_global.213
- ___block_literal_global.248
- ___block_literal_global.310
- ___block_literal_global.334
- ___block_literal_global.363
- ___block_literal_global.368
- ___block_literal_global.380
- ___block_literal_global.390
- ___block_literal_global.403
- ___block_literal_global.412
- ___block_literal_global.427
- ___block_literal_global.459
- ___block_literal_global.61
- ___block_literal_global.66
- ___block_literal_global.72
- ___block_literal_global.75
- ___block_literal_global.77
- ___block_literal_global.81
- ___block_literal_global.95
- _objc_msgSend$_isInAnimationBlock
- _objc_msgSend$adjustedContentInset
- _objc_msgSend$complicationGalleryViewControllerDidFinish:
- _objc_msgSend$configureWithDefaultBackground
- _objc_msgSend$configureWithOpaqueBackground
- _objc_msgSend$effectWithBlurRadius:
- _objc_msgSend$initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:
- _objc_msgSend$inlineComplicationGalleryViewControllerDidFinish:
- _objc_msgSend$setBackgroundEffects:
- _objc_msgSend$setStandardAppearance:
- _objc_msgSend$statementWithSignificantEvent:significantEventCounter:duration:
CStrings:
+ ".ADTSlabSoftNumeric-Heavy"
+ ".ADTSlabSoftNumeric-Medium"
+ ".ADTSlabSoftNumeric-Semibold"
+ ".NewYorkSoftNumeric-Heavy"
+ ".NewYorkSoftNumeric-Medium"
+ ".NewYorkSoftNumeric-Semibold"
+ ".SFRailRoundedNumeric-Heavy"
+ "<PRRenderer %p> Environment override added: %{public}@"
+ "<PRRenderer %p> Environment override removed: %{public}@"
+ "<PRRenderer %p> PREFERENCES adaptive time salient content rect override from %@ to %@"
+ "<PRRenderer %p> RENDERER Skipping adaptive time update; is the same"
+ "<PRRenderer %p> RENDERER Updating adaptive time height from %f -> %f"
+ "@\"PRPosterDescriptorGalleryTitleStyle\""
+ "@32@0:8d16d24"
+ "@44@0:8@16@24B32@36"
+ "Extending render session for reason: %{public}@"
+ "PRPosterDescriptorGalleryTitleStyle"
+ "T@\"NSNumber\",&,N"
+ "T@\"PRPosterDescriptorGalleryTitleStyle\",R,C,N,V_preferredTitleStyle"
+ "TB,N,Spr_setShouldShowEditingReticles:"
+ "TB,R,N,Gpr_shouldShowEditingReticles"
+ "TIME_STYLE_SELECTOR_GLASS"
+ "TIME_STYLE_SELECTOR_SOLID"
+ "TQ,N,Spr_setComplicationRowMode:"
+ "Vv24@0:8@\"PRRenderingServiceMotionEvent\"16"
+ "Vv24@0:8@16"
+ "[Widget Row] complicationRowMode is Automatic, using calculated layout for bottom: %{bool}u"
+ "[Widget Row] complicationRowMode is FixedBottom, forcing complications to bottom"
+ "[Widget Row] complicationRowMode is FixedTop, forcing complications to top"
+ "_adaptiveTimeHeight"
+ "_animateWithAnimationSettings:animations:completion:"
+ "_complicationRowMode"
+ "_defaultVariantsForStyleTypeOptions"
+ "_preferredTitleStyle"
+ "adaptiveTimeHeight"
+ "adaptiveTimeTextHeight"
+ "always"
+ "complicationRowMode"
+ "copyWithPreferredMaterial:"
+ "decodeBytesForKey:returnedLength:"
+ "decodeFloatForKey:"
+ "encodeBytes:length:forKey:"
+ "encodeFloat:forKey:"
+ "gallery demo"
+ "galleryOptionsWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:"
+ "initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:preferredTitleStyle:"
+ "initWithPreferredTimeMaxYPortrait:preferredTimeMaxYLandscape:"
+ "layoutFrame"
+ "pr_complicationRowMode"
+ "pr_complicationRowModeDidChange"
+ "pr_fontWithAttributes:options:"
+ "pr_fontWithName:forRole:includingFallbackFonts:attributes:"
+ "pr_setComplicationRowMode:"
+ "pr_setShouldShowEditingReticles:"
+ "pr_shouldShowEditingReticles"
+ "pr_shouldShowEditingReticlesDidChange"
+ "preferredTitleStyle"
+ "pui_safelySendActions:outError:"
+ "setComplicationRowMode:"
+ "setCountLimit:"
+ "setHidesSharedBackground:"
+ "setPrefersGrabberVisible:"
+ "setShowsEditingReticles:"
+ "shouldPreviewOverlapMenuForIconView:"
+ "statementWithSignificantEvent:significantEventsCounter:duration:"
+ "updatePresentationMode:"
+ "withPreferredMaterialType:"
+ "\x81Q"
- ".ADTSlabNumeric-Heavy"
- ".ADTSlabNumeric-Medium"
- ".NewYorkNumeric-Medium"
- "Extending render session for reason: %@"
- "Glass"
- "Solid"
- "T@\"NSNumber\",&,N,V_maxTextWidth"
- "_isInAnimationBlock"
- "_maxTextWidth"
- "aQ"
- "adjustedContentInset"
- "configureWithDefaultBackground"
- "configureWithOpaqueBackground"
- "effectWithBlurRadius:"
- "enforceLayoutInsetsForAxis:"
- "initWithAssetLookupInfo:galleryPresentationStyle:galleryDisplayStyle:"
- "maxTextWidth"
- "pui_significantEventCounter"
- "rotationVectorW"
- "rotationVectorX"
- "rotationVectorY"
- "rotationVectorZ"
- "setBackgroundEffects:"
- "setMaxTextWidth:"
- "setStandardAppearance:"
- "significantEventCounter"
- "statementWithSignificantEvent:significantEventCounter:duration:"
- "v24@0:8@\"PRRenderingServiceMotionEvent\"16"

```
