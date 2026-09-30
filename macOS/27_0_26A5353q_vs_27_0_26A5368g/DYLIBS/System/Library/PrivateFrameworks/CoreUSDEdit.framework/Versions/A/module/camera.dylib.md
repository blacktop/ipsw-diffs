## camera.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/camera.dylib`

```diff

-28.0.0.501.1
-  __TEXT.__text: 0x156c sha256:ed672212d4141ec1d50bc5f0f194ce7fa79f02e595679af35f2b8066c09d9f4f
-  __TEXT.__gcc_except_tab: 0x3c sha256:ea4a651a87694c7e5ff678698bcb376afdd35122de3497c893a44e6a99ee4ec8
+28.0.2.0.5
+  __TEXT.__text: 0x160c sha256:223565ff31b6ae3b48b750567a2e24b8b82ca3122cc53c6123a02ddaf1303f6f
+  __TEXT.__gcc_except_tab: 0x48 sha256:35f89a3ee79c2d6433b3aff8f8d71e38ac9914a970a3c9e355be4bcb5e9ff0b3
   __TEXT.__const: 0x10d sha256:4c70fde0e79edbbd320cc8f8f881c4c8630c11574e9ab4cecadc9894f5e294ce
   __TEXT.__cstring: 0x91b sha256:a585013d2ed94897f2d6cfe65dd78a3728b1c3e65a434f552842cb6358593c3f
-  __TEXT.__unwind_info: 0xb0 sha256:25d19e87d078efeda370915cfc055186210318c096198ef3056da912c9b6c9c2
+  __TEXT.__unwind_info: 0xb0 sha256:b20a4b354fd7aad68b5d77986bb35fe4e90f4eda3b54c18b9e9a3ee5d13aac3f
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x150 sha256:fa58a0b86562f271910f78e74b95741b6070fcfc069f37b29082cb74ec358b93
-  __AUTH_CONST.__weak_auth_got: 0x20 sha256:b7a04fda26841a0040c3791c7f7affdc0629031506fbb84d682fccd222e021f0
+  __DATA_CONST.__weak_got: 0x10 sha256:f6722cd599336f0dfba455b7fd21d99886ecb7d8c8fb57198b8a17d8be561233
+  __AUTH_CONST.__const: 0x150 sha256:855f722d7828ad522311f30edd69ba09425f151fc7c93d7243aa763f18806d1d
+  __AUTH_CONST.__weak_auth_got: 0x20 sha256:396e67293ba6b13027ef3965f36dc8d7505225f73159bf94255b9e4c198352ac
   __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0xd0 sha256:46f531b7ea0428fbf2c3ca2b60e8dc33d6bbfa000e0fd1b489c5e39140a47006
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: 105B2F72-9364-308F-B891-6087075EC4BF
+  UUID: 713AB808-B612-353E-A5FC-448DD75AA274
   Functions: 15
-  Symbols:   70
+  Symbols:   75
   CStrings:  36
 
Symbols:
+ __ZGVZN14CoreLogHandler12main_handlerEvE18s_main_log_handler
+ __ZN14CoreLogHandlerC1Ev
+ __ZZN14CoreLogHandler12main_handlerEvE18s_main_log_handler
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
- __ZN14CoreLogHandler18s_main_log_handlerE
Functions:
~ _on_register_module : sha256 2c580df7b7efa7609bbdaab8cebbd22625bb3767b1611a5a70a3bb2ffe7d897b -> 4a4b4ba82c550593dd36e8a35228d5b30e2980a5e1a03936e433ec55c589906b
~ __ZL10create_cmaPK7CtxEval : sha256 fa31587479e04ad6588cbe9bda1352fd98c4fa4fa7e8140b9e7d7d78a53989d4 -> 3deea59237c47beced124710947aa59fcd3eed32fab703e5f2bf05b7e5981d5f
~ __ZN23_ModuleCameraCallbacks_14declare_moduleER8OfObjectR15OfObjectFactory : sha256 eff7a053fb978603a607b3428d72866038deba54f7490bd7f7abecd48f6f1bdf -> 886d60fc9574d0d25a6cb8321133198706631eb4e3c2de5f972ba280797c1f02
~ __ZN23_ModuleCameraCallbacks_8paint_glER8OfObjectR10GlUtilsCtx : 304 -> 464
~ __ZN13CoreLogStreamD1Ev : sha256 6eb9d3edc46a1caf1be1162ffde41cf95a8d17c87027f4268b6c6f3ac65e0445 -> 1c3365d23b848b6f750ef454c30ea6e72df8609c8e7f6d14ded5e3dfb2a752ed
~ __ZN23_ModuleCameraCallbacks_D1Ev : sha256 48cfda91cd45e2874dcdd58d36d4f55b7513acacb45e2ed285bf7238100855c4 -> cf08443d0d85e89ed67019d6c60578f8ad0edb97aa4b85edfbc7ecf48830bb60
~ __ZN23_ModuleCameraCallbacks_D0Ev : sha256 1db7b37b8ec786420f9a8b4dd365569c6b6770ed17ea211dde6a9c44680fb18c -> 2e9686c1f1122906e875d1a735f63caf9b3c991c7dea21c09bba6e34e378ab3b
~ __ZN21ModuleCameraCallbacks14init_callbacksER16OfClassCallbacks : sha256 bcb7a8ed41422f6348eb0d9c7d4bb8a1d66216413e0fe094427a2e17fa73128d -> 04c181a8bad15a6efc39e3b91ec09714fd4394f8c2181bcf5bc7fc7babb0bb47
~ __ZN9CmaCameraD1Ev : sha256 4c26b8a0cff12e6ec861866a2d20e3e578b197d72abe713011f02fe9f8e1ea31 -> 831f0f91779439a06fe36f528bd93e720d130c912ad53d0a96109508192e4a13
~ __ZN9CmaCameraD0Ev : sha256 b3b8acb764fe2a49c242b3270c81415aea1a1146b61b027619cc38a636c936e0 -> e369ce358a692b80a535ae302da12685f142ef1c067cb870cc0bf70c2f37bde5
~ __ZNK9ModuleCma14get_class_infoEv : sha256 5e24b347b0849fe8591d39279c7d3bc4c7b898d84cd192a41c1f3aefa5f7947e -> 91b513cc48fb088fcf11ed7341bead8bedd68eceb3269b2a1cbc38e6a885c158
~ __ZN9CmaCamera21sync_attribute_valuesERK8OfObject : sha256 6a1384e40a98acd230b4278d26a70284b9515d31f0b0d9132a3c7aba089954c9 -> 07cb9ff1de92f8f9ea587c917c12ed1eb69c28038a89c4a5ba20a8e5446b9560
~ __ZN13CoreLogStreamD0Ev : sha256 49c0340e0f91fc68bf5eb31526283528123d47da59ec92ecab1a49794ead6fb1 -> 53bfaaa6c8bedbffc637dc33d96903458a4053545806922c5a8d0a5f670e9b46
~ __ZNK13CoreLogStream14get_class_infoEv : sha256 522b96dd8c7f64968164e4e6fb360083766612879bcf6c8fe40b745485c87f94 -> a490ea0eeac15eaa0a60d606b8d14d22e2bc58f5db694e91e96227d47f09afbb

```
