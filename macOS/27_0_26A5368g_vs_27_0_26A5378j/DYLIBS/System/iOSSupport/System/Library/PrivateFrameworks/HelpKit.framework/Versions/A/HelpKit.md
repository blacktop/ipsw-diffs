## HelpKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/HelpKit.framework/Versions/A/HelpKit`

```diff

-  __TEXT.__text: 0x2a66c
-  __TEXT.__objc_methlist: 0x351c
+  __TEXT.__text: 0x2bfbc
+  __TEXT.__objc_methlist: 0x3824
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
-  __DATA_CONST.__const: 0xf00
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__const: 0xf20
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25a8
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x2778
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__got: 0x578
   __AUTH_CONST.__const: 0x438
-  __AUTH_CONST.__cfstring: 0x2b00
-  __AUTH_CONST.__objc_const: 0x5118
+  __AUTH_CONST.__cfstring: 0x2e00
+  __AUTH_CONST.__objc_const: 0x5628
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0x550
-  __AUTH.__objc_data: 0xe08
+  __AUTH.__objc_data: 0xef8
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x3f4
+  __DATA.__objc_ivar: 0x438
   __DATA.__data: 0x960
   __DATA.__bss: 0x1f8
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1199
-  Symbols:   3258
-  CStrings:  784
+  Functions: 1259
+  Symbols:   3417
+  CStrings:  832
 
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
+ OBJC_IVAR_$_HLPAnalyticsEventController._activeSession
+ OBJC_IVAR_$_HLPAnalyticsEventLinkUsed._destinationURL
+ OBJC_IVAR_$_HLPAnalyticsEventLinkUsed._linkType
+ OBJC_IVAR_$_HLPAnalyticsEventLinkUsed._topicID
+ OBJC_IVAR_$_HLPAnalyticsEventSession._booksViewed
+ OBJC_IVAR_$_HLPAnalyticsEventSession._numSearches
+ OBJC_IVAR_$_HLPAnalyticsEventSession._sessionDuration
+ OBJC_IVAR_$_HLPAnalyticsEventSession._timeActive
+ OBJC_IVAR_$_HLPAnalyticsEventSession._topicsViewed
+ OBJC_IVAR_$_HLPAnalyticsSession._accumulatedActiveTime
+ OBJC_IVAR_$_HLPAnalyticsSession._booksViewed
+ OBJC_IVAR_$_HLPAnalyticsSession._lastActiveDate
+ OBJC_IVAR_$_HLPAnalyticsSession._numSearches
+ OBJC_IVAR_$_HLPAnalyticsSession._sessionID
+ OBJC_IVAR_$_HLPAnalyticsSession._sessionStartDate
+ OBJC_IVAR_$_HLPAnalyticsSession._viewedTopicIDs
+ OBJC_IVAR_$_HLPHelpViewController._analyticsSession
+ _HLPAnalyticsLinkTypeAside
+ _HLPAnalyticsLinkTypeOpenIt
+ _HLPAnalyticsLinkTypeTask
+ _HLPAnalyticsLinkTypeTopic
+ _OBJC_CLASS_$_HLPAnalyticsEventLinkUsed
+ _OBJC_CLASS_$_HLPAnalyticsEventSession
+ _OBJC_CLASS_$_HLPAnalyticsSession
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUUID
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
