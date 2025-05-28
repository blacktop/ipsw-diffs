## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

-500.25.3.7.0
-  __TEXT.__text: 0x863a4
+500.25.5.10.0
+  __TEXT.__text: 0x86d98
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0xb640
-  __TEXT.__objc_methlist: 0x3b44
+  __TEXT.__objc_stubs: 0xb7c0
+  __TEXT.__objc_methlist: 0x3bf4
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x312c
-  __TEXT.__cstring: 0x2bfe
-  __TEXT.__objc_classname: 0xee9
-  __TEXT.__objc_methname: 0xe1d4
-  __TEXT.__objc_methtype: 0x248e
-  __TEXT.__oslogstring: 0xad50
+  __TEXT.__gcc_except_tab: 0x3164
+  __TEXT.__cstring: 0x2c9a
+  __TEXT.__objc_classname: 0xf1f
+  __TEXT.__objc_methname: 0xe342
+  __TEXT.__objc_methtype: 0x24a7
+  __TEXT.__oslogstring: 0xae41
   __TEXT.__ustring: 0x246
-  __TEXT.__unwind_info: 0x1d7c
+  __TEXT.__unwind_info: 0x1dbc
   __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__cfstring: 0x3020
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__const: 0x24a0
+  __DATA_CONST.__cfstring: 0x3180
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0x28
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x780
+  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_intobj: 0x138
+  __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x8ea8
-  __DATA.__objc_selrefs: 0x3050
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x778
-  __DATA.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x8fc8
+  __DATA.__objc_selrefs: 0x30b0
   __DATA.__objc_ivar: 0x298
-  __DATA.__objc_data: 0x1b30
+  __DATA.__objc_data: 0x1b80
   __DATA.__data: 0xc68
-  __DATA.__bss: 0x4f0
+  __DATA.__bss: 0x510
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2507
+  Functions: 2526
   Symbols:   435
-  CStrings:  3783
+  CStrings:  3818
 
Symbols:
+ _OBJC_CLASS_$_RMManagedDevice
- _OBJC_CLASS_$_MDMConfiguration
CStrings:
+ "(%K == %d) || (%K == %d)"
+ "B56@0:8@16@24q32^B40^@48"
+ "Checking migration - is supervised"
+ "CoreData migration failed - process exiting: %{public}@"
+ "Failed to update management sources: %{public}@"
+ "Finished migrating"
+ "Ignoring migration - no enrolled device channel"
+ "Ignoring migration - not supervised"
+ "RMMigrationSupervised"
+ "Starting to migrate with CoreData"
+ "Startup migration failed - process exiting: %{public}@"
+ "T@\"NSString\",?,R,C"
+ "Unable to fetch device management sources: %{public}@"
+ "Updated management sources to supervised."
+ "_changeDeviceEnrollmentTypeReturningError:"
+ "_coreDataActions"
+ "_migrateWithActions:error:"
+ "_startupActions"
+ "channel"
+ "cli"
+ "currentManagedDevice"
+ "delete"
+ "fetchRequestWithEnrollmentTypes:"
+ "hasDuplicateInContext:uri:storeType:hasDuplicate:error:"
+ "hasExistingSingletonTypeInContext:hasExisting:error:"
+ "hidden"
+ "implicit"
+ "isSupervised"
+ "loaded"
+ "mdmProfileIdentifier"
+ "migrateWithCoreDataReturningError:"
+ "migrationSupervised"
+ "not loaded"
+ "once"
+ "storeHelper"
+ "supervised"
+ "undefined"
+ "validStatusForStoreIdentifier:declarationIdentifier:serverToken:"
- "-"
- "A management source for %{public}@ already exists"
- "Finished migrate on startup"
- "Migration failed - process exiting: %{public}@"
- "Unable to fetch device management source objects: %{public}@"
- "_actions"
- "memberQueueManagingProfileIdentifier"
- "refreshDetailsFromDisk"
- "sharedConfiguration"

```
