## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-183.9.1.1.7
-  __TEXT.__text: 0x9467c
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x7f90
-  __TEXT.__const: 0x2250
-  __TEXT.__oslogstring: 0x256b
-  __TEXT.__cstring: 0x117f3
-  __TEXT.__gcc_except_tab: 0x22e4
+184.37.4.0.0
+  __TEXT.__text: 0x96c50
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_methlist: 0x8cf4
+  __TEXT.__const: 0x24fb
+  __TEXT.__oslogstring: 0x2665
+  __TEXT.__cstring: 0x12007
+  __TEXT.__gcc_except_tab: 0x23b8
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x1a48
-  __TEXT.__objc_classname: 0x69d
-  __TEXT.__objc_methname: 0x1391c
-  __TEXT.__objc_methtype: 0x21ad
-  __TEXT.__objc_stubs: 0x8900
+  __TEXT.__unwind_info: 0x1c08
+  __TEXT.__objc_classname: 0x6db
+  __TEXT.__objc_methname: 0x14bb8
+  __TEXT.__objc_methtype: 0x2252
+  __TEXT.__objc_stubs: 0x8d60
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x45f0
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__const: 0x4808
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41c8
+  __DATA_CONST.__objc_selrefs: 0x45d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x930
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0xace0
-  __AUTH_CONST.__objc_const: 0x10d80
-  __AUTH_CONST.__objc_intobj: 0x888
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0xaf60
+  __AUTH_CONST.__objc_const: 0x109f8
+  __AUTH_CONST.__objc_intobj: 0x8b8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xe38
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xef4
   __DATA.__data: 0xd80
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x1d0
-  __DATA_DIRTY.__bss: 0x128
+  __DATA_DIRTY.__bss: 0x130
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3361
-  Symbols:   4274
-  CStrings:  7362
+  Functions: 3714
+  Symbols:   4979
+  CStrings:  7666
 
Symbols:
+ _CBAssignedL2CAPPSMForDCT
+ _CBAssignedL2CAPPSMForSoftwareUpdate
+ _CBCentralManagerScanOptionScanProcessedAtNsec
+ _CBCentralManagerScanOptionScanRequestedAtNsec
+ _CBDiscoveryTypesSoftwareUpdate
+ _CBManagerL2CAPChannelMaxIncomingPayloadSize
+ _CBOptionUseCaseOptions
+ _OBJC_CLASS_$_CBControllerLowPowerModeParams
+ _OBJC_CLASS_$_CBSoftwareUpdatePayloadInfo
+ _OBJC_METACLASS_$_CBControllerLowPowerModeParams
+ _OBJC_METACLASS_$_CBSoftwareUpdatePayloadInfo
+ _xpc_dictionary_create_empty
- _CBManagerL2CAPChannelInMPS
- _CBManagerL2CAPChannelInMTU
CStrings:
+ "\x02$"
+ "\x11\x11!\x8c!\x17\x12"
+ "\x11!\xa5\x1f\x03\x1b"
+ "### Error writing usecase (%u) event %@"
+ ", %s %@"
+ ", SoftwareUpdatePayloads %@"
+ ", suA %d"
+ ", suD %@"
+ ", suD <%@>"
+ ", suDMs %d"
+ ", xpcReportCompleteDevice %s"
+ "-[CBController setLowPowerModeWithParams:params:completion:]"
+ "-[CBController setLowPowerModeWithParams:params:completion:]_block_invoke"
+ "-[CBDiscovery updateWithXPCSubscriberInfo:]"
+ "177D17F5F0764227B651B5ED28AD502E.chargingcase.fill"
+ "40262ECA475D4CCF9722443885EC78D8"
+ "ActionType: %s, Blob: %@, Mask: %@, Config: 0x%x, DelayStart: %d, ScanW: 0x%x, ScanI: 0x%x, ScanD: %d, NextScan: %d, ClockDrift: %u, RSSI: %d, GPIOAssertTime: %d, dIDSalt: %@, dIDTsFrq: %d, dIDEffectiveBits: %d, dIDTsLsbsTruncated: %d, dIDIKM: %@, dIDInfo: %@, dIDLen: %d, dIDAdvScanCnt: %d, diagTxAdvInt: %d, diagTxAdvDur: %d, diagTxAdvBackoff: %d, dIDDiagInfo: %@, dIDDiagLen: %d, macKeyDiagInfo: %@, macKeyDiagLen: %d"
+ "ActionType: %s, DataBlob: %@, DataMask: %@"
+ "Aliro"
+ "B24@0:8r^*16"
+ "B32@0:8r^*16^Q24"
+ "BTWake"
+ "BTWake: Bluetooth LPM Result :%@"
+ "BTWake: Invalid RSSI %d"
+ "BTWake: Invalid scan Interval %d"
+ "BTWake: Invalid scan Window %d"
+ "CBControllerLowPowerModeParams"
+ "CBDiscovery invalid serviceUUID: “%@”"
+ "CBL2CAPChannel.m"
+ "CBPeripheralManager: handleCSProcedureEventMsg for args %@"
+ "CBSoftwareUpdatePayloadInfo"
+ "Cannot find l2CAP channel closed with psm:%u cid:%u and result:%@"
+ "Cannot find l2CAP channel received Data with psm:%u cid:%u and result:%@"
+ "CriticalBattery"
+ "DCTProtocolDataAndTelephony"
+ "DCTProtocolTelephony"
+ "DiagTxAdv"
+ "Failed to send sendData xpc message, invalid manager set"
+ "Family"
+ "FindMyActionExtendedRange"
+ "FindMyActionExtendedRangeLE2M"
+ "FindMyActionExtendedRangeTransient"
+ "FindMyPlaySoundExtendedRange"
+ "Friend"
+ "HomeRepair"
+ "L2CAP - Error"
+ "L2CAP - Invalid packet size"
+ "MidiV2"
+ "No Params"
+ "No known channel matching peer %@ with cid %u"
+ "No peripheral found in handleCSProcedureEventMsg for args %@"
+ "OutboxControllerAuth"
+ "Power reason %s is not supported"
+ "SameAccount"
+ "SharedHome"
+ "SofrwareUpdateOutboxControllerAuth"
+ "SoftwareUpdate"
+ "SoftwareUpdateBTWake"
+ "SoftwareUpdateOutboxControllerAuth"
+ "SoftwareUpdatePayloads: %@ -> %@"
+ "SystemPaired"
+ "T@\"NSArray\",C,N,V_softwareUpdateDataArray"
+ "T@\"NSArray\",C,N,V_softwareUpdatePayloads"
+ "T@\"NSData\",C,N,V_dataBlob"
+ "T@\"NSData\",C,N,V_dataMask"
+ "T@\"NSData\",C,N,V_deviceIDDiagInfo"
+ "T@\"NSData\",C,N,V_deviceIDInfo"
+ "T@\"NSData\",C,N,V_deviceIDInputKeyMaterial"
+ "T@\"NSData\",C,N,V_deviceIDSalt"
+ "T@\"NSData\",C,N,V_macKeyDiagInfo"
+ "T@\"NSData\",C,N,V_softwareUpdateData"
+ "T@\"NSData\",C,N,V_softwareUpdateDataBlob"
+ "T@\"NSData\",C,N,V_softwareUpdateDataMask"
+ "TB,N,V_isPacketBased"
+ "TB,N,V_xpcReportCompleteDevice"
+ "TC,N,V_aclLinkState"
+ "TC,N,V_actionType"
+ "TC,N,V_deviceIDAdvScanCount"
+ "TC,N,V_deviceIDDiagLength"
+ "TC,N,V_deviceIDLength"
+ "TC,N,V_deviceIDTimestampEffectiveBits"
+ "TC,N,V_deviceIDTimestampFrequency"
+ "TC,N,V_deviceIDTimestampLsbsTruncated"
+ "TC,N,V_diagnosticTxAdvBackoff"
+ "TC,N,V_diagnosticTxAdvDuration"
+ "TC,N,V_macKeyDiagLength"
+ "TC,N,V_packetLength"
+ "TC,N,V_softwareUpdateActionType"
+ "TC,R,N,V_advertisingSoftwareUpdateDataArrayCountMaximumLimit"
+ "TC,R,N,V_softwareUpdateDataArrayCountMaximumLimit"
+ "TI,N,V_maxClockDriftSeconds"
+ "TQ,N,V_authFlags"
+ "TS,N,V_configFlags"
+ "TS,N,V_diagnosticTxAdvInterval"
+ "TS,N,V_gpioAssertionTime"
+ "TS,N,V_nextScanDelay"
+ "TS,N,V_numberOfDelayIterations"
+ "TS,N,V_scanDelayStart"
+ "TS,N,V_scanDuration"
+ "TS,N,V_scanInterval"
+ "TS,N,V_scanWindow"
+ "TS,V_cid"
+ "TS,V_outgoingMTU"
+ "Tc,N,V_rssiThresholdValue"
+ "UserShutDown"
+ "W"
+ "_aclLinkState"
+ "_actionType"
+ "_advertisingSoftwareUpdateDataArrayCountMaximumLimit"
+ "_authFlags"
+ "_cid"
+ "_configFlags"
+ "_dataBlob"
+ "_dataMask"
+ "_deviceIDAdvScanCount"
+ "_deviceIDDiagInfo"
+ "_deviceIDDiagLength"
+ "_deviceIDInfo"
+ "_deviceIDInputKeyMaterial"
+ "_deviceIDLength"
+ "_deviceIDSalt"
+ "_deviceIDTimestampEffectiveBits"
+ "_deviceIDTimestampFrequency"
+ "_deviceIDTimestampLsbsTruncated"
+ "_diagnosticTxAdvBackoff"
+ "_diagnosticTxAdvDuration"
+ "_diagnosticTxAdvInterval"
+ "_gpioAssertionTime"
+ "_isPacketBased"
+ "_macKeyDiagInfo"
+ "_macKeyDiagLength"
+ "_maxClockDriftSeconds"
+ "_nextScanDelay"
+ "_numberOfDelayIterations"
+ "_outgoingMTU"
+ "_packetLength"
+ "_parseProximityPairingBattery1:"
+ "_parseProximityPairingBattery2:"
+ "_parseProximityPairingBattery3:"
+ "_parseProximityPairingColor1:"
+ "_parseProximityPairingMisc1:deviceFlags:"
+ "_parseProximityPairingPID2:"
+ "_parseProximityPairingStatus1:deviceFlags:"
+ "_parseProximityPairingStatus3:deviceFlags:"
+ "_parseSoftwareUpdatePtr:end:"
+ "_rssiThresholdValue"
+ "_scanDelayStart"
+ "_scanDuration"
+ "_scanInterval"
+ "_scanWindow"
+ "_softwareUpdateActionType"
+ "_softwareUpdateData"
+ "_softwareUpdateDataArray"
+ "_softwareUpdateDataArrayCountMaximumLimit"
+ "_softwareUpdateDataBlob"
+ "_softwareUpdateDataMask"
+ "_softwareUpdatePayloads"
+ "_xpcReportCompleteDevice"
+ "aLS"
+ "aSuda"
+ "aclLinkState"
+ "actionType"
+ "advertisingSoftwareUpdateDataArrayCountMaximumLimit"
+ "arrayByAddingObjectsFromArray:"
+ "auFl"
+ "authFlags"
+ "blb"
+ "bleSensorRssiIncreaseScanThreshold: %u -> %u"
+ "configFlags"
+ "createOfflineLEDevices:"
+ "ctND"
+ "ctcf"
+ "ctds"
+ "ctga"
+ "ctns"
+ "ctpl"
+ "ctri"
+ "ctsd"
+ "ctsi"
+ "ctsw"
+ "dIAS"
+ "dIDI"
+ "dIDL"
+ "dIEb"
+ "dIII"
+ "dIIk"
+ "dILT"
+ "dISt"
+ "dITf"
+ "dIdL"
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
+ "dtAB"
+ "dtAD"
+ "dtAI"
+ "gpioAssertionTime"
+ "handleCSProcedureEventMsg:"
+ "handleChannelClosed:"
+ "handleDataReceived:"
+ "handleL2CAPChannelDidReceiveData:"
+ "inParams %@"
+ "incomingPackets"
+ "initWithPeer:manager:info:"
+ "isPacketBased"
+ "kCBCSProcedureCounter"
+ "kCBL2CAPChannelMaxIncomingPayloadSize"
+ "kCBManagerRequiresPacketBasedLEL2CAPInterface"
+ "kCBMsgArgCID"
+ "kCBMsgArgDataLength"
+ "kCBMsgArgMaxQueuedPacketLength"
+ "kCBMsgArgOutMTU"
+ "kCBOptionUseCaseOptions"
+ "kCBScanOptionScanProcessedAtNsec"
+ "kCBScanOptionScanRequestedAtNsec"
+ "l2capChannelForPeer:withCID:"
+ "macKeyDiagInfo"
+ "macKeyDiagLength"
+ "managePendingData"
+ "maxClockDriftSeconds"
+ "maxQueuePayloadSize"
+ "mcds"
+ "mkDI"
+ "mkDL"
+ "msk"
+ "nextScanDelay"
+ "numberOfDelayIterations"
+ "openPacketL2CAPChannel:withIncomingMTU:options:"
+ "outgoingMTU"
+ "packetLength"
+ "pendingCompletionHandler"
+ "peripheral:didCloseL2CAPChannel:"
+ "peripheralManager:didChannelSoundingProcedureEvent:results:error:"
+ "peripheralManager:didCloseL2CAPChannel:"
+ "peripheralManager:l2CapChannel:didReceiveData:"
+ "publishPacketL2CAPChannel:requiresEncryption:withIncomingMTU:options:"
+ "readPacketsWithCompletionHandler:"
+ "reverseObjectEnumerator"
+ "rssiThresholdValue"
+ "scanDelayStart"
+ "scanDuration"
+ "scanInterval"
+ "scanWindow"
+ "sendData:withCompletion:"
+ "serviceUUIDsWithBlobMask"
+ "setAclLinkState:"
+ "setActionType:"
+ "setAuthFlags:"
+ "setCid:"
+ "setConfigFlags:"
+ "setDataBlob:"
+ "setDataMask:"
+ "setDeviceIDAdvScanCount:"
+ "setDeviceIDDiagInfo:"
+ "setDeviceIDDiagLength:"
+ "setDeviceIDInfo:"
+ "setDeviceIDInputKeyMaterial:"
+ "setDeviceIDLength:"
+ "setDeviceIDSalt:"
+ "setDeviceIDTimestampEffectiveBits:"
+ "setDeviceIDTimestampFrequency:"
+ "setDeviceIDTimestampLsbsTruncated:"
+ "setDiagnosticTxAdvBackoff:"
+ "setDiagnosticTxAdvDuration:"
+ "setDiagnosticTxAdvInterval:"
+ "setGpioAssertionTime:"
+ "setIsPacketBased:"
+ "setLowPowerModeWithParams:params:completion:"
+ "setMacKeyDiagInfo:"
+ "setMacKeyDiagLength:"
+ "setMaxClockDriftSeconds:"
+ "setNextScanDelay:"
+ "setNumberOfDelayIterations:"
+ "setOutgoingMTU:"
+ "setPacketLength:"
+ "setRssiThresholdValue:"
+ "setScanDelayStart:"
+ "setScanDuration:"
+ "setScanInterval:"
+ "setScanWindow:"
+ "setSoftwareUpdateActionType:"
+ "setSoftwareUpdateData:"
+ "setSoftwareUpdateDataArray:"
+ "setSoftwareUpdateDataBlob:"
+ "setSoftwareUpdateDataMask:"
+ "setSoftwareUpdatePayloads:"
+ "setXpcReportCompleteDevice:"
+ "softwareUpdateActionType"
+ "softwareUpdateData"
+ "softwareUpdateDataArray"
+ "softwareUpdateDataArrayCountMaximumLimit"
+ "softwareUpdateDataBlob"
+ "softwareUpdateDataMask"
+ "softwareUpdatePayloads"
+ "startAdvertisingForUsecase:withOptions:"
+ "suA"
+ "suA: %d -> %d"
+ "suD: %@ -> %@"
+ "suP"
+ "subarrayWithRange:"
+ "v28@0:8I16@20"
+ "v32@0:8S16S20@24"
+ "v36@0:8S16B20S24@28"
+ "xpcAuthFlagsCreateWithDeviceFlags:"
+ "xpcEventCompleteRepresentation"
+ "xpcReportCompleteDevice"
+ "{?=\"didUpdateName\"b1\"didModifyServices\"b1\"didReadRSSI\"b1\"didUpdateRSSI\"b1\"didDiscoverServices\"b1\"didDiscoverIncludedServices\"b1\"didDiscoverCharacteristics\"b1\"didUpdateCharacteristicValue\"b1\"didWriteCharacteristicValue\"b1\"didNotifyCharacteristicValue\"b1\"didDiscoverDescriptors\"b1\"didUpdateDescriptorValue\"b1\"didWriteDescriptorValue\"b1\"didReceiveTimeSync\"b1\"didOpenL2CAPChannel\"b1\"didCloseL2CAPChannel\"b1}"
+ "{?=\"willRestoreState\"b1\"didAddService\"b1\"didReceiveReadRequest\"b1\"didReceiveWriteRequests\"b1\"centralDidSubscribeToCharacteristic\"b1\"centralDidUnsubscribeFromCharacteristic\"b1\"didStartAdvertising\"b1\"didStartPeriodicAdvertising\"b1\"didStopPeriodicAdvertising\"b1\"isReadyToUpdate\"b1\"centralDidConnect\"b1\"centralDidUpdateConnectionParameters\"b1\"didPublishL2CAPChannel\"b1\"didUnpublishL2CAPChannel\"b1\"didOpenL2CAPChannel\"b1\"didStopAdvertisingWithError\"b1\"didUpdateANCSAuthorization\"b1\"didUpdateControllerBTClock\"b1\"didUpdateControllerBTClockDict\"b1\"didRequestOfflineAdvPayloadRequestedWithReason\"b1\"didChannelSoundingProcedureEvent\"b1\"didCloseL2CAPChannel\"b1\"didReceiveL2CAPData\"b1}"
+ "\xf0\xa4\"\x12/\x02\x1f\b\x11)"
- "\x11\x11!\x8c\x11\x16\x12"
- "\x11!\xa5\x1f\x03\x1a"
- "\x14"
- "### Error writing usecase (%d) event %@"
- "HandleCSProcedureEventMsg:"
- "No peripheral found in HandleCSProcedureEventMsg for args %@"
- "TC,N,V_safetyAlertsAlertIndex"
- "TC,R,N,V_safetyAlertsAlertIndex"
- "_parseStatusOne:deviceFlags:primaryPlacement:secondaryPlacement:"
- "_safetyAlertsAlertIndex"
- "kCBL2CAPChannelInMPS"
- "kCBL2CAPChannelInMTU"
- "kCBOptionUsecase"
- "l2CAP channel closed with psm : %u and result : %@"
- "safetyAlertsAlertIndex"
- "setSafetyAlertsAlertIndex:"
- "v44@0:8C16^Q20^i28^i36"
- "{?=\"didUpdateName\"b1\"didModifyServices\"b1\"didReadRSSI\"b1\"didUpdateRSSI\"b1\"didDiscoverServices\"b1\"didDiscoverIncludedServices\"b1\"didDiscoverCharacteristics\"b1\"didUpdateCharacteristicValue\"b1\"didWriteCharacteristicValue\"b1\"didNotifyCharacteristicValue\"b1\"didDiscoverDescriptors\"b1\"didUpdateDescriptorValue\"b1\"didWriteDescriptorValue\"b1\"didReceiveTimeSync\"b1\"didOpenL2CAPChannel\"b1}"
- "{?=\"willRestoreState\"b1\"didAddService\"b1\"didReceiveReadRequest\"b1\"didReceiveWriteRequests\"b1\"centralDidSubscribeToCharacteristic\"b1\"centralDidUnsubscribeFromCharacteristic\"b1\"didStartAdvertising\"b1\"didStartPeriodicAdvertising\"b1\"didStopPeriodicAdvertising\"b1\"isReadyToUpdate\"b1\"centralDidConnect\"b1\"centralDidUpdateConnectionParameters\"b1\"didPublishL2CAPChannel\"b1\"didUnpublishL2CAPChannel\"b1\"didOpenL2CAPChannel\"b1\"didStopAdvertisingWithError\"b1\"didUpdateANCSAuthorization\"b1\"didUpdateControllerBTClock\"b1\"didUpdateControllerBTClockDict\"b1\"didRequestOfflineAdvPayloadRequestedWithReason\"b1}"
- "\xf0\xa4\"\x12/\x02\x1f\a\x11)"

```
