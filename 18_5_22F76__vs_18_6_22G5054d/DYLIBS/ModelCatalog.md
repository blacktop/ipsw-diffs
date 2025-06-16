## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

-162.762.0.0.0
-  __TEXT.__text: 0x1a27f0
-  __TEXT.__auth_stubs: 0x1a50
-  __TEXT.__objc_methlist: 0x72c
-  __TEXT.__const: 0x2d104
-  __TEXT.__cstring: 0x1ae59
-  __TEXT.__swift5_typeref: 0x64c4
-  __TEXT.__oslogstring: 0x1eed
-  __TEXT.__constg_swiftt: 0x6b38
-  __TEXT.__swift5_reflstr: 0x28c7
-  __TEXT.__swift5_fieldmd: 0x10f88
+162.772.0.0.0
+  __TEXT.__text: 0x1a61a0
+  __TEXT.__auth_stubs: 0x1a90
+  __TEXT.__objc_methlist: 0x738
+  __TEXT.__const: 0x2d624
+  __TEXT.__cstring: 0x1ad79
+  __TEXT.__swift5_typeref: 0x6542
+  __TEXT.__oslogstring: 0x1f0d
+  __TEXT.__constg_swiftt: 0x6ba0
+  __TEXT.__swift5_reflstr: 0x28d7
+  __TEXT.__swift5_fieldmd: 0x1100c
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_proto: 0x34c4
-  __TEXT.__swift5_types: 0xb30
-  __TEXT.__swift5_capture: 0x5630
-  __TEXT.__swift_as_entry: 0x13c
-  __TEXT.__swift_as_ret: 0x10c
-  __TEXT.__swift5_assocty: 0x3718
+  __TEXT.__swift5_proto: 0x34e0
+  __TEXT.__swift5_types: 0xb3c
+  __TEXT.__swift5_capture: 0x5694
+  __TEXT.__swift_as_entry: 0x144
+  __TEXT.__swift_as_ret: 0x114
+  __TEXT.__swift5_assocty: 0x3730
   __TEXT.__swift5_protos: 0xfc
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x97f0
-  __TEXT.__eh_frame: 0xd648
+  __TEXT.__unwind_info: 0x98e8
+  __TEXT.__eh_frame: 0xd7f0
   __TEXT.__objc_classname: 0x39
-  __TEXT.__objc_methname: 0xda4
+  __TEXT.__objc_methname: 0xdcb
   __TEXT.__objc_methtype: 0x100
-  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xd28
-  __AUTH_CONST.__const: 0x4d400
-  __AUTH_CONST.__objc_const: 0x1368
+  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__const: 0x4d0d0
+  __AUTH_CONST.__objc_const: 0x1370
   __AUTH.__objc_data: 0x278
-  __AUTH.__data: 0x1a20
-  __DATA.__data: 0x62b0
-  __DATA.__bss: 0x5ce00
+  __AUTH.__data: 0x1aa8
+  __DATA.__data: 0x5f70
+  __DATA.__bss: 0x5d180
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x6c8
-  __DATA_DIRTY.__data: 0x28a8
+  __DATA_DIRTY.__data: 0x2868
   __DATA_DIRTY.__common: 0x80
   __DATA_DIRTY.__bss: 0xb300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C03407DB-E709-3482-A18C-85AC321D47D7
-  Functions: 21893
+  UUID: 793F671D-8F3E-342A-8CC3-5954EEAC1A42
+  Functions: 21983
   Symbols:   247
-  CStrings:  2059
+  CStrings:  2062
 
CStrings:
+ "    WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, region, languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND (isAppleIntelligenceToggleEnabled = true OR bm_gmBypass(\"afm\") = true OR bm_gmBypass(\"adm\") = true)"
+ "    WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE bm_mobileGestalt(\"deviceSupportsGenerativeModelSystems\") = true"
+ "    WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ), ValidANEArchitectures AS ( SELECT json_array(\"h13\", \"h13g\", \"h14\", \"h14g\", \"h14c\", \"h15\", \"h15g\", \"h15c\", \"h16\", \"h16g\", \"h17\", \"h14g.n301\", \"h18\") AS valid_values ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, ValidANEArchitectures, json_each(languages_json) WHERE bm_aneDeviceInfo(\"aneArchitectureType\") IN ( SELECT value FROM json_each(ValidANEArchitectures.valid_values) )"
+ "calling safetyFailures"
+ "safetyFailuresWithUserIdentifier:with:"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v28@0:8I16@?20"
+ "v28@0:8I16@?<v@?@\"NSData\"@\"NSError\">20"
- "    WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, region, languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND (isAppleIntelligenceToggleEnabled = true OR bm_gmBypass(\"afm\") = true OR bm_gmBypass(\"adm\") = true)"
- "    WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE bm_mobileGestalt(\"deviceSupportsGenerativeModelSystems\") = true"
- "    WITH EligibilityInfo AS ( SELECT region, languages_json FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ), ValidANEArchitectures AS ( SELECT json_array(\"h13\", \"h13g\", \"h14\", \"h14g\", \"h14c\", \"h15\", \"h15g\", \"h15c\", \"h16\", \"h16g\", \"h17\", \"h14g.n301\", \"h18\") AS valid_values ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, ValidANEArchitectures, json_each(languages_json) WHERE bm_aneDeviceInfo(\"aneArchitectureType\") IN ( SELECT value FROM json_each(ValidANEArchitectures.valid_values) )"
- "com.apple.fm.language.instruct_3b.text_summarizer.draft.generic"
- "com.apple.fm.language.instruct_3b.text_summarizer.generic"

```
