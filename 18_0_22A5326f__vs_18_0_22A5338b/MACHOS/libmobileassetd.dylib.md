## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.0.26.502.2
-  __TEXT.__text: 0x257908
+1309.2.2.0.0
+  __TEXT.__text: 0x25809c
   __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_stubs: 0x1f3a0
-  __TEXT.__objc_methlist: 0xec40
+  __TEXT.__objc_stubs: 0x1f460
+  __TEXT.__objc_methlist: 0xecc0
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x35ccd
-  __TEXT.__cstring: 0x4ba7c
+  __TEXT.__objc_methname: 0x35f0e
+  __TEXT.__cstring: 0x4bb6c
   __TEXT.__objc_classname: 0xd7b
   __TEXT.__objc_methtype: 0x3360
-  __TEXT.__oslogstring: 0x2f6fe
+  __TEXT.__oslogstring: 0x2f80c
   __TEXT.__gcc_except_tab: 0x250c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4

   __DATA_CONST.__auth_got: 0x11e0
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x65a0
-  __DATA_CONST.__cfstring: 0x30d60
+  __DATA_CONST.__const: 0x65b0
+  __DATA_CONST.__cfstring: 0x30dc0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8968
+  __DATA_CONST.__objc_selrefs: 0x89a8
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x918
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x141f8
+  __DATA.__objc_const: 0x14288
   __DATA.__objc_classrefs: 0x7a0
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x123c
+  __DATA.__objc_ivar: 0x1248
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
   __DATA.__bss: 0x53a0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8188
-  Symbols:   14684
-  CStrings:  15547
+  Functions: 8198
+  Symbols:   14705
+  CStrings:  15566
 
Symbols:
+ +[MADAutoAssetControlManager preferenceStagerDeterminePallasResponseFewer]
+ +[MADAutoAssetControlManager preferenceStagerDownloadFirstNotInCatalog]
+ -[MADAutoAssetControlManager preferenceStagerDeterminePallasResponseFewer]
+ -[MADAutoAssetControlManager preferenceStagerDownloadFirstNotInCatalog]
+ -[MADAutoAssetControlManager setPreferenceStagerDeterminePallasResponseFewer:]
+ -[MADAutoAssetControlManager setPreferenceStagerDownloadFirstNotInCatalog:]
+ -[MADAutoAssetStager _adjustPallasResponseBasedOnPreferences:]
+ -[MADAutoAssetStager _adjustPallasResponseBasedOnPreferences:].cold.1
+ -[MADAutoAssetStager firstDownloadedAsIfNotInCatalog]
+ -[MADAutoAssetStager setFirstDownloadedAsIfNotInCatalog:]
+ -[MADAutoTargetLookupResults lookupResultsAssetCount]
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerDeterminePallasResponseFewer
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerDownloadFirstNotInCatalog
+ OBJC_IVAR_$_MADAutoAssetStager._firstDownloadedAsIfNotInCatalog
+ __block_literal_global.1136
+ __block_literal_global.1156
+ __block_literal_global.1161
+ __block_literal_global.1163
+ _kMobileAssetPreferencesAutoAssetStagerDeterminePallasResponseFewer
+ _kMobileAssetPreferencesAutoAssetStagerDownloadFirstNotInCatalog
+ _objc_msgSend$_adjustPallasResponseBasedOnPreferences:
+ _objc_msgSend$firstDownloadedAsIfNotInCatalog
+ _objc_msgSend$lookupResultsAssetCount
+ _objc_msgSend$preferenceStagerDeterminePallasResponseFewer
+ _objc_msgSend$preferenceStagerDownloadFirstNotInCatalog
+ _objc_msgSend$setFirstDownloadedAsIfNotInCatalog:
- -[MADAutoAssetStager action_NextAwaitingBeginDownload:error:].cold.1
- __block_literal_global.1130
- __block_literal_global.1150
- __block_literal_global.1155
- __block_literal_global.1157
CStrings:
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} unable to self-heal, clearing latest-to-vend | setConfiguration:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | latest-to-vend includes personalized-not-grafted|mounted (acceptable since not currently locked) | downloadedSelector:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | personalization required after startup secure-healing | downloadedSelector:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | unable to re-graft during startup secure-healing | downloadedSelector:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {_adjustPallasResponseBasedOnPreferences} key value is not an array | setCatalogKey:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {_adjustPallasResponseBasedOnPreferences} unable to determine key/value from set-catalog | setCatalogKey:%!{(MISSING)public}@ | setCatalogValue:%!{(MISSING)public}@"
+ "2.1.13"
+ "2.2.8"
+ "?\x0f\x1f\a\x112Rd"
+ "AutoAssetStagerDeterminePallasResponseFewer"
+ "AutoAssetStagerDownloadFirstNotInCatalog"
+ "Starting built-in MobileAsset brain built Aug  8 2024 03:28:12"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Aug  8 2024 03:28:12"
+ "TB,N,V_firstDownloadedAsIfNotInCatalog"
+ "TB,N,V_preferenceStagerDownloadFirstNotInCatalog"
+ "Tq,N,V_preferenceStagerDeterminePallasResponseFewer"
+ "[CATALOG-LOOKUP-ADJUST] job provided jobInformation dropped | eventInfo:%!{(MISSING)public}@"
+ "[OSVersion:%!@(MISSING)|Build:%!@(MISSING)|GroupNames:%!@(MISSING)|LookupResults:%!l(MISSING)d|Assets:%!l(MISSING)d]"
+ "_adjustPallasResponseBasedOnPreferences:"
+ "_firstDownloadedAsIfNotInCatalog"
+ "_preferenceStagerDeterminePallasResponseFewer"
+ "_preferenceStagerDownloadFirstNotInCatalog"
+ "firstDownloadedAsIfNotInCatalog"
+ "lookupResultsAssetCount"
+ "preferenceStagerDeterminePallasResponseFewer"
+ "preferenceStagerDownloadFirstNotInCatalog"
+ "setFirstDownloadedAsIfNotInCatalog:"
+ "setPreferenceStagerDeterminePallasResponseFewer:"
+ "setPreferenceStagerDownloadFirstNotInCatalog:"
+ "unable to locate asset to be downloaded in set-lookup-results - skipping asset"
+ "{NextAwaitingBeginDownload} unable to locate entry in set-look-results - skipping asset | stagingDescriptor:%!@(MISSING)"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | latest-to-vend includes personalized-not-grafted|mounted (acceptable since not currently locked) | setConfiguration:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | personalization required after startup secure-healing - clearing latest-to-vend | setConfiguration:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | unable to re-graft during startup secure-healing - clearing latest-to-vend | setConfiguration:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {NextAwaitingBeginDownload} unable to form autoAssetCatalog | stagingDescriptor:%!{(MISSING)public}@"
- "2.1.12"
- "2.2.7"
- "?\x0f\x1f\a\x11\"Rd"
- "Starting built-in MobileAsset brain built Jul 29 2024 20:54:24"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Jul 29 2024 20:54:24"
- "[OSVersion:%!@(MISSING)|Build:%!@(MISSING)|GroupNames:%!@(MISSING)|LookupResults:%!l(MISSING)d]"
- "unable to locate set-lookup-results"
- "{%!{(MISSING)public}@} forcing unlocked of set-configuration | setConfiguration:%!{(MISSING)public}@"

```
