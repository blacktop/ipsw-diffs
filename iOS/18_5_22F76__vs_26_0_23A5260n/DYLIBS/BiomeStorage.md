## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage`

```diff

-166.23.1.0.0
-  __TEXT.__text: 0x29a74
+192.0.0.0.0
+  __TEXT.__text: 0x2a7ec
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x1fb4
-  __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x1613
+  __TEXT.__objc_methlist: 0x2054
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x165b
   __TEXT.__oslogstring: 0x42ea
-  __TEXT.__gcc_except_tab: 0x998
+  __TEXT.__gcc_except_tab: 0xa04
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0xa78
-  __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methname: 0x5117
-  __TEXT.__objc_methtype: 0x121d
-  __TEXT.__objc_stubs: 0x3c60
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x6c0
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__objc_classname: 0x328
+  __TEXT.__objc_methname: 0x52bd
+  __TEXT.__objc_methtype: 0x1259
+  __TEXT.__objc_stubs: 0x3e60
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12b0
+  __DATA_CONST.__objc_selrefs: 0x1330
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc0
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x14c0
-  __AUTH_CONST.__objc_const: 0x4b80
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x4ca8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x294
-  __DATA.__data: 0x4e0
-  __DATA.__bss: 0x218
+  __DATA.__objc_ivar: 0x298
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0190E501-1483-3637-B479-ABF0FEE0A19A
-  Functions: 969
-  Symbols:   3328
-  CStrings:  1686
+  UUID: 3B3CA13F-769D-31C8-91C1-222E0BE7C83F
+  Functions: 980
+  Symbols:   3361
+  CStrings:  1718
 
Symbols:
+ -[BMSegmentManager cacheFileDescriptorsIfNecessary:]
+ -[BMSegmentManager cacheFileDescriptorsIfNecessary:].cold.1
+ -[BMSegmentManager removeSegmentNamed:reason:direction:]
+ -[BMSegmentManager removeSegmentNamed:reason:direction:].cold.1
+ -[BMStoreConfig _initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:currentDevice:]
+ -[BMStoreConfig _initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:currentDevice:].cold.1
+ -[BMStoreConfig currentDevice]
+ -[BMStreamDatastore pruneStreamToMaxCount:]
+ -[BMStreamDatastore pruneStreamToMaxCount:].cold.1
+ -[BMStreamDatastore segmentManager:willDeleteSegmentName:frameStore:reason:direction:]
+ GCC_except_table100
+ GCC_except_table19
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table76
+ GCC_except_table78
+ _BMPruningPolicyDescribeMaxAge
+ _BMPruningPolicyDescribeMaxEventCount
+ _BMPruningPolicyDescribeMaxStreamSize
+ _OBJC_CLASS_$_BMCurrentDevice
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSDateComponentsFormatter
+ _OBJC_IVAR_$_BMStoreConfig._currentDevice
+ __OBJC_$_PROP_LIST_BMStoreEvent.176
+ __OBJC_$_PROP_LIST_BMTombstoneEvent.159
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMTombstoneEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMTombstoneEvent
+ __OBJC_$_PROTOCOL_REFS_BMTombstoneEvent
+ __OBJC_LABEL_PROTOCOL_$_BMTombstoneEvent
+ __OBJC_PROTOCOL_$_BMTombstoneEvent
+ ___30-[BMStoreEvent initWithCoder:]_block_invoke.40
+ ___43-[BMStreamDatastore pruneStreamToMaxCount:]_block_invoke
+ ___43-[BMStreamDatastore pruneStreamToMaxCount:]_block_invoke_2
+ ___56-[BMSegmentManager removeSegmentNamed:reason:direction:]_block_invoke
+ ___56-[BMSegmentManager removeSegmentNamed:reason:direction:]_block_invoke.62
+ ___86-[BMStreamDatastore segmentManager:willDeleteSegmentName:frameStore:reason:direction:]_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64s72r80r88r_e21_v24?0"BMFrame"8^B16lr72l8r80l8r88l8s32l8s40l8u104l8s48l8s56l8s64l8
+ ___block_descriptor_48_e8_32s_e40_v16?0"BMSegmentManagerProtectedState"8ls32l8
+ ___block_descriptor_81_e8_32s40s48s56s_e21_v24?0"BMFrame"8^B16ls32l8s40l8u64l8s48l8s56l8
+ ___block_descriptor_98_e8_32s40s48s56s64r72r_e39_v32?0"BMFrameStore"8"NSString"16^B24lr64l8r72l8s32l8s40l8u88l8s48l8s56l8
+ _initWithCoder:.onceToken.39
+ _objc_msgSend$_initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:currentDevice:
+ _objc_msgSend$_setError
+ _objc_msgSend$cacheFileDescriptorsIfNecessary:
+ _objc_msgSend$connectionToAccessServerInDomain:user:useCase:options:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$isDeviceUnlocked
+ _objc_msgSend$orderedSetWithObject:
+ _objc_msgSend$position
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeSegmentNamed:reason:direction:
+ _objc_msgSend$reverseEnumerateSegmentsFrom:to:withBlock:
+ _objc_msgSend$segmentManager:willDeleteSegmentName:frameStore:reason:direction:
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setUnitsStyle:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$stringFromByteCount:countStyle:
+ _objc_msgSend$stringFromTimeInterval:
- -[BMSegmentManager removeSegmentNamed:].cold.1
- -[BMStoreConfig _initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:]
- -[BMStoreConfig _initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:].cold.1
- -[BMStreamDatastore segmentManager:willDeleteSegmentName:frameStore:]
- GCC_except_table20
- GCC_except_table22
- GCC_except_table54
- GCC_except_table75
- GCC_except_table98
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _BMTombstoneSegmentMaxStreamSize
- __OBJC_$_PROP_LIST_BMStoreEvent.173
- ___30-[BMStoreEvent initWithCoder:]_block_invoke.41
- ___39-[BMSegmentManager removeSegmentNamed:]_block_invoke
- ___39-[BMSegmentManager removeSegmentNamed:]_block_invoke.62
- ___69-[BMStreamDatastore segmentManager:willDeleteSegmentName:frameStore:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e21_v24?0"BMFrame"8^B16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e40_v16?0"BMSegmentManagerProtectedState"8ls32l8s40l8
- _initWithCoder:.onceToken.40
- _objc_msgSend$_initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:
- _objc_msgSend$connectionToAccessServerInDomain:user:useCase:
- _objc_msgSend$isUnlocked
- _objc_msgSend$segmentManager:willDeleteSegmentName:frameStore:
CStrings:
+ "3A `"
+ "3`"
+ "4B `"
+ "@\"BMCurrentDevice\""
+ "@\"BMStoreBookmark\"16@0:8"
+ "@120@0:8Q16@24Q32Q40q48@56@64@72Q80Q88I96B100@104@112"
+ "BMStreamDatastore not configured for pruning"
+ "MaxCount"
+ "MaxSize"
+ "T@\"BMCurrentDevice\",R,N,V_currentDevice"
+ "TQ,R,N"
+ "_currentDevice"
+ "_initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:currentDevice:"
+ "_setError"
+ "cacheFileDescriptorsIfNecessary:"
+ "connectionToAccessServerInDomain:user:useCase:options:"
+ "currentDevice"
+ "getBytes:range:"
+ "hasError"
+ "isDeviceUnlocked"
+ "orderedSetWithObject:"
+ "position"
+ "pruneStreamToMaxCount:"
+ "removeAllObjects"
+ "removeSegmentNamed:reason:direction:"
+ "segmentManager:willDeleteSegmentName:frameStore:reason:direction:"
+ "setByAddingObjectsFromSet:"
+ "setPosition:"
+ "setUnitsStyle:"
+ "setWithArray:"
+ "stringFromByteCount:countStyle:"
+ "stringFromTimeInterval:"
+ "unlimited"
+ "v56@0:8@\"BMSegmentManager\"16@\"NSString\"24@\"BMFrameStore\"32Q40Q48"
+ "v56@0:8@16@24@32Q40Q48"
- "@112@0:8Q16@24Q32Q40q48@56@64@72Q80Q88I96B100@104"
- "_initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:user:isManaged:streamIdentifier:"
- "connectionToAccessServerInDomain:user:useCase:"
- "isUnlocked"
- "segmentManager:willDeleteSegmentName:frameStore:"
- "v40@0:8@\"BMSegmentManager\"16@\"NSString\"24@\"BMFrameStore\"32"
- "v40@0:8@16@24@32"

```
