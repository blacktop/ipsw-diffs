## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS`

```diff

-1968.400.1.0.0
-  __TEXT.__text: 0x15f2b8
-  __TEXT.__auth_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0xd1bc
+1968.400.11.0.0
+  __TEXT.__text: 0x15fd5c
+  __TEXT.__auth_stubs: 0x1a90
+  __TEXT.__objc_methlist: 0xd1d4
   __TEXT.__const: 0x412
   __TEXT.__gcc_except_tab: 0x4834
-  __TEXT.__cstring: 0xf787
-  __TEXT.__oslogstring: 0x19f1a
+  __TEXT.__cstring: 0xf7fe
+  __TEXT.__oslogstring: 0x1a03f
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
   __TEXT.__swift5_typeref: 0x8
-  __TEXT.__unwind_info: 0x4de8
+  __TEXT.__unwind_info: 0x4df0
   __TEXT.__objc_classname: 0x19c7
-  __TEXT.__objc_methname: 0x1ff6a
-  __TEXT.__objc_methtype: 0x7a90
-  __TEXT.__objc_stubs: 0x13e20
-  __DATA_CONST.__got: 0x12a0
+  __TEXT.__objc_methname: 0x2002e
+  __TEXT.__objc_methtype: 0x7b07
+  __TEXT.__objc_stubs: 0x13ea0
+  __DATA_CONST.__got: 0x12a8
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6880
+  __DATA_CONST.__objc_selrefs: 0x68a0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x458
-  __AUTH_CONST.__auth_got: 0xd50
-  __AUTH_CONST.__const: 0x67d0
+  __AUTH_CONST.__auth_got: 0xd58
+  __AUTH_CONST.__const: 0x6830
   __AUTH_CONST.__cfstring: 0x7280
-  __AUTH_CONST.__objc_const: 0x3b080
+  __AUTH_CONST.__objc_const: 0x3b090
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1310

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D656A7BD-1538-3FC9-AFB1-A69FE6931849
-  Functions: 6586
-  Symbols:   1519
-  CStrings:  10034
+  UUID: 01C4E964-079D-3F50-B7A1-B56856F73A12
+  Functions: 6587
+  Symbols:   1521
+  CStrings:  10045
 
Symbols:
+ _OBJC_CLASS_$_IDSIDQueryCallbackInfo
+ _xpc_dictionary_get_int64
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CE8RugDKJ3KL-3sC8OC36BieXRUUqjzy99aPm1A/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/Client/IDSDataChannels.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8RugDKJ3KL-3sC8OC36BieXRUUqjzy99aPm1A/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannelsUtils.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8RugDKJ3KL-3sC8OC36BieXRUUqjzy99aPm1A/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannels_Direct.m"
+ "Delegate %@ doesn't respond to either KT verifier callback!"
+ "Notifying delegate %@ about KT peer verification results (with info) for service: %@"
+ "Received cache for service %@, %d count, timestamp: %@"
+ "Received cached id status {destinations: %@, service: %@, error: %@, timestamp: %@, queryID: %@}"
+ "Received id status {destinations: %@, service: %@, error: %@, timestamp: %@, queryID: %@}"
+ "Received results for service: %@  updates %@ timestamp: %@ queryID: %@"
+ "Received results for service: %@ error: %@ timestamp: %@ queryID: %@ updates {%@}"
+ "Received results for service: %@ timestamp: %@ queryID: %@ updates {%@}"
+ "_callDelegatesForService:destinationToVerifierResult:timestamp:queryID:"
+ "dateWithTimeIntervalSince1970:"
+ "idStatusUpdatedForDestinations:service:info:"
+ "idsKTVerifierResultsUpdatedForDestinations:service:info:"
+ "initWithTimestamp:queryID:"
+ "ktPeerVerificationResultsUpdated:forService:timestamp:queryID:"
+ "query-id"
+ "query-timestamp"
+ "v40@0:8@\"NSDictionary\"16@\"NSString\"24@\"IDSIDQueryCallbackInfo\"32"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSDate\"32@\"NSUUID\"40"
+ "v48@?0@\"NSDictionary\"8@\"NSString\"16@\"NSString\"24@\"NSError\"32@\"NSDate\"40"
+ "v56@?0@\"NSDictionary\"8@\"NSString\"16@\"NSString\"24@\"NSError\"32@\"NSDate\"40@\"NSUUID\"48"
- "/AppleInternal/Library/BuildRoots/4~CDywugBd2otlkFgqKXNhtva4Pp4VoHd3aah81cg/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/Client/IDSDataChannels.m"
- "/AppleInternal/Library/BuildRoots/4~CDywugBd2otlkFgqKXNhtva4Pp4VoHd3aah81cg/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannelsUtils.m"
- "/AppleInternal/Library/BuildRoots/4~CDywugBd2otlkFgqKXNhtva4Pp4VoHd3aah81cg/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannels_Direct.m"
- "Received cache for service %@, %d count"
- "Received cached id status {destinations: %@, service: %@, error: %@}"
- "Received id status {destinations: %@, service: %@, error: %@}"
- "Received results for service: %@  updates %@"
- "Received results for service: %@  updates {%@}"
- "Received results for service: %@ error: %@ updates {%@}"
- "_callDelegatesForService:destinationToVerifierResult:"
- "ktPeerVerificationResultsUpdated:forService:"
- "v40@?0@\"NSDictionary\"8@\"NSString\"16@\"NSString\"24@\"NSError\"32"

```
