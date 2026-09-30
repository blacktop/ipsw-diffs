## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI`

```diff

-975.0.0.0.0
-  __TEXT.__text: 0x109388
+975.2.0.0.0
+  __TEXT.__text: 0x109640
   __TEXT.__auth_stubs: 0x2f80
   __TEXT.__delay_stubs: 0x140
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0xb488
-  __TEXT.__const: 0x92f8
+  __TEXT.__const: 0x9328
   __TEXT.__gcc_except_tab: 0x1a30
-  __TEXT.__cstring: 0x2b5e3
+  __TEXT.__cstring: 0x2b683
   __TEXT.__oslogstring: 0x200
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__swift5_typeref: 0x3a0

   __TEXT.__objc_methtype: 0x6b07
   __TEXT.__objc_stubs: 0x10fc0
   __DATA_CONST.__got: 0xc00
-  __DATA_CONST.__const: 0x1b6630
+  __DATA_CONST.__const: 0x1b6648
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 6249
   Symbols:   13337
-  CStrings:  10905
+  CStrings:  10908
 
Functions:
~ -[CUINamedRenditionInfo attributePresent:withValue:] : 1556 -> 1628
~ ___69-[_CSIRenditionBlockData expandCSIBitmapData:fromSlice:makeReadOnly:]_block_invoke : 788 -> 848
~ -[CUINamedRenditionInfo incrementIndex:inValues:forAttribute:] : 3176 -> 3320
~ -[CUINamedRenditionInfo setAttributePresent:withValue:] : 1552 -> 1624
~ -[CUINamedRenditionInfo decrementValue:forAttribute:] : 3104 -> 3248
~ _CUIRenditionKeyInitializeAttributeIndexWithKeyFormat : 280 -> 284
~ ___CUISubtypeFromIndex : 352 -> 396
~ -[CUINamedRenditionInfo clearAttributePresent:withValue:] : 1552 -> 1624
~ +[CUINamedRenditionInfo subtypeToIndexWithPlatform:andInput:] : 1288 -> 1360
~ _CUIValidateIdiomSubtypes : 656 -> 668
CStrings:
+ "APPLE11"
+ "CoreUI: Truncated '%s' compressed image block data name:'%s' pixelFormat:%d (rows %d rowbytes %zu, %zu bytes short)"
+ "kCoreThemeFeatureSetMetalGPUFamily11"
```
