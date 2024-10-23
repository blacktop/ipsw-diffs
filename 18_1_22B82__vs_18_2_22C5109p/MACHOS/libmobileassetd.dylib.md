## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.42.5.0.0
-  __TEXT.__text: 0x261abc
-  __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_stubs: 0x1fa20
-  __TEXT.__objc_methlist: 0xefa0
+1329.60.89.502.4
+  __TEXT.__text: 0x26333c
+  __TEXT.__auth_stubs: 0x2390
+  __TEXT.__objc_stubs: 0x1fbe0
+  __TEXT.__objc_methlist: 0xeff8
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x37303
-  __TEXT.__cstring: 0x4c76c
+  __TEXT.__objc_methname: 0x374ca
+  __TEXT.__cstring: 0x4ceac
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x3562
+  __TEXT.__objc_methtype: 0x357c
   __TEXT.__oslogstring: 0x310d5
-  __TEXT.__gcc_except_tab: 0x2544
+  __TEXT.__gcc_except_tab: 0x2558
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__constg_swiftt: 0x1530

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x4740
+  __TEXT.__unwind_info: 0x4750
   __TEXT.__eh_frame: 0x30c4
-  __DATA_CONST.__auth_got: 0x11c8
+  __DATA_CONST.__auth_got: 0x11d8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x66b8
-  __DATA_CONST.__cfstring: 0x315a0
+  __DATA_CONST.__const: 0x6700
+  __DATA_CONST.__cfstring: 0x319c0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b30
+  __DATA_CONST.__objc_selrefs: 0x8ba0
   __DATA_CONST.__objc_intobj: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x940
-  __DATA_CONST.__objc_arrayobj: 0x1b0
+  __DATA_CONST.__objc_arraydata: 0x998
+  __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x14528
-  __DATA.__objc_classrefs: 0x7a0
+  __DATA.__objc_const: 0x14558
+  __DATA.__objc_classrefs: 0x7a8
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x1280
+  __DATA.__objc_ivar: 0x1284
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
-  __DATA.__bss: 0x53a0
+  __DATA.__bss: 0x53c0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x1978
   __DATA_DIRTY.__bss: 0x340

   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8278
-  Symbols:   14855
-  CStrings:  15760
+  Functions: 8290
+  Symbols:   14891
+  CStrings:  15821
 
Symbols:
+ +[SecureMobileAssetBundle _shouldUseConclave:]
+ +[SecureMobileAssetBundle commitStagedManifestsForSelectors:darwinOnly:error:]
+ +[SecureMobileAssetBundle getExclaveManager:]
+ -[SecureMobileAssetBundle darwinOnly]
+ -[SecureMobileAssetBundle integrityCatalogPath]
+ -[SecureMobileAssetBundle isMappableToExclaves:]
+ -[SecureMobileAssetBundle isPersonalizedForExclaves:staged:]
+ -[SecureMobileAssetBundle setDarwinOnly:]
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table85
+ MABrainUtilityConclaveEnabled.answer
+ MABrainUtilityConclaveEnabled.onceToken
+ MABrainUtilityDeviceSupportsExclaves.answer
+ MABrainUtilityDeviceSupportsExclaves.onceToken
+ OBJC_IVAR_$_SecureMobileAssetBundle._darwinOnly
+ _AMAuthInstallSetUUID
+ _MABrainUtilityConclaveEnabled
+ _MABrainUtilityDeviceSupportsExclaves
+ _MGIsQuestionValid
+ _OBJC_CLASS_$_SecureMobileAssetExclaveManager
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1034
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1081
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1130
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1130.cold.1
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1137
+ ___MABrainUtilityConclaveEnabled_block_invoke
+ ___MABrainUtilityDeviceSupportsExclaves_block_invoke
+ __block_literal_global.1031
+ __block_literal_global.1033
+ __block_literal_global.1766
+ __block_literal_global.3365
+ __block_literal_global.363
+ _objc_msgSend$_shouldUseConclave:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:
+ _objc_msgSend$commitStagedManifestForFSTags:error:
+ _objc_msgSend$commitStagedManifestsForSelectors:darwinOnly:error:
+ _objc_msgSend$darwinOnly
+ _objc_msgSend$getExclaveManager:
+ _objc_msgSend$integrityCatalogPath
+ _objc_msgSend$isMappableToExclaves:
+ _objc_msgSend$isPersonalizedForExclaves:staged:
+ _objc_msgSend$proposeNonce:
+ _objc_msgSend$setDarwinOnly:
+ _objc_msgSend$stageManifest:infoPlist:catalog:error:
+ _objc_msgSend$storeManifest:infoPlist:catalog:error:
- GCC_except_table40
- GCC_except_table52
- GCC_except_table65
- GCC_except_table77
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1010
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1057
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1106
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1106.cold.1
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1113
- __block_literal_global.1007
- __block_literal_global.1009
- __block_literal_global.1158
- __block_literal_global.1680
- __block_literal_global.3357
CStrings:
+ "+[SecureMobileAssetBundle _shouldUseConclave:]"
+ "+[SecureMobileAssetBundle commitStagedManifestsForSelectors:darwinOnly:error:]"
+ "+[SecureMobileAssetBundle getExclaveManager:]"
+ "-[SecureMobileAssetBundle isMappableToExclaves:]"
+ "-[SecureMobileAssetBundle isPersonalizedForExclaves:staged:]"
+ "Allow listed for Exclaves: %!@(MISSING):%!@(MISSING) fstag=%!u(MISSING)"
+ "B24@0:8I16B20"
+ "B24@0:8^I16"
+ "Committing staged exclave manifests for fsTags: %!@(MISSING)"
+ "CrystalSeedUpdate"
+ "DOES NOT have"
+ "DOES have"
+ "ExclaveCapability"
+ "Failed to allocate NSNumber for fstag"
+ "Failed to allocate NSNumber for fstag=%!d(MISSING)"
+ "Failed to commit staged manifests to Exclaves"
+ "Failed to get exclave nonces"
+ "Failed to get nonce dictionary from SecureMobileAssetExclave: %!@(MISSING)"
+ "Failed to get shared instance of SecureMobileAssetExclave"
+ "Failed to get shared instance of SecureMobileAssetExclave: %!@(MISSING)"
+ "Generating nonce proposal for exclaves"
+ "MobileAsset"
+ "Not allow listed for Exclaves: %!@(MISSING):%!@(MISSING)"
+ "Operations will be restricted to darwin only"
+ "SECUREMABUNDLE_COMMAND_IS_PERSONALIZED"
+ "Secure MobleAsset bundle %!@(MISSING) %!s(MISSING) a %!s(MISSING) personalized manifest."
+ "SecureMobileAssetBundleOptionDarwinOnly"
+ "Starting built-in MobileAsset brain built Oct 20 2024 22:11:52"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct 20 2024 22:11:52"
+ "TB,N,V_darwinOnly"
+ "Unable to get SecureMobileAssetExclave instance in this environment"
+ "Warning: MAExclaveManifestStorageService does not support staging, commit is a no-op"
+ "Warning: MAExclaveManifestStorageService does not support staging, storing manifest instead"
+ "_darwinOnly"
+ "_shouldUseConclave:"
+ "arrayByAddingObjectsFromArray:"
+ "checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:"
+ "com.apple.MobileAsset.SecureAssetManager01.Test"
+ "com.apple.MobileAsset.UAF.FM.CodeLM"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.Photos.MagicCleanup"
+ "com.apple.MobileAsset.UAF.Search.ODLA"
+ "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
+ "com.apple.MobileAsset.UAF.VoiceAssistant"
+ "com_apple_mobileassetd_conclave"
+ "commitStagedManifestForFSTags:error:"
+ "commitStagedManifestsForSelectors:darwinOnly:error:"
+ "committed"
+ "darwinOnly"
+ "digestNonce"
+ "failed to get integrity catalog path"
+ "failed to read cryptex integrity catalog"
+ "failed to stage manifest in Exclave Secure Storage"
+ "failed to store manifest in Exclave Secure Storage"
+ "getExclaveManager:"
+ "integrityCatalogPath"
+ "isMappableToExclaves:"
+ "isPersonalizedForExclaves:staged:"
+ "proposeNonce:"
+ "rawNonce"
+ "setDarwinOnly:"
+ "stageManifest:infoPlist:catalog:error:"
+ "storeManifest:infoPlist:catalog:error:"
- "+[SecureMobileAssetBundle commitStagedManifestsForSelectors:error:]"
- "CrystalB"
- "Starting built-in MobileAsset brain built Oct 15 2024 22:29:25"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct 15 2024 22:29:25"

```
