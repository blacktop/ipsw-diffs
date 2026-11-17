## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3901.300.26.0.0
-  __TEXT.__text: 0xd60a4
-  __TEXT.__objc_methlist: 0xd08c
-  __TEXT.__const: 0x18d8
-  __TEXT.__gcc_except_tab: 0x1b050
-  __TEXT.__cstring: 0xc569
+3901.300.60.0.0
+  __TEXT.__text: 0xd7644
+  __TEXT.__objc_methlist: 0xd1ac
+  __TEXT.__const: 0x18e8
+  __TEXT.__gcc_except_tab: 0x1b3a4
+  __TEXT.__cstring: 0xc5b9
   __TEXT.__ustring: 0x170
-  __TEXT.__oslogstring: 0x6903
+  __TEXT.__oslogstring: 0x6993
   __TEXT.__dlopen_cstrs: 0x160
-  __TEXT.__swift5_typeref: 0x4b2
+  __TEXT.__swift5_typeref: 0x4c0
   __TEXT.__constg_swiftt: 0x540
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x41f

   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8648
+  __TEXT.__unwind_info: 0x8710
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4670
-  __DATA_CONST.__objc_classlist: 0x598
+  __DATA_CONST.__const: 0x4698
+  __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6208
+  __DATA_CONST.__objc_selrefs: 0x62f8
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0xc90
-  __AUTH_CONST.__const: 0x1f40
-  __AUTH_CONST.__cfstring: 0xa680
-  __AUTH_CONST.__objc_const: 0x17018
+  __DATA_CONST.__got: 0xcb0
+  __AUTH_CONST.__const: 0x1f60
+  __AUTH_CONST.__cfstring: 0xa6e0
+  __AUTH_CONST.__objc_const: 0x171d8
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xc00
-  __AUTH.__objc_data: 0x2f0
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH.__objc_data: 0x340
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xc68
-  __DATA.__data: 0x2900
+  __DATA.__objc_ivar: 0xc7c
+  __DATA.__data: 0x2908
   __DATA_DIRTY.__objc_data: 0x3770
   __DATA_DIRTY.__data: 0x380
   __DATA_DIRTY.__bss: 0xad0

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5205
-  Symbols:   9008
-  CStrings:  2176
+  Functions: 5232
+  Symbols:   9050
+  CStrings:  2182
 
Symbols:
+ +[EMMailSearchQueryBiomeLogger _normalizedKeyForQueryString:]
+ +[EMXiCloudHMEHeaderVerifier _hasVerifiedTrustedSignatureCoveringXiCloudHMEHeader:verifier:]
+ +[EMXiCloudHMEHeaderVerifier dkimSignatureCoversXiCloudHMEHeader:]
+ +[EMXiCloudHMEHeaderVerifier hasExactlyOneXiCloudHMEHeader:]
+ +[EMXiCloudHMEHeaderVerifier signingDomainsFromServerConfigurationValue:]
+ +[EMXiCloudHMEHeaderVerifier tagValueListForHeaderBody:isVerified:]
+ +[EMXiCloudHMEHeaderVerifier trustedSigningDomains]
+ +[EMXiCloudHMEHeaderVerifier trustedTagValueListForHeaders:deliveredByICloud:]
+ +[EMXiCloudHMEHeaderVerifier trustedTagValueListForHeaders:deliveredByICloud:verifier:]
+ -[EMLocalSearchInfo initWithQueryStatus:hasQueryEmbedding:hasKeywordResults:hasEmbeddingResults:querySafety:rankingSignalsByObjectID:]
+ -[EMLocalSearchInfo querySafety]
+ -[EMMailSearchQueryBiomeLogger _canLogCurrentState]
+ -[EMMailSearchQueryBiomeLogger _logEngagedStateIfSafe]
+ -[EMMailSearchQueryBiomeLogger querySafetyByQueryString]
+ -[EMMailSearchQueryBiomeLogger querySafetyKeysInInsertionOrder]
+ -[EMMailSearchQueryBiomeLogger setQuerySafetyByQueryString:]
+ -[EMMailSearchQueryBiomeLogger setQuerySafetyKeysInInsertionOrder:]
+ -[EMMailSearchQueryBiomeLogger trackQuerySafety:forQueryString:]
+ -[EMOutgoingMessageRepository invalidateLastDelayedMessageTimer:]
+ -[EMOutgoingMessageRepository outboxPresenceOfUnsentMessageWithMessageIDHeaderHash:completion:]
+ -[EMOutgoingMessageRepository restartLastDelayedMessageTimer:]
+ -[EMSearchQueryState querySafety]
+ -[EMSearchQueryState setQuerySafety:]
+ -[EMSearchableIndexQuery querySafetyBlock]
+ -[EMSearchableIndexQuery setQuerySafetyBlock:]
+ -[EMSearchableIndexTopHitsQuery querySafetyHandler]
+ -[EMSearchableIndexTopHitsQuery setQuerySafetyHandler:]
+ _ECMessageHeaderKeyHMEAddress
+ _EMQuerySafetyByCombining
+ _EMQuerySafetyForIsUnsafeQuery
+ _OBJC_CLASS_$_ECAngleBracketIDHash
+ _OBJC_CLASS_$_ECDKIMVerifier
+ _OBJC_CLASS_$_ECTagValueList
+ _OBJC_CLASS_$_EMXiCloudHMEHeaderVerifier
+ _OBJC_IVAR_$_EMLocalSearchInfo._querySafety
+ _OBJC_IVAR_$_EMMailSearchQueryBiomeLogger._querySafetyByQueryString
+ _OBJC_IVAR_$_EMMailSearchQueryBiomeLogger._querySafetyKeysInInsertionOrder
+ _OBJC_IVAR_$_EMSearchQueryState._querySafety
+ _OBJC_IVAR_$_EMSearchableIndexQuery._querySafetyBlock
+ _OBJC_IVAR_$_EMSearchableIndexTopHitsQuery._querySafetyHandler
+ _OBJC_METACLASS_$_EMXiCloudHMEHeaderVerifier
+ __OBJC_$_CLASS_METHODS_EMXiCloudHMEHeaderVerifier
+ __OBJC_$_CLASS_PROP_LIST_EMXiCloudHMEHeaderVerifier
+ __OBJC_CLASS_RO_$_EMXiCloudHMEHeaderVerifier
+ __OBJC_METACLASS_RO_$_EMXiCloudHMEHeaderVerifier
+ ___64-[EMMailSearchQueryBiomeLogger trackQuerySafety:forQueryString:]_block_invoke
+ ___66+[EMXiCloudHMEHeaderVerifier dkimSignatureCoversXiCloudHMEHeader:]_block_invoke
+ ___95-[EMOutgoingMessageRepository outboxPresenceOfUnsentMessageWithMessageIDHeaderHash:completion:]_block_invoke
+ ___block_descriptor_48_ea8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_ea8_32bs40bs48w_e27_v16?0"CSAttributedQuery"8lw48l8s32l8s40l8
+ _objc_retain_x7
+ _swift_arrayInitWithCopy
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 5Email21ActivityStateObserverC08ObservedE0V
- -[EMContentRepresentation setSkipMessageReformatting:]
- -[EMContentRepresentation skipMessageReformatting]
- -[EMLocalSearchInfo initWithQueryStatus:hasQueryEmbedding:hasKeywordResults:hasEmbeddingResults:rankingSignalsByObjectID:]
- -[EMMessageContentCachedMetadata setSkipMessageReformatting:]
- -[EMMessageContentCachedMetadata skipMessageReformatting]
- -[EMSearchQueryState canBeLogged]
- -[EMSearchQueryState isUnsafeQuery]
- -[EMSearchQueryState setIsUnsafeQuery:]
- _OBJC_IVAR_$_EMSearchQueryState._isUnsafeQuery
- ___block_descriptor_48_ea8_32bs40w_e27_v16?0"CSAttributedQuery"8lw40l8s32l8
- _objc_retain_x6
CStrings:
+ "<%@ %p queryStatus: %d, hasQueryEmbedding: %@, hasKeywordResults: %@, hasEmbeddingResults: %@ querySafety: %ld rankingSignalsByObjectID.count: %lu>"
+ "EFPropertyKey_querySafety"
+ "Not logging query because querySafety=%ld"
+ "TemporaryItems"
+ "Tracking querySafety=%ld for a query"
+ "encountered error while looking for an unsent outbox message: %{public}@"
+ "x-icloud-hme"
+ "x-icloud-hme-signing-domains"
- "<%@ %p queryStatus: %d, hasQueryEmbedding: %@, hasKeywordResults: %@, hasEmbeddingResults: %@ rankingSignalsByObjectID.count: %lu>"
- "SkipMessageReformat"
```
