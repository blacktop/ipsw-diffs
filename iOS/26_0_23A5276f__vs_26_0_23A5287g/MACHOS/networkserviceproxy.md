## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-896.0.0.0.1
-  __TEXT.__text: 0xb376c
+898.0.0.0.0
+  __TEXT.__text: 0xb377c
   __TEXT.__auth_stubs: 0x18c0
   __TEXT.__objc_stubs: 0xbf40
   __TEXT.__objc_methlist: 0x4d3c

   __TEXT.__gcc_except_tab: 0x3de8
   __TEXT.__oslogstring: 0xf831
   __TEXT.__cstring: 0xcb1a
-  __TEXT.__objc_methname: 0xf02e
+  __TEXT.__objc_methname: 0xf04f
   __TEXT.__objc_classname: 0xc7b
-  __TEXT.__objc_methtype: 0x27d9
+  __TEXT.__objc_methtype: 0x27df
   __TEXT.__unwind_info: 0x1830
   __DATA_CONST.__auth_got: 0xc70
   __DATA_CONST.__got: 0x6c8

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 95FDE48F-B9FD-34FC-9900-C23072D7A500
+  UUID: CB9D6AC0-911F-3EA9-9B2C-3DBC7F8385DC
   Functions: 2048
   Symbols:   627
   CStrings:  6866
CStrings:
+ "fetchKnownPrivateAccessTokenKeyWithFetcher:allowRetry:completionHandler:"
+ "fetchPrivateAccessTokenPairWithFetcher:allowRetry:completionHandler:"
+ "fetchPrivateAccessTokenWithFetcher:allowRetry:completionHandler:"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">28"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"@\"NSError\">28"
- "fetchKnownPrivateAccessTokenKeyWithFetcher:completionHandler:"
- "fetchPrivateAccessTokenPairWithFetcher:completionHandler:"
- "fetchPrivateAccessTokenWithFetcher:completionHandler:"
- "v32@0:8@\"NSPPrivateAccessTokenFetcher\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSPPrivateAccessTokenFetcher\"16@?<v@?@\"NSData\"@\"NSError\">24"

```
