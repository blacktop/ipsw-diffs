## libnfstorage.dylib

> `/usr/lib/libnfstorage.dylib`

```diff

-355.4.0.0.0
-  __TEXT.__text: 0x58c0
-  __TEXT.__auth_stubs: 0x2e0
+360.33.0.0.0
+  __TEXT.__text: 0x57dc
+  __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x168
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__const: 0x68
   __TEXT.__cstring: 0x7ea
   __TEXT.__oslogstring: 0x513
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xc0
   __TEXT.__objc_classname: 0xee
   __TEXT.__objc_methname: 0x8af
   __TEXT.__objc_methtype: 0x96

   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x310
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x830
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F1A767B-1D29-30C8-AD60-882A6E72B86B
+  UUID: A60366DC-D892-340C-BC39-1D50E1E1811A
   Functions: 34
-  Symbols:   305
+  Symbols:   101
   CStrings:  258
 
Symbols:
- +[AppletEntity(CoreDataProperties) fetchRequest]
- +[ExpressESEEntity(CoreDataProperties) fetchRequest]
- +[ExpressIcfEntity(CoreDataProperties) fetchRequest]
- +[PurpleTrustAppletEntity(CoreDataProperties) fetchRequest]
- +[PurpleTrustClientEntity(CoreDataProperties) fetchRequest]
- +[PurpleTrustKeyEntity(CoreDataProperties) fetchRequest]
- -[NFStorageController .cxx_destruct]
- -[NFStorageController homePath]
- -[NFStorageController managedObjectContext]
- -[NFStorageController managedObjectModel]
- -[NFStorageControllerApplet _deleteAllAppletEntities]
- -[NFStorageControllerApplet dbProtectionType]
- -[NFStorageControllerApplet deleteAllAppletEntities]
- -[NFStorageControllerApplet fetchAppletEntitiesWithError:]
- -[NFStorageControllerApplet name]
- -[NFStorageControllerApplet updateAppletEntitiesWithConfig:]
- -[NFStorageControllerESEExpress _deleteAllESEExpressEntities]
- -[NFStorageControllerESEExpress dbProtectionType]
- -[NFStorageControllerESEExpress deleteAllESEExpressEntities]
- -[NFStorageControllerESEExpress fetchESEExpressEntitiesWithError:]
- -[NFStorageControllerESEExpress name]
- -[NFStorageControllerESEExpress updateESEExpressEntitiesWithConfig:]
- <redacted>
- GCC_except_table2
- GCC_except_table8
- _OBJC_IVAR_$_NFStorageController._managedObjectContext
- _OBJC_IVAR_$_NFStorageController._managedObjectModel
- _OBJC_IVAR_$_NFStorageController._persistentStoreCoordinator
- __OBJC_$_CLASS_METHODS_AppletEntity(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_ExpressESEEntity(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_ExpressIcfEntity(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_PurpleTrustAppletEntity(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_PurpleTrustClientEntity(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_PurpleTrustKeyEntity(CoreDataProperties)
- __OBJC_$_INSTANCE_METHODS_NFStorageController
- __OBJC_$_INSTANCE_METHODS_NFStorageControllerApplet
- __OBJC_$_INSTANCE_METHODS_NFStorageControllerESEExpress
- __OBJC_$_INSTANCE_VARIABLES_NFStorageController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NFStorageInternalMethods
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFStorageInternalMethods
- __OBJC_CLASS_PROTOCOLS_$_NFStorageController
- __OBJC_CLASS_RO_$_AppletEntity
- __OBJC_CLASS_RO_$_ExpressESEEntity
- __OBJC_CLASS_RO_$_ExpressIcfEntity
- __OBJC_CLASS_RO_$_NFStorageController
- __OBJC_CLASS_RO_$_NFStorageControllerApplet
- __OBJC_CLASS_RO_$_NFStorageControllerESEExpress
- __OBJC_CLASS_RO_$_PurpleTrustAppletEntity
- __OBJC_CLASS_RO_$_PurpleTrustClientEntity
- __OBJC_CLASS_RO_$_PurpleTrustKeyEntity
- __OBJC_LABEL_PROTOCOL_$_NFStorageInternalMethods
- __OBJC_METACLASS_RO_$_AppletEntity
- __OBJC_METACLASS_RO_$_ExpressESEEntity
- __OBJC_METACLASS_RO_$_ExpressIcfEntity
- __OBJC_METACLASS_RO_$_NFStorageController
- __OBJC_METACLASS_RO_$_NFStorageControllerApplet
- __OBJC_METACLASS_RO_$_NFStorageControllerESEExpress
- __OBJC_METACLASS_RO_$_PurpleTrustAppletEntity
- __OBJC_METACLASS_RO_$_PurpleTrustClientEntity
- __OBJC_METACLASS_RO_$_PurpleTrustKeyEntity
- __OBJC_PROTOCOL_$_NFStorageInternalMethods
- __Unwind_Resume
- ___52-[NFStorageControllerApplet deleteAllAppletEntities]_block_invoke
- ___58-[NFStorageControllerApplet fetchAppletEntitiesWithError:]_block_invoke
- ___60-[NFStorageControllerApplet updateAppletEntitiesWithConfig:]_block_invoke
- ___60-[NFStorageControllerApplet updateAppletEntitiesWithConfig:]_block_invoke.168
- ___60-[NFStorageControllerApplet updateAppletEntitiesWithConfig:]_block_invoke.181
- ___60-[NFStorageControllerESEExpress deleteAllESEExpressEntities]_block_invoke
- ___66-[NFStorageControllerESEExpress fetchESEExpressEntitiesWithError:]_block_invoke
- ___68-[NFStorageControllerESEExpress updateESEExpressEntitiesWithConfig:]_block_invoke
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_48_e8_32r_e29_v32?0"NSDictionary"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_80_e8_32s40r48r56r64r_e15_v32?0816^B24ls32l8r40l8r48l8r56l8r64l8
- ___objc_personality_v0
- _objc_msgSend$URLWithString:
- _objc_msgSend$_deleteAllAppletEntities
- _objc_msgSend$_deleteAllESEExpressEntities
- _objc_msgSend$addObject:
- _objc_msgSend$addPersistentStoreWithType:configuration:URL:options:error:
- _objc_msgSend$aid
- _objc_msgSend$aliroGroupResolvingKeys
- _objc_msgSend$applets
- _objc_msgSend$associatedReaderIdentifiers
- _objc_msgSend$boolValue
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
- _objc_msgSend$crsUpdateCounter
- _objc_msgSend$dbProtectionType
- _objc_msgSend$defaultManager
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$ecp2Info
- _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$executeFetchRequest:error:
- _objc_msgSend$executeRequest:error:
- _objc_msgSend$expressEnabled
- _objc_msgSend$fetchRequest
- _objc_msgSend$fetchRequestWithEntityName:
- _objc_msgSend$fileURLWithPath:
- _objc_msgSend$firstObject
- _objc_msgSend$groupActivationStyle
- _objc_msgSend$groupHead
- _objc_msgSend$groupMembers
- _objc_msgSend$hasChanges
- _objc_msgSend$inSessionOnly
- _objc_msgSend$initWithArray:
- _objc_msgSend$initWithConcurrencyType:
- _objc_msgSend$initWithContentsOfURL:
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$initWithFetchRequest:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithManagedObjectModel:
- _objc_msgSend$initWithString:
- _objc_msgSend$initWithUTF8String:
- _objc_msgSend$insertNewObjectForEntityForName:inManagedObjectContext:
- _objc_msgSend$intValue
- _objc_msgSend$isEqualToString:
- _objc_msgSend$isUserChoice
- _objc_msgSend$keyID
- _objc_msgSend$longLongValue
- _objc_msgSend$moduleID
- _objc_msgSend$name
- _objc_msgSend$numberWithBool:
- _objc_msgSend$numberWithInt:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$passID
- _objc_msgSend$performBlock:
- _objc_msgSend$performBlockAndWait:
- _objc_msgSend$readerID
- _objc_msgSend$removeItemAtURL:error:
- _objc_msgSend$reset
- _objc_msgSend$save:
- _objc_msgSend$seid
- _objc_msgSend$setAid:
- _objc_msgSend$setAliroGroupResolvingKeys:
- _objc_msgSend$setApplets:
- _objc_msgSend$setAssociatedReaderIdentifiers:
- _objc_msgSend$setCrsUpdateCounter:
- _objc_msgSend$setEcp2Info:
- _objc_msgSend$setExpressEnabled:
- _objc_msgSend$setGroupActivationStyle:
- _objc_msgSend$setGroupHead:
- _objc_msgSend$setGroupMembers:
- _objc_msgSend$setInSessionOnly:
- _objc_msgSend$setIsUserChoice:
- _objc_msgSend$setKeyID:
- _objc_msgSend$setModuleID:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setObject:forKeyedSubscript:
- _objc_msgSend$setPassID:
- _objc_msgSend$setPersistentStoreCoordinator:
- _objc_msgSend$setReaderID:
- _objc_msgSend$setSeid:
- _objc_msgSend$setType:
- _objc_msgSend$setUwbExpressEnabled:
- _objc_msgSend$setVersion:
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$type
- _objc_msgSend$uwbExpressEnabled
- _objc_msgSend$version

```
