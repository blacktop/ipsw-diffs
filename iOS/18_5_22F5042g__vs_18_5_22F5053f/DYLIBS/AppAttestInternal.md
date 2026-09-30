## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-109.3.0.0.0
-  __TEXT.__text: 0x65b38
+109.6.0.0.0
+  __TEXT.__text: 0x667e8
   __TEXT.__auth_stubs: 0x15b0
   __TEXT.__objc_methlist: 0x68c
   __TEXT.__const: 0x2cd0
-  __TEXT.__cstring: 0x5798
-  __TEXT.__oslogstring: 0x348a
-  __TEXT.__gcc_except_tab: 0x784
+  __TEXT.__cstring: 0x57b8
+  __TEXT.__oslogstring: 0x375a
+  __TEXT.__gcc_except_tab: 0x7d0
   __TEXT.__swift5_typeref: 0x9de
   __TEXT.__swift5_reflstr: 0xdf3
   __TEXT.__swift5_assocty: 0x1b0

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x23c
-  __TEXT.__unwind_info: 0xe90
+  __TEXT.__unwind_info: 0xe98
   __TEXT.__eh_frame: 0xba0
   __TEXT.__objc_classname: 0xe2
   __TEXT.__objc_methname: 0x1236

   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0xae8
-  __AUTH_CONST.__auth_ptr: 0x4b8
+  __AUTH_CONST.__auth_ptr: 0x4c0
   __AUTH_CONST.__const: 0x23a0
-  __AUTH_CONST.__cfstring: 0x1a60
+  __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x1768
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1290
-  Symbols:   778
-  CStrings:  1083
+  Functions: 1293
+  Symbols:   792
+  CStrings:  1098
 
Symbols:
+ _AppAttest_AppAttestation_SignWithTeamIdentifier
CStrings:
+ "%25s:%-5d App_id=%@, %@"
+ "%25s:%-5d Attempting to validate key. { referenceKey=%@ }"
+ "%25s:%-5d Client is not eligible for priv service."
+ "%25s:%-5d Client is not supported. { error=%@ }"
+ "%25s:%-5d Device attestation is not supported."
+ "%25s:%-5d Failed to allocate array for certificates."
+ "%25s:%-5d Failed to attest key, completion handler is nil."
+ "%25s:%-5d Failed to attest key, invalid server response. { response=%@, error=%@ }"
+ "%25s:%-5d Failed to create certificate."
+ "%25s:%-5d Failed to create device attestation request. { error=%@ }"
+ "%25s:%-5d Failed to validate device attestation entitlements. { error=%@ }"
+ "%25s:%-5d Invalid device attestation options. { options=%@ }"
+ "%25s:%-5d Invalid referenceKey. { referenceKey=%@ }"
+ "AppAttest (%@-109.6) - %@"
+ "CDhash"
+ "allowPrivAPI"
+ "com.apple.developer.devicecheck.app-attest-opt-in"
- "AppAttest (%@-109.3) - %@"
- "com.apple.developer.devicecheck.app-attest-optin"

```
