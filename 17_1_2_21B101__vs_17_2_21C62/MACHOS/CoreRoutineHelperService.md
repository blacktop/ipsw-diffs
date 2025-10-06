## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

-893.0.5.0.2
-  __TEXT.__text: 0xec64
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x2800
-  __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__const: 0x88
-  __TEXT.__oslogstring: 0xd3d
-  __TEXT.__cstring: 0xd67
-  __TEXT.__objc_methname: 0x4bf6
+895.0.11.0.2
+  __TEXT.__text: 0x10560
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_methlist: 0x954
+  __TEXT.__const: 0x138
+  __TEXT.__oslogstring: 0xe24
+  __TEXT.__cstring: 0xe48
+  __TEXT.__objc_methname: 0x4dc0
   __TEXT.__objc_classname: 0x351
-  __TEXT.__objc_methtype: 0x2470
+  __TEXT.__objc_methtype: 0x25c4
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x2e4
-  __DATA_CONST.__auth_got: 0x360
+  __TEXT.__unwind_info: 0x32c
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0xac0
+  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2f48
-  __DATA.__objc_selrefs: 0xe78
+  __DATA.__objc_const: 0x2fe8
+  __DATA.__objc_selrefs: 0xea0
   __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x1c8
+  __DATA.__objc_classrefs: 0x1d0
   __DATA.__objc_superrefs: 0x48
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x320

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7AA467FC-69F6-33A9-A704-7606198443B8
-  Functions: 211
-  Symbols:   199
-  CStrings:  1206
+  UUID: 9B2E5478-FCF1-3AF0-965E-9AC648AD006E
+  Functions: 231
+  Symbols:   202
+  CStrings:  1238
 
Symbols:
+ _OBJC_CLASS_$_GEOMapItemIdentifier
+ __RTMultiErrorCreate
+ __RTSafeArray
CStrings:
+ "%@, %lu geoMapItems from reverseGeocode, %@, error, %@"
+ "%@, %lu mapItems from %lu GEOMapItem identifiers, error, %@"
+ "%@, %lu, mapItemsIdentifiers for reverseGeocode relatedPlaces, %lu, mapItems, %@, error"
+ "%@, related mapItem %lu, %@"
+ "Q20@0:8i16"
+ "Q32@0:8@16Q24"
+ "_relatedPlaceLists"
+ "_relatedPlacesMapItemsIdentifiersForGEOMapItem:relatedPlaceListType:handler:"
+ "_relatedPlacesMapItemsIdentifiersForGEOMapItems:relatedPlaceListType:handler:"
+ "com.apple.CoreRoutine.AuthorizedLocation"
+ "detailsViewOpenedForSessionID:"
+ "fetchAuthorizedLocationStatus:"
+ "fetchAuthorizedLocations:"
+ "fetchMapGEOItemsFromLocation:options:handler:"
+ "fetchMapItemsFromIdentifiers:options:source:handler:"
+ "fetchMapItemsRelatedPlacesFromLocation:options:handler:"
+ "fetchRelatedPlacesMapItemsForGEOMapItem:relatedPlaceListType:options:source:handler:"
+ "fetchRelatedPlacesMapItemsForMapItem:relatedPlaceListType:options:source:handler:"
+ "initWithIdentifier:geoAddressObject:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
+ "initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
+ "injectPeopleDensityStats:duration:date:advertisements:handler:"
+ "mapIdentifiers"
+ "mapItemPlaceTypeFromGEOMapItem:source:"
+ "mapItemPlaceTypeFromGEOMapItemPlaceType:"
+ "requires a GEOMapItem."
+ "requires a list GEOMapItems."
+ "requires a list of GEOMapItem identifiers."
+ "requires a map item."
+ "set"
+ "ticketForIdentifiers:traits:"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@?<v@?@\"RTAuthorizedLocationStatus\"@\"NSError\">16"
+ "v32@?0@\"<GEOMapItem>\"8Q16^B24"
+ "v32@?0@\"GEOMapItemIdentifier\"8Q16^B24"
+ "v36@0:8@16i24@?28"
+ "v40@0:8@\"RTLocation\"16@\"RTMapServiceOptions\"24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
+ "v48@0:8@\"NSArray\"16@\"RTMapServiceOptions\"24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16@24Q32@?40"
+ "v52@0:8@16i24@28Q36@?44"
+ "v56@0:8Q16d24@\"NSDate\"32@\"NSArray\"40@?<v@?@\"NSError\">48"
+ "v56@0:8Q16d24@32@40@?48"
- "administrativeArea"
- "administrativeAreaCode"
- "country"
- "countryCode"
- "initWithIdentifier:name:category:address:location:source:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "initWithIdentifier:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
- "injectPeopleDensityStats:duration:date:handler:"
- "inlandWater"
- "ocean"
- "postCode"
- "subAdministrativeArea"
- "subThoroughfare"
- "v48@0:8Q16d24@\"NSDate\"32@?<v@?@\"NSError\">40"
- "v48@0:8Q16d24@32@?40"

```
