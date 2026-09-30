## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-1084.40.3.0.1
-  __TEXT.__text: 0x3f948
-  __TEXT.__objc_methlist: 0x5ba8
+1084.40.6.0.0
+  __TEXT.__text: 0x3ff34
+  __TEXT.__objc_methlist: 0x5bd8
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x4853
+  __TEXT.__cstring: 0x492e
   __TEXT.__oslogstring: 0x27cb
   __TEXT.__gcc_except_tab: 0x868
-  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__unwind_info: 0x1e78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d68
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x4f8
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x5fc0
+  __AUTH_CONST.__cfstring: 0x6040
   __AUTH_CONST.__objc_const: 0xb018
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0x1658
+  __AUTH.__objc_data: 0x1590
   __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0x620
-  __DATA_DIRTY.__objc_data: 0x14c8
+  __DATA.__data: 0x619
+  __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2329
-  Symbols:   4610
-  CStrings:  1063
+  Functions: 2334
+  Symbols:   4620
+  CStrings:  1067
 
Symbols:
+ +[RBSProcessIdentity _applicationIdentityMatchingPersona:fromIdentities:]
+ -[RBSProcessIdentity applicationIdentityWithError:]
+ -[RBSProcessMonitorConfiguration _ensureVisibilityNamespaceIsTracked]
+ -[RBSProcessMonitorConfiguration wantsVisibilityChangesOnly]
+ _NSUnderlyingErrorKey
+ __errorWithRequestCode
+ _objc_msgSend$_applicationIdentityMatchingPersona:fromIdentities:
+ _objc_msgSend$_ensureVisibilityNamespaceIsTracked
+ _objc_msgSend$identities
+ _objc_msgSend$initWithJobLabel:error:
CStrings:
+ "RBSProcessIdentity does not represent a LSApplicationIdentity"
+ "could not resolve LSApplicationRecord for bundleIdentifier"
+ "could not resolve LSApplicationRecord for jobLabel"
+ "no LSApplicationIdentity in application record"
```
