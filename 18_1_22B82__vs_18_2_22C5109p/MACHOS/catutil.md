## catutil

> `/System/Library/PrivateFrameworks/DialogEngine.framework/catutil`

```diff

-3401.5.1.0.0
-  __TEXT.__text: 0x5f980
-  __TEXT.__auth_stubs: 0x1660
+3402.29.1.0.0
+  __TEXT.__text: 0x60078
+  __TEXT.__auth_stubs: 0x1670
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x1dd8
-  __TEXT.__gcc_except_tab: 0x740c
-  __TEXT.__cstring: 0xcc0f
+  __TEXT.__gcc_except_tab: 0x7490
+  __TEXT.__cstring: 0xcd0b
   __TEXT.__objc_methname: 0xab
-  __TEXT.__unwind_info: 0x1a18
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x158
+  __TEXT.__unwind_info: 0x1a40
+  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x9a8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1055
-  Symbols:   415
-  CStrings:  997
+  Functions: 1059
+  Symbols:   417
+  CStrings:  998
 
Symbols:
+ __ZNK4siri12dialogengine23CollectDialogIdsVisitor12GetDialogIdsEv
+ __ZTVN4siri12dialogengine23CollectDialogIdsVisitorE
CStrings:
+ "\n  <EXECUTABLE> <COMMAND> --templateDir <dir> [--catId <id>] [--locale <locale>] [--dialogIDsOnly]\n\n      If --templateDir and --catId are specified, then report metrics for the specified CAT file.\n      If --locale is also specified then report metrics for only that locale, otherwise report for all locales.\n\n      If --templateDir is specified and --catId is not, then find and report metrics for all CAT files\n      under the directory and any template directories nested within it.  If --locale is specified, then\n      only generate metrics for that locale of each CAT file, otherwise report metrics for all locales for\n      all CAT files.\n\n      If the --dialogIDsOnly option is present, this will produce a JSON that contains only the dialog IDs\n      present in each CAT file for the purpose of comparison and identification of mismatches.\n\n"
+ "--dialogIDsOnly"
+ "3402.29.1"
+ "5.2"
+ "CAT file command line utility. Version 3402.29.1.\n"
+ "catId, locale, xml lines, dialogs, texts, phrases, conditions, parameters, semantic concepts, expansion lines, expansion time (seconds), file path, dialog IDs"
- "\n  <EXECUTABLE> <COMMAND> --templateDir <dir> [--catId <id>] [--locale <locale>]\n\n      If --templateDir and --catId are specified, then report metrics for the specified CAT file.\n      If --locale is also specified then report metrics for only that locale, otherwise report for all locales.\n\n      If --templateDir is specified and --catId is not, then find and report metrics for all CAT files\n      under the directory and any template directories nested within it.  If --locale is specified, then\n      only generate metrics for that locale of each CAT file, otherwise report metrics for all locales for\n      all CAT files.\n"
- "3401.5.1"
- "5.1"
- "CAT file command line utility. Version 3401.5.1.\n"
- "catId, locale, xml lines, dialogs, texts, phrases, conditions, parameters, semantic concepts, expansion lines, expansion time (seconds), file path"

```
