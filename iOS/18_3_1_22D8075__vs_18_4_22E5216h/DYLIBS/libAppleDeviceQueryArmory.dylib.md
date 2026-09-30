## libAppleDeviceQueryArmory.dylib

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libAppleDeviceQueryArmory.dylib`

```diff

-331.80.3.0.0
-  __TEXT.__text: 0x21ef8
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0x7ec
-  __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0xa4b3
-  __TEXT.__gcc_except_tab: 0x188
+340.100.16.0.0
+  __TEXT.__text: 0x215d8
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_methlist: 0x7e4
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0xa0b3
+  __TEXT.__gcc_except_tab: 0x160
   __TEXT.__oslogstring: 0x1a6
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__objc_classname: 0x219
-  __TEXT.__objc_methname: 0x1c0d
+  __TEXT.__objc_methname: 0x1bee
   __TEXT.__objc_methtype: 0x338
   __TEXT.__objc_stubs: 0x1b40
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x820
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x938
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__objc_arraydata: 0x9f8
+  __AUTH_CONST.__auth_got: 0x4d0
+  __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x81c0
+  __AUTH_CONST.__cfstring: 0x7ee0
   __AUTH_CONST.__objc_const: 0xe38
-  __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH_CONST.__objc_dictobj: 0xaf0
-  __AUTH_CONST.__objc_arrayobj: 0x810
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__objc_dictobj: 0xac8
+  __AUTH_CONST.__objc_arrayobj: 0x900
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0xa24
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x150
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 265
-  Symbols:   486
-  CStrings:  1604
+  Functions: 330
+  Symbols:   565
+  CStrings:  1568
 
Symbols:
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _qos_class_self
- _NfRestoreOpenWithSE
- _NfRestoreSEClose
- _NfRestoreSEList
- _NfRestoreSETransceive
- __DefaultRuneLocale
- ___maskrune
- _objc_retainBlock
- _objc_retain_x25
CStrings:
+ "Query key: \"%@\" within %@ms"
+ "Query key: \"%@\" without time limitation"
+ "Unsupported AID mogul type"
+ "com.apple.private.MobileGestalt.AllowedProtectedKeys"
+ "logCallbackForSyslogCDPWithLevelBuffer"
+ "logCallbackForSyslogWithContextLevelFormat"
+ "logCallbackForSyslogWithLevelBuffer"
+ "mZfUC7qo4pURNhyMHZ62RQ"
+ "tRn/qRwm394es24o13orf0CTTM60oo8/DS2Dx26ehaqHw"
- "\nSE command %s output:"
- "\nSending command %s to SE:"
- "   "
- "%.2X "
- "%.8zx: "
- "%c"
- "+[AppleDeviceQueryKeysActionArmory querySecureElementIDWithError:]"
- "+[AppleDeviceQueryKeysActionArmory querySecureElementIDWithError:]_block_invoke"
- "ACTION_LEGACY"
- "After invoking sharedHardwareManager() from NearField Framework"
- "AppleStockholmControlUserClient"
- "Before invoking sharedHardwareManager() from NearField Framework"
- "Copy seid (seID=%d) failed."
- "Failed to query Secure Element ID!"
- "Failed to weak link libnfrestore.dylib for SE (seID=%d), NfRestoreOpenWithSE isn't available"
- "Failed to weak link libnfrestore.dylib for command '%s', NfRestoreSETransceive isn't available"
- "Failed to weak link libnfrestore.dylib, NfRestoreSEList isn't available!"
- "Get SEID"
- "NfRestoreSETranceive() returned %d for command '%s'"
- "No SE command input"
- "No SE command name input"
- "No bytes input"
- "SEID = %@"
- "Select CASD"
- "Skipping this SE (seID=%d)"
- "Unable to connect to SE (seID=%d)"
- "Unable to convert SEID"
- "Unable to copy SEID"
- "Unable to select CASD"
- "command %s may have overflowed output buffer with %zu bytes"
- "command %s returned no data"
- "command %s returned no data payload"
- "command %s returned no status"
- "context is NULL"
- "copySeid"
- "fdrDiagnosticLogCallback"
- "fdrLogCallback"
- "hexDump"
- "listCopySeid"
- "nfSECopyCommandResponse"
- "querySecureElementIDWithError:"
- "seList is NULL"
- "seLogger"
- "status word for command %s may indicate failure: 0x%x"

```
