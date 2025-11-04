## carkitd

> `/usr/libexec/carkitd`

```diff

-746.11.0.0.0
-  __TEXT.__text: 0x88e20
-  __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_stubs: 0x10360
-  __TEXT.__objc_methlist: 0x738c
+746.17.0.0.0
+  __TEXT.__text: 0x8a504
+  __TEXT.__auth_stubs: 0x14b0
+  __TEXT.__objc_stubs: 0x10780
+  __TEXT.__objc_methlist: 0x74d4
   __TEXT.__const: 0x212
-  __TEXT.__cstring: 0x6042
-  __TEXT.__gcc_except_tab: 0x1ed0
-  __TEXT.__objc_methname: 0x166f0
-  __TEXT.__oslogstring: 0xf3bd
-  __TEXT.__objc_classname: 0x1045
-  __TEXT.__objc_methtype: 0x4441
-  __TEXT.__dlopen_cstrs: 0x1c6
+  __TEXT.__cstring: 0x60c2
+  __TEXT.__gcc_except_tab: 0x1efc
+  __TEXT.__objc_methname: 0x16c1a
+  __TEXT.__oslogstring: 0xf4fd
+  __TEXT.__objc_classname: 0x107c
+  __TEXT.__objc_methtype: 0x4474
+  __TEXT.__dlopen_cstrs: 0x16e
   __TEXT.__swift5_typeref: 0xc4
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x45
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1e70
+  __TEXT.__unwind_info: 0x1ec0
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xa80
-  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__got: 0x878
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x3178
-  __DATA_CONST.__cfstring: 0x6e20
-  __DATA_CONST.__objc_classlist: 0x298
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__const: 0x31a0
+  __DATA_CONST.__cfstring: 0x6f00
+  __DATA_CONST.__objc_classlist: 0x2a0
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_intobj: 0x8d0
   __DATA_CONST.__objc_arraydata: 0x968
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x137f0
-  __DATA.__objc_selrefs: 0x4ac8
-  __DATA.__objc_ivar: 0x73c
-  __DATA.__objc_data: 0x1a70
+  __DATA.__objc_const: 0x13a18
+  __DATA.__objc_selrefs: 0x4bd0
+  __DATA.__objc_ivar: 0x754
+  __DATA.__objc_data: 0x1ac0
   __DATA.__data: 0x1a90
-  __DATA.__bss: 0x158
+  __DATA.__bss: 0x148
   __DATA.__common: 0x18
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
+  - /System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E33A86E-40D5-3E78-948A-953DF088BA0E
-  Functions: 3058
-  Symbols:   627
-  CStrings:  7199
+  UUID: 466C199E-4673-37C1-AA3F-39965D570482
+  Functions: 3091
+  Symbols:   628
+  CStrings:  7268
 
Symbols:
+ _CAFAccessoryTypeNavigation
+ _CAFServiceTypeRouteSharing
+ _OBJC_CLASS_$_CAFASCTree
+ _OBJC_CLASS_$_CRCarPlayFeatureDenyList
- _CMBaseObjectGetVTable
- _FigEndpointCopyActiveCarPlayEndpoint
- _FigEndpointGetCMBaseObject
CStrings:
+ "@\"CRPairingAirPlaySessionInfo\""
+ "@40@0:8B16@20@28B36"
+ "AirPlaySessionUpdating"
+ "CAF"
+ "CRPairingAirPlaySessionInfo"
+ "CarPlayFeatureDenyList"
+ "FeatureDenyList: fetched CarPlay MobileAsset: %@"
+ "FeatureDenyList: not found: %@"
+ "T@\"CRPairingAirPlaySessionInfo\",&,N,V_connectedSessionInfo"
+ "T@\"NSString\",R,C,N,V_oemName"
+ "T@\"NSString\",R,C,N,V_userVisibleReason"
+ "TB,N,V_hasGaugeCluster"
+ "TB,R,N,V_supportsLodWidgets"
+ "TB,R,N,V_supportsRouteSharing"
+ "_connectedSessionInfo"
+ "_hasGaugeCluster"
+ "_oemName"
+ "_presentRouteSharingInfoPromptWithCompletion:"
+ "_presentRouteSharingPermissionPromptWithCompletion:"
+ "_setRouteSharingStatus:forPromptFlow:"
+ "_supportsLodWidgets"
+ "_supportsRouteSharing"
+ "_userVisibleReason"
+ "connected a session for the current prompt flow (%{public}@)"
+ "connected a session that doesn't match the current prompt flow"
+ "connected session, continuing prompt flow. (%{public}@)"
+ "connectedSessionInfo"
+ "handleConnectedAirPlaySession:"
+ "handleDidConnectSession:forVehicle:"
+ "hasAccessory:service:"
+ "hasGaugeCluster"
+ "hasShownRouteSharingFollowup"
+ "initWithCarSessionConfiguration:"
+ "initWithSupportsRouteSharing:userVisibleReason:oemName:supportsLodWidgets:"
+ "oemName"
+ "pairingPromptFlow:receivedRouteSharingPermissionResponse:"
+ "presentRouteSharingInfoPromptForOEMName:reason:responseHandler:"
+ "presentRouteSharingPermissionPromptForVehicleName:oemName:responseHandler:"
+ "received response for route sharing info prompt: %{public}@"
+ "received response for route sharing permission prompt: %{public}@"
+ "reloadWithURL:notify:"
+ "route sharing accepted"
+ "route sharing declined"
+ "route sharing info"
+ "route sharing info prompt received response: %{public}@"
+ "route sharing permission"
+ "route sharing permission prompt received response: %{public}@"
+ "routeSharing"
+ "routeSharingMode"
+ "routeSharingOEMName"
+ "routeSharingStatus"
+ "routeSharingUserVisibleReason"
+ "setConnectedSessionInfo:"
+ "setHasGaugeCluster:"
+ "setHasShownRouteSharingFollowup:"
+ "setOemName:"
+ "setRouteSharingMode:"
+ "setRouteSharingReason:"
+ "setRouteSharingStatus:"
+ "setSupportsLodWidgets:"
+ "setSupportsRouteSharing:"
+ "supportsLodWidgets"
+ "supportsRouteSharing"
+ "supportsRouteSharing: %@, supportsLodWidgets: %@"
+ "updateWithAirPlaySessionInfo:"
+ "userVisibleReason"
+ "waiting on session"
- "failed to get an active carplay endpoint for %@"
- "failed to get endpoint value for info response, error: %i"
- "kAPEndpointProperty_EndpointInfo"
- "softlink:r:path:/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender"
- "uiContextLastOnDisplayURLs"
- "uiContextNowOnDisplayURLs"
- "vehicle %@ declares ui context support for last on display and/or now on display"
- "vehicle %@ does not declare ui context support"

```
