## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

```diff

-71.120.2.0.0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x4320
-  __TEXT_EXEC.__text: 0x13b94
+80.0.0.502.1
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x46e2
+  __TEXT_EXEC.__text: 0x1467c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
-  __DATA.__common: 0x40
+  __DATA.__common: 0x38
   __DATA.__bss: 0x19
   __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x28

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
-  __DATA_CONST.__kalloc_var: 0x1400
-  UUID: B9525377-BD28-3C66-9B16-4E2C9FF08BAF
-  Functions: 196
+  __DATA_CONST.__kalloc_var: 0x14a0
+  UUID: 0D83FAEC-9346-3642-BF2D-EBCD308C641D
+  Functions: 205
   Symbols:   0
-  CStrings:  469
+  CStrings:  490
 
CStrings:
+ "!preflightFound || allowPreflightParameter"
+ "*resultLength >= respDataSize"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "LibCall_ACMContextContainsCredentialTypeEx"
+ "LibCall_ACMContextCopyData"
+ "LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx"
+ "LibSer_ACMDeserializeEnvironmentVariableType"
+ "LibSer_ACMDeserializeSEPControlCode"
+ "command && commandSize >= sizeof(ACMSEPControlCode)"
+ "context && outSize"
+ "context && outSize && outBuffer"
+ "cred->numCredSets <= kACMContextPoolTotalCount"
+ "inData && inSize"
+ "inSize >= sizeof(ACMEnvironmentVariable)"
+ "nonAutoDisposable requires tracking support"
+ "param.parameterData && param.parameterDataLength == sizeof(uint8_t)"
+ "requirement->type == kACMRequirementTypePushButtonPressed"
+ "requirementSize <= reqSize"
+ "site.ACMRequirement.ACMRequirementDataPushButton"
+ "sourceContextExternalForm && sourceContextExternalFormLength == sizeof(ACMHandle)"
+ "targetContextExternalForm && targetContextExternalFormLength == sizeof(ACMHandle)"
+ "trackingSupported || !nonAutoDisposableRequested"
+ "transport && context"
- "*resultLength >= dataSize"
- "cred->numCredSets <= 80"

```
