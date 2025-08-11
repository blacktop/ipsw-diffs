## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-2026.0.2.0.0
-  __TEXT.__text: 0x77c00
+2026.0.2.1.1
+  __TEXT.__text: 0x78464
   __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_methlist: 0x5f44
+  __TEXT.__objc_methlist: 0x60ac
   __TEXT.__const: 0x868
-  __TEXT.__cstring: 0x6551
-  __TEXT.__gcc_except_tab: 0x2470
-  __TEXT.__oslogstring: 0x8edd
+  __TEXT.__cstring: 0x6571
+  __TEXT.__gcc_except_tab: 0x2450
+  __TEXT.__oslogstring: 0x901d
   __TEXT.__swift5_typeref: 0x2f7
   __TEXT.__swift5_capture: 0x24
   __TEXT.__constg_swiftt: 0x180

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x28
-  __TEXT.__unwind_info: 0x1f28
+  __TEXT.__unwind_info: 0x1f60
   __TEXT.__eh_frame: 0x438
-  __TEXT.__objc_classname: 0xbce
-  __TEXT.__objc_methname: 0x1176c
-  __TEXT.__objc_methtype: 0x219b
-  __TEXT.__objc_stubs: 0xa740
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x2748
-  __DATA_CONST.__objc_classlist: 0x228
+  __TEXT.__objc_classname: 0xc7e
+  __TEXT.__objc_methname: 0x11a6c
+  __TEXT.__objc_methtype: 0x2260
+  __TEXT.__objc_stubs: 0xa7c0
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__const: 0x2720
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3750
-  __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x37a8
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xc08
   __AUTH_CONST.__const: 0xcb8
-  __AUTH_CONST.__cfstring: 0x2c40
-  __AUTH_CONST.__objc_const: 0x11490
+  __AUTH_CONST.__cfstring: 0x2c60
+  __AUTH_CONST.__objc_const: 0x12050
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x280
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x710
-  __DATA.__data: 0xf68
-  __DATA.__bss: 0xdf0
+  __DATA.__objc_ivar: 0x720
+  __DATA.__data: 0x1088
+  __DATA.__bss: 0xe20
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__data: 0x198
   __DATA_DIRTY.__bss: 0xe8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C5E7C0EE-0A52-3C10-A23C-209DEE09F17F
-  Functions: 2795
-  Symbols:   9091
-  CStrings:  4147
+  UUID: 618813A2-AE23-30DF-87F4-4EA9B0D8B96B
+  Functions: 2823
+  Symbols:   9199
+  CStrings:  4182
 
Symbols:
+ +[ACHEarnedInstanceEntity journalEntryAppliedObserver]
+ +[ACHEarnedInstanceEntity receiveSyncObjects:version:syncStore:profile:error:].cold.2
+ +[ACHEarnedInstanceEntity setJournalEntryAppliedObserver:]
+ +[ACHEarnedInstanceEntity setSyncedEarnedInstancesObserver:]
+ +[ACHEarnedInstanceEntity syncedEarnedInstancesObserver]
+ +[ACHTemplateEntity setSyncedTemplatesObserver:]
+ +[ACHTemplateEntity syncedTemplatesObserver]
+ -[ACHEarnedInstanceEntityWrapper .cxx_destruct]
+ -[ACHEarnedInstanceEntityWrapper allEarnedInstancesWithError:]
+ -[ACHEarnedInstanceEntityWrapper earnedInstanceEntityDidReceiveSyncedEarnedInstances:provenance:]
+ -[ACHEarnedInstanceEntityWrapper earnedInstanceEntityDidReceiveSyncedEarnedInstances:provenance:].cold.1
+ -[ACHEarnedInstanceEntityWrapper earnedInstancesForDateComponents:error:]
+ -[ACHEarnedInstanceEntityWrapper earnedInstancesForTemplateUniqueName:error:]
+ -[ACHEarnedInstanceEntityWrapper initWithProfile:]
+ -[ACHEarnedInstanceEntityWrapper insertEarnedInstances:provenance:databaseContext:error:]
+ -[ACHEarnedInstanceEntityWrapper profile]
+ -[ACHEarnedInstanceEntityWrapper removeAllEarnedInstancesWithError:]
+ -[ACHEarnedInstanceEntityWrapper removeEarnedInstances:error:]
+ -[ACHEarnedInstanceEntityWrapper removeEarnedInstancesForTemplateUniqueName:error:]
+ -[ACHEarnedInstanceEntityWrapper setProfile:]
+ -[ACHEarnedInstanceEntityWrapper setSyncedEarnedInstancesObserver:]
+ -[ACHEarnedInstanceEntityWrapper syncedEarnedInstancesObserver]
+ -[ACHTemplateEntityWrapper .cxx_destruct]
+ -[ACHTemplateEntityWrapper allTemplatesWithError:]
+ -[ACHTemplateEntityWrapper initWithProfile:]
+ -[ACHTemplateEntityWrapper insertTemplates:provenance:databaseContext:error:]
+ -[ACHTemplateEntityWrapper profile]
+ -[ACHTemplateEntityWrapper removeTemplates:error:]
+ -[ACHTemplateEntityWrapper setProfile:]
+ -[ACHTemplateEntityWrapper setSyncedTemplatesObserver:]
+ -[ACHTemplateEntityWrapper syncedTemplatesObserver]
+ -[ACHTemplateEntityWrapper templateEntityDidReceiveSyncedTemplates:provenance:]
+ -[ACHTemplateEntityWrapper templateEntityDidReceiveSyncedTemplates:provenance:].cold.1
+ GCC_except_table61
+ _ACHRequestAwardsProfileExtensionWithError
+ _ACHRequestAwardsProfileExtensionWithError.cold.1
+ _OBJC_CLASS_$_ACHEarnedInstanceEntityWrapper
+ _OBJC_CLASS_$_ACHTemplateEntityWrapper
+ _OBJC_IVAR_$_ACHEarnedInstanceEntityWrapper._profile
+ _OBJC_IVAR_$_ACHEarnedInstanceEntityWrapper._syncedEarnedInstancesObserver
+ _OBJC_IVAR_$_ACHTemplateEntityWrapper._profile
+ _OBJC_IVAR_$_ACHTemplateEntityWrapper._syncedTemplatesObserver
+ _OBJC_METACLASS_$_ACHEarnedInstanceEntityWrapper
+ _OBJC_METACLASS_$_ACHTemplateEntityWrapper
+ __OBJC_$_INSTANCE_METHODS_ACHEarnedInstanceEntityWrapper
+ __OBJC_$_INSTANCE_METHODS_ACHTemplateEntityWrapper
+ __OBJC_$_INSTANCE_VARIABLES_ACHEarnedInstanceEntityWrapper
+ __OBJC_$_INSTANCE_VARIABLES_ACHTemplateEntityWrapper
+ __OBJC_$_PROP_LIST_ACHEarnedInstanceEntityWrapper
+ __OBJC_$_PROP_LIST_ACHTemplateEntityWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHEarnedInstanceEntitySyncedEarnedInstancesObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHTemplateEntitySyncedTemplatesObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACHEarnedInstanceEntitySyncedEarnedInstancesObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACHTemplateEntitySyncedTemplatesObserver
+ __OBJC_$_PROTOCOL_REFS_ACHAwardsProfileExtending
+ __OBJC_$_PROTOCOL_REFS_ACHEarnedInstanceEntitySyncedEarnedInstancesObserver
+ __OBJC_$_PROTOCOL_REFS_ACHTemplateEntitySyncedTemplatesObserver
+ __OBJC_CLASS_PROTOCOLS_$_ACHEarnedInstanceEntityWrapper
+ __OBJC_CLASS_PROTOCOLS_$_ACHTemplateEntityWrapper
+ __OBJC_CLASS_RO_$_ACHEarnedInstanceEntityWrapper
+ __OBJC_CLASS_RO_$_ACHTemplateEntityWrapper
+ __OBJC_LABEL_PROTOCOL_$_ACHAwardsProfileExtending
+ __OBJC_LABEL_PROTOCOL_$_ACHEarnedInstanceEntitySyncedEarnedInstancesObserver
+ __OBJC_LABEL_PROTOCOL_$_ACHTemplateEntitySyncedTemplatesObserver
+ __OBJC_METACLASS_RO_$_ACHEarnedInstanceEntityWrapper
+ __OBJC_METACLASS_RO_$_ACHTemplateEntityWrapper
+ __OBJC_PROTOCOL_$_ACHAwardsProfileExtending
+ __OBJC_PROTOCOL_$_ACHEarnedInstanceEntitySyncedEarnedInstancesObserver
+ __OBJC_PROTOCOL_$_ACHTemplateEntitySyncedTemplatesObserver
+ __OBJC_PROTOCOL_REFERENCE_$_ACHAwardsProfileExtending
+ __journalEntryAppliedObserver
+ __syncObserver
+ _journalAppliedObserverLock
+ _objc_msgSend$earnedInstanceEntityDidApplyJournalEntriesInsertedEarnedInstances:removedEarnedInstances:
+ _objc_msgSend$earnedInstanceEntityDidReceiveSyncedEarnedInstances:provenance:
+ _objc_msgSend$profileExtensionsConformingToProtocol:
+ _objc_msgSend$setSyncedEarnedInstancesObserver:
+ _objc_msgSend$setSyncedTemplatesObserver:
+ _objc_msgSend$syncedEarnedInstancesObserver
+ _objc_msgSend$syncedTemplatesObserver
+ _objc_msgSend$templateEntityDidReceiveSyncedTemplates:provenance:
+ _syncObserverLock
- +[ACHEarnedInstanceDuplicateUtility earnedInstancesAreDuplicate:otherEarnedInstance:template:calendar:firstDayOfWeek:]
- +[ACHEarnedInstanceEntity _shouldKeepEarnedInstanceForInsert:withProfile:templateCache:calendar:firstDayOfWeek:]
- +[ACHEarnedInstanceEntity _templateForEarnedInstance:withProfile:templateCache:]
- +[ACHEarnedInstanceEntity _templateForEarnedInstance:withProfile:templateCache:].cold.1
- +[ACHTemplateEntity templateWithName:profile:error:]
- _ACHEarnedInstancesAreDuplicates
- __OBJC_$_CLASS_METHODS_ACHEarnedInstanceDuplicateUtility
- ___52+[ACHTemplateEntity templateWithName:profile:error:]_block_invoke
- ___block_descriptor_64_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lr48l8s32l8s40l8
- _objc_msgSend$_shouldKeepEarnedInstanceForInsert:withProfile:templateCache:calendar:firstDayOfWeek:
- _objc_msgSend$_templateForEarnedInstance:withProfile:templateCache:
- _objc_msgSend$earnedInstancesAreDuplicate:otherEarnedInstance:template:calendar:firstDayOfWeek:
- _objc_msgSend$templateWithName:profile:error:
CStrings:
+ "@\"<ACHEarnedInstanceEntitySyncedEarnedInstancesObserver>\""
+ "@\"<ACHTemplateEntitySyncedTemplatesObserver>\""
+ "@48@0:8@16q24@32^@40"
+ "ACHAwardsProfileExtending"
+ "ACHEarnedInstanceEntitySyncedEarnedInstancesObserver"
+ "ACHEarnedInstanceEntityWrapper"
+ "ACHTemplateEntitySyncedTemplatesObserver"
+ "ACHTemplateEntityWrapper"
+ "Activity Awards plugin is nil"
+ "B32@0:8@\"NSArray\"16q24"
+ "B32@0:8@16q24"
+ "B48@0:8@16q24@32^@40"
+ "Decoded %{public}@ earned instances from sync."
+ "Earned Instance Entity Wrapper got notified about newly synced earned instances, passing that along to syncedEarnedInstancesObserver (%@)"
+ "Earned Instance Entity received sync objects and sync observer is set, passing to sync observer"
+ "Earned Instance Entity received sync objects, but no sync observer is registered yet. Writing directly to database."
+ "Earned instance entity sync received failed (doesn't fail sync though)"
+ "Error directly applying earned instance sync objects to database (doesn't fail sync though): %{public}@"
+ "Received zero decodable earned instances from sync, nothing to do."
+ "T@\"<ACHEarnedInstanceEntityJournalEntryAppliedObserver>\",W,N"
+ "T@\"<ACHEarnedInstanceEntitySyncedEarnedInstancesObserver>\",W,N"
+ "T@\"<ACHEarnedInstanceEntitySyncedEarnedInstancesObserver>\",W,N,V_syncedEarnedInstancesObserver"
+ "T@\"<ACHTemplateEntitySyncedTemplatesObserver>\",W,N"
+ "T@\"<ACHTemplateEntitySyncedTemplatesObserver>\",W,N,V_syncedTemplatesObserver"
+ "Template Entity Wrapper got notified about newly synced templates, passing that along to syncedTemplatesObserver (%@)"
+ "_syncedEarnedInstancesObserver"
+ "_syncedTemplatesObserver"
+ "allEarnedInstancesWithError:"
+ "allTemplatesWithError:"
+ "earnedInstanceEntityDidApplyJournalEntriesInsertedEarnedInstances:removedEarnedInstances:"
+ "earnedInstanceEntityDidReceiveSyncedEarnedInstances:provenance:"
+ "earnedInstancesForDateComponents:error:"
+ "insertEarnedInstances:provenance:databaseContext:error:"
+ "insertTemplates:provenance:databaseContext:error:"
+ "journalEntryAppliedObserver"
+ "profileExtensionsConformingToProtocol:"
+ "setJournalEntryAppliedObserver:"
+ "setSyncedEarnedInstancesObserver:"
+ "setSyncedTemplatesObserver:"
+ "syncedEarnedInstancesObserver"
+ "syncedTemplatesObserver"
+ "templateEntityDidReceiveSyncedTemplates:provenance:"
+ "v32@0:8@\"NSArray\"16q24"
+ "v32@0:8@16q24"
- "B56@0:8@16@24@32@40q48"
- "Decoded %{public}@ earned instances from sync, saving to database."
- "Error inserting earned instance sync objects to database (doesn't fail sync though): %{public}@"
- "Error loading template (%@) from database applying earned instance: %@"
- "Received zero decodable earned instances or all duplicates/beyond earn limit count from sync, nothing to do."
- "Synced earned instance is duplicate, dropping: %@"
- "Synced earned instance would exceed earned count limit, dropping: %@"
- "_shouldKeepEarnedInstanceForInsert:withProfile:templateCache:calendar:firstDayOfWeek:"
- "_templateForEarnedInstance:withProfile:templateCache:"
- "earnedInstancesAreDuplicate:otherEarnedInstance:template:calendar:firstDayOfWeek:"
- "templateWithName:profile:error:"

```
