## DocumentManager

> `/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager`

```diff

-401.1.5.0.0
-  __TEXT.__text: 0x32c58
-  __TEXT.__objc_methlist: 0x2e44
+403.1.8.0.0
+  __TEXT.__text: 0x332a4
+  __TEXT.__objc_methlist: 0x2e64
   __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x4df6
+  __TEXT.__cstring: 0x4e09
   __TEXT.__ustring: 0x6a2
-  __TEXT.__oslogstring: 0x348c
+  __TEXT.__oslogstring: 0x3599
   __TEXT.__gcc_except_tab: 0x8b0
-  __TEXT.__unwind_info: 0x1130
+  __TEXT.__unwind_info: 0x1150
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1708
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a90
+  __DATA_CONST.__objc_selrefs: 0x2ae8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__got: 0x640
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x4280
-  __AUTH_CONST.__objc_const: 0x45e0
+  __AUTH_CONST.__cfstring: 0x42a0
+  __AUTH_CONST.__objc_const: 0x4620
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x290
-  __DATA.__data: 0x950
+  __DATA.__data: 0x30
   __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__data: 0x920
   __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1253
-  Symbols:   2237
-  CStrings:  846
+  Functions: 1261
+  Symbols:   2243
+  CStrings:  853
 
Symbols:
+ -[FPSandboxingURLWrapper(DOCCallerAuthorization) doc_noFollowSafeWrapper]
+ -[FPSandboxingURLWrapper(DOCCallerAuthorization) doc_wrapperAuthorizedForConnection:readonly:]
+ _FPOriginalDocumentURL
+ __OBJC_$_CATEGORY_FPSandboxingURLWrapper_$_DOCCallerAuthorization
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_FPSandboxingURLWrapper_$_DOCCallerAuthorization
+ ___73-[FPSandboxingURLWrapper(DOCCallerAuthorization) doc_noFollowSafeWrapper]_block_invoke
CStrings:
+ "%@ Could not make a no follow wrapper for %@: %@"
+ "Caller has no sandbox access to %@ readonly: %d"
+ "Could not resolve wrapped URL: %@"
+ "No connection to authorize wrapper against: %@"
+ "Resolvable URL not allowed access %@ readonly: %d"
+ "Wrapper carries no sandbox extension: %@"
+ "visibilityPriority"
```
