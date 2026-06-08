## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-354.11.0.0.0
-  __TEXT.__text: 0x82b7c
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0xcac0
-  __TEXT.__objc_methlist: 0x767c
-  __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x3488
-  __TEXT.__objc_methname: 0x12aa1
-  __TEXT.__oslogstring: 0xcbf3
-  __TEXT.__objc_classname: 0x8f0
-  __TEXT.__objc_methtype: 0x30d8
-  __TEXT.__gcc_except_tab: 0xe0c
+2700.30.2.0.0
+  __TEXT.__text: 0x7ec3c
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__objc_stubs: 0xcf60
+  __TEXT.__objc_methlist: 0x7e8c
+  __TEXT.__const: 0x8f0
+  __TEXT.__cstring: 0x360a
+  __TEXT.__objc_methname: 0x13341
+  __TEXT.__oslogstring: 0xd6dc
+  __TEXT.__objc_classname: 0x900
+  __TEXT.__objc_methtype: 0x318a
+  __TEXT.__gcc_except_tab: 0x13c4
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x1f98
-  __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x948
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x1680
-  __DATA_CONST.__cfstring: 0x4b20
-  __DATA_CONST.__objc_classlist: 0x298
+  __TEXT.__unwind_info: 0x1bc0
+  __DATA_CONST.__const: 0x17a0
+  __DATA_CONST.__cfstring: 0x4c60
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_intobj: 0x600
-  __DATA_CONST.__objc_arraydata: 0x1c0
-  __DATA_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_intobj: 0xa80
+  __DATA_CONST.__objc_arraydata: 0x2f8
+  __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xf078
-  __DATA.__objc_selrefs: 0x4110
-  __DATA.__objc_ivar: 0x7f4
-  __DATA.__objc_data: 0x19f0
+  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA.__objc_const: 0xfcb8
+  __DATA.__objc_selrefs: 0x42e8
+  __DATA.__objc_ivar: 0x8a0
+  __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xa50
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1c0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFB5B85B-CC49-3EA8-8EFE-955E1E3D4DB8
-  Functions: 2945
-  Symbols:   562
-  CStrings:  5721
+  UUID: A2E75281-B8B3-3CF1-9A04-A66EC0BDF054
+  Functions: 3153
+  Symbols:   569
+  CStrings:  5891
 
Symbols:
+ _CBPairingAgentPairingDataOOBTKKey
+ _CBPairingAgentPairingDataPasskeyKey
+ _OBJC_CLASS_$_NSAssertionHandler
+ ___gxx_personality_v0
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_terminate
- _OBJC_CLASS_$_UARPAccessory
- _OBJC_CLASS_$_UARPAccessoryHardwareBluetooth
- _OBJC_CLASS_$_UARPAssetID
CStrings:
+ "%s Health Observation Bundles for peripheral \"%{private, mask.hash}@\": numOfObservations %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u,  derivedObservationId %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u,  numOfItems %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u, measurementStatus %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u, observationId %u"
+ "@\"CBCentral\""
+ "@\"ServerService\""
+ "@36@0:8r*16Q24C32"
+ "@40@0:8@16^v24q32"
+ "ACTIVE"
+ "Accepts pairing request from peripheral \"%@\""
+ "AppleMagicInputDevice"
+ "AppleMagicKeyboard"
+ "AppleMagicMouse"
+ "AppleMagicTrackpad"
+ "BDAddress"
+ "BTLEPendingEviction"
+ "Could not find peripheral for UUID %@"
+ "Created HIDNonKeyholeUserDevice"
+ "Deallocating HIDNonKeyholeUserDevice"
+ "Deferring service \"%@\" on \"%@\" — link not encrypted"
+ "DeviceAddress"
+ "EnableBTSyncInMs"
+ "FW Revision for peripheral \"%@\": %@ "
+ "Failed to create HID queue"
+ "Failed to create actuator interface"
+ "Failed to create device nonkeyhole interface"
+ "Failed to create keyboard interface"
+ "Failed to create mesa interface"
+ "Failed to create mouse interface"
+ "Failed to create notify queue"
+ "Failed to create trackpad interface"
+ "Failed to generate HID input report for ID %u"
+ "Failed to instantiate inferred pencil power state timer, can't track inferred state. Defaulting to ACTIVE."
+ "Failing pairing request becuase peripheral is nil"
+ "Failing unexpected pairing oob data from peripheral \"%@\""
+ "Failing unexpected pairing request from peripheral \"%@\""
+ "Failing unexpected pairing type from peripheral \"%@\" type %ld"
+ "Get report failed (err=0x%02X, id=0x%02X)"
+ "Got lead report before completing previous frame. Discarding previous report"
+ "Got middle report but nothing in the buffer. Discarding report"
+ "Got tail report but nothing in the buffer. Discarding report"
+ "HID perf is running; blocks to send down any get_report to peripheral"
+ "HID perf is running; blocks to send down any set_report to peripheral"
+ "HIDAppleMagicInputDevice"
+ "HIDAppleMagicInputDevice.mm"
+ "HIDAppleMagicKeyboard"
+ "HIDAppleMagicMouse"
+ "HIDAppleMagicTrackpad"
+ "HIDNonKeyholeUserDevice"
+ "HW Revision for peripheral \"%@\": %@ "
+ "IDLE"
+ "Inferred accessory power state changed from %s to %s"
+ "Input report ID %u is not a large report"
+ "Invalid size input report"
+ "Keyboard"
+ "Manfr. Name for peripheral \"%@\": %@ "
+ "Model Number for peripheral \"%@\": %@ "
+ "Mouse"
+ "NOT (SELF IN %@)"
+ "NULL"
+ "No HID devices are ready, discarding input report (ID %u)"
+ "Not a valid application ID. Good bye."
+ "Not a valid application ID. Good bye. %s"
+ "OOB pairing for HID peripheral UUID %@, enable %d"
+ "Received exit suspend input report (ID %u)"
+ "Received exit suspend input report (ID %u), IsSuspended(%d)"
+ "Rejects pairing request from peripheral \"%@\""
+ "Retry #%u getting report (id=0x%02X)"
+ "Retry #%u setting report (id=0x%02X"
+ "SW Revision for peripheral \"%@\": %@ "
+ "Serial Number for peripheral \"%@\": %@ "
+ "Set report failed (err=0x%02X, id=0x%02X)"
+ "Skipping existing service: %@"
+ "Subclasses need to overwrite this method"
+ "T@\"CBCentral\",R,&,N,V_central"
+ "T@\"NSMutableData\",&,N,V_hidInputReportBuffer"
+ "T@\"NSMutableData\",&,N,V_largeReportBuffer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_powerStateTimeoutTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,V_persistanceAssertion"
+ "T@\"NSString\",C,N,V_BDAddress"
+ "T@\"ServerService\",R,&,N,V_serverService"
+ "TB,N,V_isDisconnected"
+ "TB,N,V_isPowerStateActive"
+ "TB,N,V_powerManagementIsSuspended"
+ "Ti,R,N,V_hidperfMode"
+ "Trackpad"
+ "Unknown input report ID %u. I don't know to which keyhole it belongs to, so discarding"
+ "Waking screen with spoofed click"
+ "_BDAddress"
+ "_central"
+ "_enableOOBPairingForHID"
+ "_hidInputReportBuffer"
+ "_hidperfMode"
+ "_internalDevice"
+ "_isDisconnected"
+ "_isPowerStateActive"
+ "_largeReportBuffer"
+ "_oobPairingData"
+ "_powerManagementIsSuspended"
+ "_powerStateTimeoutTimer"
+ "_serverService"
+ "accelerometerUserDevice"
+ "accumulateLargeReport:size:"
+ "actuatorUserDevice"
+ "classifySubscribersForService:serverService:intoEvictions:"
+ "com.apple.DiagnosticExtensions.BluetoothHeadset"
+ "com.apple.bluetooth.airpodslogging"
+ "connectedTransport"
+ "controlPointDelayMs"
+ "controlPointDelayMs cnx params: %@"
+ "createServices: creating service %@"
+ "currentHandler"
+ "dataWithLength:"
+ "destroyAllServices"
+ "destroyServices: evicting non-ASK central %@ from service %@"
+ "destroyServices: retaining service %@ (%lu non-ASK central(s) to evict)"
+ "destroyServices: stopping service %@ (no ASK subscribers)"
+ "didChangeValueForKey:"
+ "evictionWithServerService:central:characteristic:"
+ "filteredArrayUsingPredicate:"
+ "generateHIDInputReport:reportID:"
+ "generateHIDInputReport:size:reportID:"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "handleInferredPowerState:"
+ "handleOOBPairingDataForHIDMsg got data, uuid: %s length: %lu"
+ "handleOOBPairingDataForHIDMsg:"
+ "hidInputReportBuffer"
+ "hidperf mode is running"
+ "hidperf mode is stopped"
+ "hidperfMode"
+ "initWithProperties:hidDescriptor:delegate:"
+ "isDisconnected"
+ "isHIDPerfCommandStart:"
+ "isHIDPerfCommandStop:"
+ "isHIDPerfRunning"
+ "isMesaKeyboard"
+ "isPowerStateActive"
+ "kEnable"
+ "kOOBPData"
+ "keyboardDescriptor"
+ "keyboardUserDevice"
+ "largeReportBuffer"
+ "legacyKeyboardDescriptor"
+ "lowercaseString"
+ "mesaKeyboardDescriptor"
+ "mesaUserDevice"
+ "mouseUserDevice"
+ "newDeviceAccelerometerUserDevice:keyholeID:"
+ "newDeviceActuatorUserDevice:keyholeID:"
+ "newDeviceInternalKeyholeUserDevice:"
+ "newDeviceInternalKeyholedUserDevice:"
+ "newDeviceKeyboardUserDevice:keyholeID:hiddescriptor:"
+ "newDeviceMesaUserDevice:keyholeID:"
+ "newDeviceMgntUserDevice:keyholeID:"
+ "newDeviceMouseUserDevice:keyholeID:"
+ "newDeviceTrackpadUserDevice:keyholeID:"
+ "newUserDevice:descriptor:descriptorLength:"
+ "newUserDevice:hiddescriptor:keyholeID:"
+ "observerDidNoteBiometricResourceStateChanged:"
+ "oobPairingForHID:enable:oobData:"
+ "peerDidRequestPairing : %ld"
+ "peripheral:didCompleteChannelSoundingSession:"
+ "peripheral:didReceiveChannelSoundingProcedureResults:error:"
+ "powerManagementIsSuspended"
+ "powerStateTimeoutTimer"
+ "respondToPairingRequest:type:accept:data:"
+ "serverService"
+ "setBDAddress:"
+ "setHidInputReportBuffer:"
+ "setIsDisconnected:"
+ "setIsPowerStateActive:"
+ "setLargeReportBuffer:"
+ "setPowerManagementIsSuspended:"
+ "setPowerStateTimeoutTimer:"
+ "trackpadUserDevice"
+ "updateInferredPowerState:"
+ "usesInferredPowerState"
+ "v24@0:8@\"BBObserver\"16"
+ "v32@0:8*16Q24"
+ "v40@0:8@\"CBPeripheral\"16@\"CBChannelSoundingProcedureResults\"24@\"NSError\"32"
+ "willChangeValueForKey:"
- "\r"
- "%c"
- "%s Health Observation TLVs for peripheral \"%{private, mask.hash}@\": numOfObservations %u"
- "Created uarpAccessory:%@ uarpAssetID:%@"
- "EnableBTSync"
- "Health"
- "HealthDaemon"
- "HeartRateCoordinator"
- "No application ID. Good bye."
- "T@\"NSObject<OS_os_transaction>\",&,N,V_persistanceAssertion"
- "TB,N,V_pmIsSuspended"
- "Unsupported UARP accessory!"
- "_pmIsSuspended"
- "initWithHardwareID:uuid:"
- "initWithLocationType:remoteURL:"
- "initWithVendorIDSource:vendorID:productID:productVersion:"
- "log_%@.uarp"
- "peripheral:didUpdateNotificationStateForCharacteristic: loggingSuperbinaryURL %@"
- "pmIsSuspended"
- "pulse"
- "setAutoDownloadAllowed:"
- "setPmIsSuspended:"

```
