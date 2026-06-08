## CaptiveNetwork

> `/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork`

```diff

-514.120.2.0.0
-  __TEXT.__text: 0xa408
-  __TEXT.__auth_stubs: 0x820
+538.0.0.0.1
+  __TEXT.__text: 0xa354
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x150
+  __TEXT.__const: 0x158
   __TEXT.__cstring: 0x670
   __TEXT.__oslogstring: 0x70b
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methname: 0x2c
-  __TEXT.__objc_methtype: 0x46
-  __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x598
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_const: 0x40
+  __AUTH_CONST.__auth_got: 0x418
   __DATA.__data: 0x150
   __DATA.__bss: 0x78
   __DATA_DIRTY.__data: 0x10

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F29E7049-9BFA-35B6-A9BE-78BBB98B120B
-  Functions: 215
-  Symbols:   639
-  CStrings:  237
+  UUID: EF9AD078-85DD-30E4-ADC9-4A97CAAEE1B4
+  Functions: 217
+  Symbols:   642
+  CStrings:  233
 
Symbols:
+ _CNShowBBMonitorPrompt
+ _ShowBBMonitorPrompt
Functions:
~ ___CNMonitorSetupConnection_block_invoke : 420 -> 376
~ _CNPluginMonitorHandleCommand : 488 -> 444
~ _CNProberProvideResult : 212 -> 168
+ _CNShowBBMonitorPrompt
~ __CNPluginProvideResponse : 352 -> 284
~ _CNPluginRegister : 704 -> 660
~ ___CNPluginRegister_block_invoke : 924 -> 880
~ _CNPluginResponseSetNetworkList : 236 -> 192
~ _CNPluginResponseSetNetwork : 236 -> 192
~ ___CNWebSheetProbeRequest_block_invoke : 784 -> 740
~ ___CNWebSheetRegister_block_invoke : 1692 -> 1648
~ _ServerConnectionCreate : 980 -> 936
~ _ServerConnectionProvideResponse : 308 -> 276
~ _ServerConnectionSendCmdAck : 308 -> 276
~ _ServerConnectionProcessControl : 384 -> 340
~ _CNScanListFilterHandleCommand : 676 -> 632
+ _ShowBBMonitorPrompt
CStrings:
- "CaptiveNetworkPlugin"
- "bindToCommand:"
- "setBoundInterfaceIdentifier:"
- "v24@0:8^{__CNPluginCommand={__CFRuntimeBase=QAQ}^{__CFDictionary}I}16"

```
