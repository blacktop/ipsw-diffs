## CloudDocsUI

> `/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

 177.2.0.0.0
-  __TEXT.__text: 0x30334
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x3be0
+  __TEXT.__text: 0x30bf4
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_methlist: 0x3c28
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x1929
-  __TEXT.__ustring: 0x378
+  __TEXT.__cstring: 0x1afb
+  __TEXT.__ustring: 0x386
   __TEXT.__oslogstring: 0x972
   __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__unwind_info: 0xea0
-  __TEXT.__objc_classname: 0xa41
-  __TEXT.__objc_methname: 0xa96f
+  __TEXT.__unwind_info: 0xea8
+  __TEXT.__objc_classname: 0xa43
+  __TEXT.__objc_methname: 0xaacf
   __TEXT.__objc_methtype: 0x2655
-  __TEXT.__objc_stubs: 0x8640
+  __TEXT.__objc_stubs: 0x8700
   __DATA_CONST.__got: 0x610
   __DATA_CONST.__const: 0xd20
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b38
+  __DATA_CONST.__objc_selrefs: 0x2b70
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x4c0
+  __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1de0
-  __AUTH_CONST.__objc_const: 0x7eb0
+  __AUTH_CONST.__cfstring: 0x1f60
+  __AUTH_CONST.__objc_const: 0x7f10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x3a4
+  __DATA.__objc_ivar: 0x3ac
   __DATA.__data: 0xba0
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1180
-  Symbols:   3474
-  CStrings:  2441
+  Functions: 1186
+  Symbols:   3489
+  CStrings:  2464
 
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
+ _objc_msgSend$pickabilityReason
+ _objc_msgSend$pickableDiagnosticGestureRecognizer
+ _objc_msgSend$rootViewController
+ _objc_msgSend$setMinimumPressDuration:
+ _objc_msgSend$setPickabilityReason:
+ _objc_msgSend$setPickableDiagnosticGestureRecognizer:
CStrings:
+ ", "
+ "Bummer"
+ "Container %@ declares types (%@), which doesn't overlap requested types (%@)"
+ "Container declares type %@, which requested type %@ conforms to"
+ "Container doesn't declare any types, so it's pickable by default"
+ "Debug..."
+ "Debug…"
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
```
