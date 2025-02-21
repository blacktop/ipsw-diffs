## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-23.1.1.2.0
-  __TEXT.__text: 0x26b30
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x2b24
+24.21.0.0.0
+  __TEXT.__text: 0x29ba4
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x32a4
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x80d0
-  __TEXT.__unwind_info: 0x978
-  __TEXT.__objc_classname: 0x35c
-  __TEXT.__objc_methname: 0x6fe0
-  __TEXT.__objc_methtype: 0xf24
-  __TEXT.__objc_stubs: 0x2860
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xa98
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__cstring: 0x81d7
+  __TEXT.__unwind_info: 0xb80
+  __TEXT.__objc_classname: 0x37e
+  __TEXT.__objc_methname: 0x6ddd
+  __TEXT.__objc_methtype: 0xfed
+  __TEXT.__objc_stubs: 0x2b40
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x9f8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1538
+  __DATA_CONST.__objc_selrefs: 0x15e0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH_CONST.__const: 0x80
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x6448
-  __AUTH.__objc_data: 0x460
+  __AUTH_CONST.__objc_const: 0x59e8
+  __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5d8
-  __DATA.__data: 0x900
+  __DATA.__objc_ivar: 0x5e8
+  __DATA.__data: 0x970
   __DATA.__common: 0x8
   __DATA.__bss: 0x34
   __DATA_DIRTY.__objc_data: 0x370

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1138
-  Symbols:   1342
-  CStrings:  2479
+  Functions: 1442
+  Symbols:   1703
+  CStrings:  2440
 
Symbols:
+ _OBJC_CLASS_$_AASystemStateMonitor
+ _OBJC_CLASS_$_AAUSBSupportedDeviceManager
+ _OBJC_METACLASS_$_AASystemStateMonitor
+ _OBJC_METACLASS_$_AAUSBSupportedDeviceManager
+ _objc_getProperty
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_atomic_copy
CStrings:
+ "\x01\x11\x11"
+ "\x11\x11\x1a"
+ "### Activate failed: %{error}\n"
+ "### proxCardUserActionOnHeadphone failed to start XPC"
+ "### proxCardUserActionOnHeadphone no XPC"
+ "-[AASystemStateMonitor _activate:]"
+ "-[AASystemStateMonitor _activate:]_block_invoke"
+ "-[AASystemStateMonitor _activateDirect:]"
+ "-[AASystemStateMonitor _activateXPC:reactivate:]"
+ "-[AASystemStateMonitor _activateXPC:reactivate:]_block_invoke"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_2"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted]_block_invoke_5"
+ "-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStopped]"
+ "-[AASystemStateMonitor _interrupted]"
+ "-[AASystemStateMonitor _invalidated]"
+ "-[AASystemStateMonitor _reportError:]"
+ "-[AASystemStateMonitor aaDeviceConnectionChanged:withAADevice:]"
+ "-[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:]"
+ "-[AASystemStateMonitor activateWithCompletion:]_block_invoke"
+ "-[AASystemStateMonitor invalidate]_block_invoke"
+ "-[AAUSBSupportedDeviceManager _handleServerDied]_block_invoke"
+ "-[AAUSBSupportedDeviceManager _interrupted]"
+ "-[AAUSBSupportedDeviceManager _invalidated]"
+ "-[AAUSBSupportedDeviceManager _reportError:]"
+ "-[AAUSBSupportedDeviceManager invalidate]_block_invoke"
+ "-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]"
+ "-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:]_block_invoke"
+ "@\"AADeviceManager\""
+ "@\"AAServicesDaemon\""
+ "AASystemStateMonitor"
+ "AASystemStateMonitor, CID 0x%X"
+ "AAUSBSupportedDeviceManager"
+ "AAUSBSupportedDeviceManager, CID 0x%X"
+ "BTMagicPairingSettings[%@]: Name(%lu), PID: %@, VID: %@"
+ "BTMagicPairingSettings[%@]: Name(%lu): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
+ "Calling connection changed handler with device %@, CID 0x%X"
+ "Calling route changed handler with device %@"
+ "Connected discovery start"
+ "Connected discovery stop"
+ "DeviceManager interrupted"
+ "DeviceManager invalidated"
+ "HRMCapableDeviceChangedHandler"
+ "T@\"AADeviceManager\",&,N,V_connectedDiscovery"
+ "T@\"AAServicesDaemon\",&,N,V_internalServicesDaemon"
+ "T@\"NSMutableDictionary\",&,N,V_devicesMap"
+ "T@?,C,V_HRMCapableDeviceChangedHandler"
+ "T@?,C,V_aaDeviceConnectionChangedHandler"
+ "T@?,C,V_aaDeviceRouteChangedHandler"
+ "TB,R,N"
+ "TB,R,V_isHRMCapableDevicePresent"
+ "_HRMCapableDeviceChangedHandler"
+ "_aaDeviceConnectionChangedHandler"
+ "_aaDeviceRouteChangedHandler"
+ "_connectedDeviceDiscoveryEnsureStarted"
+ "_connectedDeviceDiscoveryEnsureStopped"
+ "_connectedDeviceFound:"
+ "_connectedDeviceLost:"
+ "_connectedDiscovery"
+ "_devicesMap"
+ "_internalServicesDaemon"
+ "_isHRMCapableDevicePresent"
+ "aaDeviceConnectionChanged:withAADevice:"
+ "aaDeviceConnectionChangedHandler"
+ "aaDeviceRouteChanged:withAADevice:"
+ "aaDeviceRouteChangedHandler"
+ "activateSystemStateMonitorDirect:completion:"
+ "connectedDiscovery"
+ "devicesMap"
+ "direct"
+ "internalServicesDaemon"
+ "invalidateSystemStateMonitorDirect:"
+ "isHRMCapableDevicePresent"
+ "objectForKeyedSubscript:"
+ "proxCardUserActionOnHeadphone CID 0x%X device %@"
+ "proxCardUserActionOnHeadphone:btAddress:withAction:completion:"
+ "proxCardUserActionOnHeadphone:withAction:completion:"
+ "removeObjectForKey:"
+ "routed"
+ "setAaDeviceConnectionChangedHandler:"
+ "setAaDeviceRouteChangedHandler:"
+ "setConnectedDiscovery:"
+ "setDevicesMap:"
+ "setHRMCapableDeviceChangedHandler:"
+ "setInternalServicesDaemon:"
+ "systemStateMonitorActivate:completion:"
+ "v16@?0@\"AudioAccessoryDevice\"8"
+ "v28@0:8B16@20"
+ "v32@0:8@\"AASystemStateMonitor\"16@?<v@?@\"NSError\">24"
+ "v36@0:8@16C24@?28"
+ "v44@0:8@\"AAUSBSupportedDeviceManager\"16@\"NSString\"24C32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@16@24C32@?36"
- "-[SRDiscoveredDevice _setBtAddress:]"
- "-[SRDiscoveredDevice _setConnectionState:]"
- "-[SRDiscoveredDevice _setInUseBannerBackoffReason:]"
- "-[SRDiscoveredDevice _setInUseBannerBackoffTick:]"
- "-[SRDiscoveredDevice _setInUseBannerShown:]"
- "-[SRDiscoveredDevice _setIsNearby:]"
- "-[SRDiscoveredDevice _setMutedSpeakerForRemotePhoneCall:]"
- "-[SRDiscoveredDevice _setNearbyConnectedSourceCount:]"
- "-[SRDiscoveredDevice _setNearbyInEar:]"
- "-[SRDiscoveredDevice _setNearbyLastRouteHost:]"
- "-[SRDiscoveredDevice _setNearbyName:]"
- "-[SRDiscoveredDevice _setNearbyOutOfCaseTime:]"
- "-[SRDiscoveredDevice _setNearbyPaired:]"
- "-[SRDiscoveredDevice _setNearbyPrevInEar:]"
- "-[SRDiscoveredDevice _setNearbyProductID:]"
- "-[SRDiscoveredDevice _setNearbyStreamState:]"
- "-[SRDiscoveredDevice _setNearbyiCloudSignIn:]"
- "-[SRDiscoveredDevice _setRouteToWxAfterUnhide:]"
- "-[SRDiscoveredDevice _setUserConnectedState:]"
- "1\x13\x11"
- "@\"SFDevice\""
- "BTMagicPairingSettings[%@]: Name(%ld), PID: %@, VID: %@"
- "BTMagicPairingSettings[%@]: Name(%ld): %@, PID: %@, VID: %@, MainKey: %@, AccKey: %@, MainHint: %@, AccHint: %@, IRK: %@, Enc: %@, V: %@, C: %@, R: %@, BM: %@, DID1: %@, DID2: %@, LS: %@, LSv2: %@, S: %@, SS: %@, OBC: %@-%@"
- "Disconnected"
- "Disconnecting"
- "HFP Call"
- "HFP Other"
- "SRDiscoveredDevice"
- "Setting btaddress %@ -> %@"
- "Setting connectionState %s -> %s"
- "Setting inUseBannerBackoff %@ %@ -> %@"
- "Setting inUseBannerBackoffTick %@ %u -> %u"
- "Setting inUseBannerShown %@ %s -> %s"
- "Setting isNearby %@ %s -> %s"
- "Setting muted speaker for remote phone call %s -> %s"
- "Setting nearbyConnectedSourceCount %@ %d -> %d"
- "Setting nearbyInEar %@ %s -> %s"
- "Setting nearbyLastRouteHost %@ %@ -> %@"
- "Setting nearbyName %@ %@ -> %@"
- "Setting nearbyPaired %@ %s -> %s"
- "Setting nearbyPrevInEar %@ %s -> %s"
- "Setting nearbyProductID %@ %u -> %u"
- "Setting nearbyStreamState %@ %s -> %s"
- "Setting nearbyiCloudSignIn %@ %s -> %s"
- "Setting outOfCaseTime %@ %d -> %d"
- "Setting routeToWxAfterUnhide %@ %s -> %s"
- "Setting userConnectedState %s -> %s"
- "T@\"NSData\",R,N,V_nearbyLastRouteHost"
- "T@\"NSString\",R,C,N,V_btAddress"
- "T@\"NSString\",R,C,N,V_nearbyName"
- "T@\"NSString\",R,N,V_inUseBannerBackoffReason"
- "T@\"SFDevice\",R,C,N,V_nearbyWxDevice"
- "TB,R,N,V_inUseBannerShown"
- "TB,R,N,V_isNearby"
- "TB,R,N,V_mutedSpeakerForRemotePhoneCall"
- "TB,R,N,V_nearbyPaired"
- "TB,R,N,V_nearbyiCloudSignIn"
- "TB,R,N,V_routeToWxAfterUnhide"
- "TB,R,N,V_userConnectedState"
- "TC,R,N,V_connectionState"
- "TC,R,N,V_nearbyConnectedSourceCount"
- "TC,R,N,V_nearbyOutOfCaseTime"
- "TI,R,N,V_nearbyProductID"
- "TQ,R,N,V_inUseBannerBackoffTick"
- "Ti,R,N,V_nearbyInEar"
- "Ti,R,N,V_nearbyPrevInEar"
- "Tq,R,N,V_nearbyStreamState"
- "Unspecified"
- "_btAddress"
- "_connectionState"
- "_inUseBannerBackoffReason"
- "_inUseBannerBackoffTick"
- "_inUseBannerShown"
- "_isNearby"
- "_mutedSpeakerForRemotePhoneCall"
- "_nearbyConnectedSourceCount"
- "_nearbyInEar"
- "_nearbyLastRouteHost"
- "_nearbyName"
- "_nearbyOutOfCaseTime"
- "_nearbyPaired"
- "_nearbyPrevInEar"
- "_nearbyProductID"
- "_nearbyStreamState"
- "_nearbyWxDevice"
- "_nearbyiCloudSignIn"
- "_routeToWxAfterUnhide"
- "_setBtAddress:"
- "_setConnectionState:"
- "_setInUseBannerBackoffReason:"
- "_setInUseBannerBackoffTick:"
- "_setInUseBannerShown:"
- "_setIsNearby:"
- "_setMutedSpeakerForRemotePhoneCall:"
- "_setNearbyConnectedSourceCount:"
- "_setNearbyInEar:"
- "_setNearbyLastRouteHost:"
- "_setNearbyName:"
- "_setNearbyOutOfCaseTime:"
- "_setNearbyPaired:"
- "_setNearbyPrevInEar:"
- "_setNearbyProductID:"
- "_setNearbyStreamState:"
- "_setNearbyWxDevice:"
- "_setNearbyiCloudSignIn:"
- "_setRouteToWxAfterUnhide:"
- "_setUserConnectedState:"
- "_userConnectedState"
- "btAddress"
- "connectionState"
- "inUseBannerBackoffReason"
- "inUseBannerBackoffTick"
- "inUseBannerShown"
- "isEqualToData:"
- "isEqualToString:"
- "isNearby"
- "mutedSpeakerForRemotePhoneCall"
- "nearbyConnectedSourceCount"
- "nearbyInEar"
- "nearbyLastRouteHost"
- "nearbyName"
- "nearbyOutOfCaseTime"
- "nearbyPaired"
- "nearbyPrevInEar"
- "nearbyProductID"
- "nearbyStreamState"
- "nearbyWxDevice"
- "nearbyiCloudSignIn"
- "q"
- "q16@0:8"
- "routeToWxAfterUnhide"
- "userConnectedState"
- "v24@0:8q16"

```
