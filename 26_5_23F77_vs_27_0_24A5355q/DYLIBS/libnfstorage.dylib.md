## libnfstorage.dylib

> `/usr/lib/libnfstorage.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x448c
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_methlist: 0x168
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x6af
-  __TEXT.__oslogstring: 0x416
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x894
-  __TEXT.__objc_methtype: 0x96
-  __TEXT.__objc_stubs: 0xb40
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x118
-  __DATA_CONST.__objc_classlist: 0x48
+370.33.1.0.0
+  __TEXT.__text: 0x7d10
+  __TEXT.__objc_methlist: 0x268
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0xd4d
+  __TEXT.__oslogstring: 0x546
+  __TEXT.__unwind_info: 0x108
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
-  __AUTH_CONST.__auth_got: 0x150
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x830
-  __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH.__objc_data: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x560
+  __AUTH_CONST.__objc_const: 0xbc8
+  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppletTranslationFramework.framework/AppletTranslationFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0FEAB285-2A7D-3A9A-AB1D-C54166115F4F
-  Functions: 34
-  Symbols:   83
-  CStrings:  253
+  UUID: B7A9B9F2-9481-378A-80B1-ECA5E6F28D67
+  Functions: 60
+  Symbols:   105
+  CStrings:  151
 
Symbols:
+ _ATLECP2InfoKey
+ _ATLPassInformationAliroGroupResolvingKeys
+ _ATLPassInformationAppletAID
+ _ATLPassInformationAssociatedReaderIdentifiers
+ _ATLPassInformationAutomaticSelectionType
+ _ATLPassInformationExpressEnabled
+ _ATLPassInformationGroupActivationStyle
+ _ATLPassInformationGroupHead
+ _ATLPassInformationGroupMembers
+ _ATLPassInformationInSessionOnly
+ _ATLPassInformationIsUserChoice
+ _ATLPassInformationKeyIdentifier
+ _ATLPassInformationKeyReaderIdentifier
+ _ATLPassInformationModuleIdentifier
+ _ATLPassInformationUWBExpressEnabled
+ _ATLPassInformationUniqueID
+ _OBJC_CLASS_$_NFStorageControllerDeveloperPresentment
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_NFStorageControllerDeveloperPresentment
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ ""
+ "%{public}s:%i Failed to delete presentment entities: %{public}@"
+ "%{public}s:%i Failed to delete receipt entities: %{public}@"
+ "%{public}s:%i Failed to delete report entities: %{public}@"
+ "%{public}s:%i No receipt found for bundleID=%{public}@ teamID=%{public}@"
+ "%{public}s:%i No report found for id %{public}@"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReportReceipts]"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReportReceipts]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReports]"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReports]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment deleteReportWithId:]"
+ "-[NFStorageControllerDeveloperPresentment deleteReportWithId:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment fetchReportWithId:error:]"
+ "-[NFStorageControllerDeveloperPresentment fetchReportWithId:error:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment fetchReportsWithError:]"
+ "-[NFStorageControllerDeveloperPresentment fetchReportsWithError:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:]"
+ "-[NFStorageControllerDeveloperPresentment getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment savePresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:]"
+ "-[NFStorageControllerDeveloperPresentment savePresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:]"
+ "-[NFStorageControllerDeveloperPresentment updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:]_block_invoke"
+ "DeveloperPresentment"
+ "DeveloperPresentmentEntity"
+ "DeveloperPresentmentReportEntity"
+ "DeveloperPresentmentReportReceiptEntity"
+ "altitude"
+ "bundleID"
+ "bundleId == %@ AND teamId == %@"
+ "bundleId == %@ AND teamId == %@ AND timestampDay == %llu AND developerPresentments.@count < %d"
+ "city"
+ "country"
+ "developmentPresentments"
+ "endTimestamp"
+ "horizontalAccuracy"
+ "latitude"
+ "longitude"
+ "reportId"
+ "reportId == %@"
+ "startTimestamp"
+ "state"
+ "successfulTapCount"
+ "teamID"
+ "timestampDay"
- ".cxx_destruct"
- "@\"NSManagedObjectContext\""
- "@\"NSManagedObjectModel\""
- "@\"NSPersistentStoreCoordinator\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^@16"
- "CoreDataProperties"
- "ECP2Info"
- "ExpressType"
- "NFStorageController"
- "NFStorageControllerApplet"
- "NFStorageControllerESEExpress"
- "NFStorageInternalMethods"
- "T@\"NSObject\",&,D,N"
- "T@\"NSSet\",&,D,N"
- "T@\"NSString\",C,D,N"
- "T@\"PurpleTrustAppletEntity\",&,D,N"
- "T@\"PurpleTrustClientEntity\",&,D,N"
- "TB,D,N"
- "Ti,D,N"
- "Tq,D,N"
- "URLWithString:"
- "UWBExpressEnabled"
- "_deleteAllAppletEntities"
- "_deleteAllESEExpressEntities"
- "_managedObjectContext"
- "_managedObjectModel"
- "_persistentStoreCoordinator"
- "addObject:"
- "addPersistentStoreWithType:configuration:URL:options:error:"
- "aid"
- "aliroGroupResolvingKeys"
- "applet"
- "appletIdentifier"
- "associatedReaderIdentifiers"
- "blob"
- "boolValue"
- "client"
- "clientName"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "dbProtectionType"
- "defaultManager"
- "deleteAllAppletEntities"
- "deleteAllESEExpressEntities"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "ecp2Info"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "executeFetchRequest:error:"
- "executeRequest:error:"
- "expressEnabled"
- "fetchAppletEntitiesWithError:"
- "fetchESEExpressEntitiesWithError:"
- "fetchRequest"
- "fetchRequestWithEntityName:"
- "fileURLWithPath:"
- "firstObject"
- "groupActivationStyle"
- "groupHead"
- "groupMembers"
- "hasChanges"
- "identifier"
- "inSessionOnly"
- "initWithArray:"
- "initWithConcurrencyType:"
- "initWithContentsOfURL:"
- "initWithDomain:code:userInfo:"
- "initWithFetchRequest:"
- "initWithFormat:"
- "initWithManagedObjectModel:"
- "initWithString:"
- "initWithUTF8String:"
- "insertNewObjectForEntityForName:inManagedObjectContext:"
- "intValue"
- "isEqualToString:"
- "isUserChoice"
- "keyID"
- "keyIdentifier"
- "longLongValue"
- "moduleID"
- "moduleIdentifier"
- "name"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "passID"
- "passUniqueID"
- "performBlock:"
- "performBlockAndWait:"
- "purpleTrust"
- "readerID"
- "readerIdentifier"
- "removeItemAtURL:error:"
- "reset"
- "save:"
- "setAid:"
- "setAliroGroupResolvingKeys:"
- "setApplets:"
- "setAssociatedReaderIdentifiers:"
- "setCrsUpdateCounter:"
- "setEcp2Info:"
- "setExpressEnabled:"
- "setGroupActivationStyle:"
- "setGroupHead:"
- "setGroupMembers:"
- "setInSessionOnly:"
- "setIsUserChoice:"
- "setKeyID:"
- "setModuleID:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPassID:"
- "setPersistentStoreCoordinator:"
- "setReaderID:"
- "setSeid:"
- "setType:"
- "setUwbExpressEnabled:"
- "setVersion:"
- "stringByAppendingPathComponent:"
- "stringWithUTF8String:"
- "supportsUWB"
- "type"
- "uniqueIdentifier"
- "updateAppletEntitiesWithConfig:"
- "updateESEExpressEntitiesWithConfig:"
- "userChoice"
- "uwbExpressEnabled"
- "v16@0:8"
- "v24@0:8@16"
- "version"

```
