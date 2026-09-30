## xpcproxy

> `/usr/libexec/xpcproxy`

```diff

-3102.120.13.0.0
-  __TEXT.__text: 0x5d98 sha256:9934742c93e323b84c1c6b0e08358f08d25e0e7e3949059ab8891d88ce6f581b
-  __TEXT.__auth_stubs: 0xb30 sha256:577a8f89cf70f4394f35a597dd3c796ffb91e3bab6e0ad5651756c027601b0c4
-  __TEXT.__const: 0x80 sha256:ede4ecf3de3e7adf6e565f67be7fcf919637d2662a4a170c88efeff7c4086a8f
-  __TEXT.__cstring: 0xd67 sha256:41b88d15236d12990427ba64dc8fe759f7b5e2f35241fba51bbda7b73ba575d2
-  __TEXT.__oslogstring: 0x1692 sha256:4d0fa5f2956669300079d03818168d8677f61ee749e2f674a4da8ea1522aae02
+3295.0.0.502.1
+  __TEXT.__text: 0x98a8 sha256:4858a5d333209d30cb191e089389ee37b262177c59be15bc40585ea32d07696c
+  __TEXT.__auth_stubs: 0xb00 sha256:b161e5e4cacddebb108562603e53f0d23525c437074a509d101af6849e404dd8
+  __TEXT.__lazy_helpers: 0x150 sha256:e5cafcd99a3c3f24ba9c3a8ad393158fab2f0bd1a406fca5118e1af001107c46
+  __TEXT.__const: 0x190 sha256:4bb854e623f68ae705eb2cbe6a4de6ce830ec75e908504d1f4a660ed0b92bedd
   __TEXT.__xpcproxy: 0x1 sha256:4bf5122f344554c53bde2ebb8cd2b7e3d1600ad631c385a5d7cce23c7785459a
-  __TEXT.__dof_launchd: 0x2e5 sha256:b906717f968eb8ba1d3772f6ed105ecbe9ec4d751326e5fc8818662df096ec75
-  __TEXT.__unwind_info: 0x140 sha256:e2a91c9f699ea06bf555bf3bf23a19d0a2cbffb4818ffa806fa49fe2518bfe02
-  __DATA_CONST.__auth_got: 0x598 sha256:64108c45cdabe7b34da3c788b212d522fa39c215950bcae8a8386a5b00ca425f
-  __DATA_CONST.__got: 0x90 sha256:be408e32425fd4bc7e2f53e6a979479ed55de39b1256560918df4f8b319ecd79
-  __DATA_CONST.__const: 0x188 sha256:fa65ef93e6caae8e7729a6c786bee8dffffffeb81364c8b630c711765caeb843
-  __DATA.__os_assumes_log: 0x8 sha256:536b6a007b2ac6a8d64586cfb2b0a082b9b8100ad8480989e478f1c719a85932
-  __DATA.__data: 0x20 sha256:b7ec72d1762fab289d51ddd50421800728e2a9b97fdde74b83c56a68c63cf47a
+  __TEXT.__oslogstring: 0x1696 sha256:807ffc965eb221d2e610fe6cecd04d7ea5e8fead1c1f49f408d9ce0fffeacdac
+  __TEXT.__cstring: 0x19da sha256:c6ab69c23b2552914108a4c0100185ef89ec2b8b8b6c82a05120144609729104
+  __TEXT.__dof_launchd: 0x2e5 sha256:5b73ed2424117db3a028b94693685615696f35534880c2b468d8e55519ff8a78
+  __TEXT.__unwind_info: 0x178 sha256:2187cc845f2a806bafaa29f88873c22f5d25dd2636953f57a64530c3d911f7df
+  __DATA_CONST.__const: 0x248 sha256:e90067eafce0fd5b995367ae0167d6e420e2d422556c0a23b3b4df47bc483f40
+  __DATA_CONST.__auth_got: 0x580 sha256:b06439eb98e9373b2e46de6237f1c238cc06cdd5145d483aa3fc78965f75e99c
+  __DATA_CONST.__got: 0x88 sha256:7f1f796a47ae8a09d56fa2b0c5e4bf9114e7b46a071d1d5ca0fcd996cdc99701
+  __DATA.__lazy_load_got: 0x20 sha256:67db376862b3c97a7891a07dbd40412d40fc492e6e3036284d228ba01a1a58ec
+  __DATA.__os_assumes_log: 0x8 sha256:6e5b8f37d49aaac9fb4753a4e642d4d428f238ed916f870235e0dcad7f7dc2fa
+  __DATA.__data: 0x24 sha256:eb81084f2823a0779393c4deee865a3a2b1fcfbacf92694fcca3896a33b0fb2a
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
-  __DATA.__bss: 0x91 sha256:c38f1294a259a7e943728e76d1a9d2e0992d22f4cebf6de1fb42204e7126d19a
-  - /usr/lib/libCoreEntitlements.dylib
+  __DATA.__common: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
+  __DATA.__bss: 0x90 sha256:81c611f35bff79491538b2f7cf201c7597a661a5c549633541c62bdc8af1613f
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libcryptex_trampoline.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/libsandbox.1.dylib
-  UUID: 4AEDFA96-B217-3C44-8FDB-539A8DF51C35
-  Functions: 121
+  UUID: 4652E212-F05A-3FD7-AEFE-FE5F494E1BE0
+  Functions: 92
   Symbols:   199
-  CStrings:  201
+  CStrings:  297
 
Symbols:
+ __dyld_lazy_load
+ _cc_clear
+ _ccder_blob_decode_len
+ _ccder_blob_decode_range
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_decode_tag
+ _ccder_blob_decode_tl
+ _ccder_blob_encode_body_tl
+ _ccder_blob_encode_tl
+ _ccder_blob_reserve_tl
+ _ccder_sizeof
+ _memchr
+ _memcmp
+ _posix_spawnattr_set_use_sanitizers_np
- _CEAcquireUnmanagedContext
- _CESerializeWithOptions
- _CESizeSerialization
- _CEValidateWithOptions
- _der_vm_CEType_from_context
- _der_vm_bool_from_context
- _der_vm_context_is_valid
- _der_vm_data_from_context
- _der_vm_execute
- _der_vm_integer_from_context
- _der_vm_iterate
- _der_vm_string_from_context
- _kCENoError
- _sleep
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Tue May 26 21:31:49 PDT 2026; root:libxpc_executables-3295.0.0.502.1~1/xpcproxy/RELEASE_ARM64E"
+ "A memory allocation has failed"
+ "API Misuse"
+ "Attempting to select a boolean value from a non-boolean DER object"
+ "Attempting to select a data value from a non-data DER object"
+ "Attempting to select a string value from a non-string DER object"
+ "Attempting to select an integer value from a non-integer DER object"
+ "B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8"
+ "CEValidateWithOptions"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Tue May 26 21:31:49 PDT 2026; root:libxpc_executables-3295.0.0.502.1~1/xpcproxy/RELEASE_ARM64E"
+ "Entitlements element not allowed"
+ "Invalid Arguments"
+ "Not eligible for acceleration"
+ "OK"
+ "Query cannot be satisfied"
+ "String contains an embedded NUL"
+ "UTC Time element not allowed"
+ "Unexpected type to match against"
+ "Unexpected type to match against during iteration"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown boolean encoding"
+ "Unknown data encoding"
+ "Unknown numeric string encoding"
+ "Unknown string encoding"
+ "Verification failed"
+ "[%s]: entitlements blob has unexpected version %lld\n"
+ "array decoding failure"
+ "assertion failure: \"posix_spawnattr_set_use_sanitizers_np(&ctx->psattr, attr->sanitizer_flags)\" -> %llu"
+ "bool decode failure"
+ "boolean should be exactly 1 byte"
+ "could not decode size for next DER sub-sequence"
+ "could not decode tag for next DER sub-sequence"
+ "data element not allowed"
+ "der_decode_boolean"
+ "der_decode_data"
+ "der_decode_entitlements"
+ "der_decode_key_value"
+ "der_decode_next"
+ "der_decode_number"
+ "der_decode_numeric_string"
+ "der_decode_string"
+ "der_decode_utc_time"
+ "der_validate_array"
+ "der_validate_dictionary"
+ "der_vm_bool_from_context"
+ "der_vm_data_from_context"
+ "der_vm_execute_integer_value_allowed"
+ "der_vm_execute_match_bool"
+ "der_vm_execute_match_integer"
+ "der_vm_execute_match_string"
+ "der_vm_execute_match_string_prefix"
+ "der_vm_execute_nocopy"
+ "der_vm_execute_select_index"
+ "der_vm_execute_select_key"
+ "der_vm_execute_select_longest_matching_key"
+ "der_vm_execute_string_prefix_value_allowed"
+ "der_vm_execute_string_value_allowed"
+ "der_vm_integer_from_context"
+ "der_vm_iterate_b"
+ "der_vm_string_from_context"
+ "dictionary decoding failure"
+ "dictionary key / value decoding failure"
+ "dictionary key is not a valid string"
+ "dictionary keys are not sorted or not unique"
+ "dictionary value verification failure"
+ "encountered invalid element in an array"
+ "encountered invalid element in an iterable"
+ "encountered invalid tag"
+ "entitlements blob does not have CCDER_CONSTRUCTED_SET coding"
+ "entitlements blob does not have CCDER_ENTITLEMENTS coding"
+ "entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element"
+ "extra data at the end of element"
+ "integer_allowed_iterate"
+ "invalid arguments passed in"
+ "invalid dictionary element"
+ "invalid tag or length"
+ "iterable decoding failure"
+ "iteration over a non-iterable type"
+ "key / value decoding failure"
+ "key contains an embedded NUL"
+ "key length is invalid"
+ "key-value pair contains extra elements"
+ "noop"
+ "number too large"
+ "numeric string element not allowed"
+ "recursion limit reached"
+ "recursivelyValidateEntitlements"
+ "string decode failure"
+ "string_prefix_allowed_iterate"
+ "string_value_allowed_iterate"
+ "sub-sequence size is larger than sequence size"
+ "unable to decode value size for key-value pair"
+ "unable to decode value tag for key-value pair"
+ "unhandled opcode"
+ "unknown number encoding"
+ "validate_V0"
+ "validate_VNext"
+ "xml-looking blob was passed in"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Apr 18 18:25:47 PDT 2026; root:libxpc_executables-3102.120.13~110/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Apr 18 18:25:47 PDT 2026; root:libxpc_executables-3102.120.13~110/xpcproxy/RELEASE_ARM64E"
- "assertion failure: \"posix_spawnattr_set_max_addr_np(&ctx->psattr, 18446744073709551615ULL)\" -> %llu"

```
