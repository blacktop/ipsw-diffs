## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-655.0.0.0.0
-  __TEXT.__text: 0x89504
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x8d64
+658.0.0.0.0
+  __TEXT.__text: 0x897c4
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x8d74
   __TEXT.__const: 0x7c8
   __TEXT.__dlopen_cstrs: 0x649
-  __TEXT.__cstring: 0x8105
+  __TEXT.__cstring: 0x80d4
   __TEXT.__constg_swiftt: 0x2c8
   __TEXT.__swift5_typeref: 0x2ae
   __TEXT.__swift5_fieldmd: 0xe8

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0x664c
+  __TEXT.__oslogstring: 0x666c
   __TEXT.__gcc_except_tab: 0x1a30
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x20d0
+  __TEXT.__unwind_info: 0x20c8
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x13f6
-  __TEXT.__objc_methname: 0x13b74
+  __TEXT.__objc_methname: 0x13bc9
   __TEXT.__objc_methtype: 0x2972
   __TEXT.__objc_stubs: 0xdb00
-  __DATA_CONST.__got: 0x960
+  __DATA_CONST.__got: 0x968
   __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bf0
+  __DATA_CONST.__objc_selrefs: 0x4bf8
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x6ba0
-  __AUTH_CONST.__objc_const: 0xedc8
+  __AUTH_CONST.__cfstring: 0x6bc0
+  __AUTH_CONST.__objc_const: 0xedf8
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90

   __DATA.__objc_ivar: 0x5d0
   __DATA.__data: 0xb38
   __DATA.__bss: 0x7f0
-  __DATA_DIRTY.__objc_ivar: 0x504
+  __DATA_DIRTY.__objc_ivar: 0x508
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EF09F3B2-E612-33B4-83DB-90D9F199174F
-  Functions: 3117
-  Symbols:   10206
-  CStrings:  6378
+  UUID: 699B3154-7CC8-3581-9609-9BCE6FDDEC03
+  Functions: 3116
+  Symbols:   10200
+  CStrings:  6383
 
Symbols:
+ +[SettingsCellularUtils noDataConnectivityAvailableWithBSRecommendationCheck:]
+ -[PSUICellularPlanManagerCache getBootstrapState]
+ _OBJC_CLASS_$_PESettingsFeatureDescriptionCell
+ ___59-[PSUIAddCellularPlanSpecifier addCellularPlanCellPressed:]_block_invoke.44
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.472
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.473
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.478
+ ___block_literal_global.328
+ ___block_literal_global.440
+ ___block_literal_global.502
+ _objc_msgSend$getBootstrapState
+ _objc_msgSend$initAgentDataFromCellularInternetPath
+ _objc_msgSend$noDataConnectivityAvailableWithBSRecommendationCheck:
- +[SettingsCellularUtils noDataConnectivityAvailable]
- _NSClassFromString
- ___44-[PSUIVoLTESwitchSpecifier setVoLTEEnabled:]_block_invoke
- ___59-[PSUIAddCellularPlanSpecifier addCellularPlanCellPressed:]_block_invoke.38
- ___59-[PSUIAddCellularPlanSpecifier addCellularPlanCellPressed:]_block_invoke.45
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.468
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.469
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.474
- ___block_literal_global.325
- ___block_literal_global.436
- ___block_literal_global.498
- _nw_path_create_default_evaluator
- _nw_path_evaluator_cancel
- _nw_path_evaluator_copy_path
- _nw_path_evaluator_start
- _objc_msgSend$initAgentDataFromInternetPath:
- _objc_msgSend$isUsingBootstrapDataService
- _objc_msgSend$noDataConnectivityAvailable
CStrings:
+ "Bootstrap state: %@"
+ "Failed to get bootstrap state"
+ "T@\"CTBootstrapState\",R,N"
+ "_sdrLock"
+ "getBootstrapState"
+ "getBootstrapState failed:%@"
+ "initAgentDataFromCellularInternetPath"
+ "noDataConnectivityAvailableWithBSRecommendationCheck:"
- "SettingsCellularUI.SettingsCellularUIPlacardCell"
- "initAgentDataFromInternetPath:"
- "noDataConnectivityAvailable"
- "show wifi alert and reset isRequestingOngoing"

```
