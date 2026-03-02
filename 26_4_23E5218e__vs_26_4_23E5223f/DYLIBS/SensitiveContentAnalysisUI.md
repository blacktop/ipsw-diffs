## SensitiveContentAnalysisUI

> `/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI`

```diff

-130.2.11.1.0
-  __TEXT.__text: 0x1c5dd0
-  __TEXT.__auth_stubs: 0x46b0
-  __TEXT.__objc_methlist: 0x1d40
-  __TEXT.__const: 0x16464
-  __TEXT.__cstring: 0x5669
-  __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__oslogstring: 0x1013
+130.2.12.0.0
+  __TEXT.__text: 0x1c6a0c
+  __TEXT.__auth_stubs: 0x4670
+  __TEXT.__objc_methlist: 0x1d58
+  __TEXT.__const: 0x16414
+  __TEXT.__cstring: 0x5649
+  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__oslogstring: 0x10a3
   __TEXT.__dlopen_cstrs: 0x135
-  __TEXT.__swift5_typeref: 0x1591c
+  __TEXT.__swift5_typeref: 0x15926
   __TEXT.__constg_swiftt: 0x6358
-  __TEXT.__swift5_reflstr: 0x3e26
-  __TEXT.__swift5_fieldmd: 0x4f94
+  __TEXT.__swift5_reflstr: 0x3e56
+  __TEXT.__swift5_fieldmd: 0x4f7c
   __TEXT.__swift5_builtin: 0x258
   __TEXT.__swift5_types: 0x694
   __TEXT.__swift5_assocty: 0x11c0

   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x5708
-  __TEXT.__eh_frame: 0x57b4
+  __TEXT.__unwind_info: 0x5738
+  __TEXT.__eh_frame: 0x57ec
   __TEXT.__objc_classname: 0x139a
-  __TEXT.__objc_methname: 0x47b9
+  __TEXT.__objc_methname: 0x4879
   __TEXT.__objc_methtype: 0xcff
-  __TEXT.__objc_stubs: 0x37c0
-  __DATA_CONST.__got: 0x13c0
+  __TEXT.__objc_stubs: 0x3860
+  __DATA_CONST.__got: 0x13d8
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e8
+  __DATA_CONST.__objc_selrefs: 0x1218
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x2368
-  __AUTH_CONST.__const: 0xb3a0
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__auth_got: 0x2348
+  __AUTH_CONST.__const: 0xb3d0
   __AUTH_CONST.__cfstring: 0x4e0
   __AUTH_CONST.__objc_const: 0x4ee0
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x25c0
   __AUTH.__data: 0x3910
   __DATA.__objc_ivar: 0xe4
-  __DATA.__data: 0x4968
+  __DATA.__data: 0x4988
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1b100
+  __DATA.__bss: 0x1b0f8
   __DATA.__common: 0x4b0
   __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__data: 0x2528

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2FD0F508-2DF8-35D0-85C3-FEABDF8EB223
-  Functions: 8269
-  Symbols:   4948
-  CStrings:  1672
+  UUID: 2F8D8C8A-1825-39C6-828C-EB8880D5D03B
+  Functions: 8291
+  Symbols:   4972
+  CStrings:  1682
 
Symbols:
+ +[SCUIAccountHelper _getValidAccountAliases:]
+ +[SCUIAccountHelper validAliasesForAllAccounts]
+ +[SCUIAccountHelper validAliasesForAllAccounts].cold.1
+ +[SCUIAccountHelper validAliasesForAllAccounts].cold.2
+ -[SCUIReportVictim accountIDs]
+ -[SCUIReportVictim initWithDisplayName:accountIDs:mediaFiles:]
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_IVAR_$_SCUIReportVictim._accountIDs
+ _UIWindowSceneSessionRoleApplication
+ _getIMAccountControllerClass
+ _getIMServiceClass
+ _objc_msgSend$_getValidAccountAliases:
+ _objc_msgSend$accountIDs
+ _objc_msgSend$initWithDisplayName:accountIDs:mediaFiles:
+ _objc_msgSend$isKeyWindow
+ _objc_msgSend$role
+ _objc_msgSend$session
+ _objc_msgSend$validAliasesForAllAccounts
+ _objc_msgSend$windows
+ _symbolic SaySSGSg
- -[SCUIReportVictim accountID]
- -[SCUIReportVictim initWithDisplayName:accountID:mediaFiles:]
- _OBJC_IVAR_$_SCUIReportVictim._accountID
- _objc_msgSend$_windows
- _objc_msgSend$bestHandleID:
- _objc_msgSend$initWithDisplayName:accountID:mediaFiles:
CStrings:
+ "Could not find a valid window to get rootViewController"
+ "Found a valid controller rootViewController's presented controllers"
+ "No iMessageService implementation was found"
+ "No valid aliases found in all iMessage accounts"
+ "T@\"NSArray\",R,C,V_accountIDs"
+ "_accountIDs"
+ "_getValidAccountAliases:"
+ "accountIDs"
+ "initWithDisplayName:accountIDs:mediaFiles:"
+ "isKeyWindow"
+ "role"
+ "session"
+ "validAliasesForAllAccounts"
+ "windows"
- "Found a valid controller %ld from rootViewController's presented controllers"
- "PHONE_EMAIL_REGION"
- "_windows"
- "initWithDisplayName:accountID:mediaFiles:"

```
