## AirPlaySenderUIApp

> `/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp`

```diff

-760.20.1.0.0
-  __TEXT.__text: 0xad2c
+770.8.1.0.0
+  __TEXT.__text: 0xb20c
   __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0x6f0
+  __TEXT.__objc_stubs: 0x1e60
+  __TEXT.__objc_methlist: 0x710
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x1a0
-  __TEXT.__cstring: 0x32e2
-  __TEXT.__objc_methname: 0x2eb9
+  __TEXT.__cstring: 0x358e
+  __TEXT.__objc_methname: 0x2f29
   __TEXT.__objc_classname: 0x1a2
-  __TEXT.__objc_methtype: 0xe26
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_methtype: 0xe3b
+  __TEXT.__unwind_info: 0x2b8
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x5c8
-  __DATA_CONST.__cfstring: 0x9c0
+  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__cfstring: 0x9e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x1d08
-  __DATA.__objc_selrefs: 0x898
+  __DATA.__objc_selrefs: 0x8b8
   __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x670

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FBE9D1B1-4863-31CC-A405-9E85D5CD7B9A
-  Functions: 189
+  UUID: 3D890B24-3867-3CFB-9D06-8B0C9C71FF54
+  Functions: 193
   Symbols:   167
-  CStrings:  932
+  CStrings:  946
 
CStrings:
+ "-[APUIBrokerHelper _sendBrokerRequest:params:timeout:completion:]_block_invoke"
+ "-[APUISetupViewController _getSupportedNetworks:withSetupPayload:completion:]_block_invoke"
+ "-[APUISetupViewController _presentAirPlayConnectionProxCardWithSetupPayload:]_block_invoke_2"
+ "[%{ptr}] Failed to get brokerGroupInfo with error: %@"
+ "[%{ptr}] Successfully obtained brokerGroupInfo: %@"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is enabled. Current network (%@) is not supported and is not the same network in payload, try to connect to WiFi."
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is enabled. Current network (%@) is supported, try broker authentication."
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is not enabled. Current network (%@) is not the same as network in payload, try to connect to WiFi"
+ "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: Multiple network feature is not enabled. Current network (%@) is the same as network in payload, try broker authentication"
+ "_getSupportedNetworks:withSetupPayload:completion:"
+ "_sendBrokerRequest:params:timeout:completion:"
+ "allKeys"
+ "containsObject:"
+ "isMultipleWifiFeatureEnabled"
+ "supportedWiFiNetworkSSIDs"
+ "v12@?0B8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v48@0:8@16@24Q32@?40"
- "-[APUIBrokerHelper _sendBrokerRequest:params:completion:]_block_invoke"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: current network (%@) is not the same as network in payload, try to connect to WiFi"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: current network (%@) is the same as network in payload, try broker authentication"
- "[%{ptr}] presentAirPlayConnectionProxCardWithSetupPayload: proactively try broker authentication on current network (%@)"
- "_sendBrokerRequest:params:completion:"

```
