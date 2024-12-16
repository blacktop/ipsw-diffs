## HomeKitDaemonLegacy

> `/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy`

```diff

-1241.3.7.0.0
-  __TEXT.__text: 0xa7fd28
-  __TEXT.__auth_stubs: 0x3d50
-  __TEXT.__objc_methlist: 0x65bd4
+1241.4.10.0.0
+  __TEXT.__text: 0xa80718
+  __TEXT.__auth_stubs: 0x3d60
+  __TEXT.__objc_methlist: 0x65c94
   __TEXT.__const: 0x114a4
   __TEXT.__swift5_typeref: 0xdc6
-  __TEXT.__cstring: 0x527fd
+  __TEXT.__cstring: 0x527e3
   __TEXT.__constg_swiftt: 0xce0
   __TEXT.__swift5_reflstr: 0xa3a
-  __TEXT.__swift5_fieldmd: 0x8bc
+  __TEXT.__swift5_fieldmd: 0x8b0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__oslogstring: 0xf6230
+  __TEXT.__oslogstring: 0xf6265
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_capture: 0x248
-  __TEXT.__gcc_except_tab: 0x26f8c
+  __TEXT.__gcc_except_tab: 0x26f50
   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x1eb50
+  __TEXT.__unwind_info: 0x1eb68
   __TEXT.__eh_frame: 0x16b8
-  __TEXT.__objc_classname: 0x11a76
-  __TEXT.__objc_methname: 0x11362d
-  __TEXT.__objc_methtype: 0x22d3d
-  __TEXT.__objc_stubs: 0xa1da0
-  __DATA_CONST.__got: 0x5950
-  __DATA_CONST.__const: 0x14ca0
+  __TEXT.__objc_classname: 0x11a77
+  __TEXT.__objc_methname: 0x113652
+  __TEXT.__objc_methtype: 0x22d3a
+  __TEXT.__objc_stubs: 0xa1d20
+  __DATA_CONST.__got: 0x5968
+  __DATA_CONST.__const: 0x14cc8
   __DATA_CONST.__objc_classlist: 0x3330
   __DATA_CONST.__objc_catlist: 0x248
   __DATA_CONST.__objc_protolist: 0x13d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dbc8
+  __DATA_CONST.__objc_selrefs: 0x2dbf0
   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x2a98
   __DATA_CONST.__objc_arraydata: 0x2838
-  __AUTH_CONST.__auth_got: 0x1ec0
-  __AUTH_CONST.__auth_ptr: 0x3c8
+  __AUTH_CONST.__auth_got: 0x1ec8
+  __AUTH_CONST.__auth_ptr: 0x3c0
   __AUTH_CONST.__const: 0x126b8
-  __AUTH_CONST.__cfstring: 0x4cea0
-  __AUTH_CONST.__objc_const: 0xdbbe8
+  __AUTH_CONST.__cfstring: 0x4cee0
+  __AUTH_CONST.__objc_const: 0xdbd18
   __AUTH_CONST.__objc_arrayobj: 0x870
   __AUTH_CONST.__objc_intobj: 0x2e80
   __AUTH_CONST.__objc_dictobj: 0x1838
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xf988
+  __AUTH.__objc_data: 0xf980
   __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0x7e20
+  __DATA.__objc_ivar: 0x7e3c
   __DATA.__data: 0xff78
-  __DATA.__bss: 0x37f8
+  __DATA.__bss: 0x3818
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x10eb0
   __DATA_DIRTY.__data: 0x5f8
   __DATA_DIRTY.__common: 0x90
-  __DATA_DIRTY.__bss: 0xe90
+  __DATA_DIRTY.__bss: 0xe70
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 41772
-  Symbols:   44467
-  CStrings:  67841
+  Functions: 41789
+  Symbols:   44491
+  CStrings:  67851
 
Symbols:
+ _HMAccessoryMatterDeviceTypeIDCodingKey
+ _HMAccessoryMatterDeviceTypeIDUpdateMessage
+ _HMAccessoryMatterDeviceTypeIDUpdateMessageKey
+ _OBJC_CLASS_$_HMMutableCHIPAccessorySetupPayload
+ _nw_interface_get_name
CStrings:
+ "\x01\x14\x18"
+ "\x02/\x06\x1a\x12\x18\x17$+"
+ "%{public}@Accessory: %@, Updated matterDeviceTypeID to %@"
+ "%{public}@Accessory: %@, is paired - dropping provided device type update to %@"
+ "%{public}@Failed to fetch CHIPPairings per request: %@"
+ "%{public}@Fetching CHIP pairings per request"
+ "%{public}@[Pair-Verify %{public}@] matched service %{public}@ doesn't match the service transaction: %{public}@. Removing it to re-add."
+ "-seed"
+ "@64@0:8@16Q24@32@40@48Q56"
+ "T@\"NSData\",C,V_ipv4Signature"
+ "T@\"NSData\",C,V_ipv6Signature"
+ "T@\"NSNumber\",C,N,V_matterDeviceTypeID"
+ "T@\"NSNumber\",C,V_matterDeviceTypeID"
+ "T@\"NSString\",C,V_wifiAccessPointOUI"
+ "T@\"NSString\",C,V_wifiBSSID"
+ "T@\"NSString\",C,V_wifiSSID"
+ "TB,V_isIPAccessoryServer"
+ "TB,V_isInfraRelayInterfaceActive"
+ "TB,V_isSeenOnBonjour"
+ "TQ,V_mediaSystemConfiguration"
+ "_fetchPairingsFromAccessoryServer:completion:"
+ "_ipv4Signature"
+ "_ipv6Signature"
+ "_isIPAccessoryServer"
+ "_isInfraRelayInterfaceActive"
+ "_isSeenOnBonjour"
+ "_matterDeviceTypeID"
+ "_mediaSystemConfiguration"
+ "_wifiAccessPointOUI"
+ "_wifiBSSID"
+ "_wifiSSID"
+ "accessoryServer:didUpdateMatterDeviceTypeID:"
+ "deviceTypeID"
+ "fetchLastKnownPairingsWithCompletionHandler:"
+ "initWithHome:nodeId:endpointId:clusterId:commandId:source:"
+ "ipv4Signature"
+ "ipv6Signature"
+ "ir0"
+ "isIPAccessoryServer"
+ "isInfraRelayInterfaceActive"
+ "isSeenOnBonjour"
+ "matterDeviceTypeID"
+ "mediaSystemConfiguration"
+ "setDeviceTypeID:"
+ "setIpv4Signature:"
+ "setIpv6Signature:"
+ "setIsIPAccessoryServer:"
+ "setIsInfraRelayInterfaceActive:"
+ "setIsSeenOnBonjour:"
+ "setMatterDeviceTypeID:"
+ "setMediaSystemConfiguration:"
+ "setWifiAccessPointOUI:"
+ "setWifiBSSID:"
+ "setWifiSSID:"
+ "submitLogEventForCommandResponse:nodeID:endpointID:clusterID:commandID:source:error:"
+ "v72@0:8@16Q24@32@40@48Q56@64"
+ "wifiAccessPointOUI"
+ "wifiBSSID"
+ "wifiSSID"
+ "\x81\x11\x122!/\x03!\xf0\x11!"
- "\x01\x13\x18"
- "\x02/\x06\x1a\x12\x18\x16$+"
- "%{public}@Fetching locally cached CHIP pairings"
- "%{public}@[%{public}@] Finished generation of home configuration log event for analytics"
- "%{public}@[%{public}@] Home Configuration got updated. Scheduling of new log event generation."
- "%{public}@[%{public}@] Starting generation of home configuration log event for analytics"
- "-internal"
- "@72@0:8@16Q24@32@40@48@56Q64"
- "Generate Home Configuration Log Event"
- "T@\"NSData\",C,V_cachedIpv4Signature"
- "T@\"NSData\",C,V_cachedIpv6Signature"
- "T@\"NSObject\",N,R,Vfields"
- "T@\"NSString\",C,V_cachedWifiBSSID"
- "T@\"NSString\",C,V_cachedWifiSSID"
- "TB,V_cachedIsConnectedToInternet"
- "TQ,V_cachedCellularDataConnectionState"
- "TQ,V_cachedEthernetConnectionState"
- "TQ,V_cachedWifiConnectionState"
- "Tq,V_cachedBluetoothState"
- "_cachedBluetoothState"
- "_cachedCellularDataConnectionState"
- "_cachedEthernetConnectionState"
- "_cachedIpv4Signature"
- "_cachedIpv6Signature"
- "_cachedIsConnectedToInternet"
- "_cachedWifiBSSID"
- "_cachedWifiConnectionState"
- "_cachedWifiSSID"
- "cachedBluetoothState"
- "cachedCellularDataConnectionState"
- "cachedEthernetConnectionState"
- "cachedIpv4Signature"
- "cachedIpv6Signature"
- "cachedIsConnectedToInternet"
- "cachedWifiBSSID"
- "cachedWifiConnectionState"
- "cachedWifiSSID"
- "fetchPairingsWithCompletionHandler:"
- "fields"
- "initWithHome:nodeId:endpointId:clusterId:commandId:fields:source:"
- "setCachedBluetoothState:"
- "setCachedCellularDataConnectionState:"
- "setCachedEthernetConnectionState:"
- "setCachedIpv4Signature:"
- "setCachedIpv6Signature:"
- "setCachedIsConnectedToInternet:"
- "setCachedWifiBSSID:"
- "setCachedWifiConnectionState:"
- "setCachedWifiSSID:"
- "submitLogEventForCommandResponse:nodeID:endpointID:clusterID:commandID:fields:source:error:"
- "v80@0:8@16Q24@32@40@48@56Q64@72"
- "\x81\x11\x122!/\x03!\xf0!"

```
