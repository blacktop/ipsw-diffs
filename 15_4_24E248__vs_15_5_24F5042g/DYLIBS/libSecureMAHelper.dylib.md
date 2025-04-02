## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1487.101.2.0.0
-  __TEXT.__text: 0xf3f8
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x4cc
+1487.120.46.0.0
+  __TEXT.__text: 0x12238
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_methlist: 0x6d4
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x1dac
-  __TEXT.__oslogstring: 0x159f
-  __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__unwind_info: 0x2f0
-  __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0xef3
-  __TEXT.__objc_methtype: 0x1a6
-  __TEXT.__objc_stubs: 0x1220
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x260
+  __TEXT.__cstring: 0x210f
+  __TEXT.__oslogstring: 0x1d52
+  __TEXT.__gcc_except_tab: 0x814
+  __TEXT.__unwind_info: 0x320
+  __TEXT.__objc_classname: 0xea
+  __TEXT.__objc_methname: 0x1334
+  __TEXT.__objc_methtype: 0x461
+  __TEXT.__objc_stubs: 0x14a0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x270
-  __AUTH_CONST.__cfstring: 0x22a0
-  __AUTH_CONST.__objc_const: 0x5c8
+  __AUTH_CONST.__const: 0x2b0
+  __AUTH_CONST.__cfstring: 0x2520
+  __AUTH_CONST.__objc_const: 0x750
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x30
-  __DATA.__bss: 0x98
+  __DATA.__data: 0x180
+  __DATA.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/Versions/A/MobileAssetExclaveServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 184
-  Symbols:   707
-  CStrings:  643
+  Functions: 196
+  Symbols:   776
+  CStrings:  761
 
Symbols:
+ +[SecureMobileAssetBundle _requiresLiveExclaveNonce]
+ +[SecureMobileAssetBundle _requiresLiveExclaveNonce].cold.1
+ +[SecureMobileAssetBundle _shouldUseConclave:]
+ +[SecureMobileAssetBundle commitStagedManifestsToExclavesForSelectors:darwinOnly:error:]
+ +[SecureMobileAssetBundle getExclaveManager:]
+ -[SecureMobileAssetBundle _activateManifestInExclaves:error:]
+ -[SecureMobileAssetBundle _storeManifestToExclaves:infoPlist:stage:error:]
+ -[SecureMobileAssetBundle isPersonalizedForExclaves:staged:]
+ GCC_except_table107
+ GCC_except_table12
+ GCC_except_table31
+ GCC_except_table39
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table90
+ MABrainUtilityConclaveEnabled.answer
+ MABrainUtilityConclaveEnabled.cold.1
+ MABrainUtilityConclaveEnabled.onceToken
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_SecureMobileAssetExclaveManager
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1160
+ __MABrainUtilityConclaveEnabled_block_invoke.cold.1
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol
+ __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceProtocol2
+ ___52+[SecureMobileAssetBundle _requiresLiveExclaveNonce]_block_invoke
+ ___MABrainUtilityConclaveEnabled_block_invoke
+ __block_literal_global.1155
+ __block_literal_global.1261
+ __block_literal_global.1540
+ __block_literal_global.1754
+ __block_literal_global.405
+ __os_feature_enabled_impl
+ _getMappedExclavePath
+ _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
+ _objc_msgSend$_activateManifestInExclaves:error:
+ _objc_msgSend$_requiresLiveExclaveNonce
+ _objc_msgSend$_shouldUseConclave:
+ _objc_msgSend$_storeManifestToExclaves:infoPlist:stage:error:
+ _objc_msgSend$activateCommittedManifestForFSTag:specifier:error:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:
+ _objc_msgSend$checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:
+ _objc_msgSend$commitStagedManifestForFSTags:error:
+ _objc_msgSend$commitStagedManifestForFSTags:specifiers:error:
+ _objc_msgSend$commitStagedManifestsToExclavesForSelectors:darwinOnly:error:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$darwinOnly
+ _objc_msgSend$getExclaveManager:
+ _objc_msgSend$integrityCatalogPath
+ _objc_msgSend$isPersonalizedForExclaves:staged:
+ _objc_msgSend$proposeNonce:
+ _objc_msgSend$stageManifest:infoPlist:catalog:error:
+ _objc_msgSend$stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:
+ _objc_msgSend$storeManifest:infoPlist:catalog:error:
+ _requiresLiveExclaveNonce.onceToken
+ _requiresLiveExclaveNonce.required
- GCC_except_table32
- GCC_except_table36
- GCC_except_table41
- GCC_except_table42
- GCC_except_table46
- GCC_except_table47
- GCC_except_table51
- GCC_except_table66
- GCC_except_table79
- GCC_except_table80
- GCC_except_table81
- GCC_except_table97
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1070
- __block_literal_global.1258
- __block_literal_global.1424
- __block_literal_global.1607
CStrings:
+ "#16@0:8"
+ "@\"NSDictionary\"24@0:8^@16"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "Activating committed manifest is not supported on this OS"
+ "B20@0:8B16"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8I16B20"
+ "B28@0:8I16^@20"
+ "B32@0:8@\"NSArray\"16^@24"
+ "B36@0:8I16@\"NSString\"20^@28"
+ "B36@0:8I16@20^@28"
+ "B40@0:8@\"NSArray\"16@\"NSArray\"24^@32"
+ "B40@0:8@16@24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32^@40"
+ "B48@0:8@16@24@32^@40"
+ "B60@0:8I16@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44^@52"
+ "B60@0:8I16@20@28@36@44^@52"
+ "B64@0:8I16B20@\"NSData\"24@\"NSData\"32@\"NSData\"40^B48^@56"
+ "B64@0:8I16B20@24@32@40^B48^@56"
+ "B72@0:8I16@\"NSString\"20I28@\"NSData\"32@\"NSData\"40@\"NSData\"48^B56^@64"
+ "B72@0:8I16@20I28@32@40@48^B56^@64"
+ "Cannot map to Exclaves: _storeManifestToExclaves failed"
+ "Cannot map to Exclaves: info plist data is nil"
+ "Cannot map to Exclaves: info plist path is nil"
+ "Cannot map to Exclaves: ticket data is nil"
+ "Cannot map to Exclaves: ticket path is nil"
+ "Failed to activate committed manifest in Exclaves"
+ "Failed to allocate NSNumber for fstag"
+ "Failed to commit staged manifests to Exclaves"
+ "Failed to get exclave nonces"
+ "Failed to get shared instance of SecureMobileAssetExclave"
+ "LiveStorageExclaveNonce"
+ "MAExclaveManifestStorageServiceBaseProtocol"
+ "MAExclaveManifestStorageServiceProtocol"
+ "MAExclaveManifestStorageServiceProtocol2"
+ "MobileAsset"
+ "NSObject"
+ "Q16@0:8"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "ThirdPartyStagingBucketPathComponent"
+ "Unable to unregister fstag mapping"
+ "Vv16@0:8"
+ "[MAB] Boot session UUID has an invalid length (%zu)"
+ "[MAB] Caller canceled enumeration"
+ "[MAB] Canceled device unlock action (token=%d)..."
+ "[MAB] Could not allocate buffer to copy boot session UUID"
+ "[MAB] Could not copy boot session UUID: %d (%s)"
+ "[MAB] Could not create directory enumerator for %@"
+ "[MAB] Could not look up boot session UUID: %d (%s)"
+ "[MAB] Device is already unlocked.  Starting action \"%@\""
+ "[MAB] Device is now unlocked.  Starting action \"%@\" (token=%d)"
+ "[MAB] Device is still locked.  Deferring action \"%@\" (token=%d)"
+ "[MAB] Device unlock action \"%@\" is scheduled (token=%d)"
+ "[MAB] Error canceling device unlock action (token=%d). errno=%d (%s)"
+ "[MAB] Failed to write %@ with contents of dictionary:%@\n%@"
+ "[MAB] Got a NULL return from IORegistryEntryCreateCFProperty"
+ "[MAB] Got a non-CFData return value from IORegistryEntryCreateCFProperty for property %@"
+ "[SMA] \ndevnodes=%@"
+ "[SMA] %@ manifest for %@"
+ "[SMA] %@ unmount for %@"
+ "[SMA] %s"
+ "[SMA] <%@> has a registered Exclave mapped path [fstag=%d]: %@"
+ "[SMA] AMAuthInstallCreate() failed"
+ "[SMA] AMAuthInstallUpdaterCryptex1CopyTicket() failed: %@"
+ "[SMA] AMAuthInstallUpdaterCryptex1CopyTicket() is unavailable"
+ "[SMA] Activating committed manifest for %@:%@ fstag=%u"
+ "[SMA] Activating committed manifest is not supported on this OS"
+ "[SMA] All specifiers of AssetType %@ are configured to fail personalization"
+ "[SMA] Allow listed for Exclaves: %@:%@ fstag=%u"
+ "[SMA] Attempting to copy BuildManifest from %@ to %@"
+ "[SMA] Attempting to copy file from %@ to %@"
+ "[SMA] Attempting to symlink %@ to %@"
+ "[SMA] Begin access failed for secure asset (%@): %@"
+ "[SMA] Begin access successful for secure asset: %@"
+ "[SMA] Bundle already personalized and personalized manifest staged, skipping: %@"
+ "[SMA] Bundle already personalized, skipping: %@"
+ "[SMA] Cannot map to Exclaves: activate manifest failed"
+ "[SMA] Committing staged exclave manifests for fsTags and specifiers: [%@] [%@]"
+ "[SMA] Committing staged exclave manifests for fsTags: %@"
+ "[SMA] Committing staged manifests for selectors: %@"
+ "[SMA] Conflicting registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
+ "[SMA] Could not determine whether cryptex at %@ is graftable: %s"
+ "[SMA] Could not lstat %s"
+ "[SMA] Could not ungraft %s"
+ "[SMA] Cryptex at %@ is graftable"
+ "[SMA] Cryptex at %@ is not graftable"
+ "[SMA] Crytex is already dmg mounted"
+ "[SMA] Darwin nonce digest: %@"
+ "[SMA] Default %@ invalid. Uneven number of ':' separated elements:[%@]"
+ "[SMA] Depersonalizing %@"
+ "[SMA] Ejected %@ after mount failure"
+ "[SMA] End access failed for secure asset (%@): %@"
+ "[SMA] End access successful for secure asset: %@"
+ "[SMA] Exclave nonce digest: %@"
+ "[SMA] Failed to activate committed manifest because conclave manager instance is nil: %@"
+ "[SMA] Failed to activate committed manifest for %@:%@ fstag=%u %@"
+ "[SMA] Failed to allocate NSNumber for fstag=%d"
+ "[SMA] Failed to attach and mount cryptex disk image: %@"
+ "[SMA] Failed to attach cryptex disk image: %@"
+ "[SMA] Failed to commit staged manifests to Exclaves"
+ "[SMA] Failed to commit staged manifests: %@"
+ "[SMA] Failed to depersonalize: %@"
+ "[SMA] Failed to eject cryptex disk image previously mounted at %@: %@"
+ "[SMA] Failed to generate nonce proposal: %d (%s)"
+ "[SMA] Failed to get nonce dictionary from SecureMobileAssetExclave: %@"
+ "[SMA] Failed to get shared instance of SecureMobileAssetExclave"
+ "[SMA] Failed to get shared instance of SecureMobileAssetExclave: %@"
+ "[SMA] Failed to graft: %@"
+ "[SMA] Failed to personalize asset bundle: %@"
+ "[SMA] Failed to ungraft: %@"
+ "[SMA] Failed to unmount and eject cryptex disk image: %@"
+ "[SMA] Generating nonce proposal for darwin"
+ "[SMA] Generating nonce proposal for exclaves"
+ "[SMA] Img4DecodeGetManifest() failed for %@: %d"
+ "[SMA] Img4DecodeInit() failed for %@: %d"
+ "[SMA] Invalid ssoToken=%@"
+ "[SMA] Matching registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
+ "[SMA] No requestTags found in existing amai object. Creating new object"
+ "[SMA] No selectors specified"
+ "[SMA] Not adding additional requestTags to personalization request"
+ "[SMA] Not allow listed for Exclaves: %@:%@"
+ "[SMA] Nothing to eject!"
+ "[SMA] Obtained nonce (%lu bytes) and digest (%lu bytes)"
+ "[SMA] Operations will be restricted to darwin only"
+ "[SMA] Registering dissenter for volume: %@"
+ "[SMA] Registering unmount approval callback"
+ "[SMA] Removed personalized bundle: %@"
+ "[SMA] SecureMobileAsset did not contain a personalized entry for %@"
+ "[SMA] Setting headers: %@"
+ "[SMA] Signing server is '%@'"
+ "[SMA] Simulating personalization failure of asset(%@) due to default"
+ "[SMA] Successfully activated committed manifest for %@:%@ fstag=%u"
+ "[SMA] Successfully attached %@ with ID: %@"
+ "[SMA] Successfully ejected cryptex disk image previously mounted at %@"
+ "[SMA] Successfully grafted %@ onto %@"
+ "[SMA] Successfully mounted cryptex volume %@ at %@"
+ "[SMA] Successfully registered Exclave mapped path [fstag=%d] %@:%@: %s"
+ "[SMA] Successfully ungrafted %@ from the file system using %@"
+ "[SMA] Successfully unmounted cryptex volume %@ from %@"
+ "[SMA] Successfully unregistered Exclave mapped path [fstag=%d]: %@"
+ "[SMA] The current AssetType(%@) is in the list of those configured to fail personalization but the current specifier(%@) is not"
+ "[SMA] The current specifier(%@) of AssetType %@ is configured to fail personalization"
+ "[SMA] Unable to get SecureMobileAssetExclave instance in this environment"
+ "[SMA] Unable to set SSO token for user authlisting"
+ "[SMA] Unable to set signing server retry count | AMAuthInstallSetSigningServerRetry() failed with error %d (%@)"
+ "[SMA] Unregistering dissenter for volume: %@"
+ "[SMA] User-authlisting enabled."
+ "[SMA] Using overridden value for signing server"
+ "[SMA] WARNING: %@"
+ "[SMA] WARNING: Failed to eject %@ after mount failure: %@"
+ "[SMA] WARNING: Using software coprocessor parameters override:\n%@"
+ "[SMA] Warning: MAExclaveManifestStorageService does not support staging, commit is a no-op"
+ "[SMA] Warning: MAExclaveManifestStorageService does not support staging, storing manifest instead"
+ "[SMA] Warning: MASecureManifestStorage does not support staging, commit is a no-op"
+ "[SMA] Warning: MASecureManifestStorage does not support staging, returning nil"
+ "[SMA] Warning: MASecureManifestStorage does not support staging, storing manifest instead"
+ "[SMA] [Personalization] enqueue %@"
+ "[SMA] [Personalization] finish %@ (success = %i, error = %@)"
+ "[SMA] [Personalization] start %@"
+ "[SMA] [SecureMAHelper]: Creating new graft list for tracking grafted assets"
+ "[SMA] [SecureMAHelper]: Failed to create folder(%@) for grafted list file: %@"
+ "[SMA] [SecureMAHelper]: Failed to delete graft list file at %@ : %@"
+ "[SMA] [SecureMAHelper]: Failed to delete graft list file at path %@. Error: %@"
+ "[SMA] [SecureMAHelper]: Failed to load existing graft list at path %@. Error: %@"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@ to file %@: %@"
+ "[SMA] [SecureMAHelper]: Graft list does not exist at %@"
+ "[SMA] [SecureMAHelper]: Successfully created folder(%@) for grafted list file"
+ "[SMA] [SecureMAHelper]: Successfully recorded graft entry for asset of type %@"
+ "^{_NSZone=}16@0:8"
+ "_activateManifestInExclaves:error:"
+ "_requiresLiveExclaveNonce"
+ "_shouldUseConclave:"
+ "_storeManifestToExclaves:infoPlist:stage:error:"
+ "activateCommittedManifestForFSTag:specifier:error:"
+ "arrayWithObjects:count:"
+ "autorelease"
+ "checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:"
+ "checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:"
+ "class"
+ "com_apple_mobileassetd_conclave"
+ "commitStagedManifestForFSTags:error:"
+ "commitStagedManifestForFSTags:specifiers:error:"
+ "commitStagedManifestsToExclavesForSelectors:darwinOnly:error:"
+ "conformsToProtocol:"
+ "debugDescription"
+ "digestNonce"
+ "failed to get integrity catalog path"
+ "failed to read cryptex integrity catalog"
+ "failed to stage manifest in Exclave Secure Storage"
+ "failed to store manifest in Exclave Secure Storage"
+ "getExclaveManager:"
+ "hash"
+ "invalidateManifestForFSTag:error:"
+ "invalidateManifestForFSTag:specifier:error:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isPersonalizedForExclaves:staged:"
+ "isProxy"
+ "mappedPath"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "proposeNonce:"
+ "rawNonce"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "stageManifest:infoPlist:catalog:error:"
+ "stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:"
+ "storeManifest:infoPlist:catalog:error:"
+ "superclass"
+ "zone"
- "\ndevnodes=%@"
- "%@ manifest for %@"
- "%@ unmount for %@"
- "%s"
- "AMAuthInstallCreate() failed"
- "AMAuthInstallUpdaterCryptex1CopyTicket() failed: %@"
- "AMAuthInstallUpdaterCryptex1CopyTicket() is unavailable"
- "All specifiers of AssetType %@ are configured to fail personalization"
- "Allow listed for Exclaves: %@:%@ fstag=%u"
- "Attempting to copy BuildManifest from %@ to %@"
- "Attempting to copy file from %@ to %@"
- "Attempting to symlink %@ to %@"
- "Begin access failed for secure asset (%@): %@"
- "Begin access successful for secure asset: %@"
- "Boot session UUID has an invalid length (%zu)"
- "Bundle already personalized and personalized manifest staged, skipping: %@"
- "Bundle already personalized, skipping: %@"
- "Caller canceled enumeration"
- "Canceled device unlock action (token=%d)..."
- "Committing staged manifests for selectors: %@"
- "Conflicting registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
- "Could not allocate buffer to copy boot session UUID"
- "Could not copy boot session UUID: %d (%s)"
- "Could not create directory enumerator for %@"
- "Could not determine whether cryptex at %@ is graftable: %s"
- "Could not look up boot session UUID: %d (%s)"
- "Could not lstat %s"
- "Could not ungraft %s"
- "Cryptex at %@ is graftable"
- "Cryptex at %@ is not graftable"
- "Crytex is already dmg mounted"
- "Darwin nonce digest: %@"
- "Default %@ invalid. Uneven number of ':' separated elements:[%@]"
- "Depersonalizing %@"
- "Device is already unlocked.  Starting action \"%@\""
- "Device is now unlocked.  Starting action \"%@\" (token=%d)"
- "Device is still locked.  Deferring action \"%@\" (token=%d)"
- "Device unlock action \"%@\" is scheduled (token=%d)"
- "Ejected %@ after mount failure"
- "End access failed for secure asset (%@): %@"
- "End access successful for secure asset: %@"
- "Error canceling device unlock action (token=%d). errno=%d (%s)"
- "Exclave nonce digest: %@"
- "Failed to attach and mount cryptex disk image: %@"
- "Failed to attach cryptex disk image: %@"
- "Failed to commit staged manifests: %@"
- "Failed to depersonalize: %@"
- "Failed to eject cryptex disk image previously mounted at %@: %@"
- "Failed to generate nonce proposal: %d (%s)"
- "Failed to graft: %@"
- "Failed to personalize asset bundle: %@"
- "Failed to ungraft: %@"
- "Failed to unmount and eject cryptex disk image: %@"
- "Failed to write %@ with contents of dictionary:%@\n%@"
- "Generating nonce proposal for darwin"
- "Got a NULL return from IORegistryEntryCreateCFProperty"
- "Got a non-CFData return value from IORegistryEntryCreateCFProperty for property %@"
- "Img4DecodeGetManifest() failed for %@: %d"
- "Img4DecodeInit() failed for %@: %d"
- "Invalid ssoToken=%@"
- "Matching registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
- "No requestTags found in existing amai object. Creating new object"
- "Not adding additional requestTags to personalization request"
- "Not allow listed for Exclaves: %@:%@"
- "Nothing to eject!"
- "Obtained nonce (%lu bytes) and digest (%lu bytes)"
- "Registering dissenter for volume: %@"
- "Registering unmount approval callback"
- "Removed personalized bundle: %@"
- "SecureMobileAsset did not contain a personalized entry for %@"
- "Setting headers: %@"
- "Signing server is '%@'"
- "Simulating personalization failure of asset(%@) due to default"
- "Successfully attached %@ with ID: %@"
- "Successfully ejected cryptex disk image previously mounted at %@"
- "Successfully grafted %@ onto %@"
- "Successfully mounted cryptex volume %@ at %@"
- "Successfully registered Exclave mapped path [fstag=%d] %@:%@: %s"
- "Successfully ungrafted %@ from the file system using %@"
- "Successfully unmounted cryptex volume %@ from %@"
- "The current AssetType(%@) is in the list of those configured to fail personalization but the current specifier(%@) is not"
- "The current specifier(%@) of AssetType %@ is configured to fail personalization"
- "Unable to set SSO token for user authlisting"
- "Unable to set signing server retry count | AMAuthInstallSetSigningServerRetry() failed with error %d (%@)"
- "Unregistering dissenter for volume: %@"
- "User-authlisting enabled."
- "Using overridden value for signing server"
- "WARNING: Failed to eject %@ after mount failure: %@"
- "WARNING: Using software coprocessor parameters override:\n%@"
- "Warning: MASecureManifestStorage does not support staging, commit is a no-op"
- "Warning: MASecureManifestStorage does not support staging, returning nil"
- "Warning: MASecureManifestStorage does not support staging, storing manifest instead"
- "[Personalization] enqueue %@"
- "[Personalization] finish %@ (success = %i, error = %@)"
- "[Personalization] start %@"
- "[SecureMAHelper]: Creating new graft list for tracking grafted assets"
- "[SecureMAHelper]: Failed to create folder(%@) for grafted list file: %@"
- "[SecureMAHelper]: Failed to delete graft list file at %@ : %@"
- "[SecureMAHelper]: Failed to delete graft list file at path %@. Error: %@"
- "[SecureMAHelper]: Failed to load existing graft list at path %@. Error: %@"
- "[SecureMAHelper]: Failed to record %@ entry for asset of type %@ to file %@: %@"
- "[SecureMAHelper]: Graft list does not exist at %@"
- "[SecureMAHelper]: Successfully created folder(%@) for grafted list file"
- "[SecureMAHelper]: Successfully recorded graft entry for asset of type %@"

```
