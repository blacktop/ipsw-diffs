## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-140.0.0.0.1
-  __TEXT.__text: 0xf96c0
+166.40.0.502.1
+  __TEXT.__text: 0xfa350
   __TEXT.__auth_stubs: 0x2130
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x8a10
-  __TEXT.__cstring: 0x227f
-  __TEXT.__constg_swiftt: 0x21dc
-  __TEXT.__swift5_typeref: 0x1e05
-  __TEXT.__swift5_reflstr: 0x20f2
-  __TEXT.__swift5_fieldmd: 0x294c
+  __TEXT.__const: 0x8b90
+  __TEXT.__cstring: 0x255f
+  __TEXT.__constg_swiftt: 0x2230
+  __TEXT.__swift5_typeref: 0x1def
+  __TEXT.__swift5_reflstr: 0x2162
+  __TEXT.__swift5_fieldmd: 0x29c4
   __TEXT.__swift5_assocty: 0x390
-  __TEXT.__swift5_proto: 0x828
-  __TEXT.__swift5_types: 0x328
+  __TEXT.__swift5_proto: 0x848
+  __TEXT.__swift5_types: 0x334
   __TEXT.__swift5_capture: 0xe0
-  __TEXT.__oslogstring: 0x19fb
+  __TEXT.__oslogstring: 0x1c6b
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x9c
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x38b0
+  __TEXT.__unwind_info: 0x38e8
   __TEXT.__eh_frame: 0x64d8
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x35e
+  __TEXT.__objc_methname: 0x36a
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__got: 0x580
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_protorefs: 0x10
   __AUTH_CONST.__auth_got: 0x1098
-  __AUTH_CONST.__auth_ptr: 0x948
-  __AUTH_CONST.__const: 0x4c80
+  __AUTH_CONST.__auth_ptr: 0x910
+  __AUTH_CONST.__const: 0x4d70
   __AUTH_CONST.__objc_const: 0x738
   __AUTH.__objc_data: 0x1b0
-  __AUTH.__data: 0x2610
-  __DATA.__data: 0x27e8
-  __DATA.__common: 0x730
-  __DATA.__bss: 0xf400
+  __AUTH.__data: 0x2540
+  __DATA.__data: 0x2770
+  __DATA.__common: 0x758
+  __DATA.__bss: 0xf600
+  __DATA_DIRTY.__data: 0xf8
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4473
-  Symbols:   262
-  CStrings:  448
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4487
+  Symbols:   271
+  CStrings:  459
 
Symbols:
+ _OBJC_CLASS_$_NSError
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "AttestationBundle passed SEPImagePolicy: reported SEP Image from AP Ticket matches SEP attestation"
+ "Ensemble member fingerprints not found in secure-config"
+ "Ensemble member fingerprints not found in secure-config, failing open"
+ "EnsembleTopologyPolicy"
+ "Failed to read cryptexes from %!{(MISSING)public}s"
+ "Inclusion proof has expired: %!@(MISSING)"
+ "Inclusion proof verification failed: %!@(MISSING)"
+ "MIICSTCCAc+gAwIBAgIQFWHuWdy1oSD2UDkBanlRATAKBggqhkjOPQQDAzBmMS0wKwYDVQQDDCREYXRhIENlbnRlciBBdHRlc3RhdGlvbiBSb290IENBIC0gRzIxEzARBgNVBAoMCkFwcGxlIEluYy4xEzARBgNVBAgMCkNhbGlmb3JuaWExCzAJBgNVBAYTAlVTMB4XDTI0MDczMTIxMjc1OFoXDTQ5MDcyNTIxMjc1N1owZjEtMCsGA1UEAwwkRGF0YSBDZW50ZXIgQXR0ZXN0YXRpb24gUm9vdCBDQSAtIEcyMRMwEQYDVQQKDApBcHBsZSBJbmMuMRMwEQYDVQQIDApDYWxpZm9ybmlhMQswCQYDVQQGEwJVUzB2MBAGByqGSM49AgEGBSuBBAAiA2IABCkeSUWZ3YfTi9rG9PF4qfljMI1wUvTbZAjRGlBJsrkGRTaWivZB8yWwazoUhxsmG8VBSfiCNBbvczJcGRQCdZnzU9pqnUlPPa70dVUdI98IEnHq7O6KCNs2zlshQApBeqNCMEAwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQU/u8RHTmJaLaDQzmKBdtctZ8gThkwDgYDVR0PAQH/BAQDAgEGMAoGCCqGSM49BAMDA2gAMGUCMFlR1J7jG1qo4zhue+x84CaRQfjUHvBAOq4BwQShRKVNt0luhOEWIHrJ3ytA3WJ9jgIxAKrhOP/wp7grFfQLz3CcSB9KBLOGOLZNzYxAzUuTmh4m/QS2L9z1yvnmGg5MFnnZtg=="
+ "Observed Cryptex Lockdown State: %!{(MISSING)bool}d"
+ "Software %!{(MISSING)public}s has expired in the transparency log"
+ "Software %!{(MISSING)public}s is not included in transparency log, this is likely indicative of using the wrong transparency log"
+ "Validated darwin-init not available"
+ "Validated darwin-init not available, failing open"
+ "code"
+ "com.apple.SWTATLeafDataError"
+ "com.apple.SWTATLogProofsError"
+ "domain"
- "C7D3A072-B217-4920-A022-47818D05B1CB"
- "Failed to read cryptexes from either %!{(MISSING)public}s"
- "Software %!{(MISSING)public}s is not included in transparency log"
- "requireSecureConfigEnsembleUDIDs"
- "requireSecureConfigRoutingHint"
- "strictKeyOptions"

```
