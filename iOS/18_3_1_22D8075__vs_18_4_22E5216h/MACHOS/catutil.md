## catutil

> `/System/Library/PrivateFrameworks/DialogEngine.framework/catutil`

```diff

-3402.35.1.0.0
-  __TEXT.__text: 0x606cc
-  __TEXT.__auth_stubs: 0x1680
+3404.15.1.0.0
+  __TEXT.__text: 0x5ed28
+  __TEXT.__auth_stubs: 0x16b0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x1dd8
-  __TEXT.__gcc_except_tab: 0x7500
-  __TEXT.__cstring: 0xceb1
+  __TEXT.__const: 0x1e9c
+  __TEXT.__gcc_except_tab: 0x747c
+  __TEXT.__cstring: 0xcf7e
   __TEXT.__objc_methname: 0xab
-  __TEXT.__unwind_info: 0x1a60
-  __DATA_CONST.__auth_got: 0xb50
-  __DATA_CONST.__got: 0x160
+  __TEXT.__unwind_info: 0x1948
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__auth_got: 0xb68
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__const: 0xa08
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x578

   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1063
-  Symbols:   418
-  CStrings:  1007
+  Functions: 997
+  Symbols:   422
+  CStrings:  1008
 
Symbols:
+ __ZN4siri12dialogengine11RequestInfo9AddOptionEi
+ __ZN4siri12dialogengine16ExceptionDetailsERKN4YAML9ExceptionERKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE
+ __ZN4siri12dialogengine19ShouldValidateAttrsEv
+ __ZN4siri12dialogengine21OPTION_VALIDATE_ATTRSE
CStrings:
+ "\n  <EXECUTABLE> <COMMAND> --templateDir <dir> [--schema <type>] [--catId <id>] [--locale <locale>] [--visualCatId <id>]\n          [--attrs] [--noCheckSnippetDialogIds] [--sourceLocaleDialogIds <ids>] [--xcode] [--quiet] [--errors] [--pedantic]\n\n      If --catId or --visualCatId is specified, then validate the specified CAT file.\n      If --locale is also defined then only check that locale, otherwise check all locales.\n\n      If --schema is specified, then validate the specified type name.\n\n      If none of --catId, --visualCatId, or --schema is specified, then find and validate\n      all schema files and all CAT files under the template directory. If --locale is also defined\n      then only check that locale for each CAT file, otherwise check all locales for all CAT files.\n\n      If --attrs is specified, check whether XML element attributes in a CAT are valid for the CAT version.\n\n      If --noCheckSnippetDialogIds is specified, do not check for matching dialog IDs in \"UsedForSnippet\" CATs.\n\n      If --sourceLocaleDialogIds is specified, <ids> is expected to be a comma-separated set of dialog IDs to\n      use instead of reading from the source locale file.\n\n      If --xcode is specified, output is generated in a format that can be used with Xcode's\n      Build Phases > Run Script functionality to highlight errors/warnings within Xcode's UI.\n      As expected by Xcode, the exit code is 1 if there are errors, but 0 if there are only warnings.\n\n      If --quiet is specified, no output is generated. The exit code indicates success or failure.\n\n      If --errors is specified, no warnings are generated or contribute to the exit code (disables pedantic mode).\n\n      If --pedantic is specified, additional checks are performed for opportunities for improvement (\"nits\").\n      (This also activates the --attrs option.)\n"
+ "--attrs"
+ "3404.15.1"
+ "5.4"
+ "CAT file command line utility. Version 3404.15.1.\n"
+ "Could not parse YAML file: "
+ "Unable to parse YAML file: "
+ "ValidationContext::SetAttrsMode(%s)"
+ "yaml-cpp exception in YAML file: "
- "\n  <EXECUTABLE> <COMMAND> --templateDir <dir> [--schema <type>] [--catId <id>] [--locale <locale>] [--visualCatId <id>]\n          [--noCheckSnippetDialogIds] [--sourceLocaleDialogIds <ids>] [--xcode] [--quiet] [--errors] [--pedantic]\n\n      If --catId or --visualCatId is specified, then validate the specified CAT file.\n      If --locale is also defined then only check that locale, otherwise check all locales.\n\n      If --schema is specified, then validate the specified type name.\n\n      If none of --catId, --visualCatId, or --schema is specified, then find and validate\n      all schema files and all CAT files under the template directory. If --locale is also defined\n      then only check that locale for each CAT file, otherwise check all locales for all CAT files.\n\n      If --noCheckSnippetDialogIds is specified, do not check for matching dialog IDs in \"UsedForSnippet\" CATs.\n\n      If --sourceLocaleDialogIds is specified, <ids> is expected to be a comma-separated set of dialog IDs to\n      use instead of reading from the source locale file.\n\n      If --xcode is specified, output is generated in a format that can be used with Xcode's\n      Build Phases > Run Script functionality to highlight errors/warnings within Xcode's UI.\n      As expected by Xcode, the exit code is 1 if there are errors, but 0 if there are only warnings.\n\n      If --quiet is specified, no output is generated. The exit code indicates success or failure.\n\n      If --errors is specified, no warnings are generated or contribute to the exit code (disables pedantic mode).\n\n      If --pedantic is specified, additional checks are performed for opportunities for improvement (\"nits\").\n"
- "\nError: "
- "3402.35.1"
- "5.2"
- "CAT file command line utility. Version 3402.35.1.\n"
- "Could not parse YAML file "
- "Unable to parse YAML file:"
- "yaml-cpp exception in YAML file:"

```
