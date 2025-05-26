## corerepaird

> `/usr/libexec/corerepaird`

```diff

-376.60.3.0.0
-  __TEXT.__text: 0x3ae4
-  __TEXT.__auth_stubs: 0x470
+397.100.12.0.0
+  __TEXT.__text: 0x3ba8
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x740
-  __TEXT.__objc_methlist: 0xf8
-  __TEXT.__cstring: 0x2f5
-  __TEXT.__oslogstring: 0x692
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__cstring: 0x3b2
+  __TEXT.__oslogstring: 0x62f
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x6e8
-  __TEXT.__objc_methtype: 0x209
+  __TEXT.__objc_methname: 0x6ba
+  __TEXT.__objc_methtype: 0x216
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x124
-  __TEXT.__unwind_info: 0xcc
-  __DATA_CONST.__auth_got: 0x248
+  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__unwind_info: 0xe4
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x728
   __DATA.__objc_selrefs: 0x210
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1f8
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
-  - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 87
-  Symbols:   106
-  CStrings:  221
+  Functions: 89
+  Symbols:   113
+  CStrings:  235
 
Symbols:
+ _dlopen
+ _dlsym
+ _xpc_array_create
+ _xpc_array_set_string
+ _xpc_dictionary_apply
+ _xpc_dictionary_create
+ _xpc_dictionary_get_count
+ _xpc_dictionary_get_dictionary
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
+ _xpc_int64_get_value
- _OBJC_CLASS_$_NSPropertyListSerialization
- _SMCopyAllJobDictionaries
- _SMJobRemove
- _SMJobSubmit
- _objc_enumerationMutation
CStrings:
+ "%s service already %s"
+ "%s: error %lld"
+ "/usr/lib/system/libxpc.dylib"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "Failed to find libxpc API"
+ "T@\"NSString\",?,R,C"
+ "UTF8String"
+ "^v24@0:8r*16"
+ "_xpc_domain_routine"
+ "by-cli"
+ "disable"
+ "dlopen failed"
+ "dlsym(%s) failed"
+ "enable"
+ "errors"
+ "force"
+ "getInnermostNSError:"
+ "getLibXPCInternalWithSymbol:"
+ "handle"
+ "legacy-load"
+ "loaded"
+ "no-einprogress"
+ "paths"
+ "type"
+ "unloaded"
+ "xpc_release"
- "%@ job found"
- "Daemon already running"
- "Daemon not running"
- "Failed to parse plist: %@"
- "Failed to read file: %@"
- "Failed to remove launchd job. Error: %@"
- "Failed to submit launchd job. Error: %@"
- "Label"
- "countByEnumeratingWithState:objects:count:"
- "dataWithContentsOfFile:options:error:"
- "job: %@"
- "propertyListWithData:options:format:error:"

```
