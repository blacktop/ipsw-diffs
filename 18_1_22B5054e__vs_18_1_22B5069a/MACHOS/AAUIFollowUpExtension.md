## AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

-520.100.4.0.0
-  __TEXT.__text: 0x7764
+520.100.7.2.0
+  __TEXT.__text: 0x7bfc
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x1420
-  __TEXT.__objc_methlist: 0x260
+  __TEXT.__objc_stubs: 0x14e0
+  __TEXT.__objc_methlist: 0x278
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__cstring: 0x4f2
-  __TEXT.__objc_methname: 0x199c
-  __TEXT.__oslogstring: 0x1502
+  __TEXT.__objc_methname: 0x1a87
+  __TEXT.__oslogstring: 0x16d7
   __TEXT.__objc_classname: 0x117
   __TEXT.__objc_methtype: 0x7a4
-  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__unwind_info: 0x208
   __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x468
   __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x9f0
-  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_selrefs: 0x5b8
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 152
-  Symbols:   130
-  CStrings:  438
+  Functions: 156
+  Symbols:   132
+  CStrings:  452
 
Symbols:
+ _OBJC_CLASS_$_CDPFollowUpContext
+ _OBJC_CLASS_$_CDPFollowUpController
CStrings:
+ "Already checked DTO, no need to go through the first time setup!"
+ "Current state requires repair. Starting repair...: %!{(MISSING)private}@"
+ "Experienced error while attempting to clear CDP+EDP CFU in AAUI: %!@(MISSING)"
+ "Experienced error while attempting to clear CDP+EDP CFU in CDPFollowUpController: %!@(MISSING)"
+ "Successfully renewed credentials for account: %!{(MISSING)private}@"
+ "_continueDismissingRenewCredentialsFollowUpForCDP"
+ "_continueDismissingRenewCredentialsFollowUpForCDPEDP"
+ "_renewCredentialsForFollowUpItem starting..."
+ "about to dismiss CDP followup, EDP ineligible..."
+ "about to dismiss CDPEDP followup..."
+ "clearFollowUpWithContext:error:"
+ "contextForCDPEDPStateRepair"
+ "dismissFollowUpWithIdentifier:error:"
+ "isEDPEligible"
+ "startWithoutFirstTimeSetup"
- "start"

```
