## EnergyKit

> `/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit`

```diff

-213.0.0.0.0
-  __TEXT.__text: 0x5c010
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__const: 0xb98
-  __TEXT.__cstring: 0x2612
-  __TEXT.__constg_swiftt: 0x580
-  __TEXT.__swift5_typeref: 0x642
+222.0.0.0.0
+  __TEXT.__text: 0x5a550
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__const: 0xb7c
+  __TEXT.__cstring: 0x24c2
+  __TEXT.__swift5_typeref: 0x60a
+  __TEXT.__constg_swiftt: 0x564
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x5b0
-  __TEXT.__swift5_fieldmd: 0x4f4
-  __TEXT.__swift5_types: 0x40
-  __TEXT.__swift5_capture: 0xb84
-  __TEXT.__oslogstring: 0x108b
+  __TEXT.__swift5_reflstr: 0x5dc
+  __TEXT.__swift5_fieldmd: 0x4f0
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__oslogstring: 0xf9b
   __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_capture: 0x8e4
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x68
-  __TEXT.__unwind_info: 0x1520
-  __TEXT.__eh_frame: 0x4410
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__unwind_info: 0x1690
+  __TEXT.__eh_frame: 0x3f58
   __TEXT.__objc_classname: 0x9
   __TEXT.__objc_methname: 0xfcb
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x640
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__auth_got: 0x8f8
   __AUTH_CONST.__auth_ptr: 0x1b0
-  __AUTH_CONST.__const: 0x1c28
+  __AUTH_CONST.__const: 0x1508
   __AUTH_CONST.__objc_const: 0xe50
   __AUTH.__objc_data: 0x4a0
-  __AUTH.__data: 0x490
-  __DATA.__data: 0xb10
-  __DATA.__bss: 0xd00
+  __AUTH.__data: 0x218
+  __DATA.__data: 0x988
+  __DATA.__bss: 0xc00
   __DATA.__common: 0x80
-  __DATA_DIRTY.__data: 0x2f0
+  __DATA_DIRTY.__data: 0x5e0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
-  Functions: 1306
-  Symbols:   186
-  CStrings:  392
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1424
+  Symbols:   189
+  CStrings:  382
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- __swiftEmptySetSingleton
- _objc_retain_x26
- _swift_allocBox
- _swift_setDeallocating
CStrings:
+ "Failed to create subscription. Site ID is empty."
+ "Failed to get site. Site ID is empty."
+ "Failed to refresh peaks. Site ID is empty."
+ "Failed to register site. Site ID is empty."
+ "Failed to update fields. Site ID is empty."
+ "Failed to update location. Site ID is empty."
+ "Failed to update state. Site ID is empty."
+ "Failed to update subscription. Site ID is empty."
+ "Failed to update timezone. Site ID is empty."
+ "historicalEnergyUsageInterval(interval:start:end:timezone:utilityID:subscriptionID:)"
- "%!s(MISSING) %!s(MISSING) snapshot & so the interval that contains %!s(MISSING) begins on %!s(MISSING)"
- "%!s(MISSING) %!s(MISSING) to %!s(MISSING) is %!l(MISSING)d days"
- "%!s(MISSING) (%!s(MISSING)) found %!l(MISSING)d usages in %!s(MISSING): %!s(MISSING)"
- "%!s(MISSING) (%!s(MISSING)) returning %!f(MISSING) imports in %!l(MISSING)d days, starting on %!s(MISSING)"
- "%!s(MISSING) (%!s(MISSING)) the interval with %!s(MISSING) has %!f(MISSING) total exports %!f(MISSING) net exports for %!l(MISSING)d days of data = %!f(MISSING) average exports"
- "%!s(MISSING) (%!s(MISSING)) the interval with %!s(MISSING) has %!f(MISSING) total imports %!f(MISSING) net imports for %!l(MISSING)d days of data = %!f(MISSING) average imports"
- "%!s(MISSING) allocated seats %!s(MISSING) total %!l(MISSING)d"
- "%!s(MISSING) initial seats %!s(MISSING) remaining %!l(MISSING)d"
- "%!s(MISSING) invalid historical interval value given: %!s(MISSING)"
- "%!s(MISSING) invalid num of days in month. year:%!l(MISSING)d, month:%!l(MISSING)d"
- "%!s(MISSING) sorted fractional seats %!s(MISSING)"
- "%!s(MISSING) the interval that contains %!s(MISSING): %!s(MISSING)"
- "beginningOfInterval(for:interval:in:)"
- "dailyAverageNetExportsForInterval(starting:)"
- "dailyAverageNetImportsForInterval(starting:)"
- "historicalEnergyUsageInterval(interval:start:end:timezone:addingComponent:utilityID:subscriptionID:)"
- "importPricingPeriodsForInterval(starting:)"
- "intervalDateRangeContaining(startDate:interval:in:)"
- "numDaysIn(usage:)"
- "totalImportsForDateRange(_:)"

```
