## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2381.2.7.5.2
-  __TEXT.__text: 0xdf1e8
-  __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__objc_methlist: 0xa500
-  __TEXT.__const: 0x10f4
-  __TEXT.__cstring: 0x15bbd
-  __TEXT.__oslogstring: 0x83dc
-  __TEXT.__gcc_except_tab: 0xf80
+2400.4.12.0.0
+  __TEXT.__text: 0xe03fc
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_methlist: 0xaca4
+  __TEXT.__const: 0x1124
+  __TEXT.__cstring: 0x15ff6
+  __TEXT.__oslogstring: 0x8582
+  __TEXT.__gcc_except_tab: 0xf6c
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2c48
+  __TEXT.__unwind_info: 0x2d18
   __TEXT.__objc_classname: 0xc51
-  __TEXT.__objc_methname: 0x1c82a
+  __TEXT.__objc_methname: 0x1cc68
   __TEXT.__objc_methtype: 0x2149
-  __TEXT.__objc_stubs: 0xd260
+  __TEXT.__objc_stubs: 0xd400
   __DATA_CONST.__got: 0xa48
-  __DATA_CONST.__const: 0x4c48
+  __DATA_CONST.__const: 0x4c78
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5888
+  __DATA_CONST.__objc_selrefs: 0x59c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0xb60
+  __AUTH_CONST.__auth_got: 0xb58
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x2230
-  __AUTH_CONST.__cfstring: 0x18ca0
-  __AUTH_CONST.__objc_const: 0xdfe8
+  __AUTH_CONST.__const: 0x2250
+  __AUTH_CONST.__cfstring: 0x191c0
+  __AUTH_CONST.__objc_const: 0xd400
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x958
-  __DATA.__data: 0xb58
-  __DATA.__bss: 0xc89
+  __DATA.__objc_ivar: 0x968
+  __DATA.__data: 0xb68
+  __DATA.__bss: 0xc99
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1400
-  __DATA_DIRTY.__bss: 0x210
+  __DATA_DIRTY.__bss: 0x218
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4731
-  Symbols:   6784
-  CStrings:  8551
+  Functions: 5115
+  Symbols:   7196
+  CStrings:  8630
 
Symbols:
+ _MCFeatureAllowedCameraRestrictionBundleIDs
+ _MCFeatureAppleIntelligenceReportAllowed
+ _MCFeatureDefaultCallingAppModificationAllowed
+ _MCFeatureDefaultMessagingAppModificationAllowed
+ _MCFeatureSafariHistoryClearingAllowed
+ _MCFeatureSafariPrivateBrowsingAllowed
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
- _MKBLockDeviceNow
- _OBJC_CLASS_$_LSPlugInKitProxy
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "AKSGetStashStats"
+ "BROWSING_HISTORY_RETENTION"
+ "Bad Data"
+ "Crypto Error - Security Framework Error"
+ "Decode Error"
+ "Device Locked"
+ "Entitlement Error"
+ "Excluded FQDNs: %@\n"
+ "ExcludedFQDNs"
+ "FEATURE_APPLE_INTELLIGENCE_REPORT"
+ "FEATURE_CAMERA_RESTRICTION_BUNDLE_IDS"
+ "FEATURE_DEFAULT_CALLING_APP_MODIFICATION"
+ "FEATURE_DEFAULT_MESSAGING_APP_MODIFICATION"
+ "Failed to look get application extension record for bundleID %{public}@ Error: %{public}@"
+ "IOKit Error"
+ "Internal Error"
+ "Invalid Arguments"
+ "Invalid Bag"
+ "Invalid Secret"
+ "LockDeviceNow"
+ "MCPasscodeManager failed to lock device with MKB error: %{public}@ (%{public}d)"
+ "MCPasscodeManager failed to unlock device with empty passcode"
+ "MCPasscodeManager failed to unlock device with error: %{public}@"
+ "MCPasscodeManager failed to unlock device with passcode with MKB error: %{public}@ (%{public}d)"
+ "MCPasscodeManager ignoring device unlock because MobileKeyBag is disabled."
+ "MCPasscodeManager locking device immediately..."
+ "MCPasscodeManager locking device..."
+ "MCPasscodeManager successfully locked device"
+ "MCPasscodeManager successfully unlocked device with passcode."
+ "MCPasscodeManager unlocking device with passcode..."
+ "MKB Busy"
+ "MKB Error"
+ "MKB Exists"
+ "MKB Not Found"
+ "MKB Not Ready"
+ "Managed WLAN names error. Error: %{public}@"
+ "Match FQDNs: %@\n"
+ "MatchFQDNs"
+ "No Memory"
+ "Permission Failure"
+ "Policy Error - Device Unlock Disabled"
+ "Safari history retention:\n%@\n"
+ "SafariHistoryRetentionEnabled"
+ "Success"
+ "System Error - System Call Failed"
+ "T@\"NSArray\",R,C,N,V_excludedFQDNs"
+ "T@\"NSArray\",R,C,N,V_matchFQDNs"
+ "T@\"NSString\",C,N,V_uiToggleEnabled"
+ "TB,N,V_safariHistoryRetentionEnabled"
+ "UIToggleEnabled"
+ "UIToggleEnabled: %@\n"
+ "User Should Wipe - Unlock Failed"
+ "Wipe Error - Effaceable Storage Error"
+ "_boolFromDictOrDefaultTrue:key:outError:"
+ "_checkForValidContent:outError:"
+ "_checkForValidLegacyArrayContent:outError:"
+ "_excludedFQDNs"
+ "_finishInitializationWithContent:"
+ "_finishInitializationWithLegacyArrayContent:"
+ "_matchFQDNs"
+ "_mkbErrorStringForResult:"
+ "_safariHistoryRetentionEnabled"
+ "_uiToggleEnabled"
+ "allowAppleIntelligenceReport"
+ "allowDefaultCallingAppModification"
+ "allowDefaultMessagingAppModification"
+ "allowSafariHistoryClearing"
+ "allowSafariPrivateBrowsing"
+ "allowedCameraRestrictionBundleIDs"
+ "cloudConfigurationStoreDetailsForPendingMigration:completion:"
+ "containingBundleRecord"
+ "excludedFQDNs"
+ "geofenceWithID:latitude:longitude:radius:"
+ "initWithBundleIdentifier:error:"
+ "isAppleIntelligenceReportAllowed"
+ "isAppleIntelligenceRestricted"
+ "isDefaultCallingAppModificationAllowed"
+ "isDefaultMessagingAppModificationAllowed"
+ "isSafariHistoryClearingAllowed"
+ "isSafariPrivateBrowsingAllowed"
+ "matchFQDNs"
+ "removeProfileWithIdentifier:errorCompletion:"
+ "removeProfileWithIdentifier:installationType:errorCompletion:"
+ "safariHistoryRetentionEnabled"
+ "setSafariHistoryRetentionEnabled:"
+ "setUiToggleEnabled:"
+ "storePendingCloudConfigurationDetailsForMigration:completionHandler:"
+ "uiToggleEnabled"
- "Could not unlock device. Error: %{public}@"
- "Device is locked with a passcode."
- "Failed to unlock device with passcode with MKB status: %d"
- "Locking device immediately."
- "Locking device."
- "MCCellularPrivateNetworkPayload.m"
- "Managed WLAN network names error. Error: %{public}@"
- "MobileKeyBag is disabled."
- "Successfully unlocked device with passcode."
- "Unlocking device with passcode."
- "containingBundle"
- "pluginKitProxyForIdentifier:"

```
