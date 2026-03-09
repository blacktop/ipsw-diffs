## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x5bb0c
+365.8.0.0.0
+  __TEXT.__text: 0x5c514
   __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x5760
+  __TEXT.__objc_methlist: 0x5810
   __TEXT.__const: 0xf88
-  __TEXT.__cstring: 0x3064
-  __TEXT.__oslogstring: 0x4a66
-  __TEXT.__gcc_except_tab: 0xb70
+  __TEXT.__cstring: 0x30d4
+  __TEXT.__oslogstring: 0x4b06
+  __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x627
   __TEXT.__swift5_capture: 0x19c

   __TEXT.__swift5_types: 0x50
   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1c48
+  __TEXT.__unwind_info: 0x1c78
   __TEXT.__eh_frame: 0x8f8
   __TEXT.__objc_classname: 0xc96
-  __TEXT.__objc_methname: 0xbded
-  __TEXT.__objc_methtype: 0x1efe
-  __TEXT.__objc_stubs: 0x6be0
+  __TEXT.__objc_methname: 0xc0cd
+  __TEXT.__objc_methtype: 0x1f8e
+  __TEXT.__objc_stubs: 0x6cc0
   __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x1df8
+  __DATA_CONST.__const: 0x1e48
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2688
+  __DATA_CONST.__objc_selrefs: 0x26e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x280
-  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x9a0
   __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0xb340
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__cfstring: 0x3880
+  __AUTH_CONST.__objc_const: 0xb430
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1380
   __AUTH.__data: 0x6b0
-  __DATA.__objc_ivar: 0x838
+  __DATA.__objc_ivar: 0x84c
   __DATA.__data: 0xbc0
   __DATA.__bss: 0x1080
   __DATA.__common: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0B1920EC-D920-3AF6-A718-5FEAD7DAFA25
-  Functions: 2744
-  Symbols:   7652
-  CStrings:  3655
+  UUID: D6547EB3-527C-337F-8EEB-840B841F54C0
+  Functions: 2760
+  Symbols:   7701
+  CStrings:  3697
 
Symbols:
+ +[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]
+ -[NSLocale(LTLocaleIdentifier) _lt_displayNameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:]
+ -[NSLocale(LTLocaleIdentifier) _lt_displaySubnameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:]
+ -[_LTLanguageAvailability _localesRequiringAppleIntelligenceWithCompletion:]
+ -[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]
+ -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:]
+ -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:].cold.1
+ -[_LTLanguageStatusMulticaster _removeObserver:forceCloseConnection:synchronous:]
+ -[_LTLanguageStatusMulticaster setTest_avoidXPCConnections:]
+ -[_LTLanguageStatusMulticaster test_avoidXPCConnections]
+ -[_LTPreflightConfiguration downloadRequiresAppleIntelligence]
+ -[_LTPreflightConfiguration localesRequiringAppleIntelligence]
+ -[_LTPreflightConfiguration preferredStrategy]
+ -[_LTPreflightConfiguration setLocalesRequiringAppleIntelligence:]
+ -[_LTPreflightConfiguration setPreferredStrategy:]
+ -[_LTStreamingUtteranceTranslator logIdentifier]
+ -[_LTStreamingUtteranceTranslator setLogIdentifier:]
+ -[_LTSupportedLocaleList localesExclusiveToStrategy:]
+ GCC_except_table24
+ GCC_except_table39
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table9
+ _OBJC_IVAR_$__LTLanguageStatus._multicaster
+ _OBJC_IVAR_$__LTLanguageStatusMulticaster._test_avoidXPCConnections
+ _OBJC_IVAR_$__LTPreflightConfiguration._localesRequiringAppleIntelligence
+ _OBJC_IVAR_$__LTPreflightConfiguration._preferredStrategy
+ _OBJC_IVAR_$__LTStreamingUtteranceTranslator._logIdentifier
+ ___122-[NSLocale(LTLocaleIdentifier) _lt_displaySubnameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:]_block_invoke
+ ___122-[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:]_block_invoke
+ ___34-[_LTTextSession _prepareRequest:]_block_invoke.15
+ ___34-[_LTTextSession _prepareRequest:]_block_invoke_2.16
+ ___34-[_LTTextSession _prepareRequest:]_block_invoke_3
+ ___34-[_LTTextSession _prepareRequest:]_block_invoke_4
+ ___34-[_LTTextSession _prepareRequest:]_block_invoke_4.cold.1
+ ___34-[_LTTextSession _prepareRequest:]_block_invoke_4.cold.2
+ ___76-[_LTLanguageAvailability _localesRequiringAppleIntelligenceWithCompletion:]_block_invoke
+ ___81-[_LTLanguageStatusMulticaster _removeObserver:forceCloseConnection:synchronous:]_block_invoke
+ ___96-[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]_block_invoke
+ ___96-[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]_block_invoke.3
+ ___96-[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]_block_invoke_2
+ ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke
+ ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke.64
+ ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke.cold.1
+ ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke_2
+ ___Block_byref_object_copy_.15
+ ___Block_byref_object_dispose_.16
+ ___block_descriptor_67_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_72_e8_32s40bs_e46_v24?0"<_LTTextTranslationService>"8?<v?>16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e17_v16?0"NSArray"8ls32l8w64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:
+ _objc_msgSend$_initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:
+ _objc_msgSend$_localesRequiringAppleIntelligenceWithCompletion:
+ _objc_msgSend$_lt_displayNameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:
+ _objc_msgSend$_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:
+ _objc_msgSend$_removeObserver:forceCloseConnection:synchronous:
+ _objc_msgSend$languagesForText:usingModel:strategy:taskHint:completion:
+ _objc_msgSend$languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:
+ _objc_msgSend$localesExclusiveToStrategy:
+ _objc_msgSend$localesRequiringAppleIntelligence
+ _objc_msgSend$setLocalesRequiringAppleIntelligence:
+ _objc_msgSend$setPreferredStrategy:
+ _objc_msgSend$test_avoidXPCConnections
- -[NSLocale(LTLocaleIdentifier) _lt_displaySubnameForContext:inTargetLocale:alongsideLocales:]
- -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:].cold.1
- -[_LTLanguageStatusMulticaster _removeObserver:forceCloseConnection:]
- GCC_except_table25
- GCC_except_table28
- GCC_except_table36
- GCC_except_table37
- GCC_except_table43
- GCC_except_table50
- GCC_except_table61
- ___110-[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke
- ___34-[_LTTextSession _prepareRequest:]_block_invoke.16
- ___34-[_LTTextSession _prepareRequest:]_block_invoke_2.17
- ___34-[_LTTextSession _prepareRequest:]_block_invoke_2.17.cold.1
- ___34-[_LTTextSession _prepareRequest:]_block_invoke_2.17.cold.2
- ___51-[_LTLanguageStatusMulticaster _removeAllObservers]_block_invoke
- ___69-[_LTLanguageStatusMulticaster _removeObserver:forceCloseConnection:]_block_invoke
- ___83-[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]_block_invoke
- ___83-[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]_block_invoke.2
- ___83-[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]_block_invoke_2
- ___90+[_LTTranslator languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:]_block_invoke
- ___90+[_LTTranslator languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:]_block_invoke.64
- ___90+[_LTTranslator languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:]_block_invoke.cold.1
- ___90+[_LTTranslator languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:]_block_invoke_2
- ___93-[NSLocale(LTLocaleIdentifier) _lt_displaySubnameForContext:inTargetLocale:alongsideLocales:]_block_invoke
- ___Block_byref_object_copy_.14
- ___Block_byref_object_dispose_.15
- ___block_descriptor_64_e8_32s40bs_e46_v24?0"<_LTTextTranslationService>"8?<v?>16ls32l8s40l8
- ___block_descriptor_66_e8_32s40w_e5_v8?0lw40l8s32l8
- _objc_msgSend$_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:
- _objc_msgSend$_lt_displayNameForContext:inTargetLocale:alongsideLocales:
- _objc_msgSend$_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:
- _objc_msgSend$_removeObserver:forceCloseConnection:
- _objc_msgSend$languagesForText:usingModel:strategy:completion:
- _objc_msgSend$languagesForText:usingModel:useDedicatedTextMachPort:completion:
CStrings:
+ "2!"
+ "<%@: %p; number of sourceStrings: %zu; number of supportedLocales: %zu; requestedSource: %@; requestedTarget: %@; resolvedSource: %@; resolvedTarget: %@; lidUnsupportedLocale: %@; systemLocale: %@; lowConfidenceLocales: %@; isForDownloadApprovalOnly: %@; isHeadless: %@; preferredStrategy: %@; deviceSupportsTranslation: %@>"
+ "@\"_LTLanguageStatusMulticaster\""
+ "@48@0:8q16@24@32@40"
+ "@52@0:8q16q24B32@36@?44"
+ "GB"
+ "Not closing XPC connection because tests asked to prevent this"
+ "Not starting XPC connection because tests asked to prevent this"
+ "Obsv mlcast for key '%{public}@': [%@]"
+ "T@\"NSArray\",C,N,V_localesRequiringAppleIntelligence"
+ "TB,N,V_test_avoidXPCConnections"
+ "Tq,N,V_preferredStrategy"
+ "US"
+ "_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:"
+ "_initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:"
+ "_localesRequiringAppleIntelligence"
+ "_localesRequiringAppleIntelligenceWithCompletion:"
+ "_lt_displayNameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:"
+ "_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:"
+ "_multicaster"
+ "_removeObserver:forceCloseConnection:synchronous:"
+ "_test_avoidXPCConnections"
+ "de"
+ "downloadRequiresAppleIntelligence"
+ "fr"
+ "highFidelity"
+ "it"
+ "languagesForText:usingModel:strategy:taskHint:completion:"
+ "languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:"
+ "localesExclusiveToStrategy:"
+ "localesRequiringAppleIntelligence"
+ "lowLatency"
+ "setLocalesRequiringAppleIntelligence:"
+ "setPreferredStrategy:"
+ "setTest_avoidXPCConnections:"
+ "test_avoidXPCConnections"
+ "v32@0:8@16B24B28"
+ "v52@0:8B16@20q28q36B44B48"
+ "v56@0:8@\"NSArray\"16Q24Q32q40@?<v@?@\"_LTTextLanguageDetectionResult\">48"
+ "v56@0:8@16Q24Q32q40@?48"
+ "v60@0:8@16Q24Q32q40B48@?52"
- "<%@: %p; number of sourceStrings: %zu; number of supportedLocales: %zu; requestedSource: %@; requestedTarget: %@; resolvedSource: %@; resolvedTarget: %@; lidUnsupportedLocale: %@; systemLocale: %@; lowConfidenceLocales: %@; isForDownloadApprovalOnly: %@; isHeadless: %@; deviceSupportsTranslation: %@>"
- "Obsv mlcast [%@]"
- "_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:"
- "_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:"
- "_removeObserver:forceCloseConnection:"
- "languagesForText:usingModel:strategy:completion:"
- "v48@0:8@\"NSArray\"16Q24Q32@?<v@?@\"_LTTextLanguageDetectionResult\">40"
- "v48@0:8@16Q24Q32@?40"
- "v48@0:8B16@20q28q36B44"
- "\xd2"

```
