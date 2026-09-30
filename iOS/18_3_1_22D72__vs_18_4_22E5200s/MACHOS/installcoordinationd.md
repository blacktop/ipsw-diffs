## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-631.82.1.0.0
-  __TEXT.__text: 0x97c7c
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0xa540
-  __TEXT.__objc_methlist: 0x4c80
-  __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x1716b
-  __TEXT.__objc_classname: 0x9bf
-  __TEXT.__oslogstring: 0xd130
-  __TEXT.__objc_methtype: 0x21ad
-  __TEXT.__objc_methname: 0xfc1d
-  __TEXT.__gcc_except_tab: 0x28b0
-  __TEXT.__ustring: 0x1966
+699.100.7.0.0
+  __TEXT.__text: 0x9a764
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_stubs: 0xa780
+  __TEXT.__objc_methlist: 0x584c
+  __TEXT.__const: 0x200
+  __TEXT.__cstring: 0x177f1
+  __TEXT.__objc_methname: 0x10044
+  __TEXT.__objc_classname: 0x9d4
+  __TEXT.__objc_methtype: 0x224b
+  __TEXT.__oslogstring: 0xd3eb
+  __TEXT.__gcc_except_tab: 0x28c4
+  __TEXT.__ustring: 0x1a64
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x22b8
-  __DATA_CONST.__auth_got: 0x840
-  __DATA_CONST.__got: 0x408
+  __TEXT.__unwind_info: 0x2358
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x410
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x29a0
-  __DATA_CONST.__cfstring: 0x90e0
-  __DATA_CONST.__objc_classlist: 0x238
+  __DATA_CONST.__const: 0x2a40
+  __DATA_CONST.__cfstring: 0x94e0
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xcd30
-  __DATA.__objc_selrefs: 0x2ff0
-  __DATA.__objc_ivar: 0x454
-  __DATA.__objc_data: 0x1630
+  __DATA.__objc_const: 0xbce0
+  __DATA.__objc_selrefs: 0x3130
+  __DATA.__objc_ivar: 0x470
+  __DATA.__objc_data: 0x1680
   __DATA.__data: 0x650
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x260

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3091
-  Symbols:   406
-  CStrings:  5227
+  Functions: 3140
+  Symbols:   412
+  CStrings:  5315
 
Symbols:
+ _MobileInstallationCancelUpdateForStagedIdentifiersWithError
+ _MobileInstallationGetAllStagedUpdateIdentifiers
+ _MobileInstallationInstallParallelPlaceholderForStagedUpdate
+ _MobileInstallationMakeStagedUpdateLiveForIdentifier
+ _MobileInstallationStageApplicationUpdateWithIdentityWithError
+ __kCFBundleShortVersionStringKey
CStrings:
+ "\x1e"
+ "#\x17S!\x15\x19!\x13\x16\""
+ "%s: %@: Staged application for later install with staging ID %@"
+ "%s: %@: staged update identifier %@"
+ "%s: Call to %@ SPI returned retryable error %@; retrying in %d seconds (%lu/%lu tries)"
+ "%s: Cleaning up orphaned staged updates: %@"
+ "%s: Failed to cancel staged update for %@ : %@"
+ "%s: Failed to clean up abandoned staged updates %@"
+ "%s: Failed to get tracked staged updates from installd: %@"
+ "%s: Failed to stage update for %@ : %@"
+ "%s: No tracked staged updates with installd"
+ "%s: Staging background app update - not acquiring termination assertion to stage %@"
+ "%s: Unexpectedly found existing power assertion for background scheduled update: %@"
+ "%s: Unexpectedly found placeholder in staging state"
+ "%s: Unexpectedly got empty list of preferred app marketplaces : %@"
+ "%s: Unexpectedly got nil for default NFC app : %@"
+ "%s: Unexpectedly got unknown default app type %lu : %@"
+ "-[IXSCoordinatedAppInstall _limitedConcurrency_installApplication:isPlaceholder:options:hasStagedUpdateWithIdentifier:retries:error:]"
+ "-[IXSCoordinatedAppInstall _limitedConcurrency_installApplication:isPlaceholder:options:hasStagedUpdateWithIdentifier:retries:error:]_block_invoke"
+ "-[IXSCoordinatedAppInstall _limitedConcurrency_installApplication:isPlaceholder:options:hasStagedUpdateWithIdentifier:retries:error:]_block_invoke_3"
+ "-[IXSCoordinatedAppInstall _onQueue_cancelStagedUpdate]_block_invoke"
+ "-[IXSCoordinatedAppInstall _onQueue_doInstall]_block_invoke_2"
+ "-[IXSCoordinatedAppInstall _onQueue_gizmoInstallForInstallOptions:appAssetAtPath:]"
+ "-[IXSCoordinatedAppInstall _onQueue_updatePlaceholderForFailureReason:client:installType:]"
+ "-[IXSCoordinatedAppInstall _shouldRetryInstallAttemptBasedOnPreviousResult:returnedError:targetInstallURL:retriesAttempted:totalRetries:]"
+ "-[IXSCoordinatedAppInstall scheduledAppUpdateReadyToExecuteAndRunBlockWhenComplete:]"
+ "-[IXSCoordinatedAppInstall stageUpdateFromAppAsset:options:retries:error:]"
+ "07:42:34"
+ "@48@0:8@16@24Q32^@40"
+ "@60@0:8@16B24@28@36Q44^@52"
+ "B52@0:8B16@20@28Q36Q44"
+ "Canceling staged update"
+ "DEFAULT_APP_NAVIGATION_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_SELECT_NAVIGATION_APP_BODY"
+ "DEFAULT_APP_SELECT_TRANSLATION_APP_BODY"
+ "DEFAULT_APP_TRANSLATION_SELECT_DELETE_APP_TITLE"
+ "Failed to stage background update."
+ "Failed to stage update for %@"
+ "Feb 16 2025"
+ "IXAppCoordinationStateReadyForStaging"
+ "IXAppCoordinationStateStagingPending"
+ "IXDefaultAppMetadata"
+ "NSAccentColorName"
+ "Select Another Default Navigation App"
+ "Select Another Default Translation App"
+ "Stage install update"
+ "T@\"IXApplicationIdentity\",R,N,V_identity"
+ "T@\"NSDictionary\",C,N,V_uiLaunchScreen"
+ "T@\"NSString\",&,N,V_stagedUpdateIdentifier"
+ "T@\"NSString\",C,N,V_accentColorName"
+ "T@\"NSString\",C,N,V_bundleShortVersionString"
+ "TEST_MODE_RESTRICT_DEFAULT_APP_DELETION_CANNOT_OFFLOAD_APPS_IDENTIFIER_KEY"
+ "TEST_MODE_RESTRICT_DEFAULT_APP_DELETION_CANNOT_OFFLOAD_APPS_KEY"
+ "TQ,R,N,V_offloadAnswer"
+ "UILaunchScreen"
+ "UNINSTALL_ICON_BODY_NAVIGATION"
+ "UNINSTALL_ICON_BODY_TRANSLATION"
+ "Unexpectedly got empty list of preferred app marketplaces"
+ "Unexpectedly got nil for default NFC app"
+ "Unexpectedly got unknown default app type %lu"
+ "You do not have any other navigation apps on this iPhone."
+ "You do not have any other translation apps on this iPhone."
+ "_RemoveOrphanedStagedUpdates"
+ "_accentColorName"
+ "_bundleIDForDefaultAppType"
+ "_bundleShortVersionString"
+ "_isStagedUpdate"
+ "_limitedConcurrency_installApplication:isPlaceholder:options:hasStagedUpdateWithIdentifier:retries:error:"
+ "_offloadAnswer"
+ "_onQueue_cancelStagedUpdate"
+ "_onQueue_gizmoInstallForInstallOptions:appAssetAtPath:"
+ "_remote_defaultAppMetadataForAppIdentity:completion:"
+ "_remote_defaultAppMetadataListWithCompletion:"
+ "_shouldRetryInstallAttemptBasedOnPreviousResult:returnedError:targetInstallURL:retriesAttempted:totalRetries:"
+ "_stagedUpdateIdentifier"
+ "_uiLaunchScreen"
+ "accentColorName"
+ "bundleShortVersionString"
+ "defaultAppMetadataForAppIdentity:error:"
+ "defaultAppMetadataListWithError:"
+ "defaultApplicationForCategory:error:"
+ "initWithAppIdentity:appType:offloadAnswer:"
+ "install"
+ "offloadAnswer"
+ "setAccentColorName:"
+ "setApplicationRelationship:"
+ "setBundleShortVersionString:"
+ "setRelatedApplications:"
+ "setStagedUpdateIdentifier:"
+ "setUiLaunchScreen:"
+ "stage update"
+ "stageUpdateFromAppAsset:options:retries:error:"
+ "stagedUpdateIdentifier"
+ "trackingStagedUpdateIdentifier"
+ "twoStageAppInstallEnabled"
+ "uiLaunchScreen"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "v32@0:8@\"IXApplicationIdentity\"16@?<v@?@\"IXDefaultAppMetadata\"@\"NSError\">24"
+ "\xf0q"
- "\x1b"
- "\"\x17S!\x15\x19!\x13\x16\""
- "%s: Call to install SPI returned retryable error %@; retrying in %d seconds (%lu/%lu tries)"
- "%s: No LSApplicationRecord found for %@, assuming uninstalled, skipping"
- "-[IXSAppDeletionEligibilityManager _onQueue_updateRemovabilityForAppIdentities:usingEligibilityAnswer:]_block_invoke"
- "-[IXSCoordinatedAppInstall _limitedConcurrency_installApplication:isPlaceholder:options:retries:error:]"
- "-[IXSCoordinatedAppInstall _limitedConcurrency_installApplication:isPlaceholder:options:retries:error:]_block_invoke"
- "-[IXSCoordinatedAppInstall _limitedConcurrency_installApplication:isPlaceholder:options:retries:error:]_block_invoke_3"
- "04:41:36"
- "@52@0:8@16B24@28Q36^@44"
- "Jan 16 2025"
- "PPBundleMetadata"
- "_appTypeForLSDefaultAppCategory:"
- "_limitedConcurrency_installApplication:isPlaceholder:options:retries:error:"
- "_lsDefaultAppCategoryForAppType:"
- "setRequiresUserInactivity:"
- "\xf0a"

```
