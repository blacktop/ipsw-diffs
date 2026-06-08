## ClarityUICameraSettings

> `/System/Library/PreferenceBundles/ClarityUICameraSettings.bundle/ClarityUICameraSettings`

```diff

-1817.19.0.0.0
-  __TEXT.__text: 0x3e0
+1847.0.0.0.0
+  __TEXT.__text: 0x3ac
   __TEXT.__auth_stubs: 0x60
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x80

   __TEXT.__objc_methname: 0x210
   __TEXT.__objc_methtype: 0x29
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x38
-  __DATA_CONST.__got: 0x18
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x38
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0xb8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ShazamKit.framework/ShazamKit
+  - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
+  - /System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI
+  - /System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices
+  - /System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction
+  - /System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport
   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/AdCore.framework/AdCore
+  - /System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI
+  - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief
+  - /System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI
+  - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
+  - /System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings
+  - /System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl
+  - /System/Library/PrivateFrameworks/SystemVoiceAssistantServices.framework/SystemVoiceAssistantServices
+  - /System/Library/PrivateFrameworks/TouchAccommodations.framework/TouchAccommodations
+  - /System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI
+  - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
+  - /System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices
+  - /System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices
+  - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A34DB41A-B67C-38D3-806B-D895777A61A8
+  UUID: 84F0EDB0-0B65-3EB1-90B6-D3E2361BFABE
   Functions: 10
-  Symbols:   18
+  Symbols:   43
   CStrings:  30
 
Symbols:
+ -[CLCameraController isCapturePhotosEnabled:]
+ -[CLCameraController isCaptureSelfieEnabled:]
+ -[CLCameraController isCaptureSelfieVideoEnabled:]
+ -[CLCameraController isCaptureVideosEnabled:]
+ -[CLCameraController setCapturePhotosEnabled:specifier:]
+ -[CLCameraController setCaptureSelfieEnabled:specifier:]
+ -[CLCameraController setCaptureSelfieVideoEnabled:specifier:]
+ -[CLCameraController setCaptureVideosEnabled:specifier:]
+ -[CLCameraController specifiers]
+ -[CLCameraController tableViewStyle]
+ __OBJC_$_INSTANCE_METHODS_CLCameraController
+ __OBJC_CLASS_RO_$_CLCameraController
+ __OBJC_METACLASS_RO_$_CLCameraController
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$allowPhotoCapture
+ _objc_msgSend$allowSelfieCapture
+ _objc_msgSend$allowSelfieVideoCapture
+ _objc_msgSend$allowVideoCapture
+ _objc_msgSend$boolValue
+ _objc_msgSend$copy
+ _objc_msgSend$loadSpecifiersFromPlistName:target:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$setAllowPhotoCapture:
+ _objc_msgSend$setAllowSelfieCapture:
+ _objc_msgSend$setAllowSelfieVideoCapture:
+ _objc_msgSend$setAllowVideoCapture:
+ _objc_msgSend$sharedInstance
+ _objc_retainAutoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- radr://5614542

```
