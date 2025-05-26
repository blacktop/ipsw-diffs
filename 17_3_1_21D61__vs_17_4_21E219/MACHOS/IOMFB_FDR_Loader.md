## IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

```diff

-336.3.6.0.0
-  __TEXT.__text: 0x1a724
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__gcc_except_tab: 0x12c
+337.5.36.0.0
+  __TEXT.__text: 0x1e31c
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__gcc_except_tab: 0x118
   __TEXT.__const: 0x1a00
-  __TEXT.__cstring: 0x52f1
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__cstring: 0x5778
+  __TEXT.__unwind_info: 0x474
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x340
   __DATA.__bss: 0x1bd0a
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 288
-  Symbols:   121
-  CStrings:  609
+  Functions: 336
+  Symbols:   122
+  CStrings:  631
 
Symbols:
+ _AMFDRSealingMapCopyInstanceForClass
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
CStrings:
+ "UserCal: powering down"
+ "UserCal: powering up \n"
+ "basic_string"
+ "parser_error: Counted vectors [%d][%d] mismatch expected [%d][%d]\n"
+ "parser_error: Duplicate PTUC table vers=%d (bright=%d, temp=%d) found in input.\n"
+ "parser_error: Duplicate elvs table temperature=%d found in input.\n"
+ "parser_error: Failed to sort EMMP tables"
+ "parser_error: Failed to sort async PCS tables"
+ "parser_error: Failed to sort sync PCS tables"
+ "parser_error: PCS tables are NULL"
+ "parser_error: Vector exceeding max i count: %u > %u\n"
+ "parser_error: Vector exceeding max j count: %u > %u\n"
+ "parser_error: failed to set ELVS LUT temperatue %d\n"
+ "parser_error: failed to set ELVS table config"
+ "parser_error: mismatching versions: %u != 1,2,3,6\n"
+ "parser_error: mismatching versions: %u != 1,3,6\n"
+ "parser_error: missing EMMP (T%d B%d) or gray scales (sync T%d B%d async T%d B%d)\n"
+ "parser_error: out of memory for PCS table copy"
+ "parser_error: parsing did not consume the full EMMP size"
+ "parser_error: too many EM scale intervals %d\n"
+ "parser_error: underflow while reading EMMP spare"
+ "parser_error: unsupported async PCS brightness count: %u > %u\n"
+ "parser_error: unsupported async PCS temperature count: %u > %u\n"
+ "parser_error: unsupported sync PCS brightness count: %u > %u\n"
+ "parser_error: unsupported sync PCS temperature count: %u > %u\n"
+ "parser_info: set ELVS table config succeeded"
+ "parser_info: set EVLS LUTs succeeded"
- "ScreenSerialNumber"
- "YVNo6vlMjhgQ9yGYV8gatw"
- "parser_error: Duplicate PTUC table bright=%d found in input.\n"
- "parser_error: mismatching versions: %u != 1,2,3\n"
- "parser_error: mismatching versions: %u != 1,3\n"

```
