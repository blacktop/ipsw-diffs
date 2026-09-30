## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-347.26.2.0.0
-  __TEXT.__text: 0xf9870
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x9dc0
+347.31.0.0.0
+  __TEXT.__text: 0xf9900
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x9e30
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x1918
+  __TEXT.__cstring: 0x18e5
   __TEXT.__gcc_except_tab: 0x1008
   __TEXT.__oslogstring: 0x246f
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1898
-  __TEXT.__objc_classname: 0x1675
-  __TEXT.__objc_methname: 0x1ac7a
-  __TEXT.__objc_methtype: 0x5534
-  __TEXT.__objc_stubs: 0x12120
-  __DATA_CONST.__got: 0xab0
-  __DATA_CONST.__const: 0x2430
+  __TEXT.__unwind_info: 0x18a8
+  __TEXT.__objc_classname: 0x169c
+  __TEXT.__objc_methname: 0x1ae26
+  __TEXT.__objc_methtype: 0x557c
+  __TEXT.__objc_stubs: 0x121c0
+  __DATA_CONST.__got: 0xaa8
+  __DATA_CONST.__const: 0x23f0
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d30
+  __DATA_CONST.__objc_selrefs: 0x5d70
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x408
-  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x1efe0
+  __AUTH_CONST.__objc_const: 0x1f0a8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x28f0
-  __DATA.__objc_ivar: 0x9dc
-  __DATA.__data: 0x22b8
+  __DATA.__objc_ivar: 0x9e8
+  __DATA.__data: 0x2318
   __DATA.__bss: 0x120
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80715043-0C91-37C9-B49D-16CEB5E0080E
-  Functions: 3072
-  Symbols:   12364
-  CStrings:  5625
+  UUID: EC438A31-40B4-3821-A79A-E30A7F808F30
+  Functions: 3077
+  Symbols:   12383
+  CStrings:  5637
 
Symbols:
+ -[CPSOverlayViewController environmentProvider]
+ -[CPSOverlayViewController setEnvironmentProvider:]
+ -[CPSTemplateInstance clientApplicationSceneIsConnected]
+ -[CPSTemplateInstance delegate]
+ -[CPSTemplateInstance requiresApplicationScenePresenter]
+ -[CPSTemplateInstance setDelegate:]
+ -[CPSTemplateInstance visibilityEnvironmentIdentifier]
+ GCC_except_table100
+ GCC_except_table68
+ GCC_except_table90
+ GCC_except_table96
+ _OBJC_IVAR_$_CPSOverlayViewController._environmentProvider
+ _OBJC_IVAR_$_CPSTabBarViewController._tabBarButtons
+ _OBJC_IVAR_$_CPSTemplateInstance._delegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPSVisibilityEnvironmentProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPSVisibilityEnvironmentProviding
+ __OBJC_$_PROTOCOL_REFS_CPSVisibilityEnvironmentProviding
+ __OBJC_LABEL_PROTOCOL_$_CPSVisibilityEnvironmentProviding
+ __OBJC_PROTOCOL_$_CPSVisibilityEnvironmentProviding
+ __UIVisibilityEnvironmentForSceneIdentityToken
+ _objc_msgSend$environmentProvider
+ _objc_msgSend$identityToken
+ _objc_msgSend$setEnvironmentProvider:
+ _objc_msgSend$templateInstanceClientDidConnectApplicationScene:
+ _objc_msgSend$templateInstanceClientDidDisconnectApplicationScene:
+ _objc_msgSend$visibilityEnvironmentIdentifier
- GCC_except_table66
- GCC_except_table86
- GCC_except_table94
- GCC_except_table98
- _OBJC_CLASS_$_UIControl
- ___40-[CPSTabBarViewController tabBarButtons]_block_invoke
- ___40-[CPSTabBarViewController tabBarButtons]_block_invoke_2
- ___block_descriptor_32_e16_B16?0"UIView"8l
- ___block_descriptor_32_e33_q24?0"UIControl"8"UIControl"16l
- ___block_literal_global.140
- _objc_msgSend$cps_filter:
CStrings:
+ "\"\x8f\t"
+ "@\"<CPSTemplateInstanceDelegate>\""
+ "@\"<CPSVisibilityEnvironmentProviding>\""
+ "CPSVisibilityEnvironmentProviding"
+ "T@\"<CPSTemplateInstanceDelegate>\",W,N,V_delegate"
+ "T@\"<CPSVisibilityEnvironmentProviding>\",W,N,V_environmentProvider"
+ "T@\"NSArray\",R,N,V_tabBarButtons"
+ "_environmentProvider"
+ "_tabBarButtons"
+ "clientApplicationSceneIsConnected"
+ "environmentProvider"
+ "identityToken"
+ "requiresApplicationScenePresenter"
+ "setEnvironmentProvider:"
+ "templateInstanceClientDidConnectApplicationScene:"
+ "templateInstanceClientDidDisconnectApplicationScene:"
+ "visibilityEnvironmentIdentifier"
- "2"
- "8\xf0\x91"
- "B16@?0@\"UIView\"8"
- "T@\"NSArray\",R,N"
- "q24@?0@\"UIControl\"8@\"UIControl\"16"

```
