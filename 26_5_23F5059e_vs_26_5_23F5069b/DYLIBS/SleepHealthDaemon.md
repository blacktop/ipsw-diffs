## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-6200.6.7.0.0
-  __TEXT.__text: 0xb558
+6200.6.8.2.1
+  __TEXT.__text: 0xb7bc
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_methlist: 0xae4
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x64a
-  __TEXT.__oslogstring: 0x19dc
+  __TEXT.__oslogstring: 0x1b77
   __TEXT.__gcc_except_tab: 0x1f0
   __TEXT.__unwind_info: 0x270
   __TEXT.__objc_classname: 0x36e

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4106FC6-6B09-349E-AC49-8F398B18A86B
+  UUID: 535BEB63-1211-3522-AC08-0CF2892C903D
   Functions: 160
   Symbols:   1040
-  CStrings:  727
+  CStrings:  731
 
Functions:
~ -[HDSHBreathingDisturbanceAnalysisScheduler _requestBreathingDisturbanceAnalysisIfNeeded] : 1952 -> 2564
CStrings:
+ "[%{public}@] Failed to persist corrected analysis count with error: %@"
+ "[%{public}@] Recorded analysis count (%ld) exceeds expected count (%ld) which should never happen; resetting to correct a possible date shift into the future."
+ "[%{public}@] Successfully recorded %ld attempt(s) count to KVD."
+ "[%{public}@] Successfully restored skewed analysis count and last analysis date. Scheduling check-in 1 day from now."

```
