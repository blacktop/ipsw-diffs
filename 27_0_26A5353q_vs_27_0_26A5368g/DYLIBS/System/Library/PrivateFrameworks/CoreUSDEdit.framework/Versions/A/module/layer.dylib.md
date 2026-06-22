## layer.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/layer.dylib`

```diff

-28.0.0.501.1
-  __TEXT.__text: 0x266c sha256:d11f1d0b766fbefa314a2dc24a3741b7e8b53d3242ced627dd5d12575b5d83ba
-  __TEXT.__gcc_except_tab: 0x1e0 sha256:e45c1387f4c428059f3697f19c9481dae4364319f908b11b48b4f968120d3b41
+28.0.2.0.5
+  __TEXT.__text: 0x2644 sha256:ef9d3cc9f7aef0cb0d51cfbb3fc759281f70ee61bea08096e6e4a9ffd89311de
+  __TEXT.__gcc_except_tab: 0x1e0 sha256:06f794877cdb4f8f2ede8d688ab55c74bee1aadde526a2d23f76b23537b579b3
   __TEXT.__const: 0xcb sha256:81901d155b5d7b6d353e2f9dbe00e6b7e89c570661346d921ace5050c65e8a64
   __TEXT.__cstring: 0x2a25 sha256:36ca430ceae730673d39458d957eed6c3ea789d9f368bd8aad28613e83ee5804
-  __TEXT.__unwind_info: 0xc8 sha256:dd60b33a347861841a797ade3c881e930f1cca2cf9e987061d7c3a7e3e458c2c
+  __TEXT.__unwind_info: 0xc8 sha256:989e731abac414c095592540465dc71769e66e3d5da11279c3a0ccecb710650c
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xd0 sha256:7f2fcf82deeb92e73c1829d1c7ab3f46a7d200d92af77f9efee545570eceb627
-  __AUTH_CONST.__weak_auth_got: 0x20 sha256:b7a04fda26841a0040c3791c7f7affdc0629031506fbb84d682fccd222e021f0
+  __AUTH_CONST.__const: 0xd0 sha256:9a1c863c3556151a7d16a7933c90f5139a912d82a5f72cd3f9e417bf38130f53
+  __AUTH_CONST.__weak_auth_got: 0x20 sha256:396e67293ba6b13027ef3965f36dc8d7505225f73159bf94255b9e4c198352ac
   __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: 3889D243-B0FE-3116-94B1-0D11E2E2E440
+  UUID: 96B285D8-CFD7-3564-9307-16091B53CD29
   Functions: 14
   Symbols:   93
   CStrings:  28
Symbols:
+ __ZN7ColorIO34s_default_scene_linear_color_spaceEv
- __ZN7ColorIO34s_default_scene_linear_color_spaceE
Functions:
~ _on_register_module : sha256 b02aca70133a6df1c23b95ed457d3a9ca6b57c8d1911b5f7f471621776ff9809 -> 1a3cb45890d3c88a389f9da4cdb94982a0ecff288485de253ab7ab87af58c714
~ __ZL10create_cmaPK7CtxEval : sha256 22bfff1ffa56cf56cda5f03d77bcc9642e7ed637f20cc1c733eb532c067f023f -> e09198356ac09766dade7328a0d561b34bf9ed6ab7dddce42cf9d7df7fc9b09a
~ __ZN28_ModuleModuleLayerCallbacks_10init_classER7OfClass : sha256 1f74763e9fb38c6cefe72d0f3df704f03bead48a58aa1902cf7c4ec9de792868 -> 27680a892eb187aadef8a464f6bd0952f043214f640f388a726a32648dc3d64a
~ __ZN28_ModuleModuleLayerCallbacks_19on_attribute_changeER8OfObjectRK6OfAttrRiRKi : 1192 -> 1156
~ __ZN28_ModuleModuleLayerCallbacks_18module_constructorER8OfObjectP8OfModule : 1548 -> 1544
~ __ZN28_ModuleModuleLayerCallbacks_14declare_moduleER8OfObjectR15OfObjectFactory : sha256 138026991b2a6380ff63e4eec738bd771e0f0ff29120a25de4a4c7fe2bad5864 -> 1c97cc20a89cd2ec51c344e4f0590f77afd1a324231fe7596f5c0f66ad1ee5af
~ __ZN28_ModuleModuleLayerCallbacks_D1Ev : sha256 a2007f30b8bf002c19e276302a7c2c989292c0ead92d8eb797044aff36d791f5 -> 911bc32ef7909e76dcf53f864b248eb6dafa610881f30ca7182b4fbac7777443
~ __ZN28_ModuleModuleLayerCallbacks_D0Ev : sha256 4561bf2bf473ce775efe434390beba68d11d40f16b5f366269fe2a7bc799584a -> cdec5127a3e36205f6ec22a6a99ce051f4f9faf2ed7ceb84b980166bfb9ae6d1
~ __ZN20ModuleLayerCallbacks14init_callbacksER16OfClassCallbacks : sha256 df6c35581d65cde0e34706b6863e15e3ef9c4abc38a72f028ccb157e02151adb -> ce2cc38bcb56d940b435af1bb749f643099cab24cfba85dba1b2862fb3ac99e7
~ __ZN8CmaLayerD0Ev : sha256 d237698a2d7e52ca2c6a4cd189ba486d67926de1141e317fc19243af91e62dca -> a7de5240fd2ecf5b1e30c81f98c6c98df1ca99797c71e4657f48ca237c164362
~ __ZNK9ModuleCma14get_class_infoEv : sha256 1da4121dc55cbfe99747036aba2010ebded47529cff03267b96def0007464621 -> 29e94484466ea3dda145e89efcbf6b53a2d7ebd99200d7c6178f2ed565ab7e9e
~ __ZN8CmaLayer21sync_attribute_valuesERK8OfObject : sha256 91cbe7252d7b0f9a4c1dd9082d1a7f9058387cffc52054ce0370ada8266da0e1 -> ca25201cd8254452d4dfe36fa43d22319ba05ea547acd2805fe09e2a5aebf6b1
~ __ZN8CmaLayerD2Ev : sha256 ff3a7d11afb7f79e6f15640d1c4f82c620ab809a8c4780d29d9b2b37b276896c -> 725fc142481171f415c21263c437a1e69e6c882625270941d863ab87a5555273

```
