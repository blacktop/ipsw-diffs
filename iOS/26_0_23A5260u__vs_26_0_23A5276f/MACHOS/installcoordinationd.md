## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-755.0.0.0.0
-  __TEXT.__text: 0xa1ab8
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_stubs: 0xad20
-  __TEXT.__objc_methlist: 0x5c24
-  __TEXT.__const: 0x208
-  __TEXT.__cstring: 0x1888b
-  __TEXT.__objc_methname: 0x10b97
-  __TEXT.__objc_classname: 0x9ed
-  __TEXT.__objc_methtype: 0x2329
-  __TEXT.__oslogstring: 0xdb76
-  __TEXT.__gcc_except_tab: 0x2aa8
+763.0.0.502.1
+  __TEXT.__text: 0xa3508
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__objc_stubs: 0xaf20
+  __TEXT.__objc_methlist: 0x5d2c
+  __TEXT.__const: 0x210
+  __TEXT.__cstring: 0x18b3f
+  __TEXT.__objc_methname: 0x10dd0
+  __TEXT.__objc_classname: 0xa21
+  __TEXT.__objc_methtype: 0x23a7
+  __TEXT.__oslogstring: 0xdd8b
+  __TEXT.__gcc_except_tab: 0x2b98
   __TEXT.__ustring: 0x1a64
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x2478
-  __DATA_CONST.__auth_got: 0x888
-  __DATA_CONST.__got: 0x450
+  __TEXT.__unwind_info: 0x2500
+  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2b28
-  __DATA_CONST.__cfstring: 0x9c40
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__cfstring: 0x9ca0
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc398
-  __DATA.__objc_selrefs: 0x3310
-  __DATA.__objc_ivar: 0x4ac
-  __DATA.__objc_data: 0x16d0
-  __DATA.__data: 0x650
+  __DATA.__objc_const: 0xc4b0
+  __DATA.__objc_selrefs: 0x33a8
+  __DATA.__objc_ivar: 0x4b0
+  __DATA.__objc_data: 0x1720
+  __DATA.__data: 0x6b0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x260
+  __DATA.__bss: 0x270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AAFDDF2-6BDF-323F-BBBE-73174968B5F5
-  Functions: 3269
-  Symbols:   424
-  CStrings:  6751
+  UUID: 2EC04E9E-3CCC-3CAF-824F-245D880EED9D
+  Functions: 3301
+  Symbols:   428
+  CStrings:  6807
 
Symbols:
+ _CacheDeleteRegisterInfoCallbacks
+ _MobileInstallationInstallApp
+ _MobileInstallationStageApplicationUpdate
+ _OBJC_CLASS_$_MIStagedUpdateMetadata
+ _sandbox_extension_consume
+ _sandbox_extension_release
- _MobileInstallationInstallApplicationWithIdentityAndAssertionBlockWithError
- _MobileInstallationStageApplicationUpdateWithIdentityWithError
CStrings:
+ "%s: %@: Staged application for later install with staged metadata: %@"
+ "%s: %@: staged update with results %@"
+ "%s: Applying staged updates in response to disk space pressure: %@"
+ "%s: Called purge space block"
+ "%s: Called purgeable space block"
+ "%s: Failed to get termination assertion for %@ because an app extension was busy for %f seconds; transitioning to a critical termination assertion"
+ "%s: Failed to provide access to %@ : %@"
+ "%s: Failed to purge enough disk space. Required (%llu) : Achieved (%llu)"
+ "%s: Failed to register CacheDelete callbacks"
+ "%s: Nothing to purge on volume: %@"
+ "%s: Purged required disk space. Required (%llu) : Achieved (%llu)"
+ "%s: Unexpectedly received non string volume key: %@"
+ "%s: Value for CACHE_DELETE_AMOUNT_KEY is 0"
+ "%s: Value for CACHE_DELETE_AMOUNT_KEY is not of type NSNumber: %@"
+ "-[IXFileManager consumeSandboxExtension:error:]"
+ "-[IXFileManager issueSandboxExtensionForURL:withExtensionClass:error:]"
+ "-[IXFileManager releaseSandboxExtensionToken:error:]"
+ "-[IXSCacheDelete _onQueue_purge:urgency:]"
+ "-[IXSCacheDelete _onQueue_validateVolumeKey:]"
+ "-[IXSCacheDelete _purge:urgency:]_block_invoke"
+ "-[IXSCacheDelete _registerCacheDeleteInfoCallbacks]"
+ "-[IXSCacheDelete _registerCacheDeleteInfoCallbacks]_block_invoke"
+ "-[IXSClientConnection _remote_stagingLocationForInstallLocation:completion:]"
+ "22:31:58"
+ "@\"MIStagedUpdateMetadata\""
+ "@40@0:8@16r*24^@32"
+ "B32@0:8q16^@24"
+ "Failed to provide access to %@"
+ "IXSCacheDelete"
+ "IXSCacheDeleteUpdateCompleteDelegate"
+ "Jun 16 2025"
+ "Q24@0:8^@16"
+ "Q28@0:8Q16i24"
+ "T@\"MIStagedUpdateMetadata\",&,N,V_stagedUpdateMetadata"
+ "T@?,C,N,V_cacheDeleteCallback"
+ "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
+ "_cacheDeleteCallback"
+ "_onQueue_acquireAssertionForPlaceholder:forceAcquisition:"
+ "_onQueue_purge:urgency:"
+ "_onQueue_sizeForPurgeableCoordinators:"
+ "_onQueue_validateVolumeKey:"
+ "_purge:urgency:"
+ "_purgeable:urgency:"
+ "_registerCacheDeleteInfoCallbacks"
+ "_stagedUpdateMetadata"
+ "applyStagedUpdateAndRunBlockWhenComplete:"
+ "cacheDeleteCallback"
+ "com.apple.installcoordination.cachedelete.internal"
+ "com.apple.installcoordinationd.CacheDelete"
+ "consumeSandboxExtension:error:"
+ "decodeObjectForKey:"
+ "initForStagedIdentifier:diskUsage:"
+ "isUpdateScheduled"
+ "issueSandboxExtensionForURL:withExtensionClass:error:"
+ "q32@0:8@16^@24"
+ "releaseSandboxExtensionToken:error:"
+ "sandbox_extension_consume for %s failed: %s."
+ "sandbox_extension_issue_file for path %@ failed: %s"
+ "sandbox_extension_release for %lld failed: %s."
+ "scheduledUpdateComplete"
+ "setCacheDeleteCallback:"
+ "setStagedUpdateMetadata:"
+ "stagedDiskUsage"
+ "stagedIdentifier"
+ "stagedUpdateMetadata"
+ "stagedUpdateSizeOnDisk"
+ "v24@0:8B16B20"
+ "v32@0:8@\"<MILocationProtocol>\"16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24"
- "%s: %@: Staged application for later install with staging ID %@"
- "%s: %@: staged update identifier %@"
- "%s: Could not provide access to staging directory : %@"
- "%s: Failed to get termination assertion for %@ because an app extension was busy for %f seconds; skipping assertion"
- "04:44:52"
- "Could not provide access to staging directory"
- "Failed to create sandbox extension for com.apple.installcoordinationd for path %@"
- "May 23 2025"
- "T@\"NSString\",&,N,V_stagedUpdateIdentifier"
- "TB,R,N,V_isMacPlatformApp"
- "_onQueue_acquireAssertionForPlaceholder:"
- "_stagedUpdateIdentifier"
- "setStagedUpdateIdentifier:"
- "v32@0:8@\"<MILocationProtocol>\"16@?<v@?@\"NSURL\"@\"NSError\">24"

```
