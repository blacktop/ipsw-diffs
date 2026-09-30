## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

```diff

-228.80.6.0.0
-  __TEXT.__text: 0x7b3b4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x632c
+228.80.7.0.0
+  __TEXT.__text: 0x7d530
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x63cc
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x7e8b
-  __TEXT.__gcc_except_tab: 0x458
-  __TEXT.__unwind_info: 0x11c0
+  __TEXT.__cstring: 0x8121
+  __TEXT.__gcc_except_tab: 0x4d4
+  __TEXT.__unwind_info: 0x11d8
   __TEXT.__eh_frame: 0xfc
-  __TEXT.__objc_classname: 0xf42
-  __TEXT.__objc_methname: 0xd7a3
-  __TEXT.__objc_methtype: 0x589d
-  __TEXT.__objc_stubs: 0x6920
-  __DATA_CONST.__got: 0x50
+  __TEXT.__objc_classname: 0xf48
+  __TEXT.__objc_methname: 0xd832
+  __TEXT.__objc_methtype: 0x550a
+  __TEXT.__objc_stubs: 0x69e0
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23e8
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x700
-  __AUTH_CONST.__objc_const: 0xd840
+  __DATA_CONST.__objc_selrefs: 0x2440
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__objc_const: 0xd8a0
   __AUTH.__objc_data: 0x20d0
-  __AUTH.__data: 0x508
+  __AUTH.__data: 0x510
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x3d8
   __DATA.__objc_superrefs: 0x338
-  __DATA.__objc_ivar: 0xb38
+  __DATA.__objc_ivar: 0xb40
   __DATA.__data: 0x630
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 5BE4EA12-8540-32E0-A946-42DD44E58ED9
-  Functions: 2602
-  Symbols:   5286
-  CStrings:  3339
+  UUID: 2BCF7A56-2139-35B4-87C3-4D6E9CFD95D9
+  Functions: 2620
+  Symbols:   5318
+  CStrings:  3355
 
Symbols:
+ -[DebugUSBDeviceInterfaceListenerIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DebugUSBDeviceInterfaceListenerIOUSBHost interestNotificationMap]
+ -[DebugUSBInterfaceIOUSBHost abortTransfersOnEndpoint:]
+ -[DebugUSBInterfaceIOUSBHostClient abortTransfersOnEndpoint:]
+ -[DebugUSBInterfaceListenerIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DebugUSBInterfaceListenerIOUSBHost interestNotificationMap]
+ -[DockChannelProbeHubListenerIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DockChannelProbeHubListenerIOUSBHost interestNotificationByServiceID]
+ -[DockChannelSerialInterfaceListenerIOUserDockChannelSerial handleInterestNotificationForService:messageType:messageArgument:]
+ -[DockChannelSerialInterfaceListenerIOUserDockChannelSerial interestNotificationMap]
+ -[KISInterfaceDebugUSBBuffer performCleanup]
+ -[KISInterfaceDebugUSBInputPipe abortReads]
+ -[KISInterfaceDebugUSBInputPipe dealloc]
+ -[KISInterfaceDebugUSBInputPipe initWithInterfaceManager:interfaceID:endpointAddress:bufferCount:bufferSize:]
+ -[KISInterfaceDebugUSBInputPipe interfaceID]
+ -[KISInterfaceDebugUSBInputPipe interfaceInactive]
+ -[KISInterfaceDebugUSBInputPipe interfaceManagerClient]
+ -[KISInterfaceDebugUSBInputPipe interfaceManager]
+ -[KISInterfaceDebugUSBInputPipe interface]
+ -[KISInterfaceDebugUSBInputPipe lock]
+ -[KISInterfaceDebugUSBInputPipe performCleanup]
+ -[KISInterfaceDebugUSBInputPipe readsActive]
+ -[KISInterfaceDebugUSBInputPipe setInterfaceInactive:]
+ -[KISInterfaceDebugUSBInputPipe setInterfaceManagerClient:]
+ -[KISInterfaceDebugUSBInputPipe setReadsActive:]
+ -[KISInterfaceDebugUSBInputPipe startReads]
+ -[KISInterfaceDebugUSBInputPipe stopReads]
+ -[RSMChannelSystemInterfaceListenerAppleRSMChannel handleInterestNotificationForService:messageType:messageArgument:]
+ -[RSMChannelSystemInterfaceListenerAppleRSMChannel interestNotificationMap]
+ GCC_except_table20
+ OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._interestNotificationMap
+ OBJC_IVAR_$_DebugUSBInterfaceListenerIOUSBHost._interestNotificationMap
+ OBJC_IVAR_$_DockChannelProbeHubListenerIOUSBHost._interestNotificationByServiceID
+ OBJC_IVAR_$_DockChannelSerialInterfaceListenerIOUserDockChannelSerial._interestNotificationMap
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._interface
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._interfaceID
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._interfaceInactive
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._interfaceManager
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._interfaceManagerClient
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._lock
+ OBJC_IVAR_$_KISInterfaceDebugUSBInputPipe._readsActive
+ OBJC_IVAR_$_RSMChannelSystemInterfaceListenerAppleRSMChannel._interestNotificationMap
+ _NSCocoaErrorDomain
+ _SANDBOX_CHECK_NO_REPORT
+ __43-[TADFUTransportClient initWithConnection:]_block_invoke.68
+ __43-[TADFUTransportClient initWithConnection:]_block_invoke.73
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ _debug_usb_device_interface_listener_iousbhost_services_interest_callback
+ _debug_usb_interface_client_abort_transfers
+ _debug_usb_interface_iousbhost_abort_transfers
+ _debug_usb_interface_listener_iousbhost_services_interest_callback
+ _dock_channel_probe_hub_listener_iousbhost_hub_services_interest_callback
+ _dock_channel_serial_interface_listener_iouserdockchannelserial_services_interest_callback
+ _getpid
+ _objc_msgSend$abortReads
+ _objc_msgSend$abortTransfersOnEndpoint:
+ _objc_msgSend$abortWithOption:error:
+ _objc_msgSend$domain
+ _objc_msgSend$initWithInterfaceManager:interfaceID:endpointAddress:bufferCount:bufferSize:
+ _objc_msgSend$serviceName
+ _objc_msgSend$startReads
+ _objc_msgSend$stopReads
+ _rsm_channel_system_interface_listener_applersmchannel_services_interest_callback
+ _sandbox_check
- -[DebugUSBDeviceInterfaceIOUSBHostClient externalInterfacePointer]
- -[DebugUSBDeviceInterfaceIOUSBHostClient externalInterface]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost terminationIterator]
- -[DebugUSBInterfaceIOUSBHostClient externalInterfacePointer]
- -[DebugUSBInterfaceIOUSBHostClient externalInterface]
- -[DebugUSBInterfaceListenerIOUSBHost terminationIterator]
- -[DeviceInterface externalInterface]
- -[DockChannelProbeHubListenerIOUSBHost hubTerminationIterator]
- -[DockChannelSerialInterfaceListenerIOUserDockChannelSerial terminationIterator]
- -[ExternalInterfaceKISClient externalInterfacePointer]
- -[ExternalInterfaceKISClient externalInterface]
- -[KISInterfaceDebugUSBClient externalInterfacePointer]
- -[KISInterfaceDebugUSBClient externalInterface]
- -[KISInterfaceDebugUSBInputPipe initWithInterfaceClient:endpointAddress:bufferCount:bufferSize:]
- -[RSMChannelSystemInterfaceListenerAppleRSMChannel terminationIterator]
- GCC_except_table7
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHostClient._externalInterface
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._terminationIterator
- OBJC_IVAR_$_DebugUSBInterfaceIOUSBHostClient._externalInterface
- OBJC_IVAR_$_DebugUSBInterfaceListenerIOUSBHost._terminationIterator
- OBJC_IVAR_$_DeviceInterface._externalInterface
- OBJC_IVAR_$_DockChannelProbeHubListenerIOUSBHost._hubTerminationIterator
- OBJC_IVAR_$_DockChannelSerialInterfaceListenerIOUserDockChannelSerial._terminationIterator
- OBJC_IVAR_$_ExternalInterfaceKISClient._externalInterface
- OBJC_IVAR_$_KISInterfaceDebugUSBClient._externalInterface
- OBJC_IVAR_$_RSMChannelSystemInterfaceListenerAppleRSMChannel._terminationIterator
- _debug_usb_device_interface_listener_iousbhost_services_terminated
- _debug_usb_interface_listener_iousbhost_services_terminated
- _dock_channel_probe_hub_listener_iousbhost_hub_services_terminated
- _dock_channel_serial_interface_listener_iouserdockchannelserial_services_terminated
- _objc_msgSend$externalInterfacePointer
- _objc_msgSend$initWithInterfaceClient:endpointAddress:bufferCount:bufferSize:
- _rsm_channel_system_interface_listener_applersmchannel_terminated
CStrings:
+ "%s failed to register interest notification for service %u registryID %llu: %s (0x%x)."
+ "%s failed to register interest notification for service %u serviceID %llu: %s (0x%x)."
+ "%s forcing setupSucceeded=YES in sandboxed process"
+ "%s refcon %s"
+ "%s registered interest notification for service %u registryID %llu"
+ "%s registered interest notification for service %u serviceID %llu"
+ "%s setupSucceeded is %d, connectionInvalid is %d"
+ "-[DockChannelProbeHubListenerIOUSBHost handleDiscoveredHubService:]"
+ "-[DockChannelSerialInterfaceListenerIOUserDockChannelSerial handleDiscoveredService:]"
+ "@44@0:8r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16Q24C32I36I40"
+ "Error encountered while aborting transfers on endpoint %d: %@"
+ "KISInterfaceDebugUSBInputPipe-0x%llx-0x%x"
+ "T@\"NSMutableDictionary\",R,N,V_interestNotificationByServiceID"
+ "T@\"NSMutableDictionary\",R,N,V_interestNotificationMap"
+ "TB,N,V_interfaceInactive"
+ "TB,N,V_readsActive"
+ "T^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}},N,V_interfaceManagerClient"
+ "Tr^{device_interface_manager_t=^v^{device_interface_manager_functions_t}},R,N,V_interfaceManager"
+ "Tr^{device_interface_t=^v^{device_interface_functions_t}},R,N,V_interface"
+ "_interestNotificationByServiceID"
+ "_interestNotificationMap"
+ "_interfaceInactive"
+ "_interfaceManager"
+ "_readsActive"
+ "abortReads"
+ "abortTransfersOnEndpoint:"
+ "abortWithOption:error:"
+ "d"
+ "domain"
+ "initWithInterfaceManager:interfaceID:endpointAddress:bufferCount:bufferSize:"
+ "interestNotificationByServiceID"
+ "interestNotificationMap"
+ "interfaceInactive"
+ "interfaceManager"
+ "mach-lookup"
+ "readsActive"
+ "rsm_channel_system_interface_listener_applersmchannel_services_interest_callback"
+ "serviceName"
+ "setInterfaceInactive:"
+ "setInterfaceManagerClient:"
+ "setReadsActive:"
+ "startReads"
+ "stopReads"
+ "t"
+ "\x91"
- "%s setupSucceeded is %d"
- "@36@0:8^{debug_usb_interface_client_t=^v^{debug_usb_interface_client_functions_t}}16C24I28I32"
- "IOServiceTerminate"
- "TI,R,N,V_hubTerminationIterator"
- "TI,R,N,V_terminationIterator"
- "T{debug_usb_device_interface_client_t=^v^{debug_usb_device_interface_client_functions_t}},R,N,V_externalInterface"
- "T{debug_usb_interface_client_t=^v^{debug_usb_interface_client_functions_t}},R,N,V_externalInterface"
- "T{device_interface_t=^v^{device_interface_functions_t}},R,N,V_externalInterface"
- "T{external_interface_client_t=^v^{external_interface_client_functions_t}},R,N,V_externalInterface"
- "T{kis_interface_client_t=^v^{kis_interface_client_functions_t}},R,N,V_externalInterface"
- "^{external_interface_client_t=^v^{external_interface_client_functions_t}}16@0:8"
- "_externalInterface"
- "_hubTerminationIterator"
- "_terminationIterator"
- "externalInterface"
- "externalInterfacePointer"
- "hubTerminationIterator"
- "initWithInterfaceClient:endpointAddress:bufferCount:bufferSize:"
- "rsm_channel_system_interface_listener_applersmchannel_terminated"
- "terminationIterator"
- "{debug_usb_device_interface_client_t=\"_data\"^v\"_functions\"^{debug_usb_device_interface_client_functions_t}}"
- "{debug_usb_device_interface_client_t=^v^{debug_usb_device_interface_client_functions_t}}16@0:8"
- "{debug_usb_interface_client_t=\"_data\"^v\"_functions\"^{debug_usb_interface_client_functions_t}}"
- "{debug_usb_interface_client_t=^v^{debug_usb_interface_client_functions_t}}16@0:8"
- "{device_interface_t=\"_data\"^v\"_functions\"^{device_interface_functions_t}}"
- "{device_interface_t=^v^{device_interface_functions_t}}16@0:8"
- "{external_interface_client_t=\"_data\"^v\"_functions\"^{external_interface_client_functions_t}}"
- "{external_interface_client_t=^v^{external_interface_client_functions_t}}16@0:8"
- "{kis_interface_client_t=\"_data\"^v\"_functions\"^{kis_interface_client_functions_t}}"
- "{kis_interface_client_t=^v^{kis_interface_client_functions_t}}16@0:8"
- "\x83"

```
