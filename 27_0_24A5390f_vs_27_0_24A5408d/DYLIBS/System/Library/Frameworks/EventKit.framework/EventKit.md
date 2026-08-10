## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1973.0.0.0.0
-  __TEXT.__text: 0x1a1644
-  __TEXT.__objc_methlist: 0x15a74
-  __TEXT.__cstring: 0xbddf
-  __TEXT.__const: 0x4810
-  __TEXT.__oslogstring: 0xef78
-  __TEXT.__gcc_except_tab: 0x3928
+1976.0.0.0.0
+  __TEXT.__text: 0x1a3040
+  __TEXT.__objc_methlist: 0x15ac4
+  __TEXT.__cstring: 0xbe6f
+  __TEXT.__const: 0x4820
+  __TEXT.__oslogstring: 0xefd8
+  __TEXT.__gcc_except_tab: 0x3978
   __TEXT.__dlopen_cstrs: 0x400
   __TEXT.__ustring: 0x1a0
-  __TEXT.__swift5_typeref: 0x1942
+  __TEXT.__swift5_typeref: 0x1988
   __TEXT.__swift5_reflstr: 0x1261
   __TEXT.__swift5_assocty: 0x210
   __TEXT.__constg_swiftt: 0x1300

   __TEXT.__swift5_proto: 0x22c
   __TEXT.__swift5_types: 0x174
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_capture: 0x264
+  __TEXT.__swift5_capture: 0x278
   __TEXT.__swift_as_entry: 0xd4
-  __TEXT.__swift_as_ret: 0xe8
-  __TEXT.__swift_as_cont: 0x1a4
+  __TEXT.__swift_as_ret: 0xec
+  __TEXT.__swift_as_cont: 0x1a8
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x6730
-  __TEXT.__eh_frame: 0x25a8
+  __TEXT.__unwind_info: 0x6780
+  __TEXT.__eh_frame: 0x2618
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x47f8
+  __DATA_CONST.__const: 0x48e0
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae60
+  __DATA_CONST.__objc_selrefs: 0xae98
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x5d8
-  __DATA_CONST.__got: 0x1a08
-  __AUTH_CONST.__const: 0x4470
+  __DATA_CONST.__got: 0x1a50
+  __AUTH_CONST.__const: 0x4500
   __AUTH_CONST.__cfstring: 0x9ec0
-  __AUTH_CONST.__objc_const: 0x18548
+  __AUTH_CONST.__objc_const: 0x18628
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x1400
+  __AUTH_CONST.__auth_got: 0x1430
   __AUTH.__objc_data: 0x34d0
   __AUTH.__data: 0xf08
-  __DATA.__objc_ivar: 0xd64
-  __DATA.__data: 0x2830
+  __DATA.__objc_ivar: 0xd7c
+  __DATA.__data: 0x2890
   __DATA.__bss: 0x4770
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1bd0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10666
-  Symbols:   17543
-  CStrings:  2666
+  Functions: 10688
+  Symbols:   17574
+  CStrings:  2669
 
Symbols:
+ -[EKAutocompleter _filterBlockedResults:completion:]
+ -[EKLocationSearchModel _handleAvailabilityResults:addressToRoomMap:availabilityCache:notifyType:forOperation:]
+ -[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]
+ -[EKLocationSearchModel _requestAvailabilityForRecentsConferenceRooms:]
+ -[EKLocationSearchModel _updateAvailabilityForRecentsConferenceRooms]
+ -[EKObject(Shared) _setCachedMeltedObject:forKey:]
+ -[EKObject(Shared) _setCachedValue:forKey:]
+ -[EKObject(Shared) emptyValueCache]
+ -[EKRecentContactSearchResult resolvedConferenceRoom]
+ -[EKRecentContactSearchResult setResolvedConferenceRoom:]
+ -[EKVirtualConference textRepresentation]
+ GCC_except_table115
+ GCC_except_table131
+ GCC_except_table149
+ GCC_except_table169
+ GCC_except_table203
+ GCC_except_table210
+ GCC_except_table43
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table93
+ _OBJC_CLASS_$_CalBlockListFilter
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_EKAutocompleter._pendingBlockedResultFilterCount
+ _OBJC_IVAR_$_EKAutocompleter._pendingBlockedResultFilterLock
+ _OBJC_IVAR_$_EKLocationSearchModel._conferenceRoomAvailabilityByAddress
+ _OBJC_IVAR_$_EKLocationSearchModel._recentsConferenceRoomAddressesToConferenceRooms
+ _OBJC_IVAR_$_EKLocationSearchModel._recentsConferenceRoomOperationQueue
+ _OBJC_IVAR_$_EKRecentContactSearchResult._resolvedConferenceRoom
+ ___111-[EKLocationSearchModel _handleAvailabilityResults:addressToRoomMap:availabilityCache:notifyType:forOperation:]_block_invoke
+ ___111-[EKLocationSearchModel _handleAvailabilityResults:addressToRoomMap:availabilityCache:notifyType:forOperation:]_block_invoke_2
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_2
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_3
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_4
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_5
+ ___35-[EKObject(Shared) emptyValueCache]_block_invoke
+ ___52-[EKAutocompleter _filterBlockedResults:completion:]_block_invoke
+ ___52-[EKAutocompleter _filterBlockedResults:completion:]_block_invoke_2
+ ___55-[EKAutocompleter autocompleteFetch:didReceiveResults:]_block_invoke
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_32_e40_"NSString"16?0"CNAutocompleteResult"8l
+ ___block_descriptor_56_e8_32s40s48s_e33_v32?0"EKConferenceRoom"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56w_e22_v16?0"NSDictionary"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48w56w_e5_v8?0lw48l8w56l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_filterBlockedResults:completion:
+ _objc_msgSend$_handleAvailabilityResults:addressToRoomMap:availabilityCache:notifyType:forOperation:
+ _objc_msgSend$_requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:
+ _objc_msgSend$_requestAvailabilityForRecentsConferenceRooms:
+ _objc_msgSend$_setCachedMeltedObject:forKey:
+ _objc_msgSend$_setCachedValue:forKey:
+ _objc_msgSend$_updateAvailabilityForRecentsConferenceRooms
+ _objc_msgSend$filterUnblockedResults:usingBlockList:emailForResult:phoneForResult:completionQueue:completion:
+ _objc_msgSend$resolvedConferenceRoom
+ _objc_msgSend$setResolvedConferenceRoom:
+ _objc_msgSend$textRepresentation
+ _symbolic SDySS_____G 10Foundation20PersonNameComponentsV
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic ScCySDySS_____G_____G 10Foundation20PersonNameComponentsV s5NeverO
+ _symbolic _____ySS_____G s18_DictionaryStorageC 10Foundation20PersonNameComponentsV
- +[EKFeatureSet _currentSplashScreenVersion]
- +[EKFeatureSet mustDisplaySplashScreenToUser]
- +[EKFeatureSet userAcknowledgedSplashScreen]
- -[EKLocationSearchModel _handleAvailabilityResults:forOperation:]
- -[EKObject(Shared) _sharedInit]
- GCC_except_table118
- GCC_except_table134
- GCC_except_table138
- GCC_except_table166
- GCC_except_table171
- GCC_except_table200
- GCC_except_table207
- GCC_except_table22
- GCC_except_table27
- GCC_except_table28
- GCC_except_table50
- GCC_except_table53
- GCC_except_table58
- GCC_except_table75
- GCC_except_table86
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- ___55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_2
- ___55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_3
- ___55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_4
- ___55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_5
- ___65-[EKLocationSearchModel _handleAvailabilityResults:forOperation:]_block_invoke
- ___65-[EKLocationSearchModel _handleAvailabilityResults:forOperation:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e33_v32?0"EKConferenceRoom"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8
- _objc_msgSend$_currentSplashScreenVersion
- _objc_msgSend$_handleAvailabilityResults:forOperation:
- _objc_msgSend$_sharedInit
- _objc_msgSend$bypassSplashScreen
- _objc_msgSend$setLastConfirmedSplashScreenVersion:
CStrings:
+ "@\"NSString\"16@?0@\"CNAutocompleteResult\"8"
+ "Not issuing recents availability request because the source does not support it: [%@]"
+ "com.apple.calendar.intelligentScheduler.contactsLookup"
+ "suggestedAttendees(for:source:limit:)"
+ "\xf0\xf0\x81"
- "1"
- "\xf0\xf0Q"
```
