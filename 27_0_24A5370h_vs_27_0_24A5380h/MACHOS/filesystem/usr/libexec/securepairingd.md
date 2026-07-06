## securepairingd

> `/usr/libexec/securepairingd`

```diff

-  __TEXT.__text: 0x467d4
-  __TEXT.__auth_stubs: 0x1700
+  __TEXT.__text: 0x4c6d0
+  __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_stubs: 0xc0
-  __TEXT.__const: 0x7788
-  __TEXT.__constg_swiftt: 0x1ee4
-  __TEXT.__swift5_typeref: 0x167f
+  __TEXT.__const: 0x7e68
+  __TEXT.__constg_swiftt: 0x1fec
+  __TEXT.__swift5_typeref: 0x17f9
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x268
+  __TEXT.__swift5_types: 0x280
   __TEXT.__objc_classname: 0x6b7
-  __TEXT.__objc_methname: 0x1c8
-  __TEXT.__swift5_reflstr: 0x824
-  __TEXT.__swift5_fieldmd: 0x170c
-  __TEXT.__swift5_capture: 0x3f0
-  __TEXT.__oslogstring: 0x10ed
-  __TEXT.__cstring: 0xf90
-  __TEXT.__swift5_assocty: 0x2a8
-  __TEXT.__swift5_proto: 0x75c
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x20
-  __TEXT.__swift_as_cont: 0x7c
+  __TEXT.__objc_methname: 0x1ef
+  __TEXT.__swift5_reflstr: 0x864
+  __TEXT.__swift5_fieldmd: 0x17fc
+  __TEXT.__swift5_capture: 0x4a4
+  __TEXT.__oslogstring: 0x129d
+  __TEXT.__cstring: 0x1060
+  __TEXT.__swift5_assocty: 0x2d8
+  __TEXT.__swift5_proto: 0x7d0
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__swift_as_cont: 0x94
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methtype: 0x2e
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x1510
-  __TEXT.__eh_frame: 0x2b58
-  __DATA_CONST.__const: 0x42a0
+  __TEXT.__unwind_info: 0x1660
+  __TEXT.__eh_frame: 0x2e00
+  __DATA_CONST.__const: 0x46e8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xb88
+  __DATA_CONST.__auth_got: 0xbc0
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__auth_ptr: 0x3d0
-  __DATA.__objc_const: 0x1938
+  __DATA_CONST.__auth_ptr: 0x3e0
+  __DATA.__objc_const: 0x1978
   __DATA.__objc_selrefs: 0x30
-  __DATA.__data: 0x3052
-  __DATA.__bss: 0xdc20
+  __DATA.__data: 0x3242
+  __DATA.__bss: 0xe9a0
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1759
-  Symbols:   570
-  CStrings:  269
+  Functions: 1861
+  Symbols:   577
+  CStrings:  285
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__common : content changed
Symbols:
+ _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeys6UInt32VSgAFm_xtKF
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyys6UInt32VSg_xtKF
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _os_transaction_create
CStrings:
+ ".sigmaLeadPairing("
+ "Invalid key value while decoding result type for unpairAll"
+ "SecurePairingXPCService.ServiceState.addSession session=%s"
+ "SecurePairingXPCService.ServiceState.removeSession session=%s"
+ "SecurePairingXPCService.ServiceState.setClientCancelled()"
+ "awaitSessionRemoval(for:)"
+ "com.apple.securepairing.pairingSession.lead."
+ "created transaction and parked task for %s"
+ "processing XPC request sigmaSessionEnded for pairingID=%llu"
+ "released transaction and parked task for %s"
+ "session not added - client cancelled"
+ "sessionContinuations"
+ "sigmaSessionEnded"
+ "unpairAll"
+ "useDak"

```
