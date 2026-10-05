## AutomationMode

> `/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x3eb8
-  __TEXT.__objc_methlist: 0x3f0
+35.0.0.0.0
+  __TEXT.__text: 0x3f14
+  __TEXT.__objc_methlist: 0x3f8
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__cstring: 0x380
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__cstring: 0x40e
   __TEXT.__oslogstring: 0x566
   __TEXT.__unwind_info: 0x280
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
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x708
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2c

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 120
-  Symbols:   288
-  CStrings:  58
+  Functions: 121
+  Symbols:   293
+  CStrings:  64
 
Symbols:
+ -[XAMWriter _reportCancelledAuthentication]
+ GCC_except_table38
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table56
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSConstantDictionary
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
- GCC_except_table37
- GCC_except_table42
- GCC_except_table45
- GCC_except_table49
- GCC_except_table52
- GCC_except_table55
Functions:
~ ___70-[XAMWriter _authenticateAndEnableAutomationModeWithProxy:completion:]_block_invoke : 44 -> 108
+ -[XAMWriter _reportCancelledAuthentication]
~ ___43-[XAMWriter enableAutomationModeWithError:]_block_invoke : 588 -> 596
CStrings:
+ "authenticationResult"
+ "com.apple.dt.automationmode.AutomationModeAuthenticationEvent"
+ "hasPriorApproval"
+ "i"
+ "lastApprovalAge"
+ "requestedAuthentication"
```
