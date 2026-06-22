## lpe_constant.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/lpe_constant.dylib`

```diff

-28.0.0.501.1
-  __TEXT.__text: 0x9d0 sha256:a5922bef1997a798134ff30e13fafa119ed6939ee94619b7fd9a76fed82dac79
-  __TEXT.__gcc_except_tab: 0x54 sha256:3d065b00ba7bd36c76db396d69e0cd1dfc12f68f664a011c9a441e3638e29e95
+28.0.2.0.5
+  __TEXT.__text: 0x9e0 sha256:a320d9298249f0e0deb1e3dd7b8fc3d776dc4c20b02fcaeef8e4a80392102f17
+  __TEXT.__gcc_except_tab: 0x5c sha256:9fbfdb131961979420f1f5752c8a118e0d90949783583b300a72ac79cb069948
   __TEXT.__const: 0x78 sha256:ead24ce802d8ccd90b9b071c06af44dd9bac0e2d534853a28c10d28cfb653d95
   __TEXT.__cstring: 0x36d sha256:88469976af83675dd04ab6de1070ca9d20cd07924c2867757d2c362fc1be0b35
-  __TEXT.__unwind_info: 0xb8 sha256:49b0bba9e31b607f789af1635a6c141462ea5b20d634aabf14dbf9fa3d12c460
+  __TEXT.__unwind_info: 0xb8 sha256:9fd50bb7433f58626a0cb7d66e41ced9de18bb2d0f562ec39cfcf1f6ae5d620c
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xd0 sha256:8c13d17bda25e71fa0e9fc43f1ed78c0368185716971185fb36e3cf4f54ceaf0
-  __AUTH_CONST.__weak_auth_got: 0x20 sha256:b7a04fda26841a0040c3791c7f7affdc0629031506fbb84d682fccd222e021f0
+  __AUTH_CONST.__const: 0xd0 sha256:8a067c7211a01c488d7c49e15df160fd12c559b7179eba758ea9767ff324f2e6
+  __AUTH_CONST.__weak_auth_got: 0x20 sha256:396e67293ba6b13027ef3965f36dc8d7505225f73159bf94255b9e4c198352ac
   __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: FDB1D339-5DEF-3586-945B-5F459FCD246F
+  UUID: 72284E15-F6A4-3840-8643-F83B5B0CD6D8
   Functions: 15
   Symbols:   58
   CStrings:  3
Symbols:
+ __ZN12UniqueString5emptyEv
- __ZN12UniqueString5emptyE
Functions:
~ _on_register_module : sha256 adc24a0e6f0fe671840460ca612218da27950ce22a409bbb369ee8952c91a262 -> 00c31674e436c9b94e7c715131d11758f703414c98195d8f1e0c6bd72667dfca
~ __ZL10create_cmaPK7CtxEval : sha256 934f12812fde55bc4967fe37cd6d6a60253f4db159ce2f333b9f0024476e5513 -> dda46bb4fe8e2f40850458f0552f97fa3261a87871f0a399abc2c71cc7f18341
~ __ZN28_ModuleLpeConstantCallbacks_14declare_moduleER8OfObjectR15OfObjectFactory : sha256 2c7fe0e81c03fb1d216f37d8829d93f61c8d9110d0c820d2a1a2f7338aafc90c -> 542157fe82c6be2e7f60efda0d4fc6bcbb3a3ff2970b7471b45842920a0453bf
~ __ZN28_ModuleLpeConstantCallbacks_18create_module_dataERK8OfObject : 408 -> 432
~ __ZN28_ModuleLpeConstantCallbacks_19destroy_module_dataERK8OfObjectPv : sha256 b977c7b80942c837ff2ce0e472443c8c8310fa7a272b7c66a6c7e31f0d00dc42 -> 543c2b70ce865372e1548986cc7ee0b3b8acda8483d31a260bb9896436c53c60
~ __ZN28_ModuleLpeConstantCallbacks_19on_attribute_changeER8OfObjectRK6OfAttrRiRKi : 236 -> 232
~ __ZN28_ModuleLpeConstantCallbacks_21get_lpe_constant_descER8OfObjectR15LpeConstantDesc : 116 -> 112
~ __ZN28_ModuleLpeConstantCallbacks_D1Ev : sha256 e23e656a095330360f969623f3fa5b5f7b108196c591fb60fda1421ade52040c -> fd994e9df504995cc2634d9acd7f6dec52cb090f6b37dd9c509372eefcade782
~ __ZN28_ModuleLpeConstantCallbacks_D0Ev : sha256 666861e982ba3852890e1a4fe1355d1b1bcf82856a8a76d4a73cce29d1917317 -> 6160505cbda75687f0ad25d43daec5d6f49def5ba81f4b5fead22e1020a96c4b
~ __ZN26ModuleLpeConstantCallbacks14init_callbacksER16OfClassCallbacks : sha256 8e747073121e8277241f471a0afe133256b8f9b985c0bc2a7374ab13d5b30b56 -> b8a25fa4fc868d3b15311929d33050ccacd25c4ebefc48e3ffa0520479e5f745
~ __ZN30CmaLightPathExpressionConstantD1Ev : sha256 967832bdedcbc9604a96c1fe6411d141dc801307e2e994c4920887fca44998bb -> b71a23336c950d709a54bf0c60dee85ead31df6a573f19e80b755d9464ba32bb
~ __ZN30CmaLightPathExpressionConstantD0Ev : sha256 96dec4ee55294be16c3c7e496f68a11f081e7d9cea38d3f3f3b49e8822e81d8a -> 99dbbb28c0dd5572cb6665def6fdd5fe335e0fb65379b1c4c23fe926b76dc566
~ __ZNK9ModuleCma14get_class_infoEv : sha256 780663bcf7fc3194fe99e86743ee4309ce61c228493693571fc168328a1fb4ec -> d54cc1aa22ff54b5fdf889272e22256e4177304fa0b8af0939b8e945b5b89217
~ __ZN30CmaLightPathExpressionConstant21sync_attribute_valuesERK8OfObject : sha256 ed4d01726dac193cacc2b7ddd91f3860408e9ce74d6e71398c519c126b7dbdea -> 5ba5bc4169a50051be5cd9b1963bceb33d16ade4a625613e030930092d9a50be

```
