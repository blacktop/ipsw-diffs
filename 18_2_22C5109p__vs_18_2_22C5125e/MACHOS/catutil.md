## catutil

> `/System/Library/PrivateFrameworks/DialogEngine.framework/catutil`

```diff

-3402.29.1.0.0
-  __TEXT.__text: 0x60078
-  __TEXT.__auth_stubs: 0x1670
+3402.34.1.0.0
+  __TEXT.__text: 0x606cc
+  __TEXT.__auth_stubs: 0x1680
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x1dd8
-  __TEXT.__gcc_except_tab: 0x7490
-  __TEXT.__cstring: 0xcd0b
+  __TEXT.__gcc_except_tab: 0x7500
+  __TEXT.__cstring: 0xceb1
   __TEXT.__objc_methname: 0xab
-  __TEXT.__unwind_info: 0x1a40
-  __DATA_CONST.__auth_got: 0xb48
+  __TEXT.__unwind_info: 0x1a60
+  __DATA_CONST.__auth_got: 0xb50
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x9a8

   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1059
-  Symbols:   417
-  CStrings:  998
+  Functions: 1063
+  Symbols:   418
+  CStrings:  1007
 
Symbols:
+ __ZNK4siri12dialogengine4File17GetValidationNitsEv
CStrings:
+ "\n  <EXECUTABLE> <COMMAND> --templateDir <dir> [--schema <type>] [--catId <id>] [--locale <locale>] [--visualCatId <id>]\n          [--noCheckSnippetDialogIds] [--sourceLocaleDialogIds <ids>] [--xcode] [--quiet] [--errors] [--pedantic]\n\n      If --catId or --visualCatId is specified, then validate the specified CAT file.\n      If --locale is also defined then only check that locale, otherwise check all locales.\n\n      If --schema is specified, then validate the specified type name.\n\n      If none of --catId, --visualCatId, or --schema is specified, then find and validate\n      all schema files and all CAT files under the template directory. If --locale is also defined\n      then only check that locale for each CAT file, otherwise check all locales for all CAT files.\n\n      If --noCheckSnippetDialogIds is specified, do not check for matching dialog IDs in \"UsedForSnippet\" CATs.\n\n      If --sourceLocaleDialogIds is specified, <ids> is expected to be a comma-separated set of dialog IDs to\n      use instead of reading from the source locale file.\n\n      If --xcode is specified, output is generated in a format that can be used with Xcode's\n      Build Phases > Run Script functionality to highlight errors/warnings within Xcode's UI.\n      As expected by Xcode, the exit code is 1 if there are errors, but 0 if there are only warnings.\n\n      If --quiet is specified, no output is generated. The exit code indicates success or failure.\n\n      If --errors is specified, no warnings are generated or contribute to the exit code (disables pedantic mode).\n\n      If --pedantic is specified, additional checks are performed for opportunities for improvement (\"nits\").\n"
+ " validation nit(s) for "
+ "--pedantic"
+ "3402.34.1"
+ "CAT file command line utility. Version 3402.34.1.\n"
+ "CatUtilMain() exiting with result: %!s(MISSING)"
+ "ValidationContext::SetCheckSnippetDialogIds(%!s(MISSING))"
+ "ValidationContext::SetErrorsMode(%!s(MISSING))"
+ "ValidationContext::SetPedanticMode(%!s(MISSING))"
+ "ValidationContext::SetQuietMode(%!s(MISSING))"
+ "ValidationContext::SetXcodeMode(%!s(MISSING))"
+ "nit"
- "\n  <EXECUTABLE> <COMMAND> --templateDir <dir> [--schema <type>] [--catId <id>] [--locale <locale>] [--visualCatId <id>]\n          [--noCheckSnippetDialogIds] [--sourceLocaleDialogIds <ids>] [--xcode] [--quiet] [--errors]\n\n      If --catId or --visualCatId is specified, then validate the specified CAT file.\n      If --locale is also defined then only check that locale, otherwise check all locales.\n\n      If --schema is specified, then validate the specified type name.\n\n      If none of --catId, --visualCatId, or --schema is specified, then find and validate\n      all schema files and all CAT files under the template directory. If --locale is also defined\n      then only check that locale for each CAT file, otherwise check all locales for all CAT files.\n\n      If --noCheckSnippetDialogIds is specified, do not check for matching dialog IDs in \"UsedForSnippet\" CATs.\n\n      If --sourceLocaleDialogIds is specified, <ids> is expected to be a comma-separated set of dialog IDs to\n      use instead of reading from the source locale file.\n\n      If --xcode is specified, output is generated in a format that can be used with Xcode's\n      Build Phases > Run Script functionality to highlight errors/warnings within Xcode's UI.\n      As expected by Xcode, the exit code is 1 if there are errors, but 0 if there are only warnings.\n\n      If --quiet is specified, no output is generated. The exit code indicates success or failure.\n\n      If --errors is specified, no warnings are generated or contribute to the exit code.\n"
- "3402.29.1"
- "CAT file command line utility. Version 3402.29.1.\n"

```
