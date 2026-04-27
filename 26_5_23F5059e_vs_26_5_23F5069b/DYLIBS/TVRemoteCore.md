## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.50.7.0.0
-  __TEXT.__text: 0x49848
+548.50.8.0.0
+  __TEXT.__text: 0x49838
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x5d1c
   __TEXT.__const: 0x2b0
   __TEXT.__gcc_except_tab: 0xd68
   __TEXT.__cstring: 0x332e
-  __TEXT.__oslogstring: 0x6b1e
+  __TEXT.__oslogstring: 0x6898
   __TEXT.__unwind_info: 0x1608
   __TEXT.__objc_classname: 0x890
   __TEXT.__objc_methname: 0xcc6d

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B891C13-CC92-3777-92C8-53273AF59916
+  UUID: 5A893CCB-6CFA-3F34-93F9-D62F188B034D
   Functions: 1974
-  Symbols:   6763
-  CStrings:  4324
+  Symbols:   6765
+  CStrings:  4323
 
Functions:
~ -[_TVRCRapportDeviceManager removeDeviceImplForLinkDevice:] : 884 -> 880
~ _OUTLINED_FUNCTION_2 -> _OUTLINED_FUNCTION_1 : 20 -> 24
~ -[_TVRCRapportDeviceManager removeDeviceImplForLinkDevice:].cold.1 : 152 -> 148
~ ___31-[TVRCRapportDeviceQuery start]_block_invoke.cold.1 : 100 -> 96
~ ___31-[TVRCRapportDeviceQuery start]_block_invoke.69.cold.1 : 152 -> 148
~ ___38-[TVRCRapportDeviceQuery _deviceLost:]_block_invoke.cold.2 : 200 -> 196
CStrings:
+ "%s - device:<%p> state: %@ "
+ "%s currentDevices:%@"
+ "%s delegate:%@, %@"
+ "%s device=%@"
+ "%s deviceState:%@"
+ "%s event=%@, command=%s"
+ "%s identifier:%@, %@"
+ "%s linkDevice=%@, allIdentifiers:%@"
+ "%s newState: %@"
+ "%s previousDevice:%@"
+ "%s sortedImpls: %@"
+ "<TVRXDeviceQuery %p> Attempting to add new device %@."
+ "<TVRXDeviceQuery %p> Removed device %@."
+ "Asked to remove device we don't already know about, device=%@. devices:%@"
+ "Asking tvremoted for launchable apps for %@"
+ "Asking tvremoted to %@ finding session for %@"
+ "Asking tvremoted to add %@ to UpNext for %@"
+ "Asking tvremoted to cancel auth challenge to device %@"
+ "Asking tvremoted to close connection to device %@"
+ "Asking tvremoted to fetch UpNext infos for %@"
+ "Asking tvremoted to fetch connection status for %@"
+ "Asking tvremoted to fulfill auth challenge to device %@ and code %@"
+ "Asking tvremoted to launch app %@ for %@"
+ "Asking tvremoted to mark %@ as watched for %@"
+ "Asking tvremoted to open connection to device %@"
+ "Asking tvremoted to play media with item %@ for %@"
+ "Asking tvremoted to remove %@ from UpNext for %@"
+ "Asking tvremoted to send event with ID %@ to device %@"
+ "Attempting to remove device impl: %@"
+ "Could not create mediaSession for companionLinkClient <%@>, error - %{public}@"
+ "Creating new device impl with device=%@, deviceRecords=%@"
+ "Device changed, device=%@, wrapper=%@"
+ "Device changed: %@ attributesChanged :%s nameChanged: %s"
+ "Device details name:%{public}@, id:%@, ble:%{bool}d, wifip2p:%{bool}d, wifi:%{bool}d "
+ "Device found, device<%p> %@"
+ "Device is not connected over Infra and screen is not active, ignoring the device lost notification - device: %@"
+ "Device should be added, device<%p> %@"
+ "Device should be removed, device=%@"
+ "Device was %@ while lost, sending TVRCErrorCodeDeviceNotFoundError"
+ "Device was lost, wait to see if it returns, timeout=%f, deviceWrapper=%@, device=%@"
+ "Device was not found again, device=%@"
+ "Device will not be shown because it's now allowed by MDM! %@"
+ "Found an existing device: %@ for impl: %@"
+ "Found existing device = [%@] for device = [%@]"
+ "Informing delegate device was added: %@"
+ "Informing delegate device was lost: %@"
+ "Informing delegate to remove device=%@"
+ "MediaControlFlagsChangedHandler called for companionLinkClient <%@>"
+ "MediaControlFlagsVolume available for <%@>"
+ "MediaControlFlagsVolume not available for companionLinkClient <%@>"
+ "MediaSession activated for companionLinkClient <%@>"
+ "New state: %@"
+ "No deviceWrapper found for device id:%@ in mapping %@"
+ "Old state: %@"
+ "RPMediaControlFlagsVolume available for <%@>"
+ "RPMediaControlFlagsVolume not available for companionLinkClient <%@>"
+ "Received request response for FetchMediaControlStatus, response %@, error %{public}@"
+ "Removed %@"
+ "Removing %@ from dictionary: %@"
+ "Setting preferred device %@"
+ "Suggested deviceState %@ was never discovered previously"
+ "Supported Caption Events for current settings=%s, events=\n%@"
+ "Supported media commands \n%@"
+ "Telling device to disconnect, device=%@"
+ "Updated siriRemoteFindingState: %@"
+ "Updating UnAuth rapport device: %@"
+ "Updating deviceState: %@ for suggested device: %@"
+ "tvremoted informed us that a device's state changed - %@"
+ "tvremoted updated suggested devices - %@"
- "%s %{public}@"
- "%s - device:<%p> state: %{public}@ "
- "%s currentDevices:%{public}@"
- "%s delegate:%{public}@, %{public}@"
- "%s device=%{public}@"
- "%s deviceState:%{public}@"
- "%s event=%{public}@, command=%s"
- "%s identifier:%{public}@, %{public}@"
- "%s linkDevice=%{public}@, allIdentifiers:%{public}@"
- "%s newState: %{public}@"
- "%s previousDevice:%{public}@"
- "%s sortedImpls: %{public}@"
- "<TVRXDeviceQuery %p> Attempting to add new device %{public}@."
- "<TVRXDeviceQuery %p> Removed device %{public}@."
- "Asked to remove device we don't already know about, device=%{public}@. devices:%@"
- "Asking tvremoted for launchable apps for %{public}@"
- "Asking tvremoted to %@ finding session for %{public}@"
- "Asking tvremoted to add %@ to UpNext for %{public}@"
- "Asking tvremoted to cancel auth challenge to device %{public}@"
- "Asking tvremoted to close connection to device %{public}@"
- "Asking tvremoted to fetch UpNext infos for %{public}@"
- "Asking tvremoted to fetch connection status for %{public}@"
- "Asking tvremoted to fulfill auth challenge to device %@ and code %{public}@"
- "Asking tvremoted to launch app %{public}@ for %{public}@"
- "Asking tvremoted to mark %@ as watched for %{public}@"
- "Asking tvremoted to open connection to device %{public}@"
- "Asking tvremoted to play media with item %@ for %{public}@"
- "Asking tvremoted to remove %@ from UpNext for %{public}@"
- "Asking tvremoted to send event with ID %@ to device %{public}@"
- "Attempting to remove device impl: %{public}@"
- "Could not create mediaSession for companionLinkClient <%{public}@>, error - %{public}@"
- "Creating new device impl with device=%{public}@, deviceRecords=%{public}@"
- "Device changed, device=%{public}@, wrapper=%@"
- "Device changed: %{public}@ attributesChanged :%s nameChanged: %s"
- "Device details name:%{public}@, id:%{public}@, ble:%{bool}d, wifip2p:%{bool}d, wifi:%{bool}d "
- "Device found, device<%p> %{public}@"
- "Device is not connected over Infra and screen is not active, ignoring the device lost notification - device: %{public}@"
- "Device should be added, device<%p> %{public}@"
- "Device should be removed, device=%{public}@"
- "Device was %{public}@ while lost, sending TVRCErrorCodeDeviceNotFoundError"
- "Device was lost, wait to see if it returns, timeout=%f, deviceWrapper=%{public}@, device=%{public}@"
- "Device was not found again, device=%{public}@"
- "Device will not be shown because it's now allowed by MDM! %{public}@"
- "Found an existing device: %{public}@ for impl: %{public}@"
- "Found existing device = [%{public}@] for device = [%{public}@]"
- "Informing delegate device was added: %{public}@"
- "Informing delegate device was lost: %{public}@"
- "Informing delegate to remove device=%{public}@"
- "MediaControlFlagsChangedHandler called for companionLinkClient <%{public}@>"
- "MediaControlFlagsVolume available for <%{public}@>"
- "MediaControlFlagsVolume not available for companionLinkClient <%{public}@>"
- "MediaSession activated for companionLinkClient <%{public}@>"
- "New state: %{public}@"
- "No deviceWrapper found for device id:%{public}@ in mapping %{public}@"
- "Old state: %{public}@"
- "RPMediaControlFlagsVolume available for <%{public}@>"
- "RPMediaControlFlagsVolume not available for companionLinkClient <%{public}@>"
- "Received request response for FetchMediaControlStatus, response %{public}@, error %{public}@"
- "Removed %{public}@"
- "Removing %{public}@ from dictionary: %@"
- "Setting preferred device %{public}@"
- "Suggested deviceState %{public}@ was never discovered previously"
- "Supported Caption Events for current settings=%s, events=\n%{public}@"
- "Supported media commands \n%{public}@"
- "Telling device to disconnect, device=%{public}@"
- "Updated siriRemoteFindingState: %{public}@"
- "Updating UnAuth rapport device: %{public}@"
- "Updating deviceState: %{public}@ for suggested device: %{public}@"
- "tvremoted informed us that a device's state changed - %{public}@"
- "tvremoted updated suggested devices - %{public}@"

```
