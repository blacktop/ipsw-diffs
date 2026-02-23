## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-411.100.13.0.0
-  __TEXT.__text: 0x7edb0
+411.100.14.0.0
+  __TEXT.__text: 0x7ee50
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x5f7c
   __TEXT.__cstring: 0x513b
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xf029
+  __TEXT.__oslogstring: 0xf086
   __TEXT.__gcc_except_tab: 0x11b4
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x5d43

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 652EBA43-FB53-3B8D-B598-2C3232BFD61E
+  UUID: B64A5AE9-186B-3400-B69C-AAC4C8D07DAB
   Functions: 2258
   Symbols:   8187
-  CStrings:  5932
+  CStrings:  5933
 
Functions:
~ -[DiagnosticCaseManager buildSpecificRestrictionsForSignature:result:] : 1696 -> 1856
CStrings:
+ "Enhanced Beta Feedback is not enabled. This case will be dampened on Seed builds: %{public}@"

```
