## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-34.25.1.1.1
-  __TEXT.__text: 0x239794
-  __TEXT.__auth_stubs: 0x2c40
-  __TEXT.__objc_stubs: 0x1d4a0
-  __TEXT.__objc_methlist: 0xda14
-  __TEXT.__const: 0x4200
-  __TEXT.__gcc_except_tab: 0x5b64
-  __TEXT.__cstring: 0x525c3
+34.27.1.0.0
+  __TEXT.__text: 0x23ea90
+  __TEXT.__auth_stubs: 0x2c30
+  __TEXT.__objc_stubs: 0x1d6c0
+  __TEXT.__objc_methlist: 0xdae4
+  __TEXT.__const: 0x4210
+  __TEXT.__gcc_except_tab: 0x5b6c
+  __TEXT.__cstring: 0x53343
   __TEXT.__objc_classname: 0x1003
-  __TEXT.__objc_methname: 0x2a195
-  __TEXT.__objc_methtype: 0x3e49
+  __TEXT.__objc_methname: 0x2a4a5
+  __TEXT.__objc_methtype: 0x3e79
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__oslogstring: 0x8f8a
+  __TEXT.__oslogstring: 0x919a
   __TEXT.__ustring: 0x10
-  __TEXT.__constg_swiftt: 0x1acc
+  __TEXT.__constg_swiftt: 0x1adc
   __TEXT.__swift5_typeref: 0x189e
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x190b

   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_proto: 0x350
   __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift5_capture: 0x19f8
+  __TEXT.__swift5_capture: 0x1a28
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6c18
+  __TEXT.__unwind_info: 0x6cc0
   __TEXT.__eh_frame: 0x1ca0
-  __DATA_CONST.__auth_got: 0x1630
+  __DATA_CONST.__auth_got: 0x1628
   __DATA_CONST.__got: 0xd70
   __DATA_CONST.__auth_ptr: 0x580
-  __DATA_CONST.__const: 0xb950
-  __DATA_CONST.__cfstring: 0xb360
+  __DATA_CONST.__const: 0xba68
+  __DATA_CONST.__cfstring: 0xb2c0
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x170

   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x1d5e8
-  __DATA.__objc_selrefs: 0x8aa0
-  __DATA.__objc_ivar: 0x172c
+  __DATA.__objc_const: 0x1d680
+  __DATA.__objc_selrefs: 0x8b38
+  __DATA.__objc_ivar: 0x1740
   __DATA.__objc_data: 0x3020
-  __DATA.__data: 0x4cf0
+  __DATA.__data: 0x4d00
   __DATA.__bss: 0x6b80
   __DATA.__common: 0x3a0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 26FCF940-79DE-3134-A6A5-AB318D97642C
-  Functions: 10967
-  Symbols:   1287
-  CStrings:  16989
+  UUID: 110458AA-02F8-3344-AEBA-8904E40B6197
+  Functions: 11039
+  Symbols:   1286
+  CStrings:  17068
 
Symbols:
- _objc_retain_x10
CStrings:
+ "-[AASourceDevice _cancelDeactivateRpLinkTimer]"
+ "-[AASourceDevice _deactivateRpLinkWithTimeout:]"
+ "-[AASourceDevice _deactivateRpLinkWithTimeout:]_block_invoke"
+ "-[AASourceDeviceManager _removeDeviceFromRPDevice:]"
+ "-[AASourceDeviceManager _startScreenOffScanningTimer:]_block_invoke"
+ "-[AASourceDeviceManager _startScreenOffScanningWithTimeout:]"
+ "-[SR3PDiscoveredHeadphone setDevicePlacementExternal:]"
+ "-[SR3PRoutingDaemon _aaSourceDeviceFound:]"
+ "-[SR3PRoutingDaemon _deviceInfoChanged:completionHandler:]"
+ "-[SR3PRoutingDaemon _handleAudioSourceDevicesUpdate:headphone:btAddress:completionHandler:]"
+ "-[SR3PRoutingDaemon _handleAudioSourceDevicesUpdate:headphone:btAddress:completionHandler:]_block_invoke"
+ "-[SR3PRoutingDaemon _headphoneWithPendingTipiRequestFor:]"
+ "-[SR3PRoutingDaemon _registerHeadphone:btAddress:completionHandler:]"
+ "-[SR3PRoutingDaemon _updateDeviceSupport:deviceInfo:]"
+ "-[SR3PRoutingDaemon headphoneInfo:completionHandler:]_block_invoke"
+ "=== Printing all devices (%lu total) === _rpClient: %@"
+ "AASourceDeviceFound: Found headphone %@ with pending TIPI request for source %@"
+ "AASourceDeviceFound: No headphone found with pending TIPI request for source %@"
+ "AASourceDeviceFound: Source device found with BT address: %@"
+ "BtAddressFromAAKDeviceInfo: Could not resolve BT address from AAKDeviceInfo"
+ "BtAddressFromAAKDeviceInfo: Failed to resolve BT address from btIdentifier: %@"
+ "BtAddressFromAAKDeviceInfo: No AAKDeviceInfo provided"
+ "BtAddressFromAAKDeviceInfo: No btIdentifier provided in deviceInfo"
+ "CancelDeactivateRpLinkTimer: Canceling timer for device %@"
+ "Cannot extract btAddress from RPCompanionLinkDevice for removal"
+ "DeactivateRpLinkWithTimeout: Starting %.1f-second timer for device %@"
+ "DeactivateRpLinkWithTimeout: Timer expired after %.1f seconds for device %@"
+ "Device %@ does not support audio switching capability"
+ "Device %@ does not support placement capability"
+ "Device update failed for: %s - %s"
+ "Device update successful for: %s"
+ "DeviceFound - %@ (%@) %@"
+ "DeviceFound: Creating and adding new device with btAddress %@"
+ "DeviceFound: Device with btAddress %@ already exists, updating properties"
+ "DeviceFound: Skip, cannot extract btAddress from device"
+ "DeviceFound: Skip, device is nil"
+ "DeviceInfoChanged: %@ btAddress %@"
+ "DeviceInfoChanged: BTAudioDriver controller not available"
+ "DeviceInfoChanged: Device %@ does not support audio switching capability (deviceSupport=0x%X)"
+ "DeviceInfoChanged: Device %@ does not support placement capability (deviceSupport=0x%X)"
+ "DeviceInfoChanged: Headphone device %@ not found in SR3PDiscoveredHeadphoneManager"
+ "DeviceInfoChanged: Successfully updated device %@"
+ "DeviceInfoChanged: Updated device %@ with appearance %s"
+ "DeviceInfoChanged: Updated device %@ with placement %d internalPlacement %s"
+ "DeviceLost - %@ (%@)"
+ "DevicePlacementChanged: Device %@ does not support placement capability (deviceSupport=0x%X)"
+ "Failed to create reply message for getCurrent"
+ "Failed to create reply message for updateDevice"
+ "HandleAudioSourceDevicesUpdate: Current device %@ is not primary (%@) or secondary (%@) device"
+ "HandleAudioSourceDevicesUpdate: No primary device address provided"
+ "HandleAudioSourceDevicesUpdate: Other Tipi device %@ is not on the same iCloud account"
+ "HandleAudioSourceDevicesUpdate: Setting primary device %@ secondary device %@ for headphone %@ (btIdentifier %@) currentDevice %@ from bundle %@"
+ "HandleAudioSourceDevicesUpdate: Timer expired after %d seconds for headphone %@"
+ "HandleAudioSourceDevicesUpdate: Verified other Tipi device %@ is on the same iCloud account (IDSDevice: %@)"
+ "HandleAudioSourceDevicesUpdate: otherTipiAddressCandidate %@ is already set as otherTipiBtAddress, returning success"
+ "HeadphoneInfo: %@ btAddress %@"
+ "HeadphoneInfo: Headphone device %@ not found in SR3PDiscoveredHeadphoneManager"
+ "HeadphoneInfo: Successfully retrieved info for device %@"
+ "HeadphoneInfo: TIPI configuration - primary: %@, secondary: %@"
+ "Processing getCurrent for bluetoothIdentifier: %s, btAddress: %s, bundleID: %s"
+ "Processing updateDevice for bluetoothIdentifier: %s, btAddress: %s, appearance: %u, placement: %u, deviceSupports: %lld"
+ "Received nil response from Tipi request"
+ "RemoveDevice: Device with btAddress %@ not found in managed devices"
+ "RemoveDevice: Skip, rpDevice is nil"
+ "Removing device with btAddress %@"
+ "Screen off scanning timeout reached (%.1f seconds), stopping screen off scanning"
+ "SendTipiRequest: Screen locked, starting screen off scanning for %@"
+ "SendTipiRequest: Tipi request failed for headphone %@ - Reason: %@"
+ "SendTipiRequest: Tipi request succeeded for headphone %@ with remote device %@, setting routing action to %s"
+ "SetAudioSourceDevices: Device %@ does not support audio switching capability (deviceSupport=0x%X)"
+ "Setting devicePlacementExternal %@ %s -> %s"
+ "StartScanningWithControlFlags: RP client listener already exists with same control flags"
+ "StartScreenOffScanning: Invalid timeout value %.1f seconds, must be greater than 0"
+ "StartScreenOffScanning: Starting screen off scanning with control flags: 0x%x, timeout: %.1f seconds"
+ "TI,N,V_devicePlacementExternal"
+ "Tipi request failed: %@"
+ "Unknown reason"
+ "_aaSourceDeviceFound:"
+ "_cancelDeactivateRpLinkTimer"
+ "_deactivateRpLinkTimer"
+ "_deactivateRpLinkWithTimeout:"
+ "_deviceInfoChanged:completionHandler:"
+ "_devicePlacementExternal"
+ "_handleAudioSourceDevicesUpdate:headphone:btAddress:completionHandler:"
+ "_headphoneWithPendingTipiRequestFor:"
+ "_headphoneWithPendingTipiRequestFor: Found headphone %@ with pending TIPI request for candidate %@"
+ "_headphoneWithPendingTipiRequestFor: Looking for headphone with pending TIPI request for %@"
+ "_headphoneWithPendingTipiRequestFor: No headphone found with pending TIPI request for %@"
+ "_registerHeadphone: Failed to add or retrieve headphone device %@"
+ "_registerHeadphone: Successfully registered headphone %@ with device support flags 0x%x from bundle %@"
+ "_registerHeadphone:btAddress:completionHandler:"
+ "_removeDeviceFromRPDevice:"
+ "_screenOffScanningControlFlags"
+ "_screenOffScanningTimer"
+ "_screenOnScanningControlFlags"
+ "_startScreenOffScanningTimer:"
+ "_startScreenOffScanningWithTimeout:"
+ "_updateDeviceSupport: feature support changed. Notifying BTAudioDriver"
+ "_updateDeviceSupport:deviceInfo:"
+ "aaSourceDeviceFound:"
+ "btAddress %@ nbNm %@ isNb %s ts1 %s ts2 %s fw %@ isCp %s sc %d nbInEar %s nbLh %@ fd %s nbSt %s prevFailConnect %s srVer %s chipMfg %s"
+ "cancelDeactivateRpLinkTimer"
+ "connectedDeviceCount"
+ "deactivateRpLinkWithTimeout:"
+ "deviceInfoChanged:completionHandler:"
+ "devicePlacementExternal"
+ "getCurrent"
+ "getCurrent failed for: %s - %s"
+ "getCurrent failed for: %s - no device info returned"
+ "getCurrent successful for: %s"
+ "headphoneInfo:completionHandler:"
+ "ple"
+ "setDevicePlacementExternal:"
+ "speaker.bluetooth.fill"
+ "startScreenOffScanningWithTimeout:"
+ "updateDevice"
+ "v24@?0@\"AAKDeviceInfo\"8@\"NSError\"16"
+ "📋 Updated Device Info: "
- "-[AASourceDeviceManager addDeviceFromRPDevice:]"
- "-[AASourceDeviceManager addDeviceFromRPDevice:]_block_invoke"
- "-[AASourceDeviceManager addDeviceWithBtAddress:]_block_invoke"
- "-[AASourceDeviceManager removeDeviceWithBtAddress:]_block_invoke"
- "-[SRDiscoveredDevice _updateChipManufacture:]"
- "=== Printing all devices (%lu total) ==="
- "AddDevice: Skip, rpDevice is nil"
- "BtAddressFromBtIdentifier: Got BT address from connected CBDevice: %@"
- "Cannot extract btAddress from RPCompanionLinkDevice"
- "Creating and adding new device from RPDevice with btAddress %@"
- "Creating and adding new device with btAddress %@"
- "Device with btAddress %@ not found for removal"
- "MIKA Updating chipManufacture %@ %s -> %s based on productID %u"
- "RPClient: Device found - %@ (%@) %@"
- "RPClient: Device lost - %@ (%@)"
- "Received nil response from TIPI request"
- "RegisterHeadphoneWithCompletionHandler: Failed to add or retrieve headphone device %@"
- "RegisterHeadphoneWithCompletionHandler: Successfully registered headphone %@ with device support flags 0x%x from bundle %@"
- "RegisterHeadphoneWithCompletionHandler: feature support changed. Notifying BTAudioDriver"
- "SR3PRoutingDaemonErrorDomain"
- "SendTipiRequest: TIPI request failed for headphone %@ - Reason: %@"
- "SendTipiRequest: TIPI request succeeded for headphone %@ with remote device %@, setting routing action to %s"
- "StartScanningWithControlFlags: RP client listener already exists"
- "TIPI request failed"
- "TQ,R,N"
- "_btAddressFromAAKDeviceInfo: Could not resolve BT address from AAKDeviceInfo"
- "_btAddressFromAAKDeviceInfo: Failed to resolve BT address from btIdentifier: %@"
- "_btAddressFromAAKDeviceInfo: Got BT address from btAddressData: %@"
- "_btAddressFromAAKDeviceInfo: Got BT address from btIdentifier: %@"
- "_btAddressFromAAKDeviceInfo: No AAKDeviceInfo provided"
- "_btAddressFromAAKDeviceInfo: No btIdentifier provided in deviceInfo"
- "addDeviceFromRPDevice:"
- "btAddress %@ nbNm %@ isNb %s ts1 %s ts2 %s fw %@ isCp %s sc %d nbInEar %s nbLh %@ fd %s nbSt %s prevFailConnect %s srVer %s"
- "earbuds"

```
