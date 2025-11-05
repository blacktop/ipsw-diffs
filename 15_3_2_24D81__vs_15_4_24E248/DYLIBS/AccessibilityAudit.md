## AccessibilityAudit

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Versions/A/AccessibilityAudit`

```diff

-165.0.1.0.0
-  __TEXT.__text: 0x247d4
+165.2.0.0.0
+  __TEXT.__text: 0x24724
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x2d0c
-  __TEXT.__const: 0x228
+  __TEXT.__objc_methlist: 0x3174
+  __TEXT.__const: 0x218
   __TEXT.__cstring: 0x33b4
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__oslogstring: 0x426
-  __TEXT.__unwind_info: 0xa00
+  __TEXT.__unwind_info: 0x9f0
   __TEXT.__objc_classname: 0x596
   __TEXT.__objc_methname: 0x79f1
   __TEXT.__objc_methtype: 0x1170

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d70
+  __DATA_CONST.__objc_selrefs: 0x1e18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x358
   __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x1500
   __AUTH_CONST.__cfstring: 0x3500
-  __AUTH_CONST.__objc_const: 0x9448
+  __AUTH_CONST.__objc_const: 0x5180
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x858
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17EF14EA-C4C0-3CDE-B2AC-7F1495D8DE2C
-  Functions: 1120
-  Symbols:   3177
+  UUID: 83B5E080-D136-3FE0-ACE0-4A1A7FBD13E7
+  Functions: 1127
+  Symbols:   3062
   CStrings:  2578
 
Symbols:
+ +[AXAuditDocumentationManager _docTypeCatalystDictionary].cold.1
+ +[AXAuditDocumentationManager _docTypeDictionary].cold.1
+ +[AXAuditDocumentationManager _macOSToiOSTitleDictionary].cold.1
+ +[AXAuditIssueDescriptionManager _auditIssueTypeToLocalizationKeyLookup].cold.1
+ +[AXAuditIssueDescriptionManager auditIssueTypeToAuditTestTypeMapping].cold.1
+ +[AXAuditScreenshotManager imageProcessingQueue].cold.1
+ -[AXAuditIssueDescriptionManager _locStringForKey:].cold.1
+ AXAuditCGEventIsTrusted.cold.1
+ AXAuditEventIsTrusted.cold.1
+ AXAuditLocStringWithValue.cold.1
+ _OUTLINED_FUNCTION_1

```
