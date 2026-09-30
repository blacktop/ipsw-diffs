## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`

```diff

 176.0.0.0.0
-  __TEXT.__text: 0x1b58c
+  __TEXT.__text: 0x1c2cc
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x3ac0
-  __TEXT.__objc_methlist: 0x2484
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x1361
-  __TEXT.__objc_methname: 0x42e7
-  __TEXT.__oslogstring: 0x32fc
-  __TEXT.__objc_classname: 0x420
-  __TEXT.__objc_methtype: 0x8a6
-  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__objc_stubs: 0x3ca0
+  __TEXT.__objc_methlist: 0x25c4
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x13e4
+  __TEXT.__objc_methname: 0x4508
+  __TEXT.__oslogstring: 0x3455
+  __TEXT.__objc_classname: 0x442
+  __TEXT.__objc_methtype: 0x8eb
+  __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x780
-  __DATA_CONST.__const: 0x918
-  __DATA_CONST.__cfstring: 0x13e0
-  __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x80
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__const: 0x940
+  __DATA_CONST.__cfstring: 0x1400
+  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0x188
-  __DATA.__objc_const: 0x5840
-  __DATA.__objc_selrefs: 0x11c0
-  __DATA.__objc_ivar: 0x278
-  __DATA.__objc_data: 0x910
-  __DATA.__data: 0x600
+  __DATA_CONST.__got: 0x1a0
+  __DATA.__objc_const: 0x5a40
+  __DATA.__objc_selrefs: 0x1260
+  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_data: 0x960
+  __DATA.__data: 0x660
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 860
-  Symbols:   175
-  CStrings:  1457
+  Functions: 889
+  Symbols:   178
+  CStrings:  1502
 
Symbols:
+ _OBJC_CLASS_$_CMAngleManager
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_NSHashTable
CStrings:
+ "@\"AngleMonitor\""
+ "@\"CMAngleManager\""
+ "@\"NSHashTable\""
+ "AngleMonitor"
+ "AngleMonitorDelegate"
+ "CMAngleManager not available on this device"
+ "Initiated CMAngleManager with update interval %f"
+ "Invalid angle sample: state=%ld eventPhase=%ld"
+ "Received angle update: angleDegrees=%f angleValid=%d state=%ld eventPhase=%ld"
+ "T@\"AngleMonitor\",&,N,V_angleMonitor"
+ "T@\"CMAngleManager\",&,V_angleManager"
+ "T@\"NSHashTable\",&,V_delegates"
+ "T@\"NSOperationQueue\",&,V_angleQueue"
+ "TB,R,N,GisAvailable"
+ "_angleManager"
+ "_angleMonitor"
+ "_angleQueue"
+ "angleDegrees"
+ "angleDidUpdate:"
+ "angleManager"
+ "angleMonitor"
+ "angleQueue"
+ "anglemonitor"
+ "available"
+ "com.apple.powerexperienced.thermalexperience"
+ "com.apple.powerexperienced.thermalexperiencecontroller"
+ "eventPhase"
+ "initAngleMonitor"
+ "isAngleActive"
+ "isAngleValid"
+ "isAvailable"
+ "notifyDelegatesWithAngle:"
+ "numberWithFloat:"
+ "removeDelegate:"
+ "setAngleManager:"
+ "setAngleMonitor:"
+ "setAngleQueue:"
+ "setAngleUpdateInterval:"
+ "startAngleUpdatesToQueue:handler:"
+ "startMonitoring: CMAngleManager not available, skipping"
+ "startMonitoring: angle updates already active, skipping"
+ "stopAngleUpdates"
+ "v16@?0@\"CMAngle\"8"
+ "v24@0:8@\"CMAngle\"16"
+ "weakObjectsHashTable"
```
