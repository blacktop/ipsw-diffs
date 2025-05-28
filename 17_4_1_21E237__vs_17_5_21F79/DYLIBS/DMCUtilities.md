## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-3.26.5.12.0
-  __TEXT.__text: 0x2a844
+3.26.6.4.0
+  __TEXT.__text: 0x2aa4c
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x22d4
+  __TEXT.__objc_methlist: 0x22f0
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x4c8
-  __TEXT.__cstring: 0x2dc6
-  __TEXT.__oslogstring: 0x4025
+  __TEXT.__gcc_except_tab: 0x4b0
+  __TEXT.__cstring: 0x2e14
+  __TEXT.__oslogstring: 0x407d
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xaec
+  __TEXT.__unwind_info: 0xadc
   __TEXT.__objc_classname: 0x3ef
-  __TEXT.__objc_methname: 0x83ce
-  __TEXT.__objc_methtype: 0x1120
-  __TEXT.__objc_stubs: 0x4e80
+  __TEXT.__objc_methname: 0x842a
+  __TEXT.__objc_methtype: 0x112f
+  __TEXT.__objc_stubs: 0x4ec0
   __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__const: 0xdf0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2c60
-  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_selrefs: 0x1e08
   __DATA_CONST.__objc_classrefs: 0x268
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__cfstring: 0x35a0
   __AUTH_CONST.__objc_const: 0x1008
   __AUTH_CONST.__const: 0xbe0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__auth_got: 0x720
   __AUTH.__objc_data: 0xbe0
   __DATA.__objc_ivar: 0x19c
-  __DATA.__data: 0x3a1
-  __DATA.__bss: 0x7e8
+  __DATA.__data: 0x3a9
+  __DATA.__bss: 0x7e0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1064
-  Symbols:   4020
-  CStrings:  2301
+  Functions: 1067
+  Symbols:   4031
+  CStrings:  2308
 
Symbols:
+ +[DMCHTTPRequestor _parseWellKnownFailedErrorWithMessage:details:outError:]
+ +[DMCRatchet isAuthorizedForOperation:completion:]
+ _DMCHTTP403ResponseErrorCodeWellKnownFailed
+ ___50+[DMCRatchet isAuthorizedForOperation:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ _objc_msgSend$_parseWellKnownFailedErrorWithMessage:details:outError:
+ _objc_msgSend$isAuthorizedForOperation:completion:
CStrings:
+ "DMCRatchet is authorized because LARatchet is disabled"
+ "DMCRatchet is authorized because LARatchet is unavailable"
+ "HTTP_ERROR_403_RESPONSE_WELLKNOWN_FAILED"
+ "_parseWellKnownFailedErrorWithMessage:details:outError:"
+ "com.apple.well-known.failed"
+ "isAuthorizedForOperation:completion:"
+ "v12@?0B8"
+ "v32@0:8Q16@?24"
- "LARatchet is unavailable"

```
