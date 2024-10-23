## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0x79c14
+5200.2.4.1.5
+  __TEXT.__text: 0x79ea0
   __TEXT.__auth_stubs: 0x1ef0
   __TEXT.__objc_methlist: 0x2aa8
   __TEXT.__const: 0x1770
-  __TEXT.__cstring: 0x42e0
-  __TEXT.__oslogstring: 0x6082
-  __TEXT.__gcc_except_tab: 0xe18
+  __TEXT.__cstring: 0x42c0
+  __TEXT.__oslogstring: 0x60e2
+  __TEXT.__gcc_except_tab: 0xe4c
   __TEXT.__constg_swiftt: 0x690
   __TEXT.__swift5_typeref: 0xb22
   __TEXT.__swift5_reflstr: 0x70d

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 2075
-  Symbols:   1845
-  CStrings:  3035
+  Symbols:   1846
+  CStrings:  3037
 
CStrings:
+ "SELECT MAX(samples.data_id), objects.uuid, samples.data_type, objects.type FROM samples INNER JOIN objects USING(data_id) %!@(MISSING)"
+ "[%!{(MISSING)public}@] Analyzing %!@(MISSING) summaries with user entered birthdate: %!@(MISSING), cycle length: %!@(MISSING) (%!@(MISSING)), period length: %!@(MISSING) (%!@(MISSING)) alg version %!@(MISSING)"
+ "hdmc_analysisSampleInfo"
- "SELECT samples.data_id, objects.uuid, samples.data_type, objects.type FROM samples INNER JOIN objects USING(data_id) %!@(MISSING) ORDER BY samples.data_id DESC LIMIT 1"
- "[%!{(MISSING)public}@] Analyzing %!@(MISSING) summaries with user entered birthdate: %!@(MISSING), cycle length: %!@(MISSING) (%!@(MISSING)), period length: %!@(MISSING) (%!@(MISSING))"

```
