## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1968.400.1.0.0
-  __TEXT.__text: 0x1465a8
-  __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0xd22c
+1968.400.11.0.0
+  __TEXT.__text: 0x146eb0
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0xd244
   __TEXT.__const: 0x422
   __TEXT.__gcc_except_tab: 0x47dc
-  __TEXT.__oslogstring: 0x1a107
-  __TEXT.__cstring: 0x1073b
+  __TEXT.__oslogstring: 0x1a22c
+  __TEXT.__cstring: 0x107b2
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
   __TEXT.__swift5_typeref: 0x8
-  __TEXT.__unwind_info: 0x4f30
+  __TEXT.__unwind_info: 0x4f38
   __TEXT.__objc_classname: 0x19e4
-  __TEXT.__objc_methname: 0x200fb
-  __TEXT.__objc_methtype: 0x7ac2
-  __TEXT.__objc_stubs: 0x14300
-  __DATA_CONST.__got: 0x12c0
-  __DATA_CONST.__const: 0x52b0
+  __TEXT.__objc_methname: 0x201bf
+  __TEXT.__objc_methtype: 0x7b39
+  __TEXT.__objc_stubs: 0x14380
+  __DATA_CONST.__got: 0x12c8
+  __DATA_CONST.__const: 0x5328
   __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68e0
+  __DATA_CONST.__objc_selrefs: 0x6900
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x460
-  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__auth_got: 0xe90
   __AUTH_CONST.__const: 0x1b20
   __AUTH_CONST.__cfstring: 0x73e0
-  __AUTH_CONST.__objc_const: 0x3b408
+  __AUTH_CONST.__objc_const: 0x3b418
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1a90

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F75FC882-FEF0-34A4-A4AB-CFF15F90284A
+  UUID: A4383B6B-7F82-30B9-A624-FE7891C88685
   Functions: 6572
-  Symbols:   1582
-  CStrings:  10133
+  Symbols:   1584
+  CStrings:  10144
 
Symbols:
+ _OBJC_CLASS_$_IDSIDQueryCallbackInfo
+ _xpc_dictionary_get_int64
Functions:
~ sub_195f9b988 -> sub_195fd5988 : 1468 -> 1540
~ sub_195f9bf44 -> sub_195fd5f8c : 196 -> 236
~ sub_195f9c584 -> sub_195fd65f4 : 192 -> 248
~ sub_195f9c644 -> sub_195fd66ec : 520 -> 680
~ sub_195f9cef0 -> sub_195fd7038 : 192 -> 248
~ sub_195f9cfb0 -> sub_195fd7130 : 684 -> 844
~ sub_195f9d84c -> sub_195fd7a6c : 192 -> 248
~ sub_195f9d90c -> sub_195fd7b64 : 684 -> 844
~ sub_195f9e1e4 -> sub_195fd84dc : 192 -> 248
~ sub_195f9e2a4 -> sub_195fd85d4 : 772 -> 932
~ sub_195fab888 -> sub_195fe5c58 : 460 -> 548
~ sub_195faba54 -> sub_195fe5e7c : 236 -> 448
~ sub_195fac22c -> sub_195fe6728 : 580 -> 692
~ sub_195fac470 -> sub_195fe69dc : 168 -> 200
~ sub_195fac518 -> sub_195fe6aa4 : 256 -> 372
~ sub_195fac7bc -> sub_195fe6dbc : 336 -> 416
~ sub_195fac90c -> sub_195fe6f5c : 28 -> 32
~ sub_195fad9a0 -> sub_195fe7ff4 : 1048 -> 1144
~ sub_195faddb8 -> sub_195fe846c : 168 -> 200
~ sub_195fade60 -> sub_195fe8534 : 256 -> 372
~ sub_195fae00c -> sub_195fe8754 : 336 -> 416
~ sub_195fae15c -> sub_195fe88f4 : 28 -> 32
~ sub_195fae384 -> sub_195fe8b20 : 320 -> 396
~ sub_195fae4c4 -> sub_195fe8cac : 576 -> 664
~ sub_195fae704 -> sub_195fe8f44 : 344 -> 420
~ sub_195faeb3c -> sub_195fe93c8 : 240 -> 276
~ sub_195faed5c -> sub_195fe960c : 988 -> 1008
~ sub_195fd90c0 -> sub_196013984 : 740 -> 804
~ sub_195fd93a4 -> sub_196013ca8 : 20 -> 24
CStrings:
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
