## NetAppsUtilitiesUI

> `/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI`

```diff

-107.0.0.0.0
-  __TEXT.__text: 0x7744
-  __TEXT.__auth_stubs: 0x4b0
+108.0.0.0.0
+  __TEXT.__text: 0x7b4c
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0x64f
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__unwind_info: 0x340
   __TEXT.__objc_classname: 0x137
   __TEXT.__objc_methname: 0x2240
   __TEXT.__objc_methtype: 0x3d0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x980
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x268
+  __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0xb00
   __AUTH_CONST.__objc_const: 0xdb8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35DE5495-3371-3271-9DCB-45FFB829356B
+  UUID: 1EE4E29E-8E9B-3810-9C46-3C36E5051698
   Functions: 243
-  Symbols:   1028
+  Symbols:   1023
   CStrings:  620
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ +[UIView(NAUIAutolayoutDebugging) _naui_beginDebuggingAutolayout] : 760 -> 780
~ _NAStringFromCGRect : 216 -> 228
~ -[NADescriptionBuilder(NAUIAdditions) appendCGPoint:withName:] : 156 -> 160
~ -[NADescriptionBuilder(NAUIAdditions) appendCGSize:withName:] : 156 -> 160
~ -[NADescriptionBuilder(NAUIAdditions) appendCGRect:withName:] : 144 -> 148
~ -[NAUITextStyleDescriptor descriptorByAddingSymbolicTraits:removingSymbolicTraits:] : 168 -> 172
~ -[NAUITextStyleDescriptor descriptorByDisallowingAccessibilitySizes] : 144 -> 148
~ -[NAUITextStyleDescriptor descriptorByDisallowingSmallSizes] : 144 -> 148
~ +[NAUITextStyleDescriptor fontWithTextStyleDescriptor:] : 204 -> 220
~ +[NAUITextStyleDescriptor defaultFontForTextStyleDescriptor:] : 108 -> 116
~ ___38+[NAUITextStyleDescriptor na_identity]_block_invoke : 68 -> 84
~ ___38+[NAUITextStyleDescriptor na_identity]_block_invoke_2 : 204 -> 228
~ -[NAUITextStyleDescriptor description] : 248 -> 260
~ -[NAUITextStyleDescriptor hash] : 68 -> 72
~ -[NAUITextStyleDescriptor isEqual:] : 96 -> 100
~ -[NAUITextStyleDescriptor copyWithZone:] : 4 -> 40
~ -[UITableView(NAUIAdditions) naui_applyGroupedItemDiff:] : 1092 -> 1176
~ +[UIFont(NAUIAdditions) naui_ultraLightMonospacedFontOfSize:] : 444 -> 472
~ -[UIFont(NAUIAdditions) naui_dynamicFontTextStyleDescriptor] : 200 -> 216
~ _NAUICurrentContentSizeCategoryIsLargerThanOrEqualToCategory : 304 -> 308
~ _NAUIEnumerateContentSizeCategoriesInIncreasingOrder : 496 -> 492
~ ___NAUICurrentContentSizeCategoryIsLargerThanOrEqualToCategory_block_invoke : 136 -> 144
~ _NAUIShortDescriptionFromUIContentSizeCategory : 480 -> 484
~ ___NAUIEnumerateContentSizeCategoriesInIncreasingOrder_block_invoke : 364 -> 376
~ +[NSLayoutConstraint(NAUIAdditions) naui_areConstraints:equalToConstraints:] : 224 -> 228
~ -[NSLayoutConstraint(NAUIAdditions) naui_isEqualToConstraint:] : 312 -> 328
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsByCenteringView:withView:alongAxes:offset:] : 264 -> 272
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsByAttachingView:toView:alongEdges:relatedBy:insets:] : 436 -> 452
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsBySizingView:toSize:] : 256 -> 268
~ +[NSLayoutConstraint(NAUIAdditions) naui_viewsInConstraints:] : 460 -> 480
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsWithVisualFormat:options:metrics:views:label:] : 344 -> 352
~ -[NSLayoutConstraint(NAUIAdditions) naui_debugIdentifierWithBaseLabel:] : 252 -> 268
~ -[NSLayoutConstraint(NAUIAdditions) naui_setIdentifierWithLabel:] : 84 -> 88
~ +[NAUIContentSizeLayoutConstraint _constraintForAutoitem:constrainedItem:attribute:relatedBy:toItem:attribute:multiplier:defaultConstant:additionalConstant:initialize:] : 364 -> 380
~ +[NAUIContentSizeLayoutConstraint constraintForAutoitem:additionalConstant:constantLoadingBlock:] : 168 -> 172
~ +[NAUIContentSizeLayoutConstraint constraintForAutoitem:additionalConstant:constantWidthSizingStringsLoadingBlock:] : 240 -> 236
~ ___115+[NAUIContentSizeLayoutConstraint constraintForAutoitem:additionalConstant:constantWidthSizingStringsLoadingBlock:]_block_invoke : 132 -> 140
~ -[NAUIContentSizeLayoutConstraint dealloc] : 124 -> 128
~ -[NAUIContentSizeLayoutConstraint setTextStyle:] : 448 -> 464
~ -[NAUIContentSizeLayoutConstraint _defaultConstantByFixingUpDefaultConstant:] : 256 -> 272
~ _UIScreenPixelHeight : 76 -> 80
~ +[NAUIContentSizeLayoutConstraint _maximumWidthOfStrings:withFont:] : 340 -> 336
~ -[NAUIContentSizeLayoutConstraint _reloadPreferredContentSize:] : 492 -> 504
~ _NAUILayoutMetricsForUIEdgeInsetsNamed : 448 -> 488
~ _UIEdgeInsetKeyNamed : 144 -> 148
~ -[UILabel(NAUIAdditions) naui_capOffsetFromTop] : 96 -> 104
~ -[UILabel(NAUIAdditions) naui_reloadDynamicFontWithTextStyleDescriptor:] : 524 -> 536
~ ___72-[UILabel(NAUIAdditions) naui_reloadDynamicFontWithTextStyleDescriptor:]_block_invoke : 328 -> 340
~ -[NAUILayoutConstraintSet initWithOwningView:constraintBuilder:] : 192 -> 188
~ -[NAUILayoutConstraintSet isActive] : 52 -> 56
~ -[NAUILayoutConstraintSet activateIfNeeded] : 252 -> 272
~ -[NAUILayoutConstraintSet invalidate] : 168 -> 176
~ -[NAUILayoutConstraintSet updateConstraintConstants] : 580 -> 608
~ ___52-[NAUILayoutConstraintSet updateConstraintConstants]_block_invoke : 356 -> 364
~ -[NAIdentityBuilder(NAUIAdditions) appendCGFloatCharacteristic:withRole:] : 216 -> 220
~ -[NAIdentityBuilder(NAUIAdditions) appendCGPointCharacteristic:withRole:] : 200 -> 204
~ -[NAIdentityBuilder(NAUIAdditions) appendCGRectCharacteristic:withRole:] : 200 -> 204
~ +[UITableViewCell(NAUIAdditions) naui_estimatedTableRowHeight] : 92 -> 96
~ -[UIView(NAUIAutolayoutDebugging) naui_descendantsWithAmbiguousLayout] : 364 -> 388
~ +[_NAUIAmbigousLayoutView installOnView:forVariable:] : 900 -> 928
~ -[_NAUIAmbigousLayoutView drawRect:] : 424 -> 428
~ +[NAUIDeviceUtilities naui_isPad] : 68 -> 72
~ +[NAUIDeviceUtilities naui_shouldUseLargeiPadLayout] : 128 -> 136
~ +[NAUIDeviceUtilities naui_isUsingLandscapeOrientation] : 72 -> 76
~ ___37+[NAUIDeviceUtilities productVersion]_block_invoke : 68 -> 72
~ ___42+[NAUIDeviceUtilities productBuildVersion]_block_invoke : 68 -> 72
~ ___34+[NAUIDeviceUtilities productType]_block_invoke : 68 -> 72
~ ___43+[NAUIDeviceUtilities productHardwareModel]_block_invoke : 68 -> 72
~ ___47+[NAUIDeviceUtilities productHardwareModelName]_block_invoke : 68 -> 72
~ ___35+[NAUIDeviceUtilities productClass]_block_invoke : 68 -> 72
~ ___43+[NAUIDeviceUtilities localizedProductName]_block_invoke : 68 -> 72
~ ___42+[NAUIDeviceUtilities operatingSystemName]_block_invoke : 68 -> 72
~ ___45+[NAUIDeviceUtilities uniqueDeviceIdentifier]_block_invoke : 68 -> 72
~ ___38+[NAUIDeviceUtilities mainScreenScale]_block_invoke : 80 -> 84
~ -[UIViewController(NAUIAdditions) naui_addChildViewWithViewController:] : 104 -> 108
~ -[UIViewController(NAUIAdditions) naui_addChildViewWithViewController:toView:] : 132 -> 140
~ -[UIViewController(NAUIAdditions) naui_canAnimate] : 56 -> 60
~ -[UIViewController(NAUIAdditions) naui_isHorizontalSizeClassRegularOrGreater] : 72 -> 76
~ -[UIViewController(NAUIAdditions) naui_isVerticalSizeClassRegularOrGreater] : 72 -> 76
~ -[UIViewController(NAUIAdditions) naui_loadViewIfNecessary] : 44 -> 48
~ -[UIViewController(NAUIAdditions) naui_isDescendantOfViewController:] : 104 -> 108
~ -[UIViewController(NAUIUIKitDebugging) _recursiveDescriptionWithInset:] : 560 -> 600
~ _NSStringFromUIInterfaceOrientationMask : 196 -> 204
~ -[NAUIUIViewControllerNoticationObserver init] : 568 -> 592
~ ___46-[NAUIUIViewControllerNoticationObserver init]_block_invoke : 88 -> 92
~ ___46-[NAUIUIViewControllerNoticationObserver init]_block_invoke_2 : 88 -> 92
~ -[NAUIUIViewControllerNoticationObserver dealloc] : 312 -> 316
~ -[UIView(NAUIAdditions) naui_showAllViewBoundsRecursively:] : 384 -> 392
~ -[UIView(NAUIAdditions) naui_setDynamicFontTextStyleDescriptor:] : 264 -> 276
~ -[UIView(NAUIAdditions) naui_dynamicFontTextStyleDescriptor] : 112 -> 120
~ -[UIView(NAUIAdditions) naui_canAnimate] : 84 -> 88
~ +[UIView(NAUIAdditions) naui_performAnimateableChangesWithAnimationDuration:setupBlock:animatablesBlock:completion:] : 220 -> 216
~ -[UIView(NAUIAdditions) naui_performAnimateableConstraintChanges:] : 384 -> 400
~ -[UIView(NAUIAdditions) naui_addAutoLayoutSubview:] : 88 -> 96
~ -[UIView(NAUIAdditions) naui_addAutoLayoutSubviews:] : 240 -> 244
~ +[UIView(NAUIAdditions) naui_prepareToAutolayoutProperDescendantsOfView:inConstraints:] : 296 -> 300
~ -[UIView(NAUIAdditions) naui_reloadDynamicFontWithTextStyleDescriptor:] : 128 -> 132
~ -[UIView(NAUIAdditions) naui_replaceConstraint:withConstraints:] : 116 -> 112
~ -[UIView(NAUIAdditions) naui_replaceConstraints:withConstraints:] : 124 -> 120
~ -[UIView(NAUIAdditions) _naui_constraintsByNameDictionary:] : 140 -> 144
~ -[UIView(NAUIAdditions) _naui_constraintsNamed:] : 112 -> 120
~ -[UIView(NAUIAdditions) naui_setNamedConstraints:forName:] : 252 -> 268
~ -[UIView(NAUIAdditions) naui_removeConstraintsNamed:] : 192 -> 212
~ -[UIView(NAUIAdditions) naui_removeNamedConstraints] : 276 -> 284
~ -[_NAUIAutoUpdatingFontObserver initWithTarget:] : 408 -> 416
~ +[_NAUIAutoUpdatingFontObserver canObserveFontsForTarget:] : 140 -> 148
~ -[_NAUIAutoUpdatingFontObserver updateDyamicFontForCurrentContentSize] : 336 -> 348
~ -[_NAUIAutoUpdatingFontObserver dealloc] : 100 -> 104

```
