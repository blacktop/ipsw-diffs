## catutil

> `/System/Library/PrivateFrameworks/DialogEngine.framework/catutil`

```diff

-3500.26.1.0.0
-  __TEXT.__text: 0x5fb98
-  __TEXT.__auth_stubs: 0x1690
+3500.33.1.0.0
+  __TEXT.__text: 0x5f870
+  __TEXT.__auth_stubs: 0x16c0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x1e9c
-  __TEXT.__gcc_except_tab: 0x73d4
-  __TEXT.__cstring: 0xcf7e
+  __TEXT.__gcc_except_tab: 0x7360
+  __TEXT.__cstring: 0xd0ad
   __TEXT.__objc_methname: 0xab
   __TEXT.__unwind_info: 0x1a08
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0xb58
+  __DATA_CONST.__auth_got: 0xb70
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0xa08
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x578
-  __DATA.__bss: 0x220
+  __DATA.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine

   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 369A8379-9C21-399B-ACE1-7B2E56BCC393
-  Functions: 1031
-  Symbols:   421
-  CStrings:  1004
+  UUID: 790EA2C4-FE91-3AAE-9B67-BF3BA1A25C46
+  Functions: 1029
+  Symbols:   424
+  CStrings:  1008
 
Symbols:
+ __ZNK4siri12dialogengine15SpeakableString16SpeakEqualsPrintEv
+ __ZNK4siri12dialogengine4Text8GetValueEv
+ __ZNK4siri12dialogengine6Dialog13GetSupportingEv
CStrings:
+ "\n  <EXECUTABLE> <COMMAND> write --templateDir <dir> {--metadataDir|--assistantDir|--sourceDir} <dir>\n          [--category <name>] [--verbose] [--ignoreIncludes] [--locale <locale1> <locale2> ...] [--allLocales]\n\n      Read the Templates/metadata/dialog-metadata.yaml file to define the categories and locales\n      to convert. If --category is specified, exclude all other configured categories except the\n      one specified. Then read [d] tag metadata from VOC files in the dialog-metadata or assistant\n      repository and generate a CAT dialog metadata file for every locale. You can specify if you\n      want the VOC parser to follow include directives or not. You can override the list of locales\n      in the YAML file with the --locale or --allLocales arguments.\n\n      Exactly one of the options --metadataDir, --assistantDir or --sourceDir is required to specify the source of the\n      VOC files you wish to convert. --metadataDir and --assistantDir require the presence of a \"dialog-metadata.yaml\"\n      file in the Templates dir, whereas --sourceDir does not. The latter consumes all available categories present\n      in the specified source directory.\n\n      --assistantDir <dir>  The path to a copy of the “assistant” Git repository (Deprecated; Prefer --metadataDir)\n      --metadataDir <dir>   The path to a copy of the “dialog-metadata” Git repository\n      --sourceDir <dir>     The path to a directory containing .voc files (See the \"metadata copy\" command)\n\n  <EXECUTABLE> <COMMAND> read --templateDir <dir> --category <name> --locale <locale>\n  <EXECUTABLE> <COMMAND> read --filename <filename>\n\n      Read a dialog metadata file and output its contents to the shell. You can either specify\n      the file through a combination of a template dir, category name (e.g. personRelationship),\n      and a locale; or you can provide the full path to the file with the --filename option.\n\n  <EXECUTABLE> <COMMAND> copy --templateDir <dir> --category <name> --outputDir <dir>\n\n      Copy all of the dialog metadata in a CAT .dtag directory into another directory and output\n      the data in VOC format. This lets you easily view all of the metadata for all locales for a\n      given category, and also lets you set up a local version of the data that's independent of\n      the assistant repo.\n\n  <EXECUTABLE> <COMMAND> codegen --templateDir <dir> --outputDir <dir> [--category <name>]\n          [--config <path>] [--swiftCaseStyle none|lower|upper] [--debug]\n\n      Read dialog metadata files and generate Swift enum definitions from their contents.\n\n      --category <name>         Process the specified category (or all categories if omitted)\n      --config <path>           Path to a YAML file for configuring output\n      --debug                   Output debug log messages\n      --outputDir <dir>         Path to the folder in which to write generated source code files\n      --swiftCaseStyle <style>  Choose the formatting of Swift enum case statements\n                                  \"none\": Unmodified (default)\n                                  \"lower\": All lower case\n                                  \"upper\": All upper case\n      --templateDir <dir>       Path to the template directory\n"
+ "3500.33.1"
+ "; "
+ "CAT file command line utility. Version 3500.33.1.\n"
+ "Multiple source dirs specified. Use only one of the following: --metadataDir / --assistantDir / --sourceDir"
+ "No source dir specified. One of the following is required: --metadataDir / --assistantDir / --sourceDir"
+ "conditions"
+ "dialog IDs"
+ "dialogs"
+ "dialogs with print != speak"
+ "expansion lines"
+ "expansion time (seconds)"
+ "file path"
+ "phrases"
+ "semantic concepts"
+ "texts"
+ "texts with print != speak"
+ "xml lines"
- "\n  <EXECUTABLE> <COMMAND> write --templateDir <dir> [--metadataDir <dir>] [--assistantDir <dir>] [--sourceDir <dir>]\n          [--category <name>] [--verbose] [--ignoreIncludes] [--locale <locale1> <locale2> ...] [--allLocales]\n\n      Read the Templates/metadata/dialog-metadata.yaml file to define the categories and locales\n      to convert. If --category is specified, exclude all other configured categories except the\n      one specified. Then read [d] tag metadata from VOC files in the dialog-metadata or assistant\n      repository and generate a CAT dialog metadata file for every locale. You can specify if you\n      want the VOC parser to follow include directives or not. You can override the list of locales\n      in the YAML file with the --locale or --allLocales arguments.\n\n      Note: All of the options --metadataDir, --assistantDir and --sourceDir will allow you to specify the source of the\n      VOC files you wish to convert, but --metdataDir and --assistantDir require the presence of a \"dialog-metadata.yaml\"\n      file in the Templates dir, whereas --sourceDir does not. The latter will consume all available categories present\n      in the specified source directory.\n\n  <EXECUTABLE> <COMMAND> read --templateDir <dir> --category <name> --locale <locale>\n  <EXECUTABLE> <COMMAND> read --filename <filename>\n\n      Read a dialog metadata file and output its contents to the shell. You can either specify\n      the file through a combination of a template dir, category name (e.g. personRelationship),\n      and a locale; or you can provide the full path to the file with the --filename option.\n\n  <EXECUTABLE> <COMMAND> copy --templateDir <dir> --category <name> --outputDir <dir>\n\n      Copy all of the dialog metadata in a CAT .dtag directory into another directory and output\n      the data in VOC format. This lets you easily view all of the metadata for all locales for a\n      given category, and also lets you set up a local version of the data that's independent of\n      the assistant repo.\n\n  <EXECUTABLE> <COMMAND> codegen --templateDir <dir> --outputDir <dir> [--category <name>]\n          [--config <path>] [--swiftCaseStyle none|lower|upper] [--debug]\n\n      Read dialog metadata files and generate Swift enum definitions from their contents.\n\n      --category <name>         Process the specified category (or all categories if omitted)\n      --config <path>           Path to a YAML file for configuring output\n      --debug                   Output debug log messages\n      --outputDir <dir>         Path to the folder in which to write generated source code files\n      --swiftCaseStyle <style>  Choose the formatting of Swift enum case statements\n                                  \"none\": Unmodified (default)\n                                  \"lower\": All lower case\n                                  \"upper\": All upper case\n      --templateDir <dir>       Path to the template directory\n"
- "  Expansion took "
- " seconds for '"
- "' locale"
- "3500.26.1"
- "CAT file command line utility. Version 3500.26.1.\n"
- "No source dir specified: --sourceDir or --metadataDir or --assistantDir"
- "Weather#dailyForecast"
- "catId, locale, xml lines, dialogs, texts, phrases, conditions, parameters, semantic concepts, expansion lines, expansion time (seconds), file path, dialog IDs"
- "catci/dialogenginetemplates"
- "dateTime#timeShortTwentyFourHourDisplay"
- "example#"
- "it"
- "phrases#"

```
