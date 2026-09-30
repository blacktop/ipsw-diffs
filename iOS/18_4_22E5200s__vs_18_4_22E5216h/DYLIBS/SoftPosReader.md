## SoftPosReader

> `/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader`

```diff

-34.17.0.0.0
-  __TEXT.__text: 0x1b5e8
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x1828
-  __TEXT.__const: 0xbc4
-  __TEXT.__cstring: 0x1b83
+34.20.0.0.0
+  __TEXT.__text: 0x1281d0
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x1830
+  __TEXT.__const: 0x7ccd0
+  __TEXT.__cstring: 0x1bf7
   __TEXT.__oslogstring: 0x3ea
-  __TEXT.__gcc_except_tab: 0x414
+  __TEXT.__gcc_except_tab: 0x424
   __TEXT.__constg_swiftt: 0x2c4
   __TEXT.__swift5_typeref: 0x16d
   __TEXT.__swift5_proto: 0x94
   __TEXT.__swift5_types: 0x50
-  __TEXT.__unwind_info: 0x980
-  __TEXT.__eh_frame: 0x1e0
+  __TEXT.__unwind_info: 0x9a0
+  __TEXT.__eh_frame: 0x228
   __TEXT.__objc_classname: 0x344
-  __TEXT.__objc_methname: 0x4f92
+  __TEXT.__objc_methname: 0x5022
   __TEXT.__objc_methtype: 0x135a
-  __TEXT.__objc_stubs: 0x15a0
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0xbe0
+  __TEXT.__objc_stubs: 0x1660
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x1400
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcf0
+  __DATA_CONST.__objc_selrefs: 0xd28
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__auth_ptr: 0x240
-  __AUTH_CONST.__const: 0x3c8
+  __AUTH_CONST.__const: 0x9670
   __AUTH_CONST.__cfstring: 0x1a60
-  __AUTH_CONST.__objc_const: 0x3180
+  __AUTH_CONST.__objc_const: 0x3190
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x100
   __DATA.__objc_ivar: 0x1e0
-  __DATA.__data: 0x778
-  __DATA.__bss: 0x1330
+  __DATA.__data: 0x900
+  __DATA.__bss: 0x1308
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SPRCore.framework/SPRCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 792
-  Symbols:   330
-  CStrings:  1171
+  Functions: 812
+  Symbols:   334
+  CStrings:  1182
 
Symbols:
+ _AMFIIsDeveloperModeEnabled
+ __Block_object_assign
+ __CFOperatingSystemVersionGetCurrent
+ ___assert_rtn
+ ___memcpy_chk
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _dispatch_time
+ _malloc
+ _os_variant_has_internal_content
+ _os_variant_has_internal_diagnostics
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- ___memset_chk
- _ccaes_gcm_encrypt_mode
- _ccdrbg_factory_nisthmac
- _ccdrbg_init
- _ccdrbg_reseed
- _ccec_cp_256
- _ccec_x963_import_pub
- _ccecies_encrypt_gcm
- _ccecies_encrypt_gcm_setup
- _ccrng_drbg_init_withdrbg
- _ccsha256_di
- _ccsha512_di
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "AVGetJSBLVersion"
+ "AVInternalObjC.m"
+ "TB,R,N"
+ "com.apple.sprvault.attestation.nfc"
+ "endSession"
+ "isFirstInQueue"
+ "jsblVersion <= UINT16_MAX"
+ "seIsProductionSigned"
+ "sequenceCounter"
+ "startSecureElementReaderSession:"
+ "unsignedLongLongValue"
+ "v24@?0@\"NFSecureElementReaderSession\"8@\"NSError\"16"
- "OrcaVault"
- "com.apple.muirfield"

```
