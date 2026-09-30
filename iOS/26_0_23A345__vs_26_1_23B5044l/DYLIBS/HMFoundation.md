## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-886.1.1.0.0
-  __TEXT.__text: 0x866d4
-  __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x77a4
-  __TEXT.__const: 0x25e8
+892.0.0.0.0
+  __TEXT.__text: 0x88294
+  __TEXT.__auth_stubs: 0x21a0
+  __TEXT.__objc_methlist: 0x78c4
+  __TEXT.__const: 0x2658
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x3197
-  __TEXT.__swift5_typeref: 0x9e7
+  __TEXT.__cstring: 0x30aa
+  __TEXT.__swift5_typeref: 0x9e3
   __TEXT.__swift5_capture: 0x600
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x194
-  __TEXT.__constg_swiftt: 0xd38
   __TEXT.__swift5_reflstr: 0x373
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0xd38
   __TEXT.__swift5_fieldmd: 0x670
-  __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__oslogstring: 0x418e
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x1c00
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x9c
+  __TEXT.__oslogstring: 0x4213
+  __TEXT.__gcc_except_tab: 0x1c68
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2e70
+  __TEXT.__unwind_info: 0x2ee8
   __TEXT.__eh_frame: 0x2e98
-  __TEXT.__objc_classname: 0x10ed
-  __TEXT.__objc_methname: 0xc5c9
-  __TEXT.__objc_methtype: 0x2788
-  __TEXT.__objc_stubs: 0x9080
-  __DATA_CONST.__got: 0x7e8
-  __DATA_CONST.__const: 0x15d8
-  __DATA_CONST.__objc_classlist: 0x458
+  __TEXT.__objc_classname: 0x110d
+  __TEXT.__objc_methname: 0xc84b
+  __TEXT.__objc_methtype: 0x27b4
+  __TEXT.__objc_stubs: 0x9320
+  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__const: 0x1658
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3040
+  __DATA_CONST.__objc_selrefs: 0x3118
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__const: 0x21b8
-  __AUTH_CONST.__cfstring: 0x4ca0
-  __AUTH_CONST.__objc_const: 0xe2c0
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__const: 0x21d8
+  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__objc_const: 0xe3c8
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x10e0
+  __AUTH.__objc_data: 0x1130
   __AUTH.__data: 0x150
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x2430
   __DATA.__bss: 0x514
-  __DATA_DIRTY.__objc_ivar: 0x5ac
+  __DATA_DIRTY.__objc_ivar: 0x5b0
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B2708130-4C2E-3F2A-A341-131AC048BB92
-  Functions: 3418
-  Symbols:   9293
-  CStrings:  4596
+  UUID: BB337C48-2F32-3B7E-B27D-C09418E537C5
+  Functions: 3458
+  Symbols:   9418
+  CStrings:  4613
 
Symbols:
+ -[HMFKeyValueDatabase .cxx_destruct]
+ -[HMFKeyValueDatabase _cancelSyncTimer]
+ -[HMFKeyValueDatabase _startDelayedSyncTimerIfNeeded]
+ -[HMFKeyValueDatabase _syncWithoutTimerHandling:]
+ -[HMFKeyValueDatabase containsKey:]
+ -[HMFKeyValueDatabase dealloc]
+ -[HMFKeyValueDatabase dictionary]
+ -[HMFKeyValueDatabase diskRepresentation]
+ -[HMFKeyValueDatabase inMemoryDictionary]
+ -[HMFKeyValueDatabase init]
+ -[HMFKeyValueDatabase keys]
+ -[HMFKeyValueDatabase memoryMonitor:didReceiveMemoryEvent:]
+ -[HMFKeyValueDatabase queue]
+ -[HMFKeyValueDatabase removeAllEntriesWithError:]
+ -[HMFKeyValueDatabase setDiskRepresentation:]
+ -[HMFKeyValueDatabase setInMemoryDictionary:]
+ -[HMFKeyValueDatabase setQueue:]
+ -[HMFKeyValueDatabase setSyncDelayInSeconds:]
+ -[HMFKeyValueDatabase setSyncTimer:]
+ -[HMFKeyValueDatabase setValue:forKey:error:]
+ -[HMFKeyValueDatabase sync:]
+ -[HMFKeyValueDatabase syncDelayInSeconds]
+ -[HMFKeyValueDatabase syncTimer]
+ -[HMFKeyValueDatabase valueForKey:error:]
+ -[HMFKeyValueDatabase values]
+ -[NSData(FastEncoding) hmf_containsObject:forSetAtOffset:]
+ -[NSData(FastEncoding) hmf_enumerateObjectsForSetAtOffset:usingBlock:]
+ -[NSData(FastEncoding) hmf_keysForDictionaryAtOffset:]
+ -[NSData(FastEncoding) hmf_keysForDictionary]
+ -[NSData(FastEncoding) hmf_member:forSetAtOffset:]
+ -[NSData(FastEncoding) hmf_objectAtIndex:]
+ -[NSData(FastEncoding) hmf_objectForKey:]
+ -[NSData(FastEncoding) hmf_readObject]
+ -[NSData(FastEncoding) hmf_readSetAtOffset:]
+ -[NSData(FastEncoding) hmf_valuesForDictionaryAtOffset:]
+ -[NSData(FastEncoding) hmf_valuesForDictionary]
+ -[NSData(MemoryMapping) hmf_copyAsMemoryMappedData]
+ -[NSDictionary(HMFoundation) hmf_copyAsMemoryMappedData]
+ -[NSMutableData(FastEncoding) hmf_appendSet:]
+ _HMFKeyValueDatabaseErrorDomain
+ _HMFProductInfoCharismaBOSVersion
+ _HMFProductInfoCheerBOSVersion
+ _HMFProductInfoDiscoveryBOSVersion
+ _HMFProductInfoLuckBOSVersion
+ _HMFProductInfoNapiliBOSVersion
+ _OBJC_CLASS_$_HMFKeyValueDatabase
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_IVAR_$_HMFMemoryMonitor._lock
+ _OBJC_METACLASS_$_HMFKeyValueDatabase
+ __OBJC_$_CLASS_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|MemoryMapping|HMFTimeZoneCreation)
+ __OBJC_$_INSTANCE_METHODS_HMFKeyValueDatabase
+ __OBJC_$_INSTANCE_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|MemoryMapping|HMFTimeZoneCreation)
+ __OBJC_$_INSTANCE_VARIABLES_HMFKeyValueDatabase
+ __OBJC_$_PROP_LIST_HMFKeyValueDatabase
+ __OBJC_CLASS_PROTOCOLS_$_HMFKeyValueDatabase
+ __OBJC_CLASS_PROTOCOLS_$_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|MemoryMapping|HMFTimeZoneCreation)
+ __OBJC_CLASS_RO_$_HMFKeyValueDatabase
+ __OBJC_METACLASS_RO_$_HMFKeyValueDatabase
+ ___27-[HMFKeyValueDatabase keys]_block_invoke
+ ___28-[HMFKeyValueDatabase sync:]_block_invoke
+ ___29-[HMFKeyValueDatabase values]_block_invoke
+ ___30-[HMFKeyValueDatabase dealloc]_block_invoke
+ ___33-[HMFKeyValueDatabase dictionary]_block_invoke
+ ___41-[HMFKeyValueDatabase valueForKey:error:]_block_invoke
+ ___45-[HMFKeyValueDatabase setValue:forKey:error:]_block_invoke
+ ___45-[NSMutableData(FastEncoding) hmf_appendSet:]_block_invoke
+ ___45-[NSMutableData(FastEncoding) hmf_appendSet:]_block_invoke_2
+ ___49-[HMFKeyValueDatabase removeAllEntriesWithError:]_block_invoke
+ ___53-[HMFKeyValueDatabase _startDelayedSyncTimerIfNeeded]_block_invoke
+ ___53-[HMFKeyValueDatabase _startDelayedSyncTimerIfNeeded]_block_invoke_2
+ ___53-[HMFKeyValueDatabase _startDelayedSyncTimerIfNeeded]_block_invoke_3
+ ___53-[HMFKeyValueDatabase _startDelayedSyncTimerIfNeeded]_block_invoke_4
+ ___58-[NSData(FastEncoding) hmf_containsObject:forSetAtOffset:]_block_invoke
+ ___59-[HMFKeyValueDatabase memoryMonitor:didReceiveMemoryEvent:]_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e15_i24?0r^v8r^v16ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.136
+ _dispatch_sync
+ _kHMFKeyValueDatabaseQueueSpecificKey
+ _objc_msgSend$_cancelSyncTimer
+ _objc_msgSend$_startDelayedSyncTimerIfNeeded
+ _objc_msgSend$_syncWithoutTimerHandling:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$diskRepresentation
+ _objc_msgSend$hmf_appendSet:
+ _objc_msgSend$hmf_containsObject:forSetAtOffset:
+ _objc_msgSend$hmf_copyAsMemoryMappedData
+ _objc_msgSend$hmf_keysForDictionary
+ _objc_msgSend$hmf_keysForDictionaryAtOffset:
+ _objc_msgSend$hmf_objectAtIndex:forArrayAtOffset:
+ _objc_msgSend$hmf_objectForKey:
+ _objc_msgSend$hmf_objectForKey:forDictionaryAtOffset:
+ _objc_msgSend$hmf_readObject
+ _objc_msgSend$hmf_readSetAtOffset:
+ _objc_msgSend$hmf_valuesForDictionaryAtOffset:
+ _objc_msgSend$inMemoryDictionary
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$setDiskRepresentation:
+ _objc_msgSend$setInMemoryDictionary:
+ _objc_msgSend$setSyncTimer:
+ _objc_msgSend$syncDelayInSeconds
+ _objc_msgSend$syncTimer
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$valueForKey:error:
+ _objc_msgSend$writeToURL:options:error:
- +[HMFMessageFilter canInitWithMessage:]
- +[HMFMessageFilter policyClasses]
- -[HMFMemoryMonitor lastProcessMemoryStateUpdateTime]
- -[HMFMemoryMonitor lastProcessMemoryState]
- -[HMFMemoryMonitor setLastProcessMemoryState:]
- -[HMFMemoryMonitor setLastProcessMemoryStateUpdateTime:]
- -[HMFMemoryMonitor setSystemMemoryState:]
- -[HMFMemoryMonitor systemMemoryState]
- -[HMFMessageFilter .cxx_destruct]
- -[HMFMessageFilter acceptWithPolicies:error:]
- -[HMFMessageFilter attributeDescriptions]
- -[HMFMessageFilter initWithMessage:]
- -[HMFMessageFilter init]
- -[HMFMessageFilter logIdentifier]
- -[HMFMessageFilter message]
- _HMFMemoryMonitorProcessMemoryPressureNotification
- _HMFMemoryMonitorSystemMemoryStateDidChangeNotification
- _HMFProcessMemoryStateToString
- _HMFProcessMemoryStateUpdateKey
- _HMFSystemMemoryStateToString
- _HMFSystemMemoryStateUpdateKey
- _OBJC_IVAR_$_HMFMessageFilter._message
- __OBJC_$_CLASS_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|HMFTimeZoneCreation)
- __OBJC_$_CLASS_PROP_LIST_HMFMessageFilter
- __OBJC_$_INSTANCE_METHODS_HMFMessageFilter
- __OBJC_$_INSTANCE_METHODS_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|HMFTimeZoneCreation)
- __OBJC_$_INSTANCE_VARIABLES_HMFMessageFilter
- __OBJC_CLASS_PROTOCOLS_$_NSData(HMFCalendarCreation|HMFZeroing|HMFoundation|FastEncoding|HMFTimeZoneCreation)
- _objc_msgSend$acceptWithPolicies:error:
- _objc_msgSend$canInitWithMessage:
- _objc_msgSend$initWithMessage:
- _objc_msgSend$lastProcessMemoryState
- _objc_msgSend$lastProcessMemoryStateUpdateTime
- _objc_msgSend$policyClasses
- _objc_msgSend$requiredPolicyOfClass:fromPolicies:error:
CStrings:
+ "%{public}@[NSData] dataWithContentsOfURL failed with error: %@"
+ "%{public}@[NSData] removeItemAtURL failed with error: %@"
+ "%{public}@[NSData] writeToURL failed with error: %@"
+ "@\"NSTimer\""
+ "B28@0:8@16I24"
+ "B40@0:8@16@24^@32"
+ "Failed to create memory-mapped data"
+ "HMFKeyValueDatabase"
+ "HMFKeyValueDatabaseErrorDomain"
+ "MemoryMapping"
+ "Must be called on database serial queue"
+ "T@\"NSData\",&,N,V_diskRepresentation"
+ "T@\"NSMutableDictionary\",&,N,V_inMemoryDictionary"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSTimer\",&,N,V_syncTimer"
+ "Td,N,V_syncDelayInSeconds"
+ "Unexpected object type %@ in hmf_appendObject"
+ "_cancelSyncTimer"
+ "_diskRepresentation"
+ "_inMemoryDictionary"
+ "_startDelayedSyncTimerIfNeeded"
+ "_syncDelayInSeconds"
+ "_syncTimer"
+ "_syncWithoutTimerHandling:"
+ "addEntriesFromDictionary:"
+ "com.apple.HMFoundation.HMFKeyValueDatabase"
+ "containsKey:"
+ "dataWithContentsOfURL:options:error:"
+ "diskRepresentation"
+ "hmf_appendSet:"
+ "hmf_containsObject:forSetAtOffset:"
+ "hmf_copyAsMemoryMappedData"
+ "hmf_enumerateObjectsForSetAtOffset:usingBlock:"
+ "hmf_keysForDictionary"
+ "hmf_keysForDictionaryAtOffset:"
+ "hmf_member:forSetAtOffset:"
+ "hmf_objectAtIndex:"
+ "hmf_objectForKey:"
+ "hmf_readObject"
+ "hmf_readSetAtOffset:"
+ "hmf_valuesForDictionary"
+ "hmf_valuesForDictionaryAtOffset:"
+ "inMemoryDictionary"
+ "keys"
+ "removeAllEntriesWithError:"
+ "removeItemAtURL:error:"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "setDiskRepresentation:"
+ "setInMemoryDictionary:"
+ "setSyncDelayInSeconds:"
+ "setSyncTimer:"
+ "setValue:forKey:error:"
+ "sync:"
+ "syncDelayInSeconds"
+ "syncTimer"
+ "temporaryDirectory"
+ "v16@?0@\"NSTimer\"8"
+ "v28@0:8I16@?20"
+ "valueForKey:error:"
+ "values"
+ "writeToURL:options:error:"
- "%{public}@Message is not supported: %@"
- "4"
- "@\"HMFMessage\""
- "HMFMemoryMonitorProcessMemoryPressureNotification"
- "HMFMemoryMonitorSystemMemoryStateDidChangeNotification"
- "HMFProcessMemoryStateCritical"
- "HMFProcessMemoryStateUndefined"
- "HMFProcessMemoryStateUnknown"
- "HMFProcessMemoryStateUpdateKey"
- "HMFProcessMemoryStateWarning"
- "HMFSystemMemoryStateCritical"
- "HMFSystemMemoryStateNormal"
- "HMFSystemMemoryStateUndefined"
- "HMFSystemMemoryStateUnknown"
- "HMFSystemMemoryStateUpdateKey"
- "HMFSystemMemoryStateWarning"
- "Message"
- "T@\"HMFMessage\",R,C,V_message"
- "T@\"NSDate\",&,N,V_lastProcessMemoryStateUpdateTime"
- "Tq,N,V_lastProcessMemoryState"
- "Tq,N,V_systemMemoryState"
- "_lastProcessMemoryState"
- "_lastProcessMemoryStateUpdateTime"
- "_systemMemoryState"
- "acceptWithPolicies:error:"
- "canInitWithMessage:"
- "initWithMessage:"
- "lastProcessMemoryState"
- "lastProcessMemoryStateUpdateTime"
- "policyClasses"
- "setLastProcessMemoryState:"
- "setLastProcessMemoryStateUpdateTime:"
- "setSystemMemoryState:"
- "systemMemoryState"

```
