## StorageSettingsUI

> `/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI`

```diff

-166.3.1.0.0
-  __TEXT.__text: 0x7e550
-  __TEXT.__auth_stubs: 0x2330
-  __TEXT.__objc_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x1870
-  __TEXT.__const: 0x4b28
-  __TEXT.__objc_classname: 0x349
-  __TEXT.__objc_methname: 0x4de5
-  __TEXT.__objc_methtype: 0xf3e
-  __TEXT.__cstring: 0x4b2b
-  __TEXT.__oslogstring: 0x8f6
+166.5.2.0.0
+  __TEXT.__text: 0x826b4
+  __TEXT.__auth_stubs: 0x23b0
+  __TEXT.__objc_stubs: 0x4800
+  __TEXT.__objc_methlist: 0x18e0
+  __TEXT.__const: 0x4cb8
+  __TEXT.__objc_classname: 0x65e
+  __TEXT.__objc_methname: 0x55d5
+  __TEXT.__objc_methtype: 0x12bf
+  __TEXT.__cstring: 0x445b
+  __TEXT.__oslogstring: 0x956
   __TEXT.__gcc_except_tab: 0x84
   __TEXT.__ustring: 0x994
-  __TEXT.__constg_swiftt: 0x1378
-  __TEXT.__swift5_typeref: 0x56d8
+  __TEXT.__constg_swiftt: 0x1408
+  __TEXT.__swift5_typeref: 0x5938
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xc2f
-  __TEXT.__swift5_fieldmd: 0xe34
+  __TEXT.__swift5_reflstr: 0xc66
+  __TEXT.__swift5_fieldmd: 0xe68
   __TEXT.__swift5_assocty: 0x420
-  __TEXT.__swift5_proto: 0x138
-  __TEXT.__swift5_types: 0x104
-  __TEXT.__swift5_capture: 0x844
-  __TEXT.__swift_as_entry: 0xfc
-  __TEXT.__swift_as_ret: 0xa0
+  __TEXT.__swift5_proto: 0x148
+  __TEXT.__swift5_types: 0x108
+  __TEXT.__swift5_capture: 0x854
+  __TEXT.__swift_as_entry: 0x108
+  __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1c18
-  __TEXT.__eh_frame: 0x2850
-  __DATA_CONST.__auth_got: 0x11a8
-  __DATA_CONST.__got: 0xb30
-  __DATA_CONST.__auth_ptr: 0x908
-  __DATA_CONST.__const: 0x2d28
-  __DATA_CONST.__cfstring: 0x1a00
+  __TEXT.__unwind_info: 0x1cd0
+  __TEXT.__eh_frame: 0x2a28
+  __DATA_CONST.__auth_got: 0x11e8
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__auth_ptr: 0x938
+  __DATA_CONST.__const: 0x2e40
+  __DATA_CONST.__cfstring: 0x1ae0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x4c98
-  __DATA.__objc_selrefs: 0x18f0
-  __DATA.__objc_ivar: 0x164
-  __DATA.__objc_data: 0xf18
-  __DATA.__data: 0x2f28
-  __DATA.__bss: 0x2a30
+  __DATA.__objc_const: 0x4d80
+  __DATA.__objc_selrefs: 0x1970
+  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_data: 0xf20
+  __DATA.__data: 0x2f60
+  __DATA.__bss: 0x2c40
   __DATA.__common: 0x300
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB8863D0-49C0-36E6-84EA-A5D0686C9162
-  Functions: 2335
+  UUID: D9598137-4913-3753-AB3C-C2086759A009
+  Functions: 2366
   Symbols:   500
-  CStrings:  1876
+  CStrings:  1921
 
Symbols:
+ OBJC_IVAR_$_STStorageDetailViewController._stagedSize
+ _OBJC_CLASS_$_SUPurgeOptions
+ _systemUpdatePSUSAppID
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
CStrings:
+ "@64@0:8@16@24@32q40q48q56"
+ "Additional OS Content"
+ "Application update completed: %@"
+ "Application update failed for %@: %@ (%d)"
+ "Delete software update button title in the detail view"
+ "Information about re-downloading the update"
+ "Installing staged app update: %@"
+ "Label in system update detail view, size of additional OS content"
+ "Label in system update detail view, size of the software update"
+ "Pending Update Size"
+ "Pending update size cell label"
+ "StorageSettingsUI"
+ "T@\"PSSpecifier\",&,N,V_updateNowGroupSpec"
+ "T@\"PSSpecifier\",&,N,V_updateNowSpec"
+ "TB,N,V_installingUpdate"
+ "TB,N,V_updateInstalled"
+ "This update has been downloaded and is ready to install."
+ "Update Now"
+ "Update now button section footer"
+ "Update now button title"
+ "View.task @ StorageSettingsUI/DetailView.swift:"
+ "View.task @ StorageSettingsUI/StorageSettingsPreferencesView.swift:"
+ "You can re-download this update later in Software Update settings."
+ "_installingUpdate"
+ "_stagedSize"
+ "_updateInstalled"
+ "_updateNowGroupSpec"
+ "_updateNowSpec"
+ "client:newOSBuildDetected:"
+ "com.apple.fakeapp.SoftwareUpdatePSUS"
+ "deletePendingUpdate()"
+ "initWithAppRecord:bundleIdentifier:name:appSize:dataSize:stagedSize:"
+ "installingUpdate"
+ "prioritizeCoordinatorForAppWithIdentity:completion:"
+ "purgeDownloadWithOptions:withResult:"
+ "setInstallingUpdate:"
+ "setNotifyUser:"
+ "setUpdateInstalled:"
+ "setUpdateNowGroupSpec:"
+ "setUpdateNowSpec:"
+ "setUserRequested:"
+ "softwareUpdateDetails"
+ "stagedSize"
+ "updateInstalled"
+ "updateNowApp"
+ "updateNowGroupSpec"
+ "updateNowSpec"
+ "v32@0:8@\"SUManagerClient\"16@\"NSString\"24"
- "@56@0:8@16@24@32q40q48"
- "initWithAppRecord:bundleIdentifier:name:appSize:dataSize:"

```
