## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/Versions/A/ModelCatalog`

```diff

-302.1.0.2.0
-  __TEXT.__text: 0x4151fc
+302.6.0.3.0
+  __TEXT.__text: 0x415bc0
   __TEXT.__objc_methlist: 0x7f4
-  __TEXT.__swift5_typeref: 0x8e3c
-  __TEXT.__swift5_fieldmd: 0xd3dc
-  __TEXT.__const: 0x2e25c
-  __TEXT.__constg_swiftt: 0xc728
+  __TEXT.__swift5_typeref: 0x8f38
+  __TEXT.__swift5_fieldmd: 0xd598
+  __TEXT.__const: 0x2e97c
+  __TEXT.__constg_swiftt: 0xc8f8
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x64bf
-  __TEXT.__swift5_protos: 0x278
-  __TEXT.__swift5_types: 0xd70
-  __TEXT.__cstring: 0x48cee
+  __TEXT.__swift5_reflstr: 0x660f
+  __TEXT.__swift5_protos: 0x280
+  __TEXT.__swift5_types: 0xd8c
+  __TEXT.__cstring: 0x490be
   __TEXT.__oslogstring: 0x1ea9
-  __TEXT.__swift5_proto: 0x2d64
-  __TEXT.__swift5_capture: 0xfa2c
-  __TEXT.__swift_as_entry: 0x31c
-  __TEXT.__swift_as_ret: 0x2d8
-  __TEXT.__swift_as_cont: 0x404
-  __TEXT.__swift5_assocty: 0x1ab0
+  __TEXT.__swift5_proto: 0x2dd0
+  __TEXT.__swift5_capture: 0xfdbc
+  __TEXT.__swift_as_entry: 0x324
+  __TEXT.__swift_as_ret: 0x2e0
+  __TEXT.__swift_as_cont: 0x410
+  __TEXT.__swift5_assocty: 0x1af8
   __TEXT.__swift5_mpenum: 0x54
-  __TEXT.__unwind_info: 0x100c0
-  __TEXT.__eh_frame: 0x2b11c
+  __TEXT.__unwind_info: 0x102c8
+  __TEXT.__eh_frame: 0x2b4cc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1860
+  __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xc7158
-  __AUTH_CONST.__objc_const: 0x5f18
-  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__const: 0xac2a0
+  __AUTH_CONST.__objc_const: 0x5f98
+  __AUTH_CONST.__auth_got: 0xdb8
   __AUTH.__objc_data: 0x3f0
-  __AUTH.__data: 0x8538
-  __DATA.__data: 0x6e18
-  __DATA.__bss: 0x4da80
+  __AUTH.__data: 0x86a8
+  __DATA.__data: 0x6f28
+  __DATA.__bss: 0x4e780
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x628
-  __DATA_DIRTY.__data: 0x2258
+  __DATA_DIRTY.__data: 0x2220
   __DATA_DIRTY.__common: 0xc0
   __DATA_DIRTY.__bss: 0xb000
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 32927
+  Functions: 33266
   Symbols:   216
-  CStrings:  4718
+  CStrings:  4736
 
CStrings:
+ "Automated.Autograding.SiriPQA"
+ "AutomationTools.Zap.FMCLI.serve"
+ "ImageGenerationServicesDebiasingMetadata"
+ "InstructFMApiGenericLegacy"
+ "Invalid configuration for com.apple.fm.language.instruct_3b.fm_api_generic_legacy: "
+ "Invalid configuration for com.apple.gm.image_generation_services.debiasing.metadata: "
+ "LLMBundle alignment is wrong type"
+ "LLMBundle phrasebook is wrong type"
+ "VisualGeneration.ImagePlayground.DebiasingMetadata"
+ "WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE bm_userDefaults(\"com.apple.spatialphotosrelive\", \"LocallyDisabled\") != true AND ( (bm_deviceInfo(\"deviceType\") == \"iPad\" AND bm_mobileGestalt(\"chipID\") >= 33027) OR (bm_deviceInfo(\"deviceType\") == \"iPhone\" AND bm_mobileGestalt(\"chipID\") >= 33025) OR ( (bm_deviceInfo(\"deviceType\") == \"macDesktop\" OR bm_deviceInfo(\"deviceType\") == \"macPortable\") AND bm_osEligibility(\"copernicium\", false) == true ) )"
+ "accessibility.magnifier.reduceSensitiveTopics"
+ "alignmentVariant"
+ "com.apple.cloudos.service.recitation_agent.v1"
+ "com.apple.fm.language.instruct_3b.fm_api_generic_legacy"
+ "com.apple.fm.language.instruct_3b.fm_api_generic_legacy.generic"
+ "com.apple.fm.language.instruct_3b.fm_api_generic_legacy.generic_sparse"
+ "com.apple.fm.language.instruct_3b.fm_api_generic_legacy?variant=generic_sparse"
+ "com.apple.gm.image_generation_services.debiasing.metadata"
+ "com.apple.gm.image_generation_services.debiasing.metadata.generic"
+ "phrasebookVariant"
+ "public_display_version"
+ "translation.liveTranslation.personalTranslator"
+ "translation.liveTranslation.phoneFaceTime"
- "Invalid configuration for com.apple.fm.language.instruct_3b.video_caption: "
- "WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE bm_userDefaults(\"com.apple.spatialphotosrelive\", \"LocallyDisabled\") != true AND ( (bm_deviceInfo(\"deviceType\") == \"iPad\" AND bm_mobileGestalt(\"chipID\") >= 33027) OR (bm_deviceInfo(\"deviceType\") == \"iPhone\" AND bm_mobileGestalt(\"chipID\") >= 33025) OR (bm_deviceInfo(\"deviceType\") == \"macDesktop\" OR bm_deviceInfo(\"deviceType\") == \"macPortable\") )"
- "com.apple.fm.language.instruct_3b.video_caption.generic"
- "com.apple.fm.language.instruct_3b.video_caption.generic_sparse"
- "com.apple.fm.language.instruct_3b.video_caption?variant=generic_sparse"
```
