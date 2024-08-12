## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1725.0.0.0.0
-  __TEXT.__text: 0x139e34
+1727.2.0.0.0
+  __TEXT.__text: 0x13a3cc
   __TEXT.__auth_stubs: 0x2260
-  __TEXT.__objc_stubs: 0x1bda0
+  __TEXT.__objc_stubs: 0x1be20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xe284
-  __TEXT.__objc_methname: 0x2b3a3
-  __TEXT.__cstring: 0x48631
+  __TEXT.__objc_methlist: 0xe2ac
+  __TEXT.__objc_methname: 0x2b3e8
+  __TEXT.__cstring: 0x487d7
   __TEXT.__objc_classname: 0xddc
-  __TEXT.__objc_methtype: 0x75d7
+  __TEXT.__objc_methtype: 0x75dd
   __TEXT.__gcc_except_tab: 0x4990
   __TEXT.__const: 0x1f9c8
   __TEXT.__dlopen_cstrs: 0x376
-  __TEXT.__oslogstring: 0x85
+  __TEXT.__oslogstring: 0x90
   __TEXT.__info_plist: 0x5af
-  __TEXT.__unwind_info: 0x4160
+  __TEXT.__unwind_info: 0x4170
   __DATA_CONST.__auth_got: 0x1148
   __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x47c0
-  __DATA_CONST.__cfstring: 0x28a80
+  __DATA_CONST.__cfstring: 0x28b40
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x6eb8
   __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x18628
-  __DATA.__objc_selrefs: 0x80f0
+  __DATA.__objc_const: 0x18648
+  __DATA.__objc_selrefs: 0x8108
   __DATA.__objc_ivar: 0x1904
   __DATA.__objc_data: 0x28a0
   __DATA.__data: 0x5c8
   __DATA.__common: 0x168
-  __DATA.__bss: 0x468
+  __DATA.__bss: 0x470
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6537
+  Functions: 6540
   Symbols:   776
-  CStrings:  13984
+  CStrings:  13995
 
CStrings:
+ "%!{(MISSING)public}@"
+ "Don't send RCU1Message - No change in WiFi/BT state WiFiPower = (%!d(MISSING)) WiFiband = (%!d(MISSING)) btPower = (%!d(MISSING)) btBand= (%!d(MISSING))force = [%!d(MISSING)]"
+ "Failed to send message to BT about low 5G Rates:"
+ "PolicyManager: WiFi 5G is not connected, allow AoS in 5GHz"
+ "PolicyManager: WiFi 5G rates dropped, moved any AoS to 2G"
+ "PolicyManager: WiFi 5G rates recovered and no AoS link, allow AoS 5GHz"
+ "PolicyManager: WiFi 5G rates recovered, keep AoS in 2G"
+ "PolicyManager: handleLow5GRate %!d(MISSING)"
+ "PolicyManager: rates are high and 5G AoS is connected, keep 5G TDD active"
+ "Sent message to BT about low 5G Rates: %!d(MISSING)"
+ "WiFiController Low5GRate Check cureRate: %!d(MISSING) Prev1Rate: %!d(MISSING) Prev2Rate: %!d(MISSING)"
+ "WiFiController TxRate: %!d(MISSING) RxRate: %!d(MISSING) and BW: %!d(MISSING) "
+ "WiFiS: weightedWiFiAvgLQM RSSI: %!d(MISSING) SNR: %!d(MISSING) TX Rate: %!d(MISSING) Rx Rate: %!d(MISSING)"
+ "getAnyAoSLinkActive"
+ "handleLow5GRate:"
+ "kWCMBT5GHzWiFiRatesLow"
+ "send RCU1Message WiFiPower = (%!d(MISSING)) WiFiband = (%!d(MISSING)) btPower = (%!d(MISSING)) btBand= (%!d(MISSING))force = [%!d(MISSING)]"
+ "sendRCU1Message:wifiBand:btPowerState:btBand:isForce:"
+ "updateLowWiFi5GRates:"
+ "updateWeightAvgLQM:txRate:"
+ "v36@0:8B16C20B24C28B32"
- "Don't send BT status to RC1 because BT power = (%!d(MISSING)) BT band = (%!d(MISSING))"
- "Don't send Return because WiFiPower = (%!d(MISSING)) band = (%!d(MISSING)) force = [%!d(MISSING)]"
- "Send BT status to RC1 because BT power = (%!d(MISSING)) BT band = (%!d(MISSING))"
- "Send to RCU1 Power = (%!d(MISSING)) band = (%!d(MISSING)) force = (%!d(MISSING))"
- "Sending response to enableULFrequencyUpdates %!@(MISSING)"
- "WiFi Weighted Average LQM event: WeightAvgRSSI %!d(MISSING), weightAvgSNR %!d(MISSING), weightAvgTxRate %!u(MISSING), weightAvgRxRate %!u(MISSING)\n"
- "enableULFrequencyUpdates xpc_reply is NULL"
- "sendRCU1Message:wifiBand:isForce:"
- "sendRCU1MessageBtPowerStatus:BtBand:"
- "v28@0:8B16C20B24"

```
