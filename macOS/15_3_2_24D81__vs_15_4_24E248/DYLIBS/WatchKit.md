## WatchKit

> `/System/iOSSupport/System/Library/Frameworks/WatchKit.framework/Versions/A/WatchKit`

```diff

-892.25.0.0.0
-  __TEXT.__text: 0x3504c
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x3b04
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x4cf0
+2001.4.2.0.0
+  __TEXT.__text: 0x352e4
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x3eec
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x4cea
   __TEXT.__oslogstring: 0x2daa
-  __TEXT.__gcc_except_tab: 0x694
+  __TEXT.__gcc_except_tab: 0x6a0
   __TEXT.__dlopen_cstrs: 0x20b
-  __TEXT.__unwind_info: 0xd90
+  __TEXT.__unwind_info: 0xd98
   __TEXT.__objc_classname: 0x761
   __TEXT.__objc_methname: 0x7e91
   __TEXT.__objc_methtype: 0xe87

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ef8
+  __DATA_CONST.__objc_selrefs: 0x1fa8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x4b60
-  __AUTH_CONST.__objc_const: 0x79f0
+  __AUTH_CONST.__objc_const: 0x72d8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1590

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89FE1026-45CE-3045-AF39-3FB3A4C7C9C3
-  Functions: 1614
-  Symbols:   3968
-  CStrings:  3154
+  UUID: E8022504-9ED8-33E1-AC53-6D0080BD0BB2
+  Functions: 1629
+  Symbols:   3996
+  CStrings:  3151
 
Symbols:
+ +[SPCompanionAssetCache sharedInstance].cold.1
+ +[SPProtoSerializer arrayWithSPPlist:].cold.1
+ +[SPProtoSerializer dictionaryWithSPPlist:].cold.1
+ +[SPProtoSerializer spPlistWithArray:].cold.1
+ +[SPProtoSerializer spPlistWithDictionary:].cold.1
+ +[SPRemoteInterface _remoteIdentifier].cold.1
+ +[WKInterfaceDevice currentDevice].cold.1
+ -[NSString(SPExtras) _sp_stringByEncodingIllegalFilenameCharacters].cold.1
+ -[SPRemoteInterface _performAfterSendSetViewControllers:].cold.1
+ -[WKInterfaceController init].cold.1
+ GCC_except_table318
+ SPInterfaceObjectWithType.cold.1
+ WKInterfaceControllerClass.cold.1
+ _WKInterfaceObjectClassWithType.cold.1
+ __115-[SPRemoteInterface createViewController:className:properties:contextID:info:gestureDescriptions:clientIdentifier:]_block_invoke.cold.1
+ __41+[SPRemoteInterface _updateAccessibility]_block_invoke.cold.1
+ __SPLaunchSockPuppetAppForCompanionAppWithIdentifier_block_invoke.cold.2
+ isRunningOnMainQueue.cold.1
+ spUtils_SPURLQueryAllowedCharacterSet.cold.1
+ spUtils_allowedClassesForUserActivity.cold.1
+ spUtils_appExtensionFirstUnlock.cold.2
+ spUtils_deserializeObject.cold.1
+ spUtils_isRunningInAnyDemoMode.cold.1
+ spUtils_isRunningInF201DemoMode.cold.1
+ spUtils_isRunningInF5DemoMode.cold.1
+ spUtils_machTimeString.cold.1
+ spUtils_serializeObject.cold.1
+ wk_bg_app_refresh_log.cold.1
+ wk_default_log.cold.1
+ wk_extension_loading_log.cold.1
- GCC_except_table308
- _fmod
- _strcmp

```
