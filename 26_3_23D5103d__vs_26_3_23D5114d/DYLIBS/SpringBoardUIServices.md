## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4557.3.4.0.0
-  __TEXT.__text: 0x9ff1c
-  __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_methlist: 0xe2ec
+4557.3.8.0.0
+  __TEXT.__text: 0xa0264
+  __TEXT.__auth_stubs: 0x1630
+  __TEXT.__objc_methlist: 0xe304
   __TEXT.__const: 0xa08
   __TEXT.__gcc_except_tab: 0x9ac
-  __TEXT.__cstring: 0xa5e3
+  __TEXT.__cstring: 0xa662
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x4581
-  __TEXT.__unwind_info: 0x3058
-  __TEXT.__objc_classname: 0x3e49
-  __TEXT.__objc_methname: 0x23ecf
+  __TEXT.__unwind_info: 0x3060
+  __TEXT.__objc_classname: 0x3e4b
+  __TEXT.__objc_methname: 0x23f8e
   __TEXT.__objc_methtype: 0x6129
-  __TEXT.__objc_stubs: 0x16c20
-  __DATA_CONST.__got: 0x1028
+  __TEXT.__objc_stubs: 0x16d00
+  __DATA_CONST.__got: 0x1040
   __DATA_CONST.__const: 0x2c68
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x4c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a70
+  __DATA_CONST.__objc_selrefs: 0x7aa8
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x5c8
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0xb20
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __AUTH_CONST.__auth_got: 0xb28
   __AUTH_CONST.__const: 0x940
-  __AUTH_CONST.__cfstring: 0x9e00
-  __AUTH_CONST.__objc_const: 0x2ce10
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__cfstring: 0x9ee0
+  __AUTH_CONST.__objc_const: 0x2ce30
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x4dd0
-  __DATA.__objc_ivar: 0xcf0
+  __DATA.__objc_ivar: 0xcf4
   __DATA.__data: 0x3928
   __DATA.__bss: 0x3d8
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBBD202C-413F-362F-8084-9E9C4C67A6F4
-  Functions: 4615
-  Symbols:   17470
-  CStrings:  9493
+  UUID: 5AE64E06-22F6-3B77-934B-5542377C7345
+  Functions: 4618
+  Symbols:   17488
+  CStrings:  9516
 
Symbols:
+ -[SBUIPowerDownView _addInfoButtonIfNeeded]
+ -[SBUIPowerDownView _infoButtonTapped]
+ GCC_except_table56
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _OBJC_CLASS_$_SBSRemoteAlertDefinition
+ _OBJC_CLASS_$_SBSRemoteAlertHandle
+ _OBJC_IVAR_$_SBUIPowerDownView._infoButton
+ __SBDeviceRegionRequiresIMEIDisplay
+ _objc_msgSend$_addInfoButtonIfNeeded
+ _objc_msgSend$activateWithContext:
+ _objc_msgSend$addConstraint:
+ _objc_msgSend$initWithServiceName:viewControllerClassName:
+ _objc_msgSend$newHandleWithDefinition:configurationContext:
+ _objc_msgSend$setReason:
+ _objc_msgSend$setUserInfo:
- GCC_except_table50
Functions:
+ __SBDeviceRegionRequiresIMEIDisplay
~ -[SBUIPowerDownView initWithFrame:vibrantSettings:] : 1332 -> 1340
+ -[SBUIPowerDownView _addInfoButtonIfNeeded]
~ ___45-[SBUIPowerDownView showAnimated:completion:]_block_invoke_2 : 140 -> 164
~ ___45-[SBUIPowerDownView hideAnimated:completion:]_block_invoke_2 : 128 -> 152
+ -[SBUIPowerDownView _infoButtonTapped]
~ -[SBUIPowerDownView .cxx_destruct] : 260 -> 280
CStrings:
+ "\n!"
+ "AH"
+ "FlowTypeKey"
+ "Power Down Regulatory Info"
+ "RegionCode"
+ "TSSIMSetupSupportViewController"
+ "_addInfoButtonIfNeeded"
+ "_infoButton"
+ "_infoButtonTapped"
+ "activateWithContext:"
+ "addConstraint:"
+ "cellular-data"
+ "com.apple.SIMSetupUIService"
+ "initWithServiceName:viewControllerClassName:"
+ "newHandleWithDefinition:configurationContext:"
+ "setReason:"
+ "\xb1"
- "\t!"

```
