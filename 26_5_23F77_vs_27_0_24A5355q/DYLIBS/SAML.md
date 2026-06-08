## SAML

> `/System/Library/PrivateFrameworks/SAML.framework/SAML`

```diff

-593.50.1.0.0
-  __TEXT.__text: 0xe5cc
-  __TEXT.__auth_stubs: 0x500
+607.0.0.0.0
+  __TEXT.__text: 0xd784
   __TEXT.__objc_methlist: 0x1674
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x112b
-  __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x4b0
-  __TEXT.__objc_classname: 0x34e
-  __TEXT.__objc_methname: 0x19b4
-  __TEXT.__objc_methtype: 0xc77
-  __TEXT.__objc_stubs: 0x15e0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x1137
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__unwind_info: 0x440
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5c8
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9c0
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1a20
   __AUTH_CONST.__objc_const: 0x2c98
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x8c
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 76634759-EA33-3527-BD7E-778CDA515271
+  UUID: 3DB4C954-46A6-3396-9C5A-35C997BBFA26
   Functions: 426
-  Symbols:   1683
-  CStrings:  916
+  Symbols:   1686
+  CStrings:  421
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[SAMLNameId createElement:] : 124 -> 120
~ -[SAMLNameId nameQualifier] : 96 -> 88
~ -[SAMLNameId spNameQualifier] : 96 -> 88
~ -[SAMLNameId format] : 96 -> 88
~ -[SAMLNameId spProvidedId] : 96 -> 88
~ +[SAMLConditions createElement:] : 268 -> 260
~ -[SAMLConditions notBefore] : 140 -> 128
~ -[SAMLConditions notOnOrAfter] : 140 -> 128
~ -[SAMLConditions audienceRestrictions] : 384 -> 372
~ -[SAMLConditions oneTimeUse] : 68 -> 64
~ -[SAMLConditions proxyRestrictions] : 336 -> 328
~ -[SAMLConditions proxyRestrictionAudienceCount] : 220 -> 204
~ -[SAMLConditions assertionMeetsConditions:] : 220 -> 204
~ -[SAMLConditions conditions] : 16 -> 20
~ _SAMLParserErrorForErrorCode : 128 -> 124
~ _SAMLErrorInfoForParserErrorCode : 384 -> 380
~ _SAMLInvalidDocumentElementErrorForClass : 200 -> 188
~ _SAMLStringFromDate : 108 -> 100
~ _SAMLDateFormatter : 172 -> 164
~ _SAMLDateFromString : 108 -> 100
~ -[SAMLPGPData keyId] : 156 -> 148
~ -[SAMLPGPData packet] : 156 -> 148
~ +[SAMLIDPEntry createElement:] : 124 -> 120
~ -[SAMLIDPEntry providerId] : 96 -> 88
~ -[SAMLIDPEntry name] : 96 -> 88
~ -[SAMLIDPEntry loc] : 96 -> 88
~ -[SAMLDSAKeyValue p] : 156 -> 148
~ -[SAMLDSAKeyValue q] : 156 -> 148
~ -[SAMLDSAKeyValue g] : 156 -> 148
~ -[SAMLDSAKeyValue y] : 156 -> 148
~ -[SAMLDSAKeyValue j] : 156 -> 148
~ -[SAMLDSAKeyValue seed] : 156 -> 148
~ -[SAMLDSAKeyValue pgenCounter] : 156 -> 148
~ -[XMLWrapperSchema initWithSchemaData:] : 356 -> 352
~ _XMLWExternalEntityLoader : 488 -> 448
~ _XMLWSchemaValidityError : 140 -> 136
~ _XMLWSchemaValidityWarning : 140 -> 136
~ -[XMLWrapperSchema validateDocument:error:] : 568 -> 548
~ _XMLWSchemaValidityErrorFunc : 272 -> 256
~ -[SAMLX509Data issuerName] : 144 -> 132
~ -[SAMLX509Data serialNumber] : 212 -> 196
~ -[SAMLX509Data ski] : 156 -> 148
~ -[SAMLX509Data subjectName] : 108 -> 100
~ -[SAMLX509Data certificate] : 156 -> 148
~ -[SAMLX509Data crl] : 156 -> 148
~ +[SAMLAttributeQueryElement createElement:] : 604 -> 580
~ -[SAMLAttributeQueryElement identifier] : 112 -> 104
~ -[SAMLAttributeQueryElement issueInstant] : 140 -> 128
~ -[SAMLAttributeQueryElement destination] : 96 -> 88
~ -[SAMLAttributeQueryElement consent] : 96 -> 88
~ -[SAMLAttributeQueryElement channelId] : 112 -> 104
~ -[SAMLAttributeQueryElement setChannelId:] : 324 -> 312
~ -[SAMLAttributeQueryElement setSubject:] : 156 -> 152
~ -[SAMLAttributeQueryElement samlAttributes] : 308 -> 304
~ +[SAMLEvidence createElement:] : 124 -> 120
~ -[SAMLEvidence assertionIdRef] : 112 -> 104
~ -[SAMLEvidence assertionURIRef] : 112 -> 104
~ -[XMLWrapperElement initWithNode:doc:query:error:] : 872 -> 820
~ -[XMLWrapperElement initWithTagName:error:] : 228 -> 216
~ -[XMLWrapperElement elements] : 56 -> 8
~ -[XMLWrapperElement setElements:] : 76 -> 72
~ -[XMLWrapperElement attributes] : 56 -> 8
~ -[XMLWrapperElement setNamespace:] : 152 -> 140
~ -[XMLWrapperElement firstElementByTagName:] : 84 -> 76
~ -[XMLWrapperElement getElementsByTagName:] : 368 -> 360
~ -[XMLWrapperElement addChildElement:] : 120 -> 116
~ -[XMLWrapperElement replaceChildElement:newElement:] : 152 -> 156
~ -[XMLWrapperElement firstResultByXpathQuery:] : 84 -> 76
~ -[XMLWrapperElement getResultsByXpathQuery:] : 184 -> 180
~ -[XMLWrapperElement reorderChildElements] : 324 -> 316
~ -[XMLWrapperElement xmlNode:] : 788 -> 772
~ -[XMLWrapperElement setTagName:] : 64 -> 12
~ -[XMLWrapperElement setTextContent:] : 64 -> 12
~ -[XMLWrapperElement setChildElementSequence:] : 64 -> 12
~ -[XMLWrapperElement setQuery:] : 64 -> 12
~ -[SAMLAuthZDecisionQuery initWithData:schema:error:] : 232 -> 220
~ -[SAMLAuthZDecisionQuery channelId] : 84 -> 76
~ -[SAMLAuthZDecisionQuery setSubjectFromResponse:] : 216 -> 200
~ -[SAMLAuthZDecisionQuery addAction:] : 100 -> 96
~ -[SAMLAuthZDecisionQuery setResource:] : 128 -> 120
~ -[SAMLAuthZDecisionQuery requestElement] : 16 -> 20
~ -[SAMLAuthZDecisionQuery setRequestElement:] : 80 -> 20
~ -[XMLWrapperAttribute initWithNode:error:] : 260 -> 252
~ -[XMLWrapperAttribute xmlAttrNodeForNode:error:] : 336 -> 312
~ -[XMLWrapperAttribute setName:] : 64 -> 12
~ -[XMLWrapperAttribute setValue:] : 64 -> 12
~ -[XMLWrapperAttribute setNs:] : 64 -> 12
~ -[SAMLRSAKeyValue modulus] : 156 -> 148
~ -[SAMLRSAKeyValue exponent] : 156 -> 148
~ +[SAMLScoping createElement:] : 252 -> 244
~ -[SAMLScoping proxyCount] : 176 -> 164
~ -[SAMLScoping requesterIds] : 344 -> 336
~ -[SAMLScoping getComplete] : 168 -> 156
~ -[SAMLScoping idpList] : 356 -> 348
~ -[SAMLResponse initWithData:schema:error:] : 232 -> 220
~ -[SAMLResponse assertions] : 84 -> 76
~ -[SAMLResponse attributes] : 432 -> 408
~ -[SAMLResponse attributeValuesForName:] : 116 -> 108
~ -[SAMLResponse selectedProvider] : 84 -> 76
~ -[SAMLResponse subject] : 308 -> 300
~ -[SAMLResponse userName] : 92 -> 84
~ -[SAMLResponse authenticationTTL] : 120 -> 108
~ -[SAMLResponse setAuthenticationTTL:] : 164 -> 152
~ -[SAMLResponse authenticationSessionId] : 120 -> 108
~ -[SAMLResponse assertionMeetsConditions:] : 68 -> 64
~ -[SAMLResponse isValid:] : 672 -> 644
~ -[SAMLResponse statusCodes] : 248 -> 220
~ -[SAMLResponse primaryStatusCode] : 84 -> 76
~ -[SAMLResponse expectedAction] : 280 -> 268
~ -[SAMLResponse authorizationStatusForResource:] : 328 -> 320
~ -[SAMLResponse responseElement] : 16 -> 20
~ -[SAMLResponse setResponseElement:] : 80 -> 20
~ +[SAMLNameIdPolicy createElement:] : 184 -> 180
~ -[SAMLNameIdPolicy format] : 96 -> 88
~ -[SAMLNameIdPolicy allowCreation] : 96 -> 88
~ +[SAMLParserController sharedInstance] : 176 -> 160
~ -[SAMLParserController init] : 184 -> 172
~ -[SAMLParserController schema] : 56 -> 8
~ -[SAMLParserController newAttributeQuery:error:] : 168 -> 160
~ -[SAMLParserController newAuthNRequest:error:] : 168 -> 160
~ -[SAMLParserController newAuthZQuery:channelId:error:] : 200 -> 196
~ -[SAMLParserController newLogoutRequest:] : 140 -> 132
~ -[SAMLParserController parseResponse:error:] : 164 -> 160
~ -[SAMLParserController parseCachedResponse:error:] : 148 -> 144
~ -[SAMLParserController dataFromString:error:] : 108 -> 100
~ -[SAMLParserController setSchemaData:] : 64 -> 12
~ +[SAMLAuthNRequestElement createElement:] : 628 -> 600
~ -[SAMLAuthNRequestElement identifier] : 96 -> 88
~ -[SAMLAuthNRequestElement issueInstant] : 124 -> 112
~ -[SAMLAuthNRequestElement destination] : 96 -> 88
~ -[SAMLAuthNRequestElement consent] : 96 -> 88
~ -[SAMLAuthNRequestElement forceAuthN] : 116 -> 108
~ -[SAMLAuthNRequestElement setForceAuthN:] : 108 -> 104
~ -[SAMLAuthNRequestElement isPassive] : 116 -> 108
~ -[SAMLAuthNRequestElement setIsPassive:] : 108 -> 104
~ -[SAMLAuthNRequestElement providerName] : 96 -> 88
~ -[SAMLAuthNRequestElement issuer] : 112 -> 104
~ -[SAMLAuthNRequestElement setIssuer:] : 324 -> 312
~ +[SAMLRequestedAuthNContext createElement:] : 124 -> 120
~ -[SAMLRequestedAuthNContext comparison] : 92 -> 84
~ -[SAMLRequestedAuthNContext classRef] : 108 -> 100
~ -[SAMLRequestedAuthNContext declRef] : 108 -> 100
~ -[SAMLSignatureReference identifier] : 96 -> 88
~ -[SAMLSignatureReference uri] : 96 -> 88
~ -[SAMLSignatureReference type] : 96 -> 88
~ -[SAMLSignatureReference transforms] : 428 -> 412
~ -[SAMLSignatureReference digestMethod] : 152 -> 140
~ -[SAMLSignatureReference digestValue] : 160 -> 152
~ +[SAMLSignature createElement:] : 268 -> 260
~ -[SAMLSignature identifier] : 96 -> 88
~ -[SAMLSignature signatureValue] : 160 -> 152
~ -[SAMLSignature signatureValueId] : 152 -> 140
~ +[SAMLAuthZDecision createElement:] : 124 -> 120
~ -[SAMLAuthZDecision decision] : 96 -> 88
~ -[SAMLAuthZDecision resource] : 96 -> 88
~ -[SAMLAuthNRequest initWithData:schema:error:] : 296 -> 284
~ -[SAMLAuthNRequest issuer] : 84 -> 76
~ -[SAMLAuthNRequest setIssuer:] : 100 -> 96
~ -[SAMLAuthNRequest setSubjectFromResponse:] : 188 -> 180
~ -[SAMLAuthNRequest setIsPassive:] : 84 -> 80
~ -[SAMLAuthNRequest setForceAuthN:] : 84 -> 80
~ -[SAMLAuthNRequest setProviderName:] : 100 -> 96
~ -[SAMLAuthNRequest requestElement] : 16 -> 20
~ -[SAMLAuthNRequest setRequestElement:] : 80 -> 20
~ -[SAMLKeyRetrievalMethod uri] : 96 -> 88
~ -[SAMLKeyRetrievalMethod type] : 96 -> 88
~ -[SAMLKeyRetrievalMethod transforms] : 428 -> 412
~ +[SAMLBaseElement createElement:] : 68 -> 64
~ +[XMLWrapperElementFactory sharedInstance] : 176 -> 160
~ +[XMLWrapperElementFactory registerClass:forElementName:] : 104 -> 112
~ -[XMLWrapperElementFactory classForXMLNode:error:] : 164 -> 156
~ +[XMLWrapperElementFactory elementTypeByTagName:] : 68 -> 64
~ +[SAMLAdvice createElement:] : 124 -> 120
~ -[SAMLAdvice assertionIDRef] : 112 -> 104
~ -[SAMLAdvice assertionURIRef] : 112 -> 104
~ +[SAMLResponseElement createElement:] : 124 -> 120
~ -[SAMLResponseElement identifier] : 112 -> 104
~ -[SAMLResponseElement relatedRequest] : 96 -> 88
~ -[SAMLResponseElement issueInstant] : 140 -> 128
~ -[SAMLResponseElement destination] : 96 -> 88
~ -[SAMLResponseElement consent] : 96 -> 88
~ -[SAMLResponseElement issuer] : 112 -> 104
~ -[SAMLResponseElement assertions] : 308 -> 304
~ -[SAMLResponseElement authnStatement] : 316 -> 308
~ -[XMLWrapperQuery elementForNode:] : 164 -> 160
~ -[XMLWrapperQuery searchNodeWithXpathQuery:query:error:] : 84 -> 80
~ -[XMLWrapperQuery registerNamespace:] : 172 -> 164
~ -[XMLWrapperQuery registerXpathNamespacesForCtx:error:] : 468 -> 460
~ -[XMLWrapperQuery executeXpathQuery:query:ctxNode:error:] : 620 -> 608
~ +[SAMLAssertion createElement:] : 336 -> 328
~ -[SAMLAssertion identifier] : 112 -> 104
~ -[SAMLAssertion issueInstant] : 140 -> 128
~ -[SAMLAssertion issuer] : 112 -> 104
~ -[SAMLAssertion samlAttributes] : 356 -> 348
~ -[SAMLAssertion authorizations] : 308 -> 304
~ -[SAMLAssertion isValid:] : 248 -> 228
~ -[SAMLAssertion meetsConditions:] : 68 -> 64
~ -[SAMLAssertion isValidForRequestor:] : 316 -> 312
~ -[SAMLAssertion authorizationForResource:] : 356 -> 348
~ -[SAMLAttributeQuery initWithData:schema:error:] : 320 -> 308
~ -[SAMLAttributeQuery channelId] : 84 -> 76
~ -[SAMLAttributeQuery setSubjectFromResponse:] : 188 -> 180
~ -[SAMLAttributeQuery requestElement] : 16 -> 20
~ -[SAMLAttributeQuery setRequestElement:] : 80 -> 20
~ +[SAMLKeyInfo createElement:] : 124 -> 120
~ -[SAMLKeyInfo identifier] : 96 -> 88
~ -[SAMLKeyInfo keyName] : 112 -> 104
~ -[SAMLKeyInfo spkiSexpData] : 204 -> 192
~ -[SAMLKeyInfo mgmtData] : 112 -> 104
~ -[XMLWrapperDoc initWithData:schema:error:] : 256 -> 252
~ -[XMLWrapperDoc initWithElement:schema:error:] : 144 -> 152
~ -[XMLWrapperDoc setNamespace:] : 152 -> 140
~ -[XMLWrapperDoc getResultsByXpathQuery:error:] : 128 -> 120
~ -[XMLWrapperDoc firstResultByXpathQuery:error:] : 100 -> 92
~ -[XMLWrapperDoc docNode:] : 244 -> 240
~ -[XMLWrapperDoc query] : 56 -> 8
~ -[XMLWrapperDoc createDocument:] : 376 -> 360
~ -[XMLWrapperDoc setXMLDoc:] : 188 -> 180
~ -[XMLWrapperDoc createDocumentElement:] : 144 -> 140
~ -[XMLWrapperDoc setXmlData:] : 64 -> 12
~ -[XMLWrapperDoc setSchemaData:] : 64 -> 12
~ -[XMLWrapperDoc setDocumentElement:] : 64 -> 12
~ -[XMLWrapperDoc setQuery:] : 64 -> 12
~ +[SAMLAttribute createElement:] : 124 -> 120
~ -[SAMLAttribute name] : 96 -> 88
~ -[SAMLAttribute nameFormat] : 96 -> 88
~ -[SAMLAttribute friendlyName] : 96 -> 88
~ -[SAMLAttribute values] : 344 -> 336
~ +[SAMLSignedInfo createElement:] : 124 -> 120
~ -[SAMLSignedInfo xmlNode:] : 640 -> 628
~ -[SAMLSignedInfo identifier] : 96 -> 88
~ -[SAMLSignedInfo canonicalizationMethod] : 152 -> 140
~ -[SAMLSignedInfo signatureMethodLength] : 220 -> 204
~ -[SAMLSignedInfo signatureMethod] : 152 -> 140
~ -[SAMLSignedInfo references] : 308 -> 304
~ +[SAMLSubjectConfirmation createElement:] : 124 -> 120
~ -[SAMLSubjectConfirmation xmlNode:] : 580 -> 572
~ -[SAMLSubjectConfirmation method] : 96 -> 88
~ -[SAMLSubjectConfirmation notBefore] : 188 -> 172
~ -[SAMLSubjectConfirmation notOnOrAfter] : 188 -> 172
~ -[SAMLSubjectConfirmation recipient] : 152 -> 140
~ -[SAMLSubjectConfirmation inResponseTo] : 152 -> 140
~ -[SAMLSubjectConfirmation address] : 152 -> 140
~ +[NSBundle(SAMLAdditions) saml_frameworkBundle] : 84 -> 68
~ ___47+[NSBundle(SAMLAdditions) saml_frameworkBundle]_block_invoke : 76 -> 72
~ -[XMLWrapperNamespace initWithNsNode:error:] : 180 -> 172
~ -[XMLWrapperNamespace xmlNsForNode:error:] : 284 -> 264
~ -[XMLWrapperNamespace setHref:] : 64 -> 12
~ -[XMLWrapperNamespace setPrefix:] : 64 -> 12
~ +[SAMLStatus createElement:] : 124 -> 120
~ -[SAMLStatus statusMessage] : 108 -> 100
~ -[SAMLStatus statusDetail] : 108 -> 100
~ -[SAMLStatus status] : 84 -> 76
~ +[SAMLStatusCode createElement:] : 124 -> 120
~ -[SAMLStatusCode value] : 96 -> 88
~ +[SAMLAuthZDecisionQueryElement createElement:] : 520 -> 492
~ -[SAMLAuthZDecisionQueryElement identifier] : 112 -> 104
~ -[SAMLAuthZDecisionQueryElement destination] : 96 -> 88
~ -[SAMLAuthZDecisionQueryElement issueInstant] : 140 -> 128
~ -[SAMLAuthZDecisionQueryElement consent] : 96 -> 88
~ -[SAMLAuthZDecisionQueryElement resource] : 96 -> 88
~ -[SAMLAuthZDecisionQueryElement channelId] : 112 -> 104
~ -[SAMLAuthZDecisionQueryElement setChannelId:] : 324 -> 312
~ -[SAMLAuthZDecisionQueryElement addAction:] : 204 -> 200
~ -[SAMLAuthZDecisionQueryElement setEvidence:] : 156 -> 152
~ +[SAMLAuthNStatement createElement:] : 328 -> 320
~ -[SAMLAuthNStatement authnInstant] : 140 -> 128
~ -[SAMLAuthNStatement sessionIndex] : 96 -> 88
~ -[SAMLAuthNStatement sessionNotOnOrAfter] : 140 -> 128
~ -[SAMLAuthNStatement subjectAddress] : 152 -> 140
~ -[SAMLAuthNStatement subjectDNSName] : 152 -> 140
~ -[SAMLAuthNStatement authnContextDecl] : 152 -> 140
~ -[SAMLAuthNStatement authnContextDeclRef] : 152 -> 140
~ -[SAMLAuthNStatement authnContextClassRef] : 152 -> 140
~ -[SAMLAuthNStatement authenticatingAuthority] : 152 -> 140
~ -[SAMLAuthNStatement isValid] : 108 -> 100
~ +[SAMLSubject createElement:] : 252 -> 244
~ -[SAMLSubject subjectConfirmations] : 308 -> 304
~ -[SAMLLogoutRequest initWithData:schema:error:] : 296 -> 284
~ -[SAMLLogoutRequest issuer] : 84 -> 76
~ -[SAMLLogoutRequest setIssuer:] : 100 -> 96
~ -[SAMLLogoutRequest reason] : 84 -> 76
~ -[SAMLLogoutRequest setReason:] : 100 -> 96
~ -[SAMLLogoutRequest notOnOrAfter] : 84 -> 76
~ -[SAMLLogoutRequest setNotOnOrAfter:] : 100 -> 96
~ -[SAMLLogoutRequest requestElement] : 16 -> 20
~ -[SAMLLogoutRequest setRequestElement:] : 80 -> 20
~ +[SAMLLogoutRequestElement createElement:] : 472 -> 448
~ -[SAMLLogoutRequestElement identifier] : 112 -> 104
~ -[SAMLLogoutRequestElement destination] : 96 -> 88
~ -[SAMLLogoutRequestElement issueInstant] : 124 -> 112
~ -[SAMLLogoutRequestElement consent] : 96 -> 88
~ -[SAMLLogoutRequestElement reason] : 96 -> 88
~ -[SAMLLogoutRequestElement notOnOrAfter] : 124 -> 112
~ -[SAMLLogoutRequestElement setNotOnOrAfter:] : 104 -> 100
~ -[SAMLLogoutRequestElement issuer] : 112 -> 104
~ -[SAMLLogoutRequestElement setIssuer:] : 324 -> 312
~ -[SAMLLogoutRequestElement sessionIndex] : 112 -> 104
~ -[SAMLLogoutRequestElement setSessionIndex:] : 196 -> 192
CStrings:
- "#24@0:8@16"
- "#32@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16^@24"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"SAMLAttributeQueryElement\""
- "@\"SAMLAuthNRequestElement\""
- "@\"SAMLAuthZDecisionQueryElement\""
- "@\"SAMLLogoutRequestElement\""
- "@\"SAMLResponseElement\""
- "@\"XMLWrapperElement\""
- "@\"XMLWrapperNamespace\""
- "@\"XMLWrapperQuery\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16"
- "@32@0:8@16^@24"
- "@32@0:8^{_xmlAttr=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlAttr}^{_xmlAttr}^{_xmlDoc}^{_xmlNs}i^v}16^@24"
- "@32@0:8^{_xmlNs=^{_xmlNs}i**^v^{_xmlDoc}}16^@24"
- "@40@0:8@16@24^@32"
- "@40@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16@24^@32"
- "@48@0:8^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}16@24^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}32^@40"
- "@48@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}24@32^@40"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}16^@24"
- "B32@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16^@24"
- "B32@0:8^{_xmlXPathContext=^{_xmlDoc}^{_xmlNode}ii^{_xmlHashTable}ii^{_xmlXPathType}ii^{_xmlHashTable}ii^{_xmlXPathAxis}^^{_xmlNs}i^viii^{_xmlNode}^{_xmlNode}^{_xmlHashTable}^?^v^v**^?^v^^{_xmlNs}i^v^?{_xmlError=ii*i*i***ii^v^v}^{_xmlNode}^{_xmlDict}i^vQQi}16^@24"
- "Q24@0:8@16"
- "SAMLAdditions"
- "SAMLAdvice"
- "SAMLAssertion"
- "SAMLAttribute"
- "SAMLAttributeQuery"
- "SAMLAttributeQueryElement"
- "SAMLAuthNRequest"
- "SAMLAuthNRequestElement"
- "SAMLAuthNStatement"
- "SAMLAuthZDecision"
- "SAMLAuthZDecisionQuery"
- "SAMLAuthZDecisionQueryElement"
- "SAMLBaseElement"
- "SAMLConditions"
- "SAMLDSAKeyValue"
- "SAMLEvidence"
- "SAMLIDPEntry"
- "SAMLKeyInfo"
- "SAMLKeyRetrievalMethod"
- "SAMLLogoutRequest"
- "SAMLLogoutRequestElement"
- "SAMLLogoutResponseElement"
- "SAMLNameId"
- "SAMLNameIdPolicy"
- "SAMLPGPData"
- "SAMLParserController"
- "SAMLRSAKeyValue"
- "SAMLRequestedAuthNContext"
- "SAMLResponse"
- "SAMLResponseElement"
- "SAMLScoping"
- "SAMLSignature"
- "SAMLSignatureKeyValue"
- "SAMLSignatureReference"
- "SAMLSignedInfo"
- "SAMLStatus"
- "SAMLStatusCode"
- "SAMLSubject"
- "SAMLSubjectConfirmation"
- "SAMLX509Data"
- "T@\"NSArray\",&,N,V_childElementSequence"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_conditions"
- "T@\"NSData\",&,N,V_schemaData"
- "T@\"NSData\",&,N,V_xmlData"
- "T@\"NSData\",R,N"
- "T@\"NSDate\",&,N"
- "T@\"NSDate\",C,N"
- "T@\"NSDate\",R,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_namespaces"
- "T@\"NSNumber\",R,N"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_href"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_prefix"
- "T@\"NSString\",&,N,V_tagName"
- "T@\"NSString\",&,N,V_textContent"
- "T@\"NSString\",&,N,V_value"
- "T@\"NSString\",C,N"
- "T@\"NSString\",R,N"
- "T@\"SAMLAdvice\",R,N"
- "T@\"SAMLAssertion\",&,N"
- "T@\"SAMLAssertion\",R,N"
- "T@\"SAMLAttributeQueryElement\",&,N,V_requestElement"
- "T@\"SAMLAuthNRequestElement\",&,N,V_requestElement"
- "T@\"SAMLAuthNStatement\",R,N"
- "T@\"SAMLAuthZDecisionQueryElement\",&,N,V_requestElement"
- "T@\"SAMLConditions\",&,N"
- "T@\"SAMLConditions\",R,N"
- "T@\"SAMLDSAKeyValue\",R,N"
- "T@\"SAMLEvidence\",&,N"
- "T@\"SAMLEvidence\",R,N"
- "T@\"SAMLKeyInfo\",R,N"
- "T@\"SAMLKeyRetrievalMethod\",R,N"
- "T@\"SAMLLogoutRequestElement\",&,N,V_requestElement"
- "T@\"SAMLNameId\",R,N"
- "T@\"SAMLNameIdPolicy\",&,N"
- "T@\"SAMLPGPData\",R,N"
- "T@\"SAMLRSAKeyValue\",R,N"
- "T@\"SAMLRequestedAuthNContext\",R,N"
- "T@\"SAMLResponseElement\",&,N,V_responseElement"
- "T@\"SAMLScoping\",&,N"
- "T@\"SAMLSignature\",R,N"
- "T@\"SAMLSignatureKeyValue\",R,N"
- "T@\"SAMLSignedInfo\",R,N"
- "T@\"SAMLStatus\",R,N"
- "T@\"SAMLStatusCode\",R,N"
- "T@\"SAMLSubject\",&,N"
- "T@\"SAMLSubject\",R,N"
- "T@\"SAMLX509Data\",R,N"
- "T@\"XMLWrapperElement\",&,N,V_documentElement"
- "T@\"XMLWrapperNamespace\",&,N,V_ns"
- "T@\"XMLWrapperQuery\",&,N,V_query"
- "TB,N"
- "TB,R,N"
- "Ti,N,V_type"
- "URLForResource:withExtension:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "XMLWrapperAttribute"
- "XMLWrapperDoc"
- "XMLWrapperElement"
- "XMLWrapperElementFactory"
- "XMLWrapperNamespace"
- "XMLWrapperQuery"
- "XMLWrapperSchema"
- "^{_xmlAttr=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlAttr}^{_xmlAttr}^{_xmlDoc}^{_xmlNs}i^v}"
- "^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}"
- "^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}16@0:8"
- "^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}24@0:8^@16"
- "^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}"
- "^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16@0:8"
- "^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}24@0:8^@16"
- "^{_xmlNs=^{_xmlNs}i**^v^{_xmlDoc}}"
- "^{_xmlNs=^{_xmlNs}i**^v^{_xmlDoc}}32@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16^@24"
- "^{_xmlSchema=}"
- "_attributeNode"
- "_attributes"
- "_childElementSequence"
- "_conditions"
- "_doc"
- "_docNode"
- "_documentElement"
- "_elements"
- "_href"
- "_name"
- "_namespaces"
- "_ns"
- "_ownsXMLNode"
- "_prefix"
- "_query"
- "_requestElement"
- "_responseElement"
- "_schemaData"
- "_schemaPtr"
- "_tagName"
- "_textContent"
- "_type"
- "_value"
- "_xmlData"
- "_xmlNode"
- "_xmlNs"
- "absoluteString"
- "actions"
- "addAction:"
- "addAttribute:"
- "addAttribute:values:"
- "addAttributeValue:"
- "addChildElement:"
- "addChildElement:before:"
- "addObject:"
- "addObjectsFromArray:"
- "addRequesterId:"
- "address"
- "advice"
- "allowCreation"
- "appendString:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "assertion"
- "assertionIDRef"
- "assertionIdRef"
- "assertionMeetsConditions:"
- "assertionURIRef"
- "assertions"
- "attributeValuesForName:"
- "attributeWithName:"
- "attributes"
- "audienceRestrictions"
- "authenticatingAuthority"
- "authentication"
- "authenticationSessionId"
- "authenticationTTL"
- "authnContextClassRef"
- "authnContextDecl"
- "authnContextDeclRef"
- "authnInstant"
- "authnStatement"
- "authorizationForResource:"
- "authorizationStatusForResource:"
- "authorizations"
- "bundleForClass:"
- "bundleWithIdentifier:"
- "bytes"
- "canonicalizationMethod"
- "certificate"
- "channelId"
- "childElementSequence"
- "classForXMLNode:error:"
- "classRef"
- "comparison"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conditions"
- "consent"
- "context"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDocument:"
- "createDocumentElement:"
- "createElement:"
- "crl"
- "dataFromString:error:"
- "dataUsingEncoding:"
- "dataWithContentsOfURL:"
- "date"
- "dateFromString:"
- "dealloc"
- "decision"
- "declRef"
- "destination"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "digestMethod"
- "digestValue"
- "docNode:"
- "docPtr"
- "documentElement"
- "dsaKeyValue"
- "elementClassByTagName:"
- "elementForNode:"
- "elementTypeByTagName:"
- "elements"
- "errorWithDomain:code:userInfo:"
- "evidence"
- "executeXpathQuery:query:ctxNode:error:"
- "expectedAction"
- "exponent"
- "firstElementByTagName:"
- "firstObject"
- "firstResultByXpathQuery:"
- "firstResultByXpathQuery:error:"
- "forceAuthN"
- "format"
- "friendlyName"
- "g"
- "getComplete"
- "getElementsByTagName:"
- "getResultsByXpathQuery:"
- "getResultsByXpathQuery:error:"
- "hasValidAuthentication"
- "href"
- "i"
- "i16@0:8"
- "identifier"
- "idpList"
- "inResponseTo"
- "indexOfObject:"
- "init"
- "initWithBase64EncodedString:options:"
- "initWithBytes:length:encoding:"
- "initWithData:schema:error:"
- "initWithDomain:code:userInfo:"
- "initWithElement:schema:error:"
- "initWithFormat:arguments:"
- "initWithNode:doc:query:error:"
- "initWithNode:error:"
- "initWithNsNode:error:"
- "initWithSchemaData:"
- "initWithTagName:error:"
- "initialize"
- "insertObject:atIndex:"
- "isEqual:"
- "isEqualToString:"
- "isMemberOfClass:"
- "isPassive"
- "isValid"
- "isValid:"
- "isValidForRequestor:"
- "issueInstant"
- "issuer"
- "issuerName"
- "j"
- "keyId"
- "keyInfo"
- "keyName"
- "keyValue"
- "lastObject"
- "lastPathComponent"
- "length"
- "loc"
- "localeWithLocaleIdentifier:"
- "meetsConditions:"
- "method"
- "mgmtData"
- "modulus"
- "mutableCopy"
- "name"
- "nameFormat"
- "nameId"
- "nameIdPolicy"
- "nameQualifier"
- "namespaces"
- "newAttributeQuery:error:"
- "newAuthNRequest:error:"
- "newAuthZQuery:channelId:error:"
- "newLogoutRequest:"
- "nodePtr"
- "notBefore"
- "notOnOrAfter"
- "ns"
- "numberFromString:"
- "objectAtIndex:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "oneTimeUse"
- "p"
- "packet"
- "parseCachedResponse:error:"
- "parseResponse:error:"
- "pgenCounter"
- "pgpData"
- "prefix"
- "primaryStatusCode"
- "providerId"
- "providerName"
- "proxyCount"
- "proxyRestrictionAudienceCount"
- "proxyRestrictions"
- "q"
- "q16@0:8"
- "query"
- "reason"
- "recipient"
- "references"
- "registerClass:forElementName:"
- "registerNamespace:"
- "registerXpathNamespacesForCtx:error:"
- "relatedRequest"
- "removeChildElement:"
- "removeLastObject"
- "removeObject:"
- "reorderChildElements"
- "replaceChildElement:newElement:"
- "replaceObjectAtIndex:withObject:"
- "requestElement"
- "requesterIds"
- "resource"
- "responseElement"
- "retrievalMethod"
- "rsaKeyValue"
- "samlAttributes"
- "saml_frameworkBundle"
- "schema"
- "schemaData"
- "scoping"
- "searchNodeWithXpathQuery:query:error:"
- "seed"
- "selectedProvider"
- "serialNumber"
- "sessionIndex"
- "sessionNotOnOrAfter"
- "setAssertion:"
- "setAssertionIDRef:"
- "setAssertionURIRef:"
- "setAttributeWithName:value:"
- "setAuthenticationTTL:"
- "setChannelId:"
- "setChildElementSequence:"
- "setConditions:"
- "setDateFormat:"
- "setDestination:"
- "setDocumentElement:"
- "setElementProperties"
- "setElements:"
- "setEvidence:"
- "setForceAuthN:"
- "setHref:"
- "setIsPassive:"
- "setIssuer:"
- "setLocale:"
- "setName:"
- "setNameIdPolicy:"
- "setNamespace:"
- "setNotOnOrAfter:"
- "setNs:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setPrefix:"
- "setProviderName:"
- "setQuery:"
- "setReason:"
- "setRequestElement:"
- "setResource:"
- "setResponseElement:"
- "setSchemaData:"
- "setScoping:"
- "setSessionIndex:"
- "setSubject:"
- "setSubjectFromResponse:"
- "setTagName:"
- "setTextContent:"
- "setTimeZone:"
- "setType:"
- "setValue:"
- "setXMLDoc:"
- "setXmlData:"
- "sharedInstance"
- "signature"
- "signatureMethod"
- "signatureMethodLength"
- "signatureValue"
- "signatureValueId"
- "signedInfo"
- "ski"
- "spNameQualifier"
- "spProvidedId"
- "spkiSexpData"
- "status"
- "statusCode"
- "statusCodes"
- "statusDetail"
- "statusMessage"
- "string"
- "stringByAppendingString:"
- "stringByTrimmingCharactersInSet:"
- "stringFromDate:"
- "stringWithCString:encoding:"
- "stringWithContentsOfURL:encoding:error:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subject"
- "subjectAddress"
- "subjectConfirmations"
- "subjectDNSName"
- "subjectName"
- "tagName"
- "textContent"
- "timeZoneForSecondsFromGMT:"
- "transforms"
- "type"
- "unsignedIntegerValue"
- "uri"
- "userName"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v32@0:8#16@24"
- "v32@0:8@16@24"
- "validateDocument:error:"
- "value"
- "values"
- "vs_isAfter:"
- "vs_isBefore:"
- "vs_trueFalseStringValueFromBool:"
- "whitespaceAndNewlineCharacterSet"
- "x509Data"
- "xmlAttrNodeForNode:error:"
- "xmlData"
- "xmlNode:"
- "xmlNsForNode:error:"
- "xmlString:"
- "y"

```
