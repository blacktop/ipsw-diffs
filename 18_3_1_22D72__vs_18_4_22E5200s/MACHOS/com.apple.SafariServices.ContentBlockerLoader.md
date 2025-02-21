## com.apple.SafariServices.ContentBlockerLoader

> `/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader`

```diff

-7620.2.4.10.7
-  __TEXT.__text: 0x34d4
+7621.1.10.20.6
+  __TEXT.__text: 0x3648
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x124
+  __TEXT.__objc_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x2d0
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0xbc2
+  __TEXT.__objc_methname: 0xc4f
   __TEXT.__objc_methtype: 0x2dd
-  __TEXT.__cstring: 0x192
-  __TEXT.__gcc_except_tab: 0x5d0
+  __TEXT.__cstring: 0x1d2
+  __TEXT.__gcc_except_tab: 0x5dc
   __TEXT.__const: 0x20
-  __TEXT.__oslogstring: 0x52e
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__oslogstring: 0x566
+  __TEXT.__unwind_info: 0x238
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x378
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x738
-  __DATA.__objc_selrefs: 0x2b8
+  __DATA.__objc_const: 0x438
+  __DATA.__objc_selrefs: 0x3b0
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
+  - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/WebKit.framework/WebKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 58
-  Symbols:   106
-  CStrings:  193
+  Functions: 68
+  Symbols:   105
+  CStrings:  205
 
Symbols:
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$__EXQuery
+ _OBJC_CLASS_$__EXQueryController
+ _objc_release_x27
- _NSExtensionIdentifierName
- _NSExtensionPointName
- _OBJC_CLASS_$_LSApplicationProxy
- _PKContainingAppAttribute
- _objc_retain_x25
CStrings:
+ "@16@?0@\"_EXExtensionIdentity\"8"
+ "B16@?0@\"NSExtension\"8"
+ "Extensions"
+ "Failed to get bundle record for application %{private}@"
+ "URL"
+ "_plugIn"
+ "bundleRecordWithApplicationIdentifier:error:"
+ "containingUrl"
+ "executeQuery:"
+ "extensionWithIdentity:error:"
+ "initWithExtensionPointIdentifier:"
+ "initWithUTF8String:"
+ "isEqualToString:"
+ "path"
+ "safari_firstObjectPassingTest:"
+ "safari_mapObjectsUsingBlock:"
- "applicationProxyForIdentifier:"
- "bundleURL"
- "extensionsWithMatchingAttributes:error:"
- "stringWithCString:encoding:"

```
