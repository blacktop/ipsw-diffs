## com.apple.driver.usb.AppleUSBXHCI

> `com.apple.driver.usb.AppleUSBXHCI`

```diff

-1402.100.21.0.0
-  __TEXT.__const: 0xa4
-  __TEXT.__cstring: 0x5de7
-  __TEXT.__os_log: 0x5da8
-  __TEXT_EXEC.__text: 0x586e0
+1493.0.6.0.0
+  __TEXT.__cstring: 0x553e
+  __TEXT.__os_log: 0x4fc2
+  __TEXT.__const: 0x94
+  __TEXT_EXEC.__text: 0x4f8f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x428
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x168
+  __DATA.__common: 0x3f8
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x90
-  __DATA_CONST.__const: 0x5e10
+  __DATA_CONST.__const: 0x5da0
   __DATA_CONST.__kalloc_type: 0x8c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: A0F122A7-D759-3D2E-B6D2-EEBF58E4E7AF
-  Functions: 888
+  UUID: F6A8D42A-7EE1-36DD-A167-07D5E465315A
+  Functions: 843
   Symbols:   0
-  CStrings:  908
+  CStrings:  822
 
CStrings:
+ "%s@%s: %s::%s: %llu\n"
+ "%s@%s: %s::%s: force-usb-host set in boot-args, forcing host mode\n"
+ "%x.%x"
+ "121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111212112222222222222222222222222222222222222222222222222121111111222122222222111222211112222222211111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111221111111112"
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211121122222222221112211111111111111111112"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111211222222222211122111111111111111111122"
+ "121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222111221111111111111111111222"
+ "UsbHostControllerProtocolRevision"
+ "UsbProtocol (1.x)"
+ "UsbProtocol (2.0)"
+ "UsbProtocol (3.x)"
+ "usb-port-number"
- "%s@%s: %s::%s: %llu %llu\n"
- "%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usb3host set in boot-args, forcing USB3 host mode\n"
- "%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usbdevice set in boot-args, forcing device mode\n"
- "%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usbhost set in boot-args, forcing USB2 host mode\n"
- "%s@%s: %s::%s: Class did not set _transportType"
- "%s@%s: %s::%s: Could not get _transportPublishNotifier\n"
- "%s@%s: %s::%s: Could not get matchingDict\n"
- "%s@%s: %s::%s: Port-%s@%d %s IOPortTransportState terminated\n"
- "%s@%s: %s::%s: Port-%s@%d %s ignoring new transport with no USB data role\n"
- "%s@%s: %s::%s: Port-%s@%d %s new IOPortTransportState\n"
- "%s@%s: %s::%s: Port-%s@%d %s transport state created\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (no IOPortTransportState)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (tunneled: %d, role: %s, trm: %d:%d)\n"
- "%s@%s: %s::%s: _ioPort is NULL, disabling host mode\n"
- "%s@%s: %s::%s: cable connected and power is already on, reevaluate restricted mode\n"
- "%s@%s: %s::%s: cable connected, powering on\n"
- "%s@%s: %s::%s: cable detect disabled: _cableConnected %d\n"
- "%s@%s: %s::%s: cable disconnected, no action\n"
- "%s@%s: %s::%s: cable disconnected, powering off\n"
- "%s@%s: %s::%s: device functionality blocked by transport restrictions\n"
- "%s@%s: %s::%s: device signature changed\n"
- "%s@%s: %s::%s: device signature missing\n"
- "%s@%s: %s::%s: event did not change _cableConnected (%d)\n"
- "%s@%s: %s::%s: failed to create _nextTransportStateLock\n"
- "%s@%s: %s::%s: failed to create _transportMessageNotifier\n"
- "%s@%s: %s::%s: force-usb-host set in boot-args, forcing USB2 host mode\n"
- "%s@%s: %s::%s: link training approval result %d\n"
- "%s@%s: %s::%s: provider is invalid\n"
- "%s@%s: %s::%s: transport no longer available\n"
- "%s@%s: %s::%s: transportState is invalid\n"
- "%s@%s: %s::%s: waiting for link training approval\n"
- "12111112122212121121111122222222222222222222222222222222222222222222222222222222222222221212112111121211222222222222222222222222222222222222222222222222121111111222122222222111222211112222222211111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111221111111112"
- "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112"
- "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122111122"
- "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112"
- "AppleEmbeddedUSBArbitrator-force-usb3host"
- "AppleEmbeddedUSBArbitrator-force-usbdevice"
- "AppleEmbeddedUSBArbitrator-force-usbhost"
- "Device Class"
- "Device Function"
- "Device Protocol"
- "Device Subclass"
- "Manufacturer"
- "Product"
- "Product ID"
- "Revision"
- "Serial Number"
- "USB 2.0"
- "USB 3.x"
- "UsbConnector"
- "UsbDeviceSignature"
- "Vendor ID"
- "bDeviceClass"
- "bDeviceProtocol"
- "bDeviceSubClass"
- "cableChangeOccurred"
- "enumerateDeviceComplete_block_invoke"
- "idProduct"
- "idVendor"
- "kUSBProductString"
- "kUSBSerialNumberString"
- "kUSBVendorString"
- "port"
- "port-type"
- "registerTransportNotifications"
- "transportCreated"
- "transportMessage"
- "updatePortState"
- "usb-port-companion-index"

```
