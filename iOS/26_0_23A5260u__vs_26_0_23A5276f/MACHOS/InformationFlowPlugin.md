## InformationFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin`

```diff

-3500.46.2.0.0
-  __TEXT.__text: 0xa86cc
-  __TEXT.__auth_stubs: 0x4b50
+3500.53.2.0.0
+  __TEXT.__text: 0xa89d4
+  __TEXT.__auth_stubs: 0x4b70
   __TEXT.__objc_methlist: 0x26c
   __TEXT.__const: 0x449c
   __TEXT.__cstring: 0x434d
   __TEXT.__objc_methname: 0x160f
   __TEXT.__swift5_typeref: 0x1824
-  __TEXT.__oslogstring: 0x5a43
+  __TEXT.__oslogstring: 0x5b03
   __TEXT.__swift5_reflstr: 0x14a8
   __TEXT.__swift5_assocty: 0x270
   __TEXT.__constg_swiftt: 0x1b94

   __TEXT.__swift5_protos: 0x34
   __TEXT.__unwind_info: 0x1f98
   __TEXT.__eh_frame: 0x4e18
-  __DATA_CONST.__auth_got: 0x25a8
+  __DATA_CONST.__auth_got: 0x25b8
   __DATA_CONST.__got: 0x1138
   __DATA_CONST.__auth_ptr: 0xab0
-  __DATA_CONST.__const: 0x24e0
+  __DATA_CONST.__const: 0x24c0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7013B7BF-B03D-3812-869D-30783906F9E6
+  UUID: 208F7E4F-0E68-36ED-88D5-0FE1597AACAB
   Functions: 2346
-  Symbols:   20332
-  CStrings:  1066
+  Symbols:   20322
+  CStrings:  1068
 
Symbols:
+ _$s21SiriInformationSearch14PommesResponseC17isRelatedQuestionSbvg
+ _$s21SiriInformationSearch14PommesResponseC21albusMultiturnRewriteSSSgvg
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_InformationFlowPlugin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_InformationFlowPlugin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_InformationFlowPlugin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_InformationFlowPlugin
Functions:
~ _$s21InformationFlowPlugin0a7RoutingB0C012renderPommesB033_C90D02FE25FC40C99716C34BBAE4219ELLy07SiriKitB015ExecuteResponseV0nA6Search0fQ0CF : 7052 -> 7604
~ _$s21InformationFlowPlugin19DefaultBiomeDonatorC6donateyy04SiriA5Types26INInformationUseCaseIntentCFyyYacfU_TY0_ : 1488 -> 1496
~ _$s21InformationFlowPlugin21SuggestionsEntryPointC08donateToD033_75747C1F6CDEE2ADC05D167EDDA0EB0FLL_9requestIdy04SiriA6Search14PommesResponseC_SStYaFTY2_ : 728 -> 744
~ _$s21InformationFlowPlugin21SuggestionsEntryPointC08donateToD033_75747C1F6CDEE2ADC05D167EDDA0EB0FLL_9requestIdy04SiriA6Search14PommesResponseC_SStYaFTY3_ : 856 -> 1036
~ _$s13SiriInference20PersonalizationLevelO21InformationFlowPluginE4from3usoACSg0A8Ontology27UsoEntity_common_SportsItemC_tFZ : 624 -> 644
CStrings:
+ "SuggestionRequestType is .relatedQuestion and Albus Multiturn Rewrite available. Using that for knowledge fallback: %s"
+ "SuggestionsEntryPoint: Unable to donate intent %@ to SiriSuggestions. Error: %@"
+ "Using the raw utterance for knowledge fallback: %s"
- "SuggestionsEntryPoint: Unable to process intent: %@ due to unhandled error: %@"

```
