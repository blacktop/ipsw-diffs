## com.apple.driver.AppleFirmwareUpdateKext

> `com.apple.driver.AppleFirmwareUpdateKext`

```diff

-1576.0.0.0.0
-  __TEXT.__cstring: 0x885 sha256:816dacd13a3f54dc966fa224bdf3a60efea4062ceb43cf74628189bf919bd6e4
-  __TEXT.__const: 0x4 sha256:313588ae36b23498c072b8718f9a3614d9e52b444cdcea74ecd49c93044741b3
-  __TEXT_EXEC.__text: 0x2710 sha256:ce7262c3b978abd3056955fd2a4c5c1b130ec2bf5371bd2c1277ed325dba2e53
+1345.160.1.0.3
+  __TEXT.__cstring: 0x95a sha256:ea506d854efa3cc577c07227f1c03955c78232fe99304650e1ff7ab6ddcf9ddc
+  __TEXT_EXEC.__text: 0x27c4 sha256:5035dc3855c1f218d8da3eae1994d12925f95a1550a918208d03ad7c4c86860b
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:c24344ccb1a9a85b13f2a5442e638a73dece852de84bfe15358f7fb5a7742241
+  __DATA.__data: 0xc8 sha256:db27c763f00332804e122d1bc0e6ca1ccf476018c52fd37805fbafc9abf59475
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
-  __DATA_CONST.__mod_init_func: 0x10 sha256:c6375b4268511cc01eca5ae108d861873e5d5a73e9ff556ce2a35dd7fce807e4
-  __DATA_CONST.__mod_term_func: 0x10 sha256:c05322e048c834e1a7d875c879ae9d18443476e783a67621a97c8e8fbf964ea4
-  __DATA_CONST.__const: 0x1470 sha256:694c7d2aef761a6b9850da565833c5b715ef119115efe4baf7abc52298e101ac
-  __DATA_CONST.__kalloc_type: 0x80 sha256:926f755dbe453948704ce0b1d3ffff0359a767ac5f1921b759be5a984e627a03
-  __DATA_CONST.__auth_got: 0x120 sha256:c9bee3e4adf3a6a082a433704dbb391d03488182a10e741fec23bcc71419868a
-  __DATA_CONST.__got: 0x38 sha256:fef9d86b6ba323cb68ddb06c604400d830697b4c7f55cd18d1636b57866b9598
-  UUID: F88ACA76-F535-368D-A349-6B835F5C7A82
-  Functions: 84
-  Symbols:   462
-  CStrings:  58
+  __DATA_CONST.__auth_got: 0x108 sha256:39714506c15e809adc26b2042c5dbfe01f43824552da92bb61d88608de2b8f70
+  __DATA_CONST.__got: 0x40 sha256:1d2aa5f8011a52685bc1a3110648f4674a23f2b27c4dabaf4ca6ec42d164daaf
+  __DATA_CONST.__mod_init_func: 0x10 sha256:747eee40e65f1eeaa0dbb104cb2aac3015bb2cfb00a954c9e3d69bc63ebaa694
+  __DATA_CONST.__mod_term_func: 0x10 sha256:280bd6cc9269cbfd145430a28f866308593aa103304522da9c1a518795c86c86
+  __DATA_CONST.__const: 0x1480 sha256:d18faf6b5551a62f816a62bc0a3d6a758514cfc230884ca32d6c3b2f08a394a9
+  __DATA_CONST.__kalloc_type: 0x80 sha256:7ec24521f8344c56717ae4e8f495d1d3afafa3d94b80cde16e161c135745a072
+  UUID: 54880882-6A43-3462-996D-E32BAFC332C7
+  Functions: 86
+  Symbols:   464
+  CStrings:  65
 
Symbols:
+ _ZL25firmwareExecutionCallbackP14_img4_firmwareP11_img4_imageiPv.cold.1
+ __ZL25firmwareExecutionCallbackP14_img4_firmwareP11_img4_imageiPv
+ __ZN23AppleFirmwareUpdateKext18validationCompleteEP6OSDatai
+ __img4_chip_ap_reduced
+ __img4_chip_ap_sha2_384
+ __img4_runtime_default
+ _img4_firmware_destroy
+ _img4_firmware_execute
+ _img4_firmware_new
+ _img4_firmware_select_chip
+ _img4_image_get_bytes
- __ZN23AppleFirmwareUpdateKext18validationCompleteEP6OSData14Image4Return_t
- _bzero
- _image4ContextAttachManifest
- _image4ContextEvaluateManifest
- _image4ContextEvaluatePayload
- _image4ContextInit
- _image4ManifestInit
- _image4PayloadGetBytes
- _image4PayloadInit
CStrings:
+ "%s() Error: NULL context pointer delivered"
+ "%s() Failed to create img4Firmware\n"
+ "%s() Requesting AppleImage4 Validation\n"
+ "%s() Validation Successful\n"
+ "%s() error = %d\n"
+ "%s[%p]::%s() kFWValidationFailed \n"
+ "AppleFirmwareDecodeImage4"
+ "firmwareExecutionCallback"
- "%s[%p]::%s() kFWValidationFailed: %u\n"

```
