## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/Versions/A/NetworkServiceProxy`

```diff

-  __TEXT.__text: 0x64f78
-  __TEXT.__objc_methlist: 0x5da4
+  __TEXT.__text: 0x65790
+  __TEXT.__objc_methlist: 0x5dcc
   __TEXT.__const: 0x370
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x5995
-  __TEXT.__oslogstring: 0x3102
-  __TEXT.__unwind_info: 0x1178
+  __TEXT.__cstring: 0x59fe
+  __TEXT.__oslogstring: 0x31b9
+  __TEXT.__unwind_info: 0x1188
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2890
+  __DATA_CONST.__objc_selrefs: 0x28a0
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x460
   __AUTH_CONST.__const: 0x8e0
   __AUTH_CONST.__cfstring: 0x4fa0
-  __AUTH_CONST.__objc_const: 0x7ce0
+  __AUTH_CONST.__objc_const: 0x7ce8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x618
   __AUTH.__objc_data: 0x1360
   __DATA.__objc_ivar: 0x31c
   __DATA.__data: 0x268

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2089
-  Symbols:   4019
-  CStrings:  1831
+  Functions: 2094
+  Symbols:   4024
+  CStrings:  1837
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[NSPPrivateAccessTokenFetcher checkCurrentQuotaStatusWithQueue:completionHandler:]
+ -[NSPServerClient checkCurrentQuotaStatusWithFetcher:allowRetry:completionHandler:]
+ __83-[NSPPrivateAccessTokenFetcher checkCurrentQuotaStatusWithQueue:completionHandler:]_block_invoke
+ ___83-[NSPPrivateAccessTokenFetcher checkCurrentQuotaStatusWithQueue:completionHandler:]_block_invoke
+ ___83-[NSPServerClient checkCurrentQuotaStatusWithFetcher:allowRetry:completionHandler:]_block_invoke
+ _objc_msgSend$checkCurrentQuotaStatusWithFetcher:allowRetry:completionHandler:
- _os_variant_has_internal_content
CStrings:
+ "-[NSPPrivateAccessTokenFetcher checkCurrentQuotaStatusWithQueue:completionHandler:]"
+ "Check current quota status got invalid connection, retrying"
+ "Failed to fetch current quota status: %@"
+ "Fetch device quota got invalid connection, retrying"
+ "Fetching current quota status"
+ "NSPServerQuotaStatus"

```
