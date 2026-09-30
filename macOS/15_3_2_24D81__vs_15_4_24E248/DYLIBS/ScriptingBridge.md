## ScriptingBridge

> `/System/Library/Frameworks/ScriptingBridge.framework/Versions/A/ScriptingBridge`

```diff

 87.4.0.0.0
-  __TEXT.__text: 0xf2cc
+  __TEXT.__text: 0xf65c
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0xfcc
+  __TEXT.__objc_methlist: 0xff0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0xdde
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x3f8
   __TEXT.__objc_classname: 0x19e
   __TEXT.__objc_methname: 0x1fba
   __TEXT.__objc_methtype: 0x696

   __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x1558
+  __AUTH_CONST.__objc_const: 0x1520
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x70

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74AC1F24-541D-3884-A0F7-EA1D89435393
-  Functions: 336
-  Symbols:   1040
+  UUID: 682BFC48-60D4-3595-8163-933188683557
+  Functions: 354
+  Symbols:   1065
   CStrings:  902
 
Symbols:
+ +[SBCommandThunk thunksForElement:inDocument:].cold.1
+ +[SBElementThunk thunksForElement:inDocument:].cold.1
+ +[SBPropertyThunk thunksForElement:inDocument:].cold.1
+ +[SBPseudoClass alloc].cold.1
+ +[SBPseudoClass classCode].cold.1
+ +[SBPseudoClass pseudoclassWithCode:].cold.1
+ -[SBCommandThunk initWithElement:inDocument:dpIsParameter:].cold.1
+ -[SBElementThunk initWithElement:inDocument:].cold.1
+ -[SBObject setValue:forKey:].cold.1
+ -[SBObject setValue:forKey:].cold.2
+ -[SBObject setValue:forKey:].cold.3
+ -[SBObject valueForKey:].cold.1
+ -[SBObject valueForKey:].cold.2
+ -[SBPropertyThunk initWithElement:inDocument:].cold.1
+ -[SBProxyByClass initWithData:andProperties:].cold.1
+ -[SBProxyByCode initWithData:andProperties:].cold.1
+ -[SBThunk initWithElement:inDocument:].cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ type_matches_application.cold.1
+ type_matches_object.cold.1

```
