## ConfigurationEngineModel

> `/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel`

```diff

-240.0.0.0.0
-  __TEXT.__text: 0xb2aa0
+241.0.0.0.0
+  __TEXT.__text: 0xb2f10
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x15c34
+  __TEXT.__objc_methlist: 0x15d4c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x94f4
-  __TEXT.__unwind_info: 0x2d40
-  __TEXT.__objc_classname: 0x4669
-  __TEXT.__objc_methname: 0x287c6
+  __TEXT.__cstring: 0x9544
+  __TEXT.__unwind_info: 0x2d68
+  __TEXT.__objc_classname: 0x46b4
+  __TEXT.__objc_methname: 0x28724
   __TEXT.__objc_methtype: 0x13ce
-  __TEXT.__objc_stubs: 0x8c40
-  __DATA_CONST.__got: 0xee0
+  __TEXT.__objc_stubs: 0x8c60
+  __DATA_CONST.__got: 0xef0
   __DATA_CONST.__const: 0x1588
-  __DATA_CONST.__objc_classlist: 0xe48
+  __DATA_CONST.__objc_classlist: 0xe58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4f60
-  __DATA_CONST.__objc_superrefs: 0x8e0
-  __DATA_CONST.__objc_arraydata: 0xb40
+  __DATA_CONST.__objc_superrefs: 0x8e8
+  __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x1ea0
-  __AUTH_CONST.__cfstring: 0xd9c0
-  __AUTH_CONST.__objc_const: 0x4e4c8
+  __AUTH_CONST.__cfstring: 0xda00
+  __AUTH_CONST.__objc_const: 0x4ea10
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x1384
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x8ed0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 530D3DA7-4347-3C95-8DB0-D75C76EA4762
-  Functions: 7034
-  Symbols:   22711
-  CStrings:  8698
+  UUID: 5049E099-9C6B-3929-918D-DE1843549E6D
+  Functions: 7054
+  Symbols:   22777
+  CStrings:  8704
 
Symbols:
+ +[CEMSystemAppExceptionsDeclaration allowedPayloadKeys]
+ +[CEMSystemAppExceptionsDeclaration buildRequiredOnlyWithIdentifier:]
+ +[CEMSystemAppExceptionsDeclaration buildWithIdentifier:appsRatingExemptedBundleIDs:]
+ +[CEMSystemAppExceptionsDeclaration profileType]
+ +[CEMSystemAppExceptionsDeclaration registeredClassName]
+ +[CEMSystemAppExceptionsDeclaration registeredIdentifier]
+ +[CEMSystemAppExceptionsDeclaration restrictionPayloadKeys]
+ +[CEMSystemAppExceptionsDeclaration_Status allowedReasons]
+ +[CEMSystemAppExceptionsDeclaration_Status allowedStatusKeys]
+ +[CEMSystemAppExceptionsDeclaration_Status buildRequiredOnly]
+ +[CEMSystemAppExceptionsDeclaration_Status build]
+ -[CEMSystemAppExceptionsDeclaration .cxx_destruct]
+ -[CEMSystemAppExceptionsDeclaration activationLevel]
+ -[CEMSystemAppExceptionsDeclaration assetReferences]
+ -[CEMSystemAppExceptionsDeclaration copyWithZone:]
+ -[CEMSystemAppExceptionsDeclaration loadPayload:error:]
+ -[CEMSystemAppExceptionsDeclaration multipleAllowed]
+ -[CEMSystemAppExceptionsDeclaration mustBeSupervised]
+ -[CEMSystemAppExceptionsDeclaration payloadAppsRatingExemptedBundleIDs]
+ -[CEMSystemAppExceptionsDeclaration serializePayloadWithAssetProviders:]
+ -[CEMSystemAppExceptionsDeclaration setPayloadAppsRatingExemptedBundleIDs:]
+ -[CEMSystemAppExceptionsDeclaration_Status loadPayload:error:]
+ -[CEMSystemAppExceptionsDeclaration_Status serializePayload]
+ _OBJC_CLASS_$_CEMSystemAppExceptionsDeclaration
+ _OBJC_CLASS_$_CEMSystemAppExceptionsDeclaration_Status
+ _OBJC_IVAR_$_CEMSystemAppExceptionsDeclaration._payloadAppsRatingExemptedBundleIDs
+ _OBJC_METACLASS_$_CEMSystemAppExceptionsDeclaration
+ _OBJC_METACLASS_$_CEMSystemAppExceptionsDeclaration_Status
+ __OBJC_$_CLASS_METHODS_CEMSystemAppExceptionsDeclaration
+ __OBJC_$_CLASS_METHODS_CEMSystemAppExceptionsDeclaration_Status
+ __OBJC_$_CLASS_PROP_LIST_CEMSystemAppExceptionsDeclaration
+ __OBJC_$_CLASS_PROP_LIST_CEMSystemAppExceptionsDeclaration_Status
+ __OBJC_$_INSTANCE_METHODS_CEMSystemAppExceptionsDeclaration
+ __OBJC_$_INSTANCE_METHODS_CEMSystemAppExceptionsDeclaration_Status
+ __OBJC_$_INSTANCE_VARIABLES_CEMSystemAppExceptionsDeclaration
+ __OBJC_$_PROP_LIST_CEMSystemAppExceptionsDeclaration
+ __OBJC_CLASS_PROTOCOLS_$_CEMSystemAppExceptionsDeclaration
+ __OBJC_CLASS_RO_$_CEMSystemAppExceptionsDeclaration
+ __OBJC_CLASS_RO_$_CEMSystemAppExceptionsDeclaration_Status
+ __OBJC_METACLASS_RO_$_CEMSystemAppExceptionsDeclaration
+ __OBJC_METACLASS_RO_$_CEMSystemAppExceptionsDeclaration_Status
+ ___55-[CEMSystemAppExceptionsDeclaration loadPayload:error:]_block_invoke
+ ___72-[CEMSystemAppExceptionsDeclaration serializePayloadWithAssetProviders:]_block_invoke
+ _objc_msgSend$buildWithIdentifier:appsRatingExemptedBundleIDs:
- +[CEMSystemRatingsDeclaration buildWithIdentifier:withRatingRegion:withRatingApps:withRatingMovies:withRatingTVShows:withAllowExplicitContent:withAllowShowingUndownloadedTV:withAllowShowingUndownloadedMovies:withAppsRatingExemptedBundleIDs:]
- -[CEMSystemRatingsDeclaration payloadAppsRatingExemptedBundleIDs]
- -[CEMSystemRatingsDeclaration setPayloadAppsRatingExemptedBundleIDs:]
- _OBJC_IVAR_$_CEMSystemRatingsDeclaration._payloadAppsRatingExemptedBundleIDs
- ___49-[CEMSystemRatingsDeclaration loadPayload:error:]_block_invoke
- ___66-[CEMSystemRatingsDeclaration serializePayloadWithAssetProviders:]_block_invoke
CStrings:
+ "CEMSystemAppExceptionsDeclaration"
+ "CEMSystemAppExceptionsDeclaration_Status"
+ "buildWithIdentifier:appsRatingExemptedBundleIDs:"
+ "com.apple.configuration.system.app.exceptions"
- "buildWithIdentifier:withRatingRegion:withRatingApps:withRatingMovies:withRatingTVShows:withAllowExplicitContent:withAllowShowingUndownloadedTV:withAllowShowingUndownloadedMovies:withAppsRatingExemptedBundleIDs:"

```
