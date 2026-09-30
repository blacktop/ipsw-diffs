## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-1227.0.0.0.0
-  __TEXT.__text: 0x63c80
-  __TEXT.__auth_stubs: 0x10e0
+1231.100.0.0.0
+  __TEXT.__text: 0x63a24
+  __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_methlist: 0x4134
-  __TEXT.__const: 0x2d4
-  __TEXT.__cstring: 0x828a
+  __TEXT.__const: 0x2c4
   __TEXT.__gcc_except_tab: 0x13b0
+  __TEXT.__cstring: 0x829a
   __TEXT.__oslogstring: 0x2bc0
   __TEXT.__dlopen_cstrs: 0xf41
-  __TEXT.__swift5_typeref: 0x188
-  __TEXT.__swift5_capture: 0x18c
   __TEXT.__constg_swiftt: 0x178
-  __TEXT.__swift5_reflstr: 0xb9
+  __TEXT.__swift5_typeref: 0x188
+  __TEXT.__swift5_reflstr: 0xc6
   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_capture: 0x18c
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x1738
+  __TEXT.__unwind_info: 0x1728
   __TEXT.__eh_frame: 0x638
-  __TEXT.__objc_classname: 0x998
-  __TEXT.__objc_methname: 0xd2a1
+  __TEXT.__objc_classname: 0x99e
+  __TEXT.__objc_methname: 0xd36b
   __TEXT.__objc_methtype: 0x107d
-  __TEXT.__objc_stubs: 0xa180
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__const: 0x1ac0
+  __TEXT.__objc_stubs: 0xa240
+  __DATA_CONST.__got: 0x968
+  __DATA_CONST.__const: 0x1aa8
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31f8
+  __DATA_CONST.__objc_selrefs: 0x3228
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x880
+  __AUTH_CONST.__auth_got: 0x888
   __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__cfstring: 0x6e40
-  __AUTH_CONST.__objc_const: 0x6468
+  __AUTH_CONST.__objc_const: 0x6428
   __AUTH_CONST.__objc_intobj: 0x330
-  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1208
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH.__objc_data: 0x1258
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x464
+  __DATA.__objc_ivar: 0x460
   __DATA.__data: 0x4c0
   __DATA.__bss: 0x508
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libTelephonyCapabilities.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D39A503F-0A7A-3B07-A17D-1BB63F260D0C
-  Functions: 2014
-  Symbols:   7045
-  CStrings:  4563
+  UUID: C73E729C-2853-3F62-BBDF-E1758B4A3596
+  Functions: 2017
+  Symbols:   7037
+  CStrings:  4569
 
Symbols:
+ +[PUILockdownModeCTCapabilities supportsBB2GMitigation]
+ -[PUILocationServicesAuthorizationLevelController addSignificantLocationsFooter:hyperlink:toSpecifier:]
+ -[PUILocationServicesListController _iconForLocationUsage:]
+ -[PUILocationServicesListController tableView:willDisplayCell:forRowAtIndexPath:]
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table176
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table83
+ _OBJC_CLASS_$_PUILockdownModeCTCapabilities
+ _OBJC_METACLASS_$_PUILockdownModeCTCapabilities
+ _PSToggleLeadingBadgeImageKey
+ __OBJC_$_CLASS_METHODS_PUILockdownModeCTCapabilities
+ __OBJC_CLASS_RO_$_PUILockdownModeCTCapabilities
+ __OBJC_METACLASS_RO_$_PUILockdownModeCTCapabilities
+ __ZN12capabilities2ct22supportsBB2GMitigationEv
+ ___54-[PUILocationServicesListController updateTribecaText]_block_invoke.514
+ ___54-[PUILocationServicesListController updateTribecaText]_block_invoke.514.cold.1
+ ___58-[PUILocationServicesListController updateLocationSharing]_block_invoke.511
+ ___61-[PUILocationServicesListController showCoreRoutineSettings:]_block_invoke.534
+ ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.228
+ ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.228.cold.1
+ ___63-[DiagnosticDataController _loadDiagnosticsDataWithCompletion:]_block_invoke.452
+ ___66-[PUILockdownModeController setLockdownModeEnabled:forAllDevices:]_block_invoke.209
+ ___67-[PUILocationServicesListController startUpdatingFindMyPreferences]_block_invoke.506
+ ___67-[PUILocationServicesListController startUpdatingFindMyPreferences]_block_invoke.508
+ ___73-[PUIProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.915
+ ___77-[PUILocationServicesAuthorizationLevelController updateCoreRoutineSettings:]_block_invoke.805
+ ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1001
+ ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1002
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.170
+ ___block_literal_global.153
+ ___block_literal_global.172
+ ___block_literal_global.221
+ ___block_literal_global.385
+ ___block_literal_global.505
+ ___block_literal_global.960
+ ___block_literal_global.984
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_destroy_helper.100
+ _objc_msgSend$_iconForLocationUsage:
+ _objc_msgSend$addSignificantLocationsFooter:hyperlink:toSpecifier:
+ _objc_msgSend$configurationWithHierarchicalColor:
+ _objc_msgSend$refreshCellContentsWithSpecifier:
+ _objc_msgSend$removePropertyForKey:
+ _objc_msgSend$supportsBB2GMitigation
+ _objectdestroy.29Tm
+ _objectdestroy.33Tm
- -[PUILocationServicesCell .cxx_destruct]
- -[PUILocationServicesCell initWithStyle:reuseIdentifier:specifier:]
- -[PUILocationServicesCell layoutSubviews]
- -[PUILocationServicesCell location]
- -[PUILocationServicesListController tableView:cellForRowAtIndexPath:]
- GCC_except_table111
- GCC_except_table124
- GCC_except_table129
- GCC_except_table133
- GCC_except_table179
- GCC_except_table201
- GCC_except_table202
- GCC_except_table62
- GCC_except_table64
- GCC_except_table67
- OBJC_IVAR_$_PSControlTableCell._control
- _OBJC_CLASS_$_PSSwitchTableCell
- _OBJC_CLASS_$_PUILocationServicesCell
- _OBJC_IVAR_$_PUILocationServicesCell._location
- _OBJC_METACLASS_$_PSSwitchTableCell
- _OBJC_METACLASS_$_PUILocationServicesCell
- __OBJC_$_INSTANCE_METHODS_PUILocationServicesCell
- __OBJC_$_INSTANCE_VARIABLES_PUILocationServicesCell
- __OBJC_$_PROP_LIST_PUILocationServicesCell
- __OBJC_CLASS_RO_$_PUILocationServicesCell
- __OBJC_METACLASS_RO_$_PUILocationServicesCell
- ___54-[PUILocationServicesListController updateTribecaText]_block_invoke.513
- ___54-[PUILocationServicesListController updateTribecaText]_block_invoke.513.cold.1
- ___58-[PUILocationServicesListController updateLocationSharing]_block_invoke.510
- ___61-[PUILocationServicesListController showCoreRoutineSettings:]_block_invoke.533
- ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.227
- ___62-[PUILockdownModeController getEligibleDevicesWithCompletion:]_block_invoke.227.cold.1
- ___63-[DiagnosticDataController _loadDiagnosticsDataWithCompletion:]_block_invoke.449
- ___66-[PUILockdownModeController setLockdownModeEnabled:forAllDevices:]_block_invoke.208
- ___67-[PUILocationServicesListController startUpdatingFindMyPreferences]_block_invoke.505
- ___67-[PUILocationServicesListController startUpdatingFindMyPreferences]_block_invoke.507
- ___73-[PUIProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.912
- ___77-[PUILocationServicesAuthorizationLevelController updateCoreRoutineSettings:]_block_invoke.799
- ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.998
- ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.999
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.169
- ___block_literal_global.152
- ___block_literal_global.171
- ___block_literal_global.231
- ___block_literal_global.284
- ___block_literal_global.390
- ___block_literal_global.504
- ___block_literal_global.956
- ___block_literal_global.981
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PrivacySettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PrivacySettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PrivacySettingsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PrivacySettingsUI
- _block_copy_helper.97
- _block_descriptor.99
- _block_destroy_helper.98
- _objectdestroy.27Tm
- _objectdestroy.31Tm
CStrings:
+ "ALLOW_MORE_LOCATION_ACCESS_FOOTER_LINK"
+ "ALLOW_MORE_LOCATION_ACCESS_HEADER"
+ "PREFERRED_ROUTES_FOOTER_WITH_LINK"
+ "PUILockdownModeCTCapabilities"
+ "_iconForLocationUsage:"
+ "addSignificantLocationsFooter:hyperlink:toSpecifier:"
+ "configurationWithHierarchicalColor:"
+ "removePropertyForKey:"
+ "supportsBB2GMitigation"
+ "tableView:willDisplayCell:forRowAtIndexPath:"
- "PREFERRED_ROUTES_FOOTER_LINK"
- "PREFERRED_ROUTES_FOOTER_LINK_LOCATION_PLUS"
- "PUILocationServicesCell"
- "VISITED_PLACES_HEADER"

```
