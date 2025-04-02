## SystemStatusUI

> `/System/Library/PrivateFrameworks/SystemStatusUI.framework/Versions/A/SystemStatusUI`

```diff

-210.4.13.0.0
-  __TEXT.__text: 0x4afc
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0x474
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x3ab
-  __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methname: 0xf36
-  __TEXT.__objc_methtype: 0x2d8
-  __TEXT.__objc_stubs: 0xc00
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x118
+210.5.2.0.0
+  __TEXT.__text: 0xa44
+  __TEXT.__auth_stubs: 0x70
+  __TEXT.__objc_methlist: 0xe0
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x96
+  __TEXT.__unwind_info: 0x88
+  __TEXT.__objc_classname: 0x7a
+  __TEXT.__objc_methname: 0x1cb
+  __TEXT.__objc_methtype: 0x48
+  __TEXT.__objc_stubs: 0x60
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xe8
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x8d0
+  __AUTH_CONST.__auth_got: 0x40
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__objc_const: 0x2d0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x240
-  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 119
-  Symbols:   373
-  CStrings:  259
+  Functions: 21
+  Symbols:   75
+  CStrings:  35
 
Symbols:
+ -[STUIDataAccessStatusDomain observeData:]
+ -[STUIDataAccessStatusDomain observeDataWithBlock:]
+ -[STUIMutableDataAccessStatusDomainData dataAccessAttributions]
+ _OBJC_CLASS_$_STDataAccessAttribution
+ _OBJC_CLASS_$_STDataAccessStatusDomain
+ _OBJC_CLASS_$_STDataAccessStatusDomainData
+ _OBJC_CLASS_$_STMutableDataAccessStatusDomainData
+ _OBJC_METACLASS_$_STDataAccessAttribution
+ _OBJC_METACLASS_$_STDataAccessStatusDomain
+ _OBJC_METACLASS_$_STDataAccessStatusDomainData
+ _OBJC_METACLASS_$_STMutableDataAccessStatusDomainData
+ __OBJC_$_PROP_LIST_STUIDataAccessStatusDomain
+ ___42-[STUIDataAccessStatusDomain observeData:]_block_invoke
+ ___51-[STUIDataAccessStatusDomain observeDataWithBlock:]_block_invoke
+ ___56-[STUIDataAccessStatusDomainData dataAccessAttributions]_block_invoke
+ ___63-[STUIMutableDataAccessStatusDomainData dataAccessAttributions]_block_invoke
+ ___block_descriptor_32_e33_16?0"STDataAccessAttribution"8l
+ ___block_descriptor_40_e8_32bs_e38_v16?0"STDataAccessStatusDomainData"8l
+ ___block_descriptor_40_e8_32bs_e76_v24?0"STDataAccessStatusDomainData"8"<STStatusDomainDataChangeContext>"16l
+ ___copy_helper_block_e8_32b
+ __block_literal_global.28
+ _objc_msgSend$initWithDataAccessAttribution:
- +[STUIDataAccessStatusDomain statusDomainName]
- -[STUIDataAccessAttribution .cxx_destruct]
- -[STUIDataAccessAttribution _isWithinMinimumOnTimeWindow]
- -[STUIDataAccessAttribution accessEndDate]
- -[STUIDataAccessAttribution accessStartDate]
- -[STUIDataAccessAttribution attributedEntity]
- -[STUIDataAccessAttribution audioRecordingActivityAttribution]
- -[STUIDataAccessAttribution cameraCaptureAttribution]
- -[STUIDataAccessAttribution copyWithZone:]
- -[STUIDataAccessAttribution descriptionBuilderWithMultilinePrefix:]
- -[STUIDataAccessAttribution descriptionWithMultilinePrefix:]
- -[STUIDataAccessAttribution description]
- -[STUIDataAccessAttribution hasSatisfiedMinimumOnTime]
- -[STUIDataAccessAttribution hash]
- -[STUIDataAccessAttribution initWithAudioRecordingActivityAttribution:recent:startDate:endDate:]
- -[STUIDataAccessAttribution initWithCameraCaptureAttribution:recent:startDate:endDate:]
- -[STUIDataAccessAttribution initWithDataAccessType:microphoneRecordingAttribution:cameraCaptureAttribution:locationAttribution:recent:startDate:endDate:]
- -[STUIDataAccessAttribution initWithLocationAttribution:recent:startDate:endDate:]
- -[STUIDataAccessAttribution initWithMicrophoneRecordingAttribution:recent:startDate:endDate:]
- -[STUIDataAccessAttribution isEqual:]
- -[STUIDataAccessAttribution isRecent]
- -[STUIDataAccessAttribution locationAttribution]
- -[STUIDataAccessAttribution microphoneRecordingAttribution]
- -[STUIDataAccessAttribution succinctDescriptionBuilder]
- -[STUIDataAccessAttribution succinctDescription]
- -[STUIDataAccessStatusDomain .cxx_destruct]
- -[STUIDataAccessStatusDomain _dataAccessAttributionsForAttributions:dataAccessType:dataAccessAttributionProvider:]
- -[STUIDataAccessStatusDomain _internalQueue_beginWaitingForLingerTimeForAttribution:]
- -[STUIDataAccessStatusDomain _internalQueue_generatedData]
- -[STUIDataAccessStatusDomain _internalQueue_handleLocationData:mediaData:]
- -[STUIDataAccessStatusDomain _internalQueue_notifyClientsOfData:]
- -[STUIDataAccessStatusDomain _internalQueue_updateDataForLocationData:mediaData:]
- -[STUIDataAccessStatusDomain dealloc]
- -[STUIDataAccessStatusDomain initWithServerHandle:]
- -[STUIDataAccessStatusDomain invalidate]
- -[STUIDataAccessStatusDomainData .cxx_destruct]
- -[STUIDataAccessStatusDomainData _allEntities]
- -[STUIDataAccessStatusDomainData _dataWithAttributionFilter:]
- -[STUIDataAccessStatusDomainData _initWithAttributionListData:]
- -[STUIDataAccessStatusDomainData attributedEntities]
- -[STUIDataAccessStatusDomainData attributionListData]
- -[STUIDataAccessStatusDomainData copyWithZone:]
- -[STUIDataAccessStatusDomainData descriptionBuilderWithMultilinePrefix:]
- -[STUIDataAccessStatusDomainData descriptionWithMultilinePrefix:]
- -[STUIDataAccessStatusDomainData description]
- -[STUIDataAccessStatusDomainData executableIdentities]
- -[STUIDataAccessStatusDomainData hash]
- -[STUIDataAccessStatusDomainData initWithAttributionListData:]
- -[STUIDataAccessStatusDomainData initWithData:]
- -[STUIDataAccessStatusDomainData init]
- -[STUIDataAccessStatusDomainData isEqual:]
- -[STUIDataAccessStatusDomainData mutableCopyWithZone:]
- -[STUIDataAccessStatusDomainData succinctDescriptionBuilder]
- -[STUIDataAccessStatusDomainData succinctDescription]
- -[STUIDataAccessStatusDomainData userIdentities]
- -[STUIMutableDataAccessStatusDomainData attributionListData]
- -[STUIMutableDataAccessStatusDomainData copyWithZone:]
- -[STUIMutableDataAccessStatusDomainData initWithAttributionListData:]
- GCC_except_table0
- GCC_except_table1
- GCC_except_table30
- GCC_except_table33
- GCC_except_table9
- OBJC_IVAR_$_STUIDataAccessAttribution._accessEndDate
- OBJC_IVAR_$_STUIDataAccessAttribution._accessStartDate
- OBJC_IVAR_$_STUIDataAccessAttribution._cameraCaptureAttribution
- OBJC_IVAR_$_STUIDataAccessAttribution._dataAccessType
- OBJC_IVAR_$_STUIDataAccessAttribution._locationAttribution
- OBJC_IVAR_$_STUIDataAccessAttribution._microphoneRecordingAttribution
- OBJC_IVAR_$_STUIDataAccessAttribution._recent
- OBJC_IVAR_$_STUIDataAccessStatusDomainData._attributionListData
- _BSDispatchQueueCreateSerial
- _BSFloatGreaterThanFloat
- _BSLogAddStateCaptureBlockWithTitle
- _OBJC_CLASS_$_BSContinuousMachTimer
- _OBJC_CLASS_$_BSDescriptionBuilder
- _OBJC_CLASS_$_BSEqualsBuilder
- _OBJC_CLASS_$_BSHashBuilder
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_STActivityAttribution
- _OBJC_CLASS_$_STAttributedEntity
- _OBJC_CLASS_$_STListData
- _OBJC_CLASS_$_STLocationStatusDomain
- _OBJC_CLASS_$_STLocationStatusDomainLocationAttribution
- _OBJC_CLASS_$_STMediaStatusDomain
- _OBJC_CLASS_$_STMediaStatusDomainMicrophoneRecordingAttribution
- _OBJC_CLASS_$_STMutableListData
- _OBJC_CLASS_$_STStatusDomain
- _OBJC_METACLASS_$_STStatusDomain
- _STUIDataAccessStatusDomainMinumumOnTime
- __37-[STUIDataAccessAttribution isEqual:]_block_invoke.3
- __37-[STUIDataAccessAttribution isEqual:]_block_invoke.7
- __51-[STUIDataAccessStatusDomain initWithServerHandle:]_block_invoke.10
- __51-[STUIDataAccessStatusDomain initWithServerHandle:]_block_invoke.18
- __51-[STUIDataAccessStatusDomain initWithServerHandle:]_block_invoke_2.11
- __Block_object_dispose
- __MergedGlobals
- __OBJC_$_CLASS_METHODS_STUIDataAccessStatusDomain
- __OBJC_$_INSTANCE_VARIABLES_STUIDataAccessAttribution
- __OBJC_$_INSTANCE_VARIABLES_STUIDataAccessStatusDomain
- __OBJC_$_INSTANCE_VARIABLES_STUIDataAccessStatusDomainData
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSDescriptionProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSMutableCopying
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSDescriptionProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSMutableCopying
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_REFS_BSDescriptionProviding
- __OBJC_$_PROTOCOL_REFS_STMutableStatusDomainData
- __OBJC_$_PROTOCOL_REFS_STStatusDomainData
- __OBJC_CLASS_PROTOCOLS_$_STUIDataAccessAttribution
- __OBJC_CLASS_PROTOCOLS_$_STUIDataAccessStatusDomainData
- __OBJC_CLASS_PROTOCOLS_$_STUIMutableDataAccessStatusDomainData
- __OBJC_LABEL_PROTOCOL_$_BSDescriptionProviding
- __OBJC_LABEL_PROTOCOL_$_NSCopying
- __OBJC_LABEL_PROTOCOL_$_NSMutableCopying
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_LABEL_PROTOCOL_$_STMutableStatusDomainData
- __OBJC_LABEL_PROTOCOL_$_STStatusDomainData
- __OBJC_PROTOCOL_$_BSDescriptionProviding
- __OBJC_PROTOCOL_$_NSCopying
- __OBJC_PROTOCOL_$_NSMutableCopying
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_STMutableStatusDomainData
- __OBJC_PROTOCOL_$_STStatusDomainData
- __Unwind_Resume
- ___34-[STUIDataAccessStatusDomain data]_block_invoke
- ___37-[STUIDataAccessAttribution isEqual:]_block_invoke
- ___37-[STUIDataAccessAttribution isEqual:]_block_invoke_2
- ___37-[STUIDataAccessAttribution isEqual:]_block_invoke_3
- ___37-[STUIDataAccessAttribution isEqual:]_block_invoke_4
- ___40-[STUIDataAccessStatusDomain invalidate]_block_invoke
- ___42-[STUIDataAccessStatusDomainData isEqual:]_block_invoke
- ___46-[STUIDataAccessStatusDomainData _allEntities]_block_invoke
- ___51-[STUIDataAccessStatusDomain initWithServerHandle:]_block_invoke
- ___51-[STUIDataAccessStatusDomain initWithServerHandle:]_block_invoke_2
- ___51-[STUIDataAccessStatusDomain initWithServerHandle:]_block_invoke_3
- ___52-[STUIDataAccessStatusDomainData _allUserIdentities]_block_invoke
- ___53-[STUIDataAccessStatusDomainData dataWithAccessType:]_block_invoke
- ___54-[STUIDataAccessStatusDomainData _sortedAttributions:]_block_invoke
- ___54-[STUIDataAccessStatusDomainData executableIdentities]_block_invoke
- ___55-[STUIDataAccessStatusDomainData activeAttributionData]_block_invoke
- ___55-[STUIDataAccessStatusDomainData dataWithUserIdentity:]_block_invoke
- ___55-[STUIDataAccessStatusDomainData recentAttributionData]_block_invoke
- ___59-[STUIDataAccessStatusDomainData dataWithAttributedEntity:]_block_invoke
- ___61-[STUIDataAccessStatusDomainData dataWithExecutableIdentity:]_block_invoke
- ___65-[STUIDataAccessStatusDomain _internalQueue_notifyClientsOfData:]_block_invoke
- ___67-[STUIDataAccessAttribution descriptionBuilderWithMultilinePrefix:]_block_invoke
- ___67-[STUIDataAccessStatusDomain _internalQueue_makeAttributionRecent:]_block_invoke
- ___72-[STUIDataAccessStatusDomainData dataWithEntitiesThatAreSystemServices:]_block_invoke
- ___73-[STUIDataAccessStatusDomainData unsatisfiedMinimumOnTimeAttributionData]_block_invoke
- ___75-[STUIDataAccessStatusDomain _filteredLocationAttributionsForLocationData:]_block_invoke
- ___75-[STUIDataAccessStatusDomain _filteredLocationAttributionsForLocationData:]_block_invoke_2
- ___77-[STUIDataAccessStatusDomain _dataAccessAttributionsForLocationAttributions:]_block_invoke
- ___82-[STUIDataAccessStatusDomain _dataAccessAttributionsForCameraCaptureAttributions:]_block_invoke
- ___85-[STUIDataAccessStatusDomain _internalQueue_beginWaitingForLingerTimeForAttribution:]_block_invoke
- ___88-[STUIDataAccessStatusDomain _dataAccessAttributionsForMicrophoneRecordingAttributions:]_block_invoke
- ___94-[STUIDataAccessStatusDomain _internalQueue_beginWaitingForMinimumDisplayTime:forAttribution:]_block_invoke
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___CFConstantStringClassReference
- ___block_descriptor_32_e28_16?0"STAttributedEntity"8l
- ___block_descriptor_32_e35_"STUIDataAccessAttribution"16?08l
- ___block_descriptor_32_e35_16?0"STUIDataAccessAttribution"8l
- ___block_descriptor_32_e35_B16?0"STUIDataAccessAttribution"8l
- ___block_descriptor_32_e65_q24?0"STUIDataAccessAttribution"8"STUIDataAccessAttribution"16l
- ___block_descriptor_33_e35_B16?0"STUIDataAccessAttribution"8l
- ___block_descriptor_40_e35_B16?0"STUIDataAccessAttribution"8l
- ___block_descriptor_40_e51_B16?0"STLocationStatusDomainLocationAttribution"8l
- ___block_descriptor_40_e8_32s_e17_"<NSObject>"8?0l
- ___block_descriptor_40_e8_32s_e35_B16?0"STUIDataAccessAttribution"8l
- ___block_descriptor_40_e8_32s_e5_Q8?0l
- ___block_descriptor_40_e8_32s_e5_v8?0l
- ___block_descriptor_40_e8_32w_e5_8?0l
- ___block_descriptor_40_e8_32w_e71_v24?0"STMediaStatusDomainData"8"<STStatusDomainDataChangeContext>"16l
- ___block_descriptor_40_e8_32w_e80_v24?0"STLocationStatusDomainData"8"STLocationStatusDomainDataChangeContext"16l
- ___block_descriptor_41_e8_32s_e51_16?0"STLocationStatusDomainLocationAttribution"8l
- ___block_descriptor_48_e8_32s40r_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e5_v8?0l
- ___block_descriptor_48_e8_32s40w_e31_v16?0"BSContinuousMachTimer"8l
- ___block_descriptor_48_e8_32s40w_e5_v8?0l
- ___copy_helper_block_e8_32s
- ___copy_helper_block_e8_32s40r
- ___copy_helper_block_e8_32s40s
- ___copy_helper_block_e8_32s40w
- ___copy_helper_block_e8_32w
- ___destroy_helper_block_e8_32s40r
- ___destroy_helper_block_e8_32s40s
- ___destroy_helper_block_e8_32s40w
- ___destroy_helper_block_e8_32w
- ___objc_personality_v0
- ___stack_chk_fail
- ___stack_chk_guard
- __block_literal_global.10
- __block_literal_global.25
- __block_literal_global.27
- __block_literal_global.30
- __block_literal_global.40
- __block_literal_global.42
- __block_literal_global.6
- __block_literal_global.8
- __dispatch_main_q
- _dispatch_assert_queue$V2
- _dispatch_async
- _dispatch_sync
- _objc_alloc_init
- _objc_copyWeak
- _objc_destroyWeak
- _objc_enumerationMutation
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSend$_initWithAttributionListData:
- _objc_msgSend$accessEndDate
- _objc_msgSend$accessStartDate
- _objc_msgSend$activeDisplayModes
- _objc_msgSend$activeEntity
- _objc_msgSend$activityAttribution
- _objc_msgSend$addObject:
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$allKeys
- _objc_msgSend$allValues
- _objc_msgSend$allocWithZone:
- _objc_msgSend$appendBodySectionWithName:multilinePrefix:block:
- _objc_msgSend$appendObject:
- _objc_msgSend$appendObject:counterpart:
- _objc_msgSend$appendObject:withName:
- _objc_msgSend$appendObject:withName:skipIfNil:
- _objc_msgSend$appendString:withName:
- _objc_msgSend$appendUnsignedInteger:
- _objc_msgSend$appendUnsignedInteger:counterpart:
- _objc_msgSend$array
- _objc_msgSend$attributedEntity
- _objc_msgSend$attributionListData
- _objc_msgSend$attributions
- _objc_msgSend$audioRecordingActivityAttribution
- _objc_msgSend$bs_filter:
- _objc_msgSend$build
- _objc_msgSend$builder
- _objc_msgSend$builderWithObject:
- _objc_msgSend$builderWithObject:ofExpectedClass:
- _objc_msgSend$cameraAttributions
- _objc_msgSend$cameraCaptureAttribution
- _objc_msgSend$compare:
- _objc_msgSend$copy
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$data
- _objc_msgSend$dataAccessAttributions
- _objc_msgSend$dataAccessType
- _objc_msgSend$date
- _objc_msgSend$description
- _objc_msgSend$descriptionBuilderWithMultilinePrefix:
- _objc_msgSend$descriptionWithMultilinePrefix:
- _objc_msgSend$dictionary
- _objc_msgSend$eligibleDisplayModes
- _objc_msgSend$executableIdentity
- _objc_msgSend$hasSatisfiedMinimumOnTime
- _objc_msgSend$hash
- _objc_msgSend$initWithActivityAttribution:
- _objc_msgSend$initWithAttributedEntity:activeEntity:
- _objc_msgSend$initWithAttributionListData:
- _objc_msgSend$initWithAudioRecordingActivityAttribution:recent:startDate:endDate:
- _objc_msgSend$initWithCameraCaptureAttribution:recent:startDate:endDate:
- _objc_msgSend$initWithExecutableIdentity:userIdentity:website:systemService:localizedDisplayName:localizedExecutableDisplayName:
- _objc_msgSend$initWithIdentifier:
- _objc_msgSend$initWithLocationAttribution:recent:startDate:endDate:
- _objc_msgSend$initWithLocationState:activityAttribution:eligibleDisplayModes:
- _objc_msgSend$initWithMicrophoneRecordingAttribution:recent:startDate:endDate:
- _objc_msgSend$initWithServerHandle:
- _objc_msgSend$invalidate
- _objc_msgSend$isEqual
- _objc_msgSend$isEqual:
- _objc_msgSend$isInvalidated
- _objc_msgSend$isRecent
- _objc_msgSend$isSystemService
- _objc_msgSend$localizedExecutableDisplayName
- _objc_msgSend$locationAttribution
- _objc_msgSend$locationState
- _objc_msgSend$matchesAttributedEntity:
- _objc_msgSend$matchesExecutableIdentity:
- _objc_msgSend$matchesUserIdentity:
- _objc_msgSend$maximumHistoryAccessed
- _objc_msgSend$microphoneAttributions
- _objc_msgSend$microphoneRecordingAttribution
- _objc_msgSend$minusSet:
- _objc_msgSend$mutableCopy
- _objc_msgSend$objectForKey:
- _objc_msgSend$objects
- _objc_msgSend$observeData:
- _objc_msgSend$observeData:forDomain:withChangeContext:
- _objc_msgSend$removeObject:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$scheduleWithFireInterval:leewayInterval:queue:handler:
- _objc_msgSend$set
- _objc_msgSend$setDataAccessAttributions:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setObjects:
- _objc_msgSend$setWithArray:
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$succinctDescriptionBuilder
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$unionSet:
- _objc_msgSend$userIdentity
- _objc_msgSend$website
- _objc_opt_class
- _objc_retainAutoreleaseReturnValue
- _objc_setProperty_nonatomic_copy
- _objc_storeStrong
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "@16@?0@\"STDataAccessAttribution\"8"
+ "T@\"NSArray\",C,N"
+ "TQ,R,N"
+ "initWithDataAccessAttribution:"
+ "observeDataWithBlock:"
+ "v16@?0@\"STDataAccessStatusDomainData\"8"
+ "v24@0:8@?16"
+ "v24@?0@\"STDataAccessStatusDomainData\"8@\"<STStatusDomainDataChangeContext>\"16"
- "\x01"
- "\r"
- " (in minimum on time)"
- "#16@0:8"
- "%"
- "(empty)"
- ".cxx_destruct"
- "@\"<BSInvalidatable>\""
- "@\"<NSObject>\"8@?0"
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"STListData\""
- "@\"STLocationStatusDomain\""
- "@\"STLocationStatusDomainLocationAttribution\""
- "@\"STMediaStatusDomain\""
- "@\"STMediaStatusDomainCameraCaptureAttribution\""
- "@\"STMediaStatusDomainMicrophoneRecordingAttribution\""
- "@\"STUIDataAccessAttribution\"16@?0@8"
- "@\"STUIDataAccessStatusDomainData\""
- "@16@?0@\"STAttributedEntity\"8"
- "@16@?0@\"STLocationStatusDomainLocationAttribution\"8"
- "@16@?0@\"STUIDataAccessAttribution\"8"
- "@24@0:8:16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@44@0:8@16B24@28@36"
- "@8@?0"
- "B"
- "B16@0:8"
- "B16@?0@\"STLocationStatusDomainLocationAttribution\"8"
- "B16@?0@\"STUIDataAccessAttribution\"8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSDescriptionProviding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "Q"
- "Q8@?0"
- "STMutableStatusDomainData"
- "STStatusDomainData"
- "STUIDataAccessStatusDomain-LingerTime"
- "STUIDataAccessStatusDomain-MinimumDisplayTime"
- "STUIDataAccessStatusDomain-RecentAttributionExpiration"
- "SystemStatusUI - STUIDataAccessStatusDomain"
- "T#,R"
- "T@\"NSArray\",C,D,N"
- "T@\"NSDate\",R,C,N,V_accessEndDate"
- "T@\"NSDate\",R,C,N,V_accessStartDate"
- "T@\"NSSet\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"STActivityAttribution\",R,C,N"
- "T@\"STAttributedEntity\",R,C,N"
- "T@\"STListData\",R,C,N,V_attributionListData"
- "T@\"STLocationStatusDomainLocationAttribution\",R,C,N,V_locationAttribution"
- "T@\"STMediaStatusDomainCameraCaptureAttribution\",R,C,N,V_cameraCaptureAttribution"
- "T@\"STMediaStatusDomainMicrophoneRecordingAttribution\",R,C,N,V_microphoneRecordingAttribution"
- "T@\"STMutableListData\",R,C,N"
- "TB,R,N"
- "TB,R,N,GisRecent,V_recent"
- "TQ,R"
- "TQ,R,N,V_dataAccessType"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessEndDate"
- "_accessStartDate"
- "_activeAttributionLingerTimers"
- "_activeAttributionMinimumDisplayTimers"
- "_activeAttributions"
- "_attributionListData"
- "_attributionsWaitingForLingerTime"
- "_attributionsWaitingForMinimumDisplayTime"
- "_cameraCaptureAttribution"
- "_clientQueue"
- "_currentData"
- "_dataAccessType"
- "_initWithAttributionListData:"
- "_internalQueue"
- "_locationAttribution"
- "_locationDomain"
- "_mediaDomain"
- "_microphoneRecordingAttribution"
- "_recent"
- "_recentAttributionExpirationTimers"
- "_recentAttributions"
- "_stateCaptureHandle"
- "accessEndDate"
- "accessStartDate"
- "active"
- "activeDisplayModes"
- "activeEntity"
- "activityAttribution"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "allValues"
- "allocWithZone:"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendString:withName:"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:counterpart:"
- "array"
- "attributedEntities"
- "attributedEntity"
- "attribution"
- "attributionListData"
- "attributions"
- "audio"
- "audioRecordingActivityAttribution"
- "autorelease"
- "bs_filter:"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "camera"
- "cameraAttributions"
- "cameraCaptureAttribution"
- "class"
- "com.apple.systemstatusui.data-access.clientqueue"
- "com.apple.systemstatusui.data-access.internalqueue"
- "compare:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "date"
- "dealloc"
- "debugDescription"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "dictionary"
- "eligibleDisplayModes"
- "endDate"
- "executableIdentities"
- "executableIdentity"
- "hasSatisfiedMinimumOnTime"
- "hash"
- "init"
- "initWithActivityAttribution:"
- "initWithAttributedEntity:activeEntity:"
- "initWithAttributionListData:"
- "initWithAudioRecordingActivityAttribution:recent:startDate:endDate:"
- "initWithCameraCaptureAttribution:recent:startDate:endDate:"
- "initWithExecutableIdentity:userIdentity:website:systemService:localizedDisplayName:localizedExecutableDisplayName:"
- "initWithIdentifier:"
- "initWithLocationAttribution:recent:startDate:endDate:"
- "initWithLocationState:activityAttribution:eligibleDisplayModes:"
- "initWithMicrophoneRecordingAttribution:recent:startDate:endDate:"
- "initWithServerHandle:"
- "invalid"
- "invalidate"
- "isEqual"
- "isEqual:"
- "isInvalidated"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRecent"
- "isSystemService"
- "localizedExecutableDisplayName"
- "location"
- "locationAttribution"
- "locationState"
- "matchesAttributedEntity:"
- "matchesExecutableIdentity:"
- "matchesUserIdentity:"
- "maximumHistoryAccessed"
- "microphoneAttributions"
- "microphoneRecordingAttribution"
- "minusSet:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "objectForKey:"
- "objects"
- "observeData:forDomain:withChangeContext:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q24@?0@\"STUIDataAccessAttribution\"8@\"STUIDataAccessAttribution\"16"
- "recent"
- "release"
- "removeObject:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "self"
- "set"
- "setObject:forKey:"
- "setObjects:"
- "setWithArray:"
- "sortedArrayUsingComparator:"
- "startDate"
- "state"
- "statusDomainName"
- "stringByAppendingString:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "timeIntervalSinceDate:"
- "type"
- "unionSet:"
- "userIdentities"
- "userIdentity"
- "v16@0:8"
- "v16@?0@\"BSContinuousMachTimer\"8"
- "v24@?0@\"STLocationStatusDomainData\"8@\"STLocationStatusDomainDataChangeContext\"16"
- "v24@?0@\"STMediaStatusDomainData\"8@\"<STStatusDomainDataChangeContext>\"16"
- "v8@?0"
- "website"
- "zone"

```
