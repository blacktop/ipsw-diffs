## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage`

```diff

-123.2.8.0.0
-  __TEXT.__text: 0x24d24
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x1c3c
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x13c4
-  __TEXT.__oslogstring: 0x34e9
-  __TEXT.__gcc_except_tab: 0x6a8
+123.5.23.1.0
+  __TEXT.__text: 0x24ca4
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x1c04
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x13d7
+  __TEXT.__oslogstring: 0x3507
+  __TEXT.__gcc_except_tab: 0x6b4
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0xa00
-  __TEXT.__objc_classname: 0x390
-  __TEXT.__objc_methname: 0x4c59
-  __TEXT.__objc_methtype: 0x113a
-  __TEXT.__objc_stubs: 0x39c0
+  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__objc_classname: 0x386
+  __TEXT.__objc_methname: 0x4b23
+  __TEXT.__objc_methtype: 0x1133
+  __TEXT.__objc_stubs: 0x3940
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4120
-  __DATA_CONST.__objc_selrefs: 0x1138
-  __AUTH_CONST.__cfstring: 0x1140
-  __AUTH_CONST.__objc_const: 0xb30
+  __DATA_CONST.__objc_const: 0x4128
+  __DATA_CONST.__objc_selrefs: 0x1118
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__objc_const: 0xaa0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x3a8
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1a8
-  __DATA.__objc_superrefs: 0xc0
+  __AUTH_CONST.__auth_got: 0x3a0
   __DATA.__objc_ivar: 0x238
-  __DATA.__data: 0x560
-  __DATA.__bss: 0x1a0
-  __DATA_DIRTY.__objc_data: 0x8c0
+  __DATA.__data: 0x568
+  __DATA.__bss: 0x198
+  __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D1A07B7F-59E6-33E0-8E33-A1240AAFD274
-  Functions: 917
-  Symbols:   3082
-  CStrings:  1539
+  UUID: D8A81B16-05F9-32C3-9A5D-CC2F2AB27966
+  Functions: 914
+  Symbols:   3065
+  CStrings:  1543
 
Symbols:
+ +[BMStoreConfig _streamTypeFromStorePath:domain:]
+ -[BMStoreConfig _initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:isManaged:streamIdentifier:]
+ -[BMStoreConfig account]
+ -[BMStoreConfig copyWithRemoteName:]
+ -[BMStoreConfig remoteName]
+ -[BMStoreConfig setAccount:]
+ -[BMStoreConfig setRemoteName:]
+ -[BMStoreEvent eventBodyKeepingBackingData:]
+ -[BMStoreEvent eventBodyKeepingBackingData:].cold.1
+ -[BMStoreEvent eventBodyKeepingBackingData:].cold.2
+ -[BMStoreEvent eventBodyKeepingBackingData:].cold.3
+ -[BMStoreEvent eventBodyKeepingBackingData:].cold.4
+ -[BMStreamMetadata account]
+ -[BMStreamMetadata initWithStreamId:eventType:account:remoteStreamName:pruningPolicy:]
+ -[BMStreamMetadata setAccount:]
+ GCC_except_table1
+ GCC_except_table9
+ _OBJC_CLASS_$_BMAccount
+ _OBJC_IVAR_$_BMStoreConfig._account
+ _OBJC_IVAR_$_BMStoreConfig._remoteName
+ _OBJC_IVAR_$_BMStreamMetadata._account
+ __OBJC_$_PROP_LIST_BMStoreEvent.172
+ ___31-[BMWriteService newConnection]_block_invoke.12
+ ___block_descriptor_56_e8_32s40r_e40_v16?0"BMSegmentManagerProtectedState"8lr40l8s32l8
+ _objc_msgSend$_initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:isManaged:streamIdentifier:
+ _objc_msgSend$_streamTypeFromStorePath:domain:
+ _objc_msgSend$account
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$eventBodyKeepingBackingData:
+ _objc_msgSend$initWithStreamId:eventType:account:remoteStreamName:pruningPolicy:
+ _objc_msgSend$remoteName
+ _objc_msgSend$setAccount:
- +[BMStoreConfig newSharedSyncRestrictedStreamWithCurrentAccountSegmentSize:protectionClass:domain:]
- +[BMStoreConfig newSharedSyncRestrictedStreamWithUserIdentifier:segmentSize:protectionClass:domain:]
- +[BMWeakProxy weakProxyToObject:]
- -[BMStoreConfig copyStoreConfigWithOption:account:remoteStreamName:]
- -[BMStoreConfig copyStoreConfigWithOption:remoteStreamName:]
- -[BMStoreConfig initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:remoteStreamName:pruningPolicy:]
- -[BMStoreConfig initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:remoteStreamName:pruningPolicy:streamType:domain:isManaged:streamIdentifier:]
- -[BMStoreConfig remoteStreamName]
- -[BMStoreConfig setRemoteStreamName:]
- -[BMStoreEvent eventBody].cold.1
- -[BMStoreEvent eventBody].cold.2
- -[BMStoreEvent eventBody].cold.3
- -[BMStoreEvent eventBody].cold.4
- -[BMStreamDatastoreBase remoteStreamName]
- -[BMStreamMetadata isEqualStreamMetadata:]
- -[BMWeakProxy .cxx_destruct]
- -[BMWeakProxy forwardingTargetForSelector:]
- GCC_except_table11
- GCC_except_table4
- _OBJC_CLASS_$_NSProxy
- _OBJC_IVAR_$_BMStoreConfig._remoteStreamName
- _OBJC_IVAR_$_BMStreamDatastoreBase._remoteStreamName
- _OBJC_IVAR_$_BMWeakProxy._target
- _OBJC_METACLASS_$_BMWeakProxy
- _OBJC_METACLASS_$_NSProxy
- __OBJC_$_CLASS_METHODS_BMWeakProxy
- __OBJC_$_INSTANCE_METHODS_BMWeakProxy
- __OBJC_$_INSTANCE_VARIABLES_BMWeakProxy
- __OBJC_$_PROP_LIST_BMStoreEvent.169
- __OBJC_CLASS_RO_$_BMWeakProxy
- __OBJC_METACLASS_RO_$_BMWeakProxy
- __PASIsAllDigits
- ___31-[BMWriteService newConnection]_block_invoke.23
- _objc_msgSend$biomeAccountIdentifier
- _objc_msgSend$initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:remoteStreamName:pruningPolicy:
- _objc_msgSend$initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:remoteStreamName:pruningPolicy:streamType:domain:isManaged:streamIdentifier:
- _objc_msgSend$initWithStreamId:eventType:remoteStreamName:pruningPolicy:
- _objc_msgSend$isEqualStreamMetadata:
- _objc_msgSend$isTestPathOverridden
- _objc_msgSend$numberWithLongLong:
- _objc_msgSend$pathForSharedCurrentAccountStreamType:domain:
- _objc_msgSend$pathForSharedSyncUserIdentifier:streamType:domain:
- _objc_msgSend$pathIsManaged:domain:
- _objc_msgSend$remoteStreamName
- _objc_msgSend$streamTypeFromStorePath:
CStrings:
+ "\x01#!\x11\x11"
+ "\x02A\""
+ "\x05"
+ "@\"BMAccount\""
+ "@108@0:8Q16@24Q32Q40q48@56@64@72Q80Q88B96@100"
+ "@56@0:8@16#24@32@40@48"
+ "Q32@0:8@16^Q24"
+ "T@\"BMAccount\",&,N,V_account"
+ "T@\"BMAccount\",C,N,V_account"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_remoteName"
+ "Unable to lastFrameStoreOrCreateWithTimestamp and   creation also failed for %@"
+ "_account"
+ "_initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:account:remoteName:pruningPolicy:streamType:domain:isManaged:streamIdentifier:"
+ "_remoteName"
+ "_segmentAfterFrameStore: %@"
+ "_streamTypeFromStorePath:domain:"
+ "account"
+ "characterAtIndex:"
+ "copyWithRemoteName:"
+ "eventBodyKeepingBackingData:"
+ "initWithStreamId:eventType:account:remoteStreamName:pruningPolicy:"
+ "remoteName"
+ "setAccount:"
+ "setRemoteName:"
+ "\xb1"
- "\x01$!\x11\x11"
- "\x02A!"
- "@"
- "@100@0:8Q16@24Q32Q40q48@56@64Q72Q80B88@92"
- "@32@0:8q16@24"
- "@40@0:8q16@24@32"
- "@72@0:8Q16@24Q32Q40q48@56@64"
- "BMWeakProxy"
- "T@\"NSString\",R,N,V_remoteStreamName"
- "Unable to lastFrameStoreOrCreateWithTimestamp and creation also failed for %@"
- "_target"
- "biomeAccountIdentifier"
- "copyStoreConfigWithOption:account:remoteStreamName:"
- "copyStoreConfigWithOption:remoteStreamName:"
- "forwardingTargetForSelector:"
- "initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:remoteStreamName:pruningPolicy:"
- "initWithStoreVersion:storeBasePath:segmentSize:protectionClass:storeLocationOption:remoteStreamName:pruningPolicy:streamType:domain:isManaged:streamIdentifier:"
- "isEqualStreamMetadata:"
- "isTestPathOverridden"
- "newSharedSyncRestrictedStreamWithCurrentAccountSegmentSize:protectionClass:domain:"
- "newSharedSyncRestrictedStreamWithUserIdentifier:segmentSize:protectionClass:domain:"
- "numberWithLongLong:"
- "pathForSharedCurrentAccountStreamType:domain:"
- "pathForSharedSyncUserIdentifier:streamType:domain:"
- "pathIsManaged:domain:"
- "\xc1"

```
