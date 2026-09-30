## MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-502.0.5.0.0
-  __TEXT.__text: 0x27de78
+502.0.8.0.0
+  __TEXT.__text: 0x27eae0
   __TEXT.__auth_stubs: 0x4aa0
-  __TEXT.__objc_stubs: 0x9400
-  __TEXT.__objc_methlist: 0x4064
-  __TEXT.__const: 0xb3b4
-  __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__cstring: 0xa048
-  __TEXT.__objc_methname: 0x12565
-  __TEXT.__oslogstring: 0xd6e3
+  __TEXT.__objc_stubs: 0x9480
+  __TEXT.__objc_methlist: 0x4094
+  __TEXT.__const: 0xb3c4
+  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__cstring: 0xa158
+  __TEXT.__objc_methname: 0x126b5
+  __TEXT.__oslogstring: 0xda03
   __TEXT.__objc_classname: 0x2d88
-  __TEXT.__objc_methtype: 0x3d39
+  __TEXT.__objc_methtype: 0x3d79
   __TEXT.__swift5_typeref: 0x456e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x754c

   __TEXT.__swift_as_ret: 0x454
   __TEXT.__swift_as_cont: 0x720
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x9350
+  __TEXT.__unwind_info: 0x9380
   __TEXT.__eh_frame: 0x8670
-  __DATA_CONST.__const: 0x104f0
-  __DATA_CONST.__cfstring: 0x1fc0
+  __DATA_CONST.__const: 0x10568
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x2560
-  __DATA_CONST.__got: 0x1b98
+  __DATA_CONST.__got: 0x1ba8
   __DATA_CONST.__auth_ptr: 0xf28
-  __DATA.__objc_const: 0xc960
-  __DATA.__objc_selrefs: 0x3668
-  __DATA.__objc_ivar: 0xd4
+  __DATA.__objc_const: 0xca00
+  __DATA.__objc_selrefs: 0x3690
+  __DATA.__objc_ivar: 0xe8
   __DATA.__objc_data: 0x7848
   __DATA.__data: 0x9ba8
   __DATA.__common: 0x960

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/MomentsUIServiceCore.framework/MomentsUIServiceCore
-  Functions: 11030
-  Symbols:   26528
-  CStrings:  4968
+  Functions: 11037
+  Symbols:   26551
+  CStrings:  5003
 
Symbols:
+ -[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:]
+ -[MOConfigurationManagerBase isActionSuggestionsEligible]
+ -[MOConfigurationManagerBase isAutomaticPSSDonationEnabled]
+ -[MOConfigurationManagerBase refreshActionSuggestionsSnapshot]
+ GCC_except_table24
+ GCC_except_table3
+ OBJC_IVAR_$_MOConfigurationManagerBase._asFetchInFlight
+ OBJC_IVAR_$_MOConfigurationManagerBase._cachedActionSuggestionsEligible
+ OBJC_IVAR_$_MOConfigurationManagerBase._cachedExtendedRetentionFeatureEnabled
+ OBJC_IVAR_$_MOConfigurationManagerBase._cachedExtendedRetentionInternalEnabled
+ OBJC_IVAR_$_MOConfigurationManagerBase._cachedExtendedRetentionManualEnable
+ OBJC_IVAR_$_MOConfigurationManagerBase._eligibilityProvider
+ __62-[MOConfigurationManagerBase refreshActionSuggestionsSnapshot]_block_invoke
+ ___62-[MOConfigurationManagerBase refreshActionSuggestionsSnapshot]_block_invoke
+ ___62-[MOConfigurationManagerBase refreshActionSuggestionsSnapshot]_block_invoke_2
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8r80l8
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _objc_msgSend$fDefaultsManager
+ _objc_msgSend$fetchFeatureStatusWithCompletion:
+ _objc_msgSend$initWithDefaultsManager:enableTrialClient:eligibilityProvider:
+ _objc_msgSend$isActionSuggestionsEligible
+ _objc_msgSend$refreshActionSuggestionsSnapshot
- OBJC_IVAR_$_MOConfigurationManagerBase._cachedMFeatureEnabled
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- _objc_msgSend$initWithDefaultsManager:enableTrialClient:
CStrings:
+ "@\"<MOActionSuggestionEligibilityProviding>\""
+ "@36@0:8@16B24@28"
+ "AS eligibility fetch already in-flight; skipping duplicate request"
+ "AS eligibility indeterminate (%@); holding last verdict"
+ "AS eligibility resolved from snapshot: %@ (age %.0fs)"
+ "AS eligibility snapshot updated: disabled (immediate)"
+ "AS eligibility snapshot updated: enabled"
+ "AS eligibility: no persisted snapshot yet -> ineligible (fail closed)"
+ "AS eligibility: snapshot stale (age %.0fs > %.0fs) -> ineligible"
+ "Automatic PSS donation override present: %@"
+ "Configuration cache FROZEN for refresh: ActionSuggestionsEligible=%@, InternalEnabled=%@, expires at %@"
+ "Default (28d)"
+ "Extended (84d)"
+ "ExtendedRetentionFeatureEnabled"
+ "ExtendedRetentionInternalEnabled"
+ "ExtendedRetentionManualEnable"
+ "PSSActionSuggestionsLastKnownEligible"
+ "PSSActionSuggestionsSnapshotDate"
+ "PSSCascadeDonationEnabled"
+ "Retention profile for this refresh: %@ [FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d, GLP=%d]"
+ "Threshold profile: useExtendedProfile=%d (FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d) for key: %@"
+ "Using CACHED useExtendedProfile=%d for key: %@ (expires in %.0fs)"
+ "_asFetchInFlight"
+ "_cachedActionSuggestionsEligible"
+ "_cachedExtendedRetentionFeatureEnabled"
+ "_cachedExtendedRetentionInternalEnabled"
+ "_cachedExtendedRetentionManualEnable"
+ "_eligibilityProvider"
+ "eligible"
+ "fetchFeatureStatusWithCompletion:"
+ "force-off"
+ "force-on"
+ "ineligible"
+ "initWithDefaultsManager:enableTrialClient:eligibilityProvider:"
+ "isActionSuggestionsEligible"
+ "isAutomaticPSSDonationEnabled"
+ "notDetermined"
+ "refreshActionSuggestionsSnapshot"
+ "v24@?0q8@\"NSError\"16"
- "Configuration cache FROZEN for refresh: MFeatureEnabled=%@, expires at %@"
- "MFeatureEnabled"
- "Using CACHED MFeatureEnabled=%d for key: %@ (expires in %.0fs)"
- "_cachedMFeatureEnabled"
```
