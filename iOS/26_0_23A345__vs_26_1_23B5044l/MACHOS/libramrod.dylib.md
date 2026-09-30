## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3476.2.1.0.0
-  __TEXT.__text: 0xdb2d0
-  __TEXT.__auth_stubs: 0x2830
+3476.40.18.0.2
+  __TEXT.__text: 0xdbf90
+  __TEXT.__auth_stubs: 0x2890
   __TEXT.__objc_methlist: 0x1164
-  __TEXT.__cstring: 0x288ad
-  __TEXT.__const: 0x94960
-  __TEXT.__gcc_except_tab: 0xbb4
+  __TEXT.__cstring: 0x28852
+  __TEXT.__const: 0x94940
+  __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__oslogstring: 0xab1
-  __TEXT.__unwind_info: 0x1cc8
+  __TEXT.__unwind_info: 0x1cf0
   __TEXT.__eh_frame: 0x3c0
   __TEXT.__objc_classname: 0x195
-  __TEXT.__objc_methname: 0x2901
+  __TEXT.__objc_methname: 0x290e
   __TEXT.__objc_methtype: 0xb70
-  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_stubs: 0x2860
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc90
-  __AUTH_CONST.__auth_got: 0x1430
-  __AUTH_CONST.__const: 0x1fd0
-  __AUTH_CONST.__cfstring: 0xb540
+  __DATA_CONST.__objc_selrefs: 0xc98
+  __AUTH_CONST.__auth_got: 0x1460
+  __AUTH_CONST.__const: 0x1fe0
+  __AUTH_CONST.__cfstring: 0xb640
   __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x5a0

   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x2198
-  __DATA.__bss: 0x828
+  __DATA.__bss: 0x860
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libpartition2_dynamic.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E340FA70-16AF-3020-80A7-CDAB2D2929CE
-  Functions: 2620
-  Symbols:   1800
-  CStrings:  7364
+  UUID: 4960848E-1C69-3588-BB64-6BEBE17A1B64
+  Functions: 2628
+  Symbols:   1809
+  CStrings:  7377
 
Symbols:
+ _IOUSBDeviceControllerSendCommand
+ _bus_speed_in_mbps_for_socket
+ _dispatch_assert_queue$V2
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create_with_target$V2
+ _if_indextoname
+ _objc_getAssociatedObject
+ _objc_setAssociatedObject
+ _ramrod_execute_config_set_log_output
+ _ramrod_getsockopt_int
+ _set_usb_forced_off_bus
+ _stash_USB_debug_log
+ _usb_speed_in_mbps_for_service
- _CFShow
- _IOUSBDeviceControllerCreate
- _copy_main_usb_controller
- _enable_usbmux_debug_logging
- _get_main_usb_connection_speed_in_mbps
CStrings:
+ "AppleUSBVHCIDeviceController"
+ "CHECKPOINT_INTERNAL_ERROR(%s): checkpoint engine finished out of sequence\n"
+ "DeviceState"
+ "OnBus"
+ "SIM"
+ "SelectedConfiguration"
+ "StoreDriverDebugLog"
+ "[%#llx] %@ failed: %s (%#x)\n"
+ "[%#llx] USB controller %s: %@\n"
+ "[%#llx] created %@\n"
+ "[%#llx] enabling USB finished: %s (%#x)\n"
+ "[%#llx] unable to %s bus: %s"
+ "[%#llx] unable to create USB device controller: %s (%#x)\n"
+ "[%#llx] unable to find AppleUSBDeviceMux service\n"
+ "[%#llx] unable to find USB configuration: %@\n"
+ "[%#llx] unable to register for terminate events: %s (%#x)\n"
+ "[%#llx] unable to set mux debug level: %s (%#x)\n"
+ "[%llx] unable to set USB description: %s (%#x)\n"
+ "appeared"
+ "com.apple.ramrod.IOUSBDeviceController.await"
+ "force off"
+ "go on"
+ "integerValue"
+ "terminated"
- "CHECKPOINT_INTERNAL_ERROR(%s): checkpoint engine deallocated out of sequence\n"
- "Couldn't force USB off the bus. Stubbornly continuing.\n"
- "IOServiceMatched"
- "could not allocate dictionary for usbmux properties\n"
- "could not create CFNumber for mux debug level\n"
- "device not disconnected, but done waiting: runloop_status=%d\n"
- "enabling USB%s finished: %s (%#x)\n"
- "mux 'speed' property is present but unexpected type\n"
- "mux service does not have 'speed' property\n"
- "speed"
- "unable to add interest notifications for mux service: 0x%x\n"
- "unable to find AppleUSBDeviceMux service\n"
- "unable to find USB configuration: %@\n"
- "unable to get AppleUSBDeviceMux service\n"
- "unable to get USB device controller: 0x%x\n"
- "unable to register for mux notifications\n"
- "unable to set USB description: 0x%x\n"
- "unable to set mux debug level: 0x%x\n"
- "v12@?0I8"

```
