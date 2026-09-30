## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

-211.0.0.0.0
-  __TEXT.__text: 0x241144
-  __TEXT.__auth_stubs: 0x1b90
+214.1.0.0.0
+  __TEXT.__text: 0x2471bc
+  __TEXT.__auth_stubs: 0x1b80
   __TEXT.__objc_methlist: 0x7b8
-  __TEXT.__const: 0x41c1c
-  __TEXT.__cstring: 0x26a5e
-  __TEXT.__swift5_typeref: 0x8a2c
+  __TEXT.__const: 0x41efc
+  __TEXT.__cstring: 0x26f5e
+  __TEXT.__swift5_typeref: 0x8aa6
   __TEXT.__oslogstring: 0x1b1d
-  __TEXT.__constg_swiftt: 0x92a4
-  __TEXT.__swift5_reflstr: 0x37a3
-  __TEXT.__swift5_fieldmd: 0x19aa4
+  __TEXT.__constg_swiftt: 0x92e4
+  __TEXT.__swift5_reflstr: 0x39b3
+  __TEXT.__swift5_fieldmd: 0x19cb0
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_proto: 0x4cdc
-  __TEXT.__swift5_types: 0xfe4
-  __TEXT.__swift5_capture: 0x8030
+  __TEXT.__swift5_proto: 0x4d00
+  __TEXT.__swift5_types: 0xfec
+  __TEXT.__swift5_capture: 0x8180
   __TEXT.__swift_as_entry: 0x150
   __TEXT.__swift_as_ret: 0x118
-  __TEXT.__swift5_assocty: 0x4f60
+  __TEXT.__swift5_assocty: 0x4f78
   __TEXT.__swift5_protos: 0x154
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0xd598
-  __TEXT.__eh_frame: 0x11bdc
+  __TEXT.__unwind_info: 0xdaa0
+  __TEXT.__eh_frame: 0x11d4c
   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methname: 0xcbc
   __TEXT.__objc_methtype: 0x100

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xdc8
-  __AUTH_CONST.__const: 0x78ea8
+  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH_CONST.__const: 0x79778
   __AUTH_CONST.__objc_const: 0x14f0
   __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x3558
-  __DATA.__data: 0x9108
-  __DATA.__bss: 0x8d680
+  __DATA.__data: 0x9168
+  __DATA.__bss: 0x8db00
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x508
-  __DATA_DIRTY.__data: 0x1f30
+  __DATA_DIRTY.__data: 0x1f20
   __DATA_DIRTY.__common: 0x88
   __DATA_DIRTY.__bss: 0xaa00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CF23954D-E503-3434-8B76-32ECE4215EAE
-  Functions: 31038
+  UUID: C8B6BB67-8FA1-3BEF-B2A8-B7CA9E88B390
+  Functions: 31233
   Symbols:   241
-  CStrings:  2801
+  CStrings:  2815
 
CStrings:
+ "FitnessIntelligence.WorkoutVoice.Breakthrough"
+ "FitnessIntelligence.WorkoutVoice.Companion.Breakthrough"
+ "FitnessIntelligence.WorkoutVoice.Companion.Intro"
+ "FitnessIntelligence.WorkoutVoice.Companion.Outro"
+ "FitnessIntelligence.WorkoutVoice.Companion.Split"
+ "FitnessIntelligence.WorkoutVoice.Intro"
+ "FitnessIntelligence.WorkoutVoice.Outro"
+ "FitnessIntelligence.WorkoutVoice.Split"
+ "Invalid configuration for com.apple.gm.safety_retain.output.structure_extraction_safety_word_list: "
+ "STXSafetyWordList"
+ "TokenInputDenyListBundle embeddingDenyList is wrong type"
+ "TokenInputDenyListBundle missing 'embedding_deny_list' key from json: "
+ "TokenInputDenyListBundle missing EmbeddingDenyList with id "
+ "TokenInputDenyListWithDefaultsBundle embeddingDenyList is wrong type"
+ "TokenInputDenyListWithDefaultsBundle missing 'embedding_deny_list' key from json: "
+ "TokenInputDenyListWithDefaultsBundle missing EmbeddingDenyList with id "
+ "TokenOutputDenyListBundle embeddingDenyList is wrong type"
+ "TokenOutputDenyListBundle missing 'embedding_deny_list' key from json: "
+ "TokenOutputDenyListBundle missing EmbeddingDenyList with id "
+ "TokenOutputDenyListWithDefaultsBundle embeddingDenyList is wrong type"
+ "TokenOutputDenyListWithDefaultsBundle missing 'embedding_deny_list' key from json: "
+ "TokenOutputDenyListWithDefaultsBundle missing EmbeddingDenyList with id "
+ "WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ), ValidANEArchitectures AS ( SELECT bm_aneDeviceInfo(\"allAneArchitectureTypes_json\") AS valid_values ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, ValidANEArchitectures, json_each(languages_json) WHERE bm_aneDeviceInfo(\"aneArchitectureType\") IN ( SELECT value FROM json_each(ValidANEArchitectures.valid_values) )"
+ "allow_prompt_fallback"
+ "com.apple.gm.safety_retain.output.structure_extraction_safety_word_list"
+ "com.apple.gm.safety_retain.output.structure_extraction_safety_word_list.generic"
+ "com.apple.tokenoutputretainlist.defaults.structure_extraction_safety_word_list"
+ "embeddingDenyList"
+ "embeddingDenyListVariant"
+ "embeddingDenyListVariant="
+ "embedding_deny_list"
+ "output_classes_per_threshold"
+ "pendingSymbolRemoval"
- "    WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ), ValidANEArchitectures AS ( SELECT json_array(\"h13\", \"h13g\", \"h14\", \"h14g\", \"h14c\", \"h15\", \"h15g\", \"h15c\", \"h16\", \"h16g\", \"h17\", \"h14g.n301\") AS valid_values ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, ValidANEArchitectures, json_each(languages_json) WHERE bm_aneDeviceInfo(\"aneArchitectureType\") IN ( SELECT value FROM json_each(ValidANEArchitectures.valid_values) )"
- "DEPENDENT RESOURCE IDS:::::"
- "language_da_useDefault_true"
- "language_de_useDefault_true"
- "language_en_useDefault_true"
- "language_es_useDefault_true"
- "language_fr_useDefault_true"
- "language_it_useDefault_true"
- "language_ja_useDefault_true"
- "language_ko_useDefault_true"
- "language_nb_useDefault_true"
- "language_nl_useDefault_true"
- "language_pt_useDefault_true"
- "language_sv_useDefault_true"
- "language_tr_useDefault_true"
- "language_vi_useDefault_true"
- "language_zh_HK_useDefault_true"
- "language_zh_TW_useDefault_true"
- "language_zh_useDefault_true"

```
