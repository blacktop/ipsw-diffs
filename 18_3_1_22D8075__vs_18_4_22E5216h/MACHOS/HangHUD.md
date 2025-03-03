## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0x18e0c
+354.2.0.0.0
+  __TEXT.__text: 0x194f4
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x3680
-  __TEXT.__objc_methlist: 0x19c8
+  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methlist: 0x1c6c
   __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x1a81
-  __TEXT.__cstring: 0x2b34
+  __TEXT.__cstring: 0x2c13
   __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methname: 0x6c4c
+  __TEXT.__objc_methname: 0x6e10
+  __TEXT.__oslogstring: 0x1ade
   __TEXT.__objc_methtype: 0xd95
-  __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__gcc_except_tab: 0x2ac
+  __TEXT.__unwind_info: 0x6f0
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x1620
-  __DATA_CONST.__cfstring: 0x3d00
+  __DATA_CONST.__const: 0x1558
+  __DATA_CONST.__cfstring: 0x3e80
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x4500
-  __DATA.__objc_selrefs: 0x1400
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_const: 0x4158
+  __DATA.__objc_selrefs: 0x1498
+  __DATA.__objc_ivar: 0x3a4
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x450
   __DATA.__bss: 0x268

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 764
+  Functions: 803
   Symbols:   200
-  CStrings:  1947
+  CStrings:  1970
 
Symbols:
+ _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "CPU Limit"
+ "HangHUD"
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "Self Restrict"
+ "TB,N,V_isInstantiatedInHangHUDProcess"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_isInstantiatedInHangHUDProcess"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "addObjectsFromArray:"
+ "allRecordsMutable"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "cpu limit"
+ "excluding process exit record, timediff (%llu) > %llu, processName %@, pid %d, exitTimestamp %llu, exitReasonCode %llu, exitReasonNamespace %u"
+ "generativeexperiencesd"
+ "isInstantiatedInHangHUDProcess"
+ "modelcatalogd"
+ "modelmanagerd"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "rapportd"
+ "record# %d, processName %@, pid %d, spawnTimestamp %llu, exitTimestamp %llu, exitReasonCode %llu, exitReasonNamespace %u, jetsam_priority %u"
+ "self restrict"
+ "setIsInstantiatedInHangHUDProcess:"
+ "shouldAugmentSentryTailspinWithSignposts"
+ "\xf0\xf0Q!!\x17!"
- "Not removing hang since an animation is in progress %@"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "_shouldCollectOSSignpostsDeferred"
- "discarding stale record, time since exit %.0fms, HT_STALE_RECORD_THRESHOLD_IN_MSEC %llums, %@"
- "insert:"
- "removeObjectAtIndex:"
- "removeStaleHangData:"
- "removing object for key %@ from dict : %@"
- "shouldCollectOSSignpostsDeferred"
- "\xf0\xf0A\x11!\x17!"

```
