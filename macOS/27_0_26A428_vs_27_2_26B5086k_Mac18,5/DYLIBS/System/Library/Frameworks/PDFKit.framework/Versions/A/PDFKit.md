## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/Versions/A/PDFKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1537.0.0.0.0
-  __TEXT.__text: 0xdd578
-  __TEXT.__objc_methlist: 0xc870
-  __TEXT.__const: 0x9c4
+1537.1.2.0.0
+  __TEXT.__text: 0xdd7bc
+  __TEXT.__objc_methlist: 0xc8c0
+  __TEXT.__const: 0x9d4
   __TEXT.__gcc_except_tab: 0x84d8
   __TEXT.__cstring: 0x8074
   __TEXT.__dlopen_cstrs: 0x257

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4e78
+  __TEXT.__unwind_info: 0x4e80
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7938
+  __DATA_CONST.__objc_selrefs: 0x7990
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__got: 0xdd0
   __AUTH_CONST.__const: 0x2308
   __AUTH_CONST.__cfstring: 0x8880
-  __AUTH_CONST.__objc_const: 0x11870
+  __AUTH_CONST.__objc_const: 0x118f8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x5e8

   __AUTH_CONST.__auth_got: 0x18a8
   __AUTH.__objc_data: 0x19a0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xe78
+  __DATA.__objc_ivar: 0xe80
   __DATA.__data: 0x1310
   __DATA_DIRTY.__objc_data: 0x1c20
   __DATA_DIRTY.__bss: 0x258

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4486
-  Symbols:   11793
+  Functions: 4492
+  Symbols:   11812
   CStrings:  1426
 
Symbols:
+ -[PDFAccessibilityNodeContent _contentRelativeRange:]
+ -[PDFAccessibilityNodeContent _getParentTextOffset]
+ -[PDFAccessibilityNodeContent _isParentTextOffsetCalculated]
+ -[PDFAccessibilityNodeContent _parentRelativeRange:]
+ -[PDFAccessibilityNodeContent _parentTextOffset]
+ -[PDFAccessibilityNodeContent set_isParentTextOffsetCalculated:]
+ -[PDFAccessibilityNodeContent set_parentTextOffset:]
+ OBJC_IVAR_$_PDFAccessibilityNodeContent.__isParentTextOffsetCalculated
+ OBJC_IVAR_$_PDFAccessibilityNodeContent.__parentTextOffset
+ _objc_msgSend$_contentRelativeRange:
+ _objc_msgSend$_getParentTextOffset
+ _objc_msgSend$_isParentTextOffsetCalculated
+ _objc_msgSend$_parentRelativeRange:
+ _objc_msgSend$_parentTextOffset
+ _objc_msgSend$centerXAnchor
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$set_isParentTextOffsetCalculated:
+ _objc_msgSend$set_parentTextOffset:
- +[PDFAccessibilityNode _accessibilityElementForNode:]
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
```
