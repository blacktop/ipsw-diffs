## BulletinDistributorCompanion

> `/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion`

```diff

-381.0.17.0.0
-  __TEXT.__text: 0x80c38
+381.0.19.0.0
+  __TEXT.__text: 0x806ec
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x9ddc
-  __TEXT.__cstring: 0x4221
+  __TEXT.__objc_methlist: 0x9d24
+  __TEXT.__cstring: 0x41c0
   __TEXT.__const: 0x1d0
-  __TEXT.__gcc_except_tab: 0xa28
-  __TEXT.__oslogstring: 0x5237
+  __TEXT.__gcc_except_tab: 0xa08
+  __TEXT.__oslogstring: 0x53d4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1e50
-  __TEXT.__objc_classname: 0x1610
-  __TEXT.__objc_methname: 0x13a76
-  __TEXT.__objc_methtype: 0x36a0
-  __TEXT.__objc_stubs: 0xce40
-  __DATA_CONST.__got: 0x960
-  __DATA_CONST.__const: 0x1e20
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __TEXT.__unwind_info: 0x1e18
+  __TEXT.__objc_classname: 0x15db
+  __TEXT.__objc_methname: 0x138bb
+  __TEXT.__objc_methtype: 0x368f
+  __TEXT.__objc_stubs: 0xcda0
+  __DATA_CONST.__got: 0x950
+  __DATA_CONST.__const: 0x1dd0
+  __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x45a8
+  __DATA_CONST.__objc_selrefs: 0x4560
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__auth_got: 0x5a0
-  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0x18598
+  __AUTH_CONST.__objc_const: 0x18308
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2df0
-  __DATA.__objc_ivar: 0xa98
+  __AUTH.__objc_data: 0x2d50
+  __DATA.__objc_ivar: 0xa7c
   __DATA.__data: 0x1050
   __DATA.__bss: 0x290
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CDBD5F00-C155-3516-9CD4-1C689F794FEC
-  Functions: 3671
-  Symbols:   12079
-  CStrings:  5362
+  UUID: 64CC699E-0705-3C5B-92A6-1368BF8BE160
+  Functions: 3650
+  Symbols:   12005
+  CStrings:  5345
 
Symbols:
+ -[BLTBulletinDistributor _reloadBulletins]
+ -[BLTBulletinDistributor _sendCurrentBulletinIdentifiers:]
+ -[BLTBulletinDistributor handleAction:bulletin:]
+ -[BLTBulletinDistributor willSendLightsAndSirensWithRecordID:inPhoneSection:systemApp:completion:]
+ GCC_except_table103
+ GCC_except_table70
+ GCC_except_table97
+ ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke.131
+ ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke.141
+ ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke.142
+ ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke_2.143
+ ___42-[BLTBulletinDistributor _reloadBulletins]_block_invoke
+ ___42-[BLTBulletinDistributor _reloadBulletins]_block_invoke_2
+ ___42-[BLTBulletinDistributor _reloadBulletins]_block_invoke_3
+ ___42-[BLTBulletinDistributor _reloadBulletins]_block_invoke_4
+ ___42-[BLTBulletinDistributor _reloadBulletins]_block_invoke_5
+ ___48-[BLTBulletinDistributor _handleAllSyncComplete]_block_invoke.84
+ ___48-[BLTBulletinDistributor _handleAllSyncComplete]_block_invoke.85
+ ___48-[BLTBulletinDistributor handleAction:bulletin:]_block_invoke
+ ___48-[BLTBulletinDistributor handleAction:bulletin:]_block_invoke.154
+ ___48-[BLTBulletinDistributor handleAction:bulletin:]_block_invoke.154.cold.1
+ ___48-[BLTBulletinDistributor handleAction:bulletin:]_block_invoke.cold.1
+ ___48-[BLTBulletinDistributor handleAction:bulletin:]_block_invoke.cold.2
+ ___48-[BLTBulletinDistributor handleAction:bulletin:]_block_invoke.cold.3
+ ___49-[BLTBulletinDistributor _startBulletinListening]_block_invoke.83
+ ___58-[BLTBulletinDistributor _sendCurrentBulletinIdentifiers:]_block_invoke
+ ___58-[BLTBulletinDistributor _sendCurrentBulletinIdentifiers:]_block_invoke_2
+ ___66-[BLTBulletinDistributor _subscriberWillAllowBulletin:completion:]_block_invoke.126
+ ___83-[BLTBulletinDistributor removeBulletinWithPublisherBulletinID:recordID:sectionID:]_block_invoke.cold.1
+ ___98-[BLTBulletinDistributor willSendLightsAndSirensWithRecordID:inPhoneSection:systemApp:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e27_v32?0"BBBulletin"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSArray"8"NSString"16?<v?>24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.82
+ _objc_msgSend$_reloadBulletins
+ _objc_msgSend$_sendCurrentBulletinIdentifiers:
+ _objc_msgSend$bbObserver
+ _objc_msgSend$bulletinFetcher
+ _objc_msgSend$handleAction:bulletin:
+ _objc_msgSend$setObserverOptions:
+ _objc_msgSend$willSendLightsAndSirensWithRecordID:inPhoneSection:systemApp:completion:
- -[BLTBulletinDistributor _bulletinWithPublisherBulletinID:recordID:sectionID:]
- -[BLTBulletinDistributor _notifyGizmoOfBulletin:forFeed:updateType:playLightsAndSirens:shouldSendReplyIfNeeded:attachment:attachmentType:replyToken:].cold.1
- -[BLTBulletinDistributor _reloadBulletinsWithCompletion:]
- -[BLTBulletinDistributor _rememberBulletin:forFeed:syncChangesToWatch:]
- -[BLTBulletinDistributor _sendCurrentBulletinIdentifiers]
- -[BLTBulletinDistributor bulletins]
- -[BLTBulletinDistributor setBulletins:]
- -[BLTBulletinStorageBulletin .cxx_destruct]
- -[BLTBulletinStorageBulletin bulletin]
- -[BLTBulletinStorageBulletin contextSize]
- -[BLTBulletinStorageBulletin setBulletin:]
- -[BLTBulletinStorageSection .cxx_destruct]
- -[BLTBulletinStorageSection addOrReplaceBulletin:]
- -[BLTBulletinStorageSection bulletinIDToBulletin]
- -[BLTBulletinStorageSection bulletins]
- -[BLTBulletinStorageSection initWithMaxContextSize:]
- -[BLTBulletinStorageSection maxContextSize]
- -[BLTBulletinStorageSection removeBulletin:]
- -[BLTBulletinStorageSection totalContextSize]
- GCC_except_table116
- GCC_except_table122
- GCC_except_table33
- GCC_except_table78
- GCC_except_table86
- _OBJC_CLASS_$_BLTBulletinStorageBulletin
- _OBJC_CLASS_$_BLTBulletinStorageSection
- _OBJC_IVAR_$_BLTBulletinDistributor._bulletins
- _OBJC_IVAR_$_BLTBulletinStorageBulletin._bulletin
- _OBJC_IVAR_$_BLTBulletinStorageBulletin._contextSize
- _OBJC_IVAR_$_BLTBulletinStorageSection._bulletinIDToBulletin
- _OBJC_IVAR_$_BLTBulletinStorageSection._bulletins
- _OBJC_IVAR_$_BLTBulletinStorageSection._maxContextSize
- _OBJC_IVAR_$_BLTBulletinStorageSection._totalContextSize
- _OBJC_METACLASS_$_BLTBulletinStorageBulletin
- _OBJC_METACLASS_$_BLTBulletinStorageSection
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __OBJC_$_INSTANCE_METHODS_BLTBulletinStorageBulletin
- __OBJC_$_INSTANCE_METHODS_BLTBulletinStorageSection
- __OBJC_$_INSTANCE_VARIABLES_BLTBulletinStorageBulletin
- __OBJC_$_INSTANCE_VARIABLES_BLTBulletinStorageSection
- __OBJC_$_PROP_LIST_BLTBulletinStorageBulletin
- __OBJC_$_PROP_LIST_BLTBulletinStorageSection
- __OBJC_CLASS_RO_$_BLTBulletinStorageBulletin
- __OBJC_CLASS_RO_$_BLTBulletinStorageSection
- __OBJC_METACLASS_RO_$_BLTBulletinStorageBulletin
- __OBJC_METACLASS_RO_$_BLTBulletinStorageSection
- ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke.177
- ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke.187
- ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke.188
- ___122-[BLTBulletinDistributor observer:addBulletin:forFeed:playLightsAndSirens:attachment:attachmentType:alwaysSend:withReply:]_block_invoke_2.189
- ___39-[BLTBulletinDistributor handleAction:]_block_invoke.200
- ___39-[BLTBulletinDistributor handleAction:]_block_invoke.200.cold.1
- ___39-[BLTBulletinDistributor handleAction:]_block_invoke.cold.2
- ___39-[BLTBulletinDistributor handleAction:]_block_invoke.cold.3
- ___39-[BLTBulletinDistributor handleAction:]_block_invoke.cold.4
- ___48-[BLTBulletinDistributor _handleAllSyncComplete]_block_invoke.128
- ___48-[BLTBulletinDistributor _handleAllSyncComplete]_block_invoke.129
- ___48-[BLTBulletinDistributor _handleAllSyncComplete]_block_invoke_2
- ___49-[BLTBulletinDistributor _startBulletinListening]_block_invoke.127
- ___50-[BLTBulletinStorageSection addOrReplaceBulletin:]_block_invoke
- ___57-[BLTBulletinDistributor _reloadBulletinsWithCompletion:]_block_invoke
- ___57-[BLTBulletinDistributor _reloadBulletinsWithCompletion:]_block_invoke_2
- ___57-[BLTBulletinDistributor _reloadBulletinsWithCompletion:]_block_invoke_3
- ___57-[BLTBulletinDistributor _reloadBulletinsWithCompletion:]_block_invoke_4
- ___57-[BLTBulletinDistributor _reloadBulletinsWithCompletion:]_block_invoke_5
- ___57-[BLTBulletinDistributor _sendCurrentBulletinIdentifiers]_block_invoke
- ___57-[BLTBulletinDistributor _sendCurrentBulletinIdentifiers]_block_invoke_2
- ___57-[BLTBulletinDistributor _sendCurrentBulletinIdentifiers]_block_invoke_3
- ___57-[BLTBulletinDistributor _sendCurrentBulletinIdentifiers]_block_invoke_4
- ___66-[BLTBulletinDistributor _subscriberWillAllowBulletin:completion:]_block_invoke.172
- ___71-[BLTBulletinDistributor _rememberBulletin:forFeed:syncChangesToWatch:]_block_invoke
- ___71-[BLTBulletinDistributor _rememberBulletin:forFeed:syncChangesToWatch:]_block_invoke.cold.1
- ___71-[BLTBulletinDistributor _rememberBulletin:forFeed:syncChangesToWatch:]_block_invoke.cold.2
- ___block_descriptor_40_e8_32s_e27_v32?0"BBBulletin"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e39_v32?0"NSArray"8"NSString"16?<v?>24ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e22_v16?0"NSDictionary"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e43_v32?0"BLTBulletinStorageBulletin"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e52_v32?0"NSString"8"BLTBulletinStorageSection"16^B24ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48r_e27_v32?0"BBBulletin"8Q16^B24ls32l8r48l8s40l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.126
- ___block_literal_global.96
- _objc_msgSend$_bulletinWithPublisherBulletinID:recordID:sectionID:
- _objc_msgSend$_reloadBulletinsWithCompletion:
- _objc_msgSend$_rememberBulletin:forFeed:syncChangesToWatch:
- _objc_msgSend$_sendCurrentBulletinIdentifiers
- _objc_msgSend$addOrReplaceBulletin:
- _objc_msgSend$bulletinIDToBulletin
- _objc_msgSend$bulletins
- _objc_msgSend$contextSize
- _objc_msgSend$initWithMaxContextSize:
- _objc_msgSend$removeBulletin:
- _objc_msgSend$removeFirstObject
- _objc_msgSend$sizeOfObject:
CStrings:
+ "%@ _reloadBulletins: obsoletionDate: %@"
+ "%@ _reloadBulletins: obsoletionDate: %@ bulletinFetcher: %@"
+ "%@ _reloadBulletins: obsoletionDate: %@ complete"
+ "%@ _sendCurrentBulletinIdentifiers: bulletinIdentifiersBySectionID: %@"
+ "%@ _sendCurrentBulletinIdentifiers: fullList: %@"
+ "%@ _setupBBObserver"
+ "%@ _setupBBObserver: %@"
+ "%@ handleAction: %@"
+ "%@ handleAction: %@ bulletins: %@"
+ "%@ observer: %@ modifyBulletin: %@ feed: %lu"
+ "%@ observer: %@ removeBulletin: %@ feed: %lu"
+ "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ phoneSectionID: %@ - failed no bulletin found"
+ "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ phoneSectionID: %@ bulletin: %@"
+ "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ sectionID: %@"
+ "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ sectionID: %@ - failed no bulletin found"
+ "%@ removeBulletinWithPublisherBulletinID: %@ recordID: %@ sectionID: %@ bulletin: %@"
+ "%@ willSendLightsAndSirensWithPublisherBulletinID: %@ recordID: %@ phoneSectionID: %@"
+ "_reloadBulletins"
+ "_sendCurrentBulletinIdentifiers:"
+ "handleAction:bulletin:"
+ "setObserverOptions:"
+ "willSendLightsAndSirensWithRecordID:inPhoneSection:systemApp:completion:"
- "B36@0:8@16Q24B32"
- "BLTBulletinStorageBulletin"
- "BLTBulletinStorageSection"
- "Could not find matching bulletin"
- "Couldn't store bulletin. Not sending to gizmo sectionID: %@ publisherMatch: %@"
- "Exceeded space for bulletins. Dropping bulletin from coordination sectionID: %@ publisherMatch: %@"
- "Found matching bulletin: %@"
- "Not going to store/coordinate bulletin sectionID: %@ publisherMatch: %@"
- "Received remove bulletin for publisherBulletinID: %@, recordID: %@, sectionID %@"
- "Section %@ exceeded max size (%lu). Total size is %lu"
- "Setting up BB Observer"
- "T@\"NSMutableArray\",R,N,V_bulletins"
- "T@\"NSMutableDictionary\",&,N,V_bulletins"
- "T@\"NSMutableDictionary\",R,N,V_bulletinIDToBulletin"
- "TQ,R,N,V_contextSize"
- "TQ,R,N,V_maxContextSize"
- "TQ,R,N,V_totalContextSize"
- "_bulletinIDToBulletin"
- "_bulletinWithPublisherBulletinID:recordID:sectionID:"
- "_bulletins"
- "_contextSize"
- "_maxContextSize"
- "_reloadBulletinsWithCompletion:"
- "_rememberBulletin:forFeed:syncChangesToWatch:"
- "_sendCurrentBulletinIdentifiers"
- "_totalContextSize"
- "addOrReplaceBulletin:"
- "bulletinIDToBulletin"
- "bulletins"
- "contextSize"
- "initWithMaxContextSize:"
- "maxContextSize"
- "removeBulletin:"
- "removeFirstObject"
- "setBulletins:"
- "totalContextSize"
- "v32@?0@\"BLTBulletinStorageBulletin\"8Q16^B24"
- "v32@?0@\"NSString\"8@\"BLTBulletinStorageSection\"16^B24"
- "willSendLightsAndSirensWithPublisherBulletinID: found a stored bulletin for sectionID: %@ publisherMatchID: %@"

```
