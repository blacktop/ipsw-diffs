## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-6200.2.11.2.0
-  __TEXT.__text: 0xaf54
-  __TEXT.__auth_stubs: 0x520
+6200.2.12.0.0
+  __TEXT.__text: 0xb0f4
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0xad4
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x64a
-  __TEXT.__oslogstring: 0x1831
+  __TEXT.__oslogstring: 0x1960
   __TEXT.__gcc_except_tab: 0x1f0
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0x36e
-  __TEXT.__objc_methname: 0x3198
-  __TEXT.__objc_methtype: 0x9b7
+  __TEXT.__objc_methname: 0x31d5
+  __TEXT.__objc_methtype: 0x9ba
   __TEXT.__objc_stubs: 0x2220
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__const: 0x1b0

   __DATA_CONST.__objc_selrefs: 0xaf0
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__objc_const: 0x1518

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FBF5F6F-394A-30C5-9D55-9890F797740F
+  UUID: CBA0D4D9-2A72-31FB-999C-FBB55ABB6798
   Functions: 159
-  Symbols:   1039
-  CStrings:  719
+  Symbols:   1040
+  CStrings:  722
 
Symbols:
+ -[HDSHBreathingDisturbanceAnalysisScheduler _runCompletionIfExistsWithResult:retryInterval:shouldUpdateActivityCriteria:]
+ _HDStringFromPeriodicActivityResult
+ _OBJC_IVAR_$_HDSHBreathingDisturbanceAnalysisScheduler._periodicActivityCompletion
+ _OBJC_IVAR_$_HDSHBreathingDisturbanceAnalysisScheduler._periodicActivityCompletionLock
+ _objc_msgSend$_runCompletionIfExistsWithResult:retryInterval:shouldUpdateActivityCriteria:
- -[HDSHBreathingDisturbanceAnalysisScheduler _runCompletionIfExistsWithResult:retryInterval:]
- _OBJC_IVAR_$_HDSHBreathingDisturbanceAnalysisScheduler._completion
- _OBJC_IVAR_$_HDSHBreathingDisturbanceAnalysisScheduler._completionLock
- _objc_msgSend$_runCompletionIfExistsWithResult:retryInterval:
Functions:
~ -[HDSHBreathingDisturbanceAnalysisScheduler performPeriodicActivity:completion:] : 832 -> 884
~ -[HDSHBreathingDisturbanceAnalysisScheduler _runCompletionIfExistsWithResult:retryInterval:] -> -[HDSHBreathingDisturbanceAnalysisScheduler _runCompletionIfExistsWithResult:retryInterval:shouldUpdateActivityCriteria:] : 128 -> 472
~ -[HDSHBreathingDisturbanceAnalysisScheduler _requestBreathingDisturbanceAnalysisIfNeeded] : 1944 -> 1964
CStrings:
+ "[%{public}@] Calling completion with task result: %@, retry interval %f"
+ "[%{public}@] Request was processed, completion will be called when request is complete."
+ "[%{public}@] nil completion block; unless healthd has just launched, this is unexpected."
+ "[%{public}@] performPeriodicActivity called, but we already have a completion from a previous call; overwriting with a new one."
+ "_periodicActivityCompletion"
+ "_periodicActivityCompletionLock"
+ "_runCompletionIfExistsWithResult:retryInterval:shouldUpdateActivityCriteria:"
+ "v36@0:8q16d24B32"
- "[%{public}@] Request was processed, but completion exists before capture."
- "_completion"
- "_completionLock"
- "_runCompletionIfExistsWithResult:retryInterval:"
- "v32@0:8q16d24"

```
