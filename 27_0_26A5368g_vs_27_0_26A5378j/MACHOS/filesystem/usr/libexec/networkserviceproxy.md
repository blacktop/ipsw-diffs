## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-  __TEXT.__text: 0xc9b20
+  __TEXT.__text: 0xca278
   __TEXT.__auth_stubs: 0x1740
   __TEXT.__objc_stubs: 0xcb00
-  __TEXT.__objc_methlist: 0x501c
+  __TEXT.__objc_methlist: 0x5034
   __TEXT.__const: 0x278
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x3550
-  __TEXT.__oslogstring: 0x10f06
-  __TEXT.__cstring: 0xdd2a
-  __TEXT.__objc_methname: 0xfe19
+  __TEXT.__oslogstring: 0x10f6f
+  __TEXT.__cstring: 0xdd6a
+  __TEXT.__objc_methname: 0xfe5f
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a52
   __TEXT.__unwind_info: 0x1978
-  __DATA_CONST.__const: 0x2540
+  __DATA_CONST.__const: 0x2548
   __DATA_CONST.__cfstring: 0x8a60
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_intobj: 0x6d8
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xbb0
-  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__got: 0x808
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xb0b0
-  __DATA.__objc_selrefs: 0x3968
-  __DATA.__objc_ivar: 0x9e8
+  __DATA.__objc_const: 0xb0d8
+  __DATA.__objc_selrefs: 0x3970
+  __DATA.__objc_ivar: 0x9ec
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0xb48
   __DATA.__bss: 0x218

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2237
+  Functions: 2240
   Symbols:   611
-  CStrings:  7346
+  CStrings:  7352
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
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
