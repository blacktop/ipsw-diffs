## wifid

> `/usr/sbin/wifid`

```diff

-1675.21.3.1.0
-  __TEXT.__text: 0x17e274
-  __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_stubs: 0x10ae0
+1680.9.0.0.0
+  __TEXT.__text: 0x180500
+  __TEXT.__auth_stubs: 0x2560
+  __TEXT.__objc_stubs: 0x10b20
   __TEXT.__objc_methlist: 0x4f54
-  __TEXT.__objc_methname: 0x1605f
+  __TEXT.__objc_methname: 0x160af
   __TEXT.__objc_classname: 0x7ab
   __TEXT.__objc_methtype: 0x2b9f
   __TEXT.__const: 0x8c0
   __TEXT.__gcc_except_tab: 0x182c
-  __TEXT.__cstring: 0x63a91
+  __TEXT.__cstring: 0x646b0
   __TEXT.__ustring: 0x4c2
-  __TEXT.__oslogstring: 0x245
+  __TEXT.__oslogstring: 0x30d
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3338
-  __DATA_CONST.__auth_got: 0x12b8
+  __TEXT.__unwind_info: 0x33cc
+  __DATA_CONST.__auth_got: 0x12c0
   __DATA_CONST.__got: 0xfd0
   __DATA_CONST.__auth_ptr: 0x138
-  __DATA_CONST.__const: 0x68a8
-  __DATA_CONST.__cfstring: 0x1ba60
+  __DATA_CONST.__const: 0x6958
+  __DATA_CONST.__cfstring: 0x1bac0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0xd500
-  __DATA.__objc_selrefs: 0x4d48
+  __DATA.__objc_selrefs: 0x4d58
   __DATA.__objc_ivar: 0x8b8
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x1048

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 5240
-  Symbols:   1278
-  CStrings:  14779
+  Functions: 5253
+  Symbols:   1279
+  CStrings:  14841
 
Symbols:
+ _getprogname
CStrings:
+ "%s: %@ does not require a password, disqualified from possible password-missing TTR"
+ "%s: %@ is an EAP network, disqualified from possible password-missing TTR"
+ "%s: %@ is present in known networks and its password has not been in the keychain for > %d seconds in the keychain. Prompting user for TTR"
+ "%s: Already have remembered a network with a missing password, count: %ld"
+ "%s: Check for networks with deleted keychain password, count: %ld"
+ "%s: Checking network %@ to see if we need to prompt for the missing password TTR"
+ "%s: Checking password and network status for %@"
+ "%s: Checking password mod date %@ against current time"
+ "%s: End of deleted password network checks, network count: %ld"
+ "%s: Enter"
+ "%s: Invalid band preference"
+ "%s: Most recently joined network is null"
+ "%s: Most recently joined network was: %@"
+ "%s: Network %@ is no longer in the known networks list. No need to remember it for missing password purposes. "
+ "%s: Not recording password for matchingNetworkCopy %@ and previously joined network %@"
+ "%s: Password for %@ is now present in the keychain. No need to remember it for missing password purposes"
+ "%s: Recording that the password for %@ is not in the keychain. Network count with deleted passwords is now %ld"
+ "%s: Status of networks with deleted keychain password, count: %ld"
+ "%s: User accepted the TTR prompt. Removing all entries from the networksWithDeletedKeychainPassword array"
+ "%s: User declined the TTR"
+ "%s: WiFiMissingPasswordSoftError tapToRadarWithURL result:%@, error:%@"
+ "%s: WiFiNetworkSetPasswordWithTimeout for <%@> has timeout = %d and result = %d"
+ "%s: askToLaunchTapToRadarWithMessage result:%@, error:%@"
+ "%s: bssidInfo is NULL"
+ "%s: error: empty password for ssid %@"
+ "%s: error: empty ssid"
+ "%s: error: empty ssid hash"
+ "%s: for account %@"
+ "%s: kWiFiRoamManagerRoamReasonKey value is %@"
+ "%s: kWiFiRoamManagerRoamTypeKey value is %@"
+ "%s: no matching network in known networks list"
+ "%s: null device managers array"
+ "%s: null networkWithDeletedKeychainPassword"
+ "%s: numRef for kWiFiRoamManagerRoamReason is NULL"
+ "%s: numRef for kWiFiRoamManagerRoamType is NULL"
+ "%s: ssid %@ (%@)"
+ "%s: userInfo is NULL"
+ "%s:Notification %@ received"
+ "%s:[%@] completed\n"
+ "%s:[%@] error result %d \n"
+ "%s:[%@] timed out\n"
+ "CURRENT_NETWORK"
+ "HDSViewService"
+ "Missing Password"
+ "Password for WiFi network '%@' is not in the keychain. If you did not recently delete or forget this network, please tap Yes to TTR and use \"Add Devices\" to collect data from *all* devices"
+ "WiFiManager-1680.9 Apr 14 2024 10:41:58"
+ "WiFiManager-1680.9 Apr 14 2024 10:42:28"
+ "WiFiManagerCheckDeletedPasswordNetworks"
+ "WiFiManagerCheckForUnexpectedPasswordDelete"
+ "WiFiMissingPasswordSoftErrorHandler"
+ "WiFiMissingPasswordSoftErrorHandler_block_invoke"
+ "WiFiMissingPasswordSoftErrorHandler_block_invoke_2"
+ "WiFiSecurityCopyPasswordFromPasswordBackup"
+ "WiFiSecurityRemovePasswordFromPasswordBackup"
+ "WiFiSecurityRemovePasswordFromPasswordBackup_block_invoke"
+ "WiFiSecuritySavePasswordForPasswordBackup"
+ "WiFiSecuritySavePasswordForPasswordBackup_block_invoke"
+ "WiFiSecuritySetPasswordWithTimeout"
+ "__WiFiDeviceManagerRoamNotificationCallback"
+ "askToLaunchTapToRadarWithMessage:timeout:completionHandler:"
+ "dataUsingEncoding:"
+ "tap-to-radar://new?Title=WiFi%20Password%20Missing%20From%20Keychain&AutoDiagnostics=phone&Description=WiFi%20Password%20Missing%20From%20Keychain&ComponentID=621547&ComponentName=WiFi%20Connectivity&ComponentVersion=iOS&Classification=Serious%20Bug%20&ExtensionIdentifiers=com.apple.DiagnosticExtensions.WiFi"
+ "wallpaperkit.collectionsposter"
- "WallpaperKit.CollectionsPoster"
- "WiFiManager-1675.21.3.1 Mar  9 2024 02:17:36"
- "WiFiManager-1675.21.3.1 Mar  9 2024 02:18:09"

```
