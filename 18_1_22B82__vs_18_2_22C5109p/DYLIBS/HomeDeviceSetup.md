## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-257.10.4.0.0
-  __TEXT.__text: 0x55fe8
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x23b4
-  __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x16de6
-  __TEXT.__oslogstring: 0x3ba
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0xcf8
-  __TEXT.__objc_classname: 0x2c4
-  __TEXT.__objc_methname: 0xb4b5
-  __TEXT.__objc_methtype: 0x11ff
-  __TEXT.__objc_stubs: 0x6da0
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x1300
+277.20.5.0.0
+  __TEXT.__text: 0x582a0
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x2484
+  __TEXT.__const: 0x278
+  __TEXT.__cstring: 0x1781b
+  __TEXT.__oslogstring: 0x3a7
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__unwind_info: 0xd48
+  __TEXT.__objc_classname: 0x2c3
+  __TEXT.__objc_methname: 0xb8a4
+  __TEXT.__objc_methtype: 0x1212
+  __TEXT.__objc_stubs: 0x70a0
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0x1378
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2268
+  __DATA_CONST.__objc_selrefs: 0x2358
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x4640
+  __DATA_CONST.__objc_arraydata: 0x230
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x4780
   __AUTH_CONST.__objc_const: 0x77b0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0x290
-  __DATA.__objc_ivar: 0x900
+  __DATA.__objc_ivar: 0x8fc
   __DATA.__data: 0xa28
   __DATA.__common: 0x10
   __DATA.__bss: 0x528

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1313
-  Symbols:   1621
-  CStrings:  4807
+  Functions: 1340
+  Symbols:   1649
+  CStrings:  4897
 
Symbols:
+ __Block_object_dispose
+ ___NSArray0__struct
+ ___error
+ _close
+ _ffsctl
+ _kDefaultsKey_FailSetupLate
+ _kDefaultsKey_SysDropBuildMode
+ _open
+ _strerror
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CFStringCreateWithCString
- _WiFiNetworkCopyPassword
- _WiFiNetworkCreate
- _kCFAllocatorDefault
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
CStrings:
+ "\x114C!\x11!232\x11\x13\x11\x1111a\xb51Q3A\xe1!!\xb1\x81a!sAQ\x11b\x14\x13/\x0f\x04"
+ "-[HDSFileTransferService cleanupDiagnostics]"
+ "-[HDSFileTransferService handleSysDropEnablementProfileRequest:responseHandler:]"
+ "-[HDSFileTransferService handleSysDropEnablementProfileRequest:responseHandler:]_block_invoke"
+ "-[HDSFileTransferService handleSysDropEnablementProfileRequest:responseHandler:]_block_invoke_2"
+ "-[HDSFileTransferService markCacheDeletable:]"
+ "-[HDSFileTransferService writeFileToCache:]"
+ "-[HDSSetupService _handleSessionStarted:]_block_invoke_11"
+ "-[HDSSetupService _handleStartSysDropEnablementProfileTransfer:responseHandler:]_block_invoke"
+ "-[HDSSetupService _handleStartSysDropEnablementProfileTransfer:responseHandler:]_block_invoke_2"
+ "-[HDSSetupService _handleStartSysDropEnablementProfileTransfer:responseHandler:]_block_invoke_3"
+ "-[HDSSetupService installProfileData:]"
+ "-[HDSSetupService removeSysDropProfile]"
+ "-[HDSSetupSession _runHomePodLoggingProfileTransferAck]"
+ "-[HDSSetupSession _runHomePodLoggingProfileTransfer]"
+ "-[HDSSetupSession _startSysDropLoggingProfileRequest]"
+ "-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke"
+ "-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_3"
+ "-[HDSSetupSession fetchHomePodLoggingProfile]"
+ "-[HDSSetupSession homePodLoggingProfileSelected:]_block_invoke"
+ "-[HDSSetupSession removeSysDropProfile]"
+ ".tar.gz"
+ "/%!@(MISSING)"
+ "/Library/Caches"
+ "/Library/Caches/HPSetup.mobileconfig"
+ "Attempting to move %!@(MISSING) to %!@(MISSING)\n"
+ "B20@0:8I16"
+ "Cannot read transferred file path\n"
+ "Creating directory at %!@(MISSING)\n"
+ "Failed to create directory %!@(MISSING)\n"
+ "Failed to mark %!s(MISSING) as purgeable %!d(MISSING) (%!s(MISSING)) (flags 0x%!l(MISSING)lx)\n"
+ "Failed to setup File Transfer"
+ "Fetched HomePod Logging Profile successfully"
+ "File copy error %!@(MISSING)\n"
+ "File copy success\n"
+ "ForceFailEarly"
+ "ForcedError"
+ "HDS-HK-DeviceSetup-DeviceSetupOperationFailed"
+ "HDSMessageRequestSysDropEnablement\n"
+ "HomePod SysDrop capable Seed Carry: %!s(MISSING) | %!m(MISSING)\n"
+ "I16@0:8"
+ "Install Profile Success"
+ "Install Profile failed %!@(MISSING)"
+ "Installed Profiles from system BEFORE performing removal operation %!@(MISSING)"
+ "Logging Profile File Transfer Error %!@(MISSING)\n"
+ "Logging Profile File Trasfer %!@(MISSING)\n"
+ "Logging Profile not found\n"
+ "Looking for contents in %!@(MISSING)."
+ "Marked %!s(MISSING) purgeable with flags 0x%!l(MISSING)lx returned %!d(MISSING) (%!s(MISSING))\n"
+ "Primary"
+ "ProfileFileTransfer"
+ "Progress transferred byes: %!d(MISSING)\n Progress total byes: %!d(MISSING)\n"
+ "Remove failed %!@(MISSING)"
+ "Removing %!@(MISSING)"
+ "Removing SysDrop Enablement Profile"
+ "Removing SysDrop Logging Profile"
+ "Secondary"
+ "Sending request for Logging Profile for HomePod\n"
+ "Setting up file receiver for SysDrop \n"
+ "Setting up listener/receiver for File transfer\n"
+ "Successfully created directory at %!@(MISSING)\n"
+ "SysDropBuildMode"
+ "T@?,C,N,V_promptForLoggingProfileTransferAck"
+ "T@?,C,N,V_sysdropFinishedHandler"
+ "TestingDefault"
+ "URLWithString:"
+ "UUID"
+ "Unable to find contents in directory: %!@(MISSING)."
+ "Unable to find directory: %!@(MISSING)."
+ "User selection for HomePod Profile Transfer %!s(MISSING)\n"
+ "_enablementProfileInstalled"
+ "_enablementProfileInstalled %!s(MISSING)\n"
+ "_enablementProfileInstalled %!s(MISSING) | _homePodSysDropCapable %!s(MISSING) | _homePodSysDropCapableV2 %!s(MISSING) | buildMode %!d(MISSING)\n"
+ "_handleStartSysDropEnablementProfileTransfer:responseHandler:"
+ "_hds_rpft_sysdrop_enablement"
+ "_homePodProfileTransferAckState"
+ "_homePodProfileTransferAckState In Progress\n"
+ "_homePodProfileTransferAckState Starting\n"
+ "_homePodProfileTransferAckState User selected  \n"
+ "_homePodProfileTransferSelection"
+ "_homePodProfileTransferState"
+ "_homePodSysDropCapableV2"
+ "_promptForLoggingProfileTransferAck"
+ "_runHomePodLoggingProfileTransfer"
+ "_runHomePodLoggingProfileTransfer In Progress\n"
+ "_runHomePodLoggingProfileTransfer Starting\n"
+ "_runHomePodLoggingProfileTransferAck"
+ "_startSysDropLoggingProfileRequest"
+ "_startSysDropLoggingProfileRequest File Transfer activated successfully\n"
+ "_startSysDropLoggingProfileRequest beginning transfer\n"
+ "_startSysDropLoggingProfileRequest errored: %!{(MISSING)error}\n"
+ "_startSysDropLoggingProfileRequest request: %!@(MISSING)\n"
+ "_startSysDropLoggingProfileRequest sideloadFilesForTargetId errored: %!{(MISSING)error}\n"
+ "_startSysDropLoggingProfileRequest successful| response: %!@(MISSING)\n"
+ "_sysdropFinishedHandler"
+ "appGroupIdentifier"
+ "cleanupDiagnostics"
+ "com.apple.defaults.managed.homedevicesetup.logging"
+ "com.apple.homedevicesetup.sysdrop"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "containsString:"
+ "contentsAtPath:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "copyItemAtURL:toURL:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithContentsOfURL:"
+ "failSetupLate"
+ "fetchHomePodLoggingProfile"
+ "fetchHomePodLoggingProfile filePath %!@(MISSING)"
+ "fileURLWithPath:isDirectory:relativeToURL:"
+ "forceFailSetupLater"
+ "group.homedevicesetup.diagnostics"
+ "handleSysDropEnablementProfileRequest:responseHandler:"
+ "homePodLoggingProfileSelected:"
+ "https://secure-appldnld.apple.com/HomeProfiles/HPSetup.mobileconfig"
+ "installProfileData:"
+ "installProfileData:options:outError:"
+ "installedProfilesWithFilterFlags:"
+ "isReadableFileAtPath:"
+ "markCacheDeletable:"
+ "productionCacheDirectory"
+ "promptForLoggingProfileTransferAck"
+ "q\x12!\x16"
+ "removeItemAtPath:error:"
+ "removeProfileWithIdentifier:"
+ "removeSysDropProfile"
+ "sd_capa_v2"
+ "setPromptForLoggingProfileTransferAck:"
+ "setSysdropFinishedHandler:"
+ "shouldDoSysDrop:"
+ "sysDropBuildMode"
+ "sysDropProfileInstalled"
+ "sysdiagnose"
+ "sysdropFinishedHandler"
+ "sysdrop_carry"
+ "writeFileToCache:"
+ "writeToFile:atomically:"
- "\x114C!\x11!232\x11\x13\x11\x1111a\xb51Q3A\xe1!!\xb1\x81a!sAQ\x13\x11r\x14\x13/\x0f\x03"
- "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]"
- "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke"
- "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2"
- "-[HDSSetupSession _runPreflightSSIDCheck]"
- "-[HDSSetupSession createWiFiConfigurationForSetup:password:]"
- "-[HDSSetupSession passwordForSSID:]"
- "HDS-HK-DeviceSetup-NoHKAccessory"
- "HIDDEN_NETWORK"
- "HomeKitPRSSIDFetch"
- "HomeKitPrimarySSIDFetch empty result, falling back to regular wifi setup\n"
- "HomeKitPrimarySSIDFetch error %!@(MISSING)\n"
- "HomeKitPrimarySSIDFetch fetchWiFiInfosWithTimeout complete, duration %!f(MISSING) seconds\n"
- "HomeKitPrimarySSIDFetch fetched SSID %!@(MISSING)\n"
- "HomeKitPrimarySSIDFetch no selected Home, Skipping\n"
- "HomeKitPrimarySSIDFetch result %!@(MISSING)\n"
- "HomeKitPrimarySSIDFetch start\n"
- "HomeKitSetupNoAccessory"
- "Preflight SSID Check hasn't succeeded yet (%!d(MISSING))\n"
- "Preflight SSID Check start\n"
- "Preflight SSID Check succeeded\n"
- "PreflightSSID"
- "SCAN_DIRECTED"
- "SSID"
- "SSID_STR"
- "Setting up listener/receiver for File Xfer\n"
- "_didSetupWithPRSSID"
- "_homeKitPrimarySSIDFetchState"
- "_homeKitSSIDFetchDuration"
- "_homeKitSSIDFetchStart"
- "_preferredWiFiConfig"
- "_primaryResidentPassword"
- "_primaryResidentSSID"
- "_runHomeKitPrimarySSIDFetch"
- "_runPreflightSSIDCheck"
- "_selectedHomeHasPrimaryResident"
- "cStringUsingEncoding:"
- "createWiFiConfigurationForSetup finish\n"
- "createWiFiConfigurationForSetup:password:"
- "fetchWiFiInfosWithTimeout:completion:"
- "passwordForSSID WiFi Info %!@(MISSING)\n"
- "passwordForSSID:"
- "primarySSIDFetchMs"
- "primary_resident_wifi"
- "q\x12!\x15"
- "residentWiFiSetup"
- "setPreferredWiFiConfiguration:"

```
