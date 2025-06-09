## HealthToolbox

> `/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x625ec
+6074.1.2.4.0
+  __TEXT.__text: 0x5f884
   __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x7458
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x72db
-  __TEXT.__oslogstring: 0x1dc7
-  __TEXT.__gcc_except_tab: 0xa84
-  __TEXT.__dlopen_cstrs: 0x44
+  __TEXT.__objc_methlist: 0x6f50
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x7095
+  __TEXT.__oslogstring: 0x1907
+  __TEXT.__gcc_except_tab: 0xaf8
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x1a18
-  __TEXT.__objc_classname: 0x160b
-  __TEXT.__objc_methname: 0x137c2
-  __TEXT.__objc_methtype: 0x2d67
-  __TEXT.__objc_stubs: 0xef80
-  __DATA_CONST.__got: 0xc08
-  __DATA_CONST.__const: 0x1790
-  __DATA_CONST.__objc_classlist: 0x420
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x158
+  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__objc_classname: 0x150d
+  __TEXT.__objc_methname: 0x12daa
+  __TEXT.__objc_methtype: 0x2d2d
+  __TEXT.__objc_stubs: 0xe600
+  __DATA_CONST.__got: 0xb88
+  __DATA_CONST.__const: 0x1720
+  __DATA_CONST.__objc_classlist: 0x3e8
+  __DATA_CONST.__objc_catlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48e0
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_selrefs: 0x4658
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x2a0
   __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5280
-  __AUTH_CONST.__objc_const: 0xbb60
-  __AUTH_CONST.__objc_intobj: 0x3a8
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x5100
+  __AUTH_CONST.__objc_const: 0xb008
+  __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x2490
-  __DATA.__objc_ivar: 0x6fc
-  __DATA.__data: 0x1020
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x20
+  __AUTH.__objc_data: 0x2350
+  __DATA.__objc_ivar: 0x688
+  __DATA.__data: 0xfc0
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI
+  - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
   - /System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 43AC27EA-B8EC-3790-B934-EE7C687D4D9F
-  Functions: 2426
-  Symbols:   9200
-  CStrings:  5275
+  UUID: 6A9202B7-9D4C-32A1-A243-9E076DBD2B6F
+  Functions: 2302
+  Symbols:   8736
+  CStrings:  5088
 
Symbols:
+ +[WDSourcesListTableViewSection _clinicalAuthorizationFamilyControllerWithAuthorizationController:healthRecordsStore:source:readUsageDescription:]
+ +[WDSourcesListTableViewSection _healthDataAuthorizationFamilyControllerWithHealthStore:source:healthAuthorizationViewController:]
+ +[WDSourcesListTableViewSection _healthDataAuthorizationViewControllerWithSourceModel:source:profile:]
+ +[WDSourcesListTableViewSection _medicationAuthorizationFamilyControllerWithSourceModel:healthStore:source:]
+ +[WDSourcesListTableViewSection createDetailViewControllerForSourceModel:profile:completion:]
+ -[HBXViewControllerFactory createDetailViewControllerForSourceModel:healthStore:completion:]
+ -[WDAppSourcesListTableViewSection _getSourceListToShow]
+ -[WDAppSourcesListTableViewSection _shouldShowUninstalledSourcesCell]
+ -[WDAppSourcesListTableViewSection initWithDelegate:atSection:]
+ -[WDAppSourcesListTableViewSection setSourcesStyle:]
+ -[WDAppSourcesListTableViewSection sourcesStyle]
+ -[WDAtrialFibrillationEventOverviewViewController _sectionHeaderViewWithTitle:identifier:]
+ -[WDAuthorizationSettingsViewController initWithProfile:style:source:shareDescription:updateDescription:researchStudyUsageDescription:]
+ -[WDDataListViewController gestureRecognizer:shouldReceiveTouch:]
+ -[WDDataListViewController viewDidDisappear:]
+ -[WDDeviceSourcesListTableViewSection _uuidStringForDevice:]
+ -[WDElectrocardiogramDataMetadataViewController deletionSectionDidSelectRow:sourceItem:]
+ -[WDElectrocardiogramInternalSettingsViewController _startFullOnboardingFromSourceItem:]
+ -[WDElectrocardiogramInternalSettingsViewController _startUpgradeFromSourceItem:]
+ -[WDElectrocardiogramOverviewViewController _sectionHeaderViewWithTitle:identifier:]
+ -[WDSourcesListTableViewSection createDetailViewControllerForSourceModel:completion:]
+ -[WDStoredDataByCategoryViewController presentDeleteConfirmationFromSender:]
+ GCC_except_table0
+ GCC_except_table102
+ GCC_except_table37
+ GCC_except_table55
+ GCC_except_table65
+ GCC_except_table74
+ _HKCollectionViewLayoutDefaultLayoutMarginsForWidthDesignation
+ _HKHealthUIBuddyDirectionalEdgeInsetsForSolarium
+ _OBJC_CLASS_$_HAServicesDefines
+ _OBJC_CLASS_$_HKMedicationAuthorizationController
+ _OBJC_CLASS_$_HKMedicationAuthorizationSettingsViewController
+ _OBJC_CLASS_$_HKSourceAuthorizationFamilyController
+ _OBJC_CLASS_$_UIControl
+ _OBJC_IVAR_$_WDAppSourcesListTableViewSection._sourcesStyle
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIGestureRecognizerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIGestureRecognizerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIGestureRecognizerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIGestureRecognizerDelegate
+ __OBJC_PROTOCOL_$_UIGestureRecognizerDelegate
+ __UISolariumEnabled
+ ___39-[WDExportManager _writeMedicalRecords]_block_invoke.397
+ ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.589
+ ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.589.cold.1
+ ___50-[WDExportManager createExportFileWithCompletion:]_block_invoke.367
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.321
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.321.cold.1
+ ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.323
+ ___54-[WDSourceOrderController setOrderedSources:dataType:]_block_invoke.295
+ ___55-[WDDeviceStoredDataViewController deleteAllStoredData]_block_invoke.292
+ ___56-[WDAppSourcesListTableViewSection _getSourceListToShow]_block_invoke
+ ___60-[WDElectrocardiogramFilterDataProvider _countQueryForType:]_block_invoke.382
+ ___61-[WDAppAccessListViewController _refreshAppAuthorizationData]_block_invoke.303
+ ___62-[WDDocumentOverviewViewController _recomputeTotalReportCount]_block_invoke.313
+ ___64-[WDSampleListDataProvider _requestNextPageOfDataForSampleType:]_block_invoke.314
+ ___65-[WDResearchStudySourcesListTableViewSection dataSourceDidUpdate]_block_invoke
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.300
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.300.cold.1
+ ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.302
+ ___71-[WDStoredDataByCategoryViewController fetchEnabledStatusForPeripheral]_block_invoke.364
+ ___76-[WDAtrialFibrillationEventOverviewViewController recomputeTotalSampleCount]_block_invoke.357
+ ___76-[WDStoredDataByCategoryViewController presentDeleteConfirmationFromSender:]_block_invoke
+ ___77-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotifications]_block_invoke.306
+ ___79-[WDAtrialFibrillationEventOverviewViewController _getLatestAnalyzedSampleDate]_block_invoke.359
+ ___81-[WDDisplayTypeDataSourcesTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.448
+ ___82-[WDAppSourcesListTableViewSection didSelectRow:representedByCell:withCompletion:]_block_invoke
+ ___88-[WDElectrocardiogramDataMetadataViewController deletionSectionDidSelectRow:sourceItem:]_block_invoke
+ ___90-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotificationsAndTachograms]_block_invoke.308
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316.cold.1
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.316.cold.2
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.320
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.320.cold.1
+ ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.322
+ ___92-[WDResearchStudySourcesListTableViewSection didSelectRow:representedByCell:withCompletion:]_block_invoke
+ ___93+[WDSourcesListTableViewSection createDetailViewControllerForSourceModel:profile:completion:]_block_invoke
+ ___block_descriptor_40_e8_32w_e26_v16?0"UIViewController"8lw32l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.300
+ ___block_literal_global.306
+ ___block_literal_global.368
+ ___block_literal_global.383
+ ___block_literal_global.393
+ ___block_literal_global.454
+ ___block_literal_global.473
+ ___block_literal_global.489
+ ___block_literal_global.587
+ _objc_msgSend$_clinicalAuthorizationFamilyControllerWithAuthorizationController:healthRecordsStore:source:readUsageDescription:
+ _objc_msgSend$_getSourceListToShow
+ _objc_msgSend$_healthDataAuthorizationFamilyControllerWithHealthStore:source:healthAuthorizationViewController:
+ _objc_msgSend$_healthDataAuthorizationViewControllerWithSourceModel:source:profile:
+ _objc_msgSend$_isHiddenSource
+ _objc_msgSend$_medicationAuthorizationFamilyControllerWithSourceModel:healthStore:source:
+ _objc_msgSend$_sectionHeaderViewWithTitle:identifier:
+ _objc_msgSend$_shouldShowUninstalledSourcesCell
+ _objc_msgSend$_startFullOnboardingFromSourceItem:
+ _objc_msgSend$_startUpgradeFromSourceItem:
+ _objc_msgSend$_uuidStringForDevice:
+ _objc_msgSend$bluetoothIdentifier
+ _objc_msgSend$createDetailViewControllerForSourceModel:completion:
+ _objc_msgSend$createDetailViewControllerForSourceModel:profile:completion:
+ _objc_msgSend$healthSettingsSourcesSpecifier
+ _objc_msgSend$hk_addNonNilObject:
+ _objc_msgSend$hk_safeAreaAdjustedEdgeInsets:
+ _objc_msgSend$initWithController:source:healthStore:
+ _objc_msgSend$initWithProfile:style:source:shareDescription:updateDescription:researchStudyUsageDescription:
+ _objc_msgSend$internalHealthSettingsURLTo:
+ _objc_msgSend$internalPrivacySettingsURLString
+ _objc_msgSend$isPinnedInBrowse
+ _objc_msgSend$isiPad
+ _objc_msgSend$presentDeleteConfirmationFromSender:
+ _objc_msgSend$reload
+ _objc_msgSend$reloadWithCompletion:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$setController:
+ _objc_msgSend$setFamilyControllers:
+ _objc_msgSend$setSourcesStyle:
+ _objc_msgSend$setUseSolariumDesign:
+ _objc_msgSend$setViewController:
+ _objc_msgSend$sourcesStyle
+ _objc_msgSend$viewController
- +[WDEmptyUserActivityResponder emptyUserActivityResponder]
- +[WDEmptyUserActivityResponder emptyUserActivityResponder].cold.1
- +[WDNotificationManager initialize]
- +[WDNotificationManager initialize].cold.1
- +[WDNotificationManager setSuppressBadgeNotifications:]
- +[WDNotificationManager suppressBadgeNotifications]
- +[WDSourcesListTableViewSection detailViewControllerForSourceModel:withProfile:]
- -[HBXShimWDProfile userActivityManager]
- -[HBXViewControllerFactory createContactConsolidationControllerInViewController:]
- -[HBXViewControllerFactory detailViewControllerForSourceModel:withHealthStore:]
- -[HBXViewControllerFactory notificationManager]
- -[UNNotification(HealthKit) wd_domain]
- -[UNNotification(HealthKit) wd_url]
- -[UNNotification(HealthKit) wd_userInfo]
- -[WDAppSourcesListTableViewSection setUninstalledSourcesExist:]
- -[WDAppSourcesListTableViewSection uninstalledSourcesExist]
- -[WDAtrialFibrillationEventOverviewViewController _sectionHeaderViewWithTitle:]
- -[WDAtrialFibrillationEventOverviewViewController dealloc]
- -[WDAuthorizationSettingsViewController initWithProfile:style:]
- -[WDBuddyFlowUserInfoViewController applyChangeActivity:]
- -[WDBuddyFlowUserInfoViewController applyTransitionActivity:]
- -[WDContactConsolidationController .cxx_destruct]
- -[WDContactConsolidationController _consolidateSOSContactsWithMedicalIDContacts]
- -[WDContactConsolidationController _showLearnMoreViewController]
- -[WDContactConsolidationController checkAlertNecessity]
- -[WDContactConsolidationController completionHandler]
- -[WDContactConsolidationController consolidationAlertController]
- -[WDContactConsolidationController healthStore]
- -[WDContactConsolidationController initWithProfile:presentingViewController:]
- -[WDContactConsolidationController isPresentingConsolidationAlert]
- -[WDContactConsolidationController medicalIDData]
- -[WDContactConsolidationController notificationManager]
- -[WDContactConsolidationController presentContactConsolidationAlertWithCompletionHandler:]
- -[WDContactConsolidationController presentContactsConsolidationAlert]
- -[WDContactConsolidationController presentingViewController]
- -[WDContactConsolidationController setCompletionHandler:]
- -[WDContactConsolidationController setConsolidationAlertController:]
- -[WDContactConsolidationController setHealthStore:]
- -[WDContactConsolidationController setMedicalIDData:]
- -[WDContactConsolidationController setNotificationManager:]
- -[WDContactConsolidationController setPresentingViewController:]
- -[WDContactConsolidationController setSosContactsManager:]
- -[WDContactConsolidationController sosContactsManager]
- -[WDContactConsolidationLearnMoreViewController .cxx_destruct]
- -[WDContactConsolidationLearnMoreViewController createDismissButton]
- -[WDContactConsolidationLearnMoreViewController createTextView]
- -[WDContactConsolidationLearnMoreViewController dismissButtonPressed:]
- -[WDContactConsolidationLearnMoreViewController dismissHandler]
- -[WDContactConsolidationLearnMoreViewController setDismissHandler:]
- -[WDContactConsolidationLearnMoreViewController setTextView:]
- -[WDContactConsolidationLearnMoreViewController textView]
- -[WDContactConsolidationLearnMoreViewController viewDidLoad]
- -[WDContactConsolidationLearnMoreViewController viewWillAppear:]
- -[WDDataListViewController _updateActivityForViewDidAppear]
- -[WDDataListViewController applyChangeActivity:]
- -[WDDataListViewController applyTransitionActivity:]
- -[WDDocumentOverviewViewController _updateActivityForViewDidAppear]
- -[WDDocumentOverviewViewController applyChangeActivity:]
- -[WDDocumentOverviewViewController applyTransitionActivity:]
- -[WDElectrocardiogramDataMetadataViewController deletionSectionDidSelectRow:]
- -[WDElectrocardiogramInternalSettingsViewController _startFullOnboarding]
- -[WDElectrocardiogramInternalSettingsViewController _startUpgrade]
- -[WDElectrocardiogramOverviewViewController _sectionHeaderViewWithTitle:]
- -[WDEmptyUserActivityResponder applyChangeActivity:]
- -[WDEmptyUserActivityResponder applyTransitionActivity:]
- -[WDFixedChartViewController .cxx_destruct]
- -[WDFixedChartViewController applyChangeActivity:]
- -[WDFixedChartViewController applyTransitionActivity:]
- -[WDFixedChartViewController cellForChart]
- -[WDFixedChartViewController chartController]
- -[WDFixedChartViewController fixedRange]
- -[WDFixedChartViewController initWithInteractiveChartViewController:sessionSample:profile:title:]
- -[WDFixedChartViewController metadataSection]
- -[WDFixedChartViewController numberOfSectionsInTableView:]
- -[WDFixedChartViewController tableView:cellForRowAtIndexPath:]
- -[WDFixedChartViewController tableView:heightForHeaderInSection:]
- -[WDFixedChartViewController tableView:numberOfRowsInSection:]
- -[WDFixedChartViewController tableView:shouldHighlightRowAtIndexPath:]
- -[WDFixedChartViewController tableView:willSelectRowAtIndexPath:]
- -[WDFixedChartViewController viewDidLoad]
- -[WDNotificationManager .cxx_destruct]
- -[WDNotificationManager _lock_policyForNotification:]
- -[WDNotificationManager healthStore]
- -[WDNotificationManager initWithHealthStore:]
- -[WDNotificationManager setBadge:forDomain:completion:]
- -[WDNotificationManager setPolicy:forDomain:]
- -[WDNotificationManager userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]
- -[WDNotificationManager userNotificationCenter:openSettingsForNotification:]
- -[WDNotificationManager userNotificationCenter:willPresentNotification:withCompletionHandler:]
- -[WDNotificationManager(Convenience) resetEmergencySOSBadge]
- -[WDNotificationManager(Convenience) resetHealthRecordsDataBadge]
- -[WDProfile notificationManager]
- -[WDProfile notificationManager].cold.1
- -[WDProfile userActivityManager]
- -[WDSourcesListTableViewSection detailViewControllerForSourceModel:]
- -[WDSourcesViewController _updateActivityForViewDidAppear]
- -[WDSourcesViewController applyChangeActivity:]
- -[WDSourcesViewController applyTransitionActivity:]
- -[WDSourcesViewController uniqueUserActivityType]
- -[WDStoredDataByCategoryViewController presentDeleteConfirmation]
- -[WDUserActivityManager .cxx_destruct]
- -[WDUserActivityManager _resetActivities]
- -[WDUserActivityManager _restoreActivityFromPolicies:]
- -[WDUserActivityManager _restoreFromActivityChain:]
- -[WDUserActivityManager _restoreFromActivityChain:].cold.1
- -[WDUserActivityManager _setCurrentNodeToResponder:]
- -[WDUserActivityManager _userActivityWithTitle:keywords:activityType:]
- -[WDUserActivityManager _userActivityWithType:]
- -[WDUserActivityManager addPolicy:]
- -[WDUserActivityManager changeActivityForResponder:activityDictionary:title:keywords:]
- -[WDUserActivityManager decodeRestorableStateWithCoder:]
- -[WDUserActivityManager encodeRestorableStateWithCoder:]
- -[WDUserActivityManager init]
- -[WDUserActivityManager policies]
- -[WDUserActivityManager recordActivities]
- -[WDUserActivityManager restoreFromUserActivity:]
- -[WDUserActivityManager setRecordActivities:]
- -[WDUserActivityManager setRootViewController:]
- -[WDUserActivityManager transitionActivityForResponder:newResponder:transitionDictionary:]
- -[_WDActivityNode .cxx_destruct]
- -[_WDActivityNode _nextNode]
- -[_WDActivityNode addActivitiesToArray:currentNode:]
- -[_WDActivityNode changeActivityForResponder:activityDictionary:]
- -[_WDActivityNode description]
- -[_WDActivityNode initWithResponder:]
- -[_WDActivityNode nextResponder]
- -[_WDActivityNode responder]
- -[_WDActivityNode setNextResponder:]
- -[_WDActivityNode setResponder:]
- -[_WDActivityNode transitionActivityForResponder:newResponder:transitionDictionary:]
- GCC_except_table103
- GCC_except_table13
- GCC_except_table16
- GCC_except_table36
- GCC_except_table48
- GCC_except_table53
- GCC_except_table63
- GCC_except_table72
- _HKHealthAppActivityType
- _HKHealthUIBuddyDirectionalEdgeInsets
- _HKLogHealthRecords
- _HKLogMedicalID
- _HKUILegacySOSContactsExistKey
- _OBJC_CLASS_$_CNContactStore
- _OBJC_CLASS_$_HKBadge
- _OBJC_CLASS_$_HKCollectionViewLayoutEngineDefaults
- _OBJC_CLASS_$_HKNotificationStore
- _OBJC_CLASS_$_HKViewTableViewCell
- _OBJC_CLASS_$_NSMapTable
- _OBJC_CLASS_$_NSUserActivity
- _OBJC_CLASS_$_UNNotification
- _OBJC_CLASS_$_WDContactConsolidationController
- _OBJC_CLASS_$_WDContactConsolidationLearnMoreViewController
- _OBJC_CLASS_$_WDEmptyUserActivityResponder
- _OBJC_CLASS_$_WDFixedChartViewController
- _OBJC_CLASS_$_WDNotificationManager
- _OBJC_CLASS_$_WDUserActivityManager
- _OBJC_CLASS_$__HKMedicalIDData
- _OBJC_CLASS_$__WDActivityNode
- _OBJC_IVAR_$_WDAppSourcesListTableViewSection._uninstalledSourcesExist
- _OBJC_IVAR_$_WDContactConsolidationController._completionHandler
- _OBJC_IVAR_$_WDContactConsolidationController._consolidationAlertController
- _OBJC_IVAR_$_WDContactConsolidationController._healthStore
- _OBJC_IVAR_$_WDContactConsolidationController._medicalIDData
- _OBJC_IVAR_$_WDContactConsolidationController._notificationManager
- _OBJC_IVAR_$_WDContactConsolidationController._presentingViewController
- _OBJC_IVAR_$_WDContactConsolidationController._sosContactsManager
- _OBJC_IVAR_$_WDContactConsolidationLearnMoreViewController._dismissHandler
- _OBJC_IVAR_$_WDContactConsolidationLearnMoreViewController._textView
- _OBJC_IVAR_$_WDFixedChartViewController._chartController
- _OBJC_IVAR_$_WDFixedChartViewController._fixedRange
- _OBJC_IVAR_$_WDFixedChartViewController._metadataSection
- _OBJC_IVAR_$_WDNotificationManager._domainsToPolicies
- _OBJC_IVAR_$_WDNotificationManager._healthStore
- _OBJC_IVAR_$_WDNotificationManager._lock
- _OBJC_IVAR_$_WDNotificationManager._notificationStore
- _OBJC_IVAR_$_WDProfile._notificationManager
- _OBJC_IVAR_$_WDProfile._userActivityManager
- _OBJC_IVAR_$_WDUserActivityManager._currentNode
- _OBJC_IVAR_$_WDUserActivityManager._indexedActivities
- _OBJC_IVAR_$_WDUserActivityManager._policies
- _OBJC_IVAR_$_WDUserActivityManager._recordActivities
- _OBJC_IVAR_$_WDUserActivityManager._rootViewController
- _OBJC_IVAR_$_WDUserActivityManager._topNode
- _OBJC_IVAR_$__WDActivityNode._nextResponder
- _OBJC_IVAR_$__WDActivityNode._nextResponderActivity
- _OBJC_IVAR_$__WDActivityNode._responder
- _OBJC_IVAR_$__WDActivityNode._responderActivity
- _OBJC_IVAR_$__WDActivityNode._responderTable
- _OBJC_METACLASS_$_WDContactConsolidationController
- _OBJC_METACLASS_$_WDContactConsolidationLearnMoreViewController
- _OBJC_METACLASS_$_WDEmptyUserActivityResponder
- _OBJC_METACLASS_$_WDFixedChartViewController
- _OBJC_METACLASS_$_WDNotificationManager
- _OBJC_METACLASS_$_WDUserActivityManager
- _OBJC_METACLASS_$__WDActivityNode
- _SOSLibrary
- _SOSLibraryCore.frameworkLibrary
- _WDAsUserActivityResponder
- _WDNotificationManagerBadgesDidUpdateNotificationName
- _WDUserActivityBreadcrumbKey
- _WDUserActivityRestorationIdentifier
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UNNotification_$_HealthKit
- __OBJC_$_CATEGORY_UNNotification_$_HealthKit
- __OBJC_$_CLASS_METHODS_WDEmptyUserActivityResponder
- __OBJC_$_CLASS_METHODS_WDNotificationManager
- __OBJC_$_CLASS_PROP_LIST_WDNotificationManager
- __OBJC_$_INSTANCE_METHODS_WDContactConsolidationController
- __OBJC_$_INSTANCE_METHODS_WDContactConsolidationLearnMoreViewController
- __OBJC_$_INSTANCE_METHODS_WDEmptyUserActivityResponder
- __OBJC_$_INSTANCE_METHODS_WDFixedChartViewController
- __OBJC_$_INSTANCE_METHODS_WDNotificationManager(Convenience)
- __OBJC_$_INSTANCE_METHODS_WDUserActivityManager
- __OBJC_$_INSTANCE_METHODS__WDActivityNode
- __OBJC_$_INSTANCE_VARIABLES_WDContactConsolidationController
- __OBJC_$_INSTANCE_VARIABLES_WDContactConsolidationLearnMoreViewController
- __OBJC_$_INSTANCE_VARIABLES_WDFixedChartViewController
- __OBJC_$_INSTANCE_VARIABLES_WDNotificationManager
- __OBJC_$_INSTANCE_VARIABLES_WDUserActivityManager
- __OBJC_$_INSTANCE_VARIABLES__WDActivityNode
- __OBJC_$_PROP_LIST_UNNotification_$_HealthKit
- __OBJC_$_PROP_LIST_WDContactConsolidationController
- __OBJC_$_PROP_LIST_WDContactConsolidationLearnMoreViewController
- __OBJC_$_PROP_LIST_WDEmptyUserActivityResponder
- __OBJC_$_PROP_LIST_WDFixedChartViewController
- __OBJC_$_PROP_LIST_WDNotificationManager
- __OBJC_$_PROP_LIST_WDUserActivityManager
- __OBJC_$_PROP_LIST__WDActivityNode
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UNUserNotificationCenterDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WDUserActivityResponder
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WDUserActivityResponder
- __OBJC_$_PROTOCOL_METHOD_TYPES_UNUserNotificationCenterDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WDUserActivityResponder
- __OBJC_$_PROTOCOL_REFS_UNUserNotificationCenterDelegate
- __OBJC_$_PROTOCOL_REFS_WDUserActivityResponder
- __OBJC_CLASS_PROTOCOLS_$_WDEmptyUserActivityResponder
- __OBJC_CLASS_PROTOCOLS_$_WDFixedChartViewController
- __OBJC_CLASS_PROTOCOLS_$_WDNotificationManager
- __OBJC_CLASS_RO_$_WDContactConsolidationController
- __OBJC_CLASS_RO_$_WDContactConsolidationLearnMoreViewController
- __OBJC_CLASS_RO_$_WDEmptyUserActivityResponder
- __OBJC_CLASS_RO_$_WDFixedChartViewController
- __OBJC_CLASS_RO_$_WDNotificationManager
- __OBJC_CLASS_RO_$_WDUserActivityManager
- __OBJC_CLASS_RO_$__WDActivityNode
- __OBJC_LABEL_PROTOCOL_$_UNUserNotificationCenterDelegate
- __OBJC_LABEL_PROTOCOL_$_WDUserActivityResponder
- __OBJC_METACLASS_RO_$_WDContactConsolidationController
- __OBJC_METACLASS_RO_$_WDContactConsolidationLearnMoreViewController
- __OBJC_METACLASS_RO_$_WDEmptyUserActivityResponder
- __OBJC_METACLASS_RO_$_WDFixedChartViewController
- __OBJC_METACLASS_RO_$_WDNotificationManager
- __OBJC_METACLASS_RO_$_WDUserActivityManager
- __OBJC_METACLASS_RO_$__WDActivityNode
- __OBJC_PROTOCOL_$_UNUserNotificationCenterDelegate
- __OBJC_PROTOCOL_$_WDUserActivityResponder
- __OBJC_PROTOCOL_REFERENCE_$_WDUserActivityResponder
- ___35+[WDNotificationManager initialize]_block_invoke
- ___39-[WDExportManager _writeMedicalRecords]_block_invoke.394
- ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.585
- ___50-[WDDataListViewController _deleteAllWithOptions:]_block_invoke.585.cold.1
- ___50-[WDExportManager createExportFileWithCompletion:]_block_invoke.364
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.318
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.318.cold.1
- ___52-[WDDeviceSourcesListTableViewSection reloadDevices]_block_invoke.320
- ___54-[WDSourceOrderController setOrderedSources:dataType:]_block_invoke.292
- ___55-[WDContactConsolidationController checkAlertNecessity]_block_invoke
- ___55-[WDContactConsolidationController checkAlertNecessity]_block_invoke.335
- ___55-[WDDeviceStoredDataViewController deleteAllStoredData]_block_invoke.289
- ___58+[WDEmptyUserActivityResponder emptyUserActivityResponder]_block_invoke
- ___60-[WDElectrocardiogramFilterDataProvider _countQueryForType:]_block_invoke.379
- ___60-[WDNotificationManager(Convenience) resetEmergencySOSBadge]_block_invoke
- ___61-[WDAppAccessListViewController _refreshAppAuthorizationData]_block_invoke.300
- ___62-[WDDocumentOverviewViewController _recomputeTotalReportCount]_block_invoke.311
- ___64-[WDContactConsolidationController _showLearnMoreViewController]_block_invoke
- ___64-[WDSampleListDataProvider _requestNextPageOfDataForSampleType:]_block_invoke.311
- ___65-[WDNotificationManager(Convenience) resetHealthRecordsDataBadge]_block_invoke
- ___65-[WDNotificationManager(Convenience) resetHealthRecordsDataBadge]_block_invoke.cold.1
- ___65-[WDStoredDataByCategoryViewController presentDeleteConfirmation]_block_invoke
- ___69-[WDContactConsolidationController presentContactsConsolidationAlert]_block_invoke
- ___69-[WDContactConsolidationController presentContactsConsolidationAlert]_block_invoke_2
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.297
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.297.cold.1
- ___70-[WDAtrialFibrillationInternalSettingsViewController _resetOnboarding]_block_invoke.299
- ___70-[WDContactConsolidationLearnMoreViewController dismissButtonPressed:]_block_invoke
- ___71-[WDStoredDataByCategoryViewController fetchEnabledStatusForPeripheral]_block_invoke.361
- ___76-[WDAtrialFibrillationEventOverviewViewController recomputeTotalSampleCount]_block_invoke.358
- ___77-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotifications]_block_invoke.303
- ___77-[WDElectrocardiogramDataMetadataViewController deletionSectionDidSelectRow:]_block_invoke
- ___79-[WDAtrialFibrillationEventOverviewViewController _getLatestAnalyzedSampleDate]_block_invoke.360
- ___81-[WDDisplayTypeDataSourcesTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.445
- ___90-[WDAtrialFibrillationInternalSettingsViewController _deleteAllNotificationsAndTachograms]_block_invoke.305
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.313
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.313.cold.1
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.313.cold.2
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.317
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.317.cold.1
- ___91-[WDBuddyFlowUserInfo saveChangesToHealthStore:andSaveNameCompletion:andOverallCompletion:]_block_invoke.319
- ___SOSLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e38_v24?0"_HKMedicalIDData"8"NSError"16ls32l8
- ___block_descriptor_40_e8_v12?0i8l
- ___block_literal_global.288
- ___block_literal_global.294
- ___block_literal_global.303
- ___block_literal_global.365
- ___block_literal_global.377
- ___block_literal_global.390
- ___block_literal_global.451
- ___block_literal_global.470
- ___block_literal_global.486
- ___block_literal_global.583
- ___getSOSContactsManagerClass_block_invoke
- ___getSOSContactsManagerClass_block_invoke.cold.1
- ___getSOSManagerClass_block_invoke
- ___getSOSManagerClass_block_invoke.cold.1
- ___getSOSUtilitiesClass_block_invoke
- ___getSOSUtilitiesClass_block_invoke.cold.1
- __sl_dlopen
- __suppressBadgeNotifications
- _abort_report_np
- _audit_stringSOS
- _emptyUserActivityResponder._emptyUserActivityResponder
- _emptyUserActivityResponder.onceToken
- _free
- _getSOSContactsManagerClass.softClass
- _getSOSManagerClass
- _getSOSManagerClass.softClass
- _getSOSUtilitiesClass
- _getSOSUtilitiesClass.softClass
- _initialize._notifyToken
- _kHKHealthAppBadgesDidUpdateNotification
- _kHKNotificationsDomainKey
- _kHKNotificationsURLKey
- _objc_getClass
- _objc_msgSend$SOSLegacyContacts
- _objc_msgSend$SOSLegacyContactsExist
- _objc_msgSend$_consolidateSOSContactsWithMedicalIDContacts
- _objc_msgSend$_isBTLEServer
- _objc_msgSend$_lock_policyForNotification:
- _objc_msgSend$_nextNode
- _objc_msgSend$_resetActivities
- _objc_msgSend$_restoreActivityFromPolicies:
- _objc_msgSend$_restoreFromActivityChain:
- _objc_msgSend$_sectionHeaderViewWithTitle:
- _objc_msgSend$_setCurrentNodeToResponder:
- _objc_msgSend$_setEligibleForPrediction:
- _objc_msgSend$_showLearnMoreViewController
- _objc_msgSend$_startFullOnboarding
- _objc_msgSend$_updateActivityForViewDidAppear
- _objc_msgSend$_userActivityWithTitle:keywords:activityType:
- _objc_msgSend$_userActivityWithType:
- _objc_msgSend$activityChainForActivity:
- _objc_msgSend$addActivitiesToArray:currentNode:
- _objc_msgSend$applyChangeActivity:
- _objc_msgSend$applyTransitionActivity:
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$authorizationStatusForEntityType:
- _objc_msgSend$becomeCurrent
- _objc_msgSend$cellForChart
- _objc_msgSend$changeActivityForResponder:activityDictionary:
- _objc_msgSend$changeActivityForResponder:activityDictionary:title:keywords:
- _objc_msgSend$checkAlertNecessity
- _objc_msgSend$completionHandler
- _objc_msgSend$consolidatedSOSContactsWithSOSContactsManager:
- _objc_msgSend$consolidationAlertController
- _objc_msgSend$content
- _objc_msgSend$contentInset
- _objc_msgSend$createDismissButton
- _objc_msgSend$createTextView
- _objc_msgSend$decidesActivity:
- _objc_msgSend$decodeIntegerForKey:
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$detailViewControllerForSourceModel:
- _objc_msgSend$detailViewControllerForSourceModel:withProfile:
- _objc_msgSend$deviceSupportsSOS
- _objc_msgSend$dictionaryWithCapacity:
- _objc_msgSend$dismissHandler
- _objc_msgSend$edgeInsetsForWidthDesignation:
- _objc_msgSend$emergencyContacts
- _objc_msgSend$emptyUserActivityResponder
- _objc_msgSend$encodeInteger:forKey:
- _objc_msgSend$encodeObject:forKey:
- _objc_msgSend$exceptionWithName:reason:userInfo:
- _objc_msgSend$initWithActivityType:
- _objc_msgSend$initWithKeyOptions:valueOptions:capacity:
- _objc_msgSend$initWithProfile:presentingViewController:
- _objc_msgSend$initWithProfile:style:
- _objc_msgSend$initWithResponder:
- _objc_msgSend$initWithReuseIdentifier:
- _objc_msgSend$isAllowedToMessageSOSContacts
- _objc_msgSend$legacyContactsManager
- _objc_msgSend$medicalIDData
- _objc_msgSend$nextResponder
- _objc_msgSend$notification
- _objc_msgSend$notificationManager
- _objc_msgSend$policies
- _objc_msgSend$postNotificationName:object:
- _objc_msgSend$presentContactsConsolidationAlert
- _objc_msgSend$presentDeleteConfirmation
- _objc_msgSend$raise
- _objc_msgSend$removeObserver:
- _objc_msgSend$request
- _objc_msgSend$resetEmergencySOSBadge
- _objc_msgSend$responder
- _objc_msgSend$setAllowedToMessageSOSContacts:
- _objc_msgSend$setBadge:forDomain:completion:
- _objc_msgSend$setClinicalAuthorizationController:
- _objc_msgSend$setClinicalAuthorizationSettingsViewController:
- _objc_msgSend$setCompletionHandler:
- _objc_msgSend$setConsolidationAlertController:
- _objc_msgSend$setContentOffset:
- _objc_msgSend$setDismissHandler:
- _objc_msgSend$setEligibleForHandoff:
- _objc_msgSend$setEligibleForPublicIndexing:
- _objc_msgSend$setEligibleForSearch:
- _objc_msgSend$setEmergencyContacts:
- _objc_msgSend$setHealthDataAuthorizationController:
- _objc_msgSend$setHealthDataAuthorizationSettingsViewController:
- _objc_msgSend$setHealthStore:
- _objc_msgSend$setHostedView:
- _objc_msgSend$setKeywords:
- _objc_msgSend$setNextResponder:
- _objc_msgSend$setNotificationManager:
- _objc_msgSend$setPresentingViewController:
- _objc_msgSend$setRecordActivities:
- _objc_msgSend$setRequiredUserInfoKeys:
- _objc_msgSend$setResearchStudyUsageDescription:
- _objc_msgSend$setResponder:
- _objc_msgSend$setUninstalledSourcesExist:
- _objc_msgSend$setUpdateDescription:
- _objc_msgSend$setUserInfo:
- _objc_msgSend$sosContactsManager
- _objc_msgSend$suppressBadgeNotifications
- _objc_msgSend$transitionActivityForResponder:newResponder:transitionDictionary:
- _objc_msgSend$uninstalledSourcesExist
- _objc_msgSend$uniqueUserActivityType
- _objc_msgSend$userActivityManager
- _objc_msgSend$userInfo
- _objc_msgSend$userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:
- _objc_msgSend$userNotificationCenter:openSettingsForNotification:
- _objc_msgSend$userNotificationCenter:willPresentNotification:withCompletionHandler:
- _objc_msgSend$wd_userInfo
- _objc_msgSend$whiteColor
- _objc_msgSend$zeroBadge
CStrings:
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@64@0:8@16q24@32@40@48@56"
+ "ATRIAL_FIBRILLATION_DETECTION_PINNED_BROWSE_FOOTER"
+ "ATRIAL_FIBRILLATION_DETECTION_PINNED_SUMMARY_FOOTER"
+ "AboutSection"
+ "B24@0:8@\"UIGestureRecognizer\"16"
+ "B32@0:8@\"UIGestureRecognizer\"16@\"UIEvent\"24"
+ "B32@0:8@\"UIGestureRecognizer\"16@\"UIGestureRecognizer\"24"
+ "B32@0:8@\"UIGestureRecognizer\"16@\"UIPress\"24"
+ "B32@0:8@\"UIGestureRecognizer\"16@\"UITouch\"24"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "ECGResultsSection"
+ "EducationSection"
+ "GetMoreFromHealthSection"
+ "NotificationsSection"
+ "OptionsSection"
+ "PINNED_SECTION_BROWSE_FOOTER"
+ "PINNED_SECTION_SUMMARY_FOOTER"
+ "RecentResults"
+ "Shared factories reached more than 10, removing all cached factories"
+ "TQ,N,V_sourcesStyle"
+ "UIGestureRecognizerDelegate"
+ "_clinicalAuthorizationFamilyControllerWithAuthorizationController:healthRecordsStore:source:readUsageDescription:"
+ "_getSourceListToShow"
+ "_healthDataAuthorizationFamilyControllerWithHealthStore:source:healthAuthorizationViewController:"
+ "_healthDataAuthorizationViewControllerWithSourceModel:source:profile:"
+ "_isHiddenSource"
+ "_medicationAuthorizationFamilyControllerWithSourceModel:healthStore:source:"
+ "_sectionHeaderViewWithTitle:identifier:"
+ "_shouldShowUninstalledSourcesCell"
+ "_sourcesStyle"
+ "_startFullOnboardingFromSourceItem:"
+ "_startUpgradeFromSourceItem:"
+ "_uuidStringForDevice:"
+ "bluetoothIdentifier"
+ "createDetailViewControllerForSourceModel:completion:"
+ "createDetailViewControllerForSourceModel:healthStore:completion:"
+ "createDetailViewControllerForSourceModel:profile:completion:"
+ "deletionSectionDidSelectRow:sourceItem:"
+ "gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:"
+ "gestureRecognizer:shouldReceiveEvent:"
+ "gestureRecognizer:shouldReceivePress:"
+ "gestureRecognizer:shouldReceiveTouch:"
+ "gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:"
+ "gestureRecognizer:shouldRequireFailureOfGestureRecognizer:"
+ "gestureRecognizerShouldBegin:"
+ "healthSettingsSourcesSpecifier"
+ "hk_addNonNilObject:"
+ "hk_safeAreaAdjustedEdgeInsets:"
+ "initWithController:source:healthStore:"
+ "initWithHealthStore:style:source:typesToShare:typesToRead:shareDescription:updateDescription:researchStudyUsageDescription:"
+ "initWithProfile:style:source:shareDescription:updateDescription:researchStudyUsageDescription:"
+ "internalHealthSettingsURLTo:"
+ "internalPrivacySettingsURLString"
+ "isPinnedInBrowse"
+ "isiPad"
+ "presentDeleteConfirmationFromSender:"
+ "reload"
+ "reloadWithCompletion:"
+ "removeObserver:name:object:"
+ "setController:"
+ "setFamilyControllers:"
+ "setSourcesStyle:"
+ "setUseSolariumDesign:"
+ "setViewController:"
+ "sourcesStyle"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "v16@?0@\"UIViewController\"8"
+ "v32@0:8@\"HKDataMetadataDeletionSection\"16@\"<UIPopoverPresentationControllerSourceItem>\"24"
+ "viewController"
- "%s"
- "2"
- "@\"<WDUserActivityResponder>\""
- "@\"<WDUserActivityResponder>\"24@0:8@\"NSDictionary\"16"
- "@\"HKDataMetadataDetailSection\""
- "@\"HKInteractiveChartViewController\""
- "@\"HKNotificationStore\""
- "@\"HKValueRange\""
- "@\"NSMapTable\""
- "@\"SOSContactsManager\""
- "@\"UIAlertController\""
- "@\"WDNotificationManager\""
- "@\"WDUserActivityManager\""
- "@\"_WDActivityNode\""
- "@?16@0:8"
- "ATRIAL_FIBRILLATION_DETECTION_PINNED_FOOTER"
- "Convenience"
- "DATA_COLLECTION_MORE_INFO_BUTTON"
- "DATA_COLLECTION_MORE_INFO_DONE_BUTTON"
- "Failed to register for BadgesDidUpdate notification"
- "Failed to reset Emergency SOS badge with error: %@"
- "Failed to reset Health Records badge with error: %@"
- "FixedChartReuseIdentifier"
- "HealthKit"
- "MEDICAL_ID_CONSOLIDATION_ALERT_BODY"
- "MEDICAL_ID_CONSOLIDATION_ALERT_BODY_WATCH_ONLY"
- "MEDICAL_ID_CONSOLIDATION_ALERT_TITLE"
- "MEDICAL_ID_CONSOLIDATION_LEARN_MORE_BODY"
- "MEDICAL_ID_CONSOLIDATION_LEARN_MORE_TITLE"
- "Notification manager should only be bounded to the primary health store"
- "PINNED_SECTION_FOOTER"
- "Responder: %@ Next Responder: %@ \n"
- "Restoration transition problem: %{public}@"
- "SHOW_ALL_DATA_UA_FORMAT"
- "SOSContactsManager"
- "SOSLegacyContacts"
- "SOSLegacyContactsExist"
- "SOSManager"
- "SOSUtilities"
- "T@\"<WDUserActivityResponder>\",W,N,V_nextResponder"
- "T@\"<WDUserActivityResponder>\",W,N,V_responder"
- "T@\"HKDataMetadataDetailSection\",R,N,V_metadataSection"
- "T@\"HKHealthStore\",&,N,V_healthStore"
- "T@\"HKInteractiveChartViewController\",R,N,V_chartController"
- "T@\"HKValueRange\",R,N,V_fixedRange"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSMutableArray\",R,N,V_policies"
- "T@\"NSURL\",R,C,N"
- "T@\"SOSContactsManager\",&,N,V_sosContactsManager"
- "T@\"UIAlertController\",W,N,V_consolidationAlertController"
- "T@\"UITextView\",&,N,V_textView"
- "T@\"UIViewController\",W,N,V_presentingViewController"
- "T@\"WDNotificationManager\",&,N,V_notificationManager"
- "T@\"WDNotificationManager\",R,N,V_notificationManager"
- "T@\"WDUserActivityManager\",R,N,V_userActivityManager"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_dismissHandler"
- "TB,N,V_recordActivities"
- "TB,N,V_uninstalledSourcesExist"
- "The root view controller must implement the WDUserActivityResponder protocol"
- "Transition failed for breadcrumb: %@ in chain %@"
- "UNUserNotificationCenterDelegate"
- "Unable to find class %s"
- "User Activity Manager version mismatch: %ld != %ld"
- "WDContactConsolidationController"
- "WDContactConsolidationLearnMoreViewController"
- "WDContactConsolidationLearnMoreViewController - ![getSOSManagerClass() deviceSupportsSOS] && ![_HKBehavior hasPairedWatch]"
- "WDContactConsolidationLearnMoreViewController - Checking alert necessity"
- "WDContactConsolidationLearnMoreViewController - current process is not authorized to access contacts, skip contact consolidation"
- "WDContactConsolidationLearnMoreViewController - fetched medical id"
- "WDContactConsolidationLearnMoreViewController - isAllowedToMessageSOSContacts - true"
- "WDContactConsolidationLearnMoreViewController - presentContactConsolidationAlertWithCompletionHandler"
- "WDContactConsolidationLearnMoreViewController - presentContactsConsolidationAlert"
- "WDContactConsolidationLearnMoreViewController - presentingViewController presentViewController:self.consolidationAlertController"
- "WDContactConsolidationLearnMoreViewController - self.medicalIDData.emergencyContacts.count == 0 && self.sosContactsManager.legacyContactsManager.SOSLegacyContacts.count == 0"
- "WDEmptyUserActivityResponder"
- "WDFixedChartViewController"
- "WDNotificationManager"
- "WDNotificationManagerBadgesDidUpdateNotificationName"
- "WDUserActivityManager"
- "WDUserActivityResponder"
- "WDUserActivityRestorationIdentifier"
- "_ActivityBreadcrumbKey"
- "_RootControllerNotResponderName"
- "_UserActivityBreadcrumbArrayKey"
- "_UserActivityVersionKey"
- "_WDActivityNode"
- "_chartController"
- "_completionHandler"
- "_consolidateSOSContactsWithMedicalIDContacts"
- "_consolidationAlertController"
- "_currentNode"
- "_dismissHandler"
- "_domainsToPolicies"
- "_fixedRange"
- "_indexedActivities"
- "_isBTLEServer"
- "_lock_policyForNotification:"
- "_metadataSection"
- "_nextNode"
- "_nextResponder"
- "_nextResponderActivity"
- "_notificationManager"
- "_notificationStore"
- "_policies"
- "_presentingViewController"
- "_recordActivities"
- "_resetActivities"
- "_responder"
- "_responderActivity"
- "_responderTable"
- "_restoreActivityFromPolicies:"
- "_restoreFromActivityChain:"
- "_rootViewController"
- "_sectionHeaderViewWithTitle:"
- "_setCurrentNodeToResponder:"
- "_setEligibleForPrediction:"
- "_showLearnMoreViewController"
- "_sosContactsManager"
- "_startFullOnboarding"
- "_textView"
- "_topNode"
- "_uninstalledSourcesExist"
- "_updateActivityForViewDidAppear"
- "_userActivityManager"
- "_userActivityWithTitle:keywords:activityType:"
- "_userActivityWithType:"
- "activityChainForActivity:"
- "addActivitiesToArray:currentNode:"
- "addPolicy:"
- "applyChangeActivity:"
- "applyTransitionActivity:"
- "arrayWithCapacity:"
- "authorizationStatusForEntityType:"
- "becomeCurrent"
- "cellForChart"
- "changeActivityForResponder:activityDictionary:"
- "changeActivityForResponder:activityDictionary:title:keywords:"
- "chartController"
- "checkAlertNecessity"
- "com.apple.Health.tab"
- "completionHandler"
- "consolidatedSOSContactsWithSOSContactsManager:"
- "consolidationAlertController"
- "content"
- "contentInset"
- "createContactConsolidationControllerInViewController:"
- "createDismissButton"
- "createTextView"
- "decidesActivity:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "deletionSectionDidSelectRow:"
- "detailViewControllerForSourceModel:"
- "detailViewControllerForSourceModel:withHealthStore:"
- "detailViewControllerForSourceModel:withProfile:"
- "deviceSupportsSOS"
- "dictionaryWithCapacity:"
- "dismissButtonPressed:"
- "dismissHandler"
- "edgeInsetsForWidthDesignation:"
- "emergencyContacts"
- "emptyUserActivityResponder"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "exceptionWithName:reason:userInfo:"
- "fixedRange"
- "initWithActivityType:"
- "initWithHealthStore:style:"
- "initWithInteractiveChartViewController:sessionSample:profile:title:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithProfile:presentingViewController:"
- "initWithProfile:style:"
- "initWithResponder:"
- "initialize"
- "isAllowedToMessageSOSContacts"
- "isPresentingConsolidationAlert"
- "legacyContactsManager"
- "metadataSection"
- "nextResponder"
- "notification"
- "notificationManager"
- "policies"
- "postNotificationName:object:"
- "prefs://root=HEALTH&path=SOURCES"
- "prefs:root=Privacy"
- "presentContactConsolidationAlertWithCompletionHandler:"
- "presentContactsConsolidationAlert"
- "presentDeleteConfirmation"
- "raise"
- "recordActivities"
- "request"
- "resetEmergencySOSBadge"
- "resetHealthRecordsDataBadge"
- "responder"
- "restoreFromUserActivity:"
- "setAllowedToMessageSOSContacts:"
- "setBadge:forDomain:completion:"
- "setClinicalAuthorizationController:"
- "setClinicalAuthorizationSettingsViewController:"
- "setCompletionHandler:"
- "setConsolidationAlertController:"
- "setContentOffset:"
- "setDismissHandler:"
- "setEligibleForHandoff:"
- "setEligibleForPublicIndexing:"
- "setEligibleForSearch:"
- "setEmergencyContacts:"
- "setHealthDataAuthorizationController:"
- "setHealthDataAuthorizationSettingsViewController:"
- "setHealthStore:"
- "setHostedView:"
- "setKeywords:"
- "setNextResponder:"
- "setNotificationManager:"
- "setPolicy:forDomain:"
- "setPresentingViewController:"
- "setRecordActivities:"
- "setRequiredUserInfoKeys:"
- "setResearchStudyUsageDescription:"
- "setResponder:"
- "setRootViewController:"
- "setSosContactsManager:"
- "setSuppressBadgeNotifications:"
- "setTextView:"
- "setUninstalledSourcesExist:"
- "setUpdateDescription:"
- "softlink:r:path:/System/Library/PrivateFrameworks/SOS.framework/SOS"
- "sosContactsManager"
- "suppressBadgeNotifications"
- "textView"
- "transitionActivityForResponder:newResponder:transitionDictionary:"
- "uninstalledSourcesExist"
- "uniqueUserActivityType"
- "userActivityManager"
- "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
- "userNotificationCenter:openSettingsForNotification:"
- "userNotificationCenter:willPresentNotification:withCompletionHandler:"
- "v24@0:8@\"HKDataMetadataDeletionSection\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
- "v40@0:8@16q24@?32"
- "wd_domain"
- "wd_url"
- "wd_userInfo"
- "whiteColor"
- "zeroBadge"

```
