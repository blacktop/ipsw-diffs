## NetAppsUtilities

> `/System/Library/PrivateFrameworks/NetAppsUtilities.framework/Versions/A/NetAppsUtilities`

```diff

-101.4.1.0.0
-  __TEXT.__text: 0x1d77c
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x1dd4
+104.5.1.0.0
+  __TEXT.__text: 0x1d6d4
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0x2074
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x314
-  __TEXT.__cstring: 0xb97
+  __TEXT.__cstring: 0xb93
   __TEXT.__oslogstring: 0x18a
   __TEXT.__unwind_info: 0x960
   __TEXT.__objc_classname: 0x417

   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1248
+  __DATA_CONST.__objc_selrefs: 0x12b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2b8
   __AUTH_CONST.__const: 0xf80
   __AUTH_CONST.__cfstring: 0xb60
-  __AUTH_CONST.__objc_const: 0x3e98
+  __AUTH_CONST.__objc_const: 0x3a30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x1b4

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17149ABD-851F-365B-843E-F97243BD709D
-  Functions: 782
-  Symbols:   2058
-  CStrings:  1265
+  UUID: E5FD93C4-06E9-365E-987E-622CCB2E42BA
+  Functions: 789
+  Symbols:   2069
+  CStrings:  1263
 
Symbols:
+ +[NAIdentity na_identity].cold.1
+ +[NAIdentityBuilder na_identity].cold.1
+ +[NATreeNode na_identity].cold.1
+ -[NADelegateDispatcher _logEventForInvocation:metadata:].cold.1
+ -[NADelegateDispatcher _logEventForSelector:metadata:].cold.1
+ -[NADelegateDispatcher _logEventForSelector:metadata:formatArgs:arg0:].cold.1
+ -[NADescriptionBuilder appendTimeInterval:withName:decomposeUnits:].cold.1
+ __32-[NADecayingTimer _nextFireDate]_block_invoke.cold.1
+ __33+[NAScheduler immediateScheduler]_block_invoke.cold.1
+ __34+[NAScheduler mainThreadScheduler]_block_invoke.cold.1
+ __35+[NAScheduler globalAsyncScheduler]_block_invoke.cold.1
+ __46+[NAFuture(NAConveniences) futureWithNoResult]_block_invoke.cold.1
- _strcmp

```
