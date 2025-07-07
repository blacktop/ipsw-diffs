## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-890.66.3.0.0
-  __TEXT.__text: 0x7270
-  __TEXT.__auth_stubs: 0x560
+890.68.4.0.0
+  __TEXT.__text: 0x7300
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x118b
   __TEXT.__oslogstring: 0x93
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x1b0
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0xe0

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: F965FD5A-8334-3CDF-8D51-E3AB23A983AB
+  UUID: DCCE43B0-BD39-32F6-BDA6-B84C3DCB6447
   Functions: 141
-  Symbols:   127
+  Symbols:   129
   CStrings:  106
 
Symbols:
+ _APCarPlayAudioFormatInfoGetStreamType
+ _kAPEndpointProperty_ReceiverModifiesMainHighLatency

```
