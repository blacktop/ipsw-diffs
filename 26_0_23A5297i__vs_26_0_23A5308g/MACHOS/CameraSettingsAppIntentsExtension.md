## CameraSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension`

```diff

-4093.0.0.122.3
-  __TEXT.__text: 0x6e78
-  __TEXT.__auth_stubs: 0x620
+4096.0.0.0.2
+  __TEXT.__text: 0xa204
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0xe0
   __TEXT.__const: 0x9d4
-  __TEXT.__cstring: 0xf11
-  __TEXT.__constg_swiftt: 0xf8
-  __TEXT.__swift5_typeref: 0x392
-  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__cstring: 0x39d1
+  __TEXT.__constg_swiftt: 0x104
+  __TEXT.__swift5_typeref: 0x3a0
+  __TEXT.__swift5_fieldmd: 0x2c8
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_reflstr: 0x15c
+  __TEXT.__objc_methname: 0x523
+  __TEXT.__swift5_reflstr: 0x487
   __TEXT.__swift5_assocty: 0x118
-  __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x9e
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__auth_ptr: 0x4b8
-  __DATA_CONST.__const: 0x448
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__eh_frame: 0x220
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_ptr: 0x4d0
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x38
-  __DATA.__data: 0x260
+  __DATA.__objc_selrefs: 0x190
+  __DATA.__data: 0x300
   __DATA.__bss: 0x1010
-  __DATA.__common: 0x30
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CameraUI.framework/CameraUI
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
+  - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7FA10733-1D4B-3109-92BF-EF18A3E77884
-  Functions: 191
-  Symbols:   69
-  CStrings:  85
+  UUID: 2A2D6CF8-C4CB-36C9-B17E-D614BA307C94
+  Functions: 197
+  Symbols:   104
+  CStrings:  285
 
Symbols:
+ _CAMUserPreferenceCameraAdjustmentsEnabled
+ _CFPreferencesGetAppBooleanValue
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_iPadCapability
+ _NSGlobalDomain
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PFMediaCapabilities
+ ___CFConstantStringClassReference
+ ___NSArray0__struct
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
CStrings:
+ "#AUTO_MACRO_SWITCH"
+ "#CAM_CAPTURE_DYNAMIC_SHUTTER_SWITCH"
+ "#CAM_SAVE_MESSAGES_ASSETS_PHOTO_LIBRARY_SWITCH"
+ "#CameraGridSwitch"
+ "#CameraLevelSwitch"
+ "#CameraQRBannerSwitch"
+ "#IDC_SWITCH"
+ "#MIRROR"
+ "#OVER_CAPTURE_VIEW_OUTSIDE_THE_FRAME_SWITCH"
+ "#PHOTO_MODE_DEPTH_SWITCH"
+ "#SMUDGE_DETECTION_SWITCH"
+ "#TEXT_ANALYSIS"
+ "#VOLUME_UP_BURST"
+ "/CAMERA_BUTTON_SETTINGS#CAMERA_BUTTON_ADJUSTMENTS_SWITCH"
+ "/CAMERA_BUTTON_SETTINGS#CAMERA_BUTTON_PRESS_AND_HOLD_SWITCH"
+ "/CAMERA_BUTTON_SETTINGS#CAPTURE_BUTTON_REQUIRES_SCREEN_ON"
+ "/CAMERA_BUTTON_SETTINGS/CAMERA_BUTTON_ACCESSIBILITY"
+ "/CAMERA_BUTTON_SETTINGS/CAMERA_BUTTON_CUSTOMIZE_SWITCH"
+ "/CAMERA_BUTTON_SETTINGS/LAUNCH_CAMERA_BUTTON_SETTINGS"
+ "/CameraAudioSettingsList"
+ "/CameraAudioSettingsList#CAM_AUDIO_WIND_REMOVAL"
+ "/CameraAudioSettingsList#CAM_VIDEO_RECORDING_MIX_AUDIO_WITH_OTHERS"
+ "/CameraCinematicSettingsList"
+ "/CameraFocalLengthSettingsList"
+ "/CameraFormatsSettingsList#CameraCaptureGroupSpecifier"
+ "/CameraFormatsSettingsList/CAM_PRO_RES_RESOLUTION"
+ "/CameraFormatsSettingsList/ENHANCED_RESOLUTION"
+ "/CameraFormatsSettingsList/PRO_RES_COLOR_SPACE"
+ "/CameraIndicatorsSettingsList"
+ "/CameraVideoSettingsList#CAM_ACTION_MODE_LOW_LIGHT"
+ "/CameraVideoSettingsList#CAM_ENABLE_VIDEO_STABILIZATION_SWITCH"
+ "/CameraVideoSettingsList#CAM_HDR_VIDEO"
+ "/CameraVideoSettingsList#CAM_PAL_VIDEO_FORMATS"
+ "/CameraVideoSettingsList#CAM_VIDEO_RECORDING_DISABLE_CAMERA_SWITCHING"
+ "/CameraVideoSettingsList#CAM_VIDEO_RECORDING_LOCK_WHITE_BALANCE"
+ "/CameraVideoSettingsList/CAM_AUTO_FPS"
+ "/PHOTOGRAPHIC_STYLES"
+ "/SMART_STYLES"
+ "AUTO_MACRO_SWITCH"
+ "AppleLiveTextEnabled"
+ "CAMERA_ADJUSTMENTS"
+ "CAMERA_ADJUSTMENTS_CUSTOMIZE"
+ "CAMERA_BUTTON_ACCESSIBILITY"
+ "CAM_ACTION_MODE_LOW_LIGHT"
+ "CAM_AUDIO_CONFIGURATION_TITLE"
+ "CAM_AUDIO_WIND_REMOVAL_TITLE"
+ "CAM_AUTO_FPS_TITLE"
+ "CAM_CAPTURE_DYNAMIC_SHUTTER_SWITCH"
+ "CAM_ENABLE_VIDEO_STABILIZATION_SWITCH"
+ "CAM_FORMATS_CAPTURE_TITLE"
+ "CAM_FORMATS_TITLE"
+ "CAM_INDICATORS_TITLE"
+ "CAM_LINEAR_DNG_TITLE"
+ "CAM_PAL_VIDEO_FORMATS_TITLE"
+ "CAM_PRESERVE_SETTINGS_TITLE"
+ "CAM_RECORD_CINEMATIC_TITLE"
+ "CAM_RECORD_SLOMO_TITLE"
+ "CAM_RECORD_VIDEO_TITLE"
+ "CAM_SAVE_MESSAGES_ASSETS_PHOTO_LIBRARY_SWITCH"
+ "CAM_VIDEO_RECORDING_DISABLE_CAMERA_SWITCHING_TITLE"
+ "CAM_VIDEO_RECORDING_LOCK_WHITE_BALANCE_TITLE"
+ "CAM_VIDEO_RECORDING_MIX_AUDIO_WITH_OTHERS_TITLE"
+ "CAPTURE_BUTTON_LAUNCH_APP_TITLE"
+ "CAPTURE_BUTTON_LAUNCH_VISUAL_INTELLIGENCE_TITLE"
+ "CAPTURE_BUTTON_REQUIRES_SCREEN_ON"
+ "CameraSettings-CameraButton"
+ "CameraSettings-SmartStyles"
+ "CameraSettings-SmudgeDetection"
+ "ENHANCED_RESOLUTION_TITLE"
+ "FOCAL_LENGTH_ROW_TITLE"
+ "FOCAL_LENGTH_ROW_TITLE_CAMERA_BUTTON"
+ "FORMATS_SETTINGS_PATH"
+ "MIRROR_FRONT_PHOTOS"
+ "OVER_CAPTURE_VIEW_OUTSIDE_THE_FRAME_SWITCH"
+ "PHOTO_MODE_DEPTH_SWITCH"
+ "PRO_RES_COLOR_SPACE_TITLE"
+ "RECORD_SOUND_SETTINGS_PATH"
+ "RECORD_VIDEO_SETTINGS_PATH"
+ "SEMANTIC_STYLES_ROW_TITLE"
+ "SMUDGE_DETECTION_SWITCH"
+ "The “Action Mode Lower Light” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to configure Action Mode performance in low light conditions."
+ "The “Allow Audio Playback” setting is in the iOS Settings app under the “Camera” > “Record Sound” pane. This setting allows users to enable audio playback mixing during video recording."
+ "The “Auto FPS” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to enable automatic frame rate adjustment based on lighting conditions."
+ "The “Camera Adjustments Customize” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting allows users to customize which camera adjustments are available through Camera Control."
+ "The “Camera Adjustments” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting allows users to enable camera adjustment controls via the Camera Control button."
+ "The “Camera Capture” setting is in the iOS Settings app under the “Camera” > “Formats” pane. This setting allows users to configure the primary capture format and encoding settings for photos and videos."
+ "The “Camera Control Accessibility” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting allows users to configure accessibility options for the Camera Control button."
+ "The “Camera Control Requires Screen On” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting determines whether the screen must be on for Camera Control to function."
+ "The “Camera Control” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure features related to the Camera Control button."
+ "The “Camera” setting is in the iOS Settings app accessible from the top level list. This setting allows users to configure Camera related features."
+ "The “Enhanced Stabilization” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to enable improved video stabilization for smoother recordings."
+ "The “Focal Length” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure how focal length information is displayed and controlled in the camera interface."
+ "The “Formats” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure photo and video capture formats, quality, and encoding options."
+ "The “Grid” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable grid lines in the camera viewfinder for better photo composition."
+ "The “HDR Video” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to enable high dynamic range video recording for better color and contrast."
+ "The “Indicators” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure which camera indicators are displayed during photo and video capture."
+ "The “Launch Camera” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting allows users to configure what camera application the Camera Control button launches."
+ "The “Launch Visual Intelligence” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting allows users to enable Visual Intelligence features through Camera Control press and hold gestures."
+ "The “Lens Cleaning Hints” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable notifications when the camera lens needs cleaning due to smudges or debris."
+ "The “Lens Correction” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable automatic correction of lens distortion in photos."
+ "The “Level” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable the horizon level indicator in the camera to help keep photos straight."
+ "The “Lock Camera” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to prevent automatic camera switching during video recording."
+ "The “Lock Focus and Exposure” setting is in the iOS Settings app under the “Camera” > “Camera Control” pane. This setting allows users to configure focus and exposure locking behavior with Camera Control."
+ "The “Lock White Balance” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to lock white balance settings during video recording for consistent color temperature."
+ "The “Macro Control” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure automatic macro photography switching when subjects are very close."
+ "The “Mirror Front Camera” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to control whether front-facing camera photos and videos are mirrored or shown as captured."
+ "The “Photo Mode” setting is in the iOS Settings app under the “Camera” > “Formats” pane. This setting allows users to configure photo resolution and quality options for standard photo capture."
+ "The “Photographic Styles” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure and customize photographic styles that adjust the look and feel of photos."
+ "The “Portraits in Photo Mode” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable portrait mode suggestions and depth effects in regular photo mode."
+ "The “Preserve Settings” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure which camera settings are preserved between camera sessions."
+ "The “Prioritize Faster Shooting” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable faster camera response times by adjusting capture processing priorities."
+ "The “ProRAW Format” setting is in the iOS Settings app under the “Camera” > “Formats” pane. This setting allows users to configure specific ProRAW format options and resolution settings."
+ "The “ProRAW” setting is in the iOS Settings app under the “Camera” > “Formats” pane. This setting allows users to enable Apple ProRAW format for professional photo editing and processing."
+ "The “ProRes Encoding” setting is in the iOS Settings app under the “Camera” > “Formats” pane. This setting allows users to configure ProRes video encoding options including color space and quality settings."
+ "The “ProRes” setting is in the iOS Settings app under the “Camera” > “Formats” pane. This setting allows users to enable Apple ProRes video recording format for professional video production."
+ "The “Record Cinematic” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure cinematic mode video recording options and formats."
+ "The “Record Slo-mo“ setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure slow motion video recording options and formats."
+ "The “Record Sound” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure audio recording options and quality for video capture."
+ "The “Record Video” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure video recording formats, quality, and frame rate options."
+ "The “Save Captures to Photo Library” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to automatically save photos and videos taken in other apps to the main Photo Library."
+ "The “Scan QR Codes” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable automatic QR code detection and scanning in the camera."
+ "The “Show Detected Text” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable text detection and analysis in camera viewfinder."
+ "The “Show PAL Formats” setting is in the iOS Settings app under the “Camera” > “Record Video” pane. This setting allows users to enable PAL video format options for international compatibility."
+ "The “Smart Styles” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to configure and manage Smart Styles for enhanced photo appearance and editing."
+ "The “Use Volume Up for Burst” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to enable using the volume up button to capture burst photos."
+ "The “View Outside the Frame” setting is in the iOS Settings app under the “Camera” pane. This setting allows users to see content outside the capture frame for better framing and composition."
+ "The “Wind Noise Reduction” setting is in the iOS Settings app under the “Camera” > “Record Sound” pane. This setting allows users to enable wind noise filtering during audio recording."
+ "_deviceLanguage"
+ "ar"
+ "arrayWithObjects:count:"
+ "automatic saving"
+ "automatic switching"
+ "back1080pMaxFPS"
+ "back4kMaxFPS"
+ "back720pMaxFPS"
+ "backHighFrameRate1080pMaxFPS"
+ "backHighFrameRate720pMaxFPS"
+ "boolValue"
+ "capabilities"
+ "cinematic4KSupported"
+ "color temperature"
+ "com.apple.camera"
+ "composition guide"
+ "contentAwareDistortionCorrectionSupported"
+ "continuous shooting"
+ "count"
+ "cs"
+ "da"
+ "de"
+ "en"
+ "es"
+ "focalLengthPickerSupported"
+ "focus transition"
+ "fr"
+ "high dynamic range"
+ "id"
+ "isActionModeControlSupported"
+ "isBackSuperWideSupported"
+ "isBackTelephotoSupported"
+ "isCinematicAudioSupported"
+ "isEnhancedStabilizationSupported"
+ "isHEVCEncodingSupported"
+ "isImageAnalysisSupported"
+ "isLongPressVideoCaptureFromPhotoModeSupported"
+ "isMirroredFrontVideosSupported"
+ "isMixAudioWithOthersSupported"
+ "isPALVideoSupported"
+ "isPhotoResolutionSupported:forPhotoEncoding:"
+ "isProResLogColorSpaceSupported"
+ "isSmudgeDetectionSupported"
+ "isSolCamEnabled"
+ "isSpatialOverCaptureSupported"
+ "isStereoAudioRecordingSupported"
+ "isSuperWideAutoMacroSupported"
+ "isVariableFramerateVideoSupported"
+ "isWhiteBalanceLockingForVideoRecordingSupported"
+ "isWindRemovalSupported"
+ "it"
+ "ja"
+ "ko"
+ "machine learning"
+ "matchedLanguagesFromAvailableLanguages:forPreferredLanguages:"
+ "ms"
+ "multipleCaptureFeaturesSupported"
+ "nb"
+ "newFormatsConfiguration"
+ "nl"
+ "nn"
+ "no"
+ "objectForKey:inDomain:"
+ "photoModeDepthSuggestionSupported"
+ "pl"
+ "professional video"
+ "pt"
+ "responsiveShutterSupported"
+ "ro"
+ "ru"
+ "semanticStylesSupport"
+ "smartStylesSupported"
+ "standardUserDefaults"
+ "sv"
+ "th"
+ "tr"
+ "uk"
+ "vi"
+ "yue-Hans"
+ "yue-Hant"
+ "zh-Hans"
+ "zh-Hant"
- "/CAMERA_BUTTON_SETTINGS#CAMERA_BUTTON_HIDE_CONTROLS_SWITCH"
- "/CAMUserPreferenceMirrorFrontCameraCaptures"
- "/CAMUserPreferenceShowGridOverlay"
- "/CameraLevelSwitch"
- "/CameraQRBannerSwitch"
- "/CameraVideoSettingsList#HDR%20Video"
- "CAMERA_CONTROL_LOCK_FOCUS_TITLE"
- "CAMERA_CONTROL_QUIET_UI_TITLE"
- "CAMERA_SETTINGS_FORMATS"
- "CAMERA_SETTINGS_FORMATS_SYNONYMS"
- "CAMERA_SETTINGS_HDR_VIDEO_PATH"
- "CAMERA_SETTINGS_HDR_VIDEO_SYNONYMS"
- "CAMERA_SETTINGS_PATH"
- "CAMERA_SETTINGS_PRESERVE_SETTINGS"
- "CAMERA_SETTINGS_PRESERVE_SYNONYMS"
- "CAMERA_SETTINGS_PRO_RAW_PATH"
- "CAMERA_SETTINGS_PRO_RAW_SYNONYMS"
- "CAMERA_SETTINGS_PRO_RES_PATH"
- "CAMERA_SETTINGS_RECORD_SLO_MO"
- "CAMERA_SETTINGS_RECORD_VIDEO"
- "Camera HDR video setting for toggling HDR video under the Record Video settings pane for Camera settings"
- "Camera ProRAW setting for toggling ProRAW under the Formats settings pane for Camera settings"
- "Camera configuration"
- "Camera formats settings pane for settings such as camera capture high efficiency or video capture Apple ProRes"
- "Camera preserve settings pane for settings such as preserving camera mode or night mode"
- "Camera record slo-mo settings pane for settings such as 1080p HD at 120 fps"
- "Camera record video settings pane for settings such as HDR Video or Auto FPS"
- "Grid control under root pane of Camera settings.  This setting controls if a grid shows on the viewfinder when taking a photo."
- "Level control under root pane of Camera settings.  This setting controls if a level shows when taking a photo."
- "Mirror front camera control under root pane of Camera settings.  This setting controls if a photo taken with the front camera is a mirror image of the original taken."
- "Root settings pane of camera"
- "Scan QR codes control under root pane of Camera settings.  This setting controls whether a user scans QR codes when using the camera."
- "Show Camera Control setting for enabling AE/AF Lock"
- "Show Camera Control setting for enabling Clean Preview"
- "Show Camera control for ProRes. ProRes is one of the most popular formats for video professional post-production."
- "Show settings for configuring Camera Control"
- "Video recording FPS settings"
- "Video slo-mo settings"
- "Video slow motion settings"
- "Video slow-mo settings"

```
