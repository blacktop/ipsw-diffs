## UserProfilesCore

> `/System/Library/PrivateFrameworks/UserProfilesCore.framework/UserProfilesCore`

```diff

-299.10.21.0.0
-  __TEXT.__text: 0xae38
+299.20.9.0.0
+  __TEXT.__text: 0xad58
   __TEXT.__objc_methlist: 0xe34
   __TEXT.__const: 0x2b6
   __TEXT.__cstring: 0x9d7
-  __TEXT.__oslogstring: 0x9e0
+  __TEXT.__oslogstring: 0x960
   __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__swift5_typeref: 0x150
   __TEXT.__swift5_fieldmd: 0xc4

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x618
+  __TEXT.__unwind_info: 0x610
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__const: 0x278
   __AUTH_CONST.__cfstring: 0xb40
   __AUTH_CONST.__objc_const: 0x3320
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0xb8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 419
-  Symbols:   818
-  CStrings:  143
+  Functions: 417
+  Symbols:   819
+  CStrings:  142
 
Symbols:
+ +[UPPersistentContainer _loadPersistentStoreWithPersistentContainerDescription:model:logObject:]
+ +[UPPersistentContainer _persistentStoreDidFailToLoadAtURL:error:]
+ -[UPPersistentContainer initWithPersistentContainerDescription:]
+ ___96+[UPPersistentContainer _loadPersistentStoreWithPersistentContainerDescription:model:logObject:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16ls32l8r48l8s40l8
+ __os_log_fault_impl
- +[UPPersistentContainer _loadPersistentStoreWithPersistentContainerDescription:model:logObject:recreateStoreOnLoadFailure:]
- +[UPPersistentContainer persistentContainerWithDescription:]
- -[UPPersistentContainer initWithPersistentContainerDescription:recreateStoreOnLoadFailure:]
- ___123+[UPPersistentContainer _loadPersistentStoreWithPersistentContainerDescription:model:logObject:recreateStoreOnLoadFailure:]_block_invoke
- ___block_descriptor_65_e8_32s40s48r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16ls32l8r48l8s40l8
CStrings:
- "Failed to load UserProfiles Store. THIS IS A BUG. PLEASE FILE A RADAR TO \"Apple TV | UserProfiles\" AND INCLUDE THE STORE FILES AT %@"
```
