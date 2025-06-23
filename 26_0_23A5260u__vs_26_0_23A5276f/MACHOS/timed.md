## timed

> `/usr/libexec/timed`

```diff

-334.0.12.0.0
-  __TEXT.__text: 0x18b8c
+334.0.15.0.0
+  __TEXT.__text: 0x1800c
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_stubs: 0x26c0
-  __TEXT.__objc_methlist: 0xf1c
+  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__objc_methlist: 0xd6c
   __TEXT.__const: 0x278
-  __TEXT.__objc_methname: 0x2541
-  __TEXT.__cstring: 0x2006
-  __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0x56f
+  __TEXT.__objc_methname: 0x2397
+  __TEXT.__cstring: 0x1fce
+  __TEXT.__objc_classname: 0x11d
+  __TEXT.__objc_methtype: 0x53e
   __TEXT.__oslogstring: 0x2ae2
   __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__unwind_info: 0x5b8
   __DATA_CONST.__auth_got: 0x5e0
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__cfstring: 0x2b40
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__cfstring: 0x2a40
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x5b8
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2150
-  __DATA.__objc_selrefs: 0xb38
-  __DATA.__objc_ivar: 0x190
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_const: 0x1e10
+  __DATA.__objc_selrefs: 0xad8
+  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_data: 0x370
   __DATA.__data: 0x310
   __DATA.__bss: 0x140
   __DATA.__common: 0x10

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 1DE53349-480B-348D-8CB1-04F8ACC0A83D
-  Functions: 604
-  Symbols:   253
-  CStrings:  1676
+  UUID: A186E825-3DE2-39B2-B1B9-48FEBFD57656
+  Functions: 570
+  Symbols:   254
+  CStrings:  1627
 
Symbols:
+ _OBJC_CLASS_$_TMTime
CStrings:
+ "334.0.15"
- "%"
- "334.0.12"
- "@56@0:8d16d24d32d40@48"
- "@64@0:8q16d24q32d40d48@56"
- "ConvenienceConversions"
- "T@\"NSString\",C,N,V_source"
- "TB,N,GisSynthesized,V_synthesized"
- "TB,N,V_reliability"
- "TMTime"
- "Td,N"
- "Td,N,V_sf"
- "Td,N,V_sfUnc"
- "Td,N,V_utcUnc_s"
- "Tq,N,V_rtc_ns"
- "Tq,N,V_utc_ns"
- "XPCConversions"
- "_reliability"
- "_rtc_ns"
- "_sf"
- "_sfUnc"
- "_synthesized"
- "_utcUnc_s"
- "_utc_ns"
- "copy"
- "decodeInt64ForKey:"
- "encodeInt64:forKey:"
- "initWithUtc_ns:utcUnc_s:rtc_ns:sf:sfUnc:source:"
- "isEquivalent:"
- "reliability"
- "rtc_ns"
- "setRtc_ns:"
- "setUtc_ns:"
- "sfUnc"
- "synthesized"
- "timeWithUtc_s:utcUnc_s:rtc_s:sf:source:"
- "utc_ns"

```
