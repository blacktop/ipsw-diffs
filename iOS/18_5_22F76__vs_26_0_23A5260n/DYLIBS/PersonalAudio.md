## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-456.8.10.0.0
-  __TEXT.__text: 0x14d58
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0xca0
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__cstring: 0x221f
+485.3.0.0.0
+  __TEXT.__text: 0x1668c
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0xd88
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x48c
+  __TEXT.__cstring: 0x23fa
   __TEXT.__oslogstring: 0x246
-  __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__dlopen_cstrs: 0x1c1
+  __TEXT.__unwind_info: 0x570
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x2c02
-  __TEXT.__objc_methtype: 0x3cc
-  __TEXT.__objc_stubs: 0x2ba0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x828
+  __TEXT.__objc_methname: 0x2f19
+  __TEXT.__objc_methtype: 0x40b
+  __TEXT.__objc_stubs: 0x2d60
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x930
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd60
+  __DATA_CONST.__objc_selrefs: 0xe10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x1e20
-  __AUTH_CONST.__objc_const: 0xf28
+  __AUTH_CONST.__cfstring: 0x1f00
+  __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xb8
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 61BD4423-F74A-3B4F-9D7A-3F4A3FDE0E1A
-  Functions: 411
-  Symbols:   1582
-  CStrings:  1158
+  UUID: 4E99BD86-F7CF-326A-86F5-DEF680360EED
+  Functions: 439
+  Symbols:   1668
+  CStrings:  1201
 
Symbols:
+ -[PAConfiguration transparencySettingsv4ForAddress:]
+ -[PAEnrollment currentDevicePSEVersion]
+ -[PAEnrollment headphoneStateChangedNotification:]
+ -[PAEnrollment mediaServerDied]
+ -[PAEnrollment registerNotifications]
+ -[PAEnrollment setCurrentDevicePSEVersion:]
+ -[PAEnrollment updateHeadphoneState]
+ -[PAHMSManager ownVoiceForAddress:]
+ -[PAHMSManager ownVoiceSupportedForAddress:]
+ -[PAHMSManager setOwnVoice:forAddress:]
+ -[PASettings resetValueForSelector:forAddress:]
+ -[PASettings setTransparencyAutobeamformer:]
+ -[PASettings setTransparencyAutobeamformer:forAddress:]
+ -[PASettings setTransparencyOwnVoice:]
+ -[PASettings setTransparencyOwnVoice:forAddress:]
+ -[PASettings transparencyAutobeamformerForAddress:]
+ -[PASettings transparencyAutobeamformer]
+ -[PASettings transparencyOwnVoiceForAddress:]
+ -[PASettings transparencyOwnVoice]
+ GCC_except_table10
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table5
+ _AVAudioSessionRouteChangeNotification
+ _AVSystemController_ActiveAudioRouteDidChangeNotification
+ _AVSystemController_HeadphoneJackIsConnectedDidChangeNotification
+ _AVSystemController_ServerConnectionDiedNotification
+ _AVSystemController_SubscribeToNotificationsAttribute
+ _AXPerformBlockOnMainThreadAfterDelay
+ _OBJC_CLASS_$_AVSystemController
+ _OBJC_IVAR_$_PAEnrollment._currentDevicePSEVersion
+ ___20-[PAEnrollment init]_block_invoke
+ ___26-[PAAccessoryManager init]_block_invoke.40
+ ___26-[PAAccessoryManager init]_block_invoke_2.51
+ ___36-[PAEnrollment updateHeadphoneState]_block_invoke
+ ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_3
+ ___43-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_4
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.91
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.95
+ ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke.99
+ ___73+[PAAudiogramUtilities normalizedOffsetsFromLeftOffsets:andRightOffsets:]_block_invoke.117
+ ___block_descriptor_40_e8_32s_e44_v44?0"NSDictionary"8Q16"NSString"24B32Q36ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_50_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e8_v16?0Q8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e8_v16?0Q8ls32l8s40l8s48l8
+ ___block_literal_global.102
+ ___block_literal_global.108
+ ___block_literal_global.121
+ ___block_literal_global.175
+ ___block_literal_global.54
+ ___block_literal_global.87
+ _objc_msgSend$currentDevicePSEVersion
+ _objc_msgSend$getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:
+ _objc_msgSend$getPMEEverywhereSupportStateForAddress:withCompletion:
+ _objc_msgSend$getPSEVersionForAddress:withCompletion:
+ _objc_msgSend$headphoneStateChangedNotification:
+ _objc_msgSend$performSelector:withObject:afterDelay:
+ _objc_msgSend$preferenceKeyForSelector:
+ _objc_msgSend$registerNotifications
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$setAttribute:forKey:error:
+ _objc_msgSend$setCurrentDevicePSEVersion:
+ _objc_msgSend$setTransparencyAutobeamformer:
+ _objc_msgSend$setTransparencyOwnVoice:
+ _objc_msgSend$setTransparencyOwnVoice:forAddress:
+ _objc_msgSend$sharedAVSystemController
+ _objc_msgSend$transparencyAutobeamformer
+ _objc_msgSend$transparencyOwnVoice
+ _objc_msgSend$transparencyOwnVoiceForAddress:
+ _objc_msgSend$transparencySettingsv4ForAddress:
+ _objc_msgSend$updateHeadphoneState
+ _paSupportedWiredRoutes
+ _paSupportedWiredRoutes.AudioRouteSubtypes
+ _paSupportedWirelessRoutes
+ _paSupportedWirelessRoutes.AudioRouteProductIDs
- GCC_except_table20
- GCC_except_table23
- GCC_except_table43
- GCC_except_table44
- GCC_except_table46
- GCC_except_table47
- GCC_except_table6
- ___26-[PAAccessoryManager init]_block_invoke_2.50
- ___53-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_4
- ___73+[PAAudiogramUtilities normalizedOffsetsFromLeftOffsets:andRightOffsets:]_block_invoke.168
- ___block_descriptor_58_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
- ___block_literal_global.105
- ___block_literal_global.172
- ___block_literal_global.174
- ___block_literal_global.53
- ___block_literal_global.82
- ___block_literal_global.85
- _objc_msgSend$deviceFromAddressString:
- _objc_msgSend$getAACPCapabilityBit:
- _objc_msgSend$getSSLMode
- _objc_msgSend$setSSLMode:
- _objc_msgSend$setSslEnabled:
- _objc_msgSend$sslEnabled
- _paProductsIdentifiersSupportingAudioAccommodations
- _paProductsIdentifiersSupportingAudioAccommodations.AudioRouteProductIDs
- _paRouteSubtypesSupportingAudioAccommodations
- _paRouteSubtypesSupportingAudioAccommodations.AudioRouteSubtypes
CStrings:
+ "-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_3"
+ "-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_4"
+ "-[PAConfiguration transparencySettingsv4ForAddress:]"
+ "Found PME supported %@"
+ "Found route %@ - %@"
+ "Sending enabled %lf, %lf, %lf, left: {%lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf}, right: {%lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf}"
+ "Skipping custom transparency update because buds are owned by another device %@"
+ "Skipping update because pending timer"
+ "Starting processing"
+ "TQ,N,V_currentDevicePSEVersion"
+ "^{?=f{?=ffffffffffff}{?=ffffffffffff}f}24@0:8@16"
+ "_currentDevicePSEVersion"
+ "currentDevicePSEVersion"
+ "getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:"
+ "getPMEEverywhereSupportStateForAddress:withCompletion:"
+ "getPSEVersionForAddress:withCompletion:"
+ "headphoneStateChangedNotification:"
+ "mediaServerDied"
+ "ownVoiceForAddress:"
+ "ownVoiceSupportedForAddress:"
+ "performSelector:withObject:afterDelay:"
+ "registerNotifications"
+ "removeObserver:"
+ "resetValueForSelector:forAddress:"
+ "setAttribute:forKey:error:"
+ "setCurrentDevicePSEVersion:"
+ "setOwnVoice:forAddress:"
+ "setTransparencyAutobeamformer:"
+ "setTransparencyAutobeamformer:forAddress:"
+ "setTransparencyOwnVoice:"
+ "setTransparencyOwnVoice:forAddress:"
+ "sharedAVSystemController"
+ "transparencyAutobeamformer"
+ "transparencyAutobeamformerForAddress:"
+ "transparencyOwnVoice"
+ "transparencyOwnVoiceForAddress:"
+ "transparencySettingsv4ForAddress:"
+ "updateHeadphoneState"
+ "v16@?0Q8"
+ "v32@0:8:16@24"
+ "v44@?0@\"NSDictionary\"8Q16@\"NSString\"24B32Q36"
- "-[PAAccessoryManager sendPMEConfigurationToAccessory]_block_invoke_4"
- "-[PAAccessoryManager sendUpdateToAccessory]_block_invoke_2"
- "Checking Yodel %d = %@"
- "deviceFromAddressString:"
- "getAACPCapabilityBit:"
- "getSSLMode"
- "setSSLMode:"

```
