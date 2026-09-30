## AOSUI

> `/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI`

```diff

-917.0.0.0.0
-  __TEXT.__text: 0x113a14
-  __TEXT.__objc_methlist: 0x10c34
-  __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x12a3c
-  __TEXT.__oslogstring: 0xccc2
-  __TEXT.__gcc_except_tab: 0x173c
+920.3.1.0.0
+  __TEXT.__text: 0x114250
+  __TEXT.__objc_methlist: 0x10c4c
+  __TEXT.__const: 0x2d8
+  __TEXT.__cstring: 0x12a65
+  __TEXT.__oslogstring: 0xcdcc
+  __TEXT.__gcc_except_tab: 0x1774
   __TEXT.__ustring: 0x132
   __TEXT.__dlopen_cstrs: 0x1f4
-  __TEXT.__unwind_info: 0x4750
+  __TEXT.__unwind_info: 0x4778
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9728
+  __DATA_CONST.__objc_selrefs: 0x9760
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x108
-  __DATA_CONST.__got: 0x1888
-  __AUTH_CONST.__const: 0x42f0
+  __DATA_CONST.__got: 0x1898
+  __AUTH_CONST.__const: 0x4320
   __AUTH_CONST.__cfstring: 0xc8e0
-  __AUTH_CONST.__objc_const: 0x2f370
+  __AUTH_CONST.__objc_const: 0x2f390
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x180

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x35c0
   __AUTH.__data: 0x9e8
-  __DATA.__objc_ivar: 0x14a0
+  __DATA.__objc_ivar: 0x14a4
   __DATA.__data: 0x22a0
   __DATA.__bss: 0x2b0
   __DATA.__common: 0x28

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7265
-  Symbols:   14834
-  CStrings:  3306
+  Functions: 7273
+  Symbols:   14850
+  CStrings:  3311
 
Symbols:
+ -[AOSUIPrivateEmailController _presentRemoteUIForURL:account:window:]
+ -[AOSUIPrivateEmailController _presentWebViewForURL:window:]
+ -[AOSUIPrivateEmailController showPrivateEmailManage:account:]
+ OBJC_IVAR_$_AOSUIPrivateEmailController._remoteUISheetWindow
+ _AKURLBagKeyPrivateEmailManage
+ _OBJC_CLASS_$_AAUIMacRemoteUIViewFactory
+ __62-[AOSUIPrivateEmailController showPrivateEmailManage:account:]_block_invoke
+ ___62-[AOSUIPrivateEmailController showPrivateEmailManage:account:]_block_invoke
+ ___69-[AOSUIPrivateEmailController _presentRemoteUIForURL:account:window:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e40_v24?0"AKURLConfiguration"8"NSError"16l
+ _objc_msgSend$_presentRemoteUIForURL:account:window:
+ _objc_msgSend$_presentWebViewForURL:window:
+ _objc_msgSend$createRemoteUIViewControllerWithURL:account:
+ _objc_msgSend$setFrame:display:
+ _objc_msgSend$setMeCardIdentifier:
+ _objc_msgSend$showPrivateEmailManage:account:
+ _objc_msgSend$uiType
+ _objc_msgSend$urlConfigurationForKey:fromCache:completion:
- -[AOSUIPrivateEmailController showPrivateEmailManage:]
- _objc_msgSend$showPrivateEmailManage:
CStrings:
+ "%s: profile picture has no valid CGImage representation (Size: %@); skipping cache write."
+ "Failed to fetch HME manage URL configuration: %@"
+ "HME RemoteUI factory returned no view controller; falling back to webview"
+ "Presented HME RemoteUI sheet with response code: %ld"
+ "v24@?0@\"AKURLConfiguration\"8@\"NSError\"16"
```
