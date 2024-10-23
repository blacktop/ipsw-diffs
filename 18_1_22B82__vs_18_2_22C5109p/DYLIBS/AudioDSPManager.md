## AudioDSPManager

> `/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager`

```diff

-139.106.0.0.0
-  __TEXT.__text: 0x58508
-  __TEXT.__auth_stubs: 0x11c0
+139.324.0.0.0
+  __TEXT.__text: 0x5a62c
+  __TEXT.__auth_stubs: 0x1170
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x160
-  __TEXT.__gcc_except_tab: 0x5440
-  __TEXT.__const: 0x471b
-  __TEXT.__cstring: 0x3d21
-  __TEXT.__oslogstring: 0x269f
+  __TEXT.__gcc_except_tab: 0x55cc
+  __TEXT.__const: 0x49e8
+  __TEXT.__cstring: 0x400a
+  __TEXT.__oslogstring: 0x27b2
   __TEXT.__dlopen_cstrs: 0xbf
-  __TEXT.__unwind_info: 0x1c88
+  __TEXT.__unwind_info: 0x1ce8
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x86e
+  __TEXT.__objc_methname: 0x87e
   __TEXT.__objc_methtype: 0x38dd
-  __TEXT.__objc_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x6e0
   __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__const: 0x5a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3ac8
+  __AUTH_CONST.__const: 0x3c58
   __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x7f8
   __AUTH.__objc_data: 0x50

   __DATA.__data: 0x184
   __DATA.__crash_info: 0x40
   __DATA.__cf_except_bt: 0x2000
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1382
-  Symbols:   1798
-  CStrings:  941
+  Functions: 1403
+  Symbols:   1810
+  CStrings:  972
 
Symbols:
+ _tb_endpoint_set_interface_identifier
- _objc_release_x1
- _tb_message_decode_f32
- _tb_message_encode_f32
- _tb_message_encode_f64
- _tb_message_encode_s64
- _tb_message_encode_u8
CStrings:
+ "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
+ "ADM debug capture level set to %!d(MISSING)"
+ "ADMExclaveCaptures/"
+ "AnomalyDetection"
+ "EchoCancellation"
+ "Failed to serialize the input NSObject into json: %!@(MISSING)"
+ "HP16Mic"
+ "Input"
+ "MicPreprocessing"
+ "MutedTalkerDetection"
+ "Output"
+ "PROCESSERROR_UNINITIALIZED"
+ "Perception"
+ "RefSanitization"
+ "SharedDSP"
+ "Siri"
+ "SoundAnalysis"
+ "Total HW presentation latency is %!f(MISSING) seconds, mic-ref will be non-causal"
+ "bad VoiceProcessor[Uplink|Downlink]Configuration"
+ "com.apple.audiomxd.PerceptionAudioDSPControl"
+ "com.apple.audiomxd.SharedAudioDSPControl"
+ "com.apple.inbound_buffer.perception_ref_stream"
+ "com.apple.inbound_buffer.shared_audiodsp_ref_stream"
+ "failed to convert input port"
+ "failed to convert mic format"
+ "failed to convert out format"
+ "failed to convert output port"
+ "failed to convert ref format"
+ "getParameter(%!d(MISSING)): converting ex id %!d(MISSING) to tb failed"
+ "ioStarting() completed"
+ "ioStopped() completed"
+ "isolated audio perception"
+ "isolated audio shared DSP"
+ "setBool:forKey:"
+ "setParameter(%!d(MISSING), %!f(MISSING)): converting ex id %!d(MISSING) to tb failed"
+ "setting variable slice duration using block size %!u(MISSING) and output sample rate %!u(MISSING)"
+ "tb call to configure failed: failure=%!s(MISSING)"
+ "tb call to unconfigure failed: failure=%!s(MISSING)"
+ "unsupported configChangeRequest - devices"
+ "unsupported configuration: inputPort"
+ "unsupported configuration: outputPort"
+ "unsupported configuration: useCase"
+ "v24@?0{audiodspcontroller_audiodspcontrol_performio__result_s=C(?={audiodsputility_processerror_s=Q})}8"
+ "v24@?0{audiodspcontroller_audiodspcontrol_prepareforio__result_s=C(?={audiodsputility_setuperror_s=Q})}8"
+ "v24@?0{audiodspcontroller_audiodspcontrol_setparameter__result_s=C(?={audiodsputility_parametererror_s=Q})}8"
+ "v24@?0{audiodspcontroller_audiodspcontrol_unconfigure__result_s=C(?={audiodsputility_setuperror_s=Q})}8"
+ "v32@?0{audiodspcontroller_audiodspcontrol_getparameter__result_s=C(?={audiodsputility_parametererror_s=Q}{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B})})}8"
- "/AppleInternal/Library/BuildRoots/b4a7daee-7dd0-11ef-a7b2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/b4a7daee-7dd0-11ef-a7b2-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
- "ABHelper visit"
- "ADM debug capture level set to %!h(MISSING)hu"
- "Exclave kernel configuration is not valid - input port"
- "Failed to serialize the input NSObjct into json: %!@(MISSING)"
- "bad VoiceProcessor[Uplink|Downlink]Congiguration"
- "invalid configChangeRequest - devices"
- "setting variable slice duration using block size %!u(MISSING) and ouptut sample rate %!u(MISSING)"
- "tb call to configure failed: failure=%!d(MISSING), %!s(MISSING)"
- "tb call to unconfigure failed: failure=%!d(MISSING), %!s(MISSING)"
- "unsupported configuration: useCase:%!d(MISSING)"
- "v10@?0{audiodspcontroller_audiodspcontrol_performio__result_s=C(?=C)}8"
- "v10@?0{audiodspcontroller_audiodspcontrol_prepareforio__result_s=C(?=C)}8"
- "v10@?0{audiodspcontroller_audiodspcontrol_setparameter__result_s=C(?=C)}8"
- "v10@?0{audiodspcontroller_audiodspcontrol_unconfigure__result_s=C(?=C)}8"
- "v32@?0{audiodspcontroller_audiodspcontrol_getparameter__result_s=C(?=C{audiodsputility_parametervalue_s=Q(?={?=C}{?=B}{?=B}{?=B}{?=f})})}8"

```
