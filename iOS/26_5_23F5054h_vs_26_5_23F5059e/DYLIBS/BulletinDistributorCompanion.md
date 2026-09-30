## BulletinDistributorCompanion

> `/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion`

```diff

-381.4.9.0.0
-  __TEXT.__text: 0x8e540
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0xa1c4
-  __TEXT.__cstring: 0x43a7
-  __TEXT.__const: 0x622
+381.4.12.0.0
+  __TEXT.__text: 0x91d34
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0xa264
+  __TEXT.__cstring: 0x43e7
+  __TEXT.__const: 0x682
   __TEXT.__gcc_except_tab: 0x944
-  __TEXT.__oslogstring: 0x6136
+  __TEXT.__oslogstring: 0x63b5
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x12f
+  __TEXT.__swift5_typeref: 0x14b
+  __TEXT.__swift5_capture: 0x3c
   __TEXT.__swift5_fieldmd: 0x84
-  __TEXT.__constg_swiftt: 0xc8
+  __TEXT.__constg_swiftt: 0xd8
   __TEXT.__swift5_reflstr: 0x50
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x2700
-  __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1779
-  __TEXT.__objc_methname: 0x1430d
-  __TEXT.__objc_methtype: 0x3a2e
-  __TEXT.__objc_stubs: 0xd300
-  __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0x1ec0
-  __DATA_CONST.__objc_classlist: 0x4c8
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0x27f0
+  __TEXT.__eh_frame: 0x330
+  __TEXT.__objc_classname: 0x17a9
+  __TEXT.__objc_methname: 0x14393
+  __TEXT.__objc_methtype: 0x3a58
+  __TEXT.__objc_stubs: 0xd360
+  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__const: 0x1ed8
+  __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4740
+  __DATA_CONST.__objc_selrefs: 0x4758
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x3f8
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x3fe0
-  __AUTH_CONST.__objc_const: 0x19eb8
+  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__const: 0x730
+  __AUTH_CONST.__cfstring: 0x4000
+  __AUTH_CONST.__objc_const: 0x1a4e0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2f28
+  __AUTH.__objc_data: 0x2f78
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0xad8
-  __DATA.__data: 0x1250
+  __DATA.__objc_ivar: 0xaec
+  __DATA.__data: 0x1260
   __DATA.__bss: 0x4e0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 55A32FAA-27AF-3515-AFEE-E9AEBA384F7A
-  Functions: 3850
-  Symbols:   12572
-  CStrings:  5590
+  UUID: 6129B273-D6B6-3DB4-8EC3-A7C5FCB7D7A4
+  Functions: 3893
+  Symbols:   12646
+  CStrings:  5608
 
Symbols:
+ -[BLTSectionInfoListAccessorySettingsProvider _providerForSetting:]
+ -[BLTSectionInfoListAccessorySettingsProvider initWithEnabledProvider:disabledProvider:enableAllProvider:forwardingSettingsProvider:syncDelegate:stateStorageDirectory:]
+ -[BLTSectionInfoListEnableAllProvider .cxx_destruct]
+ -[BLTSectionInfoListEnableAllProvider _enabledOverrideForSectionID:timestamp:]
+ -[BLTSectionInfoListEnableAllProvider delegate]
+ -[BLTSectionInfoListEnableAllProvider initWithSettingsGateway:]
+ -[BLTSectionInfoListEnableAllProvider reloadWithCompletion:]
+ -[BLTSectionInfoListEnableAllProvider sectionInfoObserver:removedSectionWithSectionID:transaction:]
+ -[BLTSectionInfoListEnableAllProvider sectionInfoObserver:updatedSectionInfoForSectionIDs:transaction:]
+ -[BLTSectionInfoListEnableAllProvider setDelegate:]
+ -[BLTUserDefaultsNotificationForwardingSettingsProvider noteForwardingDisabledForApplication:]
+ _OBJC_CLASS_$_BLTSectionInfoListEnableAllProvider
+ _OBJC_IVAR_$_BLTSectionInfoListAccessorySettingsProvider._enableAllProvider
+ _OBJC_IVAR_$_BLTSectionInfoListEnableAllProvider._delegate
+ _OBJC_IVAR_$_BLTSectionInfoListEnableAllProvider._observer
+ _OBJC_IVAR_$_BLTSectionInfoListEnableAllProvider._queue
+ _OBJC_IVAR_$_BLTSettingSync._enableAllProvider
+ _OBJC_METACLASS_$_BLTSectionInfoListEnableAllProvider
+ __OBJC_$_INSTANCE_METHODS_BLTSectionInfoListEnableAllProvider
+ __OBJC_$_INSTANCE_VARIABLES_BLTSectionInfoListEnableAllProvider
+ __OBJC_$_PROP_LIST_BLTSectionInfoListEnableAllProvider
+ __OBJC_CLASS_PROTOCOLS_$_BLTSectionInfoListEnableAllProvider
+ __OBJC_CLASS_RO_$_BLTSectionInfoListEnableAllProvider
+ __OBJC_METACLASS_RO_$_BLTSectionInfoListEnableAllProvider
+ __PROTOCOLS_BLTAccessoryNotificationsForwardingSettingsProvider.5
+ ___103-[BLTSectionInfoListEnableAllProvider sectionInfoObserver:updatedSectionInfoForSectionIDs:transaction:]_block_invoke
+ ___35-[BLTSettingSync _spoolInitialSync]_block_invoke.57
+ ___44-[BLTSettingSync requestSectionInfoFullSync]_block_invoke.92
+ ___57-[BLTSettingSync makeAuthorizationPermanentForSectionID:]_block_invoke.86
+ ___60-[BLTSectionInfoListEnableAllProvider reloadWithCompletion:]_block_invoke
+ ___60-[BLTSectionInfoListEnableAllProvider reloadWithCompletion:]_block_invoke_2
+ ___60-[BLTSettingSync performInitialSyncWithProgress:completion:]_block_invoke.45
+ ___60-[BLTSettingSync performInitialSyncWithProgress:completion:]_block_invoke_2.46
+ ___65-[BLTSettingSync _sendSyncSupportedAppListWithInstalled:removed:]_block_invoke.62
+ ___65-[BLTSettingSync _sendSyncSupportedAppListWithInstalled:removed:]_block_invoke.67
+ ___65-[BLTSettingSync _sendSyncSupportedAppListWithInstalled:removed:]_block_invoke_2.68
+ ___72-[BLTSettingSync sendSectionInfosWithSectionIDs:completion:spoolToFile:]_block_invoke.79
+ ___78-[BLTSettingSync _updateAllBBSectionsWithCompletion:withProgress:spoolToFile:]_block_invoke.74
+ ___78-[BLTSettingSync _updateAllBBSectionsWithCompletion:withProgress:spoolToFile:]_block_invoke.76
+ ___78-[BLTSettingSync _updateAllBBSectionsWithCompletion:withProgress:spoolToFile:]_block_invoke_2.77
+ ___78-[BLTSettingSync performSyncIfNeededForSectionID:gizmoSectionInfo:completion:]_block_invoke.51
+ ___99-[BLTSectionInfoListEnableAllProvider sectionInfoObserver:removedSectionWithSectionID:transaction:]_block_invoke
+ ___block_literal_global.66
+ ___block_literal_global.81
+ ___block_literal_global.83
+ ___block_literal_global.94
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _get_type_metadata 15Synchronization5MutexVy28BulletinDistributorCompanion48AccessoryNotificationsForwardingSettingsProviderC11RecordStateOG noncopyable.7
+ _get_type_metadata 15Synchronization5MutexVyytG noncopyable.8
+ _objc_msgSend$_enabledOverrideForSectionID:timestamp:
+ _objc_msgSend$_providerForSetting:
+ _objc_msgSend$initWithEnabledProvider:disabledProvider:enableAllProvider:forwardingSettingsProvider:syncDelegate:stateStorageDirectory:
+ _objc_msgSend$noteForwardingDisabledForApplication:
+ _swift_beginAccess
+ _swift_deallocObject
+ _swift_endAccess
+ _swift_retain
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _symbolic SS
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ytIeAgHr_
- -[BLTSectionInfoListAccessorySettingsProvider initWithEnabledProvider:disabledProvider:forwardingSettingsProvider:syncDelegate:stateStorageDirectory:]
- __PROTOCOLS_BLTAccessoryNotificationsForwardingSettingsProvider.2
- ___35-[BLTSettingSync _spoolInitialSync]_block_invoke.56
- ___44-[BLTSettingSync requestSectionInfoFullSync]_block_invoke.90
- ___57-[BLTSettingSync makeAuthorizationPermanentForSectionID:]_block_invoke.85
- ___60-[BLTSettingSync performInitialSyncWithProgress:completion:]_block_invoke.44
- ___60-[BLTSettingSync performInitialSyncWithProgress:completion:]_block_invoke_2.45
- ___65-[BLTSettingSync _sendSyncSupportedAppListWithInstalled:removed:]_block_invoke.61
- ___65-[BLTSettingSync _sendSyncSupportedAppListWithInstalled:removed:]_block_invoke.66
- ___65-[BLTSettingSync _sendSyncSupportedAppListWithInstalled:removed:]_block_invoke_2.67
- ___72-[BLTSettingSync sendSectionInfosWithSectionIDs:completion:spoolToFile:]_block_invoke.78
- ___78-[BLTSettingSync _updateAllBBSectionsWithCompletion:withProgress:spoolToFile:]_block_invoke.73
- ___78-[BLTSettingSync _updateAllBBSectionsWithCompletion:withProgress:spoolToFile:]_block_invoke.75
- ___78-[BLTSettingSync _updateAllBBSectionsWithCompletion:withProgress:spoolToFile:]_block_invoke_2.76
- ___78-[BLTSettingSync performSyncIfNeededForSectionID:gizmoSectionInfo:completion:]_block_invoke.50
- ___block_literal_global.65
- ___block_literal_global.80
- _get_type_metadata 15Synchronization5MutexVy28BulletinDistributorCompanion48AccessoryNotificationsForwardingSettingsProviderC11RecordStateOG noncopyable.4
- _get_type_metadata 15Synchronization5MutexVyytG noncopyable.5
- _objc_msgSend$initWithEnabledProvider:disabledProvider:forwardingSettingsProvider:syncDelegate:stateStorageDirectory:
CStrings:
+ "@\"BLTSectionInfoListEnableAllProvider\""
+ "@64@0:8@16@24@32@40@48@56"
+ "BLTSectionInfoListEnableAllProvider"
+ "BLTSectionInfoListEnableAllProvider: applying enabled override for %@"
+ "BLTSectionInfoListEnableAllProvider: reloaded with %lu enabled overrides"
+ "BLTSectionInfoListEnableAllProvider: section removed %@"
+ "Failed to save forwardAll to limited transition: %{public}@"
+ "Noting forwarding disabled for application: %{public}s while in forwardAll - transitioning to limited"
+ "Q1"
+ "Saved transition from forwardAll to limited: %{bool,public}d"
+ "_enableAllProvider"
+ "_enabledOverrideForSectionID:timestamp:"
+ "_providerForSetting:"
+ "com.apple.bulletindistributor.enableallprovider"
+ "forwardAll"
+ "initWithEnabledProvider:disabledProvider:enableAllProvider:forwardingSettingsProvider:syncDelegate:stateStorageDirectory:"
+ "noteForwardingDisabled: expected .allow policy but found %{public}s"
+ "noteForwardingDisabled: no accessory record found for pairingID"
+ "noteForwardingDisabled: no pairingID available"
+ "noteForwardingDisabledForApplication:"
- "@56@0:8@16@24@32@40@48"
- "A1"
- "initWithEnabledProvider:disabledProvider:forwardingSettingsProvider:syncDelegate:stateStorageDirectory:"

```
