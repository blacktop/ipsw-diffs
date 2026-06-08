## ClarityUITVSettings

> `/System/Library/PreferenceBundles/ClarityUITVSettings.bundle/ClarityUITVSettings`

```diff

-1817.19.0.0.0
-  __TEXT.__text: 0x57c
-  __TEXT.__auth_stubs: 0x120
+1847.0.0.0.0
+  __TEXT.__text: 0x4fc
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__objc_methname: 0x263
-  __TEXT.__cstring: 0x89
-  __TEXT.__objc_classname: 0x11
+  __TEXT.__cstring: 0x8b
+  __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methtype: 0x52
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x98
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0xf0
   __DATA.__objc_selrefs: 0xd0
   __DATA.__objc_ivar: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ShazamKit.framework/ShazamKit
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
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
   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE184AD1-9058-39D7-AEA1-5956DE27E0BA
+  UUID: 97CB8586-6359-36D7-94D1-830CE45F50C8
   Functions: 11
-  Symbols:   33
+  Symbols:   66
   CStrings:  54
 
Symbols:
+ -[CLTVController .cxx_destruct]
+ -[CLTVController _mediaSpecifiers]
+ -[CLTVController _openTVApp:]
+ -[CLTVController init]
+ -[CLTVController privacyAppBundleIdentifier]
+ -[CLTVController setViewLibrarySpecifier:]
+ -[CLTVController specifiers]
+ -[CLTVController tableView:cellForRowAtIndexPath:]
+ -[CLTVController tableViewStyle]
+ -[CLTVController viewDidLoad]
+ -[CLTVController viewLibrarySpecifier]
+ OBJC_IVAR_$_CLTVController._mediaEntries
+ OBJC_IVAR_$_CLTVController._viewLibrarySpecifier
+ __OBJC_$_INSTANCE_METHODS_CLTVController
+ __OBJC_$_INSTANCE_VARIABLES_CLTVController
+ __OBJC_$_PROP_LIST_CLTVController
+ __OBJC_CLASS_RO_$_CLTVController
+ __OBJC_METACLASS_RO_$_CLTVController
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_mediaSpecifiers
+ _objc_msgSend$addObject:
+ _objc_msgSend$array
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$groupSpecifierWithName:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$loadSpecifiersFromPlistName:target:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$navigationItem
+ _objc_msgSend$openURL:withOptions:
+ _objc_msgSend$preferenceSpecifierNamed:target:set:get:detail:cell:edit:
+ _objc_msgSend$setButtonAction:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setViewLibrarySpecifier:
+ _objc_msgSend$specifiersWithPrivacyLinkSupport:
+ _objc_msgSend$viewLibrarySpecifier
+ _objc_retainAutoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- radr://5614542
Functions:
~ sub_c98 -> -[CLTVController viewDidLoad] : 292 -> 272
~ sub_dbc -> -[CLTVController specifiers] : 168 -> 160
~ sub_e64 -> -[CLTVController _mediaSpecifiers] : 476 -> 440
~ sub_1040 -> -[CLTVController _openTVApp:] : 124 -> 120
~ sub_10c4 -> -[CLTVController tableView:cellForRowAtIndexPath:] : 80 -> 76
~ sub_1120 -> -[CLTVController viewLibrarySpecifier] : 16 -> 20
~ sub_1130 -> -[CLTVController setViewLibrarySpecifier:] : 80 -> 20

```
