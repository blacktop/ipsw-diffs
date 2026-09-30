## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-255.0.3.0.0
-  __TEXT.__text: 0x10f4c4
-  __TEXT.__auth_stubs: 0x2540
+255.0.5.0.0
+  __TEXT.__text: 0x10e6fc
+  __TEXT.__auth_stubs: 0x2590
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x14397
-  __TEXT.__cstring: 0x2a13
-  __TEXT.__swift5_typeref: 0x26c6
-  __TEXT.__oslogstring: 0x2414
-  __TEXT.__swift5_capture: 0x220
-  __TEXT.__swift5_reflstr: 0x2a50
-  __TEXT.__swift5_assocty: 0x5b8
+  __TEXT.__const: 0x159e7
+  __TEXT.__cstring: 0x29d3
   __TEXT.__constg_swiftt: 0x2a9c
+  __TEXT.__swift5_typeref: 0x26c6
+  __TEXT.__swift5_reflstr: 0x2a70
   __TEXT.__swift5_fieldmd: 0x34c8
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0xa0
   __TEXT.__swift5_proto: 0xac8
   __TEXT.__swift5_types: 0x3dc
+  __TEXT.__oslogstring: 0x241f
   __TEXT.__swift_as_entry: 0x2a8
   __TEXT.__swift_as_ret: 0x258
+  __TEXT.__swift5_capture: 0x220
+  __TEXT.__swift5_assocty: 0x5b8
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x4800
-  __TEXT.__eh_frame: 0x8f98
+  __TEXT.__unwind_info: 0x47c8
+  __TEXT.__eh_frame: 0x8f58
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x3ce
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__const: 0xf08
+  __DATA_CONST.__got: 0x6e0
+  __DATA_CONST.__const: 0xee8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x12a0
-  __AUTH_CONST.__const: 0x6638
+  __AUTH_CONST.__auth_got: 0x12c8
+  __AUTH_CONST.__const: 0x6750
   __AUTH_CONST.__objc_const: 0x770
   __AUTH.__objc_data: 0x200
-  __AUTH.__data: 0x22c0
+  __AUTH.__data: 0x22c8
   __DATA.__data: 0x2818
-  __DATA.__common: 0x390
   __DATA.__bss: 0x12200
+  __DATA.__common: 0x390
   __DATA_DIRTY.__data: 0x1bf8
   __DATA_DIRTY.__common: 0x158
   __DATA_DIRTY.__bss: 0x2180

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4A468051-3C84-3036-90C4-D2CF004C9837
-  Functions: 6211
-  Symbols:   2345
+  UUID: EC9D3374-527A-3D91-BFC4-6AF09B072AD6
+  Functions: 6215
+  Symbols:   2372
   CStrings:  573
 
Symbols:
+ _Img4DecodeHybridScheme3Sha384IM4C
+ _Img4DecodeHybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeLocalHybridScheme3Sha384IM4C
+ _Img4DecodeLocalHybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeLocalMLDSA87Sha384IM4C
+ _LocalHybridScheme3Sha384IM4C
+ _LocalHybridScheme3Sha384IM4C_len
+ _LocalMLDSA87Sha384IM4C
+ _LocalMLDSA87Sha384IM4C_len
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _ccmldsa87
+ _ccmldsa_import_pubkey
+ _ccmldsa_verify
+ _ccrsa_pub_init
+ _hybrid_scheme3_pubkey_cast
+ _hybrid_scheme3_pubkey_pad1
+ _hybrid_scheme3_pubkey_pad2
+ _hybrid_scheme3_signature_cast
+ _hybrid_scheme3_signature_pad1
+ _hybrid_scheme3_signature_pad2
+ _kImg4DecodeHybridScheme3Sha384IM4C
+ _kImg4DecodeHybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeLocalHybridScheme3Sha384IM4C
+ _kImg4DecodeLocalHybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeLocalMLDSA87Sha384IM4C
+ _swift_dynamicCastObjCClass
+ _verify_signature_hybrid_scheme3
+ _verify_signature_hybrid_scheme3_no_pqc
+ _verify_signature_ml_dsa_87
+ _verify_signature_rsa4096_fixed
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CloudAttestation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CloudAttestation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CloudAttestation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CloudAttestation

```
