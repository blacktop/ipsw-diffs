## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

-13.0.28.0.0
-  __TEXT.__const: 0x460
-  __TEXT.__cstring: 0x219e
-  __TEXT.__os_log: 0x8081
-  __TEXT_EXEC.__text: 0x2b5e4
+13.0.31.0.0
+  __TEXT.__const: 0x470
+  __TEXT.__cstring: 0x21c6
+  __TEXT.__os_log: 0x83d1
+  __TEXT_EXEC.__text: 0x2bac0
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x268

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x5558
   __DATA_CONST.__kalloc_type: 0x800
-  UUID: 212DDB10-CC80-3E8D-8D1D-1F58F67C42D3
-  Functions: 889
-  Symbols:   1987
-  CStrings:  569
+  UUID: 8CBC31D1-CD14-3A41-AECF-55FEFE288C10
+  Functions: 890
+  Symbols:   1993
+  CStrings:  576
 
Symbols:
+ _OUTLINED_FUNCTION_33
+ __ZN16PSVR2SenseDevice21handleInputReportDataEyyPK19PSVR2SenseInputDataNS_9CRCResultE
+ __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_691
+ __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_877
+ __ZZN16PSVR2SenseDevice26handleBluetoothInputReportEyyjPvmE11_os_log_fmt_0
+ __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__21_
+ __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__22_
+ __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__23_
+ __ZZN16PSVR2SenseDevice26handleInputDataForTimesyncEPK19PSVR2SenseInputDataR18InputReportContextE11_os_log_fmt__24_
+ __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1080
+ __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1294
+ __ZZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEEUb7_E20kalloc_type_view_866
+ __ZZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEEUb9_E21kalloc_type_view_1281
+ __block_descriptor_tmp.103
+ __block_descriptor_tmp.109
+ __block_descriptor_tmp.127
+ __block_descriptor_tmp.133
+ __block_descriptor_tmp.94
- __ZN16PSVR2SenseDevice21handleInputReportDataEyyPK19PSVR2SenseInputData
- __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_689
- __ZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEE20kalloc_type_view_875
- __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1078
- __ZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEE21kalloc_type_view_1292
- __ZZZN16PSVR2SenseDevice19refreshFirmwareInfoEybU13block_pointerFviEEUb7_E20kalloc_type_view_864
- __ZZZN16PSVR2SenseDevice27refreshMotionCorrectionDataEybU13block_pointerFviEEUb9_E21kalloc_type_view_1279
- __block_descriptor_tmp.126
- __block_descriptor_tmp.132
- __block_descriptor_tmp.91
CStrings:
+ "Input.NormalizedThumbstickMaxzoneRadius"
+ "[%#010llx] \t invalidChecksum = %d"
+ "[%#010llx] #ACCESSORY Unexpected sequence number delta between input reports %llu -> %llu{\n\t deviceSequenceNumber: %llu -> %llu\n\t reportTimestampHost: %llu -> %llu\n\t receiveTimestamp3US: %llu -> %llu\n\t driverTimestamp3US: %llu -> %llu\n\t deviceTimestamp3US: %llu -> %llu\n}"
+ "[%#010llx] #TIMESYNC Detected suspicious timestamp delta between input reports %llu -> %llu{\n\t deviceSequenceNumber: %llu -> %llu\n\t reportTimestampHost: %llu -> %llu\n\t reportTimestamp3US: %llu -> %llu\n\t receiveTimestamp3US: %llu -> %llu (%d)\n\t driverTimestamp3US: %llu -> %llu (%d)\n\t deviceTimestamp3US: %llu -> %llu (%d)\n\t deviceMotionTimestamp3US: %llu -> %llu (%d)\n}"
+ "[%#010llx] #TRANSPORT Time synchronization state changed: %d -> %d"
+ "[%#010llx] Input report %#0.2x payload [%#0.2x] (%zu bytes) has invalid checksum '%#0.8x'; expected '%#0.8x'."
+ "[%#010llx] Input report %#0.2x payload has length (%zu bytes), which is less than the minimum expected length (%zu bytes). Ignoring."

```
