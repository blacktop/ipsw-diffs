## spindump

> `/usr/sbin/spindump`

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
-  __TEXT.__text: 0xb8e10
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x41a0
-  __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x1532b
-  __TEXT.__oslogstring: 0x26ded
-  __TEXT.__gcc_except_tab: 0x3094
+445.0.0.0.0
+  __TEXT.__text: 0xb9eb4
+  __TEXT.__auth_stubs: 0x13d0
+  __TEXT.__objc_stubs: 0x41e0
+  __TEXT.__objc_methlist: 0xa04
+  __TEXT.__const: 0x278
+  __TEXT.__cstring: 0x15450
+  __TEXT.__oslogstring: 0x26f23
+  __TEXT.__gcc_except_tab: 0x3244
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0x4265
+  __TEXT.__objc_methname: 0x42b1
   __TEXT.__objc_methtype: 0x530
-  __TEXT.__unwind_info: 0xcd0
-  __DATA_CONST.__const: 0x1540
-  __DATA_CONST.__cfstring: 0x9d60
+  __TEXT.__unwind_info: 0xd08
+  __DATA_CONST.__const: 0x1590
+  __DATA_CONST.__cfstring: 0x9e20
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x9c8
+  __DATA_CONST.__auth_got: 0x9f8
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x11c0
-  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_const: 0x1d88
+  __DATA.__objc_selrefs: 0x11d0
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
-  Functions: 1818
-  Symbols:   389
-  CStrings:  3878
+  Functions: 1833
+  Symbols:   395
+  CStrings:  3891
 
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
