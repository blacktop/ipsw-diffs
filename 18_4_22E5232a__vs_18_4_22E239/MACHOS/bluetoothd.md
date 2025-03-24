## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-184.42.1.2.0
-  __TEXT.__text: 0x7c1288
-  __TEXT.__auth_stubs: 0x4610
-  __TEXT.__objc_stubs: 0x12ca0
+184.42.1.3.0
+  __TEXT.__text: 0x7c5350
+  __TEXT.__auth_stubs: 0x4620
+  __TEXT.__objc_stubs: 0x130e0
   __TEXT.__init_offsets: 0x54
-  __TEXT.__objc_methlist: 0x6524
-  __TEXT.__const: 0xa76c
-  __TEXT.__gcc_except_tab: 0x61408
-  __TEXT.__cstring: 0xa2729
-  __TEXT.__objc_classname: 0x7ea
-  __TEXT.__objc_methname: 0x15b6d
+  __TEXT.__objc_methlist: 0x6554
+  __TEXT.__const: 0xa77c
+  __TEXT.__gcc_except_tab: 0x619a4
+  __TEXT.__cstring: 0xa2bbe
+  __TEXT.__objc_classname: 0x7eb
+  __TEXT.__objc_methname: 0x15e31
   __TEXT.__objc_methtype: 0x44e3
-  __TEXT.__oslogstring: 0xa148d
+  __TEXT.__oslogstring: 0xa1867
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x1fa28
+  __TEXT.__unwind_info: 0x1faa8
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x2320
+  __DATA_CONST.__auth_got: 0x2328
   __DATA_CONST.__got: 0xc90
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x2c640
-  __DATA_CONST.__cfstring: 0x1f760
+  __DATA_CONST.__const: 0x2c6c0
+  __DATA_CONST.__cfstring: 0x1f7a0
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0x8e8
+  __DATA_CONST.__objc_intobj: 0x900
   __DATA_CONST.__objc_arraydata: 0x388
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x1c8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xb3b0
-  __DATA.__objc_selrefs: 0x5500
-  __DATA.__objc_ivar: 0xb98
+  __DATA.__objc_const: 0xb4a0
+  __DATA.__objc_selrefs: 0x55f0
+  __DATA.__objc_ivar: 0xbb0
   __DATA.__objc_data: 0x14f0
   __DATA.__data: 0x4668
   __DATA.__crash_info: 0x40

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 30423
-  Symbols:   1546
-  CStrings:  35524
+  Functions: 30457
+  Symbols:   1547
+  CStrings:  35613
 
Symbols:
+ _CBDiscoveryTypesSoftwareUpdate
CStrings:
+ "\x112\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13#\x12\x12\x1a"
+ " payloadDataArray:"
+ "### Attach Multi Instances adv session failed: %@"
+ "### Software Update advertiser create failed"
+ ", suA %s %s "
+ ", suD %@,"
+ "-[CBAdvertiserDaemon _updateSoftwareUpdateAdvertising]"
+ "-[CBAdvertiserDaemon _updateSoftwareUpdatePayload]"
+ "-[CBStackBLEAdvertiserBTStack _updateMultiInstancesAdvertising]"
+ "-[CBStackBLEAdvertiserBTStack _updateMultiInstancesAdvertising]_block_invoke"
+ "-[CBStackBLEAdvertiserBTStack _updateMultiInstancesAdvertising]_block_invoke_2"
+ "20:03:16"
+ "BD_VSC_SET_LPM_HOSTWAKE_SCANPARAMETER"
+ "BD_VSC_SET_LPM_HOSTWAKE_TXADVDIAGPARAMETERS"
+ "BTWake"
+ "BTWake: LMP: entering LPM_SET_SCAN_OFFLOAD_PARAMS %p"
+ "BTWake: LMP: entering Set_LPM_HostWake_ScanParameters with deviceID %p"
+ "BTWake: LMP: entering Set_LPM_HostWake_TxAdvDiagParameters %p"
+ "BTWake: LPM: Invalid blob data %@"
+ "BTWake: LPM: Unsupported power reason %d or params %@"
+ "BTWake: LPM: data %@"
+ "BTWake: LPM: fScanOffloadParams is nil"
+ "BTWake: LPM: mask %@"
+ "CBStackAdvertiserMultiInstances-0x%X"
+ "DiagTxAdv"
+ "Disabling DebugMode configuration flag"
+ "Failed to set seaship flag with error %@"
+ "Feature is not enabled"
+ "LPM: Setting host wake Tx Diag Parameters"
+ "LPM: params reason %d, %@"
+ "LPM: test params reason %d, %@"
+ "Mar 17 2025"
+ "No paramters provided"
+ "OutboxControllerAuth"
+ "Power reason %d is not supported yet"
+ "SWUP action %d, blob  %@, mask %@"
+ "SWUP start scan  %@"
+ "SWUP: Data array count %lu doesn't match with number of available adv instances %d"
+ "SWUP: Session %{public}s has payload data array len %@ with adv interval %u"
+ "SWUP: adding to puck filter"
+ "SWUP: data Array: %@"
+ "SWUP: instance=%d, AdvData=%.*P(%d) interval=%x address:%.6P type:%d overrideAddress:%d ADVType:%d"
+ "SWUP: mfgData %@"
+ "SWUP: mfgData array %@"
+ "Set seaship flag for SEP logging"
+ "Softeware Update Data unchanged: <%@>"
+ "Software Update advertise start: suA %s swD <%@> rate %s"
+ "Software Update advertise stop"
+ "Software Update advertise update: suA %s swD <%@> rate %s"
+ "Software Update updated: suA %s -> %s suD <%@> -> <%@>, rate %s -> %s"
+ "T@\"NSArray\",C,N,V_swupPayloadDataArray"
+ "_swupActionType"
+ "_swupAdvertiseRate"
+ "_swupChanged"
+ "_swupPayloadDataArray"
+ "_swupStackAdvertiser"
+ "c249d6cdce4b07714fee94ea6aebfcc35a53f15c009e8b0a9be8b7e6d01cda63"
+ "dataBlob"
+ "dataMask"
+ "deviceIDAdvScanCount"
+ "deviceIDDiagInfo"
+ "deviceIDDiagLength"
+ "deviceIDInfo"
+ "deviceIDInputKeyMaterial"
+ "deviceIDLength"
+ "deviceIDSalt"
+ "deviceIDTimestampEffectiveBits"
+ "deviceIDTimestampFrequency"
+ "deviceIDTimestampLsbsTruncated"
+ "diagnosticTxAdvBackoff"
+ "diagnosticTxAdvDuration"
+ "diagnosticTxAdvInterval"
+ "gpioAssertionTime"
+ "lpmFlag1 or lpmFlag2 cannot be used concurrently with any other flag."
+ "macKeyDiagInfo"
+ "macKeyDiagLength"
+ "maxClockDriftSeconds"
+ "nextScanDelay"
+ "numberOfDelayIterations"
+ "packetLength"
+ "rssiThresholdValue"
+ "scanDelayStart"
+ "scanDuration"
+ "setConfigFlags:"
+ "setLpmHostWakeScanParameterCB: status = %d"
+ "setLpmHostWakeTxAdvDiagParametersCB: status = %d"
+ "setSwupPayloadDataArray:"
+ "softwareUpdateDataBlob"
+ "softwareUpdateDataMask"
+ "suD: "
+ "swupPayloadDataArray"
+ "\xf0'"
+ "\xff"
- "\x112\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x13\x11\x11\x14\x12\x12\x1a"
- "22:02:00"
- "Mar 12 2025"
- "\xf0&"

```
