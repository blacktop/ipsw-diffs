## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1576.200.62.0.0
-  __TEXT.__text: 0x16e488
+1576.200.75.0.0
+  __TEXT.__text: 0x16e57c
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_methlist: 0x1a2e0
-  __TEXT.__cstring: 0x13578
+  __TEXT.__objc_methlist: 0x1a2d0
+  __TEXT.__cstring: 0x13568
   __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x12582
+  __TEXT.__oslogstring: 0x12592
   __TEXT.__gcc_except_tab: 0x1974
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5df8
+  __TEXT.__unwind_info: 0x5df0
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x274f
-  __TEXT.__objc_methname: 0x3c5ab
-  __TEXT.__objc_methtype: 0x7f80
-  __TEXT.__objc_stubs: 0x20f00
+  __TEXT.__objc_methname: 0x3c5b5
+  __TEXT.__objc_methtype: 0x7f83
+  __TEXT.__objc_stubs: 0x20f20
   __DATA_CONST.__got: 0xe60
   __DATA_CONST.__const: 0x3678
   __DATA_CONST.__objc_classlist: 0x830

   __AUTH_CONST.__auth_got: 0x11d8
   __AUTH_CONST.__const: 0x31a8
   __AUTH_CONST.__cfstring: 0x11c80
-  __AUTH_CONST.__objc_const: 0x28390
+  __AUTH_CONST.__objc_const: 0x28368
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EFFCC9F3-6BD3-3850-9BE8-0D12A81F5495
+  UUID: 1EF0E029-17FD-3679-BDE0-855BAA25BAFE
   Functions: 10062
   Symbols:   30072
-  CStrings:  16499
+  CStrings:  16498
 
Symbols:
+ -[TUCallCenter _isCallingAvailableOnSecondaryDeviceWithRelayCallingAvailability:isProviderAvailable:isRelayAllowed:isEmergency:supportsBasebandCalling:shouldUseRelay:isTelephonyProvider:deviceType:]
+ _TURemoveIDSAvailabilityListener
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.660
+ __OBJC_$_PROP_LIST_TUFeatureFlags.664
+ ___34-[TUCallCenter answerWithRequest:]_block_invoke.247
+ ___56-[TUCallCenter joinConversationWithConversationRequest:]_block_invoke.260
+ ___block_literal_global.262
+ ___block_literal_global.264
+ _objc_msgSend$_isCallingAvailableOnSecondaryDeviceWithRelayCallingAvailability:isProviderAvailable:isRelayAllowed:isEmergency:supportsBasebandCalling:shouldUseRelay:isTelephonyProvider:deviceType:
+ _objc_msgSend$removeListenerID:forService:
- -[TUCallCenter _isCallingAvailableOnSecondaryDeviceWithRelayCallingAvailability:isProviderAvailable:isRelayAllowed:isEmergency:supportsBasebandCalling:shouldUseRelay:isTelephonyProvider:]
- -[TUFeatureFlags unknownInitiatorReportEnabled]
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.663
- __OBJC_$_PROP_LIST_TUFeatureFlags.667
- ___34-[TUCallCenter answerWithRequest:]_block_invoke.245
- ___56-[TUCallCenter joinConversationWithConversationRequest:]_block_invoke.259
- ___block_literal_global.261
- ___block_literal_global.263
- _objc_msgSend$_isCallingAvailableOnSecondaryDeviceWithRelayCallingAvailability:isProviderAvailable:isRelayAllowed:isEmergency:supportsBasebandCalling:shouldUseRelay:isTelephonyProvider:
CStrings:
+ "B56@0:8i16B20B24B28B32^B36B44q48"
+ "_isCallingAvailableOnSecondaryDeviceWithRelayCallingAvailability:isProviderAvailable:isRelayAllowed:isEmergency:supportsBasebandCalling:shouldUseRelay:isTelephonyProvider:deviceType:"
+ "relayCallingAvailability: %d isProviderAvailable: %@ isRelayAllowed: %@ isEmergency: %@ supportsBasebandCalling: %@, callsHostedElsewhere count: %d, isTelephonyProvider: %@ deviceType: %ld"
+ "removeListenerID:forService:"
- "B48@0:8i16B20B24B28B32^B36B44"
- "UnknownInitiatorReport"
- "_isCallingAvailableOnSecondaryDeviceWithRelayCallingAvailability:isProviderAvailable:isRelayAllowed:isEmergency:supportsBasebandCalling:shouldUseRelay:isTelephonyProvider:"
- "relayCallingAvailability: %d isProviderAvailable: %@ isRelayAllowed: %@ isEmergency: %@ supportsBasebandCalling: %@, callsHostedElsewhere count: %d, isTelephonyProvider: %@"
- "unknownInitiatorReportEnabled"

```
