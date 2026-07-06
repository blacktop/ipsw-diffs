## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

-  __TEXT.__text: 0x2c928
+  __TEXT.__text: 0x2c978
   __TEXT.__objc_methlist: 0x38fc
   __TEXT.__const: 0x164
   __TEXT.__cstring: 0x2c0d
   __TEXT.__oslogstring: 0x226d
   __TEXT.__gcc_except_tab: 0x10c0
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xc98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ -[ASTSession sendProfileResult:error:] : 112 -> 96
~ -[ASTSession session:signPayload:completionHandler:] : 208 -> 192
~ -[ASTSession session:signFile:completionHandler:] : 208 -> 192
~ +[ASTEncodingUtilities parseJSONResponseWithData:error:] : 160 -> 220
~ +[ASTEncodingUtilities jsonSerializeObject:error:] : 256 -> 316
~ -[ASTRemoteServerSession sendAuthInfoResult:error:] : 400 -> 408
~ -[ASTRemoteServerSession sendProfileResult:error:] : 792 -> 788
~ -[ASTRemoteServerSession sendTestResult:error:] : 600 -> 604

```
