## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-2319.0.46.0.0
-  __TEXT.__text: 0x19f28
-  __TEXT.__objc_methlist: 0x1dc8
+2319.0.63.0.0
+  __TEXT.__text: 0x1a174
+  __TEXT.__objc_methlist: 0x1de0
   __TEXT.__const: 0x118
   __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__cstring: 0xe91
-  __TEXT.__oslogstring: 0x14ec
-  __TEXT.__unwind_info: 0x788
+  __TEXT.__oslogstring: 0x153f
+  __TEXT.__unwind_info: 0x790
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1198
+  __DATA_CONST.__objc_selrefs: 0x11a0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x38

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 629
-  Symbols:   1807
-  CStrings:  262
+  Functions: 633
+  Symbols:   1811
+  CStrings:  263
 
Symbols:
+ -[MechanismBase canRecoverFromError:]
+ -[MechanismBaseComposite canRecoverFromError:]
+ GCC_except_table57
+ GCC_except_table80
+ _OUTLINED_FUNCTION_2
+ _objc_msgSend$canRecoverFromError:
- GCC_except_table56
- GCC_except_table79
Functions:
+ -[MechanismBaseComposite canRecoverFromError:]
+ -[MechanismBase canRecoverFromError:]
~ -[MechanismBase subMechanismRequestsRestart:reconnectRemoteUI:] : 108 -> 152
+ _OUTLINED_FUNCTION_2
~ -[MechanismBase isTCCAllowedWithAuditTokenData:optionAuditTokenData:forcePrompt:auditTokenUsage:error:].cold.1 : 60 -> 56
~ -[MechanismBase tccPreflightWithAuditTokenData:auditTokenUsage:].cold.1 : 76 -> 72
~ -[MechanismBase externalizedContext].cold.1 : 60 -> 56
+ -[MechanismBase subMechanismRequestsRestart:reconnectRemoteUI:].cold.1
CStrings:
+ "%{public}@ dropping restart request from %{public}@: isRunning but not a composite"
```
