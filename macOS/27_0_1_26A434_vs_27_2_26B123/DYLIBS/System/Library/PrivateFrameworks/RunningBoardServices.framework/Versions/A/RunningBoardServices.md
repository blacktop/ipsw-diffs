## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices`

```diff

-1080.0.0.0.0
-  __TEXT.__text: 0x4887c
-  __TEXT.__objc_methlist: 0x5c98
+1084.40.7.0.0
+  __TEXT.__text: 0x48f0c
+  __TEXT.__objc_methlist: 0x5cc8
   __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x4abd
+  __TEXT.__cstring: 0x4b98
   __TEXT.__oslogstring: 0x29d9
   __TEXT.__gcc_except_tab: 0x85c
-  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__unwind_info: 0x16b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e30
+  __DATA_CONST.__objc_selrefs: 0x1e60
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__got: 0x520
   __AUTH_CONST.__const: 0xeb0
-  __AUTH_CONST.__cfstring: 0x6380
+  __AUTH_CONST.__cfstring: 0x6400
   __AUTH_CONST.__objc_const: 0xb210
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x1630
+  __AUTH.__objc_data: 0x1590
   __DATA.__objc_ivar: 0x60c
   __DATA.__data: 0x620
   __DATA.__bss: 0x278
-  __DATA_DIRTY.__objc_data: 0x1540
+  __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2412
-  Symbols:   4778
-  CStrings:  1113
+  Functions: 2417
+  Symbols:   4788
+  CStrings:  1117
 
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
