## WebApp

> `/System/Library/PrivateFrameworks/WebApp.framework/WebApp`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

-625.1.22.10.3
-  __TEXT.__text: 0x2f18
-  __TEXT.__objc_methlist: 0x824
-  __TEXT.__cstring: 0x22a
+625.1.24.10.1
+  __TEXT.__text: 0x3330
+  __TEXT.__objc_methlist: 0x844
+  __TEXT.__cstring: 0x23c
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__oslogstring: 0x156
+  __TEXT.__oslogstring: 0x194
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x188
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a8
+  __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x40
+  __DATA_CONST.__got: 0x108
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x1420
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 78
-  Symbols:   447
-  CStrings:  34
+  Functions: 83
+  Symbols:   467
+  CStrings:  36
 
Symbols:
+ -[WebAppSceneDelegate _liveManagedGuidedBrowserSceneExcludingSession:]
+ -[WebAppSceneDelegate _notifyMainGuidedBrowserOfBlockedNewWindowOnScene:]
+ -[WebAppViewController showGuidedBrowsingNewWindowBlockedNotice]
+ GCC_except_table22
+ GCC_except_table28
+ _OBJC_CLASS_$_UIWindowScene
+ ___58-[WebAppSceneDelegate scene:willConnectToSession:options:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ __os_log_error_impl
+ _objc_enumerationMutation
+ _objc_msgSend$_liveManagedGuidedBrowserSceneExcludingSession:
+ _objc_msgSend$_notifyMainGuidedBrowserOfBlockedNewWindowOnScene:
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$delegate
+ _objc_msgSend$firstObject
+ _objc_msgSend$keyWindow
+ _objc_msgSend$requestSceneSessionDestruction:options:errorHandler:
+ _objc_msgSend$rootViewController
+ _objc_msgSend$showGuidedBrowsingNewWindowBlockedNotice
+ _objc_msgSend$windows
+ _objc_opt_isKindOfClass
+ _objc_retain_x25
- GCC_except_table21
- GCC_except_table27
- _objc_retain_x24
CStrings:
+ "Failed to destroy duplicate Guided Browsing scene: %{public}@"
+ "v16@?0@\"NSError\"8"
```
