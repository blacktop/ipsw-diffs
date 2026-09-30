## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1968.200.71.0.0
-  __TEXT.__text: 0x1443ec
+1968.200.71.2.1
+  __TEXT.__text: 0x144bc4
   __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0xd0a4
-  __TEXT.__const: 0x41a
+  __TEXT.__objc_methlist: 0xd0d4
+  __TEXT.__const: 0x422
   __TEXT.__gcc_except_tab: 0x47dc
-  __TEXT.__oslogstring: 0x19e82
-  __TEXT.__cstring: 0x1049a
+  __TEXT.__oslogstring: 0x19f24
+  __TEXT.__cstring: 0x10545
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
   __TEXT.__swift5_typeref: 0x8
-  __TEXT.__unwind_info: 0x4ec0
+  __TEXT.__unwind_info: 0x4ed0
   __TEXT.__objc_classname: 0x19c1
-  __TEXT.__objc_methname: 0x1fe5a
-  __TEXT.__objc_methtype: 0x7823
-  __TEXT.__objc_stubs: 0x141a0
+  __TEXT.__objc_methname: 0x1feec
+  __TEXT.__objc_methtype: 0x78e1
+  __TEXT.__objc_stubs: 0x141e0
   __DATA_CONST.__got: 0x1298
   __DATA_CONST.__const: 0x5250
   __DATA_CONST.__objc_classlist: 0x588
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6890
+  __DATA_CONST.__objc_selrefs: 0x68a0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x458
   __AUTH_CONST.__auth_got: 0xe88
   __AUTH_CONST.__const: 0x1b20
   __AUTH_CONST.__cfstring: 0x7340
-  __AUTH_CONST.__objc_const: 0x3abf0
+  __AUTH_CONST.__objc_const: 0x3aea0
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1a40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 47914350-9475-3191-932B-7962374F2C7E
-  Functions: 6536
+  UUID: 9757F1FC-C290-3300-A232-CD50485E61F4
+  Functions: 6542
   Symbols:   1574
-  CStrings:  10078
+  CStrings:  10086
 
CStrings:
+ "-[_IDSConnection inviteDroppedWithPayload:forTopic:sessionID:toIdentifier:fromID:error:]"
+ "-[_IDSService connection:account:inviteDroppedForSessionID:fromID:context:error:]"
+ "Received incoming invitation but dropped %@ forTopic %@ sessionID %@ toIdentifier %@ fromID %@"
+ "Received invitation but dropped for sessionID %@ fromID %@ with %@"
+ "connection:account:inviteDroppedForSessionID:fromID:context:error:"
+ "inviteDroppedWithPayload:forTopic:sessionID:toIdentifier:fromID:error:"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "v64@0:8@\"IDSConnection\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
+ "v64@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSError\"56"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
