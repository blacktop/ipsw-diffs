## demod_helper

> `/usr/libexec/demod_helper`

```diff

-1254.80.3.0.0
-  __TEXT.__text: 0x2cb80
+1254.100.45.0.1
+  __TEXT.__text: 0x2cebc
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_stubs: 0x3f40
-  __TEXT.__objc_methlist: 0x192c
-  __TEXT.__cstring: 0x4f61
-  __TEXT.__objc_methname: 0x4615
+  __TEXT.__objc_stubs: 0x3f80
+  __TEXT.__objc_methlist: 0x1934
+  __TEXT.__cstring: 0x4f8a
+  __TEXT.__objc_methname: 0x4651
   __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methtype: 0x593
-  __TEXT.__oslogstring: 0x56a0
+  __TEXT.__objc_methtype: 0x573
+  __TEXT.__oslogstring: 0x5747
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x250
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x760
+  __TEXT.__unwind_info: 0x768
   __DATA_CONST.__auth_got: 0x7f8
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x688

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x210
   __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1800
-  __DATA.__objc_selrefs: 0x13c0
-  __DATA.__objc_classrefs: 0x1b0
-  __DATA.__objc_superrefs: 0x60
+  __DATA.__objc_selrefs: 0x13c8
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x85c

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1034
+  Functions: 1036
   Symbols:   357
-  CStrings:  1971
+  CStrings:  1975
 
CStrings:
+ "%s: %{public}@ is a symlink. Skipping."
+ "%s: Cannot create device manifest."
+ "%s: Failed to get metadata for file: %{public}@. Skipping."
+ "%s: Manifest has not been successfully loaded yet."
+ "%s: No manifest data found for component: %{public}@ of type: %{public}@"
+ "%s: Root path must be the same between source and device manifest."
+ "-[MSDHOperations createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:]"
+ "-[MSDManifest addFilesUsingSourceManifest:]"
+ "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/Manifest.signed.plist"
+ "ComponentID"
+ "ComponentType"
+ "Media/Music/Downloads"
+ "SystemConfiguration/com.apple.wifi.plist"
+ "UserHomePath"
+ "addFilesUsingSourceManifest:"
+ "createDeviceManifestForComponent:ofType:withRootPath:userHomePath:andSavePath:"
- "%s - Will create device manifest from root %{public}@, isBackup %d, range %{public}@"
- "-[MSDHOperations createDeviceManifest:forBackup:range:andSaveTo:]"
- "/private/var/containers"
- "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/MSDWorkContainer/Manifest.plist.signed"
- "/private/var/mobile/Applications"
- "/private/var/mobile/Containers"
- "/private/var/mobile/XcodeBuiltProducts"
- "B52@0:8@16B24{_NSRange=QQ}28@44"
- "Cannot create device manifest."
- "Device manifest created (for %{public}@)"
- "IsBackup"
- "createDeviceManifest:forBackup:range:andSaveTo:"

```
