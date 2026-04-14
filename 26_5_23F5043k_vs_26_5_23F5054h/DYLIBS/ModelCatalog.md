## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

-233.37.0.0.0
-  __TEXT.__text: 0x208760
+233.38.0.0.0
+  __TEXT.__text: 0x207e50
   __TEXT.__auth_stubs: 0x1cb0
   __TEXT.__objc_methlist: 0x7dc
   __TEXT.__swift5_typeref: 0x69b2
-  __TEXT.__swift5_fieldmd: 0x8394
-  __TEXT.__const: 0x20dcc
+  __TEXT.__swift5_fieldmd: 0x837c
+  __TEXT.__const: 0x20dbc
   __TEXT.__constg_swiftt: 0x6a80
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x41e4
+  __TEXT.__swift5_reflstr: 0x4194
   __TEXT.__swift5_protos: 0x19c
   __TEXT.__swift5_types: 0x964
-  __TEXT.__cstring: 0x2a7ce
+  __TEXT.__cstring: 0x2a29e
   __TEXT.__oslogstring: 0x1d2d
   __TEXT.__swift5_proto: 0x20dc
-  __TEXT.__swift5_capture: 0x6180
+  __TEXT.__swift5_capture: 0x6140
   __TEXT.__swift_as_entry: 0x154
   __TEXT.__swift_as_ret: 0x11c
   __TEXT.__swift5_assocty: 0x11e0
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__unwind_info: 0x9a50
-  __TEXT.__eh_frame: 0x145a0
+  __TEXT.__unwind_info: 0x9a40
+  __TEXT.__eh_frame: 0x14530
   __TEXT.__objc_classname: 0x479
   __TEXT.__objc_methname: 0x10cb
   __TEXT.__objc_methtype: 0xadc

   __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_protorefs: 0x30
   __AUTH_CONST.__auth_got: 0xe60
-  __AUTH_CONST.__const: 0x6c928
+  __AUTH_CONST.__const: 0x6c130
   __AUTH_CONST.__objc_const: 0x1520
   __AUTH.__objc_data: 0x470
   __AUTH.__data: 0x1e20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5F61E739-174F-3AB5-ACD8-EBFF5D435F60
-  Functions: 17669
+  UUID: E8ACE5B8-93B3-3A72-B8CE-9ED5FC934C8D
+  Functions: 17658
   Symbols:   240
-  CStrings:  3083
+  CStrings:  3073
 
CStrings:
- "InstructFMApiGenericLegacy"
- "Invalid configuration for com.apple.fm.language.instruct_3b.fm_api_generic_legacy.draft: "
- "Invalid configuration for com.apple.fm.language.instruct_3b.fm_api_generic_legacy: "
- "WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, region, languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, bm_featureFlagValue(\"GenerativePlayground/ADMv8\") AS useDefault, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND bm_mobileGestalt(\"isSimulator\") = false AND ( isAppleIntelligenceToggleEnabled = true OR bm_gmBypass(\"afm\") = true OR bm_gmBypass(\"adm\") = true ) AND bm_isSeedBuild() = true"
- "appleintelligence.enabled.seed_only"
- "com.apple.FoundationModels.Legacy"
- "com.apple.fm.language.instruct_3b.fm_api_generic_legacy"
- "com.apple.fm.language.instruct_3b.fm_api_generic_legacy.draft"
- "com.apple.fm.language.instruct_3b.fm_api_generic_legacy.draft.generic"
- "com.apple.fm.language.instruct_3b.fm_api_generic_legacy.generic"

```
