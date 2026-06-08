## demod_helper

> `/usr/libexec/demod_helper`

```diff

-1611.120.9.0.0
-  __TEXT.__text: 0x32154
-  __TEXT.__auth_stubs: 0x1170
+1865.0.0.0.0
+  __TEXT.__text: 0x2e6ac
+  __TEXT.__auth_stubs: 0x11c0
   __TEXT.__objc_stubs: 0x4400
-  __TEXT.__objc_methlist: 0x1b98
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x6131
-  __TEXT.__objc_classname: 0x1fb
-  __TEXT.__objc_methname: 0x4ba3
-  __TEXT.__objc_methtype: 0x5cf
-  __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__oslogstring: 0x624b
+  __TEXT.__objc_methlist: 0x1bc8
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x6469
+  __TEXT.__objc_classname: 0x1ec
+  __TEXT.__objc_methname: 0x4c11
+  __TEXT.__objc_methtype: 0x5d5
+  __TEXT.__gcc_except_tab: 0x338
+  __TEXT.__oslogstring: 0x6226
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xa30
-  __DATA_CONST.__auth_got: 0x8c8
-  __DATA_CONST.__got: 0x358
+  __TEXT.__unwind_info: 0x960
   __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x4e60
+  __DATA_CONST.__cfstring: 0x50c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x2d8
-  __DATA_CONST.__objc_arrayobj: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x320
+  __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1990
-  __DATA.__objc_selrefs: 0x1560
-  __DATA.__objc_ivar: 0xb8
+  __DATA_CONST.__auth_got: 0x8f0
+  __DATA_CONST.__got: 0x358
+  __DATA.__objc_const: 0x19c0
+  __DATA.__objc_selrefs: 0x1578
+  __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x85c
   __DATA.__bss: 0x160

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5BAC3332-C0E7-39ED-B882-FA14898E91B7
-  Functions: 1049
-  Symbols:   395
-  CStrings:  2810
+  UUID: D2A738F2-C6B1-3327-8870-134897519746
+  Functions: 1048
+  Symbols:   400
+  CStrings:  2855
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _objc_retain_x25
CStrings:
+ "%s - Cannot load submanifest:  %{public}@"
+ "%s - Cannot locate container ID: %{public}@ in path: %{public}@ - Skipping ..."
+ "+[NSString(sysContainerPath) restoreSystemContainerUUIDPathsInDict:]"
+ "-[MSDHMessageResponder updateSignedManifest:]"
+ "-[MSDHOperations _updateSignedManifest:]"
+ "-[MSDHOperations createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:manifestPath:]"
+ "-[MSDHOperations restoreAppDataAttributesUnder:containerType:identifier:manifestUID:deviceUID:manifestPath:]"
+ "-[MSDHOperations restoreBackupAttributesUnder:range:manifestUID:deviceUID:manifestPath:]"
+ "-[MSDHOperations updateSignedManifest:]"
+ "/private/var/root/Library/Backup/SystemContainers/Data"
+ "/private/var/root/Library/Backup/SystemContainers/Shared"
+ "/var/mobile/Home/DemoContent"
+ "/var/mobile/Library/Preferences/com.apple.Home.ControlCenter.plist"
+ "/var/mobile/Library/Preferences/com.apple.Home.plist"
+ "/var/mobile/Library/Preferences/com.apple.Home.wallpaper.plist"
+ "/var/mobile/Library/Preferences/com.apple.HomeDeviceSetup.plist"
+ "/var/mobile/Library/Preferences/com.apple.PineBoardServices.plist"
+ "/var/mobile/Library/Preferences/com.apple.airplay.plist"
+ "/var/mobile/Library/Preferences/com.apple.home.plist"
+ "/var/mobile/Library/Preferences/com.apple.homed.plist"
+ "/var/mobile/Library/homed"
+ "B64@0:8@16@24@32@40@48@56"
+ "B64@0:8@16{_NSRange=QQ}24@40@48@56"
+ "DisableAssetDownload"
+ "Entering %s with parameter: %@"
+ "Home"
+ "HomeEcosystem"
+ "ManifestPath"
+ "Need to keep manifest in memory"
+ "System container backup only allowed on Watch or Ha devices."
+ "T@\"NSString\",&,V_manifestPath"
+ "_manifestPath"
+ "_updateSignedManifest:"
+ "automatedDeviceGroup"
+ "automatedDeviceGroupID"
+ "com.apple.demo-settings"
+ "createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:manifestPath:"
+ "disableAssetDownload"
+ "fileMetadataWithPath:"
+ "manifestPath"
+ "restoreAppDataAttributesUnder:containerType:identifier:manifestUID:deviceUID:manifestPath:"
+ "restoreBackupAttributesUnder:range:manifestUID:deviceUID:manifestPath:"
+ "setManifestPath:"
+ "systemContainerBackupAllowed: %{bool}d"
+ "updateSignedManifest:"
+ "updateSignedManifestPath"
- "%s - Cannot load manifest:  %{public}@"
- "-[MSDHMessageResponder updateSignedManifest]"
- "-[MSDHOperations createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:]"
- "-[MSDHOperations restoreAppDataAttributesUnder:containerType:identifier:manifestUID:deviceUID:]"
- "-[MSDHOperations restoreBackupAttributesUnder:range:manifestUID:deviceUID:]"
- "-[MSDHOperations updateSignedManifest]"
- "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/Manifest.signed.plist"
- "B56@0:8@16@24@32@40@48"
- "B56@0:8@16{_NSRange=QQ}24@40@48"
- "Cannot locate system container path identifier in path '%{public}@'. Skipping..."
- "Cannot lookup system container path UUID from path '%{public}@'. Skipping..."
- "Entering %s with parameter:"
- "Need to keep manaifest in memory"
- "System container path mapping created: %{public}@ -> %{public}@"
- "createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:"
- "fileMetadatatWithPath:"
- "restoreAppDataAttributesUnder:containerType:identifier:manifestUID:deviceUID:"
- "restoreBackupAttributesUnder:range:manifestUID:deviceUID:"
- "stringByReplacingCharactersInRange:withString:"
- "updateSignedManifest"

```
