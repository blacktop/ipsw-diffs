## IntentsUI

> `/System/Library/Frameworks/IntentsUI.framework/IntentsUI`

```diff

-4015.3.3.0.0
-  __TEXT.__text: 0xf870
-  __TEXT.__auth_stubs: 0x670
+4015.4.42.0.0
+  __TEXT.__text: 0x10430
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x16a4
   __TEXT.__const: 0x120
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__gcc_except_tab: 0x204
+  __TEXT.__gcc_except_tab: 0x1e8
   __TEXT.__cstring: 0x1664
   __TEXT.__oslogstring: 0xa33
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__unwind_info: 0x530
   __TEXT.__objc_classname: 0x537
   __TEXT.__objc_methname: 0x4480
   __TEXT.__objc_methtype: 0xf98

   __DATA_CONST.__objc_selrefs: 0x1248
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0xb60
   __AUTH_CONST.__objc_const: 0x26d0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 806886AD-47E0-3333-8791-EF6480E1E505
+  UUID: ABA85F71-A1A3-3FC7-AE40-129184875F0E
   Functions: 405
-  Symbols:   1980
+  Symbols:   1977
   CStrings:  1156
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
Functions:
~ -[INUIAddVoiceShortcutViewController setCurrentChildViewController:] : 20 -> 80
~ -[INUIAddVoiceShortcutViewController _setRemoteHostViewController:] : 20 -> 80
~ -[INUIAddVoiceShortcutViewController set_shortcut:] : 20 -> 80
~ -[INUIAddVoiceShortcutViewController _containedRemoteViewController] : 16 -> 64
~ -[INUIAddVoiceShortcutViewController remoteViewControllerDidCancel] : 80 -> 84
~ -[INUIAddVoiceShortcutViewController remoteViewControllerDidCreateVoiceShortcut:error:] : 168 -> 172
~ -[INUIAddVoiceShortcutViewController setChildViewController:] : 324 -> 352
~ -[INUIAddVoiceShortcutViewController initWithShortcut:] : 408 -> 424
~ ___55-[INUIAddVoiceShortcutViewController initWithShortcut:]_block_invoke : 464 -> 468
~ ___55-[INUIAddVoiceShortcutViewController initWithShortcut:]_block_invoke.6 : 128 -> 136
~ -[INUIVoiceShortcutHostViewController remoteViewControllerDidCancel] : 84 -> 88
~ -[INUIVoiceShortcutHostViewController remoteViewControllerDidDeleteVoiceShortcutWithIdentifier:] : 116 -> 120
~ -[INUIVoiceShortcutHostViewController viewServiceDidTerminateWithError:] : 276 -> 272
~ -[INUIVoiceShortcutHostViewController setServiceContext:] : 128 -> 136
~ +[INUIVoiceShortcutHostViewController getViewControllerCompletion:] : 672 -> 704
~ ___67+[INUIVoiceShortcutHostViewController getViewControllerCompletion:]_block_invoke : 660 -> 664
~ +[INUIVoiceShortcutHostViewController getViewControllerForEditingVoiceShortcut:completion:] : 188 -> 180
~ ___91+[INUIVoiceShortcutHostViewController getViewControllerForEditingVoiceShortcut:completion:]_block_invoke : 160 -> 172
~ +[INUIVoiceShortcutHostViewController getViewControllerForAddingShortcut:completion:] : 772 -> 748
~ ___85+[INUIVoiceShortcutHostViewController getViewControllerForAddingShortcut:completion:]_block_invoke : 300 -> 296
~ ___85+[INUIVoiceShortcutHostViewController getViewControllerForAddingShortcut:completion:]_block_invoke.4 : 292 -> 280
~ ___85+[INUIVoiceShortcutHostViewController getViewControllerForAddingShortcut:completion:]_block_invoke.6 : 232 -> 236
~ +[INUIVoiceShortcutHostViewController _voiceShortcutUIExtension] : 84 -> 100
~ -[INUIAppIntentForwardingActionExecutor setApplication:] : 12 -> 64
~ -[INUIAppIntentForwardingActionExecutor intentDeliverer:deliverIntent:withBlock:] : 200 -> 208
~ -[INUIAppIntentForwardingActionExecutor executeAction:completionHandler:] : 1232 -> 1288
~ ___73-[INUIAppIntentForwardingActionExecutor executeAction:completionHandler:]_block_invoke_2 : 104 -> 108
~ ___73-[INUIAppIntentForwardingActionExecutor executeAction:completionHandler:]_block_invoke_3 : 196 -> 204
~ -[INUIAppIntentForwardingActionExecutor initWithApplication:] : 116 -> 108
~ -[_INUIExtensionContextState encodeWithCoder:] : 128 -> 136
~ -[_INUIExtensionContextState initWithCoder:] : 468 -> 492
~ -[_INUIExtensionContextState copyWithZone:] : 4 -> 40
~ -[_INUIExtensionContextState isEqual:] : 188 -> 176
~ +[INUIVoiceShortcutXPCInterface remoteViewControllerServingInterface] : 352 -> 372
~ +[INUIVoiceShortcutXPCInterface remoteViewControllerHostingInterface] : 348 -> 368
~ -[INUIImageServiceConnection loadUIImageForINImage:traitCollection:reply:] : 204 -> 200
~ ___74-[INUIImageServiceConnection loadUIImageForINImage:traitCollection:reply:]_block_invoke : 156 -> 164
~ +[INUIImageServiceConnection sharedConnection] : 84 -> 100
~ +[_INUIXPCInterfaceUtilities extensionContextVendingInterface] : 352 -> 368
~ -[_INUIExtensionHostContext willBeginEditing] : 80 -> 84
~ -[_INUIExtensionHostContext requestHandlingOfIntent:] : 100 -> 104
~ -[_INUIExtensionHostContext _errorHandlingExtensionContextProxy] : 84 -> 92
~ ___41-[_INUIExtensionContext viewWasCancelled]_block_invoke : 68 -> 72
~ ___66-[_INUIExtensionContext queryRepresentedPropertiesWithCompletion:]_block_invoke : 84 -> 88
~ ___46-[_INUIExtensionContext desiresInteractivity:]_block_invoke : 84 -> 88
~ -[_INUIExtensionContext configureForParameters:ofInteraction:interactiveBehavior:context:completion:] : 248 -> 232
~ ___101-[_INUIExtensionContext configureForParameters:ofInteraction:interactiveBehavior:context:completion:]_block_invoke : 92 -> 96
~ -[_INUIExtensionContext _willBeginEditing] : 64 -> 68
~ -[_INUIExtensionContext _requestHandlingOfIntent:] : 116 -> 120
~ -[_INUIExtensionContext interfaceParametersDescription] : 628 -> 660
~ -[_INUIExtensionContext hostedViewMaximumAllowedSize] : 96 -> 100
~ -[_INUIExtensionContext hostedViewMinimumAllowedSize] : 96 -> 100
~ -[_INUIExtensionContext setExtensionContextState:completion:] : 128 -> 120
~ -[_INUIExtensionContext _errorHandlingHostProxy] : 84 -> 92
~ -[_INUIExtensionContext initWithInputItems:listenerEndpoint:contextUUID:] : 128 -> 132
~ +[INUIImageSizeProvider downscaledPNGImageForImage:size:error:] : 2484 -> 2596
~ +[INUIImageSizeProvider imageSizeForImage:] : 416 -> 440
~ +[UIImage(INUICrossPlatform) _inui_imageWithLightModeImage:darkModeImage:] : 144 -> 148
~ -[INUIPortableImageLoaderHelper setTraitCollection:] : 12 -> 64
~ -[INUIPortableImageLoaderHelper initWithCoder:] : 140 -> 144
~ -[INUIPortableImageLoaderHelper encodeWithCoder:] : 108 -> 112
~ -[INUIPortableImageLoaderHelper loadImageDataFromBundle:withImageName:accessSpecifier:completion:] : 1684 -> 1772
~ -[INUIImageLoader loadDataImageFromImage:usingPortableImageLoader:scaledSize:completion:] : 1464 -> 1504
~ -[INUIImageLoader serviceIdentifier] : 148 -> 176
~ ___36-[INUIImageLoader serviceIdentifier]_block_invoke : 184 -> 200
~ -[INUIImageLoader loadImage:withContext:completionHandler:] : 668 -> 688
~ ___59-[INUIImageLoader loadImage:withContext:completionHandler:]_block_invoke : 160 -> 164
~ ___59-[INUIImageLoader loadImage:withContext:completionHandler:]_block_invoke_2 : 180 -> 188
~ -[INUIImageLoader loadImage:withCompletionHandler:] : 120 -> 116
~ -[INUIImageLoader deregisterWithIntents] : 88 -> 92
~ -[INUIImageLoader registerWithIntents] : 88 -> 92
~ +[INUIImageLoader registeredImageLoaderWithScreenDelegate] : 104 -> 108
~ ___89-[INUIVoiceShortcutHostContext remoteViewControllerDidDeleteVoiceShortcutWithIdentifier:]_block_invoke : 84 -> 88
~ -[INUIVoiceShortcutHostContext remoteViewControllerDidUpdateVoiceShortcut:error:] : 196 -> 188
~ ___81-[INUIVoiceShortcutHostContext remoteViewControllerDidUpdateVoiceShortcut:error:]_block_invoke : 84 -> 88
~ -[INUIVoiceShortcutHostContext remoteViewControllerDidCreateVoiceShortcut:error:] : 196 -> 188
~ ___81-[INUIVoiceShortcutHostContext remoteViewControllerDidCreateVoiceShortcut:error:]_block_invoke : 84 -> 88
~ ___61-[INUIVoiceShortcutHostContext remoteViewControllerDidCancel]_block_invoke : 68 -> 72
~ -[INUIExtensionRequestInfo copyWithZone:] : 132 -> 136
~ -[INUIExtensionRequestInfo encodeWithCoder:] : 136 -> 144
~ -[INUIExtensionRequestInfo initWithCoder:] : 148 -> 152
~ -[INUIExtensionRequestInfo initWithInteraction:] : 124 -> 116
~ -[INUILoadingVoiceShortcutViewController viewDidLoad] : 496 -> 544
~ -[INUIInterfaceSection encodeWithCoder:] : 108 -> 116
~ -[INUIInterfaceSection initWithCoder:] : 200 -> 212
~ -[INUIInterfaceSection copyWithZone:] : 4 -> 40
~ -[INUIInterfaceSection isEqual:] : 156 -> 144
~ -[_INUIServiceViewController _constrainedSizeForDesiredSize:] : 152 -> 156
~ -[_INUIServiceViewController configureForParameters:ofInteraction:interactiveBehavior:context:completion:] : 616 -> 620
~ ___106-[_INUIServiceViewController configureForParameters:ofInteraction:interactiveBehavior:context:completion:]_block_invoke_4 : 664 -> 700
~ -[_INUIServiceViewController beginRequestWithExtensionContext:] : 172 -> 164
~ -[_INUIServiceViewController viewWillLayoutSubviews] : 128 -> 136
~ -[_INUIServiceViewController addChildViewController:] : 248 -> 264
~ -[INUIRemoteViewController setCurrentRequestIdentifier:] : 20 -> 80
~ -[INUIRemoteViewController setActiveExtension:] : 20 -> 80
~ -[INUIRemoteViewController setExtensionHostContext:] : 20 -> 80
~ -[INUIRemoteViewController setWidgetDescriptor:] : 20 -> 80
~ -[INUIRemoteViewController configureForParameters:ofInteraction:interactiveBehavior:context:completion:] : 808 -> 832
~ ___104-[INUIRemoteViewController configureForParameters:ofInteraction:interactiveBehavior:context:completion:]_block_invoke.68 : 276 -> 280
~ ___104-[INUIRemoteViewController configureForParameters:ofInteraction:interactiveBehavior:context:completion:]_block_invoke_3 : 308 -> 312
~ -[INUIRemoteViewController extensionHostContextWillBeginEditing:] : 100 -> 104
~ -[INUIRemoteViewController extensionHostContext:wantsToHandleIntent:] : 120 -> 124
~ -[INUIRemoteViewController _updateExtensionContextStateWithCompletion:] : 932 -> 960
~ -[INUIRemoteViewController _errorHandlingServiceViewControllerProxy] : 108 -> 120
~ -[INUIRemoteViewController _queryRepresentedPropertiesWithCompletion:] : 96 -> 100
~ -[INUIRemoteViewController desiresInteractivity:] : 176 -> 188
~ -[INUIRemoteViewController requestCancellation] : 124 -> 136
~ -[INUIRemoteViewController setIdealConfiguration:animated:completion:] : 364 -> 372
~ ___70-[INUIRemoteViewController setIdealConfiguration:animated:completion:]_block_invoke : 312 -> 316
~ -[INUIRemoteViewController setDelegate:completion:] : 224 -> 220
~ -[INUIRemoteViewController disconnect] : 148 -> 152
~ -[INUIRemoteViewController viewServiceDidTerminateWithError:] : 296 -> 300
~ +[INUIRemoteViewController requestRemoteViewControllerForInteraction:delegate:connectionHandler:] : 240 -> 232
~ +[INUIRemoteViewController _getWidgetHostingRemoteViewControllerWithIntent:descriptor:completionHandler:] : 1020 -> 1036
~ +[INUIRemoteViewController _attemptToConnectToRemoteViewControllerForRemainingExtensions:delegate:connectionHandler:] : 440 -> 416
~ ___117+[INUIRemoteViewController _attemptToConnectToRemoteViewControllerForRemainingExtensions:delegate:connectionHandler:]_block_invoke : 936 -> 928
~ +[INUIRemoteViewController _requestRemoteViewControllerWithRequestInfo:delegate:reply:] : 628 -> 640
~ ___87+[INUIRemoteViewController _requestRemoteViewControllerWithRequestInfo:delegate:reply:]_block_invoke : 688 -> 680
~ ___114+[INUIRemoteViewController _requestRemoteViewControllerForSnippetExtensionInteraction:delegate:connectionHandler:]_block_invoke : 632 -> 640
~ -[INImage(IntentsUI) fetchUIImageWithCompletion:] : 972 -> 1088
~ ___49-[INImage(IntentsUI) fetchUIImageWithCompletion:]_block_invoke : 332 -> 328
~ +[INImage(IntentsUI) imageWithUIImage:] : 180 -> 192
~ +[INImage(IntentsUI) imageWithCGImage:] : 152 -> 156
~ -[INUIAddVoiceShortcutButton setAddedToSiriLeadingConstraint:] : 20 -> 80
~ -[INUIAddVoiceShortcutButton setAddToSiriLeadingConstraint:] : 20 -> 80
~ -[INUIAddVoiceShortcutButton setCheckmarkHeightConstraint:] : 20 -> 80
~ -[INUIAddVoiceShortcutButton setHighlightFilter:] : 20 -> 80
~ -[INUIAddVoiceShortcutButton dragInteraction:itemsForBeginningSession:] : 260 -> 272
~ -[INUIAddVoiceShortcutButton accessibilityLabel] : 164 -> 180
~ -[INUIAddVoiceShortcutButton traitCollectionDidChange:] : 324 -> 356
~ -[INUIAddVoiceShortcutButton _checkAndUpdateForShortcut] : 144 -> 148
~ ___56-[INUIAddVoiceShortcutButton _checkAndUpdateForShortcut]_block_invoke : 1144 -> 1152
~ -[INUIAddVoiceShortcutButton _didTapButton] : 272 -> 292
~ -[INUIAddVoiceShortcutButton _updatePhraseVisibility] : 204 -> 220
~ -[INUIAddVoiceShortcutButton _updateContent] : 292 -> 324
~ -[INUIAddVoiceShortcutButton _dynamicBlackColor] : 120 -> 128
~ -[INUIAddVoiceShortcutButton _dynamicWhiteColor] : 120 -> 128
~ -[INUIAddVoiceShortcutButton _checkmarkImage] : 120 -> 128
~ -[INUIAddVoiceShortcutButton _dynamicDarkSphiriImage] : 124 -> 136
~ -[INUIAddVoiceShortcutButton _dynamicLightSphiriImage] : 124 -> 136
~ -[INUIAddVoiceShortcutButton _darkSphiriImage] : 120 -> 128
~ -[INUIAddVoiceShortcutButton _lightSphiriImage] : 120 -> 128
~ -[INUIAddVoiceShortcutButton _addToSiriFont] : 164 -> 176
~ -[INUIAddVoiceShortcutButton _phraseText] : 208 -> 228
~ -[INUIAddVoiceShortcutButton _addedToSiriText] : 116 -> 124
~ -[INUIAddVoiceShortcutButton _addToSiriText] : 116 -> 124
~ -[INUIAddVoiceShortcutButton _createHighlightFilterIfNecessary] : 304 -> 316
~ -[INUIAddVoiceShortcutButton _strokeColorForStyle:] : 184 -> 200
~ -[INUIAddVoiceShortcutButton _textColorForStyle:] : 148 -> 164
~ -[INUIAddVoiceShortcutButton _backgroundColorForStyle:] : 148 -> 164
~ -[INUIAddVoiceShortcutButton _sphiriImageForStyle:] : 128 -> 144
~ -[INUIAddVoiceShortcutButton _updateColors] : 352 -> 388
~ -[INUIAddVoiceShortcutButton intrinsicContentSize] : 248 -> 268
~ -[INUIAddVoiceShortcutButton layoutSubviews] : 112 -> 116
~ -[INUIAddVoiceShortcutButton setHighlighted:] : 372 -> 392
~ -[INUIAddVoiceShortcutButton setVoiceShortcut:] : 120 -> 128
~ -[INUIAddVoiceShortcutButton setShortcut:] : 112 -> 128
~ -[INUIAddVoiceShortcutButton dealloc] : 200 -> 212
~ -[INUIAddVoiceShortcutButton _configureWithStyle:] : 3004 -> 3312
~ -[INUIEditVoiceShortcutViewController setCurrentChildViewController:] : 20 -> 80
~ -[INUIEditVoiceShortcutViewController _setRemoteHostViewController:] : 20 -> 80
~ -[INUIEditVoiceShortcutViewController _containedRemoteViewController] : 16 -> 64
~ -[INUIEditVoiceShortcutViewController remoteViewControllerDidCancel] : 80 -> 84
~ -[INUIEditVoiceShortcutViewController remoteViewControllerDidDeleteVoiceShortcutWithIdentifier:] : 148 -> 156
~ -[INUIEditVoiceShortcutViewController remoteViewControllerDidUpdateVoiceShortcut:error:] : 168 -> 172
~ -[INUIEditVoiceShortcutViewController setChildViewController:] : 324 -> 352
~ ___61-[INUIEditVoiceShortcutViewController initWithVoiceShortcut:]_block_invoke : 464 -> 468
~ ___61-[INUIEditVoiceShortcutViewController initWithVoiceShortcut:]_block_invoke.5 : 128 -> 136
~ -[INUIExtensionViewControllerConfiguration encodeWithCoder:] : 164 -> 172
~ -[INUIExtensionViewControllerConfiguration initWithCoder:] : 232 -> 240
~ __INUIUtilitiesBestFittingSizeForSizeBySystemVersionDictionary : 384 -> 400
~ +[INUISearchFoundationImageAdapter _sharedImageLoader] : 84 -> 100
~ ___54+[INUISearchFoundationImageAdapter _sharedImageLoader]_block_invoke : 64 -> 68
~ -[INUISearchFoundationImageAdapter size] : 108 -> 112
~ -[INUISearchFoundationImageAdapter setSize:] : 144 -> 148
~ -[INUISearchFoundationImageAdapter payloadImage] : 124 -> 132
~ -[INUISearchFoundationImageAdapter isEqual:] : 212 -> 216
~ -[INUISearchFoundationImageAdapter initWithPayloadImage:] : 408 -> 428
~ -[SFImage(IntentsUI) downcastToIntentsUIVariantIfApplicable] : 108 -> 112

```
