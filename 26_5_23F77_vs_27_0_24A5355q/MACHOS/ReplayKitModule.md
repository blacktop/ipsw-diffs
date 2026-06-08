## ReplayKitModule

> `/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule`

```diff

-710.1.1.0.0
-  __TEXT.__text: 0xa2d4
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__objc_methlist: 0xb48
+740.44.1.0.0
+  __TEXT.__text: 0xbb4c
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x1fa0
+  __TEXT.__objc_methlist: 0xda0
   __TEXT.__const: 0xb8
-  __TEXT.__objc_methname: 0x283d
-  __TEXT.__oslogstring: 0xc0f
-  __TEXT.__cstring: 0x1868
-  __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methtype: 0x75b
-  __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x2e8
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0x580
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__cstring: 0x1f96
+  __TEXT.__objc_methname: 0x2f8c
+  __TEXT.__oslogstring: 0x1011
+  __TEXT.__objc_classname: 0x178
+  __TEXT.__objc_methtype: 0x965
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__unwind_info: 0x350
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x19f0
-  __DATA.__objc_selrefs: 0xa60
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x168
+  __DATA.__objc_const: 0x1ed8
+  __DATA.__objc_selrefs: 0xc58
+  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/ReplayKit.framework/ReplayKit
+  - /System/Library/Frameworks/ScreenCaptureKit.framework/ScreenCaptureKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE6A2CF6-C123-3D74-87FE-B6E4ACE2FA48
-  Functions: 193
-  Symbols:   137
-  CStrings:  737
+  UUID: F2680B86-94CB-3A94-96FB-4D665CC688A1
+  Functions: 239
+  Symbols:   153
+  CStrings:  868
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleTemplatePreviewDescription
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_SCContentFilter
+ _OBJC_CLASS_$_SCContentSharingPickerInfo
+ _OBJC_CLASS_$_SCControlCenterManager
+ _OBJC_CLASS_$_SCControlCenterManagerBridge
+ _OBJC_METACLASS_$_SCControlCenterManagerBridge
+ _SCContentFilterCreateiOSDisplayFilterDictionary
+ _dispatch_get_global_queue
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x4
+ _os_variant_allows_internal_security_policies
- _UIImagePNGRepresentation
- _objc_retain_x26
CStrings:
+ " [ERROR] %{public}s:%d Do not have application info for SCK picker"
+ " [ERROR] %{public}s:%d Should have an active picker from replayd, presenting ScreenCaptureKit menu item: %@"
+ " [ERROR] %{public}s:%d Trying to stop stream for Control Center menu item without a streamID"
+ " [ERROR] %{public}s:%d error=%@"
+ " [INFO] %{public}s:%d Cancel ScreenCaptureKit picker, will call dismissModule"
+ " [INFO] %{public}s:%d Did add %lu SCK menu item(s) (autoSelect=%@)"
+ " [INFO] %{public}s:%d Did call registerObserver on SCControlCenterManager"
+ " [INFO] %{public}s:%d Did not update button label and menu items, window=%@, expanded=%@"
+ " [INFO] %{public}s:%d End ScreenCaptureKit picker, will call dismissModule"
+ " [INFO] %{public}s:%d ScreenCaptureKit picker cancelled by user"
+ " [INFO] %{public}s:%d Will stop stream - streamID=%@"
+ " [INFO] %{public}s:%d broadcast extensions count 0"
+ " [INFO] %{public}s:%d environmentIDs=%@"
+ " [INFO] %{public}s:%d initialized SCControlCenterManagerBridge for observing %@"
+ " [INFO] %{public}s:%d isScreenCaptureKitPicker=%@, pickerPresenterHasActiveStream=%@, _client.recordingType=%@"
+ "-[RPControlCenterMenuModuleViewController activePickerForPresentingApp]"
+ "-[RPControlCenterMenuModuleViewController addSCKMenuItemIfExists:]"
+ "-[RPControlCenterMenuModuleViewController cancelScreenCaptureKitPickerWithDismiss:]"
+ "-[RPControlCenterMenuModuleViewController endScreenCaptureKitPicker]"
+ "-[RPControlCenterMenuModuleViewController handleNonScreenCapureKitRecordButtonTapped]"
+ "-[RPControlCenterMenuModuleViewController handleScreenCaptureKitRecordButtonTapped]"
+ "-[RPControlCenterMenuModuleViewController setupMenuForScreenCaptureKitPicker:]"
+ "-[RPControlCenterMenuModuleViewController stopStreamForButtonAction]"
+ "-[RPControlCenterMenuModuleViewController willTransitionToExpandedContentMode:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:didAddPicker:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:didGrantEndowmentWithEnvironmentIDs:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:didRemovePicker:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:pickerDidChange:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:serverDiedWithError:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:startPickingForPicker:forStream:withContentStyle:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:startPickingForPicker:forStream:withFilter:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:streamDidChange:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:streamDidEnd:]"
+ "-[SCControlCenterManagerBridge controlCenterManager:streamDidStart:]"
+ "-[SCControlCenterManagerBridge registerObservers]_block_invoke"
+ "@\"<CCUIContentModulePreviewProviding>\"24@0:8@\"CCUIContentModulePreviewContext\"16"
+ "CONTROL_CENTER_DISCLAIMER_SCK_IOS"
+ "CONTROL_CENTER_DISCLAIMER_SCK_IOS_CHINA"
+ "CONTROL_CENTER_SHARE_ENTIRE_SCREEN"
+ "CONTROL_CENTER_STOP_SHARING"
+ "CONTROL_CENTER_TITLE_SCK_PICKER"
+ "DeviceSupportsAlwaysOnTime"
+ "SCControlCenterManagerBridge"
+ "SCControlCenterManagerObserver"
+ "SCKEnableSCKIOS"
+ "ScreenCaptureKitiOS"
+ "ScreenCaptureKitvisionOS"
+ "T@\"SCControlCenterManagerBridge\",R"
+ "UTF8String"
+ "_backgroundReplacementEnabled"
+ "_edgeLightEnabled"
+ "_screenCaptureKitiOS"
+ "_screenCaptureKitvisionOS"
+ "activePickerForPresentingApp"
+ "activeStreamID"
+ "activeStreamScreenCaptureKitMenuItem"
+ "addSCKMenuItemIfExists:"
+ "addSystemRecordingItemToSCKPickerIfExists:"
+ "backgroundReplacementEnabled"
+ "bundleID"
+ "cameraRollImageData"
+ "cameraRollInfoItem"
+ "cancelScreenCaptureKitPickerWithDismiss:"
+ "clearCacheAndUpdateClientState"
+ "clearScreenCaptureKitMenuItem"
+ "com.apple.replayd"
+ "contentModuleContext"
+ "controlCenterManager:didAddPicker:"
+ "controlCenterManager:didGrantEndowmentWithEnvironmentIDs:"
+ "controlCenterManager:didRemovePicker:"
+ "controlCenterManager:pickerDidChange:"
+ "controlCenterManager:serverDiedWithError:"
+ "controlCenterManager:startPickingForPicker:forStream:withContentStyle:"
+ "controlCenterManager:startPickingForPicker:forStream:withFilter:"
+ "controlCenterManager:streamDidChange:"
+ "controlCenterManager:streamDidEnd:"
+ "controlCenterManager:streamDidStart:"
+ "controlCenterMenuItem"
+ "currentActivePicker"
+ "dismissModule"
+ "edgeLight"
+ "edgeLightEnabled"
+ "endScreenCaptureKitPicker"
+ "essonite_bg_ios"
+ "firstObject"
+ "handleNonScreenCapureKitRecordButtonTapped"
+ "handleScreenCaptureKitRecordButtonTapped"
+ "hasScreenCaptureKitMenuItem"
+ "initWithConfiguration:"
+ "initWithDescription:"
+ "initWithDictionary:"
+ "initWithTitle:identifier:image:handler:"
+ "isClientRecordingTypeScreenCaptureKit"
+ "isScreenCaptureKitPicker"
+ "numberWithBool:"
+ "numberWithUnsignedInteger:"
+ "objectForKeyedSubscript:"
+ "pickerDidCancel:forStreamInfo:"
+ "pickerDidEnd:withFilter:forStreamInfo:"
+ "presenterOwnsActiveStream"
+ "presentingScreenCaptureKitMenuItem"
+ "previewProviderForContext:"
+ "recordButtonLabelForScreenCaptureKit"
+ "recordingType"
+ "registerObserver:"
+ "registerObservers"
+ "replaykit-recording-v3"
+ "replaykit-recording-v3_IC"
+ "responsibleWebsite"
+ "screenCaptureKitMenuItems"
+ "screenCaptureKitPickerPresenterHasActiveStream"
+ "screenCaptureKitiOS"
+ "screenCaptureKitvisionOS"
+ "setBundleID:"
+ "setGlyphPackageState:"
+ "setMenuAffordanceStyle:"
+ "setMicrophoneEnabled:"
+ "setupMenuForScreenCaptureKitPicker:"
+ "shared"
+ "sharedManager"
+ "stopSessionIfActive"
+ "stopStreamForButtonAction"
+ "stopStreamForStreamID:"
+ "streamDidEnd"
+ "streamDidStart"
+ "v32@0:8@\"SCControlCenterManager\"16@\"NSArray\"24"
+ "v32@0:8@\"SCControlCenterManager\"16@\"NSError\"24"
+ "v32@0:8@\"SCControlCenterManager\"16@\"SCContentSharingPickerInfo\"24"
+ "v32@0:8@\"SCControlCenterManager\"16@\"SCStreamInfo\"24"
+ "v48@0:8@\"SCControlCenterManager\"16@\"SCContentSharingPickerInfo\"24@\"SCStreamInfo\"32@\"SCContentFilter\"40"
+ "v48@0:8@\"SCControlCenterManager\"16@\"SCContentSharingPickerInfo\"24@\"SCStreamInfo\"32q40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16@24@32q40"
+ "window"
- " [INFO] %{public}s:%d no change in available extensions"
- "_applicationIconImageForBundleIdentifier:format:scale:"
- "com.apple.mobileslideshow"
- "initWithTitle:identifier:handler:"
- "isEqualToArray:"
- "j8/Omm6s1lsmTDFsXjsBfA"
- "presentCancelReadyToRecord"
- "replaykit-v2"
- "replaykit-v2_IC"
- "scale"

```
