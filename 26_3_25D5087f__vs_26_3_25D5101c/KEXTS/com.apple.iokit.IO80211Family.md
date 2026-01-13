## com.apple.iokit.IO80211Family

> `com.apple.iokit.IO80211Family`

```diff

-1540.9.0.0.0
+1540.11.0.0.0
   __TEXT.__os_log: 0x96d3
-  __TEXT.__const: 0x13128
-  __TEXT.__cstring: 0x90d28
-  __TEXT_EXEC.__text: 0x26e8ac
+  __TEXT.__const: 0x13138
+  __TEXT.__cstring: 0x90d2e
+  __TEXT_EXEC.__text: 0x26f6c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5778
   __DATA.__common: 0x1fe8

   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0x538
   __DATA_CONST.__mod_term_func: 0x538
-  __DATA_CONST.__const: 0x38658
+  __DATA_CONST.__const: 0x386d0
   __DATA_CONST.__kalloc_type: 0x9c80
   __DATA_CONST.__kalloc_var: 0x820
-  UUID: 198103EE-680C-330D-AD6A-0AC014362F98
-  Functions: 12566
-  Symbols:   19662
+  UUID: 5E3F34FD-AF3A-3FD8-8375-B140E8A098B7
+  Functions: 12571
+  Symbols:   19668
   CStrings:  14435
 
Symbols:
+ __ZN16WCLConfigManager22getEapDelayedAssocInfoEP20apple80211_ssid_dataP21apple80211_bssid_data
+ __ZN18IO80211NANDataPeer12getAvgRssi5GEv
+ __ZN18IO80211NANDataPeer13getAvgRssi24GEv
+ __ZN18IO80211NANDataPeer16clearNANMgmtPeerEv
+ __ZN18IO80211NANDataPeer22getBeaconReceivedCountEv
CStrings:
+ "\"IO80211_kexts-1540.11\""
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCwugCyG8eEyUdsVtc1_ZwXZSq_TbNNPVxnDnU/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
+ "IO80211_kexts-1540.11"
+ "Jan  4 2026 19:18:38"
+ "getEapDelayedAssocInfo"
- "\"IO80211_kexts-1540.9\""
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD2zugAfKJyK_4weG6pSsx1si18YbeqFbYuew-c/Library/Caches/com.apple.xbs/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
- "Dec  5 2025 22:46:52"
- "IO80211_kexts-1540.9"
- "wlan.debug.getSSID"

```
