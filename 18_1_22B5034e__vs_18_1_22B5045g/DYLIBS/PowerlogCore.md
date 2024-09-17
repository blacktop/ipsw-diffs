## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-2308.40.23.502.2
-  __TEXT.__text: 0xd3320
+2308.40.41.0.0
+  __TEXT.__text: 0xd5178
   __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x81b0
-  __TEXT.__const: 0x16b0
-  __TEXT.__cstring: 0x37824
+  __TEXT.__objc_methlist: 0x8210
+  __TEXT.__const: 0x1748
+  __TEXT.__cstring: 0x37c20
   __TEXT.__gcc_except_tab: 0x29b0
-  __TEXT.__oslogstring: 0x6c8a
-  __TEXT.__unwind_info: 0x2bd8
+  __TEXT.__oslogstring: 0x6edf
+  __TEXT.__unwind_info: 0x2c08
   __TEXT.__objc_classname: 0x868
-  __TEXT.__objc_methname: 0x127ea
-  __TEXT.__objc_methtype: 0x1780
-  __TEXT.__objc_stubs: 0xf5c0
+  __TEXT.__objc_methname: 0x12883
+  __TEXT.__objc_methtype: 0x178b
+  __TEXT.__objc_stubs: 0xf720
   __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__const: 0x2528
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e50
+  __DATA_CONST.__objc_selrefs: 0x4e90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x35f20
+  __DATA_CONST.__objc_arraydata: 0x36210
   __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__const: 0x1d60
-  __AUTH_CONST.__cfstring: 0x55fc0
-  __AUTH_CONST.__objc_const: 0x9178
+  __AUTH_CONST.__cfstring: 0x564e0
+  __AUTH_CONST.__objc_const: 0x9188
   __AUTH_CONST.__objc_intobj: 0x4458
   __AUTH_CONST.__objc_doubleobj: 0xf30
-  __AUTH_CONST.__objc_arrayobj: 0xf60
-  __AUTH_CONST.__objc_dictobj: 0xdd68
+  __AUTH_CONST.__objc_arrayobj: 0xf90
+  __AUTH_CONST.__objc_dictobj: 0xdea8
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x614
   __DATA.__data: 0x438
-  __DATA.__bss: 0x1b89
+  __DATA.__bss: 0x1b81
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b30
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xb18
+  __DATA_DIRTY.__bss: 0xb20
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4162
-  Symbols:   5842
-  CStrings:  15830
+  Functions: 4183
+  Symbols:   5871
+  CStrings:  15896
 
Symbols:
+ _kPLSubmissionXC
+ _kPLSubmissionPLL
+ _kPLSubmissionSP
+ _kPLSubmissionBDC
+ _kPLBB23B
+ _kPLSubmissionPLLUpgrade
+ _kPLSubmissionMSS
+ _kPLSubmissionCE
+ _kPLSubmissionBG
CStrings:
+ "ActiveFreq_lockout"
+ "UPDATE %!@(MISSING) SET %!@(MISSING) = (((cast(\"%!@(MISSING)\" as int) + 180) + (180 / 2)) / 180) * 180"
+ "PocketDetection"
+ "No archived upgrade powerlog for upgrade date '%!@(MISSING)'"
+ "PerfPowerServicesSignpostReader tarball path: %!@(MISSING)"
+ "Choosing archived powerlog for upgrade date '%!@(MISSING)': %!@(MISSING)"
+ "PLL-Upgrade"
+ "UpgradePowerlog"
+ "@20@0:8s16"
+ "CaptureButtonAction"
+ "WHERE rowid IN (SELECT rowid FROM tmp WHERE rn = 1);"
+ "D94"
+ "upgradesubmission"
+ "Dropping tables with > 24 hr retention for upgrade tasking"
+ "submitPLLUpgrade"
+ "Upgrade powerlog requested"
+ "AOP2Power"
+ "ActiveFreq_F2"
+ "Applying config timestamp bucketization for upgrade tasking"
+ "UpgradeTasking"
+ "Upgrade date is within active powerlog region"
+ "%!@(MISSING) %!@(MISSING) %!@(MISSING)"
+ "Skipping flush"
+ "D48"
+ "Removing config columns for upgrade tasking"
+ "tasking config bools: %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "InCallBackgroundTime"
+ "WITH tmp AS (SELECT rowid, ROW_NUMBER() OVER (PARTITION BY %!@(MISSING), %!@(MISSING) ORDER BY timestamp) AS rn FROM %!@(MISSING) WHERE %!@(MISSING) != %!@(MISSING) OR %!@(MISSING) IS NULL)"
+ "AOP-EXCLAVEPower"
+ "Tasked Upgrade OTA"
+ "BaselineTrackingFreq_F2"
+ "BaselineTrackingFreq_lockout"
+ "Wake Count"
+ "HighLevelState_Baseline"
+ "InPocketDecision"
+ "InCallScreenOnTime"
+ "monotonicUpgradeDate=%!@(MISSING)"
+ "archiveForDate:"
+ "Copying archive at '%!@(MISSING)' to '%!@(MISSING)'..."
+ "CaptureButtonConfig"
+ "startDate=%!@(MISSING), endDate=%!@(MISSING)"
+ "DetectionSessionStopTime"
+ "UPDATE %!@(MISSING) SET %!@(MISSING) = (((cast(\"%!@(MISSING)\" as int) + 60) + (60 / 2)) / 60) * 60"
+ "DetectionSessionStartTime"
+ "Dropping config data for upgrade tasking"
+ "HighLevelState_Active"
+ "D47"
+ "AdditionalTables: %!@(MISSING)"
+ "BaselineTrackingFreq_F1"
+ "v24@?0@8^B16"
+ "Upgrade date is outside of active powerlog region"
+ "copyPowerlogToPath:"
+ "WHERE rowid IN (SELECT rowid FROM tmp WHERE rn > 1);"
+ "CameraCapture"
+ "bb23B"
+ "ALTER TABLE %!@(MISSING) DROP COLUMN %!@(MISSING)"
+ "ActiveFreq_F1"
+ "copyArchiveAtPath:to:"
+ "Preparing upgrade powerlog..."
+ "upgrade-archive"
+ "Button"
+ "DELETE FROM %!@(MISSING) WHERE (%!@(MISSING) != %!@(MISSING))"
+ "Dropping table '%!@(MISSING)' which is retained > 24 hr"
+ "copyUpgradePowerlogToPath:"
+ "getFirstBatteryTimestamp"
+ "Preparing most recent powerlog archive..."
+ "PLIOReportAgent_EventBackward_MTPbuttoncapture"
+ "initWithReasonType:"
+ "flush"
+ "monotonicPowerlogRange=[%!@(MISSING), %!@(MISSING)]"
+ "D93"
+ "Deleting tables > 24 hours for upgrade tasking"
- "_additionalTables: Looking for DRConfig"
- "_additionalTables: %!@(MISSING)"
- "Copying last archive to %!@(MISSING)..."
- "tasking config bools: %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING)"
- "PerfPowerServicesSignpostreader tarball path: %!@(MISSING)"
- "_additionalTables: DRConfig not found. Looking for DA defaults"

```
