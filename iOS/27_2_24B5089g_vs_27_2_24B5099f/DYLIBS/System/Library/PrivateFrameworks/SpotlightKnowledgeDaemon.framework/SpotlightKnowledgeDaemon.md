## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2465.1.3.0.0
-  __TEXT.__text: 0x492098
-  __TEXT.__objc_methlist: 0x9618
-  __TEXT.__const: 0x17a68
+2465.1.7.0.0
+  __TEXT.__text: 0x491eac
+  __TEXT.__objc_methlist: 0x9628
+  __TEXT.__const: 0x17a78
   __TEXT.__oslogstring: 0x12ace
-  __TEXT.__cstring: 0x162f3
-  __TEXT.__gcc_except_tab: 0x5c6c
+  __TEXT.__cstring: 0x162c3
+  __TEXT.__gcc_except_tab: 0x5c64
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0xee46
   __TEXT.__constg_swiftt: 0x9188

   __TEXT.__swift5_assocty: 0x13e0
   __TEXT.__swift5_proto: 0x10c4
   __TEXT.__swift5_types: 0x8f4
-  __TEXT.__swift5_capture: 0x3900
+  __TEXT.__swift5_capture: 0x38f0
   __TEXT.__swift_as_entry: 0x498
   __TEXT.__swift_as_ret: 0x4e0
   __TEXT.__swift_as_cont: 0x57c
   __TEXT.__swift5_protos: 0x284
   __TEXT.__swift5_mpenum: 0x94
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xf770
-  __TEXT.__eh_frame: 0x158c0
+  __TEXT.__unwind_info: 0xf7b8
+  __TEXT.__eh_frame: 0x15980
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e80
+  __DATA_CONST.__objc_selrefs: 0x5e88
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x4d0
-  __DATA_CONST.__objc_arraydata: 0xa30
+  __DATA_CONST.__objc_arraydata: 0xa20
   __DATA_CONST.__got: 0x2350
-  __AUTH_CONST.__const: 0x19778
-  __AUTH_CONST.__cfstring: 0x9400
-  __AUTH_CONST.__objc_const: 0x18508
+  __AUTH_CONST.__const: 0x19750
+  __AUTH_CONST.__cfstring: 0x93c0
+  __AUTH_CONST.__objc_const: 0x18528
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x37f0
+  __AUTH_CONST.__auth_got: 0x37f8
   __AUTH.__objc_data: 0x1648
   __AUTH.__data: 0x2478
-  __DATA.__objc_ivar: 0xb90
+  __DATA.__objc_ivar: 0xb94
   __DATA.__data: 0x3560
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x3f50
-  __DATA_DIRTY.__data: 0xd608
+  __DATA_DIRTY.__data: 0xd5e8
   __DATA_DIRTY.__bss: 0x99f0
   __DATA_DIRTY.__common: 0x408
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16839
-  Symbols:   11652
-  CStrings:  3765
+  Functions: 16850
+  Symbols:   11654
+  CStrings:  3763
 
Symbols:
+ -[SKDLocationProcessor isRecentRecord:]
+ -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:enablePIR:entityBlock:rangeBlock:errorBlock:]
+ -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:enablePIR:entityCategories:entityBlock:rangeBlock:errorBlock:]
+ -[SKGDataDetector enumerateDetectedLocationsInString:locale:enablePIR:entityBlock:rangeBlock:errorBlock:]
+ -[SKGDataDetector locationFromAddress:locale:enablePIR:errorBlock:]
+ _OBJC_IVAR_$_SKGDataDetector._defaults
+ ___swift_closure_destructor.26Tm
- -[SKDLocationProcessor shouldLookupOnlineLocationsForRecord:]
- -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityBlock:rangeBlock:errorBlock:]
- -[SKGDataDetector enumerateDetectedDataInString:locale:referenceDate:referenceTimezone:entityCategories:entityBlock:rangeBlock:errorBlock:]
- -[SKGDataDetector enumerateDetectedLocationsInString:locale:entityBlock:rangeBlock:errorBlock:]
- ___swift_closure_destructor.30Tm
CStrings:
- "enableOfflineLocations"
- "enableOnlineLocations"
```
