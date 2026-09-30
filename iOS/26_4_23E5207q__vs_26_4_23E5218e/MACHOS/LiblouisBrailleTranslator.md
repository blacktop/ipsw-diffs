## LiblouisBrailleTranslator

> `/System/Library/ScreenReader/BrailleTables/LiblouisBrailleTranslator.brailletable/LiblouisBrailleTranslator`

```diff

-63.0.0.0.0
-  __TEXT.__text: 0x1c0a4
-  __TEXT.__auth_stubs: 0x4b0
+64.0.0.0.0
+  __TEXT.__text: 0x1e5e4
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0x33c
   __TEXT.__const: 0x358
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x2087
+  __TEXT.__cstring: 0x230c
   __TEXT.__objc_methname: 0x8d0
   __TEXT.__objc_classname: 0x98
   __TEXT.__objc_methtype: 0x2c7
   __TEXT.__oslogstring: 0x182
-  __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__auth_ptr: 0x18
+  __TEXT.__unwind_info: 0x350
+  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x548
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x18

   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x2c0
-  __DATA.__bss: 0x6664
+  __DATA.__bss: 0x7682
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9AF84E64-0448-34FC-AD3D-69D34DBC405E
-  Functions: 226
-  Symbols:   166
-  CStrings:  544
+  UUID: 51B73B79-1489-3E2F-A6BF-6CE5AF0A22C2
+  Functions: 254
+  Symbols:   183
+  CStrings:  566
 
Symbols:
+ ___strncat_chk
+ ___tolower
+ __lou_freeTableIndex
+ _closedir
+ _lou_findTable
+ _lou_findTables
+ _lou_freeEmphClasses
+ _lou_freeTableFile
+ _lou_freeTableFiles
+ _lou_freeTableInfo
+ _lou_getTableInfo
+ _lou_indexTables
+ _lou_listTables
+ _opendir
+ _readdir
+ _strcat
+ _strncasecmp
CStrings:
+ "%d matches found"
+ "%s is not a directory"
+ "3.36.0"
+ "Analyzing table %s"
+ "Attempt to free string buffer prior to initialization of pool"
+ "Best match: %s (%d)"
+ "LOUIS_LOGLEVEL"
+ "No table could be found for query '%s'"
+ "No tables were indexed"
+ "Not a valid language tag: %s"
+ "Not a valid language tag: %s (line %d)"
+ "Query has feature '%s:%s'"
+ "Table '%s' resolves to more than one file"
+ "Table has feature '%s:%s'"
+ "Tables have not been indexed yet. Indexing LOUIS_TABLEPATH."
+ "Unexpected character '%c' at position %d"
+ "Unexpected character '%c' on line %d, column %d"
+ "Unexpected newline on line %d"
+ "Unknown log level set by LOUIS_LOGLEVEL environment variable: %s"
+ "language"
+ "region"
+ "ucs%ld"
+ "ucs2"
+ "ucs4"
+ "unicode-range"
- "%s\n"
- "3.34.0"
- "String too long: %zu"

```
