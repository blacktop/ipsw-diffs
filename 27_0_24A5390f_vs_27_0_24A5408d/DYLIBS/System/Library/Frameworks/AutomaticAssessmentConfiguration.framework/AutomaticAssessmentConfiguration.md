## AutomaticAssessmentConfiguration

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x7ae8
-  __TEXT.__objc_methlist: 0x894
+56.0.3.0.0
+  __TEXT.__text: 0x8800
+  __TEXT.__objc_methlist: 0xa7c
   __TEXT.__const: 0x3ae
-  __TEXT.__cstring: 0x34f
+  __TEXT.__cstring: 0x438
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_reflstr: 0x22

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__unwind_info: 0x260
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f0
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__objc_selrefs: 0x788
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0x130
   __AUTH_CONST.__const: 0x68
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x1040
+  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__objc_const: 0x13a0
   __AUTH_CONST.__auth_got: 0x338
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x108
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x180
   __DATA.__bss: 0x490
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 258
-  Symbols:   638
-  CStrings:  18
+  Functions: 301
+  Symbols:   722
+  CStrings:  21
 
Symbols:
+ +[AEAssessmentBinaryExecutable instanceFromApplicationDescriptor:]
+ +[AEAssessmentBinaryExecutableConfiguration instanceFromIndividualConfiguration:]
+ +[AEAssessmentBinaryExecutableConfiguration new]
+ -[AEAssessmentBinaryExecutable .cxx_destruct]
+ -[AEAssessmentBinaryExecutable applicationDescriptor]
+ -[AEAssessmentBinaryExecutable binaryExecutableURL]
+ -[AEAssessmentBinaryExecutable copyWithZone:]
+ -[AEAssessmentBinaryExecutable description]
+ -[AEAssessmentBinaryExecutable hash]
+ -[AEAssessmentBinaryExecutable initWithBinaryExecutableURL:]
+ -[AEAssessmentBinaryExecutable initWithBinaryExecutableURL:teamIdentifier:]
+ -[AEAssessmentBinaryExecutable initWithBinaryExecutableURL:teamIdentifier:requiresSignatureValidation:]
+ -[AEAssessmentBinaryExecutable isEqual:]
+ -[AEAssessmentBinaryExecutable isEqualToBinaryExecutable:]
+ -[AEAssessmentBinaryExecutable requiresSignatureValidation]
+ -[AEAssessmentBinaryExecutable setRequiresSignatureValidation:]
+ -[AEAssessmentBinaryExecutable teamIdentifier]
+ -[AEAssessmentBinaryExecutableConfiguration allowsNetworkAccess]
+ -[AEAssessmentBinaryExecutableConfiguration copyWithZone:]
+ -[AEAssessmentBinaryExecutableConfiguration description]
+ -[AEAssessmentBinaryExecutableConfiguration hash]
+ -[AEAssessmentBinaryExecutableConfiguration individualConfiguration]
+ -[AEAssessmentBinaryExecutableConfiguration init]
+ -[AEAssessmentBinaryExecutableConfiguration isEqual:]
+ -[AEAssessmentBinaryExecutableConfiguration isEqualToConfiguration:]
+ -[AEAssessmentBinaryExecutableConfiguration isRequired]
+ -[AEAssessmentBinaryExecutableConfiguration setAllowsNetworkAccess:]
+ -[AEAssessmentBinaryExecutableConfiguration setRequired:]
+ -[AEAssessmentConfiguration _allowsAccessibilityIntelligence]
+ -[AEAssessmentConfiguration _allowsVisualIntelligence]
+ -[AEAssessmentConfiguration _setAllowsAccessibilityIntelligence:]
+ -[AEAssessmentConfiguration _setAllowsVisualIntelligence:]
+ -[AEAssessmentConfiguration allowVirtualMachine]
+ -[AEAssessmentConfiguration allowsForceQuit]
+ -[AEAssessmentConfiguration configurationsByBinaryExecutable]
+ -[AEAssessmentConfiguration removeBinaryExecutable:]
+ -[AEAssessmentConfiguration setAllowVirtualMachine:]
+ -[AEAssessmentConfiguration setAllowsForceQuit:]
+ -[AEAssessmentConfiguration setBackingConfigurationsByBinaryExecutable:]
+ -[AEAssessmentConfiguration setConfiguration:forBinaryExecutable:]
+ _OBJC_CLASS_$_AEAssessmentBinaryExecutable
+ _OBJC_CLASS_$_AEAssessmentBinaryExecutableConfiguration
+ _OBJC_IVAR_$_AEAssessmentBinaryExecutable._binaryExecutableURL
+ _OBJC_IVAR_$_AEAssessmentBinaryExecutable._requiresSignatureValidation
+ _OBJC_IVAR_$_AEAssessmentBinaryExecutable._teamIdentifier
+ _OBJC_IVAR_$_AEAssessmentBinaryExecutableConfiguration._allowsNetworkAccess
+ _OBJC_IVAR_$_AEAssessmentBinaryExecutableConfiguration._required
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowsAccessibilityIntelligence
+ _OBJC_IVAR_$_AEAssessmentConfiguration.__allowsVisualIntelligence
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowVirtualMachine
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsForceQuit
+ _OBJC_IVAR_$_AEAssessmentConfiguration._backingConfigurationsByBinaryExecutable
+ _OBJC_METACLASS_$_AEAssessmentBinaryExecutable
+ _OBJC_METACLASS_$_AEAssessmentBinaryExecutableConfiguration
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CLASS_METHODS_AEAssessmentBinaryExecutable
+ __OBJC_$_CLASS_METHODS_AEAssessmentBinaryExecutableConfiguration
+ __OBJC_$_INSTANCE_METHODS_AEAssessmentBinaryExecutable
+ __OBJC_$_INSTANCE_METHODS_AEAssessmentBinaryExecutableConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AEAssessmentBinaryExecutable
+ __OBJC_$_INSTANCE_VARIABLES_AEAssessmentBinaryExecutableConfiguration
+ __OBJC_$_PROP_LIST_AEAssessmentBinaryExecutable
+ __OBJC_$_PROP_LIST_AEAssessmentBinaryExecutableConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AEAssessmentBinaryExecutable
+ __OBJC_CLASS_PROTOCOLS_$_AEAssessmentBinaryExecutableConfiguration
+ __OBJC_CLASS_RO_$_AEAssessmentBinaryExecutable
+ __OBJC_CLASS_RO_$_AEAssessmentBinaryExecutableConfiguration
+ __OBJC_METACLASS_RO_$_AEAssessmentBinaryExecutable
+ __OBJC_METACLASS_RO_$_AEAssessmentBinaryExecutableConfiguration
+ ___49-[AEAssessmentConfiguration configurationWrapper]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e88_v32?0"AEAssessmentBinaryExecutable"8"AEAssessmentBinaryExecutableConfiguration"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e87_v32?0"AEAssessmentApplicationDescriptor"8"AEAssessmentIndividualConfiguration"16^B24ls32l8s40l8
+ _objc_msgSend$_allowsAccessibilityIntelligence
+ _objc_msgSend$_allowsVisualIntelligence
+ _objc_msgSend$allowVirtualMachine
+ _objc_msgSend$allowsForceQuit
+ _objc_msgSend$binaryExecutableURL
+ _objc_msgSend$executablePath
+ _objc_msgSend$initWithBinaryExecutableURL:teamIdentifier:
+ _objc_msgSend$initWithBinaryExecutableURL:teamIdentifier:requiresSignatureValidation:
+ _objc_msgSend$initWithExecutablePath:teamIdentifier:requiresSignatureValidation:
+ _objc_msgSend$setAllowVirtualMachine:
+ _objc_msgSend$setAllowsForceQuit:
+ _objc_msgSend$set_allowsAccessibilityIntelligence:
+ _objc_msgSend$set_allowsVisualIntelligence:
- ___block_descriptor_40_e8_32s_e87_v32?0"AEAssessmentApplicationDescriptor"8"AEAssessmentIndividualConfiguration"16^B24ls32l8
CStrings:
+ "<%@: %p { allowsNetworkAccess = %@, required = %@ }>"
+ "<%@: %p { binaryExecutableURL = %@, teamIdentifier = %@, requiresSignatureChecks = %@ }>"
+ "v32@?0@\"AEAssessmentBinaryExecutable\"8@\"AEAssessmentBinaryExecutableConfiguration\"16^B24"
```
