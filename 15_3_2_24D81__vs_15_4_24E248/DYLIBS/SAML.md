## SAML

> `/System/Library/PrivateFrameworks/SAML.framework/Versions/A/SAML`

```diff

-561.30.1.0.0
-  __TEXT.__text: 0xe9c4
+561.40.17.0.0
+  __TEXT.__text: 0xe9d0
   __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x1674
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x112b
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__unwind_info: 0x448
   __TEXT.__objc_classname: 0x34e
   __TEXT.__objc_methname: 0x19b4
   __TEXT.__objc_methtype: 0xc77

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 07C06C19-0A21-33A1-899B-CF67D9FE613B
-  Functions: 425
-  Symbols:   1237
+  UUID: 5C572373-4B6C-324C-89A0-606EE566A8C0
+  Functions: 426
+  Symbols:   1239
   CStrings:  916
 
Symbols:
+ +[NSBundle(SAMLAdditions) saml_frameworkBundle].cold.1
+ +[XMLWrapperQuery initialize].cold.1
Functions:
~ _SAMLErrorInfoForParserErrorCode : 404 -> 384
- sub_24739f2b4
~ -[XMLWrapperSchema initWithSchemaData:] : 372 -> 368
~ -[XMLWrapperElement dealloc] : 88 -> 92
~ -[SAMLResponseElement assertionMeetsConditions:] : 404 -> 400
~ +[XMLWrapperQuery initialize] : 40 -> 44
~ -[XMLWrapperQuery elementForNode:] : 156 -> 168
~ -[XMLWrapperQuery searchNodeWithXpathQuery:query:error:] : 72 -> 84
~ -[XMLWrapperQuery registerXpathNamespacesForCtx:error:] : 480 -> 488
~ +[NSBundle(SAMLAdditions) saml_frameworkBundle] : 84 -> 68
~ -[XMLWrapperNamespace initWithNsNode:error:] : 192 -> 188

```
