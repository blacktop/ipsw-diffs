## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-383.120.2.0.0
-  __TEXT.__text: 0x77900
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x5f44
-  __TEXT.__cstring: 0x502b
+411.0.5.0.0
+  __TEXT.__text: 0x79140
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_methlist: 0x5f5c
+  __TEXT.__cstring: 0x5066
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xeede
+  __TEXT.__oslogstring: 0xef8e
   __TEXT.__gcc_except_tab: 0x10c0
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x54c4
-  __TEXT.__unwind_info: 0x1590
+  __TEXT.__unwind_info: 0x1578
   __TEXT.__objc_classname: 0xa08
-  __TEXT.__objc_methname: 0xe5b3
+  __TEXT.__objc_methname: 0xe65d
   __TEXT.__objc_methtype: 0x231c
-  __TEXT.__objc_stubs: 0xa2c0
-  __DATA_CONST.__got: 0x510
+  __TEXT.__objc_stubs: 0xa3a0
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__const: 0x2790
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36b0
+  __DATA_CONST.__objc_selrefs: 0x36e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x5b0
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x69e0
-  __AUTH_CONST.__objc_const: 0xc848
+  __AUTH_CONST.__cfstring: 0x6a00
+  __AUTH_CONST.__objc_const: 0xc878
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x688
-  __DATA.__data: 0xce0
+  __DATA.__objc_ivar: 0x68c
+  __DATA.__data: 0xce8
   __DATA.__bss: 0x238
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x150
-  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__common: 0xc
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 72A3EDC6-9E16-3A4F-9CC4-D56061D3A4FE
-  Functions: 2248
-  Symbols:   8145
-  CStrings:  5885
+  UUID: 398E36F1-3A7A-3806-BF37-AE3A5EE12EA9
+  Functions: 2250
+  Symbols:   8159
+  CStrings:  5904
 
Symbols:
+ -[ABCAdministrator administrativelyDisableAutoBugCapture]
+ -[ABCPreferences diagnosticPipelineEnabled]
+ -[ABCPreferences setDiagnosticPipelineEnabled:]
+ _CFStringGetLength
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _OBJC_IVAR_$_ABCPreferences._diagnosticPipelineEnabled
+ __DPCGetUploadServiceEnablement
+ _archive_entry_pathname
+ _kNetDiagOptMarkPurgeable
+ _objc_msgSend$_setError
+ _objc_msgSend$administrativelyDisableAutoBugCapture
+ _objc_msgSend$data
+ _objc_msgSend$diagnosticPipelineEnabled
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- -[ABCAdministrator administrativelyDiableAutoBugCapture]
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _objc_msgSend$administrativelyDiableAutoBugCapture
CStrings:
+ " due to override"
+ "%s: Truncated write; file may have grown while being archived (tried to write %ld bytes but wrote %ld bytes)"
+ "AutoBugCapture is %s - DNU:%d, user consent:%d, automated device group:%d%s, DP:%sabled, ABC:%savailable, ABC features:%d"
+ "BuildVersion"
+ "DiagnosticPipeline is %sabled%s"
+ "DiagnosticPipeline: %sabled -> %sabled%s"
+ "Error (%s) writing file '%@'"
+ "Failed to get serial number"
+ "ProductName"
+ "ProductVersion"
+ "Rejecting case id %{public}@ with signature %{public}@ (%{public}@)"
+ "TB,N,V_diagnosticPipelineEnabled"
+ "Unable to determine product type!"
+ "Unable to get sub product type, falling back to product type"
+ "_diagnosticPipelineEnabled"
+ "_setError"
+ "administrativelyDisableAutoBugCapture"
+ "data"
+ "diagnosticPipelineEnabled"
+ "dis"
+ "en"
+ "getBytes:range:"
+ "position"
+ "purgeable"
+ "setDiagnosticPipelineEnabled:"
+ "setPosition:"
- "AutoBugCapture is %s - DNU:%d, user consent:%d, automated device group:%d%s, ABC:%savailable, ABC features:%d"
- "Enabling NPI flag based on baseband chipset match"
- "Enabling NPI flag based on productType match"
- "Error (%s) writing file %@: request to write %ld bytes but wrote %ld bytes"
- "Rejecting case id %@{public} with signature %{public}@ (%{public}@)"
- "administrativelyDiableAutoBugCapture"
- "iPhone15"
- "mav22"

```
