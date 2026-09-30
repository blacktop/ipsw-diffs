## SoundsAndHapticsSettings

> `/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2027.0.1.100.0
-  __TEXT.__text: 0x2392c
+2027.0.3.0.0
+  __TEXT.__text: 0x23ad4
   __TEXT.__objc_methlist: 0x1c24
   __TEXT.__const: 0xc84
   __TEXT.__gcc_except_tab: 0xa50
-  __TEXT.__oslogstring: 0x11c1
+  __TEXT.__oslogstring: 0x11f0
   __TEXT.__cstring: 0x3423
   __TEXT.__swift5_typeref: 0x1070
   __TEXT.__swift5_reflstr: 0x163

   __DATA_CONST.__got: 0x780
   __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__cfstring: 0x1b40
-  __AUTH_CONST.__objc_const: 0x2a00
+  __AUTH_CONST.__objc_const: 0x2a20
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_got: 0xa10
   __AUTH.__objc_data: 0x630
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_ivar: 0x188
   __DATA.__data: 0x7f0
   __DATA.__common: 0x10
   __DATA.__bss: 0x5f0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 823
-  Symbols:   2039
-  CStrings:  458
+  Symbols:   2040
+  CStrings:  459
 
Symbols:
+ _OBJC_IVAR_$_SHSSoundsPrefController._viewIsDisappearing
Functions:
~ -[SHSSoundsPrefController willForeground] : 56 -> 164
~ -[SHSSoundsPrefController viewWillAppear:] : 488 -> 504
~ -[SHSSoundsPrefController viewDidAppear:] : 164 -> 180
~ -[SHSSoundsPrefController viewWillDisappear:] : 468 -> 488
~ -[SHSSoundsPrefController startVolumePreviewForAlertType:] : 484 -> 600
~ -[SHSSoundsPrefController startSystemSoundVolumePreview] : 444 -> 560
~ -[SHSSoundsPrefController alertSliderTouchBegan:] : 216 -> 232
~ -[SHSSoundsPrefController alarmSliderTouchBegan:] : 228 -> 244
CStrings:
+ "%s: View is disappearing, suppressing preview."
```
