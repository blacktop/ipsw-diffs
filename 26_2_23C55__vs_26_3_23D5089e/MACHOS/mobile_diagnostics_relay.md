## mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x12748
-  __TEXT.__auth_stubs: 0xc80
+49.80.2.0.0
+  __TEXT.__text: 0x12860
+  __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_stubs: 0x1740
-  __TEXT.__objc_methlist: 0xa84
-  __TEXT.__gcc_except_tab: 0x4e0
-  __TEXT.__objc_methname: 0x1b88
-  __TEXT.__cstring: 0x35c2
-  __TEXT.__objc_classname: 0x137
-  __TEXT.__objc_methtype: 0x893
-  __TEXT.__const: 0x40
+  __TEXT.__objc_methlist: 0xabc
+  __TEXT.__cstring: 0x364e
+  __TEXT.__gcc_except_tab: 0x448
+  __TEXT.__objc_methname: 0x1bdd
+  __TEXT.__objc_classname: 0x14b
+  __TEXT.__objc_methtype: 0x8ac
+  __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x22
   __TEXT.__ustring: 0x1b0
   __TEXT.__unwind_info: 0x468
-  __DATA_CONST.__auth_got: 0x650
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x660
-  __DATA_CONST.__cfstring: 0x27a0
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__cfstring: 0x27e0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1690
+  __DATA.__objc_const: 0x17c8
   __DATA.__objc_selrefs: 0x7d8
-  __DATA.__objc_ivar: 0xcc
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_ivar: 0xe0
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration
-  - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40217016-F5BA-31E1-B5C6-1E13F0E59BE5
-  Functions: 303
-  Symbols:   269
-  CStrings:  1174
+  UUID: 3D135FB4-06F7-30F2-895D-933C7B1E729C
+  Functions: 309
+  Symbols:   266
+  CStrings:  1188
 
Symbols:
+ _IONotificationPortCreate
+ _IONotificationPortSetDispatchQueue
+ _IOServiceAddMatchingNotification
+ _kIOMainPortDefault
- _objc_retain_x24
- _remote_device_copy_property
- _remote_device_get_type
- _remote_device_set_connected_callback
- _remote_device_set_disconnected_callback
- _remote_device_start_browsing
- _xpc_string_get_string_ptr
CStrings:
+ "(OK) Migration is already done, skip waiting notification"
+ "-[MDRUSBHubMonitor registerStateChangeNotification:callback:]"
+ "-[StateMachineController handleDidFinishReceivedEvent]_block_invoke"
+ "-[StateMachineController handleUSBHubAttachEvent]_block_invoke"
+ "-[StateMachineController handleUSBHubDetachEvent]_block_invoke"
+ "-[StateMachineController runBroadcastingDidFinishAction]"
+ "-[StateMachineController startUSBHubMonitor:]"
+ "."
+ "Broadcasting Did Finish"
+ "Event 'DidFinish Received' ignored in state <%@>"
+ "Event 'USB Hub Attach' ignored in state <%@>"
+ "Event 'USB Hub Detach' ignored in state <%@>"
+ "FATAL! Can't get product ID, exiting"
+ "FATAL! Can't start USB Hub monitor, exiting"
+ "Failed to register FirstMatch notification"
+ "Failed to register Terminated notification"
+ "I"
+ "IOServiceFirstMatch"
+ "IOServiceTerminate"
+ "IOUSBDevice"
+ "Invalid parameters: productID or callback is nil"
+ "It takes %.2f seconds to be here after transfer completed"
+ "MDRUSBHubMonitor"
+ "Recovering state <%@> from last exit"
+ "Session %@ | Empty tag UID"
+ "Session %@ | Read tag type %lu, UID: %@"
+ "USB Hub connnected"
+ "USB Hub disconnected"
+ "USB Hub monitor started for product ID: %@"
+ "Waiting migrationDidFinish notification"
+ "^{IONotificationPort=}"
+ "_attachedIter"
+ "_notifyPort"
+ "_removedIter"
+ "_usbEventQ"
+ "com.apple.MDR.usbeventQ"
+ "componentsSeparatedByString:"
+ "getProductIDFromIOEvent:"
+ "handleDidFinishReceivedEvent"
+ "handleUSBHubAttachEvent"
+ "handleUSBHubDetachEvent"
+ "idProduct"
+ "idVendor"
+ "lastObject"
+ "registerStateChangeNotification:callback:"
+ "runBroadcastingDidFinishAction"
+ "startUSBHubMonitor:"
- "%@ disconnnected"
- "(OK) %@ connnected"
- "-[StateMachineController handleRemoteDeviceAttachEvent]_block_invoke"
- "-[StateMachineController handleRemoteDeviceDetachEvent]_block_invoke"
- "-[StateMachineController startRemoteDeviceDiscovery]_block_invoke"
- "Advertising migrationDidFinish completed, exiting"
- "Device connnected: ProductType %@, UDID %@, isNCM %d"
- "Device disconnnected: ProductType %@, UDID %@, isNCM %d"
- "Event 'Remote Device Attach' ignored in state <%@>"
- "Event 'Remote Device Detach' ignored in state <%@>"
- "FATAL! Device browser is canceled"
- "Ignore device connection: already has one device connected"
- "Ignore device disconnection: not my desired one"
- "It takes %.2f seconds to be here after reboot"
- "Migration Done: %s"
- "My ProductType is %@"
- "Nothing to do for state <%@>"
- "Recovering state <%@> from last exception"
- "Session %@ | Read MIFARE tag UID: %@"
- "Start to browsing remote device ..."
- "ThinningProductType"
- "Timeout waiting for device to connect, exiting"
- "UniqueDeviceID"
- "com.apple.MDR.NCM-deviceQ"
- "decimalDigitCharacterSet"
- "getLocalProductType"
- "getRemoteProductType:"
- "getRemoteUDID:"
- "handleRemoteDeviceAttachEvent"
- "handleRemoteDeviceDetachEvent"
- "isNCMDevice:"
- "startRemoteDeviceDiscovery"
- "substringToIndex:"
- "v16@?0@\"OS_remote_device\"8"
- "v20@?0@\"OS_remote_device\"8B16"

```
