## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

```diff

-3505.12.1.1.1
-  __TEXT.__text: 0x40d48
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x3724
+3505.20.1.1.1
+  __TEXT.__text: 0x4131c
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x375c
   __TEXT.__const: 0x7e8
-  __TEXT.__cstring: 0x5083
+  __TEXT.__cstring: 0x5123
   __TEXT.__oslogstring: 0x3a2c
   __TEXT.__gcc_except_tab: 0x9e0
   __TEXT.__ustring: 0x22

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_capture: 0x194
+  __TEXT.__swift5_capture: 0x198
   __TEXT.__unwind_info: 0x1238
   __TEXT.__eh_frame: 0x578
   __TEXT.__objc_classname: 0x7a1
-  __TEXT.__objc_methname: 0xaa65
-  __TEXT.__objc_methtype: 0x180d
-  __TEXT.__objc_stubs: 0x70a0
-  __DATA_CONST.__got: 0x6f0
+  __TEXT.__objc_methname: 0xab2d
+  __TEXT.__objc_methtype: 0x1828
+  __TEXT.__objc_stubs: 0x7100
+  __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__objc_classlist: 0x1d8
-  __DATA_CONST.__objc_catlist: 0x150
+  __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2670
+  __DATA_CONST.__objc_selrefs: 0x2688
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0xaf8
   __AUTH_CONST.__cfstring: 0x1e00
-  __AUTH_CONST.__objc_const: 0x6268
+  __AUTH_CONST.__objc_const: 0x6308
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa08
   __AUTH.__data: 0x368
-  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0xa60
   __DATA.__bss: 0x6a0
   __DATA.__common: 0x48

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 087BD493-30CB-3E87-B340-F8658D685C11
-  Functions: 1641
-  Symbols:   5051
-  CStrings:  2941
+  UUID: 71ABE253-0A35-33E7-A00F-781C3122D1F7
+  Functions: 1646
+  Symbols:   5065
+  CStrings:  2950
 
Symbols:
+ -[SRUIFSpeechSynthesisRequest promptStyle]
+ -[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]
+ -[SRUIFSpeechSynthesisTask voicePromptStyle]
+ -[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]
+ -[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:].cold.1
+ -[SRUIFSpeechSynthesizer enqueueText:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:]
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._promptStyle
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisTask._voicePromptStyle
+ _SAVoicePromptStyleDefaultValue
+ _SAVoicePromptStyleHighValue
+ _SAVoicePromptStyleMildValue
+ __CATEGORY_INSTANCE_METHODS_SiriTTSSpeechRequest_$_SiriUIFoundation
+ __CATEGORY_SiriTTSSpeechRequest_$_SiriUIFoundation
+ ___263-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke
+ ___263-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke.2
+ ___263-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2
+ ___267-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke
+ ___267-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke.55
+ ___267-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke.59
+ ___86-[SRUIFInstrumentationManager boostQueuedMessagesAndPerformOnQueueCompletion:timeout:]_block_invoke.97
+ ___Block_byref_object_copy_.94
+ ___Block_byref_object_dispose_.95
+ ___block_descriptor_80_e8_32s40s48bs56bs64w72w_e21_v16?0"AFVoiceInfo"8lw64l8w72l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.12
+ ___block_literal_global.14
+ _objc_msgSend$_enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:
+ _objc_msgSend$initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:
+ _objc_msgSend$initWithText:voice:promptStyle:
+ _objc_msgSend$promptStyle
+ _objc_msgSend$voicePromptStyle
- -[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]
- -[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]
- -[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:].cold.1
- -[SRUIFSpeechSynthesizer enqueueText:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:]
- ___246-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke
- ___246-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke.2
- ___246-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2
- ___255-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke
- ___255-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke.55
- ___255-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke.59
- ___86-[SRUIFInstrumentationManager boostQueuedMessagesAndPerformOnQueueCompletion:timeout:]_block_invoke.94
- ___Block_byref_object_copy_.91
- ___Block_byref_object_dispose_.92
- ___block_descriptor_80_e8_32s40s48bs56bs64w72w_e21_v16?0"AFVoiceInfo"8lw64l8w72l8s32l8s48l8s56l8s40l8
- ___block_literal_global.11
- ___block_literal_global.13
- _objc_msgSend$_enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:
- _objc_msgSend$initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:
CStrings:
+ "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]"
+ "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke"
+ "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2"
+ "-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]"
+ "-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke"
+ "<%@ %p; text=\"%@\"; identifier=%@; sessionId=%@; delayed=%@; provisional=%@; eligibleForProcessing=%@; eligibleForSynthesis=%@; canUseServerTTS=%@; language=%@; gender=%@; voicePromptStyle=%@; audioByteCount=%@; error=%@; completion=%p>"
+ "@140@0:8@16@24@32@40@48@56@64@72B80d84B92@?96@?104@112@120B128@132"
+ "T@\"NSString\",R,N,V_promptStyle"
+ "T@\"NSString\",R,N,V_voicePromptStyle"
+ "_enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:"
+ "_promptStyle"
+ "_voicePromptStyle"
+ "enqueueText:identifier:sessionId:preferredVoice:language:gender:promptStyle:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:"
+ "initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:voicePromptStyle:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:"
+ "initWithText:voice:promptStyle:"
+ "promptStyle"
+ "v128@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"SAVoice\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64B72B76d80B88B92@\"NSString\"96@?<v@?q@\"NSError\">104@\"NSDictionary\"112@\"NSDictionary\"120"
+ "v128@0:8@16@24@32@40@48@56@64B72B76d80B88B92@96@?104@112@120"
+ "v140@0:8@16@24@32@40@48@56@64@72B80B84d88B96B100@104B112@?116@124@132"
+ "voicePromptStyle"
+ "\xd1"
- "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]"
- "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke"
- "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2"
- "-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]"
- "-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke"
- "<%@ %p; text=\"%@\"; identifier=%@; sessionId=%@; delayed=%@; provisional=%@; eligibleForProcessing=%@; eligibleForSynthesis=%@; canUseServerTTS=%@; language=%@; gender=%@; audioByteCount=%@; error=%@; completion=%p>"
- "@132@0:8@16@24@32@40@48@56@64B72d76B84@?88@?96@104@112B120@124"
- "_enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:"
- "enqueueText:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:"
- "initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:"
- "v120@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"SAVoice\"40@\"NSString\"48@\"NSString\"56B64B68d72B80B84@\"NSString\"88@?<v@?q@\"NSError\">96@\"NSDictionary\"104@\"NSDictionary\"112"
- "v120@0:8@16@24@32@40@48@56B64B68d72B80B84@88@?96@104@112"
- "v132@0:8@16@24@32@40@48@56@64B72B76d80B88B92@96B104@?108@116@124"
- "\xc1"

```
