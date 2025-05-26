## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2180.79.1.1.1
-  __TEXT.__text: 0x18c120
+2215.13.4.0.0
+  __TEXT.__text: 0x18c3e0
   __TEXT.__auth_stubs: 0x31e0
   __TEXT.__objc_methlist: 0x180e0
-  __TEXT.__cstring: 0x21dfb
+  __TEXT.__cstring: 0x22064
   __TEXT.__const: 0x1e8
   __TEXT.__gcc_except_tab: 0x40e0
-  __TEXT.__oslogstring: 0x756f
+  __TEXT.__oslogstring: 0x75a5
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x7f78
+  __TEXT.__unwind_info: 0x7f7c
   __TEXT.__objc_classname: 0x59c9
-  __TEXT.__objc_methname: 0x2ff72
-  __TEXT.__objc_methtype: 0x976c
+  __TEXT.__objc_methname: 0x2ffb8
+  __TEXT.__objc_methtype: 0x977d
   __TEXT.__objc_stubs: 0x1d9c0
   __DATA_CONST.__got: 0x3a58
-  __DATA_CONST.__const: 0x5140
+  __DATA_CONST.__const: 0x5138
   __DATA_CONST.__objc_classlist: 0xff0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x240

   __DATA_CONST.__objc_selrefs: 0x9808
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__objc_const: 0xa550
-  __AUTH_CONST.__cfstring: 0x16080
+  __AUTH_CONST.__cfstring: 0x161c0
   __AUTH_CONST.__const: 0xc38
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x258

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9968
-  Symbols:   34953
-  CStrings:  12363
+  Functions: 9969
+  Symbols:   34958
+  CStrings:  12373
 
Symbols:
+ -[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:]
+ -[AVOutputContextManager outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:]
+ -[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:]
+ _AVFigRoutingContextOutputContextImplSetShowErrorPromptDictionaryToEcho
+ _AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _AVOutputContextManagerDidFailToConnectToOutputDeviceUserInfoKey
+ _AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey
+ _AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo
+ ___102-[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:]_block_invoke
+ ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.149
+ ___block_literal_global.337
+ ___block_literal_global.375
+ ___block_literal_global.402
+ ___block_literal_global.407
+ __unnamed_array_storage.503
+ __unnamed_array_storage.512
+ _objc_msgSend$_copyInterstitialEventCoordinatorEnsuringItIsRemote:
+ _objc_msgSend$_showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:
+ _objc_msgSend$outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:
- -[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:]
- -[AVOutputContextManager outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:]
- -[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:forceCreate:]
- GCC_except_table117
- _AVContentKeySessionLegacyWebKitCompatibilityMode
- ___108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.152
- ___114-[AVPlayer(AVPlayerInterstitialSupport_Internal) _copyInterstitialEventCoordinatorEnsuringItIsRemote:forceCreate:]_block_invoke
- ___block_descriptor_58_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- ___block_literal_global.331
- ___block_literal_global.369
- ___block_literal_global.387
- __unnamed_array_storage.509
- __unnamed_array_storage.515
- _objc_msgSend$_copyInterstitialEventCoordinatorEnsuringItIsRemote:forceCreate:
- _objc_msgSend$_showErrorPromptForRouteDescriptor:reason:
- _objc_msgSend$outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:
CStrings:
+ "-[AVOutputContextManager outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:]"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@ with outputDevice: %{private}@ failureReason: %{public}@ didFailToConnectToOutputDeviceDictionary: %{private}@"
+ "AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextManagerDidFailToConnectToOutputDeviceUserInfoKey"
+ "AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey"
+ "AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo"
+ "Expected a NSDictionary for didFailToConnectToOutputDeviceUserInfo"
+ "Value at index 0 for kVTCompressionPropertyKey_MVHEVCVideoLayerIDs is not 0"
+ "Values for kVTCompressionPropertyKey_MVHEVCVideoLayerIDs are invalid"
+ "^{OpaqueFigPlayerInterstitialCoordinator=}20@0:8B16"
+ "_copyInterstitialEventCoordinatorEnsuringItIsRemote:"
+ "_showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:"
+ "description=AVFoundation_AVFCore-2215.13.4"
+ "echoedDictionary"
+ "en"
+ "outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:"
+ "showErrorPromptDictionaryToEcho"
+ "v40@0:8^{__CFDictionary=}16^{__CFString=}24^{__CFDictionary=}32"
- "-[AVOutputContextManager outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:]"
- "<<<< AVOutputContext >>>> %s: Posting %{public}@ with outputDevice: %{private}@ failureReason: %{public}@"
- "AVContentKeySessionLegacyWebKitCompatibilityMode"
- "^{OpaqueFigPlayerInterstitialCoordinator=}24@0:8B16B20"
- "_copyInterstitialEventCoordinatorEnsuringItIsRemote:forceCreate:"
- "_showErrorPromptForRouteDescriptor:reason:"
- "description=AVFoundation_AVFCore-2180.79.1.1.1"
- "outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:"
- "v32@0:8^{__CFDictionary=}16^{__CFString=}24"

```
