## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1325.600.31.0.0
-  __TEXT.__text: 0x645a8
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x8a64
+1356.100.2.2.1
+  __TEXT.__text: 0x679a8
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x8fa4
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x5eb2
-  __TEXT.__oslogstring: 0x361f
-  __TEXT.__gcc_except_tab: 0x764
-  __TEXT.__unwind_info: 0x1b80
-  __TEXT.__objc_classname: 0x13f6
-  __TEXT.__objc_methname: 0x10e7a
-  __TEXT.__objc_methtype: 0x3bcf
-  __TEXT.__objc_stubs: 0xa320
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__objc_classlist: 0x3c8
+  __TEXT.__cstring: 0x6200
+  __TEXT.__oslogstring: 0x3694
+  __TEXT.__gcc_except_tab: 0x778
+  __TEXT.__unwind_info: 0x1c40
+  __TEXT.__objc_classname: 0x1471
+  __TEXT.__objc_methname: 0x11904
+  __TEXT.__objc_methtype: 0x3dc7
+  __TEXT.__objc_stubs: 0xa980
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0xd40
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31d0
+  __DATA_CONST.__objc_selrefs: 0x33a0
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x3d60
-  __AUTH_CONST.__objc_const: 0xe128
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__cfstring: 0x4240
+  __AUTH_CONST.__objc_const: 0xeb90
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0x890
+  __AUTH.__objc_data: 0x19a0
+  __DATA.__objc_ivar: 0x918
   __DATA.__data: 0x1740
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0xeb0
+  __DATA.__bss: 0x110
+  __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
+  - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libBASupport.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C1CE4370-A65A-3C67-B477-E2B0D726A465
-  Functions: 3065
-  Symbols:   10042
-  CStrings:  4465
+  UUID: C1D006EC-940C-3E2D-946C-628D6A2A5D0E
+  Functions: 3173
+  Symbols:   10374
+  CStrings:  4671
 
Symbols:
+ +[CXJoinCallParticipantCluster supportsSecureCoding]
+ +[CXMember supportsSecureCoding]
+ +[CXScreenSharingRequestMetadata supportsSecureCoding]
+ +[CXSetTranslatingCallAction supportsSecureCoding]
+ -[CXAnswerCallAction receptionist]
+ -[CXAnswerCallAction setReceptionist:]
+ -[CXCall localMemberIdentity]
+ -[CXCall setLocalMemberIdentity:]
+ -[CXCallDirectoryManager firstIdentificationEntryForEnabledExtensionSyncWithPhoneNumber:cacheOnly:]
+ -[CXCallDirectoryManager synchronousServerWithErrorHandler:]
+ -[CXCallUpdate commTrustScore]
+ -[CXCallUpdate conversationGroupUUID]
+ -[CXCallUpdate isSharePlayCapable]
+ -[CXCallUpdate isUpgradeToVideo]
+ -[CXCallUpdate launchInBackground]
+ -[CXCallUpdate nearbyMode]
+ -[CXCallUpdate remoteMember]
+ -[CXCallUpdate setCommTrustScore:]
+ -[CXCallUpdate setConversationGroupUUID:]
+ -[CXCallUpdate setIsSharePlayCapable:]
+ -[CXCallUpdate setIsUpgradeToVideo:]
+ -[CXCallUpdate setLaunchInBackground:]
+ -[CXCallUpdate setNearbyMode:]
+ -[CXCallUpdate setRemoteMember:]
+ -[CXCallUpdate setSpecialUnknown:]
+ -[CXCallUpdate setStartCallMuted:]
+ -[CXCallUpdate setSupportsRecents:]
+ -[CXCallUpdate setSupportsScreenShare:]
+ -[CXCallUpdate setSupportsSharePlay:]
+ -[CXCallUpdate specialUnknown]
+ -[CXCallUpdate startCallMuted:]
+ -[CXCallUpdate startCallMuted]
+ -[CXCallUpdate supportsRecents]
+ -[CXCallUpdate supportsScreenShare]
+ -[CXCallUpdate supportsSharePlay]
+ -[CXJoinCallAction isUpgradeToVideo]
+ -[CXJoinCallAction launchInBackground]
+ -[CXJoinCallAction participantCluster]
+ -[CXJoinCallAction screenSharingRequestMetadata]
+ -[CXJoinCallAction setIsUpgradeToVideo:]
+ -[CXJoinCallAction setLaunchInBackground:]
+ -[CXJoinCallAction setParticipantCluster:]
+ -[CXJoinCallAction setScreenSharingRequestMetadata:]
+ -[CXJoinCallParticipantCluster .cxx_destruct]
+ -[CXJoinCallParticipantCluster UUID]
+ -[CXJoinCallParticipantCluster copyWithZone:]
+ -[CXJoinCallParticipantCluster description]
+ -[CXJoinCallParticipantCluster encodeWithCoder:]
+ -[CXJoinCallParticipantCluster hash]
+ -[CXJoinCallParticipantCluster initWithCoder:]
+ -[CXJoinCallParticipantCluster initWithUUID:type:]
+ -[CXJoinCallParticipantCluster isEqual:]
+ -[CXJoinCallParticipantCluster isEqualToJoinCallParticipantCluster:]
+ -[CXJoinCallParticipantCluster type]
+ -[CXMember .cxx_destruct]
+ -[CXMember copyWithZone:]
+ -[CXMember description]
+ -[CXMember description].cold.1
+ -[CXMember encodeWithCoder:]
+ -[CXMember handle]
+ -[CXMember hash]
+ -[CXMember identityBlob]
+ -[CXMember initWithCoder:]
+ -[CXMember initWithHandle:]
+ -[CXMember initWithHandle:identityBlob:]
+ -[CXMember initWithHandle:identityBlob:stableDeviceIdentifier:]
+ -[CXMember init]
+ -[CXMember isEqual:]
+ -[CXMember isEqualToMember:]
+ -[CXMember setStableDeviceIdentifier:]
+ -[CXMember stableDeviceIdentifier]
+ -[CXProviderConfiguration setSupportsAudioTranslation:]
+ -[CXProviderConfiguration supportsAudioTranslation]
+ -[CXScreenSharingRequestMetadata .cxx_destruct]
+ -[CXScreenSharingRequestMetadata appName]
+ -[CXScreenSharingRequestMetadata bundleIdentifier]
+ -[CXScreenSharingRequestMetadata copyWithZone:]
+ -[CXScreenSharingRequestMetadata encodeWithCoder:]
+ -[CXScreenSharingRequestMetadata initWithCoder:]
+ -[CXScreenSharingRequestMetadata sanitizedCopyWithZone:]
+ -[CXScreenSharingRequestMetadata setAppName:]
+ -[CXScreenSharingRequestMetadata setBundleIdentifier:]
+ -[CXSetScreeningCallAction receptionist]
+ -[CXSetScreeningCallAction setReceptionist:]
+ -[CXSetTranslatingCallAction .cxx_destruct]
+ -[CXSetTranslatingCallAction description]
+ -[CXSetTranslatingCallAction encodeWithCoder:]
+ -[CXSetTranslatingCallAction fulfillWithTranslationEngine:]
+ -[CXSetTranslatingCallAction initWithCallUUID:isTranslating:isSystemInitiated:localLocale:remoteLocale:]
+ -[CXSetTranslatingCallAction initWithCallUUID:isTranslating:localLocale:remoteLocale:]
+ -[CXSetTranslatingCallAction initWithCoder:]
+ -[CXSetTranslatingCallAction isSystemInitiated]
+ -[CXSetTranslatingCallAction isTranslating]
+ -[CXSetTranslatingCallAction localLocale]
+ -[CXSetTranslatingCallAction remoteLocale]
+ -[CXSetTranslatingCallAction translationEngine]
+ -[CXStartCallAction isUpgradeToVideo]
+ -[CXStartCallAction launchInBackground]
+ -[CXStartCallAction setIsUpgradeToVideo:]
+ -[CXStartCallAction setLaunchInBackground:]
+ -[CXStartCallAction setStartCallMuted:]
+ -[CXStartCallAction startCallMuted]
+ GCC_except_table31
+ GCC_except_table43
+ GCC_except_table47
+ _OBJC_CLASS_$_CXJoinCallParticipantCluster
+ _OBJC_CLASS_$_CXMember
+ _OBJC_CLASS_$_CXScreenSharingRequestMetadata
+ _OBJC_CLASS_$_CXSetTranslatingCallAction
+ _OBJC_CLASS_$_CXShareIdentityCallAction
+ _OBJC_CLASS_$_IDSURI
+ _OBJC_IVAR_$_CXAnswerCallAction._receptionist
+ _OBJC_IVAR_$_CXCall._localMemberIdentity
+ _OBJC_IVAR_$_CXCallUpdate._commTrustScore
+ _OBJC_IVAR_$_CXCallUpdate._conversationGroupUUID
+ _OBJC_IVAR_$_CXCallUpdate._isSharePlayCapable
+ _OBJC_IVAR_$_CXCallUpdate._isUpgradeToVideo
+ _OBJC_IVAR_$_CXCallUpdate._launchInBackground
+ _OBJC_IVAR_$_CXCallUpdate._nearbyMode
+ _OBJC_IVAR_$_CXCallUpdate._remoteMember
+ _OBJC_IVAR_$_CXCallUpdate._specialUnknown
+ _OBJC_IVAR_$_CXCallUpdate._startCallMuted
+ _OBJC_IVAR_$_CXCallUpdate._supportsRecents
+ _OBJC_IVAR_$_CXCallUpdate._supportsScreenShare
+ _OBJC_IVAR_$_CXCallUpdate._supportsSharePlay
+ _OBJC_IVAR_$_CXJoinCallAction._isUpgradeToVideo
+ _OBJC_IVAR_$_CXJoinCallAction._launchInBackground
+ _OBJC_IVAR_$_CXJoinCallAction._participantCluster
+ _OBJC_IVAR_$_CXJoinCallAction._screenSharingRequestMetadata
+ _OBJC_IVAR_$_CXJoinCallParticipantCluster._UUID
+ _OBJC_IVAR_$_CXJoinCallParticipantCluster._type
+ _OBJC_IVAR_$_CXMember._handle
+ _OBJC_IVAR_$_CXMember._identityBlob
+ _OBJC_IVAR_$_CXMember._stableDeviceIdentifier
+ _OBJC_IVAR_$_CXProviderConfiguration._supportsAudioTranslation
+ _OBJC_IVAR_$_CXScreenSharingRequestMetadata._appName
+ _OBJC_IVAR_$_CXScreenSharingRequestMetadata._bundleIdentifier
+ _OBJC_IVAR_$_CXSetScreeningCallAction._receptionist
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._isSystemInitiated
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._isTranslating
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._localLocale
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._remoteLocale
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._translationEngine
+ _OBJC_IVAR_$_CXStartCallAction._isUpgradeToVideo
+ _OBJC_IVAR_$_CXStartCallAction._launchInBackground
+ _OBJC_IVAR_$_CXStartCallAction._startCallMuted
+ _OBJC_METACLASS_$_CXJoinCallParticipantCluster
+ _OBJC_METACLASS_$_CXMember
+ _OBJC_METACLASS_$_CXScreenSharingRequestMetadata
+ _OBJC_METACLASS_$_CXSetTranslatingCallAction
+ _OBJC_METACLASS_$_CXShareIdentityCallAction
+ __OBJC_$_CLASS_METHODS_CXJoinCallParticipantCluster
+ __OBJC_$_CLASS_METHODS_CXMember
+ __OBJC_$_CLASS_METHODS_CXScreenSharingRequestMetadata
+ __OBJC_$_CLASS_METHODS_CXSetTranslatingCallAction
+ __OBJC_$_CLASS_PROP_LIST_CXJoinCallParticipantCluster
+ __OBJC_$_CLASS_PROP_LIST_CXMember
+ __OBJC_$_CLASS_PROP_LIST_CXScreenSharingRequestMetadata
+ __OBJC_$_CLASS_PROP_LIST_CXSetTranslatingCallAction
+ __OBJC_$_INSTANCE_METHODS_CXJoinCallParticipantCluster
+ __OBJC_$_INSTANCE_METHODS_CXMember
+ __OBJC_$_INSTANCE_METHODS_CXScreenSharingRequestMetadata
+ __OBJC_$_INSTANCE_METHODS_CXSetTranslatingCallAction
+ __OBJC_$_INSTANCE_VARIABLES_CXJoinCallParticipantCluster
+ __OBJC_$_INSTANCE_VARIABLES_CXMember
+ __OBJC_$_INSTANCE_VARIABLES_CXScreenSharingRequestMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CXSetTranslatingCallAction
+ __OBJC_$_PROP_LIST_CXJoinCallParticipantCluster
+ __OBJC_$_PROP_LIST_CXMember
+ __OBJC_$_PROP_LIST_CXScreenSharingRequestMetadata
+ __OBJC_$_PROP_LIST_CXSetTranslatingCallAction
+ __OBJC_CLASS_PROTOCOLS_$_CXJoinCallParticipantCluster
+ __OBJC_CLASS_PROTOCOLS_$_CXMember
+ __OBJC_CLASS_PROTOCOLS_$_CXScreenSharingRequestMetadata
+ __OBJC_CLASS_PROTOCOLS_$_CXSetTranslatingCallAction
+ __OBJC_CLASS_RO_$_CXJoinCallParticipantCluster
+ __OBJC_CLASS_RO_$_CXMember
+ __OBJC_CLASS_RO_$_CXScreenSharingRequestMetadata
+ __OBJC_CLASS_RO_$_CXSetTranslatingCallAction
+ __OBJC_CLASS_RO_$_CXShareIdentityCallAction
+ __OBJC_METACLASS_RO_$_CXJoinCallParticipantCluster
+ __OBJC_METACLASS_RO_$_CXMember
+ __OBJC_METACLASS_RO_$_CXScreenSharingRequestMetadata
+ __OBJC_METACLASS_RO_$_CXSetTranslatingCallAction
+ __OBJC_METACLASS_RO_$_CXShareIdentityCallAction
+ ___23-[CXMember description]_block_invoke
+ ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.162
+ ___65-[CXCallDirectoryManager fetchLiveBlockingInfoForHandle:timeout:]_block_invoke.21
+ ___65-[CXCallDirectoryManager fetchLiveBlockingInfoForHandle:timeout:]_block_invoke.21.cold.1
+ ___79-[CXCallDirectoryManager setPrioritizedExtensionIdentifiers:completionHandler:]_block_invoke.25
+ ___92-[CXCallDirectoryManager firstEnabledLiveBlockingExtensionIdentifierForPhoneNumber:timeout:]_block_invoke.23
+ ___92-[CXCallDirectoryManager firstEnabledLiveBlockingExtensionIdentifierForPhoneNumber:timeout:]_block_invoke.23.cold.1
+ ___99-[CXCallDirectoryManager firstIdentificationEntryForEnabledExtensionSyncWithPhoneNumber:cacheOnly:]_block_invoke
+ ___99-[CXCallDirectoryManager firstIdentificationEntryForEnabledExtensionSyncWithPhoneNumber:cacheOnly:]_block_invoke.18
+ ___99-[CXCallDirectoryManager firstIdentificationEntryForEnabledExtensionSyncWithPhoneNumber:cacheOnly:]_block_invoke_2
+ ___99-[CXCallDirectoryManager firstIdentificationEntryForEnabledExtensionSyncWithPhoneNumber:cacheOnly:]_block_invoke_2.cold.1
+ ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ _isInternalInstall
+ _objc_msgSend$appName
+ _objc_msgSend$commTrustScore
+ _objc_msgSend$conversationGroupUUID
+ _objc_msgSend$fulfill
+ _objc_msgSend$identityBlob
+ _objc_msgSend$initWithHandle:
+ _objc_msgSend$initWithHandle:identityBlob:stableDeviceIdentifier:
+ _objc_msgSend$initWithUUID:type:
+ _objc_msgSend$isEqualToJoinCallParticipantCluster:
+ _objc_msgSend$isEqualToMember:
+ _objc_msgSend$isSharePlayCapable
+ _objc_msgSend$isTranslating
+ _objc_msgSend$isUpgradeToVideo
+ _objc_msgSend$launchInBackground
+ _objc_msgSend$localLocale
+ _objc_msgSend$localMemberIdentity
+ _objc_msgSend$nearbyMode
+ _objc_msgSend$participantCluster
+ _objc_msgSend$provider:performSetTranslatingCallAction:
+ _objc_msgSend$provider:performShareIdentityCallAction:
+ _objc_msgSend$receptionist
+ _objc_msgSend$remoteLocale
+ _objc_msgSend$remoteMember
+ _objc_msgSend$screenSharingRequestMetadata
+ _objc_msgSend$setAppName:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setCommTrustScore:
+ _objc_msgSend$setConversationGroupUUID:
+ _objc_msgSend$setIsSharePlayCapable:
+ _objc_msgSend$setIsUpgradeToVideo:
+ _objc_msgSend$setLaunchInBackground:
+ _objc_msgSend$setLocalMemberIdentity:
+ _objc_msgSend$setNearbyMode:
+ _objc_msgSend$setParticipantCluster:
+ _objc_msgSend$setRemoteMember:
+ _objc_msgSend$setScreenSharingRequestMetadata:
+ _objc_msgSend$setSpecialUnknown:
+ _objc_msgSend$setStartCallMuted:
+ _objc_msgSend$setSupportsAudioTranslation:
+ _objc_msgSend$setSupportsRecents:
+ _objc_msgSend$setSupportsScreenShare:
+ _objc_msgSend$setSupportsSharePlay:
+ _objc_msgSend$specialUnknown
+ _objc_msgSend$stableDeviceIdentifier
+ _objc_msgSend$startCallMuted
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$supportsAudioTranslation
+ _objc_msgSend$supportsRecents
+ _objc_msgSend$supportsScreenShare
+ _objc_msgSend$supportsSharePlay
+ _objc_msgSend$synchronousServerWithErrorHandler:
+ _objc_msgSend$translationEngine
+ _os_variant_has_internal_diagnostics
- GCC_except_table36
- GCC_except_table40
- _OBJC_IVAR_$_CXCallUpdate._remoteHandle
- ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.158
- ___65-[CXCallDirectoryManager fetchLiveBlockingInfoForHandle:timeout:]_block_invoke.20
- ___65-[CXCallDirectoryManager fetchLiveBlockingInfoForHandle:timeout:]_block_invoke.20.cold.1
- ___79-[CXCallDirectoryManager setPrioritizedExtensionIdentifiers:completionHandler:]_block_invoke.24
- ___92-[CXCallDirectoryManager firstEnabledLiveBlockingExtensionIdentifierForPhoneNumber:timeout:]_block_invoke.22
- ___92-[CXCallDirectoryManager firstEnabledLiveBlockingExtensionIdentifierForPhoneNumber:timeout:]_block_invoke.22.cold.1
- _objc_msgSend$setRemoteHandle:
CStrings:
+ " commTrustScore=%d"
+ " conversationGroupUUID=%@"
+ " isSharePlayCapable=%d"
+ " isSystemInitiated=%d"
+ " isTranslating=%d"
+ " isUpgradeToVideo=%d"
+ " launchInBackground=%d"
+ " localLocale=%@"
+ " nearbyMode=%ld"
+ " participantCluster=%@"
+ " receptionist=%d"
+ " remoteLocale=%@"
+ " remoteMember=%@"
+ " screenSharingRequestMetadata=%@"
+ " specialUnknown=%d"
+ " startCallMuted=%d"
+ " supportsAudioTranslation=%d"
+ " supportsRecents=%d"
+ " supportsScreenShare=%d"
+ " supportsSharePlay=%d"
+ " translationEngine=%lu"
+ " type=%zd"
+ "-[CXMember initWithHandle:identityBlob:stableDeviceIdentifier:]"
+ "<%@ %p handle=%@ identityBlob=%@>"
+ "@\"CXJoinCallParticipantCluster\""
+ "@\"CXMember\""
+ "@\"CXScreenSharingRequestMetadata\""
+ "@\"NSLocale\""
+ "@44@0:8@16B24@28@36"
+ "@48@0:8@16B24B28@32@40"
+ "CXJoinCallParticipantCluster"
+ "CXMember"
+ "CXScreenSharingRequestMetadata"
+ "CXSetTranslatingCallAction"
+ "CXShareIdentityCallAction"
+ "Error using remote object proxy: %@"
+ "T@\"CXHandle\",R,C,N,V_handle"
+ "T@\"CXJoinCallParticipantCluster\",C,N,V_participantCluster"
+ "T@\"CXMember\",C,N,V_remoteMember"
+ "T@\"CXScreenSharingRequestMetadata\",C,N,V_screenSharingRequestMetadata"
+ "T@\"NSData\",C,N,V_localMemberIdentity"
+ "T@\"NSData\",R,C,N,V_identityBlob"
+ "T@\"NSLocale\",R,N,V_localLocale"
+ "T@\"NSLocale\",R,N,V_remoteLocale"
+ "T@\"NSString\",&,N,V_appName"
+ "T@\"NSString\",&,N,V_stableDeviceIdentifier"
+ "T@\"NSUUID\",&,N,V_conversationGroupUUID"
+ "TB,N,GisUpgradeToVideo,V_isUpgradeToVideo"
+ "TB,N,V_isSharePlayCapable"
+ "TB,N,V_isUpgradeToVideo"
+ "TB,N,V_launchInBackground"
+ "TB,N,V_receptionist"
+ "TB,N,V_specialUnknown"
+ "TB,N,V_startCallMuted"
+ "TB,N,V_supportsAudioTranslation"
+ "TB,N,V_supportsRecents"
+ "TB,N,V_supportsScreenShare"
+ "TB,N,V_supportsSharePlay"
+ "TB,R,N,V_isSystemInitiated"
+ "TB,R,N,V_isTranslating"
+ "TQ,R,N,V_translationEngine"
+ "Ti,N,V_commTrustScore"
+ "Tq,N,V_nearbyMode"
+ "Tq,R,N,V_type"
+ "T{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},N,V_hasSet"
+ "_appName"
+ "_commTrustScore"
+ "_conversationGroupUUID"
+ "_identityBlob"
+ "_isSharePlayCapable"
+ "_isSystemInitiated"
+ "_isTranslating"
+ "_isUpgradeToVideo"
+ "_launchInBackground"
+ "_localLocale"
+ "_localMemberIdentity"
+ "_nearbyMode"
+ "_participantCluster"
+ "_receptionist"
+ "_remoteLocale"
+ "_remoteMember"
+ "_screenSharingRequestMetadata"
+ "_specialUnknown"
+ "_stableDeviceIdentifier"
+ "_startCallMuted"
+ "_supportsAudioTranslation"
+ "_supportsRecents"
+ "_supportsScreenShare"
+ "_supportsSharePlay"
+ "_translationEngine"
+ "appName"
+ "com.apple.TelephonyUtilities"
+ "commTrustScore"
+ "conversationGroupUUID"
+ "firstIdentificationEntryForEnabledExtensionSyncWithPhoneNumber:cacheOnly:"
+ "fulfill CXSetTranslatingCallAction"
+ "fulfillWithTranslationEngine:"
+ "identityBlob"
+ "initWithCallUUID:isTranslating:isSystemInitiated:localLocale:remoteLocale:"
+ "initWithCallUUID:isTranslating:localLocale:remoteLocale:"
+ "initWithHandle:"
+ "initWithHandle:identityBlob:"
+ "initWithHandle:identityBlob:stableDeviceIdentifier:"
+ "initWithUUID:type:"
+ "internal build: _supportsAudioTranslation: %d"
+ "isEqualToJoinCallParticipantCluster:"
+ "isEqualToMember:"
+ "isSharePlayCapable"
+ "isTranslating"
+ "isUpgradeToVideo"
+ "launchInBackground"
+ "localLocale"
+ "localMemberIdentity"
+ "nearbyMode"
+ "participantCluster"
+ "provider:performSetTranslatingCallAction:"
+ "provider:performShareIdentityCallAction:"
+ "receptionist"
+ "remoteLocale"
+ "remoteMember"
+ "screenSharingRequestMetadata"
+ "setAppName:"
+ "setCommTrustScore:"
+ "setConversationGroupUUID:"
+ "setIsSharePlayCapable:"
+ "setIsUpgradeToVideo:"
+ "setLaunchInBackground:"
+ "setLocalMemberIdentity:"
+ "setNearbyMode:"
+ "setParticipantCluster:"
+ "setReceptionist:"
+ "setRemoteMember:"
+ "setScreenSharingRequestMetadata:"
+ "setSpecialUnknown:"
+ "setStableDeviceIdentifier:"
+ "setStartCallMuted:"
+ "setSupportsAudioTranslation:"
+ "setSupportsRecents:"
+ "setSupportsScreenShare:"
+ "setSupportsSharePlay:"
+ "specialUnknown"
+ "stableDeviceIdentifier"
+ "startCallMuted"
+ "startCallMuted:"
+ "stringWithString:"
+ "supportsAudioTranslation"
+ "supportsRecents"
+ "supportsScreenShare"
+ "supportsSharePlay"
+ "synchronousServerWithErrorHandler:"
+ "translationEngine"
+ "v28@0:8{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
+ "v32@0:8@\"CXProvider\"16@\"CXSetTranslatingCallAction\"24"
+ "v32@0:8@\"CXProvider\"16@\"CXShareIdentityCallAction\"24"
+ "{CXCallUpdateHasSet=\"account\"b1\"activeRemoteParticipant\"b1\"remoteMember\"b1\"localizedCallerName\"b1\"localizedCallerImageURL\"b1\"emergency\"b1\"failureExpected\"b1\"supportsEmergencyFallback\"b1\"usingBaseband\"b1\"blocked\"b1\"ttyType\"b1\"supportsTTYWithVoice\"b1\"mayRequireBreakBeforeMake\"b1\"hasVideo\"b1\"isUpgradeToVideo\"b1\"audioCategory\"b1\"audioMode\"b1\"audioInterruptionProvider\"b1\"audioInterruptionOperationMode\"b1\"verificationStatus\"b1\"priority\"b1\"requiresInCallSounds\"b1\"inCallSoundRegion\"b1\"supportsHolding\"b1\"supportsGrouping\"b1\"supportsUngrouping\"b1\"supportsDTMF\"b1\"supportsDTMFUpdates\"b1\"supportsSharePlay\"b1\"supportsScreenShare\"b1\"supportsUnambiguousMultiPartyState\"b1\"supportsAddCall\"b1\"supportsSendingToVoicemail\"b1\"supportsRecording\"b1\"isUnderlyingLinksConnected\"b1\"videoStreamToken\"b1\"callTokens\"b1\"announceProviderIdentifier\"b1\"initiator\"b1\"crossDeviceIdentifier\"b1\"ISOCountryCode\"b1\"localSenderIdentityUUID\"b1\"localSenderIdentityAccountUUID\"b1\"localMemberHandleValue\"b1\"localSenderSubscriptionIdentifier\"b1\"participantGroupUUID\"b1\"remoteParticipantHandles\"b1\"otherInvitedHandles\"b1\"activeRemoteParticipantHandles\"b1\"handoffContext\"b1\"screenShareAttributes\"b1\"context\"b1\"prefersExclusiveAccessToCellularNetwork\"b1\"remoteUplinkMuted\"b1\"shouldSuppressInCallUI\"b1\"launchInBackground\"b1\"requiresAuthentication\"b1\"mutuallyExclusiveCall\"b1\"junkConfidence\"b1\"identificationCategory\"b1\"conversation\"b1\"mixesVoiceWithMedia\"b1\"prefersToPlayDuringWombat\"b1\"mediaPlaybackOnExternalDevice\"b1\"oneToOneModeEnabled\"b1\"sharingScreen\"b1\"bluetoothAudioFormat\"b1\"ignoresBluetoothDeviceUID\"b1\"serviceStatus\"b1\"transmissionMode\"b1\"accessoryButtonEventsEnabled\"b1\"sendingVideo\"b1\"hasBeenRedirected\"b1\"isKnownCaller\"b1\"filteredOutReason\"b1\"silencingUserInfo\"b1\"isReRing\"b1\"suppressRingtone\"b1\"callSubType\"b1\"supportsScreening\"b1\"supportsRecents\"b1\"screenSharingIntention\"b1\"screenSharingType\"b1\"isSharePlayCapable\"b1\"nearbyMode\"b1\"commTrustScore\"b1\"specialUnknown\"b1\"conversationGroupUUID\"b1\"startCallMuted\"b1}"
+ "{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "$-"
- "T{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},N,V_hasSet"
- "v28@0:8{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
- "{CXCallUpdateHasSet=\"account\"b1\"activeRemoteParticipant\"b1\"remoteHandle\"b1\"localizedCallerName\"b1\"localizedCallerImageURL\"b1\"emergency\"b1\"failureExpected\"b1\"supportsEmergencyFallback\"b1\"usingBaseband\"b1\"blocked\"b1\"ttyType\"b1\"supportsTTYWithVoice\"b1\"mayRequireBreakBeforeMake\"b1\"hasVideo\"b1\"audioCategory\"b1\"audioMode\"b1\"audioInterruptionProvider\"b1\"audioInterruptionOperationMode\"b1\"verificationStatus\"b1\"priority\"b1\"requiresInCallSounds\"b1\"inCallSoundRegion\"b1\"supportsHolding\"b1\"supportsGrouping\"b1\"supportsUngrouping\"b1\"supportsDTMF\"b1\"supportsDTMFUpdates\"b1\"supportsUnambiguousMultiPartyState\"b1\"supportsAddCall\"b1\"supportsSendingToVoicemail\"b1\"supportsRecording\"b1\"isUnderlyingLinksConnected\"b1\"videoStreamToken\"b1\"callTokens\"b1\"announceProviderIdentifier\"b1\"initiator\"b1\"crossDeviceIdentifier\"b1\"ISOCountryCode\"b1\"localSenderIdentityUUID\"b1\"localSenderIdentityAccountUUID\"b1\"localMemberHandleValue\"b1\"localSenderSubscriptionIdentifier\"b1\"participantGroupUUID\"b1\"remoteParticipantHandles\"b1\"otherInvitedHandles\"b1\"activeRemoteParticipantHandles\"b1\"handoffContext\"b1\"screenShareAttributes\"b1\"context\"b1\"prefersExclusiveAccessToCellularNetwork\"b1\"remoteUplinkMuted\"b1\"shouldSuppressInCallUI\"b1\"requiresAuthentication\"b1\"mutuallyExclusiveCall\"b1\"junkConfidence\"b1\"identificationCategory\"b1\"conversation\"b1\"mixesVoiceWithMedia\"b1\"prefersToPlayDuringWombat\"b1\"mediaPlaybackOnExternalDevice\"b1\"oneToOneModeEnabled\"b1\"sharingScreen\"b1\"bluetoothAudioFormat\"b1\"ignoresBluetoothDeviceUID\"b1\"serviceStatus\"b1\"transmissionMode\"b1\"accessoryButtonEventsEnabled\"b1\"sendingVideo\"b1\"hasBeenRedirected\"b1\"isKnownCaller\"b1\"filteredOutReason\"b1\"silencingUserInfo\"b1\"isReRing\"b1\"suppressRingtone\"b1\"callSubType\"b1\"supportsScreening\"b1\"screenSharingIntention\"b1\"screenSharingType\"b1}"
- "{CXCallUpdateHasSet=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"

```
