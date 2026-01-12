## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.326.1.0.0
-  __TEXT.__text: 0x185eac
+525.326.2.0.0
+  __TEXT.__text: 0x185a34
   __TEXT.__auth_stubs: 0xc30
   __TEXT.__objc_methlist: 0xe51c
   __TEXT.__const: 0x69f8
-  __TEXT.__cstring: 0xfcde
-  __TEXT.__gcc_except_tab: 0xa134
-  __TEXT.__oslogstring: 0x12a8b
+  __TEXT.__cstring: 0xfd6c
+  __TEXT.__gcc_except_tab: 0xa04c
+  __TEXT.__oslogstring: 0x12a41
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x42a0
+  __TEXT.__unwind_info: 0x4280
   __TEXT.__objc_classname: 0x1d7c
-  __TEXT.__objc_methname: 0x23788
+  __TEXT.__objc_methname: 0x23790
   __TEXT.__objc_methtype: 0x47c0
-  __TEXT.__objc_stubs: 0xffc0
+  __TEXT.__objc_stubs: 0xff80
   __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0xa358
+  __DATA_CONST.__const: 0xa378
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208

   __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x10540
+  __AUTH_CONST.__cfstring: 0x105c0
   __AUTH_CONST.__objc_const: 0x26718
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0211A267-CA37-3286-A413-5C38B364E484
+  UUID: 2EC72152-A491-3DB1-AEF6-CB1BE9528CB5
   Functions: 5549
   Symbols:   20989
-  CStrings:  12191
+  CStrings:  12198
 
Symbols:
+ ___block_literal_global.216
+ _kAKAnalyticsAdvancedDataProtectionState
+ _kAKAnalyticsEventRequestDeviceArming
+ _kAKAnalyticsEventRequestDeviceArmingStart
+ _kAKAnalyticsEventWebAccessPush
+ _objc_msgSend$initWithEventName:eventCategory:initData:altDSID:
- ___block_literal_global.217
- _objc_msgSend$accountImprovementOptInValueForAccount:
- _objc_msgSend$initWithEventName:eventCategory:initData:
- _objc_msgSend$shouldEnableTelemetryOptIn
Functions:
~ -[AKAccountManager accountAccessTelemetryOptInForAccount:] : 1080 -> 108
~ __AKSafeCast -> -[AKAccountManager accountImprovementOptInForAccount:] : 144 -> 108
~ -[AKAccountManager accountImprovementOptInForAccount:] -> -[AKAccountManager accountImprovementOptInValueForAccount:] : 532 -> 1052
~ -[AKAccountManager accountImprovementOptInValueForAccount:] -> __AKSafeCast : 1052 -> 144
~ -[AKAccountManager identifiableTelemetryAllowedForAccount:] : 152 -> 180
~ +[AAFAnalyticsEvent(AuthKit) ak_analyticsEventWithEventName:account:error:] : 384 -> 508
~ +[AAFAnalyticsEvent(AuthKit) ak_analyticsEventWithContext:eventName:error:] : 540 -> 640
CStrings:
+ "advancedDataProtectionState"
+ "com.apple.authkit.requestDeviceArming"
+ "com.apple.authkit.requestDeviceArmingStart"
+ "com.apple.authkit.webaccess.push"
+ "initWithEventName:eventCategory:initData:altDSID:"
- "Telemetry Opt-In Override Enabled, approving Device Session ID vending..."
- "initWithEventName:eventCategory:initData:"

```
