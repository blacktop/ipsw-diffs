## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1487.102.2.0.0
-  __TEXT.__text: 0xf418
+1487.120.46.0.0
+  __TEXT.__text: 0x10050
   __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x448
+  __TEXT.__objc_methlist: 0x614
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x201f
-  __TEXT.__oslogstring: 0x1829
-  __TEXT.__gcc_except_tab: 0x6a8
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__objc_classname: 0x44
-  __TEXT.__objc_methname: 0xec0
-  __TEXT.__objc_methtype: 0x166
-  __TEXT.__objc_stubs: 0x1240
+  __TEXT.__cstring: 0x20c8
+  __TEXT.__oslogstring: 0x1cb6
+  __TEXT.__gcc_except_tab: 0x758
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_classname: 0xca
+  __TEXT.__objc_methname: 0x11b1
+  __TEXT.__objc_methtype: 0x3f3
+  __TEXT.__objc_stubs: 0x1360
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x518
+  __DATA_CONST.__objc_selrefs: 0x5f0
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4f8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x2480
-  __AUTH_CONST.__objc_const: 0x498
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x24e0
+  __AUTH_CONST.__objc_const: 0x620
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x24
-  __DATA.__bss: 0x90
+  __DATA.__data: 0x180
+  __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 164
-  Symbols:   464
-  CStrings:  655
+  Functions: 168
+  Symbols:   469
+  CStrings:  727
 
Symbols:
+ _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
CStrings:
+ "#16@0:8"
+ "@\"NSDictionary\"24@0:8^@16"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "Activating committed manifest is not supported on this OS"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B28@0:8I16^@20"
+ "B32@0:8@\"NSArray\"16^@24"
+ "B36@0:8I16@\"NSString\"20^@28"
+ "B36@0:8I16@20^@28"
+ "B40@0:8@\"NSArray\"16@\"NSArray\"24^@32"
+ "B40@0:8@16@24^@32"
+ "B48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32^@40"
+ "B48@0:8@16@24@32^@40"
+ "B60@0:8I16@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44^@52"
+ "B60@0:8I16@20@28@36@44^@52"
+ "B64@0:8I16B20@\"NSData\"24@\"NSData\"32@\"NSData\"40^B48^@56"
+ "B64@0:8I16B20@24@32@40^B48^@56"
+ "B72@0:8I16@\"NSString\"20I28@\"NSData\"32@\"NSData\"40@\"NSData\"48^B56^@64"
+ "B72@0:8I16@20I28@32@40@48^B56^@64"
+ "Failed to activate committed manifest in Exclaves"
+ "LiveStorageExclaveNonce"
+ "MAExclaveManifestStorageServiceBaseProtocol"
+ "MAExclaveManifestStorageServiceProtocol"
+ "MAExclaveManifestStorageServiceProtocol2"
+ "NSObject"
+ "Q16@0:8"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "ThirdPartyStagingBucketPathComponent"
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
+ "activateCommittedManifestForFSTag:specifier:error:"
+ "autorelease"
+ "checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:"
+ "checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:"
+ "class"
+ "commitStagedManifestForFSTags:specifiers:error:"
+ "conformsToProtocol:"
+ "debugDescription"
+ "hash"
+ "invalidateManifestForFSTag:error:"
+ "invalidateManifestForFSTag:specifier:error:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:"
+ "superclass"
+ "zone"
- "\ndevnodes=%@"
- "%@ manifest for %@"
- "%s"
- "<%@> has a registered Exclave mapped path [fstag=%d]: %@"
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
- "Committing staged exclave manifests for fsTags: %@"
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
- "Failed to allocate NSNumber for fstag=%d"
- "Failed to attach and mount cryptex disk image: %@"
- "Failed to attach cryptex disk image: %@"
- "Failed to commit staged manifests: %@"
- "Failed to depersonalize: %@"
- "Failed to eject cryptex disk image previously mounted at %@: %@"
- "Failed to generate nonce proposal: %d (%s)"
- "Failed to get nonce dictionary from SecureMobileAssetExclave: %@"
- "Failed to get shared instance of SecureMobileAssetExclave: %@"
- "Failed to graft: %@"
- "Failed to personalize asset bundle: %@"
- "Failed to ungraft: %@"
- "Failed to unmount and eject cryptex disk image: %@"
- "Failed to write %@ with contents of dictionary:%@\n%@"
- "Generating nonce proposal for darwin"
- "Generating nonce proposal for exclaves"
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
- "Operations will be restricted to darwin only"
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
- "Successfully unregistered Exclave mapped path [fstag=%d]: %@"
- "The current AssetType(%@) is in the list of those configured to fail personalization but the current specifier(%@) is not"
- "The current specifier(%@) of AssetType %@ is configured to fail personalization"
- "Unable to get SecureMobileAssetExclave instance in this environment"
- "Unable to set SSO token for user authlisting"
- "Unable to set signing server retry count | AMAuthInstallSetSigningServerRetry() failed with error %d (%@)"
- "User-authlisting enabled."
- "Using overridden value for signing server"
- "WARNING: %@"
- "WARNING: Failed to eject %@ after mount failure: %@"
- "WARNING: Using software coprocessor parameters override:\n%@"
- "Warning: MAExclaveManifestStorageService does not support staging, commit is a no-op"
- "Warning: MAExclaveManifestStorageService does not support staging, storing manifest instead"
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
