## resourcegrabberd

> `/usr/libexec/resourcegrabberd`

```diff

-113.0.0.0.0
-  __TEXT.__text: 0x11300
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x2240
-  __TEXT.__objc_methlist: 0x153c
-  __TEXT.__objc_classname: 0x2a6
-  __TEXT.__objc_methtype: 0x10b9
-  __TEXT.__cstring: 0x85d
-  __TEXT.__objc_methname: 0x2fb2
-  __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x1360
-  __TEXT.__gcc_except_tab: 0x4e4
-  __TEXT.__unwind_info: 0x600
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__cfstring: 0x740
-  __DATA_CONST.__objc_classlist: 0x98
+116.0.0.0.0
+  __TEXT.__text: 0x13048
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x25e0
+  __TEXT.__objc_methlist: 0x17ac
+  __TEXT.__objc_classname: 0x2ea
+  __TEXT.__objc_methtype: 0x1193
+  __TEXT.__cstring: 0x937
+  __TEXT.__objc_methname: 0x35d6
+  __TEXT.__const: 0xb0
+  __TEXT.__oslogstring: 0x18ec
+  __TEXT.__gcc_except_tab: 0x5ac
+  __TEXT.__unwind_info: 0x5e0
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_intobj: 0x360
-  __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__objc_dictobj: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_intobj: 0x378
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_dictobj: 0x78
+  __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2ac0
-  __DATA.__objc_selrefs: 0xd58
-  __DATA.__objc_ivar: 0x140
-  __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0x420
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x1e0
+  __DATA.__objc_const: 0x3088
+  __DATA.__objc_selrefs: 0xef0
+  __DATA.__objc_ivar: 0x158
+  __DATA.__objc_data: 0x640
+  __DATA.__data: 0x4e0
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D896E1DA-31A8-3689-B1DC-B55568545110
-  Functions: 489
-  Symbols:   189
-  CStrings:  1001
+  UUID: 9E25A2FC-A420-3A93-B203-77E2D08CBFB9
+  Functions: 540
+  Symbols:   207
+  CStrings:  1111
 
Symbols:
+ _NRDevicePropertyScreenScale
+ _OBJC_CLASS_$_LSApplicationProxy
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ ___error
+ __set_user_dir_suffix
+ __xpc_event_key_name
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
+ _strcmp
+ _xpc_dictionary_get_string
- _objc_release_x10
CStrings:
+ "############ IDS Response Failed to Send: %{public}ld bytes, identifier %{public}@ (for %{public}@) error: %@"
+ "(null)"
+ "@\"LSApplicationWorkspace\""
+ "@\"NRGPhoneIconVersionTracker\""
+ "@\"NSObject<NRGPhoneIconVersionTracking>\""
+ "@\"NSString\"60@0:8@\"PBCodable\"16S24q28@\"IDSProtobuf\"36@?<v@?@\"NSError\">44d52"
+ "@48@0:8@16@24@32@?40"
+ "A"
+ "Could not create data for phone icon versions %@"
+ "Could not determine version URL for phone icon version tracker"
+ "Could not read phone icon versions from %@ %@"
+ "Could not write phone icon versions to %@ %@"
+ "Detected out-of-date phone icons %@"
+ "Distributed notification handled: %{public}s"
+ "Failed to load phone icon versions from %@"
+ "Failed to look up application record for %@: %@"
+ "Failed to send IDS Request for identifier %{public}@ error: %{public}@"
+ "Failed to send resource %@ %@"
+ "Failed to send updated icons: %{public}@"
+ "Handling resource request from watch: bundleID=%{public}@ type=%d iconVariant=%d"
+ "IDS error %{public}@ sending resource response"
+ "LSApplicationWorkspaceObserverProtocol"
+ "Loaded phone icon versions from %@"
+ "NRGPhoneIconVersionTracker"
+ "NRGPhoneIconVersionTracker initialized, versionDictionary = %@"
+ "NRGPhoneIconVersionTracking"
+ "No active paired device for icon update push"
+ "No active paired device for resource request"
+ "No icon data found for updated apps %@"
+ "No phone icons need updating"
+ "Phone app %@ version changed from %@ to %@"
+ "PhoneIconVersionDictionary"
+ "Received resource request with nil bundleID"
+ "Responding to watch resource request: found"
+ "Responding to watch resource request: not found"
+ "Sending %lu updated phone icons to watch for %@"
+ "Sent resource with identifier %{public}@ path %@"
+ "Starting phone icon version tracker"
+ "Suspending phone icon version tracker"
+ "T@\"NRGPhoneIconVersionTracker\",&,N,V_phoneIconVersionTracker"
+ "T@\"NSObject<NRGPhoneIconVersionTracking>\",R,W,N,V_delegate"
+ "Updated icons sent successfully"
+ "_checkVersions"
+ "_phoneIconVersionTracker"
+ "_readVersions"
+ "_running"
+ "_versionDictionary"
+ "_versionURL"
+ "_workspace"
+ "_writeVersions:"
+ "addEntriesFromDictionary:"
+ "addObserver:"
+ "addOperationWithBlock:"
+ "applicationIconDidChange:"
+ "applicationInstallsArePrioritized:arePaused:"
+ "applicationInstallsDidCancel:"
+ "applicationInstallsDidChange:"
+ "applicationInstallsDidPause:"
+ "applicationInstallsDidPrioritize:"
+ "applicationInstallsDidResume:"
+ "applicationInstallsDidStart:"
+ "applicationInstallsDidUpdateIcon:"
+ "applicationProxyForIdentifier:"
+ "applicationStateDidChange:"
+ "applicationsDidChangePersonas:"
+ "applicationsDidFailToInstall:"
+ "applicationsDidFailToUninstall:"
+ "applicationsDidInstall:"
+ "applicationsDidInstall: %@"
+ "applicationsDidUninstall:"
+ "applicationsDidUpdateMetadata:"
+ "applicationsWillInstall:"
+ "applicationsWillUninstall:"
+ "cacheDir is nil, no paired device store path available"
+ "com.apple.LaunchServices.applicationRegistered"
+ "com.apple.distnoted.matching"
+ "com.apple.nanoresourcegrabber.%@"
+ "com.apple.resourcegrabberd"
+ "commitBundleIDs:"
+ "compatibilityObject"
+ "could not open %@ for %@ due to %@"
+ "databaseWasRebuilt"
+ "defaultWorkspace"
+ "deviceManagementPolicyDidChange:"
+ "failed to set user dir suffix: %d"
+ "floatValue"
+ "handleFullSyncProtoResponse:"
+ "handleResourceRequest:"
+ "helperPlaceholdersInstalled:"
+ "helperPlaceholdersUninstalled:"
+ "iconDataForVariant:proxy:screenScale:"
+ "idx (%lu) is out of range (%lu)"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "networkUsageChanged:"
+ "observeLaunchProhibitedApps"
+ "phoneIconVersionTracker"
+ "phoneIconVersionTracker:detectedOutOfDateIcons:"
+ "pluginsDidInstall:"
+ "pluginsDidUninstall:"
+ "pluginsWillUninstall:"
+ "removeObserver:"
+ "request_response"
+ "revertBundleIDs:"
+ "sendResourceAtURL:metadata:options:completionHandler:"
+ "sendResourceAtURL:metadata:toDestinations:priority:options:identifier:error:"
+ "sent %ld of %ld bytes (%f%%)"
+ "setPhoneIconVersionTracker:"
+ "shortVersionString"
+ "streamError"
+ "v24@0:8@\"NSArray\"16"
+ "v32@0:8@\"NRGPhoneIconVersionTracker\"16@\"NSSet\"24"
+ "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "############ IDS Response Failed to Send: %{public}ld bytes, identifier %{public}@ (for %{public}@)"
- "@\"NSString\"60@0:8@\"PBCodable\"16S24q28@\"IDSProtobuf\"36@?<v@?B@\"NSError\">44d52"
- "Failed to send IDS Request for identifier %{public}@"
- "handleFullSyncResponse:"
- "idx (%tu) is out of range (%tu)"

```
