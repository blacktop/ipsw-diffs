## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1440.100.7.2.5
-  __TEXT.__text: 0x275a80
-  __TEXT.__auth_stubs: 0x35a0
+1443.100.10.1.5
+  __TEXT.__text: 0x278240
+  __TEXT.__auth_stubs: 0x3600
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0x16964
-  __TEXT.__const: 0x93c0
-  __TEXT.__gcc_except_tab: 0x167b0
-  __TEXT.__cstring: 0x131d6
-  __TEXT.__oslogstring: 0x200d5
+  __TEXT.__objc_methlist: 0x16b3c
+  __TEXT.__const: 0x93d0
+  __TEXT.__gcc_except_tab: 0x16928
+  __TEXT.__cstring: 0x13276
+  __TEXT.__oslogstring: 0x202a5
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__constg_swiftt: 0x201c
-  __TEXT.__swift5_typeref: 0x2205
+  __TEXT.__swift5_typeref: 0x220d
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0x23b6
   __TEXT.__swift5_fieldmd: 0x2b04
   __TEXT.__swift5_assocty: 0x530
   __TEXT.__swift5_proto: 0x910
   __TEXT.__swift5_types: 0x258
-  __TEXT.__swift5_capture: 0x734
+  __TEXT.__swift5_capture: 0x744
   __TEXT.__swift_as_entry: 0xe0
   __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xa4a0
-  __TEXT.__eh_frame: 0x4c68
-  __TEXT.__objc_classname: 0x2709
-  __TEXT.__objc_methname: 0x400c1
-  __TEXT.__objc_methtype: 0x680c
-  __TEXT.__objc_stubs: 0x25d00
-  __DATA_CONST.__got: 0x2378
-  __DATA_CONST.__const: 0x5360
+  __TEXT.__unwind_info: 0xa710
+  __TEXT.__eh_frame: 0x4c90
+  __TEXT.__objc_classname: 0x2723
+  __TEXT.__objc_methname: 0x407ba
+  __TEXT.__objc_methtype: 0x68d0
+  __TEXT.__objc_stubs: 0x260c0
+  __DATA_CONST.__got: 0x23b0
+  __DATA_CONST.__const: 0x53d8
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x468
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdab8
+  __DATA_CONST.__objc_selrefs: 0xdbf0
   __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x1af0
-  __AUTH_CONST.__const: 0x7e40
-  __AUTH_CONST.__cfstring: 0xb620
-  __AUTH_CONST.__objc_const: 0x1e4a8
+  __AUTH_CONST.__auth_got: 0x1b20
+  __AUTH_CONST.__const: 0x7e88
+  __AUTH_CONST.__cfstring: 0xb6c0
+  __AUTH_CONST.__objc_const: 0x1e630
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x37b0
   __AUTH.__data: 0x22a8
-  __DATA.__objc_ivar: 0x1190
-  __DATA.__data: 0x4448
-  __DATA.__bss: 0x11d00
+  __DATA.__objc_ivar: 0x11a8
+  __DATA.__data: 0x4458
+  __DATA.__bss: 0x11d10
   __DATA.__common: 0x490
   __DATA_DIRTY.__objc_data: 0x1dd0
   __DATA_DIRTY.__data: 0x270

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 55550D63-ACD4-3BCB-A0F9-7130B7F5A574
-  Functions: 12444
-  Symbols:   2449
-  CStrings:  16657
+  UUID: 922B6850-CBC5-3EBA-B81A-29F5240D3721
+  Functions: 12495
+  Symbols:   2457
+  CStrings:  16734
 
Symbols:
+ _IMChatPropertyAcceptedContactBannerConsumed
+ _IMChatPropertyHasOfferedAutomaticTranslationInTranslateMenuKey
+ _IMChatPropertyLatestIncomingTranslatedMessageLanguageCodeForChatKey
+ _IMSPISimulateMessagesWithConfiguration
+ _IMSetupInfoUnreadReportsCurrentStampKey
+ _IMSetupInfoUnreadReportsLastStampKey
+ _IMUnreadCountControllerDidUpdateNotificationDeltaKey
+ _OBJC_CLASS_$_IMSimulatedMessageConfiguration
+ _OBJC_CLASS_$_IMUnreadCountReportDelta
- _IMUnreadCountControllerDidUpdateNotificationChangedGUIDsKey
CStrings:
+ "$(%@) sent a poll"
+ "$(%@) sent a vote"
+ "@32@0:8^B16B24B28"
+ "Disconencted from daemon, giving up fetching unread count replacement"
+ "Failed to fetch full replacement from daemon"
+ "IMChatRegistry_Translation"
+ "Message is already unread"
+ "Not sending another request to rebuild unread count controller when one is in flight"
+ "Not sending request to rebuild unread count because we are disconnected"
+ "POLL_VOTE_MESSAGE"
+ "Poll vote"
+ "ProcessPartialUnreadCountDeltas"
+ "Retry attempt failed, giving up fetching unread count replacement"
+ "Retrying fetch for unread count replacement"
+ "Skipping invocation, selector not implemented: %@"
+ "T@\"IMHandle\",R,N,V_senderHandle"
+ "T@\"IMSyncedSettingsManager\",R,N"
+ "T@\"NSSet\",&,N,V_mergedThreadFilterModes"
+ "T@\"NSString\",&,N,V_cachedNameThatIsNotHandle"
+ "T@\"NSString\",R,N,V_incomingLanguageCode"
+ "TB,N,GisMarkingUnread,V_markingUnread"
+ "TB,N,V_currentlyMarkingAsKnown"
+ "Tq,N,V_unreadCountReplacementState"
+ "_cachedNameThatIsNotHandle"
+ "_chat:downloadTranslationAssetsForLanguageCodes:messageItemsToTranslateLocally:"
+ "_chat:partiallyUpdated:"
+ "_currentlyMarkingAsKnown"
+ "_enumerateUnderlyingChatInfo:"
+ "_incomingLanguageCode"
+ "_initWithTranslationLanguageCode:incomingLanguageCode:senderHandle:isShowingTranslationText:"
+ "_markingUnread"
+ "_processUnreadCountFullReplacement:"
+ "_rebuildUnreadCountController"
+ "_unreadCountReplacementState"
+ "cachedNameThatIsNotHandle"
+ "canSuggestRecipientContact"
+ "clientBatchSize"
+ "currentlyMarkingAsKnown"
+ "deletedGUIDs"
+ "downloadTranslationAssetsForLanguageCodes:messageItemsToTranslateLocally:"
+ "downloadTranslationAssetsForLanguageCodes:messageItemsToTranslateLocally:chatIdentifier:style:account:"
+ "ensureUserTranslationLanguageIsResolvedForCode:"
+ "handleIDsForCNID:"
+ "hasOfferedAutomaticTranslationInTranslateMenu"
+ "immediateNameWithNeedsSuggestedNameFetch:useSuggestedName:allowHandles:"
+ "incomingLanguageCode"
+ "incomingTranslationLanguageCode"
+ "initWithDeletedGUIDs:updatedReports:isReplacement:fromStamp:toStamp:"
+ "initWithFirstName:lastName:avatar:pronouns:"
+ "invalidateMergedThreadFilterModes"
+ "isCoreRecentsAccepted"
+ "isMarkingUnread"
+ "isReplacement"
+ "markingUnread"
+ "nameThatIsNotHandle"
+ "nicknameObject"
+ "processDelta:"
+ "recalculateMergedThreadFilterModes"
+ "setAutomaticallyTranslate:languageCode:userLanguageCode:"
+ "setCachedNameThatIsNotHandle:"
+ "setCurrentlyMarkingAsKnown:"
+ "setHasOfferedAutomaticTranslationInTranslateMenu:"
+ "setMarkingUnread:"
+ "setUnreadCountReplacementState:"
+ "setValuesForKeysWithDictionary:"
+ "shouldShowIncomingTranslationIndicator"
+ "simulateMessages:configuration:completion:"
+ "translationLanguage"
+ "unreadCountChanged:"
+ "unreadCountFullReplacementWithCompletion:"
+ "unreadCountReplacementState"
+ "unreadCountReportsUpdated:"
+ "updatedReports"
+ "usersPreferredLanguageIdentifier"
+ "v16@?0@\"IMUnreadCountReportDelta\"8"
+ "v24@0:8@\"IMUnreadCountReportDelta\"16"
+ "v24@0:8@?<v@?@\"IMUnreadCountReportDelta\">16"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "v40@0:8@\"NSArray\"16@\"IMSimulatedMessageConfiguration\"24@?<v@?@\"NSError\">32"
+ "v52@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32C40@\"NSString\"44"
- "T@\"NSMutableSet\",&,N,V_mergedThreadFilterModes"
- "_initWithTranslationLanguageCode:isShowingTranslationText:"
- "addMergedThreadFilterMode:"
- "replaceReports:"
- "setAutomaticallyTranslate:languageCode:"
- "setUserTranslationLanguageCode:"
- "simulateMessages:completion:"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"

```
