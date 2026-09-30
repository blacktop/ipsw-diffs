## contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

-3654.0.0.0.0
-  __TEXT.__text: 0x10fd4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x2a00
-  __TEXT.__objc_methlist: 0xe98
-  __TEXT.__const: 0x14a
-  __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__objc_methname: 0x3932
-  __TEXT.__cstring: 0xec0
-  __TEXT.__objc_classname: 0x29a
-  __TEXT.__objc_methtype: 0xd09
+3656.0.0.0.0
+  __TEXT.__text: 0x12444
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x2e20
+  __TEXT.__objc_methlist: 0xf88
+  __TEXT.__const: 0x15a
+  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__objc_methname: 0x3dfc
+  __TEXT.__cstring: 0xf90
+  __TEXT.__objc_classname: 0x2e3
+  __TEXT.__objc_methtype: 0xe05
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__oslogstring: 0xc6e
+  __TEXT.__oslogstring: 0xe83
   __TEXT.__swift5_typeref: 0x54
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__info_plist: 0x415
-  __TEXT.__unwind_info: 0x590
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0xc18
-  __DATA_CONST.__cfstring: 0x640
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0xc58
+  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2630
-  __DATA.__objc_selrefs: 0xd70
-  __DATA.__objc_ivar: 0xec
-  __DATA.__objc_data: 0x668
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x170
+  __DATA.__objc_const: 0x2880
+  __DATA.__objc_selrefs: 0xea8
+  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_data: 0x6b8
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x180
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 500
-  Symbols:   206
-  CStrings:  866
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 530
+  Symbols:   224
+  CStrings:  936
 
Symbols:
+ _OBJC_CLASS_$_CNContainer
+ _OBJC_CLASS_$_CNLimitedAccessSyncData
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ __CFXPCCreateCFObjectFromXPCObject
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __xpc_type_dictionary
+ _objc_opt_self
+ _objc_retain_x26
+ _strcmp
+ _xpc_dictionary_get_value
+ _xpc_get_type
- _objc_retain_x27
CStrings:
+ "\x02"
+ "\x02\x1c"
+ ", "
+ "@\"ContactsService\"32@?0@\"<CNScheduler>\"8@\"<CNScheduler>\"16@\"NSXPCConnection\"24"
+ "@\"NSObject<OS_os_log>\""
+ "@48@0:8@?16@24@32@40"
+ "@48@0:8{?=[8I]}16"
+ "@64@0:8@16@24@32@40@48@56"
+ "CNContactStoreLimitedAccessDidChangeNotification"
+ "CNContactsDaemonApplicationUnregisteredListener"
+ "ContactProviderService"
+ "ContactProviderService"
+ "Did delete zombie provider containers"
+ "Failed to execute save request, error = %!@(MISSING)"
+ "Failed to fetch all provider containers, error = %!@(MISSING)"
+ "Full sync needed, drop all rows"
+ "PhoneSyncData"
+ "Registering for distnoted notifications."
+ "Registering for notifyd notifications."
+ "T@\"NSObject<OS_os_log>\",R,N,V_log"
+ "UserInfo"
+ "Will delete zombie provider container (%!{(MISSING)public}@) for unregistered app %!{(MISSING)public}@"
+ "_bestWorkQueueForAuditToken:"
+ "_log"
+ "allObjects"
+ "application unregistered bundle ids %!{(MISSING)public}@"
+ "applicationUnregisteredListeners"
+ "applyLimitedAccessSyncEvents success, save %!d(MISSING)"
+ "applyLimitedAccessSyncEvents:"
+ "applyLimitedAccessSyncEvents:withReply:"
+ "auditToken:allowsHighPriorityWithError:"
+ "bundleIDs"
+ "com.apple.LaunchServices.applicationUnregistered"
+ "com.apple.contactsd.ContactProviderService"
+ "com.apple.distnoted.matching"
+ "com.apple.distnoted.matching notification named com.apple.LaunchServices.applicationUnregistered"
+ "componentsSeparatedByString:"
+ "convertStringtoIntArray:"
+ "currentSequenceNumber"
+ "decodeObjectOfClass:forKey:"
+ "deleteContainer:"
+ "deletedContainers"
+ "dictionaryWithObjectsAndKeys:"
+ "dropAllLimitedAccesRows"
+ "dropAllLimitedAccesRowsWithReply:"
+ "encodeObject:forKey:"
+ "encodedData"
+ "finishEncoding"
+ "fullSyncRequired"
+ "fullSyncRequired %!d(MISSING) currentSequenceNumber %!d(MISSING)"
+ "getWatchLimitedAccessSyncDataStartingAtSequenceNumber:"
+ "getWatchLimitedAccessSyncDataStartingAtSequenceNumber:withReply:"
+ "handleBundleIdentifiers:"
+ "initForReadingFromData:error:"
+ "initRequiringSecureCoding:"
+ "initWithDataMapper:dataMapperConfiguration:workQueue:highPriorityWorkQueue:connection:accessAuthorization:"
+ "initWithSchedulerProvider:"
+ "initWithServiceProvider:schedulerProvider:highPrioritySchedulerProvider:tccServices:"
+ "initWithWorkQueue:highPriorityWorkQueue:connection:"
+ "intValue"
+ "invalidateCache"
+ "isPlaceholder"
+ "mutableCopy"
+ "numberWithInt:"
+ "predicateForContainersWithType:"
+ "providerIdentifier"
+ "purgeLimitedAccessRecordsForBundle:"
+ "purgeLimitedAccessRecordsForBundle:withReply:"
+ "sendSyncRequest, recieved response, update LimitedAccessTable"
+ "serviceError:"
+ "setLimitedAccessTableCurrentSequenceNumber:"
+ "setLimitedAccessTableCurrentSequenceNumber:withReply:"
+ "subscribeApplicationUnregisteredListeners"
+ "syncEvents"
+ "v24@0:8@\"NSArray\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"CNLimitedAccessSyncData\"@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "\x02\x1b"
- "@\"ContactsService\"24@?0@\"<CNScheduler>\"8@\"NSXPCConnection\"16"
- "@56@0:8@16@24@32@40@48"
- "Registering for notifications."
- "__ABLimitedAccessSyncTableUpdateNotification"
- "initWithDataMapper:dataMapperConfiguration:workQueue:connection:accessAuthorization:"
- "sendSyncRequest, recieved response, updateLimitedAccessTable"
- "updateLimitedAccessTable:"

```
