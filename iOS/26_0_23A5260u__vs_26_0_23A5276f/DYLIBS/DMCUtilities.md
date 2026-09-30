## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x33848
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x2cac
-  __TEXT.__const: 0x150
+46.0.0.0.0
+  __TEXT.__text: 0x347b4
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_methlist: 0x2d9c
+  __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x77c
-  __TEXT.__cstring: 0x3640
-  __TEXT.__oslogstring: 0x4f44
+  __TEXT.__cstring: 0x3718
+  __TEXT.__oslogstring: 0x51ca
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xdc0
-  __TEXT.__objc_classname: 0x48b
-  __TEXT.__objc_methname: 0x974b
-  __TEXT.__objc_methtype: 0x131b
-  __TEXT.__objc_stubs: 0x5fa0
-  __DATA_CONST.__got: 0x678
+  __TEXT.__unwind_info: 0xde8
+  __TEXT.__objc_classname: 0x4b7
+  __TEXT.__objc_methname: 0x99cf
+  __TEXT.__objc_methtype: 0x1335
+  __TEXT.__objc_stubs: 0x6220
+  __DATA_CONST.__got: 0x690
   __DATA_CONST.__const: 0x1168
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2478
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x780
+  __DATA_CONST.__objc_selrefs: 0x2540
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0xd20
-  __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0x4150
+  __AUTH_CONST.__cfstring: 0x4080
+  __AUTH_CONST.__objc_const: 0x4350
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x1f8
-  __DATA.__data: 0x2b1
+  __AUTH.__objc_data: 0xf00
+  __DATA.__objc_ivar: 0x208
+  __DATA.__data: 0x300
   __DATA.__bss: 0x968
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xa8

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
+  - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2FE97219-3E78-3E4B-B947-86DA1B62B13F
-  Functions: 1360
-  Symbols:   4973
-  CStrings:  3182
+  UUID: FB3CFC34-32F7-3619-8AD0-E53EC063C001
+  Functions: 1381
+  Symbols:   5062
+  CStrings:  3248
 
Symbols:
+ +[DMCFeatureFlags isMigrationEligibilityReportEnabled]
+ +[DMCFeatureOverrides simulatedMDMAccountDrivenEnrollmentAuthenticationResults]
+ -[DMCCTEnrollmentProperties .cxx_destruct]
+ -[DMCCTEnrollmentProperties imei]
+ -[DMCCTEnrollmentProperties init]
+ -[DMCCTEnrollmentProperties meid]
+ -[DMCCTEnrollmentProperties setImei:]
+ -[DMCCTEnrollmentProperties setMeid:]
+ -[DMCHangDetectionQueue _qosClassFromNSQualityOfService:]
+ -[DMCHangDetectionQueue queueBlock:afterDelay:]
+ -[DMCLoggingSupport .cxx_destruct]
+ -[DMCLoggingSupport dealloc]
+ -[DMCLoggingSupport enableDebugLoggingForProcesses:]
+ -[DMCLoggingSupport enableDebugLoggingForSubsystems:]
+ -[DMCLoggingSupport processes]
+ -[DMCLoggingSupport resetAll]
+ -[DMCLoggingSupport setProcesses:]
+ -[DMCLoggingSupport setSubsystems:]
+ -[DMCLoggingSupport subsystems]
+ GCC_except_table13
+ _DMCCTTelephonyPropertiesForEnrollmentAuthentication
+ _DMCMigrationEligibilityDescriptionABE
+ _DMCMigrationEligibilityDescriptionEligible
+ _DMCMigrationEligibilityDescriptionRRTS
+ _DMCMigrationEligibilityDescriptionSharedIPad
+ _DMCMigrationEligibilityDescriptionUnenrolled
+ _DMCMigrationEligibilityDescriptionUnsupervised
+ _DMCMigrationEligibilityDescriptionUnsupportedEnrollment
+ _DMCMigrationHasIncompleteMigrationKey
+ _DMCMigrationUserInitiatedMigrationKey
+ _OBJC_CLASS_$_DMCCTEnrollmentProperties
+ _OBJC_CLASS_$_DMCLoggingSupport
+ _OBJC_CLASS_$_OSLogPreferencesProcess
+ _OBJC_CLASS_$_OSLogPreferencesSubsystem
+ _OBJC_IVAR_$_DMCCTEnrollmentProperties._imei
+ _OBJC_IVAR_$_DMCCTEnrollmentProperties._meid
+ _OBJC_IVAR_$_DMCLoggingSupport._processes
+ _OBJC_IVAR_$_DMCLoggingSupport._subsystems
+ _OBJC_METACLASS_$_DMCCTEnrollmentProperties
+ _OBJC_METACLASS_$_DMCLoggingSupport
+ __IMEIString
+ __OBJC_$_INSTANCE_METHODS_DMCCTEnrollmentProperties
+ __OBJC_$_INSTANCE_METHODS_DMCLoggingSupport
+ __OBJC_$_INSTANCE_VARIABLES_DMCCTEnrollmentProperties
+ __OBJC_$_INSTANCE_VARIABLES_DMCLoggingSupport
+ __OBJC_$_PROP_LIST_DMCCTEnrollmentProperties
+ __OBJC_$_PROP_LIST_DMCLoggingSupport
+ __OBJC_CLASS_RO_$_DMCCTEnrollmentProperties
+ __OBJC_CLASS_RO_$_DMCLoggingSupport
+ __OBJC_METACLASS_RO_$_DMCCTEnrollmentProperties
+ __OBJC_METACLASS_RO_$_DMCLoggingSupport
+ ___47-[DMCHangDetectionQueue queueBlock:afterDelay:]_block_invoke
+ _objc_msgSend$_qosClassFromNSQualityOfService:
+ _objc_msgSend$effectiveEnabledLevel
+ _objc_msgSend$effectivePersistedLevel
+ _objc_msgSend$enabledLevel
+ _objc_msgSend$getMobileEquipmentInfo:
+ _objc_msgSend$initWithBundleID:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$meInfoList
+ _objc_msgSend$persistedLevel
+ _objc_msgSend$processes
+ _objc_msgSend$qualityOfService
+ _objc_msgSend$resetAll
+ _objc_msgSend$setImei:
+ _objc_msgSend$setMeid:
+ _objc_msgSend$setPersistedLevel:
+ _objc_msgSend$setProcesses:
+ _objc_msgSend$setSubsystems:
+ _objc_msgSend$simulatedMDMAccountDrivenEnrollmentAuthenticationResults
+ _objc_msgSend$slotID
+ _objc_msgSend$slotId
+ _objc_msgSend$subsystems
- +[DMCFeatureFlags isDEPPushEnabled]
- GCC_except_table7
- _objc_msgSend$getMobileEquipmentInfoFor:error:
- _objc_release_x2
CStrings:
+ "DMCCTEnrollmentProperties"
+ "DMCLoggingSupport"
+ "DMCNetworkMonitor: Waiting for network..."
+ "ELIGIBLE"
+ "Enabled debug log for process %@"
+ "Enabled debug log for subsystem %@"
+ "HasIncompleteMigration"
+ "I24@0:8q16"
+ "INELIGIBLE_ABE"
+ "INELIGIBLE_RRTS"
+ "INELIGIBLE_SHARED_IPAD"
+ "INELIGIBLE_UNENROLLED"
+ "INELIGIBLE_UNSUPERVISED"
+ "INELIGIBLE_UNSUPPORTED_ENROLLMENT"
+ "Log level for process %@ has been configured (effectiveEnabledLevel: %ld, enabledLevel: %ld, effectivePersistedLevel: %ld, persistedLevel: %ld, "
+ "Log level for process %@ is debug already"
+ "Log level for subsystem %@ has been configured (effectiveEnabledLevel: %ld, enabledLevel: %ld, effectivePersistedLevel: %ld, persistedLevel: %ld, "
+ "Log level for subsystem %@ is debug already"
+ "MigrationEligibilityReport"
+ "MigrationEligibilityReportEnabled"
+ "T@\"NSMutableDictionary\",&,N,V_processes"
+ "T@\"NSMutableDictionary\",&,N,V_subsystems"
+ "T@\"NSString\",C,N,V_imei"
+ "T@\"NSString\",C,N,V_meid"
+ "TB,R,N,GisMigrationEligibilityReportEnabled"
+ "UserInitiatedMigration"
+ "_EquipmentInfo: could not find acceptable equipment info"
+ "_EquipmentInfo: getMobileEquipmentInfo: failed: %{public}@"
+ "_EquipmentInfo: getMobileEquipmentInfo: returned no items"
+ "_EquipmentInfo: result = %{public}@"
+ "_imei"
+ "_meid"
+ "_processes"
+ "_qosClassFromNSQualityOfService:"
+ "_subsystems"
+ "effectiveEnabledLevel"
+ "effectivePersistedLevel"
+ "enableDebugLoggingForProcesses:"
+ "enableDebugLoggingForSubsystems:"
+ "enabledLevel"
+ "getMobileEquipmentInfo:"
+ "imei"
+ "initWithBundleID:"
+ "initWithName:"
+ "isMigrationEligibilityReportEnabled"
+ "meInfoList"
+ "meid"
+ "persistedLevel"
+ "processes"
+ "qualityOfService"
+ "queueBlock:afterDelay:"
+ "resetAll"
+ "setImei:"
+ "setMeid:"
+ "setPersistedLevel:"
+ "setProcesses:"
+ "setSubsystems:"
+ "simulatedMDMAccountDrivenEnrollmentAuthenticationResults"
+ "slotID"
+ "slotId"
+ "subsystems"
+ "v32@0:8@?16d24"
- "DEPPushEnabled"
- "TB,R,N,GisDEPPushEnabled"
- "getMobileEquipmentInfoFor:error:"
- "getMobileEquipmentInfoFor:error: failed: %{public}@"
- "isDEPPushEnabled"

```
