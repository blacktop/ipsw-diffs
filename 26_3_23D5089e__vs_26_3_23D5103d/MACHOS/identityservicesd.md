## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1968.400.1.0.0
-  __TEXT.__text: 0x940c94
+1968.400.11.0.0
+  __TEXT.__text: 0x941404
   __TEXT.__auth_stubs: 0x5ba0
-  __TEXT.__objc_stubs: 0x46cc0
-  __TEXT.__objc_methlist: 0x2992c
+  __TEXT.__objc_stubs: 0x46ce0
+  __TEXT.__objc_methlist: 0x2993c
   __TEXT.__const: 0x64ef0
   __TEXT.__gcc_except_tab: 0x29f10
-  __TEXT.__objc_methname: 0x7395d
-  __TEXT.__cstring: 0x59c47
-  __TEXT.__oslogstring: 0x7b45b
+  __TEXT.__objc_methname: 0x739ae
+  __TEXT.__cstring: 0x59cc7
+  __TEXT.__oslogstring: 0x7b49b
   __TEXT.__objc_classname: 0x440c
-  __TEXT.__objc_methtype: 0x1255b
+  __TEXT.__objc_methtype: 0x125b5
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__swift5_typeref: 0x60b2

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x48438
-  __DATA.__objc_selrefs: 0x15f80
+  __DATA.__objc_selrefs: 0x15f88
   __DATA.__objc_ivar: 0x32bc
   __DATA.__objc_data: 0xd788
-  __DATA.__data: 0xec30
+  __DATA.__data: 0xec60
   __DATA.__bss: 0x17158
   __DATA.__common: 0xf38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F752739E-E2DB-3786-A702-BF15EF250742
-  Functions: 25448
+  UUID: 2B320A72-FFB1-3D57-A36B-F197A3B1D283
+  Functions: 25450
   Symbols:   2757
-  CStrings:  41649
+  CStrings:  41655
 
CStrings:
+ "19:56:59"
+ "B72@0:8@\"NSArray\"16@\"NSData\"24@\"IDSURI\"32@\"NSString\"40@\"IDSPeerIDQueryContext\"48@\"NSString\"56@?<v@?@\"IDSURI\"@\"NSArray\"@\"NSArray\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B@\"NSUUID\">64"
+ "B72@0:8@\"NSArray\"16@\"NSData\"24@\"IDSURI\"32@\"NSString\"40@\"IDSPeerIDQueryContext\"48@\"NSString\"56@?<v@?@\"IDSURI\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B@\"NSDictionary\"@\"NSUUID\">64"
+ "B76@0:8@\"NSArray\"16@\"NSData\"24@\"IDSURI\"32@\"NSString\"40B48B52B56@\"NSString\"60@?<v@?@\"IDSURI\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B@\"NSDictionary\"@\"NSUUID\">68"
+ "Broadcasting peer verification update"
+ "Dec 20 2025"
+ "Finished query for uris %s fromURI: %@ { success: %{bool}d offline: %{bool}d queryID: %@ }"
+ "_notifyClientOfKTVerifierResults:forService:queryID:"
+ "initWithVerifierResult:requestID:timestamp:"
+ "ktPeerVerificationResultsUpdated:forService:timestamp:queryID:"
+ "peerVerificationFinishedWithResults:queryID:"
+ "query-id"
+ "query-timestamp"
+ "v32@0:8@?<v@?@\"IDSURI\"@\"NSArray\"@\"NSArray\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B@\"NSUUID\">16@\"NSString\"24"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSDate\"32@\"NSUUID\"40"
+ "v52@?0@\"NSDictionary\"8@\"IDSURI\"16@\"NSString\"24B32@\"NSError\"36@\"NSUUID\"44"
+ "v80@?0@\"IDSURI\"8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32B40@\"IDSPeerIDQueryHandlerMetricContext\"44@\"NSDictionary\"52B60@\"NSDictionary\"64@\"NSUUID\"72"
+ "v88@?0@\"IDSURI\"8@\"NSArray\"16@\"NSArray\"24@\"NSDictionary\"32@\"NSDictionary\"40@\"NSString\"48B56@\"IDSPeerIDQueryHandlerMetricContext\"60@\"NSDictionary\"68B76@\"NSUUID\"80"
- "20:36:46"
- "B72@0:8@\"NSArray\"16@\"NSData\"24@\"IDSURI\"32@\"NSString\"40@\"IDSPeerIDQueryContext\"48@\"NSString\"56@?<v@?@\"IDSURI\"@\"NSArray\"@\"NSArray\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B>64"
- "B72@0:8@\"NSArray\"16@\"NSData\"24@\"IDSURI\"32@\"NSString\"40@\"IDSPeerIDQueryContext\"48@\"NSString\"56@?<v@?@\"IDSURI\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B@\"NSDictionary\">64"
- "B76@0:8@\"NSArray\"16@\"NSData\"24@\"IDSURI\"32@\"NSString\"40B48B52B56@\"NSString\"60@?<v@?@\"IDSURI\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B@\"NSDictionary\">68"
- "Dec  8 2025"
- "Finished query for uris %s fromURI: %@ { success: %{bool}d offline: %{bool}d }"
- "_notifyClientOfKTVerifierResults:forService:"
- "initWithVerifierResult:requestID:"
- "ktPeerVerificationResultsUpdated:forService:"
- "v32@0:8@?<v@?@\"IDSURI\"@\"NSArray\"@\"NSArray\"@\"NSDictionary\"@\"NSDictionary\"@\"NSString\"B@\"IDSPeerIDQueryHandlerMetricContext\"@\"NSDictionary\"B>16@\"NSString\"24"
- "v72@?0@\"IDSURI\"8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSString\"32B40@\"IDSPeerIDQueryHandlerMetricContext\"44@\"NSDictionary\"52B60@\"NSDictionary\"64"
- "v80@?0@\"IDSURI\"8@\"NSArray\"16@\"NSArray\"24@\"NSDictionary\"32@\"NSDictionary\"40@\"NSString\"48B56@\"IDSPeerIDQueryHandlerMetricContext\"60@\"NSDictionary\"68B76"

```
