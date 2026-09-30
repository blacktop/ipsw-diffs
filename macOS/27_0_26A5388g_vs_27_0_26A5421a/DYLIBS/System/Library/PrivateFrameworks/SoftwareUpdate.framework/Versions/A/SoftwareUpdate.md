## SoftwareUpdate

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate`

```diff

-2412.0.5.0.0
-  __TEXT.__text: 0x7ca80
-  __TEXT.__objc_methlist: 0x64dc
+2412.1.1.0.0
+  __TEXT.__text: 0x7ca64
+  __TEXT.__objc_methlist: 0x64ac
   __TEXT.__const: 0x670
   __TEXT.__gcc_except_tab: 0x12a8
-  __TEXT.__cstring: 0x844c
-  __TEXT.__oslogstring: 0xb44b
+  __TEXT.__cstring: 0x8482
+  __TEXT.__oslogstring: 0xb49c
   __TEXT.__dof_SoftwareU: 0xc20
-  __TEXT.__unwind_info: 0x21f8
+  __TEXT.__unwind_info: 0x2200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa78
+  __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f58
+  __DATA_CONST.__objc_selrefs: 0x3f48
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x718
   __AUTH_CONST.__const: 0x29e0
-  __AUTH_CONST.__cfstring: 0x73a0
-  __AUTH_CONST.__objc_const: 0x8980
+  __AUTH_CONST.__cfstring: 0x73c0
+  __AUTH_CONST.__objc_const: 0x8940
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_got: 0x800

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 3206
-  Symbols:   6325
-  CStrings:  1978
+  Functions: 3204
+  Symbols:   6317
+  CStrings:  1981
 
Symbols:
+ -[SUHelperProxy registerProductFile:forProductKey:firmware:trustLevel:inForeground:]
+ -[SUSharedPrefs(ScanStatus) isLastScanResultSuccess]
+ -[SUSharedPrefs(ScanStatus) lastCatalogChangeDate]
+ -[SUSharedPrefs(ScanStatus) lastSuccessfulMSUBackgroundActionDate]
+ -[SUSharedPrefs(ScanStatus) lastSuccessfulMSUScanDate]
+ -[SUSharedPrefs(ScanStatus) setLastSuccessfulMSUBackgroundActionDate:]
+ -[SUSharedPrefs(ScanStatus) setLastSuccessfulMSUScanDate:]
+ GCC_except_table25
+ GCC_except_table73
+ GCC_except_table76
+ ___84-[SUHelperProxy registerProductFile:forProductKey:firmware:trustLevel:inForeground:]_block_invoke
+ ___block_descriptor_74_e8_32o40o48o56r_e5_v8?0l
+ _objc_msgSend$initSharedReporterStoringToPath:
+ _objc_msgSend$registerProductFile:forProductKey:firmware:trustLevel:inForeground:
- -[SUHelperProxy registerProductFile:forProductKey:firmware:trustLevel:keepOriginal:]
- -[SUHelperProxy registerProductFile:forProductKey:firmware:trustLevel:keepOriginal:inForeground:]
- -[SUPreferenceManager isLastScanResultSuccess]
- -[SUPreferenceManager lastCatalogChangedDate]
- -[SUPreferenceManager lastFullScanSuccessfulDate]
- -[SUPreferenceManager lastScanSuccessfulDate]
- -[SUPreferenceManager setLastSuccessfulScanDate:]
- -[SUSharedPrefs(ScanStatus) lastCatalogChangeDate:]
- -[SUSharedPrefs(ScanStatus) lastSuccessfulMSUBackgroundScanDate]
- -[SUSharedPrefs(ScanStatus) setLastSuccessfulMSUBackgroundScanDate:]
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table81
- GCC_except_table84
- _SUScanPrefLastCatalogChangeDateKey
- _SUScanPrefLastFullSuccessfulDateKey
- _SUScanPrefLastSuccessfulDateKey
- ___97-[SUHelperProxy registerProductFile:forProductKey:firmware:trustLevel:keepOriginal:inForeground:]_block_invoke
- ___block_descriptor_75_e8_32o40o48o56r_e5_v8?0l
- _objc_msgSend$lastScanResultCode
- _objc_msgSend$registerProductFile:forProductKey:firmware:trustLevel:keepOriginal:inForeground:
CStrings:
+ "%s: confstr(_CS_DARWIN_USER_CACHE_DIR failed %d, falling back to sharedReporter."
+ "-[SUTelemetryReporter init]"
+ "LastExecutedMSUBackgroundActionDate"
+ "LastSuccessfulMSUScanDate"
- "LastSuccessfulBackgroundMSUScanDate"
```
