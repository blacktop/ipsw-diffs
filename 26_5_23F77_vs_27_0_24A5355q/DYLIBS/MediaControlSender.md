## MediaControlSender

> `/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x56d00
-  __TEXT.__auth_stubs: 0xd20
+980.58.1.11.1
+  __TEXT.__text: 0x62724
   __TEXT.__objc_methlist: 0x1f8
-  __TEXT.__const: 0xf880
+  __TEXT.__const: 0x5690
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x3c0e
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__cstring: 0x3c14
+  __TEXT.__unwind_info: 0x3f0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x673
-  __TEXT.__objc_methtype: 0x230
-  __TEXT.__objc_stubs: 0x4c0
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__const: 0x2bc8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x2cb0
   __AUTH_CONST.__cfstring: 0xec0
   __AUTH_CONST.__objc_const: 0x288
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x166e0
-  __DATA.__bss: 0x7c
+  __DATA.__data: 0x167f0
+  __DATA.__bss: 0x80
   __DATA.__common: 0xa04
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
-  - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DF39B59-C8CD-343B-AFB5-DEC704061E2E
-  Functions: 248
+  UUID: C7531F15-97EB-3B8A-91C1-43784FFB1664
+  Functions: 263
   Symbols:   707
-  CStrings:  713
+  CStrings:  619
 
Symbols:
+ _objc_msgSend$sharedInstance
- _objc_msgSend$sharedAVSystemController
CStrings:
+ "980.58.1.11.1"
- "950.7.1"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@40@0:8@\"NSString\"16@24^i32"
- "@40@0:8@16@24^i32"
- "@?"
- "AirPlayControllerAsync"
- "AirPlayControllerSync"
- "T@\"NSString\",C,N,V_xpcName"
- "UTF8String"
- "^{MediaControlClientImp=}"
- "_client"
- "_cnx"
- "_eventHandlerBlock"
- "_eventHandlerQueue"
- "_queue"
- "_setupConnection"
- "_xpcName"
- "arrayWithObjects:count:"
- "attributeForKey:"
- "boolValue"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "ensureConnected"
- "ensureDisconnected"
- "getProperty:qualifier:completion:"
- "getProperty:qualifier:completionQueue:completionBlock:"
- "getProperty:qualifier:status:"
- "getSlideshowFeaturesWithOptions:completionQueue:completionBlock:"
- "getSlideshowInfoWithOptions:completionQueue:completionBlock:"
- "i40@0:8@\"NSString\"16@24@32"
- "i40@0:8@16@24@32"
- "i48@0:8@\"NSString\"16@24@32^@40"
- "i48@0:8@16@24@32^@40"
- "init"
- "initWithDomain:code:userInfo:"
- "initWithMachServiceName:options:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isAirPlayOutgoingRequestsPairingPasswordRequired"
- "isEqual:"
- "length"
- "mainBundle"
- "null"
- "numberWithBool:"
- "objectAtIndex:"
- "objectForKey:"
- "performCommand:qualifier:params:completion:"
- "performCommand:qualifier:params:response:"
- "performRemoteAction:withParams:completionQueue:completionBlock:"
- "postEvent:qualifier:params:"
- "postEvent:qualifier:params:completion:"
- "preferredLocalizations"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "sendPhotoData:completionQueue:completionBlock:"
- "sendPhotoData:options:completionQueue:completionBlock:"
- "setAttribute:forKey:error:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setEventHandlerQueue:eventHandlerBlock:"
- "setHost:"
- "setPassword:"
- "setPickedRouteWithPassword:withPassword:"
- "setProperty:qualifier:value:"
- "setProperty:qualifier:value:completion:"
- "setProperty:qualifier:value:completionQueue:completionBlock:"
- "setRemoteObjectInterface:"
- "setSlideshowInfo:completionQueue:completionBlock:"
- "setWithArray:"
- "setXpcName:"
- "sharedAVSystemController"
- "sharedConnection"
- "startPresentation:completionQueue:completionBlock:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v36@0:8I16@20@?28"
- "v40@0:8@\"NSString\"16@24@32"
- "v40@0:8@\"NSString\"16@24@?<v@?i@>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSString\"16@24@32@?<v@?>40"
- "v48@0:8@\"NSString\"16@24@32@?<v@?i>40"
- "v48@0:8@\"NSString\"16@24@32@?<v@?i@\"NSDictionary\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "xpcName"

```
