## CoreSpeechExclave

> `/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`

```diff

-3304.82.8.1.2
-  __TEXT.__text: 0x1e34
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0xb0
-  __TEXT.__const: 0x68
+3305.27.1.0.0
+  __TEXT.__text: 0x22ac
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0xc8
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x62c
-  __TEXT.__oslogstring: 0x5c
-  __TEXT.__unwind_info: 0xe4
+  __TEXT.__cstring: 0x639
+  __TEXT.__oslogstring: 0xc8
+  __TEXT.__unwind_info: 0xf4
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x245
-  __TEXT.__objc_methtype: 0xe0
+  __TEXT.__objc_methname: 0x289
+  __TEXT.__objc_methtype: 0xee
   __TEXT.__objc_stubs: 0x80
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x90
-  __DATA_CONST.__objc_selrefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__cfstring: 0x560
+  __AUTH_CONST.__cfstring: 0x580
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 28
-  Symbols:   131
-  CStrings:  98
+  Functions: 32
+  Symbols:   145
+  CStrings:  104
 
Symbols:
+ -[CSSecureSiriAudioProvidingProxy configAOPVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy fetchAOPVoiceTriggerResult:]
+ -[CSSecureSiriAudioProvidingProxy prepare:]
+ -[CSSecureSiriAudioProvidingProxy startSecondPassVoiceTriggerWithFirstPassSource:pHSEnabled:supportMultiPhrase:]
+ ___43-[CSSecureSiriAudioProvidingProxy prepare:]_block_invoke
+ ___56-[CSSecureSiriAudioProvidingProxy configAOPVoiceTrigger]_block_invoke
+ ___62-[CSSecureSiriAudioProvidingProxy fetchAOPVoiceTriggerResult:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e52_v16?0{corespeechexclave_aopvoicetriggerresult_s=Q}8ls32l8
+ ___block_descriptor_40_e8_32r_e67_v56?0{corespeechexclave_voicetriggersecondpassresult_s=IIdIfffQQ}8lr32l8
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.77
+ __os_log_impl
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x8
+ _objc_retain_x22
+ _objc_retain_x23
+ _tb_message_decode_f64
+ _tb_message_decode_u64
- -[CSSecureSiriAudioProvidingProxy prepare]
- -[CSSecureSiriAudioProvidingProxy startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:]
- ___42-[CSSecureSiriAudioProvidingProxy prepare]_block_invoke
- ___block_descriptor_40_e8_32r_e60_v16?0{corespeechexclave_voicetriggersecondpassresult_s=II}8lr32l8
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.70
- ___block_descriptor_tmp.71
- _objc_release_x9
- _tb_message_destruct
- _tb_owned_buffer_allocate
CStrings:
+ "B20@0:8i16"
+ "IsolatedCoreAudioClient conclave successfully launched!"
+ "IsolatedCoreAudioClient could not launch conclave!!!"
+ "Setting Siri locale: %s (%u)"
+ "configAOPVoiceTrigger"
+ "fetchAOPVoiceTriggerResult:"
+ "fr-FR"
+ "prepare:"
+ "startSecondPassVoiceTriggerWithFirstPassSource:pHSEnabled:supportMultiPhrase:"
+ "v16@?0{corespeechexclave_aopvoicetriggerresult_s=Q}8"
+ "v32@0:8Q16B24B28"
+ "v56@?0{corespeechexclave_voicetriggersecondpassresult_s=IIdIfffQQ}8"
- "Failed to assign speakerProfileEmbedding to TB message"
- "Setting Siri local: %s (%u)"
- "prepare"
- "startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:"
- "v16@?0{corespeechexclave_voicetriggersecondpassresult_s=II}8"
- "v24@0:8B16B20"

```
