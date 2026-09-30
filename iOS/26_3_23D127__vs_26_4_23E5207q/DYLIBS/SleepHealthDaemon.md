## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0xb0f4
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0xad4
+6200.5.77.2.6
+  __TEXT.__text: 0xb558
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_methlist: 0xae4
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x64a
-  __TEXT.__oslogstring: 0x1960
+  __TEXT.__oslogstring: 0x19dc
   __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__unwind_info: 0x270
   __TEXT.__objc_classname: 0x36e
-  __TEXT.__objc_methname: 0x31d5
-  __TEXT.__objc_methtype: 0x9ba
-  __TEXT.__objc_stubs: 0x2220
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x1b0
+  __TEXT.__objc_methname: 0x3221
+  __TEXT.__objc_methtype: 0x9e0
+  __TEXT.__objc_stubs: 0x2240
+  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb00
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x1518
+  __AUTH_CONST.__objc_const: 0x1520
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 437C1D29-B3E5-353E-B647-E56C9F63B373
-  Functions: 159
+  UUID: B8AF836D-2E55-3829-9109-C1873467370B
+  Functions: 160
   Symbols:   1040
-  CStrings:  722
+  CStrings:  727
 
Symbols:
+ _HKSHSleepApneaNotificationActionDelivered
+ _OBJC_CLASS_$_HKSHSleepApneaNotificationInteractedAnalyticsEvent
+ ___109-[HDSHSleepApneaRescindedNotificationManager _showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:]_block_invoke.399
+ ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.359
+ ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.361
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_literal_global.355
+ _objc_msgSend$initWithNotificationRequest:actionIdentifier:
+ _objc_retainAutoreleasedReturnValue
- ___109-[HDSHSleepApneaRescindedNotificationManager _showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:]_block_invoke.360
- ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.320
- ___block_literal_global.316
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "46F59960-332F-481C-B7DE-7E80973B07BF"
+ "D6770323-332F-481C-B7DE-7E80973B07BF"
+ "[%{public}@] Error attempting to send delivered analytic event: %@"
+ "[%{public}@] Successfully sent delivered analytic event!"
+ "initWithNotificationRequest:actionIdentifier:"
+ "samplesMapWereRemoved:anchor:"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "46F59960-D16A-4E76-B7D1-A1B0BBC73923"
- "D6770323-EBBB-4867-A1A7-99F207C64094"

```
