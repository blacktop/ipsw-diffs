## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

```diff

-126.0.0.0.0
-  __TEXT.__cstring: 0x4907
-  __TEXT.__const: 0x148
-  __TEXT.__os_log: 0x606
-  __TEXT_EXEC.__text: 0x1c444
+128.0.0.0.0
+  __TEXT.__cstring: 0x4cc9
+  __TEXT.__const: 0x218
+  __TEXT.__os_log: 0x61f
+  __TEXT_EXEC.__text: 0x1d54c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
-  __DATA.__common: 0x90
+  __DATA.__common: 0x88
   __DATA.__bss: 0x99
   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x98

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xbd8
   __DATA_CONST.__kalloc_type: 0x400
-  __DATA_CONST.__kalloc_var: 0x1400
-  UUID: DB96F965-CC87-36F7-B1F9-54587BF40FD1
-  Functions: 317
+  __DATA_CONST.__kalloc_var: 0x14a0
+  UUID: 2ADF74C0-D8F9-3BC7-881D-1595F6CAFA73
+  Functions: 324
   Symbols:   0
-  CStrings:  603
+  CStrings:  624
 
CStrings:
+ "!preflightFound || allowPreflightParameter"
+ "*resultLength >= respDataSize"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "ButtonStates: %lu Index: %lu State: %lu Filter: %d Synthetic: %d"
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
- "ButtonStates: %lu Index: %lu State: %lu"
- "cred->numCredSets <= 80"

```
