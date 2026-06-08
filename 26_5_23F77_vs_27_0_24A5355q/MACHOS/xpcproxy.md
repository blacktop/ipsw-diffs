## xpcproxy

> `/usr/libexec/xpcproxy`

```diff

-3102.120.13.0.0
-  __TEXT.__text: 0x5d98
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xd67
-  __TEXT.__oslogstring: 0x1692
+3295.0.0.502.1
+  __TEXT.__text: 0x98a8
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__lazy_helpers: 0x150
+  __TEXT.__const: 0x190
   __TEXT.__xpcproxy: 0x1
+  __TEXT.__oslogstring: 0x1696
+  __TEXT.__cstring: 0x19da
   __TEXT.__dof_launchd: 0x2e5
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x598
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x188
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__got: 0x88
+  __DATA.__lazy_load_got: 0x20
   __DATA.__os_assumes_log: 0x8
-  __DATA.__data: 0x20
+  __DATA.__data: 0x24
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x91
-  - /usr/lib/libCoreEntitlements.dylib
+  __DATA.__common: 0x1
+  __DATA.__bss: 0x90
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
