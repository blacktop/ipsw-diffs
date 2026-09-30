## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.200.35.2.5
-  __TEXT.__text: 0x224d90
-  __TEXT.__auth_stubs: 0x4500
-  __TEXT.__objc_methlist: 0x7074
+1450.200.75.0.0
+  __TEXT.__text: 0x220bf0
+  __TEXT.__auth_stubs: 0x4530
+  __TEXT.__objc_methlist: 0x710c
   __TEXT.__const: 0xa1e8
-  __TEXT.__cstring: 0x47aeb
-  __TEXT.__oslogstring: 0x1d7a6
-  __TEXT.__gcc_except_tab: 0xf898
+  __TEXT.__cstring: 0x47afb
+  __TEXT.__oslogstring: 0x1d7b6
+  __TEXT.__gcc_except_tab: 0xd054
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4ccc
-  __TEXT.__swift5_typeref: 0x322c
+  __TEXT.__swift5_typeref: 0x324c
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_reflstr: 0x2ac1
   __TEXT.__swift5_fieldmd: 0x2d50

   __TEXT.__swift5_proto: 0x664
   __TEXT.__swift5_types: 0x31c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_capture: 0xf50
+  __TEXT.__swift5_capture: 0xfb0
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8c88
+  __TEXT.__unwind_info: 0x87b8
   __TEXT.__eh_frame: 0x6de8
   __TEXT.__objc_classname: 0x11ad
-  __TEXT.__objc_methname: 0x175bf
-  __TEXT.__objc_methtype: 0x36e2
-  __TEXT.__objc_stubs: 0x11940
+  __TEXT.__objc_methname: 0x177ac
+  __TEXT.__objc_methtype: 0x371a
+  __TEXT.__objc_stubs: 0x11a40
   __DATA_CONST.__got: 0x16f8
-  __DATA_CONST.__const: 0x8358
+  __DATA_CONST.__const: 0x8330
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51a8
+  __DATA_CONST.__objc_selrefs: 0x5200
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x2290
-  __AUTH_CONST.__const: 0x9748
+  __AUTH_CONST.__auth_got: 0x22a8
+  __AUTH_CONST.__const: 0x9878
   __AUTH_CONST.__cfstring: 0x11ea0
-  __AUTH_CONST.__objc_const: 0xf278
+  __AUTH_CONST.__objc_const: 0xf320
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1b10
-  __AUTH.__data: 0x4088
-  __DATA.__objc_ivar: 0x478
-  __DATA.__data: 0x2bd0
-  __DATA.__bss: 0xa2d0
-  __DATA.__common: 0x178
+  __AUTH.__data: 0x3e78
+  __DATA.__objc_ivar: 0x484
+  __DATA.__data: 0x2b90
+  __DATA.__bss: 0x9fe0
+  __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x1620
-  __DATA_DIRTY.__data: 0x3d30
-  __DATA_DIRTY.__bss: 0x1be8
-  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__data: 0x3f40
+  __DATA_DIRTY.__bss: 0x1ee8
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2363C775-BE46-399F-B3DB-51282511AB84
-  Functions: 10479
-  Symbols:   2557
-  CStrings:  12224
+  UUID: C41C9A2A-8081-35DA-BBC8-4B433D47A066
+  Functions: 10515
+  Symbols:   2563
+  CStrings:  12243
 
Symbols:
+ _IMAttachmentsLogHandle
+ _IMCoreDuetLogHandle
+ _IMDNotificationsControllerLogHandle
+ _IMDatabaseMessageEventLogHandle
+ _OBJC_CLASS_$_IMBackpressuredDonationController
+ _OBJC_METACLASS_$_IMBackpressuredDonationController
+ _dispatch_assert_queue$V2
- _objc_retain_x7
CStrings:
+ "Attempted to get record identifier for NULL attachment record"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B80@0:8@16@24@32@40@48@56@64q72"
+ "DomainIdentifiers"
+ "Getting attachment record for attachment guid %@"
+ "No latest identifier in the iMessage Group ID domain for chat: %@"
+ "T@\"NSLock\",R,N,V_indexingDisabledLock"
+ "T@\"NSMutableOrderedSet\",&,N,V_pendingDonations"
+ "T@\"NSString\",R,D,N"
+ "TB,N,GisIndexingDisabled,V_indexingDisabled"
+ "UPDATE message SET guid =  ?  WHERE guid =  ? ;"
+ "__im_uniqueChatIdentifierForGroupChat"
+ "__kchatDomainIdentifiersKey"
+ "__unlocked_cancel"
+ "__unlocked_reload"
+ "_chatIsMutedBasedOnChatGUID:chatIdentifier:groupID:domainIdentifiers:handles:lastAddressedHandleString:originalGroupID:style:"
+ "_disableIndexing"
+ "_enableIndexing"
+ "_indexingDisabled"
+ "_indexingDisabledLock"
+ "_itemDonationTriggersChatPostProcessingForContext:"
+ "ckChatID"
+ "com.apple.IMIndexThrottleMonitor"
+ "indexingDisabled"
+ "indexingDisabledLock"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "isFilterUnknownSendersEnabled"
+ "isIndexingDisabled"
+ "muteIdentifiersForChatStyle:groupID:domainIdentifiers:participantIDs:lastAddressedHandleID:originalGroupID:chatIdentifier:"
+ "orderedSetWithArray:"
+ "reassignIdentifierForMessageWithGUID:newGUID:completionHandler:"
+ "removeObjectsAtIndexes:"
+ "scheduleGUIDs:flag:lane:reason:userInfo:completionBlock:"
+ "setIndexingDisabled:"
+ "unionOrderedSet:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "@\"IMDPersistentTask\"16@?0@\"NSString\"8"
- "Attempted to get record identifier for NULL attachment record: %@"
- "B72@0:8@16@24@32@40@48@56q64"
- "FilterMessageRequests"
- "IMDIndexing_CoreDuet"
- "IMDIndexing_CureDuet"
- "T@\"NSMutableArray\",&,N,V_pendingDonations"
- "We have never set the filtering default, check if we should be doing it by default %@"
- "__kchatOriginalGroupIDKey"
- "_chatIsMutedBasedOnChatGUID:chatIdentifier:groupID:handles:lastAddressedHandleString:originalGroupID:style:"
- "filteringKeySet"
- "generatedRoomNameForGroupChat"
- "isUnknownSenderFilteringOn"
- "muteIdentifiersForChatStyle:groupID:participantIDs:lastAddressedHandleID:originalGroupID:chatIdentifier:"
- "removeObjectsInRange:"
- "scheduleMessageGUIDs:flag:lane:reason:userInfo:completionBlock:"
- "strongToStrongObjectsMapTable"

```
