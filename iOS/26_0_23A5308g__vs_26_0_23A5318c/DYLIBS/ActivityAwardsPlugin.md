## ActivityAwardsPlugin

> `/System/Library/Health/Plugins/ActivityAwardsPlugin.bundle/ActivityAwardsPlugin`

```diff

-2026.0.2.0.0
-  __TEXT.__text: 0x1030
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0x494
-  __TEXT.__oslogstring: 0x146
-  __TEXT.__cstring: 0x1e
-  __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0x13c
-  __TEXT.__objc_methname: 0x9f9
-  __TEXT.__objc_methtype: 0x489
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x20
+2026.0.2.1.1
+  __TEXT.__text: 0x16ec
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_methlist: 0x52c
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__oslogstring: 0x197
+  __TEXT.__cstring: 0x24
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_classname: 0x1e7
+  __TEXT.__objc_methname: 0xcf8
+  __TEXT.__objc_methtype: 0x531
+  __TEXT.__objc_stubs: 0x6c0
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x318
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__auth_got: 0x138
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xa00
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x420
+  __AUTH_CONST.__objc_const: 0xae0
+  __DATA.__objc_ivar: 0x24
+  __DATA.__data: 0x5a0
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7592E4E-DE9E-3E5B-8C43-4EF42DEF98BD
-  Functions: 39
-  Symbols:   73
-  CStrings:  190
+  UUID: BA8577C4-A3B7-3E31-8EE4-7051A5DAB8F0
+  Functions: 50
+  Symbols:   84
+  CStrings:  221
 
Symbols:
+ _ACHAwardsEarnedInstancesDidChangeNotification
+ _ACHAwardsTemplatesDidChangeNotification
+ _OBJC_CLASS_$_ACHEarnedInstanceEntityWrapper
+ _OBJC_CLASS_$_ACHTemplateEntityWrapper
+ _OBJC_CLASS_$_NSSet
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ _dispatch_sync
+ _objc_retain_x19
CStrings:
+ "@\"ACHEarnedInstanceEntityWrapper\""
+ "@\"ACHTemplateEntityWrapper\""
+ "ACHAwardsProfileExtending"
+ "ACHEarnedInstanceEntityJournalEntryAppliedObserver"
+ "ACHEarnedInstanceEntitySyncedEarnedInstancesObserver"
+ "ACHTemplateEntitySyncedTemplatesObserver"
+ "B32@0:8@\"NSArray\"16q24"
+ "B32@0:8@16q24"
+ "Error inserting synced earned instances: %@"
+ "Error inserting synced templates: %@"
+ "T@\"ACHEarnedInstanceEntityWrapper\",&,N,V_earnedInstanceEntityWrapper"
+ "T@\"ACHTemplateEntityWrapper\",&,N,V_templateEntityWrapper"
+ "_earnedInstanceEntityWrapper"
+ "_templateEntityWrapper"
+ "earnedInstanceEntityDidApplyJournalEntriesInsertedEarnedInstances:removedEarnedInstances:"
+ "earnedInstanceEntityDidReceiveSyncedEarnedInstances:provenance:"
+ "earnedInstanceEntityWrapper"
+ "initWithArray:"
+ "insertEarnedInstances:provenance:useLegacySyncIdentity:profile:databaseContext:error:"
+ "insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:"
+ "setEarnedInstanceEntityWrapper:"
+ "setJournalEntryAppliedObserver:"
+ "setSyncedEarnedInstancesObserver:"
+ "setSyncedTemplatesObserver:"
+ "setTemplateEntityWrapper:"
+ "templateEntityDidReceiveSyncedTemplates:provenance:"
+ "templateEntityWrapper"
+ "v32@0:8@\"NSArray\"16@\"NSArray\"24"
+ "v32@0:8@\"NSArray\"16q24"
+ "v32@0:8@16q24"
+ "v8@?0"

```
