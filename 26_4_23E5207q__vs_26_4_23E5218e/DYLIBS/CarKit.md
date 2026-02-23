## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-774.8.0.0.0
-  __TEXT.__text: 0x5dbb4
+774.12.0.0.0
+  __TEXT.__text: 0x5de1c
   __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x6244
+  __TEXT.__objc_methlist: 0x625c
   __TEXT.__const: 0x41a
   __TEXT.__gcc_except_tab: 0xa20
-  __TEXT.__oslogstring: 0x648a
+  __TEXT.__oslogstring: 0x659a
   __TEXT.__cstring: 0x549d
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__swift5_typeref: 0x7e

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__unwind_info: 0x1ca0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xbc3
-  __TEXT.__objc_methname: 0x11101
+  __TEXT.__objc_methname: 0x11161
   __TEXT.__objc_methtype: 0x2613
-  __TEXT.__objc_stubs: 0x9640
+  __TEXT.__objc_stubs: 0x9680
   __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__const: 0x1f58
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3558
+  __DATA_CONST.__objc_selrefs: 0x3560
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0x1a28
-  __AUTH_CONST.__cfstring: 0x5780
-  __AUTH_CONST.__objc_const: 0xf9e0
+  __AUTH_CONST.__cfstring: 0x57a0
+  __AUTH_CONST.__objc_const: 0xfa10
   __AUTH_CONST.__objc_intobj: 0x138
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x11d8
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x778
+  __DATA.__objc_ivar: 0x77c
   __DATA.__data: 0x10c0
   __DATA.__bss: 0x690
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25399FB9-8F12-3504-B05E-AF0F25279A99
-  Functions: 2915
-  Symbols:   9491
-  CStrings:  5038
+  UUID: 68A58171-5B34-36B9-91EC-B16D7491331A
+  Functions: 2917
+  Symbols:   9498
+  CStrings:  5047
 
Symbols:
+ -[CARSession cachedVideoPlaybackAvailable]
+ -[CARSession setCachedVideoPlaybackAvailable:]
+ GCC_except_table147
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table202
+ _OBJC_IVAR_$_CARSession._cachedVideoPlaybackAvailable
+ ___24-[CARSession suggestUI:]_block_invoke.433
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.46
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.46.cold.1
+ ___CARHandleSuggestUI_block_invoke.429
+ ___block_literal_global.428
+ ___block_literal_global.438
+ ___block_literal_global.646
+ ___block_literal_global.751
+ _kFigEndpointProperty_AirPlayVideoPlaybackAudioOnlyMode
+ _objc_msgSend$cachedVideoPlaybackAvailable
+ _objc_msgSend$setCachedVideoPlaybackAvailable:
+ _objc_msgSend$videoPlaybackAvailable
- GCC_except_table145
- GCC_except_table168
- GCC_except_table174
- GCC_except_table200
- ___24-[CARSession suggestUI:]_block_invoke.430
- ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.45
- ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.45.cold.1
- ___CARHandleSuggestUI_block_invoke.426
- ___block_literal_global.425
- ___block_literal_global.435
- ___block_literal_global.47
- ___block_literal_global.638
- ___block_literal_global.743
- _kFigEndpointProperty_SupportedFeatures
- _objc_msgSend$unsignedLongLongValue
Functions:
~ -[CARSession videoPlaybackAvailable] : 228 -> 240
~ -[CARSession .cxx_destruct] : 152 -> 164
~ _CRCanvasSizeOverridesWithAirplayDisplays : 680 -> 876
~ _CRScaledDisplaysWithDisplayMode : 1136 -> 1304
~ -[CARSession _sessionUpdatesQueue_handleEndpointDescriptionChanged] : 188 -> 276
+ -[CARSession cachedVideoPlaybackAvailable]
+ -[CARSession setObservers:]
~ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke_2 : 204 -> 292
~ _CRFetchStopSessionReasonsList : 236 -> 216
CStrings:
+ "CRCanvasSizeOverridesWithAirplayDisplays: scaleInfo: %{public}@"
+ "CRCanvasSizeOverridesWithAirplayDisplays: zoomFactor: %{public}@"
+ "CRScaledDisplaysWithAirplayDisplays: scaleInfo: %{public}@"
+ "CRScaledDisplaysWithAirplayDisplays: zoomFactor: %{public}@"
+ "Forced"
+ "Posting notification for video playback availability changed"
+ "T@\"NSNumber\",&,N,V_cachedVideoPlaybackAvailable"
+ "_cachedVideoPlaybackAvailable"
+ "cachedVideoPlaybackAvailable"
+ "failed to get video playback available for endpoint"
+ "setCachedVideoPlaybackAvailable:"
- "Notification for video playback availability changed"
- "failed to get supported features for endpoint"
- "unsignedLongLongValue"

```
