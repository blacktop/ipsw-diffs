## PosterPlatformSupport

> `/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport`

```diff

-355.2.12.101.0
-  __TEXT.__text: 0x1db0
+355.3.7.0.0
+  __TEXT.__text: 0x1fc4
   __TEXT.__objc_methlist: 0x180
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__cstring: 0x202
+  __TEXT.__cstring: 0x223
   __TEXT.__oslogstring: 0x3fe
   __TEXT.__unwind_info: 0x148
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x1d0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 59
-  Symbols:   165
-  CStrings:  36
+  Symbols:   168
+  CStrings:  39
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _PFFeatureEnabled
+ _PFPosterRolesKnownAmbientDomino
Functions:
~ ___102-[PPSHostConfigurationManager updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:]_block_invoke : 124 -> 156
~ -[PPSHostConfigurationManager defaultsKeyForRole:] : 12 -> 228
~ +[PPSPlatformPolicyManager snapshottingSupportedForRole:] : 120 -> 188
~ +[PPSPlatformPolicyManager proactiveGallerySupportedForRole:] : 120 -> 188
~ +[PPSPlatformPolicyManager ambientPosterAutocreationSupportedForProvider:] : 28 -> 116
~ ___58+[PPSPlatformPolicyManager rolesRequiringProactiveGallery]_block_invoke : 104 -> 164
CStrings:
+ "_disabled"
+ "_enabled"
+ "_standByInfra"
```
