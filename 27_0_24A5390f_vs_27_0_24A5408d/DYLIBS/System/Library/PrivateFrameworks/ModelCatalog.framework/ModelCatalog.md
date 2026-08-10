## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-302.1.0.2.0
-  __TEXT.__text: 0x40ef24
+302.6.0.1.100
+  __TEXT.__text: 0x4101b4
   __TEXT.__objc_methlist: 0x7f4
-  __TEXT.__swift5_typeref: 0x8e3c
-  __TEXT.__swift5_fieldmd: 0xd3dc
-  __TEXT.__const: 0x2e25c
-  __TEXT.__constg_swiftt: 0xc728
+  __TEXT.__swift5_typeref: 0x8f38
+  __TEXT.__swift5_fieldmd: 0xd598
+  __TEXT.__const: 0x2e99c
+  __TEXT.__constg_swiftt: 0xc8f8
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x64bf
-  __TEXT.__swift5_protos: 0x278
-  __TEXT.__swift5_types: 0xd70
-  __TEXT.__cstring: 0x48cfe
+  __TEXT.__swift5_reflstr: 0x660f
+  __TEXT.__swift5_protos: 0x280
+  __TEXT.__swift5_types: 0xd8c
+  __TEXT.__cstring: 0x490ce
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
-  __TEXT.__unwind_info: 0x10488
-  __TEXT.__eh_frame: 0x2b1dc
+  __TEXT.__unwind_info: 0x109e0
+  __TEXT.__eh_frame: 0x2b58c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1858
+  __DATA_CONST.__const: 0x1898
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xc7a58
-  __AUTH_CONST.__objc_const: 0x5f18
-  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__const: 0xac800
+  __AUTH_CONST.__objc_const: 0x5f98
+  __AUTH_CONST.__auth_got: 0xf50
   __AUTH.__objc_data: 0x3f0
-  __AUTH.__data: 0x8540
-  __DATA.__data: 0x6e68
-  __DATA.__bss: 0x4df80
+  __AUTH.__data: 0x86b0
+  __DATA.__data: 0x6fd8
+  __DATA.__bss: 0x4ec80
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x628
-  __DATA_DIRTY.__data: 0x21f0
+  __DATA_DIRTY.__data: 0x21d0
   __DATA_DIRTY.__common: 0xc0
   __DATA_DIRTY.__bss: 0xab00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 33008
+  Functions: 33383
   Symbols:   266
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
