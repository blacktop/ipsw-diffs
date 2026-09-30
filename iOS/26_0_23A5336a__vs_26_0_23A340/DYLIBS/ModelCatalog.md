## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

 218.4.0.0.0
-  __TEXT.__text: 0x24eddc
+  __TEXT.__text: 0x259684
   __TEXT.__auth_stubs: 0x1c80
   __TEXT.__objc_methlist: 0x7b8
-  __TEXT.__cstring: 0x2739e
-  __TEXT.__swift5_typeref: 0x8c3c
-  __TEXT.__swift5_fieldmd: 0x19fb0
-  __TEXT.__const: 0x4298c
-  __TEXT.__constg_swiftt: 0x9480
+  __TEXT.__cstring: 0x27ace
+  __TEXT.__swift5_typeref: 0x8f82
+  __TEXT.__swift5_fieldmd: 0x1a48c
+  __TEXT.__const: 0x43e3c
+  __TEXT.__constg_swiftt: 0x9820
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x39d3
-  __TEXT.__swift5_protos: 0x15c
-  __TEXT.__swift5_types: 0x1014
+  __TEXT.__swift5_reflstr: 0x3a53
+  __TEXT.__swift5_protos: 0x170
+  __TEXT.__swift5_types: 0x1068
   __TEXT.__oslogstring: 0x1dcd
-  __TEXT.__swift5_proto: 0x4db8
-  __TEXT.__swift5_capture: 0x82e0
+  __TEXT.__swift5_proto: 0x4f50
+  __TEXT.__swift5_capture: 0x8500
   __TEXT.__swift_as_entry: 0x160
   __TEXT.__swift_as_ret: 0x124
-  __TEXT.__swift5_assocty: 0x4ff0
+  __TEXT.__swift5_assocty: 0x5110
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0xdd70
-  __TEXT.__eh_frame: 0x12054
+  __TEXT.__unwind_info: 0xe590
+  __TEXT.__eh_frame: 0x12644
   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methname: 0xccb
   __TEXT.__objc_methtype: 0x100

   __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_protorefs: 0x30
   __AUTH_CONST.__auth_got: 0xe40
-  __AUTH_CONST.__const: 0x7dd50
+  __AUTH_CONST.__const: 0x7fae0
   __AUTH_CONST.__objc_const: 0x14f0
   __AUTH.__objc_data: 0x488
-  __AUTH.__data: 0x3490
-  __DATA.__data: 0x9328
-  __DATA.__bss: 0x8f280
+  __AUTH.__data: 0x3620
+  __DATA.__data: 0x96a8
+  __DATA.__bss: 0x92180
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x588
-  __DATA_DIRTY.__data: 0x20f8
+  __DATA_DIRTY.__data: 0x2188
   __DATA_DIRTY.__common: 0x88
-  __DATA_DIRTY.__bss: 0xa900
+  __DATA_DIRTY.__bss: 0xac00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1C9AE1D0-536B-3B75-AE80-61938F49ABB7
-  Functions: 31610
+  UUID: 2172793E-3AC7-38A7-B72D-B24BC4CF8257
+  Functions: 32153
   Symbols:   244
-  CStrings:  2840
+  CStrings:  2863
 
CStrings:
+ "CoreMotionCalorimetryFMPredictedWRMets"
+ "CoreMotionCalorimetryReducedEmbeddings"
+ "CoreMotionFoundationModelInferenceProvider"
+ "CoreMotionIMUFoundationModel"
+ "CoreMotionPednetV1InferenceProvider"
+ "Invalid configuration for com.apple.fm.coremotion.calorimetry_fm_predicted_wrmets_v1.adaptor: "
+ "Invalid configuration for com.apple.fm.coremotion.calorimetry_reduced_embeddings.adaptor: "
+ "Invalid configuration for com.apple.fm.coremotion.imu_v1.base: "
+ "Invalid configuration for com.apple.fm.coremotion.pednet_v1.base: "
+ "MotionBundle adapter is wrong type"
+ "MotionBundle baseModel is wrong type"
+ "MotionBundle missing 'base_model' key from json: "
+ "MotionBundle missing Motion with id "
+ "WITH EligibilityInfo AS ( SELECT isAppleIntelligenceToggleEnabled, region, languages_json, json_extract(appleIntelligenceUseCase_json, \"$.waitlistStatus\") AS afm_waitlistStatus, json_extract(appleIntelligenceUseCase_json, \"$.isDeviceEligible\") AS afm_deviceEligible FROM \"AppleIntelligence.Availability\" ORDER BY eventTimestamp DESC LIMIT 1 ) SELECT  json_each.value AS language, bm_featureFlagValue(\"GenerativePlayground/ADMv8\") AS useDefault, NULL AS expirationDate FROM EligibilityInfo, json_each(languages_json)"
+ "com.apple.MobileAsset.UAF.CoreMotion.IMUFoundationModel"
+ "com.apple.coremotion.fitness"
+ "com.apple.fm.coremotion.calorimetry_fm_predicted_wrmets_v1.adaptor"
+ "com.apple.fm.coremotion.calorimetry_fm_predicted_wrmets_v1.adaptor.generic"
+ "com.apple.fm.coremotion.calorimetry_reduced_embeddings.adaptor"
+ "com.apple.fm.coremotion.calorimetry_reduced_embeddings.adaptor.generic"
+ "com.apple.fm.coremotion.imu_v1.base"
+ "com.apple.fm.coremotion.imu_v1.base.generic"
+ "com.apple.fm.coremotion.pednet_v1.base"

```
