## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-738.80.3.0.0
-  __TEXT.__text: 0x40980
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x36bc
-  __TEXT.__gcc_except_tab: 0x1620
+738.100.34.0.0
+  __TEXT.__text: 0x40f1c
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x3dfc
+  __TEXT.__gcc_except_tab: 0x1594
   __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x290b
-  __TEXT.__oslogstring: 0x303c
+  __TEXT.__cstring: 0x29a9
+  __TEXT.__oslogstring: 0x2f49
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0x13a0
-  __TEXT.__objc_classname: 0xaaf
-  __TEXT.__objc_methname: 0x7d6b
-  __TEXT.__objc_methtype: 0x1d00
-  __TEXT.__objc_stubs: 0x5f80
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__const: 0x1470
-  __DATA_CONST.__objc_classlist: 0x298
+  __TEXT.__unwind_info: 0x14a8
+  __TEXT.__objc_classname: 0xaba
+  __TEXT.__objc_methname: 0x7e7f
+  __TEXT.__objc_methtype: 0x1d30
+  __TEXT.__objc_stubs: 0x5f60
+  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__const: 0x14a0
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d90
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x1e70
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x8598
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__cfstring: 0x2360
+  __AUTH_CONST.__objc_const: 0x7ab8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x518
+  __DATA.__objc_ivar: 0x520
   __DATA.__data: 0xc08
   __DATA.__bss: 0x150
-  __DATA_DIRTY.__objc_data: 0x1950
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__objc_data: 0x19a0
+  __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1677
-  Symbols:   2164
-  CStrings:  2597
+  Functions: 1771
+  Symbols:   2259
+  CStrings:  2604
 
Symbols:
+ _OBJC_CLASS_$_TKCTKDConnection
+ _OBJC_METACLASS_$_TKCTKDConnection
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x02\x12\x13"
+ "%{public}@: Error when simulating card reinsertion: %@"
+ "%{public}@: Reinsertion simulation cancelled due to call rate limitation"
+ "%{public}@: Skipping simulated card reinsertion due to missing card"
+ "%{public}@: Started simulated card reinsertion"
+ "@\"NSDate\""
+ "@\"NSXPCInterface\""
+ "@\"TKCTKDConnection\""
+ "@\"TKCTKDConnection\"16@?0^@8"
+ "@24@?0@\"<TKClientTokenServerProtocol>\"8^@16"
+ "Card is missing"
+ "Missing TKSmartCardSlotEngineDelegate delegate"
+ "R\x19\"\x13"
+ "Reinsertion simulation is currently running or was run recently. Please wait at least %f seconds between the calls."
+ "T@\"NSXPCInterface\",&,N,V_exportedInterface"
+ "T@\"NSXPCListenerEndpoint\",R,N"
+ "T@\"TKCTKDConnection\",&,N"
+ "T@\"TKCTKDConnection\",R,N,V_ctkdConnection"
+ "T@,&,N,V_exportedObject"
+ "TKCTKDConnection"
+ "_cardReinsertionSimulationCallInterval"
+ "_connectionWithCTKDConnection:"
+ "_ctkdConnection"
+ "_exportedInterface"
+ "_exportedObject"
+ "_lastCardReinsertionSimulationCallTime"
+ "canSimulateCardReinsertion"
+ "ctkdConnection"
+ "date"
+ "distantPast"
+ "driverConfigurationsWithCTKDConnection:"
+ "engineSimulateCardReinsertion:"
+ "exportedInterface"
+ "exportedObject"
+ "initWithCTKDConnection:"
+ "initWithCTKDEndpoint:targetUID:"
+ "initWithTokenID:ctkdConnection:"
+ "invoke on token-client connection failed with connection error %{public}@"
+ "setCardReinsertionSimulationCallInterval:"
+ "setCtkdConnection:"
+ "simulateCardReinsertionWithError:"
+ "simulateCardReinsertionWithReply:"
+ "timeIntervalSinceDate:"
+ "v16@?0@\"TKCTKDConnection\"8"
+ "\xf0a1"
- "\x02\x11\x11"
- "\x02\x12\x12"
- "\x15"
- "@\"NSXPCConnection\"16@?0^@8"
- "@\"NSXPCListenerEndpoint\"24@?0@\"<TKClientTokenServerProtocol>\"8^@16"
- "A\x19\"\x13"
- "Failed to get TKTokenWatcher endpoint, watcher will be mute."
- "Failed to get connection for tokenID=%{public}@ (error %{public}@)"
- "SEPKeyEndpoint"
- "T@\"NSXPCListenerEndpoint\",R"
- "T@\"NSXPCListenerEndpoint\",R,N,V_SEPKeyEndpoint"
- "T@\"NSXPCListenerEndpoint\",R,N,V_endpoint"
- "T@\"NSXPCListenerEndpoint\",R,N,V_watcherEndpoint"
- "T@\"TKClientToken\",&,N"
- "T@\"TKClientToken\",R,N,V_client"
- "_SEPKeyEndpoint"
- "_client"
- "_connectionWithClient:"
- "_watcherEndpoint"
- "clientToken"
- "connection to the watcher endpoint invalidated/interrupted!"
- "creating rsepkey xpc connection"
- "detected interruption on token-client connection, retrying %d"
- "failed to call remotesepkey repeatedly, giving up, error: %{public}@"
- "failed to call remotesepkey, try %d, error %{public}@"
- "failed to register TKTokenWatcher, error %{public}@"
- "get*Endpoint on token-client connection failed with connection error %{public}@"
- "getSEPKeyEndpoint:"
- "getWatcherEndpoint:"
- "initWithClient:"
- "invalidationHandler"
- "setClientToken:"
- "unable to get endpoint"
- "v16@?0@\"NSXPCConnection\"8"
- "watcherEndpoint"
- "withError:getServerEndpoint:"
- "\xf0A1"

```
