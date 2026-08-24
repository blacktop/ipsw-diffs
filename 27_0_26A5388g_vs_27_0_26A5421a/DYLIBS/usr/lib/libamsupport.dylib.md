## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-475.0.2.0.0
-  __TEXT.__text: 0x13b60
-  __TEXT.__objc_methlist: 0x36c
+475.0.9.0.0
+  __TEXT.__text: 0x13dd4
+  __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0xd2c0
-  __TEXT.__cstring: 0x2c2b
+  __TEXT.__cstring: 0x2ce4
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__unwind_info: 0x538
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x368
+  __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xb08
-  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__const: 0xb28
+  __AUTH_CONST.__cfstring: 0x1000
   __AUTH_CONST.__objc_const: 0x588
-  __AUTH_CONST.__auth_got: 0x690
-  __DATA.__objc_classrefs: 0x80
+  __AUTH_CONST.__auth_got: 0x6a8
+  __DATA.__objc_classrefs: 0x88
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1b8
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 544
-  Symbols:   1250
-  CStrings:  444
+  Functions: 549
+  Symbols:   1275
+  CStrings:  451
 
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
+ shouldUpgrateToHTTPS.onceToken
+ shouldUpgrateToHTTPS.usingATS
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
