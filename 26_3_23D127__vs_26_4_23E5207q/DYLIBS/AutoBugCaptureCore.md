## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-411.80.3.0.0
-  __TEXT.__text: 0x792ec
-  __TEXT.__auth_stubs: 0xff0
+411.100.13.0.0
+  __TEXT.__text: 0x7edb0
+  __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x5f7c
-  __TEXT.__cstring: 0x510c
+  __TEXT.__cstring: 0x513b
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xef8e
-  __TEXT.__gcc_except_tab: 0x10c0
+  __TEXT.__oslogstring: 0xf029
+  __TEXT.__gcc_except_tab: 0x11b4
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x59ac
-  __TEXT.__unwind_info: 0x1570
+  __TEXT.diag_actions: 0x5d43
+  __TEXT.__unwind_info: 0x1950
   __TEXT.__objc_classname: 0xa08
-  __TEXT.__objc_methname: 0xe702
+  __TEXT.__objc_methname: 0xe71d
   __TEXT.__objc_methtype: 0x23cb
-  __TEXT.__objc_stubs: 0xa3c0
-  __DATA_CONST.__got: 0x4f0
+  __TEXT.__objc_stubs: 0xa400
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__const: 0x2790
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3700
+  __DATA_CONST.__objc_selrefs: 0x3710
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x668
-  __AUTH_CONST.__auth_got: 0x808
+  __DATA_CONST.__objc_arraydata: 0x5d8
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6b00
+  __AUTH_CONST.__cfstring: 0x6ac0
   __AUTH_CONST.__objc_const: 0xc888
-  __AUTH_CONST.__objc_dictobj: 0x5f0
+  __AUTH_CONST.__objc_dictobj: 0x500
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x480
+  __AUTH_CONST.__objc_arrayobj: 0x420
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x68c
   __DATA.__data: 0xd20
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x240
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x148

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 581C4B63-75E6-3672-A091-3BE08B482D82
-  Functions: 2251
-  Symbols:   8166
-  CStrings:  5929
+  UUID: 652EBA43-FB53-3B8D-B598-2C3232BFD61E
+  Functions: 2258
+  Symbols:   8187
+  CStrings:  5932
 
Symbols:
+ _IOServiceNameMatching
+ _OBJC_EHTYPE_$_NSException
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.226
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.227
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.229
+ ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.155
+ ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.192
+ ___block_literal_global.132
+ _handleServiceInterest
+ _nvmeIterator
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$reason
+ _scsiIterator
+ _sdxcIterator
+ _strnlen
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.269
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.270
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.272
- ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.198
- ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.235
- ___block_literal_global.175
- _iterator
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "AppleSCSISubsystemGlobals"
+ "IONVMeController"
+ "IONVMeFamily"
+ "IOSCSIFamily"
+ "StorageDriversContextUnknown"
+ "StorageDriversSubTypeUnknown"
+ "StorageDriversTypeUnknown"
+ "StorageDrivers_listener"
+ "StorageKernelSignal: %@ error detected. Requesting ABC T:%@ ST:%@ \n"
+ "StorageKernelSignal: %@ failed 0x%x\n"
+ "StorageKernelSignal: Error: Exception caught: %s - %s"
+ "StorageKernelSignal: Signature Setup Error: Exception caught: %s - %s"
+ "StorageKernelSignal: unknown error type %x\n"
+ "initWithUTF8String:"
- "CardDowntrainError"
- "Proxima"
- "StorageKernelSignal: Session %{public}@ accepted. (%@)"
- "StorageKernelSignal: downtrain error detected. Triggering ABC\n"
- "Thread"
- "WiFi Watchdog"
- "com.apple.DiagnosticExtensions.ConnectivityDE"
- "proxima"
- "proxima-diags"
- "sdxc_listener"

```
