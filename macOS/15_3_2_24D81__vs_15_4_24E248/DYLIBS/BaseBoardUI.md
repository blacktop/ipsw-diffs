## BaseBoardUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/BaseBoardUI.framework/Versions/A/BaseBoardUI`

```diff

-694.3.4.0.0
-  __TEXT.__text: 0x18414
+694.5.5.0.0
+  __TEXT.__text: 0x183cc
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x1528
+  __TEXT.__objc_methlist: 0x1924
   __TEXT.__const: 0x3e8
-  __TEXT.__gcc_except_tab: 0x2e14
+  __TEXT.__gcc_except_tab: 0x2e1c
   __TEXT.__cstring: 0x1113
   __TEXT.__oslogstring: 0x71e
-  __TEXT.__unwind_info: 0xdf8
+  __TEXT.__unwind_info: 0xde8
   __TEXT.__objc_classname: 0x441
   __TEXT.__objc_methname: 0x4f09
   __TEXT.__objc_methtype: 0xf69

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f8
+  __DATA_CONST.__objc_selrefs: 0x1500
   __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0x34e0
+  __AUTH_CONST.__objc_const: 0x2dc8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x9b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EF25738-550C-3DBB-A9F4-662443B3B7B3
-  Functions: 528
+  UUID: 4CD63CC3-90E2-3099-B448-22A578ABFC12
+  Functions: 526
   Symbols:   1988
   CStrings:  1363
 
Functions:
~ -[BSUICAPackageView initWithURL:] : 924 -> 920
~ +[BSUIVibrancyEffectValues _colorizedVibrancyMatrixForType:heroColor:backgroundType:] : 820 -> 804
~ +[BSUIVibrancyShadowValues _shadowColorMatrixForType:heroColor:backgroundType:] : 264 -> 260
- sub_1cba1c878
~ -[BSUIFontProvider preferredFontForTextStyle:hiFontStyle:] : 152 -> 156
~ -[BSUIFontProvider preferredFontForTextStyle:hiFontStyle:contentSizeCategory:] : 176 -> 180
~ -[BSUIMappedImageCacheRegistry tmpPath] : 1032 -> 1024
~ -[BSUIMappedImageCache initWithUniqueIdentifier:options:] : 3024 -> 3056
~ -[BSUIMappedImageCache dealloc] : 1124 -> 1136
~ __workBlockGenerator : 1800 -> 1812
~ ____workBlockGenerator_block_invoke : 1272 -> 1236
~ ___workBlockGenerator_block_invoke.236 : 808 -> 784
~ -[BSUIRelativeDateLabel constructLabelString] : 1424 -> 1416
- sub_1cba24378
~ +[BSUIMappedSurfaceImage writeSurfaceImage:toFileDescriptor:] : 1396 -> 1384
~ __BSUI_Private_IsN84 : 68 -> 72
~ -[UIViewController(BaseBoardUI) bs_beginAppearanceTransitionForChildViewController:toVisible:animated:] : 536 -> 540
~ -[UIViewController(BaseBoardUI) bs_endAppearanceTransitionForChildViewController:] : 504 -> 508
~ ___98-[UIViewController(BaseBoardUI) bs_addChildViewController:withSuperview:animated:transitionBlock:]_block_invoke_2 : 308 -> 312
~ ___87-[UIViewController(BaseBoardUI) bs_removeChildViewController:animated:transitionBlock:]_block_invoke_2 : 344 -> 348
~ -[BSUIScrollView setContentOffset:animated:] : 240 -> 236
~ -[BSUIScrollView _setCurrentContentOffsetImmediatelyIfScrollInterruptionAnimated:] : 132 -> 136
~ -[BSUIScrollView _setContentOffset:animation:] : 272 -> 268
~ -[BSUIMappedImageCacheFuture cacheImage] : 344 -> 332
~ +[CATransaction(BaseBoardUI) bs_performAfterSynchronizedCommit:] : 888 -> 896
~ +[CATransaction(BaseBoardUI) bs_performAfterCommit:] : 888 -> 896
~ -[BSUIDefaultDateLabel setTimeZoneRelativeStartDate:absoluteStartDate:] : 156 -> 152
~ -[BSUIDefaultDateLabel setTimeZoneRelativeEndDate:] : 156 -> 152
~ -[BSUIDefaultDateLabel _constructNonAllDayLabelStringWithDate:startTime:startIsToday:sameDayDates:eventOngoing:withCurrentDate:forStartLabel:] : 716 -> 720
~ -[BSUIDefaultDateLabel constructLabelString] : 2908 -> 2912
~ -[BSUIDefaultDateLabel updateTextIfNecessary:] : 280 -> 284
~ -[BSUIDefaultDateLabel _forceUpdate] : 480 -> 484
~ -[BSUIDefaultDateLabel update] : 40 -> 44
~ -[BSUIDefaultDateLabel stopCoalescingUpdates] : 80 -> 92
~ __BSUITransformFromOrientationToOrientation : 260 -> 244
~ -[BSUIOrientationTransformWrapperView setContentOrientation:] : 104 -> 96
~ -[BSUIOrientationTransformWrapperView _updateGeometry] : 680 -> 672
~ +[BSUIVibrancyView isDisabled] : 68 -> 72
~ -[BSUIVibrancyView _updateFilterViewsIfNeeded] : 32 -> 36
~ -[BSUIVibrancyEffectView setIsEnabled:] : 92 -> 84
~ -[BSUIVibrancyEffectView _updateSubviewsIfNeeded] : 28 -> 32
~ -[BSUIVibrancyEffectView _updateSubviews] : 744 -> 740
~ -[BSUIVibrancyShadowView _defaultGradientColors] : 248 -> 244

```
