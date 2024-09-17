## HomeWidgetIntents

> `/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents`

```diff

-962.0.0.0.0
-  __TEXT.__text: 0x3bfbc
-  __TEXT.__auth_stubs: 0x17b0
-  __TEXT.__const: 0x2a10
-  __TEXT.__cstring: 0x7fc
-  __TEXT.__oslogstring: 0x5cd
-  __TEXT.__constg_swiftt: 0x538
-  __TEXT.__swift5_typeref: 0xc9a
-  __TEXT.__swift5_reflstr: 0x339
-  __TEXT.__swift5_fieldmd: 0x4b0
+963.2.3.0.0
+  __TEXT.__text: 0x403bc
+  __TEXT.__auth_stubs: 0x19b0
+  __TEXT.__const: 0x2b20
+  __TEXT.__cstring: 0x7ec
+  __TEXT.__oslogstring: 0x63d
+  __TEXT.__constg_swiftt: 0x554
+  __TEXT.__swift5_typeref: 0xdb8
+  __TEXT.__swift5_reflstr: 0x35c
+  __TEXT.__swift5_fieldmd: 0x4e4
   __TEXT.__swift5_capture: 0x64
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x338
-  __TEXT.__swift5_proto: 0x274
-  __TEXT.__swift5_types: 0x78
+  __TEXT.__swift5_proto: 0x27c
+  __TEXT.__swift5_types: 0x7c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1140
-  __TEXT.__eh_frame: 0x1f20
-  __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x3f0
-  __TEXT.__objc_methtype: 0xbd
-  __DATA_CONST.__got: 0x2f0
+  __TEXT.__unwind_info: 0x1188
+  __TEXT.__eh_frame: 0x1f30
+  __TEXT.__objc_classname: 0x9b
+  __TEXT.__objc_methname: 0x720
+  __TEXT.__objc_methtype: 0x1b1
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x120
-  __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__auth_ptr: 0x680
-  __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__objc_const: 0x4c0
+  __DATA_CONST.__objc_selrefs: 0x118
+  __DATA_CONST.__objc_protorefs: 0x40
+  __AUTH_CONST.__auth_got: 0xcd8
+  __AUTH_CONST.__auth_ptr: 0x6c8
+  __AUTH_CONST.__const: 0xb88
+  __AUTH_CONST.__objc_const: 0xb30
   __AUTH.__data: 0x118
-  __DATA.__data: 0xc08
+  __DATA.__data: 0xe80
   __DATA.__common: 0x60
-  __DATA.__bss: 0x3288
+  __DATA.__bss: 0x3388
   __DATA_DIRTY.__data: 0x540
   __DATA_DIRTY.__bss: 0x1c80
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/Home.framework/Home
   - /System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1257
-  Symbols:   181
-  CStrings:  164
+  Functions: 1294
+  Symbols:   184
+  CStrings:  221
 
Symbols:
+ _swift_setDeallocating
+ _swift_unknownObjectRelease_n
+ _swift_getAtKeyPath
+ _swift_unknownObjectRetain_n
- _objc_retain_x24
CStrings:
+ "hf_isInRoom:"
+ "hf_shouldShowInFavorites"
+ "HFFavoritable"
+ "hf_associatedAccessories"
+ "hf_effectiveIsFavorite"
+ "hf_setTileSize:"
+ "@\"<HFHomeContainedObject>\"16@0:8"
+ "T@\"NSSet\",R,N"
+ "hf_homeKitObject"
+ "hf_containedProfiles"
+ "hf_showInHomeDashboard"
+ "T@\"HMRoom\",R,N"
+ "T@\"NSString\",R,N"
+ "hf_itemClass"
+ "hf_isForcedVisibleInHomeStatus"
+ "hf_safeRoom"
+ "hf_serviceNameComponents"
+ "%!s(MISSING) ElementID generated for Matter Accessory: %!l(MISSING)lu -> %!s(MISSING)"
+ "HFShowInHomeDashboard"
+ "hf_canShowInControlCenter"
+ "hf_accessoryType"
+ "T@\"<HFHomeContainedObject>\",R,N"
+ "hf_updateIsFavorite:"
+ "T@\"HFServiceNameComponents\",R,N"
+ "T@\"HFAccessoryType\",R,N"
+ "@20@0:8B16"
+ "hf_updateIsVisibleInHomeStatus:"
+ "%!s(MISSING) ElementID generated for HAP Accessory: %!s(MISSING)"
+ "hf_hasSetFavorite"
+ "B24@0:8@\"HMRoom\"16"
+ "hf_isIdentifiable"
+ "@\"NAFuture\"24@0:8@\"NSString\"16"
+ "hf_isFavorite"
+ "hf_effectiveShowInHomeDashboard"
+ "hf_isMatterOnlyAccessory"
+ "hf_updateShowInHomeDashboard:"
+ "hf_isVisibleInHomeStatus"
+ "HFServiceNameComponentsProviding"
+ "TB,R,N"
+ "@\"HMRoom\"16@0:8"
+ "hf_supportsHomeStatus"
+ "@\"NSSet\"16@0:8"
+ "hf_tileSize"
+ "hf_moveToRoom:"
+ "hf_containedCharacteristics"
+ "hf_hasSetShowInHomeDashboard"
+ "@\"HFServiceNameComponents\"16@0:8"
+ "HFTileResizable"
+ "@\"NAFuture\"20@0:8B16"
+ "@\"NAFuture\"24@0:8@\"HMRoom\"16"
+ "@\"HFAccessoryType\"16@0:8"
+ "HFAccessoryRepresentable"
+ "hf_containedServices"
+ "HFHomeStatusVisible"
+ "T#,R,N"
+ "hf_canSpanMultipleRooms"
+ "@24@0:8@16"
+ "hf_hasSetVisibleInHomeStatus"
- "homeKitObject"

```
