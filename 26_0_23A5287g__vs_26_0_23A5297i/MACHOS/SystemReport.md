## SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x3b474
-  __TEXT.__auth_stubs: 0xd00
+1066.0.41.0.0
+  __TEXT.__text: 0x3bc7c
+  __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_stubs: 0x4460
   __TEXT.__objc_methlist: 0x1c3c
-  __TEXT.__cstring: 0x40be0
+  __TEXT.__cstring: 0x41550
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x1fac
-  __TEXT.__objc_methname: 0x3838
+  __TEXT.__oslogstring: 0x2014
+  __TEXT.__objc_methname: 0x3832
   __TEXT.__objc_classname: 0x62b
   __TEXT.__objc_methtype: 0x5d5
   __TEXT.__gcc_except_tab: 0x288
   __TEXT.__unwind_info: 0x6d8
-  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__auth_got: 0x698
   __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x528
-  __DATA_CONST.__cfstring: 0x24ac0
+  __DATA_CONST.__const: 0x550
+  __DATA_CONST.__cfstring: 0x24c80
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x11130
+  __DATA_CONST.__objc_arraydata: 0x11210
   __DATA_CONST.__objc_arrayobj: 0x3c0
   __DATA_CONST.__objc_intobj: 0x690
   __DATA_CONST.__objc_dictobj: 0x168

   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 0942C7A5-177C-3091-A04E-5F62A94A51E7
-  Functions: 693
-  Symbols:   342
-  CStrings:  12986
+  UUID: 0E70CF62-6645-3426-B5A1-E1AA2A5308A9
+  Functions: 695
+  Symbols:   343
+  CStrings:  13042
 
Symbols:
+ _CRGetComponentState
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
+ "FaceID component repair status is state %d"
+ "Failed to query repair status for FaceID component, error %@"
+ "boffOrderedRaidSuccessValidLba"
+ "boffOrderedReadBlank"
+ "boffOrderedUnexpectedBlankValid"
+ "deviceTempHighValue"
+ "deviceTempLowValue"
+ "deviceTempMaxValue"
+ "faceIDFdrValidationStatus"
+ "gcBoffOrderedBandOrphansNumBands"
+ "gcBoffOrderedBandOrphansNumSectors"
+ "gcBoffOrderedDefragEvents"
+ "gcBoffOrderedDefragIterations"
+ "gcBoffOrderedDefragSectors"
+ "gcBoffOrderedRecoverableErrorGbbs"
+ "gcBoffOrderedUnrecoverableErrorGbbs"
+ "ldefragFailedMemBalancer"
+ "raidExpectedFailBMXReconstructionHost"
+ "raidExpectedFailBMXReconstructionInternal"
+ "raidExpectedFailPMXReconstructionHost"
+ "raidExpectedFailPMXReconstructionInternal"
+ "selfPanicEnabled"
+ "unexpectedRaidFailures"
- "biometricKitFdrValidationStatus"

```
