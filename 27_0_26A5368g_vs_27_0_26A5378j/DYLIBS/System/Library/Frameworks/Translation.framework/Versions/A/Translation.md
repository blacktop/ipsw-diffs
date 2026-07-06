## Translation

> `/System/Library/Frameworks/Translation.framework/Versions/A/Translation`

```diff

-  __TEXT.__text: 0x61444
-  __TEXT.__objc_methlist: 0x5ba0
+  __TEXT.__text: 0x61e14
+  __TEXT.__objc_methlist: 0x5cb0
   __TEXT.__const: 0xfa0
-  __TEXT.__cstring: 0x3344
-  __TEXT.__oslogstring: 0x5146
+  __TEXT.__cstring: 0x33b4
+  __TEXT.__oslogstring: 0x5176
   __TEXT.__gcc_except_tab: 0xb44
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x639

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x84
-  __TEXT.__unwind_info: 0x1c28
+  __TEXT.__unwind_info: 0x1c58
   __TEXT.__eh_frame: 0x8c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x680
-  __DATA_CONST.__objc_classlist: 0x318
+  __DATA_CONST.__const: 0x698
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2840
+  __DATA_CONST.__objc_selrefs: 0x2850
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__got: 0x5a8
-  __AUTH_CONST.__const: 0x2bd0
-  __AUTH_CONST.__cfstring: 0x3c20
-  __AUTH_CONST.__objc_const: 0xbb58
+  __DATA_CONST.__got: 0x5c0
+  __AUTH_CONST.__const: 0x2c00
+  __AUTH_CONST.__cfstring: 0x3c80
+  __AUTH_CONST.__objc_const: 0xbde0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x920
-  __AUTH.__objc_data: 0x98
+  __AUTH.__objc_data: 0x48
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0x8a0
+  __DATA.__objc_ivar: 0x8b0
   __DATA.__data: 0xba0
-  __DATA.__bss: 0x1070
+  __DATA.__bss: 0x1060
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x1dd8
+  __DATA_DIRTY.__objc_data: 0x1ec8
   __DATA_DIRTY.__data: 0x3a8
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xc0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2899
-  Symbols:   5665
-  CStrings:  1387
+  Functions: 2920
+  Symbols:   5709
+  CStrings:  1394
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[_LTNullableLocalePair supportsSecureCoding]
+ +[_LTSELFLoggingTranslateAPIContext supportsSecureCoding]
+ +[_LTTranslator selfLoggingInvocationCancelledForIDs:localePair:]
+ +[_LTTranslator selfLoggingInvocationDidError:invocationId:localePair:]
+ -[_LTLanguageStatusConfiguration multicastKey]
+ -[_LTNullableLocalePair .cxx_destruct]
+ -[_LTNullableLocalePair copyWithZone:]
+ -[_LTNullableLocalePair encodeWithCoder:]
+ -[_LTNullableLocalePair initWithCoder:]
+ -[_LTNullableLocalePair initWithLocalePair:]
+ -[_LTNullableLocalePair initWithSourceLocale:targetLocale:]
+ -[_LTNullableLocalePair localePair]
+ -[_LTNullableLocalePair sourceLocale]
+ -[_LTNullableLocalePair targetLocale]
+ -[_LTSELFLoggingInvocationOptions initWithTask:inputMode:invocationType:translateAPIContext:]
+ -[_LTSELFLoggingInvocationOptions translateAPIContext]
+ -[_LTSELFLoggingTranslateAPIContext .cxx_destruct]
+ -[_LTSELFLoggingTranslateAPIContext encodeWithCoder:]
+ -[_LTSELFLoggingTranslateAPIContext initWithCoder:]
+ -[_LTSELFLoggingTranslateAPIContext initWithLocalePair:]
+ -[_LTSELFLoggingTranslateAPIContext localePair]
+ GCC_except_table35
+ OBJC_IVAR_$__LTNullableLocalePair._sourceLocale
+ OBJC_IVAR_$__LTNullableLocalePair._targetLocale
+ OBJC_IVAR_$__LTSELFLoggingInvocationOptions._translateAPIContext
+ OBJC_IVAR_$__LTSELFLoggingTranslateAPIContext._localePair
+ _OBJC_CLASS_$__LTNullableLocalePair
+ _OBJC_CLASS_$__LTSELFLoggingTranslateAPIContext
+ _OBJC_METACLASS_$__LTNullableLocalePair
+ _OBJC_METACLASS_$__LTSELFLoggingTranslateAPIContext
+ __65+[_LTTranslator selfLoggingInvocationCancelledForIDs:localePair:]_block_invoke
+ __71+[_LTTranslator selfLoggingInvocationDidError:invocationId:localePair:]_block_invoke
+ __OBJC_$_CLASS_METHODS__LTNullableLocalePair
+ __OBJC_$_CLASS_METHODS__LTSELFLoggingTranslateAPIContext
+ __OBJC_$_CLASS_PROP_LIST__LTNullableLocalePair
+ __OBJC_$_CLASS_PROP_LIST__LTSELFLoggingTranslateAPIContext
+ __OBJC_$_INSTANCE_METHODS__LTNullableLocalePair
+ __OBJC_$_INSTANCE_METHODS__LTSELFLoggingTranslateAPIContext
+ __OBJC_$_INSTANCE_VARIABLES__LTNullableLocalePair
+ __OBJC_$_INSTANCE_VARIABLES__LTSELFLoggingTranslateAPIContext
+ __OBJC_$_PROP_LIST__LTNullableLocalePair
+ __OBJC_$_PROP_LIST__LTSELFLoggingTranslateAPIContext
+ __OBJC_CLASS_PROTOCOLS_$__LTNullableLocalePair
+ __OBJC_CLASS_PROTOCOLS_$__LTSELFLoggingTranslateAPIContext
+ __OBJC_CLASS_RO_$__LTNullableLocalePair
+ __OBJC_CLASS_RO_$__LTSELFLoggingTranslateAPIContext
+ __OBJC_METACLASS_RO_$__LTNullableLocalePair
+ __OBJC_METACLASS_RO_$__LTSELFLoggingTranslateAPIContext
+ ___65+[_LTTranslator selfLoggingInvocationCancelledForIDs:localePair:]_block_invoke
+ ___71+[_LTTranslator selfLoggingInvocationDidError:invocationId:localePair:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e46_v24?0"<_LTTextTranslationService>"8?<v?>16l
+ _objc_msgSend$initWithTask:inputMode:invocationType:translateAPIContext:
+ _objc_msgSend$multicastKey
+ _objc_msgSend$selfLoggingInvocationCancelledForIDs:localePair:
+ _objc_msgSend$selfLoggingInvocationDidError:invocationId:localePair:
+ _unexpectedEngineTypeException
- +[_LTTranslator selfLoggingInvocationCancelledForIDs:]
- +[_LTTranslator selfLoggingInvocationDidError:invocationId:]
- GCC_except_table36
- GCC_except_table40
- GCC_except_table46
- __54+[_LTTranslator selfLoggingInvocationCancelledForIDs:]_block_invoke
- __60+[_LTTranslator selfLoggingInvocationDidError:invocationId:]_block_invoke
- ___54+[_LTTranslator selfLoggingInvocationCancelledForIDs:]_block_invoke
- ___60+[_LTTranslator selfLoggingInvocationDidError:invocationId:]_block_invoke
- __keyForConfig
- _objc_msgSend$initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:languageIdentificationEnabled:
- _objc_msgSend$initWithLocaleIdentifier:
- _objc_msgSend$selfLoggingInvocationCancelledForIDs:
- _objc_msgSend$selfLoggingInvocationDidError:invocationId:
CStrings:
+ "2"
+ "Observation multicast for key '%{public}@': [%{public}@]"
+ "Observation replay for key '%{public}@': [%{public}@]"
+ "Received an unexpected on device engine type %zu"
+ "_LTUnexpectedOnDeviceEngineTypeException"
+ "translateAPIContext"
- "Obsv mlcast for key '%{public}@': [%@]"
- "Obsv replay [%{public}@]"

```
