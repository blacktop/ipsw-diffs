## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-475.0.9.0.0
-  __TEXT.__text: 0x13730
-  __TEXT.__objc_methlist: 0x37c
-  __TEXT.__const: 0xd2c0
-  __TEXT.__cstring: 0x2bbf
+475.40.6.0.0
+  __TEXT.__text: 0x136b4
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0xd2c8
+  __TEXT.__cstring: 0x2bff
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x720
+  __TEXT.__unwind_info: 0x718
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xa68
-  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__const: 0xa48
+  __AUTH_CONST.__cfstring: 0xfe0
   __AUTH_CONST.__objc_const: 0x588
-  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__auth_got: 0x6f8
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1b8
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 540
-  Symbols:   1247
+  Functions: 537
+  Symbols:   1235
   CStrings:  437
 
Symbols:
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _kAMSupportHttpOptionRequestHTTPAllowed
+ _kImg4TagStr_srvc
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$set_atsContext:
+ _os_variant_has_internal_content
- -[AMSupportOSURLSession shouldUpgrateToHTTPS]
- _CFBundleGetInfoDictionary
- _CFBundleGetMainBundle
- _OBJC_CLASS_$_NSURLComponents
- __NSConcreteGlobalBlock
- ___45-[AMSupportOSURLSession shouldUpgrateToHTTPS]_block_invoke
- ___block_descriptor_32_e5_v8?0l
- ___block_literal_global
- _dispatch_once
- _objc_msgSend$URL
- _objc_msgSend$caseInsensitiveCompare:
- _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$numberWithInt:
- _objc_msgSend$port
- _objc_msgSend$scheme
- _objc_msgSend$setPort:
- _objc_msgSend$setScheme:
- _objc_msgSend$shouldUpgrateToHTTPS
- _shouldUpgrateToHTTPS.onceToken
- _shouldUpgrateToHTTPS.usingATS
CStrings:
+ "-[AMSupportOSURLSession _defaultSessionConfigurationWithIdentifier:]"
+ "ATS: OS is internal."
+ "ATS: disabled per request on allowed build type."
+ "NSAllowsArbitraryLoads"
+ "RequestHTTPAllowed"
+ "com.apple.libamsupport.amsupporturlsession"
- "-[AMSupportOSURLSession _urlRequestForHTTPMessage:]"
- "Leaving custom port as is: %@"
- "NSAppTransportSecurity"
- "http"
- "https"
- "using ATS, upgraded requestURL to https: %@"
```
