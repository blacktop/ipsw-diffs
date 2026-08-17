## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.68.61.11.1
-  __TEXT.__text: 0x371fcc
-  __TEXT.__auth_stubs: 0x3840
-  __TEXT.__objc_stubs: 0x47440
-  __TEXT.__objc_methlist: 0x23710
+3600.68.61.11.9
+  __TEXT.__text: 0x372924
+  __TEXT.__auth_stubs: 0x3850
+  __TEXT.__objc_stubs: 0x474c0
+  __TEXT.__objc_methlist: 0x23730
   __TEXT.__const: 0xed40
-  __TEXT.__dlopen_cstrs: 0x99d
-  __TEXT.__gcc_except_tab: 0x3aac
-  __TEXT.__cstring: 0x52dfa
-  __TEXT.__oslogstring: 0x45d7e
+  __TEXT.__dlopen_cstrs: 0x9e9
+  __TEXT.__gcc_except_tab: 0x3ae4
+  __TEXT.__cstring: 0x52ede
+  __TEXT.__oslogstring: 0x45eeb
   __TEXT.__objc_classname: 0x51d5
-  __TEXT.__objc_methname: 0x61bac
-  __TEXT.__objc_methtype: 0xff45
+  __TEXT.__objc_methname: 0x61cb0
+  __TEXT.__objc_methtype: 0xff75
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0xa520
+  __TEXT.__unwind_info: 0xa548
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x143e8
+  __DATA_CONST.__const: 0x14400
   __DATA_CONST.__cfstring: 0x123e0
   __DATA_CONST.__objc_classlist: 0xd40
   __DATA_CONST.__objc_catlist: 0x630

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1c30
+  __DATA_CONST.__auth_got: 0x1c38
   __DATA_CONST.__got: 0x3e78
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x34c58
-  __DATA.__objc_selrefs: 0x155e0
-  __DATA.__objc_ivar: 0x2694
+  __DATA.__objc_const: 0x34c78
+  __DATA.__objc_selrefs: 0x15610
+  __DATA.__objc_ivar: 0x2698
   __DATA.__objc_data: 0x8480
   __DATA.__data: 0x5d60
-  __DATA.__bss: 0xdd0
+  __DATA.__bss: 0xde0
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14626
-  Symbols:   3004
-  CStrings:  27881
+  Functions: 14634
+  Symbols:   3005
+  CStrings:  27900
 
Symbols:
+ _NSStringFromAFSiriStatus
CStrings:
+ "%s #SiriAvailability computed status=%{public}@ restrictionReasons=%{public}@ isAssistantEnabled=%{bool}d"
+ "%s #SiriAvailability recomputing: assessment mode active changed"
+ "%s #SiriAvailability recomputing: first unlock since boot — data-protected capability inputs are now readable"
+ "%s Siri restriction lifted - restoring assistant to its pre-restriction state: %d"
+ "-[ADSiriCapabilitiesStore handleAssessmentModeActiveDidChange]"
+ "-[ADSiriCapabilitiesStore handleFirstUnlockNotification:]"
+ "5"
+ "@\"AEAssessmentModeGestalt\""
+ "AEAssessmentModeGestalt"
+ "Class getAEAssessmentModeGestaltClass(void)_block_invoke"
+ "MobileAssistantDaemons-3600.68.61.11.9"
+ "_assessmentModeGestalt"
+ "addObserver:forKeyPath:options:context:"
+ "assistantEnabledBeforeRestriction"
+ "handleAssessmentModeActiveDidChange"
+ "handleFirstUnlockNotification:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "removeObserver:forKeyPath:"
+ "setAssistantEnabledBeforeRestriction:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AACCore.framework/AACCore"
+ "v48@0:8@16@24@32^v40"
+ "void *AACCoreLibrary(void)"
- "37"
- "MobileAssistantDaemons-3600.68.61.11.1"
- "isDeviceScreenON"
```
