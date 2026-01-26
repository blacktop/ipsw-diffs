## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.326.2.0.0
-  __TEXT.__text: 0x185a34
+525.326.4.0.0
+  __TEXT.__text: 0x185ca0
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0xe51c
+  __TEXT.__objc_methlist: 0xe534
   __TEXT.__const: 0x69f8
-  __TEXT.__cstring: 0xfd6c
+  __TEXT.__cstring: 0xfd86
   __TEXT.__gcc_except_tab: 0xa04c
-  __TEXT.__oslogstring: 0x12a41
+  __TEXT.__oslogstring: 0x12aa2
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4280
+  __TEXT.__unwind_info: 0x4288
   __TEXT.__objc_classname: 0x1d7c
-  __TEXT.__objc_methname: 0x23790
+  __TEXT.__objc_methname: 0x237e8
   __TEXT.__objc_methtype: 0x47c0
   __TEXT.__objc_stubs: 0xff80
   __DATA_CONST.__got: 0xa98

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x73b8
+  __DATA_CONST.__objc_selrefs: 0x73c8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x105c0
-  __AUTH_CONST.__objc_const: 0x26718
-  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH_CONST.__cfstring: 0x105e0
+  __AUTH_CONST.__objc_const: 0x26748
+  __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0x1078
+  __DATA.__objc_ivar: 0x107c
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f0
   __DATA_DIRTY.__objc_data: 0x14f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EC72152-A491-3DB1-AEF6-CB1BE9528CB5
-  Functions: 5549
-  Symbols:   20989
-  CStrings:  12198
+  UUID: 89B11132-D505-3A3C-8769-D83557437D20
+  Functions: 5551
+  Symbols:   20994
+  CStrings:  12204
 
Symbols:
+ -[AKAppleIDAuthenticationContext _shouldSkipAccountUpdates]
+ -[AKAppleIDAuthenticationContext set_shouldSkipAccountUpdates:]
+ _OBJC_IVAR_$_AKAppleIDAuthenticationContext._shouldSkipAccountUpdates
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.72
+ ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.73
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.87
+ ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.88
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.64
+ ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.65
+ ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.94
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.60
+ ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.61
+ ___block_literal_global.102
+ ___block_literal_global.90
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.70
- ___73-[AKAppleIDSession _generateAppleIDHeadersForSessionTask:withCompletion:]_block_invoke.71
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.82
- ___73-[AKAppleIDSession _handleAnisetteURLResponse:forRequest:withCompletion:]_block_invoke.85
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.62
- ___83-[AKAppleIDSession URLSession:task:getAppleIDHeadersForResponse:completionHandler:]_block_invoke.63
- ___91-[AKAppleIDSession _handleAnisetteReprovisionWithRequestURL:anisetteController:completion:]_block_invoke.92
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.58
- ___92-[AKAppleIDSession URLSession:task:getAppleIDRequestOrHeadersForResponse:completionHandler:]_block_invoke.59
- ___block_literal_global.100
- ___block_literal_global.88
CStrings:
+ "TB,N,V_shouldSkipAccountUpdates"
+ "Unhandled status code in URLSession:task:getAppleIDRequestOrHeadersForResponse:completion: - %li"
+ "_shouldSkipAccountUpdates"
+ "set_shouldSkipAccountUpdates:"

```
