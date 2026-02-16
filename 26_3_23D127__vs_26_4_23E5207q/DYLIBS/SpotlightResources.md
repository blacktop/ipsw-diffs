## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2400.22.0.0.0
-  __TEXT.__text: 0x2993c
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x1598
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0xf58
-  __TEXT.__cstring: 0x2534
-  __TEXT.__oslogstring: 0x2144
-  __TEXT.__unwind_info: 0x8f0
+2418.4.8.2.100
+  __TEXT.__text: 0x2b5d0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x15e8
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0xe2c
+  __TEXT.__cstring: 0x258c
+  __TEXT.__oslogstring: 0x216f
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_classname: 0x207
-  __TEXT.__objc_methname: 0x3675
+  __TEXT.__objc_methname: 0x372f
   __TEXT.__objc_methtype: 0x64a
-  __TEXT.__objc_stubs: 0x3720
+  __TEXT.__objc_stubs: 0x37a0
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__const: 0xbc8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1040
+  __DATA_CONST.__objc_selrefs: 0x1070
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__objc_const: 0x2280
+  __AUTH_CONST.__cfstring: 0x49a0
+  __AUTH_CONST.__objc_const: 0x22a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x180
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__bss: 0x2d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1BFC6D29-3C21-33D3-9678-44065EB5B756
-  Functions: 777
-  Symbols:   2781
-  CStrings:  2265
+  UUID: 45E46E6F-0EA8-3007-A3CD-7A4DAB6C8DF7
+  Functions: 792
+  Symbols:   2833
+  CStrings:  2278
 
Symbols:
+ +[SRParameter parameterTypeFromTypeString:]
+ +[SRParameter parameterWithValue:name:typeString:]
+ +[SSTrialManager trialManagerForNamespaceName:]
+ -[SRDefaultsManager parametersOfContentTypeWithName:client:]
+ -[SRResourcesManager isNamespaceLoaded:]
+ -[SRResourcesManager loadNamespace:]
+ -[SRResourcesManager loadNamespace:].cold.1
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table122
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table82
+ GCC_except_table88
+ GCC_except_table97
+ GCC_except_table99
+ _CFStringCreateWithCString
+ _OBJC_IVAR_$_SRDefaultsManager._otherParameters
+ _OUTLINED_FUNCTION_13
+ __MDPlistContainerCopyObject
+ __MDPlistDictionaryIterate
+ __MDPlistGetPlistObjectType
+ __MDPlistGetRootPlistObjectFromBytes
+ ___47-[SRResources fetchParameter:checkForPositive:]_block_invoke_2
+ ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.453
+ ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke_2
+ ___60-[SRDefaultsManager parametersOfContentTypeWithName:client:]_block_invoke
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.628
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.630
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.630.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.629
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.629.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.524
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.529
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.529.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.530
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.539
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.541
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.541.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.525
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.531
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.540
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.540.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.557
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.559
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.559.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.559.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.561
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.561.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.562
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.562.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.564
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.4
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.567
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.567.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.568
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.568.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.569
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.569.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.569.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.570
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.571
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.571.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.572
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.572.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.565
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.565.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.497
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.497.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.498
+ ___block_descriptor_40_e8_32s_e26_v48?0r*8Q16{?=*Q{?=IC}}24ls32l8
+ ___block_descriptor_40_e8_32s_e38_v32?0"NSString"8"SRParameter"16^B24ls32l8
+ ___block_literal_global.46
+ ___block_literal_global.48
+ ___block_literal_global.50
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.56
+ _close
+ _fstat
+ _mmap
+ _munmap
+ _objc_msgSend$parameterTypeFromTypeString:
+ _objc_msgSend$parameterWithValue:name:typeString:
+ _objc_msgSend$parametersOfContentTypeWithName:client:
+ _objc_msgSend$trialManagerForNamespaceName:
+ _objc_retain_x27
+ _open
- GCC_except_table100
- GCC_except_table104
- GCC_except_table106
- GCC_except_table108
- GCC_except_table113
- GCC_except_table121
- GCC_except_table125
- GCC_except_table126
- GCC_except_table28
- GCC_except_table30
- GCC_except_table32
- GCC_except_table34
- GCC_except_table36
- GCC_except_table44
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table54
- GCC_except_table71
- GCC_except_table75
- GCC_except_table80
- GCC_except_table87
- GCC_except_table96
- GCC_except_table98
- ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.418
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.573
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.575
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.575.cold.1
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.574
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.574.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.465
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.470
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.470.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.471
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.480
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.482
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.482.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.466
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.472
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.481
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.481.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.497
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.497.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.497.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.497.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.500
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.500.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.500.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.505
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507.cold.4
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.508
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.508.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.509
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.509.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.510
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.510.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.510.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.511
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.512
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.512.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.513
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.513.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.514
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.514.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.514.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.506
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.506.cold.1
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.438
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.438.cold.1
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.439
- ___block_literal_global.49
- ___block_literal_global.51
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "\nNamespace %@ has been loaded by the Spotlight daemon\n"
+ "%@.%@"
+ "Trial update handler has not been set yet."
+ "_otherParameters"
+ "isNamespaceLoaded:"
+ "loadNamespace:"
+ "parameterTypeFromTypeString:"
+ "parameterWithValue:name:typeString:"
+ "parametersOfContentTypeWithName:client:"
+ "trialManagerForNamespaceName:"
+ "v48@?0r*8Q16{?=*Q{?=IC}}24"

```
