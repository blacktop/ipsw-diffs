## PreferencePanes

> `/System/Library/Frameworks/PreferencePanes.framework/Versions/A/PreferencePanes`

```diff

-408.2.1.0.0
-  __TEXT.__text: 0x1be2c
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x1af4
+408.3.1.0.0
+  __TEXT.__text: 0x1bec0
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_methlist: 0x23c0
   __TEXT.__cstring: 0x2a7a
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x9b0
+  __TEXT.__gcc_except_tab: 0x9c8
   __TEXT.__ustring: 0x5e
-  __TEXT.__unwind_info: 0x888
+  __TEXT.__unwind_info: 0x8a0
   __TEXT.__objc_classname: 0x40b
   __TEXT.__objc_methname: 0x53c3
   __TEXT.__objc_methtype: 0x12e1

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1668
+  __DATA_CONST.__objc_selrefs: 0x1a80
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0xb10
   __AUTH_CONST.__cfstring: 0x2ac0
-  __AUTH_CONST.__objc_const: 0x4600
+  __AUTH_CONST.__objc_const: 0x3538
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A2266A49-F57D-389A-86B7-BE8DE8507180
-  Functions: 710
-  Symbols:   2067
+  UUID: 14FC3D4C-2151-33EA-A2DC-B672F2D5B15F
+  Functions: 731
+  Symbols:   2090
   CStrings:  1967
 
Symbols:
+ +[NSPrefPaneBundle numberingSystemIsArabic].cold.1
+ +[NSPrefPaneUtils hasBattery].cold.1
+ +[NSPrefPanesCenter prefPanesDirectoriesIncludingSystem:].cold.1
+ +[NSPrefPanesCenter sharedPreferencesCenter].cold.1
+ +[NSPrefPanesCenter systemCacheFilePath].cold.1
+ +[NSPrefPanesCenter userCacheFilePath].cold.1
+ +[NSProxyPreferencePane isDebug].cold.1
+ +[PreferencePaneDispatch sharedDispatch].cold.1
+ -[NSPrefPaneBundle _isSignedByAppleUsingStaticCodeRef:].cold.1
+ -[NSPrefPaneBundle iconLabel].cold.1
+ -[NSPrefPaneBundle icon].cold.1
+ -[NSPrefPaneBundle largeIcon].cold.1
+ -[NSPrefPaneBundle localizedIconLabels].cold.1
+ -[NSPrefPaneBundle localizedNames].cold.1
+ -[NSPrefPaneBundle longName].cold.1
+ -[NSPrefPaneBundle shortName].cold.1
+ -[NSPrefPanesCenter serialNumber].cold.1
+ -[NSPrefRemoteViewService loadView].cold.1
+ -[NSProxyPreferencePane hasElementForKey:].cold.1
+ -[NSProxyPreferencePane helpMenuItems].cold.1
+ -[NSVBProxyPreferencePane _createConnectionIfNeededWithCompletion:].cold.1
+ _acos
+ initSLSGetSystemUIHasRTLDirectionLegacy.cold.1
Functions:
~ +[NSPrefPanesCenter sharedPreferencesCenter] : 84 -> 68
~ +[NSPrefPanesCenter systemCacheFilePath] : 84 -> 68
~ +[NSPrefPanesCenter cacheFolderPathForDomain:] : 372 -> 376
~ +[NSPrefPanesCenter userCacheFilePath] : 84 -> 68
~ +[NSPrefPanesCenter prefPanesDirectoriesIncludingSystem:] : 132 -> 116
~ -[NSPrefPaneBundle shortName] : 380 -> 364
~ -[NSPrefPaneBundle isVisible] : 32 -> 24
~ -[NSPrefPaneBundle iconLabel] : 572 -> 556
~ -[NSPrefPaneBundle localizedIconLabels] : 592 -> 572
~ -[NSPrefPaneBundle icon] : 1156 -> 1144
~ -[NSPrefPaneBundle largeIcon] : 1324 -> 1304
~ -[NSPrefPaneBundle _localeAwareIconNames:] : 912 -> 916
~ +[NSPrefPaneBundle numberingSystemIsArabic] : 68 -> 56
~ _initSLSGetSystemUIHasRTLDirectionLegacy : 104 -> 88
~ -[NSPrefCrossFadeWindowMoveHelper init] : 176 -> 168
~ -[NSPrefCrossFadeWindowMoveHelper _resizeWindow:toFrame:display:] : 316 -> 304
~ -[NSPrefCrossFadeWindowMoveHelper _doAnimation:] : 304 -> 296
~ __NSPrefWindowMoveHelperTimerCallBack : 536 -> 540
~ -[NSProxyPreferencePane helpMenuItems] : 452 -> 436
~ -[NSCFPrefManager registerDefaults:forDomain:] : 64 -> 56
~ -[NSPreferencePane assignMainView] : 248 -> 256
~ -[NSPreferencePane setFirstKeyView:] : 280 -> 276
~ -[NSPreference didResignActive] : 120 -> 124
~ +[NSPrefPaneUtils humanStringForModifiers:] : 828 -> 824
~ -[NSAdminPreference mainViewDidLoad] : 1216 -> 1192
~ -[NSAdminPreference authorizationViewDidAuthorize:] : 616 -> 608
~ +[NSPrefPaneUtils hasBattery] : 68 -> 56
~ -[NSPrefPaneBundle _isSignedByAppleUsingStaticCodeRef:] : 408 -> 392
~ -[NSPrefPaneBundle hasEntitlement:] : 280 -> 276
~ -[NSPrefPaneBundle longName] : 312 -> 296
~ -[NSPrefPaneBundle localizedNames] : 484 -> 468
~ -[NSPrefPaneBundle encodeWithCoder:] : 1060 -> 1064
~ -[NSPrefPanesCenter serialNumber] : 84 -> 68
~ ___59-[NSPrefPanesCenter _writeCache:isSystemCache:synchronous:]_block_invoke : 1664 -> 1668
~ -[NSPrefPanesCenter indexOfPrefPaneWithBundlePath:] : 356 -> 352
~ -[NSPrefPanesCenter indexOfPrefPane:] : 312 -> 308
~ -[NSPreference(MacManagerSupport_Private) _findControlWithTag:inView:] : 548 -> 552
~ -[NSAdminPreference doFinishPaneSwitch:] : 148 -> 144
~ -[NSAdminPreference doCancelPaneSwitch:] : 24 -> 28
~ -[NSAdminPreference willDeauthenticate:] : 124 -> 116
~ -[NSCFPrefManager booleanForKey:inDomain:] : 312 -> 308
~ -[NSPrefTabsController finishPaneSwitch:] : 84 -> 76
~ +[NSPrefPaneUtils _stringForCharacterCode:useNamesWhenPossible:] : 912 -> 904
- sub_1b9c74fb0
~ -[NSPrefPaneSearchCenter createSearchIndexForPrefPaneBundles:] : 3472 -> 3516
~ -[NSPrefPaneSearchCenter searchString:inPreferencePane:] : 1168 -> 1172
~ -[NSVBProxyPreferencePane _createConnectionIfNeededWithCompletion:] : 432 -> 344
~ ___67-[NSVBProxyPreferencePane _createConnectionIfNeededWithCompletion:]_block_invoke : 628 -> 624
~ __67-[NSVBProxyPreferencePane _createConnectionIfNeededWithCompletion:]_block_invoke.33 : 252 -> 244
~ -[NSVBProxyPreferencePane didUnselect] : 244 -> 248
~ ___38-[NSVBProxyPreferencePane didUnselect]_block_invoke : 276 -> 272
~ -[AddRemoveView awakeFromNib] : 420 -> 432
~ -[NSString(NSPrefPaneStringAdditions) centerTruncateStringToFit:] : 216 -> 212
~ -[NSPrefAnimatedView isOpaque] : 80 -> 84
~ +[NSProxyPreferencePane isDebug] : 68 -> 56
~ -[NSProxyPreferencePane hasElementForKey:] : 440 -> 424
~ -[NSPrefRemoteViewService loadView] : 2928 -> 2912
~ +[PreferencePaneDispatch sharedDispatch] : 84 -> 68
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSAdminMultiAuthenticator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSAdminPreference.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSPrefPaneBundle.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSPrefPanesCenter.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSProxyLegacyPreferencePane.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSProxyPreferencePane.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSVBProxyPreferencePane.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSAdminMultiAuthenticator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSAdminPreference.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSPrefPaneBundle.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSPrefPanesCenter.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSProxyLegacyPreferencePane.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSProxyPreferencePane.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PrefPanesFramework/NSVBProxyPreferencePane.m"

```
