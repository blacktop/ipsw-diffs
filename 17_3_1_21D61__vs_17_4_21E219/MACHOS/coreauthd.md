## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1394.82.1.0.0
-  __TEXT.__text: 0x25bac
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_stubs: 0x2c00
-  __TEXT.__objc_methlist: 0xe34
-  __TEXT.__const: 0xfa4
-  __TEXT.__objc_methname: 0x3bba
-  __TEXT.__cstring: 0x2138
-  __TEXT.__objc_classname: 0x50f
-  __TEXT.__objc_methtype: 0x1a70
-  __TEXT.__oslogstring: 0x1389
+1394.100.151.0.1
+  __TEXT.__text: 0x25b28
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_stubs: 0x2ca0
+  __TEXT.__objc_methlist: 0xe6c
+  __TEXT.__const: 0xfb4
+  __TEXT.__objc_methname: 0x3c38
+  __TEXT.__cstring: 0x21c6
+  __TEXT.__objc_classname: 0x522
+  __TEXT.__objc_methtype: 0x1a75
+  __TEXT.__oslogstring: 0x1391
   __TEXT.__gcc_except_tab: 0x234
   __TEXT.__dlopen_cstrs: 0x9b
-  __TEXT.__unwind_info: 0xa58
-  __DATA_CONST.__auth_got: 0x6c8
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0xa40
+  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2128
-  __DATA_CONST.__cfstring: 0xbe0
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__const: 0x20f8
+  __DATA_CONST.__cfstring: 0xdc0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x2b8
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6678
-  __DATA.__objc_selrefs: 0xd50
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x2b8
-  __DATA.__objc_superrefs: 0x90
+  __DATA.__objc_const: 0x6748
+  __DATA.__objc_selrefs: 0xd78
   __DATA.__objc_ivar: 0x134
-  __DATA.__objc_data: 0x910
+  __DATA.__objc_data: 0x960
   __DATA.__data: 0x12e8
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x178
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 834
-  Symbols:   317
-  CStrings:  1321
+  Functions: 820
+  Symbols:   311
+  CStrings:  1341
 
Symbols:
+ _OBJC_CLASS_$_Caller
+ _OBJC_CLASS_$_LACDTOLocationControllerFactory
+ _calloc
+ _getpid
+ _malloc
- _CFStringCompare
- _LACDarwinNotificationSystemLanguageDidChange
- _OBJC_CLASS_$_LACDTOLocationMonitor
- _OBJC_CLASS_$_LACDTOLocationProviderCRAdapter
- _OBJC_CLASS_$_LACDTOLocationProviderKVSAdapter
- _cccurve25519_make_key_pair
- _ccder_encode_body
- _ccder_encode_tl
- _cced25519_make_key_pair
- _malloc_type_calloc
- _malloc_type_malloc
CStrings:
+ "%@ held by %@[%d]"
+ "@\"<LACDTOLocationController>\""
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "Dumping status information for coreauthd[%u] (user %u)..."
+ "EnvironmentManager"
+ "PID"
+ "Status dump not allowed on production builds"
+ "T@\"NSString\",?,R,C"
+ "YYYY-MM-dd HH:mm:ss:SSS"
+ "_proxiesForContext:"
+ "biometry"
+ "com.apple.private.LocalAuthentication.StatusDump"
+ "context#"
+ "contexts"
+ "controllerWithStore:featureController:eventBus:workQueue:"
+ "coreauthd[%u]"
+ "created"
+ "creationTime"
+ "dumpStatus"
+ "dumpStatusWithCompletion:"
+ "object"
+ "objectEnumerator"
+ "passcode"
+ "pathFromPid:"
+ "process"
+ "proxies"
+ "setDateFormat:"
+ "stringFromDate:"
- "@\"<LACDTOLocationProvider>\"8@?0"
- "@\"LACDTOLocationMonitor\""
- "@\"LACDTOLocationMonitor\"8@?0"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "AuthorizedLocation"
- "CoreRoutine"
- "Should kill daemon because of localization change"
- "_registerObserverForLocalizationChanges"
- "initWithLocationProvider:store:workQueue:"

```
