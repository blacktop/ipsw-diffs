## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/Versions/A/SoftwareUpdateCoreConnect`

```diff

-2718.0.18.0.0
-  __TEXT.__text: 0xb4a8
-  __TEXT.__objc_methlist: 0x9c8
+2718.40.13.0.0
+  __TEXT.__text: 0xbed4
+  __TEXT.__objc_methlist: 0xb20
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__cstring: 0xb0a
+  __TEXT.__gcc_except_tab: 0x29c
+  __TEXT.__cstring: 0xc03
   __TEXT.__oslogstring: 0x1de0
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__unwind_info: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x678
+  __DATA_CONST.__objc_selrefs: 0x710
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x1238
+  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__objc_const: 0x1450
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xb4
-  __DATA.__data: 0x360
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 280
-  Symbols:   673
-  CStrings:  152
+  Functions: 309
+  Symbols:   730
+  CStrings:  159
 
Symbols:
+ -[SUCoreConnectClientPolicy conciseLoggingMessages]
+ -[SUCoreConnectClientPolicy debugLoggingMessages]
+ -[SUCoreConnectClientPolicy setConciseLoggingMessages:]
+ -[SUCoreConnectClientPolicy setDebugLoggingMessages:]
+ -[SUCoreConnectClientPolicy setUsesConciseMessageLogging:]
+ -[SUCoreConnectClientPolicy setUsesDebugMessageLogging:]
+ -[SUCoreConnectClientPolicy usesConciseLoggingForMessageName:]
+ -[SUCoreConnectClientPolicy usesConciseMessageLogging]
+ -[SUCoreConnectClientPolicy usesDebugLoggingForMessageName:]
+ -[SUCoreConnectClientPolicy usesDebugMessageLogging]
+ -[SUCoreConnectMessage loggableDescriptionForPolicy:]
+ -[SUCoreConnectMessage loggableLogTypeForPolicy:]
+ -[SUCoreConnectMessage setUsesConciseLogging:]
+ -[SUCoreConnectMessage setUsesDebugLogging:]
+ -[SUCoreConnectMessage usesConciseLogging]
+ -[SUCoreConnectMessage usesDebugLogging]
+ -[SUCoreConnectServerPolicy conciseLoggingMessages]
+ -[SUCoreConnectServerPolicy debugLoggingMessages]
+ -[SUCoreConnectServerPolicy setConciseLoggingMessages:]
+ -[SUCoreConnectServerPolicy setDebugLoggingMessages:]
+ -[SUCoreConnectServerPolicy setUsesConciseMessageLogging:]
+ -[SUCoreConnectServerPolicy setUsesDebugMessageLogging:]
+ -[SUCoreConnectServerPolicy usesConciseLoggingForMessageName:]
+ -[SUCoreConnectServerPolicy usesConciseMessageLogging]
+ -[SUCoreConnectServerPolicy usesDebugLoggingForMessageName:]
+ -[SUCoreConnectServerPolicy usesDebugMessageLogging]
+ OBJC_IVAR_$_SUCoreConnectClientPolicy._conciseLoggingMessages
+ OBJC_IVAR_$_SUCoreConnectClientPolicy._debugLoggingMessages
+ OBJC_IVAR_$_SUCoreConnectClientPolicy._usesConciseMessageLogging
+ OBJC_IVAR_$_SUCoreConnectClientPolicy._usesDebugMessageLogging
+ OBJC_IVAR_$_SUCoreConnectMessage._usesConciseLogging
+ OBJC_IVAR_$_SUCoreConnectMessage._usesDebugLogging
+ OBJC_IVAR_$_SUCoreConnectServerPolicy._conciseLoggingMessages
+ OBJC_IVAR_$_SUCoreConnectServerPolicy._debugLoggingMessages
+ OBJC_IVAR_$_SUCoreConnectServerPolicy._usesConciseMessageLogging
+ OBJC_IVAR_$_SUCoreConnectServerPolicy._usesDebugMessageLogging
+ _SUCoreConnectMessageAppendValue
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUCoreConnectMessageLoggingPolicy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUCoreConnectMessageLoggingPolicy
+ __OBJC_$_PROTOCOL_REFS_SUCoreConnectMessageLoggingPolicy
+ __OBJC_LABEL_PROTOCOL_$_SUCoreConnectMessageLoggingPolicy
+ __OBJC_PROTOCOL_$_SUCoreConnectMessageLoggingPolicy
+ __os_log_debug_impl
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$conciseLoggingMessages
+ _objc_msgSend$debugLoggingMessages
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$loggableDescriptionForPolicy:
+ _objc_msgSend$loggableLogTypeForPolicy:
+ _objc_msgSend$usesConciseLogging
+ _objc_msgSend$usesConciseLoggingForMessageName:
+ _objc_msgSend$usesConciseMessageLogging
+ _objc_msgSend$usesDebugLogging
+ _objc_msgSend$usesDebugLoggingForMessageName:
+ _objc_msgSend$usesDebugMessageLogging
+ _objc_setProperty_atomic_copy
- _objc_msgSend$stringByAppendingFormat:
- _objc_msgSend$stringByAppendingString:
CStrings:
+ ""
+ "%@"
+ "%@%@="
+ "(none)"
+ "(null)"
+ ","
+ "1"
+ "SUCoreConnectClientPolicy(serviceName:%@|clientID:%@|usesConciseMessageLogging:%@|conciseLoggingMessages:%@|usesDebugMessageLogging:%@|debugLoggingMessages:%@)"
+ "SUCoreConnectServerPolicy(serviceName:%@|usesConciseMessageLogging:%@|conciseLoggingMessages:%@|usesDebugMessageLogging:%@|debugLoggingMessages:%@)"
+ "UsesConciseLogging"
+ "UsesDebugLogging"
+ "["
+ "[depth-limit]"
+ "]"
+ "{"
+ "{depth-limit}"
+ "|"
+ "}"
- "\t\t%@\n"
- "\t\t%@: %@\n"
- "\t%@: %@\t]\n"
- "\t%@: %@\n"
- "\t%@: %@\n\t}\n"
- "<<<]"
- "SUCoreConnectClientPolicy(serviceName:%@|clientID:%@)"
- "SUCoreConnectServerPolicy(serviceName:%@)"
- "[\n"
- "[>>>\n"
- "{\n"
```
