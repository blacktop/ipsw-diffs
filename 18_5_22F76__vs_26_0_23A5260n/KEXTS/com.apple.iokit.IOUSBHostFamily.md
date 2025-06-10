## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

```diff

-1402.100.21.0.0
-  __TEXT.__cstring: 0x9afc
-  __TEXT.__os_log: 0x81a1
-  __TEXT.__const: 0xa90
-  __TEXT_EXEC.__text: 0x9a850
+1493.0.6.0.0
+  __TEXT.__cstring: 0x9e0e
+  __TEXT.__os_log: 0x826b
+  __TEXT.__const: 0xb50
+  __TEXT_EXEC.__text: 0x9dda8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x310
-  __DATA.__common: 0x930
+  __DATA.__data: 0x1f0
+  __DATA.__common: 0x910
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__mod_init_func: 0xe8
-  __DATA_CONST.__mod_term_func: 0xe0
-  __DATA_CONST.__const: 0xcca8
-  __DATA_CONST.__kalloc_type: 0x1c40
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__mod_init_func: 0xe0
+  __DATA_CONST.__mod_term_func: 0xd8
+  __DATA_CONST.__const: 0xc210
+  __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 9C1745DD-4E50-30EF-9C75-1AD391DBF780
-  Functions: 1934
+  UUID: 31E8820C-93F4-3B2D-A6AE-339B5FE775C9
+  Functions: 1902
   Symbols:   0
-  CStrings:  1550
+  CStrings:  1591
 
CStrings:
+ "%s@%s: %s::%s: %s: %s@%s\n"
+ "%s@%s: %s::%s: %s: rejecting transition from off to intermediate state\n"
+ "%s@%s: %s::%s: base idle policy %d ms\n"
+ "%s@%s: %s::%s: cable override %d"
+ "%s@%s: %s::%s: child service %s (IOPort %s@%d)\n"
+ "%s@%s: %s::%s: converting domainState 0x%08lx to 0x%08x\n"
+ "%s@%s: %s::%s: device functionality blocked by transport restrictions\n"
+ "%s@%s: %s::%s: device signature missing\n"
+ "%s@%s: %s::%s: failed to create _busCurrentAllocator\n"
+ "%s@%s: %s::%s: failed to create _companionPortLock\n"
+ "%s@%s: %s::%s: failed to create _ioPortPublishNotifier\n"
+ "%s@%s: %s::%s: failed to create _transportMessageNotifier\n"
+ "%s@%s: %s::%s: failed to create _transportPublishNotifier\n"
+ "%s@%s: %s::%s: failed to create _transportTerminateNotifier\n"
+ "%s@%s: %s::%s: failed to create companion port notifier\n"
+ "%s@%s: %s::%s: failed to find host controller service\n"
+ "%s@%s: %s::%s: failed to initialize IOPortTransportState\n"
+ "%s@%s: %s::%s: forcing cable detect for %s@%s\n"
+ "%s@%s: %s::%s: found %s@%d\n"
+ "%s@%s: %s::%s: found %s@%d %s(%s)\n"
+ "%s@%s: %s::%s: ignoring %s\n"
+ "%s@%s: %s::%s: ignoring %s@%d %s(%s)\n"
+ "%s@%s: %s::%s: link training approval result %d\n"
+ "%s@%s: %s::%s: powering off\n"
+ "%s@%s: %s::%s: removing %s@%d %s(%s)\n"
+ "%s@%s: %s::%s: timed out\n"
+ "%s@%s: %s::%s: tracking %s@%d %s(%s)\n"
+ "%s@%s: %s::%s: transport no longer available\n"
+ "%s@%s: %s::%s: using %s@%d for cable type\n"
+ "%s@%s: %s::%s: waiting for link training approval\n"
+ "121111121222121211111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222"
+ "12111112122212121111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122211"
+ "121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111212112222222222222222222222222222222222222222222222222121111111222122222222"
+ "12111112122212121121111122222222222222222222222222222222222222222222222222222222222222221212112111121211222222222222222222222222222222222222222222222222212111111122212222222221212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121211"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111211222222222211122111111111111111"
+ "B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16"
+ "Device Class"
+ "Device Function"
+ "Device Protocol"
+ "Device Subclass"
+ "Manufacturer"
+ "PortNumber"
+ "PortType"
+ "Product"
+ "Product ID"
+ "Serial Number"
+ "Usb3LinkPreferred"
+ "Usb3LinkRequired"
+ "UsbIOPort"
+ "UsbIdlePolicy"
+ "UsbPowerSinkAllocation"
+ "UsbProtocol (1.x)"
+ "UsbProtocol (2.0)"
+ "UsbProtocol (3.x)"
+ "UsbProtocolCompanion (1.x)"
+ "UsbProtocolCompanion (2.0)"
+ "UsbProtocolCompanion (3.x)"
+ "Vendor ID"
+ "cableDetect_block_invoke"
+ "registerCompanionPort"
+ "registerService_block_invoke"
+ "registerService_block_invoke_2"
+ "registerService_block_invoke_3"
+ "unknown process"
+ "usb-port-current-limit"
+ "usb-port-current-policy"
+ "usb-port-location"
+ "usb-port-number"
+ "usb-port-type"
- "%s@%s: %s::%s: %llu with time %llu\n"
- "%s@%s: %s::%s: %s@%s for speed %d\n"
- "%s@%s: %s::%s: acking deferred power change\n"
- "%s@%s: %s::%s: cannot register %s@%s for speed %d since a companion port %s@%s is already registered\n"
- "%s@%s: %s::%s: controller %p (%s) usbServiceArray %p\n"
- "%s@%s: %s::%s: controller %p (%s) usbServiceArray %p  options 0x%08x\n"
- "%s@%s: %s::%s: converting domainState 0x%08lx to 0x%08lx\n"
- "%s@%s: %s::%s: deferring power change to suspend\n"
- "%s@%s: %s::%s: device is not fully functional at operational speed %d\n"
- "%s@%s: %s::%s: forClient %p (%s) options 0x%08x arg %p\n"
- "%s@%s: %s::%s: forcing suspend in 50 ms\n"
- "%s@%s: %s::%s: hardware guaranteed port %d doesn't count toward current allocations\n"
- "%s@%s: %s::%s: insufficient power to enable this port\n"
- "%s@%s: %s::%s: internal port %d doesn't count toward current allocations\n"
- "%s@%s: %s::%s: operational speed %d is not supported\n"
- "%s@%s: %s::%s: port %s@%s for speed %d\n"
- "%s@%s: %s::%s: port-current-limit %d mA\n"
- "12111112122212121111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222"
- "1211111212221212111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122211"
- "1211111212221212111212211"
- "12111112122212121121111122222222222222222222222222222222222222222222222222222222222222221212112111121211222222222222222222222222222222222222222222222222121111111222122222222"
- "1211111212221212112111112222222222222222222222222222222222222222222222222222222222222222121211211112121122222222222222222222222222222222222222222222222212111111122212222222221212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121211"
- "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112"
- "121111121222121212"
- "AppleUSBHostLegacyClient"
- "AppleUSBHostResourcesClient"
- "getCompanionPortGated"
- "getFrameNumber"
- "idlePolicy"
- "legacyDeviceInterestNotifier"
- "port"
- "port-current-limit"
- "port-type"
- "registerCompanionPortGated"
- "registerUSBHostServiceGated"
- "setPowerState"
- "site.AppleUSBHostLegacyClient"
- "site.AppleUSBHostResourcesClient"
- "site.tRegisterUSBHostServiceParameters"
- "unregisterCompanionPortGated"
- "usbServiceCallback"

```
