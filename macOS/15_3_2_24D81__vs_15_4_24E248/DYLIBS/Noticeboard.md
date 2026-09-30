## Noticeboard

> `/System/Library/PrivateFrameworks/Noticeboard.framework/Versions/A/Noticeboard`

```diff

 27.0.0.0.0
-  __TEXT.__text: 0x428c
+  __TEXT.__text: 0x4298
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x334
+  __TEXT.__objc_methlist: 0x370
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x917
   __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__unwind_info: 0x130
   __TEXT.__objc_classname: 0x88
   __TEXT.__objc_methname: 0x1112
   __TEXT.__objc_methtype: 0x1b4

   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x5e0
+  __AUTH_CONST.__objc_const: 0x578
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x80

   - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01544E60-169C-3BAE-9604-7890EECF61B2
-  Functions: 80
-  Symbols:   384
+  UUID: 1E0A132F-D4BF-33AC-AC42-765F0B9A2603
+  Functions: 84
+  Symbols:   388
   CStrings:  379
 
Symbols:
+ +[NBStateController sharedInstance].cold.1
+ +[NSString(BundleLocalization) _osVersionReturningMajor:minor:point:].cold.1
+ -[NBUpdateController _catalogURL].cold.1
+ NBLogObject.cold.1
Functions:
~ +[NBError errorWithCode:underlyingError:userInfo:] : 860 -> 868
~ _NBLogObject : 84 -> 68
~ +[NSString(BundleLocalization) _osVersionReturningMajor:minor:point:] : 140 -> 124
~ -[NBUpdateController productIsSkippable:lastCatalogCheckTimeStamp:considerStagedUpdatesOnly:] : 432 -> 404
~ ___39-[NBUpdateController downloadProducts:]_block_invoke : 2160 -> 2184
~ -[NBUpdateController _catalogURL] : 240 -> 220
~ +[NBStateController sharedInstance] : 84 -> 68
~ ___38-[NBStateController remoteObjectProxy]_block_invoke : 192 -> 188

```
