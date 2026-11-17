## AppSystemSettingsUI

> `/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI`

```diff

-2027.2.1.0.0
-  __TEXT.__text: 0x26e88
-  __TEXT.__objc_methlist: 0xdbc
+2027.2.3.0.0
+  __TEXT.__text: 0x27730
+  __TEXT.__objc_methlist: 0xdd4
   __TEXT.__const: 0xe18
   __TEXT.__gcc_except_tab: 0x3fc
-  __TEXT.__cstring: 0x27bc
-  __TEXT.__oslogstring: 0xac5
+  __TEXT.__cstring: 0x27fc
+  __TEXT.__oslogstring: 0xb35
   __TEXT.__ustring: 0x2f6
   __TEXT.__dlopen_cstrs: 0xa7
   __TEXT.__constg_swiftt: 0x36c
-  __TEXT.__swift5_typeref: 0xc8c
+  __TEXT.__swift5_typeref: 0xc94
   __TEXT.__swift5_reflstr: 0x2d7
   __TEXT.__swift5_fieldmd: 0x1f8
   __TEXT.__swift5_capture: 0x218

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__unwind_info: 0xc90
+  __TEXT.__unwind_info: 0xca0
   __TEXT.__eh_frame: 0x900
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1000
+  __DATA_CONST.__objc_selrefs: 0x1018
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__got: 0x788
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__cfstring: 0x1720
   __AUTH_CONST.__objc_const: 0x18c0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xba0
+  __AUTH_CONST.__auth_got: 0xc08
   __AUTH.__objc_data: 0x348
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0xa0
-  __DATA.__data: 0x388
+  __DATA.__data: 0x398
   __DATA_DIRTY.__objc_data: 0x380
   __DATA_DIRTY.__data: 0x770
   __DATA_DIRTY.__bss: 0x610

   - /System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager
   - /System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore
   - /System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences
   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 789
-  Symbols:   1097
-  CStrings:  365
+  Functions: 794
+  Symbols:   1101
+  CStrings:  368
 
Symbols:
+ -[AUSystemSettingsSpecifiersProvider _isApprovedAuthorizationStatus:]
+ -[AUSystemSettingsSpecifiersProvider _supportsFamilyControlsDataAccess]
+ GCC_except_table104
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table147
+ GCC_except_table171
+ GCC_except_table56
+ GCC_except_table69
+ GCC_except_table86
+ GCC_except_table87
+ ___76-[AUSystemSettingsSpecifiersProvider setFamilyControlsEnabled:forSpecifier:]_block_invoke_2
+ _os_eligibility_get_domain_answer
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV6PolicyV
- GCC_except_table101
- GCC_except_table117
- GCC_except_table122
- GCC_except_table144
- GCC_except_table168
- GCC_except_table53
- GCC_except_table66
- GCC_except_table83
- GCC_except_table84
- _OUTLINED_FUNCTION_4
CStrings:
+ "Failed to check data access eligibility: %d"
+ "Failed to get application record for %{public}@: %{public}@"
+ "com.apple.developer.family-controls.app-and-website-usage"
```
