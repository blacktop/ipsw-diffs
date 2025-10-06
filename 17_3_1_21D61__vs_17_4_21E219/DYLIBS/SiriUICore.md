## SiriUICore

> `/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore`

```diff

-3300.25.1.0.0
-  __TEXT.__text: 0x23288
+3304.5.1.0.0
+  __TEXT.__text: 0x231e0
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x294c
+  __TEXT.__objc_methlist: 0x293c
   __TEXT.__const: 0x40828
-  __TEXT.__cstring: 0x815f
-  __TEXT.__oslogstring: 0x8fc
-  __TEXT.__gcc_except_tab: 0x344
+  __TEXT.__cstring: 0x810c
+  __TEXT.__oslogstring: 0x8a3
+  __TEXT.__gcc_except_tab: 0x340
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xa4c
-  __TEXT.__objc_classname: 0x70b
-  __TEXT.__objc_methname: 0x86f6
-  __TEXT.__objc_methtype: 0x17e6
-  __TEXT.__objc_stubs: 0x6620
+  __TEXT.__unwind_info: 0xa3c
+  __TEXT.__objc_classname: 0x6f1
+  __TEXT.__objc_methname: 0x86a8
+  __TEXT.__objc_methtype: 0x17ca
+  __TEXT.__objc_stubs: 0x65e0
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x9b8
+  __DATA_CONST.__const: 0x9e0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7dd8
-  __DATA_CONST.__objc_selrefs: 0x1fe0
+  __DATA_CONST.__objc_const: 0x7dd0
+  __DATA_CONST.__objc_selrefs: 0x1fc8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x370
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__cfstring: 0x13a0
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__objc_const: 0x1198
   __AUTH_CONST.__objc_intobj: 0xa8

   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x5f0
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x370
-  __DATA.__objc_superrefs: 0x138
-  __DATA.__objc_ivar: 0x624
-  __DATA.__data: 0x770
+  __DATA.__objc_ivar: 0x62c
+  __DATA.__data: 0x710
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x460
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI
   - /System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit
+  - /System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3A709FE-958A-3424-B0AA-E14E3A3A15DB
+  UUID: 6FCAB29F-EC46-37CB-9627-9085042C9C60
   Functions: 985
-  Symbols:   4168
-  CStrings:  2314
+  Symbols:   4163
+  CStrings:  2311
 
Symbols:
+ -[SUICDefaultVoicePreviewer audioPowerUpdaterDidFire:]
+ -[SUICDefaultVoicePreviewer audioPowerUpdaterDidUpdate:]
+ _OBJC_CLASS_$_SiriTTSPreviewRequest
+ _OBJC_CLASS_$_SiriTTSServiceSession
+ _OBJC_CLASS_$_SiriTTSSynthesisVoice
+ _OBJC_IVAR_$_SUICDefaultVoicePreviewer._lastRequest
+ _OBJC_IVAR_$_SUICDefaultVoicePreviewer._session
+ ___53-[SUICDefaultVoicePreviewer previewVoice:completion:]_block_invoke.5
+ ___53-[SUICDefaultVoicePreviewer previewVoice:completion:]_block_invoke_3
+ ___54-[SUICDefaultVoicePreviewer audioPowerUpdaterDidFire:]_block_invoke
+ ___54-[SUICDefaultVoicePreviewer audioPowerUpdaterDidFire:]_block_invoke_2
+ ___54-[SUICDefaultVoicePreviewer audioPowerUpdaterDidFire:]_block_invoke_3
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40w_e11_v16?0f8f12lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s48l8s40l8
+ _objc_msgSend$audioPowerUpdaterDidFire:
+ _objc_msgSend$audioPowerUpdaterDidUpdate:
+ _objc_msgSend$cancelWithRequest:
+ _objc_msgSend$getAudioPower:
+ _objc_msgSend$initWithLanguage:name:
+ _objc_msgSend$initWithVoice:previewType:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$speakWithPreviewRequest:didFinish:
- -[SUICDefaultVoicePreviewer _beginAudioPowerUpdatesIfNecessary]
- -[SUICDefaultVoicePreviewer _endAudioPowerUpdates]
- -[SUICDefaultVoicePreviewer audioPowerUpdaterDidUpdate:averagePower:peakPower:]
- _OBJC_CLASS_$_AFAudioPowerUpdater
- _OBJC_CLASS_$_AFAudioPowerXPCProvider
- _OBJC_CLASS_$_VSSpeechSynthesizer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFAudioPowerUpdaterDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFAudioPowerUpdaterDelegate
- __OBJC_$_PROTOCOL_REFS_AFAudioPowerUpdaterDelegate
- __OBJC_LABEL_PROTOCOL_$_AFAudioPowerUpdaterDelegate
- __OBJC_PROTOCOL_$_AFAudioPowerUpdaterDelegate
- ___53-[SUICDefaultVoicePreviewer previewVoice:completion:]_block_invoke.3
- ___63-[SUICDefaultVoicePreviewer _beginAudioPowerUpdatesIfNecessary]_block_invoke
- ___63-[SUICDefaultVoicePreviewer _beginAudioPowerUpdatesIfNecessary]_block_invoke.8
- ___63-[SUICDefaultVoicePreviewer _beginAudioPowerUpdatesIfNecessary]_block_invoke_2
- ___block_descriptor_40_e8_32w_e22_v16?0"AFXPCWrapper"8lw32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8lw48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- _objc_msgSend$_beginAudioPowerUpdatesIfNecessary
- _objc_msgSend$_endAudioPowerUpdates
- _objc_msgSend$beginAudioPowerUpdateWithReply:
- _objc_msgSend$beginUpdate
- _objc_msgSend$endAudioPowerUpdate
- _objc_msgSend$endUpdate
- _objc_msgSend$initWithProvider:queue:frequency:delegate:
- _objc_msgSend$initWithXPCWrapper:
- _objc_msgSend$playVoicePreviewForLanguageCode:voiceName:previewType:completion:
- _objc_msgSend$stopPlayingVoicePreview
CStrings:
+ "@\"SiriTTSPreviewRequest\""
+ "@\"SiriTTSServiceSession\""
+ "A"
+ "T@\"NSString\",?,R,C"
+ "_lastRequest"
+ "_session"
+ "audioPowerUpdaterDidFire:"
+ "audioPowerUpdaterDidUpdate:"
+ "cancelWithRequest:"
+ "getAudioPower:"
+ "initWithLanguage:name:"
+ "initWithVoice:previewType:"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "speakWithPreviewRequest:didFinish:"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSTimer\"8"
+ "v16@?0f8f12"
- "%s Begin Audio Power Update wrapper callback with existing outputAudio updater available"
- "-[SUICDefaultVoicePreviewer _beginAudioPowerUpdatesIfNecessary]_block_invoke_2"
- "@\"AFAudioPowerUpdater\""
- "AFAudioPowerUpdaterDelegate"
- "HONG_KONG_SHORT_COUNTRY_NAME"
- "_beginAudioPowerUpdatesIfNecessary"
- "_endAudioPowerUpdates"
- "audioPowerUpdaterDidUpdate:averagePower:peakPower:"
- "beginAudioPowerUpdateWithReply:"
- "beginUpdate"
- "endAudioPowerUpdate"
- "endUpdate"
- "initWithProvider:queue:frequency:delegate:"
- "initWithXPCWrapper:"
- "playVoicePreviewForLanguageCode:voiceName:previewType:completion:"
- "stopPlayingVoicePreview"
- "v16@?0@\"AFXPCWrapper\"8"
- "v32@0:8@\"AFAudioPowerUpdater\"16f24f28"
- "v32@0:8@16f24f28"

```
