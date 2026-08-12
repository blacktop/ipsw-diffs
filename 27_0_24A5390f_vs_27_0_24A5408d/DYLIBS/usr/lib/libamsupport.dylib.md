## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-475.0.2.0.0
-  __TEXT.__text: 0x136d0
-  __TEXT.__objc_methlist: 0x36c
+475.0.9.0.0
+  __TEXT.__text: 0x13928
+  __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0xd2c0
-  __TEXT.__cstring: 0x2b06
+  __TEXT.__cstring: 0x2bbf
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__unwind_info: 0x528
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x368
+  __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xa48
-  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__const: 0xa68
+  __AUTH_CONST.__cfstring: 0x1000
   __AUTH_CONST.__objc_const: 0x588
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x708
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1b8
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x19
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 535
-  Symbols:   1222
-  CStrings:  430
+  Functions: 540
+  Symbols:   1247
+  CStrings:  437
 
Symbols:
+ -[AMSupportOSURLSession shouldUpgrateToHTTPS]
+ _CFBundleGetInfoDictionary
+ _CFBundleGetMainBundle
+ _Img4EncodeItemCopyAndTransferBuffer
+ _Img4EncodeSet
+ _OBJC_CLASS_$_NSURLComponents
+ __AMSupportX509DecodeEcVerifySignatureDataWithOid
+ __NSConcreteGlobalBlock
+ ___45-[AMSupportOSURLSession shouldUpgrateToHTTPS]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ __oidSha1Ecdsa
+ _dispatch_once
+ _objc_msgSend$URL
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$port
+ _objc_msgSend$scheme
+ _objc_msgSend$setPort:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$shouldUpgrateToHTTPS
+ _oidSha1Ecdsa
+ _shouldUpgrateToHTTPS.onceToken
+ _shouldUpgrateToHTTPS.usingATS
- _Img4EncodeDictionary
CStrings:
+ "-[AMSupportOSURLSession _urlRequestForHTTPMessage:]"
+ "Leaving custom port as is: %@"
+ "NSAppTransportSecurity"
+ "http"
+ "httpResponseData is NULL"
+ "https"
+ "using ATS, upgraded requestURL to https: %@"
```
