## hangreporter

> `/usr/libexec/hangreporter`

```diff

-380.0.0.0.0
-  __TEXT.__text: 0x3e1a4
-  __TEXT.__auth_stubs: 0xf00
+382.0.0.0.0
+  __TEXT.__text: 0x3e978
+  __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_stubs: 0x2d40
-  __TEXT.__objc_methlist: 0xf74
+  __TEXT.__objc_methlist: 0xf84
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x2e80e
-  __TEXT.__oslogstring: 0x4b84
+  __TEXT.__cstring: 0x2f104
+  __TEXT.__oslogstring: 0x4b03
   __TEXT.__objc_classname: 0x147
-  __TEXT.__objc_methname: 0x5192
+  __TEXT.__objc_methname: 0x51e5
   __TEXT.__objc_methtype: 0x87b
   __TEXT.__gcc_except_tab: 0xc60
-  __TEXT.__unwind_info: 0x518
-  __DATA_CONST.__auth_got: 0x790
+  __TEXT.__unwind_info: 0x510
+  __DATA_CONST.__auth_got: 0x798
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1470
-  __DATA_CONST.__cfstring: 0x4b40
+  __DATA_CONST.__const: 0x1450
+  __DATA_CONST.__cfstring: 0x4aa0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x2640
-  __DATA.__objc_selrefs: 0x1060
-  __DATA.__objc_ivar: 0x258
+  __DATA.__objc_const: 0x2670
+  __DATA.__objc_selrefs: 0x1068
+  __DATA.__objc_ivar: 0x25c
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x638
   __DATA.__bss: 0x1d8

   - /System/Library/PrivateFrameworks/HangTracer.framework/HangTracer
   - /System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3FE64A91-631C-38DA-80C8-A0D844BC1EAE
-  Functions: 673
-  Symbols:   331
-  CStrings:  5537
+  UUID: E68C0CEF-364F-39BE-9E2D-EAE1123950EF
+  Functions: 676
+  Symbols:   332
+  CStrings:  5569
 
Symbols:
+ _NSStringFromRBSRole
CStrings:
+ "ASPFTLParseBufferToCxt: boffOrderedRaidSuccessValidLba(1380) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: boffOrderedReadBlank(1379) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: boffOrderedUnexpectedBlankValid(1382) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempHighValue(1449) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempLowValue(1450) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempMaxValue(1448) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedBandOrphansNumBands(1335) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedBandOrphansNumSectors(1336) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedDefragEvents(1337) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedDefragIterations(1338) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedDefragSectors(1339) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedRecoverableErrorGbbs(1333) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcBoffOrderedUnrecoverableErrorGbbs(1334) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: ldefragFailedMemBalancer(1401) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidExpectedFailBMXReconstructionHost(1386) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidExpectedFailBMXReconstructionInternal(1385) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidExpectedFailPMXReconstructionHost(1384) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidExpectedFailPMXReconstructionInternal(1383) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: selfPanicEnabled(1452) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: unexpectedRaidFailures(1381) cannot add 1 element to context"
+ "Generated State Info JSON Payload Dict: (%{public}@) for tailspinInfoDict: (%{public}@)"
+ "ShouldCollectCPURoleInfo"
+ "TB,R,V_shouldCollectCPURoleInfo"
+ "The provided stateInfoArray '%@' only has state objects AFTER then end of the hang (%llu matu)."
+ "_shouldCollectCPURoleInfo"
+ "boffOrderedRaidSuccessValidLba"
+ "boffOrderedReadBlank"
+ "boffOrderedUnexpectedBlankValid"
+ "cpuRoleBreakdown"
+ "cpuRoleEnum"
+ "cpuRoleName"
+ "deviceTempHighValue"
+ "deviceTempLowValue"
+ "deviceTempMaxValue"
+ "endCPURole"
+ "gcBoffOrderedBandOrphansNumBands"
+ "gcBoffOrderedBandOrphansNumSectors"
+ "gcBoffOrderedDefragEvents"
+ "gcBoffOrderedDefragIterations"
+ "gcBoffOrderedDefragSectors"
+ "gcBoffOrderedRecoverableErrorGbbs"
+ "gcBoffOrderedUnrecoverableErrorGbbs"
+ "intervalsInCPURole"
+ "ldefragFailedMemBalancer"
+ "percentInCPURole"
+ "raidExpectedFailBMXReconstructionHost"
+ "raidExpectedFailBMXReconstructionInternal"
+ "raidExpectedFailPMXReconstructionHost"
+ "raidExpectedFailPMXReconstructionInternal"
+ "secondsSinceCPURoleTransitionBeforeHangStart"
+ "selfPanicEnabled"
+ "shouldCollectCPURoleInfo"
+ "startCPURole"
+ "timeInCPURole"
+ "unexpectedRaidFailures"
- "Found last State Info transition before hang end:%llu at index %lu for array %@"
- "Found last State Info transition before hang start:%llu at index %lu for array %@."
- "RBSTaskStateNone"
- "RBSTaskStateRunningScheduled"
- "RBSTaskStateRunningSuspended"
- "RBSTaskStateRunningUnknown"
- "RBSTaskStateUnknown"
- "State Info JSON Payload Dict: %@"
- "The provided stateInfoArray '%@' only has state objects BEFORE the start (%llu matu) but AFTER then end (%llu matu)."
- "endTaskState"
- "intervalsInTaskState"
- "percentInTaskState"
- "secondsSinceTaskStateTransitionBeforeHangStart"
- "startTaskState"
- "taskEnum"
- "taskStateBreakdown"
- "taskStateEnum"
- "taskStateName"
- "timeInTaskState"

```
