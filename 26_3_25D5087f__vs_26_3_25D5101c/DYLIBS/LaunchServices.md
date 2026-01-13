## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

```diff

-1444.3.2.0.0
-  __TEXT.__text: 0x23dc88
+1444.3.4.0.0
+  __TEXT.__text: 0x23dd50
   __TEXT.__auth_stubs: 0x3c90
   __TEXT.__objc_methlist: 0xdafc
   __TEXT.__const: 0xa38
-  __TEXT.__cstring: 0x2f377
-  __TEXT.__oslogstring: 0x1efb4
-  __TEXT.__gcc_except_tab: 0x325a4
+  __TEXT.__cstring: 0x2f384
+  __TEXT.__oslogstring: 0x1efb7
+  __TEXT.__gcc_except_tab: 0x325d8
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
-  __TEXT.__unwind_info: 0xd028
+  __TEXT.__unwind_info: 0xd020
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x1f89
   __TEXT.__objc_methname: 0x1ed45

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 9437EDEE-7C07-3D4A-803D-ED0E5939EC5C
+  UUID: 3CF12EA3-9138-3944-B12E-957D098A3F73
   Functions: 10262
-  Symbols:   22662
+  Symbols:   22661
   CStrings:  16683
 
Symbols:
+ __ZL17_LSPutAnnotationsPK6AEDescPK13audit_token_tPS_PU15__autoreleasingP7NSError
+ __ZL20_LSCreateAnnotationsPK9AEKeyDescPK26LSApplicationParameters_V1PK13audit_token_tP6AEDescPU15__autoreleasingP7NSError
+ __ZL39init_AEGenerateAnnotationsForAuditTokenPK6AEDescPK13audit_token_tbPS_
+ __ZL43softLink_AEGenerateAnnotationsForAuditToken
- __ZL17_LSPutAnnotationsPK6AEDescPS_PU15__autoreleasingP7NSError
- __ZL20_LSCreateAnnotationsPK9AEKeyDescPK26LSApplicationParameters_V1P6AEDescPU15__autoreleasingP7NSError
- __ZL26init_AEGenerateAnnotationsPK6AEDescPS_
- __ZL30softLink_AEGenerateAnnotations
Functions:
~ __LSAliasCompareToNode : 1208 -> 1352
~ -[_LSDReadClient _getRedactedPluginProxy:appexRecord:UUID:node:bundleIdentifier:platform:error:] : 864 -> 872
~ __LSOpenStuffWithPreSanitizedURLs : 3368 -> 3392
~ __ZL20_LSCreateAnnotationsPK9AEKeyDescPK26LSApplicationParameters_V1P6AEDescPU15__autoreleasingP7NSError -> __ZL20_LSCreateAnnotationsPK9AEKeyDescPK26LSApplicationParameters_V1PK13audit_token_tP6AEDescPU15__autoreleasingP7NSError : 576 -> 588
~ __LSHandlePasteboardItems : 5552 -> 5564
~ __ZL21_LSCreateURLOpenEventPK7__CFURLPK19ProcessSerialNumberP11LSOpenStatePU15__autoreleasingP7NSError : 1160 -> 1184
~ __ZL26init_AEGenerateAnnotationsPK6AEDescPS_ -> __ZL39init_AEGenerateAnnotationsForAuditTokenPK6AEDescPK13audit_token_tbPS_ : 148 -> 176
~ __ZL17_LSPutAnnotationsPK6AEDescPS_PU15__autoreleasingP7NSError -> __ZL17_LSPutAnnotationsPK6AEDescPK13audit_token_tPS_PU15__autoreleasingP7NSError : 524 -> 528
~ _LSAliasCompareToNode.cold.1 : 164 -> 108
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSUtils.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSAESupport.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSUtils.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSValidationToken.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSAlias.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/DefaultApps/LSDefaultAppsCore.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCapability.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSClaimedTypes.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSDataContainerPersonality.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSEligibility.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternal.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternalPriv.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSInternetLocator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSOpenWithMenu.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistrants.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistration.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSURLPropertyProvider.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSLaunchRunningBoard.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCall.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCore.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenGenericReadMe.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenNewWorld.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSTranslocation.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSApplicationRecordEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSServiceEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationExtensionRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSBundleRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSDatabaseContext.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSExtensionPointRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSServiceRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/UTTypeRecord.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/RunIdentity/LSApplicationIdentity.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/CodeEvaluation/LSCodeEvaluationClientManager.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSDTrustedSignatureService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignature.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignatureDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDeviceEncryptionService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDisseminationClient.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDXPCClient.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSServerInterface.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLinkPlugIn.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationRestrictionsManager.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleProxy.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDefaultApplicationQuery.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDiskUsage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQuery.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithURL.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQuery.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSStatePlist.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSTranslocationHelpers.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/NSCoder+LaunchServicesAdditions.m"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
+ "/AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
+ "_AEGenerateAnnotationsForAuditToken"
+ "failed to get a property necessary to compare an alias to a node: %@ %d"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1428:63)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1459:65)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1466:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1459:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1466:65)]"
+ "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /AppleInternal/Library/BuildRoots/4~CE8IugB3snkdL4IxWzOYJzWAK_SwqbGAfAwLiL0/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSUtils.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSAESupport.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSUtils.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSValidationToken.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSAlias.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/DefaultApps/LSDefaultAppsCore.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCapability.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSClaimedTypes.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSDataContainerPersonality.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSEligibility.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternal.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternalPriv.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSInternetLocator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSOpenWithMenu.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistrants.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistration.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSURLPropertyProvider.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSLaunchRunningBoard.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCall.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCore.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenGenericReadMe.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenNewWorld.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSTranslocation.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSApplicationRecordEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSServiceEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationExtensionRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSBundleRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSDatabaseContext.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSExtensionPointRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSServiceRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/UTTypeRecord.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/RunIdentity/LSApplicationIdentity.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/CodeEvaluation/LSCodeEvaluationClientManager.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSDTrustedSignatureService.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignature.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignatureDatabase.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDeviceEncryptionService.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDisseminationClient.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDService.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDXPCClient.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSServerInterface.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLinkPlugIn.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationRestrictionsManager.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleProxy.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleWrapper.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDefaultApplicationQuery.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDiskUsage.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQuery.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithURL.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQuery.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSStatePlist.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSTranslocationHelpers.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/NSCoder+LaunchServicesAdditions.m"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
- "/AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
- "_AEGenerateAnnotations"
- "failed to get a property necessary to compare an alias to a node: %@"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1428:63)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1459:65)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1466:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1459:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1466:65)]"
- "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /AppleInternal/Library/BuildRoots/4~CDylugCCXR3U13OIm8x50nDhJjU5helmnmqQ6rQ/Library/Caches/com.apple.xbs/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"

```
