## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/Versions/A/EmailCore`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x5871c
+3826.500.181.1.5
+  __TEXT.__text: 0x588c8
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x41ec
+  __TEXT.__objc_methlist: 0x4db0
   __TEXT.__const: 0xe50
-  __TEXT.__gcc_except_tab: 0x6dec
-  __TEXT.__cstring: 0x835b
+  __TEXT.__gcc_except_tab: 0x6df4
+  __TEXT.__cstring: 0x834c
   __TEXT.__oslogstring: 0xcd8
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x27a8
+  __TEXT.__unwind_info: 0x27e0
   __TEXT.__objc_classname: 0xcbd
-  __TEXT.__objc_methname: 0xaa07
+  __TEXT.__objc_methname: 0xaa36
   __TEXT.__objc_methtype: 0x16a3
   __TEXT.__objc_stubs: 0x73a0
   __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1c08
+  __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26f8
+  __DATA_CONST.__objc_selrefs: 0x28b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x748
-  __AUTH_CONST.__const: 0xe78
+  __AUTH_CONST.__const: 0xe48
   __AUTH_CONST.__cfstring: 0x50c0
-  __AUTH_CONST.__objc_const: 0xb038
+  __AUTH_CONST.__objc_const: 0x9af0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0xac0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BE2B3080-D783-3EE8-8161-00DE76CC40A2
-  Functions: 1870
-  Symbols:   5587
-  CStrings:  4389
+  UUID: 497E5BF9-44FA-3BA9-AD60-E90A24C24539
+  Functions: 1909
+  Symbols:   5637
+  CStrings:  4391
 
Symbols:
+ +[ECAccountsObserver observedAccountTypes].cold.1
+ +[ECBIMIInfo bimiInfoForHeaders:]
+ +[ECCMSEncoder oidStringsForAuthenticatedEncryption].cold.1
+ +[ECEmailAddress _cachedEmailAddressForString:generator:].cold.1
+ +[ECMessageFlags cachedFlagsWithHash:generator:].cold.1
+ +[ECSASLClient installedMechanisms].cold.1
+ +[ECSubject _uniqueString:type:].cold.1
+ +[ECSubjectFormatter _subjectStringForDisplayForObject:style:].cold.1
+ +[ECSubjectFormatter localizedForwardPrefix].cold.1
+ +[ECSubjectFormatter localizedReplyPrefix].cold.1
+ +[NSCharacterSet(ECMessageBodyParser) ec_ignorableCharacterSet].cold.1
+ +[NSCharacterSet(ECMessageBodyParser) ec_whitespaceNewlineAndTagCharacterSet].cold.1
+ +[NSCharacterSet(ECMessageBodyParser) ec_zeroWidthCharacterSet].cold.1
+ +[NSCharacterSet(SubjectParser) ec_prefixDelimiterCharacterSet].cold.1
+ +[NSRegularExpression(ECMessageBodyParser) ec_copyAttributionRegularExpressionForType:].cold.1
+ +[NSRegularExpression(SubjectParser) ec_regularExpressionForList].cold.1
+ +[NSString(ECPersonNameComponents) ec_nameExtensions].cold.1
+ +[NSString(ECPersonNameComponents) ec_partialSurnames].cold.1
+ +[_ECBIMIHeaderParser bimiInfoForHeaders:]
+ +[_ECHeaderAuthenticationResultsParser _scanQuotedValueWithScanner:intoString:].cold.1
+ +[_ECHeaderAuthenticationResultsParser _scanToCFWSOrEqualWithScanner:intoString:].cold.1
+ +[_ECHeaderAuthenticationResultsParser _scanToCFWSOrPeriodOrSemicolonWithScanner:intoString:].cold.1
+ +[_ECHeaderAuthenticationResultsParser _scanToCFWSOrSemicolonWithScanner:intoString:].cold.1
+ +[_ECHeaderAuthenticationResultsParser _skipCFWSWithScanner:].cold.1
+ -[ECBIMIInfo .cxx_destruct]
+ -[ECBIMIInfo _calculateHash]
+ -[ECBIMIInfo evidenceLocation]
+ -[ECBIMIInfo hashAlgorithm]
+ -[ECBIMIInfo hash]
+ -[ECBIMIInfo indicatorHash]
+ -[ECBIMIInfo indicator]
+ -[ECBIMIInfo initWithIndicator:location:evidenceLocation:indicatorHash:hashAlgorithm:]
+ -[ECBIMIInfo isEqual:]
+ -[ECBIMIInfo location]
+ -[ECEncodedWordDecoder _encodedWordDelimiter].cold.1
+ -[ECEncodedWordDecoder _encodedWordEndSequence].cold.1
+ -[ECEncodedWordDecoder _encodedWordLanguageDelimiter].cold.1
+ -[ECEncodedWordDecoder _encodedWordStartSequence].cold.1
+ -[ECEncodedWordDecoder _lineSeparator].cold.1
+ -[ECEncodedWordEncoder _findNextByteThatNeedsQEncodingBetweenStartByte:endByte:].cold.1
+ -[ECMessageAuthenticator _addServerResultsFromMessage:toResult:].cold.1
+ -[ECMessageBodyElement valueForAttributes:].cold.1
+ -[ECMessageBodyHTMLParser parse].cold.1
+ -[ECMessageBodyParser didFindError:].cold.2
+ -[ECSASLClient initWithMechanismNames:credentials:externalSecurityLayer:allowPlainText:].cold.1
+ -[NSString(ECEmailAddressQuoting) ecemailaddress_trimmedAndQuotedDisplayName].cold.1
+ -[NSString(ECEmailAddressQuoting) ecemailaddress_trimmedAndQuotedLocalPart].cold.1
+ -[NSString(ECEmailAddressQuoting) ecemailaddress_uniquedDomain].cold.1
+ ECIDNALog.cold.1
+ ECNetworkAllowedLog.cold.1
+ ECSMIMELog.cold.1
+ OBJC_IVAR_$_ECBIMIInfo._evidenceLocation
+ OBJC_IVAR_$_ECBIMIInfo._hash
+ OBJC_IVAR_$_ECBIMIInfo._hashAlgorithm
+ OBJC_IVAR_$_ECBIMIInfo._indicator
+ OBJC_IVAR_$_ECBIMIInfo._indicatorHash
+ OBJC_IVAR_$_ECBIMIInfo._location
+ _OBJC_CLASS_$_ECBIMIInfo
+ _OBJC_METACLASS_$_ECBIMIInfo
+ __36-[ECEmailAddressComponents isEqual:]_block_invoke.178
+ __36-[ECEmailAddressComponents isEqual:]_block_invoke_2.179
+ __63-[NSString(ECEmailAddressQuoting) ecemailaddress_uniquedDomain]_block_invoke.269
+ __OBJC_$_CLASS_METHODS_ECBIMIInfo
+ __OBJC_$_INSTANCE_METHODS_ECBIMIInfo
+ __OBJC_$_INSTANCE_VARIABLES_ECBIMIInfo
+ __OBJC_$_PROP_LIST_ECBIMIInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EFPubliclyDescribable
+ __OBJC_CLASS_RO_$_ECBIMIInfo
+ __OBJC_METACLASS_RO_$_ECBIMIInfo
+ __block_literal_global.165
+ __block_literal_global.171
+ __block_literal_global.187
+ __block_literal_global.189
+ __block_literal_global.237
+ __block_literal_global.249
+ __block_literal_global.266
+ __block_literal_global.287
+ _ef_log_ECCMSEncoder.cold.1
+ _ef_log_ECDKIMCryptoUtil.cold.1
+ _ef_log_ECDKIMVerifier.cold.1
+ _ef_log_ECHeaderAuthenticationResults.cold.1
+ _ef_log_ECMessageBodyParser.cold.1
+ _ef_log_ECTagValueList.cold.1
+ _smb_session_setup
+ _stringByApplyingIDNATranslationWithRange.cold.2
+ _unload_negprot_resp
- +[ECBIMIData bimiDataForHeaders:]
- +[_ECBIMIHeaderParser bimiDataForHeaders:]
- -[ECBIMIData .cxx_destruct]
- -[ECBIMIData _calculateHash]
- -[ECBIMIData evidenceLocation]
- -[ECBIMIData hashAlgorithm]
- -[ECBIMIData hash]
- -[ECBIMIData indicatorHash]
- -[ECBIMIData indicator]
- -[ECBIMIData initWithIndicator:location:evidenceLocation:indicatorHash:hashAlgorithm:]
- -[ECBIMIData isEqual:]
- -[ECBIMIData location]
- OBJC_IVAR_$_ECBIMIData._evidenceLocation
- OBJC_IVAR_$_ECBIMIData._hash
- OBJC_IVAR_$_ECBIMIData._hashAlgorithm
- OBJC_IVAR_$_ECBIMIData._indicator
- OBJC_IVAR_$_ECBIMIData._indicatorHash
- OBJC_IVAR_$_ECBIMIData._location
- _OBJC_CLASS_$_ECBIMIData
- _OBJC_METACLASS_$_ECBIMIData
- __36-[ECEmailAddressComponents isEqual:]_block_invoke.175
- __36-[ECEmailAddressComponents isEqual:]_block_invoke_2.176
- __63-[NSString(ECEmailAddressQuoting) ecemailaddress_uniquedDomain]_block_invoke.266
- __OBJC_$_CLASS_METHODS_ECBIMIData
- __OBJC_$_INSTANCE_METHODS_ECBIMIData
- __OBJC_$_INSTANCE_VARIABLES_ECBIMIData
- __OBJC_$_PROP_LIST_ECBIMIData
- __OBJC_CLASS_RO_$_ECBIMIData
- __OBJC_METACLASS_RO_$_ECBIMIData
- __block_literal_global.162
- __block_literal_global.168
- __block_literal_global.184
- __block_literal_global.186
- __block_literal_global.234
- __block_literal_global.246
- __block_literal_global.263
- __block_literal_global.284
CStrings:
+ "ECBIMIInfo"
+ "Internal Error %d in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
+ "Internal Error %d in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/ntlm.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/atoken.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/atoken2.m near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/oauthbearer.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/checkpw.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
+ "Parameter error in /AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
+ "T@\"NSString\",?,R,C,N"
+ "bimiInfoForHeaders:"
+ "ef_shortPublicDescription"
+ "init()"
- "ECBIMIData"
- "GSSAPI Error: "
- "Internal Error %d in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
- "Internal Error %d in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/ntlm.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/atoken.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/atoken2.m near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/oauthbearer.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/checkpw.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
- "Parameter error in /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
- "bimiDataForHeaders:"

```
