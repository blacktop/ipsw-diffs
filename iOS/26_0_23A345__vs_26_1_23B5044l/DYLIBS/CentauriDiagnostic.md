## CentauriDiagnostic

> `/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic`

```diff

-67.0.1.0.0
-  __TEXT.__text: 0x63d4
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x1821
-  __TEXT.__oslogstring: 0xcd0
+68.0.3.0.0
+  __TEXT.__text: 0x6838
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_methlist: 0x1e4
+  __TEXT.__const: 0xa1
+  __TEXT.__cstring: 0x195e
+  __TEXT.__oslogstring: 0xd47
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x732
+  __TEXT.__objc_methname: 0x74e
   __TEXT.__objc_methtype: 0xc0
-  __TEXT.__objc_stubs: 0x7e0
+  __TEXT.__objc_stubs: 0x800
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__objc_const: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A660BB9-156A-3D84-9158-1506F7BA445D
-  Functions: 50
-  Symbols:   284
-  CStrings:  328
+  UUID: 783894C7-016F-30B7-A5B5-6E89899750EE
+  Functions: 53
+  Symbols:   292
+  CStrings:  338
 
Symbols:
+ -[CDFControlDiagnostics collectLPMDebugDataFrom:to:]
+ -[CDFControlDiagnostics collectLPMDebugDataFrom:to:].cold.1
+ -[CDFControlDiagnostics collectLPMDebugDataFrom:to:].cold.2
+ ___block_literal_global.107
+ ___block_literal_global.112
+ ___block_literal_global.114
+ ___block_literal_global.99
+ _objc_msgSend$collectLPMDebugDataFrom:to:
+ _objc_retain_x22
- ___block_literal_global.106
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.98
CStrings:
+ "-[CDFControlDiagnostics collectLPMDebugDataFrom:to:]"
+ "CDF: %s: invalid dest dir"
+ "CDF: %s: invalid src dir"
+ "CDF: %s: transfer %{public}scomplete for lpm related beta crashlogs"
+ "FeedbackAssistant"
+ "StateSnapshots"
+ "^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|mxwrap)\\.bin|BT5G\\.(dmem|imem|mxwrap)\\.bin|BTLPS\\.(dmem|imem|mxwrap|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|mxwrap|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|mxwrap|regdump)\\.bin)(\\.synced)?$"
+ "collectLPMDebugDataFrom:to:"

```
