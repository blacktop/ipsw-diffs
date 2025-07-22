## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1527.0.0.0.0
-  __TEXT.__text: 0x3845c
+1527.0.2.0.0
+  __TEXT.__text: 0x39268
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x1560
   __TEXT.__objc_methlist: 0x564
   __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x7fc
-  __TEXT.__oslogstring: 0x2207
-  __TEXT.__cstring: 0x2e6fc
+  __TEXT.__gcc_except_tab: 0x848
+  __TEXT.__oslogstring: 0x222b
+  __TEXT.__cstring: 0x2efe5
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x14af
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_methname: 0x1558
+  __TEXT.__unwind_info: 0x558
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x1a80
+  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__cfstring: 0x1b40
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_selrefs: 0x5c8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x150
   __DATA.__common: 0x62
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 12CDF9FD-4FEF-3F85-8476-2137D87C88BF
-  Functions: 322
-  Symbols:   253
-  CStrings:  4259
+  UUID: B12161A9-9B4F-32B4-84DD-26A8881C9758
+  Functions: 333
+  Symbols:   256
+  CStrings:  4307
 
Symbols:
+ _OBJC_CLASS_$_NSInputStream
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSPropertyListSerialization
CStrings:
+ " AND "
+ "(NOT(SELF.lastPathComponent BEGINSWITH '%@-'))"
+ "(NOT(SELF.lastPathComponent CONTAINS '_%@-'))"
+ "(NOT(SELF.lastPathComponent CONTAINS '_%@_'))"
+ "/private/var/mobile/Library/Preferences/com.apple.sysdiagnose.plist"
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
+ "RD_CBDRNotValidUrgentEvict"
+ "Will exclude logs for %lu processes"
+ "close"
+ "enumerateObjectsUsingBlock:"
+ "filterUsingPredicate:"
+ "initWithArray:"
+ "inputStreamWithFileAtPath:"
+ "massScanIgnoredRaidConversion"
+ "massScanNarrowBandsRefreshed"
+ "massScanTotalRefreshedBands"
+ "massScanTotalScannedBands"
+ "open"
+ "predicateWithFormat:"
+ "propertyListWithStream:options:format:error:"
+ "sysdiagnoseExcludeProcessesCrashesAndSpins"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "wearlevelingHotColdFailSafeCnt"

```
