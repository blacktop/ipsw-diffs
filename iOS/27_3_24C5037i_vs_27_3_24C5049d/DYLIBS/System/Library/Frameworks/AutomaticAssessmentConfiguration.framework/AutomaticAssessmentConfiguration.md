## AutomaticAssessmentConfiguration

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration`

```diff

-56.60.2.0.0
-  __TEXT.__text: 0x843c
-  __TEXT.__objc_methlist: 0xa94
+56.60.5.0.0
+  __TEXT.__text: 0x8b20
+  __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0x3ae
-  __TEXT.__cstring: 0x438
+  __TEXT.__cstring: 0x4a3
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_reflstr: 0x22

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x350
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x798
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__objc_selrefs: 0x7c0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x68
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x13d0
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0x15a8
   __AUTH_CONST.__auth_got: 0x338
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x134
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x180
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 303
-  Symbols:   524
-  CStrings:  21
+  Functions: 326
+  Symbols:   567
+  CStrings:  23
 
Symbols:
+ +[AEAssessmentWebClip instanceFromApplicationDescriptor:]
+ +[AEAssessmentWebClipConfiguration instanceFromIndividualConfiguration:]
+ +[AEAssessmentWebClipConfiguration new]
+ -[AEAssessmentConfiguration configurationsByWebClip]
+ -[AEAssessmentConfiguration removeWebClip:]
+ -[AEAssessmentConfiguration setBackingConfigurationsByWebClip:]
+ -[AEAssessmentConfiguration setConfiguration:forWebClip:]
+ -[AEAssessmentWebClip .cxx_destruct]
+ -[AEAssessmentWebClip applicationDescriptor]
+ -[AEAssessmentWebClip copyWithZone:]
+ -[AEAssessmentWebClip description]
+ -[AEAssessmentWebClip hash]
+ -[AEAssessmentWebClip initWithWebClipIdentifier:]
+ -[AEAssessmentWebClip isEqual:]
+ -[AEAssessmentWebClip isEqualToWebClip:]
+ -[AEAssessmentWebClip webClipIdentifier]
+ -[AEAssessmentWebClipConfiguration copyWithZone:]
+ -[AEAssessmentWebClipConfiguration hash]
+ -[AEAssessmentWebClipConfiguration individualConfiguration]
+ -[AEAssessmentWebClipConfiguration init]
+ -[AEAssessmentWebClipConfiguration isEqual:]
+ _OBJC_CLASS_$_AEAssessmentWebClip
+ _OBJC_CLASS_$_AEAssessmentWebClipConfiguration
+ _OBJC_IVAR_$_AEAssessmentConfiguration._backingConfigurationsByWebClip
+ _OBJC_IVAR_$_AEAssessmentWebClip._webClipIdentifier
+ _OBJC_METACLASS_$_AEAssessmentWebClip
+ _OBJC_METACLASS_$_AEAssessmentWebClipConfiguration
+ _OUTLINED_FUNCTION_2
+ __OBJC_$_CLASS_METHODS_AEAssessmentWebClip
+ __OBJC_$_CLASS_METHODS_AEAssessmentWebClipConfiguration
+ __OBJC_$_INSTANCE_METHODS_AEAssessmentWebClip
+ __OBJC_$_INSTANCE_METHODS_AEAssessmentWebClipConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AEAssessmentWebClip
+ __OBJC_$_PROP_LIST_AEAssessmentWebClip
+ __OBJC_$_PROP_LIST_AEAssessmentWebClipConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AEAssessmentWebClip
+ __OBJC_CLASS_PROTOCOLS_$_AEAssessmentWebClipConfiguration
+ __OBJC_CLASS_RO_$_AEAssessmentWebClip
+ __OBJC_CLASS_RO_$_AEAssessmentWebClipConfiguration
+ __OBJC_METACLASS_RO_$_AEAssessmentWebClip
+ __OBJC_METACLASS_RO_$_AEAssessmentWebClipConfiguration
+ ___49-[AEAssessmentConfiguration configurationWrapper]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e70_v32?0"AEAssessmentWebClip"8"AEAssessmentWebClipConfiguration"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e87_v32?0"AEAssessmentApplicationDescriptor"8"AEAssessmentIndividualConfiguration"16^B24ls32l8s40l8s48l8
- ___block_descriptor_48_e8_32s40s_e87_v32?0"AEAssessmentApplicationDescriptor"8"AEAssessmentIndividualConfiguration"16^B24ls32l8s40l8
CStrings:
+ "<%@: %p { webClipIdentifier = %@ }>"
+ "v32@?0@\"AEAssessmentWebClip\"8@\"AEAssessmentWebClipConfiguration\"16^B24"
```
