## navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

-2905.30.6.20.7
-  __TEXT.__text: 0x3ac6c
+2908.30.7.7.8
+  __TEXT.__text: 0x3c178
   __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_stubs: 0x7780
-  __TEXT.__objc_methlist: 0x23c8
+  __TEXT.__objc_stubs: 0x7880
+  __TEXT.__objc_methlist: 0x2490
   __TEXT.__const: 0x228
-  __TEXT.__gcc_except_tab: 0x4650
-  __TEXT.__cstring: 0x4211
-  __TEXT.__objc_methname: 0x8103
-  __TEXT.__objc_classname: 0x904
-  __TEXT.__objc_methtype: 0x1d97
-  __TEXT.__oslogstring: 0x4cab
-  __TEXT.__unwind_info: 0x1190
+  __TEXT.__gcc_except_tab: 0x46e8
+  __TEXT.__cstring: 0x4454
+  __TEXT.__objc_methname: 0x82e2
+  __TEXT.__objc_classname: 0x9a3
+  __TEXT.__objc_methtype: 0x1ec1
+  __TEXT.__oslogstring: 0x4f69
+  __TEXT.__unwind_info: 0x11e8
   __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__got: 0x790
   __DATA_CONST.__const: 0x2c58
-  __DATA_CONST.__cfstring: 0x2620
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__cfstring: 0x2640
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_intobj: 0xa38
   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x470
   __DATA_CONST.__objc_floatobj: 0x50
-  __DATA.__objc_const: 0x50b0
-  __DATA.__objc_selrefs: 0x21f8
-  __DATA.__objc_ivar: 0x3a4
-  __DATA.__objc_data: 0xff0
-  __DATA.__data: 0xc40
+  __DATA.__objc_const: 0x5498
+  __DATA.__objc_selrefs: 0x2248
+  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_data: 0x1090
+  __DATA.__data: 0xd00
   __DATA.__bss: 0x198
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3721836-207C-3BD7-AE83-C0377CA48A73
-  Functions: 966
-  Symbols:   428
-  CStrings:  2878
+  UUID: 976BAD9F-A130-3FBC-AFE3-2DA8FFD69591
+  Functions: 984
+  Symbols:   431
+  CStrings:  2927
 
Symbols:
+ _GEOConfigMapsSuggestionsDurationBetweenDOoMWidgetNudges
+ _OBJC_CLASS_$_MNFamiliarRouteAuthorizationChecker
+ _OBJC_CLASS_$_MapsSuggestionsDOoMEngineWrapper
CStrings:
+ "%.0f mins has not passed since the last widget nudge. Ignoring request for a Widget refresh"
+ "-[MapsSuggestionsCommuteWindowServer listener:shouldAcceptNewConnection:]"
+ "-[MapsSuggestionsCommuteWindowServer listener:shouldAcceptNewConnection:]_block_invoke_2"
+ "-[MapsSuggestionsCommuteWindowXPCPeer commuteStatusFromDOoMEngine:]"
+ "-[NavdDoomHost initFromResourceDepot:sharedRegister:engine:]"
+ "-[NavdMapsSuggestionsController startDoomIfNotStarted]"
+ "/Library/Caches/com.apple.xbs/Sources/Maps/iOS/Suggestions/DOoM & Location Intelligence/MapsSuggestionsCommuteWindowServer.m"
+ "@\"<MapsSuggestionsFullResourceDepot>\""
+ "@\"MapsSuggestionsCommuteWindowServer\""
+ "@\"MapsSuggestionsDOoMEngineWrapper\""
+ "@48@0:8@16@24@32@40"
+ "At %{public}s:%d, %{public}s forbids: %{public}s. Requires a non-nill handler"
+ "At %{public}s:%d, %{public}s forbids: %{public}s. This method should be called only after _doomEngineWrapper is instantiated"
+ "Commute Window Server Listener created and resumed."
+ "CommuteWindowServer"
+ "CommuteWindowXPCPeer{%@} Received isDeviceInCommuteWindow()..."
+ "CommuteWindowXPCPeer{%@} created."
+ "CommuteWindowXPCPeer{%@} destroyed."
+ "CommuteWindowXPCXPCPeer{%@} destroying..."
+ "DOoM"
+ "Device __IS__ eligible to run DOoM. OS Eligibility says so. Checking more conditions."
+ "Device is NOT eligible to run DOoM. OS Eligibility says so."
+ "MapsSuggestionsCommuteWindowProxy"
+ "MapsSuggestionsCommuteWindowServer"
+ "MapsSuggestionsCommuteWindowServerQueue"
+ "MapsSuggestionsCommuteWindowXPCPeer"
+ "MapsSuggestionsCommuteWindowXPCPeerQueue"
+ "MapsSuggestionsDOoMEngineWrapperStatusUpdateDelegate"
+ "T@\"NSXPCConnection\",R,N,V_connection"
+ "XPC connection %@ was interrupted"
+ "_commuteWindowServer"
+ "_doomEngineWrapper"
+ "_doomEngineWrapper == nil"
+ "_handlerCopy"
+ "_lastNudge"
+ "_minDurationBetweenWidgetNudges"
+ "com.apple.navd.commutewindow"
+ "commuteStatusFromDOoMEngine:"
+ "commuteWindowIs:forNextDestination:travelTime:"
+ "getCurrentCommuteStatus"
+ "initFromResourceDepot:sharedRegister:engine:"
+ "initWithResourceDepot:conditions:"
+ "initWithResourceDepot:conditions:engine:"
+ "initWithResourceDepot:triggers:conditions:engine:"
+ "initWithXPCConnection:resourceDepot:conditions:doomEngine:"
+ "isEligible"
+ "setInterruptionHandler:"
+ "setStatusUpdateDelegate:"
+ "v24@0:8@?<v@?@\"NSDateInterval\"@\"MapsSuggestionsLocationOfInterest\"d@\"NSError\">16"
+ "v40@0:8@\"NSDateInterval\"16@\"MapsSuggestionsLocationOfInterest\"24d32"
+ "v40@0:8@16@24d32"
- "\t"
- "-[NavdDoomHost initFromResourceDepot:sharedRegister:]"
- "initWithResourceDepot:triggers:conditions:"

```
