## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-  __TEXT.__text: 0xbc650
+  __TEXT.__text: 0xbcd34
   __TEXT.__auth_stubs: 0x18e0
   __TEXT.__objc_stubs: 0xcc80
-  __TEXT.__objc_methlist: 0x501c
+  __TEXT.__objc_methlist: 0x5034
   __TEXT.__const: 0x285
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x3554
-  __TEXT.__oslogstring: 0x10fcd
-  __TEXT.__cstring: 0xdd0b
-  __TEXT.__objc_methname: 0xff9a
+  __TEXT.__oslogstring: 0x11036
+  __TEXT.__cstring: 0xdd4b
+  __TEXT.__objc_methname: 0xffe0
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a69
-  __TEXT.__unwind_info: 0x1948
-  __DATA_CONST.__const: 0x2238
+  __TEXT.__unwind_info: 0x1968
+  __DATA_CONST.__const: 0x2250
   __DATA_CONST.__cfstring: 0x8ae0
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_intobj: 0x6d8
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xc80
-  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__got: 0x810
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb0d0
-  __DATA.__objc_selrefs: 0x39c8
-  __DATA.__objc_ivar: 0x9ec
+  __DATA.__objc_const: 0xb0f8
+  __DATA.__objc_selrefs: 0x39d0
+  __DATA.__objc_ivar: 0x9f0
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__bss: 0x220

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2147
+  Functions: 2150
   Symbols:   638
-  CStrings:  7372
+  CStrings:  7378
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ "-[NSPPrivacyTokenManager fetchQuotaResponseForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher checkCurrentQuotaStatusWithQueue:completionHandler:]"
+ "Configuration data has been cleared before agent data is copied"
+ "Failed to fetch current quota status: %@"
+ "NSPServerQuotaStatus"
+ "_relatedConfigurationHash"
+ "_selfConfigurationHash"
+ "checkCurrentQuotaStatusWithFetcher:allowRetry:completionHandler:"
+ "checkCurrentQuotaStatusWithQueue:completionHandler:"
+ "fetchQuotaResponseForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:"
- "-[NSPPrivacyTokenManager checkQuotaInnerForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:]"
- "checkCostQuotaForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:"
- "fetchDeviceQuotaConfigForIssuerName:quotaService:auditToken:bundleID:accessToken:completionHandler:"
- "v56@?0d8d16Q24q32@\"NSString\"40@\"NSString\"48"

```
