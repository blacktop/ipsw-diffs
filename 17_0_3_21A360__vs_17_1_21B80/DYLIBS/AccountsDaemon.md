## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-947.1.0.0.0
-  __TEXT.__text: 0x65990
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x3198
-  __TEXT.__const: 0x48
-  __TEXT.__oslogstring: 0x7de7
-  __TEXT.__cstring: 0x3584
-  __TEXT.__gcc_except_tab: 0x1ea4
+951.0.0.0.0
+  __TEXT.__text: 0x6674c
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_methlist: 0x31e8
+  __TEXT.__const: 0x50
+  __TEXT.__oslogstring: 0x7f71
+  __TEXT.__cstring: 0x379b
+  __TEXT.__gcc_except_tab: 0x1eb8
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x16a8
-  __TEXT.__objc_classname: 0x5da
-  __TEXT.__objc_methname: 0xadcd
-  __TEXT.__objc_methtype: 0x2451
-  __TEXT.__objc_stubs: 0x8c60
+  __TEXT.__unwind_info: 0x16e4
+  __TEXT.__objc_classname: 0x5f3
+  __TEXT.__objc_methname: 0xb003
+  __TEXT.__objc_methtype: 0x246c
+  __TEXT.__objc_stubs: 0x8ee0
   __DATA_CONST.__got: 0x8e0
-  __DATA_CONST.__const: 0x1548
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__const: 0x15b8
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4068
-  __DATA_CONST.__objc_selrefs: 0x2680
+  __DATA_CONST.__objc_const: 0x40b0
+  __DATA_CONST.__objc_selrefs: 0x2728
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__objc_const: 0x13f0
-  __AUTH_CONST.__cfstring: 0x2f40
+  __AUTH_CONST.__objc_const: 0x1438
+  __AUTH_CONST.__cfstring: 0x31e0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH.__objc_data: 0x370
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__auth_got: 0x638
+  __AUTH.__objc_data: 0x3c0
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x388
+  __DATA.__objc_classrefs: 0x3b0
   __DATA.__objc_superrefs: 0x120
   __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x5c8

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7F8DF087-C3D0-3BD9-9FC3-58FA29B450B7
-  Functions: 1932
-  Symbols:   6544
-  CStrings:  3305
+  UUID: ED58E738-9ACF-3BDB-A18E-E58D2DB44C49
+  Functions: 1954
+  Symbols:   6624
+  CStrings:  3379
 
Symbols:
+ +[ACDPluginAnalyticsSender _selected_PostTapToRadar:description:]
+ +[ACDPluginAnalyticsSender _selected_PostTapToRadar:description:].cold.1
+ +[ACDPluginAnalyticsSender _timeSinceLastTTROffered]
+ +[ACDPluginAnalyticsSender accountsTTREnabled]
+ +[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:]
+ +[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:].cold.1
+ +[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:].cold.2
+ +[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:].cold.3
+ +[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:].cold.4
+ +[ACDUserNotification showUserNotificationWithTitle:message:cancelButtonTitle:otherButtonTitle:level:withCompletionBlock:]
+ -[ACDAccountStore clientTokenForAccount:]
+ -[ACDAuthenticationPluginManager renewalCredentialTimeout]
+ GCC_except_table196
+ GCC_except_table201
+ GCC_except_table222
+ GCC_except_table227
+ _OBJC_CLASS_$_ACDPluginAnalyticsSender
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_METACLASS_$_ACDPluginAnalyticsSender
+ __OBJC_$_CLASS_METHODS_ACDPluginAnalyticsSender
+ __OBJC_CLASS_RO_$_ACDPluginAnalyticsSender
+ __OBJC_METACLASS_RO_$_ACDPluginAnalyticsSender
+ ___41-[ACDAccountStore clientTokenForAccount:]_block_invoke
+ ___41-[ACDAccountStore clientTokenForAccount:]_block_invoke_2
+ ___65+[ACDPluginAnalyticsSender _selected_PostTapToRadar:description:]_block_invoke
+ ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.49
+ ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.49.cold.1
+ ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.63
+ ___95-[ACDAuthenticationPluginManager discoverPropertiesForAccount:accountStore:options:completion:]_block_invoke.74
+ ___98+[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:]_block_invoke
+ ___98+[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:]_block_invoke.cold.1
+ ___98+[ACDPluginAnalyticsSender openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:]_block_invoke.cold.2
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s_e34_v24?0^{__CFUserNotification=}8Q16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e20_v24?0q8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ _objc_msgSend$URL
+ _objc_msgSend$_selected_PostTapToRadar:description:
+ _objc_msgSend$_timeSinceLastTTROffered
+ _objc_msgSend$accountsTTREnabled
+ _objc_msgSend$cancelTimer
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$distantPast
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$renewalCredentialTimeout
+ _objc_msgSend$setHost:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$showUserNotificationWithTitle:message:cancelButtonTitle:otherButtonTitle:level:withCompletionBlock:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$unsignedIntegerValue
+ _objc_retain_x10
+ _objc_retain_x7
- GCC_except_table198
- GCC_except_table20
- GCC_except_table219
- GCC_except_table224
- ___93-[ACDAuthenticationPluginManager renewCredentialsForAccount:accountStore:options:completion:]_block_invoke.41
- ___95-[ACDAuthenticationPluginManager discoverPropertiesForAccount:accountStore:options:completion:]_block_invoke.52
- ___block_descriptor_80_e8_32s40s48s56s64s_e20_v24?0q8"NSError"16ls32l8s40l8s48l8s56l8s64l8
CStrings:
+ "990749"
+ "@\"Call to renewCredentialsForAccount:accountStore:options:completion: on %@ failed to complete in expected time %llu.\""
+ "@\"Canceled open Tap-To-Radar\""
+ "@\"Offering to open Tap-To-Radar\""
+ "@\"Open Tap-To-Radar called on external build\""
+ "@\"Open Tap-To-Radar disabled\""
+ "@\"Open Tap-To-Radar offered in the last week\""
+ "@\"Opening Tap-To-Radar\""
+ "@\"_selected_PostTapToRadar Tap-To-Radar called on external build\""
+ "ACDPluginAnalyticsSender"
+ "Accounts is tracking issues with slow or stuck credential renewals, please help us out by filing a radar via Tap-To-Radar"
+ "BundleID"
+ "Cancel"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Crash/Hang/Data Loss"
+ "Description"
+ "I was informed of a slow or hung authentication plugin, please investigate."
+ "Open Tap-To-Radar"
+ "Slow Credential Renewal"
+ "Slow Credential Renewal: %@"
+ "Title"
+ "URL"
+ "_selected_PostTapToRadar:description:"
+ "_timeSinceLastTTROffered"
+ "accountsTTREnabled"
+ "cancelTimer"
+ "clientTokenForAccount:"
+ "com.apple.accounts.ttr.enabled"
+ "com.apple.accounts.ttr.lastOffered"
+ "defaultWorkspace"
+ "distantPast"
+ "iOS"
+ "initWithSuiteName:"
+ "openTapToRadarWithAlertTitle:alertDescription:TTRTitle:TTRDescription:"
+ "openURL:configuration:completionHandler:"
+ "persistentDomainForName:"
+ "queryItemWithName:value:"
+ "renewalCredentialTimeout"
+ "setHost:"
+ "setQueryItems:"
+ "setScheme:"
+ "showUserNotificationWithTitle:message:cancelButtonTitle:otherButtonTitle:level:withCompletionBlock:"
+ "standardUserDefaults"
+ "tap-to-radar"
+ "timeIntervalSinceNow"
+ "unsignedIntegerValue"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v64@0:8@16@24@32@40Q48@?56"

```
