## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3401.10.1.1.1
-  __TEXT.__text: 0x36a1e0
+3401.15.2.1.2
+  __TEXT.__text: 0x36a9dc
   __TEXT.__auth_stubs: 0x3450
-  __TEXT.__objc_stubs: 0x44fa0
-  __TEXT.__objc_methlist: 0x1d364
+  __TEXT.__objc_stubs: 0x450e0
+  __TEXT.__objc_methlist: 0x1d394
   __TEXT.__const: 0x10998
-  __TEXT.__gcc_except_tab: 0x480c
-  __TEXT.__cstring: 0x51024
-  __TEXT.__oslogstring: 0x3e328
+  __TEXT.__gcc_except_tab: 0x4828
+  __TEXT.__cstring: 0x51140
+  __TEXT.__oslogstring: 0x3e367
   __TEXT.__objc_classname: 0x51b3
-  __TEXT.__objc_methname: 0x5cf59
+  __TEXT.__objc_methname: 0x5d07a
   __TEXT.__objc_methtype: 0xee2f
-  __TEXT.__dlopen_cstrs: 0x9ce
+  __TEXT.__dlopen_cstrs: 0xa2c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa3a0
+  __TEXT.__unwind_info: 0xa3c8
   __TEXT.__eh_frame: 0xe70
   __DATA_CONST.__auth_got: 0x1a38
-  __DATA_CONST.__got: 0x3af8
+  __DATA_CONST.__got: 0x3b10
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x15030
-  __DATA_CONST.__cfstring: 0x12500
+  __DATA_CONST.__const: 0x15048
+  __DATA_CONST.__cfstring: 0x12520
   __DATA_CONST.__objc_classlist: 0xd28
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6d8

   __DATA_CONST.__objc_superrefs: 0xaf8
   __DATA_CONST.__objc_arraydata: 0x3b8
   __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA_CONST.__objc_intobj: 0x810
+  __DATA_CONST.__objc_intobj: 0x828
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x3d018
-  __DATA.__objc_selrefs: 0x13cb8
-  __DATA.__objc_ivar: 0x25ec
+  __DATA.__objc_const: 0x3cff8
+  __DATA.__objc_selrefs: 0x13d10
+  __DATA.__objc_ivar: 0x25e8
   __DATA.__objc_data: 0x8390
   __DATA.__data: 0x6048
-  __DATA.__bss: 0xe38
+  __DATA.__bss: 0xe48
   __DATA.__common: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14399
-  Symbols:   2877
-  CStrings:  26967
+  Functions: 14407
+  Symbols:   2880
+  CStrings:  26983
 
Symbols:
+ _OBJC_CLASS_$_CSFGMOptIn
+ _AFHasGMSCapabilityUnembargoed
+ _OBJC_CLASS_$_AFSystemAssistantExperienceStatusManager
+ _kAFMAStartupActivatedNotification
- _AFDeviceSupportsSystemAssistantExperience
CStrings:
+ "-[ADDeviceResolutionServiceListener getSourceDeviceForContextWithIdentifiers:completion:]_block_invoke"
+ "-[ADExternalNotificationRequestHandler audioSessionDidEnd]"
+ "setIsDeviceShowingLockScreen:"
+ "setIsAppleIntelligenceAvailable:"
+ "isSAEEnabled"
+ "MobileAssistantDaemons-3401.15.2.1.2"
+ "_getIsAppleIntelligenceHardwareCapable"
+ "setIsDeviceLocked:"
+ "-[ADAssistantProperties _getIsAppleIntelligenceHardwareCapable]"
+ "shouldBeShownInSettingsReturningAvailabilityStatus:"
+ "isDeviceShowingLockScreen"
+ "ADAssistantProperties.m"
+ "-[ADAssistantProperties _getIsAppleIntelligenceAvailable]"
+ "-[ADAssistantProperties _getIsAppleIntelligenceEnabled]"
+ "audioSessionDidEnd"
+ "setIsAppleIntelligenceHardwareCapable:"
+ "_getIsAppleIntelligenceAvailable"
+ "isOptedIn"
+ "%!s(MISSING) #ODD: %!d(MISSING)"
+ "%!s(MISSING) Override proximity for local device to be primary"
+ "%!s(MISSING) #ODD: isAvailableInSettings=%!d(MISSING) isSAEEnabled=%!d(MISSING)"
- "_sessionWasAnnouncement"
- "-[ADExternalNotificationRequestHandler notifyObserver:didChangeStateFrom:to:]"
- "2"
- "%!s(MISSING) notifyObserver didChangeStateFrom: %!l(MISSING)lu to: %!l(MISSING)lu"
- "MobileAssistantDaemons-3401.10.1.1.1"

```
