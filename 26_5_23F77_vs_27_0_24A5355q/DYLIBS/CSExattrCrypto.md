## CSExattrCrypto

> `/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x8870
-  __TEXT.__auth_stubs: 0x9b0
+2444.104.0.0.0
+  __TEXT.__text: 0x8884
   __TEXT.__objc_methlist: 0x328
-  __TEXT.__const: 0xd8
+  __TEXT.__const: 0xd0
   __TEXT.__cstring: 0xa5c
   __TEXT.__oslogstring: 0x19f
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methname: 0xcd8
-  __TEXT.__objc_methtype: 0x4b8
-  __TEXT.__objc_stubs: 0xe20
-  __DATA_CONST.__got: 0x180
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x418
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x500
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0xe0
   __DATA.__bss: 0xb0

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF5EA42A-DA5E-3408-B7E6-9297A5483A57
+  UUID: E39BA7CD-2BA5-3CE2-876C-E6F1B90DEA04
   Functions: 159
-  Symbols:   788
-  CStrings:  378
+  Symbols:   791
+  CStrings:  190
 
Symbols:
+ _fstat
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ __MDItemSetPrivateAttributesForURL : 556 -> 544
~ ____MDItemSetPrivateAttributesForURL_block_invoke_2 : 452 -> 456
~ _copyConnection : 220 -> 208
~ __MDItemDecrypt : 416 -> 412
~ __MDItemFetchPrivateAttributesForURL : 364 -> 356
~ _MDFSOnlyMDCopyXattrsDictionaryForFD : 2104 -> 2112
~ _MDFSOnlyMDCopyXattrsDictionary : 100 -> 180
~ -[MDKeyRing createRandomUUID] : 132 -> 136
~ -[MDKeyRing createRandomAESKey] : 136 -> 140
~ __MDLabelUUIDEncode : 428 -> 516
~ -[MDPrivateXattrServices extractDecryptedDataWith:cryptoCallback:decryptableXids:intoDict:keyRing:xid:] : 1652 -> 1656
~ -[MDPrivateXattrServices copyPrivateXattrsFromData:decryptedXids:] : 884 -> 888
~ _copyUpdatedData : 3680 -> 3704
~ -[MDPrivateXattrServices xidDictWithUUIDs:allKeyUUIDs:] : 480 -> 484
~ -[MDPrivateXattrServices xidDictWithXPCUUIDs:allKeyUUIDs:] : 392 -> 396
~ ___107-[MDPrivateXattrServices updatePrivateXattrParams:flags:forFileDescriptor:mergeCallback:completionHandler:]_block_invoke_2 : 600 -> 604
~ ___message_assert : 192 -> 152
~ _serializeCFType : 1356 -> 1360
~ _copyCFTypeFromBuffer : 960 -> 952
~ ____MDItemSetPrivateAttributesForURL_block_invoke_3.cold.1 : 116 -> 72
~ __copyCryptedDataWithKey.cold.1 : 128 -> 84
~ -[_MDLabel initWithUUID:attributes:forUserUUID:].cold.1 : 148 -> 104
CStrings:
- "(?=\"\"{?=\"isMutuallyExclusiveSetMember\"b1\"isPublicVisibility\"b1\"hasPreviewIcon\"b1\"hasFinderColor\"b1\"setFinderColor\"b3\"hasExtendedFinderColor\"b1\"reservedBits1\"b8\"reservedBits2\"b16\"reservedBits3\"b32}\"payload\"q)"
- "@\"<MDKeyRing>\"16@0:8"
- "@\"NSArray\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8r^^{__CFString}16"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@40@0:8@16@24I32I36"
- "@40@0:8^{__CFUUID=}16^{__CFDictionary=}24^{__CFUUID=}32"
- "@64@0:8@?16@24@32@40@48@56"
- "@72@0:8@?16@24@32@40@48@56^@64"
- "B24@0:8@16"
- "CSExattrCryptoServiceProtocol"
- "MDKeyRing"
- "MDPrivateXattrServices"
- "MDUUIDData"
- "MDXATTR"
- "Q16@0:8"
- "T@\"NSMutableDictionary\",&,N,V_keysByUUID"
- "UTF8String"
- "UUIDString"
- "^v16@0:8"
- "^v24@0:8^{__CFString=}16"
- "^{__CFDictionary=}"
- "^{__CFUUID=}"
- "^{__CFUUID=}16@0:8"
- "^{__CFUUID=}32@0:8@16@24"
- "^{__SecKey=}24@0:8@16"
- "_MDLabel"
- "_attrBits"
- "_attrs"
- "_cfTypeID"
- "_copyXattrUpdatesKey"
- "_createKeyUUIDWithAccount:password:"
- "_designatedKeyUUID"
- "_getUUIDBytesForUserUUID:"
- "_keysByUUID"
- "_queue"
- "_restoreAttributesFromDictionary:intoDictionary:"
- "_restoreAttributesFromPlistBytes:intoDictionary:"
- "_userUUID"
- "_uuid"
- "addEntriesFromDictionary:"
- "addObject:"
- "allKeyUUIDs"
- "allKeys"
- "allObjects"
- "allValues"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "bytes"
- "calendarWithIdentifier:"
- "cleanAttrs"
- "compare:"
- "components:fromDate:"
- "computeUpdatedCryptoData:newParams:isPrivateMDAttributes:doMergeArrayValues:replyBlock:"
- "containsObject:"
- "copy"
- "copyDecryptedData:withKeyUUID:iv1:iv2:"
- "copyDesignatedKeyUUID"
- "copyEncryptedData:withKeyUUID:iv1:iv2:"
- "copyPrivateKeyQuery:"
- "copyPrivateXattrsDictionary:cryptoCallback:"
- "copyPrivateXattrsFromData:"
- "copyPrivateXattrsFromData:decryptedXids:"
- "copyRandomPassword"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createKeychainItemForKey:"
- "createRandomAESKey"
- "createRandomUUID"
- "dataWithBytes:length:"
- "date"
- "dateFromComponents:"
- "dealloc"
- "decryptAttributesWithData:withReply:"
- "decryptDataArrayWithCryptoCallback:dataArray:existingXIDArray:uuids:xpc_uuids:xids:"
- "decryptDataArrayWithCryptoCallback:dataArray:existingXIDArray:uuids:xpc_uuids:xids:decrypted:"
- "defaultKeyRing"
- "defaultServices"
- "description"
- "dictionary"
- "dictionaryToSecItemFormat:"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "digestUUIDBytesWithKey:forUUID:uuidBytes:"
- "digestUUIDBytesWithKey:forXPCUUID:uuidBytes:"
- "distantPast"
- "enumerateObjectsAtIndexes:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "extractDecryptedDataWith:cryptoCallback:decryptableXids:intoDict:keyRing:xid:"
- "fetchKeyFromKeychain:"
- "getAttr:"
- "getAttrFallback:"
- "getKey:"
- "getObjects:range:"
- "getUUIDBytes:"
- "hasPrefix:"
- "hash"
- "i24@0:8@16"
- "indexOfObject:"
- "indexesOfObjectsPassingTest:"
- "init"
- "initWithArray:"
- "initWithBytes:length:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCString:encoding:"
- "initWithCapacity:"
- "initWithData:encoding:"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithObjects:"
- "initWithObjects:count:"
- "initWithObjects:forKeys:"
- "initWithObjectsAndKeys:"
- "initWithServiceName:"
- "initWithUUID:attributes:forUserUUID:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "initialize"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "keysByUUID"
- "lastObject"
- "length"
- "mutableCopy"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "restoreFromExistingKey:"
- "resume"
- "reverseObjectEnumerator"
- "scheduleAccessToKey:onQueue:usingBlock:"
- "secItemFormatToDictionary:"
- "set"
- "setKeysByUUID:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setValue:forKey:"
- "sortUsingComparator:"
- "stringByAppendingFormat:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "timeIntervalSinceDate:"
- "unarchivedObjectOfClasses:fromData:error:"
- "updateAttrs:"
- "updatePrivateXattrParams:flags:forFileDescriptor:"
- "updatePrivateXattrParams:flags:forFileDescriptor:completionHandler:"
- "updatePrivateXattrParams:flags:forFileDescriptor:mergeCallback:completionHandler:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8^{__CFDictionary=}16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\"@\"NSArray\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@16Q24i32"
- "v40@0:8@16@24[16C]32"
- "v40@0:8^{__CFUUID=}16@\"NSObject<OS_dispatch_queue>\"24@?<v@?^{__SecKey=}>32"
- "v40@0:8^{__CFUUID=}16@24@?32"
- "v44@0:8@16Q24i32@?36"
- "v48@0:8@\"NSData\"16@\"NSDictionary\"24B32B36@?<v@?@\"NSError\"@\"NSString\"@\"NSData\"@\"NSArray\">40"
- "v48@0:8@16@24B32B36@?40"
- "v52@0:8@16Q24i32@?36@?44"
- "v64@0:8@16@?24@32@40@48@56"
- "writeToKeychain:"
- "xidDictWithUUIDs:allKeyUUIDs:"
- "xidDictWithUUIDs:fromKeyRing:"
- "xidDictWithXPCUUIDs:allKeyUUIDs:"
- "{?=CCCCCCCCCCCCCCCC}24@0:8^{__CFUUID=}16"

```
