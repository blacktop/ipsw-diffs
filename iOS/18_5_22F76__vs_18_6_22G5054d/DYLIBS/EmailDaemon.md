## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0x257c08
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_methlist: 0x15cdc
-  __TEXT.__const: 0x1eec
-  __TEXT.__gcc_except_tab: 0x4c3ac
-  __TEXT.__cstring: 0x22137
-  __TEXT.__oslogstring: 0x193b6
+3826.700.51.0.0
+  __TEXT.__text: 0x257618
+  __TEXT.__auth_stubs: 0x27c0
+  __TEXT.__objc_methlist: 0x15cec
+  __TEXT.__const: 0x1f2c
+  __TEXT.__gcc_except_tab: 0x4c2bc
+  __TEXT.__cstring: 0x220d7
+  __TEXT.__oslogstring: 0x19326
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x95b

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x106c0
+  __TEXT.__unwind_info: 0x10690
   __TEXT.__eh_frame: 0xd60
-  __TEXT.__objc_classname: 0x2efa
-  __TEXT.__objc_methname: 0x39cb5
-  __TEXT.__objc_methtype: 0x85b3
-  __TEXT.__objc_stubs: 0x252a0
+  __TEXT.__objc_classname: 0x2f0d
+  __TEXT.__objc_methname: 0x39c3d
+  __TEXT.__objc_methtype: 0x859f
+  __TEXT.__objc_stubs: 0x25240
   __DATA_CONST.__got: 0x1b88
   __DATA_CONST.__const: 0x9270
   __DATA_CONST.__objc_classlist: 0x9b0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x400
+  __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba50
-  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0xba48
+  __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0x13f8
+  __AUTH_CONST.__auth_got: 0x13f0
   __AUTH_CONST.__const: 0x4118
-  __AUTH_CONST.__cfstring: 0x114c0
-  __AUTH_CONST.__objc_const: 0x24f10
+  __AUTH_CONST.__cfstring: 0x11420
+  __AUTH_CONST.__objc_const: 0x24f40
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x5c0
-  __AUTH.__data: 0x170
+  __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0x16f0
-  __DATA.__data: 0x33a0
+  __DATA.__data: 0x33c0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2480
   __DATA_DIRTY.__objc_data: 0x5db8
-  __DATA_DIRTY.__data: 0xe98
+  __DATA_DIRTY.__data: 0xea8
   __DATA_DIRTY.__bss: 0x1508
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 788C9661-B02D-302A-A8C4-AF847605E4C7
-  Functions: 10747
-  Symbols:   36325
-  CStrings:  16773
+  UUID: 3AE473CC-B15C-3BA5-946C-30C340165674
+  Functions: 10742
+  Symbols:   36312
+  CStrings:  16759
 
Symbols:
+ -[EDBatchingMessageQueryIterator _callHandlerWithError:]
+ -[EDBatchingMessageQueryIterator _callHandlerWithMessages:]
+ -[EDCategoryCoreAnalyticsLogger _isMailAccountBucketBarHidden:]
+ _OBJC_CLASS_$_EMSmartMailbox
+ _OBJC_IVAR_$_EDBatchingMessageQueryIterator._handlerLock
+ __OBJC_$_PROP_LIST_MSBucketBarMailbox
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MSBucketBarMailbox
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MSBucketBarMailbox
+ __OBJC_$_PROTOCOL_REFS_MSBucketBarMailbox
+ __OBJC_LABEL_PROTOCOL_$_MSBucketBarMailbox
+ __OBJC_PROTOCOL_$_MSBucketBarMailbox
+ __OBJC_PROTOCOL_REFERENCE_$_MSBucketBarMailbox
+ ___106-[EDBatchingMessageQueryIterator initWithMessagePersistence:query:batchSize:firstBatchSize:limit:handler:]_block_invoke_2
+ ___70-[EDCategoryPersistence persistCategorizationResultMap:userInitiated:]_block_invoke_3
+ ___block_descriptor_56_ea8_32s40s_e21_B16?0"<EDAccount>"8ls32l8s40l8
+ ___block_descriptor_94_ea8_32s40s48s56s64s72r_e25_v32?0"EFSQLRow"8Q16^B24lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.29
+ _objc_msgSend$_callHandlerWithError:
+ _objc_msgSend$_callHandlerWithMessages:
+ _objc_msgSend$_isMailAccountBucketBarHidden:
+ _objc_msgSend$isBucketBarHiddenForMailboxes:
+ _objc_msgSend$unifiedMailboxOfType:name:
- -[EDCategoryCoreAnalyticsLogger _extractAccountIdentifier:]
- -[EDCategoryCoreAnalyticsLogger _extractAccountIdentifier:].cold.1
- -[EDCategoryCoreAnalyticsLogger _retrieveBlackPearlConfig]
- -[EDCategoryCoreAnalyticsLogger isMailAccountBlackPearlEnabled:accountIdentifier:bbConfig:accountIdentifierTobbConfig:]
- -[EDMarkCertificateVerifier _certificateFromPEMData:]
- -[EDMarkCertificateVerifier _certificateFromPEMFile:]
- -[EDMarkCertificateVerifier _loadVMCRootCertificates]
- -[EDMarkCertificateVerifier _verifyIndicatorData:withMarkCertificateData:domain:date:error:].cold.5
- -[EDMarkCertificateVerifier vmcRootCertificates]
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_IVAR_$_EDMarkCertificateVerifier._vmcRootCertificates
- _SecTrustSetAnchorCertificates
- __OBJC_$_INSTANCE_VARIABLES_EDMarkCertificateVerifier
- __OBJC_$_PROP_LIST_EDMarkCertificateVerifier
- ___58-[EDCategoryCoreAnalyticsLogger _retrieveBlackPearlConfig]_block_invoke
- ___block_descriptor_64_ea8_32s40s48s_e21_B16?0"<EDAccount>"8ls32l8s40l8s48l8
- ___block_descriptor_93_ea8_32s40s48s56s64s72r_e25_v32?0"EFSQLRow"8Q16^B24lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.40
- _objc_msgSend$_extractAccountIdentifier:
- _objc_msgSend$_retrieveBlackPearlConfig
- _objc_msgSend$initWithContentsOfFile:
- _objc_msgSend$isMailAccountBlackPearlEnabled:accountIdentifier:bbConfig:accountIdentifierTobbConfig:
- _objc_msgSend$rangeOfFirstMatchInString:options:range:
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$removeThreadProxies:forMove:
- _objc_msgSend$vmcRootCertificates
CStrings:
+ "MSBucketBarMailbox"
+ "_callHandlerWithError:"
+ "_callHandlerWithMessages:"
+ "_handlerLock"
+ "_isMailAccountBucketBarHidden:"
+ "bucketBarConfigurationIdentifier"
+ "isBucketBarHiddenForMailboxes:"
+ "isInboxMailbox"
+ "unifiedMailboxOfType:name:"
- "%@%@"
- "/[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}/"
- "B48@0:8@16@24@32@40"
- "Unable to set anchor certificates"
- "[BlackPearl] [ETL-To-CA] Account Extraction for path %@ error %@"
- "_extractAccountIdentifier:"
- "_retrieveBlackPearlConfig"
- "_vmcRootCertificates"
- "accountKey: %@, mailAccountInboxesEnabled: %ui"
- "digicert vmc root"
- "entrust vmc root"
- "initWithContentsOfFile:"
- "isMailAccountBlackPearlEnabled:accountIdentifier:bbConfig:accountIdentifierTobbConfig:"
- "pem"
- "rangeOfFirstMatchInString:options:range:"
- "regularExpressionWithPattern:options:error:"
- "removeThreadProxies:forMove:"
- "vmcRootCertificates"

```
