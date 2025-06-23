## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-639.0.0.0.0
-  __TEXT.__text: 0x868a4
+645.0.0.0.0
+  __TEXT.__text: 0x88a70
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x8a84
+  __TEXT.__objc_methlist: 0x8ccc
   __TEXT.__const: 0x7c8
   __TEXT.__dlopen_cstrs: 0x649
-  __TEXT.__cstring: 0x7ed9
+  __TEXT.__cstring: 0x810b
   __TEXT.__constg_swiftt: 0x2c8
-  __TEXT.__swift5_typeref: 0x2b0
+  __TEXT.__swift5_typeref: 0x2ae
   __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0x63f5
-  __TEXT.__gcc_except_tab: 0x19b0
+  __TEXT.__oslogstring: 0x64db
+  __TEXT.__gcc_except_tab: 0x1a30
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2060
+  __TEXT.__unwind_info: 0x20a8
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x13a1
-  __TEXT.__objc_methname: 0x131df
-  __TEXT.__objc_methtype: 0x2922
-  __TEXT.__objc_stubs: 0xd3a0
-  __DATA_CONST.__got: 0x900
-  __DATA_CONST.__const: 0x1118
-  __DATA_CONST.__objc_classlist: 0x470
+  __TEXT.__objc_classname: 0x13f1
+  __TEXT.__objc_methname: 0x139d0
+  __TEXT.__objc_methtype: 0x2972
+  __TEXT.__objc_stubs: 0xd9a0
+  __DATA_CONST.__got: 0x948
+  __DATA_CONST.__const: 0x1120
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a00
-  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_selrefs: 0x4ba0
+  __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x700
-  __AUTH_CONST.__const: 0x5e8
-  __AUTH_CONST.__cfstring: 0x6940
-  __AUTH_CONST.__objc_const: 0xe918
+  __AUTH_CONST.__const: 0x628
+  __AUTH_CONST.__cfstring: 0x6ba0
+  __AUTH_CONST.__objc_const: 0xecd8
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x1b90
+  __AUTH.__objc_data: 0x1c30
   __AUTH.__data: 0x298
-  __DATA.__objc_ivar: 0x5b0
+  __DATA.__objc_ivar: 0x5c8
   __DATA.__data: 0xb38
   __DATA.__bss: 0x7f0
-  __DATA_DIRTY.__objc_ivar: 0x4d8
+  __DATA_DIRTY.__objc_ivar: 0x4f8
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25FD945F-9E26-374B-A339-D396E713C279
-  Functions: 3049
-  Symbols:   9981
-  CStrings:  6231
+  UUID: 4AE93B0F-140E-356D-8151-6CDDC5CDC17F
+  Functions: 3099
+  Symbols:   10151
+  CStrings:  6354
 
Symbols:
+ +[PSUICellularUpdateStateMessageTableCell specifierForUpdateState:details:target:action:]
+ -[PSUICellularController _handleURL:withCompletion:]
+ -[PSUICellularController cellularUpdateLearnMoreTapped:]
+ -[PSUICellularController deferredURLState]
+ -[PSUICellularController handleResourcesDictionaryDidChange:]
+ -[PSUICellularController handleURLHandlerErrorDidChange:]
+ -[PSUICellularController launchTravelFlow:withType:]
+ -[PSUICellularController resourcesDictionaryObserver]
+ -[PSUICellularController setDeferredURLState:]
+ -[PSUICellularController setResourcesDictionaryObserver:]
+ -[PSUICellularController setUrlHandlerErrorObserver:]
+ -[PSUICellularController showLocalTime:]
+ -[PSUICellularController updateStateMessageCloseTapped:]
+ -[PSUICellularController urlHandlerErrorObserver]
+ -[PSUICellularDataOptionsController viewDidLoad]
+ -[PSUICellularDiagnosticsSpecifier getCellularUpdatedDetailsLink]
+ -[PSUICellularDiagnosticsSpecifier getCellularUpdatedTime]
+ -[PSUICellularDiagnosticsSpecifier updateBasebandConfigUpdateInfo]
+ -[PSUICellularUpdateStateMessageTableCell .cxx_destruct]
+ -[PSUICellularUpdateStateMessageTableCell _setupView:Context:target:CloseAction:]
+ -[PSUICellularUpdateStateMessageTableCell closeButton]
+ -[PSUICellularUpdateStateMessageTableCell detailTextLabel]
+ -[PSUICellularUpdateStateMessageTableCell getLogger]
+ -[PSUICellularUpdateStateMessageTableCell label]
+ -[PSUICellularUpdateStateMessageTableCell refreshCellContentsWithSpecifier:]
+ -[PSUICellularUpdateStateMessageTableCell setCloseButton:]
+ -[PSUICellularUpdateStateMessageTableCell setLabel:]
+ -[PSUICellularUpdateStateMessageTableCell setTitle:]
+ -[PSUICellularUpdateStateMessageTableCell textLabel]
+ -[PSUICellularUpdateStateMessageTableCell title]
+ -[PSUICoreTelephonyRadioCache basebandConfigUpdateDetails]
+ -[PSUICoreTelephonyRadioCache basebandConfigUpdateTime]
+ -[PSUICoreTelephonyRadioCache bbConfigUpdateStatusFetched]
+ -[PSUICoreTelephonyRadioCache checkBasebandConfigUpdateInfo]
+ -[PSUICoreTelephonyRadioCache getBasebandConfigUpdateDetails]
+ -[PSUICoreTelephonyRadioCache getBasebandConfigUpdateTime]
+ -[PSUICoreTelephonyRadioCache healthStatusFetched]
+ -[PSUICoreTelephonyRadioCache setBasebandConfigUpdateDetails:]
+ -[PSUICoreTelephonyRadioCache setBasebandConfigUpdateTime:]
+ -[PSUICoreTelephonyRadioCache setBbConfigUpdateStatusFetched:]
+ -[PSUICoreTelephonyRadioCache setHealthStatusFetched:]
+ -[PSUISettingsCellularDeferredURLState .cxx_destruct]
+ -[PSUISettingsCellularDeferredURLState resourcesDictionary]
+ -[PSUISettingsCellularDeferredURLState setResourcesDictionary:]
+ -[PSUISettingsCellularDeferredURLState setUrlHandlerError:]
+ -[PSUISettingsCellularDeferredURLState urlHandlerError]
+ -[PSUITotalCellularUsageSubgroup initWithStatisticsCache:andBillingPeriodSource:usageType:]
+ -[PSUITotalCellularUsageSubgroup setUsageType:]
+ -[PSUITotalCellularUsageSubgroup usageType]
+ GCC_except_table123
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table93
+ OBJC_IVAR_$_PSSpecifier.autoCapsType
+ _NSKeyValueChangeNewKey
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_PSUICellularUpdateStateMessageTableCell
+ _OBJC_CLASS_$_PSUISettingsCellularDeferredURLState
+ _OBJC_IVAR_$_PSUICoreTelephonyRadioCache._basebandConfigUpdateDetails
+ _OBJC_IVAR_$_PSUICoreTelephonyRadioCache._basebandConfigUpdateTime
+ _OBJC_IVAR_$_PSUICoreTelephonyRadioCache._bbConfigUpdateStatusFetched
+ _OBJC_IVAR_$_PSUICoreTelephonyRadioCache._healthStatusFetched
+ _OBJC_IVAR_$_PSUISettingsCellularDeferredURLState._resourcesDictionary
+ _OBJC_IVAR_$_PSUISettingsCellularDeferredURLState._urlHandlerError
+ _OBJC_IVAR_$_PSUITotalCellularUsageSubgroup._usageType
+ _OBJC_METACLASS_$_PSUICellularUpdateStateMessageTableCell
+ _OBJC_METACLASS_$_PSUISettingsCellularDeferredURLState
+ _PSUISettingsCellularDeferredURLStateKey
+ __OBJC_$_CLASS_METHODS_PSUICellularUpdateStateMessageTableCell
+ __OBJC_$_INSTANCE_METHODS_PSUICellularUpdateStateMessageTableCell
+ __OBJC_$_INSTANCE_METHODS_PSUISettingsCellularDeferredURLState
+ __OBJC_$_INSTANCE_VARIABLES_PSUICellularUpdateStateMessageTableCell
+ __OBJC_$_INSTANCE_VARIABLES_PSUISettingsCellularDeferredURLState
+ __OBJC_$_PROP_LIST_PSUICellularUpdateStateMessageTableCell
+ __OBJC_$_PROP_LIST_PSUISettingsCellularDeferredURLState
+ __OBJC_CLASS_RO_$_PSUICellularUpdateStateMessageTableCell
+ __OBJC_CLASS_RO_$_PSUISettingsCellularDeferredURLState
+ __OBJC_METACLASS_RO_$_PSUICellularUpdateStateMessageTableCell
+ __OBJC_METACLASS_RO_$_PSUISettingsCellularDeferredURLState
+ ___46-[PSUICellularController setDeferredURLState:]_block_invoke
+ ___46-[PSUICellularController setDeferredURLState:]_block_invoke_2
+ ___52-[PSUICellularController _handleURL:withCompletion:]_block_invoke
+ ___52-[PSUICellularController _handleURL:withCompletion:]_block_invoke.186
+ ___52-[PSUICellularController launchTravelFlow:withType:]_block_invoke
+ ___52-[PSUICellularController launchTravelFlow:withType:]_block_invoke_2
+ ___63-[PSUIRemoveCellularPlanSpecifier removeCellularPlanConfirmed:]_block_invoke.40
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.462
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.463
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.468
+ ___block_descriptor_32_e25_v24?08"NSDictionary"16l
+ ___block_literal_global.103
+ ___block_literal_global.172
+ ___block_literal_global.189
+ ___block_literal_global.216
+ ___block_literal_global.318
+ ___block_literal_global.430
+ ___block_literal_global.493
+ ___block_literal_global.67
+ _objc_msgSend$_handleURL:withCompletion:
+ _objc_msgSend$_setupView:Context:target:CloseAction:
+ _objc_msgSend$basebandConfigUpdateDetails
+ _objc_msgSend$basebandConfigUpdateTime
+ _objc_msgSend$bbConfigUpdateStatusFetched
+ _objc_msgSend$boldSystemFontOfSize:
+ _objc_msgSend$checkBasebandConfigUpdateInfo
+ _objc_msgSend$checkBasebandConfigUpdateInfo:
+ _objc_msgSend$configType
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$deferredURLState
+ _objc_msgSend$getBasebandConfigUpdateDetails
+ _objc_msgSend$getBasebandConfigUpdateTime
+ _objc_msgSend$getCellularUpdatedDetailsLink
+ _objc_msgSend$getCellularUpdatedTime
+ _objc_msgSend$handleResourcesDictionaryDidChange:
+ _objc_msgSend$handleURLHandlerErrorDidChange:
+ _objc_msgSend$healthStatusFetched
+ _objc_msgSend$imageByApplyingSymbolConfiguration:
+ _objc_msgSend$imageView
+ _objc_msgSend$initWithStatisticsCache:andBillingPeriodSource:usageType:
+ _objc_msgSend$launchTravelFlow:withType:
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$longLongValue
+ _objc_msgSend$na_addNotificationBlockObserverForObject:keyPath:options:usingBlock:
+ _objc_msgSend$na_removeNotificationBlockObserver:
+ _objc_msgSend$resourcesDictionary
+ _objc_msgSend$resourcesDictionaryObserver
+ _objc_msgSend$setBasebandConfigUpdateDetails:
+ _objc_msgSend$setBasebandConfigUpdateTime:
+ _objc_msgSend$setBbConfigUpdateStatusFetched:
+ _objc_msgSend$setContentHorizontalAlignment:
+ _objc_msgSend$setContentMode:
+ _objc_msgSend$setContentVerticalAlignment:
+ _objc_msgSend$setDeferredURLState:
+ _objc_msgSend$setHealthStatusFetched:
+ _objc_msgSend$setResourcesDictionary:
+ _objc_msgSend$setResourcesDictionaryObserver:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setUrlHandlerError:
+ _objc_msgSend$setUrlHandlerErrorObserver:
+ _objc_msgSend$showLocalTime:
+ _objc_msgSend$specifierForUpdateState:details:target:action:
+ _objc_msgSend$systemButtonWithImage:target:action:
+ _objc_msgSend$tertiaryLabelColor
+ _objc_msgSend$totalSatelliteUsageForPeriod:
+ _objc_msgSend$updateBasebandConfigUpdateInfo
+ _objc_msgSend$updatedDetails
+ _objc_msgSend$updatedTime
+ _objc_msgSend$urlHandlerError
+ _objc_msgSend$urlHandlerErrorObserver
+ _symbolic So16UINavigationItemC
- -[PSUICoreTelephonyRadioCache setStatusFetched:]
- -[PSUICoreTelephonyRadioCache statusFetched]
- -[PSUITotalCellularUsageSubgroup initWithStatisticsCache:andBillingPeriodSource:]
- GCC_except_table113
- GCC_except_table60
- GCC_except_table61
- GCC_except_table86
- _OBJC_IVAR_$_PSUICoreTelephonyRadioCache._statusFetched
- ___51-[PSUICellularController handleURL:withCompletion:]_block_invoke.162
- ___51-[PSUICellularController handleURL:withCompletion:]_block_invoke.177
- ___63-[PSUIRemoveCellularPlanSpecifier removeCellularPlanConfirmed:]_block_invoke.37
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.431
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.432
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.437
- ___block_literal_global.179
- ___block_literal_global.202
- ___block_literal_global.287
- ___block_literal_global.399
- ___block_literal_global.464
- ___block_literal_global.64
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SettingsCellularUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SettingsCellularUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SettingsCellularUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SettingsCellularUI
- _objc_msgSend$initWithStatisticsCache:andBillingPeriodSource:
- _objc_msgSend$setStatusFetched:
- _objc_msgSend$statusFetched
- _objc_msgSend$updateSpecifiers:withSpecifiers:
- _symbolic So16UINavigationItemCSg
CStrings:
+ "%s returning %@ roaming %f"
+ "%s returning %@ usage %f"
+ "-[PSUICellularController _handleURL:withCompletion:]"
+ "@\"PSUISettingsCellularDeferredURLState\""
+ "@48@0:8@16@24@32:40"
+ "Baseband config update info: type=%@, time=%@ details=%@"
+ "CELLULAR_SETTINGS_DELETE_ESIM"
+ "CELLULAR_UPDATED_MESSAGE"
+ "CELLULAR_UPDATED_MESSAGE_DETAILS"
+ "CELLULAR_UPDATED_MESSAGE_LEARN_MORE"
+ "CELLULAR_UPDATE_STATE_GROUP"
+ "CellularSettings.BasebandConfigUpdateTime"
+ "CellularUpdateStateMessageContextKey"
+ "CellularUpdateStateMessageTitleKey"
+ "Checking baseband config update info error: %@"
+ "Confirmed by user for the cellular config update %@"
+ "ENABLE_2G"
+ "ENABLE_2G_FOOTER"
+ "Learn More link tapped %@"
+ "PSUICellularUpdateStateMessageCloseAction"
+ "PSUICellularUpdateStateMessageCloseTarget"
+ "PSUICellularUpdateStateMessageTableCell"
+ "PSUISettingsCellularDeferredURLState"
+ "PSUISettingsCellularDeferredURLStateKey"
+ "Skip query and return baseband config update time %@"
+ "Skip to show as user already confirmed"
+ "T@\"NSDictionary\",C,N,V_resourcesDictionary"
+ "T@\"NSError\",&,N,V_urlHandlerError"
+ "T@\"NSString\",&,V_basebandConfigUpdateDetails"
+ "T@\"NSString\",&,V_basebandConfigUpdateTime"
+ "T@\"PSUISettingsCellularDeferredURLState\",&,N,V_deferredURLState"
+ "T@\"UIButton\",&,V_closeButton"
+ "T@,&,N,V_resourcesDictionaryObserver"
+ "T@,&,N,V_urlHandlerErrorObserver"
+ "TB,V_bbConfigUpdateStatusFetched"
+ "TB,V_healthStatusFetched"
+ "_basebandConfigUpdateDetails"
+ "_basebandConfigUpdateDetailsLink"
+ "_basebandConfigUpdateTime"
+ "_basebandConfigUpdateTimestamp"
+ "_bbConfigUpdateStatusFetched"
+ "_closeButton"
+ "_deferredURLState"
+ "_handleURL:withCompletion:"
+ "_healthStatusFetched"
+ "_resourcesDictionary"
+ "_resourcesDictionaryObserver"
+ "_setupView:Context:target:CloseAction:"
+ "_urlHandlerError"
+ "_urlHandlerErrorObserver"
+ "basebandConfigUpdateDetails"
+ "basebandConfigUpdateTime"
+ "bbConfigUpdateStatusFetched"
+ "boldSystemFontOfSize:"
+ "cellularUpdateLearnMoreTapped:"
+ "checkBasebandConfigUpdateInfo"
+ "checkBasebandConfigUpdateInfo:"
+ "closeButton"
+ "configType"
+ "configurationWithPointSize:weight:"
+ "current billing cycle"
+ "dateWithTimeIntervalSince1970:"
+ "deferredURLState"
+ "getBasebandConfigUpdateDetails"
+ "getBasebandConfigUpdateTime"
+ "getCellularUpdatedDetailsLink"
+ "getCellularUpdatedTime"
+ "handleResourcesDictionaryDidChange:"
+ "handleURLHandlerErrorDidChange:"
+ "healthStatusFetched"
+ "imageByApplyingSymbolConfiguration:"
+ "imageView"
+ "initWithStatisticsCache:andBillingPeriodSource:usageType:"
+ "launchTravelFlow:withType:"
+ "launching SIMSetup Travel Flow"
+ "launching SIMSetup enablement flow"
+ "launching cross platform flow"
+ "localTimeZone"
+ "longLongValue"
+ "na_addNotificationBlockObserverForObject:keyPath:options:usingBlock:"
+ "na_removeNotificationBlockObserver:"
+ "present view controller: %@"
+ "previous billing cycle"
+ "resourcesDictionary"
+ "resourcesDictionaryObserver"
+ "setBasebandConfigUpdateDetails:"
+ "setBasebandConfigUpdateTime:"
+ "setBbConfigUpdateStatusFetched:"
+ "setCloseButton:"
+ "setContentHorizontalAlignment:"
+ "setContentMode:"
+ "setContentVerticalAlignment:"
+ "setDeferredURLState:"
+ "setHealthStatusFetched:"
+ "setResourcesDictionary:"
+ "setResourcesDictionaryObserver:"
+ "setTimeZone:"
+ "setUrlHandlerError:"
+ "setUrlHandlerErrorObserver:"
+ "showLocalTime:"
+ "specifierForUpdateState:details:target:action:"
+ "systemButtonWithImage:target:action:"
+ "tertiaryLabelColor"
+ "total"
+ "totalSatelliteUsageForPeriod:"
+ "updateBasebandConfigUpdateInfo"
+ "updateStateMessageCloseTapped:"
+ "updatedDetails"
+ "updatedTime"
+ "url handle error:%@"
+ "urlHandlerError"
+ "urlHandlerErrorObserver"
+ "v24@?0@8@\"NSDictionary\"16"
+ "v48@0:8@16@24@32:40"
+ "xmark"
- "%s returning current billing cycle roaming %f"
- "%s returning current billing cycle usage %f"
- "%s returning previous billing cycle roaming %f"
- "%s returning previous billing cycle usage %f"
- "%s returning total roaming %f"
- "%s returning total usage %f"
- "-[PSUICellularController handleURL:withCompletion:]"
- "TB,V_statusFetched"
- "[PLACE_HOLDER]"
- "_statusFetched"
- "initWithStatisticsCache:andBillingPeriodSource:"
- "setStatusFetched:"
- "statusFetched"
- "updateSpecifiers:withSpecifiers:"

```
