## MicroLocationUtilities

> `/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities`

```diff

-27.0.28.0.7
-  __TEXT.__text: 0x4e48
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x8f8
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x2db
-  __TEXT.__gcc_except_tab: 0x90
+27.0.60.0.7
+  __TEXT.__text: 0x6988
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0xbd8
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__cstring: 0x358
   __TEXT.__oslogstring: 0x201
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0xfb
-  __TEXT.__objc_methname: 0xfc2
-  __TEXT.__objc_methtype: 0x56d
-  __TEXT.__objc_stubs: 0xf80
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_classname: 0x18c
+  __TEXT.__objc_methname: 0x1508
+  __TEXT.__objc_methtype: 0x61f
+  __TEXT.__objc_stubs: 0x1400
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x590
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0xde8
-  __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x58
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0x1488
+  __AUTH.__objc_data: 0x1e0
+  __AUTH.__data: 0x18
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0677794-ABF0-32AC-8922-9C681B873BE1
-  Functions: 179
-  Symbols:   803
-  CStrings:  360
+  UUID: EFE55217-85F1-3B0E-8DD7-A2884699FD2B
+  Functions: 239
+  Symbols:   1045
+  CStrings:  449
 
Symbols:
+ +[ULEvent eventName]
+ +[ULNumericUtilities dotProduct:vectorB:]
+ +[ULNumericUtilities magnitudeOfVector:]
+ +[ULNumericUtilities sumOfVector:]
+ +[ULObjectCacheNSString ul_cachedInstanceForNSString:]
+ +[ULPair pairWithFirst:second:]
+ +[ULPlatform deviceClass]
+ +[ULSameSpaceUtilities absoluteVerticalDistanceBetweenPredictionCoordinates:andLabelCoordinates:]
+ +[ULSameSpaceUtilities cosineSimilarityBetweenPredictionProbabilities:andLabelProbabilities:]
+ +[ULSameSpaceUtilities cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:]
+ +[ULSameSpaceUtilities horizontalDistanceSquaredBetweenPredictionCoordinates:andLabelCoordinates:]
+ -[NSArray(MicroLocationUtilities) ul_allWhere:]
+ -[NSArray(MicroLocationUtilities) ul_containsObjectPassingTest:]
+ -[NSArray(MicroLocationUtilities) ul_firstWhere:]
+ -[ULBidirectionalDictionary .cxx_destruct]
+ -[ULBidirectionalDictionary init]
+ -[ULBidirectionalDictionary keyForObject:]
+ -[ULBidirectionalDictionary keyToValueMap]
+ -[ULBidirectionalDictionary objectForKey:]
+ -[ULBidirectionalDictionary setKeyToValueMap:]
+ -[ULBidirectionalDictionary setObject:forKey:]
+ -[ULBidirectionalDictionary setValueToKeyMap:]
+ -[ULBidirectionalDictionary valueToKeyMap]
+ -[ULEvent init]
+ -[ULEvent name]
+ -[ULEventMonitor .cxx_destruct]
+ -[ULEventMonitor addObserver:eventName:handler:]
+ -[ULEventMonitor dealloc]
+ -[ULEventMonitor getNumberOfObserversForEventName:]
+ -[ULEventMonitor init]
+ -[ULEventMonitor latestEventAfterAddingObserverForEventName:]
+ -[ULEventMonitor observersMap]
+ -[ULEventMonitor postEvent:]
+ -[ULEventMonitor queue]
+ -[ULEventMonitor removeObserver:]
+ -[ULEventMonitor removeObserver:fromEventName:]
+ -[ULEventMonitor setObserversMap:]
+ -[ULEventMonitor setQueue:]
+ -[ULEventMonitor startMonitoring:]
+ -[ULEventMonitor stopMonitoring:]
+ -[ULObserverRecord .cxx_destruct]
+ -[ULObserverRecord handler]
+ -[ULObserverRecord observer]
+ -[ULObserverRecord setHandler:]
+ -[ULObserverRecord setObserver:]
+ -[ULPair .cxx_destruct]
+ -[ULPair description]
+ -[ULPair first]
+ -[ULPair initWithFirst:second:]
+ -[ULPair second]
+ GCC_except_table0
+ GCC_except_table8
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_ULBidirectionalDictionary
+ _OBJC_CLASS_$_ULEvent
+ _OBJC_CLASS_$_ULEventMonitor
+ _OBJC_CLASS_$_ULNumericUtilities
+ _OBJC_CLASS_$_ULObjectCacheNSString
+ _OBJC_CLASS_$_ULObserverRecord
+ _OBJC_CLASS_$_ULPair
+ _OBJC_CLASS_$_ULSameSpaceUtilities
+ _OBJC_IVAR_$_ULBidirectionalDictionary._keyToValueMap
+ _OBJC_IVAR_$_ULBidirectionalDictionary._valueToKeyMap
+ _OBJC_IVAR_$_ULEventMonitor._observersMap
+ _OBJC_IVAR_$_ULEventMonitor._queue
+ _OBJC_IVAR_$_ULObserverRecord._handler
+ _OBJC_IVAR_$_ULObserverRecord._observer
+ _OBJC_IVAR_$_ULPair._first
+ _OBJC_IVAR_$_ULPair._second
+ _OBJC_METACLASS_$_ULBidirectionalDictionary
+ _OBJC_METACLASS_$_ULEvent
+ _OBJC_METACLASS_$_ULEventMonitor
+ _OBJC_METACLASS_$_ULNumericUtilities
+ _OBJC_METACLASS_$_ULObjectCacheNSString
+ _OBJC_METACLASS_$_ULObserverRecord
+ _OBJC_METACLASS_$_ULPair
+ _OBJC_METACLASS_$_ULSameSpaceUtilities
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_MicroLocationUtilities
+ __OBJC_$_CATEGORY_NSArray_$_MicroLocationUtilities
+ __OBJC_$_CLASS_METHODS_ULEvent
+ __OBJC_$_CLASS_METHODS_ULNumericUtilities
+ __OBJC_$_CLASS_METHODS_ULObjectCacheNSString
+ __OBJC_$_CLASS_METHODS_ULPair
+ __OBJC_$_CLASS_METHODS_ULSameSpaceUtilities
+ __OBJC_$_INSTANCE_METHODS_ULBidirectionalDictionary
+ __OBJC_$_INSTANCE_METHODS_ULEvent
+ __OBJC_$_INSTANCE_METHODS_ULEventMonitor
+ __OBJC_$_INSTANCE_METHODS_ULObserverRecord
+ __OBJC_$_INSTANCE_METHODS_ULPair
+ __OBJC_$_INSTANCE_VARIABLES_ULBidirectionalDictionary
+ __OBJC_$_INSTANCE_VARIABLES_ULEventMonitor
+ __OBJC_$_INSTANCE_VARIABLES_ULObserverRecord
+ __OBJC_$_INSTANCE_VARIABLES_ULPair
+ __OBJC_$_PROP_LIST_ULBidirectionalDictionary
+ __OBJC_$_PROP_LIST_ULEvent
+ __OBJC_$_PROP_LIST_ULEventMonitor
+ __OBJC_$_PROP_LIST_ULObserverRecord
+ __OBJC_$_PROP_LIST_ULPair
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_RO_$_ULBidirectionalDictionary
+ __OBJC_CLASS_RO_$_ULEvent
+ __OBJC_CLASS_RO_$_ULEventMonitor
+ __OBJC_CLASS_RO_$_ULNumericUtilities
+ __OBJC_CLASS_RO_$_ULObjectCacheNSString
+ __OBJC_CLASS_RO_$_ULObserverRecord
+ __OBJC_CLASS_RO_$_ULPair
+ __OBJC_CLASS_RO_$_ULSameSpaceUtilities
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_ULBidirectionalDictionary
+ __OBJC_METACLASS_RO_$_ULEvent
+ __OBJC_METACLASS_RO_$_ULEventMonitor
+ __OBJC_METACLASS_RO_$_ULNumericUtilities
+ __OBJC_METACLASS_RO_$_ULObjectCacheNSString
+ __OBJC_METACLASS_RO_$_ULObserverRecord
+ __OBJC_METACLASS_RO_$_ULPair
+ __OBJC_METACLASS_RO_$_ULSameSpaceUtilities
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_REFERENCE_$_NSCopying
+ ___25+[ULPlatform deviceClass]_block_invoke
+ ___28-[ULEventMonitor postEvent:]_block_invoke
+ ___33-[ULEventMonitor removeObserver:]_block_invoke
+ ___33-[ULEventMonitor removeObserver:]_block_invoke_2
+ ___33-[ULEventMonitor removeObserver:]_block_invoke_3
+ ___47-[ULEventMonitor removeObserver:fromEventName:]_block_invoke
+ ___47-[ULEventMonitor removeObserver:fromEventName:]_block_invoke.26
+ ___48-[ULEventMonitor addObserver:eventName:handler:]_block_invoke
+ ___48-[ULEventMonitor addObserver:eventName:handler:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32s_e33_v32?0"ULObserverRecord"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32r_e33_v32?0"ULObserverRecord"8Q16^B24lr32l8
+ ___block_descriptor_48_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32r40r_e33_v32?0"ULObserverRecord"8Q16^B24lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e33_v32?0"ULObserverRecord"8Q16^B24ls32l8s40l8s48l8
+ _deviceClass.onceToken
+ _deviceClass.value
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$allKeys
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:
+ _objc_msgSend$dotProduct:vectorB:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$first
+ _objc_msgSend$initWithFirst:second:
+ _objc_msgSend$keyToValueMap
+ _objc_msgSend$latestEventAfterAddingObserverForEventName:
+ _objc_msgSend$magnitudeOfVector:
+ _objc_msgSend$member:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$observer
+ _objc_msgSend$observersMap
+ _objc_msgSend$postEvent:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$second
+ _objc_msgSend$setKeyToValueMap:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setObserversMap:
+ _objc_msgSend$setValueToKeyMap:
+ _objc_msgSend$startMonitoring:
+ _objc_msgSend$stopMonitoring:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$sumOfVector:
+ _objc_msgSend$ul_firstWhere:
+ _objc_msgSend$valueToKeyMap
+ _objc_msgSend$weakObjectsHashTable
+ _objc_release_x2
+ _objc_sync_enter
+ _objc_sync_exit
+ _ul_cachedInstanceForNSString:.cachedInstances
- +[ULPlatform isLimitedMiloUsagePlatform]
- _MGGetProductType
CStrings:
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8@16@24"
+ "B24@0:8@?16"
+ "NSCopying"
+ "T@\"NSMutableDictionary\",&,N,V_keyToValueMap"
+ "T@\"NSMutableDictionary\",&,N,V_observersMap"
+ "T@\"NSMutableDictionary\",&,N,V_valueToKeyMap"
+ "T@\"NSString\",R,N"
+ "T@,R,N,V_first"
+ "T@,R,N,V_second"
+ "Tr^v,N,V_observer"
+ "ULBidirectionalDictionary"
+ "ULEvent"
+ "ULEventMonitor"
+ "ULNumericUtilities"
+ "ULObjectCacheNSString"
+ "ULObserverRecord"
+ "ULPair"
+ "ULPair with first: %@, second: %@"
+ "ULSameSpaceUtilities"
+ "_first"
+ "_keyToValueMap"
+ "_observer"
+ "_observersMap"
+ "_second"
+ "_valueToKeyMap"
+ "absoluteVerticalDistanceBetweenPredictionCoordinates:andLabelCoordinates:"
+ "addObserver:eventName:handler:"
+ "allKeys"
+ "arrayByAddingObject:"
+ "arrayWithObject:"
+ "com.apple.milod.ULEventMonitor"
+ "copyWithZone:"
+ "cosineSimilarityBetweenPredictionProbabilities:andLabelProbabilities:"
+ "cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:"
+ "d24@0:8@16"
+ "d32@0:8@16@24"
+ "d40@0:8@16d24@32"
+ "d48@0:81632"
+ "deviceClass"
+ "dotProduct:vectorB:"
+ "doubleValue"
+ "eventName"
+ "first"
+ "getNumberOfObserversForEventName:"
+ "horizontalDistanceSquaredBetweenPredictionCoordinates:andLabelCoordinates:"
+ "initWithFirst:second:"
+ "keyForObject:"
+ "keyToValueMap"
+ "latestEventAfterAddingObserverForEventName:"
+ "magnitudeOfVector:"
+ "member:"
+ "mutableCopy"
+ "name"
+ "numberWithDouble:"
+ "objectAtIndexedSubscript:"
+ "objectForKey:"
+ "observer"
+ "observersMap"
+ "pairWithFirst:second:"
+ "postEvent:"
+ "r^v"
+ "r^v16@0:8"
+ "removeObject:"
+ "removeObjectAtIndex:"
+ "removeObserver:"
+ "removeObserver:fromEventName:"
+ "second"
+ "setKeyToValueMap:"
+ "setObject:forKey:"
+ "setObserver:"
+ "setObserversMap:"
+ "setValueToKeyMap:"
+ "startMonitoring:"
+ "stopMonitoring:"
+ "stringWithFormat:"
+ "sumOfVector:"
+ "ul_allWhere:"
+ "ul_cachedInstanceForNSString:"
+ "ul_containsObjectPassingTest:"
+ "ul_firstWhere:"
+ "v24@0:8r^v16"
+ "v32@0:8@16@24"
+ "v32@0:8r^v16@24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v32@?0@\"ULObserverRecord\"8Q16^B24"
+ "v40@0:8r^v16@24@?32"
+ "valueToKeyMap"
+ "weakObjectsHashTable"
- "isLimitedMiloUsagePlatform"

```
