## MediaSetup

> `/System/Library/Frameworks/MediaSetup.framework/MediaSetup`

```diff

-249.40.9.0.0
-  __TEXT.__text: 0x13a5c
-  __TEXT.__auth_stubs: 0x480
+249.50.2.0.0
+  __TEXT.__text: 0x13afc
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0x1cac
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x264f
+  __TEXT.__cstring: 0x267b
   __TEXT.__gcc_except_tab: 0x23c
-  __TEXT.__oslogstring: 0x65b
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__oslogstring: 0x689
+  __TEXT.__unwind_info: 0x728
   __TEXT.__objc_classname: 0x4ab
   __TEXT.__objc_methname: 0x4303
   __TEXT.__objc_methtype: 0xae5

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x250
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x2260
+  __AUTH_CONST.__cfstring: 0x22c0
   __AUTH_CONST.__objc_const: 0x5680
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x500

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78462D6C-DB1A-3655-9D12-8FB447BDADDE
-  Functions: 635
-  Symbols:   2542
-  CStrings:  1561
+  UUID: 80687ACD-B155-32D4-99D9-540E6E7CE84C
+  Functions: 634
+  Symbols:   2541
+  CStrings:  1567
 
Symbols:
+ _objc_retain_x1
- ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke.cold.5
Functions:
~ ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke : 2136 -> 2428
+ _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
~ ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke.cold.1 : 72 -> 68
~ ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke.cold.2 : 116 -> 68
~ ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke.cold.3 : 72 -> 68
~ ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke.cold.4 : 72 -> 68
- ___85-[MSOAuthTokenHandler performTokenFetchTaskWithSession:bodyString:completionHandler:]_block_invoke.cold.5
CStrings:
+ "error"
+ "error_description"
+ "error_uri"
+ "non-200 status code: %ld error: %@"
+ "non-200 status code: %ld error: %@ error_description: %@ error_uri: %@"
- "non-200 status code: %ld"

```
