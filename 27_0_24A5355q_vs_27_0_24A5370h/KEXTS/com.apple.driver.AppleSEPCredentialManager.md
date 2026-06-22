## com.apple.driver.AppleSEPCredentialManager

> `com.apple.driver.AppleSEPCredentialManager`

```diff

-944.0.0.0.0
-  __TEXT.__cstring: 0x13130 sha256:27163ff715c48b2c854efef81c933c055d48191d318a26718a8fa65e9fd9eab0
+949.0.4.0.0
+  __TEXT.__cstring: 0x13126 sha256:1d1605988e92f19702ea7b7d9ecac13475cf328595f83c5800572a5ceb0716d1
   __TEXT.__const: 0x420 sha256:f4b337ca0d76b78d4ba11a9e2e72d3c8c887f250508917fbf4ede7b7ba0ff2c3
-  __TEXT_EXEC.__text: 0x4d300 sha256:0705dc0ea8a4ebaca1e3f6a425476e565bfac7bf05a75994eb90fab2ab19384b
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3061 sha256:b31a93eec8b5e8f50cf603bc494f8ad3bf4081bc61ea831fdcaad961c50d6a77
+  __TEXT_EXEC.__text: 0x4dd10 sha256:eb6e64a5b67a59e3a8eff341862bd5e965e3b50fb05a75aab143af9032864907
+  __TEXT_EXEC.__auth_stubs: 0x660 sha256:78cd1f7b925aea0c4255830a2bb654a27d15c82ab7bce9c5b3e56385a2ba9077
+  __DATA.__data: 0x3061 sha256:ccc288b9d5dc1359ac8fb7fabd37296d6fb37d4a6b3915065775a6819f0162b2
   __DATA.__common: 0x9c8 sha256:b4a1781b4f9c0bf924a6d4385a2aa806cb1af3dd66c512982a88c87ff41dff5e
   __DATA.__bss: 0xf9 sha256:9fb3871386d4d5abf3149a8fce19470ba4385fdc156f5da4642ba86489f1414e
-  __DATA_CONST.__mod_init_func: 0x60 sha256:2981cf493f56069f11c907bae9a8ed7d3281d44982758fa9d71d48cac92314c7
-  __DATA_CONST.__mod_term_func: 0x60 sha256:3cdb1e3d783e06d77f58c32df58354745425f0a262ce4c9a9869be279cb27f37
-  __DATA_CONST.__const: 0x1dd0 sha256:05c4c6dcb2d3fab6d7cd4322c7531a099c2822ce4ce9f5646feacbbc74030985
-  __DATA_CONST.__kalloc_type: 0x5c0 sha256:fd16acfeb7081d6fd9bbfbce5df5ee735aa55df9eebe5ee90044194e45c91067
-  __DATA_CONST.__kalloc_var: 0x15e0 sha256:ce21f6ebe7663bc7dac09f8173d822ec333f85d440f4c77a6369e7a9c40f3c12
-  __DATA_CONST.__auth_got: 0x330 sha256:c77658cb1bceb364bace9320d6b26b198d0f4ec20dc0bc18cc81c957804598ea
-  __DATA_CONST.__got: 0xc8 sha256:ee688793f927ffa6dae6d3eeaa07cfad22ceda51923c95fa4b118d4065da7598
-  __DATA_CONST.__auth_ptr: 0x10 sha256:7e798bf929bf8577ed8f0e46fc9b2fb08a7bf613a3dcc563e7074ae43b647349
-  UUID: AF6782EE-2DD0-3874-9C27-BD080A2D859D
-  Functions: 1015
+  __DATA_CONST.__mod_init_func: 0x60 sha256:6b52ba653c60d4647a3aa5843a4b2d5d8b998d3821bc5ae2870892b184238d7a
+  __DATA_CONST.__mod_term_func: 0x60 sha256:28bd8f9c232b24fefd46384e370df9de2b55655626546172d9609ceb0d06f838
+  __DATA_CONST.__const: 0x1dd0 sha256:af6d9bdabd862313ea54715eab0eb5323973ea1c67218f4feea7166764777cac
+  __DATA_CONST.__kalloc_type: 0x5c0 sha256:76d74d0d8f8e2dd21ade304303c66d14e9a76f6b3428066e0cf6cb2abd551686
+  __DATA_CONST.__kalloc_var: 0x14a0 sha256:ddeb3b7816a2bd0c2b91629b5125ff9636b2e430ab2df90c7bba2db2451510c2
+  __DATA_CONST.__auth_got: 0x330 sha256:ff6340634ee338360ae0343208342d9ba10e090715296170779723913ff1111d
+  __DATA_CONST.__got: 0xc8 sha256:2579debeeda812aa8312e732cb27e8d3462eb8f557ed5fbd7a1cf6991d17ffcd
+  __DATA_CONST.__auth_ptr: 0x10 sha256:c61a24448cc55c7d79aee70d787ac37114082228a310079fce6a0e74dcd19b3d
+  UUID: 57DB9025-AD3B-3B7A-AAEA-AF3BBFD5CE14
+  Functions: 1016
   Symbols:   0
-  CStrings:  1970
+  CStrings:  1971
 
CStrings:
+ "!entitlement || ACMKernelUtils::isEntitled(params.owningTask, entitlement)"
+ "%s: %s: DENIED: Entitlement '%s' not found!.\n"
+ "%s: %s: DENIED: Kernel call not allowed!.\n"
+ "%s: %s: Unable to detect EDU mode, will retry on next call.\n"
+ "%s: %s: cmd(%u) requestId(%u) != responseId(%u).\n"
+ "%s: %s: multiuser config not yet populated in _COMM_PAGE_MULTIUSER_CONFIG.\n"
+ "19:41:16"
+ "Jun 18 2026"
+ "checkCallerPermissions"
+ "com.apple.private.applecredentialmanager.daemon.allow"
+ "credential->type == kACMCredentialTypePasscodeValidated2"
+ "params.kernelCaller.allowed"
+ "params.userModeCaller.allowed"
- "%s: %s: requestId(%u) != responseId(%u).\n"
- "22:51:49"
- "ACMCredential - ACMCredentialDataPKITokenValidated"
- "ACMCredential - ACMCredentialDataPKITokenValidated2"
- "May 27 2026"
- "_COMM_PAGE_MULTIUSER_CONFIG not available yet"
- "credential->type == kACMCredentialTypePasscodeValidated2 || credential->type == kACMCredentialTypePKITokenValidated2"
- "dataLength == sizeof(ACMCredentialDataPKITokenValidated)"
- "dataLength == sizeof(ACMCredentialDataPKITokenValidated2)"
- "multiuser_flags != 0"
- "site.ACMCredential.ACMCredentialDataPKITokenValidated"
- "site.ACMCredential.ACMCredentialDataPKITokenValidated2"

```
