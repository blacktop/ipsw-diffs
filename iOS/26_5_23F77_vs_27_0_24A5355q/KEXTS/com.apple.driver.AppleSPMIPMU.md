## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.120.2.0.0
-  __TEXT.__cstring: 0x28ca sha256:a3f1d663119da8075305d6b29c7a34f0ee023653eb23fc694fbb9aecf11917cd
-  __TEXT.__const: 0x26 sha256:19f9c6b6744f60c830f0f2c99ec57d3120f26f14838ef45127535dfec5d7c7cc
-  __TEXT_EXEC.__text: 0xc024 sha256:2729eb97c1f53413e53a8c5b03ece69a39313a482790bce2473175181fc31258
+1371.0.0.0.0
+  __TEXT.__const: 0x36 sha256:047b62f33df4528e335780620dbb0bcdf06f9df5861d6ea469a3af4008f26de3
+  __TEXT.__cstring: 0x2bd8 sha256:3b77aac85fe9b1ac8ea455c5496ddb3646e42c003a67849249c8da86dcf14cc7
+  __TEXT_EXEC.__text: 0xcbe4 sha256:82618cdcd28e37db79f992c4502f9e9321195d9acd9071a26f9ddfb55d2cb8a9
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x320 sha256:d3a993b5a6b31e7e93e41fe95c2eb31b130119e1e0797d44cb2f576ca510ea90
-  __DATA.__common: 0xc0 sha256:5d89f056865052bcb89c910d2d62872e029fb273c3db03f8968a52a41593c1b5
-  __DATA.__bss: 0x138 sha256:6287e17fe5efcb191aec8a2578e685d0a1040a0ab53bd1f02c7f49cc6c8fced7
-  __DATA_CONST.__auth_got: 0x248 sha256:750a9f799f82da8e1b2a50fd2ef5e702c41ba9c1a85360ecd8b822053528dd2b
-  __DATA_CONST.__got: 0x118 sha256:0967d9e4b6017b6667f30ab07e34b07d145fb4d09048a3f28a598088256f66aa
-  __DATA_CONST.__auth_ptr: 0x10 sha256:e14ca65f8503058fc04f7cb81b35858b9717d07dfda9950a7b133d608569cdcb
-  __DATA_CONST.__mod_init_func: 0x10 sha256:90cebcddc644cbea71e3aec489e066bca6ca48b3ab740360265c6dcb17d5fcb5
-  __DATA_CONST.__mod_term_func: 0x10 sha256:cfa52a7c1d129d6e5b5db52c9cabb2bfe4e0bcd2d9a5f6299e20e1a5eccdefe9
-  __DATA_CONST.__const: 0xf00 sha256:fa0d1db9823f81aaaff77b841bb267b7ad5e921a6a038c1256b8b93982be4682
-  __DATA_CONST.__kalloc_type: 0x140 sha256:790cc813fc40de23de8626c4f0f5ebecb12268c6946c851c1e92998defa046ce
-  UUID: 1FEA728F-AB0F-3C16-BDB8-59BA71815F21
-  Functions: 167
+  __DATA.__data: 0x320 sha256:2a67cc9643c16922f19b2f8734dbf33b3f76b99887f60483681ed2d7bd6b22df
+  __DATA.__common: 0xe8 sha256:c4fcd50d9f0c893c46288b57d8e62b18523145956b249b6ecd6c21718be49065
+  __DATA.__bss: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
+  __DATA_CONST.__mod_init_func: 0x18 sha256:147338866d0fed499d20d75f64ba1a78b3b5b09752126c621b197d80d30d5729
+  __DATA_CONST.__mod_term_func: 0x18 sha256:d566fe26d3a34858397651e6d6e62086ded0267044a6a366c5ae4eab21d6529a
+  __DATA_CONST.__const: 0x14f0 sha256:e60a95fbd5aba4e33a93f3abc22e2725056d035629d038dd771955e229932808
+  __DATA_CONST.__kalloc_type: 0x180 sha256:0496b7130b3163a5df611dadc7ad27f06780cd27fcff50e8681a6f73b3d824c0
+  __DATA_CONST.__auth_got: 0x268 sha256:4acc3f35e4b3bf6dd3689642367b9875956d2f8cfd4b7d2d22ab1b9eeb820391
+  __DATA_CONST.__got: 0x130 sha256:4f3b46209e08af712c242b375043b4718b1d94455acef4af0fe6b4afc9a502a0
+  __DATA_CONST.__auth_ptr: 0x10 sha256:ab5fcee021ffbec36df127a694fcbd72f379ebb5cd3514ac7adbc2af4e3c13f0
+  UUID: 71B93739-AF80-3B7F-8D2D-D861C4D1B13A
+  Functions: 192
   Symbols:   0
-  CStrings:  359
+  CStrings:  378
 
CStrings:
+ "\"UPSI test panic in PMU kext at boot stage 0x%x\" @%s:%d"
+ "%s::%sAppleDialogPMU:: Enabled MCURST (info-has_mcurst in EDT)\n"
+ "%s::%sAppleDialogPMU:: No info-has_mcurst in EDT\n"
+ "%s::%sAppleDialogPMU:: info-has_mcurst in EDT but function-arm_peripheral_reset not specified\n"
+ "%s::%sArm of Peripheral MCU Reset failed\n"
+ "%s::%sPMU-LPM: Unable to write phra LPM log (%x)\n\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 22:46:09 May 27 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 22:46:09 May 27 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 22:46:10 May 27 2026\n"
+ "%s::start: %s _pmuNub: %p built 22:46:10 May 27 2026\n"
+ "/chosen"
+ "12111112122212121"
+ "1211111212221212112222222211211111122222212111111212222211122"
+ "AppleDialogSPMIPMU: UPSI injecting action 0x%llx at boot stage 0x%x\n"
+ "AppleDialogSPMIPMU: UPSI injection configured - stage=0x%llx, action=0x%llx\n"
+ "AppleDialogSPMIPMU: Unknown UPSI action 0x%llx - ignoring\n"
+ "AppleDialogSPMIPMU: pmu offwake\n"
+ "AppleDialogSPMIPMUNub"
+ "IOPMURequestMCUReset"
+ "_handlePEHaltRestart"
+ "function-arm_peripheral_reset"
+ "info-has_mcurst"
+ "injection_action"
+ "injection_stage"
+ "site.AppleDialogSPMIPMUNub"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:24:20 Apr 23 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:24:20 Apr 23 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:24:20 Apr 23 2026\n"
- "%s::start: %s _pmuNub: %p built 20:24:20 Apr 23 2026\n"
- "1211111212221212112222222211211111222222121111112122222111"
- "pmu offwake\n"

```
