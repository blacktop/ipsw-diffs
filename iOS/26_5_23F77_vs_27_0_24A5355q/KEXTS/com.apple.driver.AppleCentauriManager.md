## com.apple.driver.AppleCentauriManager

> `com.apple.driver.AppleCentauriManager`

```diff

-92.0.0.0.0
-  __TEXT.__cstring: 0x5812 sha256:b2cdc9ad0afa9c00c680e882a71eeaaf92d48f65d88d78b6bf742cca3fa90f42
-  __TEXT.__const: 0x190 sha256:5754d0f81f833fc50be27263232676ca1245de2dc7e1e39c676b2fc02c3ef0d8
-  __TEXT_EXEC.__text: 0x19e64 sha256:e9eaf12520cbe30fd3a2cb092881311fa0f4b6769442b56b7f19cdd7b93ec226
+123.0.0.0.1
+  __TEXT.__cstring: 0x5c00 sha256:79632b6baed73d2548e90067a903c84d4bce9b93c07329740814a00567a2ec90
+  __TEXT.__const: 0x180 sha256:aaa082f3f8b5a3ece7eed85fad4058787b38d645803cb5ac26e54c54a9e18b3a
+  __TEXT_EXEC.__text: 0x1ac24 sha256:cfeded0f9c919acd4972a86fcf540d5d3f1867713b2f5722369f174c3eab575a
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x188 sha256:297dc60727516ba8b9f1fa4ea1c6ffcac57cb8652cbe6b180a9d41fff1535335
+  __DATA.__data: 0x188 sha256:2a96a2e479f3bc3b9e280eb6427515d2544365f2d984b227bde6ce918dddf89f
   __DATA.__common: 0xf0 sha256:2dfba633817046c7f559ed4b93076048435f7e1a90f14eb8035c04b9ebae2537
-  __DATA.__bss: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
-  __DATA_CONST.__auth_got: 0x368 sha256:567c802a280b9ce639bf080f288da363fd1515a4fdfda35ece844c9ea7d94ed7
-  __DATA_CONST.__got: 0xf8 sha256:7bd4e3f495bfb3e36bb2f148e9c976dd3192129f40ca5cfef537a2c5fe0b41b4
-  __DATA_CONST.__mod_init_func: 0x28 sha256:ba4ed62bb83eed262988dba74e4dcd3ece174196efa57243e18b8c11657c5304
-  __DATA_CONST.__mod_term_func: 0x28 sha256:4a38630e3c5667cfdb0f05921a0323a4d963b3a0961f72f39e1aa20a2ee18f2c
-  __DATA_CONST.__const: 0x1918 sha256:8bc46c1eff679c0f916afe9cf70025be28555509d013ef099447bcb86ed35d73
-  __DATA_CONST.__kalloc_type: 0x1c0 sha256:734da9b490cbac97354428fea58a25d66b9ae8f5c25707315f1acf3a88d6b744
-  UUID: 8CB2CA6D-9482-3214-B72C-5394BDA1A1B4
-  Functions: 625
+  __DATA.__bss: 0x50 sha256:5b6fb58e61fa475939767d68a446f97f1bff02c0e5935a3ea8bb51e6515783d8
+  __DATA_CONST.__mod_init_func: 0x28 sha256:be2d0b9d594abcea74b76418ef8e00d9d12d152273d9deec4f9483b152547dc3
+  __DATA_CONST.__mod_term_func: 0x28 sha256:44e99537a07626dd7a45ad5798929922b2599712d7fc72f4c100dbe38dfc17b1
+  __DATA_CONST.__const: 0x1980 sha256:e0334a8076b301e60c8d45baf6d3ee38ae7dc38ba586e5319506346d6afc5270
+  __DATA_CONST.__kalloc_type: 0x1c0 sha256:9105cb7b99f15650ebf7a2b2ea4a2d661aa002c40d7dc47d28b02dd45a144e32
+  __DATA_CONST.__auth_got: 0x368 sha256:54c8776ac96e1388eddd08ba567785f69939873c3419349e2c1f7b2d5bd62f01
+  __DATA_CONST.__got: 0xf8 sha256:123f5923f358782ed857c08a06862b04aa6358cd3fa7eb1f159a180b5f41b947
+  UUID: D75DC8F4-822F-314E-8FBC-9DAAC2A45E3F
+  Functions: 641
   Symbols:   0
-  CStrings:  698
+  CStrings:  729
 
CStrings:
+ "\"duration != nullptr\" @%s:%d"
+ "\"fErrorEventActionDict->setObject(forClient->getName(), errorAction)\" @%s:%d"
+ "\"non-built-in client %s on %s; use centauri-builtin-disable=1 boot-arg\" @%s:%d"
+ "\"unexpected link down - no recovery path\" @%s:%d"
+ "\"unexpected link down with error detect - no recovery path\" @%s:%d"
+ "%s::%s: client no longer valid \n"
+ "%s::%s: failed to create OSDictionary for error actions \n"
+ "%s::%s: failed to create OSDictionary for firmware boot durations \n"
+ "%s::%s: ignoring device \n"
+ "%s::%s: kUSBProductString not found \n"
+ "%s::%s: kUSBVendorString not found \n"
+ "%s::%s: location 0x%llx, nibble 0x%x, ignore %u \n"
+ "%s::%s: locationID not found \n"
+ "%s::%s: notify client about prior completion timeout \n"
+ "%s::%s: overwriting pending error notification %s \n"
+ "%s::%s: skipping reenumeration since error recovery is underway (error %s) \n"
+ "%s::%s: start result: %d \n"
+ "12111112122212121111111111111111111111122222222212212121112222111211122222"
+ "Apple"
+ "Client Error Notify: %s\n"
+ "CompletionTimeout"
+ "DextLaunchTimeout"
+ "ErrorDetectGPIO"
+ "ErrorDetectGPIOLinkDown"
+ "Firmware Boot Durations:\n"
+ "FirmwareBootDurations"
+ "LinkDown"
+ "LinkTrainingTimeout"
+ "ManagerStartResult"
+ "WSSCB"
+ "[Fatal]Centauri-PCIeCompletionTimeout"
+ "kUSBProductString"
+ "kUSBVendorString"
+ "locationID"
+ "notifyPendingErrorEvents"
+ "setChipInfo"
+ "setManagerStartResult"
+ "shouldIgnoreDevice"
- "\"!fErrorEventAction\" @%s:%d"
- "\"[%s] Trigger panic for: %s\" @%s:%d"
- "%s::%s: not permitted \n"
- "%s::%s: skipping reenumeration since link training timeout recovery is underway \n"
- "1211111212221212111111111111111111111112222222221221212112222111211122222"
- "registerCentauriManagerErrorHandler"
- "triggerPanic"

```
