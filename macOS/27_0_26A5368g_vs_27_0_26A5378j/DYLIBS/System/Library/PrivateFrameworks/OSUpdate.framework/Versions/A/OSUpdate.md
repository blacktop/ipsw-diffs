## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

```diff

-  __TEXT.__text: 0x9190c
-  __TEXT.__objc_methlist: 0x7af4
+  __TEXT.__text: 0x91e24
+  __TEXT.__objc_methlist: 0x7b2c
   __TEXT.__const: 0x1f1
-  __TEXT.__cstring: 0x80ab
-  __TEXT.__oslogstring: 0xd725
-  __TEXT.__gcc_except_tab: 0x1b1c
+  __TEXT.__cstring: 0x80ff
+  __TEXT.__oslogstring: 0xd74e
+  __TEXT.__gcc_except_tab: 0x1b54
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1fe0
+  __TEXT.__unwind_info: 0x2008
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd58
+  __DATA_CONST.__const: 0xd68
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ab0
+  __DATA_CONST.__objc_selrefs: 0x4b08
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x6f8
   __DATA_CONST.__got: 0xa50
   __AUTH_CONST.__const: 0x2d00
-  __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x9f70
+  __AUTH_CONST.__cfstring: 0x6100
+  __AUTH_CONST.__objc_const: 0xa000
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_got: 0x5e0
   __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x774
+  __DATA.__objc_ivar: 0x780
   __DATA.__data: 0x612
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3331
-  Symbols:   7775
-  CStrings:  2988
+  Functions: 3342
+  Symbols:   7803
+  CStrings:  2998
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[SUOSUCatalogManager .cxx_destruct]
+ -[SUOSUCatalogManager _resetCatalogToProduction]
+ -[SUOSUCatalogManager _updateCatalogWithServer:]
+ -[SUOSUCatalogManager init]
+ -[SUOSUCatalogManager queue]
+ -[SUOSUCatalogManager resetCatalogToProduction]
+ -[SUOSUCatalogManager setQueue:]
+ -[SUOSUCatalogManager updateCatalogWithServer:]
+ -[SUOSUCatalogManager updateEnrollmentIfNecessaryWithServer:]
+ -[SUOSUCatalogServer mobileAssetSigningServerURL]
+ -[SUOSUCatalogServer setMobileAssetSigningServerURL:]
+ -[SUOSUCatalogServer setSigningServerURL:]
+ -[SUOSUCatalogServer signingServerURL]
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table130
+ GCC_except_table139
+ GCC_except_table148
+ GCC_except_table157
+ GCC_except_table181
+ GCC_except_table207
+ OBJC_IVAR_$_SUOSUCatalogManager._queue
+ OBJC_IVAR_$_SUOSUCatalogServer._mobileAssetSigningServerURL
+ OBJC_IVAR_$_SUOSUCatalogServer._signingServerURL
+ _OBJC_CLASS_$_ECODeprecationWarningClient
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_36
+ _SUOSUAudienceDictionaryMobileAssetSigningServerURLKey
+ _SUOSUAudienceDictionarySigningServerURLKey
+ __61-[SUOSUCatalogManager updateEnrollmentIfNecessaryWithServer:]_block_invoke
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUCatalogManager
+ __OBJC_$_PROP_LIST_SUOSUCatalogManager
+ ___47-[SUOSUCatalogManager resetCatalogToProduction]_block_invoke
+ ___47-[SUOSUCatalogManager updateCatalogWithServer:]_block_invoke
+ ___61-[SUOSUCatalogManager updateEnrollmentIfNecessaryWithServer:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r
+ _objc_msgSend$_resetCatalogToProduction
+ _objc_msgSend$_updateCatalogWithServer:
+ _objc_msgSend$lastLivabilityEnrollmentDate
+ _objc_msgSend$mobileAssetSigningServerURL
+ _objc_msgSend$personalizationServerURL
+ _objc_msgSend$queue
+ _objc_msgSend$setLastLivabilityEnrollmentDate
+ _objc_msgSend$setMobileAssetPersonalizationServerURL:
+ _objc_msgSend$setPersonalizationServerURL:
+ _objc_msgSend$signingServerURL
- -[SUOSUCatalogManager updateCatalogWithServer:completion:]
- -[SUOSUCatalogManager updateCatalogWithServer:withError:]
- -[SUOSUClient resetToProductionCatalogWithCompletion:]
- -[SUOSUClient resetToProductionCatalog]
- -[SUOSUShimController _showLicenseAgreementsForUpdates:skipSLA:]
- -[SUOSUShimController resetToProductionCatalogWithCompletion:]
- -[SUOSUShimController resetToProductionCatalog]
- GCC_except_table125
- GCC_except_table133
- GCC_except_table135
- GCC_except_table142
- GCC_except_table152
- GCC_except_table161
- GCC_except_table185
- GCC_except_table211
- _OBJC_CLASS_$_DeprecationWarningClient
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_35
- __62-[SUOSUShimController resetToProductionCatalogWithCompletion:]_block_invoke
- ___58-[SUOSUCatalogManager updateCatalogWithServer:completion:]_block_invoke
- ___62-[SUOSUShimController resetToProductionCatalogWithCompletion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e8_v12?0B8l
- _objc_msgSend$_showLicenseAgreementsForUpdates:skipSLA:
- _objc_msgSend$licenseAgreementText
- _objc_msgSend$resetToProductionCatalog
- _objc_msgSend$resetToProductionCatalogWithCompletion:
- _objc_msgSend$updateCatalogWithServer:withError:
CStrings:
+ "%@: Clear external updates"
+ "%@: Enrolling in livability audience: %@"
+ "%@: Failed to clear Pallas URL: %lld"
+ "%@: Failed to clear Pallas audience: %lld"
+ "%@: Failed to set Pallas URL: %lld"
+ "%@: Failed to set Pallas audience: %lld"
+ "%@: No Pallas audience specified for %@"
+ "%@: No catalog URL specified, clear IASUCatalogURL"
+ "%@: Pallas audience already set to %@"
+ "%@: Re-enrolling in livability audience: %@ (last enrolled = %@)"
+ "%@: Resetting audience and catalog settings to production"
+ "%@: Set IASUCatalogURL: %@"
+ "%@: Set Pallas URL = %@"
+ "%@: Set Pallas audience = %@"
+ "%@: Skip re-enrolling in livability audience (last enrolled = %@)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "com.apple.OSUpdate.SUOSUCatalogManager"
+ "mobileAssetSigningServerURL"
+ "signingServerURL"
- "%@: Failed to set background catalog URL"
- "%@: Found background catalog URL to set: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "Controller: Failed to reset to Production catalog as preferenceManager failed to reset."
- "Controller: Failed to unenrollFromSeedProgram because authorization failed."
- "SUPrefPane: CatalogConfiguration resetting Pallas exited with %lli"
- "SUPrefPaneController: Failed to reset to Production catalog as preferenceManager failed to reset."
- "SUPrefPaneController: Failed to unenrollFromSeedProgram because authorization failed."
- "Setting catalog to: %@"
- "Skipping showing the SLA"
- "Updating Pallas audience to %@"

```
