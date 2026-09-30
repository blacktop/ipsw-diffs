## tailspind

> `/usr/libexec/tailspind`

```diff

-218.2.0.0.0
-  __TEXT.__text: 0xd40c
+234.0.0.0.0
+  __TEXT.__text: 0xd544
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_stubs: 0x900
-  __TEXT.__objc_methlist: 0x1c4
+  __TEXT.__objc_stubs: 0x920
+  __TEXT.__objc_methlist: 0x1dc
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0xff6
-  __TEXT.__objc_methname: 0xbd2
-  __TEXT.__oslogstring: 0x256d
+  __TEXT.__cstring: 0x100c
+  __TEXT.__objc_methname: 0xc06
+  __TEXT.__oslogstring: 0x25ba
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238

   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x408
-  __DATA_CONST.__cfstring: 0x580
+  __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2a0
-  __DATA.__objc_selrefs: 0x2d0
-  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_const: 0x2d0
+  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2160
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x580
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/kperf.framework/kperf

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: FC134EF0-2CB7-3B2D-971C-A1EF9548136D
-  Functions: 240
+  UUID: 591A5355-AD80-31E1-8AF6-7622BF104407
+  Functions: 243
   Symbols:   242
-  CStrings:  474
+  CStrings:  482
 
CStrings:
+ "NumEvents"
+ "TQ,N,V_numEvents"
+ "_numEvents"
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "hangtracerd"
+ "numEvents"
+ "setNumEvents:"

```
