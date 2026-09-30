## AOSAccountsLite

> `/System/Library/PrivateFrameworks/AOSAccountsLite.framework/Versions/A/AOSAccountsLite`

```diff

-197.226.0.0.0
-  __TEXT.__text: 0x9a0
+197.450.0.0.0
+  __TEXT.__text: 0x958
   __TEXT.__auth_stubs: 0x170
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x16c
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__unwind_info: 0x88
   __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methname: 0x6e
   __TEXT.__objc_stubs: 0x80

   - /System/Library/PrivateFrameworks/AOSKit.framework/Versions/A/AOSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E3A49C7-E7AE-3DC8-AE34-129A7027651C
-  Functions: 14
-  Symbols:   73
+  UUID: 60432D43-8880-3D1C-A8F5-1AB567732E8A
+  Functions: 15
+  Symbols:   79
   CStrings:  29
 
Symbols:
+ MMLAccountCopyProperty.cold.1
+ MMLAccountIsVetted.cold.1
+ MMLCopyLoggedInAccount.cold.1
+ MMLCopyMailActivationInfo.cold.1
+ MMLServiceCopyProperty.cold.1
+ _useFullAOSAccounts.cold.1
Functions:
~ _MMLCopyLoggedInAccount : 148 -> 132
~ _MMLAccountIsVetted : 176 -> 160
~ _MMLAccountCopyProperty : 268 -> 252
~ _MMLServiceCopyProperty : 184 -> 168
~ _MMLCopyMailActivationInfo : 424 -> 408
~ __useFullAOSAccounts : 76 -> 64

```
