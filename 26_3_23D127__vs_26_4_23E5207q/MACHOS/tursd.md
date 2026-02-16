## tursd

> `/usr/libexec/tursd`

```diff

-1131.2.3.0.0
-  __TEXT.__text: 0x8594
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x10e0
-  __TEXT.__cstring: 0x893
-  __TEXT.__oslogstring: 0x2e9
+1131.4.11.0.0
+  __TEXT.__text: 0x94cc
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x1158
+  __TEXT.__cstring: 0xa23
+  __TEXT.__oslogstring: 0x313
   __TEXT.__const: 0x1b2
-  __TEXT.__objc_methname: 0x396b
+  __TEXT.__objc_methname: 0x3ad9
   __TEXT.__objc_classname: 0x150
   __TEXT.__objc_methtype: 0x8ce
   __TEXT.__swift5_typeref: 0x4a

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x328
-  __DATA_CONST.__auth_got: 0x2f8
+  __TEXT.__unwind_info: 0x3d0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x6f8
+  __DATA_CONST.__const: 0x718
   __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1730
-  __DATA.__objc_selrefs: 0xcf0
+  __DATA.__objc_const: 0x1790
+  __DATA.__objc_selrefs: 0xd40
   __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x218
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DE739413-8724-3092-8524-DB5127C834FD
-  Functions: 313
-  Symbols:   197
-  CStrings:  810
+  UUID: 8129C1FE-1D6C-36BB-8F88-CE0A91BE24EC
+  Functions: 327
+  Symbols:   193
+  CStrings:  832
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
+ _swift_release
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "%s: %d from TUCall %p"
+ "%s: %d on TUCall %p"
+ "-[TUCall(NanoPhone) nph_wasInDepthSessionOnDial]"
+ "-[TUCall(NanoPhone) nph_wasWaterLockEnabledOnDial]"
+ "-[TUCall(NanoPhone) setNph_wasInDepthSessionOnDial:]"
+ "-[TUCall(NanoPhone) setNph_wasWaterLockEnabledOnDial:]"
+ "SatelliteSlider"
+ "airplaneModeManagementForNonEmergencyCalls"
+ "isAirplaneModeManagementEnabled"
+ "isAirplaneModeManagementEnabledForNonEmergencyCalls"
+ "isRedialAfterDisablingAirplaneModeEnabled"
+ "isRedialAfterDisablingAirplaneModeEnabledForNonEmergencyCalls"
+ "isSatelliteSliderEnabled"
+ "nph_isEmergencyOrSOS"
+ "nph_wasInDepthSessionOnDial"
+ "nph_wasWaterLockEnabledOnDial"
+ "redialAfterDisablingAirplaneMode"
+ "redialAfterDisablingAirplaneModeForNonEmergencyCalls"
+ "remoteAirplaneModeManagement"
+ "setNph_wasInDepthSessionOnDial:"
+ "setNph_wasWaterLockEnabledOnDial:"
+ "setOriginatingUIType:"
+ "sos_general"
- "isKnownCaller"

```
