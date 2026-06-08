## CoreSpeechExclave

> `/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`

```diff

-3525.5.8.0.0
-  __TEXT.__text: 0x8c80
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x1a0
-  __TEXT.__const: 0x818
+3600.64.114.1.5
+  __TEXT.__text: 0xfec4
+  __TEXT.__objc_methlist: 0x260
+  __TEXT.__const: 0x1dc0
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__constg_swiftt: 0x318
-  __TEXT.__swift5_typeref: 0xe3
-  __TEXT.__swift5_fieldmd: 0x2b8
-  __TEXT.__swift5_reflstr: 0x245
-  __TEXT.__cstring: 0x947
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__oslogstring: 0x1a6
-  __TEXT.__unwind_info: 0x2e8
-  __TEXT.__eh_frame: 0x5c8
-  __TEXT.__objc_classname: 0xd9
-  __TEXT.__objc_methname: 0x535
-  __TEXT.__objc_methtype: 0x3e8
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__constg_swiftt: 0x85c
+  __TEXT.__swift5_typeref: 0x722
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_types: 0x80
+  __TEXT.__swift5_reflstr: 0x848
+  __TEXT.__swift5_fieldmd: 0xa00
+  __TEXT.__swift5_mpenum: 0x34
+  __TEXT.__swift5_proto: 0x174
+  __TEXT.__cstring: 0xa55
+  __TEXT.__swift5_protos: 0x54
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__oslogstring: 0x2a7
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__eh_frame: 0x14b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x148
+  __DATA_CONST.__objc_selrefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH_CONST.__const: 0x610
+  __DATA_CONST.__got: 0x70
+  __AUTH_CONST.__const: 0x1150
   __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__objc_const: 0x2d8
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x38
-  __DATA.__bss: 0xba8
+  __AUTH_CONST.__objc_const: 0x340
+  __AUTH_CONST.__auth_got: 0x348
+  __AUTH.__objc_data: 0x70
+  __AUTH.__data: 0x210
+  __DATA.__objc_ivar: 0xc
+  __DATA.__data: 0x100
+  __DATA.__bss: 0x2480
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7949D556-B049-3C4D-BB09-84E7230FE4FC
-  Functions: 182
-  Symbols:   316
-  CStrings:  204
+  UUID: 18FBCC48-6402-30F1-BA2C-39BB34F4C872
+  Functions: 507
+  Symbols:   431
+  CStrings:  148
 
Symbols:
+ -[CSSecureSiriAudioProvidingProxy .cxx_destruct]
+ -[CSSecureSiriAudioProvidingProxy fetchAndStoreAudioBufferWithHostTime:]
+ -[CSSecureSiriAudioProvidingProxy fetchIMUWithCatchup:]
+ -[CSSecureSiriAudioProvidingProxy fetchRaiseToSpeakResult:]
+ -[CSSecureSiriAudioProvidingProxy fetchSecondPassResult:completion:]
+ -[CSSecureSiriAudioProvidingProxy fetchVoiceTriggerAPResult:]
+ -[CSSecureSiriAudioProvidingProxy initWithServiceName:]
+ -[CSSecureSiriAudioProvidingProxy skipProcessingVoiceTriggerAPModeAOE:]
+ -[CSSecureSiriAudioProvidingProxy startBargeInVoiceTriggerWithStartOption:]
+ -[CSSecureSiriAudioProvidingProxy startRaiseToSpeak]
+ -[CSSecureSiriAudioProvidingProxy stopRaiseToSpeak]
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table25
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table66
+ _OBJC_CLASS_$_CSSecureAOEAudioProvidingProxy
+ _OBJC_IVAR_$_CSSecureSiriAudioProvidingProxy._serviceName
+ _OBJC_METACLASS_$_CSSecureAOEAudioProvidingProxy
+ __DATA_CSSecureAOEAudioProvidingProxy
+ __INSTANCE_METHODS_CSSecureAOEAudioProvidingProxy
+ __METACLASS_DATA_CSSecureAOEAudioProvidingProxy
+ ___59-[CSSecureSiriAudioProvidingProxy fetchRaiseToSpeakResult:]_block_invoke
+ ___61-[CSSecureSiriAudioProvidingProxy fetchVoiceTriggerAPResult:]_block_invoke
+ ___68-[CSSecureSiriAudioProvidingProxy fetchSecondPassResult:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e123_v32?0{corespeechexclave_raisetospeakresultprivate_s=Q(?={?={corespeechexclave_raisetospeakpolicydecisionprivate_s=Bfd}})}8ls32l8
+ ___block_descriptor_40_e8_32bs_e60_v24?0{corespeechexclave_aopvoicetriggerresultprivate_s=QB}8ls32l8
+ ___block_descriptor_40_e8_32r_e138_v40?0{corespeechexclave_bargeinvoicetriggerresultprivate_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggeredprivate_s=QIQ}})}8lr32l8
+ ___block_descriptor_40_e8_32r_e546_v88?0{corespeechexclave_voicetriggersecondpassresultprivate_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggeredprivate_s=QdIQQQQ{corespeechexclave_voicetriggerkeyworddetectionresultprivate_s=Q}{corespeechexclave_voicetriggerpersonalizationresultprivate_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejectedprivate_s=I{corespeechexclave_voicetriggerkeyworddetectionresultprivate_s=Q}{corespeechexclave_voicetriggerpersonalizationresultprivate_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailedprivate_s=Q}})}8lr32l8
+ ___block_descriptor_40_e8_32r_e56_v16?0{corespeechexclave_writebufferresultprivate_s=II}8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e65_v16?0{corespeechexclave_siriassetconfigurationerrorprivate_s=Q}8ls40l8s32l8
+ ___swift_memcpy16_8
+ ___swift_memcpy24_8
+ ___swift_memcpy25_8
+ ___swift_memcpy58_8
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 17CoreSpeechExclave10SiriLocaleOSHAASQ
+ _associated conformance 17CoreSpeechExclave27SiriAssetConfigurationErrorOSHAASQ
+ _associated conformance 17CoreSpeechExclave28RaiseToSpeakGestureFetchModeOSHAASQ
+ _associated conformance 17CoreSpeechExclave34VoiceTriggerSecondPassResultFailedOSHAASQ
+ _corespeechexclave_voicetriggersecondpassresultprivate__decode
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$fetchAndStoreAudioBuffer
+ _objc_msgSend$init
+ _objc_msgSend$initWithDelegate:serviceName:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$length
+ _objc_release_x21
+ _objc_release_x24
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_storeStrong
+ _swift_bridgeObjectRetain
+ _swift_deallocPartialClassInstance
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_release_x19
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_unknownObjectRelease
+ _symbolic $s17CoreSpeechExclave30SiriLocalePrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave37WriteBufferResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave38RaiseToSpeakResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave41AOPVoiceTriggerResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave41SpeakerRecognizerTypePrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave43SpeakerProfileEmbeddingPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave45BargeInVoiceTriggerResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave46RaiseToSpeakPolicyDecisionPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave47SiriAssetConfigurationErrorPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave48RaiseToSpeakGestureFetchModePrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave48VoiceTriggerSecondPassResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave51SiriVoiceTriggerFirstPassSourcePrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave52SiriVoiceTriggerSecondPassOptionPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave53VoiceTriggerPersonalizationResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave54BargeInVoiceTriggerResultTriggeredPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave54SiriVoiceTriggerBargeInStartOptionPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave54VoiceTriggerKeywordDetectionResultPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave54VoiceTriggerSecondPassResultFailedPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave56VoiceTriggerSecondPassResultRejectedPrivateRepresentableP
+ _symbolic $s17CoreSpeechExclave57VoiceTriggerSecondPassResultTriggeredPrivateRepresentableP
+ _symbolic Sf
+ _symbolic _____ 17CoreSpeechExclave10SiriLocaleO
+ _symbolic _____ 17CoreSpeechExclave18RaiseToSpeakResultO
+ _symbolic _____ 17CoreSpeechExclave24WriteBufferResultPrivateV
+ _symbolic _____ 17CoreSpeechExclave25BargeInVoiceTriggerResultO
+ _symbolic _____ 17CoreSpeechExclave26RaiseToSpeakPolicyDecisionV
+ _symbolic _____ 17CoreSpeechExclave27SiriAssetConfigurationErrorO
+ _symbolic _____ 17CoreSpeechExclave28AOPVoiceTriggerResultPrivateV
+ _symbolic _____ 17CoreSpeechExclave28RaiseToSpeakGestureFetchModeO
+ _symbolic _____ 17CoreSpeechExclave28VoiceTriggerSecondPassResultO
+ _symbolic _____ 17CoreSpeechExclave30SpeakerProfileEmbeddingPrivateV
+ _symbolic _____ 17CoreSpeechExclave33RaiseToSpeakPolicyDecisionPrivateV
+ _symbolic _____ 17CoreSpeechExclave34SiriVoiceTriggerBargeInStartOptionO
+ _symbolic _____ 17CoreSpeechExclave34VoiceTriggerSecondPassResultFailedO
+ _symbolic _____ 17CoreSpeechExclave39SiriVoiceTriggerSecondPassOptionPrivateV
+ _symbolic _____ 17CoreSpeechExclave41BargeInVoiceTriggerResultTriggeredPrivateV
+ _symbolic _____ 17CoreSpeechExclave43VoiceTriggerSecondPassResultRejectedPrivateV
+ _symbolic _____ 17CoreSpeechExclave44VoiceTriggerSecondPassResultTriggeredPrivateV
+ _tb_message_raw_decode_f32
+ _type_layout_string 17CoreSpeechExclave24WriteBufferResultPrivateV
+ _type_layout_string 17CoreSpeechExclave26RaiseToSpeakPolicyDecisionV
+ _type_layout_string 17CoreSpeechExclave28AOPVoiceTriggerResultPrivateV
+ _type_layout_string 17CoreSpeechExclave30SpeakerProfileEmbeddingPrivateV
+ _type_layout_string 17CoreSpeechExclave33RaiseToSpeakPolicyDecisionPrivateV
+ _type_layout_string 17CoreSpeechExclave39SiriVoiceTriggerSecondPassOptionPrivateV
+ _type_layout_string 17CoreSpeechExclave41BargeInVoiceTriggerResultTriggeredPrivateV
+ _type_layout_string 17CoreSpeechExclave43VoiceTriggerSecondPassResultRejectedPrivateV
+ _type_layout_string 17CoreSpeechExclave44VoiceTriggerSecondPassResultTriggeredPrivateV
- -[CSSecureSiriAudioProvidingProxy init]
- GCC_except_table19
- GCC_except_table22
- GCC_except_table33
- GCC_except_table35
- GCC_except_table46
- GCC_except_table50
- GCC_except_table53
- ___block_descriptor_40_e8_32bs_e53_v24?0{corespeechexclave_aopvoicetriggerresult_s=QB}8ls32l8
- ___block_descriptor_40_e8_32r_e123_v32?0{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}8lr32l8
- ___block_descriptor_40_e8_32r_e488_v72?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}8lr32l8
- ___block_descriptor_40_e8_32r_e49_v16?0{corespeechexclave_writebufferresult_s=II}8lr32l8
- ___block_descriptor_48_e8_32s40bs_e58_v16?0{corespeechexclave_siriassetconfigurationerror_s=Q}8ls40l8s32l8
- ___swift_memcpy12_8
- ___swift_memcpy42_8
- _objc_release_x22
- _objc_retainAutoreleasedReturnValue
- _swift_release
CStrings:
+ "!"
+ "CoreSpeechExclave.CSSecureAOEAudioProvidingProxy"
+ "Operation not supported on non AOE devices"
+ "Service name is nil or zero length. Not initializing TB service"
+ "Starting RaiseToSpeak fastpath"
+ "Stopping RaiseToSpeak fastpath"
+ "fetchAndStoreAudioBufferWithHostTime not supported for non-AoE, calling regular version"
+ "init()"
+ "init(serviceName:)"
+ "v16@?0{corespeechexclave_siriassetconfigurationerrorprivate_s=Q}8"
+ "v16@?0{corespeechexclave_writebufferresultprivate_s=II}8"
+ "v24@?0{corespeechexclave_aopvoicetriggerresultprivate_s=QB}8"
+ "v32@?0{corespeechexclave_raisetospeakresultprivate_s=Q(?={?={corespeechexclave_raisetospeakpolicydecisionprivate_s=Bfd}})}8"
+ "v40@?0{corespeechexclave_bargeinvoicetriggerresultprivate_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggeredprivate_s=QIQ}})}8"
+ "v88@?0{corespeechexclave_voicetriggersecondpassresultprivate_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggeredprivate_s=QdIQQQQ{corespeechexclave_voicetriggerkeyworddetectionresultprivate_s=Q}{corespeechexclave_voicetriggerpersonalizationresultprivate_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejectedprivate_s=I{corespeechexclave_voicetriggerkeyworddetectionresultprivate_s=Q}{corespeechexclave_voicetriggerpersonalizationresultprivate_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailedprivate_s=Q}})}8"
- "@16@0:8"
- "B16@0:8"
- "B48@0:8@16Q24Q32Q40"
- "CSSecureSiriAudioProvidingProxy"
- "Q16@0:8"
- "Q24@0:8Q16"
- "Q24@0:8{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}16"
- "Q24@0:8{corespeechexclave_voicetriggerpersonalizationresult_s=Q}16"
- "Q40@0:8{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}16"
- "Q80@0:8{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}16"
- "UTF8String"
- "^{tb_endpoint_s=(?=[96c]^v)}"
- "_TtC17CoreSpeechExclave23SiriVoiceTriggerService"
- "_TtCC17CoreSpeechExclave23SiriVoiceTriggerService6Server"
- "_TtCC17CoreSpeechExclave23SiriVoiceTriggerService7Service"
- "_service"
- "_tightbeamEndpoint"
- "adBlockerMatchingInProgress:"
- "adBlockerReset"
- "bytes"
- "caseInsensitiveCompare:"
- "com.apple.corespeechd.SiriVoiceTriggerService"
- "configAOPVoiceTrigger"
- "connection"
- "convertAssetConfigurationError:"
- "convertSecureBargeInVoiceTriggerResultType:"
- "convertSecureSecondPassVoiceTriggerResultType:"
- "convertSecureSpeakerRecognitionType:"
- "convertSecureVoiceTriggerKeywordDetectionResultType:"
- "convertSecureVoiceTriggerSpeakerDetectionResultType:"
- "currentHandler"
- "deinitializeSecondPass"
- "fetchAOPVoiceTriggerResult:"
- "fetchAndStoreAudioBuffer"
- "handleFailureInFunction:file:lineNumber:description:"
- "init"
- "initializeSecondPass"
- "prepare"
- "processBargeInVoiceTrigger"
- "processBargeInVoiceTriggerWithResult:"
- "processSecondPassVoiceTriggerWithShouldFlushAudio:result:"
- "requestHistoricalAudioBufferWithStartSample:completion:"
- "reset"
- "resetFirstPassVoiceTrigger"
- "setAdBlockerAsset:"
- "setAssetForLocale:isOTA:completion:"
- "setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:"
- "startAdBlockerMatching"
- "startBargeInVoiceTrigger"
- "startSecondPassVoiceTriggerWithStartOption:"
- "startSecureAdBlockerMobileAssetLoaderService:"
- "startSecureMobileAssetLoaderService:completion:"
- "stopAdBlockerMatching"
- "stopBargeInVoiceTrigger"
- "stopSecondPassVoiceTrigger"
- "stopSecureAdBlockerMobileAssetLoaderService:"
- "stopSecureMobileAssetLoaderService:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithUTF8String:"
- "v16@0:8"
- "v16@?0{corespeechexclave_siriassetconfigurationerror_s=Q}8"
- "v16@?0{corespeechexclave_writebufferresult_s=II}8"
- "v24@0:8@?16"
- "v24@?0{corespeechexclave_aopvoicetriggerresult_s=QB}8"
- "v28@0:8B16@?20"
- "v32@0:8Q16@?24"
- "v32@0:8{?=QBBI}16"
- "v32@?0{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}8"
- "v36@0:8@16B24@?28"
- "v72@?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIQQ{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultrejected_s=I{corespeechexclave_voicetriggerkeyworddetectionresult_s=Q}{corespeechexclave_voicetriggerpersonalizationresult_s=Q}}}{?={corespeechexclave_voicetriggersecondpassresultfailed_s=Q}})}8"
- "{corespeechexclave_sirivoicetriggerservice_s=\"connection\"^{tb_connection_s}}"

```
