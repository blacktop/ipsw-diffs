## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-2732.80.49.0.0
-  __TEXT.__text: 0x1269c8
-  __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0xc140
-  __TEXT.__const: 0x590
-  __TEXT.__gcc_except_tab: 0x9ed8
-  __TEXT.__cstring: 0x13f33
-  __TEXT.__oslogstring: 0xd61d
-  __TEXT.__dlopen_cstrs: 0x7ee
+2882.100.413.0.0
+  __TEXT.__text: 0x12ad4c
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_methlist: 0xdf6c
+  __TEXT.__const: 0x85e
+  __TEXT.__gcc_except_tab: 0x9f64
+  __TEXT.__cstring: 0x13fd2
+  __TEXT.__oslogstring: 0xd86e
+  __TEXT.__dlopen_cstrs: 0x79e
   __TEXT.__ustring: 0x21e
-  __TEXT.__unwind_info: 0x52f0
-  __TEXT.__objc_classname: 0x1f4d
-  __TEXT.__objc_methname: 0x22c1a
-  __TEXT.__objc_methtype: 0x62fe
-  __TEXT.__objc_stubs: 0x13660
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x5f70
-  __DATA_CONST.__objc_classlist: 0x660
+  __TEXT.__swift5_typeref: 0xb4
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_reflstr: 0x45
+  __TEXT.__swift5_fieldmd: 0x44
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__unwind_info: 0x5558
+  __TEXT.__eh_frame: 0xa0
+  __TEXT.__objc_classname: 0x1ef9
+  __TEXT.__objc_methname: 0x23051
+  __TEXT.__objc_methtype: 0x6572
+  __TEXT.__objc_stubs: 0x138a0
+  __DATA_CONST.__got: 0xab0
+  __DATA_CONST.__const: 0x5ff8
+  __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x290
+  __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6828
-  __DATA_CONST.__objc_protorefs: 0x148
-  __DATA_CONST.__objc_superrefs: 0x520
-  __DATA_CONST.__objc_arraydata: 0xa98
-  __AUTH_CONST.__auth_got: 0xd80
-  __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x1a00
-  __AUTH_CONST.__cfstring: 0x109e0
-  __AUTH_CONST.__objc_const: 0x267a8
+  __DATA_CONST.__objc_selrefs: 0x6b60
+  __DATA_CONST.__objc_protorefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_arraydata: 0xaa0
+  __AUTH_CONST.__auth_got: 0xe80
+  __AUTH_CONST.__auth_ptr: 0x190
+  __AUTH_CONST.__const: 0x1b48
+  __AUTH_CONST.__cfstring: 0x10ba0
+  __AUTH_CONST.__objc_const: 0x22ea0
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x2d0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xfc8
-  __DATA.__data: 0x1fb8
-  __DATA.__bss: 0x6b8
-  __DATA_DIRTY.__objc_data: 0x3cf0
-  __DATA_DIRTY.__data: 0x2c0
-  __DATA_DIRTY.__bss: 0x3c8
+  __DATA.__objc_ivar: 0xfd4
+  __DATA.__data: 0x1ee8
+  __DATA.__bss: 0xa40
+  __DATA.__common: 0x39
+  __DATA_DIRTY.__objc_data: 0x3c50
+  __DATA_DIRTY.__data: 0x2c1
+  __DATA_DIRTY.__bss: 0x378
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6714
-  Symbols:   8197
-  CStrings:  9885
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 7017
+  Symbols:   8505
+  CStrings:  9938
 
Symbols:
+ _CFDictionaryGetTypeID
+ _CFPreferencesGetAppBooleanValue
+ _CFPreferencesGetAppIntegerValue
+ _FPGetSharedDomainCachingPath
+ _FPPerformWithDefaultPersona
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_UMUserPersonaAttributes
+ __Block_copy
+ __Block_release
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFileProvider
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _container_copy_sandbox_token
+ _dataless_fault_header_convert_to_decmpfs_header
+ _dataless_fault_header_decode
+ _fpfs_eviction_properties
+ _fpfs_fast_realpath
+ _fpfs_flock
+ _fpfs_get_purgable_flags
+ _fpfs_get_purgeable_non_evictable_urgency
+ _fpfs_lp_mkdirat
+ _fpfs_openbyid64_np
+ _fpfs_openparent
+ _fpfs_remove_content_dependent_xattrs
+ _fpfs_renameatx_np
+ _fpfs_set_support_long_paths_iopolicy
+ _fpfs_speculative_download_hierarchy_set
+ _fpfs_speculative_download_hierarchy_unset
+ _fpfs_supports_download_lazily_v2
+ _fpfs_t_is_evictable_at
+ _fpfs_update_purgency_during_restore
+ _kCFPreferencesAnyApplication
+ _kFPDefaultIOContext
+ _kFPDefaultIOContextForLocalStorage
+ _kFPTaskErrorDomain
+ _kNSFileProviderUserInfoExperimentID
+ _notify_get_state
+ _notify_register_check
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _statfs_ext
+ _swift_allocError
+ _swift_bridgeObjectRelease
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_release
+ _swift_retain
+ _swift_task_switch
+ _swift_willThrow
- _FPFeatureFlagHelenaIsEnabled
- _FPIsFPCKXPCServiceEnabled
- _FPStatVFS
- _OBJC_CLASS_$_NSExtensionContext
- _OBJC_CLASS_$__NSExtensionContextVendor
- _OBJC_METACLASS_$_NSExtensionContext
- _fmod
- _fpfs_eviction_urgency
- _fpfs_supports_purge_reasons
- _kInPauseResumeEntitlement
CStrings:
+ "+[FPXExtensionContext principalClass]_block_invoke"
+ ".domainscache.plist"
+ "/.nofollow/"
+ "/.nofollow/%s"
+ "2882.100.413"
+ "B16@?0r*8"
+ "B48@0:8@16^@24^@32^@40"
+ "DLV2"
+ "FPRepeatDonation"
+ "FPTaskErrorDomain"
+ "Failed to spawn task"
+ "NSFileProviderUserInfoExperimentID"
+ "PreventUnindexOnEviction"
+ "PrivateDiagnostics"
+ "SIMULATOR_ROOT"
+ "Spotlight"
+ "T@\"FPXExtensionContext\",W,N,V_extensionContext"
+ "TB,N,V_isEvictedWithClone"
+ "TB,N,V_isOnMainVolume"
+ "Task finished with exit code %d"
+ "Task terminated due to signal %d"
+ "Vendor extension instance returned neither an item nor an error during trash operation of item %@"
+ "[DEBUG] Process is allowed to read domains cache"
+ "[DEBUG] Spawning FPTask with command '%@'"
+ "[DEBUG] ┳%llx continuing on %s at QoS %d"
+ "[ERROR] Failed getting sandbox extension: %d (handle: %lld)"
+ "[ERROR] Failed querying shared cache"
+ "[ERROR] Failed querying shared cache: %s"
+ "[ERROR] Failed reading domains cache: %{public}@"
+ "[ERROR] Failed to create container query"
+ "[ERROR] Failed unarchiving domains cache: %{public}@"
+ "[ERROR] failed to enable long paths i/o policy: %s"
+ "[ERROR] failed to get long paths i/o policy: %s"
+ "[ERROR] failed to list version from the provider with error: %@"
+ "[ERROR] failed to restore long paths i/o policy to %d: %s"
+ "[ERROR] waitpid() failed with errno %d, %s"
+ "[INFO] command terminated due to signal %d"
+ "[WARNING] Process is not allowed to read domains cache"
+ "_FPPerformWithPersona"
+ "_dontLoadCacheFromDisk"
+ "_ignoreUpdateNotifications"
+ "_isEvictedWithClone"
+ "_isOnMainVolume"
+ "_markItemsForUpdate:index:completionHandler:"
+ "_t_forceReadCacheFromDisk"
+ "_t_ignoreUpdateNotifications:"
+ "_t_loadCacheOnHandlerAdding:"
+ "_test_purgerBarrierWithCompletionHandler:"
+ "_test_triggerDatabaseError:domain:completionHandler:"
+ "allowedToReadCacheFromDisk"
+ "appGroup"
+ "checkErrorAgainstDiagnosticsJson:inputError:errorDirection:jobCode:completionHandler:"
+ "clearDiagnosticsState:completionHandler:"
+ "com.apple.fileprovider.log-sensitive-data-update-interval"
+ "com.apple.private.MobileContainerManager.lookup"
+ "dataWithContentsOfFile:options:error:"
+ "environment"
+ "exec:error:"
+ "exec:stdoutString:stderrString:error:"
+ "failed to remove content dpendent xattrs during eviction [%s]"
+ "failed to remove content dpendent xattrs during materialization [%s]"
+ "fpfs_metadata.m"
+ "group.com.apple.FileProvider.DomainCaching"
+ "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QICii}*Q[0c]}8"
+ "ignoreUpdateNotifications"
+ "isDefaultPersona"
+ "isEvictedWithClone"
+ "isOnMainVolume"
+ "kMDItemFileItemID"
+ "newPreparedArgvArray"
+ "personaAttributesForPersonaType:"
+ "processInfo"
+ "r^*16@0:8"
+ "readCacheFromDisk:"
+ "requestDiagnosticCollectionForItemWithIdentifier:errorReason:completionHandler:"
+ "selectNewProviderDomain:knownFolders:skipReleasePrompt:completionHandler:"
+ "setExtensionContext:"
+ "setIsEvictedWithClone:"
+ "setIsOnMainVolume:"
+ "sim_mkdirAt:path:permissions:completionHandler:"
+ "sim_openAt:path:flags:permissions:completionHandler:"
+ "sim_openByID:device:oflag:completionHandler:"
+ "sim_renameAt:from:tofd:to:flags:completionHandler:"
+ "sim_requestProtocolVersion:completionHandler:"
+ "sim_unlinkAt:path:flag:recursive:completionHandler:"
+ "simulatorRoot"
+ "slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:"
+ "stderr"
+ "stdout"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@?0@\"<FPDWakeupTransaction>\"8@\"NSError\"16"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"<FPDWakeupTransaction>\"@\"NSError\">24"
+ "v32@0:8Q16@?<v@?@\"NSError\">24"
+ "v32@0:8Q16@?<v@?Q@\"NSError\">24"
+ "v40@0:8@\"NSError\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSError\"24@?<v@?@\"NSError\">32"
+ "v40@0:8Q16i24i28@?32"
+ "v40@0:8Q16i24i28@?<v@?@\"NSFileHandle\"@\"NSError\">32"
+ "v44@0:8@\"NSString\"16Q24B32@?<v@?@\"NSError\">36"
+ "v48@0:8@\"NSFileHandle\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v52@0:8@\"NSFileHandle\"16@\"NSString\"24q32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16@24q32B40@?44"
+ "v56@0:8@\"NSFileHandle\"16@\"NSString\"24q32q40@?<v@?@\"NSFileHandle\"@\"NSError\">48"
+ "v56@0:8@\"NSString\"16@\"NSError\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8@16@24q32q40@?48"
+ "v64@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSFileHandle\"32@\"NSString\"40q48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40q48@?56"
+ "validateDiagnosticsJson:completionHandler:"
+ "waitForStabilizationOfDomainWithID:mode:completionHandler:"
+ "waitForStabilizationWithMode:completionHandler:"
+ "wakeUpForURLFixed:completionHandler:"
- "+[FPXExtensionContext principalClass]"
- ".~"
- "2732.80.49"
- "@\"<PKModularService>\"16@0:8"
- "@\"<PKModularService>\"24@0:8@\"NSDictionary\"16"
- "APFSIOC_PURGE_SINGLE_FILE did not evict anything, assuming EBUSY"
- "FPCKService"
- "FPExtension_subsystem"
- "FPExtension_subsystem.m"
- "FPPurgeReasonsSupport"
- "FPXHost"
- "FPXPlugInKitExtensionContext"
- "Helena"
- "NSExtensionPrincipalClass %@ could not be resolved to class!"
- "NSExtensionRequestHandling"
- "PKModularService"
- "Pinning"
- "T#,&,N"
- "Unable to make empty file dataless: %{errno}d"
- "Z"
- "[DEBUG] Cleanup of extension context requested, but already deallocated"
- "[DEBUG] Do not migrate to FPFS user default is configured."
- "[DEBUG] Failed to determine whether URL %@ is managed by a file provider"
- "_auxiliaryConnection"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_initializedByViewServices"
- "_setRequestCleanUpBlock:"
- "_setTransaction:"
- "_startListening:"
- "beginRequestWithExtensionContext:"
- "beginUsing:withBundle:"
- "brc_notify_get_state"
- "brc_notify_register_check"
- "bundleInfoDictionary"
- "com.apple.fileprovider.pause-resume"
- "com.apple.fileproviderd.FPCKService"
- "communicationsFailed:"
- "endUsing:"
- "exec:stdoutString:stderrString:"
- "extension context is of an invalid type of class (expected: %@, actual: %@)"
- "f"
- "fpfs_metadata.c"
- "gz"
- "i16@?0^{fpfs_fileattrs={fpfs_item_handle=QQII*iI}{fpfs_metadata=ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Sq{timespec=qq}{timespec=qq}{timespec=qq}Q{fpfs_tag_data=^vQi}(?=II)QQq*q*^{fpfs_xattr}II*BB*QIii}*Q[0c]}8"
- "initForPlugInKit"
- "initForPlugInKitWithOptions:"
- "initWithInputItems:listenerEndpoint:contextUUID:"
- "int _brc_notify_register_check(const char *, int *)"
- "makeTopologicallySortedItemsOnDisk:completionHandler:"
- "makeTopologicallySortedItemsOnDisk:error:"
- "setPrincipalClass:"
- "v24@0:8@\"<PKSubsystemServicePersonality>\"16"
- "v24@0:8@\"NSExtensionContext\"16"
- "v24@0:8@?<v@?@\"NSError\"@\"NSDictionary\">16"
- "v24@?0@\"NSError\"8@\"<FPDWakeupTransaction>\"16"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"
- "v32@0:8@\"<PKSubsystemServicePersonality>\"16@\"NSBundle\"24"
- "void _brc_notify_get_state(int, uint64_t *, const char *)"
- "xz"
- "~$"

```
