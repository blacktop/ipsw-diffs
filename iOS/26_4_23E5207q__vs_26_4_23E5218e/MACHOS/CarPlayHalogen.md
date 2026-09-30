## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-940.19.1.0.0
-  __TEXT.__text: 0x6f68
-  __TEXT.__auth_stubs: 0x570
+940.21.1.0.0
+  __TEXT.__text: 0x7430
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x118b
+  __TEXT.__cstring: 0x13c6
   __TEXT.__oslogstring: 0x93
-  __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__auth_got: 0x2b8
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 9479213F-6039-3CC5-9C88-EA22AC585A04
-  Functions: 148
-  Symbols:   129
-  CStrings:  106
+  UUID: 89D1D57C-C668-39E4-BA07-180BDFB8D906
+  Functions: 153
+  Symbols:   133
+  CStrings:  116
 
Symbols:
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
CStrings:
+ "%s, isUnplugged=%d\n"
+ "Boolean carDevice_HasProperty(FigHALAudioObjectRef, const AudioObjectPropertyAddress *)"
+ "Boolean carDevice_IsPropertySettable(FigHALAudioObjectRef, const AudioObjectPropertyAddress *)"
+ "HALCarAudioDevice-%@ ID %u EndpointStream %{ptr} Finalize enter\n"
+ "HALCarAudioDevice-%@ ID %u EndpointStream %{ptr} Finalize exit\n"
+ "UInt32 carDevice_GetPropertyDataSize(FigHALAudioObjectRef, const AudioObjectPropertyAddress *, UInt32, const void *)"
+ "carDevice_GetPropertyDataSize"
+ "carDevice_HasProperty"
+ "carDevice_IsPropertySettable"
+ "void carDevice_Finalize(CMBaseObjectRef)"

```
