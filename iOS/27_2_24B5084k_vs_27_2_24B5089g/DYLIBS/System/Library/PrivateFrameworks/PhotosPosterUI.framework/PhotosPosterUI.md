## PhotosPosterUI

> `/System/Library/PrivateFrameworks/PhotosPosterUI.framework/PhotosPosterUI`

```diff

-916.40.110.0.0
-  __TEXT.__text: 0xc16f4
-  __TEXT.__objc_methlist: 0xa72c
+916.45.110.0.0
+  __TEXT.__text: 0xc1b10
+  __TEXT.__objc_methlist: 0xa7f4
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__const: 0x2ed8
   __TEXT.__constg_swiftt: 0x172c

   __TEXT.__swift5_assocty: 0x2d8
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0xb8
-  __TEXT.__cstring: 0x6e7e
+  __TEXT.__cstring: 0x6e7f
   __TEXT.__swift5_capture: 0x8dc
-  __TEXT.__oslogstring: 0x4cf0
+  __TEXT.__oslogstring: 0x4d18
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__gcc_except_tab: 0x19a4
+  __TEXT.__gcc_except_tab: 0x1998
   __TEXT.__ustring: 0xdc
-  __TEXT.__unwind_info: 0x3c80
+  __TEXT.__unwind_info: 0x3c90
   __TEXT.__eh_frame: 0x4dc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d90
-  __DATA_CONST.__objc_classlist: 0x348
+  __DATA_CONST.__const: 0x2d18
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7420
+  __DATA_CONST.__objc_selrefs: 0x7468
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x1208
   __AUTH_CONST.__const: 0x32e0
   __AUTH_CONST.__cfstring: 0x50c0
-  __AUTH_CONST.__objc_const: 0x11b38
+  __AUTH_CONST.__objc_const: 0x11d10
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__auth_got: 0x1b48
-  __AUTH.__objc_data: 0x30d8
-  __AUTH.__data: 0x950
-  __DATA.__objc_ivar: 0xa90
-  __DATA.__data: 0x2c38
+  __AUTH.__objc_data: 0x3128
+  __AUTH.__data: 0x948
+  __DATA.__objc_ivar: 0xaa4
+  __DATA.__data: 0x2c28
   __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5310
-  Symbols:   10227
+  Functions: 5322
+  Symbols:   10258
   CStrings:  1257
 
Symbols:
+ -[PUPosterGlobalEditProperties .cxx_destruct]
+ -[PUPosterGlobalEditProperties initWithStyle:spatialPhotoEnabled:settlingEffectEnabled:]
+ -[PUPosterGlobalEditProperties isSettlingEffectEnabled]
+ -[PUPosterGlobalEditProperties isSpatialPhotoEnabled]
+ -[PUPosterGlobalEditProperties style]
+ -[PUWallpaperPosterController _displayContextForScaledSize:scale:primary:]
+ -[PUWallpaperPosterController _savedStyleForPosterMedia:displayContext:]
+ -[PUWallpaperPosterController _shouldReframeLayerStack:displayContext:]
+ -[PUWallpaperPosterController _substituteLayerStackForBakedLayerStack:wallpaperURL:displayContext:]
+ -[PUWallpaperPosterEditModel _updateCurrentEditViewModel]
+ -[PUWallpaperPosterEditModel _updateGlobalEditProperties]
+ -[PUWallpaperPosterEditModel globalEditProperties]
+ -[PUWallpaperPosterEditModel invalidateInactiveEditViewModels]
+ -[PUWallpaperPosterEditModel observable:didChange:context:]
+ -[PUWallpaperPosterEditModel setCurrentEditViewModel:]
+ -[PUWallpaperPosterEditModel setGlobalEditProperties:]
+ -[PUWallpaperPosterEditViewModel applyGlobalEditProperties:]
+ GCC_except_table1028
+ GCC_except_table1065
+ GCC_except_table1073
+ GCC_except_table1078
+ GCC_except_table1101
+ GCC_except_table1150
+ GCC_except_table1430
+ GCC_except_table1431
+ GCC_except_table1563
+ GCC_except_table1564
+ GCC_except_table1588
+ GCC_except_table1789
+ GCC_except_table1794
+ GCC_except_table1816
+ GCC_except_table1860
+ GCC_except_table1868
+ GCC_except_table1895
+ GCC_except_table1903
+ GCC_except_table1904
+ GCC_except_table1910
+ GCC_except_table1911
+ GCC_except_table1912
+ GCC_except_table1937
+ GCC_except_table1941
+ GCC_except_table1952
+ GCC_except_table1956
+ GCC_except_table1958
+ GCC_except_table1961
+ GCC_except_table1964
+ GCC_except_table1967
+ GCC_except_table1976
+ GCC_except_table2015
+ GCC_except_table2077
+ GCC_except_table2102
+ GCC_except_table2105
+ GCC_except_table2116
+ GCC_except_table2122
+ GCC_except_table2125
+ GCC_except_table2141
+ GCC_except_table2144
+ GCC_except_table2180
+ GCC_except_table2191
+ GCC_except_table2193
+ GCC_except_table2197
+ GCC_except_table2200
+ GCC_except_table2211
+ GCC_except_table2216
+ GCC_except_table2223
+ GCC_except_table2229
+ GCC_except_table2230
+ GCC_except_table2235
+ GCC_except_table2237
+ GCC_except_table2241
+ GCC_except_table2244
+ GCC_except_table2246
+ GCC_except_table2253
+ GCC_except_table2258
+ GCC_except_table2290
+ GCC_except_table2309
+ GCC_except_table2418
+ GCC_except_table2438
+ GCC_except_table2440
+ GCC_except_table2681
+ GCC_except_table2699
+ GCC_except_table3155
+ GCC_except_table3158
+ GCC_except_table3193
+ GCC_except_table3195
+ GCC_except_table3215
+ GCC_except_table3216
+ GCC_except_table3246
+ GCC_except_table3257
+ GCC_except_table3260
+ GCC_except_table3321
+ GCC_except_table3343
+ GCC_except_table3346
+ GCC_except_table3396
+ GCC_except_table3399
+ GCC_except_table3403
+ GCC_except_table3407
+ GCC_except_table3421
+ _OBJC_CLASS_$_PUPosterGlobalEditProperties
+ _OBJC_IVAR_$_PUPosterGlobalEditProperties._settlingEffectEnabled
+ _OBJC_IVAR_$_PUPosterGlobalEditProperties._spatialPhotoEnabled
+ _OBJC_IVAR_$_PUPosterGlobalEditProperties._style
+ _OBJC_IVAR_$_PUWallpaperPosterEditModel._currentEditViewModel
+ _OBJC_IVAR_$_PUWallpaperPosterEditModel._globalEditProperties
+ _OBJC_METACLASS_$_PUPosterGlobalEditProperties
+ __OBJC_$_INSTANCE_METHODS_PUPosterGlobalEditProperties
+ __OBJC_$_INSTANCE_VARIABLES_PUPosterGlobalEditProperties
+ __OBJC_$_PROP_LIST_PUPosterGlobalEditProperties
+ __OBJC_CLASS_PROTOCOLS_$_PUWallpaperPosterEditModel
+ __OBJC_CLASS_RO_$_PUPosterGlobalEditProperties
+ __OBJC_METACLASS_RO_$_PUPosterGlobalEditProperties
+ ___60-[PUWallpaperPosterEditViewModel applyGlobalEditProperties:]_block_invoke
+ ___block_descriptor_64_e8_32r40r_e5_v8?0lr32l8r40l8
+ _objc_msgSend$_displayContextForScaledSize:scale:primary:
+ _objc_msgSend$_savedStyleForPosterMedia:displayContext:
+ _objc_msgSend$_shouldReframeLayerStack:displayContext:
+ _objc_msgSend$_substituteLayerStackForBakedLayerStack:wallpaperURL:displayContext:
+ _objc_msgSend$_updateCurrentEditViewModel
+ _objc_msgSend$_updateGlobalEditProperties
+ _objc_msgSend$applyGlobalEditProperties:
+ _objc_msgSend$currentEditViewModel
+ _objc_msgSend$globalEditProperties
+ _objc_msgSend$initWithStyle:spatialPhotoEnabled:settlingEffectEnabled:
+ _objc_msgSend$invalidateInactiveEditViewModels
+ _objc_msgSend$isSegmentedStyle:
+ _objc_msgSend$setCurrentEditViewModel:
+ _objc_msgSend$setGlobalEditProperties:
- -[PUWallpaperPosterController _applyReframedLayerStack:style:displayContext:posterMedia:]
- -[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]
- GCC_except_table1027
- GCC_except_table1064
- GCC_except_table1070
- GCC_except_table1075
- GCC_except_table1080
- GCC_except_table1107
- GCC_except_table1152
- GCC_except_table1432
- GCC_except_table1433
- GCC_except_table1553
- GCC_except_table1554
- GCC_except_table1578
- GCC_except_table1779
- GCC_except_table1784
- GCC_except_table1806
- GCC_except_table1850
- GCC_except_table1858
- GCC_except_table1885
- GCC_except_table1893
- GCC_except_table1894
- GCC_except_table1900
- GCC_except_table1901
- GCC_except_table1902
- GCC_except_table1927
- GCC_except_table1931
- GCC_except_table1942
- GCC_except_table1946
- GCC_except_table1948
- GCC_except_table1951
- GCC_except_table1954
- GCC_except_table1957
- GCC_except_table1966
- GCC_except_table2005
- GCC_except_table2067
- GCC_except_table2092
- GCC_except_table2095
- GCC_except_table2106
- GCC_except_table2112
- GCC_except_table2115
- GCC_except_table2131
- GCC_except_table2134
- GCC_except_table2170
- GCC_except_table2181
- GCC_except_table2183
- GCC_except_table2187
- GCC_except_table2190
- GCC_except_table2201
- GCC_except_table2203
- GCC_except_table2206
- GCC_except_table2215
- GCC_except_table2219
- GCC_except_table2220
- GCC_except_table2227
- GCC_except_table2231
- GCC_except_table2234
- GCC_except_table2236
- GCC_except_table2243
- GCC_except_table2248
- GCC_except_table2280
- GCC_except_table2299
- GCC_except_table2408
- GCC_except_table2428
- GCC_except_table2430
- GCC_except_table2669
- GCC_except_table2687
- GCC_except_table3143
- GCC_except_table3146
- GCC_except_table3181
- GCC_except_table3183
- GCC_except_table3203
- GCC_except_table3204
- GCC_except_table3234
- GCC_except_table3245
- GCC_except_table3248
- GCC_except_table3309
- GCC_except_table3331
- GCC_except_table3334
- GCC_except_table3384
- GCC_except_table3387
- GCC_except_table3391
- GCC_except_table3395
- GCC_except_table3409
- ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke
- ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke_2
- ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke_3
- ___121-[PUWallpaperPosterController _reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:]_block_invoke_4
- ___block_descriptor_40_e8_32s_e39_B32?0"PFPosterDisplayContext"8Q16^B24ls32l8
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s40l8s48l8w72l8s56l8s64l8
- ___block_descriptor_88_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0ls32l8s40l8s48l8w80l8s56l8s64l8s72l8
- _objc_msgSend$_applyReframedLayerStack:style:displayContext:posterMedia:
- _objc_msgSend$_reframeLayerStackFromOriginalAssetIfNeeded:wallpaperURL:style:displayContext:posterMedia:
- _objc_msgSend$displayContextWithSize:scale:
- _objc_msgSend$screenScale
CStrings:
+ "GlobalEditPropertiesObservationContext"
+ "Initialized display context: %{public}@ (landscape=%d)"
+ "Not reframing poster: it has the %{public}@ photo style applied"
+ "Warmup load succeeded (complete: %{public}@), screen: %.0f×%.0f, image: %.0f×%.0f"
- "B32@?0@\"PFPosterDisplayContext\"8Q16^B24"
- "Discarding reframed poster for stale display context or media"
- "Initialized display context: %{public}@"
- "Warmup load succeeded, screen: %.0f×%.0f, image: %.0f×%.0f"
```
