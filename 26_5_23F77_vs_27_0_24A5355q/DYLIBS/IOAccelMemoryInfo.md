## IOAccelMemoryInfo

> `/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo`

```diff

-487.4.3.0.0
-  __TEXT.__text: 0x5364
-  __TEXT.__auth_stubs: 0x480
+490.0.0.0.0
+  __TEXT.__text: 0x53f8
   __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__cstring: 0xb37
-  __TEXT.__unwind_info: 0x110
-  __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methname: 0x855
-  __TEXT.__objc_methtype: 0xbb
-  __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x920
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x70
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13884741-4FCD-3B36-977A-9D63CFDED01F
-  Functions: 136
-  Symbols:   527
-  CStrings:  358
+  UUID: BE0842EA-6447-3DA2-89BF-1FF9FA7AF1BE
+  Functions: 138
+  Symbols:   534
+  CStrings:  197
 
Symbols:
+ GCC_except_table99
+ __ZNSt3__127__tree_balance_after_insertB9fqe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__13setIiNS_4lessIiEENS_9allocatorIiEEE6insertB9fqe220100ERKi
+ __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIiPvEE
+ __ZSt9terminatev
+ ___clang_call_terminate
+ ___cxa_begin_catch
- __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE25__emplace_unique_key_argsIiJRKiEEENS_4pairINS_15__tree_iteratorIiPNS_11__tree_nodeIiPvEElEEbEERKT_DpOT0_
CStrings:
- "@"
- "@\"NSDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@16"
- "B16@0:8"
- "I16@0:8"
- "IOAccelMemoryInfo"
- "IOAccelMemoryMapInfo"
- "IOAccelMemoryOpenCLInfo"
- "IOAccelMemoryOpenGLInfo"
- "IOAccelMemoryPoolTotals"
- "Q"
- "Q16@0:8"
- "T@\"NSArray\",R"
- "T@\"NSSet\",R"
- "T@\"NSString\",&,Vcl_context"
- "T@\"NSString\",&,VdebugLabel"
- "T@\"NSString\",&,Vdevice_name"
- "T@\"NSString\",&,VobjectDescription"
- "T@\"NSString\",&,VobjectType"
- "T@\"NSString\",&,Vpool"
- "T@\"NSString\",&,Vsharegroup"
- "TB,R"
- "TI,R"
- "TQ,R"
- "TQ,Vaddress"
- "TQ,VallocatedSize"
- "TQ,Vcl_mem"
- "TQ,VdirtySize"
- "TQ,VnonpurgeableSize"
- "TQ,VobjectType"
- "TQ,VorphanedSize"
- "TQ,VpurgeableSize"
- "TQ,VresidentSize"
- "TQ,VwiredSize"
- "Ti,VblamedProcess"
- "Ti,Vname"
- "Ti,Vpid"
- "_expansionData"
- "addObject:"
- "addObjectsFromArray:"
- "address"
- "allObjects"
- "allValues"
- "allocatedSize"
- "anyObject"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "blamedProcess"
- "blamedProcesses"
- "blamedProcessesForProcess:"
- "boolValue"
- "cacheDirty"
- "cachedCopy"
- "cl_context"
- "cl_mem"
- "collectAllocationTotalsWithOptions:queue:completionBlock:"
- "collectDataWithCompletionQueue:completionBlock:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugLabel"
- "description"
- "device_name"
- "devices"
- "dict"
- "dictionaryWithObjects:forKeys:count:"
- "dirtyLength"
- "dirtySize"
- "errorWithDomain:code:userInfo:"
- "formattedDescriptions"
- "i"
- "i16@0:8"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "init"
- "initWithArray:"
- "initWithDictionary:"
- "initWithFormat:"
- "initWithObjects:"
- "intValue"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "length"
- "localizedDescription"
- "mappings"
- "member:"
- "memoryPool"
- "mutableCopy"
- "name"
- "newKernelAllocationList:"
- "newKernelAllocationTotals:totalsReturn:errorReturn:"
- "nonpurgeableSize"
- "numberWithInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectDescription"
- "objectForKey:"
- "objectType"
- "openclObjects"
- "openglObjects"
- "orphaned"
- "orphanedSize"
- "pool"
- "processIDs"
- "purgeAllVidMem"
- "purgeable"
- "purgeableSize"
- "removeObject:"
- "removeObjectAtIndex:"
- "residentLength"
- "residentSize"
- "set"
- "setAddress:"
- "setAllocatedSize:"
- "setBlamedProcess:"
- "setCl_context:"
- "setCl_mem:"
- "setDebugLabel:"
- "setDevice_name:"
- "setDirtySize:"
- "setName:"
- "setNonpurgeableSize:"
- "setObject:forKey:"
- "setObjectDescription:"
- "setObjectType:"
- "setOrphanedSize:"
- "setPid:"
- "setPool:"
- "setPurgeableSize:"
- "setResidentSize:"
- "setSharegroup:"
- "setValue:forKey:"
- "setWiredSize:"
- "sharegroup"
- "string"
- "stringWithFormat:"
- "stringWithString:"
- "surfaceID"
- "unionSet:"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "validateDictionary:"
- "valueForKey:"
- "wired"
- "wiredSize"

```
