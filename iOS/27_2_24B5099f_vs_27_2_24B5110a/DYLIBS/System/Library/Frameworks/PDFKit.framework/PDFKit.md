## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1537.1.2.0.0
-  __TEXT.__text: 0xbb200
-  __TEXT.__objc_methlist: 0xb064
+1537.1.4.0.0
+  __TEXT.__text: 0xbb4a4
+  __TEXT.__objc_methlist: 0xb094
   __TEXT.__const: 0x944
   __TEXT.__cstring: 0x7384
   __TEXT.__gcc_except_tab: 0x8010

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4478
+  __TEXT.__unwind_info: 0x4488
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7120
+  __DATA_CONST.__objc_selrefs: 0x7138
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xb08
   __AUTH_CONST.__const: 0x9d8
   __AUTH_CONST.__cfstring: 0x7680
-  __AUTH_CONST.__objc_const: 0xf120
+  __AUTH_CONST.__objc_const: 0xf180
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x2e8

   __AUTH_CONST.__auth_got: 0x1798
   __AUTH.__objc_data: 0x2558
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xc7c
+  __DATA.__objc_ivar: 0xc88
   __DATA.__data: 0x13d0
   __DATA_DIRTY.__objc_data: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3768
-  Symbols:   7467
+  Functions: 3772
+  Symbols:   7474
   CStrings:  1273
 
Symbols:
+ -[PDFKitTextView _beginEditingSession]
+ -[PDFKitTextView _commitStringToModel:]
+ -[PDFKitTextView _replacementOverflowsWidget:inRange:forTextView:]
+ -[PDFKitTextView textViewDidBeginEditing:]
+ _OBJC_IVAR_$_PDFKitTextViewPrivate.isCommittingOwnEdit
+ _OBJC_IVAR_$_PDFKitTextViewPrivate.preEditValue
+ _OBJC_IVAR_$_PDFKitTextViewPrivate.sessionUndoRegistered
```
