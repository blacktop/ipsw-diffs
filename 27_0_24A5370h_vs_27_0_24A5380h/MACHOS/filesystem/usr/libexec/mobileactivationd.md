## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-  __TEXT.__text: 0x34a01c
-  __TEXT.__auth_stubs: 0x1230
+  __TEXT.__text: 0x34b994
+  __TEXT.__auth_stubs: 0x1240
   __TEXT.__objc_stubs: 0x3240
   __TEXT.__objc_methlist: 0x112c
   __TEXT.__const: 0x5c4d3
-  __TEXT.__cstring: 0xeb94
+  __TEXT.__cstring: 0xeea5
   __TEXT.__objc_methname: 0x4044
   __TEXT.__oslogstring: 0xf47
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x1061
-  __TEXT.__gcc_except_tab: 0x1a94
+  __TEXT.__gcc_except_tab: 0x1b88
   __TEXT.__dlopen_cstrs: 0x294
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x11f8
+  __TEXT.__unwind_info: 0x1238
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0x1c008
-  __DATA_CONST.__cfstring: 0xd200
+  __DATA_CONST.__const: 0x1c088
+  __DATA_CONST.__cfstring: 0xd4e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_intobj: 0x330
   __DATA_CONST.__objc_arraydata: 0x600
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA_CONST.__auth_got: 0x928
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__auth_got: 0x930
+  __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x78
   __DATA.__objc_const: 0x1900
   __DATA.__objc_selrefs: 0x10c0
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x1d38
-  __DATA.__bss: 0x558
+  __DATA.__bss: 0x568
   __DATA.__common: 0xb20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1643
-  Symbols:   11035
-  CStrings:  4721
+  Functions: 1658
+  Symbols:   11149
+  CStrings:  4778
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa_request.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa_rkproperties.o
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_48
+ ___assert_rtn
+ ___destructor_8_s0_s8_s16_s24_s32_s40_s48_s56_s64_s72_s80_s88_s96_s104_s112_s120_s128_s136_s144_s152_s160_s168_s176_s184_s192_s200_s208_s216_s224_s232_s240_s248_s256_s264_s272
+ ___redactOptionsForLogging_block_invoke
+ _baa_request_body_create_dictionary
+ _baa_request_body_has_required_fields
+ _baa_request_create_with_body
+ _baa_rkproperties_create_data
+ _baa_rkproperties_from_data
+ _baa_rkproperties_has_required_fields
+ _kMAOptionsBAABoardId
+ _kMAOptionsBAAChipID
+ _kMAOptionsBAADeviceLocalPolicyCertificate
+ _kMAOptionsBAARequestVersion
+ _kMAOptionsBAASCRT
+ _kMAOptionsBAASecurityDomain
+ _kMAOptionsBAASerialNumber
+ _kMAOptionsBAAUCRT
+ _kMAOptionsBAAUniqueChipID
+ _kMAOptionsBAAUseIM4C
+ _kMAOptionsBAAVMIdentityAttestation
+ _udid_from_chipid_and_ecid
+ _udid_from_rkproperties_data
+ baa_request.m
+ baa_request_body_create_dictionary
+ baa_rkproperties.m
+ redactOptionsForLogging.onceToken
+ redactOptionsForLogging.sensitiveKeys
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_57
- _OUTLINED_FUNCTION_58
CStrings:
+ "%08X-%016llX"
+ "1145.0.1"
+ "<private>"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1145.0.1 built on Jun 26 2026 at 22:45:04)"
+ "Could not convert data to dictionary."
+ "DeviceLocalPolicyCertificate"
+ "Failed to create RKProperties data."
+ "Input data incomplete."
+ "Missing RKCertification."
+ "Missing RKProperties."
+ "Missing RKPropertiesSignature."
+ "Missing boardID."
+ "Missing chipID."
+ "Missing ecid."
+ "Missing required input."
+ "Missing rkCertificationPub."
+ "Missing securityDomain."
+ "Missing sikPub."
+ "RKProperties is nil."
+ "Request body is nil."
+ "RequestVersion"
+ "UseIM4C"
+ "VMIdentityAttestation"
+ "baa_request.m"
+ "baa_request_body_create_dictionary"
+ "baa_request_body_has_required_fields"
+ "baa_request_create_with_body"
+ "baa_rkproperties_create_data"
+ "baa_rkproperties_from_data"
+ "baa_rkproperties_has_required_fields"
+ "iOS Device Activator (MobileActivation-1145.0.1)"
+ "requestBody"
+ "requestBody->rkCertification"
+ "requestBody->rkProperties"
+ "requestBody->rkPropertiesSignature"
+ "scrt"
+ "ucrt"
- "1144"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1144 built on Jun 15 2026 at 23:58:33)"
- "iOS Device Activator (MobileActivation-1144)"

```
