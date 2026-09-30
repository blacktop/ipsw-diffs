## HeuristicInterpreter

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter`

```diff

-615.0.2.0.0
-  __TEXT.__text: 0x16ef4
-  __TEXT.__auth_stubs: 0x600
+617.0.0.0.0
+  __TEXT.__text: 0x16ff0
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0x24c0
   __TEXT.__objc_methlist: 0xac4
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x2333
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x237b
   __TEXT.__objc_classname: 0xcc
   __TEXT.__objc_methname: 0x289b
   __TEXT.__objc_methtype: 0xa35
   __TEXT.__oslogstring: 0xb6f
   __TEXT.__gcc_except_tab: 0xcfc
   __TEXT.__unwind_info: 0x6b8
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x16f0
-  __DATA_CONST.__cfstring: 0x2360
+  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x16c0
+  __DATA_CONST.__cfstring: 0x23a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0639676-2F44-3730-B3F3-17856018438F
+  UUID: E889A834-5F49-33D4-B1AC-79E5009F6053
   Functions: 514
-  Symbols:   198
-  CStrings:  1220
+  Symbols:   201
+  CStrings:  1224
 
Symbols:
+ _SCPreferencesCreate
+ _SCPreferencesGetValue
+ _kCFBooleanTrue
Functions:
~ sub_10000e334 -> sub_10000e3a4 : 32 -> 284
CStrings:
+ "com.apple.proactive.HeuristicInterpreterInternal"
+ "com.apple.radios.plist"

```
