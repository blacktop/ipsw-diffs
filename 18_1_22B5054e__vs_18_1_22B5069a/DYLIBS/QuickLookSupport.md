## QuickLookSupport

> `/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport`

```diff

-199.2.2.0.0
-  __TEXT.__text: 0x15bc4
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x1194
-  __TEXT.__const: 0x188
+199.2.3.0.0
+  __TEXT.__text: 0x15d08
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x11a4
+  __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x360
   __TEXT.__cstring: 0xeab
-  __TEXT.__oslogstring: 0x1060
+  __TEXT.__oslogstring: 0x10ac
   __TEXT.__unwind_info: 0x6b0
-  __TEXT.__objc_classname: 0x254
-  __TEXT.__objc_methname: 0x3d49
-  __TEXT.__objc_methtype: 0x7e7
-  __TEXT.__objc_stubs: 0x2b00
+  __TEXT.__objc_classname: 0x25f
+  __TEXT.__objc_methname: 0x3cf7
+  __TEXT.__objc_methtype: 0x7d7
+  __TEXT.__objc_stubs: 0x2ae0
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x4a8
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x2368
+  __AUTH_CONST.__objc_const: 0x23f8
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x248
   __DATA.__bss: 0x48

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 603
-  Symbols:   1054
-  CStrings:  1028
+  Functions: 604
+  Symbols:   1060
+  CStrings:  1031
 
Symbols:
+ _OBJC_CLASS_$_QLURLCheck
+ _OBJC_METACLASS_$_QLURLCheck
+ _QLCheckIsPlatformWithExtensionAuditToken
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ _SecTaskGetCodeSignStatus
CStrings:
+ "Code signature identifier %!@(MISSING)"
+ "Code signature is first party: %!d(MISSING) (flags : %!x(MISSING))"
+ "Q32@0:8@16@24"
+ "QLURLCheck"
+ "extensionContextForContentType:allowExtensionsForParentTypes:firstPartyExtensionOnly:appBundleIdentifier:extensionPath:extensionType:generationType:withCompletionHandler:"
+ "quickLookPermissionForFileAtURL:clientApplicationIdentifier:"
- "extensionContextForContentType:allowExtensionsForParentTypes:appBundleIdentifier:extensionPath:extensionType:generationType:withCompletionHandler:"
- "extensionContextForContentType:allowExtensionsForParentTypes:firstPartyExtension:appBundleIdentifier:extensionPath:extensionType:generationType:withCompletionHandler:"
- "v68@0:8@16B24@28@36Q44Q52@?60"

```
