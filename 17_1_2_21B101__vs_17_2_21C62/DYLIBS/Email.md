## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0x96e04
+3774.300.61.2.4
+  __TEXT.__text: 0x973fc
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x8744
-  __TEXT.__gcc_except_tab: 0x13780
+  __TEXT.__objc_methlist: 0x87c4
+  __TEXT.__gcc_except_tab: 0x13838
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x7aaa
-  __TEXT.__oslogstring: 0x3f97
+  __TEXT.__cstring: 0x7b20
+  __TEXT.__oslogstring: 0x3fdd
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x6134
-  __TEXT.__objc_classname: 0x1732
-  __TEXT.__objc_methname: 0x1697e
+  __TEXT.__unwind_info: 0x6180
+  __TEXT.__objc_classname: 0x1748
+  __TEXT.__objc_methname: 0x16a06
   __TEXT.__objc_methtype: 0x3f30
-  __TEXT.__objc_stubs: 0xf140
+  __TEXT.__objc_stubs: 0xf200
   __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x3408
-  __DATA_CONST.__objc_classlist: 0x490
+  __DATA_CONST.__const: 0x3480
+  __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x112f0
-  __DATA_CONST.__objc_selrefs: 0x4e78
+  __DATA_CONST.__objc_const: 0x11448
+  __DATA_CONST.__objc_selrefs: 0x4e90
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x7140
-  __AUTH_CONST.__objc_const: 0x4838
-  __AUTH_CONST.__const: 0xd60
+  __AUTH_CONST.__cfstring: 0x71a0
+  __AUTH_CONST.__objc_const: 0x4880
+  __AUTH_CONST.__const: 0xd80
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x5a8
-  __AUTH.__objc_data: 0x5f0
+  __AUTH.__objc_data: 0x640
   __DATA.__objc_protorefs: 0x100
   __DATA.__objc_classrefs: 0x780
   __DATA.__objc_superrefs: 0x3b0
-  __DATA.__objc_ivar: 0x9e0
+  __DATA.__objc_ivar: 0x9e4
   __DATA.__data: 0x22b0
   __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x27b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5418201-2062-3160-B53D-FAB46C3F457F
-  Functions: 3543
-  Symbols:   14423
-  CStrings:  6772
+  UUID: 63478B43-6A78-3683-945D-5811AB8D69E6
+  Functions: 3552
+  Symbols:   14465
+  CStrings:  6785
 
Symbols:
+ +[EMMessageListItemPredicates isValidPredicate:forClass:]
+ -[EMBlockedSenderManager _locked_repopulateBlockedSenderCachedState:]
+ -[EMDiagnosticInfoGatherer searchableIndexDatabaseStatisticsWithCompletionHandler:]
+ -[EMFollowUp ef_publicDescription]
+ -[EMOutgoingMessageRepository addOutgoingMessageRepositoryObserver:]
+ -[EMOutgoingMessageRepository removeOutgoingMessageRepositoryObserver:]
+ -[EMQuery isValid]
+ -[EMReadLater ef_publicDescription]
+ -[_EMBlockedSenderState .cxx_destruct]
+ -[_EMBlockedSenderState blockedSenders]
+ -[_EMBlockedSenderState setBlockedSenders:]
+ -[_EMBlockedSenderState setValid:]
+ -[_EMBlockedSenderState valid]
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table196
+ _EMUserDefaultDisableQueryLogSubmission
+ _OBJC_CLASS_$__EMBlockedSenderState
+ _OBJC_IVAR_$__EMBlockedSenderState._blockedSenders
+ _OBJC_IVAR_$__EMBlockedSenderState._valid
+ _OBJC_METACLASS_$__EMBlockedSenderState
+ __OBJC_$_INSTANCE_METHODS__EMBlockedSenderState
+ __OBJC_$_INSTANCE_VARIABLES__EMBlockedSenderState
+ __OBJC_$_PROP_LIST__EMBlockedSenderState
+ __OBJC_CLASS_RO_$__EMBlockedSenderState
+ __OBJC_METACLASS_RO_$__EMBlockedSenderState
+ ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.304
+ ___48-[EMMessageRepository _blockedSendersDidChange:]_block_invoke.449
+ ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.301
+ ___54-[EMBlockedSenderManager _blockedSenderListDidChange:]_block_invoke
+ ___57+[EMMessageListItemPredicates isValidPredicate:forClass:]_block_invoke
+ ___68-[EMOutgoingMessageRepository addOutgoingMessageRepositoryObserver:]_block_invoke
+ ___69-[EMBlockedSenderManager _locked_repopulateBlockedSenderCachedState:]_block_invoke
+ ___71-[EMOutgoingMessageRepository removeOutgoingMessageRepositoryObserver:]_block_invoke
+ ___block_descriptor_32_e28_v16?0"<EMMessageBuilder>"8l
+ ___block_descriptor_40_ea8_32s_e31_v16?0"_EMBlockedSenderState"8ls32l8
+ ___block_descriptor_48_ea8_32s40r_e31_v16?0"_EMBlockedSenderState"8ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40s48r_e31_v16?0"_EMBlockedSenderState"8ls32l8r48l8s40l8
+ ___block_literal_global.306
+ ___block_literal_global.443
+ ___block_literal_global.455
+ _objc_msgSend$_locked_repopulateBlockedSenderCachedState:
+ _objc_msgSend$blockedSenders
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$initWithObjectID:builder:
+ _objc_msgSend$isActive
+ _objc_msgSend$isValidPredicate:forClass:
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$searchableIndexDatabaseStatisticsWithCompletionHandler:
+ _objc_msgSend$setBlockedSenders:
+ _objc_msgSend$setValid:
+ _objc_msgSend$valid
- -[EMBlockedSenderManager _resetBlockedSenderCache]
- -[EMBlockedSenderManager resetScheduler]
- -[EMBlockedSenderManager setResetScheduler:]
- -[EMOutgoingMessageRepository addOutgoingMessageObserver:]
- -[EMOutgoingMessageRepository removeOutgoingMessageObserver:]
- GCC_except_table149
- GCC_except_table151
- GCC_except_table161
- GCC_except_table166
- GCC_except_table168
- GCC_except_table171
- GCC_except_table176
- GCC_except_table178
- GCC_except_table183
- GCC_except_table188
- GCC_except_table191
- GCC_except_table194
- _OBJC_CLASS_$_NSNotification
- _OBJC_IVAR_$_EMBlockedSenderManager._resetScheduler
- ___39-[EMBlockedSenderManager test_tearDown]_block_invoke_2
- ___45-[EMDaemonInterface resetProtocolConnections]_block_invoke.303
- ___50-[EMBlockedSenderManager _resetBlockedSenderCache]_block_invoke
- ___50-[EMBlockedSenderManager _resetBlockedSenderCache]_block_invoke_2
- ___50-[EMDaemonInterface _connectionForProtocol:error:]_block_invoke.300
- ___58-[EMOutgoingMessageRepository addOutgoingMessageObserver:]_block_invoke
- ___61-[EMOutgoingMessageRepository removeOutgoingMessageObserver:]_block_invoke
- ___block_descriptor_48_ea8_32s40r_e15_v16?0"NSSet"8lr40l8s32l8
- ___block_literal_global.223
- ___block_literal_global.305
- ___block_literal_global.442
- _objc_msgSend$_resetBlockedSenderCache
- _objc_msgSend$initWithName:object:userInfo:
- _objc_msgSend$postNotification:
- _objc_msgSend$replaceObject:
- _objc_msgSend$resetScheduler
CStrings:
+ "%@\n\tObjectID:%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tSenderBucket:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tRemind Me:%@ \n\tFollow Up:%@ \n\tSummary:%@ \n\tSupportsArchiving:%@ \n\tShouldArchive:%@"
+ "Blocked sender changed for:%@ from %d to %d for addresses: %{public}@"
+ "DisableQueryLogSubmission"
+ "T@\"NSSet\",&,N,V_blockedSenders"
+ "TB,N,V_valid"
+ "Unknown targetClass:%@"
+ "_EMBlockedSenderState"
+ "_blockedSenders"
+ "_locked_repopulateBlockedSenderCachedState:"
+ "_valid"
+ "addOutgoingMessageRepositoryObserver:"
+ "blockedSenders"
+ "date:%@, isActive:%d"
+ "evaluateWithObject:"
+ "isValidPredicate:forClass:"
+ "postNotificationName:object:"
+ "removeOutgoingMessageRepositoryObserver:"
+ "searchableIndexDatabaseStatisticsWithCompletionHandler:"
+ "setBlockedSenders:"
+ "setValid:"
+ "startDate:%@, endDate:%@, isActive:%d"
+ "v16@?0@\"_EMBlockedSenderState\"8"
- "%@\n\tObjectID:%@\n\tMailboxes:%@\n\tSenderAddress:%@\n\tSubject:%@ \n\tToList:%@ \n\tCCList:%@ \n\tBCCList:%@ \n\tFlags:%@ \n\tConversationNotificationLevel:%ld \n\tSenderBucket:%ld \n\tIsVIP:%@ \n\tIsBlocked:%@ \n\tUnsubscribeType:%ld \n\tConversationID:%@ \n\tDate:%@ \n\tDisplayDate:%@ \n\tSummary:%@ \n\tSupportsArchiving:%@ \n\tShouldArchive:%@"
- "T@\"<EFScheduler>\",&,N,V_resetScheduler"
- "_resetBlockedSenderCache"
- "_resetScheduler"
- "addOutgoingMessageObserver:"
- "com.apple.email.BlockedSenderManager.resetScheduler"
- "initWithName:object:userInfo:"
- "postNotification:"
- "removeOutgoingMessageObserver:"
- "replaceObject:"
- "resetScheduler"
- "setResetScheduler:"

```
