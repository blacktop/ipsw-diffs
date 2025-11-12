## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

-13.2.7.0.0
-  __TEXT.__const: 0x470
-  __TEXT.__cstring: 0x21c6
-  __TEXT.__os_log: 0x845c
-  __TEXT_EXEC.__text: 0x2bd80
+13.2.8.0.0
+  __TEXT.__const: 0x480
+  __TEXT.__cstring: 0x21ec
+  __TEXT.__os_log: 0x85e6
+  __TEXT_EXEC.__text: 0x2c294
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x268

   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x5558
+  __DATA_CONST.__const: 0x5578
   __DATA_CONST.__kalloc_type: 0x800
-  UUID: 389A766C-A387-34A8-95C4-D1E278D5F0C8
-  Functions: 889
+  UUID: 50E295AC-37FB-3308-ADFF-423B7FDE93C6
+  Functions: 891
   Symbols:   1993
-  CStrings:  577
+  CStrings:  576
 
Symbols:
+ _OUTLINED_FUNCTION_33
+ __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_693
+ __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_879
+ __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1082
+ __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1296
+ __ZZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEEUb7_E20kalloc_type_view_868
+ __ZZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEEUb9_E21kalloc_type_view_1283
+ __ZZZN40PSVR2SenseDeviceHIDEventServerUserClient22applyHapticsPropertiesEP12OSDictionaryS1_EUb22_E11_os_log_fmt
+ __ZZZN40PSVR2SenseDeviceHIDEventServerUserClient23applyTrackingPropertiesEP12OSDictionaryS1_EUb21_E11_os_log_fmt
+ ____ZN40PSVR2SenseDeviceHIDEventServerUserClient23applyTrackingPropertiesEP12OSDictionaryS1__block_invoke_6
+ ___copy_helper_block_8_32r40r48r56r64r72r80r88r
+ ___destroy_helper_block_8_32r40r48r56r64r72r80r88r
+ __block_descriptor_tmp.126
- __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_691
- __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_877
- __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__22_
- __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__23_
- __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__24_
- __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1080
- __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1294
- __ZZN16PSVR2SenseDevice28prepareOutputDataForTrackingEP20PSVR2SenseOutputDataR19OutputReportContextE11_os_log_fmt_9
- __ZZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEEUb7_E20kalloc_type_view_866
- __ZZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEEUb9_E21kalloc_type_view_1281
- __ZZZN40PSVR2SenseDeviceHIDEventServerUserClient22applyHapticsPropertiesEP12OSDictionaryS1_EUb21_E11_os_log_fmt
- ___copy_helper_block_8_32r40r48r56r64r72r80r
- ___destroy_helper_block_8_32r40r48r56r64r72r80r
- __block_descriptor_tmp.122
- __block_descriptor_tmp.133
CStrings:
+ "Tracking.RequiredModificationInterval"
+ "[%#010llx] \t receiveTimestamp = {host:%llu, 3us:%llu}"
+ "[%#010llx] #TIMESYNC NEW CONVERSION (AVG / %u) {\n\t isTransportTimeSynchronized = %d,\n\t hostToDeviceTimestampConversion = (3US: %lli) ~ (3US: %lli),\n\t deviceToHostTimestampConversion = (3US: %lli) ~ (3US: %lli),\n}"
+ "[%#010llx] > (TRACKING) Check [%llu] (isLastApplied: %d) TX:{host:%llu, us:%llu} > EntryEmissionTime:{host:%llu, us:%llu} -> %d"
+ "[%#010llx] > (TRACKING) Check should force Tracking update for modification interval {\n\t transmissionTimestamp = %lluus\n\t lastModificationTime = %lluus\n\t requiredModificationInterval = %uus\n\t modification delta = %lluus\n} -> %d"
+ "[%#010llx] > (TRACKING) Check should skip for compatible current parameters {\n\t deviceEmissionTime = %lluus -> %lluus ~ %lluus,\n\t deviceEmissionLength = %uus -> %uus,\n\t deviceCyclePeriod = %uus -> %uus,\n\t emissionTimeOffset = %lluus,\n\t emissionTimeOffsetInCurrentCycles = %llu,\n\t exposureWindowLength = %uus,\n\t exposureWindow = [%lluus, %lluus] (%lluus),\n\t accumulatedDrift = %lluus,\n\t uncertainty = %lluus,\n\t next1PredictedEmissionTime = [%lluus, %lluus] ~> [%lluus, %lluus] (%lluus),\n\t next2PredictedEmissionEndTime = [%lluus, %lluus] ~> [%lluus, %lluus]  (%lluus),\n}"
+ "[%#010llx] > (TRACKING) Check should skip update for modification interval {\n\t transmissionTimestamp = %lluus\n\t lastModificationTime = %lluus\n\t minimumModificationInterval = %uus\n\t modification delta = %lluus\n} -> %d"
+ "[%#010llx] > (TRACKING) New parameters from queue [%llu] {\n\t entryEmissionTime = {host:%llu, 3us:%llu, us:%llu} %c%c {host:%llu, 3us:%llu, us:%llu}\n\t hostToDeviceTimestampConversion = {3us:%lli}\n\t computed device emissionTime = {3us:%u}\n}"
+ "[%#010llx] > (TRACKING) PROCEED WITH UPDATE (emission length change)"
+ "[%#010llx] > (TRACKING) PROCEED WITH UPDATE (existing pulse outside target emission window)"
+ "[%#010llx] > (TRACKING) PROCEED WITH UPDATE (mode change)"
+ "[%#010llx] > (TRACKING) Queue read failed: %#x"
+ "[%#010llx] > (TRACKING) SKIP"
+ "[%#010llx] Apply 'Tracking' override {\n\tTracking.RequiredModificationInterval = %u\n}"
- "[%#010llx] \t receiveTimestamp3US = %llu"
- "[%#010llx] \t receiveTimestampHost = %llu"
- "[%#010llx] (AVG) deviceToHostTimestampConversion3US = %lli / %u"
- "[%#010llx] (AVG) hostToDeviceTimestampConversion3US = %lli / %u"
- "[%#010llx] (AVG) isTransportTimeSynchronized = %d / %u"
- "[%#010llx] >\t PROCEED WITH UPDATE"
- "[%#010llx] >\t PROCEED WITH UPDATE (emission length change)"
- "[%#010llx] >\t PROCEED WITH UPDATE (existing pulse outside target emission window)"
- "[%#010llx] >\t PROCEED WITH UPDATE (mode change)"
- "[%#010llx] >\t SKIP"
- "[%#010llx] > (TRACKING) Check [%llu] (isLastApplied: %d) txHost:%llu > entryEmissionTimeHost:%llu -> %d"
- "[%#010llx] > (TRACKING) Check should skip Tracking update for modification interval {\n\t outputTimeUS = %lluus\n\t lastModificationTimeUS = %lluus\n\t minimumModificationIntervalUS = %uus\n\t modification delta = %lluus\n}"
- "[%#010llx] > (TRACKING) Check should skip for compatible current parameters {\n\t currentCyclePeriod3US = %uus\n\t currentEmissionLength3US = %uus\n\t currentEmissionTime3US = %lluus\n\t newCyclePeriod3US = %uus\n\t newEmissionLength3US = %uus\n\t newEmissionTime3US = %lluus\n\t emissionTimeOffset3US = %lluus\n\t emissionTimeOffsetInCurrentCycles = %llu\n\t exposureWindowLength3US = %uus\n\t exposureWindow3US = [%lluus, %lluus)]\n\t next1PredictedEmissionTime3US = [%lluus, %lluus]\n\t next2PredictedEmissionEndTime3US = [%lluus, %lluus]\n}"
- "[%#010llx] > (TRACKING) New parameters from queue [%llu] {\n\t entryEmissionTimeHost = %llu %c%c %llu\n\t entryEmissionTime3US = %llu %c%c %llu\n\t hostToDeviceTimestampConversion3US = %lli\n\t computed device emissionTime3US = %u\n}"
- "[%#010llx] > (TRACKING) Queue read failed: %x"

```
