## HealthToolbox

> `/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox`

```diff

-6074.1.2.4.0
-  __TEXT.__text: 0x5f884
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x6f50
+6087.1.2.1.0
+  __TEXT.__text: 0x5fdf8
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x6f88
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x7095
+  __TEXT.__cstring: 0x70a3
   __TEXT.__oslogstring: 0x1907
-  __TEXT.__gcc_except_tab: 0xaf8
+  __TEXT.__gcc_except_tab: 0xb10
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__unwind_info: 0x1918
   __TEXT.__objc_classname: 0x150d
-  __TEXT.__objc_methname: 0x12daa
-  __TEXT.__objc_methtype: 0x2d2d
-  __TEXT.__objc_stubs: 0xe600
+  __TEXT.__objc_methname: 0x12ee3
+  __TEXT.__objc_methtype: 0x2d36
+  __TEXT.__objc_stubs: 0xe700
   __DATA_CONST.__got: 0xb88
   __DATA_CONST.__const: 0x1720
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4658
+  __DATA_CONST.__objc_selrefs: 0x4698
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x2a0
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x5100
-  __AUTH_CONST.__objc_const: 0xb008
+  __AUTH_CONST.__objc_const: 0xb048
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0x2350
-  __DATA.__objc_ivar: 0x688
+  __DATA.__objc_ivar: 0x690
   __DATA.__data: 0xfc0
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x3c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 6A9202B7-9D4C-32A1-A243-9E076DBD2B6F
-  Functions: 2302
-  Symbols:   8736
-  CStrings:  5088
+  UUID: E4E2FCE9-3E04-3CA4-B5E4-9547809FE813
+  Functions: 2309
+  Symbols:   8760
+  CStrings:  5098
 
Symbols:
+ +[HBXHealthAppPluginFactory makeDataListDataProviderClassFromPluginName:displayType:hierarchical:]
+ -[WDBuddyFlowContinueFooterView layoutSubviews]
+ -[WDBuddyFlowUserInfoViewController viewDidLayoutSubviews]
+ -[WDBuddyFlowUserInfoViewController viewIsAppearing:]
+ -[WDDisplayTypeDataSourcesTableViewController _authorizationStatusesWithAuth:]
+ -[WDDisplayTypeDataSourcesTableViewController _fetchAuthorizationRecordsBySourceForType:]
+ -[WDDisplayTypeDataSourcesTableViewController _fetchBloodPressureAuthorizationRecordsBySource]
+ GCC_except_table32
+ GCC_except_table58
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table82
+ _OBJC_IVAR_$_WDBuddyFlowContinueFooterView._continueTrayButtonLeadingConstraint
+ _OBJC_IVAR_$_WDBuddyFlowContinueFooterView._continueTrayButtonTrailingConstraint
+ ___39-[WDExportManager _writeMedicalRecords]_block_invoke.400
+ ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.592
+ ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.592.cold.1
+ ___50-[WDExportManager createExportFileWithCompletion:]_block_invoke.370
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.324
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.324.cold.1
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.326
+ ___54-[WDSourceOrderController setOrderedSources:dataType:]_block_invoke.298
+ ___55-[WDDeviceStoredDataViewController deleteAllStoredData]_block_invoke.295
+ ___60-[WDElectrocardiogramFilterDataProvider _countQueryForType:]_block_invoke.385
+ ___61-[WDAppAccessListViewController _refreshAppAuthorizationData]_block_invoke.306
+ ___62-[WDDocumentOverviewViewController _recomputeTotalReportCount]_block_invoke.316
+ ___64-[WDSampleListDataProvider _requestNextPageOfDataForSampleType:]_block_invoke.317
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.303
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.303.cold.1
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.305
+ ___71-[WDStoredDataByCategoryViewController fetchEnabledStatusForPeripheral]_block_invoke.367
+ ___76-[WDAtrialFibrillationEventOverviewViewController recomputeTotalSampleCount]_block_invoke.360
+ ___77-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotifications]_block_invoke.309
+ ___79-[WDAtrialFibrillationEventOverviewViewController _getLatestAnalyzedSampleDate]_block_invoke.362
+ ___81-[WDDisplayTypeDataSourcesTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.450
+ ___89-[WDDisplayTypeDataSourcesTableViewController _fetchAuthorizationRecordsBySourceForType:]_block_invoke
+ ___90-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotificationsAndTachograms]_block_invoke.311
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319.cold.1
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319.cold.2
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.323
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.323.cold.1
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.325
+ ___block_descriptor_48_e8_32s40r_e29_v16?0"NSMutableDictionary"8lr40l8s32l8
+ ___block_literal_global.303
+ ___block_literal_global.309
+ ___block_literal_global.372
+ ___block_literal_global.386
+ ___block_literal_global.396
+ ___block_literal_global.457
+ ___block_literal_global.476
+ ___block_literal_global.492
+ ___block_literal_global.590
+ _objc_msgSend$_authorizationStatusesWithAuth:
+ _objc_msgSend$_fetchAuthorizationRecordsBySourceForType:
+ _objc_msgSend$_fetchBloodPressureAuthorizationRecordsBySource
+ _objc_msgSend$allowEditView
+ _objc_msgSend$hk_onboardingDirectionalEdgeInsets
+ _objc_msgSend$hk_onboardingListEdgeInsets
+ _objc_msgSend$hk_tableRowHeight
+ _objc_msgSend$isIPhone
+ _objc_msgSend$makeDataListDataProviderClassForDisplayType:hierarchical:
+ _objc_msgSend$makeDataListDataProviderClassFromPluginName:displayType:hierarchical:
+ _objc_msgSend$rowHeight
- +[HBXHealthAppPluginFactory makeDataListDataProviderClassFromPluginName:displayType:]
- -[WDQuantityListStatisticsDataProvider sampleTypes]
- GCC_except_table68
- GCC_except_table69
- GCC_except_table77
- _HKHealthUIBuddyDirectionalEdgeInsetsForSolarium
- ___39-[WDExportManager _writeMedicalRecords]_block_invoke.397
- ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.589
- ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.589.cold.1
- ___50-[WDExportManager createExportFileWithCompletion:]_block_invoke.367
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.321
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.321.cold.1
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.323
- ___54-[WDSourceOrderController setOrderedSources:dataType:]_block_invoke.295
- ___55-[WDDeviceStoredDataViewController deleteAllStoredData]_block_invoke.292
- ___60-[WDElectrocardiogramFilterDataProvider _countQueryForType:]_block_invoke.382
- ___61-[WDAppAccessListViewController _refreshAppAuthorizationData]_block_invoke.303
- ___62-[WDDisplayTypeDataSourcesTableViewController _loadDataSource]_block_invoke_4
- ___62-[WDDocumentOverviewViewController _recomputeTotalReportCount]_block_invoke.313
- ___64-[WDSampleListDataProvider _requestNextPageOfDataForSampleType:]_block_invoke.314
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.300
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.300.cold.1
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.302
- ___71-[WDStoredDataByCategoryViewController fetchEnabledStatusForPeripheral]_block_invoke.364
- ___76-[WDAtrialFibrillationEventOverviewViewController recomputeTotalSampleCount]_block_invoke.357
- ___77-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotifications]_block_invoke.306
- ___79-[WDAtrialFibrillationEventOverviewViewController _getLatestAnalyzedSampleDate]_block_invoke.359
- ___81-[WDDisplayTypeDataSourcesTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.448
- ___90-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotificationsAndTachograms]_block_invoke.308
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316.cold.1
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316.cold.2
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.320
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.320.cold.1
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.322
- ___block_descriptor_48_e8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
- ___block_literal_global.297
- ___block_literal_global.306
- ___block_literal_global.368
- ___block_literal_global.380
- ___block_literal_global.393
- ___block_literal_global.454
- ___block_literal_global.473
- ___block_literal_global.489
- ___block_literal_global.587
- _objc_msgSend$makeDataListDataProviderClassForDisplayType:
- _objc_msgSend$makeDataListDataProviderClassFromPluginName:displayType:
- _objc_msgSend$uppercaseStringWithLocale:
CStrings:
+ "!)"
+ "#28@0:8@\"HKDisplayType\"16B24"
+ "#28@0:8@16B24"
+ "#36@0:8@16@24B32"
+ "%"
+ "%1$@_DATA_TYPE_PROVIDERS_EXPLANATION_NO_REORDERING_%2$@"
+ "DATA_TYPE_PROVIDERS_EXPLANATION_NO_REORDERING"
+ "T@\"NSNumber\",&,N,V_availabilityStateCache"
+ "_authorizationStatusesWithAuth:"
+ "_continueTrayButtonLeadingConstraint"
+ "_continueTrayButtonTrailingConstraint"
+ "_fetchAuthorizationRecordsBySourceForType:"
+ "_fetchBloodPressureAuthorizationRecordsBySource"
+ "allowEditView"
+ "hk_onboardingDirectionalEdgeInsets"
+ "hk_onboardingListEdgeInsets"
+ "hk_tableRowHeight"
+ "isIPhone"
+ "makeDataListDataProviderClassForDisplayType:hierarchical:"
+ "makeDataListDataProviderClassFromPluginName:displayType:hierarchical:"
+ "rowHeight"
- "!("
- "#"
- "#24@0:8@\"HKDisplayType\"16"
- "#24@0:8@16"
- "#32@0:8@16@24"
- "%1$@_DATA_TYPE_PROVIDERS_VISION_EXPLANATION_%2$@"
- "DATA_TYPE_PROVIDERS_VISION_EXPLANATION"
- "T@\"NSNumber\",N,V_availabilityStateCache"
- "makeDataListDataProviderClassForDisplayType:"
- "makeDataListDataProviderClassFromPluginName:displayType:"
- "uppercaseStringWithLocale:"

```
