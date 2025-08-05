## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3860.100.5.2.1
-  __TEXT.__text: 0x279854
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_methlist: 0x169b4
-  __TEXT.__const: 0x1f1c
-  __TEXT.__gcc_except_tab: 0x52404
-  __TEXT.__cstring: 0x22f67
-  __TEXT.__oslogstring: 0x1a5b4
+3863.100.1.2.5
+  __TEXT.__text: 0x27a6ac
+  __TEXT.__auth_stubs: 0x27c0
+  __TEXT.__objc_methlist: 0x16a1c
+  __TEXT.__const: 0x208c
+  __TEXT.__gcc_except_tab: 0x5250c
+  __TEXT.__cstring: 0x23070
+  __TEXT.__oslogstring: 0x1a5e4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x2c
-  __TEXT.__constg_swiftt: 0x7c8
-  __TEXT.__swift5_typeref: 0x933
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x702
-  __TEXT.__swift5_fieldmd: 0xae4
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x154
-  __TEXT.__swift5_types: 0xc8
+  __TEXT.__constg_swiftt: 0x804
+  __TEXT.__swift5_typeref: 0x957
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_reflstr: 0x752
+  __TEXT.__swift5_fieldmd: 0xb28
+  __TEXT.__swift5_assocty: 0xd8
+  __TEXT.__swift5_proto: 0x168
+  __TEXT.__swift5_types: 0xd0
   __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x112f0
+  __TEXT.__unwind_info: 0x11350
   __TEXT.__eh_frame: 0xcc0
   __TEXT.__objc_classname: 0x3049
-  __TEXT.__objc_methname: 0x3b6f6
+  __TEXT.__objc_methname: 0x3b7d8
   __TEXT.__objc_methtype: 0x88a3
-  __TEXT.__objc_stubs: 0x26860
-  __DATA_CONST.__got: 0x1c38
+  __TEXT.__objc_stubs: 0x268e0
+  __DATA_CONST.__got: 0x1c48
   __DATA_CONST.__const: 0x9bc8
-  __DATA_CONST.__objc_classlist: 0xa00
+  __DATA_CONST.__objc_classlist: 0xa08
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbfa0
+  __DATA_CONST.__objc_selrefs: 0xbfc8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x13f8
-  __AUTH_CONST.__const: 0x43c0
+  __AUTH_CONST.__auth_got: 0x13f0
+  __AUTH_CONST.__const: 0x4468
   __AUTH_CONST.__cfstring: 0x117e0
-  __AUTH_CONST.__objc_const: 0x26768
+  __AUTH_CONST.__objc_const: 0x267d8
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xf10
-  __AUTH.__data: 0x3e8
+  __AUTH.__objc_data: 0xf08
+  __AUTH.__data: 0x3e0
   __DATA.__objc_ivar: 0x182c
-  __DATA.__data: 0x3470
+  __DATA.__data: 0x34b0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x2600
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5788
-  __DATA_DIRTY.__data: 0xaa0
-  __DATA_DIRTY.__bss: 0x1418
+  __DATA.__bss: 0x26f0
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x5800
+  __DATA_DIRTY.__data: 0xad0
+  __DATA_DIRTY.__bss: 0x15b0
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 09662AC9-5D75-388D-A2FE-DF833FD65ADE
-  Functions: 11095
-  Symbols:   37659
-  CStrings:  17271
+  UUID: 13931CC6-9F2B-35AA-9B82-8E6227D6CD33
+  Functions: 11121
+  Symbols:   37689
+  CStrings:  17288
 
Symbols:
+ +[EDSearchableIndexItem searchableMessageAuthenticationStateForBaseMessage:]
+ -[EDMessageAuthenticator _isICloudHideMyEmailMessage:sender:]
+ -[EDMessageAuthenticator _messageAuthenticationStateForAuthenticationResult:sender:trustingServer:]
+ -[EDMessageAuthenticator _mostAlignedDKIMServerStatementFromAuthenticationResult:forSender:]
+ -[EDSearchableIndexItem addMessageAuthenticationStateAttributesToAttributeSet:]
+ -[EDSearchableIndexManager persistenceDidUpdateAuthenticationStateForMessages:]
+ _OBJC_CLASS_$_ECDMARCVerifier
+ _OBJC_CLASS_$_EDSearchableMessageAuthenticationState
+ _OBJC_METACLASS_$_EDSearchableMessageAuthenticationState
+ __DATA_EDSearchableMessageAuthenticationState
+ __INSTANCE_METHODS_EDSearchableMessageAuthenticationState
+ __IVARS_EDSearchableMessageAuthenticationState
+ __METACLASS_DATA_EDSearchableMessageAuthenticationState
+ ___69+[EDMessageTransformer mailboxesForPersistedMessage:mailboxProvider:]_block_invoke.75
+ ___block_literal_global.38
+ ___swift_memcpy8_8
+ _associated conformance 11EmailDaemon36SearchableMessageAuthenticationStateVSHAASQ
+ _associated conformance So28EDMessageAuthenticationStateVSH11EmailDaemonSQ
+ _block_copy_helper.101
+ _block_copy_helper.108
+ _block_copy_helper.115
+ _block_copy_helper.94
+ _block_descriptor.103
+ _block_descriptor.110
+ _block_descriptor.117
+ _block_descriptor.96
+ _block_destroy_helper.102
+ _block_destroy_helper.109
+ _block_destroy_helper.116
+ _block_destroy_helper.95
+ _objc_msgSend$addMessageAuthenticationStateAttributesToAttributeSet:
+ _objc_msgSend$alignmentForDKIMSigningDomain:andSenderDomain:
+ _objc_msgSend$dkimServerResult
+ _objc_msgSend$dkimServerSigningDomain
+ _objc_msgSend$dkimServerStatements
+ _objc_msgSend$initWithAuthenticationState:
+ _objc_msgSend$initWithConversationIdentifier:mailboxIdentifiers:gmailLabels:isLikelyJunk:dateLastViewed:flags:authenticationState:
+ _objc_msgSend$searchableMessageAuthenticationStateForBaseMessage:
+ _symbolic _____ 11EmailDaemon36SearchableMessageAuthenticationStateV
+ _symbolic _____ So28EDMessageAuthenticationStateV
+ _symbolic _____Sg 11EmailDaemon36SearchableMessageAuthenticationStateV
+ _type_layout_string 11EmailDaemon36SearchableMessageAuthenticationStateV
+ _type_layout_string So28EDMessageAuthenticationStateV
- -[EDMessageAuthenticator _isICloudHideMyEmailMessage:]
- -[EDMessageAuthenticator _messageAuthenticationStateForAuthenticationResult:trustingServer:]
- _EFIsSeedBuild
- ___69+[EDMessageTransformer mailboxesForPersistedMessage:mailboxProvider:]_block_invoke.77
- ___block_literal_global.41
- ___block_literal_global.45
- ___block_literal_global.75
- _block_copy_helper.103
- _block_copy_helper.110
- _block_copy_helper.89
- _block_copy_helper.96
- _block_descriptor.105
- _block_descriptor.112
- _block_descriptor.91
- _block_descriptor.98
- _block_destroy_helper.104
- _block_destroy_helper.111
- _block_destroy_helper.90
- _block_destroy_helper.97
- _objc_msgSend$dkimHasServerResult
- _objc_msgSend$dkimServerVerified
- _objc_msgSend$initWithConversationIdentifier:mailboxIdentifiers:gmailLabels:isLikelyJunk:dateLastViewed:flags:
- _objc_msgSend$initWithDirectory:userProfileProvider:contactStore:vipManager:
CStrings:
+ "?"
+ "@\"EDAttachmentMetadata\""
+ "@\"EDMessageAttachmentMetadata\""
+ "EDCategoryMigrator.m"
+ "EDCategoryPersistence.m"
+ "EDGroupedSender.m"
+ "EDGroupedSenderQueryHandler.m"
+ "EDInteractionEventLogPersistence.m"
+ "EDMessageCategorizer.m"
+ "EDSearchableMessageAuthenticationState"
+ "EmailDaemon_Private.EDSearchableMessageAuthenticationState"
+ "Indexing authenticate state: %lld for message: %{public}@"
+ "addMessageAuthenticationStateAttributesToAttributeSet:"
+ "alignmentForDKIMSigningDomain:andSenderDomain:"
+ "com_apple_mail_is_authenticated"
+ "dkimServerResult"
+ "dkimServerSigningDomain"
+ "dkimServerStatements"
+ "initWithAuthenticationState:"
+ "initWithConversationIdentifier:mailboxIdentifiers:gmailLabels:isLikelyJunk:dateLastViewed:flags:authenticationState:"
+ "searchableMessageAuthenticationStateForBaseMessage:"
- "EDCategoryMigrator-BlackPearl.m"
- "EDCategoryPersistence-BlackPearl.m"
- "EDGroupedSender-BlackPearlUI.m"
- "EDGroupedSenderQueryHandler-BlackPearlUI.m"
- "EDInteractionEventLogPersistence-BlackPearl.m"
- "EDMessageCategorizer-BlackPearl.m"
- "dkimHasServerResult"
- "dkimServerVerified"
- "initWithConversationIdentifier:mailboxIdentifiers:gmailLabels:isLikelyJunk:dateLastViewed:flags:"

```
