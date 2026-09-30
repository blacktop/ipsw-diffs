## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.2.0.0
-  __TEXT.__text: 0xaaccc
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x2360
+64.0.3.0.0
+  __TEXT.__text: 0xaae34
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__objc_stubs: 0x2340
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2f0
-  __TEXT.__const: 0x8427
-  __TEXT.__gcc_except_tab: 0xa2f4
-  __TEXT.__cstring: 0x4351
-  __TEXT.__oslogstring: 0x25136
+  __TEXT.__const: 0x842f
+  __TEXT.__gcc_except_tab: 0xa2e4
+  __TEXT.__cstring: 0x4346
+  __TEXT.__oslogstring: 0x2518d
   __TEXT.__objc_classname: 0x1b7
-  __TEXT.__objc_methname: 0x28c7
+  __TEXT.__objc_methname: 0x28b0
   __TEXT.__objc_methtype: 0x111e
-  __TEXT.__unwind_info: 0x3388
-  __DATA_CONST.__auth_got: 0x760
+  __TEXT.__unwind_info: 0x3398
+  __DATA_CONST.__auth_got: 0x758
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x6bd8
-  __DATA_CONST.__cfstring: 0x47e0
+  __DATA_CONST.__cfstring: 0x47c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x1828
-  __DATA.__objc_selrefs: 0x988
+  __DATA.__objc_selrefs: 0x980
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2735
-  Symbols:   392
+  Functions: 2736
+  Symbols:   391
   CStrings:  3037
 
Symbols:
- _objc_retain_x14
CStrings:
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,onFirstUnlock,isBLERelaySupported\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#saEventHistory,onFirstUnlock\", \"history\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#brm,onBleAlertReceived\", \"nowSeconds\":\"%!{(MISSING)public}0.7f\", \"bleAdvertiseTime\":\"%!{(MISSING)public}0.7f\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"brm,submitMetrics\", \"isBleAdvertiser\":%!{(MISSING)private}hhd, \"wasSAReceived\":%!{(MISSING)private}hhd, \"batteryChargeLevel\":%!{(MISSING)private}d, \"bleRelayFanOutSetting\":%!{(MISSING)private}d, \"meanNumNearbyDevices\":%!{(MISSING)private}d, \"bleRelayAdvertiseDuration\":%!{(MISSING)private}d, \"bleReceivedRSSI\":%!{(MISSING)private}d, \"bleReceivedRSSIBucketed\":%!{(MISSING)private}d, \"bleLatencyRelativeToSATime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToBleAdvertiseTime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToOriginatorTime\":\"%!{(MISSING)private}0.2f\", \"alertUID\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"deviceRole\":%!{(MISSING)private, location:escape_only}s, \"pushInterface\":%!{(MISSING)private, location:escape_only}s, \"source\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb\", \"Index\":%!{(MISSING)private}d}"
- "alertIndex"
- "{\"msg%!{(MISSING)public}.0s\":\"#brm,onBleAlertReceived\", \"nowSeconds\":\"%!{(MISSING)public}0.7f\", \"igneousAlertInformation.bleAdvertiseTime\":\"%!{(MISSING)public}0.7f\"}"
- "safetyAlertsAlertIndex"
- "{\"msg%!{(MISSING)public}.0s\":\"brm,submitMetrics\", \"isBleAdvertiser\":%!{(MISSING)private}hhd, \"wasSAReceived\":%!{(MISSING)private}hhd, \"batteryChargeLevel\":%!{(MISSING)private}d, \"bleRelayFanOutSetting\":%!{(MISSING)private}d, \"meanNumNearbyDevices\":%!{(MISSING)private}d, \"bleRelayAdvertiseDuration\":%!{(MISSING)private}d, \"alertIndex\":%!{(MISSING)private}d, \"bleReceivedRSSI\":%!{(MISSING)private}d, \"bleReceivedRSSIBucketed\":%!{(MISSING)private}d, \"bleLatencyRelativeToSATime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToBleAdvertiseTime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToOriginatorTime\":\"%!{(MISSING)private}0.2f\", \"alertUID\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"deviceRole\":%!{(MISSING)private, location:escape_only}s, \"pushInterface\":%!{(MISSING)private, location:escape_only}s, \"source\":%!{(MISSING)private, location:escape_only}s}"

```
