## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

 174.0.0.0.0
-  __TEXT.__text: 0x373ca0
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x9480
-  __TEXT.__objc_methlist: 0x8d98
-  __TEXT.__gcc_except_tab: 0x105bc
-  __TEXT.__const: 0xfcde
-  __TEXT.__cstring: 0x1cb71
-  __TEXT.__oslogstring: 0x11c3b
-  __TEXT.__objc_classname: 0x1070
-  __TEXT.__objc_methtype: 0x601d
-  __TEXT.__objc_methname: 0xc220
+  __TEXT.__text: 0x3797b0
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_stubs: 0x94e0
+  __TEXT.__objc_methlist: 0x8e10
+  __TEXT.__gcc_except_tab: 0x10b50
+  __TEXT.__const: 0xffb6
+  __TEXT.__cstring: 0x1cba4
+  __TEXT.__oslogstring: 0x12537
+  __TEXT.__objc_classname: 0x1079
+  __TEXT.__objc_methtype: 0x60f1
+  __TEXT.__objc_methname: 0xc263
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc858
+  __TEXT.__unwind_info: 0xca20
   __TEXT.__eh_frame: 0x670
-  __DATA_CONST.__const: 0x28848
+  __DATA_CONST.__const: 0x29230
   __DATA_CONST.__cfstring: 0x6a00
-  __DATA_CONST.__objc_classlist: 0x4c8
+  __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_intobj: 0x1a88
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0xc38
+  __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x678
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA.__objc_const: 0x10660
-  __DATA.__objc_selrefs: 0x3050
-  __DATA.__objc_ivar: 0x94c
-  __DATA.__objc_data: 0x2fd0
+  __DATA.__objc_const: 0x10760
+  __DATA.__objc_selrefs: 0x3068
+  __DATA.__objc_ivar: 0x950
+  __DATA.__objc_data: 0x3020
   __DATA.__data: 0x2020
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17223
-  Symbols:   608
-  CStrings:  9381
+  Functions: 17293
+  Symbols:   609
+  CStrings:  9424
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
CStrings:
+ "%u AHA200 %llu"
+ "-[CSKappaDetectionService feedAHA:]"
+ "@24@0:8r^{AHASample=QfffBBC}16"
+ "AHAFp"
+ "CSSPUAHA"
+ "CSSPUAHA is null"
+ "Cannot find a matching Zg parameter for AH state %d"
+ "Sorted %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u"
+ "T^{AHASample=QfffBBC},R,N"
+ "Trying to set AH state on an unsupported platform: %d"
+ "Updating Zg parameters for %d to %s,%f,%s,%f,%s,%f,%s,%f,%s,%f,%s,%f"
+ "[%s] gated inert: AH state not stable"
+ "[%s] gated inert: AH state not stable A"
+ "[%s] gated inert: AH state not stable A/B"
+ "[%s] gated inert: AH state not stable B"
+ "[%s] gated inert: disabled on V68"
+ "[%s] setConfig ahStateGateMode,%d"
+ "[AHAState] %@ must be a string; ignoring forced-state override"
+ "[AHAState] QE force epoch %zu: settledState %d->%d, isStable %d->%d"
+ "[AHAState] QE forced-state sequence active: %zu epoch(s), last sticks"
+ "[AHAState] ignoring unrecognized forced-state char '%c'"
+ "[AHAState] invalid OTA thresholds: AH_T1 (%f) > AH_T2 (%f); reverting both to defaults"
+ "[AHAState] summary,A,%{public}llu,B,%{public}d,C,%{public}d,D,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}d,config-4,%{public}d,config-5,%{public}f,config-6,%{public}d,config-7,%{public}d,debug-1a,%{public}d,debug-1b,%{public}d,debug-1c,%{public}d,debug-1d,%{public}llu,debug-1e,%{public}llu,debug-1f,%{public}u"
+ "[C] config-42,%f,config-43,%f,config-44,%f,config-45,%f,config-46,%f,config-47,%f,config-48,%f,config-49,%f,config-50,%f,config-51,%f"
+ "[CrashGroupArb] applied,%{public}d,isGroupA,%{public}d,dv1,%{public}f,dv2,%{public}f,norm,%{public}f,pp,%{public}f,sac,%{public}f"
+ "[CrashZgArb] selected,%d,usedSettled,%d,settled,%d,stable,%d,zgTimeA,%f,zgTimeB,%f,ffA,%d,ffB,%d"
+ "[DataIntegrity] Stream=count [min_ts max_ts] epoch %d accel800=%u [%llu %llu] hgaccel=%u [%llu %llu] trigger=%u [%llu %llu] dm6=%u [%llu %llu] gps=%u [%llu %llu] steps=%u [%llu %llu] audio=%u [%llu %llu] pressure=%u [%llu %llu] hertzSample=%u [%llu %llu] companionStatus=%u [%llu %llu] remoteSample=%u [%llu %llu] ta=%u [%llu %llu] ts %llu now %llu la=%d  aha=%u [%llu %llu]"
+ "[RCG] applied,%{public}d,isGroupA,%{public}d,dv1,%{public}f,dv2,%{public}f,norm,%{public}f,pp,%{public}f,sac,%{public}f,zg,%{public}f"
+ "[RC] config-67,%f,config-68,%f,config-69,%f,config-70,%f,config-71,%f,config-72,%f,config-73,%f,config-74,%f,config-75,%f,config-76,%f,config-77,%f,config-78,%f"
+ "[de-CrashClassifier] gated inert: AH state not stable"
+ "[de-CrashClassifier] gated inert: AH state not stable A"
+ "[de-CrashClassifier] gated inert: AH state not stable A/B"
+ "[de-CrashClassifier] gated inert: AH state not stable B"
+ "[de-CrashClassifier] gated inert: disabled on V68"
+ "[de-CrashClassifier] setConfig ahStateGateMode,%d"
+ "^{AHASample=QfffBBC}16@0:8"
+ "aha"
+ "aha %llu %f\n"
+ "closing epoch because of feedAHA t=%llu"
+ "deviceState"
+ "feedAHA:"
+ "isAHASupportedDevice"
+ "recordAHA:"
+ "v24@0:8@\"CSSPUAHA\"16"
+ "{\"msg%{public}.0s\":\"CSSPUAHA is null\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{AHASample=\"timestamp\"Q\"angleDegrees\"f\"mechanicalAngleDegrees\"f\"velocityDegreesPerSecond\"f\"isAngleValid\"B\"isVelocityValid\"B\"state\"C}"
- "Sorted %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u"
- "[DataIntegrity] Stream=count [min_ts max_ts] epoch %d accel800=%u [%llu %llu] hgaccel=%u [%llu %llu] trigger=%u [%llu %llu] dm6=%u [%llu %llu] gps=%u [%llu %llu] steps=%u [%llu %llu] audio=%u [%llu %llu] pressure=%u [%llu %llu] hertzSample=%u [%llu %llu] companionStatus=%u [%llu %llu] remoteSample=%u [%llu %llu] ta=%u [%llu %llu] ts %llu now %llu la=%d "
- "kData4"
```
