## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-  __TEXT.__text: 0x60604
-  __TEXT.__objc_methlist: 0x5da4
+  __TEXT.__text: 0x60d7c
+  __TEXT.__objc_methlist: 0x5dcc
   __TEXT.__const: 0x368
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__cstring: 0x5997
-  __TEXT.__oslogstring: 0x3058
-  __TEXT.__unwind_info: 0x11a8
+  __TEXT.__cstring: 0x5a00
+  __TEXT.__oslogstring: 0x310f
+  __TEXT.__unwind_info: 0x11c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2888
+  __DATA_CONST.__objc_selrefs: 0x2898
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x448
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x5000
-  __AUTH_CONST.__objc_const: 0x7ce0
+  __AUTH_CONST.__objc_const: 0x7ce8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH.__objc_data: 0x1360
+  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH.__objc_data: 0x13b0
   __DATA.__objc_ivar: 0x31c
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x2c0
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2074
-  Symbols:   6009
-  CStrings:  1833
+  Functions: 2079
+  Symbols:   6019
+  CStrings:  1839
 
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
~ __DATA.__data : content changed
Symbols:
+ -[NSPPrivateAccessTokenFetcher checkCurrentQuotaStatusWithQueue:completionHandler:]
+ -[NSPServerClient checkCurrentQuotaStatusWithFetcher:allowRetry:completionHandler:]
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
