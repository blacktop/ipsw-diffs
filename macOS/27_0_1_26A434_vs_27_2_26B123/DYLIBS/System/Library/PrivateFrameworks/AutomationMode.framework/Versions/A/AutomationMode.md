## AutomationMode

> `/System/Library/PrivateFrameworks/AutomationMode.framework/Versions/A/AutomationMode`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x4670
-  __TEXT.__objc_methlist: 0x3f0
+35.0.0.0.0
+  __TEXT.__text: 0x46dc
+  __TEXT.__objc_methlist: 0x3f8
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__cstring: 0x380
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__cstring: 0x40e
   __TEXT.__oslogstring: 0x566
   __TEXT.__unwind_info: 0x218
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x708
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2c

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 135
-  Symbols:   365
-  CStrings:  58
+  Functions: 136
+  Symbols:   371
+  CStrings:  64
 
Symbols:
+ -[XAMWriter _reportCancelledAuthentication]
+ GCC_except_table44
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table62
+ GCC_except_table65
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSConstantDictionary
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _objc_msgSend$_reportCancelledAuthentication
- GCC_except_table43
- GCC_except_table50
- GCC_except_table53
- GCC_except_table58
- GCC_except_table61
- GCC_except_table64
Functions:
~ ___70-[XAMWriter _authenticateAndEnableAutomationModeWithProxy:completion:]_block_invoke : 44 -> 124
+ -[XAMWriter _reportCancelledAuthentication]
~ ___43-[XAMWriter enableAutomationModeWithError:]_block_invoke : 628 -> 636
CStrings:
+ "authenticationResult"
+ "com.apple.dt.automationmode.AutomationModeAuthenticationEvent"
+ "hasPriorApproval"
+ "i"
+ "lastApprovalAge"
+ "requestedAuthentication"
```
