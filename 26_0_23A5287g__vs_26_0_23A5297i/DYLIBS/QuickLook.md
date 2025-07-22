## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1012.2.0.0.0
-  __TEXT.__text: 0xd4004
-  __TEXT.__auth_stubs: 0x2560
-  __TEXT.__delay_stubs: 0x2c
-  __TEXT.__delay_helper: 0x814
-  __TEXT.__objc_methlist: 0xb3cc
+1013.1.0.0.0
+  __TEXT.__text: 0xd5228
+  __TEXT.__auth_stubs: 0x2580
+  __TEXT.__delay_helper: 0x7cc
+  __TEXT.__objc_methlist: 0xb52c
   __TEXT.__const: 0x2d94
-  __TEXT.__gcc_except_tab: 0x1a1c
-  __TEXT.__oslogstring: 0x54c7
-  __TEXT.__cstring: 0x6210
+  __TEXT.__gcc_except_tab: 0x19e8
+  __TEXT.__oslogstring: 0x5507
+  __TEXT.__cstring: 0x6280
   __TEXT.__ustring: 0x1c
   __TEXT.__swift5_typeref: 0x1a86
   __TEXT.__swift5_reflstr: 0x7e7

   __TEXT.__swift_as_ret: 0x1c0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4878
+  __TEXT.__unwind_info: 0x48c0
   __TEXT.__eh_frame: 0x4734
-  __TEXT.__objc_classname: 0x1725
-  __TEXT.__objc_methname: 0x202dd
-  __TEXT.__objc_methtype: 0x6ec0
-  __TEXT.__objc_stubs: 0x156c0
-  __DATA_CONST.__got: 0xf18
+  __TEXT.__objc_classname: 0x1731
+  __TEXT.__objc_methname: 0x2057e
+  __TEXT.__objc_methtype: 0x6ed1
+  __TEXT.__objc_stubs: 0x159a0
+  __DATA_CONST.__got: 0xf20
   __DATA_CONST.__const: 0x25e8
-  __DATA_CONST.__objc_classlist: 0x468
+  __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7198
+  __DATA_CONST.__objc_selrefs: 0x7268
   __DATA_CONST.__objc_protorefs: 0x120
-  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x12c8
+  __AUTH_CONST.__auth_got: 0x12d0
   __AUTH_CONST.__const: 0x3620
-  __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0x114e8
+  __AUTH_CONST.__cfstring: 0x3100
+  __AUTH_CONST.__objc_const: 0x116b8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x2b28
+  __AUTH.__objc_data: 0x2b78
   __AUTH.__data: 0x15a8
-  __DATA.__objc_ivar: 0xbc8
+  __DATA.__objc_ivar: 0xbdc
   __DATA.__data: 0x3250
-  __DATA.__bss: 0x2338
+  __DATA.__bss: 0x2328
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x460
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB62A9C6-A001-3735-A07B-AE3B9243E69F
-  Functions: 5489
-  Symbols:   13926
-  CStrings:  7186
+  UUID: 6CBA7ACB-D504-320F-BBFF-1925ABABB788
+  Functions: 5514
+  Symbols:   14007
+  CStrings:  7231
 
Symbols:
+ +[QLUtilitiesInternal performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:isContentManaged:completion:]
+ -[QLBadgeView .cxx_destruct]
+ -[QLBadgeView imageView]
+ -[QLBadgeView image]
+ -[QLBadgeView initWithCoder:]
+ -[QLBadgeView initWithFrame:]
+ -[QLBadgeView label]
+ -[QLBadgeView layoutSubviews]
+ -[QLBadgeView setImage:]
+ -[QLBadgeView setImageView:]
+ -[QLBadgeView setLabel:]
+ -[QLBadgeView setStackView:]
+ -[QLBadgeView setStackViewLeadingConstraint:]
+ -[QLBadgeView setText:]
+ -[QLBadgeView setupAppearance]
+ -[QLBadgeView setupLayout]
+ -[QLBadgeView setupSubviews]
+ -[QLBadgeView setupView]
+ -[QLBadgeView stackViewLeadingConstraint]
+ -[QLBadgeView stackView]
+ -[QLBadgeView text]
+ -[QLBadgeView updateStackViewConstraints]
+ -[QLItem(UI) isBookmarkable]
+ -[QLItemPresenterViewController setIsContentManaged:]
+ -[QLPreviewCollection isContentManaged]
+ -[QLPreviewController reloadDataWithIndex:]
+ GCC_except_table110
+ GCC_except_table68
+ GCC_except_table92
+ GCC_except_table96
+ _FPCreateBookmarkableStringFromDocumentURL
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_QLBadgeView
+ _OBJC_CLASS_$_UIContentUnavailableView
+ _OBJC_CLASS_$_UIStackView
+ _OBJC_IVAR_$_QLBadgeView._imageView
+ _OBJC_IVAR_$_QLBadgeView._label
+ _OBJC_IVAR_$_QLBadgeView._stackView
+ _OBJC_IVAR_$_QLBadgeView._stackViewLeadingConstraint
+ _OBJC_IVAR_$_QLPreviewCollection._isContentManaged
+ _OBJC_METACLASS_$_QLBadgeView
+ _OBJC_METACLASS_$_UIContentUnavailableView
+ __OBJC_$_INSTANCE_METHODS_QLBadgeView
+ __OBJC_$_INSTANCE_VARIABLES_QLBadgeView
+ __OBJC_$_PROP_LIST_QLBadgeView
+ __OBJC_CLASS_RO_$_QLBadgeView
+ __OBJC_METACLASS_RO_$_QLBadgeView
+ ___121+[QLUtilitiesInternal performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:isContentManaged:completion:]_block_invoke
+ ___136-[QLPreviewCollection startTransitionWithSourceViewProvider:transitionController:presenting:useInteractiveTransition:completionHandler:]_block_invoke.214
+ ___46-[QLMovieItemViewController loadAssetMetadata]_block_invoke.201
+ ___64-[QLPreviewCollection pageViewController:viewControllerAtIndex:]_block_invoke.239
+ ___89-[QLErrorItemViewController loadPreviewControllerWithContents:context:completionHandler:]_block_invoke
+ ___89-[QLErrorItemViewController loadPreviewControllerWithContents:context:completionHandler:]_block_invoke_2
+ ____QLGetOpenInAppClaimBindingForItem_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e18_v16?0"UIAction"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e15_v16?0"NSURL"8ls32l8s40l8s48l8w56l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e36_v24?0^{__CFString=}8^{__CFError=}16ls32l8s40l8s48l8s56l8w64l8
+ ___block_literal_global.186
+ ___block_literal_global.73
+ _kISImageDescriptorHomeScreen
+ _objc_msgSend$availableClaimBindingsForMode:error:
+ _objc_msgSend$borderedButtonConfiguration
+ _objc_msgSend$buttonProperties
+ _objc_msgSend$configurationWithFont:
+ _objc_msgSend$documentProxyForURL:isContentManaged:sourceAuditToken:
+ _objc_msgSend$emptyConfiguration
+ _objc_msgSend$fontWithSize:
+ _objc_msgSend$imageDescriptorNamed:
+ _objc_msgSend$imageForDescriptor:
+ _objc_msgSend$imageView
+ _objc_msgSend$imageWithConfiguration:
+ _objc_msgSend$isBookmarkable
+ _objc_msgSend$label
+ _objc_msgSend$performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:isContentManaged:completion:
+ _objc_msgSend$quaternaryLabelColor
+ _objc_msgSend$setAlignment:
+ _objc_msgSend$setAxis:
+ _objc_msgSend$setButton:
+ _objc_msgSend$setImageView:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setSpacing:
+ _objc_msgSend$setStackView:
+ _objc_msgSend$setStackViewLeadingConstraint:
+ _objc_msgSend$setupAppearance
+ _objc_msgSend$setupLayout
+ _objc_msgSend$setupSubviews
+ _objc_msgSend$setupView
+ _objc_msgSend$stackView
+ _objc_msgSend$stackViewLeadingConstraint
+ _objc_msgSend$text
+ _objc_msgSend$updateStackViewConstraints
+ _pow
- -[QLPreviewController(Overlay) _performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:completion:]
- GCC_except_table104
- GCC_except_table107
- GCC_except_table108
- GCC_except_table111
- GCC_except_table16
- GCC_except_table66
- GCC_except_table91
- GCC_except_table94
- GCC_except_table98
- GCC_except_table99
- _OBJC_CLASS_$_PXUIAssetBadgeView
- _OBJC_CLASS_$__UIContentUnavailableView
- _OBJC_METACLASS_$__UIContentUnavailableView
- _PXAssetBadgeInfoCreateWithBadges
- _PXAssetBadgeInfoCreateWithBadges$delayInitStub
- _PXAssetBadgeInfoNull
- __LSHandlerRankOwner
- __QLGetOpenInAppClaimBindingForContentType
- ___114-[QLPreviewController(Overlay) _performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:completion:]_block_invoke
- ___136-[QLPreviewCollection startTransitionWithSourceViewProvider:transitionController:presenting:useInteractiveTransition:completionHandler:]_block_invoke.211
- ___46-[QLMovieItemViewController loadAssetMetadata]_block_invoke.192
- ___57-[QLMovieItemViewController _hideAssetBadgeViewIfVisible]_block_invoke
- ___64-[QLPreviewCollection pageViewController:viewControllerAtIndex:]_block_invoke.236
- ____QLGetOpenInAppClaimBindingForContentType_block_invoke
- ___block_descriptor_48_e8_32s40w_e15_v16?0"NSURL"8lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56w_e36_v24?0^{__CFString=}8^{__CFError=}16ls32l8s40l8s48l8w56l8
- ___block_descriptor_80_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_literal_global.188
- ___block_literal_global.280
- ___block_literal_global.71
- __block_invoke.cachedApps
- _gotLoadHelper_x8$_OBJC_CLASS_$_PXUIAssetBadgeView
- _gotLoadHelper_x8$_PXAssetBadgeInfoNull
- _objc_msgSend$_performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:completion:
- _objc_msgSend$availableClaimBindingsForMode:handlerRank:error:
- _objc_msgSend$badgeInfo
- _objc_msgSend$initWithFrame:title:style:
- _objc_msgSend$performChanges:animated:
- _objc_msgSend$setBadgeInfo:
- _objc_msgSend$setContentWidth:
- _objc_msgSend$setMessage:
CStrings:
+ "@\"QLBadgeView\""
+ "Copy to %@"
+ "Couldn't get bookmark for item (might be expected): %@ #PreviewItem"
+ "First claiming app: %@ for document proxy: %@ of type: %@ supports Open In but is the current app, returning nil. #Generic"
+ "First claiming app: %@ for document proxy: %@ of type: %@ supports Open In, returning it. #Generic"
+ "HDR"
+ "No Open In app for item: %@ #Generic"
+ "ProRes"
+ "QLBadgeView"
+ "T@\"NSLayoutConstraint\",&,N,V_stackViewLeadingConstraint"
+ "T@\"NSString\",&,N"
+ "T@\"QLBadgeView\",&,N,V_assetBadgeView"
+ "T@\"UIImageView\",&,N,V_imageView"
+ "T@\"UILabel\",&,N,V_label"
+ "T@\"UIStackView\",&,N,V_stackView"
+ "Title of Copy to button displayed in Quick Look to let users copy the currently previewed file in the given app."
+ "_stackView"
+ "_stackViewLeadingConstraint"
+ "allowsNumberPadPopover"
+ "availableClaimBindingsForMode:error:"
+ "borderedButtonConfiguration"
+ "buttonProperties"
+ "configurationWithFont:"
+ "documentProxyForURL:isContentManaged:sourceAuditToken:"
+ "emptyConfiguration"
+ "fontWithSize:"
+ "imageDescriptorNamed:"
+ "imageForDescriptor:"
+ "imageView"
+ "imageWithConfiguration:"
+ "isBookmarkable"
+ "performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:isContentManaged:completion:"
+ "quaternaryLabelColor"
+ "reloadDataWithIndex:"
+ "setAlignment:"
+ "setAllowsNumberPadPopover:"
+ "setAxis:"
+ "setButton:"
+ "setImageView:"
+ "setLabel:"
+ "setSpacing:"
+ "setStackView:"
+ "setStackViewLeadingConstraint:"
+ "setupAppearance"
+ "setupLayout"
+ "setupSubviews"
+ "setupView"
+ "stackView"
+ "stackViewLeadingConstraint"
+ "text"
+ "tv"
+ "updateStackViewConstraints"
+ "v52@0:8@16@24@32B40@?44"
- "@\"PXUIAssetBadgeView\""
- "First owner app: %@ for document proxy: %@ of type: %@ supports Open In but is the current app, returning nil. #Generic"
- "First owner app: %@ for document proxy: %@ of type: %@ supports Open In, returning it. #Generic"
- "ModernPlayerControl"
- "No Open In app for content type: %@ #Generic"
- "T@\"PXUIAssetBadgeView\",&,N,V_assetBadgeView"
- "_performOpenInWithFileURL:claimBinding:additionalLaunchServicesOptions:completion:"
- "availableClaimBindingsForMode:handlerRank:error:"
- "badgeInfo"
- "initWithFrame:title:style:"
- "performChanges:animated:"
- "setBadgeInfo:"
- "setContentWidth:"
- "setMessage:"

```
