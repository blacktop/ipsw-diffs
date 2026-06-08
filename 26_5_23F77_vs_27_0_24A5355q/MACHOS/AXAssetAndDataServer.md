## AXAssetAndDataServer

> `/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x4a0c
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__oslogstring: 0x397
-  __TEXT.__cstring: 0x843
-  __TEXT.__objc_classname: 0x82
-  __TEXT.__objc_methtype: 0xe43
+3229.1.6.0.0
+  __TEXT.__text: 0x4f04
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x7cc
   __TEXT.__dlopen_cstrs: 0x127
-  __TEXT.__objc_methname: 0x23ce
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x198
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x26c
+  __TEXT.__cstring: 0x8f6
+  __TEXT.__oslogstring: 0x3d3
+  __TEXT.__objc_classname: 0x7c
+  __TEXT.__objc_methname: 0x2475
+  __TEXT.__objc_methtype: 0xe43
+  __TEXT.__unwind_info: 0x168
   __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__cfstring: 0x820
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x728
-  __DATA.__objc_selrefs: 0x7d8
-  __DATA.__objc_ivar: 0x20
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x1b8
+  __DATA.__objc_const: 0x720
+  __DATA.__objc_selrefs: 0x7f8
+  __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x68

   - /System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
+  - /System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection
   - /System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 432E8C22-24CC-3CEB-838E-D80870A0D905
-  Functions: 73
-  Symbols:   145
-  CStrings:  541
+  UUID: E9B6078B-A95A-3EDF-A46A-CC492E96AA93
+  Functions: 55
+  Symbols:   153
+  CStrings:  555
 
Symbols:
+ _AXTeachableFeatureAccessibilityReader
+ _AXTeachableFeatureHearingDevices
+ _AXTeachableFeatureTouchAccommodations
+ _AXTeachableFeatureVoiceOverRecognition
+ _OBJC_CLASS_$_AXSDSettings
+ __os_feature_enabled_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x28
+ _objc_retain_x8
- _NSKeyedArchiveRootObjectKey
- _objc_autorelease
- _objc_retain_x27
CStrings:
+ "Accessibility"
+ "HEARING_AID_TITLE"
+ "SPEECH_TITLE/AccessibilityReader"
+ "TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS"
+ "TeachableMoment: Notifications are disabled by feature flag"
+ "TeachableMomentsNotifications"
+ "VOICEOVER_TITLE/NeuralVoiceOver"
+ "accessibilityReaderEnabled"
+ "assistantConnection:speechRecordingPerformBackChannelPromptWithType:completion:"
+ "assistantConnectionDidInterrupt:"
+ "assistantConnectionDidInvalidate:"
+ "isNameRecognitionEnabled"
+ "soundDetectionEnabled"
+ "touchAccommodationsEnabled"
+ "unarchivedObjectOfClasses:fromData:error:"
- "_lastTTSVoiceAssetUpdate"
- "arrayWithObjects:count:"
- "decodeObjectOfClasses:forKey:"
- "initForReadingFromData:error:"
- "setWithArray:"

```
