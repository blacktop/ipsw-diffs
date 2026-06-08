## MechPearl

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl`

```diff

-2005.120.18.0.0
-  __TEXT.__text: 0x88c8
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x1640
-  __TEXT.__objc_methlist: 0x5ec
+2305.0.0.0.1
+  __TEXT.__text: 0x77cc
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x5b4
   __TEXT.__const: 0xd0
-  __TEXT.__objc_methname: 0x18b8
-  __TEXT.__oslogstring: 0x77c
-  __TEXT.__cstring: 0x38b
-  __TEXT.__objc_classname: 0xea
-  __TEXT.__objc_methtype: 0x61e
-  __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x528
+  __TEXT.__objc_methname: 0x17ef
+  __TEXT.__oslogstring: 0x5fc
+  __TEXT.__cstring: 0x395
+  __TEXT.__objc_classname: 0xde
+  __TEXT.__objc_methtype: 0x5ff
+  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__unwind_info: 0x290
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x838
-  __DATA.__objc_selrefs: 0x780
-  __DATA.__objc_ivar: 0x74
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x2f0
+  __DATA.__objc_const: 0x808
+  __DATA.__objc_selrefs: 0x758
+  __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x14
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E962D10B-6BF3-3B69-B421-D18C51D14334
-  Functions: 143
-  Symbols:   172
-  CStrings:  481
+  UUID: 99162D90-7F44-303B-AA3A-080F8DCC065D
+  Functions: 128
+  Symbols:   166
+  CStrings:  464
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _LACEventProcessingMirroringTypeNone
- _LACEventProcessingOptionMirrorDefaultUI
- _LACEventSimpleStatusFaceIDPrepareSecureUI
- _LACLogBiometry
- _LACPolicyOptionEventProcessing
- _LACPurposeSecureUIRecording
- _OBJC_CLASS_$_LACSecureFaceIDUIUtilities
- __dispatch_main_q
- _objc_release_x10
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
- "%{public}@ failed to pause after secure UI movement: %{public}@"
- "%{public}@ is waiting for custom UI client to prepare secure UI"
- "%{public}@ is waiting for mirrored default UI to prepare secure UI"
- "%{public}@ paused after secure UI movement"
- "%{public}@ received reply from custom UI client"
- "%{public}@ received reply from mirrored default UI"
- "%{public}@ restarting after secure UI movement"
- "@\"<LACRemoteUI>\""
- "T@\"<LACRemoteUI>\",W,N,V_remoteUiDelegate"
- "_pauseFaceIdAfterSecureUIMovement"
- "_prepareCustomSecureUiWithCompletion:"
- "_remoteUiDelegate"
- "handleUIEvent:params:"
- "isActive"
- "responseEventWithParams:timeout:reply:"
- "v32@0:8q16@24"

```
