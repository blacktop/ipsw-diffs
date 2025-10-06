## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-1238.1.3.0.0
-  __TEXT.__text: 0x64168
+1238.1.7.0.0
+  __TEXT.__text: 0x6410c
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x4124
+  __TEXT.__objc_methlist: 0x40f4
   __TEXT.__const: 0x2f4
   __TEXT.__gcc_except_tab: 0x13b0
-  __TEXT.__cstring: 0x82ba
-  __TEXT.__oslogstring: 0x2c10
+  __TEXT.__cstring: 0x830a
+  __TEXT.__oslogstring: 0x2c90
   __TEXT.__dlopen_cstrs: 0xf41
   __TEXT.__swift5_typeref: 0x188
   __TEXT.__swift5_capture: 0x1ac

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__unwind_info: 0x1738
   __TEXT.__eh_frame: 0x638
-  __TEXT.__objc_classname: 0x980
-  __TEXT.__objc_methname: 0xd384
+  __TEXT.__objc_classname: 0x962
+  __TEXT.__objc_methname: 0xd36d
   __TEXT.__objc_methtype: 0x107d
-  __TEXT.__objc_stubs: 0xa260
-  __DATA_CONST.__got: 0x960
-  __DATA_CONST.__const: 0x1a98
-  __DATA_CONST.__objc_classlist: 0x230
+  __TEXT.__objc_stubs: 0xa240
+  __DATA_CONST.__got: 0x968
+  __DATA_CONST.__const: 0x1ac8
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3230
+  __DATA_CONST.__objc_selrefs: 0x3220
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x890
   __AUTH_CONST.__const: 0xa10
-  __AUTH_CONST.__cfstring: 0x6e80
-  __AUTH_CONST.__objc_const: 0x6398
+  __AUTH_CONST.__cfstring: 0x6ec0
+  __AUTH_CONST.__objc_const: 0x62f0
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50

   __DATA.__data: 0x4c0
   __DATA.__bss: 0x508
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x550
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended
   - /System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SEService.framework/SEService

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3BE5367A-92F1-3197-BC1E-F5F07D1BB43D
-  Functions: 2015
-  Symbols:   7030
-  CStrings:  4577
+  UUID: A7E72642-7330-30A0-81CD-F4E3883F7D00
+  Functions: 2014
+  Symbols:   7025
+  CStrings:  4581
 
Symbols:
+ -[PUILocationServicesListController currentCoreRoutineStatus]
+ -[PUILocationServicesListController setCurrentCoreRoutineStatus:]
+ GCC_except_table17
+ GCC_except_table179
+ GCC_except_table18
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table33
+ _OBJC_CLASS_$_PESettingsFeatureDescriptionCell
+ _OBJC_IVAR_$_PUILocationServicesListController._currentCoreRoutineStatus
+ ___39-[PUILockdownModeController specifiers]_block_invoke
+ ___39-[PUILockdownModeController specifiers]_block_invoke_2
+ ___52-[PUILockdownModeController set2GEnabled:specifier:]_block_invoke.148
+ ___52-[PUILockdownModeController set2GEnabled:specifier:]_block_invoke_2.149
+ ___52-[PUILockdownModeController set2GEnabled:specifier:]_block_invoke_2.149.cold.1
+ ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.237
+ ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.237.cold.1
+ ___66-[PUILockdownModeController setLockdownModeEnabled:forAllDevices:]_block_invoke.218
+ ___73-[PUIProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.918
+ ___77-[PUILocationServicesAuthorizationLevelController updateCoreRoutineSettings:]_block_invoke.824
+ ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1004
+ ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1005
+ ___block_descriptor_40_e8_32s_e15_v16?0"NSURL"8ls32l8
+ ___block_literal_global.976
+ ___block_literal_global.987
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_PrivacySettingsUI
+ _objc_msgSend$currentCoreRoutineStatus
+ _objc_msgSend$pe_isSettingsFeatureDescriptionCellSupported
+ _objc_msgSend$setSettingsFeatureDescriptionURLAction:
- -[PUILocationSystemServicesListController currentCoreRoutineStatus]
- -[PUILocationSystemServicesListController setCurrentCoreRoutineStatus:]
- -[PUILockdownModeController didTapOnboardingCellLink:]
- -[PUILockdownModeOnboardingCell initWithStyle:reuseIdentifier:]
- -[PUILockdownModeOnboardingCell traitCollectionDidChange:]
- GCC_except_table16
- GCC_except_table177
- GCC_except_table200
- GCC_except_table201
- _OBJC_CLASS_$_PUILockdownModeOnboardingCell
- _OBJC_IVAR_$_PUILocationSystemServicesListController._currentCoreRoutineStatus
- _OBJC_METACLASS_$_PUILockdownModeOnboardingCell
- __OBJC_$_INSTANCE_METHODS_PUILockdownModeOnboardingCell
- __OBJC_CLASS_PROTOCOLS_$_PUILockdownModeController
- __OBJC_CLASS_RO_$_PUILockdownModeOnboardingCell
- __OBJC_METACLASS_RO_$_PUILockdownModeOnboardingCell
- ___52-[PUILockdownModeController set2GEnabled:specifier:]_block_invoke.139
- ___52-[PUILockdownModeController set2GEnabled:specifier:]_block_invoke_2.140
- ___52-[PUILockdownModeController set2GEnabled:specifier:]_block_invoke_2.140.cold.1
- ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.228
- ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.228.cold.1
- ___66-[PUILockdownModeController setLockdownModeEnabled:forAllDevices:]_block_invoke.209
- ___73-[PUIProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.915
- ___77-[PUILocationServicesAuthorizationLevelController updateCoreRoutineSettings:]_block_invoke.813
- ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1001
- ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1002
- ___block_literal_global.965
- ___block_literal_global.984
- _objc_msgSend$displayScale
- _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
- _objc_msgSend$initWithType:
- _objc_msgSend$prepareImageForDescriptor:
CStrings:
+ "%@ [%@](https://support.apple.com/kb/HT212650)"
+ "Not showing Preferred Routes because PreciseLocation is Off"
+ "Not showing Visited Places because PreciseLocation is Off"
+ "pe_isSettingsFeatureDescriptionCellSupported"
+ "setSettingsFeatureDescriptionURLAction:"
+ "telephony"
+ "v16@?0@\"NSURL\"8"
- "PUILockdownModeOnboardingCell"
- "displayScale"
- "hasDifferentColorAppearanceComparedToTraitCollection:"
- "initWithType:"
- "prepareImageForDescriptor:"

```
