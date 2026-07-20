## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0x223e0
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0xa80
+60.0.0.0.0
+  __TEXT.__text: 0x24494
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_stubs: 0xae0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x324
-  __TEXT.__gcc_except_tab: 0x2660
+  __TEXT.__gcc_except_tab: 0x2bcc
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x5cad
+  __TEXT.__cstring: 0x65a3
   __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methname: 0xbd8
-  __TEXT.__objc_methtype: 0x65d
+  __TEXT.__objc_methname: 0xc12
+  __TEXT.__objc_methtype: 0x6c9
+  __TEXT.__ustring: 0x14a
   __TEXT.__oslogstring: 0x9c4
-  __TEXT.__unwind_info: 0x790
+  __TEXT.__unwind_info: 0x7c0
   __DATA_CONST.__const: 0x578
-  __DATA_CONST.__cfstring: 0x3d60
+  __DATA_CONST.__cfstring: 0x4aa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__auth_got: 0x428
+  __DATA_CONST.__got: 0x358
   __DATA.__objc_const: 0x678
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_selrefs: 0x3c8
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 486
-  Symbols:   417
-  CStrings:  961
+  Functions: 490
+  Symbols:   423
+  CStrings:  1070
 
Symbols:
+ _CFDictionaryGetTypeID
+ _OBJC_CLASS_$_NSProcessInfo
+ __Z20getCurrentIOSVersionv
+ __ZN17DeviceCMInterface19getDiagnosticReportEPU15__autoreleasingP12NSDictionary
+ __ZN17DeviceCMInterface20getAntliaFaultStatusEPy
+ __ZN17DeviceCMInterface28getProjectorCalibratedValuesEPU15__autoreleasingP12NSDictionary
CStrings:
+ "%.1f"
+ "0x%02X"
+ "0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X"
+ "ANTLIA: ProjectorAntliaFaultStatus read OK (raw 0x%016llX)"
+ "ANTLIA: ProjectorAntliaFaultStatus unavailable (IOReturn 0x%x) — using placeholder"
+ "ANTLIA: ProjectorCalibratedValues read OK (%lu keys)"
+ "ANTLIA: ProjectorCalibratedValues unavailable (IOReturn 0x%x) — using placeholder"
+ "ANTLIA_VALUES"
+ "Antlia State [0x1B]"
+ "BIST_FAULTS"
+ "BRICK_REASON"
+ "Bist_FLT_Status_Reg_0"
+ "Bist_FLT_Status_Reg_1"
+ "Bist_FLT_Status_Reg_2"
+ "Bist_FLT_Status_Reg_3"
+ "Brick_Reason"
+ "Brick_Reason0"
+ "Brick_Reason1"
+ "CalibratedValues_MaxCurrentsNVM"
+ "CalibratedValues_MaxCurrentsOTP"
+ "CalibratedValues_MaxPulseWidthNVM"
+ "CalibratedValues_OTPVersion"
+ "CalibratedValues_PearlVersion"
+ "CalibratedValues_ProjectorBuild"
+ "DECODED"
+ "DIETemperatureActive"
+ "DIETemperatureIdle"
+ "DIETemperatureStandby"
+ "DiagnosticReport"
+ "FAULT_HISTORY"
+ "FAULT_STATUS"
+ "FSM_ARMED"
+ "FSM_Armed"
+ "FSM_BRICKED"
+ "FSM_Bricked"
+ "FSM_FAULT"
+ "FSM_STATE"
+ "FSM_STATE_RAW"
+ "FSM_State"
+ "FSM_VALUES"
+ "Fault Status [0x51..0x56]"
+ "Fault_History_Status_Reg_00"
+ "Fault_History_Status_Reg_01"
+ "Fault_History_Status_Reg_02"
+ "Fault_History_Status_Reg_03"
+ "Fault_History_Status_Reg_04"
+ "Fault_History_Status_Reg_10"
+ "Fault_History_Status_Reg_11"
+ "Fault_History_Status_Reg_12"
+ "Fault_History_Status_Reg_13"
+ "Fault_History_Status_Reg_14"
+ "Fault_History_Status_Reg_20"
+ "Fault_History_Status_Reg_21"
+ "Fault_History_Status_Reg_22"
+ "Fault_History_Status_Reg_23"
+ "Fault_History_Status_Reg_24"
+ "HARD"
+ "IOS_VERSION"
+ "Level_0"
+ "Level_1"
+ "Level_2"
+ "MAX_CURRENTS_NVM"
+ "MAX_CURRENTS_OTP"
+ "MAX_PULSE_WIDTH_NVM"
+ "Mirage_Diagnostics"
+ "NONE"
+ "NTCTemperatureActive"
+ "NTCTemperatureIdle"
+ "NTCTemperatureStandby"
+ "OTP_VERSION"
+ "PEARL_VERSION"
+ "PROJECTOR_BUILD"
+ "PROJECTOR_RESISTANCE_DELTA"
+ "PROJECTOR_RESISTANCE_NVM"
+ "PROJECTOR_RESISTANCE_STATE"
+ "PROJECTOR_TEMPERATURE"
+ "Pending driver support (rdar://178980394)"
+ "ProjectorAntliaFaultStatus"
+ "ProjectorCalibratedValues"
+ "REASON_0"
+ "REASON_1"
+ "RTRACE_LAST"
+ "Resistance"
+ "Resistance-State"
+ "Resistance_Delta"
+ "Resistance_Last"
+ "Resistance_NVM"
+ "Rtrace_Last"
+ "SILICON_REV"
+ "SOFT"
+ "Silicon_Rev"
+ "UNKNOWN"
+ "Valid"
+ "activeDIE"
+ "activeNTC"
+ "getAntliaFaultStatus failed with OSStatus 0x%x for stream id %d (%@)"
+ "getAntliaFaultStatus failed, ir stream id invalid"
+ "getDiagnosticReport failed with OSStatus 0x%x for stream id %d (%@)"
+ "getDiagnosticReport failed, ir stream id invalid"
+ "getDiagnosticReport returned unexpected CF type (not a dictionary) for stream id %d"
+ "getProjectorCalibratedValues failed with OSStatus 0x%x for stream id %d (%@)"
+ "getProjectorCalibratedValues failed, ir stream id invalid"
+ "idleDIE"
+ "idleNTC"
+ "operatingSystemVersionString"
+ "processInfo"
+ "standbyDIE"
+ "standbyNTC"
+ "unsignedIntValue"
+ "{PearlDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_gmcResult\"@\"NSNumber\"\"m_gmcPointCount\"@\"NSNumber\"\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i\"deviceName\"@\"NSString\"}\"m_rgbPearlFramesCount\"i\"m_isPearlRgbFramesArrived\"B\"m_isPearlIrFramesArrived\"B\"m_irPearlFramesCount\"i\"m_ntcIdle\"f\"m_ntcActive\"f\"m_ntcStandby\"f\"m_dieIdle\"f\"m_dieActive\"f\"m_dieStandby\"f\"m_isTemperatureDetected\"B}"
- "{PearlDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_gmcResult\"@\"NSNumber\"\"m_gmcPointCount\"@\"NSNumber\"\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i\"deviceName\"@\"NSString\"}\"m_rgbPearlFramesCount\"i\"m_isPearlRgbFramesArrived\"B\"m_isPearlIrFramesArrived\"B\"m_irPearlFramesCount\"i}"
```
