## MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
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
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-502.0.8.0.0
-  __TEXT.__text: 0x27ee50
-  __TEXT.__auth_stubs: 0x4ab0
-  __TEXT.__objc_stubs: 0x9480
-  __TEXT.__objc_methlist: 0x4094
+504.0.7.0.0
+  __TEXT.__text: 0x27f0e4
+  __TEXT.__auth_stubs: 0x4ac0
+  __TEXT.__objc_stubs: 0x9520
+  __TEXT.__objc_methlist: 0x40dc
   __TEXT.__const: 0xb3c4
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0xa1b8
-  __TEXT.__objc_methname: 0x126b5
-  __TEXT.__oslogstring: 0xda33
+  __TEXT.__gcc_except_tab: 0x248
+  __TEXT.__cstring: 0xa298
+  __TEXT.__objc_methname: 0x128e5
+  __TEXT.__oslogstring: 0xdaf3
   __TEXT.__objc_classname: 0x2d88
-  __TEXT.__objc_methtype: 0x3d79
+  __TEXT.__objc_methtype: 0x3dd9
   __TEXT.__swift5_typeref: 0x456e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x754c

   __TEXT.__swift_as_ret: 0x454
   __TEXT.__swift_as_cont: 0x720
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__unwind_info: 0x9398
+  __TEXT.__unwind_info: 0x93c0
   __TEXT.__eh_frame: 0x8698
-  __DATA_CONST.__const: 0x10568
-  __DATA_CONST.__cfstring: 0x21a0
+  __DATA_CONST.__const: 0x105c8
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x2568
-  __DATA_CONST.__got: 0x1ba0
+  __DATA_CONST.__auth_got: 0x2570
+  __DATA_CONST.__got: 0x1b90
   __DATA_CONST.__auth_ptr: 0xf28
-  __DATA.__objc_const: 0xca00
-  __DATA.__objc_selrefs: 0x3690
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_const: 0xca60
+  __DATA.__objc_selrefs: 0x36c0
+  __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x7848
   __DATA.__data: 0x9bb8
   __DATA.__common: 0x960

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/MomentsUIServiceCore.framework/MomentsUIServiceCore
-  Functions: 11042
-  Symbols:   26502
-  CStrings:  5007
+  Functions: 11055
+  Symbols:   26519
+  CStrings:  5018
 
Symbols:
+ -[MOConfigurationManagerBase _clearRetentionFreezeCache]
+ -[MOConfigurationManagerBase _currentRetentionFlags_onCacheQueue_featureEnabled:internalEnabled:manualEnable:asEligible:usedCache:]
+ -[MOConfigurationManagerBase _extendedProfileEnabledWithFeatureEnabled:internalEnabled:manualEnable:asEligible:]
+ -[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:]
+ -[MOConfigurationManagerBase isExtendedRetentionFeatureEnabled]
+ -[MOConfigurationManagerBase notifyWhenActionSuggestionsFetchSettledOnQueue:block:]
+ GCC_except_table13
+ GCC_except_table33
+ _OBJC_IVAR_$_MOConfigurationManagerBase._actionSuggestionsFeatureEnabledProvider
+ _OBJC_IVAR_$_MOConfigurationManagerBase._asFetchGroup
+ _OBJC_IVAR_$_MOConfigurationManagerBase._extendedRetentionBuildGateEnabledProvider
+ ___63-[MOConfigurationManagerBase isExtendedRetentionFeatureEnabled]_block_invoke
+ ___92-[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:]_block_invoke
+ ___92-[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:]_block_invoke_2
+ ___block_descriptor_32_e5_B8?0l
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ _dispatch_group_notify
+ _objc_msgSend$_clearRetentionFreezeCache
+ _objc_msgSend$_currentRetentionFlags_onCacheQueue_featureEnabled:internalEnabled:manualEnable:asEligible:usedCache:
+ _objc_msgSend$_extendedProfileEnabledWithFeatureEnabled:internalEnabled:manualEnable:asEligible:
+ _objc_msgSend$fetchActivityStatusWithCompletion:
+ _objc_msgSend$initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:
+ _objc_msgSend$isExtendedRetentionFeatureEnabled
- GCC_except_table24
- GCC_except_table3
- ___block_descriptor_48_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8r80l8
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- _objc_msgSend$fetchFeatureStatusWithCompletion:
CStrings:
+ "-[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:]"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@52@0:8@16B24@28@?36@?44"
+ "AS eligibility resolved from snapshot: %@"
+ "AS eligibility snapshot updated: %@ (ActionSuggestionActivityStatus)"
+ "AS eligibility: CorePersonalization/CorePersonalizationDaemon os_feature off -> ineligible (Mulberry leg only)"
+ "AS eligibility: CorePersonalization/CorePersonalizationDaemon os_feature off; skipping fetch"
+ "AS eligibility: no persisted verdict yet -> ineligible (fail closed)"
+ "B32@0:8B16B20B24B28"
+ "B8@?0"
+ "CorePersonalization"
+ "CorePersonalizationDaemon"
+ "Invalid parameter not satisfying: actionSuggestionsFeatureEnabledProvider != nil (in %s:%d)"
+ "Invalid parameter not satisfying: extendedRetentionBuildGateEnabledProvider != nil (in %s:%d)"
+ "MOExtendedRetention"
+ "Retention profile for this refresh: %@ [MOExtendedRetention=%d, FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d]"
+ "Threshold profile: OTA-disabled (buildGate=%d, trialFeatureEnabled=%d) for key: %@ -> nil (raw code fallback)"
+ "Threshold profile: useExtendedProfile=%d for key: %@"
+ "_actionSuggestionsFeatureEnabledProvider"
+ "_asFetchGroup"
+ "_clearRetentionFreezeCache"
+ "_currentRetentionFlags_onCacheQueue_featureEnabled:internalEnabled:manualEnable:asEligible:usedCache:"
+ "_extendedProfileEnabledWithFeatureEnabled:internalEnabled:manualEnable:asEligible:"
+ "_extendedRetentionBuildGateEnabledProvider"
+ "fetchActivityStatusWithCompletion:"
+ "initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:"
+ "isExtendedRetentionFeatureEnabled"
+ "notifyWhenActionSuggestionsFetchSettledOnQueue:block:"
+ "v56@0:8^B16^B24^B32^B40^B48"
- "AS eligibility resolved from snapshot: %@ (age %.0fs)"
- "AS eligibility snapshot updated: disabled (immediate)"
- "AS eligibility snapshot updated: enabled"
- "AS eligibility: no persisted snapshot yet -> ineligible (fail closed)"
- "AS eligibility: snapshot stale (age %.0fs > %.0fs) -> ineligible"
- "Endpoint received new connection request -- pid:%d"
- "GenerativeLearning"
- "GenerativeLearningPlatform"
- "MODefaultsManager.m"
- "MOSuggestionsUIServerManager.m"
- "PSSActionSuggestionsSnapshotDate"
- "PlatformInfoOverrideIsSeedBuild"
- "Retention profile for this refresh: %@ [FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d, GLP=%d]"
- "Threshold profile: useExtendedProfile=%d (FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d) for key: %@"
- "Using CACHED useExtendedProfile=%d for key: %@ (expires in %.0fs)"
- "fetchFeatureStatusWithCompletion:"
- "notDetermined"
- "v24@?0q8@\"NSError\"16"
```
