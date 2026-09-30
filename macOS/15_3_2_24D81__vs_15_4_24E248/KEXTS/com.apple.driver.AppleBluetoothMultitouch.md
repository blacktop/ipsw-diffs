## com.apple.driver.AppleBluetoothMultitouch

> `com.apple.driver.AppleBluetoothMultitouch`

```diff

 103.0.0.0.0
   __TEXT.__cstring: 0x1efe
   __TEXT.__const: 0xe
-  __TEXT_EXEC.__text: 0x7c8c
+  __TEXT_EXEC.__text: 0x7cc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x3ec8
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 02A3574E-A9B8-31B7-95A1-D303DF0AD6DC
-  Functions: 172
-  Symbols:   669
+  UUID: 13804FA0-5195-3D4D-B54D-6775F209E868
+  Functions: 170
+  Symbols:   668
   CStrings:  130
 
Symbols:
- _ZN9BNBDevice20_setMultitouchReportEhPhj.cold.1
Functions:
~ __ZN28BluetoothMultitouchTransport4freeEv : 364 -> 388
~ __ZN28BluetoothMultitouchTransport20multitouchPropertiesEv : 1300 -> 1360
~ __ZN28BluetoothMultitouchTransport15startMultitouchEv : 404 -> 412
~ __ZN28BluetoothMultitouchTransport23startMultitouchThreadedEv : 1292 -> 1312
~ __ZN28BluetoothMultitouchTransport19postMultitouchFrameEPhj : 188 -> 184
~ __ZN28BluetoothMultitouchTransport20desyncIncomingMTDataEPhj : 280 -> 300
~ __ZN17BNBTrackpadDevice20processInterruptDataEPht : 1460 -> 1468
~ __ZN14BNBMouseDevice20processInterruptDataEPht : 1872 -> 1868
~ __ZN14BNBMouseDevice19_multitouchDidStartEv : 460 -> 464
~ __ZN14BNBMouseDevice21repairTraceResistanceEv : 420 -> 432
~ __ZN9BNBDevice11handleStartEP9IOService : 524 -> 520
~ __ZN9BNBDevice4freeEv : 180 -> 184
~ __ZN9BNBDevice21processIncomingMTDataEPhj : 2320 -> 2300
- sub_fffffe00095be0f0
~ __ZN9BNBDevice24_getMultitouchReportInfoEhPhPj : 480 -> 468
~ __ZN9BNBDevice20_getMultitouchReportEhPhPj : 880 -> 868
~ __ZN9BNBDevice20_setMultitouchReportEhPhj : 724 -> 712
~ __ZN9BNBDevice16_simpleGetReportEhPhj : 672 -> 676
~ __ZN9BNBDevice16_simpleSetReportEhPhj : 672 -> 676
~ __ZN9BNBDevice17getExtendedReportEPKc : 2212 -> 2200

```
