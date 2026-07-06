## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

-  __TEXT.__text: 0x2ab28
-  __TEXT.__objc_methlist: 0x3534
+  __TEXT.__text: 0x2c478
+  __TEXT.__objc_methlist: 0x383c
   __TEXT.__const: 0x308
-  __TEXT.__gcc_except_tab: 0xae4
-  __TEXT.__cstring: 0x1bcf
+  __TEXT.__gcc_except_tab: 0xb00
+  __TEXT.__cstring: 0x1d1f
   __TEXT.__oslogstring: 0x329
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x206

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0xb50
+  __TEXT.__unwind_info: 0xbc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xef8
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25b8
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x2788
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__got: 0x578
   __AUTH_CONST.__const: 0x438
-  __AUTH_CONST.__cfstring: 0x2b20
-  __AUTH_CONST.__objc_const: 0x5148
+  __AUTH_CONST.__cfstring: 0x2e20
+  __AUTH_CONST.__objc_const: 0x5658
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0x550
-  __AUTH.__objc_data: 0xe08
+  __AUTH.__objc_data: 0xef8
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x3f8
+  __DATA.__objc_ivar: 0x43c
   __DATA.__data: 0x960
   __DATA.__bss: 0x1f8
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1202
-  Symbols:   4357
-  CStrings:  785
+  Functions: 1262
+  Symbols:   4576
+  CStrings:  833
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[HLPAnalyticsEventLinkUsed eventWithDestinationURL:linkType:topicID:]
+ +[HLPAnalyticsEventSession eventWithBooksViewed:numSearches:sessionDuration:timeActive:topicsViewed:]
+ -[HLPAnalyticsEventController activeSession]
+ -[HLPAnalyticsEventController setActiveSession:]
+ -[HLPAnalyticsEventLinkUsed .cxx_destruct]
+ -[HLPAnalyticsEventLinkUsed _initWithDestinationURL:linkType:topicID:]
+ -[HLPAnalyticsEventLinkUsed caRepresentation]
+ -[HLPAnalyticsEventLinkUsed destinationURL]
+ -[HLPAnalyticsEventLinkUsed eventName]
+ -[HLPAnalyticsEventLinkUsed linkType]
+ -[HLPAnalyticsEventLinkUsed setDestinationURL:]
+ -[HLPAnalyticsEventLinkUsed setLinkType:]
+ -[HLPAnalyticsEventLinkUsed setTopicID:]
+ -[HLPAnalyticsEventLinkUsed topicID]
+ -[HLPAnalyticsEventSearchUsed log]
+ -[HLPAnalyticsEventSession _initWithBooksViewed:numSearches:sessionDuration:timeActive:topicsViewed:]
+ -[HLPAnalyticsEventSession booksViewed]
+ -[HLPAnalyticsEventSession caRepresentation]
+ -[HLPAnalyticsEventSession eventName]
+ -[HLPAnalyticsEventSession numSearches]
+ -[HLPAnalyticsEventSession sessionDuration]
+ -[HLPAnalyticsEventSession setBooksViewed:]
+ -[HLPAnalyticsEventSession setNumSearches:]
+ -[HLPAnalyticsEventSession setSessionDuration:]
+ -[HLPAnalyticsEventSession setTimeActive:]
+ -[HLPAnalyticsEventSession setTopicsViewed:]
+ -[HLPAnalyticsEventSession timeActive]
+ -[HLPAnalyticsEventSession topicsViewed]
+ -[HLPAnalyticsSession .cxx_destruct]
+ -[HLPAnalyticsSession accumulatedActiveTime]
+ -[HLPAnalyticsSession booksViewed]
+ -[HLPAnalyticsSession clearPersistedSnapshot]
+ -[HLPAnalyticsSession didBecomeActive]
+ -[HLPAnalyticsSession didResignActive]
+ -[HLPAnalyticsSession end]
+ -[HLPAnalyticsSession init]
+ -[HLPAnalyticsSession lastActiveDate]
+ -[HLPAnalyticsSession numSearches]
+ -[HLPAnalyticsSession persistSnapshot]
+ -[HLPAnalyticsSession persistenceKey]
+ -[HLPAnalyticsSession restoreSnapshotIfNeeded]
+ -[HLPAnalyticsSession sessionID]
+ -[HLPAnalyticsSession sessionStartDate]
+ -[HLPAnalyticsSession setAccumulatedActiveTime:]
+ -[HLPAnalyticsSession setBooksViewed:]
+ -[HLPAnalyticsSession setLastActiveDate:]
+ -[HLPAnalyticsSession setNumSearches:]
+ -[HLPAnalyticsSession setSessionID:]
+ -[HLPAnalyticsSession setSessionStartDate:]
+ -[HLPAnalyticsSession setViewedTopicIDs:]
+ -[HLPAnalyticsSession start]
+ -[HLPAnalyticsSession trackBookViewed]
+ -[HLPAnalyticsSession trackSearchUsed]
+ -[HLPAnalyticsSession trackTopicViewed:]
+ -[HLPAnalyticsSession viewedTopicIDs]
+ -[HLPHelpTopicViewController linkTypeForURL:]
+ -[HLPHelpViewController _sceneDidActivate:]
+ -[HLPHelpViewController _sceneWillDeactivate:]
+ -[HLPHelpViewController analyticsSession]
+ -[HLPHelpViewController setAnalyticsSession:]
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table70
+ _HLPAnalyticsLinkTypeAside
+ _HLPAnalyticsLinkTypeOpenIt
+ _HLPAnalyticsLinkTypeTask
+ _HLPAnalyticsLinkTypeTopic
+ _OBJC_CLASS_$_HLPAnalyticsEventLinkUsed
+ _OBJC_CLASS_$_HLPAnalyticsEventSession
+ _OBJC_CLASS_$_HLPAnalyticsSession
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_HLPAnalyticsEventController._activeSession
+ _OBJC_IVAR_$_HLPAnalyticsEventLinkUsed._destinationURL
+ _OBJC_IVAR_$_HLPAnalyticsEventLinkUsed._linkType
+ _OBJC_IVAR_$_HLPAnalyticsEventLinkUsed._topicID
+ _OBJC_IVAR_$_HLPAnalyticsEventSession._booksViewed
+ _OBJC_IVAR_$_HLPAnalyticsEventSession._numSearches
+ _OBJC_IVAR_$_HLPAnalyticsEventSession._sessionDuration
+ _OBJC_IVAR_$_HLPAnalyticsEventSession._timeActive
+ _OBJC_IVAR_$_HLPAnalyticsEventSession._topicsViewed
+ _OBJC_IVAR_$_HLPAnalyticsSession._accumulatedActiveTime
+ _OBJC_IVAR_$_HLPAnalyticsSession._booksViewed
+ _OBJC_IVAR_$_HLPAnalyticsSession._lastActiveDate
+ _OBJC_IVAR_$_HLPAnalyticsSession._numSearches
+ _OBJC_IVAR_$_HLPAnalyticsSession._sessionID
+ _OBJC_IVAR_$_HLPAnalyticsSession._sessionStartDate
+ _OBJC_IVAR_$_HLPAnalyticsSession._viewedTopicIDs
+ _OBJC_IVAR_$_HLPHelpViewController._analyticsSession
+ _OBJC_METACLASS_$_HLPAnalyticsEventLinkUsed
+ _OBJC_METACLASS_$_HLPAnalyticsEventSession
+ _OBJC_METACLASS_$_HLPAnalyticsSession
+ _UISceneDidActivateNotification
+ _UISceneWillDeactivateNotification
+ __OBJC_$_CLASS_METHODS_HLPAnalyticsEventLinkUsed
+ __OBJC_$_CLASS_METHODS_HLPAnalyticsEventSession
+ __OBJC_$_INSTANCE_METHODS_HLPAnalyticsEventLinkUsed
+ __OBJC_$_INSTANCE_METHODS_HLPAnalyticsEventSession
+ __OBJC_$_INSTANCE_METHODS_HLPAnalyticsSession
+ __OBJC_$_INSTANCE_VARIABLES_HLPAnalyticsEventLinkUsed
+ __OBJC_$_INSTANCE_VARIABLES_HLPAnalyticsEventSession
+ __OBJC_$_INSTANCE_VARIABLES_HLPAnalyticsSession
+ __OBJC_$_PROP_LIST_HLPAnalyticsEventLinkUsed
+ __OBJC_$_PROP_LIST_HLPAnalyticsEventSession
+ __OBJC_$_PROP_LIST_HLPAnalyticsSession
+ __OBJC_CLASS_RO_$_HLPAnalyticsEventLinkUsed
+ __OBJC_CLASS_RO_$_HLPAnalyticsEventSession
+ __OBJC_CLASS_RO_$_HLPAnalyticsSession
+ __OBJC_METACLASS_RO_$_HLPAnalyticsEventLinkUsed
+ __OBJC_METACLASS_RO_$_HLPAnalyticsEventSession
+ __OBJC_METACLASS_RO_$_HLPAnalyticsSession
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_initWithBooksViewed:numSearches:sessionDuration:timeActive:topicsViewed:
+ _objc_msgSend$_initWithDestinationURL:linkType:topicID:
+ _objc_msgSend$accumulatedActiveTime
+ _objc_msgSend$activeSession
+ _objc_msgSend$allObjects
+ _objc_msgSend$analyticsSession
+ _objc_msgSend$booksViewed
+ _objc_msgSend$clearPersistedSnapshot
+ _objc_msgSend$destinationURL
+ _objc_msgSend$didBecomeActive
+ _objc_msgSend$didResignActive
+ _objc_msgSend$doubleValue
+ _objc_msgSend$end
+ _objc_msgSend$eventWithBooksViewed:numSearches:sessionDuration:timeActive:topicsViewed:
+ _objc_msgSend$eventWithDestinationURL:linkType:topicID:
+ _objc_msgSend$lastActiveDate
+ _objc_msgSend$linkType
+ _objc_msgSend$linkTypeForURL:
+ _objc_msgSend$numSearches
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$object
+ _objc_msgSend$pathComponents
+ _objc_msgSend$persistSnapshot
+ _objc_msgSend$persistenceKey
+ _objc_msgSend$restoreSnapshotIfNeeded
+ _objc_msgSend$sessionDuration
+ _objc_msgSend$sessionID
+ _objc_msgSend$sessionStartDate
+ _objc_msgSend$set
+ _objc_msgSend$setAccumulatedActiveTime:
+ _objc_msgSend$setActiveSession:
+ _objc_msgSend$setAnalyticsSession:
+ _objc_msgSend$setBooksViewed:
+ _objc_msgSend$setLastActiveDate:
+ _objc_msgSend$setNumSearches:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$setSessionStartDate:
+ _objc_msgSend$setViewedTopicIDs:
+ _objc_msgSend$timeActive
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$topicsViewed
+ _objc_msgSend$trackBookViewed
+ _objc_msgSend$trackSearchUsed
+ _objc_msgSend$trackTopicViewed:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$viewedTopicIDs
+ _objc_msgSend$window
+ _objc_msgSend$windowScene
- GCC_except_table53
- GCC_except_table58
- GCC_except_table68
CStrings:
+ "HLPAnalyticsSession-"
+ "accumulatedActiveTime"
+ "booksViewed"
+ "books_viewed"
+ "destination_url"
+ "guide"
+ "help"
+ "link_type"
+ "link_used"
+ "numSearches"
+ "num_searches"
+ "open_it"
+ "persistedAt"
+ "session"
+ "sessionStartDate"
+ "session_duration"
+ "support.apple.com"
+ "time_active"
+ "topic_id"
+ "topics_viewed"
+ "viewedTopicIDs"
+ "x-apple-tips"
+ "x-apple.systempreferences"
+ "x-help-action"

```
