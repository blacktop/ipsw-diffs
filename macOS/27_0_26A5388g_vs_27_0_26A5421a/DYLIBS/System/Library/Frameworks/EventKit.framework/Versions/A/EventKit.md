## EventKit

> `/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit`

```diff

-1973.0.0.0.0
-  __TEXT.__text: 0x1b68f8
-  __TEXT.__objc_methlist: 0x15a74
-  __TEXT.__cstring: 0xc22f
-  __TEXT.__const: 0x47b0
-  __TEXT.__oslogstring: 0xeda8
-  __TEXT.__gcc_except_tab: 0x3a04
+1976.0.0.0.0
+  __TEXT.__text: 0x1b8504
+  __TEXT.__objc_methlist: 0x15ac4
+  __TEXT.__cstring: 0xc2bf
+  __TEXT.__const: 0x47c0
+  __TEXT.__oslogstring: 0xee08
+  __TEXT.__gcc_except_tab: 0x3a54
   __TEXT.__dlopen_cstrs: 0x4e4
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
-  __TEXT.__unwind_info: 0x68e8
-  __TEXT.__eh_frame: 0x2578
+  __TEXT.__unwind_info: 0x6958
+  __TEXT.__eh_frame: 0x25e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12b8
+  __DATA_CONST.__const: 0x12d8
   __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaec0
+  __DATA_CONST.__objc_selrefs: 0xaef8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x5d8
-  __DATA_CONST.__got: 0x19d8
-  __AUTH_CONST.__const: 0x8140
+  __DATA_CONST.__got: 0x1a20
+  __AUTH_CONST.__const: 0x82c0
   __AUTH_CONST.__cfstring: 0x9f40
-  __AUTH_CONST.__objc_const: 0x18650
+  __AUTH_CONST.__objc_const: 0x18730
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x1208
+  __AUTH_CONST.__auth_got: 0x1238
   __AUTH.__objc_data: 0x3430
   __AUTH.__data: 0xf08
-  __DATA.__objc_ivar: 0xd5c
-  __DATA.__data: 0x2810
+  __DATA.__objc_ivar: 0xd74
+  __DATA.__data: 0x2870
   __DATA.__bss: 0x45b0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1cc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10792
-  Symbols:   17828
-  CStrings:  2695
+  Functions: 10817
+  Symbols:   17861
+  CStrings:  2698
 
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
+ GCC_except_table133
+ GCC_except_table152
+ GCC_except_table164
+ GCC_except_table168
+ GCC_except_table187
+ GCC_except_table192
+ GCC_except_table232
+ GCC_except_table35
+ GCC_except_table46
+ GCC_except_table66
+ GCC_except_table79
+ GCC_except_table87
+ GCC_except_table90
+ OBJC_IVAR_$_EKAutocompleter._pendingBlockedResultFilterCount
+ OBJC_IVAR_$_EKAutocompleter._pendingBlockedResultFilterLock
+ OBJC_IVAR_$_EKLocationSearchModel._conferenceRoomAvailabilityByAddress
+ OBJC_IVAR_$_EKLocationSearchModel._recentsConferenceRoomAddressesToConferenceRooms
+ OBJC_IVAR_$_EKLocationSearchModel._recentsConferenceRoomOperationQueue
+ OBJC_IVAR_$_EKRecentContactSearchResult._resolvedConferenceRoom
+ _OBJC_CLASS_$_CalBlockListFilter
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke
+ __166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_2
+ ___111-[EKLocationSearchModel _handleAvailabilityResults:addressToRoomMap:availabilityCache:notifyType:forOperation:]_block_invoke
+ ___111-[EKLocationSearchModel _handleAvailabilityResults:addressToRoomMap:availabilityCache:notifyType:forOperation:]_block_invoke_2
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_2
+ ___166-[EKLocationSearchModel _requestAvailabilityForConferenceRooms:eventID:source:dateRange:addressToRoomMap:availabilityCache:operationQueue:operationDomain:notifyType:]_block_invoke_3
+ ___35-[EKObject(Shared) emptyValueCache]_block_invoke
+ ___52-[EKAutocompleter _filterBlockedResults:completion:]_block_invoke
+ ___52-[EKAutocompleter _filterBlockedResults:completion:]_block_invoke_2
+ ___55-[EKAutocompleter autocompleteFetch:didReceiveResults:]_block_invoke
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s_e5_v8?0l
+ ___block_descriptor_32_e40_"NSString"16?0"CNAutocompleteResult"8l
+ ___block_descriptor_56_e8_32s40s48s_e33_v32?0"EKConferenceRoom"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56w_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_72_e8_32s40s48w56w_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s
+ ___copy_helper_block_e8_32s40s48w56w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s
+ ___destroy_helper_block_e8_32s40s48w56w
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
- GCC_except_table117
- GCC_except_table131
- GCC_except_table137
- GCC_except_table143
- GCC_except_table153
- GCC_except_table161
- GCC_except_table184
- GCC_except_table189
- GCC_except_table229
- GCC_except_table33
- GCC_except_table34
- GCC_except_table36
- GCC_except_table61
- GCC_except_table64
- GCC_except_table77
- GCC_except_table83
- GCC_except_table86
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- __55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke
- __55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_2
- ___55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_2
- ___55-[EKLocationSearchModel _addDiscoveredConferenceRooms:]_block_invoke_3
- ___65-[EKLocationSearchModel _handleAvailabilityResults:forOperation:]_block_invoke
- ___65-[EKLocationSearchModel _handleAvailabilityResults:forOperation:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e33_v32?0"EKConferenceRoom"8Q16^B24l
- ___block_descriptor_56_e8_32s40w48w_e5_v8?0l
- ___copy_helper_block_e8_32s40w48w
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
+ "\xf0\xf0q"
- "1"
- "\xf0\xf0A"
```
