## RegulatoryDomain

> `/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain`

```diff

-61.0.1.0.0
-  __TEXT.__text: 0x10be8
+63.0.0.0.0
+  __TEXT.__text: 0x11374
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x5d4
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x977
+  __TEXT.__objc_methlist: 0x5f4
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x9ad
   __TEXT.__swift5_typeref: 0x224
-  __TEXT.__oslogstring: 0x2020
+  __TEXT.__oslogstring: 0x234c
   __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_reflstr: 0x2d

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x428
   __TEXT.__eh_frame: 0x4e8
   __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0xfa8
-  __TEXT.__objc_methtype: 0x2b0
-  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_methname: 0x1039
+  __TEXT.__objc_methtype: 0x2b3
+  __TEXT.__objc_stubs: 0xe60
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x3b8
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x708
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x2c8
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x728
+  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH.__objc_data: 0xb0
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x44
+  __DATA.__data: 0x238
   __DATA.__common: 0x18
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x2f0
-  __DATA_DIRTY.__data: 0xc0
+  __DATA_DIRTY.__objc_data: 0x288
+  __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A102D0E4-29AC-3623-9F0F-5EC52B9FA9FD
-  Functions: 272
-  Symbols:   201
-  CStrings:  448
+  UUID: 50B2D55F-8608-321C-AB61-F9BEDA825439
+  Functions: 279
+  Symbols:   203
+  CStrings:  467
 
Symbols:
+ _RDUpdateCountryCodesFromGeoIP
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _kRDPriorityGEOIP
+ _objc_retain_x28
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_release_n
CStrings:
+ "@92@0:8@16@24@32@40@48@56@64@72B80@84"
+ "Except for unit tests, countryFromGeoIP should never be called from outside of countryd"
+ "GeoIP"
+ "LocalCountryCodesGeoIP"
+ "Unhandled priority value encountered during comparison. Please file a radar to RegulatoryDomain"
+ "Unhandled self-priority value encountered during comparison. Please file a radar to RegulatoryDomain"
+ "_countriesFromGeoIP"
+ "geoIPCC"
+ "initWithCountryCodeFromLocation:fromServingCell:fromNearbyCell:fromWiFi:fromGeoIP:localEstimates:combinedEstimate:lastKnownCombinedEstimate:locationLocalEstimateInDisputedArea:peerEstimates:"
+ "numberWithUnsignedInt:"
+ "q"
+ "setCountriesFromGeoIP:"
+ "setCountriesFromGeoIP:forUnitTest:"
+ "setCountriesFromGeoIPForUnitTest:"
+ "{\"msg%{public}.0s\":\"CACHE: Geo IP country code changing\", \"from\":%{public, location:escape_only}@, \"to\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"Except for unit tests, countryFromGeoIP should never be called from outside of countryd\"}"
+ "{\"msg%{public}.0s\":\"Unhandled priority value encountered during comparison. Please file a radar to RegulatoryDomain\", \"prio\":%{public}d}"
+ "{\"msg%{public}.0s\":\"Unhandled self-priority value encountered during comparison. Please file a radar to RegulatoryDomain\", \"prio\":%{public}d}"
+ "{location CC: %@,\nnearbyCell CC: %@,\ntelephony CC: %@,\nwifi AP CC: %@,\nGeo IP CC: %@,\nlocalOnlyEstimate: %@,\ncombinedEstimate: %@, lastKnown: %@, peerEstimates: %@}"
- "@84@0:8@16@24@32@40@48@56@64B72@76"
- "initWithCountryCodeFromLocation:fromServingCell:fromNearbyCell:fromWiFi:localEstimates:combinedEstimate:lastKnownCombinedEstimate:locationLocalEstimateInDisputedArea:peerEstimates:"
- "{location CC: %@, nearbyCell CC: %@, telephony CC: %@, wifi AP CC: %@, localOnlyEstimate: %@, combinedEstimate: %@, lastKnown: %@, peerEstimates: %@}"

```
