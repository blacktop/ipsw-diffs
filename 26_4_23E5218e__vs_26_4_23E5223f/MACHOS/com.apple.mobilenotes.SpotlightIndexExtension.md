## com.apple.mobilenotes.SpotlightIndexExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension`

```diff

-2952.100.23.0.0
-  __TEXT.__text: 0x2f34
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x14a
-  __TEXT.__cstring: 0x90
-  __TEXT.__oslogstring: 0x272
-  __TEXT.__objc_methname: 0x842
+2952.100.24.102.1
+  __TEXT.__text: 0x3bdc
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x188
+  __TEXT.__const: 0x15a
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x220
+  __TEXT.__objc_methname: 0xa02
+  __TEXT.__oslogstring: 0x454
   __TEXT.__objc_classname: 0x6e
-  __TEXT.__objc_methtype: 0x131
+  __TEXT.__objc_methtype: 0x151
   __TEXT.__swift5_typeref: 0xbf
   __TEXT.__swift5_reflstr: 0x47
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x218
-  __DATA.__objc_selrefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x260
+  __DATA.__objc_selrefs: 0x250
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x130
   __DATA.__data: 0xb0
   __DATA.__bss: 0x1a0

   - /System/Library/PrivateFrameworks/Notes.framework/Notes
   - /System/Library/PrivateFrameworks/NotesShared.framework/NotesShared
   - /System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 19777FF3-9039-3315-A689-89FBE712D552
-  Functions: 96
-  Symbols:   113
-  CStrings:  109
+  UUID: 6910E4B1-AF23-32BD-99F7-4845429F7BC2
+  Functions: 112
+  Symbols:   131
+  CStrings:  148
 
Symbols:
+ _ICPersistentContainerDidUnlockDatabaseNotification
+ _ICPersistentContainerWillLockDatabaseNotification
+ _NoteContextDidUnlockObjectCreationNotification
+ _NoteContextWillLockObjectCreationNotification
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ __Unwind_Resume
+ ___objc_personality_v0
+ __os_log_impl
+ _objc_alloc
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x9
+ _objc_storeStrong
- _objc_opt_class
CStrings:
+ "%s:%d"
+ "-[ICIndexRequestHandler noteContextDidUnlockObjectCreation:]"
+ "-[ICIndexRequestHandler noteContextWillLockObjectCreation:]"
+ "-[ICIndexRequestHandler persistentContainerDidUnlockDatabase:]"
+ "-[ICIndexRequestHandler persistentContainerWillLockDatabase:]"
+ "@\"RBSAssertion\""
+ "Error deleting all items before doing full reindex: %@. Will reindex nonetheless but manually delete progress state to prevent skipped updates"
+ "Finish Database-locking operation"
+ "Finish object creation-locking operation"
+ "FinishTaskInterruptable"
+ "Finishing database-locking operation"
+ "Finishing object creation-locking operation"
+ "Invalidated database-locking operation"
+ "Invalidated database-locking operation, error %@"
+ "Invalidated object creation-locking operation"
+ "Invalidated object creation-locking operation, error %@"
+ "Successfully deleted all index items before starting reindex."
+ "_databaseLockingBackgroundTask"
+ "_objectCreationLockingBackgroundTask"
+ "acquireWithInvalidationHandler:"
+ "addObserver:selector:name:object:"
+ "arrayWithObjects:count:"
+ "attributeWithDomain:name:"
+ "com.apple.common"
+ "currentProcess"
+ "forceDeleteAllProgressState"
+ "initWithExplanation:target:attributes:"
+ "invalidate"
+ "localizedDescription"
+ "noteContextDidUnlockObjectCreation:"
+ "noteContextWillLockObjectCreation:"
+ "persistentContainerDidUnlockDatabase:"
+ "persistentContainerWillLockDatabase:"
+ "setupSearchIndexers"
+ "v24@0:8@16"
+ "v24@?0@\"RBSAssertion\"8@\"NSError\"16"
- "initialize"

```
