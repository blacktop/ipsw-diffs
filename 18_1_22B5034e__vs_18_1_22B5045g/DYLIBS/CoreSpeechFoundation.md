## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3401.13.1.0.0
-  __TEXT.__text: 0xa56b8
-  __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_methlist: 0x9dc0
+3401.17.1.0.0
+  __TEXT.__text: 0xa5ce0
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0x9e20
   __TEXT.__const: 0x778
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_fieldmd: 0x128
-  __TEXT.__cstring: 0x11f99
+  __TEXT.__cstring: 0x120d7
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x1c
   __TEXT.__gcc_except_tab: 0x297c
-  __TEXT.__oslogstring: 0xcf57
+  __TEXT.__oslogstring: 0xd084
   __TEXT.__dlopen_cstrs: 0x174
-  __TEXT.__unwind_info: 0x2ad0
+  __TEXT.__unwind_info: 0x2ae0
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x173c
-  __TEXT.__objc_methname: 0x1d4a7
-  __TEXT.__objc_methtype: 0x3e08
-  __TEXT.__objc_stubs: 0xf680
-  __DATA_CONST.__got: 0xe68
-  __DATA_CONST.__const: 0x20c0
-  __DATA_CONST.__objc_classlist: 0x5f0
+  __TEXT.__objc_classname: 0x175f
+  __TEXT.__objc_methname: 0x1d5ac
+  __TEXT.__objc_methtype: 0x3e56
+  __TEXT.__objc_stubs: 0xf6c0
+  __DATA_CONST.__got: 0xe70
+  __DATA_CONST.__const: 0x20c8
+  __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f38
+  __DATA_CONST.__objc_selrefs: 0x5f58
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0xe90
+  __AUTH_CONST.__auth_got: 0xe98
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x13d0
-  __AUTH_CONST.__cfstring: 0x7d80
-  __AUTH_CONST.__objc_const: 0x118b0
+  __AUTH_CONST.__const: 0x13f0
+  __AUTH_CONST.__cfstring: 0x7dc0
+  __AUTH_CONST.__objc_const: 0x119d8
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x1b0
-  __AUTH.__objc_data: 0x100
-  __DATA.__objc_ivar: 0xb00
+  __AUTH.__objc_data: 0x150
+  __DATA.__objc_ivar: 0xb10
   __DATA.__data: 0xeb0
-  __DATA.__bss: 0x818
+  __DATA.__bss: 0x840
   __DATA_DIRTY.__objc_data: 0x3c18
   __DATA_DIRTY.__data: 0x2c0
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__bss: 0x378
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4093
-  Symbols:   5451
-  CStrings:  7913
+  Functions: 4101
+  Symbols:   5464
+  CStrings:  7935
 
Symbols:
+ _kCSPowerAssertionNameMac
+ _OBJC_METACLASS_$_CSPreventSystemSleepPowerAssertion
+ _IOPMAssertionSetProperty
+ _kCFBooleanTrue
+ _OBJC_CLASS_$_CSPreventSystemSleepPowerAssertion
CStrings:
+ "initWithConfigPathNDAPI:threshold:loggingThreshold:twoShotThreshold:twoShotDecisionWaitTime:voiceTriggerPhIds:silencePhIds:"
+ "isSelfTriggerNearMissAudioLoggingEnabled"
+ "%!s(MISSING) Failed to released power assertion for %!{(MISSING)private}@"
+ "%!s(MISSING) UserIdleSystemSleepAssertion"
+ "support_secure_platform_t8140"
+ "CSPreventSystemSleepPowerAssertion"
+ "_preventUserIdleSystemSleepAssertionId"
+ "_acquireAssertionForType:withTimeout:assertionId:details:"
+ "initWithTimeOut:"
+ "v48@0:8^{__CFString=}16d24^I32^{__CFString=}40"
+ "%!s(MISSING) IOPMAssertionSetProperty failed : %!{(MISSING)private}d"
+ "_timeoutInterval"
+ "%!s(MISSING) Taking power assertion %!{(MISSING)private}@ for a max of %!{(MISSING)private}f seconds"
+ "%!s(MISSING) Taking power assertion %!{(MISSING)private}@"
+ "%!s(MISSING) Successfully released power assertion for %!{(MISSING)private}@"
+ "-[CSPreventSystemSleepPowerAssertion _acquireAssertionForType:withTimeout:assertionId:details:]"
+ "v32@0:8^I16^{__CFString=}24"
+ "_preventSystemSleepAssertionId"
+ "AllowsDeviceRestart"
+ "-[CSPreventSystemSleepPowerAssertion _releaseAssertionForAssertionId:details:]"
+ "@56@0:8@16f24f28f32f36@40@48"
+ "_releaseAssertionForAssertionId:details:"
+ "Enable Self Trigger Near-Miss Audio Logging"
+ "-[CSPreventSystemSleepPowerAssertion invalidate]"
- "@52@0:8@16f24f28f32@36@44"
- "initWithConfigPathNDAPI:threshold:twoShotThreshold:twoShotDecisionWaitTime:voiceTriggerPhIds:silencePhIds:"

```
