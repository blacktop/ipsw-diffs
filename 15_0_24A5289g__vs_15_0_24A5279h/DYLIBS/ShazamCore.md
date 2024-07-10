## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/Versions/A/ShazamCore`

```diff

-294.0.0.0.0
+290.0.0.0.0
   __TEXT.__text: 0xc67c
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_methlist: 0xd78
   __TEXT.__const: 0x7a
-  __TEXT.__cstring: 0xc7c
+  __TEXT.__cstring: 0xc2c
   __TEXT.__oslogstring: 0x49f
   __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__swift5_typeref: 0x60

   __TEXT.__objc_methtype: 0x53c
   __TEXT.__objc_stubs: 0x1c60
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 359
-  Symbols:   1041
+  Symbols:   1039
   CStrings:  138
 
Symbols:
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_ShazamCore
CStrings:
+ "/v1/catalog/{storefront}/songs/{id}?fields=name,hapticsAssetUrl,durationInMillis&format[resources]=map"
+ "/v1/catalog/{storefront}/songs?filter[isrc]={id}&format[resources]=map&fields=name,hapticsAssetUrl,durationInMillis"
- "/v1/catalog/{storefront}/songs/{id}?fields=name,hapticsAssetUrl,durationInMillis,spatialOffsets&format[resources]=map&extend=spatialOffsets"
- "/v1/catalog/{storefront}/songs?filter[isrc]={id}&fields=name,hapticsAssetUrl,durationInMillis,spatialOffsets&format[resources]=map&extend=spatialOffsets"

```
