## BluetoothServicesUI

> `/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`

```diff

-35.14.0.0.0
-  __TEXT.__text: 0x5660
-  __TEXT.__auth_stubs: 0x300
+40.28.1.1.2
+  __TEXT.__text: 0x4f78
   __TEXT.__objc_methlist: 0x78c
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0xf66
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x138
-  __TEXT.__objc_methname: 0x12d8
-  __TEXT.__objc_methtype: 0x1f9
-  __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x160
+  __TEXT.__cstring: 0xf77
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0xf88
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x70

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86B2B2EE-3591-3BAF-9B87-097041ADD305
+  UUID: AA3B77B2-8D59-3D2D-8FF6-07F4773528B5
   Functions: 204
-  Symbols:   760
-  CStrings:  466
+  Symbols:   761
+  CStrings:  177
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_retain
+ _objc_retain_x8
- _objc_release_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ +[BTShareAudioViewController instantiateViewController] : 268 -> 256
~ -[BTShareAudioViewController _moviePathForPID:colorCode:] : 184 -> 180
~ -[BTShareAudioViewController _reportCompletion:mediaRouteID:] : 308 -> 316
~ -[BTShareAudioViewController reportUserCancelled] : 172 -> 168
~ -[BTShareAudioViewController _sessionStart] : 208 -> 196
~ ___43-[BTShareAudioViewController _sessionStart]_block_invoke : 40 -> 44
~ -[BTShareAudioViewController _sessionProgressEvent:info:] : 456 -> 464
~ -[BTShareAudioViewController _showConnecting:] : 296 -> 300
~ -[BTShareAudioViewController _transitionToViewController:animate:] : 384 -> 356
~ -[BTShareAudioViewController completion] : 16 -> 20
~ -[BTShareAudioViewController flags] : 16 -> 20
~ -[BTShareAudioViewController setFlags:] : 16 -> 20
~ -[BTShareAudioViewController shareAudioSession] : 16 -> 20
~ -[BTShareAudioViewController setShareAudioSession:] : 80 -> 20
~ -[BTShareAudioViewController mainBundle] : 16 -> 20
~ -[BTShareAudioViewController setMainBundle:] : 80 -> 20
~ -[BTShareAudioViewController mainStoryboard] : 16 -> 20
~ -[BTShareAudioViewController setMainStoryboard:] : 80 -> 20
~ -[BTShareAudioViewController vcConnecting] : 16 -> 20
~ -[BTShareAudioViewController setVcConnecting:] : 80 -> 20
~ -[BTShareAudioBaseViewController viewWillAppear:] : 288 -> 296
~ -[BTShareAudioBaseViewController viewWillDisappear:] : 80 -> 84
~ -[BTShareAudioBaseViewController _handleMenuButton:] : 136 -> 140
~ -[BTShareAudioBaseViewController mainController] : 16 -> 20
~ -[BTShareAudioBaseViewController setMainController:] : 80 -> 20
~ -[BTShareAudioBaseViewController titleLabel] : 16 -> 20
~ -[BTShareAudioBaseViewController setTitleLabel:] : 80 -> 20
~ -[BTShareAudioBaseViewController cardView] : 16 -> 20
~ -[BTShareAudioBaseViewController setCardView:] : 80 -> 20
~ -[BTShareAudioBaseViewController viewActive] : 16 -> 20
~ -[BTShareAudioBaseViewController setViewActive:] : 16 -> 20
~ -[BTShareAudioBringCloseViewController viewWillAppear:] : 324 -> 320
~ -[BTShareAudioBringCloseViewController viewWillDisappear:] : 180 -> 184
~ -[BTShareAudioBringCloseViewController viewDidLayoutSubviews] : 448 -> 424
~ -[BTShareAudioBringCloseViewController eventCancel:] : 136 -> 140
~ -[BTShareAudioBringCloseViewController _cycleProductImage] : 992 -> 972
~ -[BTShareAudioBringCloseViewController infoLabel] : 16 -> 20
~ -[BTShareAudioBringCloseViewController setInfoLabel:] : 80 -> 20
~ -[BTShareAudioBringCloseViewController bannerImageView] : 16 -> 20
~ -[BTShareAudioBringCloseViewController setBannerImageView:] : 80 -> 20
~ -[BTShareAudioBringCloseViewController productImageContainerView] : 16 -> 20
~ -[BTShareAudioBringCloseViewController setProductImageContainerView:] : 80 -> 20
~ -[BTShareAudioBringCloseViewController shareImageView] : 16 -> 20
~ -[BTShareAudioBringCloseViewController setShareImageView:] : 80 -> 20
~ -[BTShareAudioBringCloseViewController cancelButton] : 16 -> 20
~ -[BTShareAudioBringCloseViewController setCancelButton:] : 80 -> 20
~ -[BTShareAudioConfirmViewController viewWillAppear:] : 624 -> 648
~ ___52-[BTShareAudioConfirmViewController viewWillAppear:]_block_invoke : 220 -> 224
~ -[BTShareAudioConfirmViewController viewWillDisappear:] : 144 -> 148
~ -[BTShareAudioConfirmViewController eventCancel:] : 136 -> 140
~ -[BTShareAudioConfirmViewController _updateDeviceVisual:] : 600 -> 592
~ -[BTShareAudioConfirmViewController productImageView] : 16 -> 20
~ -[BTShareAudioConfirmViewController setProductImageView:] : 80 -> 20
~ -[BTShareAudioConfirmViewController productMovieView] : 16 -> 20
~ -[BTShareAudioConfirmViewController setProductMovieView:] : 80 -> 20
~ -[BTShareAudioConfirmViewController confirmButton] : 16 -> 20
~ -[BTShareAudioConfirmViewController setConfirmButton:] : 80 -> 20
~ -[BTShareAudioConfirmViewController cancelButton] : 16 -> 20
~ -[BTShareAudioConfirmViewController setCancelButton:] : 80 -> 20
~ -[BTShareAudioConfirmViewController shareImageView] : 16 -> 20
~ -[BTShareAudioConfirmViewController setShareImageView:] : 80 -> 20
~ -[BTShareAudioConfirmViewController colorCode] : 16 -> 20
~ -[BTShareAudioConfirmViewController setColorCode:] : 16 -> 20
~ -[BTShareAudioConfirmViewController deviceName] : 16 -> 20
~ -[BTShareAudioConfirmViewController productID] : 16 -> 20
~ -[BTShareAudioConfirmViewController setProductID:] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController viewWillAppear:] : 628 -> 640
~ ___55-[BTShareAudioHoldButtonViewController viewWillAppear:]_block_invoke : 220 -> 224
~ -[BTShareAudioHoldButtonViewController viewWillDisappear:] : 144 -> 148
~ -[BTShareAudioHoldButtonViewController viewDidLayoutSubviews] : 564 -> 536
~ -[BTShareAudioHoldButtonViewController eventCancel:] : 136 -> 140
~ -[BTShareAudioHoldButtonViewController _holdImageForPID:colorCode:] : 300 -> 296
~ -[BTShareAudioHoldButtonViewController _updateDeviceVisual:] : 620 -> 616
~ -[BTShareAudioHoldButtonViewController productImageView] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setProductImageView:] : 80 -> 20
~ -[BTShareAudioHoldButtonViewController productMovieView] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setProductMovieView:] : 80 -> 20
~ -[BTShareAudioHoldButtonViewController productMovieContainerView] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setProductMovieContainerView:] : 80 -> 20
~ -[BTShareAudioHoldButtonViewController shareImageView] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setShareImageView:] : 80 -> 20
~ -[BTShareAudioHoldButtonViewController infoLabel] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setInfoLabel:] : 80 -> 20
~ -[BTShareAudioHoldButtonViewController cancelButton] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setCancelButton:] : 80 -> 20
~ -[BTShareAudioHoldButtonViewController colorCode] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setColorCode:] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController productID] : 16 -> 20
~ -[BTShareAudioHoldButtonViewController setProductID:] : 16 -> 20
~ -[BTShareAudioConnectingViewController viewWillAppear:] : 272 -> 280
~ -[BTShareAudioConnectingViewController viewWillDisappear:] : 164 -> 172
~ -[BTShareAudioConnectingViewController eventCancel:] : 136 -> 140
~ -[BTShareAudioConnectingViewController _updateForDeviceInfo] : 516 -> 540
~ ___60-[BTShareAudioConnectingViewController _updateForDeviceInfo]_block_invoke : 220 -> 224
~ -[BTShareAudioConnectingViewController _updateDeviceVisual:] : 600 -> 592
~ -[BTShareAudioConnectingViewController productImageView] : 16 -> 20
~ -[BTShareAudioConnectingViewController setProductImageView:] : 80 -> 20
~ -[BTShareAudioConnectingViewController productMovieView] : 16 -> 20
~ -[BTShareAudioConnectingViewController setProductMovieView:] : 80 -> 20
~ -[BTShareAudioConnectingViewController shareImageView] : 16 -> 20
~ -[BTShareAudioConnectingViewController setShareImageView:] : 80 -> 20
~ -[BTShareAudioConnectingViewController progressView] : 16 -> 20
~ -[BTShareAudioConnectingViewController setProgressView:] : 80 -> 20
~ -[BTShareAudioConnectingViewController progressActivity] : 16 -> 20
~ -[BTShareAudioConnectingViewController setProgressActivity:] : 80 -> 20
~ -[BTShareAudioConnectingViewController progressLabel] : 16 -> 20
~ -[BTShareAudioConnectingViewController setProgressLabel:] : 80 -> 20
~ -[BTShareAudioConnectingViewController cancelButton] : 16 -> 20
~ -[BTShareAudioConnectingViewController setCancelButton:] : 80 -> 20
~ -[BTShareAudioConnectingViewController colorCode] : 16 -> 20
~ -[BTShareAudioConnectingViewController setColorCode:] : 16 -> 20
~ -[BTShareAudioConnectingViewController deviceName] : 16 -> 20
~ -[BTShareAudioConnectingViewController productID] : 16 -> 20
~ -[BTShareAudioConnectingViewController setProductID:] : 16 -> 20
~ -[BTShareAudioErrorViewController viewWillAppear:] : 368 -> 372
~ -[BTShareAudioErrorViewController eventDismiss:] : 148 -> 156
~ -[BTShareAudioErrorViewController infoLabel] : 16 -> 20
~ -[BTShareAudioErrorViewController setInfoLabel:] : 80 -> 20
~ -[BTShareAudioErrorViewController internalLabel] : 16 -> 20
~ -[BTShareAudioErrorViewController setInternalLabel:] : 80 -> 20
~ -[BTShareAudioErrorViewController dismissButton] : 16 -> 20
~ -[BTShareAudioErrorViewController setDismissButton:] : 80 -> 20
~ -[BTShareAudioErrorViewController error] : 16 -> 20
~ _OUTLINED_FUNCTION_2 : 28 -> 32
~ -[BTMediaPlayerView startMovieLoopWithPath:] : 380 -> 368
~ -[BTMediaPlayerView startMovieLoopWithPath:assetType:adjustmentsURL:] : 664 -> 644
~ -[BTMediaPlayerView stop] : 140 -> 144
~ ___52-[BTShareAudioConfirmViewController viewWillAppear:]_block_invoke.cold.1 : 64 -> 68
~ ___55-[BTShareAudioHoldButtonViewController viewWillAppear:]_block_invoke.cold.1 : 64 -> 68
~ -[BTShareAudioConnectingViewController _updateForDeviceInfo].cold.1 : 80 -> 84
~ ___60-[BTShareAudioConnectingViewController _updateForDeviceInfo]_block_invoke.cold.1 : 64 -> 68
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AVPlayerLooper\""
- "@\"AVQueuePlayer\""
- "@\"BTMediaPlayerView\""
- "@\"BTShareAudioConnectingViewController\""
- "@\"BTShareAudioSessionClient\""
- "@\"BTShareAudioViewController\""
- "@\"NSBundle\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"UIActivityIndicatorView\""
- "@\"UIButton\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIStoryboard\""
- "@\"UIView\""
- "@16@0:8"
- "@24@0:8I16I20"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "BTHighlightButton"
- "BTMediaPlayerView"
- "BTShareAudioBaseViewController"
- "BTShareAudioBringCloseViewController"
- "BTShareAudioConfirmViewController"
- "BTShareAudioConnectingViewController"
- "BTShareAudioErrorViewController"
- "BTShareAudioHoldButtonViewController"
- "BTSharedAudioDeviceInfo"
- "CGColor"
- "I"
- "I16@0:8"
- "T@\"BTMediaPlayerView\",&,N,V_productMovieView"
- "T@\"BTShareAudioConnectingViewController\",&,N,V_vcConnecting"
- "T@\"BTShareAudioSessionClient\",&,N,V_shareAudioSession"
- "T@\"BTShareAudioViewController\",&,N,V_mainController"
- "T@\"NSBundle\",&,N,V_mainBundle"
- "T@\"NSError\",C,N,V_error"
- "T@\"NSString\",C,N,V_deviceName"
- "T@\"NSString\",C,N,V_mediaRouteIdentifier"
- "T@\"UIActivityIndicatorView\",&,N,V_progressActivity"
- "T@\"UIButton\",&,N,V_cancelButton"
- "T@\"UIButton\",&,N,V_confirmButton"
- "T@\"UIButton\",&,N,V_dismissButton"
- "T@\"UIImageView\",&,N,V_bannerImageView"
- "T@\"UIImageView\",&,N,V_productImageView"
- "T@\"UIImageView\",&,N,V_shareImageView"
- "T@\"UILabel\",&,N,V_infoLabel"
- "T@\"UILabel\",&,N,V_internalLabel"
- "T@\"UILabel\",&,N,V_progressLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "T@\"UIStoryboard\",&,N,V_mainStoryboard"
- "T@\"UIView\",&,N,V_cardView"
- "T@\"UIView\",&,N,V_productImageContainerView"
- "T@\"UIView\",&,N,V_productMovieContainerView"
- "T@\"UIView\",&,N,V_progressView"
- "T@?,C,N,V_completion"
- "TB,N,V_viewActive"
- "TI,N,V_colorCode"
- "TI,N,V_flags"
- "TI,N,V_productID"
- "_avLooper"
- "_avPlayer"
- "_bannerImageView"
- "_cancelButton"
- "_cardView"
- "_colorCode"
- "_completion"
- "_confirmButton"
- "_cycleImageArray"
- "_cycleImageTimer"
- "_cycleNextIndex"
- "_cycleProductImage"
- "_deviceName"
- "_dismissButton"
- "_error"
- "_flags"
- "_handleMenuButton:"
- "_holdImageForPID:colorCode:"
- "_imageForPID:colorCode:"
- "_infoLabel"
- "_internalLabel"
- "_mainBundle"
- "_mainController"
- "_mainStoryboard"
- "_mediaRouteIdentifier"
- "_moviePathForPID:colorCode:"
- "_productID"
- "_productIDActive"
- "_productImageContainerView"
- "_productImageView"
- "_productMovieContainerView"
- "_productMovieView"
- "_progressActivity"
- "_progressLabel"
- "_progressView"
- "_reportCompletion:mediaRouteID:"
- "_sessionProgressEvent:info:"
- "_sessionStart"
- "_setContinuousCornerRadius:"
- "_setDisallowsAutoPauseOnRouteRemovalIfNoAudio:"
- "_shareAudioSession"
- "_shareImageView"
- "_showBringClose"
- "_showConfirm:"
- "_showConnecting:"
- "_showError:"
- "_showPairInstructions:"
- "_titleLabel"
- "_transitionToViewController:animate:"
- "_updateDeviceVisual:"
- "_updateForDeviceInfo"
- "_vcConnecting"
- "_viewActive"
- "activate"
- "addAnimation:forKey:"
- "addGestureRecognizer:"
- "addObject:"
- "animation"
- "arrayWithObjects:count:"
- "assetBundlePath"
- "bannerImageView"
- "bounds"
- "bundleWithIdentifier:"
- "cancelButton"
- "cardView"
- "code"
- "colorWithWhite:alpha:"
- "completion"
- "configurationByApplyingConfiguration:"
- "configurationWithHierarchicalColor:"
- "configurationWithPointSize:weight:scale:"
- "confirmButton"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "darkGrayColor"
- "dictionaryWithContentsOfURL:error:"
- "dismissButton"
- "eventCancel:"
- "eventDismiss:"
- "eventPermanentButton:"
- "eventTemporarilyShareButton:"
- "fileURLWithPath:isDirectory:"
- "flags"
- "functionWithName:"
- "getDeviceAssets:completion:"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "infoLabel"
- "initWithFormat:"
- "initWithTarget:action:"
- "initWithType:"
- "instantiateViewController"
- "instantiateViewControllerWithIdentifier:"
- "internalLabel"
- "invalidate"
- "layer"
- "layerClass"
- "mainBundle"
- "mainController"
- "mainScreen"
- "mainStoryboard"
- "mask"
- "mediaRouteIdentifier"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "pathForResource:ofType:"
- "pause"
- "play"
- "playerItemWithURL:"
- "playerLooperWithPlayer:templateItem:"
- "popToViewController:animated:"
- "productID"
- "productImageContainerView"
- "productImageView"
- "productMovieContainerView"
- "productMovieView"
- "progressActivity"
- "progressLabel"
- "progressView"
- "pushViewController:animated:"
- "removeAllItems"
- "reportError:"
- "reportUserCancelled"
- "scale"
- "sessionProgressEvent:info:"
- "setAllowedPressTypes:"
- "setAllowsExternalPlayback:"
- "setAlpha:"
- "setBackgroundColor:"
- "setBannerImageView:"
- "setBluetoothProductID:"
- "setCancelButton:"
- "setCardView:"
- "setCategory:withOptions:error:"
- "setColorCode:"
- "setColors:"
- "setCompletion:"
- "setConfirmButton:"
- "setContentMode:"
- "setDeviceName:"
- "setDismissButton:"
- "setDuration:"
- "setEndPoint:"
- "setError:"
- "setFilters:"
- "setFlags:"
- "setFrame:"
- "setHidden:"
- "setHighlighted:"
- "setImage:"
- "setInfoLabel:"
- "setInternalLabel:"
- "setLocations:"
- "setMainBundle:"
- "setMainController:"
- "setMainStoryboard:"
- "setMask:"
- "setMediaRouteIdentifier:"
- "setModalPresentationStyle:"
- "setModalTransitionStyle:"
- "setMode:"
- "setNumberOfLines:"
- "setNumberOfTapsRequired:"
- "setPlayer:"
- "setPreferredSymbolConfiguration:"
- "setPreventsDisplaySleepDuringVideoPlayback:"
- "setProductID:"
- "setProductImageContainerView:"
- "setProductImageView:"
- "setProductMovieContainerView:"
- "setProductMovieView:"
- "setProgressActivity:"
- "setProgressHandler:"
- "setProgressLabel:"
- "setProgressView:"
- "setShareAudioSession:"
- "setShareImageView:"
- "setStartPoint:"
- "setSubtype:"
- "setText:"
- "setTimeoutSeconds:"
- "setTimingFunction:"
- "setTintColor:"
- "setTitle:"
- "setTitle:forState:"
- "setTitleLabel:"
- "setType:"
- "setValue:forKey:"
- "setVcConnecting:"
- "setViewActive:"
- "shareAudioSession"
- "shareImageView"
- "sharedInstance"
- "startAnimating"
- "startMovieLoopWithPath:"
- "startMovieLoopWithPath:assetType:adjustmentsURL:"
- "stop"
- "storyboardWithName:bundle:"
- "systemImageNamed:"
- "titleLabel"
- "userConfirmed:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@16B24"
- "v28@0:8i16@20"
- "v32@0:8@16@24"
- "v36@0:8@16i24@28"
- "valueWithCAColorMatrix:"
- "vcConnecting"
- "view"
- "viewActive"
- "viewControllers"
- "viewDidLayoutSubviews"
- "viewWillAppear:"
- "viewWillDisappear:"
- "whiteColor"

```
