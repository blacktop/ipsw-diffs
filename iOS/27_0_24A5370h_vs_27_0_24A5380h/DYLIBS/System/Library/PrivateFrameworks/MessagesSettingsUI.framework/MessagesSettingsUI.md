## MessagesSettingsUI

> `/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI`

```diff

-  __TEXT.__text: 0x33884
+  __TEXT.__text: 0x36018
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x63c
-  __TEXT.__objc_methlist: 0x163c
-  __TEXT.__const: 0x2554
-  __TEXT.__cstring: 0x1fb0
-  __TEXT.__gcc_except_tab: 0x98c
-  __TEXT.__oslogstring: 0x925
+  __TEXT.__objc_methlist: 0x16cc
+  __TEXT.__const: 0x26f4
+  __TEXT.__cstring: 0x20b0
+  __TEXT.__gcc_except_tab: 0x9d4
+  __TEXT.__oslogstring: 0xa65
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__constg_swiftt: 0x11c0
-  __TEXT.__swift5_typeref: 0x2e2c
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x906
+  __TEXT.__constg_swiftt: 0x1218
+  __TEXT.__swift5_typeref: 0x2e8c
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x986
   __TEXT.__swift5_assocty: 0x368
-  __TEXT.__swift5_proto: 0x108
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__swift5_fieldmd: 0x6d0
-  __TEXT.__swift5_capture: 0x164
+  __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift5_fieldmd: 0x71c
+  __TEXT.__swift5_capture: 0x198
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xdf8
-  __TEXT.__eh_frame: 0xbc
+  __TEXT.__unwind_info: 0xf00
+  __TEXT.__eh_frame: 0x18c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4d8
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e8
+  __DATA_CONST.__objc_selrefs: 0x1518
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x6c0
-  __AUTH_CONST.__const: 0xe38
-  __AUTH_CONST.__cfstring: 0x1540
-  __AUTH_CONST.__objc_const: 0x3170
+  __DATA_CONST.__got: 0x6e8
+  __AUTH_CONST.__const: 0xef8
+  __AUTH_CONST.__cfstring: 0x1560
+  __AUTH_CONST.__objc_const: 0x33a8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH.__objc_data: 0xaa0
-  __AUTH.__data: 0x1678
-  __DATA.__objc_ivar: 0xf0
-  __DATA.__data: 0xcac
-  __DATA.__bss: 0x2380
-  __DATA.__common: 0x40
+  __AUTH_CONST.__auth_got: 0xaf8
+  __AUTH.__objc_data: 0xbf0
+  __AUTH.__data: 0x16d0
+  __DATA.__objc_ivar: 0xf4
+  __DATA.__data: 0xd4c
+  __DATA.__bss: 0x2430
+  __DATA.__common: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1262
-  Symbols:   2582
-  CStrings:  514
+  Functions: 1343
+  Symbols:   2629
+  CStrings:  524
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[CKiCloudSettingsSyncController assetDownloadPresentableStatus]
+ -[CKiCloudSettingsSyncController cachedAttachmentDuration]
+ -[CKiCloudSettingsSyncController cachedSyncState]
+ -[CKiCloudSettingsSyncController notifySyncStatusHandlerWithStatusUpdate]
+ -[CKiCloudSettingsSyncController setCachedAttachmentDuration:]
+ -[CKiCloudSettingsSyncController setCachedSyncState:]
+ -[CKiCloudSettingsViewModel isAttachmentTimeRangeRequestInProgress]
+ -[CKiCloudSettingsViewModel priorAttachmentTimeRange]
+ -[CKiCloudSettingsViewModel setAttachmentTimeRangeRequestInProgress:]
+ GCC_except_table13
+ GCC_except_table40
+ GCC_except_table41
+ _OBJC_CLASS_$_CKAttachmentAssetDownloadPresentableStatus
+ _OBJC_CLASS_$__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ _OBJC_IVAR_$_CKiCloudSettingsSyncController._assetDownloadPresentableStatus
+ _OBJC_IVAR_$_CKiCloudSettingsSyncController._cachedAttachmentDuration
+ _OBJC_IVAR_$_CKiCloudSettingsSyncController._cachedSyncState
+ _OBJC_IVAR_$_CKiCloudSettingsViewModel._attachmentTimeRangeRequestInProgress
+ _OBJC_METACLASS_$_CKAttachmentAssetDownloadPresentableStatus
+ _OBJC_METACLASS_$__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ __DATA_CKAttachmentAssetDownloadPresentableStatus
+ __DATA__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ __INSTANCE_METHODS_CKAttachmentAssetDownloadPresentableStatus
+ __INSTANCE_METHODS__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ __IVARS_CKAttachmentAssetDownloadPresentableStatus
+ __IVARS__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ __METACLASS_DATA_CKAttachmentAssetDownloadPresentableStatus
+ __METACLASS_DATA__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ __PROPERTIES_CKAttachmentAssetDownloadPresentableStatus
+ __PROTOCOLS__TtC18MessagesSettingsUI27AttachmentDownloadViewModel
+ ___53-[CKiCloudSettingsViewModel priorAttachmentTimeRange]_block_invoke
+ ___53-[CKiCloudSettingsViewModel priorAttachmentTimeRange]_block_invoke_2
+ _objc_msgSend$assetDownloadPresentableStatus
+ _objc_msgSend$cachedAttachmentDuration
+ _objc_msgSend$cachedSyncState
+ _objc_msgSend$didFinishDownloadingAttachmentHistory
+ _objc_msgSend$fetchSyncState
+ _objc_msgSend$initWithSyncState:timeFrame:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$notifySyncStatusHandlerWithStatusUpdate
+ _objc_msgSend$phase
+ _objc_msgSend$priorAttachmentTimeRange
+ _objc_msgSend$remainingCount
+ _objc_msgSend$removeEventHandler:
+ _objc_msgSend$serverAttachmentTotalCount
+ _objc_msgSend$setCachedAttachmentDuration:
+ _objc_msgSend$setCachedSyncState:
+ _objc_retain_x27
+ _symbolic So19IMCloudKitSyncStateC
+ _symbolic So42CKAttachmentAssetDownloadPresentableStatusC
+ _symbolic _____ 18MessagesSettingsUI27AttachmentDownloadViewModelC
+ _symbolic _____ So41CKAttachmentAssetDownloadPresentablePhaseV
+ _symbolic _____SgXw 18MessagesSettingsUI27AttachmentDownloadViewModelC
+ _symbolic _____SgXwz_Xx 18MessagesSettingsUI27AttachmentDownloadViewModelC
- -[CKCloudSettingsViewController earliestKeptAttachmentDuration]
- -[CKCloudSettingsViewController isAttachmentTimeRangeRequestInProgress]
- -[CKCloudSettingsViewController setAttachmentTimeRangeRequestInProgress:]
- -[CKCloudSettingsViewController setEarliestKeptAttachmentDuration:]
- -[CKiCloudSettingsViewModel _attachmentDownloadTimeFrameDisplayString]
- -[CKiCloudSettingsViewModel cachedAttachmentDownloadTimeFrame]
- -[CKiCloudSettingsViewModel setCachedAttachmentDownloadTimeFrame:]
- GCC_except_table38
- GCC_except_table39
- _IMCloudKitGetSyncStateDictionary
- _OBJC_IVAR_$_CKCloudSettingsViewController._attachmentTimeRangeRequestInProgress
- _OBJC_IVAR_$_CKCloudSettingsViewController._earliestKeptAttachmentDuration
- _OBJC_IVAR_$_CKiCloudSettingsViewModel._cachedAttachmentDownloadTimeFrame
- ___80-[CKCloudSettingsViewController(SyncStateSpecifiers) _priorAttachmentTimeRange:]_block_invoke
- ___80-[CKCloudSettingsViewController(SyncStateSpecifiers) _priorAttachmentTimeRange:]_block_invoke_2
- _objc_msgSend$_attachmentDownloadTimeFrameDisplayString
- _objc_msgSend$accountHasiMessageEnabled
- _objc_msgSend$deselectRowAtIndexPath:animated:
- _objc_msgSend$earliestKeptAttachmentDuration
- _objc_msgSend$initWithAccountEnabled:stateDictionary:
- _objc_msgSend$setCachedAttachmentDownloadTimeFrame:
- _objc_msgSend$setChecked:
- _objc_msgSend$setEarliestKeptAttachmentDuration:
- _swift_dynamicCastObjCClass
- _symbolic _____SgXwz_Xx 18MessagesSettingsUI38CKDownloadAttachmentsDetailsControllerC
CStrings:
+ "Attachment download status update — phase=%ld, remaining=%ld, finished=%@, timeFrame=%ld"
+ "Attachment download status update — phase=%lu, remaining=%ld, finished=%{bool}d, timeFrame=%ld"
+ "Attachment download time frame changed: %ld -> %ld"
+ "MessagesSettingsUI.CKAttachmentAssetDownloadPresentableStatus"
+ "SYNC_ALL_ATTACHMENTS_DOWNLOADED"
+ "SYNC_BEFORE_ALL_BUTTON"
+ "SYNC_BEFORE_SHORT_N_DOWNLOADING"
+ "SYNC_DOWNLOADING_N_ATTACHMENTS"
+ "SYNC_PENDING_ATTACHMENT_DOWNLOAD"
+ "User tapped Download All Attachments"
+ "iCloudSettings_Messages"
- "\""
- "SYNC_BEFORE_N_DAYS"

```
