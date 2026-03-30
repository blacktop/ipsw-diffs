## ShazamKit

> `/System/Library/Frameworks/ShazamKit.framework/ShazamKit`

```diff

-426.4.38.0.0
-  __TEXT.__text: 0x95840
+426.5.1.0.0
+  __TEXT.__text: 0x95858
   __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x5048
-  __TEXT.__const: 0x218a7
-  __TEXT.__cstring: 0x39c0
+  __TEXT.__objc_methlist: 0x50d8
+  __TEXT.__const: 0x21877
+  __TEXT.__cstring: 0x38e0
   __TEXT.__gcc_except_tab: 0x3b88
   __TEXT.__oslogstring: 0x149b
-  __TEXT.__constg_swiftt: 0x5f0
-  __TEXT.__swift5_typeref: 0xbec
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x3e2
-  __TEXT.__swift5_fieldmd: 0x580
+  __TEXT.__constg_swiftt: 0x5d0
+  __TEXT.__swift5_typeref: 0xbe6
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_reflstr: 0x3d2
+  __TEXT.__swift5_fieldmd: 0x558
   __TEXT.__swift5_assocty: 0x230
   __TEXT.__swift5_proto: 0xe4
-  __TEXT.__swift5_types: 0x84
+  __TEXT.__swift5_types: 0x80
   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0xc4
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x280
-  __TEXT.__unwind_info: 0x3388
+  __TEXT.__unwind_info: 0x33a8
   __TEXT.__eh_frame: 0x1da8
-  __TEXT.__objc_classname: 0xe06
-  __TEXT.__objc_methname: 0xa8b3
-  __TEXT.__objc_methtype: 0x207d
-  __TEXT.__objc_stubs: 0x7cc0
+  __TEXT.__objc_classname: 0xdf6
+  __TEXT.__objc_methname: 0xaa53
+  __TEXT.__objc_methtype: 0x20bd
+  __TEXT.__objc_stubs: 0x7d40
   __DATA_CONST.__got: 0x728
-  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2480
+  __DATA_CONST.__objc_selrefs: 0x2498
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x248
   __AUTH_CONST.__auth_got: 0xf30
-  __AUTH_CONST.__const: 0x1cd8
-  __AUTH_CONST.__cfstring: 0x27e0
-  __AUTH_CONST.__objc_const: 0x9cb0
+  __AUTH_CONST.__const: 0x1c58
+  __AUTH_CONST.__cfstring: 0x2780
+  __AUTH_CONST.__objc_const: 0x9d78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH.__objc_data: 0x9d8
+  __AUTH.__objc_data: 0xa28
   __AUTH.__data: 0x798
-  __DATA.__objc_ivar: 0x4c0
-  __DATA.__data: 0x1b24f0
+  __DATA.__objc_ivar: 0x4c8
+  __DATA.__data: 0x1b24d0
   __DATA.__bss: 0x1e08
   __DATA.__common: 0x1c8
-  __DATA_DIRTY.__objc_data: 0x1900
+  __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5AD32844-4713-371D-99AF-9E29B81ACC75
-  Functions: 3418
-  Symbols:   9201
-  CStrings:  3083
+  UUID: 61674AD4-26BF-369C-B85B-600C73A379F5
+  Functions: 3424
+  Symbols:   9231
+  CStrings:  3089
 
Symbols:
+ +[SHLocation anonymizedCoordinatesPayloadForLocation:truncatingToDecimalPlaces:]
+ +[SHLocation coordinateFromLocation:]
+ +[SHLocation locationFromCoordinate:]
+ +[SHLocation locationFromDictionaryRepresentation:]
+ +[SHLocation supportsSecureCoding]
+ -[SHCustomCatalog removeReferenceSignatureWithID:]
+ -[SHCustomCatalogMemoryContainer removeSignatureWithID:]
+ -[SHCustomCatalogMemoryStorage removeSignatureWithID:]
+ -[SHJSONLCustomCatalogContainer removeSignatureWithID:]
+ -[SHJSONLCustomCatalogContainer storage]
+ -[SHLocation anonymizedDictionaryRepresentation]
+ -[SHLocation coordinate]
+ -[SHLocation copyWithZone:]
+ -[SHLocation dictionaryRepresentation]
+ -[SHLocation encodeWithCoder:]
+ -[SHLocation hash]
+ -[SHLocation initWithCoder:]
+ -[SHLocation initWithCoordinate:]
+ -[SHLocation initWithDictionaryRepresentation:]
+ -[SHLocation isEqual:]
+ -[SHSignatureMetrics initWithSessionStartDate:signatureRecordingOffset:location:]
+ -[SHSignatureMetrics location]
+ -[SHSignatureMetrics setLocation:]
+ -[SHStreamingSessionDriver sessionStartDate]
+ -[SHStreamingSessionDriver setSessionStartDate:]
+ _OBJC_CLASS_$_NSDecimalNumberHandler
+ _OBJC_CLASS_$_SHLocation
+ _OBJC_IVAR_$_SHJSONLCustomCatalogContainer._storage
+ _OBJC_IVAR_$_SHLocation._coordinate
+ _OBJC_IVAR_$_SHSignatureMetrics._location
+ _OBJC_IVAR_$_SHStreamingSessionDriver._sessionStartDate
+ _OBJC_METACLASS_$_SHLocation
+ _SHMediaItemMatchLocation
+ __OBJC_$_CLASS_METHODS_SHLocation
+ __OBJC_$_CLASS_PROP_LIST_SHLocation
+ __OBJC_$_INSTANCE_METHODS_SHLocation
+ __OBJC_$_INSTANCE_VARIABLES_SHLocation
+ __OBJC_$_PROP_LIST_SHLocation
+ __OBJC_CLASS_PROTOCOLS_$_SHLocation
+ __OBJC_CLASS_RO_$_SHLocation
+ __OBJC_METACLASS_RO_$_SHLocation
+ _objc_msgSend$anonymizedCoordinatesPayloadForLocation:truncatingToDecimalPlaces:
+ _objc_msgSend$decimalNumberByRoundingAccordingToBehavior:
+ _objc_msgSend$decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$initWithCoordinate:
+ _objc_msgSend$initWithDictionaryRepresentation:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithSessionStartDate:signatureRecordingOffset:location:
+ _objc_msgSend$locationFromDictionaryRepresentation:
+ _objc_msgSend$removeSignatureWithID:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setSessionStartDate:
+ _objc_msgSend$storage
- +[SHLocationTransformer coordinateFromLocation:]
- +[SHLocationTransformer coordinateValueFromLatitude:longitude:]
- +[SHLocationTransformer coordinateValueFromLocation:]
- +[SHLocationTransformer isValidCoordinateValue:]
- +[SHLocationTransformer locationFromCoordinate:]
- +[SHLocationTransformer locationFromCoordinateValue:]
- +[SHLocationTransformer valueForCoordinate:]
- +[SHMediaItem transformedPropertiesFromProperties:]
- -[SHCustomCatalog removeReferenceSignatureWithID:error:]
- -[SHCustomCatalogMemoryContainer removeSignatureWithID:error:]
- -[SHCustomCatalogMemoryStorage removeSignatureWithID:error:]
- -[SHJSONLCustomCatalogContainer container]
- -[SHJSONLCustomCatalogContainer removeSignatureWithID:error:]
- -[SHStreamingSessionDriver metrics]
- _OBJC_CLASS_$_NSValue
- _OBJC_CLASS_$_SHLocationTransformer
- _OBJC_IVAR_$_SHJSONLCustomCatalogContainer._container
- _OBJC_IVAR_$_SHStreamingSessionDriver._metrics
- _OBJC_METACLASS_$_SHLocationTransformer
- _SHMediaItemMatchLocationCoordinate
- _SHMediaItemMatchLocationCoordinateSwift
- __OBJC_$_CLASS_METHODS_SHLocationTransformer
- __OBJC_CLASS_RO_$_SHLocationTransformer
- __OBJC_METACLASS_RO_$_SHLocationTransformer
- _objc_msgSend$coordinateValueFromLatitude:longitude:
- _objc_msgSend$getValue:size:
- _objc_msgSend$isValidCoordinateValue:
- _objc_msgSend$locationFromCoordinateValue:
- _objc_msgSend$objCType
- _objc_msgSend$removeSignatureWithID:error:
- _objc_msgSend$transformedPropertiesFromProperties:
- _objc_msgSend$valueForCoordinate:
- _objc_msgSend$valueWithBytes:objCType:
- _symbolic _____ So22CLLocationCoordinate2DV
- _type_layout_string So22CLLocationCoordinate2DV
CStrings:
+ "@\"SHLocation\""
+ "@36@0:8{CLLocationCoordinate2D=dd}16s32"
+ "@40@0:8@16d24@32"
+ "SHLocation"
+ "T@\"<SHCustomCatalogStorage>\",R,N,V_storage"
+ "T@\"NSDate\",&,N,V_sessionStartDate"
+ "T@\"NSDictionary\",R,C,N"
+ "T@\"SHLocation\",&,N,V_location"
+ "T@\"SHLocation\",R,N"
+ "T{CLLocationCoordinate2D=dd},R,N,V_coordinate"
+ "_coordinate"
+ "_storage"
+ "anonymizedCoordinatesPayloadForLocation:truncatingToDecimalPlaces:"
+ "anonymizedDictionaryRepresentation"
+ "decimalNumberByRoundingAccordingToBehavior:"
+ "decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:"
+ "dictionaryRepresentation"
+ "initWithCoordinate:"
+ "initWithDictionaryRepresentation:"
+ "initWithDouble:"
+ "initWithSessionStartDate:signatureRecordingOffset:location:"
+ "locationFromDictionaryRepresentation:"
+ "removeReferenceSignatureWithID:"
+ "removeSignatureWithID:"
+ "setSessionStartDate:"
+ "sh_matchLocation"
+ "storage"
+ "v24@0:8@\"NSString\"16"
- "B32@0:8@\"NSString\"16^@24"
- "SHLocationTransformer"
- "Signature with identifier '%@' could not be removed as it does not exist in the custom catalog."
- "T@\"SHSignatureMetrics\",R,N,V_metrics"
- "coordinateValueFromLatitude:longitude:"
- "coordinateValueFromLocation:"
- "getValue:size:"
- "isValidCoordinateValue:"
- "locationFromCoordinateValue:"
- "matchLocationLatitude"
- "matchLocationLongitude"
- "objCType"
- "removeReferenceSignatureWithID:error:"
- "removeSignatureWithID:error:"
- "sh_matchLocationCoordinate"
- "sh_matchLocationCoordinate_Swift"
- "transformedPropertiesFromProperties:"
- "valueForCoordinate:"
- "valueWithBytes:objCType:"
- "{CLLocationCoordinate2D=dd}"

```
