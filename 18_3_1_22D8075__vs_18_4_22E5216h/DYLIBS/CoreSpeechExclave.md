## CoreSpeechExclave

> `/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x77fc
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x170
-  __TEXT.__cstring: 0x6d1
-  __TEXT.__const: 0x1e8
-  __TEXT.__constg_swiftt: 0x1d8
-  __TEXT.__swift5_typeref: 0x97
-  __TEXT.__swift5_fieldmd: 0x114
-  __TEXT.__swift5_reflstr: 0xf6
+3404.79.2.0.0
+  __TEXT.__text: 0x75ac
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x188
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x833
+  __TEXT.__constg_swiftt: 0x1a0
+  __TEXT.__swift5_typeref: 0x78
+  __TEXT.__swift5_fieldmd: 0x64
+  __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__oslogstring: 0x1be
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__oslogstring: 0x15e
   __TEXT.__unwind_info: 0x1c0
-  __TEXT.__eh_frame: 0xb8
+  __TEXT.__eh_frame: 0xd8
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x453
-  __TEXT.__objc_methtype: 0x232
-  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_methname: 0x4ab
+  __TEXT.__objc_methtype: 0x3f2
+  __TEXT.__objc_stubs: 0x140
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x110
+  __DATA_CONST.__objc_selrefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x288
-  __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x128
+  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_ptr: 0x58
   __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__objc_const: 0x2f8
   __DATA.__objc_ivar: 0x8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 95
-  Symbols:   151
-  CStrings:  135
+  Functions: 78
+  Symbols:   154
+  CStrings:  137
 
Symbols:
+ _objc_release_x27
+ _objc_retain_x27
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_bool
+ _tb_message_raw_decode_f64
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_f32
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
- _objc_release_x25
- _objc_retain_x25
- _swift_retain
- _tb_message_decode_f64
- _tb_message_decode_u32
- _tb_message_encode_bool
- _tb_message_encode_f32
- _tb_message_encode_u32
- _tb_message_encode_u64
CStrings:
+ "Q24@0:8{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}16"
+ "Q24@0:8{corespeechexclave_voicetriggerpersonalizationresult_s=Q}16"
+ "Q80@0:8{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}16"
+ "convertSecureVoiceTriggerKeywordDetectionResultType:"
+ "convertSecureVoiceTriggerSpeakerDetectionResultType:"
+ "reset"
+ "v24@?0{corespeechexclave_aopvoicetriggerresult_s=QB}8"
+ "v72@?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}8"
- "Q72@0:8{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIfffQQ}})}16"
- "entitiesInVicinityCount:%lu, inViscinityFacing:%d, inViscinityGazing:%d, inViscinitySpeaking:%d"
- "updateEntityStatistics:"
- "v16@?0{corespeechexclave_aopvoicetriggerresult_s=Q}8"
- "v24@0:8^{SecureEntityStatistics=IBBB}16"
- "v64@?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIfffQQ}})}8"

```
