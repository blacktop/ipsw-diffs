## FamilyCircle

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle`

```diff

-245.0.0.0.0
-  __TEXT.__text: 0xa5884
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x39cc
-  __TEXT.__const: 0x6aa8
-  __TEXT.__gcc_except_tab: 0x504
+247.1.0.0.0
+  __TEXT.__text: 0xa7a10
+  __TEXT.__auth_stubs: 0x2450
+  __TEXT.__objc_methlist: 0x3994
+  __TEXT.__const: 0x6d78
+  __TEXT.__gcc_except_tab: 0x4dc
   __TEXT.__cstring: 0x5d56
-  __TEXT.__oslogstring: 0x403f
+  __TEXT.__oslogstring: 0x423f
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__swift5_typeref: 0x20aa
-  __TEXT.__constg_swiftt: 0x207c
-  __TEXT.__swift5_reflstr: 0xff0
-  __TEXT.__swift5_fieldmd: 0x1690
-  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_typeref: 0x2142
+  __TEXT.__constg_swiftt: 0x214c
+  __TEXT.__swift5_reflstr: 0x1078
+  __TEXT.__swift5_fieldmd: 0x1788
+  __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x548
-  __TEXT.__swift5_proto: 0x534
-  __TEXT.__swift5_types: 0x210
+  __TEXT.__swift5_proto: 0x550
+  __TEXT.__swift5_types: 0x224
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x738
+  __TEXT.__swift5_capture: 0x748
   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__unwind_info: 0x33f0
-  __TEXT.__eh_frame: 0x4c18
+  __TEXT.__unwind_info: 0x34c0
+  __TEXT.__eh_frame: 0x4df0
   __TEXT.__objc_classname: 0x965
-  __TEXT.__objc_methname: 0xa358
-  __TEXT.__objc_methtype: 0x16e0
-  __TEXT.__objc_stubs: 0x4f60
-  __DATA_CONST.__got: 0x9c0
-  __DATA_CONST.__const: 0x1798
+  __TEXT.__objc_methname: 0xa34d
+  __TEXT.__objc_methtype: 0x1668
+  __TEXT.__objc_stubs: 0x4f20
+  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__const: 0x1748
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25c8
+  __DATA_CONST.__objc_selrefs: 0x25f0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x170
-  __AUTH_CONST.__auth_got: 0x1218
-  __AUTH_CONST.__const: 0x4a80
+  __AUTH_CONST.__auth_got: 0x1238
+  __AUTH_CONST.__const: 0x4c28
   __AUTH_CONST.__cfstring: 0x3d60
-  __AUTH_CONST.__objc_const: 0xbd38
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_const: 0xbcf8
+  __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x1018
-  __AUTH.__data: 0xff0
-  __DATA.__objc_ivar: 0x418
-  __DATA.__data: 0x20d8
-  __DATA.__bss: 0x99e0
+  __AUTH.__data: 0x1078
+  __DATA.__objc_ivar: 0x414
+  __DATA.__data: 0x21b0
+  __DATA.__bss: 0x9d60
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x1340
-  __DATA_DIRTY.__data: 0x7f0
+  __DATA_DIRTY.__data: 0x800
   __DATA_DIRTY.__bss: 0x2c8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7797C33D-EAC6-3026-9889-529C4C8B8B83
-  Functions: 4610
+  UUID: 0E4027BD-1CA1-3DE1-8F76-F49ABFC535D3
+  Functions: 4660
   Symbols:   6410
-  CStrings:  3767
+  CStrings:  3771
 
Symbols:
+ +[FAAgeRange ageRangeValidationLevelDisplayNames]
+ -[FAAgeRange ageRangeValidationLevelToString]
+ -[FAAgeRange initWithAltDSID:bundleID:lowerbound:upperbound:response:responseType:createdAt:invalidatedAt:validationLevel:]
+ -[FAAgeRange validationLevel]
+ -[FAAgeRangeAlertModel initWithAgeRangeResponse:shouldPrompt:flowType:title:message:primaryButtonText:secondaryButtonText:]
+ -[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]
+ -[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]
+ -[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]
+ -[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:].cold.1
+ -[FAAgeRangeRequestModel initWithRequestType:entryPoint:alertModel:altDSID:]
+ GCC_except_table29
+ GCC_except_table34
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_IVAR_$_FAAgeRange._validationLevel
+ _SecTaskCopySigningIdentifier
+ ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke
+ ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31
+ ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31.cold.1
+ ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.32
+ ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.32.cold.1
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.46
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.46.cold.1
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.47
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.47.cold.1
+ ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.26
+ ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.26.cold.1
+ ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.41
+ ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.41.cold.1
+ ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.42
+ ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.42.cold.1
+ ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.48
+ ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.48.cold.1
+ ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.49
+ ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.49.cold.1
+ ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.38
+ ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.38.cold.1
+ ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.39
+ ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.39.cold.1
+ ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.43
+ ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.43.cold.1
+ ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.44
+ ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.44.cold.1
+ ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke
+ ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke.29
+ ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke.29.cold.1
+ ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke.cold.1
+ ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.35
+ ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.35.cold.1
+ ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.36
+ ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.36.cold.1
+ ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke
+ ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke.28
+ ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke.28.cold.1
+ ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke.cold.1
+ ___swift_memcpy32_4
+ ___swift_memcpy89_8
+ _associated conformance 12FamilyCircle19ShareOptionMetadataV10CodingKeys33_0BD0B73EA04A8495872C93A16D1D27F2LLOSHAASQ
+ _associated conformance 12FamilyCircle19ShareOptionMetadataV10CodingKeys33_0BD0B73EA04A8495872C93A16D1D27F2LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 12FamilyCircle19ShareOptionMetadataV10CodingKeys33_0BD0B73EA04A8495872C93A16D1D27F2LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _audit_token_to_pid
+ _audit_token_to_pidversion
+ _block_copy_helper.44
+ _block_copy_helper.50
+ _block_descriptor.46
+ _block_descriptor.52
+ _block_destroy_helper.45
+ _block_destroy_helper.51
+ _objc_msgSend$initWithAltDSID:bundleID:lowerbound:upperbound:response:responseType:createdAt:invalidatedAt:validationLevel:
+ _objc_msgSend$saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:
+ _objc_msgSend$setAgeRangeGlobalState:forAltDSID:onboardingKitVersion:completion:
+ _objc_msgSend$shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:
+ _objectdestroy.65Tm
+ _swift_cvw_instantiateLayoutString
+ _symbolic So14NSUserDefaultsC
+ _symbolic So18RBSProcessIdentityCSg
+ _symbolic _____ 12FamilyCircle14ClientMetadataV
+ _symbolic _____ 12FamilyCircle19ShareOptionMetadataV
+ _symbolic _____ 12FamilyCircle19ShareOptionMetadataV10CodingKeys33_0BD0B73EA04A8495872C93A16D1D27F2LLO
+ _symbolic _____ 12FamilyCircle29UserDefaultsBackedShareOptionV
+ _symbolic _____ So13audit_token_ta
+ _symbolic _____ s5Int32V
+ _symbolic _____Sg s6UInt64V
+ _symbolic ______A7At s6UInt32V
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12FamilyCircle19ShareOptionMetadataV10CodingKeys33_0BD0B73EA04A8495872C93A16D1D27F2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12FamilyCircle19ShareOptionMetadataV10CodingKeys33_0BD0B73EA04A8495872C93A16D1D27F2LLO
+ _type_layout_string 12FamilyCircle14ClientMetadataV
+ _type_layout_string SeRzSERzl12FamilyCircle29UserDefaultsBackedShareOptionVyxG
+ _type_layout_string So13audit_token_ta
- -[FAAgeRange initWithAltDSID:bundleID:lowerbound:upperbound:response:responseType:createdAt:invalidatedAt:]
- -[FAAgeRangeAlertModel ageRange]
- -[FAAgeRangeAlertModel initWithAgeRangeResponse:shouldPrompt:flowType:ageRange:title:message:primaryButtonText:secondaryButtonText:]
- -[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:]
- -[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:].cold.1
- -[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:completion:]
- -[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:completion:]
- -[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:]
- -[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:].cold.1
- -[FAAgeRangeRequestModel initWithRequestType:requestContext:entryPoint:altDSID:alertModel:]
- -[FAAgeRangeRequestModel requestContext]
- -[FASettingProtoAccountRestrictionsRequest removeRestrictionsWithCompletion:]
- GCC_except_table20
- GCC_except_table33
- GCC_except_table58
- _OBJC_IVAR_$_FAAgeRangeAlertModel._ageRange
- _OBJC_IVAR_$_FAAgeRangeRequestModel._requestContext
- ___118-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:]_block_invoke
- ___118-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:]_block_invoke.34
- ___118-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:]_block_invoke.34.cold.1
- ___118-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:]_block_invoke.35
- ___118-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:]_block_invoke.35.cold.1
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.49
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.49.cold.1
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.50
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.50.cold.1
- ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.29
- ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.29.cold.1
- ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.44
- ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.44.cold.1
- ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.45
- ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.45.cold.1
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.51
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.51.cold.1
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.52
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.52.cold.1
- ___62-[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:]_block_invoke
- ___62-[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:]_block_invoke.27
- ___62-[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:]_block_invoke.27.cold.1
- ___62-[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:]_block_invoke.28
- ___62-[FAAgeRangeController fetchAgeRangeWith:bundleID:completion:]_block_invoke.28.cold.1
- ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.41
- ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.41.cold.1
- ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.42
- ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.42.cold.1
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.46
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.46.cold.1
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.47
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.47.cold.1
- ___70-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:completion:]_block_invoke
- ___70-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:completion:]_block_invoke.32
- ___70-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:completion:]_block_invoke.32.cold.1
- ___70-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:completion:]_block_invoke.cold.1
- ___71-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:completion:]_block_invoke
- ___71-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:completion:]_block_invoke.31
- ___71-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:completion:]_block_invoke.31.cold.1
- ___71-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:completion:]_block_invoke.cold.1
- ___77-[FASettingProtoAccountRestrictionsRequest removeRestrictionsWithCompletion:]_block_invoke
- ___77-[FASettingProtoAccountRestrictionsRequest removeRestrictionsWithCompletion:]_block_invoke.cold.1
- ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.38
- ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.38.cold.1
- ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.39
- ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.39.cold.1
- ___block_descriptor_40_e8_32bs_e32_v24?0"FAAgeRange"8"NSError"16ls32l8
- ___block_descriptor_64_e8_32bs40r_e32_v24?0"FAAgeRange"8"NSError"16lr40l8s32l8
- ___block_literal_global.2
- _block_copy_helper.27
- _block_copy_helper.39
- _block_copy_helper.45
- _block_descriptor.29
- _block_descriptor.41
- _block_descriptor.47
- _block_destroy_helper.28
- _block_destroy_helper.40
- _block_destroy_helper.46
- _objc_msgSend$clearRestrictionsforProtoAccountWithCompletion:
- _objc_msgSend$fetchAgeRangeWith:bundleID:completion:
- _objc_msgSend$initWithAltDSID:bundleID:lowerbound:upperbound:response:responseType:createdAt:invalidatedAt:
- _objc_msgSend$saveAgeRangeGlobalState:forAltDSID:completion:
- _objc_msgSend$setAgeRangeGlobalState:forAltDSID:completion:
- _objc_msgSend$shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:
- _objectdestroy.71Tm
CStrings:
+ "\""
+ "1"
+ "@48@0:8q16q24@32@40"
+ "@68@0:8@16B24q28@36@44@52@60"
+ "@88@0:8@16@24@32@40q48q56@64@72q80"
+ "Age Range record with altDSID: %@, bundleID: %@, lowerbound: %ld, upperbound: %ld, response: %@, responseType: %@, createdAt: %@, invalidatedAt: %@, validationLevel: %@"
+ "Bundle identifier from signing identity is %s"
+ "BundleID:%s"
+ "Could not get LSApplicationRecord for process with PID %d"
+ "DisplayName:%s"
+ "Error obtaining RunningBoard process handle for connection to PID %@: %@"
+ "Error obtaining bundle record for connection to PID %d: %@"
+ "Error setting age range: %@."
+ "Failed to get signing info for connection to PID %d"
+ "Got LSApplicationRecord for process with PID %d"
+ "GuardianAttested"
+ "Record not found in UserDefaults"
+ "SelfAttested"
+ "The audit token of the xpc connection does not match the audit token of the created process handle."
+ "Unable to obtain RunningBoard process identity because the RunningBoard process identifier was nil."
+ "auditToken"
+ "bundleIdentifier"
+ "bundleRecordForAuditToken:error:"
+ "handleForIdentifier:error:"
+ "iTunesMetadata"
+ "identifierWithPid:"
+ "identity"
+ "initWithAgeRangeResponse:shouldPrompt:flowType:title:message:primaryButtonText:secondaryButtonText:"
+ "initWithAltDSID:bundleID:lowerbound:upperbound:response:responseType:createdAt:invalidatedAt:validationLevel:"
+ "initWithRequestType:entryPoint:alertModel:altDSID:"
+ "localizedName"
+ "processIdentifier"
+ "saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:"
+ "setAgeRangeGlobalState:forAltDSID:onboardingKitVersion:completion:"
+ "setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:"
+ "shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:"
+ "storeItemIdentifier"
+ "v44@0:8i16@\"NSString\"20@\"NSNumber\"28@?<v@?@\"NSError\">36"
+ "v44@0:8i16@20@28@?36"
+ "v48@0:8@\"NSArray\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"FAAgeRangeAlertModel\"@\"NSError\">40"
- "@\"FAAgeRange\""
- "@56@0:8q16q24q32@40@48"
- "@76@0:8@16B24q28@36@44@52@60@68"
- "@80@0:8@16@24@32@40q48q56@64@72"
- "Age Range record with altDSID: %@, bundleID: %@, lowerbound: %ld, upperbound: %ld, response: %@, responseType: %@, createdAt: %@, invalidatedAt: %@"
- "BEGIN [%lld]: FetchAgeRange  enableTelemetry=YES "
- "END [%lld] %fs:FetchAgeRange  ErrorCode=%{public,signpost.telemetry:number2,name=ErrorCode}d "
- "FetchAgeRange"
- "Fetched age range: %@."
- "Fetching age range."
- "T@\"FAAgeRange\",R,N,V_ageRange"
- "Tq,R,N,V_requestContext"
- "_ageRange"
- "_requestContext"
- "ageRange"
- "clearRestrictionsforProtoAccountWithCompletion:"
- "fetchAgeRangeWith:bundleID:completion:"
- "initWithAgeRangeResponse:shouldPrompt:flowType:ageRange:title:message:primaryButtonText:secondaryButtonText:"
- "initWithAltDSID:bundleID:lowerbound:upperbound:response:responseType:createdAt:invalidatedAt:"
- "initWithRequestType:requestContext:entryPoint:altDSID:alertModel:"
- "removeRestrictionsWithCompletion:"
- "requestContext"
- "saveAgeRangeGlobalState:forAltDSID:completion:"
- "setAgeRangeGlobalState:forAltDSID:completion:"
- "setGlobalStateForAltDSID:forAltDSID:completion:"
- "shouldPromptAgeRangeWith:userAgeOverride:altDSID:bundleID:attestedAtOverrideInDays:completion:"
- "v1"
- "v2"
- "v24@?0@\"FAAgeRange\"8@\"NSError\"16"
- "v36@0:8i16@\"NSString\"20@?<v@?@\"NSError\">28"
- "v36@0:8i16@20@?28"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"FAAgeRange\"@\"NSError\">32"
- "v64@0:8@\"NSArray\"16@\"NSNumber\"24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48@?<v@?@\"FAAgeRangeAlertModel\"@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"

```
