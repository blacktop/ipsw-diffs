## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_LSFSNode`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1507.0.0.0.0
-  __TEXT.__text: 0x2520f8
+1510.400.0.0.0
+  __TEXT.__text: 0x252f9c
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xeda4
-  __TEXT.__const: 0xac0
-  __TEXT.__cstring: 0x33372
-  __TEXT.__oslogstring: 0x220fd
-  __TEXT.__gcc_except_tab: 0x342f8
+  __TEXT.__objc_methlist: 0xedbc
+  __TEXT.__const: 0xab0
+  __TEXT.__cstring: 0x33486
+  __TEXT.__oslogstring: 0x222b0
+  __TEXT.__gcc_except_tab: 0x3444c
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
-  __TEXT.__unwind_info: 0xeac8
+  __TEXT.__unwind_info: 0xeaf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3e80
+  __DATA_CONST.__const: 0x3e98
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e68
+  __DATA_CONST.__objc_selrefs: 0x6e60
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x638
   __DATA_CONST.__objc_arraydata: 0xa10
   __DATA_CONST.__got: 0xe40
-  __AUTH_CONST.__const: 0xaa38
-  __AUTH_CONST.__cfstring: 0x1dea0
-  __AUTH_CONST.__objc_const: 0x16658
+  __AUTH_CONST.__const: 0xaaa8
+  __AUTH_CONST.__cfstring: 0x1df00
+  __AUTH_CONST.__objc_const: 0x16668
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1ee0
+  __AUTH_CONST.__auth_got: 0x1ec8
   __AUTH.__objc_data: 0x3b60
   __AUTH.__data: 0x248
   __DATA.__objc_ivar: 0xc68
-  __DATA.__data: 0x15f4
-  __DATA.__bss: 0x1a78
+  __DATA.__data: 0x15ec
+  __DATA.__bss: 0x1a70
   __DATA.__common: 0x5
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x250

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 11138
-  Symbols:   19516
-  CStrings:  7896
+  Functions: 11147
+  Symbols:   19519
+  CStrings:  7906
 
Symbols:
+ -[LSApplicationRecord(MobileInstall) installBuildVersion]
+ -[_LSStackBacktrace replacementObjectForCoder:]
+ GCC_except_table300
+ GCC_except_table317
+ GCC_except_table322
+ GCC_except_table325
+ GCC_except_table334
+ GCC_except_table337
+ _OBJC_CLASS_$_NSXPCCoder
+ __LSIsApplicationRunningOrExited
+ ___LSGetMainBundleURL_block_invoke
+ ___ZL21computeBestSliceRangeiP7NSArrayIP11LSSliceInfoExRxS4_RPKc_block_invoke
+ ____ZL21computeBestSliceRangeiP7NSArrayIP11LSSliceInfoExRxS4_RPKc_block_invoke
+ ___block_descriptor_41_ea8_32s_e35_v32?0"NSString"8"NSString"16^B24l
+ ___block_descriptor_72_ea8_32r40r48r56r64r_e36_v32?0r^{mach_header=IiiIIII}8Q16Q24l
+ ___block_descriptor_80_ea8_32r40r48r56r64r_e40_v40?0r^{mach_header=IiiIIII}8Q16Q24^B32l
+ __kLSApplicationAllowedToRunWithoutUIEntitlement
+ __kLSClientAllowedToBeQuitReallyHandler
+ __kLSClientAllowedToForciblyRemoveApplication
+ _copyProcessNameString
+ _macho_best_slice_in_fd
+ _macho_for_each_slice_in_fd
+ _proc_name
+ _processNameString
- GCC_except_table299
- GCC_except_table316
- GCC_except_table319
- GCC_except_table323
- GCC_except_table331
- GCC_except_table335
- GCC_except_table350
- _CFStringConvertEncodingToNSStringEncoding
- _CFStringConvertIANACharSetNameToEncoding
- _NSStringEncodingDetectionAllowLossyKey
- __NSGetEnviron
- __ZZL24encodingFromLocaleSimplevE15sLocaleEncoding
- __ZZL24encodingFromLocaleSimplevE5sOnce
- ____ZL24encodingFromLocaleSimplev_block_invoke
- _environmentStringInReasonableEncoding
- _nl_langinfo
- _objc_msgSend$defaultCStringEncoding
- _objc_msgSend$stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:
- _setlocale
- _strchr
- environmentStringInReasonableEncoding
CStrings:
+ "### ERROR, process %{public}d/%{public}@ attempted to use kLSClientAllowedToCreateOrUpdateTemplateApplicationsEntitlement but wasn't properly entitled."
+ "%s: Success canonicalizing %@ produced no result."
+ "%s: could not canonicalize %@: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSAESupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSValidationToken.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSAlias.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/DefaultApps/LSDefaultAppsCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCapability.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSClaimedTypes.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSDataContainerPersonality.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSEligibility.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternal.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternalPriv.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSInternetLocator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSOpenWithMenu.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistrants.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistration.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSURLPropertyProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSLaunchRunningBoard.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCall.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenGenericReadMe.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenNewWorld.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSTranslocation.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSApplicationRecordEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSServiceEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationExtensionRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSBundleRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSDatabaseContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSExtensionPointRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSServiceRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/UTTypeRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/RunIdentity/LSApplicationIdentity.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/CodeEvaluation/LSCodeEvaluationClientManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSDTrustedSignatureService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignature.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignatureDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDeviceEncryptionService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDisseminationClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDXPCClient.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSServerInterface.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLinkPlugIn.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationRestrictionsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleProxy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSContainerHelpers.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDefaultApplicationQuery.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDiskUsage.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfigurationResolver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPersonaAssociationMutation.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQuery.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithURL.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQuery.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSStatePlist.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSTranslocationHelpers.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/NSCoder+LaunchServicesAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
+ "Could not create bundle node from %@: %@"
+ "Couldn't construct relative path for executable: %@ %@ %@ %@"
+ "ERROR: Prohibiting application pid=%{public}ld/%{public}@ from creating or updating template application; likely missing %@ entitlement."
+ "Interruption on client connection %{public}p, pid=%{public}d/%{public}@, so invalidating connection."
+ "Invalidation on client connection %{public}p, pid=%{public}d/%{public}@, so invalidating connection."
+ "LAUNCH: Application 0x%{public}x-0x%{public}x %{public}@ launched with pid %{public}d/%{public}@, starting the application."
+ "LAUNCH: Application 0x%{public}x-0x%{public}x %{public}@ launched with pid %{public}d/%{public}@, was a beta app; sending ping to CSUIA."
+ "LAUNCH: Calling process %{public}d/%{public}@ does not have access to %{private}s so not passing an extension over to CSUI, err=%{public}d/%{public}d."
+ "LAUNCH: Cancelling launch source for pid %{public}d/%{public}@."
+ "LAUNCH: Client %{public}d/%{public}@ does not have the appropriate entitlement to override an audit token."
+ "LAUNCH: Error %{public}@ during relaunch after launchedPid %{public}d/%{public}@ death of %{public}@"
+ "LAUNCH: Launched translocated app 0x%{public}x-0x%{public}x %{public}@/%{private}@, so checking it in with pid %{public}d/%{public}@."
+ "LAUNCH: Pid %{public}d/%{public}@ has exited, so going forward with their deferred app launch now."
+ "LAUNCH: _AppleEventsHintApp* failed, 0x%{public}x-0x%{public}x app=%{public}@ pid=%{public}d/%{public}@"
+ "LAUNCH: macho_best_slice_in_fd failed for fd=%{public}d, errno=%{public}d (%{public}s)"
+ "LAUNCH: macho_for_each_slice_in_fd failed for fd=%{public}d, errno=%{public}d (%{public}s)"
+ "Overriding teamidentifier %{public}@ to %{public}@ from options because caller %{public}d/%{public}@ has appropriate entitlement."
+ "QUARANTINE: Resolving all quarantine items, caller=%{public}d/%{public}@ items=%{private}@ options=%{public}@"
+ "Setting senderAuditTokenAttr to pid=%{public}d/%{public}@ since launcher is CSUI and a launcherAuditToken was provided."
+ "Stopping lsd %{public}d/%{public}@ uid %{public}d on request; letting databases complete in-flight operations."
+ "Unable to create sandbox extension for process %{public}d/%{public}@ from path %{private}@"
+ "_LSGetMainBundleURL_block_invoke"
+ "_LSIsApplicationRunningOrExited"
+ "_LSTemplateApplicationCallInvokeWithXPC( conn=%{public}@, message=%{public}@ caller=%{public}d/%{public}@)"
+ "com.apple.private.canrunwithoutvisibleui"
+ "com.apple.private.launchservices.allowedtoforciblyremoveapplicationfromrunninglist"
+ "com.apple.private.launchservices.quithandler"
+ "createTemplateActionsManagerListeningConnection, tokenPid=%{public}d/%{public}@"
+ "initWithURL:%{private}@ options=%{public}@ creatorPid=%{public}d/%{public}@"
+ "platform default"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1498:63)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
+ "teamIdentifier for %{public}d/%{public}@ = %{public}@"
+ "v32@?0r^{mach_header=IiiIIII}8Q16Q24"
+ "v40@?0r^{mach_header=IiiIIII}8Q16Q24^B32"
+ "vendor (prioritized)"
+ "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.irL9K9/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
- "### ERROR, process %{public}d attempted to use kLSClientAllowedToCreateOrUpdateTemplateApplicationsEntitlement but wasn't properly entitled."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSAESupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSValidationToken.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSAlias.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/DefaultApps/LSDefaultAppsCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCapability.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSClaimedTypes.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSDataContainerPersonality.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSEligibility.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternal.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternalPriv.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSInternetLocator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSOpenWithMenu.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistrants.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistration.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSURLPropertyProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSLaunchRunningBoard.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCall.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenGenericReadMe.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenNewWorld.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSTranslocation.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSApplicationRecordEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSServiceEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationExtensionRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSBundleRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSDatabaseContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSExtensionPointRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSServiceRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/UTTypeRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/RunIdentity/LSApplicationIdentity.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/CodeEvaluation/LSCodeEvaluationClientManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSDTrustedSignatureService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignature.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignatureDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDeviceEncryptionService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDisseminationClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDXPCClient.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSServerInterface.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLinkPlugIn.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationRestrictionsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleProxy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleWrapper.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSContainerHelpers.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDefaultApplicationQuery.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDiskUsage.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfiguration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfigurationResolver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPersonaAssociationMutation.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQuery.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithURL.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQuery.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSStatePlist.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSTranslocationHelpers.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/NSCoder+LaunchServicesAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
- "Apple default"
- "ERROR: Prohibiting application pid=%{public}ld from creating or updating template application; likely missing %@ entitlement."
- "Interruption on client connection %{public}p, pid=%{public}d, so invalidating connection."
- "Invalidation on client connection %{public}p, pid=%{public}d, so invalidating connection."
- "LAUNCH: Application 0x%{public}x-0x%{public}x %{public}@ launched with pid %{public}d, starting the application."
- "LAUNCH: Application 0x%{public}x-0x%{public}x %{public}@ launched with pid %{public}d, was a beta app; sending ping to CSUIA."
- "LAUNCH: Calling process %{public}d does not have access to %{private}s so not passing an extension over to CSUI, err=%{public}d/%{public}d."
- "LAUNCH: Cancelling launch source for pid %{public}d."
- "LAUNCH: Client %{public}d does not have the appropriate entitlement to override an audit token."
- "LAUNCH: Error %{public}@ during relaunch after launchedPid %{public}d death of %{public}@"
- "LAUNCH: Launched translocated app 0x%{public}x-0x%{public}x %{public}@/%{private}@, so checking it in with pid %{public}d."
- "LAUNCH: Pid %{public}d has exited, so going forward with their deferred app launch now."
- "LAUNCH: _AppleEventsHintApp* failed, 0x%{public}x-0x%{public}x app=%{public}@ pid=%{public}d"
- "OPEN: Could not create environment variable from string %{public}s"
- "Overriding teamidentifier %{public}@ to %{public}@ from options because caller %{public}d has appropriate entitlement."
- "QUARANTINE: Resolving all quarantine items, caller=%{public}d items=%{private}@ options=%{public}@"
- "Setting senderAuditTokenAttr to pid=%{public}d since launcher is CSUI and a launcherAuditToken was provided."
- "Stopping lsd %{public}d uid %{public}d on request; letting databases complete in-flight operations."
- "Unable to create sandbox extension for process %{public}d from path %{private}@"
- "_LSIsApplicationRunning"
- "_LSTemplateApplicationCallInvokeWithXPC( conn=%{public}@, message=%{public}@ caller=%{public}d)"
- "createTemplateActionsManagerListeningConnection, tokenPid=%{public}d"
- "encodingFromLocaleSimple(), encoding=%{public}ld locale=%{public}s encodingStr=%{public}@ / %{public}ld"
- "initWithURL:%{private}@ options=%{public}@ creatorPid=%{public}d"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1498:63)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
- "teamIdentifier for %{public}d = %{public}@"
- "vendor (prioritized is-Apple check)"
- "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
```
