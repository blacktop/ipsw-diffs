## SensorKitHelper

> `/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper`

```diff

-972.0.21.0.0
-  __TEXT.__text: 0x3b8c
-  __TEXT.__auth_stubs: 0x2c0
+1025.0.0.0.0
+  __TEXT.__text: 0x3978
   __TEXT.__objc_methlist: 0x308
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x2c8
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__cstring: 0x2c9
   __TEXT.__oslogstring: 0x470
   __TEXT.__dlopen_cstrs: 0x82
-  __TEXT.__unwind_info: 0x178
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methname: 0xa9c
-  __TEXT.__objc_methtype: 0x26f
-  __TEXT.__objc_stubs: 0xb60
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x4e8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E90BA749-9E93-37CA-BD37-882A45107583
+  UUID: 3BFF8B38-BEA8-3EFC-91BE-D7E075D3D8A1
   Functions: 77
   Symbols:   394
-  CStrings:  234
+  CStrings:  70
 
CStrings:
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"SRHMediaViewsStore\""
- "@\"UIScrollView\""
- "@\"UIScrollViewMonitor\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "SKMediaEventsHelperProtocol"
- "SRHMediaView"
- "SensorKit"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_q"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,R,N"
- "TB,V_connectionDidInvalidate"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_position"
- "UIBackgroundModes"
- "UIScrollViewMonitorDelegate"
- "UUID"
- "UUIDString"
- "_addMediaSubviewsOfView:"
- "_addMediaSubviewsOfView:viewsTraversed:"
- "_checkViewForMediaContent:withCompletionHandler:"
- "_connection"
- "_connectionDidInvalidate"
- "_mediaViewsStore"
- "_offScreenMediaViews"
- "_onScreenMediaViews"
- "_position"
- "_q"
- "_removeMediaSubviewsOfView:"
- "_removeMediaSubviewsOfView:viewsTraversed:"
- "_scrollView"
- "_scrollViewMonitor"
- "_setQueue:"
- "_uuid"
- "_writeMediaEventsToBiome:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addViewToStore:"
- "adjustedContentInset"
- "appTags"
- "applicationExtensionRecords"
- "applicationState"
- "authorizationRequestStatusForMediaEventsStreamWithReply:"
- "boolValue"
- "bounds"
- "builtInPlugInsURL"
- "bundleIdentifier"
- "bundleRecordForCurrentProcess"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "bundleWithURL:"
- "connection"
- "connectionDidInvalidate"
- "containingBundleRecord"
- "containsObject:"
- "contentView"
- "convertPoint:toView:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultCenter"
- "defaultManager"
- "description"
- "dictionaryWithDictionary:"
- "didBecomeActive"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "genre"
- "genreIdentifier"
- "iTunesMetadata"
- "image"
- "imageAsset"
- "infoDictionary"
- "init"
- "initWithScrollView:"
- "initWithScrollView:scrollMonitor:"
- "initWithScrollView:scrollMonitor:mediaViewsStore:"
- "initWithServiceName:"
- "initialize"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "isHidden"
- "isMediaEventsCollectionEnabledFor:completionHandler:"
- "isMediaEventsStreamAuthorizedWithCompletionHandler:"
- "isMessagingApp:"
- "isSocialMediaApp"
- "keyEnumerator"
- "mainBundle"
- "markViewsAsOffScreen"
- "markViewsAsOnScreen"
- "numberWithBool:"
- "objectForKey:"
- "objectForKey:ofClass:"
- "objectForKey:ofClass:valuesOfClass:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "position"
- "processScrollViewOffset"
- "q"
- "q32@0:8@16q24"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeAllViews"
- "removeObjectForKey:"
- "removeObserver:"
- "removeViewFromStore:"
- "resume"
- "scrollViewMonitorDidStartMonitoring:"
- "scrollViewMonitorDidStopMonitoring:"
- "scrollViewMonitorScrollDid:addView:removeView:"
- "scrollViewMonitorScrollDidScrolled:"
- "scrollViewVisibleArea"
- "setConnection:"
- "setConnectionDidInvalidate:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPosition:"
- "setQ:"
- "setRemoteObjectInterface:"
- "setUuid:"
- "setupConnection"
- "sharedApplication"
- "sr_bundleRecordWithIdentifier:error:"
- "sr_isSocialNetworking"
- "sr_supportsDataGeneration"
- "sr_supportsMessagingIntents"
- "sr_supportsVOIP"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "subviews"
- "superview"
- "supportedIntents"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSDictionary\"16d24@?<v@?@\"NSError\">32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24@\"UIView\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16d24@?32"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "weakToStrongObjectsMapTable"
- "willResignActive"
- "writeMediaEvents:withTimestamp:reply:"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
