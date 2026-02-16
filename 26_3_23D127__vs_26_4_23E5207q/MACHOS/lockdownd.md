## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1350.40.9.0.0
-  __TEXT.__text: 0x983b4
-  __TEXT.__auth_stubs: 0x1d40
+1365.100.4.0.0
+  __TEXT.__text: 0xb0520
+  __TEXT.__auth_stubs: 0x1cf0
   __TEXT.__objc_stubs: 0x1360
   __TEXT.__objc_methlist: 0xe8
-  __TEXT.__cstring: 0x3a93c
-  __TEXT.__const: 0x10e90
+  __TEXT.__cstring: 0x3ba0b
+  __TEXT.__const: 0x10f50
   __TEXT.__oslogstring: 0x1e6
-  __TEXT.__gcc_except_tab: 0x9b4
+  __TEXT.__gcc_except_tab: 0x9b8
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methname: 0xd61
   __TEXT.__objc_methtype: 0x120
   __TEXT.__services: 0x2d43
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__unwind_info: 0xb98
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0xeb0
-  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__auth_got: 0xe88
+  __DATA_CONST.__got: 0x408
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x7da8
-  __DATA_CONST.__cfstring: 0xda40
+  __DATA_CONST.__const: 0x8398
+  __DATA_CONST.__cfstring: 0xdac0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x510
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1e78
-  __DATA.__bss: 0x200
-  __DATA.__common: 0xa30
+  __DATA.__data: 0x21b8
+  __DATA.__bss: 0x1e8
+  __DATA.__common: 0xab8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CC56A968-DC42-3AEF-A91E-10056C3A119E
-  Functions: 862
-  Symbols:   616
-  CStrings:  7296
+  UUID: 8D7CD309-1B1E-302B-B57B-0F874216747F
+  Functions: 880
+  Symbols:   620
+  CStrings:  7391
 
Symbols:
+ _abort
+ _freeifaddrs
+ _getifaddrs
+ _kCFUserNotificationAlternateButtonAccessibilityIdentifierKey
+ _kCFUserNotificationDefaultButtonAccessibilityIdentifierKey
+ _kLockdownAccessibilityIdentifierTrustNotificationConfirmTrust
+ _kLockdownAccessibilityIdentifierTrustNotificationDenyTrust
+ _mmap
+ _munmap
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
+ _sched_yield
+ _sysconf
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
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
+ "Could not getsockname for peer connection; assuming peer is local"
+ "Could not retrieve list of interfaces; assuming peer is local"
+ "Failed to create path for hostID '%s'"
+ "FanCount"
+ "IND_pool_avgTileSlackP"
+ "IND_pool_tilesInUseP"
+ "IND_pool_tilesSlackP"
+ "Peer is not on a wireless interface."
+ "Session required to enter recovery over RSD."
+ "USBPortCount"
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
+ "kMGQFanCount"
+ "kMGQUSBPortCount"
+ "lockdown-free-pairing=1"
+ "massScanCurrentState"
+ "massScanForceStartWithPilot"
+ "massScanIgnoredRaidConversion"
+ "massScanNarrowBandsRefreshed"
+ "massScanPilotFailedContinuedToFull"
+ "massScanPilotIgnoredTooFrequent"
+ "massScanTotalRefreshedBands"
+ "massScanTotalScannedBands"
+ "mspSOCID"
+ "numPaddingPfail"
+ "pePrevStartSLC"
+ "pePrevStartSLC_"
+ "pePrevStartTLC"
+ "pePrevStartTLC_"
+ "peThresholdStart"
+ "peThresholdStart_"
+ "peer_is_wireless"
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
+ "utun"
+ "waAtTheRecordingPoint"
+ "waAtTheRecordingPoint_"
- "ASPMSPParseBufferToCxt: fw_version_identifier(16384): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: fw_version_identifier(16384): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8196): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8196): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8195): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8195): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "Failed to turn on keepalive."
- "Unexpected remote device type: %d"
- "fw_version_identifier"
- "set_socket_option_keepalive"
- "setsockopt(SO_KEEPALIVE) failed: %s"
- "setsockopt(TCP_KEEPALIVE) failed: %s"
- "setsockopt(TCP_KEEPCNT) failed: %s"
- "setsockopt(TCP_KEEPINTVL) failed: %s"

```
