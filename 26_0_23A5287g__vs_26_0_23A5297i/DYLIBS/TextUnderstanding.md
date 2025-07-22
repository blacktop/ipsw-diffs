## TextUnderstanding

> `/System/Library/PrivateFrameworks/TextUnderstanding.framework/TextUnderstanding`

```diff

-113.0.0.0.0
-  __TEXT.__text: 0xd54f4
-  __TEXT.__auth_stubs: 0x10d0
+116.0.1.0.0
+  __TEXT.__text: 0xe6300
+  __TEXT.__auth_stubs: 0x13a0
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x17d88
-  __TEXT.__cstring: 0x1b92
-  __TEXT.__swift5_typeref: 0x492b
-  __TEXT.__constg_swiftt: 0x3720
-  __TEXT.__swift5_reflstr: 0x244f
-  __TEXT.__swift5_fieldmd: 0x524c
-  __TEXT.__swift5_proto: 0x18d4
-  __TEXT.__swift5_types: 0x630
-  __TEXT.__swift5_assocty: 0x228
-  __TEXT.__oslogstring: 0x5e0
-  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__const: 0x18f80
+  __TEXT.__cstring: 0x1ca2
+  __TEXT.__swift5_typeref: 0x4c7f
+  __TEXT.__constg_swiftt: 0x3954
+  __TEXT.__swift5_reflstr: 0x25df
+  __TEXT.__swift5_fieldmd: 0x5574
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_assocty: 0x270
+  __TEXT.__swift5_proto: 0x1a04
+  __TEXT.__swift5_types: 0x670
+  __TEXT.__oslogstring: 0x840
+  __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x4718
-  __TEXT.__eh_frame: 0x37b0
-  __TEXT.__objc_methname: 0xef4
-  __DATA_CONST.__got: 0x318
+  __TEXT.__unwind_info: 0x4b20
+  __TEXT.__eh_frame: 0x3bc8
+  __TEXT.__objc_methname: 0x10a8
+  __DATA_CONST.__got: 0x3e0
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x558
+  __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0x83c8
+  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH_CONST.__const: 0x8b40
   __AUTH_CONST.__objc_const: 0x120
-  __DATA.__data: 0x3738
-  __DATA.__bss: 0x2ac80
+  __AUTH.__data: 0x88
+  __DATA.__data: 0x3a48
+  __DATA.__bss: 0x2d180
   __DATA_DIRTY.__data: 0x24c8
   __DATA_DIRTY.__bss: 0x6680
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient
   - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3E9398DA-9B26-39FB-8913-12DB90323AB7
-  Functions: 8253
-  Symbols:   139
-  CStrings:  402
+  UUID: 19028681-2F21-38EE-82C7-39BEDD9B9180
+  Functions: 8723
+  Symbols:   153
+  CStrings:  436
 
Symbols:
+ _IOSurfacePropertyKeyBytesPerRow
+ _IOSurfacePropertyKeyHeight
+ _IOSurfacePropertyKeyPixelFormat
+ _IOSurfacePropertyKeyWidth
+ _OBJC_CLASS_$_IOSurface
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSObject
+ __swiftEmptySetSingleton
+ _objc_retainAutorelease
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x27
+ _swift_bridgeObjectRetain_n
+ _swift_getForeignTypeMetadata
CStrings:
+ "/^(?i)\\[?(fw|fwd|forward)\\]?\\s*:\\s*/"
+ "<Document.Kind calendarEvent>"
+ "<Document.Kind file>"
+ "<Request.Kind identificationDocumentsEligibility>"
+ "CSSearchableItem missing title and thus cannot be converted to CalendarEvent"
+ "Event+PostProcess: Converting event to all day event"
+ "Event+PostProcess: Using default end date time for extracted event"
+ "Event+PostProcess: carRental as a single event"
+ "Event+PostProcess: splitting carRental into multiple events"
+ "Image.Representation: failed to decode surface data - provided pixel data is too small"
+ "Image.Representation: failed to encode surface data - Surface allocation is too small to encode"
+ "Image.Representation: failed to encode surface data - too many planes to encode"
+ "allocationSize"
+ "baseAddress"
+ "bytesPerRow"
+ "carRental|{dropoff}|"
+ "carRental|{pickup}|"
+ "extractedEndTimeComponents"
+ "extractedStartTimeComponents"
+ "extractionVersion"
+ "fullyFormattedAddress"
+ "height"
+ "identificationDocumentsEligibility"
+ "initWithProperties:"
+ "lockWithOptions:seed:"
+ "pixelFormat"
+ "planeCount"
+ "setEventEndLocationAddressCountry:"
+ "setEventEndLocationAddressLatitude:"
+ "setEventEndLocationAddressLocality:"
+ "setEventEndLocationAddressLongitude:"
+ "setEventEndLocationAddressRegion:"
+ "setEventSourceIsForwarded:"
+ "setEventStartLocationAddressCountry:"
+ "setEventStartLocationAddressLatitude:"
+ "setEventStartLocationAddressLocality:"
+ "setEventStartLocationAddressLongitude:"
+ "setEventStartLocationAddressRegion:"
+ "setFormatOptions:"
+ "surface"
+ "unlockWithOptions:seed:"
+ "width"
- "_messageIdentifier"
- "capturedDocumentType"
- "endTimeComponents"
- "setFlightArrivalAirportLatitude:"
- "setFlightArrivalAirportLongitude:"
- "setFlightDepartureAirportLatitude:"
- "setFlightDepartureAirportLongitude:"
- "startTimeComponents"

```
