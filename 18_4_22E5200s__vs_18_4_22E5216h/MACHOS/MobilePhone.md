## MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

-2975.500.125.2.4
-  __TEXT.__text: 0x1e567c
-  __TEXT.__auth_stubs: 0x3ff0
-  __TEXT.__objc_stubs: 0x1cc40
-  __TEXT.__objc_methlist: 0x124c8
+2975.500.161.2.1
+  __TEXT.__text: 0x1ec3c0
+  __TEXT.__auth_stubs: 0x4010
+  __TEXT.__objc_stubs: 0x1cd00
+  __TEXT.__objc_methlist: 0x12530
   __TEXT.__const: 0x6bd4
-  __TEXT.__objc_methname: 0x2edcc
+  __TEXT.__objc_methname: 0x2ef89
   __TEXT.__cstring: 0xd415
-  __TEXT.__oslogstring: 0xb636
+  __TEXT.__oslogstring: 0xb706
   __TEXT.__objc_classname: 0x1bec
   __TEXT.__objc_methtype: 0x6aea
-  __TEXT.__gcc_except_tab: 0xb54
+  __TEXT.__gcc_except_tab: 0xb6c
   __TEXT.__dlopen_cstrs: 0xc2
   __TEXT.__ustring: 0x14
-  __TEXT.__swift5_typeref: 0x4da4
-  __TEXT.__swift5_capture: 0x2538
+  __TEXT.__swift5_typeref: 0x4d9c
+  __TEXT.__swift5_capture: 0x2528
   __TEXT.__constg_swiftt: 0x3874
   __TEXT.__swift5_builtin: 0x258
   __TEXT.__swift5_reflstr: 0x301b

   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift_as_entry: 0x2e4
   __TEXT.__swift_as_ret: 0x300
-  __TEXT.__unwind_info: 0x81f8
-  __TEXT.__eh_frame: 0x8c1c
-  __DATA_CONST.__auth_got: 0x2008
+  __TEXT.__unwind_info: 0x81d8
+  __TEXT.__eh_frame: 0x8cb4
+  __DATA_CONST.__auth_got: 0x2018
   __DATA_CONST.__got: 0x17e0
-  __DATA_CONST.__auth_ptr: 0x1160
+  __DATA_CONST.__auth_ptr: 0x1188
   __DATA_CONST.__const: 0xa268
   __DATA_CONST.__cfstring: 0x6000
   __DATA_CONST.__objc_classlist: 0x780

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x1c930
-  __DATA.__objc_selrefs: 0xa1e8
-  __DATA.__objc_ivar: 0xe10
+  __DATA.__objc_const: 0x1c9c0
+  __DATA.__objc_selrefs: 0xa238
+  __DATA.__objc_ivar: 0xe1c
   __DATA.__objc_data: 0x7c00
-  __DATA.__data: 0x7988
+  __DATA.__data: 0x7998
   __DATA.__bss: 0x6750
   __DATA.__common: 0x840
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11762
-  Symbols:   81260
-  CStrings:  10391
+  Functions: 11754
+  Symbols:   81231
+  CStrings:  10412
 
Symbols:
+ -[CHRecentCall(PhoneKit) parsedNamesStrippingEmoji]
+ -[MPVoicemailTableViewController performDeleteAtIndexPaths:dataSourceActions:completionBlock:]
+ -[PHLCDViewTextField setUnicodeDirectionalCharactersSet:]
+ -[PHLCDViewTextField unicodeDirectionalCharactersSet]
+ -[PHRecentsController fetchRecentCalls:]
+ -[PHRecentsController hasPendingUpdates]
+ -[PHRecentsController hasUpdated]
+ -[PHRecentsController setHasPendingUpdates:]
+ -[PHRecentsController setHasUpdated:]
+ -[PHRecentsController updateRecentCalls:]
+ -[PHRecentsController updateWithRecentCalls:]
+ GCC_except_table95
+ OBJC_IVAR_$_PHLCDViewTextField._unicodeDirectionalCharactersSet
+ OBJC_IVAR_$_PHRecentsController._hasPendingUpdates
+ OBJC_IVAR_$_PHRecentsController._hasUpdated
+ _$s10Foundation3URLV25deletingLastPathComponentACyF
+ _$s11MobilePhone21CallsSearchControllerC9tableView_12cellForRowAtSo07UITableG4CellCSo0lG0C_10Foundation9IndexPathVtFAGyXEfU_
+ _$s11MobilePhone21ContactSearchViewCellC15logButtonTapped33_7451B51A4E25835BD6E8176CF2D83D77LLyyF
+ _$s11MobilePhone21ContactSearchViewCellC16callButtonTappedyyFTm
+ _$s11MobilePhone23VoicemailAccountManagerC04withD6Source33_919A6ECA62650D38DFB63EF032987E64LLyqd__qd__AA0cdE8Protocol_pXElFqd__AaF_pSgzYuYTXEfU_AA0cdE4DataC_AA0cdE5CacheVyAIGytTg504$s11a7Phone23cde64C11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyu2E8n7_pXEfU_u2E4O18C_AA0cdeG0VyAOGTg5ACyxq_GSgXwz_AI_AlA0cdeoN0Rz0O0Qy_RszAA0cdepN0R_r0_lXXAA0cdeW0CTf1nnnc_nTf0nnnsn_n
+ _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_AA0cdE4DataC_AA0cdeG0VyAOGTg5Tf0nnsn_n
+ _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFTm
+ _$s11MobilePhone26VMVoicemailManagerProtocol_pMD
+ _$s11MobilePhone32VoicemailAccountManagerDecoratorC03anyD10SubscribedSbvgTm
+ _$sSo9CNContactCMa
+ _CEMCreateStringByStrippingEmojiCharacters
+ ___40-[PHRecentsController fetchRecentCalls:]_block_invoke
+ ___46-[PHVoicemailInboxListViewController _delete:]_block_invoke_2
+ ___94-[MPVoicemailTableViewController performDeleteAtIndexPaths:dataSourceActions:completionBlock:]_block_invoke
+ ___94-[MPVoicemailTableViewController performDeleteAtIndexPaths:dataSourceActions:completionBlock:]_block_invoke_2
+ __block_literal_global.527
+ _objc_msgSend$fetchRecentCalls:
+ _objc_msgSend$formattedInternationalStringValue
+ _objc_msgSend$hasPendingUpdates
+ _objc_msgSend$hasUpdated
+ _objc_msgSend$parsedNamesStrippingEmoji
+ _objc_msgSend$performDeleteAtIndexPaths:dataSourceActions:completionBlock:
+ _objc_msgSend$setHasPendingUpdates:
+ _objc_msgSend$setHasUpdated:
+ _objc_msgSend$setWritingToolsBehavior:
+ _objc_msgSend$updateRecentCalls:
+ _objc_msgSend$updateWithRecentCalls:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ block_copy_helper.135
+ block_copy_helper.138
+ block_copy_helper.154
+ block_descriptor.137
+ block_descriptor.140
+ block_descriptor.156
+ block_destroy_helper.136
+ block_destroy_helper.139
+ block_destroy_helper.155
- -[MPVoicemailTableViewController performDeleteAtIndexPaths:completionBlock:]
- -[PHRecentsController fetchRecentCalls]
- _$s11MobilePhone23VoicemailAccountManagerC04withD6Source33_919A6ECA62650D38DFB63EF032987E64LLyqd__qd__AA0cdE8Protocol_pXElFqd__AaF_pSgzYuYTXEfU_AA0cdE4DataC_AA0cdE5CacheVyAIGytTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC04withD6Source33_919A6ECA62650D38DFB63EF032987E64LLyqd__qd__AA0cdE8Protocol_pXElFqd__AaF_pSgzYuYTXEfU_AA0cdE4DataC_AA0cdE5CacheVyAIGytTg5
- _$s11MobilePhone23VoicemailAccountManagerC04withD6Source33_919A6ECA62650D38DFB63EF032987E64LLyqd__qd__AA0cdE8Protocol_pXElFqd__AaF_pSgzYuYTXEfU_TA
- _$s11MobilePhone23VoicemailAccountManagerC04withD6Source33_919A6ECA62650D38DFB63EF032987E64LLyqd__qd__AA0cdE8Protocol_pXElFqd__AaF_pSgzYuYTXEfU_ySayypGzYuYTXEfU_AA0cdE4DataC_AA0cdE5CacheVyAJGytTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC04withD6Source33_919A6ECA62650D38DFB63EF032987E64LLyqd__qd__AA0cdE8Protocol_pXElFqd__AaF_pSgzYuYTXEfU_ySayypGzYuYTXEfU_TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFScTyyts5Error_pGSgAOzYuYTXEfU0_AA0cdE4DataC_AA0cdeG0VyAQGTG5
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFScTyyts5Error_pGSgAOzYuYTXEfU0_AA0cdE4DataC_AA0cdeG0VyAQGTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFScTyyts5Error_pGSgAOzYuYTXEfU0_TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_AA0cdE4DataC_AA0cdeG0VyAOGTg5
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_AA0cdE4DataC_AA0cdeG0VyAOGTg5TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_xSgANzYuYTXEfU_AA0cdE4DataC_AA0cdeG0VyAPGTG5
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_xSgANzYuYTXEfU_TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_yxSgzYuYTXEfU0_AA0cdE4DataC_AA0cdeG0VyAPGTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_yxSgzYuYTXEfU0_TA
- _$s11MobilePhone23VoicemailAccountManagerC11updateCache3for4uuidyAA0cdE6UpdateC_10Foundation4UUIDVSgtYaFyAA0cdE8Protocol_pXEfU_yxSgzYuYTXEfU0_TATm
- _$s11MobilePhone23VoicemailAccountManagerC16writeCacheToDisk33_919A6ECA62650D38DFB63EF032987E64LLyyF
- _$s11MobilePhone23VoicemailAccountManagerC16writeCacheToDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_AA0cdE4DataC_AA0cdeG0VyAGGTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC16writeCacheToDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_TA
- _$s11MobilePhone23VoicemailAccountManagerC16writeCacheToDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_xSgAFzYuYTXEfU_AA0cdE4DataC_AA0cdeG0VyAHGTG5
- _$s11MobilePhone23VoicemailAccountManagerC16writeCacheToDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_xSgAFzYuYTXEfU_TA
- _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyF
- _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_AA0cdE4DataC_AA0cdeG0VyAGGTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_AA0cdE4DataC_AA0cdeG0VyAGGTG5TATm
- _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_TA
- _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_yxSgzYuYTXEfU_AA0cdE4DataC_AA0cdeG0VyAHGTG5TA
- _$s11MobilePhone23VoicemailAccountManagerC17loadCacheFromDisk33_919A6ECA62650D38DFB63EF032987E64LLyyFyq_zYuYTXEfU_yxSgzYuYTXEfU_TA
- _$s11MobilePhone32VoicemailAccountManagerDecoratorCAA0c15BadgeCalculatordE0A2aDP16isMessageWaitingSbvgTWTm
- _$s11MobilePhone32VoicemailAccountManagerDecoratorCAA0c15BadgeCalculatordE0A2aDP6onlineSbvgTWTm
- ___76-[MPVoicemailTableViewController performDeleteAtIndexPaths:completionBlock:]_block_invoke
- ___76-[MPVoicemailTableViewController performDeleteAtIndexPaths:completionBlock:]_block_invoke_2
- __block_literal_global.514
- _objc_msgSend$donateEventSpeakerUsed
- _objc_msgSend$familyName
- _objc_msgSend$fetchRecentCalls
- _objc_msgSend$givenName
- _objc_msgSend$performDeleteAtIndexPaths:completionBlock:
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- block_copy_helper.124
- block_copy_helper.140
- block_descriptor.126
- block_descriptor.142
- block_destroy_helper.125
- block_destroy_helper.141
- objectdestroy.23Tm
CStrings:
+ "T@\"NSCharacterSet\",&,N,V_unicodeDirectionalCharactersSet"
+ "TB,N,V_hasPendingUpdates"
+ "TB,N,V_hasUpdated"
+ "VMD(%s) estimatedAccountCount: %ld"
+ "VMD(%s) isMessageWaiting: %{bool}d"
+ "VMD(%s) isSubscribed: %{bool}d"
+ "VMD(%s) online: %{bool}d"
+ "VMD(%s) storageUsage: %lu"
+ "Voicemail application shortcut unchanged, hasEnhancedVoicemail: %d"
+ "_hasPendingUpdates"
+ "_hasUpdated"
+ "_unicodeDirectionalCharactersSet"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "directoryExistsAtPath:"
+ "fetchRecentCalls:"
+ "hasPendingUpdates"
+ "hasUpdated"
+ "parsedNamesStrippingEmoji"
+ "performDeleteAtIndexPaths:dataSourceActions:completionBlock:"
+ "setHasPendingUpdates:"
+ "setHasUpdated:"
+ "setUnicodeDirectionalCharactersSet:"
+ "setWritingToolsBehavior:"
+ "updateRecentCalls:"
+ "updateWithRecentCalls:"
- "Voicemail application shortcut unchanged"
- "donateEventSpeakerUsed"
- "fetchRecentCalls"
- "performDeleteAtIndexPaths:completionBlock:"

```
