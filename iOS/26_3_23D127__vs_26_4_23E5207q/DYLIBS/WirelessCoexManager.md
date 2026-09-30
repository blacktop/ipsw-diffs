## WirelessCoexManager

> `/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager`

```diff

-1860.5.1.0.0
-  __TEXT.__text: 0xa81c
+1870.4.0.0.0
+  __TEXT.__text: 0xa8ec
   __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_methlist: 0x678
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__gcc_except_tab: 0x250
   __TEXT.__cstring: 0x1974
-  __TEXT.__oslogstring: 0x42a
-  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__oslogstring: 0x6e5
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0xdb
   __TEXT.__objc_methname: 0x126c
-  __TEXT.__objc_methtype: 0x26c
+  __TEXT.__objc_methtype: 0x264
   __TEXT.__objc_stubs: 0xa60
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__const: 0x700
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x420
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x120
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0xda8
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x30

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE07D6B3-42CD-3558-B252-8581F1CD8403
-  Functions: 201
-  Symbols:   752
-  CStrings:  647
+  UUID: 87427EFD-3CE7-303A-9BD9-FA8CAA9C0B07
+  Functions: 210
+  Symbols:   771
+  CStrings:  661
 
Symbols:
+ -[WRM_UCMInterface getInstantLoad].cold.1
+ -[WRM_UCMInterface getInstantLoad].cold.2
+ -[WRM_UCMInterface getInstantLoad].cold.3
+ -[WRM_UCMInterface getWirelessULFrequencyBandUpdates:].cold.1
+ -[WRM_UCMInterface getWirelessULFrequencyBandUpdates:].cold.2
+ -[WRM_UCMInterface getWirelessULFrequencyBandUpdates:].cold.3
+ -[WRM_UCMInterface startTimer:].cold.1
+ -[WRM_UCMInterface startTimer:].cold.2
+ -[WRM_UCMInterface startTimer:].cold.3
+ -[WRM_UCMInterface stopTimer].cold.1
+ -[WRM_UCMInterface stopTimer].cold.2
+ -[WRM_UCMInterface stopTimer].cold.3
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table25
+ _OUTLINED_FUNCTION_1
+ ___58-[WRM_UCMInterface getWirelessFrequencyBandUpdatesForMIC:]_block_invoke.124
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ _dispatch_sync
+ _objc_retainAutoreleasedReturnValue
+ _xpc_connection_send_message_with_reply_sync
- GCC_except_table40
- ___29-[WRM_UCMInterface stopTimer]_block_invoke.86
- ___31-[WRM_UCMInterface startTimer:]_block_invoke.89
- ___34-[WRM_UCMInterface getInstantLoad]_block_invoke.83
- ___54-[WRM_UCMInterface getWirelessULFrequencyBandUpdates:]_block_invoke
- ___58-[WRM_UCMInterface getWirelessFrequencyBandUpdatesForMIC:]_block_invoke.130
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "getInstantLoad: Current BT Load: %u"
+ "getInstantLoad: Failed to create XPC arguments dictionary"
+ "getInstantLoad: Failed to get BT load"
+ "getInstantLoad: Invalid XPC connection"
+ "getWirelessULFrequencyBandUpdates: %@"
+ "getWirelessULFrequencyBandUpdates: Failed to create XPC arguments dictionary"
+ "getWirelessULFrequencyBandUpdates: Failed to get frequency updates"
+ "getWirelessULFrequencyBandUpdates: Invalid XPC connection"
+ "getWirelessULFrequencyBandUpdates: Registering for updates"
+ "getWirelessULFrequencyBandUpdates: Registration complete"
+ "i24@0:8d16"
+ "startTimer: Failed to create XPC arguments dictionary"
+ "startTimer: Failed to get initial BT load"
+ "startTimer: Initial BT Load: %u"
+ "startTimer: Invalid XPC connection"
+ "startTimer: Starting BT load timer with duration %.2f seconds"
+ "stopTimer: Failed to create XPC arguments dictionary"
+ "stopTimer: Failed to get max BT load"
+ "stopTimer: Invalid XPC connection"
+ "stopTimer: Max BT Load: %u"
+ "stopTimer: Stopping BT load timer"
- "I16@0:8"
- "I24@0:8d16"
- "Received getWirelessULFrequencyBandUpdates"
- "getWirelessRadioManagerReportLoad Current BT Load: %u"
- "getWirelessRadioManagerReportLoad Max BT Load: %u"
- "getWirelessRadioManagerReportLoad Stop Timer"
- "getWirelessRadioManagerReportLoad start Timer"

```
