## VNCPrivilegeProxy

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/Support/VNCPrivilegeProxy`

```diff

-756.28.0.0.0
-  __TEXT.__text: 0x2354 sha256:2817bed50a040cadbbdae544019005ee31653c7da93e30774b9f37404e20669f
-  __TEXT.__auth_stubs: 0x570 sha256:f67eaf9befce536946845d86c8feb77b57d49e11b0b3059e914e3a2200004a31
-  __TEXT.__objc_stubs: 0x60 sha256:570e02df81ff816d05e7e1a63cfc3ff0ab9e9f2530f011dbae759f0cade5b77f
-  __TEXT.__const: 0x11d8 sha256:c5941879e54e956a797de70a3692bfaa6d0aca335ef2c54e06e627b98ba61346
-  __TEXT.__oslogstring: 0x12c sha256:83ee2cca9a5ed8d727f7ac3938f3e7d2b2d8e752834e7b5bb786951ba2fd858a
-  __TEXT.__cstring: 0x802 sha256:1e53e804abc1b2454e409b3439310d8f6b810d44702810f36650b5aa4ce801e3
+756.30.0.0.0
+  __TEXT.__text: 0x2874 sha256:8dce13498509cd719f81cb760a5e57aed312fcb35ce4ee0e6993c96916402d36
+  __TEXT.__auth_stubs: 0x5c0 sha256:c9b1db29fa6a45547d13d8bcd62b2ffdcb8f6a36bbffcf40742600b28578f2d4
+  __TEXT.__objc_stubs: 0x60 sha256:60308c317c1dfebe0aebd3c92c71648813251b6ab9be0d9c4cb9eba04494fcee
+  __TEXT.__const: 0x11d8 sha256:1f94986e98eae4687221bd48654b035c37fd301924a0e1922bd2762429006151
+  __TEXT.__oslogstring: 0x1e2 sha256:228b05dee28a18b8adeb1eb870d5bb94c8446cf07d4bee0adae6b5a7cc09f576
+  __TEXT.__cstring: 0x94b sha256:0b9e61aa4f2ce2878b280206cc7e6a2c154baa3413e78df256f2f8407d9050ed
   __TEXT.__objc_methname: 0x42 sha256:1a947ca7d0a6e3bbe9f5e97cef7005ba4bc492db1b60269e26caea0372ea1e27
-  __TEXT.__unwind_info: 0xe0 sha256:f1bf44f304c80b4ded4dbd45b02560293061fc22127e090b3643e010843620b3
-  __DATA_CONST.__const: 0xd8 sha256:2415e16f4a500591f25fbab8773436f267656dfb7166f0351efb89ee343425ad
-  __DATA_CONST.__cfstring: 0x140 sha256:f1096d2d5e5887eebed31bb130e87a55a77571be18c3bbe3afdc40ea4b170916
+  __TEXT.__unwind_info: 0xd8 sha256:86b7fc6eedd57dad972199730d2fa0cfc27e911c1f35794360bc2386fa890a46
+  __DATA_CONST.__const: 0xd8 sha256:4045c13765f023f42a8a0b438cadbe3ae30b4857e3d396789696fbea29e46ba1
+  __DATA_CONST.__cfstring: 0x160 sha256:7a2d549d0b06e9c59ab27ffe9809e4840b37e80fd3c2243cb4363b27fe8b127c
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__auth_got: 0x2c0 sha256:9598be882456aa0ed86474ff3653357bd2f2bb772aa2d4012efadeb6d4744750
-  __DATA_CONST.__got: 0x58 sha256:fe26cd8c8b9a5a12388ddfb317086035b08356e674f9074a584ad0887a1eadd4
-  __DATA.__objc_selrefs: 0x18 sha256:ba27d4bca3f8c0e4b9a6c35b05fdea4d4eb9c127bc58923150616fc75495bbd3
+  __DATA_CONST.__auth_got: 0x2e8 sha256:3653da4951eb0a798999852ec84aa300c6b1c714100d09a8a0c9bb47b3d2433e
+  __DATA_CONST.__got: 0x58 sha256:c5ad99a967bdd5446e74a39cc1f17a3507b1016eb13b1770aee0449e1a1cb280
+  __DATA.__objc_selrefs: 0x18 sha256:05febcb45de41f17917ad97acc2c3428d83572b0008f6b49a380db9e8e17e008
   __DATA.__data: 0x80 sha256:54d5f97230200d405bcaf557d4927b761c723547976bf666eafe2b3d27994b83
   __DATA.__bss: 0x124 sha256:3453f578e4f10a1cafd84b6500620ae42aeb9b31d700b3b9c3ef5498062a25d4
   __DATA.__common: 0x1 sha256:6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/Versions/A/DiagnosticLogCollection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8934892C-0DDD-32A5-9CBB-F6017EC3823B
-  Functions: 36
-  Symbols:   102
-  CStrings:  87
+  UUID: 093EAE50-C437-3C34-A0A1-E063FCB901DD
+  Functions: 40
+  Symbols:   107
+  CStrings:  105
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _mach_msg_server_once
- _mach_msg_server
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRkEugDc0Dkuv5WRYa4mB4CUv96DKE5JsBBYMNM/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/LegacyAuthProxy/LegacyAuthProxy.c"
+ "/AppleInternal/Library/BuildRoots/4~CRkEugDc0Dkuv5WRYa4mB4CUv96DKE5JsBBYMNM/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/Log.m"
+ "/AppleInternal/Library/BuildRoots/4~CRkEugDc0Dkuv5WRYa4mB4CUv96DKE5JsBBYMNM/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/StringUtils.c"
+ "CheckCallerEntitlement"
+ "LPWDAS_KerberosAuthenticate"
+ "LPWDAS_KerberosAuthenticate called"
+ "LPWDAS_KerberosConfigured"
+ "LPWDAS_KerberosConfigured called"
+ "LPWDAS_LegacyAuthenticate"
+ "LPWDAS_LegacyAuthenticate got here"
+ "Unable to create task for audit token"
+ "com.apple.private.screensharing.xpcaccepted"
+ "has entitlement = %d"
+ "invalid entitlement"
- "/AppleInternal/Library/BuildRoots/4~CQQgugBdU24N37DZEa8zHeQWs42KFEDXiPr7tSQ/Library/Caches/com.apple.xbs/TemporaryDirectory.Ul3ToM/Sources/RemoteDesktop/LegacyAuthProxy/LegacyAuthProxy.c"
- "/AppleInternal/Library/BuildRoots/4~CQQgugBdU24N37DZEa8zHeQWs42KFEDXiPr7tSQ/Library/Caches/com.apple.xbs/TemporaryDirectory.Ul3ToM/Sources/RemoteDesktop/common/Log.m"
- "/AppleInternal/Library/BuildRoots/4~CQQgugBdU24N37DZEa8zHeQWs42KFEDXiPr7tSQ/Library/Caches/com.apple.xbs/TemporaryDirectory.Ul3ToM/Sources/RemoteDesktop/common/StringUtils.c"

```
