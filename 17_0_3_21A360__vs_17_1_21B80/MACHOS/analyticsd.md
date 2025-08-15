## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-361.2.1.0.0
-  __TEXT.__text: 0xf8620
-  __TEXT.__auth_stubs: 0x1a70
-  __TEXT.__objc_stubs: 0x2380
+371.0.0.0.0
+  __TEXT.__text: 0xf9828
+  __TEXT.__auth_stubs: 0x1a60
+  __TEXT.__objc_stubs: 0x2480
   __TEXT.__init_offsets: 0x20
-  __TEXT.__objc_methlist: 0x508
-  __TEXT.__cstring: 0xb433
+  __TEXT.__objc_methlist: 0x570
+  __TEXT.__cstring: 0xb479
   __TEXT.__const: 0xa5e4
-  __TEXT.__gcc_except_tab: 0xd9b8
-  __TEXT.__oslogstring: 0x10826
+  __TEXT.__gcc_except_tab: 0xdad8
+  __TEXT.__oslogstring: 0x109c2
   __TEXT.__objc_classname: 0x11f
-  __TEXT.__objc_methname: 0x2560
+  __TEXT.__objc_methname: 0x260e
   __TEXT.__objc_methtype: 0x152f
-  __TEXT.__unwind_info: 0x6704
+  __TEXT.__unwind_info: 0x67a4
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xd50
+  __DATA_CONST.__auth_got: 0xd48
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x92a0
+  __DATA_CONST.__const: 0x92f0
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x12f8
-  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_selrefs: 0x9d0
   __DATA.__objc_classrefs: 0x190
   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x2e8
-  __DATA.__bss: 0x478
+  __DATA.__data: 0x2e0
+  __DATA.__bss: 0x488
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: ED3AB88D-0C99-3C9A-A05A-27184D54BC9F
-  Functions: 5337
-  Symbols:   613
-  CStrings:  2940
+  UUID: C212C7BD-8631-323F-9572-266D6F3BB392
+  Functions: 5357
+  Symbols:   612
+  CStrings:  2954
 
Symbols:
- __ZN10applesauce3xpc19dyn_cast_or_defaultERKNS0_6objectEx
CStrings:
+ "==== WIPE: Marking partial data flag. Data wipe is occurring but device did not do a clean install"
+ "==== WIPE: Wiping all sampling override values"
+ "OVRD"
+ "SELECT transform_id, transform_uuid, transform_enableIf FROM eligible_transform_view;"
+ "[Config Store] Evaluation: Iterating all transforms for sampling evaluation"
+ "[Config Store] Evaluation: Iterating transforms with enableIf clauses for sampling evaluation"
+ "[Config Store] Evaluation: Using sampling override percentage %{public}u for enableIf clauses"
+ "[Config Store] Evaluation: {visited: %{public}zd, evaluated: %{public}zd, enableIfPresent: %{public}zd, enabled: %{public}zd}"
+ "[PowerResolver] thermal-pressure: %s %{public}s"
+ "_isDualSim"
+ "getServingCarrierName"
+ "getSubscriberCarrierBundleVersion"
+ "getSubscriberCarrierCountry"
+ "getSubscriberCarrierName"
+ "setDelegateForMonitoring:"
+ "setInteger:forKey:"
+ "v24@0:8^{TelephonyStateDelegate=^^?}16"
- "@24@0:8^{TelephonyStateDelegate=^^?}16"
- "[Config Store] Evaluation: %zd transforms had enableIf predicates; %zd of those were enabled."
- "[PowerResolver] thermal-pressure-value: %llu, thermal-pressure: %s %{public}s"
- "thermalPressureValue"

```
