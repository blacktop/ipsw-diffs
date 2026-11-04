## momentsd

> `/usr/libexec/momentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_floatobj`

```diff

-502.0.8.0.0
-  __TEXT.__text: 0x270f40
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x1eee0
-  __TEXT.__objc_methlist: 0xf4c4
-  __TEXT.__cstring: 0x25ebe
-  __TEXT.__objc_classname: 0x2025
-  __TEXT.__objc_methtype: 0x32ae
-  __TEXT.__objc_methname: 0x37305
-  __TEXT.__oslogstring: 0x3539b
-  __TEXT.__const: 0x1e70
-  __TEXT.__gcc_except_tab: 0x8750
+504.0.7.0.0
+  __TEXT.__text: 0x2762d0
+  __TEXT.__auth_stubs: 0x2410
+  __TEXT.__objc_stubs: 0x1f700
+  __TEXT.__objc_methlist: 0xf86c
+  __TEXT.__cstring: 0x25ece
+  __TEXT.__objc_classname: 0x2035
+  __TEXT.__objc_methtype: 0x34fe
+  __TEXT.__objc_methname: 0x37e35
+  __TEXT.__oslogstring: 0x3554b
+  __TEXT.__const: 0x1e90
+  __TEXT.__gcc_except_tab: 0x87b4
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
-  __TEXT.__swift5_typeref: 0x808
-  __TEXT.__swift5_capture: 0x3fc
-  __TEXT.__constg_swiftt: 0xa98
+  __TEXT.__swift5_typeref: 0x80e
+  __TEXT.__swift5_capture: 0x404
+  __TEXT.__constg_swiftt: 0xa78
   __TEXT.__swift5_reflstr: 0x5f3
   __TEXT.__swift5_fieldmd: 0x82c
-  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x68
-  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift5_types: 0x98
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x71e8
-  __TEXT.__eh_frame: 0x17e8
-  __DATA_CONST.__const: 0xc340
-  __DATA_CONST.__cfstring: 0x23b00
-  __DATA_CONST.__objc_classlist: 0x7d8
+  __TEXT.__unwind_info: 0x7388
+  __TEXT.__eh_frame: 0x1820
+  __DATA_CONST.__const: 0xc6a8
+  __DATA_CONST.__cfstring: 0x236c0
+  __DATA_CONST.__objc_classlist: 0x7e0
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x578
-  __DATA_CONST.__objc_intobj: 0x3a80
+  __DATA_CONST.__objc_superrefs: 0x580
+  __DATA_CONST.__objc_intobj: 0x3ac8
   __DATA_CONST.__objc_arraydata: 0x15a8
   __DATA_CONST.__objc_arrayobj: 0xb70
-  __DATA_CONST.__objc_doubleobj: 0x5c0
   __DATA_CONST.__objc_dictobj: 0x118
+  __DATA_CONST.__objc_doubleobj: 0x5d0
   __DATA_CONST.__objc_floatobj: 0x260
-  __DATA_CONST.__auth_got: 0x1230
-  __DATA_CONST.__got: 0x12b0
-  __DATA_CONST.__auth_ptr: 0x330
-  __DATA.__objc_const: 0x1aca8
-  __DATA.__objc_selrefs: 0x9ab8
-  __DATA.__objc_ivar: 0x1410
-  __DATA.__objc_data: 0x5ce0
-  __DATA.__data: 0x2168
+  __DATA_CONST.__auth_got: 0x1220
+  __DATA_CONST.__got: 0x12b8
+  __DATA_CONST.__auth_ptr: 0x338
+  __DATA.__objc_const: 0x1b028
+  __DATA.__objc_selrefs: 0x9cc8
+  __DATA.__objc_ivar: 0x1450
+  __DATA.__objc_data: 0x5d30
+  __DATA.__data: 0x2188
   __DATA.__common: 0x38c
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8625
-  Symbols:   19725
-  CStrings:  15493
+  Functions: 8749
+  Symbols:   19955
+  CStrings:  15574
 
Symbols:
+ +[MOOnboardingAndSettingsPersistence collectAndComputeAuthorizationReasonWithClientsWithDataAccess:jsReason:mulberryRequestsCollection:]
+ +[MOOnboardingAndSettingsPersistence collectAndComputeAuthorizationWithClientsWithDataAccess:applicationsWithDataAccess:onboardingFlowCompletion:mulberryRequestsCollection:]
+ +[MORefreshAnalyticsManager attemptKeyForVariant:]
+ +[MORefreshAnalyticsManager defaultPlistURL]
+ +[MORefreshAnalyticsManager providerFlagKeys]
+ +[MORefreshAnalyticsManager successKeyForVariant:]
+ -[MOCascadeDonationSessionManager _appendConfigSnapshotLocked:error:]
+ -[MOCascadeDonationSessionManager appendConfigSnapshot:error:]
+ -[MOConfigurationManagerBase _clearRetentionFreezeCache]
+ -[MOConfigurationManagerBase _currentRetentionFlags_onCacheQueue_featureEnabled:internalEnabled:manualEnable:asEligible:usedCache:]
+ -[MOConfigurationManagerBase _extendedProfileEnabledWithFeatureEnabled:internalEnabled:manualEnable:asEligible:]
+ -[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:]
+ -[MOConfigurationManagerBase isExtendedRetentionFeatureEnabled]
+ -[MOConfigurationManagerBase notifyWhenActionSuggestionsFetchSettledOnQueue:block:]
+ -[MODaemonClient _refreshAnalytics]
+ -[MODaemonClient fetchOriginalBundleForSourceSuggestionID:withContext:andHandler:]
+ -[MOEventBundleManager _clearPSSCascadeDonationDataWithReply:]
+ -[MOEventBundleManager _fetchPreviousBundlesRemovingWeeklySummariesWithDateInterval:handler:]
+ -[MOEventBundleManager _pssCascadeDonationClearIsNeeded]
+ -[MOEventBundleManager _refreshAnalytics]
+ -[MOEventBundleManager _resetPSSCascadeDonationSetsPopulatedMarker]
+ -[MOEventBundleManager considerPSSDonationForRefreshVariant:reason:donationAction:completion:]
+ -[MOEventBundleManager fetchOriginalBundleForSourceSuggestionID:CompletionHandler:]
+ -[MOEventBundleManager finalizeDonationWithFeatureEnabled:refreshVariant:handler:]
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ -[MOEventBundleStore fetchEventBundleWithGranularity:interfaceTypes:dateInterval:CompletionHandler:]
+ -[MOEventBundleStore fetchOriginalBundleForSourceSuggestionID:CompletionHandler:]
+ -[MOEventBundleStore removeEventBundlesWithGranularity:interfaceTypes:excludingActionType:CompletionHandler:]
+ -[MOEventRefreshScheduler _refreshAnalytics]
+ -[MOEventRefreshScheduler _resolveDefaultRefreshAuthorizationWithCompletion:]
+ -[MOEventRefreshScheduler _runDefaultRefreshForTask:]
+ -[MOOnboardingAndSettingsPersistence _mulberryRequestsCollection]
+ -[MOOnboardingAndSettingsPersistence getCollectAndComputeAuthorizationReason]
+ -[MORefreshAnalyticsManager .cxx_destruct]
+ -[MORefreshAnalyticsManager _captureConfigSnapshot]
+ -[MORefreshAnalyticsManager _elapsedIn:key:until:perUnit:]
+ -[MORefreshAnalyticsManager _emitAtTime:variant:trigger:outcome:failureReason:donationResult:clearResult:snapshot:]
+ -[MORefreshAnalyticsManager _hoursIn:key:until:]
+ -[MORefreshAnalyticsManager _integerIn:forKey:]
+ -[MORefreshAnalyticsManager _isInFlight:]
+ -[MORefreshAnalyticsManager _minutesIn:key:until:]
+ -[MORefreshAnalyticsManager _persistOutcome:variant:at:started:state:]
+ -[MORefreshAnalyticsManager _readState]
+ -[MORefreshAnalyticsManager _sendPayload:]
+ -[MORefreshAnalyticsManager _writeState:]
+ -[MORefreshAnalyticsManager configurationManager]
+ -[MORefreshAnalyticsManager currentClearResult]
+ -[MORefreshAnalyticsManager currentCollectFlags]
+ -[MORefreshAnalyticsManager currentDonationResult]
+ -[MORefreshAnalyticsManager currentRefreshStartTime]
+ -[MORefreshAnalyticsManager currentSnapshot]
+ -[MORefreshAnalyticsManager currentTrigger]
+ -[MORefreshAnalyticsManager currentVariant]
+ -[MORefreshAnalyticsManager emitRefreshWithOutcome:failureReason:variant:]
+ -[MORefreshAnalyticsManager emitUnstartedRefreshWithVariant:trigger:outcome:]
+ -[MORefreshAnalyticsManager initWithUniverse:]
+ -[MORefreshAnalyticsManager initWithUniverse:plistURL:]
+ -[MORefreshAnalyticsManager onboardingPersistence]
+ -[MORefreshAnalyticsManager plistURL]
+ -[MORefreshAnalyticsManager queue]
+ -[MORefreshAnalyticsManager recordClearResult:variant:]
+ -[MORefreshAnalyticsManager recordCollectResult:variant:]
+ -[MORefreshAnalyticsManager recordDonationResult:variant:]
+ -[MORefreshAnalyticsManager recordRefreshStartWithVariant:trigger:]
+ -[MORefreshAnalyticsManager refreshInFlight]
+ -[MORefreshAnalyticsManager setConfigurationManager:]
+ -[MORefreshAnalyticsManager setCurrentClearResult:]
+ -[MORefreshAnalyticsManager setCurrentCollectFlags:]
+ -[MORefreshAnalyticsManager setCurrentDonationResult:]
+ -[MORefreshAnalyticsManager setCurrentRefreshStartTime:]
+ -[MORefreshAnalyticsManager setCurrentSnapshot:]
+ -[MORefreshAnalyticsManager setCurrentTrigger:]
+ -[MORefreshAnalyticsManager setCurrentVariant:]
+ -[MORefreshAnalyticsManager setOnboardingPersistence:]
+ -[MORefreshAnalyticsManager setPlistURL:]
+ -[MORefreshAnalyticsManager setRefreshInFlight:]
+ -[MOWatchDog refreshVariant]
+ -[MOWatchDog setRefreshVariant:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MORefreshAnalyticsDictionaryKeys.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MORefreshAnalyticsManager.o
+ GCC_except_table103
+ GCC_except_table111
+ GCC_except_table120
+ GCC_except_table127
+ GCC_except_table135
+ GCC_except_table152
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table180
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table200
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table234
+ GCC_except_table33
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table77
+ GCC_except_table85
+ GCC_except_table89
+ MORefreshAnalyticsDictionaryKeys.m
+ MORefreshAnalyticsManager.m
+ _$s10ObjectiveC8ObjCBoolVMn
+ _$s10ObjectiveC8ObjCBoolVSo7NSErrorCSgIeyBhyy_Sbs5Error_pSgIeghyg_TR
+ _$s10ObjectiveC8ObjCBoolVSo7NSErrorCSgIeyBhyy_Sbs5Error_pSgIeghyg_TRTA
+ _$s11HealthPlans30ActionSuggestionActivityStatusO6activeyA2CmFWC
+ _$s11HealthPlans30ActionSuggestionActivityStatusO8inactiveyA2CmFWC
+ _$s11HealthPlans30ActionSuggestionActivityStatusOMa
+ _$s11HealthPlans38ActionSuggestionActivityStatusProviderV08activityF0AA0cdeF0OyYaKF
+ _$s11HealthPlans38ActionSuggestionActivityStatusProviderV08activityF0AA0cdeF0OyYaKFTu
+ _$s11HealthPlans38ActionSuggestionActivityStatusProviderVACycfC
+ _$s11HealthPlans38ActionSuggestionActivityStatusProviderVMa
+ _$s11HealthPlans38ActionSuggestionActivityStatusProviderVMn
+ _$s8momentsd19MOEventEntityInviteC9startDate10Foundation0F0VSgvpfiTm
+ _$s8momentsd22MODonationWriteSessionC20appendConfigSnapshotyy7Moments08MOConfigG0CKF
+ _$s8momentsd22MODonationWriteSessionC20appendConfigSnapshotyy7Moments08MOConfigG0CKFTo
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tF
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFTo
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TA
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TA.19TQ0_
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TA.19Tu
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TATQ0_
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TATu
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TQ0_
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TY1_
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_TY2_
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC19fetchActivityStatus10completionyySb_s5Error_pSgtYbc_tFyyYacfU_Tu
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC23unrecognizedStatusError018_1F5E1CB0B0CC6CD93L13CCBDFCE97ECF4LLSo7NSErrorCvpZ
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC23unrecognizedStatusError018_1F5E1CB0B0CC6CD93L13CCBDFCE97ECF4LL_WZ
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC23unrecognizedStatusError018_1F5E1CB0B0CC6CD93L13CCBDFCE97ECF4LL_Wz
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC8provider018_1F5E1CB0B0CC6CD93J13CCBDFCE97ECF4LL11HealthPlans06Actionc14ActivityStatusE0VvpWvd
+ _$s8momentsd37MOActionSuggestionEligibilityProviderC8provider018_1F5E1CB0B0CC6CD93J13CCBDFCE97ECF4LL11HealthPlans06Actionc14ActivityStatusE0Vvpfi
+ _MOAnalyticsEventDaemonRefresh
+ _MOWatchDogRefreshTimeoutPayload
+ _OBJC_CLASS_$_MORefreshAnalyticsManager
+ _OBJC_IVAR_$_MOConfigurationManagerBase._actionSuggestionsFeatureEnabledProvider
+ _OBJC_IVAR_$_MOConfigurationManagerBase._asFetchGroup
+ _OBJC_IVAR_$_MOConfigurationManagerBase._extendedRetentionBuildGateEnabledProvider
+ _OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
+ _OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
+ _OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._configurationManager
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentClearResult
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentCollectFlags
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentDonationResult
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentRefreshStartTime
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentSnapshot
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentTrigger
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._currentVariant
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._onboardingPersistence
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._plistURL
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._queue
+ _OBJC_IVAR_$_MORefreshAnalyticsManager._refreshInFlight
+ _OBJC_IVAR_$_MOWatchDog._refreshVariant
+ _OBJC_METACLASS_$_MORefreshAnalyticsManager
+ _OUTLINED_FUNCTION_15
+ __OBJC_$_CLASS_METHODS_MOOnboardingAndSettingsPersistence
+ __OBJC_$_CLASS_METHODS_MORefreshAnalyticsManager
+ __OBJC_$_INSTANCE_METHODS_MORefreshAnalyticsManager
+ __OBJC_$_INSTANCE_VARIABLES_MORefreshAnalyticsManager
+ __OBJC_$_PROP_LIST_MORefreshAnalyticsManager
+ __OBJC_$_PROP_LIST_MOWatchDog
+ __OBJC_CLASS_RO_$_MORefreshAnalyticsManager
+ __OBJC_METACLASS_RO_$_MORefreshAnalyticsManager
+ ___100-[MOEventBundleStore fetchEventBundleWithGranularity:interfaceTypes:dateInterval:CompletionHandler:]_block_invoke
+ ___109-[MOEventBundleStore removeEventBundlesWithGranularity:interfaceTypes:excludingActionType:CompletionHandler:]_block_invoke
+ ___45+[MORefreshAnalyticsManager providerFlagKeys]_block_invoke
+ ___53-[MOEventRefreshScheduler _runDefaultRefreshForTask:]_block_invoke
+ ___53-[MOEventRefreshScheduler _runDefaultRefreshForTask:]_block_invoke_2
+ ___55-[MORefreshAnalyticsManager recordClearResult:variant:]_block_invoke
+ ___57-[MORefreshAnalyticsManager recordCollectResult:variant:]_block_invoke
+ ___58-[MORefreshAnalyticsManager recordDonationResult:variant:]_block_invoke
+ ___62-[MOCascadeDonationSessionManager appendConfigSnapshot:error:]_block_invoke
+ ___62-[MOEventBundleManager _clearPSSCascadeDonationDataWithReply:]_block_invoke
+ ___63-[MOConfigurationManagerBase isExtendedRetentionFeatureEnabled]_block_invoke
+ ___67-[MORefreshAnalyticsManager recordRefreshStartWithVariant:trigger:]_block_invoke
+ ___74-[MORefreshAnalyticsManager emitRefreshWithOutcome:failureReason:variant:]_block_invoke
+ ___77-[MOEventRefreshScheduler _resolveDefaultRefreshAuthorizationWithCompletion:]_block_invoke
+ ___77-[MORefreshAnalyticsManager emitUnstartedRefreshWithVariant:trigger:outcome:]_block_invoke
+ ___81-[MOEventBundleStore fetchOriginalBundleForSourceSuggestionID:CompletionHandler:]_block_invoke
+ ___82-[MODaemonClient fetchOriginalBundleForSourceSuggestionID:withContext:andHandler:]_block_invoke
+ ___82-[MODaemonClient fetchOriginalBundleForSourceSuggestionID:withContext:andHandler:]_block_invoke_2
+ ___82-[MOEventBundleManager finalizeDonationWithFeatureEnabled:refreshVariant:handler:]_block_invoke
+ ___83-[MOEventBundleManager fetchOriginalBundleForSourceSuggestionID:CompletionHandler:]_block_invoke
+ ___83-[MOEventBundleManager fetchOriginalBundleForSourceSuggestionID:CompletionHandler:]_block_invoke_2
+ ___92-[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:]_block_invoke
+ ___92-[MOConfigurationManagerBase initWithDefaultsManager:enableTrialClient:eligibilityProvider:]_block_invoke_2
+ ___93-[MOEventBundleManager _fetchPreviousBundlesRemovingWeeklySummariesWithDateInterval:handler:]_block_invoke
+ ___94-[MOEventBundleManager considerPSSDonationForRefreshVariant:reason:donationAction:completion:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48bs56bs64r72r80r88r_e17_v16?0"NSError"8ls32l8r64l8r72l8r80l8r88l8s40l8s48l8s56l8
+ ___block_descriptor_104_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_105_e8_32s40s48s56bs64bs72bs80r88r_e17_v16?0"NSError"8ls32l8r80l8r88l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80bs88r96r104r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8r96l8s64l8s72l8r104l8s80l8
+ ___block_descriptor_121_e8_32s40s48s56bs64bs72bs80r88r96r104r_e17_v16?0"NSError"8ls32l8r80l8s40l8r88l8r96l8r104l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_121_e8_32s40s48s56bs64bs72bs80r88r96r104r_e5_v8?0ls32l8s40l8s48l8r80l8r88l8r96l8r104l8s56l8s64l8s72l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88bs96r104r112r120r128r_e5_v8?0lr96l8r104l8r112l8s32l8s40l8s48l8r120l8s56l8s64l8s72l8s88l8r128l8s80l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r_e5_v8?0lr104l8r112l8r120l8s32l8s40l8r128l8s48l8s96l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_32_e5_B8?0l
+ ___block_descriptor_40_e8_32s_e24_v16?0?<v?"NSError">8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"MOEventBundle"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e31_v16?0"BGRepeatingSystemTask"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e24_v16?0?<v?"NSError">8ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e35_v24?0"MOEventBundle"8"NSError"16ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e8_v12?0B8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e32_v16?0"NSManagedObjectContext"8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56bs64bs_e37_v32?0"NSFileHandle"8Q16"NSError"24ls32l8s40l8s56l8s48l8s64l8
+ ___block_descriptor_80_e8_32s40r48r_e32_v16?0"NSManagedObjectContext"8ls32l8r40l8r48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48bs56bs64r72r_e5_v8?0ls32l8r64l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56r64r_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_88_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40bs48bs56r64r72r80r_e5_v8?0ls32l8r56l8r64l8r72l8r80l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56bs64bs72r80r_e17_v16?0"NSError"8ls32l8r72l8r80l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e17_v16?0"NSError"8ls32l8r80l8s40l8r88l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _kMODaemonRefreshCascadeClearSucceeded
+ _kMODaemonRefreshCascadeDonationSucceeded
+ _kMODaemonRefreshCollectAndComputeAuthorization
+ _kMODaemonRefreshEnrichmentEnabled
+ _kMODaemonRefreshFailureReason
+ _kMODaemonRefreshIsCascadeDonationEnabled
+ _kMODaemonRefreshIsSignificantLocationEnabled
+ _kMODaemonRefreshMaximumAllowedEventAgeDays
+ _kMODaemonRefreshOutcome
+ _kMODaemonRefreshStartCountSinceLastOutcome
+ _kMODaemonRefreshTimeSinceLastDefaultHours
+ _kMODaemonRefreshTimeSinceLastFullHours
+ _kMODaemonRefreshTimeSinceLastLightMinutes
+ _kMODaemonRefreshTimeSinceLastSuccessfulDefaultHours
+ _kMODaemonRefreshTimeSinceLastSuccessfulFullHours
+ _kMODaemonRefreshTimeSinceLastSuccessfulLightMinutes
+ _kMODaemonRefreshTotalDurationSeconds
+ _kMODaemonRefreshTrigger
+ _kMODaemonRefreshVariant
+ _kMOEnrichedInfoKeyConfidence
+ _objc_msgSend$_appendConfigSnapshotLocked:error:
+ _objc_msgSend$_captureConfigSnapshot
+ _objc_msgSend$_clearPSSCascadeDonationDataWithReply:
+ _objc_msgSend$_clearRetentionFreezeCache
+ _objc_msgSend$_currentRetentionFlags_onCacheQueue_featureEnabled:internalEnabled:manualEnable:asEligible:usedCache:
+ _objc_msgSend$_elapsedIn:key:until:perUnit:
+ _objc_msgSend$_emitAtTime:variant:trigger:outcome:failureReason:donationResult:clearResult:snapshot:
+ _objc_msgSend$_extendedProfileEnabledWithFeatureEnabled:internalEnabled:manualEnable:asEligible:
+ _objc_msgSend$_fetchPreviousBundlesRemovingWeeklySummariesWithDateInterval:handler:
+ _objc_msgSend$_hoursIn:key:until:
+ _objc_msgSend$_integerIn:forKey:
+ _objc_msgSend$_isInFlight:
+ _objc_msgSend$_minutesIn:key:until:
+ _objc_msgSend$_mulberryRequestsCollection
+ _objc_msgSend$_persistOutcome:variant:at:started:state:
+ _objc_msgSend$_pssCascadeDonationClearIsNeeded
+ _objc_msgSend$_readState
+ _objc_msgSend$_refreshAnalytics
+ _objc_msgSend$_resetPSSCascadeDonationSetsPopulatedMarker
+ _objc_msgSend$_resolveDefaultRefreshAuthorizationWithCompletion:
+ _objc_msgSend$_runDefaultRefreshForTask:
+ _objc_msgSend$_sendPayload:
+ _objc_msgSend$_writeState:
+ _objc_msgSend$appendConfigSnapshot:error:
+ _objc_msgSend$attemptKeyForVariant:
+ _objc_msgSend$clearCascadeDonationWithReply:
+ _objc_msgSend$collectAndComputeAuthorizationReasonWithClientsWithDataAccess:jsReason:mulberryRequestsCollection:
+ _objc_msgSend$collectAndComputeAuthorizationWithClientsWithDataAccess:applicationsWithDataAccess:onboardingFlowCompletion:mulberryRequestsCollection:
+ _objc_msgSend$considerPSSDonationForRefreshVariant:reason:donationAction:completion:
+ _objc_msgSend$currentClearResult
+ _objc_msgSend$currentCollectFlags
+ _objc_msgSend$currentDonationResult
+ _objc_msgSend$currentRefreshStartTime
+ _objc_msgSend$currentSnapshot
+ _objc_msgSend$currentTrigger
+ _objc_msgSend$currentVariant
+ _objc_msgSend$defaultPlistURL
+ _objc_msgSend$emitRefreshWithOutcome:failureReason:variant:
+ _objc_msgSend$emitUnstartedRefreshWithVariant:trigger:outcome:
+ _objc_msgSend$enrichmentConfidence
+ _objc_msgSend$fetchActivityStatusWithCompletion:
+ _objc_msgSend$fetchEventBundleWithGranularity:interfaceTypes:dateInterval:CompletionHandler:
+ _objc_msgSend$fetchOriginalBundleForSourceSuggestionID:CompletionHandler:
+ _objc_msgSend$finalizeDonationWithFeatureEnabled:refreshVariant:handler:
+ _objc_msgSend$getCollectAndComputeAuthorizationReason
+ _objc_msgSend$initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:
+ _objc_msgSend$initWithUniverse:plistURL:
+ _objc_msgSend$isAutomaticPSSDonationEnabled
+ _objc_msgSend$isExtendedRetentionFeatureEnabled
+ _objc_msgSend$notifyWhenActionSuggestionsFetchSettledOnQueue:block:
+ _objc_msgSend$pCountMaxNormalized
+ _objc_msgSend$pCountWeightedAverageNormalized
+ _objc_msgSend$pCountWeightedSumNormalized
+ _objc_msgSend$plistURL
+ _objc_msgSend$providerFlagKeys
+ _objc_msgSend$recordClearResult:variant:
+ _objc_msgSend$recordCollectResult:variant:
+ _objc_msgSend$recordDonationResult:variant:
+ _objc_msgSend$recordRefreshStartWithVariant:trigger:
+ _objc_msgSend$refreshInFlight
+ _objc_msgSend$refreshVariant
+ _objc_msgSend$removeEventBundlesWithGranularity:interfaceTypes:excludingActionType:CompletionHandler:
+ _objc_msgSend$setCurrentClearResult:
+ _objc_msgSend$setCurrentCollectFlags:
+ _objc_msgSend$setCurrentDonationResult:
+ _objc_msgSend$setCurrentRefreshStartTime:
+ _objc_msgSend$setCurrentSnapshot:
+ _objc_msgSend$setCurrentTrigger:
+ _objc_msgSend$setCurrentVariant:
+ _objc_msgSend$setEnrichmentConfidence:
+ _objc_msgSend$setPCountMaxNormalized:
+ _objc_msgSend$setPCountWeightedAverageNormalized:
+ _objc_msgSend$setPCountWeightedSumNormalized:
+ _objc_msgSend$setRefreshInFlight:
+ _objc_msgSend$setRefreshVariant:
+ _objc_msgSend$successKeyForVariant:
+ _providerFlagKeys.keys
+ _providerFlagKeys.once
+ _symbolic Sb______pSgIeghyg_ s5ErrorP
+ _symbolic _____ 11HealthPlans38ActionSuggestionActivityStatusProviderV
+ _symbolic _____So7NSErrorCSgIeyBhyy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____XDXMT 8momentsd37MOActionSuggestionEligibilityProviderC
- -[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]
- -[MOEventBundleManager finalizeDonationWithFeatureEnabled:handler:]
- -[MOEventBundleRankingInput peopleCountMaxNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
- -[MOEventBundleStore fetchEventBundleWithGranularity:interfaceTypes:CompletionHandler:]
- GCC_except_table105
- GCC_except_table113
- GCC_except_table126
- GCC_except_table140
- GCC_except_table145
- GCC_except_table157
- GCC_except_table160
- GCC_except_table163
- GCC_except_table164
- GCC_except_table167
- GCC_except_table179
- GCC_except_table183
- GCC_except_table190
- GCC_except_table202
- GCC_except_table210
- GCC_except_table212
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table226
- GCC_except_table229
- GCC_except_table68
- GCC_except_table80
- GCC_except_table84
- GCC_except_table91
- _$s11HealthPlans29ActionSuggestionFeatureStatusV5StateO13notDeterminedyA2EmFWC
- _$s11HealthPlans29ActionSuggestionFeatureStatusV5StateO7enabledyA2EmFWC
- _$s11HealthPlans29ActionSuggestionFeatureStatusV5StateO8disabledyA2EmFWC
- _$s11HealthPlans29ActionSuggestionFeatureStatusV5StateOMa
- _$s11HealthPlans29ActionSuggestionFeatureStatusV5stateAC5StateOvg
- _$s11HealthPlans29ActionSuggestionFeatureStatusVMa
- _$s11HealthPlans37ActionSuggestionFeatureStatusProviderV07featureF0AA0cdeF0VyYaKF
- _$s11HealthPlans37ActionSuggestionFeatureStatusProviderV07featureF0AA0cdeF0VyYaKFTu
- _$s11HealthPlans37ActionSuggestionFeatureStatusProviderVACycfC
- _$s11HealthPlans37ActionSuggestionFeatureStatusProviderVMa
- _$s11HealthPlans37ActionSuggestionFeatureStatusProviderVMn
- _$s8momentsd21MOAppUsageAggregationC15longestActivity10Foundation12DateIntervalVSgvpfiTm
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tF
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFTo
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TA
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TA.19TQ0_
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TA.19Tu
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TATQ0_
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TATu
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TQ0_
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TY1_
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_TY2_
- _$s8momentsd37MOActionSuggestionEligibilityProviderC18fetchFeatureStatus10completionyySo011MOASFeatureH5StateV_s5Error_pSgtc_tFyyYacfU_Tu
- _$s8momentsd37MOActionSuggestionEligibilityProviderC8provider018_1F5E1CB0B0CC6CD93J13CCBDFCE97ECF4LL11HealthPlans06Actionc13FeatureStatusE0VvpWvd
- _$s8momentsd37MOActionSuggestionEligibilityProviderC8provider018_1F5E1CB0B0CC6CD93J13CCBDFCE97ECF4LL11HealthPlans06Actionc13FeatureStatusE0Vvpfi
- _$sBi64_WV
- _$sSo22MOASFeatureStatusStateVMB
- _$sSo22MOASFeatureStatusStateVML
- _$sSo22MOASFeatureStatusStateVMa
- _$sSo22MOASFeatureStatusStateVMf
- _$sSo22MOASFeatureStatusStateVMn
- _$sSo22MOASFeatureStatusStateVSo7NSErrorCSgIeyByy_ABs5Error_pSgIegyg_TR
- _$sSo22MOASFeatureStatusStateVSo7NSErrorCSgIeyByy_ABs5Error_pSgIegyg_TRTA
- _OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- _OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
- _OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
- ___57-[MOEventRefreshScheduler registerDefaultRefreshActivity]_block_invoke_2
- ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
- ___67-[MOEventBundleManager finalizeDonationWithFeatureEnabled:handler:]_block_invoke
- ___67-[MOEventBundleManager finalizeDonationWithFeatureEnabled:handler:]_block_invoke_2
- ___70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke
- ___87-[MOEventBundleStore fetchEventBundleWithGranularity:interfaceTypes:CompletionHandler:]_block_invoke
- ___97-[MOEventBundleManager runEnrichmentWithLimit:watchdogPet:startDate:endDate:donateToPSS:handler:]_block_invoke_2
- ___block_descriptor_105_e8_32s40s48s56bs64bs72bs80r88r_e17_v16?0"NSError"8ls32l8r80l8s40l8r88l8s48l8s56l8s64l8s72l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80bs88r96r104r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8r96l8s64l8s72l8r104l8s80l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80bs88r96r104r_e5_v8?0ls32l8s40l8r88l8s48l8s56l8s64l8s80l8r96l8r104l8s72l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88bs96r104r_e5_v8?0ls32l8r96l8s40l8s88l8r104l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
- ___block_descriptor_41_e8_32s_e31_v16?0"BGRepeatingSystemTask"8ls32l8
- ___block_descriptor_48_e8_32s40s_e20_v24?0q8"NSError"16ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40bs48bs_e37_v32?0"NSFileHandle"8Q16"NSError"24ls40l8s32l8s48l8
- ___block_descriptor_57_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40bs48bs56r64r_e5_v8?0ls32l8r56l8r64l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48bs56bs64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48r56r_e32_v16?0"NSManagedObjectContext"8ls32l8r48l8r56l8s40l8
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e17_v16?0"NSError"8ls32l8r64l8r72l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8r80l8
- ___block_descriptor_88_e8_32s40s48bs56bs64r72r_e17_v16?0"NSError"8ls32l8r64l8r72l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56bs64bs72r_e17_v16?0"NSError"8ls32l8r72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_97_e8_32s40s48s56bs64bs72bs80r_e17_v16?0"NSError"8ls32l8r80l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56bs64bs72bs80r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
- _objc_msgSend$_fetchPreviousBundlesWithDateInterval:handler:
- _objc_msgSend$fetchEventBundleWithGranularity:interfaceTypes:CompletionHandler:
- _objc_msgSend$fetchFeatureStatusWithCompletion:
- _objc_msgSend$finalizeDonationWithFeatureEnabled:handler:
- _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
- _symbolic _____ 11HealthPlans37ActionSuggestionFeatureStatusProviderV
- _symbolic _____ So22MOASFeatureStatusStateV
- _symbolic _____So7NSErrorCSgIeyByy_ So22MOASFeatureStatusStateV
- _symbolic ___________pSgIegyg_ So22MOASFeatureStatusStateV s5ErrorP
CStrings:
+ "%@, empty or inverted range, startDate, %@, endDate, %@, returning no visits"
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
+ "Cached events beyond CM window: %lu"
+ "Collect and compute became allowed; registering refresh activities"
+ "CorePersonalization"
+ "CorePersonalizationDaemon"
+ "DaemonRefresh"
+ "Enrichment"
+ "EnrichmentDonateBundles"
+ "EnrichmentService"
+ "EnrichmentStoreBundles"
+ "EventBundleManagerEnrichment"
+ "EventBundleManagerEnrichmentDonateBundles"
+ "EventBundleManagerEnrichmentService"
+ "EventBundleManagerEnrichmentServiceProgress"
+ "EventBundleManagerEnrichmentStoreBundles"
+ "EventBundleManagerFinalizeDonation"
+ "EventBundleManagerFinalizeDonationAppendBundles"
+ "EventBundleManagerFinalizeDonationFetchBundles"
+ "EventBundleManagerFinalizeDonationTransferToPSS"
+ "Failed to append config snapshot to donation session: %@"
+ "FinalizeDonation"
+ "FinalizeDonationAppendBundles"
+ "FinalizeDonationFetchBundles"
+ "FinalizeDonationTransferToPSS"
+ "Ignoring data access registration with no client identifier"
+ "Invalid parameter not satisfying: actionSuggestionsFeatureEnabledProvider != nil (in %s:%d)"
+ "Invalid parameter not satisfying: extendedRetentionBuildGateEnabledProvider != nil (in %s:%d)"
+ "MOCascadeDonationSessionManager: PSS donation gate closed, skipping session creation"
+ "MOExtendedRetention"
+ "MORefreshAnalyticsManager"
+ "MORefreshAnalyticsQueue"
+ "Not allowed to collect and compute; waiting for AS eligibility before deciding"
+ "PSS Cascade clear-on-disable completed successfully (%@)"
+ "PSS Cascade clear-on-disable failed"
+ "PSS Cascade clear-on-disable failed, error, %@ (%@)"
+ "PSS Cascade sets may hold stale data — clearing (%@)"
+ "PSS donation gate closed (%@, refresh variant 0x%lx) — skipping donation"
+ "PSS donation gate open (%@, refresh variant 0x%lx) — donating"
+ "PSSCascadeDonationSetsPopulated"
+ "Q36@0:8B16B20Q24B32"
+ "Refresh analytics: %@ is in the future, reporting unknown"
+ "Refresh analytics: clear result for variant %lu, which is not in flight, dropping"
+ "Refresh analytics: could not read %@, %@"
+ "Refresh analytics: could not write %@, %@"
+ "Refresh analytics: donation result for variant %lu, which is not in flight, dropping"
+ "Refresh analytics: emit for variant %lu, which is not in flight, dropping"
+ "Refresh analytics: nil cache directory, refresh state will not persist."
+ "Refresh analytics: start for variant %lu while variant %lu is in flight, keeping the first"
+ "Refresh analytics: start recorded for variant %lu, startCount now %ld"
+ "Refresh analytics: state unreadable, not persisting outcome for variant %lu"
+ "Refresh analytics: state unreadable, skipping start-count update for variant %lu"
+ "Retention profile for this refresh: %@ [MOExtendedRetention=%d, FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d]"
+ "T@\"NSDictionary\",&,N,V_currentCollectFlags"
+ "T@\"NSNumber\",C,V_refreshVariant"
+ "T@\"NSURL\",&,N,V_plistURL"
+ "TB,N,V_refreshInFlight"
+ "TQ,N,V_currentVariant"
+ "Td,N,V_currentRefreshStartTime"
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "Threshold profile: OTA-disabled (buildGate=%d, trialFeatureEnabled=%d) for key: %@ -> nil (raw code fallback)"
+ "Threshold profile: useExtendedProfile=%d for key: %@"
+ "Tq,N,V_currentClearResult"
+ "Tq,N,V_currentDonationResult"
+ "Tq,N,V_currentTrigger"
+ "T{?=qBBBq},N,V_currentSnapshot"
+ "Unrecognized Action Suggestions activity status"
+ "Watch dog [0x%p:%s] killed refresh variant %ld"
+ "[generateBehavioralPatternBundles] Behavioral pattern is disabled (extended retention feature gate closed)"
+ "_actionSuggestionsFeatureEnabledProvider"
+ "_appendConfigSnapshotLocked:error:"
+ "_asFetchGroup"
+ "_captureConfigSnapshot"
+ "_clearPSSCascadeDonationDataWithReply:"
+ "_clearRetentionFreezeCache"
+ "_currentClearResult"
+ "_currentCollectFlags"
+ "_currentDonationResult"
+ "_currentRefreshStartTime"
+ "_currentRetentionFlags_onCacheQueue_featureEnabled:internalEnabled:manualEnable:asEligible:usedCache:"
+ "_currentSnapshot"
+ "_currentTrigger"
+ "_currentVariant"
+ "_elapsedIn:key:until:perUnit:"
+ "_emitAtTime:variant:trigger:outcome:failureReason:donationResult:clearResult:snapshot:"
+ "_extendedProfileEnabledWithFeatureEnabled:internalEnabled:manualEnable:asEligible:"
+ "_extendedRetentionBuildGateEnabledProvider"
+ "_fetchPreviousBundlesRemovingWeeklySummariesWithDateInterval:handler:"
+ "_hoursIn:key:until:"
+ "_integerIn:forKey:"
+ "_isInFlight:"
+ "_minutesIn:key:until:"
+ "_mulberryRequestsCollection"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "_persistOutcome:variant:at:started:state:"
+ "_plistURL"
+ "_pssCascadeDonationClearIsNeeded"
+ "_readState"
+ "_refreshAnalytics"
+ "_refreshInFlight"
+ "_refreshVariant"
+ "_resetPSSCascadeDonationSetsPopulatedMarker"
+ "_resolveDefaultRefreshAuthorizationWithCompletion:"
+ "_runDefaultRefreshForTask:"
+ "_sendPayload:"
+ "_writeState:"
+ "action == nil OR action.actionType != %lu"
+ "appendConfigSnapshot:error:"
+ "attemptKeyForVariant:"
+ "cannot fetch original bundle, sourceSuggestionID is not a UUID, %@"
+ "cascadeClearSucceeded"
+ "cascadeDonationSucceeded"
+ "clearCascadeDonationWithReply:"
+ "clustering refresh"
+ "collectAndComputeAuthorization"
+ "collectAndComputeAuthorizationReasonWithClientsWithDataAccess:jsReason:mulberryRequestsCollection:"
+ "collectAndComputeAuthorizationWithClientsWithDataAccess:applicationsWithDataAccess:onboardingFlowCompletion:mulberryRequestsCollection:"
+ "com.apple.moments.daemon-client.fetch-original-bundle"
+ "com.apple.moments.refresh-analytics.emit"
+ "com.apple.moments.refresh-analytics.emit-unstarted"
+ "com.apple.moments.refresh-scheduler.default.authorization"
+ "considerPSSDonationForRefreshVariant:reason:donationAction:completion:"
+ "createNewEventsBetweenStartDate, empty or inverted range, startDate, %@, endDate, %@, no new events"
+ "currentClearResult"
+ "currentCollectFlags"
+ "currentDonationResult"
+ "currentRefreshStartTime"
+ "currentSnapshot"
+ "currentTrigger"
+ "currentVariant"
+ "defaultPlistURL"
+ "direct-enrichment path"
+ "emitRefreshWithOutcome:failureReason:variant:"
+ "emitUnstartedRefreshWithVariant:trigger:outcome:"
+ "enrichmentConfidence"
+ "enrichmentEnabled"
+ "fetch original bundle for sourceSuggestionID, XPC context [%@]"
+ "fetchActivityStatusWithCompletion:"
+ "fetchEventBundleWithGranularity:interfaceTypes:dateInterval:CompletionHandler:"
+ "fetchOriginalBundleForSourceSuggestionID"
+ "fetchOriginalBundleForSourceSuggestionID:CompletionHandler:"
+ "fetchOriginalBundleForSourceSuggestionID:withContext:andHandler:"
+ "finalizeDonationWithFeatureEnabled:refreshVariant:handler:"
+ "getCollectAndComputeAuthorizationReason"
+ "initWithDefaultsManager:enableTrialClient:eligibilityProvider:extendedRetentionBuildGateEnabledProvider:actionSuggestionsFeatureEnabledProvider:"
+ "initWithUniverse:plistURL:"
+ "isCascadeDonationEnabled"
+ "isExtendedRetentionFeatureEnabled"
+ "lastAttemptDefault"
+ "lastAttemptFull"
+ "lastAttemptLight"
+ "lastSuccessDefault"
+ "lastSuccessFull"
+ "lastSuccessLight"
+ "maximumAllowedEventAgeDays"
+ "notifyWhenActionSuggestionsFetchSettledOnQueue:block:"
+ "plistURL"
+ "providerFlagKeys"
+ "q32@0:8@16@24"
+ "q32@0:8B16q20B28"
+ "q40@0:8@16@24d32"
+ "q48@0:8@16@24d32d40"
+ "recordClearResult:variant:"
+ "recordCollectResult:variant:"
+ "recordDonationResult:variant:"
+ "recordRefreshStartWithVariant:trigger:"
+ "refreshAnalyticsPersistence.plist"
+ "refreshFailureReason"
+ "refreshInFlight"
+ "refreshOutcome"
+ "refreshStartCountSinceLastOutcome"
+ "refreshTotalDurationSeconds"
+ "refreshTrigger"
+ "removeEventBundlesWithGranularity:interfaceTypes:excludingActionType:CompletionHandler:"
+ "setCurrentClearResult:"
+ "setCurrentCollectFlags:"
+ "setCurrentDonationResult:"
+ "setCurrentRefreshStartTime:"
+ "setCurrentSnapshot:"
+ "setCurrentTrigger:"
+ "setCurrentVariant:"
+ "setEnrichmentConfidence:"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
+ "setPlistURL:"
+ "setRefreshInFlight:"
+ "setRefreshVariant:"
+ "skipped-clustering refresh"
+ "stage=%{public}s completed=%lu total=%lu"
+ "startCountSinceLastOutcome"
+ "successKeyForVariant:"
+ "suggestionID == %@"
+ "the PSS donation gate is open (Mulberry), so we are authorized to collect and compute"
+ "timeSinceLastDefaultRefreshHours"
+ "timeSinceLastFullRefreshHours"
+ "timeSinceLastLightRefreshMinutes"
+ "timeSinceLastSuccessfulDefaultRefreshHours"
+ "timeSinceLastSuccessfulFullRefreshHours"
+ "timeSinceLastSuccessfulLightRefreshMinutes"
+ "unable to fetch original bundle since datastore is not available"
+ "unexpected enrichment confidence type %@"
+ "v16@?0@?<v@?@\"NSError\">8"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v32@0:8Q16q24"
+ "v32@0:8q16Q24"
+ "v36@0:8B16Q20@?28"
+ "v40@0:8@\"NSString\"16@\"MOXPCContext\"24@?<v@?@\"MOEventBundle\"@\"NSError\">32"
+ "v40@0:8Q16q24q32"
+ "v40@0:8q16q24Q32"
+ "v40@0:8{?=qBBBq}16"
+ "v48@0:8Q16@24@?32@?40"
+ "v48@0:8Q16@24Q32@?40"
+ "v52@0:8q16Q24d32B40@44"
+ "v56@0:8^B16^B24^B32^B40^B48"
+ "v96@0:8d16Q24q32q40q48q56q64{?=qBBBq}72"
+ "{?=\"authorization\"q\"significantLocationEnabled\"B\"cascadeDonationEnabled\"B\"enrichmentEnabled\"B\"maximumAllowedEventAgeDays\"q}"
+ "{?=qBBBq}16@0:8"
- " ---  Grouped Interactions Count  :%3lu"
- " ---  Received Interactions Count :%3lu"
- "#PhotoMemory,sortedasset,id,%d,asset,%@"
- "%@, idx, %lu, interaction, %@"
- "%s, media title, %@, event count, %lu"
- "(%f)"
- "AS eligibility resolved from snapshot: %@ (age %.0fs)"
- "AS eligibility snapshot updated: disabled (immediate)"
- "AS eligibility snapshot updated: enabled"
- "AS eligibility: no persisted snapshot yet -> ineligible (fail closed)"
- "AS eligibility: snapshot stale (age %.0fs > %.0fs) -> ineligible"
- "CLLocation+MOExtensions.m"
- "DailyAnnotation: Event, %@"
- "Extended retention enabled: %d, cached events beyond CM window: %lu"
- "GenerativeLearning"
- "GenerativeLearningPlatform"
- "MOAggregationManager.m"
- "MOAnnotationManager.m"
- "MOBiomeManager.m"
- "MOBookmarkStore.m"
- "MOBundleClusteringManager.m"
- "MOCascadeDonationSessionManager: GLP feature flag off, skipping session creation"
- "MOContextAnnotationUtilities.m"
- "MOConversation.m"
- "MODaemonAnalyticsManager.m"
- "MODaemonClient.m"
- "MODaemonUniverse.m"
- "MODailyAnnotationManager.m"
- "MODataDumpFormatter.m"
- "MODefaultsManager.m"
- "MODictionaryEncoder.m"
- "MODictionaryTransformer.m"
- "MODominantBundleCreationManager.m"
- "MODwellAtHomeManager.m"
- "MOEmbedding.m"
- "MOEngagementHistoryManager.m"
- "MOEventBundleLabelCondition.m"
- "MOEventBundleLabelFormat.m"
- "MOEventBundleLabelLocalizer.m"
- "MOEventBundleLabelTemplate.m"
- "MOEventBundleManager.m"
- "MOEventBundleRanking.m"
- "MOEventBundleStore.m"
- "MOEventBundler.m"
- "MOEventData.m"
- "MOEventExtendedAtrributes.m"
- "MOEventManager.m"
- "MOEventPatternDetector.m"
- "MOEventPatternDetectorFeatureTransformerAggregateEvents.m"
- "MOEventRefreshScheduler.m"
- "MOEventStore.m"
- "MOFSMStore.m"
- "MOGraph.m"
- "MOHealthKitManager.m"
- "MOInteraction+_CDInteraction.m"
- "MOInteraction.m"
- "MOLifeEventManager.m"
- "MOManageServer.m"
- "MOMeasurementTransformer.m"
- "MOMediaPlay.m"
- "MOMediaPlaySession.m"
- "MOMetric.m"
- "MOMotionManager.m"
- "MONotifier.m"
- "MONowPlayingMediaManager.m"
- "MOPOICategoryStore.m"
- "MOPeopleDiscoveryManager.m"
- "MOPersistenceManager.m"
- "MOPhotoManager.m"
- "MOProactiveTravelManager.m"
- "MOPromptMetrics.m"
- "MORankingParams+CoreDataTransformable.m"
- "MORankingParamsMO+CoreDataClass.m"
- "MORoutineServiceManager.m"
- "MOSharedWithYouManager.m"
- "MOSignificantContactManager.m"
- "MOStringArrayTransformer.m"
- "MOSuggestedEventManager.m"
- "MOSummarizationParameters.m"
- "MOSummarizationUtilities.m"
- "MOTimeAtHomeParams.m"
- "MOTimeContextAnnotationManager.m"
- "MOTopicManager.m"
- "MOTrendBundler.m"
- "MOTrendsAnalyzerOptions.m"
- "MOTripAnnotationManager.m"
- "MOUserData.m"
- "MOXPCContext.m"
- "Media sessions grouped for title and day: %@"
- "PSSActionSuggestionsSnapshotDate"
- "PlatformInfoOverrideIsSeedBuild"
- "Retention profile for this refresh: %@ [FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d, GLP=%d]"
- "Tf,N,V_peopleCountMaxNormalized"
- "Tf,N,V_peopleCountWeightedAverageNormalized"
- "Tf,N,V_peopleCountWeightedSumNormalized"
- "Threshold profile: useExtendedProfile=%d (FeatureEnabled=%d, InternalEnabled=%d, Manual=%d, ActionSuggestionsEligible=%d, isInternalBuild=%d) for key: %@"
- "TitleAndDayGrouping: media session with description: %@"
- "Using CACHED useExtendedProfile=%d for key: %@ (expires in %.0fs)"
- "["
- "[THRESHOLD-CHANGE] KILLSWITCH MIGRATION complete - tracking cleared"
- "[THRESHOLD-CHANGE] KILLSWITCH MIGRATION: Reverting from extended to default retention"
- "[generateBehavioralPatternBundles] Behavioral pattern is disabled via feature flag"
- "[generateBehavioralPatternBundles] bundle subtype=%lu, subbundlecount=%lu, phenotypes=%{private}@"
- "[generateThematicSummarizationBundles] bundle subtype=%lu, subbundlecount=%lu, phenotypes=%{private}@"
- "]"
- "_fetchPreviousBundlesWithDateInterval:handler:"
- "_peopleCountMaxNormalized"
- "_peopleCountWeightedAverageNormalized"
- "_peopleCountWeightedSumNormalized"
- "fetchEventBundleWithGranularity:interfaceTypes:CompletionHandler:"
- "fetchFeatureStatusWithCompletion:"
- "finalizeDonationWithFeatureEnabled:handler:"
- "label confidence, label confidence score, %f, actionNameConfidence, %f, concurrentMediaActionNameConfidence, %f, backgroundActionNameConfidence, %@, placeNameConfidence, %f, bundle, %@"
- "label confidence, label confidence, %f, event bundle, %@"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "new conversation created for compound key: %@, for date %@, interaction count, %lu"
- "notDetermined"
- "peopleCountMaxNormalized"
- "peopleCountWeightedAverageNormalized"
- "peopleCountWeightedSumNormalized"
- "setPeopleCountMaxNormalized:"
- "setPeopleCountWeightedAverageNormalized:"
- "setPeopleCountWeightedSumNormalized:"
- "skipping fetching and rehydrating contact events"
- "skipping fetching and rehydrating life events"
- "skipping fetching and rehydrating music"
- "skipping fetching and rehydrating people density events"
- "skipping fetching and rehydrating photo memory"
- "skipping fetching and rehydrating prox"
- "skipping fetching and rehydrating state of mind"
- "skipping fetching and rehydrating workouts"
- "skipping fetching and saving motion events"
- "skipping fetching and saving screentime events"
- "skipping fetching and saving spotlight events"
- "skipping training, fetching and rehydrating visits"
- "spotlight event integration enablement param is set to %d"
- "start fetching and rehydrating contact events"
- "start fetching and rehydrating life events"
- "start fetching and rehydrating motion events"
- "start fetching and rehydrating music"
- "start fetching and rehydrating people density events"
- "start fetching and rehydrating photo memory"
- "start fetching and rehydrating prox"
- "start fetching and rehydrating screentime events"
- "start fetching and rehydrating spotlight events"
- "start fetching and rehydrating state of mind data"
- "start fetching and rehydrating workouts"
- "start training, fetching and rehydrating visits"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v40@0:8Q16@24@?32"
```
