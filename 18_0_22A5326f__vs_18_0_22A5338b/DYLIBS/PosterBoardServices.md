## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-218.0.0.0.0
-  __TEXT.__text: 0x3e350
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x2b18
+219.100.0.0.0
+  __TEXT.__text: 0x40288
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x2d80
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x403e
-  __TEXT.__gcc_except_tab: 0x608
-  __TEXT.__oslogstring: 0x2169
-  __TEXT.__dlopen_cstrs: 0x172
-  __TEXT.__unwind_info: 0xd78
-  __TEXT.__objc_classname: 0x723
-  __TEXT.__objc_methname: 0x863d
-  __TEXT.__objc_methtype: 0x17d3
-  __TEXT.__objc_stubs: 0x53c0
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0xee0
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__cstring: 0x4354
+  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__oslogstring: 0x21cd
+  __TEXT.__dlopen_cstrs: 0x1c2
+  __TEXT.__unwind_info: 0xe18
+  __TEXT.__objc_classname: 0x78d
+  __TEXT.__objc_methname: 0x8c02
+  __TEXT.__objc_methtype: 0x183e
+  __TEXT.__objc_stubs: 0x5640
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19f0
+  __DATA_CONST.__objc_selrefs: 0x1af8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x190
-  __AUTH_CONST.__auth_got: 0x680
+  __DATA_CONST.__objc_superrefs: 0x1a8
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x2de0
-  __AUTH_CONST.__objc_const: 0xa560
+  __AUTH_CONST.__cfstring: 0x3040
+  __AUTH_CONST.__objc_const: 0xae98
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x378
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x398
   __DATA.__data: 0x560
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1350
-  Symbols:   1974
-  CStrings:  2118
+  Functions: 1403
+  Symbols:   2039
+  CStrings:  2205
 
Symbols:
+ _OBJC_CLASS_$_PRSMigrationDescriptor
+ _OBJC_CLASS_$_PRSMutableMigrationDescriptor
+ _OBJC_CLASS_$_PRSPosterUpdateDiscreteStylePayload
+ _OBJC_CLASS_$_PRSPosterUpdater
+ _OBJC_METACLASS_$_PRSMigrationDescriptor
+ _OBJC_METACLASS_$_PRSMutableMigrationDescriptor
+ _OBJC_METACLASS_$_PRSPosterUpdateDiscreteStylePayload
+ _OBJC_METACLASS_$_PRSPosterUpdater
+ _PFPosterRoleAmbient
+ _PFPosterRoleLockScreen
+ _objc_getAssociatedObject
+ _objc_setAssociatedObject
CStrings:
+ "-[PRSServer notePosterConfigurationUnderlyingModelDidChange:]"
+ "-[PRSServer runMigration:migrationDescriptor:completion:]"
+ "<%!{(MISSING)public}@:%!p(MISSING)> Activating %!l(MISSING)u clients"
+ "<%!{(MISSING)public}@:%!p(MISSING)> Activating client that connected earlier: %!@(MISSING)"
+ "Ambient role is inconsistent with provided updates."
+ "Class getPRPosterMutableConfiguredPropertiesClass(void)_block_invoke"
+ "Class getPRPosterPathUtilitiesClass(void)_block_invoke"
+ "Lockscreen role is inconsistent with provided updates."
+ "PRPosterMutableConfiguredProperties"
+ "PRPosterPathUtilities"
+ "PRSMigrationDescriptor"
+ "PRSMutableMigrationDescriptor"
+ "PRSPosterUpdateDiscreteStylePayload"
+ "PRSPosterUpdateTypeDimState"
+ "PRSPosterUpdateTypeHomeScreenSuggestedTintColor"
+ "PRSPosterUpdateTypeHomeScreenTintStyle"
+ "PRSPosterUpdater"
+ "PRSPosterUpdater.m"
+ "T@\"BSColor\",C,D,N"
+ "T@\"BSColor\",C,N,V_homeScreenTintColor"
+ "T@\"NSNumber\",C,D,N,GisHomeScreenDim"
+ "T@\"NSNumber\",C,N,GisHomeScreenDim,V_homeScreenDim"
+ "T@\"NSNumber\",R,N,V_luminance"
+ "T@\"NSNumber\",R,N,V_saturation"
+ "T@\"NSNumber\",R,N,V_variation"
+ "T@\"NSString\",C,D,N"
+ "T@\"NSString\",C,N,V_homeScreenIconSize"
+ "T@\"NSString\",C,N,V_homeScreenIconStyle"
+ "Vv24@0:8@\"NSUUID\"16"
+ "Vv36@0:8B16@20@?28"
+ "Vv40@0:8@\"NSNumber\"16@\"PRSMigrationDescriptor\"24@?<v@?@\"NSError\">32"
+ "_homeScreenDim"
+ "_homeScreenDim"
+ "_homeScreenIconSize"
+ "_homeScreenIconSize"
+ "_homeScreenIconStyle"
+ "_homeScreenIconStyle"
+ "_homeScreenTintColor"
+ "_homeScreenTintColor"
+ "_initWithWeakPath:"
+ "_luminance"
+ "_luminance"
+ "_saturation"
+ "_saturation"
+ "_variation"
+ "_variation"
+ "_weakPath"
+ "appendObject:withName:skipIfNil:"
+ "applyUpdateLocally:error:"
+ "applyUpdates:error:"
+ "applyUpdatesLocally:error:"
+ "canUpdatesBeAppliedLocally:"
+ "dataUsingEncoding:"
+ "defaultConfiguredPropertiesForRole:"
+ "homeScreenDim"
+ "homeScreenDim"
+ "homeScreenIconSize"
+ "homeScreenIconSize"
+ "homeScreenIconStyle"
+ "homeScreenIconStyle"
+ "homeScreenTintColor"
+ "homeScreenTintColor"
+ "initWithVariation:saturation:luminance:"
+ "instanceURL"
+ "isHomeScreenDim"
+ "loadConfiguredPropertiesForPath:error:"
+ "luminance"
+ "notePosterConfigurationUnderlyingModelDidChange:"
+ "path is no longer valid."
+ "posterUpdateHomeScreenAppearanceDimWithValue:"
+ "posterUpdateHomeScreenIconUserInterfaceStyle:"
+ "posterUpdateHomeScreenSuggestedTintColor:"
+ "posterUpdateHomeScreenTintForColor:"
+ "posterUpdateHomeScreenTintWithVariation:saturation:luminance:"
+ "posterUpdateShouldUseLargeHomeScreenIcons:"
+ "runMigration:migrationDescriptor:completion:"
+ "saturation"
+ "server:notePosterConfigurationUnderlyingModelDidChange:"
+ "server:runMigration:migrationDescriptor:completion:"
+ "setHomeScreenDim:"
+ "setHomeScreenIconSize:"
+ "setHomeScreenIconStyle:"
+ "setHomeScreenTintColor:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit"
+ "storeConfiguredPropertiesForPath:configuredProperties:error:"
+ "update type is not valid for PRSPosterUpdater."
+ "updaterForPath:"
+ "variation"
+ "void *PosterKitLibrary(void)"
- "-[PRSServer runMigration:completion:]"
- "server:runMigration:completion:"

```
