## ITMLKit

> `/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit`

```diff

 649.0.1.0.0
-  __TEXT.__text: 0xb4360
+  __TEXT.__text: 0xb4280
   __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_methlist: 0xe944
   __TEXT.__const: 0x1e0

   __TEXT.__cstring: 0x6e62
   __TEXT.__oslogstring: 0x1ba3
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0x3270
+  __TEXT.__unwind_info: 0x3268
   __TEXT.__objc_classname: 0x2011
   __TEXT.__objc_methname: 0x1bc43
   __TEXT.__objc_methtype: 0x6bdd
   __TEXT.__objc_stubs: 0x13c80
-  __DATA_CONST.__got: 0xc60
+  __DATA_CONST.__got: 0xc58
   __DATA_CONST.__const: 0x38b0
   __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0x1a8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libxslt.1.dylib
-  UUID: 3EC0437E-E5B1-3EA4-8B51-FC5830652C4E
+  UUID: 0F50FA93-2F70-30C6-B9E5-1EC98400D43B
   Functions: 4482
-  Symbols:   17102
+  Symbols:   17101
   CStrings:  9032
 
Symbols:
- _xmlFree
Functions:
~ -[IKDOMElement getAttribute:] : 196 -> 184
~ -[IKDOMElement _attributes] : 300 -> 288
~ -[IKDOMCharacterData data] : 120 -> 108
~ +[IKTemplateStyleSheet _coalesceNode:overridingNode:forcedTemplateName:] : 3136 -> 3040
~ +[IKTemplateStyleSheet _resolveEmbeddedTemplatesInXmlTree:] : 624 -> 596
~ ___59-[IKTemplateStyleSheet _initWithXMLDoc:templateName:error:]_block_invoke.92 : 160 -> 148
~ +[IKTemplateStyleSheet _templateNodeWithXMLNode:parentNode:] : 368 -> 344
~ +[IKJSInspectorDOMAgent _parseAttributeString:] : 408 -> 380

```
