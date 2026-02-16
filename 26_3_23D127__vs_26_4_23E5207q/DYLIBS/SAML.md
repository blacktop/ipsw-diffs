## SAML

> `/System/Library/PrivateFrameworks/SAML.framework/SAML`

```diff

-593.30.1.0.0
-  __TEXT.__text: 0xd6b4
-  __TEXT.__auth_stubs: 0x530
+593.40.5.0.0
+  __TEXT.__text: 0xe5cc
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0x1674
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x112b
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x440
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__unwind_info: 0x4b0
   __TEXT.__objc_classname: 0x34e
   __TEXT.__objc_methname: 0x19b4
   __TEXT.__objc_methtype: 0xc77

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9c0
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1a20
   __AUTH_CONST.__objc_const: 0x2c98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 380B0CA3-3B74-395F-BB31-7EE773F4E68D
+  UUID: 98247BEB-1AFF-3BD0-9729-7A3B792BE227
   Functions: 426
-  Symbols:   1686
+  Symbols:   1683
   CStrings:  916
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x23
- _objc_retain_x8
Functions:
~ +[SAMLNameId createElement:] : 120 -> 124
~ -[SAMLNameId nameQualifier] : 88 -> 96
~ -[SAMLNameId spNameQualifier] : 88 -> 96
~ -[SAMLNameId format] : 88 -> 96
~ -[SAMLNameId spProvidedId] : 88 -> 96
~ +[SAMLConditions createElement:] : 260 -> 268
~ -[SAMLConditions notBefore] : 128 -> 140
~ -[SAMLConditions notOnOrAfter] : 128 -> 140
~ -[SAMLConditions audienceRestrictions] : 368 -> 384
~ -[SAMLConditions oneTimeUse] : 64 -> 68
~ -[SAMLConditions proxyRestrictions] : 324 -> 336
~ -[SAMLConditions proxyRestrictionAudienceCount] : 204 -> 220
~ -[SAMLConditions assertionMeetsConditions:] : 204 -> 220
~ _SAMLParserErrorForErrorCode : 124 -> 128
~ _SAMLErrorInfoForParserErrorCode : 380 -> 384
~ _SAMLInvalidDocumentElementErrorForClass : 188 -> 200
~ _SAMLStringFromDate : 100 -> 108
~ _SAMLDateFormatter : 164 -> 172
~ _SAMLDateFromString : 100 -> 108
~ -[SAMLPGPData keyId] : 148 -> 156
~ -[SAMLPGPData packet] : 148 -> 156
~ +[SAMLIDPEntry createElement:] : 120 -> 124
~ -[SAMLIDPEntry providerId] : 88 -> 96
~ -[SAMLIDPEntry name] : 88 -> 96
~ -[SAMLIDPEntry loc] : 88 -> 96
~ -[SAMLDSAKeyValue p] : 148 -> 156
~ -[SAMLDSAKeyValue q] : 148 -> 156
~ -[SAMLDSAKeyValue g] : 148 -> 156
~ -[SAMLDSAKeyValue y] : 148 -> 156
~ -[SAMLDSAKeyValue j] : 148 -> 156
~ -[SAMLDSAKeyValue seed] : 148 -> 156
~ -[SAMLDSAKeyValue pgenCounter] : 148 -> 156
~ -[XMLWrapperSchema initWithSchemaData:] : 352 -> 356
~ _XMLWExternalEntityLoader : 448 -> 488
~ _XMLWSchemaValidityError : 136 -> 140
~ _XMLWSchemaValidityWarning : 136 -> 140
~ -[XMLWrapperSchema validateDocument:error:] : 548 -> 568
~ _XMLWSchemaValidityErrorFunc : 256 -> 272
~ -[SAMLX509Data issuerName] : 132 -> 144
~ -[SAMLX509Data serialNumber] : 196 -> 212
~ -[SAMLX509Data ski] : 148 -> 156
~ -[SAMLX509Data subjectName] : 100 -> 108
~ -[SAMLX509Data certificate] : 148 -> 156
~ -[SAMLX509Data crl] : 148 -> 156
~ +[SAMLAttributeQueryElement createElement:] : 580 -> 604
~ -[SAMLAttributeQueryElement identifier] : 104 -> 112
~ -[SAMLAttributeQueryElement issueInstant] : 128 -> 140
~ -[SAMLAttributeQueryElement destination] : 88 -> 96
~ -[SAMLAttributeQueryElement consent] : 88 -> 96
~ -[SAMLAttributeQueryElement channelId] : 104 -> 112
~ -[SAMLAttributeQueryElement setChannelId:] : 312 -> 324
~ -[SAMLAttributeQueryElement setSubject:] : 152 -> 156
~ -[SAMLAttributeQueryElement samlAttributes] : 300 -> 308
~ +[SAMLEvidence createElement:] : 120 -> 124
~ -[SAMLEvidence assertionIdRef] : 104 -> 112
~ -[SAMLEvidence assertionURIRef] : 104 -> 112
~ -[XMLWrapperElement initWithNode:doc:query:error:] : 820 -> 872
~ -[XMLWrapperElement initWithTagName:error:] : 216 -> 228
~ -[XMLWrapperElement elements] : 8 -> 56
~ -[XMLWrapperElement setElements:] : 72 -> 76
~ -[XMLWrapperElement attributes] : 8 -> 56
~ -[XMLWrapperElement setNamespace:] : 140 -> 152
~ -[XMLWrapperElement firstElementByTagName:] : 76 -> 84
~ -[XMLWrapperElement getElementsByTagName:] : 356 -> 368
~ -[XMLWrapperElement addChildElement:] : 116 -> 120
~ -[XMLWrapperElement replaceChildElement:newElement:] : 156 -> 152
~ -[XMLWrapperElement firstResultByXpathQuery:] : 76 -> 84
~ -[XMLWrapperElement getResultsByXpathQuery:] : 180 -> 184
~ -[XMLWrapperElement reorderChildElements] : 312 -> 324
~ -[XMLWrapperElement xmlNode:] : 760 -> 788
~ -[XMLWrapperElement setTagName:] : 12 -> 64
~ -[XMLWrapperElement setTextContent:] : 12 -> 64
~ -[XMLWrapperElement setChildElementSequence:] : 12 -> 64
~ -[XMLWrapperElement setQuery:] : 12 -> 64
~ -[SAMLAuthZDecisionQuery initWithData:schema:error:] : 216 -> 232
~ -[SAMLAuthZDecisionQuery initWithElement:schema:error:] : 108 -> 112
~ -[SAMLAuthZDecisionQuery channelId] : 76 -> 84
~ -[SAMLAuthZDecisionQuery setSubjectFromResponse:] : 200 -> 216
~ -[SAMLAuthZDecisionQuery addAction:] : 96 -> 100
~ -[SAMLAuthZDecisionQuery setResource:] : 120 -> 128
~ -[SAMLAuthZDecisionQuery setRequestElement:] : 20 -> 80
~ -[XMLWrapperAttribute initWithNode:error:] : 252 -> 260
~ -[XMLWrapperAttribute xmlAttrNodeForNode:error:] : 312 -> 336
~ -[XMLWrapperAttribute setName:] : 12 -> 64
~ -[XMLWrapperAttribute setValue:] : 12 -> 64
~ -[XMLWrapperAttribute setNs:] : 12 -> 64
~ -[SAMLRSAKeyValue modulus] : 148 -> 156
~ -[SAMLRSAKeyValue exponent] : 148 -> 156
~ +[SAMLScoping createElement:] : 244 -> 252
~ -[SAMLScoping proxyCount] : 164 -> 176
~ -[SAMLScoping requesterIds] : 332 -> 344
~ -[SAMLScoping getComplete] : 156 -> 168
~ -[SAMLScoping idpList] : 344 -> 356
~ -[SAMLResponse initWithData:schema:error:] : 216 -> 232
~ -[SAMLResponse assertions] : 76 -> 84
~ -[SAMLResponse attributes] : 404 -> 432
~ -[SAMLResponse attributeValuesForName:] : 108 -> 116
~ -[SAMLResponse selectedProvider] : 76 -> 84
~ -[SAMLResponse subject] : 296 -> 308
~ -[SAMLResponse userName] : 84 -> 92
~ -[SAMLResponse hasValidAuthentication] : 348 -> 352
~ -[SAMLResponse authenticationTTL] : 108 -> 120
~ -[SAMLResponse setAuthenticationTTL:] : 152 -> 164
~ -[SAMLResponse authenticationSessionId] : 108 -> 120
~ -[SAMLResponse assertionMeetsConditions:] : 64 -> 68
~ -[SAMLResponse isValid:] : 640 -> 672
~ -[SAMLResponse statusCodes] : 220 -> 248
~ -[SAMLResponse primaryStatusCode] : 76 -> 84
~ -[SAMLResponse expectedAction] : 268 -> 280
~ -[SAMLResponse authorizationStatusForResource:] : 316 -> 328
~ -[SAMLResponse setResponseElement:] : 20 -> 80
~ +[SAMLNameIdPolicy createElement:] : 180 -> 184
~ -[SAMLNameIdPolicy format] : 88 -> 96
~ -[SAMLNameIdPolicy allowCreation] : 88 -> 96
~ +[SAMLParserController sharedInstance] : 160 -> 176
~ -[SAMLParserController init] : 172 -> 184
~ -[SAMLParserController schema] : 8 -> 56
~ -[SAMLParserController newAttributeQuery:error:] : 160 -> 168
~ -[SAMLParserController newAuthNRequest:error:] : 160 -> 168
~ -[SAMLParserController newAuthZQuery:channelId:error:] : 196 -> 200
~ -[SAMLParserController newLogoutRequest:] : 132 -> 140
~ -[SAMLParserController parseResponse:error:] : 160 -> 164
~ -[SAMLParserController parseCachedResponse:error:] : 144 -> 148
~ -[SAMLParserController dataFromString:error:] : 100 -> 108
~ -[SAMLParserController setSchemaData:] : 12 -> 64
~ +[SAMLAuthNRequestElement createElement:] : 600 -> 628
~ -[SAMLAuthNRequestElement identifier] : 88 -> 96
~ -[SAMLAuthNRequestElement issueInstant] : 112 -> 124
~ -[SAMLAuthNRequestElement destination] : 88 -> 96
~ -[SAMLAuthNRequestElement consent] : 88 -> 96
~ -[SAMLAuthNRequestElement forceAuthN] : 108 -> 116
~ -[SAMLAuthNRequestElement setForceAuthN:] : 104 -> 108
~ -[SAMLAuthNRequestElement isPassive] : 108 -> 116
~ -[SAMLAuthNRequestElement setIsPassive:] : 104 -> 108
~ -[SAMLAuthNRequestElement providerName] : 88 -> 96
~ -[SAMLAuthNRequestElement issuer] : 104 -> 112
~ -[SAMLAuthNRequestElement setIssuer:] : 312 -> 324
~ +[SAMLRequestedAuthNContext createElement:] : 120 -> 124
~ -[SAMLRequestedAuthNContext comparison] : 84 -> 92
~ -[SAMLRequestedAuthNContext classRef] : 100 -> 108
~ -[SAMLRequestedAuthNContext declRef] : 100 -> 108
~ -[SAMLSignatureReference identifier] : 88 -> 96
~ -[SAMLSignatureReference uri] : 88 -> 96
~ -[SAMLSignatureReference type] : 88 -> 96
~ -[SAMLSignatureReference transforms] : 408 -> 428
~ -[SAMLSignatureReference digestMethod] : 140 -> 152
~ -[SAMLSignatureReference digestValue] : 152 -> 160
~ +[SAMLSignature createElement:] : 260 -> 268
~ -[SAMLSignature identifier] : 88 -> 96
~ -[SAMLSignature signatureValue] : 152 -> 160
~ -[SAMLSignature signatureValueId] : 140 -> 152
~ +[SAMLAuthZDecision createElement:] : 120 -> 124
~ -[SAMLAuthZDecision decision] : 88 -> 96
~ -[SAMLAuthZDecision resource] : 88 -> 96
~ -[SAMLAuthNRequest initWithData:schema:error:] : 280 -> 296
~ -[SAMLAuthNRequest initWithElement:schema:error:] : 108 -> 112
~ -[SAMLAuthNRequest issuer] : 76 -> 84
~ -[SAMLAuthNRequest setIssuer:] : 96 -> 100
~ -[SAMLAuthNRequest setSubjectFromResponse:] : 176 -> 188
~ -[SAMLAuthNRequest setIsPassive:] : 80 -> 84
~ -[SAMLAuthNRequest setForceAuthN:] : 80 -> 84
~ -[SAMLAuthNRequest setProviderName:] : 96 -> 100
~ -[SAMLAuthNRequest setRequestElement:] : 20 -> 80
~ -[SAMLKeyRetrievalMethod uri] : 88 -> 96
~ -[SAMLKeyRetrievalMethod type] : 88 -> 96
~ -[SAMLKeyRetrievalMethod transforms] : 408 -> 428
~ +[SAMLBaseElement createElement:] : 64 -> 68
~ +[XMLWrapperElementFactory sharedInstance] : 160 -> 176
~ +[XMLWrapperElementFactory registerClass:forElementName:] : 112 -> 104
~ -[XMLWrapperElementFactory classForXMLNode:error:] : 156 -> 164
~ +[XMLWrapperElementFactory elementTypeByTagName:] : 64 -> 68
~ +[SAMLAdvice createElement:] : 120 -> 124
~ -[SAMLAdvice assertionIDRef] : 104 -> 112
~ -[SAMLAdvice assertionURIRef] : 104 -> 112
~ +[SAMLResponseElement createElement:] : 120 -> 124
~ -[SAMLResponseElement identifier] : 104 -> 112
~ -[SAMLResponseElement relatedRequest] : 88 -> 96
~ -[SAMLResponseElement issueInstant] : 128 -> 140
~ -[SAMLResponseElement destination] : 88 -> 96
~ -[SAMLResponseElement consent] : 88 -> 96
~ -[SAMLResponseElement issuer] : 104 -> 112
~ -[SAMLResponseElement assertions] : 300 -> 308
~ -[SAMLResponseElement assertionMeetsConditions:] : 376 -> 380
~ -[SAMLResponseElement authnStatement] : 304 -> 316
~ -[XMLWrapperQuery elementForNode:] : 160 -> 164
~ -[XMLWrapperQuery searchNodeWithXpathQuery:query:error:] : 80 -> 84
~ -[XMLWrapperQuery registerNamespace:] : 164 -> 172
~ -[XMLWrapperQuery registerXpathNamespacesForCtx:error:] : 456 -> 468
~ -[XMLWrapperQuery executeXpathQuery:query:ctxNode:error:] : 600 -> 620
~ +[SAMLAssertion createElement:] : 328 -> 336
~ -[SAMLAssertion identifier] : 104 -> 112
~ -[SAMLAssertion issueInstant] : 128 -> 140
~ -[SAMLAssertion issuer] : 104 -> 112
~ -[SAMLAssertion samlAttributes] : 344 -> 356
~ -[SAMLAssertion authorizations] : 300 -> 308
~ -[SAMLAssertion isValid:] : 228 -> 248
~ -[SAMLAssertion meetsConditions:] : 64 -> 68
~ -[SAMLAssertion isValidForRequestor:] : 308 -> 316
~ -[SAMLAssertion authorizationForResource:] : 344 -> 356
~ -[SAMLAttributeQuery initWithData:schema:error:] : 304 -> 320
~ -[SAMLAttributeQuery initWithElement:schema:error:] : 108 -> 112
~ -[SAMLAttributeQuery channelId] : 76 -> 84
~ -[SAMLAttributeQuery setSubjectFromResponse:] : 176 -> 188
~ -[SAMLAttributeQuery addAttribute:values:] : 340 -> 344
~ -[SAMLAttributeQuery setRequestElement:] : 20 -> 80
~ +[SAMLKeyInfo createElement:] : 120 -> 124
~ -[SAMLKeyInfo identifier] : 88 -> 96
~ -[SAMLKeyInfo keyName] : 104 -> 112
~ -[SAMLKeyInfo spkiSexpData] : 192 -> 204
~ -[SAMLKeyInfo mgmtData] : 104 -> 112
~ -[XMLWrapperDoc initWithData:schema:error:] : 252 -> 256
~ -[XMLWrapperDoc initWithElement:schema:error:] : 152 -> 144
~ -[XMLWrapperDoc setNamespace:] : 140 -> 152
~ -[XMLWrapperDoc getResultsByXpathQuery:error:] : 120 -> 128
~ -[XMLWrapperDoc firstResultByXpathQuery:error:] : 92 -> 100
~ -[XMLWrapperDoc docNode:] : 240 -> 244
~ -[XMLWrapperDoc query] : 8 -> 56
~ -[XMLWrapperDoc createDocument:] : 360 -> 376
~ -[XMLWrapperDoc setXMLDoc:] : 180 -> 188
~ -[XMLWrapperDoc createDocumentElement:] : 140 -> 144
~ -[XMLWrapperDoc setXmlData:] : 12 -> 64
~ -[XMLWrapperDoc setSchemaData:] : 12 -> 64
~ -[XMLWrapperDoc setDocumentElement:] : 12 -> 64
~ -[XMLWrapperDoc setQuery:] : 12 -> 64
~ +[SAMLAttribute createElement:] : 120 -> 124
~ -[SAMLAttribute name] : 88 -> 96
~ -[SAMLAttribute nameFormat] : 88 -> 96
~ -[SAMLAttribute friendlyName] : 88 -> 96
~ -[SAMLAttribute values] : 332 -> 344
~ +[SAMLSignedInfo createElement:] : 120 -> 124
~ -[SAMLSignedInfo xmlNode:] : 620 -> 640
~ -[SAMLSignedInfo identifier] : 88 -> 96
~ -[SAMLSignedInfo canonicalizationMethod] : 140 -> 152
~ -[SAMLSignedInfo signatureMethodLength] : 204 -> 220
~ -[SAMLSignedInfo signatureMethod] : 140 -> 152
~ -[SAMLSignedInfo references] : 300 -> 308
~ +[SAMLSubjectConfirmation createElement:] : 120 -> 124
~ -[SAMLSubjectConfirmation xmlNode:] : 564 -> 580
~ -[SAMLSubjectConfirmation method] : 88 -> 96
~ -[SAMLSubjectConfirmation notBefore] : 172 -> 188
~ -[SAMLSubjectConfirmation notOnOrAfter] : 172 -> 188
~ -[SAMLSubjectConfirmation recipient] : 140 -> 152
~ -[SAMLSubjectConfirmation inResponseTo] : 140 -> 152
~ -[SAMLSubjectConfirmation address] : 140 -> 152
~ +[NSBundle(SAMLAdditions) saml_frameworkBundle] : 68 -> 84
~ ___47+[NSBundle(SAMLAdditions) saml_frameworkBundle]_block_invoke : 72 -> 76
~ -[XMLWrapperNamespace initWithNsNode:error:] : 172 -> 180
~ -[XMLWrapperNamespace xmlNsForNode:error:] : 264 -> 284
~ -[XMLWrapperNamespace setHref:] : 12 -> 64
~ -[XMLWrapperNamespace setPrefix:] : 12 -> 64
~ +[SAMLStatus createElement:] : 120 -> 124
~ -[SAMLStatus statusMessage] : 100 -> 108
~ -[SAMLStatus statusDetail] : 100 -> 108
~ -[SAMLStatus status] : 76 -> 84
~ +[SAMLStatusCode createElement:] : 120 -> 124
~ -[SAMLStatusCode value] : 88 -> 96
~ +[SAMLAuthZDecisionQueryElement createElement:] : 492 -> 520
~ -[SAMLAuthZDecisionQueryElement identifier] : 104 -> 112
~ -[SAMLAuthZDecisionQueryElement destination] : 88 -> 96
~ -[SAMLAuthZDecisionQueryElement issueInstant] : 128 -> 140
~ -[SAMLAuthZDecisionQueryElement consent] : 88 -> 96
~ -[SAMLAuthZDecisionQueryElement resource] : 88 -> 96
~ -[SAMLAuthZDecisionQueryElement channelId] : 104 -> 112
~ -[SAMLAuthZDecisionQueryElement setChannelId:] : 312 -> 324
~ -[SAMLAuthZDecisionQueryElement addAction:] : 200 -> 204
~ -[SAMLAuthZDecisionQueryElement setEvidence:] : 152 -> 156
~ +[SAMLAuthNStatement createElement:] : 320 -> 328
~ -[SAMLAuthNStatement authnInstant] : 128 -> 140
~ -[SAMLAuthNStatement sessionIndex] : 88 -> 96
~ -[SAMLAuthNStatement sessionNotOnOrAfter] : 128 -> 140
~ -[SAMLAuthNStatement subjectAddress] : 140 -> 152
~ -[SAMLAuthNStatement subjectDNSName] : 140 -> 152
~ -[SAMLAuthNStatement authnContextDecl] : 140 -> 152
~ -[SAMLAuthNStatement authnContextDeclRef] : 140 -> 152
~ -[SAMLAuthNStatement authnContextClassRef] : 140 -> 152
~ -[SAMLAuthNStatement authenticatingAuthority] : 140 -> 152
~ -[SAMLAuthNStatement isValid] : 100 -> 108
~ +[SAMLSubject createElement:] : 244 -> 252
~ -[SAMLSubject subjectConfirmations] : 300 -> 308
~ -[SAMLLogoutRequest initWithData:schema:error:] : 280 -> 296
~ -[SAMLLogoutRequest initWithElement:schema:error:] : 108 -> 112
~ -[SAMLLogoutRequest issuer] : 76 -> 84
~ -[SAMLLogoutRequest setIssuer:] : 96 -> 100
~ -[SAMLLogoutRequest reason] : 76 -> 84
~ -[SAMLLogoutRequest setReason:] : 96 -> 100
~ -[SAMLLogoutRequest notOnOrAfter] : 76 -> 84
~ -[SAMLLogoutRequest setNotOnOrAfter:] : 96 -> 100
~ -[SAMLLogoutRequest setRequestElement:] : 20 -> 80
~ +[SAMLLogoutRequestElement createElement:] : 448 -> 472
~ -[SAMLLogoutRequestElement identifier] : 104 -> 112
~ -[SAMLLogoutRequestElement destination] : 88 -> 96
~ -[SAMLLogoutRequestElement issueInstant] : 112 -> 124
~ -[SAMLLogoutRequestElement consent] : 88 -> 96
~ -[SAMLLogoutRequestElement reason] : 88 -> 96
~ -[SAMLLogoutRequestElement notOnOrAfter] : 112 -> 124
~ -[SAMLLogoutRequestElement setNotOnOrAfter:] : 100 -> 104
~ -[SAMLLogoutRequestElement issuer] : 104 -> 112
~ -[SAMLLogoutRequestElement setIssuer:] : 312 -> 324
~ -[SAMLLogoutRequestElement sessionIndex] : 104 -> 112
~ -[SAMLLogoutRequestElement setSessionIndex:] : 192 -> 196

```
