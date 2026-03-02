## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-774.12.0.0.0
-  __TEXT.__text: 0x5de1c
+774.14.0.0.0
+  __TEXT.__text: 0x5e054
   __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_methlist: 0x625c
   __TEXT.__const: 0x41a
   __TEXT.__gcc_except_tab: 0xa20
-  __TEXT.__oslogstring: 0x659a
-  __TEXT.__cstring: 0x549d
+  __TEXT.__oslogstring: 0x660a
+  __TEXT.__cstring: 0x54ad
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__swift5_typeref: 0x7e
   __TEXT.__constg_swiftt: 0xd8

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__unwind_info: 0x1ca8
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xbc3
   __TEXT.__objc_methname: 0x11161
   __TEXT.__objc_methtype: 0x2613
   __TEXT.__objc_stubs: 0x9680
-  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__got: 0x7b8
   __DATA_CONST.__const: 0x1f58
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0x1a28
-  __AUTH_CONST.__cfstring: 0x57a0
+  __AUTH_CONST.__cfstring: 0x57c0
   __AUTH_CONST.__objc_const: 0xfa10
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 68A58171-5B34-36B9-91EC-B16D7491331A
-  Functions: 2917
-  Symbols:   9498
-  CStrings:  5047
+  UUID: 4C5B357D-0718-3D36-9334-11B592857ACD
+  Functions: 2918
+  Symbols:   9502
+  CStrings:  5052
 
Symbols:
+ _CARSafeCast
+ ___24-[CARSession suggestUI:]_block_invoke.436
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.367
+ ___CARHandleSuggestUI_block_invoke.432
+ ___block_literal_global.649
+ ___block_literal_global.754
+ _kFigEndpointCentralNotificationKey_MainAudioBorrowID
+ _kFigEndpointProperty_CurrentMainAudioBorrowID
- ___24-[CARSession suggestUI:]_block_invoke.433
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.364
- ___CARHandleSuggestUI_block_invoke.429
- ___block_literal_global.428
- ___block_literal_global.438
- ___block_literal_global.646
- ___block_literal_global.751
Functions:
~ -[CARSession carOwnsMainAudio] : 72 -> 224
~ _sessionUpdatesQueue_endpointNotificationCallback : 3772 -> 4112
~ ___sessionUpdatesQueue_endpointNotificationCallback_block_invoke : 216 -> 192
+ _CARSafeCast
CStrings:
+ "Car entity has main audio changed: %@"
+ "Car has main audio for video playback"
+ "Car owns main audio for video playback"
+ "VideoPlayback"

```
