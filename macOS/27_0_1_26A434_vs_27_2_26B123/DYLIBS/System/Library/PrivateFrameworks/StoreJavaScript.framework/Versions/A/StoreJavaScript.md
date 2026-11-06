## StoreJavaScript

> `/System/Library/PrivateFrameworks/StoreJavaScript.framework/Versions/A/StoreJavaScript`

```diff

-717.0.7.0.0
-  __TEXT.__text: 0x85f4
-  __TEXT.__objc_methlist: 0x7d4
+717.1.4.0.0
+  __TEXT.__text: 0x8870
+  __TEXT.__objc_methlist: 0x804
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x5ab
-  __TEXT.__oslogstring: 0x3c0
+  __TEXT.__cstring: 0x5c2
+  __TEXT.__oslogstring: 0x473
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__unwind_info: 0x238
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x688
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x70
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0xc88
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0xce8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x248
   __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 171
-  Symbols:   609
-  CStrings:  115
+  Functions: 175
+  Symbols:   621
+  CStrings:  118
 
Symbols:
+ -[FRBundleInterface didReadJSBridgeURLPatterns]
+ -[FRBundleInterface jsBridgeURLPatterns]
+ -[FRBundleInterface setDidReadJSBridgeURLPatterns:]
+ -[FRBundleInterface setJsBridgeURLPatterns:]
+ OBJC_IVAR_$_FRBundleInterface._didReadJSBridgeURLPatterns
+ OBJC_IVAR_$_FRBundleInterface._jsBridgeURLPatterns
+ _CKCompileBagURLPatterns
+ _CKURLMatchesCompiledPatterns
+ _objc_msgSend$bagValueForKey:error:
+ _objc_msgSend$didReadJSBridgeURLPatterns
+ _objc_msgSend$jsBridgeURLPatterns
+ _objc_msgSend$setDidReadJSBridgeURLPatterns:
CStrings:
+ "%@: js-bridge-url-patterns is not set in the bag, so pages are not filtered for the iTunes object"
+ "%@: withholding the iTunes object from %@, not matched by js-bridge-url-patterns"
+ "js-bridge-url-patterns"
```
