## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-8120.2.0.0.0
-  __TEXT.__text: 0xfea60
+8120.3.0.0.0
+  __TEXT.__text: 0xfec80
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x4be0
+  __TEXT.__objc_stubs: 0x4c20
   __TEXT.__init_offsets: 0x1f1c
-  __TEXT.__objc_methlist: 0x3b14
+  __TEXT.__objc_methlist: 0x3b34
   __TEXT.__const: 0x3e0e
-  __TEXT.__gcc_except_tab: 0xd7d8
-  __TEXT.__cstring: 0x97c7
+  __TEXT.__gcc_except_tab: 0xd810
+  __TEXT.__cstring: 0x97f1
   __TEXT.__oslogstring: 0x3003
-  __TEXT.__objc_methname: 0x55c5
+  __TEXT.__objc_methname: 0x5613
   __TEXT.__objc_classname: 0xae2
   __TEXT.__objc_methtype: 0x6fc2
-  __TEXT.__unwind_info: 0x5530
+  __TEXT.__unwind_info: 0x5548
   __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x1dd8
-  __DATA_CONST.__cfstring: 0x6200
+  __DATA_CONST.__cfstring: 0x6260
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_arraydata: 0x398
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_const: 0x7fc0
-  __DATA.__objc_selrefs: 0x1640
+  __DATA.__objc_const: 0x7fe0
+  __DATA.__objc_selrefs: 0x1658
   __DATA.__objc_ivar: 0x4ec
   __DATA.__objc_data: 0x2030
   __DATA.__data: 0x1510

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7135
-  Symbols:   25750
-  CStrings:  3133
+  Functions: 7138
+  Symbols:   25768
+  CStrings:  3141
 
Symbols:
+ -[MTTrackpadUberAlg divingButtonState]
+ -[MTTrackpadUberAlg setDivingButtonState:]
+ -[TrackpadAlgStage deviceButtonState]
+ -[TrackpadAlgStage setDeviceButtonState:]
+ -[TrackpadBridge _handleHSTNotificationEvent:]
+ GCC_except_table112
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table236
+ GCC_except_table270
+ GCC_except_table87
+ OBJC_IVAR_$_MTTrackpadUberAlg._divingButtonState
+ OBJC_IVAR_$_TrackpadAlgStage._deviceButtonState
+ __27-[TrackpadBridge setQueue:]_block_invoke.106
+ _objc_msgSend$divingButtonState
+ _objc_msgSend$setDeviceButtonState:
+ _objc_msgSend$setDivingButtonState:
- -[MacTrackpadBridge _handleHSTNotificationEvent:]
- -[MacTrackpadBridge handleHSTEvent:]
- GCC_except_table111
- GCC_except_table209
- GCC_except_table210
- GCC_except_table215
- GCC_except_table216
- GCC_except_table221
- GCC_except_table222
- GCC_except_table227
- GCC_except_table228
- GCC_except_table233
- GCC_except_table262
- GCC_except_table263
- GCC_except_table93
- OBJC_IVAR_$_TrackpadAlgStage._previousButtonState
- OBJC_IVAR_$_TrackpadSettingsManager._parserExternallyDisabled
- __27-[TrackpadBridge setQueue:]_block_invoke.101
- _objc_msgSend$parserExternallyDisabled
CStrings:
+ "-[TrackpadBridge _handleHSTNotificationEvent:]"
+ "8120.3"
+ "DivingButtonState"
+ "Properties"
+ "TB,N"
+ "TB,N,V_divingButtonState"
+ "TI,N,V_deviceButtonState"
+ "TrackpadExternallyDisabled"
+ "UberAlg"
+ "_divingButtonState"
+ "divingButtonState"
+ "setDeviceButtonState:"
+ "setDivingButtonState:"
- "-[MacTrackpadBridge _handleHSTNotificationEvent:]"
- "8120.2"
- "TB,N,V_parserExternallyDisabled"
- "UberAlgsProperties"
- "_parserExternallyDisabled"

```
