## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1739.0.0.0.0
-  __TEXT.__text: 0x6714c
-  __TEXT.__auth_stubs: 0x1b70
-  __TEXT.__objc_stubs: 0x48a0
-  __TEXT.__objc_methlist: 0x2250
+1740.40.2.0.0
+  __TEXT.__text: 0x677cc
+  __TEXT.__auth_stubs: 0x1b90
+  __TEXT.__objc_stubs: 0x4920
+  __TEXT.__objc_methlist: 0x2278
   __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0x63e0
-  __TEXT.__objc_methname: 0x5fa4
-  __TEXT.__oslogstring: 0xb516
+  __TEXT.__cstring: 0x63fb
+  __TEXT.__objc_methname: 0x6035
+  __TEXT.__oslogstring: 0xb6d4
   __TEXT.__objc_classname: 0x2fe
-  __TEXT.__objc_methtype: 0x7be
+  __TEXT.__objc_methtype: 0x81e
   __TEXT.__gcc_except_tab: 0x498
   __TEXT.__dlopen_cstrs: 0x2b2
   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x11a0
-  __DATA_CONST.__auth_got: 0xdc8
+  __DATA_CONST.__auth_got: 0xdd8
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__cfstring: 0x6cc0
+  __DATA_CONST.__cfstring: 0x6d20
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x330
-  __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__objc_dictobj: 0x118
+  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x2e8
-  __DATA.__objc_const: 0x4a20
-  __DATA.__objc_selrefs: 0x1710
-  __DATA.__objc_ivar: 0x360
+  __DATA.__objc_const: 0x4a50
+  __DATA.__objc_selrefs: 0x1738
+  __DATA.__objc_ivar: 0x364
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xa0c
   __DATA.__common: 0x1138

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2156
-  Symbols:   560
-  CStrings:  3555
+  Functions: 2166
+  Symbols:   562
+  CStrings:  3576
 
Symbols:
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
CStrings:
+ " "
+ "AppleBatteryAuth indicates auth unknown/failure, still continue..."
+ "Auth has failed/state Unknown"
+ "Could not create ppsId with subsystem BatteryTrustedData and Daily as BatteryTrustedData"
+ "Daily"
+ "Nil payload. Nothing to send to PPS"
+ "No CoreAccessories Framework to run, EXIT"
+ "PPS request object not found. Unable to send data to powerlog"
+ "T^{PPSTelemetryIdentifier=},V_ppsId"
+ "Trusted Data feature disabled, EXIT"
+ "Using updated wRA %!d(MISSING) from trusted battery data after %!l(MISSING)lu secs\n"
+ "^{PPSTelemetryIdentifier=}"
+ "^{PPSTelemetryIdentifier=}16@0:8"
+ "_ppsId"
+ "dictionaryWithDictionary:"
+ "doNotRunAnymore is true, return and dont set any more timers"
+ "ppsId"
+ "ppsId created with subsystem BatteryTrustedData and Daily as BatteryTrustedData"
+ "sendToPPS:"
+ "setPpsId:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "v24@0:8^{PPSTelemetryIdentifier=}16"
- "AppleBatteryAuth indicates auth failure, still continue..."
- "doNotRunAnymore is true, return and dont set any more timers "

```
