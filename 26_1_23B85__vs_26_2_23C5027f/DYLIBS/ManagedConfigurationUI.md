## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-55.42.6.0.0
-  __TEXT.__text: 0x24a68
+55.60.5.0.0
+  __TEXT.__text: 0x247e4
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x3908
+  __TEXT.__objc_methlist: 0x38d8
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x614
-  __TEXT.__cstring: 0x310c
+  __TEXT.__cstring: 0x30bd
   __TEXT.__ustring: 0x46
-  __TEXT.__unwind_info: 0xc90
-  __TEXT.__objc_classname: 0x9c6
-  __TEXT.__objc_methname: 0xab21
-  __TEXT.__objc_methtype: 0x1f55
-  __TEXT.__objc_stubs: 0x7740
+  __TEXT.__unwind_info: 0xc80
+  __TEXT.__objc_classname: 0x9c7
+  __TEXT.__objc_methname: 0xaa31
+  __TEXT.__objc_methtype: 0x1f51
+  __TEXT.__objc_stubs: 0x76e0
   __DATA_CONST.__got: 0x740
-  __DATA_CONST.__const: 0xa88
+  __DATA_CONST.__const: 0xa58
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2818
+  __DATA_CONST.__objc_selrefs: 0x27f8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x410

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F961E806-F8C0-3E9A-ADC9-9879A210D37A
-  Functions: 1108
-  Symbols:   4399
-  CStrings:  2611
+  UUID: 9AA0B54E-4EEC-31D7-8F42-5339961762C2
+  Functions: 1102
+  Symbols:   4383
+  CStrings:  2606
 
Symbols:
+ -[MCUIDataManager _reloadQueue_reloadInBackgroundProfiles:appSigners:blockedApps:]
+ -[MCUIDataManager appDidBecomeActive:]
+ -[MCUIDataManager reloadInBackgroundProfiles:appSigners:blockedApps:]
+ GCC_except_table17
+ GCC_except_table27
+ GCC_except_table31
+ ___69-[MCUIDataManager reloadInBackgroundProfiles:appSigners:blockedApps:]_block_invoke
+ ___82-[MCUIDataManager _reloadQueue_reloadInBackgroundProfiles:appSigners:blockedApps:]_block_invoke
+ ___82-[MCUIDataManager _reloadQueue_reloadInBackgroundProfiles:appSigners:blockedApps:]_block_invoke_2
+ ___block_descriptor_35_e5_v8?0l
+ ___block_descriptor_43_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$_reloadQueue_reloadInBackgroundProfiles:appSigners:blockedApps:
+ _objc_msgSend$reloadInBackgroundProfiles:appSigners:blockedApps:
- +[MCUIDataManager _isDeviceManagementHiddenConcrete]
- -[MCUIDataManager _reloadQueueReloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:]
- -[MCUIDataManager appMovedToForeground:]
- -[MCUIDataManager reloadAllDataInBackgroundWithCompletion:]
- -[MCUIDataManager reloadAppSignersAndBlockedAppsInBackgroundWithCompletion:]
- -[MCUIDataManager reloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:]
- -[MCUIDataManager reloadProfilesInBackgroundWithCompletion:]
- GCC_except_table16
- GCC_except_table26
- GCC_except_table28
- GCC_except_table30
- GCC_except_table32
- GCC_except_table4
- ___101-[MCUIDataManager reloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:]_block_invoke
- ___113-[MCUIDataManager _reloadQueueReloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:]_block_invoke
- ___113-[MCUIDataManager _reloadQueueReloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:]_block_invoke_2
- ___60-[MCUIDataManager reloadProfilesInBackgroundWithCompletion:]_block_invoke
- ___76-[MCUIDataManager reloadAppSignersAndBlockedAppsInBackgroundWithCompletion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e83_v56?0"MCProfileInfo"8"NSArray"16"NSArray"24"NSArray"32"NSArray"40"NSArray"48ls32l8
- ___block_descriptor_51_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_91_e8_32s40s48s56s64s72s80bs_e5_v8?0ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
- _objc_msgSend$_isDeviceManagementHiddenConcrete
- _objc_msgSend$_reloadQueueReloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:
- _objc_msgSend$reloadAllDataInBackgroundWithCompletion:
- _objc_msgSend$reloadAppSignersAndBlockedAppsInBackgroundWithCompletion:
- _objc_msgSend$reloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:
CStrings:
+ "MCUIDataManager reloading profiles and app signers because profile list changed"
+ "_reloadQueue_reloadInBackgroundProfiles:appSigners:blockedApps:"
+ "appDidBecomeActive:"
+ "reloadInBackgroundProfiles:appSigners:blockedApps:"
+ "v28@0:8B16B20B24"
- "Data manager reloading all data in background because profile list changed"
- "_isDeviceManagementHiddenConcrete"
- "_reloadQueueReloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:"
- "appMovedToForeground:"
- "reloadAllDataInBackgroundWithCompletion:"
- "reloadAppSignersAndBlockedAppsInBackgroundWithCompletion:"
- "reloadDataInBackgroundIncludingProfiles:appSigners:blockedApplications:completion:"
- "reloadProfilesInBackgroundWithCompletion:"
- "v36@0:8B16B20B24@?28"
- "v56@?0@\"MCProfileInfo\"8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48"

```
