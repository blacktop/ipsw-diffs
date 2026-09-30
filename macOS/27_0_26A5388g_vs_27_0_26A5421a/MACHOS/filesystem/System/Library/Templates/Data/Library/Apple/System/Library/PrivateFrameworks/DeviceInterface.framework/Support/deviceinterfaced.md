## deviceinterfaced

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-291.0.0.0.0
-  __TEXT.__text: 0x9390
+294.0.0.0.0
+  __TEXT.__text: 0x9374
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0x440
+  __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__cstring: 0x4720
+  __TEXT.__cstring: 0x4669
   __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x18b5
-  __TEXT.__objc_methtype: 0x737
+  __TEXT.__objc_methname: 0x1864
+  __TEXT.__objc_methtype: 0x6e9
   __TEXT.__unwind_info: 0x90
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x250
Symbols:
+ _debug_usb_device_configuration_interface_listener_iousbhost_create
+ _system_service_controller_ioregistry_create
- _debug_usb_device_interface_listener_iousbhost_create
- _dock_channel_system_service_controller_ioregistry_create
Functions:
~ sub_100001d74 : 1116 -> 1108
~ sub_1000029b0 -> sub_1000029a8 : 1256 -> 1236
CStrings:
+ "%s *kisInterfaceListener = kis_interface_listener_debug_usb_create_with_manager(self.debugUSBInterfaceManager, self.kisSnifferController, pushEndpointBufferCount, resetDelayMS);"
+ "%s *tadfuInterfaceListener = tadfu_interface_listener_rsm_create_with_manager(self.rsmInterfaceManager);"
+ "%s Calling setUpSystemService"
+ "%s Failed _systemServiceController == NULL"
+ "%s Failed setUpSystemService(queue)"
+ "%s Failed to create _systemServiceController!"
+ "%s _debugUSBDeviceListener = debug_usb_device_configuration_interface_listener_iousbhost_create();"
+ "%s _dockChannelProbeNexusController = dock_channel_probe_nexus_controller_create(_systemServiceController, eventQueue)"
+ "%s _systemServiceController = system_service_controller_ioregistry_create(queue)"
+ "-[DeviceInterfaceArbitrator setUpSystemService:]"
+ "T^{system_service_controller_t=^v^{system_service_controller_functions_t}},V_systemServiceController"
+ "^{system_service_controller_t=^v^{system_service_controller_functions_t}}"
+ "^{system_service_controller_t=^v^{system_service_controller_functions_t}}16@0:8"
+ "_systemServiceController"
+ "setSystemServiceController:"
+ "setUpSystemService:"
+ "setUpSystemService_deviceinterfaced_queue"
+ "systemServiceController"
+ "v24@0:8^{system_service_controller_t=^v^{system_service_controller_functions_t}}16"
- "%s *kisInterfaceListener = kis_interface_listener_debug_usb_create_with_manager(self.debugUSBInterfaceManager, self.debugUSBDeviceManager, self.kisSnifferController, pushEndpointBufferCount, resetDelayMS);"
- "%s *tadfuInterfaceListener = tadfu_interface_listener_rsm_create_with_manager(self.debugUSBInterfaceManager, self.debugUSBDeviceManager);"
- "%s Calling setUpDockChannelSystemService"
- "%s Failed _dockChannelSystemServiceController == NULL"
- "%s Failed setUpDockChannelSystemService(queue)"
- "%s Failed to create _dockChannelSystemServiceController!"
- "%s _debugUSBDeviceListener = debug_usb_device_interface_listener_iousbhost_create(_dockChannelSystemServiceController);"
- "%s _dockChannelProbeNexusController = dock_channel_probe_nexus_controller_create(_dockChannelSystemServiceController, eventQueue)"
- "%s _dockChannelSystemServiceController = dock_channel_system_service_controller_ioregistry_create(queue)"
- "-[DeviceInterfaceArbitrator setUpDockChannelSystemService:]"
- "T^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}},V_dockChannelSystemServiceController"
- "^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}"
- "^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@0:8"
- "_dockChannelSystemServiceController"
- "dockChannelSystemServiceController"
- "setDockChannelSystemServiceController:"
- "setUpDockChannelSystemService:"
- "setUpDockChannelSystemService_deviceinterfaced_queue"
- "v24@0:8^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16"
```
