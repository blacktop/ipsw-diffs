## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-3186.0.21.0.0
-  __TEXT.__text: 0x3c76ec
-  __TEXT.__objc_methlist: 0xd9ac
-  __TEXT.__const: 0xcd60
+3186.0.22.0.0
+  __TEXT.__text: 0x3c9f18
+  __TEXT.__objc_methlist: 0xda5c
+  __TEXT.__const: 0xcf70
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x2fcd1
-  __TEXT.__cstring: 0x47ac5
+  __TEXT.__oslogstring: 0x2ff23
+  __TEXT.__cstring: 0x47d4b
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xd50c
-  __TEXT.__unwind_info: 0xd0f0
+  __TEXT.__gcc_except_tab: 0xd7ec
+  __TEXT.__unwind_info: 0xd2a0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3d20
-  __DATA_CONST.__objc_classlist: 0x8e0
+  __DATA_CONST.__objc_classlist: 0x8e8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5728
+  __DATA_CONST.__objc_selrefs: 0x5748
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x7c8
+  __DATA_CONST.__objc_superrefs: 0x7d0
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x828
-  __AUTH_CONST.__const: 0x158b8
-  __AUTH_CONST.__cfstring: 0x13d20
-  __AUTH_CONST.__objc_const: 0x1dd78
+  __AUTH_CONST.__const: 0x15b70
+  __AUTH_CONST.__cfstring: 0x13d60
+  __AUTH_CONST.__objc_const: 0x1df28
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__auth_got: 0x14c0
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x17b8
-  __DATA.__data: 0xe10
-  __DATA.__common: 0x128
+  __DATA.__objc_ivar: 0x17c8
+  __DATA.__data: 0xe20
+  __DATA.__common: 0x138
   __DATA_DIRTY.__objc_ivar: 0x1c0
   __DATA_DIRTY.__objc_data: 0x55a0
   __DATA_DIRTY.__data: 0x138

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12719
+  Functions: 12787
   Symbols:   1815
-  CStrings:  11440
+  CStrings:  11465
 
CStrings:
+ "%{public}s calling setDisplayAngleHandler:%{public}p interval:%{public}f"
+ "-[CMMotionManager setDisplayAngleHandler:interval:]"
+ "CLHomeHubServiceNotifier"
+ "CLHomeHubServiceNotifier.mm"
+ "CMDisplayAngleService.mm"
+ "DisplayAngle"
+ "[CLHomeHubServiceNotifier] %{public}s : Bump detected, timestamp=%{public}lf, now=%{public}lf"
+ "[CLHomeHubServiceNotifier] %{public}s : angle=%{public}f, isAngleStable=%{public}d, timestamp=%{public}lf, now=%{public}lf"
+ "[CLHomeHubServiceNotifier] Bad report,type,%{public}d,size,%{public}lu"
+ "[CLHomeHubServiceNotifier] Empty payload, returning"
+ "[CLHomeHubServiceNotifier] Event ref invalid"
+ "[CLHomeHubServiceNotifier] Failed to send EnableBumpEvents command"
+ "[CLHomeHubServiceNotifier] Failed to send EnableDisplayAngle command"
+ "angle %f, isStable: %d @ %f"
+ "fHaveActivatedAOP"
+ "fHidDriverInterface"
+ "isAngleStable"
+ "onDisplayAngleChange"
+ "reopenHIDDriverInterface"
+ "updateReportInterval"
+ "virtual void CLHomeHubServiceNotifier::visitBumpEvent(const CMHomeHubReport::BumpEvent &)"
+ "virtual void CLHomeHubServiceNotifier::visitDisplayAngleState(const DisplayAngleState &)"
+ "void CLHomeHubServiceNotifier::onIoHidEvent(IOHIDEventRef)"
+ "void CLHomeHubServiceNotifier::setBumpEventsEnabled(bool)"
+ "void CLHomeHubServiceNotifier::setDisplayAngleEnabled(bool)"
```
