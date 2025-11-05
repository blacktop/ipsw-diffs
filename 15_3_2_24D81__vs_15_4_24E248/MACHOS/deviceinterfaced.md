## deviceinterfaced

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced`

```diff

-178.60.8.0.0
-  __TEXT.__text: 0x8758
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x520
-  __TEXT.__objc_methlist: 0x290
-  __TEXT.__const: 0x18
-  __TEXT.__oslogstring: 0x281c
-  __TEXT.__cstring: 0xa83
+205.0.0.0.0
+  __TEXT.__text: 0xe1a4
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x320
+  __TEXT.__oslogstring: 0x2d5b
+  __TEXT.__cstring: 0xd39
   __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x1198
-  __TEXT.__objc_methtype: 0x47d
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x40
+  __TEXT.__objc_methname: 0x1613
+  __TEXT.__objc_methtype: 0x65c
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x1b0
-  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_const: 0x5b0
+  __DATA.__objc_selrefs: 0x210
+  __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x50
+  __DATA.__data: 0x3
+  __DATA.__bss: 0x18
   - /Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface
   - /Library/Apple/System/Library/PrivateFrameworks/DeviceInterfaceClient.framework/Versions/A/DeviceInterfaceClient
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 792F88A9-19C3-3759-8039-B62F84E9DE97
-  Functions: 173
-  Symbols:   49
-  CStrings:  347
+  UUID: BED7747A-9EA2-3708-999C-3A4110B66E6C
+  Functions: 109
+  Symbols:   58
+  CStrings:  413
 
Symbols:
+ _dispatch_once
+ _dock_channel_probe_device_listener_iousbhost_create
+ _dock_channel_probe_kis_listener_iousbhost_create
+ _dock_channel_probe_nexus_controller_create
+ _dock_channel_probe_nexus_controller_start
+ _dock_channel_system_service_controller_ioregistry_create
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_storeStrong
CStrings:
+ "%s *rsm_channel_interface_listener_rsm_create(_rsmInterfaceManager, _rsmChannelSystemInterfaceManager, _rsmChannelSystemInterfaceController);"
+ "%s Calling setUpDockChannelProbeInterfaceWithControllerQueue"
+ "%s Calling setUpDockChannelSystemService"
+ "%s Failed _dockChannelProbeDeviceListener == NULL"
+ "%s Failed _dockChannelProbeInterfaceManager == NULL"
+ "%s Failed _dockChannelProbeKISListener == NULL"
+ "%s Failed _dockChannelProbeNexusController == NULL"
+ "%s Failed _dockChannelSystemServiceController == NULL"
+ "%s Failed _rsmChannelInterfaceListener == NULL"
+ "%s Failed _rsmChannelInterfaceManager == NULL"
+ "%s Failed _rsmChannelSystemInterfaceController == NULL"
+ "%s Failed _rsmChannelSystemInterfaceListener == NULL"
+ "%s Failed _rsmChannelSystemInterfaceManager == NULL"
+ "%s Failed device_interface_listener_register_callbacks(_dockChannelProbeDeviceListener, &dockChannelProbeInterfaceListenerCallbacks)"
+ "%s Failed device_interface_listener_register_callbacks(_dockChannelProbeKISListener, &dockChannelProbeInterfaceListenerCallbacks)"
+ "%s Failed device_interface_listener_register_callbacks(_rsmChannelSystemInterfaceListener, &rsmChannelSystemListenerInterfaceCallbacks)"
+ "%s Failed setUpDockChannelSystemService(queue)"
+ "%s Failed to create _dockChannelProbeKISListener!"
+ "%s Failed to create _dockChannelProbeNexusController!"
+ "%s Failed to create _dockChannelSystemServiceController!"
+ "%s Failed to create dockChannelProbeInterfaceManager!"
+ "%s Failed to start _dockChannelProbeNexusController!"
+ "%s Failed to start device_interface_manager_start(_rsmChannelInterfaceManager)!"
+ "%s Failed to start device_interface_manager_start(_rsmChannelSystemInterfaceManager)!"
+ "%s Failed to start dockChannelProbeDeviceListener listener!"
+ "%s Failed to start dockChannelProbeKISListener listener!"
+ "%s OS is supported: %d"
+ "%s Starting to listen on all interfaces"
+ "%s _dockChannelInterfaceListener = dock_channel_interface_listener_kis_pam_create(_kisInterfaceManager, _dockChannelProbeNexusController);"
+ "%s _dockChannelProbeDeviceListener = dock_channel_probe_device_listener_iousbhost_create();"
+ "%s _dockChannelProbeKISListener = dock_channel_probe_kis_listener_iousbhost_create();"
+ "%s _dockChannelProbeNexusController = dock_channel_probe_nexus_controller_create(_dockChannelSystemServiceController, controllerQueue)"
+ "%s _dockChannelSystemServiceController = dock_channel_system_service_controller_ioregistry_create(queue)"
+ "%s controllerQueue != nil failed!"
+ "%s controllerQueue %@ managerQueue %@"
+ "%s deviceQueue != nil failed!"
+ "%s device_interface_listener_register_callbacks(_dockChannelProbeDeviceListener, &dockChannelProbeInterfaceListenerCallbacks);"
+ "%s device_interface_listener_register_callbacks(_dockChannelProbeKISListener, &dockChannelProbeInterfaceListenerCallbacks);"
+ "%s deviceinterfaced enabled: %d"
+ "%s dock channels enabled: %d"
+ "%s dockChannelProbeInterfaceManager = device_interface_manager_create(managerQueue);"
+ "%s external interface enabled: %d"
+ "%s managerQueue != nil failed!"
+ "%s preferences override: %d"
+ "%s rsm enabled: %d"
+ "%s starting listening on dockChannelProbeDeviceListener;"
+ "%s starting listening on dockChannelProbeKISListener;"
+ "-[DeviceInterfaceArbitrator setUpDockChannelProbeInterfaceWithControllerQueue:managerQueue:deviceQueue:]"
+ "-[DeviceInterfaceArbitrator setUpDockChannelSystemService:]"
+ "B40@0:8@16@24@32"
+ "T^{device_interface_listener_t=^v^{device_interface_listener_functions_t}},V_dockChannelProbeDeviceListener"
+ "T^{device_interface_listener_t=^v^{device_interface_listener_functions_t}},V_dockChannelProbeKISListener"
+ "T^{device_interface_manager_t=^v^{device_interface_manager_functions_t}},V_dockChannelProbeInterfaceManager"
+ "T^{dock_channel_probe_nexus_controller_t=^v},V_dockChannelProbeNexusController"
+ "T^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}},V_dockChannelSystemServiceController"
+ "^{dock_channel_probe_nexus_controller_t=^v}"
+ "^{dock_channel_probe_nexus_controller_t=^v}16@0:8"
+ "^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}"
+ "^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@0:8"
+ "_dockChannelProbeDeviceListener"
+ "_dockChannelProbeInterfaceManager"
+ "_dockChannelProbeKISListener"
+ "_dockChannelProbeNexusController"
+ "_dockChannelSystemServiceController"
+ "dockChannelProbeDeviceListener"
+ "dockChannelProbeDeviceListener_deviceinterfaced_queue"
+ "dockChannelProbeInterfaceManager"
+ "dockChannelProbeKISListener"
+ "dockChannelProbeKISListener_deviceinterfaced_queue"
+ "dockChannelProbeListenerDiscoveryCallback"
+ "dockChannelProbeListenerTerminationCallback"
+ "dockChannelProbeNexusController"
+ "dockChannelSystemServiceController"
+ "enable_deviceinterfaced"
+ "enable_dockchannels_block_invoke"
+ "enable_externalInterface_block_invoke"
+ "enable_rsm_block_invoke"
+ "setDockChannelProbeDeviceListener:"
+ "setDockChannelProbeInterfaceManager:"
+ "setDockChannelProbeKISListener:"
+ "setDockChannelProbeNexusController:"
+ "setDockChannelSystemServiceController:"
+ "setUpDockChannelProbeInterfaceWithControllerQueue:managerQueue:deviceQueue:"
+ "setUpDockChannelProbeInterface_controller_deviceinterfaced_queue"
+ "setUpDockChannelProbeInterface_device_deviceinterfaced_queue"
+ "setUpDockChannelProbeInterface_manager_deviceinterfaced_queue"
+ "setUpDockChannelSystemService:"
+ "setUpDockChannelSystemService_deviceinterfaced_queue"
+ "v24@0:8^{dock_channel_probe_nexus_controller_t=^v}16"
+ "v24@0:8^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16"
+ "v8@?0"
- "%s *rsm_channel_interface_listener_rsm_create(self.rsmInterfaceManager, self.rsmChannelSystemInterfaceManager, self.rsmChannelSystemInterfaceController);"
- "%s Detected \"defaults write com.apple.deviceinterfaced EnableDeviceInterfaceDaemon -bool YES\" is set, using deviceinterfaced"
- "%s Detected \"defaults write com.apple.deviceinterfaced EnableDockChannels -bool YES\" is set, using dock channels"
- "%s Detected \"defaults write com.apple.deviceinterfaced EnableExternalInterface -bool YES\" is set, using external interface"
- "%s Failed device_interface_listener_register_callbacks(self.rsmChannelSystemInterfaceListener, &rsmChannelSystemListenerInterfaceCallbacks)"
- "%s Failed rsmChannelInterfaceListener == NULL"
- "%s Failed rsmChannelInterfaceManager == NULL"
- "%s Failed rsmChannelSystemInterfaceController == NULL"
- "%s Failed rsmChannelSystemInterfaceListener == NULL"
- "%s Failed rsmChannelSystemInterfaceManager == NULL"
- "%s Failed to start device_interface_manager_start(self.rsmChannelInterfaceManager)!"
- "%s Failed to start device_interface_manager_start(self.rsmChannelSystemInterfaceManager)!"
- "%s Starting to listen on all interfaces with tadfuManager %s"
- "%s _dockChannelInterfaceListener = dock_channel_interface_listener_kis_pam_create(_kisInterfaceManager, _dockChannelSerialInterfaceController);"
- "%s _dockChannelSerialInterfaceListener != NULL failed!"
- "%s self.debugUSBDeviceListener != NULL failed!"
- "%s self.debugUSBInterfaceListener != NULL failed!"
- "%s self.externalInterfaceListener != NULL failed!"
- "%s self.kisInterfaceListener != NULL failed!"
- "%s self.rsmChannelInterfaceListener != NULL failed!"
- "%s self.rsmChannelSystemInterfaceListener != NULL failed!"
- "%s self.rsmInterfaceListener != NULL failed!"
- "%s self.tadfuInterfaceListener != NULL failed!"
- "%s supported %d"
- "is_deviceinterfaced_enabled"

```
