## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

```diff

-178.60.8.0.0
-  __TEXT.__text: 0x3aa44
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x4118
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__cstring: 0x4689
-  __TEXT.__oslogstring: 0x2f49
-  __TEXT.__unwind_info: 0xbf0
-  __TEXT.__objc_classname: 0x8ea
-  __TEXT.__objc_methname: 0xa6d7
-  __TEXT.__objc_methtype: 0x4666
-  __TEXT.__objc_stubs: 0x4d00
-  __DATA_CONST.__got: 0x1d0
+205.0.0.0.0
+  __TEXT.__text: 0x84b0c
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x5a8c
+  __TEXT.__const: 0x64
+  __TEXT.__cstring: 0x4821
+  __TEXT.__gcc_except_tab: 0x8a4
+  __TEXT.__oslogstring: 0x3db7
+  __TEXT.__unwind_info: 0x1358
+  __TEXT.__objc_classname: 0xd2a
+  __TEXT.__objc_methname: 0xd107
+  __TEXT.__objc_methtype: 0x6378
+  __TEXT.__objc_stubs: 0x60a0
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x9208
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH.__objc_data: 0x1400
-  __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0x754
-  __DATA.__data: 0x3e0
-  __DATA.__bss: 0x80
+  __DATA_CONST.__objc_superrefs: 0x2c8
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x7c0
+  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__objc_const: 0xc1a0
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH.__objc_data: 0x1c70
+  __AUTH.__data: 0x4a0
+  __DATA.__objc_ivar: 0xa44
+  __DATA.__data: 0x4b0
+  __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 7FE6424B-C2CB-305E-A989-E5D808171D11
-  Functions: 1843
-  Symbols:   3701
-  CStrings:  2664
+  UUID: 43E53CBA-36D7-3390-84EB-9185735E072A
+  Functions: 2465
+  Symbols:   4881
+  CStrings:  3254
 
Symbols:
+ +[DockChannelSystemServiceIOService getIOServiceFromSystemService:]
+ -[DebugUSBDeviceInterfaceIOUSBHost transaction]
+ -[DebugUSBInterfaceIOUSBHost getTransportService]
+ -[DebugUSBInterfaceIOUSBHost initWithService:systemServiceController:]
+ -[DebugUSBInterfaceIOUSBHost systemServiceController]
+ -[DebugUSBInterfaceIOUSBHostClient getTransportService]
+ -[DebugUSBInterfaceListenerIOUSBHost initWithSystemServiceController:]
+ -[DebugUSBInterfaceListenerIOUSBHost systemServiceController]
+ -[DockChannelInterfaceKISPAM applyEnablePPMDockChannelWorkaround:]
+ -[DockChannelInterfaceKISPAM configurePushForDockChannel:]
+ -[DockChannelInterfaceKISPAM dockChannelsWithBackPressure]
+ -[DockChannelInterfaceKISPAM dockChannelsWithPush]
+ -[DockChannelInterfaceKISPAM enablePPM:]
+ -[DockChannelInterfaceKISPAM getPlatformMinimumPPWInterval:]
+ -[DockChannelInterfaceKISPAM handleConnectEventOnChannel:]
+ -[DockChannelInterfaceKISPAM handleHangUpEventOnChannel:]
+ -[DockChannelInterfaceKISPAM handlePAR:dockChannelID:words:]
+ -[DockChannelInterfaceKISPAM handleProbeInterfaceAdded:]
+ -[DockChannelInterfaceKISPAM handleProbeInterfaceRemoved:]
+ -[DockChannelInterfaceKISPAM handleSerialInterfaceAdded:suffix:]
+ -[DockChannelInterfaceKISPAM handleSerialInterfaceRemoved:suffix:]
+ -[DockChannelInterfaceKISPAM handleWatermarkEventOnChannel:highWatermark:]
+ -[DockChannelInterfaceKISPAM initWithKISInterfaceID:kisManager:nexusController:queue:]
+ -[DockChannelInterfaceKISPAM isWatchdogAvailable]
+ -[DockChannelInterfaceKISPAM lock]
+ -[DockChannelInterfaceKISPAM nexusClient]
+ -[DockChannelInterfaceKISPAM nexusControllerClient]
+ -[DockChannelInterfaceKISPAM nexusController]
+ -[DockChannelInterfaceKISPAM nexus]
+ -[DockChannelInterfaceKISPAM pinService]
+ -[DockChannelInterfaceKISPAM platformRequiresPolling]
+ -[DockChannelInterfaceKISPAM ppmEnabledDockChannels]
+ -[DockChannelInterfaceKISPAM ppmEnabled]
+ -[DockChannelInterfaceKISPAM ppmEndpoint]
+ -[DockChannelInterfaceKISPAM probeSerialState]
+ -[DockChannelInterfaceKISPAM readRSTAT:dockChannelID:]
+ -[DockChannelInterfaceKISPAM readRemainingBytes:readRemainingBytesCount:channelDockDataBase:dockChannelID:]
+ -[DockChannelInterfaceKISPAM readWSTAT:dockChannelID:]
+ -[DockChannelInterfaceKISPAM readWords:channelDockDataBase:dockChannelID:]
+ -[DockChannelInterfaceKISPAM scheduleWorkloop]
+ -[DockChannelInterfaceKISPAM setDockChannelsWithBackPressure:]
+ -[DockChannelInterfaceKISPAM setDockChannelsWithPush:]
+ -[DockChannelInterfaceKISPAM setNexusControllerClient:]
+ -[DockChannelInterfaceKISPAM setPlatformRequiresPolling:]
+ -[DockChannelInterfaceKISPAM setPpmEnabled:]
+ -[DockChannelInterfaceKISPAM setPpmEnabledDockChannels:]
+ -[DockChannelInterfaceKISPAM setProbeSerialState:]
+ -[DockChannelInterfaceKISPAM setWorkloopScheduled:]
+ -[DockChannelInterfaceKISPAM transportService]
+ -[DockChannelInterfaceKISPAM workloopScheduled]
+ -[DockChannelInterfaceKISPAM writeData:channel:]
+ -[DockChannelInterfaceKISPAM writeRemainingBytes:channelDockDataBase:dockChannelID:writeData:writeRemainingBytesCount:]
+ -[DockChannelInterfaceKISPAM writeWords:channelDockDataBase:dockChannelID:writeData:]
+ -[DockChannelInterfaceProbeSerialState .cxx_destruct]
+ -[DockChannelInterfaceProbeSerialState cleanupSerialInterfaceWithSuffix:]
+ -[DockChannelInterfaceProbeSerialState createSerialInterfaceWithSuffix:rxQueueLogSize:txQueueLogSize:permanent:]
+ -[DockChannelInterfaceProbeSerialState createdSerialInterfaces]
+ -[DockChannelInterfaceProbeSerialState handleSerialInterfaceAdded:suffix:]
+ -[DockChannelInterfaceProbeSerialState handleSerialInterfaceRemoved:suffix:]
+ -[DockChannelInterfaceProbeSerialState initWithOwner:interfaceID:nexusClient:]
+ -[DockChannelInterfaceProbeSerialState nexusClient]
+ -[DockChannelInterfaceProbeSerialState owner]
+ -[DockChannelInterfaceProbeSerialState performCleanup]
+ -[DockChannelInterfaceProbeSerialState probeBaseName]
+ -[DockChannelInterfaceProbeSerialState probeInterfaceClient]
+ -[DockChannelInterfaceProbeSerialState probeInterfaceID]
+ -[DockChannelInterfaceProbeSerialState probeInterface]
+ -[DockChannelInterfaceProbeSerialState serialInterfaces]
+ -[DockChannelProbeDeviceListenerIOUSBHost .cxx_destruct]
+ -[DockChannelProbeDeviceListenerIOUSBHost active]
+ -[DockChannelProbeDeviceListenerIOUSBHost deviceQueue]
+ -[DockChannelProbeDeviceListenerIOUSBHost discoveryCallback]
+ -[DockChannelProbeDeviceListenerIOUSBHost discoveryContext]
+ -[DockChannelProbeDeviceListenerIOUSBHost handleDiscoveredService:]
+ -[DockChannelProbeDeviceListenerIOUSBHost handlePinServiceRemoval:]
+ -[DockChannelProbeDeviceListenerIOUSBHost initWithSystemServiceController:nexusController:serialManager:serialController:deviceQueue:]
+ -[DockChannelProbeDeviceListenerIOUSBHost matchingArray]
+ -[DockChannelProbeDeviceListenerIOUSBHost nameForService:]
+ -[DockChannelProbeDeviceListenerIOUSBHost nexusController]
+ -[DockChannelProbeDeviceListenerIOUSBHost notificationPort]
+ -[DockChannelProbeDeviceListenerIOUSBHost notificationQueue]
+ -[DockChannelProbeDeviceListenerIOUSBHost performCleanup]
+ -[DockChannelProbeDeviceListenerIOUSBHost probeStateByPinServiceID]
+ -[DockChannelProbeDeviceListenerIOUSBHost serialController]
+ -[DockChannelProbeDeviceListenerIOUSBHost serialManager]
+ -[DockChannelProbeDeviceListenerIOUSBHost setActive:]
+ -[DockChannelProbeDeviceListenerIOUSBHost setDiscoveryCallback:]
+ -[DockChannelProbeDeviceListenerIOUSBHost setDiscoveryContext:]
+ -[DockChannelProbeDeviceListenerIOUSBHost setNotificationQueue:]
+ -[DockChannelProbeDeviceListenerIOUSBHost setTerminationCallback:]
+ -[DockChannelProbeDeviceListenerIOUSBHost setTerminationContext:]
+ -[DockChannelProbeDeviceListenerIOUSBHost startListeningOnQueue:]
+ -[DockChannelProbeDeviceListenerIOUSBHost stopListening]
+ -[DockChannelProbeDeviceListenerIOUSBHost systemServiceController]
+ -[DockChannelProbeDeviceListenerIOUSBHost terminationCallback]
+ -[DockChannelProbeDeviceListenerIOUSBHost terminationContext]
+ -[DockChannelProbeDeviceMatching .cxx_destruct]
+ -[DockChannelProbeDeviceMatching discoveryIteratorPointer]
+ -[DockChannelProbeDeviceMatching discoveryIterator]
+ -[DockChannelProbeDeviceMatching initWithVendorID:productID:serialPrefix:]
+ -[DockChannelProbeDeviceMatching matchingDictionary]
+ -[DockChannelProbeDeviceMatching pid]
+ -[DockChannelProbeDeviceMatching serialPrefix]
+ -[DockChannelProbeDeviceMatching setDiscoveryIterator:]
+ -[DockChannelProbeDeviceMatching vid]
+ -[DockChannelProbeInterface .cxx_destruct]
+ -[DockChannelProbeInterface acquireSerialInterfaceWithID:client:]
+ -[DockChannelProbeInterface addSerialInterfaceWithID:]
+ -[DockChannelProbeInterface baseName]
+ -[DockChannelProbeInterface cleanupAllSerialInterfacesForClient:]
+ -[DockChannelProbeInterface cleanupClient:]
+ -[DockChannelProbeInterface cleanupSerialInterface:client:]
+ -[DockChannelProbeInterface clients]
+ -[DockChannelProbeInterface createClientWithDescription:]
+ -[DockChannelProbeInterface createSerialInterface:suffix:rxQueueLogSize:txQueueLogSize:client:]
+ -[DockChannelProbeInterface getBaseName:length:]
+ -[DockChannelProbeInterface getID:]
+ -[DockChannelProbeInterface initWithProbeID:baseName:serialManager:serialController:queue:]
+ -[DockChannelProbeInterface interfacesLock]
+ -[DockChannelProbeInterface listAvailableInterfaces:suffixes:count:forClient:]
+ -[DockChannelProbeInterface nexusID]
+ -[DockChannelProbeInterface nexusLocation]
+ -[DockChannelProbeInterface performCleanup]
+ -[DockChannelProbeInterface permanentSuffixes]
+ -[DockChannelProbeInterface portID]
+ -[DockChannelProbeInterface portLocation]
+ -[DockChannelProbeInterface probeID]
+ -[DockChannelProbeInterface queue]
+ -[DockChannelProbeInterface releaseSerialInterfaceWithID:client:]
+ -[DockChannelProbeInterface removeSerialInterfaceWithID:]
+ -[DockChannelProbeInterface serialControllerClient]
+ -[DockChannelProbeInterface serialController]
+ -[DockChannelProbeInterface serialInterfaceStatesByID]
+ -[DockChannelProbeInterface serialManagerClient]
+ -[DockChannelProbeInterface serialManager]
+ -[DockChannelProbeInterface setNexusID:]
+ -[DockChannelProbeInterface setNexusLocation:]
+ -[DockChannelProbeInterface setPortID:]
+ -[DockChannelProbeInterface setPortLocation:]
+ -[DockChannelProbeInterface startListeningForClient:]
+ -[DockChannelProbeInterface startWithCompletion:]
+ -[DockChannelProbeInterface stopListeningForClient:]
+ -[DockChannelProbeInterface stopWithCompletion:]
+ -[DockChannelProbeInterface transaction]
+ -[DockChannelProbeInterfaceClient .cxx_destruct]
+ -[DockChannelProbeInterfaceClient acquireSerialInterface:]
+ -[DockChannelProbeInterfaceClient cleanupAllSerialInterfaces]
+ -[DockChannelProbeInterfaceClient cleanupSerialInterface:]
+ -[DockChannelProbeInterfaceClient clientDescription]
+ -[DockChannelProbeInterfaceClient createSerialInterface:suffix:rxQueueLogSize:txQueueLogSize:]
+ -[DockChannelProbeInterfaceClient discoveryCallback]
+ -[DockChannelProbeInterfaceClient discoveryContext]
+ -[DockChannelProbeInterfaceClient externalInterfacePointer]
+ -[DockChannelProbeInterfaceClient externalInterface]
+ -[DockChannelProbeInterfaceClient getBaseName:length:]
+ -[DockChannelProbeInterfaceClient initWithInterface:description:]
+ -[DockChannelProbeInterfaceClient interface]
+ -[DockChannelProbeInterfaceClient listAvailableInterfaces:suffixes:count:]
+ -[DockChannelProbeInterfaceClient listening]
+ -[DockChannelProbeInterfaceClient registerCallbacks:]
+ -[DockChannelProbeInterfaceClient releaseSerialInterface:]
+ -[DockChannelProbeInterfaceClient setDiscoveryCallback:]
+ -[DockChannelProbeInterfaceClient setDiscoveryContext:]
+ -[DockChannelProbeInterfaceClient setListening:]
+ -[DockChannelProbeInterfaceClient setNexusID:]
+ -[DockChannelProbeInterfaceClient setNexusLocation:]
+ -[DockChannelProbeInterfaceClient setPortID:]
+ -[DockChannelProbeInterfaceClient setPortLocation:]
+ -[DockChannelProbeInterfaceClient setTerminationCallback:]
+ -[DockChannelProbeInterfaceClient setTerminationContext:]
+ -[DockChannelProbeInterfaceClient startListening]
+ -[DockChannelProbeInterfaceClient stopListening]
+ -[DockChannelProbeInterfaceClient terminationCallback]
+ -[DockChannelProbeInterfaceClient terminationContext]
+ -[DockChannelProbeKISListenerIOUSBHost .cxx_destruct]
+ -[DockChannelProbeKISListenerIOUSBHost active]
+ -[DockChannelProbeKISListenerIOUSBHost deviceQueue]
+ -[DockChannelProbeKISListenerIOUSBHost discoveryCallback]
+ -[DockChannelProbeKISListenerIOUSBHost discoveryContext]
+ -[DockChannelProbeKISListenerIOUSBHost discoveryIterator]
+ -[DockChannelProbeKISListenerIOUSBHost handleDiscoveredService:]
+ -[DockChannelProbeKISListenerIOUSBHost handlePinServiceRemoval:]
+ -[DockChannelProbeKISListenerIOUSBHost initWithSystemServiceController:nexusController:serialManager:serialController:deviceQueue:]
+ -[DockChannelProbeKISListenerIOUSBHost matchingDictionary]
+ -[DockChannelProbeKISListenerIOUSBHost nameForService:]
+ -[DockChannelProbeKISListenerIOUSBHost nexusController]
+ -[DockChannelProbeKISListenerIOUSBHost notificationPort]
+ -[DockChannelProbeKISListenerIOUSBHost notificationQueue]
+ -[DockChannelProbeKISListenerIOUSBHost performCleanup]
+ -[DockChannelProbeKISListenerIOUSBHost probeStateByPinServiceID]
+ -[DockChannelProbeKISListenerIOUSBHost serialController]
+ -[DockChannelProbeKISListenerIOUSBHost serialManager]
+ -[DockChannelProbeKISListenerIOUSBHost setActive:]
+ -[DockChannelProbeKISListenerIOUSBHost setDiscoveryCallback:]
+ -[DockChannelProbeKISListenerIOUSBHost setDiscoveryContext:]
+ -[DockChannelProbeKISListenerIOUSBHost setTerminationCallback:]
+ -[DockChannelProbeKISListenerIOUSBHost setTerminationContext:]
+ -[DockChannelProbeKISListenerIOUSBHost startListeningOnQueue:]
+ -[DockChannelProbeKISListenerIOUSBHost stopListening]
+ -[DockChannelProbeKISListenerIOUSBHost systemServiceController]
+ -[DockChannelProbeKISListenerIOUSBHost terminationCallback]
+ -[DockChannelProbeKISListenerIOUSBHost terminationContext]
+ -[DockChannelProbeListenerProbeState .cxx_destruct]
+ -[DockChannelProbeListenerProbeState dealloc]
+ -[DockChannelProbeListenerProbeState handleServiceRemoved:]
+ -[DockChannelProbeListenerProbeState initWithOwner:probeType:probeID:probeInterface:service:nexusController:]
+ -[DockChannelProbeListenerProbeState listening]
+ -[DockChannelProbeListenerProbeState nexusClient]
+ -[DockChannelProbeListenerProbeState nexusControllerClient]
+ -[DockChannelProbeListenerProbeState nexusController]
+ -[DockChannelProbeListenerProbeState nexus]
+ -[DockChannelProbeListenerProbeState owner]
+ -[DockChannelProbeListenerProbeState performCleanup]
+ -[DockChannelProbeListenerProbeState pinServiceClient]
+ -[DockChannelProbeListenerProbeState pinService]
+ -[DockChannelProbeListenerProbeState probeAddedToNexus]
+ -[DockChannelProbeListenerProbeState probeClient]
+ -[DockChannelProbeListenerProbeState probeID]
+ -[DockChannelProbeListenerProbeState probeInterface]
+ -[DockChannelProbeListenerProbeState probeType]
+ -[DockChannelProbeListenerProbeState startListeningForTermination]
+ -[DockChannelProbeNexus .cxx_destruct]
+ -[DockChannelProbeNexus acquireProbeInterfaceWithID:client:]
+ -[DockChannelProbeNexus addProbe:probeType:probeID:pinService:pinServiceID:client:]
+ -[DockChannelProbeNexus cleanupClient:]
+ -[DockChannelProbeNexus clientsRequiringProbes]
+ -[DockChannelProbeNexus clients]
+ -[DockChannelProbeNexus createClientWithSystemServiceID:description:]
+ -[DockChannelProbeNexus externalInterfacePointer]
+ -[DockChannelProbeNexus externalInterface]
+ -[DockChannelProbeNexus getID:]
+ -[DockChannelProbeNexus getLocation:client:]
+ -[DockChannelProbeNexus initWithNexusID:nexusLocation:queue:]
+ -[DockChannelProbeNexus interfacesLock]
+ -[DockChannelProbeNexus listAvailableProbeInterfaces:count:client:]
+ -[DockChannelProbeNexus matchClientsToProbes]
+ -[DockChannelProbeNexus nexusID]
+ -[DockChannelProbeNexus nexusLocation]
+ -[DockChannelProbeNexus performCleanup]
+ -[DockChannelProbeNexus probeIDArrayByPinServiceID]
+ -[DockChannelProbeNexus probeIDsForClient:]
+ -[DockChannelProbeNexus probeStatesByProbeID]
+ -[DockChannelProbeNexus queue]
+ -[DockChannelProbeNexus releaseProbeInterfaceWithID:client:]
+ -[DockChannelProbeNexus removeProbeWithID:client:]
+ -[DockChannelProbeNexus startListeningForClient:]
+ -[DockChannelProbeNexus stopListeningForClient:]
+ -[DockChannelProbeNexusClient .cxx_destruct]
+ -[DockChannelProbeNexusClient acquireProbeInterfaceWithID:]
+ -[DockChannelProbeNexusClient addProbe:probeType:probeID:pinService:pinServiceID:]
+ -[DockChannelProbeNexusClient clientDescription]
+ -[DockChannelProbeNexusClient discoveryCallback]
+ -[DockChannelProbeNexusClient discoveryContext]
+ -[DockChannelProbeNexusClient externalInterfacePointer]
+ -[DockChannelProbeNexusClient externalInterface]
+ -[DockChannelProbeNexusClient getLocation:]
+ -[DockChannelProbeNexusClient initWithNexus:pinServiceID:description:]
+ -[DockChannelProbeNexusClient listAvailableProbeInterfaces:count:]
+ -[DockChannelProbeNexusClient listening]
+ -[DockChannelProbeNexusClient nexus]
+ -[DockChannelProbeNexusClient pinServiceID]
+ -[DockChannelProbeNexusClient registerCallbacks:]
+ -[DockChannelProbeNexusClient releaseProbeInterfaceWithID:]
+ -[DockChannelProbeNexusClient removeProbeWithID:]
+ -[DockChannelProbeNexusClient setDiscoveryCallback:]
+ -[DockChannelProbeNexusClient setDiscoveryContext:]
+ -[DockChannelProbeNexusClient setListening:]
+ -[DockChannelProbeNexusClient setTerminationCallback:]
+ -[DockChannelProbeNexusClient setTerminationContext:]
+ -[DockChannelProbeNexusClient startListening]
+ -[DockChannelProbeNexusClient stopListening]
+ -[DockChannelProbeNexusClient terminationCallback]
+ -[DockChannelProbeNexusClient terminationContext]
+ -[DockChannelProbeNexusController .cxx_destruct]
+ -[DockChannelProbeNexusController acquireNexus:pinService:client:]
+ -[DockChannelProbeNexusController activeNexusStatesByID]
+ -[DockChannelProbeNexusController cleanupClient:]
+ -[DockChannelProbeNexusController clients]
+ -[DockChannelProbeNexusController copyNexusStateAndPinServiceForService:nexusState:pinService:]
+ -[DockChannelProbeNexusController createClientWithSystemService:description:]
+ -[DockChannelProbeNexusController externalInterfacePointer]
+ -[DockChannelProbeNexusController externalInterface]
+ -[DockChannelProbeNexusController initWithSystemServiceController:queue:]
+ -[DockChannelProbeNexusController isIntermediateHubNexusDevice:]
+ -[DockChannelProbeNexusController isProbeDeviceNexusDevice:]
+ -[DockChannelProbeNexusController isUSBHubDevice:]
+ -[DockChannelProbeNexusController lock]
+ -[DockChannelProbeNexusController nexusForNexusService:intermediate:]
+ -[DockChannelProbeNexusController nexusServiceForService:]
+ -[DockChannelProbeNexusController nexusStateForNexusService:]
+ -[DockChannelProbeNexusController performCleanup]
+ -[DockChannelProbeNexusController portServiceForService:]
+ -[DockChannelProbeNexusController queue]
+ -[DockChannelProbeNexusController releaseNexusAndPinServiceForClient:]
+ -[DockChannelProbeNexusController start]
+ -[DockChannelProbeNexusController stop]
+ -[DockChannelProbeNexusController systemServiceController]
+ -[DockChannelProbeNexusControllerClient .cxx_destruct]
+ -[DockChannelProbeNexusControllerClient acquireNexus:pinService:]
+ -[DockChannelProbeNexusControllerClient acquiredNexusAndPinService]
+ -[DockChannelProbeNexusControllerClient clientDescription]
+ -[DockChannelProbeNexusControllerClient controller]
+ -[DockChannelProbeNexusControllerClient externalInterfacePointer]
+ -[DockChannelProbeNexusControllerClient externalInterface]
+ -[DockChannelProbeNexusControllerClient initWithController:service:description:]
+ -[DockChannelProbeNexusControllerClient nexusState]
+ -[DockChannelProbeNexusControllerClient pinService]
+ -[DockChannelProbeNexusControllerClient releaseNexusAndPinService]
+ -[DockChannelProbeNexusControllerClient service]
+ -[DockChannelProbeNexusControllerClient setAcquiredNexusAndPinService:]
+ -[DockChannelProbeNexusControllerClient setNexusState:]
+ -[DockChannelProbeNexusControllerClient setPinService:]
+ -[DockChannelProbeNexusHostPort addProbe:probeType:probeID:pinService:pinServiceID:client:]
+ -[DockChannelProbeNexusProbeDevice addProbe:probeType:probeID:pinService:pinServiceID:client:]
+ -[DockChannelProbeNexusProbeDevice probeIDsForClient:]
+ -[DockChannelProbeNexusProbeState .cxx_destruct]
+ -[DockChannelProbeNexusProbeState initWithInterface:interfaceID:pinService:]
+ -[DockChannelProbeNexusProbeState pinService]
+ -[DockChannelProbeNexusState .cxx_destruct]
+ -[DockChannelProbeNexusState clients]
+ -[DockChannelProbeNexusState initWithNexus:nexusID:intermediate:]
+ -[DockChannelProbeNexusState intermediate]
+ -[DockChannelProbeNexusState nexusID]
+ -[DockChannelProbeNexusState nexus]
+ -[DockChannelProbeNexusUSBHub addProbe:probeType:probeID:pinService:pinServiceID:client:]
+ -[DockChannelSerialInterfaceBuffer .cxx_destruct]
+ -[DockChannelSerialInterfaceBuffer available]
+ -[DockChannelSerialInterfaceBuffer bufferLength]
+ -[DockChannelSerialInterfaceBuffer circularBuffer]
+ -[DockChannelSerialInterfaceBuffer empty]
+ -[DockChannelSerialInterfaceBuffer getData:outBuffer:]
+ -[DockChannelSerialInterfaceBuffer headOffset]
+ -[DockChannelSerialInterfaceBuffer initWithBufferSize:]
+ -[DockChannelSerialInterfaceBuffer mod:]
+ -[DockChannelSerialInterfaceBuffer putData:]
+ -[DockChannelSerialInterfaceBuffer setHeadOffset:]
+ -[DockChannelSerialInterfaceBuffer setTailOffset:]
+ -[DockChannelSerialInterfaceBuffer tailOffset]
+ -[DockChannelSerialInterfaceBuffer used]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial controllerAvailableSempahore]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:client:]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial discoveryIterator]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial handleDiscoveredService:]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial initWithQueue:]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial matchingDictionary]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial notificationPort]
+ -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial baseName]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial getBaseName:length:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial getSuffix:length:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial handleReadDataCallback:revents:t_lock:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial readTx:maxLength:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial rxOverflow]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial setServiceConnection:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial storeReadData:length:client:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial suffix]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial txDataAvailable:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial txIntermediateBuffer]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient connect_event_callback]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient getBaseName:length:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient getSuffix:length:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient handleHighWatermark]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient handleLowWatermark]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient hang_up_event_callback]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient highWatermarkStatus]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient readTx:maxLength:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient setConnect_event_callback:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient setHang_up_event_callback:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient setHighWatermarkStatus:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient setWater_mark_callback:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient txDataAvailable:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerialClient water_mark_callback]
+ -[DockChannelSerialInterfaceListenerKIS initWithKISManager:nexusController:]
+ -[DockChannelSerialInterfaceListenerKIS nexusController]
+ -[DockChannelSerialInterfaceWrapper initWithOwner:serialInterfaceID:baseName:channelIndex:probeClient:]
+ -[DockChannelSerialInterfaceWrapper probeClient]
+ -[DockChannelSerialInterfaceWrapper readTx:maxLength:]
+ -[DockChannelSerialInterfaceWrapper readTxDataAvailable:]
+ -[DockChannelSystemServiceClientWrapper client]
+ -[DockChannelSystemServiceClientWrapper dealloc]
+ -[DockChannelSystemServiceClientWrapper initWithService:description:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceClientWrapper service]
+ -[DockChannelSystemServiceControllerIORegistry .cxx_destruct]
+ -[DockChannelSystemServiceControllerIORegistry createSystemServiceFromIOService:]
+ -[DockChannelSystemServiceControllerIORegistry createSystemServiceFromServiceID:]
+ -[DockChannelSystemServiceControllerIORegistry externalInterfacePointer]
+ -[DockChannelSystemServiceControllerIORegistry externalInterface]
+ -[DockChannelSystemServiceControllerIORegistry findChildrenForService:children:count:]
+ -[DockChannelSystemServiceControllerIORegistry findParentForService:parent:]
+ -[DockChannelSystemServiceControllerIORegistry initWithQueue:]
+ -[DockChannelSystemServiceControllerIORegistry performCleanup]
+ -[DockChannelSystemServiceControllerIORegistry queue]
+ -[DockChannelSystemServiceIOService .cxx_destruct]
+ -[DockChannelSystemServiceIOService cleanupClient:]
+ -[DockChannelSystemServiceIOService createClientWithDescription:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceIOService externalInterfacePointer]
+ -[DockChannelSystemServiceIOService externalInterface]
+ -[DockChannelSystemServiceIOService getServiceClass:]
+ -[DockChannelSystemServiceIOService getServiceID:]
+ -[DockChannelSystemServiceIOService initWithService:queue:]
+ -[DockChannelSystemServiceIOService performCleanup]
+ -[DockChannelSystemServiceIOService queue]
+ -[DockChannelSystemServiceIOService serviceClass]
+ -[DockChannelSystemServiceIOService serviceID]
+ -[DockChannelSystemServiceIOService service]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper deviceClass]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper getPlatformCapability:size:uuid:]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper getProductName:length:]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper getSerialNumber:length:]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper initWithService:description:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper location]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper pid]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper portType]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper usbDeviceClient]
+ -[DockChannelSystemServiceUSBDeviceClientWrapper vid]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost .cxx_destruct]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost clientDescription]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost dealloc]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost externalInterfacePointer]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost externalInterface]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getClass:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getLocation:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getPID:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getPlatformCapability:size:uuid:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getPortType:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getProductName:length:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getSerialNumber:length:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost getVID:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost initWithService:serviceID:description:terminationCallback:terminationContext:queue:]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost interestNotificationObject]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost notificationPort]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost queue]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost serviceID]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost service]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost terminationCallback]
+ -[DockChannelSystemServiceUSBDeviceIOUSBHost terminationContext]
+ -[DockChannelSystemServiceUSBHostPortClientWrapper initWithService:description:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceUSBHostPortClientWrapper location]
+ -[DockChannelSystemServiceUSBHostPortClientWrapper usbHostPortClient]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost .cxx_destruct]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost clientDescription]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost dealloc]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost externalInterfacePointer]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost externalInterface]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost getLocation:]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost initWithService:serviceID:description:terminationCallback:terminationContext:queue:]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost interestNotificationObject]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost notificationPort]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost queue]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost serviceID]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost service]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost terminationCallback]
+ -[DockChannelSystemServiceUSBHostPortIOUSBHost terminationContext]
+ -[DockChannelSystemServiceUSBHubPortClientWrapper initWithService:description:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceUSBHubPortClientWrapper location]
+ -[DockChannelSystemServiceUSBHubPortClientWrapper portNumber]
+ -[DockChannelSystemServiceUSBHubPortClientWrapper usbHubPortClient]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost .cxx_destruct]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost clientDescription]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost dealloc]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost externalInterfacePointer]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost externalInterface]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost getLocation:]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost getPortNumber:]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost handleInterestNotificationForService:messageType:messageArgument:]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost initWithService:serviceID:description:terminationCallback:terminationContext:queue:]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost interestNotificationObject]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost notificationPort]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost queue]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost serviceID]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost service]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost terminationCallback]
+ -[DockChannelSystemServiceUSBHubPortIOUSBHost terminationContext]
+ -[DockChannelSystemServiceWrapper createClientWithDescription:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceWrapper createUSBDeviceClientWithDescription:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceWrapper createUSBHostPortClientWithDescription:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceWrapper createUSBHubPortClientWithDescription:terminationCallback:terminationContext:]
+ -[DockChannelSystemServiceWrapper dealloc]
+ -[DockChannelSystemServiceWrapper initWithService:transferOwnership:]
+ -[DockChannelSystemServiceWrapper serviceClass]
+ -[DockChannelSystemServiceWrapper serviceID]
+ -[DockChannelSystemServiceWrapper service]
+ -[DockChannelSystemServiceWrapper transferredOwnership]
+ -[KISInterfaceDebugUSB clearWatchdogStatus:]
+ -[KISInterfaceDebugUSB getIDEFormatVersion:]
+ -[KISInterfaceDebugUSB getTargetID:]
+ -[KISInterfaceDebugUSB getTransportService]
+ -[KISInterfaceDebugUSB hardwareInitStep]
+ -[KISInterfaceDebugUSB hardwareInitVersion]
+ -[KISInterfaceDebugUSB processHardwareV1Part1:data:length:]
+ -[KISInterfaceDebugUSB processHardwareV1Part2:data:length:]
+ -[KISInterfaceDebugUSB readMemoryFromAddress:length:sequenceID:endpointAddress:portal:payloadWriteFlags:]
+ -[KISInterfaceDebugUSB readRegistersFromIndex:count:sequenceID:endpointAddress:portal:]
+ -[KISInterfaceDebugUSB sendCommandAsync:length:endpoint:timeout:]
+ -[KISInterfaceDebugUSB setHardwareInitStep:]
+ -[KISInterfaceDebugUSB setHardwareInitVersion:]
+ -[KISInterfaceDebugUSB setTransferResponseFirstWord:]
+ -[KISInterfaceDebugUSB transferResponseFirstWord]
+ -[KISInterfaceDebugUSB writeMemoryFromAddress:length:data:sequenceID:endpointAddress:portal:payloadWriteFlags:]
+ -[KISInterfaceDebugUSB writeRegistersFromIndex:count:registers:sequenceID:endpointAddress:portal:]
+ -[KISInterfaceDebugUSBClient clearWatchdogStatus:]
+ -[KISInterfaceDebugUSBClient getIDEFormatVersion:]
+ -[KISInterfaceDebugUSBClient getTargetID:]
+ -[KISInterfaceDebugUSBClient getTransportService]
+ -[KISInterfaceDebugUSBClient readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:payloadWriteFlags:]
+ -[KISInterfaceDebugUSBClient readRegistersFromIndex:count:sequenceID:endpointAddress:portal:]
+ -[KISInterfaceDebugUSBClient writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:payloadWriteFlags:]
+ -[KISInterfaceDebugUSBClient writeRegistersFromIndex:count:registers:sequenceID:endpointAddress:toPortal:]
+ -[RSMHostChannelBuffer available]
+ -[RSMHostChannelBuffer bufferLength]
+ -[RSMHostChannelBuffer empty]
+ -[RSMHostChannelBuffer headOffset]
+ -[RSMHostChannelBuffer mod:]
+ -[RSMHostChannelBuffer setBufferLength:]
+ -[RSMHostChannelBuffer setHeadOffset:]
+ -[RSMHostChannelBuffer setHeadOffsetFromDoorbell:]
+ -[RSMHostChannelBuffer setTailOffset:]
+ -[RSMHostChannelBuffer setTailOffsetFromDoorbell:]
+ -[RSMHostChannelBuffer tailOffset]
+ -[RSMHostChannelBuffer used]
+ GCC_except_table12
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table40
+ GCC_except_table5
+ OBJC_IVAR_$_DebugUSBDeviceInterfaceIOUSBHost._transaction
+ OBJC_IVAR_$_DebugUSBInterfaceIOUSBHost._systemServiceController
+ OBJC_IVAR_$_DebugUSBInterfaceListenerIOUSBHost._systemServiceController
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._dockChannelsWithBackPressure
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._dockChannelsWithPush
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._lock
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._nexus
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._nexusClient
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._nexusController
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._nexusControllerClient
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._pinService
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._platformRequiresPolling
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._ppmEnabled
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._ppmEnabledDockChannels
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._ppmEndpoint
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._probeSerialState
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._transportService
+ OBJC_IVAR_$_DockChannelInterfaceKISPAM._workloopScheduled
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._createdSerialInterfaces
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._nexusClient
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._owner
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._probeBaseName
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._probeInterface
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._probeInterfaceClient
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._probeInterfaceID
+ OBJC_IVAR_$_DockChannelInterfaceProbeSerialState._serialInterfaces
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._active
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._deviceQueue
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._matchingArray
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._nexusController
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._notificationPort
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._notificationQueue
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._probeStateByPinServiceID
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._serialController
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._serialManager
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost._systemServiceController
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost.discoveryCallback
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost.discoveryContext
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost.terminationCallback
+ OBJC_IVAR_$_DockChannelProbeDeviceListenerIOUSBHost.terminationContext
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._discoveryIterator
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._matchingDictionary
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._pid
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._serialPrefix
+ OBJC_IVAR_$_DockChannelProbeDeviceMatching._vid
+ OBJC_IVAR_$_DockChannelProbeInterface._baseName
+ OBJC_IVAR_$_DockChannelProbeInterface._clients
+ OBJC_IVAR_$_DockChannelProbeInterface._interfacesLock
+ OBJC_IVAR_$_DockChannelProbeInterface._nexusID
+ OBJC_IVAR_$_DockChannelProbeInterface._nexusLocation
+ OBJC_IVAR_$_DockChannelProbeInterface._permanentSuffixes
+ OBJC_IVAR_$_DockChannelProbeInterface._portID
+ OBJC_IVAR_$_DockChannelProbeInterface._portLocation
+ OBJC_IVAR_$_DockChannelProbeInterface._probeID
+ OBJC_IVAR_$_DockChannelProbeInterface._queue
+ OBJC_IVAR_$_DockChannelProbeInterface._serialController
+ OBJC_IVAR_$_DockChannelProbeInterface._serialControllerClient
+ OBJC_IVAR_$_DockChannelProbeInterface._serialInterfaceStatesByID
+ OBJC_IVAR_$_DockChannelProbeInterface._serialManager
+ OBJC_IVAR_$_DockChannelProbeInterface._serialManagerClient
+ OBJC_IVAR_$_DockChannelProbeInterface._transaction
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._clientDescription
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._discoveryCallback
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._discoveryContext
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._externalInterface
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._interface
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._listening
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._terminationCallback
+ OBJC_IVAR_$_DockChannelProbeInterfaceClient._terminationContext
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._active
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._deviceQueue
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._discoveryIterator
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._matchingDictionary
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._nexusController
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._notificationPort
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._notificationQueue
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._probeStateByPinServiceID
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._serialController
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._serialManager
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost._systemServiceController
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost.discoveryCallback
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost.discoveryContext
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost.terminationCallback
+ OBJC_IVAR_$_DockChannelProbeKISListenerIOUSBHost.terminationContext
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._listening
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._nexus
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._nexusClient
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._nexusController
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._nexusControllerClient
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._owner
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._pinService
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._pinServiceClient
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._probeAddedToNexus
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._probeClient
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._probeID
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._probeInterface
+ OBJC_IVAR_$_DockChannelProbeListenerProbeState._probeType
+ OBJC_IVAR_$_DockChannelProbeNexus._clients
+ OBJC_IVAR_$_DockChannelProbeNexus._clientsRequiringProbes
+ OBJC_IVAR_$_DockChannelProbeNexus._externalInterface
+ OBJC_IVAR_$_DockChannelProbeNexus._interfacesLock
+ OBJC_IVAR_$_DockChannelProbeNexus._nexusID
+ OBJC_IVAR_$_DockChannelProbeNexus._nexusLocation
+ OBJC_IVAR_$_DockChannelProbeNexus._probeIDArrayByPinServiceID
+ OBJC_IVAR_$_DockChannelProbeNexus._probeStatesByProbeID
+ OBJC_IVAR_$_DockChannelProbeNexus._queue
+ OBJC_IVAR_$_DockChannelProbeNexusClient._clientDescription
+ OBJC_IVAR_$_DockChannelProbeNexusClient._discoveryCallback
+ OBJC_IVAR_$_DockChannelProbeNexusClient._discoveryContext
+ OBJC_IVAR_$_DockChannelProbeNexusClient._externalInterface
+ OBJC_IVAR_$_DockChannelProbeNexusClient._listening
+ OBJC_IVAR_$_DockChannelProbeNexusClient._nexus
+ OBJC_IVAR_$_DockChannelProbeNexusClient._pinServiceID
+ OBJC_IVAR_$_DockChannelProbeNexusClient._terminationCallback
+ OBJC_IVAR_$_DockChannelProbeNexusClient._terminationContext
+ OBJC_IVAR_$_DockChannelProbeNexusController._activeNexusStatesByID
+ OBJC_IVAR_$_DockChannelProbeNexusController._clients
+ OBJC_IVAR_$_DockChannelProbeNexusController._externalInterface
+ OBJC_IVAR_$_DockChannelProbeNexusController._lock
+ OBJC_IVAR_$_DockChannelProbeNexusController._queue
+ OBJC_IVAR_$_DockChannelProbeNexusController._systemServiceController
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._acquiredNexusAndPinService
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._clientDescription
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._controller
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._externalInterface
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._nexusState
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._pinService
+ OBJC_IVAR_$_DockChannelProbeNexusControllerClient._service
+ OBJC_IVAR_$_DockChannelProbeNexusProbeState._pinService
+ OBJC_IVAR_$_DockChannelProbeNexusState._clients
+ OBJC_IVAR_$_DockChannelProbeNexusState._intermediate
+ OBJC_IVAR_$_DockChannelProbeNexusState._nexus
+ OBJC_IVAR_$_DockChannelProbeNexusState._nexusID
+ OBJC_IVAR_$_DockChannelSerialInterfaceBuffer._circularBuffer
+ OBJC_IVAR_$_DockChannelSerialInterfaceBuffer._headOffset
+ OBJC_IVAR_$_DockChannelSerialInterfaceBuffer._tailOffset
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._controllerAvailableSempahore
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._discoveryIterator
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._matchingDictionary
+ OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._notificationPort
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerial._baseName
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerial._rxOverflow
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerial._suffix
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerial._txIntermediateBuffer
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerialClient._connect_event_callback
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerialClient._hang_up_event_callback
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerialClient._highWatermarkStatus
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerialClient._water_mark_callback
+ OBJC_IVAR_$_DockChannelSerialInterfaceListenerKIS._nexusController
+ OBJC_IVAR_$_DockChannelSerialInterfaceWrapper._probeClient
+ OBJC_IVAR_$_DockChannelSystemServiceClientWrapper._client
+ OBJC_IVAR_$_DockChannelSystemServiceClientWrapper._service
+ OBJC_IVAR_$_DockChannelSystemServiceControllerIORegistry._externalInterface
+ OBJC_IVAR_$_DockChannelSystemServiceControllerIORegistry._queue
+ OBJC_IVAR_$_DockChannelSystemServiceIOService._externalInterface
+ OBJC_IVAR_$_DockChannelSystemServiceIOService._queue
+ OBJC_IVAR_$_DockChannelSystemServiceIOService._service
+ OBJC_IVAR_$_DockChannelSystemServiceIOService._serviceClass
+ OBJC_IVAR_$_DockChannelSystemServiceIOService._serviceID
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._deviceClass
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._location
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._pid
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._portType
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._usbDeviceClient
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceClientWrapper._vid
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._clientDescription
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._externalInterface
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._interestNotificationObject
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._notificationPort
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._queue
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._service
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._serviceID
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._terminationCallback
+ OBJC_IVAR_$_DockChannelSystemServiceUSBDeviceIOUSBHost._terminationContext
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortClientWrapper._location
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortClientWrapper._usbHostPortClient
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._clientDescription
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._externalInterface
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._interestNotificationObject
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._notificationPort
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._queue
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._service
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._serviceID
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._terminationCallback
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHostPortIOUSBHost._terminationContext
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortClientWrapper._location
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortClientWrapper._portNumber
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortClientWrapper._usbHubPortClient
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._clientDescription
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._externalInterface
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._interestNotificationObject
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._notificationPort
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._queue
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._service
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._serviceID
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._terminationCallback
+ OBJC_IVAR_$_DockChannelSystemServiceUSBHubPortIOUSBHost._terminationContext
+ OBJC_IVAR_$_DockChannelSystemServiceWrapper._service
+ OBJC_IVAR_$_DockChannelSystemServiceWrapper._serviceClass
+ OBJC_IVAR_$_DockChannelSystemServiceWrapper._serviceID
+ OBJC_IVAR_$_DockChannelSystemServiceWrapper._transferredOwnership
+ OBJC_IVAR_$_KISInterfaceDebugUSB._hardwareInitStep
+ OBJC_IVAR_$_KISInterfaceDebugUSB._hardwareInitVersion
+ OBJC_IVAR_$_KISInterfaceDebugUSB._transferResponseFirstWord
+ OBJC_IVAR_$_RSMHostChannelBuffer._bufferLength
+ OBJC_IVAR_$_RSMHostChannelBuffer._headOffset
+ OBJC_IVAR_$_RSMHostChannelBuffer._tailOffset
+ _IOObjectConformsTo
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryIDMatching
+ _IOServiceAddInterestNotification
+ _OBJC_CLASS_$_DockChannelInterfaceProbeSerialState
+ _OBJC_CLASS_$_DockChannelProbeDeviceListenerIOUSBHost
+ _OBJC_CLASS_$_DockChannelProbeDeviceMatching
+ _OBJC_CLASS_$_DockChannelProbeInterface
+ _OBJC_CLASS_$_DockChannelProbeInterfaceClient
+ _OBJC_CLASS_$_DockChannelProbeKISListenerIOUSBHost
+ _OBJC_CLASS_$_DockChannelProbeListenerProbeState
+ _OBJC_CLASS_$_DockChannelProbeNexus
+ _OBJC_CLASS_$_DockChannelProbeNexusClient
+ _OBJC_CLASS_$_DockChannelProbeNexusController
+ _OBJC_CLASS_$_DockChannelProbeNexusControllerClient
+ _OBJC_CLASS_$_DockChannelProbeNexusHostPort
+ _OBJC_CLASS_$_DockChannelProbeNexusProbeDevice
+ _OBJC_CLASS_$_DockChannelProbeNexusProbeState
+ _OBJC_CLASS_$_DockChannelProbeNexusState
+ _OBJC_CLASS_$_DockChannelProbeNexusUSBHub
+ _OBJC_CLASS_$_DockChannelSerialInterfaceBuffer
+ _OBJC_CLASS_$_DockChannelSystemServiceClientWrapper
+ _OBJC_CLASS_$_DockChannelSystemServiceControllerIORegistry
+ _OBJC_CLASS_$_DockChannelSystemServiceIOService
+ _OBJC_CLASS_$_DockChannelSystemServiceUSBDeviceClientWrapper
+ _OBJC_CLASS_$_DockChannelSystemServiceUSBDeviceIOUSBHost
+ _OBJC_CLASS_$_DockChannelSystemServiceUSBHostPortClientWrapper
+ _OBJC_CLASS_$_DockChannelSystemServiceUSBHostPortIOUSBHost
+ _OBJC_CLASS_$_DockChannelSystemServiceUSBHubPortClientWrapper
+ _OBJC_CLASS_$_DockChannelSystemServiceUSBHubPortIOUSBHost
+ _OBJC_CLASS_$_DockChannelSystemServiceWrapper
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_RSMHostChannelBuffer
+ _OBJC_METACLASS_$_DockChannelInterfaceProbeSerialState
+ _OBJC_METACLASS_$_DockChannelProbeDeviceListenerIOUSBHost
+ _OBJC_METACLASS_$_DockChannelProbeDeviceMatching
+ _OBJC_METACLASS_$_DockChannelProbeInterface
+ _OBJC_METACLASS_$_DockChannelProbeInterfaceClient
+ _OBJC_METACLASS_$_DockChannelProbeKISListenerIOUSBHost
+ _OBJC_METACLASS_$_DockChannelProbeListenerProbeState
+ _OBJC_METACLASS_$_DockChannelProbeNexus
+ _OBJC_METACLASS_$_DockChannelProbeNexusClient
+ _OBJC_METACLASS_$_DockChannelProbeNexusController
+ _OBJC_METACLASS_$_DockChannelProbeNexusControllerClient
+ _OBJC_METACLASS_$_DockChannelProbeNexusHostPort
+ _OBJC_METACLASS_$_DockChannelProbeNexusProbeDevice
+ _OBJC_METACLASS_$_DockChannelProbeNexusProbeState
+ _OBJC_METACLASS_$_DockChannelProbeNexusState
+ _OBJC_METACLASS_$_DockChannelProbeNexusUSBHub
+ _OBJC_METACLASS_$_DockChannelSerialInterfaceBuffer
+ _OBJC_METACLASS_$_DockChannelSystemServiceClientWrapper
+ _OBJC_METACLASS_$_DockChannelSystemServiceControllerIORegistry
+ _OBJC_METACLASS_$_DockChannelSystemServiceIOService
+ _OBJC_METACLASS_$_DockChannelSystemServiceUSBDeviceClientWrapper
+ _OBJC_METACLASS_$_DockChannelSystemServiceUSBDeviceIOUSBHost
+ _OBJC_METACLASS_$_DockChannelSystemServiceUSBHostPortClientWrapper
+ _OBJC_METACLASS_$_DockChannelSystemServiceUSBHostPortIOUSBHost
+ _OBJC_METACLASS_$_DockChannelSystemServiceUSBHubPortClientWrapper
+ _OBJC_METACLASS_$_DockChannelSystemServiceUSBHubPortIOUSBHost
+ _OBJC_METACLASS_$_DockChannelSystemServiceWrapper
+ _OBJC_METACLASS_$_RSMHostChannelBuffer
+ __49-[DockChannelProbeNexus startListeningForClient:]_block_invoke.16
+ __50-[DockChannelProbeNexus removeProbeWithID:client:]_block_invoke.22
+ __56-[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:]_block_invoke.3
+ __73-[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:]_block_invoke.44
+ __73-[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:]_block_invoke.47
+ __OBJC_$_CLASS_METHODS_DockChannelSystemServiceIOService
+ __OBJC_$_INSTANCE_METHODS_DockChannelInterfaceProbeSerialState
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeDeviceMatching
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeInterface
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeInterfaceClient
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeKISListenerIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeListenerProbeState
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexus
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusClient
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusController
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusControllerClient
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusHostPort
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusProbeDevice
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusProbeState
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusState
+ __OBJC_$_INSTANCE_METHODS_DockChannelProbeNexusUSBHub
+ __OBJC_$_INSTANCE_METHODS_DockChannelSerialInterfaceBuffer
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceClientWrapper
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceControllerIORegistry
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceIOService
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBDeviceClientWrapper
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBDeviceIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHostPortClientWrapper
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHostPortIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHubPortClientWrapper
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceUSBHubPortIOUSBHost
+ __OBJC_$_INSTANCE_METHODS_DockChannelSystemServiceWrapper
+ __OBJC_$_INSTANCE_METHODS_RSMHostChannelBuffer
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelInterfaceProbeSerialState
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeDeviceMatching
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeInterface
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeInterfaceClient
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeKISListenerIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeListenerProbeState
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeNexus
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeNexusClient
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeNexusController
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeNexusControllerClient
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeNexusProbeState
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelProbeNexusState
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSerialInterfaceBuffer
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceControllerIORegistry
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceIOService
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBDeviceClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBDeviceIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHostPortClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHostPortIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHubPortClientWrapper
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceUSBHubPortIOUSBHost
+ __OBJC_$_INSTANCE_VARIABLES_DockChannelSystemServiceWrapper
+ __OBJC_$_INSTANCE_VARIABLES_RSMHostChannelBuffer
+ __OBJC_$_PROP_LIST_DockChannelInterfaceProbeSerialState
+ __OBJC_$_PROP_LIST_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_$_PROP_LIST_DockChannelProbeDeviceMatching
+ __OBJC_$_PROP_LIST_DockChannelProbeInterface
+ __OBJC_$_PROP_LIST_DockChannelProbeInterfaceClient
+ __OBJC_$_PROP_LIST_DockChannelProbeKISListenerIOUSBHost
+ __OBJC_$_PROP_LIST_DockChannelProbeListenerProbeState
+ __OBJC_$_PROP_LIST_DockChannelProbeNexus
+ __OBJC_$_PROP_LIST_DockChannelProbeNexusClient
+ __OBJC_$_PROP_LIST_DockChannelProbeNexusController
+ __OBJC_$_PROP_LIST_DockChannelProbeNexusControllerClient
+ __OBJC_$_PROP_LIST_DockChannelProbeNexusProbeState
+ __OBJC_$_PROP_LIST_DockChannelProbeNexusState
+ __OBJC_$_PROP_LIST_DockChannelSerialInterfaceBuffer
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceClientWrapper
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceControllerIORegistry
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceIOService
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBDeviceClientWrapper
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBDeviceIOUSBHost
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHostPortClientWrapper
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHostPortIOUSBHost
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHubPortClientWrapper
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceUSBHubPortIOUSBHost
+ __OBJC_$_PROP_LIST_DockChannelSystemServiceWrapper
+ __OBJC_$_PROP_LIST_RSMHostChannelBuffer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DockChannelInterfaceProbeSerialStateDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DockChannelProbeListenerProbeStateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DockChannelInterfaceProbeSerialStateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DockChannelProbeListenerProbeStateDelegate
+ __OBJC_$_PROTOCOL_REFS_DockChannelInterfaceProbeSerialStateDelegate
+ __OBJC_$_PROTOCOL_REFS_DockChannelProbeListenerProbeStateDelegate
+ __OBJC_CLASS_PROTOCOLS_$_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_CLASS_PROTOCOLS_$_DockChannelProbeInterface
+ __OBJC_CLASS_PROTOCOLS_$_DockChannelProbeKISListenerIOUSBHost
+ __OBJC_CLASS_RO_$_DockChannelInterfaceProbeSerialState
+ __OBJC_CLASS_RO_$_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_CLASS_RO_$_DockChannelProbeDeviceMatching
+ __OBJC_CLASS_RO_$_DockChannelProbeInterface
+ __OBJC_CLASS_RO_$_DockChannelProbeInterfaceClient
+ __OBJC_CLASS_RO_$_DockChannelProbeKISListenerIOUSBHost
+ __OBJC_CLASS_RO_$_DockChannelProbeListenerProbeState
+ __OBJC_CLASS_RO_$_DockChannelProbeNexus
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusClient
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusController
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusControllerClient
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusHostPort
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusProbeDevice
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusProbeState
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusState
+ __OBJC_CLASS_RO_$_DockChannelProbeNexusUSBHub
+ __OBJC_CLASS_RO_$_DockChannelSerialInterfaceBuffer
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceClientWrapper
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceControllerIORegistry
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceIOService
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBDeviceClientWrapper
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBDeviceIOUSBHost
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHostPortClientWrapper
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHostPortIOUSBHost
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHubPortClientWrapper
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceUSBHubPortIOUSBHost
+ __OBJC_CLASS_RO_$_DockChannelSystemServiceWrapper
+ __OBJC_CLASS_RO_$_RSMHostChannelBuffer
+ __OBJC_LABEL_PROTOCOL_$_DockChannelInterfaceProbeSerialStateDelegate
+ __OBJC_LABEL_PROTOCOL_$_DockChannelProbeListenerProbeStateDelegate
+ __OBJC_METACLASS_RO_$_DockChannelInterfaceProbeSerialState
+ __OBJC_METACLASS_RO_$_DockChannelProbeDeviceListenerIOUSBHost
+ __OBJC_METACLASS_RO_$_DockChannelProbeDeviceMatching
+ __OBJC_METACLASS_RO_$_DockChannelProbeInterface
+ __OBJC_METACLASS_RO_$_DockChannelProbeInterfaceClient
+ __OBJC_METACLASS_RO_$_DockChannelProbeKISListenerIOUSBHost
+ __OBJC_METACLASS_RO_$_DockChannelProbeListenerProbeState
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexus
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusClient
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusController
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusControllerClient
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusHostPort
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusProbeDevice
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusProbeState
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusState
+ __OBJC_METACLASS_RO_$_DockChannelProbeNexusUSBHub
+ __OBJC_METACLASS_RO_$_DockChannelSerialInterfaceBuffer
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceClientWrapper
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceControllerIORegistry
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceIOService
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBDeviceClientWrapper
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBDeviceIOUSBHost
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHostPortClientWrapper
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHostPortIOUSBHost
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHubPortClientWrapper
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceUSBHubPortIOUSBHost
+ __OBJC_METACLASS_RO_$_DockChannelSystemServiceWrapper
+ __OBJC_METACLASS_RO_$_RSMHostChannelBuffer
+ __OBJC_PROTOCOL_$_DockChannelInterfaceProbeSerialStateDelegate
+ __OBJC_PROTOCOL_$_DockChannelProbeListenerProbeStateDelegate
+ ___173-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:client:]_block_invoke
+ ___39-[DockChannelProbeNexus cleanupClient:]_block_invoke
+ ___43-[DockChannelProbeInterface cleanupClient:]_block_invoke
+ ___46-[DockChannelInterfaceKISPAM scheduleWorkloop]_block_invoke
+ ___48-[DockChannelProbeNexus stopListeningForClient:]_block_invoke
+ ___49-[DockChannelProbeNexus startListeningForClient:]_block_invoke
+ ___50-[DockChannelProbeNexus removeProbeWithID:client:]_block_invoke
+ ___52-[DockChannelProbeInterface stopListeningForClient:]_block_invoke
+ ___53-[DockChannelProbeInterface startListeningForClient:]_block_invoke
+ ___53-[DockChannelProbeKISListenerIOUSBHost stopListening]_block_invoke
+ ___53-[DockChannelSystemServiceUSBDeviceIOUSBHost dealloc]_block_invoke
+ ___54-[DockChannelProbeInterface addSerialInterfaceWithID:]_block_invoke
+ ___54-[DockChannelSystemServiceUSBHubPortIOUSBHost dealloc]_block_invoke
+ ___55-[DockChannelSystemServiceUSBHostPortIOUSBHost dealloc]_block_invoke
+ ___56-[DockChannelInterfaceKISPAM handleProbeInterfaceAdded:]_block_invoke
+ ___56-[DockChannelProbeDeviceListenerIOUSBHost stopListening]_block_invoke
+ ___57-[DockChannelProbeInterface createClientWithDescription:]_block_invoke
+ ___57-[DockChannelProbeInterface removeSerialInterfaceWithID:]_block_invoke
+ ___58-[DockChannelInterfaceKISPAM handleProbeInterfaceRemoved:]_block_invoke
+ ___62-[DockChannelProbeKISListenerIOUSBHost startListeningOnQueue:]_block_invoke
+ ___64-[DockChannelInterfaceKISPAM handleSerialInterfaceAdded:suffix:]_block_invoke
+ ___64-[DockChannelProbeKISListenerIOUSBHost handlePinServiceRemoval:]_block_invoke
+ ___65-[DockChannelProbeDeviceListenerIOUSBHost startListeningOnQueue:]_block_invoke
+ ___66-[DockChannelInterfaceKISPAM handleSerialInterfaceRemoved:suffix:]_block_invoke
+ ___67-[DockChannelProbeDeviceListenerIOUSBHost handlePinServiceRemoval:]_block_invoke
+ ___67-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial stop]_block_invoke
+ ___67-[DockChannelSerialInterfaceIOUserDockChannelSerial cleanupClient:]_block_invoke
+ ___67-[DockChannelSerialInterfaceIOUserDockChannelSerial performCleanup]_block_invoke
+ ___68-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial start]_block_invoke
+ ___69-[DockChannelProbeNexus createClientWithSystemServiceID:description:]_block_invoke
+ ___69-[DockChannelSerialInterfaceIOUserDockChannelSerial txDataAvailable:]_block_invoke
+ ___70-[DockChannelSerialInterfaceIOUserDockChannelSerial readTx:maxLength:]_block_invoke
+ ___72-[DockChannelSerialInterfaceIOUserDockChannelSerial stopWithCompletion:]_block_invoke
+ ___81-[DockChannelSerialInterfaceIOUserDockChannelSerial storeReadData:length:client:]_block_invoke
+ ___83-[DockChannelProbeNexus addProbe:probeType:probeID:pinService:pinServiceID:client:]_block_invoke
+ ___86-[DockChannelInterfaceKISPAM initWithKISInterfaceID:kisManager:nexusController:queue:]_block_invoke
+ ___atomic_load
+ ___block_descriptor_148_e8_32s40r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40r_e5_v8?0l
+ ___block_descriptor_68_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56w
+ ___destroy_helper_block_e8_32s40s48s56w
+ ___memset_chk
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_0_1_4_0
+ ___os_log_helper_16_0_1_8_0
+ ___os_log_helper_16_0_2_4_0_4_0
+ ___os_log_helper_16_0_2_8_0_4_0
+ ___os_log_helper_16_0_3_8_0_4_0_4_0
+ ___os_log_helper_16_0_3_8_0_8_0_4_0
+ ___os_log_helper_16_0_4_8_0_4_0_4_0_4_0
+ ___os_log_helper_16_2_10_8_32_8_0_8_0_8_0_4_0_4_0_4_0_4_0_4_0_4_0
+ ___os_log_helper_16_2_11_8_32_8_32_8_0_8_0_8_0_4_0_4_0_4_0_4_0_4_0_4_0
+ ___os_log_helper_16_2_1_8_32
+ ___os_log_helper_16_2_1_8_64
+ ___os_log_helper_16_2_2_4_0_8_32
+ ___os_log_helper_16_2_2_4_0_8_64
+ ___os_log_helper_16_2_2_8_0_8_64
+ ___os_log_helper_16_2_2_8_32_4_0
+ ___os_log_helper_16_2_2_8_32_8_0
+ ___os_log_helper_16_2_2_8_32_8_32
+ ___os_log_helper_16_2_2_8_32_8_64
+ ___os_log_helper_16_2_2_8_64_8_64
+ ___os_log_helper_16_2_3_8_0_8_0_8_32
+ ___os_log_helper_16_2_3_8_0_8_64_4_0
+ ___os_log_helper_16_2_3_8_0_8_64_8_0
+ ___os_log_helper_16_2_3_8_0_8_64_8_32
+ ___os_log_helper_16_2_3_8_0_8_64_8_64
+ ___os_log_helper_16_2_3_8_32_4_0_4_0
+ ___os_log_helper_16_2_3_8_32_4_0_8_64
+ ___os_log_helper_16_2_3_8_32_8_0_4_0
+ ___os_log_helper_16_2_3_8_32_8_0_8_0
+ ___os_log_helper_16_2_3_8_32_8_0_8_32
+ ___os_log_helper_16_2_3_8_32_8_0_8_64
+ ___os_log_helper_16_2_3_8_32_8_32_4_0
+ ___os_log_helper_16_2_3_8_32_8_32_8_0
+ ___os_log_helper_16_2_3_8_32_8_32_8_32
+ ___os_log_helper_16_2_3_8_32_8_64_4_0
+ ___os_log_helper_16_2_3_8_32_8_64_8_0
+ ___os_log_helper_16_2_3_8_32_8_64_8_32
+ ___os_log_helper_16_2_3_8_32_8_64_8_64
+ ___os_log_helper_16_2_3_8_64_8_0_8_0
+ ___os_log_helper_16_2_3_8_64_8_64_8_0
+ ___os_log_helper_16_2_4_8_0_8_64_8_64_4_0
+ ___os_log_helper_16_2_4_8_32_4_0_4_0_8_64
+ ___os_log_helper_16_2_4_8_32_4_0_8_64_8_64
+ ___os_log_helper_16_2_4_8_32_8_0_4_0_8_0
+ ___os_log_helper_16_2_4_8_32_8_0_8_0_8_0
+ ___os_log_helper_16_2_4_8_32_8_0_8_0_8_64
+ ___os_log_helper_16_2_4_8_32_8_0_8_32_4_0
+ ___os_log_helper_16_2_4_8_32_8_0_8_32_8_32
+ ___os_log_helper_16_2_4_8_32_8_0_8_32_8_64
+ ___os_log_helper_16_2_4_8_32_8_32_4_0_4_0
+ ___os_log_helper_16_2_4_8_32_8_32_4_0_8_32
+ ___os_log_helper_16_2_4_8_32_8_32_8_0_4_0
+ ___os_log_helper_16_2_4_8_32_8_32_8_32_4_0
+ ___os_log_helper_16_2_4_8_32_8_32_8_32_8_32
+ ___os_log_helper_16_2_4_8_32_8_64_4_0_4_0
+ ___os_log_helper_16_2_4_8_32_8_64_8_0_4_0
+ ___os_log_helper_16_2_4_8_32_8_64_8_0_8_0
+ ___os_log_helper_16_2_4_8_32_8_64_8_32_8_64
+ ___os_log_helper_16_2_4_8_32_8_64_8_64_8_64
+ ___os_log_helper_16_2_5_8_0_4_0_4_0_4_0_8_32
+ ___os_log_helper_16_2_5_8_0_8_64_8_64_4_0_8_0
+ ___os_log_helper_16_2_5_8_0_8_64_8_64_8_32_4_0
+ ___os_log_helper_16_2_5_8_32_4_0_8_0_8_64_8_64
+ ___os_log_helper_16_2_5_8_32_4_0_8_64_8_64_8_64
+ ___os_log_helper_16_2_5_8_32_8_0_8_0_4_0_4_0
+ ___os_log_helper_16_2_5_8_32_8_0_8_32_8_32_8_32
+ ___os_log_helper_16_2_5_8_32_8_32_8_0_8_0_8_32
+ ___os_log_helper_16_2_5_8_32_8_32_8_32_8_0_8_0
+ ___os_log_helper_16_2_5_8_32_8_32_8_32_8_32_8_32
+ ___os_log_helper_16_2_7_8_32_4_0_4_0_8_0_8_0_4_0_4_0
+ ___os_log_helper_16_2_8_8_32_4_0_4_0_8_0_8_0_4_0_4_0_8_32
+ ___os_log_helper_16_2_9_8_32_8_0_8_0_8_0_4_0_4_0_4_0_4_0_4_0
+ __block_literal_global.46
+ __block_literal_global.49
+ __block_literal_global.5
+ _debug_usb_interface_client_transport_service
+ _debug_usb_interface_iousbhost_transport_service
+ _device_interface_configuration_behavior_count
+ _device_interface_configuration_behaviors
+ _device_interface_configuration_cleanup
+ _device_interface_configuration_daemon_enabled
+ _device_interface_configuration_dock_channels_enabled
+ _device_interface_configuration_external_interface_enabled
+ _device_interface_configuration_rsm_enabled
+ _dock_channel_interface_kis_pam_endpoint_command_completion_callback
+ _dock_channel_interface_kis_pam_endpoint_response_callback
+ _dock_channel_interface_kis_pam_handle_connect_event
+ _dock_channel_interface_kis_pam_handle_hang_up_event
+ _dock_channel_interface_kis_pam_handle_probe_interface_added
+ _dock_channel_interface_kis_pam_handle_probe_interface_removed
+ _dock_channel_interface_kis_pam_handle_water_mark_event
+ _dock_channel_interface_probe_serial_state_handle_serial_interface_added
+ _dock_channel_interface_probe_serial_state_handle_serial_interface_removed
+ _dock_channel_probe_device_listener_iousbhost_create
+ _dock_channel_probe_device_listener_iousbhost_services_discovered
+ _dock_channel_probe_interface_client_acquire_serial_interface
+ _dock_channel_probe_interface_client_base_name
+ _dock_channel_probe_interface_client_cleanup_all_serial_interfaces
+ _dock_channel_probe_interface_client_cleanup_serial_interface
+ _dock_channel_probe_interface_client_create_serial_interface
+ _dock_channel_probe_interface_client_list_available_serial_interfaces
+ _dock_channel_probe_interface_client_register_callbacks
+ _dock_channel_probe_interface_client_release_serial_interface
+ _dock_channel_probe_interface_client_set_nexus_id
+ _dock_channel_probe_interface_client_set_nexus_location
+ _dock_channel_probe_interface_client_set_port_id
+ _dock_channel_probe_interface_client_set_port_location
+ _dock_channel_probe_interface_client_start_listening
+ _dock_channel_probe_interface_client_stop_listening
+ _dock_channel_probe_interface_create
+ _dock_channel_probe_interface_serial_interface_added
+ _dock_channel_probe_interface_serial_interface_removed
+ _dock_channel_probe_kis_listener_iousbhost_create
+ _dock_channel_probe_kis_listener_iousbhost_services_discovered
+ _dock_channel_probe_listener_probe_state_service_removed
+ _dock_channel_probe_nexus_cleanup
+ _dock_channel_probe_nexus_cleanup_client
+ _dock_channel_probe_nexus_client_acquire_probe_interface
+ _dock_channel_probe_nexus_client_add_probe
+ _dock_channel_probe_nexus_client_list_available_probe_interfaces
+ _dock_channel_probe_nexus_client_location
+ _dock_channel_probe_nexus_client_objc_acquire_probe_interface
+ _dock_channel_probe_nexus_client_objc_add_probe
+ _dock_channel_probe_nexus_client_objc_functions
+ _dock_channel_probe_nexus_client_objc_list_available_probe_interfaces
+ _dock_channel_probe_nexus_client_objc_location
+ _dock_channel_probe_nexus_client_objc_register_callbacks
+ _dock_channel_probe_nexus_client_objc_release_probe_interface
+ _dock_channel_probe_nexus_client_objc_remove_probe
+ _dock_channel_probe_nexus_client_objc_start_listening
+ _dock_channel_probe_nexus_client_objc_stop_listening
+ _dock_channel_probe_nexus_client_register_callbacks
+ _dock_channel_probe_nexus_client_release_probe_interface
+ _dock_channel_probe_nexus_client_remove_probe
+ _dock_channel_probe_nexus_client_start_listening
+ _dock_channel_probe_nexus_client_stop_listening
+ _dock_channel_probe_nexus_controller_cleanup
+ _dock_channel_probe_nexus_controller_cleanup_client
+ _dock_channel_probe_nexus_controller_client_acquire_nexus_pin_service
+ _dock_channel_probe_nexus_controller_client_release_nexus_pin_service
+ _dock_channel_probe_nexus_controller_create
+ _dock_channel_probe_nexus_controller_create_client
+ _dock_channel_probe_nexus_controller_start
+ _dock_channel_probe_nexus_controller_stop
+ _dock_channel_probe_nexus_create_client
+ _dock_channel_probe_nexus_host_port_create
+ _dock_channel_probe_nexus_id
+ _dock_channel_probe_nexus_objc_cleanup
+ _dock_channel_probe_nexus_objc_cleanup_client
+ _dock_channel_probe_nexus_objc_create_client
+ _dock_channel_probe_nexus_objc_functions
+ _dock_channel_probe_nexus_objc_id
+ _dock_channel_probe_nexus_probe_device_create
+ _dock_channel_probe_nexus_usb_hub_create
+ _dock_channel_serial_interface_client_base_name
+ _dock_channel_serial_interface_client_read_tx
+ _dock_channel_serial_interface_client_suffix
+ _dock_channel_serial_interface_client_tx_data_available
+ _dock_channel_serial_interface_controller_iouserdockchannelserial_services_discovered
+ _dock_channel_serial_interface_iouserdockchannelserial_base_name
+ _dock_channel_serial_interface_iouserdockchannelserial_read_tx
+ _dock_channel_serial_interface_iouserdockchannelserial_suffix
+ _dock_channel_serial_interface_iouserdockchannelserial_tx_data_available
+ _dock_channel_system_service_class
+ _dock_channel_system_service_cleanup
+ _dock_channel_system_service_cleanup_client
+ _dock_channel_system_service_controller_cleanup
+ _dock_channel_system_service_controller_find_children
+ _dock_channel_system_service_controller_find_parent
+ _dock_channel_system_service_controller_find_service
+ _dock_channel_system_service_controller_ioregistry_cleanup
+ _dock_channel_system_service_controller_ioregistry_create
+ _dock_channel_system_service_controller_ioregistry_create_service
+ _dock_channel_system_service_controller_ioregistry_find_children
+ _dock_channel_system_service_controller_ioregistry_find_parent
+ _dock_channel_system_service_controller_ioregistry_find_service
+ _dock_channel_system_service_controller_ioregistry_functions
+ _dock_channel_system_service_create_client
+ _dock_channel_system_service_id
+ _dock_channel_system_service_ioservice_class
+ _dock_channel_system_service_ioservice_cleanup
+ _dock_channel_system_service_ioservice_cleanup_client
+ _dock_channel_system_service_ioservice_create_client
+ _dock_channel_system_service_ioservice_functions
+ _dock_channel_system_service_ioservice_id
+ _dock_channel_system_service_usb_device_class
+ _dock_channel_system_service_usb_device_iousbhost_class
+ _dock_channel_system_service_usb_device_iousbhost_cleanup
+ _dock_channel_system_service_usb_device_iousbhost_create
+ _dock_channel_system_service_usb_device_iousbhost_functions
+ _dock_channel_system_service_usb_device_iousbhost_location
+ _dock_channel_system_service_usb_device_iousbhost_pid
+ _dock_channel_system_service_usb_device_iousbhost_platform_capability
+ _dock_channel_system_service_usb_device_iousbhost_port_type
+ _dock_channel_system_service_usb_device_iousbhost_product_name
+ _dock_channel_system_service_usb_device_iousbhost_serial_number
+ _dock_channel_system_service_usb_device_iousbhost_vid
+ _dock_channel_system_service_usb_device_location
+ _dock_channel_system_service_usb_device_pid
+ _dock_channel_system_service_usb_device_platform_capability
+ _dock_channel_system_service_usb_device_port_type
+ _dock_channel_system_service_usb_device_product_name
+ _dock_channel_system_service_usb_device_serial_number
+ _dock_channel_system_service_usb_device_service_interest_callback
+ _dock_channel_system_service_usb_device_vid
+ _dock_channel_system_service_usb_host_port_iousbhost_cleanup
+ _dock_channel_system_service_usb_host_port_iousbhost_create
+ _dock_channel_system_service_usb_host_port_iousbhost_functions
+ _dock_channel_system_service_usb_host_port_iousbhost_location
+ _dock_channel_system_service_usb_host_port_location
+ _dock_channel_system_service_usb_host_port_service_interest_callback
+ _dock_channel_system_service_usb_hub_port_iousbhost_cleanup
+ _dock_channel_system_service_usb_hub_port_iousbhost_create
+ _dock_channel_system_service_usb_hub_port_iousbhost_functions
+ _dock_channel_system_service_usb_hub_port_iousbhost_location
+ _dock_channel_system_service_usb_hub_port_iousbhost_port_number
+ _dock_channel_system_service_usb_hub_port_location
+ _dock_channel_system_service_usb_hub_port_number
+ _dock_channel_system_service_usb_hub_port_service_interest_callback
+ _kis_interface_client_clear_watchdog_status
+ _kis_interface_client_get_ide_format_version
+ _kis_interface_client_get_target_id
+ _kis_interface_client_read_registers
+ _kis_interface_client_transport_service
+ _kis_interface_client_write_registers
+ _kis_interface_debug_usb_clear_watchdog_status
+ _kis_interface_debug_usb_get_ide_format_version
+ _kis_interface_debug_usb_get_target_id
+ _kis_interface_debug_usb_transport_service
+ _kis_interface_kis_read_registers
+ _kis_interface_kis_write_registers
+ _memset
+ _objc_msgSend$acquireNexus:pinService:
+ _objc_msgSend$acquireNexus:pinService:client:
+ _objc_msgSend$acquireProbeInterfaceWithID:
+ _objc_msgSend$acquireProbeInterfaceWithID:client:
+ _objc_msgSend$acquireSerialInterface:
+ _objc_msgSend$acquireSerialInterfaceWithID:client:
+ _objc_msgSend$acquiredNexusAndPinService
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addProbe:probeType:probeID:pinService:pinServiceID:
+ _objc_msgSend$addProbe:probeType:probeID:pinService:pinServiceID:client:
+ _objc_msgSend$addSerialInterfaceWithID:
+ _objc_msgSend$applyEnablePPMDockChannelWorkaround:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$baseName
+ _objc_msgSend$cleanupAllSerialInterfaces
+ _objc_msgSend$cleanupAllSerialInterfacesForClient:
+ _objc_msgSend$cleanupSerialInterface:
+ _objc_msgSend$cleanupSerialInterface:client:
+ _objc_msgSend$cleanupSerialInterfaceWithSuffix:
+ _objc_msgSend$clearWatchdogStatus:
+ _objc_msgSend$client
+ _objc_msgSend$clientDescription
+ _objc_msgSend$configBaseAddress
+ _objc_msgSend$configurePushForDockChannel:
+ _objc_msgSend$connect_event_callback
+ _objc_msgSend$copyNexusStateAndPinServiceForService:nexusState:pinService:
+ _objc_msgSend$createClientWithDescription:terminationCallback:terminationContext:
+ _objc_msgSend$createClientWithSystemService:description:
+ _objc_msgSend$createClientWithSystemServiceID:description:
+ _objc_msgSend$createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:
+ _objc_msgSend$createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:client:
+ _objc_msgSend$createSerialInterface:suffix:rxQueueLogSize:txQueueLogSize:
+ _objc_msgSend$createSerialInterface:suffix:rxQueueLogSize:txQueueLogSize:client:
+ _objc_msgSend$createSerialInterfaceWithSuffix:rxQueueLogSize:txQueueLogSize:permanent:
+ _objc_msgSend$createSystemServiceFromIOService:
+ _objc_msgSend$createSystemServiceFromServiceID:
+ _objc_msgSend$createUSBDeviceClientWithDescription:terminationCallback:terminationContext:
+ _objc_msgSend$createUSBHostPortClientWithDescription:terminationCallback:terminationContext:
+ _objc_msgSend$createUSBHubPortClientWithDescription:terminationCallback:terminationContext:
+ _objc_msgSend$createdSerialInterfaces
+ _objc_msgSend$deviceClass
+ _objc_msgSend$discoveryIterator
+ _objc_msgSend$discoveryIteratorPointer
+ _objc_msgSend$enablePPM:
+ _objc_msgSend$findChildrenForService:children:count:
+ _objc_msgSend$findParentForService:parent:
+ _objc_msgSend$getBaseName:length:
+ _objc_msgSend$getClass:
+ _objc_msgSend$getData:outBuffer:
+ _objc_msgSend$getIDEFormatVersion:
+ _objc_msgSend$getIOServiceFromSystemService:
+ _objc_msgSend$getLocation:client:
+ _objc_msgSend$getPID:
+ _objc_msgSend$getPlatformCapability:size:uuid:
+ _objc_msgSend$getPlatformMinimumPPWInterval:
+ _objc_msgSend$getPortNumber:
+ _objc_msgSend$getPortType:
+ _objc_msgSend$getProductName:length:
+ _objc_msgSend$getSerialNumber:length:
+ _objc_msgSend$getServiceClass:
+ _objc_msgSend$getServiceID:
+ _objc_msgSend$getSuffix:length:
+ _objc_msgSend$getTargetID:
+ _objc_msgSend$getTransportService
+ _objc_msgSend$getVID:
+ _objc_msgSend$handleConnectEventOnChannel:
+ _objc_msgSend$handleHangUpEventOnChannel:
+ _objc_msgSend$handleHighWatermark
+ _objc_msgSend$handleInterestNotificationForService:messageType:messageArgument:
+ _objc_msgSend$handleLowWatermark
+ _objc_msgSend$handlePAR:dockChannelID:words:
+ _objc_msgSend$handlePinServiceRemoval:
+ _objc_msgSend$handleProbeInterfaceAdded:
+ _objc_msgSend$handleProbeInterfaceRemoved:
+ _objc_msgSend$handleReadDataCallback:revents:t_lock:
+ _objc_msgSend$handleSerialInterfaceAdded:suffix:
+ _objc_msgSend$handleSerialInterfaceRemoved:suffix:
+ _objc_msgSend$handleServiceRemoved:
+ _objc_msgSend$handleWatermarkEventOnChannel:highWatermark:
+ _objc_msgSend$hang_up_event_callback
+ _objc_msgSend$initWithBufferSize:
+ _objc_msgSend$initWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$initWithController:service:description:
+ _objc_msgSend$initWithInterface:interfaceID:pinService:
+ _objc_msgSend$initWithKISInterfaceID:kisManager:nexusController:queue:
+ _objc_msgSend$initWithKISManager:nexusController:
+ _objc_msgSend$initWithNexus:nexusID:intermediate:
+ _objc_msgSend$initWithNexus:pinServiceID:description:
+ _objc_msgSend$initWithNexusID:nexusLocation:queue:
+ _objc_msgSend$initWithOwner:interfaceID:nexusClient:
+ _objc_msgSend$initWithOwner:probeType:probeID:probeInterface:service:nexusController:
+ _objc_msgSend$initWithOwner:serialInterfaceID:baseName:channelIndex:probeClient:
+ _objc_msgSend$initWithProbeID:baseName:serialManager:serialController:queue:
+ _objc_msgSend$initWithService:description:terminationCallback:terminationContext:
+ _objc_msgSend$initWithService:serviceID:description:terminationCallback:terminationContext:queue:
+ _objc_msgSend$initWithService:systemServiceController:
+ _objc_msgSend$initWithService:transferOwnership:
+ _objc_msgSend$initWithSystemServiceController:
+ _objc_msgSend$initWithSystemServiceController:nexusController:serialManager:serialController:deviceQueue:
+ _objc_msgSend$initWithSystemServiceController:queue:
+ _objc_msgSend$initWithVendorID:productID:serialPrefix:
+ _objc_msgSend$intermediate
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isIntermediateHubNexusDevice:
+ _objc_msgSend$isProbeDeviceNexusDevice:
+ _objc_msgSend$isUSBHubDevice:
+ _objc_msgSend$isWatchdogAvailable
+ _objc_msgSend$kisInterfaceClient
+ _objc_msgSend$listAvailableInterfaces:suffixes:count:
+ _objc_msgSend$listAvailableInterfaces:suffixes:count:forClient:
+ _objc_msgSend$listAvailableProbeInterfaces:count:
+ _objc_msgSend$listAvailableProbeInterfaces:count:client:
+ _objc_msgSend$matchClientsToProbes
+ _objc_msgSend$matchingArray
+ _objc_msgSend$matchingDictionary
+ _objc_msgSend$nameForService:
+ _objc_msgSend$nexus
+ _objc_msgSend$nexusClient
+ _objc_msgSend$nexusController
+ _objc_msgSend$nexusForNexusService:intermediate:
+ _objc_msgSend$nexusID
+ _objc_msgSend$nexusServiceForService:
+ _objc_msgSend$nexusState
+ _objc_msgSend$nexusStateForNexusService:
+ _objc_msgSend$pinService
+ _objc_msgSend$pinServiceID
+ _objc_msgSend$platformRequiresPolling
+ _objc_msgSend$portServiceForService:
+ _objc_msgSend$ppmEnabled
+ _objc_msgSend$probeBaseName
+ _objc_msgSend$probeIDArrayByPinServiceID
+ _objc_msgSend$probeIDsForClient:
+ _objc_msgSend$probeInterface
+ _objc_msgSend$probeInterfaceClient
+ _objc_msgSend$probeSerialState
+ _objc_msgSend$probeStateByPinServiceID
+ _objc_msgSend$processHardwareV1Part1:data:length:
+ _objc_msgSend$processHardwareV1Part2:data:length:
+ _objc_msgSend$putData:
+ _objc_msgSend$readMemoryFromAddress:length:sequenceID:endpointAddress:portal:payloadWriteFlags:
+ _objc_msgSend$readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:payloadWriteFlags:
+ _objc_msgSend$readRSTAT:dockChannelID:
+ _objc_msgSend$readRegistersFromIndex:count:sequenceID:endpointAddress:portal:
+ _objc_msgSend$readRemainingBytes:readRemainingBytesCount:channelDockDataBase:dockChannelID:
+ _objc_msgSend$readTx:maxLength:
+ _objc_msgSend$readTxDataAvailable:
+ _objc_msgSend$readWSTAT:dockChannelID:
+ _objc_msgSend$readWords:channelDockDataBase:dockChannelID:
+ _objc_msgSend$releaseNexusAndPinService
+ _objc_msgSend$releaseNexusAndPinServiceForClient:
+ _objc_msgSend$releaseProbeInterfaceWithID:
+ _objc_msgSend$releaseProbeInterfaceWithID:client:
+ _objc_msgSend$releaseSerialInterface:
+ _objc_msgSend$releaseSerialInterfaceWithID:client:
+ _objc_msgSend$removeProbeWithID:
+ _objc_msgSend$removeProbeWithID:client:
+ _objc_msgSend$removeSerialInterfaceWithID:
+ _objc_msgSend$replaceBytesInRange:withBytes:length:
+ _objc_msgSend$rxOverflow
+ _objc_msgSend$scheduleWorkloop
+ _objc_msgSend$sendCommandAsync:length:endpoint:timeout:
+ _objc_msgSend$serialPrefix
+ _objc_msgSend$service
+ _objc_msgSend$serviceClass
+ _objc_msgSend$serviceID
+ _objc_msgSend$setAcquiredNexusAndPinService:
+ _objc_msgSend$setDiscoveryIterator:
+ _objc_msgSend$setHighWatermarkStatus:
+ _objc_msgSend$setNexusID:
+ _objc_msgSend$setNexusLocation:
+ _objc_msgSend$setNexusState:
+ _objc_msgSend$setPinService:
+ _objc_msgSend$setPortID:
+ _objc_msgSend$setPortLocation:
+ _objc_msgSend$setProbeSerialState:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$setupHardwareV1Part2
+ _objc_msgSend$startListeningForTermination
+ _objc_msgSend$storeReadData:length:client:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$txDataAvailable:
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$vid
+ _objc_msgSend$writeData:channel:
+ _objc_msgSend$writeMemoryFromAddress:length:data:sequenceID:endpointAddress:portal:payloadWriteFlags:
+ _objc_msgSend$writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:payloadWriteFlags:
+ _objc_msgSend$writeRegistersFromIndex:count:registers:sequenceID:endpointAddress:portal:
+ _objc_msgSend$writeRegistersFromIndex:count:registers:sequenceID:endpointAddress:toPortal:
+ _objc_msgSend$writeRemainingBytes:channelDockDataBase:dockChannelID:writeData:writeRemainingBytesCount:
+ _objc_msgSend$writeWords:channelDockDataBase:dockChannelID:writeData:
+ _os_transaction_create
+ initWithService:queue:.usbHostPortClassName
+ initWithService:queue:.usbHubPortClassName
+ initWithStaticIdentification:tableData:length:.locationMap
- -[BufferInfo available]
- -[BufferInfo bufferLength]
- -[BufferInfo empty]
- -[BufferInfo headOffset]
- -[BufferInfo mod:]
- -[BufferInfo setBufferLength:]
- -[BufferInfo setHeadOffset:]
- -[BufferInfo setHeadOffsetFromDoorbell:]
- -[BufferInfo setTailOffset:]
- -[BufferInfo setTailOffsetFromDoorbell:]
- -[BufferInfo tailOffset]
- -[BufferInfo used]
- -[DebugUSBDeviceInterfaceIOUSBHost reset].cold.1
- -[DebugUSBDeviceInterfaceIOUSBHost reset].cold.2
- -[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:].cold.1
- -[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:].cold.2
- -[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:].cold.3
- -[DebugUSBInterfaceIOUSBHost addEndpoints].cold.1
- -[DebugUSBInterfaceIOUSBHost clearStallOnEndpoint:].cold.1
- -[DebugUSBInterfaceIOUSBHost initWithService:]
- -[DebugUSBInterfaceIOUSBHost startTransferOnEndpoint:buffer:timeout:callback:context:owner:].cold.1
- -[DebugUSBInterfaceIOUSBHost startWithCompletion:].cold.1
- -[DebugUSBInterfaceIOUSBHost transferOnEndpoint:buffer:bytesTransferred:timeout:].cold.1
- -[DebugUSBInterfaceListenerIOUSBHost init]
- -[DockChannelInterfaceKISPAM handleSerialInterfaceAdded:base:suffix:]
- -[DockChannelInterfaceKISPAM handleSerialInterfaceRemoved:base:suffix:]
- -[DockChannelInterfaceKISPAM initWithKISInterfaceID:kisManager:serialController:queue:]
- -[DockChannelInterfaceKISPAM serialControllerClient]
- -[DockChannelInterfaceKISPAM serialControllerCreatedInterfaces]
- -[DockChannelInterfaceKISPAM serialController]
- -[DockChannelInterfaceKISPAM serialInterfaceBaseNameCString]
- -[DockChannelInterfaceKISPAM serialInterfaceBaseName]
- -[DockChannelInterfaceKISPAM serialInterfaces]
- -[DockChannelInterfaceKISPAM setSerialControllerClient:]
- -[DockChannelInterfaceKISPAM setSerialControllerCreatedInterfaces:]
- -[DockChannelInterfaceKISPAM setSerialInterfaceBaseName:]
- -[DockChannelInterfaceKISPAM setSerialInterfaceBaseNameCString:]
- -[DockChannelInterfaceKISPAM setSerialInterfaces:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial acquireInterfaceWithID:client:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial addInterfaceWithID:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:client:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial initWithSerialManager:queue:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial interfacesLock]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial listAvailableInterfacesForBase:interfaceIDs:suffixes:count:client:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial releaseInterfaceWithID:client:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial removeInterfaceWithID:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial serialInterfaceIDsByBase]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial serialInterfaceNameComponentsByName]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial serialInterfaceStatesByID]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial serialManagerClient]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial serialManager]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial setSerialManagerClient:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial startListeningForClient:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial start].cold.1
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial start].cold.2
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerial stopListeningForClient:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient acquireInterfaceWithID:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient listAvailableInterfacesForBase:interfaceIDs:suffixes:count:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient registerCallbacksForBase:callbacks:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient releaseInterfaceWithID:]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient startListening]
- -[DockChannelSerialInterfaceControllerIOUserDockChannelSerialClient stopListening]
- -[DockChannelSerialInterfaceIOUserDockChannelSerial asyncPoll:rxCommitted:txCommitted:].cold.1
- -[DockChannelSerialInterfaceIOUserDockChannelSerial getName:length:]
- -[DockChannelSerialInterfaceIOUserDockChannelSerial mapBuffers].cold.1
- -[DockChannelSerialInterfaceIOUserDockChannelSerial mapBuffers].cold.2
- -[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:].cold.1
- -[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:].cold.2
- -[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:].cold.3
- -[DockChannelSerialInterfaceIOUserDockChannelSerial storeReadData:length:]
- -[DockChannelSerialInterfaceIOUserDockChannelSerialClient getName:length:]
- -[DockChannelSerialInterfaceListenerKIS initWithKISManager:serialController:]
- -[DockChannelSerialInterfaceListenerKIS serialController]
- -[DockChannelSerialInterfaceWrapper controllerClient]
- -[DockChannelSerialInterfaceWrapper initWithOwner:serialInterfaceID:baseName:channelIndex:controllerClient:]
- -[ExternalInterfaceKIS transfer_data:ofSize:withStruct:ofSize:withOutputStruct:ofSize:].cold.1
- -[ExternalInterfaceKIS transfer_data:ofSize:withStruct:ofSize:withOutputStruct:ofSize:].cold.2
- -[ExternalInterfaceKIS transfer_data:ofSize:withStruct:ofSize:withOutputStruct:ofSize:].cold.3
- -[KISInterfaceDebugUSB asyncPARWithAddress:length:sequenceID:endpoint:portal:]
- -[KISInterfaceDebugUSB asyncPAWWithAddress:length:data:sequenceID:endpoint:portal:]
- -[KISInterfaceDebugUSB asyncPCRWithIndex:numberOfDoorbells:sequenceID:endpoint:portal:]
- -[KISInterfaceDebugUSB asyncPCWWithIndex:numberOfDoorbells:doorbells:portal:sequenceID:endpoint:]
- -[KISInterfaceDebugUSB readDoorbellsFromIndex:numberOfDoorbells:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSB readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSB sendCommandAsync:length:onEndpoint:timeout:]
- -[KISInterfaceDebugUSB writeDoorbellsFromIndex:numberOfDoorbells:doorbells:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSB writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSBClient readDoorbellsFromIndex:numberOfDoorbells:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSBClient readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSBClient writeDoorbellsFromIndex:numberOfDoorbells:doorbells:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSBClient writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:]
- -[KISInterfaceDebugUSBInputPipe armReads].cold.1
- -[RSMChannelClass writeNotification:].cold.1
- -[RSMChannelSystemInterfaceAppleRSMChannel initWithService:andManager:].cold.1
- -[RSMInterfaceKIS dcmEndpoint]
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.1
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.10
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.11
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.12
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.13
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.14
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.15
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.2
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.3
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.4
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.5
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.6
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.7
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.8
- -[RSMInterfaceKIS initWithKISInterfaceID:kisManager:queue:].cold.9
- -[TADFUTransportClient transportClientPointer]
- GCC_except_table11
- GCC_except_table13
- GCC_except_table3
- GCC_except_table30
- GCC_except_table38
- GCC_except_table6
- GCC_except_table7
- GCC_except_table9
- OBJC_IVAR_$_BufferInfo._bufferLength
- OBJC_IVAR_$_BufferInfo._headOffset
- OBJC_IVAR_$_BufferInfo._tailOffset
- OBJC_IVAR_$_DockChannelInterfaceKISPAM._serialController
- OBJC_IVAR_$_DockChannelInterfaceKISPAM._serialControllerClient
- OBJC_IVAR_$_DockChannelInterfaceKISPAM._serialControllerCreatedInterfaces
- OBJC_IVAR_$_DockChannelInterfaceKISPAM._serialInterfaceBaseName
- OBJC_IVAR_$_DockChannelInterfaceKISPAM._serialInterfaceBaseNameCString
- OBJC_IVAR_$_DockChannelInterfaceKISPAM._serialInterfaces
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._interfacesLock
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._serialInterfaceIDsByBase
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._serialInterfaceNameComponentsByName
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._serialInterfaceStatesByID
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._serialManager
- OBJC_IVAR_$_DockChannelSerialInterfaceControllerIOUserDockChannelSerial._serialManagerClient
- OBJC_IVAR_$_DockChannelSerialInterfaceListenerKIS._serialController
- OBJC_IVAR_$_DockChannelSerialInterfaceWrapper._controllerClient
- OBJC_IVAR_$_RSMInterfaceKIS._dcmEndpoint
- OBJC_IVAR_$_TADFUTransportClient._transportClientPointer
- _OBJC_CLASS_$_BufferInfo
- _OBJC_METACLASS_$_BufferInfo
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- __102-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial cleanupInterfaceWithBase:suffix:client:]_block_invoke.cold.1
- __131-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:client:]_block_invoke.cold.1
- __47-[DeviceInterfaceClientXPCServer device_added:]_block_invoke.cold.1
- __48-[DeviceInterfaceClientXPCServer pingAllClients]_block_invoke.cold.1
- __49-[DeviceInterfaceClientXPCServer device_removed:]_block_invoke.cold.1
- __50-[DeviceInterfaceClientXPCServer pingActiveClient]_block_invoke.cold.1
- __56-[DebugUSBDeviceInterfaceIOUSBHost startWithCompletion:]_block_invoke.1
- __69-[DeviceInterfaceClientXPCServer listener:shouldAcceptNewConnection:]_block_invoke.73.cold.1
- __73-[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:]_block_invoke.1
- __73-[DockChannelSerialInterfaceIOUserDockChannelSerial startWithCompletion:]_block_invoke.4
- __92-[DebugUSBInterfaceIOUSBHost startTransferOnEndpoint:buffer:timeout:callback:context:owner:]_block_invoke.cold.1
- __93-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial cleanupAllInterfacesForClient:]_block_invoke.cold.1
- __OBJC_$_INSTANCE_METHODS_BufferInfo
- __OBJC_$_INSTANCE_VARIABLES_BufferInfo
- __OBJC_$_PROP_LIST_BufferInfo
- __OBJC_CLASS_RO_$_BufferInfo
- __OBJC_METACLASS_RO_$_BufferInfo
- ___131-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:client:]_block_invoke
- ___50-[DockChannelInterfaceKISPAM startWithCompletion:]_block_invoke
- ___69-[DockChannelInterfaceKISPAM handleSerialInterfaceAdded:base:suffix:]_block_invoke
- ___71-[DockChannelInterfaceKISPAM handleSerialInterfaceRemoved:base:suffix:]_block_invoke
- ___82-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial addInterfaceWithID:]_block_invoke
- ___85-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial removeInterfaceWithID:]_block_invoke
- ___86-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial stopListeningForClient:]_block_invoke
- ___87-[DockChannelInterfaceKISPAM initWithKISInterfaceID:kisManager:serialController:queue:]_block_invoke
- ___87-[DockChannelSerialInterfaceControllerIOUserDockChannelSerial startListeningForClient:]_block_invoke
- ___atomic_load_4
- ___block_descriptor_64_e8_32s40s48w_e5_v8?0l
- ___block_descriptor_90_e8_32s40r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48w
- ___destroy_helper_block_e8_32s40s48w
- __block_literal_global.6
- _dock_channel_interface_kis_pam_handle_serial_interface_added
- _dock_channel_interface_kis_pam_handle_serial_interface_removed
- _dock_channel_serial_interface_client_name
- _dock_channel_serial_interface_controller_client_acquire_interface
- _dock_channel_serial_interface_controller_client_list_available_interfaces
- _dock_channel_serial_interface_controller_client_register_callbacks
- _dock_channel_serial_interface_controller_client_release_interface
- _dock_channel_serial_interface_controller_client_start_listening
- _dock_channel_serial_interface_controller_client_stop_listening
- _dock_channel_serial_interface_controller_iouserdockchannelserial_acquire_interface
- _dock_channel_serial_interface_controller_iouserdockchannelserial_interface_added
- _dock_channel_serial_interface_controller_iouserdockchannelserial_interface_removed
- _dock_channel_serial_interface_controller_iouserdockchannelserial_list_available_interfaces
- _dock_channel_serial_interface_controller_iouserdockchannelserial_register_callbacks
- _dock_channel_serial_interface_controller_iouserdockchannelserial_release_interface
- _dock_channel_serial_interface_controller_iouserdockchannelserial_start_listening
- _dock_channel_serial_interface_controller_iouserdockchannelserial_stop_listening
- _dock_channel_serial_interface_iouserdockchannelserial_name
- _dock_channel_serial_interface_iouserdockchannelserial_read_data_available_space
- _kis_interface_client_read_doorbells
- _kis_interface_client_write_doorbells
- _kis_interface_kis_read_doorbells
- _kis_interface_kis_write_doorbells
- _objc_msgSend$acquireInterfaceWithID:client:
- _objc_msgSend$addInterfaceWithID:
- _objc_msgSend$asyncPARWithAddress:length:sequenceID:endpoint:portal:
- _objc_msgSend$asyncPAWWithAddress:length:data:sequenceID:endpoint:portal:
- _objc_msgSend$asyncPCRWithIndex:numberOfDoorbells:sequenceID:endpoint:portal:
- _objc_msgSend$asyncPCWWithIndex:numberOfDoorbells:doorbells:portal:sequenceID:endpoint:
- _objc_msgSend$base
- _objc_msgSend$callbacksForBase
- _objc_msgSend$createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:
- _objc_msgSend$createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:client:
- _objc_msgSend$getName:length:
- _objc_msgSend$handleSerialInterfaceAdded:base:suffix:
- _objc_msgSend$handleSerialInterfaceRemoved:base:suffix:
- _objc_msgSend$initWithKISInterfaceID:kisManager:serialController:queue:
- _objc_msgSend$initWithKISManager:serialController:
- _objc_msgSend$initWithOwner:serialInterfaceID:baseName:channelIndex:controllerClient:
- _objc_msgSend$initWithSerialManager:queue:
- _objc_msgSend$isEqualTo:
- _objc_msgSend$listAvailableInterfacesForBase:interfaceIDs:suffixes:count:
- _objc_msgSend$listAvailableInterfacesForBase:interfaceIDs:suffixes:count:client:
- _objc_msgSend$name
- _objc_msgSend$readDoorbellsFromIndex:numberOfDoorbells:sequenceID:endpointAddress:toPortal:
- _objc_msgSend$readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:
- _objc_msgSend$registerCallbacksForBase:callbacks:
- _objc_msgSend$releaseInterfaceWithID:client:
- _objc_msgSend$removeInterfaceWithID:
- _objc_msgSend$serialController
- _objc_msgSend$serialControllerClient
- _objc_msgSend$serialInterfaceBaseName
- _objc_msgSend$serialInterfaceBaseNameCString
- _objc_msgSend$setWithCapacity:
- _objc_msgSend$transportClientPointer
- _objc_msgSend$txBuf
- _objc_msgSend$writeDoorbellsFromIndex:numberOfDoorbells:doorbells:sequenceID:endpointAddress:toPortal:
- _objc_msgSend$writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:
CStrings:
+ "!1"
+ "%s Enable PPM failed"
+ "%s PAM register for callbacks for endpoint %d failed"
+ "%s PPM portal endpoint lookup failed"
+ "%s PPM register for callbacks for endpoint %d failed"
+ "%s Setting PAM_AF_TIMEOUT_CYCLES failed"
+ "%s Setting PPM_AF_TIMEOUT_CYCLES failed"
+ "%s bytesWritten %u != dataRead.length %u"
+ "%s clearWatchdogStatus failed"
+ "%s connection from pid=%d"
+ "%s ideFormatVersion %u"
+ "%s watchdogAvailable %d"
+ "&"
+ "-%s"
+ "-[DockChannelInterfaceKISPAM enablePPM:]"
+ "-[DockChannelInterfaceKISPAM initWithKISInterfaceID:kisManager:nexusController:queue:]"
+ "-[DockChannelInterfaceKISPAM isWatchdogAvailable]"
+ "@\"<DockChannelInterfaceProbeSerialStateDelegate>\""
+ "@\"<DockChannelProbeListenerProbeStateDelegate>\""
+ "@\"DockChannelInterfaceProbeSerialState\""
+ "@\"DockChannelProbeInterface\""
+ "@\"DockChannelProbeNexus\""
+ "@\"DockChannelProbeNexusController\""
+ "@\"DockChannelProbeNexusState\""
+ "@\"DockChannelSerialInterfaceBuffer\""
+ "@\"DockChannelSystemServiceClientWrapper\""
+ "@\"DockChannelSystemServiceWrapper\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"RSMHostChannelBuffer\""
+ "@24@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16"
+ "@28@0:8I16r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}20"
+ "@28@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16B24"
+ "@32@0:8S16S20@24"
+ "@32@0:8r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16r^{dock_channel_probe_nexus_controller_t=^v}24"
+ "@32@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@24"
+ "@36@0:8r^{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}}16Q24B32"
+ "@40@0:8@16@24r*32"
+ "@40@0:8@16Q24r*32"
+ "@40@0:8@16Q24r^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}32"
+ "@40@0:8Q16Q24@32"
+ "@40@0:8r*16^?24r^v32"
+ "@48@0:8@16r*24^?32r^v40"
+ "@48@0:8Q16r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}24r^{dock_channel_probe_nexus_controller_t=^v}32@40"
+ "@52@0:8@16Q24@32C40r^{dock_channel_probe_interface_client_t=^v}44"
+ "@56@0:8Q16r*24r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}32r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}40@48"
+ "@56@0:8r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16r^{dock_channel_probe_nexus_controller_t=^v}24r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}32r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}40@48"
+ "@60@0:8@16i24Q28r^{device_interface_t=^v^{device_interface_functions_t}}36@44r^{dock_channel_probe_nexus_controller_t=^v}52"
+ "@60@0:8I16Q20r*28^?36r^v44@52"
+ "AppleUSBHostPort"
+ "AppleUSBHubPort"
+ "B24@0:8*16"
+ "B24@0:8^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}16"
+ "B24@0:8^{dock_channel_probe_nexus_controller_client_t=^v}16"
+ "B24@0:8^{dock_channel_system_service_client_t=}16"
+ "B24@0:8r*16"
+ "B24@0:8r^{dock_channel_probe_interface_client_callbacks_t=^?^v^?^v}16"
+ "B24@0:8r^{dock_channel_probe_nexus_client_callbacks_t=^?^v^?^v}16"
+ "B24@0:8r^{dock_channel_serial_interface_client_callbacks_t=^?^?^?^?^v}16"
+ "B28@0:8Q16C24"
+ "B32@0:8I16Q20C28"
+ "B32@0:8^I16*24"
+ "B32@0:8^Q16@24"
+ "B32@0:8^v16^I24"
+ "B32@0:8r*16@24"
+ "B32@0:8r^^{dock_channel_probe_nexus_t}16r^^{dock_channel_system_service_t}24"
+ "B32@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16r^^{dock_channel_system_service_t}24"
+ "B36@0:8*16I24@28"
+ "B36@0:8@16C24C28B32"
+ "B36@0:8B16r*20C28C32"
+ "B36@0:8I16I20Q24C32"
+ "B40@0:8*16^Q24[16C]32"
+ "B40@0:8@16^@24^@32"
+ "B40@0:8I16Q20C28@32"
+ "B40@0:8^Q16r^*24^Q32"
+ "B40@0:8r^^{dock_channel_probe_nexus_t}16r^^{dock_channel_system_service_t}24@32"
+ "B40@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16r^^{dock_channel_system_service_t}24^Q32"
+ "B44@0:8B16r*20C28C32@36"
+ "B44@0:8I16Q20C28@32I40"
+ "B44@0:8Q16I24S28C32C36I40"
+ "B48@0:8^Q16r^*24^Q32@40"
+ "B52@0:8Q16I24r^v28S36C40C44I48"
+ "B52@0:8r^{device_interface_t=^v^{device_interface_functions_t}}16i24Q28r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}36Q44"
+ "B60@0:8r^{device_interface_t=^v^{device_interface_functions_t}}16i24Q28r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}36Q44@52"
+ "B72@0:8r*16r*24C32C36Q40Q48Q56Q64"
+ "B80@0:8r*16r*24C32C36Q40Q48Q56Q64@72"
+ "Dock channel serial controller version: %d found"
+ "Dock channel serial controller with no version found"
+ "DockChannelInterfaceProbeSerialState"
+ "DockChannelInterfaceProbeSerialStateDelegate"
+ "DockChannelInterfaceProbeState"
+ "DockChannelProbeDeviceListenerIOUSBHost"
+ "DockChannelProbeDeviceListenerProbeState"
+ "DockChannelProbeDeviceMatching"
+ "DockChannelProbeInterface"
+ "DockChannelProbeInterfaceClient"
+ "DockChannelProbeInterfaceController"
+ "DockChannelProbeKISListenerIOUSBHost"
+ "DockChannelProbeListenerProbeState"
+ "DockChannelProbeListenerProbeStateDelegate"
+ "DockChannelProbeNexus"
+ "DockChannelProbeNexusClient"
+ "DockChannelProbeNexusController"
+ "DockChannelProbeNexusControllerClient"
+ "DockChannelProbeNexusHostPort"
+ "DockChannelProbeNexusProbeDevice"
+ "DockChannelProbeNexusProbeState"
+ "DockChannelProbeNexusState"
+ "DockChannelProbeNexusUSBHub"
+ "DockChannelSerialInterfaceBuffer"
+ "DockChannelSystemServiceClientWrapper"
+ "DockChannelSystemServiceControllerIORegistry"
+ "DockChannelSystemServiceIOService"
+ "DockChannelSystemServiceUSBDeviceClientWrapper"
+ "DockChannelSystemServiceUSBDeviceIOUSBHost"
+ "DockChannelSystemServiceUSBHostPortClientWrapper"
+ "DockChannelSystemServiceUSBHostPortIOUSBHost"
+ "DockChannelSystemServiceUSBHubPortClientWrapper"
+ "DockChannelSystemServiceUSBHubPortIOUSBHost"
+ "DockChannelSystemServiceWrapper"
+ "Error encountered while cleaning up interface: controller not available"
+ "Error encountered while creating interface: controller not available"
+ "Error in async poll of event: %llu rx: %u tx: %u error: 0x%x (%s)"
+ "I24@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16"
+ "I28@0:8@16C24"
+ "IOGeneralInterest"
+ "IOTTYSuffix"
+ "IOUSBHostDevice"
+ "IOUserDockChannelSerialMajorVersion"
+ "Nexus controller client %@ acquired nexus: 0x%llx pinService: 0x%llx."
+ "Nexus controller client %@ failed to acquire nexus and pin service."
+ "Nexus controller client %@ releasing nexus/pin service."
+ "Nexus controller: finished nexus search."
+ "Nexus controller: found intermediate nexus, resuming iteration."
+ "Nexus controller: found nexus service: 0x%llx."
+ "Nexus controller: found port service: 0x%llx."
+ "Nexus controller: starting nexus/pin service search for service: 0x%llx."
+ "PAM[0x%llx] Failed to read RSTAT after configuring push for channel %d."
+ "PAM[0x%llx] Failed to write register (0x%x) to configure push on channel %d."
+ "PAM[0x%llx] Modifying push setting for channel %d from %d->%d"
+ "PAM[0x%llx] channel %d connected"
+ "PAM[0x%llx] channel %d hung up"
+ "PAM[0x%llx] channel %d water mark high:%d"
+ "ProbeNexus[0x%llx] client %@ failed to acquire probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ failed to add probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ failed to be cleaned up."
+ "ProbeNexus[0x%llx] client %@ failed to release probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ failed to remove probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ has failed to start listening."
+ "ProbeNexus[0x%llx] client %@ has failed to stop listening."
+ "ProbeNexus[0x%llx] client %@ has probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ is about to start listening."
+ "ProbeNexus[0x%llx] client %@ is about to stop listening."
+ "ProbeNexus[0x%llx] client %@ is acquiring probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ is adding probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ is being cleaned up."
+ "ProbeNexus[0x%llx] client %@ is listing probe interfaces."
+ "ProbeNexus[0x%llx] client %@ is releasing probe 0x%llx."
+ "ProbeNexus[0x%llx] client %@ is removing probe 0x%llx."
+ "ProbeNexus[0x%llx] creating client for system service ID: 0x%llx description: %s."
+ "Probe[0x%llx] cleaning up client: %@"
+ "Probe[0x%llx] cleaning up."
+ "Probe[0x%llx] client: %@ is acquiring serial interface 0x%llx"
+ "Probe[0x%llx] client: %@ is done listening (success = %d)"
+ "Probe[0x%llx] client: %@ is now listening (success = %d)"
+ "Probe[0x%llx] client: %@ is releasing serial interface 0x%llx"
+ "Probe[0x%llx] client: %@ is requesting a serial interface with name: %@ suffix: %s (permanent = %d)"
+ "Probe[0x%llx] client: %@ is requesting available serial interfaces"
+ "Probe[0x%llx] client: %@ is requesting the cleanup of all serial interfaces"
+ "Probe[0x%llx] client: %@ is requesting the cleanup of serial interface with suffix: %s"
+ "Probe[0x%llx] creating client: %@"
+ "Probe[0x%llx] initialized."
+ "Probe[0x%llx] serial interface added: 0x%llx (success = %d)"
+ "Probe[0x%llx] serial interface removed: 0x%llx (success = %d)"
+ "Probe[0x%llx] starting."
+ "Probe[0x%llx] stopping."
+ "RSMHostChannelBuffer"
+ "Serial[0x%llx] (%@%@) added %d more bytes to overflow. Overflow total: %lu bytes"
+ "Serial[0x%llx] (%@%@) invoking high water mark callback.\n"
+ "Serial[0x%llx] (%@%@) invoking low water mark callback.\n"
+ "Serial[0x%llx] (%@%@) no client, dropping %d bytes"
+ "Serial[0x%llx] (%@%@) received too many bytes (%d), starting to overflow. Overflow total: %lu bytes"
+ "Serial[0x%llx] (%@%@) wrote out %d bytes, remaining overflow: %lu bytes."
+ "Serial[0x%llx] (%@%@) wrote out all overflow data to output."
+ "T@\"<DockChannelInterfaceProbeSerialStateDelegate>\",R,W,N,V_owner"
+ "T@\"<DockChannelProbeListenerProbeStateDelegate>\",R,W,N,V_owner"
+ "T@\"DockChannelInterfaceProbeSerialState\",&,N,V_probeSerialState"
+ "T@\"DockChannelProbeInterface\",R,N,V_interface"
+ "T@\"DockChannelProbeNexus\",R,N,V_nexus"
+ "T@\"DockChannelProbeNexusController\",R,N,V_controller"
+ "T@\"DockChannelProbeNexusState\",&,N,V_nexusState"
+ "T@\"DockChannelSerialInterfaceBuffer\",R,N,V_txIntermediateBuffer"
+ "T@\"DockChannelSystemServiceClientWrapper\",R,N,V_pinServiceClient"
+ "T@\"DockChannelSystemServiceWrapper\",&,N,V_pinService"
+ "T@\"DockChannelSystemServiceWrapper\",R,N,V_pinService"
+ "T@\"DockChannelSystemServiceWrapper\",R,N,V_service"
+ "T@\"DockChannelSystemServiceWrapper\",R,N,V_transportService"
+ "T@\"NSArray\",R,N,V_matchingArray"
+ "T@\"NSMutableData\",R,N,V_circularBuffer"
+ "T@\"NSMutableData\",R,N,V_rxOverflow"
+ "T@\"NSMutableDictionary\",R,N,V_activeNexusStatesByID"
+ "T@\"NSMutableDictionary\",R,N,V_probeIDArrayByPinServiceID"
+ "T@\"NSMutableDictionary\",R,N,V_probeStateByPinServiceID"
+ "T@\"NSMutableDictionary\",R,N,V_probeStatesByProbeID"
+ "T@\"NSMutableDictionary\",R,N,V_serialInterfaces"
+ "T@\"NSMutableSet\",R,N,V_clientsRequiringProbes"
+ "T@\"NSMutableSet\",R,N,V_createdSerialInterfaces"
+ "T@\"NSMutableSet\",R,N,V_permanentSuffixes"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_deviceQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_controllerAvailableSempahore"
+ "T@\"NSObject<OS_os_transaction>\",R,N,V_transaction"
+ "T@\"NSString\",R,N,V_baseName"
+ "T@\"NSString\",R,N,V_probeBaseName"
+ "T@\"NSString\",R,N,V_serialPrefix"
+ "T@\"RSMHostChannelBuffer\",&,N,V_inBufferInfo"
+ "T@\"RSMHostChannelBuffer\",&,N,V_outBufferInfo"
+ "T@,R,W,N,V_owner"
+ "TB,N,V_acquiredNexusAndPinService"
+ "TB,N,V_highWatermarkStatus"
+ "TB,N,V_platformRequiresPolling"
+ "TB,N,V_ppmEnabled"
+ "TB,R,N,V_intermediate"
+ "TB,R,N,V_listening"
+ "TB,R,N,V_probeAddedToNexus"
+ "TB,R,N,V_transferredOwnership"
+ "TC,R,N,V_deviceClass"
+ "TC,R,N,V_portNumber"
+ "TC,R,N,V_portType"
+ "TC,R,N,V_ppmEndpoint"
+ "TC,R,N,V_serviceClass"
+ "TI,N,V_discoveryIterator"
+ "TI,N,V_dockChannelsWithBackPressure"
+ "TI,N,V_dockChannelsWithPush"
+ "TI,N,V_ppmEnabledDockChannels"
+ "TI,N,V_serviceConnection"
+ "TI,N,V_transferResponseFirstWord"
+ "TI,R,N,V_interestNotificationObject"
+ "TI,R,N,V_location"
+ "TQ,N,V_nexusID"
+ "TQ,N,V_nexusLocation"
+ "TQ,N,V_portID"
+ "TQ,N,V_portLocation"
+ "TQ,R,N,V_nexusID"
+ "TQ,R,N,V_nexusLocation"
+ "TQ,R,N,V_pinServiceID"
+ "TQ,R,N,V_probeID"
+ "TQ,R,N,V_probeInterfaceID"
+ "TQ,R,N,V_serviceID"
+ "TS,R,N,V_pid"
+ "TS,R,N,V_vid"
+ "T^?,N,V_connect_event_callback"
+ "T^?,N,V_hang_up_event_callback"
+ "T^?,N,V_water_mark_callback"
+ "T^?,R,N,V_terminationCallback"
+ "T^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}},R,N,V_serialManagerClient"
+ "T^{dock_channel_probe_interface_client_t=^v},R,N,V_probeInterfaceClient"
+ "T^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}},R,N,V_nexusClient"
+ "T^{dock_channel_probe_nexus_controller_client_t=^v},N,V_nexusControllerClient"
+ "T^{dock_channel_probe_nexus_controller_client_t=^v},R,N,V_nexusControllerClient"
+ "T^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}},R,N,V_serialControllerClient"
+ "T^{dock_channel_system_service_client_t=},R,N,V_client"
+ "T^{dock_channel_system_service_usb_device_client_t=^v^{dock_channel_system_service_usb_device_client_functions_t}},R,N,V_usbDeviceClient"
+ "T^{dock_channel_system_service_usb_host_port_client_t=^v^{dock_channel_system_service_usb_host_port_client_functions_t}},R,N,V_usbHostPortClient"
+ "T^{dock_channel_system_service_usb_hub_port_client_t=^v^{dock_channel_system_service_usb_hub_port_client_functions_t}},R,N,V_usbHubPortClient"
+ "Ti,N,V_hardwareInitStep"
+ "Ti,N,V_hardwareInitVersion"
+ "Ti,R,N,V_probeType"
+ "Ti,R,N,V_serviceClass"
+ "Timed out waiting for dock channel serial controller!"
+ "Tr^v,R,N,V_terminationContext"
+ "Tr^{device_interface_t=^v^{device_interface_functions_t}},R,N,V_probeInterface"
+ "Tr^{dock_channel_probe_interface_client_t=^v},R,N,V_probeClient"
+ "Tr^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}},R,N,V_nexusClient"
+ "Tr^{dock_channel_probe_nexus_controller_t=^v},R,N,V_nexusController"
+ "Tr^{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}},R,N,V_nexus"
+ "Tr^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}},R,N,V_systemServiceController"
+ "Tr^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}},R,N,V_service"
+ "T{dock_channel_probe_interface_client_t=^v},R,N,V_externalInterface"
+ "T{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}},R,N,V_externalInterface"
+ "T{dock_channel_probe_nexus_controller_client_t=^v},R,N,V_externalInterface"
+ "T{dock_channel_probe_nexus_controller_t=^v},R,N,V_externalInterface"
+ "T{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}},R,N,V_externalInterface"
+ "T{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}},R,N,V_externalInterface"
+ "T{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}},R,N,V_externalInterface"
+ "T{dock_channel_system_service_usb_device_client_t=^v^{dock_channel_system_service_usb_device_client_functions_t}},R,N,V_externalInterface"
+ "T{dock_channel_system_service_usb_host_port_client_t=^v^{dock_channel_system_service_usb_host_port_client_functions_t}},R,N,V_externalInterface"
+ "T{dock_channel_system_service_usb_hub_port_client_t=^v^{dock_channel_system_service_usb_hub_port_client_functions_t}},R,N,V_externalInterface"
+ "USBPortType"
+ "^{dock_channel_probe_interface_client_t=^v}"
+ "^{dock_channel_probe_interface_client_t=^v}16@0:8"
+ "^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}"
+ "^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}16@0:8"
+ "^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}32@0:8Q16r*24"
+ "^{dock_channel_probe_nexus_controller_client_t=^v}"
+ "^{dock_channel_probe_nexus_controller_client_t=^v}16@0:8"
+ "^{dock_channel_probe_nexus_controller_client_t=^v}32@0:8r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16r*24"
+ "^{dock_channel_probe_nexus_controller_t=^v}16@0:8"
+ "^{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}}16@0:8"
+ "^{dock_channel_system_service_client_t=}"
+ "^{dock_channel_system_service_client_t=}16@0:8"
+ "^{dock_channel_system_service_client_t=}40@0:8r*16^?24r^v32"
+ "^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@0:8"
+ "^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16@0:8"
+ "^{dock_channel_system_service_usb_device_client_t=^v^{dock_channel_system_service_usb_device_client_functions_t}}"
+ "^{dock_channel_system_service_usb_device_client_t=^v^{dock_channel_system_service_usb_device_client_functions_t}}16@0:8"
+ "^{dock_channel_system_service_usb_host_port_client_t=^v^{dock_channel_system_service_usb_host_port_client_functions_t}}"
+ "^{dock_channel_system_service_usb_host_port_client_t=^v^{dock_channel_system_service_usb_host_port_client_functions_t}}16@0:8"
+ "^{dock_channel_system_service_usb_hub_port_client_t=^v^{dock_channel_system_service_usb_hub_port_client_functions_t}}"
+ "^{dock_channel_system_service_usb_hub_port_client_t=^v^{dock_channel_system_service_usb_hub_port_client_functions_t}}16@0:8"
+ "_acquiredNexusAndPinService"
+ "_activeNexusStatesByID"
+ "_baseName"
+ "_circularBuffer"
+ "_client"
+ "_clientsRequiringProbes"
+ "_connect_event_callback"
+ "_controllerAvailableSempahore"
+ "_createdSerialInterfaces"
+ "_deviceClass"
+ "_deviceQueue"
+ "_dockChannelsWithBackPressure"
+ "_dockChannelsWithPush"
+ "_hang_up_event_callback"
+ "_hardwareInitStep"
+ "_hardwareInitVersion"
+ "_highWatermarkStatus"
+ "_interestNotificationObject"
+ "_intermediate"
+ "_matchingArray"
+ "_nexus"
+ "_nexusClient"
+ "_nexusController"
+ "_nexusControllerClient"
+ "_nexusID"
+ "_nexusLocation"
+ "_nexusState"
+ "_permanentSuffixes"
+ "_pinService"
+ "_pinServiceClient"
+ "_pinServiceID"
+ "_platformRequiresPolling"
+ "_portID"
+ "_portLocation"
+ "_portNumber"
+ "_portType"
+ "_ppmEnabled"
+ "_ppmEnabledDockChannels"
+ "_ppmEndpoint"
+ "_probeAddedToNexus"
+ "_probeBaseName"
+ "_probeClient"
+ "_probeID"
+ "_probeIDArrayByPinServiceID"
+ "_probeInterface"
+ "_probeInterfaceClient"
+ "_probeInterfaceID"
+ "_probeSerialState"
+ "_probeStateByPinServiceID"
+ "_probeStatesByProbeID"
+ "_probeType"
+ "_rxOverflow"
+ "_serialPrefix"
+ "_serviceClass"
+ "_serviceID"
+ "_systemServiceController"
+ "_transaction"
+ "_transferResponseFirstWord"
+ "_transferredOwnership"
+ "_transportService"
+ "_txIntermediateBuffer"
+ "_usbDeviceClient"
+ "_usbHostPortClient"
+ "_usbHubPortClient"
+ "_vid"
+ "_water_mark_callback"
+ "acquireNexus:pinService:"
+ "acquireNexus:pinService:client:"
+ "acquireProbeInterfaceWithID:"
+ "acquireProbeInterfaceWithID:client:"
+ "acquireSerialInterface:"
+ "acquireSerialInterfaceWithID:client:"
+ "acquiredNexusAndPinService"
+ "activeNexusStatesByID"
+ "addObjectsFromArray:"
+ "addProbe:probeType:probeID:pinService:pinServiceID:"
+ "addProbe:probeType:probeID:pinService:pinServiceID:client:"
+ "addSerialInterfaceWithID:"
+ "applyEnablePPMDockChannelWorkaround:"
+ "arrayWithArray:"
+ "arrayWithObject:"
+ "bDeviceClass"
+ "bananasplit"
+ "baseName"
+ "chimp"
+ "circularBuffer"
+ "cleanupAllSerialInterfaces"
+ "cleanupAllSerialInterfacesForClient:"
+ "cleanupSerialInterface:"
+ "cleanupSerialInterface:client:"
+ "cleanupSerialInterfaceWithSuffix:"
+ "clearWatchdogStatus:"
+ "client"
+ "clientsRequiringProbes"
+ "com.apple.DeviceInterface.DebugUSB-0x%llx"
+ "com.apple.DeviceInterface.Probe-0x%llx-%@"
+ "configurePushForDockChannel:"
+ "connect_event_callback"
+ "controllerAvailableSempahore"
+ "copyNexusStateAndPinServiceForService:nexusState:pinService:"
+ "createClientWithDescription:terminationCallback:terminationContext:"
+ "createClientWithSystemService:description:"
+ "createClientWithSystemServiceID:description:"
+ "createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:"
+ "createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:nexusID:nexusLocation:portID:portLocation:client:"
+ "createSerialInterface:suffix:rxQueueLogSize:txQueueLogSize:"
+ "createSerialInterface:suffix:rxQueueLogSize:txQueueLogSize:client:"
+ "createSerialInterfaceWithSuffix:rxQueueLogSize:txQueueLogSize:permanent:"
+ "createSystemServiceFromIOService:"
+ "createSystemServiceFromServiceID:"
+ "createUSBDeviceClientWithDescription:terminationCallback:terminationContext:"
+ "createUSBHostPortClientWithDescription:terminationCallback:terminationContext:"
+ "createUSBHubPortClientWithDescription:terminationCallback:terminationContext:"
+ "createdSerialInterfaces"
+ "deviceClass"
+ "deviceQueue"
+ "discoveryIteratorPointer"
+ "dockChannelsWithBackPressure"
+ "dockChannelsWithPush"
+ "dock_channel_interface_kis_pam_endpoint_response_callback"
+ "enablePPM:"
+ "findChildrenForService:children:count:"
+ "findParentForService:parent:"
+ "getBaseName:length:"
+ "getClass:"
+ "getData:outBuffer:"
+ "getIDEFormatVersion:"
+ "getIOServiceFromSystemService:"
+ "getLocation:client:"
+ "getPID:"
+ "getPlatformCapability:size:uuid:"
+ "getPlatformMinimumPPWInterval:"
+ "getPortNumber:"
+ "getPortType:"
+ "getProductName:length:"
+ "getSerialNumber:length:"
+ "getServiceClass:"
+ "getServiceID:"
+ "getSuffix:length:"
+ "getTargetID:"
+ "getTransportService"
+ "getVID:"
+ "handleConnectEventOnChannel:"
+ "handleHangUpEventOnChannel:"
+ "handleHighWatermark"
+ "handleInterestNotificationForService:messageType:messageArgument:"
+ "handleLowWatermark"
+ "handlePAR:dockChannelID:words:"
+ "handlePinServiceRemoval:"
+ "handleProbeInterfaceAdded:"
+ "handleProbeInterfaceRemoved:"
+ "handleReadDataCallback:revents:t_lock:"
+ "handleSerialInterfaceAdded:suffix:"
+ "handleSerialInterfaceRemoved:suffix:"
+ "handleServiceRemoved:"
+ "handleWatermarkEventOnChannel:highWatermark:"
+ "hang_up_event_callback"
+ "hardwareInitStep"
+ "hardwareInitVersion"
+ "highWatermarkStatus"
+ "idProduct"
+ "idVendor"
+ "initWithBufferSize:"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithController:service:description:"
+ "initWithInterface:interfaceID:pinService:"
+ "initWithKISInterfaceID:kisManager:nexusController:queue:"
+ "initWithKISManager:nexusController:"
+ "initWithNexus:nexusID:intermediate:"
+ "initWithNexus:pinServiceID:description:"
+ "initWithNexusID:nexusLocation:queue:"
+ "initWithOwner:interfaceID:nexusClient:"
+ "initWithOwner:probeType:probeID:probeInterface:service:nexusController:"
+ "initWithOwner:serialInterfaceID:baseName:channelIndex:probeClient:"
+ "initWithProbeID:baseName:serialManager:serialController:queue:"
+ "initWithService:description:terminationCallback:terminationContext:"
+ "initWithService:serviceID:description:terminationCallback:terminationContext:queue:"
+ "initWithService:systemServiceController:"
+ "initWithService:transferOwnership:"
+ "initWithSystemServiceController:"
+ "initWithSystemServiceController:nexusController:serialManager:serialController:deviceQueue:"
+ "initWithSystemServiceController:queue:"
+ "initWithVendorID:productID:serialPrefix:"
+ "interestNotificationObject"
+ "intermediate"
+ "isEqualToString:"
+ "isIntermediateHubNexusDevice:"
+ "isProbeDeviceNexusDevice:"
+ "isUSBHubDevice:"
+ "isWatchdogAvailable"
+ "kUSBProductString"
+ "kUSBSerialNumberString"
+ "kanzi"
+ "kis-%x"
+ "koba"
+ "koko"
+ "listAvailableInterfaces:suffixes:count:"
+ "listAvailableInterfaces:suffixes:count:forClient:"
+ "listAvailableProbeInterfaces:count:"
+ "listAvailableProbeInterfaces:count:client:"
+ "matchClientsToProbes"
+ "matchingArray"
+ "nameForService:"
+ "nexus"
+ "nexusClient"
+ "nexusController"
+ "nexusControllerClient"
+ "nexusForNexusService:intermediate:"
+ "nexusID"
+ "nexusLocation"
+ "nexusServiceForService:"
+ "nexusState"
+ "nexusStateForNexusService:"
+ "permanentSuffixes"
+ "pinService"
+ "pinServiceClient"
+ "pinServiceID"
+ "platformRequiresPolling"
+ "poodle"
+ "port"
+ "portID"
+ "portLocation"
+ "portNumber"
+ "portServiceForService:"
+ "portType"
+ "ppmEnabled"
+ "ppmEnabledDockChannels"
+ "ppmEndpoint"
+ "probeAddedToNexus"
+ "probeBaseName"
+ "probeClient"
+ "probeID"
+ "probeIDArrayByPinServiceID"
+ "probeIDsForClient:"
+ "probeInterface"
+ "probeInterfaceClient"
+ "probeInterfaceID"
+ "probeSerialState"
+ "probeStateByPinServiceID"
+ "probeStatesByProbeID"
+ "probeType"
+ "processHardwareV1Part1:data:length:"
+ "processHardwareV1Part2:data:length:"
+ "putData:"
+ "r^{dock_channel_probe_interface_client_t=^v}"
+ "r^{dock_channel_probe_interface_client_t=^v}16@0:8"
+ "r^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}"
+ "r^{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}16@0:8"
+ "r^{dock_channel_probe_nexus_controller_t=^v}"
+ "r^{dock_channel_probe_nexus_controller_t=^v}16@0:8"
+ "r^{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}}"
+ "r^{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}}16@0:8"
+ "r^{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}}32@0:8@16^B24"
+ "r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}"
+ "r^{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@0:8"
+ "r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}"
+ "r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16@0:8"
+ "r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}20@0:8I16"
+ "r^{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}24@0:8Q16"
+ "readMemoryFromAddress:length:sequenceID:endpointAddress:portal:payloadWriteFlags:"
+ "readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:payloadWriteFlags:"
+ "readRSTAT:dockChannelID:"
+ "readRegistersFromIndex:count:sequenceID:endpointAddress:portal:"
+ "readRemainingBytes:readRemainingBytesCount:channelDockDataBase:dockChannelID:"
+ "readTx:maxLength:"
+ "readTxDataAvailable:"
+ "readWSTAT:dockChannelID:"
+ "readWords:channelDockDataBase:dockChannelID:"
+ "releaseNexusAndPinService"
+ "releaseNexusAndPinServiceForClient:"
+ "releaseProbeInterfaceWithID:"
+ "releaseProbeInterfaceWithID:client:"
+ "releaseSerialInterface:"
+ "releaseSerialInterfaceWithID:client:"
+ "removeProbeWithID:"
+ "removeProbeWithID:client:"
+ "removeSerialInterfaceWithID:"
+ "replaceBytesInRange:withBytes:length:"
+ "rxOverflow"
+ "scheduleWorkloop"
+ "sendCommandAsync:length:endpoint:timeout:"
+ "serialPrefix"
+ "serviceClass"
+ "serviceID"
+ "setAcquiredNexusAndPinService:"
+ "setConnect_event_callback:"
+ "setDiscoveryIterator:"
+ "setDockChannelsWithBackPressure:"
+ "setDockChannelsWithPush:"
+ "setHang_up_event_callback:"
+ "setHardwareInitStep:"
+ "setHardwareInitVersion:"
+ "setHighWatermarkStatus:"
+ "setNexusControllerClient:"
+ "setNexusID:"
+ "setNexusLocation:"
+ "setNexusState:"
+ "setPinService:"
+ "setPlatformRequiresPolling:"
+ "setPortID:"
+ "setPortLocation:"
+ "setPpmEnabled:"
+ "setPpmEnabledDockChannels:"
+ "setProbeSerialState:"
+ "setServiceConnection:"
+ "setTransferResponseFirstWord:"
+ "setWater_mark_callback:"
+ "setWithSet:"
+ "startListeningForTermination"
+ "storeReadData:length:client:"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "systemServiceController"
+ "tarsier"
+ "transaction"
+ "transferResponseFirstWord"
+ "transferredOwnership"
+ "transportService"
+ "txDataAvailable:"
+ "txIntermediateBuffer"
+ "unsignedCharValue"
+ "usbDeviceClient"
+ "usbHostPortClient"
+ "usbHubPortClient"
+ "v20@0:8C16"
+ "v24@0:8C16B20"
+ "v24@0:8^{dock_channel_probe_nexus_controller_client_t=^v}16"
+ "v32@0:8@16C24B28"
+ "v32@0:8I16I20^v24"
+ "v32@0:8Q16@\"NSString\"24"
+ "v32@0:8Q16@24"
+ "v32@0:8Q16r*24"
+ "vid"
+ "water_mark_callback"
+ "writeData:channel:"
+ "writeMemoryFromAddress:length:data:sequenceID:endpointAddress:portal:payloadWriteFlags:"
+ "writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:payloadWriteFlags:"
+ "writeRegistersFromIndex:count:registers:sequenceID:endpointAddress:portal:"
+ "writeRegistersFromIndex:count:registers:sequenceID:endpointAddress:toPortal:"
+ "writeRemainingBytes:channelDockDataBase:dockChannelID:writeData:writeRemainingBytesCount:"
+ "writeWords:channelDockDataBase:dockChannelID:writeData:"
+ "{dock_channel_probe_interface_client_t=\"_data\"^v}"
+ "{dock_channel_probe_interface_client_t=^v}16@0:8"
+ "{dock_channel_probe_nexus_client_t=\"_data\"^v\"_functions\"^{dock_channel_probe_nexus_client_functions_t}}"
+ "{dock_channel_probe_nexus_client_t=^v^{dock_channel_probe_nexus_client_functions_t}}16@0:8"
+ "{dock_channel_probe_nexus_controller_client_t=\"_data\"^v}"
+ "{dock_channel_probe_nexus_controller_client_t=^v}16@0:8"
+ "{dock_channel_probe_nexus_controller_t=\"_data\"^v}"
+ "{dock_channel_probe_nexus_controller_t=^v}16@0:8"
+ "{dock_channel_probe_nexus_t=\"_data\"^v\"_functions\"^{dock_channel_probe_nexus_functions_t}}"
+ "{dock_channel_probe_nexus_t=^v^{dock_channel_probe_nexus_functions_t}}16@0:8"
+ "{dock_channel_system_service_controller_t=\"_data\"^v\"_functions\"^{dock_channel_system_service_controller_functions_t}}"
+ "{dock_channel_system_service_controller_t=^v^{dock_channel_system_service_controller_functions_t}}16@0:8"
+ "{dock_channel_system_service_t=\"_data\"^v\"_functions\"^{dock_channel_system_service_functions_t}}"
+ "{dock_channel_system_service_t=^v^{dock_channel_system_service_functions_t}}16@0:8"
+ "{dock_channel_system_service_usb_device_client_t=\"_data\"^v\"_functions\"^{dock_channel_system_service_usb_device_client_functions_t}}"
+ "{dock_channel_system_service_usb_device_client_t=^v^{dock_channel_system_service_usb_device_client_functions_t}}16@0:8"
+ "{dock_channel_system_service_usb_host_port_client_t=\"_data\"^v\"_functions\"^{dock_channel_system_service_usb_host_port_client_functions_t}}"
+ "{dock_channel_system_service_usb_host_port_client_t=^v^{dock_channel_system_service_usb_host_port_client_functions_t}}16@0:8"
+ "{dock_channel_system_service_usb_hub_port_client_t=\"_data\"^v\"_functions\"^{dock_channel_system_service_usb_hub_port_client_functions_t}}"
+ "{dock_channel_system_service_usb_hub_port_client_t=^v^{dock_channel_system_service_usb_hub_port_client_functions_t}}16@0:8"
+ "\x83"
+ "\xe7\""
- "%s RSM portal DCM endpoint lookup failed"
- "%s%s"
- "-[DeviceInterfaceClientXPCServer portalTransaction:interfaceID:withReply:]"
- "-[ExternalInterfaceKIS cleanupClient:]"
- "-[RSMChannelInterfaceRSM cleanupClient:]"
- "-[RSMChannelSystemInterfaceAppleRSMChannel cleanupClient:]"
- "-[RSMInterfaceKIS cleanupClient:]"
- "-[TADFUInterfaceRSM cleanupClient:]"
- "-[TADFUTransportClient dealloc]"
- "-[TADFUTransportClient transportClientInterfacePointer]"
- "@\"BufferInfo\""
- "@\"DockChannelInterfaceKISPAM\""
- "@32@0:8r*16r*24"
- "@32@0:8r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16@24"
- "@32@0:8r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}24"
- "@48@0:8Q16r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}24r^{dock_channel_serial_interface_controller_t=^v^{dock_channel_serial_interface_controller_functions_t}}32@40"
- "@52@0:8@16Q24@32C40r^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}44"
- "AD!"
- "B24@0:8r^{dock_channel_serial_interface_client_callbacks_t=^?^v}16"
- "B32@0:8r*16r^{dock_channel_serial_interface_controller_client_callbacks_t=^?^v^?^v}24"
- "B40@0:8Q16I24S28C32C36"
- "B40@0:8r*16r*24C32C36"
- "B44@0:8S16S20r^I24C32S36C40"
- "B48@0:8Q16I24r^v28S36C40C44"
- "B48@0:8r*16^Q24r^*32^Q40"
- "B48@0:8r*16r*24C32C36@40"
- "B56@0:8r*16^Q24r^*32^Q40@48"
- "BufferInfo"
- "Dock channel serial controller not found!"
- "Error in async poll of event: %llu error: 0x%x (%s)"
- "T@\"BufferInfo\",&,N,V_inBufferInfo"
- "T@\"BufferInfo\",&,N,V_outBufferInfo"
- "T@\"DockChannelInterfaceKISPAM\",R,W,N,V_owner"
- "T@\"NSMutableDictionary\",&,N,V_serialInterfaces"
- "T@\"NSMutableDictionary\",R,N,V_serialInterfaceIDsByBase"
- "T@\"NSMutableDictionary\",R,N,V_serialInterfaceNameComponentsByName"
- "T@\"NSMutableSet\",&,N,V_serialControllerCreatedInterfaces"
- "T@\"NSString\",&,N,V_serialInterfaceBaseName"
- "TC,R,N,V_dcmEndpoint"
- "TI,R,N,V_serviceConnection"
- "T^{device_interface_manager_client_t=^v^{device_interface_manager_client_functions_t}},N,V_serialManagerClient"
- "T^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}},N,V_serialControllerClient"
- "T^{tadfu_transport_client_t=^v},R,N,V_transportClientPointer"
- "Tr*,N,V_serialInterfaceBaseNameCString"
- "Tr^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}},R,N,V_controllerClient"
- "Writing %d bytes"
- "^{tadfu_transport_client_t=^v}"
- "_controllerClient"
- "_dcmEndpoint"
- "_serialControllerCreatedInterfaces"
- "_serialInterfaceBaseName"
- "_serialInterfaceBaseNameCString"
- "_serialInterfaceIDsByBase"
- "_serialInterfaceNameComponentsByName"
- "_transportClientPointer"
- "acquireInterfaceWithID:client:"
- "addInterfaceWithID:"
- "asyncPARWithAddress:length:sequenceID:endpoint:portal:"
- "asyncPAWWithAddress:length:data:sequenceID:endpoint:portal:"
- "asyncPCRWithIndex:numberOfDoorbells:sequenceID:endpoint:portal:"
- "asyncPCWWithIndex:numberOfDoorbells:doorbells:portal:sequenceID:endpoint:"
- "controllerClient"
- "createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:"
- "createInterfaceWithBase:suffix:rxQueueLogSize:txQueueLogSize:client:"
- "dcmEndpoint"
- "getName:length:"
- "handleSerialInterfaceAdded:base:suffix:"
- "handleSerialInterfaceRemoved:base:suffix:"
- "initWithKISInterfaceID:kisManager:serialController:queue:"
- "initWithKISManager:serialController:"
- "initWithOwner:serialInterfaceID:baseName:channelIndex:controllerClient:"
- "initWithSerialManager:queue:"
- "isEqualTo:"
- "kis-%08x"
- "listAvailableInterfacesForBase:interfaceIDs:suffixes:count:"
- "listAvailableInterfacesForBase:interfaceIDs:suffixes:count:client:"
- "r^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}"
- "r^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}16@0:8"
- "readDoorbellsFromIndex:numberOfDoorbells:sequenceID:endpointAddress:toPortal:"
- "readMemoryFromAddress:withLength:sequenceID:endpointAddress:toPortal:"
- "receivedData %@"
- "registerCallbacksForBase:callbacks:"
- "releaseInterfaceWithID:client:"
- "removeInterfaceWithID:"
- "serialControllerCreatedInterfaces"
- "serialInterfaceBaseName"
- "serialInterfaceBaseNameCString"
- "serialInterfaceIDsByBase"
- "serialInterfaceNameComponentsByName"
- "setSerialControllerClient:"
- "setSerialControllerCreatedInterfaces:"
- "setSerialInterfaceBaseName:"
- "setSerialInterfaceBaseNameCString:"
- "setSerialInterfaces:"
- "setSerialManagerClient:"
- "setWithCapacity:"
- "transportClientPointer"
- "v24@0:8^{dock_channel_serial_interface_controller_client_t=^v^{dock_channel_serial_interface_controller_client_functions_t}}16"
- "v24@0:8r*16"
- "v40@0:8Q16r*24r*32"
- "writeDoorbellsFromIndex:numberOfDoorbells:doorbells:sequenceID:endpointAddress:toPortal:"
- "writeMemoryFromAddress:withLength:withData:sequenceID:endpointAddress:toPortal:"
- "\xc7\""

```
