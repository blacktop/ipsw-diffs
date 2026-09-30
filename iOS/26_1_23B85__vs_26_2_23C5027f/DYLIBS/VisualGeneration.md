## VisualGeneration

> `/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration`

```diff

-92.13.1.0.0
-  __TEXT.__text: 0x28fe3c
-  __TEXT.__auth_stubs: 0x4dc0
+92.13.2.0.0
+  __TEXT.__text: 0x28fddc
+  __TEXT.__auth_stubs: 0x4e40
   __TEXT.__objc_methlist: 0xd7c
-  __TEXT.__const: 0x1f270
-  __TEXT.__cstring: 0x8b1f
-  __TEXT.__swift5_typeref: 0x7670
+  __TEXT.__const: 0x1f290
+  __TEXT.__cstring: 0x912f
+  __TEXT.__swift5_typeref: 0x769c
   __TEXT.__swift5_fieldmd: 0x8388
   __TEXT.__constg_swiftt: 0x7158
   __TEXT.__swift5_builtin: 0x3d4
-  __TEXT.__swift5_reflstr: 0x8103
-  __TEXT.__swift5_assocty: 0xb68
+  __TEXT.__swift5_reflstr: 0x8113
+  __TEXT.__swift5_assocty: 0xb80
   __TEXT.__swift5_protos: 0x14c
-  __TEXT.__swift5_proto: 0x1998
+  __TEXT.__swift5_proto: 0x199c
   __TEXT.__swift5_types: 0x92c
-  __TEXT.__swift5_capture: 0x1008
-  __TEXT.__oslogstring: 0x4ead
-  __TEXT.__swift_as_entry: 0x6c8
-  __TEXT.__swift_as_ret: 0x578
+  __TEXT.__swift5_capture: 0xfdc
+  __TEXT.__oslogstring: 0x4fed
+  __TEXT.__swift_as_entry: 0x6cc
+  __TEXT.__swift_as_ret: 0x57c
   __TEXT.__swift5_mpenum: 0x15c
-  __TEXT.__unwind_info: 0x9858
-  __TEXT.__eh_frame: 0x1865c
+  __TEXT.__unwind_info: 0x9848
+  __TEXT.__eh_frame: 0x18654
   __TEXT.__objc_classname: 0xe1
   __TEXT.__objc_methname: 0x35a5
   __TEXT.__objc_methtype: 0x1c82
-  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__got: 0xe40
   __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1000
   __DATA_CONST.__objc_protorefs: 0x70
-  __AUTH_CONST.__auth_got: 0x26e0
-  __AUTH_CONST.__const: 0x13fb0
+  __AUTH_CONST.__auth_got: 0x2720
+  __AUTH_CONST.__const: 0x141f8
   __AUTH_CONST.__objc_const: 0x5478
   __AUTH.__objc_data: 0x9c0
   __AUTH.__data: 0x5538
-  __DATA.__data: 0x5140
-  __DATA.__bss: 0x26880
+  __DATA.__data: 0x5168
+  __DATA.__bss: 0x26900
   __DATA.__common: 0x220
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x1e50

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D38A3C3-4340-3B3A-94BA-44A948016CC5
-  Functions: 11348
-  Symbols:   4003
-  CStrings:  2102
+  UUID: 6075A6FF-B364-350A-833D-58F29B19DE84
+  Functions: 11362
+  Symbols:   4013
+  CStrings:  2104
 
Symbols:
+ ___swift_memcpy107_8
+ _associated conformance 16VisualGeneration30ExternalGeneratorConfigurationV18AppearanceModifierOs12CaseIterableAA8AllCasessAFP_Sl
+ _block_copy_helper.22
+ _block_copy_helper.29
+ _block_copy_helper.36
+ _block_copy_helper.43
+ _block_copy_helper.51
+ _block_copy_helper.58
+ _block_descriptor.24
+ _block_descriptor.31
+ _block_descriptor.38
+ _block_descriptor.45
+ _block_descriptor.53
+ _block_descriptor.60
+ _block_destroy_helper.23
+ _block_destroy_helper.30
+ _block_destroy_helper.37
+ _block_destroy_helper.44
+ _block_destroy_helper.52
+ _block_destroy_helper.59
+ _symbolic Say_____G 16VisualGeneration30ExternalGeneratorConfigurationV18AppearanceModifierO
+ _symbolic Say___________tGz_Xx So8_NSRangeV 16VisualGeneration15EntityExtractorC07GenericD0C
+ _symbolic _____Sg 29GenerativeFunctionsFoundation23TemplateVariableBindingV0E10DefinitionV
+ _symbolic _____Sg 29GenerativeFunctionsFoundation23TemplateVariableBindingV0E5ValueO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 29GenerativeFunctionsFoundation23TemplateVariableBindingV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 29GenerativeFunctionsFoundation23TemplateVariableBindingV0H10DefinitionV016ExpandableOptionJ0V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 29GenerativeFunctionsFoundation23TemplateVariableBindingV21ExpandableOptionValueV
- ___swift_memcpy106_8
- ___swift_project_boxed_opaque_existential_0Tm
- _block_copy_helper.28
- _block_copy_helper.35
- _block_copy_helper.42
- _block_copy_helper.50
- _block_copy_helper.57
- _block_descriptor.30
- _block_descriptor.37
- _block_descriptor.44
- _block_descriptor.52
- _block_descriptor.59
- _block_destroy_helper.29
- _block_destroy_helper.36
- _block_destroy_helper.43
- _block_destroy_helper.51
- _block_destroy_helper.58
- _symbolic SDySSSo27SCMLImageSanitizationSignalCG
- _symbolic _____y_____G s23_ContiguousArrayStorageC 16VisualGeneration15ForensicsReportV
CStrings:
+ "\nIf images are provided as input, use them to influence the generated image.\n\n{% if gender != \"none\" or skinTone != \"none\" or hairstyle != \"none\" or facialHair != \"none\" or additionalDescription != \"none\" or accessories != \"none\" %}\nUse the following instructions to modify the generated image.\nThe generated image must feature a person.\n\n### Use the following description to modify the appearance of the person in the generated image\n{% if gender != \"none\" or skinTone != \"none\" or hairstyle != \"none\" or facialHair != \"none\" or additionalDescription != \"none\" or accessories != \"none\" %}The person in the new image should adhere to the following description: {% endif %}\n{% unless gender == \"none\" %}a {{ gender }} person{% endunless %}\n{% unless skinTone == \"none\" %}they have {{ skinTone }} skin tone{% endunless %}\n{% unless hairstyle == \"none\" %}with {{ hairstyle }} hairstyle{% endunless %}\n{% unless facialHair == \"none\" %}with {{ facialHair }} facial hair{% endunless %}\n{% unless additionalDescription == \"none\" %}the person should have {{ additionalDescription }}{% endunless %}\n{% unless accessories == \"none\" %}with {{ accessories }} accessories{% endunless %}\n{% else %}\nDo not add people or other elements unless explicitly requested.\n{% endif %}\n\n{%unless themes contains \"none\" and styles contains \"none\"%}### Theme and Style Modifiers (may not be present if none are selected){% endunless %}\n{%unless themes contains \"none\"%}The generated image should contain themes of {{themes | join: \", \"}} {% endunless %}\n{%unless styles contains \"none\"%}Use the following description for the style of the image: {{styles | join: \", \"}}{% endunless %}"
+ "Parameter values are being specified in a list, but there are no parameter options provided to match against."
+ "Prescription Glasses"
+ "The generated image should have the following: "
+ "localDevelopmentConfiguration = %{bool}d, visualGenerationIDTemplateID = \"%s\""
+ "sanitizePrompt called but skipped due to configuration: allowTextRejection = %{bool}d, reportForensics = %{bool}d)"
+ "visualGeneration.testTemplateVariables"
- " The generated image should be of: "
- " Use the following description for the style of the image: "
- "If images are provided as input, use them to influence the generated image."
- "headwear"
- "rejectedConcepts"

```
