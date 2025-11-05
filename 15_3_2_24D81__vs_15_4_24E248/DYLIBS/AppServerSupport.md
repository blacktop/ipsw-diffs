## AppServerSupport

> `/System/Library/PrivateFrameworks/AppServerSupport.framework/Versions/A/AppServerSupport`

```diff

-2866.81.1.0.0
-  __TEXT.__text: 0x5c10
+2894.101.1.0.0
+  __TEXT.__text: 0x5c5c
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x317
-  __TEXT.__oslogstring: 0xc91
+  __TEXT.__objc_methlist: 0x4bc
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x31a
+  __TEXT.__oslogstring: 0xc8e
   __TEXT.__unwind_info: 0x178
   __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0xd62
-  __TEXT.__objc_methtype: 0x2b2
+  __TEXT.__objc_methname: 0xd87
+  __TEXT.__objc_methtype: 0x2b5
   __TEXT.__objc_stubs: 0x600
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x40

   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x50
-  __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0xab0
+  __AUTH_CONST.__cfstring: 0x120
+  __AUTH_CONST.__objc_const: 0xae0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_ivar: 0x94
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0745B4D-38C0-34C4-AA05-8D4D274874F5
-  Functions: 150
-  Symbols:   402
-  CStrings:  351
+  UUID: A9D81D27-5D5E-3D6F-BC5F-7D52119E102F
+  Functions: 151
+  Symbols:   405
+  CStrings:  354
 
Symbols:
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:]
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.1
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.10
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.11
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.2
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.3
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.4
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.5
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.6
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.7
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.8
+ -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:].cold.9
+ -[OSLaunchdJobInfo program]
+ OBJC_IVAR_$_OSLaunchdJobInfo._program
+ __64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.33
+ _objc_msgSend$initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:
+ _os_launch_job_log.cold.1
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:]
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.1
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.10
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.11
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.2
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.3
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.4
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.5
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.6
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.7
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.8
- -[OSLaunchdJobInfo initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:].cold.9
- __64-[OSLaunchdJob _setupMonitorSourceWithPort:onQueue:withHandler:]_block_invoke.30
- _objc_msgSend$initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:
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
