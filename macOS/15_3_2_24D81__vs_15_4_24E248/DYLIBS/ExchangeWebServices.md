## ExchangeWebServices

> `/System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices`

```diff

 835.0.0.0.0
-  __TEXT.__text: 0x389b0
+  __TEXT.__text: 0x38d64
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0xa0d8
+  __TEXT.__objc_methlist: 0xa520
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x9f1f
   __TEXT.__oslogstring: 0xb29
-  __TEXT.__gcc_except_tab: 0x59c
-  __TEXT.__unwind_info: 0xff0
+  __TEXT.__gcc_except_tab: 0x5a8
+  __TEXT.__unwind_info: 0x1030
   __TEXT.__objc_classname: 0x33cb
   __TEXT.__objc_methname: 0x1041e
   __TEXT.__objc_methtype: 0x1868
   __TEXT.__objc_stubs: 0x4f60
   __DATA_CONST.__got: 0xff8
-  __DATA_CONST.__const: 0x24b0
+  __DATA_CONST.__const: 0x24e0
   __DATA_CONST.__objc_classlist: 0xf08
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3630
+  __DATA_CONST.__objc_selrefs: 0x37b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x280
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0xfcc0
-  __AUTH_CONST.__objc_const: 0x49730
+  __AUTH_CONST.__objc_const: 0x48f78
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A268B60-2AAD-315F-9461-A4FC7EFCCB26
-  Functions: 2936
-  Symbols:   9799
+  UUID: F738AB1A-0094-3BDF-94BB-A6B02418B3F0
+  Functions: 2968
+  Symbols:   9833
   CStrings:  8025
 
Symbols:
+ +[EWSAutodiscoverOperation log].cold.1
+ +[EWSAutodiscoverUtils emailDomainStringResemblesValidDomain:].cold.1
+ +[EWSAutodiscoverUtils log].cold.1
+ +[EWSExchangeServiceBinding log].cold.1
+ +[EWSTimeZoneDefinitionType log].cold.1
+ +[EWSTimeZoneType log].cold.1
+ +[ExchangeEmptyBearerResponse log].cold.1
+ +[ExchangeOAuthTokenRefreshResponse log].cold.1
+ +[JWTValidator log].cold.1
+ +[SOAPParser log].cold.1
+ +[XSDefinitions definitionForType:].cold.1
+ +[XSNamespaces prefixForNamespaceURI:].cold.1
+ -[EWSAutodiscoverBinding sendMessage:].cold.1
+ -[EWSAutodiscoverOperation URLSession:dataTask:didReceiveResponse:completionHandler:].cold.1
+ -[EWSAutodiscoverOperation start].cold.1
+ -[EWSAutodiscoverOperation start].cold.2
+ -[EWSAutodiscoverV2Binding sendMessage:withProtocol:retrieveAuthURI:].cold.1
+ -[EWSAutodiscoverV2Operation startWithProtocol:retrieveAuthURI:].cold.1
+ -[EWSExchangeServiceBindingTask completeWithResponse:].cold.1
+ -[EWSMessageType allowedElementKeys].cold.1
+ -[EWSServerVersionInfo messageTraceVersion].cold.1
+ -[ExchangeAutodiscovererV2 autodiscoverV2ForEmail:protocol:retrieveAuthURI:completionHandler:].cold.2
+ -[JWTValidator initWithIdToken:].cold.1
+ -[SOAPDocument _XMLAttributesStringWithComplexType:options:appendingToString:].cold.1
+ -[SOAPDocument _XMLStringWithComplexType:options:appendingToString:].cold.1
+ -[SOAPParser parser:didStartElement:namespaceURI:qualifiedName:attributes:].cold.1
+ -[SOAPParser parser:didStartElement:namespaceURI:qualifiedName:attributes:].cold.2
+ -[SOAPParser parser:didStartElement:namespaceURI:qualifiedName:attributes:].cold.3
+ -[XSDateDefinition stringFromValue:].cold.1
+ -[XSDateDefinition valueFromString:].cold.1
+ -[XSDateTimeDefinition valueFromString:].cold.1
+ -[XSTimeDefinition valueFromString:].cold.1
+ EWSLogURLAuthenticationChallenge.cold.1
+ exchangeLog.cold.1

```
