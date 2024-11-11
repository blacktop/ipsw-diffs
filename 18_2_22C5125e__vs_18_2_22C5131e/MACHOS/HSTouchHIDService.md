## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-8120.3.0.0.0
-  __TEXT.__text: 0xfec80
+8120.4.0.0.0
+  __TEXT.__text: 0xff024
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x4c20
-  __TEXT.__init_offsets: 0x1f1c
-  __TEXT.__objc_methlist: 0x3b34
-  __TEXT.__const: 0x3e0e
-  __TEXT.__gcc_except_tab: 0xd810
-  __TEXT.__cstring: 0x97f1
-  __TEXT.__oslogstring: 0x3003
-  __TEXT.__objc_methname: 0x5613
-  __TEXT.__objc_classname: 0xae2
+  __TEXT.__objc_stubs: 0x4c80
+  __TEXT.__init_offsets: 0x1f20
+  __TEXT.__objc_methlist: 0x3b74
+  __TEXT.__const: 0x3e2e
+  __TEXT.__gcc_except_tab: 0xd880
+  __TEXT.__cstring: 0x980e
+  __TEXT.__oslogstring: 0x3047
+  __TEXT.__objc_methname: 0x566d
+  __TEXT.__objc_classname: 0xb07
   __TEXT.__objc_methtype: 0x6fc2
-  __TEXT.__unwind_info: 0x5548
+  __TEXT.__unwind_info: 0x5570
   __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x1dd8
   __DATA_CONST.__cfstring: 0x6260
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x398
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_const: 0x7fe0
-  __DATA.__objc_selrefs: 0x1658
+  __DATA.__objc_const: 0x8070
+  __DATA.__objc_selrefs: 0x1670
   __DATA.__objc_ivar: 0x4ec
-  __DATA.__objc_data: 0x2030
-  __DATA.__data: 0x1510
+  __DATA.__objc_data: 0x2080
+  __DATA.__data: 0x1520
   __DATA.__bss: 0xb8
   __DATA.__common: 0x890
   - /AppleInternal/Library/Frameworks/HIDSensingInternalSupport.framework/HIDSensingInternalSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7138
-  Symbols:   25768
-  CStrings:  3141
+  Functions: 7145
+  Symbols:   25820
+  CStrings:  3148
 
Symbols:
+ +[HSTProxClearedAfterOccludedWakeEvent hsClassName]
+ -[HSTBackboardBridge _handleProxClearedAfterOccludedWake]
+ -[HSTBackboardBridge _handleSetPropertyEvent:].cold.9
+ -[HSTFirmwareManager _handleProxClearedAfterOccludedWakeEvent:]
+ -[HSTFirmwareManager _isSleeping]
+ _OBJC_CLASS_$_HSTProxClearedAfterOccludedWakeEvent
+ _OBJC_METACLASS_$_HSTProxClearedAfterOccludedWakeEvent
+ __OBJC_$_CLASS_METHODS_HSTProxClearedAfterOccludedWakeEvent
+ __OBJC_CLASS_RO_$_HSTProxClearedAfterOccludedWakeEvent
+ __OBJC_METACLASS_RO_$_HSTProxClearedAfterOccludedWakeEvent
+ __ZGVN6HSUtil8CoderKey7LiteralIJLc72ELc83ELc84ELc80ELc114ELc111ELc120ELc67ELc108ELc101ELc97ELc114ELc101ELc100ELc65ELc102ELc116ELc101ELc114ELc79ELc99ELc99ELc108ELc117ELc100ELc101ELc100ELc87ELc97ELc107ELc101ELc69ELc118ELc101ELc110ELc116EEE3KeyE
+ __ZN6HSUtil11DynamicCastI36HSTProxClearedAfterOccludedWakeEventEEPT_P11objc_object
+ __ZN6HSUtil8CoderKey7LiteralIJLc72ELc83ELc84ELc80ELc114ELc111ELc120ELc67ELc108ELc101ELc97ELc114ELc101ELc100ELc65ELc102ELc116ELc101ELc114ELc79ELc99ELc99ELc108ELc117ELc100ELc101ELc100ELc87ELc97ELc107ELc101ELc69ELc118ELc101ELc110ELc116EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc72ELc83ELc84ELc80ELc114ELc111ELc120ELc67ELc108ELc101ELc97ELc114ELc101ELc100ELc65ELc102ELc116ELc101ELc114ELc79ELc99ELc99ELc108ELc117ELc100ELc101ELc100ELc87ELc97ELc107ELc101ELc69ELc118ELc101ELc110ELc116EEE4_StrE
+ __cxx_global_var_init.181
+ __cxx_global_var_init.365
+ _objc_msgSend$_handleProxClearedAfterOccludedWake
+ _objc_msgSend$_handleProxClearedAfterOccludedWakeEvent:
+ _objc_msgSend$_isSleeping
- GCC_except_table103
- __cxx_global_var_init.179
CStrings:
+ "8120.4"
+ "HSTProxClearedAfterOccludedWakeEvent"
+ "Ignoring prox clear while sleeping"
+ "Prox cleared after occluded wake"
+ "ProxClearedAfterOccludedWake"
+ "_handleProxClearedAfterOccludedWake"
+ "_handleProxClearedAfterOccludedWakeEvent:"
+ "_isSleeping"
- "8120.3"

```
