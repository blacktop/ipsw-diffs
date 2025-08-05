## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-2005.0.49.0.0
-  __TEXT.__text: 0x18078
+2005.0.60.0.0
+  __TEXT.__text: 0x18054
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x1da8
   __TEXT.__const: 0x128

   __TEXT.__oslogstring: 0x14f0
   __TEXT.__unwind_info: 0x780
   __TEXT.__objc_classname: 0x404
-  __TEXT.__objc_methname: 0x4dc9
+  __TEXT.__objc_methname: 0x4dab
   __TEXT.__objc_methtype: 0xed3
-  __TEXT.__objc_stubs: 0x3a20
+  __TEXT.__objc_stubs: 0x3a00
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x920
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1218
+  __DATA_CONST.__objc_selrefs: 0x1210
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB7343AF-AF9C-34DF-81CF-459AC23050CA
+  UUID: F82F4208-4B91-3EAC-AD1D-89D1D46BE8BE
   Functions: 629
-  Symbols:   2516
-  CStrings:  1470
+  Symbols:   2515
+  CStrings:  1469
 
Symbols:
+ _objc_msgSend$preflightPolicy:parameters:maxGlobalCredentialAge:processRequirement:
- _objc_msgSend$acmParameters
- _objc_msgSend$preflightPolicy:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:
Functions:
~ -[MechanismRatchet _addBiometryConfirmationCredentialWithCompletion:] : 388 -> 352
CStrings:
+ "preflightPolicy:parameters:maxGlobalCredentialAge:processRequirement:"
- "acmParameters"
- "preflightPolicy:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:"

```
