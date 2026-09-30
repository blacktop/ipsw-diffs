## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-190.43.0.0.0
-  __TEXT.__text: 0x840dd8
+190.45.1.0.0
+  __TEXT.__text: 0x845630
   __TEXT.__auth_stubs: 0x4760
-  __TEXT.__objc_stubs: 0x16960
+  __TEXT.__objc_stubs: 0x16a20
   __TEXT.__init_offsets: 0x54
-  __TEXT.__objc_methlist: 0x8844
-  __TEXT.__const: 0x24e9c
-  __TEXT.__gcc_except_tab: 0x6a300
-  __TEXT.__cstring: 0xad54c
+  __TEXT.__objc_methlist: 0x888c
+  __TEXT.__const: 0x24edc
+  __TEXT.__gcc_except_tab: 0x6ab6c
+  __TEXT.__cstring: 0xada7f
   __TEXT.__objc_classname: 0x9d0
-  __TEXT.__objc_methname: 0x1b111
-  __TEXT.__objc_methtype: 0x491b
-  __TEXT.__oslogstring: 0xa9fc1
+  __TEXT.__objc_methname: 0x1b1f3
+  __TEXT.__objc_methtype: 0x4936
+  __TEXT.__oslogstring: 0xaa305
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x223a8
+  __TEXT.__unwind_info: 0x22748
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x23c8
-  __DATA_CONST.__got: 0xd58
+  __DATA_CONST.__got: 0xd68
   __DATA_CONST.__auth_ptr: 0x1f8
-  __DATA_CONST.__const: 0x2f1a8
-  __DATA_CONST.__cfstring: 0x223a0
+  __DATA_CONST.__const: 0x2f3c8
+  __DATA_CONST.__cfstring: 0x22740
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_intobj: 0x9d8
-  __DATA_CONST.__objc_arraydata: 0x418
-  __DATA_CONST.__objc_dictobj: 0x2a8
+  __DATA_CONST.__objc_intobj: 0x9f0
+  __DATA_CONST.__objc_arraydata: 0x438
+  __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xebe8
-  __DATA.__objc_selrefs: 0x6890
+  __DATA.__objc_selrefs: 0x68b8
   __DATA.__objc_ivar: 0xfc8
   __DATA.__objc_data: 0x19f0
   __DATA.__data: 0x47e8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x71c3a
+  __DATA.__bss: 0x71c4a
   __DATA.__common: 0x6fb0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 606CD01A-78E5-3891-B7C3-D45DA006348C
-  Functions: 32640
-  Symbols:   1591
-  CStrings:  42797
+  UUID: 885CC594-E233-33EE-8F23-7896C77EE59A
+  Functions: 32707
+  Symbols:   1593
+  CStrings:  42898
 
Symbols:
+ _kSymptomDiagnosticKeyPayloadDEParameters
+ _kTCCAccessCheckOptionPrompt
+ _tcc_authorization_check_audit_token
- _objc_retain_x9
CStrings:
+ "    %@ : %@"
+ "%s: data length: %d"
+ "-[CBDaemonServer _updateUserControllerCloudDevices]"
+ ".*(%@).*dev_sign.*(%@).*(%@)"
+ ".*(%@)_.*(%@).*(%@)"
+ "19859eeee642c440ca8735a91677ccc3cba9b936ae1f64f6344e160fa3acb561"
+ "21:51:04"
+ "Airplane Mode"
+ "Alert Data exceeds max length"
+ "Alert ID must be %d bytes"
+ "Already trying to connect to same device \"%{public}@\", %{public}s"
+ "Appearance"
+ "AppearanceValue"
+ "Attempt to call Malloc after Memory Manager was terminated"
+ "BatteryCount"
+ "BatteryServiceStats"
+ "BtMetricsCache"
+ "BtPowerOnDuration"
+ "Connecting address %{public}s, temp address %{public}s"
+ "Coupling"
+ "Deprecated"
+ "Disconnect Req, Reason: %@ (%u)"
+ "Domain"
+ "Echo Request failed for device %s cmd:%d validHandle:%d refCount:%d"
+ "EnableAntennaSwitchVSEConfig"
+ "Excessive wakes caused by device %{public}s"
+ "Excessive wakes caused by device %{public}s with vid %d and pid %d"
+ "Expected delay in SRM enabled:%d ms, maxRead:%d bytes"
+ "Failed to teardown BT Link to device with status %d"
+ "GATT is Asking to pair due to LE_ATT_ERROR_INSUFFICIENT_AUTHENTICATION startAutoPairing=%d"
+ "GATT is Asking to pair due to LE_ATT_ERROR_INSUFFICIENT_ENCRYPTION startAutoPairing=%d"
+ "HCI event: ModeChange, %!, handle %d, newMode %d (%s), interval %d, wakeUpEvent %d"
+ "Jul  1 2025"
+ "LE Audio device - disconnecting other profiles"
+ "LEAudio LiveOn, liveon enabled:%d, platform supported:%d, feature enabled:%d"
+ "LEAudioLiveOnEnable"
+ "LastBtPowerOnTimeStamp"
+ "Loading Bluetooth firmware signed with the development secure boot key"
+ "No devices to cloud sync for user controller"
+ "No devices to upload sync for user controller"
+ "OI_HCICMD_CreateConnectionCancel failed for %:"
+ "Posting HID Session Metric: Pid|Vid %x, RSSI Average %d, PER Average %d%%, Duration %ds, Disconnection Reason %d, DeviceType %s"
+ "Reconnect"
+ "Role Switch Failed"
+ "SMP_DestroyPairingDeviceAndDispatch: invalid data."
+ "SR Hijack"
+ "Safety Alerts payload construction failed with %@"
+ "Screen Undimmed - SpringBoard"
+ "Set TAG as LEAudio device"
+ "Set delay in SRM enabled:%d ms, maxRead:%d bytes"
+ "Signature must be %d bytes"
+ "StackLEPairingComplete with %@"
+ "StackPairingComplete found no identifier for device: %s"
+ "StackPairingComplete with %@"
+ "Successfully to command teardown BT Link to paired device"
+ "Swap Audio"
+ "Swapping No Audio"
+ "TCC approval status for session %s: %llu"
+ "The device \"%@\" supports CAS or ASCS"
+ "The device \"%@\" supports CCC, disabling autopairing"
+ "The device \"%@\" supports TMAS"
+ "Too Many Sources"
+ "Triangle Update"
+ "ULLA"
+ "Uncoordinated Swap"
+ "Update connecting address to temp resolved address"
+ "Updating connecting address to %@"
+ "Version is invalid"
+ "Warning: Not persisting device \"%{public}s\" to database"
+ "_LEAUDIO_DEVICE_"
+ "_TMAS_LE_AUDIO_DEVICE_"
+ "_findPowerSourceWithIdentifiers:and:"
+ "_handleStackLEPairingComplete:"
+ "_handleStackPairingComplete:"
+ "_reportMetricIfNeeded:"
+ "_reportMetrics"
+ "bearer is null for connection 0x%08x - for:%d"
+ "bt-use-dev-sign-firmware"
+ "buildSafetyAlertsAdvertisingData:advertisingAddresses:advertisingData:advertiseRate:error:"
+ "com.apple.DiagnosticExtensions.ConnectivityDE"
+ "com.apple.Language-Chooser"
+ "com.apple.Touch-ID-Settings.extension"
+ "com.apple.audio.AudioMIDISetup"
+ "com.apple.audio.midi.CoreMIDI"
+ "sendDeviceBatteryMetric: %@"
+ "srs.dev-sign-fw"
+ "v56@0:8@16^@24^@32^i40^@48"
- "    %@"
- "### Received battery change notification for device that is not connected: %s"
- "(BTPowerLog): Interval: %d"
- ".*(%@).*(%@).*(%@)"
- "21:20:37"
- "BtFirmwareErrorCache"
- "Classic Map"
- "Device \"%{public}@\" does not support multiple addresses"
- "Device \"%{public}@\" does not support multiple addresses but still in the fDevicesToUpdateInFilterAcceptList"
- "Echo Request failed for device %s cmd:%d refCount:%d"
- "GATT is Asking to pair due to LE_ATT_ERROR_INSUFFICIENT_ENCRYPTION"
- "HCI event: ModeChange, %!, handle %d, newMode %d (%s), interval %d"
- "IOKit source has non-UUID accessoryID format: %@"
- "Jun 18 2025"
- "Posting HID Session Metric: Pid|Vid %x, RSSI Average %d, PER Average %d%%, Duration %ds, Disconnection Reason %d"

```
