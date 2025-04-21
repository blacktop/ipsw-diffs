## libexpat.1.dylib

> `/usr/lib/libexpat.1.dylib`

```diff

-42.0.0.0.0
-  __TEXT.__text: 0x17e90
+43.0.0.0.0
+  __TEXT.__text: 0x1818c
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0xc5e
-  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__cstring: 0xd46
+  __TEXT.__unwind_info: 0x2e8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0xb10
+  __DATA_CONST.__const: 0xb18
   __AUTH_CONST.__auth_got: 0x78
   __AUTH_CONST.__const: 0x1960
   - /usr/lib/libSystem.B.dylib
-  Functions: 326
-  Symbols:   653
-  CStrings:  336
+  Functions: 330
+  Symbols:   661
+  CStrings:  344
 
Symbols:
+ _XML_StopParser.cold.1
+ _doProlog.cold.2
+ _internalEntityProcessor.cold.1
+ _processEntity
+ _storeAttributeValue.cold.1
- _processInternalEntity
CStrings:
+ " (+%6ld bytes %s|%u, xmlparse.c:%d) %*s\""
+ "XML_StopParser"
+ "callStoreEntityValue"
+ "expat: Entities(%p): Count %9u, depth %2u/%2u %*s%s%s; %s length %d (xmlparse.c:%d)\n"
+ "expat_2.7.1"
+ "internalEntityProcessor"
+ "parser not started"
+ "parser->m_openAttributeEntities == openEntity"
+ "parser->m_openInternalEntities == openEntity"
+ "parser->m_openValueEntities == openEntity"
+ "storeAttributeValue"
- " (+%6ld bytes %s|%d, xmlparse.c:%d) %*s\""
- "expat: Entities(%p): Count %9d, depth %2d/%2d %*s%s%s; %s length %d (xmlparse.c:%d)\n"
- "expat_2.6.3"

```
