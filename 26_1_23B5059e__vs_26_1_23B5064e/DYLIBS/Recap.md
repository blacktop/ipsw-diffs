## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

```diff

-170.101.0.0.0
-  __TEXT.__text: 0x20500
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x32e8
+170.104.0.0.0
+  __TEXT.__text: 0x20678
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_methlist: 0x3320
   __TEXT.__const: 0x350
-  __TEXT.__cstring: 0x1a68
+  __TEXT.__cstring: 0x1a7f
   __TEXT.__oslogstring: 0x37f
   __TEXT.__gcc_except_tab: 0xb28
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x960
+  __TEXT.__unwind_info: 0x968
   __TEXT.__objc_classname: 0x658
-  __TEXT.__objc_methname: 0x7a57
+  __TEXT.__objc_methname: 0x7b08
   __TEXT.__objc_methtype: 0x1795
-  __TEXT.__objc_stubs: 0x5400
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x538
+  __TEXT.__objc_stubs: 0x5440
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0x560
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_selrefs: 0x1d00
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x448
-  __AUTH_CONST.__auth_got: 0x718
+  __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x1e60
-  __AUTH_CONST.__objc_const: 0x5090
+  __AUTH_CONST.__objc_const: 0x5100
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x380
+  __DATA.__objc_ivar: 0x388
   __DATA.__data: 0x968
   __DATA.__bss: 0x148
   __DATA.__common: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2529B838-8579-32BE-8209-A71EDD9B3F01
-  Functions: 971
-  Symbols:   3743
-  CStrings:  2209
+  UUID: DB77FA7C-3592-32A1-B642-21892B9D8DEA
+  Functions: 976
+  Symbols:   3764
+  CStrings:  2218
 
Symbols:
+ -[CLTTool .cxx_destruct]
+ -[CLTTool setSignalQueue:]
+ -[CLTTool setSignalSources:]
+ -[CLTTool signalQueue]
+ -[CLTTool signalSources]
+ _OBJC_IVAR_$_CLTTool._signalQueue
+ _OBJC_IVAR_$_CLTTool._signalSources
+ __OBJC_$_INSTANCE_VARIABLES_CLTTool
+ __OBJC_$_PROP_LIST_CLTTool
+ ___15-[CLTTool main]_block_invoke
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ __dispatch_source_type_signal
+ _dispatch_activate
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _objc_msgSend$signalQueue
+ _objc_msgSend$signalSources
- _signal_handler
CStrings:
+ "00:46:50"
+ "Oct  6 2025"
+ "T@\"NSMutableArray\",&,N,V_signalSources"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_signalQueue"
+ "_signalQueue"
+ "_signalSources"
+ "com.apple.recap.signal"
+ "setSignalQueue:"
+ "setSignalSources:"
+ "signalQueue"
+ "signalSources"
- "05:05:27"
- "Sep 26 2025"

```
