## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-819.100.8.0.0
-  __TEXT.__text: 0x37c64
+819.120.2.0.0
+  __TEXT.__text: 0x37d28
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x1724
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x2447
-  __TEXT.__oslogstring: 0x5d82
-  __TEXT.__gcc_except_tab: 0xdd4
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0x2466
+  __TEXT.__oslogstring: 0x5dd7
+  __TEXT.__gcc_except_tab: 0xdec
   __TEXT.__unwind_info: 0xb18
   __TEXT.__objc_classname: 0x2a3
   __TEXT.__objc_methname: 0x3a7d

   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__cfstring: 0x2060
+  __AUTH_CONST.__cfstring: 0x2080
   __AUTH_CONST.__objc_const: 0x2160
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x1b0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6119D3F-3784-3537-91D3-743AC9CC3FAE
+  UUID: 7BDE8030-B753-3384-8A06-A08B7C6C264E
   Functions: 776
   Symbols:   2591
-  CStrings:  1991
+  CStrings:  1994
 
Symbols:
+ ___CacheDeleteEnableReserveSpace_block_invoke.295
+ ___CacheDeletePauseReserveSpaceMonitoring_block_invoke.286
+ ___CacheDeleteRequestCacheableSpaceGuidance_block_invoke.201
+ ___CacheDeleteServiceRequest_block_invoke.232
+ ___CacheDeleteSetEntitledAndUnentitledReservation_block_invoke.304
+ ____CacheDeleteCacheableForVolume_block_invoke.408
+ ____CacheDeletePurgeSpaceWithInfo_block_invoke.389
+ ____CacheDeleteRegisterLegacyCallbacks_block_invoke.360
+ ____CacheDeleteRegisterLegacyCallbacks_block_invoke.361
+ ____CacheDeleteRegister_block_invoke.323
+ ____CacheDeleteRegister_block_invoke.346
+ ____CacheDeleteRegister_block_invoke.356
+ ____CacheDeleteRegister_block_invoke_2.354
+ ____CacheDeleteSetCacheableForVolume_block_invoke.405
+ ___block_literal_global.193
+ ___block_literal_global.223
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.288
+ ___block_literal_global.290
+ ___block_literal_global.297
+ ___block_literal_global.306
+ ___block_literal_global.315
+ ___block_literal_global.317
+ ___block_literal_global.348
+ ___block_literal_global.358
+ ___block_literal_global.407
- ___CacheDeleteEnableReserveSpace_block_invoke.292
- ___CacheDeletePauseReserveSpaceMonitoring_block_invoke.283
- ___CacheDeleteRequestCacheableSpaceGuidance_block_invoke.198
- ___CacheDeleteServiceRequest_block_invoke.229
- ___CacheDeleteSetEntitledAndUnentitledReservation_block_invoke.301
- ____CacheDeleteCacheableForVolume_block_invoke.405
- ____CacheDeletePurgeSpaceWithInfo_block_invoke.386
- ____CacheDeleteRegisterLegacyCallbacks_block_invoke.357
- ____CacheDeleteRegisterLegacyCallbacks_block_invoke.358
- ____CacheDeleteRegister_block_invoke.320
- ____CacheDeleteRegister_block_invoke.343
- ____CacheDeleteRegister_block_invoke.350
- ____CacheDeleteRegister_block_invoke_2.351
- ____CacheDeleteSetCacheableForVolume_block_invoke.402
- ___block_literal_global.190
- ___block_literal_global.220
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.294
- ___block_literal_global.303
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.345
- ___block_literal_global.355
- ___block_literal_global.404
Functions:
~ _CacheDeleteCopyAvailableSpaceForVolume : 3536 -> 3732
CStrings:
+ "%d publicClientAvailableSpaceForVolume added entitled free %lld total freeSpace %lld"
+ "CACHE_DELETE_SUR_ENTITLED_FREE"

```
