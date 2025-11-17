## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-17.1.0.0.0
-  __TEXT.__text: 0x30c20
+17.2.1.0.0
+  __TEXT.__text: 0x31040
   __TEXT.__auth_stubs: 0xc20
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x205c
+  __TEXT.__objc_methlist: 0x206c
   __TEXT.__const: 0x514
-  __TEXT.__gcc_except_tab: 0xb00
-  __TEXT.__cstring: 0x317f
-  __TEXT.__oslogstring: 0x4732
+  __TEXT.__gcc_except_tab: 0xb44
+  __TEXT.__cstring: 0x31cf
+  __TEXT.__oslogstring: 0x48b4
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xc58
+  __TEXT.__unwind_info: 0xc70
   __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0x709c
+  __TEXT.__objc_methname: 0x7189
   __TEXT.__objc_methtype: 0xd73
-  __TEXT.__objc_stubs: 0x6020
+  __TEXT.__objc_stubs: 0x6080
   __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__const: 0x10b8
+  __DATA_CONST.__const: 0x10d0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dc0
+  __DATA_CONST.__objc_selrefs: 0x1dd8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x428
-  __AUTH_CONST.__cfstring: 0x2c40
+  __AUTH_CONST.__cfstring: 0x2c80
   __AUTH_CONST.__objc_const: 0x1fa8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B77720E0-A3F6-3AAE-B250-093581A03B36
-  Functions: 1054
-  Symbols:   3741
-  CStrings:  2403
+  UUID: 9C0BAAFF-AC2C-3B8D-8DD9-874E905F4E4F
+  Functions: 1058
+  Symbols:   3748
+  CStrings:  2417
 
Symbols:
+ -[PABSBiometrics resetClientRestrictionOnPasscodeGracePeriod]
+ -[PABSBiometrics resetClientRestrictionOnPasscodeGracePeriod].cold.1
+ -[PABSBiometrics resetClientRestrictionOnPasscodeGracePeriod].cold.2
+ GCC_except_table21
+ ___44-[PABSBiometrics removeIdentity:completion:]_block_invoke.14
+ ___49-[PABSBiometrics setName:forIdentity:completion:]_block_invoke.12
+ ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12ls32l8w48l8s40l8
+ ___block_literal_global.16
+ _objc_msgSend$applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:
+ _objc_msgSend$clientRestrictionsForClientUUID:
+ _objc_msgSend$resetClientRestrictionOnPasscodeGracePeriod
- ___44-[PABSBiometrics removeIdentity:completion:]_block_invoke.8
- ___49-[PABSBiometrics setName:forIdentity:completion:]_block_invoke.6
- ___block_literal_global.10
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_PasscodeAndBiometricsSettings
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_PasscodeAndBiometricsSettings
CStrings:
+ "An error occured while removing the identity type: %lu %@"
+ "Did remove identity type: %lu"
+ "Did reset client restriction on passcode grace period"
+ "Failed to reset client restriction on passcode grace period"
+ "Skipping resetting client restriction on passcode grace period as no restriction exists currently"
+ "Will remove identity type: %lu"
+ "Will reset client restriction on passcode grace period"
+ "applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
+ "clientRestrictionsForClientUUID:"
+ "com.apple.BiometricKitUI"
+ "com.apple.BiometricsKitUI.FaceID.Restrictions"
+ "resetClientRestrictionOnPasscodeGracePeriod"

```
