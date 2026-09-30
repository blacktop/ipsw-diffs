## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport`

```diff

-  __TEXT.__text: 0xe0994
-  __TEXT.__objc_methlist: 0x9e90
-  __TEXT.__cstring: 0x13dbc
+  __TEXT.__text: 0xe0efc
+  __TEXT.__objc_methlist: 0x9ea8
+  __TEXT.__cstring: 0x13d5c
   __TEXT.__const: 0x3f68
-  __TEXT.__gcc_except_tab: 0x141c
-  __TEXT.__oslogstring: 0x236d
+  __TEXT.__gcc_except_tab: 0x1420
+  __TEXT.__oslogstring: 0x238d
   __TEXT.__swift5_typeref: 0xb85
   __TEXT.__swift5_capture: 0x820
   __TEXT.__swift5_fieldmd: 0xb28

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2e00
+  __TEXT.__unwind_info: 0x2df8
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12f0
+  __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4430
+  __DATA_CONST.__objc_selrefs: 0x4448
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x4b0
-  __AUTH_CONST.__const: 0x3c30
+  __DATA_CONST.__got: 0x4d0
+  __AUTH_CONST.__const: 0x3c08
   __AUTH_CONST.__cfstring: 0x60a0
-  __AUTH_CONST.__objc_const: 0x111e8
+  __AUTH_CONST.__objc_const: 0x11218
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xf90
-  __AUTH.__objc_data: 0x1000
-  __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x10e0
+  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH.__objc_data: 0x1e68
+  __AUTH.__data: 0x550
+  __DATA.__objc_ivar: 0x10e4
   __DATA.__data: 0x2128
   __DATA.__bss: 0x2e30
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1598
-  __DATA_DIRTY.__data: 0x608
+  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0xc4
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5760
-  Symbols:   9134
-  CStrings:  3756
+  Functions: 5759
+  Symbols:   9135
+  CStrings:  3755
 
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
+ OBJC_IVAR_$_RPSiriSession._isVoiceTrigger
+ _OBJC_CLASS_$_NSMutableData
+ _RPOptionSiriIsVoiceTrigger
+ ___45-[RPSiriSession sendAudioPackets:linearGain:]_block_invoke
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e32_Q16?0"NSObject<OS_nw_framer>"8l
+ ___copy_helper_block_e8_32s40s48r56r64r
+ ___destroy_helper_block_e8_32s40s48r56r64r
+ __swift_closure_destructor.143Tm
+ __swift_closure_destructor.175Tm
+ __swift_closure_destructor.236Tm
+ __swift_closure_destructor.249Tm
+ _objc_msgSend$_sendSiriAudioEventWithMediaData:packetDescriptions:linearGain:
+ _objc_msgSend$appendData:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$proxyDeviceUpdateHandler
+ _objc_msgSend$setAdditionalPeerInfo:
- -[RPSiriSession _sendAudioBuffer:linearGain:]
- -[RPSiriSession sendAudioBuffer:linearGain:]
- __63-[RPSiriSession voiceControllerAudioCallback:forStream:buffer:]_block_invoke
- ___44-[RPSiriSession sendAudioBuffer:linearGain:]_block_invoke
- ___block_descriptor_56_e8_32s40s_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48r56r_e32_Q16?0"NSObject<OS_nw_framer>"8l
- ___copy_helper_block_e8_32s40s48r56r
- ___destroy_helper_block_e8_32s40s48r56r
- __swift_closure_destructor.145Tm
- __swift_closure_destructor.177Tm
- __swift_closure_destructor.238Tm
- __swift_closure_destructor.251Tm
- _nw_framer_connection_state_copy_object_value
- _nw_framer_connection_state_set_object_value
- _objc_msgSend$_sendAudioBuffer:linearGain:
- _objc_msgSend$channels
- _objc_msgSend$timeStamp
CStrings:
+ "-[RPSiriSession _sendSiriAudioEventWithMediaData:packetDescriptions:linearGain:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DODDg8/Sources/Rapport/Rapport/Pairing/RPPairingHelpers.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DODDg8/Sources/Rapport/Rapport/RPIRKRatchet.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DODDg8/Sources/Rapport/Rapport/Swift/RPUtilities.swift"
+ "Enabling FitnessPairing"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "Send Siri audio: %lu bytes, %lu packets, gain %f"
+ "_isVT"
- "-[RPSiriSession _sendAudioBuffer:linearGain:]"
- "-[RPSiriSession voiceControllerAudioCallback:forStream:buffer:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FoiR2U/Sources/Rapport/Rapport/Pairing/RPPairingHelpers.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FoiR2U/Sources/Rapport/Rapport/RPIRKRatchet.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FoiR2U/Sources/Rapport/Rapport/Swift/RPUtilities.swift"
- "Send Siri audio: TS 0x%016llX, %d bytes, %d packets, %d channels, gain %f"
- "Send Siri audio: TS 0x%016llX, %d bytes, %d packets, %d channels, gain %f\n"
- "started"
- "true"

```
