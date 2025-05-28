## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

```diff

-1543.7.1.0.0
-  __TEXT.__text: 0x25c8c
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x1bc8
-  __TEXT.__const: 0x710
-  __TEXT.__cstring: 0xe09
-  __TEXT.__oslogstring: 0x1218
+1552.2.4.3.0
+  __TEXT.__text: 0x262c0
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x1bd8
+  __TEXT.__const: 0x730
+  __TEXT.__cstring: 0xe85
+  __TEXT.__oslogstring: 0x129b
   __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__unwind_info: 0x9e8
-  __TEXT.__objc_classname: 0x55c
-  __TEXT.__objc_methname: 0x6bd4
-  __TEXT.__objc_methtype: 0x135c
-  __TEXT.__objc_stubs: 0x5800
+  __TEXT.__unwind_info: 0xa00
+  __TEXT.__objc_classname: 0x571
+  __TEXT.__objc_methname: 0x6c24
+  __TEXT.__objc_methtype: 0x1394
+  __TEXT.__objc_stubs: 0x57e0
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0xe58
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__const: 0xe98
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x47a0
-  __DATA_CONST.__objc_selrefs: 0x1a00
+  __DATA_CONST.__objc_const: 0x4868
+  __DATA_CONST.__objc_selrefs: 0x1a08
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__cfstring: 0xe60
+  __AUTH_CONST.__cfstring: 0xee0
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x378
-  __AUTH_CONST.__objc_const: 0xc08
+  __AUTH_CONST.__objc_const: 0xc50
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH.__objc_data: 0x8c0
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH.__objc_data: 0x910
   __DATA.__objc_classrefs: 0x2e0
   __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x54c
+  __DATA.__objc_ivar: 0x558
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 821
-  Symbols:   3497
-  CStrings:  1774
+  Symbols:   3507
+  CStrings:  1786
 
Symbols:
+ -[PKSpotlightCardView initWithDiffuse:contentInsets:averageColor:]
+ -[PKSpotlightCardView isLight]
+ -[PKTexturedCardRenderer initWithStyle:renderLoop:diffuse:insets:]
+ GCC_except_table42
+ GCC_except_table60
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table95
+ _OBJC_CLASS_$_PKSpotlightCardView
+ _OBJC_IVAR_$_PKSpotlightCardView._light
+ _OBJC_IVAR_$_PKTexturedCardRenderer._diffuseInsets
+ _OBJC_IVAR_$_PKTexturedCardView._limitZAngle
+ _OBJC_METACLASS_$_PKSpotlightCardView
+ _PKColorGetRelativeLuminance
+ __OBJC_$_INSTANCE_METHODS_PKSpotlightCardView
+ __OBJC_$_INSTANCE_VARIABLES_PKSpotlightCardView
+ __OBJC_$_PROP_LIST_PKSpotlightCardView
+ __OBJC_CLASS_RO_$_PKSpotlightCardView
+ __OBJC_METACLASS_RO_$_PKSpotlightCardView
+ ___39-[PKTexturedCardRenderer renderAtTime:]_block_invoke.69
+ ___39-[PKTexturedCardRenderer renderAtTime:]_block_invoke.70
+ ___66-[PKSpotlightCardView initWithDiffuse:contentInsets:averageColor:]_block_invoke
+ ___block_descriptor_73_e51_"PKTexturedCardRenderer"16?0"PKMetalRenderLoop"8l
+ _acosf
- -[PKGlyphView _layoutContentLayer:ringFrame:]
- -[PKTexturedCardRenderer _initWithStyle:renderLoop:diffuseLoader:metalnessLoader:normalLoader:].cold.2
- -[PKTexturedCardRenderer _initWithStyle:renderLoop:diffuseLoader:metalnessLoader:normalLoader:].cold.3
- GCC_except_table44
- GCC_except_table61
- GCC_except_table73
- GCC_except_table96
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- ___39-[PKTexturedCardRenderer renderAtTime:]_block_invoke.57
- ___39-[PKTexturedCardRenderer renderAtTime:]_block_invoke.58
- _objc_msgSend$_layoutContentLayer:ringFrame:
CStrings:
+ "#'B"
+ "@64@0:8^{CGImage=}16{PKEdgeInsets=dddd}24^{CGColor=}56"
+ "PKSpotlightCardView"
+ "PKTexturedCardRenderer (%p:%ld): could not load diffuse texture."
+ "PKTexturedCardRenderer (%p:%ld): could not load fragment function."
+ "PKTexturedCardRenderer (%p:%ld): could not load metal library - %{public}@."
+ "PKTexturedCardRenderer (%p:%ld): could not load metalness texture."
+ "PKTexturedCardRenderer (%p:%ld): could not load normal texture."
+ "PKTexturedCardRenderer (%p:%ld): could not load pipeline - %{public}@."
+ "PKTexturedCardRenderer (%p:%ld): required textures missing - invalidating."
+ "Spotlight-Dark-CardView"
+ "Spotlight-Light-CardView"
+ "TB,R,N,GisLight,V_light"
+ "_diffuseInsets"
+ "_light"
+ "_limitZAngle"
+ "initWithDiffuse:contentInsets:averageColor:"
+ "isLight"
+ "texturedCard_fragment_spotlight_dark"
+ "texturedCard_fragment_spotlight_light"
+ "{PKEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "#)"
- "PKTexturedCardRenderer: could not load diffuse texture."
- "PKTexturedCardRenderer: could not load fragment function for style %ld."
- "PKTexturedCardRenderer: could not load metal library - %@."
- "PKTexturedCardRenderer: could not load metalness texture."
- "PKTexturedCardRenderer: could not load normal texture."
- "PKTexturedCardRenderer: could not load pipeline - %@."
- "_layoutContentLayer:ringFrame:"
- "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"

```
