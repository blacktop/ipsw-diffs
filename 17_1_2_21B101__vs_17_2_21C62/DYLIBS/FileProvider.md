## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-1703.42.2.0.0
-  __TEXT.__text: 0x1186b0
-  __TEXT.__auth_stubs: 0x19b0
-  __TEXT.__objc_methlist: 0xb180
+1703.62.4.0.0
+  __TEXT.__text: 0x11b158
+  __TEXT.__auth_stubs: 0x19c0
+  __TEXT.__objc_methlist: 0xb840
   __TEXT.__const: 0x3b0
-  __TEXT.__gcc_except_tab: 0x7728
-  __TEXT.__cstring: 0x12233
-  __TEXT.__oslogstring: 0xc828
+  __TEXT.__gcc_except_tab: 0x778c
+  __TEXT.__cstring: 0x13246
+  __TEXT.__oslogstring: 0xc8cc
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x4e0c
-  __TEXT.__objc_classname: 0x1db7
-  __TEXT.__objc_methname: 0x1e747
-  __TEXT.__objc_methtype: 0x5b63
-  __TEXT.__objc_stubs: 0x127c0
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__const: 0x5bc8
-  __DATA_CONST.__objc_classlist: 0x620
+  __TEXT.__unwind_info: 0x4e7c
+  __TEXT.__objc_classname: 0x1e1e
+  __TEXT.__objc_methname: 0x20af0
+  __TEXT.__objc_methtype: 0x5bae
+  __TEXT.__objc_stubs: 0x129a0
+  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__const: 0x5c78
+  __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1f090
-  __DATA_CONST.__objc_selrefs: 0x5fb0
+  __DATA_CONST.__objc_const: 0x1fdd0
+  __DATA_CONST.__objc_selrefs: 0x6318
   __DATA_CONST.__objc_arraydata: 0xa98
-  __AUTH_CONST.__objc_const: 0x53e0
-  __AUTH_CONST.__cfstring: 0xed80
-  __AUTH_CONST.__const: 0x18a0
+  __AUTH_CONST.__objc_const: 0x5590
+  __AUTH_CONST.__cfstring: 0xfa60
+  __AUTH_CONST.__const: 0x1920
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0xce8
-  __AUTH.__objc_data: 0xa0
+  __AUTH_CONST.__auth_got: 0xcf0
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x10
   __DATA.__objc_protorefs: 0x128
-  __DATA.__objc_classrefs: 0x768
-  __DATA.__objc_superrefs: 0x4e0
-  __DATA.__objc_ivar: 0xe48
+  __DATA.__objc_classrefs: 0x788
+  __DATA.__objc_superrefs: 0x4f8
+  __DATA.__objc_ivar: 0xf30
   __DATA.__data: 0x21c8
-  __DATA.__bss: 0x2f0
+  __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x3ca0
   __DATA_DIRTY.__data: 0x2c0
   __DATA_DIRTY.__bss: 0x3d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6661
-  Symbols:   21204
-  CStrings:  9076
+  Functions: 6815
+  Symbols:   21634
+  CStrings:  9408
 
Symbols:
+ +[FPImportItemPendingReconciliation supportsSecureCoding]
+ +[FPImportItemPendingScanningDisk supportsSecureCoding]
+ +[FPImportItemPendingScanningProvider supportsSecureCoding]
+ -[FPExtensionEnumerationSettings isUnbounded]
+ -[FPExtensionEnumerationSettings setUnbounded:]
+ -[FPImportCookie description]
+ -[FPImportCookie providersWithOngoingImport]
+ -[FPImportCookieEntry creationTime]
+ -[FPImportCookieEntry description]
+ -[FPImportCookieEntry displayName]
+ -[FPImportCookieEntry initWithDomainPathRelativeToVolumeRoot:displayName:creationTime:andFileID:]
+ -[FPImportCookieEntry initWithDomainURL:displayName:error:]
+ -[FPImportCookieEntry setCreationTime:]
+ -[FPImportItemError diagnosticAttributes]
+ -[FPImportItemError setDiagnosticAttributes:]
+ -[FPImportItemPendingReconciliation .cxx_destruct]
+ -[FPImportItemPendingReconciliation diagnosticAttributes]
+ -[FPImportItemPendingReconciliation encodeWithCoder:]
+ -[FPImportItemPendingReconciliation initWithCoder:]
+ -[FPImportItemPendingReconciliation initWithItemIdentifier:]
+ -[FPImportItemPendingReconciliation itemIdentifier]
+ -[FPImportItemPendingReconciliation itemPendingReconciliationIsLockedInDB]
+ -[FPImportItemPendingReconciliation itemPendingReconciliationIsLocked]
+ -[FPImportItemPendingReconciliation itemPendingReconciliationJobBlockingCode]
+ -[FPImportItemPendingReconciliation itemPendingReconciliationJobCode]
+ -[FPImportItemPendingReconciliation itemPendingReconciliationJobSchedulingState]
+ -[FPImportItemPendingReconciliation json]
+ -[FPImportItemPendingReconciliation setDiagnosticAttributes:]
+ -[FPImportItemPendingReconciliation setItemIdentifier:]
+ -[FPImportItemPendingReconciliation setItemPendingReconciliationIsLocked:]
+ -[FPImportItemPendingReconciliation setItemPendingReconciliationIsLockedInDB:]
+ -[FPImportItemPendingReconciliation setItemPendingReconciliationJobBlockingCode:]
+ -[FPImportItemPendingReconciliation setItemPendingReconciliationJobCode:]
+ -[FPImportItemPendingReconciliation setItemPendingReconciliationJobSchedulingState:]
+ -[FPImportItemPendingScanningDisk .cxx_destruct]
+ -[FPImportItemPendingScanningDisk diagnosticAttributes]
+ -[FPImportItemPendingScanningDisk encodeWithCoder:]
+ -[FPImportItemPendingScanningDisk initWithCoder:]
+ -[FPImportItemPendingScanningDisk itemIdentifier]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskEnumerationStatus]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskHasMultiplePagesEnumeration]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingReconciliation]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingRejection]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingSyncDown]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent]
+ -[FPImportItemPendingScanningDisk itemPendingScanningDiskNumberOfChildrenPendingSyncUp]
+ -[FPImportItemPendingScanningDisk json]
+ -[FPImportItemPendingScanningDisk setDiagnosticAttributes:]
+ -[FPImportItemPendingScanningDisk setItemIdentifier:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskEnumerationStatus:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskHasMultiplePagesEnumeration:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingReconciliation:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingRejection:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingSyncDown:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingSyncUp:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:]
+ -[FPImportItemPendingScanningDisk setItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:]
+ -[FPImportItemPendingScanningProvider .cxx_destruct]
+ -[FPImportItemPendingScanningProvider diagnosticAttributes]
+ -[FPImportItemPendingScanningProvider encodeWithCoder:]
+ -[FPImportItemPendingScanningProvider initWithCoder:]
+ -[FPImportItemPendingScanningProvider itemIdentifier]
+ -[FPImportItemPendingScanningProvider itemPendingScanningProviderEnumerationStatus]
+ -[FPImportItemPendingScanningProvider itemPendingScanningProviderHasMultiplePagesEnumeration]
+ -[FPImportItemPendingScanningProvider itemPendingScanningProviderNumberOfChildrenFailingCreation]
+ -[FPImportItemPendingScanningProvider itemPendingScanningProviderNumberOfChildrenPendingCreation]
+ -[FPImportItemPendingScanningProvider itemPendingScanningProviderNumberOfChildren]
+ -[FPImportItemPendingScanningProvider itemPendingScanningProviderRemovalOfDatalessBitStatus]
+ -[FPImportItemPendingScanningProvider json]
+ -[FPImportItemPendingScanningProvider setDiagnosticAttributes:]
+ -[FPImportItemPendingScanningProvider setItemIdentifier:]
+ -[FPImportItemPendingScanningProvider setItemPendingScanningProviderEnumerationStatus:]
+ -[FPImportItemPendingScanningProvider setItemPendingScanningProviderHasMultiplePagesEnumeration:]
+ -[FPImportItemPendingScanningProvider setItemPendingScanningProviderNumberOfChildren:]
+ -[FPImportItemPendingScanningProvider setItemPendingScanningProviderNumberOfChildrenFailingCreation:]
+ -[FPImportItemPendingScanningProvider setItemPendingScanningProviderNumberOfChildrenPendingCreation:]
+ -[FPImportItemPendingScanningProvider setItemPendingScanningProviderRemovalOfDatalessBitStatus:]
+ -[FPImportProgressReport dbCreationTimestamp]
+ -[FPImportProgressReport init]
+ -[FPImportProgressReport isStreamResetRunning]
+ -[FPImportProgressReport itemsPendingReconciliation]
+ -[FPImportProgressReport itemsPendingScanningDisk]
+ -[FPImportProgressReport itemsPendingScanningProvider]
+ -[FPImportProgressReport latestFolderSelectedForImportIsMonitored]
+ -[FPImportProgressReport latestFolderSelectedForImportState]
+ -[FPImportProgressReport latestFolderSelectedForImportTimestamp]
+ -[FPImportProgressReport latestFolderSelectedForImportWasModifiedOnDisk]
+ -[FPImportProgressReport latestFolderSelectedForImportWasModifiedRemotely]
+ -[FPImportProgressReport latestFolderSelectedForImport]
+ -[FPImportProgressReport numberOfItemsPendingReconciliation]
+ -[FPImportProgressReport numberOfItemsPendingScanningDisk]
+ -[FPImportProgressReport numberOfItemsPendingScanningProvider]
+ -[FPImportProgressReport numberOfItemsPendingSelection]
+ -[FPImportProgressReport setDbCreationTimestamp:]
+ -[FPImportProgressReport setErrorDetails:]
+ -[FPImportProgressReport setIsStreamResetRunning:]
+ -[FPImportProgressReport setItemsPendingReconciliation:]
+ -[FPImportProgressReport setItemsPendingScanningDisk:]
+ -[FPImportProgressReport setItemsPendingScanningProvider:]
+ -[FPImportProgressReport setLatestFolderSelectedForImport:]
+ -[FPImportProgressReport setLatestFolderSelectedForImportIsMonitored:]
+ -[FPImportProgressReport setLatestFolderSelectedForImportState:]
+ -[FPImportProgressReport setLatestFolderSelectedForImportTimestamp:]
+ -[FPImportProgressReport setLatestFolderSelectedForImportWasModifiedOnDisk:]
+ -[FPImportProgressReport setLatestFolderSelectedForImportWasModifiedRemotely:]
+ -[FPImportProgressReport setNumberOfItemsInError:]
+ -[FPImportProgressReport setNumberOfItemsPendingReconciliation:]
+ -[FPImportProgressReport setNumberOfItemsPendingScanningDisk:]
+ -[FPImportProgressReport setNumberOfItemsPendingScanningProvider:]
+ -[FPImportProgressReport setNumberOfItemsPendingSelection:]
+ -[FPImportProgressReport setNumberOfItemsReconciled:]
+ -[FPImportProgressReport setStateOfDownloadJobs:]
+ -[FPImportProgressReport setStateOfOtherJobs:]
+ -[FPImportProgressReport setStateOfUploadJobs:]
+ -[FPImportProgressReport setStatus:]
+ -[FPImportProgressReport setXpcActivityDasdContext:]
+ -[FPImportProgressReport setXpcActivityIsActive:]
+ -[FPImportProgressReport setXpcActivityRegisteredWithDuet:]
+ -[FPImportProgressReport setXpcActivityTimeSinceLastActivation:]
+ -[FPImportProgressReport setXpcActivityTimeSinceLastRegistration:]
+ -[FPImportProgressReport stateOfDownloadJobs]
+ -[FPImportProgressReport stateOfOtherJobs]
+ -[FPImportProgressReport stateOfUploadJobs]
+ -[FPImportProgressReport xpcActivityDasdContext]
+ -[FPImportProgressReport xpcActivityIsActive]
+ -[FPImportProgressReport xpcActivityRegisteredWithDuet]
+ -[FPImportProgressReport xpcActivityTimeSinceLastActivation]
+ -[FPImportProgressReport xpcActivityTimeSinceLastRegistration]
+ -[NSFileProviderDiagnosticAttributesDescriptor copyWithZone:]
+ -[NSFileProviderItemVersion equivalentContentVersions]
+ -[NSFileProviderItemVersion equivalentMetadataVersions]
+ -[NSFileProviderItemVersion initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:]
+ -[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:]
+ -[NSURL(CopyFile) fp_volumeUsesAppleDouble:]
+ -[NSURL(CopyFile) fp_volumeUsesAppleDouble:].cold.1
+ -[_FPCopyFileStatus rootWasCopied]
+ -[_FPCopyFileStatus setRootWasCopied:]
+ -[_FPCopyFileStatus setShouldCopyAppleDouble:]
+ -[_FPCopyFileStatus shouldCopyAppleDouble]
+ _CFBooleanGetTypeID
+ _ExpirationInterval
+ _FPClearImportCookieForDomainURL
+ _FPClearImportCookieForDomainURL.cold.1
+ _FPGetImportCookieForURL
+ _FPIsImportingDomainsForUserURL
+ _FPIsImportingInVolumeAtURL
+ _FPPathRelativeToVolumeRoot
+ _FPWriteImportCookieForDomainURL
+ _FPWriteImportCookieForDomainURL.cold.1
+ _NSFileProviderInternalErrorProviderDisplayNamesKey
+ _NSURLVolumeTypeNameKey
+ _OBJC_CLASS_$_FPImportItemPendingReconciliation
+ _OBJC_CLASS_$_FPImportItemPendingScanningDisk
+ _OBJC_CLASS_$_FPImportItemPendingScanningProvider
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_IVAR_$_FPExtensionEnumerationSettings._unbounded
+ _OBJC_IVAR_$_FPImportCookieEntry._creationTime
+ _OBJC_IVAR_$_FPImportCookieEntry._displayName
+ _OBJC_IVAR_$_FPImportItemError._diagnosticAttributes
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._diagnosticAttributes
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._itemIdentifier
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._itemPendingReconciliationIsLocked
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._itemPendingReconciliationIsLockedInDB
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._itemPendingReconciliationJobBlockingCode
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._itemPendingReconciliationJobCode
+ _OBJC_IVAR_$_FPImportItemPendingReconciliation._itemPendingReconciliationJobSchedulingState
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._diagnosticAttributes
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemIdentifier
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskEnumerationStatus
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskHasMultiplePagesEnumeration
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingReconciliation
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingRejection
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingSyncDown
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingSyncUp
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion
+ _OBJC_IVAR_$_FPImportItemPendingScanningDisk._itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._diagnosticAttributes
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemIdentifier
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemPendingScanningProviderEnumerationStatus
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemPendingScanningProviderHasMultiplePagesEnumeration
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemPendingScanningProviderNumberOfChildren
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemPendingScanningProviderNumberOfChildrenFailingCreation
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemPendingScanningProviderNumberOfChildrenPendingCreation
+ _OBJC_IVAR_$_FPImportItemPendingScanningProvider._itemPendingScanningProviderRemovalOfDatalessBitStatus
+ _OBJC_IVAR_$_FPImportProgressReport._dbCreationTimestamp
+ _OBJC_IVAR_$_FPImportProgressReport._isStreamResetRunning
+ _OBJC_IVAR_$_FPImportProgressReport._itemsPendingReconciliation
+ _OBJC_IVAR_$_FPImportProgressReport._itemsPendingScanningDisk
+ _OBJC_IVAR_$_FPImportProgressReport._itemsPendingScanningProvider
+ _OBJC_IVAR_$_FPImportProgressReport._latestFolderSelectedForImport
+ _OBJC_IVAR_$_FPImportProgressReport._latestFolderSelectedForImportIsMonitored
+ _OBJC_IVAR_$_FPImportProgressReport._latestFolderSelectedForImportState
+ _OBJC_IVAR_$_FPImportProgressReport._latestFolderSelectedForImportTimestamp
+ _OBJC_IVAR_$_FPImportProgressReport._latestFolderSelectedForImportWasModifiedOnDisk
+ _OBJC_IVAR_$_FPImportProgressReport._latestFolderSelectedForImportWasModifiedRemotely
+ _OBJC_IVAR_$_FPImportProgressReport._numberOfItemsPendingReconciliation
+ _OBJC_IVAR_$_FPImportProgressReport._numberOfItemsPendingScanningDisk
+ _OBJC_IVAR_$_FPImportProgressReport._numberOfItemsPendingScanningProvider
+ _OBJC_IVAR_$_FPImportProgressReport._numberOfItemsPendingSelection
+ _OBJC_IVAR_$_FPImportProgressReport._stateOfDownloadJobs
+ _OBJC_IVAR_$_FPImportProgressReport._stateOfOtherJobs
+ _OBJC_IVAR_$_FPImportProgressReport._stateOfUploadJobs
+ _OBJC_IVAR_$_FPImportProgressReport._xpcActivityDasdContext
+ _OBJC_IVAR_$_FPImportProgressReport._xpcActivityIsActive
+ _OBJC_IVAR_$_FPImportProgressReport._xpcActivityRegisteredWithDuet
+ _OBJC_IVAR_$_FPImportProgressReport._xpcActivityTimeSinceLastActivation
+ _OBJC_IVAR_$_FPImportProgressReport._xpcActivityTimeSinceLastRegistration
+ _OBJC_IVAR_$_NSFileProviderItemVersion._equivalentContentVersions
+ _OBJC_IVAR_$_NSFileProviderItemVersion._equivalentMetadataVersions
+ _OBJC_IVAR_$__FPCopyFileStatus._rootWasCopied
+ _OBJC_IVAR_$__FPCopyFileStatus._shouldCopyAppleDouble
+ _OBJC_METACLASS_$_FPImportItemPendingReconciliation
+ _OBJC_METACLASS_$_FPImportItemPendingScanningDisk
+ _OBJC_METACLASS_$_FPImportItemPendingScanningProvider
+ __OBJC_$_CLASS_METHODS_FPImportItemPendingReconciliation
+ __OBJC_$_CLASS_METHODS_FPImportItemPendingScanningDisk
+ __OBJC_$_CLASS_METHODS_FPImportItemPendingScanningProvider
+ __OBJC_$_CLASS_PROP_LIST_FPImportItemPendingReconciliation
+ __OBJC_$_CLASS_PROP_LIST_FPImportItemPendingScanningDisk
+ __OBJC_$_CLASS_PROP_LIST_FPImportItemPendingScanningProvider
+ __OBJC_$_INSTANCE_METHODS_FPImportItemPendingReconciliation
+ __OBJC_$_INSTANCE_METHODS_FPImportItemPendingScanningDisk
+ __OBJC_$_INSTANCE_METHODS_FPImportItemPendingScanningProvider
+ __OBJC_$_INSTANCE_VARIABLES_FPImportItemPendingReconciliation
+ __OBJC_$_INSTANCE_VARIABLES_FPImportItemPendingScanningDisk
+ __OBJC_$_INSTANCE_VARIABLES_FPImportItemPendingScanningProvider
+ __OBJC_$_PROP_LIST_FPImportItemPendingReconciliation
+ __OBJC_$_PROP_LIST_FPImportItemPendingScanningDisk
+ __OBJC_$_PROP_LIST_FPImportItemPendingScanningProvider
+ __OBJC_CLASS_PROTOCOLS_$_FPImportItemPendingReconciliation
+ __OBJC_CLASS_PROTOCOLS_$_FPImportItemPendingScanningDisk
+ __OBJC_CLASS_PROTOCOLS_$_FPImportItemPendingScanningProvider
+ __OBJC_CLASS_RO_$_FPImportItemPendingReconciliation
+ __OBJC_CLASS_RO_$_FPImportItemPendingScanningDisk
+ __OBJC_CLASS_RO_$_FPImportItemPendingScanningProvider
+ __OBJC_METACLASS_RO_$_FPImportItemPendingReconciliation
+ __OBJC_METACLASS_RO_$_FPImportItemPendingScanningDisk
+ __OBJC_METACLASS_RO_$_FPImportItemPendingScanningProvider
+ ___110-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:]_block_invoke
+ ___110-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:]_block_invoke.cold.1
+ ___29-[FPImportCookie description]_block_invoke
+ ___30-[FPImportProgressReport json]_block_invoke_2
+ ___30-[FPImportProgressReport json]_block_invoke_3
+ ___30-[FPImportProgressReport json]_block_invoke_4
+ ___FPGetImportCookieForURL_block_invoke
+ ___block_descriptor_242_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_32_e18_16?0"NSObject"8l
+ ___block_descriptor_32_e41_16?0"FPImportItemPendingScanningDisk"8l
+ ___block_descriptor_32_e43_16?0"FPImportItemPendingReconciliation"8l
+ ___block_descriptor_32_e45_16?0"FPImportItemPendingScanningProvider"8l
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
+ ___block_literal_global.345
+ ___block_literal_global.354
+ ___block_literal_global.421
+ ___block_literal_global.493
+ ___block_literal_global.499
+ ___block_literal_global.505
+ ___block_literal_global.620
+ _copyfile_status_cb.cold.3
+ _copyfile_status_cb.cold.4
+ _copyfile_status_cb.cold.5
+ _fp_cachedTypeWithIdentifier:alreadyAvailableType:.hasFastSequenceNumber
+ _fp_cachedTypeWithIdentifier:alreadyAvailableType:.lastDatabaseGeneration
+ _objc_msgSend$creationTime
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:
+ _objc_msgSend$fp_volumeUsesAppleDouble:
+ _objc_msgSend$getKnowledgeUUID:andSequenceNumber:
+ _objc_msgSend$initWithDomainPathRelativeToVolumeRoot:displayName:creationTime:andFileID:
+ _objc_msgSend$initWithDomainURL:displayName:error:
+ _objc_msgSend$initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:
+ _objc_msgSend$isUnbounded
+ _objc_msgSend$providersWithOngoingImport
+ _objc_msgSend$rootWasCopied
+ _objc_msgSend$setCreationTime:
+ _objc_msgSend$setRootWasCopied:
+ _objc_msgSend$setShouldCopyAppleDouble:
+ _objc_msgSend$shouldCopyAppleDouble
- +[FPImportCookie clearCookieForDomainURL:error:]
- +[FPImportCookie clearCookieForDomainURL:error:].cold.1
- +[FPImportCookie isImportingDomainsForUserURL:]
- +[FPImportCookie isImportingInVolumeAtURL:]
- +[FPImportCookie writeCookieForDomainURL:error:]
- +[FPImportCookie writeCookieForDomainURL:error:].cold.1
- -[FPImportCookieEntry initWithDomainURL:error:]
- -[FPImportProgressReport initWithStatus:numberOfItemsReconciled:numberOfItemsInError:errorDetails:]
- _OBJC_IVAR_$_FPImportCookie.lastModificationDate
- ___88-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:completion:]_block_invoke
- ___88-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:completion:]_block_invoke.cold.1
- ___block_descriptor_241_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
- ___block_literal_global.342
- ___block_literal_global.351
- ___block_literal_global.418
- ___block_literal_global.490
- ___block_literal_global.617
- ___block_literal_global.73
- ___getStoredCookieForURL_block_invoke
- _getPathRelativeToVolumeRoot
- _getStoredCookieForURL
- _objc_msgSend$initWithContentVersion:metadataVersion:lastEditorDeviceName:
- _objc_msgSend$initWithDomainURL:error:
CStrings:
+ "._"
+ "1703.62.4"
+ "<%@: %@>"
+ "<n:%@ d:%@ f:%llu ct:%f>"
+ "@\"NSFileProviderDiagnosticAttributesDescriptor\""
+ "@16@?0@\"FPImportItemPendingReconciliation\"8"
+ "@16@?0@\"FPImportItemPendingScanningDisk\"8"
+ "@16@?0@\"FPImportItemPendingScanningProvider\"8"
+ "@16@?0@\"NSObject\"8"
+ "@48@0:8@16@24d32Q40"
+ "@56@0:8@16@24Q32B40B44@?48"
+ "A\xb3"
+ "FPImportItemPendingReconciliation"
+ "FPImportItemPendingScanningDisk"
+ "FPImportItemPendingScanningProvider"
+ "NSFileProviderInternalErrorProviderDisplayNamesKey"
+ "T@\"NSArray\",C,N,V_errorDetails"
+ "T@\"NSArray\",C,N,V_itemsPendingReconciliation"
+ "T@\"NSArray\",C,N,V_itemsPendingScanningDisk"
+ "T@\"NSArray\",C,N,V_itemsPendingScanningProvider"
+ "T@\"NSArray\",R,C,N,V_equivalentContentVersions"
+ "T@\"NSArray\",R,C,N,V_equivalentMetadataVersions"
+ "T@\"NSFileProviderDiagnosticAttributesDescriptor\",C,N,V_diagnosticAttributes"
+ "T@\"NSString\",C,N,V_itemIdentifier"
+ "T@\"NSString\",R,N,V_displayName"
+ "TB,N,GisUnbounded,V_unbounded"
+ "TB,N,V_isStreamResetRunning"
+ "TB,N,V_itemPendingReconciliationIsLocked"
+ "TB,N,V_itemPendingReconciliationIsLockedInDB"
+ "TB,N,V_itemPendingScanningDiskHasMultiplePagesEnumeration"
+ "TB,N,V_itemPendingScanningProviderHasMultiplePagesEnumeration"
+ "TB,N,V_latestFolderSelectedForImportIsMonitored"
+ "TB,N,V_latestFolderSelectedForImportWasModifiedOnDisk"
+ "TB,N,V_latestFolderSelectedForImportWasModifiedRemotely"
+ "TB,N,V_xpcActivityIsActive"
+ "TB,N,V_xpcActivityRegisteredWithDuet"
+ "TB,V_rootWasCopied"
+ "TB,V_shouldCopyAppleDouble"
+ "TQ,N,V_xpcActivityTimeSinceLastActivation"
+ "TQ,N,V_xpcActivityTimeSinceLastRegistration"
+ "Td,N,V_creationTime"
+ "Tq,N,V_dbCreationTimestamp"
+ "Tq,N,V_itemPendingReconciliationJobBlockingCode"
+ "Tq,N,V_itemPendingReconciliationJobCode"
+ "Tq,N,V_itemPendingReconciliationJobSchedulingState"
+ "Tq,N,V_itemPendingScanningDiskEnumerationStatus"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "Tq,N,V_itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "Tq,N,V_itemPendingScanningProviderEnumerationStatus"
+ "Tq,N,V_itemPendingScanningProviderNumberOfChildren"
+ "Tq,N,V_itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "Tq,N,V_itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "Tq,N,V_itemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "Tq,N,V_latestFolderSelectedForImport"
+ "Tq,N,V_latestFolderSelectedForImportState"
+ "Tq,N,V_latestFolderSelectedForImportTimestamp"
+ "Tq,N,V_numberOfItemsInError"
+ "Tq,N,V_numberOfItemsPendingReconciliation"
+ "Tq,N,V_numberOfItemsPendingScanningDisk"
+ "Tq,N,V_numberOfItemsPendingScanningProvider"
+ "Tq,N,V_numberOfItemsPendingSelection"
+ "Tq,N,V_numberOfItemsReconciled"
+ "Tq,N,V_stateOfDownloadJobs"
+ "Tq,N,V_stateOfOtherJobs"
+ "Tq,N,V_stateOfUploadJobs"
+ "Tq,N,V_status"
+ "Tq,N,V_xpcActivityDasdContext"
+ "[DEBUG] clearing import cookie for domain url %{public}@"
+ "[DEBUG] copyfile: %@ -> %@ AD-copy: %d"
+ "[DEBUG] copyfile: failed while copying an appledouble file %s, skipping error"
+ "[DEBUG] copyfile: skipping appledouble file %s"
+ "[DEBUG] writing import cookie for domain url %{public}@"
+ "[ERROR] copyfile: failed while copying (%s): %d"
+ "[ERROR] copyfile: statfs(%@) failed: %@ %{errno}d"
+ "_creationTime"
+ "_dbCreationTimestamp"
+ "_equivalentContentVersions"
+ "_equivalentMetadataVersions"
+ "_isStreamResetRunning"
+ "_itemPendingReconciliationIsLocked"
+ "_itemPendingReconciliationIsLockedInDB"
+ "_itemPendingReconciliationJobBlockingCode"
+ "_itemPendingReconciliationJobCode"
+ "_itemPendingReconciliationJobSchedulingState"
+ "_itemPendingScanningDiskEnumerationStatus"
+ "_itemPendingScanningDiskHasMultiplePagesEnumeration"
+ "_itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "_itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "_itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "_itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "_itemPendingScanningProviderEnumerationStatus"
+ "_itemPendingScanningProviderHasMultiplePagesEnumeration"
+ "_itemPendingScanningProviderNumberOfChildren"
+ "_itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "_itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "_itemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "_itemsPendingReconciliation"
+ "_itemsPendingScanningDisk"
+ "_itemsPendingScanningProvider"
+ "_latestFolderSelectedForImport"
+ "_latestFolderSelectedForImportIsMonitored"
+ "_latestFolderSelectedForImportState"
+ "_latestFolderSelectedForImportTimestamp"
+ "_latestFolderSelectedForImportWasModifiedOnDisk"
+ "_latestFolderSelectedForImportWasModifiedRemotely"
+ "_numberOfItemsPendingReconciliation"
+ "_numberOfItemsPendingScanningDisk"
+ "_numberOfItemsPendingScanningProvider"
+ "_numberOfItemsPendingSelection"
+ "_rootWasCopied"
+ "_shouldCopyAppleDouble"
+ "_stateOfDownloadJobs"
+ "_stateOfOtherJobs"
+ "_stateOfUploadJobs"
+ "_test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:"
+ "_test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:"
+ "_test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:"
+ "_unbounded"
+ "_xpcActivityDasdContext"
+ "_xpcActivityIsActive"
+ "_xpcActivityRegisteredWithDuet"
+ "_xpcActivityTimeSinceLastActivation"
+ "_xpcActivityTimeSinceLastRegistration"
+ "com.apple.private.coreservices.canmaplsdatabase"
+ "creationTime"
+ "dbCreationTimestamp"
+ "decodeDoubleForKey:"
+ "defaultWorkspace"
+ "ec"
+ "em"
+ "encodeDouble:forKey:"
+ "equivalentContentVersions"
+ "equivalentContentVersions.count < 16"
+ "equivalentMetadataVersions"
+ "equivalentMetadataVersions.count < 16"
+ "exfat"
+ "fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:completion:"
+ "fp_volumeUsesAppleDouble:"
+ "getKnowledgeUUID:andSequenceNumber:"
+ "initWithDomainPathRelativeToVolumeRoot:displayName:creationTime:andFileID:"
+ "initWithDomainURL:displayName:error:"
+ "initWithItemIdentifier:"
+ "initWithMainContentVersion:equivalentContentVersions:mainMetadataVersion:equivalentMetadataVersions:lastEditorDeviceName:"
+ "isStreamResetRunning"
+ "isUnbounded"
+ "itemPendingReconciliationIsLocked"
+ "itemPendingReconciliationIsLockedInDB"
+ "itemPendingReconciliationJobBlockingCode"
+ "itemPendingReconciliationJobCode"
+ "itemPendingReconciliationJobSchedulingState"
+ "itemPendingScanningDiskEnumerationStatus"
+ "itemPendingScanningDiskHasMultiplePagesEnumeration"
+ "itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "itemPendingScanningProviderEnumerationStatus"
+ "itemPendingScanningProviderHasMultiplePagesEnumeration"
+ "itemPendingScanningProviderNumberOfChildren"
+ "itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "itemPendingScanningProviderRemovalOfDatalessBitStatus"
+ "itemsPendingReconciliation"
+ "itemsPendingScanningDisk"
+ "itemsPendingScanningProvider"
+ "latestFolderSelectedForImport"
+ "latestFolderSelectedForImportIsMonitored"
+ "latestFolderSelectedForImportState"
+ "latestFolderSelectedForImportTimestamp"
+ "latestFolderSelectedForImportWasModifiedOnDisk"
+ "latestFolderSelectedForImportWasModifiedRemotely"
+ "msdos"
+ "numberOfItemsPendingReconciliation"
+ "numberOfItemsPendingScanningDisk"
+ "numberOfItemsPendingScanningProvider"
+ "numberOfItemsPendingSelection"
+ "providersWithOngoingImport"
+ "rootWasCopied"
+ "setCreationTime:"
+ "setDbCreationTimestamp:"
+ "setErrorDetails:"
+ "setIsStreamResetRunning:"
+ "setItemPendingReconciliationIsLocked:"
+ "setItemPendingReconciliationIsLockedInDB:"
+ "setItemPendingReconciliationJobBlockingCode:"
+ "setItemPendingReconciliationJobCode:"
+ "setItemPendingReconciliationJobSchedulingState:"
+ "setItemPendingScanningDiskEnumerationStatus:"
+ "setItemPendingScanningDiskHasMultiplePagesEnumeration:"
+ "setItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingReconciliation:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingRejection:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDown:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUp:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:"
+ "setItemPendingScanningProviderEnumerationStatus:"
+ "setItemPendingScanningProviderHasMultiplePagesEnumeration:"
+ "setItemPendingScanningProviderNumberOfChildren:"
+ "setItemPendingScanningProviderNumberOfChildrenFailingCreation:"
+ "setItemPendingScanningProviderNumberOfChildrenPendingCreation:"
+ "setItemPendingScanningProviderRemovalOfDatalessBitStatus:"
+ "setItemsPendingReconciliation:"
+ "setItemsPendingScanningDisk:"
+ "setItemsPendingScanningProvider:"
+ "setLatestFolderSelectedForImport:"
+ "setLatestFolderSelectedForImportIsMonitored:"
+ "setLatestFolderSelectedForImportState:"
+ "setLatestFolderSelectedForImportTimestamp:"
+ "setLatestFolderSelectedForImportWasModifiedOnDisk:"
+ "setLatestFolderSelectedForImportWasModifiedRemotely:"
+ "setNumberOfItemsInError:"
+ "setNumberOfItemsPendingReconciliation:"
+ "setNumberOfItemsPendingScanningDisk:"
+ "setNumberOfItemsPendingScanningProvider:"
+ "setNumberOfItemsPendingSelection:"
+ "setNumberOfItemsReconciled:"
+ "setRootWasCopied:"
+ "setShouldCopyAppleDouble:"
+ "setStateOfDownloadJobs:"
+ "setStateOfOtherJobs:"
+ "setStateOfUploadJobs:"
+ "setStatus:"
+ "setUnbounded:"
+ "setXpcActivityDasdContext:"
+ "setXpcActivityIsActive:"
+ "setXpcActivityRegisteredWithDuet:"
+ "setXpcActivityTimeSinceLastActivation:"
+ "setXpcActivityTimeSinceLastRegistration:"
+ "shouldCopyAppleDouble"
+ "stateOfDownloadJobs"
+ "stateOfOtherJobs"
+ "stateOfUploadJobs"
+ "unbounded"
+ "xpcActivityDasdContext"
+ "xpcActivityIsActive"
+ "xpcActivityRegisteredWithDuet"
+ "xpcActivityTimeSinceLastActivation"
+ "xpcActivityTimeSinceLastRegistration"
- "1703.42.2"
- "@48@0:8q16q24q32@40"
- "T@\"NSArray\",R,C,N,V_errorDetails"
- "Tq,R,N,V_numberOfItemsInError"
- "Tq,R,N,V_numberOfItemsReconciled"
- "Tq,R,N,V_status"
- "[DEBUG] clearing import cookie for domain url %@"
- "[DEBUG] copyfile: %@ -> %@"
- "[DEBUG] writing import cookie for domain url %@"
- "[INFO] Running on iPhone running an internal build, FPFS should be enabled by default."
- "clearCookieForDomainURL:error:"
- "initWithDomainURL:error:"
- "initWithStatus:numberOfItemsReconciled:numberOfItemsInError:errorDetails:"
- "isImportingDomainsForUserURL:"
- "isImportingInVolumeAtURL:"
- "lastModificationDate"
- "writeCookieForDomainURL:error:"

```
