## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1438.120.9.0.0
-  __TEXT.__text: 0x37ba0
+1512.0.0.0.0
+  __TEXT.__text: 0x37e98
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x1420
+  __TEXT.__objc_stubs: 0x13e0
   __TEXT.__objc_methlist: 0x55c
   __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x814
-  __TEXT.__oslogstring: 0x208f
-  __TEXT.__cstring: 0x2e1a2
+  __TEXT.__gcc_except_tab: 0x7c4
+  __TEXT.__oslogstring: 0x20c2
+  __TEXT.__cstring: 0x2e60d
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x1462
+  __TEXT.__objc_methname: 0x1448
   __TEXT.__unwind_info: 0x520
   __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x98
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x1ac0
+  __DATA_CONST.__cfstring: 0x1a40
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x578
+  __DATA.__objc_selrefs: 0x568
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/WirelessInsights.framework/WirelessInsights
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 46BFD0FD-253B-3CB6-976F-88E1FAB7E52F
-  Functions: 310
+  UUID: 89E11AA5-5E2F-3716-BF0C-CF8087C68621
+  Functions: 314
   Symbols:   251
-  CStrings:  4194
+  CStrings:  4235
 
Symbols:
+ _WISServerConsolidateDeviceDiagnostics
+ _kWisDiagnosticsFileArray
- _AWDServerConsolidateDeviceDiagnostics
- _kAwdDiagnosticsFileArray
CStrings:
+ "PO_SkipOnHighRD_slc"
+ "PO_SkipOnHighRD_tlc"
+ "RD_CBDR_requested"
+ "RD_CBDRwasFailedToRun"
+ "RD_OptionalPORefresh"
+ "RD_OptionalPORefreshHotBand"
+ "RD_RefreshOnSampling"
+ "RD_SamplesRequested"
+ "RD_closedBandMustSet"
+ "TASK_TYPE_ESIM_SETUP"
+ "autoReadXacts"
+ "autoReads"
+ "autoreadPrefetches"
+ "boffOrderedRaidSuccessValidLba"
+ "boffOrderedReadBlank"
+ "boffOrderedUnexpectedBlankValid"
+ "bootUpDuration"
+ "cbdrBandsRefreshedSLC"
+ "cbdrRefreshedAges2"
+ "cbdrScanPct2"
+ "deprecated_raidFailedReadBlog"
+ "deviceTempHighValue"
+ "deviceTempLowValue"
+ "deviceTempMaxValue"
+ "dmReasonsTlc_mbc2"
+ "eSIM setup SPI not available"
+ "eSIM setup error: %s\n"
+ "eSIM setup gave nil array for file key"
+ "eSIM setup gave no error, but has a nil dict!"
+ "eSIM setup timed out"
+ "eSIMSetupTaskWithTimeout:"
+ "gcBoffOrderedBandOrphansNumBands"
+ "gcBoffOrderedBandOrphansNumSectors"
+ "gcBoffOrderedDefragEvents"
+ "gcBoffOrderedDefragIterations"
+ "gcBoffOrderedDefragSectors"
+ "gcBoffOrderedRecoverableErrorGbbs"
+ "gcBoffOrderedUnrecoverableErrorGbbs"
+ "gcQLCHighWaActivation"
+ "immediatePadding"
+ "lastWipe"
+ "ldefragFailedMemBalancer"
+ "raidExpectedFailBMXReconstructionHost"
+ "raidExpectedFailBMXReconstructionInternal"
+ "raidExpectedFailPMXReconstructionHost"
+ "raidExpectedFailPMXReconstructionInternal"
+ "raidTLCPadding"
+ "readVerifyNative2"
+ "reducedReadVerifyNative2"
+ "selfPanicEnabled"
+ "selfThrottlingEnabled"
+ "snapPreserveSecondaryCount"
+ "spiRollbackCount"
+ "totalPadding"
+ "unexpectedRaidFailures"
+ "unhappyMaxDepthPerDip"
+ "unhappyWideSOBand"
+ "usingReducedGcBuffers"
- "/etc"
- "/private"
- "/tmp"
- "/var"
- "AWDServer SPI not available"
- "Invalid file list returned from AWD server."
- "TASK_TYPE_AWD"
- "Timed out waiting for AWD server."
- "_AWDTaskWithTimeout:"
- "cbdrLastScannedHr"
- "cbdrLastScannedHrHP"
- "hasPrefix:"
- "pathWithComponents:"

```
