## AdPlatformsCommon

> `/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon`

```diff

-485.0.0.0.0
-  __TEXT.__text: 0x9730
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x195c
+500.2.0.0.0
+  __TEXT.__text: 0xbd0c
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x1c64
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x126d
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__oslogstring: 0x440
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0x2ba
-  __TEXT.__objc_methname: 0x3afd
-  __TEXT.__objc_methtype: 0x64e
-  __TEXT.__objc_stubs: 0x20c0
+  __TEXT.__cstring: 0x131f
+  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__oslogstring: 0x5fc
+  __TEXT.__unwind_info: 0x400
+  __TEXT.__objc_classname: 0x375
+  __TEXT.__objc_methname: 0x40c1
+  __TEXT.__objc_methtype: 0x800
+  __TEXT.__objc_stubs: 0x2460
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2d90
-  __DATA_CONST.__objc_selrefs: 0xd88
-  __AUTH_CONST.__cfstring: 0x15e0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__objc_const: 0x3380
+  __DATA_CONST.__objc_selrefs: 0xea0
+  __AUTH_CONST.__cfstring: 0x1660
+  __AUTH_CONST.__objc_const: 0x1f8
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0x200
+  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x2b8
-  __DATA.__data: 0x300
-  __DATA_DIRTY.__const: 0xc0
+  __DATA.__objc_classrefs: 0x158
+  __DATA.__objc_superrefs: 0xc0
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x10
+  __DATA.__common: 0x1
+  __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__objc_const: 0xca8
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/APFoundation.framework/APFoundation
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A9BEA4A-AD54-3305-B4E2-BD0E3D0B816E
-  Functions: 523
-  Symbols:   150
-  CStrings:  1298
+  UUID: A762117A-7515-340D-A78F-3490A01F79FC
+  Functions: 591
+  Symbols:   167
+  CStrings:  1398
 
Symbols:
+ _OBJC_CLASS_$_APAdRequestContents
+ _OBJC_CLASS_$_APCoordinatedAdRequestBox
+ _OBJC_CLASS_$_APCoordinatedProxyUrlRequestBox
+ _OBJC_CLASS_$_APCoordinatedRankRequestBox
+ _OBJC_CLASS_$_APCoordinatedRetryBox
+ _OBJC_CLASS_$_APRequestCoordinator
+ _OBJC_METACLASS_$_APAdRequestContents
+ _OBJC_METACLASS_$_APCoordinatedAdRequestBox
+ _OBJC_METACLASS_$_APCoordinatedProxyUrlRequestBox
+ _OBJC_METACLASS_$_APCoordinatedRankRequestBox
+ _OBJC_METACLASS_$_APCoordinatedRetryBox
+ _OBJC_METACLASS_$_APRequestCoordinator
+ _gProxyIsRunning
+ _objc_opt_respondsToSelector
+ _objc_release_x28
+ _objc_retain_x6
+ _objc_storeWeak
CStrings:
+ "\x02\x11"
+ "\x11"
+ "2"
+ "@\"<APRequestCoordinatorDelegate>\""
+ "@\"APAdRequestContents\""
+ "@\"APClientInfo\""
+ "@\"APContext\""
+ "@32@0:8@16@?24"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16@24@?32"
+ "@48@0:8@16@24Q32@?40"
+ "APAdRequestContents"
+ "APCoordinatedAdRequestBox"
+ "APCoordinatedProxyUrlRequestBox"
+ "APCoordinatedRankRequestBox"
+ "APCoordinatedRetryBox"
+ "APRequestCoordinator"
+ "APRequestCoordinator was invalidated."
+ "APRequesterCoordinatorProtocol"
+ "Creating representation with APPlacementTypeApp"
+ "Received error during prewarming. %@"
+ "Received promoted contents: %lu"
+ "Requesting ad from promotedcontentd for context %{public}@"
+ "Retry failed request again."
+ "T@\"<APRequestCoordinatorDelegate>\",R,W,N,V_requestDelegate"
+ "T@\"APAdRequestContents\",R,N,V_requestContents"
+ "T@\"APClientInfo\",R,N,V_clientInfo"
+ "T@\"APContext\",R,N,V_apContext"
+ "T@\"APContext\",R,N,V_context"
+ "T@\"NSArray\",R,N,V_contentDatas"
+ "T@\"NSArray\",R,N,V_contentTypes"
+ "T@\"NSMutableDictionary\",&,N,V_managerToRetryBoxMap"
+ "T@\"NSUUID\",R,N,V_requestID"
+ "T@\"NSUUID\",R,N,V_requesterID"
+ "T@?,R,N,V_completionHandler"
+ "TB,R,N,V_deliverEntireBatch"
+ "TB,V_canRetry"
+ "TQ,R,N,V_placement"
+ "The user asked to invalidate the requester, or connection was interrupted."
+ "Tq,R,N,V_requestType"
+ "XPC Connection interrupted"
+ "[%{private}@] Request %{public}@ of type %{public}ld is attempting to retry for requester %{public}@"
+ "[%{private}@] The requester for %{public}@ is no longer stored. Dropping response."
+ "[%{private}@] Unable to retry request %{public}@ of type %{public}ld for requester %{public}@"
+ "_addBox:"
+ "_apContext"
+ "_canRetry"
+ "_clientInfo"
+ "_completionHandler"
+ "_contentDatas"
+ "_contentTypes"
+ "_context"
+ "_deliverEntireBatch"
+ "_managerToRetryBoxMap"
+ "_removeBox:"
+ "_requestContents"
+ "_requestDelegate"
+ "_requestID"
+ "_requestType"
+ "apContext"
+ "arrayWithObject:"
+ "attemptRetryMessageForBox:"
+ "beginSessionForID:"
+ "canRetry"
+ "clientInfo"
+ "completionHandler"
+ "connectionSeveredForBox:"
+ "connectionSeveredWithError:"
+ "containsObject:"
+ "contentDatas"
+ "contentTypes"
+ "context"
+ "deliverEntireBatch"
+ "firstObject"
+ "initWithContext:contentTypes:deliverEntireBatch:"
+ "initWithDelegate:contents:handler:"
+ "initWithDelegate:contents:placement:handler:"
+ "initWithDelegate:handler:"
+ "initWithType:delegate:"
+ "managerToRetryBoxMap"
+ "requestContents"
+ "requestDelegate"
+ "requestID"
+ "requestPromotedContentOfTypes:forRequester:forContext:withClientInfo:deliverEntireBatch:completionHandler:"
+ "requestPromotedContentWithBox:"
+ "requestPromotedContentWithContents:forRequester:completionHandler:"
+ "requestProxyWithBox:"
+ "requestRankingWithBox:"
+ "requestType"
+ "sendAndRankContent:forRequester:forContext:placement:completionHandler:"
+ "setCanRetry:"
+ "setManagerToRetryBoxMap:"
+ "sharedCoordinator"
+ "v32@0:8@\"NSDictionary\"16@\"<APRequestCoordinatorDelegate>\"24"
+ "v40@0:8@\"APAdRequestContents\"16@\"<APRequestCoordinatorDelegate>\"24@?<v@?@\"NSError\">32"
+ "v56@0:8@\"NSArray\"16@\"<APRequestCoordinatorDelegate>\"24@\"APContext\"32Q40@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8@16@24@32Q40@?48"
+ "v60@0:8@\"NSArray\"16@\"NSUUID\"24@\"APContext\"32@\"APClientInfo\"40B48@?<v@?>52"
+ "v60@0:8@16@24@32@40B48@?52"
- "requestPromotedContentOfTypes:forRequester:forContext:withClientInfo:completionHandler:"
- "v56@0:8@\"NSArray\"16@\"NSUUID\"24@\"APContext\"32@\"APClientInfo\"40@?<v@?>48"
- "v56@0:8@16@24@32@40@?48"

```
