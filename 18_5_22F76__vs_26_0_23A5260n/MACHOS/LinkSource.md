## LinkSource

> `/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/LinkSource.bundle/LinkSource`

```diff

-68.0.0.0.0
-  __TEXT.__text: 0x7fd4
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x824
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xa69
-  __TEXT.__objc_methname: 0x1729
-  __TEXT.__oslogstring: 0xc5b
+71.0.0.0.0
+  __TEXT.__text: 0x83b8
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x88c
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xa91
+  __TEXT.__objc_methname: 0x17df
+  __TEXT.__oslogstring: 0xd73
   __TEXT.__objc_classname: 0x98
-  __TEXT.__objc_methtype: 0xc90
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x280
+  __TEXT.__objc_methtype: 0xca5
+  __TEXT.__unwind_info: 0x248
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__cfstring: 0x9c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x150
-  __DATA.__objc_const: 0x1020
-  __DATA.__objc_selrefs: 0x668
-  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_const: 0x1090
+  __DATA.__objc_selrefs: 0x6a0
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x1e8
   __DATA.__common: 0x10

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0FFE06A-52CC-36A4-9323-E20621A20E87
-  Functions: 201
-  Symbols:   149
-  CStrings:  637
+  UUID: FE282D4E-1172-3B32-A983-711E1E203806
+  Functions: 210
+  Symbols:   151
+  CStrings:  657
 
Symbols:
+ _clock_gettime_nsec_np
+ _kTMMonotonicClockDrift
CStrings:
+ "-[TMLSLinkSource linkBecameCompatible:]"
+ "Not sending reset because backoff interval has not elapsed"
+ "TQ,N,V_lastReset"
+ "Ti,N,V_resetAttempts"
+ "_lastReset"
+ "_resetAttempts"
+ "d16@0:8"
+ "elapsed: %f pUncertainty: %f maxDrift: %f allowedError: %f"
+ "lastReset"
+ "linkBecameCompatible:"
+ "nextResetDebounceInterval"
+ "now: %llu lastReset: %llu elapsed: %llu backoff: %f resetAttempts: %d"
+ "resetAttempts"
+ "sending reset because backoff interval has elapsed"
+ "setLastReset:"
+ "setResetAttempts:"
+ "timeWasReset:"
+ "timeWasReset: resetting throttling state"
+ "v24@0:8Q16"

```
