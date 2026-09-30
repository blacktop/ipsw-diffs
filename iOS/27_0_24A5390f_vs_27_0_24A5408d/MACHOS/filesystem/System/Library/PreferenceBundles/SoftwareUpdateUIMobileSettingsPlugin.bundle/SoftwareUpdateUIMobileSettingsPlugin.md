## SoftwareUpdateUIMobileSettingsPlugin

> `/System/Library/PreferenceBundles/SoftwareUpdateUIMobileSettingsPlugin.bundle/SoftwareUpdateUIMobileSettingsPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0x652e0
+772.0.20.0.0
+  __TEXT.__text: 0x65f34
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__const: 0x28c4
   __TEXT.__swift5_typeref: 0x2171
-  __TEXT.__const: 0x2864
-  __TEXT.__swift5_capture: 0x1dec
+  __TEXT.__swift5_capture: 0x1e08
   __TEXT.__objc_classname: 0x1b5
   __TEXT.__objc_methname: 0x875
   __TEXT.__objc_methtype: 0x351

   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0xa8
   __TEXT.__swift_as_entry: 0x50
-  __TEXT.__swift_as_ret: 0x44
-  __TEXT.__swift_as_cont: 0xc8
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift_as_cont: 0xcc
   __TEXT.__swift5_assocty: 0x1a0
-  __TEXT.__oslogstring: 0xb71
+  __TEXT.__oslogstring: 0xd71
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1468
-  __TEXT.__eh_frame: 0x7d0
-  __DATA_CONST.__const: 0x4c88
+  __TEXT.__unwind_info: 0x1478
+  __TEXT.__eh_frame: 0x7f8
+  __DATA_CONST.__const: 0x4cd8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__auth_got: 0xc38
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x728
   __DATA.__objc_const: 0x530
   __DATA.__objc_selrefs: 0x2e0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2128
-  Symbols:   134
+  Functions: 2135
+  Symbols:   136
   CStrings:  286
 
Symbols:
+ _SoftwareUpdateUIMobileSettingsPluginVersionNumber
+ _SoftwareUpdateUIMobileSettingsPluginVersionString
CStrings:
+ "%{public}s.%{public}s: Assigning %{bool,public}d to automaticDownload."
+ "%{public}s.%{public}s: Assigning %{bool,public}d to automaticUpdate. userSpecified: false"
+ "%{public}s.%{public}s: Automatic Updates: Presenting RecoveryOS Info Menu"
+ "%{public}s.%{public}s: Automatic Updates: Shake gesture triggered"
+ "%{public}s.%{public}s: Automatic Updates: Triggering RecoveryOS Software Update Request"
+ "%{public}s.%{public}s: Couldn't convert NeRD info to string"
+ "%{public}s.%{public}s: Couldn't fetch RecoveryOS info"
+ "%{public}s.%{public}s: Deep link handling error: %{public}@"
+ "%{public}s.%{public}s: Deep link handling skipped — environment not initialized"
+ "%{public}s.%{public}s: Failed to perform update action: %{public}s"
+ "%{public}s.%{public}s: Failed to unschedule targeted update: %{public}@"
+ "%{public}s.%{public}s: Finished to resolve the Deep Linking request for  URL with resource dictionary: %{public}s"
+ "%{public}s.%{public}s: Initiating Deep Linking resolution request for URL with resource dictionary: %{public}s"
+ "%{public}s.%{public}s: Resolved deep link with response: %{public}s"
+ "%{public}s.%{public}s: Resolving deep link request: %{public}s"
+ "%{public}s.%{public}s: Settings Experience Plugin - Initiating Deep Linking resolution request for URL: %{public}s"
+ "%{public}s.%{public}s: Skipping on assignment of automatic download to \"%{bool,public}d\" because the automatic download toggle is disabled"
+ "%{public}s.%{public}s: Skipping on assignment of automatic update to \"%{bool,public}d\" because the automatic updates toggle is disabled"
+ "%{public}s.%{public}s: Toggeled automatic update enabled while targetted update is not scheduled: %{bool,public}d"
+ "%{public}s.%{public}s: Toggeled automatic update enabled while targetted update is scheduled: %{bool,public}d"
+ "%{public}s.%{public}s: autoScanAndDownloadIfAvailable(nil) called"
+ "%{public}s.%{public}s: unscheduleTargetedUpdate result: %{bool,public}d"
+ "Attempting to perform update action \"%{public}s\" to resolve the deep link action: %{public}s"
+ "Could not perform the deep link action %{public}s as the descriptor\nis in an unknown state. Aborting the request."
+ "Could not perform the deep link action %{public}s as the descriptor\nis not available to download or available to install. Aborting the request."
+ "User Action: Sets %{bool,public}d for auto Install System files in AutomaticUpdatesView"
+ "User Action: Sets %{bool,public}d for automatic Download in AutomaticUpdatesView"
+ "User Action: Sets %{bool,public}d for automatic Update in AutomaticUpdatesView"
- "%s.%s: Assigning %{bool}d to automaticDownload."
- "%s.%s: Assigning %{bool}d to automaticUpdate. userSpecified: false"
- "%s.%s: Automatic Updates: Presenting RecoveryOS Info Menu"
- "%s.%s: Automatic Updates: Shake gesture triggered"
- "%s.%s: Automatic Updates: Triggering RecoveryOS Software Update Request"
- "%s.%s: Couldn't convert NeRD info to string"
- "%s.%s: Couldn't fetch RecoveryOS info"
- "%s.%s: Deep link handling error: %@"
- "%s.%s: Deep link handling skipped — environment not initialized"
- "%s.%s: Failed to perform update action: %s"
- "%s.%s: Failed to unschedule targeted update: %@"
- "%s.%s: Finished to resolve the Deep Linking request for  URL with resource dictionary: %s"
- "%s.%s: Initiating Deep Linking resolution request for URL with resource dictionary: %s"
- "%s.%s: Resolved deep link with response: %s"
- "%s.%s: Resolving deep link request: %s"
- "%s.%s: Settings Experience Plugin - Initiating Deep Linking resolution request for URL: %s"
- "%s.%s: Skipping on assignment of automatic download to \"%{bool}d\" because the automatic download toggle is disabled"
- "%s.%s: Skipping on assignment of automatic update to \"%{bool}d\" because the automatic updates toggle is disabled"
- "%s.%s: Toggeled automatic update enabled while targetted update is not scheduled: %{bool}d"
- "%s.%s: Toggeled automatic update enabled while targetted update is scheduled: %{bool}d"
- "%s.%s: autoScanAndDownloadIfAvailable(nil) called"
- "%s.%s: unscheduleTargetedUpdate result: %{bool}d"
- "Attempting to perform update action \"%s\" to resolve the deep link action: %s"
- "Could not perform the deep link action %s as the descriptor\nis in an unknown state. Aborting the request."
- "Could not perform the deep link action %s as the descriptor\nis not available to download or available to install. Aborting the request."
- "User Action: Sets %{bool}d for auto Install System files in AutomaticUpdatesView"
- "User Action: Sets %{bool}d for automatic Download in AutomaticUpdatesView"
- "User Action: Sets %{bool}d for automatic Update in AutomaticUpdatesView"
```
