## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1527.80.3.0.0
-  __TEXT.__text: 0x3a7f8
-  __TEXT.__auth_stubs: 0xbe0
+1527.100.24.0.0
+  __TEXT.__text: 0x3b510
+  __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_stubs: 0x1640
-  __TEXT.__objc_methlist: 0x594
-  __TEXT.__const: 0x3f0
-  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__objc_methlist: 0x58c
+  __TEXT.__const: 0x3d0
+  __TEXT.__gcc_except_tab: 0x85c
   __TEXT.__oslogstring: 0x2407
-  __TEXT.__cstring: 0x2fbbe
-  __TEXT.__objc_classname: 0xc4
+  __TEXT.__cstring: 0x30c2b
+  __TEXT.__objc_classname: 0xc2
   __TEXT.__objc_methtype: 0x2a9
-  __TEXT.__objc_methname: 0x1605
-  __TEXT.__unwind_info: 0x590
-  __DATA_CONST.__auth_got: 0x600
+  __TEXT.__objc_methname: 0x15cb
+  __TEXT.__unwind_info: 0x5a0
+  __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0xa8
-  __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x1ba0
+  __DATA_CONST.__const: 0x6a8
+  __DATA_CONST.__cfstring: 0x1c60
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x600
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0x6b8
+  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8
   __DATA.__bss: 0x150

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: A68F9F41-4FED-3DDC-86F2-B6155C4E36D4
-  Functions: 348
-  Symbols:   258
-  CStrings:  4391
+  UUID: 6935865C-17F9-324A-BFA7-51F0F9ABC72D
+  Functions: 363
+  Symbols:   253
+  CStrings:  4484
 
Symbols:
+ _objc_retain_x24
+ _objc_retain_x25
- ___strlcpy_chk
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "%@/PalmspringCrashlog_%@_%@.%@"
+ "@28@0:8C16C20I24"
+ "ASPFTLParseBufferToCxt: IND_pool_avgTileSlackP(1703) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: IND_pool_tilesInUseP(1672) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: IND_pool_tilesSlackP(1673) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: dataLossHisto(1683): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: dataLossHisto(1683): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: extraSenseHisto(1676): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: extraSenseHisto(1676): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: formatNum(1654) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: formatNumOnSwitch(1658): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: formatNumOnSwitch(1658): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: huState(1660): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: huState(1660): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: massScanCurrentState(1347) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanForceStartWithPilot(1425) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanIgnoredRaidConversion(1477) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanNarrowBandsRefreshed(1476) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanPilotFailedContinuedToFull(1665) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanPilotIgnoredTooFrequent(1424) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanTotalRefreshedBands(1475) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanTotalScannedBands(1474) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: mspSOCID(1688) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numPaddingPfail(1480) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: pePrevStartSLC(1662): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: pePrevStartSLC(1662): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: pePrevStartTLC(1661): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: pePrevStartTLC(1661): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: peThresholdStart(1659): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: peThresholdStart(1659): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: perfPOHisto(1675): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: perfPOHisto(1675): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: qualClassHisto(1680): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: qualClassHisto(1680): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: relClassHisto(1679): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: relClassHisto(1679): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: relPOHisto(1677): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: relPOHisto(1677): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: turboFailureHisto(1682): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: turboFailureHisto(1682): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: turboSuccessHisto(1681): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: turboSuccessHisto(1681): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: uncHisto(1678): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: uncHisto(1678): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: unhLogIndex(1655) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: waAtTheRecordingPoint(1663): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: waAtTheRecordingPoint(1663): Cannot add 4 elements to context"
+ "ASPMSPParseBufferToCxt: fw_version_identifier(16384): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: fw_version_identifier(16384): cfg 8 elements; (8*1) cfg bytes != (%d) buffer bytes"
+ "B56@0:8@16@24@32Q40^@48"
+ "IND_pool_avgTileSlackP"
+ "IND_pool_tilesInUseP"
+ "IND_pool_tilesSlackP"
+ "MT crash"
+ "RD_OptionalPORefreshFailed"
+ "RD_OptionalPORefreshHotBandFailed"
+ "ST Info and Error Stats"
+ "ST crash"
+ "ST crash(rebooted)"
+ "Unknown(%d)"
+ "bootPowerMode"
+ "cbdrInvalidGrade"
+ "cbdrNeedToRefresh"
+ "cbdrNoNeedToRefresh"
+ "dataLossHisto"
+ "dataLossHisto_"
+ "extraSenseHisto"
+ "extraSenseHisto_"
+ "formatNum"
+ "formatNumOnSwitch"
+ "formatNumOnSwitch_"
+ "fw_version_identifier_"
+ "huState"
+ "huState_"
+ "initWithUniqueID:type:headerAndRawBlobSize:"
+ "massScanPilotFailedContinuedToFull"
+ "mspSOCID"
+ "numPaddingPfail"
+ "pePrevStartSLC"
+ "pePrevStartSLC_"
+ "pePrevStartTLC"
+ "pePrevStartTLC_"
+ "peThresholdStart"
+ "peThresholdStart_"
+ "perfPOHisto"
+ "perfPOHisto_"
+ "qualClassHisto"
+ "qualClassHisto_"
+ "relClassHisto"
+ "relClassHisto_"
+ "relPOHisto"
+ "relPOHisto_"
+ "turboFailureHisto"
+ "turboFailureHisto_"
+ "turboSuccessHisto"
+ "turboSuccessHisto_"
+ "uncHisto"
+ "uncHisto_"
+ "unhLogIndex"
+ "waAtTheRecordingPoint"
+ "waAtTheRecordingPoint_"
+ "writeToDirectory:crashlogData:name:options:error:"
- "%@/PalmspringCrashlog_%@.%@"
- "@36@0:8C16C20I24@28"
- "ASPMSPParseBufferToCxt: fw_version_identifier(16384): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: fw_version_identifier(16384): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8196): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8196): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8195): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8195): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "B48@0:8@16@24Q32^@40"
- "T@\"NSString\",R,N,V_name"
- "_name"
- "fw_version_identifier"
- "initWithUniqueID:type:headerAndRawBlobSize:name:"
- "stringWithCString:encoding:"
- "writeToDirectory:crashlogData:options:error:"

```
