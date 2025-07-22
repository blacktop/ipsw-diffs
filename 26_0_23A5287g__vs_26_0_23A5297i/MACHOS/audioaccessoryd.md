## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-30.51.1.1.1
-  __TEXT.__text: 0x1e779c
+30.54.2.1.1
+  __TEXT.__text: 0x1e88a8
   __TEXT.__auth_stubs: 0x2ad0
-  __TEXT.__objc_stubs: 0x16c40
-  __TEXT.__objc_methlist: 0xb55c
-  __TEXT.__const: 0x3d40
-  __TEXT.__gcc_except_tab: 0x4800
-  __TEXT.__cstring: 0x3f293
+  __TEXT.__objc_stubs: 0x16d60
+  __TEXT.__objc_methlist: 0xb5ec
+  __TEXT.__const: 0x39d0
+  __TEXT.__gcc_except_tab: 0x4970
+  __TEXT.__cstring: 0x3f6a3
   __TEXT.__objc_classname: 0xa21
-  __TEXT.__objc_methname: 0x226f5
-  __TEXT.__objc_methtype: 0x320e
+  __TEXT.__objc_methname: 0x22925
+  __TEXT.__objc_methtype: 0x3266
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_capture: 0x193c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x5430
+  __TEXT.__unwind_info: 0x5498
   __TEXT.__eh_frame: 0x2070
   __DATA_CONST.__auth_got: 0x1578
-  __DATA_CONST.__got: 0xc30
+  __DATA_CONST.__got: 0xc38
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xa7a8
-  __DATA_CONST.__cfstring: 0x9420
+  __DATA_CONST.__const: 0xa7d0
+  __DATA_CONST.__cfstring: 0x9560
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19d18
-  __DATA.__objc_selrefs: 0x7568
-  __DATA.__objc_ivar: 0x1438
+  __DATA.__objc_const: 0x19da0
+  __DATA.__objc_selrefs: 0x75d0
+  __DATA.__objc_ivar: 0x1440
   __DATA.__objc_data: 0x2a08
   __DATA.__data: 0x4218
   __DATA.__bss: 0x6ac0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D6F0E203-C57A-35CA-8571-93DB4A2E2A72
-  Functions: 9014
+  UUID: 6BA96925-4728-3569-B516-0C9844CFE5F4
+  Functions: 9033
   Symbols:   1224
-  CStrings:  14069
+  CStrings:  14118
 
Symbols:
+ _MRAVOutputContextAddOutputDevice
- _CUPrintFlags64
CStrings:
+ "### areHeadphonesNearbyAndEligibleToPlay failed %{error}"
+ "-[AANearbyDeviceManagerDaemon pairedDeviceLost:]_block_invoke"
+ "-[AAPairedDeviceDaemon _aaDeviceRecordsRemovedWithRecords:]"
+ "-[AAPairedDeviceDaemon _aaDeviceRecordsUpdatedWithRecords:]"
+ "-[AAPairedDeviceDaemon updatePairedDeviceWithIdentifier:withConfig:]_block_invoke"
+ "-[AAServicesXPCConnection areHeadphonesNearbyAndEligibleToPlay:completion:]_block_invoke"
+ "-[BTSmartRoutingDaemon _generateEvaluatorError:errorReason:]"
+ "-[BTSmartRoutingDaemon _smartRoutingAddRoute:]"
+ "-[BTSmartRoutingDaemon areHeadphonesNearbyAndEligibleToPlay:]_block_invoke"
+ "-[BTSmartRoutingDaemon areHeadphonesNearbyAndEligibleToPlay:]_block_invoke_2"
+ "@36@0:8^@16B24^B28"
+ "AANearbyDevice case unpaired: %@"
+ "AANearbyDevice unpaired: %@"
+ "AANearbyDevice updated from advertisement payload: %@"
+ "Add Route for device: %@"
+ "Error Reason"
+ "Evaluator error: %@"
+ "Found lowest battery in SR map: %@"
+ "Found lowest battery in battery monitor: %@"
+ "Found lowest battery in nearbydevice map: %@"
+ "Ignoring device streaming A2DP from companion device"
+ "Ignoring device streaming HFP from companion device"
+ "Ignoring device streaming from non-companion device"
+ "Ignoring device that is already connected"
+ "Ignoring device that is connected to SR disabled source device"
+ "Ignoring device that is not SR enabled"
+ "Ignoring device that is not paired"
+ "Ignoring devices that are not in-ear"
+ "Nearby and Eligible"
+ "No Eligible Device Nearby"
+ "Playing from current device"
+ "Playing from other device"
+ "T@\"NSString\",&,N,V_watchConnectionCategory"
+ "TB,N,V_tipiWithCompanion"
+ "_caseDeviceWithPrimaryIdentifier:"
+ "_deviceWithBluetoothAddress:"
+ "_generateEvaluatorError:errorReason:"
+ "_getEligibleNearbyWxDevice:companionNeedsToBeIdle:isStreamingFromCompanion:"
+ "_routeIndicationCountMap"
+ "_smartRoutingAddRoute:"
+ "_tipiWithCompanion"
+ "_watchConnectionCategory"
+ "areHeadphonesNearbyAndEligibleToPlay:"
+ "areHeadphonesNearbyAndEligibleToPlay: Paired %d Connected %d, NearbyInfo %d, Wx %d BluetoothState %s Screen lock state %s"
+ "areHeadphonesNearbyAndEligibleToPlay: eligibilityStatus %s"
+ "areHeadphonesNearbyAndEligibleToPlay:completion:"
+ "initWithDictionary:copyItems:"
+ "initWithLevel:productID:state:type:"
+ "lastConnectedHost is not signed into the same iCloud account as this device"
+ "received cloud push, AADeviceRecord removed: %@ \ndevice: %@"
+ "setTipiWithCompanion:"
+ "setWatchConnectionCategory:"
+ "tipiWithCompanion"
+ "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?C@\"NSError\">24"
+ "v32@0:8@16^@24"
+ "watchConnectionCategory"
- "-[AANearbyDeviceManagerDaemon _cbDeviceFound:]"
- "-[AAPairedDeviceDaemon _aaDeviceRecordsRemovedWithRecords:]_block_invoke"
- "-[AAPairedDeviceDaemon _aaDeviceRecordsUpdatedWithRecords:]_block_invoke"
- "-[AAPairedDeviceDaemon updatePairedDeviceWithIdentifier:withConfig:]"
- "-[AAXPCEventPublisherDaemon _deviceFound:]"
- "-[AAXPCEventPublisherDaemon _deviceLost:]"
- "AANearbyDevice updated from advertisment payload: %@"
- "CBDevice unpaired, %@"
- "Device found: %@"
- "Device lost: %@"
- "Found lowest battery: %@"
- "Ignoring CBDevice without BLEAdvertisementData change flag"
- "SmartRoutingSecondsBetweenConnectedBanner: %.0f -> %.0f"
- "Updating Nearby with CBDevice(Change Flags: %@): %@"
- "_connectedHeadphones"
- "received cloud push, AADeviceRecord removed: %@"
- "srSecondsBetweenBanner"

```
