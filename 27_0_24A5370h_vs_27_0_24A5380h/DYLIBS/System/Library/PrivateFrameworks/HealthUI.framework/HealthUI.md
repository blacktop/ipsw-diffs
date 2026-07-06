## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-  __TEXT.__text: 0x43c3f0
-  __TEXT.__objc_methlist: 0x3b27c
-  __TEXT.__cstring: 0x2312f
-  __TEXT.__const: 0x8d44
-  __TEXT.__gcc_except_tab: 0x23a4
-  __TEXT.__oslogstring: 0x7385
+  __TEXT.__text: 0x44b090
+  __TEXT.__objc_methlist: 0x3b3c4
+  __TEXT.__const: 0x8db4
+  __TEXT.__gcc_except_tab: 0x23d4
+  __TEXT.__cstring: 0x2330f
+  __TEXT.__oslogstring: 0x7455
   __TEXT.__ustring: 0x56
   __TEXT.__dlopen_cstrs: 0x367
-  __TEXT.__swift5_typeref: 0x3488
-  __TEXT.__constg_swiftt: 0x4e84
-  __TEXT.__swift5_reflstr: 0x3066
-  __TEXT.__swift5_fieldmd: 0x3078
+  __TEXT.__constg_swiftt: 0x4ec8
+  __TEXT.__swift5_typeref: 0x3516
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__swift5_reflstr: 0x31a6
+  __TEXT.__swift5_fieldmd: 0x3100
   __TEXT.__swift5_assocty: 0x7e8
   __TEXT.__swift5_proto: 0x39c
-  __TEXT.__swift5_types: 0x3f0
-  __TEXT.__swift5_capture: 0x1150
+  __TEXT.__swift5_types: 0x3f4
+  __TEXT.__swift5_capture: 0x14a4
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__swift_as_entry: 0x7c
-  __TEXT.__swift_as_ret: 0x6c
-  __TEXT.__swift_as_cont: 0x11c
-  __TEXT.__unwind_info: 0xf110
-  __TEXT.__eh_frame: 0x3058
+  __TEXT.__swift_as_entry: 0x90
+  __TEXT.__swift_as_ret: 0x84
+  __TEXT.__swift_as_cont: 0x158
+  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__unwind_info: 0xf368
+  __TEXT.__eh_frame: 0x3388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7978
-  __DATA_CONST.__objc_classlist: 0x21a8
+  __DATA_CONST.__const: 0x7990
+  __DATA_CONST.__objc_classlist: 0x21b0
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x6c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18a10
+  __DATA_CONST.__objc_selrefs: 0x18aa0
   __DATA_CONST.__objc_protorefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x1870
   __DATA_CONST.__objc_arraydata: 0x2080
-  __DATA_CONST.__got: 0x3768
-  __AUTH_CONST.__const: 0x84b8
+  __DATA_CONST.__got: 0x3850
+  __AUTH_CONST.__const: 0x8bf0
   __AUTH_CONST.__cfstring: 0x1e9c0
-  __AUTH_CONST.__objc_const: 0x66040
+  __AUTH_CONST.__objc_const: 0x66280
   __AUTH_CONST.__objc_intobj: 0x2a00
   __AUTH_CONST.__objc_doubleobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0xf60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x3078
-  __AUTH.__objc_data: 0x18368
-  __AUTH.__data: 0x2628
-  __DATA.__objc_ivar: 0x4054
-  __DATA.__data: 0x8220
-  __DATA.__bss: 0x70c0
-  __DATA.__common: 0x250
-  __DATA_DIRTY.__objc_data: 0x15e0
-  __DATA_DIRTY.__bss: 0x48
+  __AUTH_CONST.__auth_got: 0x30d8
+  __AUTH.__objc_data: 0x183e0
+  __AUTH.__data: 0x2640
+  __DATA.__objc_ivar: 0x405c
+  __DATA.__data: 0x82d8
+  __DATA.__bss: 0x70b0
+  __DATA.__common: 0x260
+  __DATA_DIRTY.__objc_data: 0x1680
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClockKit.framework/ClockKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26132
-  Symbols:   67025
-  CStrings:  9205
+  Functions: 26351
+  Symbols:   67238
+  CStrings:  9219
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ +[HKSettingsAuthorizationFactory authorizationViewControllerWithSource:sourceAuthorizationController:healthStore:shareDescription:updateDescription:researchStudyUsageDescription:storedDataViewControllerProvider:backgroundAppRefreshStatusProvider:]
+ -[HKAuthorizationSettingsViewController _rebuildReadingTypeOrdering]
+ -[HKAuthorizationSettingsViewController _recomputeReadingOrderingAndSections]
+ -[HKAuthorizationSettingsViewController _shouldHideDocumentRowInReadingSection]
+ -[HKAuthorizationSettingsViewController authorizationControllerDidReloadDocumentAuthorizations:]
+ -[HKAuthorizationSettingsViewController commitPendingAuthorizationsWithCompletion:]
+ -[HKCalendarScrollViewController _frameForWeekView:atOriginY:]
+ -[HKInteractiveChartViewController objectTypeForDisplayType:]
+ -[HKSourceAuthorizationController _clampEnabledReadingSubtypeModesToParents]
+ -[HKSourceAuthorizationController _readingWindowForType:exceedsLimitedWindowStartingAt:]
+ -[HKSourceAuthorizationController _setAuthorizationStatuses:completion:]
+ -[HKSourceAuthorizationController _stagedReadingModeForType:]
+ -[HKSourceAuthorizationController _updateAuthorizationStatusWithTypes:completion:]
+ -[HKSourceAuthorizationController commitAuthorizationStatusesForTypes:]
+ -[HKSourceAuthorizationController commitAuthorizationStatusesWithCompletion:]
+ -[HKSourceAuthorizationController enabledSubtypesForType:inSection:]
+ -[HKSourceAuthorizationController setEnabled:forTypes:inSection:commit:]
+ GCC_except_table131
+ GCC_except_table139
+ GCC_except_table60
+ _OBJC_CLASS_$__TtCO8HealthUI17WorkoutZonesCells7Default
+ _OBJC_IVAR_$_HKAuthorizationSettingsViewController._shouldCommitOnFinish
+ _OBJC_IVAR_$_HKCalendarScrollViewController._lastLayoutHorizontalSafeArea
+ _OBJC_METACLASS_$__TtCO8HealthUI17WorkoutZonesCells7Default
+ __DATA__TtCO8HealthUI17WorkoutZonesCells7Default
+ __INSTANCE_METHODS__TtCO8HealthUI17WorkoutZonesCells7Default
+ __METACLASS_DATA__TtCO8HealthUI17WorkoutZonesCells7Default
+ __OBJC_$_INSTANCE_METHODS__TtC8HealthUI37HKSettingsAuthorizationViewController(HealthUI|HealthUI1|HealthUI2)
+ __OBJC_CLASS_PROTOCOLS_$__TtC8HealthUI37HKSettingsAuthorizationViewController(HealthUI|HealthUI1|HealthUI2)
+ ___70-[HKSourceAuthorizationController _reloadDocumentAuthorizationRecords]_block_invoke_2
+ ___72-[HKSourceAuthorizationController _setAuthorizationStatuses:completion:]_block_invoke
+ ___83-[HKAuthorizationSettingsViewController commitPendingAuthorizationsWithCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___swift_closure_destructor.18Tm
+ ___swift_closure_destructor.67Tm
+ ___swift_closure_destructor.74Tm
+ _objc_msgSend$_clampEnabledReadingSubtypeModesToParents
+ _objc_msgSend$_frameForWeekView:atOriginY:
+ _objc_msgSend$_readingWindowForType:exceedsLimitedWindowStartingAt:
+ _objc_msgSend$_rebuildReadingTypeOrdering
+ _objc_msgSend$_recomputeReadingOrderingAndSections
+ _objc_msgSend$_setAuthorizationStatuses:completion:
+ _objc_msgSend$_shouldHideDocumentRowInReadingSection
+ _objc_msgSend$_stagedReadingModeForType:
+ _objc_msgSend$_updateAuthorizationStatusWithTypes:completion:
+ _objc_msgSend$authorizationControllerDidReloadDocumentAuthorizations:
+ _objc_msgSend$commitAuthorizationStatusesForTypes:
+ _objc_msgSend$commitAuthorizationStatusesWithCompletion:
+ _objc_msgSend$enabledSubtypesForType:inSection:
+ _objc_msgSend$objectTypeForDisplayType:
+ _objc_msgSend$setAdoptedTableViewUsesAutomaticContentInsetAdjustment:
+ _objc_msgSend$setAuthorizationStatuses:authorizationModes:modeInfos:forBundleIdentifier:options:completion:
+ _objc_msgSend$setCellLayoutMarginsFollowReadableWidth:
+ _objc_msgSend$setEnabled:forTypes:inSection:commit:
+ _objc_msgSend$setResearchStudyUsageDescription:
+ _objc_msgSend$setSectionHeaderTopPadding:
+ _objc_msgSend$setShouldCommitOnFinish:
+ _objc_msgSend$setTitleStyle:
+ _objc_msgSend$shouldCommitOnFinish
+ _swift_release_x12
+ _symbolic SaySo12HKObjectTypeCG
+ _symbolic SaySo18NSLayoutConstraintCG
+ _symbolic So7NSErrorCSgIeyBhy_
+ _symbolic _____ 8HealthUI17WorkoutZonesCellsO7DefaultC
+ _symbolic _____Sg 9HealthKit31DarwinNotificationObserverTokenC
+ _symbolic _____SgXw 8HealthUI51ClinicalAuthorizationAccountsOverviewViewControllerC
+ _symbolic _____SgXwz_Xx 8HealthUI51ClinicalAuthorizationAccountsOverviewViewControllerC
+ _symbolic ______pSgIeghg_ s5ErrorP
+ _symbolic _____yScTyyt_____GSgG 15Synchronization5MutexVAARi_zrlE s5NeverO
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 8HealthUI016Xoroshiro256StarF033_C2E9D1CDEE51921DD7A4542007EFF122LLV
- +[HKSettingsAuthorizationFactory authorizationViewControllerWithSource:sourceAuthorizationController:healthStore:shareDescription:updateDescription:storedDataViewControllerProvider:backgroundAppRefreshStatusProvider:]
- -[HKSourceAuthorizationController _commitAuthorizationStatuses:authorizationModes:modeInfo:]
- -[HKSourceAuthorizationController _setAuthorizationStatuses:]
- -[HKSourceAuthorizationController _updateAuthorizationStatusWithTypes:]
- GCC_except_table138
- __OBJC_$_INSTANCE_METHODS__TtC8HealthUI37HKSettingsAuthorizationViewController(HealthUI|HealthUI1)
- __OBJC_CLASS_PROTOCOLS_$__TtC8HealthUI37HKSettingsAuthorizationViewController(HealthUI|HealthUI1)
- ___61-[HKSourceAuthorizationController _setAuthorizationStatuses:]_block_invoke
- ___92-[HKSourceAuthorizationController _commitAuthorizationStatuses:authorizationModes:modeInfo:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e55_v32?0"_HKAuthorizationModeInfo"8"NSDictionary"16^B24ls32l8s40l8
- ___swift_closure_destructor.13Tm
- _get_type_metadata 15Synchronization5MutexVy8HealthUI016Xoroshiro256StarF033_C2E9D1CDEE51921DD7A4542007EFF122LLVG noncopyable
- _get_type_metadata 15Synchronization5MutexVyScTyyts5NeverOGSgG noncopyable
- _objc_msgSend$_commitAuthorizationStatuses:authorizationModes:modeInfo:
- _objc_msgSend$_setAuthorizationStatuses:
- _objc_msgSend$_updateAuthorizationStatusWithTypes:
- _objc_msgSend$commitAuthorizationStatusForType:
- _objc_msgSend$isTranslucent
- _objc_msgSend$setAuthorizationStatuses:authorizationModes:modeInfo:forBundleIdentifier:options:completion:
- _swift_runtimeSupportsNoncopyableTypes
- _symbolic _____Sg 9HealthKit27HKPreferredWorkoutZoneStoreV
CStrings:
+ "%s returned to foreground, reloading accounts list"
+ "ALLOW_%@_TO_UPDATE_TITLECASED"
+ "AUTHORIZATION_CHARACTERISTICS_CATEGORY_HEADER"
+ "AUTHORIZATION_STATUS_LIMIT_%@"
+ "AUTHORIZATION_STATUS_RAISE_%@_TO_FULL"
+ "AUTHORIZATION_STATUS_RAISE_%@_TO_LIMITED"
+ "CYCLING_POWER_CONFIGURATION_WATTS_UNIT"
+ "Failed to fetch cycling power zone config: %{public}s"
+ "Failed to save CyclingPowerZonesConfiguration: %{public}s"
+ "LIMITING_%@_WILL_ALSO_LIMIT_%@"
+ "RAISING_%@_TO_FULL_WILL_RAISE_%@_TO_FULL"
+ "RAISING_%@_TO_LIMITED_WILL_RAISE_%@_TO_LIMITED"
+ "TIME_BOUNDED_AUTH_DISTINCT_DAYS_%ld"
+ "[CyclingPowerZones] Unsupported configurationType: %{public}s"
+ "queryDayDatesWithData(for:since:healthStore:)"
+ "queryEarliestSampleDate(for:healthStore:)"
- "Failed to fetch cycling power zone config: %@"
- "v32@?0@\"_HKAuthorizationModeInfo\"8@\"NSDictionary\"16^B24"

```
