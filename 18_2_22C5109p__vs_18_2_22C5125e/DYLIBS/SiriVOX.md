## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX`

```diff

-3402.3.1.0.0
-  __TEXT.__text: 0x828f0
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x6840
+3402.7.1.0.0
+  __TEXT.__text: 0x81fcc
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x67e8
   __TEXT.__const: 0x94
   __TEXT.__gcc_except_tab: 0x838
-  __TEXT.__cstring: 0x10c1f
-  __TEXT.__oslogstring: 0x75b1
+  __TEXT.__cstring: 0x10b37
+  __TEXT.__oslogstring: 0x761f
   __TEXT.__dlopen_cstrs: 0xda
   __TEXT.__ustring: 0x6c
-  __TEXT.__unwind_info: 0x22a8
-  __TEXT.__objc_classname: 0x2132
-  __TEXT.__objc_methname: 0x10f01
-  __TEXT.__objc_methtype: 0x5382
-  __TEXT.__objc_stubs: 0xbae0
-  __DATA_CONST.__got: 0x6c0
+  __TEXT.__unwind_info: 0x2280
+  __TEXT.__objc_classname: 0x211e
+  __TEXT.__objc_methname: 0x10d31
+  __TEXT.__objc_methtype: 0x52cc
+  __TEXT.__objc_stubs: 0xba80
+  __DATA_CONST.__got: 0x6b8
   __DATA_CONST.__const: 0x2b48
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2a0
+  __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3608
+  __DATA_CONST.__objc_selrefs: 0x35c0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_arraydata: 0xa10
-  __AUTH_CONST.__auth_got: 0x518
-  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__auth_got: 0x510
+  __AUTH_CONST.__const: 0x9e0
   __AUTH_CONST.__cfstring: 0x5e80
-  __AUTH_CONST.__objc_const: 0x14dd8
+  __AUTH_CONST.__objc_const: 0x14bd0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xde0
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH.__objc_data: 0x3bb0
-  __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xbc4
-  __DATA.__data: 0x1f88
-  __DATA.__bss: 0x258
+  __AUTH.__data: 0x8
+  __DATA.__objc_ivar: 0xbc0
+  __DATA.__data: 0x1f28
+  __DATA.__bss: 0x238
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService
   - /System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UserActivity.framework/UserActivity
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2937
-  Symbols:   3401
-  CStrings:  5501
+  Functions: 2920
+  Symbols:   3384
+  CStrings:  5476
 
Symbols:
+ _UAUserActivityTypeSiri
- _OBJC_CLASS_$_AFMyriadCoordinator
- _OBJC_CLASS_$_AFMyriadGoodnessScoreContext
- _dlsym
CStrings:
+ "%!s(MISSING) Getting localized string with bundleIdentifier: %!@(MISSING), table: %!@(MISSING), key: %!@(MISSING), languageCode: %!@(MISSING), gender: %!@(MISSING)"
+ "%!s(MISSING) Localized string found (%!@(MISSING)) for table %!@(MISSING), key %!@(MISSING), and languageCode %!@(MISSING)"
+ "%!s(MISSING) No table provided. Checking standard localization tables for result."
+ "%!s(MISSING) Speakable utterance parser parsed an empty speakableUtterance. (speakableText = %!{(MISSING)public}@, speakableUtteranceParser = %!{(MISSING)public}@"
+ "%!s(MISSING) getLocalizedStringWith (languageCode: %!@(MISSING), gender: %!@(MISSING), key: %!@(MISSING))"
+ "-[SVXBundleUtils getLocalizedStringWithBundle:table:key:languageCode:gender:]"
+ "-[SVXLocalizationUtils getLocalizedStringWithLanguageCode:gender:key:]"
- "\x02\x14"
- "%!s(MISSING) Myriad configured for Direct Trigger with myriadContext %!@(MISSING)."
- "%!s(MISSING) Myriad configured for Voice Trigger with goodness score context %!@(MISSING) and myriadContext %!@(MISSING)."
- "%!s(MISSING) Unexpected call to startAdvertising:withMyriadGoodnessScoreContext:... with SCDA enabled"
- "%!s(MISSING) Unexpected call to startAdvertising:withSCDAGoodnessScoreContext:... with SCDA disabled"
- "-[SVXMyriadDeviceManager startAdvertising:withMyriadGoodnessScoreContext:withMyriadAudioContext:completion:]"
- "-[SVXMyriadHostDevice myriadCoordinatorDidHandleEmergency:]"
- "-[SVXMyriadHostDevice startAdvertising:withMyriadGoodnessScoreContext:withMyriadAudioContext:completion:]_block_invoke"
- "/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity"
- "@\"AFMyriadCoordinator\""
- "AFMyriadDelegate"
- "UAUserActivityTypeSiri"
- "_myriadCoordinator"
- "advertisingDidBegin:"
- "advertisingDidEnd:"
- "advertisingWillBeginWithDelay:advertisingInterval:"
- "isSCDAFrameworkEnabled"
- "listeningDidBegin:"
- "listeningDidEnd:"
- "myriadContext"
- "myriadCoordinatorDidHandleEmergency:"
- "myriadCoordinatorWillHandleEmergency:"
- "shouldAbortAnotherDeviceBetter:"
- "shouldContinue:"
- "shouldHandleEmergency:"
- "shouldUnduck:"
- "startAdvertising:withMyriadGoodnessScoreContext:withMyriadAudioContext:completion:"
- "v24@0:8@\"AFMyriadCoordinator\"16"
- "v24@0:8@\"AFMyriadSession\"16"
- "v48@0:8Q16@\"AFMyriadGoodnessScoreContext\"24@\"AFMyriadContext\"32@?<v@?@\"SVXServiceCommandResult\">40"
- "willEndSession:"
- "willStartWithSession:"

```
