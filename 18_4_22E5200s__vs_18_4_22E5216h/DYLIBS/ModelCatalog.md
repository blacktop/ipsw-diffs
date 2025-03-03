## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

-162.744.10.3.0
-  __TEXT.__text: 0x196448
-  __TEXT.__auth_stubs: 0x1a20
+162.749.4.0.0
+  __TEXT.__text: 0x19b608
+  __TEXT.__auth_stubs: 0x1a40
   __TEXT.__objc_methlist: 0x6a0
-  __TEXT.__const: 0x2c5e4
-  __TEXT.__cstring: 0x1b7b9
-  __TEXT.__swift5_typeref: 0x62e2
+  __TEXT.__const: 0x2c6c4
+  __TEXT.__cstring: 0x1ad69
+  __TEXT.__swift5_typeref: 0x62f0
   __TEXT.__oslogstring: 0x1aed
-  __TEXT.__constg_swiftt: 0x68e0
-  __TEXT.__swift5_reflstr: 0x26e7
-  __TEXT.__swift5_fieldmd: 0x10d04
+  __TEXT.__constg_swiftt: 0x68fc
+  __TEXT.__swift5_reflstr: 0x27b7
+  __TEXT.__swift5_fieldmd: 0x10d68
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_proto: 0x340c
-  __TEXT.__swift5_types: 0xaf8
+  __TEXT.__swift5_proto: 0x3418
+  __TEXT.__swift5_types: 0xafc
   __TEXT.__swift5_capture: 0x5610
   __TEXT.__swift_as_entry: 0x124
   __TEXT.__swift_as_ret: 0xfc
-  __TEXT.__swift5_assocty: 0x3700
+  __TEXT.__swift5_assocty: 0x3718
   __TEXT.__swift5_protos: 0xfc
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x9930
-  __TEXT.__eh_frame: 0xd238
+  __TEXT.__unwind_info: 0x99a8
+  __TEXT.__eh_frame: 0xd2d0
   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methname: 0xd28
   __TEXT.__objc_methtype: 0x100
-  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x438
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xd10
-  __AUTH_CONST.__auth_ptr: 0xa40
-  __AUTH_CONST.__const: 0x4e6e8
+  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__auth_ptr: 0x948
+  __AUTH_CONST.__const: 0x4e8d8
   __AUTH_CONST.__objc_const: 0x1200
   __AUTH.__objc_data: 0x1b0
-  __AUTH.__data: 0x19b0
-  __DATA.__data: 0x60c0
-  __DATA.__bss: 0x5b700
+  __AUTH.__data: 0x19a8
+  __DATA.__data: 0x60a0
+  __DATA.__bss: 0x5b880
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x6c8
-  __DATA_DIRTY.__data: 0x2878
+  __DATA_DIRTY.__data: 0x2828
   __DATA_DIRTY.__common: 0x80
   __DATA_DIRTY.__bss: 0xb300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21569
+  Functions: 21653
   Symbols:   246
-  CStrings:  2033
+  CStrings:  2032
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "    WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, region, languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND (isAppleIntelligenceToggleEnabled = true OR bm_gmBypass(\"afm\") = true OR bm_gmBypass(\"adm\") = true)"
+ "WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled,  languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND (isAppleIntelligenceToggleEnabled = true OR bm_gmBypass(\"afm\") = true OR bm_gmBypass(\"adm\") = true)"
+ "ajax"
+ "safety.codeIntelligence"
- "    WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, hasEngagedWithAppleIntelligenceCFU, datePostedAppleIntelligenceCFU, region, languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible, json_extract(appleIntelligenceUseCase_json, \"$.shouldBlockAppleIntelligenceAssets\") AS afm_shouldBlock FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, CASE WHEN isAppleIntelligenceToggleEnabled = false AND hasEngagedWithAppleIntelligenceCFU = false AND datePostedAppleIntelligenceCFU != 0 THEN datePostedAppleIntelligenceCFU + 36000 ELSE NULL END AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND ( ( afm_waitlistStatus = 4 AND afm_shouldBlock = false AND ( isAppleIntelligenceToggleEnabled = true OR (isAppleIntelligenceToggleEnabled = false AND hasEngagedWithAppleIntelligenceCFU = false) ) ) OR bm_gmBypass(\"afm\") = true )"
- "    WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, region, languages_json, json_extract(appleIntelligenceDiffusionUseCase_json, \"$.waitlistStatus\") AS adm_waitlistStatus, json_extract(appleIntelligenceDiffusionUseCase_json, \"$.isDeviceEligible\") AS adm_deviceEligible, json_extract(appleIntelligenceDiffusionUseCase_json, \"$.shouldBlockAppleIntelligenceAssets\") AS adm_shouldBlock FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT CASE WHEN region = 1 THEN true ELSE false END AS isMainlandChina, json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE adm_deviceEligible = true AND ( ( (adm_waitlistStatus = 3 OR adm_waitlistStatus = 4) AND adm_shouldBlock = false AND isAppleIntelligenceToggleEnabled = true ) OR bm_gmBypass(\"adm\") = true )"
- "WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled,  languages_json, json_extract(appleIntelligenceDiffusionUseCase_json, \"$.waitlistStatus\") AS adm_waitlistStatus, json_extract(appleIntelligenceDiffusionUseCase_json, \"$.isDeviceEligible\") AS adm_deviceEligible, json_extract(appleIntelligenceDiffusionUseCase_json, \"$.shouldBlockAppleIntelligenceAssets\") AS adm_shouldBlock FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE adm_deviceEligible = true AND ( ( (adm_waitlistStatus = 3 OR adm_waitlistStatus = 4) AND adm_shouldBlock = false AND isAppleIntelligenceToggleEnabled = true ) OR bm_gmBypass(\"adm\") = true )"
- "WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, hasEngagedWithAppleIntelligenceCFU, datePostedAppleIntelligenceCFU,  languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible, json_extract(appleIntelligenceUseCase_json, \"$.shouldBlockAppleIntelligenceAssets\") AS afm_shouldBlock FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, CASE WHEN isAppleIntelligenceToggleEnabled = false AND hasEngagedWithAppleIntelligenceCFU = false AND datePostedAppleIntelligenceCFU != 0 THEN datePostedAppleIntelligenceCFU + 36000 ELSE NULL END AS expirationDate FROM EligibilityInfo, json_each(languages_json) WHERE afm_deviceEligible = true AND ( ( afm_waitlistStatus = 4 AND afm_shouldBlock = false AND ( isAppleIntelligenceToggleEnabled = true OR (isAppleIntelligenceToggleEnabled = false AND hasEngagedWithAppleIntelligenceCFU = false) ) ) OR bm_gmBypass(\"afm\") = true )"
- "com.apple.gm.server.instruct_server_v1.answer_synthesis.multilingual"

```
