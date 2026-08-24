## AutomaticAssessmentConfiguration

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Versions/A/AutomaticAssessmentConfiguration`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x7da8
-  __TEXT.__objc_methlist: 0x894
+56.1.1.0.0
+  __TEXT.__text: 0x8c38
+  __TEXT.__objc_methlist: 0xa94
   __TEXT.__const: 0x3ae
-  __TEXT.__cstring: 0x41f
+  __TEXT.__cstring: 0x508
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_reflstr: 0x22

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x270
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x108
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f0
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x120
-  __AUTH_CONST.__const: 0xc8
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x1040
+  __DATA_CONST.__objc_selrefs: 0x798
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0x130
+  __AUTH_CONST.__const: 0xf8
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x13d0
   __AUTH_CONST.__auth_got: 0x260
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x108
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x180
   __DATA.__bss: 0x490
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Versions/A/Frameworks/AACClient.framework/Versions/A/AACClient

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 261
-  Symbols:   640
-  CStrings:  39
+  Functions: 308
+  Symbols:   731
+  CStrings:  42
 
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
+ -[AEAssessmentConfiguration allowsForceQuitKeyboardShortcuts]
+ -[AEAssessmentConfiguration allowsLockdownMode]
+ -[AEAssessmentConfiguration allowsOnlyParticipantsToRun]
+ -[AEAssessmentConfiguration allowsPrivateRelay]
+ -[AEAssessmentConfiguration allowsVirtualMachine]
+ -[AEAssessmentConfiguration configurationsByBinaryExecutable]
+ -[AEAssessmentConfiguration removeBinaryExecutable:]
+ -[AEAssessmentConfiguration requiresReleaseOS]
+ -[AEAssessmentConfiguration setAllowsForceQuitKeyboardShortcuts:]
+ -[AEAssessmentConfiguration setAllowsLockdownMode:]
+ -[AEAssessmentConfiguration setAllowsOnlyParticipantsToRun:]
+ -[AEAssessmentConfiguration setAllowsPrivateRelay:]
+ -[AEAssessmentConfiguration setAllowsVirtualMachine:]
+ -[AEAssessmentConfiguration setBackingConfigurationsByBinaryExecutable:]
+ -[AEAssessmentConfiguration setConfiguration:forBinaryExecutable:]
+ -[AEAssessmentConfiguration setRequiresReleaseOS:]
+ OBJC_IVAR_$_AEAssessmentBinaryExecutable._binaryExecutableURL
+ OBJC_IVAR_$_AEAssessmentBinaryExecutable._requiresSignatureValidation
+ OBJC_IVAR_$_AEAssessmentBinaryExecutable._teamIdentifier
+ OBJC_IVAR_$_AEAssessmentBinaryExecutableConfiguration._allowsNetworkAccess
+ OBJC_IVAR_$_AEAssessmentBinaryExecutableConfiguration._required
+ OBJC_IVAR_$_AEAssessmentConfiguration.__allowsAccessibilityIntelligence
+ OBJC_IVAR_$_AEAssessmentConfiguration.__allowsVisualIntelligence
+ OBJC_IVAR_$_AEAssessmentConfiguration._allowsForceQuitKeyboardShortcuts
+ OBJC_IVAR_$_AEAssessmentConfiguration._allowsLockdownMode
+ OBJC_IVAR_$_AEAssessmentConfiguration._allowsOnlyParticipantsToRun
+ OBJC_IVAR_$_AEAssessmentConfiguration._allowsPrivateRelay
+ OBJC_IVAR_$_AEAssessmentConfiguration._allowsVirtualMachine
+ OBJC_IVAR_$_AEAssessmentConfiguration._backingConfigurationsByBinaryExecutable
+ OBJC_IVAR_$_AEAssessmentConfiguration._requiresReleaseOS
+ _OBJC_CLASS_$_AEAssessmentBinaryExecutable
+ _OBJC_CLASS_$_AEAssessmentBinaryExecutableConfiguration
+ _OBJC_METACLASS_$_AEAssessmentBinaryExecutable
+ _OBJC_METACLASS_$_AEAssessmentBinaryExecutableConfiguration
+ _OUTLINED_FUNCTION_1
+ __49-[AEAssessmentConfiguration configurationWrapper]_block_invoke
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
+ ___block_descriptor_40_e8_32s_e88_v32?0"AEAssessmentBinaryExecutable"8"AEAssessmentBinaryExecutableConfiguration"16^B24l
+ ___block_descriptor_48_e8_32s40s_e87_v32?0"AEAssessmentApplicationDescriptor"8"AEAssessmentIndividualConfiguration"16^B24l
+ ___copy_helper_block_e8_32s40s
+ ___destroy_helper_block_e8_32s40s
+ _objc_msgSend$_allowsAccessibilityIntelligence
+ _objc_msgSend$_allowsVisualIntelligence
+ _objc_msgSend$allowsForceQuitKeyboardShortcuts
+ _objc_msgSend$allowsLockdownMode
+ _objc_msgSend$allowsOnlyParticipantsToRun
+ _objc_msgSend$allowsPrivateRelay
+ _objc_msgSend$allowsVirtualMachine
+ _objc_msgSend$binaryExecutableURL
+ _objc_msgSend$executablePath
+ _objc_msgSend$initWithBinaryExecutableURL:teamIdentifier:
+ _objc_msgSend$initWithBinaryExecutableURL:teamIdentifier:requiresSignatureValidation:
+ _objc_msgSend$initWithExecutablePath:teamIdentifier:requiresSignatureValidation:
+ _objc_msgSend$requiresReleaseOS
+ _objc_msgSend$setAllowsForceQuitKeyboardShortcuts:
+ _objc_msgSend$setAllowsLockdownMode:
+ _objc_msgSend$setAllowsOnlyParticipantsToRun:
+ _objc_msgSend$setAllowsPrivateRelay:
+ _objc_msgSend$setAllowsVirtualMachine:
+ _objc_msgSend$setRequiresReleaseOS:
+ _objc_msgSend$set_allowsAccessibilityIntelligence:
+ _objc_msgSend$set_allowsVisualIntelligence:
- -[AEAssessmentConfiguration allowLockdownMode]
- -[AEAssessmentConfiguration allowOnlyParticipantsToRun]
- -[AEAssessmentConfiguration allowPrivateRelay]
- -[AEAssessmentConfiguration setAllowLockdownMode:]
- -[AEAssessmentConfiguration setAllowOnlyParticipantsToRun:]
- -[AEAssessmentConfiguration setAllowPrivateRelay:]
- OBJC_IVAR_$_AEAssessmentConfiguration._allowLockdownMode
- OBJC_IVAR_$_AEAssessmentConfiguration._allowOnlyParticipantsToRun
- OBJC_IVAR_$_AEAssessmentConfiguration._allowPrivateRelay
- ___block_descriptor_40_e8_32s_e87_v32?0"AEAssessmentApplicationDescriptor"8"AEAssessmentIndividualConfiguration"16^B24l
- _objc_msgSend$allowLockdownMode
- _objc_msgSend$allowOnlyParticipantsToRun
- _objc_msgSend$allowPrivateRelay
- _objc_msgSend$setAllowLockdownMode:
- _objc_msgSend$setAllowOnlyParticipantsToRun:
- _objc_msgSend$setAllowPrivateRelay:
CStrings:
+ "<%@: %p { allowsNetworkAccess = %@, required = %@ }>"
+ "<%@: %p { binaryExecutableURL = %@, teamIdentifier = %@, requiresSignatureChecks = %@ }>"
+ "v32@?0@\"AEAssessmentBinaryExecutable\"8@\"AEAssessmentBinaryExecutableConfiguration\"16^B24"
```
