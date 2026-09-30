## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__oslogstring`

```diff

-684.0.0.0.0
-  __TEXT.__text: 0x70538
+684.100.0.0.0
+  __TEXT.__text: 0x70534
   __TEXT.__objc_methlist: 0x72c0
   __TEXT.__const: 0xd44
   __TEXT.__gcc_except_tab: 0xde4

   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0xc50
   __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x10700
+  __AUTH_CONST.__objc_const: 0x10720
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x80

   __AUTH_CONST.__auth_got: 0x970
   __AUTH.__objc_data: 0x1448
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x9fc
+  __DATA.__objc_ivar: 0xa00
   __DATA.__data: 0x11c0
   __DATA.__bss: 0x648
   __DATA.__common: 0x1f8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2868
-  Symbols:   6373
+  Symbols:   6374
   CStrings:  1068
 
Symbols:
+ _OBJC_IVAR_$_BKUIPearlEnrollView._currentRawPitch
+ _OBJC_IVAR_$_BKUIPearlEnrollView._lastLoggedCenterBinPitch
- _OBJC_IVAR_$_BKUIPearlEnrollView._lastLoggedCenterBinCorrectedPitch
Functions:
~ -[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:positioningGuideView:squareNeedsPositionLayout:] : 2144 -> 2160
~ -[BKUIPearlEnrollView resetPitchCorrection] : 404 -> 420
~ -[BKUIPearlEnrollView setPitch:yaw:] : 1156 -> 1132
~ -[BKUIPearlEnrollView _updateRaiseLowerGuidanceLabelIfNeededForPitch:] : 464 -> 452
CStrings:
+ "centerBin rawPitch %0.2f, window [%0.2f, %0.2f] (pitchCorrection %0.2f deliberately not applied)"
+ "pitch %0.2f vs window [%0.2f, %0.2f] -> %s (pitchCorrection %0.2f not applied to guidance)"
+ "\xf0\xf0\x92"
- "centerBin correctedPitch %0.2f (rawPitch %0.2f - pitchCorrection %0.2f), window [%0.2f, %0.2f]"
- "correctedPitch %0.2f (rawPitch %0.2f - pitchCorrection %0.2f) vs window [%0.2f, %0.2f] -> %s"
- "\xf0\xf0\x82"
```
