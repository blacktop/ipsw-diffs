## com.apple.telemetry

> `/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry`

```diff

-498.120.2.0.0
-  __TEXT.__text: 0x8804
+505.0.0.0.0
+  __TEXT.__text: 0x8c40
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_stubs: 0x340
   __TEXT.__const: 0x14b
-  __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__cstring: 0x9c5
-  __TEXT.__oslogstring: 0x4043
+  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__cstring: 0x9df
+  __TEXT.__oslogstring: 0x436d
   __TEXT.__objc_classname: 0x3
-  __TEXT.__objc_methname: 0x202
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__objc_methname: 0x213
+  __TEXT.__unwind_info: 0x150
   __DATA.__auth_got: 0x3d0
   __DATA.__got: 0xc0
-  __DATA.__auth_ptr: 0x8
+  __DATA.__auth_ptr: 0x10
   __DATA.__const: 0x258
-  __DATA.__cfstring: 0x400
+  __DATA.__cfstring: 0x420
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_selrefs: 0xd0
   __DATA.__objc_intobj: 0x18
   __DATA.__data: 0x8
   __DATA.__bss: 0x80

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8E3A09DB-03F0-3F70-B019-BD8C15E7FD97
-  Functions: 148
+  UUID: BA6F80E7-D398-3494-8743-77BE957E95A3
+  Functions: 151
   Symbols:   153
-  CStrings:  297
+  CStrings:  306
 
Symbols:
+ _DRTailspinRequest
- _objc_retain_x28
CStrings:
+ "DRTailspinRequest not available, unable to gather and upload tailspin"
+ "Gathered tailspin via DR for %@ (%@)\n%@"
+ "PMI adjustment: Have a pending change to rate %llu->%llu and/or override %d->%d, not checking daily budget"
+ "PMI adjustment: No compressed bytes written since last cleanup (%llu uncompressed), assuming compression ratio of 1.0. time_since_cleanup:%.0fs time_since_adjustment:%.0fs all_bytes_since_cleanup:%llu all_bytes_since_adjustment:%llu pmi_percent:%.0f%% pmi_interval:%llu quota:%llu"
+ "PMI adjustment: projected_pmi_remaining_compressed_bytes_written_in_the_day is 0, resetting to defaults. time_since_cleanup:%.0fs time_since_adjustment:%.0fs all_bytes_since_cleanup:%llu all_bytes_since_adjustment:%llu pmi_percent:%.0f%% pmi_interval:%llu quota:%llu"
+ "Unable to gather and upload DR tailspin: %@"
+ "com.apple.microstackshots"
+ "debugDescription"
+ "pmi_interval_to_equal_nonpmi_datarate:%llu (no non-PMI, so max)"
- "DR not supported: not gathering tailspin via DR for %@ (%@)\n%@"

```
