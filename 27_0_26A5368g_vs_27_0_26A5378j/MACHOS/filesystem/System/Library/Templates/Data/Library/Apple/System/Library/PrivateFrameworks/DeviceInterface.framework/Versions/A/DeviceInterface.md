## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

```diff

-  __TEXT.__text: 0x8b23c
-  __TEXT.__objc_methlist: 0x6f14
+  __TEXT.__text: 0x8c168
+  __TEXT.__objc_methlist: 0x7044
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x9bce
-  __TEXT.__gcc_except_tab: 0x494
+  __TEXT.__cstring: 0x9c02
+  __TEXT.__gcc_except_tab: 0x470
   __TEXT.__oslogstring: 0x49
-  __TEXT.__unwind_info: 0x1268
+  __TEXT.__unwind_info: 0x1278
   __TEXT.__eh_frame: 0xd4
-  __TEXT.__objc_stubs: 0x7c80
+  __TEXT.__objc_stubs: 0x7da0
   __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_classname: 0x101f
-  __TEXT.__objc_methname: 0xf6a9
-  __TEXT.__objc_methtype: 0x5e27
+  __TEXT.__objc_classname: 0x100e
+  __TEXT.__objc_methname: 0xf8b4
+  __TEXT.__objc_methtype: 0x5c98
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2968
+  __DATA_CONST.__objc_selrefs: 0x29b8
   __DATA_CONST.__got: 0x90
-  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__const: 0x890
   __AUTH_CONST.__cfstring: 0x860
-  __AUTH_CONST.__objc_const: 0xef68
+  __AUTH_CONST.__objc_const: 0xf138
   __AUTH_CONST.__auth_got: 0x480
   __AUTH.__objc_data: 0x2440
-  __AUTH.__data: 0x598
+  __AUTH.__data: 0x5a8
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x438
   __DATA.__objc_superrefs: 0x390
-  __DATA.__objc_ivar: 0xcac
+  __DATA.__objc_ivar: 0xcd4
   __DATA.__data: 0x580
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 2899
-  Symbols:   5943
-  CStrings:  3752
+  Functions: 2925
+  Symbols:   5985
+  CStrings:  3778
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__objc_protorefs : content changed
~ __DATA.__objc_classrefs : content changed
~ __DATA.__objc_superrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ +[DockChannelProbeDeviceHubListenerIOUSBHost baseNameForCustomName:probePortCount:portNumber:location:]
+ +[DockChannelProbeDeviceHubListenerIOUSBHost countProbePortsInMask:length:]
+ +[DockChannelProbeDeviceListenerIOUSBHost baseNameForCustomName:serialPrefix:serialNumber:]
+ -[AppleRSMChannelQueue dealloc]
+ -[AppleRSMChannelQueue dispatchSourceActivated]
+ -[AppleRSMChannelQueue setDispatchSourceActivated:]
+ -[DockChannelProbeDeviceHubListenerIOUSBHost nameForService:hubState:]
+ -[DockChannelProbeDeviceHubState customName]
+ -[DockChannelProbeDeviceHubState initWithOwner:serviceID:location:platformCapabilityDescriptor:customName:]
+ -[DockChannelProbeDeviceHubState probePortCount]
+ -[DockChannelProbeDeviceMatching customNameDescriptorIndex]
+ -[DockChannelProbeDeviceMatching initWithVendorID:productID:serialPrefix:supportsCustomName:customNameDescriptorIndex:]
+ -[DockChannelProbeDeviceMatching supportsCustomName]
+ -[DockChannelProbeInterface addPermanentSuffix:client:]
+ -[DockChannelProbeInterface dispatchDiscoveryToClient:interfaceID:suffix:]
+ -[DockChannelProbeInterface dispatchTerminationToClient:interfaceID:suffix:]
+ -[DockChannelProbeInterface permanentInterfaceStatesBySuffix]
+ -[DockChannelProbeInterface permanentSuffixByInterfaceID]
+ -[DockChannelProbeInterfaceClient dealloc]
+ -[DockChannelProbeInterfaceClient listening]
+ -[DockChannelProbeInterfaceClient setListening:]
+ -[DockChannelProbeInterfaceClient startListening]
+ -[DockChannelProbeInterfaceClient stopListening]
+ -[DockChannelProbeNexusController isProbeDeviceHubNexusDevice:]
+ -[DockChannelProbeNexusProbeDeviceHub addProbe:probeType:probeID:pinService:pinServiceID:client:]
+ -[DockChannelSerialInterfaceController dispatchDiscoveryToClient:interfaceID:baseName:suffix:]
+ -[DockChannelSerialInterfaceController dispatchTerminationToClient:interfaceID:suffix:]
+ -[DockChannelSerialInterfaceController namesByInterfaceID]
+ -[DockChannelSerialInterfaceController startCreateInterfaceForState:]
+ -[DockChannelSerialInterfaceControllerClient listening]
+ -[DockChannelSerialInterfaceControllerClient setListening:]
+ -[DockChannelSerialInterfaceControllerClient startListening]
+ -[DockChannelSerialInterfaceControllerClient stopListening]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial initWithQueue:rxQueueLogSize:]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial rxQueueLogSize]
+ -[DockChannelSerialInterfaceControllerInterfaceState interfaceExists]
+ -[DockChannelSerialInterfaceControllerInterfaceState setInterfaceExists:]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper getStringDescriptorAtIndex:string:length:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getStringDescriptorAtIndex:string:length:]
+ -[ProbePermanentSerialInterfaceState clients]
+ -[ProbePermanentSerialInterfaceState initWithSuffix:]
+ -[ProbePermanentSerialInterfaceState interfaceExists]
+ -[ProbePermanentSerialInterfaceState interfaceID]
+ -[ProbePermanentSerialInterfaceState interface]
+ -[ProbePermanentSerialInterfaceState setInterface:]
+ -[ProbePermanentSerialInterfaceState setInterfaceExists:]
+ -[ProbePermanentSerialInterfaceState setInterfaceID:]
+ -[RSMInterfaceKIS dispatchTimerActivated]
+ -[RSMInterfaceKIS setDispatchTimerActivated:]
+ GCC_except_table30
+ GCC_except_table50
+ GCC_except_table63
+ GCC_except_table76
+ GCC_except_table88
+ OBJC_IVAR_$_AppleRSMChannelQueue._dispatchSourceActivated
+ OBJC_IVAR_$_DockChannelProbeDeviceHubState._customName
+ OBJC_IVAR_$_DockChannelProbeDeviceHubState._probePortCount
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._customNameDescriptorIndex
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._supportsCustomName
+ OBJC_IVAR_$_DockChannelProbeInterface._permanentInterfaceStatesBySuffix
+ OBJC_IVAR_$_DockChannelProbeInterface._permanentSuffixByInterfaceID
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._listening
+ OBJC_IVAR_$_DockChannelSerialInterfaceController._namesByInterfaceID
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerClient._listening
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._rxQueueLogSize
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerInterfaceState._interfaceExists
+ OBJC_IVAR_$_ProbePermanentSerialInterfaceState._clients
+ OBJC_IVAR_$_ProbePermanentSerialInterfaceState._interface
+ OBJC_IVAR_$_ProbePermanentSerialInterfaceState._interfaceExists
+ OBJC_IVAR_$_ProbePermanentSerialInterfaceState._interfaceID
+ OBJC_IVAR_$_RSMInterfaceKIS._dispatchTimerActivated
+ _OBJC_CLASS_$_DockChannelProbeNexusProbeDeviceHub
+ _OBJC_METACLASS_$_DockChannelProbeNexusProbeDeviceHub
+ __OBJC_$_CLASS_METHODS_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusProbeDeviceHub
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusProbeDeviceHub
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusProbeDeviceHub
+ ___69-[DockChannelSerialInterfaceController startCreateInterfaceForState:]_block_invoke
+ ___74-[DockChannelProbeInterface dispatchDiscoveryToClient:interfaceID:suffix:]_block_invoke
+ ___76-[DockChannelProbeInterface dispatchTerminationToClient:interfaceID:suffix:]_block_invoke
+ ___87-[DockChannelSerialInterfaceController dispatchTerminationToClient:interfaceID:suffix:]_block_invoke
+ ___94-[DockChannelSerialInterfaceController dispatchDiscoveryToClient:interfaceID:baseName:suffix:]_block_invoke
+ ___block_descriptor_56_e8_32s40s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40w_e5_v8?0l
+ ___block_descriptor_74_e8_32s40w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s
+ _dock_channel_probe_interface_client_start_listening
+ _dock_channel_probe_interface_client_stop_listening
+ _dock_channel_probe_nexus_probe_device_hub_create
+ _dock_channel_serial_interface_controller_client_objc_start_listening
+ _dock_channel_serial_interface_controller_client_objc_stop_listening
+ _dock_channel_serial_interface_controller_client_start_listening
+ _dock_channel_serial_interface_controller_client_stop_listening
+ _dock_channel_system_service_usb_device_iousbhost_string_descriptor
+ _dock_channel_system_service_usb_device_string_descriptor
+ _objc_msgSend$addPermanentSuffix:client:
+ _objc_msgSend$baseNameForCustomName:probePortCount:portNumber:location:
+ _objc_msgSend$baseNameForCustomName:serialPrefix:serialNumber:
+ _objc_msgSend$countProbePortsInMask:length:
+ _objc_msgSend$customName
+ _objc_msgSend$customNameDescriptorIndex
+ _objc_msgSend$dispatchDiscoveryToClient:interfaceID:baseName:suffix:
+ _objc_msgSend$dispatchDiscoveryToClient:interfaceID:suffix:
+ _objc_msgSend$dispatchTerminationToClient:interfaceID:suffix:
+ _objc_msgSend$getStringDescriptorAtIndex:string:length:
+ _objc_msgSend$initWithOwner:serviceID:location:platformCapabilityDescriptor:customName:
+ _objc_msgSend$initWithQueue:rxQueueLogSize:
+ _objc_msgSend$initWithSuffix:
+ _objc_msgSend$initWithVendorID:productID:serialPrefix:supportsCustomName:customNameDescriptorIndex:
+ _objc_msgSend$interfaceExists
+ _objc_msgSend$isProbeDeviceHubNexusDevice:
+ _objc_msgSend$nameForService:hubState:
+ _objc_msgSend$probePortCount
+ _objc_msgSend$serialController
+ _objc_msgSend$serialInterfaceManagerClient
+ _objc_msgSend$setDispatchTimerActivated:
+ _objc_msgSend$setInterface:
+ _objc_msgSend$setInterfaceExists:
+ _objc_msgSend$startCreateInterfaceForState:
+ _objc_msgSend$stringWithIndex:languageID:error:
+ _objc_msgSend$supportsCustomName
- -[DockChannelProbeDeviceHubListenerIOUSBHost nameForService:]
- -[DockChannelProbeDeviceHubState initWithOwner:serviceID:location:platformCapabilityDescriptor:]
- -[DockChannelProbeDeviceMatching initWithVendorID:productID:serialPrefix:]
- -[DockChannelProbeInterface addPermanentSuffix:]
- -[DockChannelProbeInterface createSerialInterfaceControllerClientForClientWithDescription:]
- -[DockChannelProbeInterface permanentSerialInterfaceStatesByID]
- -[DockChannelProbeInterface permanentSuffixes]
- -[DockChannelProbeInterface registerCallbacksForSerialController:description:callbacks:]
- -[DockChannelProbeInterface removeCallbacksForSerialController:description:]
- -[DockChannelProbeInterface revokeAllSerialInterfaceRequestsForClient:]
- -[DockChannelProbeInterfaceClient requestedNonPermanentSuffixes]
- -[DockChannelProbeInterfaceClient revokeAllSerialInterfaceRequests]
- -[DockChannelProbeInterfaceClient setRequestedNonPermanentSuffixes:]
- -[DockChannelSerialInterfaceController acquireInterface:client:]
- -[DockChannelSerialInterfaceController createdInterfaceByInterfaceID]
- -[DockChannelSerialInterfaceController releaseInterface:client:]
- -[DockChannelSerialInterfaceControllerClient acquiredSerialInterfaceIDs]
- -[DockChannelSerialInterfaceControllerCreatedInterface .cxx_destruct]
- -[DockChannelSerialInterfaceControllerCreatedInterface initWithName:interface:]
- -[DockChannelSerialInterfaceControllerCreatedInterface interface]
- -[DockChannelSerialInterfaceControllerCreatedInterface name]
- -[DockChannelSerialInterfaceControllerCreatedInterface setInterface:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial initWithQueue:]
- -[DockChannelSerialInterfaceControllerInterfaceState hasSerialInterface]
- -[ProbePermanentSerialInterfaceState initWithInterface:interfaceID:suffix:]
- GCC_except_table32
- GCC_except_table44
- GCC_except_table47
- GCC_except_table60
- GCC_except_table73
- GCC_except_table85
- OBJC_IVAR_$_DockChannelProbeInterface._permanentSerialInterfaceStatesByID
- OBJC_IVAR_$_DockChannelProbeInterface._permanentSuffixes
- OBJC_IVAR_$_DockChannelProbeInterfaceClient._requestedNonPermanentSuffixes
- OBJC_IVAR_$_DockChannelSerialInterfaceController._createdInterfaceByInterfaceID
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerClient._acquiredSerialInterfaceIDs
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerCreatedInterface._interface
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerCreatedInterface._name
- _OBJC_CLASS_$_DockChannelSerialInterfaceControllerCreatedInterface
- _OBJC_METACLASS_$_DockChannelSerialInterfaceControllerCreatedInterface
- __69-[DockChannelSerialInterfaceController handleSerialInterfaceRemoved:]_block_invoke
- __OBJC_$_INSTANCE_METHODS_DockChannelSerialInterfaceControllerCreatedInterface
- __OBJC_$_INSTANCE_VARIABLES_DockChannelSerialInterfaceControllerCreatedInterface
- __OBJC_$_PROP_LIST_DockChannelSerialInterfaceControllerCreatedInterface
- __OBJC_CLASS_RO_$_DockChannelSerialInterfaceControllerCreatedInterface
- __OBJC_METACLASS_RO_$_DockChannelSerialInterfaceControllerCreatedInterface
- ___121-[DockChannelSerialInterfaceController requestInterfaceWithBase:suffix:nexusID:nexusLocation:portID:portLocation:client:]_block_invoke
- ___67-[DockChannelSerialInterfaceController handleSerialInterfaceAdded:]_block_invoke
- ___68-[DockChannelProbeInterface handlePermanentInterfaceRemoved:suffix:]_block_invoke
- ___69-[DockChannelSerialInterfaceController handleSerialInterfaceRemoved:]_block_invoke
- ___75-[DockChannelProbeInterface handlePermanentInterfaceAdded:baseName:suffix:]_block_invoke
- ___88-[DockChannelSerialInterfaceController cancelRequestForInterfaceWithBase:suffix:client:]_block_invoke
- ___block_descriptor_64_e8_32s40s48w_e5_v8?0l
- ___block_descriptor_64_e8_32s40w_e8_v12?0B8l
- ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0l
- ___block_descriptor_72_e8_32w_e5_v8?0l
- ___block_descriptor_74_e8_32w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56w
- ___copy_helper_block_e8_32s40s48w
- ___destroy_helper_block_e8_32s40s48s56w
- ___destroy_helper_block_e8_32s40s48w
- _dock_channel_probe_interface_client_revoke_all_serial_interface_requests
- _dock_channel_serial_interface_controller_client_objc_remove_callbacks
- _dock_channel_serial_interface_controller_client_remove_callbacks
- _objc_msgSend$acquireInterface:client:
- _objc_msgSend$acquiredSerialInterfaceIDs
- _objc_msgSend$addPermanentSuffix:
- _objc_msgSend$allKeys
- _objc_msgSend$createSerialInterfaceControllerClientForClientWithDescription:
- _objc_msgSend$hasSerialInterface
- _objc_msgSend$initWithInterface:interfaceID:suffix:
- _objc_msgSend$initWithName:interface:
- _objc_msgSend$initWithOwner:serviceID:location:platformCapabilityDescriptor:
- _objc_msgSend$initWithVendorID:productID:serialPrefix:
- _objc_msgSend$registerCallbacksForSerialController:description:callbacks:
- _objc_msgSend$releaseInterface:client:
- _objc_msgSend$removeCallbacksForSerialController:description:
- _objc_msgSend$requestedNonPermanentSuffixes
- _objc_msgSend$revokeAllSerialInterfaceRequests
- _objc_msgSend$revokeAllSerialInterfaceRequestsForClient:
- _objc_msgSend$setSerialControllerClient:
CStrings:
+ "\""
+ "%@-%u"
+ "@28@0:8@16C24"
+ "@36@0:8@16I24C28I32"
+ "@40@0:8@16@24@32"
+ "@40@0:8S16S20@24B32C36"
+ "@52@0:8@16Q24I32@36@44"
+ "B36@0:8C16*20^Q28"
+ "DockChannel serial RX queue size: %uK (logsz %u)"
+ "DockChannelProbeNexusProbeDeviceHub"
+ "Failed to create interface with name: %{public}@ suffix: %{public}@"
+ "Failed to start listening on probe interface client, interfaceID 0x%llx"
+ "I28@0:8r*16C24"
+ "Probe[0x%llx][%{public}@] cleaning up client: %{public}@"
+ "Probe[0x%llx][%{public}@] cleaning up."
+ "Probe[0x%llx][%{public}@] client: %{public}@ cannot acquire permanent serial interface 0x%llx, already owned by a client"
+ "Probe[0x%llx][%{public}@] client: %{public}@ failed to acquire serial interface 0x%llx"
+ "Probe[0x%llx][%{public}@] client: %{public}@ is acquiring serial interface 0x%llx"
+ "Probe[0x%llx][%{public}@] client: %{public}@ is handing off serial interface 0x%llx to client: %{public}@"
+ "Probe[0x%llx][%{public}@] client: %{public}@ is releasing serial interface 0x%llx"
+ "Probe[0x%llx][%{public}@] client: %{public}@ is requesting a serial interface with suffix: %{public}s (permanent = %d)"
+ "Probe[0x%llx][%{public}@] client: %{public}@ is requesting available serial interfaces"
+ "Probe[0x%llx][%{public}@] client: %{public}@ is requesting the cleanup of serial interface with suffix: %{public}s"
+ "Probe[0x%llx][%{public}@] creating client: %{public}@"
+ "Probe[0x%llx][%{public}@] failed to acquire permanent interface 0x%llx"
+ "Probe[0x%llx][%{public}@] failed to create dock channel serial interface controller client"
+ "Probe[0x%llx][%{public}@] failed to register callbacks on serial interface controller client"
+ "Probe[0x%llx][%{public}@] failed to start listening on serial interface controller client"
+ "Probe[0x%llx][%{public}@] initialized."
+ "Probe[0x%llx][%{public}@] invalid base name %{public}@, expected %{public}@"
+ "Probe[0x%llx][%{public}@] permanent interface added: 0x%llx suffix: %{public}s (success = %d)"
+ "Probe[0x%llx][%{public}@] permanent interface removed: 0x%llx (success = %d)"
+ "Probe[0x%llx][%{public}@] probe still has %lu clients registered during cleanup!"
+ "Probe[0x%llx][%{public}@] starting."
+ "Probe[0x%llx][%{public}@] stopping."
+ "T@\"NSMutableDictionary\",R,N,V_namesByInterfaceID"
+ "T@\"NSMutableDictionary\",R,N,V_permanentInterfaceStatesBySuffix"
+ "T@\"NSMutableDictionary\",R,N,V_permanentSuffixByInterfaceID"
+ "T@\"NSString\",R,N,V_customName"
+ "TB,N,V_dispatchSourceActivated"
+ "TB,N,V_dispatchTimerActivated"
+ "TB,N,V_interfaceExists"
+ "TB,R,N,V_supportsCustomName"
+ "TC,R,N,V_customNameDescriptorIndex"
+ "TC,R,N,V_rxQueueLogSize"
+ "TI,R,N,V_probePortCount"
+ "USBDevice[0x%llx]: Error encountered while creating device interface for string descriptor: %@"
+ "[0x%llx] (0x%08x) ZLP submission failed (result=%d)"
+ "_customName"
+ "_customNameDescriptorIndex"
+ "_dispatchSourceActivated"
+ "_dispatchTimerActivated"
+ "_interfaceExists"
+ "_namesByInterfaceID"
+ "_permanentInterfaceStatesBySuffix"
+ "_permanentSuffixByInterfaceID"
+ "_probePortCount"
+ "_rxQueueLogSize"
+ "_supportsCustomName"
+ "addPermanentSuffix:client:"
+ "baseNameForCustomName:probePortCount:portNumber:location:"
+ "baseNameForCustomName:serialPrefix:serialNumber:"
+ "countProbePortsInMask:length:"
+ "customName"
+ "customNameDescriptorIndex"
+ "dispatchDiscoveryToClient:interfaceID:baseName:suffix:"
+ "dispatchDiscoveryToClient:interfaceID:suffix:"
+ "dispatchSourceActivated"
+ "dispatchTerminationToClient:interfaceID:suffix:"
+ "dispatchTimerActivated"
+ "getStringDescriptorAtIndex:string:length:"
+ "initWithOwner:serviceID:location:platformCapabilityDescriptor:customName:"
+ "initWithQueue:rxQueueLogSize:"
+ "initWithSuffix:"
+ "initWithVendorID:productID:serialPrefix:supportsCustomName:customNameDescriptorIndex:"
+ "interfaceExists"
+ "isProbeDeviceHubNexusDevice:"
+ "nameForService:hubState:"
+ "namesByInterfaceID"
+ "permanentInterfaceStatesBySuffix"
+ "permanentSuffixByInterfaceID"
+ "probePortCount"
+ "rxQueueLogSize"
+ "setDispatchSourceActivated:"
+ "setDispatchTimerActivated:"
+ "setInterfaceExists:"
+ "startCreateInterfaceForState:"
+ "stringWithIndex:languageID:error:"
+ "supportsCustomName"
+ "v40@0:8@16Q24@32"
+ "v48@0:8@16Q24@32@40"
- "-%s"
- "@32@0:8@16^{device_interface_t=^v^{device_interface_functions_t}}24"
- "@32@0:8S16S20@24"
- "@44@0:8@16Q24I32@36"
- "B32@0:8^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}16@24"
- "B40@0:8^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}16@24r^{dock_channel_serial_interface_controller_client_callbacks_t=^?^v^?^v}32"
- "Client: %{public}@ revoking serial interface with name: %{public}@ suffix: %{public}@ with outstanding acquired interface 0x%llx — release interface must be done before revoke"
- "DockChannelSerialInterfaceControllerCreatedInterface"
- "Failed to create interface with name: %s suffix: %s"
- "Probe[0x%llx] cleaning up client: %{public}@"
- "Probe[0x%llx] cleaning up."
- "Probe[0x%llx] client: %{public}@ failed to acquire permanent serial interface 0x%llx"
- "Probe[0x%llx] client: %{public}@ is acquiring serial interface 0x%llx"
- "Probe[0x%llx] client: %{public}@ is releasing serial interface 0x%llx"
- "Probe[0x%llx] client: %{public}@ is requesting a serial interface with name: %{public}@ suffix: %{public}s (permanent = %d)"
- "Probe[0x%llx] client: %{public}@ is requesting available serial interfaces"
- "Probe[0x%llx] client: %{public}@ is requesting the cleanup of all serial interfaces"
- "Probe[0x%llx] client: %{public}@ is requesting the cleanup of serial interface with suffix: %{public}s"
- "Probe[0x%llx] creating client: %{public}@"
- "Probe[0x%llx] creating serial interface client on behalf of client: %{public}@"
- "Probe[0x%llx] failed to acquire permanent interface 0x%llx"
- "Probe[0x%llx] failed to create dock channel serial interface controller client"
- "Probe[0x%llx] failed to create serial interface client on behalf of client: %{public}@"
- "Probe[0x%llx] failed to register callbacks on serial interface controller client"
- "Probe[0x%llx] failed to register for serial interface controller callbacks on behalf of client: %{public}@"
- "Probe[0x%llx] initialized."
- "Probe[0x%llx] invalid base name %{public}@, expected %{public}@"
- "Probe[0x%llx] permanent interface added: 0x%llx suffix: %{public}s"
- "Probe[0x%llx] permanent interface removed: 0x%llx"
- "Probe[0x%llx] registering for serial interface controller callbacks on behalf of client: %{public}@"
- "Probe[0x%llx] releasing permanent interface 0x%llx with %lu probe-client(s) still holding — must release before revoke"
- "Probe[0x%llx] removing serial interface controller callbacks on behalf of client: %{public}@"
- "Probe[0x%llx] starting."
- "Probe[0x%llx] stopping."
- "T@\"NSMutableDictionary\",R,N,V_createdInterfaceByInterfaceID"
- "T@\"NSMutableDictionary\",R,N,V_permanentSerialInterfaceStatesByID"
- "T@\"NSMutableSet\",&,N,V_requestedNonPermanentSuffixes"
- "T@\"NSMutableSet\",R,N,V_acquiredSerialInterfaceIDs"
- "T@\"NSMutableSet\",R,N,V_permanentSuffixes"
- "^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}24@0:8@16"
- "_acquiredSerialInterfaceIDs"
- "_createdInterfaceByInterfaceID"
- "_permanentSerialInterfaceStatesByID"
- "_permanentSuffixes"
- "_requestedNonPermanentSuffixes"
- "acquireInterface:client:"
- "acquiredSerialInterfaceIDs"
- "addPermanentSuffix:"
- "allKeys"
- "createSerialInterfaceControllerClientForClientWithDescription:"
- "createdInterfaceByInterfaceID"
- "hasSerialInterface"
- "initWithInterface:interfaceID:suffix:"
- "initWithName:interface:"
- "initWithOwner:serviceID:location:platformCapabilityDescriptor:"
- "initWithVendorID:productID:serialPrefix:"
- "permanentSerialInterfaceStatesByID"
- "permanentSuffixes"
- "registerCallbacksForSerialController:description:callbacks:"
- "releaseInterface:client:"
- "removeCallbacksForSerialController:description:"
- "requestedNonPermanentSuffixes"
- "revokeAllSerialInterfaceRequests"
- "revokeAllSerialInterfaceRequestsForClient:"
- "setRequestedNonPermanentSuffixes:"

```
