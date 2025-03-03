## Siri

> `/Applications/Siri.app/Siri`

```diff

-3404.59.4.1.3
-  __TEXT.__text: 0xb6258
+3404.68.1.1.2
+  __TEXT.__text: 0xbc060
   __TEXT.__auth_stubs: 0x24f0
-  __TEXT.__objc_stubs: 0x17300
-  __TEXT.__objc_methlist: 0xc9f0
-  __TEXT.__const: 0x1534
-  __TEXT.__cstring: 0x21fd3
-  __TEXT.__oslogstring: 0x95c7
+  __TEXT.__objc_stubs: 0x17380
+  __TEXT.__objc_methlist: 0xca08
+  __TEXT.__const: 0x1544
+  __TEXT.__cstring: 0x220e3
+  __TEXT.__oslogstring: 0x96f7
   __TEXT.__objc_classname: 0x165f
-  __TEXT.__objc_methtype: 0x9639
-  __TEXT.__gcc_except_tab: 0x13ec
-  __TEXT.__objc_methname: 0x24628
+  __TEXT.__objc_methtype: 0x9684
+  __TEXT.__gcc_except_tab: 0x1460
+  __TEXT.__objc_methname: 0x246b4
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x1308
-  __TEXT.__constg_swiftt: 0x15f8
+  __TEXT.__swift5_typeref: 0x131c
+  __TEXT.__constg_swiftt: 0x1618
   __TEXT.__swift5_reflstr: 0xc8c
-  __TEXT.__swift5_fieldmd: 0x950
-  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_fieldmd: 0x978
+  __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0xa4
-  __TEXT.__swift5_capture: 0x38c
-  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift5_types: 0xa8
+  __TEXT.__swift5_capture: 0x3cc
+  __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2cf8
-  __TEXT.__eh_frame: 0x8c8
+  __TEXT.__unwind_info: 0x2d40
+  __TEXT.__eh_frame: 0x950
   __DATA_CONST.__auth_got: 0x1288
-  __DATA_CONST.__got: 0x1408
-  __DATA_CONST.__auth_ptr: 0x648
-  __DATA_CONST.__const: 0x3440
+  __DATA_CONST.__got: 0x1450
+  __DATA_CONST.__auth_ptr: 0x600
+  __DATA_CONST.__const: 0x35d8
   __DATA_CONST.__cfstring: 0x2fe0
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x120

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0xebf8
-  __DATA.__objc_selrefs: 0x8140
-  __DATA.__objc_ivar: 0x7fc
+  __DATA.__objc_const: 0xec20
+  __DATA.__objc_selrefs: 0x8160
+  __DATA.__objc_ivar: 0x800
   __DATA.__objc_data: 0x3ab8
-  __DATA.__data: 0x38f8
+  __DATA.__data: 0x3908
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x1050
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4025
-  Symbols:   1514
-  CStrings:  7926
+  Functions: 4043
+  Symbols:   1515
+  CStrings:  7940
 
Symbols:
+ _$s10ObjectiveC8ObjCBoolVMn
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "%s #dismissal - Montara onboarding flow complete, no longer preventing touches from dismissing Siri"
+ "%s #dismissal - found content at point in replay utility"
+ "%s #dismissal - temporarily preventing touches from dismissing Siri while presenting Montara onboarding flow"
+ "%s #dismissal Required features are not enabled, or input type is text -> overriding launch options to: %@"
+ "+[SRErrorUtility userStringForError:modeProvider:reflectionDialogWasPlayed:]"
+ ", saeAvailable: "
+ "-[SRSiriViewController hasContentAtPoint:completion:]_block_invoke"
+ "-[SRSystemAssistantExperienceViewController _resumeTouchDismissalPostMontaraOnboardingCompletion]"
+ "-[SRSystemAssistantExperienceViewController hasContentAtPoint:completion:]"
+ "-[SRSystemAssistantExperienceViewController willPresentOnboardingFlow]"
+ "@36@0:8@16@24B32"
+ "_resumeTouchDismissalPostMontaraOnboardingCompletion"
+ "_shouldShowErrorCodes:"
+ "_willPunchOut"
+ "overriddenSpeech"
+ "saeAvailable"
+ "shouldShowUnavailableView(sessionAvailability:saeAvailable:areSAEAssetsAvailable:isServerFallbackDisabledWhenAssetsAreMissing:)"
+ "siriDidPunchOutWithOptions:"
+ "siriWillPunchOutWithOptions:"
+ "userStringForError:modeProvider:reflectionDialogWasPlayed:"
+ "v40@0:8{CGPoint=dd}16@?32"
+ "v40@0:8{CGPoint=dd}16@?<v@?B>32"
- "%s #dismissal Input type is text -> overriding launch options to: %@"
- "+[SRErrorUtility userStringForError:reflectionDialogWasPlayed:]"
- ", isSAEEnabled: "
- "-[SRSystemAssistantExperienceViewController hasContentAtPoint:]"
- "_shouldShowErrorCodes"
- "shouldShowUnavailableView(sessionAvailability:isSAEEnabled:areSAEAssetsAvailable:isServerFallbackDisabledWhenAssetsAreMissing:)"
- "siriDidPunchoutWithOptions:"
- "userStringForError:reflectionDialogWasPlayed:"

```
