## HealthAlgorithms

> `/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms`

```diff

-131.0.0.0.0
-  __TEXT.__text: 0x3f790
+132.0.0.0.0
+  __TEXT.__text: 0x3f9e4
   __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x11dc
-  __TEXT.__const: 0xb7c9
-  __TEXT.__cstring: 0x1567
-  __TEXT.__oslogstring: 0x356
-  __TEXT.__gcc_except_tab: 0x4210
-  __TEXT.__unwind_info: 0x1328
+  __TEXT.__const: 0xb899
+  __TEXT.__cstring: 0x1604
+  __TEXT.__oslogstring: 0x3a7
+  __TEXT.__gcc_except_tab: 0x4214
+  __TEXT.__unwind_info: 0x1330
   __TEXT.__objc_classname: 0x380
   __TEXT.__objc_methname: 0x37db
   __TEXT.__objc_methtype: 0xda8

   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x300
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BADED4F-5016-3652-9552-DD4287F54FD5
-  Functions: 1227
-  Symbols:   3618
-  CStrings:  1061
+  UUID: 66F410AC-E19D-31B3-91FC-868EBEB7AEF5
+  Functions: 1230
+  Symbols:   3624
+  CStrings:  1066
 
Symbols:
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table128
+ __Z21get_ppg_processor_logv
+ __ZN17health_algorithms12PPGProcessor14make_processorERKNS0_11RawPPGDatumEN7hal900010GenerationEb.cold.12
+ __ZN17health_algorithms12PPGProcessor20compute_accel_outputERKNSt3__17variantIJN6mimosa8PacketV1ENS3_8PacketV2ENS3_8PacketV3ENS3_8PacketV4ENS3_8PacketV5ENS3_8PacketV6ENS3_8PacketV7ENS3_8PacketV8ENS3_8PacketV9ENS3_9PacketV10ENS3_9PacketV11ENS3_9PacketV12EEEE.cold.1
+ __ZZ21get_ppg_processor_logvE3log
- GCC_except_table112
- GCC_except_table119
CStrings:
+ "Backwards jump in timestamp detected, dropping sample with time: %lld prev: %lld"
+ "PPGProcessor"
+ "cal_led != Sunstone2p5OpticalLedIdx::S2P5_INVALID"
+ "led < static_cast<uint8_t>(OpticalTransmitIndex::SIZE)"
+ "led < to_underlying(OpticalTransmitIndex::SIZE)"
+ "sunstone2p5_led_to_idx"
- "led < mimosa::OpRTv1::led_count"

```
