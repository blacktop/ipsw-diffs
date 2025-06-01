## CoreData

> `/System/Library/Frameworks/CoreData.framework/CoreData`

```diff

-1327.0.0.0.0
-  __TEXT.__text: 0x2aa6a0
+1333.0.0.0.0
+  __TEXT.__text: 0x2abc6c
   __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x101d4
-  __TEXT.__const: 0x1078
+  __TEXT.__objc_methlist: 0x10214
+  __TEXT.__const: 0x1098
   __TEXT.__swift5_typeref: 0x33e
   __TEXT.__swift5_capture: 0x21c
-  __TEXT.__cstring: 0x54d4b
+  __TEXT.__cstring: 0x55004
   __TEXT.__constg_swiftt: 0x14c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x1bc

   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_fieldmd: 0x12c
-  __TEXT.__gcc_except_tab: 0x1577c
-  __TEXT.__oslogstring: 0x8edf
-  __TEXT.__unwind_info: 0x7c08
+  __TEXT.__gcc_except_tab: 0x15a8c
+  __TEXT.__oslogstring: 0x8f58
+  __TEXT.__unwind_info: 0x7c6c
   __TEXT.__eh_frame: 0x600
-  __TEXT.__objc_classname: 0x3966
-  __TEXT.__objc_methname: 0x1dc0e
+  __TEXT.__objc_classname: 0x397c
+  __TEXT.__objc_methname: 0x1dcc0
   __TEXT.__objc_methtype: 0x4ca1
-  __TEXT.__objc_stubs: 0x13880
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x49b0
-  __DATA_CONST.__objc_classlist: 0xfa8
+  __TEXT.__objc_stubs: 0x13940
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x4988
+  __DATA_CONST.__objc_classlist: 0xfb0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ed48
-  __DATA_CONST.__objc_selrefs: 0x5f08
-  __DATA_CONST.__objc_arraydata: 0x6478
-  __AUTH_CONST.__objc_const: 0xb988
+  __DATA_CONST.__objc_const: 0x1edd0
+  __DATA_CONST.__objc_selrefs: 0x5f30
+  __DATA_CONST.__objc_arraydata: 0x6598
+  __AUTH_CONST.__objc_const: 0xba18
   __AUTH_CONST.__const: 0x1560
-  __AUTH_CONST.__cfstring: 0x2d100
-  __AUTH_CONST.__objc_dictobj: 0x1a68
+  __AUTH_CONST.__cfstring: 0x2d280
+  __AUTH_CONST.__objc_dictobj: 0x1d38
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x6ed0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1218
-  __AUTH.__objc_data: 0x41b8
+  __AUTH.__objc_data: 0x4208
   __AUTH.__data: 0x138
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x1100
-  __DATA.__objc_superrefs: 0xcc0
-  __DATA.__objc_ivar: 0x1e6c
+  __DATA.__objc_classrefs: 0x1108
+  __DATA.__objc_superrefs: 0xcc8
+  __DATA.__objc_ivar: 0x1e7c
   __DATA.__data: 0x12d0
   __DATA.__common: 0x598
   __DATA.__bss: 0xad0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 28C80BD9-6CF1-3461-83BF-75BBBB50768F
-  Functions: 8916
-  Symbols:   29756
-  CStrings:  19473
+  UUID: FEA5F37D-37AD-36BD-9516-7EC534BAD3DE
+  Functions: 8929
+  Symbols:   29842
+  CStrings:  19507
 
Symbols:
+ +[PFModelDecoderContext assertNoContext]
+ +[PFModelDecoderContext retainedContext]
+ -[NSCloudKitMirroringDelegate _setUpCloudKitIntegration:]
+ -[NSEntityDescription(_NSInternalMethods) performPostDecodeValidationInModel:error:]
+ -[NSManagedObjectContext _coreMergeChangesFromDidSaveDictionary:usingObjectIDs:withClientQueryGeneration:]
+ -[PFModelDecoderContext dealloc]
+ GCC_except_table67
+ _.str.438
+ _.str.647
+ _NSFileProtectionCompleteWhenUserInactive
+ _OBJC_CLASS_$_PFModelDecoderContext
+ _OBJC_IVAR_$_NSCloudKitMirroringDelegateOptions._bypassDasdRateLimiting
+ _OBJC_IVAR_$_PFModelDecoderContext.entity
+ _OBJC_IVAR_$_PFModelDecoderContext.model
+ _OBJC_IVAR_$_PFModelDecoderContext.objectPool
+ _OBJC_METACLASS_$_PFModelDecoderContext
+ __NSPersistentStoreCoordinatorPrivateWillRemoveStoreNotification
+ __OBJC_$_CLASS_METHODS_PFModelDecoderContext
+ __OBJC_$_INSTANCE_METHODS_PFModelDecoderContext
+ __OBJC_$_INSTANCE_VARIABLES_PFModelDecoderContext
+ __OBJC_CLASS_RO_$_PFModelDecoderContext
+ __OBJC_METACLASS_RO_$_PFModelDecoderContext
+ ___32-[NSFetchRequest initWithCoder:]_block_invoke
+ ___37-[NSEntityDescription initWithCoder:]_block_invoke
+ ___38-[NSManagedObjectModel initWithCoder:]_block_invoke
+ ___39-[NSPropertyDescription initWithCoder:]_block_invoke
+ ___41-[NSFetchIndexDescription initWithCoder:]_block_invoke
+ ___43-[NSRelationshipDescription initWithCoder:]_block_invoke
+ ___48-[PFCloudKitStoreMonitor retainedMonitoredStore]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_49_e8_32o40r_e34_v32?0"NSObject"8"NSError"16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32o40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
+ ___block_literal_global.420
+ ___block_literal_global.441
+ __unnamed_array_storage.102
+ __unnamed_array_storage.108
+ __unnamed_array_storage.119
+ __unnamed_array_storage.126
+ __unnamed_array_storage.127
+ __unnamed_array_storage.133
+ __unnamed_array_storage.134
+ __unnamed_array_storage.140
+ __unnamed_array_storage.146
+ __unnamed_array_storage.153
+ __unnamed_array_storage.154
+ __unnamed_array_storage.161
+ __unnamed_array_storage.162
+ __unnamed_array_storage.168
+ __unnamed_array_storage.169
+ __unnamed_array_storage.203
+ __unnamed_array_storage.38
+ __unnamed_array_storage.52
+ __unnamed_array_storage.53
+ __unnamed_array_storage.593
+ __unnamed_array_storage.597
+ __unnamed_array_storage.60
+ __unnamed_array_storage.67
+ __unnamed_array_storage.68
+ __unnamed_array_storage.74
+ __unnamed_array_storage.75
+ __unnamed_array_storage.89
+ __unnamed_array_storage.90
+ __unnamed_array_storage.96
+ __unnamed_array_storage.97
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$assertNoContext
+ _objc_msgSend$checksumsForVersionedModelAtURL:error:
+ _objc_msgSend$performPostDecodeValidationInModel:error:
+ _objc_msgSend$retainedContext
+ _objc_msgSend$setOverrideRateLimiting:
- -[NSCloudKitMirroringDelegate _setUpCloudKitIntegration]
- -[NSManagedObjectContext _mergeChangesFromDidSaveDictionary:usingObjectIDs:withClientQueryGeneration:]
- GCC_except_table76
- GCC_except_table89
- _.str.408
- _.str.604
- __NSPersistentStoreCoorindatorPrivateWillRemoveStoreNotification
- ___block_descriptor_48_e8_32o40w_e8_v12?0i8lw40l8s32l8
- ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
- ___block_descriptor_49_e8_32o40r_e34_v32?0"NSObject"8"NSError"16^B24lr40l8s32l8
- ___block_descriptor_72_e8_32o40o48o56o64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.394
- ___block_literal_global.411
- __unnamed_array_storage.100
- __unnamed_array_storage.105
- __unnamed_array_storage.118
- __unnamed_array_storage.124
- __unnamed_array_storage.125
- __unnamed_array_storage.130
- __unnamed_array_storage.131
- __unnamed_array_storage.137
- __unnamed_array_storage.138
- __unnamed_array_storage.187
- __unnamed_array_storage.188
- __unnamed_array_storage.36
- __unnamed_array_storage.66
- __unnamed_array_storage.81
- __unnamed_array_storage.88
- __unnamed_array_storage.93
- __unnamed_array_storage.99
CStrings:
+ " bypassDasdRateLimiting:%@"
+ "%@: Successfully enqueued setup request from push notification: %@"
+ "%@: Successfully enqueued setup request: %@"
+ "-[NSCloudKitMirroringDelegate _setUpCloudKitIntegration:]"
+ "A model with version checksum %@ could not be found in the bundle at %@."
+ "CoreData: PFCloudKitStoreMonitor failed to tear down gracefully, this means requests are probably about to fail: %@ - %@"
+ "Invalid NSManagedObjectModel"
+ "NSDestinationEntity requires a NSEntityDescription"
+ "NSFetchRequestTemplates requires a NSMutableDictionary<NSString, NSFetchRequest>"
+ "NSInverseRelationship requires a NSRelationshipDescription"
+ "NSProperties requires a NSMutableDictionary<NSString, NSPropertyDescription>"
+ "PFCloudKitStoreMonitor failed to tear down gracefully, this means requests are probably about to fail: %@ - %@"
+ "PFModelDecoderContext"
+ "Spotlight index not deleted because indexing was not started."
+ "URLByAppendingPathExtension:"
+ "Unowned NSDestinationEntity"
+ "Unowned NSEntity"
+ "Unowned NSInverseRelationship"
+ "Unowned NSSuperentity"
+ "XPC: synchronousRemoteObjectProxyWithErrorHandler: store '%@' encountered error: %@"
+ "_NSPersistentStoreCoordinatorPrivateWillRemoveStoreNotification"
+ "_bypassDasdRateLimiting"
+ "_coreMergeChangesFromDidSaveDictionary:usingObjectIDs:withClientQueryGeneration:"
+ "assertNoContext"
+ "objectPool"
+ "performPostDecodeValidationInModel:error:"
+ "retainedContext"
+ "setOverrideRateLimiting:"
- "%@: Successfully enqueued setup request."
- "-[NSCloudKitMirroringDelegate _setUpCloudKitIntegration]"
- "NSManagedObjectModel requires a NSManagedObjectModel"
- "XPC: synchronousRemoteObjectProxyWithErrorHandler encountered error: %@"
- "_NSPersistentStoreCoorindatorPrivateWillRemoveStoreNotification"
- "_mergeChangesFromDidSaveDictionary:usingObjectIDs:withClientQueryGeneration:"

```
