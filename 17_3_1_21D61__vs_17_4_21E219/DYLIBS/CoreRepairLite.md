## CoreRepairLite

> `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`

```diff

-376.60.3.0.0
-  __TEXT.__text: 0x88e8
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1f4
+397.100.12.0.0
+  __TEXT.__text: 0x89c4
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0x5f
-  __TEXT.__oslogstring: 0x140d
-  __TEXT.__cstring: 0x341
+  __TEXT.__oslogstring: 0x13e1
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0x10c
+  __TEXT.__cstring: 0x399
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x74a
-  __TEXT.__objc_methtype: 0x14a
-  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methname: 0x776
+  __TEXT.__objc_methtype: 0x14d
+  __TEXT.__objc_stubs: 0x940
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x100
-  __DATA_CONST.__objc_selrefs: 0x288
-  __AUTH_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__objc_selrefs: 0x2a0
+  __DATA_CONST.__objc_classrefs: 0x88
+  __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__objc_const: 0xd8
+  __AUTH_CONST.__cfstring: 0x400
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0x78
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B006D257-0CE0-3591-969F-E21FC67E1FC8
-  Functions: 172
-  Symbols:   131
-  CStrings:  332
+  UUID: D63AE61B-ADDF-30A2-BCAB-516FC1B51209
+  Functions: 170
+  Symbols:   133
+  CStrings:  336
 
Symbols:
+ _AMFDRSealingMapCopyPropertyWithTag
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSSet
+ __os_log_debug_impl
- _AMFDRDiagnosticGenerateReport
- _objc_retain_x21
- _objc_retain_x23
CStrings:
+ "Failed to decode sealing manifest: %@"
+ "Failed to get local sealing manifest"
+ "Live instance missing for %@: %@"
+ "Live property missing for %@: %@"
+ "Number of data classes and instances mismatches"
+ "Property %@ does not exist"
+ "Unsealed: %@"
+ "^{__AMFDR=}16@0:8"
+ "_createFDRLocal"
+ "arrayWithObjects:count:"
+ "dictionary"
+ "drp#"
+ "findUnsealedDataWithError:"
+ "localizedDescription"
+ "minusSet:"
+ "setWithArray:"
- "B32@0:8@16^B24"
- "Cannot create options"
- "Cannot generate FDR diagnostic report"
- "FDR diagnostic report not found"
- "FailureData"
- "Found mismatch data class: %@"
- "LiveInstance"
- "SealedInstance"
- "Validating data classes: %@"
- "allKeys"
- "checkMismatch:failureDataList:"
- "getDiagnosticReport"
- "hasAnyMismatched:success:"

```
