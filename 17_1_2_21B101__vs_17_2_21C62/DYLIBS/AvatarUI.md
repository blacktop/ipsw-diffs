## AvatarUI

> `/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI`

```diff

-337.0.0.0.0
-  __TEXT.__text: 0xbc090
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x102e0
-  __TEXT.__const: 0x3d8
-  __TEXT.__cstring: 0x40eb
-  __TEXT.__gcc_except_tab: 0x12d4
+340.0.0.0.0
+  __TEXT.__text: 0xbf2f4
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x106e0
+  __TEXT.__const: 0x3e8
+  __TEXT.__cstring: 0x410e
+  __TEXT.__gcc_except_tab: 0x1350
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x3878
-  __TEXT.__objc_classname: 0x2bd3
-  __TEXT.__objc_methname: 0x2a9e6
-  __TEXT.__objc_methtype: 0x81e5
-  __TEXT.__objc_stubs: 0x1b600
+  __TEXT.__unwind_info: 0x393c
+  __TEXT.__objc_classname: 0x2c1c
+  __TEXT.__objc_methname: 0x2b1ae
+  __TEXT.__objc_methtype: 0x8301
+  __TEXT.__objc_stubs: 0x1bba0
   __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x3078
-  __DATA_CONST.__objc_classlist: 0x888
+  __DATA_CONST.__const: 0x30d0
+  __DATA_CONST.__objc_classlist: 0x890
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x3d0
+  __DATA_CONST.__objc_protolist: 0x3d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3bda0
-  __DATA_CONST.__objc_selrefs: 0x7de8
+  __DATA_CONST.__objc_const: 0x3c790
+  __DATA_CONST.__objc_selrefs: 0x7f78
   __DATA_CONST.__objc_arraydata: 0x288
-  __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0x6e78
-  __AUTH_CONST.__const: 0x6a0
+  __AUTH_CONST.__cfstring: 0x3fe0
+  __AUTH_CONST.__objc_const: 0x6ec0
+  __AUTH_CONST.__const: 0x6c0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH.__objc_data: 0x4ba0
+  __AUTH_CONST.__auth_got: 0x718
+  __AUTH.__objc_data: 0x4bf0
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xb68
-  __DATA.__objc_superrefs: 0x708
-  __DATA.__objc_ivar: 0x15bc
-  __DATA.__data: 0x3068
-  __DATA.__bss: 0x88
+  __DATA.__objc_classrefs: 0xb78
+  __DATA.__objc_superrefs: 0x710
+  __DATA.__objc_ivar: 0x1600
+  __DATA.__data: 0x30c8
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5896
-  Symbols:   21501
-  CStrings:  8054
+  Functions: 5994
+  Symbols:   21801
+  CStrings:  8134
 
Symbols:
+ -[AVTAnimojiPoseSelectionHeaderViewController avtCaptureBackgroundColor]
+ -[AVTAnimojiPoseSelectionHeaderViewController setAvtCaptureBackgroundColor:]
+ -[AVTAnimojiPoseSelectionHeaderViewController setCaptureBackgroundColor:]
+ -[AVTAnimojiPoseSelectionHeaderViewController updateForAvatarRecord:discardPose:]
+ -[AVTCombinedPickerViewController .cxx_destruct]
+ -[AVTCombinedPickerViewController actionsController:didAddRecord:]
+ -[AVTCombinedPickerViewController actionsController:didCancelEditingRecord:]
+ -[AVTCombinedPickerViewController actionsController:didDeleteRecord:withRecordUpdate:completionBlock:]
+ -[AVTCombinedPickerViewController actionsController:didDuplicateToRecord:completionBlock:]
+ -[AVTCombinedPickerViewController actionsController:didEditRecord:]
+ -[AVTCombinedPickerViewController actionsController:presentAlertController:]
+ -[AVTCombinedPickerViewController actionsControllerDidFinish:]
+ -[AVTCombinedPickerViewController actionsModel]
+ -[AVTCombinedPickerViewController actionsViewHandler]
+ -[AVTCombinedPickerViewController avatarPicker:didSelectAvatarRecord:]
+ -[AVTCombinedPickerViewController avatarPicker:shouldPresentMemojiEditorForAvatarRecord:]
+ -[AVTCombinedPickerViewController avatarPickerDidEndCameraSession:]
+ -[AVTCombinedPickerViewController avatarPickerWillStartCameraSession:]
+ -[AVTCombinedPickerViewController avatarPicker]
+ -[AVTCombinedPickerViewController avatarRecord]
+ -[AVTCombinedPickerViewController avatarStoreChangeObserver]
+ -[AVTCombinedPickerViewController avatarStore]
+ -[AVTCombinedPickerViewController beginObservingAvatarStoreChanges]
+ -[AVTCombinedPickerViewController canBecomeFirstResponder]
+ -[AVTCombinedPickerViewController dealloc]
+ -[AVTCombinedPickerViewController delegate]
+ -[AVTCombinedPickerViewController didSelectAvatarRecord:]
+ -[AVTCombinedPickerViewController didTapCancel:]
+ -[AVTCombinedPickerViewController didTapDone:]
+ -[AVTCombinedPickerViewController dismissAvatarUIControllerAnimated:]
+ -[AVTCombinedPickerViewController dismissEditorViewController:forActionsController:wasCreate:didEdit:animated:completion:]
+ -[AVTCombinedPickerViewController doneButton]
+ -[AVTCombinedPickerViewController endObservingAvatarStoreChanges]
+ -[AVTCombinedPickerViewController environment]
+ -[AVTCombinedPickerViewController initWithSelectedRecord:]
+ -[AVTCombinedPickerViewController keyCommands]
+ -[AVTCombinedPickerViewController poseController]
+ -[AVTCombinedPickerViewController poseSelectionController:didSelectPoseWithConfiguration:]
+ -[AVTCombinedPickerViewController poseSelectionController:didSetMode:withConfiguration:]
+ -[AVTCombinedPickerViewController poseSelectionControllerDidCancel:]
+ -[AVTCombinedPickerViewController presentAvatarUIController:animated:]
+ -[AVTCombinedPickerViewController presentEditorViewController:forActionsController:isCreate:]
+ -[AVTCombinedPickerViewController presentUpdatedAvatarRecord:animated:]
+ -[AVTCombinedPickerViewController presentUpdatedAvatarRecord:animated:completion:]
+ -[AVTCombinedPickerViewController presentedAvatarRecord:]
+ -[AVTCombinedPickerViewController recordDataSource]
+ -[AVTCombinedPickerViewController refreshPickerForStoreUpdate]
+ -[AVTCombinedPickerViewController returnPressed:]
+ -[AVTCombinedPickerViewController setActionsModel:]
+ -[AVTCombinedPickerViewController setActionsViewHandler:]
+ -[AVTCombinedPickerViewController setAvatarPicker:]
+ -[AVTCombinedPickerViewController setAvatarRecord:]
+ -[AVTCombinedPickerViewController setAvatarStoreChangeObserver:]
+ -[AVTCombinedPickerViewController setDelegate:]
+ -[AVTCombinedPickerViewController setDoneButton:]
+ -[AVTCombinedPickerViewController setPoseController:]
+ -[AVTCombinedPickerViewController setRecordDataSource:]
+ -[AVTCombinedPickerViewController setStickerConfiguration:]
+ -[AVTCombinedPickerViewController stickerConfiguration]
+ -[AVTCombinedPickerViewController updateActionModel]
+ -[AVTCombinedPickerViewController viewDidLoad]
+ -[AVTCombinedPickerViewController wrapAndPresentViewController:animated:]
+ -[AVTPoseSelectionViewController animateButtonConfiguration:]
+ -[AVTPoseSelectionViewController buttonEdgeLength]
+ -[AVTPoseSelectionViewController buttonSymbolWeight]
+ -[AVTPoseSelectionViewController captureButtonEdgeLength]
+ -[AVTPoseSelectionViewController clearHeaderMenu]
+ -[AVTPoseSelectionViewController configureButtonsForCapture]
+ -[AVTPoseSelectionViewController configureButtonsForReview]
+ -[AVTPoseSelectionViewController createMenuButtonIfNeeded]
+ -[AVTPoseSelectionViewController didFinishMenuPresentationWithCompletion:]
+ -[AVTPoseSelectionViewController discardButtonEdgeLength]
+ -[AVTPoseSelectionViewController discardButtonSymbolWeight]
+ -[AVTPoseSelectionViewController headerMenu]
+ -[AVTPoseSelectionViewController menuButton]
+ -[AVTPoseSelectionViewController notifyDelegateOfModeChange:]
+ -[AVTPoseSelectionViewController prepareForMenuPresentation]
+ -[AVTPoseSelectionViewController selectedPoseConfiguration]
+ -[AVTPoseSelectionViewController setHeaderMenu:]
+ -[AVTPoseSelectionViewController setMenuButton:]
+ -[AVTPoseSelectionViewController setNewAvatarRecord:]
+ -[AVTPoseSelectionViewController setUsesSingleButtonCaptureReview:]
+ -[AVTPoseSelectionViewController usesSingleButtonCaptureReview]
+ -[AVTSimpleAvatarPicker doesDisplayEditIconWhenAvailable]
+ -[AVTSimpleAvatarPicker setDoesDisplayEditIconWhenAvailable:]
+ _AVTDeviceIsMacOrIPad
+ _AVTDeviceIsMacOrIPad.deviceIsMacOrIPad
+ _AVTDeviceIsMacOrIPad.onceToken
+ _OBJC_CLASS_$_AVTCombinedPickerViewController
+ _OBJC_CLASS_$_UISpringTimingParameters
+ _OBJC_IVAR_$_AVTAnimojiPoseSelectionHeaderViewController._avtCaptureBackgroundColor
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._actionsModel
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._actionsViewHandler
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._avatarPicker
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._avatarRecord
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._avatarStore
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._avatarStoreChangeObserver
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._delegate
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._doneButton
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._environment
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._poseController
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._recordDataSource
+ _OBJC_IVAR_$_AVTCombinedPickerViewController._stickerConfiguration
+ _OBJC_IVAR_$_AVTPoseSelectionViewController._headerMenu
+ _OBJC_IVAR_$_AVTPoseSelectionViewController._menuButton
+ _OBJC_IVAR_$_AVTPoseSelectionViewController._usesSingleButtonCaptureReview
+ _OBJC_IVAR_$_AVTSimpleAvatarPicker._doesDisplayEditIconWhenAvailable
+ _OBJC_METACLASS_$_AVTCombinedPickerViewController
+ __OBJC_$_INSTANCE_METHODS_AVTCombinedPickerViewController
+ __OBJC_$_INSTANCE_VARIABLES_AVTCombinedPickerViewController
+ __OBJC_$_PROP_LIST_AVTCombinedPickerViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVTPoseSelectionViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVTPoseSelectionViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVTPoseSelectionViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_AVTPoseSelectionViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AVTCombinedPickerViewController
+ __OBJC_CLASS_RO_$_AVTCombinedPickerViewController
+ __OBJC_LABEL_PROTOCOL_$_AVTPoseSelectionViewControllerDelegate
+ __OBJC_METACLASS_RO_$_AVTCombinedPickerViewController
+ __OBJC_PROTOCOL_$_AVTPoseSelectionViewControllerDelegate
+ ___53-[AVTPoseSelectionViewController setNewAvatarRecord:]_block_invoke
+ ___59-[AVTPoseSelectionViewController configureButtonsForReview]_block_invoke
+ ___60-[AVTPoseSelectionViewController configureButtonsForCapture]_block_invoke
+ ___62-[AVTCombinedPickerViewController refreshPickerForStoreUpdate]_block_invoke
+ ___67-[AVTCombinedPickerViewController beginObservingAvatarStoreChanges]_block_invoke
+ ___70-[AVTPoseSelectionViewController updateForPoseConfiguration:animated:]_block_invoke
+ ___74-[AVTPoseSelectionViewController didFinishMenuPresentationWithCompletion:]_block_invoke
+ ___74-[AVTPoseSelectionViewController didFinishMenuPresentationWithCompletion:]_block_invoke_2
+ ___81-[AVTAnimojiPoseSelectionHeaderViewController updateForAvatarRecord:discardPose:]_block_invoke
+ ___82-[AVTCombinedPickerViewController presentUpdatedAvatarRecord:animated:completion:]_block_invoke
+ ___90-[AVTCombinedPickerViewController actionsController:didDuplicateToRecord:completionBlock:]_block_invoke
+ ___AVTDeviceIsMacOrIPad_block_invoke
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _kAVTCircularButtonUndoImageName
+ _objc_msgSend$addAnimations:
+ _objc_msgSend$animateButtonConfiguration:
+ _objc_msgSend$avtCaptureBackgroundColor
+ _objc_msgSend$buttonEdgeLength
+ _objc_msgSend$buttonSymbolWeight
+ _objc_msgSend$captureButtonEdgeLength
+ _objc_msgSend$clearHeaderMenu
+ _objc_msgSend$combinedPickerViewController:didSelectRecord:withStickerConfiguration:
+ _objc_msgSend$combinedPickerViewControllerDidCancel:
+ _objc_msgSend$configureButtonsForCapture
+ _objc_msgSend$configureButtonsForReview
+ _objc_msgSend$controller
+ _objc_msgSend$createMenuButtonIfNeeded
+ _objc_msgSend$didFinishMenuPresentationWithCompletion:
+ _objc_msgSend$didSelectAvatarRecord:
+ _objc_msgSend$discardButtonEdgeLength
+ _objc_msgSend$discardButtonSymbolWeight
+ _objc_msgSend$doesDisplayEditIconWhenAvailable
+ _objc_msgSend$doneButton
+ _objc_msgSend$initWithDuration:timingParameters:
+ _objc_msgSend$initWithMass:stiffness:damping:initialVelocity:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$initWithSelectedRecord:
+ _objc_msgSend$menuButton
+ _objc_msgSend$menuWithChildren:
+ _objc_msgSend$notifyDelegateOfModeChange:
+ _objc_msgSend$poseSelectionController:didSetMode:withConfiguration:
+ _objc_msgSend$presentUpdatedAvatarRecord:animated:
+ _objc_msgSend$presentUpdatedAvatarRecord:animated:completion:
+ _objc_msgSend$refreshPickerForStoreUpdate
+ _objc_msgSend$secondarySystemFillColor
+ _objc_msgSend$selectedPoseConfiguration
+ _objc_msgSend$setCaptureBackgroundColor:
+ _objc_msgSend$setDoesDisplayEditIconWhenAvailable:
+ _objc_msgSend$setHeaderMenu:
+ _objc_msgSend$setModalInPresentation:
+ _objc_msgSend$setNewAvatarRecord:
+ _objc_msgSend$setPreferredContentSize:
+ _objc_msgSend$setPreventsDisplaySleepDuringVideoPlayback:
+ _objc_msgSend$setShouldNotifyDelegateOnSelection:
+ _objc_msgSend$setSymbolTintColor:
+ _objc_msgSend$setUsesSingleButtonCaptureReview:
+ _objc_msgSend$updateActionModel
+ _objc_msgSend$updateForAvatarRecord:discardPose:
+ _objc_msgSend$updateWithAvatarRecord:stickerConfigurations:
+ _objc_release_x2
CStrings:
+ "\x1b"
+ "@\"<AVTCombinedPickerViewControllerDelegate>\""
+ "@\"AVTPoseSelectionViewController\""
+ "AVTCombinedPickerViewController"
+ "AVTPoseSelectionViewControllerDelegate"
+ "L"
+ "T@\"<AVTCombinedPickerViewControllerDelegate>\",W,N,V_delegate"
+ "T@\"AVTAvatarInlineActionsController\",&,N,V_actionsViewHandler"
+ "T@\"AVTAvatarRecordDataSource\",&,N,V_recordDataSource"
+ "T@\"AVTCircularButton\",&,N,V_menuButton"
+ "T@\"AVTPoseSelectionViewController\",&,N,V_poseController"
+ "T@\"AVTStickerConfiguration\",&,N,V_stickerConfiguration"
+ "T@\"UIColor\",&,N,V_avtCaptureBackgroundColor"
+ "T@\"UIMenu\",&,N,V_headerMenu"
+ "TB,N,V_doesDisplayEditIconWhenAvailable"
+ "TB,N,V_usesSingleButtonCaptureReview"
+ "_actionsViewHandler"
+ "_avtCaptureBackgroundColor"
+ "_doesDisplayEditIconWhenAvailable"
+ "_headerMenu"
+ "_menuButton"
+ "_poseController"
+ "_usesSingleButtonCaptureReview"
+ "actionsViewHandler"
+ "addAnimations:"
+ "animateButtonConfiguration:"
+ "avtCaptureBackgroundColor"
+ "buttonEdgeLength"
+ "buttonSymbolWeight"
+ "captureButtonEdgeLength"
+ "clearHeaderMenu"
+ "combinedPickerViewController:didSelectRecord:withStickerConfiguration:"
+ "combinedPickerViewControllerDidCancel:"
+ "configureButtonsForCapture"
+ "configureButtonsForReview"
+ "createMenuButtonIfNeeded"
+ "didFinishMenuPresentationWithCompletion:"
+ "didSelectAvatarRecord:"
+ "discardButtonEdgeLength"
+ "discardButtonSymbolWeight"
+ "doc.on.doc"
+ "doesDisplayEditIconWhenAvailable"
+ "gobackward"
+ "headerMenu"
+ "initWithDuration:timingParameters:"
+ "initWithMass:stiffness:damping:initialVelocity:"
+ "initWithObjects:"
+ "menuButton"
+ "menuWithChildren:"
+ "notifyDelegateOfModeChange:"
+ "pencil"
+ "poseController"
+ "poseSelectionController:didSetMode:withConfiguration:"
+ "prepareForMenuPresentation"
+ "presentUpdatedAvatarRecord:animated:"
+ "presentUpdatedAvatarRecord:animated:completion:"
+ "refreshPickerForStoreUpdate"
+ "secondarySystemFillColor"
+ "selectedPoseConfiguration"
+ "setActionsViewHandler:"
+ "setAvtCaptureBackgroundColor:"
+ "setCaptureBackgroundColor:"
+ "setDoesDisplayEditIconWhenAvailable:"
+ "setHeaderMenu:"
+ "setMenuButton:"
+ "setModalInPresentation:"
+ "setNewAvatarRecord:"
+ "setPoseController:"
+ "setPreferredContentSize:"
+ "setPreventsDisplaySleepDuringVideoPlayback:"
+ "setRecordDataSource:"
+ "setStickerConfiguration:"
+ "setUsesSingleButtonCaptureReview:"
+ "trash"
+ "updateActionModel"
+ "updateForAvatarRecord:discardPose:"
+ "usesSingleButtonCaptureReview"
+ "v24@0:8@\"AVTPoseSelectionViewController\"16"
+ "v32@0:8@\"AVTPoseSelectionViewController\"16@\"AVTStickerConfiguration\"24"
+ "v40@0:8@\"AVTPoseSelectionViewController\"16Q24@\"AVTStickerConfiguration\"32"
+ "v40@0:8@16Q24@32"
- "J"

```
