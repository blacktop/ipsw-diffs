## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

-1638.208.0.0.0
-  __TEXT.__text: 0x2701e0
+1638.209.1.0.0
+  __TEXT.__text: 0x270868
   __TEXT.__realtime: 0x29810
   __TEXT.__delay_stubs: 0x100
   __TEXT.__delay_helper: 0x148
   __TEXT.__objc_methlist: 0x205c
   __TEXT.__const: 0x494c
   __TEXT.__dlopen_cstrs: 0x8a5
-  __TEXT.__gcc_except_tab: 0x2327c
-  __TEXT.__cstring: 0x25758
-  __TEXT.__oslogstring: 0x396f4
+  __TEXT.__gcc_except_tab: 0x2328c
+  __TEXT.__cstring: 0x2576e
+  __TEXT.__oslogstring: 0x398a1
   __TEXT.__unwind_info: 0xd7a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x3a8
-  __DATA_CONST.__got: 0xde0
+  __DATA_CONST.__got: 0xdf0
   __AUTH_CONST.__const: 0x11a30
-  __AUTH_CONST.__cfstring: 0x6040
+  __AUTH_CONST.__cfstring: 0x6060
   __AUTH_CONST.__objc_const: 0x30f0
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_intobj: 0x5e8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 10060
-  Symbols:   17000
-  CStrings:  7570
+  Symbols:   17002
+  CStrings:  7576
 
Symbols:
+ _kLoudnessInfoDictionary_ContentTypeKey
+ _kLoudnessInfoDictionary_LibraryLoudnessKey
Functions:
~ ____ZN20AudioCapturerManager10InitializeEv_block_invoke : 2060 -> 2044
~ __ZNK20AudioCapturerManager11GetFilePathEv : 280 -> 400
~ __ZN14MEMixerChannel28DisconnectReconfigureAddNodeEP11MCAudioUnitRKN2CA17StreamDescriptionERNSt3__16vectorIP15XProcessingBaseNS6_9allocatorIS9_EEEE : 13252 -> 13824
~ __ZN17AQMECaptureInsert12StartCaptureEONSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE8TapPoint : 528 -> 568
~ __ZN18AQOfflineMixerBase16EncoderInputProcEP20OpaqueAudioConverterPjP15AudioBufferListPP28AudioStreamPacketDescriptionPv : 7708 -> 7768
~ __ZN15LoudnessManager11GetSettingsEjP18AQConverterOrCodecjjjjbPiPNS_8SettingsE : 8440 -> 8472
~ __ZN28AudioQueuePropertyMarshaller13GetMarshallerEj : 2896 -> 2912
~ __ZN16AudioQueueObject23SetDecoderChannelLayoutEj : 352 -> 348
~ __ZN16AudioQueueObject19GetProposedIOFormatERKN2CA17StreamDescriptionEb : 3636 -> 3632
~ __ZN16AudioQueueObject19ConverterConnection14BuildConverterERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 6776 -> 6768
~ __ZN16AudioQueueObject19ConverterConnection14AdaptToFormatsEv : 5336 -> 5364
~ __ZN16AudioQueueObject17SetLoudnessFromLMEPNS_19ConverterConnectionEPK14__CFDictionary : 13216 -> 13612
~ __ZN16AudioQueueObject11GetPropertyEjR12CASerializer : 4852 -> 4908
~ __ZN16AudioQueueObject11SetPropertyEjR14CADeserializer : 13488 -> 13584
~ __ZN16AudioQueueObject22SetOfflineRenderFormatEPK27AudioStreamBasicDescriptionPK18AudioChannelLayoutP18AQOfflineMixerBase : 1704 -> 1744
~ __ZN20MEDeviceStreamClient24StartStopInternalCaptureEb : 1636 -> 1716
~ __ZN20AudioQueueXPC_Server8NewQueueEb27AudioStreamBasicDescriptionjj : 7676 -> 7724
~ __ZN20AudioQueueXPC_Server13EnqueueBufferEjNSt3__14spanIK26AQBufferCreateDestroyEventLm18446744073709551615EEEjjjNS1_IK28AudioStreamPacketDescriptionLm18446744073709551615EEEjjNS1_IK24AudioQueueParameterEventLm18446744073709551615EEE19XAudioTimeStampBaseb : 6284 -> 6280
~ __ZN20AudioQueueXPC_Server15GetPropertySizeEjj : 1836 -> 1876
~ __ZN20AudioQueueXPC_Server8MixerNewE27AudioStreamBasicDescriptionN2CA13ChannelLayoutE : 3912 -> 3996
CStrings:
+ "%25s:%-5d %.*s@%p %s: no content type found in LID content type dictionary"
+ "%25s:%-5d %.*s@%p %s: offline queue, mLMProcessOfflineQueue is on, continuing"
+ "%25s:%-5d AQOfflineMixer(%p)::RenderPCM: queue 0x%x is connected but has never started and has no scheduled start; ignoring it"
+ "%25s:%-5d Object channel layout detected: setting mLMLoudnessNormalizerUnit channel layout to %s"
+ "%25s:%-5d ObjectMix18 layout detected: setting mLMLoudnessNormalizerUnit channel layout to %s"
+ "%25s:%-5d ObjectMix28 layout detected: setting mLMLoudnessNormalizerUnit channel layout to %s"
+ "com.apple.WebKit.GPU"
- "%25s:%-5d AQOfflineMixer(%p)::RenderPCM: queue 0x%x is connected but has never startedand has no scheduled start; withholding rendering"
```
