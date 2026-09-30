## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-  __TEXT.__text: 0xd9160
-  __TEXT.__objc_methlist: 0x9ef0
-  __TEXT.__cstring: 0x1463c
+  __TEXT.__text: 0xd96a8
+  __TEXT.__objc_methlist: 0x9f08
+  __TEXT.__cstring: 0x145dc
   __TEXT.__const: 0x3f68
-  __TEXT.__gcc_except_tab: 0x1444
-  __TEXT.__oslogstring: 0x236d
+  __TEXT.__gcc_except_tab: 0x1448
+  __TEXT.__oslogstring: 0x238d
   __TEXT.__swift5_typeref: 0xb85
   __TEXT.__swift5_capture: 0x820
   __TEXT.__swift5_fieldmd: 0xb28

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2e68
+  __TEXT.__unwind_info: 0x2e70
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2790
+  __DATA_CONST.__const: 0x2798
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44b0
+  __DATA_CONST.__objc_selrefs: 0x44c8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x4b0
-  __AUTH_CONST.__const: 0x2610
+  __DATA_CONST.__got: 0x4d0
+  __AUTH_CONST.__const: 0x25e8
   __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x11268
+  __AUTH_CONST.__objc_const: 0x11298
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1150
-  __AUTH.__objc_data: 0x1000
-  __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x10e8
+  __AUTH_CONST.__auth_got: 0x1130
+  __AUTH.__objc_data: 0x1280
+  __AUTH.__data: 0x538
+  __DATA.__objc_ivar: 0x10ec
   __DATA.__data: 0x20d8
-  __DATA.__bss: 0x2ea0
+  __DATA.__bss: 0x2e90
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1598
-  __DATA_DIRTY.__data: 0x5a8
-  __DATA_DIRTY.__bss: 0xb4
+  __DATA_DIRTY.__objc_data: 0x1318
+  __DATA_DIRTY.__data: 0x588
+  __DATA_DIRTY.__bss: 0xc4
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5734
-  Symbols:   13583
-  CStrings:  3790
+  Functions: 5733
+  Symbols:   13580
+  CStrings:  3789
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[RPSiriSession _sendSiriAudioEventWithMediaData:packetDescriptions:linearGain:]
+ -[RPSiriSession isVoiceTrigger]
+ -[RPSiriSession sendAudioPackets:linearGain:]
+ -[RPSiriSession setIsVoiceTrigger:]
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_IVAR_$_RPSiriSession._isVoiceTrigger
+ _RPOptionSiriIsVoiceTrigger
+ ___45-[RPSiriSession sendAudioPackets:linearGain:]_block_invoke
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e32_Q16?0"NSObject<OS_nw_framer>"8lr48l8r56l8r64l8s32l8s40l8
+ ___swift_closure_destructor.143Tm
+ ___swift_closure_destructor.175Tm
+ ___swift_closure_destructor.236Tm
+ ___swift_closure_destructor.249Tm
+ _objc_msgSend$_sendSiriAudioEventWithMediaData:packetDescriptions:linearGain:
+ _objc_msgSend$appendData:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$proxyDeviceUpdateHandler
+ _objc_msgSend$setAdditionalPeerInfo:
- -[RPSiriSession _sendAudioBuffer:linearGain:]
- -[RPSiriSession sendAudioBuffer:linearGain:]
- ___44-[RPSiriSession sendAudioBuffer:linearGain:]_block_invoke
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e32_Q16?0"NSObject<OS_nw_framer>"8lr48l8r56l8s32l8s40l8
- ___swift_closure_destructor.145Tm
- ___swift_closure_destructor.177Tm
- ___swift_closure_destructor.238Tm
- ___swift_closure_destructor.251Tm
- _nw_framer_connection_state_copy_object_value
- _nw_framer_connection_state_set_object_value
- _objc_msgSend$_sendAudioBuffer:linearGain:
- _objc_msgSend$channels
- _objc_msgSend$timeStamp
- _swift_retain_x21
- _swift_retain_x27
CStrings:
+ "-[RPSiriSession _sendSiriAudioEventWithMediaData:packetDescriptions:linearGain:]"
+ "Enabling FitnessPairing"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "Send Siri audio: %lu bytes, %lu packets, gain %f"
+ "_isVT"
- "-[RPSiriSession _sendAudioBuffer:linearGain:]"
- "-[RPSiriSession voiceControllerAudioCallback:forStream:buffer:]_block_invoke"
- "Send Siri audio: TS 0x%016llX, %d bytes, %d packets, %d channels, gain %f"
- "Send Siri audio: TS 0x%016llX, %d bytes, %d packets, %d channels, gain %f\n"
- "started"
- "true"

```
