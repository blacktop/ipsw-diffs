## SystemReport-iOS-D83-D84

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84`

```diff

-677.3.6.0.0
-  __TEXT.__text: 0x35564
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x3c20
-  __TEXT.__objc_methlist: 0x198c
+677.4.10.0.0
+  __TEXT.__text: 0x3653c
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x3d80
+  __TEXT.__objc_methlist: 0x19ec
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3ceb0
-  __TEXT.__oslogstring: 0x1d1e
-  __TEXT.__objc_methname: 0x31ab
+  __TEXT.__cstring: 0x3e1c2
+  __TEXT.__oslogstring: 0x1ec8
+  __TEXT.__objc_methname: 0x32f9
   __TEXT.__objc_classname: 0x5e8
-  __TEXT.__objc_methtype: 0x5b4
+  __TEXT.__objc_methtype: 0x5d0
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__unwind_info: 0x63c
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x560
-  __DATA_CONST.__cfstring: 0x277c0
+  __TEXT.__unwind_info: 0x64c
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__const: 0x570
+  __DATA_CONST.__cfstring: 0x290c0
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x2de38
-  __DATA_CONST.__objc_arrayobj: 0x2d0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_arraydata: 0x2fee8
+  __DATA_CONST.__objc_arrayobj: 0x300
   __DATA_CONST.__objc_intobj: 0x558
   __DATA_CONST.__objc_dictobj: 0x208
-  __DATA.__objc_const: 0x3240
-  __DATA.__objc_selrefs: 0x10c8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1b8
-  __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_const: 0x3280
+  __DATA.__objc_selrefs: 0x1120
+  __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x14a0
   __DATA.__data: 0x508
   __DATA.__bss: 0xc8

   - /System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport
   - /System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 333A20BE-47F3-3900-AC31-C695B67D1F1A
-  Functions: 625
-  Symbols:   330
-  CStrings:  13113
+  UUID: 4CE7C7F7-4244-34D1-8F73-B332B45E7E58
+  Functions: 633
+  Symbols:   338
+  CStrings:  13564
 
Symbols:
+ _CFRunLoopGetCurrent
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientScheduleWithRunLoop
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _IOPSCopyPowerSourcesList
+ _IOPSGetPowerSourceDescription
+ _OBJC_CLASS_$_PowerUISmartChargeClient
+ _kCFRunLoopDefaultMode
CStrings:
+ "@\"PowerUISmartChargeClient\""
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): Cannot add 14 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): (#15) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): Cannot add 15 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrAborts(696) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrFullyDone(699) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrResumeSent(689) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrSkippedBlocks(758) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterDestinations(721) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterWrites(722) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): (#32) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): Cannot add 32 elements to context"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): Cannot add 14 elements to context"
+ "BulkCSWReceive2ndTime"
+ "BulkCSWReceiveFail"
+ "BulkCSWReceiveFail2ndTime"
+ "BulkCSWTagError"
+ "BulkCheckStallError"
+ "BulkCheckStallNoHalt"
+ "BulkClearPipeStall"
+ "BulkClearPipeStallError"
+ "BulkCmdNoTimeout"
+ "BulkConfigLunError"
+ "BulkDataOverrun"
+ "BulkDeviceError"
+ "BulkDeviceUnresponsive"
+ "BulkGetEP0StatusError"
+ "BulkGetEPStatusError"
+ "BulkIOAborted"
+ "BulkIOTimeOut"
+ "BulkMassStorageReset"
+ "BulkMassStorageResetError"
+ "BulkMaxLunNoResp"
+ "BulkMaxLunStall"
+ "BulkMaxLunZero"
+ "BulkPhaseError"
+ "BulkPipeStall"
+ "BulkSendCBWError"
+ "BulkSendCSWRecvError"
+ "BulkSendFail"
+ "BulkStallCBW"
+ "BulkStdResetDeviceError"
+ "BulkStdResetDeviceSuccess"
+ "BulkStdResetDeviceTerminate"
+ "BulkTimeout"
+ "BulkUseStdResetDevice"
+ "BulkXfrDataError"
+ "Couldn't find prox service\n"
+ "Couldn't open hid system"
+ "Couldn't retrieve property from HID service..."
+ "CumReadLatency"
+ "CumTrimLatency"
+ "CumWriteLatency"
+ "Date of first use"
+ "Date of manufacture"
+ "DevConn15Min"
+ "DevConn1H"
+ "DevConn2H"
+ "DevConn30Min"
+ "DevConn4H"
+ "DevConn8H"
+ "DevConnDays"
+ "DevConnLessThan15Min"
+ "DeviceDropReEnum"
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "DriverNubStartError"
+ "Error during retrieving MCL status: %@"
+ "Error during retrieving OBC status: %@"
+ "EventVersion"
+ "Failed to retrieve battery date of first use."
+ "Failed to retrieve battery date of manufacture."
+ "Failed to retrieve power source description."
+ "Failed to retrieve power sources info (kIOPSSourceInternal)."
+ "Failed to retrieve power sources list."
+ "FindPipeError"
+ "GCReadSequential"
+ "GCReadSequential_"
+ "GCReadSequential_0"
+ "GCReadSequential_1"
+ "GCReadSequential_10"
+ "GCReadSequential_11"
+ "GCReadSequential_12"
+ "GCReadSequential_13"
+ "GCReadSequential_2"
+ "GCReadSequential_3"
+ "GCReadSequential_4"
+ "GCReadSequential_5"
+ "GCReadSequential_6"
+ "GCReadSequential_7"
+ "GCReadSequential_8"
+ "GCReadSequential_9"
+ "GetStreamError"
+ "IOLatency100ms"
+ "IOLatency10ms"
+ "IOLatency10s"
+ "IOLatency1s"
+ "IOLatency20ms"
+ "IOLatency30s"
+ "IOLatency40ms"
+ "InterfaceClampOnNoDevice"
+ "InterfaceClampOnTimeout"
+ "InterfaceOffTerminate"
+ "InterfaceOnTerminate"
+ "InterfaceProtocol"
+ "InterfaceTerminate"
+ "InterimAttachError"
+ "InterimDetachError"
+ "KioskMode"
+ "KioskModeMode"
+ "Length of AHPS Microphone Calibration Data is not as expected: %lu!"
+ "LinkRetrain"
+ "ManualLimit"
+ "None"
+ "NumInterfaceNubs"
+ "Optimized"
+ "PCIDeviceOn"
+ "PCIDevicePause"
+ "PowerOnNewInterface"
+ "PowerOnReEnumWait"
+ "PowerOnTerminate"
+ "PowerTransToOff"
+ "PowerTransToOn"
+ "RdWrCheckCondition"
+ "ReEnumTimeoutTerminate"
+ "ReadCmdCount"
+ "ReadKBytes"
+ "ReattachDeviceMatchError"
+ "ReattachNoResetError"
+ "ReattachOpenError"
+ "ReattachPipeError"
+ "ReattachTerminate"
+ "Reattached"
+ "ResetDeviceError"
+ "ResetDeviceNotFoundError"
+ "ResetDeviceSuccess"
+ "ResetDeviceTerminate"
+ "ResetTerminatedDevice"
+ "ResetTimeout"
+ "ResetUSBHostDeviceError"
+ "StartStopUnitCmdCount"
+ "SupplyCurrentReading"
+ "T@\"NSString\",?,R,C"
+ "T@\"PowerUISmartChargeClient\",&,N,V_smartChargeClient"
+ "TaskMgmtError"
+ "TaskMgmtErrorResponse"
+ "TaskMgmtLUNReset"
+ "TaskMgmtShutdown"
+ "TaskMgmtTaskAbort"
+ "TaskMgmtTimeout"
+ "TrimCmdCount"
+ "UASCmdInvalidTag"
+ "UASCmdNoTimeout"
+ "UASCommandFail"
+ "UASDataFail"
+ "UASIOTimeOut"
+ "UASNumOfStreams"
+ "UASReadIUFail"
+ "UASRequestForStatusFail"
+ "UASResetErrTerminate"
+ "UASResetError"
+ "UASResetNoDevice"
+ "UASResetOnPowerOn"
+ "UASResetSuccess"
+ "UASResponseIUFail"
+ "UASSendFail"
+ "UASStartError"
+ "UASStatusFail"
+ "UASStreamStatusFail"
+ "UASTerminateCmdWait"
+ "UASTerminateResetWait"
+ "UASWriteIUFail"
+ "USB Storage payload"
+ "USBProdRel"
+ "USBProductID"
+ "USBProductString"
+ "USBVendorID"
+ "USBVendorString"
+ "WakeHibStandby"
+ "WriteCmdCount"
+ "WriteKBytes"
+ "_smartChargeClient"
+ "addDateOfManufactureAndFirstUseToDictionary:"
+ "bandsAgeBinsReadSectors"
+ "bandsAgeBinsReadSectors_"
+ "bandsAgeBinsSnapshot"
+ "bandsAgeBinsSnapshot_"
+ "bandsAgeBinsV2"
+ "bandsAgeBinsV2_"
+ "batteryOptimizationMode"
+ "com.apple.diagnostics"
+ "com.apple.massStorage.NANDInfo.SM.FTLStatArray_4"
+ "com.apple.massStorage.USBStorageInfo.Counters"
+ "dateOfFirstUse"
+ "dateOfManufacture"
+ "daysSinceLastHarmonicLeft"
+ "daysSinceLastHarmonicRight"
+ "gcPDusterDestinations"
+ "gcPDusterWrites"
+ "gcwamp"
+ "gcwamp_"
+ "gcwamp_0"
+ "gcwamp_1"
+ "gcwamp_10"
+ "gcwamp_11"
+ "gcwamp_12"
+ "gcwamp_13"
+ "gcwamp_14"
+ "gcwamp_15"
+ "gcwamp_16"
+ "gcwamp_17"
+ "gcwamp_18"
+ "gcwamp_19"
+ "gcwamp_2"
+ "gcwamp_20"
+ "gcwamp_21"
+ "gcwamp_22"
+ "gcwamp_23"
+ "gcwamp_24"
+ "gcwamp_25"
+ "gcwamp_26"
+ "gcwamp_27"
+ "gcwamp_28"
+ "gcwamp_29"
+ "gcwamp_3"
+ "gcwamp_30"
+ "gcwamp_31"
+ "gcwamp_4"
+ "gcwamp_5"
+ "gcwamp_6"
+ "gcwamp_7"
+ "gcwamp_8"
+ "gcwamp_9"
+ "hostReadSequential"
+ "hostReadSequential_"
+ "hostReadSequential_0"
+ "hostReadSequential_1"
+ "hostReadSequential_10"
+ "hostReadSequential_11"
+ "hostReadSequential_12"
+ "hostReadSequential_13"
+ "hostReadSequential_2"
+ "hostReadSequential_3"
+ "hostReadSequential_4"
+ "hostReadSequential_5"
+ "hostReadSequential_6"
+ "hostReadSequential_7"
+ "hostReadSequential_8"
+ "hostReadSequential_9"
+ "initWithClientName:"
+ "isMCLCurrentlyEnabled:"
+ "isMCLSupported"
+ "isOBCSupported"
+ "isSmartChargingCurrentlyEnabled:"
+ "kioskMode"
+ "setSmartChargeClient:"
+ "smartChargeClient"
+ "supplyCurrent"
+ "supplyCurrentReading"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): (#10) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): Cannot add 10 elements to context"
- "FTL counters"
- "Length of AHPS Microphone Calibration Data changed to %lu!"
- "fwaHistogram"
- "fwaHistogram_"
- "fwaHistogram_0"
- "fwaHistogram_1"
- "fwaHistogram_2"
- "fwaHistogram_3"
- "fwaHistogram_4"
- "fwaHistogram_5"
- "fwaHistogram_6"
- "fwaHistogram_7"
- "fwaHistogram_8"
- "fwaHistogram_9"

```
