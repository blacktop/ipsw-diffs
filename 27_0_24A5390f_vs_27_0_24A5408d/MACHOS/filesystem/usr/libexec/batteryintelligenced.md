## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-218.0.0.0.0
-  __TEXT.__text: 0x42004
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x4940
-  __TEXT.__objc_methlist: 0x317c
-  __TEXT.__cstring: 0x354b
-  __TEXT.__objc_classname: 0x855
-  __TEXT.__objc_methname: 0x643c
-  __TEXT.__objc_methtype: 0x1537
-  __TEXT.__const: 0x338
-  __TEXT.__oslogstring: 0x7a54
-  __TEXT.__gcc_except_tab: 0x340
-  __TEXT.__unwind_info: 0xc78
-  __DATA_CONST.__const: 0xcf8
-  __DATA_CONST.__cfstring: 0x3b60
-  __DATA_CONST.__objc_classlist: 0x200
+222.0.1.0.0
+  __TEXT.__text: 0x488d0
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_stubs: 0x5460
+  __TEXT.__objc_methlist: 0x3854
+  __TEXT.__cstring: 0x3986
+  __TEXT.__objc_classname: 0x8f6
+  __TEXT.__objc_methname: 0x70ca
+  __TEXT.__objc_methtype: 0x1601
+  __TEXT.__const: 0x3a0
+  __TEXT.__oslogstring: 0x8e23
+  __TEXT.__gcc_except_tab: 0x38c
+  __TEXT.__unwind_info: 0xdb8
+  __DATA_CONST.__const: 0xd40
+  __DATA_CONST.__cfstring: 0x4380
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0xd70
-  __DATA_CONST.__objc_arrayobj: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_arraydata: 0xef8
+  __DATA_CONST.__objc_arrayobj: 0x5e8
   __DATA_CONST.__objc_intobj: 0xf00
-  __DATA_CONST.__objc_doubleobj: 0x70
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x550
-  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__objc_doubleobj: 0xd0
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__auth_got: 0x598
+  __DATA_CONST.__got: 0x358
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x7a50
-  __DATA.__objc_selrefs: 0x17a8
-  __DATA.__objc_ivar: 0x338
-  __DATA.__objc_data: 0x1400
+  __DATA.__objc_const: 0x84f0
+  __DATA.__objc_selrefs: 0x1b00
+  __DATA.__objc_ivar: 0x3c8
+  __DATA.__objc_data: 0x1590
   __DATA.__data: 0x528
-  __DATA.__bss: 0x248
+  __DATA.__bss: 0x270
+  - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AccelerateOpt.framework/AccelerateOpt
   - /System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms
   - /System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader
+  - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI
   - /System/Library/PrivateFrameworks/Trial.framework/Trial

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1499
-  Symbols:   272
-  CStrings:  2440
+  Functions: 1695
+  Symbols:   283
+  CStrings:  2773
 
Symbols:
+ _AddIpoptIntOption
+ _CFPreferencesCopyValue
+ _CreateIpoptProblem
+ _FreeIpoptProblem
+ _IpoptSolve
+ _OBJC_CLASS_$_CLPCInternalInterface
+ ___assert_rtn
+ _dispatch_walltime
+ _kCFPreferencesAnyHost
+ _malloc_type_calloc
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "!iRow && !jCol"
+ "@\"<CLPCInternalAccess>\""
+ "@\"BIATVTable\""
+ "@88@0:8d16d24d32d40d48d56d64d72d80"
+ "ATV lookup: BTVI/BTTI unavailable — falling back to range-breakpoint lookup at V=%.0fmV T=%.1f"
+ "ATV lookup: firmware indices BTVI=%@/BTTI=%@ out of table range — falling back to range-breakpoint lookup"
+ "ATV table lookup returned invalid value, falling back to deviceMaxCRate=%.2f"
+ "ATV-table"
+ "Action_CRate"
+ "Action_PackagePower"
+ "Actuators reset: package power budget and c-rate limit released."
+ "Adapter-limited ceiling: adapter capability unavailable — keeping ceiling %.2fC"
+ "Adapter-limited ceiling: ceiling=%.2fC adapterW=%.1f -> capability=%.2fC => applied=%.2fC"
+ "Ambient temp override cleared — using default %.1f°C"
+ "Ambient temp override set to %.1f°C via internal settings"
+ "AppleChargerData"
+ "B0AC"
+ "B0TI"
+ "B0TI readback after write: %@ mA (wrote %u mA), B0AC actual: %@ mA"
+ "B20@0:8f16"
+ "B28@0:8@16B24"
+ "BIATVTable"
+ "BTRA"
+ "BTRB"
+ "BTRS"
+ "BTTA"
+ "BTTC"
+ "BTTI"
+ "BTVA"
+ "BTVC"
+ "BTVI"
+ "Battery temp unavailable for ATV lookup, falling back to deviceMaxCRate=%.2f"
+ "CLPCInternalInterface %s: Sent target = %.2fW"
+ "CLTM disabled via internal settings (MSAL=0, xCFT=0)"
+ "CLTM re-enabled via internal settings (MSAL=0x%02X)"
+ "C_thDevice"
+ "Charge current paused (status=%@) — clamping c-rate ceiling to %.2fC."
+ "ChargerData"
+ "Could not load battery_analysis_tt80_model_bwatrvswhe.mlmodelc in the bundle resource"
+ "CreateIpoptProblem failed, using conservative policy"
+ "Cth"
+ "CurrentAmbientTemp"
+ "CurrentCRate"
+ "CurrentDisplayPower"
+ "CurrentInstantCRate"
+ "CurrentSysLoad"
+ "D23"
+ "D47"
+ "D48"
+ "D93"
+ "D94"
+ "Defaults updated: alphaPackageP=%.3f, alphaCRate=%.3f, maxTemp=%.1f°C, timerInterval=%.1fs, R_th=%.3f, C_th=%.3f"
+ "Display power %f W from SMC key %@ is out of reasonable range"
+ "Display power unavailable, treating as 0W for thermal model"
+ "Error reading battery amperage (%@) from ASBM. Returning kInvalidDataValue %ld"
+ "Error reading battery virtual temp from ASBM. Returning kInvalidDataValue %ld"
+ "Error reading battery voltage from ASBM. Returning kInvalidDataValue %ld"
+ "FAILED"
+ "FF: ThermalControl %s"
+ "Failed to write charge current limit (%u mA) to SMC key %@"
+ "IPOPT optimization failed (status=%d), using conservative policy"
+ "IPOPT solved (status=%d): obj=%.4f, max_temp=%.2f°C, final_temp=%.2f°C"
+ "Index"
+ "Loaded thermal params for device=%@ tvKey=%@: R=%.3f C=%.3f etaPkg=%.3f etaBatt=%.3f etaDisplay=%.3f"
+ "MPC iteration: temp=%.2f°C, battTemp=%.2f°C, voltage=%.3fV, ncc=%.0fmAh, cRateCeiling=%.2fC, displayPower=%.3fW, sysLoad=%.3fW, alpha_packageP=%.2f, alpha_crate=%.2f"
+ "MPC result: obj=%.3f, applying sys=%.2fW, c-rate=%.2fC, max predicted temp=%.2f°C"
+ "MPC_Schedule"
+ "MPC_State"
+ "MSAL"
+ "NCC unavailable or invalid from ASBM. Returning kInvalidDataValue %ld"
+ "One or more invalid values read (temp=%.2f, voltage=%.3fV, ncc=%.0fmAh), skipping iteration"
+ "Optimization result: packagePSchedule = %@, cRateSchedule =  %@"
+ "Over temperature (%.2f°C > %.2f°C + %.2f margin), using conservative policy"
+ "PerformanceControlKitInternal unavailable on this device (%@) — thermal control not supported; not starting loop"
+ "Power adapter attached — starting thermal control loop."
+ "Power adapter detached — stopping thermal control loop and releasing actuator constraints."
+ "Power telemetry data unavailable, using default system load %.1fW"
+ "R_thDevice"
+ "Read display power from SMC: %f W"
+ "Rth"
+ "SDTL"
+ "Set charge current limit: %u mA (%.2fC × %.0f mAh NCC)"
+ "Starting thermal control loop."
+ "Starting thermal model evaluation."
+ "System load (%s) missing or invalid, using default %.1fW"
+ "T@\"<CLPCInternalAccess>\",&,N,V_clpcClient"
+ "T@\"BIATVTable\",&,N,V_cachedATVTable"
+ "T@\"BIATVTable\",R,N"
+ "T@\"NSArray\",R,N,V_rawRates"
+ "T@\"NSArray\",R,N,V_temperaturesRaw"
+ "T@\"NSArray\",R,N,V_voltagesMV"
+ "T@\"NSDate\",&,N,V_controlStartTime"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
+ "T@\"NSString\",C,N,V_virtualTempKey"
+ "TB,N,V_cltmDisabled"
+ "TB,N,V_controlLoopActive"
+ "TB,N,V_enabled"
+ "TB,N,V_isDemoDevice"
+ "TB,N,V_unsupported"
+ "TQ,R,N,V_scaleFactor"
+ "Td,N,V_C_th"
+ "Td,N,V_C_thDevice"
+ "Td,N,V_R_th"
+ "Td,N,V_R_thDevice"
+ "Td,N,V_alphaCRate"
+ "Td,N,V_alphaPackageP"
+ "Td,N,V_deviceMaxCRate"
+ "Td,N,V_etaBatt"
+ "Td,N,V_etaDisplay"
+ "Td,N,V_etaPackage"
+ "Td,N,V_maxTemp"
+ "Td,N,V_overrideAmbientTemp"
+ "Td,N,V_timerInterval"
+ "Thermal control did not start (disabled or unsupported) — falling back to thermal model evaluation."
+ "Thermal control disabled via internal settings — control loop stopped and actuators reset."
+ "Thermal control is disabled via internal settings — skipping startControl."
+ "Thermal control re-enabled via internal settings — control restarted"
+ "ThermalControl"
+ "ThermalControlManager"
+ "ThermalControlManager.m"
+ "Ti,N,V_iconToken"
+ "Ti,N,V_monitorToken"
+ "Ti,N,V_notifyToken"
+ "Unable to load battery/charging data for system load, using default %.1fW"
+ "Unable to read SMC key %@ for display power"
+ "Unable to read battery amperage or NCC, cannot compute c-rate"
+ "Unable to read battery instant amperage or NCC, cannot compute c-rate"
+ "Unable to read virtual temp (%@) from SMC"
+ "Using override ambient temp: %.1f°C"
+ "V53"
+ "V54"
+ "V57"
+ "V59"
+ "V62"
+ "V63"
+ "V64"
+ "V67"
+ "V68"
+ "V69"
+ "Virtual battery temp %.2f°C from ASBM is out of range"
+ "Virtual temp %.2f°C from %@ is out of range"
+ "Virtual temp key (%@) unavailable on this device (%@) — thermal control not supported; not starting loop"
+ "_C_th"
+ "_C_thDevice"
+ "_R_th"
+ "_R_thDevice"
+ "_alphaCRate"
+ "_alphaPackageP"
+ "_cachedATVTable"
+ "_clpcClient"
+ "_cltmDisabled"
+ "_controlLoopActive"
+ "_controlStartTime"
+ "_deviceMaxCRate"
+ "_enabled"
+ "_etaBatt"
+ "_etaDisplay"
+ "_etaPackage"
+ "_iconToken"
+ "_isDemoDevice"
+ "_maxTemp"
+ "_monitorToken"
+ "_notifyToken"
+ "_overrideAmbientTemp"
+ "_rawRates"
+ "_scaleFactor"
+ "_temperaturesRaw"
+ "_timer"
+ "_timerInterval"
+ "_unsupported"
+ "_virtualTempKey"
+ "_voltagesMV"
+ "adapter"
+ "adapterLimitedMaxCRate:voltageV:nccMah:"
+ "alphaCRate"
+ "alphaPackageP"
+ "ambientTemperatureC"
+ "appendData:"
+ "applyCLTMDisabled:"
+ "applyUpdatedDefaults"
+ "applyUpdatedDefaults: received settings change notification"
+ "applyUpdatedDefaults: thermal control unsupported on this device — ignoring"
+ "atvTable"
+ "atvTable: failed to fetch ATV table from SMC. Will be unable to compute accurate c-rate schedules"
+ "batteryAmperageMa"
+ "batteryAmperageMaForKey:"
+ "batteryInstantAmperageMa"
+ "batteryTemperatureC"
+ "batteryVoltageV"
+ "battery_analysis_tt80_model_bwatrvswhe"
+ "battery_analysis_tt80_model_bwatrvswheInput"
+ "battery_analysis_tt80_model_bwatrvswheOutput"
+ "bwatrvswhe"
+ "bytes"
+ "c-rate ceiling: ATV-table=%.2fC -> adapter=%.2fC => applied=%.2fC (binding=%@)"
+ "cRateForVoltageIndex:temperatureIndex:"
+ "cRateForVoltageMV:temperatureRaw:"
+ "cRateFromATVTableForVoltageV:temperatureC:"
+ "cRateSchedule"
+ "cachedATVTable"
+ "chargerLossesFromCRate:voltageV:nccMah:pSysIn:"
+ "clpcClient"
+ "cltmDisabled"
+ "com.apple.batteryintelligenced.thermalcontrol"
+ "com.apple.batteryintelligenced.thermalcontrol.changed"
+ "com.apple.batteryintelligenced.thermalcontrolmanager.queue"
+ "conservativePolicyFromTemp:"
+ "controlLoopActive"
+ "controlStartTime"
+ "createClient:"
+ "currentCRate"
+ "currentInstantCRate"
+ "currentTemperatureC"
+ "currentTemperatureCForKey:"
+ "d32@0:8@16d24"
+ "d32@0:8Q16Q24"
+ "d32@0:8d16d24"
+ "d40@0:8d16d24d32"
+ "deviceMaxCRate"
+ "displayPowerW"
+ "enabled"
+ "etaBatt"
+ "etaDisplay"
+ "etaPackage"
+ "eta_display"
+ "fetchATVTable"
+ "fetchATVTable: BTRA truncated and BTRB unavailable"
+ "fetchATVTable: appended %u bytes from BTRB"
+ "fetchATVTable: failed to read BTVA/BTTA/BTRA"
+ "fetchATVTable: failed to read BTVC/BTTC/BTRS"
+ "fetchATVTable: invalid dimensions or scale (voltCount=%lu, tempCount=%lu, scale=%lu)"
+ "fetchATVTable: loaded %lu×%lu table (scale=%lu) from SMC"
+ "finalTemp"
+ "g\x91"
+ "handleChargeStateChange"
+ "iRow && jCol"
+ "iconToken"
+ "initForTesting"
+ "initWithVoltagesMV:temperaturesRaw:rawRates:scaleFactor:"
+ "insert == thermal_hess_nz_count(T)"
+ "insert == thermal_jac_nz_count(T)"
+ "isActivelyCharging"
+ "isCLPCAvailable"
+ "isDemoDevice"
+ "isPluggedIn"
+ "maxTemp"
+ "maxTempReached"
+ "mobile"
+ "monitorToken"
+ "nil"
+ "nominalChargeCapacityMah"
+ "notifyToken"
+ "numberWithUnsignedChar:"
+ "objectiveValue"
+ "optimizeScheduleFromTemp:voltageV:nccMah:ambientTemp:displayPowerW:alphaPackageP:alphaCRate:maxCRate:maxPackagePower:"
+ "overrideAmbientTemp"
+ "packagePSchedule"
+ "print_level"
+ "rawRates"
+ "readBoolPreference:defaultValue:"
+ "readDoublePreference:defaultValue:"
+ "recordMPCScheduleForCRate:packagePower:"
+ "recordMPCStateForTemp:ambientTemp:currentSysLoad:currentDisplayPower:currentCRate:currentInstantCRate:actionPkgPower:actionCRate:"
+ "registerTimer"
+ "resetActuators"
+ "runControlLoop"
+ "runControlLoop: PerformanceControlKitInternal unavailable — stopping thermal control."
+ "runControlLoop: adapter detached — skipping iteration."
+ "scaleFactor"
+ "setAlphaCRate:"
+ "setAlphaPackageP:"
+ "setCRateLimit:"
+ "setCRateLimit: NCC unavailable, cannot convert c-rate to current"
+ "setC_th:"
+ "setC_thDevice:"
+ "setCachedATVTable:"
+ "setClpcClient:"
+ "setCltmDisabled:"
+ "setControlLoopActive:"
+ "setControlStartTime:"
+ "setDeviceMaxCRate:"
+ "setEnabled:"
+ "setEtaBatt:"
+ "setEtaDisplay:"
+ "setEtaPackage:"
+ "setIconToken:"
+ "setIsDemoDevice:"
+ "setMaxTemp:"
+ "setMonitorToken:"
+ "setNotifyToken:"
+ "setOverrideAmbientTemp:"
+ "setPackagePowerBudgetWatts:"
+ "setPackagePowerViaCLPC:"
+ "setPackagePowerViaCLPC: PerformanceControlKitInternal unavailable — skipping"
+ "setPackagePowerViaCLPC: createClient failed: %@"
+ "setPackagePowerViaCLPC: opened CLPCInternalInterface client"
+ "setPackagePowerViaCLPC: setPowerBudget failed: %@"
+ "setPowerBudget:forReason:withTimescale:error:"
+ "setR_th:"
+ "setR_thDevice:"
+ "setTimer:"
+ "setTimerInterval:"
+ "setUnsupported:"
+ "setVirtualTempKey:"
+ "startControl"
+ "startControl: failed to register for charging iconography notification (%d)."
+ "startTemp"
+ "startTimerLoop"
+ "stopControl"
+ "stopTimerLoop"
+ "succeeded"
+ "systemLoadW"
+ "temperaturesRaw"
+ "thermal-control-manager"
+ "thermalCLTMDisabled"
+ "thermalControlAlphaCRate"
+ "thermalControlAlphaPackageP"
+ "thermalControlAmbientTempOverride"
+ "thermalControlEnabled"
+ "thermalControlMaxTemp"
+ "thermalControlTimerInterval"
+ "thermal_jac_constraints"
+ "thermal_lag_hessian"
+ "timer"
+ "timerInterval"
+ "unknown"
+ "unregisterTimer"
+ "unsignedIntegerValue"
+ "unsupported"
+ "v20@0:8i16"
+ "v80@0:8d16d24d32d40d48d56d64d72"
+ "virtualTempKey"
+ "voltagesMV"
+ "xCFT"
+ "xDPE after setting via CLPC: %.3fW (target %.2fW)"
- "Read %u bytes from SMC key %@"
- "Read SMC key %@: %@"
```
