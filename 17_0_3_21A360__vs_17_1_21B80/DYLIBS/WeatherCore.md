## WeatherCore

> `/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore`

```diff

-469.4.0.0.0
-  __TEXT.__text: 0x179c54
-  __TEXT.__auth_stubs: 0x3a90
+484.0.0.0.0
+  __TEXT.__text: 0x17a770
+  __TEXT.__auth_stubs: 0x3ab0
   __TEXT.__objc_methlist: 0x554
-  __TEXT.__const: 0x114a4
-  __TEXT.__cstring: 0x1385c
+  __TEXT.__const: 0x115d4
+  __TEXT.__cstring: 0x1387c
   __TEXT.__oslogstring: 0x43d
-  __TEXT.__swift5_typeref: 0x4d77
-  __TEXT.__swift5_fieldmd: 0x4b30
-  __TEXT.__constg_swiftt: 0x427c
-  __TEXT.__swift5_reflstr: 0x4103
+  __TEXT.__swift5_typeref: 0x4d87
+  __TEXT.__swift5_fieldmd: 0x4b7c
+  __TEXT.__constg_swiftt: 0x42a0
+  __TEXT.__swift5_reflstr: 0x4113
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0x7e8
+  __TEXT.__swift5_assocty: 0x800
   __TEXT.__swift5_protos: 0x104
-  __TEXT.__swift5_proto: 0x10c8
-  __TEXT.__swift5_types: 0x4d8
-  __TEXT.__swift5_capture: 0xe44
+  __TEXT.__swift5_proto: 0x10dc
+  __TEXT.__swift5_types: 0x4dc
+  __TEXT.__swift5_capture: 0xe6c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6d94
-  __TEXT.__eh_frame: 0x74c8
+  __TEXT.__unwind_info: 0x6e04
+  __TEXT.__eh_frame: 0x74e0
   __TEXT.__objc_classname: 0x10b
   __TEXT.__objc_methname: 0x51d8
   __TEXT.__objc_methtype: 0xc8d

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x83e8
+  __DATA_CONST.__objc_const: 0x8428
   __DATA_CONST.__objc_selrefs: 0x958
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__const: 0xecc0
+  __AUTH_CONST.__const: 0xee50
   __AUTH_CONST.__objc_const: 0x5e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x4a8
-  __AUTH_CONST.__auth_got: 0x1d50
+  __AUTH_CONST.__auth_got: 0x1d60
   __AUTH.__data: 0xdd8
   __AUTH.__objc_data: 0x210
   __DATA.__objc_protorefs: 0x38

   __DATA.__objc_superrefs: 0x30
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0xd0
-  __DATA.__data: 0x3610
-  __DATA.__bss: 0x12560
+  __DATA.__data: 0x36a8
+  __DATA.__bss: 0x127e0
   __DATA.__common: 0x40
   __DATA_DIRTY.__const: 0xa0
   __DATA_DIRTY.__objc_data: 0x850
-  __DATA_DIRTY.__data: 0x67c8
+  __DATA_DIRTY.__data: 0x67d8
   __DATA_DIRTY.__bss: 0xcfe0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12353
-  Symbols:   7048
-  CStrings:  2548
+  Functions: 12386
+  Symbols:   7054
+  CStrings:  2550
 
Symbols:
+ _associated conformance 11WeatherCore20ReverseGeocodeSourceOSHAASQ
+ _block_copy_helper.28
+ _block_copy_helper.34
+ _block_copy_helper.74
+ _block_copy_helper.80
+ _block_copy_helper.86
+ _block_copy_helper.92
+ _block_copy_helper.98
+ _block_descriptor.100
+ _block_descriptor.30
+ _block_descriptor.36
+ _block_descriptor.76
+ _block_descriptor.82
+ _block_descriptor.88
+ _block_descriptor.94
+ _block_destroy_helper.29
+ _block_destroy_helper.35
+ _block_destroy_helper.75
+ _block_destroy_helper.81
+ _block_destroy_helper.87
+ _block_destroy_helper.93
+ _block_destroy_helper.99
+ _dispatch_sync
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic Ig_
+ _symbolic So24GEOApplicationAuditTokenCSg
+ _symbolic _____ 11WeatherCore20ReverseGeocodeSourceO
- _block_copy_helper.13
- _block_copy_helper.56
- _block_copy_helper.71
- _block_copy_helper.77
- _block_copy_helper.83
- _block_copy_helper.89
- _block_descriptor.15
- _block_descriptor.58
- _block_descriptor.73
- _block_descriptor.79
- _block_descriptor.85
- _block_descriptor.91
- _block_destroy_helper.14
- _block_destroy_helper.57
- _block_destroy_helper.72
- _block_destroy_helper.78
- _block_destroy_helper.84
- _block_destroy_helper.90
- _symbolic So24GEOApplicationAuditTokenCSgSg
CStrings:
+ "Failed to reverse geocode searchQuery. searchQuery=%{sensitive,mask.hash}s, error=%{public}s"
+ "Finding displayRegion. uniqueID=%{private,mask.hash}s, name=%{private,mask.hash}s, searchQuery=%{sensitive,mask.hash}s, searchTitle=%s"
+ "`GEOMapItem` missing while reverse geocoding. searchQuery=%{sensitive,mask.hash}s"
+ "auditToken"
+ "clientSide"
+ "serverSide"
+ "serverSideRegionGeoJSONLock"
- "$__lazy_storage_$_auditToken"
- "$__lazy_storage_$_locationManager"
- "Failed to reverse geocode searchQuery. searchQuery=%{public}s, error=%{public}s"
- "Finding displayRegion. uniqueID=%{private,mask.hash}s, name=%{private,mask.hash}s, searchQuery=%s, searchTitle=%s"
- "`GEOMapItem` missing while reverse geocoding. searchQuery=%{public}s"

```
