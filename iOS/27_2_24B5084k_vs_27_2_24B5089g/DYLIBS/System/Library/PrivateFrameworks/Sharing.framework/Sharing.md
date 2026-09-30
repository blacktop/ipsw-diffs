## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Sharing`

```diff

-2131.20.65.2.1
-  __TEXT.__text: 0x38c36c
-  __TEXT.__objc_methlist: 0x15294
-  __TEXT.__const: 0x264f4
-  __TEXT.__cstring: 0x3ba05
-  __TEXT.__gcc_except_tab: 0x35f0
-  __TEXT.__oslogstring: 0xc553
+2131.20.71.0.0
+  __TEXT.__text: 0x38cb78
+  __TEXT.__objc_methlist: 0x152fc
+  __TEXT.__const: 0x26544
+  __TEXT.__cstring: 0x3ba15
+  __TEXT.__gcc_except_tab: 0x35f8
+  __TEXT.__oslogstring: 0xc703
   __TEXT.__dlopen_cstrs: 0x687
   __TEXT.__ustring: 0xf0
   __TEXT.__swift5_typeref: 0x9aa6

   __TEXT.__swift_as_ret: 0x4a8
   __TEXT.__swift_as_cont: 0xd00
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x13b40
+  __TEXT.__unwind_info: 0x13b68
   __TEXT.__eh_frame: 0x105ec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9bb0
+  __DATA_CONST.__objc_selrefs: 0x9c08
   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x448
   __DATA_CONST.__got: 0x1410
   __AUTH_CONST.__const: 0x1d050
-  __AUTH_CONST.__cfstring: 0x137a0
-  __AUTH_CONST.__objc_const: 0x3ca20
+  __AUTH_CONST.__cfstring: 0x137e0
+  __AUTH_CONST.__objc_const: 0x3cdf0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_dictobj: 0x5c8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x2cb8
-  __AUTH.__objc_data: 0x7af8
-  __AUTH.__data: 0x5188
-  __DATA.__objc_ivar: 0x25b4
-  __DATA.__data: 0xd590
+  __AUTH.__objc_data: 0x3f10
+  __AUTH.__data: 0x3c88
+  __DATA.__objc_ivar: 0x25bc
+  __DATA.__data: 0xd4b8
   __DATA.__common: 0x160
-  __DATA_DIRTY.__objc_data: 0x1080
-  __DATA_DIRTY.__data: 0x2f0
+  __DATA_DIRTY.__objc_data: 0x4c68
+  __DATA_DIRTY.__data: 0x1940
   __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25372
-  Symbols:   24005
-  CStrings:  9033
+  Functions: 25387
+  Symbols:   24029
+  CStrings:  9041
 
Symbols:
+ -[SFAutoUnlockNotificationModel authToken]
+ -[SFAutoUnlockNotificationModel setAuthToken:]
+ -[SFCollaborationPerformer _failIfMetadataLoadFailed]
+ -[SFCollaborationPerformer _isOptionsLoadInFlightForItem:]
+ -[SFCollaborationPerformer _performAfterOptionsCheck]
+ -[SFCollaborationPerformer _stopWaitingForOptionsLoad]
+ -[SFCollaborationPerformer isWaitingForOptionsLoad]
+ -[SFCollaborationPerformer observable:didChange:]
+ -[SFCollaborationPerformer setIsWaitingForOptionsLoad:]
+ GCC_except_table65
+ _OBJC_IVAR_$_SFAutoUnlockNotificationModel._authToken
+ _OBJC_IVAR_$_SFCollaborationPerformer._isWaitingForOptionsLoad
+ __OBJC_CLASS_PROTOCOLS_$_SFCollaborationPerformer
+ ___53-[SFCollaborationPerformer _performAfterOptionsCheck]_block_invoke
+ ___53-[SFCollaborationPerformer _performAfterOptionsCheck]_block_invoke_2
+ ___54-[SFCollaborationPerformer _stopWaitingForOptionsLoad]_block_invoke
+ _objc_msgSend$_failIfMetadataLoadFailed
+ _objc_msgSend$_isOptionsLoadInFlightForItem:
+ _objc_msgSend$_performAfterOptionsCheck
+ _objc_msgSend$_stopWaitingForOptionsLoad
+ _objc_msgSend$authToken
+ _objc_msgSend$inheritedParticipants
+ _objc_msgSend$isCurrentUser
+ _objc_msgSend$isReadOnly
+ _objc_msgSend$isWaitingForOptionsLoad
+ _objc_msgSend$setAuthToken:
+ _objc_msgSend$setIsWaitingForOptionsLoad:
- GCC_except_table40
- ___63-[SFCollaborationPerformer _performWithAddParticipantsAllowed:]_block_invoke
- ___63-[SFCollaborationPerformer _performWithAddParticipantsAllowed:]_block_invoke_2
CStrings:
+ "%@: cannot set allowsAccessRequests:%s, share options have not loaded"
+ "%@: cannot set isPublicCollaboration:%s, share options have not loaded"
+ "Collaboration Performer for item %@ resuming after options loaded"
+ "Collaboration Performer for item %@ resuming without options after loading finished"
+ "Collaboration Performer for item %@ waiting for options to load before performing"
+ "Mac17,5"
+ "MacBookNeo"
+ "canShowShareOptions:no, the share options are read-only"
```
