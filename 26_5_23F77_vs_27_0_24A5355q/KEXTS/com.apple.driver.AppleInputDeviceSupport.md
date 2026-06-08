## com.apple.driver.AppleInputDeviceSupport

> `com.apple.driver.AppleInputDeviceSupport`

```diff

-9140.6.0.0.0
-  __TEXT.__cstring: 0x1e6c
+10100.34.0.0.0
+  __TEXT.__cstring: 0x2e35
   __TEXT.__const: 0x70
-  __TEXT.__os_log: 0x63a
-  __TEXT_EXEC.__text: 0x173dc
+  __TEXT.__os_log: 0xd6f
+  __TEXT_EXEC.__text: 0x1ada4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x358
-  __DATA_CONST.__auth_got: 0x370
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__mod_init_func: 0x80
-  __DATA_CONST.__mod_term_func: 0x80
-  __DATA_CONST.__const: 0x3540
-  __DATA_CONST.__kalloc_type: 0x640
+  __DATA.__common: 0x3a8
+  __DATA_CONST.__mod_init_func: 0x90
+  __DATA_CONST.__mod_term_func: 0x90
+  __DATA_CONST.__const: 0x41c8
+  __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x2d0
-  UUID: 531C5B7C-2C21-3A83-BFFD-5ECC0A547119
-  Functions: 740
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0xe8
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
