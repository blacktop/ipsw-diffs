## SymptomLinkAdvisory

> `/System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory`

```diff

-2158.80.11.0.0
-  __TEXT.__text: 0xa00
+2169.100.28.0.0
+  __TEXT.__text: 0xa68
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__objc_methlist: 0x490
   __TEXT.__cstring: 0x68
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__gcc_except_tab: 0x38
   __TEXT.__oslogstring: 0x176
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x92
   __TEXT.__objc_methname: 0xb7f
   __TEXT.__objc_methtype: 0x859

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43E2CCE7-6596-3B92-B4ED-6B63E6F77DB4
+  UUID: 5B847571-BACC-362F-858B-AB610107837C
   Functions: 51
   Symbols:   237
   CStrings:  189
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
Functions:
~ _aluManagerLogHandle : 68 -> 84
~ _connManagerLogHandle : 68 -> 84
~ _nwActReporterLogHandle : 68 -> 84
~ +[SymptomLinkAdvisoryConnectionManager sharedInstance] : 68 -> 84
~ -[SymptomLinkAdvisoryConnectionManager _setupXPCConnection] : 636 -> 648
~ ___59-[SymptomLinkAdvisoryConnectionManager _setupXPCConnection]_block_invoke : 272 -> 284
~ ___59-[SymptomLinkAdvisoryConnectionManager _setupXPCConnection]_block_invoke_2 : 272 -> 284
~ ___59-[SymptomLinkAdvisoryConnectionManager _setupXPCConnection]_block_invoke.135 : 104 -> 108

```
