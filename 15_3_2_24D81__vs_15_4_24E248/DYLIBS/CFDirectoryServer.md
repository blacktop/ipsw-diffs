## CFDirectoryServer

> `/System/Library/PrivateFrameworks/DirectoryServer.framework/Frameworks/CFDirectoryServer.framework/Versions/A/CFDirectoryServer`

```diff

 65.0.0.0.0
-  __TEXT.__text: 0x8958
+  __TEXT.__text: 0x88cc
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x220c
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__cstring: 0x2209
+  __TEXT.__unwind_info: 0x160
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x1f0
   __AUTH_CONST.__auth_got: 0x608

   - /System/Library/PrivateFrameworks/HeimODAdmin.framework/Versions/A/HeimODAdmin
   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /usr/lib/libSystem.B.dylib
-  UUID: A29D882C-5381-3B47-8981-91642B2B1492
-  Functions: 76
+  UUID: 74738F91-630E-3147-957F-7E2F7D963818
+  Functions: 75
   Symbols:   348
-  CStrings:  527
+  CStrings:  526
 
Functions:
~ _DSLDAPContainerCreate : 632 -> 608
~ __ldap2dserror : 192 -> 220
- sub_1d16b5ac4
~ _DSLDAPContainerCopyHostNameConnectedTo : 432 -> 428
~ _DSLDAPQueryCreate : 676 -> 680
~ _DSLDAPQueryCopyResults : 1020 -> 1016
~ _DSLDAPSetCredentials : 1444 -> 1440
~ _DSLDAPRecordCreate : 1472 -> 1468
~ __createMods : 448 -> 440
~ _DSCopyIPAddrsForHost : 344 -> 352
~ _DSCopyAccountPasswordFromKeychain : 460 -> 448
~ _DSKerberosAddPrincipalToKeytab : 948 -> 940
~ _DSKerberosAddPrincipalToKeytabWithAcctKey : 1192 -> 1196
~ _DSKerberosRemovePrincipalFromKeytab : 824 -> 820
~ _DSKerberosRemoveAllPrincipalsFromKeytabForRealm : 568 -> 564
~ _DSKerberosCopyPrincipalFromKeytab : 820 -> 816
~ _DSChangePasswordWithPolicy : 876 -> 884
~ _DSConfigGetDirectoryServerType : 516 -> 492
CStrings:
- "lo"

```
