## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-990.60.10.0.1
-  __TEXT.__text: 0xc5870
-  __TEXT.__auth_stubs: 0x18f0
-  __TEXT.__objc_stubs: 0xd4c0
-  __TEXT.__objc_methlist: 0x50c4
-  __TEXT.__const: 0x2e8
+990.60.12.0.1
+  __TEXT.__text: 0xc6774
+  __TEXT.__auth_stubs: 0x1910
+  __TEXT.__objc_stubs: 0xd500
+  __TEXT.__objc_methlist: 0x50e4
+  __TEXT.__const: 0x308
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x39a0
-  __TEXT.__oslogstring: 0x1242a
-  __TEXT.__cstring: 0xe531
-  __TEXT.__objc_methname: 0x10979
+  __TEXT.__gcc_except_tab: 0x39cc
+  __TEXT.__oslogstring: 0x12664
+  __TEXT.__cstring: 0xe660
+  __TEXT.__objc_methname: 0x10a0a
   __TEXT.__objc_classname: 0xc2e
-  __TEXT.__objc_methtype: 0x2b8c
-  __TEXT.__unwind_info: 0x1fc0
-  __DATA_CONST.__const: 0x2498
+  __TEXT.__objc_methtype: 0x2bcb
+  __TEXT.__unwind_info: 0x1ff8
+  __DATA_CONST.__const: 0x2560
   __DATA_CONST.__cfstring: 0x8e40
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0x6f0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__auth_got: 0xc98
   __DATA_CONST.__got: 0x870
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb200
-  __DATA.__objc_selrefs: 0x3c00
+  __DATA.__objc_const: 0xb208
+  __DATA.__objc_selrefs: 0x3c18
   __DATA.__objc_ivar: 0xa0c
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2195
-  Symbols:   651
-  CStrings:  6440
+  Functions: 2207
+  Symbols:   653
+  CStrings:  6461
 
Symbols:
+ _homepodShouldEagerlyExit
+ _xpc_transaction_exit_clean
CStrings:
+ "-[NSPPrivacyTokenManager clearRetryIntervalForIssuerName:]"
+ "-[NSPPrivateAccessTokenFetcher clearRetryIntervalWithQueue:completionHandler:]"
+ "Clearing retry interval for issuer name \"%@\""
+ "ConfigFetchOnNetworkChange"
+ "Failed subscription check after %u attempts"
+ "Failed to clear retry interval: %@"
+ "Failed to get challenge issuer name, cannot clear retry interval"
+ "NSPServerErrorRetryAfter"
+ "Requesting clean exit after client request"
+ "Requesting clean exit after client token request"
+ "Requesting clean exit after daily stats event"
+ "Requesting clean exit after publish stats activity"
+ "Requesting clean exit after refresh activity"
+ "Retry: checking subscription after %lu seconds"
+ "Subscription check retry timer fired"
+ "System client entitlement missing, cannot clear retry interval"
+ "clearRetryAfterIntervalWithFetcher:allowRetry:completionHandler:"
+ "clearRetryIntervalForIssuerName:"
+ "clearRetryIntervalWithQueue:completionHandler:"
+ "com.apple.networkserviceproxy.subscriptionCheck"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSError\">28"
+ "v48@?0@\"NSData\"8q16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40"
+ "v56@?0@\"NSData\"8@\"NSData\"16q24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48"
+ "v56@?0@\"NSPPrivacyProxySuccessResponse\"8@\"NSData\"16q24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48"
+ "v64@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24q32@\"NSString\"40@\"NSString\"48@\"NSNumber\"56"
+ "v80@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSDate\"32@\"NSDictionary\"40q48@\"NSString\"56@\"NSString\"64@\"NSNumber\"72"
- "v40@?0@\"NSData\"8q16@\"NSString\"24@\"NSString\"32"
- "v48@?0@\"NSData\"8@\"NSData\"16q24@\"NSString\"32@\"NSString\"40"
- "v48@?0@\"NSPPrivacyProxySuccessResponse\"8@\"NSData\"16q24@\"NSString\"32@\"NSString\"40"
- "v56@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24q32@\"NSString\"40@\"NSString\"48"
- "v72@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSDate\"32@\"NSDictionary\"40q48@\"NSString\"56@\"NSString\"64"
```
