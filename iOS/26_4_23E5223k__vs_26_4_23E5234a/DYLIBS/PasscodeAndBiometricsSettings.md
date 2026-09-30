## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-17.4.9.0.0
-  __TEXT.__text: 0x43400
+17.4.10.0.0
+  __TEXT.__text: 0x43510
   __TEXT.__auth_stubs: 0x1530
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x2334
   __TEXT.__const: 0x1014
   __TEXT.__gcc_except_tab: 0xb3c
-  __TEXT.__cstring: 0x3773
-  __TEXT.__oslogstring: 0x537d
+  __TEXT.__cstring: 0x3793
+  __TEXT.__oslogstring: 0x53ad
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__swift5_typeref: 0x714

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x1288
+  __TEXT.__unwind_info: 0x1298
   __TEXT.__eh_frame: 0x828
   __TEXT.__objc_classname: 0x6ed
-  __TEXT.__objc_methname: 0x76e0
+  __TEXT.__objc_methname: 0x76b0
   __TEXT.__objc_methtype: 0x1086
-  __TEXT.__objc_stubs: 0x6380
+  __TEXT.__objc_stubs: 0x6360
   __DATA_CONST.__got: 0x778
   __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f10
+  __DATA_CONST.__objc_selrefs: 0x1f08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0xab0
   __AUTH_CONST.__const: 0xbf0
-  __AUTH_CONST.__cfstring: 0x2d20
+  __AUTH_CONST.__cfstring: 0x2d40
   __AUTH_CONST.__objc_const: 0x2430
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D0F0C0E-18C8-3943-9240-00A815C15992
-  Functions: 1444
-  Symbols:   4096
-  CStrings:  2582
+  UUID: 4AD515B0-AAA7-3B8F-A02C-3B39BE913672
+  Functions: 1446
+  Symbols:   4101
+  CStrings:  2584
 
Symbols:
+ -[PABSPasscodeLockController enableVisionUnlockForDevice:ofSpecifier:].cold.1
+ -[PABSPasscodeLockController enableVisionUnlockForDevice:ofSpecifier:].cold.2
+ _OUTLINED_FUNCTION_15
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.318
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.318.cold.1
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.117
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.117.cold.1
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.313
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.315
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.316
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.316.cold.1
+ ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.295
+ ___block_literal_global.320
+ ___block_literal_global.322
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.315
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.315.cold.1
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.114
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.114.cold.1
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.310
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.312
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.313
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.313.cold.1
- ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.292
- ___block_literal_global.317
- ___block_literal_global.319
- _objc_msgSend$enableForType:withIDSDeviceID:passcodeRef:
CStrings:
+ "%@: Failed to extract passcode - no passcode"
+ "BKOptionAuthWithCredentialSet"
+ "enabling Vision Pro autounlock device using pwd: %@"
- "enableForType:withIDSDeviceID:passcodeRef:"
- "enabling Vision Pro autounlock device: %@"

```
