## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/Versions/A/SiriUIFoundation`

```diff

-  __TEXT.__text: 0x7ec38
-  __TEXT.__objc_methlist: 0x4308
-  __TEXT.__const: 0x32ac
-  __TEXT.__cstring: 0x6216
-  __TEXT.__oslogstring: 0x5c59
+  __TEXT.__text: 0x7f0cc
+  __TEXT.__objc_methlist: 0x4300
+  __TEXT.__const: 0x32cc
+  __TEXT.__cstring: 0x62b6
+  __TEXT.__oslogstring: 0x5c87
   __TEXT.__gcc_except_tab: 0x9b4
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__swift5_typeref: 0x119a
+  __TEXT.__swift5_typeref: 0x119e
   __TEXT.__swift5_capture: 0x534
   __TEXT.__constg_swiftt: 0x13f0
-  __TEXT.__swift5_reflstr: 0xfaa
-  __TEXT.__swift5_fieldmd: 0xe5c
+  __TEXT.__swift5_reflstr: 0xfda
+  __TEXT.__swift5_fieldmd: 0xe68
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_proto: 0x228
   __TEXT.__swift5_types: 0x118
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0xc0
-  __TEXT.__swift_as_cont: 0x108
+  __TEXT.__swift_as_cont: 0x110
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x21c8
-  __TEXT.__eh_frame: 0x1978
+  __TEXT.__unwind_info: 0x21d8
+  __TEXT.__eh_frame: 0x1950
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c00
+  __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x8c8
-  __AUTH_CONST.__const: 0x4be1
-  __AUTH_CONST.__cfstring: 0x2260
+  __DATA_CONST.__got: 0x908
+  __AUTH_CONST.__const: 0x4bb1
+  __AUTH_CONST.__cfstring: 0x2240
   __AUTH_CONST.__objc_const: 0x8848
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xb98
-  __AUTH.__objc_data: 0x1168
-  __AUTH.__data: 0xbb8
-  __DATA.__objc_ivar: 0x3f8
-  __DATA.__data: 0x1538
-  __DATA.__bss: 0x4190
-  __DATA.__common: 0x70
-  __DATA_DIRTY.__objc_data: 0xd80
-  __DATA_DIRTY.__data: 0x858
-  __DATA_DIRTY.__bss: 0x1a0
-  __DATA_DIRTY.__common: 0x60
+  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH.__objc_data: 0xff0
+  __AUTH.__data: 0xb98
+  __DATA.__objc_ivar: 0x3fc
+  __DATA.__data: 0x1520
+  __DATA.__bss: 0x4100
+  __DATA.__common: 0x48
+  __DATA_DIRTY.__objc_data: 0xef8
+  __DATA_DIRTY.__data: 0x8c8
+  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3108
-  Symbols:   5000
-  CStrings:  1306
+  Functions: 3111
+  Symbols:   4994
+  CStrings:  1308
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ +[SRUIFSiriFeatureFlag(SWEFeatureFlags) isAssistedLinwoodVoiceResponseFromCompanionEnabled]
+ +[SRUIFSpeechSynthesizer _inlineStreamMarkerRequestTextForText:inlineStreamId:companionVoiceResponseEnabled:]
+ -[SRUIFVisualCaptureContext surfaces]
+ OBJC_IVAR_$_SRUIFVisualCaptureContext._surfaces
+ _SRUIFIsCompanionVoiceResponseEnabled
+ __OBJC_$_CLASS_METHODS_SRUIFSpeechSynthesizer
+ _objc_msgSend$_inlineStreamMarkerRequestTextForText:inlineStreamId:companionVoiceResponseEnabled:
+ _objc_msgSend$expressivityPreset
+ _objc_msgSend$pacePreset
+ _objc_msgSend$sruif_applyAcousticPresetsFromVoiceInfo:
+ _symbolic _____Sg 14SiriTTSService16SynthesisContextC15VoicePacePresetO
+ _symbolic _____Sg 14SiriTTSService16SynthesisContextC23VoiceExpressivityPresetO
- +[SRUIFVisualCaptureContext supportsSecureCoding]
- -[SRUIFVisualCaptureContext description]
- -[SRUIFVisualCaptureContext encodeWithCoder:]
- -[SRUIFVisualCaptureContext initWithCoder:]
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSKeyedUnarchiver
- __OBJC_$_CLASS_METHODS_SRUIFVisualCaptureContext
- __OBJC_$_CLASS_PROP_LIST_SRUIFVisualCaptureContext
- __OBJC_CLASS_PROTOCOLS_$_SRUIFVisualCaptureContext
- ___block_descriptor_80_e8_32s40s48bs56bs64w72w_e21_v16?0"AFVoiceInfo"8l
- _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
- _objc_msgSend$data
- _objc_msgSend$initWithData:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- _swift_runtimeSupportsNoncopyableTypes
- get_type_metadata s8SendableRzsAAR_r0_l15Synchronization5MutexVyytG noncopyable
CStrings:
+ "%@%@\\%@"
+ "%s #tts inline-stream marker+text from streamId: %@"
+ "+[SRUIFSpeechSynthesizer _inlineStreamMarkerRequestTextForText:inlineStreamId:companionVoiceResponseEnabled:]"
+ "GenerateCompanionVoiceResponse"
+ "assisted_linwood_voice_response_from_companion"
- "SRUIFVisualCaptureContext %@"
- "_data"

```
