## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore`

```diff

-  __TEXT.__text: 0xd3818
-  __TEXT.__objc_methlist: 0x8a08
+  __TEXT.__text: 0xd3d34
+  __TEXT.__objc_methlist: 0x8a58
   __TEXT.__const: 0x650
-  __TEXT.__cstring: 0x3c437
-  __TEXT.__oslogstring: 0x70b0
+  __TEXT.__cstring: 0x3cde2
+  __TEXT.__oslogstring: 0x715e
   __TEXT.__gcc_except_tab: 0x2084
-  __TEXT.__unwind_info: 0x2a20
+  __TEXT.__unwind_info: 0x2a28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdf8
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5150
+  __DATA_CONST.__objc_selrefs: 0x5180
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x3f620
+  __DATA_CONST.__objc_arraydata: 0x3fc60
   __DATA_CONST.__got: 0x618
-  __AUTH_CONST.__const: 0x36a0
-  __AUTH_CONST.__cfstring: 0x62580
-  __AUTH_CONST.__objc_const: 0x9c68
-  __AUTH_CONST.__objc_intobj: 0x49b0
+  __AUTH_CONST.__const: 0x36e0
+  __AUTH_CONST.__cfstring: 0x63140
+  __AUTH_CONST.__objc_const: 0x9cc8
+  __AUTH_CONST.__objc_intobj: 0x49c8
   __AUTH_CONST.__objc_doubleobj: 0x13a0
   __AUTH_CONST.__objc_arrayobj: 0xf30
-  __AUTH_CONST.__objc_dictobj: 0xed80
+  __AUTH_CONST.__objc_dictobj: 0xedf8
   __AUTH_CONST.__auth_got: 0xb08
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x700
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x708
   __DATA.__data: 0x440
-  __DATA.__bss: 0x1611
+  __DATA.__bss: 0x15d1
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1bd0
+  __DATA_DIRTY.__objc_data: 0x1c70
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0xf48
+  __DATA_DIRTY.__bss: 0xf88
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4484
-  Symbols:   10482
-  CStrings:  26304
+  Functions: 4492
+  Symbols:   10497
+  CStrings:  26497
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[PLArchiveManager fireArchiveListener]
+ -[PLArchiveManager setFireArchiveListener:]
+ -[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:]
+ -[PowerlogCore fireSBCListener]
+ -[PowerlogCore fireSignificantBatteryChangeNotification]
+ -[PowerlogCore setFireSBCListener:]
+ OBJC_IVAR_$_PLArchiveManager._fireArchiveListener
+ OBJC_IVAR_$_PowerlogCore._fireSBCListener
+ __20-[PowerlogCore init]_block_invoke
+ ___116-[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:]_block_invoke
+ ___24-[PLArchiveManager init]_block_invoke_2
+ ___block_descriptor_32_e38_v32?0"NSDictionary"8"NSString"1624l
+ _objc_msgSend$fireSignificantBatteryChangeNotification
+ _objc_msgSend$initWithOperator:forDynamicServiceClass:forNotificationType:forAFKRole:withMatchBlock:
- GCC_except_table49
- ___105-[PLIOKitOperatorComposition initWithOperator:forDynamicServiceClass:forNotificationType:withMatchBlock:]_block_invoke
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Operators/Agents/PLEnhancedTaskingAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Operators/Compositions/PLEntryNotificationOperatorComposition.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Operators/Compositions/PLIOHIDOperatorComposition.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Operators/Compositions/PLIOKitOperatorComposition.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Operators/Compositions/PLTimer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/PowerlogCore/PLCoreOperator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/PowerlogCore/PLOperator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/PowerlogCore/PLXPCRelay.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/PowerlogCore/PowerlogCore.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLArchiveJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLArchiveManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLCoreStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLDefaults.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLEntry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLStorageCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLSubmissions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionConfig.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFile.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFilePLL.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFileSP.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLTimeManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLTimeReference.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceDynamic.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceSystem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterion.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionEntry.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionTime.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/DataTypes/PLEntryKey.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/DataTypes/PLSQLStatement.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLEntryDefinition.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLKQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLMonotonicTimer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLNetworkUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLSQLiteConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLSemaphore.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GrCe6Z/Sources/PerfPowerServices/Utilities/PLUtilities.m"
+ "1006035"
+ "ANE1"
+ "BatteryShippingChargeLimit"
+ "CPU_Energy"
+ "CSIDualAntennaDuration"
+ "CSIEnabledDuration"
+ "CSIMacActiveDuration"
+ "Dormancy"
+ "ECPU_CORE0_NRG"
+ "ECPU_CORE0_SRM_NRG"
+ "ECPU_CORE1_NRG"
+ "ECPU_CORE1_SRM_NRG"
+ "ECPU_CORE2_NRG"
+ "ECPU_CORE2_SRM_NRG"
+ "ECPU_CORE3_NRG"
+ "ECPU_CORE3_SRM_NRG"
+ "ECPU_CPM_NRG"
+ "ECPU_CPM_SRM_NRG"
+ "ECPU_NRG"
+ "Features"
+ "FirstPartyApps"
+ "Manually firing SBC"
+ "Manually firing archive activity"
+ "PCPU0_CORE0_NRG"
+ "PCPU0_CORE0_SRM_NRG"
+ "PCPU0_CORE1_NRG"
+ "PCPU0_CORE1_SRM_NRG"
+ "PCPU0_CPM_NRG"
+ "PCPU0_CPM_SRM_NRG"
+ "PCPU_NRG"
+ "PLBatteryAgent_EventBackward_Battery.filtered.Level_0_1.Level_7_1800.Level_8_300"
+ "ShipChargeLimitCompliant"
+ "ShipChargeLimitEnabled"
+ "ShipChargeLimitSupported"
+ "ShippingChargeLimitSystemStatus"
+ "Skipping manual archive: archive manager is not enabled"
+ "Skipping manual archive: storage is locked"
+ "SystemCapability100ms_Battery0"
+ "SystemCapability100ms_Battery0_0"
+ "SystemCapability100ms_Battery0_1"
+ "SystemCapability100ms_Battery0_2"
+ "SystemCapability100ms_Battery0_3"
+ "SystemCapability100ms_Battery0_4"
+ "SystemCapability100ms_Battery0_5"
+ "SystemCapability100ms_Battery0_6"
+ "SystemCapability100ms_Battery0_7"
+ "SystemCapability100ms_Battery1"
+ "SystemCapability100ms_Battery1_0"
+ "SystemCapability100ms_Battery1_1"
+ "SystemCapability100ms_Battery1_2"
+ "SystemCapability100ms_Battery1_3"
+ "SystemCapability100ms_Battery1_4"
+ "SystemCapability100ms_Battery1_5"
+ "SystemCapability100ms_Battery1_6"
+ "SystemCapability100ms_Battery1_7"
+ "SystemCapability1sec_Battery0"
+ "SystemCapability1sec_Battery0_0"
+ "SystemCapability1sec_Battery0_1"
+ "SystemCapability1sec_Battery0_2"
+ "SystemCapability1sec_Battery0_3"
+ "SystemCapability1sec_Battery0_4"
+ "SystemCapability1sec_Battery0_5"
+ "SystemCapability1sec_Battery0_6"
+ "SystemCapability1sec_Battery0_7"
+ "SystemCapability1sec_Battery1"
+ "SystemCapability1sec_Battery1_0"
+ "SystemCapability1sec_Battery1_1"
+ "SystemCapability1sec_Battery1_2"
+ "SystemCapability1sec_Battery1_3"
+ "SystemCapability1sec_Battery1_4"
+ "SystemCapability1sec_Battery1_5"
+ "SystemCapability1sec_Battery1_6"
+ "SystemCapability1sec_Battery1_7"
+ "SystemCapabilityInsta_Battery0"
+ "SystemCapabilityInsta_Battery0_0"
+ "SystemCapabilityInsta_Battery0_1"
+ "SystemCapabilityInsta_Battery0_2"
+ "SystemCapabilityInsta_Battery0_3"
+ "SystemCapabilityInsta_Battery0_4"
+ "SystemCapabilityInsta_Battery0_5"
+ "SystemCapabilityInsta_Battery0_6"
+ "SystemCapabilityInsta_Battery0_7"
+ "SystemCapabilityInsta_Battery1"
+ "SystemCapabilityInsta_Battery1_0"
+ "SystemCapabilityInsta_Battery1_1"
+ "SystemCapabilityInsta_Battery1_2"
+ "SystemCapabilityInsta_Battery1_3"
+ "SystemCapabilityInsta_Battery1_4"
+ "SystemCapabilityInsta_Battery1_5"
+ "SystemCapabilityInsta_Battery1_6"
+ "SystemCapabilityInsta_Battery1_7"
+ "UISoc"
+ "candidate"
+ "com.apple.powerlogd.archive"
+ "com.apple.powerlogd.fireSBC"
+ "effectiveIdleSeconds"
+ "eventTimestamp"
+ "excluded"
+ "inactive"
+ "\xa3"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Operators/Agents/PLEnhancedTaskingAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Operators/Compositions/PLEntryNotificationOperatorComposition.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Operators/Compositions/PLIOHIDOperatorComposition.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Operators/Compositions/PLIOKitOperatorComposition.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Operators/Compositions/PLTimer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/PowerlogCore/PLCoreOperator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/PowerlogCore/PLOperator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/PowerlogCore/PLXPCRelay.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/PowerlogCore/PowerlogCore.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLArchiveJob.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLArchiveManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLCoreStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLDefaults.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLEntry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLStorageCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLSubmissions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionConfig.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFile.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFilePLL.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFileSP.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLTimeManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLTimeReference.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceDynamic.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceSystem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterion.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionEntry.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionTime.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/DataTypes/PLEntryKey.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/DataTypes/PLSQLStatement.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLEntryDefinition.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLKQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLMonotonicTimer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLNetworkUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLSQLiteConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLSemaphore.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kJaVms/Sources/PerfPowerServices/Utilities/PLUtilities.m"
- "\xa2"

```
