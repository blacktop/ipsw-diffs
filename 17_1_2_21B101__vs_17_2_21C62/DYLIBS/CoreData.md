## CoreData

> `/System/Library/Frameworks/CoreData.framework/CoreData`

```diff

-1333.0.0.0.0
-  __TEXT.__text: 0x2abc6c
+1338.0.0.0.0
+  __TEXT.__text: 0x2af378
   __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x10214
+  __TEXT.__objc_methlist: 0x103ec
   __TEXT.__const: 0x1098
   __TEXT.__swift5_typeref: 0x33e
   __TEXT.__swift5_capture: 0x21c
-  __TEXT.__cstring: 0x55004
+  __TEXT.__cstring: 0x55dd3
   __TEXT.__constg_swiftt: 0x14c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x1bc

   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_fieldmd: 0x12c
-  __TEXT.__gcc_except_tab: 0x15a8c
-  __TEXT.__oslogstring: 0x8f58
-  __TEXT.__unwind_info: 0x7c6c
+  __TEXT.__gcc_except_tab: 0x15b50
+  __TEXT.__oslogstring: 0x92fc
+  __TEXT.__unwind_info: 0x7cd8
   __TEXT.__eh_frame: 0x600
-  __TEXT.__objc_classname: 0x397c
-  __TEXT.__objc_methname: 0x1dcc0
-  __TEXT.__objc_methtype: 0x4ca1
-  __TEXT.__objc_stubs: 0x13940
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x4988
-  __DATA_CONST.__objc_classlist: 0xfb0
+  __TEXT.__objc_classname: 0x39d3
+  __TEXT.__objc_methname: 0x1e0ba
+  __TEXT.__objc_methtype: 0x4ce2
+  __TEXT.__objc_stubs: 0x13c80
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__const: 0x49d8
+  __DATA_CONST.__objc_classlist: 0xfc0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1edd0
-  __DATA_CONST.__objc_selrefs: 0x5f30
-  __DATA_CONST.__objc_arraydata: 0x6598
-  __AUTH_CONST.__objc_const: 0xba18
+  __DATA_CONST.__objc_const: 0x1efe8
+  __DATA_CONST.__objc_selrefs: 0x6020
+  __DATA_CONST.__objc_arraydata: 0x65f8
+  __AUTH_CONST.__objc_const: 0xbb38
   __AUTH_CONST.__const: 0x1560
-  __AUTH_CONST.__cfstring: 0x2d280
-  __AUTH_CONST.__objc_dictobj: 0x1d38
+  __AUTH_CONST.__cfstring: 0x2d820
+  __AUTH_CONST.__objc_dictobj: 0x1dd8
   __AUTH_CONST.__objc_intobj: 0x558
-  __AUTH_CONST.__objc_arrayobj: 0x6ed0
+  __AUTH_CONST.__objc_arrayobj: 0x6f00
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1218
-  __AUTH.__objc_data: 0x4208
+  __AUTH.__objc_data: 0x42a8
   __AUTH.__data: 0x138
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x1108
-  __DATA.__objc_superrefs: 0xcc8
-  __DATA.__objc_ivar: 0x1e7c
+  __DATA.__objc_classrefs: 0x1120
+  __DATA.__objc_superrefs: 0xcd8
+  __DATA.__objc_ivar: 0x1ea4
   __DATA.__data: 0x12d0
   __DATA.__common: 0x598
   __DATA.__bss: 0xad0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: FEA5F37D-37AD-36BD-9516-7EC534BAD3DE
-  Functions: 8929
-  Symbols:   29842
-  CStrings:  19507
+  UUID: 906D68F4-4D51-3C8D-8ED3-20C2086555F3
+  Functions: 8972
+  Symbols:   29997
+  CStrings:  19669
 
Symbols:
+ +[NSPersistentCloudKitContainerActivityVoucher describeConfiguration:]
+ +[NSPersistentCloudKitContainerActivityVoucher describeConfigurationWithoutPointer:]
+ +[NSPersistentCloudKitContainerActivityVoucher stringForQoS:]
+ +[NSPersistentCloudKitContainerActivityVoucher supportsSecureCoding]
+ -[NSAttributeDescription _attributeValueClasses]
+ -[NSCloudKitMirroringActivityVoucherManager _vouchersForEventType:]
+ -[NSCloudKitMirroringActivityVoucherManager addVoucher:]
+ -[NSCloudKitMirroringActivityVoucherManager countVouchers]
+ -[NSCloudKitMirroringActivityVoucherManager dealloc]
+ -[NSCloudKitMirroringActivityVoucherManager expireVoucher:]
+ -[NSCloudKitMirroringActivityVoucherManager hasVoucherMatching:]
+ -[NSCloudKitMirroringActivityVoucherManager init]
+ -[NSCloudKitMirroringActivityVoucherManager usableVoucherForEventType:]
+ -[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:voucher:completionHandler:]
+ -[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:voucher:completionHandler:]
+ -[NSCloudKitMirroringDelegate addActivityVoucher:]
+ -[NSCloudKitMirroringDelegate expireActivityVoucher:]
+ -[NSCloudKitMirroringDelegate newActivityWithIdentifier:andVoucher:]
+ -[NSCloudKitMirroringDelegateSetupRequest createDefaultOptions]
+ -[NSCloudKitMirroringDelegateSetupRequestOptions copyWithZone:]
+ -[NSCloudKitMirroringDelegateSetupRequestOptions createDefaultOperationConfiguration]
+ -[NSCloudKitMirroringRequest createDefaultOptions]
+ -[NSCloudKitMirroringRequestOptions applyToOperation:]
+ -[NSCloudKitMirroringRequestOptions createDefaultOperationConfiguration]
+ -[NSCloudKitMirroringRequestOptions setVouchers:]
+ -[NSCloudKitMirroringRequestOptions vouchers]
+ -[NSCompositeAttributeDescription _setEntityAndMaintainIndices:]
+ -[NSPersistentCloudKitContainer applyActivityVoucher:toStores:]
+ -[NSPersistentCloudKitContainer expireActivityVoucher:]
+ -[NSPersistentCloudKitContainerActivityVoucher bundleIdentifier]
+ -[NSPersistentCloudKitContainerActivityVoucher copyWithZone:]
+ -[NSPersistentCloudKitContainerActivityVoucher dealloc]
+ -[NSPersistentCloudKitContainerActivityVoucher description]
+ -[NSPersistentCloudKitContainerActivityVoucher encodeWithCoder:]
+ -[NSPersistentCloudKitContainerActivityVoucher eventType]
+ -[NSPersistentCloudKitContainerActivityVoucher fetchRequest]
+ -[NSPersistentCloudKitContainerActivityVoucher initWithCoder:]
+ -[NSPersistentCloudKitContainerActivityVoucher initWithLabel:forEventsOfType:withConfiguration:affectingObjectsMatching:]
+ -[NSPersistentCloudKitContainerActivityVoucher label]
+ -[NSPersistentCloudKitContainerActivityVoucher operationConfiguration]
+ -[NSPersistentCloudKitContainerActivityVoucher processName]
+ -[NSPropertyDescription(_NSInternalMethods) _qualifiedName]
+ -[PFCloudKitMetadataModelMigrator checkForOrphanedMirroredRelationshipsInStore:inManagedObjectContext:error:]
+ _.str.452
+ _.str.661
+ _OBJC_CLASS_$_NSCloudKitMirroringActivityVoucherManager
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSPersistentCloudKitContainerActivityVoucher
+ _OBJC_IVAR_$_NSCloudKitMirroringActivityVoucherManager._vouchersByEventType
+ _OBJC_IVAR_$_NSCloudKitMirroringDelegate._voucherManager
+ _OBJC_IVAR_$_NSCloudKitMirroringRequestOptions._vouchers
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerActivityVoucher._bundleIdentifier
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerActivityVoucher._eventType
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerActivityVoucher._fetchRequest
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerActivityVoucher._label
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerActivityVoucher._operationConfiguration
+ _OBJC_IVAR_$_NSPersistentCloudKitContainerActivityVoucher._processName
+ _OBJC_IVAR_$_PFCloudKitMetadataMigrationContext._needsCleanupFromOrphanedMirroredRelationships
+ _OBJC_METACLASS_$_NSCloudKitMirroringActivityVoucherManager
+ _OBJC_METACLASS_$_NSPersistentCloudKitContainerActivityVoucher
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ __OBJC_$_CLASS_METHODS_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_$_CLASS_PROP_LIST_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_$_INSTANCE_METHODS_NSCloudKitMirroringActivityVoucherManager
+ __OBJC_$_INSTANCE_METHODS_NSCloudKitMirroringDelegateSetupRequest
+ __OBJC_$_INSTANCE_METHODS_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_$_INSTANCE_VARIABLES_NSCloudKitMirroringActivityVoucherManager
+ __OBJC_$_INSTANCE_VARIABLES_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_$_PROP_LIST_NSCloudKitMirroringActivityVoucherManager
+ __OBJC_$_PROP_LIST_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_CLASS_PROTOCOLS_$_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_CLASS_RO_$_NSCloudKitMirroringActivityVoucherManager
+ __OBJC_CLASS_RO_$_NSPersistentCloudKitContainerActivityVoucher
+ __OBJC_METACLASS_RO_$_NSCloudKitMirroringActivityVoucherManager
+ __OBJC_METACLASS_RO_$_NSPersistentCloudKitContainerActivityVoucher
+ ___100-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:voucher:completionHandler:]_block_invoke
+ ___100-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:voucher:completionHandler:]_block_invoke
+ ___50-[NSCloudKitMirroringDelegate addActivityVoucher:]_block_invoke
+ ___53-[NSCloudKitMirroringDelegate expireActivityVoucher:]_block_invoke
+ ___57-[NSCloudKitMirroringDelegate _performExportWithRequest:]_block_invoke.403
+ ___60-[NSCloudKitMirroringDelegate _performMetadataResetRequest:]_block_invoke.448
+ ___64-[NSCompositeAttributeDescription _setEntityAndMaintainIndices:]_block_invoke
+ ___69-[NSCloudKitMirroringDelegate _performAcceptShareInvitationsRequest:]_block_invoke.501
+ ___79-[NSCloudKitMirroringDelegate _acceptShareMetadatasInRequest:workBlockContext:]_block_invoke.521
+ ___84-[NSCloudKitMirroringDelegate _recoverFromUnknownShareRecordIDs:forStore:inMonitor:]_block_invoke
+ ___block_descriptor_104_e8_32o40o48o56o64o72o80o88r96r_e45_v32?0"NSObject<NSCopying>"8"NSError"16^B24ls32l8r88l8r96l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_48_e8_32o40r_e41_v24?0"NSArray"8"NSEntityDescription"16lr40l8s32l8
+ ___block_descriptor_56_e8_32o40b48r_e32_v16?0"NSAttributeDescription"8lr48l8s40l8s32l8
+ ___block_descriptor_80_e8_32o40o48o56o64r72r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_literal_global.284
+ __unnamed_array_storage.177
+ __unnamed_array_storage.185
+ __unnamed_array_storage.323
+ __unnamed_array_storage.326
+ __unnamed_array_storage.356
+ __unnamed_array_storage.392
+ __unnamed_array_storage.417
+ __unnamed_array_storage.608
+ __unnamed_array_storage.611
+ __unnamed_array_storage.612
+ _objc_msgSend$_qualifiedName
+ _objc_msgSend$addActivityVoucher:
+ _objc_msgSend$addParticipant:
+ _objc_msgSend$addVoucher:
+ _objc_msgSend$allowsExpensiveNetworkAccess
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$createDefaultOperationConfiguration
+ _objc_msgSend$createDefaultOptions
+ _objc_msgSend$describeConfiguration:
+ _objc_msgSend$eventType
+ _objc_msgSend$expireActivityVoucher:
+ _objc_msgSend$expireVoucher:
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$initWithLabel:forEventsOfType:withConfiguration:affectingObjectsMatching:
+ _objc_msgSend$invert
+ _objc_msgSend$isLongLived
+ _objc_msgSend$operationConfiguration
+ _objc_msgSend$participants
+ _objc_msgSend$replaceCharactersInRange:withString:
+ _objc_msgSend$role
+ _objc_msgSend$setVouchers:
+ _objc_msgSend$stringForQoS:
+ _objc_msgSend$timeoutIntervalForRequest
+ _objc_msgSend$timeoutIntervalForResource
+ _objc_msgSend$usableVoucherForEventType:
- -[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:completionHandler:]
- -[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:completionHandler:]
- -[NSCloudKitMirroringDelegate newActivityWithIdentifier:]
- -[NSPropertyDescription _qualifiedName]
- _.str.438
- _.str.647
- ___57-[NSCloudKitMirroringDelegate _performExportWithRequest:]_block_invoke.401
- ___60-[NSCloudKitMirroringDelegate _performMetadataResetRequest:]_block_invoke.446
- ___69-[NSCloudKitMirroringDelegate _performAcceptShareInvitationsRequest:]_block_invoke.500
- ___79-[NSCloudKitMirroringDelegate _acceptShareMetadatasInRequest:workBlockContext:]_block_invoke.520
- ___92-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:completionHandler:]_block_invoke
- ___92-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:completionHandler:]_block_invoke
- ___block_descriptor_48_e8_32b40r_e32_v16?0"NSAttributeDescription"8lr40l8s32l8
- ___block_descriptor_96_e8_32o40o48o56o64o72o80r88r_e45_v32?0"NSObject<NSCopying>"8"NSError"16^B24ls32l8r80l8r88l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.282
- ___block_literal_global.441
- __unnamed_array_storage.116
- __unnamed_array_storage.361
- __unnamed_array_storage.377
- __unnamed_array_storage.402
- __unnamed_array_storage.593
- __unnamed_array_storage.597
CStrings:
+ "$_"
+ "%@ deleted %@ mirrored relationship entries because %@:%@ is no longer in the managed object model of this store: %@"
+ "%@ does not allow clients to specify if operations are longlived or not. Clients should leave longLived unmodified and allow %@ to choose to mark operations long lived or not."
+ "%@ does not support network customizations yet (allowsCellularAccess = NO). If you require this functionality please file a radar to CoreData | New Bugs."
+ "%@ does not support network customizations yet (allowsExpensiveNetworkAccess = NO). If you require this functionality please file a radar to CoreData | New Bugs."
+ "%@ does not support the escalation of events of type %@. %@ events will be escalated in association with a voucher that is applied to %@ / %@ events as needed."
+ "%@ requires that clients pass in an instance of %@ that describes how they would like to prioritize work on behalf of the voucher."
+ "%@: Bypassing dasd for scheduling for voucher: %@\n%@"
+ "%@:%@:%d:%f:%f"
+ "+checksumsForVersionedModelAtURL:error: Failed to load model at URL '%@' due to error %@"
+ "-[NSCloudKitMirroringDelegate _recoverFromUnknownShareRecordIDs:forStore:inMonitor:]_block_invoke"
+ "-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:voucher:completionHandler:]"
+ "-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:voucher:completionHandler:]_block_invoke"
+ "-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:voucher:completionHandler:]"
+ "-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:voucher:completionHandler:]_block_invoke"
+ "-[PFCloudKitMetadataModelMigrator checkForOrphanedMirroredRelationshipsInStore:inManagedObjectContext:error:]"
+ "<%@:%p %@:%@:%d:%f:%f>"
+ "<%@:%p %@>\n\t%@\n\t%@:%@\n\t%@\n\t%@"
+ "@\"NSCloudKitMirroringActivityVoucherManager\""
+ "@48@0:8@16q24@32@40"
+ "AutomatedExportBypassingDasdDueToVoucher"
+ "Background"
+ "Composite"
+ "Composite %@ that is preserved on deletion but element %@ is not."
+ "CoreData: %@ Apply"
+ "CoreData: %@ Expire"
+ "CoreData: Could not materialize Objective-C class \"%@\" for attribute named \"%@\", property setter will not validate type"
+ "CoreData: Could not materialize Objective-C class for declared attribute value class name \"%@\" of attribute named %@"
+ "CoreData: Could not materialize Objective-C class named \"%@\" from declared attribute value type \"%@\" of attribute named %@"
+ "CoreData: Declared Objective-C type \"%@\" for attribute named %@ is not valid"
+ "CoreData: Did someone add a new QoS class? This method should probably be updated."
+ "CoreData: Got an unknown item error for a zone metadata without a share: %@ - %@"
+ "CoreData: Illegal branch data: lower"
+ "CoreData: Illegal branch data: offset"
+ "CoreData: Illegal branch data: operation"
+ "CoreData: Illegal branch data: parameter"
+ "CoreData: Illegal branch data: upper"
+ "CoreData: Is there a new event type: %@"
+ "CoreData: Zone metadata is missing it's encoded share data but is marked for a mutation: %@ - %@"
+ "Could not materialize Objective-C class \"%@\" for attribute named \"%@\", property setter will not validate type"
+ "Could not materialize Objective-C class for declared attribute value class name \"%@\" of attribute named %@"
+ "Could not materialize Objective-C class named \"%@\" from declared attribute value type \"%@\" of attribute named %@"
+ "DELETE FROM ANSCKMIRROREDRELATIONSHIP WHERE ZCDENTITYNAME = '%@' AND ZRELATIONSHIPNAME = '%@'"
+ "Declared Objective-C type \"%@\" for attribute named %@ is not valid"
+ "Did someone add a new QoS class? This method should probably be updated."
+ "Element"
+ "Element %@ is preserved on deletion but its composite %@ is not."
+ "Failed to recover from an unknown item error because the replacement share record couldn't be encoded: %@\n%@"
+ "Failed to recover from an unknown item error because the share recovery save failed: %@\n%@"
+ "Failed to recover from an unknown item error for '%@' because the zone metadata couldn't be fetched: %@"
+ "Failed to recover from unknown item error because the current share couldn't be decoded: %@ - %@"
+ "Got an unknown item error for a zone metadata without a share: %@ - %@"
+ "Illegal branch data: lower"
+ "Illegal branch data: offset"
+ "Illegal branch data: operation"
+ "Illegal branch data: parameter"
+ "Illegal branch data: upper"
+ "Is there a new event type: %@"
+ "NSCloudKitMirroringActivityVoucherManager"
+ "NSPersistentCloudKitContainerActivityVoucher"
+ "Nested composite %@ is not eligible for preserving values on deletion (only allowed for root composite and leaves)."
+ "Push-Voucher-%@"
+ "T@\"CKOperationConfiguration\",R,C,N,V_operationConfiguration"
+ "T@\"NSArray\",&,N,V_vouchers"
+ "T@\"NSFetchRequest\",R,C,N,V_fetchRequest"
+ "T@\"NSString\",R,C,N,V_bundleIdentifier"
+ "T@\"NSString\",R,C,N,V_label"
+ "T@\"NSString\",R,C,N,V_processName"
+ "The store must be opened one time without Staged Migration to update store metadata to be able to use Staged Migration."
+ "Tq,R,N,V_eventType"
+ "Unsupported type for buffer allocated dictionary: %@"
+ "UserInitiated"
+ "UserInteractive"
+ "Utility"
+ "VoucherImmediateExport"
+ "VoucherImmediateImport"
+ "Zone metadata is missing it's encoded share data but is marked for a mutation: %@ - %@"
+ "_needsCleanupFromOrphanedMirroredRelationships"
+ "_qualifiedName"
+ "_voucherManager"
+ "_vouchers"
+ "_vouchersByEventType"
+ "addActivityVoucher:"
+ "addParticipant:"
+ "addVoucher:"
+ "allowsExpensiveNetworkAccess"
+ "applyActivityVoucher:toStores:"
+ "cdEntityName = %@ AND relationshipName = %@"
+ "characterSetWithCharactersInString:"
+ "com.apple.coredata.voucher.apply"
+ "com.apple.coredata.voucher.expire"
+ "componentsSeparatedByCharactersInSet:"
+ "countVouchers"
+ "createDefaultOperationConfiguration"
+ "createDefaultOptions"
+ "describeConfiguration:"
+ "describeConfigurationWithoutPointer:"
+ "eventType"
+ "eventTypeNum"
+ "expireActivityVoucher:"
+ "expireVoucher:"
+ "fetchIndexDescriptions requires a NSFetchIndexDescription"
+ "fetchIndexDescriptions requires an NSArray"
+ "formUnionWithCharacterSet:"
+ "hasVoucherMatching:"
+ "indexDescription requires a NSFetchIndexDescription"
+ "initWithLabel:forEventsOfType:withConfiguration:affectingObjectsMatching:"
+ "invert"
+ "isLongLived"
+ "offendingConfiguration"
+ "property description requires a NSPropertyDescription"
+ "replaceCharactersInRange:withString:"
+ "role"
+ "setVouchers:"
+ "stringForQoS:"
+ "timeoutIntervalForRequest"
+ "timeoutIntervalForResource"
+ "usableVoucherForEventType:"
+ "v24@?0@\"NSArray\"8@\"NSEntityDescription\"16"
+ "vouchers"
+ "wifi+celluar"
+ "wifi-only"
- "+checksumsForVersionedModelAtURL:error: Failed to load model at URL '%@'"
- "-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:completionHandler:]"
- "-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:completionHandler:]_block_invoke"
- "-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:completionHandler:]"
- "-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:completionHandler:]_block_invoke"
- "The metadata of this store file must be updated to use Staged Migration."
- "Unsupoorted type for buffer allocated dictionary: %@"

```
