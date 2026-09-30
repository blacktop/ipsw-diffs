## localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

-3404.69.2.0.0
-  __TEXT.__text: 0x3cd38
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0x29a0
-  __TEXT.__objc_methlist: 0x1514
-  __TEXT.__const: 0x1010
-  __TEXT.__cstring: 0x3a9b
-  __TEXT.__objc_methname: 0x5055
-  __TEXT.__constg_swiftt: 0x1788
-  __TEXT.__swift5_typeref: 0xad7
+3404.77.1.0.0
+  __TEXT.__text: 0x4169c
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_stubs: 0x29e0
+  __TEXT.__objc_methlist: 0x152c
+  __TEXT.__const: 0x1018
+  __TEXT.__cstring: 0x3b53
+  __TEXT.__objc_methname: 0x52e5
+  __TEXT.__constg_swiftt: 0x17b8
+  __TEXT.__swift5_typeref: 0xb15
   __TEXT.__swift5_reflstr: 0xe63
   __TEXT.__swift5_fieldmd: 0xa48
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x94
   __TEXT.__objc_classname: 0x278
-  __TEXT.__objc_methtype: 0x197e
+  __TEXT.__objc_methtype: 0x1982
   __TEXT.__swift5_capture: 0x15c
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__gcc_except_tab: 0x550
-  __TEXT.__unwind_info: 0xe38
-  __TEXT.__eh_frame: 0xb30
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x6f8
+  __TEXT.__unwind_info: 0xe40
+  __TEXT.__eh_frame: 0xb58
+  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__got: 0x720
   __DATA_CONST.__auth_ptr: 0x290
   __DATA_CONST.__const: 0xeb0
-  __DATA_CONST.__cfstring: 0x720
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2fd0
-  __DATA.__objc_selrefs: 0x14b8
+  __DATA.__objc_const: 0x2fd8
+  __DATA.__objc_selrefs: 0x1558
   __DATA.__objc_ivar: 0x90
-  __DATA.__objc_data: 0x1388
-  __DATA.__data: 0x2738
+  __DATA.__objc_data: 0x1398
+  __DATA.__data: 0x2798
   __DATA.__bss: 0xd88
   __DATA.__common: 0x208
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1227
-  Symbols:   443
-  CStrings:  1514
+  Functions: 1270
+  Symbols:   450
+  CStrings:  1539
 
Symbols:
+ _OBJC_CLASS_$_ASRSchemaASRLMEOverActivationEdit
+ _OBJC_CLASS_$_ASRSchemaASRNamedEntityUserEdit
+ _OBJC_CLASS_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ _OBJC_CLASS_$__EARSpeechMessagesContext
+ _OBJC_CLASS_$__EARVisualContextEvaluation
+ _OBJC_CLASS_$__EARVisualContextMetrics
+ _objc_retain_x4
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "%@ Config Path: %@"
+ "+[LSRConnection completionWithEuclidErrorWithDescription:configPath:completion:]"
+ "EARSpeechRecognizer.%s clearing the configured speech profile."
+ "Euclid not available on this device for this locale"
+ "Euclid not available on this device for this locale."
+ "Failed to create ASRSchemaASRNamedEntityUserEdit"
+ "NT-savedactivity"
+ "SELF: visual context metrics: %s"
+ "Unsupported entity tagger category: %s"
+ "Unsupported speech profile category: %s"
+ "Unsupported visual context category: %s"
+ "Vv64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSUUID\"40@\"NSString\"48@?<v@?B>56"
+ "completionWithEuclidErrorWithDescription:configPath:completion:"
+ "computeContextualizationMetricsWithMesssagesContext:correctedText:recognizedText:profilePath:"
+ "entityTaggerCategory"
+ "evaluateMessagesContext(_:recognizedText:correctedText:asrID:speechProfilePath:reply:)"
+ "evaluateMessagesContext:recognizedText:correctedText:asrID:speechProfilePath:reply:"
+ "lmeOverActivationEdits"
+ "namedEntityUserEdits"
+ "setEntityTaggerCategory:"
+ "setIsNamedEntityPresentInSpeechProfile:"
+ "setIsNamedEntityPresentInVisualContext:"
+ "setLmeOverActivationEdits:"
+ "setMessages:"
+ "setNamedEntityUserEdits:"
+ "setNumTotalEdit:"
+ "setPersonalizationUserEditNamedEntityMetrics:"
+ "setSender:"
+ "setSpeechProfileCategories:"
+ "setSpeechProfileCategory:"
+ "setVisualContextCategories:"
+ "speechProfileCategories"
+ "speechRecognizerDidProduceLoggableMultiUserPackages:"
+ "visualContextCategories"
- "EARSpeechRecognizer.%s clearing recognizer profiles"
- "MUX: %ld speech profiles are cached. %ld are available to be loaded"
- "MUX: EARSpeechRecognizer prepareForReuse speechProfileContainers size=%ld"
- "No accessible config at path: %@"
- "Received messagesContext:%s recognizedText:%s correctedText:%s asrID:%s speechProfilePath:%s"
- "Vv56@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSUUID\"40@\"NSString\"48"
- "Vv56@0:8@16@24@32@40@48"
- "evaluateMessagesContext(_:recognizedText:correctedText:asrID:speechProfilePath:)"
- "evaluateMessagesContext:recognizedText:correctedText:asrID:speechProfilePath:"
- "v56@0:8@16@24@32@40@48"

```
