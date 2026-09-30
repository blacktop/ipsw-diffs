## installcoordination_proxy

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy`

```diff

-784.82.1.0.0
-  __TEXT.__text: 0x1259c
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0xd14
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x228e
-  __TEXT.__objc_classname: 0x18c
-  __TEXT.__objc_methname: 0x2c74
-  __TEXT.__oslogstring: 0x1a5f
-  __TEXT.__objc_methtype: 0x7e2
-  __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__auth_got: 0x4e8
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0xc40
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_catlist: 0x8
+787.100.20.502.1
+  __TEXT.__text: 0xaa60
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x1860
+  __TEXT.__objc_methlist: 0x9f4
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x158b
+  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__oslogstring: 0xfca
+  __TEXT.__objc_methname: 0x20df
+  __TEXT.__objc_classname: 0x143
+  __TEXT.__objc_methtype: 0x662
+  __TEXT.__unwind_info: 0x318
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1b28
-  __DATA.__objc_selrefs: 0xa40
-  __DATA.__objc_ivar: 0xb4
-  __DATA.__objc_data: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA.__objc_const: 0x1878
+  __DATA.__objc_selrefs: 0x768
+  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_data: 0x230
   __DATA.__data: 0x2b0
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A83B5C7-C645-3A66-A63A-139A1EF669CA
-  Functions: 404
-  Symbols:   218
-  CStrings:  980
+  UUID: CAB6177D-CA3B-32B3-BBFB-4E7D054B9BD8
+  Functions: 283
+  Symbols:   147
+  CStrings:  631
 
Symbols:
+ _IXArrayContainsOnlyClass
+ _IXStringForClientID
+ _OBJC_CLASS_$_IXFileManager
+ __IXCreateError
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- _CFBundleGetInfoDictionary
- _CFPropertyListIsValid
- _CFRelease
- _IXFunctionNameErrorKey
- _IXSourceFileLineErrorKey
- _IXStringForIXError
- _MGGetStringAnswer
- _NSLocalizedDescriptionKey
- _NSLocalizedFailureReasonErrorKey
- _NSURLIsExcludedFromBackupKey
- _NSUnderlyingErrorKey
- _OBJC_CLASS_$_MIHelperServiceFrameworkClient
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSSet
- _SANDBOX_EXTENSION_DEFAULT
- __CFBundleCreateFilteredInfoPlist
- __CFBundleCreateUnique
- ___chkstk_darwin
- __os_crash_msg
- __os_log_send_and_compose_impl
- _acl_free
- _acl_get_link_np
- _acl_init
- _acl_set_fd
- _acl_set_link_np
- _bzero
- _closedir
- _confstr
- _container_system_group_path_for_identifier
- _copyfile
- _dirfd
- _dispatch_get_global_queue
- _fcntl
- _fdopendir
- _fts_close
- _fts_open
- _fts_read
- _getattrlistbulk
- _getpwnam_r
- _kCFAllocatorDefault
- _lchmod
- _lchown
- _lstat
- _mkdir
- _mkdtemp
- _mkpath_np
- _objc_claimAutoreleasedReturnValue
- _objc_enumerationMutation
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x9
- _open
- _opendir
- _os_transaction_create
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _os_variant_has_internal_diagnostics
- _qos_class_self
- _readdir_r
- _readlink
- _realpath$DARWIN_EXTSN
- _removefile
- _removefile_state_alloc
- _removefile_state_free
- _removefile_state_get
- _removefile_state_set
- _rename
- _sandbox_extension_consume
- _sandbox_extension_issue_file
- _sandbox_extension_release
- _strdup
- _strlen
- _symlink
- _sysconf
CStrings:
+ "%s: Exceeded maximum number of retries (%lu attempts) when constructing a coordinator for %@"
+ "%s: Failed to create a new coordinator for this installation because one already existed: %@"
+ "+[IXSRemoteInstaller retryingCoordinatorCreateForIdentity:attempt:isUpdate:creationBlock:cancelationBlock:shouldCancelExistingBlock:error:]"
+ "21:21:03"
+ "@\"IXAppInstallCoordinator<IXInitiatingOrUpdatingCoordinator>\"36@?0@\"IXApplicationIdentity\"8B16^B20^@28"
+ "@44@0:8@16Q24B32^@36"
+ "@68@0:8@16Q24B32@?36@?44@?52^@60"
+ "B16@?0@\"IXAppInstallCoordinator<IXInitiatingOrUpdatingCoordinator>\"8"
+ "B32@?0@\"IXAppInstallCoordinator<IXInitiatingOrUpdatingCoordinator>\"8@\"NSError\"16^@24"
+ "Canceling existing coordinator by %@"
+ "Exceeded maximum number of retries (%lu attempts) when constructing a coordinator for %@"
+ "Failed to create a new coordinator for this installation because one already existed: %@"
+ "Feb  3 2026"
+ "_retryingCoordinatorCreateForIdentity:attempt:isUpdate:error:"
+ "code"
+ "domain"
+ "existingCoordinatorForAppWithIdentity:error:"
+ "retryingCoordinatorCreateForIdentity:attempt:isUpdate:creationBlock:cancelationBlock:shouldCancelExistingBlock:error:"
- ""
- "#"
- "%s: CFBundleGetInfoDictionary returned NULL for bundle %@ : %@"
- "%s: Created %@"
- "%s: Failed to create CFBundle from %@ : %@"
- "%s: Failed to create URL by appending %s to %@"
- "%s: Failed to create a new coordinator : %@"
- "%s: Failed to create a new coordinator as one already existed : %@"
- "%s: Failed to create path to child directory by appending \"%s\" to %@"
- "%s: Failed to determine if %@ exists: %s"
- "%s: Failed to find a \".app\" inside the extracted contents at %@ : %@"
- "%s: Failed to get filtered Info.plist with keys %@ from bundle %@ : %@"
- "%s: Failed to get group container path for group 'systemgroup.com.apple.installcoordinationd'; container_system_group_path_for_identifier returned %llu : %@"
- "%s: Failed to get name for directory item %llu in %@; not counting its children"
- "%s: Failed to get path to url %@"
- "%s: Failed to open directory %@ : %s"
- "%s: Failed to realpath %s : %s at %s"
- "%s: Failed to remove ACL : %@"
- "%s: Failed to remove move source after copy at %@ : %@"
- "%s: Failed to retrieve depth of %@"
- "%s: Failed to retrieve realpath for base path %@ "
- "%s: Failed to retrieve realpath for suspicious path %@"
- "%s: Failed to set backup exclusion on %@ : %@"
- "%s: Failed to stat %s : %s"
- "%s: Got error %s while processing entry %llu in %@"
- "%s: Ignoring error %s from acl_set_link_np for %s"
- "%s: Ignoring symlink at %s/%s"
- "%s: Object returned from _CFBundleCreateFilteredInfoPlist for %@ was not a dictionary, was type %@ : %@"
- "%s: Readlink failed: %s"
- "%s: Realpathed %@ ; appending non-existing components %@"
- "%s: Rejecting %@ -> %@, as it is points outside or to the base %@"
- "%s: Rejecting %@ -> %s, as absolute symlinks are not allowed"
- "%s: Rejecting %@ with base %@ (reals %@ ; %@) because components diverge at %@ != %@"
- "%s: Rejecting %@ with base %@ because base component count is greater than child component count (reals %@ ; %@)"
- "%s: Rejecting %@ with base %@ because real component counts don't make sense (reals %@ ; %@)"
- "%s: Skipping hardlinked file at %@/%s"
- "%s: The base path %@ and/or suspicious path %@ were nil"
- "%s: The suspicious path %@ contains '..' paths, which are invalid"
- "%s: Writing ACL to %s"
- "%s: getattrlistbulk on entry %llu in %@ returned error %s"
- "%s: removefile hit error for %s : %s"
- "%s: removefile hit error for %s but we failed to get the error number"
- "%s: removefile_state_set REMOVEFILE_STATE_ERROR_CALLBACK failed: %s"
- "%s: removefile_state_set REMOVEFILE_STATE_ERROR_CONTEXT failed: %s"
- "%s: skipping empty directory at %@/%s"
- "%s: supiscious path %@ does not contain base path %@ as a prefix"
- "-[IXFileManager _diskUsageForDirectoryURL:]"
- "-[IXFileManager _moveItemAtURL:toURL:failIfSrcMissing:error:]"
- "-[IXFileManager _realPathForURL:allowNonExistentPathComponents:]"
- "-[IXFileManager _realPathWhatExistsInPath:]"
- "-[IXFileManager _removeACLAtPath:isDir:error:]"
- "-[IXFileManager _traverseDirectory:ignoringFTSErrors:error:withBlock:]"
- "-[IXFileManager consumeSandboxExtension:error:]"
- "-[IXFileManager copyACLFrom:toAllChildrenOfPath:ignoringCopyErrors:error:]"
- "-[IXFileManager copyACLFrom:toAllChildrenOfPath:ignoringCopyErrors:error:]_block_invoke"
- "-[IXFileManager createSymbolicLinkAtURL:withDestinationURL:error:]"
- "-[IXFileManager dataProtectionClassOfItemAtURL:class:error:]"
- "-[IXFileManager destinationOfSymbolicLinkAtURL:error:]"
- "-[IXFileManager diskUsageForURL:]"
- "-[IXFileManager issueSandboxExtensionForURL:withExtensionClass:error:]"
- "-[IXFileManager itemDoesNotExistAtURL:]"
- "-[IXFileManager realPathForURL:ifChildOfURL:]"
- "-[IXFileManager releaseSandboxExtensionToken:error:]"
- "-[IXFileManager setDataProtectionClassOfItemAtURL:toClass:ifPredicate:error:]"
- "-[IXFileManager setPermissions:onAllChildrenOfPath:error:]_block_invoke"
- "-[IXFileManager setPermissionsOfItemAtURL:toMode:error:]"
- "-[IXFileManager standardizeOwnershipAtURL:toUID:toGID:error:]_block_invoke"
- "-[IXGlobalConfiguration _dataStorageHomeURLWithError:]"
- "-[IXGlobalConfiguration _userTempDirURLWithError:]"
- "-[IXGlobalConfiguration createDirectories]"
- "."
- ".."
- "/"
- "/private"
- "/private/"
- "0a"
- "22:49:13"
- "<lstat error: %s>"
- "<uid:%u gid:%u mode:0%ho flags:0x%x>"
- "@24@0:8^@16"
- "@36@0:8@16B24^@28"
- "@40@0:8@16@24^@32"
- "@40@0:8@16r*24^@32"
- "@f"
- "AppURLFromExtractedPayloadDir"
- "B16@?0^{dirent=QQSSC[1024c]}8"
- "B24@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8^@16"
- "B32@0:8@16^@24"
- "B32@0:8q16^@24"
- "B36@0:8@16B24^@28"
- "B36@0:8@16I24^I28"
- "B36@0:8@16S24^@28"
- "B36@0:8S16@20^@28"
- "B36@0:8r*16B24^@28"
- "B40@0:8@16B24S28^@32"
- "B40@0:8@16I24I28^@32"
- "B40@0:8@16^B24^@32"
- "B40@0:8@16^i24^@32"
- "B44@0:8@16@24B32^@36"
- "B44@0:8@16B24S28i32^@36"
- "B44@0:8@16B24^@28@?36"
- "B44@0:8@16i24@?28^@36"
- "CFBundleGetInfoDictionary returned NULL for bundle %@"
- "CFBundleInfoPlistURL"
- "Cancel orphaned coordinator"
- "Could not create symlink containing %s at %s: %s"
- "Could not readlink %s : %s"
- "DeviceClass"
- "Error for path %s: %s"
- "ExtractedApps"
- "Failed to create CFBundle from %@"
- "Failed to create a new coordinator as one already existed : %@"
- "Failed to create data directory at %@ : %@"
- "Failed to create removability directory at %@ : %@"
- "Failed to create temp dir at path %s"
- "Failed to fetch data directory: %@"
- "Failed to fetch system container URL: %@"
- "Failed to find a \".app\" inside the extracted contents at %@"
- "Failed to get data directory: %@"
- "Failed to get filtered Info.plist with keys %@ from bundle %@"
- "Failed to get group container path for group 'systemgroup.com.apple.installcoordinationd'; container_system_group_path_for_identifier returned %llu"
- "Failed to get home dir path size: %s"
- "Failed to get promise staging directory for install location %@ with uniqueName %@: %@"
- "Failed to get removability directory: %@"
- "Failed to getclass of file %s: %s"
- "Failed to initialize temporary directory: error = %d (%s)"
- "Failed to lchmod %s to mode 0%o : %s"
- "Failed to lchown %s with uid/gid %d/%d : %s"
- "Failed to open %s : %s"
- "Failed to remove ACL"
- "Failed to set ACL on %s: %s"
- "Failed to set ACL on dir %s: %s"
- "Failed to setclass(%d) on directory %@: %s"
- "Failed to setclass(%d) on file %s: %s"
- "I"
- "I16@0:8"
- "IXCopyItemAtURL"
- "IXCreateDirectoryAtURL"
- "IXCreateTemporaryDirectoryInDirectoryURL"
- "IXFileManager"
- "IXGlobalConfiguration"
- "IXItemExistsAtURL"
- "IXRemoveItemAtURL"
- "IXUrlsForItemsInDirectoryAtURL"
- "IXUrlsForItemsInDirectoryAtURL_block_invoke"
- "InstallCoordination"
- "InstallCoordination.framework"
- "InstallCoordinationAdditions"
- "Jan 22 2026"
- "Library"
- "LoadInfoPlistFromBundle"
- "LoadInfoPlistFromBundleAtURL"
- "Object returned from _CFBundleCreateFilteredInfoPlist for %@ was not a dictionary, was type %@"
- "PrivateFrameworks"
- "Q24@0:8@16"
- "RemoteInstallStaging"
- "Removability"
- "System"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_daemonUserHome"
- "T@\"NSURL\",R,N,V_dataStorageHome"
- "T@\"NSURL\",R,N,V_rootPath"
- "TB,R,N"
- "TI,R,N,V_daemonGID"
- "TI,R,N,V_daemonUID"
- "TempIcons"
- "UTF8String"
- "_IterateDirectory for %s returned %s"
- "_copyItemAtURL:toURL:failIfSrcMissing:error:"
- "_daemonGID"
- "_daemonUID"
- "_daemonUserHome"
- "_dataStorageHome"
- "_dataStorageHomeURLWithError:"
- "_diskUsageForDirectoryURL:"
- "_dynamicPropertyLock"
- "_moveItemAtURL:toURL:failIfSrcMissing:error:"
- "_realPathForURL:allowNonExistentPathComponents:"
- "_realPathWhatExistsInPath:"
- "_removeACLAtPath:isDir:error:"
- "_removefile_error_callback"
- "_rootPath"
- "_traverseDirectory:ignoringFTSErrors:error:withBlock:"
- "_userTempDirURLWithError:"
- "_validateSymlink:withStartingDepth:andEndingDepth:"
- "acl_get_link_np failed for %s"
- "acl_get_link_np found no ACLs on %s"
- "acl_init() failed: %s"
- "acl_set_link_np for %s failed"
- "allObjects"
- "app"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "boolValue"
- "com.apple.InstallCoordination.async-block"
- "consumeSandboxExtension:error:"
- "containsObject:"
- "copyACLFrom:toAllChildrenOfPath:error:"
- "copyACLFrom:toAllChildrenOfPath:ignoringCopyErrors:error:"
- "copyItemAtURL:toURL:error:"
- "copyItemIfExistsAtURL:toURL:error:"
- "copyfile of %@ to %@ failed: %s"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectories"
- "createDirectoryAtURL:withIntermediateDirectories:mode:class:error:"
- "createDirectoryAtURL:withIntermediateDirectories:mode:error:"
- "createSymbolicLinkAtURL:withDestinationURL:error:"
- "createTemporaryDirectoryInDirectoryURL:error:"
- "createTemporaryExtractionDirectoryWithError:"
- "daemonGID"
- "daemonUID"
- "daemonUserHome"
- "dataDirectoryAbortingOnError"
- "dataDirectoryWithError:"
- "dataProtectionClassOfItemAtURL:class:error:"
- "dataStorageHome"
- "debugDescriptionOfItemAtURL:"
- "destinationOfSymbolicLinkAtURL:error:"
- "dictionaryWithCapacity:"
- "dirfd of %s failed: %s"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extractedInstallableStagingDirectory:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "fileURLWithPath:"
- "fileURLWithPathComponents:"
- "frameworkURL"
- "fts_close failed for %s with error %s"
- "fts_open failed for %s with error %s"
- "getpwnam_r failed for user '%s' : %s"
- "hasPrefix:"
- "iPad"
- "iconStagingDirectoryWithError:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithFormat:arguments:"
- "isiPad"
- "issueSandboxExtensionForURL:withExtensionClass:error:"
- "itemDoesNotExistAtURL:"
- "itemExistsAtURL:error:"
- "itemExistsAtURL:isDirectory:error:"
- "length"
- "lstat of %s failed: %s"
- "mkdir of %@ failed: %s"
- "mkpath_np of %@ failed: %s"
- "mobile"
- "moveItemAtURL:toURL:error:"
- "moveItemIfExistsAtURL:toURL:error:"
- "mutableCopy"
- "nil url passed to -removeItemAtURL:error:"
- "numberWithInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "open of %s failed: %s"
- "opendir of %@ failed: %s"
- "opendir of %s failed: %s"
- "pathComponents"
- "pathExtension"
- "pathWithComponents:"
- "private"
- "promiseStagingRootAbortingOnErrorForInstallLocation:usingUniqueName:"
- "promiseStagingRootForInstallLocation:usingUniqueName:error:"
- "q32@0:8@16^@24"
- "realPathForURL:"
- "realPathForURL:ifChildOfURL:"
- "releaseSandboxExtensionToken:error:"
- "remoteInstallationStagingDirectory:"
- "removabilityDirectoryAbortingOnError"
- "removabilityDirectoryWithError:"
- "removeItemAtURL:error:"
- "removeItemAtURL:keepParent:error:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removefile of %@ failed: %s"
- "rename of %@ to %@ failed: %s"
- "rootPath"
- "sandbox_extension_consume for %s failed: %s."
- "sandbox_extension_issue_file for path %@ failed: %s"
- "sandbox_extension_release for %lld failed: %s."
- "setDataProtectionClassOfItemAtURL:toClass:ifPredicate:error:"
- "setPermissions:onAllChildrenOfPath:error:"
- "setPermissionsOfItemAtURL:toMode:error:"
- "setResourceValue:forKey:error:"
- "setWithCapacity:"
- "sharedInstance"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
- "standardizeOwnershipAtURL:toUID:toGID:error:"
- "stat of %@ failed: %s"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringWithFileSystemRepresentation:length:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "systemgroup.com.apple.installcoordinationd"
- "temp.XXXXXX"
- "urlByAppendingPathComponents:lastIsDirectory:"
- "urlsForItemsInDirectoryAtURL:ignoringSymlinks:error:"
- "userVolumeURL"
- "v32@?0@8@16^B24"
- "var"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
