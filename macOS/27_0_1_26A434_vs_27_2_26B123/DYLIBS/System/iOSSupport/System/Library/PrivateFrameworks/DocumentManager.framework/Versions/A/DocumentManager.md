## DocumentManager

> `/System/iOSSupport/System/Library/PrivateFrameworks/DocumentManager.framework/Versions/A/DocumentManager`

```diff

-399.0.0.0.0
-  __TEXT.__text: 0x32db0
-  __TEXT.__objc_methlist: 0x2f8c
+403.1.9.0.0
+  __TEXT.__text: 0x33530
+  __TEXT.__objc_methlist: 0x2fb4
   __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x4fdd
+  __TEXT.__cstring: 0x5008
   __TEXT.__ustring: 0x68c
-  __TEXT.__oslogstring: 0x3066
-  __TEXT.__gcc_except_tab: 0x780
-  __TEXT.__unwind_info: 0xd50
+  __TEXT.__oslogstring: 0x3206
+  __TEXT.__gcc_except_tab: 0x784
+  __TEXT.__unwind_info: 0xd58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15c0
+  __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b50
+  __DATA_CONST.__objc_selrefs: 0x2bc8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x620
+  __DATA_CONST.__got: 0x630
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x42e0
-  __AUTH_CONST.__objc_const: 0x4720
+  __AUTH_CONST.__cfstring: 0x4320
+  __AUTH_CONST.__objc_const: 0x4760
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x2a0
-  __DATA.__data: 0x9b0
+  __DATA.__data: 0x90
   __DATA.__bss: 0x49
   __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__data: 0x920
   __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1254
-  Symbols:   3321
-  CStrings:  837
+  Functions: 1265
+  Symbols:   3340
+  CStrings:  846
 
Symbols:
+ -[FPSandboxingURLWrapper(DOCCallerAuthorization) doc_noFollowSafeWrapper]
+ -[FPSandboxingURLWrapper(DOCCallerAuthorization) doc_wrapperAuthorizedForConnection:readonly:]
+ -[UIDocumentBrowserAction hash]
+ GCC_except_table52
+ GCC_except_table60
+ GCC_except_table76
+ _FPOriginalDocumentURL
+ _OBJC_CLASS_$_DOCStateRestorationCrashGuard
+ __OBJC_$_CATEGORY_FPSandboxingURLWrapper_$_DOCCallerAuthorization
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_FPSandboxingURLWrapper_$_DOCCallerAuthorization
+ ___73-[FPSandboxingURLWrapper(DOCCallerAuthorization) doc_noFollowSafeWrapper]_block_invoke
+ _objc_msgSend$_resolveFlags
+ _objc_msgSend$accessibilityIdentifier
+ _objc_msgSend$assembleURL:sandbox:physicalURL:physicalSandbox:
+ _objc_msgSend$doc_hasSandboxAccessToFile:readonly:
+ _objc_msgSend$doc_noFollowSafeWrapper
+ _objc_msgSend$doc_noFollowURL
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$isRestorationSuppressed
+ _objc_msgSend$scope
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setTemporaryResourceValue:forKey:
+ _objc_msgSend$setVisibilityPriority:
+ _objc_msgSend$sharedGuard
+ _objc_msgSend$visibilityPriority
+ _objc_msgSend$wrapperWithSecurityScopedURL:
- GCC_except_table54
- GCC_except_table61
- GCC_except_table77
- __41-[DOCSmartFolderDatabase purgeOldEntries]_block_invoke
- ___38-[DOCSmartFolderDatabase initWithURL:]_block_invoke
- ___41-[DOCSmartFolderDatabase purgeOldEntries]_block_invoke
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
CStrings:
+ "%s: Skipping the most recent interface state because repeated launch crashes suppressed state restoration"
+ "%s: Skipping the saved state because repeated launch crashes suppressed state restoration"
+ "Caller has no sandbox access to %@ readonly: %d"
+ "Could not resolve wrapped URL: %@"
+ "No connection to authorize wrapper against: %@"
+ "Resolvable URL not allowed access %@ readonly: %d"
+ "Wrapper carries no sandbox extension: %@"
+ "accessibilityIdentifier"
+ "visibilityPriority"
```
