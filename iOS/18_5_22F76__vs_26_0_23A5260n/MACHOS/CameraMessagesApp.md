## CameraMessagesApp

> `/System/Library/ExtensionKit/Extensions/CameraMessagesApp.appex/CameraMessagesApp`

```diff

-4026.120.2.0.0
-  __TEXT.__text: 0x9364
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x28c0
-  __TEXT.__objc_methlist: 0xb40
-  __TEXT.__objc_methname: 0x3542
-  __TEXT.__cstring: 0x3c4
-  __TEXT.__objc_classname: 0x266
-  __TEXT.__objc_methtype: 0xc63
-  __TEXT.__const: 0x130
-  __TEXT.__oslogstring: 0xd1c
-  __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x438
-  __DATA_CONST.__cfstring: 0x220
+4082.0.0.122.5
+  __TEXT.__text: 0x6804
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x1e20
+  __TEXT.__objc_methlist: 0x888
+  __TEXT.__objc_methname: 0x27bf
+  __TEXT.__cstring: 0x295
+  __TEXT.__objc_classname: 0x21f
+  __TEXT.__objc_methtype: 0xab0
+  __TEXT.__const: 0x98
+  __TEXT.__oslogstring: 0x82c
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__unwind_info: 0x250
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xd28
-  __DATA.__objc_selrefs: 0xc98
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_const: 0xb78
+  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x420
-  __DATA.__bss: 0x78
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6AE36AC-E627-30D3-9E80-EFACF0075CC7
-  Functions: 227
-  Symbols:   182
-  CStrings:  684
+  UUID: 186D220B-9331-36D2-AF49-324C08092CDF
+  Functions: 165
+  Symbols:   146
+  CStrings:  526
 
Symbols:
+ _OBJC_CLASS_$_CAMUserPreferences
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ _objc_retain_x4
- _AVMediaTypeVideo
- _CEKIsViewInMultitask
- _CFRelease
- _CGImageRelease
- _CGImageSourceCopyPropertiesAtIndex
- _CGImageSourceCreateThumbnailAtIndex
- _CGImageSourceCreateWithURL
- _CGRectStandardize
- _CGSizeZero
- _CMTimeGetSeconds
- _CMTimeMakeWithSeconds
- _OBJC_CLASS_$_AVAsset
- _OBJC_CLASS_$_AVAssetImageGenerator
- _OBJC_CLASS_$_CAMCaptureConversions
- _OBJC_CLASS_$_CAMUserPreferenceOverrides
- _OBJC_CLASS_$_CAMView
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_PFAssetAdjustments
- _OBJC_CLASS_$_PLUUIDString
- _OBJC_CLASS_$_PUReviewAsset
- _OBJC_CLASS_$_UIScreen
- _PLScaledSizeToFitSize
- _PUFunEffectsAdjustmentFormatIdentifier
- _PUFunEffectsAdjustmentFormatVersion
- _kCFBooleanTrue
- _kCGImagePropertyOrientation
- _kCGImagePropertyPixelHeight
- _kCGImagePropertyPixelWidth
- _kCGImageSourceCreateThumbnailFromImageAlways
- _kCGImageSourceCreateThumbnailFromImageIfAbsent
- _kCGImageSourceCreateThumbnailWithTransform
- _kCGImageSourceThumbnailMaxPixelSize
- _objc_opt_respondsToSelector
- _objc_retain_x21
- _objc_retain_x9
- _sysctl
CStrings:
+ "\""
+ "_preferredContentSizeCategoryChanged"
+ "_saveAssetIfNeeded:"
+ "initWithReferenceBounds:shutterIntrinsicSize:usingExternalChrome:"
+ "isSolCamEnabled"
+ "preferences"
+ "registerForTraitChanges:withAction:"
+ "saveMessagesCapturesPhotoLibrary"
+ "setModalTransitionStyle:"
- "#"
- "/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit"
- "<CFXCamera> Failed to create review asset for mediaItem, not proceeding with review"
- "@\"CAMUserPreferenceOverrides\""
- "@\"CFXCameraViewController\""
- "AVDevicePositionForCAMDevicePosition:"
- "CAMCreativeCameraDelegate"
- "CAMDevicePositionForAVDevicePosition:"
- "CFXCamera"
- "CFXCamera started while in state %{public}@, not taking action"
- "CFXCamera stopped while in state %{public}@, not taking action"
- "CFXCameraStopped_RegularCameraStarting"
- "CFXCameraStoppingForRegularCamera"
- "CFXCameraViewController"
- "CFXCameraViewControllerDelegate"
- "CFXMediaItem"
- "CFXMediaItem does not have originalAssetURL"
- "Cannot switch cameras from state %{public}@"
- "Could not generate preview image for %{public}@. Error: %{public}@"
- "Creating review asset for photo took %.3f seconds"
- "Creating review asset for video took %.3f seconds"
- "Dismissing from cameraViewControllerDoneButtonWasTapped (CFXCameraViewController)"
- "Dismissing from cameraViewControllerRequestedDismissal (CAMCameraViewController)"
- "Ignoring volume button press because review view controller is presented"
- "Ignoring volume button press during state %{public}@"
- "Ignoring volume button press for CFXCamera since no capture API available"
- "Received NSExtensionHostDidEnterBackgroundNotification while showing CFXCamera (cannot verify if recording), dismissing CameraMessagesApp extension."
- "RegularCameraStopped_CFXCameraStarting"
- "RegularCameraStoppingForCFXCamera"
- "Should not be trying to start CFX camera from %{public}@"
- "T@\"CAMUserPreferenceOverrides\",&,N,S_setUserPreferenceOverrides:,V__userPreferenceOverrides"
- "T@\"CFXCameraViewController\",&,N,S_setCfxCameraViewController:,V__cfxCameraViewController"
- "T@\"CFXCameraViewController\",&,N,V_funCamViewController"
- "TB,R,N,V__shouldShowFunEffects"
- "Trying to start CFXCamera but no view controller found"
- "UUIDString"
- "Unable to create AVAsset for '%{public}@'."
- "Unable to create image source for '%{public}@'."
- "Unable to find valid duration for '%{public}@'."
- "Unknown media type for CFXMediaItem"
- "__cfxCameraViewController"
- "__shouldShowFunEffects"
- "__userPreferenceOverrides"
- "_assetAdjustmentsFromCFXMediaItem:"
- "_avDevicePositionFromUserPreferenceOverrides:"
- "_avFlashModeFromUserPreferenceOverrides:"
- "_canCaptureFromMessagesCaptureState:"
- "_cfxAspectRatioCropFromUserPreferenceOverrides:"
- "_cfxCameraDidStartCaptureSession"
- "_cfxCameraDidStopCaptureSession"
- "_cfxCameraViewController"
- "_cfxCaptureModeFromUserPreferenceOverrides:"
- "_createAndEmbedCFXCameraViewControllerIfNecessary"
- "_deviceMemorySize"
- "_deviceSupportsFunEffects"
- "_dismissAndPresentPhotosApp"
- "_fadeInViewController:overOutgoingViewController:"
- "_funCamViewController"
- "_photoReviewAssetFromCFXMediaItem:"
- "_preheatCFXCameraFromUserPreferenceOverrides:"
- "_saveAsset:"
- "_setCfxCameraViewController:"
- "_setUserPreferenceOverrides:"
- "_shouldShowFunEffects"
- "_startCFXCamera"
- "_startCFXCamera:"
- "_stopAndReleaseCFXCameraViewController"
- "_stopCFXCamera"
- "_stopCFXCamera:"
- "_switchCameraViewControllers"
- "_userPreferenceOverrides"
- "_userPreferenceOverridesFromCFXCamera:baseUserPreferenceOverrides:"
- "_userPreferenceOverridesFromRegularCamera:baseUserPreferenceOverrides:"
- "_videoReviewAssetFromCFXMediaItem:"
- "_volumeButtonPressed:"
- "adjustmentsData"
- "animateIfNeededWithDuration:options:animations:completion:"
- "aspectRatioCrop"
- "assetWithURL:"
- "cam_screenPixelSize"
- "cameraViewController:didCaptureMediaItem:"
- "cameraViewController:didChangeEffectsState:"
- "cameraViewController:didDropFrame:"
- "cameraViewController:didRenderFrame:"
- "cameraViewController:presentationRectWasPinchedWithState:scale:velocity:"
- "cameraViewControllerCreativeCameraButtonWasPressed"
- "cameraViewControllerCreativeCameraButtonWasReleased"
- "cameraViewControllerDidRequestDismissal"
- "cameraViewControllerDidRequestPhotosExtension"
- "cameraViewControllerDidStartCaptureSession:"
- "cameraViewControllerDidStopCaptureSession:"
- "cameraViewControllerDoneButtonWasTapped:"
- "cameraViewControllerEffectsButtonWasTapped:"
- "cameraViewControllerPresentationRectWasDoubleTapped:"
- "captureDevice"
- "captureFlashModeForFlashMode:"
- "com.apple.camera.softlink.CameraEffectsKit"
- "copyCGImageAtTime:actualTime:error:"
- "date"
- "devicePosition"
- "dictionaryWithObjects:forKeys:count:"
- "duration"
- "flashMode"
- "flashModeForCaptureFlashMode:"
- "funCamViewController"
- "handleVolumeButtonPressed"
- "handleVolumeButtonReleased"
- "imageWithCGImage:"
- "initWithAVAsset:audioMix:width:height:captureDate:duration:previewImage:videoURL:adjustments:identifier:"
- "initWithAsset:"
- "initWithCaptureMode:devicePosition:flashMode:aspectRatioCrop:"
- "initWithFormatIdentifier:formatVersion:data:baseVersion:editorBundleID:renderTypes:"
- "initWithOverrides:"
- "initWithPhoto:mediaSubtypes:width:height:captureDate:metadata:burstIdentifier:representedCount:fullsizeImageURL:fullsizeUnadjustedImageURL:assetAdjustments:identifier:"
- "initWithReferenceBounds:shutterIntrinsicSize:"
- "intValue"
- "integerValue"
- "isEqualToString:"
- "mainScreen"
- "mediaSubtypes"
- "mode"
- "naturalSize"
- "numberWithInteger:"
- "objectForKeyedSubscript:"
- "originalAssetURL"
- "path"
- "photoModeAspectRatioCrop"
- "preferredContentSizeCategory"
- "preferredTransform"
- "preheatWithWindow:captureMode:devicePosition:aspectRatioCrop:"
- "q24@0:8@16"
- "reviewAssetFromCFXMediaItem:"
- "setAppliesPreferredTrackTransform:"
- "setAspectRatioCrop:"
- "setCaptureDevice:"
- "setCaptureMode:"
- "setCreativeCameraDelegate:"
- "setFlashMode:"
- "setFunCamViewController:"
- "setMaximumSize:"
- "setTorchMode:"
- "setTransitionState:animated:"
- "setTransitioningDelegate:"
- "startCaptureSession"
- "stopCaptureSession"
- "torchMode"
- "tracksWithMediaType:"
- "traitCollection"
- "traitCollectionDidChange:"
- "type"
- "v24@0:8@\"CFXCameraViewController\"16"
- "v32@0:8@\"CFXCameraViewController\"16@\"CFXFrame\"24"
- "v32@0:8@\"CFXCameraViewController\"16@\"CFXMediaItem\"24"
- "v32@0:8@\"CFXCameraViewController\"16^{__CVBuffer=}24"
- "v32@0:8@\"CFXCameraViewController\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16^{__CVBuffer=}24"
- "v32@0:8@16q24"
- "v48@0:8@\"CFXCameraViewController\"16q24d32d40"
- "v48@0:8@16q24d32d40"
- "{CGSize=dd}16@0:8"

```
