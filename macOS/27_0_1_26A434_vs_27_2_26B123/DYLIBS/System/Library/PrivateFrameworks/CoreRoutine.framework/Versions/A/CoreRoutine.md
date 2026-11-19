## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/CoreRoutine`

```diff

-1122.0.0.0.0
-  __TEXT.__text: 0x7041c
-  __TEXT.__objc_methlist: 0x847c
-  __TEXT.__const: 0x278
+1123.0.3.0.0
+  __TEXT.__text: 0x70198
+  __TEXT.__objc_methlist: 0x8474
+  __TEXT.__const: 0x270
   __TEXT.__oslogstring: 0x3131
-  __TEXT.__cstring: 0x7371
+  __TEXT.__cstring: 0x735e
   __TEXT.__gcc_except_tab: 0x38c
-  __TEXT.__unwind_info: 0x1ed8
+  __TEXT.__unwind_info: 0x1ec8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c0
+  __DATA_CONST.__objc_selrefs: 0x29b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x98

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1090
+  __AUTH.__objc_data: 0xf50
   __DATA.__objc_ivar: 0x898
   __DATA.__data: 0x2d0
   __DATA_DIRTY.__objc_ivar: 0x150
-  __DATA_DIRTY.__objc_data: 0x1d60
+  __DATA_DIRTY.__objc_data: 0x1ea0
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2975
-  Symbols:   6231
-  CStrings:  1131
+  Functions: 2974
+  Symbols:   6229
+  CStrings:  1130
 
Symbols:
+ _kRTFamiliarityIndexOptionsUnspecifiedLookbackInterval
- -[RTAddress initWithGeoDictionary:language:country:phoneticLocale:]
- __os_feature_enabled_impl
- _objc_msgSend$initWithIdentifier:geoAddressObject:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:
Functions:
- -[RTAddress initWithGeoDictionary:language:country:phoneticLocale:]
~ -[RTFamiliarityIndexOptions init] : 116 -> 28
~ -[RTFamiliarityIndexOptions initWithDateInterval:spatialGranularity:] : 144 -> 20
~ -[RTFamiliarityIndexOptions initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:] : 356 -> 296
CStrings:
- "ExtendedTimeToLive"
```
