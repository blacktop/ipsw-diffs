## integrator.dylib

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/module/integrator.dylib`

```diff

-28.0.0.501.1
-  __TEXT.__text: 0x114c sha256:b8903e37455a601119136c02aeb8b3cfca73d075621d421b4f4814808706c7a3
-  __TEXT.__gcc_except_tab: 0x158 sha256:fe51a9912508b28c78354978e4eb6aa8c5a68cffe71d435e6f7ad398481ece26
+28.0.2.0.5
+  __TEXT.__text: 0x12f4 sha256:60ff6b17e9cb057235878dca0d5a7b9afd09f35d934d4ddf7a4c3a75ed5c542a
+  __TEXT.__gcc_except_tab: 0x188 sha256:d3341de518e374d22b05e04022805f9114e821f688fbadf4e4e12e65069ce772
   __TEXT.__cstring: 0x214 sha256:a9490c8199d18964d7883f598319060649cfef96f9379d0f60e31cb8dee09c69
   __TEXT.__const: 0x65 sha256:d0f354bf85e7bf82aed69c23628fe262040d750570dbee4f9a0782e1d54398c9
-  __TEXT.__unwind_info: 0xc8 sha256:752d3fd41e38ab0c44e4c81475687e7ae47000582ba1bae0d429ef735ca79dac
+  __TEXT.__unwind_info: 0xc8 sha256:c409b3fbe3a9772c42a65f419ca39ea0d12406337677d474c432416ca65acd4c
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x120 sha256:a3b56dd91db96407188475712c3587cfc6e2230163daebcdba118082532f5c3a
-  __AUTH_CONST.__weak_auth_got: 0x20 sha256:b7a04fda26841a0040c3791c7f7affdc0629031506fbb84d682fccd222e021f0
+  __DATA_CONST.__weak_got: 0x10 sha256:eb1e1f490f4b00eef10bbb284ac072d78ab0e27c8f32419312f4952bf6d229d0
+  __AUTH_CONST.__const: 0x120 sha256:b7ed91b94a02b8e2e6d77a33ba455c94ed130c7fc4a21cdbd5b4f60ca4da1a8e
+  __AUTH_CONST.__weak_auth_got: 0x20 sha256:396e67293ba6b13027ef3965f36dc8d7505225f73159bf94255b9e4c198352ac
   __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0xd0 sha256:46f531b7ea0428fbf2c3ca2b60e8dc33d6bbfa000e0fd1b489c5e39140a47006
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
-  UUID: EAEFA043-2102-3544-BE99-BE14FEC19888
+  UUID: CA5420C9-0494-3B8D-9379-625BC7DFBC3E
   Functions: 17
-  Symbols:   75
+  Symbols:   80
   CStrings:  11
 
Symbols:
+ __ZGVZN14CoreLogHandler12main_handlerEvE18s_main_log_handler
+ __ZN14CoreLogHandlerC1Ev
+ __ZN16ModuleIntegrator14s_event_objectEv
+ __ZN16ModuleIntegrator8s_modelsEv
+ __ZZN14CoreLogHandler12main_handlerEvE18s_main_log_handler
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
- __ZN14CoreLogHandler18s_main_log_handlerE
- __ZN16ModuleIntegrator14s_event_objectE
- __ZN16ModuleIntegrator8s_modelsE
Functions:
~ _on_register_module : sha256 2c3b8e31a2c84fdf25c1fa91f479d9436e3614c12ff685a81e19e4e928b2b564 -> 78ec659b938a9b9b082df27b68f2d9c28c8a4390d75f1490adf877d7b401381d
~ __ZL10create_cmaPK7CtxEval : sha256 1af48848e927894773ca0be7f10379c6fe84bf753f2993d92d46246c74486876 -> 1541bf9c457338878250526091c62b2635afdb0cf56ede0295038a256f417515
~ __ZN27_ModuleIntegratorCallbacks_13create_moduleER8OfObjectR15OfObjectFactory : sha256 705ade9d8f707889630d2f3a5c1f8c44f476a51d92e3715535f24c797f9f5804 -> 4c874da8103a0ebea3caeacab750af0163d05c362101e797725da7d56b4a26e6
~ __ZN27_ModuleIntegratorCallbacks_17on_modules_loadedER5OfAppRKN11EventObject9EventInfoEPv : 784 -> 944
~ __ZN27_ModuleIntegratorCallbacks_21on_preferences_loadedER5OfAppRKN11EventObject9EventInfoEPv : 2156 -> 2436
~ __ZN13CoreLogStreamD1Ev : sha256 266c347355ee5dcde56305039869d8b5aafb89f34442baf28b7ba4a7d3275b34 -> 4d2457e90e0a1fdbee3ddc1e8fe75a549d54d141bbc608c5d403dc06f7720643
~ __ZN9CoreArrayI10CoreStringED1Ev : 128 -> 112
~ __ZN27_ModuleIntegratorCallbacks_D1Ev : sha256 b033f2c4ad4e991285e15ea8c77ef15733d65a7c81b98d3d81773d9e25c7cdca -> 2b6db20655ff7e1bd2b03731873fc24f776d8949f8cf17ac61e8319cf84584dd
~ __ZN27_ModuleIntegratorCallbacks_D0Ev : sha256 735f2cfe44968e7a56b3186279f49395245902c3f5202f583be0edb0068059e1 -> 912990539d507248f3b29f25dfd47e900d5a615fd1baad76e23309abcece5493
~ __ZN25ModuleIntegratorCallbacks14init_callbacksER16OfClassCallbacks : sha256 806650b5d3df50bf262499001b51b1f0ed7da5bf1c2cc11eefd2bab3b18e44e3 -> 998e1c4422d7a4375c3bb82d721605e39743bf97c2d871433c9a7cce19b0f41c
~ __ZN13CmaIntegratorD0Ev : sha256 0597e67b3f9e89037f188b3abb96b3a6c05276e692cff873b77e4357cacf4967 -> 9888aaada03fbca24546756094118f527a33aeadf6f590c8018d8580991e40b8
~ __ZNK9ModuleCma14get_class_infoEv : sha256 1e76dd2695ea9abf7b00f886be6992123dbf4351d9fd0476f7edf02ce4a2f993 -> 10ae66f720e0730bebb21ee66f30e9a8b68db0b85c5c33a521ac6facf1168e5a
~ __ZN13CoreLogStreamD0Ev : sha256 70d5ad6e35122a550d58770345bb5ee804b95a4e1b600c85d69d0653452c3db0 -> fa6f9f81166e9ed405b5ab2823912afc6d06585ba8a21780b99be4feb11b721e
~ __ZNK13CoreLogStream14get_class_infoEv : sha256 065943c8ed9d538a0d6e6217b39ca3107551f87b727a23469a20ecca875bbce4 -> 01e2b4d45f94bd86efa44bce427272897458ec8f20b3ac619e0eb7980a10d8dc

```
