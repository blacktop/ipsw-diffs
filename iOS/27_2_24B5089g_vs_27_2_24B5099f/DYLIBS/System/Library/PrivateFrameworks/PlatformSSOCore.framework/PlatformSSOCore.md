## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-643.40.27.0.0
-  __TEXT.__text: 0x93ea8
-  __TEXT.__objc_methlist: 0x6388
-  __TEXT.__const: 0x1a04
-  __TEXT.__cstring: 0xae78
-  __TEXT.__oslogstring: 0x2027
+643.40.34.0.0
+  __TEXT.__text: 0x95498
+  __TEXT.__objc_methlist: 0x63b0
+  __TEXT.__const: 0x1a14
+  __TEXT.__cstring: 0xb2a8
+  __TEXT.__oslogstring: 0x2067
+  __TEXT.__ustring: 0x2c
   __TEXT.__gcc_except_tab: 0x6f4
   __TEXT.__dlopen_cstrs: 0xa6
   __TEXT.__swift5_typeref: 0x166

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x2e40
+  __TEXT.__unwind_info: 0x2ea0
   __TEXT.__eh_frame: 0x568
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2600
+  __DATA_CONST.__const: 0x2630
   __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d68
+  __DATA_CONST.__objc_selrefs: 0x2dd0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x9d0
-  __AUTH_CONST.__const: 0xc60
-  __AUTH_CONST.__cfstring: 0x7c20
-  __AUTH_CONST.__objc_const: 0x14e40
-  __AUTH_CONST.__objc_intobj: 0x240
+  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__got: 0x9d8
+  __AUTH_CONST.__const: 0xce0
+  __AUTH_CONST.__cfstring: 0x80c0
+  __AUTH_CONST.__objc_const: 0x14e50
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH_CONST.__auth_got: 0xdb8
   __AUTH.__objc_data: 0x35f0
   __AUTH.__data: 0x1a8
   __DATA.__objc_ivar: 0x65c

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3869
-  Symbols:   5877
-  CStrings:  1775
+  Functions: 3894
+  Symbols:   5899
+  CStrings:  1814
 
Symbols:
+ +[POConstantCoreUtil validatedAdditionalHTTPHeaders:]
+ -[POAuthenticationProcess addAdditionalHTTPHeadersToRequest:context:]
+ -[PODeviceConfiguration additionalHTTPHeaders]
+ -[PODeviceConfiguration setAdditionalHTTPHeaders:]
+ GCC_except_table128
+ GCC_except_table153
+ GCC_except_table56
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_IVAR_$_PODeviceConfiguration._additionalHTTPHeaders
+ _POIsReservedHTTPHeaderField.onceToken
+ _POIsReservedHTTPHeaderField.reservedFields
+ _POIsValidHTTPHeaderFieldName.illegalFieldCharacters
+ _POIsValidHTTPHeaderFieldName.onceToken
+ _POIsValidHTTPHeaderFieldValue.illegalValueCharacters
+ _POIsValidHTTPHeaderFieldValue.onceToken
+ _PO_LOG_POConstantCoreUtil
+ _PO_LOG_POConstantCoreUtil.log
+ _PO_LOG_POConstantCoreUtil.once
+ ___53+[POConstantCoreUtil validatedAdditionalHTTPHeaders:]_block_invoke
+ ___69-[POAuthenticationProcess addAdditionalHTTPHeadersToRequest:context:]_block_invoke
+ ___POAdditionalHTTPHeadersForDisplay_block_invoke
+ ___POIsReservedHTTPHeaderField_block_invoke
+ ___POIsValidHTTPHeaderFieldName_block_invoke
+ ___POIsValidHTTPHeaderFieldValue_block_invoke
+ ___PO_LOG_POConstantCoreUtil_block_invoke
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ _kPOErrorDomain
- -[POUserConfiguration newUser]
- GCC_except_table126
- GCC_except_table151
- _NSClassFromString
- _OBJC_IVAR_$_POUserConfiguration._newUser
CStrings:
+ "!#$%&'*+-.^_`|~"
+ "%@…%@ (%@ characters)"
+ "Added %{public}@ of %{public}@ additional HTTP headers to request: %{public}@"
+ "Additional HTTP header is already set on the request; not overwriting it."
+ "AdditionalHTTPHeaders entry is not a string pair; discarding it."
+ "AdditionalHTTPHeaders field collides with another entry that differs only in case; discarding all of them."
+ "AdditionalHTTPHeaders field is not a valid header name; discarding it."
+ "AdditionalHTTPHeaders field is reserved; discarding it."
+ "AdditionalHTTPHeaders is not a dictionary; ignoring it."
+ "AdditionalHTTPHeaders value is not a valid header value; discarding it."
+ "Headers: %@, Limit: %@"
+ "Missing device encryption key."
+ "Missing temporary account credential."
+ "POConstantCoreUtil"
+ "Too many entries in AdditionalHTTPHeaders; ignoring all of them."
+ "Unable to decrypt temporary account credential with the outgoing key; dropping entry."
+ "accept"
+ "accept-encoding"
+ "authentication-info"
+ "authorization"
+ "connection"
+ "content-encoding"
+ "content-length"
+ "content-type"
+ "cookie"
+ "cookie2"
+ "expect"
+ "host"
+ "keep-alive"
+ "proxy-authenticate"
+ "proxy-authentication-info"
+ "proxy-authorization"
+ "set-cookie"
+ "set-cookie2"
+ "soapaction"
+ "te"
+ "trailer"
+ "transfer-encoding"
+ "upgrade"
+ "www-authenticate"
- "XCTestCase"
```
