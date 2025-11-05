## com.apple.driver.AppleSPU

> `com.apple.driver.AppleSPU`

```diff

-1014.60.6.0.0
-  __TEXT.__cstring: 0x4b22
-  __TEXT.__os_log: 0x868
-  __TEXT.__const: 0x258
-  __TEXT_EXEC.__text: 0x42944
+1014.100.12.0.0
+  __TEXT.__cstring: 0x4b0f
+  __TEXT.__os_log: 0x871
+  __TEXT.__const: 0x280
+  __TEXT_EXEC.__text: 0x41948
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x848
   __DATA.__common: 0x8a8

   __DATA_CONST.__const: 0x1faf0
   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: A33EFF49-0242-3354-B904-2586A12B54C7
-  Functions: 1878
-  Symbols:   3020
-  CStrings:  837
+  UUID: 4DA3E021-209C-3390-9A7B-2FAE70138410
+  Functions: 1986
+  Symbols:   3223
+  CStrings:  836
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZN15AppleSPUControl12_toggleResetEv.cold.1
+ _ZN15AppleSPUControl14TryToggleResetEv.cold.1
+ _ZN15RemoteDataQueue12_dequeue_oneEjPhmj.cold.1
+ _ZN17AppleSPUHIDDriver11handleStartEP9IOService.cold.1
+ _ZN17AppleSPUHIDDriver13openForClientEP9IOServicejP12OSDictionaryPPv.cold.1
+ _ZN17AppleSPUHIDDriver13openForClientEP9IOServicejP12OSDictionaryPPv.cold.2
+ _ZN17AppleSPUHIDDriver13openForClientEP9IOServicejP12OSDictionaryPPv.cold.3
+ _ZN17AppleSPUInterface16_handleSubPacketEP13_AOPSubPacket.cold.1
+ _ZN17AppleSPUInterface23_spuPerformCommandGatedE13SpuPacketTypePKhmPNS_15_command_ParamsE.cold.1
+ _ZN18AppleSPUUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN20AppleSPUWakeProfiler11handleEventEPK8OSSymboljPvj.cold.1
+ _ZN21AppleSPUDispADCDriver15stopMeasurementEPP6OSData.cold.1
+ _ZN21AppleSPUDispADCDriver15stopMeasurementEPP6OSData.cold.2
+ _ZN21AppleSPUDispADCDriver15stopMeasurementEPP6OSData.cold.3
+ _ZN21AppleSPUDispADCDriver19_stopRawStreamGatedEP17IOSharedDataQueue.cold.1
+ _ZN21AppleSPUDispADCDriver20_startRawStreamGatedEP17IOSharedDataQueue.cold.1
+ _ZN22AppleSPUMarconiControl19_setPowerStateGatedEmP9IOService.cold.1
+ _ZN25AppleSPUDispADCUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN27AppleSPUAppDriverUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN27AppleSPUHIDDeviceUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN27AppleSPUHIDDeviceUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.2
+ _ZN27AppleSPUHIDDriverUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN28AppleSPUGNSSDriverUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN28AppleSPUHapticsManagerDriver12latencyCheckEP30HapticsManagerPlayAssetRequest.cold.1
+ _ZN29AppleSPUBattChannelUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN31AppleSPUProfileDriverUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN32AppleSPUFastpathDriverUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN32AppleSPUHapticsManagerUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN32AppleSPUHapticsManagerUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.2
+ _ZN8AppleSPU13_asyncMessageEPvS0_.cold.10
+ _ZN8AppleSPU13_asyncMessageEPvS0_.cold.11
+ _ZN8AppleSPU13_asyncMessageEPvS0_.cold.7
+ _ZN8AppleSPU13_asyncMessageEPvS0_.cold.8
+ _ZN8AppleSPU13_asyncMessageEPvS0_.cold.9
+ _ZN8AppleSPU18setPowerStateGatedEmP9IOService.cold.1
+ _ZN8AppleSPU18setPowerStateGatedEmP9IOService.cold.2
+ _ZN8AppleSPU18setPowerStateGatedEmP9IOService.cold.3
+ _ZN8AppleSPU27_handleHistoricalQueueGatedEPvS0_.cold.1
- _ZN17AppleSPUInterface25_spuGetNamedPropertyGatedEPNS_23_GetNamedPropertyParamsE.cold.1
- _ZN17AppleSPUInterface25_spuSetNamedPropertyGatedEPNS_23_SetNamedPropertyParamsE.cold.1
- _ZN17AppleSPUInterface25_spuSetNamedPropertyGatedEPNS_23_SetNamedPropertyParamsE.cold.2
- _ZN17AppleSPUInterface31_spuPerformCommandInternalGatedE13SpuPacketTypebPKhmPhPmjb.cold.1
- _ZN18AppleSPUGNSSDriver18handleReportPacketEjyPKhmj.cold.1
- _ZN19AppleSPUCalibration17setAllCalibrationEP17AppleSPUHIDDriverP17AppleSPUInterface.cold.1
- _ZN23AppleSPUFirmwareService23updatePatchbayVariablesEP15RTBuddyFirmware.cold.2
- _ZN23AppleSPURemoteCrashdump12startCaptureEv.cold.1
- __ZL41iop_streaming_ringbuffer_write_client_logP28iop_streaming_ringbuffer_refjhhyyy
CStrings:
+ "Dropped gnss data report due to missing data queue %zu"
+ "Dropped gnss data report queue is full(%zu)"
+ "Dropped gnss event due to missing data queue %zu"
+ "Dropped gnss event due to oversized packet: %zu"
+ "Dropped gnss event for queue error: %#x (%zu)"
+ "Tried to override key %s but failed with: 0x%x\n"
- "Dropped gnss data report due to missing data queue (%zu)"
- "Dropped gnss data report for queue (%zu)"
- "Dropped gnss event due to missing data queue (%zu)"
- "Dropped gnss event due to oversized packet (%zu)"
- "Dropped gnss event for queue (%zu)"
- "Tried to override key %s but failed with: 0x%x"
- "compass-calibration"

```
