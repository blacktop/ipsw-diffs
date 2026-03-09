## AppleAOPAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/AppleAOPAudioPlugin.driver/AppleAOPAudioPlugin`

```diff

 540.1.0.0.0
-  __TEXT.__text: 0x18440
-  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__text: 0x182e0
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_stubs: 0xca0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x350
   __TEXT.__gcc_except_tab: 0x15c4
   __TEXT.__const: 0x300
   __TEXT.__oslogstring: 0x1875
-  __TEXT.__cstring: 0x32ff
+  __TEXT.__cstring: 0x306b
   __TEXT.__objc_methname: 0xc2f
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methtype: 0x5bd
   __TEXT.__unwind_info: 0xbc0
-  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x528
   __DATA_CONST.__cfstring: 0x4a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0986099C-F061-307E-BC9D-FF081C417C39
+  UUID: C6AD7874-83E4-3473-9ED8-D2D029F85205
   Functions: 691
-  Symbols:   698
-  CStrings:  606
+  Symbols:   697
+  CStrings:  604
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ __ZN14CACFDictionary10PrintToLogEPK14__CFDictionaryj : 616 -> 400
~ __ZN12CADeprecated15CADispatchQueue31RemoveMachPortDeathNotificationEj : 324 -> 288
~ __ZN12CADeprecated15CADispatchQueue22RemoveMachPortReceiverEjU13block_pointerFvvE : 352 -> 308
~ sub_146c0 -> sub_14598 : 408 -> 352
CStrings:
+ "23:28:44"
+ "Feb 28 2026"
- "/AppleInternal/Library/BuildRoots/4~CJlHugDrY2aAxDtSEpNnQqNv9GpsZ7ouaRsO4dk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlHugDrY2aAxDtSEpNnQqNv9GpsZ7ouaRsO4dk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "02:14:12"
- "Feb 22 2026"

```
