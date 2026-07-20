## spindump_fileparser

> `/usr/libexec/spindump_fileparser`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-443.0.0.0.0
-  __TEXT.__text: 0xc20c8
-  __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_stubs: 0x4440
-  __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x280
-  __TEXT.__cstring: 0x15ed3
-  __TEXT.__oslogstring: 0x28949
-  __TEXT.__gcc_except_tab: 0x31b4
+445.0.0.0.0
+  __TEXT.__text: 0xc312c
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_stubs: 0x4480
+  __TEXT.__objc_methlist: 0xa04
+  __TEXT.__const: 0x288
+  __TEXT.__cstring: 0x15ff8
+  __TEXT.__oslogstring: 0x28a7f
+  __TEXT.__gcc_except_tab: 0x3364
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x437e
+  __TEXT.__objc_methname: 0x43ca
   __TEXT.__objc_methtype: 0x530
-  __TEXT.__unwind_info: 0xce8
-  __DATA_CONST.__const: 0x1590
-  __DATA_CONST.__cfstring: 0xa380
+  __TEXT.__unwind_info: 0xd20
+  __DATA_CONST.__const: 0x15e0
+  __DATA_CONST.__cfstring: 0xa440
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x9e8
+  __DATA_CONST.__auth_got: 0xa18
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x1228
-  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_const: 0x1d88
+  __DATA.__objc_selrefs: 0x1238
+  __DATA.__objc_ivar: 0x218
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x818
+  __DATA.__bss: 0x820
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1831
-  Symbols:   394
-  CStrings:  3981
+  Functions: 1845
+  Symbols:   400
+  CStrings:  3994
 
Symbols:
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_terminate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
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
