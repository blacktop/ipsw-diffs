## FamilyCircle

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle`

```diff

-247.1.0.0.0
-  __TEXT.__text: 0xa7a10
-  __TEXT.__auth_stubs: 0x2450
-  __TEXT.__objc_methlist: 0x3994
-  __TEXT.__const: 0x6d78
-  __TEXT.__gcc_except_tab: 0x4dc
-  __TEXT.__cstring: 0x5d56
-  __TEXT.__oslogstring: 0x423f
+248.0.0.0.0
+  __TEXT.__text: 0xa7d70
+  __TEXT.__auth_stubs: 0x2480
+  __TEXT.__objc_methlist: 0x39ac
+  __TEXT.__const: 0x6e48
+  __TEXT.__gcc_except_tab: 0x4b4
+  __TEXT.__cstring: 0x5da6
+  __TEXT.__oslogstring: 0x41bf
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__swift5_typeref: 0x2142
-  __TEXT.__constg_swiftt: 0x214c
-  __TEXT.__swift5_reflstr: 0x1078
-  __TEXT.__swift5_fieldmd: 0x1788
-  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_typeref: 0x2148
+  __TEXT.__constg_swiftt: 0x21a4
+  __TEXT.__swift5_reflstr: 0x10c8
+  __TEXT.__swift5_fieldmd: 0x17fc
+  __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x548
   __TEXT.__swift5_proto: 0x550
-  __TEXT.__swift5_types: 0x224
+  __TEXT.__swift5_types: 0x230
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x748
+  __TEXT.__swift5_capture: 0x788
   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__unwind_info: 0x34c0
+  __TEXT.__unwind_info: 0x34b8
   __TEXT.__eh_frame: 0x4df0
   __TEXT.__objc_classname: 0x965
-  __TEXT.__objc_methname: 0xa34d
-  __TEXT.__objc_methtype: 0x1668
-  __TEXT.__objc_stubs: 0x4f20
+  __TEXT.__objc_methname: 0xa41f
+  __TEXT.__objc_methtype: 0x1711
+  __TEXT.__objc_stubs: 0x4f00
   __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0x1748
+  __DATA_CONST.__const: 0x1720
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25f0
+  __DATA_CONST.__objc_selrefs: 0x2600
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x170
-  __AUTH_CONST.__auth_got: 0x1238
-  __AUTH_CONST.__const: 0x4c28
-  __AUTH_CONST.__cfstring: 0x3d60
-  __AUTH_CONST.__objc_const: 0xbcf8
+  __AUTH_CONST.__auth_got: 0x1250
+  __AUTH_CONST.__const: 0x4d20
+  __AUTH_CONST.__cfstring: 0x3da0
+  __AUTH_CONST.__objc_const: 0xbd80
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x1018
   __AUTH.__data: 0x1078
-  __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x21b0
+  __DATA.__objc_ivar: 0x420
+  __DATA.__data: 0x21d0
   __DATA.__bss: 0x9d60
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x1340

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E4027BD-1CA1-3DE1-8F76-F49ABFC535D3
-  Functions: 4660
-  Symbols:   6410
-  CStrings:  3771
+  UUID: 40316E60-60C5-390E-8888-9C85A9EB8460
+  Functions: 4676
+  Symbols:   6417
+  CStrings:  3782
 
Symbols:
+ -[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]
+ -[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]
+ -[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]
+ -[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]
+ -[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:].cold.1
+ -[FAAgeRangeRequestModel ageGates]
+ -[FAAgeRangeRequestModel attestedAtOverrideInDays]
+ -[FAAgeRangeRequestModel bundleID]
+ -[FAAgeRangeRequestModel initWithRequestType:entryPoint:altDSID:bundleID:ageGates:userAgeOverride:attestedAtOverrideInDays:]
+ -[FAAgeRangeRequestModel userAgeOverride]
+ _OBJC_IVAR_$_FAAgeRangeRequestModel._ageGates
+ _OBJC_IVAR_$_FAAgeRangeRequestModel._attestedAtOverrideInDays
+ _OBJC_IVAR_$_FAAgeRangeRequestModel._bundleID
+ _OBJC_IVAR_$_FAAgeRangeRequestModel._userAgeOverride
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31.cold.1
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.32
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.32.cold.1
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.44
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.44.cold.1
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.45
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.45.cold.1
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.46
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.46.cold.1
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.47
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.47.cold.1
+ ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke
+ ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.28
+ ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.28.cold.1
+ ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.cold.1
+ ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke
+ ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.29
+ ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.29.cold.1
+ ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.cold.1
+ ___swift_memcpy24_8
+ ___swift_memcpy90_8
+ _objc_msgSend$fetchPrivacyVersionForAltDSID:completion:
+ _objc_msgSend$saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:
+ _objc_msgSend$setAgeRangeGlobalState:forAltDSID:privacyVersion:completion:
+ _objc_msgSend$shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:
+ _objc_retain_x6
+ _symbolic _____ 12FamilyCircle20DeclaredAgeRangeFlowO
+ _symbolic _____ 12FamilyCircle30DeclaredAgeRangeServerResponseV
+ _symbolic _____ So21FAAgeRangeGlobalStateV
+ _type_layout_string 12FamilyCircle30DeclaredAgeRangeServerResponseV
- -[FAAgeRangeController fetchBundleIDWithCompletionHandler:]
- -[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]
- -[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]
- -[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]
- -[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]
- -[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:].cold.1
- -[FAAgeRangeRequestModel alertModel]
- -[FAAgeRangeRequestModel initWithRequestType:entryPoint:alertModel:altDSID:]
- GCC_except_table54
- _OBJC_IVAR_$_FAAgeRangeRequestModel._alertModel
- ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke
- ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31
- ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31.cold.1
- ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.32
- ___101-[FAAgeRangeController shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.32.cold.1
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.46
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.46.cold.1
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.47
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.47.cold.1
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.48
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.48.cold.1
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.49
- ___59-[FAAgeRangeController fetchBundleIDWithCompletionHandler:]_block_invoke.49.cold.1
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.43
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.43.cold.1
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.44
- ___67-[FAAgeRangeController fetchParentalControlsWithCompletionHandler:]_block_invoke.44.cold.1
- ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke
- ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke.29
- ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke.29.cold.1
- ___84-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:]_block_invoke.cold.1
- ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke
- ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke.28
- ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke.28.cold.1
- ___92-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32bs40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
- ___swift_memcpy89_8
- _objc_msgSend$fetchBundleIDWithCompletionHandler:
- _objc_msgSend$fetchParentalControlsWithCompletionHandler:
- _objc_msgSend$saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:
- _objc_msgSend$setAgeRangeGlobalState:forAltDSID:onboardingKitVersion:completion:
- _objc_msgSend$shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:
CStrings:
+ "%"
+ "@72@0:8q16q24@32@40@48@56@64"
+ "AGE_RANGE_PROMPT_MESSAGE_ADULT"
+ "Client: %s has age range entitlement : %{bool}d"
+ "Error fetching privacy version: %@."
+ "FamilyCircle daemon connection for fetchPrivacyVersion returned an error: %@."
+ "Fetching privacy version for account"
+ "T@\"NSArray\",R,N,V_ageGates"
+ "T@\"NSNumber\",R,N,V_attestedAtOverrideInDays"
+ "T@\"NSNumber\",R,N,V_userAgeOverride"
+ "_ageGates"
+ "_attestedAtOverrideInDays"
+ "_userAgeOverride"
+ "ageGates"
+ "attestedAtOverrideInDays"
+ "com.apple.onboarding.agerange"
+ "fetchPrivacyVersion with error: %@."
+ "fetchPrivacyVersionForAltDSID:completion:"
+ "initWithRequestType:entryPoint:altDSID:bundleID:ageGates:userAgeOverride:attestedAtOverrideInDays:"
+ "saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:"
+ "setAgeRangeGlobalState:forAltDSID:privacyVersion:completion:"
+ "setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:"
+ "shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:"
+ "userAgeOverride"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v52@0:8i16@\"NSString\"20@\"NSNumber\"28@\"NSNumber\"36@?<v@?@\"NSError\">44"
+ "v52@0:8i16@20@28@36@?44"
+ "v72@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@?<v@?@\"FAAgeRangeAlertModel\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "valueForEntitlement:"
- "\""
- "@\"FAAgeRangeAlertModel\""
- "@48@0:8q16q24@32@40"
- "Error fetching bundleID: %@."
- "Error fetching parental controls: %@."
- "FamilyCircle daemon connection for fetchBundleID returned an error: %@."
- "FamilyCircle daemon connection for fetchParentalControls returned an error: %@."
- "Fetching bundleID for account"
- "Fetching parental controls for account"
- "T@\"FAAgeRangeAlertModel\",R,N,V_alertModel"
- "_ageRangeAlertModel"
- "_alertModel"
- "alertModel"
- "fetchBundleID with error: %@."
- "fetchBundleIDWithCompletionHandler:"
- "fetchParentalControls with error: %@."
- "fetchParentalControlsWithCompletionHandler:"
- "initWithRequestType:entryPoint:alertModel:altDSID:"
- "saveAgeRangeGlobalState:forAltDSID:cacheDuration:completion:"
- "setAgeRangeGlobalState:forAltDSID:onboardingKitVersion:completion:"
- "setGlobalStateForAltDSID:forAltDSID:onboardingKitVersion:completion:"
- "shouldPromptAgeRangeWith:userAgeOverride:attestedAtOverrideInDays:completion:"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v32@0:8Q16@?<v@?@@\"NSError\">24"
- "v48@0:8@\"NSArray\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"FAAgeRangeAlertModel\"@\"NSError\">40"

```
