## ProactivePredictionClient

> `/System/Library/PrivateFrameworks/ProactivePredictionClient.framework/ProactivePredictionClient`

```diff

-613.0.1.0.0
-  __TEXT.__text: 0x1e708
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__const: 0x219e
-  __TEXT.__cstring: 0x952
-  __TEXT.__oslogstring: 0x499
-  __TEXT.__swift5_typeref: 0x7c4
-  __TEXT.__swift5_capture: 0xcc
-  __TEXT.__constg_swiftt: 0x63c
-  __TEXT.__swift5_reflstr: 0x205
-  __TEXT.__swift5_fieldmd: 0x5fc
+615.0.2.0.0
+  __TEXT.__text: 0x2278c
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0x434
+  __TEXT.__const: 0x2340
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__cstring: 0xcbc
+  __TEXT.__oslogstring: 0x4b7
+  __TEXT.__swift5_typeref: 0x808
+  __TEXT.__constg_swiftt: 0x730
+  __TEXT.__swift5_reflstr: 0x2cc
+  __TEXT.__swift5_fieldmd: 0x69c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x1e0
-  __TEXT.__swift5_types: 0x94
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift5_proto: 0x1e8
+  __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8d8
-  __TEXT.__eh_frame: 0xca8
-  __TEXT.__objc_classname: 0x94
-  __TEXT.__objc_methname: 0x617
-  __TEXT.__objc_methtype: 0x11d
-  __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__swift5_capture: 0xdc
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0xa20
+  __TEXT.__eh_frame: 0xe98
+  __TEXT.__objc_classname: 0xb9
+  __TEXT.__objc_methname: 0x85f
+  __TEXT.__objc_methtype: 0x189
+  __TEXT.__objc_stubs: 0x380
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a8
+  __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x8f0
-  __AUTH_CONST.__const: 0x1650
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0xb08
-  __AUTH.__objc_data: 0x388
-  __AUTH.__data: 0x450
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x7f0
-  __DATA.__bss: 0x3e80
-  __DATA.__common: 0x50
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__const: 0x1708
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0xe70
+  __AUTH.__objc_data: 0x5c8
+  __AUTH.__data: 0x558
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x850
+  __DATA.__bss: 0x3f80
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9431756A-D05E-3E28-AD2E-20CA6ABD6812
-  Functions: 896
-  Symbols:   1018
-  CStrings:  239
+  UUID: E24FBDC6-844B-3AB7-AFC5-5996B6971A3B
+  Functions: 973
+  Symbols:   1113
+  CStrings:  292
 
Symbols:
+ +[ATXEncodedActionSuggestionMetadata supportsSecureCoding]
+ -[ATXEncodedActionSuggestionMetadata .cxx_destruct]
+ -[ATXEncodedActionSuggestionMetadata canonicalActionID]
+ -[ATXEncodedActionSuggestionMetadata copyWithZone:]
+ -[ATXEncodedActionSuggestionMetadata encodeWithCoder:]
+ -[ATXEncodedActionSuggestionMetadata encodedInvocation]
+ -[ATXEncodedActionSuggestionMetadata encodedSummary]
+ -[ATXEncodedActionSuggestionMetadata initWithCoder:]
+ -[ATXEncodedActionSuggestionMetadata initWithEncodedInvocation:encodedSummary:canonicalActionID:]
+ -[ATXEncodedActionSuggestionMetadata isEqual:]
+ -[ATXProactivePredictionClientHelper suggestionMetadataForActions:error:]
+ -[ATXProactivePredictionClientHelper suggestionMetadataForActions:withCompletion:]
+ GCC_except_table30
+ _OBJC_CLASS_$_ATXActionSuggestionMetadataClient
+ _OBJC_CLASS_$_ATXEncodedActionSuggestionMetadata
+ _OBJC_CLASS_$_SFFormattedText
+ _OBJC_CLASS_$_SFRichText
+ _OBJC_CLASS_$__TtC25ProactivePredictionClient19SPParameterizedTool
+ _OBJC_IVAR_$_ATXEncodedActionSuggestionMetadata._canonicalActionID
+ _OBJC_IVAR_$_ATXEncodedActionSuggestionMetadata._encodedInvocation
+ _OBJC_IVAR_$_ATXEncodedActionSuggestionMetadata._encodedSummary
+ _OBJC_METACLASS_$_ATXActionSuggestionMetadataClient
+ _OBJC_METACLASS_$_ATXEncodedActionSuggestionMetadata
+ _OBJC_METACLASS_$__TtC25ProactivePredictionClient19SPParameterizedTool
+ __Block_object_dispose
+ __CLASS_METHODS_ATXActionSuggestionMetadataClient
+ __CLASS_PROPERTIES_ATXActionSuggestionMetadataClient
+ __DATA_ATXActionSuggestionMetadataClient
+ __DATA__TtC25ProactivePredictionClient19SPParameterizedTool
+ __DATA__TtC25ProactivePredictionClient24ActionSuggestionMetadata
+ __INSTANCE_METHODS_ATXActionSuggestionMetadataClient
+ __INSTANCE_METHODS__TtC25ProactivePredictionClient19SPParameterizedTool
+ __IVARS__TtC25ProactivePredictionClient19SPParameterizedTool
+ __IVARS__TtC25ProactivePredictionClient24ActionSuggestionMetadata
+ __METACLASS_DATA_ATXActionSuggestionMetadataClient
+ __METACLASS_DATA__TtC25ProactivePredictionClient19SPParameterizedTool
+ __METACLASS_DATA__TtC25ProactivePredictionClient24ActionSuggestionMetadata
+ __OBJC_$_CLASS_METHODS_ATXEncodedActionSuggestionMetadata
+ __OBJC_$_CLASS_PROP_LIST_ATXEncodedActionSuggestionMetadata
+ __OBJC_$_INSTANCE_METHODS_ATXEncodedActionSuggestionMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ATXEncodedActionSuggestionMetadata
+ __OBJC_$_PROP_LIST_ATXEncodedActionSuggestionMetadata
+ __OBJC_CLASS_PROTOCOLS_$_ATXEncodedActionSuggestionMetadata
+ __OBJC_CLASS_RO_$_ATXEncodedActionSuggestionMetadata
+ __OBJC_METACLASS_RO_$_ATXEncodedActionSuggestionMetadata
+ __PROPERTIES__TtC25ProactivePredictionClient19SPParameterizedTool
+ __Unwind_Resume
+ ___73-[ATXProactivePredictionClientHelper suggestionMetadataForActions:error:]_block_invoke
+ ___73-[ATXProactivePredictionClientHelper suggestionMetadataForActions:error:]_block_invoke.cold.1
+ ___82-[ATXProactivePredictionClientHelper suggestionMetadataForActions:withCompletion:]_block_invoke
+ ___82-[ATXProactivePredictionClientHelper suggestionMetadataForActions:withCompletion:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___objc_personality_v0
+ _objc_autorelease
+ _objc_msgSend$canonicalActionID
+ _objc_msgSend$copy
+ _objc_msgSend$encodedSummary
+ _objc_msgSend$initWithEncodedInvocation:encodedSummary:canonicalActionID:
+ _objc_msgSend$suggestionMetadataForActions:withCompletion:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x3
+ _symbolic So10SFRichTextCSg
+ _symbolic So6NSDataC
+ _symbolic _____ 25ProactivePredictionClient024ActionSuggestionMetadataC0C
+ _symbolic _____ 25ProactivePredictionClient024ActionSuggestionMetadataC5ErrorO
+ _symbolic _____ 25ProactivePredictionClient19SPParameterizedToolC
+ _symbolic _____ 25ProactivePredictionClient24ActionSuggestionMetadataC
+ _symbolic _____ 7ToolKit0A17InvocationSummaryV
+ _symbolic _____Sg 7ToolKit0A17InvocationSummaryV
+ _type_layout_string 25ProactivePredictionClient024ActionSuggestionMetadataC5ErrorO
CStrings:
+ ": Server did not return metadata for all requested actions"
+ "@\"NSString\""
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24@32"
+ "ATXActionSuggestionMetadataClient"
+ "ATXEncodedActionSuggestionMetadata"
+ "Failed to decode invocation and summary"
+ "Failed to get action suggestion metadata: %@"
+ "ProactivePredictionClient.SPParameterizedTool"
+ "T@\"ATXActionSuggestionMetadataClient\",N,R"
+ "T@\"NSData\",N,R,VtoolInvocationData"
+ "T@\"NSData\",N,R,VtoolInvocationSummaryData"
+ "T@\"NSData\",R,N,V_encodedSummary"
+ "T@\"NSString\",R,N,V_canonicalActionID"
+ "T@\"SFRichText\",N,R,VparameterizedTitle"
+ "Unxpected parameter"
+ "Unxpected summaryElement"
+ "_TtC25ProactivePredictionClient19SPParameterizedTool"
+ "_TtC25ProactivePredictionClient24ActionSuggestionMetadata"
+ "_canonicalActionID"
+ "_encodedSummary"
+ "canonicalActionID"
+ "canonicalID"
+ "copy"
+ "encodedSummary"
+ "fetchFormattedTitlesForActions:error:"
+ "initWithEncodedInvocation:encodedSummary:canonicalActionID:"
+ "initWithToolInvocationData:toolInvocationSummaryData:parameterizedTitle:"
+ "parameterizedTitle"
+ "setEncapsulationStyle:"
+ "setFormattedTextPieces:"
+ "setIsEmphasized:"
+ "setText:"
+ "shared"
+ "suggestionMetadataForActions:error:"
+ "suggestionMetadataForActions:withCompletion:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "toolInvocationData"
+ "toolInvocationSummary"
+ "toolInvocationSummaryData"
+ "v16@?0@\"NSError\"8"
+ "v32@0:8@16@?24"

```
