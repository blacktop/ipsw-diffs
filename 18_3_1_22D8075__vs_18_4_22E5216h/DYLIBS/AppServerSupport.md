## AppServerSupport

> `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

```diff

-2866.80.6.0.0
-  __TEXT.__text: 0x5894
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x2d3
-  __TEXT.__oslogstring: 0xc91
-  __TEXT.__unwind_info: 0x188
+2894.100.80.0.0
+  __TEXT.__text: 0x58d8
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x4bc
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x2d6
+  __TEXT.__oslogstring: 0xc8e
+  __TEXT.__unwind_info: 0x190
   __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0xd62
-  __TEXT.__objc_methtype: 0x2b2
+  __TEXT.__objc_methname: 0xd87
+  __TEXT.__objc_methtype: 0x2b5
   __TEXT.__objc_stubs: 0x600
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x68

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0xab0
-  __DATA.__objc_ivar: 0x90
+  __AUTH_CONST.__cfstring: 0x120
+  __AUTH_CONST.__objc_const: 0xae0
+  __DATA.__objc_ivar: 0x94
   __DATA.__crash_info: 0x40
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 149
-  Symbols:   291
-  CStrings:  348
+  Functions: 150
+  Symbols:   295
+  CStrings:  350
 
Symbols:
+ _objc_release_x26
+ _objc_retain_x25
CStrings:
+ "%s"
+ "4"
+ "@68@0:8q16i24i28@32@40B48@52@60"
+ "T@\"NSString\",R,C,N,V_program"
+ "assertion failure: \"[[job handle] isEqual:handle]\" -> %llu"
+ "assertion failure: \"_domain != ((void *)0)\" -> %llu"
+ "assertion failure: \"_handle == ((void *)0)\" -> %llu"
+ "assertion failure: \"_monitor_handler != ((void *)0)\" -> %llu"
+ "assertion failure: \"_monitor_handler == ((void *)0)\" -> %llu"
+ "assertion failure: \"_monitor_source == ((void *)0)\" -> %llu"
+ "assertion failure: \"_plist != ((void *)0)\" -> %llu"
+ "assertion failure: \"bundleExecutable != ((void *)0)\" -> %llu"
+ "assertion failure: \"domain != ((void *)0)\" -> %llu"
+ "assertion failure: \"error != 0\" -> %llu"
+ "assertion failure: \"error == 0\" -> %llu"
+ "assertion failure: \"handle != ((void *)0)\" -> %llu"
+ "assertion failure: \"handle\" -> %llu"
+ "assertion failure: \"handler != ((void *)0)\" -> %llu"
+ "assertion failure: \"job != ((void *)0)\" -> %llu"
+ "assertion failure: \"job.handle != ((void *)0)\" -> %llu"
+ "assertion failure: \"kr\" -> %llu"
+ "assertion failure: \"label != ((void*)0)\" -> %llu"
+ "assertion failure: \"manager != ((void *)0)\" -> %llu"
+ "assertion failure: \"monitor_port != 0\" -> %llu"
+ "assertion failure: \"os_reason_code != ((void *)0)\" -> %llu"
+ "assertion failure: \"os_reason_flags != ((void *)0)\" -> %llu"
+ "assertion failure: \"os_reason_namespace != ((void *)0)\" -> %llu"
+ "assertion failure: \"pid != 0\" -> %llu"
+ "assertion failure: \"pid == 0\" -> %llu"
+ "assertion failure: \"pid > 0\" -> %llu"
+ "assertion failure: \"plist != ((void *)0)\" -> %llu"
+ "assertion failure: \"program != ((void*)0)\" -> %llu"
+ "assertion failure: \"status != ((void *)0)\" -> %llu"
+ "assertion failure: \"status == ((void *)0)\" -> %llu"
+ "assertion failure: \"wait4Status != ((void *)0)\" -> %llu"
+ "assertion failure: \"xhandle != ((void*)0)\" -> %llu"
+ "assertion failure: \"xpc_array_get_count(results) == jobs.count\" -> %llu"
+ "assertion failure: \"xpc_get_type(plist) == (&_xpc_type_dictionary)\" -> %llu"
+ "initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:"
- "3"
- "@60@0:8q16i24i28@32@40B48@52"
- "assertion failure: \"[[job handle] isEqual:handle]\" -> %lld"
- "assertion failure: \"_domain != ((void *)0)\" -> %lld"
- "assertion failure: \"_handle == ((void *)0)\" -> %lld"
- "assertion failure: \"_monitor_handler != ((void *)0)\" -> %lld"
- "assertion failure: \"_monitor_handler == ((void *)0)\" -> %lld"
- "assertion failure: \"_monitor_source == ((void *)0)\" -> %lld"
- "assertion failure: \"_plist != ((void *)0)\" -> %lld"
- "assertion failure: \"bundleExecutable != ((void *)0)\" -> %lld"
- "assertion failure: \"domain != ((void *)0)\" -> %lld"
- "assertion failure: \"error != 0\" -> %lld"
- "assertion failure: \"error == 0\" -> %lld"
- "assertion failure: \"handle != ((void *)0)\" -> %lld"
- "assertion failure: \"handle\" -> %lld"
- "assertion failure: \"handler != ((void *)0)\" -> %lld"
- "assertion failure: \"job != ((void *)0)\" -> %lld"
- "assertion failure: \"job.handle != ((void *)0)\" -> %lld"
- "assertion failure: \"kr\" -> %lld"
- "assertion failure: \"label != ((void *)0)\" -> %lld"
- "assertion failure: \"manager != ((void *)0)\" -> %lld"
- "assertion failure: \"monitor_port != 0\" -> %lld"
- "assertion failure: \"os_reason_code != ((void *)0)\" -> %lld"
- "assertion failure: \"os_reason_flags != ((void *)0)\" -> %lld"
- "assertion failure: \"os_reason_namespace != ((void *)0)\" -> %lld"
- "assertion failure: \"pid != 0\" -> %lld"
- "assertion failure: \"pid == 0\" -> %lld"
- "assertion failure: \"pid > 0\" -> %lld"
- "assertion failure: \"plist != ((void *)0)\" -> %lld"
- "assertion failure: \"program != ((void *)0)\" -> %lld"
- "assertion failure: \"status != ((void *)0)\" -> %lld"
- "assertion failure: \"status == ((void *)0)\" -> %lld"
- "assertion failure: \"wait4Status != ((void *)0)\" -> %lld"
- "assertion failure: \"xhandle != ((void *)0)\" -> %lld"
- "assertion failure: \"xpc_array_get_count(results) == jobs.count\" -> %lld"
- "assertion failure: \"xpc_get_type(plist) == (&_xpc_type_dictionary)\" -> %lld"
- "initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:"

```
