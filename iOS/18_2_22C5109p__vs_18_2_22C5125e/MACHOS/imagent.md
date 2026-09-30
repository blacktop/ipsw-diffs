## imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1402.300.129.2.15
-  __TEXT.__text: 0x467e4
-  __TEXT.__auth_stubs: 0x14e0
+1402.300.158.2.2
+  __TEXT.__text: 0x46d00
+  __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_stubs: 0x57e0
-  __TEXT.__objc_methlist: 0x1654
-  __TEXT.__const: 0x1014
+  __TEXT.__objc_methlist: 0x1658
+  __TEXT.__const: 0x1024
   __TEXT.__gcc_except_tab: 0x3bd8
-  __TEXT.__cstring: 0x1b7c
-  __TEXT.__oslogstring: 0x573b
-  __TEXT.__objc_methname: 0x98ba
+  __TEXT.__cstring: 0x1b9c
+  __TEXT.__oslogstring: 0x588b
+  __TEXT.__objc_methname: 0x98fa
   __TEXT.__objc_classname: 0x598
   __TEXT.__objc_methtype: 0x21ee
-  __TEXT.__swift5_typeref: 0x422
-  __TEXT.__swift5_fieldmd: 0x2a4
-  __TEXT.__constg_swiftt: 0x4b0
+  __TEXT.__swift5_typeref: 0x42c
+  __TEXT.__swift5_fieldmd: 0x2b0
+  __TEXT.__constg_swiftt: 0x4c0
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0x120
+  __TEXT.__swift5_capture: 0x130
   __TEXT.__swift5_proto: 0xac
   __TEXT.__swift5_types: 0x38
-  __TEXT.__swift5_reflstr: 0x338
+  __TEXT.__swift5_reflstr: 0x357
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x14b0
+  __TEXT.__unwind_info: 0x14b8
   __TEXT.__eh_frame: 0x500
-  __DATA_CONST.__auth_got: 0xa80
+  __DATA_CONST.__auth_got: 0xab0
   __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__auth_ptr: 0x2c8
-  __DATA_CONST.__const: 0x1288
+  __DATA_CONST.__auth_ptr: 0x2d8
+  __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x198

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x52e0
-  __DATA.__objc_selrefs: 0x2178
+  __DATA.__objc_const: 0x52e8
+  __DATA.__objc_selrefs: 0x2180
   __DATA.__objc_ivar: 0x44
-  __DATA.__objc_data: 0xae0
+  __DATA.__objc_data: 0xaf8
   __DATA.__data: 0x1200
   __DATA.__common: 0xe0
   __DATA.__bss: 0xf70

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync
+  - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 953
-  Symbols:   517
-  CStrings:  2141
+  Functions: 958
+  Symbols:   524
+  CStrings:  2148
 
Symbols:
+ _MobileInstallationWaitForSystemAppMigrationWithCompletion
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ _swift_deletedAsyncMethodErrorTu
+ _swift_getErrorValue
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
CStrings:
+ "22:25:55"
+ "Deleting %!s(MISSING) user defaults domain."
+ "Oct 29 2024"
+ "Performing launch tasks"
+ "Skipping launch tasks - still not past first unlock"
+ "Skipping launch tasks - system app migrator hasn't ran yet"
+ "Waiting for SystemAppMigration failed with error: %!s(MISSING)"
+ "Waiting for SystemAppMigration succeeded, resetting daemon shortly"
+ "We don't have to wait for any startup tasks - performing launch tasks now"
+ "completedSystemAppMigration"
+ "didPerformStartupTasks"
+ "movedMessagesToRecentlyDeletedForChatsWithGUIDs:queryID:deletionDate:"
+ "recoveredMessagesWithChatGUIDs:queryID:"
+ "removePersistentDomainForName:"
- "22:19:22"
- "Oct 20 2024"
- "We are unlocked - performing launch tasks now"
- "We have unlocked - performing launch tasks"
- "movedMessagesToRecentlyDeletedForChatsWithGUIDs:queryID:"
- "recoveredMessagesWithQueryID:"
- "removeSuiteNamed:"

```
