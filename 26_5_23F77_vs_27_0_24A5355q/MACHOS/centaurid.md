## centaurid

> `/usr/libexec/centaurid`

```diff

-92.0.0.0.0
-  __TEXT.__text: 0x336dc
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_stubs: 0x3200
-  __TEXT.__objc_methlist: 0x10e4
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x18f8
-  __TEXT.__cstring: 0x1968b
-  __TEXT.__oslogstring: 0x58e0
-  __TEXT.__objc_methname: 0x3051
-  __TEXT.__objc_classname: 0x1bc
-  __TEXT.__objc_methtype: 0x960
-  __TEXT.__unwind_info: 0x7d0
-  __DATA_CONST.__auth_got: 0x4f8
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x8
+123.0.0.0.1
+  __TEXT.__text: 0x300e4
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_stubs: 0x3320
+  __TEXT.__objc_methlist: 0x112c
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x15f0
+  __TEXT.__cstring: 0x19b63
+  __TEXT.__oslogstring: 0x5baf
+  __TEXT.__objc_methname: 0x316a
+  __TEXT.__objc_classname: 0x190
+  __TEXT.__objc_methtype: 0x982
+  __TEXT.__unwind_info: 0x7c8
   __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0x10a00
+  __DATA_CONST.__cfstring: 0x10c20
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x558
   __DATA_CONST.__objc_intobj: 0x9480
   __DATA_CONST.__objc_dictobj: 0x1c48
-  __DATA.__objc_const: 0x1be0
-  __DATA.__objc_selrefs: 0xd98
-  __DATA.__objc_ivar: 0x1b0
+  __DATA_CONST.__auth_got: 0x558
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x1c40
+  __DATA.__objc_selrefs: 0xde0
+  __DATA.__objc_ivar: 0x1bc
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x2a8
   __DATA.__bss: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5C16D93F-3A0E-3EDB-AF31-F1608E015376
-  Functions: 617
-  Symbols:   227
-  CStrings:  5550
+  UUID: 6DB22BB4-F178-3529-8D3D-ED5C2CB3EBE7
+  Functions: 623
+  Symbols:   240
+  CStrings:  5631
 
Symbols:
+ _CFDictionarySetValue
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOServiceAddMatchingNotification
+ _kCentauriControllerPropertyFirmwareBootDurations
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retain_x28
CStrings:
+ "%@ %@%@"
+ "%@ %@us%@"
+ "%@ (%@, %@us)%@"
+ "%{public}@::%{public}@: %{public}@ not comparable with range end %{public}@"
+ "%{public}@::%{public}@: %{public}@ not comparable with range start %{public}@"
+ "%{public}@::%{public}@: HW %u, transaction %u, power assertion %u, matched %u, activated %u, LPM %u, halted %u, PMU error %u, activate retries %lu, previous activate retry %@, boot retries %lu, previous boot retry %@"
+ "%{public}@::%{public}@: assertion failure: !_notificationPort -- notification port already exists"
+ "%{public}@::%{public}@: assertion failure: !_serviceMatchIterator -- service match iterator already exists"
+ "%{public}@::%{public}@: assertion failure: !_serviceMatched -- service already matched"
+ "%{public}@::%{public}@: assertion failure: !found -- found more than one service"
+ "%{public}@::%{public}@: assertion failure: (kr == kIOReturnSuccess) && _serviceMatchIterator -- failed to add matching notification"
+ "%{public}@::%{public}@: assertion failure: NO -- invalid power stat dict count"
+ "%{public}@::%{public}@: assertion failure: [key hasSuffix:@\"Duration\"] -- invalid power stat key"
+ "%{public}@::%{public}@: assertion failure: _notificationPort -- failed to create notification port"
+ "%{public}@::%{public}@: assertion failure: _notificationPort -- notification port already null"
+ "%{public}@::%{public}@: assertion failure: _serviceMatchIterator != IO_OBJECT_NULL -- service match iterator already null"
+ "%{public}@::%{public}@: assertion failure: _serviceMatched -- activate without service matched"
+ "%{public}@::%{public}@: chip state: %{public}@"
+ "%{public}@::%{public}@: found service"
+ "%{public}@::%{public}@: idle: %{public}@"
+ "%{public}@::%{public}@: no stats available"
+ "%{public}@::%{public}@: pcie: %{public}@"
+ "%{public}@::%{public}@: registering matching notification"
+ "%{public}s: assertion failure: refcon -- invalid refcon in service match callback"
+ "CompletionTimeout"
+ "Count"
+ "Duration"
+ "EntryCount"
+ "GetPMUFaultInfoFailure"
+ "GetPowerStatsFailure"
+ "GetSiKPublicKeyFailure"
+ "HelloCommandFailure"
+ "IOPropertyExistsMatch"
+ "IOServiceFirstMatch"
+ "IdleDuration"
+ "ManagerStartResult"
+ "PCIe"
+ "RawCommandFailure"
+ "ShellCommandFailure"
+ "WSKU"
+ "^{IONotificationPort=}"
+ "_notificationPort"
+ "_serviceMatchIterator"
+ "_serviceMatched"
+ "assertion failure: !_notificationPort -- notification port already exists"
+ "assertion failure: !_serviceMatchIterator -- service match iterator already exists"
+ "assertion failure: !_serviceMatched -- service already matched"
+ "assertion failure: !found -- found more than one service"
+ "assertion failure: (kr == kIOReturnSuccess) && _serviceMatchIterator -- failed to add matching notification"
+ "assertion failure: NO -- invalid power stat dict count"
+ "assertion failure: [key hasSuffix:@\"Duration\"] -- invalid power stat key"
+ "assertion failure: _notificationPort -- failed to create notification port"
+ "assertion failure: _notificationPort -- notification port already null"
+ "assertion failure: _serviceMatchIterator != IO_OBJECT_NULL -- service match iterator already null"
+ "assertion failure: _serviceMatched -- activate without service matched"
+ "assertion failure: refcon -- invalid refcon in service match callback"
+ "bootPerformanceDataForHostTimestamps:firmwareDurations:"
+ "btLoad"
+ "fdrCal"
+ "flrSetup"
+ "getBootPerformanceSummaryStats"
+ "getFirmwareBootDurations"
+ "hasSuffix:"
+ "initWithObjects:forKeys:"
+ "logPowerStats:"
+ "ptm"
+ "rom"
+ "serviceMatched"
+ "serviceMatched:"
+ "sortedArrayUsingSelector:"
+ "storeFirmwareBootDurations:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "v20@0:8I16"
+ "wifiLoad"
- "%{public}@::%{public}@: %{public}@ not comparible with range end %{public}@"
- "%{public}@::%{public}@: %{public}@ not comparible with range start %{public}@"
- "%{public}@::%{public}@: Awake (%{public}@, %{public}@us), AwakeL3 (%{public}@, %{public}@us), WarmSleep (%{public}@, %{public}@us), DeepSleep (%{public}@, %{public}@us)"
- "%{public}@::%{public}@: HW %u, transaction %u, power assertion %u, activated %u, LPM %u, halted %u, PMU error %u, activate retries %lu, previous activate retry %@, boot retries %lu, previous boot retry %@"
- "%{public}@::%{public}@: L0 (%{public}@, %{public}@us), L1 (%{public}@, %{public}@us), L1.1 (%{public}@, %{public}@us), L1.2 (%{public}@, %{public}@us), L3 (%{public}@, %{public}@us)"
- "%{public}@::%{public}@: idle: CCPU %{public}@, WiFiUMAC %{public}@, WiFiPHY2G %{public}@, WiFiPHY5G %{public}@, WiFiTX %{public}@, WiFiRX %{public}@, WiFiLMAC %{public}@, LMAC2G %{public}@, WiFiLMAC5G %{public}@, WiFiScan %{public}@, BTMain %{public}@, BTSecondary %{public}@, BTScan %{public}@, BTPHY2G %{public}@, BTPHY5G %{public}@"
- "%{public}@::%{public}@: no manager service found"
- "FirmwareBootPerfStats"
- "bootPerformanceDataForHostTimestamps:firmwareTimestamps:"
- "gD8SNRcHQeIxCAvsp+2vjA"

```
