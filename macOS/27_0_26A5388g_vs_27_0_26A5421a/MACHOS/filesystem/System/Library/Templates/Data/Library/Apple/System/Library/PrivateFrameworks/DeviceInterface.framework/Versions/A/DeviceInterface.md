## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__AUTH.__data`
- `__DATA.__objc_protorefs`
- `__DATA.__data`

```diff

-291.0.0.0.0
-  __TEXT.__text: 0x8c01c
-  __TEXT.__objc_methlist: 0x7034
+294.0.0.0.0
+  __TEXT.__text: 0x8b6c4
+  __TEXT.__objc_methlist: 0x6f3c
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x9ca8
+  __TEXT.__cstring: 0x9b1d
   __TEXT.__gcc_except_tab: 0x470
   __TEXT.__oslogstring: 0x49
-  __TEXT.__unwind_info: 0x1278
+  __TEXT.__unwind_info: 0x1250
   __TEXT.__eh_frame: 0xd4
-  __TEXT.__objc_stubs: 0x7d80
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_classname: 0x100e
-  __TEXT.__objc_methname: 0xf89f
-  __TEXT.__objc_methtype: 0x5c87
+  __TEXT.__objc_stubs: 0x7d40
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_classname: 0xf93
+  __TEXT.__objc_methname: 0xf2ae
+  __TEXT.__objc_methtype: 0x55b0
   __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29b8
+  __DATA_CONST.__objc_selrefs: 0x2978
   __DATA_CONST.__got: 0x90
-  __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x860
-  __AUTH_CONST.__objc_const: 0xf138
-  __AUTH_CONST.__auth_got: 0x480
-  __AUTH.__objc_data: 0x2440
+  __AUTH_CONST.__const: 0x850
+  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__objc_const: 0xee28
+  __AUTH_CONST.__auth_got: 0x488
+  __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x5a0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x438
-  __DATA.__objc_superrefs: 0x390
-  __DATA.__objc_ivar: 0xcd4
+  __DATA.__objc_classrefs: 0x430
+  __DATA.__objc_superrefs: 0x388
+  __DATA.__objc_ivar: 0xca0
   __DATA.__data: 0x580
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 2920
-  Symbols:   5958
-  CStrings:  3690
+  Functions: 2900
+  Symbols:   5914
+  CStrings:  3654
 
Symbols:
+ +[SystemServiceIOService getIOServiceFromSystemService:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost .cxx_destruct]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost cleanupClient:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost createClientWithDescription:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost getID:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost initWithService:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost interfaceID]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost performCleanup]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost service]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost startWithCompletion:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost stopWithCompletion:]
+ -[DebugUSBDeviceConfigurationInterfaceIOUSBHost transaction]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost .cxx_destruct]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost active]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost discoveryCallback]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost discoveryContext]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost discoveryIterator]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost handleDiscoveredService:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost handleTerminatedService:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost init]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost interestNotificationMap]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost interfaceMap]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost matchingDictionary]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost notificationPort]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost notificationQueue]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost performCleanup]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost setDiscoveryCallback:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost setDiscoveryContext:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost setTerminationCallback:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost setTerminationContext:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost startListeningOnQueue:]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost stopListening]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost terminationCallback]
+ -[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost terminationContext]
+ -[DebugUSBInterfaceIOUSBHost copyDeviceTransportService]
+ -[DebugUSBInterfaceIOUSBHost getSerialNumber:length:]
+ -[DebugUSBInterfaceIOUSBHost reset]
+ -[DebugUSBInterfaceIOUSBHostClient copyDeviceTransportService]
+ -[DebugUSBInterfaceIOUSBHostClient getSerialNumber:length:]
+ -[DebugUSBInterfaceIOUSBHostClient reset]
+ -[DockChannelProbeDeviceHubListenerIOUSBHost cleanupInterestNotificationForServiceID:]
+ -[DockChannelProbeDeviceHubListenerIOUSBHost handleConfiguredCaptiveAppleDeviceService:]
+ -[DockChannelProbeDeviceMatching initWithVendorID:productID:serialPrefix:]
+ -[KISInterfaceDebugUSB initWithDebugUSBInterface:interfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:]
+ -[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:]
+ -[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManagerClient:kisSnifferController:pushEndpointBufferCount:resetDelayMS:]
+ -[SystemServiceClientWrapper .cxx_destruct]
+ -[SystemServiceClientWrapper client]
+ -[SystemServiceClientWrapper dealloc]
+ -[SystemServiceClientWrapper initWithService:description:]
+ -[SystemServiceClientWrapper registerCallbacks:]
+ -[SystemServiceClientWrapper serviceWrapper]
+ -[SystemServiceClientWrapper service]
+ -[SystemServiceClientWrapper startListening]
+ -[SystemServiceClientWrapper stopListening]
+ -[SystemServiceControllerIORegistry .cxx_destruct]
+ -[SystemServiceControllerIORegistry createSystemServiceFromIOService:]
+ -[SystemServiceControllerIORegistry createSystemServiceFromServiceID:]
+ -[SystemServiceControllerIORegistry findChildrenForService:children:count:]
+ -[SystemServiceControllerIORegistry findParentForService:parent:]
+ -[SystemServiceControllerIORegistry initWithQueue:]
+ -[SystemServiceControllerIORegistry performCleanup]
+ -[SystemServiceControllerIORegistry queue]
+ -[SystemServiceIOService .cxx_destruct]
+ -[SystemServiceIOService cleanupClient:]
+ -[SystemServiceIOService createClientWithDescription:]
+ -[SystemServiceIOService createServicePointer]
+ -[SystemServiceIOService getServiceClass:]
+ -[SystemServiceIOService getServiceID:]
+ -[SystemServiceIOService initWithService:queue:]
+ -[SystemServiceIOService performCleanup]
+ -[SystemServiceIOService queue]
+ -[SystemServiceIOService serviceClass]
+ -[SystemServiceIOService serviceID]
+ -[SystemServiceIOService service]
+ -[SystemServiceUSBDeviceClientWrapper deviceClass]
+ -[SystemServiceUSBDeviceClientWrapper getCurrentConfiguration:]
+ -[SystemServiceUSBDeviceClientWrapper getPlatformCapabilityDescriptor:size:uuid:]
+ -[SystemServiceUSBDeviceClientWrapper getProductName:length:]
+ -[SystemServiceUSBDeviceClientWrapper getSerialNumber:length:]
+ -[SystemServiceUSBDeviceClientWrapper getStringDescriptorAtIndex:string:length:]
+ -[SystemServiceUSBDeviceClientWrapper initWithService:description:]
+ -[SystemServiceUSBDeviceClientWrapper location]
+ -[SystemServiceUSBDeviceClientWrapper pid]
+ -[SystemServiceUSBDeviceClientWrapper portType]
+ -[SystemServiceUSBDeviceClientWrapper reset]
+ -[SystemServiceUSBDeviceClientWrapper usbDeviceClient]
+ -[SystemServiceUSBDeviceClientWrapper vid]
+ -[SystemServiceUSBDeviceIOUSBHost .cxx_destruct]
+ -[SystemServiceUSBDeviceIOUSBHost clientDescription]
+ -[SystemServiceUSBDeviceIOUSBHost dealloc]
+ -[SystemServiceUSBDeviceIOUSBHost getBcdUSB:]
+ -[SystemServiceUSBDeviceIOUSBHost getClass:]
+ -[SystemServiceUSBDeviceIOUSBHost getCurrentConfiguration:]
+ -[SystemServiceUSBDeviceIOUSBHost getLocation:]
+ -[SystemServiceUSBDeviceIOUSBHost getPID:]
+ -[SystemServiceUSBDeviceIOUSBHost getPlatformCapabilityDescriptor:size:uuid:]
+ -[SystemServiceUSBDeviceIOUSBHost getPortType:]
+ -[SystemServiceUSBDeviceIOUSBHost getProductName:length:]
+ -[SystemServiceUSBDeviceIOUSBHost getSerialNumber:length:]
+ -[SystemServiceUSBDeviceIOUSBHost getStringDescriptorAtIndex:string:length:]
+ -[SystemServiceUSBDeviceIOUSBHost getVID:]
+ -[SystemServiceUSBDeviceIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[SystemServiceUSBDeviceIOUSBHost initWithService:serviceID:description:queue:]
+ -[SystemServiceUSBDeviceIOUSBHost interestNotificationObject]
+ -[SystemServiceUSBDeviceIOUSBHost notificationPort]
+ -[SystemServiceUSBDeviceIOUSBHost notificationsActive]
+ -[SystemServiceUSBDeviceIOUSBHost queue]
+ -[SystemServiceUSBDeviceIOUSBHost registerCallbacks:]
+ -[SystemServiceUSBDeviceIOUSBHost reset]
+ -[SystemServiceUSBDeviceIOUSBHost serviceID]
+ -[SystemServiceUSBDeviceIOUSBHost service]
+ -[SystemServiceUSBDeviceIOUSBHost startListening]
+ -[SystemServiceUSBDeviceIOUSBHost stopListening]
+ -[SystemServiceUSBDeviceIOUSBHost terminationCallback]
+ -[SystemServiceUSBDeviceIOUSBHost terminationContext]
+ -[SystemServiceUSBHostPortClientWrapper initWithService:description:]
+ -[SystemServiceUSBHostPortClientWrapper location]
+ -[SystemServiceUSBHostPortClientWrapper usbHostPortClient]
+ -[SystemServiceUSBHostPortIOUSBHost .cxx_destruct]
+ -[SystemServiceUSBHostPortIOUSBHost clientDescription]
+ -[SystemServiceUSBHostPortIOUSBHost dealloc]
+ -[SystemServiceUSBHostPortIOUSBHost getLocation:]
+ -[SystemServiceUSBHostPortIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[SystemServiceUSBHostPortIOUSBHost initWithService:serviceID:description:queue:]
+ -[SystemServiceUSBHostPortIOUSBHost interestNotificationObject]
+ -[SystemServiceUSBHostPortIOUSBHost notificationPort]
+ -[SystemServiceUSBHostPortIOUSBHost notificationsActive]
+ -[SystemServiceUSBHostPortIOUSBHost queue]
+ -[SystemServiceUSBHostPortIOUSBHost registerCallbacks:]
+ -[SystemServiceUSBHostPortIOUSBHost serviceID]
+ -[SystemServiceUSBHostPortIOUSBHost service]
+ -[SystemServiceUSBHostPortIOUSBHost startListening]
+ -[SystemServiceUSBHostPortIOUSBHost stopListening]
+ -[SystemServiceUSBHostPortIOUSBHost terminationCallback]
+ -[SystemServiceUSBHostPortIOUSBHost terminationContext]
+ -[SystemServiceUSBHubPortClientWrapper initWithService:description:]
+ -[SystemServiceUSBHubPortClientWrapper location]
+ -[SystemServiceUSBHubPortClientWrapper portNumber]
+ -[SystemServiceUSBHubPortClientWrapper usbHubPortClient]
+ -[SystemServiceUSBHubPortIOUSBHost .cxx_destruct]
+ -[SystemServiceUSBHubPortIOUSBHost clientDescription]
+ -[SystemServiceUSBHubPortIOUSBHost dealloc]
+ -[SystemServiceUSBHubPortIOUSBHost getLocation:]
+ -[SystemServiceUSBHubPortIOUSBHost getPortNumber:]
+ -[SystemServiceUSBHubPortIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[SystemServiceUSBHubPortIOUSBHost initWithService:serviceID:description:queue:]
+ -[SystemServiceUSBHubPortIOUSBHost interestNotificationObject]
+ -[SystemServiceUSBHubPortIOUSBHost location]
+ -[SystemServiceUSBHubPortIOUSBHost notificationPort]
+ -[SystemServiceUSBHubPortIOUSBHost notificationsActive]
+ -[SystemServiceUSBHubPortIOUSBHost queue]
+ -[SystemServiceUSBHubPortIOUSBHost registerCallbacks:]
+ -[SystemServiceUSBHubPortIOUSBHost serviceID]
+ -[SystemServiceUSBHubPortIOUSBHost service]
+ -[SystemServiceUSBHubPortIOUSBHost startListening]
+ -[SystemServiceUSBHubPortIOUSBHost stopListening]
+ -[SystemServiceUSBHubPortIOUSBHost terminationCallback]
+ -[SystemServiceUSBHubPortIOUSBHost terminationContext]
+ -[SystemServiceWrapper createClientWithDescription:]
+ -[SystemServiceWrapper createUSBDeviceClientWithDescription:]
+ -[SystemServiceWrapper createUSBHostPortClientWithDescription:]
+ -[SystemServiceWrapper createUSBHubPortClientWithDescription:]
+ -[SystemServiceWrapper dealloc]
+ -[SystemServiceWrapper initWithService:transferOwnership:]
+ -[SystemServiceWrapper serviceClass]
+ -[SystemServiceWrapper serviceID]
+ -[SystemServiceWrapper service]
+ -[SystemServiceWrapper transferredOwnership]
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost._interfaceID
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost._service
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost._transaction
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._active
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._discoveryIterator
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._interestNotificationMap
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._interfaceMap
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._matchingDictionary
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._notificationPort
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost._notificationQueue
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost.discoveryCallback
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost.discoveryContext
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost.terminationCallback
+ OBJC_IVAR_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost.terminationContext
+ OBJC_IVAR_$_SystemServiceClientWrapper._client
+ OBJC_IVAR_$_SystemServiceClientWrapper._service
+ OBJC_IVAR_$_SystemServiceClientWrapper._serviceWrapper
+ OBJC_IVAR_$_SystemServiceControllerIORegistry._queue
+ OBJC_IVAR_$_SystemServiceIOService._queue
+ OBJC_IVAR_$_SystemServiceIOService._service
+ OBJC_IVAR_$_SystemServiceIOService._serviceClass
+ OBJC_IVAR_$_SystemServiceIOService._serviceID
+ OBJC_IVAR_$_SystemServiceUSBDeviceClientWrapper._deviceClass
+ OBJC_IVAR_$_SystemServiceUSBDeviceClientWrapper._location
+ OBJC_IVAR_$_SystemServiceUSBDeviceClientWrapper._pid
+ OBJC_IVAR_$_SystemServiceUSBDeviceClientWrapper._portType
+ OBJC_IVAR_$_SystemServiceUSBDeviceClientWrapper._usbDeviceClient
+ OBJC_IVAR_$_SystemServiceUSBDeviceClientWrapper._vid
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._clientDescription
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._interestNotificationObject
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._notificationPort
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._notificationsActive
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._queue
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._service
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._serviceID
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._terminationCallback
+ OBJC_IVAR_$_SystemServiceUSBDeviceIOUSBHost._terminationContext
+ OBJC_IVAR_$_SystemServiceUSBHostPortClientWrapper._location
+ OBJC_IVAR_$_SystemServiceUSBHostPortClientWrapper._usbHostPortClient
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._clientDescription
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._interestNotificationObject
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._notificationPort
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._notificationsActive
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._queue
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._service
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._serviceID
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._terminationCallback
+ OBJC_IVAR_$_SystemServiceUSBHostPortIOUSBHost._terminationContext
+ OBJC_IVAR_$_SystemServiceUSBHubPortClientWrapper._location
+ OBJC_IVAR_$_SystemServiceUSBHubPortClientWrapper._portNumber
+ OBJC_IVAR_$_SystemServiceUSBHubPortClientWrapper._usbHubPortClient
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._clientDescription
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._interestNotificationObject
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._location
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._notificationPort
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._notificationsActive
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._queue
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._service
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._serviceID
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._terminationCallback
+ OBJC_IVAR_$_SystemServiceUSBHubPortIOUSBHost._terminationContext
+ OBJC_IVAR_$_SystemServiceWrapper._service
+ OBJC_IVAR_$_SystemServiceWrapper._serviceClass
+ OBJC_IVAR_$_SystemServiceWrapper._serviceID
+ OBJC_IVAR_$_SystemServiceWrapper._transferredOwnership
+ _OBJC_CLASS_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ _OBJC_CLASS_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ _OBJC_CLASS_$_SystemServiceClientWrapper
+ _OBJC_CLASS_$_SystemServiceControllerIORegistry
+ _OBJC_CLASS_$_SystemServiceIOService
+ _OBJC_CLASS_$_SystemServiceUSBDeviceClientWrapper
+ _OBJC_CLASS_$_SystemServiceUSBDeviceIOUSBHost
+ _OBJC_CLASS_$_SystemServiceUSBHostPortClientWrapper
+ _OBJC_CLASS_$_SystemServiceUSBHostPortIOUSBHost
+ _OBJC_CLASS_$_SystemServiceUSBHubPortClientWrapper
+ _OBJC_CLASS_$_SystemServiceUSBHubPortIOUSBHost
+ _OBJC_CLASS_$_SystemServiceWrapper
+ _OBJC_METACLASS_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ _OBJC_METACLASS_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ _OBJC_METACLASS_$_SystemServiceClientWrapper
+ _OBJC_METACLASS_$_SystemServiceControllerIORegistry
+ _OBJC_METACLASS_$_SystemServiceIOService
+ _OBJC_METACLASS_$_SystemServiceUSBDeviceClientWrapper
+ _OBJC_METACLASS_$_SystemServiceUSBDeviceIOUSBHost
+ _OBJC_METACLASS_$_SystemServiceUSBHostPortClientWrapper
+ _OBJC_METACLASS_$_SystemServiceUSBHostPortIOUSBHost
+ _OBJC_METACLASS_$_SystemServiceUSBHubPortClientWrapper
+ _OBJC_METACLASS_$_SystemServiceUSBHubPortIOUSBHost
+ _OBJC_METACLASS_$_SystemServiceWrapper
+ __OBJC_$_CLASS_METHODS_SystemServiceIOService
+ __OBJC_$_INSTANCE_METHODS_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_SystemServiceClientWrapper
+ __OBJC_$_INSTANCE_METHODS_SystemServiceControllerIORegistry
+ __OBJC_$_INSTANCE_METHODS_SystemServiceIOService
+ __OBJC_$_INSTANCE_METHODS_SystemServiceUSBDeviceClientWrapper
+ __OBJC_$_INSTANCE_METHODS_SystemServiceUSBDeviceIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_SystemServiceUSBHostPortClientWrapper
+ __OBJC_$_INSTANCE_METHODS_SystemServiceUSBHostPortIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_SystemServiceUSBHubPortClientWrapper
+ __OBJC_$_INSTANCE_METHODS_SystemServiceUSBHubPortIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_SystemServiceWrapper
+ __OBJC_$_INSTANCE_VARIABLES_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceControllerIORegistry
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceIOService
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceUSBDeviceClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceUSBDeviceIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceUSBHostPortClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceUSBHostPortIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceUSBHubPortClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceUSBHubPortIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_SystemServiceWrapper
+ __OBJC_$_PROP_LIST_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ __OBJC_$_PROP_LIST_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ __OBJC_$_PROP_LIST_SystemServiceClientWrapper
+ __OBJC_$_PROP_LIST_SystemServiceControllerIORegistry
+ __OBJC_$_PROP_LIST_SystemServiceIOService
+ __OBJC_$_PROP_LIST_SystemServiceUSBDeviceClientWrapper
+ __OBJC_$_PROP_LIST_SystemServiceUSBDeviceIOUSBHost
+ __OBJC_$_PROP_LIST_SystemServiceUSBHostPortClientWrapper
+ __OBJC_$_PROP_LIST_SystemServiceUSBHostPortIOUSBHost
+ __OBJC_$_PROP_LIST_SystemServiceUSBHubPortClientWrapper
+ __OBJC_$_PROP_LIST_SystemServiceUSBHubPortIOUSBHost
+ __OBJC_$_PROP_LIST_SystemServiceWrapper
+ __OBJC_CLASS_PROTOCOLS_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ __OBJC_CLASS_PROTOCOLS_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ __OBJC_CLASS_RO_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ __OBJC_CLASS_RO_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ __OBJC_CLASS_RO_$_SystemServiceClientWrapper
+ __OBJC_CLASS_RO_$_SystemServiceControllerIORegistry
+ __OBJC_CLASS_RO_$_SystemServiceIOService
+ __OBJC_CLASS_RO_$_SystemServiceUSBDeviceClientWrapper
+ __OBJC_CLASS_RO_$_SystemServiceUSBDeviceIOUSBHost
+ __OBJC_CLASS_RO_$_SystemServiceUSBHostPortClientWrapper
+ __OBJC_CLASS_RO_$_SystemServiceUSBHostPortIOUSBHost
+ __OBJC_CLASS_RO_$_SystemServiceUSBHubPortClientWrapper
+ __OBJC_CLASS_RO_$_SystemServiceUSBHubPortIOUSBHost
+ __OBJC_CLASS_RO_$_SystemServiceWrapper
+ __OBJC_METACLASS_RO_$_DebugUSBDeviceConfigurationInterfaceIOUSBHost
+ __OBJC_METACLASS_RO_$_DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost
+ __OBJC_METACLASS_RO_$_SystemServiceClientWrapper
+ __OBJC_METACLASS_RO_$_SystemServiceControllerIORegistry
+ __OBJC_METACLASS_RO_$_SystemServiceIOService
+ __OBJC_METACLASS_RO_$_SystemServiceUSBDeviceClientWrapper
+ __OBJC_METACLASS_RO_$_SystemServiceUSBDeviceIOUSBHost
+ __OBJC_METACLASS_RO_$_SystemServiceUSBHostPortClientWrapper
+ __OBJC_METACLASS_RO_$_SystemServiceUSBHostPortIOUSBHost
+ __OBJC_METACLASS_RO_$_SystemServiceUSBHubPortClientWrapper
+ __OBJC_METACLASS_RO_$_SystemServiceUSBHubPortIOUSBHost
+ __OBJC_METACLASS_RO_$_SystemServiceWrapper
+ ___48-[SystemServiceUSBDeviceIOUSBHost stopListening]_block_invoke
+ ___49-[SystemServiceUSBHubPortIOUSBHost stopListening]_block_invoke
+ ___50-[SystemServiceUSBHostPortIOUSBHost stopListening]_block_invoke
+ ___70-[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost stopListening]_block_invoke
+ ___79-[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost startListeningOnQueue:]_block_invoke
+ _debug_usb_device_configuration_interface_iousbhost_create
+ _debug_usb_device_configuration_interface_listener_iousbhost_create
+ _debug_usb_device_configuration_interface_listener_iousbhost_services_discovered
+ _debug_usb_device_configuration_interface_listener_iousbhost_services_interest_callback
+ _debug_usb_interface_client_copy_device_transport_service
+ _debug_usb_interface_client_reset
+ _debug_usb_interface_client_serial_number
+ _debug_usb_interface_iousbhost_copy_device_transport_service
+ _debug_usb_interface_iousbhost_reset
+ _debug_usb_interface_iousbhost_serial_number
+ _mach_port_mod_refs
+ _objc_msgSend$cleanupInterestNotificationForServiceID:
+ _objc_msgSend$copyDeviceTransportService
+ _objc_msgSend$getBcdUSB:
+ _objc_msgSend$getCurrentConfiguration:
+ _objc_msgSend$handleConfiguredCaptiveAppleDeviceService:
+ _objc_msgSend$initWithDebugUSBInterface:interfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:
+ _objc_msgSend$initWithDebugUSBInterfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:
+ _objc_msgSend$initWithDebugUSBInterfaceManagerClient:kisSnifferController:pushEndpointBufferCount:resetDelayMS:
+ _objc_msgSend$initWithService:
+ _objc_msgSend$initWithVendorID:productID:serialPrefix:
+ _system_service_class
+ _system_service_cleanup
+ _system_service_cleanup_client
+ _system_service_client_register_callbacks
+ _system_service_client_start_listening
+ _system_service_client_stop_listening
+ _system_service_controller_cleanup
+ _system_service_controller_find_children
+ _system_service_controller_find_parent
+ _system_service_controller_find_service
+ _system_service_controller_ioregistry_cleanup
+ _system_service_controller_ioregistry_create
+ _system_service_controller_ioregistry_create_service
+ _system_service_controller_ioregistry_find_children
+ _system_service_controller_ioregistry_find_parent
+ _system_service_controller_ioregistry_find_service
+ _system_service_controller_ioregistry_functions
+ _system_service_create_client
+ _system_service_id
+ _system_service_ioservice_class
+ _system_service_ioservice_cleanup
+ _system_service_ioservice_cleanup_client
+ _system_service_ioservice_create_client
+ _system_service_ioservice_functions
+ _system_service_ioservice_id
+ _system_service_usb_device_class
+ _system_service_usb_device_current_configuration
+ _system_service_usb_device_iousbhost_base_client_functions
+ _system_service_usb_device_iousbhost_class
+ _system_service_usb_device_iousbhost_cleanup
+ _system_service_usb_device_iousbhost_create
+ _system_service_usb_device_iousbhost_current_configuration
+ _system_service_usb_device_iousbhost_functions
+ _system_service_usb_device_iousbhost_location
+ _system_service_usb_device_iousbhost_pid
+ _system_service_usb_device_iousbhost_platform_capability_descriptor
+ _system_service_usb_device_iousbhost_port_type
+ _system_service_usb_device_iousbhost_product_name
+ _system_service_usb_device_iousbhost_register_callbacks_function
+ _system_service_usb_device_iousbhost_reset
+ _system_service_usb_device_iousbhost_serial_number
+ _system_service_usb_device_iousbhost_start_listening_function
+ _system_service_usb_device_iousbhost_stop_listening_function
+ _system_service_usb_device_iousbhost_string_descriptor
+ _system_service_usb_device_iousbhost_vid
+ _system_service_usb_device_location
+ _system_service_usb_device_pid
+ _system_service_usb_device_platform_capability_descriptor
+ _system_service_usb_device_port_type
+ _system_service_usb_device_product_name
+ _system_service_usb_device_reset
+ _system_service_usb_device_serial_number
+ _system_service_usb_device_service_interest_callback
+ _system_service_usb_device_string_descriptor
+ _system_service_usb_device_vid
+ _system_service_usb_host_port_iousbhost_base_client_functions
+ _system_service_usb_host_port_iousbhost_cleanup
+ _system_service_usb_host_port_iousbhost_create
+ _system_service_usb_host_port_iousbhost_functions
+ _system_service_usb_host_port_iousbhost_location
+ _system_service_usb_host_port_iousbhost_register_callbacks_function
+ _system_service_usb_host_port_iousbhost_start_listening_function
+ _system_service_usb_host_port_iousbhost_stop_listening_function
+ _system_service_usb_host_port_location
+ _system_service_usb_host_port_service_interest_callback
+ _system_service_usb_hub_port_iousbhost_base_client_functions
+ _system_service_usb_hub_port_iousbhost_cleanup
+ _system_service_usb_hub_port_iousbhost_create
+ _system_service_usb_hub_port_iousbhost_functions
+ _system_service_usb_hub_port_iousbhost_location
+ _system_service_usb_hub_port_iousbhost_port_number
+ _system_service_usb_hub_port_iousbhost_register_callbacks_function
+ _system_service_usb_hub_port_iousbhost_start_listening_function
+ _system_service_usb_hub_port_iousbhost_stop_listening_function
+ _system_service_usb_hub_port_location
+ _system_service_usb_hub_port_number
+ _system_service_usb_hub_port_service_interest_callback
- +[DockChannelProbeDeviceListenerIOUSBHost baseNameForCustomName:serialPrefix:serialNumber:]
- +[DockChannelSystemServiceIOService getIOServiceFromSystemService:]
- +[KISInterfaceListenerDebugUSB getUSBDeviceInterfaceIDWithUSBInterfaceID:withUSBInterfaceManagerClient:andSaveTo:]
- -[DebugUSBDeviceInterfaceIOUSBHost .cxx_destruct]
- -[DebugUSBDeviceInterfaceIOUSBHost cleanupClient:]
- -[DebugUSBDeviceInterfaceIOUSBHost createClientWithDescription:]
- -[DebugUSBDeviceInterfaceIOUSBHost getID:]
- -[DebugUSBDeviceInterfaceIOUSBHost getSerialNumber:length:]
- -[DebugUSBDeviceInterfaceIOUSBHost getTransportService]
- -[DebugUSBDeviceInterfaceIOUSBHost initWithService:systemServiceController:]
- -[DebugUSBDeviceInterfaceIOUSBHost interfaceID]
- -[DebugUSBDeviceInterfaceIOUSBHost performCleanup]
- -[DebugUSBDeviceInterfaceIOUSBHost reset]
- -[DebugUSBDeviceInterfaceIOUSBHost service]
- -[DebugUSBDeviceInterfaceIOUSBHost setUsbDevice:]
- -[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:]
- -[DebugUSBDeviceInterfaceIOUSBHost stopWithCompletion:]
- -[DebugUSBDeviceInterfaceIOUSBHost systemServiceController]
- -[DebugUSBDeviceInterfaceIOUSBHost transaction]
- -[DebugUSBDeviceInterfaceIOUSBHost usbDevice]
- -[DebugUSBDeviceInterfaceIOUSBHostClient .cxx_destruct]
- -[DebugUSBDeviceInterfaceIOUSBHostClient clientDescription]
- -[DebugUSBDeviceInterfaceIOUSBHostClient getSerialNumber:length:]
- -[DebugUSBDeviceInterfaceIOUSBHostClient getTransportService]
- -[DebugUSBDeviceInterfaceIOUSBHostClient initWithInterface:description:]
- -[DebugUSBDeviceInterfaceIOUSBHostClient interface]
- -[DebugUSBDeviceInterfaceIOUSBHostClient reset]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost .cxx_destruct]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost active]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost discoveryCallback]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost discoveryContext]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost discoveryIterator]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost handleDiscoveredService:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost handleTerminatedService:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost initWithSystemServiceController:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost interestNotificationMap]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost interfaceMap]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost matchingDictionary]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost notificationPort]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost notificationQueue]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost performCleanup]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost setDiscoveryCallback:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost setDiscoveryContext:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost setTerminationCallback:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost setTerminationContext:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost startListeningOnQueue:]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost stopListening]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost systemServiceController]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost terminationCallback]
- -[DebugUSBDeviceInterfaceListenerIOUSBHost terminationContext]
- -[DebugUSBInterfaceIOUSBHost getDeviceID:]
- -[DebugUSBInterfaceIOUSBHost getTransportService]
- -[DebugUSBInterfaceIOUSBHostClient getDeviceID:]
- -[DebugUSBInterfaceIOUSBHostClient getTransportService]
- -[DockChannelProbeDeviceMatching customNameDescriptorIndex]
- -[DockChannelProbeDeviceMatching initWithVendorID:productID:serialPrefix:supportsCustomName:customNameDescriptorIndex:]
- -[DockChannelProbeDeviceMatching supportsCustomName]
- -[DockChannelSystemServiceClientWrapper client]
- -[DockChannelSystemServiceClientWrapper dealloc]
- -[DockChannelSystemServiceClientWrapper initWithService:description:]
- -[DockChannelSystemServiceClientWrapper registerCallbacks:]
- -[DockChannelSystemServiceClientWrapper service]
- -[DockChannelSystemServiceClientWrapper startListening]
- -[DockChannelSystemServiceClientWrapper stopListening]
- -[DockChannelSystemServiceControllerIORegistry .cxx_destruct]
- -[DockChannelSystemServiceControllerIORegistry createSystemServiceFromIOService:]
- -[DockChannelSystemServiceControllerIORegistry createSystemServiceFromServiceID:]
- -[DockChannelSystemServiceControllerIORegistry findChildrenForService:children:count:]
- -[DockChannelSystemServiceControllerIORegistry findParentForService:parent:]
- -[DockChannelSystemServiceControllerIORegistry initWithQueue:]
- -[DockChannelSystemServiceControllerIORegistry performCleanup]
- -[DockChannelSystemServiceControllerIORegistry queue]
- -[DockChannelSystemServiceIOService .cxx_destruct]
- -[DockChannelSystemServiceIOService cleanupClient:]
- -[DockChannelSystemServiceIOService createClientWithDescription:]
- -[DockChannelSystemServiceIOService createServicePointer]
- -[DockChannelSystemServiceIOService getServiceClass:]
- -[DockChannelSystemServiceIOService getServiceID:]
- -[DockChannelSystemServiceIOService initWithService:queue:]
- -[DockChannelSystemServiceIOService performCleanup]
- -[DockChannelSystemServiceIOService queue]
- -[DockChannelSystemServiceIOService serviceClass]
- -[DockChannelSystemServiceIOService serviceID]
- -[DockChannelSystemServiceIOService service]
- -[DockChannelSystemServiceUSBDeviceClientWrapper deviceClass]
- -[DockChannelSystemServiceUSBDeviceClientWrapper getPlatformCapabilityDescriptor:size:uuid:]
- -[DockChannelSystemServiceUSBDeviceClientWrapper getProductName:length:]
- -[DockChannelSystemServiceUSBDeviceClientWrapper getSerialNumber:length:]
- -[DockChannelSystemServiceUSBDeviceClientWrapper getStringDescriptorAtIndex:string:length:]
- -[DockChannelSystemServiceUSBDeviceClientWrapper initWithService:description:]
- -[DockChannelSystemServiceUSBDeviceClientWrapper location]
- -[DockChannelSystemServiceUSBDeviceClientWrapper pid]
- -[DockChannelSystemServiceUSBDeviceClientWrapper portType]
- -[DockChannelSystemServiceUSBDeviceClientWrapper usbDeviceClient]
- -[DockChannelSystemServiceUSBDeviceClientWrapper vid]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost .cxx_destruct]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost clientDescription]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost dealloc]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getClass:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getLocation:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getPID:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getPlatformCapabilityDescriptor:size:uuid:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getPortType:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getProductName:length:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getSerialNumber:length:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getStringDescriptorAtIndex:string:length:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost getVID:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost initWithService:serviceID:description:queue:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost interestNotificationObject]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost notificationPort]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost notificationsActive]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost queue]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost registerCallbacks:]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost serviceID]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost service]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost startListening]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost stopListening]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost terminationCallback]
- -[DockChannelSystemServiceUSBDeviceIOUSBHost terminationContext]
- -[DockChannelSystemServiceUSBHostPortClientWrapper initWithService:description:]
- -[DockChannelSystemServiceUSBHostPortClientWrapper location]
- -[DockChannelSystemServiceUSBHostPortClientWrapper usbHostPortClient]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost .cxx_destruct]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost clientDescription]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost dealloc]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost getLocation:]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost initWithService:serviceID:description:queue:]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost interestNotificationObject]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost notificationPort]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost notificationsActive]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost queue]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost registerCallbacks:]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost serviceID]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost service]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost startListening]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost stopListening]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost terminationCallback]
- -[DockChannelSystemServiceUSBHostPortIOUSBHost terminationContext]
- -[DockChannelSystemServiceUSBHubPortClientWrapper initWithService:description:]
- -[DockChannelSystemServiceUSBHubPortClientWrapper location]
- -[DockChannelSystemServiceUSBHubPortClientWrapper portNumber]
- -[DockChannelSystemServiceUSBHubPortClientWrapper usbHubPortClient]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost .cxx_destruct]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost clientDescription]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost dealloc]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost getLocation:]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost getPortNumber:]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost initWithService:serviceID:description:queue:]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost interestNotificationObject]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost location]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost notificationPort]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost notificationsActive]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost queue]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost registerCallbacks:]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost serviceID]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost service]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost startListening]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost stopListening]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost terminationCallback]
- -[DockChannelSystemServiceUSBHubPortIOUSBHost terminationContext]
- -[DockChannelSystemServiceWrapper createClientWithDescription:]
- -[DockChannelSystemServiceWrapper createUSBDeviceClientWithDescription:]
- -[DockChannelSystemServiceWrapper createUSBHostPortClientWithDescription:]
- -[DockChannelSystemServiceWrapper createUSBHubPortClientWithDescription:]
- -[DockChannelSystemServiceWrapper dealloc]
- -[DockChannelSystemServiceWrapper initWithService:transferOwnership:]
- -[DockChannelSystemServiceWrapper serviceClass]
- -[DockChannelSystemServiceWrapper serviceID]
- -[DockChannelSystemServiceWrapper service]
- -[DockChannelSystemServiceWrapper transferredOwnership]
- -[KISInterfaceDebugUSB debugUSBDeviceClient]
- -[KISInterfaceDebugUSB debugUSBDeviceInterfaceID]
- -[KISInterfaceDebugUSB debugUSBDeviceInterface]
- -[KISInterfaceDebugUSB debugUSBDeviceManagerClient]
- -[KISInterfaceDebugUSB debugUSBDeviceManager]
- -[KISInterfaceDebugUSB initWithDebugUSBDevice:deviceManager:debugUSBInterface:interfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:]
- -[KISInterfaceDebugUSB setDebugUSBDeviceClient:]
- -[KISInterfaceDebugUSB setDebugUSBDeviceInterface:]
- -[KISInterfaceDebugUSB setDebugUSBDeviceManagerClient:]
- -[KISInterfaceListenerDebugUSB debugUSBDeviceManagerClient]
- -[KISInterfaceListenerDebugUSB debugUSBDeviceManager]
- -[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManager:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:]
- -[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManagerClient:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:]
- -[KISInterfaceListenerDebugUSB setDebugUSBDeviceManagerClient:]
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHost._interfaceID
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHost._service
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHost._systemServiceController
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHost._transaction
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHost._usbDevice
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHostClient._clientDescription
- OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHostClient._interface
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._active
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._discoveryIterator
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._interestNotificationMap
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._interfaceMap
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._matchingDictionary
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._notificationPort
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._notificationQueue
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost._systemServiceController
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost.discoveryCallback
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost.discoveryContext
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost.terminationCallback
- OBJC_IVAR_$_DebugUSBDeviceInterfaceListenerIOUSBHost.terminationContext
- OBJC_IVAR_$_DockChannelProbeDeviceMatching._customNameDescriptorIndex
- OBJC_IVAR_$_DockChannelProbeDeviceMatching._supportsCustomName
- OBJC_IVAR_$_DockChannelSystemServiceClientWrapper._client
- OBJC_IVAR_$_DockChannelSystemServiceClientWrapper._service
- OBJC_IVAR_$_DockChannelSystemServiceControllerIORegistry._queue
- OBJC_IVAR_$_DockChannelSystemServiceIOService._queue
- OBJC_IVAR_$_DockChannelSystemServiceIOService._service
- OBJC_IVAR_$_DockChannelSystemServiceIOService._serviceClass
- OBJC_IVAR_$_DockChannelSystemServiceIOService._serviceID
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._deviceClass
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._location
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._pid
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._portType
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._usbDeviceClient
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._vid
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._clientDescription
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._interestNotificationObject
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._notificationPort
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._notificationsActive
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._queue
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._service
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._serviceID
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._terminationCallback
- OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._terminationContext
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortClientWrapper._location
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortClientWrapper._usbHostPortClient
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._clientDescription
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._interestNotificationObject
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._notificationPort
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._notificationsActive
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._queue
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._service
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._serviceID
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._terminationCallback
- OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._terminationContext
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortClientWrapper._location
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortClientWrapper._portNumber
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortClientWrapper._usbHubPortClient
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._clientDescription
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._interestNotificationObject
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._location
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._notificationPort
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._notificationsActive
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._queue
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._service
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._serviceID
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._terminationCallback
- OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._terminationContext
- OBJC_IVAR_$_DockChannelSystemServiceWrapper._service
- OBJC_IVAR_$_DockChannelSystemServiceWrapper._serviceClass
- OBJC_IVAR_$_DockChannelSystemServiceWrapper._serviceID
- OBJC_IVAR_$_DockChannelSystemServiceWrapper._transferredOwnership
- OBJC_IVAR_$_KISInterfaceDebugUSB._debugUSBDeviceClient
- OBJC_IVAR_$_KISInterfaceDebugUSB._debugUSBDeviceInterface
- OBJC_IVAR_$_KISInterfaceDebugUSB._debugUSBDeviceInterfaceID
- OBJC_IVAR_$_KISInterfaceDebugUSB._debugUSBDeviceManager
- OBJC_IVAR_$_KISInterfaceDebugUSB._debugUSBDeviceManagerClient
- OBJC_IVAR_$_KISInterfaceListenerDebugUSB._debugUSBDeviceManager
- OBJC_IVAR_$_KISInterfaceListenerDebugUSB._debugUSBDeviceManagerClient
- _OBJC_CLASS_$_DebugUSBDeviceInterfaceIOUSBHost
- _OBJC_CLASS_$_DebugUSBDeviceInterfaceIOUSBHostClient
- _OBJC_CLASS_$_DebugUSBDeviceInterfaceListenerIOUSBHost
- _OBJC_CLASS_$_DockChannelSystemServiceClientWrapper
- _OBJC_CLASS_$_DockChannelSystemServiceControllerIORegistry
- _OBJC_CLASS_$_DockChannelSystemServiceIOService
- _OBJC_CLASS_$_DockChannelSystemServiceUSBDeviceClientWrapper
- _OBJC_CLASS_$_DockChannelSystemServiceUSBDeviceIOUSBHost
- _OBJC_CLASS_$_DockChannelSystemServiceUSBHostPortClientWrapper
- _OBJC_CLASS_$_DockChannelSystemServiceUSBHostPortIOUSBHost
- _OBJC_CLASS_$_DockChannelSystemServiceUSBHubPortClientWrapper
- _OBJC_CLASS_$_DockChannelSystemServiceUSBHubPortIOUSBHost
- _OBJC_CLASS_$_DockChannelSystemServiceWrapper
- _OBJC_METACLASS_$_DebugUSBDeviceInterfaceIOUSBHost
- _OBJC_METACLASS_$_DebugUSBDeviceInterfaceIOUSBHostClient
- _OBJC_METACLASS_$_DebugUSBDeviceInterfaceListenerIOUSBHost
- _OBJC_METACLASS_$_DockChannelSystemServiceClientWrapper
- _OBJC_METACLASS_$_DockChannelSystemServiceControllerIORegistry
- _OBJC_METACLASS_$_DockChannelSystemServiceIOService
- _OBJC_METACLASS_$_DockChannelSystemServiceUSBDeviceClientWrapper
- _OBJC_METACLASS_$_DockChannelSystemServiceUSBDeviceIOUSBHost
- _OBJC_METACLASS_$_DockChannelSystemServiceUSBHostPortClientWrapper
- _OBJC_METACLASS_$_DockChannelSystemServiceUSBHostPortIOUSBHost
- _OBJC_METACLASS_$_DockChannelSystemServiceUSBHubPortClientWrapper
- _OBJC_METACLASS_$_DockChannelSystemServiceUSBHubPortIOUSBHost
- _OBJC_METACLASS_$_DockChannelSystemServiceWrapper
- __OBJC_$_CLASS_METHODS_DockChannelProbeDeviceListenerIOUSBHost
- __OBJC_$_CLASS_METHODS_DockChannelSystemServiceIOService
- __OBJC_$_CLASS_METHODS_KISInterfaceListenerDebugUSB
- __OBJC_$_INSTANCE_METHODS_DebugUSBDeviceInterfaceIOUSBHost
- __OBJC_$_INSTANCE_METHODS_DebugUSBDeviceInterfaceIOUSBHostClient
- __OBJC_$_INSTANCE_METHODS_DebugUSBDeviceInterfaceListenerIOUSBHost
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceClientWrapper
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceControllerIORegistry
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceIOService
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBDeviceClientWrapper
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBDeviceIOUSBHost
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHostPortClientWrapper
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHostPortIOUSBHost
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHubPortClientWrapper
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHubPortIOUSBHost
- __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceWrapper
- __OBJC_$_INSTANCE_VARIABLES_DebugUSBDeviceInterfaceIOUSBHost
- __OBJC_$_INSTANCE_VARIABLES_DebugUSBDeviceInterfaceIOUSBHostClient
- __OBJC_$_INSTANCE_VARIABLES_DebugUSBDeviceInterfaceListenerIOUSBHost
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceClientWrapper
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceControllerIORegistry
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceIOService
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBDeviceClientWrapper
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBDeviceIOUSBHost
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHostPortClientWrapper
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHostPortIOUSBHost
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHubPortClientWrapper
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHubPortIOUSBHost
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceWrapper
- __OBJC_$_PROP_LIST_DebugUSBDeviceInterfaceIOUSBHost
- __OBJC_$_PROP_LIST_DebugUSBDeviceInterfaceIOUSBHostClient
- __OBJC_$_PROP_LIST_DebugUSBDeviceInterfaceListenerIOUSBHost
- __OBJC_$_PROP_LIST_DockChannelSystemServiceClientWrapper
- __OBJC_$_PROP_LIST_DockChannelSystemServiceControllerIORegistry
- __OBJC_$_PROP_LIST_DockChannelSystemServiceIOService
- __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBDeviceClientWrapper
- __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBDeviceIOUSBHost
- __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHostPortClientWrapper
- __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHostPortIOUSBHost
- __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHubPortClientWrapper
- __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHubPortIOUSBHost
- __OBJC_$_PROP_LIST_DockChannelSystemServiceWrapper
- __OBJC_CLASS_PROTOCOLS_$_DebugUSBDeviceInterfaceIOUSBHost
- __OBJC_CLASS_PROTOCOLS_$_DebugUSBDeviceInterfaceListenerIOUSBHost
- __OBJC_CLASS_RO_$_DebugUSBDeviceInterfaceIOUSBHost
- __OBJC_CLASS_RO_$_DebugUSBDeviceInterfaceIOUSBHostClient
- __OBJC_CLASS_RO_$_DebugUSBDeviceInterfaceListenerIOUSBHost
- __OBJC_CLASS_RO_$_DockChannelSystemServiceClientWrapper
- __OBJC_CLASS_RO_$_DockChannelSystemServiceControllerIORegistry
- __OBJC_CLASS_RO_$_DockChannelSystemServiceIOService
- __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBDeviceClientWrapper
- __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBDeviceIOUSBHost
- __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHostPortClientWrapper
- __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHostPortIOUSBHost
- __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHubPortClientWrapper
- __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHubPortIOUSBHost
- __OBJC_CLASS_RO_$_DockChannelSystemServiceWrapper
- __OBJC_METACLASS_RO_$_DebugUSBDeviceInterfaceIOUSBHost
- __OBJC_METACLASS_RO_$_DebugUSBDeviceInterfaceIOUSBHostClient
- __OBJC_METACLASS_RO_$_DebugUSBDeviceInterfaceListenerIOUSBHost
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceClientWrapper
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceControllerIORegistry
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceIOService
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBDeviceClientWrapper
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBDeviceIOUSBHost
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHostPortClientWrapper
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHostPortIOUSBHost
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHubPortClientWrapper
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHubPortIOUSBHost
- __OBJC_METACLASS_RO_$_DockChannelSystemServiceWrapper
- ___56-[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:]_block_invoke
- ___56-[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:]_block_invoke_2
- ___57-[DebugUSBDeviceInterfaceListenerIOUSBHost stopListening]_block_invoke
- ___59-[DockChannelSystemServiceUSBDeviceIOUSBHost stopListening]_block_invoke
- ___60-[DockChannelSystemServiceUSBHubPortIOUSBHost stopListening]_block_invoke
- ___61-[DockChannelSystemServiceUSBHostPortIOUSBHost stopListening]_block_invoke
- ___66-[DebugUSBDeviceInterfaceListenerIOUSBHost startListeningOnQueue:]_block_invoke
- _debug_usb_device_interface_client_reset
- _debug_usb_device_interface_client_serial_number
- _debug_usb_device_interface_client_transport_service
- _debug_usb_device_interface_iousbhost_client_functions
- _debug_usb_device_interface_iousbhost_create
- _debug_usb_device_interface_iousbhost_reset
- _debug_usb_device_interface_iousbhost_serial_number
- _debug_usb_device_interface_iousbhost_transport_service
- _debug_usb_device_interface_listener_iousbhost_create
- _debug_usb_device_interface_listener_iousbhost_services_discovered
- _debug_usb_device_interface_listener_iousbhost_services_interest_callback
- _debug_usb_interface_client_device_id
- _debug_usb_interface_client_transport_service
- _debug_usb_interface_iousbhost_device_id
- _debug_usb_interface_iousbhost_transport_service
- _dock_channel_system_service_class
- _dock_channel_system_service_cleanup
- _dock_channel_system_service_cleanup_client
- _dock_channel_system_service_client_register_callbacks
- _dock_channel_system_service_client_start_listening
- _dock_channel_system_service_client_stop_listening
- _dock_channel_system_service_controller_cleanup
- _dock_channel_system_service_controller_find_children
- _dock_channel_system_service_controller_find_parent
- _dock_channel_system_service_controller_find_service
- _dock_channel_system_service_controller_ioregistry_cleanup
- _dock_channel_system_service_controller_ioregistry_create
- _dock_channel_system_service_controller_ioregistry_create_service
- _dock_channel_system_service_controller_ioregistry_find_children
- _dock_channel_system_service_controller_ioregistry_find_parent
- _dock_channel_system_service_controller_ioregistry_find_service
- _dock_channel_system_service_controller_ioregistry_functions
- _dock_channel_system_service_create_client
- _dock_channel_system_service_id
- _dock_channel_system_service_ioservice_class
- _dock_channel_system_service_ioservice_cleanup
- _dock_channel_system_service_ioservice_cleanup_client
- _dock_channel_system_service_ioservice_create_client
- _dock_channel_system_service_ioservice_functions
- _dock_channel_system_service_ioservice_id
- _dock_channel_system_service_usb_device_class
- _dock_channel_system_service_usb_device_iousbhost_base_client_functions
- _dock_channel_system_service_usb_device_iousbhost_class
- _dock_channel_system_service_usb_device_iousbhost_cleanup
- _dock_channel_system_service_usb_device_iousbhost_create
- _dock_channel_system_service_usb_device_iousbhost_functions
- _dock_channel_system_service_usb_device_iousbhost_location
- _dock_channel_system_service_usb_device_iousbhost_pid
- _dock_channel_system_service_usb_device_iousbhost_platform_capability_descriptor
- _dock_channel_system_service_usb_device_iousbhost_port_type
- _dock_channel_system_service_usb_device_iousbhost_product_name
- _dock_channel_system_service_usb_device_iousbhost_register_callbacks_function
- _dock_channel_system_service_usb_device_iousbhost_serial_number
- _dock_channel_system_service_usb_device_iousbhost_start_listening_function
- _dock_channel_system_service_usb_device_iousbhost_stop_listening_function
- _dock_channel_system_service_usb_device_iousbhost_string_descriptor
- _dock_channel_system_service_usb_device_iousbhost_vid
- _dock_channel_system_service_usb_device_location
- _dock_channel_system_service_usb_device_pid
- _dock_channel_system_service_usb_device_platform_capability_descriptor
- _dock_channel_system_service_usb_device_port_type
- _dock_channel_system_service_usb_device_product_name
- _dock_channel_system_service_usb_device_serial_number
- _dock_channel_system_service_usb_device_service_interest_callback
- _dock_channel_system_service_usb_device_string_descriptor
- _dock_channel_system_service_usb_device_vid
- _dock_channel_system_service_usb_host_port_iousbhost_base_client_functions
- _dock_channel_system_service_usb_host_port_iousbhost_cleanup
- _dock_channel_system_service_usb_host_port_iousbhost_create
- _dock_channel_system_service_usb_host_port_iousbhost_functions
- _dock_channel_system_service_usb_host_port_iousbhost_location
- _dock_channel_system_service_usb_host_port_iousbhost_register_callbacks_function
- _dock_channel_system_service_usb_host_port_iousbhost_start_listening_function
- _dock_channel_system_service_usb_host_port_iousbhost_stop_listening_function
- _dock_channel_system_service_usb_host_port_location
- _dock_channel_system_service_usb_host_port_service_interest_callback
- _dock_channel_system_service_usb_hub_port_iousbhost_base_client_functions
- _dock_channel_system_service_usb_hub_port_iousbhost_cleanup
- _dock_channel_system_service_usb_hub_port_iousbhost_create
- _dock_channel_system_service_usb_hub_port_iousbhost_functions
- _dock_channel_system_service_usb_hub_port_iousbhost_location
- _dock_channel_system_service_usb_hub_port_iousbhost_port_number
- _dock_channel_system_service_usb_hub_port_iousbhost_register_callbacks_function
- _dock_channel_system_service_usb_hub_port_iousbhost_start_listening_function
- _dock_channel_system_service_usb_hub_port_iousbhost_stop_listening_function
- _dock_channel_system_service_usb_hub_port_location
- _dock_channel_system_service_usb_hub_port_number
- _dock_channel_system_service_usb_hub_port_service_interest_callback
- _objc_msgSend$baseNameForCustomName:serialPrefix:serialNumber:
- _objc_msgSend$customNameDescriptorIndex
- _objc_msgSend$debugUSBDeviceManager
- _objc_msgSend$debugUSBDeviceManagerClient
- _objc_msgSend$getDeviceID:
- _objc_msgSend$getUSBDeviceInterfaceIDWithUSBInterfaceID:withUSBInterfaceManagerClient:andSaveTo:
- _objc_msgSend$initWithDebugUSBDevice:deviceManager:debugUSBInterface:interfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:
- _objc_msgSend$initWithDebugUSBInterfaceManager:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:
- _objc_msgSend$initWithDebugUSBInterfaceManagerClient:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:
- _objc_msgSend$initWithVendorID:productID:serialPrefix:supportsCustomName:customNameDescriptorIndex:
- _objc_msgSend$setDebugUSBDeviceManagerClient:
- _objc_msgSend$supportsCustomName
CStrings:
+ "!q"
+ "%s debugUSBInterfaceManager %s kisSnifferController %s"
+ "%s debugUSBInterfaceManagerClient %s kisSnifferController %s"
+ "-%s"
+ "-[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost handleDiscoveredService:]"
+ "-[DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost handleTerminatedService:]"
+ "-[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:]"
+ "-[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManagerClient:kisSnifferController:pushEndpointBufferCount:resetDelayMS:]"
+ "@\"SystemServiceClientWrapper\""
+ "@\"SystemServiceWrapper\""
+ "@24@0:8r^{system_service_controller_t=^v^{system_service_controller_functions_t}}16"
+ "@28@0:8I16r^{system_service_controller_t=^v^{system_service_controller_functions_t}}20"
+ "@28@0:8^{system_service_t=^v^{system_service_functions_t}}16B24"
+ "@32@0:8S16S20@24"
+ "@32@0:8r^{system_service_controller_t=^v^{system_service_controller_functions_t}}16@24"
+ "@40@0:8@16^{system_service_t=^v^{system_service_functions_t}}24r^{dock_channel_probe_nexus_controller_t=^v}32"
+ "@40@0:8^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}}16^{kis_sniffer_controller_t=^v^{kis_sniffer_controller_functions_t}}24I32I36"
+ "@40@0:8^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16^{kis_sniffer_controller_t=^v^{kis_sniffer_controller_functions_t}}24I32I36"
+ "@48@0:8Q16r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}24r^{kis_sniffer_controller_t=^v^{kis_sniffer_controller_functions_t}}32I40I44"
+ "@48@0:8r^{system_service_controller_t=^v^{system_service_controller_functions_t}}16r^{dock_channel_probe_nexus_controller_t=^v}24r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}32@40"
+ "@52@0:8r^{system_service_controller_t=^v^{system_service_controller_functions_t}}16r^{dock_channel_probe_nexus_controller_t=^v}24r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}32@40B48"
+ "B24@0:8^{system_service_client_t=^v^{system_service_client_functions_t}}16"
+ "B24@0:8r^{system_service_client_callbacks_t=^?^v}16"
+ "B32@0:8^^{dock_channel_probe_nexus_t}16^^{system_service_t}24"
+ "B32@0:8r^{system_service_t=^v^{system_service_functions_t}}16^^{system_service_t}24"
+ "B40@0:8^^{dock_channel_probe_nexus_t}16^^{system_service_t}24@32"
+ "B40@0:8r^{system_service_t=^v^{system_service_functions_t}}16^^{system_service_t}24^Q32"
+ "B52@0:8^{device_interface_t=^v^{device_interface_functions_t}}16i24Q28^{system_service_t=^v^{system_service_functions_t}}36Q44"
+ "B60@0:8^{device_interface_t=^v^{device_interface_functions_t}}16i24Q28^{system_service_t=^v^{system_service_functions_t}}36Q44@52"
+ "DebugUSBDeviceConfigurationInterfaceIOUSBHost"
+ "DebugUSBDeviceConfigurationInterfaceListenerIOUSBHost"
+ "Error encountered while configuring Debug USB device: %@"
+ "Error encountered while opening Debug USB device for configuration: %@"
+ "I24@0:8r^{system_service_t=^v^{system_service_functions_t}}16"
+ "Service (id=0x%llx) not configured"
+ "SystemServiceClientWrapper"
+ "SystemServiceControllerIORegistry"
+ "SystemServiceIOService"
+ "SystemServiceUSBDeviceClientWrapper"
+ "SystemServiceUSBDeviceIOUSBHost"
+ "SystemServiceUSBHostPortClientWrapper"
+ "SystemServiceUSBHostPortIOUSBHost"
+ "SystemServiceUSBHubPortClientWrapper"
+ "SystemServiceUSBHubPortIOUSBHost"
+ "SystemServiceWrapper"
+ "T@\"SystemServiceClientWrapper\",R,N,V_pinServiceClient"
+ "T@\"SystemServiceWrapper\",&,N,V_pinService"
+ "T@\"SystemServiceWrapper\",R,N,V_pinService"
+ "T@\"SystemServiceWrapper\",R,N,V_service"
+ "T@\"SystemServiceWrapper\",R,N,V_serviceWrapper"
+ "T@\"SystemServiceWrapper\",R,N,V_transportService"
+ "T^{system_service_client_t=^v^{system_service_client_functions_t}},R,N,V_client"
+ "T^{system_service_t=^v^{system_service_functions_t}},R,N,V_service"
+ "T^{system_service_usb_device_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_device_client_functions_t}},R,N,V_usbDeviceClient"
+ "T^{system_service_usb_host_port_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_host_port_client_functions_t}},R,N,V_usbHostPortClient"
+ "T^{system_service_usb_hub_port_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_hub_port_client_functions_t}},R,N,V_usbHubPortClient"
+ "Tr^{system_service_controller_t=^v^{system_service_controller_functions_t}},R,N,V_systemServiceController"
+ "Tr^{system_service_t=^v^{system_service_functions_t}},R,N,V_service"
+ "USBDevice[0x%llx]: Error encountered while opening device for reset: %@"
+ "USBDevice[0x%llx]: Error encountered while resetting device: %@"
+ "[0x%llx] (0x%08x) Parent service is not a USB device"
+ "^{dock_channel_probe_nexus_controller_client_t=^v}32@0:8^{system_service_t=^v^{system_service_functions_t}}16r*24"
+ "^{system_service_client_t=^v^{system_service_client_functions_t}}"
+ "^{system_service_client_t=^v^{system_service_client_functions_t}}16@0:8"
+ "^{system_service_client_t=^v^{system_service_client_functions_t}}24@0:8r*16"
+ "^{system_service_t=^v^{system_service_functions_t}}"
+ "^{system_service_t=^v^{system_service_functions_t}}16@0:8"
+ "^{system_service_t=^v^{system_service_functions_t}}20@0:8I16"
+ "^{system_service_t=^v^{system_service_functions_t}}24@0:8Q16"
+ "^{system_service_usb_device_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_device_client_functions_t}}"
+ "^{system_service_usb_device_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_device_client_functions_t}}16@0:8"
+ "^{system_service_usb_host_port_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_host_port_client_functions_t}}"
+ "^{system_service_usb_host_port_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_host_port_client_functions_t}}16@0:8"
+ "^{system_service_usb_hub_port_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_hub_port_client_functions_t}}"
+ "^{system_service_usb_hub_port_client_t={system_service_client_t=^v^{system_service_client_functions_t}}^{system_service_usb_hub_port_client_functions_t}}16@0:8"
+ "_serviceWrapper"
+ "bcdUSB"
+ "cleanupInterestNotificationForServiceID:"
+ "configuredCaptiveAppleDeviceService"
+ "copyDeviceTransportService"
+ "getBcdUSB:"
+ "getCurrentConfiguration:"
+ "handleConfiguredCaptiveAppleDeviceService:"
+ "initWithDebugUSBInterface:interfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:"
+ "initWithDebugUSBInterfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:"
+ "initWithDebugUSBInterfaceManagerClient:kisSnifferController:pushEndpointBufferCount:resetDelayMS:"
+ "initWithService:"
+ "initWithVendorID:productID:serialPrefix:"
+ "kUSBCurrentConfiguration"
+ "other entity has Debug USB device, continuing anyways"
+ "r^{system_service_controller_t=^v^{system_service_controller_functions_t}}"
+ "r^{system_service_controller_t=^v^{system_service_controller_functions_t}}16@0:8"
+ "r^{system_service_t=^v^{system_service_functions_t}}"
+ "r^{system_service_t=^v^{system_service_functions_t}}16@0:8"
+ "serviceWrapper"
+ "\xae"
- "!\x91"
- "\""
- "%s debugUSBInterfaceManager %s debugUSBDeviceManager %s kisSnifferController %s"
- "%s debugUSBInterfaceManagerClient %s debugUSBDeviceManagerClient %s kisSnifferController %s"
- "%s deviceID %llu result %d"
- "%s self.debugUSBDeviceManager %s self.debugUSBDeviceManagerClient %s"
- "-[DebugUSBDeviceInterfaceListenerIOUSBHost handleDiscoveredService:]"
- "-[DebugUSBDeviceInterfaceListenerIOUSBHost handleTerminatedService:]"
- "-[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManager:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:]"
- "-[KISInterfaceListenerDebugUSB initWithDebugUSBInterfaceManagerClient:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:]"
- "@\"DebugUSBDeviceInterfaceIOUSBHost\""
- "@\"DockChannelSystemServiceClientWrapper\""
- "@\"DockChannelSystemServiceWrapper\""
- "@\"IOUSBHostDevice\""
- "@24@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16"
- "@28@0:8I16r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}20"
- "@28@0:8^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16B24"
- "@32@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@24"
- "@40@0:8@16@24@32"
- "@40@0:8@16^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}24r^{dock_channel_probe_nexus_controller_t=^v}32"
- "@40@0:8S16S20@24B32C36"
- "@48@0:8^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}}16^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}}24^{kis_sniffer_controller_t=^v^{kis_sniffer_controller_functions_t}}32I40I44"
- "@48@0:8^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}24^{kis_sniffer_controller_t=^v^{kis_sniffer_controller_functions_t}}32I40I44"
- "@48@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16r^{dock_channel_probe_nexus_controller_t=^v}24r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}32@40"
- "@52@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16r^{dock_channel_probe_nexus_controller_t=^v}24r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}32@40B48"
- "@64@0:8Q16r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}24Q32r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}40r^{kis_sniffer_controller_t=^v^{kis_sniffer_controller_functions_t}}48I56I60"
- "B24@0:8^{dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}16"
- "B24@0:8r^{dock_channel_system_service_client_callbacks_t=^?^v}16"
- "B32@0:8^^{dock_channel_probe_nexus_t}16^^{dock_channel_system_service_t}24"
- "B32@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16^^{dock_channel_system_service_t}24"
- "B40@0:8Q16^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}}24^Q32"
- "B40@0:8^^{dock_channel_probe_nexus_t}16^^{dock_channel_system_service_t}24@32"
- "B40@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16^^{dock_channel_system_service_t}24^Q32"
- "B52@0:8^{device_interface_t=^v^{device_interface_functions_t}}16i24Q28^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}36Q44"
- "B60@0:8^{device_interface_t=^v^{device_interface_functions_t}}16i24Q28^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}36Q44@52"
- "DebugUSBDeviceInterfaceIOUSBHost"
- "DebugUSBDeviceInterfaceIOUSBHostClient"
- "DebugUSBDeviceInterfaceListenerIOUSBHost"
- "DockChannelSystemServiceClientWrapper"
- "DockChannelSystemServiceControllerIORegistry"
- "DockChannelSystemServiceIOService"
- "DockChannelSystemServiceUSBDeviceClientWrapper"
- "DockChannelSystemServiceUSBDeviceIOUSBHost"
- "DockChannelSystemServiceUSBHostPortClientWrapper"
- "DockChannelSystemServiceUSBHostPortIOUSBHost"
- "DockChannelSystemServiceUSBHubPortClientWrapper"
- "DockChannelSystemServiceUSBHubPortIOUSBHost"
- "DockChannelSystemServiceWrapper"
- "Error encountered while configuring device: %@"
- "Error encountered while creating device interface for reset: %@"
- "Error encountered while creating device interface: %@"
- "Error encountered while resetting device: %@"
- "I24@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16"
- "KISInterfaceListenerDebugUSB getUSBDeviceInterfaceID"
- "KISInterfaceListenerDebugUSB: Failed to create interface client for interface ID: 0x%llx"
- "KISInterfaceListenerDebugUSB: Failed to retrieve device ID for interface ID: 0x%llx"
- "KISInterfaceListenerDebugUSBDevice"
- "T@\"DebugUSBDeviceInterfaceIOUSBHost\",R,N,V_interface"
- "T@\"DockChannelSystemServiceClientWrapper\",R,N,V_pinServiceClient"
- "T@\"DockChannelSystemServiceWrapper\",&,N,V_pinService"
- "T@\"DockChannelSystemServiceWrapper\",R,N,V_pinService"
- "T@\"DockChannelSystemServiceWrapper\",R,N,V_service"
- "T@\"DockChannelSystemServiceWrapper\",R,N,V_transportService"
- "T@\"IOUSBHostDevice\",&,N,V_usbDevice"
- "TB,R,N,V_supportsCustomName"
- "TC,R,N,V_customNameDescriptorIndex"
- "TQ,R,N,V_debugUSBDeviceInterfaceID"
- "T^{debug_usb_device_interface_client_t=^v^{debug_usb_device_interface_client_functions_t}},N,V_debugUSBDeviceClient"
- "T^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}},N,V_debugUSBDeviceManagerClient"
- "T^{device_interface_manager_t=^v^{device_interface_manager_functions_t}},R,N,V_debugUSBDeviceManager"
- "T^{dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}},R,N,V_client"
- "T^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}},R,N,V_service"
- "T^{dock_channel_system_service_usb_device_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_device_client_functions_t}},R,N,V_usbDeviceClient"
- "T^{dock_channel_system_service_usb_host_port_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_host_port_client_functions_t}},R,N,V_usbHostPortClient"
- "T^{dock_channel_system_service_usb_hub_port_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_hub_port_client_functions_t}},R,N,V_usbHubPortClient"
- "Tr^{device_interface_manager_t=^v^{device_interface_manager_functions_t}},R,N,V_debugUSBDeviceManager"
- "Tr^{device_interface_t=^v^{device_interface_functions_t}},N,V_debugUSBDeviceInterface"
- "Tr^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}},R,N,V_systemServiceController"
- "Tr^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}},R,N,V_service"
- "[0x%llx] Failed to acquire debug usb device interface"
- "[0x%llx] Failed to create debug usb device client"
- "[0x%llx] Failed to create debug usb device manager client"
- "^{debug_usb_device_interface_client_t=^v^{debug_usb_device_interface_client_functions_t}}"
- "^{debug_usb_device_interface_client_t=^v^{debug_usb_device_interface_client_functions_t}}16@0:8"
- "^{dock_channel_probe_nexus_controller_client_t=^v}32@0:8^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16r*24"
- "^{dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}"
- "^{dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}16@0:8"
- "^{dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}24@0:8r*16"
- "^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}"
- "^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16@0:8"
- "^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}20@0:8I16"
- "^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}24@0:8Q16"
- "^{dock_channel_system_service_usb_device_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_device_client_functions_t}}"
- "^{dock_channel_system_service_usb_device_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_device_client_functions_t}}16@0:8"
- "^{dock_channel_system_service_usb_host_port_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_host_port_client_functions_t}}"
- "^{dock_channel_system_service_usb_host_port_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_host_port_client_functions_t}}16@0:8"
- "^{dock_channel_system_service_usb_hub_port_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_hub_port_client_functions_t}}"
- "^{dock_channel_system_service_usb_hub_port_client_t={dock_channel_system_service_client_t=^v^{dock_channel_system_service_client_functions_t}}^{dock_channel_system_service_usb_hub_port_client_functions_t}}16@0:8"
- "_customNameDescriptorIndex"
- "_debugUSBDeviceClient"
- "_debugUSBDeviceInterface"
- "_debugUSBDeviceInterfaceID"
- "_debugUSBDeviceManager"
- "_debugUSBDeviceManagerClient"
- "_supportsCustomName"
- "_usbDevice"
- "baseNameForCustomName:serialPrefix:serialNumber:"
- "customNameDescriptorIndex"
- "debugUSBDeviceClient"
- "debugUSBDeviceInterface"
- "debugUSBDeviceInterfaceID"
- "debugUSBDeviceManager"
- "debugUSBDeviceManagerClient"
- "getDeviceID:"
- "getUSBDeviceInterfaceIDWithUSBInterfaceID:withUSBInterfaceManagerClient:andSaveTo:"
- "initWithDebugUSBDevice:deviceManager:debugUSBInterface:interfaceManager:kisSnifferController:pushEndpointBufferCount:resetDelayMS:"
- "initWithDebugUSBInterfaceManager:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:"
- "initWithDebugUSBInterfaceManagerClient:andDebugUSBDeviceManager:withKISSnifferController:pushEndpointBufferCount:resetDelayMS:"
- "initWithVendorID:productID:serialPrefix:supportsCustomName:customNameDescriptorIndex:"
- "other entity has device interface, continuing anyways"
- "r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}"
- "r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@0:8"
- "r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}"
- "r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16@0:8"
- "setDebugUSBDeviceClient:"
- "setDebugUSBDeviceInterface:"
- "setDebugUSBDeviceManagerClient:"
- "setUsbDevice:"
- "supportsCustomName"
- "usbDevice"
- "v24@0:8^{debug_usb_device_interface_client_t=^v^{debug_usb_device_interface_client_functions_t}}16"
- "\xfe"
```
