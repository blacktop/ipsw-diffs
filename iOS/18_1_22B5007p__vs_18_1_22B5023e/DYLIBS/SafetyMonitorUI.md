## SafetyMonitorUI

> `/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI`

```diff

-962.0.0.0.0
-  __TEXT.__text: 0x16dcf4
-  __TEXT.__auth_stubs: 0x2e70
+967.0.0.0.0
+  __TEXT.__text: 0x16bed4
+  __TEXT.__auth_stubs: 0x2ed0
   __TEXT.__objc_methlist: 0x624
   __TEXT.__const: 0x81b8
-  __TEXT.__cstring: 0xc59f
-  __TEXT.__swift5_typeref: 0x1b8ba
-  __TEXT.__swift5_capture: 0x15b8
+  __TEXT.__cstring: 0xc95f
+  __TEXT.__swift5_typeref: 0x1b6ea
+  __TEXT.__swift5_capture: 0x16c0
   __TEXT.__swift5_reflstr: 0x2371
   __TEXT.__swift5_assocty: 0x990
   __TEXT.__constg_swiftt: 0x3530
-  __TEXT.__swift5_fieldmd: 0x1e50
+  __TEXT.__swift5_fieldmd: 0x1e44
   __TEXT.__swift5_builtin: 0x190
-  __TEXT.__oslogstring: 0x70a6
+  __TEXT.__oslogstring: 0x7116
   __TEXT.__swift5_proto: 0x288
   __TEXT.__swift5_types: 0x258
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3da0
-  __TEXT.__eh_frame: 0x1d08
+  __TEXT.__unwind_info: 0x3df8
+  __TEXT.__eh_frame: 0x1c98
   __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0x2fbd
+  __TEXT.__objc_methname: 0x30d6
   __TEXT.__objc_methtype: 0x7bd
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__const: 0x778
+  __DATA_CONST.__got: 0xc30
+  __DATA_CONST.__const: 0x7d8
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd80
+  __DATA_CONST.__objc_selrefs: 0xdc8
   __DATA_CONST.__objc_protorefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1738
-  __AUTH_CONST.__auth_ptr: 0x15f0
-  __AUTH_CONST.__const: 0x6268
+  __AUTH_CONST.__auth_got: 0x1768
+  __AUTH_CONST.__auth_ptr: 0x1560
+  __AUTH_CONST.__const: 0x65b0
   __AUTH_CONST.__objc_const: 0x33d8
   __AUTH.__objc_data: 0x2220
-  __AUTH.__data: 0x25c0
-  __DATA.__data: 0x4790
+  __AUTH.__data: 0x25b8
+  __DATA.__data: 0x47b8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x5c90
-  __DATA.__common: 0x930
+  __DATA.__common: 0x950
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6413
-  Symbols:   677
-  CStrings:  1962
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 6473
+  Symbols:   707
+  CStrings:  1988
 
Symbols:
+ _OBJC_CLASS_$_CNContactStore
+ _SMSessionUserDetailsAnalyticsEvent
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "%!s(MISSING), %!s(MISSING), sending analytics event perSessionUserDetails, %!s(MISSING)"
+ "%!s(MISSING), %!s(MISSING): contacts access not authorized"
+ "Check\u00a0In requires a cellular connection to keep up with your progress. If Check\u00a0In cannot determine that you’ve arrived by your original ETA, your friend will be notified."
+ "Check\u00a0In requires a cellular connection to respond when prompted. If a network connection is not available, your friend will be notified."
+ "Includes all data from Limited plus route traveled and location of last iPhone unlock."
+ "Includes current location, route traveled, location of last iPhone unlock, and details about battery and network signal."
+ "Let a Friend Know You’ve Arrived with Check\u00a0In"
+ "Let a Friend Know You’ve Finished Your Workout with Check\u00a0In"
+ "Warning for initiator when cellular is disabled during Destination Check\u00a0In."
+ "Warning for initiator when cellular is disabled during non Destination Check\u00a0In."
+ "Watch Workout - RTL"
+ "analyticsSendPerSessionUserDetailsEvent(queue:sessionConfiguration:)"
+ "analyticsSendSessionStartEntryEvent(queue:sessionConfiguration:)"
+ "antenna.radiowaves.left.and.right.slash.circle.fill"
+ "authorizationStatusForEntityType:"
+ "dateFromString:"
+ "destinationLocationTypeEnum"
+ "fetchNumEmergencyRecipientsWithReceiverHandles:handler:"
+ "fetchNumFavoriteRecipientsWithReceiverHandles:handler:"
+ "fetchNumiCloudFamilyRecipientsWithReceiverHandles:handler:"
+ "isAnomalyState"
+ "isMonitoringState"
+ "numRecipientsInEmergency"
+ "numRecipientsInFavorites"
+ "numRecipientsIniCloudFamily"
+ "sessionStartTimeOfDay"
+ "setDateFormat:"
+ "setTimeZone:"
+ "v24@?0Q8@\"NSError\"16"
+ "yyyy-MM-dd HH:mm:ss"
- "Cellular Data Required"
- "Includes all data from Limited plus route traveled and location of last iPhone unlock and Apple Watch removal."
- "Includes current location, route traveled, location of last iPhone unlock, location of Apple Watch removal, and details about battery and network signal."
- "analyticsSendSessionStartEntryEvent(sessionConfiguration:)"

```
