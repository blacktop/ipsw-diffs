## libAudioDSPCore.dylib

> `/usr/lib/libAudioDSPCore.dylib`

```diff

-747.207.0.0.0
-  __TEXT.__text: 0x67058
-  __TEXT.__auth_stubs: 0x1390
+747.333.0.0.0
+  __TEXT.__text: 0x68764
+  __TEXT.__auth_stubs: 0x13b0
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__gcc_except_tab: 0x6860
-  __TEXT.__cstring: 0x27af
+  __TEXT.__gcc_except_tab: 0x6ad0
+  __TEXT.__cstring: 0x27c6
   __TEXT.__const: 0x1419c
-  __TEXT.__oslogstring: 0x346b
+  __TEXT.__oslogstring: 0x3428
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2670
+  __TEXT.__unwind_info: 0x26f0
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methname: 0x14d
   __TEXT.__objc_methtype: 0xb

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x9d8
+  __AUTH_CONST.__auth_got: 0x9e8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x1078
-  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__const: 0x10c0
+  __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0x90
   __DATA.__data: 0x108
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1687
-  Symbols:   2220
-  CStrings:  765
+  Functions: 1710
+  Symbols:   2245
+  CStrings:  769
 
Symbols:
+ _MGCopyAnswerWithError
+ __ZN2IR12IRDataLoader11getLoadedIRERKNS_16IRDataAttributesE
+ __ZN2IR12IRDataLoader30getPersonalizedHRTFCacheStatusEv
+ __ZN2IR12IRDataLoader33addToPersonalizedHRTFCallbackPoolENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_8functionIFvNS_18PersonalizedIRData10DataStatusENS9_12DataValidityEEEENS_28PersonalizedHRIRCallbackTypeE
+ __ZN2IR12IRDataLoader38removeFromPersonalizedHRTFCallbackPoolENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN2IR18PersonalizedIRData17RegisterObserversERKNSt3__18functionIFvNS0_10DataStatusEEEEb
+ __ZN2IR18PersonalizedIRData18RebuildCFDataCacheERKNSt3__18functionIFvNS0_12DataValidityEEEE
+ __ZNK2IR18PersonalizedIRData13GetDataSourceEv
+ _objc_release_x27
+ _objc_retain_x8
- __ZN2IR18PersonalizedIRData17RegisterObserversERKNSt3__18functionIFvbEEEb
- __ZN2IR18PersonalizedIRData18RebuildCFDataCacheERKNSt3__18functionIFvbEEE
- _objc_retain_x25
CStrings:
+ "%!s(MISSING)%!s(MISSING): Invalid personalized HRIR data source."
+ "%!s(MISSING): Callback for caller ID %!s(MISSING) is removed from Personalized HRTF callback pool."
+ "%!s(MISSING): Callback is added in the personalized HRTF callback pool (%!s(MISSING)) with caller ID %!s(MISSING)."
+ "%!s(MISSING): Executing client callback with (DataStatus, DataValidity) = (%!s(MISSING), %!s(MISSING)) for clientID = %!s(MISSING)."
+ "%!s(MISSING): ID %!s(MISSING) already exists in personalized HRTF callback pool (%!s(MISSING))."
+ "AID"
+ "Invalid"
+ "Modified"
+ "OnDataChangeOnly"
+ "OnDataOrAccessiblityChange"
+ "Unchanged"
+ "Valid"
+ "[%!s(MISSING)|%!s(MISSING)] Executing callback with DataValidity = %!s(MISSING)."
+ "[%!s(MISSING)|%!s(MISSING)] Executing callback with valid data = true"
+ "[%!s(MISSING)|%!s(MISSING)] Personalized HRIR type %!u(MISSING) is %!s(MISSING) in CFData cache."
+ "[%!s(MISSING)|%!s(MISSING)] Successfully pulled SoundProfile pack in %!f(MISSING)ms. Size: %!u(MISSING)"
+ "addToPersonalizedHRTFCallbackPool"
+ "executePersonalizedHRTFCallbacks"
+ "found"
+ "removeFromPersonalizedHRTFCallbackPool"
+ "unavailable"
- " (empty)"
- "%!s(MISSING)%!s(MISSING): Caching host-provided CFData for personalized HRIR type %!u(MISSING) in IRDataLoader cache."
- "%!s(MISSING)%!s(MISSING): Could not find Personalized HRIR type %!u(MISSING). Reverting back to generic HRIR: %!s(MISSING)."
- "%!s(MISSING): Callback for caller ID %!s(MISSING) is removed from Personalized HRTF listener queue."
- "%!s(MISSING): Executing client callback with (isDataChanged, isDataValid) = (%!s(MISSING), %!s(MISSING)) for clientID = %!s(MISSING)."
- "%!s(MISSING): ID %!s(MISSING) already exists in PersonalizedHRTFListenerCallback."
- "%!s(MISSING): New callback is added in the personalized HRTF listener queue with caller ID %!s(MISSING)."
- "/AID"
- "[%!s(MISSING)|%!s(MISSING)] Executing callback with valid data = %!s(MISSING)."
- "[%!s(MISSING)|%!s(MISSING)] Personalized HRIR%!s(MISSING) type %!u(MISSING) is returned from cache."
- "[%!s(MISSING)|%!s(MISSING)] Successfully pulled SoundProfile pack. Size: %!u(MISSING)"
- "acoustic_id"
- "addPersonalizedHRTFListenerCallback"
- "available but not allowed"
- "executePersonalizedHRTFListenerCallbacks"
- "not available"
- "removePersonalizedHRTFListenerCallback"

```
