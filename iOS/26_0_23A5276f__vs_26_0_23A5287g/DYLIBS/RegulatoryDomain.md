## RegulatoryDomain

> `/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain`

```diff

-65.0.0.0.0
-  __TEXT.__text: 0x1127c
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x5dc
+66.0.0.0.0
+  __TEXT.__text: 0x11630
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x9ad
+  __TEXT.__cstring: 0x9d6
   __TEXT.__swift5_typeref: 0x224
-  __TEXT.__oslogstring: 0x234c
+  __TEXT.__oslogstring: 0x255c
   __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_reflstr: 0x2d
-  __TEXT.__swift5_capture: 0x90
+  __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x34

   __TEXT.__unwind_info: 0x428
   __TEXT.__eh_frame: 0x4e8
   __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0x1003
+  __TEXT.__objc_methname: 0x1080
   __TEXT.__objc_methtype: 0x2b3
-  __TEXT.__objc_stubs: 0xe40
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x250
+  __TEXT.__objc_stubs: 0xea0
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b8
+  __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__const: 0x3c8
+  __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x728
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xb0

   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x288
   __DATA_DIRTY.__data: 0x98
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3783F8CF-0143-3D2E-8C16-7B3EF45AFB80
-  Functions: 277
-  Symbols:   199
-  CStrings:  464
+  UUID: 16FFD1B5-B7E2-3949-A897-EB9E575593C4
+  Functions: 279
+  Symbols:   209
+  CStrings:  477
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFErrorGetCode
+ _CFErrorGetDomain
+ _CFGetTypeID
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _kCFAllocatorDefault
+ _mach_task_self_
+ _task_info
CStrings:
+ "-[RDCachedData localEstimatesForPriority:]"
+ "LocalCountryEstimatesGeoIP"
+ "LocalCountryEstimatesLocation"
+ "LocalCountryEstimatesNearbyCells"
+ "LocalCountryEstimatesServingCell"
+ "LocalCountryEstimatesWiFiAPs"
+ "SecTaskCopyValueForEntitlement failed with error"
+ "SecTaskCreateWithAuditToken failed"
+ "_estimatesFromGeoIP"
+ "_estimatesFromLocation"
+ "_estimatesFromNearbyCells"
+ "_estimatesFromServingCell"
+ "_estimatesFromWiFiAPs"
+ "arrayWithCapacity:"
+ "attempting to access montara estimates without proper entitlement"
+ "com.apple.RegulatoryDomain.montara"
+ "enumerateObjectsUsingBlock:"
+ "estimateArrayFromStrings:withPriority:andTimestamp:disputed:"
+ "estimatesForMontara"
+ "getGeoIPLocalEstimates"
+ "localEstimatesForPriority:"
+ "v32@?0@8Q16^B24"
+ "{\"msg%{public}.0s\":\"RegulatoryDomain #Montara estimates\", \"montara\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"SecTaskCopyValueForEntitlement failed with error\", \"err\":%{public, location:escape_only}@, \"code\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"SecTaskCreateWithAuditToken failed\"}"
+ "{\"msg%{public}.0s\":\"attempting to access montara estimates without proper entitlement\"}"
- "-[RDCachedData countryCodesForPriority:]"
- "LocalCountryCodesGeoIP"
- "LocalCountryCodesLocation"
- "LocalCountryCodesNearbyCells"
- "LocalCountryCodesServingCell"
- "LocalCountryCodesWiFiAPs"
- "_countriesFromGeoIP"
- "_countriesFromLocation"
- "_countriesFromNearbyCells"
- "_countriesFromServingCell"
- "_countriesFromWiFiAPs"
- "countryCodesForPriority:"
- "q24@?0@\"NSString\"8@\"NSString\"16"
- "sortedArrayUsingComparator:"

```
