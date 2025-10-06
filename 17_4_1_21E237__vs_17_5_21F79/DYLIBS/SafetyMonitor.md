## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-900.0.12.0.0
-  __TEXT.__text: 0x59a20
+900.0.25.0.0
+  __TEXT.__text: 0x59cec
   __TEXT.__auth_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x35bc
+  __TEXT.__objc_methlist: 0x35ec
   __TEXT.__const: 0xe70
-  __TEXT.__cstring: 0x729c
+  __TEXT.__cstring: 0x7317
   __TEXT.__swift5_typeref: 0x441
   __TEXT.__swift5_capture: 0xf4
   __TEXT.__constg_swiftt: 0x358

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0x32c8
+  __TEXT.__oslogstring: 0x32f9
   __TEXT.__ustring: 0x8c4
   __TEXT.__gcc_except_tab: 0x7d0
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x1da0
   __TEXT.__eh_frame: 0xa18
   __TEXT.__objc_classname: 0x7d7
-  __TEXT.__objc_methname: 0x9922
-  __TEXT.__objc_methtype: 0x170f
-  __TEXT.__objc_stubs: 0x4920
+  __TEXT.__objc_methname: 0x99e6
+  __TEXT.__objc_methtype: 0x1713
+  __TEXT.__objc_stubs: 0x4940
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x1128
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5a40
-  __DATA_CONST.__objc_selrefs: 0x1a60
+  __DATA_CONST.__objc_const: 0x5aa0
+  __DATA_CONST.__objc_selrefs: 0x1a80
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_classrefs: 0x338
   __DATA_CONST.__objc_superrefs: 0x158
   __AUTH_CONST.__const: 0x7c8
   __AUTH_CONST.__objc_const: 0x1c58
-  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__cfstring: 0x4240
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x920
-  __AUTH.__objc_data: 0xfb8
+  __AUTH.__objc_data: 0xf68
   __AUTH.__data: 0x2b8
-  __DATA.__objc_ivar: 0x304
+  __DATA.__objc_ivar: 0x30c
   __DATA.__data: 0xeb8
-  __DATA.__common: 0x118
+  __DATA.__common: 0x100
   __DATA.__bss: 0x1200
   __DATA_DIRTY.__objc_ivar: 0x184
-  __DATA_DIRTY.__objc_data: 0x740
-  __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x790
+  __DATA_DIRTY.__data: 0xd0
+  __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x400
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BA37E1BF-8BFF-38B2-87F2-31E893AD189B
-  Functions: 1769
-  Symbols:   4622
-  CStrings:  3140
+  UUID: 1A1D4960-D6DC-3F58-8A6F-4C0E59F4B5A7
+  Functions: 1773
+  Symbols:   4633
+  CStrings:  3152
 
Symbols:
+ -[SMTriggerDestinationState currentStatusDate]
+ -[SMTriggerDestinationState initWithSessionIdentifier:currentStatus:currentStatusDate:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:]
+ -[SMTriggerDestinationState originLocation]
+ -[SMTriggerDestinationState setCurrentStatusDate:]
+ -[SMTriggerDestinationState setOriginLocation:]
+ _OBJC_IVAR_$_SMTriggerDestinationState._currentStatusDate
+ _OBJC_IVAR_$_SMTriggerDestinationState._originLocation
+ _objc_msgSend$currentStatusDate
+ _objc_msgSend$initWithSessionIdentifier:currentStatus:currentStatusDate:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:
- -[SMTriggerDestinationState initWithSessionIdentifier:currentStatus:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:]
- _objc_msgSend$initWithSessionIdentifier:currentStatus:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:
CStrings:
+ "\x14$"
+ "%s, currentStatus, %@, currentStatusDate, %@"
+ "%s, currentStatusDate, %@"
+ "-[SMTriggerDestinationState setCurrentStatusDate:]"
+ "@120@0:8@16Q24@32@40@48Q56S64B68@72@80@88d96d104@112"
+ "T@\"CLLocation\",N,V_originLocation"
+ "T@\"NSDate\",&,N,V_currentStatusDate"
+ "__kSMTriggerDestinationStateCurrentStatusDateKey"
+ "_currentStatusDate"
+ "_originLocation"
+ "currentStatusDate"
+ "initWithSessionIdentifier:currentStatus:currentStatusDate:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:"
+ "originLocation"
+ "sessionIdentifier, %@, date, %@, currentStatus, %@, currentStatusDate, %@, lastLockDate, %@, lastUnLockDate, %@, predominantModeOfTransport, %@, numberOfETARetries, %hu, shouldRetryETAQuery, %@, roundTripReminderDate, %@, timeToUpdateStatus, %@, upperBoundEta, %@, mapsExpectedTravelTime, %.1f, remainingDistance, %.1f"
+ "setCurrentStatusDate:"
+ "setOriginLocation:"
- "\x14#"
- "%s, currentStatus, %@"
- "@112@0:8@16Q24@32@40Q48S56B60@64@72@80d88d96@104"
- "initWithSessionIdentifier:currentStatus:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:"
- "sessionIdentifier, %@, date, %@, currentStatus, %@, lastLockDate, %@, lastUnLockDate, %@, predominantModeOfTransport, %@, numberOfETARetries, %hu, shouldRetryETAQuery, %@, roundTripReminderDate, %@, timeToUpdateStatus, %@, upperBoundEta, %@, mapsExpectedTravelTime, %.1f, remainingDistance, %.1f"

```
