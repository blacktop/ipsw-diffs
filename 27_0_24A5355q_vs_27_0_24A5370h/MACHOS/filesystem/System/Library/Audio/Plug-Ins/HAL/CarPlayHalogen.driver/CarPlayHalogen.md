## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-980.58.1.11.1
-  __TEXT.__text: 0x7210 sha256:7fa2a5cb99f817e01ac7bebb49a091dec1bbde39439a5026fe4d65bee17534f3
-  __TEXT.__auth_stubs: 0x5b0 sha256:7b055b277403838c102df7cd4c167bea92fe68d166e32f551e25e0631d4492e9
+980.63.2.0.0
+  __TEXT.__text: 0x7478 sha256:b9ffd50de506ce537a0bf5bd070d532061f2d2b88e2e1f2d70a75f82269908c6
+  __TEXT.__auth_stubs: 0x5b0 sha256:999bc24de7b0a1e2c983bb614679de172761aaa6130a1e7c5741e7a712b87ceb
   __TEXT.__const: 0x90 sha256:32a8fc2b729494d6b14878bd8d9f6f7a73adeb85bc74c8c8ac3d4715a836ed0b
-  __TEXT.__cstring: 0x1235 sha256:22b90187ea34a3c61d63b2ca3b25449cf8c22e8546a9566f98873e1624a92fa7
+  __TEXT.__cstring: 0x132a sha256:4117835c48ea84be875280d0cc12b6b499c05d096a1c22068ed5cc1d976ee5b3
   __TEXT.__oslogstring: 0x93 sha256:1e034f8de245a2c28ab79cf2097b64437751e2deb191c0758308dbae1d18f12a
-  __TEXT.__unwind_info: 0x1a0 sha256:59f5652c731b57e006c50152427ea8e79a034c35cb093f93b3e64671fc34c3df
-  __DATA_CONST.__const: 0x2d0 sha256:fb96bbd17a2528868513fb3477983c8ef8896be48bc6f5506ffe9e21d2eeb176
-  __DATA_CONST.__cfstring: 0x60 sha256:a5cf8f01e9741854ea422bd02b7270bbe0ef7e8549c1a4df59e278cc3af8c8c5
+  __TEXT.__unwind_info: 0x1a8 sha256:4ef699e7096f266e8d4280177d619f3069d9999a05398c360b816c620f9f7634
+  __DATA_CONST.__const: 0x2d0 sha256:51684f704bd45aa2b32195c0bd10b4604876cc363612584ceb9486fcc5e833ff
+  __DATA_CONST.__cfstring: 0x60 sha256:a7ee8a058f635edaf96546005de477c3e14851ea883d8ba2f6754d39fba0d249
   __DATA_CONST.__auth_got: 0x2d8 sha256:c14db2ffeda92ddcf1928449341c732cc2c0f60272edfc5177686f36be5f8ab2
   __DATA_CONST.__got: 0x118 sha256:c125c17ef11e64c15ab2f75f7629bb4a7fc183c4351282d41f9d4f85a863b2a4
-  __DATA.__data: 0xe0 sha256:3d6f5f21f07b9414db48154e9f6430696a0f0da525579964b12285fb70696ca8
+  __DATA.__data: 0xe0 sha256:61aaa84c62f820a4b96c44368bb4ccb885e43f130606727c65fce69bdfcd253b
   __DATA.__bss: 0x8c sha256:24045c10c12a89f4c11e3b88ea34558fcdf926a8c1008cd08cc33bc71407c774
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: B7F1B2C7-D229-3785-8204-9D695C0933A2
-  Functions: 153
+  UUID: A0438E23-516C-3322-B510-07BE13FEC87D
+  Functions: 157
   Symbols:   131
-  CStrings:  109
+  CStrings:  114
 
CStrings:
+ "HALCarAudio%sStream-%@ Started\n"
+ "HALCarAudio%sStream-%@ linked to audioSink %{ptr} \n"
+ "HALCarAudio%sStream-%@ linked to audioSource %{ptr}\n"
+ "HALCarAudioDevice-%@ Stopped HAL Audio; error %#m\n"
+ "HALCarAudioDevice-%@: startIO completed with error %#m \n"

```
