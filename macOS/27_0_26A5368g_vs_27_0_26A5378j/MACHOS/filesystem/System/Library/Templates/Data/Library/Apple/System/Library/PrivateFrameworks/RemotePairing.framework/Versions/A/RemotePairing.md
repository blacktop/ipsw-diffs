## RemotePairing

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/RemotePairing`

```diff

-  __TEXT.__text: 0x104ed8
+  __TEXT.__text: 0x10601c
   __TEXT.__objc_methlist: 0x9a4
-  __TEXT.__const: 0xd454
-  __TEXT.__cstring: 0x652d
-  __TEXT.__oslogstring: 0x4c9b
-  __TEXT.__swift5_typeref: 0x3f20
-  __TEXT.__swift5_fieldmd: 0x3ac8
-  __TEXT.__constg_swiftt: 0x43e4
-  __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0x31bd
+  __TEXT.__const: 0xd5a4
+  __TEXT.__cstring: 0x658d
+  __TEXT.__oslogstring: 0x4dfb
+  __TEXT.__swift5_typeref: 0x3fb0
+  __TEXT.__swift5_fieldmd: 0x3b60
+  __TEXT.__constg_swiftt: 0x44d4
+  __TEXT.__swift5_builtin: 0x2d0
+  __TEXT.__swift5_reflstr: 0x322d
   __TEXT.__swift5_assocty: 0x4b0
-  __TEXT.__swift5_protos: 0x58
-  __TEXT.__swift5_proto: 0xbfc
-  __TEXT.__swift5_types: 0x454
-  __TEXT.__swift5_capture: 0x3250
-  __TEXT.__swift5_mpenum: 0x1d0
-  __TEXT.__unwind_info: 0x4dd8
+  __TEXT.__swift5_protos: 0x5c
+  __TEXT.__swift5_proto: 0xc04
+  __TEXT.__swift5_types: 0x464
+  __TEXT.__swift5_capture: 0x328c
+  __TEXT.__swift5_mpenum: 0x1e4
+  __TEXT.__unwind_info: 0x4e50
   __TEXT.__eh_frame: 0x36e8
   __TEXT.__objc_stubs: 0x1120
   __TEXT.__auth_stubs: 0x2d60
-  __TEXT.__objc_classname: 0x7bc
-  __TEXT.__objc_methname: 0x2570
+  __TEXT.__objc_classname: 0x83c
+  __TEXT.__objc_methname: 0x25c0
   __TEXT.__objc_methtype: 0x618
   __DATA_CONST.__const: 0x9c0
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x588
   __DATA_CONST.__got: 0x5f0
-  __AUTH_CONST.__const: 0xf4e0
+  __AUTH_CONST.__const: 0xf648
   __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x38e8
+  __AUTH_CONST.__objc_const: 0x3a50
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0x16a8
   __AUTH.__objc_data: 0x10a0
-  __AUTH.__data: 0x2760
+  __AUTH.__data: 0x28c0
   __AUTH.__s_async_hook: 0x1a0
   __DATA.__objc_protorefs: 0x88
   __DATA.__objc_classrefs: 0x120
   __DATA.__objc_superrefs: 0x30
   __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x3d81
+  __DATA.__data: 0x3d91
   __DATA.__swift56_hooks: 0xb0
   __DATA.__bss: 0x16d18
   __DATA.__common: 0xd0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9986
-  Symbols:   5348
-  CStrings:  1341
+  Functions: 10035
+  Symbols:   5366
+  CStrings:  1351
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__s_async_hook : content changed
~ __DATA.__objc_protorefs : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ __DATA__TtC13RemotePairing35AlwaysApprovePairingPolicyValidator
+ __DATA__TtC13RemotePairing35AlwaysDeclinePairingPolicyValidator
+ __IVARS__TtC13RemotePairing35AlwaysDeclinePairingPolicyValidator
+ __METACLASS_DATA__TtC13RemotePairing35AlwaysApprovePairingPolicyValidator
+ __METACLASS_DATA__TtC13RemotePairing35AlwaysDeclinePairingPolicyValidator
+ __swift_closure_destructor.151Tm
+ __swift_closure_destructor.285Tm
+ __swift_closure_destructor.327Tm
+ _symbolic $s13RemotePairing0B15PolicyValidatorP
+ _symbolic Sb14promptRequired_t
+ _symbolic _____ 13RemotePairing013AlwaysApproveB15PolicyValidatorC
+ _symbolic _____ 13RemotePairing013AlwaysDeclineB15PolicyValidatorC
+ _symbolic _____ 13RemotePairing0B23PolicyValidationOutcomeO
+ _symbolic _____ 13RemotePairing19DeveloperModeStatusO
+ _symbolic _____Iegn_Sg 13RemotePairing0B7OutcomeO
+ _symbolic _____Sg 13RemotePairing0B4DataV
+ _symbolic _____Sg18initialPairingData_t 13RemotePairing0B4DataV
+ _symbolic ______p 13RemotePairing0B15PolicyValidatorP
- __swift_closure_destructor.150Tm
- __swift_closure_destructor.192Tm
CStrings:
+ "%{public}s: Pairing policy allowed; configuring pairing session"
+ "%{public}s: Pairing policy validation completed but connection is no longer in correct state to handle response"
+ "%{public}s: Rejecting PairSetup because ManagedConfiguration requires a challenge response and this flow has no return path to deliver one"
+ "%{public}s: Rejecting PairSetup because pairing policy rejected the attempt: %{public}s"
+ "%{public}s: _doConfigureNewPairingSession"
+ "280.0.5"
+ "Developer mode must be enabled on the device."
+ "_TtC13RemotePairing35AlwaysApprovePairingPolicyValidator"
+ "_TtC13RemotePairing35AlwaysDeclinePairingPolicyValidator"
+ "_rejectionError"
+ "pairingPolicyValidator"
+ "security.mac.amfi.developer_mode_status.changed"
- "%{public}s: Not requesting user consent for pairing attempt as requireUserConsentForPairing is set to false"
- "280"

```
