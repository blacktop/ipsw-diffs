## UniversalAccess

> `/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/UniversalAccess`

```diff

-696.3.1.0.0
-  __TEXT.__text: 0x185a8
+696.5.5.0.0
+  __TEXT.__text: 0x18778
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x1b8c
+  __TEXT.__objc_methlist: 0x2100
   __TEXT.__const: 0x250
   __TEXT.__cstring: 0x198b
   __TEXT.__oslogstring: 0x25f
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__unwind_info: 0x678
   __TEXT.__objc_classname: 0x7d6
   __TEXT.__objc_methname: 0x5e1a
   __TEXT.__objc_methtype: 0x1571

   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1550
+  __DATA_CONST.__objc_selrefs: 0x17f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0x4910
+  __AUTH_CONST.__objc_const: 0x3ee8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1040

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libUniversalAccess.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFF8FB80-14BE-3870-8F51-955DC50852A8
-  Functions: 644
-  Symbols:   2027
+  UUID: 9A63134B-FFF8-3958-BFA4-3B7F7DEFF6A6
+  Functions: 663
+  Symbols:   2049
   CStrings:  1765
 
Symbols:
+ +[UAShortcutExecutor shared].cold.1
+ +[UAShortcutPickerWindowController showOnWindow:identifiers:allowsMultiple:prompt:completionHandler:].cold.1
+ +[UAShortcutPickerWindowController showOnWindow:identifiers:allowsMultiple:prompt:completionHandler:].cold.2
+ +[UAShortcutWorkflow runWorkflow:completionHandler:].cold.1
+ +[UAShortcutWorkflow runWorkflow:completionHandler:].cold.2
+ +[UAShortcutWorkflow workflowWithIdentifier:].cold.3
+ +[UAShortcutWorkflow workflowWithName:].cold.2
+ +[UAUtilities localizedStringForKey:].cold.1
+ -[UAShortcutExecutor _complete:success:cancelled:output:error:].cold.3
+ -[UAShortcutExecutor _complete:success:cancelled:output:error:].cold.4
+ -[UAShortcutExecutor _run:completionHandler:].cold.1
+ -[UAShortcutExecutor _run:completionHandler:].cold.2
+ -[UAShortcutExecutor init].cold.1
+ -[UAShortcutExecutor run:completionHandler:].cold.3
+ -[UAShortcutExecutor run:completionHandler:].cold.4
+ -[UAShortcutWorkflow initWithIdentifier:].cold.3
+ UAShowStatusOverlayForFeature.cold.4
+ _OUTLINED_FUNCTION_3
+ _UAExecuteWithHUDRemoteProxy.cold.1

```
