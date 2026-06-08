## PromotedContentSupport

> `/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport`

```diff

-556.5.31.0.0
-  __TEXT.__text: 0x3e98
-  __TEXT.__auth_stubs: 0x2d0
+557.1.16.0.0
+  __TEXT.__text: 0x3b64
   __TEXT.__objc_methlist: 0x348
   __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x257
   __TEXT.__oslogstring: 0x414
-  __TEXT.__cstring: 0x252
   __TEXT.__gcc_except_tab: 0x140
   __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0xf7
-  __TEXT.__objc_methname: 0x85c
-  __TEXT.__objc_methtype: 0x272
-  __TEXT.__objc_stubs: 0x860
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x738
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12D598A6-3580-3039-A934-21704C49F4E5
+  UUID: 1F52F383-7B93-3689-A82A-D0E62A7E3388
   Functions: 86
-  Symbols:   101
-  CStrings:  194
+  Symbols:   105
+  CStrings:  60
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"APUnfairLock\""
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSUUID\""
- "@16@0:8"
- "@40@0:8@16@24q32"
- "APStatusConditions_XPC"
- "B16@0:8"
- "B32@0:8@16q24"
- "PCAdPolicyFormat"
- "PCConfiguration"
- "PCNewsSegmentation"
- "PCRingBuffer"
- "PCRuntimeParameters"
- "PCStatusConditionRateLimitedObject"
- "PCStatusConditions"
- "PCStatusConditionsImpl"
- "PCSupportDaemonInterface"
- "PCSupportRequester"
- "PCTestingRig"
- "T@\"APUnfairLock\",R,N,V_lock"
- "T@\"NSDate\",R,N,V_setTime"
- "T@\"NSMutableArray\",&,N,V_ringBuffer"
- "T@\"NSNumber\",R,N"
- "T@\"NSUUID\",R,N,V_statusCondition"
- "Tq,R,N,V_operation"
- "_classProperties"
- "_lock"
- "_operation"
- "_ringBuffer"
- "_setTime"
- "_setupXPCConnection"
- "_statusCondition"
- "_updateGenderAndAgeGroupValues"
- "addClientToSegments:replaceExisting:privateSegment:"
- "addObject:"
- "array"
- "canShareConnection"
- "cappedRingBufferTo:"
- "cleanupExpiredConditionsInBuffer"
- "clearStatusCondition:completionHandler:"
- "configurationForPath:"
- "connectionInterrupted"
- "connectionInvalidated"
- "contextPrefetchLimit"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "daemonDelivery"
- "daemonDeliveryClass"
- "date"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "fetchConfigurationForClass:completion:"
- "fetchGenderAndAgeGroupData"
- "fetchGenderAndAgeGroupData:"
- "filterUsingPredicate:"
- "finished"
- "init"
- "init:at:kind:"
- "initWithConfig:notifier:"
- "initWithMachServiceName:options:"
- "initWithOptions:"
- "initWithPurpose:metric:contentIdentifier:contextIdentifier:handle:secondaryHandle:branch:properties:internalProperties:relayData:environment:order:options:"
- "interfaceWithProtocol:"
- "invalidate"
- "invokeTestingRigHandlerForMessage:payload:completionHandler:"
- "isAppleInternalInstall"
- "isConditionRateLimited:onOperation:"
- "isEqual:"
- "isEqualToString:"
- "isStatusConditionRegistered:bundleIdentifier:completionHandler:"
- "lock"
- "machService"
- "metricClass"
- "mutableCopy"
- "now"
- "numberWithFloat:"
- "objectForKey:"
- "operation"
- "operationWithCondition:forType:"
- "path"
- "policiesForContainerType:adType:adFormatType:completion:"
- "policiesToEnforce:"
- "predicateWithBlock:"
- "q"
- "q16@0:8"
- "rateLimitRequests:"
- "rateLimitRequestsInFeed:inArticle:betweenArticle:videoInArticle:nativeInFeed:nativeInArticle:"
- "receivedMetric:"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "resume"
- "ringBuffer"
- "segmentData"
- "setConfiguration:"
- "setContextPrefetchLimit:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setRingBuffer:"
- "setStatusCondition:completionHandler:"
- "setTime"
- "setValue:forKey:"
- "sharedInstance"
- "sleepForTimeInterval:"
- "statusCondition"
- "subarrayWithRange:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceDate:"
- "unlock"
- "v16@0:8"
- "v20@0:8f16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8#16@?24"
- "v32@0:8@\"NSArray\"16B24B28"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSString\">32"
- "v40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8f16f20f24f28f32f36"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\">40"
- "v48@0:8@16@24@32@?40"

```
