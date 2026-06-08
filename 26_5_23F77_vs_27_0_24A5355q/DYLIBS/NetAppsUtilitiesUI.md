## NetAppsUtilitiesUI

> `/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI`

```diff

 108.0.0.0.0
-  __TEXT.__text: 0x7b4c
-  __TEXT.__auth_stubs: 0x460
+  __TEXT.__text: 0x77ac
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x64f
+  __TEXT.__cstring: 0x655
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__unwind_info: 0x340
-  __TEXT.__objc_classname: 0x137
-  __TEXT.__objc_methname: 0x2240
-  __TEXT.__objc_methtype: 0x3d0
-  __TEXT.__objc_stubs: 0x1c20
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x50

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x980
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x1d0
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0xb00
   __AUTH_CONST.__objc_const: 0xdb8
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA6CBD79-216D-3D5E-A5E8-D629CEF89C6C
+  UUID: 15CD52AE-8A94-37F6-984A-299BEED67C4D
   Functions: 243
-  Symbols:   1023
-  CStrings:  620
+  Symbols:   1028
+  CStrings:  194
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[UIView(NAUIAutolayoutDebugging) _naui_beginDebuggingAutolayout] : 780 -> 760
~ _NAStringFromCGRect : 228 -> 216
~ -[NADescriptionBuilder(NAUIAdditions) appendCGPoint:withName:] : 160 -> 156
~ -[NADescriptionBuilder(NAUIAdditions) appendCGSize:withName:] : 160 -> 156
~ -[NADescriptionBuilder(NAUIAdditions) appendCGRect:withName:] : 148 -> 144
~ -[NAUITextStyleDescriptor descriptorByAddingSymbolicTraits:removingSymbolicTraits:] : 172 -> 168
~ -[NAUITextStyleDescriptor descriptorByDisallowingAccessibilitySizes] : 148 -> 144
~ -[NAUITextStyleDescriptor descriptorByDisallowingSmallSizes] : 148 -> 144
~ +[NAUITextStyleDescriptor fontWithTextStyleDescriptor:] : 220 -> 204
~ +[NAUITextStyleDescriptor defaultFontForTextStyleDescriptor:] : 116 -> 108
~ ___38+[NAUITextStyleDescriptor na_identity]_block_invoke : 84 -> 68
~ ___38+[NAUITextStyleDescriptor na_identity]_block_invoke_2 : 228 -> 204
~ -[NAUITextStyleDescriptor description] : 260 -> 248
~ -[NAUITextStyleDescriptor hash] : 72 -> 68
~ -[NAUITextStyleDescriptor isEqual:] : 100 -> 96
~ -[NAUITextStyleDescriptor copyWithZone:] : 40 -> 4
~ -[UITableView(NAUIAdditions) naui_applyGroupedItemDiff:] : 1176 -> 1100
~ +[UIFont(NAUIAdditions) naui_ultraLightMonospacedFontOfSize:] : 472 -> 444
~ -[UIFont(NAUIAdditions) naui_dynamicFontTextStyleDescriptor] : 216 -> 200
~ _NAUICurrentContentSizeCategoryIsLargerThanOrEqualToCategory : 308 -> 304
~ _NAUIEnumerateContentSizeCategoriesInIncreasingOrder : 492 -> 496
~ ___NAUICurrentContentSizeCategoryIsLargerThanOrEqualToCategory_block_invoke : 144 -> 136
~ _NAUIShortDescriptionFromUIContentSizeCategory : 484 -> 480
~ ___NAUIEnumerateContentSizeCategoriesInIncreasingOrder_block_invoke : 376 -> 364
~ +[NSLayoutConstraint(NAUIAdditions) naui_areConstraints:equalToConstraints:] : 228 -> 224
~ -[NSLayoutConstraint(NAUIAdditions) naui_isEqualToConstraint:] : 328 -> 312
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsByCenteringView:withView:alongAxes:offset:] : 272 -> 264
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsByAttachingView:toView:alongEdges:relatedBy:insets:] : 452 -> 436
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsBySizingView:toSize:] : 268 -> 256
~ +[NSLayoutConstraint(NAUIAdditions) naui_viewsInConstraints:] : 480 -> 464
~ +[NSLayoutConstraint(NAUIAdditions) naui_constraintsWithVisualFormat:options:metrics:views:label:] : 352 -> 348
~ -[NSLayoutConstraint(NAUIAdditions) naui_debugIdentifierWithBaseLabel:] : 268 -> 252
~ -[NSLayoutConstraint(NAUIAdditions) naui_setIdentifierWithLabel:] : 88 -> 84
~ +[NAUIContentSizeLayoutConstraint _constraintForAutoitem:constrainedItem:attribute:relatedBy:toItem:attribute:multiplier:defaultConstant:additionalConstant:initialize:] : 380 -> 388
~ +[NAUIContentSizeLayoutConstraint constraintForAutoitem:additionalConstant:constantLoadingBlock:] : 172 -> 168
~ +[NAUIContentSizeLayoutConstraint constraintForAutoitem:additionalConstant:constantWidthSizingStringsLoadingBlock:] : 236 -> 240
~ ___115+[NAUIContentSizeLayoutConstraint constraintForAutoitem:additionalConstant:constantWidthSizingStringsLoadingBlock:]_block_invoke : 140 -> 132
~ -[NAUIContentSizeLayoutConstraint setDefaultConstant:] : 32 -> 36
~ -[NAUIContentSizeLayoutConstraint setAutoUpdatingConstantShrinks:] : 32 -> 36
~ -[NAUIContentSizeLayoutConstraint _defaultConstantByFixingUpDefaultConstant:] : 272 -> 256
~ _UIScreenPixelHeight : 80 -> 76
~ +[NAUIContentSizeLayoutConstraint _maximumWidthOfStrings:withFont:] : 336 -> 344
~ -[NAUIContentSizeLayoutConstraint _reloadPreferredContentSize:] : 504 -> 516
~ -[NAUIContentSizeLayoutConstraint autoUpdatingConstantShrinks] : 16 -> 20
~ -[NAUIContentSizeLayoutConstraint defaultConstant] : 16 -> 20
~ -[NAUIContentSizeLayoutConstraint additionalConstant] : 16 -> 20
~ -[NAUIContentSizeLayoutConstraint setAdditionalConstant:] : 16 -> 20
~ -[NAUIContentSizeLayoutConstraint textStyle] : 16 -> 20
~ -[NAUIContentSizeLayoutConstraint constantLoadingBlock] : 16 -> 20
~ _NAUILayoutMetricsForUIEdgeInsetsNamed : 488 -> 448
~ _UIEdgeInsetKeyNamed : 148 -> 144
~ -[UILabel(NAUIAdditions) naui_capOffsetFromTop] : 104 -> 96
~ -[UILabel(NAUIAdditions) naui_reloadDynamicFontWithTextStyleDescriptor:] : 536 -> 524
~ ___72-[UILabel(NAUIAdditions) naui_reloadDynamicFontWithTextStyleDescriptor:]_block_invoke : 340 -> 328
~ -[NAUILayoutConstraintSet initWithOwningView:constraintBuilder:] : 188 -> 192
~ -[NAUILayoutConstraintSet isActive] : 56 -> 52
~ -[NAUILayoutConstraintSet activateIfNeeded] : 272 -> 252
~ -[NAUILayoutConstraintSet invalidate] : 176 -> 168
~ -[NAUILayoutConstraintSet updateConstraintConstants] : 608 -> 584
~ ___52-[NAUILayoutConstraintSet updateConstraintConstants]_block_invoke : 364 -> 356
~ -[NAIdentityBuilder(NAUIAdditions) appendCGFloatCharacteristic:withRole:] : 220 -> 216
~ -[NAIdentityBuilder(NAUIAdditions) appendCGPointCharacteristic:withRole:] : 204 -> 200
~ -[NAIdentityBuilder(NAUIAdditions) appendCGRectCharacteristic:withRole:] : 204 -> 200
~ +[UITableViewCell(NAUIAdditions) naui_estimatedTableRowHeight] : 96 -> 92
~ -[UIView(NAUIAutolayoutDebugging) naui_descendantsWithAmbiguousLayout] : 388 -> 368
~ +[_NAUIAmbigousLayoutView installOnView:forVariable:] : 928 -> 900
~ -[_NAUIAmbigousLayoutView drawRect:] : 428 -> 424
~ +[NAUIDeviceUtilities naui_isPad] : 72 -> 68
~ +[NAUIDeviceUtilities naui_shouldUseLargeiPadLayout] : 136 -> 128
~ +[NAUIDeviceUtilities naui_isUsingLandscapeOrientation] : 76 -> 72
~ ___37+[NAUIDeviceUtilities productVersion]_block_invoke : 72 -> 68
~ ___42+[NAUIDeviceUtilities productBuildVersion]_block_invoke : 72 -> 68
~ ___34+[NAUIDeviceUtilities productType]_block_invoke : 72 -> 68
~ ___43+[NAUIDeviceUtilities productHardwareModel]_block_invoke : 72 -> 68
~ ___47+[NAUIDeviceUtilities productHardwareModelName]_block_invoke : 72 -> 68
~ ___35+[NAUIDeviceUtilities productClass]_block_invoke : 72 -> 68
~ ___43+[NAUIDeviceUtilities localizedProductName]_block_invoke : 72 -> 68
~ ___42+[NAUIDeviceUtilities operatingSystemName]_block_invoke : 72 -> 68
~ ___45+[NAUIDeviceUtilities uniqueDeviceIdentifier]_block_invoke : 72 -> 68
~ ___38+[NAUIDeviceUtilities mainScreenScale]_block_invoke : 84 -> 80
~ -[UIViewController(NAUIAdditions) naui_addChildViewWithViewController:] : 108 -> 104
~ -[UIViewController(NAUIAdditions) naui_addChildViewWithViewController:toView:] : 140 -> 132
~ -[UIViewController(NAUIAdditions) naui_canAnimate] : 60 -> 56
~ -[UIViewController(NAUIAdditions) naui_isHorizontalSizeClassRegularOrGreater] : 76 -> 72
~ -[UIViewController(NAUIAdditions) naui_isVerticalSizeClassRegularOrGreater] : 76 -> 72
~ -[UIViewController(NAUIAdditions) naui_loadViewIfNecessary] : 48 -> 44
~ -[UIViewController(NAUIAdditions) naui_isDescendantOfViewController:] : 108 -> 104
~ -[UIViewController(NAUIUIKitDebugging) _recursiveDescriptionWithInset:] : 600 -> 564
~ _NSStringFromUIInterfaceOrientationMask : 204 -> 196
~ -[NAUIUIViewControllerNoticationObserver init] : 592 -> 568
~ ___46-[NAUIUIViewControllerNoticationObserver init]_block_invoke : 92 -> 88
~ ___46-[NAUIUIViewControllerNoticationObserver init]_block_invoke_2 : 92 -> 88
~ -[UIView(NAUIAdditions) naui_showAllViewBoundsRecursively:] : 392 -> 388
~ -[UIView(NAUIAdditions) naui_setDynamicFontTextStyleDescriptor:] : 276 -> 264
~ -[UIView(NAUIAdditions) naui_dynamicFontTextStyleDescriptor] : 120 -> 112
~ -[UIView(NAUIAdditions) naui_canAnimate] : 88 -> 84
~ +[UIView(NAUIAdditions) naui_performAnimateableChangesWithAnimationDuration:setupBlock:animatablesBlock:completion:] : 216 -> 220
~ -[UIView(NAUIAdditions) naui_performAnimateableConstraintChanges:] : 400 -> 384
~ -[UIView(NAUIAdditions) naui_addAutoLayoutSubview:] : 96 -> 88
~ -[UIView(NAUIAdditions) naui_reloadDynamicFontWithTextStyleDescriptor:] : 132 -> 128
~ -[UIView(NAUIAdditions) naui_replaceConstraint:withConstraints:] : 112 -> 116
~ -[UIView(NAUIAdditions) naui_replaceConstraints:withConstraints:] : 120 -> 124
~ -[UIView(NAUIAdditions) _naui_constraintsByNameDictionary:] : 144 -> 136
~ -[UIView(NAUIAdditions) _naui_constraintsNamed:] : 120 -> 112
~ -[UIView(NAUIAdditions) naui_setNamedConstraints:forName:] : 268 -> 252
~ -[UIView(NAUIAdditions) naui_removeConstraintsNamed:] : 212 -> 192
~ -[UIView(NAUIAdditions) naui_removeNamedConstraints] : 284 -> 280
~ -[_NAUIAutoUpdatingFontObserver initWithTarget:] : 416 -> 408
~ +[_NAUIAutoUpdatingFontObserver canObserveFontsForTarget:] : 148 -> 140
~ -[_NAUIAutoUpdatingFontObserver updateDyamicFontForCurrentContentSize] : 348 -> 336
~ -[_NAUIAutoUpdatingFontObserver dealloc] : 104 -> 100
~ +[_NAUIAmbigousLayoutView installOnView:forVariable:].cold.1 : 140 -> 96
CStrings:
+ "MarketingProductName"
+ "SupportsForceTouch"
- ".cxx_destruct"
- "@"
- "@\"NAUITextStyleDescriptor\""
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"UIView\""
- "@\"UIViewController\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8I16I20"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@32@0:8@16@?24"
- "@32@0:8@?16q24"
- "@32@0:8d16@24"
- "@36@0:8@16I24B28B32"
- "@40@0:8@16@24@32"
- "@40@0:8@16d24@?32"
- "@40@0:8@16{CGSize=dd}24"
- "@40@0:8d16@24Q32"
- "@40@0:8{CGPoint=dd}16@32"
- "@40@0:8{CGSize=dd}16@32"
- "@56@0:8@16@24Q32{UIOffset=dd}40"
- "@56@0:8@16Q24@32@40@48"
- "@56@0:8@16q24@32q40d48"
- "@56@0:8@16q24q32@40d48"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "@72@0:8@16@24Q32{UIEdgeInsets=dddd}40"
- "@72@0:8@16q24q32@40q48d56d64"
- "@80@0:8@16@24Q32q40{UIEdgeInsets=dddd}48"
- "@80@0:8@16@24q32q40@48q56d64d72"
- "@92@0:8@16@24q32q40@48q56d64d72d80B88"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8{CGSize=dd}16"
- "I"
- "I16@0:8"
- "NAUIAdditions"
- "NAUIAutolayoutDebugging"
- "NAUIContentSizeLayoutConstraint"
- "NAUIDeviceUtilities"
- "NAUILayoutConstraintSet"
- "NAUITextStyleDescriptor"
- "NAUIUIKitDebugging"
- "NAUIUIViewControllerNoticationObserver"
- "NAUIWeakRef"
- "NSCopying"
- "Q16@0:8"
- "T@\"NAUITextStyleDescriptor\",&,N,Snaui_setDynamicFontTextStyleDescriptor:"
- "T@\"NAUITextStyleDescriptor\",R,N"
- "T@\"NSArray\",C,N,V_constraints"
- "T@\"NSArray\",R,N,V_constraints"
- "T@\"NSString\",C,N,V_textStyle"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_textStyle"
- "T@\"NSString\",R,N,V_name"
- "T@\"UIView\",R,W,N,V_owningView"
- "T@\"UIViewController\",W,N,V_viewController"
- "T@,R,C,N,V_stalenessToken"
- "T@,R,W,N,V_target"
- "T@?,C,N,V_constantLoadingBlock"
- "T@?,R,C,N,V_builder"
- "TB,N,V_autoUpdatingConstantShrinks"
- "TB,R,N"
- "TB,R,N,GisActive"
- "TB,R,N,V_allowsAccessibilitySizes"
- "TB,R,N,V_allowsSmallSizes"
- "TI,R,N,V_symbolicTraits"
- "Td,N,V_additionalConstant"
- "Td,N,V_defaultConstant"
- "Td,R,N"
- "Ti,R,N"
- "_NAUIAmbigousLayoutView"
- "_NAUIAutoUpdatingFontObserver"
- "_NAUINamedViewConstraints"
- "_additionalConstant"
- "_allDescriptions"
- "_allowsAccessibilitySizes"
- "_allowsAccessibilityTextStyleSizes"
- "_allowsSmallSizes"
- "_applicationKeyWindow"
- "_autoUpdatingConstantShrinks"
- "_autoitem"
- "_baselineOffsetFromBottom"
- "_bodyLeading"
- "_builder"
- "_constantLoadingBlock"
- "_constraintForAutoitem:constrainedItem:attribute:relatedBy:toItem:attribute:multiplier:defaultConstant:additionalConstant:initialize:"
- "_constraints"
- "_defaultConstant"
- "_defaultConstantByFixingUpDefaultConstant:"
- "_dynamicTextStyleDescriptor"
- "_forceUpdatePreferredContentSize"
- "_isConstantUpdatingConstraint"
- "_layoutVariablesWithAmbiguousValue"
- "_maximumWidthOfStrings:withFont:"
- "_name"
- "_naui_beginDebuggingAutolayout"
- "_naui_constraintsByNameDictionary:"
- "_naui_constraintsNamed:"
- "_notificationObserver"
- "_observations"
- "_owningView"
- "_preferredContentSizeDidChangeObserver"
- "_recursiveDescriptionWithInset:"
- "_reloadPreferredContentSize:"
- "_stalenessToken"
- "_symbolicTraits"
- "_target"
- "_textStyle"
- "_textStyleDefaultBodyLeading"
- "_updatePreferredContentSize"
- "_useWeakStorage"
- "_viewController"
- "_weakPointer"
- "_weakStorage"
- "activateConstraints:"
- "activateIfNeeded"
- "active"
- "addAttribute:value:range:"
- "addChildViewController:"
- "addConstraint:"
- "addConstraints:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserverForName:object:queue:usingBlock:"
- "addSubview:"
- "additionalConstant"
- "allKeys"
- "allowsAccessibilitySizes"
- "allowsWeakReference"
- "animateWithDuration:animations:completion:"
- "appendBool:withName:"
- "appendCGFloat:withName:"
- "appendCGFloat:withName:decimalPrecision:"
- "appendCGFloatCharacteristic:"
- "appendCGFloatCharacteristic:withRole:"
- "appendCGPoint:withName:"
- "appendCGPointCharacteristic:"
- "appendCGPointCharacteristic:withRole:"
- "appendCGRect:withName:"
- "appendCGRectCharacteristic:"
- "appendCGRectCharacteristic:withRole:"
- "appendCGSize:withName:"
- "appendCharacteristic:"
- "appendCharacteristic:withRole:comparatorBlock:hashBlock:"
- "appendDouble:withName:decimalPrecision:"
- "appendObject:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendSuper"
- "appendUnsignedInteger:withName:"
- "areAnimationsEnabled"
- "array"
- "arrayWithObjects:count:"
- "ascender"
- "attributedText"
- "autoUpdatingConstantShrinks"
- "baselineConstraintForAutoitem:relation:toView:attribute:defaultConstant:"
- "baselineConstraintForView:attribute:relation:toAutoitem:defaultConstant:"
- "beginUpdates"
- "boolForKey:"
- "borderStyle"
- "bounds"
- "build"
- "builder"
- "builderWithObject:"
- "canObserveFontsForTarget:"
- "capHeight"
- "characterAtIndex:"
- "childViewControllers"
- "colorWithRed:green:blue:alpha:"
- "componentsJoinedByString:"
- "constant"
- "constantLoadingBlock"
- "constraintForAutoitem:additionalConstant:constantLoadingBlock:"
- "constraintForAutoitem:additionalConstant:constantWidthSizingStringsLoadingBlock:"
- "constraintForAutoitem:attribute:relatedBy:toItem:attribute:multiplier:defaultConstant:"
- "constraintForAutoitem:constrainedItem:attribute:relatedBy:toItem:attribute:multiplier:defaultConstant:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "constraints"
- "constraintsWithVisualFormat:options:metrics:views:"
- "convertPoint:fromView:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "d32@0:8@16@24"
- "d32@0:8d16@24"
- "deactivateConstraints:"
- "dealloc"
- "defaultCenter"
- "defaultConstant"
- "defaultFontForTextStyle:"
- "defaultFontForTextStyleDescriptor:"
- "deleteRowsAtIndexPaths:withRowAnimation:"
- "deleteSections:withRowAnimation:"
- "description"
- "descriptorByAddingSymbolicTraits:removingSymbolicTraits:"
- "descriptorByDisallowingAccessibilitySizes"
- "descriptorByDisallowingSmallSizes"
- "descriptorWithTextStyle:"
- "deviceClass"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "drawRect:"
- "eQd5mlz0BN0amTp/2ccMoA"
- "endUpdates"
- "enumerateAttribute:inRange:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "exerciseAmbiguityInLayout"
- "firstAnchor"
- "firstAttribute"
- "firstItem"
- "font"
- "fontAttributes"
- "fontDescriptor"
- "fontDescriptorByAddingAttributes:"
- "fontWithDescriptor:size:"
- "fontWithTextStyleDescriptor:"
- "frame"
- "fromIndex"
- "fromIndexPath"
- "groupOperations"
- "hasAmbiguousLayout"
- "hasOrbCapability"
- "hash"
- "hashOfObject:"
- "horizontalSizeClass"
- "i16@0:8"
- "indexSetWithIndex:"
- "init"
- "initWithFrame:"
- "initWithName:constraints:stalenessToken:"
- "initWithOwningView:constraintBuilder:"
- "initWithStyle:reuseIdentifier:"
- "initWithTarget:"
- "initWithTextStyle:symbolicTraits:allowsAccessibilitySizes:allowsSmallSizes:"
- "insertRowsAtIndexPaths:withRowAnimation:"
- "insertSections:withRowAnimation:"
- "installOnView:forVariable:"
- "intValue"
- "integerValue"
- "intrinsicContentSize"
- "invalidate"
- "isActive"
- "isDescendantOfView:"
- "isEqual:"
- "isEqualToString:"
- "isObject:equalToObject:"
- "itemOperations"
- "j9Th5smJpdztHwc+i39zIg"
- "keyWindow"
- "layoutIfNeeded"
- "length"
- "localizedProductName"
- "mainQueue"
- "mainScreen"
- "mainScreenScale"
- "moveRowAtIndexPath:toIndexPath:"
- "moveSection:toSection:"
- "multiplier"
- "mutableCopy"
- "na_firstObjectPassingTest:"
- "na_identity"
- "name"
- "naui_addAutoLayoutSubview:"
- "naui_addAutoLayoutSubviews:"
- "naui_addChildViewWithViewController:"
- "naui_addChildViewWithViewController:toView:"
- "naui_addConstraint:"
- "naui_addConstraints:"
- "naui_applicationDidEnterBackground"
- "naui_applicationWillEnterForeground"
- "naui_applyGroupedItemDiff:"
- "naui_areConstraints:equalToConstraints:"
- "naui_baselineOffsetFromBottom"
- "naui_beginDisablingAnimations"
- "naui_canAnimate"
- "naui_capOffsetFromTop"
- "naui_constraintsByAttachingView:toView:alongEdges:insets:"
- "naui_constraintsByAttachingView:toView:alongEdges:relatedBy:insets:"
- "naui_constraintsByCenteringView:withView:alongAxes:offset:"
- "naui_constraintsBySizingView:toSize:"
- "naui_constraintsWithVisualFormat:options:metrics:views:label:"
- "naui_containsCJKScripts"
- "naui_debugIdentifierWithBaseLabel:"
- "naui_descendantsWithAmbiguousLayout"
- "naui_distanceFromBaselineToCoordinate:inView:"
- "naui_endDisablingAnimations"
- "naui_estimatedTableRowHeight"
- "naui_hasAxisWithRegularSizeClassOrGreater"
- "naui_isDescendantOfViewController:"
- "naui_isEqualToConstraint:"
- "naui_isHorizontalSizeClassRegularOrGreater"
- "naui_isPad"
- "naui_isProperDescendantOfView:"
- "naui_isUsingLandscapeOrientation"
- "naui_isVerticalSizeClassRegularOrGreater"
- "naui_loadViewIfNecessary"
- "naui_performAnimateableChangesWithAnimationDuration:setupBlock:animatablesBlock:completion:"
- "naui_performAnimateableConstraintChanges:"
- "naui_prepareToAutolayoutProperDescendantsOfView:inConstraints:"
- "naui_prototypeCell"
- "naui_reloadDynamicFontWithTextStyleDescriptor:"
- "naui_removeConstraint:"
- "naui_removeConstraints:"
- "naui_removeConstraintsNamed:"
- "naui_removeNamedConstraints"
- "naui_replaceConstraint:withConstraints:"
- "naui_replaceConstraints:withConstraints:"
- "naui_setDynamicFontTextStyleDescriptor:"
- "naui_setIdentifierWithLabel:"
- "naui_setNamedConstraints:forName:"
- "naui_shouldUseLargeiPadLayout"
- "naui_shouldUseLargeiPadLayoutForSize:"
- "naui_showAllViewBoundsRecursively:"
- "naui_supportsAutoLayout"
- "naui_tableRowHeight"
- "naui_ultraLightMonospacedFontOfSize:"
- "naui_viewsInConstraints:"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "object"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operatingSystemName"
- "orangeColor"
- "owningView"
- "parentViewController"
- "performWithoutAnimation:"
- "preferredContentSizeCategory"
- "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
- "priority"
- "productBuildVersion"
- "productClass"
- "productHardwareModel"
- "productHardwareModelName"
- "productType"
- "productVersion"
- "recursiveDescription"
- "relation"
- "reloadRowsAtIndexPaths:withRowAnimation:"
- "reloadSections:withRowAnimation:"
- "removeConstraint:"
- "removeConstraints:"
- "removeObjectForKey:"
- "removeObserver:"
- "scale"
- "secondAnchor"
- "secondAttribute"
- "secondItem"
- "setAdditionalConstant:"
- "setAnimationsEnabled:"
- "setAttributedText:"
- "setAutoUpdatingConstantShrinks:"
- "setBackgroundColor:"
- "setClipsToBounds:"
- "setConstant:"
- "setConstantLoadingBlock:"
- "setConstraints:"
- "setDefaultConstant:"
- "setFill"
- "setFont:"
- "setIdentifier:"
- "setNeedsLayout"
- "setNeedsUpdateConstraints"
- "setObject:forKey:"
- "setOpaque:"
- "setText:"
- "setTextStyle:"
- "setTintColor:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setViewController:"
- "sharedApplication"
- "stalenessToken"
- "standardUserDefaults"
- "statusBarOrientation"
- "stringWithFormat:"
- "subviews"
- "symbolicTraits"
- "systemLayoutSizeFittingSize:"
- "target"
- "tintColor"
- "toIndex"
- "toIndexPath"
- "traitCollection"
- "type"
- "uniqueDeviceIdentifier"
- "unsignedIntegerValue"
- "updateConstraintConstants"
- "updateConstraintsIfNeeded"
- "updateDyamicFontForCurrentContentSize"
- "userInterfaceIdiom"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v32@0:8@16@24"
- "v48@0:8d16@?24@?32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "valueForKey:"
- "valueWithCGPoint:"
- "valueWithCGRect:"
- "verticalSizeClass"
- "view"
- "viewController"
- "viewForLastBaselineLayout"
- "weakRefWithObject:"
- "window"

```
