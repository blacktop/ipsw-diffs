## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3515.6.1.0.0
-  __TEXT.__text: 0x7be38
+3515.7.1.0.0
+  __TEXT.__text: 0x7cba4
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x3768
+  __TEXT.__objc_methlist: 0x37e8
   __TEXT.__const: 0x1c0
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__cstring: 0xb766
+  __TEXT.__cstring: 0xb8a3
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__oslogstring: 0xeb4c
+  __TEXT.__oslogstring: 0xed1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x15d0
-  __TEXT.__unwind_info: 0x13e8
-  __TEXT.__objc_classname: 0x483
-  __TEXT.__objc_methname: 0xa30e
-  __TEXT.__objc_methtype: 0x10eb
-  __TEXT.__objc_stubs: 0x83e0
-  __DATA_CONST.__got: 0x578
+  __TEXT.__unwind_info: 0x13f0
+  __TEXT.__objc_classname: 0x4a2
+  __TEXT.__objc_methname: 0xa480
+  __TEXT.__objc_methtype: 0x10ef
+  __TEXT.__objc_stubs: 0x84e0
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__const: 0x1ec0
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2760
+  __DATA_CONST.__objc_selrefs: 0x27a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x8c0
   __AUTH_CONST.__const: 0x668
-  __AUTH_CONST.__cfstring: 0x4c00
-  __AUTH_CONST.__objc_const: 0x4558
+  __AUTH_CONST.__cfstring: 0x4c20
+  __AUTH_CONST.__objc_const: 0x4658
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x3e0
+  __AUTH.__objc_data: 0x430
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x334
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0x288
   __DATA.__bss: 0x50
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6F8DB8B3-9468-32BA-B324-EFF536610AF9
-  Functions: 1553
-  Symbols:   5681
-  CStrings:  4613
+  UUID: 01767AAF-E4FA-39B4-927D-77AF969F8010
+  Functions: 1563
+  Symbols:   5718
+  CStrings:  4639
 
Symbols:
+ +[UAFAutoAssetManager getAssetSelectorsFromSpecifiers:status:]
+ +[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:telemetryInfo:]
+ +[UAFBiomeInstrumenter _createBiomeAssetSet:withAssets:]
+ +[UAFBiomeInstrumenter logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:]
+ +[UAFInstrumentationProvider logAlterSetFromPSUSAtomicInstance:alterSetData:]
+ -[UAFInstrumentationAlterSetData .cxx_destruct]
+ -[UAFInstrumentationAlterSetData addedSpecifiers]
+ -[UAFInstrumentationAlterSetData removedSelectors]
+ -[UAFInstrumentationAlterSetData setAddedSpecifiers:]
+ -[UAFInstrumentationAlterSetData setRemovedSelectors:]
+ GCC_except_table79
+ _OBJC_CLASS_$_UAFInstrumentationAlterSetData
+ _OBJC_IVAR_$_UAFInstrumentationAlterSetData._addedSpecifiers
+ _OBJC_IVAR_$_UAFInstrumentationAlterSetData._removedSelectors
+ _OBJC_METACLASS_$_UAFInstrumentationAlterSetData
+ __OBJC_$_INSTANCE_METHODS_UAFInstrumentationAlterSetData
+ __OBJC_$_INSTANCE_VARIABLES_UAFInstrumentationAlterSetData
+ __OBJC_$_PROP_LIST_UAFInstrumentationAlterSetData
+ __OBJC_CLASS_RO_$_UAFInstrumentationAlterSetData
+ __OBJC_METACLASS_RO_$_UAFInstrumentationAlterSetData
+ ___111+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:telemetryInfo:]_block_invoke
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.454
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.465
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.415
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.417
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.401
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.425
+ ___85+[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:currentPolicy:]_block_invoke
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.438
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.466
+ ___block_literal_global.414
+ ___block_literal_global.421
+ ___block_literal_global.424
+ _objc_msgSend$_createBiomeAssetSet:withAssets:
+ _objc_msgSend$addedSpecifiers
+ _objc_msgSend$getAssetSelectorsFromSpecifiers:status:
+ _objc_msgSend$getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:telemetryInfo:
+ _objc_msgSend$logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:
+ _objc_msgSend$logAlterSetFromPSUSAtomicInstance:alterSetData:
+ _objc_msgSend$removedSelectors
+ _objc_msgSend$setAddedSpecifiers:
+ _objc_msgSend$setRemovedSelectors:
- +[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]
- GCC_except_table92
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.452
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.463
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.414
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.416
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.400
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.424
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.437
- ___97+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]_block_invoke
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.465
- ___block_literal_global.413
- ___block_literal_global.420
- ___block_literal_global.423
- _objc_msgSend$getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:
CStrings:
+ "%s Can't log %{public}@ as this system doesn't support Biome."
+ "%s Cannot log %{public}@ with nil asset set name"
+ "%s Emitted alter set from PSUS event for asset set: %{public}@"
+ "%s Logging alter set from PSUS for asset set: %{public}@"
+ "%s No latest downloaded atomic instance entries for asset set %{public}@"
+ "%s Unexpected object type passed in assets set"
+ "%s Using Biome to send %{public}@ for asset set: %{public}@ with %lu removed specifiers and %lu added specifiers"
+ "+[UAFAutoAssetManager getAssetSelectorsFromSpecifiers:status:]"
+ "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:telemetryInfo:]"
+ "+[UAFBiomeInstrumenter _createBiomeAssetSet:withAssets:]"
+ "+[UAFBiomeInstrumenter logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:]"
+ "+[UAFInstrumentationProvider logAlterSetFromPSUSAtomicInstance:alterSetData:]"
+ "@68@0:8@16^@24B32^B36^B44^@52^@60"
+ "PSUSAlteredAssetSet"
+ "T@\"NSSet\",C,N,V_addedSpecifiers"
+ "T@\"NSSet\",C,N,V_removedSelectors"
+ "UAFInstrumentationAlterSetData"
+ "_addedSpecifiers"
+ "_createBiomeAssetSet:withAssets:"
+ "_removedSelectors"
+ "addedSpecifiers"
+ "getAssetSelectorsFromSpecifiers:status:"
+ "getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:telemetryInfo:"
+ "logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:"
+ "logAlterSetFromPSUSAtomicInstance:alterSetData:"
+ "removedSelectors"
+ "setAddedSpecifiers:"
+ "setRemovedSelectors:"
- "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]"
- "@60@0:8@16^@24B32^B36^B44^@52"
- "getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:"

```
