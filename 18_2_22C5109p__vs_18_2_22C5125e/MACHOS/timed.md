## timed

> `/usr/libexec/timed`

```diff

-334.0.0.0.0
-  __TEXT.__text: 0x188c4
+334.0.2.0.0
+  __TEXT.__text: 0x18ef8
   __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x2620
-  __TEXT.__objc_methlist: 0xba0
+  __TEXT.__objc_stubs: 0x2740
+  __TEXT.__objc_methlist: 0xc08
   __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x2014
-  __TEXT.__oslogstring: 0x2a0d
-  __TEXT.__objc_methname: 0x238f
-  __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methtype: 0x504
+  __TEXT.__cstring: 0x2050
+  __TEXT.__oslogstring: 0x2ad6
+  __TEXT.__objc_methname: 0x24d0
+  __TEXT.__objc_classname: 0x13d
+  __TEXT.__objc_methtype: 0x53f
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__unwind_info: 0x578
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0xdb0
-  __DATA_CONST.__cfstring: 0x2bc0
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__cfstring: 0x2c00
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x2420
-  __DATA.__objc_selrefs: 0xa50
-  __DATA.__objc_ivar: 0x17c
-  __DATA.__objc_data: 0x320
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x2510
+  __DATA.__objc_selrefs: 0xaa0
+  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_data: 0x370
   __DATA.__data: 0x310
   __DATA.__bss: 0x140
   __DATA.__common: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 539
-  Symbols:   258
-  CStrings:  1303
+  Functions: 548
+  Symbols:   259
+  CStrings:  1326
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
CStrings:
+ "334.0.2"
+ "@\"TMTimeSynthesizerMonitor\""
+ "SynthesizerMonitor: ntp_rejects: %!d(MISSING) apns_rejects: %!d(MISSING)"
+ "T@\"NSMutableDictionary\",V_sourceRejects"
+ "TMTimeSynthesizerMonitor"
+ "_sourceRejects"
+ "com.apple.timed.consecutiveRejectsByInput"
+ "dictionaryWithDictionary:"
+ "dictionaryWithSharedKeySet:"
+ "monitor"
+ "numberWithInteger:"
+ "report_reason"
+ "resetRejectCountsForReason:rtc:"
+ "resetting reject counts"
+ "sendConsecutiveRejectsAnalyticsAtRtc:forReason:withTime:"
+ "setSourceRejects:"
+ "sharedKeySetForKeys:"
+ "shouldReset"
+ "source %!@(MISSING) has been rejected by Secure Filter, incrementing count"
+ "source %!@(MISSING) is not being tracked by TMTimeSynthesizerMonitor"
+ "sourceRejects"
+ "synthesizer:rejectedTimeInput:"
+ "v32@0:8q16d24"
+ "v40@0:8d16q24@32"
- "334"

```
