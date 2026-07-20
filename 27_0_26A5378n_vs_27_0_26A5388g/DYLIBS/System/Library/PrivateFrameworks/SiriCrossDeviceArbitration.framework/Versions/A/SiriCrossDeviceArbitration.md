## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-3600.49.8.0.0
-  __TEXT.__text: 0x312ec
-  __TEXT.__objc_methlist: 0x30fc
+3600.49.11.0.0
+  __TEXT.__text: 0x31460
+  __TEXT.__objc_methlist: 0x310c
   __TEXT.__const: 0x1b0
   __TEXT.__dlopen_cstrs: 0xc2
   __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__oslogstring: 0x54a6
+  __TEXT.__oslogstring: 0x557e
   __TEXT.__cstring: 0x5da9
   __TEXT.__unwind_info: 0xd38
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e08
+  __DATA_CONST.__objc_selrefs: 0x1e10
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x2e8

   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x350
-  __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0x4fc
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x120
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1269
-  Symbols:   3065
-  CStrings:  1045
+  Functions: 1270
+  Symbols:   3067
+  CStrings:  1048
 
Symbols:
+ +[SCDAUtilities deviceClassCanMakeEmergencyCall:]
+ _objc_msgSend$deviceClassCanMakeEmergencyCall:
Functions:
~ -[SCDAGoodnessScoreEvaluator _bumpGoodnessScore:lastActivationTime:mediaPlaybackInterruptedTime:recentlyWonBySmallAmount:] : 684 -> 900
~ -[SCDACoordinator _startAdvertisingFromInTaskVoiceTrigger] : 416 -> 424
~ ___41-[SCDACoordinator _shouldHandleEmergency]_block_invoke : 36 -> 68
~ ___48-[SCDACoordinator heySiri:foundDevice:withInfo:]_block_invoke : 1648 -> 1752
+ +[SCDAUtilities deviceClassCanMakeEmergencyCall:]
CStrings:
+ "%s #scda Odeon: media-playback boost suppressed (TV-state tier covers playback)"
+ "%s #scda Odeon: media-playback boost suppressed (interrupted)"
+ "%s BTLE not emergency-capable, returning to NoActivity instead of waiting"
```
