## ctkd

> `/System/Library/Frameworks/CryptoTokenKit.framework/ctkd`

```diff

-805.0.10.0.0
-  __TEXT.__text: 0x200e4
+805.0.15.0.0
+  __TEXT.__text: 0x20854
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_stubs: 0x3f80
-  __TEXT.__objc_methlist: 0x2184
+  __TEXT.__objc_stubs: 0x3fe0
+  __TEXT.__objc_methlist: 0x2214
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x1580
-  __TEXT.__objc_methname: 0x53fc
-  __TEXT.__oslogstring: 0x21b6
-  __TEXT.__cstring: 0xe11
-  __TEXT.__objc_classname: 0x641
-  __TEXT.__objc_methtype: 0x1863
+  __TEXT.__objc_methname: 0x55c0
+  __TEXT.__oslogstring: 0x2200
+  __TEXT.__cstring: 0xe2e
+  __TEXT.__objc_classname: 0x65a
+  __TEXT.__objc_methtype: 0x1aae
   __TEXT.__dlopen_cstrs: 0x6e
   __TEXT.__ustring: 0x98
-  __TEXT.__unwind_info: 0xc30
+  __TEXT.__unwind_info: 0xc58
   __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xab8
-  __DATA_CONST.__cfstring: 0xd00
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__cfstring: 0xd20
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x45c0
-  __DATA.__objc_selrefs: 0x1380
-  __DATA.__objc_ivar: 0x2d4
+  __DATA.__objc_const: 0x4640
+  __DATA.__objc_selrefs: 0x13d8
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__objc_data: 0xb90
-  __DATA.__data: 0xa20
+  __DATA.__data: 0xa80
   __DATA.__bss: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA25F58C-E511-388D-9817-B88E9ADC76BB
-  Functions: 825
+  UUID: 916B63F0-BD4B-3432-8E72-9DDD85A3ADF3
+  Functions: 837
   Symbols:   232
-  CStrings:  1626
+  CStrings:  1655
 
CStrings:
+ "Failed to test connection to endpoint for registered token: %@, error: %@"
+ "Q"
+ "T@\"TKHostTokenDriver\",&,N"
+ "TKClientTokenProtocol"
+ "_driverQueue"
+ "acquireTokenConnection:canRequireCardInsertion:completion:"
+ "endSession:reply:"
+ "hosttoken-driver:%@"
+ "isEndpointValidWithCompletion:"
+ "session:createObjectWithAttributes:reply:"
+ "session:deleteObjectWithObjectID:reply:"
+ "session:evaluateAccessControl:forOperation:reply:"
+ "session:getAdvertisedItemsWithReply:"
+ "session:getAttributesOfObjectID:reply:"
+ "session:objectID:operation:data:algorithms:parameters:reply:"
+ "session:slotNameWithReply:"
+ "startSessionWithLAContext:parameters:reply:"
+ "v12@?0B8"
+ "v32@0:8@\"NSNumber\"16@?<v@?>24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSString\">24"
+ "v32@0:8B16B20@?24"
+ "v40@0:8@\"LAContext\"16@\"NSDictionary\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSData\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSDictionary\"24@?<v@?@\"NSData\"@\"NSDictionary\"@\"NSError\">32"
+ "v48@0:8@\"NSNumber\"16@\"NSData\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "v72@0:8@\"NSNumber\"16@\"NSData\"24q32@\"NSData\"40@\"NSArray\"48@\"NSDictionary\"56@?<v@?@@\"NSError\">64"
+ "v72@0:8@16@24q32@40@48@56@?64"
- "T@\"TKHostTokenDriver\",&,N,V_driver"

```
