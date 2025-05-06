## CloudDocsUI

> `/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI`

```diff

 176.0.0.0.0
-  __TEXT.__text: 0x2d064
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x3bd8
+  __TEXT.__text: 0x2d81c
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x3c20
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x1986
-  __TEXT.__ustring: 0x378
+  __TEXT.__cstring: 0x1b58
+  __TEXT.__ustring: 0x386
   __TEXT.__oslogstring: 0x972
   __TEXT.__gcc_except_tab: 0x5a4
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__unwind_info: 0xc68
-  __TEXT.__objc_classname: 0xa41
-  __TEXT.__objc_methname: 0xa93b
+  __TEXT.__unwind_info: 0xc70
+  __TEXT.__objc_classname: 0xa43
+  __TEXT.__objc_methname: 0xaa9b
   __TEXT.__objc_methtype: 0x2624
-  __TEXT.__objc_stubs: 0x8640
+  __TEXT.__objc_stubs: 0x8700
   __DATA_CONST.__got: 0x608
   __DATA_CONST.__const: 0xd78
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b30
+  __DATA_CONST.__objc_selrefs: 0x2b68
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1de0
-  __AUTH_CONST.__objc_const: 0x7ea8
+  __AUTH_CONST.__cfstring: 0x1f60
+  __AUTH_CONST.__objc_const: 0x7f08
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x3a4
+  __DATA.__objc_ivar: 0x3ac
   __DATA.__data: 0xba0
   __DATA.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1181
-  Symbols:   4818
-  CStrings:  2463
+  Functions: 1187
+  Symbols:   4839
+  CStrings:  2485
 
Symbols:
+ -[_UIDocumentPickerCell _showPickableDiagnostic]
+ -[_UIDocumentPickerCell pickableDiagnosticGestureRecognizer]
+ -[_UIDocumentPickerCell setPickableDiagnosticGestureRecognizer:]
+ -[_UIDocumentPickerContainerItem pickabilityReason]
+ -[_UIDocumentPickerContainerItem setPickabilityReason:]
+ -[_UIDocumentPickerDocumentCell _showPickableDiagnostic]
+ _CPIsInternalDevice
+ _OBJC_IVAR_$__UIDocumentPickerCell._pickableDiagnosticGestureRecognizer
+ _OBJC_IVAR_$__UIDocumentPickerContainerItem._pickabilityReason
+ ___block_literal_global.101
+ ___block_literal_global.103
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.314
+ _objc_msgSend$pickabilityReason
+ _objc_msgSend$pickableDiagnosticGestureRecognizer
+ _objc_msgSend$rootViewController
+ _objc_msgSend$setMinimumPressDuration:
+ _objc_msgSend$setPickabilityReason:
+ _objc_msgSend$setPickableDiagnosticGestureRecognizer:
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.104
- ___block_literal_global.106
- ___block_literal_global.293
- ___block_literal_global.98
CStrings:
+ "\x01\"!\x11"
+ "\x17\x11\x1f\x01"
+ ", "
+ "Bummer"
+ "Container %@ declares types (%@), which doesn't overlap requested types (%@)"
+ "Container declares type %@, which requested type %@ conforms to"
+ "Container doesn't declare any types, so it's pickable by default"
+ "Debug..."
+ "Document picker is in a mode that doesn't allow picking items"
+ "Internal diagnostic: Item is not pickable"
+ "Internal diagnostic: Item is pickable"
+ "Item %@ has nil type."
+ "Item %@ has type %@, which does not conform to any of the allowed types (%@)"
+ "T@\"NSString\",C,N,V_pickabilityReason"
+ "T@\"UILongPressGestureRecognizer\",&,N,V_pickableDiagnosticGestureRecognizer"
+ "_pickabilityReason"
+ "_pickableDiagnosticGestureRecognizer"
+ "_showPickableDiagnostic"
+ "pickabilityReason"
+ "pickableDiagnosticGestureRecognizer"
+ "rootViewController"
+ "setMinimumPressDuration:"
+ "setPickabilityReason:"
+ "setPickableDiagnosticGestureRecognizer:"
- "\x01\"!"
- "\x17\x11\x1f"

```
