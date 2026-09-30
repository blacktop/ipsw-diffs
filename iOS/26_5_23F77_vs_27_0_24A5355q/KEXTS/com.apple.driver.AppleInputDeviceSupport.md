## com.apple.driver.AppleInputDeviceSupport

> `com.apple.driver.AppleInputDeviceSupport`

```diff

-9140.6.0.0.0
-  __TEXT.__cstring: 0x1e6c sha256:2515156b5ec16d15683e68e7f33975fa222b42552637fdb1def1a09e348ff57d
+10100.34.0.0.0
+  __TEXT.__cstring: 0x2e35 sha256:11f3169475425bb8784b94551ab2535d19dce4094de9238cafea2f78a83b776f
   __TEXT.__const: 0x70 sha256:2cf8b74e6d8cb09f34e54882faba7c9c25af7dc2b7bbd50d793988b4685a9aa2
-  __TEXT.__os_log: 0x63a sha256:feb0dfe8bf8520d1e9a99502bd641b7bbb4bad9831fcbf68ae1db654f2101acc
-  __TEXT_EXEC.__text: 0x173dc sha256:6894a635337091ee5ffc426710568866d2d60fa4255eb9e611ddcaa167918bb7
+  __TEXT.__os_log: 0xd6f sha256:f5aba59d16d5e743f9e4f2c3c382718f33f5c75c3ba2b0e0a9f9e06c910a9c23
+  __TEXT_EXEC.__text: 0x1ada4 sha256:855c670016a4f72462207b47509745f958108f786c6c2be195a74cc5ef090996
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:d5c32cb0a18107f289258d73c5a8268664c849e8187bf019f16328bbb909fb15
-  __DATA.__common: 0x358 sha256:ab9ac8d62fd064748c921e6bd4c123f5cc8910a384d1804bec33ffe27da27c4c
-  __DATA_CONST.__auth_got: 0x370 sha256:3b90d3a99bbaad1820eb17aae9a60c322e327c443fc18bb480e8a1bda3981c19
-  __DATA_CONST.__got: 0xf8 sha256:90c59d8923d6ee2aef2038208db8f2f2e7b5e7555bccbb850cf26cc4a72f158d
-  __DATA_CONST.__mod_init_func: 0x80 sha256:d4887a940dc01a369855684c43e388a07e5a014b67d575eb064f323e22437f77
-  __DATA_CONST.__mod_term_func: 0x80 sha256:65fd5dc9f961d3a1a191eb434648382d49d557e9083eb270b364b8259239fbed
-  __DATA_CONST.__const: 0x3540 sha256:6c6a81c0f34c9fabf334ad1f030ee3371477ddd52546a268d4fb25aadeeff6ec
-  __DATA_CONST.__kalloc_type: 0x640 sha256:dfde21ae7417c9954a5c29a2536d92a09c9817a638c4542d23f63578c91be31c
-  __DATA_CONST.__kalloc_var: 0x2d0 sha256:eb61e5b6c558505bbdbdec5b3112cc8aa66b058bbd4ab0504241bb800e24c726
-  UUID: 531C5B7C-2C21-3A83-BFFD-5ECC0A547119
-  Functions: 740
+  __DATA.__data: 0xc8 sha256:294147d4d60f3f0e46bd86bd25bca935b60d1a6ffb2c9fb5932be4631e2dfe14
+  __DATA.__common: 0x3a8 sha256:4db2fd521b198ad08a6602141c428d23a3bf232e85fd7de8418439e89d7b3d04
+  __DATA_CONST.__mod_init_func: 0x90 sha256:a611952783af6facf57c9e0e6decfb8728ef2103f0aa8e0126211cf67c1a353b
+  __DATA_CONST.__mod_term_func: 0x90 sha256:0c339f51efc634699e98287669dd45b3de28b4020b349d02a12e27b2242d6b63
+  __DATA_CONST.__const: 0x41c8 sha256:f06b170d4d84a644573b312941922617499e6ba6e6e1c644002d13b27d81b1cd
+  __DATA_CONST.__kalloc_type: 0x6c0 sha256:ad67ec2269f192ea3b5813ebf61aa4efc9d0c4bb1df343888a62dd30c603aa89
+  __DATA_CONST.__kalloc_var: 0x2d0 sha256:49c1aefcadeabf7bc90ed20e052c438abec8c79619fb3facbe20521a52ebd210
+  __DATA_CONST.__auth_got: 0x3d0 sha256:3a512c93641873a0470c88f3be3bfe7b59b1719b7232f37522c1a4a0fa670c42
+  __DATA_CONST.__got: 0xe8 sha256:45e417b37dc71e54336b748d8dcb0bf21c2c4202fc266256e8389317653e5660
+  UUID: 62F7BCE8-8C53-3748-B3C9-1764E306F83F
+  Functions: 866
   Symbols:   0
-  CStrings:  324
+  CStrings:  425
 
CStrings:
+ "%s \n"
+ "%s Task not privileged \n"
+ "%s() Validation Successful for payload:%p with length:%u\n"
+ "%s::%s() Performing img4 validation outside of workloop\n"
+ "%s::%s() Time Taken For IMG4 Validation: %llu ms\n"
+ "%s::%s() Total Time Taken For Kernel Client's to complete: %llu ms\n"
+ "%s::%s() Total Time Taken For User Space Request to complete: %llu ms\n"
+ "%s::%s(): Calling external handler for manifest tag 0x%08x\n"
+ "%s::%s(): Unhandled manifest tag 0x%08x\n"
+ "%s[%p]::%s() %s is working asynchronously\n"
+ "%s[%p]::%s() Boot-arg present, skipping firmware validation\n"
+ "%s[%p]::%s() Cannot create fdrClass\n"
+ "%s[%p]::%s() Cannot create fdrClassBuffer\n"
+ "%s[%p]::%s() Cannot create fdrData\n"
+ "%s[%p]::%s() Entering \n"
+ "%s[%p]::%s() Exiting with status = 0x%x \n"
+ "%s[%p]::%s() Invalid _firmwareBuffer\n"
+ "%s[%p]::%s() Invalid _firmwareDescriptor\n"
+ "%s[%p]::%s() Invalid _firmwareMap\n"
+ "%s[%p]::%s() Invalid map\n"
+ "%s[%p]::%s() No FDR callback registered\n"
+ "%s[%p]::%s() No FDR class received\n"
+ "%s[%p]::%s() No FDR data received\n"
+ "%s[%p]::%s() No loadFDRDataComplete callback registered\n"
+ "%s[%p]::%s() Only non signed FDR data supported\n"
+ "%s[%p]::%s() Return value from inputMD->prepare(): %d\n"
+ "%s[%p]::%s() bufferLength must be > classLength (%u > %u)\n"
+ "%s[%p]::%s() commandSleep awakened, validateImage4Completed = %s\n"
+ "%s[%p]::%s() commandSleep interrupted, validateImage4Completed = %s\n"
+ "%s[%p]::%s() commandSleep timed out, validateImage4Completed = %s\n"
+ "%s[%p]::%s() commandSleep waitResult = %d, validateImage4Completed = %s\n"
+ "%s[%p]::%s() kFWValidationFailed: %u\n"
+ "%s[%p]::%s() kFWValidationSuccess \n"
+ "%s[%p]::%s() status = 0x%x, Disabling event source\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareImage4.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateService.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateUserClient.cpp"
+ "12111112122212121111111111111111122222222"
+ "121111121222121211111111111112"
+ "121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222"
+ "AIDFirmwareDecodeImage4"
+ "AIDFirmwareDecodeImage4(_firmwareBuffer, tag, this)"
+ "AIDFirmwareUpdateService"
+ "AIDFirmwareUpdateUserClient"
+ "FDR Classes"
+ "FDR Data Identifiers"
+ "FWValidated"
+ "FWValidationNotRequired == false"
+ "IOUserClientClass"
+ "Image Tag"
+ "KernelClientRequestTimeMs"
+ "Need FUD Download"
+ "UserSpaceRequestTimeMs"
+ "ValidationTimeMs"
+ "_afuLock"
+ "_beginFDRDataDownloadCallback"
+ "_beginFirmwareDownloadCallback"
+ "_commandGate"
+ "_customTagValidationCallback"
+ "_customTagValidationCallbackContext"
+ "_firmwareBuffer"
+ "_firmwareDescriptor"
+ "_firmwareMap"
+ "_isCustomValidationNeeded"
+ "_loadFDRDataCompleteCallback"
+ "_userAccess"
+ "_validateImage4TES"
+ "bufferLengthIn > classLengthIn"
+ "com.apple.afu.userclientaccess"
+ "com.apple.hid.firmware.userclientaccess"
+ "dataIdentifierMap->getCount() > 0"
+ "false"
+ "fdr-data-identifier"
+ "fdrClass"
+ "fdrClassBuffer"
+ "fdrData"
+ "fdrDataIdentifier"
+ "image4Ret == kImage4ReturnSuccess"
+ "inputMD"
+ "loadFDRData"
+ "loadFDRDataComplete"
+ "loadFirmware"
+ "map"
+ "payloadReturn"
+ "performCustomValidation"
+ "returnValue == kIOReturnSuccess"
+ "signatureType == kNoSignature"
+ "site.AIDFirmwareUpdateService"
+ "site.AIDFirmwareUpdateUserClient"
+ "skip-image-loading"
+ "skipFWValidation"
+ "status == kIOReturnSuccess"
+ "success"
+ "tag"
+ "true"
+ "validateFirmware"
+ "validateFirmwareGated"
+ "validateImage4"
+ "validationComplete"
+ "verified == true"
+ "virtual IOReturn AIDFirmwareUpdateUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)"

```
