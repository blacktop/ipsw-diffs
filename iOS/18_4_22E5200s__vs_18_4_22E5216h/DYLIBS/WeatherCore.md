## WeatherCore

> `/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore`

```diff

-860.1.0.0.0
-  __TEXT.__text: 0x1fd9dc
-  __TEXT.__auth_stubs: 0x4c80
+864.0.0.0.0
+  __TEXT.__text: 0x20db74
+  __TEXT.__auth_stubs: 0x4c10
   __TEXT.__objc_methlist: 0x1374
-  __TEXT.__const: 0x1b3b0
-  __TEXT.__cstring: 0xe15a
-  __TEXT.__oslogstring: 0xd447
-  __TEXT.__swift5_typeref: 0x7f6d
-  __TEXT.__swift5_fieldmd: 0x6a30
-  __TEXT.__constg_swiftt: 0x6210
-  __TEXT.__swift5_reflstr: 0x62f1
+  __TEXT.__const: 0x1a5e0
+  __TEXT.__cstring: 0xe05a
+  __TEXT.__oslogstring: 0xd407
+  __TEXT.__swift5_typeref: 0x7b23
+  __TEXT.__swift5_fieldmd: 0x686c
+  __TEXT.__constg_swiftt: 0x618c
+  __TEXT.__swift5_reflstr: 0x60f1
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_assocty: 0x1180
+  __TEXT.__swift5_assocty: 0xfc8
   __TEXT.__swift5_protos: 0x178
-  __TEXT.__swift5_proto: 0x18f0
-  __TEXT.__swift5_types: 0x720
-  __TEXT.__swift_as_entry: 0x244
-  __TEXT.__swift_as_ret: 0x1f0
+  __TEXT.__swift5_proto: 0x180c
+  __TEXT.__swift5_types: 0x70c
+  __TEXT.__swift_as_entry: 0x238
+  __TEXT.__swift_as_ret: 0x1e4
   __TEXT.__swift5_capture: 0x21bc
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x8cd8
-  __TEXT.__eh_frame: 0xb8c0
+  __TEXT.__unwind_info: 0x8918
+  __TEXT.__eh_frame: 0xb9d0
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methname: 0x59b9
   __TEXT.__objc_methtype: 0xd4c
   __TEXT.__objc_stubs: 0xd20
-  __DATA_CONST.__got: 0xf18
-  __DATA_CONST.__const: 0x630
+  __DATA_CONST.__got: 0xf08
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x2648
-  __AUTH_CONST.__auth_ptr: 0x1f98
-  __AUTH_CONST.__const: 0x11ea8
+  __AUTH_CONST.__auth_got: 0x2610
+  __AUTH_CONST.__auth_ptr: 0x1f70
+  __AUTH_CONST.__const: 0x119d0
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x9300
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH.__objc_data: 0x2f0
   __AUTH.__data: 0x13a8
   __DATA.__objc_ivar: 0x48
-  __DATA.__data: 0x3770
-  __DATA.__bss: 0x1bbd0
+  __DATA.__data: 0x34c8
+  __DATA.__bss: 0x1a3d0
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0xa70
-  __DATA_DIRTY.__data: 0x8af8
-  __DATA_DIRTY.__bss: 0x129c0
+  __DATA_DIRTY.__data: 0x8a78
+  __DATA_DIRTY.__bss: 0x12540
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14820
-  Symbols:   3643
-  CStrings:  3258
+  Functions: 14554
+  Symbols:   3733
+  CStrings:  3244
 
Symbols:
+ _objc_retain_x13
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "Invalid URL!"
+ "Local store was changed externally - committing to the remote. ExternallyChangedLocalLocations=%{private,mask.hash}s, oldLocationDataModels=%{private,mask.hash}s, reconciledLocations=%{private,mask.hash}s"
- "Current Temperature"
- "Feels Like Temperature"
- "High Temperature"
- "Local store was changed externally (by the watch) - committing to the remote. ExternallyChangedLocalLocations=%{private,mask.hash}s, oldLocationDataModels=%{private,mask.hash}s, reconciledLocations=%{private,mask.hash}s"
- "LocationMapEntity: Could not determine map kind!"
- "Next-Hour Precipitation"
- "Sunrise and Sunset"
- "Weather Map Kind"
- "averages"
- "conditions"
- "humidity"
- "moon"
- "nhp"
- "sunriseSunset"
- "uvIndex"
- "visibility"

```
