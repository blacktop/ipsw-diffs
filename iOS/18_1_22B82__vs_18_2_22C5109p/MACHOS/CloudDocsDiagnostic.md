## CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```diff

-3097.40.5.0.0
-  __TEXT.__text: 0xfc0
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x3a0
+3097.60.140.0.0
+  __TEXT.__text: 0x1420
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0x224
-  __TEXT.__objc_methname: 0x309
-  __TEXT.__oslogstring: 0x127
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__cstring: 0x31f
+  __TEXT.__oslogstring: 0x203
   __TEXT.__objc_classname: 0x1d
-  __TEXT.__objc_methtype: 0x39
+  __TEXT.__objc_methname: 0x337
+  __TEXT.__objc_methtype: 0x3e
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x100
-  __DATA.__objc_ivar: 0x4
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 13
-  Symbols:   77
-  CStrings:  65
+  Functions: 19
+  Symbols:   85
+  CStrings:  77
 
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSNumber
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _objc_opt_class
+ _objc_opt_isKindOfClass
- _objc_msgSendSuper2
CStrings:
+ "-[CloudDocsDiagnosticExtension _enableLogSensitiveData:]"
+ "-[CloudDocsDiagnosticExtension _getConfigureLogsParam:configureLogs:]"
+ "-[CloudDocsDiagnosticExtension attachmentsForParameters:]"
+ "B32@0:8@16^B24"
+ "NO"
+ "YES"
+ "[DEBUG] Enable com.apple.fileprovider.log-sensitive-data [%!s(MISSING)]%!@(MISSING)"
+ "[DEBUG] Only setup parameters at this step. Return 0 attachments%!@(MISSING)"
+ "[DEBUG] Parameter missing or invalid: %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] Running attachmentsForParameters %!@(MISSING)%!@(MISSING)"
+ "_enableLogSensitiveData:"
+ "_getConfigureLogsParam:configureLogs:"
+ "boolValue"
+ "com.apple.fileprovider.log-sensitive-data"
+ "configure-logs"
+ "i"
+ "objectForKey:"
+ "v20@0:8B16"
- "@16@0:8"
- "B"
- "_isTimberLorry"
- "init"
- "setupWithParameters:"
- "v24@0:8@16"

```
