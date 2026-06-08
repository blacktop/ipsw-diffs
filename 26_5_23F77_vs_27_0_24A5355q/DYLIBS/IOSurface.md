## IOSurface

> `/System/Library/Frameworks/IOSurface.framework/IOSurface`

```diff

-393.5.7.0.0
-  __TEXT.__text: 0x13a24
-  __TEXT.__auth_stubs: 0xe00
+401.3.0.0.0
+  __TEXT.__text: 0x1389c
   __TEXT.__objc_methlist: 0x9ec
-  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__gcc_except_tab: 0x130
   __TEXT.__const: 0x153
   __TEXT.__oslogstring: 0x6ae
-  __TEXT.__cstring: 0x2983
-  __TEXT.__unwind_info: 0x600
-  __TEXT.__objc_classname: 0x192
-  __TEXT.__objc_methname: 0x1371
-  __TEXT.__objc_methtype: 0xc7f
-  __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0xa48
+  __TEXT.__cstring: 0x29a8
+  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xaa8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x620
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__cfstring: 0x2040
   __AUTH_CONST.__objc_const: 0x12e0
+  __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x6e8
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x2b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CD71ECE-5CC4-35CC-91E7-095A391E387F
-  Functions: 664
-  Symbols:   1940
-  CStrings:  1053
+  UUID: 16CE6F2B-EE33-368E-B8A2-172E684BDBA0
+  Functions: 659
+  Symbols:   1928
+  CStrings:  690
 
Symbols:
+ GCC_except_table25
+ _CFArrayGetValueAtIndex
+ __ZNKSt9type_infoeqB9fqe220100ERKS_
+ __ZNSt3__110shared_ptrIA_30IOSurfaceTransactionSerializedEC2B9fqe220100IS1_NS_14default_deleteIS2_EELi0EEEPT_T0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS8_SC_SA_EENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS8_SC_SA_EENS_9allocatorIS8_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS8_SC_SA_EENS_9allocatorIS8_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS8_SC_SA_EENS_9allocatorIS8_EEED2Ev
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220100Ev
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEEEENS_21__unordered_map_equalImS8_SC_SA_EENS_9allocatorIS8_EEE16__emplace_uniqueB9fqe220100IJRKNS_21piecewise_construct_tENS_5tupleIJRS7_EEENSN_IJEEEEEENS6_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEEDpOT_ENKUlSO_SM_OSP_OSQ_E_clESO_SM_S11_S12_
+ __ioSurfaceValidateNonNegativeProperties.bufferKeys
+ __ioSurfaceValidateNonNegativeProperties.planeKeys
+ __isNegativeCFNumber
+ _kIOSurfaceAGXUseNearestChromaFiltering
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
- GCC_except_table26
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- __ZNKSt9type_infoeqB9nqe210106ERKS_
- __ZNSt3__110shared_ptrIA_30IOSurfaceTransactionSerializedEC2B9nqe210106IS1_NS_14default_deleteIS2_EELi0EEEPT_T0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRS7_EEENSN_IJEEEEEENS6_INS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImP20IOSurfaceTransactionEENS_22__unordered_map_hasherImNS_4pairIKmS3_EENS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS8_SC_SA_Lb1EEENS_9allocatorIS8_EEED2Ev
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZSt9terminatev
- ___clang_call_terminate
- ___cxa_begin_catch
- ___cxa_end_catch
- ___cxa_rethrow
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "AGXUseNearestChromaFiltering"
- "#16@0:8"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"IOSurfaceRemotePerSurfaceGlobalState\""
- "@\"IOSurfaceSharedEvent\""
- "@\"IOSurfaceTransaction\"24@0:8Q16"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{__IOSurfaceClient=}16"
- "@24@0:8r^v16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8@16Q24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8r^{?=QIIIIIIIIQQCCCCIQQQQQQQ}16r^{?=QQQQIII}24@32"
- "@44@0:8I16^v20Q28@36"
- "@48@0:8^{__IOSurfaceClient=}16^v24Q32@40"
- "@56@0:8{shared_ptr<IOSurfaceTransactionSerialized[]>=^{?}^{__shared_weak_count}}16Q32Q40Q48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8Q16Q24"
- "I"
- "I16@0:8"
- "I24@0:8Q16"
- "IOSurface"
- "IOSurfaceDebugDescription"
- "IOSurfaceMemoryPool"
- "IOSurfaceRemotePerSurfaceGlobalState"
- "IOSurfaceRemotePerSurfacePerClientState"
- "IOSurfaceRemoteRemoteClient"
- "IOSurfaceRemoteServer"
- "IOSurfaceSharedEvent"
- "IOSurfaceSharedEventListener"
- "IOSurfaceTransaction"
- "IOSurfaceTransactionList"
- "IOSurfaceTransactionListImpl"
- "IOSurfaceWiringAssertion"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "T#,R"
- "T@\"IOSurfaceRemotePerSurfaceGlobalState\",&,N,V_globalState"
- "T@\"IOSurfaceSharedEvent\",R,V_event"
- "T@\"NSMutableArray\",&,N,V_clients"
- "T@\"NSMutableDictionary\",&,N,V_surfaceStates"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_disconnectedQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_listener"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_remoteConnection"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,D"
- "T@?,C,N,V_disconnectedHandler"
- "TB,R"
- "TB,R,D"
- "TB,R,GisInUse"
- "TB,R,V_isWrite"
- "TI,R"
- "TI,R,D"
- "TI,R,N"
- "TI,R,V_eventPort"
- "TQ"
- "TQ,R"
- "TQ,R,D"
- "TQ,R,V_globalTraceObjectID"
- "TQ,R,V_kernelFullListLength"
- "TQ,R,V_length"
- "TQ,R,V_selectedLength"
- "TQ,R,V_waitValue"
- "T^v,R"
- "T^{__IOSurfaceClient=},R,N"
- "Ti,N,V_pid"
- "Ti,R"
- "Tq,R"
- "UTF8String"
- "Vv16@0:8"
- "^v"
- "^v16@0:8"
- "^v24@0:8Q16"
- "^{IONotificationPort=}"
- "^{_NSZone=}16@0:8"
- "^{__IOSurfaceClient=}"
- "^{__IOSurfaceClient=}16@0:8"
- "^{__IOSurfaceClient=}36@0:8I16@20^@28"
- "_IOSurfaceDebugDescription"
- "_addSurface:mappedAddress:mappedSize:extraData:"
- "_basicInfo"
- "_cfTypeID"
- "_clients"
- "_csid"
- "_disconnectedHandler"
- "_disconnectedQueue"
- "_dispatchQueue"
- "_event"
- "_eventOptions"
- "_eventPort"
- "_extraData"
- "_getClient:inboundExtradata:outboundExtraData:"
- "_globalState"
- "_globalTraceObjectID"
- "_handleClientConnection:"
- "_handleClientDisconnected:"
- "_handleError:"
- "_handleMessage:"
- "_impl"
- "_isWrite"
- "_kernelFullListLength"
- "_layoutInfo"
- "_length"
- "_listener"
- "_lock"
- "_mach_port"
- "_mapped_address"
- "_mapped_size"
- "_mtx"
- "_name"
- "_notificationPort"
- "_notifyEventPort:event:atValue:block:"
- "_pid"
- "_poolId"
- "_poolPort"
- "_queue"
- "_refcount"
- "_remoteConnection"
- "_removeSurface:"
- "_selectedLength"
- "_serializedData"
- "_signaledValue"
- "_surface"
- "_surfaceStates"
- "_txnCache"
- "_waitValue"
- "addClientReferenceToSurfaceWithExtraData:"
- "addEntriesFromDictionary:"
- "addObject:"
- "allAttachments"
- "allocationSize"
- "allowsPixelSizeCasting"
- "arrayWithObjects:count:"
- "attachmentForKey:"
- "autorelease"
- "baseAddress"
- "baseAddressOfPlaneAtIndex:"
- "bytes"
- "bytesPerElement"
- "bytesPerElementOfPlaneAtIndex:"
- "bytesPerRow"
- "bytesPerRowOfPlaneAtIndex:"
- "cStringUsingEncoding:"
- "class"
- "clients"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "copy"
- "copyDebugInfo"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "debugRefCount"
- "decodeXPCObjectOfType:forKey:"
- "decrementUseCount"
- "decrementUseCountForCategory:"
- "defaultManager"
- "description"
- "dirtySize"
- "disconnectedHandler"
- "disconnectedQueue"
- "elementHeight"
- "elementHeightOfPlaneAtIndex:"
- "elementWidth"
- "elementWidthOfPlaneAtIndex:"
- "encodeWithCoder:"
- "encodeXPCObject:forKey:"
- "ensureMemory:"
- "event"
- "eventPort"
- "eventPortAtIndex:"
- "flush:"
- "formattedDescription:"
- "fromSerialized:"
- "getBytes:length:"
- "globalState"
- "globalStateForSurface:mappedAddress:mappedSize:extraData:"
- "globalTraceObjectID"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "height"
- "heightOfPlaneAtIndex:"
- "i16@0:8"
- "i24@0:8@16"
- "i28@0:8I16^I20"
- "inUse"
- "incrementUseCount"
- "incrementUseCountForCategory:"
- "init"
- "initWithBasicInfo:layoutInfo:name:"
- "initWithBytes:length:"
- "initWithClientBuffer:"
- "initWithCoder:"
- "initWithDispatchQueue:"
- "initWithIOSurface:"
- "initWithIOSurfaceClient:"
- "initWithListener:options:"
- "initWithMachPort:"
- "initWithOptions:"
- "initWithProperties:"
- "initWithRemoteConnection:disconnectedQueue:disconnectedHandler:"
- "initWithSerializedData:numWritten:actualLength:selectedLength:"
- "initWithSharedEvent:waitValue:isWrite:"
- "initWithSurface:mappedAddress:mappedSize:extraData:"
- "initWithSurfaceID:"
- "initWithSurfaceID:mappedAddress:mappedSize:extraData:"
- "intValue"
- "isDisplayable"
- "isEqual:"
- "isInUse"
- "isInUseForAnyOtherCategory:"
- "isInUseForCategory:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMemoryRegionUsed"
- "isProxy"
- "isSysMemOnly"
- "isWired"
- "isWrite"
- "kernelFullListLength"
- "lastPathComponent"
- "length"
- "listener"
- "localUseCount"
- "lockWithOptions:seed:"
- "mergeExtraData:"
- "name"
- "newChildSurfaceWithProperties:"
- "newWiringAssertion"
- "notifyListener:atValue:block:"
- "numberOfUseCountCategories"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pixelFormat"
- "pixelFormatString"
- "planeCount"
- "poolId"
- "protectionOptions"
- "q16@0:8"
- "q24@0:8Q16"
- "queue"
- "r^Q"
- "raise:format:"
- "rangeOfString:"
- "registryID"
- "release"
- "remoteConnection"
- "removeAllAttachments"
- "removeAllObjects"
- "removeAttachmentForKey:"
- "removeClientReferenceToSurface"
- "removeObject:"
- "removeObjectForKey:"
- "residentSize"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "seed"
- "selectedLength"
- "self"
- "setAllAttachments:"
- "setAttachment:forKey:"
- "setClients:"
- "setDisconnectedHandler:"
- "setDisconnectedQueue:"
- "setGlobalState:"
- "setListener:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPid:"
- "setPurgeable:oldState:"
- "setQueue:"
- "setRemoteConnection:"
- "setSignaledValue:"
- "setSurfaceStates:"
- "setTimestamp:atIndex:"
- "setValue:forKey:"
- "shutdown"
- "signaledValue"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringWithCString:encoding:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongToWeakObjectsMapTable"
- "substringFromIndex:"
- "superclass"
- "supportsProtectionOptions:"
- "supportsRollback"
- "supportsSecureCoding"
- "surface"
- "surfaceDescriptions"
- "surfaceID"
- "surfaceStates"
- "timestampAtIndex:"
- "traceID"
- "transactionAtIndex:"
- "unlockWithOptions:seed:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v32@0:8Q16Q24"
- "v40@0:8@16Q24@?32"
- "v44@0:8I16@20Q28@?36"
- "v48@0:8^{__IOSurfaceClient=}16^v24Q32@40"
- "virtualAddress"
- "waitUntilSignaledValue:timeoutMS:"
- "waitValue"
- "width"
- "widthOfPlaneAtIndex:"
- "zone"
- "{?=\"clientAddress\"Q\"surfaceID\"I\"pixelFormat\"I\"retainCount\"I\"yCbCrMatrix\"I\"cacheMode\"I\"mapCacheAttribute\"I\"purgeableState\"I\"purgeableStateAPI\"I\"allocOffset\"Q\"allocSize\"Q\"isGlobal\"C\"isAllocated\"C\"isWired\"C\"pad\"C\"parentSurfaceID\"I\"detachModeCode\"Q\"initDetachModeCodeTime\"Q\"protectionOptions\"Q\"residentSize\"Q\"dirtySize\"Q\"traceID\"Q\"memDescID\"Q}"
- "{?=\"offset\"Q\"width\"Q\"height\"Q\"bytesPerRow\"Q\"bytesPerElement\"I\"elementWidth\"I\"elementHeight\"I}"
- "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{shared_ptr<IOSurfaceTransactionSerialized[]>=\"__ptr_\"^{?}\"__cntrl_\"^{__shared_weak_count}}"
- "{unordered_map<unsigned long, IOSurfaceTransaction *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, IOSurfaceTransaction *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, IOSurfaceTransaction *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
