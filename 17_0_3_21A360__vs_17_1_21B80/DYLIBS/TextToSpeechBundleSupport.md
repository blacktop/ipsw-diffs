## TextToSpeechBundleSupport

> `/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport`

```diff

-580.4.0.0.0
-  __TEXT.__text: 0x38f1c
+583.1.4.0.0
+  __TEXT.__text: 0x39624
   __TEXT.__auth_stubs: 0x1f10
-  __TEXT.__objc_methlist: 0x12e8
+  __TEXT.__objc_methlist: 0x1318
   __TEXT.__const: 0xd0a
-  __TEXT.__gcc_except_tab: 0x1abc
-  __TEXT.__cstring: 0x4234
-  __TEXT.__ustring: 0x13b8
-  __TEXT.__oslogstring: 0xde9
+  __TEXT.__gcc_except_tab: 0x1bc0
+  __TEXT.__cstring: 0x4284
+  __TEXT.__ustring: 0x13c4
+  __TEXT.__oslogstring: 0xe33
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__swift5_typeref: 0x35e
   __TEXT.__swift5_capture: 0xec

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x38
-  __TEXT.__unwind_info: 0xf8c
+  __TEXT.__unwind_info: 0xfd0
   __TEXT.__eh_frame: 0x168
   __TEXT.__objc_classname: 0x1db
-  __TEXT.__objc_methname: 0x47dc
+  __TEXT.__objc_methname: 0x4876
   __TEXT.__objc_methtype: 0xe21
-  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_stubs: 0x36a0
   __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x6e0
+  __DATA_CONST.__const: 0x730
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28f0
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_const: 0x2920
+  __DATA_CONST.__objc_selrefs: 0x1180
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__cfstring: 0x3940
+  __AUTH_CONST.__cfstring: 0x39a0
   __AUTH_CONST.__const: 0x1080
   __AUTH_CONST.__objc_const: 0x5a0
   __AUTH_CONST.__objc_arrayobj: 0x60

   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x1f0
   __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x208
+  __DATA.__objc_ivar: 0x20c
   __DATA.__objc_data: 0x18
   __DATA.__data: 0xa70
   __DATA.__objc_stublist: 0x8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5B95A2E1-0300-3DE8-95D0-23DBD8A0506F
-  Functions: 1281
-  Symbols:   3636
-  CStrings:  2329
+  UUID: 90FAC927-0633-319D-9D19-AB3B1D2B38EB
+  Functions: 1289
+  Symbols:   3662
+  CStrings:  2343
 
Symbols:
+ -[TTSSiriSynthWrapper _applyPostRuleRewrites:]
+ -[TTSSiriSynthWrapper _rawLiteralCharacterRegexForCurrentLanguage]
+ -[TTSSiriSynthWrapper initWithVoicePath:language:delegate:]
+ -[TTSSiriSynthWrapper initWithVoicePath:language:delegate:].cold.1
+ -[TTSSiriSynthWrapper initWithVoicePath:language:delegate:].cold.2
+ -[TTSSiriSynthWrapper language]
+ -[TTSSiriSynthWrapper loadVoiceResource:].cold.1
+ -[TTSSiriSynthWrapper processedSpeechString]
+ -[TTSSiriSynthWrapper setLanguage:]
+ -[TTSSiriSynthWrapper setProcessedSpeechString:]
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table57
+ GCC_except_table69
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._language
+ _OBJC_IVAR_$_TTSSiriSynthWrapper._processedSpeechString
+ ___46-[TTSSiriSynthWrapper _applyPostRuleRewrites:]_block_invoke
+ ___46-[TTSSiriSynthWrapper _applyPostRuleRewrites:]_block_invoke_2
+ ___block_descriptor_48_ea8_32s40s_e37_v32?0"NSTextCheckingResult"8Q16^B24ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e37_v32?0"NSTextCheckingResult"8Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.168
+ _objc_msgSend$_applyPostRuleRewrites:
+ _objc_msgSend$_rawLiteralCharacterRegexForCurrentLanguage
+ _objc_msgSend$originalString
+ _objc_msgSend$processedSpeechString
+ _objc_msgSend$setProcessedSpeechString:
- -[TTSSiriSynthWrapper initWithVoicePath:delegate:]
- -[TTSSiriSynthWrapper initWithVoicePath:delegate:].cold.1
- -[TTSSiriSynthWrapper proccessedSpeechString]
- -[TTSSiriSynthWrapper setProccessedSpeechString:]
- GCC_except_table24
- GCC_except_table63
- _OBJC_IVAR_$_TTSSiriSynthWrapper._proccessedSpeechString
- _objc_msgSend$proccessedSpeechString
- _objc_msgSend$setProccessedSpeechString:
CStrings:
+ "\x11'"
+ "\x1b\\tn=raw\\%@\x1b\\tn=spell\\"
+ "((?<=(\\\\!|\\x1B)\\\\tn=spell\\\\)[\\s\\S]*?(?=((\\\\!|\\x1B)\\\\tn=)|$))"
+ "Siri resource load exception."
+ "SiriTTSSynthesizer initialization exception"
+ "T@\"<TTSSiriSynthWrapperDelegate>\",W,N,V_delegate"
+ "T@\"NSString\",&,N,V_language"
+ "T@\"TTSSpeechString\",&,N,V_processedSpeechString"
+ "_applyPostRuleRewrites:"
+ "_language"
+ "_processedSpeechString"
+ "_rawLiteralCharacterRegexForCurrentLanguage"
+ "initWithVoicePath:language:delegate:"
+ "originalString"
+ "primaryLanguages"
+ "processedSpeechString"
+ "setLanguage:"
+ "setProcessedSpeechString:"
- "\x11\x17"
- "T@\"<TTSSiriSynthWrapperDelegate>\",&,N,V_delegate"
- "T@\"TTSSpeechString\",&,N,V_proccessedSpeechString"
- "_proccessedSpeechString"
- "initWithVoicePath:delegate:"
- "proccessedSpeechString"
- "setProccessedSpeechString:"

```
