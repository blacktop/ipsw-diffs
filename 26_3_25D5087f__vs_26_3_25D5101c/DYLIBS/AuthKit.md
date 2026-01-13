## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit`

```diff

-525.326.1.0.0
-  __TEXT.__text: 0x2b0440
+525.326.2.0.0
+  __TEXT.__text: 0x2affc8
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_methlist: 0xe32c
   __TEXT.__const: 0x406f8
-  __TEXT.__cstring: 0xf6b0
-  __TEXT.__oslogstring: 0x12461
-  __TEXT.__gcc_except_tab: 0xa074
+  __TEXT.__cstring: 0xf73e
+  __TEXT.__oslogstring: 0x12417
+  __TEXT.__gcc_except_tab: 0x9f8c
   __TEXT.__dlopen_cstrs: 0x2aa
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x42e0
+  __TEXT.__unwind_info: 0x42c0
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x1d1d
-  __TEXT.__objc_methname: 0x22ef7
+  __TEXT.__objc_methname: 0x22eff
   __TEXT.__objc_methtype: 0x4793
-  __TEXT.__objc_stubs: 0xf520
+  __TEXT.__objc_stubs: 0xf4e0
   __DATA_CONST.__got: 0x940
-  __DATA_CONST.__const: 0x8820
+  __DATA_CONST.__const: 0x8840
   __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208

   __DATA_CONST.__objc_arraydata: 0x2f8
   __AUTH_CONST.__auth_got: 0x648
   __AUTH_CONST.__const: 0xc7b0
-  __AUTH_CONST.__cfstring: 0x10200
+  __AUTH_CONST.__cfstring: 0x10280
   __AUTH_CONST.__objc_const: 0x25fd8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x438

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0465A853-2C1C-38AD-887B-BC8BD8AA2DF8
+  UUID: 7C1AD2E1-589A-3847-8FB1-10BF8A57F394
   Functions: 5622
   Symbols:   15384
-  CStrings:  12005
+  CStrings:  12012
 
Symbols:
+ __64-[AKAccountManager combinedAliasesAndReachableEmailsForAccount:]_block_invoke.223
+ __block_literal_global.218
+ _kAKAnalyticsAdvancedDataProtectionState
+ _kAKAnalyticsEventRequestDeviceArming
+ _kAKAnalyticsEventRequestDeviceArmingStart
+ _kAKAnalyticsEventWebAccessPush
+ _objc_msgSend$initWithEventName:eventCategory:initData:altDSID:
- __64-[AKAccountManager combinedAliasesAndReachableEmailsForAccount:]_block_invoke.224
- __block_literal_global.219
- _objc_msgSend$accountImprovementOptInValueForAccount:
- _objc_msgSend$initWithEventName:eventCategory:initData:
- _objc_msgSend$shouldEnableTelemetryOptIn
Functions:
~ +[AAFAnalyticsEvent(AuthKit) ak_analyticsEventWithEventName:account:error:] : 384 -> 508
~ +[AAFAnalyticsEvent(AuthKit) ak_analyticsEventWithContext:eventName:error:] : 540 -> 640
~ -[AKAccountManager accountAccessTelemetryOptInForAccount:] : 1080 -> 108
~ __AKSafeCast -> -[AKAccountManager accountImprovementOptInForAccount:] : 144 -> 108
~ -[AKAccountManager accountImprovementOptInForAccount:] -> -[AKAccountManager accountImprovementOptInValueForAccount:] : 532 -> 1052
~ -[AKAccountManager accountImprovementOptInValueForAccount:] -> __AKSafeCast : 1052 -> 144
~ -[AKAccountManager identifiableTelemetryAllowedForAccount:] : 152 -> 180
CStrings:
+ "advancedDataProtectionState"
+ "com.apple.authkit.requestDeviceArming"
+ "com.apple.authkit.requestDeviceArmingStart"
+ "com.apple.authkit.webaccess.push"
+ "initWithEventName:eventCategory:initData:altDSID:"
- "Telemetry Opt-In Override Enabled, approving Device Session ID vending..."
- "initWithEventName:eventCategory:initData:"

```
