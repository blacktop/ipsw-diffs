## ReplayKit

> `/System/iOSSupport/System/Library/Frameworks/ReplayKit.framework/Versions/A/ReplayKit`

```diff

-595.11.1.0.0
-  __TEXT.__text: 0x28c78
+610.5.1.5.1
+  __TEXT.__text: 0x293d4
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x20d0
+  __TEXT.__objc_methlist: 0x2a90
   __TEXT.__const: 0xd8
   __TEXT.__oslogstring: 0x362e
-  __TEXT.__cstring: 0x5469
+  __TEXT.__cstring: 0x5516
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x608
-  __TEXT.__objc_methname: 0x6fa3
-  __TEXT.__objc_methtype: 0x1d55
-  __TEXT.__objc_stubs: 0x4ae0
+  __TEXT.__objc_methname: 0x700d
+  __TEXT.__objc_methtype: 0x1db7
+  __TEXT.__objc_stubs: 0x4b00
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17f0
+  __DATA_CONST.__objc_selrefs: 0x1938
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0xc18
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x6790
+  __AUTH_CONST.__const: 0xc38
+  __AUTH_CONST.__cfstring: 0x1380
+  __AUTH_CONST.__objc_const: 0x55b8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x9b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 488EA6CF-C207-37CE-A1F0-AA41641B11C5
-  Functions: 1045
-  Symbols:   2693
-  CStrings:  2164
+  UUID: 1630465D-4039-3D98-97B1-1A62B2713D9D
+  Functions: 1061
+  Symbols:   2710
+  CStrings:  2172
 
Symbols:
+ +[NSBundle(RPExtensions) _rpFrameworkBundle].cold.1
+ +[NSBundle(RPExtensions) _rpPluralLocalizedStringFromFrameworkBundleWithKey:]
+ +[RPDaemonProxy daemonProxy].cold.1
+ +[RPFeatureFlagUtility sharedInstance].cold.1
+ +[RPStoreManager sharedManager].cold.1
+ -[RPBroadcastSampleHandler audioQueue].cold.1
+ -[RPBroadcastSampleHandler group].cold.1
+ -[RPBroadcastSampleHandler videoQueue].cold.1
+ -[RPDaemonProxy pickerDidUpdate:withFilter:preservedFilter:forStream:]
+ -[RPScreenRecorder audioQueue].cold.1
+ -[RPScreenRecorder processQueue].cold.1
+ -[RPScreenRecorder videoQueue].cold.1
+ _OUTLINED_FUNCTION_7
+ __21-[RPDaemonProxy init]_block_invoke.236
+ __70-[RPDaemonProxy pickerDidUpdate:withFilter:preservedFilter:forStream:]_block_invoke.cold.1
+ ___70-[RPDaemonProxy pickerDidUpdate:withFilter:preservedFilter:forStream:]_block_invoke
+ __block_literal_global.241
+ __block_literal_global.243
+ __block_literal_global.245
+ __block_literal_global.247
+ __block_literal_global.249
+ __block_literal_global.251
+ __block_literal_global.253
+ __block_literal_global.255
+ __block_literal_global.257
+ __block_literal_global.259
+ __block_literal_global.261
+ __block_literal_global.263
+ __block_literal_global.265
+ __block_literal_global.267
+ __block_literal_global.269
+ __block_literal_global.271
+ __block_literal_global.273
+ __block_literal_global.275
+ __block_literal_global.277
+ __block_literal_global.279
+ __block_literal_global.281
+ __block_literal_global.283
+ __block_literal_global.285
+ __block_literal_global.287
+ __block_literal_global.289
+ __block_literal_global.291
+ __block_literal_global.293
+ __block_literal_global.295
+ __block_literal_global.297
+ __block_literal_global.299
+ __block_literal_global.301
+ __block_literal_global.303
+ __block_literal_global.305
+ __block_literal_global.307
+ __block_literal_global.309
+ __block_literal_global.311
+ __block_literal_global.313
+ __block_literal_global.315
+ __block_literal_global.317
+ __block_literal_global.323
+ __block_literal_global.325
+ __block_literal_global.327
+ __block_literal_global.329
+ __block_literal_global.331
+ __block_literal_global.333
+ __block_literal_global.335
+ __block_literal_global.337
+ __block_literal_global.339
+ __block_literal_global.348
+ __block_literal_global.350
+ __block_literal_global.352
+ __block_literal_global.354
+ __block_literal_global.356
+ __block_literal_global.358
+ __block_literal_global.360
+ __block_literal_global.362
+ __block_literal_global.364
+ __block_literal_global.366
+ __block_literal_global.368
+ __block_literal_global.370
+ __block_literal_global.372
+ __block_literal_global.374
+ __block_literal_global.376
+ __block_literal_global.378
+ __block_literal_global.380
+ __block_literal_global.382
+ __block_literal_global.384
+ __block_literal_global.386
+ __block_literal_global.388
+ __block_literal_global.390
+ __block_literal_global.392
+ __block_literal_global.394
+ __block_literal_global.396
+ _objc_msgSend$pickerDidUpdate:withFilter:preservedFilter:forStream:
- __21-[RPDaemonProxy init]_block_invoke.233
- __block_literal_global.238
- __block_literal_global.240
- __block_literal_global.242
- __block_literal_global.244
- __block_literal_global.246
- __block_literal_global.248
- __block_literal_global.250
- __block_literal_global.252
- __block_literal_global.254
- __block_literal_global.256
- __block_literal_global.258
- __block_literal_global.260
- __block_literal_global.262
- __block_literal_global.264
- __block_literal_global.266
- __block_literal_global.268
- __block_literal_global.270
- __block_literal_global.272
- __block_literal_global.274
- __block_literal_global.276
- __block_literal_global.278
- __block_literal_global.280
- __block_literal_global.282
- __block_literal_global.284
- __block_literal_global.286
- __block_literal_global.288
- __block_literal_global.290
- __block_literal_global.292
- __block_literal_global.294
- __block_literal_global.296
- __block_literal_global.298
- __block_literal_global.300
- __block_literal_global.302
- __block_literal_global.304
- __block_literal_global.306
- __block_literal_global.308
- __block_literal_global.310
- __block_literal_global.312
- __block_literal_global.314
- __block_literal_global.320
- __block_literal_global.322
- __block_literal_global.324
- __block_literal_global.326
- __block_literal_global.328
- __block_literal_global.330
- __block_literal_global.332
- __block_literal_global.334
- __block_literal_global.336
- __block_literal_global.345
- __block_literal_global.347
- __block_literal_global.349
- __block_literal_global.351
- __block_literal_global.353
- __block_literal_global.355
- __block_literal_global.357
- __block_literal_global.359
- __block_literal_global.361
- __block_literal_global.363
- __block_literal_global.365
- __block_literal_global.367
- __block_literal_global.369
- __block_literal_global.371
- __block_literal_global.373
- __block_literal_global.375
- __block_literal_global.377
- __block_literal_global.379
- __block_literal_global.381
- __block_literal_global.383
- __block_literal_global.385
- __block_literal_global.387
- __block_literal_global.389
- __block_literal_global.391
CStrings:
+ "-[RPDaemonProxy pickerDidUpdate:withFilter:preservedFilter:forStream:]"
+ "-[RPDaemonProxy pickerDidUpdate:withFilter:preservedFilter:forStream:]_block_invoke"
+ "LocalizablePlural"
+ "Vv48@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSDictionary\"32@\"NSDictionary\"40"
+ "Vv48@0:8@16@24@32@40"
+ "_rpPluralLocalizedStringFromFrameworkBundleWithKey:"
+ "pickerDidUpdate:withFilter:preservedFilter:forStream:"

```
