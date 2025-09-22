## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-738.0.5.0.0
-  __TEXT.__text: 0x194cec
+738.0.7.0.0
+  __TEXT.__text: 0x194ee8
   __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__objc_methlist: 0x1110c
+  __TEXT.__objc_methlist: 0x11124
   __TEXT.__const: 0x2c118
   __TEXT.__gcc_except_tab: 0x13dc0
-  __TEXT.__oslogstring: 0x1e687
-  __TEXT.__cstring: 0x1d925
+  __TEXT.__oslogstring: 0x1e6c5
+  __TEXT.__cstring: 0x1d931
   __TEXT.__ustring: 0xe6
   __TEXT.__unwind_info: 0x6720
   __TEXT.__objc_classname: 0x2027
-  __TEXT.__objc_methname: 0x2a408
+  __TEXT.__objc_methname: 0x2a46c
   __TEXT.__objc_methtype: 0xa641
-  __TEXT.__objc_stubs: 0x1ac60
+  __TEXT.__objc_stubs: 0x1ac80
   __DATA_CONST.__got: 0x1680
   __DATA_CONST.__const: 0x3658
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d98
+  __DATA_CONST.__objc_selrefs: 0x7da8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x790
   __DATA_CONST.__objc_arraydata: 0x880
   __AUTH_CONST.__auth_got: 0x1e58
   __AUTH_CONST.__const: 0x3cb8
-  __AUTH_CONST.__cfstring: 0x10480
-  __AUTH_CONST.__objc_const: 0x3ce80
+  __AUTH_CONST.__cfstring: 0x104a0
+  __AUTH_CONST.__objc_const: 0x3ceb0
   __AUTH_CONST.__objc_intobj: 0x3240
   __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3660
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x2000
+  __DATA.__objc_ivar: 0x2004
   __DATA.__data: 0x1ca0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1dd8

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 164340C8-E7CF-3DAC-8A8F-9B3892106732
-  Functions: 7772
-  Symbols:   30082
-  CStrings:  14424
+  UUID: 8F3CFFB5-8F69-336C-9CD9-20F9F17A8A93
+  Functions: 7774
+  Symbols:   30088
+  CStrings:  14431
 
Symbols:
+ -[ARWorldTrackingConfiguration disableLocationSensor]
+ -[ARWorldTrackingConfiguration setDisableLocationSensor:]
+ _OBJC_IVAR_$_ARWorldTrackingConfiguration._disableLocationSensor
+ ___45+[ARSession _applySessionOverrides:outError:]_block_invoke.465
+ ___48-[ARSession _sessionShouldAttemptRelocalization]_block_invoke.511
+ ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.311
+ ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.312
+ ___69-[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]_block_invoke.469
+ ___block_literal_global.290
+ ___block_literal_global.295
+ ___block_literal_global.299
+ ___block_literal_global.314
+ ___block_literal_global.319
+ ___block_literal_global.323
+ ___block_literal_global.341
+ ___block_literal_global.421
+ ___block_literal_global.427
+ ___block_literal_global.430
+ ___block_literal_global.459
+ ___block_literal_global.479
+ ___block_literal_global.931
+ ___block_literal_global.935
+ ___block_literal_global.940
+ _objc_msgSend$disableLocationSensor
- ___45+[ARSession _applySessionOverrides:outError:]_block_invoke.462
- ___48-[ARSession _sessionShouldAttemptRelocalization]_block_invoke.508
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.308
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.309
- ___69-[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]_block_invoke.466
- ___block_literal_global.292
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.320
- ___block_literal_global.416
- ___block_literal_global.420
- ___block_literal_global.422
- ___block_literal_global.476
- ___block_literal_global.928
- ___block_literal_global.932
- ___block_literal_global.934
CStrings:
+ "%{public}@ <%p>: Disabling location sensor data type via SPI."
+ "TB,N,V_disableLocationSensor"
+ "_disableLocationSensor"
+ "class != %@"
+ "disableLocationSensor"
+ "setDisableLocationSensor:"

```
