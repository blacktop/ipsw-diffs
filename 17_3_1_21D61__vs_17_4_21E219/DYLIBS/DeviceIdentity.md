## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-898.60.6.0.0
+921.100.31.0.0
   __TEXT.__text: 0x150ec
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__cstring: 0x32c4
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x1cc
+  __TEXT.__cstring: 0x3372
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x4d8
+  __TEXT.__oslogstring: 0x50c
   __TEXT.__const: 0xba
   __TEXT.__gcc_except_tab: 0x5d8
   __TEXT.__dlopen_cstrs: 0x144
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2c4
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x1438
+  __TEXT.__objc_methname: 0x14ba
   __TEXT.__objc_methtype: 0x320
-  __TEXT.__objc_stubs: 0xe00
+  __TEXT.__objc_stubs: 0xe20
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa38
-  __DATA_CONST.__objc_selrefs: 0x448
-  __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__cfstring: 0x3800
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_const: 0xa68
+  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_arraydata: 0x370
+  __AUTH_CONST.__cfstring: 0x3920
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x390
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x44
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__auth_got: 0x3a8
+  __DATA.__objc_ivar: 0x48
   __DATA.__data: 0xc4
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__const: 0x100
+  __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__objc_const: 0x120
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 181
-  Symbols:   876
-  CStrings:  787
+  Functions: 184
+  Symbols:   888
+  CStrings:  801
 
Symbols:
+ -[DeviceTypeDeviceIdentity device_supports_mfi_certificates]
+ _OBJC_IVAR_$_DeviceTypeDeviceIdentity._device_supports_mfi_certificates
+ _X509ExtensionParseCertifiedChipIntermediate
+ ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.164
+ ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.310
+ ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.313
+ ___block_descriptor_282_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e5_v8?0lr136l8r144l8r152l8s32l8r160l8r168l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r176l8r184l8r192l8r200l8r208l8r216l8s104l8r224l8r232l8r240l8r248l8r256l8s112l8r264l8s120l8s128l8r272l8
+ ___block_descriptor_298_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144bs152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r_e5_v8?0ls32l8s40l8r152l8s48l8r160l8r168l8s56l8r176l8r184l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8s128l8r280l8s136l8s144l8r288l8
+ ___block_literal_global.350
+ __unnamed_array_storage.331
+ __unnamed_array_storage.336
+ _device_supports_mfi_certificates
+ _kMAOptionsBAAOIDImageCertificateProperties
+ _objc_msgSend$device_supports_mfi_certificates
+ _objc_release_x3
+ _objc_retain_x24
+ _objc_retain_x28
- ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.162
- ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.309
- ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.312
- ___block_descriptor_281_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e5_v8?0lr136l8r144l8r152l8s32l8r160l8r168l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r176l8r184l8r192l8r200l8r208l8r216l8s104l8r224l8r232l8r240l8r248l8r256l8s112l8r264l8s120l8s128l8r272l8
- ___block_descriptor_297_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144bs152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r_e5_v8?0ls32l8s40l8r152l8s48l8r160l8r168l8s56l8r176l8r184l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8s128l8r280l8s136l8s144l8r288l8
- ___block_literal_global.349
- __unnamed_array_storage.307
- __unnamed_array_storage.312
CStrings:
+ "%{public}@ (non-fatal, existing valid certificates)"
+ "1.2.840.113635.100.6.1.15"
+ "Failed to alloc dictionary."
+ "MapsTransactionInsightsExtension"
+ "MobileAssetLibTests-Runner"
+ "Passbook"
+ "SPREngineIntegrationTests-Runner"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_device_supports_mfi_certificates"
+ "_device_supports_mfi_certificates"
+ "asutil"
+ "device_supports_mfi_certificates"
+ "financed"
+ "iOS Device Activator (MobileActivation-921.100.31)"
+ "mapspushd"
+ "mobileassetd"
- "iOS Device Activator (MobileActivation-898.60.6)"
- "s7nuHoZIYNoOHCqT9iyZkQ"

```
