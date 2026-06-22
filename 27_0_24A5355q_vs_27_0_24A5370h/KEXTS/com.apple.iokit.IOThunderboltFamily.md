## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6832.0.0.0.0
-  __TEXT.__cstring: 0x4adb4 sha256:4057791724cc8146811c8b6e71f24437f381bb61cbd102ee420cee0582167be9
-  __TEXT.__os_log: 0x3be20 sha256:d4d94ed0ebf165b28a7dbd389e484df17a7b50d170134b49272e94041e11f066
+6834.0.0.0.0
+  __TEXT.__cstring: 0x4ad99 sha256:363782e5f88f0819d191a6425f0f5667e5d93e84ec7e0dff305a62a8990ff33a
+  __TEXT.__os_log: 0x3bd4b sha256:0fa0eb378252ea027352c32ffd1b509e4cdd1bf9a46678b25054c6a5df131c88
   __TEXT.__const: 0xb60 sha256:aa9eaea3e1bf4554c080430db01f7b89090cdc6435b8bd29d7ac7da1b71c8287
-  __TEXT_EXEC.__text: 0x1cb7f0 sha256:6e42dfacd865573d2dd60b48e79450767ba9dc7871c556383c71ad8387931666
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc42 sha256:8f8aeebf8da83e9398d4580c67659fe5bf8663376cca67031b4d742b50e79d7d
+  __TEXT_EXEC.__text: 0x1cc084 sha256:feaaaeb7e47109ac960a7ec06d20b07e3250096b7ff9080fb23ef3cbf1780c2f
+  __TEXT_EXEC.__auth_stubs: 0xaa0 sha256:10c199c6e8ca7a3d01ca034861aa5c22724072b4d0f01bb27b183eaede747873
+  __DATA.__data: 0xc42 sha256:261c32a62b51f1df86f12b810c5fe6bf52288b4fb5e183431e58ce6d0454c46c
   __DATA.__common: 0x1600 sha256:07fa8a94dd06b17cdd8a23295f9687cd861be80591e8ab912dafabf21117f264
   __DATA.__bss: 0x9 sha256:3e7077fd2f66d689e0cee6a7cf5b37bf2dca7c979af356d0a31cbc5c85605c7d
-  __DATA_CONST.__mod_init_func: 0x460 sha256:42b95b722da8909fc690e769bd1d541a9aa5f0736e78ed4021fac73893c91203
-  __DATA_CONST.__mod_term_func: 0x460 sha256:41fcd353e6b427cca1c747cf42e10cb9efab5ec0fa68f52b7bc05a64debd1d79
-  __DATA_CONST.__const: 0x24a38 sha256:6ad9ef76fb3a7ab985f7daacdb23b686aa048a9a393b211e4f3c4418e5429146
-  __DATA_CONST.__kalloc_type: 0x2340 sha256:573c9cc3b58e52264fdc3ed653c0d5a0839b5cecf75c333c25b0e2d646efe178
-  __DATA_CONST.__kalloc_var: 0xcd0 sha256:771f85f3e583bd884c910caeb1cf0c744218b32f8a3f232692fcb88e671e49f5
-  __DATA_CONST.__auth_got: 0x550 sha256:754884fb9c50571f9327901894f60a27c5768caf80230967443b1212b2799743
-  __DATA_CONST.__got: 0x168 sha256:7f32976c896ee7dc877635b7c64852bc1e9663f393a0c905d3978995e4266c2a
-  UUID: 0BDFA420-4DDE-33EA-9A17-9A8A3324DCF8
-  Functions: 5698
+  __DATA_CONST.__mod_init_func: 0x460 sha256:5c66347ab5dcb5d4881a7088982d80c381ba5185421d82bb2c882b8b13f45744
+  __DATA_CONST.__mod_term_func: 0x460 sha256:c1a14b5b60da096df789684a9edc8b11140fd9607647d9731cfe7144e0fa0d92
+  __DATA_CONST.__const: 0x24a28 sha256:725e872892d9d2e4a07689a895843d197d1b990cd4cdb8bd37abf0e3ba0c9e21
+  __DATA_CONST.__kalloc_type: 0x2340 sha256:74027dd56eff6fea36b51eb302de77f92aa8849d209e1cb0e360e6cc27229f1b
+  __DATA_CONST.__kalloc_var: 0xcd0 sha256:de7410f451701ac8168c6e201e43bd4590f66f39501b2b45bd7603a236b9c8d7
+  __DATA_CONST.__auth_got: 0x550 sha256:d081aa3550846f46142379f2240282f05ec60c19997021d673427f03ac75e612
+  __DATA_CONST.__got: 0x168 sha256:be4312ccd946b92c4300b0916314429f499195c881cc3916424e2f4f32cdb92e
+  UUID: CC6E2618-4FB2-3098-A43A-C201929E86F6
+  Functions: 5701
   Symbols:   0
-  CStrings:  6221
+  CStrings:  6219
 
CStrings:
+ "%lldus IOThunderboltController(%d)::updateCLxModeInternal - sw_clx_objection=0x%x\n"
+ "%lldus IOThunderboltController(%d)::updateCLxModeInternal - switch_sw_clx_Objection = 0x%x route_string = 0x%llx (sw_clx_objection=0x%x)\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::doOverrideSupportedCLxStates - new_clx_states=0x%x controllerObjection=0x%x (explicit=%d)\n"
+ "%lldus IOThunderboltSwitchOS2(%d)::updateCLxModeInternal enable=0x%x\n"
+ "%lldus IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricMode - dispatchAsync( IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricModeInternal )\n"
+ "%lldus IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricMode - dispatchAsync( IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricModeInternal ) failed with status=0x%x\n"
+ "1211111212221212111111111222211111112212222212222221"
+ "121111121222121211111111122221111111221222221222222121212122"
+ "19:34:13"
+ "Jun 18 2026"
+ "mode"
- "%lldus IOThunderboltController(%d)::updateCLxModeInternal - fSWObjectionCLxStates=0x%x\n"
- "%lldus IOThunderboltController(%d)::updateCLxModeInternal - switch_sw_clx_Objection = 0x%x route_string = 0x%llx (fSWObjectionCLxStates=0x%x)\n"
- "%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - done waiting for in-progress asymmetric transition\n"
- "%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - start waiting for in-progress asymmetric transition (if any)\n"
- "%lldus IOThunderboltSwitch(%x@%llx)::doOverrideSupportedCLxStates - new_clx_states=0x%x controllerObjection=0x%x\n"
- "%lldus IOThunderboltSwitchOS2(%x@%llx)::blockUntilAsymmetricFlowDone - Asymmetric flow is in progress, sleep the thread\n"
- "%lldus IOThunderboltSwitchOS2(%x@%llx)::blockUntilAsymmetricFlowDone - thread woke up\n"
- "121111121222121211111111122221111112212222212222221"
- "12111112122212121111111112222111111221222221222222121212122"
- "22:46:39"
- "May 27 2026"

```
