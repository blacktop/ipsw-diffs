## spindump

> `/usr/sbin/spindump`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-443.0.0.0.0
-  __TEXT.__text: 0x10dbbc
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_stubs: 0x4b80
-  __TEXT.__objc_methlist: 0xcd0
-  __TEXT.__const: 0x2d8
-  __TEXT.__oslogstring: 0x355c0
-  __TEXT.__cstring: 0x1bace
+445.0.0.0.0
+  __TEXT.__text: 0x10ee70
+  __TEXT.__auth_stubs: 0x1580
+  __TEXT.__objc_stubs: 0x4bc0
+  __TEXT.__objc_methlist: 0xce0
+  __TEXT.__const: 0x2e0
+  __TEXT.__oslogstring: 0x356f6
+  __TEXT.__cstring: 0x1bbf3
   __TEXT.__objc_classname: 0x143
   __TEXT.__objc_methtype: 0x596
-  __TEXT.__gcc_except_tab: 0x461c
-  __TEXT.__objc_methname: 0x49c5
-  __TEXT.__unwind_info: 0x1410
-  __DATA_CONST.__const: 0x2130
-  __DATA_CONST.__cfstring: 0xdac0
+  __TEXT.__gcc_except_tab: 0x47cc
+  __TEXT.__objc_methname: 0x4a11
+  __TEXT.__unwind_info: 0x1460
+  __DATA_CONST.__const: 0x2190
+  __DATA_CONST.__cfstring: 0xdb80
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0xab0
+  __DATA_CONST.__auth_got: 0xad0
   __DATA_CONST.__got: 0x348
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA.__objc_const: 0x2560
-  __DATA.__objc_selrefs: 0x13a8
-  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_const: 0x2580
+  __DATA.__objc_selrefs: 0x13b8
+  __DATA.__objc_ivar: 0x288
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x1c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x928
+  __DATA.__bss: 0x930
   __DATA.__common: 0x70
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2758
-  Symbols:   454
-  CStrings:  5182
+  Functions: 2773
+  Symbols:   458
+  CStrings:  5195
 
Symbols:
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_terminate
CStrings:
+ " exclave %-*s"
+ "%-*s"
+ "%@%lu"
+ "%@:%@"
+ "Heaviest stack"
+ "Parsing spindump text: Unable to filter heaviest callstack to specific index range, it remains unfiltered"
+ "SaveReportSerialized"
+ "Unable to format: Parsing spindump text: Unable to filter heaviest callstack to specific index range, it remains unfiltered"
+ "Unable to format: Waited %.1f to get report lock"
+ "Waited %.1f to get report lock"
+ "^(?<indentWhitespace> +(?<kernelDot>\\*)?)(?<countAndWhitespace>(?<count>\\d+)\\s+)(?:\\?\\?\\?(?:\\s+\\+\\s+(?<offsetIntoUnknownSymbol>\\d+))?|(?<symbolName>.*?)\\s+\\+\\s+(?<offsetIntoSymbol>\\d+))(?:\\s+\\((?:(?:(?<sourceFilepath>.+?)(?::(?<sourceLineNumber>\\d+)(?:[:\\.,](?<sourceColumnNumber>\\d+))?)?\\s+in\\s+)?(?:<(?<binaryUuid>[\\dabcdef\\-]{32,36})>|(?<binaryName>.+?))\\s+\\+\\s+(?<offsetIntoBinary>\\d+))?(?:\\s*(?<exclaveInfo>exclave\\s+.+?))?\\))?(?:\\s+\\[(?<address>(?:0x)?[\\dabcdef]+)\\])?(?:\\s+\\((?<stateInfo>.+?)\\))?(?:\\s+(?<startIndex>\\d+)(?:\\s*-\\s*(?<endIndex>\\d+))?)?$"
+ "^\\s*(?<kernelDot>\\*)?(?:(?<startAddress>(?:0x)?[\\dabcdef]+)|\\?\\?\\?)\\s*\\-\\s*(?:(?<endAddress>(?:0x)?[\\dabcdef]+)|\\?\\?\\?)\\s*(?:\\?\\?\\?|(?<bundleIdentifier>\\S+\\.\\S+\\.\\S+)|(?<name>.+?\\b))\\s+(?<version>(?:.*?)?(?:\\s*\\(.*?\\)))?\\s*(?:exclave\\s+(?<exclaveName>.+?)\\s+)?\\s*<(?<binaryUuid>[\\dabcdef\\-]{32,36})>(?<segmentName>\\S+?)?(?:\\s+(?<binaryPath>.+?)?)?$"
+ "_exclaveName"
+ "_serializeReportToStream:withSampleStore:"
+ "exclaveInfo"
+ "exclaveName"
+ "unsignedIntegerValue"
- "%@-%@"
- "SaveReport"
- "^(?<indentWhitespace> +(?<kernelDot>\\*)?)(?<countAndWhitespace>(?<count>\\d+)\\s+)(?:\\?\\?\\?(?:\\s+\\+\\s+(?<offsetIntoUnknownSymbol>\\d+))?|(?<symbolName>.*?)\\s+\\+\\s+(?<offsetIntoSymbol>\\d+))(?:\\s+\\((?:(?<sourceFilepath>.+?)(?::(?<sourceLineNumber>\\d+)(?:[:\\.,](?<sourceColumnNumber>\\d+))?)?\\s+in\\s+)?(?:<(?<binaryUuid>[\\dabcdef\\-]{32,36})>|(?<binaryName>.+?))\\s+\\+\\s+(?<offsetIntoBinary>\\d+)\\))?(?:\\s+\\[(?<address>(?:0x)?[\\dabcdef]+)\\])?(?:\\s+\\((?<stateInfo>.+?)\\))?(?:\\s+(?<startIndex>\\d+)(?:\\s*-\\s*(?<endIndex>\\d+))?)?$"
- "^\\s*(?<kernelDot>\\*)?(?:(?<startAddress>(?:0x)?[\\dabcdef]+)|\\?\\?\\?)\\s*\\-\\s*(?:(?<endAddress>(?:0x)?[\\dabcdef]+)|\\?\\?\\?)\\s*(?:\\?\\?\\?|(?<bundleIdentifier>\\S+\\.\\S+\\.\\S+)|(?<name>.+?\\b))\\s+(?<version>(?:.*?)?(?:\\s*\\(.*?\\)))?\\s*<(?<binaryUuid>[\\dabcdef\\-]{32,36})>(?<segmentName>\\S+?)?(?:\\s+(?<binaryPath>.+?)?)?$"
```
