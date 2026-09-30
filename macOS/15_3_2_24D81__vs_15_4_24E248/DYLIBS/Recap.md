## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Versions/A/Recap`

```diff

-158.0.0.0.0
-  __TEXT.__text: 0x1fb80
+159.1.0.0.0
+  __TEXT.__text: 0x1faf0
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x26c4
+  __TEXT.__objc_methlist: 0x3118
   __TEXT.__cstring: 0x1989
   __TEXT.__const: 0x2f4
   __TEXT.__oslogstring: 0x204
   __TEXT.__ustring: 0x1e
-  __TEXT.__gcc_except_tab: 0xa78
+  __TEXT.__gcc_except_tab: 0xa80
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__unwind_info: 0x840
   __TEXT.__objc_classname: 0x631
   __TEXT.__objc_methname: 0x73e9
   __TEXT.__objc_methtype: 0x1729

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a18
+  __DATA_CONST.__objc_selrefs: 0x1ad8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x448
   __AUTH_CONST.__auth_got: 0x568
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0x1da0
-  __AUTH_CONST.__objc_const: 0x60d8
+  __AUTH_CONST.__objc_const: 0x4da8
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x230

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE18D95E-3EB3-390D-9076-E34E39CD4ACB
-  Functions: 902
-  Symbols:   2531
+  UUID: 35B151D7-1BAD-3C32-B715-D45A697670A5
+  Functions: 931
+  Symbols:   2564
   CStrings:  2102
 
Symbols:
+ +[RCPEventSenderProperties _cachedPropertiesOrCacheIfNeeded:senderID:].cold.1
+ +[RCPEventSenderProperties crownSender].cold.1
+ +[RCPEventSenderProperties gamepadSender].cold.1
+ +[RCPEventSenderProperties globalPositionSender].cold.1
+ +[RCPEventSenderProperties keyboardSenderForDisplayUUID:].cold.1
+ +[RCPEventSenderProperties keyboardSender].cold.1
+ +[RCPEventSenderProperties mouseSender].cold.1
+ +[RCPEventSenderProperties naturalInputCollectionSender].cold.1
+ +[RCPEventSenderProperties pencilDigitizerSender].cold.1
+ +[RCPEventSenderProperties phoneButtonSender].cold.1
+ +[RCPEventSenderProperties senderFromIOHIDService:].cold.1
+ +[RCPEventSenderProperties supplyMissingStandardProperties:senderID:].cold.1
+ +[RCPEventSenderProperties touchScreenDigitizerSenderForDisplayUUID:].cold.1
+ +[RCPEventSenderProperties touchScreenDigitizerSender].cold.1
+ +[RCPEventSenderProperties trackpadSender].cold.1
+ +[RCPEventSenderProperties tvRemoteSender].cold.1
+ +[RCPInlinePlayer sharedInstance].cold.1
+ +[RCPPlayer sharedPlayer].cold.1
+ +[RCPRecorder sharedRecorder].cold.1
+ -[RCPSyntheticEventStream pointerDiscreteScroll:duration:frequency:].cold.1
+ RCPLogPlayback.cold.1
+ RCPLogWorkarounds.cold.1
+ RCPMachDurationFromTimeInterval.cold.1
+ RCPMachTimestampFromTimeInterval.cold.2
+ RCPTimeIntervalFromMachDuration.cold.1
+ RCPTimeIntervalFromMachTimestamp.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _RCPIsAllowlistedProperty.cold.1
+ _RCPVirtualHIDServiceQueue.cold.1
+ parseCommandFromCLIArguments.cold.1
CStrings:
+ "22:25:00"
+ "Mar  7 2025"
- "00:20:19"
- "Dec 14 2024"

```
