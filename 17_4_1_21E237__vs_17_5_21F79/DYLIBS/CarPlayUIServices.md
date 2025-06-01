## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-332.13.2.0.0
-  __TEXT.__text: 0x1685c
+332.16.0.0.0
+  __TEXT.__text: 0x16a40
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x1f30
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x8fd
+  __TEXT.__oslogstring: 0x9b4
   __TEXT.__cstring: 0x1095
   __TEXT.__gcc_except_tab: 0x254
   __TEXT.__unwind_info: 0x734
   __TEXT.__objc_classname: 0xcbb
-  __TEXT.__objc_methname: 0x4c45
+  __TEXT.__objc_methname: 0x4c29
   __TEXT.__objc_methtype: 0x1107
   __TEXT.__objc_stubs: 0x33e0
   __DATA_CONST.__got: 0x40

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_classrefs: 0x2e8
   __DATA_CONST.__objc_superrefs: 0x140
-  __AUTH_CONST.__objc_const: 0x1930
-  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__objc_const: 0x828
   __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__auth_got: 0x270
-  __AUTH.__objc_data: 0x15e0
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x25c
   __DATA.__data: 0xd88
   __DATA.__bss: 0x98
+  __DATA_DIRTY.__const: 0x280
+  __DATA_DIRTY.__objc_const: 0x1108
+  __DATA_DIRTY.__objc_data: 0x1040
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EEAA013-5ECA-34A1-8F7D-2D8C6FC8BD9E
-  Functions: 749
-  Symbols:   3328
-  CStrings:  1413
+  UUID: 56D6B0D8-BABD-3DB5-969D-3403EE33AF93
+  Functions: 751
+  Symbols:   3332
+  CStrings:  1416
 
Symbols:
+ -[CRSUIDashboardWidgetWindow invalidated]
+ -[CRSUIDashboardWidgetWindow setContentReady].cold.1
+ -[CRSUIDashboardWidgetWindow setFocusableViews:].cold.1
+ _objc_msgSend$invalidated
- -[CRSUIDashboardWidgetWindow isInvalidated]
- _objc_msgSend$isInvalidated
CStrings:
+ "Attempting to set content ready after invalidation, ignoring."
+ "Attempting to set new focusable views after invalidation, ignoring."
+ "Invalidating connection"
+ "Invalidating focusable items"
+ "TB,N,V_invalidated"
- "TB,N,GisInvalidated,V_invalidated"
- "isInvalidated"

```
