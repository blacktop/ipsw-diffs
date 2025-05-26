## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1870.2.1.0.0
-  __TEXT.__text: 0x121f2c
+1870.4.3.0.0
+  __TEXT.__text: 0x12223c
   __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0x132f8
+  __TEXT.__objc_methlist: 0x132e8
   __TEXT.__const: 0x4f2
-  __TEXT.__cstring: 0xaaae
+  __TEXT.__cstring: 0xad64
   __TEXT.__oslogstring: 0xc814
   __TEXT.__gcc_except_tab: 0x26d8
   __TEXT.__dlopen_cstrs: 0x2ba

   __TEXT.__swift5_fieldmd: 0xf8
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0x1b2
-  __TEXT.__swift5_capture: 0xa0
-  __TEXT.__unwind_info: 0x4928
+  __TEXT.__swift5_capture: 0xb0
+  __TEXT.__unwind_info: 0x491c
   __TEXT.__objc_classname: 0x1801
-  __TEXT.__objc_methname: 0x2abb2
+  __TEXT.__objc_methname: 0x2abec
   __TEXT.__objc_methtype: 0x3e06
-  __TEXT.__objc_stubs: 0x1e3a0
+  __TEXT.__objc_stubs: 0x1e460
   __DATA_CONST.__got: 0xbf8
-  __DATA_CONST.__const: 0x3cc8
+  __DATA_CONST.__const: 0x3ca0
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x16908
-  __DATA_CONST.__objc_selrefs: 0x9d08
+  __DATA_CONST.__objc_selrefs: 0x9d30
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0xb10
+  __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x610
   __AUTH_CONST.__objc_const: 0x6338
-  __AUTH_CONST.__cfstring: 0x8ec0
-  __AUTH_CONST.__const: 0x1ae0
+  __AUTH_CONST.__cfstring: 0x8ea0
+  __AUTH_CONST.__const: 0x1b08
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xa28
-  __AUTH.__objc_data: 0x2568
+  __AUTH.__objc_data: 0x2518
   __AUTH.__data: 0xa0
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0xb10
-  __DATA.__objc_superrefs: 0x4d0
   __DATA.__objc_ivar: 0xc1c
   __DATA.__data: 0x1510
   __DATA.__bss: 0x3d8
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1f90
+  __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x838
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8186
+  Functions: 8188
   Symbols:   25042
-  CStrings:  9388
+  CStrings:  9410
 
Symbols:
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:]
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:].cold.1
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:].cold.2
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:].cold.3
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:].cold.4
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:].cold.5
+ -[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:].cold.6
+ -[EKTravelLookupManager _travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]
+ _CalRouteType_Bicycle
+ __OBJC_$_PROP_LIST_EKCalendarShareeOrOwner.635
+ __PROTOCOLS__TtC8EventKit33EKRemoteUIPersistentObjectPointer.12
+ ___68-[EKAutocompleter autocompleteResultsFromDirectoryRecords:withType:]_block_invoke.61
+ ___69-[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:]_block_invoke
+ ___69-[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:]_block_invoke.cold.1
+ ___69-[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:]_block_invoke.cold.2
+ ___69-[EKTravelLookupManager _findCoordinatesForLocation:completionBlock:]_block_invoke.cold.3
+ ___90-[EKTravelLookupManager _travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke
+ ___90-[EKTravelLookupManager _travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke_2
+ ___90-[EKTravelLookupManager _travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke_3
+ ___90-[EKTravelLookupManager _travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke_3.cold.1
+ ___block_literal_global.1453
+ _objc_msgSend$_findCoordinatesForLocation:completionBlock:
+ _objc_msgSend$_travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:
+ _objc_msgSend$middleName
+ _objc_msgSend$namePrefix
+ _objc_msgSend$nameSuffix
+ _objc_msgSend$nickname
+ _objc_msgSend$setMiddleName:
+ _objc_msgSend$setNamePrefix:
+ _objc_msgSend$setNameSuffix:
- +[EKTravelLookupManager geocodeAddress:withCompletionBlock:]
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:]
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:].cold.1
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:].cold.2
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:].cold.3
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:].cold.4
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:].cold.5
- -[EKTravelLookupManager findCoordinatesForLocation:completionBlock:].cold.6
- -[EKTravelLookupManager travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]
- __OBJC_$_PROP_LIST_EKCalendarShareeOrOwner.633
- __PROTOCOLS__TtC8EventKit33EKRemoteUIPersistentObjectPointer.13
- ___60+[EKTravelLookupManager geocodeAddress:withCompletionBlock:]_block_invoke
- ___68-[EKAutocompleter autocompleteResultsFromDirectoryRecords:withType:]_block_invoke.60
- ___68-[EKTravelLookupManager findCoordinatesForLocation:completionBlock:]_block_invoke
- ___68-[EKTravelLookupManager findCoordinatesForLocation:completionBlock:]_block_invoke.cold.1
- ___68-[EKTravelLookupManager findCoordinatesForLocation:completionBlock:]_block_invoke.cold.2
- ___68-[EKTravelLookupManager findCoordinatesForLocation:completionBlock:]_block_invoke.cold.3
- ___89-[EKTravelLookupManager travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke
- ___89-[EKTravelLookupManager travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke_2
- ___89-[EKTravelLookupManager travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke_3
- ___89-[EKTravelLookupManager travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:]_block_invoke_3.cold.1
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
- ___block_literal_global.1452
- _objc_msgSend$findCoordinatesForLocation:completionBlock:
- _objc_msgSend$geocodeAddressString:completionHandler:
- _objc_msgSend$travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,R,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_findCoordinatesForLocation:completionBlock:"
+ "_travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:"
+ "invalid Collection: less than 'count' elements in collection"
+ "middleName"
+ "namePrefix"
+ "nameSuffix"
+ "nickname"
+ "setMiddleName:"
+ "setNamePrefix:"
+ "setNameSuffix:"
- "CLGeocoder"
- "findCoordinatesForLocation:completionBlock:"
- "geocodeAddress:withCompletionBlock:"
- "geocodeAddressString:completionHandler:"
- "travelTimeFrom:to:arrivalDate:withRouteType:withCompletionBlock:"

```
