## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-554.80.2.0.0
-  __TEXT.__text: 0x8384c
+579.102.3.0.0
+  __TEXT.__text: 0x858c0
   __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0x8ca0
-  __TEXT.__objc_methlist: 0x426c
+  __TEXT.__objc_stubs: 0x8e00
+  __TEXT.__objc_methlist: 0x42bc
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x13781
+  __TEXT.__cstring: 0x13e5b
   __TEXT.__objc_classname: 0x84e
-  __TEXT.__objc_methname: 0xdc3e
-  __TEXT.__oslogstring: 0xb34c
-  __TEXT.__objc_methtype: 0x1eae
-  __TEXT.__gcc_except_tab: 0x1b20
+  __TEXT.__objc_methname: 0xdd36
+  __TEXT.__oslogstring: 0xb787
+  __TEXT.__objc_methtype: 0x1f31
+  __TEXT.__gcc_except_tab: 0x1cd4
   __TEXT.__ustring: 0x26c
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x1e50
+  __TEXT.__unwind_info: 0x1eb4
   __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2408
-  __DATA_CONST.__cfstring: 0x7580
+  __DATA_CONST.__const: 0x24b8
+  __DATA_CONST.__cfstring: 0x7840
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xb9f0
-  __DATA.__objc_selrefs: 0x2940
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x390
-  __DATA.__objc_superrefs: 0x190
-  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_const: 0xba00
+  __DATA.__objc_selrefs: 0x29a0
+  __DATA.__objc_ivar: 0x3d4
   __DATA.__objc_data: 0x12c0
   __DATA.__data: 0x590
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1d0
+  __DATA.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8731930B-A658-3288-BC4F-1BF7F36B5384
-  Functions: 2788
+  UUID: 745C7212-1788-3D18-9187-AB3224ECEBA7
+  Functions: 2815
   Symbols:   367
-  CStrings:  5457
+  CStrings:  5534
 
Symbols:
+ _MobileInstallationUpdateSinfDataForInstallCoordination
- _MobileInstallationUpdateSinfForInstallCoordination
CStrings:
+ "\"\x17S!\x15\x19!\x13\x16"
+ "%s: %@: Not updating loading progress: no relevant promises set"
+ "%s: %@: Not updating loading progress: user data promise is complete, but we have no app asset yet for this restoring coordinator."
+ "%s: Cannot demote app with identity %@ because it is a placeholder : %@"
+ "%s: Client %@ setting the %@ did not have the required entitlement \"%@\" = TRUE to allow the distribution info in the store metadata to be set (supplied distributor ID was '%@'). : %@"
+ "%s: Client %@ setting the install options did not have the required entitlement to allow the linkedParentBundleID property of the supplied MIInstallOptions to be set to '%@' (found \"com.apple.private.mobileinstall.allowed-linked-parents\" = %@) : %@"
+ "%s: Client attempted to set metadata promise that was not complete: %@ : %@"
+ "%s: Failed to decode MIInstallOptions from promise %@ : %@"
+ "%s: Failed to locate install options promise with UUID %@ : %@"
+ "%s: Failed to read iTunesMetadata.plist from %@ when demoting %@ : %@"
+ "%s: Got exception while trying to encode object %@ : %@ : %@"
+ "%s: LSApplicationRecord for %@ did not contain a bundleContainerURL during demotion : %@"
+ "%s: Metadata promise %@ did not contain a decodeable MIStoreMetadata instance. : %@"
+ "%s: No LSApplicationRecord found for %@ during demotion : %@"
+ "%s: No coordinator found for %@ and app is not vendable by App Store so showing alert"
+ "%s: No coordinator found for %@ and app is vendable by App Store (error %ld); sending message to prioritize by identity to %@."
+ "%s: No coordinator found for %@ and error is a hard error (%ld) so showing alert"
+ "%s: No coordinator found for %@ and prioritize is otherwise unhandled; showing alert"
+ "+[IXSCoordinatedAppInstall _fetchInstallOptionsFromPromise:error:]"
+ "+[IXSPlaceholder _metadataFromPromise:]"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:getInstallOptions:]"
+ "-[IXSClientConnection _remote_IXSCoordinatedAppInstall:getInstallOptions:]_block_invoke"
+ "-[IXSClientConnection _remote_updateiTunesMetadata:forAppWithIdentity:completion:]"
+ "-[IXSClientConnection _remote_updateiTunesMetadata:forAppWithIdentity:completion:]_block_invoke"
+ "-[IXSCoordinatedAppInstall _onQueue_fetchMetadataFromInstalledAppForOffloadWithError:]"
+ "-[IXSCoordinatedAppInstall(IPCMethods) _validateParentLinkageForInstallOptions:connection:error:]"
+ "-[IXSPlaceholder(IXSPlaceholderIPCMethods) _remote_setMetadataPromiseUUID:fromConnection:completion:]"
+ "22:32:53"
+ "Cannot demote app with identity %@ because it is a placeholder"
+ "Client %@ setting the %@ did not have the required entitlement \"%@\" = TRUE to allow the distribution info in the store metadata to be set (supplied distributor ID was '%@')."
+ "Client %@ setting the install options did not have the required entitlement to allow the linkedParentBundleID property of the supplied MIInstallOptions to be set to '%@' (found \"com.apple.private.mobileinstall.allowed-linked-parents\" = %@)"
+ "Client attempted to set metadata promise that was not complete: %@"
+ "Delete App Marketplace"
+ "Device is not eligible to install this app."
+ "Failed to decode MIInstallOptions from promise %@"
+ "Failed to locate install options promise with UUID %@"
+ "Failed to read iTunesMetadata.plist from %@ when demoting %@"
+ "Feb 16 2024"
+ "Got exception while trying to encode object %@ : %@"
+ "IXEncodeRootObject"
+ "IXSanitizeAndValidateRestrictedStoreMetadata"
+ "LSApplicationRecord for %@ did not contain a bundleContainerURL during demotion"
+ "Metadata promise %@ did not contain a decodeable MIStoreMetadata instance."
+ "No LSApplicationRecord found for %@ during demotion"
+ "No metadata found for app %@"
+ "Removing from Home Screen will keep the app marketplace in your App Library. If you delete this marketplace, apps installed from this marketplace will no longer update."
+ "T@\"NSString\",?,R,C"
+ "This app could not be installed because this device is not eligible to install it."
+ "UNINSTALL_ICON_BODY_MOVE_TO_APP_LIBRARY_MARKETPLACE"
+ "UNINSTALL_ICON_BUTTON_DELETE_MARKETPLACE"
+ "UNINSTALL_ICON_TITLE_MOVE_TO_APP_LIBRARY_OR_DELETE_MARKETPLACE"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"MIInstallOptions\"@\"NSError\">24"
+ "_fetchInstallOptionsFromPromise:error:"
+ "_metadataFromPromise:"
+ "_onQueue_fetchMetadataFromInstalledAppForOffloadWithError:"
+ "_remote_IXSCoordinatedAppInstall:getInstallOptions:"
+ "_remote_getInstallOptions:"
+ "_remote_setMetadataPromiseUUID:fromConnection:completion:"
+ "_remote_updateiTunesMetadata:forAppWithIdentity:completion:"
+ "_runAsyncBlockWithDescription:onUninstallQueue:"
+ "_validateParentLinkageForInstallOptions:connection:error:"
+ "bundleContainerURL"
+ "com.apple.private.install.distributor-info-source"
+ "distributorID"
+ "distributorInfo"
+ "distributorIsFirstPartyApple"
+ "iTunesMetadata.plist"
+ "install options"
+ "isManagedAppDistributor"
+ "kIXUserPresentableDeviceNotEligibleError"
+ "metadataFromPlistAtURL:error:"
+ "placeholder metadata"
+ "setInstallIntent:"
+ "uninstallConcurrencyQueue"
+ "updated metadata"
+ "updatedPromiseWithData:error:"
+ "v40@0:8@\"MIStoreMetadata\"16@\"IXApplicationIdentity\"24@?<v@?@\"NSError\">32"
- "\"\x17S!\x15\x19!\x13\x17"
- "%s: Failed to locate install options data promise with UUID %@ : %@"
- "%s: No coordinator found for %@ and app is not vendable by App Store or is a hard error (%ld) so showing alert"
- "%s: No coordinator found for %@ and app is vendable by App Store (error %ld); sending message to prioritize by identity."
- "%s: The client setting the install options promise did not have the required entitlement to allow the linkedParentBundleID property of the supplied MIInstallOptions to be set to '%@' (found \"com.apple.private.mobileinstall.allowed-linked-parents\" = %@) : %@"
- "-[IXSClientConnection _remote_updateiTunesMetadataForAppWithIdentity:plistData:options:completion:]"
- "-[IXSClientConnection _remote_updateiTunesMetadataForAppWithIdentity:plistData:options:completion:]_block_invoke"
- "-[IXSPlaceholder metadata]"
- "-[IXSPlaceholder(IXSPlaceholderIPCMethods) _remote_setMetadataPromiseUUID:completion:]"
- "18:56:55"
- "Dec 20 2023"
- "Failed to locate install options data promise with UUID %@"
- "T@\"NSArray\",&,N,V_installOptionsSetterAllowedLinkedParentBundleIDs"
- "The client setting the install options promise did not have the required entitlement to allow the linkedParentBundleID property of the supplied MIInstallOptions to be set to '%@' (found \"com.apple.private.mobileinstall.allowed-linked-parents\" = %@)"
- "_installOptionsSetterAllowedLinkedParentBundleIDs"
- "_remote_setMetadataPromiseUUID:completion:"
- "_remote_updateiTunesMetadataForAppWithIdentity:plistData:options:completion:"
- "initWithLegacyOptionsDictionary:"
- "installOptionsSetterAllowedLinkedParentBundleIDs"
- "legacyOptionsDictionary"
- "setInstallOptionsSetterAllowedLinkedParentBundleIDs:"

```
