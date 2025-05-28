## TextToSpeechBundleSupport

> `/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport`

```diff

-583.1.4.0.0
-  __TEXT.__text: 0x39624
-  __TEXT.__auth_stubs: 0x1f10
-  __TEXT.__objc_methlist: 0x1318
-  __TEXT.__const: 0xd0a
+583.1.13.0.0
+  __TEXT.__text: 0x3a704
+  __TEXT.__auth_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x1398
+  __TEXT.__const: 0xf2a
   __TEXT.__gcc_except_tab: 0x1bc0
   __TEXT.__cstring: 0x4284
   __TEXT.__ustring: 0x13c4
   __TEXT.__oslogstring: 0xe33
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x35e
-  __TEXT.__swift5_capture: 0xec
-  __TEXT.__constg_swiftt: 0x46c
-  __TEXT.__swift5_reflstr: 0x381
-  __TEXT.__swift5_fieldmd: 0x3dc
+  __TEXT.__swift5_typeref: 0x3a6
+  __TEXT.__swift5_capture: 0xfc
+  __TEXT.__swift5_reflstr: 0x3e1
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0x500
+  __TEXT.__swift5_fieldmd: 0x464
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x4
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__unwind_info: 0xfd0
-  __TEXT.__eh_frame: 0x168
-  __TEXT.__objc_classname: 0x1db
-  __TEXT.__objc_methname: 0x4876
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__unwind_info: 0x1010
+  __TEXT.__eh_frame: 0x170
+  __TEXT.__objc_classname: 0x1dd
+  __TEXT.__objc_methname: 0x498c
   __TEXT.__objc_methtype: 0xe21
-  __TEXT.__objc_stubs: 0x36a0
-  __DATA_CONST.__got: 0x248
+  __TEXT.__objc_stubs: 0x3740
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__const: 0x730
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2920
-  __DATA_CONST.__objc_selrefs: 0x1180
+  __DATA_CONST.__objc_const: 0x2ab0
+  __DATA_CONST.__objc_selrefs: 0x11c8
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__cfstring: 0x39a0
-  __AUTH_CONST.__const: 0x1080
+  __AUTH_CONST.__const: 0x1198
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__objc_const: 0x5a0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH_CONST.__auth_got: 0xfd0
   __AUTH.__objc_data: 0x370
   __AUTH.__const_weak: 0x4e8
-  __AUTH.__data: 0x18
+  __AUTH.__data: 0x20
   __AUTH.__got_weak: 0x28
   __DATA.__got_weak: 0x128
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x1f0
+  __DATA.__objc_classrefs: 0x1f8
   __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_ivar: 0x220
   __DATA.__objc_data: 0x18
-  __DATA.__data: 0xa70
+  __DATA.__data: 0xa90
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x340
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x380
-  __DATA_DIRTY.__data: 0x218
-  __DATA_DIRTY.__bss: 0x88
-  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__data: 0xe8
+  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1289
-  Symbols:   3662
-  CStrings:  1882
+  Functions: 1337
+  Symbols:   3704
+  CStrings:  1902
 
Symbols:
+ -[TTSSiriSynthWrapper _setProsodyParameters]
+ -[TTSSiriSynthWrapper duration]
+ -[TTSSiriSynthWrapper energy]
+ -[TTSSiriSynthWrapper pitchRange]
+ -[TTSSiriSynthWrapper pitch]
+ -[TTSSiriSynthWrapper setDuration:]
+ -[TTSSiriSynthWrapper setEnergy:]
+ -[TTSSiriSynthWrapper setPitch:]
+ -[TTSSiriSynthWrapper setPitchRange:]
+ -[TTSSiriSynthWrapper setTilt:]
+ -[TTSSiriSynthWrapper tilt]
+ GCC_except_table24
+ GCC_except_table68
+ _OBJC_CLASS_$_AUParameterTree
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._duration
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._energy
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._pitch
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._pitchRange
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._tilt
+ __PROTOCOLS__TtC25TextToSpeechBundleSupport21TTSSiriSynthAudioUnit.32
+ __ZN14TTSSynthesizer19set_global_propertyENS_14GlobalPropertyEf
+ ___block_literal_global.197
+ ___swift_memcpy1_1
+ _associated conformance 25TextToSpeechBundleSupport13SiriParameterOSHAASQ
+ _block_copy_helper.25
+ _block_copy_helper.52
+ _block_copy_helper.77
+ _block_copy_helper.95
+ _block_descriptor.27
+ _block_descriptor.54
+ _block_descriptor.79
+ _block_descriptor.97
+ _block_destroy_helper.26
+ _block_destroy_helper.53
+ _block_destroy_helper.78
+ _block_destroy_helper.96
+ _objc_msgSend$_setProsodyParameters
+ _objc_msgSend$duration
+ _objc_msgSend$energy
+ _objc_msgSend$pitchRange
+ _objc_msgSend$tilt
+ _symbolic $sSY
+ _symbolic Sf
+ _symbolic So32AVSpeechSynthesisProviderRequestC
+ _symbolic _____ 25TextToSpeechBundleSupport13SiriParameterO
+ _symbolic _____ySfG 12TextToSpeech12AUParamValueV
- GCC_except_table17
- GCC_except_table25
- GCC_except_table57
- GCC_except_table69
- __PROTOCOLS__TtC25TextToSpeechBundleSupport21TTSSiriSynthAudioUnit.7
- ___block_literal_global.168
- _block_copy_helper.26
- _block_copy_helper.4
- _block_copy_helper.41
- _block_copy_helper.51
- _block_descriptor.28
- _block_descriptor.43
- _block_descriptor.53
- _block_descriptor.6
- _block_destroy_helper.27
- _block_destroy_helper.42
- _block_destroy_helper.5
- _block_destroy_helper.52
CStrings:
+ "1'"
+ "Tf,N,V_duration"
+ "Tf,N,V_energy"
+ "Tf,N,V_pitchRange"
+ "Tf,N,V_tilt"
+ "_duration"
+ "_energy"
+ "_pitchRange"
+ "_setProsodyParameters"
+ "_tilt"
+ "createParameterWithIdentifier:name:address:min:max:unit:unitName:flags:valueStrings:dependentParameters:"
+ "duration"
+ "energy"
+ "jobIdentifier"
+ "pitchRange"
+ "setDuration:"
+ "setEnergy:"
+ "setPitchRange:"
+ "setTilt:"
+ "tilt"
- "\x11'"
- "%s --> %s"
- "Recieved SSML: %s"
- "Vocalizer Markup: %s"
- "initWithString:"
- "shouldLogSensitiveSpeech"

```
