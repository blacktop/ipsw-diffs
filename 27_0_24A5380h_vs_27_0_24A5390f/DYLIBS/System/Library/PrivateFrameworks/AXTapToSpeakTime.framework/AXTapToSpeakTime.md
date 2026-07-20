## AXTapToSpeakTime

> `/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3234.5.0.0.0
-  __TEXT.__text: 0x6cd8
+3237.1.0.0.0
+  __TEXT.__text: 0x6be8
   __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0xe0
   __TEXT.__oslogstring: 0xdfc
   __TEXT.__cstring: 0x900
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__unwind_info: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x810
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x910

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 165
-  Symbols:   659
+  Symbols:   662
   CStrings:  182
 
Symbols:
+ _kAXSTapToSpeakTimeAvailabilityPreference
+ _kAXSTapToSpeakTimeEnabledPreference
+ _kAXSVoiceOverTapticTimeEncoding
Functions:
~ -[AXTimeOutputPreferences tapToSpeakTimeEnabled] : 88 -> 28
~ -[AXTimeOutputPreferences setTapToSpeakTimeEnabled:] : 124 -> 104
~ -[AXTimeOutputPreferences tapToSpeakTimeAvailability] : 88 -> 28
~ -[AXTimeOutputPreferences setTapToSpeakTimeAvailability:] : 124 -> 104
~ -[AXTimeOutputPreferences voiceOverTapticTimeEncoding] : 88 -> 28
~ -[AXTimeOutputPreferences setVoiceOverTapticTimeEncoding:] : 124 -> 104
```
