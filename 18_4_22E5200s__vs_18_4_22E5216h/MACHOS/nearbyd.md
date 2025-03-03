## nearbyd

> `/usr/libexec/nearbyd`

```diff

-465.0.14.0.0
-  __TEXT.__text: 0x446c0c
+465.0.16.0.0
+  __TEXT.__text: 0x449064
   __TEXT.__auth_stubs: 0x28b0
-  __TEXT.__objc_stubs: 0x11b80
+  __TEXT.__objc_stubs: 0x11be0
   __TEXT.__init_offsets: 0x614
-  __TEXT.__objc_methlist: 0xbf84
-  __TEXT.__gcc_except_tab: 0x49b78
-  __TEXT.__const: 0x2d6820
-  __TEXT.__cstring: 0x31cae
-  __TEXT.__objc_methname: 0x1b4fa
-  __TEXT.__oslogstring: 0x50600
-  __TEXT.__objc_classname: 0x18d2
-  __TEXT.__objc_methtype: 0x1cb16
+  __TEXT.__objc_methlist: 0xc08c
+  __TEXT.__gcc_except_tab: 0x49e64
+  __TEXT.__const: 0x2d6910
+  __TEXT.__cstring: 0x3269a
+  __TEXT.__objc_methname: 0x1b728
+  __TEXT.__oslogstring: 0x50a20
+  __TEXT.__objc_classname: 0x18e5
+  __TEXT.__objc_methtype: 0x1cb83
   __TEXT.__swift5_typeref: 0x7d
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x88
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x17c48
+  __TEXT.__unwind_info: 0x17d48
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1470
   __DATA_CONST.__got: 0x9c0
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x20510
-  __DATA_CONST.__cfstring: 0x124e0
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __DATA_CONST.__const: 0x20660
+  __DATA_CONST.__cfstring: 0x12ac0
+  __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x468
   __DATA_CONST.__objc_arraydata: 0x3b0
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_intobj: 0x5b8
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x14ad0
-  __DATA.__objc_selrefs: 0x5708
-  __DATA.__objc_ivar: 0x13e4
-  __DATA.__objc_data: 0x3038
+  __DATA.__objc_const: 0x14cf8
+  __DATA.__objc_selrefs: 0x5750
+  __DATA.__objc_ivar: 0x1400
+  __DATA.__objc_data: 0x3088
   __DATA.__data: 0x30c4
   __DATA.__bss: 0xca20
   __DATA.__common: 0xcc0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19103
+  Functions: 19159
   Symbols:   998
-  CStrings:  17146
+  CStrings:  17251
 
CStrings:
+ "#roseprovider,#aop-sf-zone-update: btConnHandle = 0x%04x (%u), zone: %s, RSSI: %d, displacing: %d, explicitPAI: %d, SFinBubble: %d"
+ "#roseprovider,Got RoseState Event: ChipUnavailable, Reason: %s"
+ "#ses-acwg,ACWG session destroyed when receiving AopSFZoneUpdate"
+ "#ses-acwg,AopSFZoneUpdate: update.btConnHandle = 0x%04x (%u)"
+ "#ses-home,Not to re-pause session to handle UWB state change since its already in progress."
+ "#ses-home,Not to re-reun session to handle UWB state change since its not needed."
+ "#ttr,Configuring test capability"
+ "#ttr,Event %@ only presented once per erase install. It's already been presented, now disable it"
+ "#ttr,Previously disabled TTR alerts for event %@"
+ "-[NIServerAcwgSession didReceiveAopSFZoneUpdate:]"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "1.) Are you experiencing issues with UWB features like Precision Finding or Digital Car Key?\n2.) Are you experiencing issues with OTA software updates?"
+ "@44@0:8q16S24c28B32B36B40"
+ "Could not get currently allowed RF channels"
+ "Failed to read RoseServiceState value from the dictionary"
+ "Failed to read SecureROMStatus value from the dictionary or isn't a CFNumbertype"
+ "Invalid specified RF channel %d"
+ "MaxChipResets"
+ "NIAcwgSFZoneUpdate"
+ "Nearby Interaction test TTR 1"
+ "Nearby Interaction test TTR 2"
+ "Nearby Interaction test TTR1"
+ "Nearby Interaction test TTR2"
+ "PRRose: Can't get boot UUID to persist crash"
+ "PRRose: Handling unrecoverable error %s. Current boot already crashed on %s, so don't crash again"
+ "PRRose: Resetting chip. Previous counter: %d"
+ "PRRose: Unable to power off Rose after an unrecoverable error"
+ "PRRose: crash on unrecoverable error %s"
+ "PRRose: current boot crashed on %s. Setting state to UNAVAILABLE"
+ "PRRose::errorHandlingRoutine : failed to reset chip. Set to UNAVAILABLE state"
+ "PRRoseUnrecoverableErrorBootUUID"
+ "PRRoseUnrecoverableErrorDate"
+ "PRRoseUnrecoverableErrorReason"
+ "PowerState"
+ "RF channel %d not allowed"
+ "RoseController Debug Info: PowerState: %d, ServiceState: %d, SecureROMState: %d"
+ "RosePowerOn"
+ "RosePowerOnFailure"
+ "RosePowerState isn't present in the dictionary or isn't a CFNumbertype"
+ "RoseServiceState"
+ "RoseServiceState isn't present in the dictionary or isn't a CFNumbertype"
+ "SecureROMState"
+ "SecureROMStatus"
+ "SecureROMStatus isn't present in the dictionary"
+ "ServiceState"
+ "Simulate boot error to test reset chip abort."
+ "TB,R,N,V_currentSFInBubble"
+ "TB,R,N,V_explicitPAITriggered"
+ "TB,R,N,V_ioStateDisplacing"
+ "TS,R,N,V_btConnHandle"
+ "Tc,R,N,V_lastBtRssiValue"
+ "Test1"
+ "Test2"
+ "TestResetChipAbort"
+ "Testing TTR 1"
+ "Testing TTR 2"
+ "Tq,R,N,V_currentZone"
+ "Ultra Wideband chip issue"
+ "Unable to obtain debug info"
+ "Unrecoverable error: Max chip resets (activate AOP time sync failure)"
+ "Unrecoverable error: Max chip resets (apply config params CIR version failure)"
+ "Unrecoverable error: Max chip resets (apply config params send power table failure)"
+ "Unrecoverable error: Max chip resets (apply config params set MAC address failure)"
+ "Unrecoverable error: Max chip resets (apply config params update coex status failure)"
+ "Unrecoverable error: Max chip resets (cal data push failure)"
+ "Unrecoverable error: Max chip resets (configure sleep failure)"
+ "Unrecoverable error: Max chip resets (disable logs failure)"
+ "Unrecoverable error: Max chip resets (ext clock setting failure)"
+ "Unrecoverable error: Max chip resets (ping FW failure)"
+ "Unrecoverable error: Max chip resets (push FW failure)"
+ "Unrecoverable error: Max chip resets (time sync enable failure)"
+ "Unrecoverable error: Max chip resets (unspecified failure)"
+ "Unrecoverable error: Unable to power on Rose"
+ "UnrecoverableChipError"
+ "[Internal only] Test TTR 1"
+ "[Internal only] Test TTR 2"
+ "[Internal only] UWB chip failed to power on."
+ "[Internal only] UWB chip has reset the maximum number of times."
+ "[Internal only] UWB max chip reset"
+ "[Internal only] UWB power on failure"
+ "_btConnHandle"
+ "_currentSFInBubble"
+ "_currentZone"
+ "_explicitPAITriggered"
+ "_ioStateDisplacing"
+ "_lastBtRssiValue"
+ "_pendingRerunSessionWhenUWBStateUpddate"
+ "btConnHandle"
+ "btConnHandle:(0x%04x)\n"
+ "c16@0:8"
+ "com.apple.nearbyd.RoseResetFailed"
+ "com.apple.nearbyd.TapToRadarTest.1"
+ "com.apple.nearbyd.TapToRadarTest.2"
+ "currentSFInBubble"
+ "currentSFInBubble:%d>\n"
+ "currentZone"
+ "currentZone:%@\n"
+ "didReceiveAopSFZoneUpdate:"
+ "explicitPAITriggered"
+ "explicitPAITriggered:%d\n"
+ "initWithSFZone:btConnHandle:lastBtRssiValue:ioStateDisplacing:explicitPAITriggered:currentSFInBubble:"
+ "ioStateDisplacing"
+ "ioStateDisplacing:%d\n"
+ "lastBtRssiValue"
+ "lastBtRssiValue:%d\n"
+ "session:didReceiveAopSFZoneUpdate:"
+ "v16@?0r^{RoseSupervisorReport=d{RoseSupervisorReportPacket=I(?={AOPRoseGenericResponse={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}}{AOPRoseGenericEvent={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}}{AOPRoseHelloResponseV1={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=[32C]SSC{?=SS[16C]SCI}})}}{AOPRoseHelloResponseV2={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=S[32C]SS{?=SS[16C]SCI}I[39C]})}}{AOPRoseMeasurement=CSQ(?={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCQSCSissssi(?=SSS)SssSIcccssQCSSSCsssC[5C][5C][5C][5C][10C]})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCQSCSissssi(?=SSS)SssSIcccssQCSSS(?=S{?=b11b5})sssCs(?={?=CC[2C]}{?=CC(?=S{?=b11b5})})CssssCCCCCC[8C]})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCCSQQSCCQQssSssIcccssCssCssiCSSSsss[16C]})})}{AOPRoseRangeResultDebugEvent=CS(?={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCSCSQQQQQQSS[2[3{?=ss}]]Q})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCSQI[7C][5C][5C][5C][5C][20C]})})}{AOPRoseCIRDataEvent={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}Q}{AOPRoseAOACIRDataEvent=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=CSS[3C]I[8I][8I][8I]})}}{AOPRoseTOACIRDataEvent=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=CSSCSI[8I]})}}{AOPRoseError=SSqqqBSBi}{AOPRoseStatusUpdate=SCCq}{AOPRoseCoexEventData={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}Q}{AOPRoseSuperframeCompleteEvent=CSQ[128C]}{AOPRoseSPMIMessage=[64C]Q}{AOPRosePowerStatsResponse={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}{?=IIIIIIIIISSIIIIIIII}}}{AOPRoseControlReport=C}{AOPRoseSessionStartReport=CSS}{AOPRoseSessionDataReport=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCCSQQ[16C]C[0C]})}}{AOPRoseSessionSubratingUpdate=SSCCi{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSSCC})}}{AOPRoseAlishaCapabilities={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SC[10S]CIC{?=(?=C{?=b5b3})}C[10C][32C]})}}{AOPRoseAlishaKey=C(?={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SI})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCCIQQQSSIII})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCCIQQQSSIII})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SI})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=S[1I][40C]})})}{AOPRoseRangingBlockCompleteEvent=CSiS[128C]}{AOPRoseAlishaRangeResponse=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SS})}Q}{AOPRoseAlishaSessionStats=CSCS[7S]Sss}{AOPRoseActivitySummaryPart1=QC[26{AOPRoseJobInfo=SCB}]B{AOPRoseSchedulerCoreInfo=(?=C{?=b1})CCCCCCCCC}}{AOPRoseTimeConversionResult=CCQQ}{AOPRoseTimeConversionState=C}{AOPRoseLPEMEnableResponse={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}{?=S}}}{AOPRoseTOACIRDataV2Event=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=C[2C]CSS[2{?=CSSI[9C][8I]}]})}}{AOPRoseDeepSleepStateReport=CCB}{AOPRoseBtConnRssiReport=QSc}{AOPRoseDisplacementReport=Q[3f][3f]QQ[3Q]Q[4f]fC}{AOPRoseSensorFusionUpdate=iS}{AOPRoseBtConnRssiFilterInit=S{ConnectionRSSIKalmanFilterParams=dddddcc}}{AOPExtendedReport=S(?={AOPRoseBtConnRssiFilterStateReport=QS{ConnectionRSSIKalmanFilterState=ddQBBB}}{AOPRoseActivitySummaryPart2={AOPRoseSFManagerCoreInfo=(?=C{?=b1b1b1})CQQQSc}[8{AOPRoseSFManagerConnectionInfo=(?=C{?=b1b1b1})SQcCCC}]}{AOPRoseBtConnRssiFilterThresholdUpdate=QSdd}{AOPRoseAcwgRangeDataEvent=SiCS[128C]}{AOPRoseSFZoneUpdate=Scb2b1b1b1b3})})}}8"
+ "v20@0:8{AOPRoseSFZoneUpdate=Scb2b1b1b1b3}16"
+ "v24@0:8@\"NIAcwgSFZoneUpdate\"16"
- "#roseprovider,Got RoseState Event: RegulatoryDisallow, Reason: %s"
- "#ttr,User previously disabled TTR alerts for event %@"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "FatalStartUpError"
- "PRRose: Resetting chip."
- "Unable to power on R1"
- "Unable to power on Rose"
- "fResetCounter exceeded kMaxChipResets (%d)"
- "v16@?0r^{RoseSupervisorReport=d{RoseSupervisorReportPacket=I(?={AOPRoseGenericResponse={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}}{AOPRoseGenericEvent={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}}{AOPRoseHelloResponseV1={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=[32C]SSC{?=SS[16C]SCI}})}}{AOPRoseHelloResponseV2={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=S[32C]SS{?=SS[16C]SCI}I[39C]})}}{AOPRoseMeasurement=CSQ(?={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCQSCSissssi(?=SSS)SssSIcccssQCSSSCsssC[5C][5C][5C][5C][10C]})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCQSCSissssi(?=SSS)SssSIcccssQCSSS(?=S{?=b11b5})sssCs(?={?=CC[2C]}{?=CC(?=S{?=b11b5})})CssssCCCCCC[8C]})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCCSQQSCCQQssSssIcccssCssCssiCSSSsss[16C]})})}{AOPRoseRangeResultDebugEvent=CS(?={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCSCSQQQQQQSS[2[3{?=ss}]]Q})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCSQI[7C][5C][5C][5C][5C][20C]})})}{AOPRoseCIRDataEvent={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}Q}{AOPRoseAOACIRDataEvent=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=CSS[3C]I[8I][8I][8I]})}}{AOPRoseTOACIRDataEvent=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=CSSCSI[8I]})}}{AOPRoseError=SSqqqBSBi}{AOPRoseStatusUpdate=SCCq}{AOPRoseCoexEventData={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[108C])}Q}{AOPRoseSuperframeCompleteEvent=CSQ[128C]}{AOPRoseSPMIMessage=[64C]Q}{AOPRosePowerStatsResponse={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}{?=IIIIIIIIISSIIIIIIII}}}{AOPRoseControlReport=C}{AOPRoseSessionStartReport=CSS}{AOPRoseSessionDataReport=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSCCSQQ[16C]C[0C]})}}{AOPRoseSessionSubratingUpdate=SSCCi{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SSSCC})}}{AOPRoseAlishaCapabilities={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SC[10S]CIC{?=(?=C{?=b5b3})}C[10C][32C]})}}{AOPRoseAlishaKey=C(?={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SI})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCCIQQQSSIII})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SCCIQQQSSIII})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SI})}{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=S[1I][40C]})})}{AOPRoseRangingBlockCompleteEvent=CSiS[128C]}{AOPRoseAlishaRangeResponse=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=SS})}Q}{AOPRoseAlishaSessionStats=CSCS[7S]Sss}{AOPRoseActivitySummaryPart1=QC[26{AOPRoseJobInfo=SCB}]B{AOPRoseSchedulerCoreInfo=(?=C{?=b1})CCCCCCCCC}}{AOPRoseTimeConversionResult=CCQQ}{AOPRoseTimeConversionState=C}{AOPRoseLPEMEnableResponse={?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}{?=S}}}{AOPRoseTOACIRDataV2Event=S{?={?=SCCCSSCSI}{?=(?=I(?={?=b16}{?=b10b4b2b1b2b13}))}(?=[0C]{?=C[2C]CSS[2{?=CSSI[9C][8I]}]})}}{AOPRoseDeepSleepStateReport=CCB}{AOPRoseBtConnRssiReport=QSc}{AOPRoseDisplacementReport=Q[3f][3f]QQ[3Q]Q[4f]fC}{AOPRoseSensorFusionUpdate=iS}{AOPRoseBtConnRssiFilterInit=S{ConnectionRSSIKalmanFilterParams=dddddcc}}{AOPExtendedReport=S(?={AOPRoseBtConnRssiFilterStateReport=QS{ConnectionRSSIKalmanFilterState=ddQBBB}}{AOPRoseActivitySummaryPart2={AOPRoseSFManagerCoreInfo=(?=C{?=b1b1b1})CQQQSc}[8{AOPRoseSFManagerConnectionInfo=(?=C{?=b1b1b1})SQcCCC}]}{AOPRoseBtConnRssiFilterThresholdUpdate=QSdd}{AOPRoseAcwgRangeDataEvent=SiCS[128C]})})}}8"

```
