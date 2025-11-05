## NotesHTML

> `/System/Library/PrivateFrameworks/NotesHTML.framework/Versions/A/NotesHTML`

```diff

-2994.3.0.0.0
-  __TEXT.__text: 0xd2220
+2998.23.0.0.0
+  __TEXT.__text: 0xd1f08
   __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0xcaa4
-  __TEXT.__const: 0x6ca
-  __TEXT.__gcc_except_tab: 0x4b3c
-  __TEXT.__cstring: 0xe0a2
+  __TEXT.__objc_methlist: 0xe380
+  __TEXT.__const: 0x6da
+  __TEXT.__gcc_except_tab: 0x4b1c
+  __TEXT.__cstring: 0xe096
   __TEXT.__oslogstring: 0x137
-  __TEXT.__unwind_info: 0x35b8
+  __TEXT.__unwind_info: 0x35b0
   __TEXT.__objc_classname: 0x1d12
   __TEXT.__objc_methname: 0x1b864
   __TEXT.__objc_methtype: 0x3b18

   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6fa8
+  __DATA_CONST.__objc_selrefs: 0x71b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4f8
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x950
   __AUTH_CONST.__const: 0x1520
   __AUTH_CONST.__cfstring: 0xfce0
-  __AUTH_CONST.__objc_const: 0x18978
+  __AUTH_CONST.__objc_const: 0x15a70
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: F9CBEE29-5F41-3B9B-979D-8A96EBA69610
-  Functions: 4401
-  Symbols:   11783
-  CStrings:  10198
+  UUID: E840065C-6003-3AB7-A404-E3BAE976A9EE
+  Functions: 4443
+  Symbols:   11843
+  CStrings:  10195
 
Symbols:
+ +[ICNFIMAPClientFetchDataItem UIDDataItem].cold.1
+ +[ICNFIMAPClientFetchDataItem bodyStructureDataItem].cold.1
+ +[ICNFIMAPClientFetchDataItem flagsDataItem].cold.1
+ +[ICNFIMAPClientFetchDataItem gmailLabelsDataItem].cold.1
+ +[ICNFIMAPClientFetchDataItem internalDateDataItem].cold.1
+ +[ICNFIMAPClientFetchDataItem modificationSequenceDataItem].cold.1
+ +[ICNFIMAPClientFetchDataItem sizeDataItem].cold.1
+ +[ICNFIMAPClientOperation _IMAPNeedsQuoteCharacterSet].cold.1
+ +[ICNFIMAPFramework logsIMAPErrors].cold.1
+ +[ICNFIMAPGateway sharedKeySetForMessageInfo].cold.1
+ +[ICNFMCAttachment _backgroundFileReadingQueue].cold.1
+ +[ICNFMCByteSet ASCIIByteSet].cold.1
+ +[ICNFMCByteSet asciiWhitespaceSet].cold.1
+ +[ICNFMCByteSet nonASCIIByteSet].cold.1
+ +[ICNFMCDateFormatterFactory newIMAPDateFormatter].cold.1
+ +[ICNFMCDateParser _commonDateFormatters].cold.1
+ +[ICNFMCDateParser _dateFromString:imapFirst:].cold.1
+ +[ICNFMCDateParser _fallbackDateFormaters].cold.1
+ +[ICNFMCDateParser _imapDateFormatter].cold.1
+ +[ICNFMCMailCoreFramework isRunningInMail].cold.1
+ +[ICNFMCManagedObjectContextManager attachContextManagerWithOptions:toContext:].cold.1
+ +[ICNFMCMessage sharedKeySetForSpotlightAttributes].cold.1
+ +[ICNFMCMessageHeaders _localizedHeadersForKeys].cold.1
+ +[ICNFMCMessageHeaders basicHeaderKeys].cold.1
+ +[ICNFMCMessageHeaders localizedHeaders].cold.1
+ +[ICNFMCMimeDataEncoding sharedKeySetForEncodingOptions].cold.1
+ +[ICNFMCNetworkController getHostUUIDString].cold.1
+ +[ICNFMCSubjectParser effectivePrefixLengthForSubject:replyOnly:].cold.1
+ +[NFAccount sharedAccountStore].cold.1
+ +[NFLocalToRemotePusher _exchangePusher].cold.1
+ +[NFLocalToRemotePusher _imapPusher].cold.1
+ +[NFPersistenceManager persistentStoreCoordinatorAddPersistentStoreIfNecessary:].cold.1
+ +[NSCharacterSet(ICNFMCMailCoreAdditions) ic_unsafeDomainNameCharacterSet].cold.1
+ -[ICNFMCArchiveFileWrapper _archiveFileWrapperCommonInit].cold.1
+ -[ICNFMCMessage description].cold.1
+ -[ICNFMCMessageGenerator init].cold.1
+ -[ICNFMCMessageHeaders initWithHeaderData:encodingHint:].cold.1
+ -[ICNFMCMimePart _parseSubpartsWithEncodingHint:messageBodyData:hasVisualEncoding:].cold.1
+ -[ICNFMCMimePart _parseUUEncodedPartsWithEncodingHint:bodyData:range:].cold.1
+ -[ICNFMCMimePart(ICNFMCStringRendering) renderString:].cold.1
+ -[ICNFMCSaslClient initWithMechanismNames:account:externalSecurityLayer:allowPlainText:].cold.1
+ -[ICNFMCSocket init].cold.1
+ -[NFAosImapAccountProxy _anisetteData].cold.1
+ -[NFAosImapAccountProxy clientInfo].cold.1
+ -[NSData(ICNFMCHFSDataConversion) ic_wrapperForAppleFileDataWithFileEncodingHint:].cold.1
+ -[NSData(ICNFMCHFSDataConversion) ic_wrapperForBinHex40DataWithFileEncodingHint:].cold.1
+ -[NSFileWrapper(ICNFMCHFSDataConversion) ic_appleDoubleDataWithFilename:length:].cold.1
+ -[NSFileWrapper(ICNFMCHFSDataConversion) ic_appleSingleDataWithFilename:length:].cold.1
+ -[NSMutableData(ICNFMCRFC2231Support) ic_appendRFC2231CompliantValue:forKey:withEncodingHint:].cold.1
+ -[NSMutableData(ICNFMCRFC2231Support) ic_appendRFC2231CompliantValue:forKey:withEncodingHint:].cold.2
+ -[NSMutableData(ICNFMCRFC2231Support) ic_appendRFC2231CompliantValue:forKey:withEncodingHint:].cold.3
+ -[NSMutableDictionary(ICNFMCRFC2231Support) ic_fixupRFC2231ValuesWithSender:fromWindows:].cold.1
+ -[NSString(ICNFMCFormatFlowedSupport) ic_convertFromFlowedText:].cold.1
+ -[NSString(ICNFMCMailCoreAdditions) ic_stringByReplacingNonBreakingSpacesWithString:].cold.1
+ -[NSString(ICNFMCRFC2047Support) ic_decodeMimeHeaderValueWithCharsetHint:detectOtherEncodings:fromWindows:].cold.1
+ -[_ICNFMCMimeEnrichedReader parenthesesSet].cold.1
+ -[_ICNFMCMimeEnrichedReader punctuationSet].cold.1
+ ICNFMCCreateStringFromHeaderBytes.cold.1
+ createInternetMessageDateFormatter.cold.1
+ dateForString.cold.1
CStrings:
- "-->"
- "AMP"
- "amp"

```
