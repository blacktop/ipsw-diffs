## demod

> `/usr/libexec/demod`

```diff

-1254.80.3.0.0
-  __TEXT.__text: 0xc9e04
-  __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0x16ca0
-  __TEXT.__objc_methlist: 0xa4a4
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xcfa6
-  __TEXT.__objc_methname: 0x1adde
-  __TEXT.__oslogstring: 0x15a38
-  __TEXT.__objc_classname: 0x14e0
-  __TEXT.__objc_methtype: 0x3579
-  __TEXT.__gcc_except_tab: 0x35d8
-  __TEXT.__unwind_info: 0x2960
-  __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x5f8
+1254.100.45.0.1
+  __TEXT.__text: 0xcac1c
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_stubs: 0x16d60
+  __TEXT.__objc_methlist: 0xa544
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0xd0c8
+  __TEXT.__objc_methname: 0x1af36
+  __TEXT.__oslogstring: 0x15bd8
+  __TEXT.__objc_classname: 0x14f0
+  __TEXT.__objc_methtype: 0x356e
+  __TEXT.__gcc_except_tab: 0x35f8
+  __TEXT.__unwind_info: 0x2994
+  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__got: 0x608
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2608
-  __DATA_CONST.__cfstring: 0xc160
-  __DATA_CONST.__objc_classlist: 0x610
+  __DATA_CONST.__cfstring: 0xc280
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x480
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_classrefs: 0xab0
+  __DATA_CONST.__objc_superrefs: 0x3a8
+  __DATA_CONST.__objc_intobj: 0x498
   __DATA_CONST.__objc_arraydata: 0x780
   __DATA_CONST.__objc_arrayobj: 0x3a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x17a28
-  __DATA.__objc_selrefs: 0x64f8
-  __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0xaa8
-  __DATA.__objc_superrefs: 0x3a8
-  __DATA.__objc_ivar: 0x9b0
-  __DATA.__objc_data: 0x3ca0
+  __DATA.__objc_const: 0x17b18
+  __DATA.__objc_selrefs: 0x6530
+  __DATA.__objc_ivar: 0x9b8
+  __DATA.__objc_data: 0x3cf0
   __DATA.__data: 0x2328
   __DATA.__bss: 0x4e0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4973
-  Symbols:   740
-  CStrings:  9012
+  Functions: 4984
+  Symbols:   744
+  CStrings:  9044
 
Symbols:
+ _AIDAServiceTypeFaceTime
+ _AIDAServiceTypeMessages
+ _AKAuthenticationDemoAccountKey
+ __os_feature_enabled_impl
+ _dispatch_block_create
- _NSLocaleCountryCode
CStrings:
+ "\x11\x13"
+ "%s: %{public}@ is a symlink. Skipping."
+ "%s: Failed to create device manifest. Initializing empty device manifest dictionary."
+ "%s: Failed to get metadata for file: %{public}@. Skipping."
+ "%s: Failed to load device manifest from: %{public}@ error: %{public}@"
+ "%s: Incorrect demo mode value: %{public}@ for key: %{public}@"
+ "%s: Root path must be the same between source and device manifest."
+ "%s: entered for component: %{public}@ of type: %{public}@ root path: %{public}@"
+ "-[MSDHelperAgent createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:]"
+ "-[MSDManifest addFilesUsingSourceManifest:]"
+ "-[MSDTargetDevice demoModeValueForKey:]"
+ "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/DeviceManifests"
+ "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/Manifest.signed.plist"
+ "/tmp/DownloadedFileList.plist"
+ "12"
+ "Account not allowlisted: %{public}@"
+ "ComponentID"
+ "ComponentType"
+ "Device manifest already exists at path: %{public}@; Skipping XPC request."
+ "DisableNightlyRefresh"
+ "Failed to create device manifest folder: %{public}@"
+ "Found 'demo account' flag in IdMS auth response!"
+ "InternationalMobileEquipmentIdentity2"
+ "MSDFeatureFlags"
+ "Media/Music/Downloads"
+ "MobileStoreDemo"
+ "No 'demo account' flag set in IdMS auth response!"
+ "PressDemoMode"
+ "SetupDoneTimestamp"
+ "Skip collecting any app usage data as setup done timestamp is not set."
+ "SystemConfiguration/com.apple.wifi.plist"
+ "T@\"CDPContext\",?,&,N"
+ "T@\"CDPContext\",?,&,N,VcdpContext"
+ "T@\"NSSet\",?,C,N"
+ "T@\"NSString\",&,N,V_countryCode"
+ "T@\"NSString\",&,V_language"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,N,GisFastSignInEnabled"
+ "TQ,?,N"
+ "Turning on Press Demo Mode."
+ "UserHomePath"
+ "_isAllowListedAccount:withAuthResults:"
+ "addFilesUsingSourceManifest:"
+ "collectAppUsageBetweenLastSetupDoneAndNow"
+ "collectAppUsageDataForSession:fromStart:toEnd:withDelay:"
+ "collectAppUsageWithSessionStart:andEnd:withDelay:"
+ "com.apple.mobilestoredemo.FaceTime"
+ "com.apple.mobilestoredemo.iMessage"
+ "country"
+ "createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:"
+ "demoModeValueForKey:"
+ "demo_mode"
+ "isDemoModeOn"
+ "isPressDemoDevice"
+ "isPressDemoModeEnabled"
+ "isRecoveryKeyAvailable:"
+ "press"
+ "pressDemoMode"
+ "sendAppUsageDataEvent:withExecutable:sessionUUID:sessionStart:sessionEnd:sessionDuration:appOrder:appDuration:"
+ "sessionDuration"
+ "turnOnDemoMode"
+ "turnOnPressDemoMode"
+ "v28@0:8@?16B24"
+ "v80@0:8@16@24@32@40@48q56q64d72"
+ "waitForBuddy:updateStatus:"
+ "waitForBuddyWithoutStatusUpdate:"
+ "xRyzf9zFE/ycr/wJPweZvQ"
- "\x11\x12"
- "%s: Incorrect demo mode settings: %{public}@"
- "%s: iCloud account username not allowed: %{public}@"
- "%s: iTunes account username not allowed: %{public}@"
- "%tu_%tu"
- "-[MSDHelperAgent createDeviceManifest:forBackup:range:]"
- "-[MSDTargetDevice storeDemoMode]"
- "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer"
- "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/DownloadedFileList.plist"
- "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/Manifest.plist.signed"
- "11"
- "@44@0:8@16B24{_NSRange=QQ}28"
- "Account not allowlisted: %{public}@."
- "Device manifest exist at path: %{public}@; skipping XPC request"
- "DeviceManifest.plist"
- "Failed to get device manifest, initializing empty device manifest dictionary"
- "Failed to read device manifest from: %{public}@; initializing empty dictionary"
- "IsBackup"
- "T@\"CDPContext\",&,N"
- "T@\"CDPContext\",&,N,VcdpContext"
- "T@\"NSSet\",C,N"
- "TB,N,GisFastSignInEnabled"
- "TQ,N"
- "_isAllowListedAccount:"
- "collectAppUsageDataForSession:fromStart:toEnd:"
- "collectAppUsageWithSessionStart:andEnd:"
- "country_code"
- "createDeviceManifest:forBackup:range:"
- "getDeviceManifestSavePathWithIdentifier:"
- "isRecoveryKeyAvailable"
- "languageCode"
- "localeIdentifier"
- "readManifestDictFromPath:"
- "sendAppUsageDataEvent:withExecutable:sessionUUID:sessionStart:sessionEnd:appOrder:andDuration:"
- "unknown"
- "v72@0:8@16@24@32@40@48q56d64"

```
