## CoreSpeechExclave

> `/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/Versions/A/CoreSpeechExclave`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x33b0
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__cstring: 0x177
-  __TEXT.__const: 0x190
-  __TEXT.__constg_swiftt: 0x1d8
-  __TEXT.__swift5_typeref: 0x97
-  __TEXT.__swift5_fieldmd: 0x114
-  __TEXT.__swift5_reflstr: 0xf6
+3404.82.3.0.0
+  __TEXT.__text: 0x7744
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_methlist: 0x188
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x879
+  __TEXT.__constg_swiftt: 0x1a0
+  __TEXT.__swift5_typeref: 0x78
+  __TEXT.__swift5_fieldmd: 0x64
+  __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0xc0
-  __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x20
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x80
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__oslogstring: 0x15e
+  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__eh_frame: 0xd8
+  __TEXT.__objc_classname: 0x21
+  __TEXT.__objc_methname: 0x4ab
+  __TEXT.__objc_methtype: 0x3f2
+  __TEXT.__objc_stubs: 0x140
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0xf8
-  __AUTH_CONST.__const: 0x128
-  __AUTH_CONST.__objc_const: 0x2b0
+  __DATA_CONST.__objc_selrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_const: 0x2f8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x1e8
+  __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x18
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x188
+  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Versions/A/Tightbeam
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 3063EE92-F8DE-3DE5-AE41-C7264EAFBF35
-  Functions: 42
-  Symbols:   89
-  CStrings:  10
+  UUID: C74A81DA-6EC9-35DE-A8FE-41419045BBED
+  Functions: 88
+  Symbols:   222
+  CStrings:  182
 
Symbols:
+ -[CSSecureSiriAudioProvidingProxy adBlockerMatchingInProgress:]
+ -[CSSecureSiriAudioProvidingProxy configAOPVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy convertAssetConfigurationError:]
+ -[CSSecureSiriAudioProvidingProxy convertSecureBargeInVoiceTriggerResultType:]
+ -[CSSecureSiriAudioProvidingProxy convertSecureSecondPassVoiceTriggerResultType:]
+ -[CSSecureSiriAudioProvidingProxy convertSecureSpeakerRecognitionType:]
+ -[CSSecureSiriAudioProvidingProxy convertSecureVoiceTriggerKeywordDetectionResultType:]
+ -[CSSecureSiriAudioProvidingProxy convertSecureVoiceTriggerSpeakerDetectionResultType:]
+ -[CSSecureSiriAudioProvidingProxy fetchAOPVoiceTriggerResult:]
+ -[CSSecureSiriAudioProvidingProxy fetchAndStoreAudioBuffer]
+ -[CSSecureSiriAudioProvidingProxy init]
+ -[CSSecureSiriAudioProvidingProxy initializeSecondPass]
+ -[CSSecureSiriAudioProvidingProxy prepare:]
+ -[CSSecureSiriAudioProvidingProxy processBargeInVoiceTriggerWithResult:]
+ -[CSSecureSiriAudioProvidingProxy processBargeInVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy processSecondPassVoiceTriggerWithShouldFlushAudio:result:]
+ -[CSSecureSiriAudioProvidingProxy requestHistoricalAudioBufferWithStartSample:completion:]
+ -[CSSecureSiriAudioProvidingProxy resetFirstPassVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy reset]
+ -[CSSecureSiriAudioProvidingProxy setAdBlockerAsset:]
+ -[CSSecureSiriAudioProvidingProxy setAssetForLocale:isOTA:completion:]
+ -[CSSecureSiriAudioProvidingProxy setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:]
+ -[CSSecureSiriAudioProvidingProxy startAdBlockerMatching]
+ -[CSSecureSiriAudioProvidingProxy startBargeInVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy startSecondPassVoiceTriggerWithStartOption:]
+ -[CSSecureSiriAudioProvidingProxy startSecureAdBlockerMobileAssetLoaderService:]
+ -[CSSecureSiriAudioProvidingProxy startSecureMobileAssetLoaderService:completion:]
+ -[CSSecureSiriAudioProvidingProxy stopAdBlockerMatching]
+ -[CSSecureSiriAudioProvidingProxy stopBargeInVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy stopSecondPassVoiceTrigger]
+ -[CSSecureSiriAudioProvidingProxy stopSecureAdBlockerMobileAssetLoaderService:]
+ -[CSSecureSiriAudioProvidingProxy stopSecureMobileAssetLoaderService:]
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table50
+ OBJC_IVAR_$_CSSecureSiriAudioProvidingProxy._service
+ OBJC_IVAR_$_CSSecureSiriAudioProvidingProxy._tightbeamEndpoint
+ __Block_object_assign
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __OBJC_$_INSTANCE_METHODS_CSSecureSiriAudioProvidingProxy
+ __OBJC_$_INSTANCE_VARIABLES_CSSecureSiriAudioProvidingProxy
+ __Unwind_Resume
+ ___43-[CSSecureSiriAudioProvidingProxy prepare:]_block_invoke
+ ___53-[CSSecureSiriAudioProvidingProxy setAdBlockerAsset:]_block_invoke
+ ___55-[CSSecureSiriAudioProvidingProxy initializeSecondPass]_block_invoke
+ ___56-[CSSecureSiriAudioProvidingProxy configAOPVoiceTrigger]_block_invoke
+ ___59-[CSSecureSiriAudioProvidingProxy fetchAndStoreAudioBuffer]_block_invoke
+ ___61-[CSSecureSiriAudioProvidingProxy processBargeInVoiceTrigger]_block_invoke
+ ___62-[CSSecureSiriAudioProvidingProxy fetchAOPVoiceTriggerResult:]_block_invoke
+ ___63-[CSSecureSiriAudioProvidingProxy adBlockerMatchingInProgress:]_block_invoke
+ ___70-[CSSecureSiriAudioProvidingProxy setAssetForLocale:isOTA:completion:]_block_invoke
+ ___70-[CSSecureSiriAudioProvidingProxy stopSecureMobileAssetLoaderService:]_block_invoke
+ ___72-[CSSecureSiriAudioProvidingProxy processBargeInVoiceTriggerWithResult:]_block_invoke
+ ___79-[CSSecureSiriAudioProvidingProxy stopSecureAdBlockerMobileAssetLoaderService:]_block_invoke
+ ___80-[CSSecureSiriAudioProvidingProxy startSecureAdBlockerMobileAssetLoaderService:]_block_invoke
+ ___82-[CSSecureSiriAudioProvidingProxy startSecureMobileAssetLoaderService:completion:]_block_invoke
+ ___90-[CSSecureSiriAudioProvidingProxy requestHistoricalAudioBufferWithStartSample:completion:]_block_invoke
+ ___92-[CSSecureSiriAudioProvidingProxy processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke
+ ___99-[CSSecureSiriAudioProvidingProxy setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:]_block_invoke
+ ___CFConstantStringClassReference
+ ___block_descriptor_40_e8_32bs_e53_v24?0{corespeechexclave_aopvoicetriggerresult_s=QB}8l
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8l
+ ___block_descriptor_40_e8_32r_e123_v32?0{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}8l
+ ___block_descriptor_40_e8_32r_e488_v72?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}8l
+ ___block_descriptor_40_e8_32r_e49_v16?0{corespeechexclave_writebufferresult_s=II}8l
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40bs_e58_v16?0{corespeechexclave_siriassetconfigurationerror_s=Q}8l
+ ___block_descriptor_tmp
+ ___copy_helper_block_8_32b
+ ___copy_helper_block_8_32r
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32s40b
+ ___destroy_helper_block_8_32b
+ ___destroy_helper_block_8_32r
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s40s
+ ___f32__v_raw_encode_block_invoke
+ ___f32__v_sizeof_block_invoke
+ ___f32__v_visit_block_invoke
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __block_descriptor_tmp.183
+ __block_descriptor_tmp.186
+ __block_descriptor_tmp.188
+ __f32__v_raw_encode_block_invoke.187
+ __os_crash
+ __os_log_error_impl
+ __os_log_impl
+ _corespeechexclave_sirivoicetriggerservice_bargeinprocess
+ _corespeechexclave_voicetriggersecondpassresulttriggered__decode
+ _f32__v_visit
+ _objc_msgSend
+ _objc_msgSend$UTF8String
+ _objc_msgSend$bytes
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$convertAssetConfigurationError:
+ _objc_msgSend$convertSecureBargeInVoiceTriggerResultType:
+ _objc_msgSend$convertSecureSecondPassVoiceTriggerResultType:
+ _objc_msgSend$convertSecureSpeakerRecognitionType:
+ _objc_msgSend$convertSecureVoiceTriggerKeywordDetectionResultType:
+ _objc_msgSend$convertSecureVoiceTriggerSpeakerDetectionResultType:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _os_log_create
+ _os_log_type_enabled
+ _os_variant_is_darwinos
+ _printf
+ _sLog
+ _tb_client_connection_activate
+ _tb_client_connection_create_with_endpoint
+ _tb_client_connection_message_construct
+ _tb_client_connection_message_destruct
+ _tb_conclave_endpoint_for_service
+ _tb_connection_send_query
+ _tb_endpoint_set_interface_identifier
+ _tb_message_complete
+ _tb_message_configure_received
+ _tb_message_construct
+ _tb_message_decode_bool
+ _tb_message_decode_f32
+ _tb_message_decode_u64
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
+ _tb_message_subrange
+ _tb_transport_message_buffer_wrap_buffer
- ___swift_memcpy48_8
- ___swift_memcpy49_8
- ___swift_noop_void_return
- _swift_retain
- _symbolic Sd
- _symbolic Sf
- _symbolic _____ 17CoreSpeechExclave28VoiceTriggerSecondPassResultO
- _symbolic _____ 17CoreSpeechExclave37VoiceTriggerSecondPassResultTriggeredV
- _symbolic _____ s6UInt32V
- _symbolic _____ s6UInt64V
CStrings:
+ "-"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/CoreSpeech_Common/install/TempContent/Objects/CoreSpeech.build/CoreSpeechExclave.build/DerivedSources/CoreSpeechExclave_C.c"
+ "@16@0:8"
+ "B16@0:8"
+ "B20@0:8i16"
+ "B48@0:8@16Q24Q32Q40"
+ "Error: Invalid locale %s. Falling back to en-US"
+ "Failed to setSpeakerProfileEmbedding"
+ "Framework"
+ "I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8"
+ "IsolatedCoreAudioClient BargeIn start"
+ "IsolatedCoreAudioClient BargeIn stop"
+ "IsolatedCoreAudioClient conclave successfully launched!"
+ "IsolatedCoreAudioClient could not launch conclave with error %d!!!"
+ "IsolatedCoreAudioClient process barge-in"
+ "Q16@0:8"
+ "Q24@0:8Q16"
+ "Q24@0:8{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}16"
+ "Q24@0:8{corespeechexclave_voicetriggerpersonalizationresult_s=Q}16"
+ "Q40@0:8{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}16"
+ "Q80@0:8{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}16"
+ "Siri locale:%@, isOTA:%d"
+ "TB_ASSERT: (err == TB_ERROR_SUCCESS) && \"failed to wrap packed buffer\""
+ "TB_ASSERT: (vErr == TB_ERROR_SUCCESS) && \"tb_message_subrange failed\""
+ "TB_FATAL: invalid tag in array metadata: 0x%x"
+ "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid value: unexpected case value, %llx"
+ "TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n"
+ "UTF8String"
+ "^{tb_endpoint_s=(?=[96c]^v)}"
+ "_"
+ "_service"
+ "_tightbeamEndpoint"
+ "adBlockerMatchingInProgress:"
+ "ar-AE"
+ "ar-SA"
+ "bytes"
+ "caseInsensitiveCompare:"
+ "com.apple.corespeech"
+ "com.apple.corespeechd.SiriVoiceTriggerService"
+ "configAOPVoiceTrigger"
+ "convertAssetConfigurationError:"
+ "convertSecureBargeInVoiceTriggerResultType:"
+ "convertSecureSecondPassVoiceTriggerResultType:"
+ "convertSecureSpeakerRecognitionType:"
+ "convertSecureVoiceTriggerKeywordDetectionResultType:"
+ "convertSecureVoiceTriggerSpeakerDetectionResultType:"
+ "da-DK"
+ "de-AT"
+ "de-CH"
+ "de-DE"
+ "en-AU"
+ "en-CA"
+ "en-GB"
+ "en-IE"
+ "en-IN"
+ "en-NZ"
+ "en-SG"
+ "en-US"
+ "en-ZA"
+ "es-CL"
+ "es-ES"
+ "es-MX"
+ "es-US"
+ "fetchAOPVoiceTriggerResult:"
+ "fetchAndStoreAudioBuffer"
+ "fi-FI"
+ "fr-BE"
+ "fr-CA"
+ "fr-CH"
+ "fr-FR"
+ "he-IL"
+ "init"
+ "initializeSecondPass"
+ "it-CH"
+ "it-IT"
+ "ja-JP"
+ "ko-KR"
+ "ms-MY"
+ "nb-NO"
+ "nl-BE"
+ "nl-NL"
+ "prepare:"
+ "processBargeInVoiceTrigger"
+ "processBargeInVoiceTriggerWithResult:"
+ "processSecondPassVoiceTriggerWithShouldFlushAudio:result:"
+ "pt-BR"
+ "requestHistoricalAudioBufferWithStartSample:completion:"
+ "reset"
+ "resetFirstPassVoiceTrigger"
+ "ru-RU"
+ "setAdBlockerAsset:"
+ "setAssetForLocale:isOTA:completion:"
+ "setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:"
+ "startAdBlockerMatching"
+ "startBargeInVoiceTrigger"
+ "startSecondPassVoiceTriggerWithStartOption:"
+ "startSecureAdBlockerMobileAssetLoaderService:"
+ "startSecureMobileAssetLoaderService:completion:"
+ "stopAdBlockerMatching"
+ "stopBargeInVoiceTrigger"
+ "stopSecondPassVoiceTrigger"
+ "stopSecureAdBlockerMobileAssetLoaderService:"
+ "stopSecureMobileAssetLoaderService:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "sv-SE"
+ "th-TH"
+ "tr-TR"
+ "v12@?0B8"
+ "v16@0:8"
+ "v16@?0{corespeechexclave_siriassetconfigurationerror_s=Q}8"
+ "v16@?0{corespeechexclave_writebufferresult_s=II}8"
+ "v20@?0Q8f16"
+ "v24@0:8@?16"
+ "v24@?0{corespeechexclave_aopvoicetriggerresult_s=QB}8"
+ "v28@0:8B16@?20"
+ "v32@0:8Q16@?24"
+ "v32@0:8{?=QBBI}16"
+ "v32@?0{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}8"
+ "v36@0:8@16B24@?28"
+ "v72@?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}8"
+ "vi-VN"
+ "yue-CN"
+ "zh-CN"
+ "zh-HK"
+ "zh-TW"
+ "{corespeechexclave_sirivoicetriggerservice_s=\"connection\"^{tb_connection_s}}"

```
