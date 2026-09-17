## OSInstaller

> `/System/Library/PrivateFrameworks/OSInstaller.framework/Versions/A/OSInstaller`

```diff

-1639.0.1.0.0
-  __TEXT.__text: 0x59680
+1642.40.1.0.0
+  __TEXT.__text: 0x598bc
   __TEXT.__objc_methlist: 0x3694
-  __TEXT.__cstring: 0x10356
+  __TEXT.__cstring: 0x10346
   __TEXT.__gcc_except_tab: 0x2308
-  __TEXT.__ustring: 0x34
+  __TEXT.__ustring: 0x296
   __TEXT.__const: 0x178
   __TEXT.__oslogstring: 0xe2a
   __TEXT.__unwind_info: 0x1070

   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b00
+  __DATA_CONST.__objc_selrefs: 0x2b08
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x160
   __DATA_CONST.__got: 0x790
   __AUTH_CONST.__const: 0xa50
-  __AUTH_CONST.__cfstring: 0x6620
+  __AUTH_CONST.__cfstring: 0x6700
   __AUTH_CONST.__objc_const: 0x5588
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
   Functions: 1419
-  Symbols:   3791
-  CStrings:  1835
+  Symbols:   3792
+  CStrings:  1842
 
Symbols:
+ _objc_msgSend$pathWithComponents:
Functions:
~ -[OSITemplateMigrationOptions findPrebootAndLoadCookie] : 2036 -> 2216
~ -[OSITemplateMigrationController persistDiagnostics] : 696 -> 984
~ -[OSITemplateMigrationController quitOrReboot] : 2292 -> 2396
CStrings:
+ "/Applications/Install macOS 27 Golden Gate Beta.app"
+ "DiagnosticReports"
+ "Library/Logs/DiagnosticReports"
+ "Logs"
+ "MigrationMode"
+ "Template Migration: Cookie deleted successfully — boot loop broken"
+ "Template Migration: Cookie deletion FAILED at %@: %@ — THIS MAY CAUSE A REBOOT LOOP"
+ "Template Migration: Cookie read FAILED — file missing or malformed at %@. Proceeding with defaults."
+ "Template Migration: Cookie read OK — mode=%@, keys=%@"
+ "TemplateMigration (implicit)"
- "/Applications/Install macOS 27 Golden Gate.app"
- "Template Migration: Failed to remove cookie file: %@"
- "Template Migration: Loaded settings from Preboot cookie file: %@"
```
