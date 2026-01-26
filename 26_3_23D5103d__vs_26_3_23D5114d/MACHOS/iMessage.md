## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.400.13.2.1
-  __TEXT.__text: 0xbb930
+1450.400.42.0.0
+  __TEXT.__text: 0xba28c
   __TEXT.__auth_stubs: 0x1b90
-  __TEXT.__objc_stubs: 0xc660
-  __TEXT.__objc_methlist: 0x2b94
+  __TEXT.__objc_stubs: 0xc3a0
+  __TEXT.__objc_methlist: 0x298c
   __TEXT.__const: 0xe68
-  __TEXT.__gcc_except_tab: 0xaa58
+  __TEXT.__gcc_except_tab: 0xa910
   __TEXT.__cstring: 0x34bd
-  __TEXT.__oslogstring: 0x16e7b
-  __TEXT.__objc_classname: 0x54a
-  __TEXT.__objc_methname: 0x128a5
-  __TEXT.__objc_methtype: 0x2a3f
+  __TEXT.__oslogstring: 0x16cab
+  __TEXT.__objc_classname: 0x50c
+  __TEXT.__objc_methname: 0x12386
+  __TEXT.__objc_methtype: 0x2a1c
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x676
   __TEXT.__constg_swiftt: 0x368

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x22a8
+  __TEXT.__unwind_info: 0x2278
   __TEXT.__eh_frame: 0x8d8
   __DATA_CONST.__auth_got: 0xdd8
-  __DATA_CONST.__got: 0x1038
+  __DATA_CONST.__got: 0x1048
   __DATA_CONST.__auth_ptr: 0x1c8
   __DATA_CONST.__const: 0x38d0
   __DATA_CONST.__cfstring: 0x3820
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x390
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3278
-  __DATA.__objc_selrefs: 0x3a98
-  __DATA.__objc_ivar: 0x20c
-  __DATA.__objc_data: 0xa58
+  __DATA.__objc_const: 0x2e08
+  __DATA.__objc_selrefs: 0x39e8
+  __DATA.__objc_ivar: 0x1c8
+  __DATA.__objc_data: 0x9b8
   __DATA.__data: 0xa58
   __DATA.__bss: 0x8f0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25A7C90D-1A36-31B1-A981-49CA4600823B
-  Functions: 1666
-  Symbols:   873
-  CStrings:  5126
+  UUID: CCBCEEA0-D71D-3990-83D8-0A58258DE34D
+  Functions: 1625
+  Symbols:   871
+  CStrings:  5054
 
Symbols:
+ _OBJC_CLASS_$_IMDGroupConvergenceContext
+ _OBJC_CLASS_$_IMDGroupParticipantConvergenceResult
- _OBJC_CLASS_$_GroupConvergenceContext
- _OBJC_CLASS_$_GroupParticipantConvergenceResult
- _OBJC_METACLASS_$_GroupConvergenceContext
- _OBJC_METACLASS_$_GroupParticipantConvergenceResult
CStrings:
- "   Adding participant: %@"
- "   I was removed from this chat, leaving"
- "   Participants to be removed %@"
- "   Removing participant: %@"
- " Adding participant explicitly: %@"
- " I was added to a chat, so updating chat status"
- " Removing participant explicitly: %@"
- " Updating participants: %@   toIdentifier: %@, fromIdentifier :%@, updateType %lu, allowSelfRemoval %@"
- "@32@0:8Q16@24"
- "C"
- "C16@0:8"
- "Chat participants after converge %@"
- "Chat participants before converge %@"
- "Group changed and will write to db? %@"
- "GroupConvergenceContext"
- "GroupParticipantConvergenceResult"
- "T@\"IMDAccount\",&,N,V_account"
- "T@\"NSArray\",&,N,V_currentParticipants"
- "T@\"NSArray\",&,N,V_participantsToAdd"
- "T@\"NSArray\",&,N,V_participantsToRemove"
- "T@\"NSArray\",&,N,V_toParticipants"
- "T@\"NSArray\",R,N,V_chatStatusChanges"
- "T@\"NSArray\",R,N,V_memberStatusChanges"
- "T@\"NSDictionary\",&,N,V_participantChangeGUIDs"
- "T@\"NSString\",&,N,V_chatIdentifier"
- "T@\"NSString\",&,N,V_fromIdentifier"
- "T@\"NSString\",&,N,V_groupID"
- "T@\"NSString\",&,N,V_messageID"
- "T@\"NSString\",&,N,V_toIdentifier"
- "TB,N,V_allowSelfRemoval"
- "TB,N,V_isBlackholed"
- "TB,N,V_isReflection"
- "TC,N,V_chatStyle"
- "_allowSelfRemoval"
- "_chatIdentifier"
- "_chatStatusChanges"
- "_chatStyle"
- "_currentParticipants"
- "_fromIdentifier"
- "_groupID"
- "_isBlackholed"
- "_isReflection"
- "_memberStatusChanges"
- "_messageID"
- "_messageIDForUpdateType:participant:"
- "_participantChangeGUIDs"
- "_participantsToAdd"
- "_participantsToRemove"
- "_toIdentifier"
- "_toParticipants"
- "allowSelfRemoval"
- "chatStatusChangeContextForUpdateType:participant:"
- "chatStatusChanges"
- "currentParticipants"
- "didUpdateChatStatusWithContext:"
- "initWithMemberStatusChanges:chatStatusChanges:"
- "isEqualToArray:"
- "isReflection"
- "memberStatusChangeContextForUpdateType:participant:"
- "memberStatusChanges"
- "participantChangeGUIDs"
- "participantsToAdd"
- "participantsToRemove"
- "setChatStatus:"
- "setChatStyle:"
- "setCurrentParticipants:"
- "setFromHandleID:"
- "setUnattributed:"
- "toParticipants"
- "v20@0:8C16"

```
