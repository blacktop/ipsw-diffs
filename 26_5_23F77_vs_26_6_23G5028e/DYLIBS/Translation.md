## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-365.13.0.0.0
-  __TEXT.__text: 0x5c6c4
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x5810
+365.14.0.0.0
+  __TEXT.__text: 0x5cec4
+  __TEXT.__auth_stubs: 0x1330
+  __TEXT.__objc_methlist: 0x58e8
   __TEXT.__const: 0xf88
-  __TEXT.__cstring: 0x30d4
-  __TEXT.__oslogstring: 0x4b36
+  __TEXT.__cstring: 0x3104
+  __TEXT.__oslogstring: 0x4be6
   __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x627

   __TEXT.__swift5_types: 0x50
   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1c78
+  __TEXT.__unwind_info: 0x1c90
   __TEXT.__eh_frame: 0x8f8
-  __TEXT.__objc_classname: 0xc96
-  __TEXT.__objc_methname: 0xc0cd
+  __TEXT.__objc_classname: 0xcc6
+  __TEXT.__objc_methname: 0xc246
   __TEXT.__objc_methtype: 0x1f8e
-  __TEXT.__objc_stubs: 0x6cc0
-  __DATA_CONST.__got: 0x568
+  __TEXT.__objc_stubs: 0x6e00
+  __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0x1e48
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26e0
+  __DATA_CONST.__objc_selrefs: 0x2740
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH_CONST.__auth_got: 0x9a8
   __AUTH_CONST.__const: 0x1020
-  __AUTH_CONST.__cfstring: 0x3880
-  __AUTH_CONST.__objc_const: 0xb430
+  __AUTH_CONST.__cfstring: 0x3900
+  __AUTH_CONST.__objc_const: 0xb608
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1380
+  __AUTH.__objc_data: 0x13d0
   __AUTH.__data: 0x6b0
-  __DATA.__objc_ivar: 0x84c
+  __DATA.__objc_ivar: 0x860
   __DATA.__data: 0xbc0
   __DATA.__bss: 0x1090
   __DATA.__common: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF3ECD73-CA01-3149-A511-82966C882C9A
-  Functions: 2763
-  Symbols:   7710
-  CStrings:  3699
+  UUID: A3906CC0-8FE6-3678-B269-2877AF5125B6
+  Functions: 2782
+  Symbols:   7776
+  CStrings:  3728
 
Symbols:
+ +[_LTLanguageDetectionConfiguration supportsSecureCoding]
+ +[_LTTranslator languagesForText:configuration:completion:]
+ -[NSString(TranslationAdditions) lt_stringByReplacingInvalidUTF8Characters]
+ -[NSString(TranslationAdditions) lt_stringByReplacingInvalidUTF8Characters].cold.1
+ -[NSString(TranslationAdditions) lt_stringByReplacingInvalidUTF8Characters].cold.2
+ -[_LTLanguageDetectionConfiguration copyWithZone:]
+ -[_LTLanguageDetectionConfiguration encodeWithCoder:]
+ -[_LTLanguageDetectionConfiguration engineType]
+ -[_LTLanguageDetectionConfiguration initWithCoder:]
+ -[_LTLanguageDetectionConfiguration initWithTaskHint:]
+ -[_LTLanguageDetectionConfiguration model]
+ -[_LTLanguageDetectionConfiguration setEngineType:]
+ -[_LTLanguageDetectionConfiguration setModel:]
+ -[_LTLanguageDetectionConfiguration setStrategy:]
+ -[_LTLanguageDetectionConfiguration setUseDedicatedTextMachPort:]
+ -[_LTLanguageDetectionConfiguration strategy]
+ -[_LTLanguageDetectionConfiguration taskHint]
+ -[_LTLanguageDetectionConfiguration useDedicatedTextMachPort]
+ _OBJC_CLASS_$__LTLanguageDetectionConfiguration
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._engineType
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._model
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._strategy
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._taskHint
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._useDedicatedTextMachPort
+ _OBJC_METACLASS_$__LTLanguageDetectionConfiguration
+ _OUTLINED_FUNCTION_11
+ __OBJC_$_CLASS_METHODS__LTLanguageDetectionConfiguration
+ __OBJC_$_CLASS_PROP_LIST__LTLanguageDetectionConfiguration
+ __OBJC_$_INSTANCE_METHODS__LTLanguageDetectionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES__LTLanguageDetectionConfiguration
+ __OBJC_$_PROP_LIST__LTLanguageDetectionConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__LTLanguageDetectionConfiguration
+ __OBJC_CLASS_RO_$__LTLanguageDetectionConfiguration
+ __OBJC_METACLASS_RO_$__LTLanguageDetectionConfiguration
+ ___21-[_LTTranslator log:]_block_invoke.99
+ ___24-[_LTTranslator cleanup]_block_invoke.84
+ ___39-[_LTTranslator preheatForRequestSync:]_block_invoke.78
+ ___42+[_LTTranslator selfLoggingEventWithData:]_block_invoke.102
+ ___42-[_LTTranslator updateOVADStreamingState:]_block_invoke.109
+ ___46-[_LTTranslator preheatForRequest:completion:]_block_invoke.81
+ ___52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.95
+ ___54+[_LTTranslator selfLoggingInvocationCancelledForIDs:]_block_invoke.105
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke.65
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke.cold.1
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke_2
+ ___60+[_LTTranslator selfLoggingInvocationDidError:invocationId:]_block_invoke.106
+ ___65+[_LTTranslator _getServiceProxyWithDelegate:errorHandler:block:]_block_invoke.71
+ ___71+[_LTTranslator selfLoggingLanguageIdentificationCompletedWithLIDData:]_block_invoke.104
+ ___81+[_LTTranslator selfLoggingInvocationStartedWithData:invocationStartedTier1Data:]_block_invoke.103
+ ___94+[_LTTranslator _getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:]_block_invoke.75
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"<_LTTextTranslationService>"8?<v?>16ls32l8s40l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.77
+ ___block_literal_global.80
+ ___block_literal_global.83
+ ___block_literal_global.86
+ ___block_literal_global.98
+ _malloc_type_malloc
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$getCharacters:range:
+ _objc_msgSend$initWithCharactersNoCopy:length:freeWhenDone:
+ _objc_msgSend$initWithTaskHint:
+ _objc_msgSend$languagesForText:configuration:completion:
+ _objc_msgSend$model
+ _objc_msgSend$setEngineType:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setStrategy:
+ _objc_msgSend$setUseDedicatedTextMachPort:
+ _objc_msgSend$strategy
+ _objc_msgSend$useDedicatedTextMachPort
- ___21-[_LTTranslator log:]_block_invoke.98
- ___24-[_LTTranslator cleanup]_block_invoke.83
- ___39-[_LTTranslator preheatForRequestSync:]_block_invoke.77
- ___42+[_LTTranslator selfLoggingEventWithData:]_block_invoke.101
- ___42-[_LTTranslator updateOVADStreamingState:]_block_invoke.108
- ___46-[_LTTranslator preheatForRequest:completion:]_block_invoke.80
- ___52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.93
- ___54+[_LTTranslator selfLoggingInvocationCancelledForIDs:]_block_invoke.104
- ___60+[_LTTranslator selfLoggingInvocationDidError:invocationId:]_block_invoke.105
- ___65+[_LTTranslator _getServiceProxyWithDelegate:errorHandler:block:]_block_invoke.70
- ___71+[_LTTranslator selfLoggingLanguageIdentificationCompletedWithLIDData:]_block_invoke.103
- ___81+[_LTTranslator selfLoggingInvocationStartedWithData:invocationStartedTier1Data:]_block_invoke.102
- ___94+[_LTTranslator _getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:]_block_invoke.74
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke.64
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke.cold.1
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke_2
- ___block_descriptor_72_e8_32s40bs_e46_v24?0"<_LTTextTranslationService>"8?<v?>16ls32l8s40l8
- ___block_literal_global.107
- ___block_literal_global.76
- ___block_literal_global.79
- ___block_literal_global.82
- ___block_literal_global.85
- ___block_literal_global.97
- _objc_msgSend$languagesForText:usingModel:strategy:taskHint:completion:
- _objc_msgSend$languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:
CStrings:
+ "Failed to malloc a buffer for string, so can't replace invalid UTF8 characters. Using an empty string instead"
+ "String contains characters not encodable as UTF-8; replacing lone surrogates"
+ "TB,N,V_useDedicatedTextMachPort"
+ "TQ,N,V_model"
+ "TQ,N,V_strategy"
+ "Tq,N,V_engineType"
+ "_LTLanguageDetectionConfiguration"
+ "_model"
+ "_strategy"
+ "_useDedicatedTextMachPort"
+ "dataUsingEncoding:"
+ "getCharacters:range:"
+ "initWithCharactersNoCopy:length:freeWhenDone:"
+ "initWithTaskHint:"
+ "languagesForText:configuration:completion:"
+ "lt_stringByReplacingInvalidUTF8Characters"
+ "model"
+ "setEngineType:"
+ "setModel:"
+ "setStrategy:"
+ "setUseDedicatedTextMachPort:"
+ "strategy"
+ "useDedicatedTextMachPort"
+ "v40@0:8@\"NSArray\"16@\"_LTLanguageDetectionConfiguration\"24@?<v@?@\"_LTTextLanguageDetectionResult\">32"
- "languagesForText:usingModel:strategy:taskHint:completion:"
- "v56@0:8@\"NSArray\"16Q24Q32q40@?<v@?@\"_LTTextLanguageDetectionResult\">48"
- "v56@0:8@16Q24Q32q40@?48"

```
