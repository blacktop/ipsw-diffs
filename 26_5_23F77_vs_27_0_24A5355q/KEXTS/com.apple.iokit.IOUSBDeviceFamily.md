## com.apple.iokit.IOUSBDeviceFamily

> `com.apple.iokit.IOUSBDeviceFamily`

```diff

-847.100.26.0.0
-  __TEXT.__cstring: 0x2bc1 sha256:7364735fffd252d16429abf458e4bae8972b991ad91bd4d459ad32b8cb092ddd
+891.0.0.0.0
+  __TEXT.__cstring: 0x33f8 sha256:b97f577e3e73a90aefb1e2981a45e079357b02fcca0bdb4e46ed133505501d0b
   __TEXT.__const: 0x260 sha256:893d93049c5aa335676d7a2f6bd30953636d3fb2e93737f83995de2ebbb489e3
-  __TEXT.__os_log: 0x1b09 sha256:d6849e87fb6b909daaa0c5d3dc45fe2bf4b146b80f3cc95c1b9a1254d8dbba2b
-  __TEXT_EXEC.__text: 0x27bd8 sha256:d09ba1148a83c177e6889aa4c6ec429e00b07d814f0e42aa8bd06dc57a0c1a7e
+  __TEXT.__os_log: 0x21fc sha256:fbdac576c0687a6e089ecd5c71f076b3fdf825faedd905491f084308cbbfe6b8
+  __TEXT_EXEC.__text: 0x2accc sha256:65be386a7c1508c34dfe27bbb7538fdc26d0150ecca0d0ceb5a629596e102718
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:93e0a26c768fa4a80ed094947899ee354ec125eafc4e8d52f2d25d590fab2526
+  __DATA.__data: 0xc8 sha256:c66d98ece63e2c7f296e1f5592a4c9c947d9d3bd4456f38539e4e6016541fac1
   __DATA.__common: 0x218 sha256:7d73a488b95b99a42237504643b79aa49c55a9aad3cd97e58518f093d3e095df
   __DATA.__bss: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__auth_got: 0x378 sha256:8151961d6b8f10f83ff97104c92d82edba7fa6ffc43d86568ce86810939489b6
-  __DATA_CONST.__got: 0xe0 sha256:296d68e9015a705285e2fdb3c09b128b8561f964bf16a15c49583d9227b16c99
-  __DATA_CONST.__auth_ptr: 0x8 sha256:8f1612f1af9e40021d2e6eb4b85f45c15eab8b7d9e231549e90239309e015d85
-  __DATA_CONST.__mod_init_func: 0x58 sha256:466740f6f6426ec9ea44455404fb8da135d1a0aae674979017872ab16e45fde5
-  __DATA_CONST.__mod_term_func: 0x50 sha256:7717fa840ab12b9fce2e25ccc62ddc1425f81996560a35c96d35f0bc02105ed8
-  __DATA_CONST.__const: 0x3760 sha256:c12e7f8a15276ffc6d8df1c8464ac6e10c4b308eef3538de255c2c0fdcb916a0
-  __DATA_CONST.__kalloc_type: 0x6c0 sha256:12ee20883674511fc79c5895742729eb9acdb5326a68a0c8a0d2a817c268981b
-  __DATA_CONST.__kalloc_var: 0x190 sha256:b06c2d7860e0dabf503dd0dbcf93b5487e651d0889d414e411c9fdf265c9b3aa
-  UUID: A94C7679-13B8-3B9A-9DCB-4593704E1DE0
-  Functions: 730
+  __DATA_CONST.__mod_init_func: 0x58 sha256:db8091e2e0f562f55bb8f3af906d8512f0e7888c0c663a87df449005f499fd24
+  __DATA_CONST.__mod_term_func: 0x50 sha256:a5b0cd2881b41b2fc017bc0eba29a8e91cee5b00fe21c4fe38ea4b3577790e29
+  __DATA_CONST.__const: 0x3760 sha256:f39c36e75519a9405de475737814a4f6ca724af758cc7890351f8270ac3dd2e8
+  __DATA_CONST.__kalloc_type: 0x6c0 sha256:7cbd0e4e447dd9e49184133f84baae1fbdce192be69e0d8a17c0c0741199ea83
+  __DATA_CONST.__kalloc_var: 0x190 sha256:0795cc37ffd4aa11a15fdfd0c4a7ad4c439a48f0ed37a212247c6259fffff3dd
+  __DATA_CONST.__auth_got: 0x380 sha256:e35d072b102167855065119f664512007909c2f83bb809cc92e44c046716944a
+  __DATA_CONST.__got: 0xe0 sha256:b8ed4365006c5e70eb2b7f1bb92dc34bac111eb718051368e7eb22e27afbcc36
+  __DATA_CONST.__auth_ptr: 0x8 sha256:d754d0b5f6c902523a5801ff2cd20cd1405c62d46f84af037e6be6edac031b7f
+  UUID: EDFEB4BD-9419-3050-91A4-7596060C3050
+  Functions: 739
   Symbols:   0
-  CStrings:  489
+  CStrings:  553
 
CStrings:
+ "%s@%s: %s::%s: %d function(s) failed to register within timeout\n"
+ "%s@%s: %s::%s: Activating ncmAuxOnly fallback configuration\n"
+ "%s@%s: %s::%s: Added failed function to BOS descriptor: %s (string index %d)\n"
+ "%s@%s: %s::%s: All functions registered - cancelling timeout timer\n"
+ "%s@%s: %s::%s: Already in ncmAuxOnly fallback mode but %d function(s) still failed to register - giving up\n"
+ "%s@%s: %s::%s: Creating failed functions capability descriptor for %d failed functions\n"
+ "%s@%s: %s::%s: Driver registration timeout triggered\n"
+ "%s@%s: %s::%s: Failed functions capability descriptor size limit reached\n"
+ "%s@%s: %s::%s: Failed to allocate FD capability descriptor\n"
+ "%s@%s: %s::%s: Failed to allocate config dictionary\n"
+ "%s@%s: %s::%s: Failed to allocate configurations array\n"
+ "%s@%s: %s::%s: Failed to allocate interfaces array\n"
+ "%s@%s: %s::%s: Failed to build fallback device description - unable to proceed with fallback configuration\n"
+ "%s@%s: %s::%s: Failed to copy device description\n"
+ "%s@%s: %s::%s: Failed to create config attributes\n"
+ "%s@%s: %s::%s: Failed to create config description\n"
+ "%s@%s: %s::%s: Failed to create fallback USB device: 0x%x\n"
+ "%s@%s: %s::%s: Failed to create interface name strings\n"
+ "%s@%s: %s::%s: Failed to get current device description\n"
+ "%s@%s: %s::%s: Found failed NCM interface: %s\n"
+ "%s@%s: %s::%s: NCM interfaces are in the failed functions list - cannot fallback to NCM-only configuration. Giving up with %d function(s) unregistered\n"
+ "%s@%s: %s::%s: No failed functions to add to BOS descriptor\n"
+ "%s@%s: %s::%s: Successfully added failed functions capability descriptor to BOS (length=%d)\n"
+ "%s@%s: %s::%s: Successfully built fallback device description\n"
+ "%s@%s: %s::%s: Successfully created ncmAuxOnly fallback configuration\n"
+ "%s@%s: %s::%s: Unregistered function: %s\n"
+ "12111112122212121112122122222221221222211212111111121212222211222222222222222222222222222222222222222222222222222222222222222112222222222"
+ "A745B2DF-FB29-4E45-844D-BEFD6D125F9A"
+ "AppleUSBNCM"
+ "AppleUSBNCMControlAux"
+ "AppleUSBNCMDataAux"
+ "Fallback Configuration - ncmAux"
+ "activateFallbackConfiguration"
+ "addFailedFunctionsCapabilityDescriptor"
+ "buildFallbackDeviceDescription"
+ "handleUnregisteredFunctionsTimeout"
+ "hasFailedNCMFunctions"
+ "ncmAuxOnly_fallback"
+ "recordFailedFunctions"
- "12111112122212121112122122222221221222211212111111121222221222222222222222222222222222222222222222222222222222222222222222112222222222"

```
