## timed

> `/usr/libexec/timed`

```diff

-334.0.4.1.0
-  __TEXT.__text: 0x186f4
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_stubs: 0x2680
-  __TEXT.__objc_methlist: 0xf04
+334.0.12.0.0
+  __TEXT.__text: 0x18b8c
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_stubs: 0x26c0
+  __TEXT.__objc_methlist: 0xf1c
   __TEXT.__const: 0x278
-  __TEXT.__objc_methname: 0x24ff
-  __TEXT.__cstring: 0x1f5b
+  __TEXT.__objc_methname: 0x2541
+  __TEXT.__cstring: 0x2006
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0x54f
-  __TEXT.__oslogstring: 0x2ad6
+  __TEXT.__objc_methtype: 0x56f
+  __TEXT.__oslogstring: 0x2ae2
   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x5d8
-  __DATA_CONST.__auth_got: 0x5c8
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0xdb8
-  __DATA_CONST.__cfstring: 0x29c0
+  __TEXT.__unwind_info: 0x5f0
+  __DATA_CONST.__auth_got: 0x5e0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__cfstring: 0x2b40
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__objc_intobj: 0x588
+  __DATA_CONST.__objc_intobj: 0x5b8
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2130
-  __DATA.__objc_selrefs: 0xb20
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_const: 0x2150
+  __DATA.__objc_selrefs: 0xb38
+  __DATA.__objc_ivar: 0x190
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x310
   __DATA.__bss: 0x140

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7476FF7A-F68F-35F5-8459-E86730E9C1A3
-  Functions: 599
-  Symbols:   251
-  CStrings:  1647
+  UUID: 1DE53349-480B-348D-8CB1-04F8ACC0A83D
+  Functions: 604
+  Symbols:   253
+  CStrings:  1676
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
- _XPC_ACTIVITY_INTERVAL_1_MIN
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _xpc_activity_unregister
- _xpc_retain
CStrings:
+ "/var/db/timed/TimeZoneRules.plist"
+ "334.0.12"
+ "@\"NSObject<OS_dispatch_source>\""
+ "Error requesting heartbeat job with status %lu"
+ "Handling heartbeat execution"
+ "LocationBorder"
+ "MAAssetRetryInterval"
+ "NTP job timer fired"
+ "OTA rules plist not found: %@!\n"
+ "ResetDueToRejects"
+ "Scheduling wanted job to fire in %f seconds"
+ "TMResetPreserveCache"
+ "TMSoftReset"
+ "_fetchAttemptTimer"
+ "cached state"
+ "com.apple.timed.heartbeat"
+ "defaultNTPServer"
+ "estimatePresent"
+ "estimateUncertainty"
+ "not fetching %@ due to same technology as %@"
+ "not recomputing because %@ and %@ come from same technology"
+ "not recomputing because %@ source is not fetchable"
+ "prepareForExit"
+ "previousRejectsExist"
+ "proactiveBBFetchTimer"
+ "resetThreshholdReached"
+ "shouldPreserveCache: %d"
+ "softReset"
+ "timeSinceNTPFetch"
+ "timeWasReset:"
+ "valueForKey:"
- "334.0.4.1"
- "Error requesting proactive time check job with status %lu"
- "NTP job satisfied, state: %lu"
- "Received unknown job status %lu"
- "Scheduling wanted job"
- "SynthesizerMonitor: ntp_rejects: %d apns_rejects: %d"
- "Td,V_lastReschedule"
- "_lastReschedule"
- "accessory input rejected by secure filter"
- "com.apple.timed.check-active"
- "com.apple.timed.ntp.wanted"
- "lastReschedule"
- "not rescheduling NTP fetch activity because interval has not elapsed lastReschedule: %f wanted time: %f, elapsed %f"
- "setLastReschedule:"
- "shouldReset"

```
