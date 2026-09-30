## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/Versions/A/FrontBoardServices`

```diff

-935.0.0.0.0
-  __TEXT.__text: 0x93ec0
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x6bc4
+939.0.0.0.0
+  __TEXT.__text: 0x95600
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x6d6c
   __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x90d2
-  __TEXT.__oslogstring: 0x304e
-  __TEXT.__gcc_except_tab: 0x1b38
-  __TEXT.__unwind_info: 0x24d0
-  __TEXT.__objc_classname: 0x12d3
-  __TEXT.__objc_methname: 0xedc1
-  __TEXT.__objc_methtype: 0x3242
-  __TEXT.__objc_stubs: 0x9840
-  __DATA_CONST.__got: 0x668
-  __DATA_CONST.__const: 0xca0
-  __DATA_CONST.__objc_classlist: 0x450
+  __TEXT.__cstring: 0x91a2
+  __TEXT.__oslogstring: 0x3089
+  __TEXT.__gcc_except_tab: 0x19c4
+  __TEXT.__unwind_info: 0x2528
+  __TEXT.__objc_classname: 0x12ed
+  __TEXT.__objc_methname: 0xee9c
+  __TEXT.__objc_methtype: 0x3267
+  __TEXT.__objc_stubs: 0x98e0
+  __DATA_CONST.__got: 0x670
+  __DATA_CONST.__const: 0xd00
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3678
+  __DATA_CONST.__objc_selrefs: 0x36c8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x308
-  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2b10
-  __AUTH_CONST.__cfstring: 0x8b80
-  __AUTH_CONST.__objc_const: 0x10e30
+  __AUTH_CONST.__const: 0x2b50
+  __AUTH_CONST.__cfstring: 0x8c20
+  __AUTH_CONST.__objc_const: 0x10fe0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x730
+  __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x9d8
   __DATA.__data: 0x17d0
-  __DATA.__bss: 0x24c
+  __DATA.__bss: 0x254
   __DATA_DIRTY.__objc_data: 0x23f0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3585
-  Symbols:   8148
-  CStrings:  1367
+  Functions: 3637
+  Symbols:   8214
+  CStrings:  1373
 
Symbols:
+ +[FBSPseudoSceneUpdater sharedInstance]
+ +[FBSScene pseudoSceneWithIdentifier:specification:]
+ +[FBSScene pseudoSceneWithIdentifier:specification:].cold.1
+ +[FBSScene pseudoSceneWithIdentifier:specification:].cold.2
+ +[FBSSceneIdentityToken pseudoTokenWithIdentifier:]
+ +[FBSSettings settingForSubclassProperty:]
+ +[FBSSettings settingForSubclassProperty:].cold.1
+ +[FBSSettingsExtension extensionForProtocol:].cold.2
+ -[FBSApplicationDataStoreMonitor add:]
+ -[FBSApplicationDataStoreMonitor remove:]
+ -[FBSApplicationPlaceholder add:]
+ -[FBSApplicationPlaceholder remove:]
+ -[FBSDisplayLayoutPublisher add:]
+ -[FBSDisplayLayoutPublisher remove:]
+ -[FBSDisplayMonitor add:]
+ -[FBSDisplayMonitor remove:]
+ -[FBSPseudoSceneUpdater activateSceneFuture:completion:]
+ -[FBSPseudoSceneUpdater callOutQueue]
+ -[FBSPseudoSceneUpdater canHaveAgent]
+ -[FBSPseudoSceneUpdater createSceneFutureWithDefinition:]
+ -[FBSPseudoSceneUpdater hostProcess]
+ -[FBSPseudoSceneUpdater identifier]
+ -[FBSPseudoSceneUpdater requestSceneWithOptions:completion:]
+ -[FBSPseudoSceneUpdater scene:didReceiveActions:forExtension:]
+ -[FBSPseudoSceneUpdater scene:didReceiveActions:forExtension:].cold.1
+ -[FBSPseudoSceneUpdater scene:didUpdateClientSettings:withDiff:transitionContext:]
+ -[FBSPseudoSceneUpdater scene:sendMessage:withResponse:]
+ -[FBSPseudoSceneUpdater sceneWithIdentity:]
+ -[FBSPseudoSceneUpdater scenes]
+ -[FBSPseudoSceneUpdater sendActions:toWorkspaceID:completion:]
+ -[FBSScene add:]
+ -[FBSScene invalidate]
+ -[FBSScene invalidate].cold.1
+ -[FBSScene remove:]
+ -[FBSScene updateSettings:]
+ -[FBSScene updateSettings:].cold.1
+ -[FBSSceneTransitionContextCore error]
+ -[FBSSceneTransitionContextCore setError:]
+ -[FBSSetting expectedClass]
+ -[FBSSetting indirect_defaultValue]
+ -[FBSSetting type]
+ -[FBSSettings _underlyingValueForSetting:]
+ -[FBSSettings _underlyingValueForSetting:].cold.1
+ -[FBSSettings containsSetting:]
+ -[FBSSettings valueForSetting:]
+ -[FBSSettings valueForSetting:].cold.1
+ -[FBSSettingsDiff _containsAnySettingNamed:]
+ -[FBSSettingsDiff _containsAnySettingNamed:].cold.1
+ -[FBSSettingsDiff _containsKey:]
+ -[FBSSettingsDiff _containsKey:].cold.1
+ -[FBSWorkspace _callOutQueue]
+ FBSSubclassHasBeenIngested.cold.1
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table126
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table18
+ GCC_except_table26
+ GCC_except_table38
+ GCC_except_table76
+ GCC_except_table93
+ GCC_except_table94
+ _FBSSettingForLegacySelector
+ _FBSSubclassHasBeenIngested
+ _OBJC_$_PROP_LIST_FBSSceneTransitionContext.165
+ _OBJC_CLASS_$_FBSPseudoSceneUpdater
+ _OBJC_METACLASS_$_FBSPseudoSceneUpdater
+ __51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.216
+ __51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.223
+ __51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.226
+ __76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.200
+ __76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.204
+ __NSIsNSValue
+ __OBJC_$_CLASS_METHODS_FBSPseudoSceneUpdater
+ __OBJC_$_CLASS_METHODS_FBSScene
+ __OBJC_$_INSTANCE_METHODS_FBSPseudoSceneUpdater
+ __OBJC_$_PROP_LIST_FBSPseudoSceneUpdater
+ __OBJC_CLASS_PROTOCOLS_$_FBSPseudoSceneUpdater
+ __OBJC_CLASS_RO_$_FBSPseudoSceneUpdater
+ __OBJC_METACLASS_RO_$_FBSPseudoSceneUpdater
+ ___27-[FBSScene updateSettings:]_block_invoke
+ ___39+[FBSPseudoSceneUpdater sharedInstance]_block_invoke
+ ___44-[FBSSettingsDiff _containsAnySettingNamed:]_block_invoke
+ ___51+[FBSSettingsExtension extensionForBSObjCProtocol:]_block_invoke_2
+ ___FBSIngestSubclassProperties_block_invoke
+ ___FBSRealizeSceneExtension_block_invoke
+ ___FBSRealizeSettingsExtension_block_invoke
+ ___block_descriptor_32_e8_v16?08l
+ ___block_descriptor_40_e5_v8?0lu32l8
+ ___block_descriptor_40_e8_32s_e21_16?0"FBSSettings"8l
+ ___block_descriptor_40_e8_32s_e21_#16?0"FBSSettings"8l
+ ___block_descriptor_40_e8_32s_e21_:16?0"FBSSettings"8l
+ ___block_descriptor_40_e8_32s_e21_Q16?0"FBSSettings"8l
+ ___block_descriptor_40_e8_32s_e21_d16?0"FBSSettings"8l
+ ___block_descriptor_40_e8_32s_e22_r*16?0"FBSSettings"8l
+ ___block_descriptor_48_e5_v8?0lu32l8u40l8
+ ___block_descriptor_48_e8_32s_e28_{?=[2Q]}16?0"FBSSettings"8l
+ ___block_descriptor_48_e8_32s_e28_{?=[2d]}16?0"FBSSettings"8l
+ ___block_descriptor_48_e8_32s_e28_{?=[4d]}16?0"FBSSettings"8l
+ ___block_descriptor_56_e8_32s40s48r_e11_v24?0Q8Q16l
+ ___ingestPropertiesFromSettingsSubclass_block_invoke.434
+ ___realizeSettingsExtension_block_invoke.253
+ ___realizeSettingsExtension_block_invoke.257
+ ___realizeSettingsExtension_block_invoke.268
+ ___realizeSettingsExtension_block_invoke.276
+ ___realizeSettingsExtension_block_invoke.280
+ ___realizeSettingsExtension_block_invoke.284
+ ___realizeSettingsExtension_block_invoke.297
+ ___realizeSettingsExtension_block_invoke.300
+ ___realizeSettingsExtension_block_invoke.304
+ ___realizeSettingsExtension_block_invoke.308
+ ___realizeSettingsExtension_block_invoke.308.cold.1
+ ___realizeSettingsExtension_block_invoke.308.cold.2
+ ___realizeSettingsExtension_block_invoke.323
+ ___realizeSettingsExtension_block_invoke.327
+ ___realizeSettingsExtension_block_invoke.331
+ ___realizeSettingsExtension_block_invoke.335
+ ___realizeSettingsExtension_block_invoke.339
+ ___realizeSettingsExtension_block_invoke.343
+ __block_literal_global.209
+ __block_literal_global.219
+ __block_literal_global.225
+ __block_literal_global.228
+ _objc_msgSend$identityForIdentifier:
+ _objc_msgSend$instanceMethodForSelector:
+ _objc_msgSend$pseudoTokenWithIdentifier:
+ _objc_msgSend$settingChangedForKey:
+ _objc_msgSend$valueForSetting:
+ sharedInstance.updater
- +[FBSSettingsExtension extensionForBSObjCProtocol:].cold.3
- +[FBSSettingsExtension extensionForBSObjCProtocol:].cold.4
- -[FBSSettings _realValueForSetting:]
- -[FBSSettings _realValueForSetting:].cold.1
- -[FBSSettings _unitTestRealValueForProperty:]
- -[FBSSettings _unitTestRemoveSettingsExtension:]
- -[FBSSettingsDiff _containsSettingNamed:]
- -[FBSSettingsDiff _containsSettingNamed:].cold.1
- GCC_except_table117
- GCC_except_table118
- GCC_except_table118
- GCC_except_table119
- GCC_except_table120
- GCC_except_table120
- GCC_except_table132
- GCC_except_table33
- GCC_except_table50
- GCC_except_table83
- GCC_except_table84
- GCC_except_table85
- GCC_except_table86
- GCC_except_table87
- GCC_except_table88
- _OBJC_$_PROP_LIST_FBSSceneTransitionContext.157
- _OUTLINED_FUNCTION_20
- __51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.193
- __51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.200
- __51-[FBSScene updater:didReceiveActions:forExtension:]_block_invoke.203
- __76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.178
- __76-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:]_block_invoke.182
- ___41-[FBSSettingsDiff _containsSettingNamed:]_block_invoke
- ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_48_e8_32s_e21_#16?0"FBSSettings"8lu40l8
- ___block_descriptor_48_e8_32s_e21_:16?0"FBSSettings"8lu40l8
- ___block_descriptor_48_e8_32s_e21_Q16?0"FBSSettings"8lu40l8
- ___block_descriptor_48_e8_32s_e21_d16?0"FBSSettings"8lu40l8
- ___block_descriptor_48_e8_32s_e22_r*16?0"FBSSettings"8lu40l8
- ___block_descriptor_56_e8_32s_e28_{?=[2Q]}16?0"FBSSettings"8lu40l8
- ___block_descriptor_56_e8_32s_e28_{?=[2d]}16?0"FBSSettings"8lu40l8
- ___block_descriptor_56_e8_32s_e28_{?=[4d]}16?0"FBSSettings"8lu40l8
- ___block_descriptor_57_e8_32s40s_e21_16?0"FBSSettings"8lu48l8
- ___realizeSettingsExtension_block_invoke.259
- ___realizeSettingsExtension_block_invoke.272.cold.1
- ___realizeSettingsExtension_block_invoke.278
- ___realizeSettingsExtension_block_invoke.283
- ___realizeSettingsExtension_block_invoke.288
- ___realizeSettingsExtension_block_invoke.293
- ___realizeSettingsExtension_block_invoke.298
- ___realizeSettingsExtension_block_invoke.312
- ___realizeSettingsExtension_block_invoke.316
- ___realizeSettingsExtension_block_invoke.320
- ___realizeSettingsExtension_block_invoke.324
- ___realizeSettingsExtension_block_invoke.324.cold.1
- ___realizeSettingsExtension_block_invoke.324.cold.2
- ___realizeSettingsExtension_block_invoke.336
- ___realizeSettingsExtension_block_invoke.340
- ___realizeSettingsExtension_block_invoke.344
- ___realizeSettingsExtension_block_invoke.348
- ___realizeSettingsExtension_block_invoke.352
- ___realizeSettingsExtension_block_invoke.356
- __block_literal_global.196
- __block_literal_global.202
- __block_literal_global.205
- _objc_allocateClassPair
- _objc_lookUpClass
- _objc_registerClassPair
CStrings:
+ "%!i(MISSING)/psuedo:%!@(MISSING)"
+ "BOOL FBSSubclassHasBeenIngested(__unsafe_unretained Class _Nonnull)"
+ "FBSPseudoSceneUpdater.m"
+ "PseudoScene:%!@(MISSING)"
+ "it is not (yet) appropriate to call -invalidate: on this scene"
+ "it is not appropriate to call -updateSettings: on this scene"
+ "not supported"
+ "settingName != ((void *)0)"
- "adding +protcol implementation failed"
- "class %!@(MISSING) is not a FBSSettingsExtension"

```
