## AirPlaySenderUIApp

> `/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp`

```diff

-755.3.1.0.0
-  __TEXT.__text: 0xaedc
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x1e40
-  __TEXT.__objc_methlist: 0x704
+760.20.1.0.0
+  __TEXT.__text: 0xad2c
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x1dc0
+  __TEXT.__objc_methlist: 0x6f0
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x1a0
-  __TEXT.__cstring: 0x34a7
-  __TEXT.__objc_methname: 0x2ef5
+  __TEXT.__cstring: 0x32e2
+  __TEXT.__objc_methname: 0x2eb9
   __TEXT.__objc_classname: 0x1a2
   __TEXT.__objc_methtype: 0xe26
-  __TEXT.__unwind_info: 0x2b4
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x618
-  __DATA_CONST.__cfstring: 0x9e0
+  __TEXT.__unwind_info: 0x2b0
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x5c8
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x1d08
-  __DATA.__objc_selrefs: 0x8b0
-  __DATA.__objc_classrefs: 0x190
-  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_selrefs: 0x898
   __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x670

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2464F84A-B7F9-381C-98DC-57D24E8CCCF8
-  Functions: 192
-  Symbols:   163
-  CStrings:  935
+  UUID: 528FD002-99EE-303B-B8C9-2DF09F9A5B0B
+  Functions: 189
+  Symbols:   167
+  CStrings:  932
 
Symbols:
+ _APSRemoteConfigGetBooleanIfPresent
+ _APSRemoteConfigGetShared
+ _AVOutputContextDestinationChangeCancellationReasonAuthorizationSkipped
+ _kAPSRemoteConfigKey_AirPlaySetupAssistantAndBrokeredDiscovery
CStrings:
+ "%s %s"
+ "-[SceneDelegate _setupAssistantEnabled]"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIWindow\",?,&,N"
+ "[%{ptr}] Showing invalid code alert as AirPlay receiver token %@ has expired"
+ "[%{ptr}] Showing invalid code alert as broker token %@ is invalid"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: current network (%@) is not the same as network in payload, try to connect to WiFi"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: current network (%@) is the same as network in payload, try broker authentication"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: proactively try broker authentication on current network (%@)"
+ "_setupAssistantEnabled"
+ "disabled"
+ "enabled"
+ "locally"
+ "remotely"
+ "setBlueAtlasNetwork:"
- "-[APUISetupViewController _getSupportedNetworks:withSetupPayload:completion:]_block_invoke"
- "-[APUISetupViewController _presentAirPlayConnectionProxCardWithSetupPayload:]_block_invoke_2"
- "T@\"UIWindow\",&,N"
- "[%{ptr}] Failed to get brokerGroupInfo with error: %@"
- "[%{ptr}] Successfully obtained brokerGroupInfo: %@"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is enabled. Current network (%@) is not supported and is not the same network in payload, try to connect to WiFi."
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is enabled. Current network (%@) is supported, try broker authentication."
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is not enabled. Current network (%@) is not the same as network in payload, try to connect to WiFi"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is not enabled. Current network (%@) is the same as network in payload, try broker authentication"
- "_getSupportedNetworks:withSetupPayload:completion:"
- "allKeys"
- "containsObject:"
- "isMultipleWifiFeatureEnabled"
- "setPublicAirPlayNetwork:"
- "supportedWiFiNetworkSSIDs"
- "v12@?0B8"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"

```
