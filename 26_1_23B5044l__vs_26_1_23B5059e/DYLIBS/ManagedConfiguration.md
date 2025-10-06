## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2430.0.0.0.0
-  __TEXT.__text: 0xf8588
+2432.40.1.0.0
+  __TEXT.__text: 0xf88e0
   __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0xb16c
+  __TEXT.__objc_methlist: 0xb1dc
   __TEXT.__const: 0x13c4
-  __TEXT.__cstring: 0x17b87
+  __TEXT.__cstring: 0x17c1c
   __TEXT.__oslogstring: 0x8fbc
   __TEXT.__gcc_except_tab: 0x10c4
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x3128
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0x1e06b
+  __TEXT.__objc_methname: 0x1e267
   __TEXT.__objc_methtype: 0x236f
-  __TEXT.__objc_stubs: 0xdba0
+  __TEXT.__objc_stubs: 0xdc20
   __DATA_CONST.__got: 0xa88
-  __DATA_CONST.__const: 0x4d00
+  __DATA_CONST.__const: 0x4d20
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cb0
+  __DATA_CONST.__objc_selrefs: 0x5cf8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH_CONST.__const: 0x2090
-  __AUTH_CONST.__cfstring: 0x191a0
-  __AUTH_CONST.__objc_const: 0xd678
+  __AUTH_CONST.__cfstring: 0x19240
+  __AUTH_CONST.__objc_const: 0xd708
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x2328
-  __DATA.__objc_ivar: 0x97c
+  __DATA.__objc_ivar: 0x988
   __DATA.__data: 0xc30
   __DATA.__bss: 0xc59
   __DATA.__common: 0x28

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED19B09F-FAAE-3317-A04E-8F536B9BCD05
-  Functions: 5632
-  Symbols:   17347
-  CStrings:  12193
+  UUID: D0A8D507-DF82-3E62-9C81-0461D4CE0692
+  Functions: 5641
+  Symbols:   17376
+  CStrings:  12218
 
Symbols:
+ -[MCProfileConnection(Misc) isAccessibilityLiveCaptionsAllowed]
+ -[MCProfileConnection(Misc) isAccessibilityReaderAllowed]
+ -[MCProfileConnection(Misc) isAccessibilityReaderSuggestionsAllowed]
+ -[MCSingleAppModeConfiguration allowAccessibilityLiveCaptions]
+ -[MCSingleAppModeConfiguration allowAccessibilityReaderSuggestions]
+ -[MCSingleAppModeConfiguration allowAccessibilityReader]
+ -[MCSingleAppModeConfiguration setAllowAccessibilityLiveCaptions:]
+ -[MCSingleAppModeConfiguration setAllowAccessibilityReader:]
+ -[MCSingleAppModeConfiguration setAllowAccessibilityReaderSuggestions:]
+ GCC_except_table283
+ _MCFeatureAccessibilityLiveCaptionsAllowed
+ _MCFeatureAccessibilityReaderAllowed
+ _MCFeatureAccessibilityReaderSuggestionsAllowed
+ _MCFeatureLegacyAppsRatingExemptedBundleIDs
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowAccessibilityLiveCaptions
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowAccessibilityReader
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowAccessibilityReaderSuggestions
+ ___block_literal_global.676
+ ___block_literal_global.696
+ ___block_literal_global.745
+ ___block_literal_global.781
+ ___block_literal_global.786
+ ___block_literal_global.791
+ ___block_literal_global.796
+ ___block_literal_global.801
+ _objc_msgSend$MCDeleteBoolRestriction:
+ _objc_msgSend$allowAccessibilityLiveCaptions
+ _objc_msgSend$allowAccessibilityReader
+ _objc_msgSend$allowAccessibilityReaderSuggestions
- GCC_except_table280
- ___block_literal_global.673
- ___block_literal_global.693
- ___block_literal_global.742
- ___block_literal_global.778
- ___block_literal_global.783
- ___block_literal_global.788
- ___block_literal_global.793
- ___block_literal_global.798
CStrings:
+ "FEATURE_APPS_RATING_EXEMPTED"
+ "TB,N,V_allowAccessibilityLiveCaptions"
+ "TB,N,V_allowAccessibilityReader"
+ "TB,N,V_allowAccessibilityReaderSuggestions"
+ "_allowAccessibilityLiveCaptions"
+ "_allowAccessibilityReader"
+ "_allowAccessibilityReaderSuggestions"
+ "allowAccessibilityLiveCaptions"
+ "allowAccessibilityReader"
+ "allowAccessibilityReaderSuggestions"
+ "isAccessibilityLiveCaptionsAllowed"
+ "isAccessibilityReaderAllowed"
+ "isAccessibilityReaderSuggestionsAllowed"
+ "ratingAppsExemptedBundleIDs"
+ "setAllowAccessibilityLiveCaptions:"
+ "setAllowAccessibilityReader:"
+ "setAllowAccessibilityReaderSuggestions:"

```
