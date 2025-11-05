## ShazamEvents

> `/System/Library/PrivateFrameworks/ShazamEvents.framework/Versions/A/ShazamEvents`

```diff

-307.2.0.0.0
-  __TEXT.__text: 0x6dc98
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x198
-  __TEXT.__const: 0x6ca8
-  __TEXT.__cstring: 0xf12
+318.0.0.0.0
+  __TEXT.__text: 0x69e10
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_methlist: 0x3d4
+  __TEXT.__const: 0x6cb0
+  __TEXT.__cstring: 0xe02
   __TEXT.__constg_swiftt: 0x17a8
-  __TEXT.__swift5_typeref: 0x1c45
+  __TEXT.__swift5_typeref: 0x1caf
   __TEXT.__swift5_reflstr: 0x9b6
   __TEXT.__swift5_fieldmd: 0x193c
   __TEXT.__swift5_proto: 0x7cc
   __TEXT.__swift5_types: 0x1f8
   __TEXT.__swift5_assocty: 0x360
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x1e8
   __TEXT.__oslogstring: 0x18
-  __TEXT.__unwind_info: 0x2268
-  __TEXT.__eh_frame: 0x3794
+  __TEXT.__unwind_info: 0x20d8
+  __TEXT.__eh_frame: 0x3744
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methname: 0x79c
   __TEXT.__objc_methtype: 0x333
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_protorefs: 0x48
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH_CONST.__const: 0x4020
-  __AUTH_CONST.__objc_const: 0xeb8
-  __AUTH.__objc_data: 0x470
+  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__const: 0x41b0
+  __AUTH_CONST.__objc_const: 0xb00
+  __AUTH.__objc_data: 0x420
   __AUTH.__data: 0xdb8
-  __DATA.__data: 0x21e0
+  __DATA.__data: 0x2180
   __DATA.__bss: 0xf620
   __DATA.__common: 0x50
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C778F8F4-E0B0-36DE-9E47-DB2453305CFF
-  Functions: 2775
-  Symbols:   1033
-  CStrings:  258
+  UUID: 662B2C90-16B7-3EDB-90F4-C5E68595583A
+  Functions: 2678
+  Symbols:   1079
+  CStrings:  249
 
Symbols:
+ SHShazamEventsClientInterface.cold.1
+ SHShazamEventsServiceInterface.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_1Tm
+ _symbolic SccySS_____G s5NeverO
+ _symbolic SccySS______pG s5ErrorP
+ _symbolic SccySo11SHEndpointsC______pG s5ErrorP
+ _symbolic SccySo12AMSURLResultC______pG s5ErrorP
+ _symbolic SccySo13AMSURLRequestC______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ block_copy_helper.2
+ block_copy_helper.27
+ block_copy_helper.37
+ block_copy_helper.46
+ block_copy_helper.50
+ block_copy_helper.54
+ block_copy_helper.58
+ block_copy_helper.61
+ block_descriptor.29
+ block_descriptor.39
+ block_descriptor.4
+ block_descriptor.52
+ block_descriptor.56
+ block_descriptor.60
+ block_descriptor.63
+ block_destroy_helper.28
+ block_destroy_helper.3
+ block_destroy_helper.38
+ block_destroy_helper.47
+ block_destroy_helper.51
+ block_destroy_helper.55
+ block_destroy_helper.59
+ block_destroy_helper.62
- _symbolic _____Sg 12ShazamEvents15VenueAttributesV
- _symbolic _____Sg 12ShazamEvents17PromotionalAssetsV10PhotoAlbumV0E0V
- _symbolic _____Sg 12ShazamEvents17PromotionalAssetsV14PhoneWallpaperV
- _symbolic _____Sg 12ShazamEvents17PromotionalAssetsV9WatchFaceV
- block_descriptor.2
- block_descriptor.35
- block_descriptor.42
- block_descriptor.44
- block_descriptor.46
- block_descriptor.49
CStrings:
+ "event/v2/{storefront}/shazam-events/{event_id}?l={lang}&webUrl=apple&format[artists.artwork.url]=c,f"
+ "event/v2/{storefront}/shazam-events?l={lang}&artistId={artistid}&from={fromdate}&to={todate}&limit={limit}&offset={offset}&webUrl=apple&filter[hasVenue]=true&format[artists.artwork.url]=c,f"
+ "event/v2/{storefront}/venues/{venue_id}?l={lang}&filter[shazam-events.startTime.from]={fromdate}&filter[shazam-events.startTime.to]={todate}&limit={limit}&offset={offset}&webUrl=apple&format[artists.artwork.url]=c,f"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Swift/Array.swift"
- "Swift/IntegerTypes.swift"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "event/v2/{storefront}/shazam-events/{event_id}?l={lang}&webUrl=apple"
- "event/v2/{storefront}/shazam-events?l={lang}&artistId={artistid}&from={fromdate}&to={todate}&limit={limit}&offset={offset}&webUrl=apple&filter[hasVenue]=true"
- "event/v2/{storefront}/venues/{venue_id}?l={lang}&filter[shazam-events.startTime.from]={fromdate}&filter[shazam-events.startTime.to]={todate}&limit={limit}&offset={offset}"

```
