## CameraSettings

> `/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings`

```diff

-4026.120.2.0.0
-  __TEXT.__text: 0x11060
+4082.0.0.122.5
+  __TEXT.__text: 0x12b78
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x2b80
-  __TEXT.__objc_methlist: 0xb24
-  __TEXT.__cstring: 0x37e9
-  __TEXT.__objc_methname: 0x320e
-  __TEXT.__objc_classname: 0x27c
-  __TEXT.__objc_methtype: 0x325
+  __TEXT.__objc_stubs: 0x2d80
+  __TEXT.__objc_methlist: 0xca4
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__cstring: 0x3a4c
+  __TEXT.__objc_methname: 0x36dd
+  __TEXT.__objc_classname: 0x2a2
+  __TEXT.__objc_methtype: 0x3c4
   __TEXT.__oslogstring: 0x218
-  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__unwind_info: 0x470
   __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x3d8
-  __DATA_CONST.__cfstring: 0x3dc0
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__cfstring: 0x40a0
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_arraydata: 0x330
+  __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_intobj: 0x2e8
-  __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA.__objc_const: 0xf00
-  __DATA.__objc_selrefs: 0xd78
-  __DATA.__objc_ivar: 0x38
-  __DATA.__objc_data: 0x550
+  __DATA.__objc_const: 0x1000
+  __DATA.__objc_selrefs: 0xe60
+  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_data: 0x5a0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FEABF4B-4CE0-37CC-AE87-48666ADD211A
-  Functions: 270
-  Symbols:   242
-  CStrings:  1536
+  UUID: EBD1C0F0-BE1C-3C8A-AB39-7D23B024801A
+  Functions: 311
+  Symbols:   255
+  CStrings:  1622
 
Symbols:
+ _CAMButtonControlCamerasKey
+ _CAMButtonControlDepthKey
+ _CAMButtonControlExposureKey
+ _CAMButtonControlStylesKey
+ _CAMButtonControlToneKey
+ _CAMButtonControlZoomKey
+ _CAMUserPreferenceAlwaysShowActionModeIndicator
+ _CAMUserPreferenceAlwaysShowActionModeIndicatorDefaultValue
+ _CAMUserPreferenceAlwaysShowFlashIndicator
+ _CAMUserPreferenceAlwaysShowFlashIndicatorDefaultValue
+ _CAMUserPreferenceAlwaysShowLivePhotoIndicator
+ _CAMUserPreferenceAlwaysShowLivePhotoIndicatorDefaultValue
+ _CAMUserPreferenceAlwaysShowVideoFormatsIndicator
+ _CAMUserPreferenceAlwaysShowVideoFormatsIndicatorDefaultValue
+ _CAMUserPreferenceCameraAdjustmentsEnabled
+ _CAMUserPreferenceOverlayControlsOrder
+ _CAMUserPreferenceOverlayEnabledControls
+ _MGGetSInt32Answer
+ _OBJC_CLASS_$_CameraAdjustmentsSettingsController
+ _OBJC_CLASS_$_CameraIndicatorSettingsController
+ _OBJC_CLASS_$_NSIndexPath
+ _OBJC_METACLASS_$_CameraAdjustmentsSettingsController
+ _OBJC_METACLASS_$_CameraIndicatorSettingsController
- _CAMUserPreferenceEnableSpatialVideoCaptureControl
- _CAMUserPreferencePreserveSpatialVideoEnabled
- _CameraSettingsDetailTableCellTextKey
- _OBJC_CLASS_$_CameraSettingsDetailedTableCell
- _OBJC_CLASS_$_PSTableCell
- _OBJC_METACLASS_$_CameraSettingsDetailedTableCell
- _OBJC_METACLASS_$_PSTableCell
- _PSCellClassKey
- __os_feature_enabled_impl
- _kCameraCaptureGroupSpecifierID
CStrings:
+ "%@\n\n%@"
+ "@\"NSDictionary\""
+ "@40@0:8@16@24@32"
+ "@44@0:8@16@24@32B40"
+ "B32@0:8@16@24"
+ "CAMERA_ADJUSTMENTS"
+ "CAMERA_ADJUSTMENTS_FOOTER"
+ "CAMERA_ADJUSTMENTS_GESTURE_LIGHT_PRESS"
+ "CAMERA_ADJUSTMENTS_GESTURE_SWIPE"
+ "CAMERA_ADJUSTMENTS_GESTURE_TITLE"
+ "CAMERA_OPTION_DISABLED"
+ "CAMERA_OPTION_ENABLED"
+ "CAMOverlayControlSelected"
+ "CAMOverlayControlsGroupSpecifier"
+ "CAMUserPreferenceEnableSmudgeNotifications"
+ "CAMUserPreferencesSaveMessagesCapturesPhotoLibrary"
+ "CAM_INDICATORS_ACTION_MODE"
+ "CAM_INDICATORS_FLASH"
+ "CAM_INDICATORS_FOOTER_IPHONE"
+ "CAM_INDICATORS_LIVE_PHOTO"
+ "CAM_INDICATORS_PHOTO_TITLE"
+ "CAM_INDICATORS_TITLE"
+ "CAM_INDICATORS_VIDEO_FORMATS"
+ "CAM_INDICATORS_VIDEO_FORMATS_FOOTER"
+ "CAM_INDICATORS_VIDEO_TITLE"
+ "CAM_PRESERVE_CREATIVE_CONTROLS_SWITCH"
+ "CAM_PRESERVE_PHOTO_ASPECT_FOOTER"
+ "CAM_PRESERVE_PHOTO_FILTER_ASPECT_FOOTER"
+ "CAM_PRESERVE_PHOTO_LIGHTING_ASPECT_FOOTER"
+ "CAM_SAVE_MESSAGES_ASSETS_PHOTO_LIBRARY_FOOTER"
+ "CAM_SAVE_MESSAGES_ASSETS_PHOTO_LIBRARY_SWITCH"
+ "CAM_SAVE_MESSAGES_ASSETS_PHOTO_LIBRARY_TITLE"
+ "CAPTURE_BUTTON_CONTROLS_TITLE"
+ "CAPTURE_BUTTON_CONTROL_CAMERAS"
+ "CAPTURE_BUTTON_CONTROL_DEPTH"
+ "CAPTURE_BUTTON_CONTROL_EXPOSURE"
+ "CAPTURE_BUTTON_CONTROL_STYLES"
+ "CAPTURE_BUTTON_CONTROL_TONE"
+ "CAPTURE_BUTTON_CONTROL_ZOOM"
+ "CameraAdjustmentsMasterSwitch"
+ "CameraAdjustmentsSettingsController"
+ "CameraIndicatorSettingsController"
+ "CameraSettings-SmudgeDetection"
+ "DeviceClassNumber"
+ "SMUDGE_DETECTION_FOOTER"
+ "SMUDGE_DETECTION_SWITCH"
+ "SMUDGE_DETECTION_TITLE"
+ "T@\"NSDictionary\",&,N,V__availableOverlayControlLocalizationStrings"
+ "T{_NSRange=QQ},N,V__availableControlsSpecifiersRange"
+ "__availableControlsSpecifiersRange"
+ "__availableOverlayControlLocalizationStrings"
+ "_addPhotoSpecifiers:"
+ "_addVideoSpecifiers:"
+ "_availableControlsSpecifiersRange"
+ "_availableOverlayControlLocalizationStrings"
+ "_availableOverlayControlSpecifiers"
+ "_cameraAdjustmentsEnablementString:"
+ "_currentSmartStyleName:"
+ "_initializeOverlayControlLocalizationDictionary"
+ "_isIPad"
+ "_isSaveAssetsPhotoLibraryEnabled:"
+ "_isSmudgeDetectionEnabled:"
+ "_overlayControlsSectionIncludesRowAtIndexPath:"
+ "_saveCameraButtonControlSelection"
+ "_setCameraAdjustmentsEnabled:specifier:"
+ "_setSaveAssetsPhotoLibraryEnabled:specifier:"
+ "_setSmudgeDetectionEnabled:specifier:"
+ "cleanPreviewGroup"
+ "currentWithUseCaseIdentifiers:language:"
+ "groupSpecifierWithTitle:footer:identifier:"
+ "indexPathForRow:inSection:"
+ "isLiveFilteringSupported"
+ "isNightModeSupported"
+ "isSmudgeDetectionSupported"
+ "isSolCamEnabled"
+ "mutableCopy"
+ "numberOfRowsInSection:"
+ "objectForKey:"
+ "reloadSpecifierID:"
+ "setAccessoryType:"
+ "setShowsReorderControl:"
+ "set_availableControlsSpecifiersRange:"
+ "set_availableOverlayControlLocalizationStrings:"
+ "switchSpecifierWithLabel:key:defaultValue:"
+ "switchSpecifierWithLabel:key:domain:defaultValue:"
+ "systemOverlay.halfPressGestureEnabled"
+ "systemOverlay.swipeToPresentEnabled"
+ "tableView:canMoveRowAtIndexPath:"
+ "tableView:moveRowAtIndexPath:toIndexPath:"
+ "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
+ "tableView:willDisplayCell:forRowAtIndexPath:"
+ "v32@0:8{_NSRange=QQ}16"
+ "v40@0:8@16@24@32"
+ "zoomFactorForCustomLensZoomFactor:"
+ "{_NSRange=\"location\"Q\"length\"Q}"
+ "{_NSRange=QQ}16@0:8"
- "CAM_PRESERVE_CAMERA_MODE_FOOTER"
- "CAM_PRESERVE_LIGHTING_ASPECT_FOOTER"
- "CAM_PRESERVE_LIGHTING_ASPECT_SWITCH"
- "CAM_PRESERVE_PHOTO_FILTER_FOOTER"
- "CAM_PRESERVE_PHOTO_FILTER_LIGHTING_APERTURE_SWITCH"
- "CAM_PRESERVE_PHOTO_FILTER_LIGHTING_FOOTER"
- "CAM_PRESERVE_PHOTO_FILTER_LIGHTING_SWITCH"
- "CAM_PRESERVE_PHOTO_FILTER_SWITCH"
- "CAM_PRESERVE_SPATIAL_VIDEO_ENABLED_FOOTER"
- "CAM_PRESERVE_SPATIAL_VIDEO_ENABLED_SWITCH"
- "CAPTURE_BUTTON_LIGHT_PRESS_TITLE"
- "CameraCaptureButtonGroupSpecifier"
- "CameraSettings-48MP-UltraWide"
- "CameraSettings-4k120"
- "CameraSettings-JpegXL"
- "CameraSettings-SpatialVideoCapture"
- "CameraSettingsDetailTableCellTextKey"
- "CameraSettingsDetailedTableCell"
- "SPATIAL_VIDEO_CAPTURE_FOOTER"
- "SPATIAL_VIDEO_CAPTURE_SWITCH_LABEL"
- "TextRecognition"
- "arrayByAddingObjectsFromArray:"
- "cleanPreview"
- "currentWithUseCaseIdentifiers:"
- "detailTextLabel"
- "extended_latin"
- "isLowLightSupported"
- "isSpatialVideoCaptureSupported"
- "refreshCellContentsWithSpecifier:"
- "setNeedsLayout"
- "setText:"
- "spatialVideoGroup"
- "tableView:cellForRowAtIndexPath:"

```
