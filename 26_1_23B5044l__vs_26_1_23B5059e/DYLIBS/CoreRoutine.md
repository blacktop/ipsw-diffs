## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1067.0.2.0.0
-  __TEXT.__text: 0x640d4
-  __TEXT.__auth_stubs: 0x6a0
+1069.0.1.0.0
+  __TEXT.__text: 0x640d8
+  __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_methlist: 0x7d84
   __TEXT.__const: 0x2c8
   __TEXT.__oslogstring: 0x331f
-  __TEXT.__cstring: 0x644c
+  __TEXT.__cstring: 0x6466
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__unwind_info: 0x1e08
+  __TEXT.__unwind_info: 0x1e00
   __TEXT.__objc_classname: 0xf9a
-  __TEXT.__objc_methname: 0xed3c
-  __TEXT.__objc_methtype: 0x26d3
-  __TEXT.__objc_stubs: 0x74c0
+  __TEXT.__objc_methname: 0xed42
+  __TEXT.__objc_methtype: 0x26d7
+  __TEXT.__objc_stubs: 0x74a0
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x1290
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2850
+  __DATA_CONST.__objc_selrefs: 0x2848
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x5980
-  __AUTH_CONST.__objc_const: 0xe210
+  __AUTH_CONST.__cfstring: 0x59a0
+  __AUTH_CONST.__objc_const: 0xe230
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x808
+  __DATA.__objc_ivar: 0x80c
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_ivar: 0x130
   __DATA_DIRTY.__objc_data: 0x16d0

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94C97671-A0B5-3B8D-837E-6636574234A6
+  UUID: 54D3FBFD-2587-3366-8B6D-F9C45C1A0EF7
   Functions: 2806
-  Symbols:   8762
-  CStrings:  4427
+  Symbols:   8761
+  CStrings:  4429
 
Symbols:
+ -[RTMapItem initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:]
+ _OBJC_IVAR_$_RTMapItem._geoMapItemIdentifier
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
+ _objc_msgSend$mapsIdentifierString
- -[RTMapItem initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:]
- __os_log_fault_impl
- _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
- _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
- _objc_msgSend$initWithMUID:coordinate:
Functions:
~ -[RTMapItem .cxx_destruct] : 176 -> 188
~ -[RTMapItem initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:] -> -[RTMapItem initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:] : 1048 -> 1080
~ -[RTMapItem description] : 412 -> 448
~ -[RTMapItem initWithCoder:] : 860 -> 908
~ -[RTMapItem encodeWithCoder:] : 496 -> 516
~ -[RTMapItem geoMapItemIdentifier] -> -[RTMapItem setExtendedAttributes:] : 152 -> 128
~ -[RTMapItem setExtendedAttributes:] -> -[RTMapItem setSource:] : 128 -> 28
~ -[RTMapItem setSource:] -> -[RTMapItem updateWeightWithSource:extendedAttributes:] : 28 -> 192
~ -[RTMapItem updateWeightWithSource:extendedAttributes:] -> +[RTMapItem weightForExtendedAttributes:] : 192 -> 108
~ +[RTMapItem weightForExtendedAttributes:] -> +[RTMapItem weightForSource:] : 108 -> 200
~ +[RTMapItem weightForSource:] -> -[RTMapItem category] : 200 -> 8
CStrings:
+ "@148@0:8@16@24@32@40@48@56Q64Q72Q80q88@96@104@112@120@128@136B144"
+ "T@\"NSData\",R,N,V_geoMapItemIdentifier"
+ "_geoMapItemIdentifier"
+ "identifier, %@, geoMapItemIdentifier, %@ (%@), name, \"%@\", category, %@, categoryMUID, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
+ "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
+ "mapsIdentifierString"
- "@140@0:8@16@24@32@40@48@56Q64Q72Q80q88@96@104@112@120@128B136"
- "T@\"NSData\",R,N"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "identifier, %@, geoMapItemIdentifier, %@, name, \"%@\", category, %@, categoryMUID, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
- "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "initWithMUID:coordinate:"

```
