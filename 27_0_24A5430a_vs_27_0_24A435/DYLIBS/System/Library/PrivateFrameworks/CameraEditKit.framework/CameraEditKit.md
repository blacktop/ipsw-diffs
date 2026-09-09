## CameraEditKit

> `/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`

```diff

 4177.22.4.0.0
-  __TEXT.__text: 0x422d8
-  __TEXT.__objc_methlist: 0x5704
+  __TEXT.__text: 0x432c4
+  __TEXT.__objc_methlist: 0x5844
   __TEXT.__const: 0xce4
-  __TEXT.__cstring: 0x143e
+  __TEXT.__cstring: 0x162e
   __TEXT.__oslogstring: 0x69c
   __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__constg_swiftt: 0x5d4

   __TEXT.__swift5_capture: 0x6c
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x13c8
+  __TEXT.__unwind_info: 0x1420
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd60
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0xda8
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34a0
+  __DATA_CONST.__objc_selrefs: 0x3530
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x2f8
-  __DATA_CONST.__got: 0x528
-  __AUTH_CONST.__const: 0x728
-  __AUTH_CONST.__cfstring: 0x1760
-  __AUTH_CONST.__objc_const: 0x9260
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_arraydata: 0x358
+  __DATA_CONST.__got: 0x548
+  __AUTH_CONST.__const: 0x768
+  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__objc_const: 0x93c8
   __AUTH_CONST.__objc_doubleobj: 0x1d0
-  __AUTH_CONST.__objc_intobj: 0x588
+  __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x980
-  __AUTH.__objc_data: 0x14a0
+  __AUTH_CONST.__auth_got: 0x988
+  __AUTH.__objc_data: 0x14f0
   __AUTH.__data: 0x1c0
-  __DATA.__objc_ivar: 0x708
+  __DATA.__objc_ivar: 0x714
   __DATA.__data: 0xc48
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2059
-  Symbols:   4732
-  CStrings:  267
+  Functions: 2093
+  Symbols:   4797
+  CStrings:  284
 
Symbols:
+ +[CEKTextureStyle _cmiPresetNameForPreset:]
+ +[CEKTextureStyle _defaultValuesForPreset:intensity:grain:]
+ +[CEKTextureStyle _indexForPresetString:]
+ +[CEKTextureStyle canCustomizeGrainForPreset:]
+ +[CEKTextureStyle canCustomizeIntensityForPreset:]
+ +[CEKTextureStyle defaultStyles]
+ +[CEKTextureStyle identityStyle]
+ +[CEKTextureStyle persistenceStringForPreset:]
+ +[CEKTextureStyle presetFromPersistenceString:success:]
+ +[CEKTextureStyle styleWithDictionary:referenceStyle:error:]
+ -[CEKTextureStyle _analyticsDictionary]
+ -[CEKTextureStyle analyticsDictionaryForCapture]
+ -[CEKTextureStyle analyticsDictionaryForPreferences]
+ -[CEKTextureStyle description]
+ -[CEKTextureStyle dictionaryRepresentationUsingReferenceStyle:]
+ -[CEKTextureStyle grain]
+ -[CEKTextureStyle hash]
+ -[CEKTextureStyle initWithPreset:]
+ -[CEKTextureStyle initWithPreset:intensity:grain:]
+ -[CEKTextureStyle intensity]
+ -[CEKTextureStyle isCustomizable]
+ -[CEKTextureStyle isCustomized]
+ -[CEKTextureStyle isEqual:]
+ -[CEKTextureStyle isEqualToTextureStyle:]
+ -[CEKTextureStyle preset]
+ _AVGQGYSWMQKMTMQOUYQ2AKUCKEN6AA
+ _AVGestaltGetIntegerAnswerWithDefault
+ _CEKDebugStringForTextureStylePreset
+ _CEKTextureStyleAllPresets
+ _CEKTextureStyleCameraAvailablePresets
+ _CEKTextureStyleSystemStylePresets
+ _CMITextureStylePresetNameFilmic
+ _CMITextureStylePresetNameGlowy
+ _CMITextureStylePresetNameSoft
+ _CMITextureStylePresetNameStandard
+ _CMITextureStylePresetNameStudio
+ _OBJC_CLASS_$_CEKTextureStyle
+ _OBJC_CLASS_$_CMITextureStyleTuningLookup
+ _OBJC_IVAR_$_CEKTextureStyle._grain
+ _OBJC_IVAR_$_CEKTextureStyle._intensity
+ _OBJC_IVAR_$_CEKTextureStyle._preset
+ _OBJC_METACLASS_$_CEKTextureStyle
+ __OBJC_$_CLASS_METHODS_CEKTextureStyle
+ __OBJC_$_CLASS_PROP_LIST_CEKTextureStyle
+ __OBJC_$_INSTANCE_METHODS_CEKTextureStyle
+ __OBJC_$_INSTANCE_VARIABLES_CEKTextureStyle
+ __OBJC_$_PROP_LIST_CEKTextureStyle
+ __OBJC_CLASS_RO_$_CEKTextureStyle
+ __OBJC_METACLASS_RO_$_CEKTextureStyle
+ ___32+[CEKTextureStyle identityStyle]_block_invoke
+ ___41+[CEKTextureStyle _indexForPresetString:]_block_invoke
+ ___41+[CEKTextureStyle _indexForPresetString:]_block_invoke_2
+ _objc_msgSend$_analyticsDictionary
+ _objc_msgSend$_cmiPresetNameForPreset:
+ _objc_msgSend$_defaultValuesForPreset:intensity:grain:
+ _objc_msgSend$canCustomizeGrainForPreset:
+ _objc_msgSend$canCustomizeIntensityForPreset:
+ _objc_msgSend$defaultStyleForCastType:textureStyleVersion:
+ _objc_msgSend$defaultTextureStyleForPresetName:
+ _objc_msgSend$grain
+ _objc_msgSend$initWithPreset:
+ _objc_msgSend$initWithPreset:intensity:grain:
+ _objc_msgSend$intensity
+ _objc_msgSend$isEqualToTextureStyle:
+ _objc_msgSend$preset
CStrings:
+ "Analog"
+ "CEKTextureStyleErrorDomain"
+ "Glowy"
+ "Grain"
+ "Intensity"
+ "People"
+ "Preset"
+ "Scene"
+ "TextureStyle(Preset:%@)"
+ "TextureStyle(Preset:%@, Intensity:%.2f, Grain:%.2f)"
+ "TextureStyleCustomized"
+ "TextureStyleGrain"
+ "TextureStyleIntensity"
+ "TextureStylePreset"
+ "Unexpected CEKTextureStyle dictionary structure, incorrect type for values of known keys"
+ "Unexpected CEKTextureStyle dictionary structure, incorrect value for PresetKey: no preset match found"
+ "Unexpected CEKTextureStyle dictionary structure, missing required keys"
```
