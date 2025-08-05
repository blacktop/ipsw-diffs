## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x8d1dc
+289.103.0.0.0
+  __TEXT.__text: 0x8dbc8
   __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_methlist: 0xa3e4
-  __TEXT.__const: 0xab4
-  __TEXT.__oslogstring: 0x3471
-  __TEXT.__cstring: 0x5c52
-  __TEXT.__gcc_except_tab: 0x166c
+  __TEXT.__objc_methlist: 0xa3b4
+  __TEXT.__const: 0xa94
+  __TEXT.__oslogstring: 0x3581
+  __TEXT.__cstring: 0x5cd2
+  __TEXT.__gcc_except_tab: 0x16b0
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x502
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x2648
-  __TEXT.__objc_classname: 0x174a
-  __TEXT.__objc_methname: 0x18571
-  __TEXT.__objc_methtype: 0x3f66
-  __TEXT.__objc_stubs: 0x10c60
-  __DATA_CONST.__got: 0xe40
-  __DATA_CONST.__const: 0x2558
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __TEXT.__unwind_info: 0x2690
+  __TEXT.__objc_classname: 0x1713
+  __TEXT.__objc_methname: 0x187df
+  __TEXT.__objc_methtype: 0x3e41
+  __TEXT.__objc_stubs: 0x10c80
+  __DATA_CONST.__got: 0xe28
+  __DATA_CONST.__const: 0x2588
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54f0
+  __DATA_CONST.__objc_selrefs: 0x5520
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1b0
   __AUTH_CONST.__auth_got: 0xe28
   __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x6620
-  __AUTH_CONST.__objc_const: 0x1dec0
+  __AUTH_CONST.__cfstring: 0x66c0
+  __AUTH_CONST.__objc_const: 0x1db68
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x2320
+  __AUTH.__objc_data: 0x21e0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xb64
-  __DATA.__data: 0x1720
+  __DATA.__objc_ivar: 0xb70
+  __DATA.__data: 0x16c0
   __DATA.__bss: 0x7e0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0C4F4854-1D4A-3BC4-87AC-FBF18C5C9246
-  Functions: 3846
-  Symbols:   13799
-  CStrings:  6658
+  UUID: 08880029-EAFB-318C-83BA-53F15CFBD0EF
+  Functions: 3851
+  Symbols:   13797
+  CStrings:  6671
 
Symbols:
+ +[PUIStylePickerHomeScreenTintSourceControl defaultDiameter]
+ +[RBSAssertion(PosterUIFoundation) pui_snapshottingAssertionForTarget:auditToken:posterProviderBundleIdentifier:]
+ -[FBSMutableSceneClientSettings(PosterUIFoundation) pui_setPowerlogIdentifier:]
+ -[FBSSceneClientSettings(PosterUIFoundation) pui_powerlogIdentifier]
+ -[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]
+ -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:]
+ -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:].cold.1
+ -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:].cold.2
+ -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:].cold.3
+ -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:].cold.4
+ -[PUIPosterSnapshotRequest retryCount]
+ -[PUIPosterSnapshotter copyWithZone:]
+ -[PUIPosterSnapshotter delegate]
+ -[PUIPosterSnapshotter sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]
+ -[PUIPosterSnapshotter setDelegate:]
+ -[PUIStylePickerHomeScreenComponentViewController setVariantPickerWrapperView:]
+ -[PUIStylePickerHomeScreenComponentViewController variantPickerWrapperView]
+ -[PUIStylePickerHomeScreenItemVariantPicker _updateSegmentWidths]
+ -[PUIStylePickerHomeScreenItemVariantPicker calculatedWidthForAvailableWidth:]
+ -[PUIStylePickerHomeScreenItemVariantPicker layoutSubviews]
+ -[PUIStylePickerHomeScreenItemView _descriptorAppearanceForStyleTypeOption:styleTypeVariant:]
+ -[PUIStylePickerHomeScreenItemView _descriptorAppearanceVariantForStyleTypeOption:]
+ -[PUIStylePickerHomeScreenItemView layoutSubviews]
+ -[PUIStylePickerHomeScreenItemView selectionViewWidthConstraint]
+ -[PUIStylePickerHomeScreenItemView setSelectionViewWidthConstraint:]
+ -[PUIStylePickerHomeScreenTintSourceControl _imageViewForEnabled:]
+ -[PUIStylePickerHomeScreenTintSourceControl setEnabled:]
+ -[_PUIStylePickerHomeScreenVariantPickerWrapperView layoutSubviews]
+ GCC_except_table26
+ GCC_except_table47
+ GCC_except_table83
+ _OBJC_CLASS_$__PUIStylePickerHomeScreenVariantPickerWrapperView
+ _OBJC_IVAR_$_PUIPosterSnapshotRequest._retryCount
+ _OBJC_IVAR_$_PUIPosterSnapshotter._delegate
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenComponentViewController._variantPickerWrapperView
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._idealSegmentWidths
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._lastKnownWidth
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._segmentMinimumWidth
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._totalIdealWidth
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenItemView._imageContainerView
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenItemView._selectionViewWidthConstraint
+ _OBJC_METACLASS_$__PUIStylePickerHomeScreenVariantPickerWrapperView
+ __OBJC_$_CLASS_METHODS_PUIStylePickerHomeScreenTintSourceControl
+ __OBJC_$_INSTANCE_METHODS__PUIStylePickerHomeScreenVariantPickerWrapperView
+ __OBJC_CLASS_RO_$__PUIStylePickerHomeScreenVariantPickerWrapperView
+ __OBJC_METACLASS_RO_$__PUIStylePickerHomeScreenVariantPickerWrapperView
+ ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.103
+ ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.103.cold.1
+ ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke
+ ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke.43
+ ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke_2
+ ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke_2.44
+ ___98-[PUIPosterSnapshotter sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]_block_invoke
+ ___98-[PUIPosterSnapshotter sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]_block_invoke.34
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.356
+ ___block_literal_global.90
+ _objc_msgSend$_descriptorAppearanceForStyleTypeOption:styleTypeVariant:
+ _objc_msgSend$_descriptorAppearanceVariantForStyleTypeOption:
+ _objc_msgSend$_imageViewForEnabled:
+ _objc_msgSend$_setUseSpringBoardVibrancy:
+ _objc_msgSend$_teardownSceneSynchronously:sceneWasDeactivated:
+ _objc_msgSend$_updateSegmentWidths
+ _objc_msgSend$calculatedWidthForAvailableWidth:
+ _objc_msgSend$constraintLessThanOrEqualToConstant:
+ _objc_msgSend$defaultDiameter
+ _objc_msgSend$floatValue
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$preferredMaxLayoutWidth
+ _objc_msgSend$pui_snapshottingAssertionForTarget:auditToken:posterProviderBundleIdentifier:
+ _objc_msgSend$sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:
+ _objc_msgSend$selectionViewWidthConstraint
+ _objc_msgSend$setSelectionViewWidthConstraint:
+ _objc_msgSend$setWidth:forSegmentAtIndex:
+ _objc_msgSend$sizeWithAttributes:
+ _objc_msgSend$snapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:
- +[PUIPosterSceneSnapshotter teardownScene:sceneWasDeactivated:]
- +[PUIStylePickerHomeScreenItemVariantPicker _cornerRadiusForTraitCollection:size:]
- -[PUIPosterSceneSnapshotter _teardownScene:]
- -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:]
- -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:].cold.1
- -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:].cold.2
- -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:].cold.3
- -[PUIPosterSnapshotRequest initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:].cold.4
- -[PUIStylePickerHomeScreenItemVariantPicker _segmentedControlAppearance]
- -[_PUIStylePickerMicaAssetView .cxx_destruct]
- -[_PUIStylePickerMicaAssetView _layoutPackageView]
- -[_PUIStylePickerMicaAssetView iconSize]
- -[_PUIStylePickerMicaAssetView initWithFrame:]
- -[_PUIStylePickerMicaAssetView intrinsicContentSize]
- -[_PUIStylePickerMicaAssetView layoutSubviews]
- -[_PUIStylePickerMicaAssetView publishedObjectNames]
- -[_PUIStylePickerMicaAssetView publishedObjectWithName:]
- -[_PUIStylePickerMicaAssetView setIconSize:]
- -[_PUIStylePickerMicaAssetView setState:]
- -[_PUIStylePickerMicaAssetView setState:animated:]
- -[_PUIStylePickerMicaAssetView setState:animated:transitionSpeed:completion:]
- -[_PUIStylePickerMicaAssetView setState:onLayer:animated:transitionSpeed:completion:]
- -[_PUIStylePickerMicaAssetView setStateControllerDelegate:]
- -[_PUIStylePickerMicaAssetView stateControllerDelegate]
- -[_PUIStylePickerMicaAssetView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:]
- -[_PUIStylePickerMicaAssetView updateAsset:bundle:]
- GCC_except_table32
- GCC_except_table82
- _OBJC_CLASS_$_BSUICAPackageView
- _OBJC_CLASS_$__PUIStylePickerHomeScreenItemBorderView
- _OBJC_CLASS_$__PUIStylePickerMicaAssetView
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._font
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._normalTextColor
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._selectedTextColor
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemView._selectedBorderView
- _OBJC_IVAR_$__PUIStylePickerMicaAssetView._iconSize
- _OBJC_IVAR_$__PUIStylePickerMicaAssetView._packageView
- _OBJC_METACLASS_$__PUIStylePickerHomeScreenItemBorderView
- _OBJC_METACLASS_$__PUIStylePickerMicaAssetView
- _UIFontWeightMedium
- __OBJC_$_INSTANCE_METHODS__PUIStylePickerMicaAssetView
- __OBJC_$_INSTANCE_VARIABLES__PUIStylePickerMicaAssetView
- __OBJC_$_PROP_LIST_PUIStylePickerMicaAssetControlling
- __OBJC_$_PROP_LIST__PUIStylePickerMicaAssetView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PUIStylePickerMicaAssetControlling
- __OBJC_$_PROTOCOL_METHOD_TYPES_PUIStylePickerMicaAssetControlling
- __OBJC_$_PROTOCOL_REFS_PUIStylePickerMicaAssetControlling
- __OBJC_CLASS_PROTOCOLS_$__PUIStylePickerMicaAssetView
- __OBJC_CLASS_RO_$__PUIStylePickerHomeScreenItemBorderView
- __OBJC_CLASS_RO_$__PUIStylePickerMicaAssetView
- __OBJC_LABEL_PROTOCOL_$_PUIStylePickerMicaAssetControlling
- __OBJC_METACLASS_RO_$__PUIStylePickerHomeScreenItemBorderView
- __OBJC_METACLASS_RO_$__PUIStylePickerMicaAssetView
- __OBJC_PROTOCOL_$_PUIStylePickerMicaAssetControlling
- ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.116
- ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.116.cold.1
- ___63+[PUIPosterSceneSnapshotter teardownScene:sceneWasDeactivated:]_block_invoke
- ___63-[PUIPosterSnapshotter sceneSnapshotterDidFinish:result:error:]_block_invoke.34
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.103
- ___block_literal_global.361
- _objc_msgSend$_layoutPackageView
- _objc_msgSend$_segmentedControlAppearance
- _objc_msgSend$_setSegmentedControlAppearance:
- _objc_msgSend$_teardownScene:
- _objc_msgSend$initWithPackageName:inBundle:
- _objc_msgSend$label
- _objc_msgSend$lineHeight
- _objc_msgSend$publishedObjectNames
- _objc_msgSend$setBorderOffset:
- _objc_msgSend$setNeedsUpdateConstraints
- _objc_msgSend$setState:animated:
- _objc_msgSend$setState:animated:transitionSpeed:completion:
- _objc_msgSend$setState:onLayer:animated:transitionSpeed:completion:
- _objc_msgSend$setStateControllerDelegate:
- _objc_msgSend$stateControllerDelegate
- _objc_msgSend$systemBlackColor
- _objc_msgSend$systemFontOfSize:weight:
- _objc_msgSend$teardownScene:sceneWasDeactivated:
CStrings:
+ "\r5"
+ "(%{public}@) Extension process interrupted in state '%{public}@'. Invalidating scene snapshotter: %{public}@"
+ "(%{public}@) Signaling scene invalidation"
+ "(%{public}@) Signaling scene invalidation %{public}@"
+ "(%{public}@) calling PUIPosterSceneSnapshotter invalidate. isComplete: %{public}d"
+ "(%{public}@, pid: %{public}d) _mainQueue_finishWithError: Called on already-complete snapshot session"
+ "(%{public}@, pid: %{public}d) _mainQueue_finishWithError:'%{public}@' result:'%@'; runtime: %f"
+ "(%{public}@, pid: %{public}d) scene torn down"
+ "(%{public}@, pid: %{public}d) sceneWillDeactivate:'%@' withError:'%@'"
+ "-Entitled"
+ "-Nominal"
+ "-Photos"
+ "@\"<PUIPosterSnapshotterDelegate>\""
+ "@\"UIView<PUIStylePickerMicaAssetControlling>\""
+ "@\"_PUIStylePickerHomeScreenVariantPickerWrapperView\""
+ "@64@0:8@16@?24q32@40Q48d56"
+ "H:|[imageContainerView]|"
+ "Snapshotter state error: shouldn't call %s in %{public}@ state"
+ "T@\"<PUIPosterSnapshotterDelegate>\",W,N,V_delegate"
+ "T@\"NSLayoutConstraint\",&,N,V_selectionViewWidthConstraint"
+ "T@\"_PUIStylePickerHomeScreenVariantPickerWrapperView\",&,N,V_variantPickerWrapperView"
+ "TQ,N,Spui_setPowerlogIdentifier:"
+ "TQ,N,V_retryCount"
+ "TQ,R,N,V_retryCount"
+ "V:|[imageContainerView]-interitemSpacing-[label]|"
+ "WaitingForSceneInvalidation"
+ "_PUIStylePickerHomeScreenVariantPickerWrapperView"
+ "_descriptorAppearanceForStyleTypeOption:styleTypeVariant:"
+ "_descriptorAppearanceVariantForStyleTypeOption:"
+ "_idealSegmentWidths"
+ "_imageContainerView"
+ "_imageViewForEnabled:"
+ "_lastKnownWidth"
+ "_segmentMinimumWidth"
+ "_selectionViewWidthConstraint"
+ "_setUseSpringBoardVibrancy:"
+ "_teardownSceneSynchronously:sceneWasDeactivated:"
+ "_totalIdealWidth"
+ "_updateSegmentWidths"
+ "_variantPickerWrapperView"
+ "after scene invalidation completion"
+ "calculatedWidthForAvailableWidth:"
+ "constraintLessThanOrEqualToConstant:"
+ "defaultDiameter"
+ "floatValue"
+ "imageContainerView, imageView, label"
+ "immediately"
+ "initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:"
+ "numberWithFloat:"
+ "preferredMaxLayoutWidth"
+ "pui_powerlogIdentifier"
+ "pui_setPowerlogIdentifier:"
+ "pui_snapshottingAssertionForTarget:auditToken:posterProviderBundleIdentifier:"
+ "sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:"
+ "selectionViewWidthConstraint"
+ "setEnabled:"
+ "setSelectionViewWidthConstraint:"
+ "setVariantPickerWrapperView:"
+ "setWidth:forSegmentAtIndex:"
+ "sizeWithAttributes:"
+ "snapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:"
+ "v36@0:8@\"PUIPosterSceneSnapshotter\"16B24@\"PUIPosterSnapshotRequest\"28"
+ "v36@0:8@16B24@28"
+ "variantPickerWrapperView"
+ "\xb1"
- "\r4"
- "(%{public}@) Extension process interrupted while snapshotting: %{public}@"
- "(%{public}@) _mainQueue_finishWithError: Called on already-complete snapshot session"
- "(%{public}@) _mainQueue_finishWithError:'%{public}@' result:'%@'; runtime: %f"
- "(%{public}@) scene torn down"
- "(%{public}@) sceneWillDeactivate:'%@' withError:'%@'"
- "@\"BSUICAPackageView\""
- "@\"CALayer\"24@0:8@\"NSString\"16"
- "@\"NSObject<CAStateControllerDelegate>\"16@0:8"
- "@\"_PUIStylePickerMicaAssetView\""
- "@56@0:8@16@?24q32@40d48"
- "B24@0:8@\"NSString\"16"
- "B28@0:8@\"NSString\"16B24"
- "B44@0:8@\"NSString\"16B24d28@?<v@?B>36"
- "B44@0:8@16B24d28@?36"
- "B52@0:8@\"NSString\"16@\"CALayer\"24B32d36@?<v@?B>44"
- "B52@0:8@16@24B32d36@?44"
- "H:|[assetView]|"
- "PUIStylePickerMicaAssetControlling"
- "PosterUpdate"
- "Snapshotter state error: shouldn't call %s in PUIPosterSnapshotterStateSnapshotting"
- "T@\"NSObject<CAStateControllerDelegate>\",W,N"
- "Ti,N,V_retryCount"
- "V:|[assetView]-interitemSpacing-[label]|"
- "_PUIStylePickerHomeScreenItemBorderView"
- "_PUIStylePickerMicaAssetView"
- "_cornerRadiusForTraitCollection:size:"
- "_layoutPackageView"
- "_normalTextColor"
- "_packageView"
- "_segmentedControlAppearance"
- "_selectedBorderView"
- "_selectedTextColor"
- "_setSegmentedControlAppearance:"
- "_teardownScene:"
- "assetView, label"
- "d28@0:8@16i24"
- "i16@0:8"
- "initWithPackageName:inBundle:"
- "initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:"
- "lineHeight"
- "publishedObjectNames"
- "setBorderOffset:"
- "setNeedsUpdateConstraints"
- "setState:animated:"
- "setState:animated:transitionSpeed:completion:"
- "setState:onLayer:animated:transitionSpeed:completion:"
- "setStateControllerDelegate:"
- "stateControllerDelegate"
- "systemBlackColor"
- "systemFontOfSize:weight:"
- "teardownScene:sceneWasDeactivated:"
- "v20@0:8i16"
- "v24@0:8@\"NSObject<CAStateControllerDelegate>\"16"
- "v32@0:8@\"NSString\"16@\"NSBundle\"24"
- "{?=@dd{?=@@@@@{CGSize=dd}}{?=@@@@@{CGSize=dd}}{?=@@@@@{CGSize=dd}}{?=@@@@@{CGSize=dd}}B}16@0:8"

```
