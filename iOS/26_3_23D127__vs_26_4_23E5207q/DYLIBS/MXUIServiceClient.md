## MXUIServiceClient

> `/System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient`

```diff

-315.6.1.0.0
-  __TEXT.__text: 0x1d5c
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_methlist: 0x294
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x390
-  __TEXT.__oslogstring: 0x14b
-  __TEXT.__unwind_info: 0xd8
+320.18.1.0.0
+  __TEXT.__text: 0x2558
+  __TEXT.__auth_stubs: 0x190
+  __TEXT.__objc_methlist: 0x2e4
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x485
+  __TEXT.__oslogstring: 0x1bd
+  __TEXT.__unwind_info: 0xf0
   __TEXT.__objc_classname: 0xba
-  __TEXT.__objc_methname: 0x688
-  __TEXT.__objc_methtype: 0x31e
-  __TEXT.__objc_stubs: 0x540
+  __TEXT.__objc_methname: 0x7bb
+  __TEXT.__objc_methtype: 0x3a8
+  __TEXT.__objc_stubs: 0x5c0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x248
+  __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x868
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x8b8
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x180
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6059F4FA-C5A0-3392-8B75-35E2B2887793
-  Functions: 50
-  Symbols:   273
-  CStrings:  176
+  UUID: 5DD70E67-617D-3B1D-A499-7E038416C53E
+  Functions: 74
+  Symbols:   329
+  CStrings:  196
 
Symbols:
+ -[MXUIService_Client copyCarPlayVideoBannerParameters:routeToCar:]
+ -[MXUIService_Client promptForCarPlayVideoBanner:routeToCar:callbackHandler:]
+ -[MXUIService_Client updateSTBackgroundActivitiesStatusPill:showOrRemove:callbackHandler:]
+ -[MXUIService_ServerDelegate showCarPlayVideoBanner:completionHandler:]
+ -[MXUIService_ServerDelegate updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:]
+ _MXUIService_BackgroundActivityIdentifierCarPlayVideo
+ _MXUIService_CommonButtonParam_RouteToCar
+ _NSLog
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ ___100-[MXUIService_ServerDelegate updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:]_block_invoke
+ ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.85
+ ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.86
+ ___71-[MXUIService_ServerDelegate showCarPlayVideoBanner:completionHandler:]_block_invoke
+ ___77-[MXUIService_Client promptForCarPlayVideoBanner:routeToCar:callbackHandler:]_block_invoke
+ ___90-[MXUIService_Client updateSTBackgroundActivitiesStatusPill:showOrRemove:callbackHandler:]_block_invoke
+ ___block_literal_global.64
+ ___block_literal_global.84
+ _objc_msgSend$copyCarPlayVideoBannerParameters:routeToCar:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$showCarPlayVideoBanner:completionHandler:
+ _objc_msgSend$updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:
+ _objc_release_x20
- ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.81
- ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.82
- ___block_literal_global.60
- ___block_literal_global.80
CStrings:
+ "-MXUIServiceClient- %s: Showing STBackgroundActivityStatus pill (activityIdentifier='%{public}@', yesToShow='%d')"
+ "-[MXUIService_Client copyCarPlayVideoBannerParameters:routeToCar:]"
+ "-[MXUIService_Client updateSTBackgroundActivitiesStatusPill:showOrRemove:callbackHandler:]"
+ "@28@0:8@16B24"
+ "@36@0:8@16B24@?28"
+ "Received action %d\n"
+ "RouteToCar"
+ "Vv40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "com.apple.systemstatus.background-activity.carplayvideo"
+ "copyCarPlayVideoBannerParameters:routeToCar:"
+ "numberWithUnsignedChar:"
+ "promptForCarPlayVideoBanner:routeToCar:callbackHandler:"
+ "showCarPlayVideoBanner:completionHandler:"
+ "updateSTBackgroundActivitiesStatusPill:showOrRemove:callbackHandler:"
+ "updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:"
+ "v36@0:8@16C24@?28"

```
