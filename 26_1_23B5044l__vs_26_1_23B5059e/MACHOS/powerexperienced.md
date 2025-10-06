## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-118.40.8.0.0
-  __TEXT.__text: 0x17f10
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x32e0
-  __TEXT.__objc_methlist: 0x1f5c
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x106c
-  __TEXT.__objc_methname: 0x3973
-  __TEXT.__oslogstring: 0x25f0
+118.40.12.0.0
+  __TEXT.__text: 0x18788
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x3400
+  __TEXT.__objc_methlist: 0x1fe4
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x10da
+  __TEXT.__objc_methname: 0x3b7e
+  __TEXT.__oslogstring: 0x27f7
   __TEXT.__objc_classname: 0x3df
-  __TEXT.__objc_methtype: 0x7ee
+  __TEXT.__objc_methtype: 0x80e
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x620
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x170
+  __TEXT.__unwind_info: 0x638
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x850
-  __DATA_CONST.__cfstring: 0x10e0
+  __DATA_CONST.__cfstring: 0x1100
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x4a28
-  __DATA.__objc_selrefs: 0xf90
-  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_const: 0x4ae8
+  __DATA.__objc_selrefs: 0xfe8
+  __DATA.__objc_ivar: 0x224
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x600
   __DATA.__bss: 0x210

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A04460D3-50B2-38C8-81E5-DB4E05DBA41F
-  Functions: 730
-  Symbols:   165
-  CStrings:  1409
+  UUID: C5A8EC7E-EF8C-3E98-8BA7-04011A9B3249
+  Functions: 745
+  Symbols:   169
+  CStrings:  1442
 
Symbols:
+ _DMIsMigrationNeeded
+ __dispatch_source_type_timer
+ _dispatch_source_cancel
+ _dispatch_source_set_timer
CStrings:
+ "@\"NSObject<OS_dispatch_source>\""
+ "DataMigration in progress - not applying any power target mitigations"
+ "DataMigration monitoring timer stopped - migration complete"
+ "DataMigration needed. Creating resource hint"
+ "DataMigration no longer needed. Releasing resource hint"
+ "DataMigration status check: migrationNeeded=%d"
+ "DataMigrationInProgress"
+ "Error in fetching lock state"
+ "Started DataMigration monitoring timer (immediate first check, then 5 minute intervals)"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_dataMigrationTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,V_modeActive"
+ "T@\"NSObject<OS_os_transaction>\",&,V_powerBudgetActive"
+ "T@\"ResourceHint\",&,V_dataMigrationResourceHint"
+ "Updating lock state %@"
+ "_dataMigrationResourceHint"
+ "_dataMigrationTimer"
+ "_modeActive"
+ "_powerBudgetActive"
+ "checkDataMigrationStatus"
+ "com.apple.powerexperienced.cpmModeActive"
+ "com.apple.powerexperienced.powerBudgetActive"
+ "dataMigrationResourceHint"
+ "dataMigrationTimer"
+ "evaluatePowerMode: %@: %d display %d unlocked %d, carPlay %d, pluggedIn %d, dataMigrationInProgress %d, batterylevel %@"
+ "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, fitnessIntelligence %d, dataMigrationInProgress %d, pluggedIn %d (allowOnCharger: %d)"
+ "evaluatePowerMode: isUnlocked %d"
+ "initDataMigrationMonitoring"
+ "modeActive"
+ "powerBudgetActive"
+ "setDataMigrationResourceHint:"
+ "setDataMigrationTimer:"
+ "setModeActive:"
+ "setPowerBudgetActive:"
+ "startDataMigrationTimer"
- "evaluatePowerMode: %@: %d display %d, carPlay %d, pluggedIn %d, batterylevel %@"
- "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, fitnessIntelligence %d, pluggedIn %d (allowOnCharger: %d)"

```
