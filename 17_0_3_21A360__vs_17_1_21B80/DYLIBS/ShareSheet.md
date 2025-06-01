## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-1936.10.1.2.18
-  __TEXT.__text: 0xa8d24
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0xc8f8
-  __TEXT.__const: 0x410
-  __TEXT.__cstring: 0x611e
+1936.20.66.2.11
+  __TEXT.__text: 0xaa218
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0xcaa0
+  __TEXT.__const: 0x430
+  __TEXT.__cstring: 0x6173
   __TEXT.__ustring: 0xca
-  __TEXT.__oslogstring: 0x5870
-  __TEXT.__gcc_except_tab: 0x185c
-  __TEXT.__dlopen_cstrs: 0x63f
-  __TEXT.__unwind_info: 0x2bdc
-  __TEXT.__objc_classname: 0x2020
-  __TEXT.__objc_methname: 0x28f19
-  __TEXT.__objc_methtype: 0x6940
-  __TEXT.__objc_stubs: 0x19de0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x2420
-  __DATA_CONST.__objc_classlist: 0x580
-  __DATA_CONST.__objc_catlist: 0x10
+  __TEXT.__oslogstring: 0x58f7
+  __TEXT.__gcc_except_tab: 0x1858
+  __TEXT.__dlopen_cstrs: 0x68f
+  __TEXT.__unwind_info: 0x2c2c
+  __TEXT.__objc_classname: 0x2053
+  __TEXT.__objc_methname: 0x292b9
+  __TEXT.__objc_methtype: 0x6969
+  __TEXT.__objc_stubs: 0x19fa0
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x2460
+  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x24398
-  __DATA_CONST.__objc_selrefs: 0x78f8
+  __DATA_CONST.__objc_const: 0x245f0
+  __DATA_CONST.__objc_selrefs: 0x79c0
   __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__cfstring: 0x49e0
-  __AUTH_CONST.__objc_const: 0x44d8
-  __AUTH_CONST.__const: 0xfc0
+  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__objc_const: 0x45a8
+  __AUTH_CONST.__const: 0xfe0
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x728
-  __AUTH.__objc_data: 0x1b30
-  __AUTH.__data: 0x168
+  __AUTH_CONST.__auth_got: 0x738
+  __AUTH.__objc_data: 0x1c20
+  __AUTH.__data: 0x170
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0xaa0
-  __DATA.__objc_superrefs: 0x398
-  __DATA.__objc_ivar: 0x1218
-  __DATA.__data: 0x2a38
-  __DATA.__bss: 0x458
-  __DATA_DIRTY.__objc_data: 0x1bd0
+  __DATA.__objc_classrefs: 0xab0
+  __DATA.__objc_superrefs: 0x3a0
+  __DATA.__objc_ivar: 0x1238
+  __DATA.__data: 0x2a40
+  __DATA.__bss: 0x470
+  __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0x268
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 991BFF51-1A72-3089-A132-C08D6A259892
-  Functions: 5045
-  Symbols:   18400
-  CStrings:  8704
+  UUID: 22CD1586-567D-3689-8054-E06964C24808
+  Functions: 5086
+  Symbols:   18533
+  CStrings:  8748
 
Symbols:
+ -[SHSheetAction initWithType:]
+ -[SHSheetAction type]
+ -[SHSheetContentLayoutProvider _resolvedDirectionalLayoutMargins:trailingMargin:]
+ -[SHSheetMetadataChangedAction initWithSerializedMetadata:]
+ -[SHSheetMetadataChangedAction serializedMetadata]
+ -[SHSheetMetadataUpdateAction initWithSerializedMetadata:]
+ -[SHSheetMetadataUpdateAction metadata]
+ -[SHSheetMetadataUpdateAction serializedMetadata]
+ -[SHSheetPresentationBlockingRootView .cxx_destruct]
+ -[SHSheetPresentationBlockingRootView containerView]
+ -[SHSheetPresentationBlockingRootView descriptionLabel]
+ -[SHSheetPresentationBlockingRootView didMoveToSuperview]
+ -[SHSheetPresentationBlockingRootView hasAppliedConstraints]
+ -[SHSheetPresentationBlockingRootView initWithFrame:]
+ -[SHSheetPresentationBlockingRootView setContainerView:]
+ -[SHSheetPresentationBlockingRootView setDescriptionLabel:]
+ -[SHSheetPresentationBlockingRootView setHasAppliedConstraints:]
+ -[SHSheetPresentationBlockingRootView setTitleLabel:]
+ -[SHSheetPresentationBlockingRootView titleLabel]
+ -[SHSheetPresentationBlockingRootView updateConstraints]
+ -[SHSheetPresentationBlockingViewController .cxx_destruct]
+ -[SHSheetPresentationBlockingViewController _createSystemCloseButton]
+ -[SHSheetPresentationBlockingViewController _handleClose]
+ -[SHSheetPresentationBlockingViewController closeButton]
+ -[SHSheetPresentationBlockingViewController loadView]
+ -[SHSheetPresentationBlockingViewController setCloseButton:]
+ -[SHSheetScene fenceCompletionHandler]
+ -[SHSheetScene setFenceCompletionHandler:]
+ -[SHSheetSceneSpecification uiSceneMinimumClass]
+ -[SHSheetSceneViewController scene:didReceiveMetadataUpdateAction:]
+ -[SHSheetWindowScene _usesMinimumSafeAreaInsets]
+ -[UIActivityActionGroupCell _legacyIconSizeForContentSizeCategory:]
+ -[UIAirDropGroupActivityCell isLongPressable]
+ -[UIAirDropGroupActivityCell setLongPressable:]
+ -[UIDevice(ShareSheet) setSh_hostUserInterfaceIdiom:]
+ -[UIDevice(ShareSheet) sh_hostUserInterfaceIdiom]
+ -[UIPrintActivity _cleanup]
+ -[_UIActivityBundleHelper imageForApplicationIconFormat:activityCategory:contentSizeCategory:]
+ -[_UIActivityContentSectionHeaderView leftAlignHeaderText]
+ -[_UIActivityContentSectionHeaderView prepareForReuse]
+ -[_UIActivityContentSectionHeaderView setTitleLabelTopConstraint:]
+ -[_UIActivityContentSectionHeaderView titleLabelTopConstraint]
+ GCC_except_table36
+ _OBJC_CLASS_$_SHSheetMetadataUpdateAction
+ _OBJC_CLASS_$_SHSheetPresentationBlockingRootView
+ _OBJC_CLASS_$_SHSheetWindowScene
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_IVAR_$_SHSheetPresentationBlockingRootView._containerView
+ _OBJC_IVAR_$_SHSheetPresentationBlockingRootView._descriptionLabel
+ _OBJC_IVAR_$_SHSheetPresentationBlockingRootView._hasAppliedConstraints
+ _OBJC_IVAR_$_SHSheetPresentationBlockingRootView._titleLabel
+ _OBJC_IVAR_$_SHSheetPresentationBlockingViewController._closeButton
+ _OBJC_IVAR_$_SHSheetScene._fenceCompletionHandler
+ _OBJC_IVAR_$_UIAirDropGroupActivityCell._longPressable
+ _OBJC_IVAR_$__UIActivityContentSectionHeaderView._titleLabelTopConstraint
+ _OBJC_METACLASS_$_SHSheetMetadataUpdateAction
+ _OBJC_METACLASS_$_SHSheetPresentationBlockingRootView
+ _OBJC_METACLASS_$_SHSheetWindowScene
+ _OBJC_METACLASS_$_UIWindowScene
+ _SFFilterStringsFromList
+ _SFGenerateTypeList
+ _SHSheetUserInterfaceIdiomPropertyKey
+ _UIFontTextStyleTitle1
+ __OBJC_$_CATEGORY_UIDevice_$_ShareSheet
+ __OBJC_$_INSTANCE_METHODS_SHSheetMetadataUpdateAction
+ __OBJC_$_INSTANCE_METHODS_SHSheetPresentationBlockingRootView
+ __OBJC_$_INSTANCE_METHODS_SHSheetWindowScene
+ __OBJC_$_INSTANCE_METHODS_UIDevice(ShareSheet)
+ __OBJC_$_INSTANCE_VARIABLES_SHSheetPresentationBlockingRootView
+ __OBJC_$_INSTANCE_VARIABLES_SHSheetPresentationBlockingViewController
+ __OBJC_$_PROP_LIST_SHSheetMetadataUpdateAction
+ __OBJC_$_PROP_LIST_SHSheetPresentationBlockingRootView
+ __OBJC_$_PROP_LIST_SHSheetPresentationBlockingViewController
+ __OBJC_CLASS_RO_$_SHSheetMetadataUpdateAction
+ __OBJC_CLASS_RO_$_SHSheetPresentationBlockingRootView
+ __OBJC_CLASS_RO_$_SHSheetWindowScene
+ __OBJC_METACLASS_RO_$_SHSheetMetadataUpdateAction
+ __OBJC_METACLASS_RO_$_SHSheetPresentationBlockingRootView
+ __OBJC_METACLASS_RO_$_SHSheetWindowScene
+ __ShareSheetIsRealityLauncher
+ __ShareSheetIsRealityLauncher.isRealityLauncher
+ __ShareSheetIsRealityLauncher.onceToken
+ ___41-[SHSheetSceneViewController viewDidLoad]_block_invoke
+ ___45-[SHSheetSceneViewController reloadMetadata:]_block_invoke
+ ___45-[SHSheetSceneViewController reloadMetadata:]_block_invoke_2
+ ___55-[SHSheetScene updateWithChange:transitionCoordinator:]_block_invoke_3
+ ___55-[SHSheetScene updateWithChange:transitionCoordinator:]_block_invoke_4
+ ____ShareSheetIsRealityLauncher_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_literal_global.108
+ ___block_literal_global.31
+ ___block_literal_global.43
+ ___block_literal_global.50
+ _initSFUILinkMetadataSerializationForLocalUseOnly
+ _objc_msgSend$_legacyIconSizeForContentSizeCategory:
+ _objc_msgSend$_resolvedDirectionalLayoutMargins:trailingMargin:
+ _objc_msgSend$addCommitHandler:forPhase:
+ _objc_msgSend$boundingRectWithSize:options:attributes:context:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:multiplier:constant:
+ _objc_msgSend$containerView
+ _objc_msgSend$defaultFontDescriptorWithTextStyle:
+ _objc_msgSend$descriptionLabel
+ _objc_msgSend$fenceCompletionHandler
+ _objc_msgSend$hasAppliedConstraints
+ _objc_msgSend$imageForApplicationIconFormat:activityCategory:contentSizeCategory:
+ _objc_msgSend$initWithSerializedMetadata:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$loadedSerializedMetadatas
+ _objc_msgSend$scene:didReceiveMetadataUpdateAction:
+ _objc_msgSend$serializedMetadata
+ _objc_msgSend$setFenceCompletionHandler:
+ _objc_msgSend$setHasAppliedConstraints:
+ _objc_msgSend$setPointSize:
+ _objc_msgSend$setView:
+ _objc_msgSend$sh_hostUserInterfaceIdiom
+ _softLinkSFUILinkMetadataSerializationForLocalUseOnly
- -[SHSheetAction actionType]
- -[SHSheetAction initWithActionType:]
- -[SHSheetContentUpdateNotification didUpdateDataSource]
- -[SHSheetContentUpdateNotification headerMetadata]
- -[SHSheetContentUpdateNotification initWithHeaderMetadata:didUpdateDataSource:]
- -[SHSheetMetadataChangedAction initWithMetadata:]
- -[SHSheetSceneViewController scene:didReceiveContentUpdateNotification:]
- -[UIActivityViewController _endDelayingPresentation].cold.1
- -[_UIActivityBundleHelper imageForApplicationIconFormat:activityCategory:]
- _OBJC_CLASS_$_SHSheetContentUpdateNotification
- _OBJC_METACLASS_$_SHSheetContentUpdateNotification
- __OBJC_$_INSTANCE_METHODS_SHSheetContentUpdateNotification
- __OBJC_$_PROP_LIST_SHSheetContentUpdateNotification
- __OBJC_CLASS_RO_$_SHSheetContentUpdateNotification
- __OBJC_METACLASS_RO_$_SHSheetContentUpdateNotification
- __UIActivityFormattedAppIconImage
- ___block_literal_global.45
- ___block_literal_global.54
- ___block_literal_global.63
- _objc_msgSend$actionType
- _objc_msgSend$dataRepresentationForLocalUseOnly
- _objc_msgSend$didUpdateDataSource
- _objc_msgSend$imageForApplicationIconFormat:activityCategory:
- _objc_msgSend$initWithMetadata:
- _objc_msgSend$latestSerializedMetadatas
- _objc_msgSend$scene:didReceiveContentUpdateNotification:
CStrings:
+ "\x01!1\x11\x12"
+ "!q"
+ "@36@0:8i16q20@28"
+ "Preparing activity %{public}@ (%{public}@) with activity items:%{sensitive}@ of types:%{public}@"
+ "RealityLauncher"
+ "Resolved activity item types:%{private}@ to:%{private}@"
+ "Resolved activity item types:%{public}@ to:%{public}@"
+ "Resolved placeholder activity item types:%{private}@ to:%{private}@"
+ "Resolved placeholder activity item types:%{public}@ to:%{public}@"
+ "SFUILinkMetadataSerializationForLocalUseOnly"
+ "SHARE_SHEET_SHARING_UNAVAILABLE_DESCRIPTION"
+ "SHARE_SHEET_SHARING_UNAVAILABLE_TITLE"
+ "SHSheetMetadataUpdateAction"
+ "SHSheetPresentationBlockingRootView"
+ "SHSheetWindowScene"
+ "T@\"NSData\",R,N"
+ "T@\"NSLayoutConstraint\",&,N,V_titleLabelTopConstraint"
+ "T@\"UILabel\",&,N,V_descriptionLabel"
+ "T@\"UIView\",&,N,V_containerView"
+ "T@?,C,N,V_fenceCompletionHandler"
+ "TB,N,V_hasAppliedConstraints"
+ "_containerView"
+ "_createSystemCloseButton"
+ "_descriptionLabel"
+ "_fenceCompletionHandler"
+ "_handleClose"
+ "_hasAppliedConstraints"
+ "_legacyIconSizeForContentSizeCategory:"
+ "_resolvedDirectionalLayoutMargins:trailingMargin:"
+ "_titleLabelTopConstraint"
+ "_usesMinimumSafeAreaInsets"
+ "addCommitHandler:forPhase:"
+ "boundingRectWithSize:options:attributes:context:"
+ "constraintLessThanOrEqualToAnchor:multiplier:constant:"
+ "containerView"
+ "defaultFontDescriptorWithTextStyle:"
+ "descriptionLabel"
+ "did receive action with type:%ld"
+ "didMoveToSuperview"
+ "fenceCompletionHandler"
+ "hasAppliedConstraints"
+ "imageForApplicationIconFormat:activityCategory:contentSizeCategory:"
+ "initWithSerializedMetadata:"
+ "initWithSize:scale:"
+ "initWithType:"
+ "leftAlignHeaderText"
+ "loadView"
+ "loadedSerializedMetadatas"
+ "scene:didReceiveMetadataUpdateAction:"
+ "serializedMetadata"
+ "setContainerView:"
+ "setDescriptionLabel:"
+ "setFenceCompletionHandler:"
+ "setHasAppliedConstraints:"
+ "setPointSize:"
+ "setSh_hostUserInterfaceIdiom:"
+ "setTitleLabelTopConstraint:"
+ "setView:"
+ "sh_hostUserInterfaceIdiom"
+ "titleLabelTopConstraint"
+ "uiSceneMinimumClass"
+ "v32@0:8@\"SHSheetScene\"16@\"SHSheetMetadataUpdateAction\"24"
+ "{NSDirectionalEdgeInsets=dddd}32@0:8d16d24"
- "\x01!1\""
- "!a"
- "@28@0:8i16q20"
- "CopyLinkActivityEdit"
- "Preparing activity %{public}@ (%{public}@) with activity items:%{private}@"
- "Resolved activity items:%{private}@ to:%{private}@"
- "Resolved placeholder activity items:%{private}@ to:%{private}@"
- "SHSheetContentUpdateNotification"
- "Sharing is unavailable in Guest Mode"
- "_endDelayingPresentation has already been called."
- "actionType"
- "dataRepresentationForLocalUseOnly"
- "didUpdateDataSource"
- "imageForApplicationIconFormat:activityCategory:"
- "initWithActionType:"
- "initWithHeaderMetadata:didUpdateDataSource:"
- "initWithMetadata:"
- "latestSerializedMetadatas"
- "scene:didReceiveContentUpdateNotification:"
- "v32@0:8@\"SHSheetScene\"16@\"SHSheetContentUpdateNotification\"24"

```
