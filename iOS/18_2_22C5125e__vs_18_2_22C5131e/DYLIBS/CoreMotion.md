## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-2953.0.25.0.0
-  __TEXT.__text: 0x340e1c
-  __TEXT.__auth_stubs: 0x2960
-  __TEXT.__objc_methlist: 0xb59c
-  __TEXT.__const: 0xa1c8
+2953.0.26.3.2
+  __TEXT.__text: 0x342ea4
+  __TEXT.__auth_stubs: 0x2a00
+  __TEXT.__objc_methlist: 0xb664
+  __TEXT.__const: 0xa3a8
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x3ea11
-  __TEXT.__oslogstring: 0x25aae
+  __TEXT.__cstring: 0x3ec52
+  __TEXT.__oslogstring: 0x25c98
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0xaef8
-  __TEXT.__unwind_info: 0xaa20
+  __TEXT.__gcc_except_tab: 0xb058
+  __TEXT.__unwind_info: 0xab08
   __TEXT.__eh_frame: 0x1d0
-  __TEXT.__objc_classname: 0x189d
-  __TEXT.__objc_methname: 0x192aa
-  __TEXT.__objc_methtype: 0x856f
-  __TEXT.__objc_stubs: 0xcf60
-  __DATA_CONST.__got: 0x788
-  __DATA_CONST.__const: 0x36f8
-  __DATA_CONST.__objc_classlist: 0x7e8
+  __TEXT.__objc_classname: 0x18ae
+  __TEXT.__objc_methname: 0x19410
+  __TEXT.__objc_methtype: 0x867c
+  __TEXT.__objc_stubs: 0xd020
+  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__const: 0x3718
+  __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c28
+  __DATA_CONST.__objc_selrefs: 0x4c60
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x6f0
-  __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x14c8
+  __DATA_CONST.__objc_superrefs: 0x6f8
+  __DATA_CONST.__objc_arraydata: 0x250
+  __AUTH_CONST.__auth_got: 0x1518
   __AUTH_CONST.__auth_ptr: 0xc0
-  __AUTH_CONST.__const: 0x127a8
-  __AUTH_CONST.__cfstring: 0x11680
-  __AUTH_CONST.__objc_const: 0x1bab8
+  __AUTH_CONST.__const: 0x129b0
+  __AUTH_CONST.__cfstring: 0x11760
+  __AUTH_CONST.__objc_const: 0x1bc80
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__objc_dictobj: 0x280
+  __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0xaa0
+  __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x1568
-  __DATA.__data: 0xe58
+  __DATA.__objc_ivar: 0x157c
+  __DATA.__data: 0xe68
   __DATA.__bss: 0x480
   __DATA.__common: 0x158
   __DATA_DIRTY.__objc_ivar: 0x150
   __DATA_DIRTY.__objc_data: 0x4470
   __DATA_DIRTY.__data: 0x108
-  __DATA_DIRTY.__bss: 0xec8
+  __DATA_DIRTY.__bss: 0xed8
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11424
-  Symbols:   1720
-  CStrings:  14761
+  Functions: 11479
+  Symbols:   1721
+  CStrings:  14800
 
Symbols:
+ _objc_moveWeak
CStrings:
+ "%!{(MISSING)public}s calling _setDisplayGravityHandler:%!{(MISSING)public}p interval:%!{(MISSING)public}f"
+ "-[CMMotionManager setDisplayGravityHandler:interval:]"
+ "20:02:10"
+ "@72@0:8{?={?=dddd}{?=fff}}16d64"
+ "AppleSPUHIDDevice"
+ "CLDisplayGravityService.mm"
+ "CLLidAngleNotifier"
+ "CLLidAngleNotifier.mm"
+ "CMDisplayGravity"
+ "DisplayGravity"
+ "IOHIDDeviceRef lidAngleSensorDevice()"
+ "IOProviderClass"
+ "Nov  7 2024"
+ "QuaternionX %!f(MISSING) QuaternionY %!f(MISSING) QuaternionZ %!f(MISSING) QuaternionW %!f(MISSING) GravityX %!f(MISSING) GravityY %!f(MISSING) GravityZ %!f(MISSING) @ %!f(MISSING)"
+ "T@?,C,N,V_fDisplayGravityHandler"
+ "TB,R,N,GisDisplayGravityAvailable"
+ "Td,R,N,V_timestamp"
+ "[CLDisplayGravityService] %!{(MISSING)public}s : gravity=%!{(MISSING)public}f, %!{(MISSING)public}f ,%!{(MISSING)public}f, lidAngleDeg=%!{(MISSING)public}f, gravityCameraFrame=%!{(MISSING)public}f, %!{(MISSING)public}f ,%!{(MISSING)public}f"
+ "[LidAngleSensor] %!{(MISSING)public}s; opening HID manager failed with status = %!{(MISSING)public}d"
+ "[LidAngleSensor] %!{(MISSING)public}s; opening lid angle sensor failed with status = %!{(MISSING)public}d"
+ "[LidAngleSensor] %!{(MISSING)public}s; reading lid angle sensor failed with status = %!{(MISSING)public}d"
+ "_fDisplayGravityHandler"
+ "anyObject"
+ "bool CLLidAngleNotifier::LidAngleSensor::open()"
+ "displayGravityAvailable"
+ "fDisplayGravityHandler"
+ "fDisplayGravityService"
+ "fIsOpen"
+ "info"
+ "initWithDisplayGravity:timestamp:"
+ "isDisplayGravityAvailable"
+ "onDeviceMotion"
+ "onLidAngleChange"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "setDisplayGravityHandler:interval:"
+ "setFDisplayGravityHandler:"
+ "std::optional<double> CLLidAngleNotifier::LidAngleSensor::lidAngle() const"
+ "v16@?0@\"NSTimer\"8"
+ "v32@0:8@?16d24"
+ "void CLDisplayGravityService::notifyDeviceMotion(const CLDeviceMotion::Sample &)"
+ "{unique_ptr<CLDisplayGravityService, std::default_delete<CLDisplayGravityService>>=\"__ptr_\"{__compressed_pair<CLDisplayGravityService *, std::default_delete<CLDisplayGravityService>>=\"__value_\"^{CLDisplayGravityService}}}"
- "03:12:49"
- "Oct 27 2024"

```
