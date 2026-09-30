## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/Versions/A/FrontBoardServices`

```diff

-943.3.9.0.0
-  __TEXT.__text: 0x958bc
+943.5.17.0.0
+  __TEXT.__text: 0x94db4
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x6dac
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x917f
-  __TEXT.__oslogstring: 0x3148
-  __TEXT.__gcc_except_tab: 0x19f8
-  __TEXT.__unwind_info: 0x2540
+  __TEXT.__objc_methlist: 0x7e80
+  __TEXT.__const: 0x240
+  __TEXT.__cstring: 0x938c
+  __TEXT.__oslogstring: 0x3108
+  __TEXT.__gcc_except_tab: 0x19fc
+  __TEXT.__unwind_info: 0x2600
   __TEXT.__objc_classname: 0x12ed
-  __TEXT.__objc_methname: 0xeec0
-  __TEXT.__objc_methtype: 0x3267
-  __TEXT.__objc_stubs: 0x9940
+  __TEXT.__objc_methname: 0xef77
+  __TEXT.__objc_methtype: 0x3282
+  __TEXT.__objc_stubs: 0x99c0
   __DATA_CONST.__got: 0x678
-  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36e0
+  __DATA_CONST.__objc_selrefs: 0x37a8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x308
   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0x2b20
-  __AUTH_CONST.__cfstring: 0x8c00
-  __AUTH_CONST.__objc_const: 0x10fe0
+  __AUTH_CONST.__cfstring: 0x8d40
+  __AUTH_CONST.__objc_const: 0xf230
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x9d8
+  __DATA.__objc_ivar: 0x9e0
   __DATA.__data: 0x17d0
-  __DATA.__bss: 0x254
+  __DATA.__bss: 0x25c
   __DATA_DIRTY.__objc_data: 0x23f0
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD75D4F3-FB24-335B-9991-A4DA1CA82AB2
-  Functions: 3646
-  Symbols:   8224
-  CStrings:  6039
+  UUID: 48BE52CD-B2AB-391F-8A4C-C2E49161CF55
+  Functions: 3828
+  Symbols:   8275
+  CStrings:  6068
 
Symbols:
+ +[FBSApplicationDataStoreClientFactory sharedInstance].cold.1
+ +[FBSApplicationPlaceholder _callOutQueue].cold.1
+ +[FBSApplicationPlaceholder _sharedQueue].cold.1
+ +[FBSDispatchSerialQueue _mainQueue].cold.1
+ +[FBSDisplayConfiguration _virtualDisplayConfigurationWithIdentifier:]
+ +[FBSDisplayLayoutMonitor interface].cold.1
+ +[FBSDisplayMode _emptyMode].cold.1
+ +[FBSOpenApplicationServiceSpecification interface].cold.1
+ +[FBSProcess currentProcess].cold.1
+ +[FBSProfileManager sharedInstance].cold.1
+ +[FBSPseudoSceneUpdater sharedInstance].cold.1
+ +[FBSSceneHostHandle localHandle].cold.1
+ +[FBSSceneIdentityToken tokenWithHostEndpoint:workspace:identifier:].cold.8
+ +[FBSSceneIdentityToken tokenWithHostPID:directEndpointTarget:workspace:identifier:].cold.8
+ +[FBSSerialQueue queueWithDispatchQueue:].cold.2
+ +[FBSSystemService clientCallbackQueue].cold.1
+ +[FBSSystemService sharedService].cold.1
+ -[FBSApplicationDataStore objectForKey:withResult:].cold.1
+ -[FBSApplicationDataStore setArchivedObject:forKey:].cold.2
+ -[FBSApplicationInfo _initWithApplicationProxy:record:appIdentity:processIdentity:overrideURL:].cold.1
+ -[FBSDisplayConfiguration isVirtualized]
+ -[FBSDisplayConfigurationBuilder buildWithError:]
+ -[FBSDisplayConfigurationBuilder setDisplayType:]
+ -[FBSDisplayConfigurationBuilder setDisplayType:].cold.1
+ -[FBSDisplayConfigurationBuilder setDisplayType:].cold.2
+ -[FBSDisplayConfigurationBuilder setDisplayType:].cold.3
+ -[FBSDisplayIdentity _initWithType:UIKitMainLike:displayID:connectionType:connectionSeed:pid:external:uniqueIdentifier:secure:root:].cold.1
+ -[FBSDisplayIdentity isVirtualized]
+ -[FBSDisplayMode _copyWithOverrideSize:scale:refreshRate:]
+ -[FBSDisplayMode _initWithCADisplayMode:scale:rotation:].cold.1
+ -[FBSDisplaySource _lock_noteConnected].cold.5
+ -[FBSDisplaySource _lock_noteDisconnecting].cold.3
+ -[FBSDisplaySource _lock_setRawReportedConfiguration:effectiveReportedConfigurations:].cold.2
+ -[FBSDisplaySource _updateForInitialization:forTransformInvalidation:].cold.4
+ -[FBSMainRunLoopSerialQueue _initWithModes:].cold.2
+ -[FBSSceneClientSettingsDiffInspector init].cold.1
+ -[FBSSceneSettingsDiffInspector init].cold.1
+ -[FBSSettings _addSceneExtension:].cold.4
+ -[FBSSettings _applySettings:].cold.3
+ -[FBSSettings _removeAllSceneExtensions].cold.2
+ -[FBSSettings _removeVolatileSettings].cold.2
+ -[FBSSettings _setValue:forSetting:].cold.3
+ -[FBSSettings _underlyingValueForSetting:].cold.2
+ -[FBSSettings hash].cold.1
+ -[FBSSettings mutableCopyWithZone:].cold.1
+ -[FBSSettingsDiff _containsSetting:].cold.2
+ -[FBSSettingsDiffInspector _observeSetting:withBlock:].cold.4
+ -[FBSShutdownOptions initWithReason:].cold.1
+ -[FBSWorkspace _queue_scenesClientForEndpoint:creatingIfNecessary:].cold.3
+ -[FBSWorkspaceSceneRequestOptions initWithBSXPCCoder:].cold.1
+ -[FBSWorkspaceScenesClient queue_activate].cold.2
+ -[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:].cold.5
+ FBLogAppDataStore.cold.1
+ FBLogAppLaunch.cold.1
+ FBLogCommon.cold.1
+ FBLogInterfaceOrientationObserver.cold.1
+ FBLogSceneClient.cold.1
+ FBLogSceneExtension.cold.1
+ FBLogWatchdog.cold.1
+ FBSFrameworkBundle.cold.1
+ FBSLogApplicationLibrary.cold.1
+ FBSLogApplicationLibraryObserver.cold.1
+ FBSLogApplicationPlaceholder.cold.1
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table166
+ GCC_except_table54
+ GCC_except_table61
+ GCC_except_table79
+ GCC_except_table95
+ OBJC_IVAR_$_FBSDisplayConfigurationBuilder._lock_displayType
+ OBJC_IVAR_$_FBSDisplayConfigurationBuilder._lock_displayTypeSet
+ _BSLogAddStateCaptureBlockForUserRequestsOnlyWithTitle
+ _FBSDisplayTagToFBSDisplayType
+ _FBSDisplayTypeToDisplayTag
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.236
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.240
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.244
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.250
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.256
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.261
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke.266
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.245
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.251
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.257
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.262
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke_3.246
+ __35-[FBSDisplayConfiguration isEqual:]_block_invoke_3.252
+ __39-[FBSDisplaySource _lock_noteConnected]_block_invoke.cold.2
+ __43-[FBSDisplaySource _lock_noteDisconnecting]_block_invoke.cold.2
+ __63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.181.cold.2
+ __63-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:]_block_invoke.181.cold.3
+ __65-[FBSWorkspaceScenesClient scene:didReceiveActions:forExtension:]_block_invoke.cold.1
+ __88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.120.cold.1
+ __88-[FBSWorkspaceScenesClient _initWithIdentifier:connection:queue:calloutQueue:workspace:]_block_invoke.cold.1
+ __94-[FBSApplicationLibrary _handleApplicationStateDidChange:notifyForUpdateInsteadOfReplacement:]_block_invoke.177
+ __94-[FBSWorkspaceScenesClient _queue_updateScene:withSettings:diff:transitionContext:completion:]_block_invoke.cold.1
+ __MergedGlobals
+ ___ingestPropertiesFromSettingsSubclass_block_invoke.437
+ ___realizeSettingsExtension_block_invoke.256
+ ___realizeSettingsExtension_block_invoke.260
+ ___realizeSettingsExtension_block_invoke.267
+ ___realizeSettingsExtension_block_invoke.271
+ ___realizeSettingsExtension_block_invoke.275
+ ___realizeSettingsExtension_block_invoke.279
+ ___realizeSettingsExtension_block_invoke.283
+ ___realizeSettingsExtension_block_invoke.287
+ ___realizeSettingsExtension_block_invoke.303
+ ___realizeSettingsExtension_block_invoke.307
+ ___realizeSettingsExtension_block_invoke.311
+ ___realizeSettingsExtension_block_invoke.311.cold.1
+ ___realizeSettingsExtension_block_invoke.311.cold.2
+ ___realizeSettingsExtension_block_invoke.326
+ ___realizeSettingsExtension_block_invoke.330
+ ___realizeSettingsExtension_block_invoke.334
+ ___realizeSettingsExtension_block_invoke.338
+ ___realizeSettingsExtension_block_invoke.342
+ ___realizeSettingsExtension_block_invoke.346
+ _objc_msgSend$_copyWithOverrideSize:scale:
+ _objc_msgSend$_copyWithOverrideSize:scale:refreshRate:
+ _objc_msgSend$buildWithError:
+ _objc_msgSend$currentPhase
+ _objc_msgSend$isVirtualized
- -[FBSDisplaySource _lock_setRawConfiguration:].cold.1
- GCC_except_table123
- GCC_except_table126
- GCC_except_table132
- GCC_except_table136
- GCC_except_table137
- GCC_except_table138
- GCC_except_table163
- GCC_except_table59
- GCC_except_table78
- _BSLogAddStateCaptureBlockWithTitle
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke.229
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke.233
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke.237
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke.243
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke.249
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke.254
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.238
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.244
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.250
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke_2.255
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke_3.239
- __35-[FBSDisplayConfiguration isEqual:]_block_invoke_3.245
- __54-[FBSApplicationLibrary applicationsDidFailToInstall:]_block_invoke.cold.1
- __94-[FBSApplicationLibrary _handleApplicationStateDidChange:notifyForUpdateInsteadOfReplacement:]_block_invoke.171
- ___ingestPropertiesFromSettingsSubclass_block_invoke.434
- ___realizeSettingsExtension_block_invoke.253
- ___realizeSettingsExtension_block_invoke.257
- ___realizeSettingsExtension_block_invoke.264
- ___realizeSettingsExtension_block_invoke.268
- ___realizeSettingsExtension_block_invoke.272
- ___realizeSettingsExtension_block_invoke.276
- ___realizeSettingsExtension_block_invoke.280
- ___realizeSettingsExtension_block_invoke.284
- ___realizeSettingsExtension_block_invoke.297
- ___realizeSettingsExtension_block_invoke.304
- ___realizeSettingsExtension_block_invoke.308
- ___realizeSettingsExtension_block_invoke.308.cold.1
- ___realizeSettingsExtension_block_invoke.308.cold.2
- ___realizeSettingsExtension_block_invoke.323
- ___realizeSettingsExtension_block_invoke.327
- ___realizeSettingsExtension_block_invoke.331
- ___realizeSettingsExtension_block_invoke.335
- ___realizeSettingsExtension_block_invoke.339
- ___realizeSettingsExtension_block_invoke.343
- ___sharedInstance
- ___sharedInstanceInitializationBlocks
- ___sharedInstanceLock
- _objc_msgSend$buildConfigurationWithError:
CStrings:
+ "/System/AppleInternal/Library/Frameworks/QuartzCore.framework/QuartzCore"
+ "/System/AppleInternal/Library/Frameworks/UIKitServices.framework/UIKitServices"
+ "@48@0:8{CGSize=dd}16d32d40"
+ "Virtual Display"
+ "_copyWithOverrideSize:scale:refreshRate:"
+ "_lock_displayType"
+ "_lock_displayTypeSet"
+ "_virtualDisplayConfigurationWithIdentifier:"
+ "buildWithError:"
+ "cannot build a virtualized display configuration that's main display type."
+ "currentPhase"
+ "do not set the display type to airPlay, find that display via FBDisplayManager."
+ "do not set the display type to main, use mainConfiguration on FBDisplayManager."
+ "existing app for %@"
+ "existing placeholder for %@"
+ "invalid display type : %@"
+ "isVirtualized"
+ "selector != ((void*)0)"
+ "setDisplayType:"
+ "settingsClass != ((void*)0)"
+ "vDisplay"
+ "virtualized"
- "existing app for %{public}@"
- "existing placeholder for %{public}@"
- "selector != ((void *)0)"

```
