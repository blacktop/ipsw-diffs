## JavaLaunching

> `/System/Library/PrivateFrameworks/JavaLaunching.framework/Versions/A/JavaLaunching`

```diff

 325.0.0.0.0
-  __TEXT.__text: 0x5ab4
+  __TEXT.__text: 0x5d9c
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x2b8
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0xcbc
   __TEXT.__oslogstring: 0x404
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__unwind_info: 0xf0
   __TEXT.__objc_classname: 0x3d
   __TEXT.__objc_methname: 0x9b4
   __TEXT.__objc_methtype: 0x162

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94D03636-CEAB-34BF-A048-A672501C8842
-  Functions: 70
-  Symbols:   282
+  UUID: 09076005-A435-3FEB-A8C0-8045632B4459
+  Functions: 90
+  Symbols:   304
   CStrings:  375
 
Symbols:
+ +[JLArchitecture archWithArchString:error:].cold.1
+ +[JLRuntime allRuntimes].cold.1
+ +[JLRuntime filteredRuntimes].cold.1
+ +[JLRuntime runtimeWithJavaHome:error:].cold.1
+ +[JLRuntime supportedRuntimes].cold.1
+ +[NSArray(JLArgv) jl_argumentsForArgv:].cold.1
+ -[JLRuntime initWithName:identifier:javaHome:vendor:platformVersion:version:minSystemVersionString:maxSystemVersionString:error:].cold.1
+ -[JLRuntime initWithName:identifier:javaHome:vendor:platformVersion:version:minSystemVersionString:maxSystemVersionString:error:].cold.2
+ -[JLRuntime initWithName:identifier:javaHome:vendor:platformVersion:version:minSystemVersionString:maxSystemVersionString:error:].cold.3
+ -[JLRuntime initWithName:identifier:javaHome:vendor:platformVersion:version:minSystemVersionString:maxSystemVersionString:error:].cold.4
+ -[JLRuntime initWithName:identifier:javaHome:vendor:platformVersion:version:minSystemVersionString:maxSystemVersionString:error:].cold.5
+ -[JLRuntime initWithName:identifier:javaHome:vendor:platformVersion:version:minSystemVersionString:maxSystemVersionString:error:].cold.6
+ -[JLRuntime reverseOrderByVersion:].cold.1
+ -[JLRuntime reverseOrderByVersion:].cold.2
+ -[JLRuntime spawnTool:arguments:setExec:error:].cold.1
+ -[JLRuntime spawnTool:arguments:setExec:error:].cold.2
+ -[NSArray(JLArgv) jl_argv].cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ jlmacho_iterate_slices.cold.2
+ jlmacho_iterate_slices.cold.3

```
