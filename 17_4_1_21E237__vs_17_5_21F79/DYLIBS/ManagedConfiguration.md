## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2288.0.1.0.0
-  __TEXT.__text: 0xd8674
+2295.0.0.0.0
+  __TEXT.__text: 0xd8a38
   __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0xa214
-  __TEXT.__cstring: 0x14605
+  __TEXT.__objc_methlist: 0xa24c
+  __TEXT.__cstring: 0x146a3
   __TEXT.__oslogstring: 0x7d4b
   __TEXT.__const: 0xfb4
   __TEXT.__gcc_except_tab: 0xa48
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2be8
+  __TEXT.__unwind_info: 0x2bf8
   __TEXT.__objc_classname: 0xc76
-  __TEXT.__objc_methname: 0x1be17
-  __TEXT.__objc_methtype: 0x217f
-  __TEXT.__objc_stubs: 0xd020
+  __TEXT.__objc_methname: 0x1bec1
+  __TEXT.__objc_methtype: 0x2153
+  __TEXT.__objc_stubs: 0xd0a0
   __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x4908
+  __DATA_CONST.__const: 0x4948
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa4b0
-  __DATA_CONST.__objc_selrefs: 0x5650
+  __DATA_CONST.__objc_selrefs: 0x5678
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x538
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__cfstring: 0x17fe0
+  __AUTH_CONST.__cfstring: 0x18080
   __AUTH_CONST.__objc_const: 0x3bf0
   __AUTH_CONST.__const: 0x2220
   __AUTH_CONST.__objc_intobj: 0x438

   __AUTH_CONST.__auth_got: 0xb10
   __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0x954
-  __DATA.__data: 0xde8
-  __DATA.__bss: 0x901
+  __DATA.__data: 0xe08
+  __DATA.__bss: 0x8e1
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x200

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4647
-  Symbols:   15315
-  CStrings:  8233
+  Functions: 4653
+  Symbols:   15335
+  CStrings:  8243
 
Symbols:
+ -[MCProfileConnection(CloudConfiguration) cloudConfigurationUIDidCompleteWasApplied:completionHandler:]
+ -[MCProfileConnection(CloudConfiguration) storeProfileData:]
+ -[MCProfileConnection(CloudConfiguration) storeProfileData:completion:]
+ -[MCProfileConnection(Misc) _notificationRestrictedApps]
+ -[MCProfileConnection(Misc) _restrictionEnforcedNotificationSettingsForBundleID:settingsArray:]
+ GCC_except_table238
+ _MCFeatureAutoDimAllowed
+ _MCFeatureNotificationRestrictedApps
+ _MCLegacyCallHistorySyncHelperBundleIdentifier
+ ___100-[MCProfileConnection(Misc) defaultAppBundleIDForCommunicationServiceType:forAccountWithIdentifier:]_block_invoke.47
+ ___60-[MCProfileConnection(CloudConfiguration) storeProfileData:]_block_invoke
+ ___68-[MCProfileConnection(Misc) restrictionEnforcedNotificationSettings]_block_invoke
+ ___block_descriptor_40_e8_32s_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8
+ ___block_literal_global.1291
+ ___block_literal_global.1293
+ ___block_literal_global.1295
+ ___block_literal_global.1297
+ ___block_literal_global.1299
+ ___block_literal_global.46
+ ___block_literal_global.461
+ ___block_literal_global.556
+ ___block_literal_global.564
+ ___block_literal_global.578
+ ___block_literal_global.627
+ ___block_literal_global.662
+ ___block_literal_global.667
+ ___block_literal_global.672
+ ___block_literal_global.677
+ ___block_literal_global.682
+ _objc_msgSend$_notificationRestrictedApps
+ _objc_msgSend$_restrictionEnforcedNotificationSettingsForBundleID:settingsArray:
+ _objc_msgSend$cloudConfigurationUIDidCompleteWasApplied:completionHandler:
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$storeProfileData:
+ _objc_msgSend$storeProfileData:completion:
- GCC_except_table235
- ___100-[MCProfileConnection(Misc) defaultAppBundleIDForCommunicationServiceType:forAccountWithIdentifier:]_block_invoke.45
- ___88-[MCProfileConnection(CloudConfiguration) storeProfileData:configurationSource:purpose:]_block_invoke
- ___block_literal_global.1285
- ___block_literal_global.1290
- ___block_literal_global.1292
- ___block_literal_global.1294
- ___block_literal_global.1296
- ___block_literal_global.455
- ___block_literal_global.550
- ___block_literal_global.558
- ___block_literal_global.572
- ___block_literal_global.621
- ___block_literal_global.656
- ___block_literal_global.661
- ___block_literal_global.666
- ___block_literal_global.671
- ___block_literal_global.676
- _objc_msgSend$storeProfileData:configurationSource:purpose:completion:
- _objc_msgSend$storeProfileData:configurationSource:purpose:completionBlock:
CStrings:
+ "B24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "FEATURE_AUTO_DIM"
+ "FEATURE_WEB_APP_INSTALLATION"
+ "_notificationRestrictedApps"
+ "_restrictionEnforcedNotificationSettingsForBundleID:settingsArray:"
+ "allowAutoDim"
+ "cloudConfigurationUIDidCompleteWasApplied:completionHandler:"
+ "com.apple.CallHistorySyncHelper"
+ "filterUsingPredicate:"
+ "notificationRestrictedApps"
+ "storeProfileData:"
+ "storeProfileData:completion:"
- "storeProfileData:configurationSource:purpose:completion:"
- "v40@0:8@\"NSData\"16i24i28@?<v@?@\"NSError\">32"

```
