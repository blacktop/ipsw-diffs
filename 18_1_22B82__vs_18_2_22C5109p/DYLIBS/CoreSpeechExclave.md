## CoreSpeechExclave

> `/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`

```diff

-3401.25.3.11.1
-  __TEXT.__text: 0x4e18
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0xec
-  __TEXT.__cstring: 0x757
-  __TEXT.__const: 0x290
-  __TEXT.__constg_swiftt: 0x17c
-  __TEXT.__swift5_typeref: 0x99
-  __TEXT.__swift5_fieldmd: 0xa4
-  __TEXT.__swift5_reflstr: 0x68
-  __TEXT.__swift5_assocty: 0x18
+3402.62.3.1.3
+  __TEXT.__text: 0x6d24
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0x164
+  __TEXT.__cstring: 0x65e
+  __TEXT.__const: 0x1e8
+  __TEXT.__constg_swiftt: 0x1d0
+  __TEXT.__swift5_typeref: 0x97
+  __TEXT.__swift5_fieldmd: 0x114
+  __TEXT.__swift5_reflstr: 0xf6
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__oslogstring: 0xdc
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__eh_frame: 0xa8
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__oslogstring: 0x15e
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x2fb
-  __TEXT.__objc_methtype: 0xf5
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x40
+  __TEXT.__objc_methname: 0x43b
+  __TEXT.__objc_methtype: 0x20a
+  __TEXT.__objc_stubs: 0x100
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__auth_ptr: 0xe0
-  __AUTH_CONST.__const: 0x90
-  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_ptr: 0x68
+  __AUTH_CONST.__const: 0x128
+  __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__objc_const: 0x2f8
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x38
-  __DATA.__bss: 0x388
+  __DATA.__data: 0x18
+  __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x1e0
+  __DATA_DIRTY.__data: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 87
-  Symbols:   135
-  CStrings:  118
+  Functions: 93
+  Symbols:   150
+  CStrings:  130
 
Symbols:
+ _objc_release_x25
+ _objc_retain
+ _objc_retain_x25
+ _swift_retain
+ _tb_endpoint_set_interface_identifier
+ _tb_message_configure_received
- _objc_release_x24
- _objc_retain_x24
- _swift_dynamicCast
- _swift_errorRelease
- _tb_message_configure_recieved
- _tb_message_decode_u8
CStrings:
+ "IsolatedCoreAudioClient BargeIn start"
+ "IsolatedCoreAudioClient BargeIn stop"
+ "IsolatedCoreAudioClient could not launch conclave with error %!d(MISSING)!!!"
+ "IsolatedCoreAudioClient process barge-in"
+ "Q16@0:8"
+ "Q24@0:8Q16"
+ "Q40@0:8{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}16"
+ "Q72@0:8{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIfffQQ}})}16"
+ "adBlockerMatchingInProgress:"
+ "convertAssetConfigurationError:"
+ "convertSecureBargeInVoiceTriggerResultType:"
+ "convertSecureSecondPassVoiceTriggerResultType:"
+ "convertSecureSpeakerRecognitionType:"
+ "illegal variant selector: "
+ "requestHistoricalAudioBufferWithStartSample:completion:"
+ "setAdBlockerAsset:"
+ "startAdBlockerMatching"
+ "startSecondPassVoiceTriggerWithStartOption:"
+ "startSecureAdBlockerMobileAssetLoaderService:"
+ "stopAdBlockerMatching"
+ "stopSecureAdBlockerMobileAssetLoaderService:"
+ "v16@?0{corespeechexclave_siriassetconfigurationerror_s=Q}8"
+ "v32@0:8Q16@?24"
+ "v32@0:8{?=QBBI}16"
+ "v32@?0{corespeechexclave_bargeinvoicetriggerresult_s=Q(?={?={corespeechexclave_bargeinvoicetriggerresulttriggered_s=QI}})}8"
+ "v64@?0{corespeechexclave_voicetriggersecondpassresult_s=Q(?={?={corespeechexclave_voicetriggersecondpassresulttriggered_s=QdIfffQQ}})}8"
+ "vi-VN"
- "I32@0:8Q16Q24"
- "IsolatedCoreAudioClient could not launch conclave!!!"
- "TB_ASSERT: (corespeechexclave_siriaudioprovidingerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: CoreSpeechExclave.SiriAudioProvidingError\""
- "i16@0:8"
- "invalid rawValue for SiriLocale "
- "invalid rawValue for SiriVoiceTriggerFirstPassSource "
- "invalid rawValue for SpeakerRecognizerType "
- "prepare threw an unexpected error type"
- "requestHistoricalAudioBufferWithStartSample:numSamples:"
- "startSecondPassVoiceTriggerFromOrigin:enablePHS:supportMultiPhrase:"
- "v12@?0I8"
- "v16@?0{corespeechexclave_bargeinvoicetriggerresult_s=II}8"
- "v16@?0{corespeechexclave_sirivoicetriggerservice_prepare__result_s=C(?=IB)}8"
- "v32@0:8Q16B24B28"
- "v56@?0{corespeechexclave_voicetriggersecondpassresult_s=IIdIfffQQ}8"

```
