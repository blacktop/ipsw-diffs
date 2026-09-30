## ActionPredictionHeuristicsInternal

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal`

```diff

-619.8.0.0.0
-  __TEXT.__text: 0x3f040
+619.9.0.1.0
+  __TEXT.__text: 0x3f104
   __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_methlist: 0x29f4
-  __TEXT.__const: 0x328
+  __TEXT.__const: 0x330
   __TEXT.__cstring: 0x31ca
-  __TEXT.__gcc_except_tab: 0xe6c
-  __TEXT.__oslogstring: 0x6d77
+  __TEXT.__gcc_except_tab: 0xe8c
+  __TEXT.__oslogstring: 0x6d8c
   __TEXT.__dlopen_cstrs: 0x1a0
-  __TEXT.__unwind_info: 0xe88
+  __TEXT.__unwind_info: 0xe90
   __TEXT.__objc_classname: 0xc98
-  __TEXT.__objc_methname: 0x7a8b
+  __TEXT.__objc_methname: 0x7a76
   __TEXT.__objc_methtype: 0x1175
   __TEXT.__objc_stubs: 0x6da0
   __DATA_CONST.__got: 0x8c0

   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x498
-  __AUTH_CONST.__const: 0x940
+  __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0x34e0
-  __AUTH_CONST.__objc_const: 0x9b18
+  __AUTH_CONST.__objc_const: 0x9af8
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2fc
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x340
-  __DATA.__bss: 0x2e0
+  __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x100

   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83C13E88-6C49-347D-A4A3-798CBAC3301E
-  Functions: 1192
-  Symbols:   5101
-  CStrings:  2798
+  UUID: 56C4692B-397B-37C6-ACE2-2C2EBEB45108
+  Functions: 1193
+  Symbols:   5106
+  CStrings:  2797
 
Symbols:
+ -[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:].cold.1
+ __ContactCache.contactCache
+ __ContactCache.onceToken
+ __EventDictionaryLRUCache.cache
+ __EventDictionaryLRUCache.onceToken
+ ___78-[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:]_block_invoke.24
+ ____ContactCache_block_invoke
+ ____EventDictionaryLRUCache_block_invoke
+ ___block_literal_global.25
+ ___block_literal_global.31
+ ___block_literal_global.329
+ ___block_literal_global.46
- -[ATXHeuristicDevice dictForEvent:contactCache:].cold.3
- _OBJC_IVAR_$_ATXHeuristicDevice._cachedCalendarDicts
- ___78-[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:]_block_invoke.25
- ___block_literal_global.30
Functions:
~ -[ATXHeuristicDevice initWithLocationManager:] : 140 -> 116
~ -[ATXHeuristicDevice _dictContactForParticipant:contactCache:] : 724 -> 824
~ -[ATXHeuristicDevice dictForEvent:contactCache:] : 528 -> 728
~ -[ATXHeuristicDevice .cxx_destruct] : 140 -> 128
+ ____EventDictionaryLRUCache_block_invoke
~ _OUTLINED_FUNCTION_1 : 20 -> 32
- _OUTLINED_FUNCTION_2
~ -[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:] : 816 -> 828
+ ____ContactCache_block_invoke
~ -[ATXHeuristicDevice dictForEvent:contactCache:].cold.1 : 128 -> 20
~ -[ATXHeuristicDevice dictForEvent:contactCache:].cold.2 : 128 -> 68
- -[ATXHeuristicDevice dictForEvent:contactCache:].cold.3
+ -[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:].cold.1
CStrings:
+ "%s: Cache hit for ekEvent.eventIdentifier: %@"
+ "%s: Cache miss for ekEvent.eventIdentifier: %@"
+ "Found ekEvent with nil eventIdentifier, not using cache"
- "%s: Cache hit for ekEvent.uniqueId: %@"
- "%s: Cache miss for ekEvent.uniqueId: %@"
- "Found ekEvent with nil uniqueId, not using cache"
- "_cachedCalendarDicts"

```
