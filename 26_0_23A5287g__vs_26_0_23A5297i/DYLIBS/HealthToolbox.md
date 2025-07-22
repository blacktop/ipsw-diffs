## HealthToolbox

> `/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox`

```diff

-6093.0.0.0.0
+6100.0.0.0.0
   __TEXT.__text: 0x6042c
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_methlist: 0x6f68

   __TEXT.__ustring: 0x38
   __TEXT.__unwind_info: 0x1930
   __TEXT.__objc_classname: 0x150b
-  __TEXT.__objc_methname: 0x12fd4
+  __TEXT.__objc_methname: 0x12ff4
   __TEXT.__objc_methtype: 0x2cf3
-  __TEXT.__objc_stubs: 0xe740
+  __TEXT.__objc_stubs: 0xe760
   __DATA_CONST.__got: 0xb98
   __DATA_CONST.__const: 0x1780
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x46d8
+  __DATA_CONST.__objc_selrefs: 0x46e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x2a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: EE0E4906-98C0-31A6-BB72-5E028963DED7
+  UUID: 4CBF97A3-2602-3D59-B254-107A0B740E64
   Functions: 2312
-  Symbols:   8782
-  CStrings:  5109
+  Symbols:   8783
+  CStrings:  5110
 
Symbols:
+ ___39-[WDExportManager _writeMedicalRecords]_block_invoke.397
+ ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.589
+ ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.589.cold.1
+ ___50-[WDExportManager createExportFileWithCompletion:]_block_invoke.367
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.321
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.321.cold.1
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.323
+ ___54-[WDSourceOrderController setOrderedSources:dataType:]_block_invoke.295
+ ___55-[WDDeviceStoredDataViewController deleteAllStoredData]_block_invoke.292
+ ___60-[WDElectrocardiogramFilterDataProvider _countQueryForType:]_block_invoke.382
+ ___61-[WDAppAccessListViewController _refreshAppAuthorizationData]_block_invoke.303
+ ___62-[WDDocumentOverviewViewController _recomputeTotalReportCount]_block_invoke.313
+ ___64-[WDSampleListDataProvider _requestNextPageOfDataForSampleType:]_block_invoke.314
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.300
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.300.cold.1
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.302
+ ___71-[WDStoredDataByCategoryViewController fetchEnabledStatusForPeripheral]_block_invoke.364
+ ___76-[WDAtrialFibrillationEventOverviewViewController recomputeTotalSampleCount]_block_invoke.357
+ ___77-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotifications]_block_invoke.306
+ ___79-[WDAtrialFibrillationEventOverviewViewController _getLatestAnalyzedSampleDate]_block_invoke.359
+ ___81-[WDDisplayTypeDataSourcesTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.448
+ ___90-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotificationsAndTachograms]_block_invoke.308
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316.cold.1
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316.cold.2
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.320
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.320.cold.1
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.322
+ ___block_literal_global.297
+ ___block_literal_global.306
+ ___block_literal_global.370
+ ___block_literal_global.380
+ ___block_literal_global.393
+ ___block_literal_global.455
+ ___block_literal_global.473
+ ___block_literal_global.489
+ ___block_literal_global.587
+ _objc_msgSend$hk_showViewController:animated:
- ___39-[WDExportManager _writeMedicalRecords]_block_invoke.400
- ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.592
- ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.592.cold.1
- ___50-[WDExportManager createExportFileWithCompletion:]_block_invoke.370
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.324
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.324.cold.1
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.326
- ___54-[WDSourceOrderController setOrderedSources:dataType:]_block_invoke.298
- ___55-[WDDeviceStoredDataViewController deleteAllStoredData]_block_invoke.295
- ___60-[WDElectrocardiogramFilterDataProvider _countQueryForType:]_block_invoke.385
- ___61-[WDAppAccessListViewController _refreshAppAuthorizationData]_block_invoke.306
- ___62-[WDDocumentOverviewViewController _recomputeTotalReportCount]_block_invoke.316
- ___64-[WDSampleListDataProvider _requestNextPageOfDataForSampleType:]_block_invoke.317
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.303
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.303.cold.1
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.305
- ___71-[WDStoredDataByCategoryViewController fetchEnabledStatusForPeripheral]_block_invoke.367
- ___76-[WDAtrialFibrillationEventOverviewViewController recomputeTotalSampleCount]_block_invoke.360
- ___77-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotifications]_block_invoke.309
- ___79-[WDAtrialFibrillationEventOverviewViewController _getLatestAnalyzedSampleDate]_block_invoke.362
- ___81-[WDDisplayTypeDataSourcesTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.451
- ___90-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotificationsAndTachograms]_block_invoke.311
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319.cold.1
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319.cold.2
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.323
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.323.cold.1
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.325
- ___block_literal_global.303
- ___block_literal_global.309
- ___block_literal_global.373
- ___block_literal_global.386
- ___block_literal_global.396
- ___block_literal_global.458
- ___block_literal_global.476
- ___block_literal_global.492
- ___block_literal_global.590
CStrings:
+ "hk_showViewController:animated:"

```
