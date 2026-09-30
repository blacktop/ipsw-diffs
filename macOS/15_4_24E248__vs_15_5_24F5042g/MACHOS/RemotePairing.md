## RemotePairing

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/RemotePairing`

```diff

-199.100.20.0.0
-  __TEXT.__text: 0xf72f4
+199.120.5.0.0
+  __TEXT.__text: 0xf8304
   __TEXT.__auth_stubs: 0x2dc0
   __TEXT.__objc_methlist: 0x9a4
-  __TEXT.__const: 0xbf94
-  __TEXT.__cstring: 0x7b5d
-  __TEXT.__oslogstring: 0x435b
-  __TEXT.__swift5_typeref: 0x3b44
-  __TEXT.__swift5_fieldmd: 0x38b4
-  __TEXT.__constg_swiftt: 0x4150
+  __TEXT.__const: 0xc094
+  __TEXT.__cstring: 0x7c1d
+  __TEXT.__oslogstring: 0x444b
+  __TEXT.__swift5_typeref: 0x3b5c
+  __TEXT.__swift5_fieldmd: 0x3910
+  __TEXT.__constg_swiftt: 0x4188
   __TEXT.__swift5_builtin: 0x2d0
-  __TEXT.__swift5_reflstr: 0x2ebd
-  __TEXT.__swift5_assocty: 0x408
+  __TEXT.__swift5_reflstr: 0x2f2d
+  __TEXT.__swift5_assocty: 0x420
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__swift5_proto: 0xba4
-  __TEXT.__swift5_types: 0x438
-  __TEXT.__swift5_capture: 0x1f14
+  __TEXT.__swift5_proto: 0xbb4
+  __TEXT.__swift5_types: 0x440
+  __TEXT.__swift5_capture: 0x1f20
   __TEXT.__swift5_mpenum: 0x1e0
-  __TEXT.__unwind_info: 0x4ac0
+  __TEXT.__unwind_info: 0x4b00
   __TEXT.__eh_frame: 0x3ef0
   __TEXT.__objc_classname: 0x82
   __TEXT.__objc_methname: 0x10a9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x578
   __AUTH_CONST.__auth_got: 0x16e8
-  __AUTH_CONST.__auth_ptr: 0xa20
-  __AUTH_CONST.__const: 0xbb88
+  __AUTH_CONST.__auth_ptr: 0xa28
+  __AUTH_CONST.__const: 0xbcb0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x37f8
   __AUTH.__objc_data: 0xff0

   __DATA.__objc_classrefs: 0x118
   __DATA.__objc_superrefs: 0x30
   __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x3801
+  __DATA.__data: 0x3879
   __DATA.__swift56_hooks: 0xb0
-  __DATA.__bss: 0x16398
+  __DATA.__bss: 0x16518
   __DATA.__common: 0xb0
   - /Library/Apple/System/Library/PrivateFrameworks/Mercury.framework/Versions/A/Mercury
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8935
-  Symbols:   3963
-  CStrings:  1273
+  Functions: 8967
+  Symbols:   3973
+  CStrings:  1279
 
Symbols:
+ _associated conformance 13RemotePairing8DefaultsV0B21ViaLockdownPreferenceOSHAASQ
+ _symbolic _____ 13RemotePairing24ControlChannelConnectionC33OutOfBandPairSetupDecisionHandlerV
+ _symbolic _____ 13RemotePairing8DefaultsV0B21ViaLockdownPreferenceO
+ _symbolic _____Iegn_ 13RemotePairing24ControlChannelConnectionC33OutOfBandPairSetupDecisionHandlerV
+ _symbolic _____ytIegnr_ 13RemotePairing24ControlChannelConnectionC33OutOfBandPairSetupDecisionHandlerV
+ _symbolic y_____cSg 13RemotePairing24ControlChannelConnectionC33OutOfBandPairSetupDecisionHandlerV
+ _symbolic y_____cyYbc 13RemotePairing0B7OutcomeO
+ _symbolic yyYbc
+ block_copy_helper.199
+ block_copy_helper.210
+ block_copy_helper.213
+ block_copy_helper.216
+ block_descriptor.201
+ block_descriptor.212
+ block_descriptor.215
+ block_descriptor.218
+ block_destroy_helper.200
+ block_destroy_helper.211
+ block_destroy_helper.214
+ block_destroy_helper.217
+ objectdestroy.143Tm
+ objectdestroy.190Tm
+ objectdestroy.8Tm
- _symbolic _____Iegn_Iegg_ 13RemotePairing0B7OutcomeO
- _symbolic _____ytIegnr_ytIegnr_ 13RemotePairing0B7OutcomeO
- _symbolic yy_____ccSg 13RemotePairing0B7OutcomeO
- block_copy_helper.201
- block_copy_helper.212
- block_copy_helper.215
- block_copy_helper.218
- block_descriptor.203
- block_descriptor.214
- block_descriptor.217
- block_descriptor.220
- block_destroy_helper.202
- block_destroy_helper.213
- block_destroy_helper.216
- block_destroy_helper.219
- objectdestroy.137Tm
- objectdestroy.192Tm
- objectdestroy.9Tm
CStrings:
+ "%{public}s: Out-of-band PairSetup handler accepted ownership of pairing attempt"
+ "%{public}s: Out-of-band PairSetup handler declined ownership of pairing attempt. Will handle attempt using standard pairing flow"
+ "%{public}s: Will attempt to use out-of-band PairSetup handler to complete pairing"
+ "199.120.5"
+ "Only unauthenticated connections can initiate pairing. Current state is "
+ "createNewPairingsThroughLockdown"
+ "hostPairingViaLockdownPreference"
+ "never"
+ "upgradeExistingPairingsOnly"
- "%{public}s: Using configured out-of-band PairSetup handler to complete pairing"
- "199.100.20"
- "hostPreferPairingViaLockdown"

```
