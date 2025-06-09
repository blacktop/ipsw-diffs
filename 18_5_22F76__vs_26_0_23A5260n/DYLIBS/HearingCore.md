## HearingCore

> `/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore`

```diff

-456.8.10.0.0
-  __TEXT.__text: 0x703c
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x758
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xc20
-  __TEXT.__oslogstring: 0x186
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x2d8
+485.3.0.0.0
+  __TEXT.__text: 0x79d0
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x7b8
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xd24
+  __TEXT.__oslogstring: 0x1e9
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__unwind_info: 0x308
   __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x1659
-  __TEXT.__objc_methtype: 0x2e1
-  __TEXT.__objc_stubs: 0x1460
+  __TEXT.__objc_methname: 0x17c5
+  __TEXT.__objc_methtype: 0x2f3
+  __TEXT.__objc_stubs: 0x1560
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x388
+  __DATA_CONST.__const: 0x3b8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x720
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3c8
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xc80
-  __AUTH_CONST.__objc_const: 0x958
+  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__cfstring: 0xda0
+  __AUTH_CONST.__objc_const: 0x988
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__common: 0x10
-  __DATA.__bss: 0xb1
+  __DATA.__bss: 0x141
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__common: 0x40
-  __DATA_DIRTY.__bss: 0x130
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FEC24DC-1E2A-3288-9B7D-34E43B8BF0BD
-  Functions: 257
-  Symbols:   1070
-  CStrings:  562
+  UUID: E89EDA72-C610-31E6-BB1B-32019C36B31A
+  Functions: 277
+  Symbols:   1136
+  CStrings:  601
 
Symbols:
+ +[HCUtilities comfortSoundsAudioQueue]
+ +[HCUtilities comfortSoundsAudioQueue].cold.1
+ +[HCUtilities isBTLEAudioEnabled]
+ +[HCUtilities isBTLEAudioEnabled].cold.1
+ +[HCUtilities isDeviceInDeveloperMode]
+ +[HCUtilities isDeviceInDeveloperMode].cold.1
+ +[HCUtilities isLEAudioEnabled]
+ +[HCUtilities isLEAudioEnabled].cold.1
+ -[HCServer responseBlocks]
+ -[HCServer sendMessageWithPayload:identifier:andResponseBlock:]
+ -[HCServer sendSynchronousMessageWithPayloadAndGetResponse:andIdentifier:]
+ -[HCServer setResponseBlocks:]
+ GCC_except_table17
+ _CFPreferencesGetAppBooleanValue
+ _HCMessageUUIDKey
+ _OBJC_IVAR_$_HCServer._responseBlocks
+ ___24-[HCServer handleReply:]_block_invoke.15
+ ___31+[HCUtilities isLEAudioEnabled]_block_invoke
+ ___33+[HCUtilities isBTLEAudioEnabled]_block_invoke
+ ___38+[HCUtilities comfortSoundsAudioQueue]_block_invoke
+ ___38+[HCUtilities isDeviceInDeveloperMode]_block_invoke
+ ___63-[HCServer sendMessageWithPayload:identifier:andResponseBlock:]_block_invoke
+ ___74-[HCServer sendSynchronousMessageWithPayloadAndGetResponse:andIdentifier:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_literal_global.102
+ ___block_literal_global.108
+ ___block_literal_global.150
+ ___block_literal_global.49
+ ___block_literal_global.57
+ ___block_literal_global.65
+ ___block_literal_global.67
+ ___block_literal_global.69
+ ___block_literal_global.71
+ ___block_literal_global.73
+ ___block_literal_global.75
+ ___block_literal_global.81
+ ___block_literal_global.95
+ ___block_literal_global.97
+ __os_feature_enabled_impl
+ _comfortSoundsAudioQueue.ComfortSoundsQueue
+ _comfortSoundsAudioQueue.token
+ _isBTLEAudioEnabled.token
+ _isDeviceInDeveloperMode._isDeviceInDeveloperMode
+ _isDeviceInDeveloperMode.token
+ _isLEAudioEnabled._IsLEAudioEnabled
+ _isLEAudioEnabled.token
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$isBTLEAudioEnabled
+ _objc_msgSend$isDeviceInDeveloperMode
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$responseBlocks
+ _objc_msgSend$setResponseBlocks:
+ _objc_msgSend$valueForKey:
+ _sysctlbyname
- ___24-[HCServer handleReply:]_block_invoke.14
- ___block_literal_global.128
- ___block_literal_global.48
- ___block_literal_global.50
- ___block_literal_global.52
- ___block_literal_global.56
- ___block_literal_global.59
- ___block_literal_global.61
- ___block_literal_global.63
- ___block_literal_global.72
- ___block_literal_global.84
CStrings:
+ "3"
+ "AutomationAction"
+ "BT LEA 3 Enabled: yes"
+ "Device is in Developer Mode: %d (%llu/1, %d/0)"
+ "HCMessageUUIDKey"
+ "LEA 3 feature is enabled: yes"
+ "LeAudio"
+ "LiveListenRegisterForRemoteUpdates"
+ "LiveListenRewind"
+ "LiveListenTranscription"
+ "RTTMessageInjection"
+ "RTTSetTranslationLocales"
+ "T@\"NSMutableDictionary\",&,N,V_responseBlocks"
+ "_responseBlocks"
+ "com.apple.bluetooth"
+ "comfortSoundsAudioQueue"
+ "comfort_sounds_audio"
+ "dictionary"
+ "dictionaryWithDictionary:"
+ "enableHALEAudio"
+ "isBTLEAudioEnabled"
+ "isDeviceInDeveloperMode"
+ "isLEAudioEnabled"
+ "removeObjectForKey:"
+ "responseBlocks"
+ "security.mac.amfi.developer_mode_status"
+ "sendMessageWithPayload:identifier:andResponseBlock:"
+ "sendSynchronousMessageWithPayloadAndGetResponse:andIdentifier:"
+ "setResponseBlocks:"
+ "v40@0:8@16Q24@?32"
+ "valueForKey:"
- "2"

```
